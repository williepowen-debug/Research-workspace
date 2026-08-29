# SENTRY feed pipeline — RETIRED 2026-08-29 (Will-ruled WQ-127, verbatim "okay go ahead retire it")

**What this was:** `.github/workflows/feeds.yml` (removed from the tree this commit; `git log --all -- .github/workflows/feeds.yml` has it) ran `fetch_feeds.py` twice daily on GitHub Actions, committing `SIGNALS/inbound.md` + `seen.json` straight to `master`. Two feeds enabled at the end: EIA *Today in Energy* RSS and the SEC EDGAR current-filings Atom.

**Why retired:** schedule disabled 2026-06-02 (bot pushes to master = the concurrent-writer collision canon prevents); SENTRY dormant 2026-06-27; `SIGNALS/` FROZEN 2026-08-11; successor = the **RESEARCH-INTAKE** repo (6 collectors, weekday-daily, own repo, WALTER consumes since 7/2). Never dispatched after 6/2.

**Gap found at retirement:** RESEARCH-INTAKE does NOT carry the EIA *Today in Energy* RSS (`https://www.eia.gov/rss/todayinenergy.xml`) — its EIA collector is the petroleum data API and its news sweep is Google-News-query based. Flagged to WALTER/Will for a one-source add on the intake side.

Files here are verbatim from `scripts/` at retirement. `scripts/env_doctor.py` and `AGENTS/DAEDALUS/CHECKS.tsv` still mention the old paths in prose/registry rows (DAEDALUS-owned; packeted).
