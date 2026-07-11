# JPY-Vol Instrument — SCOPE (not built) — 2026-07-11 (Sat, weekend; vintages stamped)

**Trigger:** PROME pre-CPI wave (Will-approved), item 2 — scope the JPY-vol leg of the queued canary map ahead of the 7/16 Japan double-discriminator. **This memo scopes; nothing was built.** Feasibility pulls run 2026-07-11 ~17:55 ET (weekend — all values Fri-close/last-trade vintages).

## 1. Metric candidates + pullability (tested from this environment)

| Candidate | Pullable? | Test result (7/11 pull) | Verdict |
|---|---|---|---|
| **CBOE/CME JPY vol index (^JYVIX)** | ❌ NO | yfinance: "possibly delisted; no price data" (period=1mo, 0 rows). ^EVZ (euro sibling) equally dead — the CBOE FX-vol index family is discontinued | Dead — exclude |
| **USDJPY realized vol (from JPY=X closes)** | ✅ YES | JPY=X 161.67 [7/10]; 66 rows/3mo clean; 3y history clean (770 rolling obs). 10d annualized RV **5.62%** [7/10], 20d **4.25%** | **PRIMARY** — free, robust, computable to any window |
| **FXY ATM option IV (yfinance chain)** | ✅ YES | FXY spot 56.74 [7/10 last]; chain live, monthlies to Dec-2026; Aug-2026 near-ATM call IV **~11.4%** with real OI (2,174 near-ATM; the 14.3% quote sat on OI 17 — filter thin strikes) | **CONFIRM leg** — forward-looking but chain-quality-sensitive (OI filter mandatory, weekend quotes stale) |
| OTC USDJPY implied (25δ RR / 1m ATM, e.g. Bloomberg/Refinitiv) | ❌ not from this environment | No free feed found; would be the professional-grade instrument | Note as upgrade path only |

**Design: two-legged proxy.** Realized (JPY=X) = the always-available spine, percentile-calibrated; FXY ATM IV = the forward-looking confirm and the event-premium gauge (IV/RV ratio). This mirrors the VIX/realized VRP structure VIOLET already uses.

## 2. Threshold grounding (3y percentiles, computed this session — n=770 rolling 10d RV obs, 2023-07-24 → 2026-07-10)

| Line | 10d RV level | Role |
|---|---|---|
| p50 | 8.35% | Baseline |
| p75 | 11.25% | — |
| **p90 = 13.95%** | **WATCH** | Canary yellow — carry stress building |
| **p95 = 15.13%** | **FIRE** | Canary red — route to SAM + PROME; cross-check vs SAM's flow resolver |
| p99 = 17.80% | Aug-2024-class | Reference: the 2024 carry-unwind peaked **17.88% (2024-08-09)**; 3y max 20.06% (2025-04-23) |

**Current state [7/10]: 10d RV 5.62% — BELOW p50, near-floor calm.** Same complacency shape as the equity surface. Meanwhile FXY ATM IV ~11.4% ≈ **2× realized** — the options market is already carrying an event premium into the 7/15-7/16 window that the realized leg can't see. That IV/RV spread is itself the third proposed signal: **spread >2× = event priced; spread collapsing toward 1× post-event without an RV spike = risk passed; RV spiking through IV = unwind underway** (the Aug-2024 signature).

**Canary-map integration (fire → route):** WATCH (p90) → note in NEXUS_BRIEF cross-domain; FIRE (p95) → outbox to SAM + PROME same session (carry-unwind = the KB-VIO-102/Aug-2024 replay class; VIOLET owns only the vol-transmission read, SAM the substance). Thresholds are percentile-anchored so they self-update with the window — re-derive at each calibration pass, don't hardcode.

## 3. Build cost (estimate)

| Component | Cost |
|---|---|
| `jpy_vol.py` (JPY=X pull → rolling RV → percentile table → threshold check; FXY chain → OI-filtered ATM IV → IV/RV ratio) | ~1 focused session (the RV math is 20 lines; the chain OI-filter is the only fiddly part) |
| boot.py wiring (one BOOT_SEQUENCE step + KEY_MARKERS, same pattern as the 6/23 credit-gate wiring) | ~15 min, established pattern |
| Calibration note (percentile ladder + Aug-2024 anchor → KB row + SIGNAL_INTAKE threshold line) | ~30 min |
| Data cost | $0 (yfinance) |

**Total: one small session.** No new dependencies. Recommend building BEFORE Wed 7/15 evening (MOF ITS ~7:50 PM ET) so the instrument is live for the discriminator, not after it.

## 4. Risks / caveats

- **JPY=X is Yahoo's composite FX feed** — fine for RV, but a data-minute discipline note applies (KB-VIO-100/101 class): FX trades nearly 24h, so "close" needs a fixed convention (use Yahoo's daily bar as-is, stamp it).
- **FXY chain on weekends quotes stale IVs** — the confirm leg is only trustworthy intraday with OI ≥ some floor (propose ≥100).
- **FXY is yen-UP exposure** (inverse USDJPY) — ATM IV is direction-agnostic but skew reads would invert; scope excludes skew for v1.
- The 7/16 row is already in CATALYSTS.tsv/CALENDAR.md (this session) with the current near-floor readings stamped — if the build doesn't happen by 7/15, the manual recipe in §1-2 is executable by hand in ~5 minutes.

*Sources: yfinance JPY=X (3y daily, pulled 2026-07-11), FXY option chain (pulled 2026-07-11, weekend-stale caveat), ^JYVIX/^EVZ dead-ticker tests same pull. SAM resolver figures per PROME canon 7/11. Nothing herein is live; nothing was built.*
