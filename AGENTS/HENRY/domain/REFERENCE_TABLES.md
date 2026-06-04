# HENRY — Static Reference Tables
*Moved from STATUS.md Mar 5 to save space. These rarely change.*

## CASCADE ORDER

| Order | Strategy | AUM | Trigger | Speed |
|-------|----------|-----|---------|-------|
| 1 | Fast Vol-Control | Multi-$T | 10-day realized vol | Immediate |
| 2 | Short-Term CTAs | ~$100B | 50-DMA breach (6,883) | Days |
| 3 | Medium-Term CTAs | ~$200B | 6,707 close below → $80B | 1-4 weeks |
| 4 | Longer-Duration CTAs | ~$200B+ | ~6,494 sustained below | Weeks |
| 5 | Risk Parity | ~$1T | Cross-asset correlation | Monthly |

## LEADING INDICATOR SEQUENCE

```
MOVE rises (VIX flat)       → 2-5 days before
VIX inverts (spot > futures) → 1-3 days before
GEX thins (<$2B)            → 1 day before
DIX drops (<40%)            → 1-2 days before
PUT WALL BREAKS             → T-0: Cascade begins
CTAs flip at 6,494          → T+1 to T+5
Risk parity deleverages     → T+5 to T+30
```

## CREDIT-EQUITY TRANSMISSION

| HY OAS 5-Day Change | Equity Impact | Lead Time |
|---------------------|---------------|-----------|
| +25-50 bps | -2% to -5% | 2-3 sessions |
| +50-100 bps | -5% to -10% | 0-1 session |
| +100+ bps | -10%+ | Same day |

## TRANSMISSION PATHS

- **LABOR → HENRY:** Claims >300K = fundamental trigger → gamma test of Put Wall
- **HENRY → CARL:** SPX -10%+ → Reverse Wealth Effect → spending pullback. SBC amplifies to $19-26T wealth destruction.
- **SAM → HENRY:** Yen appreciation = carry unwind = Aug 2024 playbook

## SENTIMENT REVERSAL FRAMEWORK (3-pillar)
*Reusable structure from KB ML-HEN-021 (Jan'26); read the pillars, pull live readings — don't cite the archived Jan levels.*

| Pillar | What to read | Reversal-risk signature |
|--------|--------------|-------------------------|
| 1. Positioning | AAII / NAAIM allocation | Fully-invested both = exhausted upside |
| 2. Structural leverage | FINRA margin debt + retail options share | Record margin + high 0DTE/retail = fragile |
| 3. Smart-money distribution | Insider sell/buy ratio | >3σ from ~2-3:1 norm = distribution phase |

## SENTIMENT / FLOW DATA SOURCES (release cadence)
*From KB ML-HEN-025 (Jan'26). Where to pull each input.*

| Source | Cadence | Source | Cadence |
|--------|---------|--------|---------|
| AAII | Thu | ICI fund flows | Wed |
| Investors Intelligence | Wed | OCC options | Daily |
| CNN Fear & Greed | Real-time | Fintel insiders | Daily |
| NAAIM | Thu | NASDAQ short interest | Bi-monthly |
| FINRA margin | Monthly | | |
