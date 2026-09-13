# ACCEPTANCE — three external findings, 2026-09-13

Written **2026-09-13 10:5x ET before any edit**, per `PROME/CLAUDE.md` § Session Process Controls.
Each condition set is stated in the defect's own terms, not as a restatement of the symptom.

---

## F1 (HIGH) — `argus_scope.py` fails OPEN when scope discovery fails

⛔ **This is the same bypass class I previously reported CLOSED. It was not.** The earlier repair
made `--mark-reviewed` and the closeout gate fall back to the tool's own computed scope when no path
list was supplied — but wrapped that fallback in `except: paths = None` with the comment
*"scope unavailable => cannot claim completeness; stay silent."* **Staying silent IS the fail-open.**

**Reproduced 2026-09-13 in a throwaway fixture** (never the live repo): baseline recorded, candidate
frozen and promoted to REVIEWED, then an unreviewed file added.

| scope discovery | rc | UNREVIEWED flagged |
|---|---|---|
| working | **1** | yes |
| raising | **0** | **no** — and it printed *"1 path(s) … byte-identical to the frozen candidate (verdict REVIEWED)"* |

**Acceptance conditions**
1. Failed or invalid scope discovery returns **CANNOT-EVALUATE**, never a pass. The run cannot claim
   completeness it did not establish.
2. **Promotion to REVIEWED is prevented** under that condition — `--mark-reviewed` must refuse.
3. The **required review check blocks** at standard/heavy under that condition.
4. The distinction survives in the output: *"we looked and found nothing"* and *"we could not look"*
   must not render the same, which is precisely how this survived.
5. An explicit `paths` list from the caller still works; this changes only the `paths is None` path.
6. A genuinely clean run still returns 0. The guard must not make every run unevaluable.

---

## F2 (HIGH) — the F-4 suite still writes into the live repository

`test_agent_freshness_L294_F4.py` creates and deletes `AGENTS/BRENT/zz_f4_probe.md`, and other cases
create `AGENTS/ZZ_F4_*` directories and delete their contents in cleanup.

⛔ **This is the THIRD live-state test defect in three sessions**, and the worst of the three, because
I built `gate_fixture.py` for exactly this on 2026-09-12 and then did not apply it to the suite that
needed it. A fixture that exists and is not used is not a control.

**Acceptance conditions**
1. No test writes, creates, or deletes anything under the live checkout. The live tree is untouched by
   a full run — asserted, not assumed.
2. The fixture carries **git history** (the age query needs commits) and a **dirty-file** case (the
   `dirty_paths` tests need an uncommitted file).
3. The defect each test was written for is still exercised: a real dirty path is seen; a failed
   `git status` returns UNKNOWN; a never-committed desk reads `never`; the pre-spawn STOP fails closed.
4. Fixture allocation is owned and cleaned up by the fixture module (the 9/12 `destroy()` contract).
5. ⚠️ Two tests deliberately read the LIVE repo without writing — the perimeter-derivation test and the
   real-repo control. Reading is not the defect; **writing** is. They stay, and stay read-only.

---

## F3 (MEDIUM) — the Pending-Will parser truncates at the first period

`fleet_dashboard.py:327` terminates on `[^.\n]+`. A generated item containing a period — the reporter's
case, `WQ-169 (e.g. next week) · WQ-238 (9/19)` — truncates to `WQ-169 (e` and **drops every item after
it**. Yesterday's repair widened the LABEL match and left the TERMINATOR broken, so it fixed the
heading and not the content.

A missing label also still returns `[]`, so **an empty queue and a failed parse render identically** —
the same failing-silent property that hid the label break for a week.

**Acceptance conditions**
1. The parser consumes the **complete generated block** and preserves punctuation inside items.
2. An item containing `.` does not truncate and does not drop its successors.
3. **Empty queue and failed parse are DISTINCT** in the returned value and in what the page renders.
4. `·` splitting stays outside parentheses (the 8/16 grouped-sub-item rule survives).
5. Bold residue does not leak into item 1.
6. ★ **Generator and consumer are tested TOGETHER** — the contract broke because each was correct
   alone. The test drives `willq_view.py`'s real output into `fleet_dashboard.py`'s real parser.

