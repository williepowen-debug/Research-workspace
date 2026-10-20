# BRENT key-file and workbook review — October 20, 2026

Will directly requested review/update of BRENT's key files, specifically workbook. Scope: owned-file agreement, navigation, declared ledger coverage, existing saved evidence and standard health checks. No new trade, threshold, paid feed or scheduled research job. Root resolved with Git; foreign PROME/WALTER changes were left alone and pull deferred.

## Repairs completed

| Surface | Finding | Repair / evidence boundary |
|---|---|---|
| workbook/README.md | September navigation omitted USO and the COT vintage ledger; latest-research links still led to September passes | Added USO/COT destinations, current report navigation and explicit freshness limits. No duplicate numerical USO table. |
| workbook/LEDGER_GLOB | The maintained USO observations series was outside the existing scan | Added its exact path. Scan now covers 13 rather than 12 files; USO is no longer in the outside-perimeter list. Extends the existing tool; no new guard or numeric trading threshold. Generic scans use maintenance/Git time for this headerless TSV, not its per-row source clocks. |
| workbook/COT_VINTAGES.tsv | Header said October 9/vintage9 although the final row was October13/vintage10, recorded October16 | Reconciled header to saved row and October16 routine's primary/independent-pull receipt. All numerical/data rows unchanged. Not a new CFTC retrieval, grade or reissue check. |
| docket/CATALYSTS.tsv and STATUS calendar | October26 USO short-interest publication dependency missing | Added one research-only row from the FINRA calendar already verified in the investigation, then used the existing calendar generator. No promised automatic run; report observes October15, not October20. Existing 25 rows preserved. |
| thesis/THESIS.md | Latest holdings paragraph still cited October14 and treated the expiring calls' outcome as unknown | Reconciled to TRADE's October20 recovery, October19 secondary broker evidence and matched closing receipt. Current orders/fill clocks/post-snapshot changes remain unknown. No new broker-image verification or booking. |
| thesis/THESIS.md and CHANGELOG.md | Today's news and USO research lacked an explicit thesis-reader boundary | Linked completed studies and retained announcement-versus-delivery / proposal-versus-throughput / historical-versus-current distinctions. v5.13, WAIT, probabilities, holding rules and authority unchanged. |
| STATUS / SCRATCH / NEXUS_BRIEF / demand tracker | Needed a current audit/handoff and older call-context reconciliation | Added scoped update and retained evidence debts. STATUS's fundamental-source clock explicitly scoped; no global freshness inferred. Routine alert observations/rules unchanged. |
| STATUS dated detail | Crossed existing 75% rotation threshold during the update | Preserved dated October14 context verbatim in archive with exact UTF-8 byte/hash/CRC receipt; reduced active reader below the existing 70% stop. Current rules and position reader remain accessible. |

## Files deliberately kept unchanged

- **Frozen KB/VX/FLOW/GROUP_MAP:** historical, not destinations for the new USO findings.
- **REGISTRY:** no new registered trading test/instrument or changed numerical letter. A research folder is not a trigger.
- **LESSONS / LESSONS_INDEX:** existing provenance, source-date and duplicate-state lessons already apply. The structural prose/index check passes. No complete new semantic re-verification or lesson amendment claimed; last semantic dates remain intact and age findings visible.
- **TRADE:** already carries the newer recovery/closing evidence; no new broker fact or owner grade to record. THESIS's stale reader was repaired instead.
- **PREDICTIONS:** no new outcome established by USO research or file maintenance. BRT30 remains open for its endpoint; BRT31 owner evaluation remains pending.
- **INCIDENTS:** no new authenticated current restart/loss evidence. Historical status/last_verified fields are not refreshed by age or a diagnostic.
- **board_log:** no new packet was consumed by this review. Previous mail state remains at startup receipt and handoff.

[Preservation manifest](preservation.json) permits byte checks of these unchanged files and COT data rows. [STATUS rotation receipt](status-rotation.json) records the archived payload and extraction rule.

## Health findings and remaining work

Full boot ran once for this review: **6 OK / 4 FINDINGS / 0 FAIL, exit2**, all ten checks completed. This is not a clean boot. It fetched diagnostic source observations; no vendor market quote or diagnostic threshold output was adopted as a new settlement, owner holding grade or position mark.

- EIA utilization returned week ending October9 but exceeded its unchanged age budget. Presence and freshness differ.
- Instrument check found the JWC human-verification stamp outside budget; Cushing age and paired crack/spread coverage remain limited. Tanker liveness requires its owner-grade components.
- Facility diagnostics disclosed five aged ACTIVE rows and twenty aged rows in other present-tense statuses. These are evidence debts, not inferred restarts; counts belong to this run, not a replacement outage census.
- Ledger activity nudge remains advisory work to assess, not authority to restamp unrelated ledgers. Once STATUS's recent document date governs the scan, LESSONS_INDEX's older semantic verification date also produces an age finding; structural prose/index agreement does not resolve semantic freshness.
- Calendar event-set check passes after generation, but eight standing-state reconciliation rows remain flagged as predating the graded October15 catalyst. They are UNVERIFIED, not proven wrong, and were not silently restamped.
- Existing next owner priorities: saved October15 EIA/policy/BRT31 interpretation; HENRY's December measurement adoption/rejection; deferred ACTION packets; source/restart and actual live-scheduler verification. USO's new publication dependency does not displace those tasks.

No missing software dependency prevented this review. Broad authenticated USO lending data and current technical/options studies remain absent research inputs. New source research and contract-matched holding grades are distinct from the completed recordkeeping repair.

## Validation scope

Run existing calendar/ledger/read-cap/weekday/lesson checks plus local link, TSV-shape, source-row preservation and archive-hash checks. The coverage change was tested against the previous perimeter (USO absent) and the new perimeter (USO included exactly once); no shared checking code changed. The calendar's eight standing-state findings and unrelated aged evidence are intentionally retained. See [checks.json](checks.json) for the final receipt. No fleet notification, owner consumption or live-scheduler acceptance is asserted.
