# Agent Profile — CARL

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow firm7-profiles-cards; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md (251 ln), thesis/{THESIS.md 426 ln, PREDICTIONS.tsv, CHANGELOG.md 1282 ln skim}, workbook/{KB.tsv 297 rows, SCHEMA.tsv, frozen-banner check on VX/FLOW/BNPL_STRESS/STATE_DIFFUSION/TRENDS/ABS_BASELINE}, NEXUS_BRIEF.md, TRADE.md, TEAM.md, ROADMAP/SCRATCH/MEMORY (line-counts), docket/CATALYSTS.tsv, board/BOARD_LOG.tsv (row-count), scripts/ ls · **Staleness:** refresh when the convergence matrix re-scores (next vector fire/invalidate) or the masking/Path-C falsification windows (CRL-20/21/24) resolve, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
U.S. consumer financial stress — credit DQ (CC/auto/student/mortgage), housing & foreclosures, K-shape bifurcation, consumer spending, gas-pump pass-through, ABS, consumer-cost insurance/healthcare. **Class:** Market. **Transmission: the MIDDLE** — `LABOR → CARL → REGINALD → market repricing` (CARL measures how employment/cost stress *converts* to credit deterioration); also feeds HENRY (wealth-effect V14) + LIQUID (ABS subordinate breach). **Spawnable by:** PROME / Will. **Cedes (one-source-of-truth):** labor/NFP/JOLTS → LABOR; bank-level impact → REGINALD; oil/Brent spot → HAWK/BRENT (CARL owns pump + energy-CPI downstream); SPX/vol → HENRY; HY OAS series → LIQUID (read as counter-signal, never double-counted); counter-thesis/red-team → RED; private-credit gate-count → BROCK. **Runs 7 sub-agents** (STUE student-loans / HOMER housing / DOC healthcare / GIG gig / PHAN phantom-debt / POLLY insurance / POP small-biz) + META. **What it's for:** "Is the U.S. consumer cracking, and how fast does the cost/employment squeeze convert into credit deterioration that lands on banks?"

