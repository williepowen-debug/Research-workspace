---
request_id: REQ-DEWEY-20261023-002
from: WALTER (Will-directed in the WALTER terminal, 2026-10-23 11:12 ET: "yes dewey offer. I will spawn him shortly. use inbox", on WALTER's offer to commission an AI-vs-everything-else breakdown of junk-bond spreads)
to: DEWEY
created: 2026-10-23 (UTC stamp in the commit)
state: NEW
flag_trigger: T3 load-bearing but thin (HY at 340, 10bp under REG-T-04's issuance-freeze line, and no fleet instrument can say whether the move is AI-concentrated or broad; LIQUID records sector breadth as NO_INSTRUMENT) + T4 thesis pivot (broad credit turn vs AI-financing stress route to different owners and decisions)
originating_evidence: SIG-W-20261023-015 (near-trigger watch, HY 340 [10/22]), SIG-W-20261023-016 (HY new-issue market shutting), SIG-W-20261023-002 (10/22 chip selloff); WALTER analysis AGENTS/WALTER/research/2026-10-23_morning/HY_SPREAD_DEEP_DIVE.md
clusters: BANK_COLLATERAL (secondary AI_INFRA_CAPEX)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261023-002
kill_condition: (a) At intake, check whether LIQUID, BROCK or VULCAN has since published a sector or AI-vs-non-AI HY spread decomposition for October (grep their STATUS and workbooks); if one exists, return this request with the pointer. (b) Date expiry: the decision value is highest before the 10/27 close (REG-T-04's earliest fire, published about 10/28, FOMC day); after 11/06 run only the history leg (scope item 5) unless WALTER renews. (c) Re-verify at intake: the latest FRED BAMLH0A0HYM2 first-published value; if HY has fallen back below 320, deliver a short version (scope items 1 and 3 only).
deliver_by: Mon 2026-10-26 if possible (before the 10/27 close); usable through 11/06
---

# DEEP-RESEARCH REQUEST — Is October's junk-bond widening concentrated in AI-related issuers, or is it a broad credit turn?

**Why now:** the ICE BofA US High Yield spread rose from 260 [8/28] to **340 [10/22]**, +13bp on 10/22 alone; CCC is **1,340**, the highest in FRED's three-year window; US high-yield issuance fell to about $7B in October from about $51B in September (Bloomberg 10/21, via a syndicated copy). REG-T-04 (HY > 350 for 3 consecutive closes, the issuance-freeze trigger; chain REGINALD / LIQUID / Will) could fire on the 10/27 close. One unsourced claim in circulation (Connect CRE 10/21) says AI-related HY spreads hit a record 360 while non-AI moved 2bp, but it names no index and no date. Nobody on the fleet can say which story the 10/22 print is.

**Decision question:** of the HY and CCC widening since late August (and the +13bp on 10/22 specifically), how much comes from AI-related issuers (data-center and GPU-cloud borrowers, AI-infrastructure financings, semiconductor and tech names) and how much from the rest of the market?

**What changes with the answer:** if broad, it is an ordinary credit turn, and REGINALD, LIQUID and BROCK read REG-T-04 as a cycle signal (refinancing walls, CCC defaults, bank NDFI books). If AI-concentrated, it is VULCAN's financing channel (S1) and BROCK's AI-credit web, and the broad-credit read is weaker than the headline suggests. In the 3-year FRED history, the two prior 60bp+ widenings in 21 sessions either kept going (March 2025, to 461) or fully reversed within months (August 2024); which kind this is decides how much weight the 10/27 print deserves.

## Your own prior work to build on

- `output/2026-07-09_energy-hy-oas-unblind.md`: you recovered the **ICE BofA HY sector OAS table** from Fidelity Institutional's monthly US Fixed Income PDF (`931730.PDF`, as-of month-end). The same route for **9/30/2026** (and 10/31 if it lands before you deliver) gives a sector cross-section.
- `output/2026-07-02_hy-ccc-widening-decomposition.md`: June's CCC widening was AI-led (four named institutions), and the "8.3% tech/AI share of HY" figure could not be sourced. Reuse the method and the open question.
- `output/2026-08-02_ai-credit-guarantee-web.md`: the AI credit web (ORCL, CRWV, META, NVDA): the issuer list for the basket.

## Scope (in bounds)

1. **Sector cross-section from ICE BofA, as republished:** HY sector OAS at 8/31 and 9/30 (and 10/31 if available): which sectors widened most, especially technology, telecom/cable, and whatever sector holds the AI-infrastructure issuers. State the republisher and as-of date for every cell.
2. **A named AI-issuer bond basket, daily, 9/1 → latest:** 8-15 USD high-yield or crossover bonds of AI-infrastructure borrowers (for example CoreWeave notes, data-center and GPU-cloud issuers, AI-linked converts if relevant, SoftBank USD bonds). Use FINRA TRACE (free, public) or another public price source; convert to yield or spread where possible; compare with HYG/JNK or the broad HY OAS over the same dates. Name each bond (issuer, coupon, maturity, CUSIP if found).
3. **Strategist attribution, dated and named:** dealer or asset-manager notes (Goldman, JPMorgan, BofA, Barclays, Nuveen and similar, as publicly reported) that put a number on AI vs non-AI HY spreads in October, with the index they used. Resolve or kill the Connect CRE "record 360 / non-AI +2bp" claim.
4. **The tech/AI share of the HY index:** a sourced, dated figure (ICE or Bloomberg index factsheet, or a strategist note naming its source), so the weight of the AI slice is known.
5. **History leg (secondary):** a public long-run series for the ICE BofA **CCC & lower** OAS before July 2023 (FRED now serves only about three years), so October's 1,340 can be ranked historically. Fidelity's archive, ICE factsheets or academic replication datasets.
6. **Counter-evidence, required:** evidence that the widening is broad (defaults, downgrades or spread moves outside tech; energy, retail, healthcare, autos), and any sign the AI slice tightened while the index widened.

## Out of bounds

Trades and positions (TERRY); grading REG-T-04 or any desk's thesis (owners); paid data (Bloomberg/ICE terminal access needs Will's word); building a collector or new feed.

## Deliverable

Tables over prose, every cell sourced and dated:
1. Sector OAS cross-section (8/31, 9/30, 10/31 if available).
2. AI bond basket, daily, vs the broad index.
3. Strategist attributions with index and date; the Connect CRE claim resolved or killed.
4. AI/tech share of the HY index.
5. CCC long-run history (if found).
6. Counter-evidence.
7. UNKNOWNs.
8. A one-paragraph verdict: AI-concentrated, broad, or mixed, with a rough share if the data supports one.

**Return routing:** LIQUID and REGINALD action (REG-T-04 owners); VULCAN action on the AI-financing leg; BROCK and HENRY info; RED info. Drop the deliverable to `AGENTS/WALTER/inbox/DEWEY/` per the usual handoff and WALTER routes it (CHECKLIST 2.8b).
