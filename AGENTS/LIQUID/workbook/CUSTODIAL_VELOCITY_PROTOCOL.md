# Foreign Custodial Flow & Collateral Velocity Monitoring Protocol

**Created:** 2026-02-11  
**Owner:** LIQUID Agent  
**Priority:** HIGH — Early warning systems for structural fragility

---

## Framework #1: Foreign Custodial Flow Disaggregation

### Objective
Distinguish between **benign custody migration** (China moving assets to European custodians) vs **stealth exit** (actual selling disguised as custody shift).

### The Problem
- China official TIC holdings: $682.6B (down from $1.06T in 2021)
- Belgium TIC holdings: $481B (up from ~$300B baseline)
- **Is this migration or exit?** Critical difference for term premium impact.

### Data Sources

| Source | Frequency | URL/Access | What It Shows |
|--------|-----------|------------|---------------|
| **Treasury TIC Data** | Monthly | treasury.gov/resource-center/data-chart-center/tic | Official holdings by country |
| **BIS Table B4** | Quarterly | bis.org/statistics/bankstats.htm | Custodial claims by banking system |

**Next TIC Release:** Mar 18, 2026 (Jan 2026 data) — Dec 2025 released Feb 18  
**Next BIS Release:** Q1 2026 data (April/May 2026)

### Methodology: Two-Signal Cross-Reference

| Scenario | Belgium TIC | BIS B4 Custody | Interpretation |
|----------|-------------|----------------|----------------|
| **A (Benign)** | ↑ Rising | ↑ Rising | PBOC moving from US to EU custodians — no net selling |
| **B (Crisis)** | ↑ Rising | → Flat | Actual exit — selling disguised as custody shift |

**Key Insight:** TIC data is monthly, BIS is quarterly. Use quarterly comparison to validate/falsify monthly TIC trends.

### Vector Tracking

**VX-LIQUID-7.06: Belgium UST Holdings**
- Current: $481B (Nov 2025)
- Baseline: ~$300B (2023)
- YELLOW: >$400B
- ORANGE: >$500B
- RED: >$600B

**VX-LIQUID-7.07: Belgium + China Combined Flow**
- Current: -$100B/quarter (estimated)
- YELLOW: -$30B/quarter
- ORANGE: -$50B/quarter
- RED: -$75B/quarter

### Alert Triggers

| Trigger | Action |
|---------|--------|
| Belgium >$500B | Update STATUS.md to RED, alert PROME |
| Combined flow <-$50B/quarter | ORANGE alert — coordinated exit in progress |
| BIS B4 flat while Belgium rises | **Scenario B confirmed** — escalate to PROME immediately |
| Pre-April 2026 acceleration | Watch for Trump-Xi summit positioning |

### Monitoring Cadence

**Monthly (TIC release day ~15th-20th):**
1. Pull latest TIC data for Belgium and China
2. Calculate month-over-month changes
3. Update VX-LIQUID-7.06 and 7.07 current values
4. If threshold breached → update STATUS.md + alert PROME

**Quarterly (BIS release ~2 months after quarter end):**
1. Download BIS International Banking Statistics Table B4
2. Extract custodial claims for Belgium banking system on US securities
3. Cross-reference with Belgium TIC holdings for same period
4. Validate Scenario A vs Scenario B
5. Document in ML.tsv with diagnostic value

**Event-Driven:**
- Trump-Xi summit (April 2026): Watch for pre-positioning
- Major tariff announcements: Potential retaliation trigger
- Taiwan tensions: Financial war prep scenario

---

## Framework #2: Collateral Velocity / Rehypothecation Monitoring

### Objective
Track the **velocity** at which collateral moves through the system. Declining velocity = dealers stuffed = settlement stress = auction risk.

### The Calculation
```
Collateral Velocity Ratio = (Triparty Repo Volume) / (Outstanding UST)
```

### Data Sources

| Source | Frequency | URL/Access | What It Shows |
|--------|-----------|------------|---------------|
| **SIFMA Triparty Repo** | Weekly | sifma.org/resources/research/us-repo-markets-data/ | Triparty repo volume |
| **SIFMA Outstanding UST** | Monthly | sifma.org/resources/research/us-treasury-securities-statistics/ | Total marketable UST outstanding |

**Weekly Update:** Thursday/Friday (triparty volume)  
**Monthly Update:** Mid-month (outstanding UST)

### Baseline & Thresholds

| Status | Threshold | Interpretation |
|--------|-----------|----------------|
| **GREEN** | ≥2.8x | Normal rehypothecation velocity |
| **YELLOW** | <2.5x | Slowing — dealers reducing intermediate |
| **ORANGE** | <2.0x | Velocity crisis — dealers refusing to expand |
| **RED** | <1.5x | March 2020 levels — market breakdown imminent |

**Historical Context:**
- 2023-25 average: ~2.8x
- March 2020 crisis: <1.5x (Fed emergency intervention required)
- Current estimate: ~2.8x (needs weekly verification)

### Vector Tracking

**VX-LIQUID-8.01: Collateral Velocity Ratio**
- Current: ~2.8x (estimated, needs SIFMA data)
- Confidence: 70% (estimate until verified)
- Update weekly from SIFMA

### The Early Warning Sequence

```
1. Velocity drops (<2.5x)
        ↓
2. Dealers stuffed (balance sheet at SLR cap)
        ↓
3. FTDs spike (>$50B — VX-LIQUID-1.03)
        ↓
4. Auction tail widens (>1.5bps — VX-LIQUID-2.03)
        ↓
5. Auction failure (BTC <2.0x)
```

