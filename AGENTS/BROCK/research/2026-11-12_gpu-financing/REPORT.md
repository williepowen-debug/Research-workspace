# GPU-financing assessment — cards SIG-W-20261111-020 and -021 (D:L1098 brief addition)

**BROCK, 2026-11-12 ~16:40 ET (from `date`).** Basis: Will in PROME's chat 2026-11-11 14:02 ET via PROME packet `inbox/2026-11-11_from-PROME_gpu-financing-assessment-at-your-thursday-wake.md`. $0, no paid source. Primary reads at EDGAR (UA from `scripts/sec_contact.py`); press items are the cards' own reads, not re-opened unless stated. KB-BRK-485 to 487.

## Verdict: ONE SPECIFIC FOLLOW-UP — the view (KB-BRK-445) is otherwise intact

**Follow-up:** read Trinity Capital's (TRIN) 12/31/2026 schedule of investments in its FY2026 10-K (expected late Feb to early Mar 2027, date not verified) for its "AI Infrastructure" equipment financings: Boost Run, QumulusAI, Together Computer, Trin H OpCo I, Cirrascale. **Complete when** fair value as a share of cost for each line, non-accrual status and the sector's share of the portfolio are logged in KB. Any line under 95% of cost would be the first BDC mark on GPU-type equipment collateral in my record and feeds KB-BRK-445. Registered as a dated row in `docket/CATALYSTS.tsv`, not a monitoring job.

**Why not "changes the assessment":** nothing on the cards or at primary shows a price, spread, yield, advance rate or tenor moving against GPU lending, and the one BDC with direct GPU-type equipment collateral I found (TRIN) marked it at about par on 9/30. The OBDC link through Wingspire is small and is borrower exposure inside a diversified lender, not GPU collateral as far as anything I can read shows.

## CATO's question, in so many words

**Does the evidence show lenders withdrawing, repricing or restricting GPU financing, or only concern about depreciation? Only concern, plus one unpriced anonymous claim.**
- Concern on the record: Ares's chief executive said on the 10/29 call he does "not know how to underwrite the decline in depreciation curves" and that Ares is "for the time being" sticking to buildings and power. That is one lender describing where it already lends; the transcript gives no Ares GPU exposure and no change from a prior stance, so it is not evidence of a withdrawal.
- Unpriced claim: Semafor 11/9, one anonymous source, GPU loan portfolios "shopped at steep discounts". No price, spread or yield. It cannot grade anything.
- Korea's five big banks have no GPU-collateral product or valuation model (Seoul Economic Daily, anonymous bank positions). That is never having entered, not withdrawing.
- Against a pull-back, at the dates they carry: Wingspire 2026-1 ($407M, late September, 5x oversubscribed) and Stonebriar SCF 2026-1 ($869M, priced 10/7) placed; TRIN booked new AI-infrastructure equipment loans through 9/29/2026 (Boost Run, $69.7M, 8.7% fixed). Oversubscription is investor demand, not collateral safety; it is evidence only that the window was open.
- Not lending terms: on the Nvidia chief-executive exit (11/12) CoreWeave traded about −10% and Nebius about −16% pre-market (vendor relays, card 20261112-002). Equity moves, not loan repricing.

## Borrower exposure vs GPU-collateral exposure, deal by deal

