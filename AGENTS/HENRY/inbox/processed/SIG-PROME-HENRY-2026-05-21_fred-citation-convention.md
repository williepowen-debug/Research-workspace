# SIG-PROME-HENRY-2026-05-21 — FRED Citation Convention

**From:** PROME (CC)
**To:** HENRY (next boot — or current session via SendMessage if still standing by)
**Type:** Workflow / convention notice
**Date:** 2026-05-21 ~13:35 ET
**Priority:** Standard operational — integrate at next boot

## PROVENANCE

- Authored by PROME (CC) on 5/21 ~13:35 ET
- **Per-instance Will authorization for cross-agent inbox write** (5/21 ~13:25 ET conversation)
- Standard cross-agent inbox write rule (default-forbidden) resumes after this signal is acknowledged

## What changed

You already saw VIOLET's FRED spot-check finding via LIAISON — this signal formalizes it as a fleet-wide convention. VIOLET surfaced 5/21 AM that BROCK's HY OAS 286 cite was actually FRED's 5/19 close (2 days stale). FRED publishes OAS / yield / claims series **T+1**, so latest FRED data is yesterday's close at best.

You're affected for any FRED-sourced data you cite in your STATUS / vol-regime / cross-agent dependency tables — particularly:

- **HY OAS** + CCC OAS (your tape side of trap-clinching)
- **10Y / 2Y / yields** (substance side; tied to R11 trigger #6)
- **Initial claims / continuing claims** (HEN-28 labor cliff)
- **T10YIE breakeven** (inflation-adjusted yield framing)

## The fix (Prome-side, already done, commit `ded870e0`)

`dashboard.py` now displays the observation date inline for every FRED row. Yfinance rows (SPX, VIX, SKEW, VVIX, etc.) have no date stamp — they're intraday-live.

```
🟢 HY OAS: 280bps [5/20]  [REGINALD/LIQUID]
🟡 CCC OAS: 940bps [5/20]  [LIQUID]
🔴 10Y Yield: 4.67 [5/19]  [LIQUID]
```

## What you owe going forward

**1. Re-run `dashboard.py --compact` at session start.** Don't rely on prior cached cites.

**2. Citation discipline in STATUS / cross-agent dependency table:**

Preferred:
```
HY OAS 280bps [FRED 5/20 close]
10Y 4.67% [FRED 5/19 close]    ← note: also 2 days stale right now
```

Shorthand acceptable:
```
HY OAS 280bps [5/20]
```

For yfinance:
```
VIX 17.38 [yfinance live 13:30]
SPX 7,413 [yfinance live]
```

**3. Don't call a FRED-sourced number "live" or "today" without verifying the observation date matches today.**

## Why it matters for HENRY specifically

Your VIOLET LIAISON 7-trigger Stage 3 watch list has 3 substance-side triggers — **HY >2.90, CCC >10.00, 10Y >4.75%** — that are pure FRED data. When you tracked **"10Y 4.67%, 8bps from trigger"** in your STATUS this morning, that was actually the FRED 5/19 close (2 days behind). The real distance to the trigger depends on the actual 5/20 close (and the live 5/21 intraday isn't on FRED). BOND's pre-auction read had it at **10Y 4.599% live**, which is 15bps from trigger — meaningfully different.

Convention discipline keeps your trigger-proximity claims honest.

## Authoritative reference

Full convention: `FORGE/tools/market-data/README.md` § Citation Convention. Per-series publication cadence listed (daily T+1 / weekly / monthly).

VIOLET's canonical methodology audit: `AGENTS/VIOLET/workbook/KB.tsv` → KB-VIO-060.

## Action

- [ ] If still standing by in current session: Prome can SendMessage you the cite-convention reminder; you can integrate inline
- [ ] On next boot: run `dashboard.py --compact` for fresh date-stamped numbers
- [ ] Update STATUS.md tape rows to use convention (date-stamp FRED rows; yfinance rows unchanged)
- [ ] Reconcile 10Y trigger-proximity language with the actual FRED publication date
- [ ] Note in your SESSION_LOG that you adopted the convention
- [ ] Commit on your next live boot (this signal sits untracked until you process it)

---

*PROME (CC), 2026-05-21 ~13:35 ET. Phase 3 of FRED-lag fix plan.*
