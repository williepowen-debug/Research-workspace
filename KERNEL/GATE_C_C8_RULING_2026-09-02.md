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

## AMENDMENT — build-spec gate on leg 3 (PROME 2026-09-02 12:5x ET; external review relayed by Will 12:43, every citation PROME-verified at the artifact before adoption; the ruling itself is unchanged)
**Finding (🟠, verified):** the accepted Kernel records carry no structured three-outcome vector — `schemas/question.schema.json` permits only `forecast_family: BINARY_PROBABILITY`; `schemas/forecast.schema.json` stores one scalar `probability`; `tools/core.py` `_question_payload` rejects every other family (`FAMILY_NOT_ENABLED`); `tools/render.py` computes a binary Brier from that scalar. MIDAS-06's accepted `ForecastSubmitted` event (`EVT-…006b`) carries `probability: 0.45` only; the NO 0.20 / AMBIGUOUS 0.35 masses live in prose (`decision_consequence`, the native companion). A renderer that read them from prose or from the mutable companion would break the event-derived model. And "scores on the declared mass" is under-specified: for realized YES, binary Brier = 0.3025 · unnormalized multiclass = 0.465 · half-normalized = 0.2325 — three defensible numbers.
**Gate (binding on the DOCKET L247 build, before any code):** the spec letter must define, and pass independent review (DAEDALUS or RED) on —
1. the authoritative STRUCTURED carrier for `outcome_vocabulary` and the complete probability vector;
2. how MIDAS-06 acquires that carrier without editing an accepted event or extracting numbers from prose (a successor command class, or a projection-metadata declaration keyed to the immutable event — named, not assumed);
3. the exact multiclass scoring rule and its normalization, with the three candidate numbers above as the worked example;
4. validation: sum-to-one, duplicate label, missing label, realized label ∈ vocabulary;
5. whether this is projection metadata or a schema-v2 / native-event change — and therefore which review seat and which activation class it needs.
**MIDAS-06 stays excluded (`OUTCOME_VOCABULARY_MISMATCH`) until the spec passes review.** The (a) direction stands; the registration had jumped from "approve three outcomes" to "renderer change" without the data-and-score contract between them — PROME's miss, recorded.
