# RECON DRY RUN — LABOR Stage 1 Prompt Evaluation
**Date:** 2026-03-15 (Sun) | **Agent:** LABOR | **Type:** Dry run / prompt QA

---

## 1. Does the prompt make sense?

**Yes — clearly written and unambiguous.** The task is well-defined: read domain state, produce a structured gap list for Stage 2 search. The separation between Stage 1 (triage) and Stage 2 (search) is sound and matches how an analyst would actually work.

One minor friction point: the prompt says "Your last STATUS update was approximately Mar 12" — but STATUS.md has entries through Mar 13 (JOLTS Jan release, NFIB Feb, GDP Q4 second estimate). The agent should know its data goes through end of day Mar 13, not Mar 12. Slightly incorrect framing could cause the agent to generate redundant search targets for data it already has. **Recommend changing "approximately Mar 12" to "end of day Mar 13."**

---

## 2. File Coverage

**STATUS.md — Essential. Keep.** This is the primary state document. It has the convergence matrix, signal dashboard, predictions, and EOD notes. Without it the agent has no context.

**KB.tsv — Valuable but noisy for this task.** At 92 entries, the KB contains a lot of confirmed/superseded historical data. For the purpose of RECON (identifying staleness), the agent mostly needs to scan Stale_By dates and STALE/ACTIVE flags — not read every row. The KB is useful for cross-referencing "last known values" and dates for the Search Targets section. The KB *should* stay in the prompt, but the agent may need to be told to focus on Stale_By < today or Status = STALE/ACTIVE rather than reading every entry.

**TRADE.md — Useful but partially redundant.** For RECON purposes, TRADE.md adds value in two ways: (1) it flags specific data staleness (e.g., VX-LAB-8.04 APO/PSEC as of Sep 30 2025) and (2) it identifies what data *moves positions*, which is exactly the filter needed for search target prioritization. The "focus on what moves our positions" instruction in the prompt is directly served by TRADE.md. **Keep it.**

**What's missing:**
- **`workbook/VX.tsv`** — The STATUS.md notes 70 vectors in VX.tsv. Individual vector Stale_By dates or last-updated fields would catch staleness the KB.tsv doesn't. Not critical to include (STATUS.md captures most of what matters), but if VX.tsv has its own staleness flags, it could add precision. *Nice to have, not required.*
- **Previous RECON_REPORT.md** (if one exists) — To avoid re-generating targets that were already searched last cycle. On first run this doesn't matter, but for recurring runs, the prior RECON_REPORT should be checked to avoid duplication. *Add to prompt once pattern is established.*

---

## 3. Context Gaps

The Confirmed Data section is well-constructed. It gives the agent anchor prices and prevents wasted searches. A few additions would sharpen the output:

**Gaps I'd want filled:**
- **DHS shutdown status as of Mar 15** — The prompt asks about DHS paycheck miss (Mar 14) but doesn't confirm whether the shutdown is still ongoing. My last KB entry (LAB-065, LAB-091) had shutdown confirmed through Day 23+. Has it resolved? This directly determines whether claims data will be clean on Mar 19 (the next print). Without knowing, I'd have to flag it as a search target anyway, but context would sharpen the priority.
- **Current KELYA price** — TRADE.md notes the stop loss at $9.50 and take profit at $5.50. Knowing where KELYA closed Mar 13 would help me assess whether any position action is urgent vs. routine monitoring.
- **ADP NER weekly pulse Mar 10 result** — STATUS.md notes "Alert if <10,000/week" and the next pulse was due Mar 17 (not yet). Fine. But the Mar 10 status is ambiguous — was there a new ADP pulse between the last confirmed (Feb 21 = 15,500) and now? If yes, that data point is missing from Confirmed Data.
- **FL legislative status on UI extension** — TRADE.md flags this explicitly: "FL legislature extends UI. Wave 1 + Wave 2 missed (exhaustion cliff delayed)." If the FL legislature has done anything since Mar 12, that's critical context. The prompt doesn't address it.

These are minor — the prompt is workable without them. But they'd reduce hedge language in the output.

---

