# BRENT SCRATCH — October 8, 2026 (2nd session: boot + Isaias deep-dive)

**Closeout writeback 2026-10-08 11:06 EDT; source clocks: named futures 08:24 ET vendor quotes, live-tape confirm 09:09 ET (continuous), MMA 10/7 11:00 CDT, NHC #7/7A 10/8 ~09Z.** 2nd BRENT session this day (follow-on to the 08:46 WQ-391 wake closeout). Claude Code, Opus 4.8 (`claude-opus-4-8`), laptop `WilliePOwen`, sole BRENT writer (TERRY/WALTER/PROME live in their own windows). [Evidence](research/2026-10-08_isaias-hormuz/REPORT.md). $0; no trade, threshold, grade or gate change.

## CHANGES SINCE LAST SESSION
- Only ~2h since the 08:46 writeback. Market materially unchanged: live tape 09:09 ET Brent ~$104.4 (+4.2%) / WTI `CLX26` ~$92.1 (+4.3%) — holds the overnight jump, ~$0.8 off the 08:24 highs. No new verifiable 10/8 news (web returns only the 2020 same-name storm; NOT used).
- WALTER WQ-393 backfill (commits 0a97008bc / 5b4d3db7e this morning) added CORRECTIONS.tsv rows ⇒ **COR-20260921-16 surfaced as unreceipted for BRENT** (was 0 at the 08:46 closeout).

