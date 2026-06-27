# TERRY — Will's Day-Trading Profile & Rulebook

**Started:** 2026-06-23 · **Re-based 2026-06-24** (Session 2, 29 trading days 5/1–6/23) · **Session 3 2026-06-27** (3 days 6/24–6/26, same account)
**Status of evidence:** Session 2's clean CSV **retracted two Session 1 "leaks" as data artifacts** (see ⚠ below) and **firmed the realized number** (+$2,951.67, no short/assignment ambiguity). Of the original five suspected leaks, the verified data convicts **one**: holding losers to $0 expiry. Edge is now mildly *supported* (29-day positive sample, puts the driver) but still regime-thin — June was a selloff month and Will's edge is downside reads. **Session 3 vindicated the regime-thin warning:** 6/24–26 was a 3-day whipsaw, the QQQ engine **reversed** (−$3,969, wiping the S2 +$2,952; cumulative 5/1→6/26 now **−$1,017**), and the walk-to-zero leak fired a **second time** (−$1,624). Edge is **regime-conditional, not regime-free** — it shows up in trend/clean-chop and inverts in whipsaw.

> ⚠ **Artifacts corrected by Session 2 (do not re-assert without short/STO evidence):**
> - **No naked short premium ever existed** — 0 sell-to-open codes in the full CSV. The "assignment tails / income" leak was a pasted-feed misread. Realized P&L is firm, not a range.
> - **Overnight holds were net winners** (+$3,464, 16W/6L), not "the clean losing pattern." Session 1's 0W/3L was a 5-day crash-sample fluke.
> - **Long calls were net positive** (+$604), not losing. Puts simply dominate.

---

## Where the edge lives (keepers — protect these)

1. **React & exit, don't predict & hold.** Every clean winner monetized a move *already on the tape*, taken off the same session (AAOI −13.9% → +310; CCL −4.9% → +150; sold the crash-day roll-legs into the move).
2. **Single-name down-reads on a risk-off day** — AAOI +310, CCL +150, SOXX +314, SMCI puts + short TQQQ on 6/23. Reads relative beta/weakness well. *(Now backed by a 29-day positive sample, but the window was a selloff — unproven on a rally.)*
3. **Cuts winners fast.** Genuinely good reflex. The problem is it *only* fires on greens — losers get walked to expiry instead (see Leak 1 / Rule 5).
4. **QQQ 0–1 DTE scalping is the engine — but REGIME-DEPENDENT.** **+$3,044** in S2 (trend/chop). *S3 caveat:* in a 3-day whipsaw it **reversed and gave back more than it ever made** (both 0DTE puts AND calls round-tripped through the strikes). It's the edge in trend/clean-chop and a *liability* in whipsaw. Protect it from the expiry-bleed leak that surrounds it — and from being run in the wrong regime.

## The leaks (ranked by VERIFIED damage)

1. **Holding losers to $0 expiry — ✅✅ CONFIRMED REPEAT (2 reviews).** **S2: −$2,793 / 19 threads** (QQQ 6/11 694P −554, 6/17 735C −412, 6/16 744C −366…). **S3: −$1,624 / 5 threads** (MRVL 6/26 260P −720, QQQ 6/25 705P −651, USO/WEN calls). Winners exit in minutes; directional losers get walked to zero. In S3 this also wore an **overnight costume** (4W/13L — multi-day holds carried to $0, *not* a separate overnight problem). Two reviews running = this is the durable core leak, not a one-off. *(The real content of old Rule 5; NOT about overnight-vs-intraday.)*
2. **Buying premium AFTER the move (peak-IV chase).** MRVL 277.5P @ $13 = **$1,300 after a −9.4% flush** (open, the worst risk on the book); QQQ 6/24 715 straddle bought into the 6/23 crash; index bounce-forces (715C, USO 113C). Top-ticks IV in the direction of an already-made move.
3. **Oversizing the worst entries.** Biggest bet = worst entry: MRVL **$1,300** = 10× its SMCI **$135** sibling. Size inversely correlated with entry quality.
4. **Churn (unquantified this round).** 28 of 155 contracts re-entered same strike. Cancel rate / 20.2% **could not be recomputed** — settled-activity CSV has no canceled orders. Needs an order-level export to confirm whether churn is shrinking. *Was profitable churn this month (QQQ scalps), so demoted pending evidence it actually costs money.*

## Named tendencies (tracked in LEDGER.tsv)

