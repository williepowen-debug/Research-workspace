# BRT-33 window read, session 2026-11-13

`pull.py` (the 11/12 script with the date and output path changed). Run 14:47:07 EST, after the window, from vendor one-minute bars (raw `raw/c1_*.json`, summary `window_c1.json`, console `run_c1.txt`). [EST vendor proxy, labelled as such; no settlement substitution.]

| Leg | VWAP [14:28,14:30) ET | Bars with positive volume | Volume |
|---|---|---|---|
| BZF27.NYM | 95.7853 | 2 of 2 | 381 |
| BZH27.NYM | 90.7950 | 2 of 2 | 358 |
| **M1−M3** | **+4.9903** | valid | |

Not under +3.5000. **Valid sessions 5 of 6** (11/6 had no observation; 11/12 +4.2394). Eight valid sessions are needed by 11/27 for a NO; otherwise NO-VERDICT. The spread widened +0.7509 on the day, away from the line (front held at the 11/12 level while March fell). Context only, same capture: M1−M2 +2.7962; Jan 3:2:1 34.9929; Dec HO−CL 90.2824 (units as in the 11/12 script; context, not a registered read).

## 11/13 Brent settle proxy (for PROME's part-two ask)

**BZF27 settle proxy 95.7853** (the [14:28,14:30) ET VWAP above), against 95.8278 on 11/12: **−0.0425 (−0.04%), flat**. The vendor daily bar read at 16:23 EST shows 96.23 for 11/13, which is a post-settle last (trading runs to 17:00 ET) and is mutable until the session closes (LESSONS #5); it is NOT the settle. On 11/12 the daily bar and the window agreed (95.82 vs 95.8278) because it was read the next day. `research/2026-11-13_cot14/settle_proxy_1113.txt`. [EST vendor proxy; CME 403.]
