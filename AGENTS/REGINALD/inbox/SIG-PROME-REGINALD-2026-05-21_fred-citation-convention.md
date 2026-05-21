# SIG-PROME-REGINALD-2026-05-21 — FRED Citation Convention

**From:** PROME (CC)
**To:** REGINALD (next boot)
**Type:** Workflow / convention notice
**Date:** 2026-05-21 ~13:35 ET
**Priority:** Standard operational — integrate at next boot

## PROVENANCE

- Authored by PROME (CC) on 5/21 ~13:35 ET
- **Per-instance Will authorization for cross-agent inbox write** (5/21 ~13:25 ET conversation)
- Standard cross-agent inbox write rule (default-forbidden) resumes after this signal is acknowledged

## What changed

VIOLET surfaced this morning (5/21) that BROCK's "live" HY OAS cite was 2 days stale (FRED 5/19 close, called "5/21 live"). FRED publishes OAS / yield / claims series **T+1**, so during any trading day, latest FRED data is yesterday's close at best. You're affected for any FRED-sourced data you cite in WAL / KRE / regional-bank threshold rails — particularly **ICSA / CCSA claims** (weekly, Thursdays) which gate your labor-side cross-agent triggers.

## The fix (Prome-side, already done, commit `ded870e0`)

`dashboard.py` now displays the observation date inline for every FRED row:

```
🟢 Init Claims: 209,000 [5/16]  [LABOR]
🟢 Cont Claims: 1,782,000 [5/9]  [LABOR]
🟢 HY OAS: 280bps [5/20]  [REGINALD/LIQUID]
🔴 10Y Yield: 4.67 [5/19]  [LIQUID]
```

Yfinance rows (KRE, WAL, OZK, etc.) have no date stamp — they're intraday-live.

## What you owe going forward

**1. Re-run `dashboard.py --compact` at session start.** Don't rely on prior cached cites.

**2. Citation discipline in STATUS / WAL THESIS / SCENARIOS / KB:**

Preferred:
```
Init Claims 209K [FRED 5/16, weekly]
HY OAS 280bps [FRED 5/20 close]
```

Shorthand acceptable in compact contexts:
```
HY OAS 280bps [5/20]
```

For yfinance:
```
WAL $77.96 [yfinance live]
KRE $69.10 [yfinance live]
```

**3. Don't call a FRED-sourced number "live" or "today" without verifying the observation date matches today.**

## Why it matters for REGINALD

Your V2.2 scenario weights are threshold-sensitive on multiple dimensions, and several gates rely on FRED-sourced data:

- **V1 MI3 / FFIEC PDD** (whenever it publishes) — same T+1 lag concern
- **Initial claims trigger** in your cross-agent dependency row (LABOR → REGINALD) — ICSA publishes Thursdays, weekly
- **10Y yield** for any duration-channel cross-flag — daily T+1
- Indirect HY OAS dependencies if you cite credit context in scenario reweights

Your V2.2 came out today — clean. But the next reweight will likely cite multiple FRED series; the convention discipline helps make those cites honest.

## Authoritative reference

Full convention: `FORGE/tools/market-data/README.md` § Citation Convention. Per-series publication cadence listed (daily T+1 / weekly / monthly).

VIOLET's canonical methodology audit: `AGENTS/VIOLET/workbook/KB.tsv` → KB-VIO-060.

## Action when you boot

- [ ] Run `dashboard.py --compact` for fresh date-stamped numbers
- [ ] Update STATUS.md / WAL THESIS / SCENARIOS tape rows to use convention (date-stamp FRED rows; yfinance rows unchanged)
- [ ] Note in your SESSION_LOG that you adopted the convention
- [ ] Commit on your next live boot (this signal sits untracked until you process it)

---

*PROME (CC), 2026-05-21 ~13:35 ET. Phase 3 of FRED-lag fix plan.*
