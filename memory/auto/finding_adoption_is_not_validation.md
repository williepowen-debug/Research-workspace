---
name: finding_adoption_is_not_validation
description: "An inherited rule that is internally consistent, confidently worded and actively consumed reads as validated — those three properties are exactly what stop anyone testing it, and none is evidence it was ever tested. Limit case (ORACLE 8/27): the described thing did not EXIST — a 272-line metric spec with no implementation, consumed for 67 days, its outputs routed to three desks."
symptoms: "the doc describes a metric but nothing computes it; a published score cannot be regenerated; method doc cited in boot but no matching script; formula in a spec with no code; sigma/index/score that was hand-computed; alert that only runs when someone remembers"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c5ddae97-826b-4924-afcd-ba6e3e2ed927
  modified: 2026-08-21T15:54:15.009Z
---

Four things failed in one ZHAO session (2026-08-21). **None was sloppy.** Each was internally consistent, confidently worded, and actively consumed by other desks — and each turned out never to have been tested:

1. **An interpretation rule.** `CLAUDE.md` stated as an identity: *"Belgium rising while China TIC falls **=** custody migration, NOT a reduction. Net neutral."* Applied as deterministic for ~5 months. Tested: **rho = +0.05 over n=41 months**, ~zero on every window; the "mirror" pattern occurs in **56%** of China-selling months — a coin flip.
2. **A mechanism claim.** A Will-approved reframe explained a falling Treasury line as *"Treasury→Agency rotation."* Directly refutable from a table already on disk. Tested: China's Agency holdings **fell** $37.9B over the same twelve months. It sold both.
3. **A canon paragraph.** The retired rule in (1) had itself been shipped as a **correction** of an earlier contradiction — so it read as freshly audited. It was fixed, consistent, and still untested.
4. **A fix commit.** A peer green-lit an action contingent on their fix. The commit was correct and **local-only**; origin still carried the unfixed text. Truthful about their tree, false about the only place the consumer reads.

**The common property is not staleness — it is that being *used* was silently taken as evidence of having been *checked*.** Consumption feels like validation: if HANS and LIQUID have been consuming a rule for months and nothing broke, the rule looks load-bearing and proven. It is only load-bearing. Nothing in "widely consumed" implies "ever tested," and the confidence of the wording actively suppresses the impulse to test — a hedged rule invites a check; an identity (`=`) does not.

**Inverted, the danger is legible:** *the better-written and more-adopted a rule is, the less likely anyone has tested it.*

**How to apply:**
- **When a rule you are about to APPLY would produce a tidy, load-bearing conclusion, test it instead — once.** The tidiness is the tell. In (1) and (2) the rule would have produced a *cleaner* finding than the truth; that is exactly when to stop and measure.
- **Ask of any inherited rule: "what measurement would refute this, and has anyone run it?"** If the answer to the second half is "unknown," it is untested, not validated — regardless of age or adoption.
- **A rule stated as an identity (`X = Y`) is a red flag**, not a sign of rigour. Rewrite to probabilistic language with the base rate attached, and register the level at which it becomes usable again.
- **Adoption count raises the stakes, never the confidence.** Two desks consuming it means the correction must be *routed*, not that the rule is sounder.
- **Don't delete a falsified rule — preserve it verbatim as a dated dead record with a DO-NOT-APPLY stamp.** The wording is the teaching artifact; a paraphrase loses exactly the property (its confident, specified-looking form) that made it go unchecked.
- **For (4)'s variant:** a peer's "you're clear" describes their *local* state. **Verify the fix is where the consumer reads** — the commit is the record, origin is the action. Fix-author side: push before green-lighting, or say "in force after the next train."
- Related: [[finding_base_rate_the_threshold_before_building_it]] (base-rate before *shipping*; this is the *inherited and already in-force* case) · [[finding_a_teaching_surface_ages_like_data]] (the figures-rot version; this is the rule-never-tested version) · [[finding_record_of_an_action_is_not_the_action]] · [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_retired_threshold_has_no_publisher]].

**EXTENSION 2026-08-27 (ORACLE) — the limit case: the thing was not merely untested, it DID NOT EXIST, and was consumed anyway for 67 days.**

`PREDICTION_MARKET_METRICS.md` — 272 lines specifying binary entropy, KL bits with interpretation bands, a discount chain, and a σ-scored entropy-collapse alert with `k=3 watch / k=5 urgent` — **had no implementation anywhere.** No script computed any of it. In that state it was cited by the agent's own `CLAUDE.md`, named as a boot-sequence read for dislocation work, and **its outputs were routed to three other desks.**

