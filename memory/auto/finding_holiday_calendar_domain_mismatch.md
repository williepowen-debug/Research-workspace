---
name: finding_holiday_calendar_domain_mismatch
description: pandas USFederalHolidayCalendar does NOT contain Good Friday, but bond and equity markets close for it — a business-day rule built on the federal calendar demands data from a day markets never published
metadata:
  type: reference
---

**`pandas.tseries.holiday.USFederalHolidayCalendar` does not include Good
Friday.** Verified on this box 2026-07-27:

```
Good Friday 2026-04-03 in USFederalHolidayCalendar? False
Good Friday 2027-04-02 in USFederalHolidayCalendar? False
2027-04-05 (Mon) - CustomBusinessDay(USFederalHolidayCalendar) = 2027-04-02
```

Good Friday is the one **market** holiday that is not a **federal** holiday
(SIFMA-recommended bond close; NYSE closed; Treasury posts no curve). Every
other market close in the US calendar — July 4th, Memorial Day, Labor Day,
Thanksgiving, Christmas, New Year, MLK, Presidents, Columbus, Veterans — is
federal, so the two calendars agree on all of them **and a fixture built from
them will pass while the gap survives.**

**Consequence:** any "newest observation that could exist = previous business
day" rule built on the federal calendar will, on the Monday after Good Friday,
demand an observation from a day no daily market series published — producing
either a permanent refetch loop or, worse, a **false "stale" alarm that cries
wolf once a year.**

**How to apply:** when picking a holiday calendar, ask which **domain** the data
comes from, not which calendar is nearest to hand. Market data wants a market
calendar (`pandas_market_calendars`, or federal + an explicit Good Friday rule);
payroll/government series want the federal one. **And build the fixture from the
case that DISAGREES** — verifying against July 4th and Memorial Day proves only
that the two calendars overlap where they were always going to overlap
([[finding_verify_fix_against_capable_case]]).

**The parent class, which is the durable part:** *calendar arithmetic applied to
a business-day domain.* VIOLET found **two independent instances in one agent**
on 2026-07-27, both failing **only on Mondays** and neither ever erroring —
`thresholds.py` asked for `today − 1 calendar day` → Sunday → no settlements → 8
of 12 Mondays silently blank; `fred_fetch.py` accepted a cache within 4 calendar
days → reached back only to Thursday → Friday's credit print was never demanded.
**Both presented a confident stamp on stale data, which is why they survived
months of weekly review.** The detector that finds these is on the DATA side,
not the code side: **a Monday or post-holiday row that is blank or unchanged.**
A grep for `timedelta(days=` misses `DateOffset`, positional `timedelta(1)`, and
tolerance constants like `FRESH_TOLERANCE_DAYS` — which was the actual carrier.
Related: [[finding_weekday_assumed_never_evaluated]], [[finding_date_gate_beats_weekday_name]].
