---
name: finding-refresh-not-retire-perentity-profiles
description: "When a thesis bump leaves per-entity reference profiles stale, refresh-with-trajectory-preservation beats archive-and-rely-on-aggregator. Aggregator files cannot hold executive quotes, source attributions, deal specifics, or historical trajectory."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 8379bbd6-9b77-4f3e-8f44-b4d99518b3e6
---

When a thesis update makes per-entity reference profiles (per-insurer, per-bank, per-name, per-belligerent, etc.) look stale, the instinct to "retire to archive and rely on the aggregator file" is wrong by default. **Refresh-with-trajectory-preservation is the right move.**

**Why:** Aggregator files (TRACKER-style tables, dashboard summaries) carry the *synthesis layer* — what fired, what the latest reading is, where it routes. They cannot carry the *depth layer*:
- Executive quotes with attribution ("Akira Tsuzuki cited 'low liquidity and elevated volatility'")
- Specific deal commitments by amount + counterparty ($3.25B TCW, ¥500B SMFG, ¥1.6T PC book at Sumitomo)
- Source attributions (TwentyFour AM, AsianInvestor, Bloomberg, Reuters Mar dates)
- Historical trajectory (FY2023 ESR → FY2024 → FY2025 with deltas and what drove each)
- "Why it matters" framing for the entity's role in the thesis

If the per-entity profile gets archived, a future session looking up "what's Nippon's PC position" or "who said what about super-longs" won't naturally find the archived file (archive folders are often labeled "legacy graveyard" or "do not add to"). The depth layer effectively disappears from the working set even though the data still exists on disk.

**How to apply:**

When auditing stale per-entity reference files during a thesis bump:

1. **Don't archive by default.** The retire-vs-refresh question should default to REFRESH unless the entity is genuinely no longer relevant to the thesis (extinct firm, abandoned vector, etc.).

2. **Refresh-with-trajectory-preservation pattern:**
   - Update the header line with current data
   - Add a new section for the latest event/disclosure ("FY2025 ESR DISCLOSURE — RESOLVED [date]" or equivalent)
   - **Preserve all pre-event narrative as "Historical Key Data" or "pre-[event] context"** — executive quotes, deal specifics, source attributions, trajectory tables
   - Update "Signals to watch" to forward-looking under the new thesis version
   - Reframe "Why it matters" under the new thesis (don't delete the old framing — restate it under v1.x)
   - Cross-reference resolved predictions / RED challenges where the entity drove the resolution

3. **Don't formula-stamp.** Each per-entity profile should reflect that entity's distinct role in the thesis. (E.g., under SAM v1.5: Nippon = canonical threshold-vs-mechanism trap; Meiji = cleanest base-case datapoint; Sumitomo = strongest individual evidence point with directionally-opposite outcome; Norinchukin = standalone independent reactivation gate; Fukoku = first-mover historical-marker.) Same-shaped sections, different load-bearing content.

4. **The aggregator file gets the synthesis edit; per-entity files get the depth edit.** Both. Not one or the other.

5. **Check CLAUDE.md before deciding.** Agent CLAUDE.md files often flag per-entity profiles as "stale; retire-vs-refresh deferred to [event]." If that event has now landed, run the retire-vs-refresh decision — and default to refresh per above.

**Validation case:** SAM v1.5 propagation sweep 2026-05-27 evening. Initial recommendation was retire-Big-3-mutual profiles (Nippon / Meiji Yasuda / Sumitomo) after TRACKER absorbed their FY2025 ESR data. Will pushed back: "I am not sure we want to completely archive our knowledge of the big three insurers. Are we sure this data is not needed?" Pushback was correct — refresh path preserved 7 profiles' worth of executive quotes, deal specifics, and historical trajectory that TRACKER's table form could not carry. Each profile took 3-7 min; total ~30 min for all 7. Behavioral upside: future sessions and RED audits can deep-dive into individual entities without having to dig into archive.

**Transferable to:**
- CARL — if there are per-bank profiles for regional banks
- REGINALD — per-name BDC / credit profiles
- HENRY — per-vol-product or per-position profiles
- BROCK — per-spread-pair or per-instrument profiles
- HAWK — per-belligerent / per-conflict profiles
- BRENT — per-field / per-refinery / per-route profiles
- Any agent with a multi-doc layered architecture (aggregator + per-entity reference)

**Anti-pattern:** Per-entity profiles that DUPLICATE aggregator data without adding depth. Those are correctly retired. Refresh-not-retire applies when the per-entity file carries content the aggregator can't.

Related: [[feedback_audit_behavioral_ranking]] (rank cleanup findings by behavioral impact before line-count); [[finding_followup_audit_pass]] (re-read after scoped ask, surface adjacent staleness).
