# PROPOSAL — the push obeys the tier: `commit_check.py push --tier <t>` as the ONE push path (WQ-448)

**Written:** 2026-10-15 20:4x ET (PROME `prome-be`), on the reviewer's instruction relayed by Will at 20:42 ET ("Before starting simplification change 2, investigate the Light-tier verification and push path"). **Status:** PROPOSAL — a change to `PROME/CLOSEOUT.md` step 10 and to two PROME tools; it moves which check gates a push, so it is Will's word (WQ-448), then the next sitting's one process change (WQ-299 R1) with its acceptance file and one independent read. Nothing in this file is implemented. Friday's due research and position work runs first; the startup simplification (change 1) stays as shipped and is observed at the next normal boot.

## 1. What the two commits satisfied — by requirement, not by outcome

The applicable Light-tier requirements, read from `PROME/CLOSEOUT.md` (tier table; Pre-closeout 3; steps 9–10), root `CLAUDE.md` Git Protocol, and `PROME/CLAUDE.md` § Repair-completion (a consequential repair needs an independent reader). A push receipt establishes PUSHED and nothing else.

| Requirement (source) | 5b8f63130 (change 1, 8 paths) | 7d3325390 (memory n+2, 1 path) |
|---|---|---|
| Closeout gate run WITH the tier, rc 0, after the last content edit (step 9) | **SATISFIED** — `prome_gate closeout --tier light --no-memory --no-superseded` PASS (17 blocking / 22 advisory) at 20:1x ET, after the ORCH_LOG append, before the commit; log `/tmp/prome-closeout-569fac8d.txt` | **UNVERIFIED** — no gate run covers it: the only run preceded this commit and declared `--no-memory`, which this commit made false; the slug check was run by hand (`memory_index_check --strict --slug …` rc 0, `check_memory_length.sh` rc 0) outside the gate |
| Pathspec commit, exact paths, subject ≤100, intent ↔ commit match (root 4b/4d; `commit_check`) | **SATISFIED** — `commit_check commit --stage`, 8/8 paths match; first attempt refused at 116 chars, re-run at 98 | **SATISFIED** — 1/1 match; first attempt refused at 105 chars, re-run at 90 |
| ORCH_LOG rows through the writer; `orch_log.py check` ok (Pre-closeout 3, L733) | **SATISFIED** — coldreader row appended via `orch_log.py append`; check ok inside the gate | N/A — no spawn |
| Independent read before a consequential repair is called fixed (WQ-229) | **SATISFIED** — coldreader (Sonnet) RELEASE 0 ❌ / 5 ⚠️; W1 one-character fix after the read declared | N/A — a memory extension |
| Step 10: `argus_scope --verify-review --ref HEAD --paths …` rc 0 BEFORE `safe-push.sh` | **FAILED AS WRITTEN** — verify returned rc 2 CANNOT-EVALUATE ("manifest frozen against baseline 022a98267, current 6eb4ed323 — a PRIOR closeout"); the push ran in the same command on a `;`. **In substance NOT APPLICABLE at Light:** no review is frozen at this tier, so the verify can never return 0 — see § 2 | **FAILED AS WRITTEN, differently** — verify-review was never run for this commit; the first (refused) attempt's chain still invoked `safe-push.sh` ("Nothing to push"); the retry pushed gated only on the commit rc |
| Light touches: SCRATCH targeted update · STATUS surgical (tier table) | SCRATCH **SATISFIED** (header + ★ NEXT paragraph); STATUS **UNVERIFIED/NOT DONE** — its Last-mile row still names L738 as "the next process slot"; nothing in STATUS was wrong enough to block, but the surgical touch was not made | N/A |
| PUSHED (receipt) | **SATISFIED** — `Pushed. CONFIRMED: HEAD 5b8f63130 is on origin/master (fresh fetch).` | **SATISFIED** — `… HEAD 7d3325390 …` |
| PUBLISHED | N/A at Light; Deck owed set unchanged ⇒ NO-OP under WQ-446 A | N/A |

Net: both commits are COMMITTED and PUSHED with every Light-tier substantive check satisfied except STATUS's surgical touch (minor, now stale by one pointer) and the second commit's uncovered memory declaration. The step-10 control FAILED AS WRITTEN on both, and the failure did not stop anything.

## 2. The conflict, and why a failed verification stopped nothing

