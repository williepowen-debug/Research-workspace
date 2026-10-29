# Verify H4: corporate, AI financing and other bookmarks (20 posts)

Written 2026-10-29T15:27Z (from `date -u`) by a read-only verification helper for WALTER (Claude Opus 5.5). Owners grade the evidence. Nothing here was routed.
Full post text for all 20 IDs came from api.fxtwitter.com (`curl`, 2026-10-29 ~15:25Z). Images were viewed for items 9, 30, 32, 35, 47 and 54.
Vendor prices come from `FORGE/tools/market-data/fetch.py` and yfinance history. They are vendor figures, not certified closes. Moving averages (MAs) were computed from vendor daily closes.

## TOP SUMMARY
1. **Item 9, the "$200B AI capital call in one day", is CORRECTED-FRAMING.** It adds Meta's $97.5B, which includes a $60B Class C at-the-market (ATM) program with no agreement, starting Q1 2027. It also adds the $63B Broadcom/Anthropic SPV, which is committed but not funded, and the SpaceX/Apollo $40B lease, which ZH says "closing" but is a binding commitment still due to close before year-end 2026. Cash actually priced on Oct 26 is about $37.5B (Meta). What's new versus SIG-W-20261026-001: Meta priced on Oct 26 and **upsized the common to $25.0B** from $22.5B (FWP, SEC, Oct 27). The total of 25 + 12.5 + 60 explains the "$97.5B". The underwriters' option on the common is about $3.75B (6M shares).
2. **Item 57, AMD $1B into the Meta offering, is CONFIRMED at secondary level only (an AMD release is reported, primary not reached).** Nvidia separately committed $3B (reported). Meta's FWP still describes the cornerstone interest as indications, and no binding share count was found.
3. **Item 40, SK hynix, is CONFIRMED at the primary (6-K, Oct 28).** Q3 revenue was ₩104.6T (+327.9% YoY, +31.9% QoQ). Operating profit was ₩83.3T (+632.1% YoY, +37.6% QoQ), an 80% margin and a record. Net profit was ₩39.8T, **−57.7% QoQ** because of non-operating losses. The CNBC post omitted that, and it is decision-relevant. The company also announced about ₩100T of shareholder returns for 2026.
4. **Item 37, GOOGL below its 200-day MA by the widest gap in 17 months, is CONFIRMED** on vendor data: Oct 26 close −7.08% versus the 200-day MA, last that deep on 2025-05-12. **It is superseded today: GOOGL is −11.67% intraday on 10/29 (vendor, ~$287), about −15.7% below its 200-day MA**, after Alphabet's Q3 8-K (filed 10/28 20:01Z). That release was not read here. VULCAN/HENRY should look.
5. **Corporate primaries are CONFIRMED at SEC:**
   - Dropbox 8-K (10/28): about 9% RIF (reduction in force) costing $27–33M; CTO Ali Dasdan leaves 11/18; Q3 pre-announced in line or above guidance.
   - GM 8-K (10/27): NYSE→Nasdaq, last NYSE day 11/16, Nasdaq from 11/17.
   - HOOD and Visa releases (10/27) match the posts on figures.
   - Villa Vie layup in Cambodia over fuel is confirmed via trade press (10/27), not the company's own channel. Iran/Hormuz fuel costs are cited.

---

