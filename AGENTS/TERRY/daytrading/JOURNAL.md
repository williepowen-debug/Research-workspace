# TERRY — Day-Trading Review Journal

Append-only. **Newest on top.** One entry per review. Metrics mirror to `LEDGER.tsv`; durable rules/tendencies live in `PROFILE.md`.

---

## Session 2 — 5/1–6/23/2026 (29 trading days) · reviewed 6/24 · **re-bases Session 1**

**Intake:** Robinhood **CSV export** (`May_1_2026—Jun_23_2026.csv`), 357 option/stock fills, 155 distinct contracts. This is the cleaner-data re-run Session 1 asked for, and it extends the window back to 5/1. **Marks:** live data unavailable this session (no yfinance / Yahoo 429) — open book marked qualitatively vs the 6/23 crash closes; exact option marks flagged for Will.

### ⚠️ Three Session 1 conclusions were data artifacts — corrected here

1. **There was NO naked short premium. Zero.** The CSV has **0 sell-to-open (STO) codes** — all 189 opens were BTO (long). The OZK 8/21 50P, the "6/18 726C/730C," "SOXX 635P," "USO 112C" that Session 1 flagged as short *assignment tails* were all **long round-trips** (BTO→STC). The "1S/2S" tag on expiration rows is Robinhood notation, not a short marker — it fooled the pasted-feed read. **Consequence: realized P&L is a firm number, not a $700–$3,300 range.** Rule 3 (short credit ≠ income) had **zero real violations** this month.
2. **Overnight holds were the biggest *winners*, not the clean loser.** Session 1 (5-day crash sample) said overnight = 0W/3L, −$767. Full month: **overnight closed 16W/6L, +$3,464** — the two largest wins of the month were 1–3 day holds (QQQ 6/23 735P +$1,522; QQQ 6/15 722C +$1,173). The "DTE is the win/loss divider" claim does not survive the larger sample.
3. **Long calls did not "lose."** Month: long puts +$2,347 (83 closed) vs long calls **+$604** (65 closed) — calls modestly positive. Puts dominate (downside read is the real edge), but calls were not a net loss.

### Headline P&L (FIRM)

**Realized 5/1–6/23: +$2,951.67.** = +$5,744.83 from sold round-trips − **$2,793.16 bled on options held to $0 expiry**. Deposits +$1,283; fees −$20.

- **Engine: QQQ +$3,044** (116 threads, mostly 0–1 DTE scalps). Single-name put winners: SOXX +$314, AAOI +$310, CCL +$150. Everything else net small-negative.
- Intraday closed 65W/42L +$2,281; overnight closed 16W/6L +$3,464.

### The one validated leak: **holding losers to $0 expiry** (this is the real Rule 5)

**−$2,793 across 19 expired-worthless threads.** Biggest: QQQ 6/11 694P −$554, QQQ 6/17 735C −$412, QQQ 6/16 744C −$366, QQQ 6/9 722C −$251, QQQ 5/8 690P −$238, IWM 6/11 281P −$182. Winners get cut in minutes; losers get walked to expiration. The disposition asymmetry (cut greens fast, hold reds to zero) is the **only** behavior the verified data convicts — and it nearly halved the sold-trade gains.

### Rule scorecard (this month, verified data)

- **R1 Flat-by-close:** not a leak this month — overnight was net +$3,464. *Reframe needed (see PROFILE).*
- **R2 No long premium after a move:** ✗ MRVL 277.5P @ $13 = $1,300 *after* −9.4% (open, peak-IV chase); QQQ 6/24 715 straddle bought on the 6/23 crash.
- **R3 Short credit ≠ income:** ✓ no violations (no shorts existed). Retain as hygiene only.
- **R4 Per-idea cap:** ✗ MRVL $1,300 = 10× the SMCI $135 sibling; biggest bet, worst entry — pattern holds.
- **R5 Loss-side time-stop:** ✗✗ the −$2,793 expiry bleed. **The validated leak.**

