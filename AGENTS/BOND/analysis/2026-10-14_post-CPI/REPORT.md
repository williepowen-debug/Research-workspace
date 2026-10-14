# October14 post-CPI rates and Treasury functioning

**BOND · written October14, 2026 · intraday evidence cutoff 13:59 EDT; Beige Book added after14:00.** Authorization: Will's October14 own-terminal assignment plus existing desk obligations. No trade, new threshold, source purchase or external send. Existing WQ-400 definition encoded as ruled, prospectively. Raw captures and arithmetic: `raw/manifest.json`, `raw/derived.json`; runtime/ownership: `BOOT.md`.

## Judgment and decision implications

**CPI produced an initial yield jump, but it was not a sustained long-end selloff at this cutoff. A firmer near-term Fed path coexists with lower quoted real yields and slightly wider inflation compensation by about14:00. Treasury financing remains expensive; the available evidence does not establish funding dysfunction.** The afternoon pair is a qualified vendor benchmark comparison, not an official same-date CMT decomposition or a causal account of the morning spike. The official October14 split and October14 repo transactions remain pending publication.

The surviving duration-short holding is **TBT5**, not the older TBT10/TLT82P mirror. FORGE's October14 broker receipt establishes the TLT October16 82P sale on October12 and TBT10→5; exact fill/capture times remain UNKNOWN. WQ-357's October14 decision clock applies to the surviving TBT holding; closing the option does not itself resolve that decision. BOND preserves the prior operational exit recommendation, its MET grade and NO-ADD. TERRY owns construction, Will orders. Today's intraday retracement weakens the claim that hot CPI guarantees continued bond losses; it does not establish a durable rebound.

## 1. Inflation evidence: current release versus expectations

| Evidence | Dated observation | Interpretation and limit |
|---|---|---|
| BLS September CPI, released October14 08:30ET | Headline +0.6% m/m SA, +3.7% y/y NSA; core +0.3% m/m, +2.6% y/y; gasoline +9.1% m/m explains over half the headline increase | Inflation pressure persists. Realized prices do not measure bond-market expectations. Reused WALTER's saved BLS release, not a second independent witness. Direct BOND BLS/DOL retrieval403. |
| FRED T5YIFR | 2.33% October13;17bp below existing2.50 line | No unanchoring at this dated cell. It cannot clear October14. |
| Treasury matched daily par nominal minus real | October13 10Y2.33%,30Y2.28% | Inflation compensation, including inflation-risk/liquidity effects; not pure expected inflation. |
| CNBC benchmark nominal/TIPS subtraction | October14 13:58–13:59EDT10Y:2.359%, vs vendor prior2.344%;+1.5bp | Qualified widening alongside lower nominal yields. Instruments mature Aug2036/Jul2036, quotes differ by one minute; not the Treasury fitted constant-maturity pair. No gate graded. |

Primary CPI URL: https://www.bls.gov/news.release/archives/cpi_10142026.htm ; reusable bytes: `AGENTS/WALTER/research/2026-10-14_morning-news/cpi.txt` (copied to raw). Expectations series: https://fred.stlouisfed.org/series/T5YIFR and https://fred.stlouisfed.org/series/T10YIE .

## 2. Three windows that must remain separate

| Window and basis | Nominal10Y | Real10Y | Inflation compensation10Y | Supported conclusion |
|---|---:|---:|---:|---|
| October14 08:29→08:31EDT, Yahoo/CBOE one-minute index |5.190→5.263%,+7.3bp | UNKNOWN | UNKNOWN | Immediate nominal response after08:30 CPI. No synchronized pre/post TIPS observation; morning attribution withheld. |
| October14 vendor previous close→13:58/13:59EDT, CNBC |5.217→5.211%,−0.6bp |2.873→2.852%,−2.1bp |2.344→2.359%,+1.5bp | Afternoon nominal change = real decline plus compensation rise, approximately. The morning jump retraced. |
| October9→13, Treasury fitted daily curves |5.24→5.21%,−3bp |2.91→2.88%,−3bp |2.33→2.33%,0bp | Pre-CPI rally entirely real-led on these rounded daily cells. |
| October7→13, same official basis |−7bp |−4bp |−3bp | Long-end rebound evidence:30Y nominal−11bp, real−8bp, compensation−3bp. |
| September21→October13, same official basis |+25bp |+26bp |−1bp | The broader high-rate episode remains real-led despite recent relief.30Y nominal+27bp, real+26bp, compensation+1bp. |

