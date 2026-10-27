# CARL file audit — October 26, 2026

**Session:** began October 26; closeout crossed midnight into October 27 ET. File/date vintages are preserved.

The audit found real code defects, stale operating text and unfinished obligations. Mechanical repairs are complete within the reviewed perimeter; the research backlog and child freshness failures remain open. No forecast, probability, instrument threshold, convergence score or paper fill was changed. The current score remains 53/70, v2.6.6.

## Scope and evidence

Git root: `/home/willi/Research-workspace`; desk: `AGENTS/CARL`; runtime: OpenAI Codex, exact model UNKNOWN. Root CLAUDE.md, AGENTS.md and USER.md and the full local charter were explicitly read earlier this same conversation; startup receipt is `domain/sources/2026-10-26_startup-recovery/STARTUP_RECEIPT.md`. Additional on-disk AGENTS.md files at AGENTS/ and CARL/ are absent; the user-supplied instructions apply. Existing approvals were recovered, not reset. No child was launched and no other owner's state was edited.

The initial recursive inventory recorded 830 files and 193 active-text candidates, including historical artifacts and nested child directories. All 24 current Python files parse. The audit checked active instructions, scripts, canonical/mirror pairs, task narratives, inbox obligations, prediction windows, dependencies and TSV structure. Historical source sentences and every old attachment were not independently re-researched. `inventory.json`, `initial-checks.json`, `CHECK_RESULTS.json` and the focused inventories define the evidence perimeter.

## Repaired

| Finding | Repair and evidence |
|---|---|
| Brier CLI crashed on the prediction ledger's comment header | Canonical line-oriented TSV loader skips comments, rejects malformed/duplicate rows and retains unresolved/unscored exclusions. CLI now runs. Its maximum-prior heuristic is explicitly a legacy diagnostic, not the official first-call score. |
| Brier decomposition mislabeled grouped results and mishandled fractional MIXED outcomes | Uses actual outcome variance, labels the bin-mean decomposition and separately reports the raw-score difference. No official scoring convention changed. |
| Boot's staleness check used mtime and treated frozen ABS data as live | Replaced with the root content-clock/frozen-state/perimeter checker. Missing checker, timeout and empty failure cannot report clean. Actual child staleness remains visible. |
| Threshold script implied thesis confirmation from legacy price screens | Diagnostic-only banners, labels and JSON marker; unsupported NCO inferences removed. Existing numeric levels/operators unchanged and still need calibration review. |
| Threshold output mis-scaled HY spread units and displayed stale builder margins | Converts FRED percentage points to basis points for display only; removes static margin figures. Vendor quote basis/time are shown; previous-close fallback time stays UNKNOWN. Missing input coverage returns nonzero. No live quote run or security-master verification is claimed. |
| Revision TSV serialization could swallow subsequent events at literal quotation marks | Uses a real tab-delimited CSV writer. Regenerated canonical census: 151 parseable events, four status events UNCLASSIFIED. Original bytes and checksum preserved in `revision-ledger-before.tsv` / `revision-ledger-repair.json`. September 24 headline analysis remains explicitly historical. |
| Nine resolved or superseded tasks remained in OPEN | Removed verified false-open FERT roster, CRL-08, CRL-27, CRL-14/Doc54, Q2 card, original pilot delivery, card-wording, as-made ladder and September retail entries. Four remaining narratives reconciled. Generated index is now 22 threads. Every original row is preserved verbatim with crc32 in `roadmap-dispositions.json`. |
| Charter and script text falsely said WALTER never uses its delivery lane | Reconciled with §3.5.8 and actual September/October delivery. Unconditional BOARD scan, substantive review and acted/deferred rules remain. Empty mail is not evidence of no owed work. |
| Read-cap heuristic misread explanatory machine-read wording as a whole boot read | Charter now states machine lookup, not a boot read. Seven detected whole-read surfaces pass. No ledger was trimmed to satisfy a false perimeter. Charter/runtime composite coverage remains unassessed by this heuristic. |
| Human prediction mirror still claimed the CRL-05 void hurt CARL's record | Restored the September 24 withdrawal: undated 20% is invalid for first-call scoring; 75% governs and the void helped the record. This is an old correction reaching a stale mirror, not a new grade. |
| L786's CRL-21 status change lacked a current CHANGELOG entry | Added an explicitly late receipt for the already-implemented OPEN → STUCK change in result 5b18d5a88, preserving its mass-neutrality proof and all operative fields. |
| CRL-25 presented an obsolete private-credit count conjecture as current | Notes/mirror now flag BROCK's September 3 retirement of the predecessor. CARL's unscored pointer remains OPEN and administratively UNRECONCILED; no R2 fire was imported or scored. |
| SCRATCH malformed and duplicated its workbook table | Rewritten from the required template, with one health table and corrected UNKNOWN model text. |
| Old files appeared to give current instructions | Bannered August LAST_COMPLETION, April BUILD_PLAN and May WALTER liaison conventions as historical. Corrected frozen PORTFOLIO truth pointer, paper antecedent labels and five live path references. Child historical text was preserved. |
| WQ-516 I3 question unanswered, due October 30 | Answer packet to PROME declines a standing line: historical coverage is KB402/403, but no current decision/gate would use the proposed series. All five questions answered; no new study or backtest. |
| ISHM seam confirmation owed | Direct analytical answer confirms the four existing boundaries; no routing table or workload change. |
| Partial DR1 delivery and withdrawn criticism left as open mail | Consumed DEWEY's SYF Q3 descriptive leg as KB560. SCALE ONLY, no causal 50 bp grade; COF/BFH remain due November 13. Filed the superseded accusation and correction without inventing a new repair. |
| Completed delivery copies still live | Filed seven consumed copies with git mv, including the now-sender-committed WALTER tariff note. Receipt and source consideration remain separate. |

