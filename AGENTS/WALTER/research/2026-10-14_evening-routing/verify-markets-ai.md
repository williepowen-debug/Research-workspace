# Verify pass: markets and AI items, 10/14 evening

Read-only verify helper for WALTER. Written about 00:30Z on Oct 15 (20:30 ET on Oct 14).
**Price basis:** unless another source is named, prices come from yfinance through `FORGE/tools/market-data` and are **single-source vendor data**. Session closes are for 2026-10-14. Pulled about 00:20Z on Oct 15.
**Hyperliquid basis:** figures come from the public Hyperliquid info API (`api.hyperliquid.xyz/info`), pulled 00:24Z on Oct 15.

---

## 1. S&P 500 "worst day since July 29th, erasing $800B"
**VERDICT: CONFIRMED for the S&P 500. The $800B is CORRECTED-FRAMING (rounded up). Event date: Wed 2026-10-14.**

| Index | 10/14 close | Change | Last worse day |
|---|---|---|---|
| S&P 500 | 7,718.94 | -86.51 / **-1.11%** | **7/29 (-1.52%)**. No day from 7/30 to 10/13 fell more. Earlier: 7/23 -1.21%. Next-worst since 7/29: 8/20 -0.87%, 9/28 -0.77%, 9/23 -0.75% |
| Nasdaq Comp | 26,692.87 | -511.51 / **-1.88%** | **7/23 (-2.15%)**. For the Nasdaq this is worse than 7/29 (-1.74%), so its marker is "worst since July 23" |
| Dow | 51,621.48 | -48.62 / -0.09% | Not notable |

- **Sources:** AP (Stan Choe, 10/14, via OPB) gives the same closes and "worst day since July". The yfinance ranking was computed from daily history.
- **$800B:** This is plausible in size, but it is a rounded-up figure that I did not compute from constituent data. A 1.11% drop on a total S&P cap of about $67–70T comes to roughly **$0.74–0.78T**. That cap range is inferred: a weak aggregator item from 9/15 said ">$800B over 3 days = 1.2%". Treat $800B as an upper-end round number.
- **Causes cited by AP:**
  - **Inflation:** September CPI was **3.7% y/y** against 3.6% expected (August: 3.4%). Fuel tied to the Iran war was a key driver.
  - **10-year Treasury:** it briefly rose **above 5.32%**, from below 5.17% before the release. yfinance ^TNX shows an intraday high of 5.329% and a close of 5.19%.
  - **Fed odds:** CME odds of **another hike at the next meeting (about 2 weeks away) rose to ~35% from 22%**. The Fed "recently raised its rate for the first time in three years."
  - **AI selloff:** CoreWeave (CRWV) -15.5%, Oracle (ORCL) -8.8%, AMD -5.7%, Nvidia (NVDA) -3.2%, Broadcom (AVGO) -3.1%, GE Vernova (GEV) -6.2%.
  - **Banks:** Bank of America (BAC) -4.8% and State Street -4.1%.
- **Also on 10/14 (yfinance):** semiconductor index (^SOX) -4.30%, Russell 2000 (^RUT) -1.93%, VIX 16.87 (+10.5%).
- **NEW vs board:** the market-level move, the CPI-plus-yields-plus-AI-debt mix, and hike odds at ~35%.

## 2. BAC "crashes over -8% … Q3 missed, net income -16%, down >22% over the last month" (BullTheory)
**VERDICT: CORRECTED-FRAMING. The fine is ALREADY-COVERED. Event date: 10/14, results released before the open.**

**Price (yfinance):**
- Previous close (10/13): $53.96.
- 10/14: open $49.83 (-7.65%), **low $49.26 (-8.71%)**, high $51.52, **close $51.39 (-4.76%)**, volume about 118M.
- AP's close figure agrees: -4.8%.
- ⇒ **"-8%" happened only at the intraday low. The stock closed down 4.8%.**

**1-month change:**

