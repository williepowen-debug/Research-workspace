# CRUISE correction receipt — substantial repair, incomplete propagation, new inference overreach

**Date:** 2026-09-20, approximately 12:25–12:31 EDT. **Reviewer:** CATO, CRUISE-only session. **Scope:** verify the CRUISE response relayed by Will against the [original eight-finding report](2026-09-20_1103_cruise-evidence-registration-review_9f24c7.md), inspect subsequent CRUISE corrections, and assess the new voyage-length inference. No authority borrowed from other CATO sessions or the owner's separately reported approvals.

**Snapshot:** `80622311e02bebf4bcc13531ce5fc332c64e8275`. Owner's principal correction `62795cc17`, followed by CRUISE claim-marking changes `aeb9f61c3`, `ac78be234`, and `635233dbb`. Ten core reviewed files matched that snapshot byte-for-byte at the closing evidence check. The uncommitted original CATO report and another session's memory edit were preserved.

**Remote receipt:** read-only `git ls-remote origin refs/heads/master` returned exactly `80622311e02bebf4bcc13531ce5fc332c64e8275`; local `git merge-base --is-ancestor 62795cc17 80622311` returned 0. This independently establishes that the reported CRUISE correction commit is on the observed remote branch. No fetch, pull, stage, commit or push was performed. Live notification delivery was not independently inspected; CRUISE's correction outbox artifacts to TERRY and CARL were read.

## Disposition

CRUISE accepted and implemented substantial corrections. The principal Truist interpretation, invented discount bound, December-share confound and unsupported credit-access conclusions are withdrawn in the current operator-facing correction blocks. CRU-10 now explicitly disclaims causal identification in its Notes while retaining its original numerical forecast and probability. CRU-09's live denial example is corrected, including the separate-other-competitor case.

**Do not close this as “all applied” yet.** Three material follow-ups remain: the new voyage-length conclusion repeats the outcome-to-cause error; several source-paper claims remain uncorrected at their locations despite a categorical completed-sweep receipt; and CRU-09's frozen-reference path still sends a strict reader to the pre-correction examples. A fourth, smaller issue reverses the direction of copying that publication chronology excludes. These are bounded documentary/interpretive corrections, not a request for another general research sweep, new controls, or a changed trade.

## R1 — HIGH: the new average-duration result is correct; the capacity/yield/consumer conclusions do not follow

**Locations:** `AGENTS/CRUISE/workbook/KB.tsv:111` (KB-CRU-110); `STATUS.md:10`; `TRADE.md:11`; capacity paper correction banner; CRUISE's September 20 correction packets to TERRY and CARL.

