# WQ-295 R3 WATCH_FOR live test — GROUP B (FLG · BOND · HENRY · HOMER · CRUISE)

**Run:** 2026-10-01 ~10:45–11:30 ET by a WALTER test subagent. Read-only to `~/Research-Intake`, which is at local HEAD `cca0ef6` (2026-09-30 17:59 ET). This HEAD carries the FLG, `treasury-moves` and `diesel-export-policy` entries. Nothing committed, moved or edited except this file.

**Method (R3):** `AGENTS/WALTER/tools/watch_for_harness.py` runs the lane's real `match_watch_for()` over:
- **Lane history:** **10,405 unique headlines, 71 lane days, 2026-06-29 → 2026-09-30.**
- **A live Google-News RSS sample:** on-topic subject queries, windows 21–90 days as stated per desk.
- **Synthetic positive controls:** plausible real headlines, used to test recall.

The reader (this agent) classified every hit. **TRUE** means the headline reports the event the phrase is keyed to. **FALSE** covers everything else, including previews, precursors, other markets and other entities. Verdict: ⛔ REJECTED at >0 FALSE, ✅ PASS otherwise. ⚠️ marks recall notes. A 0-hit result is called **UNINFORMATIVE** wherever the lane fetches no headlines on that subject.

**Matcher facts relied on, verified in the source:**
- Words of 3 characters or fewer are dropped. Words longer than that must appear as case-insensitive *substrings*.
- Tokens matching `[A-Z][A-Z0-9-]{1,4}` are required entity tokens. Each must match case-sensitively on a word boundary, or match an `ENTITY_INDEX` alias when the token is itself a key.
- **None of `TRO`, `KB`, `NVR`, `LGI`, `CCL`, `RCL`, `NCLH` is an `ENTITY_INDEX` key.** Each therefore binds only to its literal uppercase form in the title. `CCL`/`RCL`/`NCLH` exist only as *aliases* under the `Carnival Corp`/`Royal Caribbean`/`Norwegian Cruise` keys, so the aliases do not help a phrase.
- Google-News titles end in ` - <Outlet>`, and outlet words count toward a match.

**Lane coverage per subject (substring counts, 10,405 headlines):**

| Subject | Lane headlines |
|---|---|
| Lennar / KB Home / Horton / Toll Brothers / PulteGroup | 0 / 0 / 0 / 0 / 0 |
| American Airlines | 0 |
| Southwest Airlines | 1 |
| Freedom Mortgage / loanDepot | 0 / 0 |
| term premium / basis trade / swap spread / Treasury auction | 0 / 0 / 0 / 0 (`treasury-moves` query has run only since 9/28) |
| Jazan | 4 |
| Jizan | 1 |
| Carnival | 31 |
| Royal Caribbean | 60 |
| Norwegian Cruise | 9 |
| rent freeze | 18 |

⇒ Lane 0-hit results are **uninformative** for builders, airlines, servicers and Treasury topics.

---

## 1. FLG — `WATCH_FOR["FLG"]` (8 keep + 3 add)

**Live queries:**
- **30-day run:** `rent freeze court`, `rent freeze lawsuit`, `Rent Guidelines Board`, `rent freeze judge` → 159 headlines.
- **90-day run:** `rent freeze`, `Mamdani rent freeze`, `rent freeze appeal`, `rent freeze landlords`, `rent freeze injunction`, `rent freeze struck down`, `rent freeze overturned`, `rent stabilized lawsuit` → 325 headlines.
- **Replacement and upheld runs:** 213 and 257 headlines.

