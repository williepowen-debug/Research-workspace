# SAM closeout additions — expiry integration verified, memory claims need narrowing

September21, 2026, CATO for Will. Reviewed `730edfa0a` at initial shared HEAD `2bbb38f61`. Scope: new memory addition, dated expiry integration and peer-consumption assertion. The earlier correction chain remains closed under [its receipt](2026-09-20_1924_sam-chain-closure.md); these are newly published closeout claims. Concurrent auto-memory edit and three untracked CATO CRUISE reports preserved; no pull, owner edit or message.

## Verified delivery

- `docket/CALENDAR.md` and `docket/CATALYSTS.tsv` contain the September22 15:15 JST source-age deadline, distinguish October30 decision expiry, and keep the publisher holiday gap conditional.
- Ran `.venv/bin/python3 -B AGENTS/SAM/scripts/catalyst_countdown.py --days 3`: exit0; the OIS expiry appears under imminent events with the correct time, source-age explanation and SAM-owned review action. This verifies visibility in the date-level countdown, not a new intraday scheduler. Actual stale-quote rejection remains the existing validator's job.
- Existing `memory/auto/finding_output_shape_implies_more_than_the_measurement.md` was extended, rather than duplicated. Its existing auto-memory index reference is present; SAM's local MEMORY links the extension and carries the dated next action. Actual next-session memory retrieval was not executed or certified.
- The brief carries a re-read warning. A targeted search of markdown/TSV files in AGENTS and PROME, excluding SAM/CATO, found no matches for the new cumulative1.94/hike-or-April wording,63%-next-hike/December wording, source-image hash prefix or exact September18 quote timestamp. This supports “no matching peer citations found” within that search, not proof that no peer consumed anything or no paraphrase exists. No recipient-specific copied error was established and no packet was sent.

## F1 — Medium: five dark days are conflated with the propagation delay

New `NEXUS_BRIEF.md:3`, `MEMORY.md:49`, `thesis/CHANGELOG.md:27` and `thesis/timeline/TIMELINE.md:9` say the brief told peers pricing was unavailable for five days after that became false. The commit record establishes a different sequence:

| Event | Commit | Author/commit date, EDT |
|---|---|---|
| Reviewed quote restored to ledger/STATUS | `a16c17f6b` | September20 11:04:22 |
| Peer brief updated to restored pricing | `bed42686f` | September20 12:26:15 |

The committed restoration-to-brief lag was1h21m53s on the same day. That is distinct from SAM's reported September15–20 period without current reviewed pricing. The exact first in-session availability time could precede its commit, but nothing in these records supports five subsequent days of stale propagation.

Suggested replacement on the four new surfaces: **Pricing was restored September20; the brief initially retained the old unavailable claim and was corrected later that day.** Keep the missing-pricing period and publication lag separate. Do not replace it with a falsely precise wall-clock lag unless explicitly using commit times as the measurement.

## F2 — Medium: memory overstates what CATO reproduced and certified

The new shared-memory extension says every number SAM published was correct and independently reproduced by a reviewer, and every measurement layer was clean. Local MEMORY and the timeline repeat that universal claim. The receipts establish five image-row transcriptions, the rounded event-study table from a same-vendor rerun, and particular arithmetic/boundary checks. They explicitly do not certify all vendor inputs, current broker positions, funding allocation, causal identification or whole-desk measurements. A contradicted TBT14 is itself in the six-row example table; it is not a verified current holding merely because that numeral appeared in a source file.

The new memory also repeats approximately all the intervention total falling on two days. The prior study labels one day's value an estimate and the other a residual; the follow-up review expressly withheld official allocation certification. Preserve that status rather than teaching the allocation as an established corrected fact.

Suggested replacement: **The checked OIS transcription and rounded study calculations reproduced, but several conclusions and labels exceeded their evidence. Review summary claims separately and inspect all active sibling references after a correction. Other measurements and current holdings were not comprehensively certified.** This retains the useful lesson and avoids a blanket “measurements never fail” exemption. The13-point tally is SAM's own accounting; CATO has not performed a separate complete finding-count audit.

## Scope and disposition

Accept the dated expiry integration and reuse of an existing memory. Ask only for correction of the new history and verification-scope claims, across the closeout surfaces that repeat them. No new rule, gate, calendar rebuild, chart re-review or market study is needed. No publisher holiday schedule or new market/broker state checked. Only CATO report and SAM continuity entry authored; whitespace and four-file weekday checks passed. Orphan advisory flagged the concurrent auto-memory edit, preserved along with other CATO reports. Exact-path receipt follows in-session. Next for this conversation: orient and await Will; other CATO sessions unaffected.
