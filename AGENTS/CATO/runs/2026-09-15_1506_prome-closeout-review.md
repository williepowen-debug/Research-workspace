# PROME September 15 closeout — CATO review

## Scope, revision and limits

Will asked: “Okay PROME has closed out its session. Want to take a look at the results and analyze?” Reviewed the `prome-9e` closeout and follow-up through `a45213b81ad660d74a7be50e1bcbe0d5551729f5`, including CATO's provisional registration, SL-5 delivery, selected desk obligations, final state records and audit limitations. PROME's inspected paths were clean at this revision; BRENT had live uncommitted work. No pull or edits to another owner's files.

This is an independent comparison of PROME's new completion claims with their evidence. CATO's earlier renderer/instruction implementations were not independently re-certified here; inspecting their behavior is author follow-up where that earlier authorship applies. PROME's feedback was already known, so CATO-boundary findings are post-contact verification, not blind convergence. No primary market-source validation, trade recommendation, gate re-grade, hosted artifact inspection or whole-fleet quality verdict is claimed.

**Assessment:** substantive deliveries landed, but completion prose still diverges from machine state and source evidence. Repair the specific record/consumer mismatches before adding more process documentation.

## Verified deliveries

- `PROME/ROSTER.md:170` contains the provisional CLASSIFICATION PENDING entry and manual-only restriction. This is a registration of the boundary, not RAV succession or automatic launch eligibility.
- `FORGE/PREDICTION_DISCIPLINE.md:32` contains the approved SL-5 pointer. The referenced SL-5 section and registration template exist. The ruling record preserves plan/result review findings. This review does not independently certify the full canon or resolve its seven declared result warnings.
- BOND's `RECEIPT.md:5` separates the delivered September 15 grade from confirmation of September 17 frozen bars. OSPREY's `L308_DOWNGRADE_WINDOW_CLOSED_2026-09-15.md` documents the consumer objection dispositions. FERT's September 15 G3 memo records its grade and source limitations. PROME's ORCH_LOG rows 141–146 now record six ASKED→RECEIPT outcomes. Those are durable owner claims about the asks; CATO did not inspect the live-session transcripts to independently establish their timing or completeness.
- Fresh `git fetch origin master` succeeded. Ancestry checks returned 0 for the final PROME closeout tail `a45213b81`, roster `f1bd2147a`, SL-5 `7c405ef62`, BOND `171d272ad`, OSPREY `376d7536a`, FERT `107e6ccfe`, and CATO's earlier repair `bd1c1b683`. Those commits are on origin/master.

## Findings

### F1 — High: FERT's rationale was converted into a false arithmetic comparison

**Source:** `PROME/DOCKET.tsv:204` says the $500/t India floor is “NOT above prevailing $443/t now or when set.” The source memo, `AGENTS/FERT/outbox/2026-09-15_from-FERT_G3-china-quota-floor-re-read-DOCKET-L204.md:38`, explicitly says “India floor $500 IS numerically above $443.” The previous line also qualifies the $443 figure as a global index, not a named FOB benchmark.

**Consequence:** the unchanged grade acquires a false supporting premise. FERT's stated reasons instead include the floor predating registration and contested enforcement/supersession. The memo's historical comparison has its own source limits; CATO has not independently validated that market history. A correct grade does not authenticate PROME's rewritten rationale.

**Repair:** correct the current L204 summary from FERT's actual reasoning, retain benchmark/enforcement caveats, and check dependent summaries for the same numerical inversion. Do not change FERT's grade or claim new market verification.

### F2 — High: BOND's later grade has no correctly dated coordinator obligation

**Sources:** `PROME/DOCKET.tsv:316` registers “dual-print grades” for September 15 and September 17 but retains a single September 15 date. The closeout appends “DISCHARGED … BOTH LEGS” and “RESOLVED,” while also acknowledging that the September 17 TIPS print was not graded. BOND's `RECEIPT.md:10` says “CONFIRMED, NOT GRADED, as instructed”; `AGENTS/BOND/docket/CATALYSTS.tsv:17` retains the September 17 grade.

**Reproduction:** the only PROME catalyst row naming `91282CRE3` or `10Y TIPS` is L316. Running `spawn_list.collect` over the unchanged snapshot with `today=2026-09-17` returns L316 as due September 15, `ACTIVE`, because BOND committed on September 15 and `classify` compares that date with the row's start. This is a conditional replay of current records, not a forecast of later commits. Confirming frozen bars satisfied today's narrower brief; it did not discharge the original later grading obligation.

**Consequence:** the future grade survives in BOND's own calendar but is not represented as a September 17 due item in the coordinator's driver. The earlier completed session can suppress a DARK classification for that later task. This does not prove the grade will be missed; it identifies the broken scheduling representation.

**Repair:** separate the completed September 15 obligation from a live September 17 grading obligation, preserving pre-registration evidence and BOND's ownership. Verify the September 17 coordinator view/driver with the existing September 15 completion as a negative control.

### F3 — Medium: four completed dispositions are still machine-open

**Sources:** `PROME/DOCKET.tsv:204`, `:308`, `:316` and `:395`; canonical parser `scripts/docket_view.py:110`, imported by `PROME/tools/spawn_list.py`.

