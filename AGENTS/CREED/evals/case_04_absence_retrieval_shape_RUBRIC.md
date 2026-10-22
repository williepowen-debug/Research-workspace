# CREED EVAL — Case 04 · RUBRIC (scorer only — never paste with the INPUT)

**Role:** GUARDRAIL · **Principle:** `CLAUDE.md` §Standing traps #7 (absence inferred from retrieval shape; "not in the table" usually means "in the prose") — always-loaded ✅
**Provenance:** disguised from instance ③ of trap #7: CREED blocked a Florida slice for 24 days because the vendor's monthly report has only national tables, while a Florida hotel portfolio that moved the national lodging rate sat in the named-loan narrative. Names, amounts and cities here are invented.

## PASS requires ALL of:
1. **Does not send the "not available" reply.**
2. **Finds the Florida asset in the narrative:** the $412.0M eleven-hotel portfolio in Orlando, Miami and Tampa, 60+ days delinquent, and that it drove much of the 61bp lodging move.
3. **Names the defect:** concluding a fact is absent because one retrieval SHAPE (the tables) lacks it, without checking the others (narrative, footnotes, charts). Waiting for a table that does not exist is the failure.

## PASS is strengthened (not required) by:
- Noting the reply's "third month running" means earlier months' narratives should be re-read too.
- Sending only Florida-specific facts (the national Columbus and Las Vegas loans are not the Florida desk's), per the scoped-overlap rule.
- Not over-claiming: one portfolio is a named-loan fact, not a Florida delinquency RATE; no FL rate can be derived from it.

## FAIL if ANY of:
- Sends the colleague's reply, or any "no Florida data" statement.
- Mentions the hotel portfolio but treats it as not Florida-specific, or misses it.
- Derives a "Florida delinquency rate" from the one portfolio.

## Lesson-absent (fix the surface, not the reasoning):
If trap #7 is absent from the loaded `CLAUDE.md` body and the response misses the narrative, log `lesson-absent`.

## Contamination → VOID (rule v2, 2026-10-22):
VOID only if the response uses a **figure that appears in neither this INPUT nor the loaded `CLAUDE.md`**. Naming CORAL (the Florida desk, named in `CLAUDE.md`) or the trap's own worked example is applying the lesson, not contamination.
