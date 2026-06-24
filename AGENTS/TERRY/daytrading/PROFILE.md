# TERRY — Will's Day-Trading Profile & Rulebook

**Started:** 2026-06-23 · **Re-based 2026-06-24** (Session 2, CSV export, 29 trading days 5/1–6/23)
**Status of evidence:** Session 2's clean CSV **retracted two Session 1 "leaks" as data artifacts** (see ⚠ below) and **firmed the realized number** (+$2,951.67, no short/assignment ambiguity). Of the original five suspected leaks, the verified data convicts **one**: holding losers to $0 expiry. Edge is now mildly *supported* (29-day positive sample, puts the driver) but still regime-thin — June was a selloff month and Will's edge is downside reads.

> ⚠ **Artifacts corrected by Session 2 (do not re-assert without short/STO evidence):**
> - **No naked short premium ever existed** — 0 sell-to-open codes in the full CSV. The "assignment tails / income" leak was a pasted-feed misread. Realized P&L is firm, not a range.
> - **Overnight holds were net winners** (+$3,464, 16W/6L), not "the clean losing pattern." Session 1's 0W/3L was a 5-day crash-sample fluke.
> - **Long calls were net positive** (+$604), not losing. Puts simply dominate.

---

## Where the edge lives (keepers — protect these)

1. **React & exit, don't predict & hold.** Every clean winner monetized a move *already on the tape*, taken off the same session (AAOI −13.9% → +310; CCL −4.9% → +150; sold the crash-day roll-legs into the move).
2. **Single-name down-reads on a risk-off day** — AAOI +310, CCL +150, SOXX +314, SMCI puts + short TQQQ on 6/23. Reads relative beta/weakness well. *(Now backed by a 29-day positive sample, but the window was a selloff — unproven on a rally.)*
3. **Cuts winners fast.** Genuinely good reflex. The problem is it *only* fires on greens — losers get walked to expiry instead (see Leak 1 / Rule 5).
4. **QQQ 0–1 DTE scalping is the engine** — **+$3,044** of the month's realized. Not breakeven churn (Session 1's worry); it's where the money is made. Protect it from the expiry-bleed leak that surrounds it.

## The leaks (ranked by VERIFIED damage)

1. **Holding losers to $0 expiry** — the one verified, money-losing leak. **−$2,793 across 19 expired-worthless threads** (QQQ 6/11 694P −554, 6/17 735C −412, 6/16 744C −366, 6/9 722C −251, 5/8 690P −238, IWM 6/11 281P −182…). Winners exit in minutes; directional losers get walked to zero. This single asymmetry nearly halved the +$5,745 of sold-trade gains. *(This is the real content of old Rule 5; it is NOT about overnight-vs-intraday — overnight was profitable.)*
2. **Buying premium AFTER the move (peak-IV chase).** MRVL 277.5P @ $13 = **$1,300 after a −9.4% flush** (open, the worst risk on the book); QQQ 6/24 715 straddle bought into the 6/23 crash; index bounce-forces (715C, USO 113C). Top-ticks IV in the direction of an already-made move.
3. **Oversizing the worst entries.** Biggest bet = worst entry: MRVL **$1,300** = 10× its SMCI **$135** sibling. Size inversely correlated with entry quality.
4. **Churn (unquantified this round).** 28 of 155 contracts re-entered same strike. Cancel rate / 20.2% **could not be recomputed** — settled-activity CSV has no canceled orders. Needs an order-level export to confirm whether churn is shrinking. *Was profitable churn this month (QQQ scalps), so demoted pending evidence it actually costs money.*

## Named tendencies (tracked in LEDGER.tsv)

| Tendency | Pattern | Status |
|---|---|---|
| **Disposition (reversed)** | cuts winners fast, **holds losers to $0 expiry** (−$2,793) — a profit-stop with no loss-stop | ✅ verified, the core leak |
| **Put vs call** | long puts the driver (+$2,347); calls positive but secondary (+$604) | ✅ refined (calls not a loss) |
| **Sizing** | biggest bet = worst entry (MRVL $1,300 vs SMCI $135) | ✅ holds |
| **Post-move chase** | buys premium into an already-made move (MRVL, index bounces) | ✅ holds |
| **DTE** | ~~0–1 DTE wins / overnight loses~~ — **retracted**; overnight 16W/6L +$3,464 | ❌ artifact |
| **Vol-timing** | claimed "sells into calm" — **moot**, no premium was ever sold | ❌ artifact (no shorts) |
| **Time-of-day** | hesitate at open → over-trade flush → revenge-build at close | ⚠ unverified from CSV (needs intraday timestamps) |

---

## The 5 Rules (enforceable at order entry) — re-ordered by verified damage

1. **Loss-side time-stop / no walk-to-zero.** *(the verified leak.)* Mirror the winner-cut reflex on reds: a directional option that's wrong by your stop comes off — it is **never** held to expiry to save a few cents of premium. −$2,793 says so.
2. **No new long premium after a big move** (>5% single-name / >2% index) — you may only *exit*. Killed MRVL's entry; would have killed the 6/23 crash straddle.
3. **Per-idea max-loss cap,** sized *below* a typical scalp stack — cap the size, cap the chase. (MRVL $1,300 was the cap-breaker.)
4. **Don't fight what's working: protect the QQQ 0–1 DTE scalp engine.** It made +$3,044. Don't let revenge-size or expiry-bleed contaminate the one proven process.
5. **~~Flat by the close~~ → Pre-register every overnight hold.** Overnight was *profitable*, so this is no longer a prohibition — but every carried position still needs a written invalidation + time-stop so it's a *decision*, not a default. *(Old "short credit ≠ income" rule retired to hygiene-only: no shorts have ever appeared; re-activate only if an STO shows up.)*

---

## Open / unresolved

- **OZK $50P 8/21 was NOT a naked short** — CSV shows BTO 6/15 @1.85 → STC 6/17 @2.30 = **long put, +$44.80 closed gain.** Session 1's "naked short / assignment tail / thesis-conflict" flag was a misread; closed and resolved.
- **Mark the open book exactly** — needs a positions/marks export (live data was down this session). MRVL 277.5P $1,300 and the QQQ 6/24 715 straddle are the items that matter.
- **Edge** — now 29-day positive, but the window was a selloff and the edge is downside reads. Unproven on a rally/grind-up tape.
- **Will's preferred risk unit** (still open) — $ max-loss / % portfolio / R. Rule 3 needs a number to be enforceable.
- **Churn cost** — needs an order-level export (with cancels) to confirm; CSV can't show it.

*Refresh, don't retire: update this file as the sample grows; preserve the trajectory rather than overwriting it.*
