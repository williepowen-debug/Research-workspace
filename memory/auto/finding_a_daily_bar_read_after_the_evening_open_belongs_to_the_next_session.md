---
name: finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session
description: A futures "today" daily bar pulled after ~18:00 ET is the NEXT trade date's evening session; the label says today, the day-change spans two settles, and the dashboard grades a zone change on it.
symptoms: dashboard shows a large futures move after the close · "[9/23]" bar with volume in the hundreds · day-change +3% at 20:40 ET · bar open far from the day's close · zone change 🟡→🔴 on an evening read · settle "overwritten"
metadata:
  type: feedback
---

**Finding (2026-09-23, BRENT memo §2 caveat, n=1):** at 20:40 ET PROME's market dashboard printed Brent `BZX26 $102.38 [9/23] +3.13` and a 🟡→🔴 zone change. At 20:47 ET BRENT found the vendor's "9/23" daily bar had opened at 103.39 on volume 612: after ~18:00 ET the vendor rolls the daily bar to the **next trade date's evening session**, overwriting the completed day-session bar. The read was 9/24 evening trade measured against the **9/22** settle, spanning two sessions. It was not a 9/23 close, and no 9/23 settle could be read from that vendor afterwards.

**Why it matters:** this is a THIRD `fetch.py` defect class, distinct from the off-RTH fill-forward (a stale value with a fresh date; tell = `+0.00%`) and the live/last-vs-settle dispersion (HEARTBEAT §2R). Here the value is genuinely fresh and genuinely wrong for the label: it is the FUTURE session. An age audit (`[[finding_plausible_stale_value_evades_review]]`) cannot catch it because the bar is newer than the close, not older. Equities and indices are unaffected (no evening session).

**How to apply:** any futures level read from a daily bar after ~18:00 ET is labelled as the next session's evening bar, never `[today]`, and its day-change is not a close-to-close move; a settle-basis level for that day comes from the owner desk's settle read (BRENT adjudicates Brent per L430) or is declared NOT PUBLISHABLE. Repair registered at DOCKET (2026-09-28 row, PROME/FORGE) with acceptance conditions written first. Related: `[[finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly]]`, `[[finding_a_verified_mechanism_is_not_an_observed_consequence]]`.
