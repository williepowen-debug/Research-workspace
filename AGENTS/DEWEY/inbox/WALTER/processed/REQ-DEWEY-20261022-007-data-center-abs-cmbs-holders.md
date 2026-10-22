---
request_id: REQ-DEWEY-20261022-007
from: WALTER (Will-approved in the WALTER terminal, 2026-10-22 ~12:30 ET, option C of WALTER's shortlist)
to: DEWEY
created: 2026-10-22 (UTC stamp in the commit)
state: NEW
flag_trigger: T1 new coverage channel (no desk maps holders of data-center securitizations) + T2 cross-channel (AI capex to insurer and private-credit balance sheets)
originating_evidence: SIG-W-20261020-011 (Lambda-linked CMBS lead; dated execution and senior-class evidence missing) + SIG-W-20261020-010 (data-center bond tenant cohort) + SIG-W-20261016-017 (Volta ~$5B loan sold at S+650 / 95) + SIG-W-20261008-008 (Blue Owl insurance push); SHADE has received data-center signals but holds no analysis
clusters: AI_INFRA_CAPEX (secondary PC_STRESS)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-007
kill_condition: At intake, grep AGENTS/SHADE, AGENTS/BROCK, AGENTS/VULCAN and AGENTS/CREED for an existing data-center ABS/CMBS size-and-holder table. If one exists, extend it and say so. Coordinate scope with REQ-DEWEY-20261022-005 (hyperscaler funding gap) so the two do not duplicate the project-finance leg: 005 owns the issuer side, 007 owns the securitized debt and its holders.
deliver_by: no hard date
---

# DEEP-RESEARCH REQUEST — How much securitized debt is backed by data centers, and who holds it?

**Why now:** this week's flow included a CMBS deal tied to Lambda, a cohort of data-center bonds, and the Volta loan clearing at 95 cents. AI-infrastructure debt is increasingly packaged into asset-backed securities (ABS) and commercial-mortgage-backed securities (CMBS) and sold to insurers and private-credit vehicles. No desk maps how big this is, how concentrated the tenants are, or who holds it.

**Decision question:** how much data-center ABS and CMBS is outstanding and in the pipeline, how concentrated is it by tenant (hyperscaler vs AI-cloud companies without an investment-grade tenant), and what share is held by life insurers, private-credit-affiliated insurers and private-credit funds?

**What changes with the answer:** SHADE learns whether data-center paper is a material exposure for the insurers it watches (the private-equity-insurer nexus); BROCK learns whether private-credit funds hold the weaker tranches; VULCAN gets a check on the "chain breaks at developers without an IG tenant" view from its L782 ranking.

## Scope (in bounds)

1. **Size.** Outstanding and 2025–26 issuance of data-center ABS and CMBS (single-asset single-borrower and conduit exposure), from rating-agency presale and surveillance reports (KBRA, Moody's, S&P, Fitch, DBRS), Finsight or similar trackers, and trade press. Dates and sources per figure.
2. **Tenant concentration.** For the largest deals: main tenants, lease terms, whether the tenant is investment grade, and any AI-cloud company tenants (CoreWeave, Lambda, Crusoe, others). Mark reported-not-documented items.
3. **Holders.** Evidence from insurer statutory filings (NAIC Schedule D), insurer investor presentations, and fund holdings on who buys these: life insurers, Apollo/Athene, KKR/Global Atlantic, Brookfield, Blackstone-affiliated insurers, BDCs and private-credit funds. Give amounts where disclosed.
4. **Rating and structure.** Typical capital structure, ratings, and what protects senior holders if a tenant leaves (lease term, re-leasing assumptions, power contracts).
5. **Stress evidence.** Any downgrades, watch placements, tenant departures or price markdowns on data-center paper to date.
6. **Counter-evidence, required.** Analysis that this asset class is well-protected (long hyperscaler leases, high senior subordination) or small relative to insurer portfolios.

## Out of bounds

Trade ideas (TERRY); grading SHADE's, BROCK's or VULCAN's theses; the hyperscalers' own corporate bonds (REQ-005 covers them).

## Deliverable

Tables over prose, every cell sourced and dated: (1) size and issuance table; (2) top-deal tenant table; (3) holder table; (4) structure and rating summary; (5) stress events; (6) counter-evidence; (7) explicit UNKNOWNs.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-007. WALTER routes it as a research-output signal: SHADE action; BROCK, VULCAN, CREED, LIQUID, RED and PROME info.
