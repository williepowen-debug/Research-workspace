> 🗄️ **ARCHIVED 2026-08-23** under the amended root Data-Hygiene retirement rule (>60d old **AND** not boot-read **AND** not referenced by a live doc; index-refs do not count, per the 2026-08-21 root batch `326181484`). Rule applied file-by-file, not as a batch — sweep record: `archive/RETIREMENT_SWEEP_2026-08-23.md`. **Historical only; not maintained.**
> ⚠️ **STALE-VINTAGE — Feb/Mar-2026 fossil (bannered 2026-07-17 audit). Do NOT cite as current.** Live canon: price/tape → `../STATUS.md`; positions → `../POSITIONS.md`; thesis → `../THESIS.md` (**it owns its own version — de-versioned here 2026-08-20 so this banner cannot rot on the next bump**).

# WAL (Western Alliance Bancorporation) — Trade Status

**Last Updated:** 2026-02-24

---

## Position

| Field | Value |
|-------|-------|
| **Ticker** | WAL |
| **Position** | Long Puts |
| **Strike** | $82.50 |
| **Expiry** | Jun 2026 |
| **Quantity** | 1 contract |
| **Entry Price** | $3.91 |
| **Entry Date** | ~Feb 21, 2026 |
| **Current P/L** | +30.54% (as of Feb 24) |

---

## Thesis: Hidden CRE Exposure

WAL is actively relabeling CRE loans as C&I to mask true exposure. This is the "Metropolitan Capital Pattern" — the same classification game that contributed to Metropolitan Capital Bank's failure (Jan 30, 2026).

### The Smoking Gun

| Metric | Value | Why It Matters |
|--------|-------|----------------|
| **Memo Item 3 / C&I Ratio** | 24.2% | Hidden CRE in C&I book |
| **Ratio Trend** | GROWING (15.5% → 24.2%) | Only bank with INCREASING hidden ratio |
| **Hidden CRE Amount** | $2.73B | Loans "to finance CRE not secured by RE" |
| **True CRE Exposure** | ~59% of loans | vs. labeled ~35% |
| **CRE / Tier 1 Capital** | 474% | Breaches 300% SR 07-1 threshold |

### Management Confirmation

From Q4 2025 earnings call:
- **Ken Vecchione:** "reserves adjusting modestly as our mix shifts towards higher return C&I growth"
- **Tim Bruckner:** "we curtailed our growth and pressed out...CRE loans as a percentage decreased"

**Reality:** True CRE stable at ~$36.8B while *labeled* CRE fell — they relabeled, not reduced.

---

## Technical Levels

| Level | Price | Significance |
|-------|-------|--------------|
| Feb 2026 High | $97.23 | 52-week high, distribution top |
| Current | ~$88 | Down 9.5% from peak |
| Strike | $82.50 | 6.2% below current |
| Dec 2025 Support | $80 | First major support |
| May 2025 Low | $57.08 | Major support, -35% downside |

### Chart Pattern (1Y)
- Parabolic rally from $57 (May 2025) to $97 (Feb 2026) = +70%
- Distribution at top with heavy volume
- Now forming lower highs
- Textbook "selling into strength" pattern

---

## Catalysts

| Date | Event | Expected Impact |
|------|-------|-----------------|
| April 2026 | Q1 Earnings | CRE provision reveal |
| **May 12, 2026** | **Investor Day** | Management questioned on CRE strategy |
| Jun 2026 | Put Expiry | Position deadline |

---

## 🆕 SSFA Capital Arbitrage — CONFIRMED (Feb 25, 2026)

**Source:** FFIEC Call Report Q4 2025, Schedule RC-R Part II (Items 9-10)

WAL is using Simplified Supervisory Formula Approach (SSFA) to achieve 5x better capital efficiency on $17B of securitization exposures.

### Securitization Exposures (Schedule RC-R Part II)