I reproduce the calculation from the [NCLH Q2 10-Q statistical table and terminology](https://www.sec.gov/Archives/edgar/data/1513761/000110465926089657/nclh-20260630x10q.htm):

```text
2025: 6,288,800 passenger cruise days / 738,635 passengers = 8.514083 days
2026: 6,745,954 passenger cruise days / 906,689 passengers = 7.440207 days
Change: (7.440207 / 8.514083 - 1) × 100 = -12.612940%
```

This is **average cruise duration per passenger carried**, not an unweighted average across sailings or an observed voyage count. The filing defines capacity days using available berths and days in service, and net yield as adjusted gross margin per capacity day. Its MD&A attributes the increase in capacity days to delivery of new ships.

Three separate overextensions need narrowing:

1. **Shorter average passenger duration does not explain capacity-day growth.** More turnarounds within the same number of operating days do not create extra berth-days. The sentence in KB-CRU-110 and the TERRY packet that NCLH grew its capacity-day base substantially by running more, shorter voyages is not established by this division. Available berths, service days and voyage/passenger mix need separate treatment. Nor does a passenger-weighted average alone prove a larger number of sailings: passengers can redistribute across existing short and long itineraries.
2. **A duration change does not mechanically change yield per day.** Different itineraries can have different per-day fares, onboard revenue, variable costs and occupancy, so mix is a plausible influence. But the observed average alone does not measure that influence or its sign. Fewer days per guest also means less spending per guest at a constant daily spend; that is not, by itself, lower revenue per day.
3. **It does not demonstrate a non-consumer explanation, especially at Carnival.** CARL's packet calls it a fleet decision far removed from household spending, then later calls the cause unproven. Changing trip length can reflect supply choices, customer affordability preferences, geography or brand mix. An NCLH observation cannot establish that CCL's mix changed, or that any CCL actual-versus-guide difference was caused by mix. The guide may already incorporate planned deployment.

**Reviewer counterexample, executed as simple arithmetic:** one 100-berth ship operating 70 days at full double occupancy, with $200 adjusted margin per passenger-day:

| Schedule | Passengers carried | Capacity days | Net yield |
|---|---:|---:|---:|
| Ten 7-day trips | 1,000 | 7,000 | $200/day |
| Fourteen 5-day trips | 1,400 | 7,000 | $200/day |

Trips get shorter and passengers increase, while capacity days, occupancy and yield are unchanged. This is not an estimate of NCLH's economics; it disproves necessity of the asserted relationship.

**Proposed replacement:** “Average passenger cruise duration fell 12.61%. This indicates a change in the passenger-trip mix. Its contribution to NCLH's yield and occupancy changes is unmeasured; it does not explain capacity growth by itself. CCL-specific mix effects should be assessed only against CCL's own deployment and guidance.” Preserve the numerical observation and the 60% registration; do not turn this into an automatic CRU-10 adjustment or another causal verdict. Because the stronger claim is in the correction packets, eventual owner correction should include those consumers. No sends were made by this reviewer.

## R2 — MEDIUM: the claimed complete correction-at-the-claim sweep remains incomplete

All four papers now assert that **every withdrawn claim is struck in place**. Later commits really did repair some headings, examples and conclusions. However, these unmarked assertions remain at the inspected snapshot:

| Current location, relative to `AGENTS/CRUISE/` | Residual claim | Why it matters |
|---|---|---|
| `domain/sources/2026-09-20_capacity-vs-occupancy-the-mechanism-measured.md:4` and `:42` | A measured cause/mechanism has been established | Contradicts the banner's causal narrowing |
| Same capacity paper `:34` | Occupancy swung 3.80pp | Keeps the level/difference mislabel the owner says it repaired |
| Same capacity paper `:40` | Exactly one lever before sailing: price | The original causal overclaim survives at its location |
| Same capacity paper `:77`, `:79`, `:89` | The 69.1M issuance is a larger, opposite confound; read the print as the net of both; second confound registered | Reintroduces the withdrawn guide-denominator error |
| `domain/sources/2026-09-20_capital-access-ladder-rcl-ccl-nclh.md:51` | NCLH has no bond-market access in the window | The ladder cell still says inability rather than observed non-issuance |
| Same capital paper `:84` and `:98` | Higher pricing proves no transmission by June 30; old/new coupons show a credit re-rating | Both inferences were rejected in the original review |
| `domain/sources/2026-09-20_the-discounting-event-found-at-primary.md:94` | Q3's yield line is the first place transmission can appear | Booking dates still become an identified revenue-impact window |
| Same discounting paper `:119` | The evidence argues for more caution on a CCL put because Truist raised Carnival on it | Directly conflicts with the withdrawal delivered to Will and TERRY |
| `TRADE.md:3` | CCL takes a second material adverse fact stronger than the buyback | The newly updated header retains the withdrawn conclusion; the superseded-AM label applies to the later historical block, not this header |

The capital paper's banner can qualify a reader who starts at the top. It does not satisfy its specific assertion that the retraction accompanies every claim. These examples distinguish incomplete propagation from ordinary historical preservation: clearly marked old passages, such as TRADE's superseded AM block, are not counted as live defects here.

**Bounded correction:** repair or explicitly mark the remaining claim units, retaining history where useful. Do not certify a complete sweep from the named examples alone. No additional ledger, check or instruction rule is proposed. The desk has already stated the applicable standard; implementation needs to match it.

## R3 — MEDIUM: the repaired CRU-09 example is not connected to its frozen registration reference

**Locations:** `workbook/PREDICTIONS.tsv:10`; live definition `domain/2026-09-19_DRAFT_FL-CRU-10_identifying_test.md:4`, `:79`, `:143`, `:151`.

The corrected denial example is right: denial-only fails the disclosure predicate; an independent affirmative attribution to another competitor may confirm it. The header's REGISTERED/NOT-REGISTERED contradiction and §9d's no-contradicted-state assertion were corrected. The owner records this as a Will-approved clarification, which this session does not treat as authority to edit anything.

But the CRU-09 TSV row is **byte-for-byte unchanged**. Its definition still points to the draft **at the commit that registered CRU-09**, namely `6639cbfa8`. That frozen version retains the wrong CONFIRMED example. The current file repeats the registration-commit reference in §9b. A grader following the declared frozen source, rather than the mutable live path, therefore misses the approved correction. Being before a later deadline does not automatically change an already named revision.

**Bounded correction:** attach an explicit, additive erratum reference at the registration's entry point: original definition `6639cbfa8` plus the specified approved clarification at `62795cc17`, identifying which example controls and stating that the predicate, probability and cutoffs are unchanged. Preserve the original record and the correction's authority; no re-registration or probability change is demanded by this review.

**Separate retained limitation:** §4c's supported row still has the alternative “or behaviour described that is uniquely Norwegian's” without expressly requiring affirmative attribution of the qualifying pressure. Identification alone remains insufficient. Close that literal ambiguity when recording the clarification; a statement identifying a unique promotion while denying its effect must not score SUPPORTED. This is the narrower remaining part of original F2, not a claim the denial-only worked-example repair failed.

## R4 — MEDIUM: the replacement chronology statement reverses the direction it can exclude

**Location:** discounting paper `:58`, the explicit replacement for the shared-source claim.

The new text says earlier publication rules out **WF/Stifel copying Truist**. It does the opposite: a July Truist note could be copied or used by later September notes. The date excludes the July publication being downstream of those particular later publications, not the later publications using the earlier one. Shared upstream sources remain possible either way. Elsewhere in the same paragraph the owner states the chronological direction correctly, leaving a live contradiction inside the repair.

**Bounded replacement:** “Truist's earlier publication cannot be downstream of those later WF/Stifel publications. It does not exclude the later houses using Truist or any of the houses sharing upstream inputs.” No original bank notes were newly obtained; this is a chronology correction, not a finding of actual copying.

## What this pass verified, and what remains separate

- Original F3/F4/F5/F8 corrections are present in the main STATUS/TRADE correction blocks and in named correction records; those substantive acknowledgments are supported. Residual source-paper propagation is R2.
- CRU-07, CRU-08 and CRU-09 TSV rows are unchanged between the earlier and current snapshots. CRU-10 changes only column 8, its Notes: it explicitly withdraws causal interpretation and the old rationale while preserving the original forecast, 60%, deadline and OPEN status. Its Notes also correctly say CRU-09 confirmation alone cannot establish Norwegian causation. Do not treat “60% still registered” as a claim that new evidence independently supports 60%; original forecast scoring and a current analytical belief are different objects.
- The source-promotion and Truist-withdrawal corrections do not establish an opposite trade conclusion. Leaving the desk's rows WATCH is documented; this review does not independently price the trade or establish that new information has exactly zero economic value.
- Cadence #8 now withdraws the port causal grading rule and limits counts to context. The “first physical window” and “adjudicates” framing still survives earlier in that row, despite its new caveat. The source paper has the same partial propagation; no complete current port-series search was undertaken here.
- CRUISE's TERRY/CARL correction packets exist and were read. Their new voyage-length assertions are covered by R1. This session did not assess TERRY's pricing work, CARL's consumer work, other CATO assignments, or live peer-message delivery.
- The NCLH funding model's previously retained timing/reserve/availability limitations were not re-modelled or closed. No assertion of exhaustive correction of every historical CRUISE surface is made.

**Delivery:** only this uniquely named report was authored in this follow-up; the prior report was preserved. Report remains uncommitted for coordinating CATO integration. CONTINUITY, owner files and other sessions' work were not edited. No Git mutations or peer sends. Suggested next action is a bounded owner correction of R1–R4 with exact grading references, not a new research or policy project.
