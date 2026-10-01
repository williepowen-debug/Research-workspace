# WQ-295 R3: WATCH_FOR live test, GROUP A (LIQUID · CREED · WAL · REGINALD · DEWEY)

**Run:** 2026-10-01, WALTER test subagent. Read-only: nothing landed, nothing committed. The lane repo was not pulled or written. **Verdicts are WALTER's test result. Owners adopt or decline, and PROME lands.**

## Method

- **Matcher:** the real `match_watch_for()` from `~/Research-Intake/scripts/newsweep_config.py`, run in memory by `AGENTS/WALTER/tools/watch_for_harness.py`. Matching rules:
  - Every word longer than 3 characters must appear as a case-insensitive substring.
  - Words of 3 characters or fewer are dropped (`cut`, `bar`, `Ave`, `St`, `V`, `and`).
  - Words in the skip list are dropped (`above`, `below`, `from`, `with`, `that`, `this`, `than`, `into`).
  - Tokens matching `[A-Z][A-Z0-9-]{1,4}` are entity tokens. They must match case-sensitively on a word boundary, so `REIT` does **not** match `REITs`.
- **Lane corpus:** 10,405 unique headlines from 71 lane days, 2026-06-29 → 2026-09-30, as of the last lane commit on 2026-09-30 17:59 ET.
  - ⚠️ **8,780 of the 10,956 raw lane titles carry a Google-News ` - Outlet` suffix**, and the matcher reads it as part of the title. Outlet names are therefore live match text. This is where the `reserve scarcity` false hit and the `MBA …` true hit both came from.
  - Lane `description` is empty in all 10,956 items, so a title-only test matches what runs in production.
- **Live corpus:** Google-News RSS, 30-day window, using on-topic subject queries plus the phrase itself run as a query. Generic phrases were run as their own query to expose the off-topic class. For named Nano Banc entities, a 365-day window was also run, because 30 days of thinly covered names says little.
- **Classification:** I classified each hit TRUE if it reports the event the phrase is keyed to, and FALSE otherwise. **R3 rule: ⛔ REJECTED at more than 0 FALSE hits; ✅ PASS otherwise.** Synthetic headlines test recall only, never noise.
- **A 0 is labelled UNINFORMATIVE** wherever neither corpus could have contained the event.
- 🔴 **Lane-coverage caveat for the whole Nano Banc cluster:** the lane holds **0 Nano Banc or Sunwest headlines** for 9/25–9/30, the days the bank failed. All 15 TRUE `Nano Banc` hits came from Google-News queries that the lane does not run. **A clean phrase only fires if a lane feed carries the headline.** Fixing that is a lane-query question for PROME. Phrase wording cannot fix it.

---

## LIQUID (sources: `inbox/2026-09-26_from-LIQUID_WATCH_FOR-R3-retest-list.md`, `inbox/2026-09-29_from-LIQUID_R3-harness-pre-read-…md`, both read whole)

**Live queries (30d, headline count):**

| Query | Headlines |
|---|---:|
| `junk bond spreads` | 43 |
| `high-yield spreads` | 68 |
| `repo rate` | 100 |
| `standing repo facility` | 17 |
| `money market fund` | 100 |
| `Treasury auction` | 100 |
| `weak Treasury auction` | 42 |
| `bank reserves Fed` | 67 |
| `reserve scarcity` | 41 |
| `ample reserves` | 38 |
| `scarce reserves` | 28 |
| `Fed balance sheet reserves` | 56 |
| `repo market stress` | 33 |

