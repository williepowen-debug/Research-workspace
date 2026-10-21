# L736 follow-through — independent remedy and prior post-review code read

Reader: `/root/l736_review`, Codex/OpenAI, inherited runtime; 2026-10-20 ET. Read-only repair reviewer under UPGRADE_PROTOCOL4/4a/4b and COMPLETION_SPEC minimal-reviewer exemption, not a full desk boot. Git root explicitly resolved `/home/willi/Research-workspace`; root CLAUDE/AGENTS/USER and local CLAUDE/OPERATIONS read, review clauses and runtime exemption inspected. Shell/Python available; no missing dependency for these probes. Combined instruction/acceptance output initially truncated; bounded relevant ranges recovered. This is not a claim to have read every startup surface.

Reviewed baseline: HEAD `c16eba75b74a5bfee76fc91de38b067b27de33c4`, `scripts/orch_log.py` SHA256 `31b72d9a5db4545ff9f65bc19e695a7e60a6f38225f5435de1b1ddacf09e6d82`. Scope: implementation lines1–410 and510–558; existing selftest middle not audited wholesale. Canonical inputs: processed PROME October15 writer-three-defects packet; `runs/2026-10-20_TOOL_REPAIRS.md` writer section; full `runs/2026-10-20_L733_ORCH_LOG_INDEPENDENT_READ.md`; PROME L733 acceptance A1–A9 and residue; DOCKET.tsv line736; PROME gate lines1594–1637; tests lines1–115; CLOSEOUT and ORCHESTRATION_PLAYBOOK invocation sites from targeted search. No production ledger, view, source, or other desk files changed.

## Independent counterexample before verdict

A false repaired verdict would be refuted if a CLI append started while rotate has replaced the hot inode but is still rendering the view can finish before that render, lose its row, or observe a stale count; likewise if a CLI view rendering concurrently with append leaves stale count. A comment/header-shaped date that writes invisible data, or an empty-note acknowledgement ending with a separator, refutes the other two claims.

My fresh harness `/tmp/daedalus_l736_review.py` imports the actual source in separate child processes, delays `render_view` one second, signals readiness with a temp marker, then starts a real CLI append. Fixtures/results: `/tmp/l736-independent-3zvqf32p/results.json`. Initial harness invocation had an argv construction bug and failed before the ready marker; corrected invocation below succeeded. This harness issue was not a product finding.

| Prior finding | Independent observation | Verdict |
|---|---|---|
| R1 new hot file born locked | Rotate held at render after hot replacement; racing append waited1.004s; rotate0/append0; RACER retained once; hot/view counts2/2 | VERIFIED |
| R2 public view under writer lock | View held at render; racing append waited1.009s; view0/append0; RACER retained once; counts3/3 | VERIFIED for public CLI and cooperating writers |
| R5 invisible date/row count | `#x`, two-space-prefixed `#x`, and `date` each refused2 with ledger bytes unchanged; inspected post-write rows+1 assertion | VERIFIED for named shapes and assertion; not general date-schema certification |
| R8 separator | One hand row followed by exact ack1 and empty notes → append0; notes exactly `ACK-UNOBSERVED 1` | VERIFIED |
| Remaining R3 view absorption | Valid hand row raises ledger2→3; ordinary CLI view returns0 and rewrites header count3 | STILL PRESENT at reviewed baseline |

## Accepted minimal remedy for L736 item7 (pre-implementation)

The canonical row permits **view refuses OR requires acknowledgement**. Prefer refusal-only public `view`, avoiding a new growing acknowledgement record. Existing append acknowledgement records the delta in a genuine new ledger row.

1. Under existing `_locked_open`, validate the ledger before doing any write. Read the previous view header count while holding that same lock.
2. Missing view: allow initial generation and explicitly report first use. This exception does not establish provenance and stays disclosed.
3. Bad/unparseable view or view ahead of ledger: refuse2, preserving ledger/view. There is no trustworthy positive delta to acknowledge. Owner repair of malformed/ahead inputs is separate; do not suggest deleting a view to bypass refusal.
4. Equal counts: regenerate normally. A nonzero `--acknowledge-unobserved` on view should refuse instead of silently ignoring a flag that appears to certify acknowledgement; absent/0 may be accepted as no-op.
5. Ledger count rise: refuse2, name both counts and delta, direct owner to identify rows and use **a legitimate next append** with exact `--acknowledge-unobserved K`, never fabricate a ledger event solely to reset the view. Reject wrong ack/no ack before any mutation.
6. Keep `write_view` as the trusted internal projection used under append/rotate's existing lock. Guard the public command in a separate wrapper; moving the count guard into the primitive would reject deliberate append/rotation count changes. Document that direct internal calls are not public guarded CLI.

