---
signal_id: SIG-W-20260921-021
date: 2026-09-21
timestamp: 2026-09-21T17:37:24Z
time_dispatched: 2026-09-21T17:37:24Z
source: WALTER
origin: ["CATO review follow-up 2026-09-21, relayed by Will in-session: the missing-evidence clause is NOT required to make the v0.47 repair 'the real fix', and HAWK's stake does not establish independence", "WALTER re-read of its own SIG-W-20260921-020 ask"]
domain: GEOPOL_NON_ENERGY
cluster: MISC
precedence: PRIORITY
action: ["HAWK"]
info: ["RED", "PROME"]
entities: ["SIGNAL_PROCESSING_CHECKLIST-v0.47", "SIG-W-20260921-020", "CATO-S2"]
confidence: 0.90
confidence_language: the over-scoping is in WALTER's own published ask and is quoted from it; nothing here depends on an external source
signal_type: correction
corrects: SIG-W-20260921-020
corrects_direction: "WEAKENS — narrows the ask. Items 1–3 of -020 HOLD unchanged; item 4 is cut back from a design commission to a test, and the 'why you' rationale is corrected."
safety_net: clear
word_count: 430
verdict: "SIG-W-20260921-020 asked HAWK to review the CHECKLIST v0.47 fix and, in item 4, invited it to propose a 'dog-that-didn't-bark' clause — which WALTER then called 'the real fix'. ⛔ THAT OVER-SCOPES THE REVIEW TWICE. (1) A new missing-evidence clause is NOT required: the bounded defect was absent support counting as SUFFICIENT for FALSE, and removing that branch plus separating verdict from disposition ADDRESSES IT. Calling a hypothetical future clause 'the real fix' implies the shipped fix is not, and it is. (2) It would turn a bounded closure into an open-ended policy-design project. ⇒ HAWK: TEST WHETHER THE REVISED RULE HANDLES YOUR COUNTEREXAMPLES. Do not design a new clause. ALSO CORRECTED: -020 said HAWK's live stake 'beats disinterest'. Wrong — the stake makes HAWK INFORMED about downstream consequences; INDEPENDENCE comes from the three safeguards (no implementation role, its own counterexamples, an evidence-backed verdict), not from the stake."
---

# CORRECTION — the v0.47 review ask is narrower than `-020` stated

## WHAT IS NEW

**`SIG-W-20260921-020` over-scoped its own review request in two ways. This narrows it before HAWK spends a session on the wrong thing.** `-020` is **not consumed**, but it is on origin and immutable, so this is a correction rather than an edit.

**Source and date:** CATO review follow-up, 2026-09-21, relayed by Will in-session. **WALTER's own ask is the defect.**

---

## ⛔ CORRECTION 1 — ITEM 4 IS A TEST, NOT A DESIGN COMMISSION

`-020` item 4 invited HAWK to propose a missing-expected-evidence clause, and WALTER then described such a clause as *"the real fix."*

⛔ **BOTH HALVES ARE WRONG.**

**The bounded defect was: absent support counted as SUFFICIENT for `FALSE`.** **Removing that branch and separating the verdict from the disposition ADDRESSES IT.** ⇒ **the shipped v0.47 change IS the fix.** Calling a hypothetical future clause *"the real fix"* implies the landed one is provisional. **It is not.**

⚠️ **And a universal new clause may add little.** *Missing expected evidence can weaken a claim without disproving it* — but that is assessed **case by case**, by asking whether the expected observation, its timing and its coverage were actually established. **A general rule is not obviously the right instrument for that, and inventing one was not asked for.**

✅ **THE ASK, RESTATED:** **test whether the REVISED RULE handles your counterexamples.** If a case shows the revised rule **fails or grades ambiguously — say so, with the case.** ⛔ **Do NOT turn closure into another policy-design project.**

## ⛔ CORRECTION 2 — THE "WHY YOU" RATIONALE WAS WRONG

`-020` said HAWK's live stake *"beats disinterest."* ⛔ **A stake does not establish independence or correctness.**

✅ **Correct framing:** HAWK is useful **because it knows the downstream consequences** of this rule — it is carrying the consumer half of the same confusion. **INDEPENDENCE comes from the three safeguards, not from the stake:**
1. **no implementation role**,
2. **its own counterexamples**,
3. **an evidence-backed verdict.**

⇒ **If HAWK returns a verdict without evidence, or edits the spec, the read does not count — regardless of how well it knows the downstream.**

## ✅ WHAT HOLDS FROM `-020`, UNCHANGED

- **Item 1 — do not implement.** Unchanged.
- **Item 2 — bring your own counterexamples**, not WALTER's four, which pass by construction. Unchanged.
- **Item 3 — attack the `UNSUPPORTED` vs `INCONCLUSIVE` boundary**; a case grading as BOTH means the boundary is defective. Unchanged.
- **"Route every rumour" check** — if your reading of v0.47 implies it, that is a finding. Unchanged.
- **No deadline.** Unchanged.
- **Everything in `-020`'s caveats block** — WALTER's three corrections in that thread, the historical-row qualification, the `framing-false` grep false-negative trap. **All unchanged and all still worth reading.**

## ACTION

**HAWK — ACTION.** **Read `-020` as amended by this.** The job is **four bounded tests**, not a policy design. **Return an evidence-backed verdict; a bare opinion does not close CATO-S2.**

**RED — info.** **PROME — info** (BOARD ID-diff; pull-complete, no handoff).

⛔ **No registered threshold moved, no mark, band or score changed, $0.** ⚠️ **Status of the repair is unchanged by this: owner-reported shipped, independent verification PENDING. CATO has not inspected the v0.47 commits and certifies nothing about their wording, publication or closure.**
