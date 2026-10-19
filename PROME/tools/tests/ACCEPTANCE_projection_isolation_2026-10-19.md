# Projection test isolation and CATO record reconciliation

**Authority:** Will's 2026-10-19 request to assess/address CATO's cleanup review. Source: `AGENTS/CATO/runs/2026-10-19_1340_prome-retired-procedures-review.md`, push-confirmed `a183cfe54`. Existing actions only: L601 canonical, duplicate L636, related L519, L366 item ②. No new tracker, production behavior, dashboard duty or broader retirement.

## Acceptance before editing

1. The projection failed-render test writes its HTML, snapshot and receipt only inside its own temporary directory. It still observes rc1, preserves the previous snapshot and verifies a failed-build receipt. A missing receipt-path override must be caught by a mutation probe under an outer temporary witness; never allow the regression to touch the live repository.
2. Missing-companion coverage tests the retained library contract against the existing frozen amended HEARTBEAT fixture, not the current retired companion or live market prose. With a valid companion the fixture succeeds; missing companion withholds the amended view. No new production projection maintenance is implied.
3. Run the complete projection and desk-attention suites with repository writes denied, temporary output confined, and live dashboard receipt/state bytes unchanged. Distinguish selected-case CATO evidence from this full-suite acceptance. L519 needs record reconciliation only if this passes; no duplicate implementation.
4. DOCKET: L601 is the single surviving projection action until verified complete; L636 is folded/superseded by L601, not independently repaired. Only L366 item ② is superseded by existing dashboard retirement; ①③④⑤ and its due date/owner remain intact. L519 closes only on full-suite evidence. Preserve prior row text and physical line numbers. L523/L742 remain untouched.

Neighbour cases: ordinary failed build/valid historical fixture; overlap of duplicate backlog rows; wrong-owner receipt writes; missing companion and absent/seeded outer receipt; concurrent repository activity addressed by denying this test process repository writes and not restoring any file. No operational boot/closeout/render or other-desk edits.

This is a targeted retained-test repair and record reconciliation, not a canon amendment. Independent result review with a fresh counterexample is required because the isolation defect recurred. No extra plan-review round is required for this small repair. This directed follow-through is additional process work after today's three cleanup changes, on Will's fresh request; no general ceiling change is inferred.

reads: 1

2026-10-19 — independent RESULT read by `/root/deck_pause_result`: RELEASE, no blocking findings; read-only assignment closed out.

**IMPLEMENTED:** projection failed-render test overrides BUILD_PATH alongside STATE_PATH and asserts its own failed receipt; missing-companion test uses the existing frozen amended HEARTBEAT fixture. Desk-attention implementation unchanged. L636 folds into canonical L601; only L366② superseded; L519 acceptance reconciled. Shared L523/L742 untouched.

**TESTED (2026-10-19):** `python3 -B -W error::ResourceWarning /tmp/prome_projection_acceptance.py`: complete projection **12/12** plus desk-attention **10/10** pass. Temporary author harness imports both suites, redirects tempfile.tempdir to one outer temporary root, uses a Python audit hook to deny writes outside that root (including dir_fd-relative cleanup), and forbids subprocesses. Zero denied write attempts; live dashboard_build.json and dashboard_state.json bytes unchanged before/after; no restore or operational render. The isolated fd.main calls mock build(). Existing read-only live dependencies elsewhere in these legacy suites remain; this run certifies their current result and write isolation, not full fixture independence.

The fixed projection test additionally passes with both absent and seeded outer BUILD_PATH witnesses, leaving each unchanged. A temporary in-memory test mutant removing only the BUILD_PATH override writes the outer witness and fails on its missing own receipt: the new assertion detects the original defect without touching the repository. The normal suite also demonstrates valid frozen companion success and missing-companion withholding. The temporary harness is validation evidence, not a new maintained instrument.

**INDEPENDENTLY VERIFIED (2026-10-19):** result reader RELEASE, no blocking findings. Independently reran all **22/22** tests with the reviewed temporary write guard and ResourceWarning-as-error: no forbidden writes; live receipt/state bytes unchanged. Fresh counterexample forced the receipt writer to record ok:true despite rc1 and preserved snapshot: the new assertion rejected it. Fresh fixture counterexample substituted an unamended base: missing-companion coverage rejected that incorrect basis, while the normal frozen case passed. Seeded outer receipt AND its atomic .tmp sibling remained unchanged. Reader verified four-row conservation and L523/L742 unchanged; no repository edits, operational renders or restores.

**STILL UNRESOLVED:** L366①③④⑤, L523 and L742 retain their existing obligations. No cost measurement, hidden schedule inspection, live dashboard rebuild or broad legacy-fixture migration is claimed.

**Declared residue (2026-10-19 result read):** legacy read-only live dependencies prevent a claim of complete fixture independence. Existing generated docket-view size advisory (11,427 B versus 6,000 B budget) and L366 surviving items remain outside this repair. No new workstream created.

**Record checks:** 754 physical DOCKET rows retained; only L366/L519/L601/L636 changed; six-cell layouts, date/description/owner/source fields and all prior state/notes preserved. Generated docket and Will-queue views agree with their sources; weekday and scoped whitespace checks pass.