## 9. @zerohedge 2115279522438258743 (2026-10-28 03:08Z), "$200B AI capital call"
- **Full text read:** yes, plus the quoted ZH post and the chart image. The chart's source line says "ZeroHedge; Meta prospectus/pricing; Broadcom/lenders joint release; Reuters (first-lien size per sources); JPMorgan; SpaceX/Apollo; Anthropic S-1". It also says the Anthropic S-1 discloses "~$637bn of named compute commitments". That figure was not verified.
- **Claim:** On Monday Oct 26: Broadcom deal + Anthropic S-1 + Meta "$95B offering (upside $97.5B)" + SpaceX "closing" a $40B lease ≈ $200B. Quoted claim: the first lien is about $43.5B, or 69% of the $63B, "effectively guaranteed by the vendor".
- **Primary:** Meta pricing FWP, SEC, 2026-10-27 10:02Z (acc 0001193125-26-432549). It states Meta "has increased the size of the Common Stock Offering to $25.0 billion, consisting of 40,000,000 shares (46,000,000 if the option is exercised)". Pricing date Oct 26, trade date Oct 27, settlement Oct 29. Final 424B5s were filed 10/28. Also used: Apollo/SpaceX release (10/26) and the BofA/Blackstone/Citi/MS release (10/26, via the prior card).
- **Verdict: CORRECTED-FRAMING.**
  - The $97.5B is $25B common forward (proceeds arrive on settlement through 11/19/2027) + $12.5B mandatory convertible preferred + $60B Class C ATM. The ATM still has no agreement, and the chart itself labels it "from Q1 2027".
  - The $63B is committed financing, not funded. The 10/26 release does not disclose tranche sizes, so the $43.5B first lien / 69% figure rests on Reuters sources, not the release. Broadcom's residual value support "equivalent to the first-lien amount" is support for equipment value, not a guarantee of the loan.
  - SpaceX/Apollo is a binding commitment. It is expected to close before year-end 2026, with lease schedules starting on delivery in H1 2027. No closing announcement was found. "Closing" is FALSE as of now.
  - Of the ~$200B, about $37.5B was priced on Oct 26.
- **Prior cards:**
  - SIG-W-20261026-001: Meta $35B + $60B not established.
  - SIG-W-20261027-029: Broadcom/Anthropic $63B committed.
  - SIG-W-20261026-002: SpaceX binding, not closed.
  - SIG-W-20261026-003: Anthropic S-1 filed, prospectus unread.
- **New since those cards:** the Meta upsize to $25.0B common (total $37.5B launched) and the reported first-lien size of about $43.5B. Anthropic's ~$637B in commitments is unverified; it needs the S-1.
- **Gaps:** I did not re-read the 10/28 final 424B5s in full. The S-1 was not read.
- **Owners:** BROCK/LIQUID (financing); VULCAN INFO.

## 51. @michaeljburry 2115174435242058121 (10/27 20:10Z), "My take on Anthropic's S-1"
- **Full text read:** the post, yes. The Substack ("Short Thoughts: Anthropic's S-1", Cassandra Unchained, Oct 27) is **paywalled**, so only the intro was visible.
- **Claim:** The visible part makes no factual claim. Burry says others' teardowns are good. His focus is "the degree of risk in the system". He mentions a visual showing "circular revenue and other connections between Anthropic and those around it", in the style of his Apollo AMAP visual.
- **Verdict: OPINION**, with the substance not reached. "Circular revenue" is his characterization and is unsupported in the visible text.
- **Gaps:** the body and the visual. **Owner:** VULCAN (Anthropic IPO record), BROCK INFO.

## 56. @unusual_whales 2115145755266793982 (10/27 18:17Z), AI firms scrambling for cash (WaPo)
- **Full text read:** yes. The post claims Meta "up to $95B" with AMD/Nvidia buying in, Anthropic preparing one of the largest IPOs ever, and OpenAI seeking $30B at more than $1.4T.
- **Primary:** the WaPo article was not reached; only an aggregator summary was found.
- **Verdict: CORRECTED-FRAMING.**
  - The Meta "up to $95B" has the same problem as item 9. It is now $97.5B after the upsize, and $60B of it has no agreement.
  - The OpenAI figure is stale. SIG-W-20261023-037 has the round target cut to $1.25T pre-money from $1.4T (FT).
- **Gaps:** the WaPo text. **Owners:** BROCK/LIQUID; VULCAN INFO. Nothing here is new beyond the cards.

