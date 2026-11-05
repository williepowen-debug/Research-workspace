# TRADE CARD — CF Industries — post-Q3 supply tightening, December 125/135 call spread
**Date:** 2026-11-02
**Setup ID:** `IDEA-CF-Q3-NOV02`
**Thesis owner:** FERT; TERRY owns this prospective construction, not the fertilizer grade.
**Thesis reference:** FERT's October 28 frozen `AGENTS/FERT/workbook/GRADING_CARD_2026-11-03_MOS-CF-Q3.md`, commit `4b42bfd9a`; October 26 filing-based `companies/CF/README.md` and `Q3_PREP.md`; current FERT STATUS.
**Terry verdict:** CLOSED — WQ-593 RULED B, DECLINED (Will in PROME's chat 2026-11-04 20:59 ET, verbatim "approved with your recs"; record `PROME/proposals/2026-11-04_wq591-601-RULED.md`). Never approved, never filled, $0. FERT owns the Q3 read; CAL-0005 still resolves on its own date. (was: CONDITIONAL — NOT-FIRED; new proposal)
**Prepared:** 2026-11-02T10:27:55-05:00.
**Confidence in trade structure:** Low at the observed spread widths. Recommendation: conditional review only, no pre-results buy.

## 0. Risk and missing inputs
| Field | Figures / consequence |
|---|---|
| Default | **$500/card. X1 CLOSED / DON'T-SIZE.** Candidate **×1** only at debit **≤ $3.30**; maximum loss **$331.30**, including assumed $1.30 opening fees. Current deployment **0 / $0**. Going against X1 or using a larger size requires Will's per-card choice. |
| Position truth | `[POSITION_STATE_UNKNOWN]`; no assumed existing CF exposure or portfolio hedge credit. |
| Price / chain time | Required fetch.py: **CF $120.42, −2.34%, RED**, retrieval bracket beginning **November 2 10:26:10 EST**; session date only in price payload. Required chain `fetch_ts 10:26:12 local on November 2`, spot_asof 10:26, $120.42. Per-leg quote times/delay flags unavailable. Vendor screening marks, broker complex quote before any fill. |
| Missing | Live Greeks, IV rank, event expected move, broker fees and deliverable details unknown. Two 90-day chart pulls returned **0 bars** on DNS failure; daily/weekly trend, technical levels and relative-return verdicts withheld. All dollar entry/kill rails are proposed construction choices, not FERT thresholds or measured support. |
| Calendar | FERT frozen card says **November 4 after close results; November 5 call**. Its schedule source is **MIRROR**, not issuer-verified in this session. Entry requires the actual primary release plus FERT's existing two-stage read, so a calendar error cannot authorize a pre-print fill. |

## 1. One-line setup
Buy limited upside **after** CF's results if FERT's existing read finds a fresh, policy-linked tightening of Chinese urea supply and retained constructive demand. The spread seeks continuation of a confirmed company-specific supply update, not an earnings-gap lottery.

## 2. Evidence and trigger state
| Input | Dated evidence | Boundary / implication |
|---|---|---|
| Operating leverage | FERT October 26 primary filing baseline: H1 issuer adjusted EBITDA $2,175 million vs $1,405 million; product sales 8.935 million vs 10.025 million short tons. | Higher prices helped while volume shrank. $170 million litigation gain remains inside adjusted EBITDA; Q2 $50 million insurance recovery is distinct. No recurring-earnings or consensus-beat inference. |
| Supply mechanism | FERT October 28: Yara reports European ammonia curtailment; its frozen CF C1 test raises V1 **2→3 only if CF cuts its China 2026 export estimate below 4 Mt and explicitly attributes it to policy**. Prior estimate 4–6 Mt. | A potential reopening in one company's evidence, not proof today's nitrogen market is tight. |
| Counterevidence | FERT STATUS: broad nitrogen channel **DEAD**; India G2 awarded CFR >$600 not met; China G3 NOT-FIRED; imports/exports and allocation bases have known limits. | No broad-gate revival, no claim that CF's estimate is a Chinese government action. FERT's watch-only scores grant no capital permission. |
| **T1, proposed card condition** | Following the actual primary Q3 release/call, FERT records **C1 <4 Mt with explicit policy attribution** and C3's “constrained supply / constructive demand through 2026 into 2027” outlook **retained**, by November 6 close. | **NOT-FIRED:** Q3 evidence ahead, no result cells filled in the frozen card read. Only the existing FERT interpretation is used; no new study commissioned. |
| Additional tape condition | After that owner read, a completed CF close **≥ $125.00**, then an eligible red entry day. | Not met by the live $120.42 observation. Confirmation can cost more; an unaffordable chain means no trade. |

Original filing basis rechecked at [CF August 5 release, SEC Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1324404/000132440426000017/cf-08052026_ex991xearnings.htm). August's outlook is historical; Q3 must supply the new evidence. No phosphate-price signal is treated as CF nitrogen revenue.

## 3. Entry
After T1 and the completed-close confirmation, take the first **RED CF session** through **November 10**, share quote **$122.00–$129.00**, broker complex debit **≤ $3.30**. Root rule #6: calls on red days; no exception. Today's red tape is not permission to enter before results. If price exceeds $129, debit exceeds $3.30, the primary results/FERT read are absent, or the first eligible opportunity is missed, no chase; lapse unused by November 10. No automatic re-strike or recurring order.

## 4. Structure and live-tool screen
Buy Dec-18-2026 **125C**, sell **135C**, **×1** intact spread. Expiry 46 calendar days from November 2; post-print continuation view ends December 4. The long strike is **3.80% above** the current spot; the 135 short strike is **12.11% above**, a payoff ceiling rather than a forecast that one earnings print can reach it. No pre-print fill; the bank-print envelope is not imported into this sector.

| Leg | Bid / ask | Width / mid | OI / volume | IV |
|---|---:|---:|---:|---:|
| Buy 125C | $4.80 / $6.10 | 23.85% | 276 / 7 | 46.97% |
| Sell 135C | $2.00 / $3.30 | 49.06% | 835 / 301 | 48.02% |

Required chain tool **November 2 10:26:12 local**, named legs clean. Outer purchase **$4.10**, liquidation **$1.50**, leg-mid **$2.80**, not a fill. Round trip $2.60 / $2.80 = **92.86%**: this is a serious construction weakness. Outer risk ×1 $411.30 fits the $500 default but **exceeds this proposed $3.30 entry cap by $80**. The card waits for a substantially better broker complex market, plausibly after event premium clears; that improvement is not guaranteed. Raw stdout: `../research/2026-11-02_WQ590-week-ideas/CF_dec18_chain.txt.receipt.json`.

## 5. Independence and size
| Field | Assessment |
|---|---|
| N_claimed / N_eff | **3 / 1**: pricing power, European curtailment and a China supply revision all share nitrogen supply/demand tightness. One view, one small spread. |
| Book relationship | Different near-term resolver from banks/AI credit, but still an equity and commodity producer; oil/war and global-demand roots overlap existing energy exposure. **Not a second independent $500 budget beside UNG**: higher US gas can hurt CF input costs. No measured net hedge. |
| Edge / Kelly | Public evidence; no valuation or consensus model, positive option expectancy unproved. No Kelly sizing or precise profit odds. |
| Candidate at cap | ×1 × $330 + $1.30 = **$331.30**, **1.3252R** at STATUS's $250 unit. Terminal maximum gain **$668.70** before closing costs; fee-inclusive breakeven **$128.313**. Numbers are payoff arithmetic, not a price target. |
| Alternatives | Three CF shares cost $361.26 at the screen, with full equity downside and earnings exposure; the proposed vertical fixes loss mechanically. Outright 125C ask $610.65 exceeds $500; far-OTM calls would turn the view into a tail lottery. |

## 6. Management written before any fill
| Rail | Prospective rule |
|---|---|
| Harvest | Sell the whole spread at executable complex bid **≥ $6.60**; net gain **$327.40** at a 3.30 entry and $1.30 fees each way. |
| Kill | Exit all on **CF completed close < $115.00**, FERT retracting the qualifying supply/outlook read, or executable complex bid **≤ $1.65**. At exactly 1.65, modeled loss $167.60 including round-trip fees; a gap can lose all $331.30. |
| Time stop | Close by **December 4 close**, regardless of P/L. |
| Roll / add / review | None pre-approved. Review at FERT's already scheduled Q3/call reads or material owner change; no new monitor. A missed entry or different strike needs rework and Will. No prompt on a held line. |

## 7. Why not
China can export more, nitrogen prices can normalize, and CF can lose volume or spend more on Blue Point despite attractive product prices. FERT has no valuation or consensus-surprise model here. A favorable owner grade can already be in the stock, and post-print IV compression can hurt a call. **The observed option market is too wide for an entry recommendation**; a $3.30 limit is a condition, not an assertion someone will fill it.

## 8. Trigger forecast, WQ-493 A
| Field | Pre-outcome registration |
|---|---|
| Event | FERT records the full T1 conjunction: policy-linked China export estimate below 4 Mt and retained constructive supply/demand outlook after CF Q3. |
| Deadline | November 6, 2026, 16:00 ET. |
| Resolver | FERT frozen grading card C1/C3 results, with source-located issuer release/call; the existing <4 Mt/policy test controls. Missing source stays unresolved. |
| Probability | **0.25, subjective TERRY**; European curtailment supports the possibility, current China/India counterevidence argues against it. `CAL-0005`. Predicts T1 only, not tape confirmation, affordable entry or profit; no calibrated model or sizing authority. |

## 9. Decision route
PROME registers a separate Will decision before presenting an approve/reject ask. WQ-590 authorizes a fresh card, not purchase. Recommend a conditional only; the current screen is unattractive. Confirm standard 100-share deliverables and broker handling. Early assignment/broker intervention can create cash/share obligations beyond the intact managed spread's terminal payoff.

**APPROVAL REQUIRED — Will must approve/reject before execution.**
