# SIGNALS — SENTRY Working Directory

> ⚠️ **FROZEN 2026-08-11 — dead surface, do not cite as current.** SENTRY was retired/archived 2026-06-27 (`PROME/ROSTER.md` RETIRED section) and this feed pipeline died with the VPS cron; last inbound item is 2026-06-02. **The workflow and scripts this README describes below NO LONGER EXIST in the tree — `.github/workflows/feeds.yml` deleted and `scripts/fetch_feeds.py` + `requirements.txt` moved to `archive/SENTRY_pipeline/` (WQ-127, 2026-08-29); read the body as history.** **Successor for always-on signal collection = the RESEARCH-INTAKE lane** (GitHub Actions repo `williepowen-debug/RESEARCH-INTAKE`; WALTER consumes). WALTER's boot step 7c already tombstones this as a dead feed — this banner puts the tombstone on the artifact itself (PAT-057 class). Retirement owner: PROME. Rewrite trigger: archive the directory wholesale at the next Will-approved deletion pass.

This directory is owned by **SENTRY** (Cross-domain signals analyst, `AGENTS/SENTRY/`).

## Contents

| Path | Purpose | Writer |
|------|---------|--------|
| `feeds.yml` | RSS/Atom feed config | Will (proposes), SENTRY |
| `inbound.md` | Latest raw feed items, last 48h | GitHub Action (`scripts/fetch_feeds.py`) |
| `seen.json` | Deduplication state | GitHub Action |
| `briefings/` | SENTRY's morning/evening/adhoc briefings | SENTRY |
| `archive/` | Monthly rotation of inbound + old briefings | SENTRY |

## Pipeline

`scripts/fetch_feeds.py` runs twice daily via `.github/workflows/feeds.yml` (10:00 UTC / 22:00 UTC ≈ 6 AM / 6 PM ET). It pulls each enabled feed in `feeds.yml`, deduplicates against `seen.json`, and rewrites `inbound.md` with items from the last 48 hours.

Manual run:
```bash
cd /home/willi/Research-workspace
source .venv/bin/activate
python3 scripts/fetch_feeds.py
```

## Edit boundaries

- **SENTRY** owns this directory: rewrites `inbound.md`/`seen.json` via the script, writes briefings, manages archive rotation.
- **Will** proposes feed additions/removals via `AGENTS/SENTRY/proposals.md`; SENTRY does not autonomously add data sources.
- **Other agents** read `briefings/` as published. They do not write here.

## Scope note

This directory previously held a draft Prome-managed signal-routing depot (`agents/{HAWK,BRENT,...}/`, `images/`, etc.). That model never materialized — the Apr 30 README has been replaced. Image/screenshot routing now lives with WALTER on Telegram. If a fleet-wide raw-signal depot is revived later, it should live elsewhere (e.g. `AGENTS/HERMES/` or its successor) so SIGNALS/ stays scoped to SENTRY's pipeline.

---
*Owned by SENTRY since 2026-05-07.*
