# United Fidelity Bank: tradeability read, NO CARD

**Date:** 2026-11-12, written 08:5x to 09:0x EST (clock from `date`). **Desk:** TERRY, Claude Code, Claude Opus 5.5. **Asked by:** PROME packets ×3 of 11/11 evening (DOCKET L1126, Will 11/11 18:51 ET) and DEWEY's 11/11 losses-and-capital packet. **Setup id:** `TRY-NOTRADE-UFB-NOV12`.
**Inputs, read in full:** `PROME/reports/2026-11-11_united-fidelity-follow-up/SYNTHESIS.md` (incl. Addendum 1 and 2), `D-parent-paper-holders.md` lines 1–62, `AGENTS/DEWEY/output/2026-11-11_united-fidelity-losses-and-capital.md`, DEWEY 003R refresh packet. Thesis and figures are the owners'; this note answers only "is there a trade".

## Answer: NO CARD

No listed instrument carries this exposure in a size worth a card, and the only listed holder with options has no quotable put.

| # | Candidate | Exposure | Tradeable? | Verdict |
|---|---|---|---|---|
| 1 | United Fidelity Bank, Fidelity Federal Bancorp, Pedcor | the whole loss | private, no listed equity or bonds; parent sub-notes unrated and held by funds | no instrument |
| 2 | ArrowMark Financial (BANX), closed-end fund | former TARP preferred, 0.88% of net assets, already marked at 60% since at least 6/2024 (report D) | $19.54 [11/11 close, vendor, stale pre-open]. Options exist but the Dec-18 put chain has ONE strike, 17.5P, bid 0.00 / ask 0.00, OI 2, last trade 10/26 (`chain_fetch.py` 08:54 ET, flag DEAD) | a full write-off moves net assets at most about 0.9%, less than an ordinary day; loss not definable through options; NO |
| 3 | Angel Oak Financial Strategies Income Term Trust (FINS), closed-end fund | $3.0M of the parent's notes, 0.66% of net assets, marked 95–99.5% of par through 8/31 | $11.85 [11/11 close, vendor]; **0 listed option expiries** | short-only, loss undefined, exposure under 1%; NO |
| 4 | Ginnie Mae securities the loans were converted into | government-guaranteed; holders bear no credit loss from this bank | n/a | no credit channel |
| 5 | Brokered and retail depositors | FDIC-insured up to limits; brokered roll-over limit is a funding channel for the BANK, not a market | n/a | no instrument |
| 6 | Other regional banks / KRE | transmission NOT shown (PROME: no outside lender on any filing read; DEWEY 003R: larger band does not follow the six-bank sample, concentration caveat required) | KRE puts exist, but this event gives them no new premise | no card from this event; Will's bank/credit put cluster is already 14 lines (11/11 note) |

**Why the answer is not close.** The bank is the lender, developer, owner and fee-earner inside one family group, with a second sponsor (Birge & Held) that shares its address history. Most layers found so far sit inside that circle, but containment is NOT established: 53.6% of origination dollars are unmatched and outside funds hold the parent's notes and preferred (PROME synthesis, "Correction 2026-11-12, second"; reworded here 2026-11-12 evening on that correction and Will's word). No card is a finding about listed instruments, not a finding that the risk is contained. A trade needs a listed party that loses when this goes worse; the two found hold under 1% each, and one is already marked down 40%.

## What would change it (dated where a date exists)

- **An OCC action naming a sale, merger or receivership** (November enforcement release, about the third week of November; capital-plan date about 12/14 is INFERRED from rule text). A named **listed acquirer** or an FDIC loss-share with a listed bank is the first thing that could put a listed name on the other side. Re-read then.
- **A listed outside lender, participant or senior lien holder** found on a recorded mortgage (needs a person's browser; report E). Only a holding above about 5% of that lender's equity, or a named loss, would be card-sized.
- **A listed holder with a material position** (above about 5% of net assets) found in a later fund filing. The BANX (about late November) and FINS (about late December) marks are dated tells for the record; at under 1% each they do not change the answer on their own.
- **Florida:** $598M of originations; whether any Florida loan is impaired is UNKNOWN. A Florida-listed exposure would be a fresh read.

## Logged, not scored

Added to `SIGNALS.tsv` `COMBO-BEAR-PREMISE-EROSION` as a member with both directions: a real multifamily credit loss ($362.5M charge-offs, total capital 7.26% [9/30 Call Report, DEWEY]), and counterevidence that the loss may sit mostly in-house (concentration, no outside lender shown [PROME synthesis, INFERRED]); containment itself is not established (53.6% of origination dollars unmatched; wording narrowed 2026-11-12 evening on PROME's second correction). Logging is not scoring. No card, gate, level or threshold changed.
