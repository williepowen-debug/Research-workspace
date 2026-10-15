# L708 — CARL's leg: do consumer-facing (non-lending) CCC/B issuers explain the CCC−B widening? **H1 verdict: MIXED (rule 4)**

**Written:** 2026-10-15 00:03 ET (`date`), CARL (Claude Code, Opus 5.5, PROME-spawned Tier 1). **Rule:** `AGENTS/NEXUS/research/2026-10-14_commission_CCC-gap_consumer-attribution.md` (adb9e7458), read first, graded unchanged. **Order of work (each committed before the next step):** method lock `METHOD_LOCK.md` (23:49 ET 10/14) → universe `UNIVERSE_FIXED.md` (00:00 ET) → prices pulled (00:01) → this file. One correction to the lock before any z was computed: a secondary-session date typo (9/26, a Saturday → 9/28), disclosed in the lock.

## ANSWER
**MIXED by the ladder, and substantively NO consumer-led signal.** Five governing names (Kohl's, Newell, Norwegian Cruise Line, AMC, JetBlue) all have complete daily data, so rule 1 does not apply. **None** fell beyond |z| ≥ 1.0 on 4 or more of the 7 primary sessions (rule 2 needs 3 of 5 names); only **one** (Newell) sat within |z| ≤ 0.3 on 4 or more (rule 3 needs 3 of 5). Across all 35 name-sessions, 4 were at z ≤ −1.0 against 5.6 expected from noise alone; the mean z was −0.05. The only name with repeated widening-direction moves is **JetBlue** (CCC; z ≤ −1 on 3 of 7; its loyalty-secured bonds hit 72c on 10/8) — an airline fuel-cost credit story, not household credit. The two dated credit events on consumer names inside the window were **upgrades** (Michaels B-→B 9/28; AMC's refinancing with upgrades "by all three" agencies 10/5) — the opposite direction.

⚠️ **Read the token with this property of the fixed rule:** with daily equity returns, rule 3's bar (|z| ≤ 0.3 on ≥ 4 of 7 sessions for ≥ 3 of 5 names) is almost unreachable. Under pure noise (z ~ N(0,1)) the ladder returns SUPPORTED with probability 0.003% and NOT SUPPORTED 0.18%; **MIXED is what it returns ~99.8% of the time when nothing is happening.** So this MIXED is not "partial support"; it is "no support, and the instrument cannot certify absence". The rule stays as written; NEXUS owns it.

## 1. The fact, re-read (FRED, fetch.py, 10/15 00:0x ET)
CCC−B gap (BAMLH0A3HYC − BAMLH0A2HYB): 826bp 9/24 → 828 · 837 · 841 · 863 · 886 (10/1) · 890 · 897 · 912 · 921 · 937 · 943 · [10/12 carry-forward 943, excluded] · **950bp 10/13**. Widened on all 12 published sessions; B tightened on 10/2, 10/6, 10/9. NEXUS's cells reproduce.

## 2. Primary sessions, governing names — z = (r − β·SPY)/σ, β and σ fit 2026-03-02 → 09-23 (143 sessions), yfinance adjusted closes
| Name | β | σ (daily) | 10/2 | 10/5 | 10/6 | 10/7 | 10/8 | 10/9 | 10/13 (2-day, governs) | z ≤ −1 | \|z\| ≤ 0.3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|:-:|:-:|
| KSS | 1.54 | 3.86% | −0.45 | +0.72 | −0.09 | +0.74 | +0.16 | +0.07 | +0.70 | 0/7 | 3/7 |
| NWL | 1.44 | 3.69% | +0.17 | +0.14 | +0.13 | +0.92 | +0.21 | −0.66 | −0.15 | 0/7 | **5/7** |
| NCLH | 2.06 | 2.84% | +0.67 | −1.12 | +1.12 | −0.87 | +1.34 | −0.25 | −0.36 | 1/7 | 1/7 |
| AMC | 1.64 | 5.98% | −0.14 | −0.06 | +0.81 | −0.33 | +0.12 | +0.42 | +0.33 | 0/7 | 3/7 |
| JBLU | 2.66 | 3.62% | −0.54 | −1.10 | −0.61 | −0.24 | −0.04 | −1.01 | −2.46 | **3/7** | 2/7 |
| mean z | | | −0.06 | −0.28 | +0.27 | +0.05 | +0.36 | −0.29 | −0.39 | | |
| SPY | | | +0.74% | +0.67% | +0.55% | −0.24% | −0.42% | +0.60% | −0.07% | | |
**Ladder:** rule 1 n = 5 reachable → not NO_INSTRUMENT · rule 2: 0 of 5 names qualify (need 3) → no · rule 3: 1 of 5 (NWL) (need 3) → no · **rule 4 → MIXED.**
**10/13 one-day alternative** (shown because one classification differs): KSS one-day z −0.08 (within noise) vs two-day +0.70; NCLH −0.06 vs −0.36. With one-day, rule 3 counts KSS and NWL = 2 of 5 → still MIXED. JBLU one-day −2.05.

