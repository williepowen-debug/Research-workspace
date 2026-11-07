# CARL scoring — independent replication, November 7, 2026

Reader: `/root/carl_scoring_review`, OpenAI Codex; exact model variant not exposed. Scope: the two existing CARL scoring assignments only. Authority: parent assignment under UPGRADE_PROTOCOL review-method 4/4b. No owner file, probability, outcome, method or maturity grade changed. This is independent replication, **not a blind discovery claim**: parent findings were visible in inherited context and additional metadata arrived during the review.

## Counterexamples stated before verdict

1. The aggregate would be wrong if a current binary outcome, original mark, or existing WQ-112 ruling differed from the row used; a Notes maximum is not an original probability. I read actual rows and exact historical claims, including the reassigned March IDs.
2. CRL-15's re-mark could be supported if a comparable current rate, defined denominator/window and dated reasoning established its distance to the unchanged 6.5% bar, and if that mark preceded a publicly knowable resolution. A March TTM rate and absence of an owner read do not establish those conditions.
3. CRL-23's re-mark could be an honest forward probability even after adverse interim data; a forecast is supposed to update on public information. It would be late if the target quarter's outcome or a conclusive kill were already public. Conversely, remaining above a threshold does not itself justify a probability cut, especially when the new figures are closer to it.

## Verdicts

| Leg | Verdict | Evidence and limit |
|---|---|---|
| CRL-21 60% scoring mark | ACCEPT | First-call 60% is in STATUS at `656c41795` and the current machine field restores it under WQ-112(ii). The former 25% field lacks a re-mark date; the narrative dates a leg failure, not a valid dated machine mark. MISS contributes 0.3600, not 0.0625. This read does not re-grade the full underlying ABS/issuer evidence. |
| Current resolved aggregate | ACCEPT | Eleven CONFIRMED/MISSED rows, two hits and nine misses; sum 4.6303, mean **0.42093636**. Exclude OPEN, NO-VERDICT, RETIRED and MIXED; do not treat MIXED as 0.5. CRL-15/23 contribute nothing yet. |
| Original-call comparison | ACCEPT WITH LIMITS | Same eleven row lineages; CRL-08 original 85% instead of eligible revised 28%; all other current scoring marks equal their original/earliest-known marks. Sum 5.2744, mean **0.47949091**. CRL-11 is earliest recorded June 5, not proven March 31 as-made; CRL-07/08 windows and CRL-08 kill were subsequently changed, so this is not a pure unchanged-question/horizon comparison. |
| CRL-15 10% November 6 mark | DATED FIELD VERIFIED; EVIDENCE ACCEPTANCE WITHHELD | The cited 4.8% is TTM through March 31, not a current November rate. Current Lumos page is dated July 17, before the July 24 35% change; October 28 is the owner's read date. The +170bp-in-two-months rationale conflates data age with time remaining. Calendar-end claim versus FY2026 file is not reconciled. Current official-file metadata contradicts the unqualified claim that the September 30 file is not out. None of this establishes that the precise target outcome was already knowable, because no comparable rate was reconstructed. Contest the rationale, preserve 65/35/10 and their dates, do not invent a replacement mark or outcome. |
| CRL-23 15% November 6 mark | PRE-RESULT TIMING SUPPORTED; NUMERICAL REDUCTION NOT ESTABLISHED | PHM issuer October 22 release confirms Q3 home-sale GM 24.8%. DHI October 29 transcript reports forward Q1 guide 18–18.5%; the read source is third-party transcript reproduction, not issuer audio. Target DHI quarter ends December 31 and PHM Q1 is in 2027. No final result/kill established by November 6. However, DHI guide fell from prior 20.5–21 and PHM actual from 25.0: both moved toward the downside bars. Distance above the bar establishes neither a 15% joint probability nor that the new evidence supports cutting 45 to 15. Contest that derivation while preserving the dated forward judgment and original70. |

## Arithmetic reproduced with Decimal

