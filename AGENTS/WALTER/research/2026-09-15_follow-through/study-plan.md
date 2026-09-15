# September 30 INFO-backlog review — analysis plan

Prepared September 15 before prospective outcome measurement. This advances the existing DOCKET L334 obligation; no new threshold, launch or trading authority. September 30 remains the review date, not a promised statistically conclusive result.

## Data and unit

Use `AGENTS/WALTER/routed/delivery_log.tsv`, `routed/route_log.tsv`, BOARD action/info declarations, recipient disposition artifacts and `registry/DOORBELL_LOG.tsv`. DOCKET's `state/delivery_log.tsv` pointer is broken; this plan records the correct path without editing PROME state. Baseline must follow `d398fb2f5`. Freeze September 15 local ledger bytes and hashes; local observations are not origin-proof or owner consumption. Existing retrospective receipt and minute-order corrections remain provenance, not exact reconstructed delivery times.

Unit: recipient-day for eligible INFO recipients with an observable delivery lane and disposition instrument. Separate exempt BOARD-pull desks and desks lacking receipts; do not impute zero exposure or zero outcomes. Mixed ACTION/INFO signals use the recipient-specific role. Report ACTION load separately as a possible confounder. No inference from an unread INFO queue to an ACTION obligation.

## Exposure, outcome and follow-up

At baseline, report delivered INFO count, dated age distribution and counts with unknown timestamp/receipt/origin status. Uncommitted handoffs are not delivered exposure. Active inbox position is an exposure proxy, not proven unreadness. Record known acknowledged/deferred and processed states separately. Use an age interval where only a calendar date is supported; exclude ambiguous transport times from exact latency calculations.

Prospective follow-up: September 16–29, review September 30. Outcome requires an exact later artifact documenting a correction, stale-figure dispatch or reconciliation related to the recipient and underlying information. Record event date, first available artifact date, signal linkage and an independent adjudication. Count distinct events, not repeated mentions; unknown linkage stays unclassified. Historical examples are descriptive and separate from this prospective arm. Do not claim this is blind preregistration: September 15 owner evidence was already inspected.

Compare exposure on day t with outcomes during the next seven calendar days; primary complete-window cohort therefore ends September 22. Later exposure windows are right-censored at September 29. An owner with no observable follow-up is missing/censored, not a zero. Repeated desk-days and overlapping windows are dependent; report per-desk event counts and use desk-level resampling only if sample supports it.

## Interpretation and executable checkpoint

Before fitting anything, publish eligible/excluded desks, complete windows, missingness and event counts. Show descriptive event rates by prespecified exposure groups (0, 1–10, >10 observable INFO items), including exact denominators; collapse no groups after seeing outcomes. Report uncertainty and sensitivity to receipt quality and age ambiguity. Estimate detectable effects using actual eligible sample and event counts at review; do not promise power in advance. If too sparse, return descriptive/insufficient evidence rather than an unstable predictive model. Association would not establish causation: activity, desk scope, signal volume and receipt instrumentation are confounders.

A null result permits only a bounded monitoring decision for observed desks, window and detectable effect; it does not establish that unread INFO is costless. Any proposed operational bar goes to Will. Next work: collect dated snapshots as sessions run; adjudicate outcomes independently before September 30 interpretation.
