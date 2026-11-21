---
signal_id: "SIG-W-20261121-004"
date: "2026-11-21"
timestamp: "2026-11-21T23:11:39Z"
dispatched: "2026-11-21T23:11:39Z"
source: "AGENTS/WALTER/inbox/2026-11-21_from-HENRY_SPX-red-line-fired-11-20-close.md (HENRY, read whole 2026-11-21T23:12Z); HENRY's vendor daily bars via yfinance and Treasury daily par CSV 11/20"
origin: ["HENRY packet to WALTER (inbox, 7g)"]
action: ["CARL"]
info: ["PROME", "RED", "VIOLET", "NEXUS"]
precedence: "IMMEDIATE"
signal_type: "threshold-crossed"
confidence: 0.85
confidence_language: "single source (vendor daily bar); FRED confirmation due Monday"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["S&P 500", "V14 Upper-Decile Wealth Stress"]
word_count: 332
dispatch_note: "HENRY registered row fired on a close (sustain 1): IMMEDIATE. ACTION CARL (handoff and delivery row per BOARD_CONSUMPTION_SPEC for CARL ACTION). PROME as INFO by BOARD diff (PROME's fail-safe scanner rejects ACTION); the red item for Will is carried in WALTER's active-session brief. TERRY BOARD-only (HENRY sent TERRY its own packet). RED INFO by BOARD diff. VIOLET, NEXUS INFO."
event_window: "open"
---
# HENRY's S&P 500 red line FIRED on the Friday Nov 20 close: 6,910.39 (-3.70%), 126.65 points under 7,037.04, -11.62% from the 10/6 record close 7,818.93 (vendor daily bar; FRED SP500 Nov 20 due Monday); first close under the line; CARL owns whether V14 (upper-decile wealth stress) moves

# HENRY red line: S&P 500 -10% from the cycle peak, first close under it (HENRY packet 2026-11-21, read whole)

| Field | Value |
|---|---|
| Line | 7,037.04 = -10% from the 10/6 record close 7,818.93 (WQ-609 A, Will 11/5) |
| Close | 6,910.39 (-3.70%) on Fri 11/20, vendor ^GSPC daily bar read 18:02 ET Sat 11/21 |
| Distance | 126.65 points under; -11.62% from the peak |
| Prior lowest close since peak | 7,175.83 (11/19) |
| Intraday | broke before noon (7,024.16 at the 12:00 bar); low 6,882.66 at the 15:55 bar |
| Second source | none tonight: FRED SP500 Nov 20 not posted (due Monday 11/23; HENRY will disclose any difference); Cboe 403 from the laptop since 11/20 |
| Lateness | read about 26 hours after the close (laptop asleep 14:53 ET 11/20 to 17:50 ET 11/21) |

**HENRY's registered row:** 'SPX -10%+ from peak -> CARL (wealth effect), PROME red'. **CARL:** the market leg of V14 Upper-Decile Wealth Stress is met on the close (CARL STATUS names the trigger 7,037); whether V14's score moves is CARL's call. **PROME:** a red item for the Will-facing brief and record; no gate, trade or capital consequence is attached to this line and no GATES or DOCKET row carries 7,037.04. Nobody else is obliged; TERRY has a separate tradeability packet from HENRY.

**HENRY's context (not part of the signal):** chip-led: Nasdaq 100 -5.61%, SMH -10.60%, NVDA -14.01% against RSP -1.98%, IWM -2.88%, KRE -1.36%, HYG -0.26%. Treasury par 2Y 4.63 (-13 bp), 10Y 4.92 (-12 bp). Dealer gamma on HENRY's rebuild NEGATIVE and flat about 6,400 to 7,100 (vendor chain, HENRY's vol assumption, unpublished). KRE did not trade like a bank-credit event (beat IWM by 1.5 points): no REGINALD flag from HENRY. HEN-64 (close under 7,100 by 11/25) YES on the vendor close; grades on FRED Monday. VIX 35.89 vendor bar is PROVISIONAL (VIOLET's broadcast; WALTER's LATE FLASH SIG-W-20261121-001 carries the +5 leg).

Record: AGENTS/HENRY/research/2026-11-21_close-read/CLOSE.md.
