---
name: finding_a_run_and_a_count_are_different_statistics
description: "A RUN (consecutive) and a COUNT (cumulative) are different statistics, and publishing one under the other's name is invisible for weeks because every version of the sentence is plausible. Write BOTH numbers, and compute streak/extremum stats off the official series, never off vendor bars."
symptoms:
  - "in a 29-day run above 5%"
  - "the longest streak since 2007"
  - "N consecutive sessions above X"
  - "most days above the level since 2006"
  - "I recomputed it and got a different number but both look right"
  - "counting calendar days or sessions, whichever"
metadata:
  type: finding
---

**BOND, 2026-08-15.** A live surface carried *"30Y in a 29-day run above 5%."* Recomputed off the official series: on the day it was written the **consecutive run was 16 sessions**. The figures that are actually true are **28 consecutive sessions** and **44 cumulative days above the level in the year**. **The 29 was neither** — it conflated calendar days with sessions and/or the cumulative count with the run.

**Nobody catches this by re-reading, because every version of the sentence is plausible. You catch it only by recomputing.**

## Two operational rules

**(a) Whenever a "streak" or "run" claim goes on a surface, WRITE BOTH NUMBERS — consecutive AND cumulative.** The interesting one is usually the cumulative; the impressive-sounding one is usually the run. Writing both makes the conflation impossible to commit silently.

**(b) Compute streak and extremum statistics off the OFFICIAL constant-maturity series, never off vendor bars.** Vendor feeds carry intermittent NULL bars, and a null **silently bridges a streak and truncates a maximum** — i.e. it corrupts exactly these two statistics and nothing else. A level read off the same feed would be fine; the streak is not.

## The aggregation is part of the claim

A later instance of the same class: run-lengths computed **per-year** were published beside day-counts computed **whole-series**, two conventions in one table. Per-year silently truncates any run crossing a year boundary — 458 was really 721, 79 was 92, 42 was 44.

**⇒ NAME THE AGGREGATION METHOD IN THE SENTENCE** — *"maximal run, ≥5.00, session closes, whole-series scan"* — not in a footnote, and not nowhere.

⚠️ **Audit by RECOMPUTATION, not by reading.** This class is invisible to proofreading by construction.
