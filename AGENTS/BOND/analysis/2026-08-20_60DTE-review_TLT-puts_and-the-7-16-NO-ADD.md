# BOND — 60-DTE REVIEW (OVERDUE) + does Will's 7/16 NO-ADD need revisiting?

**Date:** 2026-08-20 (Thu) · **Author:** BOND · **Trigger:** Will asked in-session — *"'Will's 7/16 NO-ADD stands' — should we revisit this? It is now 8/20."*
**Instrument:** `TRY-FIRE-004` — 25× TLT Sep-30-2026 77P. **TERRY owns the card, the roll, the harvest and the sizing. BOND owns the channel read only.**

---

## 0. THE SHORT ANSWER

**The NO-ADD does not need revisiting. A different, overdue review does — and asking the question surfaced it.**

- **Revisiting the NO-ADD could only re-confirm it.** It governs ADDING; no add-gate has fired; the one surviving gate (DFII10 >2.50) is **9bp away and moved AWAY** (2.44 [8/17] → 2.41 [8/18]). Gates (b), (c), (d) are resolved-and-dead. There is nothing on the add side to reopen.
- 🔴 **What IS overdue is the 60-DTE review, by 19 days.** Sep-30 expiry ⇒ 60-DTE fell on **2026-08-01**. The leg is at **41 DTE** today. This checkpoint is mandated in **four** BOND files (`CLAUDE.md` §EXIT RULES 4, `THESIS.md`, `STATUS.md`, `TRADE.md`) and **I can find no record of it ever running.**
- **The right question is not add-or-not. It is hold / roll / harvest — and under root rule #7 the facts point at ROLL, not trim.** That call is **TERRY's with Will's approval**, not BOND's.

---

## 1. Why the 60-DTE review going missing is the real finding

The NO-ADD was never the stale thing. **It was load-bearing, correct, and I restated it accurately every session.** Restating a correct ruling is not a defect.

**The defect is that a time-based checkpoint has no publisher.** An add-gate fires when a *level* crosses — something recomputes it every boot and it announces itself. **A DTE checkpoint fires when the CALENDAR crosses, and nothing on this desk watches the calendar against a position.** `boot_recompute` checks levels. `docket_check` checks the issuer's auction calendar. `closeout_check` checks assertions. **Nothing maps expiry dates to today.** So the checkpoint passed on 8/01 in silence and stayed silent for 19 days.

⚠️ **This is the same shape as the August-refunding miss** (`MEMORY.md`, 8/18): *a stale number looks wrong eventually; a missing event looks like nothing.* There it was a missing docket row. **Here it is a checkpoint with a date and no watcher.**

---

## 2. What has actually changed since 7/16 — and one item is genuinely new

| | 2026-07-16 (NO-ADD ruled) | 2026-08-20 (today) |
|---|---|---|
| DTE | ~76 | **41** |
| Size | 30× (pre-fill; filled 7/20) | **25×** (Will sold 5 at 3.23× on 7/31) |
| Mark vs fees-in basis | — | **0.69×** — underwater [TERRY 8/20] |
| Live add-gates | (a) + (b) + (c) + (d) | **(a) only** — (b)(c)(d) resolved-and-dead |
| Gate (a) distance | — | **9bp, and WIDENING** (was 6bp on 8/17) |
| Exit gate | none registered | **`GATE-TERRY-007`** — 5 consecutive DGS10 closes <4.50 ⇒ EXIT (Will-ruled 8/19) |
| Mechanism | intact | **intact — 13 straight benign resolutions**, composite 12/35 unchanged |

**Two of these matter for the decision:**

**(a) Will already revisited the EXIT side one day ago.** Rulings B and C were encoded on the card **8/19** (`GATE-TERRY-007`). So the position is not unattended — **the exit branch got fresh attention yesterday; the TIME branch is the one nobody has touched.** DGS10 is **4.71**, nowhere near the 4.50 count, so that gate is dormant and not the live question.

**(b) 🔴 `sb0607` is new information that post-dates the NO-ADD and is priced into no gate.** From **9/9**, Treasury doubles long-end buybacks ($2bn → ≥$4bn/op, 10-20y and 20-30y) through 11/4. **That is an official bid in exactly the sector this position is short, for 21 of its remaining 41 days — more than half its remaining life.** The card pays on a **GAP**; a grind pays $0. **An official buyer standing in the sector compresses gap probability in the back half of the position's life.** On 8/19 that bid was worth **TLT +1.67% in a single session** — the largest one-day rally of the episode, on flow, not data.

⚠️ **State the counter-argument, because it is real:** `sb0607` is liquidity-support on the letter (capped, dated, no yield target) and **the 30Y made a 19-year high THROUGH the existing programme.** It is not a yield cap. It changes the *distribution*, not the direction.

---

## 3. The rule that actually applies

> **Root rule #7:** *"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain."*

**Thesis: intact.** Composition has not failed at any tenor since 7/9 across 13 tests; the August refunding cleared clean at all three tenors; composite unchanged 12/35; nothing crossed a pre-registered line.
**Timeline: uncertain.** The only live gate moved away, and an official bid arrives 9/9 for the back half of the leg's life.

⇒ **Thesis intact + timeline uncertain is the textbook rule-#7 ROLL case, and explicitly NOT a trim case.** ⛔ **BOND is not proposing a roll — vehicle, strike, expiry, size and cost are TERRY's on TERRY's rules with Will's approval.** This desk's contribution is the channel read that the *timeline*, not the thesis, is what moved.

---

## 4. What I am NOT saying

- ❌ **Not proposing an add.** No gate fired; the nearest one is widening. **The position working and the thesis confirming are not add-gates** — this desk has said so on every surface and it holds today.
- ❌ **Not proposing a trim.** Under rule #7 a trim asserts the thesis is broken. It is not.
- ❌ **Not calling the position wrong.** 13 consecutive benign mechanism resolutions is the thesis's *own* record, and the channel read is unchanged.
- ❌ **Not overriding the NO-ADD.** It stands, and it stands correctly.

---

## 5. Recommendation

1. **Keep the 7/16 NO-ADD.** It is correct and nothing has fired against it. ✅ No revisit needed.
2. 🔴 **Run the overdue 60-DTE review as a TERRY deliverable, with Will's word on the outcome.** Question for that review: *hold to expiry, or roll duration past the 9/9–11/4 buyback window?* — the window covers 21 of 41 remaining days.
3. **Fix the class, not the instance:** add an expiry-vs-today check to `boot_recompute` so any open options leg prints its DTE and flags a crossed checkpoint. **The checkpoint existed in four files and fired in none of them** — detection was never the gap; a watcher was.

**Routed:** TERRY (owner, items 2), PROME (visibility + the ledger/gate side), Will (the decision).
