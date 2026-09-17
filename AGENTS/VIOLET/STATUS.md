# VIOLET STATUS

**As of:** 2026-09-17T08:4x-04:00 (pre-open). Market basis: **September 16, 2026 OFFICIAL close** (CBOE publisher of record), except cells explicitly dated otherwise. Thesis **v4.1.1**. Grade record: [VIO-FOMC-0916 part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md). Prior state (9/14 close) preserved in git (`git show 75de562af^:AGENTS/VIOLET/STATUS.md` or earlier).

## BOTTOM LINE

**The Fed HIKED +25bp to 3.75–4.00% (12–0; federalreserve.gov, verified 9/17) and the frozen letter's part 1 graded on the 9/16 close: leg 1 VOID (VIX 17.20 at the 9/15 close >16), leg 4 KILL (MOVE +16.26% did not beat VIX +22.05%), leg 5 HELD with its §5 roll-date defect disclosed. Leg 3 first read: no branch at 2-of-3. F-B HELD (realized 9.30% ≤ 17.84% implied).** No CONFIRM in part 1. Rates vol led the whole approach and lost the lead on the delivery session (9/16: MOVE −3.56%, VIX +2.97%). LOW_VOL persists; cheap-tail DORMANT 2/4. **No trade proposed; no threshold moved.** Last recorded book flat; broker mirror is the Sep 10 FORGE snapshot, not a fresh confirmation. 9/17 pre-open TICK: VIX 15.70 (−11.35%) — inside leg 2's window, grades only on 9/23.

## SIGNAL DASHBOARD

| Metric | Value | As of | Source / interpretation |
|---|---:|---|---|
| VIX | **17.71**; +2.97% vs 17.20 (9/15) | Sep 16 SETTLE | [CONF] CBOE `VIX_History.csv`; yfinance agrees; LOW_VOL. FRED VIXCLS: access failed ×2 9/17 (UNKNOWN, not evidence) |
| VIX9D | **17.40**; +1.10% | Sep 16 SETTLE | [CONF] CBOE |
| VIX9D / VIX | **0.9825** | Sep 16 | [CONF] same-date calculation |
| VIX3M / VIX6M | **19.73 / 21.03** | Sep 16 SETTLE | [CONF] CBOE |
| VIX3M / VIX | **1.1141** | Sep 16 | [CONF] same-date; flatter, not inverted; letter branch-A cell (<1.10) NOT met on the first read |
| VVIX | **95.41**; +0.53% | Sep 16 SETTLE | [CONF] CBOE; above cheap-tail ≤90, below watch >100 / stress >120 |
| SKEW daily | **145.95**; −0.45% vs 146.61 (9/15) | Sep 16 SETTLE | [CONF] CBOE archive; both bars supplied to RED for FT-10 — RED owns the count |
| SKEW 20-session mean | **147.21** | Sep 16 | [CONF] latest 20 populated CBOE-confirmed SETTLE rows |
| Adjusted M1:M2 | **+2.381%**, October/November | Sep 16 settlement | [CONF] CBOE; matched pair vs 9/15 (+2.436%) = −0.055 pp — flat across the expiry. Strict Sep/Oct pair ended 9/16: VX/U6 final settlement (SOQ) **16.79** |
| MOVE | **80.73**; −2.98 vs 83.71 (9/15) | Sep 16 | [CONF] investing.com PRIMARY, cross-check agrees; +8.32 vs F1 72.41, +5.23 vs confirm-3 75.50 — still above both lines, fell on the hike |
| OVX | **57.49**, ratio **3.25**, FIRE | Sep 16 | [CONF] `OVX.tsv`; ratio ≥ p95 3.21; context canary, not an action-gate |
| JPY RV10 | **14.79%**, p93.2, **WATCH** | Sep 17 boot | [CONF] `JPY_VOL.tsv`; ≥ p90 14.15%. FXY IV leg 1.9% is an off-RTH pull — unverified; SAM owns BOJ 9/18 |
| COR1M / COR3M / COR30D | **14.43 / 13.07 / 9.42** | Sep 17 TICK | [CONF] Cboe delayed quote; DISPERSED; the 0.0% d/d field is the known false-zero (do not cite) |
| HY / CCC / BB OAS | **2.76 / 10.85 / 1.61%** | Sep 15 FRED | [CONF] direct FRED cache; CCC−BB **9.24 pp**; BIN-B block active (CCC ≥9.55). LIQUID owns credit interpretation |
| IG OAS / 10Y / 10Y real / 2Y | **0.80 / 5.00 / 2.62 / 4.67%** | Sep 15 FRED | [CONF] direct cache; pre-decision macro context, not 9/16 closes |
| COT leveraged money net | **−23,270**, p56.4; OI 431,671 | Sep 8 report | [CONF] CFTC via `COT_VIX.tsv`; next report not provably owed before 9/22 (KB-VIO-226) |
| VIX options positioning | **UNUSABLE current OI** (pre-open pull; 5 OI comparisons skipped as after-hours artifact) | Sep 17 pre-open | Forward C/P OI 3.52 is NOT positioning evidence; regular-hours chain needed |

