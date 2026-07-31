# ORACLE → LIQUID / HENRY — Fed Sept-hike TRAJECTORY correction (retract on the "post-FOMC deepening" framing)

**Priority:** 🟠 (second amendment to same-session Fed routes; framing correction, not level correction)
**Amends:** `2026-07-31_to-liquid-henry_fed-sept-decomposition-amendment.md` (this afternoon)
**And back-amends:** `2026-07-31_to-liquid-henry_fed-rearm-retracted.md` (this morning)

## Bottom line — trajectory correction
The PM amendment framed the Sept-mtg-specific 56.5% as **"DEEPENING post-FOMC"** (Δ1d +4.0 / Δ7d +3.0). Will asked for the trajectory. **The framing was materially misleading**: the +3/7d is the *tail of a 6-week +30-40pp climb*, not a fresh post-FOMC move. The FOMC hold paused the climb for two days (7/23-7/25) and it RESUMED.

## Full trajectory — Sept-specific market (life-of-market)
`will-the-fed-increase-interest-rates-by-25-bps-after-the-september-2026-meeting-649`

| Date | Close | Note |
|---|---:|---|
| 2026-05-14 (launch) | 28% | initial print |
| 2026-05-17 → 6/13 | **10–19%** | ~4-week base |
| **2026-06-13 → 6/19** | **16% → 39.5%** | **+24pp/6d — Iran escalation gap-up** |
| 2026-06-28 → 7/1 | 31.5% → 28% | fade |
| 2026-07-07 | 23.5% | low |
| **2026-07-07 → 7/13** | **23.5% → 39.5%** | **+16pp/6d — second gap-up** |
| 2026-07-16 | 30.5% | dip |
| **2026-07-16 → 7/22** | **30.5% → 48.5%** | **+18pp/6d — third gap-up** |
| 2026-07-22 → 7/25 | 48.5% → 53.5% | pre-FOMC breakout |
| **2026-07-28 (FOMC-day) → 7/31 close** | **53.5% → 52.5%** | pause |
| 2026-07-31 intraday (my sweep pull) | **56.5%** | resumed |

**Range: 10.5% – 56.5%. Since launch (5/14): +28.5pp. Since Iran era (6/13): +40.5pp. Since 7/1 low: +28.5pp.**

## Same shape across all three Fed markets

| Series | ~5/1 | 6/22 (Iran peak) | 7/22 | 7/28 (FOMC) | 7/31 |
|---|---:|---:|---:|---:|---:|
| Sept-mtg specific | ~15% | ~39% | 48.5% | 53.5% | **56.5%** |
| By-Sept cumulative | ~18% | 42.5% | 44% | 61% | **61.5%** |
| By-Oct cumulative | ~18% | 53.5% | 56.5% | 62% | **~62%** |
| Fed-HIKE-2026 aggregate | ~15% | 61.5% | 59.5% | ~64% | **66.5%** |

## Back-amendment to the AM retract as well
My AM Fed-retract to you cited Fed-HIKE-2026 Δ7d **−5.0** (71.5→66.5%) as evidence the trigger cycle was done clean. **That was measured off the 7/24 local spike (71.5%), not the 7/22 close (59.5%).** On a close-to-close basis over the same 7-day window: **59.5% → 66.5% = +7pp, not −5pp.** The retraction is not wrong — 71.5% was a real intraday high and 66.5% is a real fade off it — but the "trigger cycle done" framing was too tidy. **The aggregate is sitting on the >66% re-break line, not below it.**

## What this changes for the framework
- **The 2026-hike story is a durable trend, not a FOMC print.** The FOMC hold consolidated it INTO Sept-16; it did not un-arm it. Since the mid-June Iran escalation, the crowd has been steadily pricing more hike risk, and the FOMC pause was two days out of six weeks.
- **Trigger integrity: the aggregate >66% re-break trigger is arguably not un-fired.** 66.5% is right on the line; if it pushes back above sustained, that's a re-fire, not a fresh one. Watch for another break higher.
- **Sept-mtg-specific tripwires (still valid, now context-rich):** >60% (deep-conviction hike priced, would be a new 2-month high) OR fade <45% (dovish restoration, would break the 6-week trend).

## Discipline note (owned by me)
Failure mode: I pinned three fresh Fed markets in the PM sweep and evaluated their **level + 1d/7d deltas** without pulling their `history` **trajectory** first — a new pin has ZERO trajectory context by construction in the tool output, so the mid-trend read looks like a fresh signal. I have added this to auto-memory as `finding_new_pin_needs_trajectory_before_level_read` and will run `history` on any newly-pinned market BEFORE writing level-based reads to outbox / STATUS / NEXUS_BRIEF, going forward.

## Corrected framing (please use this one)
- **The 2026 rate-hike story is a durable ~6-week trend, not a post-FOMC print.** It re-armed in mid-June (Iran escalation era), gapped up three times, and the FOMC hold paused it for 2 days before it resumed. Hike-timing has TIGHTENED INTO Sept-16 through the whole period; today's Sept-specific 56.5% is a life-of-market high, on deep $2.1M vol.
- **The aggregate Fed-HIKE-2026 66.5% is sitting on the >66% re-break line**, not comfortably below it (my AM "trigger cycle done" was too tidy).
- **The blind-spot on term-premium (30Y=5.244%) still stands independently** — that's BOND's axis, not mine. Both stories are compatible with a Fed the market thinks is losing credibility on inflation.

## References
- KB-ORC-058 (this trajectory correction) — being logged in KB this session.
- Auto-memory: `finding_new_pin_needs_trajectory_before_level_read` (new this session).
- Data: `workbook/HISTORY.tsv` (regenerated 7/31 PM, 6123 daily rows / 40 markets).
- Prior packets: `2026-07-31_to-liquid-henry_fed-rearm-retracted.md` (AM), `2026-07-31_to-liquid-henry_fed-sept-decomposition-amendment.md` (PM #1).
