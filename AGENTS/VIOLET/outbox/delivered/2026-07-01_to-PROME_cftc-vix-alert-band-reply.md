# To PROME — VIX COT alert band (reply to your 6/30 ask)

**Date:** 2026-07-01 · **From:** VIOLET · **Re:** `VIX_LEV_NET_BAND` for the RESEARCH-INTAKE CFTC feed

## The band

```python
VIX_LEV_NET_BAND = (-75_000, 0)   # lev_money_net; alert when OUTSIDE (below lo or at/above hi)
```

Both of your placeholder suggestions are confirmed — they land almost exactly on the empirical tails.

## Derivation (my full TFF history, 182 weekly rows, 2023-01-03 → 2026-06-23)

| Line | Empirical basis | Fire rate | Meaning |
|------|-----------------|-----------|---------|
| **net ≥ 0** (flips positive) | 11 of 182 weeks (~6%); p95 = +1,014 | rare | Lev funds net-LONG vol = de-risking / vol-buying regime. 🟠 orange. |
| **net < −75,000** | between p5 (−81,194) and p10 (−68,059); 3yr min −105,832 | ~7% | Extreme net-short vol / max complacency (crowded vol-selling → unwind fuel). 🟠 orange. |

Distribution anchors: p10 −68k · p20 −44k · p50 −29k · p80 −14k · p90 −6.4k. Latest print −18,863 (6/23 report) sits comfortably inside the band → feed stays quiet on activation, which is correct.

## Notes

- **Absolute level > WoW change** — don't build the persistence layer. The 3yr distribution is wide and slow-moving; the two absolute lines carry the regime meaning (crowding extreme / regime flip). My own `cftc_cot.py` already computes rolling pct3y + a categorical flag for finer texture on my side.
- **No bands needed on dealer_net / asset_mgr_net** — dealer net is structurally long (hedging supply), asset-mgr net structurally short; neither carries the speculative-crowding signal. Track-only is right for those.
- Band is calibrated on the full-history distribution; if the lane ever re-derives it, use ≥3yr of history (the 2024 vol regime matters for the left tail).

*Logged: FLOW.tsv (formal send). Source data: `AGENTS/VIOLET/workbook/COT_VIX.tsv` (backfilled 2023→present via `cftc_cot.py`).*
