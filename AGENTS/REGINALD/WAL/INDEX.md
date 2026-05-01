# WAL — Agent Index
**Start here on cold boot.**

**Last session (May 1 — Wave 1 chunks 1-6):** THESIS v2.0 release ("compounder with concentrated CRE tail risk"); CHANGELOG created; STATUS refreshed; FRAUD/STATUS + FRAUD/SYNTHESIS_V2 post-print rewrite; **KB.tsv 80→105 rows** (Q1 print evidence appended); KB_INDEX +1 group (LEADING_CREDIT) + post-Apr 21 quick-reference; SCENARIOS.md re-weighted (Bear 45%→30%, Base 30%→38%, Bull 20%→25%, EV $57→$72).

---

## Key Numbers (Q1 2026, post-Apr 21 print)

| Metric | Value | Signal |
|--------|-------|--------|
| **Office Classified** (V1) | $407M = 38% of classified mix, **18.5% stress rate, 9.5x book disproportion** | 🔴 |
| **Office Maturity Wall 2026** (V1) | $946M matures during 2026 (43% of $2.2B Office book) | 🔴 |
| **30-89d PD building** (V1) | +$49M QoQ to $157M (+45% QoQ) | 🟠 |
| **Special Mention building** (V1) | +$78M QoQ to $403M (+24% QoQ) | 🟠 |
| **CRE-NOO Q1 charge** (V1) | $27.7M (largest in 5 quarters) | 🟠 |
| **Q1 Fraud Charge-off** (V2 RESOLVED) | **$152.5M** (LAM $126.4M + Cantor $26.1M) | 🔴 → resolved |
| **Cantor residual** (V2) | ~$70M on book + $13M senior liens + UHNW guarantees | 🟡 |
| **NDFI cohort position** (V3) | Slide 24: WAL 7% Ex-Mtg Credit (peer median 6%) — at center | 🟢 (disconfirmed at agg) |
| **Mortgage Warehouse + MSR** (V3) | $7.155B (12% of loans, 30x peer median) | 🟠 |
| **CLN reference pool** | $8.5B → $7.9B Mar-26 (-$600M YoY) — shrinking | 🟢 |
| **CET1** | 11.0% steady; Tier 1 12.0%; Total Cap 14.4% | 🟢 |
| **TBV** | $61.14 (+13% YoY) | 🟢 |
| **Deposits** | $82.7B (+$5.6B QoQ = +7.2%; +$13.4B YoY = +19.3%) — **cohort lead** | 🟢 |
| **NCO ex-fraud Q1** | 39bps annualized (vs 25-35bps mgmt guide top) | 🟠 |
| **Insider Buying** | Zero | 🔴 |

## Positions

| Strike | Expiry | Contracts | EV @ $81.22 | Recommendation |
|--------|--------|-----------|-------------|----------------|
| $85P | Jun 18 | 1 | $13.93 | HOLD — slightly ITM; 7wk to Q2 catalyst |
| $77.5P | Sep 18 | 1 | $8.31 | HOLD — best risk-adjusted core |
| $70P | Sep 18 | 1 | $4.20 | HOLD — cheap tail exposure |
| $65P | Jun 18 | 1 | ~$0.75 | **CONSIDER CLOSE OR ROLL TO SEP** — needs rapid move v2.0 thesis no longer projects |

**Q1 2026 print: ✅ Apr 21** | **Investor Day: May 12** | **Q2 print: ~late Jul** | **Bear EV target: $58-68 (30%)** | **Base EV target: $70-78 (38%)** | **Bull EV target: $85-95 (25%)** | **Tail: $35-45 (7%)**

## Data Update Rules

| What Changed | Where to Update | Don't Touch |
|---|---|---|
| **A number/data point** | KB.tsv only (append; mark old via DerivedFrom) | THESIS.md |
| **Narrative/framing shift** | THESIS.md + CHANGELOG.md entry; bump version | KB.tsv |
| **New evidence arrives** | Add KB.tsv row → check off STATUS.md research agenda | |
| **Probability re-weight** | SCENARIOS.md only | THESIS.md (unless framework breaks) |
| **Sub-thesis (V2 fraud) state changes** | FRAUD/STATUS.md + SYNTHESIS_V2.md | KB.tsv (use new rows) |
| **Session ending** | Update "Last session" line above + STATUS.md "What's Changed" | |

## Boot Sequence (post-v2.0)

| Order | File | Time | What You Get |
|-------|------|------|-------------|
| 1 | `STATUS.md` | 1 min | Dashboard, current price, V1/V2/V3 compact, mgmt outlook tensions, research agenda |
| 2 | `THESIS.md` v2.0 | 4 min | "Compounder with concentrated CRE tail risk" framework; PT $55-70; REG-24/REG-25 |
| 3 | `CHANGELOG.md` | 2 min | What changed v1.0 → v2.0; why; old vs new view |
| 4 | `SCENARIOS.md` v2.0 | 2 min | Re-weighted probabilities (Bear 30/Base 38/Bull 25/Tail 7); position EV at current price |
| 5 | `workbook/KB.tsv` | 3 min | **105-row** canonical evidence database |
| — | `workbook/KB_INDEX.md` | 2 min | **16 groups** → vectors → thesis layers → post-Apr 21 quick-reference |

## File Map

