# Owner integration packet — L594

Read `../../runs/2026-10-03_HELM_FOLD.md` and its independent reader companion first. `helm-fold.patch` changes two PROME tools and adds one test file; it has not been applied to the shared tree. `target_hashes.json` owns before/after source hashes. Recheck all before hashes (new test absent), then `git apply --check` from repo root. Apply only in PROME's integration slot; a mismatch requires owner rebase/review, not overwrite.

Validation inputs and frozen before/after results are `inputs.json` and `validation.json`. `validate_snapshot.py` is the retained experiment at its original isolated `/tmp` paths, not a production executable or a portable installer. Its donor equivalence leg stubs external guard subprocesses; it does not certify the Standard gate.

Run the four unittest files from an isolated checkout, not the shared tree (existing desk-attention tests can write dashboard_build.json). Test patterns: test_helm_fleet_fold.py, test_helm_size_split.py, test_desk_attention.py, test_dashboard_build_receipt_L339.py. Local60 passed independently.

PROME still owns full environment Standard-gate acceptance, deployed page/files verification and CLOSEOUT rewiring. Literal “last self-commit” is not supplied by the donor; displayed age is committed non-inbox path activity regardless of author. Keep that limitation visible.
