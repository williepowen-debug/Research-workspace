# CARL answer: do DEWEY's two card reports change the consumer thesis or its test?

**Assigned:** Will, 2026-11-04 21:12 ET, through PROME. **Written:** 2026-11-05 08:30 ET.
**Read in full:** `AGENTS/DEWEY/output/2026-11-04_carl-dr1-cof-q3-fdm-three-issuer-final.md`, `AGENTS/DEWEY/output/2026-11-04_card-modified-cohort-peer-check.md`, both DEWEY packets, WALTER's SIG-W-20261104-080 (at `BOARD/`; no copy reached `inbox/WALTER/`). Figures rechecked at DEWEY's two evidence JSON files and its saved text of the Capital One 10-Q. No new data pulled.

## The short answer

1. **Thesis: NOT YET, on one line only.** The line is the masking framework's Capital One row in `thesis/THESIS.md`, together with item 2 of DR-1's tell-list ("re-default on modified pools"). Capital One's borrowers on hardship plans got visibly worse in one quarter, and that is where the framework says to look. But it is one quarter at one lender, the cause is unknown, and the whole card book is better than a year ago. Everything else stands: score 53/70, version 2.6.6, every vector. The October 12 finding also stands: concentrated strain is supported, a broad collapse is not established.
2. **Test: NO.** The class-wide 50 basis point (0.50 percentage point) test stays NOT COMPUTABLE, neither passed nor failed. No registered prediction, gate or score moves. These reports complete the collection for three lenders. They do not supply what the test lacks.

**Working model, not truth:** at least part of the Capital One move is real plan failure, because the default count excludes loans that were already in default when they entered a plan (see trap 1). I cannot size that part. I also cannot tell whether borrowers got worse or whether Capital One changed who enters its plans or how it handles them.

## Question 1: which thesis line, and why "not yet"

| Pull toward "yes" | Pull toward "no" |
|---|---|
| Domestic modified group delinquent $645M to $993M (+54.0%) against book +11.1% | Whole-book 30+ day rate 3.74%, 15 bp below 3.89% a year ago |
| Delinquent share 17.2% to 25.2% | Domestic card charge-offs 3.98%, Q2 4.71%, −65 bp on the year (`STATUS.md`, KB-537) |
| Subsequent defaults $152M to $230M (+51.3%) | Domestic Card allowance net release "due to favorable credit performance" (10-Q) |
| The group is 35.8% of the quarter's rise in domestic late dollars ($348M of $971M), 6.9% a year earlier | The group's late balances are 38 bp of domestic card loans; the rise is 13 bp |
| Rate cut on plans slightly deeper: 15.95 points, Q2 15.42 | One quarter, one lender, cause unknown |

⚠️ The allowance release is management's estimate, and "release into a worsening mix" is one of the patterns this framework names at Ally. It counts against stress but does not close the question.

**Masking is not established.** The framework's definition needs an accounting or composition choice that defers recognition. These delinquencies are being reported, and nothing shows a deferral. The shape resembles the framework (clean headline, worse cohort), but resemblance is not confirmation. Reading it as "the cushion is running out" would need more than a $3.9B group inside a $260B book.

**The modified group is not a bottom-60 sample.** Lenders choose who gets in. It tells us about those plans, not about the fragile share of households.

## Question 2: what is and is not computable

**DR-1 state: PARTIAL.** The 50 bp kill is neither discharged nor breached. Under Will's WQ-104 ruling every DR-1 statement carries both figures: **97.4 bp weighted / 22.5 bp best leg**. Both are older mortgage proxy illustrations, not measured class-wide effects, so neither is a pass or a fail.

| Computable, each lender alone | Not computable |
|---|---|
| Scale of the current modified group against the card book: Capital One 113.31 bp (June 119.27), Synchrony 99.24, Bread 139.20. Scale only | How much reported delinquency improved because of plans, for any lender or the class. No untreated comparison group and no loan-level payment history |
| Delinquent share, modification flow and default dollars, each on the lender's own definition | Any class-wide figure. Card dollars cannot be added to count-weighted mortgage proxies, and these lenders' tables do not share a basis |
| Capital One 30+ rate without the group: 3.18% to 3.41%, an assumption-based derivation with the bias noted below | A true default rate at JPMorgan or Capital One (see trap 2) |
| | Why Capital One moved, or how much is legacy Discover. Citi, which is unread |

⚠️ The 113.31 bp fall is not an improvement. Current balances fell because loans moved into delinquency while the group grew from $3,896M to $4,104M.

