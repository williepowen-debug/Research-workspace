# BRENT SCRATCH — September 18, 2026 (Friday; live session with Will, boot 10:58 ET — ⛔ **CUT BY A MACHINE CRASH ~15:36 ET, BEFORE CLOSEOUT AND BEFORE ANY PUSH.** The closeout write-back below had been WRITTEN TO DISK but not committed; a PROME-spawned recovery session validated and committed it 2026-09-18 17:2x ET. Treat every 'closeout' verb below as *written, then recovered* — the session never ran its own step 14.)

## CHANGES SINCE LAST SESSION
- Petroline day 8: Aramco OBJECTIVE ≥half "within days" / full ~6 wks (Bloomberg via ENR; Wright "within days"); Saudi MoE names no timeline; pump stations 8 and 9 damaged, drones from Iraq. Kpler 9/17: no Yanbu loadings since 9/11, 3–5 d stock, ~4.5 mb/d halted (estimate). Sohar STS offers + Ras Tanura/Juaymah ~4 mb/d loadings (Reuters, unnamed) = hand-off THROUGH Hormuz, not a bypass; ~60M bbl sold for Sep/Oct.
- Saudi–Houthi direct exchanges 9/17 (Hajjah/Taiz strikes; drone debris death at Taif ~150 km from Yanbu); no Red Sea ship attack since 8/24; Bab transits recovering (45 on 9/13, single-source). Tanker `Trend` (Togo) struck/detained in Hormuz 9/18 per IRGC; UKMTO 16 nm NE Khasab, crew safe; cargo state UNKNOWN. Yaroslavl (~300 kb/d) hit 9/17; no RU/UA energy truce.
- Tape: Brent Nov settled $104.82 on 9/17; 9/18 15:31 ET vendor bars BZX26 $103.07, CLV26 $99.78 (below $100 intraday), CLX26 $95.54; Nov−Jan +$7.59. Dated Brent >$130, diesel >$220 (Saxo/Rigzone/Kpler). FOMC hiked 25bp 9/16 citing oil.
- IEA Sept OMR: 2026 demand −2.5 mb/d; observed stocks −95 mb Aug, −507 mb since Feb. Japan (METI Jul; SAM correction): ME share 58.9%, US crude 37.0%, Kuwait/Qatar zero. JWLA-035 (16 Sep): Black Sea only; Gulf still listed.

## WHAT I DID THIS SESSION
- Booted (2 FINDINGS: JWLA-035 → resolved NOT FIRED, probe baseline re-stamped; standing rows → all 8 re-read and re-stamped at closeout). Six packets processed (3 WALTER acted/info; ORACLE + DAEDALUS-PR6 DEFERRED, left in inbox; DAEDALUS-COT acted; SAM correction acted).
- Graded BRT-26 at the BH primary (452, +2, NOT BREACHED, 1 print left) and COT-35B vintage #6 at the raw primary (JOINT NO-VERDICT, 5th). Graded the 9/18 Yanbu catalyst row (loadings stopped day 1; stock retained).
- Will-approved pursuits: Yanbu optical berth source (candidate only), IEA/OSP watch rows, DEMAND_COMPOSITE.md (new LIVE). Answered SAM's routed question at METI (US crude = the replacement; durability not determinable); SAM integrated.
- Will-approved next steps: 4.909% REPRODUCED (104 obs ending 8/4 inclusive); re-issue watch built + falsified (COT_VINTAGES.tsv, cot_grade.py exit 4); COT-35B REGISTRY row re-cut, GATES cell wording cut in by PROME (9ca99225d); restart-resolver PROPOSAL to Will via PROME; FALCON packet (route-c candidate). Archive checksum caveat investigated → my miss; both archive headers corrected (character counts), desk receipt rule extended.
- Closeout write-back (drafted to disk 15:3x–15:36, committed by the recovery session): STATUS 9/18 block + 8 standing rows re-stamped; TRACKER re-stamped SCOPED-PARTIAL; CHANGELOG evidence entry; TRADE pointer; NEXUS_BRIEF write-back with vintage boundaries. ⛔ Steps 13a (mail archive sweep) and 14 (commit/push) were NOT reached by the crashed session.

