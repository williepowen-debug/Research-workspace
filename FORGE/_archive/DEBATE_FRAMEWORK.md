# FORGE — Structured Debate Framework v2.1

*For adversarial analysis of trading theses*

---

## Overview

This framework structures debates between Prome (thesis holder) and RED (adversarial challenger) to pressure-test trading positions and generate actionable outputs.

**Purpose:** Not just "who's right" but "what should we do given uncertainty."

---

## Current Debate

**Proposition:** KRE will close below $59.84 (15% decline from $70.40) by December 31, 2026.

**Positions:**
- **PROME** argues FOR (bearish case)
- **RED** argues AGAINST (bull/soft landing case)

---

## Phase 1: Pre-Debate Setup

### 1.1 Agreed Facts

Both sides accept these data points as true. No disputing during debate.

| Fact | Value | Source |
|------|-------|--------|
| KRE price (Feb 19 close) | $70.38 | Market data |
| Put/Call OI ratio (total) | ~1.9 | Market Chameleon |
| Highest put OI strike (June) | $65 (40,735 contracts) | Public.com |
| HY OAS (Feb 18) | 2.86% | FRED |
| BKLN 3-month return | -1.7% | StockAnalysis |
| KRE 3-month return | +5.9% to +18% | Multiple sources |
| Short interest | 45.6M shares (~65% float) | Fintel |
| Initial claims | 227K | DOL |
| FHLB advances | $480B | FHLB data |
| Wright 90+ DQ mortgages | 530K | Black Knight |
| Blue Owl gate date | Feb 19, 2026 | News |

**Additional agreed facts** (each side may add up to 3):

*PROME additions:*
1. ___
2. ___
3. ___

*RED additions:*
1. ___
2. ___
3. ___

### 1.2 Falsification Pre-Registration

Before arguing, each side states what would change their mind.

**PROME (bearish) would EXIT/REDUCE if:**
- *Exit trigger:* ___
- *Conviction increase trigger:* ___

**RED (bullish) would FLIP/CONCEDE if:**
- *Concede trigger:* ___
- *Conviction increase trigger:* ___

---

## Phase 2: Debate Rounds

### Round 1 — Opening Statements (500 words max)

**Requirements:**
1. State the strongest version of opponent's case first (steelman, 2-3 sentences)
2. Present your core argument with evidence
3. Declare opening probability: "I assign X% probability to the proposition"

**Order:** PROME first, then RED

### Round 2 — Crux Identification

After opening statements, each side identifies:
- The 1-2 key disagreements driving the probability gap
- Which variables, if resolved, would close the gap

**Format:** "The crux is ___. If ___ happens, I would move to ___% probability."

### Round 3 — Cross-Examination (3 questions each)

Direct questions to opponent. Must answer directly, then may elaborate.

**Rules:**
- Questions must be specific and answerable
- "I don't know" is acceptable if honest
- No compound questions (one question at a time)

**Order:** RED asks 3 questions → PROME answers → PROME asks 3 questions → RED answers

### Round 4 — Scenario Matrix

Both sides must address these three scenarios:

**Scenario A: Employment breaks**
- Definition: Initial claims >280K sustained for 4+ weeks
- PROME's probability-weighted outcome: ___
- RED's probability-weighted outcome: ___

**Scenario B: Another BDC gates or fails before April**
- Definition: Any BDC >$1B AUM gates redemptions or announces distressed merger
- PROME's probability-weighted outcome: ___
- RED's probability-weighted outcome: ___

**Scenario C: Fed announces backstop**
- Definition: BTFP 2.0, expanded discount window, or similar facility
- PROME's probability-weighted outcome: ___
- RED's probability-weighted outcome: ___

### Round 5 — Rebuttals (400 words max)

Respond to:
- Opponent's opening statement
- Cross-examination answers
- Scenario assessments

**Requirements:**
- Must concede at least one point where opponent is correct
- Must identify weakest part of own argument

**Order:** PROME first, then RED

### Round 6 — Expected Value Calculation

Both sides present EV for June $65 puts specifically.

**Template:**
```
Current premium: $X.XX
Break-even at expiry: $XX.XX
My probability of >15% decline by June: X%
My probability of total loss: X%
Expected payout if right: $X.XX
Expected loss if wrong: $X.XX
Net EV per contract: $X.XX
```

### Round 7 — Closing Statements (300 words max)

**Requirements:**
1. Final argument (no new evidence)
2. State final probability
3. State what would change your mind going forward
4. Recommended position structure given your probability

**Order:** RED first (defense closes first), then PROME

---

## Phase 3: Post-Debate

### 3.1 Update Tracking

| Metric | PROME Start | PROME End | Δ | RED Start | RED End | Δ |
|--------|-------------|-----------|---|-----------|---------|---|
| Probability | | | | | | |

The side that moved more arguably learned more.

### 3.2 Judge's Assessment

Will provides:
- Which arguments were most convincing
- Which arguments were least convincing
- Areas where both sides agreed
- His own probability assessment
- Any clarifying questions

### 3.3 Synthesis Document

After debate, Prome writes a one-page synthesis for FORGE/KRE/ containing:

1. **Areas of Agreement** — What both sides accept as true
2. **Key Disagreements** — The unresolved cruxes
3. **Monitoring Metrics** — What data points to watch weekly
4. **Position Structure Recommendation** — Allocation across expiries
5. **Decision Triggers** — Specific events that warrant action

Written in flowing prose, audio-friendly (no tables).

### 3.4 File Outputs

- Debate transcript saved to `FORGE/KRE/debates/YYYY-MM-DD_debate.md`
- Synthesis saved to `FORGE/KRE/SYNTHESIS.md`
- Update `FORGE/KRE/STATUS.md` with conclusions

---

## Conduct Rules

1. **No ad hominem** — Attack arguments, not intelligence
2. **Engage strongest version** — No strawmanning
3. **Concede when wrong** — Intellectual honesty builds credibility
4. **Source numbers** — Or mark clearly as estimates
5. **Stay within word limits** — Brevity forces prioritization
6. **Audio-friendly closing** — Final synthesis readable via TTS

---

## Scheduling

Typical debate takes 60-90 minutes of active time.

**Option A: Synchronous** — Run all rounds in one session
**Option B: Async** — Run rounds over multiple sessions with research breaks

---

*Framework version 2.1 — Updated Feb 20, 2026*
