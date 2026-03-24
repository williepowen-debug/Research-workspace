# OZK Gap Analysis Report
**Date:** 2026-03-24 | **Analyst:** Subagent (Gap Audit)
**Files Reviewed:** 33 .md files across root, research/, and sources/
**Context:** Short thesis, Aug $45 puts, earnings Apr 16

---

## EXECUTIVE SUMMARY

The folder is **strong on mechanics, weak on freshness and primary sourcing at key nodes**. Two prior audits (AUDIT_REPORT.md, AUDIT_REPORT_MAR23.md) identified many issues — some were fixed, some weren't, and new ones have emerged. The biggest meta-gap: **the folder has two audit reports but incomplete execution on their findings**, creating a false sense of completeness.

The thesis survives its own stress test (WEAKNESSES.md is excellent). But several claims still rest on secondary sources, and internal contradictions from multiple editing passes persist. With 23 days to earnings, the priority is surgical: fix what could embarrass you, pull what could surprise you.

---

## PART 1: GAPS — MISSING DATA & WEAK SPOTS

### GAP 1: Q1 2026 Real-Time CRE Market Data — STALE
- **What's missing:** Life sciences vacancy rates are undated. "35%" for Sorrento Mesa and "25-29%" for San Diego appear throughout without quarter or source. Could be Q2 2025 or older. No Q1 2026 data from CBRE/JLL/Cushman.
- **Why it matters:** If vacancy improved even 2-3 points, bulls will cite it as inflection. If it worsened, it strengthens the case. Either way, you're trading blind on the thesis's second-largest sector exposure.
- **Data source:** CBRE Q1 2026 San Diego Life Sciences Report (typically published mid-quarter), JLL Life Sciences Outlook, Cushman & Wakefield San Diego quarterly.
- **Priority:** HIGH

### GAP 2: TDR / Loan Modification Data — COMPLETELY ABSENT
- **What's missing:** Zero troubled debt restructuring or loan modification data anywhere in the folder. The 8K_FORCED_DISCLOSURE_FRAMEWORK.md explicitly flags TDR surge as the #2 leading indicator (after 30-89 day past due), yet the folder has never pulled OZK's TDR disclosures.
- **Why it matters:** Rising TDRs + flat NPLs = extend-and-pretend proof at the institution level, not just district inference. This would convert the "extend-and-pretend" narrative from inference to evidence.
- **Data source:** OZK 10-K/10-Q footnotes (ASC 326 modification disclosures), FFIEC Call Report RC-C Memo Item 1, RC-N Memo.
- **Priority:** HIGH

### GAP 3: State-Level Noncurrent Breakdowns — STILL EMPTY
- **What's missing:** EARNINGS_PREP.md's RC-C state-level table is still TBD. GAP_CLOSURE_PLAN says "not in standard call report format" but this is wrong — RC-C Part II (Schedule RC-C Memoranda) provides state-level CRE breakdowns for banks above $300M in CRE. OZK qualifies.
- **Why it matters:** The geographic thesis (OZK lends in NY/FL but is counted in Dallas) is the folder's most novel analytical contribution. Without OZK-specific state data, it's inference from district averages.
- **Data source:** FFIEC CDR bulk download, RC-C Part II Memoranda, or direct FFIEC CDR query for RSSD 107244.
- **Priority:** HIGH

### GAP 4: FHLB Borrowing Capacity & Collateral Haircuts — INCOMPLETE
- **What's missing:** D2 analysis identifies $23.9B pledged loans (74%) and $8.8B FHLB capacity, but doesn't quantify: (a) current advance rates/haircuts by collateral type, (b) what happens to capacity if CRE collateral is downgraded, (c) FHLB Dallas specific policies on construction loan eligibility.
- **Why it matters:** The tail scenario (Scenario D, 5%) depends on liquidity failing. Without FHLB mechanics, it's hand-waving. FHLB Dallas publishes its advance rates and eligible collateral schedules.
- **Data source:** FHLB Dallas member products guide (public), OZK Call Report RC-M (pledged assets detail).
- **Priority:** MEDIUM

