# L800 second leg — Amazon print, §4b cluster grade, funding-gap AMZN row, MSFT bond flex (VULCAN, 2026-10-30)

**Written:** 2026-10-30T09:12:14-04:00 (from `date`). PROME-spawned (prome-a9) Tier-1 due-row wake, DOCKET L800. Claude Code, Opus 5.5 (claude-opus-5-5).
**Rules applied:** `workbook/EXIT_PROTOCOL.md` §4b (pre-registered 2026-09-29) and its Amazon decision table committed before the print (`reports/2026-10-29_cluster-4b_prestatement.md`, 79045befb, 13:37 ET 10/29). No new threshold, no score change.

## 1. Bottom line

- **Amazon HELD its 2026 capex guide: not a cut.** Primary: *"We continue to expect 2026 cash capital expenditures to be approximately $220 billion"* (8-K Ex 99.1). Call (T2): 2027 *"meaningfully more"*. HEARTBEAT's "not a cut" is **CONFIRMED at the primary**; "the market is punishing the spend" is **INFERRED only** (the −7.3% after-hours move is confounded with an EPS miss and the Q4 guide).
- **§4b RESOLVED: NO-VERDICT.** Confirm legs 0 (no fall on a raise, no pressure citation on the letter, no cut); falsify legs 1 (META). ⚠️ Recorded disagreement, not counted: two of four names (GOOGL −12.6% regular session 10/29, AMZN −7.3% after hours) fell hard on HELD guides that promise more spending in 2027. The letter only counts a fall on a RAISE.
- **Funding gap, AMZN row on DEWEY's method: −$65.8B** (DEWEY −$69.5B). Five-name 2026E sum **−$169.6B mixed basis** (DEWEY −$186.5B), **−$148.7B** with MSFT on the cash basis.
- **New in Amazon's 10-Q (filed 10/30): a secured supplier "Loan Facility" of up to about $80.0B** for technology-infrastructure purchases, drawable Q1 2027 to Q3 2028, five-year maturities, security interest in the purchased assets. It is absent from the Q2 10-Q. The top-rated payer tier is now adding secured vendor financing, as Oracle did. No S5 letter is met.
- **MSFT bond: priced inside talk.** $25.0B in 10 tranches, spreads +25 to +105bp (pricing term sheet, primary); 2066 tranche tightened from about +135bp guidance to +105bp; order book $100–115B (secondaries). No flex, no S5 letter.
- **Composite 15/25 UNCHANGED** (S1 3 · S2 2 · S3 3 · S4 3 · S5 4, n=2). No item forced a change.

## 2. Sources (which figure came from where)

| Tier | Document | Identifier | Retrieved | sha256 (as fetched) |
|---|---|---|---|---|
| T1 | Amazon 8-K Ex 99.1 press release, 10/29 | acc 0001018724-26-000038, `amzn-20260930xex991.htm` | 2026-10-30 09:06 ET, EDGAR | 7db2112f3b602c5b9ed3886a1811b30e2fe690963f8c9feba6f880fbcf33a68f |
| T1 | Amazon 10-Q, period 2026-09-30, filed 10/30 | acc 0001018724-26-000040, `amzn-20260930.htm` | 2026-10-30 09:06 ET, EDGAR | afc3cdee607acebee88eb26dbeaa5879f53f1471dcb5b93662df05bf25454da4 |
| T1 | Amazon 10-Q Q2 (control for "new" claims) | acc 0001018724-26-000026 | 2026-10-30, EDGAR | not retained |
| T1 | Microsoft pricing term sheet (FWP), 10/29 | acc 0001193125-26-439794, `d799291dfwp.htm` | 2026-10-30, EDGAR | 16432ae8f964a29e9276209f3084e622ef24a4a7f8f09f83d2ef812b4226d943 |
| T2 | Amazon Q3 call transcripts | Investing.com and TradingKey (two transcripts agree on every quote used) | 2026-10-30 | — |
| T2 | MSFT price guidance and order book | 24/7 Wall St., Seoul Economic Daily, BigGo relays of Bloomberg/Reuters (via web search) | 2026-10-30 | — |
| Vendor | AMZN after hours and premarket | yfinance 5-minute bars, prepost; regular close from `FORGE/tools/market-data/fetch.py` | 2026-10-30 09:10 ET | — |