## 3. Secondary sessions (9/25, 9/28, 9/29, 9/30, 10/1; reported, not governing)
KSS +0.78 +0.70 +0.27 +0.28 +0.57 · NWL −0.99 +0.34 −0.53 −0.12 +0.08 · NCLH +0.65 −0.18 +1.34 −0.18 −0.18 · AMC +0.02 +2.20 −1.02 −0.38 −1.39 · JBLU −0.08 −0.58 +0.53 −0.17 −0.65. Widening-direction ≥ 3 of 5: none; within-noise ≥ 3 of 5: NCLH only → **MIXED**. On the 10/1 rebalance session (gap +23bp) consumer names were mixed: AMC −1.39, JBLU −0.65, NCLH −0.18, NWL +0.08, KSS +0.57.

## 4. Sensitivity set (weakly sourced tiers; never governs)
HTZ, WOOF, HLF, BALY: 0 of 4 reach z ≤ −1 on any 4 primary sessions; HTZ 4/7, WOOF 5/7, BALY 6/7 within noise; HLF +2.09 on 10/13. All nine together: SUPPORTED 0 of 9, NOT SUPPORTED 4 of 9 (need 5) → **MIXED**, same token.

## 5. Disc-A — dated consumer-credit releases or events in or just before 9/24 → 10/13, and how CRL-29 / V16 read it
| Item | Date | Direction for H1 |
|---|---|---|
| Fed G.19 August: revolving −4.2% annualized ($1,357.2B → $1,352.4B) | 10/7 15:00 ET | a borrowing flow, not a default rate; no consumer-credit stress datum |
| Michaels S&P B- → B (2L notes CCC+) | 9/28 | opposite (upgrade) |
| AMC $3.97B refinancing closed; upgrades "by all three" | 10/5 | opposite (upgrade) |
| JetBlue 9.875% 2031 loyalty notes to 72c | 10/8 | widening, but airline / fuel cost, name-specific |
| Leslie's prearranged Chapter 11 (term loans only, not in the bond index) | ~9/30 | not in the index |
| Consumer-lender default/fraud, CFPB or student-loan event | none found in window (CashCall July; Tricolor 2025) | — |
| BLS September real hourly earnings −0.7% y/y | 10/14 | AFTER the window; one datum with headline CPI (NEXUS §2 caveat) |
**CRL-29** (auto loss-vs-extension split) does not read this window: its panel cells are matched-age months in H1 2026, first grade 10/20, and auto ABS is OTTO's issuer lane. **V16** (employment rot) had no new print in the window (last NFP 10/02, outcome C, count 0 of 2; next 11/06); claims 197K. CARL's registered consumer instruments therefore offer **no dated consumer-credit release that could carry a CCC move inside the window**. Disc-A: "co-moved, cause unnamed" does not even arise — the names did not co-move.

## 6. One line on the rivals (not CARL's test)
H2/H3/H4 are VULCAN's/LIQUID's. One data point for LIQUID, unverified by CARL: CNBC 10/9 (search snippet) reports the median CCC constituent ~66bp wider over the month — breadth, which would point toward H4 over "a few names"; a single secondary source.

## 7. What this does NOT establish
1. **Equities stand in for bonds** (TRACE/CDS unreachable); a bond-level read could differ. 2. **Same-day test**; a lagged credit catch-up to earlier equity damage is not excluded (VULCAN's caveat). 3. **n = 5, CARL's selection**, ratings mostly SNIPPET-sourced from filings/press (agency pages paywalled); ICE index membership of each bond NOT checked. 4. Consumer-facing CCC issuers with public equity are few: most CCC consumer names are private (Michaels' 2L) or recently restructured (QVC, Saks), so the CCC tier's consumer share may simply be small — not measured here (LIQUID: sector decomposition NO_INSTRUMENT). 5. Lenders/subprime auto are OTTO's names; this verdict says nothing about them.

**Verdict token for H1 (CARL's names): MIXED.** Files: `METHOD_LOCK.md`, `UNIVERSE_FIXED.md`, `issuer_ledger_helper.md`, `closes.json`, `z_out.json`, `compute.py`, `zscore.py` in this folder.
