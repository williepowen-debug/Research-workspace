# REGINALD video and concentration review — November 16

## Decision and perimeter

Will asked CATO to examine REGINALD's supplied thread. Recommend a bounded owner correction before the existing closeout/NEXUS synthesis, not a new population study or desk launch. Useful work survives: distinguishing owner-occupied exposure from the supervisory CRE definition and preserving bank-level counterevidence. Neither the video's alarm nor REGINALD's reassurance should outrun the evidence.

Reviewed local HEAD `8577ac3d2d`; REGINALD report/script last changed at `4b09daf765`. Read the report and 53-line script whole, relevant source-transcript lines 25–34 and the 75% claim search match; did not read the entire transcript or independently establish its property cases, Fed papers, prices or bank-specific figures. WALTER delivery log dirty, preserved. No owner files edited, messages sent or agents launched. This is an independent calculation/method review; the sensitivity script is CATO author work, not a replacement canonical bank figure.

## RGV-1 — material method correction: supervisory denominator is not CBLR-only

REGINALD uses total risk-based capital (3792) except for CBLR banks, where it uses tier 1 (8274) plus loan/lease allowance (3123). The report labels the combined results the regulators' own measure. The interagency statement effective March 31, 2020 applies the latter denominator across banking organizations for concentration supervision, not only CBLR. CECL institutions use the loan-and-lease portion of allowance; non-CECL institutions use ALLL. This does not redefine total capital for other uses.

Primary source opened November 16: [Federal Reserve SR 20-8, revised April 2, 2020](https://www.federalreserve.gov/supervisionreg/srletters/SR2008.htm), paragraphs beginning “Accordingly” and “These denominators”. Its explanation of CBLR motivates the change; it does not restrict its scope to CBLR participants.

**Reproduction:** extracted the saved DEWEY SDF archive to an isolated temporary directory, ran REGINALD's unmodified script, then changed only its `if g("3792") and not cblr:` branch to `if False:` to use its existing tier-1-plus-allowance branch for every bank. All other numerator, population, missing-value and parsing choices retained. Both runs exit 0, 4,205 banks, no unmatched files, original figures reproduced. This tests the denominator consequence, not full regulatory compliance or population completeness. The sensitivity output's inherited `basis T1+ACL (CBLR)` label now counts all banks on that basis, NOT actual CBLR membership.

| $1–10B banks, September 30 saved sample | Original | Denominator-only sensitivity |
|---|---:|---:|
| Banks | 889 | 889 |
| CRE excluding owner-occupied / capital median | 226% | 226% |
| Count/share at or above 300% | 177 / 19.9% | 175 / 19.7% |
| Including owner-occupied median | 306% | 305% |
| Including owner-occupied share at or above 300% | 52.2% | 51.9% |

For $10–100B the count changes 15 to 17 (12.1% to 13.7%); all-bank count 375 to 372. Thus the broad owner-occupied distinction survives, but the published exact counts and method claim need correction. EagleBank's near-match alone does not validate all denominators, missing-data handling or numerator scope. A bounded missingness check found all eight requested numerator/capital fields present/nonblank in all 889 $1–10B saved files; do not allege that zeros from absent fields drove this band's result. An initial CSV-based probe failed on a None value; the corrected semicolon parser completed. Ancillary date strings in the diagnostic are not a filing-date audit.

**Owner/closure:** REGINALD checks SR 20-8 and its source-field mapping, updates its script and corrects active report, KB ML-REG-303, STATUS, MEMORY and any NEXUS summary/consumer carrying the old basis/counts. Preserve original result as history. Label the saved sample and omitted growth leg; do not silently use CATO's sensitivity as a fully validated replacement. No need to expand into a new study or compute three years of growth merely to disclose its absence.

## RGV-2 — material inference: exposure concentration is not distress breadth

The report's final sentence says the count supports “concentrated, not tier-wide” stress. A stock of CRE exposure relative to capital measures potential vulnerability, not delinquency, expected loss, extension funding or present solvency. Banks below 300% can be stressed; banks above it need not be. The [interagency CRE guidance](https://www.federalreserve.gov/frrs/guidance/interagency-guidance-on-concentrations-in-commercial-real-estate-lending-sound-risk-management-practices.htm), opened November 16, § Supervisory Oversight expressly denies a safe harbor below the criteria. The 100% construction route is a separate alternative; the 300% plus 50%-growth condition is not the entire supervisory approach.

**Owner/closure:** restrict this result to exposure distribution. Retain any “stress concentrated” assessment only on separately dated credit-quality, funding and loss evidence, with its population limits; this review does not overturn that evidence. Do not describe 19.9% (or the sensitivity's 19.7%) as a ceiling on every bank warranting supervisory scrutiny. It is, at most, a conditional ceiling for the joint 300%/growth criterion on the chosen measure, before assessing completeness.

## RGV-3 — bounded narrative corrections, no fresh property investigation required

The report says every CMBS figure is already held while its own table marks the 75% Class A refinancing claim unverified and not held. Use “mostly familiar; one identified old case and an unverified claim,” not “nothing new” as a blanket dismissal. Its 600 California account is expressly search-summary-level, but the verdict calls it real and the chat calls it not a bank loss. Securitization and no identified bank holder do not establish absence of bank exposure. Either open enough sources for the exact claims or retain “reported CMBS loss; bank holders not established.”

The transcript's capital-cushion language is imprecise but does not by itself establish that the speaker intended the accounting loan-loss allowance. Clarify the distinction without claiming a demonstrated substitution. REGINALD's “a year's reserve” chat phrase is also wrong in kind: allowance is a balance-sheet stock, not a year's earnings or provision expense. Its own broad exposure result roughly supports “about three times capital”; the video's conflation with a different supervisory screen is the stronger supported criticism, not “mostly wrong.”

**Owner/closure:** amend those conclusions and preserve unknowns beside the claims at ordinary correction/closeout. No new score, trading action or mandated trade card follows from this review.

## Delivery and remaining work

REGINALD owns the bounded method and conclusion corrections and its ordinary closeout, including NEXUS synthesis, current-state reconciliation and applicable checks. The previously reported ledger freeze/header cleanup was not independently audited here; do not turn checker success into proof all consumers are current. Avoid reopening all boot work. WALTER/PROME/SLOANE follow-through remains separate. This CATO assessment stops at delivering a concrete correction request to Will; it does not send that request or authorize taking over REGINALD's active work.

Reproduction artifacts: [directory](2026-11-16_1926_reginald-video-review/). Run each saved script with an extracted copy of DEWEY's `research/2026-11-11_003R-population/call-reports-sdf.tar.gz` as argument 1 and its `current-bank-rows.tsv` as argument 2. Original input owner files unchanged. No broad rerun needed after the demonstrated denominator sensitivity.

**Checks and delivery:** verified all ten distinct required check inputs readable. Weekday passed on the three root PROME files (`DOCKET.tsv`, `GATES.tsv`, `WILL_QUEUE.md`), this report and CATO CONTINUITY. Read-cap passed on CATO AGENTS/CHARTER/CONTINUITY and root CLAUDE/USER/AGENTS (continuity 11,201 B). Optional CATO status/calendar/catalyst files absent. Diff whitespace clean. Orphan advisory showed concurrent WALTER history-review and PROME SCRATCH/argus-review/daily-memory changes, not CATO-authored, preserved. No source figure or owner canonical number superseded by CATO: the sensitivity is review evidence with owner reconciliation explicitly pending, not a replacement consumer value. No auto-memory or STATUS-ledger change. Exact-file delivery only; receipt in chat.
