# VIOLET STATUS

**As of:** 2026-09-14T22:44:19-04:00. Market basis: **September 14, 2026 close**, except cells explicitly dated otherwise. Thesis **v4.1.1**. Detailed evidence: [sweep report](reports/2026-09-14_sweep/README.md), [news and sources](reports/2026-09-14_sweep/news.md).

## BOTTOM LINE

**LOW_VOL with an event bid; cheap-tail CLOSED (2/4).** VIX and VVIX rose from Friday while SKEW eased but stayed above 150. The near end repriced upward; the tail remains expensive. This is not a new formal coiled-spring trigger. **No new trade proposed.** Last recorded VIOLET position is flat; the broker mirror is September 10, not a fresh holdings confirmation.

The main external context is the Fed/BOJ/expiry cluster, energy-supply risk and concentrated AI losses. HENRY's September 14 gamma board is negative at both horizons, with a **one-session shelf life**. It informs amplification risk; it neither identifies the shock nor grades VIOLET's frozen letter.

## SIGNAL DASHBOARD

| Metric | Value | As of | Source / interpretation |
|---|---:|---|---|
| VIX | **17.10**; +7.95% vs 15.84 Friday | Sep 14 SETTLE | [CONF] Cboe quote + archive agreement; LOW_VOL |
| VIX9D | **16.91**; +16.86% | Sep 14 SETTLE | [CONF] Cboe; near-term risk rebid |
| VIX9D / VIX | **0.9889** | Sep 14 | [CONF] same-date calculation |
| VIX3M / VIX6M | **19.28 / 20.71** | Sep 14 SETTLE | [CONF] Cboe |
| VIX3M / VIX | **1.1275** | Sep 14 | [CONF] same-date calculation; flatter, not inverted |
| VVIX | **94.89**; +3.95% | Sep 14 SETTLE | [CONF] Cboe; above cheap-tail ≤90, below stress >120 |
| SKEW daily | **152.09**; −1.55% vs 154.49 | Sep 14 SETTLE | [CONF] Cboe archive; RED owns FT-10 grading |
| SKEW 20-session mean | **146.90** | Sep 14 | [CONF] calculated from latest 20 populated Cboe-confirmed session rows |
| Strict M1:M2 | **+9.81%**, September/October | Sep 14 settlement | [CONF] Cboe futures; September has 2 calendar days to expiry |
| Adjusted pair | **+3.226%**, October/November | Sep 14 settlement | [CONF] Cboe; roll rule skips front contract when DTE <5. **Not comparable with Friday's September/October +10.57%.** |
| MOVE | **83.90** | Sep 14 | [CONF] investing.com PRIMARY; Sep 11 recovered at 82.21; +11.49 vs F1 72.41 |
| OVX | **59.46**, ratio **3.48**, FIRE | Sep 14 | [CONF] `OVX.tsv`; level +0.92%, VIX +7.95%, so ratio eased. Context canary; no upgrade merely from ratio |
| JPY RV10 | **13.53%**, p87.6, CALM | Sep 14 | [CONF] `JPY_VOL.tsv`; WATCH 13.98%. FXY IV is off-hours and not actionable |
| COR1M / COR3M / COR30D | **13.10 / 12.03 / 8.66** | Sep 14 | [CONF] Cboe via ledger. COR1M vs Sep 11 ledger 11.18: +17.17%; API prev-close equality is not a trustworthy daily-change field |
| HY / CCC / BB OAS | **2.65 / 10.76 / 1.50%** | Sep 11 FRED | [CONF] direct FRED cache; CCC−BB **9.26 pp**. LIQUID owns credit interpretation |
| IG OAS / 10Y Treasury / 10Y real yield | **0.80 / 4.96 / 2.60%** | Sep 11 FRED | [CONF] direct cache; dated macro context, not Sep 14 closes |
| COT leveraged money net | **−23,270**, p56.4; OI 431,671 | Sep 8 report | [CONF] CFTC via `COT_VIX.tsv`; NORMAL, not extreme |
| VIX options positioning | **UNUSABLE current OI** | Sep 14 after hours | Near-zero/absent OI artifact. Do not quote 9.95 C/P as positioning; last usable Sep 11 C/P 2.79 is historical |

**Spot integrity:** `backfill.py --spot-only` confirmed 2,526 cells across 421 sessions, zero corrections. Both Sep 11 and Sep 14 SKEW closes agree with Cboe archives. Current mirror-check receipt: `reports/2026-09-14_sweep/skew-integrity.txt`; **rc=0: all 20 compared sessions agree within 0.005; no omission or disagreement.**

## GATE STATUS

