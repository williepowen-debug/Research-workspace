# CODEX → PROME: Highest-Value Questions Audit

**Date:** 2026-08-28  
**Requested by:** Will  
**Reviewer:** Codex, cross-vendor read-only review  
**Repository baseline:** local `master` matched `origin/master` at review start  
**Scope:** PROME coordination value, Monday Kernel readiness, briefing traceability, and live-gate executability  
**Authority:** Findings and recommendations only. No operational state, thresholds, gates, policies, or research records were changed.

---

## Executive conclusion

PROME is producing real institutional value through error detection, source reconciliation, explicit retractions, and disciplined fail-closed operation. The strongest evidence is not the amount of activity; it is the number of material mistakes caught before they became rulings, accepted Kernel events, or capital actions.

The cost-effectiveness of that machinery remains unproven. Friday required nine orchestrated desk sessions across three waves, and the repository recorded 944 commits over August 27–28. The system measures activity, defects, and narrative state extensively, but it does not yet normalize research output against operator and coordination burden.

Two concrete control defects require attention:

1. The gate checker does not enforce `review_by`, allowing overdue gate reviews to coexist with a green boot result.
2. `GATE-BRENT-COT-35B` names a nonexistent canonical definition path.

Monday's Kernel sitting is authorization-ready and safely fail-closed, but it is not accurately described as having only one operational dependency. Will's window is the only missing pre-sitting authorization; the sitting still contains a multi-step dependency chain. MIDAS-06 must remain unscored because its four-outcome probability structure cannot be represented faithfully by the Kernel's binary scoring model.

---

# 🔴 CRITICAL

No critical integrity failure was confirmed. The Kernel remains non-authoritative, its existing two shadow events are additions-only, and the current test suite passed 212 tests.

---

# 🟠 HIGH

## H1 — Gate review clocks can expire while the boot gate reports green

**Where**

- `PROME/GATES.tsv`, live row `GATE-TERRY-007`:
  - `review_by`: `2026-08-24 CONFIRMED 8/23 ...`
  - `last_checked`: blank
  - row text still says the 8/21 official observation was owed.
- `PROME/GATES.tsv`, live row `GATE-CORAL-MSI-01`:
  - `review_by`: `2026-08-28 ... awaits CORAL confirm`.
- `PROME/tools/prome_gate.py`, `check_gates_tsv()` validates:
  - state vocabulary;
  - `FIRED-UNEXECUTED`;
  - `consumed_by` dates and empty cells.

It does not parse or enforce `review_by`, and it does not require `last_checked` for live `INSTRUMENT` gates.

**Observed result**

`python3 PROME/tools/prome_gate.py boot` returned:

> `✅ all blocking gates pass`

while `GATE-TERRY-007` carried a passed review date and blank `last_checked`.

HEARTBEAT contains a fresher conclusion—counter `0-of-5`, with official DGS10 through 8/26 above 4.50—but that newer state did not reconcile the canonical gate row.

**Bite**

A live instrument gate can miss its explicit owner-review clock, retain an obsolete owed-print narrative, and still produce blocking green. If the missing print crossed a fire condition, the coordination layer could silently fail its core purpose: surfacing a fired action gate before new work proceeds.

**Resolution shape**

- Parse the leading ISO date in `review_by` for every live row.
- A passed `review_by` must produce at least a high-severity advisory; for live `INSTRUMENT` gates, consider blocking until disposition.
- Require nonblank `last_checked` on every live `INSTRUMENT` row.
- Distinguish `review overdue`, `publication pending`, `owner dark`, and `graded elsewhere but registry unreconciled`.
- Add a discriminating test in which `consumed_by` remains valid but `review_by` has passed; the checker must not report unqualified green.

---

## H2 — MIDAS-06 cannot be scored faithfully in the binary Kernel

**Where**

- `KERNEL/GATE_C_SITTING2_PREP_2026-08-27.md`, MIDAS scoring finding.
- `PROME/inbox/2026-08-27_from-MIDAS_kernel-increment2-authored-paths-hashes-verifier-RED-plus-one-perimeter-conflict.md`.
- Kernel schema constrains `forecast_family` to `BINARY_PROBABILITY`.

MIDAS-06's frozen forecast distribution is:

- `P(YES) = 0.45`
- `P(NO) = 0.20`
- `P(AMBIGUOUS) = 0.35`

**Bite**

