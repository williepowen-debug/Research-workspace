# Agent Profile — BRENT

> Δ **2026-07-22 PRODUCTION REVIEW — named trigger fired; REFRESH-AT-TOUCH (PRIORITY #3 — all 3 trigger legs fired).** Per-agent delta bullets + row re-grade banked in `upgrades/PRODUCTION_REVIEW_2026-07-22.md` (the delta store). Body below is prior-vintage — READ WITH THE DELTAS; full refresh executes at the next firming touch of this agent.

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow `firm7-profiles-cards`; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md, TRADE.md, thesis/{THESIS.md, PREDICTIONS.tsv, PREDICTIONS_ARCHIVE.md (head), CHANGELOG.md (head)}, workbook/{KB.tsv (banner+head), VX.tsv (banner), FLOW.tsv (banner), SCHEMA.tsv}, NEXUS_BRIEF.md, SCRATCH.md, LESSONS.md (head), demand_destruction/TRACKER.md (head), docket/CATALYSTS.tsv (head), board ledgers (head) · **Staleness:** refresh when TRADE.md trade surface, the THESIS version (currently v5.0), or the STATUS convergence matrix materially changes, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
Oil & energy markets — Brent/WTI spot + term structure, crack spreads, OPEC+, Gulf production, global storage (Cushing/SPR/floating), tankers/freight + war-risk, US shale/rigs, demand indicators, energy HY credit. **Class:** Market. **Transmission:** consumes ← HAWK (military ops, Hormuz status, escalation tier — HAWK supersedes on kinetic) and ← MARCO (trade policy); sends → CARL (gas pump/consumer), HENRY (energy CPI/PPI inputs), LIQUID (energy HY-OAS), SAM (Japan LNG/import cost), REGINALD (energy loan exposure), HAWK (oil price + storage for scenario framework), PROME (Cushing/WTI-dislocation tier flag). Cedes military/escalation + A/B/C/D scenario framework to HAWK; gas→consumer to CARL; systemic credit to LIQUID; inflation prints to HENRY; Japan to SAM (one-source-of-truth). **Spawnable by:** PROME / Will. **What it's for:** "What does oil supply/price structure mean for the squeeze→demand-destruction sequencing, and where does it transmit?"

## 2. File anatomy (where the richness lives) — HEAVY, multi-layer (~11MB, research-corpus-dominated)
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (223 ln) | live dashboard: header REGIME BLOCK (v5.0 banner), dated narrative sections (JUN 29 AM kinetic test, JUN 26 PM adjudication), STATE / PATH A-B, STORAGE, PRICE DASHBOARD table, **14-vector CONVERGENCE MATRIX (47/70)**, PREDICTIONS status table, KEY OPEN ITEMS, CATALYST CALENDAR, SUMMARY FOR WILL | live state |
| **TRADE.md (102 ln)** | **NEW canonical trade surface (migrated Jun-29).** CURRENT STANCE v5.0, POSITIONS, ACTIVE TRADE PLAN (convex-arm, deploy-on-trigger, tiered), DORMANT Phase-2 short, DECISIONS ON RECORD, CROSS-AGENT, EXECUTION LOG, CATALYSTS. **LIVE surface (explicitly NOT frozen)** | trade truth (FRESH) |
| thesis/THESIS.md (v5.0, 229 ln) | full thesis: two-phase model + v5.0 asymmetry-flip reframe + **TIMED-RACE core frame** + 4 Transmission Channels + EXIT PROTOCOL + KEY THRESHOLDS + RISK FACTORS skew table + version-history footer | exemplary |
| thesis/CHANGELOG.md (72 KB) | full version audit trail (vX.Y, old-view→new-view per entry) | rich / institutional |
| thesis/PREDICTIONS.tsv (54 rows, 10-col) | **Calibration Record** — live ledger + scoreboard preamble (running tally, DIRECTIONAL-FAILURES, CALIBRATION-FINDINGS-by-class, PRE-FLIGHT CHECK) | **exemplary (best-in-fleet)** |
| thesis/PREDICTIONS_ARCHIVE.md (26 KB) | per-prediction blow-by-blow post-mortems w/ calibration notes (not boot-loaded) | learning loop |
| workbook/KB.tsv (160 ln incl banner) | **FROZEN/ARCHIVAL historical corpus (frozen 6-14)** + durable structural-reference keep-clusters; 13-col schema, Admiralty digraph (A-F/1-6) + EMPIRICAL/ESTIMATE/ASSUMPTION tags | frozen record (the FROZEN-banner MODEL) |
| workbook/{VX,FLOW}.tsv | **FROZEN/ARCHIVAL (frozen 6-14)** — VX→live successor STATUS matrix; FLOW→live successor CLAUDE.md cross-feed tables + THESIS channels | frozen (banner model) |
| workbook/SCHEMA.tsv (14 ln) | the 13-col KB schema definition (controlled vocab refs) | reference |
| demand_destruction/TRACKER.md (46 KB) | **LIVE operational dashboard** — Path-A/B trigger states, EIA weekly alerts, ROUTING-boundary fires | rich / live |
| demand_destruction/{ANALOGS,HAMILTON,HOARDING,TRANSITION_MATRIX,MATRIX_REVIEW}.md | demand-destruction research corpus (Mar-Apr vintage, mostly static) | deep / mostly static |
| docket/CATALYSTS.tsv (19 rows, 8-col) | canonical forward-state; FASTOW sub-agent maintains | forward state |
| docket/{FASTOW,FASTOW_MEMORY}.md | catalyst-maintenance sub-agent (spec + memory) | sub-agent |
| refinery_damage/INCIDENTS.tsv (35 rows) | energy-infra strike ledger (facility-damage only; mil-ops→HAWK) | live-ish |
| NEXUS_BRIEF.md (v5.0) | cross-agent synthesis brief (SENDING / WAITING-FOR tables) — the primary cross-agent surface now | sync |
| SCRATCH.md / LESSONS.md / MEMORY.md | session handoff / numbered lessons (#1-19+) / persistent learnings (small) | ephemeral / learning |
| CLAUDE.md (17 KB) | agent instructions; symmetric boot↔closeout (read→write-back pairing) | instructions (has stale threshold table — §4) |
| scripts/ (boot.py, eia_weekly.py, thresholds.py, catalyst_countdown.py, refiner_ratios.py) | live-data + EIA + threshold tooling | tooling |
| research/ (11 MB, ~30 files, Mar-17 vintage + 3 .docx ~3.4MB ea) | deep one-time research corpus | **SKIP (huge, static)** |
| archive/, recon/, design/, handoff_WALTER/, board/, workbook/STATUS_archive_*, KB_old_6col.tsv, PHASE2_EXECUTION, SIGNAL_INTAKE, LAST_COMPLETION | history / handoff / retired | **SKIP** |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | thesis/THESIS.md + CHANGELOG.md | two-phase model (squeeze→demand-destruction), v5.0 "asymmetry-flip" reframe, **TIMED-RACE core (deficit-closing clock vs buffer-exhaustion clock)**, 4 Transmission Channels, full vX.Y audit trail | exemplary |
| Convergence / scoring | STATUS CONVERGENCE MATRIX | 14-vector, emoji+number (1-5) with ↓ trend arrows, composite **TOTAL 47/70** (unch vs Jun-26), "measures the transition, not a crisis" | strong (VX.tsv is its frozen predecessor) |
| Invalidation / exit | THESIS EXIT PROTOCOL + RISK FACTORS table + TRADE.md arm/disarm | Path-A operational-gate table (7 criteria) + Path-B 3-trigger table + SHORT PLAYBOOK (demoted to conditional) + tiered convex-arm triggers + **"thesis break REDEFINED" bidirectional flip** ("<$75=break" RETIRED→decoupling; >$75×2 re-arms up; <$70-on-demand revives short) | **exemplary — blueprint's NAMED source for §4 bidirectional-flip exit** |
| Thresholds | THESIS KEY THRESHOLDS (live) + CLAUDE.md KEY THRESHOLDS (durable) | level / significance / status-emoji split; durable-vs-live separation | conformant — but CLAUDE.md copy DRIFTED (§4) |
| Predictions | thesis/PREDICTIONS.tsv + PREDICTIONS_ARCHIVE.md + CHANGELOG | BRT-xx IDs; 10-col (Pred_ID/Date_Made/Prediction/Confidence/Timeframe/Status/Date_Resolved/Outcome/**Invalidation**/Notes); scoreboard preamble splits calibration by prediction-CLASS (chokepoint=under-confident, industrial-transmission=over-confident, n=2) + PRE-FLIGHT CHECK | **exemplary (exceeds blueprint)** |
| Cross-agent routing | CLAUDE.md NETWORK CONNECTIONS + THESIS CROSS-AGENT LINKS + NEXUS_BRIEF SENDING/WAITING-FOR | direction→agent→flow→priority; NEXUS_BRIEF is the live steady-state surface; outbox reserved for 🔴 acute only | strong |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** (1) **PREDICTIONS = best-in-fleet calibration loop** — scoreboard splits accuracy by prediction-CLASS with explicit anchor ranges (under-confident on chokepoint/storage 80-95%; over-confident on industrial-transmission 40-55%) + a 3-question PRE-FLIGHT CHECK gating the next prediction. (2) **KB/VX/FLOW = the fleet's FROZEN-banner MODEL** — each carries a dated `ARCHIVAL (frozen 2026-06-14)` banner + per-row DISPOSITION rules + explicit LIVE-SUCCESSOR pointers (no silent-rot middle; root-CLAUDE hygiene done right). (3) **Bidirectional-flip exit** — THESIS is the blueprint's NAMED source for §4 exit logic (level reinterpreted not just breached: same <$75 print = "break" under v4, "decoupling" under v5; symmetric up-arm vs down-revival). (4) **TIMED-RACE frame** — two named clocks (deficit-close vs buffer-exhaust) gating near-term-robust vs medium-term-whipsaw. (5) **demand_destruction/TRACKER.md** = a live operational dashboard beyond the STATUS surface.
- **Structural quirk (EQUIVALENT, not debt):** BRENT's **KB.tsv is FROZEN/archival, NOT the live canonical record** (unlike BROCK). The live "canonical record" function is SPLIT across STATUS + demand_destruction/TRACKER.md + thesis/PREDICTIONS*. A scripted L0-L2 scan that assumes "KB.tsv = live record" will mis-grade this — it's a deliberate demotion, not rot.
- **6/28 false-negatives the mechanical scan made:** PAT-023 flagged "TRADE.md 111d stale, no FROZEN banner" — **now RESOLVED** (TRADE.md wholesale-rewritten Jun-29, commit ~6b4f99ef, to the live v5.0 surface + wired into boot/closeout; correctly a **LIVE** surface, NOT frozen — so the original "needs a FROZEN banner" framing was itself wrong for a trade surface). The uppercase-`FROZEN` grep also MISSES the lowercase `frozen`/`ARCHIVAL` banners on KB/VX/FLOW — a literal banner-detector false-negative.
- **Real (small) debt:** (a) **CLAUDE.md KEY THRESHOLDS table still says "Brent <$75 = Thesis break — squeeze failed"** — contradicts v5.0 (sub-$75 = structural decoupling); the instructions-file threshold copy drifted behind THESIS. (b) CLAUDE.md DOMAIN SCOPE still lists stale positions ("USO 2sh + STNG 2sh"). (c) PREDICTIONS.tsv scoreboard preamble stamped "As of 2026-06-20" (~9d stale; BRT-08 DUE Jul-1). (d) `LAST_COMPLETION.md` is explicitly RETIRED (SCRATCH replaces it) but the May-04 file still sits in the dir un-archived. (e) `board/BOARD_LOG.tsv` (57 rows, May-05) appears dormant vs the live `board_log.tsv` (WALTER lane, Jun-29) — silent-rot-middle candidate (freeze-or-confirm).
- **Closure note (2026-07-12):** Independence col applied 7/10 (BATCH_03 #1 closed); <$75 threshold line fixed 7/12.

## 5. Load-bearing context / DO NOT TOUCH
- **TRADE.md is the canonical trade surface (Jun-29 migration)** — positions / trade plans / arm-triggers / execution-log live HERE, not STATUS (STATUS keeps a 1-line pointer). It is a **LIVE** surface — do NOT freeze-banner it; it must be refreshed every closeout or it rots (it sat Mar→Jun stale once).
- **The v5.0 SKEW-vs-DIRECTION guardrail** — "asymmetry flipped UPSIDE-CONVEX" is a *positioning/skew* reversal, NOT a price-forecast call ("we are NOT calling oil up; the convexity is up, not the forecast"). Any edit that collapses this into "BRENT is bullish oil" breaks the thesis.
- **TIMED-RACE frame** (deficit-closing vs buffer-exhaustion; near-term-robust / medium-term-whipsaw-gated-on-reopening; price is the LAGGING tell, leading tells = reopening 2nd-derivative + P&I resumption + floating-storage builds).
- **FROZEN-banner discipline on KB/VX/FLOW** — banners + per-row DISPOSITION + LIVE-SUCCESSOR pointers must survive any workbook touch; these are the fleet template.
- **PREDICTIONS calibration scoreboard** — the by-class anchor ranges + DIRECTIONAL-FAILURES + PRE-FLIGHT CHECK feed the next prediction; don't flatten to a bare ledger.
- **Bidirectional-exit semantics** — sub-$75 = decoupling (not break); real break = reopening-completes-and-grinds-to-~$79 (skew was wrong) OR <$70-on-DEMAND-collapse (revives short). The Phase-2 SHORT is DEMOTED-to-conditional, not deleted.
- **One-source-of-truth cessions** — HAWK owns scenario %s + kinetic (BRENT owns the price mapping); LIQUID owns HY-OAS; HENRY owns CPI prints; STATUS owns live prices; THESIS owns conviction; TRADE owns position status.
- **NEXUS_BRIEF is the live cross-agent surface** (outbox is 🔴-acute-only) — keep SENDING/WAITING-FOR fresh at closeout.
- **Admiralty digraph + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic tagging** in KB (per SCHEMA.tsv).

## 6. Maturity snapshot
**L4 (conf H)** — adversarially confirmed 6/28; **STRENGTHENED since.** Conformant-or-exemplary on all 6 market dimensions; exemplary on Predictions (best-in-fleet), Thesis, Exit (blueprint's named source), FROZEN-banner hygiene. Both L4 criteria met (TRADE.md feeding live convex-arm proposal + signals flowing via NEXUS_BRIEF). **The principal 6/28 L4→L5 blocker (stale trade-position surface, PAT-023) is RESOLVED** by the Jun-29 TRADE.md migration — BRENT now sits closer to L5 than the BROCK profile of the same vintage. Below L5 only on small residual debt (§4d/e: CLAUDE.md stale threshold + position lines, scoreboard date-stamp, retired-LAST_COMPLETION present, board/BOARD_LOG silent-rot candidate) and no zero-YEYOU clean bill. Work queue → `upgrades/BRENT_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated).

## 7. Open questions / comprehension gaps
- Is XLE $65C Sep-30 the actual current book vs `WILL/trading-journal/` (broker truth)? STATUS/TRADE both say LAPSE/deep-OTM, but cost-basis/marks are non-authoritative from state files — verify against the journal, never STATUS.
- `board/BOARD_LOG.tsv` (57 rows, May-05) — live, dormant, or superseded by `board_log.tsv`? Resolve freeze-vs-confirm before any L5 claim.
- PREDICTIONS scoreboard tally ("As of 2026-06-20") — refresh owed after BRT-08 resolves Jul-1; the calibration math is ~9 days behind.
- Is the demand_destruction research corpus (ANALOGS/HAMILTON/HOARDING/TRANSITION_MATRIX, Mar-Apr) still consulted, or a >60-day archive candidate? (TRACKER.md is the live successor.)
- `scripts/ledger_staleness.py` (boot step 5a, "wired Jun-27") is MISSING — STATUS + SCRATCH both flag it to PROME; not yet confirmed built.
