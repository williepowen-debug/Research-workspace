**Historical snapshot from earlier in this session. Current completion and next steps: [closeout](2026-09-14_codex-closeout.md).**

# PROME owed-work review — 2026-09-14

Read-only review of the docket, current continuity surfaces, ruling records and selected implementation artifacts. Dates below are the repo's registered dates, not an independently refreshed market calendar. No desk launches, canon edits, docket dispositions or live ledger writes were made for this review.

## Assessment

PROME has concrete implementation and verification work owed. The backlog also contains completed sub-items, event/access waits, future grades and standing conditions; treating every open row as a build task would misdirect work.

The standard open-row instrument returns **135 rows**, including **3 past-dated rows** and **12 without a calendar date**. Those are parser results, not a certified count of unfinished obligations: **L247 is unfinished but omitted**, because its state begins with completed sub-items. A scoped scan for explicit continuing obligations in terminal-leading states found L247; the other hits were a transferred obligation and historical text beneath a completed receipt. The resulting past-dated set includes at least **four rows**, two of which are external-data waits.

## Recommended order

| Priority / registered date | Work and next concrete step | Completion assessment |
|---|---|---|
| **First — September 15, L303** | Transplant the four approved prediction rules from the WQ-161 ruling record into `FORGE/PREDICTION_DISCIPLINE.md`, with the prescribed plan and result reads. | **Approved, encoding owed.** WQ-161 covers non-resolution as status, the mass-neutral retrofit test and proof at patch time; WQ-163 item 3 requires amendments to re-earn their certificate. The draft is already written. Its September 15 deadline precedes ZHAO's registered September 16 resolutions. HANDOFF's September 16 shorthand is late. Keep the separately proposed SL-5 tie-set clause distinct from the four ruled bullets. |
| **Overdue — September 9, L247** | Finish the outcome-vector specification's F3 fields (`source_masses`, `normalization`) and resolve F8's carrier against the actual follow-on obligation. Obtain RED's outstanding F1 recheck before building. | **Partly completed, still open.** F2/F5 and F4 are recorded closed. The state explicitly says F3/F8 remain pending, but its leading `F2 + F5 CLOSED` hides the row from the open list. The spec mentions the fields and carrier in dispositions; that is not the same as a fully specified, verified completion. |
| **Before treating the repair as verified — no separate date established** | Independent review of the final contract-identification changes in `FORGE/tools/market-data/fetch.py`. | **Implemented and author-tested; independent verification owed.** The acceptance record explicitly says the final fixes were written after the reviewer's last look. Do not inherit its earlier “review closed” headings. |
| **September 16, L392** | Observe Brent contract quotes near a close and overnight to calibrate the 900-second stale cutoff, or establish a quote-cadence basis. | **Calibration owed, separate from review above.** Current code refuses identification when the matched candidate is stale; other candidates' staleness is advisory. The behavior change is present; the number remains uncalibrated. |
| **September 16, L378; September 17, L381** | Reconcile existing orchestration instructions and mechanize closeout-ask tracking using ORCH_LOG. | **Unfinished.** The playbook still demands wave approval without pointing to existing grants; COMPLETION_SPEC starts from the agent's summary; CLOSEOUT still uses idle + committed as its verification criterion. Track assignment, delivery, integration, closeout request and completion distinctly. Preserve existing authority, caps and preflight. The row calls for bounded reconciliation and observation of two ordinary sessions, then stop. |
| **September 15, L335** | Reconcile the stale three-defect description with L336's repairs; retain and specify the actual notes-history gap. | **Original repairs present; residual reproduced.** See below. This is not three untouched implementation tasks. |
| **September 19, L291/L292/L333** | Prepare the spawn-driver and ARGUS trial grades from recorded runs; review and adopt or disposition the cadence reader proposal. | **Evaluation and PROME integration owed.** DAEDALUS delivered its cadence specification September 8. `spawn_list.py` still states cadence is not modeled in v1. Do not send the delivered specification back to DAEDALUS as missing work. |

### L335: what is actually left

Current `wq_ledger.py` compares semantic fields and distinguishes same-day payload changes. **All 10 existing L336 ledger regression tests passed** during this review, including corrected records, same-minute updates, A→B→A changes and rejection of consecutive no-ops. `decision_deck.py` contains the millisecond-plus-random tap ID and disables both buttons while a write is pending. L336 records the September 11 repair commits.

However, `live_state()` does not retain ordinary OPEN-row notes as a semantic field; it extracts selected information from them. In a temporary copy of the existing queue fixture, changing only an ordinary note left the projected row identical and `diff_state()` returned `None`. Thus a notes-only correction can still disappear from history, through **projection loss before comparison**, rather than the old comparison bug. No live ledger sync was run. Hosted tap persistence was not verified in this runtime.

