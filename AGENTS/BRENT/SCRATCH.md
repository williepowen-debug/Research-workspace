# BRENT SCRATCH — September 10 (noon WPSR session, Will-opened window, DOCKET L305; extended through the 13:xx ET STATUS/SCRATCH audits)

## CHANGES SINCE LAST SESSION

- Third straight +3%+ crude session: BZX26 9/9 daily-bar close 101.21 (agrees with the CNBC-relayed ICE settle, highest since 5/22); 9/10 live 106.58 at 12:03 → **107.20 session high at 12:25** (highest since 5/19). Nov–Jan Brent +9.17 → +9.43 (from +7.54 / +6.62); WTI−Brent Nov −9.37; OVX 56.9 → 58.3 (+17%). **XLE −0.5% and SPY/TLT both down on the day** — stagflation tape; tankers +1–1.6%.
- Kinetic: five IRGC-linked hulls struck 9/8, **Riesco SANK** (CENTCOM primary); Iran's claimed 10-vessel wave 9/9 plus 20 missiles at Jordan (18 intercepted); two NON-Iranian hulls hit 9/9 — Hercules Star at the Dubai anchorage (1 dead, 1 missing) and New Andros (~2.0M bbl Iraqi fuel oil, off Al-Faw, afloat, no leakage). **Overnight 9/10, per Iranian state media: strikes on Iran's Hormuz shore** — Sirik pier + Ports and Maritime Organization tower, Qeshm Island, Hormozgan grid, Jiroft airport (no CENTCOM 9/10 statement found). Israeli DM Katz threatened Iranian energy infrastructure. SNSC "exclusion zone" declared, no coordinates, unenforced. Houthis took Mokha 9/10. FALCON backfilled the Amzan (Bahri VLCC) strike of 8/24 off Yanbu; FALCON KB-151: Jazan shut through August ⇒ 9/7–9/8 hits had zero incremental loss.
- Macro: ECB +25bp to 2.50% on energy (energy HICP 14.3%); US Aug PPI energy +4.2%, diesel +24.1%; UK 30Y gilt 5.94%; TTF €80.90 leg high.
- WPSR wk-9/4 published 12:00 ET (Labor Day schedule); the 9/9 autonomous EIA routine correctly recorded "no report".

## WHAT I DID THIS SESSION