| Instrument | State | Exact scope / next step |
|---|---|---|
| Cheap-tail alert | **CLOSED, 2/4** | VIX 17.10 >16 and VVIX 94.89 >90 fail; SKEW ≥140 and dated catalyst ≤21d pass. A partial never reopens it. |
| GATE-VIO-RV1 | **RETIRED**, F2-killed Aug 27 | Alert observations do not revive the retired gate. Any successor requires its own authorization and validated specification. |
| July tail-hedge packet | **RETIRED-SUPERSEDED** | Will stood it down Sep 4; no remaining fire condition. |
| RED-FT-10 | **RED-OWNED** | Supply dated SKEW 154.49 [Sep 11], 152.09 [Sep 14]. No VIOLET count or grade. Read RED's current record; do not adopt pending amendments. |
| RED-FT-06 | **RED-OWNED** | Its exit uses its registered VIXCLS series and sustain rule; VIOLET does not grade it. |
| KB-VIO-123 crack/fade tree | MOVE leg above line | MOVE >75.50; VVIX >120, VIX >20, inversion, and COT ≥95 not met. Credit leg requires LIQUID's owner determination; do not imply all six freshly adjudicated. |
| BIN-A / BIN-B | **BIN-A STUCK; BIN-B block active** | Retired BIN-A level lines produce no verdict. BIN-B CCC ≥9.55 remains met on Sep 11 FRED. |
| GATE-VIO-116 | **RESOLVED July 16** | MOVE monitoring continues; no new deployment authorization. |
| T9 self-falsifier | **NOT MET** | Conjunctive COR1M <6.77, JPY RV<IV, OVX <45, MOVE <66. Three observed legs fail; JPY IV leg unverified off-hours. |
| VIO-FOMC-0916 | **FROZEN, unresolved** | Sep 16 / 18 / 23 grades. **Leg 1 void if Sep 15 VIX >16**. Roll-date error documented in separate addendum; original bytes unchanged. |
| F-B | **IN PROGRESS** | Two of four sessions: +0.856%, −0.484%; zero-mean RMS 11.04% annualized vs 17.84%. Resolve Sep 16 close; no early grade. |

## CONVERGENCE MATRIX

**Convergence Score: 30/50** (10 vectors ×5). Re-evaluated on current evidence; unchanged total. An ordinal dashboard, not a probability or ten independent confirmations. Cheap-tail remains outside this stress matrix.

| Vector | Score | Current reasoning |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE remains above F1 and confirm-3; current primary recovered |
| SKEW / tail bid | 🔴🔴 **5** | Close remains above 150 and mean elevated; score is not RED's gate state |
| Oil vol | 🔴 **4** | High OVX level persists; ratio easing and no new numerator-led upgrade |
| Credit | 🟠 **3** | Distressed tail widening; no fresh broad-credit transmission confirmation |
| Positioning | 🟠 **3** | Latest CFTC report still net short, mid-range percentile; no squeeze threshold |
| VVIX | 🟡 **2** | Rebid, but under the >100 watch and >120 stress lines |
| Front curve | 🟡 **2** | Same-date spot curve flatter but not inverted; adjusted-pair discontinuity excluded |
| Implied correlation | 🟡 **2** | Up vs prior ledger, remains DISPERSED; no standalone validated trigger |
| JPY carry vol | 🟡 **2** | CALM below WATCH; attribution not inferred from Japanese equity losses |
| Equity concentration | 🟡 **2** | VULCAN's structural watch retained; one AI-led selloff is not a new calibrated regime |

## REGIME STATUS AND DRIFT

- Price classification remains LOW_VOL; SKEW mean remains above 140. Short-run moves do not establish a terminated ≥60-session regime, so that conditional base rate is not invoked.
- **CPI wording corrected:** actual core +0.3% m/m and +2.4% y/y are verified; the prior unconditional “in line” surprise claim is withdrawn. Friday's vol decline remains measured, but does not prove a dovish report.
- **Attribution reduced:** Friday's front/tail divergence does not by itself prove premium transferred between tenors or identify the same traders. Cboe's flow commentary provides independent context, not a conservation-of-premium measurement.
- **HENRY context [Sep 14 measurement]:** negative sign at both horizons; flip 7,676–7,677; call wall 7,700, put band 7,500–7,600. Computing spot 7,630.02 is the estimator input, not the final close. Refresh before Sep 16/18; do not place this sign in the durable thesis. OI term split still unavailable, so H-new remains untested.
- **News balance:** macro hedging and energy persistence support vigilance; broad participation outside AI argues against calling Monday a universal liquidation. [Source-grounded sweep](reports/2026-09-14_sweep/news.md).

## POSITIONS

Last recorded VIOLET book: **FLAT**. `TRY-VIOLET-VIXCS` closed July 30; FORGE's September 10 mirror confirms the historical closure. No broker refresh, new order, or trade proposal in this sweep. Historical trade records live in `TRADE.md` and the archived pre-sweep copy.

## RESEARCH QUEUE

1. Capture Sep 15 Cboe closes; evaluate the frozen Leg 1 applicability condition; preserve complete SKEW bars.
2. Grade frozen VIO-FOMC-0916 and F-B on their specified dates; fresh gamma context must not replace registered inputs. See `workbook/PREDICTIONS.tsv` and the roll-date addendum.
3. Obtain usable regular-hours VIX options OI; retain H-new OPEX-vs-FOMC as untested without term decomposition.
4. Tooling debt found during this sweep: thresholds can write an empty SETTLE row on source failure; implied-correlation can display a false zero daily change; cheap-tail use-time mirror check remains unwired. Data recovered; no code fix claimed.
5. Existing research: Path-A F2 audit, H-carry event-conditioned realized-vol study, directional-vs-level signal sample enlargement. No new gate calibrated in this sweep.
6. Historical-ledger quality: VX_M1_HISTORY is not a pure front-month sample; VX_TERM_HISTORY and DIET study are frozen research inputs, not live daily measures. See workbook state register.

## OPERATING LIMITS

Full data/news sweep completed locally. Other desks' dirty work prevented pulling. Incoming packets were reviewed for context; no outbound messages sent. Completion delivery and remote artifact publication are separate from this file refresh; **Full closeout guard: 8/10 contracts pass; two delivery checks remain red because no PROME memo was sent.** This is an explicit scope exception, not a clean guard certification. Details are in the sweep report.
