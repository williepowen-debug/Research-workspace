# TERRY — Day-Trading Review Journal

Append-only. **Newest on top.** One entry per review. Metrics mirror to `LEDGER.tsv`; durable rules/tendencies live in `PROFILE.md`.

---

## Session 5 — 2026-08-04 · **three more 0DTE QQQ puts, all worthless — found from broker truth, not from intake**

> **Reviewed 2026-08-04 ~16:10 ET, after the close. Source: Will's Fidelity + Robinhood captures (~15:40), Will-confirmed "this is it" — the book is complete.**
> ⚠️ **These tickets were NOT in the intake.** Session 4 closed this morning believing the class was 8 tickets and ≈ −$3,081. **It was not.** Three further 0DTE puts were opened on 8/4 itself and are only visible because Will sent the broker screens. **The review loop did not surface them; a position capture did.**

### The 8/4 tickets

| Ticket | Acct | Qty | Basis | Close | Realized | Self-reconciles? |
|---|---|---|---|---|---|---|
| **QQQ 693P Aug-04 (0DTE)** | Fido | 2 | $657.33 | $2.00 | **−$655.33** | ✅ $3.29×2×100 ✓ |
| **QQQ 698P Aug-04 (0DTE)** | Fido | 2 | $489.33 | $2.00 | **−$487.33** | ✅ $2.45×2×100 ✓ |
| **QQQ 712P Aug-04 (0DTE)** | RH | 1 | ≈$119 | ≈$2 | **≈ −$117** | ⚠️ derived from −98.32% |
| **8/4 realized** | | **5** | **≈$1,266** | **≈$6** | **≈ −$1,259.66** | |
| *QQQ 720P Aug-06* | Fido | 1 | $443.66 | $417 live | *−$26.66 unrealized* | ✅ $4.44×1×100 ✓ |
| *IWM 301P Aug-06* | Fido | 2 | $231.32 | $248 live | *+$16.68 unrealized* | ✅ $1.16×2×100 ✓ |

*⚠️ Figures read from broker screenshots. Three of four self-validate (cost/share × qty = total, and cost − value = stated G/L). The Robinhood line shows only return, so its basis is back-computed. **I misread the 693P basis as $857.33 on first pass and caught it on the arithmetic** — treat all of these as broker-derived, not broker-confirmed.*

### 🔴 THE FINDING — the same-day re-entry pattern did not continue. It escalated.

Session 4's convicted leak was **four losses / four same-day re-entries — one re-entry per session.** On 8/4 that became **THREE separate 0DTE put tickets in a single session**, and every one expired worthless.

**The context they were opened into:**
- **QQQ closed +3.2%** — the strongest up-day of the recovery, and its **fourth** consecutive up-session
- the **687P from the prior day was being closed at a loss the same morning**
- **`TRY-WILL-QQQ-VFADE`'s hard condition was live** — *"becomes the ONLY QQQ short — no adds, no 0-DTE tickets alongside, or the card is void by its own terms."* **Three 0-DTE tickets voided it independently of its 712 price invalidation.**
- `QQQ_DESK_CARD.md` **§4b (P1/P2) was written this morning** off the 687P postmortem

**⇒ Class totals, corrected:** **≈ 11 closed tickets + 1 live** since 7/20 · **realized ≈ −$4,311 to −$4,371** (was ≈ −$3,081). **Walk-to-zero adds ≈ −$1,260 — all three were held to expiry.**

**⇒ Direction: 11 of 11 short**, across a window in which QQQ rose **+10.1% in four sessions.**

### What is NOT in the loss column

- **`IWM 301P` is +7.21%** — bought today at $1.16, marked $1.24. **The only green index short in the book**, and the one ticket of the day whose entry was into weakness rather than after it.
- ⚠️ **It is 2 DTE with no harvest order on it.** That is the 687P shape exactly (+23.6% Friday → worthless Monday). **`qqq/PLAYBOOK.md` G3 would have a resting sell-half at entry.** Flagged to Will 8/4; his call.

