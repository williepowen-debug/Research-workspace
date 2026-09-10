# TLT September 30 $85P — existing approved exit tracking
**Setup ID:** `TRY-EXIT-TLT85P`
**Updated:** 2026-09-09 21:1x ET (owner expiry-pass write-back; prior 2026-09-08T17:27:10-04:00)
**Terry verdict:** STAGED
**Tracking state:** STAGED — approved $2.60-limit exit; broker reconciliation pending.

Owner continuation of WQ-168 §⑤, approved by Will September 3 at 12:45 ET. Full original card: `PROME/inbox/processed/2026-09-03_from-TERRY_expiry-pass-Sep18-Sep30-seven-lines-007-grade-UNKNOWN-mirrors.md`. This is management-only under RISK_RULES #20; entry rationale is UNRECOVERABLE. No new proposal, price change or approval request.

The approved **$2.60 sell-to-close limit uses the broker's actual current contract count**. Will resolves Fidelity Activity & Orders before placing or replacing any order. The September 3 15:07 capture showed **one contract then** (2→1 relative to the prior mirror); it establishes neither current holdings nor a fill price/time nor an open order. Will's 20:38 denial was withdrawn at 20:47; “maybe I did” reasons from the same capture and is not independent corroboration.

**WQ-169 D-43 remains UNCERTAIN; D-45 Activity & Orders is the resolver.** No current fill, live quantity or working order confirmed; `[POSITION_STATE_INCOMPLETE]`. STAGED changes only on Will/broker execution truth, never from option last-trade or a position count. The old September 4 placement target is elapsed, not an active pending date. September 30 expiry remains the disposition backstop; record actual fill or non-fill/expiry outcome, not presumed worthless expiry. Current bid/ask and forward mark **UNKNOWN** (local Yahoo DNS failure; `../outbox/2026-09-08_owner-market-evidence.json`). Original two-lot $520 proceeds arithmetic is September 3 hypothetical history, not a current amount.

## 2026-09-09 21:1x ET — count and fill still UNKNOWN; and the approved limit is now BELOW the bid

**Standing record: contract count and fill are Will's receipts and remain UNKNOWN.** No re-ask (WQ-169 D-43/D-45 is the resolver). STAGED unchanged.

**New observation with a decision consequence, and it is the reason this line is not merely restated.** At the 9/9 close the TLT Sep-30 **$85P marks bid `3.25` / ask `3.40` / mark `3.33`** (spread 4.51%, IV 13.04%, OI 1,431, last trade 15:55 ET, no quote flag; `chain_fetch.py TLT 2026-09-30 --type put --no-cache --legs 77,85`, 21:09 ET; TLT spot **$81.73**). Intrinsic = **$3.27**; the bid is **$0.02 under intrinsic**, i.e. extrinsic is gone.

⇒ **The approved $2.60 sell-to-close limit is $0.65 BELOW the current bid.** Two mutually exclusive readings, and the repo cannot tell them apart:
- **(a) the order is resting** ⇒ it would have filled at or above $2.60 on any session since the mark cleared that level — so a resting order implies a FILL, and the position is gone. *(This is an inference from the tape, not a fill receipt. It does not book anything.)*
- **(b) no order was ever placed** ⇒ the contract is still held and **$2.60 is a stale limit that forgoes ≈$65 per contract** against the current bid.

⛔ **Neither branch is asserted and no order is placed, replaced or cancelled by TERRY.** The resolver is unchanged: Fidelity **Activity & Orders** (D-45). **A re-priced limit is a NEW threshold and therefore Will's [Approve] — carried as a one-line ask in the delivery memo, not adopted here.** 21 DTE; the 9/30 expiry remains the backstop. `[POSITION_STATE_INCOMPLETE]`.

## QQQ Sep-10 $715P ×1 — same standing

**Disposition UNKNOWN — Will's receipt.** Off-thesis / day-trade class, on no TERRY card and owned by no agent (FORGE mirror, "Fidelity — Off-thesis / day-trade class"); recorded here only so the expiry is not invisible. **Expires TOMORROW, 2026-09-10.** Screenshot mark $2.40 vs $2.55 basis [9/9 screenshot, PROME `research/2026-09-09-position-review/snapshot.csv`] — screenshot provenance, no capture stamp, **not an executable quote**. No current bid/ask, order state or fill is established. ⛔ **No disposition proposed by TERRY and no ask raised** — this is a Will/PROME line, and its outcome is recorded when a receipt lands, never inferred from a close.

No brokerage access, order, capital movement, add, roll or size change by TERRY.
