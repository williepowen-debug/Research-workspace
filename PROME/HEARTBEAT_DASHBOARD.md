# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Twenty-second base 2026-09-25 (post-close) — chain 0: the twenty-first base's amendment #1 was folded into the base at the re-base, so its projection is REMOVED; zero projections stood until amendment #1 (2026-09-26 17:5x ET, PROME, Will-directed correction): projection below.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "f4f3a32c6881b83b97ad42b4d0211b4932be79e09625ea42ad21c688d3de5375",
  "set": {
    "channels": {
      "AI capex": {
        "headline": "🟠 GATE-LIQ-069 now 2-of-2 on CoreWeave CDS trades — upfronts observed, spreads model-derived",
        "body": "CoreWeave 5Y CDS DTCC trades: 500bp coupon + 11.82pt upfront [9/24] / 11.46pt [9/23] — OBSERVED. ≈847 / 835bp = MODEL-DERIVED (LIQUID crwv_cds_grade.py, not the ISDA model; gap unmeasured; ±25bp not established). Will (WQ-301 a): the trades are the instrument; anchor re-base HELD for the ISDA benchmark (L510, Mon). The registered cohort discriminator did NOT FIRE on its checked observations — not evidence wider stress is absent; NEXUS flag unrouted at WALTER. ORCL 10-Q: off-BS DC leases $288B; Oracle 5Y CDS record [9/24, press/vendor, ungraded]. No capital path."
      }
    }
  }
}
```

*Amendment #2 (2026-09-28 12:5x ET, PROME, first market-session write since the 9/25 post-close base): projection below.*

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "c5fd67a54cc020464d11b7a270d8a020b8ec87554da2d4a42372fe0cde2fdc57",
  "set": {
    "channels": {
      "Credit": {
        "headline": "🟠 HY 293 / CCC 1,128 [9/25] — RED-FT-01 2 of 3; the 9/28 cell decides",
        "body": "FRED 9/25 (published Mon AM): HY OAS 293 · CCC 1,128. RED-FT-01 (≥280 ×3) 2 of 3 — the 9/28 cell (Tue AM) completes or resets; RED rules. X1 >280 strict 1 of 3, CLOSED regardless (8/28). Re-kill 0 of 2, 33bp. LIQUID's 283 estimate missed high; Q4 'isolated CCC' lean withdrawn. IG/BBB not joined (BOND). STAND DOWN holds; no capital path."
      }
    }
  }
}
```
