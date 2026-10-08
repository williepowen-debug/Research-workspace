# BRENT SCRATCH — October 8, 2026 (3rd session: PM wake — shut-in 62.89%, settle-window crack, COT-35B base)

**Closeout writeback 2026-10-08 16:4x EDT; source clocks: MMA 10/8 11:00 CDT (primary), named-contract 14:28–30 ET 1-min bars (vendor), CFTC archive 16:37 ET, EIA WPSR schedule 16:4x ET.** 3rd BRENT session today, spawned by PROME `prome-7c` (desktop) under WQ-369 C8 on WALTER SIG-W-20261008-035. Claude Code, Opus 5.5 (`claude-opus-5-5`), sole BRENT writer per PROME's 16:34 ET preflight. [PM note](research/2026-10-08_isaias-hormuz/PM_NOTE.md). $0; no trade, threshold, grade or gate change.

## CHANGES SINCE LAST SESSION (11:06 ET)
- MMA 10/8 release: Gulf shut-in **1,282,879 b/d = 62.89%** (from 25.08%), gas 57.35%, 121/371 platforms. Refineries: still no shutdown reported.
- Trump (Truth Social, before 13:00 ET): no US attack on Iran before 11/3 — tape, not a decision record; Brent ~$105.4 → ~$103.6 after. CLX26 settled $91.49 (+3.21, Newsquawk).
- WQ-399 (Will 15:28 ET): correction receipts now require fields; 6 corrections from the WQ-393 backfill named BRENT.

## WHAT I DID THIS SESSION
- Booted (no pull — tree carries other desks' uncommitted work). boot.py rc=2, same 4 carried findings (threshold monitor, instrument check, ledger staleness LESSONS_INDEX +14d, ledger nudge); none new.
- **Shut-in read** at the BSEE primary; balance [EST]: WPSR wk-10/9 loses ≈3.1–3.5M bbl; event base path ≈6–7M bbl vs ESA 9.55M; transient unless damage. **WPSR wk-10/9 prints Thu 10/15 12:00 ET** (EIA schedule; PROME's brief said Wed 10/14 — flagged).
- **Settle-window crack (WQ-386 source ③, ESTIMATE):** Nov $113.57914 / Dec $107.32876 (typical VWAP); Nov $23.42 above $90.16. Gasoline crack ≈flat ⇒ distillate-only widening. TERRY grades.
- **COT-35B Leg-B base 4.909% re-reproduced** (4.908595%, fresh CFTC archive; identical to 9/18). No GATES edit; PROME told the GATES "not re-reproduced since 8/13" caveat is stale.
- Receipted 6 corrections NO-OP (new form); charter step 6d receipt line updated (WQ-399, C4-class). Inbox: -033/-034/-035 ACTED; DAEDALUS L546 DEFERRED (stays in inbox).

## NEXT SESSION (dated, future-verifiable)
1. **Fri 10/9 15:00 ET:** USO Oct-09 $150C sell-or-roll rail (TERRY's stop; WQ-366 DECLINE; Will executes). **~15:30 ET:** COT #9 (as-of 10/6) — `cot_grade.py --expect 2026-10-06` + raw `f_disagg.txt`; grade before the next release. Rigs record-only.
2. **Fri 10/9 (daytime):** refinery precautionary-shutdown headlines close the Isaias GAP (Pascagoula/Saraland/Chalmette/Meraux — none reported through 10/8 PM); MMA 1 pm CDT release (11:00 CDT data; 10/8 = 62.89%, likely RISES into landfall). Settle-window crack again if TERRY asks (method: research/2026-10-08_isaias-hormuz/pm_crack_pull.py).
2b. **At next cot_grade.py touch:** DAEDALUS L546 float-tie fix (round Leg-B share before the 4.909 compare + one exact-on-edge test) — packet deferred in inbox/.
3. **Sat 10/10 – Mon 10/12:** Isaias restart read — grade the CATALYSTS 10/10 row against the REPORT §10 three-way fork (base/transient · damage-tail/crack-widener · bust). MMA post-storm releases, platform/refinery damage (deepwater hubs 29N87W, Pascagoula/Saraland), AEOLUS landfall packet. **Watch the crack, not crude.**
4. **By 10/14 settlement:** November governs WQ-386 leg A; TERRY grades; BRENT supplies proxy/settlement only if asked. **10/14 (modeled):** IEA OMR October.
5. **Thu 10/15 12:00 ET:** WPSR week 10/9 (EIA schedule) = BRT-31 first release + first print carrying the Isaias shut-in (expect ≈3M bbl crude-draw bias IF EIA's production estimate carries it). December governs WQ-386 from 10/15.
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
- USO 37 sh / VLO 1 sh / USO Oct-09 $150C ×1 per 10/7 capture (time unknown). USO $150.13 at 15:43Z (WALTER) was above the Oct-9 $150 strike; **fetch.py 16:36 ET read $147.58 (+2.55%) — back BELOW the strike after the Trump post** [CONF vendor, not a close check]. VLO $443.80 (+4.65%) same read. Tomorrow's 15:00 ET sell-or-roll rail is TERRY's card (WQ-366 DECLINE), told directly; order = Will. WQ-366/WQ-200/WQ-192 unchanged. No position/rule change this session.

## MAIL STATE (one line per signal)
- Inbox at this session: WALTER **-033** (WQ-399 receipt form — ACTED: 6 receipts + charter line), **-034** (Trump no-attack-before-11/3 = tape; named-contract settle basis supplied — ACTED), **-035** (shut-in 62.89% — ACTED). DAEDALUS **L546 float-tie** — DEFERRED, left in `inbox/` (latent, next cot_grade.py touch). Every move has a board_log row (3 moved, 3 rows + 1 deferred row). Corrections check rc=0.
- Earlier today: -019/-020/-023/-027/-028 + 2 AEOLUS packets processed (see 11:06 writeback in git history).
- Outbox: no live packets.

## WORKBOOK HEALTH
- Boot rc=2, ALL CARRIED (none new): TANKER-LIVENESS DEAD+STALE (pre-market equity quotes, 64d human stamp) — gates nothing in stand-down; THESIS-WTI-BRENT/DIESEL-CRACK partial coverage; 4 ACTIVE incident rows past 60d (RF-013/014/022/033) + 9 other present-tense stale; LESSONS_INDEX stale +14d; ledger-nudge 5 ledgers behind STATUS (mostly frozen). Corrections check: 1 named (COR-20260921-16) now receipted. Frozen KB/VX/FLOW/TIMELINE untouched.
- Threshold monitor: GASREGW 4.354 (>4.0, CARL), HY OAS 3.030 (>3.0, LIQUID) — reference-only breaches owned elsewhere; DCOILBRENTEU anomaly (above).