| Row | Outcome | WQ-112 mark | Original / earliest-known | WQ-112 loss | Original loss |
|---|---:|---:|---:|---:|---:|
| CRL-01 | 0 | .75 | .75 | .5625 | .5625 |
| CRL-03 | 0 | .90 | .90 | .8100 | .8100 |
| CRL-04 | 1 | .88 | .88 | .0144 | .0144 |
| CRL-07 | 0 | .80 | .80 | .6400 | .6400 |
| CRL-08 | 0 | .28 | .85 | .0784 | .7225 |
| CRL-09 | 0 | .75 | .75 | .5625 | .5625 |
| CRL-11 | 0 | .85 | .85 | .7225 | .7225 |
| CRL-16 | 0 | .60 | .60 | .3600 | .3600 |
| CRL-18 | 1 | .60 | .60 | .1600 | .1600 |
| CRL-21 | 0 | .60 | .60 | .3600 | .3600 |
| CRL-24 | 0 | .60 | .60 | .3600 | .3600 |
| Total | 2/11 | mean .691818 | mean .743636 | **4.6303 / 11** | **5.2744 / 11** |

The 0.05855455 gap is entirely CRL-08's accepted revision. It is not evidence that the November 6 revisions worked. Adding CRL-21 at .36 lowers the prior ten-row average .42703 to .42094 even though the added forecast missed: an average moving down does not prove improving reliability. Both current aggregate variants exceed the fixed 50% benchmark loss .25 on this sample. High confidence with two hits is poor calibration in the included set; eleven heterogeneous, related, selectively resolvable forecasts do not estimate CARL's whole-system reliability or future skill. Exclusions and horizon/spec changes matter. An ex-post base-rate benchmark is not an available ex-ante forecasting strategy.

## Historical provenance actually reopened

- `91c301279:AGENTS/CARL/workbook/PREDICTIONS.tsv`: exact gas-pump peak claim CRL-01 75% (the current thesis path did not exist there).
- `9e30a573c1:AGENTS/CARL/workbook/PREDICTIONS.tsv`: exact FL UI/DQ CRL-07 80%, gas-$4.50 CRL-08 85%; same in `8d250848b9`. Commit March 9 UTC and rows label Date_Made March 10; no exact-day as-made certainty claimed. Original windows May–June and March20–April5 differ from later versions.
- `4e8c98359:AGENTS/CARL/STATUS.md`: exact Fannie claim is old CRL-05 90%, now CRL-03; student90+ claim old CRL-06 88%, now CRL-04. IDs alone would be wrong.
- `656c41795:AGENTS/CARL/STATUS.md`: CRL-18 60% and CRL-21 60%.
- `bf073316af:AGENTS/CARL/thesis/PREDICTIONS.tsv`: CRL-15 65% with the same 6.5% claim.
- `e7177e56e:AGENTS/CARL/STATUS.md`: CRL-23 original 70%.
- `6e748c97e:AGENTS/CARL/thesis/PREDICTIONS.tsv`: CRL-24 original 60% while OPEN.
- `a5ac65852:AGENTS/CARL/thesis/PREDICTIONS.tsv`: CRL-07's 80-to85 history and CRL-08's 85-to80 history/extended window.
- `5d49f49056` records the two new machine-field marks at November 6 13:41:15 ET. Existing September 24 report and owner reply supply already-adjudicated09/11/16 scoring provenance; their underlying original blobs were not all independently reopened in this reader pass.

## External evidence read and coverage limits

