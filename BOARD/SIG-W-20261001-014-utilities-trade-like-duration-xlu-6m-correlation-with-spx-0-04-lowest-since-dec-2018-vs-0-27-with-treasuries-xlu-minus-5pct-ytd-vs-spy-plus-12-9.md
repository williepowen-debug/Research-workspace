---
signal_id: SIG-W-20261001-014
date: 2026-10-01
timestamp: 2026-10-01T16:46:11Z
time_dispatched: 2026-10-01T16:46:11Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 8-image batch 2026-10-01 ~16:42Z (msgs 4805-4812), batch manifest BM-20261001-02
origin: ["Will Telegram photo (msg 4808): X @LHMacro (Lighthouse Macro) 9/30 20:01 ET; chart: rolling 126-trading-day correlation of XLU daily returns with SPY and with Treasury prices (10Y yield change, sign flipped), Jun 1999-Sep 29 2026; data Yahoo Finance + Fed H.15"]
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
entities: ["XLU", "SPY", "UST 10Y", "126-day correlation"]
confidence: 0.6
confidence_language: "The account's own computation, not re-derived by WALTER; a low-reach account (42 views). Method is stated and standard."
signal_type: context
safety_net: clear
verdict: "Per Lighthouse Macro (data through 9/29): utilities' (XLU) 6-month correlation with the S&P 500 is 0.04, the lowest since Dec 2018 (1st percentile since 1999), vs 0.27 with Treasury prices. XLU is -5.0% YTD vs SPY +12.9%. The sector is trading like duration, not equity, in a year of rising long yields."
precedence: ROUTINE
action: []
info: ["HENRY", "WATT", "VULCAN"]
dispatch_note: "Source: Will-Telegram 8-image batch 2026-10-01 ~16:42Z (msgs 4805-4812), batch manifest BM-20261001-02, item 4. 'Already ours?' No XLU line in HENRY or WATT STATUS. MARKET_VOL index-mechanics (correlation regime) -> HENRY info; WATT info (utility sector / rate-case cost of capital); VULCAN info (power-demand equities are the usual bull case for utilities, and this says rates dominate). Not the safety-net correlation-break trigger (that is a >0.3 drop in a correlated pair as an event; this is a six-month drift). ROUTINE, info only."
---

# Utilities are trading like bonds, not stocks. XLU's 6-month correlation with the S&P 500 is 0.04, the lowest since 2018 (Lighthouse Macro).

- **XLU vs S&P 500, 126-day correlation: 0.04**, the lowest since December 2018 (1st percentile since 1999).
- **XLU vs Treasury prices: 0.27.**
- **YTD (to 9/29): XLU −5.0%, SPY +12.9%.**

**So what:** in a year when long yields keep rising, utilities are behaving like a long bond. **The AI-power-demand story is not what is moving them right now; rates are.** That matters for anyone holding utilities as a power-demand play.

## Caveats
- The account's computation, not re-derived. Low-reach account; the method (126-day rolling correlation, Yahoo + H.15) is standard.
- A six-month drift, **not** the routing safety net's sudden correlation break.

Info only.
