# SIG-PROME-BROCK-2026-05-21 — FRED Citation Convention

**From:** PROME (CC)
**To:** BROCK (next boot)
**Type:** Workflow / convention notice
**Date:** 2026-05-21 ~13:35 ET
**Priority:** Standard operational — integrate at next boot

## PROVENANCE

- Authored by PROME (CC) on 5/21 ~13:35 ET
- **Per-instance Will authorization for cross-agent inbox write** (5/21 ~13:25 ET conversation)
- Standard cross-agent inbox write rule (default-forbidden) resumes after this signal is acknowledged

## What changed

VIOLET surfaced this morning (5/21) that your STATUS cite **"HY OAS 286 (live 5/21 dashboard)"** was actually matching FRED's **5/19 close** — meaning your "live" number was 2 days stale. Same for CCC OAS 948 (actually 5/19 close; FRED 5/20 = 940). This propagated through the 4-agent thesis convergence (BROCK + REGINALD + HENRY + VIOLET) before VIOLET's direct-FRED spot-check caught it (her KB-VIO-060).

**Root cause:** FRED publishes OAS / yield / claims series **T+1** (end-of-day computed → next morning publish). At any moment during a trading day, the latest data FRED returns is yesterday's close at best. This isn't your fault — the workflow / dashboard wasn't surfacing the observation date.

## The fix (Prome-side, already done, commit `ded870e0`)

`dashboard.py` now displays the observation date inline for every FRED row:

```
🟢 HY OAS: 280bps [5/20]  [REGINALD/LIQUID]
🟡 CCC OAS: 940bps [5/20]  [LIQUID]
🔴 10Y Yield: 4.67 [5/19]  [LIQUID]
🔴 Brent: $104.75  [HENRY]              ← yfinance intraday-live, no stamp needed
```

Yfinance-sourced rows (KRE, APO, WAL, Brent, etc.) have no date stamp — they're intraday-live.

## What you owe going forward

**1. Re-run `dashboard.py --compact` at session start** to get the date-stamped numbers. Don't rely on prior cached cites.

**2. Citation discipline in STATUS / KB / TRADE.md:**

Preferred:
```
HY OAS 280bps [FRED 5/20 close]
CCC OAS 940bps [FRED 5/20 close]
```

Shorthand acceptable in compact contexts:
```
HY OAS 280bps [5/20]
```

For yfinance (intraday-live):
```
APO $132.65 [yfinance live 13:30]
APO $132.65                          ← timestamp implied current if no tag
```

**3. Don't call a FRED-sourced number "live" or "today" without verifying the observation date matches today.**

## Why it matters for BROCK

Your convergence math is threshold-sensitive. When HY OAS is "286 [live]" vs "286 [5/19]" vs actual "280 [5/20 latest]":

- Cushion from 260 kill: **20bps actual vs 26bps cited** (closer to bear-thesis invalidation than the morning framing suggested)
- Distance from R11 trigger #4 (HY >290): **10bps actual vs 4bps cited** (Stage-3 firing farther off than morning framing suggested)

Both readings shift the convergence picture. Not a thesis-breaker, but precision discipline matters at thresholds.

## Authoritative reference

Full convention: `FORGE/tools/market-data/README.md` § Citation Convention (just added). Per-series publication cadence listed there.

VIOLET's canonical methodology audit: `AGENTS/VIOLET/workbook/KB.tsv` → KB-VIO-060.

## Action when you boot

- [ ] Run `dashboard.py --compact` for fresh date-stamped numbers
- [ ] Update STATUS.md tape rows to use convention (date-stamp FRED rows; yfinance rows unchanged)
- [ ] Note in your SESSION_LOG that you adopted the convention
- [ ] Commit on your next live boot (this signal sits untracked until you process it)

---

*PROME (CC), 2026-05-21 ~13:35 ET. Phase 3 of FRED-lag fix plan.*
