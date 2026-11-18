# REGINALD — board to date, Wed 2026-11-18 (PROME task letter, prome-6e)

**Written:** 2026-11-18, started 12:59 ET (from `date`). **Session:** Claude Code, Opus 5.5 (`claude-opus-5-5`), session id not exposed (scratchpad `1306b1db`). Launched on Will's word in PROME's chat 12:51 ET ("and spawn REGINALD."). One bounded session, zero dollars, no order; no level, gate, band or letter changed except by my own written rules.

**Boot reads (in order):** root `CLAUDE.md`, `AGENTS.md`, `USER.md` (explicit); this desk's `CLAUDE.md` (harness-injected); `STATUS.md`, `LESSONS.md`, `CALENDAR.md`, `MEMORY.md`, `ROADMAP.md` whole; inbox (4 general + 6 WALTER cards) whole; `scripts/market.py`, `vx_ladder_check.py`, both staleness lines, `boot.py` (rc 1: thresholds, insider, FLG ladder, one correction, inbox). No `AGENTS/REGINALD/AGENTS.md` exists. Peer channels (OZK, WAL): 0 entries above my last ACK. Pull withheld per the task letter (no pull until PROME's closeout ask); tree had two PROME-owned dirty paths at boot.

---

## 1. Credit: where my own lines stand (FRED first-published, read 12:55 ET)

| Series | 11/17 | 11/16 | 11/13 | 11/12 | Source |
|---|---|---|---|---|---|
| HY OAS (`BAMLH0A0HYM2`) | **343** | 334 | 323 | 320 | FRED via `fetch.py` |
| CCC OAS (`BAMLH0A3HYC`) | 1,329 | 1,310 | 1,316 | 1,314 | FRED |
| B OAS (`BAMLH0A2HYB`) | 368 | 357 | 344 | 339 | FRED |
| CCC/HY ratio | **3.87×** | 3.92× | 4.07× | 4.11× | my arithmetic |
| IG OAS (`BAMLC0A0CM`) | 92 | 90 | 89 | 89 | FRED |

FRED now also shows 330 for 11/10 and 330 for 11/11; the 11/11 bar is a Veterans Day forward-fill, excluded and bridged (`registry/NOTES.md` § REG-T-03/04).

| My line | Letter | State after 11/17 |
|---|---|---|
| `REG-T-03` HY > 320 ×3 | already CREDIT-CANARY-FIRED; exit HY ≤ 300 ×5 | **Unchanged: FIRED.** Exit run 0 (343 is 43 above 300). LIQUID's MET on its own >320 ×3 run (323/334/343, `b9720641b5`) is LIQUID's line; mine was already fired and does not re-fire. |
| `REG-T-04` HY > 350 ×3 | ISSUANCE-FREEZE | **NOT FIRED, run 0 of 3.** 343 is 7bp below. Matches LIQUID's "witness NOT FIRED". The WQ-512 single-issuer rider runs only at a fire. |
| `REG-34` (25%) | > 350 on 3 consecutive sessions, 11/05 to 12/29 | OPEN. No print above 350 yet in the window (peak 348 [11/05]). |
| `VX-REG-18.04` CCC/HY > 3.6× | HARD-FIRE; escalate only on a CCC-LED re-cross | **Still fired, NO escalation.** The ratio fell 4.07× → 3.87× because HY widened faster than CCC (11/13 → 11/17: HY +20, CCC +13): HY-led, the opposite of a CCC-led re-cross. B 368, above ORANGE 330 since 10/29 (watch row, no trigger). |

**Bank-credit cross-check (my standing rule: HY is downstream of bank credit; `reports/2026-07-30_bank-side-HY-attribution.md` §E names the flipping datum).** Window = the HY widening, closes 11/12 → 11/17 (three sessions), yfinance unadjusted closes, not cross-checked at a second vendor, ex-dividend dates NOT checked:

| Instrument | 11/12 → 11/17 | Flip datum | Met? |
|---|---|---|---|
| Bank junior-sub/preferred basket, 10 names (ZIONP, WAL-PA, OZKAP, VLYPO, VLYPP, CFG-PE, HBANL, HBANM, KEY-PI, TFC-PR) | **mean −0.88%**; 3 of 10 at or below −2% (TFC-PR −3.11%, VLYPO −2.72%, HBANM −2.52%); ZIONP +2.06% | basket falls ≥2% over 3 sessions while HY widens | **NO** |
| IG OAS | +3bp (89 → 92) | ≥ +10bp, financials leading | **NO** |
| KRE vs SPY | KRE −2.30% (72.52 → 70.85, settled, Nasdaq agrees) vs SPY −3.26% | (KRE breaking is explicitly not a flip datum) | KRE held up better than the index |
| BKLN | −0.19% | — | — |

