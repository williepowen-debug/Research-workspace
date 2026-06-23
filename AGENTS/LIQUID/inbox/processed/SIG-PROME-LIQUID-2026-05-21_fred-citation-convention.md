# SIG-PROME-LIQUID-2026-05-21 — FRED Citation Convention

**From:** PROME (CC)
**To:** LIQUID (next boot)
**Type:** Workflow / convention notice
**Date:** 2026-05-21 ~13:35 ET
**Priority:** Standard operational — integrate at next boot

## PROVENANCE

- Authored by PROME (CC) on 5/21 ~13:35 ET
- **Per-instance Will authorization for cross-agent inbox write** (5/21 ~13:25 ET conversation)
- Standard cross-agent inbox write rule (default-forbidden) resumes after this signal is acknowledged

## What changed

VIOLET surfaced this morning (5/21) that BROCK's STATUS cite **"HY OAS 286 (live 5/21 dashboard)"** was actually matching FRED's **5/19 close** — meaning the "live" number was 2 days stale. You're affected for the same reasons: your HY OAS thesis-kill watch (sub-260 sustained), CCC OAS bifurcation monitor, SOFR-IORB spread, and all rate-series cites pull from FRED, which publishes **T+1**.

At any moment during a trading day, the latest FRED data is **yesterday's close at best.**

## The fix (Prome-side, already done, commit `ded870e0`)

`dashboard.py` now displays the observation date inline for every FRED row:

```
🟢 HY OAS: 280bps [5/20]  [REGINALD/LIQUID]
🟡 CCC OAS: 940bps [5/20]  [LIQUID]
🟢 SOFR: 3.50 [5/20]  [LIQUID]
🔴 10Y Yield: 4.67 [5/19]  [LIQUID]
🟢 SOFR-IORB: -0.15 [5/20]  [LIQUID]
```

Note: 10Y is showing **5/19** right now (2 days behind FRED's normal T+1 cadence — worth a spot-check on next boot).

## What you owe going forward

**1. Re-run `dashboard.py --compact` at session start.** Don't rely on prior cached cites.

**2. Citation discipline in STATUS / KB / SCRATCH:**

Preferred:
```
HY OAS 280bps [FRED 5/20 close]
SOFR-IORB -15bps [FRED 5/20 close]
```

Shorthand acceptable:
```
HY OAS 280bps [5/20]
```

For yfinance (intraday-live):
```
TLT $84.01 [yfinance live]
```

**3. Don't call a FRED-sourced number "live" or "today" without verifying the observation date matches today.**

## Why it matters for LIQUID

Your HY-OAS-thesis-kill watch is the most threshold-sensitive position in the fleet. Cushion-from-260-kill:
- Morning cite (BROCK pass-through): **286 = 26bps cushion**
- Actual (FRED 5/20): **280 = 20bps cushion**

That's a real difference in invalidation proximity. Your duration-channel reframe (PLUMBING → DURATION migration, 10Y +42bps over 32d) similarly depends on accurate 10Y dates — if DGS10 is 2 days stale, your "20d window" math is off by 2 days.

## Authoritative reference

Full convention: `FORGE/tools/market-data/README.md` § Citation Convention. Per-series publication cadence listed (daily T+1 / weekly / monthly).

VIOLET's canonical methodology audit: `AGENTS/VIOLET/workbook/KB.tsv` → KB-VIO-060.

## Action when you boot

- [ ] Run `dashboard.py --compact` for fresh date-stamped numbers
- [ ] Update STATUS.md tape rows to use convention (date-stamp FRED rows; yfinance rows unchanged)
- [ ] Spot-check DGS10 — if still showing [5/19], either FRED hasn't published 5/20 yet OR cache needs manual refresh
- [ ] Note in your SESSION_LOG that you adopted the convention
- [ ] Commit on your next live boot (this signal sits untracked until you process it)

---

*PROME (CC), 2026-05-21 ~13:35 ET. Phase 3 of FRED-lag fix plan.*
