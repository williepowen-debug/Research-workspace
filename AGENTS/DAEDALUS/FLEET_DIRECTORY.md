# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-08-28.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| PROME | Meta | L5 | M | 2026-08-17 | Coordinator / chief of staff | L5 CONFIRM at sweep run #2 ~9/6 — full 21d window, ZERO new unexecuted-… |
| WALTER | Utility | L4 | H | 2026-08-26 | Signal & news routing | L5 blocker RE-CUT 8/26: prior blocker (BOTTOM LINE regression) DISCHARG… |
| NEXUS | Utility | L5 | M | 2026-08-17 | Cross-agent synthesis | L5 CONF M->H at next review if the §7 AUTHORITY label lands (optional p… |
| RED | Utility | L4 | H | 2026-08-12 | Adversarial red-team | L4->L5 re-cut 8/12: (a) addendum-closeout subset defined in CLAUDE.md |
| SAM | Market | L4 | H | 2026-08-17 | Japan — BOJ / JGB / carry | L5 on: owner-doc bidirectional sweep demonstrated one cycle |
| LIQUID | Market | L4 | H | 2026-08-17 | HY / credit spreads / liquidity | L4 HOLD — 8/10 restamp landed in ONE surface: CLAUDE.md:143 (BOOT-READ) |
| VIOLET | Market | L4 | M | 2026-08-17 | VIX / vol term structure / vol-of-vol | L4 HOLD (Conf H->M at PR#4): of the '6/6 handles VERIFIED 7/22' — BOTTO… |
| BRENT | Market | L4 | H | 2026-08-17 | Oil — Brent / WTI | L5 on: ONE closeout cycle w/ derived surfaces agreeing with banner laye… |
| HENRY | Market | L4 | H | 2026-08-17 | Macro velocity / market trends | L5 blocker unchanged (§2 handles ABSENT — scan re-detects it) |
| CARL | Market | L4 | H | 2026-08-17 | Consumer & credit-transmission macro | L5 DENIED at PR#4 on the zero-flags leg (prior 8/17-noon cell 'boot-wir… |
| LABOR | Market | L5 | H | 2026-08-17 | Labor market (claims / JOLTS / NFP) | L5 SUSTAINED-WATCH: PUBLISHED.tsv schema still has NO status column (su… |
| BROCK | Market | L4 | H | 2026-08-17 | Private credit / BDC / non-traded credit | L5 blocker external (YEYOU, waived-dormant) |
| HAWK | Market | L4 | H | 2026-08-17 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | URGENT pre-8/24: checkpoint conditions UNBUILT — successor falsificatio… |
| TERRY | Utility | L4 | H | 2026-08-07 | Trade construction / risk scoring ‡‡ | L5 (re-cut 8/7 PM per profile refresh |
| REGINALD | Market | L4 | H | 2026-08-17 | Regional banks | L5 legs: THESIS v1.4 refresh (own trigger now +27d, WORSE than at 8/7 s… |
| MARCO | Market | L4 | H | 2026-08-17 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | 8/21 write-back CLOSED-VERIFIED at artifact (3rd session): FLOW two-sta… |
| ORACLE | Utility | L4 | H | 2026-08-07 | Prediction-market diagnostics ‡‡‡ | L5: §2 CONTRACT block (cheap) |
| BOND | Market | L4 | H | 2026-08-20 | US bond-market structure / auctions / rates | "Packet ROUTED 8/20 (Will verbatim ""Approved on both - implement per y… |
| CORAL | Market | L3 | H | 2026-08-17 | Florida (whole-state, 10 pillars) | SLIPPED: ZERO self-commits 14d |
| SHADE | Market | L3 | H | 2026-08-17 | Insurer-lender / PE-insurance-captive | L3->L4 leg (a) = 3 cheap handles (seed PREDICTIONS.tsv — NONE EXISTS an… |
| ZHAO | Market | L3 | H | 2026-08-17 | China macro — UST demand / capital flows / Korea | DARK since 8/3 (14d — prior cell asserted LIVE, corrected PR#4) |
| AEOLUS | Market | L2 | H | 2026-08-17 | Climate → economy (macro; insurance/ag/energy-demand channels) | "8/21 PR#4 write-back CLOSED-VERIFIED 6/6 (3rd session |
| WATT | Market | L3 | H | 2026-08-07 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | L3->L4: verify reader-side consumption at next review (AEOLUS seam two-… |
| VULCAN | Market | L3 | H | 2026-08-15 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | L3->L4: consumption legs only (WATT already consuming the CRWV S3-S5 co… |
| MIDAS | Market | L3 | M | 2026-08-07 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | Firm L3 conf M->H at next touch: MIDAS-05 |
| OSPREY | Market | L2 | H | 2026-08-15 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | L3: OSP-01/02/03 window (Aug 1-3) CLOSED — retro-grade or record NO-VER… |
| FALCON | Market | L4 | H | 2026-08-15 | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | L4->L5: process the 8/6 Will-ruling write-back tail FIRST (VX-FALCON-SU… |
| HOMER | Market | L2 | H | 2026-08-23 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | upgrades/HOMER_CARD.md is now the queue (BUILT 8/22 — first ever |
| OZK | Market | L4 | H | 2026-08-17 | Bank OZK specialist (RESG construction / classified-migration watch) | P-OZK decision window ends 8/21 (DOCKET row cited BY DATE+TEXT — prior… |
| WAL | Market | L3 | H | 2026-08-17 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | predictions ledger UNGRADEABLE: WAL-01/02 OPEN 115d, schema has NO Reso… |
| FLG | Market | L1 | H | 2026-08-28 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | L2 when PREDICTIONS.tsv accrues its first OWN forward row (first live s… |
| CRUISE | Market | L3 | M | 2026-08-21 | Cruise-sector event specialist — CCL vehicle; fuel-cost transmission (BRENT → CCL); 8-channel pre-announce watchlist (`WATCHLIST_CCL_PREANNOUNCE.md`, 8/14); Q3 print ~9/28-29. ⚠️ The 7/2 arm-CCL ladder is PROPOSED-NEVER-RATIFIED and 4wk in-band — retire-or-fresh-levels decision staged at next session (row-55 ruling 8/21); do NOT treat its band as a live threshold | Next session (Will-staged): retire-or-fresh the ladder FIRST |
| FERT | Market | L2 | H | 2026-08-17 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | L2->L3 when: >=1 OPEN forward prediction registered (book is 0-OPEN — a… |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| CREED | Market | L3 | H | 2026-08-20 | National CRE / CMBS | Packet ROUTED 8/20 w/ 3 Will rulings (pointer pass APPROVED · T-08a bas… |
| DEWEY | Utility | L4 | M | 2026-08-07 | Deep on-demand research | CONTRACT block → L5 candidate |
| HANS | Market | L3 | M | 2026-08-07 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | next spawn: FLOW reconcile-or-freeze changelist |
| OTTO | Market | L4 | H | 2026-08-17 | Auto-industry fraud & stress | L5 blockers unmoved (OTTO-07 OPEN 15%, Dec-31 EDGAR-FTS re-instrument) |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — |
| BARON | — | — | — | — | Trump financial-policy network | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next |
|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L4 | H | 2026-08-28 | Fleet architect — design / structure / maturity / lifecycle | Staleness #4 ~9/1 ON TIME (last L5 cadence leg) |
| YEYOU | Utility | L3 | H | 2026-08-20 | Repo-wide reviewer (manual / branch model) | L4 on PROOF OF CONSUMPTION (PROME acts on the digest / a flag becomes b… |
| RAV | Meta | L2 | M | 2026-08-07 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on the FIRST charter-conformant run report in AGENTS/RAV/runs/ — §5'… |

---
*33 active · 4 tier-2 · 2 dormant · 3 special. Dropped (retired): HERMES. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*
