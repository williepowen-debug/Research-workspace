# BRENT SCRATCH — September 10 (noon WPSR session, Will-opened window, DOCKET L305)

## CHANGES SINCE LAST SESSION

- Third straight +3%+ crude session: BZX26 9/9 daily-bar close 101.21 (agrees with CNBC-relayed ICE settle, highest since 5/22), 9/10 live ~106.5; Nov–Jan Brent +9.17 (from +7.54 / +6.62); WTI−Brent Nov −9.37; OVX 56.9 (+14%). XLE −0.5% on the day; tankers barely up.
- Kinetic: five IRGC-linked hulls struck 9/8, **Riesco SANK** (CENTCOM primary); Iran's claimed 10-vessel wave 9/9 plus 20 missiles at Jordan (18 intercepted); two NON-Iranian hulls hit 9/9 — Hercules Star at the Dubai anchorage (1 dead, 1 missing) and New Andros (~2.0M bbl Iraqi fuel oil, off Al-Faw, afloat, no leakage); SNSC "exclusion zone" outside Hormuz declared, unenforced. Houthis took Mokha 9/10. FALCON backfilled the Amzan (Bahri VLCC) strike of 8/24 off Yanbu; FALCON KB-151: Jazan shut through August ⇒ 9/7–9/8 hits had zero incremental loss.
- Macro: ECB +25bp to 2.50% on energy (energy HICP 14.3%); US Aug PPI energy +4.2%, diesel +24.1%; UK 30Y gilt 5.94%; TTF €80.90 leg high.
- WPSR wk-9/4 published 12:00 ET (Labor Day schedule); the 9/9 autonomous EIA routine correctly recorded "no report".

## WHAT I DID THIS SESSION

- Boot complete (rc=2: weekly-freshness finding now cleared by the read; BRT-29 M and instrument-coverage/incident-staleness findings remain). No pull needed (local was one PROME commit ahead; PROME session live with dirty PROME files).
- **Read WPSR wk-9/4 at 12:00:03 ET** (pre-noon 403s were the signed-URL embargo). Wrote [research/2026-09-10_wpsr/REPORT.md](research/2026-09-10_wpsr/REPORT.md) + 3 CSVs + manifest. **L305 first print NO VERDICT** (SPR 285.360M, Δ1 −1.244M). **Edouard pre-registered narrow read RIGHT** (US util 97.8% −0.2pp; PADD 3 98.3% +0.6pp). Cushing 21.824M (−0.684M). Distillate +2.086M (2nd build). Gasoline 4-wk −1.4% (BRT-29 T moving away).
- TRACKER lines 1/2/3/5/6/9/10/11 refreshed; STATUS re-based (two dated blocks rotated to `archive/STATUS_DETAIL_2026-09.md`, crc32 `1139d716` and `ade73d1d`; file 32.3–32.5 KB vs 32,550 budget — **tight**); TRADE header/rows updated with delayed option indications (no instruction change); CATALYSTS L305 graded-partial + new 9/16 resolver row; calendar re-rendered, check passes.
- WQ-189 instance ③ graded on BG-02: Riesco NOT MET (already-interdicted limb; grade does not turn on laden state), New Andros and Hercules Star NOT MET. Reply packet to `AGENTS/FALCON/inbox/` (copy in outbox/). $0 moved; STAND DOWN intact.
- Inbox drained: 5 WALTER + PROME L305 + FALCON 9/10 + PROME/FALCON KB-151 + OSPREY 9/8 — 9 rows in board_log, 9 files `git mv`'d. No objection lodged on the OSPREY downgrade path (window 9/15).
- Completion memo → `PROME/inbox/2026-09-10_from-BRENT_L305-wpsr-first-print-no-verdict-inbox-drained.md`.

## NEXT SESSION (dated, future-verifiable)

