# CARL ROADMAP — "Where are we"
**Updated:** 2026-05-02 (workbook restructure — full compliance with "TSVs only" rule + AAA pump $4.433 daily refresh) | **Status:** ACTIVE

Persistent state-of-CARL tracker across sessions. SCRATCH = "what to do next session." STATUS = "live dashboard." ROADMAP = "what threads are open, what data are we waiting on, what questions are unresolved, what we want to investigate next, what just got done."

**Maintenance discipline:** Updated at session end before commit. If a thread is moved to RESOLVED, that's the audit trail of what each session shipped.

---

## OPEN THREADS
*Active work spanning multiple sessions. Each entry: what / status / next step / last-touched.*

| Thread | Status | Next Step | Last Touched |
|--------|--------|-----------|--------------|
| **v2.5.1 hardening — 9 PENDING_VERIFY items** | NEW May 1 PM2 from v2.5 promotion. (1) UMich triangulation TIPS 5y5y / SPF / NY Fed 3yr → V12 hardens or caveats. (2) Foreclosure 2019 absolute baseline → V10 base-effect caveat resolved. (3) Path C COF/SYF Q1'24/'25 ACL counterfactual → provisional → firm or → ACTIVATING-RED. (4) Crying-wolf X-thresholds standalone working doc. (5) Brier audit full prediction history. (6) CONTAINMENT prior-calibration audit (joint CARL-RED). (7) COF/SYF candor puzzle (RED handoff). (8) Trade duration roll plan (FORGE/REGINALD coord on KRE/WAL Dec 2026 → Q1-Q2 2027). (9) RED-CARL interface protocol document. | Sequence: items 1-3 (data) before item 5 (Brier audit). Items 4 + 9 (working docs) can run parallel. Items 6-8 require RED activation or cross-agent coordination. | 2026-05-01 |
| **Diesel divergence — freight demand destruction signal** | NEW Apr 29 PM2. Diesel $5.464 DOWN -$0.144 over 16d while Brent rose 12.5% (KB-CARL-253). Vector #9 qualitative reinforcement candidate. | 4-week sustainability test: track ATA truck tonnage, Cass Freight Index, EIA distillate stocks (Wed weekly), refinery utilization. If sustained 4+ weeks while Brent stays $100+ → thesis-level note + Vector #9 reinforcement. | 2026-04-29 |
| **Apr 26-28 PENDING catalysts** — all surface-resolved | FL UI Wave 2 PARTIAL May 1: surface initial claims declining (counter-thesis on surface), but exhaustion mechanism invisible in initial claims; granular DEO + DOL ETA = LABOR/GIG spawn (KB-CARL-262). Rithm + Case-Shiller fully resolved (KB-CARL-257, 261). | LABOR/GIG spawn for FL UI Wave 2 deeper analysis on next mechanical session OR May 8 NFP trigger. HOMER full Case-Shiller sub-market deferred to next housing spawn. | 2026-05-01 |
| **Workbook refresh — multiple TSVs 12d stale** | VX (109 rows), FLOW (22), STATE_DIFFUSION (63), BNPL_STRESS (44) all last touched Apr 17. STATE_DIFFUSION specifically should fold KB-CARL-249 (FL labor weakness) on next pass. | Single dedicated maintenance session — refresh all four together, fold pending KB references into appropriate vector rows. | 2026-04-17 |
| **ABS_BASELINE refresh — March 10-D filings** | 13d stale (Apr 16). March 10-D filings (Apr 20-25 window) for SDART/EART/AMCAR/HAROT/Ally not yet collected. EART Class E CE already breached; AMCAR Class E ~2mo cushion. | Dedicated EDGAR pull session — collect March 10-Ds, update ABS_BASELINE.tsv, flag any new breaches to LIQUID. | 2026-04-16 |
| **CRL-08 near-breach — gas $4.50 May-Jun** | Pump $4.392 May 1 live (KB-CARL-259), **CRL-08 reprice 78→92%**. Gap to threshold $0.108; at overnight pace breaches May 2-3, weekly pace by May 4-5. Pass-through ACCELERATED (3-4d vs 2-4wk typical lag). Sustainability test = whether Brent holds $107+ AND no demand destruction at $4.50+. | Daily AAA tracking until breach; weekly EIA Wed inventory; if breach holds 2+ weeks → CRL-08 CONFIRMED, possible Vector #5 thesis upgrade to "STRESSED + STRUCTURAL" sub-tier. | 2026-05-01 |
| **Sub-agent staleness — DOC 8d borderline** | DOC last refreshed Apr 9 (now 21d if recalc). All other 6 sub-agents fresh from Apr 17 burst. | DOC refresh on next ACA enrollment / KFF survey trigger; otherwise hold. | 2026-04-17 |

