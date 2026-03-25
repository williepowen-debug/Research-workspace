# WAL KB Index — Group Navigator
**61 rows | 10 groups | Seeded 2026-03-25**

---

## Group Map

| # | Group | Rows | IDs | Vector | Key Fact | Research Folder |
|---|-------|------|-----|--------|----------|----------------|
| 1 | HIDDEN_CRE | 7 | 001-007 | V1 | MI3 24.2% GROWING, 474% CRE/Tier 1, mgmt confirmed relabeling | `research/HIDDEN_CRE/` |
| 2 | SSFA | 6 | 008-013 | V3 | $17.2B at 20% RW, $1.1B capital savings, $10.8B "Other OBS" | `research/SSFA/` |
| 3 | CANTOR_FRAUD | 9 | 014-022 | V2 | $98M exposure, 30% reserved vs ZION 83%, $52M shortfall, OREO +2,625% | `research/` (RQ-REG-A01) |
| 4 | INSIDER | 7 | 023-029 | ALL | CFO swap (JPM FIG crisis banker), board risk additions, zero buying | `sources/INSIDER_SCAN_WAL.md` |
| 5 | GEOGRAPHIC | 6 | 030-035 | ALL | SF NCO highest (1.13%), pipeline lowest (0.26%), fast-transmission thesis | `sources/FDIC_QBP_Q4...` |
| 6 | JEFFERIES | 6 | 036-040,060 | V2 | Double-pledging chain, SMFG 20%, Convergence Day -10.64% | `research/JEFFERIES/` |
| 7 | NEVADA_GAMING | 5 | 041-045 | — | 18-22% NV exposure, Circa $420M, consumer crossover (CARL) | `sources/RENO_WAL...` |
| 8 | CAPITAL | 4 | 046-049 | V3 | CET1 11.0% (assumes SSFA), CLN doesn't cover MI3, 74% pledged | — |
| 9 | EARNINGS | 4 | 050-053 | — | Record Q4 ($2.59 EPS, $991M FY), NPL improving on surface | — |
| 10 | MARKET_SIGNAL | 7 | 054-059,061 | ALL | Two -10%+ drops, Madison "bankruptcy risk", Portnoy investigating | — |

---

## Vector Mapping

| Vector | Description | Primary Groups | Key KB Rows |
|--------|-------------|---------------|-------------|
| **V1** | Hidden CRE (MI3 reclassification) | HIDDEN_CRE, INSIDER (024) | 001-007, 024 |
| **V2** | Jefferies double-pledging / fraud pattern | CANTOR_FRAUD, JEFFERIES, MARKET_SIGNAL (054) | 014-022, 036-040, 054 |
| **V3** | SSFA capital arbitrage | SSFA, CAPITAL | 008-013, 046 |
| **ALL** | Cross-vector (insider, geographic, market) | INSIDER, GEOGRAPHIC, MARKET_SIGNAL | 023,025,027,029-035,055 |

---

## Thesis Layer Mapping

| Thesis Layer | Groups | What It Proves |
|-------------|--------|---------------|
| **Concentration** | HIDDEN_CRE, CAPITAL | True CRE 474% Tier 1, not the labeled 35% |
| **Transmission Speed** | GEOGRAPHIC | Losses bypass pipeline → direct to P&L |
| **Under-Provisioning** | CANTOR_FRAUD, EARNINGS | $52M shortfall masked by record earnings |
| **Insider Signal** | INSIDER | Coordinated repositioning (CFO, board, zero buying) |
| **Contagion Chain** | JEFFERIES, NEVADA_GAMING | Intermediary stress + consumer discretionary |
| **Capital Fragility** | SSFA, CAPITAL | $1.1B savings vanish under stress; CLN doesn't cover thesis |
| **Market Pricing** | MARKET_SIGNAL | Two -10%+ events, institutional "bankruptcy risk" calls |

---

## Earnings Prep Quick-Reference

For Apr 21 Q1 earnings, focus on:
- **HIDDEN_CRE** (001-007): Did MI3 ratio rise further?
- **CANTOR_FRAUD** (014-022): Additional reserves? Cantor resolution?
- **EARNINGS** (050-053): Provision trajectory continuing?
- **INSIDER** (023-029): Any buying? CFO Idnani first full quarter.
- **SSFA** (008-013): Any regulatory commentary?

---

## Staleness

| Stale_By | Rows | Action |
|----------|------|--------|
| 2026-03-26 | 040 | Jefferies Q1 results — PULL IMMEDIATELY |
| 2026-04-30 | 001-003,006-012,014,016,018-020,022,027,041,046-053 | Q1 data refresh at earnings |
| 2026-06-30 | 005,030-033,037 | FDIC QBP Q1 + H.8 refresh |
| No expiry | 004,017,021,023-026,028-029,034-036,038-039,042-045,054-059 | Structural/historical facts |
