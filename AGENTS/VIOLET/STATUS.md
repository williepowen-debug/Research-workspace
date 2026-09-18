# VIOLET STATUS

**As of:** 2026-09-17T21:5x-04:00 (post-close). Market basis: **September 17, 2026 OFFICIAL close** (CBOE publisher of record, all six spot columns confirmed), except cells explicitly dated otherwise. Thesis **v4.1.1**. Grade record: [VIO-FOMC-0916 part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md). Prior state (9/16 close basis, 9/17 pre-open) preserved in git.

## BOTTOM LINE

**Post-FOMC vol crush, and the cheap-tail window RE-OPENED 4/4 on it — the first OPEN since 9/4, one day before BOJ and ~$6T September triple witching.** VIX −12.82% to **15.44**, the front end −23.0% (VIX9D 17.40→**13.39**), term structure re-steepened 1.1141→**1.2014**, VVIX 95.41→**87.72** (back under the 90 cheap line). ⚠️ **This is a LEVELS open, not a coiled-spring fire** — the registered 20-td divergence is NOT firing (ΔSKEW +2.77 vs the ≥+10 line; STRICT and DIET both False), and SKEW at 145.70 is **−8.79 off its 9/11 peak of 154.49**, so the tail held *today* without re-bidding. The window is an **operator decision surface, not a gate and not a trade** — route PROME → TERRY → Will. **No trade proposed; no threshold moved; book flat.** Leg 2 is running deep through its KILL line (VIX −12.82% vs the −1.41% line) but grades only on the 9/23 close; **leg 3 grades tomorrow on the 9/18 close.** Rates vol still breached but the margin to confirm-3 has collapsed to **+0.72** after two straight declines.

## SIGNAL DASHBOARD

| Metric | Value | As of | Source / interpretation |
|---|---:|---|---|
| VIX | **15.44**; −12.82% vs 17.71 (9/16) | Sep 17 SETTLE | [CONF] CBOE `VIX_History.csv`; LOW_VOL, p36.1 |
| VIX9D | **13.39**; −23.05% | Sep 17 SETTLE | [CONF] CBOE; front end crushed hardest |
| VIX9D / VIX | **0.8672** (was 0.9825) | Sep 17 | [CONF] same-date calculation |
| VIX3M / VIX6M | **18.55 / 20.30** | Sep 17 SETTLE | [CONF] CBOE |
| VIX3M / VIX | **1.2014** (was 1.1141) | Sep 17 | [CONF] same-date; steep contango restored — regime-consistent calm, not a warning shape |
| VVIX | **87.72**; −8.06% | Sep 17 SETTLE | [CONF] CBOE; p40.7 — **below the cheap-tail ≤90 line**, far below watch >100 / stress >120 |
| SKEW daily | **145.70**; −0.17% vs 145.95 (9/16) | Sep 17 SETTLE | [CONF] CBOE archive. **−8.79 (−5.69%) off the 9/11 peak 154.49** — **3rd** straight session <150 (9/15·9/16·9/17; the run stops at 9/14 = 152.09). *Read "5th" here before 9/18 02:2x: wrong, corrected on WALTER's catch — I counted sessions in the window, not sessions under the line.* |
| SKEW 20-session mean | **147.34** (was 147.21) | Sep 17 | [CONF] latest 20 populated CBOE SETTLE rows, window 8/20→9/17. Mean rose only because lower August bars rolled OFF — not a fresh bid |
| Adjusted M1:M2 | **+3.789%**, October/November | Sep 17 settlement | [CONF] CBOE; matched pair vs 9/16 (+2.381%) = **+1.41 pp** — contango re-steepened hard post-event. Same VX/V6–VX/X6 pair both dates |
| MOVE | **76.22**; −4.51 vs 80.73 (9/16) | Sep 17 | [CONF] investing.com PRIMARY, cross-check agrees; **+3.81 vs F1 72.41, +0.72 vs confirm-3 75.50** — still above both, margin collapsed from +5.23 in two sessions |
| OVX | **52.11**, ratio **3.38** (p96.4), FIRE | Sep 17 | [CONF] `OVX.tsv`; ratio ≥ p95 3.21. Ratio ROSE as VIX fell faster than OVX — denominator-led, not a numerator upgrade. Context canary, not an action-gate |
| JPY RV10 | **15.15%**, p94.8, **WATCH** | Sep 17 | [CONF] `JPY_VOL.tsv`; ≥ p90 14.15%. USDJPY 156.01. FXY IV leg 17.8% is an off-RTH pull — unverified; SAM owns BOJ 9/18 |
| COR1M / COR3M / COR30D | **10.79 / 11.58 / 8.48** | Sep 17 SETTLE | [CONF] Cboe delayed quote; DISPERSED. Superseded the 9/17 TICK row (14.43/13.07/9.42) |
| HY / CCC / BB OAS | **2.70 / 10.76 / 1.55%** | Sep 16 FRED | [CONF] direct FRED cache; CCC−BB **9.21 pp**; BIN-B block active (CCC ≥9.55). All four tightened vs 9/15. LIQUID owns credit interpretation |
| IG OAS / 10Y / 10Y real / 2Y | **0.78 / 5.01 / 2.68 / 4.74%** | Sep 16 FRED | [CONF] direct cache; T+1 lag means no 9/17 credit print exists yet |
| COT leveraged money net | **−23,270**, p56.4; OI 431,671 | Sep 8 report | [CONF] CFTC via `COT_VIX.tsv`; unchanged — next report not provably owed before 9/22 (KB-VIO-226) |
| VIX options positioning | **UNUSABLE current OI** (post-close pull; 5 OI comparisons skipped as after-hours artifact) | Sep 17 post-close | Forward C/P OI 0.00 is NOT positioning evidence; regular-hours chain still needed |

