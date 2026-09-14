# WALTER local drop-zone (`inbox/WILL/`)

**Desktop-only signal intake.** Will drops signal images/screenshots here; WALTER reads them directly (full-res, original filenames) and routes — an alternative to Telegram for bulk desktop batches.

- **Gitignored** — raw drops never touch the shared repo (bloat + often sensitive). Only this README + `.gitkeep` + `.gitignore` are tracked.
- **Boot-surfaced** — WALTER counts/lists new files at boot (gitignored ⇒ invisible to `git status`, so the boot-step is the only discovery path).
- **`processed/`** — after routing, consumed images move here so the active count returns to 0 (also gitignored). 🔴 **THE EXECUTABLE HOME OF THIS RULE IS BOOT STEP 7f IN `AGENTS/WALTER/CLAUDE.md`, NOT THIS LINE.** From 2026-07-06 to 2026-09-14 it lived ONLY here — and no boot step opens this README (7f reads the directory LISTING) — so on 9/14 a batch closed 47/47 while all 47 images stayed put and the next boot read them as a fresh backlog. ⚠️ **If you are editing this line, edit 7f in the same commit; a rule that lives only in a file nobody travels is not in force.**
- **Desktop-local** — Telegram remains the from-phone/anywhere path. This complements, doesn't replace, it.

Pattern mirrors TERRY's `inbox/WILL/` (finding_gitignored_private_drop_boot_surfaced).
