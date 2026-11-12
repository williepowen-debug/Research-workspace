# USD/JPY 160 — handoff to the 19:00 ET grading session (WQ-680, C9)

**Written 2026-11-12 16:49 ET (clock), closeout on PROME's ask (Will 16:48 ET: close SAM, respawn about 18:50 ET).** The row is **UNGRADED**. The fresh session grades it once; nothing here grades it.

## The row and its rule

- **Row:** STATUS § KEY THRESHOLDS, "USD/JPY 160 / <155 / <147". These are investigation levels with **no automatic entry**, and no retired gate is re-armed.
- **Rule (letter):** `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS (WQ-162):
  - Series: yfinance `USDJPY=X`, 1-hour bars aggregated to sessions labelled in **Europe/London**.
  - **COMPLETED sessions only**; "the current bar is never scored".
  - Observations are taken as last revised (30-day upsert window, `usdjpy.py --revise-window`).
  - This is NOT the BOJ 17:00 JST fix and NOT the MOF basis.
- **The 11/12 London session completes at 00:00 London = 19:00 ET.**

## What is already observed (intraday, NOT a grade)

| Item | Value | File |
|---|---|---|
| Touch | **160.044 high at 11:41 ET** (1-minute bar O 160.018 / H 160.044 / L 160.018 / C 160.037); 160.040 at 11:42 | `USDJPY_1m_1130-close.csv` |
| Drop | **11:43 ET bar O 160.003 / H 160.008 / L 159.303 / C 159.588 (range 0.705)**, yen-wide (EUR/JPY, GBP/JPY, AUD/JPY fell together; EUR/USD 1.106 flat) | the five `*_1m_1130-close.csv` files |
| Partial London session (hourly, 22 bars to 21:00 London) | **H 160.044 (16:00 London bar) / L 159.303**; last bar 21:00 London C 159.831 | `USDJPY_1h_london_20261112_partial.csv` |
| After 11:50 ET | range 159.551–159.898, no one-minute range ≥0.25 yen, **no reprint ≥160.00 through 16:48 ET** (in-session watch, stopped 16:48 ET) | — |
| Prior completed session, 11/11 | O 158.709 / H 159.938 / L 158.659 / **C 159.743** (`workbook/USDJPY.tsv`) | — |

## What the grade still has to observe at completion

1. **Run `usdjpy.py` (or `boot.py`) after 19:00 ET** so `workbook/USDJPY.tsv` takes the **11/12 completed row**. Read the session **High and Close from that row**, not from the minute file. Vendor revisions can move a bar.
2. **Touch:** a completed-session **High ≥160.00** records a completed-session TOUCH of 160. On the saved bars this is 160.044, but confirm it on the revised hourly series.
3. **Close:** a completed-session **Close ≥160.00** records a CLOSE above 160. At 21:00 London it was 159.831, so the session's remaining bars decide this.
4. **Speed row:** check the session range against "≥1.5–2%/day or ~2–3 yen in 1–2 sessions". The partial range is 0.741 yen (160.044 − 159.303), not fired.
5. **Packet rule (PROME 11:5x ET):** send **ONE** packet only if the completed session records a touch or a close at or above 160, or if an official acts or speaks. On the saved bars a touch is likely, so expect one short packet.

## Officials (as of 16:48 ET)

- **Katayama:** ESTABLISHED as Minister of Finance (MOF Japanese `about_mof/ministers_profile/index.htm`, read 11/12).
- **Mimura:** REPORTED only as 財務官 (no MOF page names him; the officials pages return 404). His 11/12 "too fast / too early to forget the summer" came on Thursday in Tokyo, BEFORE the cross.
- **Nothing tied to 11:43 ET.** No rate check or intervention is ESTABLISHED or REPORTED. Searches were run at 11:44, 11:50 and 13:09 ET.
- **MOF statements:** none since 8/3.
- **BOJ:** Asada (Nagasaki, 11/12) was dovish on pace, with no currency warning.

## Funding-line correction (carried; already delivered)

My first read (62d87fd10c) said MOF "draws first on deposits and repo before selling securities". **That was wrong.** After July–August, reserve **securities fell $87.8B against deposits −$6.9B**. These are month-end holdings, valuation included, and **not identified Treasury sales**.

- Corrected in the full packet (3607f04e92) and sent to BOND directly (7427197c94).
- PROME replaced its own BOND line (7af3437f13).
- Reserves on 10/31: $1,179.1B; securities $834.6B; deposits $150.7B.

## Measurement calendar (what can show an official operation)

| Date | Instrument | Covers the 11/12 move? |
|---|---|---|
| 11/12 16:30 ET | FRBNY H.4.1, foreign-official custody (Wed 11/11 levels) | No: the baseline |
| 11/13 | FRBNY Q3 FX quarterly (July–August US account split) · CFTC 11/10 window | No |
| ~11/17 JST | BOJ current-account fiscal factors: settlement of an op dealt 11/12 NY / 11/13 JST (playbook S1-A) | Yes, as a residual. A missed forecast is not a size. |
| 11/19 | H.4.1 (11/18 levels) · MOF weekly flows (week 11/8–14; designated investors, not the reserve account) | First custody print after the move |
| 11/18 | US TIC September | No |
| **~11/30** | **MOF monthly intervention total (10/29–11/26)** | **The only official confirmation** |
| early Dec | MOF reserves, November | Securities/deposits split |

Packets: `PROME/inbox/processed/2026-11-12_from-SAM_usdjpy-160-first-read.md`, `..._full-packet.md`.
