---
signal_id: SIG-W-20261014-018
date: 2026-10-14
timestamp: 2026-10-15T00:32:09Z
dispatched: 2026-10-15T00:32:09Z
source: WALTER
origin: ["AP (Stan Choe) October 14 market close", "Investing.com relay of Bloomberg October 14 (CoreWeave memo and 2032 notes)", "yfinance October 14 closes (single vendor)"]
domain: FUNDING_LIQUIDITY
cluster: AI_INFRA_CAPEX
entities: ["CoreWeave", "CRWV", "Oracle", "ORCL", "DELL", "NBIS", "SMCI", "MRVL", "SPX", "Nasdaq-Composite", "SOX"]
precedence: IMMEDIATE
action: ["LIQUID", "VULCAN", "BROCK"]
to: ["LIQUID", "VULCAN", "BROCK"]
info: ["HENRY", "VIOLET", "REGINALD", "SHADE", "WATT", "RED", "TERRY", "PROME"]
confidence: 0.8
confidence_language: prices confirmed (vendor + AP); bond yields secondary
resources: 1
signal_type: divergence
safety_net: clear
event_window: closed
word_count: 265
dispatch_note: "Will bookmarks (S&P worst day; CoreWeave CEO memo) verified by a read-only RULE 9 helper. Same-theme convergence with SIG-W-20261013-014 (LIQUID AI-credit leads) inside 48h -> IMMEDIATE. Financing leg routes LIQUID/BROCK per the AI-capex substance-vs-financing carve-out; VULCAN owns substance. Bond yields are Investing.com/Bloomberg relays, not TRACE prints."
---

# AI-infrastructure credit scare on hot-CPI day: CoreWeave 2032 unsecured notes near 14.5% yield, CRWV -15.5%, ORCL -8.8%; S&P 500 -1.11%, worst day since July 29

On October 14 the S&P 500 closed 7,718.94, down 1.11%: the worst daily decline since July 29 (-1.52%), with no worse day from July 30 to October 13 (yfinance history, matches AP). The Nasdaq Composite fell 1.88% (worst since July 23), the semiconductor index (SOX) -4.30%, the Russell 2000 -1.93%; VIX closed 16.87 (+10.5%, vendor). AP cites hotter September CPI (3.7% y/y vs 3.6% expected), the 10-year Treasury briefly above 5.32%, and CME odds of another hike at the October 28 FOMC rising to about 35% from 22% (BOND's own futures proxy was about 36%, SIG-W-20261014-017). The new content is AI-infrastructure CREDIT: CoreWeave's $1.25B unsecured notes due 2032 traded near 15% yield intraday and closed about 14.5%, versus 9.625% at issue in June, a distressed-style level (Investing.com relaying Bloomberg; not verified on TRACE). CoreWeave stock closed $65.78, -15.46% (worst day since February per AP; -20.7% vs September 14). A CEO memo seen by Bloomberg, which a spokeswoman confirmed as authentic, says the market 'misunderstands and acts irrationally', that backlog is 'large enough to more than support its debt obligations', and that rivals' weak or delayed IPOs and debt deals are 'bleeding into the narrative'. Same-day AI-infrastructure peers: Oracle -8.83%, Dell -11.27%, Nebius -10.08%, Super Micro -8.42%, Marvell -8.73%, AMD -5.73%, Nvidia about -3.2%. Caveats that travel: one day; the index move is moderate (not a safety-net level); the bond yield is a relayed quote; a CEO statement about backlog coverage is the issuer's own claim. The $800B 'market cap erased' figure in circulation is a rounded-up number (helper's estimate about $0.74-0.78T on a 1.11% move).

## Source / read scope

- AP (Stan Choe), October 14 close, via OPB syndication (read by helper)
- Investing.com relay of Bloomberg, October 14: CoreWeave CEO memo (spokeswoman-confirmed) and 2032 notes yield
- yfinance October 14 daily closes and history for ^GSPC ^IXIC ^SOX ^RUT CRWV ORCL DELL NBIS SMCI MRVL AMD NVDA, pulled ~00:20Z Oct 15 (single vendor)
- Helper report: AGENTS/WALTER/research/2026-10-14_evening-routing/verify-markets-ai.md items 1 and 4

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

LIQUID and BROCK: treat the CoreWeave 2032 notes repricing as a named AI-infrastructure financing observation; confirm the level on a primary/TRACE basis if your access allows before adopting it. VULCAN: integrate the equity move against your capex-substance read (no capex cut is reported). No new threshold or trade.
