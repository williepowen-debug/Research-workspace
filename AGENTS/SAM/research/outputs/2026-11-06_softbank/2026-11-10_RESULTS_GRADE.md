# SoftBank Q2 FY2026 results: graded against the 11/9 lookup

**Read:** 2026-11-10 10:04–10:11 ET (clock). The scheduled 02:47 ET pass fired at 10:04 ET, most likely because the laptop slept; the results had been out since 01:30 ET. **Owner:** SAM. $0. **Rules:** `2026-11-10_RESULTS_LOOKUP.md`, committed 11/9 before the print, applied as written (not re-tuned).

**Sources read at the primary (SBG IR, downloaded 11/10 ~10:05 ET, SHA-256 prefix):** earnings presentation `earnings-presentation_q2fy2026_01_en.pdf` (1e69c9ec) · investor briefing incl. Finance section `investor-presentation_q2fy2026_01_en.pdf` (a9c2649e) · SVF deck `investor-svf_q2fy2026_01_en.pdf` (19f59e21) · data sheet `earnings-datasheet_q2fy2026_02.pdf` (87990f8b) · financial report `financial-report_q2fy2026_01_en.pdf` (c3fa95f8). No separate finance deck this quarter (the Q1-style `investor-finance_` URL returns 404); the Finance section is inside the investor briefing. **Briefing transcript not yet published; one news search found no coverage of Gotō's remarks.**

## Grade: ✅ ESTIMATE CONFIRMED

| | Value | Basis |
|---|---|---|
| **SoftBank's reported LTV, 9/30** | **15.9%** = net debt **¥11.30T** ÷ equity value of holdings **¥71.14T** | Data sheet p.17; Finance 38/41. FX ¥157.35 |
| SoftBank's basis rolled to the read (Arm **$183.26**, vendor intraday 10:06 ET 11/10; USD/JPY 158.63) | **22.5%** (12.89 / 57.15) | `ltv_lookup.py --nd 11.30 --v 71.14 --arm 183.26 --fx 158.63 --svf2-inside` |
| My A figure at the same Arm price | **21.6%** (C 23.6%) | `ltv_lookup.py --nd 11.10 --v 72.86 --arm 183.26 --fx 158.63` |
| **Difference** | **+0.9 points**, inside ±1.5 | ✅ CONFIRMED |
| Quick-read check (headline only) | 15.9% sits inside the 14.0–16.5% confirm band | agrees; superseded by the calculator row above |
| At the lookup's reference price (Arm $187.71, fx 158.0) | SoftBank basis 22.3% vs my A 21.3%: +1.0 | same grade |
| **Arm price where SoftBank's own basis reaches 25%** | **$145** (35%: $44) | Arm $183.26 is 26% above |

**Not ≥25%: no over-ceiling packet is triggered.** The confirm is on the total, and the parts were both off and partly offsetting (below).

### What the model got wrong inside a confirmed total

| Input | My model (9/30) | Reported | Read |
|---|---|---|---|
| SVF2 $10B loan | Probably **outside** the ratio (KB-SAM-261 Notes) | **INSIDE**: definition item (j) "Inclusion of the outstanding balance of the loan using OpenAI shares held by SVF2 and guaranteed by SBG"; financing slide "Treated as SBG debt in the LTV calculation" | **Wrong.** View C's structure is SoftBank's own. Per the lookup, "A was the kind one" on structure |
| Net debt | 11.10 (A, ex-loan) / 12.69 (C, with loan) | **11.30** with the loan | My non-SVF2 net debt was about ¥1.4T too high |
| Equity value | 72.86 (A) / 74.45 (C) | **71.14** | About ¥3.3T too high on the C basis |
| Headline 9/30 | 15.2% (outside) / **17.0% (inside)** | **15.9%** | The correct-structure model (17.0%) was 1.1 points high |