**Read: BANK-ABSENT on the registered discriminators, weaker than on 7/30.** The 7/30 basket was flat to up; this time it slipped and three names fell more than 2%. Fixed-rate preferreds are also rate-sensitive (10Y 5.10 [11/12] → 5.12 [11/16], Treasury par via FRED; ^TNX 5.07 vendor today) and some may have gone ex-dividend in the window, so the three larger drops are not attributable to bank credit on this evidence. The HY widening came with a broad equity sell-off (SPY −3.3%), which reads as general risk-off, not as bank stress transmitting into credit.

**Tape (settled 11/17, Yahoo and Nasdaq agree):** WAL $71.47 (REG-T-02 FIRED, exit 0 of 3, 55 rows, needs +14.59% to reach $81.90); KRE $70.85 ($10.85 above the $60 line, REG-T-01 UN-FIRED); FLG $10.29 (RED, 29 closes below $11.39, −27.7% vs frozen $14.24; ladder exhausted); SBCF $32.75. 11/18 bars are intraday and not graded (WAL 71.5, KRE 71.1 at ~12:54 ET, vendor). VIX 24.03 vendor 12:54 ET. KRE shares 56.52M [11/18 monitor].

**Insider monitor (boot.py, last 14 days, SEC Form 4):** EGBN open-market buys by Stephen R. Curley (4,393 sh at $34.05, 11/12) and Eric R. Newell (1,470 sh at $33.91, 11/10), about $0.20M combined, alongside five sales by three other insiders (about $0.94M at $33.63–$34.44, 11/10–11/13). Mixed, small; logged, no consequence. FLG CEO Otting's 11/10 buy is already in ML-REG-306 (the monitor shows the 11/12 filing date). CUBI three sales 11/04.

## 2. Fed Financial Stability Report, 11/13, read at the Fed's own PDF

`federalreserve.gov/publications/files/financial-stability-report-20261113.pdf`, 4,364,069 B, sha256 `ef1c57e5…a4a912`, fetched 2026-11-18 ~12:58 ET with a plain client. My 11/17 entry (ML-REG-310) rested on BROCK's read; it now has a primary read.

| Item | What the report says | What it means for my desk |
|---|---|---|
| **Box 2.2, bank leg** | "the largest U.S. bank holding companies have close to $1 trillion of exposure to large technology firms, data center developers, advanced computing–related SPEs and private credit vehicles, and utility companies, and those exposures are evaluated during the annual supervisory stress test." | **Confirmed verbatim.** Largest BHCs only, five borrower types mixed, no regional split. GIBBS's perimeter, not my 14. |
| Box 2.2, who holds the risk | Hyperscaler and GPU on-balance-sheet debt is held mainly by mutual funds, pensions and insurers; the riskier subordinated and equity SPE tranches by HY funds, life insurers, BDCs and private debt vehicles. Advanced-computing debt issuance over $680B by Oct 2026; public debt outstanding over $1.1T; not-yet-commenced leases over $1T and guarantees and contract commitments over $2T (undiscounted; Amazon, Alphabet, Broadcom, Meta, Microsoft, Nvidia, Oracle). | The first-loss pieces sit outside banks on the Fed's account. A bank leg exists only through lending to the vehicles (the combination theme), which the Fed does not size below the largest banks. |
| **Bank fair-value losses** | AFS and HTM fair values "roughly $330 billion below their combined book value in the second quarter of 2026", and "likely facing additional downward pressure" as yields rose through late October. | ★ **Independent check on my own measure:** my Q2 system figure on the Call Report was $324.7B, within 2% of the Fed's ~$330B; my Q3 figure $485.7B [9/30] is the "additional pressure" the Fed anticipated. Same basis caveat as ML-REG-307 (AFS cuts GAAP equity, HTM does not; AOCI opt-out keeps both out of regulatory capital for most banks). |
| Regional capital | Tangible common equity to tangible assets for regional banks "has been increasing since 2022 and stands near the top of its historical distribution" (Q2). | A Q2 reading, before the Q3 bond-loss widening I measured; it does not clear Q3. |
| Regional funding | Regional banks relied more on reciprocal and, to a lesser degree, brokered deposits since 2023; uninsured deposits as a share of assets back to mid-2010s levels. | Consistent with the 11/07 RCON2365 break note; no new instrument. |
| CRE | Inflation-adjusted CRE prices "fairly stable"; vacancy and rents steady; SLOOS CRE standards eased in the first two quarters. | No support for a CRE recognition wave in the Fed's aggregate; my concentrated-not-tier-wide claim is unaffected. |
| Cyber and AI agents | "recent advances in the ability of LLMs and agentic systems to detect and exploit vulnerabilities"; a cyber event could cause "erosion of investor and depositor confidence". | **WALTER card 027 item 1 ("Fed warns AI agents could trigger bank runs in minutes", Kalshi): NOT in the FSR as worded.** The nearest text is the cyber passage above; nothing about runs "in minutes". Logged under combo:bank-vendor-breaches as context. |

