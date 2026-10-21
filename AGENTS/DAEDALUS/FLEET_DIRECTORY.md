# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-10-21.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

**WF:** configured phrase-list entries at render time, not hits or routing health. `0` = explicit empty list; `—` = no list; `n/a` = owner-declared non-query desk; `UNKNOWN` = source unavailable/unsupported. Regenerate after lane edits; the existing directory-age guard watches ROSTER/FLEET_MAP only.
WF source: `/home/willi/Research-Intake/scripts/newsweep_config.py` · SHA256 `90647b8d00e91af4bc0f76bf9055f156eda1bfef4ec6c9e9456029cea99ab464`.

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| PROME | Meta | L4 | M | 2026-10-21 | Coordinator / chief of staff | L5 requires DAEDALUS judgment of zero own-rule-unexecuted against curre… | — |
| WALTER | Utility | L4 | H | 2026-10-21 | Signal & news routing | L5 confirm-read on current utility ladder and completed procedural peri… | — |
| NEXUS | Utility | L5 | M | 2026-10-21 | Cross-agent synthesis | Conf-H: verify schema-write authority/safety in local form and own-read… | — |
| RED | Utility | L5 | M | 2026-10-21 | Adversarial red-team | Conf-H retains both RED state-token draft and committed WALTER counters… | — |
| SAM | Market | L4 | H | 2026-10-21 | Japan — BOJ / JGB / carry | At the first closeout after SAM-42 resolves: verify both-direction reco… | 12 |
| LIQUID | Market | L4 | H | 2026-10-21 | HY / credit spreads / liquidity | DAEDALUS confirms whether the October 14 baseline banner plus live owne… | 7 |
| VIOLET | Market | L4 | M | 2026-10-21 | VIX / vol term structure / vol-of-vol | L5 candidate after KB.tsv gains its two-clock header and a clean closeo… | 7 |
| BRENT | Market | L5 | M | 2026-10-21 | Oil — Brent / WTI | Conf M-to-H after version-consistency check is wired and observed on ca… | 15 |
| HENRY | Market | L4 | H | 2026-10-21 | Macro velocity / market trends | DAEDALUS adjudicates the existing prose local form at the next profile… | 6 |
| CARL | Market | L4 | H | 2026-10-21 | Consumer & credit-transmission macro | L5 after CARL dispositions its17 stale child ledgers and6 attention war… | 4 |
| LABOR | Market | L5 | H | 2026-10-21 | Labor market (claims / JOLTS / NFP) | SUSTAIN at next claims-grade closeout (after its source release) with o… | 12 |
| BROCK | Market | L4 | H | 2026-10-21 | Private credit / BDC / non-traded credit | DAEDALUS conducts L5 per-leg confirmation at this PR: old three owner r… | 6 |
| HAWK | Market | L4 | H | 2026-10-21 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | L5 requires a current substantive owner pass that performs the October… | 8 |
| TERRY | Utility | L5 | H | 2026-10-21 | Trade construction / risk scoring ‡‡ | L5 retained at prior grade | 7 |
| REGINALD | Market | L4 | H | 2026-10-21 | Regional banks | L5 candidate after REG-06 gets a dated positive search instrument befor… | 6 |
| MARCO | Market | L4 | M | 2026-10-21 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | DAEDALUS confirm-read may restore Conf H after remaining matrix/figure/… | 5 |
| ORACLE | Utility | L4 | H | 2026-10-21 | Prediction-market diagnostics ‡‡‡ | Review F1 calibration artifact and NEH leg when owner delivers | — |
| BOND | Market | L4 | H | 2026-10-21 | US bond-market structure / auctions / rates | L5 candidate after own-tree LEDGER_GLOB and named-core two-clock header… | 7 |
| CORAL | Market | L4 | M | 2026-10-21 | Florida (whole-state, 10 pillars) | Owner should resolve forward-log authority and make thesis clock's mean… | 16 |
| SHADE | Market | L3 | H | 2026-10-21 | Insurer-lender / PE-insurance-captive | At the already-recorded October 23 owner session: predictions with regi… | 10 |
| ZHAO | Market | L4 | H | 2026-10-21 | China macro — UST demand / capital flows / Korea | L5 still requires GACC/SAFE dispositions and verified clean/current clo… | 11 |
| AEOLUS | Market | L4 | M | 2026-10-21 | Climate → economy (macro; insurance/ag/energy-demand channels) | AEOLUS dispositions dated profile packet within existing scope | 12 |
| WATT | Market | L4 | H | 2026-10-21 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | Two clean WEEKLY cycles remain unverified | 21 |
| VULCAN | Market | L4 | H | 2026-10-21 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | Keep L5 conditional on two verified clean WEEKLY cycles and resumed S2… | 11 |
| MIDAS | Market | L4 | H | 2026-10-21 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | L5 on verified clean/current weekly contract-map and crossing review, w… | 11 |
| OSPREY | Market | L3 | H | 2026-10-21 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | Retain L3 pending reading-A trade branch | 14 |
| FALCON | Market | L4 | H | 2026-10-21 | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | L5 on a current clean owner cycle honoring October21 review and registe… | 10 |
| HOMER | Market | L3 | M | 2026-10-21 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | L4 adjudication on reading-A trade/consumer leg at next DAEDALUS review | — |
| YURI | Market | L2 | M | 2026-10-21 | **Russia — ACTOR-KEYED: what the Russian state DECIDES, across all channels, as one actor** (mobilisation, asset seizure, force posture, export instruments). ⛔ **NOT Russia macro** — the name follows the fleet's human-first-name convention for geography desks and reads narrower than the charter; the charter scope is the authority, not the name. | DAEDALUS confirm-read of INTENT_LEDGER/grade memos can firm confidence | — |
| OZK | Market | L4 | H | 2026-10-21 | Bank OZK specialist (RESG construction / classified-migration watch) | L5 candidate after adding218/219 to MEMO_ITEM_3 and proving row-ID cove… | 2 |
| WAL | Market | L4 | M | 2026-10-21 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | Conf M-to-H after Q3 10-Q is published and the registered cross-check c… | 3 |
| FLG | Market | L3 | M | 2026-10-21 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | Conf M-to-H when FLG-02/03 are graded from actualQ3 10-Q publication, R… | 8 |
| CRUISE | Market | L3 | H | 2026-10-21 | Cruise-sector event specialist — CCL vehicle; fuel-cost transmission (BRENT → CCL); 8-channel pre-announce watchlist (`WATCHLIST_CCL_PREANNOUNCE.md`, 8/14); Q3 print ~9/28-29. ⚠️ The 7/2 arm-CCL ladder is PROPOSED-NEVER-RATIFIED and 4wk in-band — retire-or-fresh-levels decision staged at next session (row-55 ruling 8/21); do NOT treat its band as a live threshold | L4 branch remains unverified: existing WATCH is not automatically DECLA… | 7 |
| FERT | Market | L4 | M | 2026-10-21 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | L5 clean-closeout measurement remains owed | 10 |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| GIBBS | Market | L1 | M | 2026-10-21 | Large-bank desk — the 16 US firms in Fed Categories I–III (named list, re-cut quarterly): is regional-bank stress industry-wide, and is large-bank lending to non-bank finance transmitting it | L2 after tagged READS accrual across a second owner session under exist… | — |
| CREED | Market | L4 | H | 2026-10-21 | National CRE / CMBS | Preserve current-judgment/date consistency and full-manifest read-cap g… | 36 |
| DEWEY | Utility | L4 | M | 2026-10-21 | Deep on-demand research | Conf-H requires a full reviewer read of substantive PRODUCES/CONSUMED B… | n/a |
| HANS | Market | L5 | H | 2026-10-21 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | SUSTAIN L5 review at actual named Q3 event, requiring the ex-ante HNS-0… | 10 |
| OTTO | Market | L5 | M | 2026-10-21 | Auto-industry fraud & stress | Retain L5/M bounded pending full source-cell transition verification | 9 |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — | — |
| BARON | — | — | — | — | Trump financial-policy network | — | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L4 | M | 2026-10-21 | Fleet architect — design / structure / maturity / lifecycle | L5 not attempted: finish current review dispositions and satisfy zero-o… | n/a |
| RAV | Meta | L2 | M | 2026-10-21 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on first charter §5 run report when Will commissions it | — |
| CATO | — | — | — | — | Will's manual Codex/Astra adviser + independent reviewer | UNGRADED BY RULING (WQ-255, 2026-09-26): manual-only — no launch, no routing, no ladder row | — |

---
*34 active · 5 tier-2 · 2 dormant · 3 special. Dropped (retired): HERMES, YEYOU. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*

*⏸ **CLASSIFICATION PENDING (ROSTER, Will's hold):** entries under that heading are NOT graded and carry no FLEET_MAP row by ruling — read the section in `PROME/ROSTER.md` for the names and the restriction. Absence from the tables above is the hold, not an omission.*
