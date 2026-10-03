# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-10-03.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

**WF:** configured phrase-list entries at render time, not hits or routing health. `0` = explicit empty list; `—` = no list; `n/a` = owner-declared non-query desk; `UNKNOWN` = source unavailable/unsupported. Regenerate after lane edits; the existing directory-age guard watches ROSTER/FLEET_MAP only.
WF source: `/home/willi/Research-Intake/scripts/newsweep_config.py` · SHA256 `1d5a88fb5e3f8cfa1297764cce79b19a3f711180a35443894349960983cba0b7`.

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| PROME | Meta | L4 | M | 2026-10-01 | Coordinator / chief of staff | L5 'zero own-rule-unexecuted': PROME runs the spine audit (DOCKET L503,… | — |
| WALTER | Utility | L4 | H | 2026-10-01 | Signal & news routing | L5 at WALTER's next session: WALTER aligns CLAUDE.md:149 with BOARD_CON… | — |
| NEXUS | Utility | L5 | M | 2026-10-01 | Cross-agent synthesis | Conf M→H at the NEXUS closeout that lands an AUTHORITY & SAFETY block i… | — |
| RED | Utility | L5 | M | 2026-10-01 | Adversarial red-team | Conf M→H when RED writes its state-token vocabulary in its own tree AND… | — |
| SAM | Market | L4 | H | 2026-10-01 | Japan — BOJ / JGB / carry | L5 at the first SAM closeout after SAM-42 is graded (resolves by 2026-1… | 12 |
| LIQUID | Market | L4 | H | 2026-10-01 | HY / credit spreads / liquidity | L5 at LIQUID's next full session: THESIS.md re-cut off v2.0 with an in-… | 7 |
| VIOLET | Market | L4 | M | 2026-10-01 | VIX / vol term structure / vol-of-vol | L5 at the first VIOLET closeout where workbook/KB.tsv carries the two-c… | — |
| BRENT | Market | L5 | M | 2026-10-01 | Oil — Brent / WTI | Conf M→H at the first BRENT closeout where boot.py BOOT_SEQUENCE runs a… | 15 |
| HENRY | Market | L4 | H | 2026-10-01 | Macro velocity / market trends | L5 at the HENRY closeout that adds the §2 handle to STATUS (or after a… | 6 |
| CARL | Market | L4 | H | 2026-10-01 | Consumer & credit-transmission macro | L5 when ledger_staleness.py CARL reports 0 stale on its sub_agents ledg… | 4 |
| LABOR | Market | L5 | H | 2026-10-01 | Labor market (claims / JOLTS / NFP) | SUSTAIN at the 10/8 claims-card grade closeout (fires once the 10/8 pri… | 12 |
| BROCK | Market | L4 | H | 2026-10-01 | Private credit / BDC / non-traded credit | L5 'current' at BROCK's next session: grade BRK-02, fix STATUS.md:91 ag… | 6 |
| HAWK | Market | L4 | H | 2026-10-01 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | L5 on one closeout cycle with no outside-desk correction landing, start… | 8 |
| TERRY | Utility | L5 | H | 2026-10-01 | Trade construction / risk scoring ‡‡ | L5 SUSTAIN at the next TERRY closeout with ledger_sweep.py section I =… | 7 |
| REGINALD | Market | L4 | H | 2026-10-01 | Regional banks | L5 adjudication by DAEDALUS at PR#8 (2026-10-15) on three against-legs… | 6 |
| MARCO | Market | L4 | M | 2026-10-01 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | At MARCO's next session: a current-judgment summary section (## BOTTOM… | 5 |
| ORACLE | Utility | L4 | H | 2026-10-01 | Prediction-market diagnostics ‡‡‡ | L5 on F-1: a per-resolved-market Brier ledger (slug · resolution · outc… | — |
| BOND | Market | L4 | H | 2026-10-01 | US bond-market structure / auctions / rates | L5 at BOND's next closeout: create workbook/LEDGER_GLOB and add two-clo… | 7 |
| CORAL | Market | L4 | M | 2026-10-01 | Florida (whole-state, 10 pillars) | L5 at the next CORAL session: read_cap_check --agent CORAL rotation_due… | 16 |
| SHADE | Market | L3 | H | 2026-10-01 | Insurer-lender / PE-insurance-captive | L4 at SHADE's self-dated 2026-10-08 session (needs a PROME spawn): a DE… | 10 |
| ZHAO | Market | L4 | H | 2026-10-01 | China macro — UST demand / capital flows / Korea | L5 at the first ZHAO session after the August TIC print (Fri 2026-10-16 | — |
| AEOLUS | Market | L3 | M | 2026-10-01 | Climate → economy (macro; insurance/ag/energy-demand channels) | L4 at the next WEEKLY session (~10/05): TRADE.md rows 1/3 and THESIS.md… | — |
| WATT | Market | L4 | H | 2026-10-01 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | L5 on two consecutive clean WEEKLY cycles, the first a boot by 10/09 (W… | 21 |
| VULCAN | Market | L4 | H | 2026-10-01 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | L5 on two consecutive WEEKLY cycles that take every registered slot (fi… | 11 |
| MIDAS | Market | L4 | H | 2026-10-01 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | L5 on a second consecutive clean WEEKLY cycle after 10/01 (≤10/08) with… | 11 |
| OSPREY | Market | L3 | H | 2026-10-01 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | L4 at OSPREY's next session: a DECLARED-FLAT TRADE.md whose explicit un… | — |
| FALCON | Market | L4 | H | 2026-10-01 | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | L5 on one closeout cycle (from the 10/08 7-day review) with no outside… | 10 |
| HOMER | Market | L2 | H | 2026-10-01 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | L3 on building 3c into thesis/THESIS.md with CARL's three labels, HOMER… | — |
| YURI | Market | L2 | M | 2026-10-01 | **Russia — ACTOR-KEYED: what the Russian state DECIDES, across all channels, as one actor** (mobilisation, asset seizure, force posture, export instruments). ⛔ **NOT Russia macro** — the name follows the fleet's human-first-name convention for geography desks and reads narrower than the charter; the charter scope is the authority, not the name. | Conf M→H at the next YURI session (needs a PROME spawn | — |
| OZK | Market | L4 | H | 2026-10-01 | Bank OZK specialist (RESG construction / classified-migration watch) | L5 on one edit in OZK's tree: add 218-219 to MEMO_ITEM_3 (4→6), set the… | 2 |
| WAL | Market | L4 | M | 2026-10-01 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | Conf M→H at the first review after the WAL Q3 release has published (da… | — |
| FLG | Market | L3 | M | 2026-10-01 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | Conf M→H when FLG-02/03 are graded off the Q3 10-Q (fires only once it… | 8 |
| CRUISE | Market | L3 | H | 2026-10-01 | Cruise-sector event specialist — CCL vehicle; fuel-cost transmission (BRENT → CCL); 8-channel pre-announce watchlist (`WATCHLIST_CCL_PREANNOUNCE.md`, 8/14); Q3 print ~9/28-29. ⚠️ The 7/2 arm-CCL ladder is PROPOSED-NEVER-RATIFIED and 4wk in-band — retire-or-fresh-levels decision staged at next session (row-55 ruling 8/21); do NOT treat its band as a live threshold | L4 at the CRUISE session that re-states TRADE.md's two WATCH rows as DE… | — |
| FERT | Market | L4 | M | 2026-10-01 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | L5 on the FERT-11 Pink Sheet grade (10/02) and the next two DTN G5 prin… | 10 |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| CREED | Market | L4 | H | 2026-10-01 | National CRE / CMBS | L5 at the next tier-2 CREED spawn whose closeout carries a BOTTOM LINE… | 36 |
| DEWEY | Utility | L4 | M | 2026-10-01 | Deep on-demand research | L5 on a labeled CONTRACT block (PRODUCES / CONSUMED BY / PROOF) in CLAU… | n/a |
| HANS | Market | L5 | H | 2026-10-01 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | SUSTAIN at the first HANS closeout after a large-EU-bank Q3 result prin… | 10 |
| OTTO | Market | L4 | H | 2026-10-01 | Auto-industry fraud & stress | L5 at the OTTO closeout that lands the §2 5-pt | 9 |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — | — |
| BARON | — | — | — | — | Trump financial-policy network | — | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L4 | M | 2026-10-01 | Fleet architect — design / structure / maturity / lifecycle | Finish owed outputs and owner-dependent dispositions on STATUS dated bo… | n/a |
| RAV | Meta | L2 | M | 2026-10-01 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on the first §5 run report in AGENTS/RAV/runs/ | — |
| CATO | — | — | — | — | Will's manual Codex/Astra adviser + independent reviewer | UNGRADED BY RULING (WQ-255, 2026-09-26): manual-only — no launch, no routing, no ladder row | — |

---
*34 active · 4 tier-2 · 2 dormant · 3 special. Dropped (retired): HERMES, YEYOU. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*

*⏸ **CLASSIFICATION PENDING (ROSTER, Will's hold):** entries under that heading are NOT graded and carry no FLEET_MAP row by ruling — read the section in `PROME/ROSTER.md` for the names and the restriction. Absence from the tables above is the hold, not an omission.*
