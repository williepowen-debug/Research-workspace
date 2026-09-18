# LIQUID — Durable Reference Tables (thresholds · playbooks)

**Moved OFF `STATUS.md` 2026-09-17 to hold the read cap.** These are **durable reference**, not live state: `STATUS.md` keeps the five registered GATES and their states, and **every live level comes from `scripts/boot.py`** — never from this file.
**Moved verbatim. crc32 `ecaa34cd` · 6,795 B.**

⛔ **Dates inside these rows are the vintage of the annotation, not of the market.** A row here is a *definition* plus its history; if a row's level looks live, it is not — re-pull.

---

## Triggers & Thresholds (durable reference — live levels → `scripts/boot.py`)

| Metric | Threshold / line | Owner |
|--------|------------------|-------|
| **HY OAS** | **<260 kill (×2 consecutive closes) · 265–280 approach · >280 X1-decoupling half · >320 confirmation** | **Live → `boot.py`** (266 [FRED 9/2] at this stamp; 2026 obs strictly <260: zero, n=177). **GATE-HY-REKILL NOT FIRED 0-of-2**; a ≤−4bp session is ~20% of 2026 sessions so the **CONSECUTIVE leg is the whole bar**; an unpublished session is `UNGRADEABLE-PENDING-PUBLICATION`, never `NOT-FIRED`. **H-2: a joint fire with HENRY's <260 bp sustained-5 leg is ONE event on ONE series.** **X1 UN-FIRED and CONJUNCTIVE — wrapper half ADJUDICATED NOT ARMED (BROCK 8/28).** ⛔ **Read any approach against the TAIL: a tape-only compression into <260 while CCC/BB sits at a 3-year record is exactly what the two-sided KILL_MEMO guard (KB-LIQ-105) blocks.** Canonical letter + ladder → `workbook/KILL_MEMO_HY_OAS_260.md`. |
| **CCC-BB tail-gap** | NEXUS R3 falsifier <~400 (pin = wide) — ⚠️ TWO annotations on every read **until the 7/31 index rebalance flush**: (a) partly AI-composition artifact BOTH legs (KB-LIQ-066); (b) **DISH stays IN the index until the 7/31 rebalance** (Ch.11 filed 6/30 AFTER the 6/25 lock-out — DEWEY/SIG-W-20260702-001; expect a MECHANICAL CCC tightening at removal that is NOT credit improvement → re-pull BAMLH0A3HYC + composition after 7/31; KB-LIQ-068 — don't read early-July moves as healing OR ratchet-failure without decomposing). Precision: 806 = 15-month high, NOT cycle (831 4/7/25); CCC 970 < 1,020 (3/30/26) = range re-test | LIQUID / NEXUS |
| **BB floor / AI-credit beta** | BB OAS >220 while CCC flat-to-tighter = AI-capex repricing the FUNDED leg (KB-LIQ-066); any single-agency ORCL cut to Baa3/BBB− = fallen-angel pipeline live (both outlooks NEGATIVE; ~$133B basis ≈ largest fallen angel ever) | LIQUID |
| **IG OAS + HY−IG basis** (mandate ext.) | IG >94 = 2026-high break; >110 = regime (IG leads when transmission is balance-sheet); basis +30bps/20 sessions with IG <85 = junk-specific decompression; basis <180 = complacency extreme | LIQUID |
| **SOFR dispersion** (mandate ext.) | 🔴 **BAND DEAD — retired 2026-08-27 (KB-LIQ-106).** The registered line (*SOFR75−IORB ≥0 ×3 consecutive non-Q-end days*) was cleared by the **MEDIAN day** (59.9% of non-Q-end sessions, n=615) and had been satisfied for **27 consecutive sessions** while this file read *"1 print, needs 3."* **Mechanism: a 75th PERCENTILE benchmarked against IORB — a level the distribution's mean trades near — is biased positive BY CONSTRUCTION; a percentile must be banded on its OWN distribution.** **Successor `scripts/sofr_dispersion.py`** reports deviation (base-rated robust z) and drift (slope, deliberately UNBANDED) separately; wired into `boot.py`. ⚠️ Its percentiles are percentiles of a sample containing **no funding seizure** — better-calibrated, NOT validated. **Today SOFR75−IORB +6bp [9/1].** ⛔ **`GATE-LIQ-079` is a DIFFERENT series and UNAFFECTED — ARM leg `SOFR99−IORB` +9bp [9/1], 21bp under +30, NOT ARMED** (basis repaired 8/28, KB-LIQ-113). *(Derivation rotated → `archive/status_snapshots/`.)* |
| **Dealer positions** (mandate ext., weekly Thu) | Corp IG inventory aggregate <0 = no warehouse bid (G5L10 already −$825mm 6/17); UST coupon net at ATH or +2σ/12wk = basis-absorption capacity shrinking | LIQUID |
| HY Energy OAS | >300 energy-credit trip — **structurally unavailable on free FRED** (paid ICE sub-index); reason, don't fabricate. **7/8 restate (KB-LIQ-071): direction in-line-to-tighter unless Brent <$60 — REINFORCED at $79; tanker/shipping + refiner HY = new name-level tail, not a sector-wide flip** | LIQUID |
| APO co-trigger | broke <$130 = alts-crack deepening (the old >$130-recovery framing is moot; KILL_MEMO) | BROCK |
| BIZD | $12.50 mark-stress line | LIQUID / BROCK |
| VIX | >25 (>23 = HENRY cascade) | HENRY |
| SOFR / SOFR-IORB | SOFR >3.70 · IORB spread sustained >0 = funding stress | LIQUID |
| 10Y / 30Y / 2Y | 10Y >4.50 sustained · 30Y >5.00 re-establish / <4.90 unwind · 2Y front-end tell | LIQUID / BOND |
| RRP / SRF / Reserves | RRP sustained >$10B into July · SRF >$50B · reserves <$2.8T (canonical WRESBAL, **not** FFIEC) | LIQUID |
| USD/JPY | >160 (triggered on level; repat pushed to Sep tail) | SAM |
| Auction indirect | <55% sustained = demand break | LIQUID / BOND |

---

## Active Playbooks / Monitors

| File | Purpose |
|------|---------|
| `workbook/KILL_MEMO_HY_OAS_260.md` | Canonical two-sided HY OAS trigger ladder + X1 conjunction — live until thesis reframed |
| `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` | **Q2-marks PRE-REG grading card (7/18, KB-083)** — 6 names, 5 QoQ metrics, mechanical CONFIRM/REFUTE/MIXED lines for the 7/25-28→early-Aug window = NEXUS R3/M-08 + BROCK wrapper-leads X1 half; grade name-by-name on arrival |
| `workbook/ORCL_FALLEN_ANGEL_MAP.md` | **ORCL fallen-angel trigger map (7/18, KB-082)** — cross-agency ladder (S&P BBB−/Moody's Baa2-neg/Fitch BBB), index middle/avg mechanics, ~$130-160B forced-sell sizing, GATE-069 2nd-leg fire condition (R1 = Moody's→Baa3) |
| `workbook/AUCTION_FRAMEWORK.md` · `workbook/TIC_FRAMEWORK.md` | Foreign-demand / auction-bid reference |
| `workbook/EXPECTED_SIGNALS_TRACKER.md` | Absence-is-data tracker (ES-LIQ-01..05: FHLB / sponsored-repo / MMF WAM / FTD / CCY-basis) — born 7/11, ask-8 closed |
| `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` | 3-leg amplification conjunction (SOFR-short / dealer warehouse / MOVE) — ARMED-WATCH, 2-of-3 fire rule (KB-LIQ-076) |
| ~~`workbook/CONSUMER_CREDIT_MONOLINES_PREREG.md`~~ | **GRADED REFUTE + ARCHIVED 2026-08-24** (KB-LIQ-103) → `archive/CONSUMER_CREDIT_MONOLINES_PREREG_GRADED_2026-08-24.md`. Consumer stress stays subprime/nonbank-CONTAINED |
| `workbook/DECOUPLING_TESTS_VIX_HY_2026-08-10.md` | **VIX-vs-HY independence battery (8/10 forum, Will-ruled). Tests B and C CLOSED; Test A v1 is UNGRADEABLE-UNDERPOWERED (WQ-113, Will-ruled 8/28) and NO GRADE IS OWED ON THAT LETTER.** ⇒ **Only live leg: T3 v2, first decidable 2026-09-23** (38 sessions from 7/31; DOCKET row 238), graded on the **38-session** partial correlation against the **≥0.45** detection band only, reported with its 95% Fisher CI and power. ⛔ **The 20-session r=+0.399 [7/31→8/27] is SUPERSEDED at that date, not carried — a different statistic, never compared against 0.45.** ⛔ A run of NO-VERDICT readings is **not** evidence of decoupling and **not** evidence the shared factor is the dollar; it is the absence of a reading. |
| `scripts/hy_oas_watch.py` | Unattended HY OAS X1/kill watcher (systemd timer; alerts/ surface) |

---
