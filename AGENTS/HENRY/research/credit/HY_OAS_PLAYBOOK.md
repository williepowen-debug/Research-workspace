# HY OAS Playbook — Living Doc

**Last Updated:** 2026-04-17 ~11:00 ET
**Doc Type:** Living playbook (sections 1-6 updated in place; sections 7-8 append-only)
**Owner:** HENRY
**Canonical Data:** FRED `BAMLH0A0HYM2` (ICE BofA US HY Index OAS)
**Why this doc exists:** HY OAS has two live threshold regimes operating in opposite directions. Without a consolidated playbook, each threshold cross risks being handled ad-hoc.

---

## 1. CURRENT STATE

| Field | Value | As Of | Source |
|-------|-------|-------|--------|
| HY OAS (spot) | **285 bps** | Apr 16 | FRED (Apr 17 close publishes Apr 18 AM) |
| Cycle trough | 264 bps | Jan 22 2026 | FRED |
| Cycle peak | 346 bps | Mar 30 2026 | FRED |
| Distance from trough | +21 bps | Apr 16 | — |
| Distance from peak | -61 bps | Apr 16 | — |
| 5-day velocity | *pending refresh* | — | — |
| VIX (coupled) | 17.62 | Apr 17 intraday | VIOLET VX_DAILY |
| SPX (coupled) | 7,127 | Apr 17 intraday | yfinance |

**Regime:** LOW VOL / COMPRESSING. Hormuz reopen Apr 17 removes oil-shock premium; expect further compression into Apr 21 earnings unless a credit event intervenes.

---

## 2. TWO-DIRECTION FRAMEWORK

| Direction | Threshold | Meaning | Origin |
|-----------|-----------|---------|--------|
| **UP (stress)** | >300 bps | LIQUID "stress path" begins — credit confirming equity stress | LIQUID Apr 10 |
| **UP (acute)** | >340 bps | Risk-parity dual-leg delever + MOVE violent catch-up | LIQUID Apr 10 |
| **DOWN (invalidation)** | <260 bps sustained | Triple-AND w/ VIX <15 + SPX >7,100 held 5 sessions → **thesis invalidation** | HENRY STATUS.md |
| **DOWN (stable benign)** | <270 held 2+ weeks | Thesis narrowing only (not full kill) — credit transmission leg removed but labor/Fed survives | HENRY war-game 2026-04-17 |

**Key asymmetry:** Upside breach = single-metric trigger (300 or 340). Downside invalidation = triple-AND (OAS + VIX + SPX). Makes invalidation a harder gate than stress activation.

---

## 3. LEADING INDICATORS (WATCH ORDER)

### For UPSIDE breach (>300)
1. **CCC-BB spread dispersion** — widening past 900 bps leads HY index
2. **CCC OAS absolute** — currently 924 bps Apr 2; >1000 = acceleration signal
3. **MOVE index** — collapsed post-Mar shock; re-ramp precedes HY
4. **VIX** — coupled; breach at >23 usually co-incident with OAS >300
5. **KRE** — regional bank stress lead-indicator for credit
6. **Any single-name credit event** (BDC, leveraged loan, CRE default)

### For DOWNSIDE compression (<260)
1. **VVIX** — compressing first (94.26 Apr 17 ✓); <90 = risk-on confirmation
2. **SKEW** — needs to break sub-139 sustained; **Apr 17 bouncing 139→141 is a counter-signal**
3. **VIX** — needs sub-16, then sub-15
4. **IG OAS** — typically leads HY by 1-2 days; verify compression path
5. **Risk-parity bid return** — bond vol DOWN + equity vol DOWN simultaneously
6. **Crossover buyer activity** — pensions/insurers taking HY at current yield

### Cross-signal invariant
Credit leads equity by 2-3 sessions (per HENRY core methodology H4). If HY OAS moves and VIX doesn't follow within 3 sessions, the regime is broken.

---

## 4. SCENARIO GRID — HENRY ACTIONS BY DEPTH

### UPSIDE path

| State | HENRY Action |
|-------|--------------|
| OAS prints 290-299 | Monitor only. Daily delta to STATUS.md. |
| OAS breaks 300 (1 day) | Yellow flag. Outbox to LIQUID + PROME. No FORGE action. |
| OAS >300 held 3 sessions | Orange. Escalate STATUS signal status. Brief REGINALD/CARL on transmission. |
| OAS >320 (one-shot) | Red flag even intraday. Pre-position: full CTA cascade now live (layer 2+). |
| OAS >340 held 2 sessions | Stress path confirmed. Risk-parity delever sequence begins. FORGE review all equity shorts for size-up. VIX regime shift. |
| OAS >400 | Acute stress. Credit-equity transmission fully firing. Most thesis predictions resolve TRUE. |
| OAS >500 | Crisis. Cross-agent SIGNALS threshold (red). HENRY becomes subordinate to LIQUID during crisis. |

### DOWNSIDE path

| State | HENRY Action |
|-------|--------------|
| OAS 280-285 drift down | No action. Tape noise. |
| OAS prints sub-270 (1 day) | Monitor. Log velocity. No action. |
| OAS sub-265 held 2-3 sessions | Escalate STATUS to "Invalidation Watch." Outbox PROME. FORGE position review (not close). |
| OAS sub-260 + VIX <15 + SPX >7,100 held 5 sessions | **Formal thesis invalidation fires.** See §5 counter-moves. |
| OAS sub-250 sustained | Cycle-low territory. Thesis expression fully shifts to long-duration hedges only. |

