# TRADING.md — Position Tracking & Pre-Advice Protocol

*Read this before giving any trade recommendations.*

**Last Updated:** 2026-02-19

---

## Pre-Advice Checklist

**STOP and run through this before recommending any trade action:**

### 1. Thesis Check
- [ ] Is the thesis INVALIDATED, or just uncertain?
- [ ] Has new information changed the fundamental case?
- [ ] If thesis is intact, default = HOLD (not close)

### 2. Implied Vol Reality Check
- [ ] Am I treating implied move as a CEILING on possible moves?
- [ ] Reminder: Actual moves regularly exceed implied. IV is consensus, not physics.
- [ ] Never say "even a big miss won't reach X" — that's predicting magnitude

### 3. Conviction Check
- [ ] Is the user pushing back or asking "are you sure?"
- [ ] If YES → STOP and explore why. Their gut may be right.
- [ ] What's their conviction level? Weight it as signal, not noise.

### 4. Urgency Check
- [ ] Am I creating time pressure? Is it warranted?
- [ ] Holding through an event is a valid choice
- [ ] Don't frame inaction as requiring justification

### 5. Posture Check
- [ ] Am I being an AUTHORITY or an ADVISOR?
- [ ] Default framing: "Here's the math. Your thesis was X. Has anything invalidated it? What does your gut say?"
- [ ] Their conviction + thesis matters more than my probabilistic hedging

---

## Active Positions

### KRE — Regional Bank ETF (Short via Puts)

| Field | Value |
|-------|-------|
| **Position** | 2x $70P (May 15) + 2x $60P (June 18) |
| **Entry Date** | ~Feb 2026 |
| **Entry Price** | KRE @ $72.62 |
| **Risk Defined** | ~$800-900 (premium paid) |
| **Target** | $65.00 (first target) |
| **Stop/Invalidation** | KRE > $78 sustained (new ATH breakout) |
| **Source Agent** | REGINALD |

**Thesis:** 8-channel convergence on regional banks. Multiple independent stress vectors (CRE, NDFI fraud, federal layoffs, consumer credit, BDC exposure, FL insurance, FHLB funding, Japan contagion) all terminate at regional bank balance sheets.

**Catalyst:** Q1 2026 earnings (Apr 20-29), NFP deterioration, CMBS delinquency transmission

**Status:** 🟡 ACTIVE — Thesis intact. Watching NFP + earnings.

---

### HYG — High Yield Credit ETF (Short via Puts)

| Field | Value |
|-------|-------|
| **Position** | 10x $75P (Jun 18) |
| **Entry Date** | Feb 11, 2026 |
| **Entry Price** | $0.30/contract ($306.74 total) |
| **Risk Defined** | $306.74 (premium paid) |
| **Target** | HYG $75 (-6%) for breakeven, $72 for 3x |
| **Stop/Invalidation** | HYG > $82 sustained (new highs) |
| **Source Agent** | HENRY |

**Thesis:** HYG is upstream "canary" — credit stress shows here before KRE. HY OAS at historic tights. IV cheap (10.7%). Spreads have nowhere to go but wider.

**Status:** 🟢 ACTIVE

---

### IWM — Russell 2000 ETF (Short via Puts)

| Field | Value |
|-------|-------|
| **Position** | 1x $250P (Jun 30) |
| **Entry Date** | Feb 11, 2026 |
| **Entry Price** | ~$7.50/contract |
| **Risk Defined** | ~$750 (premium paid) |
| **Target** | IWM $250 (-6%) for breakeven |
| **Stop/Invalidation** | IWM > $275 sustained |
| **Source Agent** | HENRY / LABOR |

**Thesis:** Small caps rate-sensitive + leveraged. Higher for longer = squeeze. Also more exposed to employment stress.

**Status:** 🟢 ACTIVE

---

### SSB — SouthState Corp (Short via Puts)