⚠️ The "without the group" rate is not a clean control. An account that is late when it enters a plan leaves the rest of the book and arrives in the group. So "about 23 bp, against 28 bp a year ago" can be flattered by that transfer. The transfer-free figures are the whole book: up about 35 bp in the quarter, against about 30 bp a year ago, and 15 bp lower on the year. (That 3.41% is also coincidentally the filing's company-wide rate. They are different numbers.)

| Registered item | Effect | Why |
|---|---|---|
| CARL-DR-1 50 bp class-wide test | None | NOT COMPUTABLE |
| CRL-20 (1%), masking outer window | None | Its Capital One leg needs card charge-offs up at least 25 bp for two straight quarters. Q3 fell 73 bp. The cohort is not a leg |
| CRL-31 (1%), equity leads credit | None | Same charge-off leg |
| CRL-21 (STUCK) | None | Ally only |
| CRL-30 (25%), national card flow into 90+ days | None | A New York Fed series; a lender cohort is not an input |
| CRL-24 Axis A confirm cell | None, closed | Resolved MISSED. Book delinquency rose 35 bp against its 25 bp leg, but charge-offs of 3.98% are far under its 5.5% leg, so this is not half a firing |
| Full-thesis kill, V1, V8, score 53/70 | None | No input here |

**Recommendation to PROME: no threshold, level, gate, score or weight should change.** No trade idea arises from this reading.

## Trap 1: "Capital One-specific" is not "benign"

These are separate claims. "Not shared" says where the move sits. "Harmless" says what it means. The peer check supports the first in part and says nothing about the second.

**What "not shared" establishes.** Delinquent share at the other five lenders read stayed within about one point: Synchrony 22.9% to 23.7%, Bread 18.8% flat, JPMorgan 11.3% to 11.6%, Bank of America 14.4% to 14.2%, American Express 8.4% flat. Three limits apply:
- Citi is unread, so this is five of five read, not all large lenders.
- It holds for delinquent share. On default dollars against group size, three lenders rose on the year (table in trap 2). This is crude and each lender is compared only with itself, but it is a reason not to say "only Capital One".
- Lenders choose who enters a modified group, so a flat share elsewhere does not show those borrowers are fine.

**What a real deterioration at one lender would mean.** It would still be real: actual households failing plans and an actual lender loss. There are two readings, and they matter differently:
- **The lender's own problem.** Underwriting, a vintage, collections or integration. That is mainly a bank question (REGINALD), not a statement about households.
- **The first place it shows.** Capital One's book runs late (3.74%, against JPMorgan 1.97%, Bank of America 2.32%, American Express 1.20%, on differing bases), so the weakest borrowers could fail here first. This is the reading that would matter for the thesis. The evidence against it is that Synchrony (book 30+ 4.34%) and Bread also lend to weaker borrowers and show no jump. "First" cannot be told from "only" on one quarter.

**Size.** If the whole $348M rise were charged off with no recovery, that is about 13% of one quarter's domestic charge-offs (about $2.6B, derived from 3.98% on the average book). That would be material to this cohort and visible in the numbers, but it is no threat to the lender.

| Explanation | What the filing shows | Can the filing separate it? |
|---|---|---|
| Borrowers failing plans after entering | Defaults +$78M in the quarter. The 10-Q says loans that entered "while in default are not considered to have subsequently defaulted" | **Partly.** Some of the rise is movement into default after entry. It cannot size this, and a loan entering 30–89 days late still counts |
| More borrowers entering already late | Modification flow +$357M, close to the +$348M delinquent rise. That closeness is arithmetic, not evidence. Delinquency at entry is not shown | **Partly.** The default exclusion rules this out as the sole cause of the $230M, not of the 30–89 day rise |
| Discover integration or conversion | No conversion statement. "Modification programs and balances include those in place at Discover." No legacy split. Integration expense flat at $338M | **No.** See the timing note below |
| Portfolio mix | Legacy Capital One card growing, Discover shrinking. No credit-score or legacy split of the group | **No.** Mix usually drifts, and this was a step, which argues against it but does not exclude it (inferred) |
| Programme, definition or reporting change | None stated; DEWEY's full-text search and my own searches of the saved text found none | **No.** A filing's silence is not proof. An internal change would look the same |
| Seasonality | A year earlier the group and book moved together (+8.8%, +8.9%) | **Mostly against**, but only one comparison, and that row holds pre-closing Discover loans |

**Discover timing, from my own record.** My April note (KB-245, from call transcripts, not a primary document) had Discover *new originations* reaching about 100% on Capital One's platform by end Q3 2026, with *existing accounts* converting in Q4 2026 to Q1 2027. If that held, the existing-account conversion came after this jump and did not cause it, and any conversion distortion may still lie ahead in the next two tables. Other integration work (collections, hardship programmes) could still have happened in Q3. Whether the April timeline held is UNKNOWN. My thesis row had merged the two dates and is corrected.

**Shape of the jump.** Every lateness bucket moved at once. The 90+ day bucket rose $130M, its largest quarterly rise in the table by far (next largest +$22M), yet the June feeder buckets were normal ($357M, range $341M–$388M). So this was not a simple walk through the buckets. The 10-Q says a borrower who breaks a plan may revert to original terms and be "reflected in the appropriate delinquency category", which can move balances in bulk. That shape fits plan reversion, a batch event, or already-late entrants, and it does not choose between them.

**Thin baseline.** "25.2% against 15.7–18.0% at five prior period-ends" sounds like a long history. Four of the five rows may hold pre-closing Discover loans, so only June 2026 is clean.

## Trap 2: JPMorgan's rising default dollars

**Verdict: a true default RATE is NOT COMPUTABLE from what DEWEY has. Neither "higher" nor "flat" can be claimed.**

| JPMorgan, retained card | Q3 2025 | Q3 2026 | Change |
|---|---:|---:|---:|
| Defaults in the quarter | $56M | $127M | +126.8% |
| Modified group, start of quarter | $1,297M | $2,651M | +104.4% |
| Modified group, end of quarter | $1,642M | $2,859M | +74.1% |
| Crude ratio on start of quarter (not a rate) | 4.32% | 4.79% | +0.47 pt |
| Crude ratio on end of quarter (not a rate) | 3.41% | 4.44% | +1.03 pt |
| Delinquent share of group | 12.4% | 11.6% | −0.8 pt |
| 90+ day share of group | 4.3% | 4.1% | −0.2 pt |

- **Most of the rise is size.** A group that simply grew at the same crude ratio would explain 58% to 82% of the extra $71M, depending on which base is used.
- ⚠️ **The rest should not be hidden.** Dollars grew faster than either base, so the crude ratio rose on both. Rising dollars alone say nothing, and the base does not make the whole rise disappear.
- **Why the ratio is not a rate.** A rate needs the balances at risk, tracked by when they were modified and including those that later left. The table gives a quarter-end stock after exits, with no age breakdown. DEWEY declined a Fannie re-default rate on 2026-08-13 for this same reason.
- **Age alone can raise the ratio.** The group grew 26.6% in Q3 2025 and 7.9% in Q3 2026. A fast-growing group is young, and young loans have had less time to miss payments. As growth slows, the crude ratio can rise with no change in borrower behaviour. This is inferred, not measured.
- **Other evidence points against worsening.** Delinquent share is flat to lower, and the 90+ bucket was flat in the quarter ($118M to $117M). The reason for the group's growth is UNKNOWN: outreach or need. The Apple Card purchase is not on the book.
- **Definitions differ.** JPMorgan counts two consecutive missed contractual payments, which trips earlier than Capital One's 90+ days, charge-off or nonaccrual. American Express allows up to three missed payments by programme. Each lender can only be read against itself.

| Same crude ratio, end of quarter, each lender against itself only | Q3 2025 | Q3 2026 |
|---|---:|---:|
| Capital One domestic ⚠️ 2025 row holds pre-closing Discover loans | 4.09% | 5.83% |
| JPMorgan | 3.41% | 4.44% |
| American Express | 2.35% | 2.65% |

Bank of America gives no amount. Synchrony's defaults fell $88M to $84M on the quarter, with no prior-year row pulled. Bread's are not comparable to prior periods.

## What settles it, with no new work

The 180-day charge-off rule does this on its own. The $418M at 90+ days on September 30 must cure, be re-aged or be charged off by about year-end, and the ordinary January issuer read and the next Capital One table will show which. This is a description of existing reading. No test, watch or job is registered.

## Figures checked and notes on the record

Reproduced from DEWEY's evidence files: all scale ratios; the $645M to $993M move and its buckets; +11.1% book; 35.8% and 6.9% shares; flows and defaults; both 30+ rate series, with and without the group; the JPMorgan, Bank of America and American Express shares. No discrepancy.

Three small notes:
1. DEWEY's default definition omits the 10-Q's exclusion of loans already in default at entry. That sentence is what makes the "partly" above possible. It refines DEWEY's list of explanations and does not correct a figure.
2. DEWEY's evidence file says "two consecutive missed contractual payments"; its report says "two missed".
3. One correction of my own: `thesis/THESIS.md` said "Discover back-book conversion ... ~100% on COF platform Q3 2026". KB-245 says originations by end Q3 and back-book Q4 2026 to Q1 2027. The cell now matches KB-245. No version, score or rule moved.

**Citi** is DEWEY's unfinished work under Will's four-lender approval and PROME's registered row. I did not chase it.

**Left out of this assignment:** all `inbox/` items not named here, none of which bears on either question.
- Board-ledger gap packets, four rather than three: 10/31, 11/02, 11/03, 11/04.
- `2026-10-30_from-DAEDALUS_falsification-5.md`; three ISHM packets (Caterpillar, October manufacturing, equipment and rail).
- Eleven `inbox/WALTER/` signals, plus ten owed BOARD signals still unrecorded once SIG-W-20261104-080 is logged here (the two lists largely overlap). Two adjacent auto-lender signals (CPS, Credit Acceptance) are auto, not card.
- Correction COR-20261031-22, unreceipted.
