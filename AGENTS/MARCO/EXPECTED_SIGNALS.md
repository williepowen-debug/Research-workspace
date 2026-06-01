# MARCO Expected Signals

**Purpose:** Track signals that SHOULD appear if thesis is correct but haven't yet. **Absence of an expected signal is information** — it flags a timing error, a blocked transmission, or a thesis flaw. This is the complement to `thesis/PREDICTIONS.tsv`: predictions assert what will happen; expected-signals assert what we'd *see* if the mechanism is live.

**Last refreshed:** 2026-05-31 (session 8 — added ES-MARCO-08 produce-vs-pump decoupling test)

---

## Active Expected Signals

| ES-ID | Signal | Expected By | Status | Current read (2026-05-31) |
|-------|--------|-------------|--------|---------------------------|
| ES-MARCO-01 | FL hospitality employment decline | Q2 2026 | WATCHING | No clean FL leisure/hospitality decline yet; NFP rebounded +115K Apr. Tourism stress not (yet) transmitting to jobs — consistent with softened tourism vector. |
| ES-MARCO-04 | TX border city revenue decline >10% | Q2 2026 | WATCHING | Nogales residential −43.2%, but no clean *municipal revenue* print. Sales-tax data lag. Deadline approaching (Jun). |
| ES-MARCO-05 | CA ag produce prices spike >10% YoY | Q2 2026 | NEAR | CPI fresh F&V **+6.1% YoY Apr** (veg +3.1% MoM) — appearing, trajectory toward 10% but not breached. If holds to Jun without hitting 10%, push deadline to H2 (aligns w/ Pred MAR-14). |
| ES-MARCO-06 | FL domestic migration turns negative | Dec 2026 | WATCHING | Last print 22,517 (93% collapse), Miami −2.0%. Annual Census — no new data until late 2026. On track for the Dec test. |
| ES-MARCO-07 | Vegas visitor decline continues >5% | Q2 2026 | WATCHING | No fresh LVCVA print pulled this session. Canadian air −8.1% supports, but unconfirmed for Vegas specifically. |
| ES-MARCO-08 | **Produce CPI decouples from pump prices** (fresh F&V CPI stays elevated while retail gas/diesel falls) | **Jun 10 + Jul CPI** | WATCHING | **The v2.1 discriminating test for produce attribution.** Diesel/freight was a transient co-driver of the Apr +6.1% spike; crude −19% on the month, pump relief lands May 31–Jun 14 (BRENT). **If fresh F&V CPI holds ≳+5% YoY into June/July while pump prices fall** → transient driver exiting, residual (labor + freeze + tariff) re-weighted UP → labor partially rehabilitated. **If F&V softens in step with diesel** → freight carried more of the spike than credited → labor demoted further. Caveat: distillate structurally tight (−11% vs 5-yr), so freight relief is partial/lagged, not 1:1. Resolves the Channel-1 thermometer question (`thesis/THESIS.md` v2.1). |

---

## Resolved Expected Signals

| ES-ID | Signal | Expected By | Outcome | Date | Notes |
|-------|--------|-------------|---------|------|-------|
| ES-MARCO-03 | FL condo inventory exceeds 9 months | Q2 2026 | **APPEARED** | 2026-04-17 | 9.1mo Mar 2026 (FL Realtors) — breached before Q2 midpoint. NB: reverted to 8.9mo Apr (one-month breach, now tightening). Mechanism appeared but did not extend → see thesis v2.0 "FL cooling" reframe. |
| ES-MARCO-02 | Canadian snowbird bookings down >20% | Q1 2026 | **PARTIAL** | 2026-05-11 | Capacity side confirmed (Air Transat exited all 3 Quebec-FL routes; WestJet summer transborder −32% ASM). But Apr headline crossings flipped +1.4% YoY; air channel only −8.1%. The >20% magnitude did NOT appear on the demand side — base-effect moderation. Boycott softened on auto/headline, persists on air. |

---

## How to Use

1. When the thesis predicts something, add to Active with an expected timeframe.
2. Check each session — has it appeared? Update the current-read column with a date.
3. When the deadline passes: move to Resolved as APPEARED / DID_NOT_APPEAR / PARTIAL and assess implications.
4. Absence past deadline may indicate: timing error, blocked transmission, or thesis flaw — feed that read into `thesis/CHANGELOG.md`.

---

*Review during reconciliation/closeout sessions. Complements `thesis/PREDICTIONS.tsv`.*