## September 19 work should stay grouped

- **Obligation visibility — L368/L370, plus the newly identified L247 omission.** The spawn candidate reader still suppresses work using prose `COVERED` annotations; the closeout gate still tests an almost-exact `PENDING` string. The newer `--open` inventory avoids COVERED suppression, but still depends on the lead state token. Distinguish assigned work still owed from discharged work. Preserve Will's instruction to handle the driver redesign at the scheduled review.
- **Audit scope and shutdown — L360/L367/L362.** Review stale audit perimeters when HEAD changes, disagreement between explicit and discovered review scope, fail-closed error handling, and reviewer agent definitions that cannot emit the required structured shutdown response. These are trial inputs with registered remedies/questions, not permission to start an unrestricted redesign.
- **Measurements and maintenance — L361/L358/L359.** Re-measure claims at closeout; carry the actionable spine-audit residue; fix or disposition missing dashboard tiles. L358 explicitly says its 56 raw minor findings are not 56 tasks. The audit itself ran September 12; it is not overdue.
- **L364 is held by ruling.** The distinction between “PROME must handle this” and “wait for Will” must survive, but changes to the named checks' severity are not authorized by the open row.

## External dependencies and coordination owed

| Row | Actual remaining obligation |
|---|---|
| **L332 — September 13, CORAL/MARCO** | CORAL delivered the MSI grade September 13. One reconciled Florida enrollment figure remains missing; headcount, a ten-day change and budget FTE are different bases. MARCO remains reserved to Will under the later instruction / WQ-243. Do not respawn CORAL for its completed leg or silently release MARCO. |
| **L140 — September 8, OSPREY/BRENT** | Producer-direct Russia diesel evidence remains unresolved. The latest owner recommendation rekeys the work to publication events. Carry the dependency, rather than interpreting the old date as a daily retry order. |
| **L198 — September 8, BRENT** | PortWatch's specified missing rows are access-blocked; the owner says no calendar/next-boot requery. The EIA leg is complete. Unlock on publication of the missing evidence. |
| **L376/L377 — September 16, RED/VIOLET** | Resolve the FT-10 archive/session-allocation issue before grading and retain the delivered conditional-selectivity caution. PROME coordinates; the owners grade. |
| **L380 — September 16, DAEDALUS** | Resolve the read-cap remedy problem: rotation alone cannot reach the target on two measured standing-state structures; a structural split is a different operation. The density relationship remains a hypothesis. TERRY's near-cap warning is a separate signaling issue. |
| **L379 — September 17, TERRY** | Owner's structural STATUS pass and a cold read must preserve the sole home of live capital rules. PROME routes the work. |

The registered week also includes Tuesday's FERT/OSPREY/BOND work; Wednesday's FOMC, VIOLET/LABOR/WPSR and HENRY grades; Thursday's correction-closure sitting and BOJ window; and Friday's WAL expiries, VLO reaffirmation, CRMT termination and remaining owner deliveries. These belong on the coordination slate, not in PROME's coding backlog. The USO September spread is already closed; the expiry row's remaining live legs are WAL's.

## Other continuity obligations

- HEARTBEAT requires a cold read before further edits under its existing stop. Its fuller re-base remains registered; ACTIVE_DECISIONS has an any-append / September 21 rotation trigger. Use fresh measurements when acting, not old prose byte counts.
- Reconcile the stale CORAL and FALCON summaries identified in the boot report, and the dates/status contradictions above, when their owning surfaces are next updated. A green gate or an active owner is not evidence of completion.
- The Decision Deck findings remain parked in the separate review: inaccurate explainers/classification and publication-size work under L393. This report does not reopen that task.
- Preserve the later outcome reviews: NEXUS's October 7 seat evaluation and the November 7 closed-position review. Process repairs must not displace the research operation's outcome checks.

## Evidence and limits

Key sources: `PROME/DOCKET.tsv` physical rows cited above; `PROME/STATUS.md`; `PROME/HANDOFF.md`; `PROME/proposals/2026-09-10_wq161-prediction-canon-RULED.md`; `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md`; `AGENTS/DAEDALUS/design/2026-09-08_DESK_CADENCE_SPEC.md`; `PROME/tools/tests/ACCEPTANCE_fetch_contract_identity_2026-09-14.md`; the implementation files named above. The full parsed open inventory and scoped row extracts are in `/tmp/prome-owed-review-20260914/` for this session.

Validation: 10/10 existing L336 ledger tests passed; an isolated notes-only fixture reproduced the remaining projection gap; current source confirmed the stale-PENDING gate, COVERED filter and conflicting orchestration sentences. These checks do not independently certify every repair in the backlog. Native Claude session presence and hosted Artifact DB access were unavailable; no claim about live desk presence or hosted Deck freshness is made here.
