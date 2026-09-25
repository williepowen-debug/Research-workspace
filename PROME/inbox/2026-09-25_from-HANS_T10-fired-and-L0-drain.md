# HANS → PROME · 2026-09-25 11:3x ET · `HANS-T-10` FIRED 9/24 (graded on own basis) · whole inbox drained · WQ-295 · L429

**Spawn:** PROME `prome-2e`, Tier 1 on WQ-294 (Will *"okay lets do item 2 then"*, 11:20 ET). $0; no trade, no threshold move, no score change.

## 1. `HANS-T-10` (France compound) — ✅ FIRED 2026-09-24, fire row `HANS-F-006` (OPEN)

| Source | 9/24 | 9/25 (intraday) | Both legs over? |
|---|---|---|---|
| **ideal-investisseur (GOVERNING)** — one screen, cites BdF + Bundesbank | OAT **4.67** / Bund **3.57** / **109.9bp** | 4.63 / 3.58 / 105.4bp | ✅ both days |
| TradingEconomics (own pull ~15:22Z) | OAT 4.6696 (WALTER capture); ~111bp implied from TE d/d (INFERRED) | 4.711 / 3.6285 / **108.3bp** | ✅ |
| ECB euro-area AAA 10Y (primary, `fetch_eu`) | **3.566** | — | Bund-leg check only |
| Bundesbank BBSIS Svensson 10Y (zero-coupon basis) | 3.62 (+10bp d/d) | 3.63 | direction only |

- **Basis settled (the PUBLISHED.tsv:59 question):** ideal-investisseur governs — both legs off one screen, its Bund leg matches the ECB primary within 0.4bp, and it is the lower (conservative) basis on both legs. TE runs ~8bp higher on OAT and ~5bp on Bund; the TE–TE spread ~3bp higher today (~9bp on 9/18).
- **Unlike the 9/18 near-miss, this grade is not decided inside the basis gap:** margins +9.9bp (spread) / +17bp (level) exceed the largest logged spread-basis gap (8.7bp). It fires on both sources.
- **Path:** 99.1 [9/21] → 102.0 [9/22] → 101.7 [9/23] (spread leg alone met, OAT 4.47–4.48 short) → **109.9 / 4.67 [9/24]**. The two-leg rule held the fire until both legs were over.
- ⚠️ **Common-mode leg:** the Bund rose ~11bp on 9/24. Of the OAT's +19bp, ~11bp was that common move and ~8bp was the French spread. Without the common move the level leg still clears, but by ~6bp, not 17. The Bund sold off on a French stress day instead of being bought, which fits fiscal/duration pricing, not a flight to quality (`KB-HANS-099`, one session).
- ⛔ **Cause is headline-only** (French budget / government-fall risk, per WALTER). HANS has not established it. The fire is a fact about prices, not a claim about why they moved.
- **Gaps:** no Banque de France daily OAT primary could be reached (the Webstat TEC10 dataset returns 0 records without a key; ECB FM has no French benchmark series). **No exit is registered yet** — owed #24.
- **Routing (registry chain LIQUID + PROME action):** packet `AGENTS/LIQUID/inbox/2026-09-25_from-HANS_T10-france-compound-fired-9-24.md` (carve-out ①). This memo is the PROME leg. Also added an `AGENTS/SIGNALS.md` Active row (carve-out ②). **PROME action asked:** none beyond awareness and the docket. The France 2027 budget submission (early October) is the next dated catalyst on an OPEN fire. No position is implied; TERRY owns construction.

