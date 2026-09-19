# SAM closeout build — independent review

**Assignment:** Will asked CATO to check SAM's reported closeout build and accompanying correction/handoff. **Reviewed revision:** `12c399ce5735977ca36b29f939a2e29553743322`; build `c327b78599c1890c0c3dbd540772fb5b83ee8f7f`, correction `25a15d470`, final brief `12c399ce5`. SAM paths remained unchanged through the review recheck; PROME committed concurrently. Other owners' dirty paths were preserved. No SAM edits, grade changes, peer sends or agent launches.

**Assessment:** useful structure, but not ready to support the claimed breadth of verification. All nine supplied tests and the current checker pass. Independent counterexamples nevertheless reproduce failures in the very checks meant to prevent stale scoreboards and divergent dockets. The grading challenge is preserved in the handoff but not honestly reflected in the peer-facing conclusion.

Evidence: [pinned counterexamples](2026-09-19_1230_sam-closeout-probe.py), [results](2026-09-19_1230_sam-closeout-probe.txt), [test/checker and closeout receipts](2026-09-19_1230_sam-closeout-checks.txt). Probes load the reported revision using `git show` and use temporary fixtures/mocks; they do not mutate owner files. Passing these probes means the reported gaps reproduced, not that a repair passed.

## R1 — MEDIUM — the original stale THESIS escapes the scoreboard guard

**Source:** `AGENTS/SAM/scripts/closeout_check.py:157–168`.

D recognizes only one uninterrupted four-field sequence: `N CONFIRMED / N FAILED / N special / N OPEN`. Missing files or no matching assertion are silently accepted. The actual pre-repair THESIS at `22e55db36^:AGENTS/SAM/thesis/THESIS.md:316` says **4 OPEN as of 2026-08-27** separately from **14 CONFIRMED / 14 FAILED / 1 special**. Restoring that actual file against the current ledger produces **zero D findings**, despite derived counts **16/16/1/1**. A synthetic full-format incorrect scoreboard is detected, confirming that the blind spot is parsing/coverage.

**Correction/acceptance:** recognize the supported live count assertions separately or designate explicit machine-readable current scoreboard blocks and report missing/unparseable expected blocks. Preserve dated correction quotations as history. Add the actual stale THESIS regression, not just a synthetic four-field string. The claim that D prevents the original 23-day drift is currently unsupported.

## R2 — MEDIUM — docket agreement means dates only, and undated rows disappear

**Source:** `AGENTS/SAM/scripts/closeout_check.py:82–128`; SAM `CLAUDE.md:72` requires the two dockets not diverge.

C reduces both files to **sets of dates**, losing event identity and multiplicity. Deleting the current September 30 JGB 2Y auction from CALENDAR leaves the BOJ purchase-plan event on that date; **A/B/C all still pass**, while CATALYSTS retains the auction. This is an internal consistency failure, not an argument that software should discover missing external events. Same-day collisions already exist in ordinary current data.

`_catalysts()` also silently drops rows with an empty date. Appending an undated event produces no finding even though boot step 3 explicitly requires undated/past rows to be pruned. CALENDAR rows outside its one accepted date syntax likewise have no explicit unparseable-row disposition.

**Correction/acceptance:** compare stable event identities plus dates, allowing documented presentation differences; validate forward event rows rather than dropping unparseable/missing dates. Test a removed same-day event, undated rows and the existing resolved-block quiet case.

## R3 — MEDIUM — the delegation receipt overstates coverage and hides evidence

**Source:** `AGENTS/SAM/scripts/closeout_check.py:56–71,210–233,266–271`; `scripts/check_memory_length.sh:12–13`.

- The table labels root 1b **DELEGATED orphan_check.sh**, but the four-command `DELEGATED` list never invokes it. It is also absent from the final MANUAL list. The displayed coverage is false.
- Step 14 labels local SAM handoff maintenance delegated to `check_memory_length.sh`. That script reads **root `memory/auto/MEMORY.md`**, not `AGENTS/SAM/MEMORY.md`; even a local size check would not prove a session handoff was updated. The shared memory guard can be useful, but is mapped to the wrong obligation.
- Child stdout/stderr are captured then discarded. The runner instructs the user to “read that tool's own output” without exposing it or saving its location. Our wiring probe makes every child return rc=2 and a diagnostic: the parent exits **0/PASS**, prints the rc values, and hides the diagnostic. Exceptions/timeouts are likewise only returned as display strings, not structural problems.

