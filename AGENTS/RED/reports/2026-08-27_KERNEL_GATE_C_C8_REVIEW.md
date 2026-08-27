# KERNEL Gate C — C8 Post-Closeout Review (pilot LIVE-2026-0001)

**Reviewer:** RED (Will's pick from the ruled RED-or-DAEDALUS pair; PROME built and ran the pilot and per the 8/26 ruling cannot review it)
**Date:** 2026-08-27, review executed ~17:2x–17:5xZ (S36)
**Object:** `KERNEL/GATE_C_C8_CLOSEOUT_PACKET_2026-08-27.md` (`ca348e4a5`, amended `82fdb902b`)
**Method:** re-derive everything; accept none of PROME's framing (their own instruction, honored). Every check below was re-run by this desk against the tree, the commit graph, origin, and the tools themselves — not read off the packet.
**Deliverable:** continue / pause / remediate / end recommendation **to Will**.

**Disclosures, so they cannot surface later as omissions:** ① RED is named `independent_verifier_actor_id` inside Q-…033 — a resolution-time role (post-2027-01-01) with no bearing on this process review, disclosed anyway. ② RED performed the C7 adversarial review; this is continuity, and it is why the assignment routed here.

---

## 1. Verdict

**CONTINUE** — with six remediations required before the next sitting (§5). None of them touches code except one test fixture; none invalidates this pilot's results.

**Basis:** every claim in the packet that is re-derivable was re-derived and held. The two integrity properties — additions-only on protected paths and deterministic view reproduction — were **re-run independently by this desk today and both PASS**, including additions-only extended past the packet's range out to the current HEAD. All six frozen-input hashes re-verified byte-exact. All timeline stamps match the commit graph. The kernel commit is exactly the six declared paths, 60 insertions, zero deletions. The submission files hash-match the activation pins, the runbook pins, and the staged rehearsal copies — three independent surfaces, one value. Fail-closed demonstrated itself live, and against the custodian's own document, which is the strongest possible form of that demonstration.

**What would have changed the verdict:** an additions-only failure anywhere in the extended range; any evidence the diagnostic third apply wrote to the events path; any deviation acted on without an operator ruling that had integrity effect. None found.

---

## 2. What was re-derived and held (packet §§1–2, 4–5)

| Claim | My re-derivation | Result |
|---|---|---|
| Timeline stamps (9 rows) | `git show` on all 7 commits; author/commit stamps | **exact match** (16:28:00 → 16:56:39Z) |
| Kernel commit = 6 paths, additions only | `git show --stat 01478b659` | ✅ 6 files, 60 insertions, 0 deletions |
| Submission hashes = activation pins | `sha256sum` both CMD files vs activation JSON vs runbook vs `rehearsals/c7_staged_submissions/` | ✅ byte-exact, 3 surfaces agree |
| Policy pins (actors / capability-grants / custody-policy) | `sha256sum` today | ✅ all three still byte-exact |
| Source commit `1d940042…` present, ancestor of submission | `git cat-file -e` + `merge-base --is-ancestor` | ✅ both |
| Events well-formed, in-window, SHADOW | read both EVT files: `recorded_at=16:32:16.852694Z`, `writer_id=PROME`, `authority_mode=SHADOW`, `stream_version=1` | ✅ |
| 0 rejected receipts | `KERNEL/audit/` does not exist | ✅ consistent (created only on rejection) |
| `check-views` PASS | **re-run by RED 17:26Z** at the committed stamp | ✅ **PASS** |
| `additions-only` PASS over `cb8979041..01478b659` | **re-run by RED 17:27Z**, then extended to current HEAD | ✅ **PASS both ranges** |
| D5 ancestry (4 early commits at origin mid-sitting) | `merge-base --is-ancestor` vs `origin/master` for all four | ✅ all four at origin *(arrival TIME is not re-derivable from ancestry; PROME's mid-window claim accepted as consistent, not re-proven)* |
| Burden: 5 commits + packet, 2 sessions | commit graph | ✅ consistent |

**Discrepancy dispositions D1–D5: CONCUR on all five** — each is real, none was silent, and each disposition matches the durable record where one exists. Judgments PROME asked of this desk specifically are in §4.

---

## 3. New findings — items the packet's "complete list" missed

Severity order. None is integrity-touching; all are process/spec/evidence findings.

### N1 — MODERATE · The committed views are the *diagnostic third apply's* output, and the diagnostic ran before Will's ruling
The committed views carry `render_as_of=16:32:47.037821Z` — the diagnostic apply's stamp, not step 5's (16:32:16). The sitting rule is *"any stop condition on screen ⇒ stop, preserve, no disposition without Will."* The step-6 stop condition appeared at 16:32:25; the diagnostic apply ran at 16:32:47; Will's PROCEED came ~16:35. **A third live apply is neither "stop" nor "preserve" — and it overwrote the run-2 views that fired the stop condition**, leaving the run2-vs-run3 diff only in an ephemeral scratchpad. Integrity is unharmed (events proven idempotent; views deterministic — my `check-views` re-run proves the committed bytes reproduce). But the packet records the diagnostic as a timeline row without recording that (a) it was an unplanned live apply pre-ruling and (b) its output is what got committed. Step 6's criterion also has a *second* defect beside D3: "zero new writes" is violated by design on every retry (views re-render). **Remedy → §5.3.**

### N2 — MODERATE · No durable transcript of the sitting exists, and the session holding the evidence crashed
The packet's evidentiary base says *"every claim cites a commit, a tool transcript line, or a Will ruling."* Five timeline rows cite the transcript or a scratchpad diff. **Neither exists as an artifact**: `KERNEL/rehearsals/` holds a durable transcript for the C6 *rehearsal* but nothing for the live pilot, and PROME's session — the only holder — crashed after the sitting (`f2306d8d5`). Every *outcome* those rows describe was re-derived by me and held, so nothing rests on trust today; but the exact refusal string at 16:31:23 and the one-line-per-view diff are now permanently unverifiable. The live pilot — the record that matters most — got weaker evidence preservation than its own rehearsal. This also subsumes the minor point that D2's refusal has no machine artifact (preflight refusals precede command processing, so no receipt is due by design — with a durable transcript that evidence gap closes itself). **Remedy → §5.4.**

### N3 — LOW-MODERATE · The activation was never revoked; closure is passive — and the "expired" claim was written while the window was still open
At review time (17:26–17:44Z) the activation was **still valid**: `revoked_at: null`, window end 18:00:00Z. Verified live — the tool accepted my read-only invocations under it. Both the assignment packet (~16:5xZ) and RED's own S35 board_log row said the activation *"expired at its own 18:00Z bound"* — a future bound written in the past tense, ~70 minutes early (the dated-carry class, and this desk repeated it, logged against RED). Practical exposure was near-nil: `writer_id=PROME` binds the writer, and nothing ran. But the runbook's step 9 *declares* "nothing further runs" without any mechanism — no revocation step exists, so for ~70 minutes a valid live grant sat open with the custodian's session crashed and no one attending. Fail-closed design should close the window affirmatively, not by clock-lapse plus good behavior. No action needed on LIVE-2026-0001 (it lapsed at 18:00Z). **Remedy → §5.3.**

### N4 — LOW · The pilot broke its own test suite, and the packet's "212 green" is a pre-sitting vintage cited post-sitting
Re-run by RED: **1 failed, 211 passed.** `test_prepare_pilot::test_disposable_clone_gets_only_two_canonical_commands_and_ephemeral_manifests` clones the **live repo** into a temp mirror and `prepare()` writes the two commands with exclusive-create (`open("xb")`). SAM's step-1 commit put the real submissions into history at that exact path, so every fresh clone now already contains them → `FileExistsError`. The suite went red **at 16:30:23Z, mid-sitting, permanently** — the sitting itself invalidated the fixture's pre-pilot assumption. The packet's §4 claim is honestly labeled ("212 green *at packet v2*") but was already stale when the packet was cut, and nobody re-ran the suite post-sitting. Two notes: the failure mode is itself reassuring (the tool *refuses to clobber a real submission* — correct behavior); and a known-red suite is an unusable regression baseline for the §5 remediation work, so this fix goes first. **Remedy → §5.5.**

### N5 — LOW · Governing surfaces lag the pilot
- `KERNEL/GATE_C_READINESS_PLAN.md` checkpoint record: C7 still reads "INDEPENDENT REVIEW OWED" (delivered — PROCEED, CHG-050 RESOLVED) and C8 "NOT AUTHORIZED" (the pilot ran under Will's ruling). The governing surface contradicts the packet it governs.
- Root `CLAUDE.md`'s custody enumeration authorizes PROME to commit "schemas and policy/registry versions; accepted events; rejected receipts; the four views" — **the activation document and the closeout packet are in none of those classes**, yet the operator-approved runbook (steps 2 and 9) instructs PROME to commit both into `KERNEL/`. The authority chain is intact (the approved packet governs); the root mirror lags it — the exact mirror-lag class root CLAUDE.md itself documents at n=2. This makes it n=3. **Remedy → §5.6.**

### N6 — NOTE · Mid-sitting rulings have asymmetric durable records
The window ruling and D1 got a proper committed ruling record (`PROME/proposals/…RULED.md`). The D3 PROCEED is durably recorded only inside the closeout packet, written by the same custodian, citing an ephemeral AskUserQuestion record. Will can confirm it here (and should, by ruling on this review); future sittings should append mid-sitting rulings to the ruling record at ruling time. **Remedy → folded into §5.3.**

---

## 4. Judgments PROME asked of this desk

**D3 (step-6 criterion vs tool design): RE-WORD THE CRITERION; do NOT build the unchanged-content skip.** Grounds, from this desk's C7 probe context: the skip is new comparison logic on `write_views` — the exact durable-write chokepoint whose correction history already produced a partial guard that read as complete (C7 Finding 1: first fix guarded one of two paths; only the delta re-review caught it). A stamp-normalizing comparator adds a masking class (a stamp-format change silently renders everything "unchanged") for zero integrity gain — view reproduction is already carried deterministically by step 8's `check-views` at the committed stamp, which I re-ran and which passes. Re-word step 6 to: *"events byte-identical AND zero event writes; views re-render by design — the diff vs the prior run must be exactly the `render_as_of` lines, verified by `diff <(grep -v render_as_of run1) <(grep -v render_as_of run2)` returning empty, captured into the durable transcript."* That makes the criterion mechanical, satisfiable, and preserved — and moves the view-integrity weight explicitly onto step 8 where it already lives.

**D5 (push-train vs "no push during the sitting"): DROP THE GUARANTEE from steps 1/7/9; do not build a freeze or a branch.** The guarantee is unhonorable in this repo — verified: a shared commit graph plus any peer's ff-sweep pushes everything, and root CLAUDE.md itself records that only per-agent branches could prevent it. A fleet push-freeze burdens ~30 desks for zero integrity gain; a per-agent branch contradicts the repo's single-branch canon for a property the design doesn't need. The pilot is the proof: four commits reached origin mid-window and every integrity check still passes, because the events' integrity is carried by content, hashes, and additions-only — not locality. Replace the clause with: *"commits may reach origin at any time via the push-train; no step may depend on a commit remaining local."* The design already satisfies it.

**D1:** concur with the packet's reviewer note — the criterion the sitting actually used (staged index empty + custody paths clean) is the right one; write it into step 0. **D2:** concur — authoring defect, owned; successor drafts carry a canonical-form example in the `TO-BE-RULED` placeholder. **D4:** concur — not a defect; the submitter-side guard working is a C1 result worth keeping in the record.

---

## 5. Required remediations before the next sitting (the CONTINUE conditions)

1. **Runbook step 6 re-worded** per §4-D3 (also fixes "zero new writes"). Doc-only.
2. **Steps 1/7/9 drop the hold-local push assumption** per §4-D5. Doc-only.
3. **Step 9 becomes an affirmative close + stop-condition discipline (N1/N3/N6):** at sitting end, set `revoked_at` and commit it — closure is an act, not a lapse. After any stop condition: no further live applies until the operator rules; preserve the on-screen state durably *before* any diagnostic run; append mid-sitting rulings to the ruling record at ruling time. Doc-only.
4. **Durable transcript (N2):** tee every tool invocation's output to `KERNEL/rehearsals/<date>_pilot-transcript.txt` (the C6 precedent), committed with the closeout packet. Doc/process-only.
5. **Fix `test_prepare_pilot` (N4)** — build the mirror from the pinned source commit, or tolerate pre-existing canonical files whose hashes match the pins — and re-run the suite to green so the next remediation cycle has a usable baseline. **The only code change on this list, and it is test-fixture code.**
6. **Housekeeping (N5):** advance the READINESS_PLAN checkpoint rows to reflect C7-complete + this review; reconcile the root CLAUDE.md custody enumeration to name activation documents and closeout packets (or point it at the runbook as governing). Both PROME-lane; the root edit is Will-gated per its own rules.

## 6. Why CONTINUE and not remediate/pause

"Remediate" would imply the pilot's *results* need repair — they don't; every durable artifact checks out under independent re-derivation, twice over for the two integrity properties. "Pause" would imply an open risk while remediations land — there is none: the activation lapsed at 18:00Z, nothing runs without a fresh Will-ruled window, and the C7 refusal matrix (RED-probed) plus the live D2 demonstration show the fail-closed posture holds against real inputs. The six conditions above are five documents and one test fixture. The pilot did what a pilot is for: it surfaced five discrepancies plus the six findings here, at a cost of ~32 attended minutes and zero integrity events. Gate C's next increment should proceed on a corrected runbook.

— RED, 2026-08-27
