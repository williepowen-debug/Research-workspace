# CARL SCRATCH
> ✅ Clean & synced to origin (HEAD `cd7883ef`). All this session's work is pushed.

**Last session:** 2026-05-29 (single long session, multiple Will-directed work-blocks)
**Type:** 5/28-print resolution → boot-process build (predictions scan + docket) → docket QA. Big infra session plus live-data integration.

**PRIORITY-1:** **Boot the new way — run the step-7 scans FIRST, then handle the early-June data wall.** `.venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py` will surface a dense cluster: **ISM Mfg Jun 1, JOLTS Apr Jun 2, ISM Svc Jun 3, NFP May Jun 5** (all within ~a week). JOLTS Jun 2 is CRL-09-adjacent (just missed) + CRL-11 hires; NFP Jun 5 is the V16 second realized print. Process these as they land. Prune fired docket rows + add next month's instance at write-back.

**PRIORITY-2:** **V12 thesis pass — 3 hardening datapoints loaded** (Waller pivot 5/22 + GDP Q1 2nd-est stagflation composition 5/28 + Apr Core PCE 3.3% cycle-high 5/28). Re-read THESIS.md Vector #12 vs "locked + hawkish + possibly hiking"; decide v2.5.2 minor. Score-upgrade review V1/V8/V12. **Hold the FORMAL V12 call for Jun 16-17 SEP** (decisive), but a dedicated thesis pass before then is warranted.

---

## WHAT HAPPENED
1. **Boot** after 2-day gap (5/27). In sync; inbox clean; BOARD diff skipped (INDEX unmoved). Will scoped to "resolve 5/28 prints."
2. **CRL-18 CONFIRMED** — GDP Q1 2nd est **+1.6%** (-0.4pp), bottom-edge of predicted band. One-release stagflation signature: growth↓ / Core PCE↑ 4.4%. Drivers: healthcare-services (Census QSS) + inventory; goods revised up.
3. **CRL-08 re-armed OPEN** — AAA $4.391 5/29, breach window closed (partial-not-sustained), conf 92→70%.
4. **Apr PCE integrated** — Core PCE **3.3% YoY** cycle-high; **savings rate 2.6% (-100bps)**, Real DPI -0.5%, income flat = buffer-exhaustion deepening + V12 third datapoint.
5. **AFT/MOHELA 5/28** — conf held, no ruling, still in discovery (STUE; low signal).
6. **Boot step 7 added** (PREDICTIONS due/stale scan) → first run caught **CRL-09 ❌ MISSED** (JOLTS Mar 0.95 vs <0.88; 24d OPEN-stale; threshold miss, V16 intact).
7. **Docket built + consolidated** — `docket/CATALYSTS.tsv` + `CALENDAR.md` + `scripts/docket_countdown.py`; single source of truth; killed 4 drift surfaces (ROADMAP AWAITING DATA, STATUS EXIT-RULES line, DANGER WINDOW dated rows, EARNINGS_WATCH → archived). STATUS 260→250.
8. **Docket QA pass** — 3 date fixes (NFP Jun5/CPI Jun10/PCE Jun25 verified); **CRL-03 90→72%** (Fannie Apr 0.64% reversal; Mar 0.78% near-breach; Apr = month 1 of <0.65% invalidation); gap-filled all tiers **16→34 catalysts**.
9. **Git:** QA commit briefly deferred (origin diverged + SAM tree dirty) → rode SAM's push-train onto origin. All pushed, clean.

## STATUS CHANGES (key)
| Item | Change |
|------|--------|
| CRL-18 | OPEN → ✅ CONFIRMED (1.6%) |
| CRL-09 | OPEN → ❌ MISSED (JOLTS 0.95) |
| CRL-08 | partial → re-armed OPEN (92→70%) |
| CRL-03 | 90% → **72%** (Fannie Apr reversal; STATUS row 🔴→🟠) |
| GDP / Core PCE / Savings / Real DPI rows | refreshed to Apr/2nd-est; V12 hardening |
| STATUS line count | 260 → **250** (at target) |
| New infra | `docket/` (34 catalysts) + `scripts/docket_countdown.py` + CLAUDE.md step 7/13 |

---

## NEXT SESSION SHOULD

### IMMEDIATE (boot + 24h)
1. **Run step-7 scans** (docket countdown + PREDICTIONS awk) — this replaces reconstructing catalysts from prose.
2. **Early-June data wall** (per docket): ISM Mfg Jun 1, JOLTS Apr Jun 2, ISM Svc Jun 3, NFP May Jun 5, DG Q1 Jun 2. Integrate + prune docket rows.

### THIS WEEK / NEXT 2 WEEKS (docket has full dated list)
3. **Jun 10** CPI May · **Jun 12** UMich prelim · **Jun 16** Retail Sales + NAHB + LEN FQ2 · **Jun 16-17 FOMC + SEP** (V12 decisive).

### WATCH / CONDITIONAL
4. **CRL-03 invalidation watch** — May Fannie (~Jun 26) decides: 2nd consecutive <0.65% print invalidates. (In docket.)
5. **AAA pump** — dormant unless Brent re-spikes on Iran-kinetic (CRL-08 re-armed, no active breach).

