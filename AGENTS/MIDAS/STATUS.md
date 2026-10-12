# MIDAS — STATUS

**Last Updated:** 2026-10-12T17:03:53-04:00 — Will-directed due metals review, Codex. **Composite 8/20 unchanged; no capital or threshold change.** Full sourced review: `analysis/2026-10-12_due-metals-review-held-GLD.md`. Prior page archived verbatim at `analysis/STATUS_ARCHIVE_2026-10.md`.
**Class:** Market-agent · Fleet maturity L4 · Cadence WEEKLY · five-leg boot: metals, ledger staleness, predictions, gold COT, Ag/Pt/Pd COT.

## LIVE MARKS AND BASIS

All quotes below retrieved 10/12 from explicit same-contract VENDOR daily bars dated **10/9**. These are last-trade bars, **not exchange-certified settlements**. ETF closes are unadjusted. Today's mutable bars do not enter metrics. FRED latest-revised yield ends **10/8**; COT is **10/6**, not today's flow.

| Metal | Contract | 10/9 vendor bar | Since 9/30 | ETF 10/9 |
|---|---|---:|---:|---:|
| Gold | `GCZ26.CMX` (Dec 2026) | $4,216.30 | +0.71% | GLD $384.58 |
| Silver | `SIZ26.CMX` (Dec 2026) | $61.05 | +0.80% | SLV $54.78 |
| Platinum | `PLF27.NYM` (Jan 2027) | $1,693.30 | -1.49% | PPLT $15.25 |
| Palladium | `PAZ26.NYM` (Dec 2026) | $1,150.40 | -5.11% | PALL $20.77 |
| Copper | `HGZ26.CMX` (Dec 2026) | $6.69 | +1.06% | CPER $40.31 |

Explicit-month **GSR 69.07** (GCZ26/SIZ26), Pt/Pd **1.472**, Pt/Au **0.402**. DFII10 **2.87% [10/8 FRED MIRROR-WALLED]**; Treasury direct check failed, BOND owns the level. LME Cu **233,025t [10/9] = −0.69% vs 234,650t rolling 2yr median** (Westmetall LME mirror). Boot quote ~16:51 ET 10/12: GLD **$382.15, −0.63%**, not a certified close.

**Instrument warnings:** (1) futures daily vendor bars are not a settlement source; never certify a fast-info quote as a settle; (2) SI=F/HG=F/PL=F/PA=F are DYING on 10/9 volume, so quote explicit contracts and no cross-roll deltas; GC=F matched GCZ26; (3) a bar that can still move is not a close; pull again/T+1 for grading. `FRONT_MONTHS` is hand-maintained; PLF27 remains the mapped front month.

## HELD GLD

**17 shares** in the 10/11-received FORGE mirror, capture/mark time UNKNOWN; off-repo Will/broker truth controls. At the mirror's $384.58, $6,537.86 = **19.64% of Fidelity's $33,284.88**. The independently retrieved 10/9 GLD close happens to match that mark, but does not date the capture. Old 16-share arithmetic is superseded.

**Rolling-120 GLD/DFII10 beta −0.1632%/bp (t −4.83, R² 0.165, n=120, 4/20→10/8)**. Intercept OLS, percentage GLD daily returns on same-date DFII10 change in bp, latest-revised FRED. **−0.08 flip NOT reached.** Implied 17-share local response **−$106.71 per +10bp** at 10/9 mark; association, not causal identification or a net hedge ratio. 20/60-session betas −0.1155/−0.1397. 9/29 construction reproduces −0.1684; replay 9/23 is −0.1545 vs archived −0.1551, unresolved vintage/sample difference because old paired inputs were not frozen.

Gold remains relevant to fiscal/monetary diversification, but GLD is not a dependable hedge against rising real yields. September global ETFs added **$10bn/67t**, holdings **4,256t** (WGC 10/7, through 9/30), even as September spot gold fell **8.5%** (WGC). Global ETF totals are not GLD-specific flows. August reported CB net buying **39t, 170t YTD** (WGC 10/6) excludes unreported buying and cannot replace the quarterly total-demand kill test. Historical VECTOR-3 falsifier FIRED on 9/11 and 9/18; today's regression does not erase it. **TERRY owns action and live book sensitivities:** FORGE now carries 10 TBT and one TLT $82P Oct-16 with 10/14 management clock; old Sep-30 $77P delta is inapplicable. Net coverage UNVERIFIED.