### The process finding, which is separate from the trading

**The day-desk review loop is fed by `inbox/WILL/` drops and did not see these tickets.** Session 4 was closed this morning with a total that was **~$1,260 too small**, and I published that figure to `STATUS.md` and to a brand-new `qqq/README.md`. **A review loop that can close a session while a third of the day's tickets are invisible to it is measuring intake, not activity** — `finding_count_measures_intake_not_domain`.

⇒ **The fix is not more review cadence. It is that a position capture must precede any session close.** Proposed, not adopted — needs Will.

---

## Session 4 — 7/20–8/3/2026 · the QQQ short-dated put cluster · reviewed 8/3 (live, mid-session)

> ## ✅ SESSION 4 CLOSED — 2026-08-04. **The open ticket resolved, and it resolved the worst way available.**
>
> **Will (8/4): the 8/3 QQQ 687P ×3 was CLOSED AT A LOSS, "almost worthless."** ⚠️ **`[FILL_PRICE_UNKNOWN]` — exact fill not supplied; do not treat the estimate below as a broker figure.** Basis **$2.81 × 3 × 100 = $843**. Against the last observed mark of **$0.20 (11:02)**, recovery was ≈ **$0–60** ⇒ **loss ≈ −$783 to −$843.**
>
> **⇒ Session-4 window total moves from ≈ −$2,268 (7 closed tickets) to ≈ −$3,051 to −$3,111.** The −$2,268 was *realized* only; this ticket was still open and is therefore **additive, not included.**
> **⇒ Walk-to-zero now 4 reviews / ≈ −$7,012 to −$7,072** (was 3 / ≈ −$6,229).
>
> ### 🔴 The three things this outcome actually establishes
>
> **① THE PROFIT-SIDE GAP IS NOW CONFIRMED BY OUTCOME, NOT HYPOTHESIS.** On 8/3 I wrote the cross-book finding that *"the 687P was +23.6% at Friday's close and NO rule said take it"* — and flagged that this card had **five loss-side checks and zero profit-side lines.** It has now gone from **+23.6% to near-total loss.** That is no longer a structural observation about the card; it is a **measured cost**. ⇒ **Rules P1/P2 added to `QQQ_DESK_CARD.md` §4b.** Same root cause as `TRY-VIOLET-VIXCS` (−$111.60): every trigger keyed to the move going *further*, none to being in profit.
>
> **② THE HARD STOP HAS NOW NEVER BEEN EXECUTED — 4 REVIEWS, ZERO TIMES.** The −60% line was breached **~10:10 on 8/3** and not acted on; the ticket then went to ~zero exactly as the rule predicts. The stop was written in June specifically to kill the walk-to-zero behaviour, and **the behaviour has survived every review since.** ⚠️ **A rule that has never once been executed is not a rule — it is a note.** This is the single most repeated finding on the day desk and it is now `4th_CONFIRM`.
>
> **③ SIZE: $843 = 3.4R against a 2R = $500 cap.** The cap was an unratified "empirical default" until today, which is precisely why it did not bind. **Ratified 8/4 (Will): the unit is DOLLARS, 1R ≡ $250.** Under the confirmed rule this ticket was **1.7× oversized before it was ever wrong** — and it sat in the same session as the 7/30 ticket at **$1,431 = 5.7R**.
>
> **Not scored as a rule-following failure of the *analysis*:** the read was a put on a stretched tape, consistent with the desk's one genuine edge (7/7 puts across the review). **The loss is entirely on size and management, not on direction.** That distinction is the reason this desk is worth keeping at all — and the reason the fix is two mechanical lines, not a change of view.