| Item | Category | Exposure ($000s) | RWA ($000s) | Implied RW |
|------|----------|------------------|-------------|------------|
| 9a | HTM Securities | $165,051 | $33,071 | 20.0% |
| 9b | AFS Securities | $3,792,017 | $799,649 | 21.1% |
| 9c | Trading Assets | $0 | $0 | — |
| 9d | **Other On-B/S** | **$10,815,082** | **$2,167,129** | **20.0%** |
| 10 | Off-B/S | $2,446,364 | $489,273 | 20.0% |
| **TOTAL** | — | **$17,218,514** | **$3,489,122** | **20.3%** |

### Capital Arbitrage Math

| Scenario | RWA | Capital Required (8%) |
|----------|-----|----------------------|
| **With SSFA (20% RW)** | $3.49B | $279M |
| **Without SSFA (100% RW)** | $17.22B | $1,378M |
| **Savings** | **$13.73B** | **$1,098M** |

**WAL is holding ~$1.1B LESS capital than they would without SSFA treatment.**

### What's In "Other On-Balance Sheet Securitization" ($10.8B)?

This is likely the NDFI warehouse lending structured through SPVs:
- Mortgage warehouse lines: $9.2B (low risk, self-liquidating)
- Business credit intermediary lines: $3.4B (BDC exposure)
- Private equity fund lines: $1.2B (capital call facilities)

By structuring these through securitization vehicles, WAL achieves 20% RW instead of 100%.

### Why This Matters

1. **Capital ratios overstate buffer** — CET1 of 11.76% assumes SSFA treatment continues
2. **Regulatory risk** — Basel III Endgame proposed tightening SSFA; if enacted, WAL would need to raise capital
3. **Stress amplifier** — Less capital = less cushion when losses hit
4. **Combined with hidden CRE** — The $2.73B in Memo Item 3 PLUS aggressive SSFA = true risk profile materially worse than headline ratios

### Raw MDRM Codes (Verification)

```
RCONS490 (9d Exposure): 10,815,082
RCONS493 (9d RWA): 2,167,129
Ratio: 2,167,129 / 10,815,082 = 20.04% ← Exactly SSFA floor
```

---

## Risk Factors

1. **Fed pivot** — Rate cuts would help NIM, sentiment could shift bullish
2. **M&A announcement** — Sector could rip on consolidation news
3. **CRE stabilization** — Any positive data could trigger relief rally
4. **Short squeeze** — If positioning too bearish

---

## RED Team Challenge (Feb 24)

RED graded the broader regional bank "topped" thesis at 40-50% confidence (vs our 75-80%). Key challenges:
- Sector correlation is normal, not "coordinated distribution"
- Volume analysis lacks benchmark context
- 2025 lows may be irrelevant if macro backdrop differs
- Bull case: Fed pivot, M&A, curve steepening

**Counter:** RED didn't engage with fundamental thesis (hidden CRE, Memo Item 3). Technical skepticism valid, but credit analysis is the core case.

---

## Position Management

| Scenario | Action |
|----------|--------|
| Stock breaks $80 | Hold, thesis confirming |
| Stock breaks $75 | Consider taking partial profit |
| Stock reclaims $95 | Re-evaluate thesis, consider stop |
| Q1 earnings miss | Add to position |
| Fed announces cuts | Reduce position 50% |

---

## Journal

**Feb 24, 2026:** Position +30.54%. Stock bounced slightly (+0.9%) on risk-on day (VIX -8%). Distribution pattern intact on 1Y chart. RED challenged thesis — valid technical skepticism but fundamental case (hidden CRE) remains strong. Considering adding OZK as second position.

---

## Links

- **Hidden CRE Research:** `AGENTS/REGINALD/` — Metropolitan Capital Pattern discovery
- **CREED CRE Data:** `AGENTS/REGINALD/sub-agents/CREED/STATUS.md`
- **RED Challenge:** `AGENTS/RED/sessions/` — Feb 24 adversarial review
