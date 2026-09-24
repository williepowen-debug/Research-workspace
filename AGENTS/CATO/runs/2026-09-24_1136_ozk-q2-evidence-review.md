# OZK Q2 filing-read review — September 24, 2026

**Disposition: useful evidence work accepted in the checked areas; correct the guidance claim, finish Boston propagation and fix the charter's scope labels.** The operator-summary claim of a first C&I stress signal is also wrong. Keep Horton and the already-owed reserve re-derivation moving; these findings do not require another broad restructuring pass or a fresh trading/model decision.

## Scope and sources

Will supplied OZK's completion brief citing `6cbb6933f`. Implementation `5ab96492e`; two delivery packets `6cbb6933f`. At inspection HEAD was `2018762a4d5859995f5c0e277052e857bb711915`, which had already updated the charter with an owner-recorded Will approval. Initially one commit ahead, later observed synchronized with origin without CATO pushing it. No owner working changes observed. Inspected the new read report, relevant consumers/diffs, recipient packets and later charter change. Prediction ledger has no diff from `daff3885c` to `2018762a4`.

Primary sources opened independently:

- [Q2 2026 10-Q](https://ir.ozk.com/static-files/be1e7bcd-b8bc-4b66-aef6-ece49f463f22), 69 pages, also local `AGENTS/OZK/raw/Q2_2026_10Q.pdf`. Selected pages 13–14, 17, 20–21 and 57/59–60 extracted; page 20 visually inspected. The first guessed issuer URL and direct FDIC attachment open failed; the actual issuer static-file URL worked.
- [Q2 Management Comments](https://ir.ozk.com/2Q26_Management_Comments), especially printed pp.19–24, for guidance and named property transitions.
- [Q1 Management Comments](https://ir.ozk.com/1Q26_Management_Comments), printed p.23 / physical PDF page 24, for the maturity pairing. CATO rendered and visually inspected that local page; layout directly associates each note with its loan.

CATO did **not** independently read all 69 pages, inspect the owner's reading transcript, re-pull all Call Reports, identify every property against land records, or independently re-check the July call audio. Owner's claim to have read every page remains owner-reported. This is a targeted claim review, not full-filing certification.

## What the evidence supports

The Boston life-science maturity is **February 13, 2026**; December 18, 2025 belongs to Baltimore land. The Q1 table supports the exact Boston day; Q2 repeats the month. A January 29 filing therefore precedes that maturity. The correction withdraws a consequential false premise, not merely a typo. Actual borrower/sponsor identification against registry records was not re-investigated.

Q2's named transitions include Sullivan's return to pass status and deterioration/foreclosure of other credits. The resulting evidence is two-sided. The new read also correctly keeps warning §1 fired/undetermined: identifying migrations between risk categories does not identify the departing 30–89-day delinquent loans. Earlier OZ2 acceptance stands.

Capital arithmetic broadly checks on a static, principal-only basis: `RWA = 4,491,623 / 10% = 44,916,230` ($K); `(6,661,654 − 70,000) / RWA = 14.6754%`, and subtracting 350,000 instead gives 14.0521%. Round to **14.68% / 14.05%**. Both exceed the filing's total-capital minimum including buffer (10.5%), as well as its 10% well-capitalized threshold. This supports headroom in that scenario; it is not an October forecast or proof that redemption's liquidity/capital opportunity cost is immaterial.

RaDD's pass-status inference is plausible **conditional on** the carried $555M balance applying to the same date and being one unsplit exposure. Retain its INFERRED-HIGH label: the filing does not name RaDD. The Jack/San Carlos attribution also remains inference. The owner appropriately identifies the sum-match limitation in the BROCK packet. No inferred attribution is independent permission to grade BROCK's trigger.

## QF1 — Medium: the claimed written-versus-spoken guidance conflict is contradicted by the written document

**Location:** `AGENTS/OZK/research/threads/Q2_2026_10Q_READ.md`, F11, and Will's pasted brief. F11 describes the written material as an elevated-loss outlook and the call as a below-industry outlook, then labels the difference a signal.

**Primary check:** Q2 Management Comments **p.19** already states management's full-year goal is to outperform industry losses, while **p.20** discusses continued elevated losses. The written document contains both ideas. Elevated versus the bank's own history and favorable relative to peers can coexist. This is not evidence that management kept the favorable outlook out of writing.

**Consequence:** a supposed disclosure inconsistency becomes a bearish signal without a demonstrated inconsistency.

**Correction / close when:** withdraw F11's asserted conflict and the operator-summary signal, or identify an actual like-for-like contradiction with the same period, metric, benchmark and degree of commitment. Preserve both statements and track whether the full-year goal is met. No broad transcript investigation is required to remove the unsupported comparison.

## QF2 — Low: the “first sign outside real estate” is not a first

**Location:** Will-facing brief; F10 supplies the current observation but does not itself make the same first-ever assertion.

**Primary check:** 10-Q **p.20** shows one C&I hardship modification for **$40.361M in Q2 2026**, and also one for **$28.474M in Q2 2025**. Page 14 additionally contains earlier C&I substandard balances. The new loan is a current stress observation, not the first such evidence.

**Correction / close when:** call it the latest observed C&I hardship modification, retaining the prior comparator and avoiding an unestablished borrower identity. CATO supplies that correction to Will here; no new report-writing cycle is required solely for this wording. F10's “2026 vintage revolving” also should not be inferred from a table column that merely says revolving loans.

## QF3 — Medium: Boston's correction has not reached every active copy

**Verified surviving sources at the pin:**

- `workbook/KB.tsv`, **KB-OZK-195** remains ACTIVE and still explains the January lien as six weeks after a December maturity, with the old five-year date fit. New correction row KB-OZK-235 references it but does not supersede or qualify its surviving body.
- `SEVEN_CREDIT_DEEP_DIVE.md:89` still calls the January UCC-1 post-maturity. Its later paragraph correctly retracts that chronology, leaving the local verdict inconsistent with the correction.
- `research/threads/IQHQ_SECONDARY_EXPOSURE.md:22` retains the post-maturity description and a concluding December-date fit alongside its new correction.

**Consequence:** a future retrieval can recover the old workout interpretation as current, despite the completion claim that all copies were corrected.

**Correction / close when:** qualify/supersede KB-195's invalid reasoning and remove or explicitly historical-label the two active narrative survivors. Preserve genuine registry evidence and do not substitute an unsupported story about why the pre-maturity lien was filed. Keep the corrected date and withdraw only reasoning dependent on the old one. PROME's correction memo exists, but consumption was not independently verified.

## QF4 — Medium: the approved charter refresh mixes population scopes

**Location:** later commit `2018762a4`, `AGENTS/OZK/CLAUDE.md:18`. The new line calls the figures a RESG problem book, then combines named RESG nonaccrual with **bank-wide** substandard-accrual, foreclosed-asset and special-mention figures.

**Primary check:** 10-Q p.14 identifies the bank-wide substandard-accrual total as $72.839M, including $40.413M of C&I; it is not a RESG-only subtotal. The five RESG special-mention loans are a subset of the bank-wide special-mention total. Thus the line's amounts cannot be added or described as one uniform RESG roster.

**Correction / close when:** label bank-wide totals and RESG subsets separately, or make this slow-changing charter line point to the dated roster in STATUS/read report without duplicating mixed-scope amounts. Do not change source values, classifications or thresholds to reconcile a wording error.

The approval question in the pasted message is overtaken by the subsequent commit, whose body and file annotation record Will's approval. CATO did not witness the external approval exchange, does not dispute it, and does not request it again. This finding concerns the implemented content, not permission to refresh it.

## Bounded residue, checks and recommendation

The SEVEN_CREDIT Q2 banner calls San Carlos debt-on-debt without its report's inference qualifier; retain that qualifier at next touch. The fresh primary read did not settle the Q1 Memo-1 coding discrepancy, so the proposed explanation for that discrepancy stays an inference. No expanded charge-off attribution investigation is commissioned here.

Checks: directly inspected primary table layouts; recomputed the two capital scenarios and the $63K sum-match gap; verified unchanged prediction ledger; read the Boston correction packet and BROCK attribution packet; checked active Boston survivors and the actual later charter diff. No production code changed or operational scripts run. CATO authored only this report and CONTINUITY. Existing OZK correction acceptance and PROME docket handoff remain separate and unchanged.

**Suggested next step for PROME:** retain the new research, correct QF1/QF3/QF4 with the exact source evidence above, and carry QF2's wording correction. Continue Horton and the already-planned reserve-estimate work. Keep grades/probabilities and the original fired warning unchanged unless separately adjudicated. This instruction has not been sent. No owner edits, agent launches, trades or publication by CATO. Resume: orient and await Will.
