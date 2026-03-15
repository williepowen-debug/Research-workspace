# HENRY — RECON DRY RUN EVALUATION
**Date:** 2026-03-15 (simulated)
**Agent:** HENRY
**Task:** Evaluate Stage 1 recon prompt before live deployment

---

## 1. Does the prompt make sense?

Yes, clearly. The ask is unambiguous: read your state files, identify what's stale or unknown, produce structured search targets. The distinction between Stage 1 (recon planning) and Stage 2 (actual searching) is well-drawn. No confusion.

One minor ambiguity: "You have NOT had access to live news since your last update" — the prompt doesn't specify *when* that last update was. For a clean dry run this is fine, but in a live run the agent needs to know the gap. If STATUS.md is timestamped, the agent can infer it (STATUS.md says "Last Updated: 2026-03-13 17:30 UTC"). That works. But if STATUS.md ever lacks a timestamp, the prompt breaks. Recommend adding: "Your last update was [DATE]. Today is [DATE]." or "Check STATUS.md header for last update date."

---

## 2. File Coverage

**STATUS.md** — Essential. Contains the dashboard, vector scores, positions, and recent signal log. The most information-dense file for identifying stale data. ✅

**KB.tsv** — Useful but partially redundant with STATUS for recent entries. Its main value is surfacing *older* KB entries (Jan-Feb) that may have drifted without STATUS updating them. For a stale-data audit, it's worth including — but the agent should be told to focus on entries with old dates and high `Thesis_Impact`, not scan all ~100 rows. ⚠️ Consider adding: "Focus on KB entries with Date >5 days old and Thesis_Impact = CONSISTENT."

**TRADE.md** — Relevant for surfacing data gaps explicitly flagged in Section 8 (Data Gaps). Generated Mar 7 — 8 days before the simulated run date. Position data (IWM price, VIX term structure, VVIX) is all marked stale with ⚠️ REQUIRES LIVE DATA. Good source for search targets. ✅

**What's missing:**
- `AGENTS/HENRY/domain/ECON_CALENDAR.md` — HENRY's macro release calendar. Without it, the agent can't assess *which upcoming events* are unresearched vs. already covered. FOMC and BOJ are called out in the context block, but what about JOLTS, retail sales, Q1 GDP flash? The calendar would prevent missing a release.
- `CONVERGENCE_REPORT.md` (referenced in STATUS) — Contains vector-level detail. Stale vectors are harder to spot without it. Optional but useful for completeness.

**What's not useful:**
- Full KB scan for early January entries (ML-HEN-001 through ~030) is low value — those are structural baseline entries, not time-sensitive data. Could waste context/time. Filtering guidance would help.

---

## 3. Context Gaps

The context block is lean but functional for FOMC/BOJ week. What's there:
- Date ✅
- War Day count ✅
- Brent level ✅
- FOMC timing ✅
- BOJ timing ✅

**What would improve search target quality:**

- **Current SPX/IWM levels** — TRADE.md and STATUS.md are 2+ days stale on price. Knowing "SPX ~6,550" vs "SPX ~6,800" changes which trigger levels are live. Consider adding last known price levels to context.
- **VIX current level** — STATUS shows 23.61 (Mar 6 close). That's 9 days stale. The agent needs to know whether to search for "VIX term structure current" at 23 vs. 30 vs. 35. Big difference for trade decisions.
- **Whether FOMC dots have leaked** — context says FOMC Monday-Tuesday, presser Wednesday. Has anything leaked? The agent can't know, but the context block could note "no pre-leak signals as of [date]."
- **Hormuz status update** — "Brent $100+" tells us the conflict is ongoing, but is it escalating, stable, or de-escalating? That shapes oil-related search priority significantly.

Minor: BOJ presser date listed as "March 19" but description says "BOJ Wednesday" — March 19, 2026 is a Thursday. Small inconsistency worth fixing before live run.

---

## 4. Output Format