**Why the parent finding's three properties are not the whole story here.** Internally consistent, confidently worded and actively consumed all applied — but the decisive fourth property is **the imperative voice**. A method doc written as *"Compute: `H(p) = -p log2 p …`"* reads as a description of what the desk DOES. Nothing in it distinguishes a capability from a proposal, and no closeout step anywhere asks **"does the thing this document describes actually exist?"**

**What it cost, concretely.** Every σ published from the spec was hand-computed and therefore unauditable. When the implementation was finally written and pointed at the desk's own published record: **every dH and entropy level reproduced exactly** — the math and the inputs were right — while **every σ came back inflated**, and a sweep over every rolling window showed **three of five were unreachable at ANY window**. Two threshold classifications had to be withdrawn, one of them an alert that had been reported as *crossing* its watch line and never did. The directional finding survived intact, because it rested on signs and levels rather than on the scores.

**The hedges were already there and did not save it.** The source row disclosed the irregular sampling cadence, stated in terms that *"σ values rank attention, they do not carry frequentist meaning,"* and correctly refused to quote a σ at n=4. All three were right and all three were insufficient: **a caveat constrains how a number is READ; it does not make the number REPRODUCIBLE, and only reproducibility catches a wrong denominator.**

**How to apply:**
- **This one IS mechanically checkable, unlike the parent.** For any method/spec doc that names a computed quantity (σ, z, index, score, ratio, bits, spread), grep for code that computes it. "Doc names a computation, no code exists" is a cheap, high-yield scan — noisy enough to be review-only, like a nomination sweep, never an auto-fixer.
- **Ship the code in the same session as the score, or do not publish the score.** A derived number without a command that regenerates it is unauditable the moment the session ends.
- **Point a new instrument at your OWN prior claims first, before any fresh question.** That is why this was found at all: the implementation's first target was the desk's published record rather than a new market. A new instrument's highest-value first use is the claims you already made with its predecessor.
- **An alert with no code is a remembered ritual, not a check** — see [[finding_mechanize_the_cap_not_the_ritual]]. Related: [[finding_loadbearing_number_must_be_reproducible]], [[finding_guard_correctness_and_wiring_are_independent]] (its sibling: the code exists but is not wired).

---

## Instance 2026-09-14 — **the author confirming the reviewer's finding is not the reviewer validating the author's fix**

**A new form, and it is the one that hides inside good practice.** A repair to a shared tool was reviewed by an independent reader across seven rounds, which produced **twenty-one findings, five blocking**. Every single one was verified by the author at the artifact before being fixed — no finding taken on the reviewer's word, one finding **declined as stated** and the disagreement produced a better fix. That is the discipline working.

**Then the author wrote *"review closed"* against a commit no reviewer had ever seen**, and kept writing *"confirmed by PROME at the artifact"* as though it conferred independence. ⛔ **It does not. Confirming a FINDING establishes that the defect was real. It says nothing whatever about whether the FIX is right** — and the fixes are exactly the code nobody reviewed. An external reader had to point out that the acceptance record *on the same page* said **"NOT ONE FIX FROM ANY ROUND HAS BEEN RE-REVIEWED."**

**The base rate is not hypothetical, and it is the reason this matters.** In the same review, **two of the five blocking defects were introduced by the author's own repairs**, not present in the original — including a cache fix that made a failing ticker vanish (`rc=3` → `rc=0` on the identical command, three seconds apart). **A round found a blocking defect INSIDE a previous round's fix.** So "the findings were all confirmed" and "the result is sound" are not merely different claims; the second is the one the evidence does not reach.

**A second form of the same error, same session, worth its own line:** the author reported a threshold's *behaviour* — "too tight and it will refuse" — **that its own code did not implement.** Staleness only changed a label; the verdict still returned success. The reviewer reproduced it with a fixture; the author reproduced it before changing anything. ⇒ **A status report can describe a gate that does not exist, and no test catches that, because the test suite tests the code and the report describes the intention.**

**How to apply:**
- **Never write "reviewed commit."** Write **"final commit,"** and say plainly whether any reviewer has seen it. If none has, that is the headline of the status, not a footnote.
- **Name the four states and never merge them** (WQ-229): IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED. **Author verification of findings belongs under TESTED at best, never under INDEPENDENTLY VERIFIED.**
- **A hand-run check recorded in prose is not a test.** "TESTED" was claimed twice in this repair while no executable test existed; the fix was a six-case fixture file, not another paragraph.
- **Before reporting a repair's effect, run the case you are about to describe.** The claim "too tight ⇒ it refuses" was checkable in one fixture and was never checked — the author described the design they intended rather than the code they wrote.
- Related: [[finding_a_correction_pass_is_unreviewed_work]] (the base rate above), [[finding_record_of_an_action_is_not_the_action]] (the markdown table recording a control that the code claimed to run), [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]] (the vanishing-ticker fix).
