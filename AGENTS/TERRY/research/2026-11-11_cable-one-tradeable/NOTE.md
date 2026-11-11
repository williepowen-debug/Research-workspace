# Cable One (CABO) restructuring-officer board seat: tradeability read (TERRY, 2026-11-11)

**Asked by:** PROME prome-2b by message 10:2x ET (Will's 11/10 18:03 ET word). **Source:** BROCK packet `PROME/inbox/processed/2026-11-11_from-BROCK_catchup-hiking-fed-read.md` (KB-BRK-480; D:L1058; BRK-37 25%, BRK-38 55%). **Desk:** TERRY, Claude Code, Claude Opus 5.5, desktop. **No order, no fill, no card term, gate or level changed.** Prices are vendor screens, not broker.

## Answer: NO CARD

The equity has already fallen 63.5% in 30 sessions. There are no listed options, so the only bearish expression left is a short sale with an open-ended loss, and the owner's own read is that it is not a card candidate. Kept as `TRY-NOTRADE-CABO-NOV11`.

## The fact (BROCK, primary)

8-K acc 0000950157-26-001140 (Item 5.02, accepted 10/30 16:35 ET): Paul Keglevic, former CEO and chief restructuring officer of Energy Future Holdings, was elected to the board and named to "a special committee of the Board established to evaluate strategic alternatives". BROCK's read: evidence toward BRK-37 and BRK-38, resolves neither. Context from BROCK's STATUS: equity −$86.3M, NYSE 802.01B non-compliance stated; a delisting puts $345.0M of convertibles to the company at par, then cross-default, on the issuer's words. The hearing on the motion to dissolve the 10/9 order is Fri 11/13.

## Why, in figures

| # | Reason | Figures (vendor, 10:23 ET) |
|---|---|---|
| 1 | **The stress is in the price.** CABO $3.78 +0.83%, −63.5% over 30 bars, at the bottom of its $3.75–$15.38 range. Closes since the 8-K: $5.46 (10/30) → $3.75 (11/10), −31%. A restructuring adviser on the board is the market's base case, not news to it. | `snapshot.py`; 66 daily bars |
| 2 | **No defined-loss vehicle.** `chain_fetch.py CABO`: 0 listed option expiries. The only bearish expression is a short sale: borrow availability and cost unknown, loss not capped, and a strategic-alternatives committee can produce a takeout bid that gaps the stock up. Hard boundary: if the loss cannot be defined, there is no trade. | `chain_fetch.py` |
| 3 | **The owner says no card, and the event is binary.** BROCK: not a card candidate. The 11/13 hearing and the delisting/put/cross-default chain resolve on court and exchange dates the desk cannot price. On the long side, a recovery bet on a company with negative equity ahead of a possible Chapter 11 is a lottery, not a card. | BROCK packet and STATUS |
| 4 | **Not near the exchange line.** 30-close average $7.55 against the $2.64 NYSE prompt-delisting line (BROCK, 11/11). The mechanical trigger in the issuer's chain is not close on the average. | BROCK |

**Would change:** listed CABO options returning with a quotable chain; or a strategic-alternatives outcome (a sale or a restructuring support agreement) with terms that put a number on the equity, graded by BROCK.

## Small item logged (WQ-622)

`SIGNALS.tsv` `COMBO-CREDIT-FOLLOWING` gains the CABO restructuring-officer appointment, counterevidence included. Logging is not scoring.
