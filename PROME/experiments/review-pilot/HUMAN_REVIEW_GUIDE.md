# Human validation of the review pilot

Status: PENDING. This guide was prepared during evaluation, before the operator compared conditions. It adds human validation; it does not change the frozen automated scoring rules or primary results.

Open `evaluation-v1/human-review.json` or its readable companion `human-review.md`. Avoid `human-review-mapping-private.json`, individual run files, outcomes, and condition summaries until your grades are recorded. The bundle removes condition labels, but answers or prior knowledge might still reveal a condition; record any suspected identification. No claim of successful blinding is made in advance.

For each OUTPUT identifier, use the supplied question, field specifications and documents to record:

1. Whether every required field is present exactly once and answers the final question correctly, including later corrections or withdrawals.
2. Whether each field's cited documents support its answer. Flag missing supporting steps, even when the automated allowed-source check passes.
3. Any correct answer that uses equivalent wording or formatting rather than the key's exact string.
4. Overall acceptable / unacceptable / uncertain, a brief reason, and whether you suspect which workflow produced it.

Record grades in a separate file keyed by OUTPUT identifier; retain the original bundle. If timing matters, record actual start/stop times and interruptions prospectively. Do not infer past human effort from timestamps or commit history.

The corpus and keys also need human validation: assess whether the intended answers follow from the documents and whether the tasks meaningfully resemble research work. Doing this before grading may reveal intended answers, so disclose the order and whether the same person did both. Human findings should be reported alongside the frozen automated results; any corrected scoring belongs in a clearly labeled additional analysis, never a silent replacement.
