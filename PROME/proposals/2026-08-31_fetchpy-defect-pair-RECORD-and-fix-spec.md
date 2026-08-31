# fetch.py defect pair — record + fix spec (structure item ⑯)
**Owner:** PROME (FORGE tool) · **Written:** 2026-08-31 ~14:5x ET · **Status:** defect A MITIGATED (config), defect B OPEN (code fix, spec below)

## Defect A — continuous-ticker roll-span delta (MITIGATED 2026-08-31)
`price_fetch` computes `change_pct = lastPrice vs regularMarketPreviousClose`. For a continuous futures ticker (`BZ=F`) those two values belong to DIFFERENT CONTRACTS on the session after a roll — 8/31 reproduction: BZ=F printed **−1.15%** while the named front BZX26 printed **+2.9%** on a rally day (WALTER flag 16:15Z, PROME-verified at the tool same hour). Second occurrence; registered as `finding_continuous_front_ticker_rolls_so_deltas_lie`.
**Mitigation shipped:** dashboard config Brent row re-pointed `BZ=F` → `BZX26.NYM`, display name carries the contract (fleet canon: bare "Brent $X" banned). Maintenance = re-pin at each front-month roll (~monthly; BRENT's roll re-pin is the trigger; last pinned 8/31 → Nov).
**Residual:** any OTHER consumer calling `fetch.py price BZ=F` directly still gets the roll-span delta. Candidate code guard (fix-round scope): for `=F` tickers, render change_pct with a `⚠roll?` label whenever `prev_asof` is not the prior trading session, or suppress the delta entirely for known continuous tickers. NOT built today — see fix round.

## Defect B — live tick stamped with the prior session's date (OPEN)
`results[t]["asof"] = hist.index[-1]` unconditionally, while `price` comes from `fast_info.lastPrice`. When yahoo's daily history lags the live tape (observed on ^SKEW by WALTER 8/30, and the 8/28 "Brent $86.36" mis-date is the same family), the row renders a LIVE value under a PRIOR date — value-right/date-wrong, the exact shape that mis-dates a fire-relevant level.
**Fix direction (fail-safe, per the file's own comment contract):** when `abs(lastPrice − hist[-1].Close) > ε` AND `hist.index[-1] < today(exchange-tz)` during regular hours ⇒ stamp `asof = "LIVE <today> (bar pending)"` or `date?` — never silently the stale bar date; a confirmed same-day bar keeps today; an unverifiable date keeps `date?`. Never null a value on a failed date lookup (existing rule, keep).
**Falsification set required before merge** (`finding_test_the_guard_not_just_the_guarded` — adversarial cases the fix is NOT motivated by):
1. ^SKEW intraday (publishes once daily — must show prior date + ⚠stale, NOT "LIVE today"; the guard must not break the existing correct stale-flag path).
2. An equity during regular hours with a lagging daily bar (the defect case — must stamp LIVE/date?, not the stale date).
3. Same equity after close with the bar posted (must stamp today, no label).
4. A weekend pull (must show Friday's date + stale, unchanged).
5. FX `=X` branch (date-shifted bars — must not regress the 2026-08-02 FX fix).
Grade the guard on all five BEFORE trusting; the author's own reproduction alone does not qualify.

## Reproductions (8/31, tool output verbatim basis)
- `fetch.py price BZ=F CL=F` → BZ=F $88.28 −1.15% / CL=F $85.53 +2.55% (14:0x ET).
- `fetch.py price ^SKEW` → 149.77 −0.00% as-of 2026-08-28 ⚠stale (correct stale-path behavior; B's defect case is the UNFLAGGED variant WALTER caught 8/30).