The freeze took force 10/01. No injunction, TRO or merits ruling has occurred, so recall on the ruling phrases rests on synthetics.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `rent freeze injunction` | 0 | 0 / 325 | ✅ PASS | ⚠️ A precursor ("landlords seek injunction against rent freeze") would match. None was observed in 90 days. |
| 2 | `TRO rent freeze` | 0 | 0 | ✅ PASS | **`TRO` binding CHECKED: FLG is right.** `TRO` is a case-sensitive entity token. Synthetic "Court issues TRO halting NYC rent freeze" and "Judge grants TRO in rent freeze case" both match. ⚠️ Headlines that spell out "temporary restraining order" are missed. Tested add `restraining order rent freeze`: 0/0, synthetic ✓, but it carries the same precursor risk as #1. |
| 3 | `blocks rent freeze` | 0 | 0 | ✅ PASS | Synthetic "Judge blocks NYC rent freeze…" ✓. ⚠️ "blocked" does not contain "blocks", so it misses. |
| 4 | `halts rent freeze` | 0 | 0 | ✅ PASS | — |
| 5 | `rent freeze annulled` | 0 | 0 | ✅ PASS | ⚠️ "annuls" is missed. Tested add `annuls rent freeze`: 0/0, synthetic ✓. |
| 6 | `Rent Guidelines Board lawsuit` | 3 | 2 | ✅ PASS | All 5 hits are TRUE as case news on the named suit: amNY 9/24 "Judge demands to see communications…", Queens Chronicle 9/24 and 9/29, and ny1 "Group of landlords files lawsuit…". ⚠️ It fires on case *progress*, not only rulings. |
| 7 | `Kenilworth Holdings` | 0 | 0 | ✅ PASS | Headlines do not name the petitioner (0 in 325), so recall is weak. |
| 8 | `Lantry rent freeze` | 0 | 0 | ✅ PASS | Same as #7. |
| 9 | `rent freeze overturned` (ADD) | 0 | 0 | ✅ PASS | ⚠️ "Appeals court overturns … rent freeze" is missed ("overturns" does not contain "overturned"). It matched only via #11. Tested add `overturns rent freeze`: 0/0, synthetic ✓. ⛔ **Do NOT use `overturn rent freeze`: 5 FALSE live.** Examples: "New York Landlords Are Suing to Overturn a Rent Freeze on 1 Million Stabilized Apartments - yahoo.com"; "NYC Landlords Sue to Overturn Rent Freeze, Claim Mamdani Influenced Board - Law Commentary"; "Landlords Sue to Overturn New York City Rent Freeze - Law.com". |
| 10 | `rent freeze struck down` (ADD) | 0 | 0 | ✅ PASS | ⚠️ **Synthetic "Judge strikes down NYC rent freeze" → NO MATCH** ("strikes" does not contain "struck"). Add `strikes down rent freeze`: 0/0, synthetic ✓. |
| 11 | `rent freeze appeal` (ADD) | 0 | 0 | ✅ PASS | Synthetics "Landlords appeal ruling upholding rent freeze" and "Appeals court overturns Mamdani rent freeze" both match. |

**Further recall gaps:**
- **The city-wins side of T-12 is unwatched.** "Rent freeze upheld by state judge" and "Judge rules against landlords in rent freeze lawsuit" match nothing. Tested `upholds rent freeze` and `rent freeze upheld`: 0/0, synthetics ✓.
- ⛔ **`dismisses rent freeze` REJECTED: 2 FALSE.** Both are about a *different city's* case: "Judge Dismisses Rent Freeze Lawsuit Against City of Santa Barbara - Noozhawk" and "Federal Judge Dismisses Lawsuit Challenging Santa Barbara Rent Freeze… - edhat".
- ⚠️ **None of the 11 phrases is NYC-bound, and rent-freeze litigation is live elsewhere (Santa Barbara).** No FLG phrase hit it in the sample, but #1/#3/#4/#9/#10 would fire on another city's ruling.

**Tally: 11 pass, 0 rejected.** Suggested adds, all PASS: `strikes down rent freeze`, `overturns rent freeze`, `annuls rent freeze`, `upholds rent freeze`, `rent freeze upheld`. Rejected as replacements: `overturn rent freeze`, `dismisses rent freeze`.

---

## 2. BOND — five WATCH_FOR candidates (`term premium` · `real yields` · `basis trade` · `swap spreads` · `Treasury auction`)

These came from BOND `SCRATCH.md` item 7e and WALTER `LAST_COMPLETION` 0c. The 9/28 pulled-deal packet itself carries no phrases.

**Classification basis:** BOND has keyed none of the five to a registered trigger. They are rates-attribution *topic* terms. TRUE therefore means the headline reports a development in that US Treasury-market quantity. FALSE means another market or subject, or no development (a preview, op-ed or product marketing). ⚠️ **R3 asks the owner to key each phrase to a registered trigger. BOND should do so; the topic basis used here is this reader's.**

