# Integration validation — September 8 ET / September 9 JST

- BOJ tests: 10 passed. Primary image/page fixture, positive curve extraction from reviewed transcription, stale/future/expiry, changed image/error HTML, arithmetic/nonfinite values, truncated/duplicate terms, method/layout drift, same-vintage conflict, idempotency, no-write and failure behavior. Test receipt: `ois-tests.txt`.
- Live read-only validation succeeded at 2026-09-09 03:10:05 UTC. First ingestion at 03:10:34 UTC wrote five rows. Subsequent live verification wrote zero; see `ois-live.txt` and the ledger's source/pull clocks. Quote vintage: September 9 11:15, JST assumed. The fixture original is hashed in `sources.json` and the review JSON.
- Boot inventory: exit 0, 19 operational tools / 14 boot-wired / five declared manual tools. Regression tests are excluded from the market-tool inventory; see `tool-inventory.txt`.
- Strict `csv.reader(..., delimiter='\t', strict=True)` on KB: 170 records including header, nine fields each, unique IDs. Three malformed quoting rows fixed in a separate cleanup commit; only 209's analytical meaning was consolidated afterwards.
- All ten before-images match `0670d96e2` byte for byte. PREDICTIONS, PREDICTIONS_ARCHIVE, TRADE, old BOJ_OIS, FLOW and VX match that commit unchanged. New Markdown links in changed owner docs and the integration report resolve locally.
- Read cap: STATUS 31,489 bytes / 187 lines; MEMORY 21,137 bytes / 94 lines. Both within SAM/root limits. Weekday checks pass for STATUS and the paired docket. No forward dates or frozen prediction terms changed. Read-cap checker flags STATUS as rotation-tier but under budget; the outgoing session was archived rather than active obligations removed.
- Live-document `git diff --check` is clean. Staged artifact check preserves an intentional exception: the original KB before-image ends several rows in a tab representing its empty ninth field; stripping those tabs would corrupt the archive. Other newly copied tool receipts have terminal blank lines normalized. The outgoing STATUS block remains verbatim with an explicit archive-end marker.

## Consumer-scan dispositions

The 97→98 scan is filtered by the Totan series. Initial self scan reported seven apparent stale matches: NEXUS and the candidate needed the current source reference; both are refreshed in this integration. The catch-up report and its validation receipt are correctly dated September 8 observations, and three more hits are verbatim before-images. Those historical records remain unchanged. Non-Totan 97 matches are unrelated candidates, not stale quote findings.

Peer scan found no series-confirmed Totan quote needing correction. The exact withdrawn “FUNDING VIA REPO, NOT SALES” scan found a WALTER SESSION_LOG paragraph: inspected in place, it explicitly describes SAM's retraction and labels the funding unresolved. It is a preserved August correction, not a current claim of FIMA use. The self hit is the intentionally frozen original KB before-image. No peer file changes or messages were warranted.

Receipts: `consumer-ois-self.txt`, `consumer-ois-peers.txt`, `consumer-funding-self.txt`, `consumer-funding-peers.txt`. They preserve the initial scan before final NEXUS/candidate reconciliation so the disposition can be audited; raw red counts are not a count of unresolved live claims.

## Limits

New Totan images require SAM visual review; no unattended image decoder. No fresh-session operator judgment eval or full market boot was run for this integration. Independent intervention broker baseline, post-move positioning/funding and upcoming policy outcomes remain open source dependencies. Shared pull/push is deferred while other agents have uncommitted work; all commits are explicitly scoped to SAM.
