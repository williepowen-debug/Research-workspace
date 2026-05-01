# CARL ROADMAP — "Where are we"
**Updated:** 2026-04-30 (rebuilt from session state) | **Status:** ACTIVE

Persistent state-of-CARL tracker across sessions. SCRATCH = "what to do next session." STATUS = "live dashboard." ROADMAP = "what threads are open, what data are we waiting on, what questions are unresolved, what just got done."

**Maintenance discipline:** Updated at session end before commit. If a thread is moved to RESOLVED, that's the audit trail of what each session shipped.

---

## OPEN THREADS
*Active work spanning multiple sessions. Each entry: what / status / next step / last-touched.*

| Thread | Status | Next Step | Last Touched |
|--------|--------|-----------|--------------|
| **Diesel divergence — freight demand destruction signal** | NEW Apr 29 PM2. Diesel $5.464 DOWN -$0.144 over 16d while Brent rose 12.5% (KB-CARL-253). Vector #9 qualitative reinforcement candidate. | 4-week sustainability test: track ATA truck tonnage, Cass Freight Index, EIA distillate stocks (Wed weekly), refinery utilization. If sustained 4+ weeks while Brent stays $100+ → thesis-level note + Vector #9 reinforcement. | 2026-04-29 |
| **Apr 26-28 PENDING catalysts** — three deferred from earnings cluster | FL UI Wave 2 / Case-Shiller Feb / Rithm-NewRez Q1 all still ⏳ in Danger Window. Rithm has falsifiable mgmt claim ("DQ will reverse Q1") + 18% Ginnie exposure. | Triage in next session: Rithm first (CARL direct, highest signal value), then Case-Shiller (HOMER), then FL UI Wave 2 (LABOR/GIG). | 2026-04-29 |
| **Workbook refresh — multiple TSVs 12d stale** | VX (109 rows), FLOW (22), STATE_DIFFUSION (63), BNPL_STRESS (44) all last touched Apr 17. STATE_DIFFUSION specifically should fold KB-CARL-249 (FL labor weakness) on next pass. | Single dedicated maintenance session — refresh all four together, fold pending KB references into appropriate vector rows. | 2026-04-17 |
| **ABS_BASELINE refresh — March 10-D filings** | 13d stale (Apr 16). March 10-D filings (Apr 20-25 window) for SDART/EART/AMCAR/HAROT/Ally not yet collected. EART Class E CE already breached; AMCAR Class E ~2mo cushion. | Dedicated EDGAR pull session — collect March 10-Ds, update ABS_BASELINE.tsv, flag any new breaches to LIQUID. | 2026-04-16 |
| **CRL-08 sustainability — gas $4.50 May-Jun** | Pump $4.229 Apr 29 live (KB-CARL-252), 78% reprice on track inside model (gap $0.27, pace $0.21/30d). Brent $110+ sustainability is the swing factor. | Weekly AAA refresh; track Brent sustainability; Memorial Day (May 25) seasonal premium adds $0.10-0.15 organically. | 2026-04-29 |
| **Sub-agent staleness — DOC 8d borderline** | DOC last refreshed Apr 9 (now 21d if recalc). All other 6 sub-agents fresh from Apr 17 burst. | DOC refresh on next ACA enrollment / KFF survey trigger; otherwise hold. | 2026-04-17 |

---

## AWAITING DATA
*Known external prints with dates. Order = chronological.*

| Date | Item | Test / Implication |
|------|------|-------------------|
| **Apr 30** | **GDP Q1 advance (BEA 8:30am ET)** | vs GDPNow Q1 1.3% (Apr 7 anchor). Print materially below → hardens Vector #12 (Stagflation Trap). |
| Apr 30 | PayPal Q1 (PHAN) | First print under new CEO Lores. |
| May 1 | ALL Q1 (POLLY) | P&C, complements PGR/TRV. |
| May 1 | ISM Manufacturing Apr (POP/CARL) | Sub-50 = contraction confirmation. |
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
| **TRENDS (23d) / ML (22d) TSV refresh** | Apr 17 | Low priority — non-load-bearing on current threads. |

---

## RECENTLY RESOLVED
*Last ~2 weeks. Top of mind so the audit trail is visible without reading commits.*

| Date | What | Result |
|------|------|--------|
| 2026-04-29 PM2 | AAA gas pump live refresh + diesel divergence finding | Pump $4.229 confirmed CRL-08 reprice on track. NEW K-shape finding: diesel falling while gasoline rises = freight demand destruction (KB-252/253). |
| 2026-04-29 AM | CRL-08 reprice 65→78% on Brent breakout | $110.38 close / $115 intraday, ceasefire-binary fired into "breaks" branch. KB-CARL-248. |
| 2026-04-29 AM | Apr 21 quadruple earnings synthesis (SYF/COF/UNH/DHI) | K-shape WIDENING confirmed three independent ways. CRL-12 repriced 77→55% on SYF survivor-pool. KB-CARL-243-247. |
| 2026-04-29 AM | 50-signal BOARD disposition pass | 5 INTEGRATED, 13 INFO_ONLY, 32 REFERRED. KB-CARL-249 (FL labor), 250 (housing prices), 251 (farm bankruptcies). BOARD_LOG synced through Apr 29. |
| 2026-04-29 AM | UMich April Final 49.8 + 5-10Y inflation 3.5% (un-anchoring deeper) | KB-CARL-241. STATUS dashboard updated. |
| 2026-04-19 PM | BOARD pull synthesis — Iran day-cluster, Qatar LNG, MS counter-frame | KB-CARL-234/235/236. Vector #5 reinforced; counter-evidence logged. |
| 2026-04-17 PM | ALLY Q1 composition-masking framework | FY24/25 10-K audit: S-tier 40→37%, nonprime 9.7→10.1%, ACL -$224M/-6%. Composition-masking, not fraud. CRL-05 85→82%. KB-CARL-222-228. |
| 2026-04-17 | Sub-agent buildout completion | All 7 monitoring sub-agents BUILT and refreshed. POLLY + POP final adds. |
| 2026-04-16 | ATTOM Q1 foreclosure pull | 118,727 filings (+26% YoY), Q1 REO 14,020 (+45% YoY), FL Q1 REO +108% nationally greatest. Vector #10 upgraded 4→5. |
