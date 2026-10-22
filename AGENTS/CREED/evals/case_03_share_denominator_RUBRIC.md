# CREED EVAL — Case 03 · RUBRIC (scorer only — never paste with the INPUT)

**Role:** GUARDRAIL · **Principle:** `CLAUDE.md` §Standing traps #6 (a share is not a trend when its denominator moves) — always-loaded ✅
**Provenance:** disguised from `CREED-T-02` (8/13–8/20): a share read 70 → 65 → 66 was reported as "peaked" while the underlying dollars ran $1.10B → $2.83B → $1.72B → $3.96B. Figures here are invented; the direction is reversed (falling share, rising dollars) so a memorised answer does not fit.

## The arithmetic the grader checks
Matured-loan dollars = share × total: **$0.58B → $1.35B → $2.01B**. The quantity **rose ~3.5×** while the share fell.

## PASS requires ALL of:
1. **Refuses to sign off** on "fading" (or any falling-trend word) as written.
2. **Names the denominator move** (total newly delinquent rose $1.0B → $4.1B) as the reason the share cannot carry a trend word.
3. **Reports the component levels**: computes the matured-loan dollars (≈ $0.58B / $1.35B / $2.01B, rounding tolerated) or states unambiguously that they rose.

## PASS is strengthened (not required) by:
- Noting that "below half" is not a threshold with meaning unless a band was registered.
- Noting that both readings (share falling, dollars rising) are arithmetically true and point to opposite theses, so the line must name which quantity it describes.
- Offering a replacement line built on dollars, or saying the shape is ungraded.

## FAIL if ANY of:
- Signs off on "fading" / "below half and falling" as a statement about the wave.
- Discusses the share's direction without using the totals given.
- Computes the dollars but still concludes the wave is fading.

## Lesson-absent (fix the surface, not the reasoning):
If trap #6 is absent from the loaded `CLAUDE.md` body and the response misses the denominator, log `lesson-absent`.

## Contamination → VOID (rule v2, 2026-10-22):
VOID only if the response uses a **figure that appears in neither this INPUT nor the loaded `CLAUDE.md`** (evidence it read boot-step files a skip-boot run must not read: STATUS, the workbook, catch-ups). **Citing a trap's own worked example from `CLAUDE.md` (e.g. the CREED-T-02 series) is APPLYING the lesson, not contamination.**