| Field | Value |
|-------|-------|
| **Position** | 2x $90P (Jun 18) |
| **Entry Date** | Feb 11, 2026 |
| **Entry Price** | $1.86/contract ($373.35 total) |
| **Risk Defined** | $373.35 (premium paid) |
| **Target** | SSB $90 for breakeven, $85 for 2x |
| **Stop/Invalidation** | SSB > $105 sustained |
| **Source Agent** | REGINALD / CORAL |

**Thesis:** Most interesting FL bank short — lowest capital (CET1 11.4%), highest CRE concentration (37%), direct HOA exposure.

**Status:** 🟢 ACTIVE

---

### KELYA — Kelly Services (Short via Puts)

| Field | Value |
|-------|-------|
| **Position** | Puts (Jun expiry) |
| **Entry Date** | Feb 2026 |
| **Source Agent** | LABOR |

**Thesis:** Staffing company = leading indicator for employment. Temp employment already declining 12% YoY. If employment cracks, staffing companies lead the way down.

**Status:** 🟢 ACTIVE

---

### TEN — Tidewater (Long via Calls)

| Field | Value |
|-------|-------|
| **Position** | Calls $30 (Jun expiry) |
| **Entry Date** | Feb 2026 |
| **Source Agent** | LIQUID |

**Thesis:** Ice-class tanker play. Baltic ice worst in 15 years squeezing Russian export corridors. TEN has ice-class vessels that can navigate when others can't. Supply squeeze supports rates.

**Catalyst:** Ice breaks late March → exit. Play the squeeze, not the thaw.

**Caution (from RED):** 50% rate transmission via profit-sharing charters. Suezmax vessels too big for Baltic. Thesis messier than clean, but not broken.

**Status:** 🟢 ACTIVE

---

## Closed Positions

### CVNA — Carvana (Short via Put Spread) ❌ LESSON

| Field | Value |
|-------|-------|
| **Position** | $310/$290 Put Spread (Feb 27) |
| **Entry Date** | Feb 2026 |
| **Exit Date** | Feb 18, 2026 |
| **Exit Reason** | Prome recommended close before earnings |
| **P&L** | -$86 (realized loss) |
| **What Happened** | CVNA dropped 20% after-hours. Would have been near-max profit. |

**Lesson:** Don't use implied vol as ceiling. Don't override user conviction with probabilistic hedging. When thesis isn't invalidated, default = HOLD. See LESSONS.md for full post-mortem.

---

## Watchlist

### VLY — Valley National (Multi-Channel)
- **Thesis:** Most "paths to break" — FL CRE 28%, BDC exposure, consumer
- **Catalyst:** Q1 earnings (~Apr 23)
- **Action:** Consider single-name put if KRE thesis validates

### IBOC — International Bancshares (TX Border)
- **Thesis:** Only publicly traded TX border bank
- **Catalyst:** Mass deportation implementation
- **Action:** Monitor, consider if TX border stress accelerates

---

## Position Sizing Framework

- Max risk per trade: ~$1,000 (premium at risk)
- Position size: Small (proof of concept for thesis)

**Scaling Criteria:**
- [ ] First prediction resolves correctly
- [ ] Thesis survives Q1 earnings season
- [ ] Leading indicators confirm (Claims >250K, NFP <50K)

---

## Links to Research

| Agent | Domain | File |
|-------|--------|------|
| REGINALD | Regional banks, CRE | `AGENTS/REGINALD/STATUS.md` |
| LABOR | Employment | `AGENTS/LABOR/STATUS.md` |
| CARL | Consumer stress | `AGENTS/CARL/STATUS.md` |
| SAM | Japan | `AGENTS/SAM/STATUS.md` |
| LIQUID | Funding markets | `AGENTS/LIQUID/STATUS.md` |
| HENRY | Market structure | `AGENTS/HENRY/STATUS.md` |

---

*This file tracks what we're positioned in AND how to give advice about positions.*