**Two rules disagree about Light.** The tier table says Light runs no audit ("Optional" commit; no ARGUS); `prome_gate.check_review_manifest(tier)` encodes that — the review check is ADVISORY below Standard and BLOCKING at Standard/Heavy. But step 10 is written tier-blind: *"commit → `--verify-review --ref HEAD --paths` → `safe-push.sh` ONLY if the line above returned rc 0"*. At Light nothing is frozen for this closeout, so `verify_review()` returns rc 2 (no manifest, or a manifest whose baseline belongs to a PRIOR closeout — tonight's case) by construction. A Light push therefore has exactly two outcomes under the letter: a protocol breach, or no push at all. The manual asks for a check it has already said this tier does not run.

**Nothing mechanical joins the verify to the push.** `scripts/safe-push.sh` takes no precondition input — it checks branch, shallow-ness, fast-forward, and issues the receipt. `commit_check.py --push` runs safe-push after its own intent↔commit verify only, and step 10 forbids `--push` precisely because that verify is not the review verify. So the join between "verify rc" and "push" lives in the operator's shell line. Tonight that line was `…--verify-review …; echo rc; bash scripts/safe-push.sh` — a sequence, not a conditional — so the printed rc=2 was an advisory and the push ran (`finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`, n+2). Same shape minutes later: a refused commit (subject 105 chars) whose chain still invoked safe-push ("Nothing to push") because `| tail -3` laundered the wrapper's rc.

**The gate does not tell the push what tier it ran.** `prome_gate closeout --tier light` records nothing on disk; the tier exists only in the operator's command history. So even a careful operator cannot make the push *depend on* the tier's result — there is nothing for it to read.

## 3. Smallest correction using existing tooling

**Principle:** the selected tier is recorded ONCE by the instrument that already takes it (the closeout gate), and the ONE push verb reads that record and the existing verifiers, then calls the existing push script or refuses. No new review layer; no new check; two tools gain a few lines each; the manual's step 10 becomes one command.

### 3a. `PROME/tools/prome_gate.py closeout --tier <t>` writes a receipt (new, ~15 lines)
At the end of `mode_closeout`, write `PROME/state/closeout_gate_receipt.json` (gitignored like the other `state/` run files, or tracked — decide at implementation; the push verb reads it either way):
`{"tier": "<t>", "rc": <aggregate rc>, "head": "<git rev-parse HEAD at run time>", "recorded_at": "<ISO>", "blocking_fail": [...names...], "errored": [...names...]}`.
Boot and refresh modes write nothing. No existing check changes class or meaning.

### 3b. `PROME/tools/commit_check.py push --tier <bounce|light|standard|heavy> [--push-cmd …]` (new subcommand, ~50 lines; reuse `verify()` and `argus_scope.verify_review`)
In order, each a refusal (rc 1, "NOT PUSHED: <reason>") that stops before any push:
1. **Receipt present and binding** — `closeout_gate_receipt.json` exists, `tier` equals `--tier`, `rc == 0`, no `errored`, and `head` equals the push base (`origin/master` after `git fetch origin master`). Missing, unreadable, mismatched tier, rc≠0, errored, or a head that is not the push base ⇒ refuse ("UNKNOWN never pushes"). This is what makes the tier's result control the push mechanically, and it closes tonight's second shape: a commit made after the gate on top of other unpushed commits is still covered (the gate ran at the base), but the verb prints the commits-since-gate list so the report can name what the gate's declarations did not see.
2. **Intent ↔ commit** — existing `verify("HEAD")` must return 0 (all tiers).
3. **Review, tier-selected** — at `standard`/`heavy`: `argus_scope.verify_review(paths=<HEAD's own paths from git>, ref="HEAD")` must return 0 AND the manifest verdict must read `REVIEWED` (mirrors `check_review_manifest`; a FROZEN candidate refuses; rc 1 CHANGED or an UNREVIEWED addition refuses; rc 2 refuses with the verifier's own CANNOT-EVALUATE line). At `light`/`bounce`: not required; the verb prints `review NOT required at <tier> — delivery = gate receipt + intent↔commit`, and still runs `verify_review` ADVISORY so a stale manifest is named, never read as a pass.
4. **Push** — `subprocess.run(push_cmd)` where `push_cmd` defaults to `bash scripts/safe-push.sh` (unchanged, fleet-shared) and `--push-cmd` substitutes an isolated command for tests. The verb returns safe-push's own rc (0 confirmed · 1 not pushed · 2 CANNOT-CONFIRM) and never prints a receipt of its own — safe-push's line is the only receipt.
Remove `--push` from the `commit` subcommand (the unverified path step 10 already forbids); `commit` stays otherwise untouched.

### 3c. `PROME/CLOSEOUT.md` step 10 (the letter)
Replace the three-line recipe with: *commit with `commit_check.py commit --stage -F <msgfile> -- <exact paths>`; then `python3 PROME/tools/commit_check.py push --tier <the tier you ran at step 9>`; it refuses unless the step-9 receipt carries that tier with rc 0 at the push base, intent↔commit matches, and — at Standard/Heavy — the review verifies REVIEWED and unchanged for HEAD's own paths; safe-push's line remains the only push receipt.* The tier table's "Optional" commit at Light is unchanged; the `/closeout` runner's step 5 line (both copies) carries the same single command. Nothing else in the manual changes.

**What this does NOT do:** no new audit, no new reader, no change to what any gate check means, no change to `safe-push.sh`, no change to Standard's protections (the review requirement moves from the operator's chain into the verb and is therefore stronger, not weaker), no change to boot.

**Replaces:** the operator-typed verify→push chain (the control that failed twice tonight) and one standing prohibition (`--push`).

## 4. Acceptance (WQ-229: written before the edit; five categories) — `PROME/tools/tests/test_commit_check_push_tier.py`, throwaway repo only (`gate_fixture.py` contract: never the live tree)

Fixture: a temp repo with an `origin` bare remote, one base commit pushed; a fake push command `fake_push.sh` that appends its argv to `pushed.log` and exits 0 (a second variant exits 1 for the "safe-push refused" case). The receipt and the review manifest are written as files inside the fixture (the tools' `ROOT` is pointed at the fixture the way the existing argus/closeout tests do it).

| # | Category | Condition | Test |
|---|---|---|---|
| A1 | Ordinary — Light permitted | receipt {light, rc 0, head = base}; one commit on base with a matching intent file; `push --tier light --push-cmd fake` ⇒ rc 0, `pushed.log` has one line, stdout carries "review NOT required at light" | `test_light_permitted_pushes_once` |
| A2 | Ordinary — Standard permitted | receipt {standard, rc 0, head = base}; manifest REVIEWED, baseline = current, every HEAD path byte-identical ⇒ rc 0, pushed once | `test_standard_permitted_pushes_once` |
| A3 | Missing information — no receipt | no receipt file (either tier) ⇒ refused, `pushed.log` absent, stdout "UNKNOWN never pushes" | `test_no_receipt_refuses_any_tier` |
| A4 | Missing information — Standard without a review | receipt {standard, rc 0}; no manifest ⇒ refused with the verifier's CANNOT-EVALUATE line; no push | `test_standard_cannot_evaluate_refuses` |
| A5 | 🔴 Overlap — frozen but not reviewed | manifest exists, verdict FROZEN, unchanged ⇒ refused at standard ("freezing is not an audit"); permitted at light with the advisory line | `test_frozen_not_reviewed_refuses_standard_allows_light` |
| A6 | 🔴 Overlap — reviewed, then a path added | manifest REVIEWED; HEAD carries one path not in the manifest ⇒ refused at standard (UNREVIEWED addition); light prints it as advisory and pushes | `test_unreviewed_addition_refuses_standard` |
| A7 | Wrong owner — tier mismatch | receipt {light}; `push --tier standard` ⇒ refused ("receipt tier light ≠ standard"); and the reverse ⇒ refused | `test_tier_mismatch_refuses_both_ways` |
| A8 | Wrong owner — receipt from another base | receipt head = an older commit, not the push base ⇒ refused; same with rc 1 or an `errored` list ⇒ refused | `test_stale_or_failed_receipt_refuses` |
| A9 | Ordinary — intent mismatch | receipt ok; HEAD has a path the intent file does not name ⇒ refused before any review or push | `test_intent_mismatch_refuses` |
| A10 | Concurrent activity — second commit after the gate | receipt head = base; two commits since; `push --tier light` ⇒ permitted (gate ran at the base) and stdout lists both commits as "since the gate"; at standard the second commit's paths must be in the manifest or A6 refuses | `test_commits_since_gate_are_listed` |
| A11 | Ordinary — push failure is not laundered | fake push exits 1 ⇒ verb returns 1 and prints nothing that reads as a receipt | `test_push_rc_propagates` |
| A12 | Shape — the removed flag | `commit --push` is no longer accepted (argparse error) | `test_commit_push_flag_removed` |

Run under `python3 -W error::ResourceWarning`; count measured at the result with `grep -c 'def test_'`. Neighbour N/A: none — every category has a case because the defect was an operator join, and the verb now owns every join.

## 5. Residue and limits, stated now
- The receipt binds the gate run to the push base, not to the final tree: a file edited after the gate and committed is covered only by intent↔commit (and at Standard by the manifest). The verb names the commits since the gate; it does not re-run the gate. A re-run is the operator's call per step 9's loop rule, as today.
- The report line for a Light push still says "review NOT required"; it does not say "reviewed". The two-state honesty (COMMITTED · PUSHED) is unchanged.
- This proposal was written in the sitting whose process slot was spent on change 1; it is not implemented here. Implementation = one process change, acceptance file = this § 4, one independent read (a tool touching a Will-facing control ⇒ a reader with its own counterexample, Opus per WQ-447).