ACCEPTED remedy under4a for that bounded contract. Result implementation still requires review. Tests must watch refusal and clean lines, prove both files unchanged on refusal, cover missing/bad/ahead/equal/rise, and show exact append acknowledgement followed by view succeeds. Existing race probes must still pass.

## Consumer effects and remaining limits

- PROME gate `check_orch_log_observed` currently tells users `check`, then `view` on count rise, malformed header, and count decrease. Those remedies must be updated by PROME; acceptance A5 and `test_A5_hand_row_then_view_passes` currently use the unguarded internal primitive and will not prove the public CLI fix. Keep that internal behavior test only if explicitly relabelled and add a public-boundary refusal test. `test_LIMIT_hand_row_absorbed_by_a_later_writer_append` already pins superseded append behavior and needs owner revision.
- Routine view at registration/consumption (L675 item1) must account for the refusal. A writer append whose view failed may also cause a count rise: wording must say unobserved rows, not assert all were hand entered. No caller may automatically acknowledge or fabricate an event.
- `rotate` still regenerates from the entire ledger and can absorb prior hand rows; this minimal public-view repair must not claim to close that route. Direct Python `write_view` remains trusted/internal, also not a provenance guard.
- Count-only mechanism cannot detect net-zero hand edits; header source comparison remains PROME-owned; missing-view first use remains exception. Prior R7 rotation-on-postheader-comment exception remains outside this fix.
- These results close the named prior POST-REVIEW verification gap and accept one minimal remedy; **they do not close full L736**, PROME-owned items, or all L733 evidence/provenance limits.

REVIEW: required — guard scope; scope source ranges and callers above; reader `/root/l736_review`; disposition VERIFIED R1/R2/R5/R8, ACCEPTED bounded refusal-only remedy, RESIDUE as listed. Any subsequent implementation is POST-REVIEW until separately checked.

## Final implementation review (same reader, subsequent pass)

Reviewed final source delta `guarded_view` and `main` CLI dispatch, acceptance `design/2026-10-20_L736_VIEW_ACCEPTANCE.md`, and seven-test source `scripts/tests/test_orch_log_view_L736.py`. Reviewed tool SHA256 **e84f5601735ab85a97931d4c2b57f1f62e7d2b81ef9119f1f0ae5d87f1429aac**. No source edits by reader. The accepted refusal-only remedy is implemented at the public command boundary; internal projection remains unchanged.

Independent final probes: `/tmp/daedalus_l736_result_review.py`, fixtures/result `/tmp/l736-independent-pn1k3r1d/`. Real CLI count-rise refusal returned2 and preserved both files byte-for-byte. CLI equal and missing returned0, with missing explicitly reporting no provenance; malformed header, ahead, nonzero ack and invalid ledger each returned2 and preserved existing files. Exact CLI append acknowledgement1 then CLI view returned0/0 and persisted `ACK-UNOBSERVED 1` in the ledger. No fabricated event was written outside synthetic fixtures. Printed clean and refusal lines were observed, not inferred from rc alone.

Races rerun on final code: rotate rendering after replace blocked append1.005s (0/0, counts2/2); public view rendering blocked append1.023s (0/0, counts3/3); racer retained exactly once. Prior R5 date probes still refused without mutation; R8 still produced exact separator-free acknowledgement.

**VERDICT: ACCEPT bounded implementation.** No new defect found in reviewed delta. R1/R2/R5/R8 verification and public-view count-rise hole are independently verified. Consumer caveats and all remaining limits above remain binding: PROME must update public-command repair guidance and tests, internal helper tests do not certify guarded CLI, and full L736 is not closed. Source header usage/help still describes view as regeneration without its new refusal policy; nonblocking documentation refinement is to name the guarded behavior there (not a basis for calling count equality provenance).

REVIEW: required — guard scope; scope `scripts/orch_log.py` final delta and CLI dispatch, new test source and acceptance above; reader `/root/l736_review`; disposition ACCEPTED implementation, RESIDUE existing consumer/provenance limits, no post-review source fix included in this verdict.
