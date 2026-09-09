# Self-review versus separate review

This is the private implementation of Will's public [research-quality pilot draft](https://github.com/williepowen-debug/Selected-Agents-Open-Demonstration/blob/main/experiments/research-quality-pilot.md). It uses synthetic evidence and isolated experimental threads; it does not use or alter the live research desks.

Read `PROTOCOL.md` for the exact feasibility variant and limits. `corpus.json` contains both task materials and withheld answer keys; only `public_task()` fields and the stage's evidence updates are sent to the model. `KEY_REVIEW.md` records the independent AI key check and corrections applied before freeze. Human validation remains pending. `development/` contains practice, never evaluation evidence.

The frozen input set is `FREEZE.json`. Its Git commit precedes evaluation. Verify it before running or analyzing evaluation:

```bash
cd /home/willi/Research-workspace
python3 -B -c "import sys; sys.path.insert(0,'PROME/experiments/review-pilot'); from runner import verify_freeze; verify_freeze()"
python3 -B -m unittest discover -s PROME/experiments/review-pilot -p test_runner.py -v
```

The runner creates new owned Codex processes under temporary empty directories, using the current account's authenticated CLI. A named output directory must not already exist. It serializes experimental turns and retains failures; it never automatically retries or resumes a failed batch. Running the command consumes subscription capacity. Current no-tool configuration was tested with empty configured MCP-server inventory; do not reuse unchanged in an environment with additional inherited integrations without a new development check.

```bash
python3 -B PROME/experiments/review-pilot/runner.py --phase evaluation --out /tmp/review-evaluation-new
python3 -B PROME/experiments/review-pilot/analyze.py /tmp/review-evaluation-new
```

`outcomes.csv` includes every scheduled run, even NOT_RUN. `summary.json` contains per-family and paired descriptive results. `human-review.json` contains randomized anonymous output IDs and no condition labels; keep `human-review-mapping-private.json` away from the grader until scoring is complete. Masking alone does not establish blindness. Final narrative and implementation limitations are recorded in `RESULTS.md` after evaluation.

Equal three-turn opportunity is enforced. The token threshold only stops a subsequent turn; it cannot cap a turn already running. A complete token total is unknown if any turn's usage is missing/invalid; known category sums are lower bounds in that case. Dollar charges and human minutes are not inferred. Do not describe this feasibility study as the original hard-token-cap, human-graded experiment.
