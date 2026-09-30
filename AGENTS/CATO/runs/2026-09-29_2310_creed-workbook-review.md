# CREED workbook review — September 29, 2026

## Current assessment

**Accept the data reconciliation in `c6b0731c9`; CW1–CW4 close in the checked scope. CW5 narrows to validation of the new history counter.** Current counts are correct, and the named current views, colours, field meanings and history dispositions are repaired. Independent probes show missing/invalid history can still be accepted as usable observations. Finish that bounded guard correction; no rebuild, threshold changes or additional research recommended. The workbook is usable with these limits; operational benefit remains unmeasured.

Will asked CATO to examine CREED's workbook following the [ledger/prediction/recovery review](2026-09-29_2139_creed-changes-review.md). This assignment covers all workbook tables structurally, selected consequential claims and current-state relationships, and the scripts that consume/check them. It does not independently certify every research claim, reprice the market, review all bank exposures, or reopen the stopped broader Nano investigation.

**Snapshot/concurrency:** began at `b5fc5530e` with eleven dirty CREED paths; did not pull or edit them. Saved workbook inputs under `/tmp/cato-creed-workbook-review/` for stable reads. CREED committed its edits as `8b795b2a9` during review; all seven saved data/schema/scoreboard files exactly match that commit. The design spec is explicitly a historical build record, not a current task list. Only CATO's report and continuity change in this delivery. No owner edits, sends, agents, paid access or deployment.

## What holds up

- Parsed **34 VX vectors, 8 transmission chains, 47 KB rows, 11 prediction rows and 87 history rows**, with no TSV field-count errors. Shape validity does not establish column meaning or factual validity.
- Independently read archived Trepp August DQ PDF pages 2–3 and SS PDF page 2 at `AGENTS/WALTER/sources/2026-08_Trepp_CMBS_{Delinquency,Special_Servicing}_Report.pdf`. They support the current 12.00% office DQ, 16.90% office SS, 9.81% maturity-adjusted DQ, 81% matured-balloon share, and $3.16B transfers versus about $500.7M exits. The exact-12.00 no-fire rule and September's leg-1-only setup are consistent with the frozen terms. This is source verification of the named observations, not every narrative inference.
- Prior independent ARI/MBA grade and note-preservation checks remain applicable; no prediction-ledger changes in `8b795b2a9`. The new score is not evidence of demonstrated calibration. Kernel divergence for 004/007 remains disclosed and outside this review.
- The scan correctly distinguishes five numeric comparisons from six unscannable triggers, preserves the suspended bank level, and does not adjudicate a new fire. Its exit 1 here is the already-known office-DQ near-band condition, not a broken run.
- `8b795b2a9` closes **CD5** in the checked active lien-test surfaces: the analysis requires evidence linking the party to this specific lien, and the preserved research-agent text has an explicit superseding annotation. It also closes the prior PRED-010 waiting-text and issuance-certainty cleanup. No ownership conclusion is established by that correction. Earlier CD1–CD4 are not closed by this commit.

## CW1 — MEDIUM: the current views do not consistently consume evidence already on file

**Transmission chains (`workbook/FLOW.tsv`):** rows 01/02, lines 6–7, still say August SS has no print, maturity-adjusted DQ is 9.62%, and August adds no composition point. The primary PDFs above and the September 26 workbook refresh establish 16.90%, 9.81% and 81%. Row 05, line 10, still calls the old 5.54pp SS–DQ spread “THE GAUGE,” although `KB-CREED-034` and VX's full note explicitly reject using its direction alone. Row 06 leads with Moody's Q1 vacancy despite the declared CBRE Q2 basis; row 07 says 8/11 dividends held while the latest cohort is 7/11; row 08 remains on Q1 MBA holdings. Its dated header helps a careful reader but does not turn a LIVE current view into a frozen archive.

