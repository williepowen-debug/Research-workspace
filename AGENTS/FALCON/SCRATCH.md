# FALCON SCRATCH — 2026-10-04 (bounded PROME spawn, prome-ed, ~17:25–17:5x ET)

## CURRENT MARKS
**B 1 / C 14 / D 85** (unchanged; HELD 10/04). Convergence 43/50 unchanged. **1 OPEN: FAL-06 (70%, to 11/05).** **Production rung D 85→92 (WQ-355): ARMED, NOT FIRED.** GATE-FALCON-001 LIVE; leg 2 PROVISIONAL, NOT FIRED at the last read (10/01); **review_by 10/06**. WARRISK falsifier LIT; 4 rows expire 10/06 (+2d), Bab AWRP row expired +62d. **Losses stay 3.** No settle-count clock; step 12b no-op.

## CHANGES SINCE LAST SESSION (10/02 ~14:4x ET → 10/04 ~17:25 ET)
- 10/03: PROME read-only pre-fetch of SIG-W-20261003-012/-013 ("nothing fires", items left unconsumed by design).
- 10/04: WALTER dispatched -005 (UKMTO 150-26 + closure restatement), -010 (Houthi Khurais CLAIM, disputed; Aramco plume S of Riyadh; Bab near-miss; Petroline PS-2 unconfirmed), -011 (Iraq VLCC bypass, info). CATO baseline §BF3; WALTER Bright Data fetch `7525bb064` (portal reached, 150-26 NOT obtained).

## WHAT I DID THIS SESSION (bounded: ONE item, Will's word via PROME)
- Adjudicated SIG-W-20261004-005 / UKMTO 150-26 → `reports/2026-10-04_falcon-ukmto-150-26-adjudication.md`.
  - (a) Source: **CANNOT-AUTHENTICATE at primary** (ukmto.org Cloudflare 403 to curl + WebFetch, incl. the inferred product PDF URL and the search-indexed 148-26 URL; MSCIO mirror lags at 134-26; WALTER BD "0 reports" shell = NOT OBTAINED). **Content corroborated** by Arab Times (names 150-26), Reuters/MEE, Arab News. Event B2.
  - (b) Identity: **NEW event, VI-2026-0045 (INFERRED)**. Event date UNKNOWN (TBC). **Found + fixed an own-ledger miss: 149-26 (10/02 2142Z, crude tanker ~4 nm E of Oman) backfilled as VI-2026-0044.** VI-0043 mapped to 148-26 (Ambrey: Panama flag → resolves WALTER -018's "Panama inbound", INFERRED).
  - (c) Screenshot = STRIKE (not sinking, not mine). Account's "9 in 5 days" NOT SUPPORTED (8 hulls 9/28–10/04, max 7 in 5 days); "highest rate" contradicted (9/05–9/09 = 10). Fars-via-SBS IRGC 7-tanker claim = F3, watch.
- KB-FALCON-236..239; VESSELS (2 new rows, 2 annotated, data clock 10/04); board_log ×2; 2 items `git mv`'d to processed.
- Boot checks run: 5a (FLOW +166d, known), 5a-2/5a-3 (WARRISK rows +2d; Bab expired +62d), 5b-2 (Hormuz DEEPENING, newest print 9/25–9/27, no new prints), 5b-3 (bypass HOLDING 122,458 vs floor 29,590), 5c (STRIKES swept through 10/01; no new facility rows in scope), 7b (PASS). SKIPPED: 5b baghdad (demoted), 5b-4 kharg (impeached), web sweep beyond 150-26 (bounded scope), CTP-ISW Iraq read (still owed).
- NO pull (shared dirty tree: WALTER + PROME paths). NO push (spawn order: PROME pushes).

## NEXT SESSION (dated, future-verifiable)
1. **BEFORE 2026-10-06:** consume SIG-W-20261004-010 — **Khurais = PRODUCTION class**: a counting-source (state/operator/CENTCOM/named wire) confirmation of a hostile hit FIRES the rung D 85→92, C 14→7 → PROME first line, same hour. WALTER verify found Aramco silent, coalition says "misleading", a plume at an Aramco facility S of Riyadh (not Khurais).
2. **2026-10-06:** GATE-FALCON-001 review on the PROVISIONAL leg-2 letter (TankerMap read; R1/R2/R3 as written).
3. **2026-10-08:** 7-day scenario review.
4. Drain the rest of `inbox/WALTER/` (10/02 -025/-026/-033; 10/03 -001/-003/-012/-013; 10/04 -010/-011) + PROME's 10/03 pre-fetch note.
5. Watches from 10/04: 150-26 hull name / NUC / CTL; KAZIMAH III "Abandoned" (tertiary); Fars 7-tanker claim primary; 150-26 primary authentication (exact URL in the report — PROME's Bright Data call).
6. CTP-ISW + Shafaq Iraq read (owed since 10/01, carried 3×).

## OPEN THREADS / WATCHES
- 🔴 CARRIED OPEN (MEMORY.md): KB-168 Yanbu terminus proxy unbuilt.
- Pattern-watch: KOTC-concentrated hits (AL FUNTAS + KAZIMAH III); a 3rd Kuwait hit ⇒ same-hour note to PROME + HAWK. 150-26 hull unnamed.
- Yanbu/Ghawar IMMEDIATE triggers unchanged (see STATUS Owed). Petroline 5.5 mb/d one-source. Kpler/Vortexa weekly Saudi print for FAL-06 route (c).
- VESSELS backfill: El Gaia 9/13, St Helena 9/14, Trend 9/16, STI Steadfast 9/18; AL FUNTAS UKMTO number. VX sweep owed. FRESH_LEG_BASELINE hot/cold split owed.

## PREDICTIONS DUE / DECISIONS PENDING
1 OPEN (FAL-06, 70%, 2026-11-05) — 150-26 is a hull strike, not a crude-supply loss; unaffected. No trade (WQ-192). No Will decision from this desk. One PROME call offered: spend 1 Bright Data request on the exact 150-26 product URL.

## MAIL STATE
In: 2 consumed (PROME 150-26 packet; WALTER -005). 10 unconsumed (9 WALTER + PROME 10/03 note). Out: `PROME/inbox/2026-10-04_from-FALCON_ukmto-150-26.md` + SendMessage COMPLETION block.

## PENDING PUSH / GIT
Exact-path commits by this desk; **NOT pushed** (spawn order: PROME pushes the train at its closeout). Foreign dirty paths (WALTER bookmarks JSON, PROME WQ ledger) are not mine.
