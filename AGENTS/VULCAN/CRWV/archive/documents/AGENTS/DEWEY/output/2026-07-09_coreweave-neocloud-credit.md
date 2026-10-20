# CoreWeave / neocloud AI-credit — capital structure + transmission map
**Date:** 2026-07-09 | **Mode:** Thesis | **Confidence:** High (capital structure + ratings mechanics, primary-verified) / Low (live spreads + index placement — unmeasured, see gaps)

> **Flag:** REQ-DEWEY-20260704-018 (Batch-2 prompt 18). **Freshness reframe:** prompt was anchored to the Mon-7/6 discriminator (deliver ASAP off the SIG-704-001 CoreWeave bond slide). By 7/9 the fleet reads the canary as **QUIETED since ~7/4** (digest §6: X1 closed both halves; SpaceX $25B BBB-at-BB = idiosyncratic; SHADE 7/9: "AI-HY canary quieter"). So this delivers the **durable structural map + a named tripwire for forward monitoring**, not a live-slide chase. Verdict below is on structural grounds.

## Key Finding
The neocloud debt complex is a **two-layer stack**: (1) parent-level **senior *unsecured*** HY notes (the "junk bonds" that slid) and (2) ring-fenced, non-recourse **GPU/asset-backed SPV term loans (DDTLs)** whose credit quality is driven by **take-or-pay customer contracts, not GPU collateral**. The single most important structural fact: CoreWeave's $8.5B DDTL 4.0 earned a genuine **investment-grade rating (Moody's A3 / DBRS A(low))** because rating agencies rate to *contracted cash flow* (tenant-default/re-lease stress), not GPU resale value. **The true credit tripwire is anchor-contract cancellation, not GPU prices or macro HY.** On structural evidence the June–July slide reads **IDIOSYNCRATIC, not systemic** — extreme single-name concentration (Microsoft ~67% of FY25 revenue) against a >98% take-or-pay base ($60.7B backlog) and Blackstone-concentrated (not broadly syndicated) private-credit holders. **What's NOT measured here** (and remains the live watch): current secondary spreads, the exact ICE-HY index bucket, and the operational spread level of the tripwire.

## Evidence

### 1. Capital structure — DEWEY primary pull (10-Q) + workflow deal-by-deal
**DEWEY pulled CoreWeave's full funded-debt table straight from the Q1-2026 10-Q** (accession 0001769628-26-000222, as of Mar 31 2026) [PRIMARY: SEC 10-Q]:

| Instrument | Maturity | Eff. rate* | Mar-26 $M | Dec-25 $M | Type |
|---|---|---|---|---|---|
| DDTL 1.0 | Mar 2028 | 15% | 1,438 | 1,553 | GPU/asset-backed SPV |
| DDTL 2.0 | Aug 2030 | 11% | 4,425 | 5,037 | GPU/asset-backed SPV |
| DDTL 2.1 | Mar 2031 | 9% | 3,000 | 2,741 | GPU/asset-backed SPV |
| DDTL 3.0 | Aug 2030 | 9% | 1,700 | 340 | SPV (Co.VII, OpenAI offtake) |
| DDTL 4.0 (non-recourse) | Mar 2032 | 7% | 1,260 | — | SPV (Co.VIII, IG-rated) |
| **2030 Senior Notes** | Jun 2030 | 10% | 2,000 | 2,000 | **senior UNSECURED** |
| **2031 Senior Notes** | Feb 2031 | 10% | 1,750 | 1,750 | **senior UNSECURED** |
| 2031 Convertible Sr Notes | Dec 2031 | 2% | 2,588 | 2,588 | convertible |
| Convertible Promissory Notes | Apr 2026 | 7% | 171 | 168 | convertible |
| Revolving Credit Facility | Nov 2029 | 6% | 1,500 | 1,000 | revolver |
| **TOTAL debt, net** | | | **24,859** | **21,373** | (+$3.49B/qtr) |

\* **Reconciliation note (DEWEY):** the 10-Q "rate" column is the **effective** interest rate (incl. discount/issuance amortization). The workflow's coupons from the pricing releases are the **stated** rates — and they differ: **2030 notes = 9.25% stated** (issued May 2025), **2031 notes = 9.00% stated** (upsized $250M to $1.75B, priced Jul 22 2025) [PRIMARY: SEC pricing releases]. Not a conflict — effective ≈ stated + amortization. The public HY notes total **~$6.4B issued in 2025** ($2.0B + $1.75B + $2.587B convert).