**Spot integrity:** `backfill.py --spot-only` 9/17 created the two missing session rows (9/15, 9/16) the 9/16-evening crash had left out — 2,526 cells agreed, 12 blanks filled, **0 corrections**, both rows stamped SETTLE. The 9/17 boot wrote a TICK row with blank spot cells (known writer defect, KB class "empty row on source failure"); it will be superseded at the next SETTLE run.

## GATE STATUS

| Instrument | State | Exact scope / next step |
|---|---|---|
| **VIO-FOMC-0916** | **PART 1 GRADED 9/17 on the 9/16 close** | **Leg 1 VOID · leg 4 KILL · leg 5 HELD-with-defect · leg 3 first read: no branch at 2/3 (A 1/3, B 1/3, C 0/3).** Leg 3 GRADE = 9/18 close ([read plan §6](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md)); leg 2 = 9/23 close (KILL < −1.41%). Letter bytes unchanged; anchor-value defect (8/27 VIX 14.70→14.51) disclosed, verdict invariant. |
| **F-B** | **HELD** (9/16 close) | Zero-mean RMS 9.30% ann (4/4 sessions) ≤ 17.84%. Separate instrument; not a clean causal FOMC experiment (H-new untested). |
| Cheap-tail alert | **DORMANT, 2/4** | VIX 17.71 >16 and VVIX 95.41 >90 fail; SKEW ≥140 and catalyst ≤21d pass. A partial never reopens it. |
| GATE-VIO-RV1 | **RETIRED**, F2-killed Aug 27 | Alert observations do not revive it. |
| July tail-hedge packet | **RETIRED-SUPERSEDED** | Will stood it down Sep 4. |
| RED-FT-10 | **RED-OWNED** | Bars supplied: 154.49 [9/11], 152.09 [9/14], 146.61 [9/15], 145.95 [9/16]. No VIOLET count or grade; L376 adoption pending RED/PROME. |
| RED-FT-06 | **RED-OWNED** | Its registered VIXCLS series and sustain rule; VIOLET does not grade it. |
| KB-VIO-123 crack/fade tree | MOVE leg above line | MOVE 80.73 >75.50; VVIX >120, VIX >20, inversion, COT ≥95 not met. Credit leg = LIQUID's determination. |
| BIN-A / BIN-B | **BIN-A STUCK; BIN-B block active** | CCC 10.85 ≥ 9.55 on Sep 15 FRED. Retired BIN-A lines produce no verdict. |
| GATE-VIO-116 | **RESOLVED July 16** | MOVE monitoring continues; no deployment authorization. |
| T9 self-falsifier | **NOT MET** | Conjunctive COR1M <6.77, JPY RV<IV, OVX <45, MOVE <66; three observed legs fail; JPY IV leg unverified off-hours. |

## CONVERGENCE MATRIX

**Convergence Score: 30/50** (10 vectors ×5). Same total as 9/14, different composition: SKEW/tail bid 5→4 (close under 150), JPY carry vol 2→3 (WATCH). Ordinal dashboard, not a probability.

