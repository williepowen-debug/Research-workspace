# Independent result re-read 2 — TERRY IDEA ledger guard

Date: 2026-10-25. Reviewer: Codex helper `/root/terry_guard_review`. Exact committed snapshot: `5586d2e2038e5337016de0cdcc121c566ec590a6`. Review 2 of the maximum 3 in this repair episode, authorized by PROME to inspect the F1 correction only. Read the updated committed acceptance/history and `/tmp/prome-terry-guard-review.md` before inspecting/testing. The acceptance records `reads: 1` and identifies the prior PARTIAL result and pending correction read; this report supplies read 2, not an invented plan review. No owner-file edits, commits, external calls or TERRY contact.

**Verdict: 0 blocking findings. F1 resolved within the declared scope.** VERIFIED: normal IDEA INDEX structure cell now reaches G through `gather_live()`, and both exact preserved F1 mutations produce the expected strike disagreement. This is bounded independent verification of the repair, not operational or trading approval.

## Verification and evidence

The changed `index_md_states(..., include_idea_structure=True)` appends normal IDEA `cells[3]` after the existing state text. `gather_live()` invokes that mode. The default extractor and TRY/MGMT extraction remain unchanged. The seven added regressions run `gather_live()` before A/G for normal INDEX strikes, TRADE_BOOK strikes, expiry, matching surfaces and retained state behavior, then check missing structure and legacy extraction. They address the read-1 bypass directly.

Committed snapshot exported into the throwaway Git repository `/tmp/prome-terry-guard-snapshot2`. Inputs come from `git show 5586d2e20:<path>`; the read-1 script was separately exported from `3be3db220` for invariant comparison. Replay:

`python3 -B -W error::ResourceWarning /tmp/prome-terry-guard-tests2.py > /tmp/prome-terry-guard-results2.jsonl`

Observed exit 0, with assertions enforcing these outcomes:

- Normal committed IDEA claim includes `|| QQQ Nov-20 690/670P x2 (card default x1)`; complete committed fixture A/G/H each return `[]`.
- Original preserved complete INDEX input `/tmp/prome-terry-guard-failing-INDEX.md`, applied alone: G reports `INDEX.md=690/665 · TRADE_BOOK.md=690/670` for `IDEA-QQQ-PUTWALL-OCT22`. A remains clean.
- Original preserved complete TRADE_BOOK input `/tmp/prome-terry-guard-failing-TRADE_BOOK.md`, applied alone: G reports `INDEX.md=690/670 · TRADE_BOOK.md=690/665` for the same ID. A remains clean. Because this exact old file also restores the old abbreviated USO year label, G additionally reports `Jan-15-2027` versus `Jan-15` for the USO IDEA; that is expected detection, not ignored test output.
- Normal INDEX expiry changed from Nov-20 to Nov-27: G reports the expiry disagreement through the reader path; A remains clean.
- Matching inputs stay clean; absent structure is not invented. TRY/MGMT live-mode state extraction equals the prior extractor, and default extraction of the full committed INDEX equals the prior extractor.
- Syntax-level AST comparison confirms unchanged operative functions: `strip_history`, `state_of`, `check_state_agreement`, `fingerprint`, `check_structure_agreement`, `paper_live_counts`, `counts_in`, `contract_count_findings`, `_own_row`, `check_contract_counts`. STATES, COMPATIBLE, strike/expiry regexes and all count regexes also compare equal. Thus the F1 correction does not change the tested A/H policies established in read 1.
- Committed TRADE_BOOK's USO `Jan-15-2027` now agrees with the existing card and INDEX. The inspected commit diff changes the explicit year label; it does not change the declared instrument's expiry.
- Corroboration: the exact committed script's `selftest()` returns 0 with 118 PASS assertions. Output preserved separately at `/tmp/prome-terry-guard-selftest2.txt`; original read-1 artifacts were not overwritten by this review.

Probe source and full observations: `/tmp/prome-terry-guard-tests2.py`, `/tmp/prome-terry-guard-results2.jsonl`.

## Disposition and retained limits

IMPLEMENTED, TESTED and INDEPENDENTLY VERIFIED within the stated IDEA namespace/normal INDEX-versus-TRADE_BOOK structure boundary. STILL UNRESOLVED: no blocking item in that boundary. Read 1's disclosed legacy limits remain: no universal card/TSV/all-surface structure completeness; first-mention/two-assertion behavior and count-present policy are unchanged; no broker truth or transactional/concurrent live-read guarantee. These are not new repair obligations. No third read or additional helper work is needed for this result.

## COMPLETION — TERRY GUARD REVIEW — 2026-10-25
STATUS: ✅ DONE
CHANGED: /tmp/prome-terry-guard-review2.md, /tmp/prome-terry-guard-tests2.py, /tmp/prome-terry-guard-results2.jsonl, /tmp/prome-terry-guard-selftest2.txt, /tmp/prome-terry-guard-snapshot2/
RESULT: Read 2 of exact snapshot 5586d2e2038e5337016de0cdcc121c566ec590a6 found 0 blocking findings; both preserved F1 mutations fire and 118 selftest assertions pass.
GAPS: No unresolved blocker in the bounded repair scope; retained policy/coverage limits are stated above.
WILL_NEEDS: None.
FOLLOW-UP: PROME to persist review 2 and its disposition in the owner receipt; helper work is complete and closed out, with no further task pending. No operational approval given.