- [Lumos original analysis](https://www.lumosdata.com/blog/sba-default-rates-small-business-credit-risk-2026): current page dated July17; 4.8 is March TTM. A current dated webpage is not an immutable historical snapshot.
- [Lumos measurement definitions](https://www.lumosdata.com/blog/how-lumos-measures-default-and-prepayment): current page dated August18; several constructions/windows differ. Vendor's own construction, not an independently recomputed official rate.
- [PulteGroup October22 issuer release](https://pultegroup.com/investor-relations/news/news-details/2026/PulteGroup-Reports-Third-Quarter-2026-Financial-Results/default.aspx): 24.8% Q3, includes impairments; target is future Q1.
- [DHI October29 issuer release](https://investor.drhorton.com/~/media/Files/D/D-R-Horton-IR/press-release/dhi-q4-2026-earnings-release.pdf): dates and operating context. It did not establish the Q1 GM guide in the inspected release text.
- [DHI transcript reproduction](https://www.earningswhispers.com/transcript/DHI/Q42026), HOMER saved excerpts, plus search-returned Motley Fool/ROIC reproductions: same18–18.5 guidance, third-party sourcing. No issuer audio replay.
- Parent's saved official SBA resource HEAD receipt was read. HTTP200 with Last-Modified October30 is evidence of an available resource now and supports prior availability; not a complete dated publication audit or computation of CRL-15's outcome. Reader's attempted generic SBA `/dataset/7-a-504-foia` URL returned404; that guessed route's failure is not absence of the official data.

No current target outcome was assigned for CRL-15 or23. No full CARL ledger-outcome re-adjudication, market recommendation, causal attribution, or numerical recalibration model was performed. Public-availability evidence cannot prove what CARL knew internally.

## Hash pins at reader source completion

Observed HEAD `a5790484a131cbec452b73ece2182d5759e9690e`; hashes below identify actual inputs independently of concurrent HEAD motion.

| Path | SHA256 |
|---|---|
| AGENTS/CARL/thesis/PREDICTIONS.tsv | c58bee834d20c142e1873862106e284eaa69bbf4ddcde6d6729ca3b01f53fabe |
| FORGE/PREDICTION_DISCIPLINE.md | e4748d4a95457c56b564f1effd12cdd0b034354b0bca4498d0da494da63c91ab |
| AGENTS/DAEDALUS/runs/2026-09-24_CARL_BRIER_RESCORE_AND_CRL08_RULING.md | 307595910d83e3cfd13577c5b8d78e7e9303750c5628430db747bf66190421eb |
| AGENTS/CARL/sub_agents/POP/state_vectors/SV-POP-2026-10-28-01.md | 786da339d45415205958243de572d61ad931c3fcf57eb49c3fcc74a30c7869c8 |
| AGENTS/CARL/sub_agents/POP/state_vectors/SV-POP-2026-10-28-02.md | 38fb632c644f835ed806f444885b933f1ab0ad41ed8f254c09e09f08af3d6f17 |
| AGENTS/HOMER/workbook/BUILDER.tsv | a863e9b15c5fb4b0a4cdfdd5032eda020117ec40caef1608c64040708219b0cf |
| AGENTS/HOMER/reports/2026-11-05_evidence/dhi_fq4_call_excerpts.txt | c844ba82a0673c2c47c9ffe76bbc6beed3c7c7e41d43fda829918df48221b1e1 |
| AGENTS/DAEDALUS/runs/2026-11-07_CARL_SCORING/SBA_RESOURCE_HEAD.json | 9e30fb3d6a153b5025aa87d0073a977187f7788b631711650c2f55706ca9d2db |

## Final candidate acceptance

Parent candidate `runs/2026-11-07_CARL_SCORING.md` read whole through its final coverage-limit paragraph; calculation source read whole; RESULTS parsed completely and reproduced byte-for-byte by running `calculate.py` with `Path.write_text` intercepted in memory (no artifact writes). All seven INPUTS.json source hashes still match current bytes. Historical rows embedded in RESULTS are generated from named immutable commits, not moving HEAD.

**ACCEPT within the declared scope, zero required corrections.** The result preserves originals and existing scoring rules, reproduces both aggregates, excludes both OPEN rows, identifies the date/basis defect without claiming a known SBA outcome, and qualifies CRL-23's timing separately from its unsubstantiated numerical reduction. The limitations on changed windows, CRL-11's earliest-known probability, inherited outcome grades, third-party transcript sourcing and historical public availability are material and present. The report requests explanation of the two revisions; it neither writes replacement marks nor imposes a new model, checker or fleet rule. Final review metadata may be updated to record this acceptance; any substantive later edit is POST-REVIEW until re-read.

| Candidate | SHA256 |
|---|---|
| runs/2026-11-07_CARL_SCORING.md | d8c6f01047037f027000c2a8d12753ff2ce1d36e11610b879335ef6baeaa1ed5 |
| runs/2026-11-07_CARL_SCORING/INPUTS.json | e9be016e93cefde6eca5421b0dac7bb34863ff4cd274e1a6d9602a99262c7aa9 |
| runs/2026-11-07_CARL_SCORING/calculate.py | d5e0a1fcb447e2240fb290519261d74115eeaf8349f5eb96f778fd990687171f |
| runs/2026-11-07_CARL_SCORING/RESULTS.json | f471b3d7bcd48e5fdb3468087a3a31a3ce4d34d9b2a7c5a6c1c846ce720963c3 |
| runs/2026-11-07_CARL_SCORING/SBA_RESOURCE_HEAD.json | 9e30fb3d6a153b5025aa87d0073a977187f7788b631711650c2f55706ca9d2db |

Reader complete and stopped. No background process or lifecycle dependency remains. Parent owns exact-path commit/publication and recipient coordination.
