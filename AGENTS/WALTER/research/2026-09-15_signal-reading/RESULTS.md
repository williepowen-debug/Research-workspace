# Oversized-signal reading repair — September 15

## Result and scope

Implemented the user-approved companion for SIG-W-20260619-008. Independent review approves historical interpretive substitution with all **11 obligation/watch items and13 material qualification groups** preserved. Original BOARD remains byte-identical; no new financial grade, primary-source verification, threshold, dispatch or owner completion is implied. Other over-budget signals still require their own review/remedy.

## Reading path and cost

Charter step7 invokes `tools/signal_read_check.py SIGNAL_ID --read`. For the registered case it verifies source, companion and independent review hashes; explicit approval; review date/expiry; UTF8 text; and the canonical fleet byte budget before emitting the whole companion. Unknown IDs or invalid/stale evidence fall back visibly to the original-source read with PARTIAL companion status. A complete oversized read in chunks is not declared a cap remedy. Registry updates require real review; the tool never refreshes its own hashes.

Selected content: **39,509→21,889 bytes**, saving17,620. Charter increased360 bytes and the successful check adds149 bytes of output: net saving17,111 for this observed selected-read path, excluding unchanged boot inputs. Checker reads source/review bytes programmatically; those are not emitted as extra mandatory human reads. Full source detail remains available on demand. If full detail is additionally needed, total reading cost increases accordingly; this is not a promise of savings for every task.

Obligations before/after:11/11; material qualification groups13/13; none retired, stranded or silently marked complete. Recommendations, caveats and final citation-limit block (original143–174) are retained verbatim. Condensed evidence/recipient sections retain dates, conditions, divergent bank bases, commercial-insurance population/approval limits, approximate bankruptcy denominators, hidden condo exposure, aggregate-versus-segment limits and source incentives. Coverage census and exact source/companion hashes: independent-review.md.

## Validation

10 failure-oriented unit tests pass: changed source/companion/review, missing source/ID, due/future review, unapproved receipt, budget, escaped path, wrong source ID and invalid UTF8. Independent reviewer also exercised10 additional failure fixtures and verified the UTF8 repair. Actual CLI --read output equals the reviewed companion bytes exactly; unknown-ID --read rejects without emitting companion text. Source unchanged verified against HEAD.

23 boot BASIS hashes match. Fleet read-cap0 within19 measured declared reads,31 other declarations not counted. Version-drift and archive checks pass; no live workbook ledger requires refresh. PROME reads_check precommit reports UNKNOWN because the new BASIS files have no git history yet; rerun after their first commit before claiming a clean attestation. Only WALTER rows changed in shared READS.tsv; foreign rows verified unchanged.

## Review and remaining limits

The prior September16 repair checkpoint is completed early for this case by the actual read, independent census and implementation tests. Review again **September30 or upon any source/companion change**, whichever first; the checker rejects at the deadline. This does not move owner-evidence or market-observation deadlines. Original source citation and internal-consistency gaps remain explicit research limitations, not defects this reading repair pretends to resolve.

Current foreign PROME/CATO work prevents auto-push under WALTER closeout rules. Commit exact authorized paths locally; no foreign work swept. Postcommit verification and publication status will be recorded separately.
