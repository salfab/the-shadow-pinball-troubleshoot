# Sauvegarde du projet sur GitHub (dépôt privé).
# Recopie dans .sauvegarde-claude/ la mémoire Claude du projet, les transcriptions des
# sessions et leurs fichiers de travail, puis fait un commit et un push.
# Usage : pwsh -File sauvegarde.ps1 [-Message "message de commit"]
param([string]$Message = "Sauvegarde du $(Get-Date -Format 'yyyy-MM-dd HH:mm')")
$ErrorActionPreference = 'Stop'

$depot  = $PSScriptRoot
$cle    = 'C--sources-the-shadow-pinball-troubleshoot'   # dossier de Claude Code pour ce projet
$projet = Join-Path $HOME ".claude\projects\$cle"
$temp   = Join-Path ([IO.Path]::GetTempPath()) "claude\$cle"
$dest   = Join-Path $depot '.sauvegarde-claude'
$limite = 40MB   # GitHub refuse les fichiers de plus de 100 Mo

# Garde-fou : sur une machine pas encore restaurée, ne pas vider la mémoire sauvegardée.
if (-not (Test-Path (Join-Path $projet 'memory\MEMORY.md'))) {
    throw "Mémoire Claude introuvable dans $projet : la restaurer d'abord (voir README.md)."
}

# 1. Mémoire : copie exacte ; une mémoire supprimée disparaît aussi de la sauvegarde.
robocopy (Join-Path $projet 'memory') (Join-Path $dest 'memoire') /MIR /NJH /NJS /NFL /NDL /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy (mémoire) : code $LASTEXITCODE" }

# 2. Transcriptions : jamais effacées de la sauvegarde (Claude Code supprime les siennes
#    après 30 jours). Au-delà de $limite, découpées en .part001, .part002… Lecture en
#    partage, car la session en cours écrit encore dans sa transcription.
function Copier-Transcription([string]$source, [string]$cible) {
    Remove-Item -Path $cible, "$cible.part*" -ErrorAction Ignore
    $flux = [IO.File]::Open($source, 'Open', 'Read', 'ReadWrite')
    try {
        if ($flux.Length -le $limite) {
            $sortie = [IO.File]::Create($cible)
            try { $flux.CopyTo($sortie) } finally { $sortie.Dispose() }
            return
        }
        $tampon = [byte[]]::new($limite)
        for ($n = 1; ; $n++) {
            $lus = 0
            while ($lus -lt $limite -and ($r = $flux.Read($tampon, $lus, $limite - $lus)) -gt 0) { $lus += $r }
            if ($lus -eq 0) { break }
            $sortie = [IO.File]::Create(('{0}.part{1:000}' -f $cible, $n))
            try { $sortie.Write($tampon, 0, $lus) } finally { $sortie.Dispose() }
            if ($lus -lt $limite) { break }
        }
    } finally { $flux.Dispose() }
}
Get-ChildItem $projet -Recurse -File |
    Where-Object { $_.FullName -notlike "$projet\memory\*" } |
    ForEach-Object {
        $cible = Join-Path $dest ('sessions' + $_.FullName.Substring($projet.Length))
        New-Item -ItemType Directory -Force (Split-Path $cible) | Out-Null
        Copier-Transcription $_.FullName $cible
    }

# 3. Fichiers de travail des sessions (scratchpad) : ajout seul, comme les transcriptions.
if (Test-Path $temp) {
    robocopy $temp (Join-Path $dest 'temp') /E /XD __pycache__ /NJH /NJS /NFL /NDL /NP | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy (temp) : code $LASTEXITCODE" }
}

# 4. Commit et push.
git -C $depot add -A
if ($LASTEXITCODE) { throw 'git add a échoué' }
# Notes du plugin Remember : son dossier s'exclut lui-même de git (.gitignore « * ») ;
# on force l'ajout des notes .md, sans ses fichiers techniques (tmp/, logs/).
if (Test-Path (Join-Path $depot '.remember\*.md')) {
    git -C $depot add -f -- '.remember/*.md'
    if ($LASTEXITCODE) { throw 'git add (.remember) a échoué' }
}
if (git -C $depot status --porcelain) {
    git -C $depot commit -q -m $Message
    if ($LASTEXITCODE) { throw 'git commit a échoué' }
} else {
    Write-Host 'Rien de nouveau à sauvegarder.'
}
git -C $depot push -q -u origin main
if ($LASTEXITCODE) { throw 'git push a échoué' }
Write-Host 'Sauvegarde envoyée sur GitHub.'
