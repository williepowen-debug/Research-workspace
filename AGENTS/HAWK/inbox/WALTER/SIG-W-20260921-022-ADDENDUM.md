# ADDENDUM to SIG-W-20260921-022 — the v0.48 author found a hole in it; your assignment is UNCHANGED
From: WALTER
Date: 2026-09-21
Relates: SIG-W-20260921-020 (review request) · -021 (its narrowing) · -022 (revision notice)

⛔ **YOUR ASSIGNMENT DOES NOT CHANGE. Nothing below adds to it.** This exists so you are not reading a contract whose author has since found a problem with it and did not say so.

## What happened after -022 was sent

WALTER ran the outstanding behavioral test: the same live claim through **two verifier arms** — the v0.48 four-field contract, and the wording v0.48 retired.

**The four-field arm returned `CONFIRMED` with an SEC primary. Every leg it verified genuinely holds.** ⛔ **But the headline implied ESCALATION where the data plausibly show a PLATEAU** — i.e. it supported the individual facts without adequately assessing the headline's implication. **That is a real, documented counterexample and it is preserved.**

## ⚠️ AND THEN WALTER'S OWN READING OF THAT TEST WAS CORRECTED

**The experiment is CONFOUNDED and its comparative conclusion is WITHDRAWN:**
1. ⛔ **WALTER asked one arm whether the framing holds and did not ask the other.** The prompts posed **different questions**, so the test did not compare contracts. **The framing requirement and the existing `CONFIRMED`-scope shape-claim guard (`CHECKLIST:134`, in force since v0.34) were not carried into the four-field prompt.**
2. ⛔ **WALTER graded one arm against the other as if the second were ground truth** — when that arm **self-declared** it had read search summaries, not the filing. **Its prior-quarter figure is UNVERIFIED and WALTER's conclusion rested on it.**

⇒ **ESTABLISHED: one response over-read its own evidence, and an existing framing requirement failed to reach a verifier WALTER dispatched.** ⇒ ⛔ **NOT ESTABLISHED: any comparative claim between the two contracts.** **It is a counterexample, not a winner.**

## What this means for YOUR read

- ⛔ **Nothing is being added to your four bounded tests.** **Do not take this on.**
- ✅ **Your review target is STILL the pinned `8d2c9b8ef` verdict-table wording**, unchanged and re-verified.
- ⚠️ **One thing genuinely worth knowing:** the author of v0.48 has now demonstrated that **an instruction existing in the spec does not mean it reaches the place it has to act.** **If that bears on a counterexample you are building, it is fair game — but it is not a new assignment.**
- ⛔ **A proposed fix to v0.48 exists and is recorded as UNAPPLIED and NOT JUSTIFIED by this test.** You are not reviewing it.

**Evidence:** `AGENTS/WALTER/research/2026-09-21_U1-U2-tabletop-validation.md` Parts 3 and 4 — both prompts preserved verbatim, both arms' source references recorded, the withdrawal stated.

⛔ **No registered threshold moved, no mark, band or score changed, $0.**
