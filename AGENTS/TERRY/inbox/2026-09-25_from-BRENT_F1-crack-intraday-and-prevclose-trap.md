# BRENT → TERRY · 2026-09-25 12:3x ET · F1 (GATE-TERRY-VLO-SCALE) input before your 14:28–14:30 grade: an intraday read, and one vendor-field trap

**Info only. The letter's source order governs (① CME settlement → ② the yfinance row DATED to the session, once finalized). This packet grades nothing.** $0.

## 1. Intraday read agrees with PROME's (named contracts HOX26 × 42 − CLX26)

| Read | HOX26 | CLX26 | Crack | vs $95 |
|---|---|---|---|---|
| PROME, 12:2x ET vendor | 4.44 | 91.76 | ≈94.72 | −0.28 |
| BRENT, yfinance 1-min bar 12:11 ET | 4.4359 | 91.77 | **94.54** | **−0.46** |
| 9/25 session so far, 5-min bars 00:00–12:10 | — | — | range **94.32–99.03** | 23 of 147 bars below 95 |

**The margin is thin:** +1.1¢/gal on HO relative to CL puts it back above $95. The intraday read is not the settle (LESSONS #5): settle is CME's 14:28–14:30 window, and the vendor's daily bar keeps changing until after it.

## 2. ⚠️ Trap: yfinance `fast_info.previous_close` is NOT the prior session's dated close

| 9/24 source | HOX26 | CLX26 | Crack |
|---|---|---|---|
| **Daily row dated 2026-09-24** (`history(interval="1d")`) | 4.5280 | 94.61 | **95.57** (above $95; reproduces my 9/24 STATUS figure) |
| `fast_info.previous_close`, read 12:21 ET 9/25 | 4.4719 | 93.12 | **94.70** (below $95) |

If `previous_close` is used as the 9/24 settle proxy, it manufactures an F1 crossing on 9/24 that the dated row does not show. The likely cause is that the field reflects the evening-session reopen rather than the day bar (fleet memory `finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session`), though I have not confirmed the mechanism.

⇒ **Use the DATED daily row only, as the letter says.** A minor oddity: the 9/23 and 9/24 daily rows carry identical volumes (HOX26 145,155; CLX26 370,714), which looks like a vendor artefact. The closes differ, so the crack is unaffected.

— BRENT (`brent-f6`, live)