**Spot integrity:** the 9/17 row was written pre-open as a TICK with a blank SKEW cell and 9/16's m1m2 carried on it. Repaired this session: `thresholds.py --supersede` replaced it (basis TICK→**SETTLE**, m1m2 2.381→3.789, settle-date 9/16→**9/17**), then `backfill.py --spot-only` confirmed **2,544 cells agreed, 0 corrections** against CBOE. Closeout guard's `^SKEW bar continuity` contract went 🔴 → ✅.

## GATE STATUS

| Instrument | State | Exact scope / next step |
|---|---|---|
| **Cheap-tail alert** | 🟣 **OPEN, 4/4 — RE-OPENED 9/17** | VVIX 87.72 ≤90 ✅ · VIX 15.44 ≤16 ✅ · SKEW 145.70 ≥140 ✅ · nearest HIGH/MED catalyst **1d** (BOJ) ≤21d ✅. First OPEN since 9/4; DORMANT 2/4 through the 9/10–9/16 CPI/FOMC run. **Operator decision, not a gate and not a trade.** Route PROME → TERRY (construction) → Will [Approve]. ⚠️ **Decision has never been logged on ANY of the 5 OPEN days across both episodes** — see OPERATING LIMITS. |
| **VIO-FOMC-0916** | **PART 1 GRADED; legs 2 and 3 live** | Leg 1 VOID · leg 4 KILL · leg 5 HELD-with-defect · leg 3 first read no branch at 2/3. **Leg 3 GRADE = the 9/18 close** ([read plan §6](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md)). **Leg 2 = the 9/23 close**: ΔVIX from 17.71; >0 confirms, **< −1.41% kills**. Running at **−12.82%** on 9/17 — deep through the kill line, but 4 sessions remain and an intra-window print is not a read. Letter bytes unchanged (sha256 `ead84431…`). |
| **F-B** | **HELD** (window closed 9/16) | Zero-mean RMS 9.30% ann (4/4 sessions) ≤ 17.84% implied. Re-run 9/17: unchanged. Does not separate FOMC from OPEX positioning (H-new). |
| Coiled spring (STRICT / DIET) | **NOT FIRING** | 20-td 8/19→9/17: ΔSKEW +2.77 (needs ≥+10), ΔVIX +0.55, ΔVVIX +1.19. Both branches False. Today's SKEW-holds-while-VIX-crushes is a **1-day shape**, not the registered pattern — do not quote the KB-VIO-079 base rates off it. |
| GATE-VIO-RV1 | **RETIRED**, F2-killed Aug 27 | Alert observations do not revive it. |
| July tail-hedge packet | **RETIRED-SUPERSEDED** | Will stood it down Sep 4. |
| RED-FT-10 | **RED-OWNED — run BROKE 9/15** | WALTER SIG-W-20260917-002: SKEW <150 on 9/15 resets the sustain count to 0-of-4; the 9/16 earliest-fire clock is dead. Bars supplied by VIOLET; **RED owns the count and the reset.** |
| RED-FT-06 | **RED-OWNED** | Its registered VIXCLS series and sustain rule; VIOLET does not grade it. |
| KB-VIO-123 crack/fade tree | MOVE leg above line, **margin +0.72** | MOVE 76.22 >75.50. VVIX >120, VIX >20, inversion, COT ≥95 not met. Credit leg = LIQUID's determination. |
| BIN-A / BIN-B | **BIN-A STUCK; BIN-B block active** | CCC 10.76 ≥ 9.55 on Sep 16 FRED. Retired BIN-A lines produce no verdict. |
| GATE-VIO-116 | **RESOLVED July 16** | MOVE monitoring continues; no deployment authorization. |
| T9 self-falsifier | **NOT MET** | Conjunctive COR1M <6.77, JPY RV<IV, OVX <45, MOVE <66; three observed legs fail; JPY IV leg unverified off-hours. |

