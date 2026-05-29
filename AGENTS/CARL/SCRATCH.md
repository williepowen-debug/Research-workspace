# CARL SCRATCH
**Last session:** 2026-05-29 ~15:30 UTC
**Type:** 5/28-print resolution + boot-process build (both Will-directed). CRL-18 CONFIRMED; CRL-08 re-armed OPEN; Apr PCE grabbed (Core 3.3% cycle-high, savings 2.6%); boot-step 7 PREDICTIONS scan → caught CRL-09 MISSED; **`docket/` built (single-source catalyst feed + countdown) consolidating 4 drift surfaces, STATUS 260→250**. Multiple commits pushed; docket commit pending.

**PRIORITY-1:** **V12 score-upgrade case now has THREE hardening datapoints in one window** (Waller pivot 5/22 + GDP Q1 2nd-est stagflation composition 5/28 + Apr monthly Core PCE 3.3% cycle-high 5/28). Re-read THESIS.md Vector #12 against "locked + hawkish + possibly hiking"; decide v2.5.2 minor. Score-upgrade review for V1 (CC DQ 13.1%) + V8 (K-shape wage completion) + V12. **Hold the FORMAL V12 score call for Jun 16-17 SEP** (decisive catalyst), but the evidence is now loaded — worth a dedicated thesis pass before then.

**PRIORITY-2:** **Buffer-exhaustion deepening is its own thread now.** Apr savings rate 2.6% (-100bps MoM) + Real DPI -0.5% (5th neg, accelerating) + income flat = savings-funded-forced-consumption intensifying. This is the consumer-runway-shortening mechanic; worth a SAV-vector update + possible KB synthesis row.

---

## WHAT HAPPENED

