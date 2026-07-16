# WAS THE US REPO MARKET CALM DURING THE SVB WINDOW (MAR 9–16, 2023)?
**Date:** 2026-07-16 | **Mode:** Thesis | **Confidence:** High (on repo); Medium (on MOVE date attribution)

## Key Finding
**Repo was genuinely calm — the "calm repo" narrative survives an active attempt to refute it.** Secured funding stayed *below* IORB throughout the window; SOFR moved 3bp (4.55%→4.58%). The best disconfirming evidence found is real but small: the **99th percentile of SOFR crossed above IORB on Mar 14–16 (peak +7bp on Mar 15, vs −3bp pre-stress)** and SOFR volume rose ~17%. That is a detectable tail-firming, not a dislocation. Stress in March 2023 surfaced in **other channels** (discount window, BTFP, FHLB advances, Treasury vol/liquidity) — claim (b), not claim (a).

## Data Table

| Date | Item | Figure | Source URL | Tag |
|---|---|---|---|---|
| 2023-03-08 | SOFR | 4.55% | [FRED SOFR](https://fred.stlouisfed.org/series/SOFR) | PRIMARY |
| 2023-03-09 | SOFR | 4.55% | FRED SOFR | PRIMARY |
| 2023-03-10 | SOFR | 4.55% | FRED SOFR | PRIMARY |
| 2023-03-13 | SOFR | 4.55% | FRED SOFR | PRIMARY |
| 2023-03-14 | SOFR | 4.55% | FRED SOFR | PRIMARY |
| 2023-03-15 | SOFR | **4.58%** (window high) | FRED SOFR | PRIMARY |
| 2023-03-16 | SOFR | 4.57% | FRED SOFR | PRIMARY |
| 2023-03-17 | SOFR | 4.55% | FRED SOFR | PRIMARY |
| 2023-03-08→17 | IORB | 4.65% flat (4.90% from 2023-03-23) | [FRED IORB](https://fred.stlouisfed.org/series/IORB) | PRIMARY |
| 2023-03-08 | SOFR99 (99th pctile) | 4.62% | [FRED SOFR99](https://fred.stlouisfed.org/series/SOFR99) | PRIMARY |
| 2023-03-10 | SOFR99 | 4.61% | FRED SOFR99 | PRIMARY |
| 2023-03-13 | SOFR99 | 4.63% | FRED SOFR99 | PRIMARY |
| 2023-03-14 | SOFR99 | 4.69% | FRED SOFR99 | PRIMARY |
| 2023-03-15 | SOFR99 | **4.72%** (window peak) | FRED SOFR99 | PRIMARY |
| 2023-03-16 | SOFR99 | 4.69% | FRED SOFR99 | PRIMARY |
| 2023-03-17 | SOFR99 | 4.64% | FRED SOFR99 | PRIMARY |
| 2023-03-15 | SOFR75 | 4.66% (from 4.57% on 3/8) | [FRED SOFR75](https://fred.stlouisfed.org/series/SOFR75) | PRIMARY |
| 2023-03-14 | SOFR1 (1st pctile) | 4.40% (window low) | [FRED SOFR1](https://fred.stlouisfed.org/series/SOFR1) | PRIMARY |
| 2023-03-10 | SOFR volume | $1,088B (window low) | [FRED SOFRVOL](https://fred.stlouisfed.org/series/SOFRVOL) | PRIMARY |
| 2023-03-16 | SOFR volume | $1,272B (+17% vs 3/10) | FRED SOFRVOL | PRIMARY |
| 2023-03-08→17 | EFFR | 4.57%→4.58% (+1bp total) | [FRED EFFR](https://fred.stlouisfed.org/series/EFFR) | PRIMARY |
| 2023-03-09 | ON RRP take-up | $2,229.6B | [FRED RRPONTSYD](https://fred.stlouisfed.org/series/RRPONTSYD) | PRIMARY |
| 2023-03-14 | ON RRP take-up | $2,042.6B (window low, −$187B) | FRED RRPONTSYD | PRIMARY |
| 2023-03-22 | ON RRP take-up | $2,279.6B (rebound) | FRED RRPONTSYD | PRIMARY |
| 2023-03-16 | MOVE index | **198.71 intraday high** (NOT 3/15) | Yahoo ^MOVE via FORGE | UNVERIFIED (vendor) |
| 2023-03-20 | MOVE index | 182.64 (highest *close* in window) | Yahoo ^MOVE | UNVERIFIED (vendor) |
| 2023-03-09 | MOVE index | 129.28 close (pre-stress) | Yahoo ^MOVE | UNVERIFIED (vendor) |
| mid-Mar 2023 | Treasury market depth | "fell substantially" | [Fed FSR May 2023, Asset Valuations](https://www.federalreserve.gov/publications/2023-may-financial-stability-report-asset-valuations.htm) | PRIMARY |
| mid-Mar 2023 | Treasury bid-ask intraday vol (short maturities) | "levels last seen in March 2020" | Fed FSR May 2023 | PRIMARY |
| week 1 post-3/12 | Discount window primary credit | <$5B → >$150B | [Fed FSR May 2023, Funding Risks](https://www.federalreserve.gov/publications/2023-may-financial-stability-report-funding-risks.htm) | PRIMARY |
| Mar 2023 | BTFP credit | stabilized $70–80B | Fed FSR May 2023, Funding Risks | PRIMARY |
| week ending 2023-03-17 | FHLB total debt outstanding | +~$250B → $1.5T | Fed FSR May 2023, Funding Risks | PRIMARY |

### Derived: SOFR−IORB and SOFR99−IORB spreads (bp), IORB = 4.65%

| Date | SOFR−IORB | SOFR99−IORB |
|---|---|---|
| Mar 8 | −10 | −3 |
| Mar 9 | −10 | −3 |
| Mar 10 | −10 | −4 |
| Mar 13 | −10 | −2 |
| Mar 14 | −10 | **+4** |
| Mar 15 | **−7** | **+7** ← peak |
| Mar 16 | −8 | **+4** |
| Mar 17 | −10 | −1 |

## Evidence

**1. NY Fed / Fed primary sources do not treat repo as a stress point.** I searched Liberty Street Economics and federalreserve.gov/econres/notes for March-2023 repo/money-market analysis. The striking result is a **negative finding**: the Fed's own retrospectives on this episode analyze bank runs, deposit flows, MMFs, bond funds, FHLB advances, and the discount window — and **do not discuss repo dislocation at all**. ["Anatomy of the Bank Runs in March 2023"](https://libertystreeteconomics.newyorkfed.org/2024/12/anatomy-of-the-bank-runs-in-march-2023/) [PRIMARY] finds "almost all run-on banks borrowed from Federal Home Loan Banks (FHLBs), whereas only a few borrowed from the discount window." ["Bank Funding during the Current Monetary Policy Tightening Cycle"](https://libertystreeteconomics.newyorkfed.org/2023/05/bank-funding-during-the-current-monetary-policy-tightening-cycle/) [PRIMARY] finds "a substantial amount of liquidity was provided by the private markets, likely via the FHLB system." No repo dislocation is described in either. The Fed's May 2023 Financial Stability Report "Funding Risks" section likewise contains **no repo-stress analysis**.

*Caveat on this evidence class:* absence of discussion is weaker than an affirmative "repo functioned normally" statement. I could not source such an explicit affirmative sentence about repo specifically. The FRED tape below is the load-bearing evidence, not the blog absence.

**2. The rate tape shows firming, not dislocation.** SOFR ranged 4.55–4.58% across the entire window — a 3bp move, and it stayed **7–10bp BELOW IORB throughout**. In a genuine repo dislocation, secured rates print *above* the administered ceiling, and print big: in September 2019, SOFR hit 5.25% against an IORB of ~2.10% — roughly a **300bp** overshoot. The March 2023 analog is a **7bp overshoot at the 99th percentile only**, with the volume-weighted median never leaving its pre-stress band. That is two orders of magnitude apart.

**3. Collateral was abundant, not scarce.** ON RRP take-up stayed above $2.0 trillion every single day of the window [FRED RRPONTSYD, PRIMARY]. Cash lenders had over $2T they were voluntarily parking at the Fed rather than lending in repo. A repo market cannot be liquidity-starved while $2T of cash sits idle at the ON RRP facility — the dip to $2,042.6B on Mar 14 (−$187B from 3/9) is consistent with *some* cash rotating into private repo (which is why SOFR99 firmed), i.e. the facility absorbing the shock exactly as designed.

**4. Stress went to OTHER channels — and it was enormous there.** Discount window primary credit went from **<$5B to >$150B in one week** — a >30x move [Fed FSR May 2023, PRIMARY]. FHLB debt outstanding rose **~$250B in the week ending Mar 17** [same]. BTFP was created from nothing and ran to $70–80B. Compare the magnitudes: DW +$145B and FHLB +$250B, against a 3bp SOFR move. **The stress was real and severe; it simply did not route through repo.**

**5. Treasury market ≠ repo market.** MOVE hit an intraday high of **198.71 on 2023-03-16** (highest close 182.64 on 3/20), against a 129.28 close on 3/9 — a ~54% surge [Yahoo ^MOVE, UNVERIFIED vendor tag]. The Fed FSR [PRIMARY] confirms Treasury market depth "fell substantially in mid-March," bid-ask spreads "rose marketwide," and intraday bid-ask volatility on short maturities "rose to levels last seen in March 2020." **But this is Treasury cash/options volatility, not secured funding.** And even here the Fed's verdict is qualified: *"Despite these strains, Treasury markets continued to function throughout the episode without severe dislocations or reports of investors being unable to transact."*

## Counter-Evidence (the disconfirming case, presented at full strength)

**The strongest single piece of disconfirming evidence: SOFR99 crossed above IORB on Mar 14–16.** The 99th percentile ran −3bp to −4bp vs IORB pre-stress and flipped to **+4/+7/+4bp on Mar 14/15/16**, returning to −1bp by Mar 17. This is a genuine, primary-sourced, date-aligned signal that *some* repo borrowers paid above the administered rate precisely in the SVB window. It is not nothing: it means the tail of the distribution felt the event.

Supporting disconfirming points:
- **SOFR75 moved more than the median** — 4.57%→4.66% (+9bp) vs the median's +3bp. The *distribution widened*; the headline rate understates it. The 1st percentile fell to 4.40% on Mar 14 (from 4.48%), so the **1st-to-99th spread widened from ~14bp to ~29bp on Mar 14** — it roughly doubled. Anyone citing only "SOFR moved 3bp" is compressing a distributional event into a point estimate.
- **Volume rose ~17%** (1,088→1,272 $B, Mar 10→16). Rising volume alongside rising tail rates is consistent with a real scramble for cash at the margin.
- **The Fed's silence is not evidence of calm.** The FSR "Funding Risks" section not discussing repo could reflect editorial focus on the bank-run story rather than an affirmative finding of repo health.

**Why I do not think this overturns the verdict:** the tail-firming is +7bp for three days and fully mean-reverts by Mar 17 with no facility intervention aimed at repo. The 2019 comparison (300bp) and the concurrent >30x discount-window surge establish the scale. A market where the *median* never leaves its pre-stress band and the *worst* print is 7bp over IORB is a market absorbing a shock, not dislocating.

**What would disprove "repo was calm":** tri-party or GCF repo prints materially above IORB (I could not source these — see Gaps); a Fed standing-repo-facility (SRF) drawdown spike in the window; evidence of failed repo trades or dealer balance-sheet refusal; intraday SOFR prints far above the 99th percentile.

## Source Quality Assessment
Strong on the rate tape — every SOFR/IORB/RRP/EFFR figure is NY Fed data via FRED [PRIMARY], the authoritative source for exactly this question, at daily frequency with the full published distribution. Strong on the "other channels" claim — Fed FSR is primary. **Weak on MOVE** — Yahoo `^MOVE` is a vendor redistribution of an ICE index, not a primary source, and Yahoo index series are known in fleet memory to carry date-shift risk (`finding_yahoo_sparse_index_date_shift`); the 198.71/Mar-16 attribution should be confirmed against ICE or Bloomberg before it is load-bearing. **Weak on affirmative Fed statements about repo** — I have a negative finding (no Fed source discusses repo stress), not a positive quote.

## Gaps
1. **Tri-party / GCF / DVP repo rates and fails data not pulled.** SOFR is a broad tri-party-inclusive measure; GCF repo (interdealer) is where a dealer-side squeeze would show first, and DVP fails are the classic dislocation tell. Neither sourced. This is the biggest hole in the disconfirming hunt — I hunted in the SOFR distribution, not in the segment most likely to break.
2. **No explicit affirmative Fed/NY Fed sentence stating repo functioned normally in March 2023.** Verdict rests on the data tape plus an absence-of-discussion argument.
3. **Standing Repo Facility (SRF) take-up in the window not pulled** — would be a direct test.
4. **MOVE not verified against a primary/ICE source**; the prompt's "~198 on Mar 15" claim is **close on value but wrong on date** — 198.71 was an *intraday high on Mar 16*, and no close in the window exceeded 182.64 (Mar 20, i.e. *after* the window). If the original claim meant a closing value, it is unsupported.
5. **Bloomberg US Government Securities Liquidity Index** — paywalled, not sourced. Used the Fed FSR's qualitative market-depth description as a substitute.
6. **No intraday SOFR data** — the published distribution is daily; a few-hour squeeze could hide inside a calm daily print.

## VERDICT

**Repo was calm during Mar 9–16, 2023.** The evidence points clearly one way. SOFR traded 4.55–4.58% and remained 7–10bp *below* IORB every day of the window; the volume-weighted median never left its pre-stress band; ON RRP take-up stayed above $2.0T throughout, meaning cash lenders had two trillion dollars they declined to deploy into repo — the definitional opposite of a funding squeeze. The Fed's own retrospectives on this episode (Liberty Street's bank-run and bank-funding analyses, the May 2023 FSR) analyze deposit flight, FHLB advances, the discount window, MMFs, and bond funds — and never identify repo as a stress point.

Critically, **claim (b) is supported, not claim (a)**: stress in March 2023 was severe but routed around the secured funding market entirely. Discount window primary credit went from <$5B to >$150B in a week; FHLB debt outstanding rose ~$250B in the week ending Mar 17; BTFP was stood up and ran to $70–80B; Treasury volatility spiked ~54% and Treasury market depth "fell substantially." Repo moved 3bp. The transmission channel was **bank-level liquidity replacement via administered facilities and the FHLB system**, not a breakdown in secured funding. Anyone reasoning from "March 2023 was a funding crisis" to "repo dislocates in bank stress" is fitting the wrong channel.

**Strongest disconfirming evidence found against this verdict:** the **99th percentile of SOFR flipped from −3bp to +7bp versus IORB on Mar 14–16** (SOFR99: 4.62% on 3/8 → 4.72% on 3/15), while the 1st-to-99th percentile spread roughly doubled from ~14bp to ~29bp and volume rose 17%. The repo *distribution* demonstrably widened in the SVB window even though the *median* did not move. This is a real signal and it deserves to be stated rather than smoothed away — the honest framing is "the tail felt it, briefly." But at +7bp for three days, fully mean-reverting by Mar 17 with no repo-directed intervention, against a September-2019 benchmark of a ~300bp overshoot, it is a rounding error on the scale of dislocation. It qualifies the word "calm"; it does not overturn it.

## Process Report
**Searches run:** ~6 (Liberty Street targeted domain search, FEDS Notes domain search, MOVE peak search, 3 primary WebFetches). Domain-restricted search on libertystreeteconomics.newyorkfed.org worked well. The decisive material came from the **primary FRED pull, not the web search** — again consistent with the standing carve-out finding.
**Data gaps:** GCF/tri-party repo rates, DVP fails, SRF take-up, Bloomberg liquidity index — all unreached (see Gaps).
**Source frustrations:** No `yfinance` in `FORGE/tools/market-data` cwd — required the repo-root `.venv/bin/python` (matches `finding_market_data_venv_invocation`). MOVE has no free primary source; ICE does not publish it openly.
**Confidence:** High on the repo verdict (daily primary data from the authoritative publisher, unambiguous, and cross-checked against a second independent indicator in ON RRP). Medium on the MOVE date/value.
**If I had more time/tools:** pull GCF repo + DVP fails from OFR's short-term funding monitor (`app.financialresearch.gov/short-term-funding-monitor`) — that is the single highest-value unclosed gap and it would either strengthen or genuinely dent this verdict; verify MOVE against ICE.
**Suggestions:** an OFR short-term-funding-monitor puller belongs in `scripts/` — this is the second repo-plumbing question where GCF/fails data was the gap. BACKLOG candidate.
