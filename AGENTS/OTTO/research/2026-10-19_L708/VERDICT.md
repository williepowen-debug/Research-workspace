# L708 — OTTO consumer-lender credit attribution: NO_INSTRUMENT

**As of:** 2026-10-19, OTTO s030. Existing Will-approved commission, fixed NEXUS §3; $0. **One-line return:** no two issuers clear the full corporate B/CCC bond × in-window ICE membership × daily-data join (strict n=0), so **H1 = NO_INSTRUMENT**; a frozen, non-qualified Enova/Carvana equity basket is **MIXED** in both windows and supplies no support for consumer-led widening. Consumer stress is not disproved.

## What NEXUS can use

1. **No lender attribution of the CCC index is established.** Historical ratings identify candidates, not October 2026 index constituents. HYG's October 14 holdings are a later snapshot of a different benchmark. No ICE constituent weights, rating composites, sector contributions or daily constituent bond/CDS panel were recovered. The formal ladder stops at rule 1; the supplemental equity calculation cannot turn that into a formal MIXED result.
2. **The obvious stressed lender is not a qualified index witness.** CRMT publicly extended covenant/liquidity relief on September 24, October 1 and October 8; no B/CCC corporate bond/index join is verified. Its warehouse agreement is not a HY corporate bond, nor are its ABS trusts. BROCK owns the grade; the seventh bridge filed October 15 is outside the measurement window.
3. **World Acceptance is a concrete stale-universe trap.** A February 2025 report gives corporate B- / unsecured CCC+, but its June 2026 10-Q Note 12 says the remaining $168.3M November-2026 notes were fully redeemed August 29, 2025. Those retired notes cannot explain the 2026 CCC move. Do not use WRLD's liquid stock to manufacture a second qualified issuer.
4. **In-window financing evidence is not uniformly adverse.** Enova closed $500.026M OnDeck ABS September 25 and extended a $200M NetCredit facility October 13; CPS disclosed October 13 a warehouse increase from $390M to $518M agreed October 9. OnDeck is small-business credit, not a household-credit release. These are funding-access observations, not proof that the whole sector is healthy.
5. **Exeter collateral weakness is dated and real, but the mechanism stays unresolved.** Four August-collection reports filed September 29 show DQ below each deal's 40% trigger; all four explicitly say no delinquency-trigger occurrence. Two report $22M combined September 15 reserve capital contributions. Those are support to ABS trusts, not corporate default, bond repricing or new fraud. Earlier panel DQ worsening coincides with fewer extensions; servicing policy versus borrower deterioration is not separated.

## Eligibility and source discipline

`issuer_coverage.tsv` is the full screened set; `filing_inventory.json` retains every returned form September 15–October 19 for eight public issuers. Public 8-Ks were read, including excluded candidates; absent 8-Ks do not establish absent events. This bounded scan is not a census of all private lenders or agency actions.

| Candidate | Dated evidence | Why it does not supply a qualified daily index observation |
|---|---|---|
| Enova (ENVA) | [S&P July 29 2024](https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3221986): proposed 2029 unsecured notes B-. June 2026 10-Q confirms outstanding 2028/2029 corporate notes | Primary publisher search extract accessible; full agency HTTP fetch 403. Historical issue rating is not a verified October 2026 rating or ICE composite. Public equity reachable; supplementary only |
| Carvana (CVNA), retail/finance boundary | [S&P March 13 2025](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101616201): issuer/secured B, unsecured CCC+. HYG October 14 holds 9% June-2031 notes | Historical primary publisher extract, full HTTP 403; neither rating history nor ICE membership at the observation dates established. Equity includes retail/loan-sale economics, not pure consumer losses; not private DriveTime equity |
| Cobra/Exeter | [S&P March 17 2026 EART presale](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101675261): Cobra Equity Holdco B-/Stable | Parent rating, EART ABS and corporate index debt are three different objects. No verified corporate bond in the target index or daily corporate price series; no listed Exeter equity |
| DriveTime/Bridgecrest | [S&P May 10 2016](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/9635349): historical B issuer/secured | Far too old to establish current tier. Private corporate equity unavailable; BLAST/DT ABS ratings cannot substitute |
| World Acceptance (WRLD) | June-2026 10-Q Note 12: full redemption of November-2026 notes in August 2025 | Excluded retired bond; February-2025 B-/CCC+ report is historical secondary context only |
| Oportun (OPRT) | March-2026 10-Q: corporate term loan; February-2026 issuer release identifies ABS funding | No verified B/CCC HY corporate bond. A rated ABS tranche is not a corporate index constituent |
| CRMT / CPS (CPSS) | SEC 8-K relief extensions / warehouse increase, detailed below | No verified qualifying corporate bond/rating/index join. Public equities alone do not cure eligibility |
| Credit Acceptance (CACC) | Corporate notes visible in HYG October 14; September 18/21 8-Ks read | No B/CCC bond eligibility verified. Analyst stock ratings and ABS ratings are excluded; no current tier inferred from memory |
| OneMain Finance (OMF) | June-2026 10-Q, Credit Ratings: S&P BB / Moody's Ba2 / KBRA BB+, stable | Above the commissioned B/CCC categories on this dated issuer debt table. HYG membership alone does not qualify it |