### GAP 5: Peer ACL/NCO Ratios — ONLY TWO NAMED PEERS
- **What's missing:** Peer table has Huntington and Truist plus "regional peer avg 1.75-2.05%." No ZION, WAL, COLB, FNB, EWBC, or other CRE-heavy regionals. No quarter cited. No source.
- **Why it matters:** A PM will ask "who's in the peer group?" Two banks isn't a peer group. ZION and WAL are on the same watchlist — their ACL ratios would contextualize OZK's outlier status.
- **Data source:** FDIC API for CERTs of 5-8 CRE-heavy regionals, Q4 2025 data already available.
- **Priority:** MEDIUM

### GAP 6: Short Interest — UNDATED, UNSOURCED
- **What's missing:** "14-15% SI, 12-18 days to cover" appears in THESIS.md, SCENARIOS.md, WEAKNESSES.md with no date, no source. Short interest changes biweekly. This could be months old.
- **Why it matters:** SI is the primary risk management input for position sizing. If SI has risen to 18-20%, squeeze risk is materially higher. If it's fallen to 10%, thesis is less crowded.
- **Data source:** FINRA short interest (published twice monthly), S3 Partners, or Ortex.
- **Priority:** MEDIUM

### GAP 7: OZK's Q1 2026 8-K Activity — NO MONITORING EVIDENCE
- **What's missing:** 8K watch window opened Mar 25 per EARNINGS_PREP.md. No evidence of any EDGAR monitoring being set up or results logged. STATUS.md research agenda has "8-K EDGAR watch begins" as "Pending."
- **Why it matters:** Per the 8K_FORCED_DISCLOSURE_FRAMEWORK, the 8-K is potentially the real catalyst, not earnings day. If OZK files a mid-quarter update, the put position needs immediate attention.
- **Data source:** EDGAR full-text search, SEC RSS feed for CIK 0001609065.
- **Priority:** HIGH (time-sensitive — window is NOW)

### GAP 8: Affinius Capital $2.7B Bond Maturity Detail
- **What's missing:** EVIDENCE.md and D3 cite Affinius (most frequent OZK co-lender, 7+ deals) having "$2.7B in bonds at 81¢ with Oct 2026 deadline." No source cited. No bond CUSIP, no filing, no news article.
- **Why it matters:** If Affinius is OZK's most frequent co-lending partner and faces its own liquidity crisis in Oct 2026, that's a direct transmission channel for the Aug puts. But without a source, it's an assertion.
- **Data source:** Bloomberg terminal, TRACE bond data, Affinius Capital SEC filings or Luxembourg stock exchange filings.
- **Priority:** MEDIUM

### GAP 9: Construction Loan Interest Reserve Depletion Timeline
- **What's missing:** The interest reserve data (89.7% of $7.8B construction on reserves, $108.6M capitalized Q4) is the folder's strongest "hidden" finding. But nobody has modeled when these reserves deplete. If average reserve is 12-18 months of interest and loans are 36-42 months into their term, many should be running dry NOW.
- **Why it matters:** This is the mechanical catalyst for Wave 1-2. If you can estimate that $X billion in construction loans exhaust their interest reserves in Q1-Q2 2026, that's a quantifiable nonaccrual pipeline — far more powerful than "maturity wall forces recognition."
- **Data source:** OZK management comments (interest reserve policy), industry standard construction loan terms, back-of-envelope from RCONG376/RIADG377 quarterly trend.
- **Priority:** HIGH