Both input gaps are consistent with what the model said it could not see ("SVF and Others held at 6/30 except FX; monetizations unknown"): Q2 asset monetization (−2.1 points of LTV per SoftBank's Q2 bridge) and SVF distributions (−0.7) cut debt and value together. That reading is consistent with the bridge, not proven item by item.

## The four lookup figures

| # | Figure | Read |
|---|---|---|
| 1 | 9/30 LTV, net debt, value | **15.9% · ¥11.30T · ¥71.14T** (above). Net debt = consolidated 25.04 − self-financing entities 6.48 − other adjustments 7.25 (asset-backed +6.49, hybrid +0.76). Value: Arm 38.16 (42.06 gross − 3.90 margin loan), SBKK 3.42, T-Mobile 0.00 (collared out), SVF1/SVF2/LatAm 3.45/20.07/0.96, others 5.07 |
| 2 | SVF2 loan inside? | **YES** (above). Financial report: outstanding **¥1,543.7B** at 9/30, guaranteed by SBG; OpenAI shares not pledged; margining provisions reference OpenAI share value; 18 institutions incl. Goldman, JPMorgan, Mizuho, Apollo, SMBC |
| 3 | OpenAI fair value at 9/30 | **Unchanged in the quarter** (SVF deck: "OpenAI valuation unchanged"; "Unchanged Sep-26 Quarter Fair Value Change"). No mark-up, so none of the ~2.6-point no-cash relief. SVF2's OpenAI position as of 10/1, after the final tranche: cost **$65B**, unrealized fair value **$110B**, 1.7× |
| 4 | Pro forma / Gotō | SoftBank printed a **pro forma NAV ¥44.7T ($282B)** and equity value **¥56.0T** at **11/9 closes for Arm ($186.30), SBKK and Intel, FX 158.34, with 9/30 composition**. **It printed no pro forma LTV %**; the implied figure is **11.30 ÷ 56.0 = 20.2% (SAM arithmetic)**. ⚠️ That 20.2% **excludes the $10B October tranche** (¥1.57T at 157.35, funded 10/1, in Q3); adding it gives 22.4% at $186.30, matching my roll. **Gotō's spoken words: not read** (no transcript yet). Deck wording: "Maintain LTV below 25% in normal circumstances (upper threshold of 35% even in extraordinary circumstances)"; "Multiple LTV management measures are available": monetization, asset-backed finance, hybrid finance, adjusting investment pace. No sale of Arm, T-Mobile or SoftBank Corp announced in the deck |

**Roll cross-check:** SoftBank's pro forma equity value (¥56.0T) matches my calculator's Arm-only roll without the October tranche (¥56.03T at $186.30 / 158.34), so SBKK, Intel and FX moves since 9/30 net to about zero. ✅

## §6 read list (`SOFTBANK_FUNDING_STACK.md`)

| # | Read |
|---|---|
| 1 | 15.9% at 9/30; pro forma implied 20.2% ex-October tranche (above) |
| 2 | Inside (above) |
| 3 | SVF2 loan $10.0B raised in Q2 (¥1,573.5B at 157.35; ¥1,543.7B outstanding per the financial report). Referenced OpenAI fair value unchanged in Q2 |
| 4 | OpenAI flat at 9/30 |
| 5 | **Arm margin loan: facility $25B (+$5B, agreement Sep 2026), term 2 years with a one-year extension option, 41 institutions.** Drawn about **$24.8B** at 9/30 (the ¥3.90T asset-backed deduction at 157.35, SAM arithmetic). ⚠️ The "9/2027" maturity I carried from a relay does not match a two-year term from a Sep-2026 agreement (about 9/2028); pledged share count not read |
| 6 | **$11.9B "senior term loan borrowing"** listed under debt financing, not asset-backed, so **inside** net debt; borrower and collateral not stated. Apollo appears as a lender in the OpenAI-shares loan; no separate Apollo loan found in the deck. The 18.8% "if outside" branch is moot |
| 7 | **Cash position ¥5.0T ($32B) vs ¥1.6T of bond redemptions over the next two years** (6/30: ¥2.3T vs ¥1.5T) |
| 8 | ABB robotics: still upcoming, **$5.4B "Q3 onwards"**, about $1.8B of it from LBO finance. ⚠️ Not in my roll: if it closes debt-funded at cost, about +1.2 points on SoftBank's basis (rough SAM arithmetic; the LBO portion may sit outside) |
| 9 | Guarantees: the financial report names the SBG guarantee of the SVF2 OpenAI-shares loan. **No SBG guarantee of SB Energy obligations found** (zero "SB Energy" hits in the financial report). Deck: SBG committed $3.0B to SB Energy ($1.5B funded); the PORTS-Pike credit support is NVIDIA's. **Musk turbine claim (card 20261109-005): CORRECTED 11/10 17:20 ET, see § Correction below.** A route exists through Silver Bands 7 (SB7, a subsidiary of SBG and SVF2, "a separate entity from SB Energy"): a ¥597.2B loss on power-equipment procurement, already inside the 9/30 15.9%. The SB Energy guarantee finding stands, narrowed to SB Energy |
| 10 | $1.25T round: nothing new found in the deck. VULCAN owns terms |
| 11 | Gotō: transcript not read (above) |

**Other figures (Q2, financial report):** six-month net income attributable to owners **−¥768.0B** (prior year +¥2,924.1B); total assets ¥69.39T; equity ratio 23.6% (29.0% at 3/31). SBG 9984.T closed **¥3,872, +13.88%** on 11/10 (vendor; Tokyo close, read after it).

## Japan consequence

Unchanged. SoftBank's own basis is under its 25% normal-times ceiling at today's Arm (22.5% rolled, Arm $145 for 25%). No rating action or pulled yen retail deal read; the deck cites a **¥1T retail bond issuance record (70th domestic senior "Fukuoka SoftBank Hawks Bonds")**, which is retail demand, not withdrawal. Combo theme KB-SAM-262: no member moves the read.

## Kill-on-sight check

This write-up does not say "SoftBank reported 22%": SoftBank reported **15.9% at 9/30**; 22.5% is **SAM's roll-forward** of SoftBank's figures to Arm $183.26. "Leverage is 13%" appears only as the 6/30 print. No "$40B bridge wall" (repaid 9/15; facility terminated 9/30, deck Finance 8). The 9/30 15.9% is not presented as today's leverage.

## Correction, 2026-11-10 17:20 ET (WALTER card SIG-W-20261110-010; PROME tap 17:17 ET)

**What line 55 said:** "Musk turbine claim (card 20261109-005): no route to SoftBank's leverage found in these documents."

**Why that was wrong:** my 10:04 ET search keyed on "SB Energy" and on guarantees. It never searched for the procurement entity. The financial report I had already downloaded (same SHA c3fa95f8) carries the route under Silver Bands 7.

**Re-read:** at the primary, using the same files and SHA prefixes as above, plus the accounting deck `investor-accounting_q2fy2026_01_en.pdf` (2945557a). Page numbers are given as PDF page / printed page.

| Item | SoftBank's own text | Where |
|---|---|---|
| Q2 net loss | Net income attributable to owners **−¥1,115.3B** for Q2 alone (Q1 +¥347.3B; six months −¥768.0B) | data sheet p.2 |
| Power-equipment loss | **¥597,248M ($3.73B)**, booked in "Other gain (loss)": ¥457,030M of non-refundable advance payments written off, plus ¥140,218M for contract modifications and settlements | financial report p.7/5 and p.75/73 note 1 |
| Who and what | SB7, a subsidiary of SBG and SVF2, procuring "power generation-related equipment ... for AI data center projects in the U.S., including the PORTS-Pike Technology Campus in Pike County, Ohio". Cumulative payments FY2025 through 9/30: **¥1,500.9B ($9.48B)**. Of that, **$6.6B** is allocated to purchases still in the plan and **$2.9B** is written off | financial report p.7/5; accounting deck p.8 |
| Ohio framing | **"The loss of $3.7B is completely unrelated to PORTS-Pike"**: the written-off payments are for equipment "no longer in the revised procurement plans" | accounting deck p.8 |
| Still to pay | "Cash payments for (2) expected from Q3 onward", i.e. the ¥140.2B settlement | accounting deck p.8 |
| Rebates | Up to $2.1B over 10 years on future purchases, conditional; **not recognised as an asset** | financial report p.7/5 |
| Left on the balance sheet | Advance payments for US power-generation and AI data-center assets: **¥1,065.1B** at 9/30 (+¥386.4B in the half) | financial report p.29 |
| Intel collar | **¥321,891M derivative loss** on prepaid forwards (collars) that raised $7.35B in August against all Intel shares held, recorded "as Intel's share price increased by the second quarter-end" | financial report p.9/7 and p.13/11; deck p.15 |
| Intel shares | Q2 valuation loss **−¥270.1B**; Q1 gain +¥1,332.9B; six months **+¥1,062.8B** | deck p.14; financial report p.13/11 |

**Effect on the leverage ratio** (definition: deck p.82; SAM reading):

- **Power equipment:**
  - The 15.9% is a 9/30 figure, so it already contains the loss and the cash already paid.
  - SBG's stand-alone Q2 cash bridge shows a line, "Data center and power generation-related expenditures −¥0.4T" (deck p.79).
  - The remaining **¥140.2B** settlement is future cash. If SBG pays it from stand-alone cash, net debt goes 11.30 → 11.44, which is **about +0.2 points**: 15.9% → about 16.1%, and the roll 22.5% → about 22.8% (SAM arithmetic).
  - The rebates are not in.
  - Whether SB7's equity sits in "Others (b)" unlisted holdings is not stated. If it does, the write-down is already inside the 9/30 value.
- **Intel:**
  - Holdings value counts Intel shares "net of the settlement amount of the prepaid forward contracts" (deck p.82 item a).
  - The prepaid-forward liability is deducted from net debt (deck p.82 item i).
  - So the derivative loss is the accounting mirror of the collar and is already inside Intel's net value. **No separate LTV effect.** My roll used SoftBank's 11/9 pro forma, which includes Intel.

**Lines:**
- **Line 55: CORRECTED.**
  - A route exists, to earnings and to SBG stand-alone cash and net debt. It is already counted in the 9/30 figures, plus about 0.2 points still to come.
  - What SoftBank describes is a write-off on a revised procurement plan, not a default. The deck states the loss is unrelated to PORTS-Pike.
- **"No SBG guarantee of SB Energy found": STANDS, narrowed.**
  - It is true for SB Energy, but SB7 is a different entity.
  - No SBG guarantee of SB7's obligations was found either: the financial report's guarantee hits are the SVF2 OpenAI loan and Son-related receivables only.

**Grade: CONFIRMED is NOT touched.**
- The letter of the rule compares SoftBank's reported 9/30 LTV, rolled forward, with my estimate. The reported 15.9% is unchanged.
- Even with the ¥140.2B pending settlement added, 22.8% against my 21.6% is +1.2 points, still inside ±1.5. That is sensitivity only, not a re-grade.
