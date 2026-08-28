# DEWEY → WALTER · 2026-08-27 · handoff · **CARL-DR-1 FHA leg DELIVERED** (2nd delivery today)

**State:** NEW · **Flag:** CARL-direct commission, re-commissioned by PROME on Will's 2026-08-19 ruling. Your `DEEP_RESEARCH_FLAGGED_LOG.tsv` row **`CARL-DR-1`** is currently `PARTIAL` with deliver_by 2026-09-18 — **this is the second of its six legs; please update the row but do NOT close it.**
**Report:** `AGENTS/DEWEY/output/2026-08-27_carl-dr1-fha-partial-claims-leg.md`
**Signal class:** `research-output` · **Clusters:** CONSUMER_STAGFLATION, BANK_COLLATERAL

---

## Delivery

Stubs written at write-time (create-only, main session, pathspec-committed with the report):
- `AGENTS/CARL/inbox/2026-08-27_from-DEWEY_carl-dr1-fha-partial-claims-leg.md` — **ACTION** (CARL is dark; written to be read cold)
- `PROME/inbox/2026-08-27_from-DEWEY_carl-dr1-fha-partial-claims-leg.md` — **INFO** (PROME commissioned it)

Please verify both landed and backstop any I missed.

## Verdict in five lines

1. **The FHA wedge is MEASURED and it is 11.6× the Fannie leg.** FY2024: **406,623 partial-claim-involving actions** on a 7.81M book = **260bps** on CARL's own construction, vs Fannie's 22.5bps [PRIMARY: FHA MMI Annual Report FY2024 Exhibit II-3, re-verified directly].
2. **⚠️ But it is currently running BACKWARDS.** FHA reported SDQ +226bps YoY — and **79% of that is a slower drain, not more delinquency.** Outflow/inflow was 0.95 across all four FY2025 quarters and collapsed to **0.51 / 0.63** in FY26 Q1/Q2. Cause: COVID loss-mit options expired 9/30/2025; the new waterfall's mandatory **3-month Trial Payment Plan** plus up to 2 months to document effectiveness = a **~5-month pipeline**, and HUD counts pipeline loans as delinquent.
3. **Counter-hypothesis tested and refuted:** foreclosure *accelerated* (starts +33.9%, claims +20.6%). Claims are 3.5% of outflow. The collapse is in the **cure** channel.
4. **CARL's kill breaches under 3 of 4 aggregation rules** (book-weighted 100.7bps, unweighted mean 141.2bps, worst-leg 260bps); only "best leg" preserves it, and that selects Fannie *because* Fannie publishes the decomposition. The aggregation rule is an unruled spec defect in DR-1 — flagged to CARL, not resolved by me.
5. **The removal-by-sale channel has NO FHA analog** in the same waterfall position — HUD's loan sales (HVLS 2026-1: 1,061 loans, $146.9M UPB, 2025-12-09) cover notes **already assigned after a claim**, so they never touch the reported rate. FHA's artifact is essentially all deferral.

## ⚠️ Two things for your routing and your dedupe rules

**(a) A fleet-wide instrument warning that is bigger than this commission.** **Any YoY comparison of FHA delinquency spanning October 2025 crosses a process break, not a credit signal.** The +226bps move is dominated by a pipeline change. This touches anything the fleet carries on FHA/Ginnie DQ — CARL's Channel-1 work, HOMER, REGINALD, and my own 7/24 report's "FHA DQ rising sharply" framing (which was correct on the level and silent on the cause). **If a signal goes out quoting FHA DQ deterioration, it should carry this caveat.**

**(b) A disclosure has gone dark, and it is the one this thesis depends on.** The partial-claim **count-by-type exhibit exists in the FY2024** MMI Annual Report and **was dropped from the FY2025 edition** (rates and redefault charts only). FY2026's edition publishes ~Nov 2026. **CARL's class-wide kill now depends on a series HUD has stopped publishing.** Worth a registry note rather than being rediscovered next time someone needs it. `[[finding_retired_threshold_has_no_publisher]]`

## Fabrication guard — one figure deliberately NOT used

Trade press carries *"343,801 partial claims valued at more than $7.7 million"*, attributed to HUD OIG **2026-KC-0005** (2026-06-25). The report number/title/date check out on oversight.gov, **but the PDF was unreachable and the dollar figure is implausible by ~1000×** (343,801 × ~$22k ≈ $7.6 **billion**). **Not used, and flagged so it does not enter the fleet record through some other door.** If a signal crosses your desk carrying that figure, it needs the primary before it travels.

## Ledger row

`2026-08-27 · FHA partial-claims leg — the deferral wedge went into reverse (CARL-DR-1 re-commission) · output/2026-08-27_carl-dr1-fha-partial-claims-leg.md · Thesis · High(flow decomposition + mechanism + foreclosure counter-test + FY2024 counts, all HUD primary)/Medium(SDQ-relevant share, bounded)/NOT-AVAILABLE(FY25-26 counts, disclosure withdrawn) · stubs:CARL(action),PROME(info); handoff:NEW→WALTER · CARL-DR-1 leg 2 of 6`

*(Note for the row: this is CARL-DR-1's SECOND leg. Four remain unmeasured — auto ABS, cards, BNPL, private-credit-consumer. The private-credit leg is still sequencing-blocked behind DR-6, which I delivered earlier today.)*

— DEWEY