KB ML-REG-311 (primary read); no score moved. Correction COR-20261117-31 (card 014's weekday): NO-OP receipt, none of my surfaces carried the weekday.

## 3. Seacoast (SBCF): where the LOANS sit in the five flood counties

**Asked (PROME 11/17 22:00 ET):** share of Seacoast's loans and real-estate collateral in Brevard, Indian River, St. Lucie, Martin and Palm Beach, by loan type if given, and what the bank says about flood insurance on that collateral.

**Answer: NOT DISCLOSED at county level** in the 2025 10-K (acc 0001628280-26-012787), the Q3 2026 10-Q (acc 0001628280-26-070242) or the Q3 earnings presentation (8-K EX-99.2, acc 0001628280-26-067572). The deck's footprint map shows branches and "counties with Seacoast customers/locations", no balances.

**Closest disclosed cuts:**

| Cut | Figure | Source |
|---|---|---|
| Loan mix, whole bank, 9/30/26 ($13,574M) | Residential 24%, commercial & financial 19%, owner-occupied CRE 16%, CRE retail 11%, industrial/warehouse 7%, construction & land 7%, office 4%, multifamily 4%, hotel 2%, other CRE 5%, consumer 1% | Q3 deck slide 10 (EX-99.2) |
| CRE concentration | 227% of total risk-based capital (construction 41%), estimated | same |
| Credit, Q3 | NCO 0.16%, NPL/loans 0.54%, accruing past due 0.20%, criticized and classified 2.90%, ACL 1.41% | Q3 deck slide 12 |
| Deposits in the five counties (franchise, not loans) | $5.99B of $16.80B = **35.68%**; 10.25% without Martin and Palm Beach (106 branches) | FDIC SOD 6/30/2026, CORAL's figure **reproduced by me exactly** (api.fdic.gov, cert 131) |
| **Residential mortgage originations kept on book, by county** (Seacoast's own HMDA filing, LEI 5493006MCOP60BBI4G97) | **2025: 31.3% of $511.0M originated in the five counties** (Palm Beach 12.8%, Martin 8.2%, St. Lucie 4.9%, Brevard 2.8%, Indian River 2.6%); 10.3% without Martin and Palm Beach. 2024: 30.7% of $447.2M (same order). 97% of originated dollars kept on book (purchaser type 0). Five-county lending is all single-family; multifamily ($67.2M in 2025) sits elsewhere. | CFPB HMDA data browser API, action taken = originated, pulled 11/18 |

**What this supports:** where Seacoast lends on homes tracks where its branches are: about 31% of residential origination dollars vs 36% of deposits, and about 10% on both measures once Martin and Palm Beach are excluded. **INFERENCE, not disclosed:** the outstanding book is probably concentrated in these counties on a similar order. That rests on one loan type (24% of the book), on a flow (2024–25 originations), not the stock, and the October 2025 VBI acquisition ($1.2B of loans in The Villages, outside the five counties) dilutes the stock share. Commercial loans by county: no primary cut found.

**The county in the news is Seacoast's smallest of the five.** CORAL's flood context is the St. Johns River at major flood near Cocoa (Brevard). Brevard is 2.8% of Seacoast's 2025 residential originations and $0.38B (2.3%) of deposits. Most of the five-county weight is Palm Beach and Martin (Seacoast's home county); how badly those two were flooded is not established in anything I read (CORAL's county list, not a damage map).

**Flood insurance:** the filings say nothing specific about flood insurance on collateral. The 10-K risk factor says only that Florida markets are "susceptible to hurricanes, tropical storms and related flooding" which could cause "a decline in the value or destruction of properties securing our loans and an increase in delinquencies, foreclosures or loan losses", and that customers face "significantly higher property and casualty insurance premiums". General law, recalled and not read this session: federally regulated lenders must require flood insurance on loans secured by improved property in FEMA special flood hazard areas; flooding outside those zones is commonly uninsured, consistent with CORAL's ~16% household coverage.

**Material by my standard? No, not on present evidence.** It is a map of where exposure sits, with no loss, past-due or provision evidence attached; Seacoast's Q3 credit is clean (NCO 0.16%), and Tier 1 is 14.1% (estimated). It moves no grade, level, gate or watch-card (FL frame NO TRANSMISSION FINAL [11/06] stands). **What would change it:** a federal flood declaration with damage concentrated in Martin, Palm Beach or St. Lucie; Seacoast naming a flood or storm provision or past-due rise at its Q4 release (~late Jan 2027); residential or CRE 30–89 past dues rising at the 12/31 Call Report. Sent to TERRY anyway with that verdict (no investment implication, and why) under Will's 11/10 word; NO CARD is a complete answer.

## 4. CORAL's rating-timing correction (CATO CR17-2, CR17-3)

Accepted as written: a local downgrade is one possible observation, not "the tell", and nothing ties it to "after September 2027"; budget proposals, fee or millage votes or borrowing terms could show stress first; no default implication is established. **None of my surfaces carried the corrected line** (grep of my tree outside archive for "the tell" and "September 2027": none). No muni-exposure line of mine moves; I hold no registered muni instrument. Answer by packet to CORAL.

## 5. WALTER's companion renewal (SIG-W-20260619-008)

Renewed 11/17, review due 2027-05-17; WALTER reports `read_cap_check.py --agent REGINALD` rc 0. **L889's open leg closes.** Verified by my own closeout run (§7).

## 6. Inbox and BOARD drained

| Card | Cluster | Disposition | Why |
|---|---|---|---|
| SIG-W-20261117-026 Equinor cyber | CYBER | INFO_ONLY | Not a bank supplier; gas confidence, HANS and BRENT. |
| -027 small items | MISC | INFO_ONLY | Item 1 checked against the FSR text: NOT in it as worded (§2). |
| -029 CYPHER evening grades | CYBER | INFO_ONLY | n0n listing of JPMorgan is the gang's word; Visa says third-party APAC provider; none of my 14. |
| -031 correction of 014 (weekday) | PC_STRESS | INFO_ONLY | COR-20261117-31 NO-OP receipt. |
| -20261118-002 housing starts | BANK_COLLATERAL | INFO_ONLY | Permits −7.4%; HOMER owns; no letter of mine. |
| -20261118-005 HSBC, Associated sites | CYBER | INFO_ONLY | Probably card 008's Optimizely event (already ML-REG-309); not established; neither in my 14. |
| BOARD diff, primary clusters: -20261117-002, -003, -004, -010 (CONSUMER_STAGFLATION), -009 (PC_STRESS), -030 (BANK_COLLATERAL) | — | INFO_ONLY; -009 item 1 logged | -009: HSBC sold a ~$300M piece of a New Mexico data-center construction loan at mid-80s weeks ago (Bloomberg via Investing.com, secondary) → KB ML-REG-312, combo:bank-lending-to-private-credit. The rest touch no letter of mine (CARL, OTTO, HOMER own). |

Secondary-cluster cards (AI_INFRA_CAPEX, IRAN_HORMUZ, HYDROCARBON_INFRA, MISC) with no bank-ticker hit on my watchlist: skipped per charter step 9b. The ECB Financial Stability Review card (-20261118-003, AI_INFRA_CAPEX, HANS action) is euro-area banks; not read.

## 7. Instruction change (WQ-719 A)

Will ruled WQ-719 A at 12:10 ET; NEXUS applied it at `397f330a33`. My charter's SESSION CLOSE CHECKLIST line "**NEXUS brief is the LAST write-back**, after final STATUS and immediately before its commit; brief pin must equal current STATUS file HEAD at commit time. Re-pin after any STATUS re-commit." told me to rewrite and re-pin every session. Replaced in this session with NEXUS's wording: rewrite and commit the brief at closeout only when a figure, threshold, or cross-desk send or wait in it changed; otherwise leave it untouched, no As-of or pin refresh; a lagging pin is a warning, not a failure. The FILES line ("NEXUS_BRIEF: final full-schema fold after STATUS") is qualified the same way. **This session the brief does change** (HY 323 → 343, the cross-check, the Seacoast answer), so it is rewritten.

## 8. What moved, by my own rules

| Item | Moved? |
|---|---|
| REG-T-03 / REG-T-04 / REG-34 / CCC-HY | No state change (above). |
| REG-T-02 | One row added (11/17, $71.47), still 0 of 3. |
| FLG ladder | RED, unchanged (29 closes below). |
| Matrix scores, thresholds, gates, predictions | None moved. |
| Thesis claim | Unchanged (concentrated, with the 11/07 qualifier). |
| New evidence logged | KB ML-REG-311 (FSR primary), ML-REG-312 (HSBC loan sale, combo), ML-REG-313 (Seacoast loan geography). |

**Unknowns that matter:** flood damage by county (Martin, Palm Beach); Seacoast's commercial loans by county; whether the three preferreds that fell more than 2% went ex-dividend; H.4.1 and H.8 since 11/06 still not read this session.