The PASS footer **explicitly scopes itself to the self-checks**. This is not proof that SAM's actual delegated tools failed, nor a claim every nonzero advisory must block. The observed current run returned 0/0/0/1, with the ledger tool's explanation hidden. The problem is the misleading coverage map and unusable disposition evidence.

**Correction/acceptance:** actually call the orphan advisory or mark it manual; label handoff content manual and distinguish the shared memory cap. Expose/store child output and give execution failures an explicit incomplete/unknown result. Interpret each tool's documented warning/failure semantics; do not globally equate nonzero with failure or success. Test missing tool, timeout, advisory and critical failure paths.

## R4 — MEDIUM — the documented invocation phase contradicts the gate

**Source:** SAM `CLAUDE.md:77–80`; checker `:186–207`.

Step 15 says to run the checker **before the final commit**, after required write-backs. G fails for any uncommitted SAM path, including a legitimate freshly written STATUS or brief. F checks only committed history, so it cannot validate the pending final write-back at that phase. The clean current snapshot passes after commitment; that does not validate the prescribed workflow.

**Correction/acceptance:** make the final clean-tree/committed-order verification explicitly post-commit, or offer separately named pre-commit and post-commit phases. No numbering change is needed. Test an ordinary pending write-back followed by its exact-path commit and final verification. F does implement the charter's stated timestamp comparison; this review does not substitute a different ordering policy.

## R5 — HIGH — unresolved grade challenges remain categorical in the consumer brief

**Source:** SAM `MEMORY.md:51–58`, `NEXUS_BRIEF.md:21`, `docket/2026-09-19_SAM28_SAM31_GRADE.md:85`; original [CATO R4](2026-09-19_1148_recent-updates-review.md#r4--high--sams-firm-false-grades-exceed-their-unresolved-episode-evidence).

The session-count correction is real and visible. The two unresolved questions are explicitly TIER 0 and the packet remains in inbox. Keeping a substantive adjudication out of a rushed closeout is reasonable.

However, the brief still says the new measurement **“settles it”** and the Episode-B control **“carries the grade”**, calling September a move with **“no eligible route at all.”** The earlier review separately challenged that control: its intervention attribution remains OPEN, and even an established untreated analogue would not prove Episode A lacked an intervention effect. That challenge is not answered by fixing the weekend count. The handoff also declares SAM-31 leg 1 “untouched” and sufficient before its proposed check; CATO had explicitly retained the regime-convention question.

**Correction/acceptance:** mark the affected consumer conclusion as disputed/pending adjudication now, without silently changing the underlying prediction or scoreboard. Carry the Episode-B treatment-status/causal-inference challenge into the owner's review, alongside route exhaustion and mean-versus-episode. Assess SAM-31's regime convention independently. “CATO does not assign TRUE” must not become “CATO endorses the unchanged terminal FALSE.” This review does not assign a replacement grade or reopen the trading frame.

## Test and process claims

The nine tests pass, including the real pre-repair docket fixture. They exercise A–E; they do **not** test F, G or child-process behavior. The described “end-to-end” historical test calls `check_docket()` only, not `main()` or its delegates. If its history fixture cannot be read, it returns after printing SKIP and the outer harness prints PASS; that branch did not occur in this checkout. Expand the evidence before saying each of seven checks is proven to fire.

Keeping step numbers is sensible. The stronger causal story about the skipped duty is unproven: write-back step 10 already explicitly said to prune and synchronize, so the duty was not discoverable only in boot. Consolidating the presentation may help; the available artifacts do not establish “not inattention” as the exclusive cause. Avoid treating a workflow hypothesis as a demonstrated root cause.

## Disposition and next step

Independent review complete; **no owner repair implemented**. Suggested next step: SAM corrects R1–R4 and demonstrates the counterexamples now fail appropriately; separately it marks the disputed grade conclusion on consumer surfaces and adjudicates R5 against the original conventions. No extra checklist or renumbering is necessary. Will has not assigned CATO implementation or delivery to owners. This committed report is the durable shared-repository copy; no inbox delivery is claimed.

CATO closeout checks and publication outcome are recorded in the companion checks file and final in-session receipt. Next CATO session: orient and await Will; recheck owner revisions before any assigned follow-up.
