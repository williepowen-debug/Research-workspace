# Mortgage Warehouse Line Exposure — Regional Bank Analysis

**Created:** 2026-04-14 | **Trigger:** SIG-CARL-REGINALD-20260413 (non-bank servicer stress → warehouse transmission)

---

## THE CARL THESIS (in one sentence)

FHA delinquencies (11.52%, 4x conventional) are converting non-bank mortgage servicer cash-flow stress into bank warehouse line counterparty risk via the Ginnie Mae advance obligation asymmetry — and regional banks, not JPM, hold the exposure.

## MFS UK TEMPLATE

Barclays lost ~$669M through warehouse line exposure when MFS UK collapsed (Feb 2026). "Cockroaches" narrative. The warehouse line itself — not the underlying mortgage — was the loss vector. This is the template CARL is extrapolating.

---

## REGIONAL BANK WAREHOUSE ACTIVITY (our coverage universe)

| Bank | Warehouse Book | Capital Treatment | Growth Trajectory | Risk Posture |
|------|----------------|-------------------|-------------------|--------------|
| **WAL** | ~$9.2B est. (within $10.8B SSFA "Other OBS") | 20% RW via SSFA ($1.1B capital savings) | Not explicit; embedded in NDFI growth | **Largest absolute balance; opaque counterparty detail** |
| **FHN** | GROWING; $767M Q4 2025 increase in "loans to mortgage companies" alone | Standard RW disclosed | **Actively leaning in** — "NDFI growth driven by mortgage warehouse" | Management calls it "prudent" — direct doc, secondary market sale as mitigant |
| **TCBI** | Material; 59% in "enhanced credit structures" | 57% blended RW via enhanced structures — SSFA-style arb, $275M freed capital | Migrating more balances into enhanced structures; +5-10% next 2Q | **Most explicit about capital arb**; exposes same mechanism as WAL |

**Common thread:** All three banks are structuring mortgage warehouse lending for capital efficiency, implicitly assuming non-bank servicer counterparties remain solvent. That assumption is under stress.

---

## WHY THIS SHARPENS EXISTING THESIS — NOT A NEW VECTOR

For WAL, this does NOT add a 4th vector. It **refines V3 (SSFA/NDFI)**.

- V3 as originally framed: SSFA capital arbitrage is a **regulatory** risk — if Basel III Endgame or stress scenario forces SSFA reclassification, capital ratios drop.
- V3 as refined by CARL signal: SSFA capital arbitrage is ALSO a **counterparty credit** risk — the 20% RW assumes collateral (mortgage loans in warehouse) is low-loss. Under FHA servicer stress, that collateral becomes encumbered/disputed, advance obligations drain counterparty liquidity, and warehouse lender takes direct loss.

**Two parallel pathways to same P&L hit:**
1. **Regulatory:** Scrutiny forces reclassification → $1.1B capital need at WAL
2. **Credit:** Non-bank servicer counterparty default → warehouse line loss (MFS UK template)

The original V3 framing missed pathway #2.

---

## THE NON-BANK SERVICER STRESS STACK (from CARL KB)

| Servicer | Type | FHA DQ | Ginnie Exposure | Liquidity Signal |
|----------|------|--------|-----------------|------------------|
| **PennyMac (PFSI)** | Public | 7.5% (+160bps QoQ) | High | Debt/equity 3.6x, $15.6B total debt, acquiring Cenlar $740B UPB |
| **loanDepot (LDI)** | Public | — | 28% | $107.5M FY25 loss, pledging GNMA MSR income |
| **Rithm/NewRez** | Public | — | 18% Ginnie MSRs | Mgmt: "DQ will reverse in Q1" — testable Apr 28 |
| **Lakeview** | Private | 18% (Jul 2025, stale) | High | No updated data |
| **Freedom** | Private | 15.5% (Jul 2025, stale) | High | Exec: "more M&A possible on greater delinquency" |

CARL notes GAO finding: 35% of 550+ non-banks have "high levels of debt," only 30% were profitable during 2022-23 downturn. Ginnie Mae has NO stagflation stress test — our environment is the untested one.

---

## COUNTERPARTY MAPPING GAP (what we don't know)

None of WAL/FHN/TCBI discloses specific warehouse counterparty names in 10-K. Rough inference channels:
- 10-K risk factor prose may describe counterparty concentration qualitatively
- Call Report schedules (FFIEC) may disclose NDFI subsegment detail post-Q1
- MBA/NMSA reports may include league tables of warehouse lenders ↔ servicers
- Non-bank servicer 10-Ks (PFSI, LDI, RITM) sometimes name their bank warehouse providers

**Research gap:** Map which regional banks provide warehouse lines to which FHA-heavy non-bank servicers. Should be an external research prompt.

---

## SIGNAL THRESHOLDS (new)

| Trigger | Action |
|---------|--------|
| Any public non-bank servicer (PFSI, LDI, RITM, COOP) breaches 10% FHA DQ or announces covenant issue | Escalate WAL V3 + FHN/TCBI to 🔴 |
| RITM Q1 earnings (Apr 28) fails to show "DQ reversal" | CARL's testable claim invalidates servicer mgmt tone; confirms CARL thesis |
| Q1 Call Report (early May) shows WAL MI3/OBS stable while NDFI growing | Warehouse book absorbing stress, not shrinking = vulnerability accumulating |
| JPM or G-SIB flags NDFI provisioning in Q1 | Regulatory scrutiny spreading; SSFA reclassification risk ↑ |

---

## ACTION TAKEN

1. Added FHN + TCBI to warehouse-vulnerability watchlist (not yet on main matrix as they lack other vector scoring)
2. Added RITM Apr 28 to CALENDAR (testable claim)
3. Outbox reply to CARL confirms integration + raises counterparty mapping as open question for HOMER/CARL extension

## NOT TAKEN

- No position change recommended. WAL already at full thesis-size; V3 refinement deepens conviction but doesn't add a new strike.
- FHN/TCBI warehouse exposure noted but not a near-term trigger — no earnings catalyst in our current window.
