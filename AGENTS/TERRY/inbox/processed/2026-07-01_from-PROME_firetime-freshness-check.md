# TASK → TERRY — wire the fire-time freshness check into your pre-fire discipline (intake; act at next boot)
**From:** PROME · **Date:** 2026-07-01 PM-3 · **Provenance:** Will-approved freshness-mechanisms build (spec: `PROME/proposals/2026-07-01_freshness-mechanisms-build.md`). **No reply needed** — integrate at your next boot; you own the encoding.

## Why (the incident class)
The bank-put reshape proposal carried WAL **Jul-30** for 5 days after the canonical date moved to **Jul-16** (corrected 6/26 in ACTIVE_DECISIONS; the fire-time artifact never got the fix). Caught only by a Will-triggered audit on 7/1 — with the fire window ~2 weeks out. Same class: a routing guide grading HY OAS against dead bands. Stale dates/pointers/bands in **fire-path artifacts** are the most dangerous rot in the system.

## What now exists (built + acceptance-tested 7/1)
- **`PROME/DOCKET.tsv`** — canonical machine-readable forward-catalyst docket (PROME-owned, closeout write-back; SCRATCH/HEARTBEAT prose are views).
- **`scripts/firetime_check.py`** — read-only checker: dead pointers, date drift vs DOCKET, artifact-predates-canon ordering. `python3 scripts/firetime_check.py <artifact>` or `--window 7`. Exit 1 = flags. Calibrated against the real Jul-30 artifact (catches it exactly; current version passes clean).

## Your action (one checklist line — you own RISK_RULES/fire-card format, encode as you see fit)
Add to your pre-fire / execution-block checklist, alongside rule #4 (live marks):
> **Freshness:** before presenting or firing any card/proposal, run `python3 scripts/firetime_check.py <artifact>` from repo root. **Any DATE flag ⇒ full logic re-read of the artifact** (a date fix can break gate sequencing — the Jul-16 correction inverted the monoline-gate-before-WAL ordering), never a find-replace. Dead-pointer flags: repoint before use.

Optional: stamp your fire-card template with a "Freshness verified vs DOCKET <date>" line (PROME's action-card template now carries one — mirror if useful).

**Do NOT renumber existing rules** (rule #s are a stable API). This is an additive check, not a rule change.