**Live queries:**
- **21-day run:** `Treasury yields`, `term premium`, `real yields`, `basis trade`, `swap spreads`, `Treasury auction` → 428 headlines.
- **30-day runs:** the same six plus `bond auction`, `TIPS yields`, `Treasury basis` → 569 headlines. Collision run with `swap spread`, `credit default swap spreads`, `CDS spreads widen`, `swap spreads Treasury`, `TIPS yield`, `basis trade hedge funds`, `tips` → 378 headlines.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `term premium` | 0 | 14 (≥11 FALSE) | ⛔ REJECTED | FALSE: "Proposed rate hikes for long-term care plans would double premiums for thousands of seniors - Maryland Matters"; "JPMorgan upgrades CoreWeave to Overweight on premium short-term compute pricing - Yahoo Finance"; "Aviva India launches term plan with 105% premium return - Insurance Asia"; "Costco: A Premium Worth Paying For Long-Term Compounding - Seeking Alpha". Replacements PASS: `Treasury term premium` (0/0, synthetic ✓, but ⚠️ misses "Term premium on 10-year notes climbs"); `term premium yields` (2 TRUE: P&I "The term premium is driving higher yields…", Chosunbiz); `term premium bond` (1 TRUE). |
| 2 | `real yields` | 6 | 27 | ⛔ REJECTED | FALSE (lane): "Fewer Fed Meetings And Higher Yields Put Commercial Real Estate At Risk - Globest" (8/03) and "As 10-Year Treasury Yields Rise, Commercial Real Estate Reels - Commercial Observer" (9/28). FALSE (live): "Analysis: Higher Treasury yields deliver a reality check on a hot, inflation-prone economy - CNBC"; "Market Minute: Rising 5-year yields and the increasing cost of doing business - The Real Economy Blog"; "Never mind the bond yields, Bank of America shows where the real threat to the economy lies - MarketWatch". Replacement PASS: `TIPS yield` (7 TRUE, incl. 10-year TIPS reopening results; synthetic "10-year TIPS yield hits…" ✓). `TIPS yields` (plural) misses the singular. |
| 3 | `basis trade` | 1 | 14 | ⛔ REJECTED | FALSE (lane 7/07): "The SOFR–federal funds rate basis saw strong buying interest following record-breaking trades. - 富途牛牛". FALSE (live): "ENA rallies 16% as Ethena partners with Binance to extend USDe basis trade into equity perpetuals - FXStreet"; "Dishman Carbogen Allots ₹15 Crore NCDs on Private Placement Basis - scanx.trade". Replacements: `Treasury basis trade` ⛔ REJECTED, 2 FALSE ("How to fix the brittleness caused by Treasury basis trades - Financial Times" is an op-ed with no development; "Beyond the Basis Trade: Spreading Cash and Futures Using Treasury Link - CME Group" is product marketing). `hedge funds basis trade` ✅ PASS, 8 TRUE (Reuters "Hedge funds sour on basis trade as Treasury selloff continues", Bloomberg "Hedge Funds Pull Back From the Basis Trade…", etc.; BeInCrypto "Hedge Funds Own 7% of Treasurys…" counted TRUE as a positioning fact, borderline). |
| 4 | `swap spreads` | 0 | 0 / 428, 0 / 569 | ✅ PASS | Recall **UNPROVEN**: a dedicated `swap spreads` query returned no title carrying the phrase. Synthetic ✓. ⛔ Singular `swap spread` REJECTED: "Heating Oil vs. Brent Crack Spread Swap Futures Jul '28 Futures Price History - Barchart.com". `Treasury swap spread` 0/0. |
| 5 | `Treasury auction` | 0 | 45 | ⛔ REJECTED | FALSE (foreign sovereign or other): "Treasury Bond Auction Announcement - RIKB 38 0215 - RIKS 50 0915 - Yahoo Finance" (Iceland); "Greece to auction €400 million in six-month treasury bills - eKathimerini.com"; "K Auction Receives 500,000 Treasury Shares as Free Transfer from Largest Shareholder - TipRanks"; plus Kenya, Ghana, Sri Lanka, Philippines and India bill auctions. Replacements: `Treasury note auction` ✅ PASS, 7 TRUE, all US coupon results (⚠️ misses 20Y/30Y *bond* and TIPS auctions). `year Treasury auction` ⛔ REJECTED for previews: "Why Today's 7-Year Treasury Auction Matters for Bond Yields - Barron's"; "10-Year Treasury Yield Closes at 5.01% Before $183 Billion Auction Test - TechStock²"; "Trump's $5,000 Voter Dividend Pledge Clouds Treasury Outlook Ahead of 30-Year Auction - finance.biggo.com". `Treasury auction tail` ⛔ REJECTED: "Treasury borrowing rates may rise ahead of retail bond auction - BusinessWorld" (the "tail" is inside "re**tail**"). |