| Basis | Change |
|---|---|
| 9/11 close $62.69 to 10/14 close | **-18.0%** |
| 9/14 close $59.47 to 10/14 close | -13.6% |
| 9/11 intraday high $63.83 to 10/14 intraday low $49.26 | **-22.8%** |

The ">22%" figure only works on that high-to-low basis. **The close-to-close figure is 13.6–18.0%.**

**Q3 2026, from the 8-K filed 10/14 (EX-99.1 release and EX-99.3 supplement, SEC accession 0000070858-26-000481):**
- **Net income:** $6.933B vs $8.332B in 3Q25 as now presented, a **change of -16.8%**. The 3Q25 figure reflects a 4Q25 accounting-method change applied retrospectively; it was originally reported as about $8.5B and $1.06 per share. On that original basis the decline is about -18%.
- **EPS:** GAAP diluted **$0.91** vs $1.04.
- **Settlement charge:** **$1.2B, not tax-deductible, about $0.17 per share**. It accrues the OCC/FinCEN civil money penalties announced 10/13.
- **Excluding the charge:** net income $8.1B and EPS **$1.08**.
- **Revenue:** $29.958B, up 3% y/y.
- **Other lines:**

| Metric | 3Q26 | 2Q26 | 3Q25 |
|---|---|---|---|
| Net charge-offs | $1.349B | — | — |
| Net charge-off ratio | 0.44% | 0.47% | 0.47% |
| Return on equity (ROE) | 9.14% | 12.09% | 11.01% |

**Miss: CONFIRMED.**
- Adjusted EPS of $1.08 missed consensus of **about $1.10** (GuruFocus/Yahoo 10/14). Previews ranged from $1.10 to $1.18.
- Revenue missed estimates of about $30.6B (secondary sources).
- AP: profit "would have missed even without" the fines.

**Peers on 10/14 (yfinance):** JPMorgan (JPM) +1.16%, Wells Fargo (WFC) +0.20%, Citigroup (C) -1.81%, Goldman Sachs (GS) -1.48%, Morgan Stanley (MS) -2.75%, bank ETFs KBE -0.70% and KRE -0.75%. ⇒ **The BAC move was specific to BAC, not a bank-sector move.**

**NEW vs board:**
- The stock reaction.
- The miss on an adjusted basis, which shows the miss was not only the charge.
- The revenue miss.
- ROE down to 9.1%.

## 3. "OpenAI computing chief to depart: WSJ" (10/14)
**VERDICT: CONFIRMED (WSJ itself not read; paywalled). Event date: 10/14.**
- **Who:** **Sachin Katti**, OpenAI's "head of computing capacity" (WSJ framing via runtimewire, 10/14). Unite.AI gives his title as VP of compute strategy and GPT-Infra. He was previously Intel's CTO.
- **Tenure:** he joined around late 2025, so about one year.
- **Timing:** he leaves in **November**, with a **last day of Nov 15, 2026**, according to his LinkedIn post as quoted by Unite.AI on 10/14. He stays on as an **adviser**.
- **Reason:** "decided to move on to build something new". The new venture is not named.
- **Context:** OpenAI plans to spend about **$750B on compute through 2030** (WSJ via runtimewire; basis not given).
- **Earlier departures:** head of data centers Chris Malone left in **August 2026** (DCD). Earlier, Keith Heyde and Peter Hoeschele left (secondary source).
- ⚠️ **Successor is unverified.** One secondary source (FourWeekMBA) says Uday Ruddarraju, compute CTO since July, will lead. It has not been confirmed by a primary source.

## 4. CoreWeave CEO blames share drop on "irrational" market (10/14)
**VERDICT: CONFIRMED. Event date: 10/14.**

**Price (yfinance):**
- **Close $65.78, -15.46%**, from $77.81.
- Intraday low $64.41 (-17.2%). Volume about 109M.
- AP: "worst day since February".

**1-month change:**

