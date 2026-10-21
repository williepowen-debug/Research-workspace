# L748 rebase independent review — 2026-10-20 ET

Reviewer: `/root/l748_rebase_review`, OpenAI/Codex thread-local helper. ACCEPT for the bounded rebase; no new blocking finding. This is not installation, owner consumption, timestamp authentication, fleet liveness, or full-system certification.

REVIEW: required — rule4/4b guard/evidence interpretation; scope `repair.patch` whole and both target manifests whole, prior patch comparison, applied `guarded_view`, append interaction, rotation and closeout consumers through targeted tests; reader `/root/l748_rebase_review`; disposition APPLIED 0 · RESIDUE 0 for rebase.

Repository resolved to `/home/willi/Research-workspace`; execution isolated at `/tmp/l748-rebase-yb2mt2_p/repo`. Verified shell/Python/Git tools; model exact label unavailable. Reviewed root/local instructions explicitly, COMPLETION_SPEC reviewer exemption, UPGRADE_PROTOCOL whole, applicable runtime mechanics and helper charter. No desk boot or global inbox disposition claimed; no live source/ledger/view edits. Initial combined instruction output truncated; relevant operational ranges recovered; no claim of exhaustive fleet startup. Report path is the sole shared write authorized by parent.

## Integrity

- All before hashes match pinned base objects; all after hashes match the applied clone.
- Prior and new repair patches are identical after removing only `index` and `@@` hunk metadata. L748 semantics unchanged.
- `guarded_view` complete function text is byte-identical between current base and patched clone. L736 preserved.
- `orch_time.py` and `orch_closeout.py` after hashes are unchanged from prior manifest.

```json
{
  "base": "25a79bddf6562d69f2a6ec882acd277d113ac886",
  "rebased_over": "cf074c5fc9ee751e6a1fd53bd210cc989373ef8a",
  "paths": {
    "scripts/orch_time.py": {
      "before": null,
      "after": "891ac86886a83d2785b0f195bf7976db3b2ee25dc4e8ddf32ed1b4d1cfb727ce"
    },
    "scripts/orch_log.py": {
      "before": "e84f5601735ab85a97931d4c2b57f1f62e7d2b81ef9119f1f0ae5d87f1429aac",
      "after": "e3e563e03102e19469ea02d159e943783af5fd7b825678849b8974190107b14b"
    },
    "PROME/tools/orch_closeout.py": {
      "before": "b4ec5ad1e58f3263ec895d3b4e018da2be226366aa367b1eef67077fac09eb3b",
      "after": "c005cdbee0ab693ae024ca87f241c6a83ff0ef1fa231d7188ade273c6e1f9cd0"
    }
  },
  "patch_sha256": "437c72d452ea1b21f6be4060d2cc20b4d970134a2cbae0c55e5f0e904ae73451",
  "previous_manifest": "pre_L736_rebase/target_hashes.json"
}
```

## Executed validation

| Check | Result |
|---|---|
| L748 build tests | 13 passed |
| writer `--selftest` | 36/36 passed |
| closeout unittest file | 27 passed |
| L736 public-view unittest file | 7 passed |
| Four real target rows, temp ledger | 4 appended; original bytes preserved; all 4 UNKNOWN/INVALIDATED-UNKNOWN; before/after obligation count686; live ledger unchanged |

Tests used clone `scripts` on PYTHONPATH. Initially attempted writer `selftest` positional mode, received CLI refusal; corrected to documented `--selftest`. Existing ResourceWarnings appeared during L748 tests, without failures. No unavailable dependency remained.

Production target identity checked against prior `production.txt`, not just physical line numbers:

- `5ed3b057344b3bd304ea5cb5def7870b8167868af1f0439177338b9db3e2070c`
- `e8d70e57221fc9b28bca05ecc4b16260521a83806148cdc1152e391a09acf795`
- `35fefce6df499534fc792cd52110cb9676a2b38c527f88c325455317f3c3fce8`
- `62cd8214d7f3235cc3ac9fe97cadc0df3394d60a4b1d707d156c5a5f15f76a99`

## Independent counterexample

Hypothesis: a valid L748 invalidation after an unobserved hand row could bypass L736 view refusal or acknowledge drift while losing the invalidation. Executed on temp ledger: append without acknowledgment and public view both refuse with ledger/view unchanged; acknowledged legitimate append succeeds; subsequent view succeeds; original remains UNKNOWN/INVALIDATED-UNKNOWN and both original obligations survive reconciliation. Hypothesis refuted.

Initial counterexample assertion incorrectly expected `evaluate` to retain an older ALREADY_CLOSED unrelated row. Inspected its documented date/state filter; this is expected filtering, not a bug. Corrected the assertion to inspect `reconcile`, which retains both original obligations. The correction changes reviewer expectation only, no source fix.

Raw interaction output:

```text
ORCH-LOG ✓ view regenerated → ../../tmpgw_35zbz/view (1273 B, 0 table rows, window 30d)
ORCH-LOG ✗ rc 2 — append REFUSED: 2 ledger rows vs the view's 1 — 1 row(s) entered without this writer; run `check`, name them, then re-run with --acknowledge-unobserved 1; nothing written
ORCH-LOG rc 2 — view REFUSED: ledger 2 rows vs view 1; delta 1; nothing written
Inspect the extra rows. A legitimate next append requires --acknowledge-unobserved 1; do not invent an event to reset the view.
ORCH-LOG ✓ appended 1 row (2026-10-20 reader touch CLOSE, CLOSE_SUMMARY) — ledger validates after the write · view regenerated → ../../tmpgw_35zbz/view
ORCH-LOG ✓ view regenerated → ../../tmpgw_35zbz/view (1287 B, 0 table rows, window 30d)
PASS: unacknowledged append/view refuse unchanged; explicit acknowledgment preserves UNKNOWN original and 2 reconciled original obligations.

```

## Limits and closeout

Bounded rebase review complete; no pending work in this assignment. Parent owns commit/publication and PROME delivery. Owner must recheck exact before hashes and apply patch, validate after hashes/tests, then perform explicitly authorized historical invalidations. No production install or historical correction was performed by this reviewer. No new implementation was made after this review; later source/package changes require POST-REVIEW labeling and applicable verification.