**Reproduction:** `state_kind` returns `PENDING` for all four because their state cells begin with `PENDING`. Appended `RESOLVED`, `DISCHARGED`, and “PENDING text above is HISTORY” do not change the lead token. L395 is especially clear: its closing paragraph says the correction prevents tomorrow's overdue entry, but the parser still reports it open and the driver returns `PROME-OWNED`. A September 17 snapshot replay leaves the other three as old September 15 obligations.

**Consequence:** completion claims and the live inventory disagree. Repeated “corrected” prose has not corrected the property the consumer reads. For FERT, the later October 15 check IS retained in GATES.review_by; do not create a duplicate obligation while cleaning its spent docket instance. BOND needs F2 handled before terminalizing its row.

**Repair:** update the actual leading state to match the present disposition, then preserve old text explicitly as history. Regenerate affected views and check state interpretation, not merely presence of the word RESOLVED. Do not mark L125 terminal: its September 15–16 FOMC window remains pending intentionally.

### F4 — Medium: CATO is automatically enumerated by the freshness tool

**Sources:** `PROME/ROSTER.md:179` and `PROME/SCRATCH.md:21` assert that no instrument enumerates CATO and that `agent_freshness` only profiles it when named. `PROME/tools/agent_freshness.py:158` lists directories under AGENTS; its ordinary fleet mode consumes that list.

**Reproduction:** ran `python3 PROME/tools/agent_freshness.py` with NO `--agent` or `--all`. It returned rc=0 and included `CATO … 0 … 1 … 0 … DRAIN-FIRST` (one unread CATO packet in PROME's inbox). CATO was discovered automatically. This is not evidence that it was automatically launched or that message routing bypassed WALTER.

**Other instruments checked:** `read_cap_check.py --fleet` assessed 37 desks with no CATO; rc=1 reflected five desks over budget, not a CATO result. `wiring_census.py --all` did not include CATO; rc=2 reflected unevaluable other desks. Its enumeration is a scripts/tools DIRECTORY scan (`:118`), not FLEET_DIRECTORY. `spawn_list` reads dated DOCKET/GATES owners, and validate-all's read-cap leg delegates to read_cap_check. These do not share one universal roster predicate. CATO did not run every validate-all leg.

**Repair:** correct the claimed boundary to describe each consumer. In the bounded integration pass, decide whether freshness should omit manual-only sessions or present them explicitly without fleet-action cues, then test normal enumeration and direct queries separately. Do not add a CATO scripts directory or CLAUDE.md assuming registry exclusion alone protects every consumer. Preserve the provisional row; it is useful even though its surrounding explanation overclaims.

## Additional design and continuity observations

- **L402's proposed repair needs an identity contract.** It says decide OWNED/SHARED by the “committing author.” `git show -s --format='%an <%ae> | %cn <%ce>'` gives the SAME identity for WALTER `0951f361e`, CATO `ebeee2832` and PROME's roster commit `f1bd2147a`. Git author/committer fields alone cannot distinguish them. CATO's `Implemented-by: CATO` helps prospectively, but historical and uncommitted work need explicit attribution/UNKNOWN handling; mixed contributors cannot safely collapse to the last writer of a file. This is a defect in the proposed acceptance wording, not an implemented new classifier.
- **CATO roster explanation exceeds its evidence.** VIRGIL's missing directory is a member-specific exception, not a demonstrated class-wide exclusion. SPECIAL explicitly contains Codex RAV, so “every existing class assumes Claude Code” contradicts the same entry's evidence. Co-membership alone does not establish succession. Keep these as unsettled rationale, not governing taxonomy facts.
- **Late corrections did not reach every summary.** SCRATCH still labels its header September 14 and lists the already-committed CATO launcher/trailer fixes as open. Its generated docket stamp does not match the current DOCKET bytes. The SL-5 record's final “What happens to these” paragraph at `:131` still calls warning 8 permanently incomplete, despite its recovered/fixed row at `:101`. These are smaller instances of the same completion-propagation problem.
- **The final delivery is not independently certified by the earlier ARGUS receipt.** `argus_review.json` explicitly says the fixes and dispositions were self-tested and not independently re-reviewed. Its hashes for DOCKET/HANDOFF/ORCH_LOG differ from final bytes. `--verify-review --ref a45213b81 --paths …` returns CANNOT-EVALUATE because the baseline was advanced; that is expected for a prior manifest, NOT evidence of a new checker failure. The record establishes audit catches and author follow-up, not independent final-output verification. L378/L400/L402/L403 remain real pending work; documentation of a remedy is not its implementation.

## Recommended next pass

Correct F1; preserve the September 17 obligation in F2; normalize F3 and regenerate its consumers. Then address F4's consumer-specific manual boundary. Reconcile L402's identity acceptance before building a classifier. Use an independent reader on consequential control changes under the applicable owner rules; avoid a wider rewrite of the closeout system during these corrections.

**Implemented here:** CATO report and continuity only. **Checks performed:** source/consumer comparisons, parser and dated-driver replay, three instrument runs, local Git identities and fresh remote ancestry. **Independent limits:** stated above; no final whole-session certification. **Owner disposition:** not yet requested or received for these new findings. **Unresolved:** F1–F4 and the listed design/continuity residue. Delivery is directly to Will; no other owner's files were repaired.
