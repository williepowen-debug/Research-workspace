---
signal_id: SIG-W-20260723-004
dispatched: 2026-07-23T23:10:00Z
origin: RESEARCH-INTAKE lane (CFTC COT feed, run 2026-07-23T16:23Z — orange flag)
source: CFTC Commitments of Traders, VIX futures, report date 2026-07-14 (released ~7/17)
signal_type: positioning
domain: VOLATILITY
cluster: POSITIONING_VALUATION
signal_role: primary_substance
precedence: ROUTINE
to: VIOLET
info: [SAM]
confidence: 0.9
verify_verdict: PRIMARY-DATA (CFTC series via lane feed; no verify-spawn — registered-feed class)
---

# CFTC COT (7/14): leveraged-money net LONG +10,189 VIX futures — the structural vol-short cohort is positioned long vol

## Substance (CFTC primary, 0.9)

VIX futures COT, report date **2026-07-14** (OI 389,088):
- **Leveraged money net +10,189 (LONG)** — the cohort that structurally harvests the vol carry short; a net-long print = hedge funds positioned FOR vol, the lane's registered de-risking-regime flag (orange).
- Dealer net +34,335 · Asset manager net −43,329.

## Read + caveats

- **Vintage is load-bearing:** 7/14 data — **pre-dates this week's escalation** (Brent >$100 7/23, VIX 18.7→19.7, OVX 70.3 cycle high, oil-vol transmitting to equities per BRENT). Positioning was ALREADY long-vol before the 7/22-23 leg — meaning the de-risking posture preceded the escalation rather than chasing it. Next COT (7/21 data, releases ~7/24) shows whether it extended.
- For VIOLET: pairs with the dealer-gamma halving datum (SIG-W-20260719-009, $16.2bn→$6.2bn) — dealers shed the stabilizer while fast money went net-long vol = both structural vol-suppressors weakening into the escalation window.
- **SAM (info):** vol positioning context for the yen/carry axis (long-vol regime + USD/JPY 163.8).

## Provenance

- Intake: lane CFTC feed orange flag → ROUTINE dispatch per lane precedence mapping; onset-dedup fresh (first flag on this condition).