Twelve new regression tests and all 14 existing BOARD regression checks pass. Canonical prediction operative fields are checked against pre-audit HEAD in `forecast-immutability.json`; Notes and header bookkeeping are the only prediction-ledger changes.

## Still incomplete, owed or awaiting evidence

| Priority / next action | Finding and owner | Required disposition |
|---|---|---|
| October 27 regular open | Seven paper exit decisions already made; actual fills unavailable before that open | CARL records actual quote source/time and bid/ask or adverse 15 bp fill. Seven rows remain OPEN; no fabricated prices or scoring. |
| October 27 owner review | WQ-228 fintech review was due October 26 and is unperformed | CARL checks REGINALD agreement and available CCB/SOFI Q3 source joins; missing exposure stays UNKNOWN. Existing event remains in both calendars. |
| October 27 owner review | October 22 LABOR claims release remains UNREVIEWED | Keep original release date; next-review note now explicit. Do not treat a carried kill-leg state as a grade of this print. |
| October 27 releases | Confidence and EIA checks already registered | Use saved publisher dates and distinguish observation from release time. |
| October 28 | Pilot falsifier report promised for about September 10 has no delivery evidence | Locate or deliver the residual report to DAEDALUS. The original pilot was consumed August 28; do not re-open that delivery. |
| October 28 / existing owner gates | STUE ES-01/04/06 grades and assignment reconciliation, AFT/FSA follow-through | Still incomplete. PROME assignment presence UNKNOWN; no child launch assumed from a date or stale flag. |
| October 28 parent review | CRL-25's Q3 unscored pointer uses a retired owner instrument | Reconcile administrative disposition with BROCK's September 3 retirement. A successor's different population/rule cannot grade the old question. |
| October 29, 08:30 ET | GDP advance / September PCE read; DOC-P10 still prints October 30 | Use BEA-verified parent plan. DOC received a bounded calendar-correction packet; its threshold/window was not edited. EART collection-month grade remains separate. |
| Next authorized DOC/GIG/POP read | Past-window rows: DOC-P02 September, DOC-P05 Q3, GIG-P02 Q2–Q3, POP-P03 by September 30 | Evidence-based owner disposition or exact missing measurement. Packets queued in each existing inbox; no silent deadline extension or parent-side grade. |
| Existing child gates | 23 of 52 declared ledgers stale, some UNATTENDED | Real inherited failures; do not clear by touching files. Current scanner also excludes 13 TSVs in this working tree, including audit artifacts; this is not whole-tree certification. |
| Before writing affected ledgers | Eight TSV files have ragged rows or quoting/parser ambiguity | Parent frozen VX plus PHAN ML/PROVIDER, DOC ML, POP ML, GIG FLOW/VX/ML. `TSV-parser-review.json` checks raw and CSV parses. Determine missing-field positions with the owner; no blind padding or historical rewrite. |
| Next existing mechanical review | Four later revision status events unclassified; RED response not established | Keep historical September 24 result separate. Classify from rulings/artifacts before publishing a new benefit denominator. |
| Existing research backlog | GIG-P03/P06 instruments, FLOW-PHAN-06 unpublished leg, old V16 counterevidence staging, liaison calibration and tape/mark automation | Still unresolved or unbuilt. Legacy May ideas are not proof of current authority; no new commission or child spawn was inferred. |
| November 6 | ALLY matched vintage-loss measurement still unavailable; CRL-21 STUCK | Original-source checkpoint only, no forecast extension or automatic miss. RITM's mixed evidence does not prove accounting cushion exhaustion. |
| November 13 | COF/BFH DR1 descriptive Q3 legs | DEWEY still owes both under L567; no all-three completion claim. |
| Existing consumer watch / optional intake | Five live generic packets remain: stablecoin INFO, screwworm ACTION, optional FEMA, FERT baseline and ISHM price/volume | Stub reads and prior boundary intake are distinguished from full canonical-report consumption. Screwworm L797 is existing work; scenario arithmetic is not a forecast. No new standing line adopted. |

