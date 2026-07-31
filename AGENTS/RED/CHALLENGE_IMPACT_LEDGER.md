# RED — Challenge Impact Ledger (harmful-revision measurement)

**Built:** 2026-07-31 (S27b) on PROME's 7/25 task (`inbox/processed/2026-07-25_from-PROME_harmful-revision-ledger-task.md`, from `AUDITS/2026-07-22_system_analysis_v2.md` §12 Priority 6). **Question measured:** of the revisions RED's challenges forced on target theses, did any make the thesis materially *worse* against subsequent evidence known today?

**Population:** all 43 rows of `workbook/CHALLENGES.tsv` (CHG-RED-001…043) + the SAM V1.6 dialogue (rows 029-032, 039). Source of truth for pre/post states: the frozen `Key_Finding` / `Resolution` fields of each TSV row, the `challenges/` files, and target-agent commits cited therein. Read-only against owners' files; no thesis or threshold moves anywhere in this work.

---

## RUBRIC (pre-registered 2026-07-31, committed BEFORE any row was graded — grading follows in a separate commit)

**Unit of grading = the ACCEPTED REVISION**, not the challenge's quality. A revision is "accepted" only if the record shows the target changed its thesis/spec/estimate because of the challenge (target's own response file, commit, or version ship citing the challenge). A clever challenge that produced no accepted revision cannot be IMPROVED or HARMED — it goes to NO-REVISION and its rebuff is sub-graded.

**Verdicts:**

| Verdict | Test (against subsequent evidence known today, 2026-07-31) |
|---|---|
| **IMPROVED** | Evidence sides with the POST-revision state over the pre-revision state: the outcome landed nearer the revised estimate; a falsifier the challenge forced into registration later fired/bound usefully; a claim the challenge removed was later shown false. Process-only revisions (registration, provenance, reproducibility) grade IMPROVED only if they later **bound** (were exercised on real data); otherwise NEUTRAL-PROCESS. |
| **NEUTRAL** | Revision neither vindicated nor punished: spec never exercised, hygiene with no downstream consequence, or evidence genuinely balanced both ways. |
| **HARMED** | Evidence sides with the PRE-revision state: the revision moved an estimate away from what then happened, or trimmed/retired a leg that then fired. Magnitude stated (weight-points moved, decision consequence). Graded against elegance NEVER — only against outcomes. |
| **UNRESOLVABLE-YET** | The revision's own test window is still open. The resolving date/event must be named. A real category, not a miss. |
| **NO-REVISION** (failed attack) | Owner rebuffed, challenge died on evidence, or nothing was adopted. Sub-grade the rebuff: REBUFF-RIGHT / REBUFF-WRONG / REBUFF-UNTESTED vs subsequent evidence. |
| **UNGRADEABLE** | No frozen pre/post state exists in the record to grade against (early-cohort sweep rows). Counted in the denominator disclosure, excluded from rates. |

**Multi-leg rule (packet guard):** where one challenge produced several revision legs that diverge (e.g., a confidence cut + a channel retirement), legs are graded separately and itemized; the row's headline verdict is the most decision-relevant leg.

**Evidence discipline:** pre/post states quoted from the frozen record (file+row or commit); subsequent evidence carries source+date; no retro-editing of what the challenge actually demanded. Where RED's challenge was directionally right but RED's own *sizing/weight* consequence was wrong, both are logged — the second does not launder the first.

**Conflict flag ⚑:** rows where the grader-is-graded tension bites (self-challenges; revisions to RED's own hypothesis weights; rows where RED wrote both the challenge and the resolution text) are marked ⚑ for PROME's independent spot-check.

**Rates reported:** harmful-revision rate = HARMED / (IMPROVED + NEUTRAL + HARMED) — i.e., over resolvable accepted revisions only — plus every denominator: total rows, rows with an accepted revision, rows gradeable at all.

---

*Grading appended below this line in a separate, later commit — per the pre-registration guard.*
