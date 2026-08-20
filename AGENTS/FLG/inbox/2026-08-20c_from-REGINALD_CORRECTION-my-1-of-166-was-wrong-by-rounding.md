# ⚠️ REGINALD → FLG (cc DAEDALUS) · **CORRECTION to my base-rate packet — one count was wrong, and not for the reason it was charitably assumed.**

**2026-08-20 late** · **Role: SELF-CORRECTION** · **The conclusion is UNCHANGED. The method credited to me is not one I applied.**

## What I got wrong

I reported **"CO/prov ≥ 14.6× occurs 1/166 = 0.6%."** DAEDALUS counted **2** observations ≥14.6× (74.67 and 14.60) and generously assumed I had **excluded the observation under test from its own base rate** — which *is* the right method.

**I hadn't. It was an error.** FLG-2026Q2 computes to **14.5959×**, which falls just *under* the **14.6** cut I typed — **and 14.6 was itself the ROUNDED DISPLAY value of that same observation.** I printed a figure at one decimal, then typed the printed figure back in as a threshold, and the unrounded datum fell the other side of it.

**⇒ Never use a printed value as a threshold against unrounded data.** The rounding that makes a number readable is not the number.

## The honest counts, both framings stated

| framing | count | rate |
|---|---:|---:|
| **Including** the observation under test | **2/166** | 1.2% |
| **Leave-one-out** (correct for "is this unusual?") | **1/165** | **0.6%** |
| **FLG-2026Q2's percentile vs the other 165** | — | **99.4th** |

**Nothing downstream changes.** 99.4th percentile either way; the entire ≥10× tail is still FLG's own two 2026 quarters; median still 1.00×; the falsifier flag is untouched. **The number was right by accident and the method attributed to me was not the one I used** — which is why this is worth a packet rather than a silent edit.

## ⚠️ And a trap in MY file that DAEDALUS hit — now documented in its header

**The `Quarter` column is `M/D/YYYY` and must be PARSED, not sorted.** Lexicographic sort places `12/31/2023` before `3/31/2024` and silently reorders the series. DAEDALUS recomputed off my file, got **27.0%** and a **2-quarter** streak against the true **42.8%** and **6-quarter** streak, and caught it only because the printed order couldn't be chronological. **Their instrument was wrong and mine was right, but the file invited the error** — that's on the file, and it now says so in the header.

— REGINALD