---

## AWAITING DATA
*Known external prints with dates. Order = chronological.*

| Date | Item | Test / Implication |
|------|------|-------------------|
| **May 5** | PayPal Q1 (PHAN) — SCHEDULE CORRECTION May 1 (actual release May 5, was incorrectly listed as Apr 29/30 in earlier trackers) | First print under new CEO Lores. Consensus EPS $1.27 (-4.5% YoY), revenue $8.29B (+14.4% YoY). |
| **May 1 (today)** | ALL Q1 (POLLY) | P&C, complements PGR/TRV. |
| **May 1 (today)** | ISM Manufacturing Apr (POP/CARL) | Sub-50 = contraction confirmation. |
| **May 28** | BEA GDP Q1 2026 second estimate | Revision risk -0.2 to -0.4pp per pattern (Q4 1.4→0.7→0.5). |
| **~May 30** | March monthly core PCE | Bridge test: should accelerate from Feb 3.0% YoY toward 3.3-3.5% to be consistent with Q1 NIPA 4.3% annualized. |
| Late Apr | Fannie MF March DQ (HOMER) | **CRL-03 GFC breach test** (0.74 → 0.80%?). |
| Late Apr / early May | PennyMac Q1 (CARL direct) | FHA DQ >7.5%? Cenlar integration. |
| May 6 | Uber Q1 + DoorDash Q1 (GIG) | Driver count QoQ post-gas-squeeze. |
| May 6 | BLS state jobs March | FL labor confirmation/extension test (KB-CARL-249 follow-up). |
| **May 7 TRIPLE** | Dave Q1 + Lyft Q1 + Affirm Q3 FY2026 | 28DPD GIG-P01 + ALLY analog test. |
| May 8 | BLS Apr NFP (LABOR/CARL) | Goldman 10K-jobs/mo framework first realized print. |
| ~May 18 | Klarna Q1 2026 (PHAN) | First full quarter post-FY-loss. |
| May 28 | AFT/MOHELA status conference (STUE) | Discovery progress. |
| ~Mid-May | NY Fed Q1 2026 HHDC | **CARL CORE — CC 90+ DQ Q1 update vs 12.7%; tests CRL-05 mechanism shift.** |
| Jun 24 | FL Wave 1 UI exhaustion cliff | DQ spike follows 30-60d. |
| Q2-Q3 | ABS subordinate rating actions | EART Class E + AMCAR Class E + SDART Class D. |
| Jul 1 | **SAVE → RAP transition** (STUE) | 7.5M forced into new plans, payment shock for non-selectors. |
| Jul-Aug | FL + national UI exhaustion peak | $7.4M/mo FL + $800-930M/mo national spending hole. |

---

## OPEN QUESTIONS
*Flagged but not actively worked. Decide before next acting on them.*

