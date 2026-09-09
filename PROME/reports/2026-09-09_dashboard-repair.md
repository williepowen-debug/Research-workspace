# PROME dashboard repair — September 9, 2026

Will requested: “repair Prome misleading dashboard”. DAEDALUS O1/O2 are repaired and verified in the generated local pages. Existing Claude-hosted Artifact tabs were not republished: this session has no compatible publisher. This is not an overall PROME maturity regrade or a fresh market-data sweep.

- [FleetOps local page](../artifacts/fleet_dashboard.html)
- [Helm local page](../artifacts/handbook.html)
- Finding source: `AGENTS/DAEDALUS/upgrades/PROME_SWEEP_2026-09-08.md`, O1/O2.

## Changes and evidence

| Claim | Artifact | Command / inspection | Result | Change |
|---|---|---|---|---|
| Amendments outrank the older base | HEARTBEAT.md; PROME/HEARTBEAT_DASHBOARD.md; tools/heartbeat_projection.py | `python3 -m unittest discover -s PROME/tools/tests -p test_heartbeat_projection.py` | 12 tests pass | Ordered, numbered JSON projections bind to exact amendment prose by SHA-256; missing, changed, malformed or unsupported projections withhold summary/levels. Semantic completeness still requires author review. |
| FleetOps no longer asks for a closed deployment decision or implies a September 9 fourth bar | artifacts/fleet_dashboard.html | `python3 PROME/tools/fleet_dashboard.py --no-snapshot -o PROME/artifacts/fleet_dashboard.html`; independent rendered HTML inspection | Build passes; STAND DOWN / NO DEPLOY; FT-10 consumer 0/4 NOT FIRED; owner integration pending | Headline, affected channel heads/bodies and ticker consume the reviewed amendments. Source dates remain separate from build time. |
| Basis-point units remain correct | tools/fleet_dashboard.py; generated HY tile | Regression cases for HY, CCC and SOFR-IORB; actual HTML inspection | HY 268 bp, 12 bp below 280 | Explicit bp conversion uses each configured series unit; prevents 268 becoming 2680. Also fixes direct library build's undefined timestamp and uses timezone-aware ET. |
| Helm reflects the later Cboe publication and the confirmed call sale | BRIEF.md; artifacts/handbook.html | `python3 PROME/tools/will_handbook.py --no-feed -o PROME/artifacts/handbook.html`; independent HTML inspection | Build passes; later SKEW 148.86 supersedes failed retrieval; sold USO call absent from holdings, 37 shares retained | Narrative reconciled to September 8 evening checks and September 9 broker receipt; position parser preserves closure markers before stripping Markdown. |
| Dated account values remain visible without appearing freshly reconciled | tools/will_brief.py; generated Helm account panel | Long-header regression; rendered export date/stale warning | Pass | Parse the complete FORGE header rather than truncating at an arbitrary character offset. No new cash/account total inferred from sale proceeds. |
| Repair preserves unaffected consumers and baselines | tools/tests/test_heartbeat_projection.py; existing gate/queue suites | 12 new regressions; gate tests (4); queue parser self-test (22); `git diff --check`; weekday claim check | Pass | Japan, AI capex, metals, unaffected ticker tokens and NEXUS split preserved. Test renders do not advance dashboard/change-feed baselines. Original amendment paragraphs unchanged. |

The projection companion holds display metadata only. Its payloads were moved unchanged from the initial inline implementation after measurement exposed a byte-budget problem. `python3 PROME/tools/measure.py HEARTBEAT.md` reports **24,266 B**, below the **24,412 B** rotation trigger; before this repair the file was **24,106 B**. The companion pointer and whitespace are the only HEARTBEAT changes. No historical prose was deleted or silently regraded.

## Independent review and remaining scope

A PLAN cold read checked amendment precedence, all affected fields, source dates and failure behavior. A RESULT cold read independently inspected both generated HTML pages and passed the then-current 11 tests, with no blocking defect in O1/O2. The subsequent size fix only relocates identical projection payloads; the added missing-companion regression brings the suite to 12. The narrowly scoped follow-up passed: identical parsed views for inline/companion inputs, missing-companion withholding, actual FleetOps output and all 12 regressions; no new residue.

Declared residue: Helm's separate Top priorities retains September 8 “Cboe ungraded” wording, which is ambiguous against the corrected FALSIFIER; HEARTBEAT's unconsumed book/threshold prose remains historical and unreconciled. Header amendment-count checking remains owned by the existing gate, not duplicated in the projection parser. The Helm's existing ticker-mention gate association is not a precise contract join. Owner integrations and broker fills not supplied by Will remain unverified. O3/S1/S2 and broader queue/canon reconciliation are outside this repair.

Publication is a separate unfinished step. Existing targets remain FleetOps `https://claude.ai/code/artifact/c884f088-4936-44a0-9232-30851b9427b6` and Helm `https://claude.ai/code/artifact/ee088d08-bf26-48ab-bad2-7ee9155da12a`. Local build success does not establish their contents. Republish these files through the compatible Artifact publisher and inspect both hosted pages before claiming remote completion.