The Yahoo one-minute10Y series reaches5.325% at08:58 (maximum of returned non-null minute closes). CNBC reports a different statistic: day-high5.329%; no high timestamp. Do not subtract independently timed nominal/TIPS highs. CNBC13:58–13:59 quotes:2Y4.827% (+3.4bp),5Y5.019% (+1.2),10Y5.211% (−0.6),30Y5.539% (−2.4), each versus its own vendor previous close. This is afternoon curve flattening:2s10s−4.0bp;2s30s−5.8bp. Yahoo13:44:24 index10Y5.206/30Y5.537 agrees directionally; different quote times/bases explain small gaps. No official October14 close inferred.

Source URLs and captures: Treasury nominal/real CSV URLs in `raw/manifest.json`; CNBC https://quote.cnbc.com/quote-html-webservice/quote.htm?symbols=US2Y%7CUS5Y%7CUS10Y%7CUS30Y%7CUS10YTIP&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json ; Yahoo https://query1.finance.yahoo.com/v8/finance/chart/%5ETNX?range=1d&interval=1m . Vendor payloads saved in raw. `raw/derived.json` uses Decimal for daily changes.

## 3. Policy path and term premium: related, not additive decompositions

CBOT fed-funds futures via Yahoo, evolving October14 daily bars captured13:58EDT, NOT CME settlements: November implied3.970% versus3.935% October13 (+3.5bp); December4.125 versus4.085 (+4.0bp); January2027 4.200 versus4.160 (+4.0bp). EFFR anchor3.88% October13. November has no FOMC meeting: (3.970−3.88)/0.25 ≈ **36% hold/+25 October28 proxy**, versus22% on the preceding vendor bar; assumptions are one binary step, unchanged EFFR basis and no extra November meeting. This is a risk-neutral/futures proxy, not a certified FedWatch probability. HENRY owns the policy-path series; BOND consumes the established pull. Independent dated FedWatch/OIS remains unavailable. Do not add this+3.5/+4bp to the real-yield/compensation split; expected policy contributes to the real leg too.

NYFed ACM Daily, retrieved13:57EDT, latest October13:10Y term premium0.851455%. October9→13 fitted nominal yield−3.6476bp = term premium−5.0842bp + risk-neutral component+1.4366bp. This model supports a pre-CPI duration-risk-premium retreat despite firmer expected short rates. **Real yield is not term premium**: it also includes expected real short rates and other premia. ACM has no October14 observation yet; the October14 morning move cannot be called term-premium-led from this file. Kim-Wright latest October9 TP1.0729%; different model/vintage, not averaged.

Due BND-30 companion serviced: Kim-Wright September28→29 fitted yield+1.87bp, TP+1.12bp, share0.59893. ACM's first-published BND-30 verdict remains TRUE/TP-DOMINANT (+2.28/+5.39bp); KW is milder and does not reproduce ACM's ≥2bp premise. Latest-revised KW companion does not re-grade the registered first-publication ACM letter. Sources: https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls ; https://fred.stlouisfed.org/series/THREEFYTP10 ; https://fred.stlouisfed.org/series/THREEFY10 .

Hammack October12 reaction function remains conditional, not a fixed October hike or committee decision (WALTER-044/MIDAS return reused). October14 Beige Book adds supply-cost pressure and generally subdued spending/employment: four Districts report faster price increases, and energy costs recur across reports; consumer resistance squeezes margins. Contact information collected on/beforeOctober5, not post-CPI; qualitative, not a policy vote. This supports the inflation/growth tension rather than an unconditional hiking forecast. Source: https://www.federalreserve.gov/monetarypolicy/beigebook202610-summary.htm .