**Tally: 1 pass, 4 rejected.** Tested replacements that PASS: `TIPS yield`, `hedge funds basis trade`, `Treasury note auction`, `Treasury term premium`, `term premium yields`, `term premium bond`, `swap spreads` (as-is).

### BOND pulled-deal query proposal (2026-09-28 packet) — assessment, no config edited

| Query form (Google News RSS) | Window | Items | Finding |
|---|---|---|---|
| As proposed: `"pulls bond sale" OR "pulled its bond" OR "postpones bond offering" OR "postpones notes offering" OR "shelves debt sale" OR "scraps bond deal" OR "junk bond" "withdrawn" OR "high-yield" "postponed"` | 30d | **0** | **Would return nothing.** |
| The six exact phrases only (parenthesised) | 30d / 90d / no window | **0 / 0 / 0** | The exact verb forms do not occur in Google-News titles. The zero therefore does not come from the tail alone. |
| `("junk bond" OR "high-yield") (withdrawn OR postponed OR pulled OR shelved)` | 30d | 0 | — |
| `"high-yield" "postponed"` (the unparenthesised tail on its own) | 60d | 4 | All noise (3 Coinbase prediction markets, 1 IPO delays). ⚠️ Unparenthesised, Google ANDs adjacent terms around `OR`. Parenthesise every group. |
| Reshaped: `"bond sale" (pulled OR pulls OR postpones OR postponed OR shelves OR scraps OR delays OR delayed OR withdraws)` | 60d | 53 (94 with `bond offering`/`debt sale`/loan variants) | Returns real events, but about 3 of 53 are TRUE pulled deals and all 3 are **non-USD**: "Doosan Enerbility Scraps $300 Million Bond Sale as Rates Bite - Seoul Economic Daily"; "Henan Issuer Asserts It Can Redeem $160M Despite Postponed Offshore Bond Sale - Briefs Finance"; "Indonesian Stocks Rise… as Danantara Delays Bond Sale - Jakarta Globe". The rest are new-issue noise (Uber, Paramount, Alphabet, SoftBank) plus "Drive Sober or Get Pulled Over…". |
| Press-release form: `"notes offering" (postpones OR postponement OR postponed OR withdraws OR withdrawal OR terminates)` and related queries | 180d | 17 | 0 relevant. |

**Phrase test on the reshaped query (60 days, 94 headlines):**

| Phrase | Live hits | Classification |
|---|---|---|
| `scraps bond sale` | 1 | TRUE (Doosan) |
| `postponed bond sale` | 1 | TRUE (Henan LGFV) |
| `delays bond sale` | 1 | TRUE (Danantara) |
| `pulls bond sale`, `postpones bond sale`, `shelves bond sale`, `pulls debt sale`, `pulled bond sale` | 0 | — |
| `postpones notes offering`, `postponement notes offering`, `postpones bond offering`, `withdraws notes offering` | 0 | — (synthetics ✓) |

**All three TRUE hits are outside BOND's USD-HY scope** (KR corporate, CN LGFV, ID sovereign fund), so they would be routing and classification work, not trigger evidence.

**Verdict on the proposal:**
- Do **not** land the query as written; it returns zero.
- A reshaped `when:7d "bond sale" (…verbs…)` query plus verb-phrase WATCH_FOR terms works mechanically, at roughly 94% query-level noise.
- **USD-HY recall is unproven.** No USD-HY withdrawal headline appeared anywhere in 60–180 days of live samples. That is uninformative rather than a zero, which is BOND's own limit (1).

---

## 3. HENRY — drop 6 old, propose 6 (all keyed to HEN-46)

Dropping all six current phrases is agreed. They are not tested further; the prior BRENT rejection and the `SPR`/`gas` matcher defects stand.

