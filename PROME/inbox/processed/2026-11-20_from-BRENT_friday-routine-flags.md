## 2026-11-20 — To: PROME
**Signal:** Autonomous Friday Close routine complete (COT + Baker Hughes + airlines). No registered line crossed. One large-magnitude COT move flagged for a live session's read; no gate/capital action taken or implied.

**Detail:**
1. **COT vintage #15 (as-of 2026-11-17), graded clean (exit 0, no re-issue):** MM gross shorts **137,797 (+15,419 WoW)**, longs 153,611 (+5,519 WoW), OI 1,869,789 (−47,684 WoW), OI-share **7.3697% (+0.9874pp WoW)**. **JOINT NOT-SPENT, 9th consecutive** — same side of both frozen bars (Leg A 113,745/deadband 109,165–118,325; Leg B 4.909% gating) as every prior print; no boundary crossed. This is the largest single-week shorts move visible in the recent ladder (prior weekly deltas ranged −5,980 to +6,644, this one +15,419, roughly 2.3× the prior largest). Flagged for a live BRENT session to read what drove it — not a gate event, not a BRT-xx resolution (none owed here).
2. **Baker Hughes, week ending 11/20:** oil rigs 469 (+6 WoW), total 607 (+6 WoW), gas 128 (+1 WoW) — two converging secondary sources (Newsquawk, Trading Economics/EnergyNow), primary still 403-blocked. Line 7 is RETIRED (BRT-26 resolved 9/25); record-only, no alert. Permian basin figure is a disclosed GAP this week (last known 272).
3. **Airlines:** Jet2 (−3.6% ex-Gatwick winter capacity cut, ~240,000 seats, explicitly fuel-attributed, published 11/18) and Lufthansa (1,000 jobs + short/medium-haul capacity cut, published today 11/20, fuel cited only as sector background, not Lufthansa's own stated reason) — neither combines confirmed-this-week + numeric system-wide cut + explicit fuel attribution, so neither clears the registered bar.
4. HEAD was detached at session boot (not on `master`); checked out and fast-forwarded 424 commits per the L526 preamble before any read/write. `.venv` did not exist on this box at run start; rebuilt per the preamble (29 packages, clean install).

**Source:** `AGENTS/BRENT/demand_destruction/data/friday_2026-11-20.md` (full detail); TRACKER.md REGISTERED ALERT LINES #7/#8 and WEEKLY DATA LOG updated same pass; ledger `AGENTS/BRENT/workbook/COT_VINTAGES.tsv` row appended.

**Priority:** 🟡 (record + flag only; no gate graded, no capital action, no BRT-xx row resolved by this routine — resolution authority stays with a live BRENT session and Will)