## 2. File anatomy (where the richness lives) — HEAVY, multi-layer (thesis/ + workbook/ + docket/ + handoff/ + sub_agents/)
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (251 ln) | live dashboard — SIGNAL DASHBOARD (4 tables: Credit / Housing-MF / Insurance-Health / Macro-Energy, Value·AsOf·Status), CONVERGENCE MATRIX mirror (14-vector, **52/70**, histogram), THESIS summary, DANGER WINDOW (recently-fired digest, dense), CROSS-AGENT LINKS, PREDICTIONS table, EXIT RULES. **No labeled BOTTOM LINE** (the L5 gap). | live state |
| thesis/THESIS.md (426 ln) | **canonical thesis of record** — "Beneath the Ice" v2.6. Core thesis, What's-Confirmed/Forecast, 5 Load-Bearing Vectors w/ kill-conditions, **Cross-Industry Masking Framework** (4 issuers, meta-pattern, X-thresholds), K-shape Selection + Tariff Transmission siblings (CRL-22/23), **Path C Activation ladder** (provisional→firm→activating), **Path C Bifurcated Timing Axis** (FFIEC 180/120-DPD, CRL-24), **Path PC** (BCRED gate, CRL-25→BROCK), Trade-Duration, Puzzles, full Convergence Score table (downgrade triggers + honest-commentary + upgrade-path + Fast Early-Warning 1-mo Kill), Exit/Invalidation, Open Work Items | the brain — exemplary |
| thesis/PREDICTIONS.tsv (25 preds, CRL-01..25) | live ledger — 2 CONFIRMED / 1 CONFIRMED\* / 2 MISSED / 1 MIXED / **19 OPEN**; Conf + Timeframe + Invalidation + resolution notes (CRL-21/CRL-24 carry position-action commitments) | institutional learning loop |
| thesis/CHANGELOG.md (1282 ln) | audit trail of every version bump (v1.0→v2.6) + prediction change, old→new | history — reference-only, SKIP at grade |
| workbook/KB.tsv (297 rows, LIVE, max KB-CARL-301) | canonical record, 15-col schema — Admiralty digraph (A1-F6) conf + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic + **Delegated_To** (7 sub-agents). 254 ACTIVE / 49 delegated | permanent record |
| workbook/SCHEMA.tsv | col defs for all TSVs (read at boot step 3) | durable method |
| workbook/{VX,FLOW,BNPL_STRESS,STATE_DIFFUSION,TRENDS}.tsv | **FROZEN 2026-06-26** banner — STATUS canonical, do NOT append | frozen ledgers |
| workbook/ABS_BASELINE.tsv | ABS trust baselines — **LIVE** (flagged stale by ledger_staleness, freeze candidate) | live ledger |
| NEXUS_BRIEF.md (74 ln) | cross-agent synthesis twin of SCRATCH — VIEW / CALIBRATION / CROSS-DOMAIN (sending+waiting) / NEXT-DECISION / FORWARD-CATALYSTS. **Mandatory every session** (≥ refresh As-of stamp) | sync surface |
| ROADMAP.md (141) / SCRATCH.md (83) / MEMORY.md (45) | cross-session process state / ephemeral handoff (template-rewritten) / persistent feedback+findings (cap 100) | process memory |
| docket/CATALYSTS.tsv (18) + CALENDAR.md | **single source of truth for forward catalysts** — boot countdown (`docket_countdown.py`), past-due integrate-&-prune flag; TSV↔CALENDAR mirror | forward state |
| board/BOARD_LOG.tsv (325 rows) | WALTER signal-disposition ledger (CARL dispositions BOARD/INDEX signals) | intake ledger |
| TRADE.md (48 ln) | **⛔ RETIRED BY DESIGN (Jun 26)** — transmission-middle agent holds no own book; live expression via REGINALD/HENRY/OZK/FORGE. NOT a gap. | retired stub |
| handoff_RED/ (COUNTER_LOG, SOFT_LANDING, CONTAINMENT, …) | counter-evidence staged for RED. **CARL stages, RED owns — do NOT maintain.** | cross-agent stage |
| handoff_WALTER/LIAISON.md (46k) | append-only CARL↔WALTER routing liaison (Will mediates turns) | liaison |
| scripts/ (boot, docket_countdown, abs_monitor, gas/housing/consumer_pulse, thresholds, catalyst_countdown) | boot scans + domain trackers; `ledger_staleness.py` lives at repo-root /scripts (boot 7d calls it from there — present, not a gap) | tooling |
| sub_agents/ (STUE/HOMER/DOC/GIG/PHAN/POLLY/POP + META) | 7 monitoring agents, each own CLAUDE.md/STATUS/workbook/PREDICTIONS | fan-out depth — SKIP detail |
| archive/ (Ally 10-Ks ~9MB htm ×2, NY-Fed xlsx, PNGs, founding_synthesis, LV-0x, legacy_workbook) | history | SKIP |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | THESIS.md (canonical) + STATUS THESIS summary | "Beneath the Ice" v2.6, 5 Load-Bearing Vectors + Paths A/B/C/F/PC + 3 separated mechanisms (Masking / K-shape Selection / Tariff Transmission) | exemplary |
| Convergence / scoring | THESIS Convergence Score table (canonical) → STATUS matrix (mirror) | 14-vector, 5-pt def (bias-against-5), **composite 52/70**, score histogram, per-vector v2.4→v2.5→current + reason-for-change + downgrade trigger | exemplary |
| Invalidation / exit | THESIS Exit/Invalidation + per-vector downgrade triggers + Fast Early-Warning 1-mo Kill table + Masking falsification windows + Path-C ladder; STATUS EXIT RULES | **deepest falsification loop in the fleet** — thesis-kill (2-condition) + per-vector triggers + 1-month kill table + CRL-20/21 dual windows w/ position-action commitments + CRL-24 pre-registered hard trigger + Path-C provisional/firm/activating operational distinction | exemplary |
| Thresholds | CLAUDE.md KEY THRESHOLDS + STATUS dashboard (live) + PREDICTIONS (full list) + per-vector triggers | named anchors (CC 90+ >13.74%, Fannie MF >0.80%, gas >$4.50, UMich 5-10Y >3.5%, ABS sub-CE breach) w/ implication + source-tag discipline | conformant |
| Predictions | thesis/PREDICTIONS.tsv (canonical) → STATUS PREDICTIONS table (mirror) | 25 preds CRL-01..25, status+conf+timeframe+invalidation; resolved rows carry failure-mode notes (CRL-01/09/19); CRL-21/24 carry **position-action commitments** | exemplary |
| Cross-agent routing | CLAUDE.md CROSS-AGENT SIGNALS matrix + NEXUS_BRIEF CROSS-DOMAIN + outbox/ | condition→target→priority send-matrix; receive-list; NEXUS_BRIEF sending/waiting tables; AGENTS/SIGNALS.md threshold-breach appends | conformant |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** (1) **The falsification loop is the fleet benchmark** — layered: per-vector downgrade triggers + a 1-month Fast Early-Warning Kill table + dual masking windows (CRL-21 intermediate / CRL-20 outer) **with literal position-action commitments** (-25-30pp + trim 25% + extend duration) + CRL-24 pre-registered hard trigger (Q2 monoline prints) + Path-C provisional→firm→activating operational ladder. (2) **3-mechanism discrimination** — masking vs K-shape-selection vs tariff-transmission held *separate* so falsifiability survives (load-bearing scope honest at 4 issuers, not 6, after May-3 external review). (3) **KB Delegated_To** column = 7-sub-agent fan-out ownership, orthogonal to Status — richer than a single-agent KB. (4) **FFIEC-grounded bifurcated timing axis** (180-DPD card / 120-DPD auto un-maskable; extend-and-pretend is CRE-only) = mechanism-grounded, not calendar-guessed. (5) Path PC defers gate-count to BROCK (CRL-25 = pointer, not duplicated trigger) — clean one-source discipline.
- **TRADE.md RETIRED BY DESIGN is NOT a gap** — this is the false-negative the old mechanical "no TRADE.md = sub-L4" scan would flag. CARL is the transmission *middle*; it owns no book; the L4 trade criterion is met via cross-agent routing to REGINALD/HENRY/OZK/FORGE (documented in TRADE.md + Trade-Duration Implications). Grading must read intent, not file-presence.
- **Debt (real, cheap):** (a) **no labeled BOTTOM LINE** — STATUS leads with a dense multi-clause "Updated:" megaparagraph instead; the single L5 handle gap. (b) **consistency_check.py not built** — referenced in CLAUDE.md closeout step 15 as the "Phase-3 enhancement / boot-side auto-scan," but only the *manual* closeout mirror-check exists. (c) **self-doc drift** — CLAUDE.md FILES table (line 238) still calls TRADE.md a "Stub" while the file now carries an explicit ⛔ RETIRED banner. (d) ABS_BASELINE.tsv flagged-stale but still LIVE (freeze candidate — same silent-rot-middle class root-CLAUDE warns on).

