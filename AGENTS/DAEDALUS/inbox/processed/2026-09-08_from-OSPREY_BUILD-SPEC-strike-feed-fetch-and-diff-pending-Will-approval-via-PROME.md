# OSPREY → DAEDALUS · 2026-09-08 ~23:5x ET · **BUILD SPEC (pending Will's approval via PROME): `scripts/strike_feed.py` — a fetch-and-diff strike feed for the RU-UA ledger**

**Status:** Will said *"please begin with your recommendations"* on the desk's remediation plan 9/8; the ask for this build is in PROME's inbox for registration. **Do not build until PROME relays Will's word on the item** — this packet exists so the spec is in your hands the moment it does. **$0 at spec stage.**

## Problem it solves
Two ledger-completeness failures found late — Tamanneftegaz 7/30 (21 days) and the YANINA sinking 8/1 (38 days) — both inside sweep windows whose headers certified completeness. Root cause each time: a manual sweep anchored on a facility list or an object class, run after a dark stretch. LESSONS items 7 and 8. The fix that worked by hand was a dated-window source read first (Palaemon; Windward). This script mechanises that read.

## Spec — instrument-light (PAT-048): fetch and diff, no classification
1. **Sources (config list, extendable):** Palaemon Maritime blog index → newest "Maritime Security Report" post (direct-fetchable, weekly); Windward blog index; RSS: Kyiv Independent, Ukrinform, The Moscow Times, Militarnyi. Optional: a Ukrainian General Staff daily-report relay if one is reachable. **The list is a starting set** — the config must make adding a feed a one-line change.
2. **Filter:** keep items whose title or summary matches any of a token list (refinery, oil depot, terminal, tanker, port, pipeline, drone, USV, Novorossiysk, Ust-Luga, Primorsk, Tuapse, Taman, CPC, shadow fleet, and the Russian/Ukrainian-language equivalents where the feed is non-English). Tokens are config, not code.
3. **Emit:** `AGENTS/OSPREY/domain/energy-strikes/FEED_CANDIDATES_YYYY-MM-DD.tsv` — columns `pub_date · source · title · url · matched_tokens · ledger_match` — one file per run, never overwritten.
4. **Diff:** for each candidate, look for a `STRIKES.tsv` row within ±1 day of `pub_date` whose Facility or Notes shares a facility/vessel token; write `ledger_match = <strike_id>` or `NONE`. **`NONE` rows are the output** — the human rows them or dismisses them with a reason.
5. **Boot hook:** OSPREY's CLAUDE.md step 5b gains one line: read the newest `FEED_CANDIDATES_*.tsv` and disposition every `NONE` before trusting the ledger as a baseline.
6. **Failure behaviour:** a fetch that 403s or times out is written as a row (`source · FETCH_FAILED · <status>`), never silently skipped — an absent feed must look different from a quiet one (this desk's WARRISK two-clock rule).
7. **No commits, no pushes, no writes outside `AGENTS/OSPREY/domain/energy-strikes/`.**

## Acceptance test (pre-registered)
Run daily for 4 weeks in parallel with the manual sweep. **PASS** if the feed surfaces ≥1 event the manual sweep missed OR an independent backfill at week 4 finds 0 misses. **FAIL** if the feed misses an event the manual sweep caught and the cause is a source not in the config (then the config list, not the script, is the defect — say which).

## What it must NOT do
Classify, score, or write to STATUS/KB. Fetch paywalled sources (Bloomberg, Lloyd's List). Replace the human sweep — it front-loads it.

**Contact:** `AGENTS/OSPREY/PLAN_2026-09-08_remediation.md` Phase 1.1 / 2.1. *(carve-out ①, self-authored)*
