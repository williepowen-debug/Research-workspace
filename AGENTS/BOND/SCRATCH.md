# BOND SCRATCH — 2026-07-06 (Mon, teams session)

**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md`; thesis → `thesis/THESIS.md` (v1.1); live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (7/1 → 7/6)
- **30Y AT ~5.00 intraday (7/6)** (^TYX) — was 4.97 close 7/1; the day before the 7/9 reopen. 10Y flat 4.48. **DFII10 ticked UP to 2.25 (7/1)** from 2.20 — real-rate leg re-approaching the 2.5 re-arm (not there). Credit inert: HY 275 / IG 75 / CCC 971 (FRED 7/2). TLT $85.31.
- **QT-framing corrected** (PROME fix-packet, Will-authorized): `domain/sources/AUCTION_FRAMEWORK_from_LIQUID.md` line 29 "QT still active" → **QT ended Dec-1-2025; Fed buys T-BILLS not coupons (RMPs) → no Fed coupon backstop.** Sharpens the 7/9 read: long-end absorption is entirely private/foreign/dealer.
- **BND-11 refunding pre-reg built + reconciled with LIQUID** → `BND11_REFUNDING_PREREG_2026-07.md`. ONE figure both agents grade: **30Y indirect as %-of-competitive-accepted vs June-6/11 60.0% benchmark.**

## WHAT I DID THIS SESSION
1. Boot + read fix-packet + LIQUID's `DEMAND_HOLE_AUCTION_PREREG_2026-07.md`.
2. Applied QT fix to `AUCTION_FRAMEWORK_from_LIQUID.md` (post-QT RMP framing, dated correction note).
3. Live pulls: CBOE intraday yields (^TNX/^TYX/^FVX), FRED (DGS/DFII10/OAS series), yfinance ETFs. FR2004 6/24 print NOT retrievable (NY Fed API caps pre-2026 in this env) → carried 6/17 record, flagged pending.
4. Built the reconciled BND-11 pre-reg (grade card fusing BOND mechanics + LIQUID absorption; the "masked hole" reconciliation).
5. STATUS full refresh (dashboard, regime, matrix, trade, catalysts, bottom line); BND-11 row note updated (criteria unchanged).
6. Delivered to PROME via SendMessage.

## NEXT SESSION (dated, future-verifiable)
1. **Tue 7/7 3Y · Wed 7/8 10Y-R · Thu 7/9 30Y-R** — results ~1pm ET each. **Resolve BND-11** from TreasuryDirect primary (30Y heaviest). Grade each on the reconciled card: post a one-line verdict per tenor to STATUS + cross-flag LIQUID same-day. **Compute 30Y indirect as %-of-competitive-accepted** (same denom as LIQUID) vs 60.0%.
   - **JGB 30Y auction 7/7 (Tokyo PM, overnight ET) = LEADING INDICATOR** — grade it first (SAM: firm BTC≥2.9/tail≤3bp · soft 4-6bp · weak >7bp; benchmark Jun-10 2.936x/2.8bp). Sets my OPENING 7/9 lean. **Two-step gate: a JGB-soft is only a real 7/9 downgrade if the US 10Y reopen 7/8 ALSO comes soft** (correlation transmitted); JGB-soft + US-10Y-firm = noise → revert to base 70%. JGB moves the term-premium/tail leg, NOT the indirect-composition leg → can't fire the acute/arm-#1 alone. Full framework in the pre-reg file's JGB-link section.
2. **Pull the FR2004 as-of 6/24 print** (released 7/2) — decisive dealer-absorption 3-vs-4; still pending. Also 7/7–9 auction sizes + 10Y JGB (7/2) result to reconcile.
3. **Daily:** 30Y vs 5.0 (BND-12 sustain-count — a poke ≠ a hold; needs 5 consecutive closes); DFII10 vs 2.5 (now 2.25, ticking up); USD/JPY 165 / MOF actual intervention (FL-BND-11).
4. **7/8** June FOMC minutes (HENRY owns rate-path; BOND owns long-end consequence). **7/24** resolve BND-12. **End-July** resolve BND-01.

## OPEN THREADS / WATCHES
- 🔴 **7/9 30Y = the month's decisive print.** Demand-hole config fully pre-positioned (record dealer stock + fading indirects + 30Y at 5.0 + supply gauntlet + no Fed coupon bid) — everything but the trigger. The reconciled "masked hole" (indirect <55% + directs/dealers backfilling, no tail) is the likeliest way it bites without a headline marker.
- 🟠 FR2004 6/24 print pending (env-limited pull); →4 trigger still ARMED, half-met.
- 🟠 JGB-FX channel (FL-BND-11): verbal stage; actual MOF intervention = mechanical UST selling. Joint w/ SAM.
- 🟡 CCC 971 non-retrace; Energy HY unpinnable [STALE Apr 28]; EU xccy proxy build (converge w/ LIQUID); Packet 7 (NEXUS_BRIEF) still open.

## POSITION DECISIONS
- **TLT puts: HOLD, no add.** 30Y at 5.0 is a poke not a hold; DFII10 2.25 not >2.5; no auction marker. Add-gates: DFII10 >2.5 sustained / 30Y >5.0 ×5 + weak auction / BND-11 FALSE (reconciled verdict ③).
- **HYG puts: stay closed** (issuance boom). Credit-equity lead inactive.

## MAIL STATE
- Inbox: fix-packet `2026-07-06_from-PROME_fix-stale-QT-framing.md` PROCESSED (fix applied). → move to `inbox/processed/` at closeout.
- Outbox: none needed (LIQUID coordination is same-session teams; PROME got SendMessage + this dir).

## WORKBOOK / PUSH HEALTH
- No new KB rows this session (correction + pre-reg, not new evidence); consider a KB row logging the QT-framing correction + the reconciled-grade methodology at next full closeout.
- Commits path-scoped BOND-only; rides the push-train (auto-push via safe-push at closeout).
