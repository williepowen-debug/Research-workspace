---
signal_id: SIG-W-20260704-006
dispatched: 2026-07-04T16:30:00Z
origin: Will-Telegram image batch 2026-07-04 (img 2, The Kobeissi Letter @KobeissiLetter); verified via WALTER verify-research sub-agent vs BLS JOLTS
source: "The Kobeissi Letter (@KobeissiLetter): US construction hiring RATE fell -0.3pp in May 2026 to 3.5% = lowest since JOLTS began 2000; down -1.1pp since January; vs 2008 GFC low 4.5% / 2020 pandemic low 3.7%; 295,000 construction hires in May = 3rd-lowest monthly total since 2020. Chart FRED 'Hires: Construction'."
signal_type: threshold-crossed
domain: LABOR_MARKET
cluster: CONSUMER_STAGFLATION
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
event_window: closed
precedence: ROUTINE
to: [LABOR]
info: [CARL, CORAL, RED]
confidence: 0.85
verify_verdict: CONFIRMED-with-CORRECTED-FRAMING 0.85 (WALTER verify sub-agent vs BLS JOLTS API primary, series JTS230000000000000HIR/HIL). EXACT: 3.5% rate (Apr 3.8→May 3.5, −0.3pp), 295K May hires. CORRECTED-FRAMING (2): (1) "−1.1pp since January" is actually **−0.9pp** (Jan 4.4→May 3.5; the 1.1 likely used a pre-revision Jan); (2) "lowest since 2000" is a **TIE with Feb 2026** (also 3.5) — a co-record-low set in Feb and matched in May, not a fresh solo record (floored at 3.5% twice in 4 months). "3rd-lowest since 2020" consistent (only Oct-25 294 + Feb-26 294 lower). 2008/2020 comps (4.5%/3.7%) reasonable, not independently re-pulled.
verify_method: WALTER verify-research sub-agent (BLS Public Data API v1 primary; FRED Akamai-blocked; corroboration ZipRecruiter Research / Haver / Roofing Contractor).
routing_note: >
  US construction hiring at a series-record-low → LABOR (labor-market owner). Kobeissi's headline figures are EXACT vs BLS JOLTS (3.5% rate, −0.3pp MoM, 295K hires) — this is a real, primary-confirmed construction-labor-weakness datapoint, decelerating hard through 2026. Carry the two precision overlays: (1) "−1.1pp since Jan" is really −0.9pp; (2) "lowest since 2000" is a TIE with Feb-26, not a solo record (3.5% is a floor hit twice in 4 months, not a fresh break lower). **Two-sided composition nuance (load-bearing):** the SAME JOLTS release showed construction JOB OPENINGS rising to a 10-month high (~298K) — concentrated in data-center/electrician demand. So it's hires-at-record-low + openings-at-10mo-high = a COMPOSITION/mismatch story (skills/wage/project-type), not a clean demand collapse. **Cross-signal:** that data-center/electrician openings concentration ties to today's PJM grid-emergency signal (SIG-704-007) — the AI-data-center buildout is simultaneously straining the grid AND absorbing the construction labor that IS being hired, even as broad construction hiring floors. LABOR (action): fold into the freeze-deepening matrix; is construction the sharpest sector cut, and how much is the openings-up/hires-down split composition vs demand? CARL (info): construction-labor weakness = a consumer/income-transmission input. CORAL (info): construction hiring is a FL/housing-construction leading input (condo/homebuilding). RED (info): the precision overlays + the openings-up counter keep it two-sided. cluster CONSUMER_STAGFLATION.
---

# US construction hiring rate at a series-record-low 3.5% (ties Feb-26) — real, but with a precision overlay + an openings-up counter (Kobeissi, BLS-verified)

From Will's 2026-07-04 image batch (img 2, The Kobeissi Letter); **verified** vs BLS JOLTS primary.

## What's confirmed (EXACT vs BLS JOLTS)
- Construction **hiring rate fell −0.3pp in May to 3.5%** (Apr 3.8 → May 3.5).
- **295,000 construction hires** in May = 3rd-lowest monthly total since 2020 (only Oct-25 294 + Feb-26 294 lower).
- 3.5% is a **series-record low** (JOLTS since 2000).

## Two precision overlays (CORRECTED-FRAMING)
1. **"−1.1pp since January" is really −0.9pp** (Jan 4.4 → May 3.5; Kobeissi likely used a pre-revision January).
2. **"Lowest since 2000" is a TIE with Feb 2026** (also 3.5%), not a fresh solo record — the rate has floored at 3.5% twice in four months.

## The load-bearing nuance — openings UP while hires floor
The **same JOLTS release showed construction JOB OPENINGS rising to a 10-month high (~298K)**, concentrated in **data-center/electrician demand.** So hires-at-record-low + openings-at-10mo-high = a **composition/mismatch** story (skills/wage/project-type), NOT a clean demand collapse.

**Cross-signal:** that data-center/electrician concentration ties to today's **PJM grid-emergency signal (SIG-704-007)** — the AI-data-center buildout is straining the grid AND absorbing the construction labor that IS hired, even as broad construction hiring floors.

## Per-recipient
- **LABOR (action):** fold into the freeze-deepening matrix — is construction the sharpest sector cut? How much of the openings-up/hires-down split is composition vs demand?
- **CARL (info):** construction-labor weakness = consumer/income-transmission input.
- **CORAL (info):** construction hiring is a FL/housing-construction leading input.
- **RED (info):** the precision overlays + the openings-up counter keep it two-sided.

## Caveats
- Direction/severity solid (record-low, decelerating). The framing corrections (−0.9 not −1.1; tie not solo-record) + the openings-up composition nuance are the overlay. 2008/2020 comps not independently re-pulled.