## Missing dependencies and limitations

- Claude-native hooks, skills and messaging were not assumed or invoked. Codex shell and existing-task tools are available; receipt acceptance does not establish recipient consumption.
- PyMuPDF (`fitz`) and `pdftotext` are unavailable. Installed pdfplumber/pdfminer and requests supplied the earlier PDF fallback; no installation is needed for these repairs.
- `fredapi` is absent, but current FRED scripts use urllib; its absence is an obsolete build-plan dependency, not a runtime blocker. requests, bs4, yfinance, pandas, pdfminer and pdfplumber are installed.
- No full live market boot was repeated for this maintenance audit. Changed logic was tested with controlled inputs; the canonical staleness and Brier CLIs were run against actual owned records. Legacy screen calibration and quote-source availability remain separate limitations.
- Reference scan: 37 candidates adjudicated; five current pointers fixed, six resolve relative to the owning child, eight are command/template/abbreviated notation, 14 are missing historical/proposal references, three are child historical suffix omissions, one is POP's wrong flat path. Missing proposals were not recreated as if approved.
- Research-retirement recheck repeated after midnight using the October 27 cutoff: four live/pending anchors retained, none retired. The August 27 CRL-29 registration is now 61 days old and remains exempt as a pending frozen prediction artifact. Exact references and the new age census are in `retirement-check.json`. No frozen/pending artifact was moved for age alone.

## Checks and delivery

`CHECK_RESULTS.json` and individual logs retain exact exits. Consistency: zero hard errors, six inherited soft advisories. Corrections: zero unreceipted named rows. Roadmap rendering matches regeneration; 25 docket events agree with their calendar twins. BOARD has no unrecorded action-addressed CARL item in the assessed INDEX, but hundreds of unrecorded non-action entries remain; a receipt count is not evidence of considering all signals.

Read-cap passes only the seven detected surfaces, not undeclared runtime/charter composite cost. The child-ledger checker still exits 1. The audit is complete within its stated perimeter; operational closeout remains PARTIAL for inherited child-ledger hygiene and the explicitly outstanding owner work. No new Will approval or capital action is required by this report.

Exact authored commits, fresh-fetch remote confirmation and notification/consumption states are recorded in the dated PROME delivery receipt and final chat response. Foreign dirty files are excluded; no pull, stash or rebase is performed over another owner's work.

Consumer propagation: numeric-only 0.0400 searches were nondiagnostic (1,131 cross-agent and nine self candidates; no certified stale series). Exact text searches for the withdrawn CRL-05 claim found no unqualified current copy in either perimeter. The remaining literal old wording found by targeted rg was an explicitly historical September before-image, retained. No peer correction packet was warranted from a bare numeric match. Logs: consumer-void-*.txt.