| Deal / holder | AI or cloud BORROWER exposure | Actual GPU COLLATERAL exposure | Basis |
|---|---|---|---|
| Wingspire Equipment Finance 2026-1, $407M | Three AI or cloud obligors, about 18% of assets ≈ **$73M** (INFERRED: 18% × $407M) | **NOT ESTABLISHED.** 9fin names obligor type, not equipment type | 9fin 10/8 via card 021 (page cut off). Rule 15Ga-2 accountants' report (ABS-15G 0001193125-26-390250, filed 9/14) lists tested fields incl. "guaranteed residual value" and "unguaranteed residual value", so some contracts carry residuals; no amounts, obligors or equipment types disclosed |
| Stonebriar SCF Equipment Leasing 2026-1, $869M | Cirrascale, TensorWave, Rackspace, DigitalOcean named | Cirrascale GPU loans 5.3% ≈ **$46M**; about 15% GPU collateral overall ≈ **$130M** (one anonymous source) | 9fin via card 021. ABS-15G 0001193125-26-402967 (9/25): cut-off 8/31/2026, tested fields incl. "Residual", "Balloon amount", SIC; no amounts |
| OBDC via Wingspire Capital Holdings LLC | Equity in Wingspire: cost **$504.6M**, FV **$606.2M** at 9/30 = **8.6% of OBDC net assets** ($7,014.9M; BROCK computation). Q3 FV change −$5.1M; dividend income $40.0M nine months | **NOT ESTABLISHED.** OBDC describes Wingspire as an asset-based lender to middle-market borrowers, operating through Wingspire Capital LLC; the 10-Q never names Wingspire Equipment Finance or the ABS | OBDC 10-Q 0001655888-26-000069. That Wingspire Equipment Finance LLC (CIK 2033146) sits under OBDC's Wingspire is the card's framing plus the shared name: INFERRED, not read at primary |
| Trinity Capital (TRIN), direct lender | "AI Infrastructure" **6.6% of portfolio FV ($189.4M) at 9/30, from 0.9% ($22.65M) at 12/31/25**. Debt subtotal $179.0M FV = **13.5% of net assets** ($1,325.75M) | Equipment financings to GPU-cloud operators: Boost Run $67.4M FV (8.7%, booked 9/29/2026, EOT 0%), QumulusAI $45.7M (8.2–8.3%, EOT 9.5%), Together Computer $41.9M (11.0%, EOT 4.5%), Trin H OpCo I $22.2M (14.9%), Cirrascale $1.7M (10.2%, EOT 5.0%; was $17.8M at 12/31/25, amortizing). Marks ≈ 100% of cost. ⚠️ **The 10-Q never says "GPU"**: that the equipment is GPUs is my inference from the borrowers' businesses | TRIN 10-Q 0001193125-26-446245 (filed 11/4), schedule of investments |

## Who bears the credit and residual-value risk

| Structure | Credit risk (lessee/borrower default) | Residual-value risk (what the GPUs fetch) |
|---|---|---|
| Wingspire 2026-1 / Stonebriar 2026-1 | ABS noteholders by tranche, after the sponsor's retained piece and any overcollateralisation. **Tranche sizes, ratings, credit enhancement and the retained piece: NOT ESTABLISHED** (144A offering memoranda not public; 15Ga-2 reports carry none). US risk retention generally requires the sponsor to keep 5%; its form here is not established | On contracts with an unguaranteed residual, the lessor owns the residual; whether residuals are in the ABS collateral or kept by the sponsor: **NOT ESTABLISHED** |
| OBDC | Only through Wingspire's equity, i.e. whatever Wingspire retained. **Ceiling for the AI slice even at 100% retention: ~$73M = 1.0% of OBDC net assets** (INFERRED); actual retention unknown, most notes were sold | Same, through equity; NOT ESTABLISHED |
| TRIN | TRIN itself, as the lender of record (some lines pledged to its credit facility) | TRIN, through the end-of-term payments (up to 9.5% of principal) and recovery on the equipment if a borrower fails |
| KB-BRK-398 / 399 (context) | Broadcom–Anthropic SPV: Blackstone sole 2L; SpaceX: Apollo-managed lessor | Broadcom residual support equals the first-lien amount, so the 2L is residual-exposed; SpaceX residual terms not in release |

## What this does to my rows
- **KB-BRK-445 (theme):** adds TRIN as the first BDC holder of GPU-type equipment collateral I can name at primary; adds the two equipment ABS as borrower-exposure items. No score, gate, band or prediction moves.
- **OBDC read:** unchanged. Wingspire is 8.6% of OBDC net assets, but the AI-obligor slice of one ABS is at most about 1% even at full retention.
- **For TERRY (via PROME):** TRIN's AI-infrastructure book grew about 8x in nine months to 13.5% of net assets at par marks. My read: a concentration fact, not a stress signal; no mark or default yet.