**Live queries:**
- **30-day run:** `Jazan refinery`, `Jazan`, `Russia diesel export ban`, `Russia fuel export ban`, `American Airlines guidance`, `Southwest Airlines guidance`, `airline fuel costs`, `airlines jet fuel` → 528 headlines.
- **60-day run:** `Jazan`, `Jazan refinery restart`, `Jizan refinery`, `Russia diesel export ban`, `American Airlines outlook`, `American Airlines forecast`, `Southwest Airlines outlook`, `American Airlines`, `Southwest Airlines` → 611 headlines.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Jazan restart` | 0 | 0 (30d) · **6 (60d)** | ⛔ REJECTED | **6 FALSE: restart *delays*, not restarts.** "Saudis Delay Restart of Jazan Plant to Late August, IIR Says - Bloomberg.com"; "Saudi Aramco delays Jazan oil refinery restart to August 30, IIR note shows - The Economic Times"; "Saudi Aramco delays Jazan refinery restart to August 30 - Oil & Gas Middle East"; "THIS MORNING: Aramco delays Jazan restart - EnterpriseAM"; plus Zawya and Caliber.Az copies. ⚠️ A 30-day-only window would have PASSED it; the delay stories were 8/10–11. Replacement `Jazan restarts`: 0/0, synthetic ✓ (⚠️ misses "restarted"). |
| 2 | `Jazan resume` | 0 | 0 (60d) | ✅ PASS | Synthetic "…Jazan refinery resumes operations" ✓. ⚠️ A forward-intent "Aramco to resume…" would match as a precursor; none was observed. |
| — | spelling | — | — | ⚠️ | **The lane itself carried "Saudi Aramco's Jizan Refinery Hit Again…" (OilPrice, 9/07).** Add `Jizan restarts` / `Jizan resumes`. |
| 3 | `Russia diesel export extend` | 0 | **33 (30d), all TRUE** | ✅ PASS | Examples: "Russia extends diesel export ban until end of October - reuters.com", FT, Bloomberg, Rigzone. 5 are sourced pre-decision reports ("Russia set to extend… Vedomosti reports - reuters.com") and are counted TRUE because they carry the outcome. ⚠️ **Lane 0 is a lane recall gap:** the `diesel-export-policy` query returned only US-ban stories on 9/29–9/30 and carried none of the Russian extension. ⚠️ **F3 leg 1 appears resolved:** extended to 10/31 per 33 headlines; HENRY to grade. ⚠️ The **lapse** side is unwatched. Tested `Russia diesel export lift` and `Russia diesel export expire`: 0/0, synthetics ✓. |
| 4 | `American Airlines guidance` | 0 | 0 (60d) | ✅ PASS | ⚠️ **Recall gap, live-proven:** AAL's guidance events in the window were headlined "outlook"/"warning", e.g. "American Airlines Stock Slides As Fuel Costs Crush 2026 Outlook - StocksToTrade" and "…offsets $1 billion fuel cost warning - AD HOC NEWS". Tested: `American Airlines raises` ✅ 0/0, synthetic ✓. `American Airlines outlook` ⛔ ("Zacks Industry Outlook Delta Air, American Airlines, and Copa - Yahoo Finance"). `American Airlines forecast` ⛔ ("The 9@9: … holiday shopping forecast, new American Airlines app - KSAT"). `American Airlines cuts` ⛔ ("United and American airlines say fuel-cost surge may require capacity cuts - Chicago Tribune"). |
| 5 | `Southwest Airlines guidance` | 0 | 3 | ⛔ REJECTED | 3 FALSE against F4 (an FY guide raise or cut). All are reaffirmations of a **Q3 EPS** guide: "Southwest Airlines stock gains as CFO reiterates Q3 EPS guidance despite fuel hit - AD HOC NEWS"; "Southwest Airlines stock holds on to profit guidance - AD HOC NEWS"; "Southwest Airlines stock holds Q3 EPS guidance as fuel costs rise - AD HOC NEWS". *If HENRY wants reaffirmations as well, these reclassify TRUE and it passes; that is the owner's call.* Tested: `Southwest Airlines raises` ✅ 0/0, synthetic ✓. `Southwest Airlines cuts` ⛔ ("BMO cuts Southwest Airlines stock target to USD 50.00 - AD HOC NEWS"). `Southwest Airlines outlook` ⛔ ("S&P upgrades Southwest Airlines outlook on earnings growth" is a credit outlook). |
| 6 | `airline fuel cost` | 2 | 16 | ⛔ REJECTED | As HENRY expected. FALSE (live): "IAG selects OpenAirlines' SkyBreathe platform to trim fuel costs - FlightGlobal"; "Air Cargo Demand Climbs 4.4% as Airlines Face Soaring Fuel Costs Ahead of Peak Season - Devdiscourse"; "Flair Airlines secures $76M bailout from Ottawa as fuel costs soar - CBC" (non-US carrier). FALSE (lane 8/18): "Airlines in 'stand-off' over price cuts as jet fuel costs ease". |

**Tally: 3 pass, 3 rejected.** Suggested replacements, all PASS: `Jazan restarts`, `Jizan restarts`, `Jizan resumes`, `American Airlines raises`, `Southwest Airlines raises`, `Russia diesel export lift`, `Russia diesel export expire`. ⚠️ The lane fetches neither airline guidance nor the Russian diesel ban (0 lane headlines), so even passing phrases need a lane query to fire.

---

## 4. HOMER — 14-phrase set (packet `9c874fb75` + addendum: #10 → `Horton Reports`, +#13, +#14)

**Live queries:**
- **Servicer/policy run (90 days):** `Freedom Mortgage`, `loanDepot`, `mortgage servicing transfer`, `Ginnie Mae issuer`, `Mortgagee Letter`, `maturity-adjusted delinquency`, `non-warrantable condo` → 255 headlines.
- **Builder run (90 days):** `Lennar earnings`, `Lennar third quarter`, `KB Home results`, `KB Home earnings`, `D.R. Horton earnings`, `D.R. Horton`, `PulteGroup earnings`, `Toll Brothers earnings`, `NVR earnings`, `LGI Homes`, `homebuilder earnings` → 598 headlines.
- **Replacement run (90 days):** 362 headlines.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Freedom Mortgage downgrade` | 0 | 0 | ✅ PASS | Synthetic "Moody's downgrades Freedom Mortgage…" ✓. ⚠️ "S&P cuts … rating" wording is missed. |
| 2 | `loanDepot downgrade` | 0 | 0 | ✅ PASS | Synthetic "Fitch downgrades loanDepot…" ✓. Synthetic "S&P cuts loanDepot rating…" ✗. |
| 3 | `emergency servicing transfer` | 0 | 0 | ✅ PASS | Recall unproven. |
| 4 | `Ginnie Mae issuer default` | 0 | 0 | ✅ PASS | "Mae" drop confirmed (title-case, 3 characters). Synthetic "Ginnie Mae seizes servicing portfolio of defaulted issuer" ✓. |
| 5 | `Mortgagee Letter loss mitigation` | 0 | 0 | ✅ PASS | Synthetic "HUD extends Mortgagee Letter 2026-08 loss mitigation deadline" ✓. |
| 6 | `maturity-adjusted delinquency` | 0 | 0 | ✅ PASS | Synthetic ✓. ⚠️ The hyphen is literal, so "maturity adjusted" without it is missed. |
| 7 | `non-warrantable condo` | 0 | 1 | ⛔ REJECTED | FALSE: "UWM Broadens Non-Warrantable Condo Financing, Adds Eligibility Tool - National Mortgage Professional". This is a lender product, not the GSE policy action the trigger keys to. Replacement `Fannie Mae non-warrantable`: 0/0, synthetic ✓. CORAL holds the related `Fannie Mae condo warrantability`; reconcile per the CORAL↔HOMER overlap. `condo project review` ⛔ REJECTED (e.g. "Planners to review 192-foot hotel/condo project; will they get a say? - Treasure Coast News"). |
| 8 | `Lennar Reports` | 0 | 7 | ✅ PASS | All TRUE: "Lennar Reports Third Quarter 2026 Results - TradingView", "Lennar (LEN) Reports Q3 Earnings…", etc. ⚠️ Synthetic "Lennar misses estimates as margins shrink" ✗; only reports/PR-style titles match. |
| 9 | `KB Home Reports` | 0 | 7 | ⛔ REJECTED | 2 FALSE previews: "Earnings To Watch: KB Home (KBH) Reports Q3 Results Tomorrow - TradingView" and the same title on Yahoo Finance. HOMER's addendum counted these TRUE; a day-before preview does not report the print. `KB` binding confirmed. Replacement **`KB Home Reports Quarter`**: 4 TRUE, 0 FALSE ("KB HOME REPORTS 2026 THIRD QUARTER RESULTS - PR Newswire", marketscreener, TradingView, Pulse 2.0), and it excludes the "Reports Q3 Results Tomorrow" form. |
| 10 | `Horton Reports` | 0 | 1 | ✅ PASS | TRUE: "D.R. Horton, Inc., America's Builder, Reports Fiscal 2026 Third Quarter Earnings…". The withdrawn `America's Builder` is confirmed ⛔: "D-FW real estate: Will tariffs hurt America's biggest homebuilder? - Dallas News". |
| 11 | `PulteGroup Reports` | 0 | 5 | ✅ PASS | All TRUE (Q2 print: Business Wire PR, Yahoo, TradingView, marketscreener). |
| 12 | `Toll Brothers Reports` | 0 | 1 | ✅ PASS | The harness query set returned 0. A separate `Toll Brothers results` 90-day query surfaced the 8/19 PR "Toll Brothers Reports FY 2026 Third Quarter Results - The Manila Times"; the re-run matched it TRUE. |
| 13 | `NVR Announces` | 0 | 1 | ✅ PASS | TRUE: "NVR, INC. ANNOUNCES SECOND QUARTER RESULTS - Yahoo Finance". `NVR` binding confirmed. |
| 14 | `LGI Homes Reports` | 0 | 4 | ⛔ REJECTED | 3 FALSE monthly-closings releases, not the earnings print: "LGI Homes, Inc. Reports July 2026 Home Closings - globenewswire.com"; "LGI Homes, Inc. Reports June and Second Quarter 2026 Home - globenewswire.com"; "LGI Homes Reports June and Second Quarter 2026 Home Closings, Sets Q2 Earnings Call for August 4 - Quiver Quantitative". Replacement **`LGI Homes Reports Results`**: 1 TRUE ("LGI Homes, Inc. Reports Strong Second Quarter 2026 Results - globenewswire.com"), 0 FALSE. |

