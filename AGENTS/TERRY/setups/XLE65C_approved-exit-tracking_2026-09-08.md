# XLE September 30 $65C — existing approved exit tracking
**Setup ID:** `TRY-EXIT-XLE65C`
**Updated:** 2026-09-09 21:1x ET (owner expiry-pass write-back; prior 2026-09-08T17:27:10-04:00)
**Terry verdict:** CLOSED
**Tracking state:** CLOSED — 2026-09-11, execution receipt received, **REALIZED −$77.33 / −33.97%**; nothing further tracked. *(was ~~CONDITIONAL~~ / ~~STAGED — approved exit selected; execution unconfirmed~~ — see the CLOSED block at the foot of this file.)*

This is owner write-back of WQ-168 §⑦, approved by Will September 3 at 12:45 ET. No new proposal or approval is requested. Full original expiry card: `PROME/inbox/processed/2026-09-03_from-TERRY_expiry-pass-Sep18-Sep30-seven-lines-007-grade-UNKNOWN-mirrors.md`. Its September 6 “Sat” labels are calendar errors: that date was Sunday. The date and approved rule are unchanged.

## Observed condition and consequence
XLE September 8 regular close **$64.77**, below **$66.50** by **$1.73**. Source: Yahoo **MIRROR**, daily bar and regular-close metadata agree, metadata September 8 16:00 ET; capture September 8 16:21:41 ET in PROME's preserved evidence, sha256 in `../outbox/2026-09-08_owner-market-evidence.json`. This is not an independently obtained exchange close.

The existing rule selects **sell to close both XLE September 30, 2026 $65 calls at the bid on the September 9 open**. Will checks the live Fidelity position and open orders first. The dated exit still binds on a red open; a September 9 rebound does not replace the September 8 test. No order submitted or fill claimed by TERRY. Current holdings/orders/executable bid/fill are **UNKNOWN**; `[POSITION_STATE_INCOMPLETE]`. Do not sell contracts no longer held or duplicate an existing order.

## 2026-09-09 21:1x ET — SELECTED at the 9/8 close; fill UNKNOWN pending Will's receipt

**Record, in the required form: SELECTED at the 9/8 close; fill UNKNOWN pending Will's receipt.** The 9/8 test ($64.77 < $66.50) selected the already-approved SELL BOTH at the 9/9 open. Execution is Will's hand at the broker; **the repo has no fill — quantity, price, time and account are all UNKNOWN.** No proceeds booked, no holdings removed, no re-approval requested.

⛔ **NOT re-litigated on the day's colour (Non-Negotiable #12).** For the record and *not* as a reason to revisit: **XLE closed $65.31 on 9/9, +0.83% — a GREEN day, and $0.54 above the $64.77 that selected the exit.** The dated test ran on the 9/8 close and is spent; a 9/9 rebound does not replace it and does not reopen it. The rule was ruled cold, before the print.

