# BOND Monitor — Dealer Capacity / Absorption

**Owner:** BOND
**Last Updated:** 2026-07-28 by BOND — **no new FR2004 data; this monitor is BLIND and has been for 6 weeks.**

> ## 🔴 DATA GAP — ESCALATING, not rolling again
> **The stock series that drives this vector has not been pulled since the 6/17 as-of print. Five prints are now owed: 6/24 · 7/1 · 7/8 · 7/15 · 7/22.** The NY Fed API path used here returns pre-2026 data in-env; retried 7/6, 7/23, 7/28.
>
> **Why this matters more than a normal stale row:** dealer absorption is a **STOCK** vector — benign auction takedowns (which is what we keep getting) show the backstop *wasn't binding that day* and **cannot refresh the inventory stock.** Only FR2004 can move this vector in either direction. So the 🟠 score and the **"→4 trigger ARMED"** state are both resting on a **6-week-old observation**, and the 7/2 downgrade condition in STATUS ("dealer-absorption →2 if the 7/2 print shows a sharp drawdown") has been **unscoreable the entire time.**
>
> **This has been carried as "pending pull" for four weeks. Escalating to Will/PROME as an owed data-source gap rather than deferring a fifth time.** Options: an alternate NY Fed endpoint, the FRED mirror of the primary-dealer series, or accepting the vector as **[STALE — frozen at 6/17]** and saying so on every surface that cites it.
**Purpose:** Track whether dealers can absorb Treasury and credit supply without creating funding or duration stress.

## Key Inputs

| Metric | Source | Cadence | Interpretation |
|---|---|---|---|
| Primary dealer net Treasury positions | NY Fed FR2004 | Weekly | Rising = absorption capacity used; falling under stress = forced de-risking |
| Treasury auction dealer take-down | Treasury auction results | Every auction | High dealer % = weak end demand / warehousing |
| eSLR / SLR rule changes | Fed/OCC/FDIC / news | Event | Capacity relief or constraint |
| Basis trade leverage | CFTC/SEC/Fed reports / market research | Monthly/event | Hidden duration/funding fragility |
| SOFR/repo pressure | LIQUID | Daily | Funding consequence, not BOND-owned |

## Current Read

**🟠 Dealer-absorption vector = 3 (elevated), 4-trigger ARMED.** FR2004 as-of **6/17** (pulled 7/1, KB-061): **FRESH HIGHS, not off the record** — 11–21Y **$74.6B = new all-time bucket record** (+$7.6B/+11.4% over the prior 5/27 record $67.0B, after sitting flat ~$66-67B on 6/3 and 6/10); 7–11Y $42.9B (vs 38.0 on 5/27); >21Y $57.0B (vs 49.7). Combined long-end **$174.5B = #2 print ever** ($1.2B below the 2/25/26 record). NUANCE intact: the build is NOT auction-forced — the 6/16 20Y PD take was only $1.1B vs a +$7.7B w/w bucket build, and the 6/23-25 cluster showed no dealer spike (10.2–12.9%) — this is secondary-market warehousing during FOMC week. The pre-registered →4 trigger (**fresh highs + weak auction**) is half-met; the weak-auction half is judgment (6/11 30Y dealer take 14.7% arguably qualifies; everything since is benign). **Decisive tests: the 6/24-week FR2004 print (released 7/2) and the 7/9 30Y reopening** — record stock + a 30Y stress marker = the demand-hole configuration. ⚠️ **The 6/24 print is PENDING PULL as of 7/6** (NY Fed raw API returns pre-2026 data in-env; need the tool/dashboard path) — carried the 6/17 record; re-grade 3-vs-4 when it lands. eSLR (effective 4/1/26) eased GSIB intermediation incrementally but did NOT exclude Treasuries from the SLR denominator. **Post-QT context (7/6): no Fed coupon backstop** — a warehoused long-end auction has no Fed bid to lean on (RMPs buy bills; KB-069), so dealer capacity is the *only* backstop at the coupon end.

## Rolling Table

| Date | Dealer UST position | Auction take-down note | Repo/SOFR context | Read | Source |
|---|---:|---|---|---|---|
| 2026-05-05 refresh | ~$550B net Treasuries | Capacity expanded post-eSLR | SOFR-IORB normalized | 🟡 capacity-used | Prior BOND STATUS / NY Fed/FT note |
| 2026-05-11 3Y | N/A | Dealer accepted 13.6% | SOFR-IORB -5bps | 🟡 watch | FiscalData + dashboard |
| 2026-05-12 10Y | N/A | Dealer 12.0% | SOFR-IORB ~0 | 🟡 | FiscalData |
| 2026-05-13 30Y | N/A | Dealer 11.7% | SOFR-IORB ~0 | 🟡 | FiscalData |
| 2026-05-27 FR2004 | **11–21Y $67.0B (record); 7–11Y $38.0B (94th pctile); >21Y $49.7B** | — (positioning snapshot) | SOFR-IORB ~0 | 🟠 record *stock* | NY Fed FR2004 (KB-BND-047) |
| 2026-06-10→16 June auctions | (pre-6/23 re-pull) | 10Y PD 9.5%, 20Y 8.5%, 30Y 14.7% — **flow benign** | SOFR-IORB -2bp (6/17) | 🟠 stock-high / flow-benign | TreasuryDirect |
| 2026-06-17 FR2004 | **11–21Y $74.6B (NEW record, +11.4% w/w); 7–11Y $42.9B; >21Y $57.0B; combined $174.5B #2 ever** | 6/23-25 cluster takes 10.2–12.9% (benign) | SOFR-IORB +3bp 6/30 = clean qtr-end (SRF $0) | 🟠 fresh-record stock / flow-benign — **→4 trigger ARMED** | NY Fed FR2004 API (KB-BND-061) |

## Triggers

| Trigger | Action |
|---|---|
| Dealer inventories at/near record + weak auctions | Signal LIQUID/ZHAO; watch repo funding |
| Forced inventory decline during selloff | 🔴 market-function stress |
| eSLR relief drives absorption while end-demand weak | Mark as mechanical support, not clean bill of health |
| Weak auction followed by SOFR-IORB positive | Escalate as auction stress funding through repo |
