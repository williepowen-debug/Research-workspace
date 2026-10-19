# WALTER bookmark continuation — independent result review

Status: VERIFIED blocking defect; repair not installed. Review helper `/root/walter_bookmark_result`, explicitly selected gpt-6.1-sol/Codex. One result read of the October19 continuation episode; no owner edits or live API operations. All seven files in the owner's verification.json matched implementation6c89f1a2c and saved hashes. The57 existing offline tests passed.

**HIGH: exact staged IDs are not bound to continuation.** `AGENTS/WALTER/tools/x_bookmarks_workflow.py` stage() hashes only next_token bytes. proposed_checkpoint() checks that hash but not staged IDs. Scanner mark accepts a newly completed review matching a damaged stage and advances the original cursor.

Independent disposable-fixture reproduction: scan synthetic0…500 (stage0…499,cursor500); remove499 from pending.ids without changing timestamp/checkpoint hash; create a fresh valid review for remaining499IDs; mark succeeds; scan/review/mark500; scan_complete becomes true; next all-seen first page ends traversal while499 remains unconsumed/unreviewed. The defect requires a damaged/edited stage: no spontaneous deletion in an ordinary crash was demonstrated. It violates the existing §10 exact-ID/corrupt-state contract.

Repair at owner: bind proposal to the exact staged ID set and stage identity, validate before seen writes/cursor advance, and add this regression. Preserve the checkpoint's own byte binding, legacy behavior only where explicitly allowed, interrupted-mark ordering, cap and credential/body isolation. A missing binding on a new continuation must refuse or conservatively restart; do not silently treat it as a safe legacy stage.

Three other independently devised cases recovered safely: crash after cursor commit before receipt; loss of both seen/continuation; expiry after successful resumed pages. Original local reproduction: `/tmp/bookmark_independent_review.py`; precise counterexample above is durable and sufficient to rebuild it. Scanner SHA256 ea5c9b7642cd1c95430b676b6a59b009597dd42bd9375b0f11f0ac179b7ebcbe; workflow49ab565fa7d158ac4b7b566ea7db376b09f826d58f89a32a7acab8404be23da1.

First substantive owner contact: none. Native read_thread of01a154ec-5479-76c0-bcd2-abf9d66a523d returned notLoaded and the completed full-closeout/partial-coverage receipts. No owner resume or live scan was requested. A durable PROME-authored packet carries this finding for the next owner session. No other live owner absence is inferred. Live pagination and WQ458 renewal remain separate.

Reviewer closeout confirmed: all findings delivered, no workspace writes, no remaining assignment. IMPLEMENTED: owner’s original repair only. TESTED:57 original tests plus four fresh probes. INDEPENDENTLY VERIFIED: defect established; repair acceptance withheld. STILL UNRESOLVED: exact-ID binding and subsequent required live verification.
