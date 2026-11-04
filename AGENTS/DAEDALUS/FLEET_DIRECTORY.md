# FLEET DIRECTORY — what every agent is, does, and is missing

> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by `AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — hand-edits are overwritten. Generated 2026-11-04.

> ⚑ **THIS IS THE BOOT-READ HOT INDEX (SPAWN PROTOCOL step 2, re-homed 2026-08-23).** `FLEET_MAP.tsv` is the COLD full register — it holds the complete Gaps/Next_upgrade text and is read PER-AGENT on demand (`grep -P '^AGENT\t' FLEET_MAP.tsv`) or whole at a Production Review. Why: FLEET_MAP hit **121% of the harness single-read token cap** and had been truncating at every boot for ~6 days (PAT-111 recurring on its third file). Rotating the accumulated Gaps narrative to `FLEET_MAP_HISTORY.tsv` cut it 65,725 → 43,006 B, which is **not enough** — squeezing it under the budget would have meant deleting live gap content from the rich rows. So the register went cold and this generated view became the read, the same hot/cold split `PATTERNS_HOT.md` uses. ⛔ Never answer a cap breach by raising the budget: the read cap is not ours to move.

*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); **class** + **maturity level** + **Cf** (confidence: H=read-verified, M=read+mechanical, L=mechanical-only) + **Scored** (last-scored date) + **missing/next** ← FLEET_MAP (DAEDALUS). "Missing / next" is a truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never by-design. PROME graded 2026-07-28 (Will-ratified, judgment-read only — the scripted floor cannot see a root-level agent).*

**WF:** configured phrase-list entries at render time, not hits or routing health. `0` = explicit empty list; `—` = no list; `n/a` = owner-declared non-query desk; `UNKNOWN` = source unavailable/unsupported. Regenerate after lane edits; the existing directory-age guard watches ROSTER/FLEET_MAP only.
WF source: `/home/willi/Research-Intake/scripts/newsweep_config.py` · SHA256 `72c2a8ae943e2d40cc676884e5c036da6c114bd2453bb42b0a0f93a77aa28789`.

## 🟢 ACTIVE — persistent domain owners

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| PROME | Meta | L4 | M | 2026-10-21 | Coordinator / chief of staff | L5 requires current zero-own-rule judgment and owner dispositions of th… | — |
| WALTER | Utility | L4 | H | 2026-10-21 | Signal & news routing | L5 requires surviving procedural perimeter and current utility legs ver… | — |
| NEXUS | Utility | L5 | M | 2026-10-21 | Cross-agent synthesis | Conf-H: verify schema-write authority/safety in local form and own-read… | — |
| RED | Utility | L5 | M | 2026-10-21 | Adversarial red-team | Conf H follows substantive draft/countersign verification and DAEDALUS… | — |
| SAM | Market | L4 | H | 2026-10-21 | Japan — BOJ / JGB / carry | Inspect first post-SAM-42 closeout for one figure checked both directio… | 12 |
| LIQUID | Market | L4 | H | 2026-10-21 | HY / credit spreads / liquidity | Verify current structural-leg/local-form judgment and clean/current clo… | 7 |
| VIOLET | Market | L4 | M | 2026-10-21 | VIX / vol term structure / vol-of-vol | L5 candidate after KB.tsv gains its two-clock header and a clean closeo… | 7 |
| BRENT | Market | L5 | M | 2026-10-21 | Oil — Brent / WTI | Conf M-to-H after version-consistency check is wired and observed on ca… | 15 |
| HENRY | Market | L4 | H | 2026-10-21 | Macro velocity / market trends | Whole relevant-section read decides existing prose local form before an… | 6 |
| CARL | Market | L4 | H | 2026-10-21 | Consumer & credit-transmission macro | L5 requires current child-ledger/STUE dispositions and independently ve… | 4 |
| LABOR | Market | L5 | H | 2026-10-21 | Labor market (claims / JOLTS / NFP) | November 3 JOLTS updates LEG C before November 6 NFP | 12 |
| BROCK | Market | L4 | H | 2026-10-30 | Private credit / BDC / non-traded credit | Remaining L5 adjudication needs full clean/current owner closeout and s… | 8 |
| HAWK | Market | L4 | H | 2026-10-22 | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | Verify actual HAW-20/22 grades and live K2/post-October-31 successor | 8 |
| TERRY | Utility | L5 | H | 2026-10-21 | Trade construction / risk scoring ‡‡ | Next sustain checks actual arrival/boot chronology and ledger consisten… | 7 |
| REGINALD | Market | L4 | H | 2026-10-30 | Regional banks | L5 remains NOT ADJUDICATED at this bounded check | 6 |
| MARCO | Market | L4 | M | 2026-10-21 | Florida migration / tourism (FL sub; reconcile w/ CORAL) | DAEDALUS confirm-read may restore Conf H after remaining matrix/figure/… | 5 |
| ORACLE | Utility | L4 | H | 2026-10-21 | Prediction-market diagnostics ‡‡‡ | Review owner F1/NEH/settled-pin evidence when delivered | — |
| BOND | Market | L4 | H | 2026-10-21 | US bond-market structure / auctions / rates | Existing header/declaration/rotation and clean-closeout requirements re… | 7 |
| CORAL | Market | L4 | M | 2026-10-21 | Florida (whole-state, 10 pillars) | Owner clarifies thesis clock meaning and PROME updates GATES mirror | 16 |
| SHADE | Market | L3 | H | 2026-10-21 | Insurer-lender / PE-insurance-captive | Next authorized owner session dispositions existing remaining surfaces… | 10 |
| ZHAO | Market | L4 | H | 2026-10-21 | China macro — UST demand / capital flows / Korea | L5 requires actual source-debt dispositions and independently verified… | 11 |
| AEOLUS | Market | L4 | M | 2026-10-21 | Climate → economy (macro; insurance/ag/energy-demand channels) | Bounded November 2 verification closes C4 verdict-label and C3 level-ma… | 12 |
| WATT | Market | L4 | H | 2026-10-21 | Power/grid — PJM stress → wholesale price → industrial/data-center cost | Read existing November 4 test at required tape/EEA/202(c) inputs includ… | 21 |
| VULCAN | Market | L4 | H | 2026-10-21 | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | L5 remains conditional on independently verified clean WEEKLY cycles/cu… | 11 |
| MIDAS | Market | L4 | H | 2026-11-02 | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | MIDAS dispositions dated owner packet | 11 |
| OSPREY | Market | L3 | H | 2026-10-21 | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | Retain L3 pending charter no-book plus demonstrated consumer, or condit… | 14 |
| FALCON | Market | L4 | H | 2026-10-30 | US/Israel/Iran-Gulf war theater — 3-tier B/C/D scenario ladder (no Scenario A; THESIS/EXIT), Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | November 4 read: WQ-559 owner encoding still open | 10 |
| HOMER | Market | L4 | H | 2026-11-02 | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | L5 NOT-ADJUDICATED; verify current clean closeout and remaining owner d… | — |
| YURI | Market | L2 | M | 2026-10-21 | **Russia — ACTOR-KEYED: what the Russian state DECIDES, across all channels, as one actor** (mobilisation, asset seizure, force posture, export instruments). ⛔ **NOT Russia macro** — the name follows the fleet's human-first-name convention for geography desks and reads narrower than the charter; the charter scope is the authority, not the name. | Grade YUR-F02 November 28 at actual dated call records | 3 |
| OZK | Market | L4 | H | 2026-10-22 | Bank OZK specialist (RESG construction / classified-migration watch) | L5 candidate after independently verified clean closeout and first exis… | 2 |
| WAL | Market | L4 | M | 2026-10-30 | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.4 (since 8/20; cell corrected 2026-10-30 on DAEDALUS WAL refresh § 4)) | Conf M to H requires forward Q4 predictions by November 15 and current… | 3 |
| FLG | Market | L3 | M | 2026-10-22 | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | L4 adjudication once FLG-02/03 grade from the actual Q3 10-Q (Resolve_B… | 17 |
| CRUISE | Market | L3 | H | 2026-10-21 | Cruise-sector desk — **live scope re-set under WQ-435 (Will 2026-10-15 12:26 ET; charter § Live scope encoded 2026-10-16, verified 64dc05e37):** ① operator dispersion + NCLH credit/demand (CRU-11, `VX-CRU-05`) · ② cruise as a consumer-demand read for CARL/MARCO · ③ Florida/Gulf ports. Gulf/war-risk = ONE trigger (`VX-CRU-04`, FALCON owns the theater); fuel = a cost line only (BRENT owns the price). Wake carrier = dated PROME DOCKET rows naming CRUISE (RCL Q3 L713 10/27 · NCLH L714). ⚠️ The March fuel-cost / tourism-canary mission and the 7/2 arm-CCL ladder are HISTORY (ladder PROPOSED-NEVER-RATIFIED; do NOT treat its band as a live threshold) — row text refreshed 2026-10-23 08:49 ET (DOCKET L815 ①) | L4 reading-A branch remains unverified | 7 |
| FERT | Market | L4 | M | 2026-10-21 | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | Existing clean-closeout measurement remains | 12 |

## 🟡 TIER-2 — spawned as needed

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| GIBBS | Market | L1 | M | 2026-11-04 | Large-bank desk — the 16 US firms in Fed Categories I–III (named list, re-cut quarterly): is regional-bank stress industry-wide, and is large-bank lending to non-bank finance transmitting it | GIBBS dispositions three schema cells preserving source/basis prose | — |
| CYPHER | Market | L2 | M | 2026-10-28 | Cyber → markets desk — tracks cyber events that can move money (bank/core-vendor incidents, exploited flaws in widely used products, supply-chain compromises, insurer aggregation, attacks on energy/shipping/grid, state-actor campaigns); owns the event (what happened, confirmed?, class, dates, escalation state); hands bank/insurance/energy consequences to existing owners (REGINALD/GIBBS, SHADE, BRENT/FALCON, WATT, HENRY/VULCAN) | L3 requires actual resolving prediction plus other ladder legs on their… | 51 |
| ISHM | Market | L2 | M | 2026-10-28 | US industrial / manufacturing-cycle desk — is the factory upturn real end-demand or borrowed (tariff front-running, AI/defence capex, inventory rebuild), and when does it roll over; surveys (ISM, S&P Global PMI, five regional Feds), hard data (IP/CU, durables and core capex, factory orders), freight volumes ex-tankers, eight frozen bellwethers (CAT · DE · HON · GE Aerospace · PH · MMM · EMR · UNP); standing jobs J1 core capex vs VULCAN, J2 freight vs LIQUID/RED | L3 requires actual resolving prediction/calibration and convergence loc… | — |
| CREED | Market | L4 | H | 2026-10-30 | National CRE / CMBS | Owner re-verifies or marks the 11 expired ACTIVE evidence rows on next… | 36 |
| DEWEY | Utility | L4 | M | 2026-10-21 | Deep on-demand research | Conf-H requires a full reviewer read of substantive PRODUCES/CONSUMED B… | n/a |
| HANS | Market | L5 | H | 2026-10-23 | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | Owner grades on frozen instruments when actual inputs arrive | 10 |
| OTTO | Market | L5 | M | 2026-10-21 | Auto-industry fraud & stress | Retain L5/M bounded pending full source-cell transition verification | 9 |

## ⚪ DORMANT — revive only on explicit need

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| SENTRY | — | — | — | — | Cross-domain signal pipeline | — | — |
| BARON | — | — | — | — | Trump financial-policy network | — | — |

## 🔵 SPECIAL — meta / cross-fleet (on-demand)

| Agent | Class | Lvl | Cf | Scored | What it does | Missing / next | WF |
|---|---|---|---|---|---|---|---|
| DAEDALUS | Meta | L4 | M | 2026-11-02 | Fleet architect — design / structure / maturity / lifecycle | On next authorized resume: November 4 post-cutoff events, repaired-owne… | n/a |
| RAV | Meta | L2 | M | 2026-10-21 | Deep factual/analytical reviewer + bounded repair (Codex, Will-driven) | L3 on first charter §5 run report when Will commissions it | — |
| CATO | — | — | — | — | Will's manual Codex/Astra adviser + independent reviewer | UNGRADED BY RULING (WQ-255, 2026-09-26): manual-only — no launch, no routing, no ladder row | — |

---
*34 active · 7 tier-2 · 2 dormant · 3 special. Dropped (retired): HERMES, YEYOU. Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*

*⏸ **CLASSIFICATION PENDING (ROSTER, Will's hold):** entries under that heading are NOT graded and carry no FLEET_MAP row by ruling — read the section in `PROME/ROSTER.md` for the names and the restriction. Absence from the tables above is the hold, not an omission.*
