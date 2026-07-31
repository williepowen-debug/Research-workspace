# STRICT TEXT — ten rules for cost-bearing text (fleet build standard)

**Owner:** DAEDALUS · **Created:** 2026-07-31 (Will-approved; provenance: STE/ASD-STE100 adaptation assessment, `design/2026-07-31_STE_WRITING_STANDARD_ASSESSMENT.md` §3B — the "10-line ruleset" option, not the 900-word dictionary).

**Why:** our cost-bearing text is read by LLM sessions with limited context — the modern version of STE's stressed non-native mechanic. A misread packet ACTION line is misexecuted; a hedge-stacked claim can't be graded; a vague error message converts a warning into a post-mortem. Banked incident classes: paraphrase drift corrupting a redelivered instruction ([[finding_backstop_redelivery_is_a_paraphrase_not_a_copy]]), summary compression inverting a meaning ([[finding_triage_summary_compression_inversion]]), PASS lines that mean nothing (PAT-074).

## Scope — STRICT applies ONLY where a wrong reading has a cost

| Surface class | Mode |
|---|---|
| Packet **ACTION/ASK lines** · script output & error messages · gate/threshold/kill specs · the **letter** of a prediction · checklist steps | **STRICT (these 10 rules)** |
| Thesis docs, research prose, audit narratives, STATUS bodies | Output Canon as-is (root `CLAUDE.md §Output Canon`) — dense is fine, line caps force it |
| Will-facing synthesis (Telegram, dashboards) | **VOICE — exempt.** Never lint the operator's reading experience |

## The ten rules

1. **One instruction per sentence** in ACTION blocks; target ≤20 words. Four asks = four sentences (or a numbered list).
2. **Active voice with a named actor.** "REGINALD re-points row 7" — not "row 7 should be re-pointed." An instruction without an actor is a wish.
3. **Verbs, not nominalizations.** "Re-grade X" — not "perform a re-grading of X."
4. **At most one hedge per claim carrying a number** — and prefer a stated probability/confidence tier over any hedge word. "May potentially help to reduce" is zero gradable content.
5. **One name per thing per document.** Entity, metric, file, agent: pick the name, keep it. State tokens come from `BLUEPRINTS/STATE_VOCABULARY.md`.
6. **Every number carries unit + source + as-of date** (root Output Canon, restated here as the per-sentence checkable form — no naked numbers).
7. **Every threshold carries LEVEL + INSTRUMENT + WINDOW** ([[finding_guard_scope_expires_at_the_fill]], [[finding_number_carries_threshold_unit_source]]). "HY OAS ≥300bp (ICE BofA, 3 consecutive sessions)" — not "spreads blow out."
8. **No unresolved pronoun across a sentence boundary in instructions.** Repeat the noun; "it/this/that" pointing at the previous sentence is where misexecution starts.
9. **A status/error message states what it searched and what a null result means** (PAT-074 — audit a check by what its PASS means). "0 ledgers found in workbook/*.tsv (3 TSVs exist outside the glob)" — never a bare benign line.
10. **Redelivery is a copy, never a paraphrase.** Restating another agent's instruction/figure = quote it verbatim with its source stamp.

## What this is not

- Not a style gate — no linter enforces it (ruled DO-NOT-BUILD, assessment §3C: a mechanized style screen false-positives against the best-documented agents; deliberate density and sloppy density are byte-identical from the condition alone).
- Not a prose standard — STATUS/thesis density is deliberate (line caps) and stays.
- Not a vocabulary whitelist — finance vocabulary is the content, not the noise.

**Applied at:** packet templates, new-build script messages, gate/threshold registration (DAEDALUS checks at build — REGISTRATION_CHECKLIST row 15). Blueprint variants cite this file — they do not restate the rules.