## 4. Treasury functioning and funding: what the evidence actually tests

| Layer | Evidence frontier | Finding | What is NOT established |
|---|---|---|---|
| Auction clearing | Completed BOND October7/8 returns reused |10Y indirect80.34%;30Y72.32%,competitive-accepted denominator;30Y stop5.618%; both clean on frozen letters; downgrade counter2 | No auction tail; TreasuryDirect lacks deadline WI. No new nominal coupon since10/8. Indirect bid is not foreign-official holdings. |
| Dealer stock | NYFed FR2004 re-pulled October14; still as-ofSeptember30 |3–6Y$52.885B,−$7.194B w/w; long-end$133.062B,−$7.483B | Net inventory does not prove warehousing or today's capacity. No early October7 grade; next publicationOctober15. WQ291 closed window remains MET. |
| Buyback composition | Four authorized F2 reads reused throughOctober8 |All OFF-THE-RUN under corrected original-issue-date rank; latest recent_share0.00% | Full cap use does not prove yield targeting; next opOctober15, no premature result. |
| Secured/unsecured overnight funding | NYFed October13 transactions, publishedOctober14 |SOFR3.89%,EFFR/TGCR/BGCR3.88%;IORB3.90%;SOFR−IORB−1bp. SOFR volume$3,000B,25th/75th3.88/3.94%,99th3.98% | These transactions precede CPI. They do not clear October14 margin calls, individual funds, haircuts, fails or collateral restrictions. LIQUID owns the funding verdict. |
| Credit price | ICE/FRED October13 latest vintage |HY316/CCC1267/IG83/BBB103/BB191/B317bp;HY+5/CCC+14/IG0bp versusOctober12. CCC−BB1076bp;HY34bp below350 | Daily changes remain tail-dominated. LIQUID14:05ownerreturn grades cumulative15-observation broadening inIG/BBB/BB under its frozen rule;not actual stronger-borrowerdefaults or a measured aggregate issuance freeze. No comprehensive pulled-deal census or trueCDX basis. |
| Investor flow | WALTER's dated Lipper/Reuters week endingOctober7 return |Global cash+$153.81B AND bond+$26.03B;government-bond+$4.65B | Subscription flow is not bank-deposit flight or issuer-level absorption. Same provenance chain, not independent corroboration. |
| Pension derivatives | WALTEROctober13 Chile lead reused |Reported derivative losses/unwind at AFP managers; full article/regulator data unretrieved | No identified Treasury cash-sale quantity, margin-payment amount, counterparty loss or system cascade. Mark-to-market loss is not cash funding demand. |

Latest NYFed primary capture: https://markets.newyorkfed.org/api/rates/all/latest.json . Dealer pull uses existing `fr2004_fetch.py`, runtime-resolved series break, saved raw; no hardcoded partition. Auction/F2 arithmetic remains in completed `analysis/2026-10-08_ninth-wake/REPORT.md`, KB425–428 and `registry/f2_reads.tsv`; not repeated. Broad Treasury depth/bid-ask, cash/futures basis, settlement fails and current fund-level collateral demands were not obtained. Therefore **market-wide dysfunction is not established**, not certified absent.

A borrower can refinance only at a painful price while cash markets, auctions and repo continue operating. Funding dysfunction requires actual missing cash/credit/collateral access, margin-driven sales or impaired intermediation. Higher real yields increase refinancing costs and bond valuation losses; their level alone does not establish those mechanisms. This preserves PROME's compound-stress finding and REGINALD/WAL's matched borrower/lender funding work; no duplicate bank screen. Latest LIQUID14:05return(`research/2026-10-14_credit-funding-refresh/REPORT.md`) adds cumulative stronger-credit spread broadening under its15-observation frozen rule; tail dominance is not exclusivity. Its funding verdict remains absent throughOctober13.