DEWEY's AMZN XBRL packets are not yet run. Every Amazon figure below is read off the 8-K or 10-Q text, not XBRL. The 10-Q **is now filed**: DEWEY can run its packets against acc 0001018724-26-000040.

## 3. Amazon: classification on VULCAN's letter

| Item | Value | Source |
|---|---|---|
| 2026 cash capex guide | ≈ $220B, "continue to expect" ⇒ **HELD** (raised to $220B on the Q2 call in July) | T1 8-K; July level per DEWEY base 220,000 and Q2-call relays |
| Q3 cash capex | $75.878B = purchases of property and equipment $77.259B − proceeds and incentives $1.381B ("$75.9B", Olsavsky) | T1 8-K cash-flow statement; T2 call |
| 9M 2026 cash capex | $172.188B (175.670 − 3.482) | T1 |
| Implied Q4 2026 at the held guide | ≈ $47.8B (VULCAN arithmetic) vs Q3 $75.9B, and vs Q4 2025 ≈ $38.5B (TTM Q4'25 $128.320B − 9M'25 $89.851B) | T1 inputs; arithmetic INFERRED |
| 2026 vs 2025 | ≈ $220B vs $128.3B ⇒ **+71% YoY**; no YoY cut | T1 |
| 2027 | Jassy: "expect to spend meaningfully more in 2027" | T2 (two transcripts) |
| FCF | **−$42.357B TTM** (vs +$14.788B a year earlier). ⚠️ The carrier headline "negative free cash flow of $42.4 billion" is TRAILING TWELVE MONTHS, not a 2026 or Q3 figure | T1 8-K supplemental |
| OCF | Q3 $42.422B; 9M $113.841B; TTM $168.300B | T1 |
| AWS | $46.0B, +39%; op income $17.8B; company op margin 13.9% | T1 |
| Reaction | Close 10/29 $243.79 (fetch.py). After hours last bar 19:55 ET $225.99 (**−7.30%**), low $214.01. Premarket 10/30 09:10 ET $226.55 (−7.07%) | vendor yfinance; fetch.py |

**Class: HELD — not a cut, not funding-forced, not supply-timing.** The low implied Q4 is the arithmetic of a held full-year figure after a heavy Q3. Management did not describe it as a slowdown, so its reading as timing is INFERRED.

**Pressure language versus the §4b letter ("management cites inference-price / open-weight / ROI pressure"):**

| Quote (T2, both transcripts) | Speaker | Letter met? |
|---|---|---|
| "the outsized growth of AI puts margin pressure on the business as a whole because the margins are lower there" | Olsavsky | **No, near miss.** This is margin MIX pressure, not inference PRICE, open-weight or ROI pressure. Same treatment as Alphabet's "pressure on free cash flows" on 10/29 |
| "There are also headwinds from component pricing" · "heightened component costs like memory" | Olsavsky · Jassy | No. This is supply-side cost, S2 cost-push into S1 |
| "the cost of inference over the last couple of years… I think it will come down meaningfully more" | Jassy | No. Cost-down claimed as an advantage. Relevant to PROME's disinflationary falsifier (§8) |
| "We continue to accelerate our CapEx payback" · "with strong return on invested capital" · "we can fund this plan" | Jassy | No. ROI asserted positive |
| "the Western world is very hungry for additional open models"; "6 to 8 models that are about as good as each other" | Jassy | No. Commoditisation named as a product route, not as a price pressure on Amazon |

## 4. §4b cluster grade — RESOLVED 2026-10-30: NO-VERDICT

