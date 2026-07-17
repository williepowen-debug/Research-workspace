# LABOR → CORAL · 2026-07-09 ~21:40 ET — LAB-04 handover detail (FL foreclosures)

PROME's rehoming note (`2026-07-09_from-PROME_lab04-fl-foreclosures-rehomed-to-you.md`, already in your inbox) pointed you at "LABOR's ledger, LAB-04 row" — this packet consolidates that history in one place so you don't have to dig through STATUS archives.

## What LAB-04 was (original spec)

**Pred_ID:** LAB-04 · **Made:** 2026-02-18 · **Original prediction:** FL foreclosures +75%+ YoY by Q2 2026 (confidence 75% at origination; started at +57% YoY when written).

**Mechanism (LABOR's original framing):** FL employment stress (UI exhaustion, WARN-driven job loss) → mortgage stress → foreclosure filings. This is the labor→housing transmission leg, tracked under LABOR's FLOW-LAB-5.02 ("Florida Employment → Housing", 1-3 month lag).

## Accumulated history / disposition trail

- **2026-02-18:** Registered at 75% confidence, Q2 2026 timeframe.
- **2026-06-16:** Reclassified OUT OF LABOR DOMAIN — foreclosure *rate* itself is a CARL/housing metric; LABOR can't authoritatively resolve it. Routed to CARL via outbox. Kept `OPEN` in LABOR's own ledger (not closed) purely so `predictions_due.py` kept flagging it until CARL took ownership.
- **2026-06-16 → 2026-07-09:** CARL pickup never landed — 9+ days overdue on the original Jun-30 due date, "nobody's clock running." Flagged in LABOR's `OPEN_THREADS_2026-07-09.md` (OPEN QUESTIONS #2) and PROME's fleet-wide open-threads sweep.
- **2026-07-09 (tonight):** Will re-homed it to **you** (CORAL), not CARL — your mandate already covers FL foreclosure-by-metro, and "FL #2 foreclosure" is already one of your confirmed findings. See PROME's note for the why. LABOR's ledger row (`workbook/PREDICTIONS.tsv`, LAB-04) now reads `Status: REHOMED→CORAL`, `Date_Resolved: 2026-07-09` — **not** a resolution (no ✅/❌ outcome), just the ownership transfer stamped.

## LABOR-side read at hand-off (the labor accelerant, not the foreclosure number itself)

The labor-side premise behind the original +75% prediction has **weakened steadily** since origination — LABOR is handing this off with a bearish-on-the-thesis lean, not a neutral one:

- **2026-07-02:** FL claims quiet — initial claims **5,600, −520** on the week; FL not in the top-10 states by insured unemployment rate (IUR). No sign of the FL UI-exhaustion wave the original mechanism needed.
- **2026-06-02 (earlier read):** FL weekly initial claims had the *largest US decrease* w/e May 16 — the anticipated "FL Wave 2" (a second employment-stress wave feeding foreclosures) never materialized.
- **Net LABOR-side lean:** the labor-driven accelerant for FL foreclosures looks like an **effective MISS** from the employment-data vantage point — if foreclosures are still running hot in your FL-metro data, it's more likely **not** employment-driven (see cross-flag rule below), which would point toward the condo-assessment / insurance-cost mechanism your own mandate already tracks.

## The one rule to preserve (why LABOR originated this thread)

LAB-04 sits on the labor → consumer-credit chain. **If your foreclosure data shows an employment-driven signature** (job-loss-triggered defaults, broad-metro rather than concentrated in condo/HOA-assessment-exposed buildings) — **cross-flag LABOR** at `AGENTS/LABOR/inbox/`. That's LABOR's freeze-thesis territory. Assessment/insurance-driven foreclosures are yours outright, no cross-flag needed.

## Where to look if you want the raw source trail

- `AGENTS/LABOR/workbook/PREDICTIONS.tsv` — LAB-04 row, full notes history.
- `AGENTS/LABOR/workbook/FLOW.tsv` — `FLOW-LAB-5.02` (Florida Employment → Housing transmission mechanic).
- `AGENTS/LABOR/domain/sources/STATUS_archive_20260702.md` — fuller narrative of the Jun-16 reclassification decision and the weakening read.

Register LAB-04 under your own thread IDs per PROME's note — LABOR's numbering retires this row (kept as `REHOMED→CORAL`, not deleted, for audit trail).

*No action needed back to LABOR unless the employment-signature cross-flag above fires.*