## 57. @financialjuice 2115071263429554308 (10/27 13:20Z), "AMD to invest $1b in Meta offering"
- **Full text read:** yes (one line).
- **Primary:** the AMD release of Oct 27 was not reached directly. It is reported by Magica and FourWeekMBA, which say the same release says Helios is running at Meta. Meta's 10/26 release named Nvidia, AMD and Broadcom as "cornerstone investors" with **nonbinding** indications of up to $5.0B. Nvidia has reportedly committed $3B. Broadcom's amount is not reported.
- **Verdict: CONFIRMED (secondary)** for the $1B intent. The share count and execution are not disclosed.
- **Gaps:** an AMD 8-K or release primary. I did not check EDGAR for AMD. **Owners:** BROCK (vendor financing / circularity); VULCAN INFO.

## 16. @zerohedge 2115459864352768371 (10/28 15:05Z), Citadel "Tokenomics 2.0"
- **Full text read:** the post, yes. The ZH article is **ZH Premium, paywalled**, so only the opening was visible. The author is Frank Flight (Citadel Securities macro strategy).
- **Visible quoted Citadel text:**
  - "Consumption weighted token prices have declined approximately 50% over six months."
  - Frontier average token prices fell 62%.
  - "Increased competition from open-weight models **may** exert pressure on margins at the frontier."
  - The "expansion of token volume suggests overall inference demand is accelerating."
- **Primary:** the Citadel Securities site hosts the June 2026 "Tokenomics" note. The "2.0" note itself was not reached.
- **Verdict: CORRECTED-FRAMING.** "Eating alive" and "margins getting destroyed" are ZH's words. The Citadel text is hedged ("may") and pairs the price decline with accelerating volume. No lab names or market-share figure were visible.
- **Owner:** VULCAN.

## 40. @CNBC 2115227644862071012 (10/27 23:42Z), SK hynix Q3
- **Full text read:** yes. The post's figures: revenue +327.9% YoY / +31.9% QoQ; operating profit +632.1% YoY / +37.6% QoQ.
- **Primary:** SK hynix 6-K, SEC, filed 2026-10-28 (acc 0001193125-26-434994), consolidated and preliminary.

| Q3 2026 (₩ millions) | Value | QoQ | YoY |
|---|---|---|---|
| Revenue | 104,615,483 | +31.9% | +327.9% |
| Operating profit | 83,333,818 | +37.6% | +632.1% |
| Pre-tax profit | 50,708,500 | −58.7% | +242.8% |
| Net profit | 39,775,593 | −57.7% | +215.7% |

- **Verdict: CONFIRMED.** Revenue and operating profit are records: the first quarter above ₩100T revenue, with an 80% operating margin.
- **Omitted from the post:** net profit −57.7% QoQ, which secondaries attribute to a ₩22.9T valuation loss on investment assets and a ₩11.6T FX loss. Also omitted: the 2026 shareholder return plan of about ₩100T (6-K acc 0001193125-26-435008). That breaks down as ≥₩30T dividends and ≥₩60T buyback/cancellation, including the ₩40T resolved in August.
- **Secondary consensus:** operating profit ~₩76.7T (CNBC via aggregator).
- **Prior:** no Q3 card found. **Owner:** VULCAN (semis/HBM); HENRY INFO.

## 37. @Barchart 2114924310334939239 (10/27 03:37Z), GOOGL below its 200-day MA by the widest margin in 17 months
- **Full text read:** yes, and the image is a chart.
- **Check (vendor yfinance closes):**
  - 10/26 close $316.80 vs 200-day MA $340.95 = **−7.08%**. The last close at or below that gap was **2025-05-12 (−7.19%)**, about 17.5 months earlier.
  - Then 10/27 −5.96% and 10/28 −4.69%.
  - **10/29 intraday: $286.96, −11.67% on the day, ~−15.7% vs the 200-day MA.** That is the widest gap in the 5-year vendor window.
- **Verdict: CONFIRMED** for 10/26. **Superseded:** Alphabet filed its Q3 8-K 2.02 on 2026-10-28 20:01Z and its 10-Q on 10/29 00:29Z. That release was **not read**, so the cause of today's drop is unverified here.
- **Owners:** HENRY (equities); VULCAN (hyperscaler capex), and Alphabet results need an OPEN read under 7e(d.1).