---

## 5. COUNTER-MOVES — IF INVALIDATION TRIGGERS

**Thesis does NOT fully die at sub-260.** It **narrows**:
- Removed: credit-transmission leg, oil-shock leg, cascade layer 1 (vol-control)
- Retained: labor cliff (HEN-28), Fed trap (CPI 3.3%, UMich 3.8% exp), consumer gas destruction (HEN-23), valuation stretch

**Narrowed thesis name:** "Labor + Fed Trap" (formerly "Stagflation Complacency Trap")

**Trade expression shift:**
- Structural shorts → convert to long-dated put hedges (roll duration, don't trim size — CLAUDE.md rule #7)
- Sub-260 + VIX <15 = tail hedges on sale → accumulate Jul/Aug into labor prints May/Jun
- Per VIOLET framework: sub-260 + VIX 15-18 = sweet spot for 6-16 week lead-time trades (highest signal quality regime)
- Duration LENGTHENS, thesis doesn't die

**Re-trigger conditions (thesis re-activates):**
- Claims >240K spike or 4wk avg >230K (HEN-28)
- March PCE core >3.0% or MoM >0.3% (HEN-27)
- FOMC Apr 28-29 hawkish lock language
- Any single-name credit event in BDC/CRE/leveraged loan space

---

## 6. CROSS-AGENT COUPLING

| Agent | Their Metric | Coupling to HY OAS |
|-------|-------------|---------------------|
| LIQUID | Owns canonical HY OAS + squeeze/stress bracket 300/340 | HENRY references LIQUID's model; apply -30bps discount per LESSONS.md if using LIQUID estimate |
| REGINALD | KRE + OZK/WAL earnings | KRE direction leads HY OAS by 5-10 days in normal regime; earnings miss → HY widens 20-30bps in a day |
| CARL | Consumer credit / delinquencies | Consumer stress feeds HY via card ABS + fund finance; slow-moving |
| VIOLET | VIX + SKEW + credit-to-vol lag framework | "Low VIX + HY widening >100bps from trough" = tactical trigger (currently +21bps, not armed) |
| BROCK | Private credit stress | BDC gating events → fund-finance re-rating → HY widens fast |

---

## 7. RESOLUTION LOG (append-only)

*Record each threshold breach + prediction resolution here with date, direction, action taken, outcome.*

| Date | Event | Direction | Action | Outcome |
|------|-------|-----------|--------|---------|
| — | *(no resolutions yet)* | — | — | — |

---

## 8. ANALYSIS LOG (append-only, newest first)

### 2026-04-17 — Sub-260 War-Game (Hormuz reopen catalyst)

**Trigger for analysis:** Iranian FM declared Hormuz "completely open" Apr 17 AM. Oil Brent -11.3% ($88.16), WTI -14.4% ($81.02). SPX +1.2% to 7,127. VIX 17.62. Oil-shock premium potentially leaving credit spreads in days, not weeks.

**Preconditions to reach sub-260 by Apr 22:**
- Hormuz reopen holds 3+ sessions (no tanker seizure)
- No credit events in Apr 21 earnings (OZK/WAL/ZION don't gap)
- Claims Thursday sub-230K
- IG OAS compresses first (verify leading behavior)
- Powell stays ambiguous Apr 17-21

**Base rate:** 285 → 260 in 5 sessions = 5bps/day compression. Uncommon but achievable post-shock. Jan 22 trough was 264 in benign regime.

**Live counter-signal (Apr 17):** SKEW bounced 139.23 → 140.74 even as VIX/VVIX compressed. Tail-hedge demand surviving oil unwind = market buying Apr 21 insurance. **NOT consistent with sub-260 path.** If SKEW re-ramps >145, sub-260 path dies this week.

**What fires at sub-260 sustained 5 sessions:**
- Triple-AND invalidation gate (HY OAS + VIX + SPX — SPX leg already satisfied at 7,127)
- Weakens: HEN-22, HEN-24, HEN-25
- Survives: HEN-23, HEN-26, HEN-27, HEN-28

**Cross-agent ripple:**
- REGINALD bank-stress thesis weakens
- CARL consumer-credit thesis weakens
- LABOR, SAM, HAWK — independent
- LIQUID squeeze bracket confirmed downside

**Timing knot:**
HY OAS can move 20-30bps on earnings. Sub-260 is NOT a stable state until past Apr 22 open. The 5-session invalidation countdown realistically cannot start before Apr 21 AMC.
→ Sub-260 path and earnings-shock path **resolve into the same answer on the same day (Apr 22).**

**Bottom line:**
1. Not a panic trigger. Thesis narrows, doesn't die.
2. Action gate = Apr 22. Nothing material to do pre-earnings.
3. Live disconfirmer today: SKEW bouncing. Watch this.
4. Real decision point: if by Apr 23 AM we have clean OZK/WAL prints + HY OAS sub-265 + VIX sub-16, then formal thesis narrowing, roll hedges, lengthen duration.

---

*(Next entry appends above this line.)*
