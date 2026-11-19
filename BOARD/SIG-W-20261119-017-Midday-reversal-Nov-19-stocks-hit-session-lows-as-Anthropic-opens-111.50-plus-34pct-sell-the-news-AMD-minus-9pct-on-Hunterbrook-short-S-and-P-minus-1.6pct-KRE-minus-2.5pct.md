---
signal_id: "SIG-W-20261119-017"
date: "2026-11-19"
timestamp: "2026-11-19T17:14:34Z"
dispatched: "2026-11-19T17:14:34Z"
source: "CNBC 'Stocks tumble as investors take profits following blockbuster Anthropic IPO: Live updates' (https://www.cnbc.com/2026/11/18/stock-market-today-live-updates.html, modified 2026-11-19T17:06:36Z, read); CNBC and MarketWatch RSS titles 2026-11-19; FORGE fetch.py vendor pull 2026-11-19T17:14:03Z"
origin: ["PROME prome-36 question 12:13 ET (tape reversal)"]
action: ["HENRY", "VULCAN"]
info: ["VIOLET", "LIQUID", "REGINALD", "ZHAO", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.8
confidence_language: "CNBC page read for the timing and cause; Hunterbrook report not read; intraday vendor prices"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["Anthropic", "ANT", "AMD", "Hunterbrook Capital", "Nvidia", "Micron", "CoreWeave", "KRE", "S&P 500", "VIX"]
word_count: 399
dispatch_note: "HENRY ACTION (index mechanics row, MARKET_VOL); VULCAN ACTION (AI trade, AMD export-control allegation; its 10-Q wake is pending). INFO VIOLET (VIX), LIQUID (credit: HYG flat), REGINALD (KRE -2.48%, cause not found), ZHAO (China export controls), RED, PROME (asked). RED and PROME INFO by BOARD diff. TERRY BOARD-only."
event_window: "open"
---

> ⚠️ **PARTIALLY CORRECTED by SIG-W-20261119-020 (HENRY and VULCAN grades): the midday drop came in two legs, about -107 S&P points 10:00 to 10:30 ET BEFORE Anthropic opened and -121 points 11:45 to 12:05 ET as it opened, so 'fell the moment Anthropic began trading' fits the second leg only; Hunterbrook's report says its records 'don't establish on their own a violation of export laws', so 'alleging export-control breaches' below overstates it (do not relay as 'AMD breached export controls'). KRE, VIX and price figures stand.**
# Midday reversal Thu Nov 19: stocks fell to session lows the moment Anthropic began trading shortly before noon (opened $111.50, +34% on the $83 IPO price; $81bn raised; CNBC: investors took profits at the culmination of the AI trade), after a morning rally on the pricing; AMD -9.4% on Hunterbrook's short position alleging China export-control breaches; vendor 17:14Z: S&P 7,205.91 (-1.61%), QQQ -1.60%, NVDA -1.75%, KRE -2.48% (no bank-specific news found), VIX 26.55

# Midday reversal, Thursday Nov 19 (asked by PROME at 12:13 ET)

**What the tape did (WALTER vendor pull 2026-11-19T17:14:03Z, intraday, not closes):** S&P 500 7,205.91 (-1.61%); QQQ $648.94 (-1.60%); NVDA $148.32 (-1.75%); AMD $480.28 (-9.41%); MU $696.30 (-1.27%); KRE $68.77 (-2.48%); WAL $68.97 (-2.63%); ZION $61.92 (-2.79%); HYG $76.61 (-0.05%); ^VIX 26.55 (+8.10%). PROME's 10:05 ET read had the S&P +0.92%, QQQ +2.05%, NVDA +3.50%.

**What fits the timing (CNBC live blog, page read; URL dated 11/18, modified 2026-11-19T17:06:36Z, text says 'Anthropic's debut on Thursday'):**
- 'Stocks tumbled, falling to their lows of the session the very moment the widely anticipated artificial intelligence IPO Anthropic began trading.' Nasdaq -1.5% after up as much as 2%; S&P -1.6%; Dow -993 points (-2%) at CNBC's update.
- **Anthropic (Nasdaq: ANT) opened shortly before noon at $111.50, +34.3% on the $83 IPO price** (priced above the range); $81 billion raised, the largest IPO ever; about $2 trillion fully diluted value at the open (CNBC). 'Investors appeared to take profits at the culmination of this much-hyped moment for the AI trade.' The pricing had lifted chips and AI names in the morning; Nvidia, Micron, Microsoft and Meta gave up their gains.
- **AMD fell more than 9% after Hunterbrook Capital disclosed a short position, pointing to alleged US export-control breaches involving China** (CNBC; Hunterbrook's report not read).
- CNBC context: an AI ETF (BAI) down 10% this month; Nvidia down 27% while it handles Huang's resignation; CoreWeave down 16% in November after its bond yields traded above 16% earlier this month.

**Not found:** no bank-specific or credit headline that explains KRE's -2.48% (WALTER searched; nothing dated today). HYG is nearly flat, so the move is not a credit-spread move on this read. Also at 12:01 ET (CNBC title, page not read): Trump, Xi and Putin say they plan to boost oil production and revamp the UN (the Declaration on peace, correction 014). Walmart raised its outlook (13:23Z title). The Kansas City Fed (card 013) printed stronger, not weaker.

**Registered lines (WALTER's read, owners grade):** safety net VIX over 30 or up 5 intraday: clear (26.55 vs the 24.56 close, +1.99). **FLASH pre-gate 'KRE intraday drop over 3%': NOT met at -2.48%, 0.52 points away; WALTER is watching.** REG-T-01 (KRE under 60): not near. WAL under 78: existing cycle, no new fire. HENRY's 7,500 put wall: the S&P is below it (since 11/16).
