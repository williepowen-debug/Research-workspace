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

## RE-LOOK 2026-11-16 11:2x EST: NO CARD STANDS

**Asked by:** PROME prome-6f packet `inbox/processed/2026-11-16_from-PROME_United-Fidelity-funding-and-rule-reads-for-re-look.md` (1cc77b1423), on Will's 11:05 ET "Lets look into these". **Read in full:** DEWEY `output/2026-11-16_ufb-brokered-funding-call-report.md` (a0f5f80727) and REGINALD `reports/2026-11-16_UFB-and-FHLB-deeper-read.md` (dc53393902). Figures and rule readings are theirs; this answers only "is there a trade". Setup id `TRY-NOTRADE-UFB-RELOOK-NOV16`.

**Re-open standard (set 11/12, above):** (a) an OCC action naming a sale, merger or receivership and a listed acquirer; (b) a listed outside lender on a recorded lien; (c) a listed holder above about 5% of net assets. **None is met.**

| New fact (owner, label) | Does it meet (a), (b) or (c)? | Does it put a listed name on the losing side? |
|---|---|---|
| Undercapitalized by rule since 10/30, total capital 7.26% vs 8.0% (REGINALD, VERIFIED rule text; 10/30 conditional on no later OCC notice) | No: a category, not an action | No. It was the 11/12 premise |
| No brokered waiver possible now; about $1.0B brokered under the bar, up to about $1.75B with reciprocal above the cap (REGINALD; waiver history INFERRED) | No | No: depositors are insured; the bar binds the bank's funding, not a market |
| Brokered CDs due within a year at most about $363.0M vs cash plus unpledged securities about $239.1M at 9/30 (DEWEY; sweep split INFERRED); no FHLB since 12/2024; pledged securities +$293.7M in Q3, pledgee UNKNOWN | No | No. It raises the odds of the outcome (a) watches for, but that outcome is not here and its acquirer is unknown |
| Capital plan due Mon 12/14; a guarantee of up to about $295.8M by the controlling companies, likely ahead of the parent's notes (REGINALD; 11 USC 507(a)(9) recalled, not opened) | No | Hurts the parent's private notes; the listed holders still hold under 1% |
| FINS 0.66% and BANX 0.88% of net assets (same as 11/12); NexPoint Capital holds the bank's 7% preferred at a $0.5M mark (REGINALD; NexPoint's listing not checked) | No: all far under 5% | No. A $0.5M mark is immaterial to any fund |
| REGINALD read-across: none of its 14 banks under a capital-level order or near 8% total capital | — | No regional bank name; no new premise for KRE puts |

**Live check, 11:23 EST (vendor, intraday, not settles):** BANX $19.40 (+0.26%), FINS $11.66 (−0.26%), KRE $72.43 (−0.43%). BANX puts: Dec-18 17.5P 0.00/0.75, OI 2, NOBID · Jan-15 17.5P 0.00/2.00 NOBID, 20P 0.75/1.70 (77.6% spread), OI 16 · Apr-16 17.5P 0.00/2.10 NOBID, 20P DEAD (`chain_fetch.py --no-cache`). FINS: 0 listed expiries. Loss through options is still not definable, and the exposure behind it is still under 1%.

**Why it stands:** the reports make the bank's position worse and the dates sharper, but they do not move the exposure onto any listed instrument. A worse outcome for a private bank is still not a trade. The one path to a card is the same as on 11/12: a resolution that names a listed counterparty. Even then the sign for an acquirer is not obvious, because an FDIC-assisted deal usually helps the buyer. That would be read fresh, not assumed short.

**Dated tells (unchanged path, sharper dates):** OCC monthly enforcement release about Thu 11/19 (INFERRED) · capital plan Mon 12/14 (the OCC may set another date in writing, not public) · OCC plan decision about Fri 2/12/2027 if filed 12/14 · 12/31 Call Report notice event Mon 2/1/2027 · BANX mark about late November, FINS about late December. **A failed or missing plan is a ground for receivership, never automatic (REGINALD, statute recalled).** That is the event most likely to name a listed party.

**Logged, not scored:** added to `SIGNALS.tsv` `COMBO-BEAR-PREMISE-EROSION`, both directions (funding wall and closed waiver route against: no listed transmission, none of REGINALD's 14 banks in the same position).
