# Refinancing-screen follow-up — six research directions from the September Trepp series

**Opened:** 2026-09-30 evening, Will: *"Ok approved go ahead"* (on CREED's six-direction read of the Trepp 9/10 · 9/15 · 9/21 · 9/22 · 9/23 · 9/24 · 9/25 pieces; `KB-CREED-048/049/050`). **Living page.**
**Rule for every figure here:** publication date + URL + tier. A subagent's figure is a CANDIDATE until CREED re-fetches it. Samples across articles are NEVER additive. A screen is not a forecast until a base rate is attached (trap #4).
**Not done, by design:** the Trepp full-report contact form (it would hand Will's email to a vendor; not submitted without his direct instruction).

> ⛔ **STATE AT 2026-09-30 ~20:5x ET — WORK IN PROGRESS, INTERRUPTED BY A MACHINE CRASH (~19:50 ET).** Committed in this state on Will's choice (PROME recovery question, 20:5x). **What is done:** CREED read 15 Trepp posts at source (§Findings) and built the listing sweep (`scripts/trepptalk_sweep.py`). **What is NOT done:** ① the four Opus research agents (directions 1, 2+3, 4, 5+6 beyond Trepp) died in the crash and **returned nothing**; ② **no KB row** has been written from any finding below; ③ the sweep is **not wired into the boot order** (a `CLAUDE.md` edit). ⚠️ The scratchpad copies of the fetched article texts were lost in the crash: **re-fetch each article before writing a KB row from this page.** Figures below were transcribed from CREED's own read of each page, 19:46–19:50 ET.

| # | Direction | Feeds | Status |
|---|---|---|---|
| 1 | Office "current but DSCR < 1.0x" reservoir + interest reserves + watchlist share | lane 5 (modifications; 1 vector, no aggregate series) | 🟡 **Trepp office analogue FOUND** (F1, F2). Other publishers: agent died, NOT searched |
| 2 | Office lease-expiry-before-maturity timing screen (the 9/15 industrial method) | lane 8 / the mission's "lease wall"; no vector | 🟡 **LA only** (F3). National office version: NOT FOUND on TreppTalk; other publishers NOT searched |
| 3 | Office hard maturity vs extension capacity, 2026–27 | `VX-3.02`; T-02 successor question | 🟡 **Partial:** sub-1.0x office cohort by hard-maturity year (F1); industrial method read (F6); whole-office version NOT FOUND |
| 4 | Payoff-at-maturity rates by property type; base rate of DY<8% loans paying off | PREREG F2 (conduit payoff rate, snippet-tier today) | ⏳ **NOT STARTED** (agent died). Leads: Trepp "Hard Maturity Playbook" (2024–25 refi vs delinquency, form-gated), F5 |
| 5 | Opex/insurance growth by region and property type; Florida | un-owned operating-cost channel; CORAL/AEOLUS overlap | 🟡 **Florida MF insurance series FOUND** (F7); MF NOI excerpt (F8). Office by region: form-gated report only |
| 6 | Office in-place coupon by vintage vs current refi coupon | debt-service shock on the office wall | ⏳ **NOT STARTED** (agent died). Indirect: F9 office LTV/origination |
| P | TreppTalk listing sweep at each spawn (process) | boot | 🟡 **BUILT, NOT WIRED** — see the script's own header for known limits |

## Findings — CREED PRIMARY-READ at trepp.com/trepptalk/<slug>, 2026-09-30 19:46–19:50 ET (re-fetch before any KB row)

**F1 · 2026-08-28 · "$10.7 Billion of Performing Office Loans With Sub-Breakeven DSCRs Reach Hard Maturity by 2029"** (`office-loans-sub-breakeven-dscrs-hard-maturity-by-2029`). Of **$97.2B** performing urban + suburban office loans, **$12.1B / 162 loans** report DSCR < 1.00x while current (median DSCR 0.67x, avg loan $74.7M). **$10.7B (88.1%) reaches HARD maturity by YE-2029.** By hard-maturity year: 2026 $2.0B (27 loans) · 2027 $2.1B (36) · **2028 $4.5B (36)** · 2029 $2.1B (39) · 2030+ $1.4B (24). Named: 280 Park Ave $1.075B (PRK 2017-280P, DSCR 0.68x, 93.5% occupied, hard maturity Sep-2028) · 555 California $1.2B (SFO 2021-555, DSCR 0.47x, hard maturity May-2028). ⇒ **This is the office "current but not covering" reservoir — direction 1 — with a maturity schedule attached.** It is a candidate aggregate series for lane 5 (`VX-8.01` has none).

**F2 · 2026-08-20 · "Two Fifths of the Performing Office Loans With Sub-Breakeven DSCRs Are on Well-Occupied Buildings"** (`two-fifths-of-the-performing-office-loans-with-sub-breakeven-dscrs-are-on-well-occupied-buildings`; the shorter slug 404s). Same $12.1B / $97.2B base. **$5.17B** is on buildings ≥ 80% occupied: $1.46B free-rent cited (280 Park = $1.075B of it) · $2.12B floating-rate · $1.59B fixed-rate, no free rent, median expense ratio 64.8%. ⇒ the sub-1.0x screen mixes tenant loss with rate and **opex** causes; ties to `KB-CREED-050`.

**F3 · 2026-08-21 · "Los Angeles Office Stress Is Concentrated in Urban Towers, but Suburban Lease Rollover Looms"** (`los-angeles-office-stress`). LA urban 73 loans $7.8B (occ 83%, DQ 6.6%, SS 19.7%, 20.4% fail ≥1 credit test) vs suburban 111 loans $3.5B (93%, 5.9%, 6.2%, 11.9%). **Suburban: $1.6B (~46%) has its largest tenant's lease expiring before loan maturity; $236M where that tenant holds > 50% of NRA (avg 89.0%).** ⇒ the industrial timing screen applied to office, **one metro only**. A cases candidate set: Wilshire Courtyard $384.3M · One California Plaza $300.0M · EY Plaza $275.0M (none in `cases/` today).

**F4 · 2026-08-04 and 2026-09-02 · monthly hard-maturity cohorts** (`august-2026-cmbs-hard-maturities`, `september-2026-cmbs-hard-maturities`). Aug $5.49B (office $1.81B, 32.86%; all delinquency in office; office SS $986.5M = 54.63% of office balance). Sep $2.74B: office $1.48B, **45.67% of office balance below 8.0% DY, 14.21% below 6.0%**, SS 36.50%; whole cohort 26.96% below 6.0% DY. ⇒ **a monthly office series exists in public posts** (`VX-3.02` cites only the 9/2 piece today).

**F5 · 2026-06-05 · "Why 'Extend and Pretend' Misreads CRE Maturity Stress"** (`why-extend-and-pretend-misreads-cre-maturity-stress`). Cites Glancy (2026, Fed): after 2022 low-DY and nonrecourse bank loans became LESS likely to be extended, and extended ones more likely to carry paydowns/recourse/higher spreads; stress-period extensions did not perform worse. Trepp: in CMBS, debt yield has become more predictive of going past maturity than DSCR. ⇒ **direct evidence against CREED's lane-5 framing "extend-and-pretend still absorbing"** — read Glancy at source before the next THESIS edit (direction 4 lead).

**F6 · 2026-09-18 · "The Industrial Hard Maturity Mirage"** (`industrial-hard-maturity-mirage`). Of $47.76B industrial stated maturities 2026–28, only $6.90B (14.4%) is hard by YE-2028; $40.86B can extend to 2029–31 (median DSCR 1.13x, all floating). Method template for direction 3.

**F7 · 2026-08-27 · "Florida Multifamily Insurance Costs Reverse Course"** (`florida-multifamily-insurance-costs`). Median YoY MF insurance cost change, Florida vs rest of nation: 2023 **42.1% vs 16.0%** · 2024 7.7% vs 11.1% · 2025 **−6.2% vs +3.4%**. ⇒ Florida datum: **CORAL/HOMER's lane, not CREED's** — route via WALTER, no CREED KB row.

**F8 · 2026-08-25 · "Multifamily NOI Growth Weakened in 2025"** (`multifamily-noi-growth-weakened-in-2025`, excerpt). 2025 medians: opex 3.7% (from 5.1%), insurance 2.7% (from 10.9%), revenue 2.8%, NOI 1.8%; 2021–25 implied: opex 32.4%, revenue 26.6%, NOI 21.9%, insurance 57.9%; metro NOI 3.4% SF to 33.9% Miami. HOMER's lane.

**F9 · 2026-08-17 / 2026-09-03 · office origination** (`office-loan-ltvs-recover`; `large-new-york-loans-are-driving-2026-office-cmbs-origination-volume-and-carrying-lower-debt-yields`). Conduit office median LTV 59.1% (2026 thru Jul) vs 52.7% (2023), 64.1% (2019). 2026 private-label office originated $18.3B thru 8/4, $15.6B SASB; 14 NY SASB loans = 60%. ⇒ the refi window for office is reopening for large NY assets; relevant to S8b/lender appetite.

**F10 · lodging, CREED's own lane (`VX-1.05`)** — 2026-09-28 "Limited-Service Hotel Loans Lead CMBS Lodging in Nonperforming Rate…" and 2026-09-30 "Hilton and Marriott Flag Over 40%…". Securitized lodging book $92.18B. Limited-service: $11.58B, NP rate 10.34% (full-service 5.86%, extended-stay 3.89%); 19.9% below 8.0% DY (sector 16.4%); **the only segment whose hard maturities through 2028 ($5.43B) exceed its stated ($5.16B)** — no extension capacity. Hilton NP 11.73% vs Marriott 7.23%, driven by full-service (Palmer House Hilton $328.9M in foreclosure). ⚠️ "Nonperforming" is not Trepp's headline DQ basis — do not compare with `VX-1.05` 5.84% without naming both bases.

**Also read, context only:** "The 30% Signal" (6/25, excerpt; acquisition share of issuance as a bubble indicator, office now single digits) · "The 2025 CMBS Reappraisal Cohort" (5/14, excerpt; $23B at median −53%; urban office −64%, suburban −52%; 2017–18 office vintages −71%/−67%) · "Office Deals Led CMBS Growth Through July 2026" (8/11) · TPPI Q1 2026 (6/11; office VW −13.80% vs June 2022 — a free substitute candidate for the `VX-9.02` CPPI GAP, quarterly).

## 2026-10-01 session (Will: "Start the refi-screen follow-up") — re-fetch + Glancy read

**F1 RE-FETCHED 2026-10-01 ~14:0x ET, PRIMARY-READ, matches the 9/30 transcription exactly** (Trepp, Thomas Taylor, 2026-08-28, https://www.trepp.com/trepptalk/office-loans-sub-breakeven-dscrs-hard-maturity-by-2029): $12.1B / 162 performing urban+suburban office loans with DSCR < 1.00x, of $97.2B performing; median DSCR 0.67x; avg $74.7M; hard maturity 2026 $2.0B (27) · 2027 $2.1B (36) · 2028 $4.5B (36) · 2029 $2.1B (39) · 2030+ $1.4B (24); 88.1% by YE-2029. Split loans combined by TreppREAL ID. "As of August 2026." F2 and F5 re-fetched the same session (200, text saved to scratch).

**F5's source READ: Glancy, D. (2026), "Pretend or Amend? On Evergreening in CRE," FEDS 2026-025, Federal Reserve Board, May 4, 2026** (https://www.federalreserve.gov/econres/feds/files/2026025pap.pdf, PRIMARY-READ).
| Item | Finding (page text) |
|---|---|
| Data | FR Y-14Q Schedule H.2: non-owner-occupied CRE loans > $1M at banks **> $100B in assets**; 2016Q1–2025Q4 |
| Extension volume | 2023–25: banks extended roughly half of maturing loans; similar share pre-COVID, more at the pandemic's onset. Extensions are "a persistent feature," not a stress response |
| By risk | After 2022, low-debt-yield loans ~7pp LESS likely to be extended; nonrecourse ~5pp less. Terms tightened (paydowns, guarantees, spreads), most for office |
| Performance | Stress-era extensions performed slightly BETTER than pre-pandemic ones |
| ⭐ Office payoff at maturity | **"Only about 20% of office loan balances paid off during the period of stress, compared to over 40% before the pandemic"**, mostly **higher default, not more extensions** (a direction-4 data point: bank office payoff rate) |
| The one pretend-consistent result | Large-office extension rate +3pp (statistically insignificant); non-maturing large-office extensions +1.4pp from 2023 |
| Author's own limit | "it only covers larger banks, which tend to be less exposed to CRE loans and thus perhaps have weaker extend-and-pretend incentives"; small banks covered only indirectly (Glancy & Kurtzman 2024: composition, not hiding) |

**What it does to CREED's framing (a recommendation for Will, NOT yet a THESIS edit):** the thesis list item "extend-and-pretend still absorbing — still active in banks" is **contradicted for banks > $100B** on all three of Glancy's tests. It is **not tested** for the regional and community banks where CRE concentration sits (the `CREED-T-03` scope limit again). The CMBS side is Trepp's "maturity drag", a different mechanism. A defensible rewording: *"maturities are being absorbed by negotiated extensions with tighter terms at large banks (Glancy 2026) and by slow CMBS resolution; loss deferral is untested at smaller banks."*

**Agents relaunched 2026-10-01 (four, Opus, background): outputs in `research/2026-10-01_refi_agents/`.** Prompts rebuilt from this page (the 9/30 prompts were not on this machine).

### Results 2026-10-01 afternoon — all four agents returned; CREED re-read the load-bearing figures at source

⚠️ **Correction to the Glancy read above, same session:** the NY Fed paper the dir-1 agent surfaced, **Crosignani & Prazad, "Extend-and-Pretend in the U.S. CRE Market," SR 1130, rev. June 2026** (PRIMARY-READ, abstract + introduction), uses the **same Y-14 data** and finds that **weakly capitalized banks DID extend distressed CRE loans and grant payment relief to preserve capital**, piling up a near-term maturity wall at those banks. Glancy tests the average large bank; C&P the weak-capital tail (Glancy says his patterns hold there too). ⇒ **At large banks the claim is CONTESTED, not refuted; at small banks it is untested.** `KB-CREED-053`.

| # | Direction | Result | Verified by CREED at source | KB |
|---|---|---|---|---|
| 1 | Office current-but-sub-1.0x reservoir | **No other publisher reports it**; Trepp's $12.1B stands alone. CRED iQ measures the conversion instead: 51% of office SS transfers current at transfer; 72% of 93 later failed; 71% of distressed office balance refinancing-led. Interest reserves: no aggregate (single banks only). Candidate series: FDIC `RSNRES` $10.66B Q2 (definition from a search summary; **confirm at FFIEC before adopting**) and DIY from SEC ABS-EE (conduit only, DSCR often blank) | Trepp F1 ✅ · CRED iQ 9/24 ✅ | `052`, `054` |
| 2 | National office lease-before-maturity screen | **NOT FOUND** from any publisher; LA (Trepp 8/21) is the only office version. **Buildable from SEC ABS-EE** for registered conduit deals (largest tenant, its lease expiry, maturity, DSCR, occupancy all present; SASB/CLO/bank absent) | not yet | — |
| 3 | Office hard vs stated maturity | **Not public for office.** All-types only (Trepp: 2026 $146.2B stated / $76.6B hard). Office split is inside two FORM-GATED Trepp reports (not submitted). Public hard-basis office = Trepp monthly cohorts: Apr $1.07B · May $0.74B · Jul $0.84B · Aug $1.81B · Sep $1.48B (agent) | not yet | — |
| 4 | Payoff base rate | **No public payoff rate by debt-yield bucket.** Office CMBS 2026 YTD ≈ 39–49% by balance (conduit 49% thru Jul, SASB 39% thru Aug; agent, BofA via CREFC / KBRA); bank office ≈ 20% stress vs > 40% pre-pandemic (Glancy p.25 ✅). Definitions differ by 20–40 points: **never compare across series.** For the Sept-26 office cohort's < 8% DY half, only "below the cohort rate" is sourced; the agent's ≤ 25% is an ESTIMATE | Glancy ✅; CMBS payoff rates NOT yet | in `053` (bank) |
| 5 | Opex / insurance by region | Office opex outgrew revenue in all 7 Census divisions Trepp could measure (worst East North Central, NOI −1.4%/yr; press citing Trepp, full report form-gated). Insurance cost has turned: Marsh US property rates −13% Q2-26, 8th straight fall | not yet | — (extends `050`) |
| 6 | Office coupon gap | **CRED iQ: office 5.14% → 6.86% = +172bp** (maturing Sep-26–Jun-27 vs originated May–Aug 26). Agent's own EDGAR pools: 2016 vintage 4.34% → 6.87% = +253bp (DERIVED, samples). All published coupons predate the September rate jump | CRED iQ 8/21 ✅ | `055` |

**What this does to the thesis (no score, band or trigger moved):**
- **Supports the base case's mechanism:** distress is refinancing-led (CRED iQ 71%; Trepp sub-1.0x reservoir maturing 2026–29, 2028 heaviest), and the coupon step for office (+172bp) is among the largest, before the September rate move.
- **Weakens one hypothesis wording:** "extend-and-pretend still absorbing … still active in banks" overstates what is known. ✅ **ADOPTED 2026-10-01 13:23 ET, WQ-356, Will: "approved"** (THESIS + CLAUDE.md edited; CHANGELOG 2026-10-01). Proposed wording: *"Maturities are being absorbed partly by extensions. At large banks the evidence is contested: on average terms tightened (Glancy 2026), but weakly capitalized banks extended distressed loans (Crosignani & Prazad 2026). Smaller banks are untested. In CMBS the drag is slow resolution."*
- **Base rate to attach to the office maturity screen:** ~35–50% of balance pays off near maturity in 2026 office CMBS (agent; definitions vary), ~20% at large banks (Glancy). Lower for < 8% DY: magnitude unsourced.

**Still owed (not done this session):** verify the agent's CMBS payoff rates (BofA/CREFC, KBRA) before any KB row · confirm FDIC `RSNRES` definition at FFIEC before proposing it as a lane-5 vector · decide whether to build the ABS-EE lease-before-maturity screen (engineering; Will's call) · the form-gated Trepp reports stay unsubmitted (Will's email; his call) · Florida/MF items routed to WALTER this session.


## Next session (owed, in order)
1. Re-fetch F1/F2/F4/F10 and decide KB rows (F1 is the strongest: an aggregate series for lane 5).
2. Route F7/F8 + student housing (9/21, 9/22) to WALTER for HOMER/CORAL.
3. Re-run directions 1–6 beyond Trepp (the agent prompts are in this session's transcript; re-spawn on Opus). **Already approved (line 3). The crash lost the outputs, not the approval, so this is not a Will question** (corrected 2026-09-30 21:59 ET, CATO RC5). Unfinished: the four fan-outs (1, 2+3, 4, 5+6) returned nothing; directions 4 (payoff rates) and 6 (coupon gap) have no result at all. ⚠️ That transcript is not on the laptop; rebuild the prompts from this page if needed. Sequencing: do items 1 (F1) and 4 (F5 / Glancy) first.
4. Read Glancy (2026) at source before any THESIS wording on extend-and-pretend (F5).
5. ~~Ask Will before wiring the sweep into `CLAUDE.md` boot order.~~ **Ruled 2026-10-01: not wired; it stays a manual tool (Will).** *(The sweep was repaired first, 2026-09-30 evening, CATO RC4: incomplete coverage now exits 2, dates bind per card, `--all` shows every row; saved cases `scripts/test_trepptalk_sweep.py`.)*
