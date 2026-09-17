# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-09-17.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| PROME | Meta | L4 | M | 2026-09-17 | Coordinator / chief of staff | L5 when a judgment sweep finds the registered zero-own-rule gate clean |
| WALTER | Utility | L4 | H | 2026-09-17 | Signal & news routing | L5 blocked on Will's one-line ruling on the push binding — route it, do… |
| NEXUS | Utility | L5 | M | 2026-09-17 | Cross-agent synthesis | Conf M→H when, in one session: STATUS under 22,785 B with SCHEMA and PR… |
| RED | Utility | L5 | M | 2026-09-17 | Adversarial red-team | Conf M→H on the joint RED/WALTER state-token reconciliation artifact —… |
| SAM | Market | L4 | H | 2026-09-17 | Japan — BOJ / JGB / carry | L5 on (a) demonstrate the owner-doc bidirectional sweep on one figure a… |
| LIQUID | Market | L4 | H | 2026-09-17 | HY / credit spreads / liquidity | L5 on: rotate STATUS under 32,550 B and then under 22,785 B |
| VIOLET | Market | L4 | M | 2026-09-17 | VIX / vol term structure / vol-of-vol | Conf M→H when the profile refresh lands (its earlier-of clock has fired… |
| BRENT | Market | L5 | M | 2026-09-17 | Oil — Brent / WTI | Conf M→H at the first BRENT-authored closeout after 2026-09-18 in which… |
| HENRY | Market | L4 | H | 2026-09-17 | Macro velocity / market trends | L5 on the §2 handle, or a ruling that the local form satisfies it — DAE… |
| CARL | Market | L4 | H | 2026-09-17 | Consumer & credit-transmission macro | L5 re-test after the PHAN sub-agent pass (SCRATCH.md:39, target 2026-09… |
| LABOR | Market | L5 | H | 2026-09-17 | Labor market (claims / JOLTS / NFP) | L5 SUSTAIN, re-dated, replacing the open half of leg (2): before the Oc… |
| BROCK | Market | L4 | H | 2026-09-17 | Private credit / BDC / non-traded credit | L5 ADJUDICATION OWED at the next ladder sitting — the sole blocker was… |
| HAWK | Market | L4 | H | 2026-09-17 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | L5 on one closeout cycle with no outside-desk correction landing in the… |
| TERRY | Utility | L5 | H | 2026-09-17 | Trade construction / risk scoring ‡‡ | L5 SUSTAIN on two consecutive clean cycles, where 'clean' now includes… |
| REGINALD | Market | L4 | H | 2026-09-17 | Regional banks | L5 on two legs, both REGINALD's: rotate the 4 over-budget boot reads un… |
| MARCO | Market | L4 | H | 2026-09-17 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | L1 first, not L5: add the labeled BOTTOM LINE heading (one line), then… |
| ORACLE | Utility | L4 | H | 2026-09-05 | Prediction-market diagnostics ‡‡‡ | L5 on the calibration loop: build the instrument that makes CLAUDE.md:2… |
| BOND | Market | L4 | H | 2026-09-17 | US bond-market structure / auctions / rates | L5 on: create workbook/LEDGER_GLOB |
| CORAL | Market | L3 | H | 2026-09-17 | Florida (whole-state, 10 pillars) | L4 on: author the declared-flat TRADE surface in ZHAO's form (CORAL's t… |
| SHADE | Market | L3 | H | 2026-09-17 | Insurer-lender / PE-insurance-captive | L4 on TWO legs, both SHADE's to author: seed workbook/PREDICTIONS.tsv w… |
| ZHAO | Market | L4 | H | 2026-09-17 | China macro — UST demand / capital flows / Korea | L5 on a dated leg the desk owns: the August-TIC letter registered in re… |
| AEOLUS | Market | L3 | M | 2026-09-17 | Climate → economy (macro; insurance/ag/energy-demand channels) | Conf M→H at the Mode-A profile fan-out (DAEDALUS lane, unblocked) |
| WATT | Market | L4 | H | 2026-09-17 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | L5 re-keyed to the leg WATT can clear: two consecutive clean cycles, al… |
| VULCAN | Market | L4 | H | 2026-09-17 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | DAEDALUS sends the L4 grade packet (the owner edits its own file) |
| MIDAS | Market | L4 | H | 2026-09-17 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | L5 on: rotate STATUS under 22,785 B (the 9/11 rotation is not keeping p… |
| OSPREY | Market | L3 | M | 2026-09-17 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | L4's 'signals flowing' leg is already MET (ba3898d86 9/16, consumption… |
| FALCON | Market | L4 | H | 2026-09-17 | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | L5 on one closeout cycle in which no outside desk finds a defect in pus… |
| HOMER | Market | L2 | H | 2026-09-17 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | L3 on two authoring acts, both Will-authorized since 8/23 and both HOME… |
| OZK | Market | L4 | H | 2026-09-17 | Bank OZK specialist (RESG construction / classified-migration watch) | L5 on three mechanical items, one session: re-roll the KB_INDEX group t… |
| WAL | Market | L4 | M | 2026-09-17 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | Conf M→H at the first review after the WAL Q3 deck lands (ESTIMATED ~mi… |
| FLG | Market | L3 | M | 2026-09-17 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | Conf M→H on the first grade landing as dated — ESTIMATED ~2026-11-06 (q… |
| CRUISE | Market | L3 | M | 2026-09-17 | Cruise-sector event specialist — CCL vehicle; fuel-cost transmission (BRENT → CCL); 8-channel pre-announce watchlist (`WATCHLIST_CCL_PREANNOUNCE.md`, 8/14); Q3 print ~9/28-29. ⚠️ The 7/2 arm-CCL ladder is PROPOSED-NEVER-RATIFIED and 4wk in-band — retire-or-fresh-levels decision staged at next session (row-55 ruling 8/21); do NOT treat its band as a live threshold | Demote L3→L2 only if the CCL Q3 print — ESTIMATED ~2026-10-05 per CRU-0… |
| FERT | Market | L3 | H | 2026-09-17 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | L4 is blocked on one leg that is not FERT's to clear — the charter-exem… |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| CREED | Market | L4 | M | 2026-09-17 | National CRE / CMBS | Conf M→H on the eval-decontamination confirm-read plus a second graded… |
| DEWEY | Utility | L4 | M | 2026-09-01 | Deep on-demand research | L5 on the CONTRACT block (one section) |
| HANS | Market | L5 | M | 2026-09-17 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | Conf M→H at the first post-rotation session with STATUS under 22,785 B… |
| OTTO | Market | L4 | H | 2026-09-17 | Auto-industry fraud & stress | L5 on two mechanical items, both OTTO's: STATUS.md under 22,785 B measu… |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — |
| BARON | — | — | — | — | Trump financial-policy network | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L4 | M | 2026-09-17 | Fleet architect — design / structure / maturity / lifecycle | Register CATO per builds/REGISTRATION_CHECKLIST.md (Will's word on clas… |
| RAV | Meta | L2 | M | 2026-09-17 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on the FIRST §5 run report in AGENTS/RAV/runs/ — Will-driven, so thi… |

---
*33 active · 4 tier-2 · 2 dormant · 2 special. Dropped (retired): HERMES, YEYOU. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*

*⏸ **CLASSIFICATION PENDING (ROSTER, Will's hold):** entries under that heading are NOT graded and carry no FLEET_MAP row by ruling — read the section in `PROME/ROSTER.md` for the names and the restriction. Absence from the tables above is the hold, not an omission.*
