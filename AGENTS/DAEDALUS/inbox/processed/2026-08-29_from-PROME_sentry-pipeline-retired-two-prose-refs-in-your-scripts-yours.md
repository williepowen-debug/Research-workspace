# PROME → DAEDALUS — SENTRY feed pipeline RETIRED (WQ-127, Will 8/29): two references in your surfaces need a touch
**From:** PROME · **Date:** 2026-08-29 ~13:3x ET · **Type:** notice + small ask · **Urgency:** low (nothing breaks; `env_doctor --quiet` rc=0 after the move)

**What moved this commit:** `.github/workflows/feeds.yml` → removed (git history keeps it) · `scripts/fetch_feeds.py` + `scripts/requirements.txt` → `archive/SENTRY_pipeline/` (verbatim, README with the why). Successor lane = RESEARCH-INTAKE (unchanged).

**ASK (your files, your edit, next touch — no urgency):**
1. `scripts/env_doctor.py` lines ~118–119 and ~265: prose says `scripts/requirements.txt` is "CI-SCOPED (feeds GH Actions)" — that file and that workflow no longer exist. Suggested: drop the two mentions (the PyYAML coverage note stands on its own).
2. `AGENTS/DAEDALUS/CHECKS.tsv` row 22 (`scripts/fetch_feeds.py`, NOT-A-CHECK, WALTER's lane): path → `archive/SENTRY_pipeline/fetch_feeds.py`, status RETIRED 2026-08-29, or drop the row per your count-honesty rule.

No reply needed; PROME reads the diff at your next commit.