## 35. @SteveRattner 2115142144252109218 (10/27 18:02Z), data center capacity in red states
- **Full text read:** yes, plus the chart.
- **Source line on the chart:** Cleanview data center tracker (Sept 26, 2026), with 2024 results compiled by T. McGovern.
- **Chart figures (share of capacity):**

| Capacity stage | Trump +5 or more | Within 5 points | Harris +5 or more |
|---|---|---|---|
| Operating, end-2023 | 36% | 8% | 56% |
| Under construction | 60% | 14% | 26% |
| Planned | 66% | 14% | 19% |

  Footnotes: Texas 11.5 GW under construction; Virginia 9.4 GW; excluding Virginia, 92% of capacity under construction is in Trump states.
- **Verdict: CORRECTED-FRAMING (minor).** "Red states" means states Trump won by 5+ points, and the 60% figure is for under-construction capacity. The 92% figure's denominator treatment of the within-5 states is unclear. The Cleanview primary was not reached.
- **Owners:** VULCAN (power/siting). CORAL INFO is not applicable; Florida is not shown.

## 54. @KobeissiLetter 2115165670136496363 (10/27 19:36Z), S&P 500 ex-AI outperforming by +6.4pp in October
- **Full text read:** yes, plus the chart (source line: "Bloomberg").
- **Claims:** +6.4pp month-to-date, a record (previous record +3.6 in July). September −5.1 was the 2nd-worst. +7.4pp over 3 weeks is a record.
- **Verdict: INDETERMINATE.** The index identifier ("S&P 500 ex AI") and its constituents are not named, and the month is partial (through 10/27). It is directionally consistent with SIG-W-20261023-023 (RSP vs SPX on 10/22).
- **Gaps:** the Bloomberg series ticker; the month is not complete. **Owner:** HENRY.

## 48. @coinbureau 2115175409503629485 (10/27 20:14Z), HOOD Q3
- **Full text read:** yes.
- **Primary:** HOOD 8-K Ex-99.1, 2026-10-27 20:06Z (acc 0001783879-26-000164). An 8-K/A followed on 10/28; its purpose was not extracted.
- **Release figures:**
  - Revenue $1.42B (+12% YoY), a record.
  - Diluted EPS $0.51 (−16%); adjusted EPS $0.60 (−3%, a new non-GAAP measure).
  - Crypto revenue $120M (−55%); event contracts (prediction markets) $173M (more than 6x); options $399M (+31%).
  - Net interest revenue $415M (−9%); net deposits $15.7B.
  - October-to-date net deposits above $13B, including **$6B from the Dell family's contribution to Trump Accounts**.
  - Net income included a $67M unrealized loss on RVI.
- **Verdict: CONFIRMED** on figures. The $0.56 consensus is unverified. The post-market move is unverified. Vendor closes: 10/27 $94.56, 10/28 $91.43 (−3.3%).
- **Owner:** CARL (consumer/brokerage); HENRY INFO.

## 50. @coinbureau 2115182749057179973 (10/27 20:44Z), Visa beat, dividend +16%, slid ~2% after hours
- **Full text read:** yes.
- **Primary:** Visa 8-K Ex-99.1, 2026-10-27 (acc 0001403161-26-000126). Fiscal Q4 FY26 (Sept quarter):
  - Net revenue $12.1B (+13%).
  - GAAP EPS $3.19 (+22%); non-GAAP EPS $3.48 (+17%).
  - Payments volume +9%; cross-border +14%; processed transactions +10%.
  - Quarterly dividend raised 16% to $0.780, payable 12/1. FY revenue $45.9B (+15%).
- **Verdict: CONFIRMED** for the release figures and the dividend. The "beat" and the "$14B wiped" are unverified, though roughly consistent with a 2% move on a ~$780B market cap. The after-hours move did not hold: vendor closes were 10/27 $401.86 and 10/28 $400.60 (−0.3%), and 10/29 is $411.28 (+2.7%).
- **Prior:** SIG-W-20261023-020 (Visa layoffs, unverified). **Owner:** CARL.

