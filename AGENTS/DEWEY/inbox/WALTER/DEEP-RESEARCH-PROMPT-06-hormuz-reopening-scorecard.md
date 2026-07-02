---
request_id: REQ-DEWEY-20260702-002
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: "verified legs ~0-1/4" (AGENTS/BRENT/NEXUS_BRIEF.md); "~80 mines... reported-but-not-detonated" uncorroborated (AGENTS/HAWK/REMARK_20260628.md). Highest cross-agent convergence in the mining sweep (BRENT+HAWK+WALTER+ORACLE).
clusters: Iran-Hormuz / energy tail / oil structural decoupling
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 2 of 13
deliver_by: 2026-07-04 (HAW-13 resolves Jul 4)
---

# DEEP-RESEARCH PROMPT 06 — Hormuz physical + institutional reopening scorecard

**Decision question:** Has reopening institutionally completed, stalled, or reversed — does HAW-13 fail Jul 4, is BRENT's Tier-1 stall-trigger or auto-disarm closer, and is the Brent<$74 decoupling backed by physically intact throughput?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** every leg is scattered-primary-document work no feed carries — JWC circulars, P&I club guidance, liner announcements, UKMTO/tanker-tracker data, MCM deployment reporting, 1987-91 clearance histories. The fleet's last verified snapshot is Jun-20 vintage.
- **(b) Consequence:** HAW-13 resolution + successor gate registration; BRENT's B/C/D scenario re-marks; BRT-07/17 timer start/kill (the P&I start-gun); the dormant Phase-2 short gate; validity of the >$74-75 re-arm trigger; SAM's Asia import-cost input.

## `/deep-research` prompt (paste-and-go)

> As of Jul 1-4 2026, build a verified Hormuz reopening scorecard resolving whether institutional reopening has completed, stalled, or reversed. IN-BOUNDS: (1) Institutional legs from primaries/trade press — JWC JWLA-033 Listed-Area status and any amendment since Jun-17 (Lloyd's/JWC circulars); IG P&I club and war-risk underwriter resumption guidance + current AP war-risk premium levels (% hull value) vs pre-Jun-17; liner routings Maersk/MSC/CMA-CGM/Hapag-Lloyd (Cape vs Gulf calls, resumption announcements); the PGSA-OFAC insurance-trap mechanics and whether it still blocks commercial cover. (2) Physical legs — corroborate or kill the "~80 mines" count; MCM assets deployed and demining progress/ETA; tanker strikes since Jun-20 incl. Kiku (6/27); actual transit throughput vs pre-war ~20mb/d (UKMTO/JMIC/tanker-tracker data) vs the ~75%-of-prewar claim. (3) Base rates — 1987-88 Earnest Will and 1991 Gulf mine-clearance timelines; historical lag from ceasefire to JWC de-listing and to P&I resumption in prior Gulf episodes; harassment-campaign→realized-supply-shock frequency. OUT-OF-BOUNDS: oil price forecasting, OPEC+ policy, SPR mechanics, Russian crude supply, ceasefire-durability odds (HAWK's own judgment), positioning/COT. TIMEFRAME: events Jun-17→Jul-4 2026; comparanda 1987-2024. ENTITIES: JWC (Lloyd's), IG P&I clubs, UKMTO, JMIC, Maersk, MSC, CMA-CGM, Hapag-Lloyd, Kiku, PGSA, OFAC, USN/coalition MCM forces. DELIVERABLE: per-leg VERIFIED/PARTIAL/UNVERIFIED/REVERSED grades feeding HAW-13 pass/fail and the BRT-07/17 P&I start-gun.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-002; WALTER routes as a `research-output` signal (→ HAWK, BRENT action / SAM, RED, PROME info) and closes the ledger row.