## 5. Due authorized maintenance and strongest counterevidence

- **WQ-400 encoded exactly:** VX-BND-19 disorderly Bund leg = existing level>3.25 AND five-session rise>17.0bp STRICT, Bundesbank Svensson-fitted10.0Y daily series `BBSIS.D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A`; prospectiveOctober9, no historical re-grade. LatestOctober14 3.51%, five-sessionOctober7→14−4bp; all four prospective published evaluations NOT MET (October9+4,12+2,13−3,14−4bp). Existing OAT/basis alternatives unchanged and not newly graded. Score3 unchanged. Ruling: incoming PROME WQ400 packet; base rate KB432.
- **VX20 review serviced:** Ministry National Budget2027 §4.4.3 still describes NBIM's70→50 proposal as input to further work, with expert reportJanuary25,2027 and Ministry assessment planned spring2027. No adoption or qualifying second holder located in this bounded primary/search review; absence not proven. Score2/FL14 LATENT unchanged. Another Norwegian fund's Nordic weighting change is not a second>$250B UST-cut proposal. Primary: https://www.regjeringen.no/no/dokumenter/meld.-st.-1-20262027/id3175768/?ch=4 ; direct request403, browser tool read successful; NBIM primary bytes saved. Existing expert date preserved; next bounded checkpointOctober28 or issuer news.
- **REG-T-06 WQ414 consumed:** existing>$700B×3 quarterly condition now yields REVIEW; top-four growth contribution and matched qualified SEC-filer median required before escalation, with missing/incomparable/nonpositive-growth handling. BOND VX18/gates unchanged. Use REGINALD's committed result; no independent bank nowcast or new cutoff.
- Strongest evidence against continuing duration losses: the morning CPI selloff retraced; officialOctober7→13 nominal30Y−11bp/real30Y−8bp; ACM pre-CPI term premium fell while its risk-neutral component rose; clean10Y/30Y auction demand; dealer3–6Y build unwound; cash and bond funds both attracted money. Offsetting evidence: September21→October13 real10Y+26bp; futures price a firmer path; CPI/Beige Book cost pressure persists; CCC spreads deteriorate. Neither set justifies a guaranteed directional forecast or a new trade.

## 6. Next dated tests, dependencies and delivery

| Date | Existing test / action | Decision implication |
|---|---|---|
| October14 after Treasury daily publication; next BOND touchOctober15 | Replace vendor pair with matched official nominal/realOctober14 versusOctober13; separately review new ACM row when actually published | Does the intraday real relief/compensation rise survive the close? Official close captures all day's news, not solely CPI. |
| October15 08:30 / weekly releases / ~14:15 | PPI macro context; FR2004as-ofOctober7;PMMS;F2 10–20Y op | Price persistence versus actual dealer-stock/funding/buyback evidence; route newF2 toRED under existing carrier. |
| October21 /22 |20Y-R912810UX4 /5YTIPS91282CRR4; freeze appropriate bars at announcements, preserve TIPS exclusion |20Y could take clean-nominal counter2→3 only on actual grade. FOMC curve prediction registration dueOctober21, not fabricated today. |
| October28 /November4 /November9 /January25,2027 |FOMC;QRA F1/F3;FHLBQ3;GPFG expert report | Existing policy/supply/backstop/mandate resolvers. No new threshold. |

Unresolved: morning synchronized TIPS/event-window split; October14 official close/ACM/repo publication; independent dated OIS/FedWatch; trueCDX, paidMBSOAS, failed-deal census, current Treasury microstructure/fails/haircuts and named pension cash demands; broker exact times/working orders. Primary Beige Book recovered; CPI reused from WALTER's primary capture after direct403. Parent/native messaging tools do not address separate owner windows; tested existing bridge endpoint disconnected at initialization, so live notification and recipient consumption remain unverified. Durable PROME delivery is required and supplied; no replacement launch or raw-socket workaround. Pull deferred because other desks have dirty work; exact-path Git persistence follows root rules.