## WHAT I DID THIS SESSION
- Booted (did NOT git pull — TERRY's PAPER_BOOK.tsv is dirty; per pull protocol left the tree alone). Boot rc=2, all 4 findings carried (see WORKBOOK HEALTH); none new.
- Receipted **COR-20260921-16 NO-OP** — BRENT was info-only ("the Brent leg was mis-paired here; nothing in your book changes"); ACTION was on HANS. Receipt in `registry/corrections_receipts.tsv`.
- **Isaias deep-dive (Will-requested):** built the transmission-channel + 3-way weekend scenario framework → **REPORT §10**. Core finding = the crack asymmetry (refinery shut WIDENS the crack / offshore-only loss COMPRESSES it), so "offshore vs refining story" governs the book, not crude level. Wrote it into STATUS Oct-8 block, CATALYSTS 10/10 row (grading basis), NEXUS VIEW+WATCH. Regenerated calendar (--check clean, 29 events).
- Flagged `DCOILBRENTEU` 125.44 (FRED 10/6) threshold breach as a **feed artifact** (contradicts our 10/6 front-month by ~$21), not a real level — advisory, not acted on.

## NEXT SESSION (dated, future-verifiable)
1. **Fri 10/9 15:00 ET:** USO Oct-09 $150C sell-or-roll rail (TERRY's stop; WQ-366 DECLINE; Will executes). **~15:30 ET:** COT #9 (as-of 10/6) — `cot_grade.py --expect 2026-10-06` + raw `f_disagg.txt`; grade before the next release. Rigs record-only.
2. **Fri 10/9 (daytime):** refinery precautionary-shutdown headlines close the Isaias GAP (Pascagoula/Saraland/Chalmette/Meraux); MMA ~11:00 CDT update (shut-in likely RISES into landfall).
3. **Sat 10/10 – Mon 10/12:** Isaias restart read — grade the CATALYSTS 10/10 row against the REPORT §10 three-way fork (base/transient · damage-tail/crack-widener · bust). MMA post-storm releases, platform/refinery damage (deepwater hubs 29N87W, Pascagoula/Saraland), AEOLUS landfall packet. **Watch the crack, not crude.**
4. **By 10/14 settlement:** November governs WQ-386 leg A; TERRY grades; BRENT supplies proxy/settlement only if asked. **10/14 (modeled):** IEA OMR October.
5. **10/15 noon ET:** BRT-31 first release (data week 10/9). December governs WQ-386 from 10/15.
6. **10/24:** WQ-264 shadow endpoint; resolver still unregistered; Texas waiver ends. **10/26:** BRT-30 on JWLA-034 baseline.
7. Carried: China post-holiday guidance (NOT FOUND 10/8, UNKNOWN), Treasury/IRS diesel-tax implementation (10/10), SPR exchange awards; broader WQ-252/HEN-46 owner debt; incident re-verify RF-013/014/022/033 + nine; LESSONS_INDEX semantic reconciliation; routine deployment parked at the CATO handoff.

## OPEN THREADS / WATCHES
- 🔴 Hormuz strike rate and transit floor (FALCON owns rungs); Isaias **now a hurricane (85 mph, NHC Adv #8), Cat-2 peak forecast, landfall AL/FL line late Fri–early Sat** (RI harbinger closed-eye vs pre-landfall shear). ⚠️ Reported deepwater evacuations (Shell Mars/Olympus/Ursa/Vito/Appomattox + Chevron 4) are UNVERIFIED single-Substack — evacuation≠damage; verify at companies/BSEE over the weekend. Nudges Scenario-2 readiness; nothing confirmed. AEOLUS primary (Adv#8): deepwater 64-kt odds 35→48% (offshore side up), but Pascagoula on the WEAK side at current track (refinery-damage risk lower unless westward shift) — the two sides of Scenario 2 now diverge.
- 🟠 Isaias refinery GAP — unresolved until Fri shutdown headlines / weekend restart data. Meraux is Valero's ⇒ double-edged for VLO (throughput − vs crack-margin +); TERRY grades.
- 🟠 Diesel balance: release barrels mostly not new; product losses unmeasured in runs. Forties >$140 relay not carried.
- 🟠 Freight (SIG-W-20261008-028, basis-checked): Bloomberg $1.4M/day Gulf→E.Asia VLCC is UNCLEAR basis, **NOT confirmed TD3C — do not cite as the TD3C record**; verified TD3C stays $1,221,893/day (10/2), Baltic weekly print Fri 10/9. Lump sums: Gulf→China VLCC $76M (Trafigura, load ~11/19), Gulf→Japan $82M offer. Dear long-haul freight widens the WTI export discount (§6 mechanism); Brent-WTI widened ~$0.9 today = mixed, no freight-to-WTI beta, no trade action.
- 🟡 Official settlements, current USO weights, quantified Saudi loss: unavailable.
- ⚠️ `DCOILBRENTEU` FRED feed shows 125.44 (10/6) — anomalous vs ~$101 front-month; threshold-monitor data issue to flag, not a real breach.

## POSITION DECISIONS PENDING
- USO 37 sh / VLO 1 sh / USO Oct-09 $150C ×1 per 10/7 capture (time unknown). **USO $150.13 at 15:43Z (WALTER) — now ABOVE the Oct-9 $150 strike** (pre-market was $149.10). Tomorrow's 15:00 ET sell-or-roll rail is TERRY's card (WQ-366 DECLINE), told directly; order = Will. WQ-366/WQ-200/WQ-192 unchanged. No position/rule change this session.

## MAIL STATE (one line per signal)
- Inbox: clear at boot; mid-session THREE cards arrived, all processed ACTED (board_log rows + git mv): WALTER **SIG-W-20261008-019** (Isaias hurricane upgrade), WALTER **SIG-W-20261008-020** (Iran/Gulf PM: Houthi all-facilities threat, tape +5.6%, USO above strike, Rabigh/Fujairah FALCON items), AEOLUS **isaias-adv8-theater-update** (primary NHC read refining the storm geometry — deepwater 64-kt odds 35→48%, Pascagoula on the WEAK side at current track). THREE MORE at closeout, also processed: **-023** Russia refinery strikes (info-only, OSPREY owns), **-027** El Niño advisory (info-only, AEOLUS owns), **-028** tanker-cost watch (acted — $1.4M ≠ TD3C basis-check, see freight thread). Six cards + one correction total; inbox clear, every move has a board_log row. One correction (COR-20260921-16) receipted NO-OP.
- Outbox: no live packets.

## WORKBOOK HEALTH
- Boot rc=2, ALL CARRIED (none new): TANKER-LIVENESS DEAD+STALE (pre-market equity quotes, 64d human stamp) — gates nothing in stand-down; THESIS-WTI-BRENT/DIESEL-CRACK partial coverage; 4 ACTIVE incident rows past 60d (RF-013/014/022/033) + 9 other present-tense stale; LESSONS_INDEX stale +14d; ledger-nudge 5 ledgers behind STATUS (mostly frozen). Corrections check: 1 named (COR-20260921-16) now receipted. Frozen KB/VX/FLOW/TIMELINE untouched.
- Threshold monitor: GASREGW 4.354 (>4.0, CARL), HY OAS 3.030 (>3.0, LIQUID) — reference-only breaches owned elsewhere; DCOILBRENTEU anomaly (above).
