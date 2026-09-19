# SAM repair reply — independent recheck

**Scope:** Will supplied SAM's follow-up to CATO's five closeout findings. Reviewed SAM repair revisions `eea592b8c`, `33c67e6f7`, and `003e7b14e4e96d5c79ac01608b88e914432dac6a`, unchanged in SAM's working tree at recheck; shared HEAD initially `6afe0cfe7`. Active HANS/PROME/shared-memory changes preserved. No owner edits, messages, launches or grade changes.

**Result: F4 and the consumer-warning portion of F5 verified; F1–F3 partially repaired.** The original stale THESIS and dropped same-day event now trigger the checker, and the consumer brief plainly marks its old reasoning disputed. “All five fixed” overstates the remaining coverage.

[Independent pinned probes](2026-09-19_1257_sam-repair-recheck-probe.py) · [results](2026-09-19_1257_sam-repair-recheck-probe.txt) · [owner suite/current runs and closeout checks](2026-09-19_1257_sam-repair-recheck-checks.txt). Probes use temporary fixtures and the pinned code, including a real orphan advisory from an isolated temporary Git repository. No production fixture or owner file is changed.

## F1 — MEDIUM — scoreboard repair still accepts ordinary wrong claims

**Source:** `AGENTS/SAM/scripts/closeout_check.py:216–243` (lone-count loop and quote guard).

Verified repaired: the actual complete pre-repair THESIS now produces findings; the new three-part parser and unquoted lone-count case work. However, with the current ledger deriving **16/16/1/1**, all of these wrong live claims produce **no finding**:

1. `PREDICTIONS.tsv: 4 OPEN` — at end of line, `after` is the empty string; Python considers `'' in quote_characters` true. A line beginning with the count has the analogous `before` problem. This is a concrete implementation error, not ambiguous interpretation of a quotation.
2. ``PREDICTIONS.tsv currently has `4 OPEN`.`` — backticks format a live claim just as readily as historical prose. Neither quotation marks nor backticks establish retirement.
3. `PREDICTIONS.tsv: 4 OPEN. Scoreboard 16 CONFIRMED / 16 FAILED / 1 special.` — a three-part match causes the entire line's separate OPEN count to be skipped. It is the same split-assertion shape as the motivating defect, after only the first three counts have been corrected.

The genuine historical correction-note control stays quiet. Reading the five suppressed current examples establishes those five cases only; it does not establish the guard's precision for ordinary future live claims.

**Acceptance:** test and detect these three cases while retaining the true historical quiet case. Do not exempt counts merely because they touch punctuation; evaluate the OPEN count separately from a matching three-part scoreboard. An explicit current scoreboard block would avoid inferring assertion status from arbitrary prose.

## F2 — MEDIUM — event counts are improved, but do not establish event agreement

**Source:** checker `:100–168`.

Verified repaired: removal of the September 30 JGB 2Y row now fails C; blank dates in CATALYSTS are explicitly checked. The current CALENDAR yields **23 parsed rows**.

The implementation compares **counts per date**, not identities. Replacing the JGB 2Y calendar event with a different event on the same date leaves both counts unchanged and passes. In the independent fixture the replacement is named JGB 99Y to make the mismatch unmistakable; the failure is identical for any ordinary wrong auction/event name. An added `| TBD | Extra undated live event |` in the forward CALENDAR is also silently ignored. Checking that today's rows all parse does not make the parser reject tomorrow's unparseable row.

**Acceptance:** compare stable event identity/date pairs, with explicit handling for presentation differences, and reject or report unparseable forward event rows. Otherwise narrow the claim to a count-consistency check and retain event reconciliation as manual; do not call this full closure of the original event-agreement finding.

## F3 — MEDIUM — the orphan check runs, but its actionable output is still lost

**Source:** checker `:301–336` and `:382–389`; `scripts/orphan_check.sh:18–19` and its final `exit 0`.

Verified repaired: orphan_check is called; deleting its delegation raises through the new table/list guard; fleet-index and local handoff are no longer confused. H checks local handoff existence/line cap; it does not establish that this session's handoff content was written, which remains a manual obligation.

`run_delegated()` retains output **only for nonzero return codes**, then only the final four lines, each truncated to 150 characters. The actual orphan checker deliberately **exits 0 even when it identifies likely sender-authored uncommitted packets**. In an isolated repository the real script reports `[likely YOURS]` for an untracked from-SAM packet at rc=0; SAM's wrapper drops the entire advisory and reports `ok`. This suppresses the check's intended result, so adding the subprocess call alone does not close the gap. In the live run, other owners' dirty paths likewise produce no visible orphan detail in SAM's wrapper.

Execution failures also remain rc=0/PASS at the parent: an injected delegated ERROR is printed but does not make completion incomplete. The footer does scope PASS to self-checks, so this is not evidence that SAM experienced a real timeout or ignored a known failure. It is an unresolved part of the earlier request for explicit unknown/incomplete execution state.

**Acceptance:** expose or retain the complete advisory irrespective of exit status, with a usable file pointer if condensed. Make tool execution failures incomplete/unknown. Preserve each tool's documented advisory semantics; a normal orphan warning need not become a fatal error.

## Verified closures and remaining adjudication

- **F4 closed:** charter step 15 now says AFTER final commit / BEFORE safe-push. Pre-commit mode skips F/G explicitly and the PASS scope names the skipped checks. The full and pre-commit runs complete successfully on the current clean SAM tree.
- **F5 consumer-warning repair closed on the three named surfaces:** STATUS, NEXUS_BRIEF and the grade record prominently say DISPUTED and no replacement grade. The brief explicitly labels its retained reasoning as the as-published argument under challenge. That is a substantive improvement over simply appending a warning elsewhere.
- **Adjudication stays open:** this recheck does not certify terminal FALSE or assign TRUE. The original CATO review also challenged Episode B's purported untreated-control status and SAM-31's regime convention. Preserve those in the next adjudication; narrowing the handoff to route exhaustion and mean-versus-episode must not silently drop them. The disputed-publication fix does not answer them.

## Verification limits and receipt

The **committed closeout suite contains 19 runnable tests**, all passing, zero skipped. The reported 29 may include additional ad hoc verification, but that total and the 441-input sweep were not independently reproduced from a durable supplied suite here. The pre-commit owner test still checks source strings; the independent recheck also ran both actual modes. Correctly rejecting a source-code grep as proof of bad runtime output is sound; it does not settle the separate parser counterexamples above. No inference about actual runtime output is based solely on a quoted docstring or comment.

The corrected test harness reports missing historical fixtures as SKIP instead of printing PASS for them; no skip occurred here. The present ledger/sidecar and clean-tree checks pass. CPI behavior, proxy re-benchmarking, BOJ pricing and other carried work were outside this assignment.

Suggested next step: SAM handles the remaining F1–F3 counterexamples, then supplies one reproducible verification receipt. Keep the analytical adjudication separate. No new checker, queue or sweep is needed. CATO has not implemented the fixes or sent a packet; the committed report is the shared evidence. Closeout checks and exact-path publication receipt are delivered in-session. Next session: orient and await Will; recheck later changes only when assigned.
