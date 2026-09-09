# Review pilot v1: no observed acceptance advantage

**Completed September 8, 2026. Automated feasibility results; human validation PENDING.** Separate review and continued-context self-review each passed the frozen acceptance check in 22 of 24 workflows (91.7%). All final answer values were correct in both arms. Every acceptance failure came from citation eligibility on the same source-dependence task. This pilot does not establish a research-quality advantage for either workflow.

## Design and execution receipt

VERIFIED: twelve synthetic tasks, three families, two repetitions in each of two conditions: 48 scheduled and completed workflows, 144 completed turns. Practice was separate. The inputs were frozen in commit `96b3b8ad5` at 21:59:29 ET; evaluation began at 21:59:38 ET and finished at 22:17:08 ET. Freeze verification passed immediately before analysis. Sources: [freeze](FREEZE.json), [provenance](evaluation-v1/provenance.json), [completion](evaluation-v1/finished.json), and the individual run records. The frozen `evaluation_started:false` flag describes the pre-evaluation freeze, not current completion status.

Both arms used gpt-6-astra, CLI 0.153.4 and three turns: draft, review with updated evidence, final revision. Every turn requested low reasoning effort; saved settings events report low. Thread creation initially reports high before that per-turn override. Self-review continued the analyst conversation; separate review used a fresh reviewer session, then returned the review to the original analyst. This treatment includes differences in conversation history, message roles and repeated context.

VERIFIED: no failed workflows, recorded harness retries, missing usage records or observed tool/interactive requests. Hidden provider retries are unobservable. The largest observed workflow total was 27,831 tokens, below the 60,000 inter-turn stopping threshold. That threshold is not a hard token cap. Total evaluation usage was 1,293,059 tokens, including input context replay; this excludes development, orchestration and report review.

## Frozen automated results

Source: [summary and paired differences](evaluation-v1/summary.json), [all scheduled outcomes](evaluation-v1/outcomes.csv). Acceptance requires correct values, eligible citations and valid shape.

| Measure | Self-review | Separate reviewer |
|---|---:|---:|
| Completed workflows | 24/24 | 24/24 |
| Initial acceptance, against initial evidence | 22/24 | 22/24 |
| Final acceptance, against final evidence | 22/24 | 22/24 |
| Final value checks passed | 138/138 | 138/138 |
| Final citation-eligibility checks passed | 133/138 | 134/138 |
| Fields repaired against final evidence | 36 | 36 |
| Newly failing field checks | 1 | 0 |
| Valid review flags / visibly acted on | 36/36 | 36/36 |
| Invalid flags / valid flags ignored | 0/0 | 0/0 |
| Total observed tokens | 656,068 | 636,991 |
| Mean observed tokens per workflow | 27,336.2 | 26,541.3 |
| Mean summed turn latency per workflow | 20.57 seconds | 22.56 seconds |

All 24 task/repetition pairs tied on final acceptance. The same task failed in both repetitions in both arms. Repetitions are clustered within twelve tasks; these are not 48 independently sampled research problems. No significance test was performed.

| Task family | Self-review final acceptance | Separate final acceptance |
|---|---:|---:|
| Source dependence | 6/8 | 6/8 |
| Supersession | 8/8 | 8/8 |
| Correction application | 8/8 | 8/8 |

VERIFIED: all designated no-change controls passed in both arms. The 36 repaired fields per arm include applying information introduced at review time; they must not be described as 36 mistakes against the original evidence. This experiment has no no-review baseline, so it does not measure whether review itself was necessary.

Separate review used 19,077 fewer observed tokens overall (2.91%), with fewer tokens in every paired comparison. Its mean summed turn latency was 1.99 seconds longer. INFERRED: the token difference plausibly reflects the conversation layout, not superior reasoning efficiency. Latency excludes process launch/setup; cache use and runtime variability complicate cost comparisons. Actual dollar charges are UNAVAILABLE, human effort minutes UNMEASURED, and no money or human-time savings are claimed.

## Citation failures require human adjudication

VERIFIED: all failed checks are on `sd_e01`, where the model correctly identified one north-room observational root and a 30% rate. The answer also cited `sd_e01_d`, an independent inspection explicitly confined to south rooms. The frozen key excludes that document as support for the north-room answer. Both arms cited it for root count and support classification; in self-review repetition 2 the final revision also added it to the root-ID field. That additional citation produced the sole newly failing field check. The reviewer emitted no flags in these runs.

INFERRED: citing the south-room document could be a reasonable way to show why it was excluded from the north-room root count. The automated failure may therefore reflect an overly narrow citation key, rather than an analytical mistake. The pre-freeze AI key review missed this exclusion-evidence interpretation; its reviewer acknowledged that omission in the [result review](RESULT_REVIEW.md). The observed one-field difference is not evidence that self-review damaged substantive reasoning. Keep the frozen results intact; any human adjudication or alternative scoring must be a separately labeled analysis. Inspect [the task and keys](corpus.json) and runs [024](evaluation-v1/run-024.json), [025](evaluation-v1/run-025.json), [030](evaluation-v1/run-030.json), [031](evaluation-v1/run-031.json).

## Interpretation, limits and next step

The narrow result is a tie in automated acceptance, with a ceiling on answer-value accuracy and a citation-scoring ambiguity. It does not prove equivalence or that separate review never helps. These short AI-authored tasks, checked by another AI before freeze, leave human task/key validation pending. Citation scoring only tests predefined eligibility, not completeness of supporting reasoning. Exact-string matching may reject equivalent answers; automated flag validity does not establish that the explanation is sound.

This is one model identifier and settings configuration, not an immutable provider snapshot, and fresh sessions rather than persistent specialist desks. No live evidence retrieval or actual file-edit execution was tested. The original public draft's hard equal-token ceiling and human grading were not completed; this disclosed feasibility variant used equal three-turn opportunity and observed usage. Human validation is still PENDING, and no public-demo files were changed.

Next: validate the tasks, keys and outputs by hand using the [human-review guide](HUMAN_REVIEW_GUIDE.md) and [condition-masked packet](evaluation-v1/human-review.md). Masking is not proof of blindness. If a second experiment is warranted, freeze a new study with more demanding tasks and a citation rubric that distinguishes evidence supporting inclusion from evidence supporting exclusion. Do not harden or rerun this batch after seeing its results.

Will selected the research question and authorized execution. PROME and its AI helpers implemented the harness, authored and checked the corpus, ran the experiment and prepared this report. The result provides a completed, inspectable comparison and a concrete measurement limitation; it does not validate the wider fleet or establish fellowship admission prospects.

**Result-review closeout and declared residue — September 8, 2026:** The [independent AI result review](RESULT_REVIEW.md) verified the numerical table, paired comparisons and citation account. Its retry-wording blocker is corrected above, and its key-review omission is disclosed. The exact pre-analysis verification and guide-preparation order are operator-reported from this session's tool execution; the committed provenance does not independently timestamp those later actions. Current frozen-input integrity was independently rechecked. The reader sampled four workflow records for turn settings; the broader all-record checks are PROME's audit, supported by [the audit receipt](evaluation-v1/audit.json) and retained run events, not a claim that the independent reader inspected every event. Human validation, semantic citation adjudication, hard token enforcement, actual charges and human labor measurement remain unresolved limits; no further scoring or frozen-input changes were made.
