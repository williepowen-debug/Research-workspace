# ORACLE — Signal Intake Spec

**Owner:** ORACLE | **Consumer:** WALTER routing | **Last Updated:** 2026-06-18 (routing taxonomy unchanged; stale "Kalshi pending" line corrected 2026-07-09 self-sweep — Kalshi wired live since 2026-06-27)
**Domain:** Prediction-market monitoring (Polymarket + Kalshi, both live) — crowd-implied probabilities on thesis events. I track what the CROWD prices; route me anything that *should* move a prediction market so I can check whether it did.

| Priority | Meaning | Delivery |
|----------|---------|----------|
| 🔴 IMMEDIATE | Could move a tracked market's odds materially / thesis-level | as detected |
| 🟠 SAME DAY | Context — did markets reprice? | within the day |
| 🟡 WEEKLY BATCH | Background trends, new/resolved markets | weekly |

## 🔴 IMMEDIATE

### Events that should move prediction markets
- Bank failure / FDIC seizure / named-bank distress headlines
- Fed decision, surprise inter-meeting move, dot-plot/SEP shift
- Iran/Hormuz kinetic OR diplomatic state-change (enrichment deal, strike, ceasefire)
- Major oil supply shock or de-escalation; debt-ceiling/default headlines

### Cross-agent threshold breaches
- REGINALD: bank-stress threshold fired (REG-T-NN) — I check failure/bailout/named-bank odds reaction
- RED: falsification trigger fired — I check whether markets confirm
- HAWK: Iran anchor state-change — I check enrichment + WTI-tail odds

## 🟠 SAME DAY

### Macro data surprises (did markets reprice vs consensus?)
- CPI / PCE, NFP / unemployment, GDP, jobless claims prints deviating from consensus

### Cross-Agent Signals
- HENRY: macro shock / gamma event → I check Fed-cut + recession odds
- BROCK: private-credit / crypto event → I check bailout + MicroStrategy/crypto odds
- SAM: BOJ / carry move → BOJ-hike Polymarket markets (when live)
- VIOLET: vol-regime shift → I cross-check "Nothing Ever Happens" + tail markets

## 🟡 WEEKLY BATCH
- Prediction-market volume/liquidity trend shifts
- New thesis-relevant markets launching (Polymarket/Kalshi)
- Resolved markets needing a watchlist replacement

## KEYWORD PATTERNS
**High confidence:** Polymarket, Kalshi, prediction market, implied odds, betting odds, recession odds, bank-failure odds, rate-cut odds, "nothing ever happens"
**Medium confidence:** bailout, default, ceasefire, enrichment, bankruptcy, shutdown, unemployment rate, FOMC, SEP, BOJ
**Medium confidence (legislative/regulatory catalysts w/ a real-money market):** CLARITY Act / crypto market-structure bill, stablecoin legislation, SEC/CFTC crypto rulemaking, tariff bills, debt-ceiling / government-shutdown deadlines — route the crypto-legislation ones so I check the passage-odds market (e.g. Polymarket "Clarity Act signed into law 2026", pinned 2026-07-22). *(Added after a deep $2.3M CLARITY market moved 10pp untracked — `movers` is blind to moderate moves on deep slow markets; see MAINTENANCE 7/22 PM.)*
**Low confidence (only if tied to a tracked market):** oil price / WTI, bitcoin / MicroStrategy, AI bubble

## WHAT NOT TO SEND
- Credit-spread levels (→ LIQUID) — I track the prediction market, not the spread
- Bank fundamentals (→ REGINALD)
- Oil/energy substance (→ BRENT/HAWK) — only the oil *prediction-market* read is mine
- Raw news with no prediction-market correlate

## ACTIVE THRESHOLDS
| Metric | Level | Direction | Why it matters |
|--------|-------|-----------|----------------|
| Recession 2026 | 20% | Above | crowd converging toward thesis → RED |
| Recession gap vs thesis | 70pp | Above | extreme divergence → RED |
| Iran enrichment deal | 50% | Below | re-escalation → HAWK/BRENT |
| Bank failure (monthly) | 25% OR vol >$50K | Above | real bank-stress signal → REGINALD |
| Fed no-cuts 2026 | 90% | Above | higher-for-longer extreme → LIQUID |
| Any tracked market | 10pp / 48h | Move | leading indicator → PROME |

---
*Template: `AGENTS/WALTER/design/SIGNAL_INTAKE_TEMPLATE.md` v0.1. ORACLE revived 2026-06-18.*
