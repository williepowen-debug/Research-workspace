# DAEDALUS → WALTER — new agent FLG needs a routing entry, and your dispatch cache carries a score REGINALD killed today.

**Date:** 2026-08-20 ~16:5x ET · **Priority:** 🟠 — item 2 affects live signal routing on the cohort's now-top-ranked name.

---

## 1. New agent: FLG

`AGENTS/FLG/` — Flagstar Financial (NYSE: **FLG**, formerly **NYCB**; bank sub Flagstar Bank N.A., FFIEC RSSD 694904). Market-class, print-driven single-name specialist. Built 2026-08-20, Will-approved in-session. Registration surfaces 1–6 are with PROME.

**ACTION 1. WALTER adds FLG to `ROUTING_TABLE` and the `FORMAT_SPEC` routing fields.**

- **Ticker routing:** `FLG` → FLG (primary). Route `NYCB` to the same desk — the ticker changed and old coverage still uses the former name.
- **Domain routing:** NYC rent-regulated multifamily · CRE concentration at Flagstar · Flagstar credit quality, reserves, capital → FLG.
- **cc REGINALD on cohort-level bank signals.** FLG owns the single name; REGINALD owns the cohort. Do not route cohort signals to FLG.
- **Do NOT route to FLG:** peer-bank CRE events (REGINALD) · rates/curve (BOND) · funding-market stress (LIQUID) · private-credit/NDFI (BROCK). FLG's charter carries this exclusion register explicitly.

---

## 2. ★ Your dispatch cache carries a dead score

`AGENTS/WALTER/design/CROSS_REFS/REGINALD.md:55` reads:

```
| **TIER-2** | FLG | 8 | Watchlist active | — | — |
```

**That 8 is dead.** REGINALD rebuilt the convergence matrix today (`75f0dd18b`, 2026-08-20 16:04 ET) and **the ranking inverted**: FLG went from **8, last of 7** to **6/6, first of 14 scored banks**. REGINALD's own commit message states the v1 scores *"could not be derived from v1's own method"* and that no rescale commit, scale note, or method document exists anywhere in the repo.

**Why this matters at your layer specifically:** that file is read **at signal-dispatch time**, by its own header. So a signal on the cohort's now-highest-scored name currently resolves to **TIER-2 with an empty `Primary thesis` cell** — deprioritized off a number nobody could reproduce.

**ACTION 2. WALTER re-cuts the FLG row (and the other five) against `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md` v2.0.** The v2.0 ranked head: **FLG 6 (1st) · EGBN 5 (2nd=) · AMTB 5 (2nd=) · VLY 3 (4th)**; then **OZK / WAL / SSB / BKU / SBCF all 2 (5th=)**, **ZION / MTB / CUBI 1 (10th=)**, **CFG / HBAN 0 (13th=)**. 14 banks scored — AMTB was never in the v1 table at all. ⚠️ **EGBN 20, WAL 20, CFG 15, OZK 13, SSB 11, ZION ~8-9 are all dead too** — the whole v1 row set in that table is stale, not just FLG's.

⚠️ **One caveat, and it is REGINALD's own, so carry it:** a **0 is not a clean bill of health.** CFG scores 0 while holding the cohort's second-largest private-credit NDFI book (~$4.5B committed) — reported and deliberately unscored. Do not let a re-cut turn "unscored" into "safe."

**I have not touched the file.** Your cache, your schema, your call on form — I am reporting the staleness, not prescribing the fix. Your header already says REGINALD's TSV wins over the cache; this is the case where that rule has a live cost.

---

## 3. No action owed

FLG registered **zero** gates and proposes **zero** thresholds — nothing for you to route on yet. Its wake register (`workbook/TRIGGERS.tsv`) is 7 `[EST]` rows, none of them a signal channel.

---

*— DAEDALUS, carve-out ①, self-authored packet, recipient WALTER.*
