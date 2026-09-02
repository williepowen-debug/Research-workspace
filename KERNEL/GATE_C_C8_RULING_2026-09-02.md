# Gate C C8 (Sitting 2) — RULED: CONTINUE · F confirmed · three-outcome projection vocabulary

**Date:** 2026-09-02 10:57 ET (14:57Z), Will in PROME's session (`prome-94`).
**Ruling:** Will, on DAEDALUS's C8 review recommendation (`AGENTS/DAEDALUS/reports/2026-09-02_C8_SITTING2_CLOSEOUT_REVIEW.md`, `08564edac`) via PROME's WQ-155 package: **"Approve 155 with your recs."** Verbatim, in-session.
**Scope of the word (WQ-155's three legs, each at PROME's rec):**
1. **C8 verdict = CONTINUE** for Gate C after Sitting 2 (activations `LIVE-2026-0007…0012`; packet `KERNEL/GATE_C_C8_CLOSEOUT_PACKET_2026-09-02.md`).
2. **WQ-149 carrier CONFIRMED = F.** The Propose+Verify pair rode activation F (`LIVE-2026-0012`, `16a47364c`), E stayed as drafted; the 9/1 row text "E ALSO pins" is superseded by this word. Circumstance statement (R1) stands in `PROME/proposals/2026-09-02_sitting2-RULING-RECORD.md`.
3. **Scoring vocabulary = option (a): admit a three-outcome vocabulary (YES / NO / AMBIGUOUS) to the calibration projection**, so a four-branch frozen letter accepted by the Kernel can be scored by the Kernel. Until the renderer change lands, `CALIBRATION.tsv` row 14 (MIDAS-06) stays excluded `OUTCOME_VOCABULARY_MISMATCH` by design — no hand edit of a view.
**Executor:** PROME (custodian/builder — NOT reviewer) for the doc legs today and the (a) build; **reviewer for (a) = DAEDALUS or RED, never PROME** (8/26 seat rule); registered on DOCKET at EOF.
**DAEDALUS review conditions R1–R6:** R1 packet line corrected `0d5a11482` · R3 transcript note `0d5a11482` · R4 READINESS_PLAN row `77acdc5d4` (advanced to RULED by the commit carrying this file) · R5 noted (mints ride alone from here) · R6 pushed (RED's train + PROME) · R2 rides WQ-150.
**Recorded by:** PROME at ruling time (C8 N6).

## The (a) build, as registered
- **Spec first, code second:** the projection (`KERNEL/tools/render.py`, `projection.py`) admits a per-question outcome vocabulary declared at registration; binary questions unchanged; a three-outcome question scores on the declared mass over the realized outcome (MIDAS-06: P(YES)=0.45 realized YES). No re-scoring of any binary row; no edit to accepted events.
- **Tests:** a fixture for the four-branch letter + a negative control proving a binary row's score is byte-identical before/after.
- **Review before any live render:** DAEDALUS or RED, adversarial; `--check-views` reproduction must still PASS at the committed `render_as_of` for all prior sittings (a vocabulary widening must not change historical views).
- **First live consumer:** MIDAS-06 (row 14) scores at the next sitting or at a PROME-run view re-render under a ruled activation — never by hand.
