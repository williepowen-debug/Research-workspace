# Decisions app — SR5 intake-isolation fix: PROME independent review

**Written:** 2026-10-31 18:41 ET · PROME (prome-34, Claude Code, Opus 5.5). **Asked by Will** in PROME's chat 18:34 ET, verbatim *"Can we fix this."* (pasting CATO's SR5 note).
**Subject:** CATO's prepared patch `AGENTS/CATO/runs/2026-10-31_1749_commit-review/intake-isolation.patch` (finding SR5 in `AGENTS/CATO/runs/2026-10-29_0942_recent-system-review.md`; pushed f415eb466). It changes `AGENTS/CATO/prototypes/decisions/mvp/owner_receipt.py` (one lookup: chained `.get()` on `display`/`record` replaced by type-checked access) and adds `test_intake_shape_review.py`. PROME did not author it, so this is an independent read of CATO's code.

## The defect (CATO SR5, reproduced)
One malformed reply file (e.g. `{"display": []}`) raised inside intake while every valid unreceipted answer was being inspected, so unrelated valid answers were marked `needs_clarification`. It blocks answers; it cannot approve anything or write a ruling.

## What PROME ran (fresh disposable clone of origin at 61b16595a; nothing run in the live tree)
| Check | Result |
|---|---|
| Patch applies to the installed build (WQ-579, cd0f1a254) | clean |
| CATO's new witnesses on the ORIGINAL owner_receipt.py | FAIL: six malformed-shape subcases + the no-receipt assertion — the defect is real and the test sees it |
| CATO's witnesses + test_batch WITH the patch | 23 tests OK |
| PROME's own counterexamples WITH the patch (not in CATO's suite): id of the wrong type (int), record with no id, display = True / 0 / 1.5, id null, unhashable id (a list), no display key at all | each malformed file → its own `needs_clarification` row; the unrelated valid answer → `received`; WILL_QUEUE.md untouched |
| Full app suite WITH the patch | 167 of 168 pass; the one failure (`test_revision_delivery … test_refused_commit_then_revised_answer_delivers_without_sweeping_old_stage`: "ValueError not raised") fails IDENTICALLY without the patch, with and without the repo hooks wired — pre-existing in a fresh clone, not caused by this patch; sent to CATO |

## Verdict
**ACCEPT** — ❌ 0. The change only turns an exception on malformed shapes into a skip; a well-formed reply follows the same path as before; corruption that names the same question still blocks that question (by design, CATO's second witness).
**Install:** CATO's exact patch bytes, with `PROME/decisions/app-acceptance.json` re-pinned for `owner_receipt.py` (sha256 963486f3f69c41df876dac9ec591895cde0ffd9db1ce087089de276f62b5fb39); no other pinned file changes. Chat confirmation stays required for every answer (WQ-571 A). The running app must be reopened once (it refuses replies when its own files change under it).
**Limits:** the pre-existing revision-delivery test failure is unexplained here (CATO's); actual answers through the live app are not exercised by this review.
