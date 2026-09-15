# L335 — OPEN-row history coverage repaired

**Implemented, independently accepted, and applied to the live ledger on September 14, 2026.** Changes to ordinary Notes and Item-body text now produce retained history. Repeating an unchanged sync produces no additional events.

## Implementation

`PROME/tools/wq_ledger.py` now stores the full parsed OPEN source in the existing `record` field as deterministic `wq-open-source-v1` JSON. It includes Item, Type, raw Needed-by, Since, recommendation and Notes. This preserves evidence beyond the display summaries, including links, Unicode and embedded tabs. Type/Since retain the shared parser's existing normalization.

The schema and terminal ruling records are unchanged. The existing semantic comparison already includes `record`, so no parallel change detector was added. The CSV reader temporarily allows fields up to the file's encoded size and restores its prior setting afterward; this prevents a large source snapshot from making the ledger unreadable.

**Tradeoff:** future updates retain more text and the ledger will grow faster. It remains a programmatically read history surface, not a boot-read document.

## Verification receipt

**VERIFIED:** reviewed implementation based on `f9875b6f4`, `wq_ledger.py` SHA-256:

`49aeb2da11305637e25aefb3511452cd753504d37a54b56a228e2fa06ac35ece`

| Claim | Exact artifact / command | Observed result |
|---|---|---|
| Original defect is reproducible | Extended `test_wq_ledger_L336.py` against the original implementation | Notes/body/long-tail cases failed before the repair; no harness errors |
| Source changes survive append and read | `python3 -W error::ResourceWarning PROME/tools/tests/test_wq_ledger_L336.py` | 24 tests pass, including deletion, A→B→A, URLs, tabs, long fields, legacy upgrade, unchanged repeats, transitions and broken-seal refusal |
| Existing behavior remains tested | `python3 -W error::ResourceWarning PROME/tools/wq_ledger.py --selftest` and `python3 -W error::ResourceWarning PROME/tools/decision_deck.py --selftest` | Both selftests PASS |
| Rollout adds only missing OPEN-source evidence | Frozen migration candidate and independently checked live append | Exactly 28 UPDATED events; among compared semantic fields, only `record` changes |
| History remains append-only | Old ledger compared with candidate and live result | Entire original byte sequence preserved as an exact prefix |
| Live ledger remains valid and idempotent | Tool `check`, then second live `sync` | 270 events, schema/seal pass; second sync adds zero and changes neither ledger nor seal |
| Deck compatibility | Compare terminal ledger and full Decided projections before/after migration | Identical projections; no new source snapshot is rendered as a ruling |

The live ledger moved from **242 to 270 events**. Added snapshot events cover WQ **31, 157, 169, 187, 204, 213, 219, 224, 225, 228, 229, 230, 234, 235, 236, 237, 238, 241, 242, 243, 244, 245, 246, 247, 248, 250, 251 and 252**. These record content newly captured by the improved projection. They do not assert that Will changed those decisions at sync time.

## Independent review

**Plan read — `docket_plan_read`:** found the CSV field-capacity blocker before implementation. Its oversized Notes counterexample was addressed in the reader and a source→stored-event→repeat-sync regression. Other flags are declared in the [acceptance plan](../plans/2026-09-14_L335-ledger-coverage.md).

**Result read — `docket_result_read`: ACCEPTED, no blockers.** The reader inspected the final code hash above, checked the candidate against the frozen source, independently verified prefix preservation and the precise event set, and tested an additional combination: **terminal → OPEN → BLOCKED**, with a large recommendation, a tail correction, and ruling-like text inside the snapshot. Each real transition produced one event; the full recommendation survived; snapshots never entered the terminal Deck projection. Repeating sync was a no-op, and a caller CSV limit deliberately set to 64 was restored.

Both readers confirmed read-only closeout. Their temporary evidence is under `/tmp/prome-L335-independent/`; the durable findings and acceptance are recorded here. This was a review of the implemented result, not author confirmation substituted for independent verification.

## Live rollout and limits

Immediately before sync, queue/archive contents, archive membership, ledger, seal and reviewed code were checked against the frozen candidate inputs. Live sync ran through the ledger tool. Post-sync checks confirmed the reviewed semantic event set, unchanged old prefix, valid seal, unchanged source inputs and unchanged Decided projection. No queue content or foreign desk files were edited.

- **IMPLEMENTED — VERIFIED:** full parsed OPEN-source records and adequate reader capacity.
- **TESTED — VERIFIED:** regressions, both selftests, candidate rollout and live idempotence checks pass.
- **INDEPENDENTLY VERIFIED — VERIFIED:** bounded implementation and candidate rollout accepted by a separate reader; live rollout matches the reviewed semantic result.
- **STILL UNRESOLVED:** historical hosted tap-loss remains **UNKNOWN**; missing past amendments cannot be recovered by this change. Existing archive fallback behavior, parser limitations, terminal-record truncation and general concurrent-writer handling remain outside scope.

L335's source-to-ledger repair is closed with those limits explicit. The earlier [L394 contract-probe repair](2026-09-14_contract-repair-completion.md) remains complete; L392 calibration remains open.