Primary rating extracts are **historical observations**, not assertions of unchanged live ratings. Search result navigation rails often show unrelated 2026 stories; those dates were never used as the article date. `primary_manifest.json` records source failures honestly. `SOURCE_NOTES.md` preserves publisher links and retrieval limits. No account, payment or paid data used.

## Fixed §3 calculation — supplementary, never the governing universe

Universe and method committed before any returns: `METHOD_LOCK.md` (54598a6b9), `UNIVERSE_FIXED.md` (637347ca0). Enova and Carvana were frozen as a two-name candidate basket; no names added after seeing prices. Best-tier measurement was attempted first: the public [FINRA bond page](https://www.finra.org/finra-data/fixed-income/bond) supplies a lookup interface, not a recovered, complete candidate daily bond/CDS panel; HYG snapshot lacks daily history. Historical Yahoo adjusted equity closes were then collected via yfinance. Latest data used October 13; these are dated returns, not live prices.

Beta and residual daily sample SD fit **2026-03-02–09-23, 143 return sessions** (prior close supplied). No intercept in z; beta uses covariance/variance. Primary = seven fixed dates October 2–13; secondary = September 25–October 1, five dates. October 12 ICE carry-forward excluded. Governing supplementary rows use previous **equity** trading close, including October 12 for October 13. This matches a daily equity test; a two-day October 9–13 sensitivity is separately shown. No post-window event or price enters the fit/test.

| Name | β | σ/day | 10/2 | 10/5 | 10/6 | 10/7 | 10/8 | 10/9 | 10/13 | z≤−1 | abs(z)≤0.3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ENVA | 1.2675 | 2.9098% | −0.042 | +0.722 | +0.703 | +0.338 | −0.101 | −1.112 | −0.353 | 1/7 | 2/7 |
| CVNA | 2.0440 | 3.2161% | −0.110 | −0.453 | −0.271 | −0.393 | +0.487 | −0.120 | +0.467 | 0/7 | 3/7 |

If eligibility were assumed, ≥half of two issuers means **one**, and ≥half of seven sessions means **four**: rule 2 has **0/2** qualifying issuers; rule 3 has **0/2**; conditional rule 4 = **MIXED**. Across 14 primary name-sessions, one z≤−1; mean z −0.017. This is descriptive, not a significance test or index contribution estimate.

| Secondary name | 9/25 | 9/28 | 9/29 | 9/30 | 10/1 | z≤−1 | abs(z)≤0.3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| ENVA | +0.079 | −0.361 | −0.344 | −0.076 | +0.823 | 0/5 | 2/5 |
| CVNA | +0.081 | −1.721 | +1.737 | −0.397 | +0.135 | 1/5 | 2/5 |

Secondary conditional **MIXED**: neither name clears three of five sessions under either rule. October 13 two-equity-day alternative (σ×√2) gives ENVA −0.398 / CVNA −1.120: neither primary issuer count reaches four; conditional token remains MIXED. Neither secondary nor sensitivity changes the strict NO_INSTRUMENT verdict.

**Noise caveat:** CARL's n=5 independent-normal exercise puts MIXED at about **99.8%** under noise (`AGENTS/CARL/research/2026-10-15_L708/VERDICT.md`). That percentage is not a new n=2 calibration. It establishes why MIXED must not be sold as partial support or proof of absence; the supplied rule is retained, not optimized. Additional limits: small selected basket, historical rating vintages, unknown ICE membership/weights, same-day equity responses, and credit/equity or lagged responses can diverge. The two desks are not independent credit witnesses merely because they run the same equity method.

## Disc-A — separate mechanism assessment and full bounded event inventory

`events.tsv` contains each 8-K source URL, public filing date, accession, items and window classification; the table below adds underlying event dates and interpretation. In the **September 24–October 13** event window:

| Public date | Issuer / event date | Evidence and interpretation |
|---|---|---|
| 9/24 | CRMT agreement 9/24, bridge 4 | SEC 8-K 0001171843-26-006216, Items 1.01/8.01: relief through 10/1; continued covenant/default risk, temporary accommodation. Separate same-day 8-K 006214 concerns director election/compensation votes, not a new credit event |
| 9/25 | Enova / OnDeck closing 9/25 | SEC 8-K 0001193125-26-402851: $500.026M ABS, weighted coupon 6.22%, revolving through September 2028. Small-business loan collateral; funding access, not a household default event |
| 9/29 | EART August collections; support paid 9/15 | Four filed 10-D certificates: 60+ DQ **15.22 / 14.46 / 12.32 / 10.89%**, all below **40%**; trigger occurrence **No** in each. Extension rates **4.49 / 4.73 / 5.29 / 5.44%**. EART 2022-2 / 2022-3 reserve capital contributions **$9.5M / $12.5M** on September 15 (pre-window underlying event, in-window filing). September 11 certificate signature is not publication date |
| 10/1 | CRMT agreement 10/1, bridge 5 | SEC 8-K 0001171843-26-006326: temporary relief through 10/8; continued transaction discussions. No permanent solution disclosed |
| 10/8 | CRMT agreement 10/8, bridge 6 | SEC 8-K 0001171843-26-006538: temporary relief through 10/15. Late-day disclosure; same-day stock test would miss a next-day response, even if CRMT qualified |
| 10/13 | CPS agreement 10/9 | SEC 8-K 0001683168-26-007809: warehouse capacity **$390M→$518M**, up to 95.5% advance rate, funding termination October 17 2027. Bank-lending expansion, not a withdrawal |
| 10/13 | Enova / NetCredit amendment 10/13 | SEC 8-K 0001193125-26-420462: **$200M**, SOFR+4%, 90% funding rate; revolving through October 15 2028, maturity October 15 2030. Terms, not a measured pre/post tightening |

**Just before window, not treated as new in-window news:** CACC September 18 filing describes September 17 state consent judgments (no admission, no new charge beyond existing accrual); September 21 filing extends Wells Fargo funding. WRLD September 21 filing appoints a CEO, not a borrower-credit release. These are in the saved inventory. Historical Tricolor collapse and existing fraud allegations do not become fresh September–October events through re-coverage.

**After cutoff, excluded from every attribution:** CRMT October 15 seventh bridge, through October 22 (BROCK KB-BRK-343, source re-read); Enova October 16 termination of the Grasshopper merger with $4M payment, SEC 8-K 0001193125-26-424282. The latter could matter to later funding expectations but cannot explain October 2–13 using hindsight. BLS October 14 real-pay evidence likewise postdates the window; its CPI denominator is one shared antecedent.

**Disc-A conclusion [EST]:** there is dated auto-lender stress and dated ABS support, alongside funding-access counterexamples. There is no qualified corporate-price co-move and causal consumer-credit event join. H1 is **not established**, and mechanism attribution remains **unresolved**; no “TRUE-in-spirit” finding. No new corporate lender downgrade, missed coupon, LME or new fraud was verified inside this bounded public filing/primary-search set. This is coverage-limited, not a universal negative. The four Exeter certificates establish no delinquency-trigger breach in those four reports; they do not establish absence of all trigger types or all shelves. Private corporate issuers remain unmeasured.

## Scope, continuity and verification

Boot/runtime receipt and ownership boundaries are in METHOD_LOCK. Replay: `.venv/bin/python3 AGENTS/OTTO/research/2026-10-19_L708/equity_test.py --replay` reproduces `equity_result.json` from saved adjusted closes. All 143 fit dates and both fixed windows complete for both supplementary names. Raw primary HTML is gzip-compressed, hashes refer to decompressed bytes; text extractions retained. Rating HTTP failures remain failures, not authenticated bodies. No index series, threshold, score, probability or trade changed; convergence remains 33/50 (same local colours).

Immediately consequential backlog outside this bounded read: September SDART/BLAST cycle and M&T October 16 Wilmington-specific read remain unswept; now explicitly pending October 20, before/with Ally. BlackRock October 16 confer outcome remains unverified, next check October 21. They are not labelled absent or resolved. THESIS v1.6 and broader backlog were not expanded. OTTO's three-packet inbox is integrated; seasoning verification closes the label/value review, not every legacy parser branch. BLAST computed-clock basis is now labelled at the panel schema.

**Formal H1 verdict: NO_INSTRUMENT.**
