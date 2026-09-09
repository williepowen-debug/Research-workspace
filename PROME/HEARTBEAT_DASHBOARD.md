# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "81ae87ba171e2cda06530921a6e27fba578ba7e02b3d3699ec058f19f028a83f",
  "set": {
    "one": "September 7 ruling: STAND DOWN, NO DEPLOY (WQ-189/192). FALCON's hull-loss gate fired; BRENT's capacity test was NOT MET. The deployment question is closed. Other observations retain their source dates.",
    "channels": {
      "Energy": {
        "headline": "🔴 STAND DOWN; deployment decision closed",
        "body": "September 7 WQ-189/192 ruling: NO DEPLOY. FALCON's hull-loss gate remains FIRED; BRENT's capacity test NOT MET. No new capital authorized; the capacity floor applies prospectively."
      }
    }
  }
}
```

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "65854f0e064715ede38beb1c367e075b34b2495f5e68fd0901c642d6a009a132",
  "set": {
    "one": "STAND DOWN, NO DEPLOY (September 7 WQ-189/192 ruling). September 8 Cboe SKEW 148.86 broke the prior run: FT-10 consumer 0/4, NOT FIRED; RED/VIOLET integration pending. XLE September 8 close 64.77 selected the approved September 9 exit; execution unverified. HY 268 bp [September 7]; DGS10 4.78% and DFII10 2.43% [September 4]. Other channels retain their dated observations.",
    "channels": {
      "Energy": {
        "headline": "🔴 STAND DOWN; XLE exit selected",
        "body": "NO DEPLOY under WQ-189/192. XLE 64.77 [September 8 vendor close] selected the approved September 9 sale; execution unverified. FALCON's hull-loss gate FIRED; BRENT's capacity test NOT MET."
      },
      "Rates": {
        "headline": "🔴 Officials updated through September 4; no add",
        "body": "DGS10 4.78%; DFII10 2.43% [September 4 officials]. September 8 officials UNKNOWN at the amendment read. Real-yield add gate 2.50%: 7 bp away. No new threshold or owner grade."
      },
      "Credit": {
        "headline": "🔴 HY between its lines; WAL owner grade pending",
        "body": "HY OAS 268 bp [September 7]: 8 bp above 260, 12 bp below 280. WAL 79.94 [September 8 vendor close] below 81.90; REGINALD grade pending. No new streak count or trade authority inferred."
      },
      "Equity-vol": {
        "headline": "🟡 FT-10 consumer 0/4; NOT FIRED",
        "body": "Cboe SKEW 148.86 [September 8] breaks the prior >=150 run. Consumer count 0/4; NOT FIRED. September 9 cannot be the fourth bar. RED/VIOLET owner integration pending; SIG-W-20260908-019 routed."
      },
      "War theaters + tariffs + housing": {
        "headline": "🔴 PJM post-expiry outcome ungraded",
        "body": "September 8 pre-expiry read found no successor DOE order; post-23:59 ET outcome UNKNOWN at that read. WATT owns the grade. Other theater, tariff and housing observations retain the September 7 base vintage."
      }
    },
    "ticker": {
      "HY OAS": "HY OAS 268 bp [9/7 official] (8 bp above 260; 12 bp below 280)",
      "DFII10": "DFII10 2.43 [9/4 official] (add gate 2.50 = 7 bp)",
      "DGS10": "DGS10 4.78 [9/4 official]",
      "^SKEW": "^SKEW 148.86 [9/8 Cboe; consumer 0/4, NOT FIRED; owner integration pending]",
      "WAL": "WAL 79.94 [9/8 vendor close; below 81.90; owner grade pending]",
      "USO": "USO 146.03 [9/8 vendor close]",
      "XLE": "XLE 64.77 [9/8 vendor close; approved 9/9 exit selected; execution unverified]"
    }
  }
}
```