---

## Neighbour categories — considered for the set

| # | Category | Disposition |
|---|---|---|
| 1 | **Ordinary** | TESTED in each: clean verify passes; a real dirty path is seen; today's live block parses all 17 items. |
| 2 | 🔴 **Overlap** | TESTED — F1: scope discovery fails **while** an explicit `paths` list is supplied (the caller's list must still be honoured, and the failure must not be laundered into a pass). F3: an item with a period **and** a parenthesised group in one block. |
| 3 | **Wrong owner** | TESTED — F3: a `Pending Will` string appearing in PROSE elsewhere in SCRATCH must not be parsed as the block. F2: the two read-only live-repo tests stay read-only. |
| 4 | **Missing information** | TESTED — F1 is this category by construction. F3: label absent ⇒ explicit failure, not `[]`. |
| 5 | **Concurrent activity** | F1/F3 **N/A, justified** — single-pass readers, no shared state. F2 is the *reason* this category matters: the old suite could collide with another session writing the same live paths, which the fixture removes by construction. |

---

## F1 ROUND 2 — the fix's own carve-out was the same bypass

Written **2026-09-13 afternoon, before the round-2 edit.** Conditions 1–3 are the reviewer's own
words; 4–5 are mine.

My round-1 repair raised on a scope-discovery *exception* but carved out "no baseline" as merely
**not applicable**, so four content-only fixtures would keep passing. `load_baseline()` returns
`None` for several conditions — not just absence — **including a recorded commit git cannot
reach**. The carve-out therefore reopened the hole for every real-world way git breaks, which is
most of them.

⛔ The tell was in my own round-1 test docstring: *"hiding the second would re-open a quieter
version of the same hole"* — and then the code did it. Printing `NOTE: additions were NOT checked`
does not protect a caller that only reads the return code, and the note itself asserted the wrong
direction: *"the unreviewed-additions half is not applicable without a baseline."* **An unavailable
baseline makes completeness UNKNOWN; it does not make completeness UNNECESSARY.**

**Acceptance conditions**
1. Both raised discovery failures **and** unusable/missing baselines prevent certification for a
   required review, unless an explicit, complete candidate path list is supplied.
2. Content-only comparison stays available **as a diagnostic**, but must not authorize REVIEWED or
   satisfy the Standard/Heavy gate.
3. The four content-only **test fixtures** are updated to pass an explicit list; production
   verification is **not** weakened to accommodate them.
4. The regression test drives **real git failure** (the fixture's `.git` moved aside), not only a
   mocked `build_scope()` exception. The mock could not have found this defect, so a mock cannot
   be the thing that pins it closed.
5. The new tests must **fail against the carve-out code**. Verified: 3 of the 5 fail on `8f4d8ba44`
   (the other 2 are a stated precondition and the unchanged escape path, version-independent by
   design).

**Neighbour categories** — ordinary (a clean fixture run still returns 0) and missing-information
(the category the defect lives in) TESTED. Overlap TESTED: git broken **while** an explicit list is
supplied still returns 0. Wrong owner / concurrent activity **N/A, justified** — a single-pass
reader over a frozen manifest, no shared state and no second writer.

---

## F1 ROUND 3 — an independent reviewer broke my round-2 claim three ways

Written **2026-09-13 11:4x ET before any edit.** Commissioned per WQ-229 (a consequential repair
touching a gate, on a defect that has already recurred, goes to an independent reader who devises
its own counterexample). It did, and it was right.

⛔ **I told Will "there is no longer any input or environment condition under which
`verify_review()` returns 0 without establishing completeness." That claim was FALSE.** Round 2
closed the door I had been shown and left three others open. All three were confirmed at the
artifact and two reproduced empirically before this was written.

| # | Defect | Confirmed |
|---|---|---|
| ❌1 | `--paths` **present but empty** (`nargs="*"`, an unset shell variable) is `[]`, which `is not None`, so discovery is skipped and completeness is vacuous — rc 0 over an unreviewed addition. **Omitting the flag returns rc 1.** Passing it empty is strictly worse than not passing it. | reproduced |
| ❌2 | `git()` carries no `cwd`, so scope is discovered from the **process CWD** while content is read from `ROOT`. From a second worktree/clone the baseline resolves against the shared object DB, discovery returns the *other* checkout's scope, nothing raises, and `mark_reviewed()` promotes the real repo. `git worktree list` shows a live second worktree, so this is reachable, not theoretical. | confirmed at `argus_scope.py:43` vs `:218` |
| ❌3 | The discovery fallback builds from `lanes[...]` and **discards `excluded`**, so an unreviewed addition at any EXCLUDED path (`CLAUDE.md`, `scripts/**`, `docs/**`, `AGENTS/**`) yields rc 0 — while the explicit-list form on the same tree yields rc 1. Two callers of one function, opposite verdicts, and the permissive one is the one that promotes to REVIEWED. | confirmed at `:285-287` |

**Acceptance conditions**
1. An empty `paths` list NEVER authorizes rc 0. It establishes nothing, and the message must say
   that omitting the flag is safer than passing it empty.
2. Scope discovery reads **the same repository whose content is being compared** — independent of
   the caller's CWD.
3. The completeness check considers the **whole commit set**. The perimeter decides what ARGUS
   *audits*; it must not decide what counts as *shipping unreviewed*. Those are different questions
   and one was answering the other.
4. Round-1 and round-2 behaviour survives unchanged: discovery failure and unusable baseline ⇒ rc 2;
   an explicit complete list ⇒ rc 0; a genuinely clean run ⇒ rc 0.
5. Every new test **fails at `625cb7070`**. A test that passes before the fix pins nothing.

**Not fixed in this pass, and why.** The reviewer's four ⚠️ (SystemExit escaping `except Exception`;
`AttributeError` on malformed manifests; the rc-0 line not naming its scope basis; rc 2 recorded as
a PASS when `--tier` is omitted) are real but all **fail closed** — they exit 1 or block. They are
residue, registered rather than swept into a repair pass that is already three rounds deep on one
file. ⚠️4 is the strongest of them: the rc-1 remedy text is the wrong repair for a missing input,
and the gate skips every check after it.

---

## Verification status — stated as CASES CHECKED, not as rounds

Will, 2026-09-13: *"Describe verification in terms of the cases checked, rather than declaring
whole 'rounds' universally verified."* I had written "rounds 1–2 are now INDEPENDENTLY VERIFIED",
which is the same overreach as the claim the reviewer falsified — a real result carried to a
wider conclusion than it supports. A review establishes the cases it drove. It does not certify
a round.

**Checked by an independent reader, with its own fixtures:** empty `--paths`; `--paths ""`;
`--paths` omitted; a foreign CWD (clone, worktree, non-repo); `.git` moved aside; baseline absent,
unparseable, empty, and sha-not-a-commit; a genuinely empty scope vs a failed discovery; detached
HEAD; unreviewed additions at OWNED and at EXCLUDED paths; `mark_reviewed()`'s single call path;
`load_perimeter()` missing, empty and malformed; manifest `paths` as list, string and null.

**NOT reached, and named by the reader:** an empty repo with no commits; a valid but too-old
baseline sha; concurrent writers mutating the manifest between freeze and verify; a hostile
`GIT_*` environment where git exits 0 with empty stdout; ambiguous short-sha collisions;
`prome_gate.py` driven end to end against a live repo (❌2's gate consequence was established from
the import path plus a faithful replica of its `try/except`, not a live gate run).

**Checked by me only, not independently:** the two round-3 fixes themselves — the empty-list guard
and `cwd=ROOT` — plus the two fixture repairs. Each is pinned by a test that fails at `625cb7070`;
none has had a second reader. L367 stays OPEN for the `excluded` integration and is the place that
work lands.
