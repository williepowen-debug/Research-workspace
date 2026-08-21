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
10. **Fertilizer/food:** BRENT (gas/feedstock cost) → FERT (nitrogen + phosphate supply/price/policy; China policy = live vector) → CARL (food-CPI transmission) + HENRY; {OSPREY, FALCON} theater signals → FERT (Hormuz/Black-Sea supply shocks). *Potash → FERT at TRIAGE DEPTH (Will-ruled 2026-08-18; log + flag PROME, no deep-dive — full rule canonical in FERT's `CLAUDE.md` §POTASH). ⛔ This line's prior "Potash = UNOWNED, routes to PROME" was 3 days stale against that ruling — reconciled 2026-08-21 under the root-batch word; "potash is UNOWNED" is kill-on-sight fleet-wide.*

NEXUS synthesizes across all chains. MARCO feeds immigration/labor supply into LABOR + BRENT. **VIOLET tracks credit-to-vol transmission — when credit spreads widen and VIX hasn't caught up.** **TERRY converts thesis into trade construction: entry, structure, sizing, invalidation, roll/no-roll rules, and postmortems.**

## Agents

Grouped directory views live in `AGENTS/_INDEX.md`; the canonical topology map lives in `AGENTS/_NETWORK.md`. Canonical agent paths remain flat as `AGENTS/<NAME>/` to avoid breaking existing scripts, docs, and Claude Code workflows.

**Run model (all agents):** every agent is a Claude Code session — launch it from its own dir (`cd AGENTS/<NAME> && claude`), or PROME spawns it via teams-mode when orchestrating (mode-split rule → `PROME/ORCHESTRATION_PLAYBOOK.md`). Live vs Tier-2 vs dormant classification → `PROME/ROSTER.md` (single source of truth — dormant/retired agents do not launch unless Will revives). **Exceptions:** CREED = explicit-permission only; DAEDALUS = on-demand meta-agent (PROME/Will). *(The old per-agent "Spawn?" column — OpenClaw-era "Persistent (Telegram)" framing — was retired 2026-07-01; the spawnable-vs-persistent split no longer exists.)*

> **⚠️ The table below is a ROUTING subset, not the roster.** It lists the agents in the canonical transmission chains — **33 rows: 30 of the 32 live ACTIVE agents (all but PROME and WALTER, who route from root canon and their own specs) plus 3 non-ACTIVE chain members (CREED, OTTO, DAEDALUS)** *(count corrected 8/6, Will-directed review — this line said "~20 rows against 30" from authoring, never true; 31→32 at the 2026-08-16 FERT registration; 32→33 at the 2026-08-21 FLG row [build 8/20], Will-ruled root batch)* — so a name's absence here means "not on a named chain," never "not active." Roster membership and **responsibility class** are owned by **`PROME/ROSTER.md`**, which as of the **2026-08-05 Phase 1 taxonomy pass** splits the live roster into five descriptive classes: **ORGANIZING / SERVICE · REVIEW / QC · DOMAIN ACTIVE · PROVISIONAL ACTIVE · EVENT-DRIVEN SPECIALIST**. Read class there; **do not mirror per-agent classes into this table** — a duplicated high-churn field rots independently, which is the failure that pass exists to fix. Classes are **descriptive only** (no routing, boot-priority, grading or read-obligation effect), and neither `PROVISIONAL ACTIVE` nor `EVENT-DRIVEN SPECIALIST` is a demotion.

| Agent | Domain | Chain |
|-------|--------|-------|
| LABOR | Employment, claims | Credit |
| CARL | Consumer credit (housing asset-market → HOMER 7/12; CARL keeps consumer-transmission reads) | Credit |
| **HOMER** | **Housing — pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface** | **Housing → {CARL, REGINALD, HENRY}** |
| REGINALD | Regional banks — cohort + non-spun names (ZION/CFG/EGBN/BKU/SSB/AMTB/SBCF); **no longer owns the OZK or WAL single-name books** — both promoted out | Credit |
| **OZK** | **Bank OZK single-name specialist (RESG construction, classified-migration watch)** — promoted out of REGINALD 2026-04-24 | **Credit (→ REGINALD cohort, BROCK NDFI seam)** |
| **WAL** | **Western Alliance single-name specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3, FRAUD/litigation arc)** — promoted out of REGINALD 2026-07-25 | **Credit (→ REGINALD cohort, TERRY construction)** |
| **FLG** | **Flagstar Financial single-name specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB)** — the fleet's first GREENFIELD per-bank build, born 2026-08-20 (not a REGINALD promotion; cadence print-driven, Call Report ~QE+45d) | **Credit (REGINALD → FLG single-name depth; FLG → {REGINALD, LIQUID, TERRY})** |
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
| **FERT** | **Fertilizer supply/price/policy (nitrogen + phosphate; potash EXCLUDED-UNOWNED) — re-chartered EVENT-DRIVEN 2026-08-16** | **BRENT feedstock → FERT → {CARL, HENRY}; {OSPREY, FALCON} theater in** |
| **DAEDALUS** | **Fleet architect — design / structure / maturity / lifecycle** | **Meta / system** |

---

## First Message

On session start, read `PROME/BOOT.md` and follow its sequence.
Before `/clear` or `/new`, read `PROME/HANDOFF.md`.
Orchestration + protocols: `PROME/BOOT.md`, `PROME/CLOSEOUT.md`, `PROME/AUTONOMY.md`, `PROME/COMPLETION_SPEC.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md`

---

## Safety

- Don't exfiltrate private data. Ever.
- `trash` > `rm`
- **Internal actions** (read, organize, search): do freely
- **External actions** (emails, tweets, public posts): ask first
- **Trade proposals** → Will approves/rejects (binary). Never execute without approval. TERRY may propose trade structure; approval still required.
- **Agent check-in proposals** → when agents propose research or new tracking, route to Will for approval. Standard practice.
- **Autonomy/proposal rules:** `PROME/AUTONOMY.md`; task completion format: `PROME/COMPLETION_SPEC.md`. Historical Toscanini files live under `PROME/archive/TOSCANINI_2026-03/`.

---

## Core Principles

| Principle | Meaning |
|-----------|---------|
| **Files > Memory** | Write it down or lose it |
| **Fresh > Stale** | Clear context beats long context |
| **Read > Assume** | Read the file before editing. Always. |
| **Verify > Trust** | Check that it worked |
| **Simple > Clever** | Obvious solutions beat elegant complexity |

**Anti-pattern:** "I remember from earlier" — No you don't. Read the file.
