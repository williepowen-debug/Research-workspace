# MEMORY — Key Insights & Lessons

**Last Updated:** 2026-03-25 04:45 UTC

**Positions → `PROME/POSITIONS.md`** | **Agent roster → `AGENTS_DIRECTORY.md`** | **Background → `WILL/BACKGROUND.md`**

---

## CORE DISCOVERIES (condensed — detail in linked files)

- **Seven Depletion Clocks** — 7 simultaneous physical supply depletions with hard deadlines. Nearest: USDA 3/31, FAO 4/3, planting mid-Apr, China crude mid-late Apr. Each triggers NEW crisis on top of energy. → `FORGE/research/SEVEN_DEPLETION_CLOCKS.md`
- **Oil Shock Is Structural** — Infrastructure damage means prices can't normalize even with ceasefire. Best case 80-85% capacity by Q4 2026, full recovery 2027. Floor WTI ~$80-85. No relief valve → Dec expiry strengthened. → `FORGE/research/iran-war/`
- **HY OAS Transmission Confirmed** — Crossed 320 RED (Mar 17). 2007 template: 320→500 in 2-4mo (May-Jul), 500+ = acceleration/forced selling. No Fed put (PCE 3.1%). CFA projects 1,093bps next recession.
- **Hamilton Framework** — NOPI=47, GDP drag -3.0 to -4.9pp, peak lag4 Q1'27. Credit peaks BEFORE equity (~3mo lead). $4/gal = behavioral breakpoint. Jun=1/3 damage, Dec=peak. Roll Jun→Dec. → `FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md`
- **Fed Stealth Liquidity** — T-Bills $195B→$352B in 12wk (exceeds COVID peak). Reserves $2.8T (4yr low), concentrated G-SIBs. Surface calm = intervention working, not health. 2019 repo parallel: breaks binary. → `FORGE/research/FED_TBILL_REPO_ANALYSIS.md`
- **Private Credit Cascade** — Multiple funds gated, accelerating. JPM marking down collateral (Snider Stage 2). Defaults 4-5% true rate. Software wall $70B 2028. BCRED first monthly loss (reflexivity active). DBRS: 16% of rated universe CCC-C, 3.4yr avg time to default, 2021-22 vintages cracking NOW. → BROCK domain
- **PC Contagion Mechanics Mapped (Mar 25)** — Three-source confirmed (Gemini+Claude+Perplexity). Six-stage contagion: gate → cash substitution → financing tighten → honest marks → CLO spillover → bank impairment. Currently Stage 2. Key corrections: CLO OC failure ≠ forced selling (needs EOD + AAA vote, high bar). Bank exposure $95B committed (manageable, ~2bps CET1). THE tripwire = fire-sale at 80-85¢ (not Blue Owl's 99.7¢). 2007 analog: 4-5 months gate→bank writedown = Q2-Q3 2026. Software = stress vector (10-13% CLO, 17-35% BDC, 37 managers holding same 15 distressed credits). Goldman: $45-70B retail outflows projected. PE-controlled insurers (APO/Athene, BX/Evermore, KKR/GA) = dual exposure risk. → `AGENTS/BROCK/research/PC_CONTAGION_MECHANICS.md`
- **CARL Path C Activating (Mar 23)** — "Help with mortgage" Google Trends at ALL-TIME HIGH (surpasses GFC). Lennar margins 15.2% (lowest since 2010). Housing cracking BEFORE employment — thesis evolution from K-shape model. Employment no longer sole detonator; housing + employment running parallel stress paths. Convergence 43/50.
- **Ghalibaf Financial Warfare (Mar 23)** — Iran Parliament Speaker declared UST buyers "legitimate military targets." Not fringe — post-Khamenei, most powerful institutional voice. Gives Gulf SWFs political cover to reduce UST exposure. One-way ratchet (stigma makes re-entry harder). ZHAO revised demand hole $70-135B/mo (from $70-130B).
- **BOJ Timing Revision (Mar 23)** — Shunto 5.26% confirmed (3rd year >5%), but oil chaos delays hike from April to likely May 1. FY-end flows (GPIF rebalancing, life insurer repatriation) are MECHANICAL and happening NOW regardless. Full carry unwind needs actual hike. **Ueda language shift (Mar 23):** can hike even into weak growth — April NOT dead.
- **Japan Structural UST Demand Withdrawal (Mar 25)** — Three-source confirmed (Gemini+Perplexity+Claude). Life insurers driving: hedge ratio collapsed 60%→45.7% (lowest since 2011), hedged UST return now **-0.34%** vs JGB 2.27%. 7/10 major insurers announced reductions. $50-120B annual swing from buyer to neutral/seller, concentrated in long-duration. NOT a March 31 event — a multi-year regime change. Feb 2026 already saw ¥3.42T net sales (largest since Oct 2024). Most FY-end flow already behind us by Mar 25. Primary channel is FX hedges/funding, not outright Treasury dumping. **FXY implication:** repatriation alone doesn't reliably strengthen yen (Mar 2025 counter-example). BOJ hike is the real catalyst, not calendar flows. Oil shock currently suppressing yen move. → `AGENTS/SAM/research/JAPAN_FYEND_REPATRIATION.md`
- **WAL Fast-Transmission Thesis (Mar 25)** — WAL losses bypass delinquency pipeline → direct to P&L. SF district has LOWEST 30-89 day pipeline (0.26%) but HIGHEST NCO (1.13%). Standard leading indicators break for WAL. Three independent vectors: Hidden CRE (MI3 24.2% growing), Jefferies double-pledging (unconfirmed chain), SSFA $1.1B capital arbitrage. KB: 61 rows, 10 groups. EV $57.10 vs $69.70 (18% overvalued). Short interest 3.54% = NOT consensus = edge.
- **Two-Pass KB Method Works** — Extraction pass (read all sources → staging list in SCRATCH) then formatting pass (clean context → TSV). Produced cleaner output than single-pass for OZK. Use this method for future KB builds.
- **WAL vs OZK: Complementary, Not Symmetric** — OZK = reservoir (gradual, maturity wall, predictable pipeline). WAL = fast-transmission (episodic, sudden, unpredictable). Different put expiry logic. OZK crowded (13.81% SI), WAL uncrowded (3.54%). Paired trade covers both failure modes.

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
- **Two-pass KB seeding works.** Pass 1 = extract facts to staging list (SCRATCH). Pass 2 = fresh context, convert to TSV. Separation prevents quality drift. Used for WAL (61 rows in one night).
- **WAL = fast-transmission, OZK = reservoir.** Different loss patterns → different scenario structures → different put expiry logic. WAL losses bypass pipeline (SF NCO highest, pipeline lowest). OZK losses accumulate behind interest reserves.
- **Short interest contrast matters.** OZK 13.81% (crowded, squeeze risk). WAL 3.54% (not consensus, repricing edge). Low SI = you're ahead of the market, but less institutional validation.
- **Domain audits via subagent spawn = high value.** Cold-boot agent reading the full domain catches staleness, orphan files, evidence gaps that the daily operator misses. Run periodically.
