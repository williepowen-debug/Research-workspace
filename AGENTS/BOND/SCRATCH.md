# BOND SCRATCH — 2026-11-06 close-of-day refresh

> STATE AT WRITING: Composite **17/35** (5+3+2+3+1+1+2, unchanged). Clean-nominal counter 3; auction health 3. **OPEN predictions 5 (BND-33 to 37), none due.** Position: **FLAT** per the FORGE 10/30 reconcile (last broker capture 10/30 intraday; FORGE stale mirror); WQ-592 declined; NO-ADD WQ280. Latest official cells: Treasury 2Y/10Y/30Y 4.51/4.86/5.26 [11/6]; real 10Y 2.63; 5Y5Y 2.17 [11/6]; Bund 3.29 [11/6]; HY/CCC/IG 348/1320/93 [11/5]; SOFR−IORB +2 [11/5]; FR2004 long-end $146.946B [as-of 10/28]; PMMS 7.18 [11/5], 234bp same-date. VX-BND-17 2, VX-BND-04 2. Refunding bars FROZEN 11/2. THESIS v1.2.13. December about 76% [11/6 last vendor print, not settlement; HENRY owns, HEN-63 0.70].

## WHAT I DID

PROME relay of Will's 17:08 ET word: boot, drain, refresh through the 11/6 close; no new thread, no spawn, no trade or card. Boot 17:09 ET; HEAD equal to origin, tree clean at boot.

- **Mail:** inbox and WALTER lane empty. Corrections rc=0. docket_check rc=0, verified only through 11/19; blind span 11/20 to 11/27 holds the 2Y, 5Y, 7Y rows, already docketed from the QRA.
- **Refreshed:** Treasury par and real re-read, cells unchanged from 15:53 ET. New: 5Y5Y 2.17, breakeven 2.23, Bund 3.29 [11/6]; final fed funds vendor print; HYG/IEF 0.8407; VIX 25.64 vendor; EDGAR 22 filers. KB-BND-558, 559.
- **WQ400:** 11/6 evaluated, five-session −11bp, 0 of 21.
- **Pulled-deal search:** one new hit, ANI Pharmaceuticals 8-K exhibit 10.1 filed 11/5; read it, credit agreement takeover boilerplate, not a pulled deal.
- **Stale line fixed:** `monitors/CDX_CASH_BASIS.md` carried 0.8440 for 11/5; the close is 0.8403. Cause of the old figure not established.

## NOT MOVED

No score, band, gate or threshold. VX-BND-15 held 2 at 2.17. 5Y5Y fell, not a registered event.

## UNPUBLISHED OR UNREAD

ICE 11/6 (about 10:10 ET 11/9; no estimate made) · SOFR, EFFR 11/6 (11/9) · ACM 11/6 · KW after 10/30 · FR2004 as-of 11/4 (11/12) · Friday HY volume.

## NEXT (dated)

1. **11/9:** ICE for 11/6, BND-34 needs 352; 3Y `91282CRW3` with `--frozen-bars AGENTS/BOND/registry/auction_bars/<date>_<cusip>.json` under `.venv` python. **A PRE-PRINT line after the print means NOT GRADED, whatever the rc.** One blank Yes/No on any coupon row refuses every grade in the run. Check whether a target stays in `upcoming` after results post (R4).
2. **11/10:** CPI 08:30, 10Y 13:00, UK 5⅜% 2056. **11/12:** 30Y, BND-33 resolves; PMMS re-scores VX-BND-17; FR2004 as-of 11/4.
3. 11/11 VX-20 review; 11/12–11/17 freeze 20Y and TIPS bars; 11/13 FHLB CFR, L226, FRBNY FX report; 11/17 F2 op; 11/19 freeze month-end bars.
4. **Before 12/2:** register any 12/9 curve-shape row with a base rate (docket). After 11/9: bring R1, R5 back to Will.
5. Check BND-34 and BND-37 for early TRUE at each read. 12/17 BND-36; 12/31 BND-34, 35, 37.

## OPEN THREADS

L226 FHLB retune waits on 11/13. 7Y reopening handling before April 2027. Same-day runner re-run reads its own transcript (leftover, bring with R1, R5). True CDX, pulled-deal census, private funding, event-time TIPS unchanged. WQ291 funding window UNGRADED. No primary Fed speaker read. BLS 403 here, so 12/10 November CPI rests on RED's docket row and HENRY.

## CLOSEOUT STEPS (standard, end of day)

C1 STATUS done · C2 KB 558, 559, VX text on 06, 07, 15, 19, FLOW no-op · C3 none due, none registered · C4 no-op, token unchanged · C5 no-op, no catalyst fired since 16:02 · C6 no-op, no gate or position change · C7 this file · C8 RECEIPT done, board_log no-op, no signal consumed · C9 no-op · C11 NEXUS last.

## POSITION

FLAT on this thesis. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

Inbox empty at writing. No packet: no figure others cite moved. Reply to prome-51 sent after the 17:14 run.

## ADDENDUM 18:34 ET, closeout on Will's 18:33 ET word

WALTER card 049 landed after the refresh: Michigan preliminary, long-run 3.4% from 3.5%, interviews end 11/2. Logged KB-BND-560, board_log row, card moved to processed. No score moved. No new work. Everything above stands.

**Control skipped, corrected here:** commit 30a0e63c7d went in after `--verify` printed FREEZE MOVED, because my chained command did not gate on it, and its message wrongly says FREEZE MATCH and cause not traced. Cause, read at `tree_digest`: the digest hashes HEAD, and other desks' commits moved HEAD during the fleet closeout. No BOND path was dirty at the probe. Not self-fixed: a shared HEAD in the digest fails freeze whenever desks close together; bring to CATO or DAEDALUS with R1, R5.

## ADDENDUM 2026-11-09 13:07 ET — PROME due-row wake (Will 12:07 ET), session OPEN

Boot 12:56 ET: corrections rc=0, docket_check rc=0 (verified through 11/19), WALTER lane empty, boot_recompute rc=1 (VX-BND-17 spread-leg review, already scored 2 on 11/5). ICE 11/6: HY 342, CCC 1317, IG 93; BND-34 not TRUE (KB-BND-561). ACM 11/6 0.6428, −7.9bp.
**3Y `91282CRW3` graded REGISTERED 13:04 ET:** indirect 55.48 vs I′ 57.44 → FIRE; dealer 9.48, BTC 2.53 (cover marker by 0.01); OLD not met. **BND-33 TRUE.** Counter 3 → 0; auction health held 3; composite 17. KB-BND-562. Packets: PROME (L924), LIQUID and ZHAO (🟠 FYI).
**NEXT:** 10Y `91282CRX1` 11/10 13:00 ET (bars 63.95 / 13.38 · 2.39 · I′ 65.05), 30Y `912810UY2` 11/12 (59.95 / 14.74 · 2.29 · I′ 63.89) — registered grades for the counter only. Stay open until PROME asks for closeout; NEXUS_BRIEF fold at closeout.
