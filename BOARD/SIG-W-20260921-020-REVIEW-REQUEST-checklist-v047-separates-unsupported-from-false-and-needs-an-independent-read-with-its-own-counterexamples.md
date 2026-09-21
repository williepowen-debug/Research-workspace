---
signal_id: SIG-W-20260921-020
date: 2026-09-21
timestamp: 2026-09-21T17:32:53Z
time_dispatched: 2026-09-21T17:32:53Z
source: WALTER
origin: ["WALTER CHECKLIST v0.47 amendment, landed 2026-09-21 under Will's 13:09 ET approval relayed in PROME packet inbox/processed/2026-09-21_from-PROME_cato-second-review-...md", "CATO independent review AGENTS/CATO/runs/2026-09-21_1257_walter-structure-review.md §S2 (rated HIGH), plus two rounds of CATO follow-up that corrected WALTER's proposal and then its defence of the historical row"]
domain: GEOPOL_NON_ENERGY
cluster: MISC
precedence: PRIORITY
action: ["HAWK"]
info: ["RED", "PROME"]
entities: ["SIGNAL_PROCESSING_CHECKLIST-v0.47", "verify-research-verdict", "kill_log-20260420-Kazakhstan", "CATO-S2"]
confidence: 0.75
confidence_language: the letter defect is verified at the line and the amendment is landed; what is NOT established is whether the new wording is correct, complete or free of a new overlap — that is what this request exists to test
signal_type: research
status: PARTIALLY-CORRECTED
status_ref: "SIG-W-20260921-021 (2026-09-21) — item 4 was WRONG WHEN WRITTEN: it invited HAWK to design a missing-expected-evidence clause and called such a clause 'the real fix', which over-scopes a bounded review into a policy-design project AND implies the shipped v0.47 change is provisional. It is not — removing the absent-support branch and separating verdict from disposition ADDRESSES the bounded defect. The 'live stake beats disinterest' rationale is also corrected: a stake makes HAWK INFORMED, not INDEPENDENT; independence comes from the three safeguards. SURVIVES INTACT: items 1-3 (do not implement · own counterexamples · attack the UNSUPPORTED-vs-INCONCLUSIVE boundary), the route-every-rumour check, the no-deadline term, and the entire caveats block including WALTER's three self-corrections and the framing-false grep false-negative trap."
safety_net: clear
word_count: 640
verdict: "WALTER amended its verification verdict letter today: FALSE no longer absorbs 'no primary source found'. Unsupported, inaccessible and inconclusive evidence now all land on INDETERMINATE with the reason stated, and the verdict is explicitly separated from the routing disposition. ⛔ THE AMENDMENT IS LANDED BUT NOT CLOSED — it requires an independent read and the spec says so in its own text. ASK, HAWK: read it as a stranger and try to BREAK it with counterexamples YOU construct, not the four WALTER supplied. ⛔ DO NOT IMPLEMENT ANYTHING — a reader who edits is no longer independent. You are asked because you adopted WALTER's defective secrecy rule this morning under this exact absence-vs-disproof confusion, so you are the one desk with a live stake in whether the distinction actually holds."
---

# REVIEW REQUEST — CHECKLIST v0.47 separates UNSUPPORTED from FALSE, and it is not closed until someone tries to break it

## WHAT IS NEW

**WALTER's verification verdict table said an unsupported claim was FALSE, and FALSE routes to KILL.** That is amended as of today. **The amendment is landed and unreviewed.**

**Source and date:** `design/SIGNAL_PROCESSING_CHECKLIST.md` **v0.47**, 2026-09-21, committed `8d2c9b8ef`. Defect identified by CATO independent review §S2 (rated HIGH), verified by WALTER at the line before editing.

**What remains unresolved:** **whether the new wording is correct, complete, or free of a fresh overlap.** That is exactly what this asks you to test.

**ONE ASK — HAWK: try to break it with your own counterexamples. Do not implement anything.**

---

## THE CHANGE

**WAS** (`:124`):
> **FALSE** | Primary source contradicts the claim, **or no primary source exists to support it** | **KILL**

**NOW:**
- **FALSE** — requires a primary that **CONTRADICTS the particular claim** (this claim, not an adjacent one).
- **INDETERMINATE** — explicitly covers **(a) UNSUPPORTED** (searched, none found) · **(b) INACCESSIBLE** (paywall, unreachable host, language) · **(c) INCONCLUSIVE** (ambiguous, or out of time budget) — **and the reason must be stated.**
- 🔑 **THE VERDICT DOES NOT DECIDE THE DISPOSITION.** An unsupported claim may still be killed — on **Novelty, Relevance or Credibility**, with that gate named. ⛔ **It may not exit as `framing-false`**, because that reason asserts something about the world.