**The DDTL ladder** (workflow, primary-confirmed): each is a ring-fenced bankruptcy-remote SPV mapped to one anchor contract — DDTL 1.0 (≤$2.3B, Jul 2023), 2.0 (≤$7.6B, May 2024, Blackstone/Magnetar-led $7.5B predecessor), **3.0 ($2.6B, SOFR+4%, Co.VII, OpenAI offtake)**, **4.0 ($8.5B, Co.VIII, Meta take-or-pay MSA ~$14-19B)** [PRIMARY: SEC 8-K EX-99.1s].

### 2. GPU-collateral economics — the gap is real, but it's not the binding constraint
- **The collateral-value gap is confirmed from the 10-K:** CoreWeave depreciates technology equipment (GPUs) over a **6-year useful life** vs NVIDIA's **~18–24-month architecture cadence** (Hopper 2022 → Blackwell 2024 → Rubin 2026 — CoreWeave's *own* 10-Q flags "expected deployment of the NVIDIA Rubin platform in H2 2026") [PRIMARY: SEC 10-K/10-Q]. This is the Michael-Burry-flagged datum; the 6-year figure is factual, the *economic appropriateness* is what's debated.
- **But the rating agencies rate around it:** KBRA's Data Center ABS methodology rates to **sustainable net cash flow (KNCF)** with tenant-default / re-lease-lag / revenue-haircut stress — **not GPU residual value** [PRIMARY: KBRA methodology SFXMrrxW]. This is *why* DDTL 4.0 earned A3/A(low) despite obsolescence risk (DBRS: "no exposure to volume risk"). **Implication: the GPU gap bites mainly if the anchor contract is lost** — contract cancellation, not GPU prices, is the true structural tripwire.

### 3. Circular financing + offtake concentration — the idiosyncratic core
- **Concentration is extreme but EASING:** Microsoft was **~67% of FY2025 revenue** (no other customer ≥10%) per the 10-K; DEWEY's Q1-2026 10-Q pull shows **Customer A down to 45%** of quarterly revenue (Customer B 20%; top-2 = 65%). So single-name risk is severe but trending down as OpenAI/Meta scale in. [PRIMARY: SEC 10-K FY25 + 10-Q Q1-26]
- **Contracted durability is the offset:** committed **take-or-pay contracts = >98% of FY2025 revenue**; **RPO $60.7B (up from $15.1B YoY)**, ~5-yr weighted-avg duration; $7.5B deferred revenue [PRIMARY: 10-K/10-Q]. This is a *contracted-backlog* credit, not a demand-cyclical one — the key discriminator against a 2015-16/2020-style energy-HY bust.
- **Anchor map:** Microsoft (largest revenue) · OpenAI (DDTL 3.0 offtake) · Meta (DDTL 4.0 MSA). The Nvidia→neocloud→hyperscaler equity/vendor-financing loop was **not verified beyond the contract-type facts** — flagged open.

### 4. Who holds the paper — CORRECTION to the prompt's hypothesis
The prompt hypothesized **APO/ARES/Blue Owl** AI-credit books. The verified holder base is **Blackstone-centric, not those three:** the $7.5B May-2024 facility syndicate = **Blackstone (lead), Magnetar (co-lead), Coatue, Carlyle, CDPQ, DigitalBridge Credit, BlackRock, Eldridge, Great Elm Capital**; **DDTL 4.0 anchored by Blackstone Credit & Insurance** [PRIMARY: Blackstone press release]. **This matters for transmission:** the asset-backed paper is concentrated in Blackstone + large asset managers/a pension, *not* broadly syndicated across the BDC complex — which **narrows** the cross-cohort contagion vector (BROCK/SHADE: check Blackstone vehicles, not primarily APO/ARES/Blue Owl, for direct CoreWeave exposure).

