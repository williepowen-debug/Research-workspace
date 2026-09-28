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
        "body": "FRED 9/25 (published Mon AM): HY OAS 293 · CCC 1,128. RED-FT-01 (≥280 ×3) 2 of 3 — the 9/28 cell (Tue AM) completes or resets; RED rules. X1 >280 strict 1 of 3, CLOSED regardless (8/28). Re-kill 0 of 2, 33bp. LIQUID under-called by 10bp (293 vs ≈283); Q4 'isolated CCC' lean withdrawn. IG/BBB not joined (BOND). STAND DOWN holds; no capital path."
      }
    }
  }
}
```

*Amendment #3 (2026-09-28 18:5x ET, PROME, third-sitting Standard closeout after the close): projection below.*

```dashboard-amendment
{
  "amendment": 3,
  "source_sha256": "1e0fa993b76add7b5217c0362c04a74ce45fab752e2342421ed2c70c3663e99d",
  "set": {
    "channels": {
      "Rates": {
        "headline": "🔴 OFFICIAL 9/28: 2Y 4.92 · 10Y 5.24 · 30Y 5.56 (through HENRY's 5.50 red) · 10Y real 2.90 — near-parallel since 9/22, driver wire-attributed, not causal",
        "body": "Treasury par curve 9/28 (BOND KB-BND-350/353, official): 2Y 4.92 (+11, highest since May-2024) · 10Y 5.24 (since Jun-2007) · 30Y 5.56 (+7, since Jun-2004; HENRY's L489 wake grades 9/29) · 10Y real 2.90 (+7; NEXUS grades the FRED cell) · 2s30s 64. 9/22→9/28: 2Y +21 / 30Y +27 — BOND corrects its whole-episode 'front-end-led' framing (9/28 itself was front-end-led). Oct hike odds ~68% (from ~64%, vendor ZQ, approximate); the 2027 path rose. No US data or Fed speaker — wire-attributed to oil/Iran headlines (KB-BND-357), not causal — WQ-317 approved (one page 10/02, 'undetermined' allowed). Book: 004 TLT 77P ×15, TLT 82P ×1 (Will's 9/28 fills)."
      },
      "Energy": {
        "headline": "🟠 Brent Nov expires Tue — the Wed headline drops ~$7.50 on the Dec pin (a calendar step); export-restriction risk registered (L531)",
        "body": "BRENT's 9/28 read is a VENDOR read (BRENT publishes settles): Nov ~$105.29, Dec ~$97.83, Nov−Dec $7.51 (expiry squeeze). F1 crack at the ~settle: Nov $96.23 ABOVE $95, Dec $94.50 BELOW — November governs through 10/14; the 10/06 sitting sets the month after. 'Petroline restarted / Yanbu resumed' = Bloomberg, one source, Aramco silent — kill-list entry STANDS; FALCON grades 9/29. US diesel export-restriction risk: Trump on record 9/22 + 9/27, denials from aides; first dated read Wed 9/30 (EIA exports + Russia ban expiry); CATO MR19 — breach timings WITHDRAWN. VLO held share ×1 now under GATE-TERRY-VLO-HELD-01 (WQ-330 BOTH); 2 staged shares unchanged."
      },
      "Credit": {
        "headline": "🟠 KILL-ON-SIGHT: 'CCC 968 is under 1,100' — Bloomberg index vs the fleet's ICE BofA CCC (1,128 [9/25]); RED-FT-01 still 2 of 3, Tue AM decides",
        "body": "968 [9/25] is the BLOOMBERG CCC index; the fleet's series and BOND's 1,100 marker are ICE BofA CCC & lower (FRED BAMLH0A3HYC) = 1,128 [9/25]; same trap for B (281 vs 300) and HY YTW (8.10% vs 7.87%) — never compare across indices. The 9/28 HY cell (Tue AM) completes or resets RED-FT-01 (2 of 3). X1 CLOSED regardless. $0 moved."
      }
    }
  }
}
```
