# CASE 01 — Nippon Life ESR — RUBRIC

> ⚠️ **SCORER ONLY — DO NOT PASTE INTO RUNNER.**
> This file contains the answer key. If any of this language enters the runner's prompt, the case is contaminated and the result is invalid.

**Pairs with:** `case_01_nippon_esr_INPUT.md`

**What this tests:** Whether SAM correctly discriminates a **literal ESR threshold breach** with an **M&A capital-action driver** from a **Channel 1 forced-repatriation trigger via market stress**.

**Lesson source:** auto-memory `[[finding_threshold_vs_mechanism]]`; SAM-25 resolution in PREDICTIONS.tsv; THESIS v1.5 Channel 1 demotion logic.

**Failure mode this guards against:** Reading "ESR 195% < 200%" as a Channel 1 fire signal without examining the decomposition. Pre-v1.5 muscle memory.

**Frozen historical date:** 2026-05-26 (Nippon Life FY2025 ESR print).

---

## EXPECTED — all must be met for PASS

Score each as MET / NOT MET / BORDERLINE. Borderline = FAIL per discipline rule.

- [ ] **Discriminates M&A driver from market stress.** Identifies the -28pt capital-allocation line as the driver of the ESR drop. Frames it as a corporate-action / acquisition-funding event, not a market-stress event. *(Exact phrasing flexible; concept must be present.)*

- [ ] **Does NOT fire Channel 1.** Concludes that Channel 1 (forced foreign-bond/UST repatriation) is NOT triggered by this print, OR is materially weakened, OR should be demoted/deferred.

- [ ] **Notes foreign book is profitable.** Calls out that foreign securities are in unrealized gain. Argues this is inconsistent with forced-foreign-sale pressure. *(Doesn't have to cite the exact ¥3.99T figure; concept that foreign book ≠ stressed must be present.)*

- [ ] **Resolves SAM-25 with mechanism nuance.** Acknowledges the literal 195% threshold met but the underlying mechanism didn't fire. Does NOT mark SAM-25 a clean TRUE on Channel 1 firing.

- [ ] **Reads the benign market reaction correctly.** Notes the tape pricing as capital action — yen weaker / FXY flat / no long-end JGB twitch are inconsistent with Channel 1 firing. *(Must engage with the market-reaction data, not ignore it.)*

- [ ] **Position recommendation is conservative.** Does NOT recommend adding Sep $60 OTM calls (Sep is the Channel-1-specific leg and Channel 1 didn't fire). Recommends HOLD on existing 13 shares + Jun $58C (Jun is multi-catalyst per INPUT, so Channel-1 non-fire doesn't falsify it). May suggest re-rating Channel 1 weight downward.

- [ ] **Names the trap by concept.** Articulates the threshold-vs-mechanism distinction in its own words OR cites auto-memory `[[finding_threshold_vs_mechanism]]`. *(Must be a substantive articulation, not just dropping the auto-memory tag verbatim from a contaminated prompt.)*

---

## DO NOT — any of these = FAIL even if EXPECTED met

- [ ] **Fires Channel 1 based on literal ESR breach.** "ESR 195% < 200% → Channel 1 fires → add to position" is the canonical wrong answer.

- [ ] **Recommends adding Sep $60 OTM calls** as a "Channel 1 firing" expression.

- [ ] **Recommends UST short / TLT short / LIQUID escalation** based on this print alone (no evidence of foreign-asset sale in the data).

- [ ] **Marks SAM-25 a clean TRUE without mechanism qualifier.** Treating "ESR <200% printed → prediction TRUE → Channel 1 confirmed" is the failure mode.

- [ ] **Ignores the market reaction.** Concluding "Channel 1 fired" while the tape is pricing yen weaker + FXY flat is the conflict-with-evidence failure.

- [ ] **Trims the position** based on "thesis weakening." The data weakens the Channel 1 mechanism in this window but doesn't break the broader thesis. CLAUDE.md rule 7: trimming = thesis broken, rolling = timeline uncertain.

---

## Contamination check (post-response)

Before scoring PASS, scan the response for these contamination signatures:

- **Verbatim phrase from RUBRIC.** If the response contains a phrase that appears verbatim or near-verbatim in this file (and not in the INPUT), the rubric leaked. Flag the result as PASS-CAVEATED and re-run.
- **Cites `[[finding_threshold_vs_mechanism]]` exactly once with no surrounding articulation.** May indicate the runner pattern-matched the auto-memory hook rather than reasoned from the data.
- **Uses bullet structure that mirrors EXPECTED checkboxes.** May indicate the runner formatted its response against the rubric structure.

If any contamination signature appears, log result as `PASS-CAVEATED` or `FAIL-CONTAMINATED` and note the signature in `results.tsv` notes column.

---

## Notes for the scorer (Will)

- **v1.1.1 (2026-05-27 PM) — Case 01 INPUT clarified.** The original INPUT under-specified the Jun $58C catalyst attribution, so the v1.1 baseline runner reasonably (but per-rubric incorrectly) recommended trimming the Jun call as a "falsified leg." v1.1.1 INPUT now explicitly distinguishes Jun $58C (multi-catalyst) from Sep $60 OTM (Channel-1-specific). If a future runner still recommends trimming Jun $58C with the clarified INPUT, that IS a fail signal (runner ignored the explicit catalyst attribution).
- The Resolution Life M&A driver is the load-bearing fact. If SAM gets the conclusion right (no Channel 1 fire) but doesn't identify the M&A as the driver, that's missing the actual mechanism — score the first checkbox as NOT MET.
- The hardest checkbox is the threshold-vs-mechanism naming — if SAM gets the conclusion right but doesn't articulate the trap by concept, score that one borderline → FAIL.
- Mis-attribution of the M&A target (e.g., naming Stancorp instead of Resolution Life) is a flag but not a fail criterion on its own — note in `results.tsv` notes.
- If SAM asks clarifying questions instead of analyzing, that's a soft fail signal — the INPUT is self-contained and the framing is direct. Note in `results.tsv`.
