# Docket reconciliation — September 14, 2026

**Authorization:** Will: “Okay approved go ahead with dockey reconciliation.”

**Scope:** correct the coordinator's docket against existing completion evidence. Preserve existing physical row numbers and original dates. No research judgments, gate levels, code, owner files or launch permissions change.

**Baseline:** `a993a451b9402cd9803a59d6f77896d072524482:PROME/DOCKET.tsv`. Replaced prose remains available in that Git revision. This report records the reconciliation; the live docket owns the resulting obligations. The earlier owed-work report is a pre-reconciliation snapshot.

## Changes

| Docket row | Reconciliation | Remaining work |
|---|---|---|
| L140 | Put BRENT's publication-event retry instruction ahead of the obsolete next-boot instruction. | Missing Russia primary text, diesel/gasoil flow and matched crack evidence; existing October 1 full read unchanged. |
| L198 | Make ACCESS-BLOCKED and its exact publication unlock explicit; withdraw the obsolete calendar retry. | PortWatch August 31–September 1 rows. Preserve the ungradeable lag-test leg and completed EIA leg. |
| L247 | Restore the `PENDING` lead token; identify completed and remaining specification/review legs. | PROME F3/F8 and RED F1 review; no implementation or activation authorized by reconciliation. L314 already exists. |
| L292 | Record DAEDALUS's delivered specification and assign remaining adoption/reader integration to PROME. | September 19 grade; proposed cadence semantics remain proposed. |
| L303 | Point to the completed ruling draft and retain September 15 as the encoding deadline. | Four approved bullets; separately proposed SL-5 transplant is not ratified here. |
| L332 | Retain CORAL's delivered grade, remove obsolete darkness/inbox counts and the contradictory promise to spawn MARCO. | MARCO contribution and one comparable Florida enrollment figure. Will's MARCO reservation remains. |
| L335 | Replace the obsolete three-defects-all-open account with the actual ledger coverage residual. | Notes-only history coverage; historical hosted tap loss remains unknown. |
| L392 | Separate calibration from final-code verification. | Calibrate the stale-quote cutoff; final-code review is L394. |
| **L394, appended** | Give the existing owed final-code verification a visible owner, acceptance condition and coordinator target of September 16. | Independent review of the final contract-identification implementation. The date is a coordinator target, not a reviewer commitment. |

## Evidence ledger

| Claim | Exact artifact | Verification | Observed result | Disposition |
|---|---|---|---|---|
| **VERIFIED:** original F2/F3 ledger repairs are present and pass their regression set. | `PROME/tools/wq_ledger.py`; `PROME/tools/tests/test_wq_ledger_L336.py`; L336 | `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s PROME/tools/tests -p test_wq_ledger_L336.py -v` | 10 tests pass, including corrected semantic fields, same-day changes, oscillations and rejection of consecutive no-ops. | Narrow L335; do not rebuild completed repairs. |
| **VERIFIED:** ordinary OPEN notes can be lost before comparison. | `wq_ledger.live_state()` and existing `fixtures/wq_ledger/WILL_QUEUE.md` | Copy fixture to a temporary directory; replace first row's Notes em dash with `ordinary factual correction only`; compare `live_state(..., [])` before/after. | Projected WQ-901 row unchanged; `diff_state` returns `None`. No live ledger writes. | Retain source-to-ledger coverage as unfinished. |
| **VERIFIED at source; hosted behavior UNKNOWN:** tap ID/button repair is present. | `PROME/tools/decision_deck.py`, tap handler; L336 repair commits | Inspect full timestamp plus random suffix and both-button pending-write disable. | Original code defect has a repair. Hosted history was not inspected. | Do not assert historical tap loss or live hosted verification. |
| **VERIFIED:** Kernel work is incomplete but omitted by the open reader. | Baseline L247; `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md`; L314 | Compare explicit pending legs with shared `list_open` result. | Non-PENDING lead hides a row that expressly retains F3/F8/F1. | Correct state lead; keep original date and review requirements. |
| **VERIFIED:** cadence specification was delivered. | `AGENTS/DAEDALUS/design/2026-09-08_DESK_CADENCE_SPEC.md`; `PROME/tools/spawn_list.py` | Read delivered spec and current reader header. | Spec exists; reader says cadence not modeled in v1. | Correct L292 ownership/completion split. |
| **VERIFIED:** prediction encoding is approved and due September 15. | `PROME/proposals/2026-09-10_wq161-prediction-canon-RULED.md` | Read four drafted bullets, ruling and insertion procedure. | Approved encoding is owed; the draft's procedure and deadline are explicit. | Correct L303's source and stale conditional wording. |
| **VERIFIED as owner instructions:** L140 and L198 have different retry dispositions. | `PROME/inbox/processed/2026-09-14_from-BRENT_barrels-vs-routing-the-tape-priced-it-once-on-the-attack-day-and-freight-is-still-repricing.md`, “YOUR ASKS, ANSWERED” | Read the L140/L198 instruction directly. | Publication-event retry retained for L140; L198 unlocks on the specified PortWatch rows. | Remove competing obsolete retry instructions. No new source retrieval claimed. |
| **VERIFIED as recorded completion/reservation:** CORAL's grade is delivered; joint task remains open and MARCO is reserved. | Baseline L332, CORAL receipt `7035b2b3b`, WQ-243 | Read current row's dated delivery and later restriction. | Old promise to spawn both conflicts with the reservation; the common-basis figure is still missing. | Reconcile coordinator text without changing the grade or launch authority. |
| **VERIFIED as an outstanding verification requirement:** final contract code has not been independently accepted. | `PROME/tools/tests/ACCEPTANCE_fetch_contract_identity_2026-09-14.md`, “Completion states” | Read final completion block, rather than earlier “review closed” headings. | Implemented/author-tested are distinguished from independently verified; final re-review explicitly owed. | Append L394; L392 retains calibration scope. |

