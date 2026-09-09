# SAM boot corrections — proposed design

September 9, 2026. Requested by Will following the [startup review](../reports/2026-09-09_orientation.md). Design complete; implementation pending. No production script, prediction term, historical grade or trading instruction changes in this proposal.

The first objective is a boot that reports observations and missing evidence accurately. The second is faster recovery of current context. Both can ship within SAM's directory without adopting the broader state-rendering architecture in INFRA_AGENDA.

## 1. Correct the monitor's interpretation

Files: `scripts/thresholds.py`, `scripts/jgb_yields.py`; reconcile the descriptive KEY THRESHOLDS section in `CLAUDE.md` against the current owner sections in THESIS and STATUS.

| Current output | Proposed output / behavior |
|---|---|
| Sub-155: “THESIS CONFIRMING”, “Phase 2 carry unwind onset” | “USDJPY below the 155 watch level; mechanism unconfirmed.” |
| Sub-147: “Forced carry unwind zone” | “Forced-unwind investigation level; check funding, positioning and transmission.” |
| Sub-145 / sub-135: mechanical or forced insurer sales | “Historical insurer-exposure watch zone; named exposures and sales require evidence.” |
| FXY stop, targets and “consider partial profits” | Remove from default monitor. Keep FXY as a quote. Historical trade records remain intact. |
| USDJPY 150/162/165/167 as current trade/stop thresholds | Remove from the default active list: absent from current THESIS structural watch table. Preserve historical instructions in existing history. |
| JGB 30Y 4%: severe insurer stress | “Conditional demand-floor test; auction and institution evidence required.” Use consistent wording in both scripts. |
| JGB 40Y 4%: extreme stress | Retain the observation as long-end context, explicitly without a new mechanism grade. Remove the unsupported severity claim. |
| Brent below $90/$80: headwind resolved, BOJ comfortable | Remove causal and trade conclusions. Continuous BZ=F may remain a labeled context quote; suspend its automated threshold grades pending a named-contract/roll specification. The structural $120 reference remains in THESIS. |

Use a neutral “Watch levels crossed” heading. Keep current comparator operators and the descriptive 5% proximity window for surviving rows; changing alert calibration is separate work. Fix rendering to include the existing `stress` classification, which currently lacks a breach-output branch. Do not add replacement stop prices or trade triggers.

Quote retrieval must preserve the field actually returned and its source timestamp. A `previousClose` fallback is labeled historical and excluded from current crossing checks. Report missing symbols individually; partial price availability must not imply every symbol was checked. Report unknown quote age when the provider supplies no timestamp. Market-session freshness policies need explicit instrument rules; do not invent one universal age cutoff.

Verification: deterministic captured-output fixtures for sub-155, sub-147, JGB 30Y at/above 4%, partial quotes, and previous-close-only data. Assert observation, missing-input and date reporting; assert no entry/exit or mechanism-confirmation instructions. These test consequential behavior, not cosmetic wording.

## 2. Separate CFTC display correction from historical storage

File: `scripts/cftc_jpy.py`.

The retained -180,000 constant is intentional for the legacy `Pct_of_Jul24_Peak` column. Replacing that constant globally would mix denominators within one historical column. Preserve its schema, historical bytes and append calculation during this correction.

For the live display, compute against the ratified reference **-188,077 contracts, June 26, 2007**, labeled as the historical reference established from the reviewed record through August 2026—not an automatically refreshed all-time record. Example: -92,227 / -188,077 = **49.0%**. State separately that the workbook's legacy percentage column retains its old basis. Update the script header and reference label as well as the number. Net-long observations should say net long; do not describe a negative ratio as a positive short-fuel percentage.

Also correct the short-cover calculation to use prior shorts in both trigger and printed percentage: `prior_short = current_short - change_short`; compare the decline with 10% of `prior_short`. The current trigger uses current shorts, while the printed percentage uses prior shorts. A local fixture of 1,000 prior / 905 current / -95 change incorrectly triggers today at a true decline of 9.5%. Preserve the documented strict greater-than-10% comparator; reject invalid/zero prior denominators. This is an arithmetic repair to the descriptive monitor, not a prediction regrade.

