# FASTOW MEMORY

State file for the docket-steward sub-agent. Spec is in [`FASTOW.md`](FASTOW.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** FASTOW writes this file directly at end-of-run (consistent with FASTOW's other write privileges — full-edit mode by default, busy-work-only). BRENT may pre-edit between runs to seed `## NEXT RUN HINTS`, `## PENDING`, or `## CALIBRATION`.

**Spawn order:** FASTOW reads `FASTOW.md` first (spec), then `FASTOW_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by FASTOW at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(no prior run — this is FASTOW's pre-Run-1 initial state)*

---

## LAST RUN

*(no runs yet — FASTOW Run 1 will append the first entry here)*

---

## PENDING

*Items FASTOW has surfaced for BRENT to act on. FASTOW adds; BRENT clears when resolved. Do NOT auto-clear from FASTOW — BRENT owns the close.*

*(none — pre-Run-1 state)*

---

## STANDING MONITORS

*Recurring watches FASTOW should check every run (in addition to baseline-audit triggers). Seed list — extend as patterns emerge.*

- **Modeled-date rows** — every run, check CATALYSTS.tsv rows with `date_class=modeled` against current STATUS storage section. Currently active: SPR 350M floor (Jun 10), Cushing 20M floor (Jul 1). Update dates if STATUS projection has shifted.
- **STATUS ↔ TSV event-SET divergence** — every run, verify STATUS § CATALYST CALENDAR section matches TSV event set. Surface divergence as ESCALATION; don't edit STATUS.
- **1-week retention on `— FIRED` rows** — every run, prune any `— FIRED` row whose date is >7 days past today.

---

## CALIBRATION

*BRENT-owned section. FASTOW reads but never writes here. Records which release classes BRENT has declined to track under the current thesis lens — prevents baseline-audit from re-proposing the same classes every month.*

### Declined release classes

*(none — initial state; BRENT will add as the thesis lens tightens / loosens)*

**Format when added:**
```
- {class name} — declined YYYY-MM-DD. Reason: {one-line — what about the current thesis lens makes this class out-of-scope}. Re-evaluate if: {condition that would bring it back in scope}.
```

---

## NEXT RUN HINTS

*FASTOW writes at end-of-run; BRENT may pre-edit between runs. What the next-spawn-of-FASTOW should know that isn't obvious from the read-set.*

- **Run 1 is the first FASTOW run, EVER.** Monthly baseline-audit trigger fires by definition (no prior run = no "first run of this calendar month" precedent). Execute § BASELINE AUDIT full sweep against all 10 release classes in the table. Expect this to find existing rows already in TSV (Jun 5 COT, Jun 5 BH, Jun 7 OPEC+, Jun 10 EIA, Jun 11 STEO, etc.) — the audit value is identifying any release class that's been silently absent (e.g., IEA OMR, OPEC MOMR, EIA STEO for July if it's been scheduled).
- **Prune candidate:** Jun 3 EIA WPSR row tagged `— FIRED` is now 1 day old as of Run 1 spawn (Jun 4). Under the 1-week retention rule, it should NOT be pruned this run — keep until Jun 10. Surface in LAST RUN entry as "Jun 3 EIA FIRED row retained (1d old, eligible Jun 10)".
- **Modeled-date check on Run 1:** SPR 350M floor row currently dated 2026-06-10 (per STATUS Jun 3 PM read). Verify against latest EIA WPSR Jun 3 synthesis at `AGENTS/BRENT/demand_destruction/data/eia_2026-06-03.md` — if STATUS-projection has shifted since Run 1 spawn, revise. Same check for Cushing 20M floor (currently 2026-07-01).
- **Source URLs to fetch this run** (for baseline audit):
  - EIA WPSR schedule: `eia.gov/petroleum/supply/weekly/`
  - CFTC COT schedule: `cftc.gov/MarketReports/CommitmentsofTraders/index.htm`
  - Baker Hughes: `bakerhughes.com/rig-count`
  - EIA STEO schedule: `eia.gov/outlooks/steo/`
  - OPEC MOMR: `opec.org/opec_web/en/publications/202.htm`
  - IEA OMR: `iea.org/topics/oil-market-report`
  - OPEC+ meeting calendar: `opec.org/opec_web/en/press_room/4787.htm`
- **Cost budget for Run 1:** monthly-audit estimate is 5-8 min. Run 1 may run longer (first time fetching all sources, building source-cache mental model). Budget 10-12 min; flag if longer.