1. Boot after 2-day gap from 5/27. Branch up-to-date with origin (5/29 SENTRY feed already pulled). SAM/BROCK/HENRY/REGINALD dirty in their dirs — did NOT pull/stash (nothing to pull). Inbox clean. BOARD diff skipped (INDEX mtime 5/26 < CARL last disposition 5/27).
2. **Will scoped session to "Resolve 5/28 prints."** 3 live-data fetches (parallel WebSearch + 1 WebFetch on BEA detail).
3. **GDP Q1 2026 2nd est (BEA May 28): +1.6%, -0.4pp from 2.0% advance → CRL-18 CONFIRMED** (60% conf, bottom-edge of predicted 1.6-1.8%). Stagflation signature: growth↓ / Core PCE prices↑ to 4.4% ann. (from 4.3%); headline PCE 4.5% held. Drivers: consumer SERVICES (healthcare, Census QSS) + inventory drawdown; goods (recreation/vehicles) revised UP.
4. **AAA pump $4.391 (5/29) → CRL-08 breach window CLOSED** — partial-not-sustained, re-armed OPEN (92→70%). -17.3¢ from $4.564 peak; Memorial Day spike reverting.
5. **AFT/MOHELA 5/28 conf** held — no ruling, still in discovery, no class cert / settlement. Low new signal (STUE).
6. **Apr PCE grabbed (per Will follow-up).** Core PCE **3.3% YoY** cycle-high (+0.2% MoM); headline 3.8% (+0.4%). **Savings rate 2.6% (-100bps from Mar 3.6%)**, Real DPI -0.5% (5th neg, accel), income flat 0.0%, Real PCE +0.1%. Third V12-hardening datapoint of the window + buffer-exhaustion deepening. 4 STATUS rows updated (Core PCE Monthly, Savings Rate, Real DPI, Real Consumer Spending).
7. **BOOT PROCESS CHANGE (Will-directed).** Added SPAWN PROTOCOL **step 7 "PREDICTIONS due/stale scan"** to CLAUDE.md (cheap half of SAM's calibration discipline). Helper: `awk -F'\t' 'NR>1 && $6=="OPEN"{print $1"\t"$5"\t"$4}' thesis/PREDICTIONS.tsv`. **First run caught CRL-09 → ❌ MISSED** (JOLTS Mar ratio 0.95 vs predicted <0.88; direction-wrong, crossed own 0.93 invalidation line; cause = pre-flagged LFPR-denominator shrink; V16 intact via other legs). Was OPEN-stale 24d. Resolved in PREDICTIONS + STATUS + CHANGELOG.
8. **DOCKET BUILT (Will-directed, full consolidation).** New `docket/` (CATALYSTS.tsv 16-row + CALENDAR.md twin) + `scripts/docket_countdown.py` = single source of truth for forward catalysts. Boot step 7 now "Boot scans" (7a docket countdown + 7b predictions); write-back step 13 prunes fired catalysts. **Consolidated 4 drift surfaces:** ROADMAP AWAITING DATA + STATUS EXIT-RULES line → docket pointers; DANGER WINDOW trimmed 12 dated/fired rows (STATUS 260→250); EARNINGS_WATCH_Q1.md → archive/. Countdown auto-flagged **Fannie MF DQ Mar/Apr past-due** (CRL-03 refresh, 0.80% GFC, 6bps away).

## STATUS CHANGES
| Item | Change |
|------|--------|
| GDP row | advance +2.0% → **2nd est +1.6%** (-0.4pp) + stagflation-composition detail; 🔴🔴 held |
| Gas Pump row | $4.459 5/27 → **$4.391 5/29**, CRL-08 breach window CLOSED |
| CRL-18 | OPEN → **✅ CONFIRMED** (moved to Resolved table; PREDICTIONS Date_Resolved 2026-05-28 + Outcome) |
| CRL-08 | partial → **re-armed OPEN**, conf 92→70%, dated disposition note (PREDICTIONS field-count re-verified 10/10) |
| DANGER WINDOW | NOW row → 5/29 lead (CRL-18 + CRL-08); recently-fired digest +3 (5/28 GDP, 5/28 AFT/MOHELA, 5/29 gas) |
| EXIT RULES | dropped past 5/28; leads ~May 30 core PCE |
| CHANGELOG | +5/29 entry (CRL-18 + CRL-08) |
| ROADMAP | CRL-08 thread → re-armed; V12 thread +5/29 GDP-composition add; RECENTLY RESOLVED +entry; timestamp |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **V12 thesis pass** — 3 hardening datapoints loaded (see PRIORITY-1); dedicated re-read worth doing before Jun 16-17 SEP.
2. **Fannie MF DQ refresh** — STATUS stale at Feb 0.74%; Mar/Apr monthly data should be out. CRL-03 (90%, Q2 2026, 0.80% GFC target) is 6bps away — worth a fetch. (Surfaced by new PREDICTIONS scan.)
3. **Run boot-step 7 scans every boot now:** (7a) `.venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py` (docket countdown — past-due + upcoming); (7b) PREDICTIONS due/stale awk. Prune fired catalysts from docket at write-back.
4. **AAA pump** — only re-arm daily cadence if Brent re-spikes on Iran-kinetic; otherwise dormant. Apr core PCE DONE (grabbed 5/29).

### UPCOMING (this week)
3. **Jun 6** BLS May NFP (V16 second realized print).

### UPCOMING (next 2 weeks)
4. **Jun 11** BLS May CPI (second Iran-shock + tariff month).
5. **Jun 16-17** FOMC + SEP — first dot-plot post-Waller; market pricing ~2-in-3 Oct hike vs Fed dots. MATERIALLY HIGHER STAKES.

### UPCOMING (next 6+ weeks)
6. **Jun 24** FL Wave 1 UI exhaustion cliff. **Jul 1** SAVE→RAP (7.5M). **~mid-Aug** NY Fed Q2 HHDC (CRL-05 breach window).

### Workbook / thesis hardening pending
7. **KB candidates now ~16** — 12 carried + **GDP 2nd-est (stagflation composition)** + **CRL-08 5d-breach episode** + **Apr PCE Core 3.3%** + **Apr savings-rate 2.6% / buffer-exhaustion**. Dedicated workbook session. Also: SAV-vector update for 2.6% print.
8. **V12 thesis re-read / v2.5.2** — 2 hardening datapoints now (Waller + GDP composition).
9. **V1 + V8 + V12 score-upgrade review.**
10. **STATUS hygiene** — was 260 over target; this session net ~neutral, recheck line count.
11. **LIAISON calibration cycle 1** — now OVERDUE ~10d.
12. **Sub-agent staleness** — all 7 now 42+ days. **DOC spawn candidate surfaced** (healthcare-services GDP drag = care-avoidance primary data).
13. **5/6-5/13 BOARD backlog (~70 sigs)** — mechanical ledger sync.

### BACKLOG (no deadline)
14. HY OAS refresh (now ~49d stale). Workbook Item #3 (validator) + #6 (INDEX). v2.5.1 8 PENDING_VERIFY. ABS_BASELINE March 10-Ds. POLLY/MARCO refresh. 6 Apr-17 outbox signals (deferred per messaging-overhaul).

---

## OUTBOX (6 Apr 17 signals deferred per messaging-overhaul; no new this session)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 60+ DQ |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS new structured-credit sub-vector |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | FL UI Wave 2 + $4.09 FL gas + 22% gig |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar SB metrics |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA + $166B refunds |

**Candidates for NEW outbox (NOT WRITTEN — Will should decide):** (unchanged from 5/27)
- SIG-CARL-PROME-20260527-V12-regime-shift-Waller-pivot.md — now reinforced by GDP-composition; load-bearing transmission-chain reset.
- SIG-CARL-LIQUID-20260527-Wilmington-Trust-ABS-custodial-exit.md
- SIG-CARL-HOMER-20260527-condo-K-shape-Wolf-Street.md
- SIG-CARL-PROME-20260527-K-shape-wage-side-completion.md

## INBOX (0 items, clean)

## HANDOFF_RED (4 files staged, awaiting RED pickup — unchanged)
COUNTER_LOG.md / SOFT_LANDING.md / CONTAINMENT.md / COUNTER_EVIDENCE_FROM_THESIS.md

## HANDOFF_WALTER (LIAISON.md — calibration cycle 1 OVERDUE ~10d)
- LIAISON.md last touched 2026-05-06 PM2. Calibration cycle 1 trigger met May 19.

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | 279 | May 5 PM | 24d — ~14 candidates pending (12 carried + GDP 2nd-est + CRL-08 breach episode) |
| VX | 117 | May 5 PM | 24d — FOMC/GAS/HSG + K-shape WAGE candidate pending |
| PREDICTIONS | 24 | **May 29** | This session (CRL-18 → CONFIRMED, CRL-08 re-armed) |
| CHANGELOG.md | — | **May 29** | This session (+5/29 entry); still owes V12 regime-shift + K-shape-wage backfill |
| ROADMAP.md | — | **May 29** | This session |
| STATUS.md | ~260 | **May 29** | This session; recheck line count vs 250 target next hygiene pass |
| BOARD_LOG | 193 | May 27 | INDEX unmoved since 5/26 — no diff owed |
| handoff_WALTER/LIAISON.md | 7 turns | May 6 PM2 | calibration cycle 1 OVERDUE ~10d |
| FLOW | 24 | Apr 17 | **42d** |
| STATE_DIFFUSION | 62 | Apr 17 | **42d** |
| BNPL_STRESS | 59 | Apr 17 | **42d** |
| ABS_BASELINE | 72 | Apr 16 | **43d** |
| TRENDS | 39 | Apr 6 | **53d** |

---

## URGENT
- **V12 score-upgrade now has 3 hardening datapoints** (Waller + GDP composition + Apr Core PCE 3.3%) — flag for thesis re-read; hold formal call for Jun 16-17 SEP.
- CRL-08 dormant unless Brent re-spikes — don't burn AAA daily fetches without a kinetic trigger.

## SESSION FINDINGS WORTH CARRYING
- **GDP Q1 2nd est is a clean one-release stagflation signature** — real growth revised DOWN (1.6%) while Core PCE prices revised UP (4.4%). Strongest single-print V12 evidence since Waller; the two compound.
- **Apr PCE deepens it twice over:** (1) Core PCE 3.3% YoY = monthly-data confirmation of the GDP-quarterly read (V12 third datapoint same window); (2) **savings rate 2.6% (-100bps MoM) on Real DPI -0.5% + flat income** = the consumer runway is shortening fast — savings-funded forced consumption is now eating buffer at an accelerating rate. This is the clearest single-month buffer-exhaustion print of the cycle. Watch whether May/Jun savings rate stabilizes or keeps falling toward sub-2.5% (GFC/2022 territory).
- **Healthcare-services drag drove the consumer-side GDP revision** (Census QSS) — that's care-avoidance showing up in NIPA, a DOC-domain primary-data point. Goods (recreation/vehicles) revised UP = forced/trade-down consumption.
- **CRL-08 is the textbook threshold-vs-mechanism case** (cf. finding_threshold_vs_mechanism): threshold reached but didn't sustain, mechanism intact → re-arm OPEN, not MISS. Brent-pump lag empirically 17-18d both directions this cycle.