### 5. Cohort — same template
Applied Digital (APLD) priced **$2.35B 9.25% senior *secured* notes due 2030** (97 OID, Nov 2025) via subsidiary APLD ComputeCo, first-priority liens on Compute/Guarantor assets + equity — a ring-fenced data-center financing structurally mirroring CoreWeave [PRIMARY: APLD 8-K, CIK 1144879]. **Crusoe, Lambda, Nebius (NBIS) had no verified capital-structure detail** in this pass — a gap, since a cohort tripwire needs their bonds mapped too.

## The deliverables

**(i) One-page map** — above (§1 stack table + §4 holder map + §3 anchor map).

**(ii) NAMED-cohort tripwire (operationalized structurally; spread level = open):**
Watch this specific basket for the *transmission signature* — **cohort HY spreads widen while broad CCC stays flat** (LIQUID's "BB-floor >220 while CCC flat" tell):
- **CoreWeave 9.25% Sr Notes due 2030** ($2.0B) + **9.00% Sr Notes due 2031** ($1.75B) — the public unsecured HY, the actual "canary" bonds.
- **Applied Digital 9.25% Sr Secured due 2030** ($2.35B).
- (add Nebius/Crusoe/Lambda issues once mapped — open.)
- **Fires (→ transmission) if:** this basket widens materially *while broad CCC OAS is flat/tightening* → sector-specific, not macro. **Stays idiosyncratic if:** moves track a single-name catalyst (a CoreWeave/Microsoft headline) and don't spread to APLD et al.
- **DEWEY cross-anchor (from prompt 10 today):** broad HY OAS was **267–270bps, tightening** through 7/7-8 — so any CoreWeave slide in this window was *against a calm-to-tightening broad tape* = the idiosyncratic reading, consistent with the fleet's "quieted since 7/4."

**(iii) Idiosyncratic-vs-systemic verdict: IDIOSYNCRATIC (on structural evidence), with a named systemic-tripwire.**
- *For idiosyncratic:* (a) 67%/45% single-name Microsoft concentration = name risk, not sector risk; (b) >98% take-or-pay + $60.7B RPO = contracted, not demand-cyclical; (c) DDTL SPVs rated to contract (IG A3), so macro-HY beta is muted — the tripwire is contract cancellation; (d) Blackstone-concentrated holders limit BDC-complex contagion; (e) consistent with the canary quieting since 7/4 + SpaceX-idiosyncratic read + broad HY tightening.
- *The systemic counter (what would flip it):* the 6yr-vs-2yr GPU depreciation gap is **cohort-wide**; APLD/Nebius share the ring-fenced template; **common-anchor risk** — if Microsoft/OpenAI/Meta renegotiate, *multiple* SPVs re-rate at once; and the complex's sheer scale ($25B+ CoreWeave commitments alone) means growing HY-index weight. The discriminating test is the §(ii) tripwire.

## Counter-Evidence
- **The live-slide legs are unmeasured.** No verified secondary spread, no dated slide magnitude, no ICE tech-HY bucket. The idiosyncratic verdict rests on *structure*, not on the spread tape — if the CRWV notes were in fact gapping wider with APLD in sympathy while I write this, the structural read would be too sanguine. The fleet's "quieted since 7/4" is the qualitative offset, but it's not a DEWEY-measured number.
- **"IG-rated GPU financing" is partly issuer framing.** The A3/A(low) is real and third-party (Moody's/DBRS), but it rates the *SPV secured facility*, NOT the public unsecured notes — those are the HY "junk" the prompt is about, and sit well below IG (9%+ coupons ⇒ BB/B-area, exact notch unpinned).
- **Concentration cuts both ways.** Easing (67%→45%) is favorable, but 45% single-name is still extreme; and the RPO durability *depends on* those same 2-3 mega-customers honoring take-or-pay — the concentration and the durability are the same coin.
- **6-year GPU life may genuinely overstate collateral.** If a downturn coincided with an anchor-contract loss, the re-lease stress KBRA models could clear well below book — the gap is dormant, not absent.

## Source Quality Assessment
High on capital structure, ratings mechanics, holder base, concentration (all SEC-primary + rating-agency-primary, DEWEY-pulled via UA-header curl/edgar_doc — SEC.gov 403s plain WebFetch, known blocker). Low/absent on the three transmission legs (secondary spreads, index bucketing, tripwire spread level) — these need a bond terminal (ICE/Bloomberg/TRACE), out of free reach. Cohort coverage lopsided: only CoreWeave + APLD mapped; Crusoe/Lambda/Nebius open.

## References
- CoreWeave funded-debt table, Microsoft concentration, GPU 6-yr life, RPO $60.7B — SEC 10-Q Q1-2026 (acc. 0001769628-26-000222) + 10-K FY2025 (acc. 0001769628-26-000104), DEWEY-pulled 7/9: `https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm`
- DDTL 4.0 $8.5B / A3 / A(low) — SEC 8-K EX-99.1 (acc. 0001769628-26-000129); Moody's `https://ratings.moodys.com/ratings-news/462400`
- 2030 (9.25%) / 2031 (9.00%) note pricing — SEC pricing release `https://www.sec.gov/Archives/edgar/data/1769628/000176962825000030/coreweave-pressreleasepric.htm`
- DDTL 3.0 ($2.6B, SOFR+4%, OpenAI) — SEC EX-99.1 (acc. 0001769628-25-000033)
- $7.5B syndicate (Blackstone/Magnetar/Coatue/Carlyle/CDPQ/BlackRock/Eldridge/Great Elm) — `https://www.blackstone.com/news/press/coreweave-secures-7-5-billion-debt-financing-facility-led-by-blackstone-and-magnetar/`
- KBRA Data Center ABS methodology — `https://www.kbra.com/publications/SFXMrrxW/`
- APLD $2.35B 9.25% 2030 secured — `https://ir.applieddigital.com/news-events/press-releases/detail/136/`
- Broad HY OAS cross-anchor (267-270, 7/7-8) — FRED BAMLH0A0HYM2 (DEWEY, prompt-10 pull 7/9)

## Process Report
- **Searches run:** 1 `/deep-research` workflow (109 agents; 6 angles, 26 sources, 95 claims → 25 verified 25-0; **first attempt failed on the scope agent — StructuredOutput retry cap, 0 agents done, resumed clean**) + DEWEY EDGAR primary pass (10-Q debt table, customer concentration, GPU life, subsequent events, all via edgar_doc.py UA-header).
- **What worked:** the SEC-primary lane was decisive — DEWEY's edgar_doc pull gave the exact funded-debt table + the effective-vs-stated-rate reconciliation the workflow's newswire sources couldn't. The workflow's rating-agency-methodology angle (KBRA KNCF) was the key conceptual unlock — it reframes the whole credit from "GPU collateral" to "contract cash flow," which flips the tripwire from GPU prices to contract cancellation.
- **Data gaps:** the three transmission legs (live secondary spreads + dated slide magnitude, ICE BofA tech-HY index bucket/BB-B-CCC placement, the operational tripwire spread level) — **all need a bond terminal**, none free-reachable. Crusoe/Lambda/Nebius capital structures unmapped. Nvidia equity-stake/vendor-financing loop unverified beyond contract-type. Microsoft take-or-pay cancellation *terms* not obtained.
- **Source frustrations:** SEC.gov 403s plain WebFetch throughout (known UA blocker — edgar_doc.py / UA-header curl is the workaround); TRACE/bond-level pricing is the recurring wall for any single-name HY credit question.
- **Confidence:** High on structure/ratings/holders/concentration; Low on the unmeasured transmission legs. The idiosyncratic verdict is well-supported *structurally* but is NOT corroborated by a measured spread series.
- **If I had more time/tools:** a TRACE/FINRA bond-price pull on the CRWV 2030/2031 + APLD 2030 notes to quantify the Jun–Jul slide and operationalize the tripwire spread level; map Nebius/Crusoe/Lambda debt; obtain the Microsoft MSA cancellation/renegotiation terms (the real systemic hinge).
- **Suggestions:** (1) BACKLOG — a `scripts/trace_bond.py` FINRA-TRACE helper would un-block single-name HY spread/slide questions (recurs on every credit-canary run; this is the 2nd HY-single-name gap after prompt 05's HYG-holdings). (2) LIQUID/HENRY own the live tripwire — DEWEY supplies the named basket (CRWV 9.25%-2030 / 9.00%-2031 + APLD 9.25%-2030); they watch it vs broad CCC on the terminal.
