# DRAFT: thesis-kill #2 names its instrument (D:L1112 main item)

**Status: DRAFT ONLY. Nothing is encoded.** Naming an instrument is a change to the letter, so PROME takes this to Will as a queue row; `workbook/EXIT_PROTOCOL.md` §1 row 2 stays byte-identical until his word.
**Author:** FALCON (Claude Code, Opus 5.5, desktop), 2026-11-18 about 10:40 ET, PROME prome-6e weekly wake. Flag first raised in FALCON's 11/11 packet, item 2.

## The current letter (EXIT_PROTOCOL v4 §1, row 2, verbatim)

> Hormuz verifiably reopened: mine clearance complete AND transits >50% of 88/day for 10 days

## What is wrong with it

| Gap | Why it matters |
|---|---|
| "88/day" names no instrument | 88 is the pre-war median of **one** series: IMF PortWatch, Strait of Hormuz, all vessel types, 2025-02-28 to 2026-02-27, n=365 (median 88.0, mean 90.7; KB-055). Other trackers give other baselines: the Hormuz Strait Monitor's is 97/day, and press figures of 130 to 140/day are the top of the daily range, not an average. A transit count from another tracker read against 88 would be graded against the wrong yardstick, and the error could run either way |
| "for 10 days" is ambiguous | It could mean every day for 10 days in a row, or a 10-day average. A single busy day could lift a 10-day average over the bar; the every-day reading cannot be met that way |
| No rule for a missing print | PortWatch publishes 5 to 8 days late and sometimes skips days. The letter does not say whether a gap breaks the count |

## Draft wording (for Will)

> **2. Hormuz verifiably reopened:** mine clearance complete AND, on the IMF PortWatch daily chokepoint series for the Strait of Hormuz (`Daily_Chokepoints_Data`, `portid = chokepoint6`, field `n_total`, all vessel types), a total of **45 or more transits on each of 10 consecutive calendar days**. 45 is the first whole number above half of 88/day, the median of this same series over 2025-02-28 to 2026-02-27. Grade only published print-days, on the series as it stands when graded. A calendar day with no print breaks the run. No other tracker's count substitutes; if PortWatch cannot be read, this limb is UNGRADEABLE, never graded on a substitute.

## Choices inside the draft (Will's to make)

| Choice | Recommended | Alternative | Why the recommendation |
|---|---|---|---|
| What "10 days" means | **Every one of 10 consecutive days at 45 or more** | 10-day average above 44 | The limb is meant to show the strait is *verifiably* open. Requiring every day means one convoy day cannot carry it |
| Which count | **All vessels (`n_total`)** | Tankers only (`n_tanker`) | 88 is an all-vessel median; switching to tankers needs a new baseline built from the same series, which would be a separate proposal |
| A missing print | **Breaks the run** | Skip it and keep counting | Errs toward *not* calling the war over; the cost is a later kill, not a false one |

## What it would read today

Nothing changes now: the limb is far from met under either reading. Newest print 2026-11-15 = **2/88** (own run of `hormuz_transit_watch.py`, 11/18). Over the war's 261 days (2/28 to 11/15), the series reached 45 or more on **3 days** (2/28: 57, 6/24: 51, 6/25: 46), and the longest run was **2 days**. War-period median: **4/day**. Thesis-kill stays **0/7**.

## Not in this draft

- **"Mine clearance complete" also names no authority.** Not drafted: outside D:L1112's scope. Flagged for a later row if Will wants it.
- No other kill row, threshold or route changes. The 88 baseline itself is unchanged: this draft names where it comes from and does not move it.
- If Will rules, FALCON encodes the text in EXIT_PROTOCOL §1 row 2 and updates the citing surfaces: STATUS and the thesis-kill lines in THESIS, the PortWatch script's docstring and FRESH_LEG_BASELINE row 2 if it is cited there.
