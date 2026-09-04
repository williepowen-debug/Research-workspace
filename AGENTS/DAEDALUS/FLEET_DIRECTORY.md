# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-09-03.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| PROME | Meta | L5 | M | 2026-09-01 | Coordinator / chief of staff | L5 CONFIRM at judgment-tail sweep #2 ~9/6 (full 21d window, ZERO new un… |
| WALTER | Utility | L4 | H | 2026-09-01 | Signal & news routing | L5 on: (a) Will's word on the push binding · (c) re-key the 12(f) handl… |
| NEXUS | Utility | L5 | M | 2026-09-03 | Cross-agent synthesis | Conf M→H when, in one session: CONFIRMED.md C-36 row |
| RED | Utility | L5 | M | 2026-09-03 | Adversarial red-team | Conf M→H on the first post-9/12 commit where `grep -c CARRIED workbook/… |
| SAM | Market | L4 | H | 2026-09-01 | Japan — BOJ / JGB / carry | L5 on (a)+(b)+(c) + a STATUS byte tier (rotate to <32,550 B). |
| LIQUID | Market | L4 | H | 2026-09-01 | HY / credit spreads / liquidity | L5 on: THESIS version bump reflecting the 8/23-8/28 rework |
| VIOLET | Market | L4 | M | 2026-09-01 | VIX / vol term structure / vol-of-vol | Conf M→H on the 6/6-handles re-verification (still owed) |
| BRENT | Market | L5 | M | 2026-09-01 | Oil — Brent / WTI | Conf M→H at PR#6 on a SECOND clean cycle + RULINGS.md touched or frozen. |
| HENRY | Market | L4 | H | 2026-09-01 | Macro velocity / market trends | L5 on the §2 handle (or a ruling that the local form satisfies it) |
| CARL | Market | L4 | H | 2026-09-01 | Consumer & credit-transmission macro | L5 on: boot.py whitelist widened to surface plain ERROR lines (one edit) |
| LABOR | Market | L5 | H | 2026-09-01 | Labor market (claims / JOLTS / NFP) | L5 SUSTAINED-WATCH: STATUS byte tier to <32,550 B (rotation) at next cl… |
| BROCK | Market | L4 | H | 2026-09-01 | Private credit / BDC / non-traded credit | L5 blocker external; a declared byte-budget block (TERRY form) is the o… |
| HAWK | Market | L4 | H | 2026-09-01 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | L5 on: a self-driven session (spawn driver) |
| TERRY | Utility | L4 | H | 2026-09-01 | Trade construction / risk scoring ‡‡ | L5 on the ONE-LINE fix: POSTMORTEMS.md:4 header re-cut to its own entri… |
| REGINALD | Market | L4 | H | 2026-09-01 | Regional banks | L5 on the Brier/archive layer (PREDICTIONS_ARCHIVE |
| MARCO | Market | L4 | H | 2026-09-01 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | L5 on the three handles (labeled BOTTOM LINE · §2 5-pt/Independence · P… |
| ORACLE | Utility | L4 | H | 2026-09-01 | Prediction-market diagnostics ‡‡‡ | L5 on the Brier scoreboard (decide first whether it is required at L5-u… |
| BOND | Market | L4 | H | 2026-09-01 | US bond-market structure / auctions / rates | L5 on: STATUS byte tier — rotate to <32,550 B (SHADE's crc-archive form… |
| CORAL | Market | L3 | H | 2026-09-01 | Florida (whole-state, 10 pillars) | L4 on: the flat-by-design TRADE ruling (Will) |
| SHADE | Market | L3 | H | 2026-09-01 | Insurer-lender / PE-insurance-captive | L4 on PREDICTIONS.tsv seeded with confidences AT REGISTRATION (one file… |
| ZHAO | Market | L3 | H | 2026-09-01 | China macro — UST demand / capital flows / Korea | L4 on: inbox drained (VULCAN ×3 first) |
| AEOLUS | Market | L3 | M | 2026-09-01 | Climate → economy (macro; insurance/ag/energy-demand channels) | Conf M→H at the Mode-A profile fan-out (owed since 8/23) |
| WATT | Market | L3 | H | 2026-09-01 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | L4 on: a boot that consumes the AEOLUS seam packets |
| VULCAN | Market | L4 | M | 2026-09-01 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | Conf M→H on ONE reader-side consumption confirmed at the reader's artif… |
| MIDAS | Market | L3 | H | 2026-09-01 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | L4 on: TRADE.md feeding a proposal (zero capital by design — Will's cal… |
| OSPREY | Market | L2 | H | 2026-09-01 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | L3 on the strike-feed instrument (scripts/ |
| FALCON | Market | L4 | H | 2026-09-01 | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | L5 on: STATUS ≤250 (clears YEY-002) |
| HOMER | Market | L2 | H | 2026-09-01 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | L3 on: (a) a thesis-level kill rail file (dated) |
| OZK | Market | L4 | H | 2026-09-01 | Bank OZK specialist (RESG construction / classified-migration watch) | L5 on: KB_INDEX re-rolled |
| WAL | Market | L4 | M | 2026-09-01 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | Conf M→H at PR#6 on WAL-01/02 graded-or-voided |
| FLG | Market | L3 | M | 2026-09-01 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | Conf M→H on the first grade 11/06 landing as dated |
| CRUISE | Market | L3 | M | 2026-09-01 | Cruise-sector event specialist — CCL vehicle; fuel-cost transmission (BRENT → CCL); 8-channel pre-announce watchlist (`WATCHLIST_CCL_PREANNOUNCE.md`, 8/14); Q3 print ~9/28-29. ⚠️ The 7/2 arm-CCL ladder is PROPOSED-NEVER-RATIFIED and 4wk in-band — retire-or-fresh-levels decision staged at next session (row-55 ruling 8/21); do NOT treat its band as a live threshold | DEMOTE L3→L2 if the Q3 print (~9/28) passes with no session |
| FERT | Market | L2 | H | 2026-09-01 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | L3 on ≥1 OPEN forward prediction registered with Resolve_By |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| CREED | Market | L4 | M | 2026-09-01 | National CRE / CMBS | Conf M→H on the TRADE-feeding read |
| DEWEY | Utility | L4 | M | 2026-09-01 | Deep on-demand research | L5 on the CONTRACT block (one section) |
| HANS | Market | L4 | H | 2026-09-01 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | L5 on cycle 2 clean (a session after the 9/10 ECB with HNS-05 graded on… |
| OTTO | Market | L4 | H | 2026-09-01 | Auto-industry fraud & stress | L5 on: §2 overlay + SIGNALS.md line struck + STATUS ≤250 / byte tier +… |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — |
| BARON | — | — | — | — | Trump financial-policy network | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L5 | H | 2026-09-01 | Fleet architect — design / structure / maturity / lifecycle | Sustain L5: profile refresh queue (NEXUS→RED→PROME 9/08 |
| YEYOU | Utility | L3 | H | 2026-09-01 | Repo-wide reviewer (manual / branch model) | L4 on proof of consumption beyond YEY-012 |
| RAV | Meta | L2 | M | 2026-09-01 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on the FIRST §5 run report in AGENTS/RAV/runs/ (Will-driven |

---
*33 active · 4 tier-2 · 2 dormant · 3 special. Dropped (retired): HERMES. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*