Replace “unwind underway”, “max fuel” and “bullish crowded” with observed gross-long/gross-short/net changes. Historical resolver contract gates remain untouched.

Verification: 49.0% example; net-long handling; 9.5%, exactly 10%, and above-10% decline; invalid prior denominator; existing-date idempotency; historical TSV byte preservation and unchanged legacy calculation for newly appended fixture rows. Scan actual code consumers before any later schema migration.

## 3. Make boot failures explicit

File: `scripts/boot.py`.

Confirmed locally with an injected failed child returning `ERROR: fixture failed`: condensed output prints “ran cleanly, no alerts”, although the final summary correctly returns exit 1. Branch on execution success before filtering text. A failed child must print its failure reason; successful execution without matched lines should say “completed; see detailed output”, which makes no data-quality assertion.

Preserve raw stdout/stderr in an explicit report path; print that path and a concise cause for failure, timeout, missing script or BOJ review requirement. Continue independent legs and retain a nonzero aggregate exit when a required leg fails. Include inventory drift in the aggregate result—normal boot currently prints drift but only `--tools` returns failure for it.

Separate “script completed” from “source refreshed.” Existing scripts have different cadence and skip behavior, so do not infer fresh data from exit zero. Initially show content-derived observation dates where available and otherwise mark freshness unverified. A later common result schema is optional, not a prerequisite for these fixes.

Correct help text: `--quick` currently skips options only, despite claiming it also skips auction lookback; options are checked daily, despite comments calling the schedule weekly. Preserve runtime behavior and document it accurately in this pass. Fixing incomplete same-day options snapshots is a separate small follow-up: require the configured expiry set, not merely one dated row, before skipping.

Verification: injected success/error/timeout/missing-child cases; failure with no recognized emoji; inventory drift; preservation of final nonzero status and raw diagnostic output. No market fetches required for these tests.

## 4. Give a changed BOJ chart a complete recovery path

Files: `scripts/boj_ois.py`, `workbook/BOJ_OIS_README.md`, existing `workbook/boj_ois_reviews/` schema.

Keep exact image-hash, method, date, arithmetic, term and expiry checks. When an image is unreviewed, offer an explicit `--prepare-review` operation that saves source page, original image and a manifest of URL/retrieval time/hash into a dated SAM research package. Emit a local image path and a draft transcription template with empty numeric fields. The operation does not write quote rows.

SAM opens the image, supplies the transcription, then validates and ingests using the existing workflow. This is an assistant task; it need not become a recurring user permission question. If the publisher changes the image during review, reject the mismatched review and prepare the newer image. Repeated preparation of identical bytes should reuse the same evidence rather than accumulate copies.

The old reviewed quote may appear only with its historical vintage. A successful prepare operation means evidence saved, not a current quote validated. Automatic OCR is deferred until there is evidence that its errors can be detected reliably.

Verification: changed-chart fixture creates evidence but zero ledger rows; reviewed chart passes existing tests; expiry and changed-during-review still reject; error HTML cannot become a chart. Retain the existing ten BOJ regression tests.

## 5. Repair the handoff and shorten context loading

First reconcile the live contradictions, then trim history. Initial replacements:

- MEMORY item 0b: “Before Sep-29, rule a tenor-appropriate 40Y test: uniform-price 40Y has no yield/price tail. Keep the historical Sep-3 30Y grade and existing counter unchanged. Rounding treatment remains a separate issue for tail-bearing auctions.” Carry the same distinction in STATUS and NEXUS; the calendar already states it.
- MEMORY item 0c: “Review INFRA_AGENDA disposition around Sep-18; date is an estimate pending provenance verification.” Trace the governing ruling before treating this as an automatic retirement deadline; elapsed time must not silently close it.
- Reconcile other items labeled “owed” against their destination artifacts before carrying them again. The fleet memory index already names `finding_retired_figure_relabelled_onto_another_subject_evades_its_guard`; verify the file's substance before declaring the corresponding local task complete.
- Update obsolete charter/reference wording at its live home. Keep dated prediction terms and version-history passages unchanged, with history clearly separated from active instructions.

