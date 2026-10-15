# BOND SCRATCH — 2026-10-15 (Thu) end-of-day, standard closeout

> STATE AT WRITING: TBT 5 held / TLT 82P closed 10/12; WQ357 TBT decision is Will/TERRY's. NO-ADD WQ280; WQ291 kill MET recommendation, funding window UNGRADED. Composite 17/35 (5+4+2+3+1+1+1), counter 2, OPEN predictions 0. Frontiers: Treasury curve/real 10/14 · ICE 10/14 · NY Fed repo 10/14 · FR2004 9/30 · vendor 10/15 13:50.

## WHAT I DID (Claude Code / Opus 5.5, Will-launched)
- **Boot:** docket_check rc=0 (verified through 10/22; blind span 10/23→11/05 UNVERIFIED) · boot_recompute rc=0 · corrections rc=1 → COR-20261014-36 NO-OP receipt. HEAD == origin/master at boot fetch; no pull needed. Foreign dirty WALTER/TERRY paths and WALTER's staged rename left untouched.
- **10/14 official close confirmed:** 2Y +3, 10Y −2 (real −4, comp +2), 30Y −4 → bull flattener (KB-460).
- **10/15 PPI day:** 10Y −11bp already at 08:20 BEFORE the PPI; PPI blip +2.5bp faded; haven bid from Asia selloff; FF contracts −3 to −6bp vs 10Y ~−10 (KB-461/467).
- Credit 10/14 HY 325 / CCC 1282 / IG 84; SOFR−IORB −2bp; PMMS 7.40 (221bp); Bund 3.45, WQ400 NOT MET (5th eval) (KB-462..465).
- **Bars frozen:** 20Y-R 912810UX4 I' indirect <57.96% (old conj <52.47 AND >17.59; cover <2.36). 5Y TIPS 91282CRR4 conj <51.43 AND >25.42; cover <2.10; no I' (KB-466, docket rows). Run grade_auction from `.venv` (system python lacks numpy → I' NOT COMPUTED).
- **F2 10/15:** OFF-THE-RUN 0.33%, 93% into 912810TC2 → RED packet committed cbf40ee2b (carve-out ①); ledger row `registry/f2_reads.tsv`.
- **Buyback dig (Will ask):** `analysis/2026-10-15_buyback-dig/REPORT.md`, KB-469..471. Prior-close spread "collapse" = TIMING ARTIFACT; op-window spread flat ~11–13bp (10–20Y), ~7bp (20–30Y). ~30% DV01 offset since 9/10. Record 10–20Y offers concentrated in single 2041–42 bonds; 912810TH1 28.2% retired.
- **News sweep (Will ask):** `analysis/2026-10-15_buyback-dig/NEWS.md`, KB-472..474. No Fed support; Treasury intent yes, effect limited; 20Y cut = analyst speculation (Bloomberg 10/12), Treasury silent; QTD buybacks $43.13B vs $38B guided; 20Y>30Y hump only since 9/10. **Docketed Fri 10/16 dealer questionnaire** (date press-reported, date_class estimated).

## Closeout C1–C12 outcomes (standard)
C1 STATUS rewritten (dashboard, gates, matrix re-summed 17, catalysts, bottom line). C2 KB-460..474 (15 rows), VX 12 Current_State refreshed (scores unchanged), FLOW 01/02/03/07/15/16 evidence (statuses unchanged; FL-07 got dated COUNTER-evidence: haven worked). C3 no-op — nothing DUE; 10/28 FOMC curve-shape registration owed by 10/21. C4 THESIS current-evidence legs + channel table updated; no version/regime/gate change, token unchanged. C5 docket: 10/14-confirmation row COMPLETED, PMMS re-dated 10/22, 10/21 + 10/22 frozen bars recorded, 10/16 dealer questionnaire added. C6 TRADE §2/§3/review updated; posture/gates/token unchanged. C7 this file. C8 RECEIPT overwritten; board_log 5 rows. C9 MEMORY: timing-artifact lesson (BOND-local, links fleet vintage-clock finding); outbox none. C10 n/a (standard). C11 NEXUS_BRIEF re-pinned last. C12: first run declared `--superseded 61.72 57.96` in error — those are frozen I' bars for two DIFFERENT 20Y auctions (9/15 vs 10/21, rolling trailing-12), not a superseded figure; the 9/15 grade file is correct history. Re-run without it.

## NEXT SESSION (dated)
1. **FR2004 next weekly as-of** (publishes Thu 10/15 ~16:15 ET, after this closeout) → VX-BND-04 stock read + weak 11–21Y test of dealer selling into the first October 10–20Y buyback op (buyback-dig REPORT §Owed).
2. **Official 10/15 Treasury close** → confirm vendor −10bp; fill the 10/15 same-day-close bracket in `analysis/2026-10-15_buyback-dig/dig.py` (re-run with refreshed `nominal.csv`).
3. **Fri 10/16 dealer questionnaire** → read special topics (20Y / bills / buyback cap after 11/4). FRED 10/15 HY cell 10/16 AM (RED/REGINALD own >320 count).
4. **By 10/21:** register the 10/28 FOMC curve-shape prediction with base rate. **10/21** grade 20Y-R vs frozen bars; **10/22** 5Y TIPS.
5. 10/27 F2 op (20–30Y) · 10/28 FOMC · 11/2 borrowing estimates · 11/4 QRA F1/F3 + buyback-cap expiry.

## OPEN THREADS
- Offered Will a RED follow-up on the timing-corrected buyback pricing (second independent leg vs F2 YCC-lite); no answer — not sent.
- KB lint FYI: KB-BND-352/422/423 Stale_By 10/14 overdue (423 Fed path superseded in substance by 467) — lifecycle not edited.
- Asia figures (KOSPI/Nikkei) only X-feed + press; HENRY/ZHAO lanes.

## POSITION
TBT 5 (FORGE 10/14); TBT −3.1% on 10/15 vendor tape. No action by BOND.

## MAIL
WALTER lane drained (5). General inbox not swept: `inbox/2026-10-15_from-PROME_ORACLE-pulls-fed-oct-hike-odds-30pct-cpi-3.7.md` (info; figures cited). Packet sent: RED F2 read (committed).
