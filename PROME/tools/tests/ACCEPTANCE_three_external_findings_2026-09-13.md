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
