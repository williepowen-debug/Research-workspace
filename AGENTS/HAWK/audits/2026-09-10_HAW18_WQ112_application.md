# HAW-18 — WQ-112 scoring-vintage application (DOCKET L306)

**HAWK's half of the joint HAWK/DAEDALUS owner application. Delivered 2026-09-10 12:3x ET, one day ahead of the L306 due date (2026-09-11).**
**No score edited. No new scoring rule proposed.** PROME's 2026-09-08 packet authorises the application and explicitly forbids both.

## The question, stated narrowly

HAW-18's machine `Confidence` field changed **60% → 55%** on 2026-07-25, ten minutes after first publication and ten days before the row resolved FAILED (2026-08-04). WQ-112(ii) requires a re-mark to "land in the machine field **with its date**." The 55% **is** in the machine field; its **date** sits in `Notes`, not in a `Remark_Date` field — because the `Remark_Confidence`/`Remark_Date` convention (`BLUEPRINTS/market-agent.md` §5) is **forward-only and postdates this registration**.

**Eligible, or not?** That is the whole of the open point. Nothing else about HAW-18 is uncertain.

## Documentary record — HAWK and DAEDALUS independently agree, no disputed fact

| Artifact | Observation |
|---|---|
| `a552c04be`, 2026-07-25 16:40:43 ET | HAW-18 machine `Confidence` **60%**, Status OPEN, no resolution date |
| `7b103dc29`, 2026-07-25 16:51:02 ET | HAW-18 machine `Confidence` **55%**, Status OPEN, no resolution date |
| Same blob, `Notes` | Explicit **dated** same-session registration correction, 2026-07-25, describing 60→55, before resolution evidence |
| Same blob, header | 10 columns; **no** `Remark_Confidence`/`Remark_Date` pair; the `Confidence` cell is a bare `55%` |
| Resolution | FAILED 2026-08-04 — **outcome not in question and not touched here** |

**Elapsed between the two commits: 10m19s.** DAEDALUS's independent run: `AGENTS/DAEDALUS/runs/2026-09-08_HAW18_SCORING_APPLICATION.md`. HAWK's: `proposals/2026-09-08_batch2_rule-decisions.md` §HAW18.

## Application of the existing canon

WQ-112 (`FORGE/PREDICTION_DISCIPLINE.md` §Grading & re-marking, Will-ratified 2026-09-01) has two limbs:

- **(i) the LATEST dated pre-resolution mark governs scoring**; Date_Made confidence is retained and reported separately as first-call calibration.
- **(ii) a re-mark is valid only when it lands in the machine field with its date** — *"a narrative-only re-mark is not a mark and does not score."*

**Limb (ii)'s stated mischief is named in its own text: BRT-26, "a reasoned ~58% [7/28] that NEVER REACHED THE FIELD."** The rule exists to exclude confidence that lived only in prose while the scoreable number sat unchanged.

**HAW-18 is the opposite case on exactly that axis.** The machine field itself moved, in a committed artifact, while the row was OPEN, ten days before any resolution evidence. What is absent is not the mark and not the date — both are on the record — but the **encoding form** in which a 2026-09 convention would have carried the date.

## Determination HAWK recommends

> **The 55% is ELIGIBLE. Scoring vintage = 55%; first-call calibration = 60%, reported separately, both preserved.**

**Reasoning.** Reading limb (ii)'s *form* as an eligibility bar applies a **forward-only encoding convention retroactively**, and it would disqualify the mark not because the desk failed to hold or record it, but because **the field to record its date had not been invented yet**. That converts an encoding rule into a retroactive scoring rule — which WQ-112 does not say, which `market-agent.md` §5 expressly disclaims by declaring itself forward-only, and which PROME's packet does not authorise. The mark's date is independently established to the minute by two artifacts (the dated `Notes` correction; the commit timeline 16:40:43 → 16:51:02), so nothing has to be reconstructed to accept it.

**What this determination does NOT claim** (both desks flagged the same limit, and it stands): git commit time **is not** a `Remark_Date` field and must not be silently promoted into one; no retrospectively reconstructed field date has been inserted to make any check pass; and the correction's own statement that it preceded resolution evidence is **not** upgraded into a complete information-timeline audit.

## ⚠️ Conflict disclosure — the determination runs in HAWK's own favour

On the recorded **FAILED** outcome, conditional Brier contributions are **0.3025 at 55%** and **0.3600 at 60%** — accepting 55% **improves HAWK's own score by 0.0575**. HAWK is the beneficiary of the determination it is recommending, so it is stated here rather than left for a reader to notice (`finding_asymmetric_rigor_counterparty_claims`, pointed inward).

**The direction-blindness test, run explicitly:** the rule recommended is *"the machine field changed contemporaneously while OPEN and before resolution evidence ⇒ the latest field value scores."* Had HAW-18 been corrected **55 → 60** and then FAILED, that same rule would score the desk at **60% (Brier 0.3600)** — the worse number. The rule does not know which direction it is running in, and HAWK would be bound by it either way. That is the only ground on which a self-favouring determination should be accepted.

These remain **sensitivity calculations, not an adopted score** and not a recomputed fleet average.

## Disposition

- **HAWK's application: delivered.** Recommendation above, with reasoning and the conflict disclosed.
- **DAEDALUS:** documentary half published 2026-09-08; concurs on every fact and routes the eligibility point onward.
- **The eligibility word is NOT taken here.** DAEDALUS routed it to PROME/HAWK; HAWK is the interested party, so HAWK **recommends** and does not rule. **PROME/Will takes it.**
- **Until ruled:** both vintages stay preserved and the scoring vintage stays labelled **unresolved** on the record. `thesis/PREDICTIONS.tsv` HAW-18 is **untouched by this session** — no score edit, no Notes rewrite, consistent with the packet.
- HAW-01 premise and HAW-04/05 provenance residuals remain **separate** and are not addressed here.
