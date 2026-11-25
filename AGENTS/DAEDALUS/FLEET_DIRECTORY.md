# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-11-25.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

**WF:** configured phrase-list entries at render time, not hits or routing health. `0` = explicit empty list; `—` = no list; `n/a` = owner-declared non-query desk; `UNKNOWN` = source unavailable/unsupported. Regenerate after lane edits; the existing directory-age guard watches ROSTER/FLEET_MAP only.
WF source: `/home/willi/Research-Intake/scripts/newsweep_config.py` · SHA256 `973b9fb4983c16630c867fe203745a6467bb6871b0d16210654d823f0f582226`.

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| PROME | Meta | L4 | M | 2026-11-18 | Coordinator / chief of staff | L5 requires a DAEDALUS zero-own-rule adjudication over a window that st… | — |
| WALTER | Utility | L4 | H | 2026-11-18 | Signal & news routing | L5 requires a DAEDALUS confirm-read of the current charter (post Novemb… | — |
| NEXUS | Utility | L5 | M | 2026-11-18 | Cross-agent synthesis | Conf H needs a DAEDALUS confirm-read of the schema-authority line and o… | — |
| RED | Utility | L5 | M | 2026-11-18 | Adversarial red-team | Conf H needs a DAEDALUS full read of the current charter, STATUS and cl… | — |
| SAM | Market | L4 | H | 2026-11-18 | Japan — BOJ / JGB / carry | L5 requires STATUS and MEMORY rotated under 70% of budget, the November… | 12 |
| LIQUID | Market | L4 | H | 2026-11-18 | HY / credit spreads / liquidity | L5 requires a DAEDALUS read of clean and current closeout, including th… | 7 |
| VIOLET | Market | L4 | M | 2026-11-18 | VIX / vol term structure / vol-of-vol | L5 requires MEMORY.md rotated under 70% of budget (rotation_due=0), the… | 7 |
| BRENT | Market | L5 | M | 2026-11-18 | Oil — Brent / WTI | Conf M to H after a version-consistency check is wired into boot.py and… | 15 |
| HENRY | Market | L4 | H | 2026-11-18 | Macro velocity / market trends | L5 needs a DAEDALUS whole read of the thesis, thresholds and cross-desk… | 64 |
| CARL | Market | L4 | H | 2026-11-18 | Consumer & credit-transmission macro | L5 needs a DAEDALUS read of the seven sub-agent ledgers for current dis… | 4 |
| LABOR | Market | L5 | H | 2026-11-18 | Labor market (claims / JOLTS / NFP) | L5 sustain needs the charter trimmed under 50,000 B by moving history o… | 12 |
| BROCK | Market | L4 | H | 2026-11-18 | Private credit / BDC / non-traded credit | L5 requires a DAEDALUS read of clean and current owner closeouts and th… | 8 |
| HAWK | Market | L4 | H | 2026-11-18 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | Retain L4. Verify that HAWK grades C3 limb 2 at November 27 (DOCKET wak… | 8 |
| TERRY | Utility | L5 | H | 2026-11-18 | Trade construction / risk scoring ‡‡ | L5 sustain needs STATUS at closeout to list each inbox packet held for… | 7 |
| REGINALD | Market | L4 | H | 2026-11-18 | Regional banks | L5 requires a DAEDALUS read of a dated clean and current owner closeout | 6 |
| MARCO | Market | L4 | M | 2026-11-18 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | Conf H after MARCO re-dates or re-states its BOTTOM LINE heading agains… | 5 |
| ORACLE | Utility | L4 | H | 2026-11-18 | Prediction-market diagnostics ‡‡‡ | L5 requires F-1 Brier and NEH evidence from the owner, a current STATUS… | — |
| BOND | Market | L4 | H | 2026-11-18 | US bond-market structure / auctions / rates | L5 requires workbook/LEDGER_GLOB declared, two-clock headers on the dec… | 7 |
| CORAL | Market | L4 | M | 2026-11-18 | Florida (whole-state, 10 pillars) | L5 requires clean, current closeouts verified by DAEDALUS: the November… | 16 |
| SHADE | Market | L3 | H | 2026-11-18 | Insurer-lender / PE-insurance-captive | L4 requires a declared-flat TRADE surface with an explicit re-arm condi… | 10 |
| ZHAO | Market | L4 | H | 2026-11-18 | China macro — UST demand / capital flows / Korea | L5 requires the GACC tables read or a declared substitute, the August r… | 11 |
| AEOLUS | Market | L4 | M | 2026-11-18 | Climate → economy (macro; insurance/ag/energy-demand channels) | Bring the charter under 50,000 B per WQ-701 A2, drain the six packets,… | 12 |
| WATT | Market | L4 | H | 2026-11-18 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | L5 requires a DAEDALUS confirm-read of two consecutive clean WEEKLY cyc… | 21 |
| VULCAN | Market | L4 | H | 2026-11-18 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | Re-cut TRADE.md against the current matrix and the live TERRY card, or… | 11 |
| MIDAS | Market | L4 | H | 2026-11-18 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | DAEDALUS runs the November 6 guard repairs on a capable case and a clea… | 11 |
| OSPREY | Market | L3 | H | 2026-11-18 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | Retain L3 pending the reading-A trade branch | 14 |
| FALCON | Market | L4 | H | 2026-11-18 | US/Israel/Iran-Gulf war theater — 3-tier B/C/D scenario ladder (no Scenario A; THESIS/EXIT), Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | L5 needs two things: the November 18 carried items disposed, and a clea… | 10 |
| HOMER | Market | L4 | H | 2026-11-18 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | L5 needs a DAEDALUS read of the November 20 formal grade and its closeo… | 14 |
| YURI | Market | L2 | M | 2026-11-18 | **Russia — ACTOR-KEYED: what the Russian state DECIDES, across all channels, as one actor** (mobilisation, asset seizure, force posture, export instruments). ⛔ **NOT Russia macro** — the name follows the fleet's human-first-name convention for geography desks and reads narrower than the charter; the charter scope is the authority, not the name. | Grade YUR-F02 on November 28 against the dated call records (DAEDALUS r… | 3 |
| OZK | Market | L4 | H | 2026-11-18 | Bank OZK specialist (RESG construction / classified-migration watch) | L5 requires a DAEDALUS read of a clean and current closeout | 2 |
| WAL | Market | L4 | M | 2026-11-18 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.4 (since 8/20; cell corrected 2026-10-30 on DAEDALUS WAL refresh § 4)) | Conf M to H requires the KB Stale_By backlog judged row by row (no bulk… | 3 |
| FLG | Market | L4 | M | 2026-11-18 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | Conf M to H requires the 44 stale KB rows dispositioned, the outside-au… | 17 |
| CRUISE | Market | L4 | M | 2026-11-18 | Cruise-sector desk — **live scope re-set under WQ-435 (Will 2026-10-15 12:26 ET; charter § Live scope encoded 2026-10-16, verified 64dc05e37):** ① operator dispersion + NCLH credit/demand (CRU-11, `VX-CRU-05`) · ② cruise as a consumer-demand read for CARL/MARCO · ③ Florida/Gulf ports. Gulf/war-risk = ONE trigger (`VX-CRU-04`, FALCON owns the theater); fuel = a cost line only (BRENT owns the price). Wake carrier = dated PROME DOCKET rows naming CRUISE (RCL Q3 L713 10/27 · NCLH L714). ⚠️ The March fuel-cost / tourism-canary mission and the 7/2 arm-CCL ladder are HISTORY (ladder PROPOSED-NEVER-RATIFIED; do NOT treat its band as a live threshold) — row text refreshed 2026-10-23 08:49 ET (DOCKET L815 ①) | L4 granted November 18 on DAEDALUS's reading of reading A, branch 1: th… | 7 |
| FERT | Market | L4 | M | 2026-11-18 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — log+flag, no deep-dive; the scope and its benchmark rows landed in one charter edit 2026-08-19 (beb3a36cb9) and the full rule, with its depth-revisit trigger, is `AGENTS/FERT/CLAUDE.md` § POTASH; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | L5 requires a DAEDALUS confirm-read of clean, current closeouts across… | 12 |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| GIBBS | Market | L2 | M | 2026-11-18 | Large-bank desk — the 16 US firms in Fed Categories I–III (named list, re-cut quarterly): is regional-bank stress industry-wide, and is large-bank lending to non-bank finance transmitting it | Market L3 cannot fire as written while WQ-426 rules out thresholds and… | — |
| CYPHER | Market | L2 | M | 2026-11-18 | Cyber → markets desk — tracks cyber events that can move money (bank/core-vendor incidents, exploited flaws in widely used products, supply-chain compromises, insurer aggregation, attacks on energy/shipping/grid, state-actor campaigns); owns the event (what happened, confirmed?, class, dates, escalation state); hands bank/insurance/energy consequences to existing owners (REGINALD/GIBBS, SHADE, BRENT/FALCON, WATT, HENRY/VULCAN) | L3 needs at least one CYP prediction actually resolved on its named ins… | 53 |
| ISHM | Market | L2 | M | 2026-11-18 | US industrial / manufacturing-cycle desk — is the factory upturn real end-demand or borrowed (tariff front-running, AI/defence capex, inventory rebuild), and when does it roll over; surveys (ISM, S&P Global PMI, five regional Feds), hard data (IP/CU, durables and core capex, factory orders), freight volumes ex-tankers, eight frozen bellwethers (CAT · DE · HON · GE Aerospace · PH · MMM · EMR · UNP); standing jobs J1 core capex vs VULCAN, J2 freight vs LIQUID/RED | L3 requires an approved prediction row that actually resolves, plus con… | — |
| CREED | Market | L4 | H | 2026-11-18 | National CRE / CMBS | L5 requires a DAEDALUS read of the current guards and the November 5 to… | 36 |
| DEWEY | Utility | L4 | M | 2026-11-18 | Deep on-demand research | Conf-H requires a DAEDALUS read of the local contract form and actual c… | n/a |
| HANS | Market | L5 | H | 2026-11-18 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | L5 SUSTAIN requires a DAEDALUS read of the next owner closeout that rec… | 10 |
| OTTO | Market | L5 | M | 2026-11-18 | Auto-industry fraud & stress | Conf H needs a confirm-read after OTTO closes the s047 closeout surface… | 9 |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — | — |
| BARON | — | — | — | — | Trump financial-policy network | — | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L4 | M | 2026-11-25 | Fleet architect — design / structure / maturity / lifecycle | Grade YUR-F02 November 28 | n/a |
| RAV | Meta | L2 | M | 2026-11-18 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on first charter §5 run report when Will commissions it | — |
| CATO | — | — | — | — | Will's manual Codex/Astra adviser + independent reviewer | UNGRADED BY RULING (WQ-255, 2026-09-26): manual-only — no launch, no routing, no ladder row | — |

---
*34 active · 7 tier-2 · 2 dormant · 3 special. Dropped (retired): HERMES, YEYOU. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*

*⏸ **CLASSIFICATION PENDING (ROSTER, Will's hold):** entries under that heading are NOT graded and carry no FLEET_MAP row by ruling — read the section in `PROME/ROSTER.md` for the names and the restriction. Absence from the tables above is the hold, not an omission.*
