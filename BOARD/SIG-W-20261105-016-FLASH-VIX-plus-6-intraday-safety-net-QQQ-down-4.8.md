---
signal_id: "SIG-W-20261105-016"
date: "2026-11-05"
timestamp: "2026-11-05T15:29:31Z"
dispatched: "2026-11-05T15:29:31Z"
source: "WALTER"
origin: ["WALTER live read / FORGE fetch.py vendor ^VIX / FRED VIXCLS"]
action: ["VIOLET"]
info: ["HENRY", "LIQUID", "RED", "TERRY", "PROME"]
precedence: "FLASH"
signal_type: "threshold-crossed"
confidence: 0.85
confidence_language: "confirmed by two vendor reads"
resources: 1
safety_net: "TRIGGERED: VIX +5 intraday (ROUTING_OVERLAYS Safety Net; FILTER_SPEC Pre-Gate bypass => FLASH). 22.51 at about 15:28:55Z, 22.63 at 15:29:11Z, versus VIXCLS 16.61 [Nov 4]"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["VIX", "VVIX", "SPX", "QQQ", "SMH", "KRE", "WAL", "HYG"]
word_count: 169
dispatch_note: "FLASH by the Pre-Gate bypass on an observed +5 intraday move. Precedent SIG-W-20261030-004: that touch faded by the close, so read this as a touch until a close says otherwise. Vendor quote clock not exposed. Will alerted in the active session; no Telegram."
---
# FLASH — VIX +6 intraday safety net: 22.63 versus 16.61 close, QQQ down 4.8%, banks and credit proxies not confirming

Vendor intraday, not closes: ^VIX 22.51 about 10:28 ET, then 22.63 at 10:29:11 ET, versus VIXCLS 16.61 [November 4] = +6.02. Two reads, both over the line; the previous read at 10:19 ET was 20.86.

Same read: S&P 7,489.91 (−2.58%), SPY −2.63%, QQQ 658.60 (−4.82%), SMH 461.15 (−8.55%), VVIX 114.37 (+26.5%). KRE 74.68 (+0.75%), HYG 77.25 (−0.35%). WAL 78.04 (−1.51%), 4 cents above REG-T-02's 78 line, which grades on the regular-session close; existing cycle, no new fire claimed.

The move is still centered on AI names (cards 005, 010, 014). Banks and the credit ETF are not confirming so far; that is an intraday read, not a finding. Cause of the last 15-minute acceleration not read. HY 332 and VIXCLS are November 4 and predate all of this.

Not a RED-FT-06 event: that row grades closes only. No position inference; book truth is off-repo.

ACTION VIOLET: vol-regime read and term structure now. HENRY: gamma and put-wall read. TERRY: held-book exposure at your discretion. Will alerted in the active session.

Sources: research/2026-11-05_morning/tape-flash.json ; FRED VIXCLS 2026-11-04 ; AGENTS/REGINALD/registry/THRESHOLDS.tsv