**Tally: 11 pass, 3 rejected (#7, #9, #14).** Replacements that PASS: `Fannie Mae non-warrantable`, `KB Home Reports Quarter`, `LGI Homes Reports Results`.

**Builder-earnings recall gap (confirmed): the lane holds 0 headlines naming Lennar, KB Home, Horton, Toll Brothers or PulteGroup in 10,405.** The `housing` query's `"homebuilder"` term does not fetch company press releases. The phrases do match the real PR titles in the live sample (Lennar 7, KB 4 after the fix, Pulte 5, Toll, NVR, Horton), so **the gap is the lane query, not the phrases.**

A candidate lane query was tested, not landed (lane semantics are WALTER's; PROME lands): `when:30d ("Lennar" OR "KB Home" OR "D.R. Horton" OR "PulteGroup" OR "Toll Brothers" OR "NVR, Inc." OR "LGI Homes" OR "Meritage Homes" OR "Dream Finders") ("reports" OR "announces") (results OR earnings OR quarter)`.
- It returned **4 items in 30 days, including both missed prints:** "KB HOME REPORTS 2026 THIRD QUARTER RESULTS - PR Newswire" (9/22) and "Lennar Reports Third Quarter 2026 Results - TradingView" (9/16).
- The other 2 are Dream Finders/Beazer consent-solicitation items, which no HOMER phrase matches.
- Without the `reports/announces` group, a 7-day form returns 40+ items, mostly stock chatter.

---

## 5. CRUISE — six ticker-bound phrases

**Live queries:**
- **CRUISE run (90 days):** `CCL Industries`, `Carnival guidance`, `Carnival Corporation earnings`, `Royal Caribbean guidance`, `Royal Caribbean conference call`, `Norwegian Cruise Line guidance`, `Norwegian Cruise Line Holdings conference call`, `Carnival conference call`, `CCL stock`, `NCLH stock`, `RCL stock` → 695 headlines.
- **Name-form run (90 days):** 550 headlines.
- **CCL Industries collision sample:** `"CCL Industries"` over 180 days (43 items) and `"CCL Industries" (conference OR guidance OR outlook)` over 365 days (12 items).

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `CCL guidance` | 0 | 4 | ✅ PASS | All TRUE (Carnival): "Carnival (NYSE:CCL) Issues Q4 2026 Earnings Guidance - MarketBeat"; "Carnival Corporation (CCL) Beats Q3 Guidance; Raises Bookings Outlook - TradingView"; "Carnival (NYSE:CCL) Announces FY 2026 Earnings Guidance - MarketBeat"; a TradingKey (Portuguese) raised-EPS-guide item. **CCL Industries collision: 0 observed** in 695 live headlines and in the 180- and 365-day CCL Industries samples. **However, synthetic "CCL Industries raises guidance" → MATCHES**, and `\bCCL\b` also matches "TSX:CCL.B". The collision is mechanically live, just not observed. ⚠️ Synthetic "Carnival raises full-year guidance again" ✗. |
| 2 | `RCL guidance` | 0 | 3 | ✅ PASS | TRUE: "RCL: Q2 2026 delivered robust revenue and occupancy, with FY guidance raised…"; "Royal Caribbean (RCL) Stock Ignores Margin Strength And Guidance Lift - Simply Wall Street" (a lagged secondary). Also "RCL Q1 2026 Earnings: EPS Surges Past Estimates… - Guidance Revision Trend - dars.gov.et": the content is a true RCL guidance event, but it is a stale Q1 repost on a suspect domain. Counted TRUE; flagged. |
| 3 | `NCLH guidance` | 0 | 2 | ✅ PASS | TRUE: "NCLH's Q2 outperforms but full-year guidance disappoints - Seatrade Cruise News"; "Norwegian Cruise Line (NCLH) Tops Q2 EPS by 10c… Offers FY26 EPS Guidance - streetinsider.com". |
| 4 | `CCL conference call` | 0 | 0 | ✅ PASS | **No collision observed:** CCL Industries' call PR reads "CCL to Hold Live Webcast Call to Discuss 2026 Second Quarter Results…" (Yahoo, 7/23), with no "conference". ⚠️ **Live-proven recall MISS:** Carnival's own call PR in the window, "CARNIVAL CORPORATION LTD. TO HOLD CONFERENCE CALL ON THIRD QUARTER EARNINGS - Yahoo Finance", carries no "CCL", so #4 missed it. `Carnival Corp conference call` caught it (1 TRUE). |
| 5 | `RCL conference call` | 0 | 0 | ✅ PASS | ⚠️ Synthetic "Royal Caribbean Group to Host Third Quarter 2026 Conference Call" ✗. Issuer PRs use the name, not the ticker. `Royal Caribbean conference call`: 0/0, synthetic ✓. |
| 6 | `NCLH conference call` | 0 | 0 | ✅ PASS | ⚠️ Synthetic "Norwegian Cruise Line Holdings Ltd. to Host Third Quarter 2026 Earnings Conference Call" ✗. `Norwegian Cruise conference call`: 0/0, synthetic ✓. |

**Name-form alternatives (CRUISE's named fallback plus two more), live over 90 days:**

| Phrase | Hits | Verdict | Note |
|---|---|---|---|
| `Carnival Corp guidance` | 5 TRUE | ✅ PASS | "Corp" also matches "Corporation". |
| `Carnival Corp conference call` | 1 TRUE | ✅ PASS | — |
| `Royal Caribbean guidance` | 8 TRUE | ✅ PASS | Includes "ROYAL CARIBBEAN GROUP REPORTS SECOND QUARTER RESULTS… AND RAISES FULL YEAR GUIDANCE - PR Newswire" and "Why Royal Caribbean Stock Is Rising After Revenue Guidance Cut - Barron's". |
| `Norwegian Cruise guidance` | 12 TRUE | ✅ PASS | Includes "Norwegian Cruise Line Lowers Full-Year Earnings Guidance" and "Norwegian Cruise Line Holdings raises Q3 guidance, announces $750m notes offering - Data Portuaria". |
| bare `Carnival guidance` | 16 | ⛔ REJECTED | FALSE: "Uckfield Bonfire Society scrap torches and cancel fireworks at this year's carnival due to Government's fire safety guidance - SussexWorld". Use `Carnival Corp guidance`. |

**Tally: 6 pass, 0 rejected.** ⚠️ **The ticker forms caught 9 guidance headlines; the name forms caught 25, with 0 false.** #4 missed Carnival's own call-date PR. Recommend CRUISE adopt the name forms (`Carnival Corp …`, `Royal Caribbean …`, `Norwegian Cruise …`) alongside or instead of the ticker forms. This also removes the latent CCL Industries collision.

---

## Group B tally

| Desk | Pass | Rejected | Rejected phrases |
|---|---|---|---|
| FLG | 11 | 0 | — |
| BOND | 1 | 4 | `term premium`, `real yields`, `basis trade`, `Treasury auction` |
| HENRY | 3 | 3 | `Jazan restart`, `Southwest Airlines guidance`, `airline fuel cost` |
| HOMER | 11 | 3 | `non-warrantable condo`, `KB Home Reports`, `LGI Homes Reports` |
| CRUISE | 6 | 0 | — |
