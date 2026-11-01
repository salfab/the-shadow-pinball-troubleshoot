# Bally *The Shadow* — diagnostic et réparation

Dépôt **privé** : sauvegarde du diagnostic de la Power Driver (A-12697-3) et de tout le travail fait avec Claude.

| Contenu | Où |
|---|---|
| Journal technique : mesures, hypothèses, checklist | `journal-diagnostic-the-shadow.md` |
| Carnet de bord : récit des séances, futur article | `carnet-de-bord.md` |
| Manuel complet en PDF (183 pages, reconstitué depuis la version en ligne de Planetary Pinball) | `docs/manuel-the-shadow/manuel-The-Shadow_16-50032-101_complet.pdf` |
| Pages utiles du manuel, schémas, théorie WPC | `docs/` |
| Photos et images annotées | `photos/` |
| Mémoire Claude du projet | `.sauvegarde-claude/memoire/` |
| Transcriptions des sessions Claude | `.sauvegarde-claude/sessions/` |
| Fichiers de travail des sessions (scripts d'annotation, extraits du manuel) | `.sauvegarde-claude/temp/` |
| Notes du plugin Remember (fichiers `.md` seulement) | `.remember/` |

## Dépendances

- [Claude Code](https://claude.com/claude-code), avec un compte connecté.
- Le plugin **Remember** (`remember@claude-plugins-official`) : il tient les notes de séance dans `.remember/` et les relit au début de chaque conversation. Pour l'installer : `/plugin install remember@claude-plugins-official` dans Claude Code.
- Git et l'outil GitHub `gh`, connecté au compte (`gh auth login`), pour cloner le dépôt et lancer `sauvegarde.ps1`.
- PowerShell 7 (`pwsh`) pour le script de sauvegarde, et Python avec Pillow et PyMuPDF pour les scripts d'annotation d'images (`.sauvegarde-claude/temp/…/scripts/`).

## Mettre la sauvegarde à jour

```
pwsh -File sauvegarde.ps1
```

Le script recopie la mémoire, les transcriptions et les fichiers de travail dans `.sauvegarde-claude/`, puis fait un commit et un push. Les transcriptions ne sont jamais effacées de la sauvegarde, même quand Claude Code supprime les siennes (après 30 jours par défaut).

## Restaurer après un crash

1. Cloner le dépôt **au même chemin**, car Claude Code range la mémoire d'un projet d'après son chemin :
   `git clone https://github.com/salfab/the-shadow-pinball-troubleshoot.git C:\sources\the-shadow-pinball-troubleshoot`
2. Copier le contenu de `.sauvegarde-claude\memoire\` dans `%USERPROFILE%\.claude\projects\C--sources-the-shadow-pinball-troubleshoot\memory\`.
3. Pour retrouver l'historique des sessions (`claude --resume`), copier aussi `.sauvegarde-claude\sessions\` dans `%USERPROFILE%\.claude\projects\C--sources-the-shadow-pinball-troubleshoot\`. Une transcription de plus de 40 Mo est découpée en morceaux `.part001`, `.part002`…, car GitHub refuse les fichiers de plus de 100 Mo. Il faut les recoller dans l'ordre, par exemple dans Git Bash : `cat <session>.jsonl.part* > <session>.jsonl`, puis supprimer les morceaux.
