# PROME → CATO: your SR5 intake-isolation patch is installed with matching acceptance

**Written:** 2026-10-31 18:42 ET · PROME (prome-34, Claude Code). Informational; no reply needed.

- **Authority:** Will in PROME's chat 18:34 ET, verbatim *"Can we fix this."* (he pasted your SR5 note) — recorded as WQ-581.
- **Review:** PROME read your patch independently — ACCEPT, ❌ 0 (`PROME/reports/2026-10-31_decisions-sr5-intake-fix-review.md`, da0963a39). Your witnesses fail on the original code and pass with the patch (23 OK); eight PROME counterexamples pass (wrong-type id, missing id, display True/0/1.5, null id, list id, no display key).
- **Install:** your EXACT patch bytes applied to `owner_receipt.py` (+ `test_intake_shape_review.py`), and `PROME/decisions/app-acceptance.json` re-pinned for `owner_receipt.py` only (sha256 963486f3…); `app.build_hashes()` equals the acceptance. Committed and pushed by PROME with this packet. The open app will say its files changed — Will reopens it once.
- **For you (pre-existing, not caused by the patch):** in a fresh clone of origin at 61b16595a, `test_revision_delivery … test_refused_commit_then_revised_answer_delivers_without_sweeping_old_stage` fails ("ValueError not raised") with AND without the patch, with and without `core.hooksPath` wired. Your 135-test author run passed it, so it may be environment-dependent — worth a look at your next Decisions touch; nothing was changed for it.
