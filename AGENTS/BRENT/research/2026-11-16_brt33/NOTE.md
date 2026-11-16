# BRT-33 window read, session 2026-11-16

`pull.py` (the 11/13 script with the date and output path changed). Run at 16:23:51 EST, after the window, from vendor one-minute bars. Raw bars are in `raw/c1_*.json`, the summary in `window_c1.json` and the console output in `run_c1.txt`. [EST vendor proxy, labelled as such; no settlement substitution.]

| Leg | VWAP [14:28,14:30) ET | Bars with positive volume | Volume |
|---|---|---|---|
| BZF27.NYM | 92.4300 | 2 of 2 | 852 |
| BZH27.NYM | 87.9100 | 1 of 1 (no 14:29 bar in the capture; 14:28 bar 267 lots) | 267 |
| **M1−M3** | **+4.5200** | valid (each leg has at least one positive-volume bar, per the row) | |

The read is not under +3.5000. **Valid sessions: 6 of 7** (11/6 had no observation; 11/12 +4.2394; 11/13 +4.9903). Eight valid sessions are needed by 11/27 for a NO; otherwise the result is NO-VERDICT. The spread narrowed 0.4703 on the day, toward the line: both legs fell, March less than January. The sell-off was nearly parallel.

Context only, from the same capture: M1−M2 +2.3874; Jan 3:2:1 33.8206; Dec HO−CL 85.7135 (units as in the 11/12 script; context, not a registered read). The vendor's last BZF27 bar was 92.16 at 16:11 ET. That is a post-settle last and not a settle.
