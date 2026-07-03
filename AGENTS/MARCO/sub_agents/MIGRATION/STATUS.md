# MIGRATION STATUS

> ⚠️ **FROZEN 2026-07-02** — dormant sub-agent, not maintained since Apr 2026. Figures below are as-of Apr-21 and STALE (e.g. SDL-01 magnitude re-marked "2.2M CBO" → ~1.0M realized foreign-born LF / ~1.5M pop, thesis v2.6). Top-level `AGENTS/MARCO/STATUS.md` is canonical — do not cite these rows as current.

**Last Updated:** 2026-04-21 | **Status:** 🔴 RED — Domestic collapse + Sunbelt reversal + SDL-01 geographic concentration revealed + reversed-flow emigration watch

---

## SIGNAL DASHBOARD

| Indicator | Value | Date | Status |
|-----------|-------|------|--------|
| FL Net Domestic Migration | 22,517 (93% collapse from #1 to #8) | Jul 2025 | 🔴 BREACHED |
| Miami Domestic Migration | -2.0% (worse than pre-COVID NYC) | Jul 2025 | 🔴 BREACHED |
| Sun Belt Migration Delta | -534K shift (Sunbelt loses, Snowbelt gains) | 2022-2023 | 🔴 BREACHED |
| Texas Net Migration | Still positive but slowing | 2023 | 🟡 ELEVATED |
| Midwest Population Gains | First gains since 2000s | 2022-2023 | 🟡 ACTIVE |
| FL School Enrollment | Decline signaling family outmigration | 2024-2025 | 🔴 BREACHED |
| TX School Enrollment | Slowing growth | 2024-2025 | 🟡 ELEVATED |
| SDL-01 Sender Geography | AZ -6.1%, TX -5.8% ($659M), MI -5.6% lead decline; CA LEAST (-3.5%) composition-protected | 2024→2025 | 🔴 BREACHED |
| American Emigration (EMG-01) | IRS Q1 2025 renunciations +102% YoY; Brookings net migration negative first time since ~1935 | Q1 2025 | 🟡 ELEVATED (PENDING formalization) |

**Composite: 6 BREACHED, 3 ELEVATED**

---

## THESIS

The COVID-era migration boom is **explicitly reversing**. Three domestic patterns + two population-flow patterns confirm:

1. **Florida collapse:** 93% migration decline + Miami now negative = COVID bubble deflating
2. **Sunbelt-Snowbelt reversal:** -534K delta, first Midwest gains since 2000s
3. **School enrollment signal:** FL enrollment decline precedes price declines (families leave first, prices follow)
4. **SDL-01 outflow concentration:** Self-deportation of ~2.2M is NOT distributed evenly. Banxico reverse-map shows pain cluster in AZ/TX/Midwest; CA composition-protected.
5. **EMG-01 reversed-flow watch:** US-citizen emigration rising (Brookings, IRS) — not tradeable yet, 2-3yr watch.

**Key insight:** Migration turns before prices. Miami -2.0% is a leading indicator for FL housing demand withdrawal. This is the housing demand signal CARL needs for Path C confirmation.

**SDL-01 geographic concentration (Banxico reverse-map, 2024→2025):** MARCO's `tools/banxico_reverse.py` takes Banxico's Mexican-state-destination data and applies MPI/Wilson Center corridor ratios to estimate US state-of-origin flows. Top decliners: Arizona -6.1%, Texas -5.8% ($659M absolute), Michigan -5.6%. Next cluster: CO/MN/GA/WI/IN/FL -4.7 to -5.4%. California LEAST impacted (-3.5%) despite largest base ($797M absolute) — because CA's Mexican-state composition (Oaxaca/Guerrero/Yucatán indigenous flows) is flat-to-positive YoY, while Edomex/CDMX/Sinaloa/Sonora (which over-index TX/AZ/Midwest) are collapsing -14 to -20%. Full methodology: `domain/sources/SDL/BANXICO_STATE_REVERSE.md`.

**EMG-01 watch status:** WSJ "1930s levels" headline PARTIALLY SUPPORTED (net-migration angle supported; citizen-exodus angle hyperbole). Upgrade triggers: 3+ quarters IRS Federal Register >1,500 AND Canada IRCC US-PR >500/mo sustained. Full validation: `domain/sources/EMG/EMG_WSJ_VALIDATION.md`, `EMG_DATA_STREAMS.md`.

---

## ACTIVE PREDICTIONS

| ID | Prediction | Timeframe | Confidence |
|----|-----------|-----------|------------|
| MIG-01 | FL condo inventory >9 months | Q2 2026 | ✅ **RESOLVED-CORRECT Apr 17** (9.1mo Mar 2026 print; Lee 14.6mo, Miami-Dade 14.1mo) |
| MIG-02 | OIA (Orlando) airport traffic flips negative | Q2-Q3 2026 | 70% |
| MIG-03 | All 3 FL airports negative simultaneously | Q3 2026 | 65% |
| MIG-04 | Sunbelt-Snowbelt price convergence accelerates | 2026-2027 | 70% |
| MIG-05 | Q1 2026 Banxico data (Jun 2026) shows pothole from 1% remittance tax pull-forward — validates/weakens geographic concentration read | Jun 2026 | 60% |

---

## CROSS-AGENT SIGNALS

| Direction | Signal |
|-----------|--------|
| → CARL | Miami -2.0% = Path C confirmation (housing demand withdrawal, FL dimension); target AZ/TX/Midwest for SDL-01 consumer stress, NOT CA |
| → CARL | School enrollment decline → housing demand pipeline |
| → REGINALD | FL triple exposure compounding (migration + insurance + TSA); SDL-01 pain cluster = Phoenix/Tucson/Yuma, Houston/DFW/RGV, Twin Cities/Milwaukee/Indianapolis for bank-ticker screening |
| → NEXUS | Migration reversal = structural demand shift, not cyclical; SDL-01 geographic map + EMG-01 reversed-flow watch are new vectors |

---

## DATA SOURCES

- **Primary:** Census ACS (annual), IRS SOI (tax migration), Kolko/Redfin analysis
- **Secondary:** School enrollment data (leading indicator), U-Haul migration indices
- **SDL-01 sender geography:** Banxico CE100 quarterly state-destination data + MPI/Wilson Center sender-corridor ratios (`tools/banxico_reverse.py`)
- **EMG-01 watch:** IRS Federal Register quarterly expatriation lists, Canada IRCC US-PR stats, Portugal AIMA
- **Validation:** Regional price data (CARL), airport traffic (TOURISM sub-agent)
- **Research docs:** `domain/sources/SDL/`, `domain/sources/EMG/`

---

## KEY DATES

| Date | Event |
|------|-------|
| Sep 2025 | Census 2024 ACS release (migration data) |
| Ongoing | Monthly school enrollment updates |
| May 17 2026 | FL Realtors Apr 2026 — did 9.1mo hold or extend? |
| Jun 2026 | Banxico Q1 2026 BOP — validates/weakens geographic concentration; IRS Q4 2025 expatriation list |
| Q3 2026 | All 3 FL airports negative? |

---

## WORKBOOK

- `KB.tsv` — 19 migration knowledge entries
- `PREDICTIONS.tsv` — Active falsifiable predictions
- `outbox/` — Signals to CARL, REGINALD, NEXUS