### Core (read at boot)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — start here |
| `STATUS.md` | Live dashboard (refreshed May 1: V2 RESOLVED + V1 sharpened + V3 disconfirmed at agg) |
| `THESIS.md` v2.0 | "Compounder with concentrated CRE tail risk" — released May 1 |
| `CHANGELOG.md` | Thesis evolution audit trail (created May 1; v1.0 baseline pinned + v2.0 transition documented) |
| `SCENARIOS.md` v2.0 | Re-weighted probabilities + position EV (refreshed May 1) |
| `workbook/KB.tsv` | Canonical evidence store (**105 rows**, 13 columns; Q1 rows 081-105 added May 1) |
| `workbook/KB_INDEX.md` | **KB group navigator — 16 groups** mapped to vectors, thesis layers, staleness, predictions |

### Sub-thesis (V2 Fraud)
| File | Description |
|------|-------------|
| `FRAUD/STATUS.md` | V2 RESOLVED IN PUBLIC 8-K — vector-by-vector status (LAM/Cantor resolved; First Brands/Tricolor silent) |
| `FRAUD/SYNTHESIS_V2.md` | Post-print synthesis: hypothesis vs outcome; auditor case demoted; Leucadia inventory open thread |
| `FRAUD/AUDITOR_NEXUS.md` | RSM PCAOB findings, "Issuer B" hypothesis (pre-print research; demoted post-print) |
| `FRAUD/AUDIT_COMMITTEE.md` | Audit committee composition / governance |
| `FRAUD/CLASS_ACTION_FINDINGS.md` | Securities class action findings |
| `FRAUD/STUPIN_CRE.md` | Cantor Group V deep dive (pre-print) |
| `FRAUD/FIRST_BRANDS.md` | First Brands deep dive (silent in Q1 print — latent vector) |
| `FRAUD/TRICOLOR.md` | Tricolor deep dive (silent in Q1 print — latent vector) |
| `FRAUD/INVESTIGATION_ROADMAP.md` | Pre-print plan (largely retrospective) |
| `FRAUD/ZION_AUDIT_COMPARISON.md` | EY (ZION) vs RSM (WAL) comparative |
| `FRAUD/WAL-JEF-PointBonita-Analysis-20260326.docx` | Mar 26 Point Bonita analysis (pre-print) |

### Deep Dives (read on-demand)
| File | When to Read |
|------|-------------|
| `Q1_2026_ANALYSIS.md` | Round 1 Q1 print analysis (Apr 22) — TL;DR, two fraud credits detail, GAAP-vs-adj gap, ex-fraud credit quality, deposit strength, capital, gaps for supplement |
| `EARNINGS_PREP.md` | **PRE-PRINT (Apr 21) — RETROSPECTIVE** — tripwires, decision matrix, mgmt defense, 11 KB gaps. Useful for prepping future earnings. |
| `WEAKNESSES.md` | Stress-testing — what breaks the thesis |
| `EXTERNAL_PROMPTS.md` | Research prompts for Will to run externally |
| `TECHNICALS.md` / `TECHNICALS_20260401.md` | Chart levels and technical analysis |
| `LEADERSHIP.md` | Leadership / insider deep analysis |
| `AUDIT_MAR25.md` | Mar 25 thesis audit (pre-print) |
| `FORGE_STATUS.md` | Original FORGE trade status + SSFA deep dive |
| `PRIOR_RESEARCH_EXTRACTS.md` | Older LLM research (Feb 2026) — verified selectively |

### Research (vector-organized)
| Folder | Topic |
|--------|-------|
| `research/HIDDEN_CRE/` | Vector 1: MI3 reclassification, true CRE exposure |
| `research/JEFFERIES/` | Vector 2: Double-pledging, intermediary chain |
| `research/SSFA/` | Vector 3: Capital arbitrage, $17.2B exposures |
| `research/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md` | WAL vs ZION fraud provision analysis |

### Sources & Archive
| Folder | Contents |
|--------|----------|
| `sources/` | Raw inputs (FDIC, FFIEC, insider scans, Jefferies signal, q1_2026/ deck+press+transcript) |
| `sources/q1_2026/` | Q1 print materials: 8-K, press release, deck PDF, transcript markdown, 3 synthesis docs (Round 2 deep mine) |
| `MARKET/` | Market technical / structural analysis |

---

## Open Threads (post-Wave 1)

1. **REG-20 resolution** — Will's call: mark CONFIRMED on miss + $152.5M fraud + tape -2%, or hold for higher bar (capital raise / regulatory action)
2. **Other LAM/Leucadia-era credits** (post-print PRIMARY) — 10-Q Table 16 May 4-10 + Investor Day May 12 = inventory test
3. **Q1 Call Reports May 1-10** — MI3 / RCON2746 ratio test for V1 acceleration; CFG NDFI reconcile to Slide 24 prelim $19.6B
4. **VLY 10-Q drill (~May 10)** — verify "provisions mask deterioration" claim
5. **Synthesis-files gitignore decision** — Will's call (negation rule / move path / git add -f) — 2 WAL Round 2 synthesis files still blocked from commit
6. **Cantor residual quarterly tracking** — any incremental specific reserve build above ~$70M residual = recovery posture deteriorated
7. **Q2 NCO trajectory** — REG-25 (>40bps in Q2 OR Q3, 55%) is the bear bet against mgmt's 25-35bps guide

---

*Master agent: REGINALD | Domain: Western Alliance Bancorporation (WAL) | Sub-thesis sub-folder: `FRAUD/` (V2 vector deep dive) | Peer agents: OZK at `../../OZK/` (separate compounder thesis)*