**⚠️ INTAKE QUALITY — "acceptable" tier, not "best."** No CSV export this session. Reconstructed from **FORGE §D-14** (ANVIL 8/2 reconcile off Will's Fidelity export + activity tab). Per-fill quantities on the 680P are **not expanded in the activity view**, and one 680P expiry row is **inferred, not observed** (FORGE labels it). Realized totals are firm because all legs are long (0 STO); the per-fill split is not. **An order-level export would nail the timestamps this review still can't see** — same gap as S2/S3.

**Marks:** live yfinance chain, pulled during the session (09:45 / 09:56 / 10:06 ET). Market OPEN. Session-4's last ticket is **still open while this is being written** — flagged as such, not scored as closed.

### Headline: seven tickets, one instrument, ≈ −$2,268 realized and the eighth is live and red

| Ticket | Expiry | Basis | Exit | Realized |
|---|---|---|---|---|
| QQQ 696P | ~7/20 | — | — | **≈ −$455** |
| QQQ 675P | Jul-30 | $391.66 | liquidated **+$1.99** | **−$389.67** |
| QQQ 672P | Jul-31 | $416.66 | **expired worthless** | **−$416.66** |
| QQQ 680P ×2 fills | Jul-31 | $1,013.99 | liquidated **+$8.51** | **−$1,005.48** |
| **QQQ 687P ×3** | **Aug-03 (0DTE)** | **$841.99** | ⏳ **OPEN** | **−$470 unrealized @ 10:06** |

**Realized on the class since 7/20 ≈ −$2,267.81.** With the open ticket marked live: **≈ −$2,738.**

### 🔴 THE FINDING — four losses, four same-day re-entries, zero flat days

This is the pattern the arithmetic alone hides. Reconstructed by date:

- **7/30:** sold the 675P for **+$1.99** — realizing **−$389.67**. **The same session**, bought the 672P **and** two 680P fills for **−$1,430.65**. That is **3.65× the size of the ticket that had just died, on the day it died.**
- **7/31:** the 672P expires worthless; the 680P is liquidated at **+$8.51**. **−$1,422.14 realized that day.** **The same session**, re-entered **687P ×3 for −$841.99.**
- **8/3 (today):** the 687P is **−56% by 10:06 ET.**

**Four consecutive tickets, each opened the same day its predecessor died. Not one flat day between them.** S3 named "revenge-build at close" as *partly corroborated, needs timestamps.* It no longer needs timestamps — the **date sequence alone convicts it**, and this time the escalation is in *size*, not just frequency.

### ⭐ The most useful finding, and it is NOT a discipline failure

**The 687P was +23.6% at Friday's close** (marked $3.47 vs $2.81 basis, QQQ ~688). It was a **winning trade** and there was **no rule anywhere that said take it.**

That is not carelessness — it is a **missing rule class**, and it is the *identical structural defect* that cost the thesis desk **−$111.60 on `TRY-VIOLET-VIXCS`** three days earlier: every trigger keyed to the move going **further**, none keyed to simply **being in profit**. Will was ruled fleet-wide on 7/31 (`NO_HARVEST_RULE`) that every card must answer this at build time. **The day-trade book has no such rule at all.** The desk card's five checks and its hard stop are **all loss-side**; there is not one profit-side line in the document.

**Cost of the gap, this ticket alone: ~$200 of a realized gain that round-tripped into a ~$470 loss.** Same defect, same week, two books, ≈ −$310 combined.

### Rules scorecard — the read was fine, the risk discipline was absent

| Desk-card rule | Verdict |
|---|---|
| **1. Puts are the edge** | ✅ **COMPLIED** — 7 of 7 tickets were puts. The side-selection discipline is holding. |
| **2. Both-ways is a chop tactic** | ✅ N/A — one-sided throughout. |
| **3. Size: 1R $250 / hard cap 2R ~$500** | 🔴 **VIOLATED ×2** — 680P **$1,013.99 = 2.03×** the cap; 687P **$841.99 = 1.68×**. |
| **4. Define the loss before the fill** | 🔴 **VIOLATED** — no written invalidation or time stop on any ticket. |
| **5. 0DTE scalps stay small** | 🔴 **VIOLATED** — the shortest-dated tickets were the **largest**, exactly inverted. |
| **⛔ HARD STOP: no-hold-to-zero** | 🔴 **VIOLATED ×3** — 675P exited at **0.5%** of basis, 680P at **0.8%**, 672P at **$0**. All three walked to zero. |

**Read discipline: intact. Risk discipline: absent.** He is picking the right side of the market and losing on structure — which is the good version of this problem, because structure is fixable and edge isn't.

### Repeat-leak tally

1. **Walk-to-zero — ✅✅✅ THIRD CONFIRMATION.** S2 −$2,793 (19 threads) · S3 −$1,624 (5) · **S4 −$1,811.81 (3)**. **Cumulative ≈ −$6,229 across three reviews.** This is now unambiguously the durable core leak. The hard stop written to kill it in June has **never once been executed**.
2. **Oversizing the worst entry — ✅ CONFIRMED AGAIN.** Biggest ticket of the cluster (680P, $1,013.99) produced the biggest loss (−$1,005.48). Third review running.
3. **Same-day re-entry after a loss — 🆕 NEW, 4-for-4.**
4. **No profit-side rule — 🆕 NEW**, and shared with the thesis book (see above).

### What improved

- **Side selection**: 7/7 puts, zero forced calls. S3's both-ways-in-whipsaw wreck did not repeat.
- **Will self-reported the trim intent on TLT** unprompted, which is how the 004 harvest got onto the record at all.
- **The 687P read was not wrong** — QQQ did sell off into 7/31 and the position went green. Honest scoring: the entry earned money and the exit rule lost it.

### Actions proposed (TERRY → Will)

1. **Add a profit-side line to `QQQ_DESK_CARD.md`** — the mirror of the hard stop. Proposed: *"up ≥50% on a 0–1DTE ticket → sell at least half, immediately, no exceptions."* Would have banked ~$200 on Friday.
2. **Enforce the existing size cap.** Two of four tickets were 1.7–2.0× a cap Will already agreed to. Nothing new to decide — just apply it.
3. **One-ticket-per-instrument-per-day.** Kills the same-day re-entry chain at the mechanical level rather than relying on restraint on a losing day.
4. **Order-level export** — the one intake upgrade that would close the timing questions three reviews running have punted.

*⏳ Session-4 close-out owed once the 687P is disposed of: final realized number + whether the −60% hard stop was executed or breached. **This entry will be amended, not rewritten.***

---

## Session 3 — 6/24–6/26/2026 (3 trading days) · reviewed 6/27 · **extends Session 2 (3 new days, same account)**

**Intake:** Robinhood **CSV export** covering the full 5/1→6/26 window (520 rows). The 5/1–6/23 portion reproduces Session 2 to the penny (+$2,951.67, 148 closed threads) — which validates the method, so the new number is trustworthy. **New content = the 3 days 6/24–6/26.** **Marks:** yfinance live this session (worked, unlike S2) — used to verify intraday tape + settlement values.

### Headline P&L (FIRM — 0 STO, all long)

**New window 6/24–6/26: −$3,968.84 realized over 52 closed threads.** That **erased the entire +$2,951.67** from the prior 7 weeks. **Cumulative 5/1→6/26 is now −$1,017.17.**

- **Losses ESCALATED daily:** 6/24 −$425 → 6/25 −$1,443 → 6/26 −$2,100. Getting worse, not stabilizing — a revenge cycle, confirmed by **two intraday ACH deposits ($200 + $100) mid-session on 6/26**, the worst day. Funding a losing day to keep trading is a **new tendency** (not seen in S1/S2).
- **The QQQ 0DTE engine ran in REVERSE.** In S2 it was the +$3,044 engine; in 3 days it gave all of that back and more. Worst threads are QQQ 0DTE **puts AND calls on the same days**, both losing.

### Root cause #1 — both-ways tactic into a whipsaw tape (the bulk of the loss)

Will's stated plan: *"trying to catch movement going either way."* Intentional both-ways (28 call + 30 put BTO entries; both-sided all 3 days). But the tape wasn't chop — it was **whipsaw**, and both-ways is built for chop, not whipsaw:

| Day | QQQ path |
|---|---|
| 6/24 | 715 → **704** → 710 |
| 6/25 | **726 → 705** → 716 (21-pt round trip) |
| 6/26 | 707 → 715 → **702** → 706 |

Three days of 2–3% intraday reversals that round-tripped *through* the strikes in both directions → full premium paid on both legs, both decayed/stopped. **The tactic was wrong for the tape, independent of anything else.**

### Root cause #2 — EXECUTION TRAP (not a discipline failure): RH 0DTE auto-liquidation

Will flagged a "sudden EOD drop, but my puts had already auto-sold — almost seemed engineered." **Verified real, with a number:**
- 6/26 final 5 min (3:55–4:00pm ET): QQQ **709 → 705.21**, closed ~705.5. A genuine close-of-day flush.
- **QQQ 6/26 $709 Put:** bought $292, exited at ~$19 (−$273) — but at the 705.54 settlement it was ~$3.46 ITM = **~$346**. Hold-to-settlement was a **+$54 winner**; the early exit made it a −$273 loser. **~$327 swung against him on that one contract** in the final minutes.
- **Mechanism, not conspiracy:** the EOD move is dealer-gamma + MOC-imbalance flow (mechanical, concentrates in the last 10 min); the exit is **Robinhood's expiration-day auto-liquidation** force-closing 0DTE longs before settlement. Not aimed at Will — but it *is* systematic, which means avoidable. **This bucket is an execution-rail problem (TERRY's lane), separate from discipline.**
- **Caveat:** CSV has no intraday timestamps → can't *prove* auto-close vs. a resting order; the price math ($19 vs ~$346) is certain, the auto-close *cause* is likely-but-unconfirmed. An order-level/timestamped export would nail it.