Introduce an explicit **orientation mode** and retain the existing full monitoring default. Proposed `boot.py --orient` produces a local-only read packet and performs no network calls, market writes, inbox moves or prediction grades. `--quick` keeps its existing meaning. Intent examples belong in CLAUDE: “load context/read starting docs” selects orientation; “refresh SAM/current markets” selects monitoring. Ambiguous requests should state which mode was chosen.

The orientation packet includes current THESIS identity/pillars/channels/thresholds, STATUS current state, forward calendar rows, two newest timeline entries, complete MEMORY, calibration warning and all OPEN predictions. Use stable headings and checked section boundaries, never fixed line numbers. Missing or duplicate required headings fail visibly. Print included paths, source hashes, section names and bytes; a read list alone is not proof the contents were loaded.

Move superseded session prose into SAM's existing archives with explicit pointers. Preserve pending obligations and load-bearing caveats. Pilot target: current STATUS below 20KB and each emitted chunk below 16KB; measure the full packet before setting a total cap. If over budget, report it and require section reads—never silently truncate. This addresses my oversized-read mistake as well as document growth.

Verification: current retirement/no-successor state, all three OPEN predictions, BOJ unavailability, corrected 40Y obligation and latest handoff survive extraction; missing/duplicate headings fail; orientation causes zero network calls and zero file mutations. Record emitted bytes and elapsed time; make no token-savings claim without measurement.

## 6. Add prediction reminders without automatic grading

Start with a reader for `thesis/PREDICTIONS.tsv`: validate schema/IDs, derive the OPEN count from rows, and show each OPEN row's verbatim Timeframe, Prediction and Notes. This immediately eliminates reliance on a stale preamble count.

For reliable countdowns, add a small SAM-local scheduling sidecar keyed by prediction ID: ISO due date, timezone, boundary rule, and hash of the authoritative row's condition/timeframe/notes. Populate only after checking the original terms. SAM-28/31 retain September 18 close after the BOJ decision; SAM-33 retains December 31. Do not invent an exact clock time where “close” is undefined.

Every OPEN ID must have either a validated schedule or a visible scheduling gap. Changed conditions invalidate the sidecar join and require reconciliation. At the boundary print “review due”; never resolve, fail, activate or retire a prediction automatically. Show activation clauses for SAM to evaluate; semantic activation automation requires a separate explicit specification.

Wire this reader into both orientation and monitoring modes. Unknown legacy status tokens or malformed rows must produce a diagnostic rather than disappear from counts. Keep the frozen prediction ledger byte-identical.

Verification: three current OPEN IDs; stale count in preamble ignored; missing schedule, changed row hash, malformed TSV and unknown status all visible; before/on/after due-date behavior; zero prediction writes. No historical rule tuning.

## Delivery order and completion evidence

**First change set:** monitor semantics/quote provenance, CFTC display/arithmetic, boot failure reporting, and the concrete handoff corrections. Highest value: remove authoritative-looking errors.

**Second change set:** BOJ evidence preparation plus prediction listing/countdown. Existing review and grading authority stays with SAM.

**Third change set:** orientation mode and document extraction/compaction, measured against this boot. Existing INFRA_AGENDA proposals for full structured state, fleet observability and expanded evals remain separate decisions; do not treat this design as wholesale adoption.

Run targeted deterministic tests, existing affected tests, read-cap/weekday/link checks and scoped consumer scans. A non-trivial charter boot-protocol change also requires the existing fresh-session evaluation process in `evals/README.md` before promotion; prepare the candidate and operator packet first, and report the eval as pending until actually run. Inspect whether the dated cases remain applicable before scoring; no rubric contamination or simulated pass.

Commit each change set with explicit SAM paths. Rollback is a scoped revert of the implementation, never a workbook-history rewrite. The thesis remains v1.7 unless a separately argued research decision changes it.

This design session encountered uncommitted PROME work. No pull was attempted, no peer files were changed, and this proposal does not depend on the peer work. Commit locally and defer publication under the shared-workspace protocol.
