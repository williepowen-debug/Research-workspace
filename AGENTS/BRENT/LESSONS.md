# BRENT LESSONS.md

*Review at spawn. Add mistakes as they happen.*

---

## Inherited (from system)

1. **Agent data can be hallucinated.** Verify oil prices, storage levels, rig counts against EIA/primary sources before citing. No naked numbers.
2. **Source tags mandatory.** Every data point: `[CONF]` with source + date, or `[EST]` for estimates.
3. **Don't maintain stale copies.** HAWK owns military ops. HENRY owns VIX. LIQUID owns HY OAS. Reference their values, don't copy.
4. **Write synthesis .md for major data releases.** EIA weekly, OPEC decisions, Baker Hughes — extract the 5 things that matter, not raw data.

## Oil-Specific

5. **Oil prices are 24/7.** STATUS.md prices go stale fast. Always `web_search` for live prices before updating.
6. **Crack spreads tell the real story.** Crude price alone is incomplete — refinery margins show where stress concentrates.
7. **Two-phase thesis is the core.** Every data point should be assessed against: "Are we still in Phase 1? Any Phase 2 signals?"
8. **Storage data has reporting lag.** EIA weekly is delayed. Gulf state storage is estimated (JPMorgan, Kpler). Note the lag.
