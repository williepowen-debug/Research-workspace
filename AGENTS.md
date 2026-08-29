# AGENTS.md

Detect stress transmission early enough to position ahead of consensus.

**Transmission Chains:**
1. **Credit:** LABOR → CARL → REGINALD → repricing (CREED national CRE/CMBS + CORAL geo convergence + HENRY velocity + LIQUID amplification)
2. **Private credit cascade:** BROCK → SHADE (insurance) → LIQUID (funding)
3. **Energy shock / war:** {OSPREY (Russia/Ukraine), FALCON (Iran/Gulf)} → HAWK (cross-war synthesis, no double-count) → BRENT → HENRY (demand destruction); acute theater signals → BRENT direct, HAWK cc'd
4. **Japan:** SAM — independent trigger via carry unwind → LIQUID
5. **Volatility:** VIOLET — credit-to-vol lag detection → HENRY, LIQUID, RED
6. **Power:** AEOLUS (weather detection) → WATT (grid stress → power price) → HENRY (AI-capex FCF) + CARL (retail pass-through)
7. **AI-capex:** VULCAN (concentration mechanism / memory cycle / compute-demand / Taiwan chokepoint) → VIOLET (concentration-unwind vol) + HENRY (FCF) + WATT (power demand)
8. **Metals:** {BOND (gold↔real-rates), ZHAO (copper↔China)} ↔ MIDAS → LIQUID (safe-haven) + HENRY (growth tell); HAWK → MIDAS (PGM supply)
9. **Housing:** HOMER (asset market: pipeline, GSE+CMBS multifamily, builders, HPI) → CARL (consumer transmission) + REGINALD (Path C bank collateral) + HENRY (wealth effect)
10. **Fertilizer/food:** BRENT (gas/feedstock cost) → FERT (nitrogen + phosphate supply/price/policy; China policy = live vector) → CARL (food-CPI transmission) + HENRY; {OSPREY, FALCON} theater signals → FERT (Hormuz/Black-Sea supply shocks). *Potash → FERT at TRIAGE DEPTH (log + flag PROME, no deep-dive — full rule canonical in FERT's `CLAUDE.md` §POTASH). ⛔ "potash is UNOWNED" is kill-on-sight fleet-wide.*

NEXUS synthesizes across all chains. MARCO feeds immigration/labor supply into LABOR + BRENT. **VIOLET tracks credit-to-vol transmission — when credit spreads widen and VIX hasn't caught up.** **TERRY converts thesis into trade construction: entry, structure, sizing, invalidation, roll/no-roll rules, and postmortems.**

## Agents

Grouped directory views live in `AGENTS/_INDEX.md`; the canonical topology map lives in `AGENTS/_NETWORK.md`. Canonical agent paths remain flat as `AGENTS/<NAME>/` to avoid breaking existing scripts, docs, and Claude Code workflows.

**Run model (all agents):** every agent is a Claude Code session — launch it from its own dir (`cd AGENTS/<NAME> && claude`), or PROME spawns it via teams-mode when orchestrating (mode-split rule → `PROME/ORCHESTRATION_PLAYBOOK.md`). Live vs Tier-2 vs dormant classification → `PROME/ROSTER.md` (single source of truth — dormant/retired agents do not launch unless Will revives). **Exceptions:** CREED = explicit-permission only; DAEDALUS = on-demand meta-agent (PROME/Will). *(The old per-agent "Spawn?" column — OpenClaw-era "Persistent (Telegram)" framing — was retired 2026-07-01; the spawnable-vs-persistent split no longer exists.)*

> **⚠️ The table below is a ROUTING subset, not the roster.** It lists the agents in the canonical transmission chains — **34 rows: 31 of the 33 live ACTIVE agents (all but PROME and WALTER, who route from root canon and their own specs) plus 3 non-ACTIVE chain members (CREED, OTTO, DAEDALUS)** — so a name's absence here means "not on a named chain," never "not active." Roster membership and **responsibility class** are owned by **`PROME/ROSTER.md`** (five descriptive classes since the 2026-08-05 Phase 1 pass). Read class there; **do not mirror per-agent classes into this table** — a duplicated high-churn field rots independently. Classes are **descriptive only** (no routing, boot-priority, grading or read-obligation effect). *(Count history + potash line history → `docs/CANON_PROVENANCE.md` `key: agents-routing-table`.)*

| Agent | Domain | Chain |
|-------|--------|-------|
| LABOR | Employment, claims | Credit |
| CARL | Consumer credit (housing asset-market → HOMER 7/12; CARL keeps consumer-transmission reads) | Credit |
| **HOMER** | **Housing — pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface** | **Housing → {CARL, REGINALD, HENRY}** |
| REGINALD | Regional banks — cohort + non-spun names (ZION/CFG/EGBN/BKU/SSB/AMTB/SBCF); **no longer owns the OZK or WAL single-name books** — both promoted out | Credit |
| **OZK** | **Bank OZK single-name specialist (RESG construction, classified-migration watch)** — promoted out of REGINALD 2026-04-24 | **Credit (→ REGINALD cohort, BROCK NDFI seam)** |
| **WAL** | **Western Alliance single-name specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3, FRAUD/litigation arc)** — promoted out of REGINALD 2026-07-25 | **Credit (→ REGINALD cohort, TERRY construction)** |
| **FLG** | **Flagstar Financial single-name specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB)** — the fleet's first GREENFIELD per-bank build, born 2026-08-20 (not a REGINALD promotion; cadence print-driven, Call Report ~QE+45d) | **Credit (REGINALD → FLG single-name depth; FLG → {REGINALD, LIQUID, TERRY})** |
| **CRUISE** | **Cruise-sector event specialist — CCL vehicle; fuel-cost transmission; 8-channel pre-announce watchlist; Q3 print ~9/28-29** — re-classed ACTIVE/EVENT-DRIVEN 2026-08-21 (was personal-interest/archive; label measured false). ⚠️ Its 7/2 arm-CCL ladder is PROPOSED-NEVER-RATIFIED — not a live threshold | **Energy → consumer discretionary (BRENT fuel-cost → CCL); event-driven** |
| CORAL | Florida real estate, insurance, FL banks, migration/tourism | Credit (geo convergence) |
| CREED | National CRE / CMBS + public REIT equity tape | Credit (CRE→bank bridge) |
| HENRY | Market structure, econ data | Credit (velocity) |
| LIQUID | Funding, Treasury, spreads | All (amplification) |
| BOND | US bond market structure, auctions, issuance, CDX/cash | Credit + funding bridge |
| BROCK | BDC, private credit, CLOs | PC cascade |
| SHADE | PE-insurance-captive | PC cascade |
| SAM | Japan, BOJ, carry trade | Japan |
| HAWK | Geopolitical synthesis (cross-war) + dormant book (Taiwan, Venezuela, trade, chokepoints) | Energy (synthesis hub) |
| **OSPREY** | **Russia/Ukraine war — energy strikes, crude-vs-products channel, shadow-fleet kinetic** | **Energy (theater → HAWK/BRENT)** |
| **FALCON** | **US/Israel/Iran-Gulf war — scenario ladder, Hormuz, Bab-al-Mandab, Baghdad watch** | **Energy (theater → HAWK/BRENT)** |
| BRENT | Oil, energy markets | Energy |
| RED | Adversarial analysis | All |
| MARCO | Migration, labor supply | Credit + Energy |
| ZHAO | China, capital flows | Japan + PC |
| OTTO | Auto, consumer DQ | Credit (→ CARL) |
| NEXUS | Cross-agent synthesis | All |
| ORACLE | Prediction markets | Utility |
| TERRY | Trade construction, chart/tape analysis, execution rails | Utility / trading desk |
| **VIOLET** | **VIX, vol term structure** | **Credit → Vol** |
| **AEOLUS** | **Climate → economy (insurance, ag/food, energy demand)** | **Climate → {BRENT, CORAL, MARCO}** |
| **WATT** | **Power/grid (PJM stress → wholesale price → data-center/industrial cost)** | **AEOLUS C3 → WATT → {HENRY, CARL}** |
| **VULCAN** | **AI-capex / semiconductor / memory (systemic: concentration, memory cycle, power demand, Taiwan chokepoint)** | **VULCAN → {VIOLET, HENRY, WATT}** |
| **MIDAS** | **Metals (monetary: gold/silver debasement/real-rates; industrial: copper/PGM growth/China/supply)** | **{BOND, ZHAO} ↔ MIDAS → {LIQUID, HENRY}** |
| **FERT** | **Fertilizer supply/price/policy (nitrogen + phosphate; potash TRIAGE-ONLY — rule in FERT `CLAUDE.md` §POTASH) — re-chartered EVENT-DRIVEN 2026-08-16** | **BRENT feedstock → FERT → {CARL, HENRY}; {OSPREY, FALCON} theater in** |
| **DAEDALUS** | **Fleet architect — design / structure / maturity / lifecycle** | **Meta / system** |

---

## Pointers (rules live in root `CLAUDE.md`, auto-injected — not restated here)

- PROME boot/closeout: `PROME/BOOT.md` · `PROME/CLOSEOUT.md` · `PROME/HANDOFF.md`. Autonomy tiers + proposal rules: `PROME/AUTONOMY.md`; task-completion format: `PROME/COMPLETION_SPEC.md`; orchestration: `PROME/ORCHESTRATION_PLAYBOOK.md` / `PROME/ORCHESTRAL_LAYER_DESIGN.md`.
- Trade proposals → Will approves (binary); TERRY proposes structure, never executes. Agent research/tracking proposals → Will. External sends → ask first.
- **Gate C Kernel Git boundary:** root `CLAUDE.md` Git Protocol carve-out ④ is canonical; inactive until a separate bounded Gate C activation ruling — planning or installation alone authorizes nothing.
- Historical Toscanini files: `PROME/archive/TOSCANINI_2026-03/`.
