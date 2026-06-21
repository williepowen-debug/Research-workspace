---
signal_id: SIG-W-20260621-005
dispatched: 2026-06-21T22:18:00Z
origin: Will Telegram intake (2nd 6-image batch, msgs 2547-2552, 2026-06-21 ~22:38 UTC)
source:
  - Steve Hanke @steve_hanke (X) citing NPR — "45% of US adults not taking a summer vacation; cost the top reason for 49%"
  - First Squawk @FirstSquawk (X, 2026-06-20 11:08 PM) — "Americans face surging homeownership costs beyond mortgages as taxes, insurance and maintenance soar"
  - Flightradar24 — commercial flights tracked per day (2022-2026 overlay)
signal_type: thesis-frame
domain: CONSUMER
cluster: CONSUMER_STAGFLATION
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: CARL
info: [MARCO, CRUISE, RED]
confidence: 0.70
verify_verdict: SKIP-VERIFY (NPR-cited survey + named-source flight data + headline; directional, single-survey caveat — see framing)
verify_method: BOARD-grep dedup (extends CONSUMER_STAGFLATION affordability thread; SIG-007 6/19 bankruptcy / cost-push prior); survey + chart, no verify-spawn
---

# Consumer discretionary K-shape — vacation cancellations + non-mortgage homeownership cost-push, WHILE air travel holds up (two-way)

## Substance (SKIP-VERIFY 0.70 — directional, two-sided)

Three same-batch consumer data points that resolve into a **K-shape**, not a clean demand-collapse:

- **Bottom-half squeezed (the bear leg):** Steve Hanke citing NPR — **45% of US adults are not taking a summer vacation, and 49% cite cost as the top reason.** Discretionary-travel pullback driven explicitly by affordability.
- **Cost-push driver:** First Squawk (6/20) — **non-mortgage homeownership costs (property taxes, insurance, maintenance) are surging**, pushing total cost-of-ownership well beyond the mortgage. Headline-level (teaser, no fresh numbers) but the channel is real and already in BOARD (CORAL FL insurance/property-tax + the 6/19 SIG-007 cost-push thread).
- **Top-half holding up (the counter leg — present it honestly):** Flightradar24 — **global commercial flights per day in 2026 are tracking in line with 2024-2025** (near the top of the multi-year range, well above 2022-23). Air travel demand is NOT collapsing globally. The squeezed 45% dropping out coexists with robust flying by those who can still afford it = textbook K-shape (and partly a global-vs-US-survey mismatch — the flights series is global, the vacation survey is US adults).

## Why it matters — mediates demand-destruction vs resilience (cluster_mediating)

**CARL (action) — consumer stress / K-shape:** this is CARL's core channel — the affordability squeeze biting the bottom cohort (vacation cancellations, cost-of-ownership) while the top cohort's consumption (air travel) holds. Pairs with CARL's existing K-shape spine (LEN guide cut, UMich expectations, energy-disinflation-reversing). The honest read: **the survey + cost-push are real bear inputs, but the flights data is a genuine counter** — don't route this as "consumer rolling over"; route it as the K-shape widening (bottom-half discretionary capitulation, top-half intact). Single-survey caveat: the NPR vacation stat needs a 2nd corroborating print before it's load-bearing (per single-month-sub-component skepticism).

**MARCO (info) — travel/tourism:** the flights-holding-up datum is MARCO-relevant (World-Cup-masks-on-pax dynamic; global travel robust vs US-consumer-survey softness). Reconcile the global-flights resilience against any US-specific tourism softness MARCO tracks — don't let the global series paper over a US pullback or vice-versa.

**CRUISE (info):** discretionary-travel affordability pullback is the CRUISE demand-destruction channel (45% skipping vacations on cost) — but the air-travel counter says premium/committed leisure travel persists; relevant to the CCL/RCL/NCLH demand split (mass-market vs premium).

**RED (info):** steelman the bull — flights at/near record + a single NPR survey is thin for a "consumer cracking" call; the vacation stat may reflect a long-running affordability gripe, not a fresh deterioration. Calibration input for CONSUMER_STAGFLATION weighting; the K-shape framing (not collapse) is the disciplined read.

## Source framing

NPR-cited survey via a pundit (Hanke) + a teaser headline (First Squawk) + a named flight-data chart. Numbers are plausible but lightly-sourced; route as **directional K-shape, not a hard print.** The load-bearing structure is the *combination* (squeeze + cost-push + resilient top) more than any single stat.

## AIGs / cross-refs

- BOARD: SIG-W-20260619-007 (S-FL bankruptcy uptick / cost-push — CONSUMER_STAGFLATION), SIG-W-20260619-008 (S-FL distress deep-research — consumer deteriorating, K-shape), CARL consumer K-shape thread
- CARL STATUS 6/16 (CRITICAL 52/70; K-shape biting; energy-disinflation reversing)

## Provenance

- Intake: Telegram 2nd 6-image batch msgs 2547-2552, 2026-06-21 ~22:38 UTC
- Pipeline: BOARD-grep (extends CONSUMER_STAGFLATION affordability thread, distinct from SIG-007 bankruptcy) + Phase 1b same-theme combine (3 origins, consumer-affordability K-shape) → SKIP-VERIFY (survey + chart; directional, flagged) → dispatch