A binary scorer normally infers `P(NO) = 1 − P(YES) = 0.55`. That is not MIDAS's forecast. It reallocates the 0.35 ambiguous mass to NO and will generate incorrect Brier or log scores. Ambiguous is not a remote edge case here; it is the likely branch under the current reading.

The event may still be useful for provenance, lifecycle, permission, and resolution-separation testing. It is not valid binary calibration data.

**Resolution shape**

- Mark MIDAS-06 explicitly `UNSCORED—OUTCOME VOCABULARY MISMATCH` before acceptance or at projection time.
- Do not infer the complementary probability.
- Preserve the original multi-outcome distribution in the native companion.
- Treat support for categorical/multi-outcome forecasts as a later schema proposal requiring its own review and ruling.
- Do not patch the live forecast or collapse `(d) AMBIGUOUS` into `NO` after observing the result.

---

## H3 — The coordination system's cost-effectiveness is not yet measurable

**Where**

- `PROME/state/ORCH_LOG.tsv`, 2026-08-28 rows.
- Git history for 2026-08-27 through 2026-08-28.
- PROME closeout commit `a50a2ccb146bb3cc49b29e28c9f483c597861b88`.

**Measured evidence**

- Friday: nine desk spawns, two clerks, one cold reader, three waves.
- Repository: 944 commits over August 27–28.
- Friday closeout: 19 files, 349 insertions, 133 deletions.
- Kernel pilot 1: two accepted events in roughly 32 attended minutes.
- Kernel sitting 2 attempt: zero accepted events and three safe stops.

**Benefits observed**

- False market and source claims retired.
- Several owner files refused incorrect PROME instructions.
- Evidence dependence was reduced from desk count to evidence-type count.
- The Kernel stopped malformed or mismatched commands before writes.
- FLG's read-cap claim was tested, narrowed, and fully retracted.
- Zero capital moved and PROME set no thresholds.

**Bite**

The repository can demonstrate high activity and high error-detection value, but cannot answer whether the same or better research outcomes could be achieved with fewer sessions, commits, surfaces, and operator rulings. Without a normalized scorecard, process expansion can become self-validating: more machinery produces more detected machinery defects, which is then counted as value.

**Resolution shape**

Create a weekly coordination-value scorecard with at least:

| Measure | Definition |
|---|---|
| Completed research loops | Registered question → sourced answer → canonical disposition |
| Forecast resolutions | Properly graded, including no-verdict/annulled outcomes |
| Pre-decision catches | Material defects caught before ruling, acceptance, or capital action |
| Post-decision corrections | Material defects discovered after canon or action |
| Operator burden | Will minutes and ruling count |
| Coordination burden | Sessions, touches, and commits |
| Decision yield | Completed loops per operator hour |
| Correction efficiency | Pre-decision catches ÷ total material defects |
| State-maintenance share | Coordination-only commits ÷ all commits |

Do not set a success threshold after seeing the first score. Run several weeks descriptively before adopting a gate.

---

# 🟡 MEDIUM

## M1 — Monday Kernel readiness is described too simply

**Where**

- `PROME/SCRATCH.md`: “ONE precondition: Will's window.”
- `PROME/DOCKET.tsv`, row 233.
- `KERNEL/GATE_C_SITTING2_PREP_2026-08-27.md`.

**What is true**

Will's bounded time window is the only missing **pre-sitting authorization**. Activation drafts A–E exist, parse, and deliberately fail closed until exact window bounds and source commit are minted. Policy hashes match the prep record. The suite is 212/212 green.

**What is compressed away**

The sitting still depends on this live sequence:

1. The 8/28-dated DFII10 observation publishes Monday.
2. MIDAS grades MIDAS-06 from the published cell.
3. Will rules the prospective no-verdict band.
4. MIDAS moves its first three commands to the authorized submission path.
5. Activations A–D run on the current grants.
6. The resolution grants are promoted between D and E.
7. Activation E runs on the promoted grant hash.
8. MIDAS authors the resolution proposal.
9. RED independently authors `VerifyResolution`.
10. If RED disagrees, verification refuses and the sitting pauses because `DisputeResolution` is outside the approved command set.
11. DAEDALUS performs the closeout review.

**Bite**

Calling this “one precondition” can cause the operator or custodian to treat an in-window dependency failure as an unexpected defect, or to run steps in the wrong order—especially the grants promotion, which must occur after D and before E.