The run returned 606 unique headlines. **The reserves subject was widened from LIQUID's 2 headlines to about 230.**

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `HY OAS above 350` (current) | 0 | 0 | ✅ PASS (noise) | The design is dead. It reduces to `HY`+`OAS` (`above` is skipped and `350` is dropped), and headlines rarely print "OAS". **I agree with LIQUID's re-word.** |
| 1′ | `junk bond spreads widen` (proposed) | 0 | 0 / 111 | ✅ PASS | ✅ Caught "Junk bond spreads widen most since April…". ⚠️ It misses "High-yield spreads widen…". **Add `high-yield spreads widen`:** 1 live hit, TRUE ("Lisa Abramowicz: High-yield bond spreads widen sharply since October 2025 - Traders Union"), 0 FALSE, synthetic caught. Do **not** use `junk spreads`: 4 lane hits, all FALSE ("Junk bonds' 'thin' spreads are an illusion - Reuters", ×4 variants). |
| 2 | `repo rate spike` (keep) | 0 | 0 / 133 | ✅ PASS | ✅ Caught "Repo rates spike as quarter-end liquidity dries up". |
| 3 | `SRF usage` (current) | 0 | 0 | ✅ PASS (noise) | Dead on design: the press writes the facility's name. **I agree with the re-word.** |
| 3′ | `standing repo facility` (proposed) | 0 | 0 / 150 | ✅ PASS | ✅ Caught "Banks tap Fed's standing repo facility for record $50 billion". |
| 4 | `money market fund break` (current) | 0 | **1 FALSE** | ⛔ **REJECTED** | FALSE: **"ICI: Money Market Fund Assets Continue Record-Breaking Growth - Yahoo Finance"**. "break" is a substring of "Breaking". This confirms LIQUID's pre-read. |
| 4′ | `money market fund breaks buck` (proposed) | 0 | 0 / 100 | ✅ PASS | ✅ Caught "Money market fund breaks the buck". |
| 5 | `Treasury auction failure` (keep) | 0 | 0 / 142 | ✅ PASS | ⚠️ "failure" is not a substring of "fails" or "failed", so it **missed "Treasury auction fails to draw demand"**. **Suggest `Treasury auction fail`:** 0 lane, 0 / 142 live, synthetic caught. ⚠️ Neither phrase catches "weak/sloppy/tailing auction", which is how the press usually reports a low bid-to-cover. The registered trigger is a ratio below 2.0x, and that ratio is rarely a headline word. |
| 6 | `bank reserve crunch` (current) | 0 | 0 | ✅ PASS (noise) | Dead on design. **I agree with the re-word.** |
| 6′ | `reserve scarcity` (proposed) | 0 | **1 FALSE** | ⛔ **REJECTED** | FALSE: **"Mitigating Labour Scarcity and Land Costs: SSI Schaefer Korea Brings Global Best Practices to Domestic Manufacturers - The Malaysian Reserve"**. "Reserve" came from the **outlet suffix**, which lane titles also carry. The same mechanism will fire on "Federal Reserve … scarcity". **Suggest `reserves scarce`:** 0 lane, 0 / ~230 on-topic reserves headlines. ✅ It caught "Reserves are becoming scarce, Fed's Logan says" and "Fed sees bank reserves nearing scarce levels", both of which `reserve scarcity` misses. |

