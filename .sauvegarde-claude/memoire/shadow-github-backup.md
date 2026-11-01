---
name: shadow-github-backup
description: The The Shadow project is backed up to the private GitHub repo salfab/the-shadow-pinball-troubleshoot; run sauvegarde.ps1 at the end of each session
metadata:
  node_type: memory
  type: project
  originSessionId: 67a0b140-c89f-4ca5-be8f-b924fa2c867f
  modified: 2026-10-26T06:09:44.816Z
---

On 2026-10-26 the user asked to back up the whole project to a private GitHub repo, so nothing is lost if their disk crashes. They allowed binaries (photos, PDFs) in the repo.

- Repo: https://github.com/salfab/the-shadow-pinball-troubleshoot (private, branch `main`).
- It holds the project files: journal, carnet, `docs/`, `photos/`.
- It holds a copy of the `.remember/*.md` notes in `.sauvegarde-claude/remember/`. Never track `.remember/` itself in git: the Remember plugin refuses to inject notes that git tracks (seen 2026-11-01).
- It also holds `.sauvegarde-claude/`:
  - `memoire/`: a mirror of this memory folder;
  - `sessions/`: the session transcripts, split into 40 MB `.partNNN` files above that size;
  - `temp/`: the session scratchpads.
- A `.ignore` file keeps ripgrep out of `.sauvegarde-claude/`.

**Why:** the user fears losing the diagnostic work, the project memory and the session history. Claude Code also deletes local transcripts after 30 days by default.

**How to apply:**
- At the end of each session, first update the journal, `carnet-de-bord.md` and memory. Then run `pwsh -File sauvegarde.ps1` from the project root; it copies, commits and pushes.
- Commit messages must not carry a `Co-Authored-By` trailer (the user's global rule).
- Restore steps are in the repo's `README.md`.

See [[shadow-blog-work-log]].
