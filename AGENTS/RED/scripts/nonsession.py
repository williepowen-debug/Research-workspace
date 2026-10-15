"""Market non-session calendar for RED's sustain counters. ONE home for both tools.

Will-approved 2026-10-14 (S52, CHG-051 review proposal P1): a FRED bar dated on a day the
underlying market was CLOSED is a NON-SESSION. It is excluded from the count domain and the
run BRIDGES it, which is FT-10's S41 ruling (2026-09-06) applied registry-wide.

Why it exists, measured 2026-10-14: FRED's ICE BofA OAS series and VIXCLS carry bars on
market holidays. HY 2.68 [9/4] = 2.68 [9/7, Labor Day]; HY 3.11 [10/9] = 3.11 [10/12,
Columbus Day, SIFMA full close]; CCC 8.88 [2025-11-10] = 8.88 [2025-11-11, Veterans Day];
VIXCLS printed 15.30 on 9/7 with NYSE closed. boot.py counted those bars as sessions, so an
HY close >320 on Tue 11/10 plus the Veterans Day forward-fill on Wed 11/11 would have put
TWO of FT-02's three observations on one session.

The rule is CALENDAR-based, never "value equals the prior bar". Labor Day's CCC bar
(10.55 vs 10.54) was not a copy, and a real session can repeat a value.

Calendars:
  nyse - NYSE full-day holidays (VIXCLS)
  bond - NYSE holidays PLUS the SIFMA full-close days that NYSE trades through (Columbus
         Day, Veterans Day), for the ICE BofA cash-bond OAS series.
Known simplification, stated so nobody has to rediscover it: Good Friday is treated as a
bond non-session (SIFMA usually recommends an early close, occasionally a full one), and a
Saturday Veterans Day is not moved to the Friday.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta

SERIES_CALENDAR = {
    "BAMLH0A0HYM2": "bond",   # HY OAS        (FT-01/02/12, WL-03/04)
    "BAMLH0A3HYC": "bond",    # CCC OAS       (FT-07, WL-05/06)
    "BAMLH0A1HYBB": "bond",
    "BAMLH0A2HYB": "bond",
    "BAMLC0A0CM": "bond",
    "VIXCLS": "nyse",         # VIX close     (FT-06)
}


def us_market_holidays(y):
    """Standard US equity-market holidays for year y (observed rule for fixed dates).

    Moved VERBATIM from boot.py `_us_market_holidays` (S41) on 2026-10-14 so that boot.py and
    base_rate_review.py share one calendar. boot.py re-imports it under its old name.
    """
    def nth(m, wd, k):
        d = date(y, m, 1); d += timedelta(days=(wd - d.weekday()) % 7)
        return d + timedelta(weeks=k - 1)
    def last(m, wd):
        d = date(y, m, 31) if m != 5 else date(y, 5, 31)
        while d.weekday() != wd:
            d -= timedelta(days=1)
        return d
    def obs(d):
        return d - timedelta(days=1) if d.weekday() == 5 else (d + timedelta(days=1) if d.weekday() == 6 else d)
    a = y % 19; b_ = y // 100; c = y % 100; d_ = b_ // 4; e = b_ % 4
    f = (b_ + 8) // 25; g = (b_ - f + 1) // 3
    h = (19 * a + b_ - d_ - g + 15) % 30; i_ = c // 4; k_ = c % 4
    l = (32 + 2 * e + 2 * i_ - h - k_) % 7; mm = (a + 11 * h + 22 * l) // 451
    easter = date(y, (h + l - 7 * mm + 114) // 31, ((h + l - 7 * mm + 114) % 31) + 1)
    out = {obs(date(y, 1, 1)), obs(date(y, 7, 4)), obs(date(y, 12, 25)),
           nth(1, 0, 3), nth(2, 0, 3), last(5, 0), nth(9, 0, 1), nth(11, 3, 4),
           easter - timedelta(days=2)}
    if y >= 2021:
        out.add(obs(date(y, 6, 19)))
    return out


def bond_extra_closures(y):
    """SIFMA full-close days on which NYSE is OPEN: Columbus Day and Veterans Day."""
    d = date(y, 10, 1)
    d += timedelta(days=(0 - d.weekday()) % 7)          # first Monday of October
    columbus = d + timedelta(weeks=1)                     # second Monday
    vet = date(y, 11, 11)
    out = {columbus}
    if vet.weekday() < 5:
        out.add(vet)
    elif vet.weekday() == 6:
        out.add(vet + timedelta(days=1))                  # Sunday -> Monday observed
    return out


def _as_date(x):
    if isinstance(x, date):
        return x
    return datetime.strptime(str(x)[:10], "%Y-%m-%d").date()


def is_nonsession(series_key, d) -> bool:
    """True iff `d` is a weekend or a closed-market day for this series' calendar.
    Series without a declared calendar are never filtered (fail open = unchanged behaviour)."""
    cal = SERIES_CALENDAR.get(series_key)
    if cal is None:
        return False
    d = _as_date(d)
    if d.weekday() >= 5:
        return True
    if d in us_market_holidays(d.year):
        return True
    return cal == "bond" and d in bond_extra_closures(d.year)


def drop_nonsessions(series_key, obs, date_field="date"):
    """Filter a FRED observation list (dicts with a date field) to real sessions only."""
    if series_key not in SERIES_CALENDAR:
        return list(obs)
    return [o for o in obs if not is_nonsession(series_key, o.get(date_field, "1900-01-01"))]