### GAP 10: Dividend Sustainability — Board Composition & Precedent
- **What's missing:** D5 models the dividend math well but doesn't examine: (a) board composition and whether dividend-focused directors exist, (b) OZK's actual dividend history during prior stress (2008-2009), (c) Arkansas state banking regulations on capital distributions.
- **Why it matters:** OZK markets the 62-quarter streak aggressively. Understanding whether the board has ever cut (they didn't during GFC — Gleason grew through it) would sharpen or weaken the dividend-cut catalyst.
- **Data source:** OZK proxy statement (DEF 14A), OZK historical dividend data (IR page), Arkansas banking code.
- **Priority:** LOW

---

## PART 2: CLAIMS LACKING PRIMARY SOURCE CITATIONS

| # | Claim | Where Used | Source Status | Fix |
|---|-------|-----------|-------------|-----|
| 1 | Bioterra $203M, vacant, co-originated with Square Mile Capital Dec 2022 | EVIDENCE.md, THESIS.md | Claude deep research only — no SEC filing, no news article URL | Pull Commercial Observer article (cited as source in Claude output) |
| 2 | "DBRS: 2021-2022 vintages are 63% of CCC-C borrower pool; avg time to default 3.4 years" | THESIS.md | No link, no report name, no date | Find DBRS Morningstar report or remove |
| 3 | KBRA Negative outlook, "CRE 358%, construction 197%" | THESIS.md, EVIDENCE.md | KBRA report never accessed, not in sources/ | Obtain KBRA report or cite press coverage |
| 4 | Affinius $2.7B bonds at 81¢, Oct 2026 deadline | EVIDENCE.md, D3 | Zero sourcing | Bond data or news article needed |
| 5 | "Record RESG paydowns Q3-Q4 2025" | C2, SCENARIOS.md | Asserted without specific $ figure or source | Pull from Q3/Q4 management comments |
| 6 | Pacific Center sold "at par" | EVIDENCE.md | Management claim accepted uncritically | Cross-check Q4 charge-off data for timing |
| 7 | "$13.8B construction loans originated 2022" | THESIS.md, multiple | No primary source — appears to be from Temple 8 or industry data | Verify via FDIC API historical or H.8 data |
| 8 | OZK "largest construction lender in US that year, outpacing JPM and WFC" | THESIS.md | No source | Find the ranking — likely S&P Global or FDIC data |

**Priority:** Items 1-4 are HIGH (used in thesis-critical arguments). Items 5-8 are MEDIUM.

---

## PART 3: ESTIMATED vs. VERIFIED NUMBERS

| Number | Status | Confidence | Notes |
|--------|--------|-----------|-------|
| ACL $631.9M (total) / $475.7M (funded) | ✅ VERIFIED | HIGH | Primary from Mgmt Comments + FDIC API |
| CRE/Tier 1 358% | ✅ VERIFIED | HIGH | KBRA + multiple calculations reconcile |
| MI3 $1.289B / 37.6% | ✅ VERIFIED | HIGH | RCON2746 from FFIEC CDR |
| Noncurrent $341M / 1.07% | ✅ VERIFIED | HIGH | FDIC API CERT 110 |
| Interest reserves 89.7% / $108.6M | ✅ VERIFIED | HIGH | RCONG376/RIADG377 from FFIEC CDR |
| NDFI $2.74B | ✅ VERIFIED | HIGH | RCONJ454 from FFIEC CDR |
| Shadow CRE $1.25-1.75B | 🟡 ESTIMATED | MEDIUM | Based on CEO quote + 70-90% CRE assumption on NDFI sub-categories. Range is honest but wide. |
| Adjusted CRE/Tier 1 405-420% | 🟡 ESTIMATED | MEDIUM | Derived from verified inputs but CRE % assumptions on NDFI are judgment calls |
| IQHQ funded ~$555M, value ~$500M | 🟡 SECONDARY | MEDIUM | Bisnow (primary journalism) but not OZK filing. Cole valuation is one professor's estimate. |
| IQHQ maturity ~Aug 2028 | 🟡 INFERRED | MEDIUM | "Two-year extension" from Bisnow Oct 2024 on original Aug 2026 maturity. OZK has never disclosed. |
| $13.8B construction originated 2022 | ❌ UNVERIFIED | LOW | No primary source found in folder |
| "Largest construction lender in US" | ❌ UNVERIFIED | LOW | No ranking source |
| Bioterra $203M | 🟡 SECONDARY | MEDIUM | Claude deep research cites Commercial Observer but no URL verified |
| Bear case 50% probability | 🟡 SUBJECTIVE | N/A | Judgment — not verifiable. Well-argued but should be stress-tested against base rates for bank short theses. |

---

## PART 4: LOGICAL LEAPS & ASSUMPTIONS TO STRESS-TEST

### LEAP 1: "~46% of construction decline migrated to C&I"
The folder treats the C&I growth / construction decline correlation as proof of reclassification. But correlation ≠ causation. Construction loans completing and converting to permanent CRE (nonfarm nonresidential) is the normal life cycle. The C&I growth could be genuinely new CIB origination happening simultaneously with construction paydowns. **The MI3 data ($1.289B) proves SOME migration, but $1.289B is only ~28% of C&I growth ($2.077B), not 46%.** The other 72% of C&I growth may be genuine diversification. The "46% migration" framing overstates what the data actually shows.

**Stress test:** Compare OZK's C&I growth rate to CIB hiring data, deal announcements, and ABLG/CBSF pipeline commentary from earnings calls. If CIB is genuinely originating $1.5B+/year in new non-CRE loans, the reclassification narrative weakens.

### LEAP 2: "Interest reserves = artificiality"
89.7% of construction on interest reserves sounds alarming, but this is **standard practice** for construction lending. During construction, there IS no cash flow — the building isn't finished. Interest reserves are the expected mechanism, not evidence of manipulation. The real question is: what happens at maturity when the reserve runs out and the building hasn't stabilized? The folder correctly identifies the maturity wall but the "artificiality" framing implies something sinister about normal construction loan mechanics.

**Stress test:** What % of peer construction books use interest reserves? If industry standard is 80-90%, OZK's 89.7% is unremarkable. The thesis should focus on **what happens at maturity** (the maturity wall), not imply that interest reserves are fraudulent.

### LEAP 3: Bear case probability 50%
SCENARIOS.md assigns 50% to the bear case ($30-37). This is aggressive. Historical base rate for "concentrated CRE bank has earnings compression of 25%+" in a given year is probably 15-25%, even during stress cycles. The 50% is justified by the maturity wall and interest reserve data, but it's still a point estimate on a fundamentally uncertain outcome. **The folder would be more honest acknowledging this is a conviction-weighted probability, not a base-rate-derived one.**

### LEAP 4: "Blue Owl is an OZK exit counterparty"
EVIDENCE.md states Blue Owl took out OZK's $215M Wynwood loan and frames Blue Owl's stress (dividend suspension) as threatening OZK's exit capacity. But one deal doesn't make Blue Owl a systemic exit counterparty. **How many OZK construction loans has Blue Owl refinanced?** If it's just Wynwood, this is a data point, not a pattern.

### LEAP 5: "The healthy loans are already leaving"
C2 and SCENARIOS.md argue that record RESG paydowns mean what's left at maturity is distressed. This is plausible but unproven. **Paydowns could also reflect sponsors with healthy projects refinancing at better terms elsewhere** — not a signal that the remaining book is impaired, just that OZK is losing performing loans to competitors. The composition of remaining loans matters, and the folder doesn't have it.

---

## PART 5: INTERNAL CONTRADICTIONS STILL UNFIXED

These were flagged by AUDIT_REPORT_MAR23.md but remain in the files:

| # | Issue | Status |
|---|-------|--------|
| 1 | EARNINGS_PREP.md peer table still shows 1.16% ACL, <1.0x coverage, 455% CRE/Tier 1 | ✅ FIXED — peer table now shows corrected 1.26%, 1.39x, 358% |
| 2 | "Q4 NCO rate 1.18%" mislabeling (FY rate, not Q4) | ✅ FIXED — THESIS.md now labels as "FY2025 gross NCO rate" with Q4 quarterly (0.64%) noted separately. SCENARIOS.md updated. |
| 3 | FY2025 charge-offs: $160M (THESIS) vs $172.5M (FDIC API) | **STILL UNRECONCILED** |
| 4 | KBRA construction 197% vs FDIC-derived 142% | **STILL UNEXPLAINED** (55pt gap) |
| 5 | Life sciences "$3.2B" vs "$3.1B" inconsistency | ✅ FIXED — THESIS.md uses $3.1B (confirmed), notes $3.2B as Temple 8 rounding |
| 6 | EVIDENCE.md "Still need RCON2746" note — already pulled | ✅ FIXED — stale note removed |
| 7 | STATUS.md price "~$49" vs SCENARIOS.md "~$42-44" | **INCONSISTENT** — $7 gap |
| 8 | Dallas PDNA gap cited as OZK evidence despite methodological circularity | **STILL PRESENT** per audit E6 |

**Priority:** Items 1-2 are HIGH (would embarrass in any external use). Items 3-8 are MEDIUM.

---

## PART 6: NEW ANGLES NOT YET EXPLORED

### ANGLE 1: OZK's Loan Loss History Through Prior Cycles — GLEASON'S TRACK RECORD
**What:** The bull case centers on "Gleason has never lost." The rebuttal is "never faced this environment." But nobody has actually pulled OZK's (formerly Bank of the Ozarks) FDIC data through 2008-2012. If OZK had near-zero losses during GFC while peers were blowing up, that's a genuinely strong counter-argument that deserves quantification, not dismissal.
**Why it matters:** If Gleason navigated 2008-2012 with <20bps NCOs while running high CRE concentration, the "this time is different" argument needs to be much more specific about WHY (frozen refi + collapsed life sciences + sponsor fatigue as a unique combination).
**Data source:** FDIC API, CERT 110, 2007-2012 quarterly data. 15-minute pull.
**Priority:** HIGH — this is the single strongest bull counterargument and you're dismissing it without data.

### ANGLE 2: OZK's Specific Construction Loan Maturity Schedule
**What:** The "2022 vintage = Q1-Q3 2026 maturities" is the thesis backbone, but it's generic (36-42 month terms on 2022 originations). OZK's actual construction loan maturity schedule — how much matures each quarter — should be in the 10-K or management comments.
**Why it matters:** If $3B matures in Q2 2026 and $1B in Q3, the catalyst is front-loaded. If it's spread evenly over 18 months, the "wall" is more of a "slope."
**Data source:** OZK management comments (loan maturity tables), 10-K risk factor disclosures, or earnings call commentary on construction pipeline maturities.
**Priority:** HIGH

### ANGLE 3: FDIC Enforcement Actions / MRA History
**What:** Has OZK received any Matters Requiring Attention, formal/informal enforcement actions, or consent orders? The FDIC enforcement database is public.
**Why it matters:** If OZK is already under enhanced supervision (likely given 358% CRE/Tier 1 > 300% threshold), any escalation would be a catalyst. If they have a clean enforcement history, that's a point for the bull case.
**Data source:** FDIC enforcement actions database (public), OCC/Fed enforcement actions search.
**Priority:** MEDIUM

### ANGLE 4: Sell-Side Coverage Changes
**What:** Citi downgraded OZK to Sell in May 2024 over IQHQ. What's current coverage? How many Buys vs Sells? Any recent rating changes?
**Why it matters:** Consensus expectations set the bar for earnings surprise. If consensus is already bearish (mostly Holds/Sells), a bad quarter is partially priced. If consensus is still bullish (Buys), the repricing potential is larger.
**Data source:** Bloomberg consensus, FactSet, or free sources like TipRanks/MarketBeat.
**Priority:** MEDIUM

### ANGLE 5: Metropolitan Capital Bank Failure (Jan 30, 2026) Deep Comparison
**What:** The folder notes Metropolitan had MI3/C&I of 39.6% (vs OZK's 37.6%) but doesn't dig deeper. What were Metropolitan's other metrics at failure? CRE concentration? ACL coverage? Noncurrent rate? How close is OZK to Metropolitan's failure profile?
**Why it matters:** If OZK's metrics are within 10-20% of a bank that just failed, that's an extremely powerful comparison for any published piece.
**Data source:** FDIC failed bank data (CERT lookup for Metropolitan), FDIC loss-sharing agreement details, FDIC Material Loss Review (published within 6 months of failure).
**Priority:** MEDIUM

### ANGLE 6: OZK Stock Buyback Non-Activity
**What:** 10K_ANALYSIS_2024.md notes $200M buyback authorized July 2024, only $460K used (0.2%). Has this changed? A bank not buying its own stock at 52-week lows with $200M authorized is a powerful signal — arguably stronger than insider selling.
**Why it matters:** Management has the authority AND the capital to buy stock but chooses not to. This is the corporate-level equivalent of insiders not buying.
**Data source:** OZK Q4 2025 management comments (buyback activity), Q1 2026 8-K filings.
**Priority:** MEDIUM

---

## PART 7: PRIORITY ACTION LIST ⚠️ FROZEN AS OF MAR 24
*Live task tracking has moved to STATUS.md "Research Agenda." This list is preserved as the original audit output — do not update here.*

### MUST DO (This Week)
1. **Fix EARNINGS_PREP.md** — Replace all Temple 8 numbers with corrected figures. 10 minutes.
2. **Fix NCO rate labeling** — Global find/replace "Q4 NCO rate 1.18%" → "FY2025 annualized NCO rate." 15 minutes.
3. **Set up 8-K EDGAR monitoring** — SEC RSS feed or daily manual check for CIK 0001609065. 5 minutes.
4. **Pull current short interest** — FINRA or Ortex. 5 minutes.
5. **Update stock price** in STATUS.md ($49 → current). 1 minute.

### SHOULD DO (Before Apr 10)
6. **Pull OZK GFC-era FDIC data** — CERT 110, 2007-2012. Quantify Gleason's track record. 30 minutes.
7. **Model interest reserve depletion** — Estimate how many construction loans exhaust reserves by Q2 2026. 1 hour.
8. **Pull Q1 2026 life sciences vacancy** — CBRE San Diego quarterly. 30 minutes.
9. **Build proper peer comp table** — 5-8 CRE-heavy regionals, Q4 2025 FDIC data. 45 minutes.
10. **Pull TDR/modification data** from most recent OZK 10-K/Q filing. 30 minutes.

### NICE TO HAVE (If Time Permits)
11. Construction loan maturity schedule from management comments
12. Metropolitan Capital failure comparison
13. Sell-side consensus tracker
14. FHLB Dallas advance rate schedules
15. Affinius bond CUSIP and trading data
16. Source the $13.8B 2022 origination claim

---

## OVERALL ASSESSMENT

**Folder grade: B+/A-** — The analytical framework is excellent. The primary data work (FDIC API, FFIEC CDR) is strong. The weakness rebuttals (C1-C3) are genuinely thoughtful. The NDFI/shadow CRE analysis is novel and well-sourced.

**What would make it A+:**
1. Clean the contaminated files (EARNINGS_PREP.md, NCO labeling)
2. Source the 5-6 unsourced claims that appear in thesis-critical arguments
3. Pull Gleason's GFC track record (strongest bull counter-argument, currently unaddressed with data)
4. Model the interest reserve depletion timeline (converts the best finding into a quantifiable catalyst)
5. Get current life sciences vacancy and short interest data

**The thesis is sound.** The gaps are execution details, not structural flaws. But execution details matter when you're trading real money against a 14-15% SI crowded short with 23 days to a binary catalyst.

---

*This report should be re-run after the MUST DO items are complete to verify cleanup.*
