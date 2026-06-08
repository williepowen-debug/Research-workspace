# MARCO Expected Signals

**Purpose:** Track signals that SHOULD appear if thesis is correct but haven't yet. **Absence of an expected signal is information** — it flags a timing error, a blocked transmission, or a thesis flaw. This is the complement to `thesis/PREDICTIONS.tsv`: predictions assert what will happen; expected-signals assert what we'd *see* if the mechanism is live.

**Last refreshed:** 2026-06-08 (session 12 — Pull Session 1: ES-01 World-Cup-masked, ES-04/ES-07 trending DID_NOT_APPEAR at Q2 deadline)

---

## Active Expected Signals

| ES-ID | Signal | Expected By | Status | Current read (2026-05-31) |
|-------|--------|-------------|--------|---------------------------|
| ES-MARCO-01 | FL hospitality employment decline | Q2 2026 | WATCHING — **WORLD-CUP-MASKED** | **(6/8) May NFP +172K; L&H +70K = ~5× the 14K/mo trailing avg, food svcs +48K — BLS attributes to "hiring needed for the World Cup."** A labor-side event-mask (same logic as MIA pax): a Jun/Jul hospitality beat is event-driven, NOT a tourism-stress reversal. Signal is now MASKED, not absent — **tell is no *sustained* hospitality strength after Jul 19.** No clean FL-state hospitality cut yet (state release lags). KB-MARCO-WFD-NFP-01. |
| ES-MARCO-04 | TX border city revenue decline >10% | Q2 2026 | **COUNTER-SIGNAL → likely DID_NOT_APPEAR** | **(6/8) Revenue is GROWING, not declining:** TX Comptroller Apr 2026 allocations — El Paso County 2025 ~+2% vs 2024; most RGV cities grew (≈dozen double-digit). The >10% municipal-revenue decline is NOT materializing at the Q2 deadline. Cross-border-shopping erosion is **slow-structural** (Dallas Fed swe2602 — Mexican residents favoring local retail), NOT an acute cliff. Shopper-SHARE collapse (VX-BDR-03) intact; revenue terminus offset by local spend + inflation. **Mechanism intact, threshold not breached.** Formally resolve DID_NOT_APPEAR at Jun-30 close. KB-MARCO-TX-04. |
| ES-MARCO-05 | CA ag produce prices spike >10% YoY | Q2 2026 | NEAR | CPI fresh F&V **+6.1% YoY Apr** (veg +3.1% MoM) — appearing, trajectory toward 10% but not breached. If holds to Jun without hitting 10%, push deadline to H2 (aligns w/ Pred MAR-14). |
| ES-MARCO-06 | FL domestic migration turns negative | Dec 2026 | WATCHING | Last print 22,517 (93% collapse), Miami −2.0%. Annual Census — no new data until late 2026. On track for the Dec test. |
| ES-MARCO-07 | Vegas visitor decline continues >5% | Q2 2026 | **NOT BREACHED → likely DID_NOT_APPEAR** | **(6/8) LVCVA Apr 2026: total visitor volume 3.28M, −1.8% YoY** — convention +3.2%, occ 83.1%, ADR record $190.41. Bodies-down/dollars-up substitution holds, but −1.8% is well short of the >5% threshold on the total-visitor metric. (Distinct from the harsher LAS *airport-pax* −7.1% in the dashboard.) Demand soft, not collapsing — convention base is the floor. Formally resolve DID_NOT_APPEAR at Jun-30 close unless May worsens sharply. KB-MARCO-NV-02. |
| ES-MARCO-08 | **Produce CPI decouples from pump prices** (fresh F&V CPI stays elevated while retail gas/diesel falls) | **Jun 10 + Jul CPI** | WATCHING | **The v2.1 discriminating test for produce attribution.** Diesel/freight was a transient co-driver of the Apr +6.1% spike; crude −19% on the month, pump relief lands May 31–Jun 14 (BRENT). **If fresh F&V CPI holds ≳+5% YoY into June/July while pump prices fall** → transient driver exiting, residual (labor + freeze + tariff) re-weighted UP → labor partially rehabilitated. **If F&V softens in step with diesel** → freight carried more of the spike than credited → labor demoted further. Caveat: distillate structurally tight (−11% vs 5-yr), so freight relief is partial/lagged, not 1:1. Resolves the Channel-1 thermometer question (`thesis/THESIS.md` v2.1). |
| ES-MARCO-09 | **World Cup does NOT reverse the inbound decline** (NTTO Jun+Jul 2026 combined overseas stays ≥−20% vs 2019 *during* the event) | **Aug–Sep 2026** | WATCHING — advance signals lean FAIL | **The v2.4 absence-is-information test for Channel 2.** CY2025 = first US inbound decline in 20yr (−5.5%, 68.3M); the **FIFA World Cup (Jun 11–Jul 19, US co-host)** is the catalyst that *should* pull inbound back toward 2019. **Thresholds locked (TOURISM pull 6/2, KB-WC-05): test PASSES / thesis weakens if NTTO Jun+Jul combined overseas ≥5.5M AND ≥−10% vs 2019; FAILS / thesis hardens if ≥−20% vs 2019 despite the WC.** Advance signals already lean FAIL: **AHLA Apr 30 — 80% of host-city hoteliers BELOW WC forecasts** (Miami/Atlanta only exceptions; Miami match-night occ 24–31%, ADR flat); national projection 1.24M intl / 742K incremental (Tourism Economics) vs a −26.5% vs-2019 hole. **NB: MIA pax may print +YoY in Jun/Jul on the WC — that's an event-mask, NOT recovery** (the tell is the absence of *sustained* MIA recovery after Jul 19). Docket: Jun 11–Jul 19 + ~Aug 15 NTTO. Detail: `sub_agents/TOURISM` thread 3 + KB-WC-01..07. |

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
