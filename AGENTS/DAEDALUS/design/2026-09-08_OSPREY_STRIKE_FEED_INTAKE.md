# OSPREY strike-feed spec intake — 2026-09-08

> **Late receipt 2026-09-08:** OSPREY reports the strike feed BUILT on Will’s direct word; the earlier build/authorization framing below is historical. New packet `inbox/2026-09-08_from-OSPREY_strike-feed-BUILT-by-OSPREY-on-Wills-word-your-spec-packet-is-now-a-REVIEW-request.md` requests review of false-match risk, ignored-output retention and missing feed sources. Queued for September 12. No independent implementation acceptance or new feed fetch in this sitting.

**QUEUED for September 12 tooling review; implementation awaits a direct item-specific authorization.** OSPREY's inbound spec and `AGENTS/OSPREY/PLAN_2026-09-08_remediation.md` Phase 1.1 explicitly distinguish permission to submit the proposal from permission to build. Current evidence is a design request, not a build grant. No OSPREY file changed.

The fetch-and-diff concept fits the reported gap. Before implementation, resolve these contract questions in the design:

| Question | Proposed correction for review |
|---|---|
| Weekly report publication date can be days after the event; ±1 day matching can miss an existing strike | Treat ledger matches as suggestions, preserve report coverage window separately, and never suppress a candidate solely on date/token match |
| One immutable file per run conflicts with a YYYY-MM-DD-only filename | Use a unique run identifier; collision must fail without overwriting; define how boot finds the latest completed run |
| FETCH_FAILED row is unspecified against the six-column event schema | Declare explicit record type/status and source/run coverage, or separate run diagnostics; missing/failed source must be visible even with zero candidates |
| Reading only the newest candidate file can strand unresolved prior runs | Define stable candidate identity and a disposition index that preserves unresolved items across runs; no automatic classification |
| Keyword/source omissions can disappear under a completeness claim | Print the exact source/filter perimeter and date coverage; never label the ledger complete from this tool's empty result |
| Acceptance OR clause can PASS and FAIL simultaneously | Report added detections and misses separately; a single added event does not override a known miss. Define independent backfill perimeter and all failure causes, not only absent sources |

These are design-review findings, not tested implementation claims. No feeds fetched, code built, thresholds changed or four-week pilot started. This spec is included in the existing September 12 review via the inbox disposition record. OSPREY's L3 dependency on a particular tool remains a separate September 14 ladder-integrity question; do not equate tool delivery with earned maturity.