### The validated leak fired again — CONFIRMED REPEAT

**Walk-to-zero (S2's one convicted leak): −$1,624 across 5 expired-worthless threads** — MRVL 6/26 260P −$720, QQQ 6/25 705P −$651, USO 108C/110C, WEN 8C. Plus **overnight 4W/13L** this window (vs S2's +$3,464 16W/6L) — but that's the *same* walk-to-zero leak in an overnight costume (multi-day holds carried to $0), not a separate overnight problem. **Second review running = this is now a confirmed pattern, not a one-off.**

### Rule scorecard (current PROFILE rules)

- **R1 Loss-side time-stop / no walk-to-zero:** ✗✗ −$1,624 to $0 again. *The repeat.*
- **R2 No new premium after a big move:** ✗ chased both sides of the 6/24 gap + intraday reversals.
- **R3 Per-idea max-loss cap:** ✗ MRVL $720; four QQQ threads >$400.
- **R4 Protect the QQQ engine:** ✗ revenge-size turned the one proven process into the wreck.
- **R5 Pre-register overnight holds:** ⚠ 13 overnight losers + WAL/WEN open — decisions or defaults?

### Open book at 6/26 (cost basis — need Monday marks)

- **WAL 9/18 75P (−$360 cost)** — *thesis-aligned* (REGINALD WAL bear; ~mid-July print test). **NOT day-trade scope** — belongs to the thesis book, flag to FORGE.
- WEN 7/2 8.50P (−$132), TZA/JETD tiny stock.

**New rule this session earns (execution — see PROFILE R6):** don't hold 0DTE into RH's auto-liquidation window (~3pm ET on) with a directional lean into the close — exit on your terms before 3pm, or hold to settlement *with* buying power, or don't run 0DTE you mean to carry to the bell.

**Biggest mistake (discipline):** running the chop tactic (both-ways) into a whipsaw, then revenge-funding the worst day.
**Not-your-fault loss:** RH force-closing the 709P before a settlement it would have won (~$327).
**Watch next review:** Did both-ways get throttled in whipsaw tape? Did the 0DTE auto-liquidation rule hold? Did escalation/revenge-funding stop? Provide a **timestamped order export** to confirm the auto-close mechanism.

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