## CONVERGENCE MATRIX

| # | Channel | Score (1–5) | Local state | Independence | Key signal [source/date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| M1 | Gold / real rates | **4** | Current tape is rate-sensitive; structural ETF demand persists. No new decoupling grade. Historical MIDAS-06/08 remain terminal; gold $4,216.30 is +4.11% above $4,050 flip and below $4,340.70 consumed key. Carve-outs: diverge-test-not-composition; rates-ASSISTED; un-banded. | monetary root shared with M2 | Beta −0.1632 [to 10/8]; COT 53.1003% [10/6], p97.12; ETF 4,256t [9/30] | No live registered successor; register beta with window, vintage, basis and existing flip, after prospective base-rate design |
| M2 | Silver / GSR | **1** | Bands ADOPTED LIVE-BUT-UNSCORED. Current would-be silver 3. Ratio below yellow is not evidence of calm in both price legs. | monetary + industrial, shared precious root | SIZ26 $61.048 [10/9]; SLV d200 −16.71%; GSR 69.07; silver COT 22.0232% [10/6] | GSR >85 for 3+ sessions; standalone scoring subject to WQ-352 floor and CROSSING letter |
| I1 | Copper / China | **1** | Downside conjunction clear; upside remains UNSCOREABLE under old bands. September construction rebound contradicts carrying August collapse forward. LME draw alone still confounded by venue relocation. | China/industrial root | HGZ26 $6.692 [10/9]; LME 233,025t; construction 50.3 [NBS Sep], mfg 50.1, composite 50.7 | Copper −20% AND LME +100% for collapse; no new upside band authorized |
| I2 | Platinum / palladium | **2** | Bands ADOPTED LIVE-BUT-UNSCORED. Would-be Pt2/Pd3. Pt crossed −15% post-approval on 10/7, then recovered; Pd's −20% cross was pre-approval 10/1. WPIC 2026 +265koz surplus verified; Pd supply call not paying in tape. | precious + supply; not independent votes | PLF27 $1,693.30 / PAZ26 $1,150.40 [10/9]; COT Pt21.2060% / Pd−33.3191% [10/6] | Confirmed major SA/Russia outage→4; standalone scoring subject to one-month floor and qualifying crossing |

**Actual composite 8/20 = 4+1+1+2.** Current all-levels counterfactual **11/20 = 4+3+1+3** is diagnostic only. Shared monetary/precious antecedents count once; no four-signal inference from correlated metals.

## STANDALONE BAND READ — EVERY LEG

| ETF | T d200 | C dd252 / decayed level | S upside | Current would-be max |
|---|---|---|---|---:|
| SLV | −16.71% →3 | −48.13%, old crash decayed →1 | below +30% →1 | 3 |
| PPLT | −13.47% →2 | −39.54%, old crash decayed →1 | below +30% →1 | 2 |
| PALL | −21.96% →3 | −44.14%, old crash decayed →1 | below +30% →1 | 3 |

No C/S crossing post-approval through 10/9. **PPLT T −15% first crossed 10/7 at −16.31%**, recovered 10/9; T is state, so the old cross is not a permanently latched score. **PALL T −20% crossed 10/1 at −20.18%, before the 21:40 ET approval**, then stayed below; no post-approval first crossing. The 9/30 "1.0pt from orange" expectation is superseded by that exact timing. PALL 10/7 −24.04% did not cross red −25%. **No scores before 11/1 21:40 ET**. WQ-368 remains pending: CROSSING waits for a qualifying post-approval crossing; CALENDAR promotes existing levels. Operative letter CROSSING; keep day-31 adjudication with Will. Design-fixed bands include the collapse they fit; context, not an out-of-sample proof.

## COT — CONSUMED 10/12, AS-OF 10/6

| Metal | OI contracts | Net NC contracts | Net/OI | Frozen full-history percentile |
|---|---:|---:|---:|---:|
| Gold | 396,109 | 210,335 | 53.1003% | 97.12 |
| Silver | 105,130 | 23,153 | 22.0232% | 52.18 |
| Platinum | 65,868 | 13,968 | 21.2060% | 25.23 |
| Palladium | 21,060 | -7,017 | -33.3191% | 16.06 |