**Dashboard/history:** `VX.tsv:23` retains Q1 industry PDNA 1.53% and “Q2 QBP ~late Aug” while KB-022 and THESIS already carry Q2 1.44%. `VX.tsv:39` still gives life holdings $775B / +$3.3B Q1, and `VX_HISTORY.tsv:44` keeps Q2 PENDING with no numeric successor for VX-10.05, despite KB-047 and the accepted MBA grade. These are missing propagation, not reasons to redo the research. `VX.tsv:22` also remains Q1 community-bank reserve coverage; refresh it from its own matching perimeter, **not** the industry-wide 172.7% used elsewhere. This review did not independently retrieve the Q2 FDIC primary, so its bank figures here are internal-consistency evidence, not fresh FDIC certification.

**KB/task state:** KB-024/026 still announce unresolved approval paths after the registry records the ruling; KB-027 keeps the retired MF-dollar chase open despite KB-028 and the explicit no-reopen instruction; KB-038 still directs grading the now-resolved MBA pair. Preserve their dated facts and rationale, but mark the dispositions superseded and link the successor. KB-039 needs the split disposition: CREED grade done, Kernel still open. Scoreboard open rows 001/002 also retain July rather than August commentary; pinned row 001 must remain untouched, with current progress carried on the permitted scoreboard/registry surface.

**Consequence:** the answer depends on which “current” file a reader opens; old tasks and withdrawn interpretations can be restarted. **Closure:** reconcile these named consumers to existing source/decision records, preserve original prediction terms and labelled history, and inspect the whole affected row. Keep FLOW as a concise current chain map with old correction narratives reachable elsewhere; freeze any row the owner elects not to maintain.

## CW2 — MEDIUM: two displayed colours disagree with their own numeric bands

| Row | Displayed value | Written bands | Stored status | Arithmetic on the stated value |
|---|---|---|---|---|
| `VX.tsv:10`, overall CMBS DQ (1.02) | 7.85% | >7 / >8 / >9 | ORANGE | YELLOW |
| `VX.tsv:22`, community-bank reserve coverage (4.02) | 146.6% | <150 / <140 / <130 | ORANGE | YELLOW |

The second row's note itself says only the yellow line is crossed. No explicit basis exception explaining these two status cells was found. This overstates their mechanical severity; it does **not** establish that the broader thesis should be downgraded.

Do not blanket-recolour other apparent mismatches: VX-4.01 explicitly holds an indicative ORANGE after a basis change, and VX-9.03 carries uncalibrated provider bands. Those are disclosed exceptions. **Closure:** correct CW2's two statuses on refreshed, like-for-like values, or explicitly separate an analyst judgment from mechanical band state. Keep approved bands unchanged. The already-proposed band/value check can enforce that distinction once the exceptions are named; no new score system is needed.

## CW3 — MEDIUM before quantitative use: the history is a mixed evidence log, not an unambiguous series

`VX_HISTORY.tsv` has **five repeated vector/date keys**. Office-DQ February has 11.40 (line 7, superseded only in prose) and 11.20 (line 79); July has identical 11.91 observations twice (lines 11/51). August SS has NO PRINT and 16.90; August matured-balloon share has NOT PUBLISHED and 81. Vacancy has four entries under the same vector/date: CBRE, C&W, unavailable Moody's, and a basis-change marker. The bank series also uses both `2026-Q1` and `2026-03-31` for one period. Full notes disclose most of these issues; ordinary key/value queries do not.

**Demonstrated consequence:** counting raw rows yields office DQ **10 vs 8 distinct months**, office SS **8 vs 7**, and balloon share **6 vs 5**. A first-match February lookup can return the withdrawn 11.40. A last-row-wins rule is no general remedy: it selects the nonnumeric vacancy basis marker. No existing published statistic was shown to have used these faulty queries.

