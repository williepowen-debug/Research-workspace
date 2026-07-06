# WALTER local drop-zone (`inbox/WILL/`)

**Desktop-only signal intake.** Will drops signal images/screenshots here; WALTER reads them directly (full-res, original filenames) and routes — an alternative to Telegram for bulk desktop batches.

- **Gitignored** — raw drops never touch the shared repo (bloat + often sensitive). Only this README + `.gitkeep` + `.gitignore` are tracked.
- **Boot-surfaced** — WALTER counts/lists new files at boot (gitignored ⇒ invisible to `git status`, so the boot-step is the only discovery path).
- **`processed/`** — after routing, consumed images move here so the active count returns to 0 (also gitignored).
- **Desktop-local** — Telegram remains the from-phone/anywhere path. This complements, doesn't replace, it.

Pattern mirrors TERRY's `inbox/WILL/` (finding_gitignored_private_drop_boot_surfaced).