| Question | Surfaced | Action Owed |
|----------|----------|-------------|
| **POP correction** — 125-145% China IEEPA pre-ruling rate is wrong; should be ~20%. | Pre-Apr 17 | On next POP spawn, correct in POP/STATUS or KB. |
| **CRL-06 metric ambiguity** — "70K/qtr foreclosures" — starts vs filings vs REO? Q1 ATTOM 82,631 starts already breaches if starts-basis. | Apr 17 | Clarify metric; if starts-basis → mark CONFIRMED. |
| **6 outbox signals from Apr 17 still undelivered** | Apr 17 | Defer per messaging-overhaul direction (don't patch HERMES). Will be replaced by new system. |
| **SoFi 2025-1 CNL 2.6% triggered** — no SEC path (private/144A), can't refresh via abs_monitor. | Mar 2026 (KB-078) | Accept as snapshot-only; flag if Eisman / industry source provides update. |
| **Convergence score calibration** — 58/60 is subjectively scored. What would 30/60 look like? | Mar 31 (legacy) | Low priority. Important for intellectual honesty if conviction holds long. Each vector needs explicit downgrade criteria. |
| **Counter-evidence rigor** — currently just COUNTER_LOG.md (running log). | Mar 31 (legacy) | Low priority. Old red_team/ structure had competing hypotheses; consider rebuild at sustained high conviction. |
| **TRENDS (26d) / ML.tsv (25d) refresh OR retire** | Apr 17 | Low priority — non-load-bearing. **Surfaced May 2 during workbook restructure:** CARL CLAUDE.md explicitly calls `ML.tsv` "legacy data log" — open question whether to fully retire (move to archive/) since its ancestors (ML_old_9col, ML synthesis MDs, S2_ADDITIONS) are now archived. If kept, refresh; if not actively used, archive next pass. |

---

## INVESTIGATIONS BACKLOG
*Research / deep-dive ideas not yet started. Each: what / why / scope. Pull from here when there's a research session and no urgent catalyst.*

| Topic | Why interesting | Scope |
|-------|-----------------|-------|
| **Non-bank servicer stress map beyond PennyMac/loanDepot** | Lakeview 18%, Freedom 15.5%, Mr. Cooper, Carrington — DQ stale, advance-expense trajectory unclear. GAO flagged 35% high-debt, no stagflation test. MFS UK collapse = warehouse contagion template. Weakest links matter for Ginnie advance drain thesis. | Medium (1 session, 2-3 sub-agents) |
| **K-shape upper-cohort quantification** | We claim "K-shape CONVERGING downward" with anecdotes (Dollar Tree +6.5M HH from >$100K, RV market collapse, retail investor withdrawal). Want a quantified magnitude — what % of top-40% is materially pulling back, and how does that compare to 2008 wealth-effect pullback? | Deep (multi-session synthesis) |
| **Freight demand destruction framework** | Diesel divergence (KB-CARL-253) is the trigger. Build a working framework: which freight indicators lead, by how much, and at what scale do they produce visible consumer-credit transmission? Cass / ATA / class-1 rail / port volumes / Schneider-J.B. Hunt earnings. | Medium |
| **Phantom debt $400B+ better quantification** | Current estimate is wide ($150-400B BNPL/cash advance/medical). Methodology mostly-extrapolation. Want a tighter range with explicit error bars and sensitivity to BNPL dataset choice. Affirm/Klarna/Sezzle/PayPal Pay-in-4 + earnin/Dave/MoneyLion + medical. | Deep (PHAN owns; CARL synthesis) |
| **ABS terminal-CNL framework — AMCAR / HAROT / Ally** | Already have EART (32.3%), SDART (17.6%), AMCAR (14.5%) — but Honda and Ally Class E baselines not modeled. Q3-Q4 rating actions imminent on subordinate tranches; want explicit forecast curves. | Medium |
| **Tricolor MTB ABS 2nd-channel implications for CARL** | REGINALD primary, but the auto-fraud→ABS-2nd-channel pattern has consumer-credit implications: did the borrowers actually exist? Does it expand the subprime-auto fraud-vintage we've been tracking via CVNA? | Quick (1 session research fork) |
| **Sun Belt structural housing weakness — cycle dynamics** | Zillow 35.5% top-200 falling YoY (post-pandemic high). Realtor.com -2.3% SQFT 13-week streak. Sun Belt overweight in declines = direct overlap with KRE/WAL/OZK geo. Want: is this 2008-analog or different mechanism (insurance + climate + over-build)? | Deep (HOMER + MARCO joint) |
| **FL Triple Squeeze full force-of-impact model** | Vector #7 is at 4 with energy + HOA + insurance components. No quantitative model of how it transmits to bank credit (FL deposit base, mortgage book, CRE concentration). MARCO has migration; we have consumer cost; REGINALD has bank-side — needs joint synthesis. | Deep (cross-agent) |
| **$4.50 demand destruction empirical curve** | We assume "demand destruction at $4.30+" caps gas pump moves. Is there an actual consumer-behavior step-function, and where? VMT data, gasoline consumption, Visa/MC card data, GasBuddy panel. Would tighten CRL-08 ceiling logic. | Quick-Medium |
| **Subchapter V +67% structural mapping** | Sub-V breach Apr 17 captured via NFIB. But: which sectors / sizes / states are concentrated? Tariff exposure overlap? POP has the framework but no granular cut. Would feed into REGINALD SB-provision Q2 prediction (CRL-16). | Medium (POP primary) |

---

## RECENTLY RESOLVED
*Last ~2 weeks. Top of mind so the audit trail is visible without reading commits.*

| Date | What | Result |
|------|------|--------|
| 2026-05-02 | **Workbook restructure — full compliance with CLAUDE.md "TSVs only — no prose" rule.** Workbook 31 → 9 files (only the 9 canonical TSVs remain: KB, VX, FLOW, ABS_BASELINE, BNPL_STRESS, STATE_DIFFUSION, SCHEMA, TRENDS, ML). 22 files relocated across 3 phases. Phase 1A (trash, 2 files): `ML_old_9col.tsv` (true duplicate of ML.tsv with supersession notes), `CARL_MLFLFLOWVX_S6.xlsx` (Excel predecessor). Phase 1B (archive/snapshots, 3 files): `VX_HISTORY.tsv` (Jan-Feb 2026 first-read snapshot), `CARL_ML_S2_ADDITIONS.tsv` (founding NICK/POLLY/PHANTOM/Beneath-the-Ice synthesis entries), `CARL_ML_MARCO_TRANSFER_FOOD.tsv` (Jan 22 MARCO domain transfer record). Phase 1C (archive/status, 2 files): two STATUS archives (Mar 1-15, Mar 25). Phase 2 (Tier 3 prose MDs, 14 files via cluster disposition): (a) ABS framework cluster + SDART baseline (5 files) → `domain/sources/ABS/`; (b) `STATE_STRESS_FRAMEWORK.md` → `domain/sources/`; (c) Trade analyses Feb 16 (2 files) → `archive/trade_analyses/`; (d) ML synthesis cluster ML-CARL-01..06 (6 files) → `archive/founding_synthesis/`; (e) `ML-CR-18_PHANTOM_DEBT_ANALYSIS.md` → `domain/sources/`. Atomic edits: `domain/sources/ABS/README.md` 4 path refs fixed (was pointing to nonexistent `domain/workbook/`); `sub_agents/PHAN/CLAUDE.md` ML-CR-18 path updated. Verified: zero remaining broken `workbook/<moved-file>` references repo-wide. Also: `archive/reviews/` created earlier in session for two thesis-thoughts files (v2.5 r1/r2 review docs Will dropped). Note: 2 OTHER broken paths in ABS README (`domain/workbook/VX.tsv`, `domain/workbook/FL.tsv` — FL.tsv doesn't exist) left alone, out of scope for this pass. |
| 2026-05-02 | AAA pump daily refresh — $4.433 May 2 (+4.1¢ overnight; pace decelerated from May 1 +9.2¢, partial Saturday calendar effect) | Gap to CRL-08 $4.50 collapsed $0.108 → $0.067; breach now ~May 4. Diesel $5.627 (+16.3¢) — diesel divergence narrowing; KB-CARL-253 freight-demand thread weakening. KB-CARL-264 added; VX-CARL-GAS-01 + STATUS gas pump row updated. CRL-08 stays 92% (reprice to 95%+ deferred until threshold-cross + 2-wk sustainability test). Data caveat: AAA top-state list returned East-Coast-only — fetch parse anomaly, headline corroborated by WoW/MoM/YoY internal consistency. |
| 2026-05-01 PM2 | **THESIS v2.5 PROMOTED TO CANONICAL** (commits 1faf70ce + ca003039) | 3 structural changes: (1) Cross-industry data masking promoted KB-225 → thesis-level methodology with CRL-21 Q3'26 + CRL-20 Q1'27 falsification windows. (2) Path C ACTIVATING-RED → ACTIVE-RED (PROVISIONAL pending COF/SYF Q1'24/Q1'25 ACL counterfactual). (3) Convergence matrix expanded 12→14 vectors with rescaled 5-definition; V8+V9 merged; V13/V14/V16 added; V15 dropped (RED domain); V2 strict-def 5→4; multiple other 5s rescaled. Score 58/60 → **53/70 (76%)** — ~60% calibration + ~40% legitimate conviction reduction; prior was probably overconfident. Architectural realignment: Counter-Evidence section stripped, staged for RED in handoff_RED/. red_team/ folder also moved (commit 3d0bdf75). KB-CARL-263 logged. 9 PENDING_VERIFY items queued for v2.5.1. Drafted in 3 revisions (r1/r2/r3) with 2 rounds of external review feedback. |
| 2026-05-01 | Apr 30 GDP Q1 advance integration | Real GDP +2.0% (above 1.3% GDPNow, below 2.3% cons). PCE Q1 NIPA +4.5% / core +4.3% data-confirms UMich un-anchoring → **Vector #12 HARDENED**. Q4 2025 revised down 0.7→0.5%. Composition K-shape (residential drag, healthcare-led PCE, AI capex driver). Full workbook discipline: KB-CARL-254/255/256 + VX MACRO-01 refresh + MACRO-04 real-wage correction + MACRO-07 Core PCE NIPA new + CRL-18 (Q1 second-est revision) + CRL-19 (Mar monthly Core PCE bridge). |
| 2026-05-01 | Rithm/NewRez Q1 2026 (Apr 28 release, 3-day catch-up) | Prior mgmt claim "DQ will reverse Q1" QUIETLY DROPPED. Replaced with "stable QoQ + FHA flatten via FHA modification guidelines normalization" (Silverstein). Servicer advances -$224M / -7.3% QoQ. MSR mark losses halved -$422M → -$204M. BV $12.51. Origination $15.5B (+31% YoY). **Bear case INTACT w/ 12-24mo mod-accounting cushion caveat.** Non-bank servicer stress framework REINFORCED — PennyMac FHA DQ 7.5% remains cleaner stress proxy. Vector #10 unchanged. KB-CARL-257. |
| 2026-05-01 | Live Brent/WTI/AAA pump refresh + CRL-08 reprice 78→92% | Apr 30 Brent intraday $126 NEW HIGH; May 1 pullback $107-110 on Iran peace proposal + Trump WPR 60-day deadline today. AAA pump $4.392 May 1 (+9.2¢ overnight, +33.3¢ WoW, +37.7% YoY). Gap to $4.50 threshold $0.108 — breaches May 2-5. Pump pass-through ACCELERATED (3-4d vs 2-4wk lag). **CRL-08 78→92%.** Vector #5 intensity reinforced (already 5/5); Vector #12 energy-CPI loading reinforced. KB-CARL-258 (Brent path) + KB-CARL-259 (pump acceleration) + VX-CARL-GAS-01 added. |
| 2026-04-29 PM2 | AAA gas pump live refresh + diesel divergence finding | Pump $4.229 confirmed CRL-08 reprice on track. NEW K-shape finding: diesel falling while gasoline rises = freight demand destruction (KB-252/253). |
| 2026-04-29 AM | CRL-08 reprice 65→78% on Brent breakout | $110.38 close / $115 intraday, ceasefire-binary fired into "breaks" branch. KB-CARL-248. |
| 2026-04-29 AM | Apr 21 quadruple earnings synthesis (SYF/COF/UNH/DHI) | K-shape WIDENING confirmed three independent ways. CRL-12 repriced 77→55% on SYF survivor-pool. KB-CARL-243-247. |
| 2026-04-29 AM | 50-signal BOARD disposition pass | 5 INTEGRATED, 13 INFO_ONLY, 32 REFERRED. KB-CARL-249 (FL labor), 250 (housing prices), 251 (farm bankruptcies). BOARD_LOG synced through Apr 29. |
| 2026-04-29 AM | UMich April Final 49.8 + 5-10Y inflation 3.5% (un-anchoring deeper) | KB-CARL-241. STATUS dashboard updated. |
| 2026-04-19 PM | BOARD pull synthesis — Iran day-cluster, Qatar LNG, MS counter-frame | KB-CARL-234/235/236. Vector #5 reinforced; counter-evidence logged. |
| 2026-04-17 PM | ALLY Q1 composition-masking framework | FY24/25 10-K audit: S-tier 40→37%, nonprime 9.7→10.1%, ACL -$224M/-6%. Composition-masking, not fraud. CRL-05 85→82%. KB-CARL-222-228. |
| 2026-04-17 | Sub-agent buildout completion | All 7 monitoring sub-agents BUILT and refreshed. POLLY + POP final adds. |
| 2026-04-16 | ATTOM Q1 foreclosure pull | 118,727 filings (+26% YoY), Q1 REO 14,020 (+45% YoY), FL Q1 REO +108% nationally greatest. Vector #10 upgraded 4→5. |