**Resolution shape**

- Retain “one missing pre-sitting authorization” if useful.
- Separately display “six in-window dependencies” and their exact order.
- Put a hard stop beside grants-promotion ordering.
- Pre-name the disposition if RED is unavailable: verification rides a later sitting; no substitute is inferred.
- State before launch that disagreement is a designed pause, not a failed pilot.

---

## M2 — The briefing is traceable, but two interpretations read like facts

**Where**

- `PROME/BRIEF.md`, headline/story.
- `HEARTBEAT.md`, one-liner and rates section.

The major briefing numbers trace to desk-owned or canonical artifacts:

| Claim | Repository support |
|---|---|
| Hike odds 31% → 50% | ORACLE/PROME state |
| Curve flattened roughly 6 bp | LIQUID/HENRY market proxies |
| Gold −3.3%, NVDA −4.6% | Closing-price surfaces |
| HY 263, 2026 low | LIQUID/FRED, dated 8/27 |
| CCC/HY 3.920 record | LIQUID/NEXUS, 787 observations |
| QCEW −79K/−178K private | LABOR primary pull, PROME re-verification; preliminary |
| HEN-42 denied | HENRY record and PROME reproduction |
| WAL $78.55, gate un-fired | REGINALD grade |
| Throughput impairment retired | BRENT adjudication |
| `$160B` wall misattributed | CREED source hunt |

Two compressed statements need qualification:

1. **“The market believed Warsh”** is an inference from several observations, not a directly measured fact.
2. The curve read uses CBOE-market proxies because official FRED H.15 values for 8/27–8/28 were unpublished. HEARTBEAT discloses this; the shorter BRIEF does not.

**Bite**

A later reader may quote the inference as an established causal finding, or treat the proxy curve as the final official series. That contaminates later attribution and gate grading even if the underlying numbers were accurately recorded.

**Resolution shape**

Suggested framing:

> Markets priced a more hawkish path after Warsh; contemporaneous proxies showed front-end-led flattening, while official H.15 confirmation remained pending.

Keep the stronger causal interpretation under `STORY` or `DISAGREEMENT`, explicitly labeled as PROME synthesis.

---

## M3 — One live gate's canonical definition pointer is broken

**Where**

`PROME/GATES.tsv`, `GATE-BRENT-COT-35B`:

> `definition_surface: AGENTS/BRENT/registry/REGISTRY.tsv ...`

That path does not exist. The live file is:

> `AGENTS/BRENT/workbook/REGISTRY.tsv`

The additional setup memo does exist.

**Bite**

A cold grader following the declared single canonical home fails at the first path and may substitute a copied summary, archived letter, or ad hoc reconstruction. This is particularly risky because the latest owner report disclosed a trader-category parsing ambiguity that could change the verdict.

**Resolution shape**

- Owner/PROME verifies the intended canonical registry file.
- Correct the pointer without altering the letter, threshold, or state.
- Add a check that every live `INSTRUMENT` definition path resolves.
- Because definition cells may contain multiple paths and anchors, use an explicit structured primary path rather than whitespace-splitting narrative text.

---

## M4 — Only a minority of live gates are mechanically scannable

**Where**

`PROME/GATES.tsv` currently contains:

- 30 total rows;
- 16 `LIVE` rows;
- 4 live `INSTRUMENT` rows;
- 12 live `JUDGEMENT` rows.

**Bite**

“Live” may be interpreted as continuously monitored. In practice, 75% of live gates require owner judgment, event summons, or periodic review. Several rows have already been re-dated because the owner was dark. A gate can be logically executable yet operationally unobserved.

**Resolution shape**

Expose operating mode separately from gate state:

- `MACHINE_MONITORED`
- `OWNER_GRADED`
- `EVENT_SUMMONED`
- `CANNOT_FIRE_PARTIAL`

For conjunctions with uncovered legs, avoid plain `NOT FIRED`; use `UNKNOWN` or `CANNOT-FIRE(partial)` for the uncovered portion.

---

## M5 — HEARTBEAT's cap compliance has no usable margin

**Where**

Commit `1cfd0a869` reports:

> `32,492 B under the P1 32,550 B read-cap`

That leaves 58 bytes, approximately 0.18% headroom.

**Bite**

One timestamp, short qualification, or formatting change can breach the limit. Calling it “under cap” is mechanically correct but operationally fragile. The 15/15 cold-reader result establishes comprehension of the present file; it does not establish capacity for the next update.