Gold **−0.6897pp WoW**, net −8,297, OI −10,347: third weekly de-crowding, still top 2.9% (frozen n868). Non-gold n872 references; Pt/Pd post-2022 regime shifts limit full-history ranks. Context only, no positioning band. Raw response and all identities saved. Per-metal Ag/Pt/Pd consumed ledger boot-wired; no automatic consumption.

## EXIT / INVALIDATION — standing rule | current state | fire

Rules remain on their 8/7 re-derived letter; observations updated 10/12. Historical endpoint-basis fire preserved under Will's 8/21 ruling.

| Channel | Standing rule | Current state @ date | FIRED? |
|---|---|---|---|
| M1 | Gold <$3,317 without yield spike; WGC CB <100t/q; gold re-decouples up for 3+ weeks, weekly endpoint basis | GCZ26 $4,216.30 [10/9], +27.11% over shelf; carried Q2 CB 288.9t above100t, not refreshed; Aug39t monthly reported is a different object. 9/17→10/8 real yield +26bp and GLD −4.96%, no new shape | Historical leg3 FIRED 7/17→8/7; no new fire; quarterly leg uses carried quarter |
| M2 | GSR >95 sustained | 69.07 [10/9 explicit months] | NOT-FIRED |
| I1 | Copper −20% AND LME stocks +100% | HGZ26 +1.06% since9/30, CPER r63+6.25%, d200+7.18%; LME −0.69% vs contemporaneous median [10/9] | NOT-FIRED |
| I2 | Major SA/Russia PGM outage/sanction | No fresh major event established in bounded sweep; corrected Irkutsk story is not a production outage; US Pd duty channel remains closed | NOT-FIRED |

**Fired-count: 1 of 4, historical.** Bidirectional M1 flip: gold <$4,050 with DFII10≥2.40 →2; **NOT fired**, +4.11% margin on the current explicit December vendor bar. A futures level near the boundary still requires exchange settle/basis verification.

## OPEN ON MIDAS — TOP 3

1. **M1 live successor remains owed:** today's beta remeasurement is diagnostic, not a score-changing new letter. Window/vintage/basis/base-rate design must be prospective; WQ-161/162 apply. Review by **10/19 next weekly boot**.
2. **WQ-368 day-31 reading due11/1:** bands already adopted, never call WQ-352 pending. PGM mechanism remains unresolved without lease rates, NYMEX stocks and fund flows; HAWK's instrument-access negative was delivered9/2, so no sixth asking. BIS check still owed; bounded review10/19.
3. **I1 venue comparison incomplete:** current COMEX/SHFE series absent; construction→copper lag unknown. September50.3 print integrated; China's causal interpretation stays ZHAO's. MIDAS-09/10 resolve **10/30**; no early grades.

Full register `OPEN_ITEMS.md` remains boot-read. COT ledger wiring, SCRATCH rotation, float edge and WQ-399 syntax are DONE. NEXUS_BRIEF is current and below cap. No new action from Citi's forecast or Shelton's appointment. Irkutsk correction applied; no plague/production claim survives.

## BOTTOM LINE

The held gold position retains structural demand support, while the measured real-rate response remains negative; it should not be counted as a reliable hedge against rising real yields. Palladium is the weakest precious metal in this review period, and the band's approval timing excludes its October1 orange crossing. Platinum's October7 crossing qualifies as post-approval evidence, but all new bands remain unscored for the approved month. Next: 10/19 weekly review, 10/30 registered pair resolutions and WQ-368 by11/1; no new trade decision today.
- **Gold** Dec2026 `GCZ26` **$4,216.30 [10/9]**, +0.71% vs9/30; modest rate relief/ETF support, crowded longs declining.
- **Silver** Dec2026 `SIZ26` **$61.048 [10/9]**, +0.80% vs9/30; monetary recovery with solar-thrifting headwind, April forecast deficit46.3Moz newly primary-verified, COT middling.
- **Platinum** Jan2027 `PLF27` **$1,693.30 [10/9]**, −1.49% vs9/30; rates/investment flows dominate, WPIC forecasts2026 surplus265koz, post-approval trend crossing recovered.
- **Palladium** Dec2026 `PAZ26` **$1,150.40 [10/9]**, −5.11% vs9/30; supply-tightening call unconfirmed, COT net-short33.32%, no demonstrated fresh supply outage.
