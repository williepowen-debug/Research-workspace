# LIQUID — RECON PROMPT DRY RUN EVALUATION
**Date:** 2026-03-15 | **Agent:** LIQUID | **Task:** Evaluate Stage 1 Recon Prompt

---

## 1. Does the Prompt Make Sense?

Yes, clearly. The task (identify stale data, flag known unknowns, produce search targets) maps directly to what LIQUID actually does between updates. The separation of Stage 1 (recon planning) from Stage 2 (actual searching) is well-structured — it prevents the agent from jumping straight to web searches without first auditing what it knows.

One minor ambiguity: "what moves our positions" implies LIQUID should know what positions are currently live. The positions ARE in STATUS.md (TEN calls, HYG puts), so this resolves when the agent reads its files. But if STATUS hadn't been maintained, "our positions" would be undefined. Low risk given current file hygiene, but worth noting.

---

## 2. File Coverage

**STATUS.md + KB.tsv + TRADE.md — Assessment:**

| File | Usefulness | Notes |
|------|-----------|-------|
| STATUS.md | ✅ High | Primary state file. Has confirmed values + timestamps + pending items. The richest source for STALE DATA and KNOWN UNKNOWNS sections. |
| KB.tsv | ✅ Moderate | Contains structured fact entries with `Date` and `Stale_By` fields — perfect for STALE DATA audit. Small KB (5 entries) right now, but format is ideal. |
| TRADE.md | ⚠️ Low — Currently stale | TRADE.md was last updated **2026-02-14** — nearly a month before the context date of March 15. It references different data (10Y at ~4.5%, RRP at ~$0.86B) than STATUS.md current state. It's structurally useful but is itself a stale file. The agent should know this going in. |

**Missing files the prompt doesn't mention but that LIQUID actually uses:**
- `workbook/VX.tsv` — the active vector tracker. STALE DATA section would be significantly stronger if this were read. Vectors have their own last-updated logic.
- `workbook/FLOW.tsv` — transmission flows. Not critical for search targeting but relevant.
- `workbook/DIFC_TRANSMISSION_MAR11.md` — referenced as ACTIVE in STATUS. Technically in scope for "what's live" but probably overkill for recon.

**Recommendation:** Add `workbook/VX.tsv` as an optional 4th read, or note it's available. TRADE.md is fine to keep — its staleness is actually signal (tells the agent what hasn't been updated).

---

## 3. Context Gaps

The context block is good — specifically:
- War Day 14 + Brent $100+ → immediately relevant to repo/funding thesis
- FOMC Monday-Tuesday is exactly what LIQUID needs to frame search priority
- BOJ Wednesday → relevant via SAM/carry unwind → LIQUID funding transmission

**What's missing that would sharpen search targets:**

1. **Current SPX level / how far it's moved since Mar 12.** STATUS.md has Mar 11 data. The agent needs to know if the market has moved 2% or 10% since its last update to calibrate HY OAS search priority.
2. **Whether LIQ-01 has been confirmed since Mar 13.** STATUS.md flagged this as "confirmation imminent." If the agent doesn't know whether this already fired, it may generate a search target that's already resolved.
3. **TIC data release status.** STATUS.md flagged TIC release on Mar 15 (TODAY). The context should note whether this has already dropped — it's a key data point LIQUID was waiting for.

**Suggested addition to Context block:**
> - TIC data due today (Mar 15) — may already be released.
> - LIQ-01 status unknown — last confirmed HY OAS was 319bps on Mar 9.
> - No SPX/credit data available since Mar 13.

---

## 4. Output Format

The four-section structure (STALE DATA / KNOWN UNKNOWNS / SEARCH TARGETS / CROSS-AGENT NEEDS) is clean and practical. No friction.

Minor note on SEARCH TARGETS format: requiring Query + Why + Priority per item is good discipline. The 3-priority emoji system (🔴/🟠/🟡) aligns exactly with how LIQUID already uses urgency markers in STATUS.md — no translation needed.

One suggestion: add a "**Last Known:**" field to SEARCH TARGETS so Stage 2 results can be compared directly to prior state. Example:
```
- **Query:** "HY OAS BAMLH0A0HYM2 March 2026"
- **Why:** Confirm LIQ-01 trigger (threshold 320bps)
- **Last Known:** 319bps as of Mar 9
- **Priority:** 🔴
```
This makes the Stage 2 agent's job easier — it knows what to compare against without re-reading STATUS.md.

---

## 5. Scope Concerns

**8-15 search targets: appropriate for LIQUID.**

Given LIQUID's domain density (repo, SOFR, RRP, HY OAS, auction results, TIC, FOMC, BOJ all in scope simultaneously), 8-15 is achievable and realistic. On a normal week, 8-10 would be right. This week (FOMC + BOJ + TIC + war ongoing + quarter-end approaching), 12-15 is more realistic.

The "Focus on what moves our positions, not general news" constraint is useful — it would otherwise balloon into 20+ targets during a week this busy.

No scope concerns.

---

## 6. Questions for Prome

1. **Is TRADE.md expected to be current?** It's a month stale. Should the recon prompt instruct the agent to flag TRADE.md staleness explicitly, or is STATUS.md the canonical "live" file and TRADE.md treated as background?

2. **What does Stage 2 look like?** Knowing whether Stage 2 is a single web_search pass vs. a multi-tool research session affects how specific SEARCH TARGETS should be. If Stage 2 is lightweight, 8-10 tight queries is right. If Stage 2 has room to dig, 15 broader targets makes more sense.

3. **Cross-agent needs: is there a mechanism for LIQUID's RECON_REPORT to actually trigger reads from SAM/HAWK?** The format produces the requests, but does Stage 2 or Prome handle fulfillment? Knowing this affects how much detail to put in that section.

4. **Is TIC data confirmed as released before this recon runs?** STATUS.md was waiting for it as of Mar 13. If it dropped today (Mar 15), it's the highest-priority resolved item LIQUID needs — and the recon should be structured around analyzing it, not just searching for it.

5. **Should RECON_REPORT include a brief "state of positions" summary?** The proposals in STATUS.md (HYG puts, TEN calls) have time-sensitive decisions (HYG roll to Sep/Dec, crude short timing). A one-section position health check might be worth adding to the output format.

---

## Overall Assessment

**Prompt quality: 8.5/10.** Well-scoped, appropriate file set, clean output format. The main improvement would be adding 2-3 sentences of "what we don't know since Mar 13" to the Context block — specifically TIC release status and LIQ-01 confirmation status. Those two items will likely dominate the search target list and the context should acknowledge they're unresolved rather than leaving the agent to discover that via file-reading.

Ready to deploy with minor context additions.

---
*Written by: LIQUID subagent (DRY RUN) | 2026-03-15*
