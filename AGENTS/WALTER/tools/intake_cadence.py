"""Shared weekday collector cadence; holidays are deliberately not modelled."""
import datetime as dt


def missed_weekday_runs(last_run_date, today):
    """Expected weekday runs strictly after last run through today inclusive."""
    n = 0
    day = last_run_date + dt.timedelta(days=1)
    while day <= today:
        n += day.weekday() < 5
        day += dt.timedelta(days=1)
    return n