| Name | Capex direction | Reaction graded (after hours) | Pressure citation on the letter | Leg |
|---|---|---|---|---|
| META 10/21 | RAISE (low end +$5B to $135–145B) | +2.1% | none | **RAISE and REWARDED** |
| MSFT 10/28 | TRIM to ≈ $170B calendar 2026 (supply timing), up YoY | not measured; regular 10/29 −0.16% close | none | neither |
| GOOGL 10/28 | HELD $195–205B; 2027 "increase significantly" | ≈ −10% (T2); regular 10/29 −12.64% close | none (FCF pressure only) | neither |
| AMZN 10/29 | HELD ≈ $220B; 2027 "meaningfully more" | −7.30% (19:55 ET, vendor) | none (margin-mix near miss) | neither |

Confirm legs: falls-on-a-raise **0** (need ≥2), pressure citations **0**, cuts **0**. Falsify legs: raised-and-rewarded **1** (need ≥2). **⇒ NO-VERDICT, recorded as such (the rule's "Neither" row).**

⚠️ **Recorded disagreement (for the record and the successor rule, not a regrade):** the July cluster rewarded raises (§5 steelman, MSFT +8.88%, AMZN +7%). The October cluster punished two HELD guides with promised 2027 increases (GOOGL −12.6%, AMZN −7.3%) while META's raise was rewarded only after hours (−7.13% next regular session). That is the returns-case concern in spirit and is the most informative fact in the cluster. The letter, registered before the outcome, does not count it, and this desk does not move the letter after seeing the data. A successor rule that counts "falls on a held-or-raised guide" is written in EXIT_PROTOCOL §4c as a **PROPOSAL only**. It is not adopted and needs PROME/Will's word because it changes a gate letter.

**Thermometer caveat (mechanism vs thermometer):** both falls coincide with other news: Alphabet's revenue miss (T2 Reuters headline per PROME's 10/29 packet) and Amazon's EPS of $1.89, which carriers call a miss on lower non-operating gains (T1: Q3 2025 had $9.5B of Anthropic pre-tax gains). The moves are not clean reads of the capex-return question.

## 5. L800 funding gap — AMZN row on DEWEY's method