The four-section structure (STALE DATA → KNOWN UNKNOWNS → SEARCH TARGETS → CROSS-AGENT NEEDS) is logical and well-ordered. No friction.

**Small friction points:**

- **STALE DATA** asks for "last known value and date" — straightforward from STATUS.md. Works well.
- **KNOWN UNKNOWNS** — good framing, but STATUS.md doesn't have a dedicated "pending/unresolved" section. The agent has to infer these from prediction statuses (HEN-02, HEN-03, etc.) and WHAT TO WATCH items. This is doable but slightly more interpretive than the other sections. Consider adding: "Check PREDICTIONS table for ACTIVE items with no recent signal update."
- **SEARCH TARGETS** — the priority tiers (🔴/🟠/🟡) tied to FOMC/BOJ week is smart context-anchoring. Clean.
- **CROSS-AGENT NEEDS** — good inclusion. HENRY regularly needs SAM (JPY/BOJ), CARL (consumer/claims), REGINALD (credit/HY OAS). This section will naturally surface those dependencies.

---

## 5. Scope Concerns

**8-15 search targets: slightly low for HENRY's domain on an FOMC/BOJ week.**

From my file review alone, I can already identify:
- 8 stale data points in TRADE.md Section 8 (all flagged ⚠️ REQUIRES LIVE DATA)
- ~5 active predictions needing status checks (HEN-02, HEN-03, HEN-04 resolution, HEN-05, HEN-06)
- 3-4 market structure items (VIX term structure, VVIX, GEX, HY OAS current level)
- 2-3 geopolitical updates (Hormuz current status, Iran negotiation signals, Navy EOM timeline)
- 2 calendar events to research (FOMC dot plot expectations, BOJ rate decision odds)

That's ~20-22 natural targets before prioritization. Forcing to 8-15 means either losing coverage or writing vague queries. 

**Recommendation:** Raise ceiling to 20, keep floor at 8. Or allow "8-15 high-priority + up to 5 low-priority overflow." The current ceiling will produce either: (a) artificially merged queries that are too broad, or (b) missed coverage of real gaps.

---

## 6. Questions for Prome

1. **Is the ECON_CALENDAR.md file current?** If it's stale, HENRY might generate search targets for releases that already happened. Should the recon prompt include a calendar check?

2. **Should HENRY search for cross-agent data in Stage 2, or flag it and let the respective agent do the search?** The CROSS-AGENT NEEDS section implies flagging only, but if SAM is offline or stale, should HENRY pull JPY/BOJ data directly?

3. **Is there a position changes log?** TRADE.md was generated Mar 7 and STATUS notes positions added Mar 10-12 (TLT, CF, WAL). There may be no single file that shows current position state accurately. For a live run, HENRY needs to know actual current positions before generating trade-relevant search targets.

4. **What's the output destination for Stage 2 results?** RECON_REPORT.md tells Stage 2 *what* to search. But where do Stage 2 results land? Back into KB.tsv? A separate RECON_RESULTS.md? Knowing this affects how HENRY formats the search targets (more vs. less structured queries).

5. **BOJ date inconsistency:** Prompt says "BOJ Wednesday (Ueda presser March 19)" — March 19, 2026 is a Thursday. Which is it? If Wednesday, date is March 18. If Thursday, day label is wrong. Should fix before live run.

---

## Overall Assessment

**Prompt quality: Strong. Ready for live run with minor fixes.**

The core structure is sound. File selection is 80% right (add ECON_CALENDAR.md). Context block is sufficient for the FOMC/BOJ framing but would benefit from current price levels and Hormuz status. The 8-15 target ceiling is the main constraint I'd push back on — HENRY's domain is wide and this is a high-signal week. Raising to 20 would produce better coverage without meaningfully increasing Stage 2 cost.

The prompt will generate a useful, actionable RECON_REPORT on live run. Recommend fixing the BOJ date, adding the calendar file, and loosening the search target ceiling before deploying.

---

*HENRY | Dry Run Evaluation | 2026-03-15*