## Validation and independent reads

**Plan read:** independent `docket_plan_read` returned three blocking findings: removing COVERED made L198 a new DARK spawn candidate; L303 retained an imperative to transplant proposed SL-5; L392 retained a false verdict consequence for a stale nonmatched quote. All were corrected before the live edit. Nonblocking findings were addressed by explicit suppression on L140/L332, a data-row-only schema invariant, and creation of this receipt. The reader made no edits.

**VERIFIED:** exact comparison against the baseline changes only L140/L198/L247/L292/L303/L332/L335/L392 and appends L394. All existing dates, physical row positions and unrelated bytes are preserved. Data rows have six fields and both files pass the shared schema loader. The shared open reader changes 135 → 137: L247 becomes visible and L394 is added; no open obligation disappears and L336 stays resolved.

**VERIFIED:** the independent counterexample is now an executed check using `spawn_list.collect`, September 14, a seven-day horizon and a frozen September 1 self-commit. L140/L198/L332 are suppressed in both baseline and result, while remaining L247/L292/L394 work is PROME-OWNED, never a domain spawn. Unchanged rows retain identical dispatch output. Explicit COVERED annotations implement existing waits/reservation; they do not mark the underlying work complete. General COVERED parsing remains L368.

The existing ten ledger regression tests pass. The temporary notes-only reproduction confirms the retained L335 residual. The live docket passes the weekday check and scoped whitespace check. Validation scripts and output are under `/tmp/prome-docket-reconcile-20260914/` for this session; the commands and observations above are the durable evidence. Review of this metadata batch does not certify the underlying code or research.

**Result read:** independent `docket_result_read` verified the row perimeter, dates, schema, open inventory, frozen dispatch, ten tests and cited evidence. It found one blocking wording issue: L335 implied the prior L336 review certified the final repairs, although C2 reviewed `ee79e1ef6`, graded B2 NOT MET and preceded subsequent fixes. Corrected in one result pass: the state now explicitly disclaims independent certification of those underlying repairs. No rule meaning changed; no third read. The wording correction received author verification, not a further independent read. Both review agents completed read-only with no file changes.

## Declared residue

- **September 14 result-read counterexample, VERIFIED by PROME reproduction:** changing WQ-901's Item body from `Some body text.` to `Material evidence-basis correction.` while preserving its bold title also leaves `live_state(..., [])` unchanged and `diff_state` returns `None`. The residual is source-to-ledger coverage and extends beyond Notes. This finding is declared in L335's notes for the same follow-up; underlying code is unchanged.
- Reader defects registered at L368/L370 remain unchanged. Correcting L247's state fixes this instance; it does not repair general obligation parsing.
- Original calendar dates remain visible for the two publication/access waits. Their explicit wait instructions govern retries; no new scheduler behavior is implied.
- Hosted Deck access and tap-history inspection are unavailable in this runtime. The earlier Deck review remains a separate task.
- Prior continuity reports remain dated snapshots; this reconciliation does not copy docket obligations into every historical summary.
