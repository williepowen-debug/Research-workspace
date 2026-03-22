# MEMORY — Key Insights & Lessons

**Last Updated:** 2026-03-22 21:15 UTC

---

## CORE DISCOVERIES (condensed — detail in linked files)

- **Seven Depletion Clocks** — 7 simultaneous physical supply depletions with hard deadlines. Nearest: USDA 3/31, FAO 4/3, planting mid-Apr, China crude mid-late Apr. Each triggers NEW crisis on top of energy. → `FORGE/research/SEVEN_DEPLETION_CLOCKS.md`
- **Oil Shock Is Structural** — Infrastructure damage means prices can't normalize even with ceasefire. Best case 80-85% capacity by Q4 2026, full recovery 2027. Floor WTI $80-85. Dubai $166. No relief valve → Dec expiry strengthened. → `FORGE/research/iran-war/`
- **HY OAS Transmission Confirmed** — Crossed 320 RED (Mar 17). 2007 template: 320→500 in 2-4mo (May-Jul), 500+ = acceleration/forced selling. No Fed put (PCE 3.1%). CFA projects 1,093bps next recession.
- **Hamilton Framework** — NOPI=47, GDP drag -3.0 to -4.9pp, peak lag4 Q1'27. Credit peaks BEFORE equity (~3mo lead). $4/gal = behavioral breakpoint. Jun=1/3 damage, Dec=peak. Roll Jun→Dec. → `FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md`
- **Fed Stealth Liquidity** — T-Bills $195B→$352B in 12wk (exceeds COVID peak). Reserves $2.8T (4yr low), concentrated G-SIBs. Surface calm = intervention working, not health. 2019 repo parallel: breaks binary. → `FORGE/research/FED_TBILL_REPO_ANALYSIS.md`
- **Two Expiry Frameworks** — PC single-name puts (APO, ARES, ARCC): dateable catalysts, May/Jun/Jul expiry. Macro/index (HYG, KRE, IWM): Hamilton Dec expiry. BRENT owns Hamilton. BROCK owns PC clock.
- **Private Credit Cascade** — 6 funds gated in 5wk. JPM marking down collateral (Snider Stage 2). Defaults 4-5% true rate. Software wall $70B 2028. → BROCK domain

---

## THESIS FRAMEWORK

- **RED Team (Feb 14)** — 85% confidence (upgraded Mar 20). Falsification: exit 50% if claims <240K + CBRE >-5%; exit 100% if BTFP 2.0 / HY OAS <260bps. → `AGENTS/RED/`
- **UST Demand Hole** — Four-anchor stress (Japan+China+Korea+Gulf). Combined selling $40-72B/mo. Gulf recycling broken.
- **Hamilton** — see Core Discoveries above.

---

## SYSTEM ARCHITECTURE

- **Inbox siloed from spawn.** Separate spawn for inbox processing vs normal tasks.
- **Reply rule:** Only reply to signals if (a) new info, (b) error correction, (c) threshold trigger.
- **Inbox = folder.** Files in `inbox/`, move to `inbox/processed/`.
- **Root TSVs canonical.** workbook/ is archive.
- **Agent STATUS ≤250 lines.** Archive resolved to workbook.
- **HERMES 2x daily** (9AM + 5PM ET). Agents write OUTBOX.
- **Stale data:** Skip VX rows >5 trading days. Pull live before citing STATUS >24h.
- **Schema standard:** REGINALD TSV format. Mechanically triggerable vectors > vibes.
- **Poisoned refs:** Separate methodology from live data. Methodology = thresholds only, never current values.

---

## KEY CORRECTIONS

- OZK earnings: **April 16, 2026**
- NYCB → **FLG (Flagstar Financial)** Oct 2024
- CMA → **FITB (Fifth Third)** Feb 2, 2026
- PSEC PIK was **8.6%**, not 35%
- Always verify agent data against SEC filings before trading
