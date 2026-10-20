# BOND — owed work, missing work and gaps

**Audit:** October20,2026 12:53 ET, at Will's request. Repository evidence audit; no market refresh, research-rule amendment or repair performed. Read current SCRATCH, docket, prediction ledger, live monitors, grader code, L410 acceptance record and September28 scope ruling. This separates current evidence catch-up from unresolved legacy work. Inbox and WALTER lane are empty at inspection; BND32 is registered and not yet due.

## Immediate BOND backlog

| Priority | Item | What remains | Evidence / boundary |
|---|---|---|---|
| First, before next auction if practical | Auction-grader rounding alignment | `grade_auction.py` compares against unrounded computed indirect bars, while the governing registered bars are frozen to two decimals. Near a bar, the automated verdict can disagree. Repair comparison against the governing frozen bar and exercise equality/just-below/just-above cases; do not change the economic threshold. | Existing overdue October6 docket row; `monitors/grade_auction.py:638`; `monitors/AUCTION_HEALTH.md` October1 block. Manual frozen2dp grading remains the documented fallback for October21, not a completed repair. |
| Same repair closeout | Independent verification of L410 fixes | Acceptance record still says PARTIAL: initial reviewer found defects; author fixed and re-tested them, but no independent read of the fixed code is recorded. Selftest does not exercise the full command path; the old reviewer harness was a temporary scratch path. | `analysis/2026-10-01_L410_grade_auction_repair_ACCEPTANCE.md` Results; PROME docket repeats the same partial state. No later completed verification artifact located. This is an evidence-of-verification gap, not proof every prior grade was wrong. |
| Small output repair | Buyback packet template prints superseded base rate | The live module documents original-issue-date re-ranking and 1/53 historical fire rate, but its rendered packet stub still says `base rate 0/52`. Bring output text to the recorded metric/vintage; preserve historical maturity-rank results as history. | `monitors/buyback_f2.py:477` versus lines59–67. Already noted in October14 handoff; not fixed in the news catch-up. No change to the >50% rule or recorded operation verdicts follows. |
| Small documentation repair | Retired HYG-options clause remains live-looking in CDX monitor/tool text | VX-BND-06 already explicitly RETIRED the VIOLET skew-direction clause August23. Yet CDX monitor still lists it as an escalation trigger/request and the proxy script still tells readers to request it. Reconcile descriptions to existing retirement; do not commission an options accumulator. | `workbook/VX.tsv#VX-BND-06`; VIOLET August20 reply in processed inbox; `monitors/CDX_CASH_BASIS.md:96–101`; `monitors/cdx_proxy.py:86`. The old September20 “if no reply” reminder is obsolete: a reply existed and the clause was retired. |

These were not completed by refreshing today's data. My prior “caught up” statement referred to published evidence/inboxes, not a cleared legacy-repair backlog. All four mechanical checks passing did not establish that this backlog was empty.

## Missing research / coverage, with limits

| Item | Status and implication | Next appropriate step / owner |
|---|---|---|
| U.S. high-yield withdrawals/postponements and weekly market-access evidence | No comprehensive current census. Aggregate issuance and a few successful borrowers cannot establish that access is open for everyone; no search hits cannot mean zero withdrawals. “Pulled-deal cluster” remains qualitative, without a ruled numeric count/window. | Log verified issuer/instrument/event cases and hand-grade under existing rule. R3 noisy-query landing was declined October20. September28 ruling forbids signups/paid tracker for this gap and defers an SEC monitor behind a manual matching sample. No new spend or automatic threshold authorized. |
| Clean swap-spread measure | Small timestamp/convention/benchmark validation is still not located as completed. September28 sample was feasibility only: six dates tested, five produced rows; not a validated standing series. | Bounded validation can be considered on existing scope; full daily build remains DEFERRED by Will's September28 ruling. Do not describe the full monitor as currently approved/owed to build. |
| Duration-confounded cash-credit proxy / true derivatives basis | HYG/IEF is cash credit over a duration-mismatched Treasury denominator. It cannot establish true synthetic-versus-cash lead. A cleaner cash construction is a research possibility, not a completed or commissioned replacement. | Keep limitation on conclusions. True CDX source access retest December1 is dated; the retired VIOLET skew clause is not missing promised VIOLET delivery. |
| Funding and MBS blind spots | Private collateral, lender choices and offshore basis remain outside BOND's observable evidence; LIQUID owns funding. MBS weekly spread leg is watched, but active Fed MBS-sales and GSE-release execution legs are not watched by that tool. | Respect owner/source boundaries and event evidence; do not declare an all-channel clean bill or silently revive dormant scope. |
| Synchronized CPI-morning TIPS | Event-time nominal/real split remains unmeasured. Official daily decomposition is now current but is a different clock. | Withhold event-time causal conclusions; do not substitute daily changes as the missing intraday observation. |
| Older 30Y TIPS history | Auction monitor retains a September20 re-test to check history before2023. No completion artifact located in this bounded audit. Its dated superlative is already constrained to the observed sample. | Lower-priority source/history check, or explicitly retain the narrower historical claim; no wider superlative in the meantime. |

## Ungraded or deferred by design — not permission to improvise

- **September23 auction funding window:** explicitly UNGRADED under WQ291; current repo calm and LIQ07's different windows cannot grade it. A new window/letter needs its existing governance route. WQ157 pairing replacement study remains PARKED; it is not an overdue self-started build.
- **FHLB “advance-depletion” clause:** no defined quantitative instrument/threshold in that leg. November9 Q3 report is the existing checkpoint for the underlying capacity/base-rate work; do not manufacture a fire from a narrative.
- **US sovereign CDS:** declined build, December1 source retest. Auction-tail gates retired. Foreign holdings/TIC and primary repo ownership remain other desks' lanes.

## Scheduled work, not late

| When | BOND owes |
|---|---|
| October21,13:00ET | Grade20Y reopening against the frozen October15 bars; manual fallback unless repaired. |
| October22 | Grade5Y TIPS; refresh PMMS and FR2004 only after publication; freeze month-end nominal auction bars at announcement. |
| October26–29 | Grade nominal auction cluster; floating-rate note excluded. October27 buyback read; October28 forecast/benchmark-holder review; macro/ECB cross-section on issuer dates. |
| October28 publication, ceilingNovember3 | Resolve already-registered BND32 on its frozen contract. |
| November4 | Treasury refunding/buyback-policy F1/F3 assessment and scheduled F2 operation. |
| November9 /13 | FHLB Q3 checkpoint / Fed FX report (November13 remains cadence-based until issuer-confirmed). |

## Coordination / housekeeping

R3 owner answer is written/committed; PROME's actual config landing remains unverified. Native cross-session notification/consumption is unverified, not owner absence. Existing MEMORY rotation advisory and charter explicit-read size/perimeter issue remain housekeeping. Optional LEDGER_GLOB is absent, but the actual ledger nudge checked three live ledgers; absence did not mean the check was unavailable. Foreign VULCAN/WALTER changes defer pulling and were untouched.

**Recommendation:** prioritize grader alignment plus independent verification, then the two small output/documentation corrections. After the next auction duties, address the current HY market-access gap and bounded swap validation. No new Will ruling is requested by this audit; it identifies priorities and preserves existing deferrals.

## Repair follow-up — October20

Will authorized the four immediate repairs. Implementation and durable tests now saved; final independent review and heavy-closeout evidence are indexed at `../analysis/2026-10-20_monitor-repairs_ACCEPTANCE.md`. Original audit above remains the as-found record. The broader source-access, proxy-duration, event-time and governance gaps are not closed by these repairs.
