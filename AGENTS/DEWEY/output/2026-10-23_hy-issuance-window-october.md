# Is the US high-yield issuance window shut in October 2026, and who is locked out?
**Date:** 2026-10-23 (research 15:01–15:29 ET) | **Mode:** Thesis | **Request:** Will-directed thread 1 (`inbox/2026-10-23_from-WILL_three-research-threads.md`; no WALTER REQ). Decision owners: REGINALD and LIQUID on REG-T-04; VULCAN on AI borrowers | **Confidence:** Medium that the window is narrowed and expensive, not shut. Low on the October volume figure itself: one source, read only as a snippet.

## Key Finding
**Narrowed and expensive, not shown to be shut.** The only October volume figure is Bloomberg's: about $7B month-to-date against $51B in September, read from a snippet. October 2025 also ran at less than half of a record September, so seasonality and the earnings blackout explain part of the drop. Deals that came to market in October still priced, at wide levels. **No named corporate high-yield *bond* deal was found pulled.** Named pulled or postponed corporate *loans*: AVI-SPL ($690M, dropped), Circet (€3B refinancing, Europe, postponed), and Radiology Partners (loan pulled, switched to a bond that priced the same day). The lock-out is **on price**: CCC effective yield is 17.99%, up from 16.72% on 9/30, while the single-B yield is flat at 8.19%.

## Evidence

