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

*Twenty-third base 2026-09-28 (post-close, PROME prome-64) — chain 0: the twenty-second base's amendments #1–#3 were folded into the base at the re-base, so their projections are REMOVED; zero projections stand until the next amendment.*

*Amendment #1 (2026-09-28 22:1x ET, PROME `prome-64` closeout; folds the SCRATCH queue ①–⑧): projection below.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "0a8398c3dbce766e6c92b5617dba69389f9cb70d83dde048ee9de7c3ea327561",
  "set": {
    "channels": {
      "Credit": {
        "headline": "🟠 HY 293 / CCC 1,128 [9/25] — RED-FT-01 2 of 3, Tuesday's cell decides; the CDS ±25bp claim is CONDITIONAL, the >552/>666.5 letter governs",
        "body": "FRED 9/25: HY OAS 293 · B 300 · CCC 1,128; RED-FT-01 (≥280 ×3) 2 of 3 — the 9/28 cell (Tue) completes or resets; X1 CLOSED regardless. GATE-LIQ-069 2-of-2: the base's ±25bp / >697–>737 sentence is WITHHELD — LIQUID's own conditions (packet 332a8687b L61–62): positive 7/06 sign, cash convention, official curve in bracket; negative sign ⇒ >520/>649; 'not a recommendation to re-base permanently now'; the letter governs, Will's hold stands (WQ-301 b, 10/02). No capital path."
      },
      "Equity-vol": {
        "headline": "🟡 HENRY 9/28: SPX gamma NEGATIVE both horizons, spot below the 7,700 put strike — supersedes the base's ≈0 [9/24]",
        "body": "HENRY b07da43bd (via WALTER): gamma negative on both horizons with spot below the 7,700 put strike; VIX 16.07 · MOVE 101.82 [9/28c, yfinance]. VIOLET 9/28: credit widened in every bucket 9/22→9/25 while VIX fell — WATCH, not a fire. No threshold moved."
      }
    }
  }
}
```

*Amendment #2 (2026-09-29 10:5x ET, PROME `prome-82` closeout; the 9/28 credit cells + LIQ-076 + HOMER gate): projection below.*

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "cae9d5adc63ba8dad3c27ba496c1b604dc7b37cf13954f1d8ff43948a3b73dc1",
  "set": {
    "channels": {
      "Credit": {
        "headline": "🟠 HY 302 / B 309 / CCC 1,146 [9/28] — RED-FT-01 EXIT leg met (CONF 68→70, not a bear confirm); X1 CLOSED; nearest line HY >320 (18bp)",
        "body": "FRED 9/28 (posted ~10:2x 9/29): HY 302 · BB 183 · B 309 · CCC 1,146 · IG 83 · BBB 102. RED: ≥280 ×3 is FT-01's EXIT leg — met at 280.0/293/302, CONF +2 mechanical, not a bear confirm; FT-02 >320 is the nearest line. LIQUID: X1 strict 2 in a row, CLOSED regardless; LIQ-07 1 of 3; BROADENS 3rd print. BOND: row 4 (HY >300 w/ velocity) MET → 15/35, a marker; IG/BBB legs NOT MET. GATE-LIQ-076 conjunction MET 9/25 (write-up, not a trigger). GATE-HOMER-THESIS-KILL registered (24 rows)."
      },
      "Energy": {
        "headline": "🟠 Nov Brent's LAST GRADED SETTLE is today; live 10:11 ET $103.76 (−1.4%, vendor); Dec pin Wed (L461, a calendar step)",
        "body": "Live 10:11 ET vendor reads, not settles: BZX26 $103.76 · USO 146.85 (−2.1%) · VLO 383.64 (−1.5%). BRENT publishes the settle. Wed: the Dec pin (headline drops ~$7.5 on the calendar, never a signal), WPSR (first dated diesel export-restriction read), Will's expiries. STAND DOWN (WQ-192) holds."
      }
    }
  }
}
```

*Amendment #3 (2026-09-29 15:5x ET, PROME `prome-e6` closeout; session 5 long-end-led · NEXUS two roots · the 9/29 reconcile · KRE/WAL yellow · the gamma shelf-life KOS entry): projection below.*

```dashboard-amendment
{
  "amendment": 3,
  "source_sha256": "d8e39dd73686aa5eb0f0cbed9bf215d2fbdd57177d98c3fd5eff6e94099869f0",
  "set": {
    "channels": {
      "Rates": {
        "headline": "🔴 SESSION 5 LONG-END-LED: 10Y ~5.28 · 30Y ~5.61 intraday 9/29 (vendor), front end flat, FF strip unmoved — term-premium SHAPE, US-ORIGINATED; the 9/29 official cells (~16:15) are the grade",
        "body": "BOND KB-BND-361/362 (vendor intraday 12:3x–12:5x ET): bear steepener, Bund 10Y −3bp · gilt +1 · JGB flat · oil down; the 30Y rose ~2bp INTO the 10:00 consumer-confidence miss (81.9, weakest since Apr-2014). Pre-registered: BND-30 (70%, ACM term-premium share ≥0.50 on the 9/29 row, ceiling 10/9) · BND-31 (65%, Tokyo 9/30 JGB 30Y < +4bp = NOT exporting). If the close holds: 30Y ≥5.60 ⇒ since 2004-05-13, 10Y ≥5.28 ⇒ since 2002-05-15. NEXUS WQ-340, as corrected by CATO (744a8b540): an established rates-related cluster + a CANDIDATE second credit cause + a control — not 'two roots'; PRED-50's branches not yet exhaustive (NEXUS repairing); next link IG OAS >94 (GATE-LIQ-072, 11bp), a level, not an attribution. KOS: HENRY's negative-gamma read has a ONE-SESSION shelf life (expires at the 9/29 close)."
      },
      "Credit": {
        "headline": "🟠 A CANDIDATE second credit cause is UNOWNED — NEXUS: the 9/25 tier widening was nominal-rates-flat, cable-led (an AI-disruption scare in incumbents; not an established root, CATO PN2); WQ-341 for Will; KRE/WAL zone green→yellow 12:08 9/29",
        "body": "NEXUS 83e6fe366: RED FT-01 · BOND row 4 · LIQUID X1 · REGINALD re-arm = ONE FRED series read four ways; CCC 1,146 is a pre-existing R3; the credit leg's own discriminator is LIQ-07 SPREAD-B (B ≥304 [9/29] · ≥308 [9/30]); NEXUS PRED-50 tests the candidate on B OAS over nominal-rates-quiet sessions 9/29→10/8 (DOCKET L553) — its branches are not exhaustive (CATO PN1), correction owed by NEXUS. KRE 69.54 · WAL 74.24 (vendor 12:08 ET). Book RECONCILED 9/29 13:4x intraday (ANVIL b983d745a): quantities unchanged; D-60 narrowed (OTM expiry liquidation OBSERVED ×4; ITM unobserved). 24th re-base OWED."
      }
    }
  }
}
```
