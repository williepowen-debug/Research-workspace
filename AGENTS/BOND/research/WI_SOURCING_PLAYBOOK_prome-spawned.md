# WI Sourcing Playbook — Treasury Coupon Auctions

## PROVENANCE
- **Author:** Prome-spawned one-shot research sub-agent (Claude Code, master branch)
- **When:** 2026-05-20 PM ET
- **Why:** Today BOND left the 20Y auction tail at "provisional clean-to-1bp" because intraday When-Issued (WI) yield was unverifiable without a Bloomberg/Tradeweb terminal. ZeroHedge confirmed 0bp post-hoc, single-source, ~2 hours later. Tomorrow (5/21) brings the 10Y reopening at 1pm ET — same gap will repeat unless BOND has a playbook.
- **Disposition:** BOND integrates and commits on next boot. Sub-agent did NOT touch STATUS, monitors, outbox, or commit anything.

---

## Verdict (Executive Summary)

1. **No free public source provides reliable real-time pre-1pm intraday WI yield.** This is a structural gap, not a search failure. Tradeweb/Reuters/IFR WI ticks live behind institutional terminals only.
2. **The fastest credible post-auction WI confirmation is InvestingLive/ForexLive**, which publishes a structured "WI level at the time of the auction" bullet within ~5-15 min of 1pm. They quote the same Reuters/Tradeweb tick ZeroHedge uses, but typically beat ZeroHedge to publish by 15-45 min.
3. **ZeroHedge auction recap is the second confirmation** — prose-form, embeds WI explicitly, usually live 1:15-1:45pm ET. Use as cross-check, not primary.
4. **Pre-1pm WI is unobtainable** without a paid terminal. Best proxy: front-month Treasury futures yield at 12:55pm ET via CME free quote page (directional, NOT a substitute for the actual WI tick).
5. Workflow: pre-position at 12:55pm with futures-implied yield as anchor → at 1:01pm pull TreasuryDirect awarded high yield → wait 5-15 min for InvestingLive WI bullet → cross-check ZeroHedge by 1:45pm.

---

## Ranked Playbook

| Rank | Source | URL | Cost | WI availability | Reliability | Latency post-1pm | Format |
|------|--------|-----|------|-----------------|-------------|-------------------|--------|
| 1 | InvestingLive auction recap | investinglive.com/news (search "X year notes high yield") | Free | Post-auction only; "WI level at time of auction" as explicit bullet | High (Reuters/Tradeweb-sourced; confirmed 5/13 30Y, 1/12 10Y) | ~5-15 min | Bulleted prose w/ 6-mo averages |
| 2 | ZeroHedge auction recap | zerohedge.com/markets | Free | Post-auction only; WI quoted in prose ("stopped X bps through Y.YY% WI") | High (matches InvestingLive; confirmed today 5/20) | ~15-45 min | Prose narrative |
| 3 | ForexLive (sister site to InvestingLive) | forexlive.com | Free | Same structure as InvestingLive | High (often same wire feed) | ~5-15 min | Bulleted prose |
| 4 | CME Treasury futures front-month | cmegroup.com/markets/interest-rates/us-treasury.html | Free, 10-min delayed (real-time requires account) | Pre-auction directional proxy ONLY (NOT WI tick) | Medium (futures yield ≠ WI; CTD basis introduces noise) | Real-time-ish | Quote ticker |
| 5 | TreasuryDirect "Today's Auction Results" | treasurydirect.gov/auctions/announcements-data-results/announcement-results-press-releases/auction-results/ | Free | Awarded high yield only (NO WI) | High (official) | ~1-3 min post-1pm | HTML/PDF press release |
| 6 | Investing.com economic calendar | investing.com/economic-calendar | Free | Forecast + post-auction high yield; NO WI field | Medium (forecast is consensus, not WI) | ~1-5 min | Calendar row |
| 7 | Tradeweb US Treasury closing prices | tradeweb.com/our-markets/data-analytics/u.s.-treasury-closing-prices | Free | End-of-day close ONLY; no intraday WI | High | End of day | Table |
| 8 | Twitter/X traders (@Convertbond, @biancoresearch, @Fedguy12) | x.com | Free | Sporadic; some buy-side post screencaps but inconsistent and not auction-by-auction | Low-Medium (unverifiable single-source) | Variable | Tweet |
| 9 | Wrightson ICAP commentary | wrightson.com/commentary | Free (some) | Auction previews but rarely with explicit WI tick | Medium (forward-looking commentary, not point quote) | Pre-auction | Long prose |
| 10 | InTouch Capital Markets | itcmarkets.com | Paywalled (free trial available; sub-agent did NOT sign up) | Unverified pre-auction WI | Unverified | Unknown | Unknown |

---

## Recommended Workflow — 5/21 10Y Reopening (1pm ET)

**12:45-12:55pm ET — Pre-position:**
1. Open CME 10Y futures front-month (ZN) quote page; note current implied yield. This is your DIRECTIONAL anchor only — do not state it as WI.
2. Open Investing.com 10Y note auction calendar row in a tab (will populate awarded high yield first).
3. Pre-load InvestingLive search URL: `investinglive.com/news?q=10+year+notes+high+yield` (refresh at 1:05pm).

**1:00-1:05pm ET — Print:**
4. TreasuryDirect press release goes up within 1-3 min. Capture **awarded high yield** immediately. Do NOT state WI yet.

**1:05-1:20pm ET — WI confirmation:**
5. Refresh InvestingLive every 60 sec until the recap drops. The "WI level at the time of the auction" bullet gives the tick. Capture tail = awarded high yield − WI.
6. If InvestingLive late: pivot to ForexLive (same group, often parallel publish).

**1:20-1:45pm ET — Cross-check:**
7. Pull ZeroHedge auction recap (zerohedge.com/markets). Confirm WI matches InvestingLive within 0.1bp. If divergent: flag as data-quality issue, do not propagate tail to STATUS until reconciled.

**Discipline rule:** If WI is unavailable by 1:45pm (rare but possible on holidays/late publishes), STATUS gets "tail: pending WI verification" — do NOT guess from futures. Today's session showed waiting 2 hours was acceptable; do not invent precision.

---

## Known Unknowns

- **Pre-1pm intraday WI tick:** Not publicly available in any free source the sub-agent could verify. Tradeweb and Reuters wire feeds carry it but require institutional logins. If BOND needs pre-1pm WI for trade timing, the answer is "infrastructure gap, not a search problem."
- **Twitter/X buy-side posters:** Real accounts exist but the sub-agent could NOT verify any specific handle reliably posts the 12:55pm WI tick auction-by-auction. Treat as opportunistic, not systematic. Manually scan FinTwit for ~30 min around 1pm and build a verified handle list over 2-3 auctions before relying on any single account.
- **InTouch Capital Markets:** Has a free-trial offer but sub-agent did not sign up. Worth a one-time trial test if WI sourcing remains a persistent bottleneck.
- **Wrightson ICAP:** Publishes Treasury market commentary but the sub-agent could not confirm whether pre-auction notes contain explicit WI ticks vs general directional commentary.
- **CNBC Rick Santelli live:** May mention WI verbally on-air around 12:55pm but the sub-agent could not verify systematic coverage. Requires live TV; not a scrapeable workflow.
