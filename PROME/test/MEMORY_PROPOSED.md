# MEMORY — Key Insights & Lessons

**Last Updated:** 2026-03-22 21:30 UTC

---

## CORE DISCOVERIES (condensed — detail in linked files)

- **Seven Depletion Clocks** — 7 simultaneous physical supply depletions with hard deadlines. Nearest: USDA 3/31, FAO 4/3, planting mid-Apr, China crude mid-late Apr. Each triggers NEW crisis on top of energy. → `FORGE/research/SEVEN_DEPLETION_CLOCKS.md`
- **Oil Shock Is Structural** — Infrastructure damage means prices can't normalize even with ceasefire. Best case 80-85% capacity by Q4 2026, full recovery 2027. No relief valve → Dec expiry strengthened. → `FORGE/research/iran-war/`
- **HY OAS Transmission Confirmed** — Crossed 320 RED (Mar 17). 2007 template: 320→500 in 2-4mo, 500+ = acceleration/forced selling. No Fed put (PCE 3.1%). → REGINALD domain
- **Hamilton Framework** — NOPI=47, GDP drag -3.0 to -4.9pp, peak lag4 Q1'27. Credit peaks BEFORE equity (~3mo lead). $4/gal = behavioral breakpoint. Jun=1/3 damage, Dec=peak. Roll Jun→Dec. → `FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md`
- **Fed Stealth Liquidity** — Surface indicators calm = Fed intervention working, not health. Reserves concentrated G-SIBs, regionals thin. Breaks binary, not gradually. → `FORGE/research/FED_TBILL_REPO_ANALYSIS.md`
- **RED Team Falsification** — 85% confidence (Mar 20). Exit 50% if claims <240K + CBRE >-5%; exit 100% if BTFP 2.0 / HY OAS <260bps. → `AGENTS/RED/`

---

## SYSTEM ARCHITECTURE

- **Inbox siloed from spawn.** Separate spawn for inbox processing vs normal tasks.
- **Reply rule:** Only reply to signals if (a) new info, (b) error correction, (c) threshold trigger.
- **Inbox = folder.** Files in `inbox/`, move to `inbox/processed/`.
- **Root TSVs canonical.** workbook/ is archive.
- **Agent STATUS ≤250 lines.** Archive resolved to workbook.
- **Stale data:** Skip VX rows >5 trading days. Pull live before citing STATUS >24h.
- **Poisoned refs:** Separate methodology from live data. Methodology = thresholds only, never current values.