### (1) Volume
| Measure | Value | As of | Source |
|---|---|---|---|
| US HY bond issuance, October MTD | **about $7B** | about 10/20–10/21 (exact date not visible) | [INSTITUTIONAL: Bloomberg 2026-10-21, "Junk-Bond Sales Drop Sharply…", via Advisor Perspectives, https://www.advisorperspectives.com/articles/2026/10/21/surging-yields-biggest-debt-sale-delay. **Snippet only:** the page returned HTTP 403 to the sub-agent and to DEWEY's curl] |
| US HY bond issuance, September 2026 | $51–51.7B | Sept | Bloomberg (same); September also confirmed by Fidelity/ICE per REQ-002 |
| "New supply has dried up considerably since the start of the month" | qualitative | week to 10/16 | [INSTITUTIONAL: Octus Americas LevFin Weekly 2026-10-16, https://octus.com/resources/articles/americas-leveraged-finance-weekly-ma-volta-infrastructure/]. The same edition lists Ineos Energy $700M priced at 9.125%, which contradicts its own "no new HY" line. |
| October 2025 seasonal comparison | HY issuance and loan launches "both less than half of September's levels" (Sept 2025 = $48.4B, a record for the month) | 2025-10-31 | [INSTITUTIONAL: Bloomberg Credit Daybook, https://news.bgov.com/capital-markets/credit-daybook-americas-debt-sales-set-for-quiet-end-to-month] |
| Normal October baseline | UNKNOWN | — | No sourced multi-year October series was found |

**Unresolved:** Paramount's roughly $11.4B of USD HY notes appear in Octus's 10/2 weekly (https://octus.com/resources/articles/americas-leveraged-finance-weekly-paramount-loan-issuance-rebound/). If Bloomberg booked them in October, "$7B" cannot be the full MTD figure. Which month they were booked in is UNKNOWN.

### (2) Price: who is locked out
| ICE BofA series (FRED) | 9/30 | 10/22 | Change |
|---|---|---|---|
| CCC & lower effective yield (BAMLH0A3HYCEY) | 16.72% | **17.99%** (peak 18.01% on 10/20) | +127bp |
| CCC & lower OAS (BAMLH0A3HYC) | 11.79% | 13.40% | +161bp |
| Single-B effective yield (BAMLH0A2HYBEY) | 8.21% | 8.19% | −2bp |
| HY OAS (BAMLH0A0HYM2) | 3.12% | 3.40% | +28bp |

[PRIMARY: FRED, pulled 2026-10-23 with `AGENTS/DEWEY/scripts/fred_pull.py`.] PIMCO (Sept 2026) says CCC refinancing costs could "potentially double" at index yields [INSTITUTIONAL: pimco.com, "US corporate issuers can digest higher refinancing costs"]. **DEWEY inference:** CCC issuers and AI-builder credits are shut out on price, while single-B issuers are not.

### (3) October deals
| Issuer | Instrument | Outcome | Bucket | Source |
|---|---|---|---|---|
| Radiology Partners | $485M loan add-on (Everlight acquisition) | **Pulled 10/20**, switched to HY bond, priced same day at a 9.75% coupon, ~10% yield; bond size UNKNOWN | other (healthcare) | [INSTITUTIONAL: Bloomberg 10/20 headline; NEWS: Radiology Business, snippet] |
| Volta Infrastructure | ~$5B GPU and term loans (JPM-led) | **Delayed past 10/14 deadline**, priced 10/15 at the wide end: SOFR+650, 95 OID, ~11% | **AI builder** | [INSTITUTIONAL: Octus 10/16] |
| Ineos Energy | $700M senior notes | Priced at 9.125% | other | Octus 10/16 |
| WellSky / Ensono | $1.97B / $1.4B refinancing loans | Priced | software / IT services | Octus 10/16 |
| Flow Control (Blackstone LBO), Crescent Energy, AmWINS | M&A loans | In market at 10/16 | other | Octus 10/16 |
| AVI-SPL | $690M leveraged loan | **Dropped** | other (AV/IT services) | Bloomberg 10/21 via WALTER relay |
| Circet | €3B refinancing (Europe) | **Postponed** | other | Bloomberg 10/21 via WALTER relay |

- Bloomberg (10/21): **more than $5B of US and European** debt sales put off this month, from at least seven issuers. Named: **AVI-SPL $690M leveraged loan dropped** (AV/IT services; bucket iii), Freddie Mac >$440M multifamily MBS postponed, **Circet €3B refinancing postponed** (European telecom-infrastructure services; bucket iii), and 475 Fifth Ave $175M CMBS [INSTITUTIONAL: Bloomberg via syndicated copy, as relayed in WALTER `research/2026-10-23_morning/HY_SPREAD_DEEP_DIVE.md` and SIG-W-20261023-016; DEWEY did not read the full article]. The total mixes corporate and structured deals and is not a junk-bond figure. *(A DEWEY sub-agent's read of this as "mostly mortgage/real-estate" was too strong and is withdrawn.)*
- AI-builder stress shows up in the secondary market: 3 of CoreWeave's 4 USD notes traded above 1,000bp spread on 10/14–15 [INSTITUTIONAL: Octus 10/16].

### (4) Substitution
- **Leveraged loans stayed open.** Octus (10/16) calls loan issuance "strong", led by M&A, but gives no total. September loans were about $70B (banker quoted by Octus 10/2). October CLO issuance: UNKNOWN (September $41.1B / 92 deals, per CRE Daily 10/14).
- **Private credit was not absorbing syndicated deals in Q3.** In Q3, $16.39B of direct-lending loans refinanced into syndicated loans, against $2.60B moving the other way. Q3 direct-lending volume was $49.77B, down 28% y/y [NEWS: PitchBook LCD via Reuters 10/15, relayed by M&A Alerts 10/22, https://maadvisor.com/maalerts/private-credit-under-pressure-the-refinancing-test/]. No October deal moved to private credit was found.
- **Investment grade stayed open.** Walmart and Kimberly-Clark raised about $8B on 10/19 [INSTITUTIONAL: Bloomberg via Advisor Perspectives]; Workday raised $2.5B on 10/21 [NEWS].

### (5) Maturity wall (weakest section)
| Measure | Value | Source |
|---|---|---|
| Debt rated B− and lower maturing 2028 | **$268.8B** (healthcare, high tech, media) | [PRIMARY-derived: S&P Credit Market Research, snippet; spglobal.com 403] |
| HY bonds maturing 2027 / 2028 | ~$160B / ~$229B | [UNVERIFIED: blog citing LCD; Baker McKenzie Jan 2026 gives the same $229B] |
| Loans and HY maturing 2027–29 | ~$580B loans / ~$625B HY | [INSTITUTIONAL: PitchBook LCD snippet, ~4 months old] |
| **2027 maturities of CCC issuers specifically** | **UNKNOWN** | — |

Largest named 2027 CCC wall: Optimum/CSC Holdings, about $6.2B due 2027 (about $4.1B in April) [NEWS secondary, unverified]. See the REQ-003 report.

### (6) Fund flows
Global HY bond funds: **−$1.68B** in the week to 10/21 [NEWS: Reuters/LSEG Lipper 10/23, https://1027wbow.com/2026/10/23/global-equity-funds-attract-inflows-for-a-fifth-consecutive-week/]. The "−$756.4M, 7th straight week" figure circulating is **muni** HY funds (Bond Buyer); do not relay it as corporate.

## Counter-Evidence
1. **Seasonality:** October 2025 also fell to less than half of a record September.
2. **Deals clear at a price:** Radiology Partners moved from loan to bond in one day; Volta's AI-builder loan filled at the wide end; Ineos priced.
3. **Part of the move is rates:** Janus Henderson (10/15) attributes the widening "principally" to "higher borrowing costs as central bankers have turned more hawkish" [INSTITUTIONAL]. The 10-year Treasury hit 5.365%, its highest since 2002 [NEWS: NBC]. Single-B yields are flat since 9/30. *Against this:* on 10/22 the 10-year fell below 5% while HY widened (WALTER SIG-W-20261023-016 reads it as a credit-quality repricing). Investment-grade funds are buying BB bonds at their cheapest since March [INSTITUTIONAL: Bloomberg 10/20 via Advisor Perspectives].
4. **Not checked:** whether issuance resumed in the week of 10/19–10/23. No source was found.

## Source Quality Assessment
FRED yields are primary. The volume figure is a single-source Bloomberg snippet, and the Paramount booking question could change it. Deal detail comes from Octus weekly excerpts, an institutional source with internal inconsistency. The maturity wall rests mostly on snippets. **For REG-T-04 ("issuance freeze"): the evidence supports "sharply slower and expensive at CCC". It does not establish a freeze independent of the seasonal pattern.**

## References
(accessed 2026-10-23) URLs inline. FRED: BAMLH0A3HYCEY, BAMLH0A3HYC, BAMLH0A2HYBEY, BAMLH0A0HYM2. Reproduce with `python3 AGENTS/DEWEY/scripts/fred_pull.py <ID> --start 2026-09-29 --all`.

## Process Report
**Searches run:** one Opus sub-agent, ~28 searches and 57 tool calls; DEWEY re-pulled FRED and retried the Advisor Perspectives page (403).
**Data gaps:** a second October volume source; a normal-October baseline; October loan, CLO and IG totals; CCC-specific 2027 maturities; the Radiology Partners bond size and rating; US-only HY fund flows.
**Source frustrations:** PitchBook, Bloomberg, Advisor Perspectives, S&P, CNBC and Forbes all returned 403. Octus and bgov/bloomberglaw excerpts are the best free weekly route.
**Confidence in findings:** Medium (direction); Low (volume level).
**If I had more time/tools:** a PitchBook LCD or IFR monthly tally; the full Bloomberg Daybook; the October month-end total (due about 11/2).
**Suggestions:** re-check the October total at month-end, the first week of November. That is the cheap test of whether REG-T-04's "freeze" leg is seasonal.
