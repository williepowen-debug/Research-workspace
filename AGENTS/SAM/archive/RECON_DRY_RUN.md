# SAM — RECON PROMPT DRY RUN EVALUATION

**Date:** 2026-03-15 (Sunday)
**Evaluator:** SAM (subagent dry run)
**Prompt evaluated:** Stage 1 RECON REPORT prompt

---

## 1. Does the prompt make sense?

**Yes, clearly.** The structure is unambiguous: read my domain files, identify what's stale and what I don't know, produce a prioritized search list. The separation of STALE DATA / KNOWN UNKNOWNS / SEARCH TARGETS / CROSS-AGENT NEEDS is logical and maps well to how intelligence gaps actually accumulate.

One minor framing note: "You have NOT had access to live news since your last update" is a useful grounding statement, but the prompt could clarify *when* the last update was. STATUS.md is last updated **Mar 13, 17:30 UTC** — that's 2 days of gap into March 15. Worth saying explicitly: "Your last update was Mar 13 ~17:30 UTC." That anchors the stale data dating and prevents over- or under-estimating what I've missed.

---

## 2. File coverage

**Critical problem: `KB.tsv` does not exist.**

The workbook directory contains:
- `ML.tsv` — master log (events/findings, dated)
- `VX.tsv` — values/indicators log
- `FLOW.tsv` — institutional flow tracking
- `VX_HISTORY.tsv` — historical values

There is no `KB.tsv`. If deployed as written, the prompt will hit a read error or return nothing useful. This needs to be corrected to the actual file names before Stage 2.

**Recommended fix:** Replace `AGENTS/SAM/workbook/KB.tsv` with one or more of:
- `AGENTS/SAM/workbook/VX.tsv` — for stale data detection (time-stamped values)
- `AGENTS/SAM/workbook/ML.tsv` — for event/finding gaps
- `AGENTS/SAM/workbook/FLOW.tsv` — for institutional flow tracking

VX.tsv is probably the most useful for generating "stale data" targets, since it tracks specific values with dates. ML.tsv for known-unknowns.

**STATUS.md coverage: excellent.** It's dense but comprehensive — it contains USD/JPY levels, BOJ scenario probabilities, repatriation flow data, cross-agent flags, and dated alert tables. It's the right anchor file.

**TRADE.md coverage: partial.** TRADE.md is dated **Feb 14** and reflects the pre-Iran-war state. It still shows EWJ puts / FXY calls as watchlist items with Feb 19 Shunto triggers that have long since passed. As a "trade-relevant vectors" file it's stale but still structurally useful for understanding what positions are being tracked. Real-time positioning context lives in STATUS.md. Worth noting in the prompt that TRADE.md may be outdated and SAM should weight STATUS.md as authoritative on current trade state.

**Missing file worth considering:** `AGENTS/SAM/PREDICTIONS.tsv` — this tracks probabilistic calls with dates and could be valuable for identifying stale predictions. Would help generate "did this resolve?" search targets.

---

## 3. Context gaps

The context section is **good but has one gap and one ambiguity:**

**Good:**
- USDJPY 159.717 Friday close is specific and directly usable
- BOJ Thursday + FOMC Monday-Tuesday creates a tight event calendar
- War Day 14 / Brent $101.07 situates the energy context
- "Markets closed today" prevents me from looking for live data

**Gap — Shunto:** The context doesn't mention Shunto status. My STATUS heavily tracks Shunto (first tally expected Mar 21 per my files). Is the Mar 21 Shunto tally still on schedule? Has any preliminary data leaked? This is the most BOJ-relevant domestic variable and it should be in the context if known.

**Ambiguity — TIC data:** STATUS.md flagged the March 15 TIC release as a key watch item (Japan UST holdings, January data). The context is silent on whether this released and what it showed. If TIC data dropped on Saturday (as scheduled in my STATUS), it should be in the context — it's one of my top-tracked signals.

**Ambiguity — NFP aftermath:** NFP was -92K. The context states this but doesn't say how USD responded beyond yen weakening. Knowing whether DXY rallied or fell into the weekend would help me calibrate the "yen weakened despite bad NFP" framing better.

These are minor — the context is sufficient to generate useful search targets. But adding Shunto status and TIC data result (if released) would significantly improve search target quality.

---

## 4. Output format

**No friction.** The four sections (STALE DATA / KNOWN UNKNOWNS / SEARCH TARGETS / CROSS-AGENT NEEDS) are well-structured and map naturally to how I'd reason through this.

The SEARCH TARGETS format (Query / Why / Last Known / Priority) is exactly right — it forces specificity rather than vague topic-naming. The Priority tiers (🔴 FOMC/BOJ week | 🟠 important | 🟡 nice to have) are appropriate for the current event density.

One suggestion: add a **"Who updates this?"** field to CROSS-AGENT NEEDS, even if just a guess. Stating "this belongs to LIQUID" vs. "unclear ownership" would make the consolidation step faster for Prome.

---

## 5. Scope concerns

**8-20 is the right range for my domain in this specific week.**

Given BOJ Thursday + FOMC Monday-Tuesday + war ongoing + FY-end 16 days away, I would naturally generate:
- ~4-5 🔴 targets (BOJ pre-meeting signals, USDJPY intervention proximity, Ueda pre-meeting communication, Shunto status, FOMC impact on rate differential)
- ~4-6 🟠 targets (TIC data result, MoF flow data, JKM/LNG pricing, life insurer statements, JGB auction results)
- ~3-4 🟡 targets (Nikkei levels, cross-currency basis, GPIF positioning, Taiwan LNG update)

That's ~11-15, comfortably within range. 20 would be slightly exhausting but not harmful. 8 would feel artificially constrained given current event density. No changes needed.

---

## 6. Questions for Prome

1. **KB.tsv doesn't exist — what should I read instead?** This is the blocking issue. Should I read VX.tsv + ML.tsv as a substitute? Or just read STATUS.md more carefully and skip the workbook entirely?

2. **Did TIC data release on March 15 as scheduled?** My STATUS.md flagged this as a critical watch item. If it dropped, please include the Japan UST holdings change in the context — it would significantly focus my search targets.

3. **Shunto March 21 tally — any preliminary data?** If any major union results leaked before Sunday, that changes my BOJ pre-meeting assessment.

4. **FOMC context — is there any pre-meeting Fed communication I should know about?** My STATUS has FOMC as same week as BOJ but I have no context on current Fed expectations. Is the March FOMC a live cut? Hold? What's the dot plot situation?

5. **Should I read PREDICTIONS.tsv?** It's in my directory and tracks probabilistic calls by date. Might help identify which predictions have gone stale or resolved, but not in the original prompt spec.

6. **Is SAM_COUNTER_THESIS.md (archived) still relevant?** It's in the archive/RED_old folder. Probably not, but worth confirming before I skip it.

---

## Summary

The prompt is well-designed and will produce useful output with one blocking fix: **replace `KB.tsv` with `VX.tsv` and/or `ML.tsv`**. Everything else is minor polish. The context section would benefit from TIC data result (if available) and Shunto preliminary status. Recommend also considering adding `PREDICTIONS.tsv` to the read list.

Ready to execute real run once file reference is corrected.