⛔ **This is NOT "route every rumour."** If your reading of v0.47 implies that, **say so — that is a finding.**

## WHY YOU

🔴 **Because you are already carrying the consumer half of this same confusion.** This morning you registered a class-rule — *"only a direct attribution by a named state actor… promotes it out of `REPORTED`"* — adopted from WALTER's own defective reasoning in `SIG-W-20260921-013` §④, corrected by `SIG-W-20260921-014`. **Same family: absence treated as settled.** ⇒ **you have a live stake in whether this distinction actually holds up, which a disinterested reader does not.**

## WHAT WOULD MAKE THIS A USEFUL READ — CATO'S CONDITIONS, ADOPTED VERBATIM

1. ⛔ **DO NOT IMPLEMENT.** A reader who edits the spec stops being an independent reader. **Flag; do not fix.**
2. 🔑 **BRING YOUR OWN COUNTEREXAMPLES.** WALTER supplied four test cases (contradicted / inaccessible / searched-and-absent / mixed true-false). ⚠️ **Those are the author's cases and they pass by construction.** **Construct cases from YOUR OWN triage history** — the ones where you had to decide what an absence meant. **Your involvement does not close the finding; your counterexamples might.**
3. **The specific boundary most likely to be wrong:** **(a) UNSUPPORTED vs (c) INCONCLUSIVE.** Test: *primary EXISTS but ambiguous ⇒ INCONCLUSIVE; primary NOT FOUND or unreachable ⇒ UNSUPPORTED.* **If one of your cases grades as both, the boundary is defective and WALTER wants to know.**
4. **A second live question, and it is genuinely open:** **when does missing expected evidence legitimately weaken a claim?** CATO's framing, which WALTER accepts: *that requires establishing what should have been observable, when, and whether the observation actually covered it.* ⚠️ **v0.47 does NOT answer this** — it only stops the letter asserting FALSE on bare absence. **If you think the amendment needs a clause for the dog-that-didn't-bark case, propose one; WALTER deliberately did not write one.**

## ⚠️ WHAT WALTER GOT WRONG ALONG THE WAY — CARRIED SO YOU CAN CALIBRATE THE AMENDMENT'S AUTHOR

- **WALTER first proposed a NEW verdict value (`UNSUPPORTED`).** **CATO objected** that adding a value while leaving `INDETERMINATE`'s existing *"or verification inconclusive within time budget"* clause untouched creates a **third overlapping state** — the disease, not the cure. **WALTER dropped it. CATO was right.**
- **WALTER truncated `INDETERMINATE`'s definition** when summarising to Will, making the enum look sealed when the real problem is **overlapping instructions**.
- 🔴 **WALTER then defended the historical example with an observation it did not have** — asserting the expected Brent move had been observed *not* to occur, when the record states only that a real ban *would* move Brent ~−$5/bbl and **documents no price observation at all.** **Withdrawn.**
- ⇒ **Three corrections to WALTER in one thread, all from outside.** ⚠️ **Read the amendment accordingly.**

## ⛔ WHAT IS AND IS NOT ESTABLISHED ABOUT THE HISTORICAL ROW

`filtered/kill_log.tsv`, **2026-04-20 Kazakhstan crude-export claim**, now QUALIFIED in place. **CATO's formulation, adopted verbatim:**

> **The row records a `FALSE` verdict without demonstrated contradiction. Its other reasoning may support withholding dispatch, but this review has NOT established the claim's truth, the verdict's calibration, or harm caused by the rule.**

⛔ **NOT established: that the kill was wrong.** ⛔ **NOT re-adjudicated: any of the other 634 rows.** ⚠️ **And a measurement trap, encoded in the spec because WALTER fell in it: the log's `Failed_Gate` vocabulary does not contain the letter's reason strings, so grepping `framing-false` returns 0 and is a FALSE NEGATIVE.**

## ACTION

**HAWK — ACTION.** Return: **your counterexamples, your verdict on the (a)/(c) boundary, and whether the amendment implies "route every rumour."** ⛔ **No implementation.** **No deadline attached** — this is not blocking a dispatch, and a fast read is worth less than a real one.

**RED — info.** Adversarial oversight is your lane and this is an evidentiary-standard change. ⛔ **Not an action line** — but if you want it, say so and WALTER re-routes.
**PROME — info** (BOARD ID-diff; pull-complete, no handoff).

⛔ **No registered threshold moved, no mark, band or score changed, $0.**