- Boot complete (rc=2: weekly-freshness finding cleared by the read; BRT-29 M and instrument-coverage/incident-staleness findings remain). No pull needed (local one PROME commit ahead; PROME live with dirty PROME files).
- **Read WPSR wk-9/4 at 12:00:03 ET** (pre-noon 403s were the signed-URL embargo). Wrote [research/2026-09-10_wpsr/REPORT.md](research/2026-09-10_wpsr/REPORT.md) + 3 CSVs + manifest, §2b 12:25 tape update. **L305 first print NO VERDICT** (SPR 285.360M, Δ1 −1.244M). **Edouard pre-registered narrow read RIGHT** (US util 97.8% −0.2pp; PADD 3 98.3% +0.6pp). Cushing 21.824M (−0.684M). Distillate +2.086M (2nd build). Gasoline 4-wk −1.4% (BRT-29 T moving away).
- TRACKER lines 1/2/3/5/6/9/10/11 refreshed. TRADE: delayed option indications, then **Will's Robinhood screenshot receipt** (spread HELD, mark 6.11, cost 3.00), then the **WQ-207 ruling** (see below). CATALYSTS: L305 graded-partial; 9/16 resolver row added; 9/18 expiry row re-keyed to **9/17 mandatory close**; 9/11 row extended with the Boundary #8 settle grade.
- WQ-189 instance ③ graded on BG-02: Riesco NOT MET (already-interdicted limb; grade does not turn on laden state), New Andros and Hercules Star NOT MET. $0 moved; STAND DOWN intact.
- **Position ruling: Will approved TERRY option 1 (`TRY-MGMT-USORH150165`) at 12:35 ET, verbatim "Approve option 1"** ⇒ WQ-207: mandatory close of the USO Sep-18 150/165 spread at the **9/17 open**, or next open after a USO close ≥165 / <153; no roll; supersedes WQ-168 ③ HOLD. BRENT concurred as thesis owner (RISK_RULES #23 attribution: kinetic, not OPEC+). TERRY ratified/STAGED the card after verifying the word in the committed artifact; PROME registered WQ-207 and will ask Will's one-line confirm in its own window (formality). TERRY then flagged two stale "HOLD through expiry" rows — swept by grep: 7 live sites across TRADE/SCRATCH/NEXUS/STATUS replaced, struck text kept as SUPERSEDED.
- Inbox drained: 5 WALTER + PROME L305 + FALCON 9/10 + PROME/FALCON KB-151 + OSPREY 9/8 + TERRY stale-rows flag — **10 rows in board_log, 10 files `git mv`'d.** No objection lodged on the OSPREY downgrade path (window 9/15).
- **Packets sent (6):** FALCON ×1 (WQ-189 laden-leg answer) · TERRY ×2 (concurrence + RR#23; WQ-207 ruling relay) · PROME ×3 (L305 completion memo; Robinhood screenshot mark; WQ-207 ruling). Cross-session: WALTER (WPSR agreement; Boundary #8 basis) and PROME (WQ-207 doorbell) messaged; PROME and TERRY replied, loops closed.
- **16:3x ET — PROME relayed Will's 16:10 Robinhood capture: spread CLOSED early ($630), USO 159C 9/11 bought @1.52.** Verified at PROME's transcription; TRADE/CATALYSTS/STATUS/NEXUS updated; WQ-207 marked discharged.
- **STATUS audit cut (Will-approved):** 11 blocks rotated verbatim to `archive/STATUS_DETAIL_2026-09.md` (crc-stamped, all 12 cited blocks re-verified), pointer paragraphs collapsed to one ARCHIVE INDEX + OWNER POINTERS block, four stale claims fixed (9/18 expiry → 9/17 close; frame-breaker pointer → SPECS_GATES BG-02; WQ-112 58% → 85% canonical; stance-row v5.8 quote dated). **STATUS 32.5 → 25.1 KB (77% of budget).** SCRATCH re-audited and rewritten (this file).

## NEXT SESSION (dated, future-verifiable)

1. **Fri 9/11 — Friday pair.** Baker Hughes ~13:00 ET (GET the landing page, pick the file by date in content-disposition, never HEAD; frozen line 457, oil rigs 449 at 9/4; two independent pulls). CFTC COT as-of 9/8 ~15:30 ET: `cot_grade.py --expect 2026-09-08`, exit 3 = WAIT; cross-check raw `f_disagg.txt`. GATE-BRENT-COT-35B review_by 9/11. Don't stack. Re-stamp the STANDING STATE rows (reconciled 9/7) against the new prints.
2. **Fri 9/11 — Boundary #8 grade at SETTLES** (WALTER row 8: Brent 3:2:1 > $50/bbl, 2–3 sessions sustained = dispatch; BRENT primary): (2×RBX26 + HOX26)×42/3 − BZX26, same delivery month, ICE settle after 18:00 ET, for the **9/10 and 9/11 sessions** (9/14 third). 9/9 bars = 47.80 not crossed; 9/10 intraday 49.7–50.8 depending on the print. Letter: `AGENTS/WALTER/design/ROUTING_OVERLAYS.md` row 8. Dispatch to CARL/HENRY/REGINALD only if sustained; WALTER logs. The report's 59.48 is WTI-basis, not the letter.
3. ~~Nightly USO close check / 9/17 mandatory close~~ **DONE EARLY: Will closed the Sep-18 150/165 spread by hand ~15:1x 9/10 for $630 (+$330); WQ-207 discharged, receipt in TRADE (PROME 16:10 capture transcription).** Remaining Will-hand leg: **USO Sep-11 159C ×1 @1.52, expires TOMORROW (CPI 08:30 ET)** — no rule, no BRENT action; note the outcome in TRADE when Will's activity shows it (settle/expiry).
4. **Mon 9/14** — EIA retail release (9/14 observation; TRACKER line 4); Monday autonomous routine writes `demand_destruction/data/monday_2026-09-14.md` (boot step 2b: it wins on tape if newer). FALCON 9/14 re-mark may carry the New Andros / Hercules Star VI rows and the Riesco laden-state note.
5. **Wed 9/16 10:30 ET — WPSR wk-9/11 = L305 SPR second print (DOCKET L318).** Δ2 vs 285.360M; Branch A needs Δ2 ≥ −2.756M, Branch B ≤ −6.756M, between = NO-VERDICT and re-read the next two. Also Cushing vs 20.0, util vs 97.8, distillate trend, gasoline 4-wk YoY (BRT-29 T).
6. **XLE receipt (L253) still pending** from the 9/9 selected exit — do not infer fill; 65C delayed 1.42/1.52 at 11:35 ET 9/10.
7. **Before 9/30 — BRT-12 original construction** (contracts/roll/price field + dated refiner-vs-upstream credit series) per [REMAINING_PLAN](audits/2026-09-09_maintenance/REMAINING_PLAN.md); **BRT-29 M overdue since 8/31** — pursue eligible carrier events; no new grade until evidence. BRT-29 T reading −1.4% at wk-9/4; needs ≤ −3.0% by wk-9/25 (released 9/30).
8. **Basra/Al-Faw export approach** — live-incident leg with no instrument on BRENT or FALCON. Candidate: Iraqi SOMO/Basra loadings via a named relay with dated observation; register only with base rates (L21/L22). Not a threshold yet.
9. **Incident ledger:** boot's re-verify list — RF-004 / 009 / 013 / 014 / 015 / 017 (Kstovo) / 022 / 030 ACTIVE past budget, plus RF-005 / 031 / 008 in present-tense non-ACTIVE statuses. ⚠️ Boot's heading counted **nine** ACTIVE rows but printed **eight** — check the script's count before trusting either figure. OSPREY reports Kstovo/NORSI struck **8/26 and shut** — a NEW event against RF-017's April row, log only at a primary (LESSONS #1); Novorossiysk terminal fire 9/8–9 (OSPREY KB-101) — facility unnamed, no throughput statement, not logged.
10. **STATUS read-cap: 25.1 KB of 32,550** after the 9/10 audit cut; ~7 KB headroom. Add dated blocks at the top; rotate at ≥75%.
11. Later: 9/15 OSPREY window closes (no objection); 9/30 resolutions + XLE residual; 10/1 full owner read + EU storage window; 10/4 OPEC; 10/6 STEO; 10/26 BRT-30.

## OPEN THREADS / WATCHES

- 🔴 Iran "exclusion zone" outside Hormuz: declaratory until an enforcement event; transit relays ~10–12/day vs 85–130 pre-war (Kpler / Lloyd's List / CBS; JMIC ~22/day US-escorted 9/1–9/2) — no BRENT instrument (PortWatch impeached). Frame-breaker needs confirmed cargo/throughput loss, never a headline. **US strikes now on Iran's Hormuz coastline (Sirik/Qeshm) and an Israeli threat to Iranian energy infrastructure** — watch for a first confirmed export-capacity hit; that is the frame-breaker class, a sunk sanctioned hull is not.
- 🔴 SPR two-print test — the ONLY thing that can resolve L305 is the 9/16 print; do not pre-judge from Δ1.
- 🟠 Distillate: two consecutive builds with the matched-Nov ULSD crack >$105 — export pull vs US hole; watch exports (1,556 kb/d, −179) and PADD 3 production next print.
- 🟠 Boundary #8 (Brent-basis 3:2:1) is sitting on the $50 line intraday; the basis decides the grade and settles decide the sessions (item 2).
- 🟠 Equity/crude divergence (XLE down, tankers flat, three sessions) — consistent with premium-not-regime; if it persists into the Friday pair, note it against the tanker-liveness composite (owner grade not run).
- 🟡 Remote routine timing repair still uninstalled; A5/A6 open.

## POSITION DECISIONS PENDING

- **WQ-207 ruled 12:35, then discharged ~15:1x when Will closed the spread by hand ($630, +$330)** — receipt recorded, nothing owed on that leg. Open Will-hand leg: USO Sep-11 159C ×1 (expires 9/11; no rule). XLE exit receipt (L253) still pending. USO 37 shares; USO Oct 135C CLOSED. STAND DOWN (WQ-192) binds; no arm, no proposal; $0 new capital this session.

## MAIL STATE

- Inbox: clear (WALTER lane and top level both empty; 10 files consumed → `processed/`, 10 board_log rows).
- Outbox: 6 packets sent this session — FALCON ×1, TERRY ×2, PROME ×3 (list in WHAT I DID); one sender copy in `outbox/`. Loops: FALCON (WQ-189) closes on its VI-2026-0028 note; TERRY and PROME both replied — closed. Nothing owed to any desk.

## WORKBOOK HEALTH

- board_log +10 rows. CATALYSTS: +1 row (9/16), L305 row graded-partial, 9/18 → 9/17 re-keyed, 9/11 row extended. TRACKER block refreshed with a dated REFRESH stamp (lines 4/7/8 retain 9/7 retail / 9/6 grades — next 9/11). TRADE: POSITIONS + EXECUTION LOG (⏳ WQ-207 fill) + BINDING RULINGS updated. PREDICTIONS.tsv untouched (nothing DUE; BRT-29 T reading lives in TRACKER line 6). Frozen ledgers untouched. INCIDENTS untouched (Jazan increment resolved by relay, status unchanged — no primary). No lesson added. NEXUS_BRIEF re-verified (C6 content) incl. WQ-207 and Boundary #8 corrections. CHANGELOG entry 2026-09-10 written; THESIS v5.8 unchanged.