## NEXT SESSION (dated, future-verifiable)
1. **Mon 9/21:** if Will approves ask ① — start the Yanbu berth shadow run (daily read of hormuzstraittracker Red Sea page → `demand_destruction/data/yanbu_berth_YYYY-MM-DD.tsv`). Re-read `MKT-CL-F-ABOVE-100` at boot: name the contract (CLV26 last settles vs CLX26 after the ~9/22 roll) before calling any un-fire.
2. **Tue 9/22:** ATA August tonnage (composite row; no threshold). CLV26 expiry — resolve `CL=F` identity with a negative control before any WTI-basis figure.
3. **Wed 9/23:** EIA WPSR wk-9/18 — BRT-29 gasoline leg (−1.0% last; needs ≤ −3.0% by wk-9/25), Cushing, distillate, SPR. Refresh composite rows.
4. **Fri 9/25 17:00 ET:** BG-02 window CLOSES — grade on R1–R4 with dual-tracker rules; expect NO-VERDICT on throughput by construction; do NOT extend without Will's word. Same day: rigs = BRT-26 FINAL September print (457 line; +5 breaches) and COT as-of 9/22 (vintage #7; grader appends ledger, re-issue watch runs).
5. **By 9/30:** DAEDALUS PR6 asks (BOUNDARIES register; render_calendar/boot docstrings; BRT-26 split — do the split AFTER 9/25 resolves the row). BRT-12/BRT-29 adjudication 9/30. Reply owed to ORACLE (relevance ruling on Venezuela ladder / OPEC-exit rows).
6. **~10/2:** METI August crude-by-source (SAM registered the row naming me): Kuwait/Qatar zero→non-zero = Hormuz normalisation tell; Saudi kKL = Petroline audit. **~10/5** Aramco Nov OSP; **~10/14** IEA OMR (second collective action watch).

## OPEN THREADS / WATCHES
- 🔴 Petroline restart evidence by class (statement / optical berths / trackers) — proposal pending Will; net lost Saudi crude UNKNOWN; Yanbu tank levels remain a paid-data gap (Kayrros).
- 🔴 Hormuz hull strikes (Trend 9/18, unnamed hull 9/16): laden state unknown; FALCON/HAWK own; carve-out not met on facts.
- 🟠 Demand composite: destruction global/China/US-air, absent India-diesel/US-trucking; first US freight tell = ATA Aug y/y.
- 🟠 WQ-234 (AIS class) with Will; the resolver proposal survives either ruling. WQ-213 reaffirmation still open.
- 🟠 Aramco October OSP NOT FOUND (search-only negative) — confirm at the November print whether October was issued.
- 🟡 Boundary #6/#8 month basis with Will (WALTER); Russia diesel carve-out Q1 UNKNOWN-AT-PRIMARY; nine ACTIVE incidents past 60d re-verify.

## POSITION DECISIONS PENDING
- None new. TRADE owns: USO 37 shares; the 9/16 USO 165C disposition is Will's (WQ-169). WQ-192 stand-down holds; WQ-213 needs Will's reaffirmation + TERRY checks. No construction authorized. Root rule #6 note: today was a RED day for oil — no call proposed; none warranted.

## MAIL STATE
- Inbox: 2 DEFERRED (ORACLE 9/17 pinned markets — reply owed; DAEDALUS 9/17 PR6 — due 9/30). WALTER lane: clear.
- Outbox: clear. Sends were direct inbox packets: **SAM ×1 · DAEDALUS ×2 · PROME ×3 · FALCON ×1 = SEVEN**, every one VERIFIED COMMITTED at the artifact with a sha by the recovery session. ⚠️ **Corrected from "PROME ×2" (six)** — the original line undercounted PROME by one (the Friday-routine-flags packet, `cd3aa83e7`). **Consumption, as re-checked 2026-09-18 17:1x:** SAM consumed (→`processed`, `80308fab8`); PROME consumed the **GATES mirror-fix only** (→`processed`, cut in at `9ca99225d`). ⛔ The **restart-resolver PROPOSAL** and the **Friday-routine-flags** packet are STILL UNCONSUMED in `PROME/inbox/`, and **no `WILL_QUEUE.md` or `DOCKET.tsv` row registers the resolver** — the earlier claim that "PROME acknowledged both PROME packets" is withdrawn as unverifiable: any acknowledgement was verbal and left no artifact. FALCON and DAEDALUS packets still sit unconsumed in their inboxes.

## WORKBOOK HEALTH
- New LIVE: `workbook/COT_VINTAGES.tsv` (grader-maintained), `demand_destruction/DEMAND_COMPOSITE.md` (two-clock header; refresh at each closeout or mark partial). Frozen KB/VX/FLOW/TIMELINE untouched. INCIDENTS.tsv: 9 ACTIVE rows past 60d — still owed a re-verify pass. ⚠️ **Corrected by the recovery session:** the September 15 and 16 blocks were rotated THIS session (two archive files, both receipts reproduced), so the pre-crash note telling the next session to rotate them was already stale when it was written. STATUS now sits in the 70–75% read-cap band with TRADE.md above the 75% rotate trigger — measure with `scripts/read_cap_check.py --agent BRENT` at boot, never from a figure written here.
- Git: all commits path-scoped from the repo root; no pull mid-session (SAM/PROME live on the same box). ⛔ **The push did NOT happen.** The machine crashed at ~15:36 leaving 8 modified + 2 untracked files uncommitted; the PROME-spawned recovery session committed all 10 paths 2026-09-18 ~17:2x ET and **deliberately did NOT push** — AEOLUS was recovering concurrently in the same tree and PROME runs the single `safe-push.sh`. Stamp on the crashed session's last write: `2026-09-18T15:36:04-0400`.
