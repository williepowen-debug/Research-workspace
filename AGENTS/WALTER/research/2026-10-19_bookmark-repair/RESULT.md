# Bookmark workflow implementation — 2026-10-19T18:01:12Z

**Authority:** Will directly requested implementation of the four practical improvements. OpenAI/Codex0.163.0,gpt-6.1-sol; same independent WALTER owner/session01a154ec-5479-76c0-bcd2-abf9d66a523d at repository root/home/willi/Research-workspace. Bounded code/workflow repair; no pilot renewal inferred.

**Status: IMPLEMENTED and AUTHOR-TESTED. Independent review PENDING; live pagination verification PENDING.** The existing acceptance spec requires an independent read before a working/verification claim. No independent reviewer is attached or launched in this terminal; a concrete review request is delivered to PROME. Author tests do not substitute for that read. Prior base-reader live OAuth/API checks remain historical evidence, not certification of this change.

## Delivered behavior

1. Capped scans retain an opaque continuation and their pre-traversal seen baseline. Marking500cannot turn that prefix into a stop condition for the remaining tail. Migration from a legacy ledger and recovery after missing local state audit the returned collection conservatively. Rejected cursor fails loud and prepares a restart; rate-limit/network failures do not mark IDs. The50rows/page and10bookmark-read-attempt budget are unchanged.
2. Stage advancement follows reviewed marking, not fetch. Cursor proposals are hash-bound to the stage. Seen is written atomically before cursor advance; retry after an interrupted mark is idempotent. Zero-new-ID segments can advance without a content review. Synced seen data adds only a boolean completion guard; cursor/baseline sidecars are local and ignored under the existing *_token.json rule.
3. New stages need an exact-ID review: disposition and fully_read/partly_read/unread labels. These are WALTER attestations. Partial/unread material DISPATCH/FOLD requires an existing follow-up artifact or a specific missing-content request. Unread cannot be KILL; a missing-content request cannot masquerade as fully_read. Templates are create-only and bound to the exact scan timestamp. Historical stages remain usable with reading status explicitly unrecorded.
4. Receipts distinguish fetched from reviewed, show reading/disposition counts, preserve follow-ups/selected requests and report incomplete/resumed coverage. A resumed tail does not claim this run inspected new head items. Auth-only output says no scan occurred. Receipt/template commands neither fetch bookmarks nor read credentials.
5. Setup/operator instructions keep article bookmarks normal, explain selective screenshots/text requests and direct urgent/reconsideration links to the WALTER conversation. Source retrieval/vision remains a session step; no automatic reading is claimed. Will need not prepare JSON, add tags or run commands.

## Evidence

57offline tests passed:32existing A-row/enrichment/isolation tests plus25workflow tests. Both direct test scripts and unittest discovery pass; discovery ran with ResourceWarning promoted to error. Core/companion version guard PASS; read-cap check PASS for its declared scope. Exact file hashes and ignored-path/unchanged-production-ledger proof: verification.json. Full test outputs: tests.txt, legacy-tests.txt, workflow-tests.txt. Python compilation passed.

Functional regressions exercise actual scan→review-template→mark flows with synthetic pages:501items→500then1;1001→500/500/1. Other cases: legacy seen prefixes, local cursor loss, rejected cursor/restart, fresh head additions during continuation, no-mark retry, crash after seen write, stage/proposal tampering, wrong IDs/new stage timestamps, unread/partial follow-up, missing review, bad/future timestamps, duplicate page IDs, HTTP401withsamecursorandbudget,429/network failures, corrupt continuation and absence of source bodies/credential values in persisted fixture records. These are author-run tests, not an independent counterexample review.

## Limits and remaining work

No live bookmark API request, authorization, mark, seen/stage mutation, new source measurement, L599 rerun, paid feed, unattended task, external message, financial threshold/band/trade change or main-repo pull/stash/reset/push. The production seen/stage diff is empty. This modifies workflow code and documentation only.

Next authorized use needs the independent repair review and a human-watched live check. WQ458 remains a separate unrenewed pilot decision. Cursors are opaque upstream state, not a consistent snapshot guarantee: remote additions/removals/reordering may affect them; live cursor lifetime/semantics remain unverified. Review should challenge crash/file ordering, cursor expiry, collection mutation, legacy migration and truthful receipt coverage. The first upgraded scan may spend its bounded budget on old already-seen pages to establish missing historical coverage;0newIDs may still mean older coverage incomplete. No claim made that the earlier live queue was affected by the original cap defect.

The transport follows X’s [documented next-token pagination](https://docs.x.com/xdks/python/pagination) and existing [bookmarks endpoint](https://docs.x.com/x-api/users/get-bookmarks). Those references do not certify cursor lifetime or a changing-list snapshot.

During implementation, three OTTO owner packets arrived: readiness, CATO-OR1 correction and forecast repairs. Packet bodies read to identify the supersession chain; source-report validation/routing remains separate pending desk work. They were left unconsumed. This repair does not claim the desk inbox is empty or re-grade those forecasts.
