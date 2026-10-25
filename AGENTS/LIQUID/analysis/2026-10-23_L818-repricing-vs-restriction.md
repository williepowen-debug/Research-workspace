# L818 — Is the credit widening financing restriction, or repricing? What would a REG-T-04 fire add?

**LIQUID, 2026-10-23 22:1x ET** (Will-launched session; question from CATO via Will). Inputs: DEWEY REQ-002 `AGENTS/DEWEY/output/2026-10-23_hy-widening-ai-vs-broad-decomposition.md`, REQ-003 + correction box `…/2026-10-23_ccc-and-under-80-loans-three-way-split.md`, `…/2026-10-23_ccc-concentration-optimum-altice.md` (a4d44b7ed), `…/2026-10-23_hy-issuance-window-october.md`; REGINALD `PROME/inbox/processed/2026-10-23_from-REGINALD_REG-T-04-bank-lane-and-10Y-falsifier.md` (012e5c08c) and its later volume withdrawal (`AGENTS/REGINALD/NEXUS_BRIEF.md`); my own grades `research/2026-10-23_evening/REPORT.md`. Targeted check run here: `scripts/transmission_check.py --asof 2026-10-22` (FRED latest-revised; matches first-published on every 10/16–10/22 cell read tonight). No gate, letter or approval changed.

## Answer

**Mainly repricing, not yet shown to be restricted financing.** Spreads are wider at every tier, and the cost of new junk debt is up sharply. But no measured funding channel has tightened, and the "issuance freeze" is only partly shown: the window is narrower and more expensive, not shown to be shut. A REG-T-04 fire would confirm the size and persistence of the repricing. On its own it would **not** show restriction, because the rule grades a price only.

## 1. Broad repricing vs concentrated issuer stress — what is established

| Claim | Status | Basis |
|---|---|---|
| HY 260 → 340: ~65% came in a broad September selloff; ICE Technology moved in line with the index | ESTABLISHED (DEWEY REQ-002) | ICE sub-indices via DEWEY |
| AI infrastructure ≈ 10–15% of October's widening (CoreWeave ≈ +230bp, SoftBank ≈ +100bp; ~3% of market ≈ 3bp of +24bp, 10/13–10/22) | ESTABLISHED as an estimate | DEWEY, HYG holdings files saved 10/13–10/21 (a **proxy**, not the ICE index) |
| Tier shape, 15 sessions 10/1 → 10/22 (governing ICE index, FRED): **CCC +125bp, B +17, BB +6, IG +3** | ESTABLISHED | `transmission_check.py`; CCC 15-session move at the 96th percentile of a ~3-year window |
| Tier shape, one day 10/22: BB +12, B +14, CCC +33, HY +13 (all ≥ 97th pct d/d) | ESTABLISHED, **n = 1 day** | same |
| Rated CCC (BondBloxx XCCC, Bloomberg 2%-capped CCC index, holdings 10/22) is **0% AI builders**, ~6% software, **16.5% cable/telecom/media** | ESTABLISHED as **constituent weights** | DEWEY fund-page parse (DEWEY's correction applied: CoreWeave is B+/Ba3/BB-, not CCC; the "~17% AI" figure was HYG's yield ≥12% **sleeve**, not rated CCC) |
| Whether a few names (e.g. Optimum/CSC) explain most of CCC's +161bp October move | **UNKNOWN** | weights are not contributions; no 9/30 XCCC file; bond prices not public |

**Reading:** across October the move is CCC-led (distress-tier repricing on the L818 rule: CCC alone). On 10/22 BB moved with CCC for one day, which is the transmission-widening shape. **One day does not establish it.** The rated CCC tier is cable/telecom-heavy, not AI-heavy. Software and AI-disruption stress sits mostly in **loans, private credit and BDCs** (below-80 loans: technology 39%, $54.4B of $139.8B, JPM 10/6, via DEWEY). It does not sit in rated CCC bonds.

## 2. Funding or issuance restriction — observed vs unobserved