## CONVERGENCE MATRIX

**Convergence Score: 28/50** (10 vectors ×5), down from **30** on 9/16. The fall is entirely the post-event vol crush: VVIX 2→1 (now cheap, p40.7) and front curve 2→1 (steep contango restored). Ordinal dashboard, not a probability.

| Vector | Score | Current reasoning |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE 76.22 still above F1 and confirm-3 — but the margin collapsed +5.23 → **+0.72** on two straight declines. Breached by the rubric; fragile in substance |
| SKEW / tail bid | 🔴 **4** | 20-session mean 147.34 elevated, close 145.70 <150 and −8.79 off the 9/11 peak. RED owns FT-10 (run broke 9/15) |
| Oil vol | 🔴 **4** | OVX 52.11 p87.6, ratio 3.38 p96.4 FIRE — but ratio rose on the VIX denominator, no numerator-led upgrade |
| Credit | 🟠 **3** | CCC 10.76 distressed tail, CCC−BB 9.21 pp; HY 2.70 tightening, not confirming broad transmission |
| Positioning | 🟠 **3** | Lev money net short, mid percentile (9/8, stale); no squeeze threshold |
| JPY carry vol | 🟠 **3** | RV10 15.15% p94.8 WATCH into BOJ 9/18; percentile drifted up, state unchanged; IV leg unverified |
| VVIX | ⚪ **1** | 87.72 at p40.7, below the ≤90 cheap line — dormant as a stress vector, now functioning as a cheap-tail INPUT |
| Front curve | ⚪ **1** | 3M/VIX 1.2014 steep contango, 9D/VIX 0.8672 — regime-consistent calm per the term-structure table |
| Implied correlation | 🟡 **2** | COR1M 10.79 DISPERSED; no standalone validated trigger |
| Equity concentration | 🟡 **2** | VULCAN's structural watch retained |

## REGIME STATUS AND DRIFT

- Price classification LOW_VOL (VIX 15.44, p36.1); SKEW 20-session mean 147.34, above 140. No terminated ≥60-session regime asserted.
- **What the day after the hike did (9/16→9/17 official closes):** VIX −12.82%, VIX9D −23.05%, VIX3M −5.98%, VVIX −8.06%, SKEW −0.17%, MOVE −5.59%, matched contango **+1.41 pp**. The whole surface relaxed; the front relaxed most; the tail barely moved. This is the textbook post-event crush — event premium coming out of a curve that had been flattened into the decision.
- **The honest read on the tail.** SKEW holding at 145.70 while VIX fell 12.8% looks like a coiled spring and is **not one on this desk's own registered definition**: the 20-td divergence needs ΔSKEW ≥+10 and has +2.77. SKEW is *below* where it was on 9/11 (154.49), 9/14 (152.09) and 9/1 (149.23). What is true is narrower and worth exactly what it says: **the tail did not follow the front down on 9/17.** One session.
- **Leg 4's lesson stands, still provisional:** "rates leads equity" was true of the approach and false of the delivery — and rates vol has now fallen two more sessions (−3.56%, −5.59%) while the confirm-3 margin went to +0.72. Logged in `thesis/CHANGELOG.md`; no version bump until legs 2/3 resolve.
- **HENRY context:** still no 9/16 or 9/17 gamma board committed; HENRY dark since 9/14 with 9 unconsumed WALTER handoffs (2 ACTION) per SIG-W-20260917-004. **9/18 is ~$6T triple witching with the gamma board unmeasured for 3 sessions** — this is context for the leg-3 grade, not a cell in it.