## 4. Output Format

**No friction.** The four-section structure (Stale Data / Known Unknowns / Search Targets / Cross-Agent Needs) maps cleanly to how I'd naturally triage:
1. What do I have that's expired?
2. What did I flag for follow-up but never close?
3. What should I search?
4. What do I need from others?

The Search Target schema (Query / Why / Last Known / Priority) is well-designed. "Last Known" forces the agent to actually anchor the value — it prevents vague targets like "check on employment." The priority tiers (🔴/🟠/🟡) work well for this week specifically because FOMC/BOJ is a genuine categorical difference from routine data pulls.

**One potential issue:** The prompt asks for 8-20 targets in a domain that has a lot of open threads right now. With FOMC week, BOJ decision, FL exhaustion cliff, DHS shutdown, Challenger Mar data, WARN pipeline, ADP pulse, and the Confirmed Data section already locking down most macro anchors — the domain has more than 20 relevant things to check. The agent may need to compress or make hard prioritization calls to stay within the ceiling. That's a feature, not a bug — but the agent should be told it's acceptable to hit 20 and note "additional lower-priority targets omitted."

---

## 5. Scope Concerns

**8-20 is the right range for a focused Stage 2.** Fewer than 8 would miss important threads; more than 20 creates noise and dilutes search quality.

For LABOR specifically this week, my honest count of *distinct searchable topics* is approximately 22-26 before filtering. The Confirmed Data section removes about 8-10 of those (claims 213K, NFP -92K, JOLTS Jan, FOMC dates, etc.), bringing the realistic target list to 12-18. That fits the range well.

The instruction to "focus on what moves our positions" is the right compression filter. Pure research curiosity items (e.g., "update on AI productivity 1bp finding") are lower priority than "DHS shutdown resolved?" which determines whether Mar 19 claims data is clean.

---

## 6. Questions for Prome Before the Real Run

1. **DHS shutdown — resolved by Mar 15?** My last confirmed data was Day 23+ (Mar 9). The paycheck miss was flagged for Mar 14 in the Confirmed Data section — does that mean it happened, or is it still TBD? The answer changes whether claims on Mar 19 will be clean or suppressed. This is the single biggest unknown for my domain this week.

2. **War status / Hormuz update** — Confirmed Data says "War Day 14." The prompt says Trump called it "largely complete" around Mar 11 (per STATUS). Has the Hormuz closure status changed by Mar 15? My TRADE.md notes "Hormuz may reopen" as the primary thesis-kill for several positions. If Hormuz is re-opening, that should be in Confirmed Data, not a search target.

3. **Should RECON_REPORT be written if I'm uncertain about the DHS/Hormuz status?** Or is the expectation that I flag those as 🔴 search targets and let Stage 2 resolve them? (I'll assume the latter, but want to confirm.)

4. **Cross-agent needs consolidation process** — The prompt says overlapping needs will be consolidated after all agents complete Stage 1. For LABOR, the main cross-agent needs are: CARL (consumer transmission from FL exhaustion), REGINALD (regional bank credit quality), and SAM (BOJ/yen carry if Shunto shock). Should I flag what I need from those agents even if they're running their own RECON in parallel? (Yes, I assume — just want to confirm the workflow.)

5. **KELYA price as of Mar 13 close** — Not in Confirmed Data. Is it available? Stop loss ($9.50) and take profit ($5.50) depend on knowing the current level. If KELYA is near a threshold, that changes the urgency of the staffing canary search targets.

---

## Summary Verdict

**The prompt is ready to deploy with one recommended fix:** Change "approximately Mar 12" to "end of day Mar 13" in the "Your last STATUS update" line to avoid generating redundant search targets for data already captured (JOLTS Jan, NFIB Feb, GDP Q4 second estimate — all Mar 13 prints).

Everything else works. The file set is correct, the context section is solid, the output structure is clean, and the 8-20 target range fits the domain. The main gaps (DHS resolution, Hormuz status) will likely appear as 🔴 search targets anyway, so the prompt is functional even without those resolved.

*Written by LABOR subagent — 2026-03-15 dry run*