### THESIS / WORKBOOK (no hard deadline)
6. **V12 thesis pass + score-upgrade review** (V1/V8/V12) — PRIORITY-2 above.
7. **Workbook session** — ~16 KB candidates pending (GDP 2nd-est / Apr PCE Core 3.3% / savings 2.6% buffer-exhaustion / CRL-08 5d-breach + 12 carried); VX 24d stale (FOMC/GAS/HSG/K-shape-WAGE); SAV-vector update for 2.6%.
8. **LIAISON calibration cycle 1** — OVERDUE ~23d (since May 6).
9. **Sub-agent staleness** — all 7 now 42+ days. **DOC spawn candidate** (healthcare-services GDP drag = care-avoidance primary data).
10. **5/6-5/13 BOARD backlog (~70 sigs)** — mechanical ledger sync.
11. **Docket maintenance** — firm the (~) approximate dates (Q2 earnings, Aug/Sep windows) as official schedules confirm.

### BACKLOG (no deadline)
12. HY OAS refresh (~49d). Workbook Item #3 (validator) + #6 (INDEX). v2.5.1 8 PENDING_VERIFY. ABS_BASELINE Mar 10-Ds. POLLY/MARCO refresh. 6 Apr-17 outbox signals (deferred per messaging-overhaul).

---

## OUTBOX (6 Apr 17 signals deferred per messaging-overhaul; none new)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 60+ DQ |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS structured-credit sub-vector |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | FL UI Wave 2 + $4.09 FL gas + 22% gig |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar SB metrics |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA + $166B refunds |

**Candidates for NEW outbox (NOT WRITTEN — Will to decide):**
- SIG-CARL-PROME-V12-regime-shift — now reinforced by GDP-composition + Apr Core PCE (3 datapoints); transmission-chain reset.
- SIG-CARL-LIQUID-Wilmington-Trust-ABS-custodial-exit · SIG-CARL-HOMER-condo-K-shape · SIG-CARL-PROME-K-shape-wage-completion.

## INBOX (0 items, clean)
## HANDOFF_RED (4 files staged, awaiting RED pickup — unchanged): COUNTER_LOG / SOFT_LANDING / CONTAINMENT / COUNTER_EVIDENCE_FROM_THESIS
## HANDOFF_WALTER — LIAISON cycle 1 OVERDUE ~23d (last touched May 6)

---

## WORKBOOK HEALTH (as of 5/29)
| TSV / file | Rows | Last Mod | Note |
|-----|------|----------|------|
| **docket/CATALYSTS.tsv** | 34 | **May 29** | NEW — single-source catalyst feed; run countdown at boot |
| PREDICTIONS | 24 | **May 29** | CRL-18 CONFIRMED, CRL-09 MISSED, CRL-08 re-armed, CRL-03 72% |
| CHANGELOG.md | — | **May 29** | 5/29 entry (CRL-18/08/09/03 + Apr PCE); still owes V12/K-shape-wage backfill |
| STATUS.md | 250 | **May 29** | at target |
| ROADMAP.md | — | **May 29** | AWAITING DATA retired → docket |
| KB | 279 | May 5 | 24d — ~16 candidates pending |
| VX | 117 | May 5 | 24d — FOMC/GAS/HSG/K-shape-WAGE pending |
| BOARD_LOG | 193 | May 27 | INDEX unmoved — no diff owed |
| LIAISON.md | 7 turns | May 6 | cycle 1 OVERDUE ~23d |
| FLOW / STATE_DIFFUSION / BNPL_STRESS | 24/62/59 | Apr 17 | **42d** |
| ABS_BASELINE | 72 | Apr 16 | **43d** |
| TRENDS | 39 | Apr 6 | **53d** |

---

## URGENT
- Early-June data wall starts **Jun 1** (ISM) — boot with the docket countdown.
- **CRL-03 May Fannie (~Jun 26)** = invalidation decider (month 2 of <0.65%).
- **Jun 16-17 FOMC + SEP** = V12 decisive catalyst.

## SESSION FINDINGS WORTH CARRYING
- **GDP 2nd-est + Apr PCE = a one-window stagflation triple** with the Waller pivot: growth revised down while core inflation revised/printed up. V12 is loaded 3 ways; the formal score call waits for SEP.
- **Savings rate 2.6% (-100bps MoM)** on flat income + Real DPI -0.5% = clearest single-month buffer-exhaustion print of the cycle. Watch May/Jun toward sub-2.5% (GFC/2022 territory).
- **Healthcare-services drag drove the GDP consumer revision** (Census QSS) = care-avoidance in NIPA, a DOC primary-data point → DOC spawn candidate.
- **CRL-08 (re-arm) and CRL-09 (miss)** both exercised threshold-vs-mechanism discipline; CRL-03 (reprice) is the same pattern — Fannie MF DQ is lumpy, mechanism intact, threshold pushed out.
- **Process:** the docket + predictions scans both earned their keep on first run (caught a 24d-stale MISS + a CRL-03-material stale value). The docket is now the forward-catalyst source of truth — don't rebuild date-lists in STATUS/ROADMAP.
