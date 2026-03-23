# MEMORY — Key Insights & Lessons

**Last Updated:** 2026-03-23 14:15 UTC

**Positions → `PROME/POSITIONS.md`** | **Agent roster → `AGENTS_DIRECTORY.md`** | **Background → `WILL/BACKGROUND.md`**

---

## CORE DISCOVERIES (condensed — detail in linked files)

- **Seven Depletion Clocks** — 7 simultaneous physical supply depletions with hard deadlines. Nearest: USDA 3/31, FAO 4/3, planting mid-Apr, China crude mid-late Apr. Each triggers NEW crisis on top of energy. → `FORGE/research/SEVEN_DEPLETION_CLOCKS.md`
- **Oil Shock Is Structural** — Infrastructure damage means prices can't normalize even with ceasefire. Best case 80-85% capacity by Q4 2026, full recovery 2027. Floor WTI ~$80-85. No relief valve → Dec expiry strengthened. → `FORGE/research/iran-war/`
- **HY OAS Transmission Confirmed** — Crossed 320 RED (Mar 17). 2007 template: 320→500 in 2-4mo (May-Jul), 500+ = acceleration/forced selling. No Fed put (PCE 3.1%). CFA projects 1,093bps next recession.
- **Hamilton Framework** — NOPI=47, GDP drag -3.0 to -4.9pp, peak lag4 Q1'27. Credit peaks BEFORE equity (~3mo lead). $4/gal = behavioral breakpoint. Jun=1/3 damage, Dec=peak. Roll Jun→Dec. → `FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md`
- **Fed Stealth Liquidity** — T-Bills $195B→$352B in 12wk (exceeds COVID peak). Reserves $2.8T (4yr low), concentrated G-SIBs. Surface calm = intervention working, not health. 2019 repo parallel: breaks binary. → `FORGE/research/FED_TBILL_REPO_ANALYSIS.md`
- **Private Credit Cascade** — Multiple funds gated, accelerating. JPM marking down collateral (Snider Stage 2). Defaults 4-5% true rate. Software wall $70B 2028. BCRED first monthly loss (reflexivity active). DBRS: 16% of rated universe CCC-C, 3.4yr avg time to default, 2021-22 vintages cracking NOW. → BROCK domain
- **CARL Path C Activating (Mar 23)** — "Help with mortgage" Google Trends at ALL-TIME HIGH (surpasses GFC). Lennar margins 15.2% (lowest since 2010). Housing cracking BEFORE employment — thesis evolution from K-shape model. Employment no longer sole detonator; housing + employment running parallel stress paths. Convergence 43/50.
- **Ghalibaf Financial Warfare (Mar 23)** — Iran Parliament Speaker declared UST buyers "legitimate military targets." Not fringe — post-Khamenei, most powerful institutional voice. Gives Gulf SWFs political cover to reduce UST exposure. One-way ratchet (stigma makes re-entry harder). ZHAO revised demand hole $70-135B/mo (from $70-130B).
- **BOJ Timing Revision (Mar 23)** — Shunto 5.26% confirmed (3rd year >5%), but oil chaos delays hike from April to likely May 1. FY-end flows (GPIF rebalancing, life insurer repatriation) are MECHANICAL and happening NOW regardless. Full carry unwind needs actual hike.

---

## THESIS FRAMEWORK

- **RED Team (Feb 14)** — 85% confidence (upgraded Mar 20). Falsification: exit 50% if claims <240K + CBRE >-5%; exit 100% if BTFP 2.0 / HY OAS <260bps. → `AGENTS/RED/`
- **UST Demand Hole** — Four-anchor stress (Japan+China+Korea+Gulf). Combined selling $70-135B/mo (revised up Mar 23 — Ghalibaf ratchet). Gulf recycling broken. Note: CNY 7.30 call missed (actual 6.91 Mar 20 — yuan strengthened). Structural selling thesis intact but magnitude/timing uncertain.

---

## SYSTEM ARCHITECTURE

- **Inbox siloed from spawn.** Separate spawn for inbox processing vs normal tasks.
- **Reply rule:** Only reply to signals if (a) new info, (b) error correction, (c) threshold trigger.
- **Inbox = flat folder at agent root.** `inbox/` and `outbox/` (migrated from `mail/inbox` Mar 23). Processed → `inbox/processed/`, delivered → `outbox/delivered/`.
- **Root TSVs canonical.** workbook/ is archive.
- **Agent STATUS ≤250 lines.** Archive resolved to workbook.
- **HERMES 2x daily** (9AM + 5PM ET). Agents write OUTBOX.
- **Stale data:** Skip VX rows >5 trading days. Pull live before citing STATUS >24h.
- **Schema standard:** REGINALD TSV format. Mechanically triggerable vectors > vibes.
- **Poisoned refs:** Separate methodology from live data. Methodology = thresholds only, never current values.
