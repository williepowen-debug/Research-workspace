# Independent companion review: SIG-W-20260619-008

- Date: 2026-11-18T02:44Z (from `date -u`: Wed Nov 18 02:44:18 UTC 2026)
- Reviewer: independent Sonnet reader (read-only except this file)
- SOURCE: `BOARD/SIG-W-20260619-008-south-florida-distress-deep-research-bank-transmission-assessment.md` — 39509 B (`wc -c`), 174 lines, sha256 `17e64d21e944e628139719841335f18e059bb3d1c652a7d93b3998d90274ddd9`
- COMPANION: `AGENTS/WALTER/reading/SIG-W-20260619-008.md` — 21889 B (`wc -c`), 105 lines, sha256 `5d0b19d81e41aaa5e99672cdc95c4e747e91732a394b09b5713dcf5e7ed30d2d`
- Both hashes and sizes are identical to those bound by the 2026-10-22 review.
- Coverage: SOURCE read whole (1-70, 71-142, 143-174). COMPANION read whole (1-105). Prior review used as a criteria checklist only; every row re-checked.
- Tail diff: `sed -n 143,174p SOURCE` vs `sed -n 74,105p COMPANION` -> `diff` clean, IDENTICAL (Recommendations 1-5, 6 Caveats, 3 Verification notes, Remaining open item).
- Tool state: `signal_read_check.py SIG-W-20260619-008` currently prints "PARTIAL ... review future-dated or due; re-review required" (the 2026-10-22 review's next-review date 2026-11-05 has passed; the companion header's own recheck date 2026-09-30 also passed). This review is the recheck.

## Findings

