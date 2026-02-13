# LIQUID Session Context — Fresh Start Guide

**Purpose:** Context document for a fresh Claude session to update/verify LIQUID agent
**Created:** 2026-01-26
**For:** New session that hasn't seen previous conversation

---

## WHAT IS LIQUID?

LIQUID is a monitoring agent for **US Treasury and funding markets**. It tracks:
- Repo/SOFR rates (overnight funding costs)
- RRP balance (Fed's reverse repo facility — liquidity buffer)
- Treasury auction demand
- Settlement stress (Fails-to-Deliver)
- Bank funding (FHLB advances)
- Cross-border funding (USD/JPY basis)

**Location:** `C:\Projects\LIQUID\`

---

## CURRENT STATE (As of 2026-01-25)

LIQUID was initialized but **needs baseline verification**. The values in the skeleton may be stale.

| Vector | Current Value | Status | Needs Verification? |
|--------|---------------|--------|---------------------|
| SOFR-IORB Spread | +3bps | GREEN | YES — check NY Fed |
| RRP Balance | $2.5B | RED | YES — check NY Fed |
| Treasury FTD | $42.4B | YELLOW | YES — check SEC data |
| Auction BTC | 2.5x | GREEN | YES — check recent auctions |
| Indirect Bid % | 68% | GREEN | YES — check recent auctions |
| FHLB Advance Rate | "Normal" | GREEN | YES — needs quantification |
| CCY Basis USD/JPY | -45bps | GREEN | YES — check current |

**Key Concern:** RRP is flagged as RED ($2.5B = depleted). Verify this is still accurate.

---

## YOUR TASK

### Option A: Quick Verification (UPDATE session)
Verify current values for all 7 vectors using OSINT sources:
1. NY Fed for SOFR, RRP
2. TreasuryDirect for recent auction results
3. SEC for FTD data
4. Proxy sources for CCY basis

Update `workbook/VX.tsv` with verified values.

### Option B: Full Research (Like REGINALD)
Create research prompts in `research/` folder for deep research LLM sessions:
1. RRP depletion historical analysis
2. Treasury auction demand trends
3. FHLB stress indicators
4. Japan repatriation flow sizing
5. Settlement stress (FTD) patterns

This approach worked well for REGINALD — generated prompts, ran them through a deep research LLM, then imported results.

### Option C: Hybrid
Do quick verification for easy-to-check items (SOFR, RRP, recent auctions), create research prompts for complex items (FHLB, Japan flows).

---

## KEY FILES TO LOAD

```
C:\Projects\LIQUID\
├── CLAUDE.md                    # Agent instructions (load first)
├── LIQUID_SKELETON.md           # Domain skeleton with thresholds
├── RESEARCH_STATUS.md           # What research is pending
├── workbook/
│   └── VX.tsv                   # Current vector values
```

**Also relevant:**
- `C:\Projects\META\MONITORING_CHECKLIST.md` — Central monitoring dashboard (LIQUID section needs populating)
- `C:\Projects\META\NETWORK_ENHANCEMENT_HANDOFF.md` — Network status overview

---

## DATA SOURCES

### Primary (OSINT)

| Metric | Source | URL |
|--------|--------|-----|
| SOFR Rate | NY Fed | https://www.newyorkfed.org/markets/reference-rates/sofr |
| RRP Balance | NY Fed | https://www.newyorkfed.org/markets/desk-operations/reverse-repo-counterparties |
| Treasury Auctions | TreasuryDirect | https://www.treasurydirect.gov/auctions/results/ |
| FTD Data | SEC | https://www.sec.gov/data-research/sec-markets-data/fails-deliver-data |
| FHLB Data | FHLB Office of Finance | https://www.fhlb-of.com/ |

### Proxy Sources (When Terminal Data Unavailable)

| Need | Proxy | Source |
|------|-------|--------|
| CCY Basis | USD/JPY forward points | Investing.com |
| Dealer stress | Auction tails | TreasuryDirect |
| Bank funding stress | FHLB debt issuance news | Bloomberg/Reuters |

---

## CROSS-AGENT CONTEXT

### From REGINALD (Relevant Findings)

REGINALD research identified signals relevant to LIQUID:

1. **BDC Stress (ORANGE):** -16% NAV discount means $142B in unfunded bank credit lines could be drawn. If triggered, banks would need FHLB funding → LIQUID should monitor FHLB advance surge.

2. **Japan "Great Rotation":** Japan banks are NOT selling USTs — they're rotating INTO CLOs. The repatriation risk to Treasury markets may be lower than initially assumed. However, the "bid withdrawal" risk remains if US credit cycle turns.

3. **Transmission Trigger Changed:** No longer Fed rate policy — now US credit cycle deterioration. This affects LIQUID's Japan repatriation thesis.

### Signal from REGINALD to LIQUID (Latent)

```yaml
signal:
  from: REGINALD
  to: LIQUID
  priority: LATENT
  topic: "BDC-Bank Transmission Pre-loaded"
  content: |
    BDC sector at -16% discount (ORANGE).
    $142B unfunded bank lines represent contingent liability.
    If CLO spreads widen to 150bps+, BDC draws could stress regional bank liquidity.
    LIQUID should monitor FHLB advance surge as secondary indicator.
```

---

## RESEARCH PROMPT TEMPLATE

If you create research prompts (Option B), use this structure:

```markdown
# Research Prompt: [TOPIC]

**Vector:** VX-LIQUID-X.XX
**Priority:** HIGH/MEDIUM/LOW
**Estimated Scope:** Simple/Medium/Complex

---

## Objective
[What we're trying to learn]

## Research Tasks
1. [Task 1]
2. [Task 2]
3. [Task 3]

## Output Format
[Structured format for results]

## Sources to Check
- [Source 1]
- [Source 2]

## Data Quality Notes
[Caveats, lags, limitations]
```

---

## SUGGESTED RESEARCH PROMPTS (If Going Option B)

### 1. RRP Balance & Historical Patterns (HIGH)
- Current RRP balance verification
- Historical pattern when RRP approached zero
- What happened to SOFR in those periods
- Fed response patterns

### 2. Treasury Auction Demand Analysis (MEDIUM)
- Recent auction results (4-week, 3-month, 10-year, 30-year)
- BTC trends over past 6 months
- Indirect bid % trends (foreign demand proxy)
- Any auction "tails" (weak demand signals)

### 3. Settlement Stress / FTD Analysis (MEDIUM)
- Current FTD levels
- Historical patterns
- What drove the $42.4B level
- Correlation with other stress indicators

### 4. FHLB System Health (MEDIUM)
- Current advance rates (if available)
- Recent FHLB debt issuance
- Any news on bank draws
- Historical stress precedents (2023 banking crisis)

### 5. Cross-Currency Basis (LOW)
- Current USD/JPY basis
- Trend over past year
- Correlation with Japan institutional flows
- Hedging cost impact on Japan holdings

---

## THRESHOLDS QUICK REFERENCE

| Vector | GREEN | YELLOW | ORANGE | RED |
|--------|-------|--------|--------|-----|
| SOFR-IORB | <+15bps | +15bps | +25bps | +50bps |
| RRP Balance | >$50B | $10-50B | $5-10B | <$5B |
| Treasury FTD | <$40B | $40-50B | $50-60B | >$60B |
| Auction BTC | >2.3x | 2.0-2.3x | 1.8-2.0x | <1.8x |
| Indirect Bid | >65% | 60-65% | 55-60% | <55% |
| FHLB Advance | Normal | >75% | >85% | Delivery issues |
| CCY Basis | >-60bps | -60 to -75 | -75 to -100 | <-100bps |

---

## SESSION WORKFLOW

1. **Load CLAUDE.md** — Contains startup protocol
2. **Check inbox** — `C:\Projects\AGENT_COMMS\LIQUID_INBOX\` for any signals
3. **Verify vectors** — Update VX.tsv with current values
4. **Create research prompts** (if needed) — Save to `research/` folder
5. **Update RESEARCH_STATUS.md** — Document what was done
6. **Update MONITORING_CHECKLIST.md** — Populate LIQUID weekly check values
7. **Create handoff** — `handoffs/LIQUID_002_HANDOFF.md`

---

## EXPECTED OUTPUT

After this session, LIQUID should have:
- [ ] Verified current values for all 7 vectors
- [ ] Updated VX.tsv with fresh data
- [ ] Research prompts created (if deep research needed)
- [ ] MONITORING_CHECKLIST.md LIQUID section populated
- [ ] Handoff document created
- [ ] Any signals to SAM/REGINALD identified

---

## NOTES ON RESEARCH QUALITY

From REGINALD experience: Agent #2 (deep research LLM) produced significantly better analysis than others. If creating research prompts for external execution, use that agent.

Quality markers to look for:
- Goes beyond data retrieval to analysis
- Explains mechanisms and "why"
- Identifies risks not in the prompt
- Professional report structure
- Clear sourcing

---

*Context document for LIQUID session — 2026-01-26*
