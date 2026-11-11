# Multifamily CMBS special servicing at a 2026 high, into a priced December hike: tradeability read (TERRY, 2026-11-11)

**Asked by:** PROME prome-2b by message 09:4x ET (fifth read, Will's 11/10 18:03 ET word). **Source:** HOMER packet `PROME/inbox/processed/2026-11-11_from-HOMER_catchup-live-data.md`; HOMER `thesis/THESIS.md` C2 row and `STATUS.md` HOM-05. **Desk:** TERRY, Claude Code, Claude Opus 5.5, desktop. **No order, no fill, no card term, gate or level changed.** Prices are vendor screens (09:48 ET), not broker.

## Answer: NO CARD

The cleanest carrier has already been repriced, the owners of the buildings are not where the stress lands, and the owner of the data moved no letter. Kept as `TRY-NOTRADE-MFCMBS-NOV11`.

## What HOMER measured

Trepp CMBS multifamily special servicing 9.22% in October, +69 bp, a new 2026 high and above HOMER's pre-set 9.08% line, driven by loans hitting maturity (the $517.7M Blackjack portfolio named). The special-servicing minus delinquency gap widened from 50 to 113 bp: more loans in workout than show as late. Delinquency 8.09% [Oct]. Rates into it: 10Y 4.98, 2Y 4.73, 30Y 5.35 [11/10 Treasury close]; MND 30-year 7.30% (+12 bp, 11/10); December hike priced about 85% 25 bp / 15% 50 bp (secondary, per HOMER). NY Fed Q3 mortgage 90+ 1.13% (0.83% a year ago), Nevada 1.98% (0.99%); loanDepot Q3 loss $28.7M.

## Why, in figures

| # | Reason | Figures (vendor, 09:48 ET, 30 bars each) |
|---|---|---|
| 1 | **The owner moved no letter, and its dated call leans the other way.** No HOMER criterion attaches to special servicing; the C2 kill count is 0/3; HOM-05 (Trepp November delinquency below 8.09%, 55%) is open to about 12/01–05, and HOMER records the tension without re-weighting. A card keyed to special servicing would be the desk writing a criterion the owner did not. | HOMER STATUS, THESIS |
| 2 | **The purest carrier is already repriced.** Arbor Realty (ABR), a multifamily bridge lender HOMER cites for realized marks: $1.44, −61.2% over 30 bars, at the bottom of its $1.44–$3.71 range. Its Jan-15 option chain lists one put strike ($1.50, OI 265). A put now buys the mark after it is realized. Cause of the 30-day fall not checked by the desk. | `snapshot.py`, `chain_fetch.py` (feed DEAD at this pull, structure only) |
| 3 | **Apartment owners are not the borrowers in default.** MAA $118.01 (+2.8%), CPT $99.01 (+2.5%) over 30 bars: low-leverage owners of their buildings, not floating-rate CMBS borrowers hitting maturity. A put there pays only if the stress spreads to rents, which HOMER's own data does not show (Zillow rent +2.9% YoY, October). Durable finding #7: match the vehicle to the open channel. | vendor |
| 4 | **The commercial-mortgage REITs are mixed, not trending.** BXMT $10.95 (−3.2%), KREF $5.45 (−12.1%), STWD $11.81 (−10.4%, at its 30-bar low), LADR $8.76 (+0.5%). No owner has mapped any of them to the Blackjack loan or the October special-servicing rise; picking one is a single-name credit call nobody has made (BROCK's lane). | vendor |
| 5 | **The rate leg is already in the book's answer.** Same as 11/10: the December hike is priced past 25 bp and no BOND or HENRY card-ready view exists on the front end. The credit-transmission view is carried by the HYG ×5 (fired, unfilled) and HYG ×4 (not fired) cards. | STATUS 11/10 |

## What would change the answer (each a fresh build on that day's prices)

1. **Trepp November print (about 12/01–05) misses HOM-05:** delinquency at or above 8.09% with special servicing still rising, graded by HOMER as a C2 confirmation, and **a carrier not already repriced**, named by a credit owner (BROCK for commercial-mortgage REITs, REGINALD for banks: HOMER's own table puts bank multifamily criticized loans at 35–39% in Phoenix, Houston and Dallas, Q2).
2. **A named loan-to-lender map** for the Blackjack portfolio or the October maturity defaults (which REIT or bank holds the B-piece or the bridge loan).
3. **HOMER's 11/20 formal grade** setting a criterion on special servicing or a new PMMS rung (A2 has none above Red).

## Addendum 10:0x ET — REGINALD names a carrier (Preferred Bank, PFBC): NO CARD STANDS

PROME prome-2b relayed REGINALD's catch-up (`PROME/inbox/processed/2026-11-11_from-REGINALD_catchup-live-data.md`): PFBC Q3 10-Q (FDIC, 11/09, primary): CRE loans 60–89 days late $150.2M vs $29.8M at 30–59 [9/30] (6/30: $80.5M vs $10.1M); real-estate special mention $148.4M from $19.6M at year-end; nonaccrual $103.2M held for investment + $56.6M held for sale; NPAs 2.27% of assets; REG-31 resolved TRUE.

| # | Why it does not change the answer | Figures (vendor, 10:0x ET) |
|---|---|---|
| 1 | **Only half the re-open condition arrived.** Condition 1 was an AND: the Trepp November print missing HOM-05 *and* a carrier not already repriced. PFBC supplies the carrier; the November print is still about 12/01–05. | this note § What would change |
| 2 | **PFBC has no usable option vehicle.** 3 expiries (Dec-18, Mar-19, Jun-17); the Mar-19 put chain returned no strikes within ±20% of spot. REGINALD's 11/05 record already rates its options not tradeable for Will. Shares-short is outside this book. | `chain_fetch.py PFBC` |
| 3 | **The name is not repriced, but the cohort is rising, not following.** PFBC $103.40, −1.7% over 30 bars (−6.1% vs KRE), mid-range two days after the filing; CATY +9.0%, HAFC +5.6%, KRE $73.06 +4.4% near its 30-bar high. A cohort put (KRE) would be a call that one bank's aging spreads, against a tape that says it has not. | `snapshot.py` |
| 4 | **The cohort expression is already in Will's book, by hand.** Bank/credit put cluster 41 contracts across 14 lines, basis $6,644.24, value $1,110.00 [FORGE mirror, 11/10 intraday], including KRE Nov-27 68P ×10 and KRE Dec-31 65P ×2. Another cohort put stacks on the same falsifier (the 9/11 shared-falsifier grouping: nothing caps the cluster). | `FORGE/STATUS.md` D-74 |

**Would change:** the Trepp November miss lands *and* PFBC (or a named peer) shows the aging in its price, with a listed option chain that quotes; or REGINALD maps the PFBC late loans to a cohort mechanism (a shared maturity wall) that a broker-quoted KRE structure, sized against the existing cluster, expresses better than the lines Will already holds.

## Small item logged (WQ-622)

`SIGNALS.tsv` `COMBO-CREDIT-FOLLOWING` gains the special-servicing print and the ABR / mortgage-REIT tape, counterevidence included. Logging is not scoring.