| Basis | Change |
|---|---|
| vs 9/14 close $82.98 | **-20.7%** |
| vs 9/11 close $88.99 | -26.1% |
| vs 9/8 close $99.83 (high of the window) | -34.1% |

**The memo** (seen by Bloomberg, via Investing.com 10/14; a spokeswoman confirmed it is authentic):
- "there will be periods of time when the market misunderstands and acts irrationally".
- The backlog is "large enough to more than support its debt obligations".
- Rivals' weak or delayed IPOs and debt financings are "bleeding into the narrative around CoreWeave".

**🔴 Credit leg (NEW):**
- CoreWeave's **$1.25B unsecured notes due 2032** yielded about **15% intraday and closed at 14.5%**, against **9.625% at issue in June**. That level is typical of distressed debt.
- Chamath Palihapitiya flagged the move and Musk replied "Yikes."
- Source: Investing.com and Bloomberg. These are secondary sources; the bond levels have not been verified on TRACE.

**Same-day AI-infrastructure peers (yfinance):** Oracle (ORCL) -8.83%, Nebius (NBIS) -10.08%, Dell (DELL) -11.27%, Super Micro (SMCI) -8.42%, Marvell (MRVL) -8.73%.

## 5. Anthropic pre-IPO perpetual "<$2T on Liquid, >10% down in a month, >$200B wiped" (unusual_whales, 10/14)
**VERDICT: CORRECTED-FRAMING. The prices are real trades on a synthetic instrument; they are NOT a company valuation. Event date: 10/14 (UTC day).**

**Venue:**
- "Liquid" (liquid.trade) calls itself a "**non-custodial trading app**", not an exchange.
- Its pre-IPO markets are "perpetual markets that track a reference price for a private company … price exposure without owning equity", with no expiry date.
- It is not affiliated with the former Liquid/Quoine exchange.
- Its market ID is `io:ANTH`. The Hyperliquid API confirms the `io` venue is **EntropyIO, a third-party market launched on Hyperliquid under its builder-deployed market standard (HIP-3)**.
- The instrument is a **synthetic perpetual**, with max leverage 6x. It carries no equity and no claim on Anthropic shares.
- Hyperliquid blocks US users (secondary source).

**Live figures (00:24Z Oct 15):**
- Mark **$1,934.3**, oracle $1,933.3.
- Previous day $2,032.3, so **-4.8% over 24h**.
- 24h notional volume **$23.7M**.
- Open interest 20,532 contracts, about **$39.7M notional**. The market is thin.

**Daily closes (UTC):**

| Date | Close |
|---|---|
| 9/14 | $2,204.9 |
| 10/14 | $1,940.9 |

- 1-month change: **-12.0%**.
- From the 9/9 peak close of $2,279.5 (intraday high $2,359.3): -14.9%.

**Implied valuation:**
- Convention: price × ~1B shares. This is Bybit's stated convention, and it matches Tema's "$2.09T" for Oct 5.
- On that basis: about **$1.93T now vs $2.20T on 9/14**, roughly **$270B lower**.
- The claim's arithmetic holds **on that convention only**. The share count is an assumption, not a company figure.

