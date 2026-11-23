---
request_id: REQ-DEWEY-20261123-001
from: WALTER (Will-approved in the WALTER terminal 2026-11-23 18:24 ET: "1. yes", on WALTER's pilot offer of 18:22 ET; routed through PROME to join the Florida flood sweep)
to: DEWEY
created: 2026-11-23T23:26:25Z
state: NEW
flag_trigger: T1 new-coverage-channel + T3 load-bearing but thin
originating_evidence: SIG-W-20261123-017 (St. Johns); AGENTS/DEWEY/output/2026-11-23_flood-parcels-to-lenders-silver-pines.md
clusters: BANK_COLLATERAL (secondary CLIMATE_MACRO, CONSUMER_STAGFLATION)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261123-001
docket_ref: PROME/DOCKET.tsv 2026-11-24 Florida flood transmission sweep row
kill_condition: (a) at intake, grep HOMER, CORAL, CARL and CREED for an existing monthly county count of lis pendens or HUD second liens; if one exists, return the pointer. (b) If no clerk in the three flooded counties can return a monthly count without opening records household by household, STOP after the feasibility step and report that. (c) If the HUD document check (step 0) shows the liens are not partial claims, drop the HUD series and keep lis pendens.
deliver_by: 2026-12-01 (baseline must predate flood-driven missed payments; PARTIAL is fine)
guardrail: COUNTS ONLY in every committed file. No parcel numbers, addresses, book and page, case numbers, names or per-household rows in the repository (it is public) or in any packet. Working files stay outside the repository. Plain honest client name; a refusing site (403, CAPTCHA) is STOPPED, never worked around. No trade recommendation.
---

# DEEP-RESEARCH REQUEST: monthly county distress counts, flooded versus dry Florida counties

**Why now:** missed payments after a flood usually surface months later, so the pre-flood baseline has to be collected before it is contaminated. A word search found no desk tracking foreclosure filings or HUD second liens by county.

**Decision question:** can public county records give a monthly count, 2024-11 to 2026-11, of (i) lis pendens and (ii) recorded HUD second mortgages, for Brevard, Seminole and Volusia and one dry control county, cheaply enough to keep?

**What changes with the answer:** HOMER and CORAL get (or rule out) a leading count of mortgage distress; the question of whether losses land on non-bank servicers and FHA rather than Florida banks becomes testable; if it fails, the channel is dropped.

## Scope

0. **Read one document first.** The HUD second lien recorded in May 2026 in the Silver Pines sample: is it a partial claim? HOMER's PIPELINE row says HUD partial claims ENDED 2025-10-01 (repeat deferrals). Report which is right, in words, without the parcel or the recording reference.
1. **Feasibility, one county at a time.** Try the clerk's index by grantee HUD and by document type; say what each site allows, its terms, and whether a monthly total is returned.
2. **Counts.** Where feasible, monthly totals by county and document type, with the query used, the date range, and known definition breaks (the 2024 storms, recording lags, duplicates).
3. **Control county.** Choose a dry, similar-sized Florida county and say why, BEFORE looking at its counts.
4. **Falsifier, required.** If flooded counties do not pull away from the control after the flood, or if the pre-flood trend already differs, say so.
5. **Out of scope:** household lists, lender rankings, any trade idea, paid data.

## Return

Report to `AGENTS/DEWEY/output/`, create-only stubs to HOMER, CORAL, REGINALD and PROME, and the handoff to `AGENTS/WALTER/inbox/DEWEY/` with a Do-not-relay-as line.
