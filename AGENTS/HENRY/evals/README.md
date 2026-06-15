# HENRY EVAL SUITE — v1

**Purpose:** Catch judgment regressions in HENRY caused by prompt edits, CLAUDE.md/boot-protocol changes, thesis-doc rewrites, or auto-memory drift. Each case is a frozen scenario with PASS/FAIL criteria. Re-run before promoting non-trivial changes to the prompt surface.

**Not the same as** `workbook/PREDICTIONS.tsv` (which tracks HENRY's forward calls vs reality). Evals test whether HENRY's *reasoning surface* still produces correct judgment when given known inputs.

**Built:** 2026-06-15, modeled on `AGENTS/SAM/evals/` (the fleet's only prior suite — faithful copy of its two-file split, skip-boot, fresh-session, PASS/FAIL+contamination, results.tsv). Refinements below per ORC review.

---

## ⚠️ READ FIRST — what a skip-boot eval CAN and CANNOT test

The deferred CLAUDE.md change is largely boot/closeout **steps** ("read peer NEXUS_BRIEFs at boot," "write own at closeout"). **Evals run skip-boot — those steps do NOT execute during the eval.** CLAUDE.md loads as *text*, but the agent won't *perform* a boot step it's told to skip.

**Consequence:**
- An eval can test a judgment **PRINCIPLE** — but only if that principle is in the **always-loaded surface** (CLAUDE.md body + auto-memory), NOT merely expressed as a boot step.
- For the boot-step change, the eval is a **REGRESSION GUARD** (did adding the steps degrade reasoning?), **NOT proof-of-fix.**
- **Proof-of-fix is a separate, cheaper BOOT SMOKE-TEST:** after the CLAUDE.md change lands, boot HENRY for real and confirm he surfaces a fresh peer fact (e.g. "VIOLET current to 6/12" from her NEXUS_BRIEF) without being told. That validates the boot-read *delivers data*; the eval validates the *judgment* didn't regress. Don't conflate them.

Each case below notes **which loaded surface carries its principle** — a FAIL where the principle isn't loaded is "lesson-absent" (fix the surface), not a reasoning regression.

---

## Case roles — the promotion bar is NOT flat "no regression"

| Role | Baseline expectation | Success after a change |
|---|---|---|
| **TARGET** | May FAIL at baseline (the change is meant to fix it) | FAIL→PASS, or "applies the now-loaded lesson" |
| **GUARDRAIL** | PASS at baseline | Stays PASS (no regression) |

**Promotion rule:** promote a change when **the TARGET improves AND every GUARDRAIL holds** — not a uniform "no regression." Do NOT be alarmed if a TARGET fails at baseline; that's the point of it.

## Current cases (v1)

| ID | INPUT (pasteable) | RUBRIC (scorer only) | Role | Principle source (loaded?) | Tests |
|---|---|---|---|---|---|
| 01 | `case_01_sibling_staleness_INPUT.md` | `case_01_sibling_staleness_RUBRIC.md` | **TARGET** | auto-memory `feedback_verify_counts_before_propagating` + `finding_anchor_prediction_to_surprise_not_priced`-adjacent staleness note (✓ loaded) | Sibling-staleness trap: a peer that looks stale per HENRY's *own prior note* is actually fresh — re-check the peer's header, don't propagate the stale claim |
| 02 | `case_02_catalyst_pricing_INPUT.md` | `case_02_catalyst_pricing_RUBRIC.md` | **GUARDRAIL** | auto-memory `finding_anchor_prediction_to_surprise_not_priced` + `finding_catalyst_vs_consequence_conflation` (✓ loaded) | Catalyst-vs-pricing: an already-priced outcome delivering moves nothing — anchor the prediction to surprise-vs-pricing; labels can invert |
| 03 | `case_03_kre_rate_vs_credit_INPUT.md` | `case_03_kre_rate_vs_credit_RUBRIC.md` | **GUARDRAIL** | CLAUDE.md "Structural vs war attribution test" (✓ loaded) | Rate-vs-credit discriminator: KRE down DESPITE falling yields = credit trade (gaps), not margin (grinds) — identify the driver before forecasting |

Cases are orthogonal — staleness-propagation / pricing-anchoring / mechanism-discrimination are different failure modes; passing one ≠ passing all.

**Cap discipline (per SAM):** durable suite = the **2 GUARDRAILS** (02, 03). Case 01 is a **change-specific TARGET** tied to the pending boot-read/staleness-overlay CLAUDE.md change — it may retire or convert to a guardrail once that principle is fully codified. Don't grow past 3 without a real fire.

---

## Runner protocol

Two file types per case:
- **`*_INPUT.md`** — pasteable prompt block (between triple backticks) + operator instructions. Pure scenario + questions, no rubric. **This is what you paste.**
- **`*_RUBRIC.md`** — EXPECTED checkboxes + DO-NOT anti-patterns + scorer notes. **You read it while scoring; it must NEVER enter the runner's context.**

### Steps
1. **Fresh Claude Code session** in `/home/willi/Research-workspace/AGENTS/HENRY/`. New terminal, new conversation — no shared context with any running HENRY.
2. Open the case INPUT, copy **only** the content inside the triple-backtick block (starts `DO NOT RUN BOOT`, ends `Be direct.`).
3. **Contamination self-check before pasting:** selection must NOT contain `EXPECTED`, `DO NOT`, `RUBRIC`, or checkboxes (`- [ ]`). If it does, you grabbed too much — re-select.
4. **Paste as the first prompt.** Add no framing of your own.
5. When the runner responds, open the matching RUBRIC in a separate window. Score against EXPECTED + DO-NOT.
6. **Contamination check:** scan the response for verbatim phrase echo from the rubric.
7. Append a row to `results.tsv`: date · case · session_id (`YYYY-MM-DD-HHMM`) · result · auto_memory_loaded (which lessons appeared in context) · notes.
8. **Close the eval session** — its context is contaminated with the eval inputs; don't reuse it for real work.

### Why skip-boot
Full boot loads STATUS/MEMORY/LESSONS — those contain the **answer keys** (e.g. HEN-33's re-anchoring, the VIOLET-6/12 correction). Loading them tests reading comprehension, not judgment. CLAUDE.md + auto-memory auto-load regardless — that's correct: they hold the **lesson references**, and the test is whether HENRY **applies** an available lesson.

### Why fresh session, not sub-agent
Sub-agents boot differently and don't trigger the same CLAUDE.md / auto-memory load path. The surface we care about is the actual HENRY-session surface = fresh Claude Code session.

---

## Scoring (PASS/FAIL only)

- **PASS:** every EXPECTED met AND no DO-NOT appears AND no contamination signature.
- **FAIL:** any EXPECTED missing/ambiguous OR any DO-NOT appears.
- **PASS-CAVEATED:** all EXPECTED met, no DO-NOT, BUT contamination observed — not diagnostic until the case boundary is fixed and re-run.
- **FAIL-CONTAMINATED:** failed AND contamination present.

Borderline criterion → score NOT MET → FAIL. Cases are tuned to be unambiguous when HENRY reasons correctly.

## Failure protocol (diagnose before reacting)

Four buckets: **lesson-absent** (the principle isn't loaded — fix the surface / promote to auto-memory) · **lesson-present-not-applied** (had it, still wrong — strengthen/escalate the lesson) · **case-bug** (INPUT/RUBRIC ambiguous — re-spec) · **contamination** (rubric leaked — fix boundary, re-run). Don't blindly revert the triggering change; the diagnosis dictates the fix.

## Re-run cadence

Re-run **all cases** before promoting: a non-trivial CLAUDE.md edit · a boot/closeout protocol change · a MEMORY/auto-memory restructure · ≥10 new auto-memory entries since last baseline. Do NOT re-run for routine STATUS/data updates or a single new prediction.

---

## ⏱️ OPERATOR COST — the real gate (read before scheduling)

The build is cheap; **the baseline-run is the cost, and it can't be delegated** — it needs a fresh HENRY session with no shared context, scored by Will (~10 min/case). 3 cases + a post-change re-run ≈ 30–60 min of operator time. **Until Will runs the baseline, the suite is shelf-ware and the CLAUDE.md boot-wiring change stays blocked** — which is fine (it's deferred). Just go in knowing: the gate is operator availability, not engineering.

**Minimum viable baseline:** if time is tight, run **Case 01 (TARGET) + one GUARDRAIL**; the third can follow.

*Suite format follows SAM's eval pattern. v1 holds at 3 cases (2 guardrails + 1 change-specific target).*