| Vector | Score | Current reasoning |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE 80.73 above F1 and confirm-3; fell 3.56% on the hike — lead lost, level still breached |
| SKEW / tail bid | 🔴 **4** | Close 145.95 <150, 20-session mean 147.21 elevated; RED owns FT-10 |
| Oil vol | 🔴 **4** | OVX 57.49 p91.7, ratio FIRE; no numerator-led upgrade |
| Credit | 🟠 **3** | CCC 10.85 distressed tail; HY 2.76 not confirming broad transmission |
| Positioning | 🟠 **3** | Lev money net short, mid percentile; no squeeze threshold |
| JPY carry vol | 🟠 **3** | RV10 14.79% p93.2 WATCH into BOJ 9/18; IV leg unverified |
| VVIX | 🟡 **2** | 95.41 under the >100 watch and >120 stress lines |
| Front curve | 🟡 **2** | 1.114 flatter, not inverted; matched-pair contango flat across the expiry |
| Implied correlation | 🟡 **2** | DISPERSED; no standalone validated trigger |
| Equity concentration | 🟡 **2** | VULCAN's structural watch retained |

## REGIME STATUS AND DRIFT

- Price classification LOW_VOL; SKEW mean above 140. No terminated ≥60-session regime asserted.
- **What the hike did to the surface (9/15→9/16 official closes):** VIX +2.97%, VIX9D +1.10%, VIX3M +1.91%, VVIX +0.53%, SKEW −0.45%, MOVE −3.56%, matched contango −0.055 pp. Equity vol rose, rates vol relaxed, the tail eased. The letter's structural claim (the expiring contract carried no Fed: SOQ 16.79 vs spot close 17.71; October +0.96%) held on the tape — it is not a graded leg.
- **Leg 4's lesson, provisional until legs 2/3 resolve:** "rates leads equity" was true of the approach and false of the delivery; a rates-led claim graded AT the event inherits the delivery day's composition. Logged in `thesis/CHANGELOG.md` (no version bump).
- **HENRY context:** last board 9/14 close (negative both horizons, one-session shelf life); no 9/16 board committed as of 9/17 08:2x — 9/16 gamma UNMEASURED. Packet sent for the 9/18 read (context, not a cell).

## POSITIONS

Last recorded VIOLET book: **FLAT**. `TRY-VIOLET-VIXCS` closed July 30; FORGE's September 10 mirror confirms the historical closure. No broker refresh, no order, no proposal this session.

## RESEARCH QUEUE

1. **9/18 close — leg 3 GRADE** per read plan §6 (VIOLET grades; HENRY gamma context; RED adversarial byte/anchor check + the two pre-declared weak-discriminator flags). BOJ same day — SAM owns; JPY RV10 already WATCH.
2. **9/23 close — leg 2** (ΔVIX 9/16→9/23 > 0 confirms; < −1.41% kills). The 9/17 pre-open crush is not an early read.
3. **Will-facing artifacts** (vol cheat-sheet · operating picture): post-FOMC trigger FIRED 9/16; refresh owed — deferred to after 9/23 so one redeploy carries all three parts (URLs in the memory files; republish to the SAME URL).
4. Regular-hours VIX options OI + term decomposition (H-new untested); RED/PROME L376 adoption pending.
5. Tooling debt unchanged: empty TICK/SETTLE rows on source failure; false-zero COR1M d/d; cheap-tail use-time mirror check unwired. Recovered by `backfill.py`, not fixed in code.
6. Research: Path-A F2 audit; H-carry event-conditioned RV study; directional-vs-level sample; L342 holiday-counter audit before Nov 26.

## OPERATING LIMITS

Graded on the OFFICIAL 9/16 closes at a 9/17 pre-open boot (the box crashed on the 9/16 evening; DOCKET L276 dated 9/16, one day late by machine, not by data). **Inbox: 1 top-level item consumed (board_log + `git mv`), WALTER lane empty — 0 files left.** Packets sent to HENRY and RED (carve-out ①); both desks DARK at `ListAgents` 9/17 08:3x — doorbell routed via PROME (messaging rule 6b). Other desks hold crash residue: **no pull, no stash**; local commits + `safe-push.sh` only if fast-forward.
