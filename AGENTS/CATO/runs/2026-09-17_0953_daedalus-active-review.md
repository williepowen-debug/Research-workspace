# DAEDALUS active-work review — September 17, 2026

Will requested examination and analysis while DAEDALUS remained active. This is an interim review of delivered work, not its final closeout. Main revisions: `6e63c5eb9`, `00f179cc1`, `460422749`, `84cc5a47a`; latest observed shared HEAD `e6abbfd1b`. Production/profile/wiring work and scanner edits were still in progress. No owner files edited, no messages sent, no fleet agents launched.

## Assessment

Substantial useful work, but parts of its synthesis overstate what its evidence establishes. Correct the gate-reader perimeter before using that sweep to justify new standards or owner re-registration. Reconcile the fleet totals and preserve the pilot's original success test.

Useful contributions include the correction-closure ruling package's concrete decision breakdown; distinguishing missing receipts from proven failures; the gate sweep's separation of source vintage, observation count and reset rules; and identifying that FERT's Pink Sheet monthly $/mt context is not a matched base rate for a DTN weekly $/ton trigger. That last observation concerns calibration, not proof of a wrong live gate grade. The document-retirement and overdue-battery records also expose their methods and remaining limits. These are substantive deliverables, not merely activity counts.

## Findings

### High — summary-only reader exercise is promoted into defects in canonical definitions

Evidence: `AGENTS/DAEDALUS/runs/2026-09-17_GATE_BASIS_SWEEP_01_STRANGER_B.md:4` explicitly prohibits opening GATES, owner directories, STATUS and definition_surface, treating pointers as unavailable. The main sweep at `460422749`, sections 0/2/3, nevertheless concludes that full letters lack populations, integers or datasets; corresponding owner packets repeat those claims.

Three concrete counterexamples:

- **CORAL:** the packet `AGENTS/CORAL/inbox/2026-09-17_from-DAEDALUS_gate-basis-sweep-1-MSI-01-breadth-and-sustain-carry-no-integer.md` says neither breadth nor sustain carries a number, while acknowledging STATUS is canonical. `AGENTS/CORAL/STATUS.md:92–110` explicitly defines the registered stand-down: breadth <5-of-5, MSI >6.0, two consecutive readings at least ten days apart. The reader instead tries to grade a firing condition from a summary. The absence of a re-fire rule is real, explicitly acknowledged by CORAL and already assigned to Will; it is not evidence that the existing stand-down lacks integers. Cohort enumeration and governing clock may still merit clarification. The packet's proposed new consecutive-update rule is not a faithful restatement of the current elapsed-day rule.
- **BRENT:** its packet says Leg B names no dataset and two obedient graders can choose futures-only or futures-plus-options. The complete canonical `AGENTS/BRENT/workbook/REGISTRY.tsv:131` names the raw `f_disagg.txt` source, market name, MM gross shorts/OI formula and build pointer. The linked August 12 build explicitly identifies disaggregated futures-only. A reader denied that material has not established ambiguity in the full definition. Stale machine fields in the row remain a legitimate concern, but the same row contains a September 6 supersession defining the corrected base and decisive deadband; do not report the old leading prose as the complete operative specification.
- **BROCK:** `AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv:1–14`, the referenced definition, gives counted runs, prospective grading dates, qualifying measurements and ASIF's explicit exclusion pending Will. The stranger's inability to see a population was imposed by the exercise. This does not prove that the population is perfectly frozen or all future edge cases are resolved; it invalidates the stronger missing-population conclusion without reading that definition.

**Consequence:** owners receive avoidable repair asks, and an artificial information restriction becomes evidence for adding mandatory wording. Multiple independent readers do not cure a shared defective brief.

**Suggested disposition:** retain this as a summary-usability test. Re-run only the affected cases with each registered canonical definition and its explicit source references available, still withholding owner explanations and current verdicts. Correct the report and dispatched packets before promoting their conclusions. Keep independently supported findings such as BRENT's stale machine fields and CORAL's acknowledged re-fire gap.

### Medium — falsification sweep headline does not reconcile with its own cohort evidence

`AGENTS/DAEDALUS/runs/2026-09-17_FALSIFICATION_SWEEP_03.md:6` at `84cc5a47a` reports approximately 285 OPEN rows and 86 negative-class rows. Section 4 lists OPEN counts 110/42/39/21/20/22 and negative counts 14/21/7/10/12/6. Independent arithmetic yields **254 and 70**, matching its table footer. Missing-precondition counts sum to **22, plus one separate dated-window case**. SHADE is explicitly NOT-SEEN and cannot supply an invented residual denominator.

**Consequence:** the operator receives conflicting scale/prevalence claims. This is not explained by rounding. Reconcile to reader evidence and regenerate dependent summaries. The four scanner flags support a finding about this sample; they do not establish that the scanner now detects only header defects generally.

### Medium — proposed pilot pass changes the acceptance criterion

`AGENTS/DAEDALUS/runs/2026-09-17_P4_SITTING_RULING_PACKAGE.md:144–152` records only two of three pilots at an evidence-backed terminal state, yet recommends PASS-on-shape and closure. The cited original `PROME/codex/findings/2026-09-05_correction-closure-architecture-report.md:252` requires **all three**. The package transparently labels the third as NO and asks Will to decide: this is a proposed relaxation, not a secretly enacted pass.

**Consequence:** architectural usefulness and demonstrated completion become interchangeable. Prefer “promising design; original completion criterion not yet met.” Complete the ES-02 scope receipt and verify the evidence, or ask Will to explicitly amend/waive the criterion. A missing validation_ref alone is not proof that the underlying repair failed; the record should distinguish evidence existing from evidence durably linked.

## Verification and limits

Read owner instructions, recent commit history, the overdue battery, gate and falsification sweep reports, relevant stranger/vintage evidence, P4 decision sections, original pilot criterion, dispatched gate packets and sampled canonical owner definitions. Independently recomputed the cohort sums and traced the challenged absence claims to owner sources. No external market data was re-fetched; contemporary prices, percentages and actual trading implications are not certified. This is independent review of DAEDALUS work, not independent verification of CATO's own review report.

No code or policy repaired. DAEDALUS was still producing additional work, so incomplete live writebacks are not closeout failures. Re-check current revisions before acting on these findings. Remaining action belongs to Will/DAEDALUS; no repair task or communication was authorized. Next CATO session: orient and await Will, using this report for a bounded follow-up if requested.