## 5. Load-bearing context / DO NOT TOUCH
- **K-shape methodology** — every datum decomposed bottom-60 vs top-40; "aggregate improvement is NOT improvement if the bottom is still deteriorating"; public issuers (SYF/ALLY) carry survivorship bias. Payment hierarchy **Auto→Mortgage→Student→CC**.
- **Masking framework's 3-mechanism separation** (masking / K-shape selection / tariff transmission) — collapsing them re-breaks falsifiability; 4-issuer load-bearing scope (ALLY/COF/SYF-ACL-leg/RITM) is deliberate, not incomplete.
- **Falsification handles**: CRL-20 (Q1'27 outer), CRL-21 (Q3'26 intermediate, position-action), CRL-24 (Axis-A pre-registered hard trigger). Do not re-date without re-deriving.
- **Bifurcated timing axis rule** — Axis A (unsecured monoline, FFIEC-mandated charge-off, un-maskable) is the leading tell but **NEVER a proxy for Axis B** (CRE/regional, extend-and-pretend defers). A monoline-only break confirms A, does not flip B.
- **Frozen ledgers** (VX/FLOW/BNPL_STRESS/STATE_DIFFUSION/TRENDS) — do NOT append; STATUS is canonical. KB.tsv + ABS_BASELINE remain the live ledgers.
- **KB Delegated_To is orthogonal to Status** — never overload (a delegated row keeps its ACTIVE/CONFIRMED state).
- **Doc Ownership mirror pairs** (THESIS matrix↔STATUS matrix; PREDICTIONS OPEN-IDs↔STATUS table; CATALYSTS↔CALENDAR) — canonical wins on drift; closeout step 15 verifies.
- **handoff_RED/** — CARL stages counter-evidence, RED owns it; do not maintain. Counter-narrative belongs to RED at system level.
- **Cede lines**: HY OAS = LIQUID's series (counter-signal, no double-count); labor=LABOR; bank=REGINALD; oil spot=HAWK/BRENT; private-credit gate-count=BROCK.

## 6. Maturity snapshot
**L4 (conf H)** — exemplary on Thesis / Convergence / Invalidation-exit / Predictions; conformant on Thresholds / Cross-agent routing. Both L4 criteria met: trade-feed (via cross-agent routing — TRADE.md retired by design, not a gap) + signals flowing (NEXUS_BRIEF + outbox + SIGNALS.md). Below L5 only on: (1) no BOTTOM LINE handle, (2) consistency_check.py not yet built, (3) CLAUDE FILES-table self-doc drift, (4) ABS_BASELINE freeze-or-refresh. Work queue → `upgrades/CARL_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated).

## 7. Open questions / comprehension gaps
- **No content drift since the grading snapshot.** All CARL-owned files stamp Jun 22-26; every post-6/28 commit touching `AGENTS/CARL/` is WALTER writing CARL's inbox/board, not CARL content. The 6/28 read captured the current Jun-26 state — KB 297 rows, preds CRL-01..25, 52/70 all match exactly.
- CRL-06 metric ambiguity (FC filings vs starts basis) flagged unresolved in ROADMAP — may already be CONFIRMED on starts.
- Is consistency_check.py planned or quietly abandoned? (status of the "Phase-3 enhancement" reference).
- Sub-agent staleness propagation: PHAN/POLLY/POP ~66d stale per TEAM (Jun 22) — possible unpropagated facts in their KBs (not read here; closeout subagent-diff would catch).