## 28. @Polymarket 2115434155651813574 (10/28 13:23Z), Dropbox cuts 9%, CTO departs
- **Full text read:** yes.
- **Primary:** Dropbox 8-K, 2026-10-28 13:05Z (acc 0001467623-26-000052), Items 2.02/2.05/5.02.
  - About 9% global RIF, with cash costs of $27–33M.
  - CTO Ali Dasdan steps down effective 11/18/2026 (severance, plus a $515K pro rata bonus and about $1.3M lump sum).
  - Q3 expected in line with or above guidance; report due 11/5.
- **Verdict: CONFIRMED.** The headcount number is not stated. No BOARD prior.
- **Owner:** HENRY INFO (labor: LABOR desk if routed).

## 60. @Polymarket 2115102191895887939 (10/27 15:23Z), GM to leave NYSE after 115 years
- **Full text read:** yes.
- **Primary:** GM 8-K, 2026-10-27 10:30Z (acc 0001193125-26-432602), Item 3.01. On 10/26 the board authorized a voluntary transfer to the **Nasdaq Global Select Market**, keeping the ticker GM. Last NYSE trading is at the close on **11/16/2026**; Nasdaq trading begins **11/17/2026**.
- **Verdict: CORRECTED-FRAMING.** It is a listing transfer, not a delisting or distress event. The "115 years" was not verified in the 8-K text.
- **Owner:** OTTO, INFO only.

## 31 + 63. @Polymarket 2115293981873758301 (10/28 04:06Z) and @shipmonk 2114991192161276287 (10/27 08:02Z), Villa Vie Odyssey halted in Cambodia
- **Full text read:** yes, both.
- **Primary:** the company statement was quoted by Maritime Executive (2026-10-27). It cites "the extraordinary increase in fuel costs" and says "Passing the full increase on to residents is not a realistic solution". The company will "work toward restructuring and recapitalization over the next 60 days".
  - Residents were noticed the morning of 10/27 (one outlet says 10/26) to disembark by 2 p.m. local time; the port is Sihanoukville per CruiseHive.
  - Fuel cost: historically about $1,800/month, now about $6,000–8,000 per cabin in Asia. TMZ attributes this to the Iran war and Hormuz.
- **Verdict: CONFIRMED** on the event. **CORRECTED** on details: Polymarket's "200 passengers" conflicts with about 300 residents (CruiseFever), and the ship is in layup with recapitalization pending, not definitively ended.
- **Gaps:** the company's own release or site was not reached. **Owners:** CRUISE (operator stress); BRENT INFO (marine fuel price pass-through).

## 64. @unusual_whales 2115045092092411980 (10/27 11:37Z), airlines brace for years of pain (FT)
- **Full text read:** yes.
- **Primary:** the FT article was not reached; an expert.ru summary of it was found.
  - High jet fuel prices; carriers fear fare increases plus inflation will shrink demand.
  - An unnamed executive says inflation will leave people poorer.
  - TAP CEO Luís Rodrigues expects 3–5 difficult years.
  - Fleet plans are under review.
- **Verdict: CONFIRMED (secondary).** The quote comes from an anonymous executive.
- **Owners:** BRENT (jet fuel); HENRY INFO. Prior: SIG-W-20261021-014 (Southwest fuel).

## 47. @Barchart 2114929043841991045 (10/27 03:55Z), China on track for 12 consecutive red weeks, longest ever
- **Full text read:** yes, plus the chart. **The index is the CSI 300 ($CSHZ, 4,103.54 on 10/26)**, not the Shanghai Composite.
- **Check:** a Reuters syndication of 10/23 says the CSI 300 was headed for its "longest-ever weekly losing run" but gives no count. Vendor CSI 300 weekly history is unavailable.
  - The ASHR proxy (USD, so FX-contaminated) shows one up week, 9/18 (+$0.13). The CSI 300's own sequence is unconfirmed.
  - The Shanghai Composite has fallen about 6 weeks in a row (9/21→10/26 week).
  - "On track" means the 10/30 week is incomplete.
- **Verdict: INDETERMINATE**, plausible on Reuters' "longest-ever". **Owner:** ZHAO. Prior: SIG-W-20261022-002 (CSI 300 bear market).