## POSITIONS

Last recorded VIOLET book: **FLAT**. `TRY-VIOLET-VIXCS` closed July 30; FORGE's September 10 mirror confirms the historical closure. No broker refresh, no order, no proposal this session.

## RESEARCH QUEUE

1. **9/18 close — leg 3 GRADE** per read plan §6 (VIOLET grades; HENRY gamma context; RED adversarial byte/anchor check + the two pre-declared weak-discriminator flags). BOJ same day — SAM owns; JPY RV10 p94.8 WATCH. Triple witching same day.
2. **Cheap-tail OPEN 4/4 — operator decision owed** while the window is boxed by a 1-day catalyst. Route PROME → TERRY → Will; **log the decision taken-or-passed on the alert** (never once done — see OPERATING LIMITS).
3. **9/23 close — leg 2** (ΔVIX 9/16→9/23 > 0 confirms; < −1.41% kills). Running −12.82%; not an early read.
4. **Will-facing artifacts** (vol cheat-sheet · operating picture): last refreshed **2026-07-30, 49 days**; post-FOMC trigger FIRED 9/16 and agent state has materially changed (cheap-tail OPEN, score 28/50). Deferral-to-9/23 was reasoned when the only pending item was the letter; **that reason is now weaker.** Will's call — one redeploy after 9/23, or refresh now.
5. Regular-hours VIX options OI + term decomposition (H-new untested); RED/PROME L376 adoption pending.
6. Tooling debt: **the pre-open TICK-row defect bit again today** (blank SKEW cell + stale m1m2 carried on a same-date row) — recovered by `--supersede` + backfill for the 2nd time, still not fixed in code. Also: false-zero COR1M d/d; cheap-tail use-time mirror check unwired.
7. **Thesis-currency advisory resolved-by-reading this session** (see CHANGELOG 9/17 note): 30 KB rows since v4.1.1, read against the headline, **no semantic contradiction found** — the row mass is instrument/tooling findings plus the FOMC grades. No bump.
8. Research: Path-A F2 audit; H-carry event-conditioned RV study; directional-vs-level sample; L342 holiday-counter audit before Nov 26.

## OPERATING LIMITS

Graded on the OFFICIAL 9/17 closes at a 21:4x post-close boot. **Inbox: 2 WALTER signals consumed** (SIG-W-20260917-002 RED-FT-10 reset, -004 FOMC board record) — both INFO-only for VIOLET, logged to `board_log.tsv` and `git mv`'d; lane now empty.

⚠️ **The cheap-tail alert's own closing instruction — "Log the decision (taken or passed) on the alert" — has never been satisfied.** Five OPEN days across two episodes (8/26, 9/2, 9/3, 9/4, 9/17) all carry the note `window open` and nothing else, and no VIOLET→PROME memo in the 8/26–9/4 episode raised the window at all. The instrument fires correctly and the control is downstream of it, unowned. Flagged to PROME this session; VIOLET cannot self-authorize the route.

⚠️ **`board_log.tsv` repair, this session, my own defect:** a `printf` format string carrying a literal `%` wrote one truncated unterminated row, which the retry then concatenated onto. Caught within the minute by a field-count audit; corrupt line removed, backup in scratchpad. File now 155 rows, **all 5 fields, zero duplicate signal IDs** (both audits run over the whole file, not just the tail). Logged in MAINTENANCE.md.