**Tally (LIQUID's 10): 8 pass, 2 rejected** (`money market fund break`, `reserve scarcity`).

**Clean set if LIQUID adopts:** `junk bond spreads widen` · `high-yield spreads widen` · `repo rate spike` · `standing repo facility` · `money market fund breaks buck` · `Treasury auction fail` (or keep `…failure`) · `reserves scarce`.

---

## CREED

### A. Standing candidates (source: `inbox/2026-09-26_from-PROME_CREED-watch-for-candidates-R3-live-test.md`, read whole; T-06b, T-08a and T-08b checked against `AGENTS/CREED/registry/THRESHOLDS.tsv`)

**Live queries (30d, headline count).** Pass 1, on-topic subjects:

| Query | Headlines |
|---|---:|
| `Trepp CMBS delinquency` | 9 |
| `CMBS delinquency rate` | 10 |
| `special servicing rate` | 16 |
| `office CMBS` | 62 |
| `commercial real estate maturity default` | 15 |
| `CMBS balloon maturity` | 3 |
| `FDIC Quarterly Banking Profile` | 4 |
| `noncurrent commercial real estate loans` | 0 |
| `commercial real estate loan modification` | 28 |
| `extend and pretend commercial real estate` | 9 |
| `CRE note sale` | 1 |
| `deed-in-lieu` | 21 |
| `office building discounted sale` | 74 |
| `non-traded REIT redemptions` | 6 |
| `BREIT redemptions` | 1 |
| `redemption queue REIT` | 0 |
| `REIT stocks selloff` | 33 |
| `VNQ` | 30 |
| `10-year Treasury yield` | 100 |
| `FOMC` | 100 |
| `mortgage REIT dividend cut` | 62 |
| `mortgage REIT strategic alternatives` | 6 |
| `mortgage REIT wind-down` | 6 |
| `bank loan portfolio sale` | 62 |
| `MBA commercial multifamily mortgage debt` | 7 |
| `life insurers commercial mortgages` | 33 |

Pass 1 returned 642 unique headlines.

Pass 2, each phrase run as its own query plus re-word subjects:

| Query | Headlines |
|---|---:|
| `loan modification` | 63 |
| `strategic alternatives` | 83 |
| `share repurchase plan` | 100 |
| `note sale` | 69 |
| `discounted sale` | 100 |
| `re-default` | 69 |
| `maturity default` | 43 |
| `newly delinquent` | 23 |
| `redemptions suspended` | 32 |
| `suspends redemptions` | 15 |
| `redemption queue` | 20 |
| `non-traded REIT` | 67 |
| `extend and pretend` | 10 |
| `mortgage REIT dividend` | 59 |
| `REIT redemptions` | 14 |
| `CRE loan sale` | 62 |
| `CRE loan portfolio` | 71 |
| `life insurers mortgage` | 71 |
| `nonresidential` | 55 |
| `balloon maturity` | 22 |
| `noncurrent loans` | 5 |
| `Trepp` | 7 |

Pass 2 returned 1,063 unique headlines.

Pass 3, re-words:

| Query | Headlines |
|---|---:|
| `deed in lieu of foreclosure` | 10 |
| `returned to lender` | 70 |
| `handed back to lender` | 8 |
| `property fund redemptions` | 46 |
| `mortgage REIT cuts dividend` | 66 |
| `special servicing` | 69 |

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Trepp CMBS delinquency report` | 0 | 0 | ✅ PASS | ⚠️ Trepp coverage titles end ": Trepp" with no "report" (live: "Multifamily CMBS servicing rate declined, delinquencies stayed flat in August: Trepp - Multifamily Dive"). Recall is near zero. **Add `CMBS delinquency rate`:** 1 lane + 4 live hits, **all TRUE** (e.g. "KBRA-rated U.S. CMBS delinquency rate rises in September - Traders Union"), 0 FALSE. ✅ It caught "CMBS delinquency rate rises in September: Trepp". ⚠️ Its hits include KBRA prints and stale months, and T-01a is Trepp-basis, so read the source. ⚠️ "delinquency" does not substring-match "delinquencies". |
| 2 | `office CMBS delinquency` | 0 | 3, all TRUE | ✅ PASS | The TRUE hits were "Office CMBS Delinquency Rate at Highest Level This Decade - Commercial Observer", "CMBS Delinquency Holds at 7.85% as Office Risk Rises - Yahoo Finance", and a KBRA print. ⚠️ It misses all-property headlines with no "office"; phrase #1′ covers those. |
| 3 | `Trepp special servicing report` | 0 | 0 | ✅ PASS | ⚠️ Same "report" recall gap as #1. **Suggest `Trepp special servicing`:** 0 lane, 0 live, ✅ caught "Trepp: office special servicing rate hits 17%". Do **not** use `special servicing rate`: 1 FALSE, "News \| Higher rates scramble CMBS playbook; New York loan moves to special servicing early; Deadline looms for Jersey City hotel loan - CoStar", where "rate" matched inside "rates". |
| 4 | `office special servicing` | 0 | 0 / 85 | ✅ PASS | ⚠️ It missed the real headline "CMBS Special Servicing Hits Highest Rate Since 2013 - Yahoo Finance". Nothing tested captures that wording cleanly. |
| 5 | `matured balloon` | 0 | 0 / 25 | ✅ PASS | — |
| 6 | `maturity default` | 0 | 0 / 58 | ✅ PASS | — |
| 7 | `newly delinquent` | 0 | 0 / 23 | ✅ PASS | — |
| 8 | `FDIC Quarterly Banking Profile` | 0 | 0 / 4 | ✅ PASS (thin) | The 0 is UNINFORMATIVE: the Q3 QBP is not out until late November. ✅ Synthetic caught. |
| 9 | `noncurrent CRE` | 0 | 0 / 5 | ✅ PASS (thin) | ✅ Synthetic caught. ⚠️ Headlines that spell out "noncurrent commercial real estate loans" miss it, because `CRE` is a required case-sensitive token. |
| 10 | `nonfarm nonresidential` | 0 | 0 / 55 | ✅ PASS | — |
| 11 | `loan modification` | 0 | 0 / 91 | ✅ PASS | ⚠️ The on-topic sample is consumer-mortgage heavy ("Mortgage Relief…", "What Is Mortgage Forbearance…"). A consumer "loan modification" headline would be FALSE for T-04. None appeared in a title here, but that class is the residual risk. |
| 12 | `extend and pretend` | 0 | 0 / 19 | ✅ PASS | — |
| 13 | `re-default` | 0 | 0 / 69 | ✅ PASS | — |
| 14 | `discounted sale` | 0 | **10 FALSE** | ⛔ **REJECTED** | **"25+ Of The Best Discounted Games From Xbox's Publisher Spotlight Sale - purexbox.com"**; **"Harbour Energy's top shareholder further cuts stake to 16% in discounted share sale - reuters.com"**; plus 8 more games, retail and share sales. |
| 15 | `note sale` | 0 | **21 FALSE** | ⛔ **REJECTED** | **"Hit the right note at Yorktown Music Boosters' annual tag sale - Halston Media Group"**; **"AIG closes €1.1 billion euro-denominated note sale in two tranches - app.dealroom.co"**; **"Xiaomi Redmi Note 17 5G is already on sale – days after launch - Trusted Reviews"**. |
| 16 | `deed-in-lieu` | 0 | 0 / 31 | ✅ PASS | ⚠️ **The press writes it unhyphenated**, so it missed "Dania Beach condo community trades in deed in lieu of foreclosure - The Business Journals". **Add `deed in lieu`:** 1 live hit, TRUE. **Add `returned to lender`:** 1 live hit, TRUE ("Hell's Kitchen office buildings once targeted for life-sciences project returned to lender - The Business Journals"), 0 FALSE / 78. Do **not** use `back to lender`: 4 FALSE, e.g. "Private student loans with rewards: These lenders offer cash back and discounts - CNBC". |
| 17 | `below basis` | **3 FALSE** | **1 FALSE** | ⛔ **REJECTED** | `below` is in the matcher's skip list, so the phrase is just `basis`. Lane FALSE: **"EUR/USD Cross-Currency Basis Futures - CME Group"**, "The SOFR–federal funds rate basis saw strong buying interest…", "…Wheat Basis, and Harvest Strategy - Oklahoma Farm Report". Live FALSE: **"FOMC Raises Fed Funds Rate Range by 25 Basis Points in 12-0 Vote - Yahoo Finance"**. No clean re-word was found. |
| 18 | `redemptions suspended` | 0 | 0 / 47 | ✅ PASS | ⚠️ "suspended" is not a substring of "suspends", so it **missed "Starwood REIT suspends redemptions"**. That is the 'suspend' blind spot CREED's own VX-5.03 census found. **Add `REIT redemptions`:** 0 lane, 0 live / 81. ✅ It caught "Blackstone REIT limits redemptions…" and "Starwood REIT suspends redemptions". **Add `property fund redemptions`:** 2 live hits, **both TRUE**: "Deutsche Bank's DWS to Shut US Property Fund Hit by Redemptions - Bloomberg.com" and "Market Chatter: Deutsche Bank's DWS Considers Limits on German Property Fund Redemptions - Yahoo Finance". **These are live T-06b-class events that no CREED phrase caught.** Do **not** use `suspend redemptions`: 1 FALSE, "Metrics Credit Partners suspends redemptions from $11b feeder funds as audit crisis deepens", an Australian private-credit fund that is not CRE. |
| 19 | `share repurchase plan` | 0 | **12 FALSE** | ⛔ **REJECTED** | **"Nvidia Adds $150 Billion to Existing Share Repurchase Plan - U.S. News Money"**; **"Valvoline boosts share repurchase plan to $500M - TradingView"**. |
| 20 | `gated` | **3 FALSE** | 0 | ⛔ **REJECTED** | "gated" is a substring of "investigated". Lane FALSE: **"105-year-old investigated for crimes at Nazi PoW camp in Germany"**; **"Trainline, Virgin Atlantic and RED Driving School investigated over 'drip pricing'"**; "…Cliffwater Gated CCLFX…", a private-credit fund outside T-06b's open-end CRE scope. |
| 21 | `redemption queue` | 0 | 0 / 20 | ✅ PASS | — |
| 22 | `non-traded REIT` | 0 | 0 / 73 | ✅ PASS (sample) | ⚠️ The press writes "**Nontraded** REIT" ("JLL Launches Nontraded REIT For Real Estate Debt - Bisnow"), and `REIT` will not match "REITs". The phrase names a subject, not an event. The unhyphenated variant `nontraded REIT` drew 2 FALSE (fund launches), so it is not a fix. |
| 23 | `VNQ` | 0 | **19, ≥16 FALSE** | ⛔ **REJECTED** | **"VNQ Nov 2026 95.000 put (VNQ261120P00095000) stock price, news, quote and history - Yahoo Finance UK"**; **"VNQ Top Holdings List & Exposure (Vanguard Real Estate ETF) - MarketBeat"**; "Zurich and Tokyo top UBS housing bubble risk index (VNQ:NYSEARCA)". This confirms PROME's pre-read. |
| 24 | `REIT selloff` | 0 | 1 TRUE (borderline) | ✅ PASS ⚠️ | The hit was "NNN REIT's Rate-Driven Selloff Creates Opportunity…", a single-name, rate-driven REIT selloff. I graded it TRUE on mechanism, but it is not the sector tape. ⚠️ It misses "sell-off" (hyphenated) and "REITs". |
| 25 | `10-year Treasury` | **8 (≥3 FALSE)** | 44 | ⛔ **REJECTED** | Lane FALSE: **"Ultra 10-Year U.S. Treasury Note Futures Margins - CME Group"** (plus "…Overview" and "…Calendar"). The 44 live yield-move headlines ("10-year Treasury yield hits 5.1% for first time in 19 years \| CNN Business") report a rate move, not the T-08a event (VNQ vs SPY below −10pp). CREED reads T-08a from the instrument anyway. This confirms PROME's pre-read. |
| 26 | `FOMC` | **6 (≥2 FALSE)** | 65 | ⛔ **REJECTED** | Lane: **"EBC Live Trader Cup Indonesia Kicks Off Amid NFP and FOMC Season - EBC Financial Group"**. Live: **"Federal Open Market Committee (FOMC) \| History, Functions, & Members - Britannica"**, "When Is the Next FOMC Meeting? FOMC Meeting Schedule 2026 - Mitrade". This confirms PROME's pre-read. |
| 27 | `mortgage REIT dividend cut` | 0 | 0 / 121 | ✅ PASS (sample) ⚠️ **design defect** | `cut` (3 characters) is dropped, so the phrase fires on **any** mortgage-REIT dividend headline. Negative controls **matched**: "Mortgage REIT raises dividend 10%" and "Ellington Financial mortgage REIT declares monthly dividend". It **missed** "Mortgage REITs cut dividends…". **Re-word to `mortgage REIT cuts dividend`:** 0 / 66 live, ✅ caught "Mortgage REIT cuts dividend by 30%", and it does not match a raise. ⚠️ Name-only headlines ("KREF slashes dividend…") miss every variant. |
| 28 | `strategic alternatives` | 0 | **27 FALSE** | ⛔ **REJECTED** | **"Vertical Aerospace Announces Review of Strategic Alternatives to Support Next Phase of Development; Appoints Jefferies…"**; **"Cineplex explores strategic alternatives as new CEO Bill Walker takes the helm - Yahoo Finance UK"**. (Byproduct: "MacKenzie Realty … suspends preferred repurchase to pursue strategic alternatives". MacKenzie is a non-traded REIT, so that one may be T-06b-relevant for CREED.) |
| 29 | `wind-down` | 0 | **1 FALSE** | ⛔ **REJECTED** | **"SEIT Calls General Meeting on Board Appointments for Wind-Down - Yahoo Finance UK"**: a UK energy-efficiency investment trust, not a mortgage REIT. |
| 30 | `loan portfolio sale` | 0 | **3 (2 FALSE)** | ⛔ **REJECTED** | **"Mechanics Bank Completes Sale of Substantial Majority of Runoff Auto Loan Portfolio to Bank of America - Yahoo Finance"**; **"A&M advises Unión de Créditos Inmobiliarios on full Greek market exit through loan portfolio and servicing business sales"**. The third hit, "BCB Bancorp to Record $43.3 Million Pre-Tax Loss in Q3 From Sale of Problem Loan Portfolios", is a possible CRE-distress case for CREED. **Suggest `CRE loan portfolio`:** 0 lane, 0 / 133 live, ✅ caught "Bank sells $1 billion CRE loan portfolio at discount". |
| 31 | `MBA commercial multifamily mortgage debt outstanding` | 0 | 1 TRUE | ✅ PASS | The hit was **"Commercial, Multifamily Mortgage Debt Outstanding Increased by $42.9B in Second Quarter - MBA Newslink"**, which is the PRED-CREED-006 Q2 release, now out. ⚠️ It matched only because `MBA` came from the **outlet suffix**, so secondary coverage without "MBA" will miss. |
| 32 | `life insurer mortgage holdings` | 0 | 0 / 104 | ✅ PASS | — |

**Tally (CREED standing, 32): 21 pass, 11 rejected.** Rejected: `discounted sale`, `note sale`, `below basis`, `share repurchase plan`, `gated`, `VNQ`, `10-year Treasury`, `FOMC`, `strategic alternatives`, `wind-down`, `loan portfolio sale`.

**Tested additions that pass** (CREED adopts or declines): `CMBS delinquency rate` · `Trepp special servicing` · `REIT redemptions` · `property fund redemptions` · `deed in lieu` · `returned to lender` · `mortgage REIT cuts dividend` (replacing #27) · `CRE loan portfolio`.

**Tested and rejected:** `special servicing rate`, `suspend redemptions`, `back to lender`, `nontraded REIT`.

### B. Nano Banc block (queue row 3, supersedes PROME's first five; source `AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md` §3 via the queue)

**Live queries, 30d:**

| Query | Headlines |
|---|---:|
| `Nano Banc` | 35 |
| `FDIC Nano Banc` | 19 |
| `Nano Banc failure` | 36 |
| `Sunwest Bank` | 20 |
| `Honarkar` | 1 |
| `Makhijani` | 5 |
| `Laguna Beach` | 98 |
| `FDIC loan sale` | 5 |
| `failed bank loan sale` | 43 |
| `FDIC structured transaction` | 2 |
| `Preferred Bank` | 60 |
| `Cantor Group` | 41 |
| `Cantor Fitzgerald` | 100 |
| `Material Loss Review` | 25 |
| `Moreno Valley` | 48 |
| `Inland Empire` | 86 |
| `Chino` | 99 |
| `Bellflower` | 71 |
| `bank failure FDIC receiver` | 13 |

The 30-day run returned 720 unique headlines.

**Live queries, 365d:**

| Query | Headlines |
|---|---:|
| `Honarkar` | 9 |
| `Makhijani` | 52 |
| `Sunwest Bank` | 39 |
| `Preferred Bank` | 99 |
| `FDIC loan sale` | 39 |
| `FDIC structured transaction` | 6 |
| `Material Loss Review` | 78 |
| `failed bank loan sale` | 76 |
| `FDIC receiver notice to creditors` | 8 |
| `claims bar date FDIC` | 8 |
| `Nano Banc` | 51 |

**Lane: 0 for every phrase, and the lane holds no Nano Banc headline at all** (see the caveat in the header).

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Nano Banc` | 0 | **15, all TRUE** | ✅ PASS | Examples: "California's Nano Banc fails - Banking Dive"; "FDIC Appoints Sunwest Bank as Nano Banc's Acquiring Institution - PR Newswire". ✅ Caught every synthetic (FDIC sale, auction, MLR, claims deadline). **It subsumes every `Nano Banc …` phrase below**: any headline those catch, this catches too. Expect retrospective "6th bank failure of 2026" pieces. They are TRUE on subject but do not act on L515. |
| 2 | `Nano Banc receivership` | 0 | 0 | ✅ PASS | Subsumed by #1. |
| 3 | `FDIC as receiver for Nano Banc` (also DEWEY) | 0 | 0 | ✅ PASS | Subsumed by #1. |
| 4 | `FDIC loan sale` | 0 | 0 (30d) · **1 FALSE (365d)** | ⛔ **REJECTED** | **"First Citizens eyes loan sales to repay FDIC after SVB deal - American Banker"**: a bank selling loans, not an FDIC receivership sale. ⚠️ It also missed "FDIC sells $190 million of failed Nano Banc's loans", because "sale" is not a substring of "sells". **Suggest `FDIC sells loans` and `FDIC loan auction`:** 0 lane, 0 live (365d), synthetics caught. The noise sample is thin. |
| 5 | `FDIC structured transaction` | 0 | 0 / 8 | ✅ PASS (thin) | ✅ Synthetic caught. |
| 6 | `failed bank loan sale` | 0 | 0 / 119 | ✅ PASS | — |
| 7 | `Sunwest Bank` | 0 | 6 TRUE (30d) · **≥4 FALSE (365d)** | ⛔ **REJECTED** | 365d FALSE: **"Sunwest Bank Data Breach Exposes Social Security Numbers - Claim Depot"**; **"Sunwest Bank Expands in Colorado - ocbj.com"**; "Sunwest Bank Selected to Win the Benefits Innovator Award at Thrive Summit 2026 - PR Newswire"; "Zaldy Co got P802 million in bank deposits from Sunwest…" (a Philippine Sunwest). All 30-day hits were TRUE, but only because the failure dominates the window. #1 covers only 4 of the 6 TRUE hits. Two omit "Nano Banc": "Small California Bank Becomes The 6th U.S. Bank To Fail This Year. Sunwest Bank Assumed All Deposits. - 247wallst.com" and "BREAKING NEWS: Utah's Sunwest Bank Acquires Failed California Bank…". That recall loss is small and accepted here. |
| 8–11 | `23750 Alessandro Blvd Moreno Valley` · `3700 Inland Empire Blvd Ontario` · `12233 Central Ave Chino` · `9826 Cedar St Bellflower` | 0 | 0 / 304 geo headlines | ✅ PASS (noise) | **The 0 is UNINFORMATIVE for recall, and recall is near zero by construction.** Street numbers rarely appear in headlines. The matcher drops `Ave` and `St` but **requires `blvd`**, so "Boulevard" misses. |
| 12 | `Honarkar` | 0 | 0 / 9 (365d) | ✅ PASS (thin) | ✅ Caught "Honarkar wins final arbitration award…". The surname is distinctive. The noise sample is too small to say more. |
| 13 | `Laguna Beach` | 0 | **75 FALSE** | ⛔ **REJECTED** | **"Cracking Seawall Raises Concern In Laguna Beach As Strong Surf Pummels Coast - Patch"**; **"Laguna Beach Football Roster (2026-27) - maxpreps.com"**; "Diane Keaton's Final Laguna Beach Design Project To Hit the Market for $10.3 Million - Realtor.com". The queue's pre-note was right. |

**Tally (CREED Nano block, 13): 10 pass (4 of them inert addresses), 3 rejected** (`FDIC loan sale`, `Sunwest Bank`, `Laguna Beach`).

**CREED combined: 31 pass, 14 rejected.**

---

## WAL (queue row 4; PROME pointer 9/27)

Queries and corpora are shared with CREED Nano block B above.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Nano Banc loan sale` | 0 | 0 | ✅ PASS | Subsumed by `Nano Banc` (CREED B#1). |
| 2 | `Makhijani` (also DEWEY) | 0 | 14 TRUE · **3 FALSE (365d)** | ⛔ **REJECTED** | **"Princeton Staff Author Series featuring Pooja Makhijani - Inside Princeton"**; **"Mamta Makhijani promoted to VP and HR head at SBICAPS - HR Katha"** (×2 outlets). **Suggest `Mahender Makhijani`:** **13 hits (365d), all TRUE** (e.g. "Indian-Origin Tycoon Mahender Makhijani Arrested at California Mansion in Alleged $100 Million Bank Fraud Case - NewsGram"), 0 FALSE. ⚠️ It misses surname-only and case-caption headlines ("Security National Guaranty Inc. v. Makhijani et al. - Daily Journal"; synthetic "Makhijani fraud trial begins…"). |
| 3 | `Cantor Group V` | 0 | **13 FALSE** | ⛔ **REJECTED** | The `V` is dropped (1 character), so the phrase is `cantor`+`group`. FALSE: **"US drug lobby group names former House leader Cantor as CEO - reuters.com"**; **"Cantor Fitzgerald raises Porch Group stock price target on growth - Investing.com"**. The press calls the entity "Cantor V" ("Cantor V founder … Mahender Makhijani accused…"), and "Cantor V" also reduces to `cantor`. **No clean wording exists. Rely on `Mahender Makhijani`.** |
| 4 | `Preferred Bank nonaccrual` | 0 | 0 / 159 | ✅ PASS | ✅ Caught "Preferred Bank moves $40 million loan to nonaccrual". ⚠️ The hyphenated "non-accrual" misses. |

**Tally (WAL, 4): 2 pass, 2 rejected** (`Makhijani`, `Cantor Group V`).

---

## REGINALD (queue row 5; claims-bar terms, proposal ②)

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Nano Banc notice to creditors` | 0 | 0 / 8 | ✅ PASS | Subsumed by `Nano Banc`. The 0 is UNINFORMATIVE: no notice has been published yet. |
| 2 | `Nano Banc claims bar date` (also DEWEY) | 0 | 0 / 8 | ✅ PASS | The matcher drops `bar` and requires `date`, so it **missed "FDIC sets deadline for claims against failed Nano Banc"**. `Nano Banc` catches that headline. The 0 is UNINFORMATIVE: REGINALD estimates the bar date at late December 2026 to early January 2027. |

**Tally (REGINALD, 2): 2 pass, 0 rejected.** Both phrases are redundant once `Nano Banc` lands.

---

## DEWEY (queue row 7; source `inbox/DEWEY/processed/2026-09-27_from-DEWEY_nano-banc-primary-documents.md`, WATCH_FOR block read)

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `purchase-assumption-agreement-nano-banc` | 0 | 0 | ✅ PASS (noise), ⚠️ **INERT** | This is a URL slug: one 39-character token that must appear verbatim in a headline. It cannot fire. Lane descriptions are empty, and URLs are not matched. **Drop it. `Nano Banc` covers the P&A posting headline.** |
| 2 | `FDIC as Receiver for Nano Banc` | — | — | ✅ PASS | Duplicate of CREED B#3. |
| 3 | `Nano Banc claims bar date` | — | — | ✅ PASS | Duplicate of REGINALD #2. |
| 4 | `Material Loss Review Nano Banc` | 0 | 0 / 103 | ✅ PASS | ✅ Caught "Fed watchdog reviews Nano Banc failure in material loss review". Subsumed by `Nano Banc`. |
| 5 | `Honarkar final award` | 0 | 0 | ✅ PASS | ✅ Synthetic caught. Subsumed by `Honarkar`. |
| 6 | `Makhijani` | — | — | ⛔ **REJECTED** | Duplicate of WAL #2. Use `Mahender Makhijani`. |

**Tally (DEWEY, 6): 5 pass (1 inert), 1 rejected** (`Makhijani`).

---

## Cross-cutting findings

1. **Outlet suffixes are match text.** About 80% of lane titles end " - Outlet", and the matcher reads that suffix. It produced one rejection (`reserve scarcity` via "The Malaysian Reserve") and propped up one pass (`MBA …` via "MBA Newslink"). Any phrase whose words could appear in an outlet name carries this risk.
2. **Dropped short words break event phrases silently.** `cut`, `bar`, `V`, `Ave` and `St` are dropped, and `below` is in the skip list. As a result, `mortgage REIT dividend cut` fires on dividend raises, `below basis` reduces to `basis`, and `Cantor Group V` reduces to `cantor group`.
3. **Substring matching cuts both ways.** It adds noise (`gated`⊂"investigated", `break`⊂"Breaking", `rate`⊂"rates"). It also loses recall wherever the inflection changes the stem (`failure`≠"fails", `suspended`≠"suspends", `delinquency`≠"delinquencies"). Hyphenation (`deed-in-lieu`, `non-traded`, `non-accrual`) and the REIT/REITs entity boundary do the same.
4. **The Nano Banc phrases can only work if a lane feed fetches Nano Banc news, and as of 9/30 none did.**