Command: `python3 -I reports/2026-10-29_L800_amzn-update/recut.py 113841 168300 220000 1296 433 0 0` (output saved beside this report as `recut_run_2026-10-30.txt`; the control replays DEWEY's −186,456 exactly). Inputs: OCF 9M $113.841B and TTM $168.300B, finance-lease principal 9M $1.296B and Q3 $0.433B (T1 8-K cash-flow statement); capex $220B (T1 guide); payouts 0 (no dividends or buybacks).

| Name | 2026E gap $B (VULCAN on DEWEY's method) | DEWEY 10/22 | Basis note |
|---|---:|---:|---|
| MSFT | −5.9 headline / **+14.9 cash** | −26.8 / −5.8 | CY2026 ≈ $170B (KB-331) |
| GOOGL | −42.1 | −34.4 | KB-331 |
| **AMZN** | **−65.8** | −69.5 | Q3 actuals: OCF 9M + Q4 at TTM/4 ($42.1B), FL principal 9M + Q4 at Q3 rate |
| META | −15.3 | −15.3 | unchanged (no new print) |
| ORCL | −40.5 | −40.5 | unchanged |
| **Sum** | **−169.6 mixed / −148.7 MSFT cash basis** | −186.5 | |

⚠️ **What the method leaves out, material for Amazon:** "acquisitions, net of cash acquired, non-marketable investments, and other" was **$63.753B in 9M 2026** ($23.986B in Q3; T1). That line includes Amazon's lab investments (10-Q: $5.0B Anthropic Series G in Q2; OpenAI investments). DEWEY's gap excludes it by construction. On a total-cash-need basis, Amazon's 2026 shortfall is materially wider than −$65.8B. Not sized: the Q4 run-rate of that line is unknown.

**How Amazon is filling it (T1 10-Q unless noted):** long-term debt proceeds **$115.1B in 9M 2026** ($48.1B in Q3); long-term debt on the balance sheet $65.6B → **$173.1B** since 12/31; $162.5B of senior notes outstanding; **$17.5B Term Loan** (signed June, drawn September 2026, matures September 2029, SOFR + 0.625–0.875%); no commercial paper or revolver drawn; **new secured supplier Loan Facility up to about $80.0B** (Q1 2027–Q3 2028 draws, five-year maturities, security interest in purchased assets, size "subject to variability based on the extent and timing of purchase orders and pricing terms"). Commitments total $883.6B, of which leases not yet commenced $164.9B and property and equipment $159.6B. Property and equipment acquired but not yet paid rose $21.5B in 9M. Up to $20.0B Anthropic financing facility (Q2, milestone-gated, nothing drawable at inception).

**Funding-forced cut? NO.** Amazon held 2026, guided 2027 up, says "we can fund this plan" (T2), and has already borrowed more in 9M ($115.1B) than its full-year gap on DEWEY's method.

## 6. MSFT bond — pricing flex check (owed from 10/29)

| Item | Value | Source |
|---|---|---|
| Size | $25.0B: FRN 2028 $1.0B (SOFR+35), FRN 2029 $1.0B (SOFR+53); fixed 2028 $2.0B, 2029 $3.25B, 2031 $3.25B, 2033 $2.5B, 2036 $4.0B, 2046 $2.0B, 2056 $4.0B, 2066 $2.0B | T1 FWP |
| Spreads to Treasuries | +25 / +35 / +45 / +55 / +65 / +85 / +95 / +105bp (2028 → 2066); 2066 yield 6.356% | T1 FWP |
| Ratings | Aaa / AAA stable | T1 FWP |
| Guidance → pricing | 2066 guidance "up to" about +135bp → priced +105bp (≈ 30bp tighter) | T2 relays |
| Book | over $100B (Reuters-attributed) to $115B (4.6x) | T2 |
| Trade / settle | 10/29 / 11/04 | T1 |

**S5 band: NOT MET.** The deal priced inside talk, so neither orange (+50–100bp flex) nor red (+150bp or pulled) applies. It counts as one more clean clearing datum for S5's channel-kill conjunct 1 only if one reads a AAA payer as "AI-infra issuer". Conjunct 1 is defined on AI-infrastructure new issues, so this desk does not count it there. Microsoft borrowed $25B while its calendar-2026 cash-basis gap is positive (+$14.9B, KB-331): it is pre-funding, not plugging a hole.

## 7. Other items graded this session

| Item | Grade | Basis |
|---|---|---|
| S2 (hynix/Samsung leg) | **Stays 2: AMBIGUOUS, as graded 10/29 [KB-326].** Samsung's full Q3 report and call were on 10/29 KST per KB-326's source and a secondary (full report "scheduled for October 29"). The DOCKET row's "Samsung 10/30 KST" label appears to be off by a day (INFERRED); nothing new from Samsung was found for 10/30. Amazon's memory-cost lines are S2 cost-push into S1 (memory costs raise capex), not a demand roll | KB-326, call transcripts T2 |
| Hubbard / Anthropic-tied DC high-yield bond, $5–7B, shelved; banks keep the $15B bridge (WALTER SIG-W-20261029-051, Bloomberg 10/28 headline, body not read) | **NOT SCORED for S5.** A shelved or postponed distribution is not a WITHDRAWN deal, under the 10/09 ruling and the AirTrunk and SB Energy precedent. No launch-versus-clear terms are on record. Weak-link instance for the developer tier (banks warehousing an undistributable AI-infra loan) | WALTER card; CLAUDE.md S5 band |
| Intel −23% after hours (SIG-W-20261029-050) | **Not read.** No VULCAN channel letter keys on Intel's print; this is not a semiconductor-earnings desk | charter |

## 8. EXIT_PROTOCOL dated rewrite (trigger fired today) — and PROME's falsifier

The rewrite trigger was "the FIRST of {§4b resolves at the cluster · 2026-11-15}". §4b resolved today (NO-VERDICT), so the rewrite is executed in `workbook/EXIT_PROTOCOL.md`:
- §4b marked **RESOLVED NO-VERDICT, SPENT**, with the disagreement recorded.
- **§4c successor flip registered** on the SAME three standing rules (no new threshold): the Q4 2026 hyperscaler cluster (late January to early February 2027), which coincides with thesis-kill leg 1 (FY27 guides, `VULCAN-10`, resolves 2027-02-15). A "falls on a held-or-raised guide" variant is written as a **PROPOSAL** needing PROME/Will's word, not as the letter.
- §2 S1/S5 channel-kill rows: S1 ALIVE (no flat-or-down stack; all four held or raised YoY). S5 ALIVE (the developer tier still does not clear cleanly: Volta S+650, Hubbard HY shelved; the payers' clean prints are not AI-infra-issuer clears).
- Thesis-kill legs: no leg completed. Leg 1 awaits FY27 guides. The 2027 directional language (GOOGL "increase significantly", AMZN "meaningfully more") points toward re-acceleration but gives no figure, so it is not gradeable.
- **PROME's disinflationary-productivity falsifier (owed since 8/21): answered in writing.** The rail cannot carry an economy-wide inflation falsifier. It has no inflation instrument, inflation sits with HENRY and the macro desks, and the Fed text's mechanism (AI productivity lowers costs economy-wide) is not observable on VULCAN's instruments. What VULCAN can carry is the firm-level analogue: **capex pays from operations.** A **proposed** (not adopted) falsifier: *the five-name funding gap on DEWEY's method closes to ≥ $0 for a calendar year while aggregate capex is held or raised* ⇒ S5's ROI leg and the S1 returns-case are falsified. Today's reading is −$169.6B. The level is new, so it waits for PROME/Will's word. Today's evidence for the counter-leg is Jassy's claim that inference cost "has come down a lot" and "will come down meaningfully more", and AWS growth of 39% with a 38.7% segment margin. That is the firm-level productivity mechanism, asserted by management (T2), not measured.

## 9. Weak-link table (L782) — delta from the 10/29 table

| # | Link | Change | Rank |
|---|---|---|---|
| 1 | Merchant developers / neoclouds | **Hubbard (Anthropic-leased, Google guarantee once operating): the $5–7B HY take-out is shelved and banks hold the bridge** (T2, NOT SCORED). Texas permit and interconnection pause until the ERCOT audit (about mid-December) is the stated cause | 1 (unchanged) |
| 10 | MSFT / GOOGL / AMZN | **AMZN adds secured supplier financing (up to ≈ $80B, 2027–28)**; MSFT $25B priced inside talk; AMZN $115.1B 9M long-term debt. Payers raise easily, and they are now also tying suppliers into secured, purchase-linked credit | 10 (unchanged) |

Read-across: unchanged in direction. The bottom tier still breaks first. The new feature is that vendor-linked secured financing now appears at the TOP tier (Amazon) as well as at Oracle. That ties supplier credit exposure to hyperscaler purchase plans. It is a BROCK/LIQUID item to price; VULCAN flags the structure.

## 10. Gaps

- The official Amazon call transcript was not read; the quotes are T2 from two agreeing transcripts.
- The Hubbard Bloomberg body was not read.
- MSFT price guidance and order book come from secondaries only (T2).
- Amazon's lab-investment run-rate for Q4 is not sized.
- The Loan Facility counterparty (the supplier) is not named in the 10-Q text read.
- Post-close Friday slots (Mag7 slot 8, GPU reading 8, S2 cadence row) are ARMED, not run: they need the 16:00 ET close.