**Closure:** retain the audit trail but make the eligible series explicit: one canonical value per vector/provider/basis/observation period; revisions/placeholders outside that series or structurally marked and excluded; provider and period identity resolved before trends or n=12 counts. This can be done within the existing files; no database rebuild is required. Separate history's band state from evidence disposition. Sample count means valid distinct observations on the declared basis, not physical rows.

## CW4 — MEDIUM for structured consumption: the declared schema no longer describes the stored fields

`SCHEMA.tsv:9–11` promises Admiralty confidence, EMPIRICAL/ESTIMATE/ASSUMPTION epistemic states, and six lifecycle statuses. In KB, **five** confidences (022–026) are percentages instead, **16** epistemic cells fall outside that vocabulary, and **27** status cells do. PRIMARY-READ is a source-access state, not an epistemic class. Some expanded vocabulary may be useful; it must be declared rather than silently mixed with the existing meanings. A percentage cannot be converted mechanically into an Admiralty reliability/credibility pair.

There is also a concrete column-placement error despite valid TSV width: `VX.tsv:34` (9.03) has `Source=2026-08-20` and puts the full CBRE source description in `Cross_Links`. A source consumer receives a date and a routing consumer receives a citation.

**Closure:** restore source/cross-link fields, reconcile KB vocabulary with the intended schema, retain richer judgments in notes or declared fields, and reassess the five source ratings rather than inventing conversions. Validate field semantics as well as column counts. These defects do not by themselves invalidate the underlying evidence; they invalidate treating the current tables as uniformly typed data.

## CW5 — MEDIUM: the advertised checks do not cover the workbook's actual failure modes

- `CLAUDE.md:114` still runs an mtime-based `find` as the workbook's boot freshness check, despite the files' own warning that Git sync changes mtime. This mechanism is blind to a recently touched file with stale rows. The existing content-aware command `python3 scripts/ledger_staleness.py CREED --writes --abs-floor` flags FLOW as stale (13 STATUS writes behind in this run), while a newly edited VX file reads fresh despite CW1. Use the existing tool and inspect row-level dates for cited vectors; do not install another freshness tool.
- `registry/THRESHOLDS.tsv` obligation D names `scripts/threshold_scan.py` as the **counter** for the approved n=12 sample-size revisit. Full code inspection shows the script reads registry, VX and the fire log only; it never reads VX_HISTORY, counts observations or emits that obligation. Current distinct-month counts remain below 12, so no missed due revisit is demonstrated. The promised detection is nevertheless absent. After CW3, implement the counter in the named existing script or identify another explicit maintained mechanism; do not say it already exists.
- `creed_selfcheck.py` returns CLEAN on this workbook because it checks file-level fire markers and selected count phrases. That result is correct within its advertised scope and does not refute CW1–CW4. The threshold scan likewise checks trigger comparisons, not every dashboard colour or KB schema.

**Closure:** the boot instruction uses content vintage; cited stale rows are visible despite unrelated file edits; the n=12 obligation counts eligible observations and emits a due result in an isolated boundary test. No changes to frozen thresholds, sustain windows, prediction terms or Kernel state are implied.

## Lower-impact residue and stop condition

The history's lodging note labels 49/72 a “sigma” comparison while 72 is a mean absolute monthly move, not a standard deviation; the September preregistration similarly calls a mean absolute move a 1-sigma noise floor. Treat these as named heuristics, not sigma statistics. Correct via a dated clarification outside the frozen preregistration boundary; do not retroactively rewrite its terms. A broader statistical redesign is deferred.

Review complete. CREED can keep using the sourced workbook with its full notes for qualitative research; do not infer a new trade action or confirmed bank cascade from this review. The useful next result is consistent current answers across the existing views, with usable history and fields, not more rows. A subsequent verification should check these named closure conditions only.

