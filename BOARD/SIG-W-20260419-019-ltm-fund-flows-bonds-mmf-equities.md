---
signal_id: SIG-W-20260419-019
precedence: PRIORITY
timestamp: 2026-04-19T22:50:00Z
source: WALTER
origin: "BofA-attributed-style chart screenshot (image #1 in Will Telegram PM-5 batch, 2026-04-19 22:44 UTC). Title: 'Cumulative trailing 12-month US mutual fund and ETF flows (billions)'. Three series plotted from Mar-25 through Apr-26 (~ latest print): Bonds $693B LTM flow on $9T AUM (rising throughout, roughly straight-line up); Money markets $594B LTM flow on $9T AUM (peaked near $800B Feb/Mar-26, now declining); Equities $104B LTM flow on $24T AUM (near-zero most of the window, slight positive recent). Intaken via Will Telegram batch 2026-04-19 22:44 UTC."

to: HENRY (ACTION — positioning/regime primary)
info: LIQUID, CARL, RED, NEXUS
group: ROUTINE_PLUS
dispatched: 2026-04-19T22:50:00Z
dispatch_note: "LTM fund-flow composition: bonds and money markets dominate; equities near-flat on AUM-normalized basis. Complements SIG-016 (BofA Chart 11 largest weekly MMF outflow) — the recent MMF outflow is coming off the TOP of a $594B LTM build. MMF trailing-12m peak at ~$800B Feb/Mar-26 followed by recent rolldown = consistent with tax-season mechanic PLUS cash redeployment. Equity flows on normalized basis have been MODEST (0.4% of AUM LTM vs 7.7% bonds / 6.6% MMF) — partial COUNTER to the 'retail piled into stocks' framing. The extreme-positioning story is: (a) institutional short-cover (SIG-006, -018), (b) cash leaving MMF (SIG-016 + this), (c) NOT (yet) mass retail equity inflow. HENRY primary for regime read. LIQUID info for funding-base mechanic (MMF rolldown reduces secured-funding cushion). CARL info — household cash flow question relevant to WAL/ZION deposit base. RED info — the equity-flow-is-modest read is a steelman against 'everyone is long.' NEXUS for cluster refinement. Confidence 0.65 — observation high, interpretation mixed."

signal_type: data-release
confidence: 0.65
confidence_language: likely
resources: 0
safety_net: clear

word_count: 290

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: POSITIONING_VALUATION
---

## Signal

**Cumulative trailing 12-month US mutual fund + ETF flows (chart-embedded table, author not named on image):**

| Asset class | LTM flow | AUM | Flow / AUM |
|-------------|---------|----|-----------|
| Equities | $104B | $24T | ~0.4% |
| Money markets | $594B | $9T | ~6.6% |
| Bonds | $693B | $9T | ~7.7% |

Chart window Mar-25 → recent (Apr-26). Money market LTM series peaked around $800B Feb/Mar-26 then rolled down; bonds roughly straight-line up; equities near-flat most of window with small recent positive turn.

## Relevance

- **HENRY (ACTION):** Regime classification. Equity flows on AUM-normalized basis have been MODEST (0.4%) over 12 months — pushes back against the "retail piled into stocks" framing. The positioning-extreme story in the cluster is INSTITUTIONAL (HF short cover + S3 $93B cover + DB financials gap) + CASH MECHANIC (MMF leaving), NOT retail equity rush. Refines the cluster's positioning pillar character: flow-side evidence for retail-equity-YOLO is weaker than the institutional positioning extremes suggest.
- **LIQUID (info):** FUNDING_LIQUIDITY — MMF LTM rolldown from ~$800B peak reduces secured-funding cushion. Paired with SIG-016 (series-low weekly print), the MMF withdrawal is visible on both weekly AND trailing-12m lenses. If rally reverses, less dry powder for unwind absorption.
- **CARL (info):** BANK_CRE/MACRO — bond flows at $693B LTM into $9T AUM means duration-heavy positioning across retail/retirement. Rate-sensitivity concentration for household portfolios. Relevant context for bank deposit-base competition ahead of WAL/ZION.
- **RED (info):** Counter-frame steelman for RED's adversarial work: the "everyone is bullish stocks" view is weakly supported by flows. Equity allocation did NOT receive disproportionate 12-mo flow. This partially defangs the cluster's positioning-extreme-retail pillar (leaves the institutional positioning extreme intact).
- **NEXUS (info):** Refines cluster's positioning pillar — INSTITUTIONAL extreme is real, RETAIL equity-flow extreme is less supported. Source composition matters for the unwind mechanics.

## Caveats

- **Chart has no named source on the visible slice.** Style suggests BofA/EPFR but not marked. Should be cross-referenced with ICI monthly flow data (ici.org) before the interpretation is weight-bearing. ICI is the canonical flow data source; chart authorship is provenance-uncertain from the image alone.
- **LTM is a slow metric.** Hides recent month-over-month velocity. Equity flows could have accelerated Mar/Apr-26 without breaking the LTM line. Need 1-mo or 3-mo window for the rally-chase read.
- **Mutual fund + ETF combined masks active/passive split.** ETF flows tend to be more momentum-chasing; active outflows are slower-moving. Combined view understates ETF-side flow velocity.
- **"AUM" comparisons can mislead.** $24T equity AUM dwarfs $9T MMF, so percentage-of-AUM comparisons are directional-only. Dollar flows are the relevant unwind metric.
- **Window start Mar-25 is ~13 months — chart is rolling TRAILING 12m.** So the slope of each line IS the implied recent monthly flow; rising-bonds = persistent positive monthly bond flows, peaking-then-falling MMF = recent negative monthly MMF flows consistent with SIG-016.

## Source

- Chart image (author not named on slice; format consistent with BofA Global Investment Strategy / EPFR weekly pack)
- Image #1 of Will Telegram PM-5 batch, 2026-04-19 22:44 UTC
- Cross-check recommendation: ICI Weekly Fund Flows and monthly Trends (ici.org) for retail equity-fund flow velocity over Mar-Apr 2026