1. **Fri 9/11 — Friday pair.** Baker Hughes ~13:00 ET (GET the landing page, pick the file by date in content-disposition, never HEAD; frozen line 457, oil rigs 449 at 9/4; two independent pulls). CFTC COT as-of 9/8 ~15:30 ET: `cot_grade.py --expect 2026-09-08`, exit 3 = WAIT; cross-check raw `f_disagg.txt`. GATE-BRENT-COT-35B review_by 9/11. Don't stack. **Also grade WALTER Boundary #8 (Brent 3:2:1 > $50/bbl, 2–3 sessions sustained = dispatch; BRENT primary) at the 9/10 and 9/11 SETTLES on the Brent basis: (2×RBX26 + HOX26)/3 ×42 − BZX26. 9/9 bars = 47.80 (not crossed); 9/10 intraday ≈ 50.1. Letter at AGENTS/WALTER/design/ROUTING_OVERLAYS.md row 8. Dispatch to CARL/HENRY/REGINALD only if sustained; WALTER logs.**
2. **Wed 9/16 10:30 ET — WPSR wk-9/11 = L305 SPR second print.** Δ2 vs 285.360M; Branch A needs Δ2 ≥ −2.756M, Branch B ≤ −6.756M, between = NO-VERDICT and re-read the next two. Also Cushing vs 20.0, util vs 97.8, distillate trend, gasoline 4-wk YoY (BRT-29 T).
3. **Fri 9/18 — USO Sep-18 150/165 spread expiry.** HOLD through expiry (WQ-168 ③); TERRY's card governs; USO 156.74 between strikes at 9/10. No BRENT action beyond the price leg; the broker/Will handle settlement.
4. **XLE receipt (L253) still pending** from the 9/9 selected exit — do not infer fill; 65C delayed 1.42/1.52 at 11:35 ET 9/10.
5. **Before 9/30 — BRT-12 original construction** (contracts/roll/price field + dated refiner-vs-upstream credit series) per [REMAINING_PLAN](audits/2026-09-09_maintenance/REMAINING_PLAN.md); **BRT-29 M overdue since 8/31** — pursue eligible carrier events; no new grade until evidence. BRT-29 T reading −1.4% at wk-9/4; needs ≤ −3.0% by wk-9/25 (released 9/30).
6. **Basra/Al-Faw export approach** — now a live-incident leg with no instrument on BRENT or FALCON. Candidate: Iraqi SOMO/Basra loadings via a named relay with dated observation; register only with base rates (L21/L22). Not a threshold yet.
7. **STATUS is at the read-cap edge** (~32.4–32.5 KB of 32,550). Next session: rotate the "September 9 approved review" and "September 8 owner result" blocks before adding anything.
8. Later: 9/15 OSPREY window closes (no objection); 9/30 resolutions; 10/1 full owner read; 10/4 OPEC; 10/6 STEO; 10/26 BRT-30.

## OPEN THREADS / WATCHES

- 🔴 Iran "exclusion zone" outside Hormuz: declaratory until an enforcement event; transit relays say ~10/day vs ~130 pre-war (CBS) — no BRENT instrument (PortWatch impeached). Frame-breaker needs confirmed cargo/throughput loss, never a headline.
- 🔴 SPR two-print test — the ONLY thing that can resolve L305 is the 9/16 print; do not pre-judge from Δ1.
- 🟠 Distillate: two consecutive builds with the matched-Nov ULSD crack >$105 — export pull vs US hole; watch exports (1,556 kb/d, −179) and PADD 3 production next print.
- 🟠 CPC partial restart / Jazan current state / nine stale ACTIVE incident rows (RF-004/009/013/014/015/017/022/030 + Kstovo now confirmed by OSPREY 8/26 shutdown) still need primaries; Novorossiysk terminal fire 9/8–9 (OSPREY KB-101) not logged — facility unnamed, no throughput statement.
- 🟠 WALTER Boundary #8 located (ROUTING_OVERLAYS.md row 8): Brent-basis 3:2:1 sat ≈ $50.1 intraday 9/10 vs the $50 line — right on it; the basis decides the grade and settles decide the sessions. Grade at settles 9/10 → 9/11 → 9/14; the WTI-basis 59.48 in the report is NOT the letter.
- 🟡 Remote routine timing repair still uninstalled; A5/A6 open.

## POSITION DECISIONS PENDING

- None new. XLE exit receipt pending (TERRY/Will). USO 37 shares; USO Sep-18 150/165 ×1 HOLD through 9/18; USO Oct 135C CLOSED. STAND DOWN (WQ-192) binds; no arm, no proposal; $0 moved this session.

## MAIL STATE

- Inbox: clear (WALTER lane and top level both empty after the 9/10 drain).
- Outbox: 1 sent this session (to FALCON, WQ-189 laden-leg answer; loop closes on FALCON's VI-2026-0028 note). Completion memo delivered to PROME/inbox.

## WORKBOOK HEALTH

- board_log +9 rows. CATALYSTS +1 row (9/16), L305 row graded-partial. TRACKER block refreshed with a dated REFRESH stamp. PREDICTIONS.tsv untouched (nothing DUE; BRT-29 T reading lives in TRACKER line 6). Frozen ledgers untouched. INCIDENTS untouched (Jazan increment resolved by relay, status unchanged — no primary). No lesson added.