### Open book at 6/23 (cost basis −$3,883; live marks needed)

Day-trade: MRVL 6/26 277.5P **$1,300** (post-flush chase, worst risk), QQQ 6/24 715C **$654** + QQQ 6/24 715P **$585** (= long straddle into today's expiry, $1,239), USO 7/8 113C $370, SMCI 6/26 33P $135, USO 3 shares ~$346. Thesis-book (NOT day-trade scope — flag): WAL 9/18 75P $360, NCLH 9/18 19P $143. Residual: TZA/JETD tiny stock.

**Scope note:** this account mixes day-trade scalps with thesis-book swing puts (WAL/NCLH/OZK). The realized number blends both. Keep mining day-trade behavior; thesis P&L belongs in FORGE.

**Cannot recompute from this file:** cancel rate / 20.2% — settled-activity CSV contains no canceled orders. Round-trips on same contract: 28 of 155.

**Biggest mistake (verified):** walking directional index losers to $0 instead of mirroring the winner-cut reflex (−$2,793).
**Best behavior:** the QQQ 0DTE put scalping + single-name down-reads (AAOI/CCL/SOXX) — react-and-exit, the edge expressed cleanly.

**Watch next review:** Did expiry-bleed fall from −$2,793 / 19 threads? Did MRVL get cut or walked to zero? Did the post-move chase (R2) stop? Provide a **positions/marks export** so the open book can be marked exactly.

---

## Session 1 — 6/16–6/23/2026 (5 trading days) · reviewed 6/23 evening

**Intake:** pasted broker activity feed (assignment outcomes + roll strikes not visible → several figures `UNKNOWN`/gated).
**Marks:** 6/23 closes. QQQ 713.65 (−3.29%, a crash day); semis/AI gapped down hard (MRVL −9.4%, ARM −10.1%, AAOI −13.9%, SMCI −6.0%, TQQQ −9.9%, SOXX −7.9%); banks green (WAL +2.4%, OZK +1.6%).

**Headline P&L:** +$3,336 in-window — **but not a real number.** Floor **+$719–$992** if four short options assigned; **clean / no-tail / no-churn = +$460** (AAOI put +310, CCL put +150). The spread *is* finding #1: half the headline has an undefined loss living in un-expired short options.

**Rule scorecard (baseline — all 5 tripped; the rules were *derived* from these):**
- **R1 Flat-by-close:** ✗ multiple overnight holds = the only clean losing category (0W/3L, −$767), +$834 still open.
- **R2 No long premium after a move:** ✗ MRVL 277.5P @$13 post −9.4%; 715C & USO 113C bounce-buys into the crash.
- **R3 Short credit ≠ income:** ✗ four assignment tails (6/18 726C/730C, SOXX 635P, USO 112C) + open OZK 8/21.
- **R4 Per-idea cap:** ✗ MRVL $1,300 (10× the SMCI $135) and the single worst entry.
- **R5 Loss-side time-stop:** ✗ QQQ 721P 6/18 held to ~zero (−$523).

**Biggest mistake:** booking naked short premium as income → undefined loss on ~half the headline.
**Best behavior:** AAOI put +$310 — caught the −13.9% move, cut it same session. The edge, expressed cleanly.

**Open at review:** QQQ 715C 6/24 ($654, near-dead), USO 113C 6/24 ($180, near-dead), MRVL 277.5P 6/26 ($1,300), SMCI 33P 6/26 ($135, well-sized), WAL 75P 9/18 ($360), NCLH 19P 9/18 ($143), OZK 50P 8/21 **SHORT** (+$230 credit), QQQ/USO roll-books `UNKNOWN`.

**Watch next review:** Did cancel-rate fall from 20.2%? Overnight-hold count from 3? Long-call directional entries stop? Naked-short count fall from 1 (OZK)? Did any rule survive a full session unbroken?

---
