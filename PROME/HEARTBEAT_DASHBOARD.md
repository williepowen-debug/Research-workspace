# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Thirteenth base 2026-09-10: chain 0 — no amendment projections (the three 9/7–9/9 projections were folded into the base at the re-base; history via `git show`).*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "ccfa529662ab93548cc75bf2f0530e6196fbb50fd4a41b3e98c23f2db3e9fb8a",
  "set": {
    "one": "September 10 close: WPSR first print NO VERDICT (SPR −1.244M; 9/16 decides). Officials [9/9] DGS10 4.83 (TLT gate 0-of-5, 33 bp = window high), DFII10 2.46 (add gate 4 bp, NO-ADD). First long-end buyback: 1.75× cover, below every prior 10Y–20Y op ⇒ RED FT-11 v1.1 ACTIVATES (off-the-run branch; n=1). PJM §202(c) lapsed QUIET 9/8. Book: USO 150/165 spread closed +$330; TLT 77P ×20; XLE 65C ×1 owed a ruling. STAND DOWN holds.",
    "channels": {
      "Energy": {
        "headline": "🔴 WPSR first print NO VERDICT; spread closed +$330",
        "body": "SPR 285.360M (−1.244M) [EIA 9/10]: L305 two-print test unresolved, the 9/16 print decides; Cushing 21.824M. USO 158.38 [9/10 close]. Robinhood USO 150/165 spread CLOSED by Will's hand +$330; a USO 159C expiring 9/11 is on, Will-managed. STAND DOWN (WQ-192) unchanged."
      },
      "Rates": {
        "headline": "🔴 Officials [9/9]: 10Y 4.83, real 2.46; buyback cover 1.75× ⇒ FT-11 v1.1 activates",
        "body": "DGS10 4.83 [9/9]: TLT gate 0-of-5, 33 bp from 4.50 (window high). DFII10 2.46: add gate 2.50 is 4 bp away, NO-ADD; BOND's 9/10 estimate fires nothing until FRED prints. 30Y reopening clean on every test (BOND: expensive, not broken). First 10Y–20Y buyback: $5.187B of $6.0B, offered $10.489B = 1.75× cover, below the prior minimum 3.22× ⇒ off-the-run ⇒ RED FT-11 v1.1 ACTIVATES; DGS30 9/10 close unknown until FRED (L320)."
      },
      "Credit": {
        "headline": "🔴 C#2 locks on the 9/8–9/9 cells; WAL 79.28",
        "body": "HY 267 · 271 [9/8 · 9/9] both inside (260, 280) ⇒ C on NEXUS's letter; NEXUS grades 9/11. WAL 79.28 [9/10 close], exit line 81.90 0-of-3. CRMT letters graded at Friday's close (OTTO L311)."
      },
      "War theaters + tariffs + housing": {
        "headline": "🔴 PJM order lapsed QUIET 9/8 (WATT); large-load leg unknown",
        "body": "DOE 202-26-41 expired 9/8 with no extension and no emergency event on the tape; whether a large-load direction was ever issued is UNKNOWN (no utilisation report). NEXUS decides ARMED vs COUNTED. WATT P1 steps 5→3 at its first boot on/after 9/11."
      }
    },
    "ticker": {
      "DGS10": "DGS10 4.83 [9/9 official] (TLT gate <4.50: 0-of-5, 33 bp)",
      "DFII10": "DFII10 2.46 [9/9 official] (add gate 2.50 = 4 bp, NO-ADD)",
      "DGS30": "DGS30 5.28 [9/9 official]",
      "USO": "USO 158.38 [9/10 close]",
      "TLT": "TLT 80.78 [9/10 close]",
      "WAL": "WAL 79.28 [9/10 close] (exit line 81.90 ×3, 0-of-3)",
      "XLE": "XLE 64.93 [9/10 close] (65C ×1 survivor — WQ-210)",
      "Cushing": "Cushing 21.824M [wk-9/4, EIA 9/10] (re-arm floor <20.0M = 1.824M away)"
    }
  }
}
```