**Marks at 9/9 close (MOMENT properties, `RISK_RULES` #14 — recorded, not a proposal):** XLE Sep-30 **$65C bid `1.65` / ask `1.75` / mark `1.70`**, spread 5.88%, IV 25.51%, OI 7,380, vol 519, last trade 15:58 ET, no quote flag (`chain_fetch.py XLE 2026-09-30 --type call --no-cache --legs 65`, 21:07 ET). **If still held**, ×2 ⇒ ≈**$330 at bid / $340 at mark** vs **$456 basis** ($2.28 ×2) ⇒ **−$126 / −27.6%** at the bid. 21 DTE. **These are post-close quotes, not executable, and they do not establish that the position is still held.**

PROME L252 may consume this owner observation. **L253 remains open until an execution receipt** (actual quantity, price, time, account and remaining disposition). No sale proceeds or realized P/L estimated. Track as STAGED until execution is reported; “selected” does not mean “filled.” No add, roll, replacement threshold or new sizing.

---

## 2026-09-10 Thu ~12:2x ET — ⑦ IS CONSUMED, ONE CONTRACT SURVIVED IT, AND THIS SECTION IS THE RULING REC IT HAS NEVER HAD (D-49)

**MARKETS OPEN. Every price in this block is a LIVE intraday quote with its pull stamp on its face — not a close, not a mark carried from a state file (root rule #4; `RISK_RULES` #5).** ⛔ **`$0` moved. No order placed, replaced or cancelled. No threshold adopted. TERRY proposes; Will [Approve]s.**

### What changed, from the broker record — not from this desk

`FORGE/STATUS.md` (PROME/ANVIL reconcile of the 9/10 ~10:3x ET Fidelity positions view + Activity & Orders, commit `20aefcf05`): **XLE Sep-30 $65C qty 2 → 1.** One contract SOLD; **it is NOT among the activity ledger's four visible rows (all dated 9/10)** ⇒ the sale is before today or outside the screenshot crop. **Date, price and account UNKNOWN — D-49.** Basis of the survivor **$227.67 = ½ × $455.34** (ANVIL lot arithmetic ✓, i.e. a sale at lot basis, not a re-basing).

⛔ **WQ-168 ⑦ ("SELL BOTH at the bid on the 9/9 open unless XLE closed ≥ $66.50 on 9/8") is CONSUMED, and NOT re-litigated** — `RISK_RULES` **finding #12**, *a fired kill-switch is held, not re-litigated*. ⚠️ **CITATION CORRECTION:** this file's 2026-09-09 block above, and `STATUS.md`'s 9/9 block, cite this rule as *"Non-Negotiable #12."* **There is no Non-Negotiable #12 — that list ends at 8.** The rule is **durable finding #12** in `RISK_RULES.md`. The substance was right in both places; only the list name was wrong. *(Root `CLAUDE.md` citation discipline: name the list, never a bare "#12".)*

⇒ **The dated test is spent. The question this block answers is the NEW one: the surviving ×1 rides with no rule on file.**

### Live marks (MOMENT properties, `RISK_RULES` #14 — recorded with their stamp, never carried forward)

| Field | Value | Source / stamp |
|---|---|---|
| XLE spot | **$65.14 (−0.26%) — a RED day** | `fetch.py price XLE`, 2026-09-10 **12:24 ET**, live intraday |
| Sep-30 $65C | **bid `1.49` / ask `1.62` / mark `1.56`** | `chain_fetch.py XLE 2026-09-30 --type call --no-cache`, fetch **12:24 ET**, last trade **12:06 ET** |
| Spread / IV / OI / vol | **8.36% · 24.88% · OI 7,320 · vol 128** | same pull. **No quote flag** (not LOCK/XSD/DEAD/NOBID) |
| Survivor ×1 at the bid | **$149.00** vs **$227.67** basis ⇒ **−$78.67 / −34.6%** | arithmetic |
| DTE | **20 calendar / 14 trading sessions** (9/11 → 9/30) | calendar |

⚠️ **Chain-quality read, stated not hidden:** the Sep-30 XLE call strip returned **NONMONO on 25 of 57 rows (44%)** and 17 DEAD rows out at the wings. Per `chain_fetch.py`'s own doctrine that is a verdict on the **STRIP**, not on this strike — and **the $65 line is exactly what it says trust: a round-number strike with OI 7,320, vol 128, an 8.36% spread and a 12:06 ET print, carrying no flag.** The figures above are usable; the wing strikes on that chain are not.

### ★ THE STRUCTURE, IN ONE NUMBER

**$65 strike vs $65.14 spot ⇒ intrinsic $0.14. The bid is $1.49. ⇒ `$1.35` — 90.6% of what this contract is worth — is TIME VALUE, and time value goes to zero with certainty.**

- **Break-even $67.28** (= 65 + 2.28 basis) = **+3.29% from $65.14, required inside 14 sessions.**
- **The tape is not delivering it:** XLE has closed **64.77 [9/8] → 65.31 [9/9] → $65.14 [9/10 12:24 live]**. Three sessions, net **+0.57%**, no trend.
- **Decay, √t-scaled off the $1.35:** ≈**−$26 next week** (20 → 13 DTE), ≈**−$35 the week after** (13 → 6 DTE), then the rest. **Accelerating, and it is the majority of the position.**
- `RISK_RULES` **#10** (surface the MARK before recommending a cleanup exit): **the mark is NOT unfavourable** — 8.36% spread, OI 7,320, a fresh print, no sanity flag. #10's "propose a window-trigger, not a mechanical close-now" branch is the one for a **bad** mark; **this mark does not trigger it.**

### 🎯 REC (a) — TWO BRANCHES, BECAUSE D-49's ANSWER DECIDES WHICH ONE APPLIES

**The branch point is a fact only Will holds: was the 1-lot sale a partial fill of the ruled 2-lot, or a deliberate decision to keep one?** ⛔ **TERRY picks neither** — ANVIL labelled the same three conjectures (a)/(b)/(c) and picked none.

**BRANCH 1 — DEFAULT, and it is what I recommend if Will has no positive intent on the survivor: SELL the ×1 TO CLOSE AT THE BID ON THE NEXT REGULAR OPEN.**
This is **completion of an already-approved action, not a new proposal.** ⑦'s dated test fired against BOTH contracts; one leg went unexecuted. Nothing in the tape since has argued the other way — XLE is **+0.57% over three sessions and $2.14 below the $67.28 break-even** — and every day of delay spends time value that is 90.6% of the remaining mark.

**BRANCH 2 — IF Will answers D-49 with "the ×1 is a deliberate keep": then it needs a rule, and here it is, OR-joined.**

| Line | Term | Why this and not something else |
|---|---|---|
| **HARVEST** | First XLE **regular-session official close ≥ $67.28** ⇒ **SELL ×1 at the bid at the next regular open.** | $67.28 is the position's **own break-even**, not an invented level. ⚠️ Named honestly: at $67.28 this contract **recovers basis, it does not profit** — the profit zone starts above it. `RISK_RULES` **#9** wants a rule that fires when the position is *merely* profitable, and on a −34.6% leg the first such zone IS break-even. |
| **TIME (backstop)** | **UNCONDITIONAL SELL at the bid on the open of Fri 2026-09-25** — 5 sessions before expiry, ~5 DTE. | **A date cannot fire late.** ⛔ **Deliberately NOT 9/28 (2 DTE):** by then ~all $1.35 of extrinsic is gone and the backstop is ceremonial — it would recover only intrinsic. At **9/25** roughly **$0.67** of extrinsic is still recoverable (√t off $1.35). **A backstop should salvage something, not merely witness the expiry.** |
| **JOIN** | **OR.** Whichever comes first. | ⛔ Never AND-joined. |
| **FALSIFIER (dated, gradeable)** | If **9/30 arrives with neither line executed**, this is a specification and not a control ⇒ record it as such on this card (`RISK_RULES` **#16** corollary: **count executions, not specifications**). | The four-times-specified-zero-times-executed class. |

### Root-rule application, stated rather than skipped

- **Root rule #6 (puts on green days, calls on red days): DOES NOT APPLY — and it is named so the omission is not read as an oversight.** #6 is a **proxy** for one question: *am I paying up for convexity?* **A SALE of a call buys no convexity, so the proxy has no object.** ⛔ **This is NOT a break of root rule #6 and MUST NOT be logged as one** — a break requires a fill whose convexity price the proxy misprices, and there is none here. *(Same reading applied to the USO share sale on `USO-SHARES_management-card_2026-09-09.md` §6.)* ⚠️ **Citation discipline (root `CLAUDE.md`): this is root rule #6, NOT Non-Negotiable #6 (*no roll-by-hope*) — the two lists are independent and both are cited by number.**
- **The day-colour analogue that DOES bite for a sale — selling into weakness — is named with its figure, not waved past.** XLE is **red −0.26%**, so BRANCH 1 sells on a down day. **Magnitude: $0.17 of underlying move against $1.35 of decaying extrinsic in the same contract.** ⇒ the day's colour is **noise at roughly an eighth of the thing being lost to the clock**, and waiting for a green day is a **chase dressed as patience** — the exact move the root-rule-#6 adjudication test in `RISK_RULES.md` exists to refuse. **Written in figures, before any fill, as that test requires.**
- **Root rule #7 (roll duration, don't trim size): NOT a trim and NOT a roll.** No roll is proposed (a roll would need pre-registration or fresh approval — **Non-Negotiable #6**). BRANCH 1 is the **execution of an existing approved exit**; BRANCH 2's HARVEST is a **profit/recovery-keyed** line, which is #7's live half. **Nothing here claims the energy thesis is broken — BRENT owns that and has not said so.**

⛔ **`[POSITION_STATE_INCOMPLETE]` stands.** The ×1 count is a **9/10 ~10:3x ET MIRROR** from `FORGE/STATUS.md`, not live holdings. **Confirm the live Fidelity position and any open order before acting** (Non-Negotiable #4) — do not sell a contract no longer held and do not duplicate a resting order.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## ✅ CLOSED — 2026-09-11. EXECUTION RECEIPT RECEIVED. REALIZED **−$77.33 / −33.97%**. **TRACKING FILE CLOSED.**

**Will-supplied Fidelity activity row, verbatim:** `Sep-11-2026 · Sell to Close · 1 Contract XLE Sep 30 2026 65 Call Limit at $1.51 (Day) · Filled at $1.51 · $150.34`

| | |
|---|---:|
| Gross (1 × $1.51 × 100) | **$151.00** |
| Fees / costs | **$0.66** |
| **NET PROCEEDS** | **$150.34** |
| Basis (avg cost $2.28) | **$227.67** |
| **REALIZED** | **−$77.33 · −33.97%** |

⇒ **`WQ-210` BRANCH 1 is DISCHARGED, and with it the 9/3 `WQ-168 ⑦` "SELL BOTH" ruling — the survivor is gone and the XLE line is FLAT.** **DOCKET `L253` closes on this receipt.** The FIRST contract's sale date/price remains **UNKNOWN** and is a FORGE **D-49** item, not a gap on this card.

### GRADE vs BRANCH 1 — execution CLEAN; the ruling's moment was missed, and missing it HELPED

**BRANCH 1 as ruled:** *sell the ×1 at the bid at the Fri 9/11 regular open.*

- ✅ **PRICE — hit the quoted bid EXACTLY, zero slippage.** The broker screen at **10:07 ET** showed **bid `1.51` × 53**; the fill is **`$1.51`**. A limit at the bid, Day, filled. **No chase, no spread paid, no mid-hunting.** ⛔ **This desk's own mid-limit suggestion ($1.73, 15-min leash) was NOT taken, and that was the better call** — the spread had already tightened to 4.53% and the optimization was worth ~$3.50 against the risk of not filling on a tape that then fell.
- ⚠️ **TIMING — the ruling's moment (the 09:30 open) was missed; the fill came later in the morning.** Per `RISK_RULES` **#14** the "at the open" clause is a **MOMENT property** and expired at 09:30; the SELL decision is the structure property and survived, so this desk treated the approval as live at a fresh mark rather than sending it back to Will. **That reading is recorded here as the one that was acted on.**
- 📐 **DID THE DELAY COST OR PAY? It paid — and the instrument is the broker's own day range, not a reconstruction.** Contract **day range `$1.37 – $1.75`**, previous close `$1.50` [Fidelity, 10:07 ET]. XLE opened **`$64.89`** and bottomed `64.84` in the 09:30–09:35 bars. **`$1.51` is mid-range and above the day's low.** ⛔ **NOT graded as a measured execution finding:** this desk does not hold the option's 09:30 bid, and comparing a fill to a reconstructed mark is exactly the 21-minute gap that manufactured a fake n=2 finding (`RISK_RULES` **#6**). **The honest statement is "the delay did not cost," not a number.**
- 📊 **POST-FILL, for the record and not as a grade:** at **12:20 ET** the contract is **bid `1.45` / ask `1.52`**, XLE `$65.14`. The fill is **above the current bid**. It traded as low as **bid `1.30` at 11:11 ET** (XLE `$64.80`) before recovering. **A round trip, not a trend — no skill is claimed and none is refuted.**

### STRUCTURE GRADE — the exit was right on the numbers that existed, not on the outcome

At the 10:16 decision the contract was **83% time value** ($0.32 intrinsic against a $1.51 bid), **19 DTE**, break-even **$67.28** requiring **+3.1%** from a tape that had gone `64.77 → 65.31 → 64.93 → 65.32`. **Theta, not direction, was the case, and theta does not round-trip.** ⇒ **Exiting was correct on structure regardless of where XLE closes today.** `GOOD_PROCESS` — the loss was taken by a pre-registered dated rule, on the operator's hand, at the quoted bid.

### 🔴 The finding this trade actually produced — and it is worth more than the $77

**The vendor chain read `bid 1.66` at 10:16 while the broker read `1.51` at 10:07: ~10% HIGH, on the side being SOLD, in the direction that FLATTERS the sale.** Had the ticket been priced off `chain_fetch.py`, a limit at 1.66 would likely **not have filled at all**, and the position would still be open into a contract that printed `1.30` an hour later. ⇒ **`RISK_RULES` 5b adopted the same session: vendor marks are SCREENING marks; the fill price comes from the BROKER.** **This card is the founding case.**

⛔ **NOTHING FURTHER IS TRACKED HERE. No new checkpoint, no review date, no successor card.** The XLE line is flat; a future XLE expression is a new card with its own approval.