| Channel | Observed | Reading |
|---|---|---|
| Overnight funding | SOFR99−IORB +8bp [10/22] (+5 to +8 all October); SRF $0 [10/23]; reserves $2,962.6B [week to 10/21] | **No restriction.** GATE-LIQ-079 not armed |
| Dealer corporate inventory | NY Fed PD IG 5–10y net −$1,717M [as-of 10/14] after −$1,462M (076 W2 MET) | Dealers holding **less** IG paper. This is a net stock, not refused intermediation |
| HY bond issuance | ~$7B October to 10/21 vs ~$51B September (**one Bloomberg snippet**); October 2025 also ran below half of September; deals priced at wide levels; **no named HY bond pulled** | **Narrowed and expensive, not shown shut** (DEWEY). REGINALD withdrew his earlier "freeze under way on volume" on 10/23 evening |
| Leveraged loans | AVI-SPL $690M pulled; Circet €3B postponed | Two named loan deals. That is evidence of restriction at the margin, and it sits in loans |
| Price lock-out | CCC effective yield 17.99% vs single-B ~8.19% [10/22, DEWEY] | CCC issuers are priced out. That is a price restriction, not a quantity restriction |
| Named facilities | Car-Mart relief extended to 11/01; RaDD extended to 2029; Lambda-tenant CMBS not sold as of 10/21 | Mixed. Some borrowers need support while others still get access |
| **Unobserved** | Haircuts, prime-broker terms, sponsored repo, MMF maturity, bank revolver draw data, October HY volume total (month-end ~11/2), EUR→USD basis | The restriction channels I cannot see. **Do not read their silence as health** |

## 3. Bank / NDFI channel

A candidate bank channel is **actual draws on C&I revolvers or NDFI lender/fund-finance lines** when other financing becomes less attractive (REGINALD). That would be a liquidity-use channel, distinct from credit loss. Such draws and their financing motive are not identified by the aggregate balance observations below. Wider spreads are **not** evidence of regional-bank credit losses:
- REGINALD: KRE vs HY daily correlation +0.07 over 57 days. The 10-year, not HY, moves regionals (R² 0.13, weak). BANK-ABSENT at the 10/22 cell (~0.7).
- H.8 small domestic banks SA [week to 10/14, released 10/23]: borrowings 307.3 → 316.4 ($B), with deposits +7.0 and cash +12.1. That is one week, and since deposits rose it is not a deposit-replacement signature.
- Losses, if they come, come later and through BDC/NDFI borrowers (BROCK's lane), not through bond spreads.

## 4. What a REG-T-04 fire would add

- **Adds:** the repricing is large (>350) and persistent (3 published closes). That is a cycle signal for the bank/NDFI lane, and it is the trigger for TERRY's approved-not-fired HYG put leg (DOCKET L830; TERRY and Will own that).
- **Does not add:** proof that financing is restricted. The letter grades price only. A fire on a CCC-only week would most likely be distress-tier repricing, possibly concentrated in a few names (Optimum is the live dated event, L825), and **the share those names explain stays UNKNOWN**.
- **Single-issuer rider:** CATO's brief calls REGINALD's single-issuer disclosure rider a proposal. `PROME/WILL_QUEUE.md` row 512 records it **RULED APPROVE A, Will 2026-10-23 17:01 ET**. It is a disclosure line with no level or consequence change, so this interpretation is the same either way. Flagged to PROME; not adjudicated here.

## 5. Next observation that would change this conclusion

1. **BB widening with CCC on consecutive days** (FRED A1HYBB/A3HYC, 10/23 obs publishes Mon 10/26). If BB keeps moving with CCC, the read shifts from distress-tier repricing toward transmission widening.
2. **A funding leg moving with credit:** SOFR99−IORB ≥ +30bp (079 arm), SRF draws outside quarter-end, or a dealer move from net stock to refused intermediation. Any of these would move me from repricing to restriction.
3. **October HY issuance total at month-end (~11/2)** and any named HY **bond** pulled. A shut window on quantity, not price, would confirm the freeze leg.
4. **H.8 C&I / NDFI loan balances** rising over consecutive weeks would be a lead for investigation, not proof of draws or market-to-bank substitution. Identify the borrower/facility and reconcile originations, repayments, purchases, reclassification and other balance changes against unused commitments and the reason for borrowing before calling it liquidity use caused by a narrowed market window.
5. **Optimum Chapter 11 or creditor deal** (L825): read the CCC/HY cells that day and the two following, to bound how much of the tier's move is one name.


**Correction 2026-10-25T14:40:14-04:00 — WQ-523 / DOCKET L839 (Will-approved; PROME packet October25):** the former item 4 called H.8 balances “draw lines” and said persistence “would show” liquidity use. That inference is withdrawn. H.8 stocks can flag a candidate channel but cannot identify utilisation or substitution. Section 3 now states the bank-draw route conditionally. Original October23 observations, tier/spread grades, forecasts and REG-T-04 terms are unchanged; pre-correction text preserved in `research/2026-10-25_WQ523-carmart/sources/before-2026-10-23_L818-repricing-vs-restriction.md`.