Checks actually run: all-table TSV parsing and counts; schema comparisons; duplicate-key/unique-period queries; numeric-band examples with basis exceptions inspected; exact snapshot-to-commit comparisons; primary Trepp reads; prior grade applicability; full threshold-scan code inspection and execution; owner selfcheck; existing ledger-staleness scan. FDIC web fetch failed (403); no unverified replacement value was installed. No fresh market-price pull, full KB fact audit, code repair, hosted publication or independent test of operational benefit. Closeout: five-file weekday and whitespace checks passed; index empty before staging; orphan advisory identified only concurrent CREED SCRATCH/STATUS/catch-up edits outside CATO, preserved and flagged to Will. No memory, canonical numerical-series or STATUS edits trigger conditional checks. Exact CATO paths only; Git receipt delivered in-session.

## September 29 late follow-up — owner repair `c6b0731c9`

Will supplied CREED's completion account. Verified the named closure conditions against the committed repair, not merely the owner's tests. Initial shared HEAD was `857dd43a1`, clean and aligned with the then-local origin ref. CREED/PROME continued committing while this review ran; isolated probes extract **`c6b0731c9` directly from Git**. Later S8a refreshes and PROME's broader pass are not reviewed here. No owner writes or messages.

**CW1 CLOSED:** the six named FLOW rows now consume the existing August Trepp, Q2 bank/vacancy/cohort and MBA evidence. The full prior Current/Key_Insight cells survive verbatim in FLOW_NOTES; all six CRC32 checks match. VX bank and insurer rows and Q2 history are updated. KB-024/026 carry the completed ruling, 027/038 point to successors, 039 distinguishes CREED's completed grade from pending Kernel work; the original KB notes remain preserved. Scoreboard 001/002 now carry August progress without changing the pinned prediction ledger. Community-bank coverage 145.6% is explicitly identified as the community-bank measure, distinct from industry coverage 172.7%; the new FDIC primary read is **owner-reported**, not independently re-fetched by CATO in this follow-up.

**CW2 CLOSED:** 7.85% overall CMBS DQ and 145.6% community-bank coverage both correctly display YELLOW on unchanged bands. Declared basis exceptions remain visible. This is a display repair, not a new thesis downgrade.

**CW3 CLOSED for the current dataset:** the committed history has 90 rows, comprising 76 CANONICAL, 2 SUPERSEDED, 1 DUPLICATE, 5 CONTEXT, 5 PLACEHOLDER and 1 BASIS-MARKER. The earlier 87 records survive; three Q2 observations were added. The cohort's `4 of 11` value is normalized to numeric 4 with its cohort context retained. Period keys and provider/basis labels distinguish eligible rows from evidence history. Eligible office-DQ / office-SS / balloon-share counts are 8 / 7 / 5. The remaining validation issue below limits the guard's guarantee, not those current counts.

**CW4 CLOSED:** the named field shift is corrected, KB tokens conform to the amended declared vocabulary (including ANALYTICAL), and the five percentage confidences have explicit source-based reassessment explanations rather than numeric conversions. Original notes are retained. CATO verified representation and rationale preservation, not all source claims or the absolute accuracy of every Admiralty judgment.

**Preservation:** the complete PREDICTIONS.tsv, THRESHOLDS.tsv and fire log are byte-identical across this repair. Every VX Yellow/Orange/Red band cell is unchanged. The entire previous September preregistration remains an exact prefix of the amended file: the heuristic-not-sigma clarification is appended. Thus the repair itself changes no frozen prediction terms, threshold or recorded fire. Later market updates are a separate scope.

### CW5 — remaining MEDIUM guard limitation, bounded

The boot check now uses the existing content-vintage tool and explicitly requires looking at individual row dates. The n=12 counter is implemented and prints the correct current samples. Independent [probe code](2026-09-29_2310_creed-workbook-probe.py) and [results](2026-09-29_2310_creed-workbook-probe.txt) reproduce the positive cases: 11 monthly observations stay 11, an excluded duplicate or context provider adds nothing, 12 valid months emit DUE, and a data-bearing file without Role fails loudly. Replaying the original data against the new selfcheck catches both colour errors, the shifted fields, vocabulary defects and missing Role. These tests substantiate a substantial repair, not complete validation.

