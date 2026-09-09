# SAM boot corrections — implementation record

Implemented September 9, 2026 under Will's approved [plan](../proposals/2026-09-09_boot-corrections.md). This pass changes tooling and handoff accuracy; it introduces no market assessment, prediction grade or trade.

## Delivered

- Neutral USDJPY/JGB observations replace causal/trading labels. FXY and continuous Brent are context quotes. Each vendor quote carries its field, observation clock and per-download retrieval time; previous-close and unknown-age fallbacks cannot fire a crossing. Numeric comparators for retained watches are preserved.
- CFTC live display uses R=−188,077, while legacy workbook normalization is unchanged. The strict >10% cover alert now uses prior gross shorts consistently in both trigger and printed percentage. Gross-position changes no longer announce liquidation or rearm.
- Monitoring preserves full child stdout/stderr, exit reasons and partial timeout output in raw JSONL reports. Failures cannot print a clean-completion verdict. Inventory drift and prediction gaps make the aggregate exit nonzero. Stored vintages are distinguished from execution success. Options skip checks four distinct future calendar-date expiries; `--quick` skips options only.
- BOJ `--prepare-review` saves source HTML/PNG, hashes, original retrieval time and a blank transcription. It is idempotent by image hash and rejects tampered saved evidence. Preparation never validates a quote or writes its ledger. Existing source/layout/hash/term/age/expiry/arithmetic/revision guards remain.
- Read-only `--orient` emits an index and individually requested ≤14KB parts with source/content hashes and end markers. It reads required context, original OPEN conditions and the full MEMORY handoff without market or inbox actions. `--predictions` derives the three OPEN IDs, shows their original conditions and checks a separate hashed reminder schedule; missing/changed mappings remain visible. No grading terms were invented.
- STATUS is 18,210 bytes (31,742 before); MEMORY is 12,164 bytes/79 lines (22,088 before). Complete before-images live in adjacent `STATUS_ARCHIVE.md` and `MEMORY_ARCHIVE.md`, with snapshot hashes. Pending obligations remain explicit, including METSUKE Run-12 apply work that previously sat inside historical narrative. Verified completed auto-memory/class-ruling tasks are distinguished from outstanding work. The 40Y no-tail correction is consistent across the handoff and docket; infrastructure disposition date remains estimated pending original-rule provenance.

Usage: [scripts README](../scripts/README.md). Evidence and checks: [validation manifest](2026-09-09_boot-corrections-validation.json), [test output](2026-09-09_boot-corrections-tests.txt).

## Validation and limits

36 affected regression tests and 4 existing funding-proxy tests pass. Coverage includes the 9.5%/10%/10.1% CFTC boundary through the CLI, positive/failed/partial child output, fallback quote clocks, unchanged ledger bytes, missing sections/schedules, and BOJ blank-draft/idempotency/tamper checks. Script inventory, owner read-cap, weekday and patch-applicability checks pass. Orientation contains about 60KB in 21 parts; the index alone never claims content was loaded. The calendar reader selects the explicit owner-maintained forward section rather than inferring dates from prose; stale scheduling rows still need owner reconciliation.

The baseline hashes for THESIS, TRADE, PREDICTIONS and all 19 existing workbook TSVs are preserved in the validation manifest. They remain byte-identical. BOJ/monitor orchestration was validated with saved primary evidence and offline fixtures; no full live market refresh or new BOJ chart transcription was performed in this implementation pass.

Consumer scans found no certified stale peer CFTC claim requiring a packet. Self hits were the preserved raw September 8/9 reports and declared legacy TSV. No peer edits or messages. External section-name redirects in STATUS remain intact. The ledger nudge returns its expected advisory because documentation moved without 15 market ledgers; all existing ledger bytes and their declared source vintages were deliberately preserved. Boot-output counts are not source-freshness certification.

## Remaining promotion check

Live `CLAUDE.md` is unchanged. Its default startup selection and descriptive threshold corrections are prepared as an applicable [candidate patch](../proposals/2026-09-09_boot-protocol.patch). The [operator packet](../evals/BOOT_CORRECTIONS_2026-09-09_RUN_PROMPT.md) implements `evals/README.md`'s fresh-session requirement; no judgment pass or results row is fabricated. Case 02 requires applicability review of its historical premise and incorrect weekday. Explicit new commands and data-layer corrections are usable now. Default prompt promotion remains pending valid fresh-session checks.