| Tendency | Pattern | Status |
|---|---|---|
| **Disposition (reversed)** | cuts winners fast, **holds losers to $0 expiry** (S2 −$2,793 / S3 −$1,624) — a profit-stop with no loss-stop | ✅✅ confirmed repeat, the core leak |
| **Put vs call** | long puts the driver (+$2,347); calls positive but secondary (+$604) | ✅ refined (calls not a loss) |
| **Sizing** | biggest bet = worst entry (MRVL $1,300 vs SMCI $135) | ✅ holds |
| **Post-move chase** | buys premium into an already-made move (MRVL, index bounces) | ✅ holds |
| **DTE** | ~~0–1 DTE wins / overnight loses~~ — **retracted**; overnight 16W/6L +$3,464 | ❌ artifact |
| **Vol-timing** | claimed "sells into calm" — **moot**, no premium was ever sold | ❌ artifact (no shorts) |
| **Time-of-day** | hesitate at open → over-trade flush → revenge-build at close | ⚠ partly corroborated (S3 escalation + intraday funding); exact times still need timestamps |
| **Both-ways regime-fit** *(NEW S3)* | both-ways (28 call + 30 put entries) works in chop, **shredded in whipsaw** — both legs round-trip the strikes (−$3,969 over 3 whipsaw days) | ⚠ NEW — regime-conditional |
| **Revenge escalation + intraday funding** *(NEW S3)* | daily losses escalated −$425 → −$1,443 → −$2,100; **ACH +$200+$100 mid-session** on the worst day | ⚠ NEW — the revenge-build tendency, now with $ evidence |
| **Engine regime-dependency** *(NEW S3)* | QQQ 0DTE +$3,044 in trend (S2) → **reversed** in whipsaw (S3) | ⚠ NEW — edge is conditional, not constant |
| **Execution: RH 0DTE auto-liquidation** *(NEW S3)* | broker force-closed the 6/26 709P at ~$19 before a ~$346 settlement (~$327 lost) | ⚠ NEW — execution-rail, not discipline; confirm w/ timestamped export |

---

## The Rules (enforceable at order entry) — re-ordered by verified damage

1. **Loss-side time-stop / no walk-to-zero.** *(the verified leak.)* Mirror the winner-cut reflex on reds: a directional option that's wrong by your stop comes off — it is **never** held to expiry to save a few cents of premium. −$2,793 says so. **Mechanical trigger (see `QQQ_DESK_CARD.md`): dead when down ≥60%, OR <60 min to expiry and OTM, OR invalidation level printed.**
2. **No new long premium after a big move** (>5% single-name / >2% index) — you may only *exit*. Killed MRVL's entry; would have killed the 6/23 crash straddle.
3. **Per-idea max-loss cap,** sized *below* a typical scalp stack — cap the size, cap the chase. (MRVL $1,300 was the cap-breaker.)
4. **Don't fight what's working: protect the QQQ 0–1 DTE scalp engine — but only in its regime.** It made +$3,044 in trend/chop; it **reversed −$3,969 in S3's whipsaw** run both-ways. Don't let revenge-size or expiry-bleed contaminate it — and **don't deploy the both-ways chop tactic when the tape is whipsawing** (2–3% intraday reversals that round-trip both legs). When the regime is unclear, size down or stand down.
5. **~~Flat by the close~~ → Pre-register every overnight hold.** Overnight was *profitable in S2*, so this is no longer a blanket prohibition — but every carried position still needs a written invalidation + time-stop so it's a *decision*, not a default. *(S3 caveat: overnight went 4W/13L when the carries were just walk-to-zero losers — Rule 1 governs those, not this one.)* *(Old "short credit ≠ income" rule retired to hygiene-only: no shorts have ever appeared; re-activate only if an STO shows up.)*
6. **0DTE auto-liquidation window (execution — NEW S3).** Don't hold 0DTE into Robinhood's expiration-day auto-close (~3pm ET on) with a directional lean into the bell. RH force-closed the 6/26 709P at ~$19 right before a settlement worth ~$346 — **~$327 lost to the broker's exit, not yours.** Options: (a) exit on *your* terms before 3pm; (b) hold to settlement *with* the buying power so RH can't force you out; (c) don't run 0DTE you intend to carry to the close. *(Execution-rail, not a discipline failure — TERRY's lane. Confirm frequency with a timestamped order export.)*

---

## Open / unresolved

- **OZK $50P 8/21 was NOT a naked short** — CSV shows BTO 6/15 @1.85 → STC 6/17 @2.30 = **long put, +$44.80 closed gain.** Session 1's "naked short / assignment tail / thesis-conflict" flag was a misread; closed and resolved.
- **S2 open book RESOLVED:** MRVL 277.5P and the QQQ 6/24 715 straddle were 6/24–26 expiries — they resolved inside the S3 window and the walk-to-zero pattern continued (−$1,624). **New S3 open book (need Monday marks):** WAL 9/18 75P (−$360 cost, **THESIS-scope → belongs in FORGE, not day-trade**), WEN 7/2 8.50P (−$132), TZA/JETD tiny.
- **Execution trap (NEW S3):** RH 0DTE auto-liquidation force-closed the 6/26 709P (~$19) before a ~$346 settlement = ~$327 lost. Need a **timestamped order-level export** to confirm auto-close vs manual exit and measure how often it bites — *the same export also closes the churn/cancel-rate gap.* → Rule 6.
- **Edge** — S2's 29-day positive sample **flipped negative with S3** (cumulative 5/1→6/26 −$1,017). Confirmed **regime-conditional**: downside-read edge in trend, inverts in whipsaw. Still unproven on a rally/grind-up tape — now also shown fragile in whipsaw.
- **Will's preferred risk unit** (still open) — $ max-loss / % portfolio / R. Rule 3 needs a number to be enforceable.
- **Churn cost** — needs an order-level export (with cancels) to confirm; CSV can't show it.

*Refresh, don't retire: update this file as the sample grows; preserve the trajectory rather than overwriting it.*