**Resolution shape**

- Treat 95%+ as operationally at-cap.
- Target 85–90% after a rebase.
- Preserve current-state priority; move narrative/history to snapshots before the file reaches the hard boundary.

---

# 🟢 LOW

## L1 — Closeout commits are broad enough to impede selective review

The main Friday closeout mixed market state, narrative, gate/docket changes, archival rotation, memory governance, machine-local notes, orchestration bookkeeping, and a DAEDALUS handoff across 19 files.

The closeout is coherent as an operational unit, but a defect in one component is difficult to review or revert independently.

**Resolution shape**

Consider separate commits for:

1. canonical state transitions;
2. briefing/narrative rewrite;
3. archive rotations;
4. memory-index maintenance;
5. cross-agent design packets.

The separate HEARTBEAT rebase commit is a good precedent.

---

## L2 — Fast correction chains expose transient false canon

The FLG read-cap claim moved from finding → narrowed correction → PROME routing → full retraction within minutes. The final state is good and preserves the erroneous claim under a clear retraction header.

The risk is intermediate readers or consumers acting before the final correction lands.

**Resolution shape**

When a new finding is actively being tested, mark it `DISPUTED/PENDING VERIFICATION` before routing it as a settled defect. Preserve the full correction history once adjudicated.

---

## Cross-document drift summary

| Topic | Surface A | Surface B | Drift |
|---|---|---|---|
| Kernel readiness | `SCRATCH`: one precondition | Sitting prep: multi-step in-window chain | Authorization count is compressed into operational readiness |
| MIDAS-06 | Native forecast has YES/NO/AMBIGUOUS mass | Kernel binary family | Scoring vocabulary cannot represent the forecast |
| Rates reaction | BRIEF states causal interpretation compactly | HEARTBEAT discloses proxies and unpublished officials | Qualification lost in compression |
| GATE-TERRY-007 | HEARTBEAT current through 8/26, counter 0-of-5 | GATES row still carries old owed-print language and blank `last_checked` | Current grade did not propagate to canonical registry row |
| BRENT COT gate | GATES points to `AGENTS/BRENT/registry/REGISTRY.tsv` | Actual registry is `AGENTS/BRENT/workbook/REGISTRY.tsv` | Canonical pointer broken |
| Queue load | Closeout narrative says below cap | Current boot tool reports 29 actionable rows against cap 20 | Narrative and executable count disagree |

---

## Requested action order

1. Repair `review_by` enforcement in the gate checker.
2. Reconcile `GATE-TERRY-007`, including `last_checked` and the newer official-print state.
3. Correct the BRENT COT canonical pointer after owner verification.
4. Mark MIDAS-06 unscored before any calibration output.
5. Present Monday's Kernel sitting as one missing authorization plus an explicit ordered in-window dependency chain.
6. Give HEARTBEAT meaningful byte headroom.
7. Reconcile the actionable WILL_QUEUE count reported by the executable checker with the closeout narrative.
8. Build the weekly coordination-value scorecard before widening orchestration or unattended Kernel authority.
9. Label the Warsh causal interpretation as inference and retain the official/proxy distinction.

---

## Verification performed

- Fetched `origin/master`; local and remote were equal at review start.
- Read current PROME closeout, HEARTBEAT, SCRATCH, HANDOFF, BRIEF, DOCKET, WILL_QUEUE, GATES, orchestration log, and relevant owner artifacts.
- Inspected recent PROME and Kernel commit history.
- Parsed Kernel activation drafts A–E and checked current policy hashes.
- Inventoried staged and submitted Kernel command files.
- Ran:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py'
Ran 212 tests — OK
```

- Ran:

```text
python3 PROME/tools/prome_gate.py boot
All blocking gates passed; advisories included four due-today Will items and 29 actionable rows against the cap of 20.
```

- Confirmed the repository was clean at the end of the audit.

---

## Final assessment

PROME is presently strongest as an epistemic and operational safety layer: it catches false claims, forces owners to preserve contrary evidence, and prevents malformed commands from becoming durable institutional state. That value is demonstrated.

The next maturity step is not more machinery by default. It is proving that the machinery produces enough completed, decision-useful research per unit of Will attention and coordination burden. The gate-review blind spot and MIDAS scoring mismatch should be repaired or explicitly fenced before treating the current system as ready for broader autonomy.