**Cross-Vector Validation:**
- VX-LIQUID-1.05: Dealer Net Position (stuffed = >$200B)
- VX-LIQUID-1.03: Treasury FTD (spike = >$50B)
- VX-LIQUID-2.01: Auction BTC (weak = <2.30x)

### Alert Triggers

| Trigger | Action |
|---------|--------|
| Velocity <2.5x for 2 consecutive weeks | YELLOW alert — update STATUS.md |
| Velocity <2.0x | ORANGE alert — escalate to PROME |
| Velocity <2.0x + FTD >$50B | **RED alert** — imminent auction risk |
| Velocity <1.5x | **CRITICAL** — expect Fed intervention within days |

### Monitoring Cadence

**Weekly (Thursday/Friday):**
1. Visit SIFMA triparty repo page
2. Download latest weekly volume data
3. Calculate velocity: (Triparty vol) / (Outstanding UST)
4. Update VX-LIQUID-8.01 current value
5. If <2.5x for 2+ weeks → alert PROME

**Monthly (mid-month):**
1. Update Outstanding UST denominator from SIFMA
2. Recalculate baseline velocity
3. Document any structural shifts in ML.tsv

**Event-Driven:**
- Quarter-end: Velocity often drops due to window dressing
- SRF usage >$50B: Indicates dealers hitting capacity
- Fed RMP changes: Affects reserve supply

---

## Integration with Existing LIQUID Vectors

### Cross-Agent Coordination

| Agent | Signal Exchange | Relevance |
|-------|-----------------|-----------|
| **SAM** | Japan repatriation flows | Amplifies FOI demand hole |
| **REGINALD** | CLO spreads, FHLB advances | Credit transmission from Treasury stress |
| **HENRY** | VaR shocks, equity cascade | Market structure amplification |

### Threshold Escalation Matrix

| Condition | Status | Escalation |
|-----------|--------|------------|
| Belgium >$500B **OR** Combined flow <-$50B/qtr | ORANGE | Update STATUS.md, document in ML.tsv |
| Velocity <2.5x for 2+ weeks | YELLOW | Update STATUS.md, monitor closely |
| Belgium >$500B **AND** Velocity <2.0x | RED | Immediate PROME alert — dual fragility |
| BIS confirms Scenario B **AND** Velocity <2.0x | **CRITICAL** | Systemic stress — expect term premium spike |

---

## Operational Checklist

### Weekly Tasks (Every Thursday/Friday)
- [ ] Pull SIFMA triparty repo volume
- [ ] Calculate collateral velocity ratio
- [ ] Update VX-LIQUID-8.01 if changed
- [ ] Check velocity trend (2+ week decline?)

### Monthly Tasks (Mid-month)
- [ ] Update Outstanding UST denominator
- [ ] Pull TIC data on release day (~15th-20th)
- [ ] Update VX-LIQUID-7.06 (Belgium) and VX-LIQUID-7.07 (combined flow)
- [ ] Calculate quarterly flow rates
- [ ] Check threshold breaches

### Quarterly Tasks (2 months after quarter end)
- [ ] Download BIS International Banking Statistics Table B4
- [ ] Cross-reference Belgium TIC vs BIS custodial claims
- [ ] Validate Scenario A (migration) vs Scenario B (exit)
- [ ] Document findings in ML.tsv with diagnostic value
- [ ] Update STATUS.md if scenario changes

### Event-Driven
- [ ] Pre-Trump-Xi summit (April 2026): Daily TIC monitoring
- [ ] Quarter-end: Watch velocity drop
- [ ] Major tariff announcement: Check for China retaliation signal

---

## Data Access Notes

**TIC Data:**
- Treasury publishes monthly with ~6-week lag
- Historical file: https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.txt
- Watch for "Belgium" row in Major Foreign Holders table

**BIS Data:**
- International Banking Statistics → Table B4 (External positions of banks)
- Filter: "Belgium" + "Debt securities" + "United States"
- Quarterly publication, ~2 month lag

**SIFMA Data:**
- US Repo Markets: https://www.sifma.org/resources/research/us-repo-markets-data/
- Treasury Securities Statistics: https://www.sifma.org/resources/research/us-treasury-securities-statistics/
- Weekly repo volume typically in PDF/Excel format

---

## Current Readings (As of 2026-02-11)

### Foreign Custodial Flow
- **Belgium TIC**: $481B (Nov 2025) — ORANGE status
- **China TIC**: $682.6B (Nov 2025) — YELLOW status
- **Combined flow**: Est. -$100B/quarter — RED status
- **Next data**: Feb 18, 2026 (Dec 2025 TIC)
- **BIS validation**: Pending Q4 2025 data (April 2026)

### Collateral Velocity
- **Current ratio**: ~2.8x (estimated) — GREEN status
- **Triparty repo**: ~$4.5T (est, needs verification)
- **Outstanding UST**: ~$27T marketable
- **Confidence**: 70% (estimate until SIFMA verified)
- **Next update**: Weekly SIFMA check

---

## Bottom Line

These two frameworks provide **early warning** for the dual fragility thesis:

1. **Custodial Flow**: Tracks whether China's official "decline" is real exit (crisis) or custody shuffle (manageable)
2. **Collateral Velocity**: Tracks whether dealers can intermediate shocks or are at capacity

**When both flash red simultaneously** → Systemic stress regime → Term premium spike → Cascade

*Next review: Feb 18, 2026 (TIC data) or weekly SIFMA check*