| Item | Source loc | Companion loc | Verdict | Note |
|---|---|---|---|---|
| Dispatch metadata (06-19 23:05Z, PRIORITY, conf 0.85, BANK_COLLATERAL / CONSUMER_STAGFLATION, FL_REAL_ESTATE, to CORAL, INFO x5) | 2-14 | 9 | PASS | All match. |
| Frontmatter "VERIFIED-PRIMARY / none required" overstated vs closing paragraph | 12-13, 172-174 | 15 | PASS | Companion refuses blanket primary verification. |
| Flag closure of SIG-007 Phase 2.8 is lifecycle only | 14, 24 | 9 | PASS | Adds "not proof CORAL integrated"; consistent. |
| 70/30 normalization/crash, Q2-Q3, Iran dominant tail | 28, 66, 78 | 11, 26 | PASS | Labeled dated judgment, not validated probability. |
| "9-11 bps NCO" five-bank all-clear vs bank paragraphs (SSB 9, SBCF 11, BKU ~37 TTM, AMTB 0.45%, VLY none) | 68, 76, 115-125 | 13, 52-56 | PASS | Internal inconsistency correctly surfaced. Source calls BKU's rate "elevated" (119); companion omits the word (MINOR, covered below). |
| CORAL ACTION: split insurance mark; +10.4/+18.8 blended commercial, not condo-only | 34, 107, 103 | 21, 46 | PASS | Colour codes and "resolves SIG-007 TENSION" omitted; non-load-bearing. |
| CORAL: add AMTB; top-six artifact; synchronized diagnostic; Ch7 ~230/100k; Q2 re-test | 35-37 | 21, 56 | PASS | Retained. |
| REGINALD: BKU ACL 0.87% not 1.21%; deposits; 6/8 cohort read | 40 | 22 | PASS | Retained. |
| CARL: consumer-led; energy >60% of May CPI gain; core 0.2/2.9; forward risk; Snaith no recession | 43, 80, 139-141 | 23, 66, 68 | PASS | Rupkey quote omitted; non-load-bearing. |
| SHADE: wholesale vs commercial; liability/umbrella; condo-master undisclosed | 46 | 24, 42, 46, 58 | PASS | Retained. |
| MARCO: cost stack/out-migration; Spirit not FL demand, SDNY, ~$100M fuel | 49, 131 | 25, 62 | PASS | Retained. |
| RED: incentive discipline, realized-data preference, aggregate vacancy, 70/30 | 52, 125, 133 | 26, 38, 58, 64 | MINOR | "Miami office vacancy lowest of top-25" dropped; 12.5/15.7/17.6 figures survive. |
| Bankruptcy national/district figures (591,850 +11.9%; 25,960; 565,890; MD 27,925 vs 21,927 #2; SD 16,326 vs 14,387 #6) | 72, 88-90 | 36 | PASS | Match. |
| FL 44,496 +22.2% from 36,407: "nonbusiness" (72) vs "total" (97) | 72, 97 | 36 | PASS | Inconsistency correctly flagged unresolved. |
| Per-capita FL 190, SD 222, MD 199, US 168-173, AL ~520; SmartAsset/BankruptcyWatch; Dec-2025 proxy | 64, 95-99 | 38 | PASS | Match with caveats retained. |
| Chapter-level counts (US Ch7 369,702 etc., district Ch7/11/13 pairs), Maryland ~203, FL "third in growth" | 88, 92-93, 97 | omitted | MINOR | Non-load-bearing for conclusions; Ch7 tripwire lacks a Ch7 baseline in companion (companion does flag total-vs-Ch7 basis mismatch, line 28). |
| "Chapter 11 is not exclusively consumer" | 72, 88 | 36 | MINOR | Reader caution, not in source as such; derived. |
| Insurance reinsurance: GC -15/-20, Gallagher 20-25/22.8, Aon/Howden to 25; ARDC -0.46%; FHCF -9.51%; CR 77 vs 92; surplus +45%; $4.3B cat bonds | 103 | 42 | PASS | Match; benign-season condition retained. |
| Citizens personal: -2.6% filed, ~-8.7/-8.8% approved, eff Jun 1 2026-May 31 2027; 463,096 / 59.2% / -11.5%; Insurify $8,458 vs $2,948 | 105 | 44 | PASS | Match. |
| Citizens residual 1.41M -> 336,000 -> 293,404 | 105-109 | 44 | PASS | Match. |
| Commercial +10.4/+18.8; MP +9.6/+21.3; wind +10.9/+17.2; property-only 10-20%; SIRS/HB1021-1203 | 107 | 46 | PASS | Match; blended-line caveat retained. |
| SSB metrics | 115 | 52 | PASS | All figures match (ROA/ROTCE/$49.5B omitted, non-load-bearing). |
| SBCF metrics | 117 | 53 | PASS | Match. |
| BKU metrics | 119 | 54 | PASS | Match; CET1 12.2%, NIM, EPS omitted. |
| VLY metrics | 121 | 55 | MINOR | Match; "CRE concentration ratio edged down" and "not showing a Florida-driven break" dropped. |
| AMTB metrics | 123 | 56 | PASS | Match. |
| Condo-master not isolated; managements structurally optimistic | 125 | 58 | PASS | Retained. |
| Business: SubV +36%, Ch11 -~7% (684 v 739), Spirit May 2 SDNY ~$100M, Darden 28 | 129-131 | 62 | PASS | Match. |
| Vacancy: Miami office 12.5/15.7, US 17.6, Tampa 15.1; retail 2.8/3.0/3.4 vs 4.2; no segment series | 133 | 64 | PASS | Match. |
| Energy/CPI: Hormuz closed since Feb 28; Brent 117/107/77-92; EIA 105, 79; May CPI 0.5/4.2, energy 3.9/23.5 (>60%), core 0.2/2.9, core goods -0.1, transport -0.6 | 137-139 | 66 | PASS | Match; marked as June context. "Highest since April 2023" dropped. |
| Snaith/UCF GDP 2.1->1.8->1.7, no recession, housing flattened, no audited scorecard | 141 | 68 | PASS | Match. |
| Recommendations 1-5, Caveats, Verification notes, Remaining open item | 143-174 | 74-105 | PASS | Byte-identical (diff clean). |
| Source line-range references in companion headings | n/a | 7, 32-70 | PASS | Ranges map to correct content (heading grep: 33-53 wrapper, 86-99 bankruptcy, 101-109 insurance, 111-125 banks, 127-142 business/macro, 143-174 tail). |

## Currency check (item 5): PASS
Companion line 3: "**Historical interpretation only — June 19, 2026 packet, reviewed September 15, 2026.** This is a WALTER reading aid, not a new signal, independent primary verification, current market grade, owner receipt or change to a registered threshold."
Line 11: "Its June war-state/“ceasefire” language, future Q2-print statements and oil levels must not become current context."
Also lines 66 ("Those are not current prices, confirmed present war-state or contract-matched trigger inputs") and 68 ("Do not carry the June “post-ceasefire” wording as present fact"), and line 72 for the verbatim tail ("“Today,” unavailable Q2 releases, prices, probabilities and proposed tripwires refer to June19").

## Claims in companion absent from source (item 6)
None is a new figure or conclusion. Companion-originated reader cautions, all derived from source text and labeled as companion observations: NCO inconsistency (13; derivable from 115-125 vs 68/76/125); Ch7 ~230/100k not comparable to total-filing rates and "sustained" undefined (28); Chapter 11 not exclusively consumer (36); 463,096 is filing population not June 12 count (44; arithmetic 463,096 > 293,404); "neither realized all-market increase nor condo-only" (46); "no completion inferred / flag closure not proof of integration" (9, 19); "Snaith's slower GDP path does not forecast recession" (23, matches 141). "Reviewed September 15, 2026" (3) is a companion-process date, not a source claim.

## Other observations
- STALE REVIEW CLOCK: companion line 3 says "Recheck ... September 30, 2026"; that and the prior review's 2026-11-05 next-review date have both passed, and `signal_read_check.py` currently reports PARTIAL for that reason. A PASS here supports re-registration of the review, but the companion header text (line 3) still names the old 09-15 review date and 09-30 recheck; the owner should refresh it only on content review. I did not edit anything.
- FORMATTING: the companion pervasively omits spaces between words and numbers ("at23:05Z", "confidence0.85", "SSB9bp", "Chapter7", "Q1 ... 12months"). Content is intact, but root Output Canon says never glue words/numbers to save bytes. Readability MINOR, not a content defect.
- Pointer tests: link to `../research/2026-09-15_follow-through/signal-read-review.md` resolves; `AGENTS/WALTER/tools/signal_read_check.py` resolves.
- No FAIL items. MINORs are omissions of secondary metrics, ranking trivia and two dropped descriptive phrases ("elevated" on BKU NCO; VLY "no Florida-driven break").

VERDICT: PASS — companion may substitute for the source

---

WALTER approval (2026-11-18T02:45:37Z, walter-85, on the independent Sonnet reader's PASS above; REGINALD packet 2026-11-17 DOCKET L889). Source, companion and both hashes are unchanged since the 2026-10-22 review. Next re-review **2027-05-17** (six months, on REGINALD's suggestion): the source is immutable and hash-bound, so any correction banner or other byte change on it, or any companion edit, invalidates this approval at once; the date is a backstop, not the main guard. The reader's MINOR items are non-load-bearing omissions. Known and accepted: the companion's own header still names the September review dates, and it runs some words and numbers together; fixing either changes its bytes and would need another independent review, so it is carried, not fixed tonight.

Verdict: APPROVED