## 43. @KobeissiLetter 2115117452644221274 (10/27 16:24Z), Brazil −19.8% "rarest event"
- **Full text read:** yes, plus the quote.
- **Check:** EWZ vendor closes were 10/23 $42.59 and 10/26 $34.15, which is **−19.8%**. This confirms a one-day move on the ETF basis; the post's "Monday" is correct.
- **What's new:** only the sigma framing (8.4 sd; "1 in 58 quadrillion" under a normal distribution). That is analytical framing, and fat tails make the normal-distribution probability meaningless.
- **Since then:** EWZ is $33.08 on 10/29 (vendor), about −10.7% vs its 200-day MA. The quoted "−30%" and "$200B" figures came from 10/26 intraday and were not re-verified.
- **Prior:** SIG-W-20261026-004/-008/-012. **Owner:** LIQUID, INFO only.

## 32. @stockdatamarket 2115114170110931095 (10/27 16:11Z), SPY put premiums rising as the market rises
- **Full text read:** yes, plus the chart.
- **Chart:** an Unusual Whales SPY net-premium screenshot, 10/27 about 12:10 ET. SPY 770.26, VIX ~17.6. Net put premium about +5.4M, net call premium about +25.6M. Calls dominate in the chart.
- **Verdict: OPINION**, single-session intraday, low evidentiary weight. **Owner:** HENRY, INFO only.

## 30. @DonMiami3 2115237169833144464 (10/28 00:20Z), "Another one...? Can it be?"
- **Full text read:** yes, plus the image.
- **Subject:** a **US crude oil spot (WTI, CFD) 4-hour chart** by PolarBearMarketResearch (TradingView, 10/27 17:19 PT), last 101.80. A cup drawn from a ~$107 mid-Sept high, a ~$89.5 low on Oct 6, then a recovery to ~$105 around 10/23, with a small bull-flag "handle". It implies another leg higher.
- **Verdict: OPINION** (technical-analysis pattern). There is no event claim.
- **Owner:** BRENT, INFO only, or no action.

## Unreached / gaps
- WaPo (item 56) and FT (item 64) originals.
- The Burry Substack body and visual (paywall).
- The ZH Premium body and the Citadel "Tokenomics 2.0" note (only the June "Tokenomics" note was located).
- AMD's own release or 8-K.
- The Cleanview tracker.
- Bloomberg's "S&P 500 ex AI" series ID.
- CSI 300 weekly closes.
- The Villa Vie company channel.
- Alphabet's Q3 8-K body (10/28), which is relevant to today's −11.7% move.
- The Anthropic S-1 (~$637B commitments figure).
- HOOD's 8-K/A purpose.

Unreached is not an all-clear.

## Sources
- SEC EDGAR:
  - Meta FWP 0001193125-26-432549
  - Dropbox 8-K 0001467623-26-000052
  - GM 8-K 0001193125-26-432602
  - HOOD 8-K Ex-99.1 0001783879-26-000164
  - Visa 8-K Ex-99.1 0001403161-26-000126
  - SK hynix 6-Ks 0001193125-26-434994 and -435008
  - Alphabet 8-K 0001652044-26-000080 (not read)
- SpaceX/Apollo: https://www.apollo.com/insights-news/pressreleases/2026/10/spacex-secures--40-billion-in-the-largest-gpu-financing-ever
- Villa Vie: https://maritime-executive.com/article/passengers-told-to-disembark-as-villa-vie-residences-suspends-operations
- Burry: https://michaeljburry.substack.com/p/short-thoughts-anthropics-s-1
- ZH Citadel piece: https://www.zerohedge.com/ai/ais-low-cost-carriers-are-eating-frontier-labs-alive-citadel-securities-says-tokenomics-20-here
- Citadel "Tokenomics" (June): https://citadelsecurities.com/news-and-insights/global-macro-strategy/tokenomics
- AMD $1B (secondary): https://magica.com/news/amd-meta-ai-equity-investment-nvidia
- FT airlines summary: https://expert.ru/en/news/ft-aviakompanii-zhdut-gody-trudnostey-iz-za-vysokikh-tsen-na-toplivo