Additional independently chosen cases expose a common remaining gap in `scripts/threshold_scan.py:202–218` and `scripts/creed_selfcheck.py`'s history block:

| Input | Actual result | Required distinction |
|---|---|---|
| Empty history, or old header only without Role | Counter prints n=0; selfcheck CLEAN | Missing/unusable evidence is not a valid zero |
| 11 monthly observations + a dated entry in the same eleventh month | Counter emits n=12 DUE; selfcheck CLEAN | Monthly observation count cannot include a second day-key for one month |
| 11 observations on one basis + one CANONICAL row on another basis | n=12 DUE; selfcheck CLEAN | Distinct strings are not twelve comparable observations |
| 11 valid months + `2025-13`, or a twelfth row with blank Basis | n=12 DUE; selfcheck CLEAN | Calendar validity and declared basis must be checked |
| Conflicting CANONICAL duplicate | Selfcheck rejects it; counter silently deduplicates to 11 | Boot counter must not certify conflicted input merely because the closeout check will catch it later |

The counter validates the Role header only while iterating data rows and never checks Basis or period semantics. The selfcheck's period regex accepts impossible months and mixed cadence. All scan fixture return codes are 1 because the unchanged real registry already contains the known near-band condition; the distinguishing evidence is each counter message and selfcheck result, **not** the exit code alone.

**Closure:** validate required headers, available data, numeric canonical records, real observation periods, series cadence, consistent declared basis and conflicting duplicates before counting. Reject unusable evidence visibly rather than reporting zero or DUE; preserve valid per-series counts for unaffected series. Re-run the saved failure cases alongside the owner's ordinary boundary cases. Use the existing scripts; no new data collection or scoring system. No current false due memo, altered trigger, or incorrect current count was demonstrated. This guard issue need not block reading the corrected workbook.

**Receipt-log disposition accepted within scope:** reran the existing tools. FLOW clears; corrections_receipts is flagged only at 12 STATUS writes (content age two days in this run). Corrections boot check returns 0 with **zero unreceipted NAMED rows**, plus one separately disclosed ALL/broadcast advisory (`COR-20260925-13`). That supports noting activity noise without making a fake receipt or timestamp refresh. It does not certify that past receipt actions were substantively correct or prove the absence of every other obligation.

**Publication/status:** the user's “local only” account is stale relative to subsequent shared pushes. Final delivery will confirm via the required fresh-fetch receipt. No audit of the claim that WQ-316 is the only deadline was commissioned; its existing September 30 deadline is not changed. Review complete; retain only CW5's narrowed correction. CATO changed this report/continuity and added its isolated evidence probe/results, with no owner implementation.

Follow-up delivery checks: five-file weekday and tracked/new-file whitespace checks pass. Shared index empty before staging; orphan advisory finds concurrent CREED edits only outside CATO, preserved and flagged to Will. Further owner edits, including the selfcheck, began after the pinned probe; this verdict does not certify or condemn those in-progress changes. No memory, STATUS or canonical series edit triggers conditional checks. Commit/push receipt delivered in-session.

## September 30 — final CW5 verification at `dcee03b80`

**CW5 CLOSED in the named scope; CW1–CW5 now closed within this report's verification limits.** The shared validator rejects every remaining independent counterexample saved above while preserving normal boundaries and excluded-row handling. All 13 independent history cases match their expected distinctions; the owner suite also passes 23/23, including unaffected-series counts. Current selfcheck is clean. The fixed counter's current office sample remains 8, not 12. [Replay evidence](2026-09-30_1014_creed-cw5-replay.txt) and [new key-files audit](2026-09-30_1014_creed-key-files-audit.md) record scope and later narrative findings. The new audit does not reopen the repaired workbook findings or certify untested source claims. No owner implementation by CATO.