**The actual company valuation:**
- Last primary round: **Series H, $65B at $965B post-money, 5/29/2026** (Orrick, Anthropic's counsel).
- The perpetual prices Anthropic at about **2.0x the last round**.

**Prices differ widely across venues:**

| Market | Mark | Open interest |
|---|---|---|
| Ventuals `vntl:ANTHROPIC` | $1,619 | zero |
| Paragon `para:ANTH` | $2,000 | zero |

**Must travel:**
- This is a different instrument from the Ornn GPU/inference price index corrected on 10/14. It is still not a valuation.
- Anthropic and OpenAI have warned against trading in unauthorized instruments tied to their securities (secondary source).
- **Unverified:** Liquid's own 10/13 X post attributed the decline to de-risking before a reported Q3 disclosure to institutional investors, plus a Bloomberg report of an IPO roadshow the week of Nov 9. I did not read the X post (HTTP 402).

## 6. "Auto loan market is $1.7T" (10/13 tweet)
**VERDICT: CONFIRMED, but it is NOT new data.**
- **Source:** NY Fed Household Debt and Credit report for **Q2 2026, released 2026-08-11**.
- **Auto loans:** **$1.713T** (+$28B q/q, +$58B y/y).
- **Originations:** $211B, a nominal record.
- **Serious-delinquency transition rate:** 3.00% (Q2'25: 2.93%).
- **Total household debt:** $18.771T (-$13B).
- **What the chart shows:** I did not see the tweet's chart. A $1.7T figure is the Q2 2026 vintage (or about $1.685T for Q1).
- **Next print:** the Q3 2026 report is due in early November. Don't route the tweet as a new print.

## 7. Musk praises Micron's "reasonable" pricing; "MU fell 3.2%"
**VERDICT: CORRECTED-FRAMING. The quote is confirmed; the 3.2% figure is wrong.**

**What Musk said:**
- Platform: posted on X **after the close on Tue 10/13, US time**. TrendForce dates it 10/14 (Asia time).
- He was replying to an analyst's summary of a JPMorgan note.
- Quote: Micron "has been reasonable regarding future memory prices, while others have been extortionate", and customers "won't forget" (TrendForce 10/14; Yahoo/BeInCrypto 10/14).
- He did not name rivals. The remark is widely read as aimed at Samsung and SK hynix.

**MU price (yfinance):**

| Date | Close | Change |
|---|---|---|
| 10/13 | $953.19 | **-3.62%** |
| 10/14 | **$914.13** | **-4.10%** |

- 10/14 was the **fifth straight decline**: -16.0% from the 10/7 close of $1,088.00, and -16.7% from the 10/1 peak close of $1,097.39.
- **The "3.2%" matches neither close**; it was probably an intraday snapshot. Musk's praise did not stop the slide.

**Supply-contract context (via TrendForce):**
- Micron had 26 long-term agreements (LTAs) by September, up from 16 in June.
- Commitments total $32B, up from $22B (Reuters).
- JPMorgan: LTAs could cover more than 75% of FY27 output (Money Today).

## 8. TrendForce: CSP capex >$1.5T in 2027; AI server revenue >+90%
**VERDICT: CONFIRMED (primary: TrendForce press release, 2026-10-14).**
- **Who is counted:** the **9 largest cloud providers (CSPs)**: Google, Amazon, Meta, Microsoft, Oracle, ByteDance, Tencent, Alibaba and Baidu.
- **Capex:**

| | Aug 3 release | Oct 14 release |
|---|---|---|
| 2026 | >$886.7B (~+90%) | **$957B (+106% y/y)** |
| 2027 | ~$1.3T (~+50%) | **>$1.5T (+60%)** |

- **AI servers:**

| | Revenue | Revenue growth | Share of all server revenue | Shipment growth |
|---|---|---|---|---|
| 2026 | ~$479B | — | ~75% of $639.2B | +32.2% |
| 2027 | **~$920B** | **>+90%** | ~81% | ~+36% |

- Total server revenue passes **$1T for the first time** in 2027.
- ⚠️ **Caveat: the growth is driven by prices.** Revenue grows about 90% while units grow about 36%. TrendForce attributes this to system and component price increases amid shortages, especially memory. It also says supplier **prepayments pull cash spending forward**. Much of the capex growth is price inflation and timing, not volume. All figures are projections.
- Oracle is one of the nine CSPs, and it fell 8.8% the same day on AI-debt fears.

## 9. AMD / Lisa Su at the Open Compute Project (OCP) summit: "year of inference"; 2030 CPU TAM $200B+
**VERDICT: CONFIRMED. The keynote was Mon 10/12 Pacific time; articles were dated 10/13.**
- **Source:** TrendForce, 10/13.
- **Su's quotes:**
  - 2026 is "really the year of inference".
  - Inference is "about 60% of the market going forward".
  - CPU total addressable market (TAM) of "over a $200 billion TAM by the time you get to 2030", at "approximately 50% CAGR over the next 4 or 5 years".
  - The CPU TAM has been raised "**three times in the last nine months**".
  - The data center AI accelerator TAM will "approach $1.5 trillion by 2030".

**Prior TAMs (secondary sources only):**

| Date | Venue | 2030 server-CPU TAM |
|---|---|---|
| Nov 2025 | Financial Analyst Day | ~$60B (~18% CAGR) |
| May 2026 | Q1 2026 earnings call | >$120B (>35% CAGR) |
| Undated | (Wolfe Research note) | A further raise above $120B |
| 10/12 | OCP keynote | >$200B |

- The undated raise is unverified.
- BofA's own estimate (6/11/2026) is >$170B.

**Caveats:**
- It is unconfirmed whether the $200B covers server CPUs only.
- A TAM is not AMD's revenue share.

**Products:**
- Helios production has shipped since September to OpenAI, Meta, Microsoft, Oracle and Anthropic.
- The Helion agentic AI rack is available from Nov 26.

**Stock:** AMD closed at **$570.82 (-5.73%) on 10/14**, after +1.90% on 10/13.

## 10. CPI diffusion (Anna Wong, Bloomberg Economics) and Robin Brooks
**Wong — VERDICT: CONFIRMED in substance from secondary sources only. Bloomberg Terminal/BE note not accessed; the article is paywalled.**
- **Source:** investingLive (Eamonn Sheridan, 10/14).
- **The measure:** BE's gauge is the **share of CPI components rising faster than 3%** a year. It is built like the PCE breadth gauge Wong links to Warsh.
- **Readings:**
  - The six-month annualized share is **about 40%, down from about 55% earlier in 2026**, and **it fell in September**.
  - The 12-month share eased by less; no figure was given.
- **Warsh comparison (search summary only, not fetched):** at Jackson Hole in August, Warsh cited **54%** of PCE items above 3% over 12 months. The six-month figure was about 49%, which BE estimates fell to 45% after the August PCE data.
- **Policy read (search summary):** Wong expects the Fed to **hold for the rest of the year, though the risk of a hike has risen**.
- **Caveat:** breadth measures how widespread price rises are, not how large they are, and one month is not a trend. The same article puts core CPI at 2.6% y/y, which I have not checked against BLS.

**Brooks — VERDICT: CORRECTED (date).**
- The robinjbrooks.substack.com post "**Is the Fed Behind the Curve?**" is dated **2026-09-19** on its page, not 10/14. The Oct 5–13 archive does not include it.
- Subtitle: "The Taylor Rule doesn't suggest the Fed is massively behind the curve."
- **Gist:** a Taylor rule (0.5 on the inflation gap, -2.0 on the unemployment gap) signals **about 50bp of hikes one year ahead**, matching the Fed's projections. Brooks argues the hawkish turn after Jackson Hole was a change in narrative, not a response to data, so **the Fed is not materially behind the curve**.
- This is a stale reshare. It is useful context but not news for 10/14.

---

**Overall:**
- 10/14 was a hot-CPI, rising-yield and AI-credit day. The S&P 500 fell 1.11% (worst since 7/29) and the Nasdaq 1.88%.
- **The new risk content is credit:**
  - CoreWeave's 2032 bonds at about 14.5–15% yield.
  - CoreWeave -15.5%, Oracle -8.8%, Dell -11.3%.
  - CME odds of a Fed hike rose to about 35%.
- **Framing fixes:**
  - **BAC:** -4.8% at the close (-8.7% was only the intraday low). It missed on an adjusted basis, not only because of the charge.
  - **MU:** -3.62% on 10/13 and -4.10% on 10/14, not 3.2%.
  - **Brooks:** the post dates from 9/19.
  - **Anthropic "valuation":** it is a thin synthetic perpetual (about $40M open interest) at roughly 2x the $965B Series H.