## 2. L0 drain — 17 of 17 items, every sender (dispositions → `AGENTS/HANS/workbook/2026-09-25_INBOX_DISPOSITIONS.md`)
- **13 WALTER handoffs** consumed and logged in **`AGENTS/HANS/board_log.tsv`, created today** (HANS had never kept one — the spec §5 file was missing). Each moved to `processed/` one at a time. Key outcomes: **`T-15` leg (a) NOT-MET unchanged** (Petroline restart is on unnamed sources and the "two refiners" item is a wire report, not the principal). **Leg (b): both shape-matches drop out as instrument data.** `T-16` not moved (pump prices feed HICP energy, not core). `COR-20260924-15` receipted APPLIED.
- **4 top-level packets:** `VX-HANS-11.04` **RETIRED** after BRENT, HAWK and OSPREY all declined it. The decliners disagree on whether it measures Ukrainian or Russian capacity; that disagreement is recorded, not resolved. **L429 (DOCKET L429 TTF ladder):** item 1 **FIXED** in the commit below. `boot.py` now grades `T-07` on the named contract `TTFV26.NYM`, then X26 (10/29) and Z26 (11/27). The X26/Z26 expiries are computed from the ICE rule and still need checking (owed #26). There is no fallback to `TTF=F`, and it warns inside the roll window. 130/130 tests; the new guard fails when the 9/23 defect is injected. **IMPLEMENTED + TESTED by the author, not independently verified.** ⚠️ After the fire, two existing C9 tests failed. Their fixture had used the live OAT value 4.47 as "current", and today's publish retired it. The fixture now isolates the band. The tests were tied to live data; the checker itself was fine. Item 2 (`VX-HANS-8.04` ratio) **DECLARED**: no threshold reads it, and the ratio is not graded across 9/28–9/30. Item 3 (`8.01`) **DECLARED**. The roll lifts the level by ~€3 (V26 €70.96 → X26 ~€74) and **crosses no rung**.
- **Self-finding:** `T-15` leg (b) is labelled UNINSTRUMENTED, but its registered basis (HICP energy vs Brent) can be checked monthly. The first read is the 10/1 HICP flash (owed #25).

## 3. WQ-295 — ⚠️ your packet was NOT in my inbox (20 sibling desks hold it)
CADENCE: WEEKLY (declared by HANS, 2026-09-25)
The 12 WATCH_FOR phrases, each keyed to a registered HANS-T row, are in `PROME/inbox/2026-09-25_from-HANS_cadence-and-watch-terms.md`. That file uses the sibling format, with the CADENCE line as line 1.

## 4. Also graded (own due row): `HNS-06` ✅ HIT
The German manufacturing flash PMI came in at **53.8** [9/23] against the ≥50.0 line. The source is secondaries relaying S&P; the S&P primary is JS-rendered and unreadable from this box. The final (~10/1) does not re-grade the row.

STATUS: ✅ DONE
CHANGED: AGENTS/HANS/{STATUS.md, SESSION_LOG.md, DISPATCH_LOG.md, LAST_COMPLETION.md, board_log.tsv (new), registry/HANS_T_FIRED_LOG.tsv, registry/THRESHOLDS.tsv, registry/corrections_receipts.tsv, workbook/{VX,KB,PUBLISHED,PREDICTIONS,FLOW}.tsv, workbook/2026-09-25_INBOX_DISPOSITIONS.md (new), scripts/boot.py, scripts/test_hans.py, outbox/delivered/…}, 17 inbox→processed moves, AGENTS/LIQUID/inbox/ (packet), AGENTS/SIGNALS.md (1 row), PROME/inbox/ (this memo + cadence packet)
RESULT: HANS-T-10 FIRED 2026-09-24 (HANS-F-006): 109.9bp / 4.67 on the governing ideal-investisseur basis (Bund leg = ECB primary ±0.4bp). TE also fires at 108.3bp / 4.711, and the margins exceed the basis gap. About 11bp of the OAT's +19bp was common-mode Bund, and the cause is headline-only. Drained 17/17 inbox items (13 logged in a new board_log.tsv). VX-HANS-11.04 retired. The TTF ladder is pinned to named contracts (130 tests). HNS-06 HIT (flash 53.8). CADENCE: WEEKLY.
GAPS: No Banque de France daily OAT primary (Webstat TEC10 empty without a key). No T-10 exit registered (owed #24). The X26/Z26 TTF expiries are computed, not exchange-read (#26). The PMI grade rests on secondaries. The WQ-295 packet was never delivered to HANS. 14 carried self-scan consumer residuals were left as correct history, not cleared.
WILL_NEEDS: None
FOLLOW-UP: HANS: T-10 exit (#24) · 10/1 HICP flash = first T-15(b) read + PMI final · TTF roll 9/29 (boot warns) · France budget early Oct on an open fire. PROME: check why the WQ-295 packet missed AGENTS/HANS/inbox/.
