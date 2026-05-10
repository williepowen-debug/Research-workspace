# ZION — Research TODO / Backlog
**Created:** 2026-05-09 evening ET  
**Reason:** Will correctly identified that ZION has not been researched at OZK/WAL depth. Existing ZION work is mostly comparator/accounting work, not full single-bank short diligence.

---

## Priority 0 — framing correction

### 0. Stop treating thin folder as clean evidence
**Status:** ✅ corrected

ZION folder had only a few files because ZION was originally a WAL benchmark, not because it had been cleared. Current trade recommendation can still be “kill July put,” but research status should be **UNDER-RESEARCHED / MONITOR**, not “clean.”

---

## Priority 1 — must answer before any new/rolled ZION exposure

### 1. Q1 2026 Call Report: MI3 / RCON2746 / hidden CRE screen
**Question:** Is ZION hiding CRE-economic exposure inside C&I like OZK/WAL, and did Q1 leasing→C&I reclassification matter?

**Pull/check:**
- RC-C Part I Item 4 C&I
- RC-C Memo Item 3 / RCON2746
- C&I vs CRE migration QoQ/YoY
- Any leasing/equipment/warehouse sub-bucket clues
- Modified loans by class
- Nonaccrual / past-due / classified by C&I, owner-occupied, CRE term, construction

**Output:** `research/MI3_HIDDEN_CRE_SCREEN.md` + KB rows.

**Decision relevance:** If MI3 surprises high or accelerates, reopen ZION downside despite clean Q1 narrative.

---

### 2. CRE / multifamily maturity wall deep dive
**Question:** Is the 46% 12-month multifamily maturity wall benign, or a recognition delay?

**Known hooks:**
- MF CRE: ~$4.1B, 30% of CRE.
- ~46% scheduled to mature within 12 months.
- Basis Multifamily acquisition adds agency MF origination/servicing platform.
- CRE activity returning; management noted intense CRE pricing pressure.

**Pull/check:**
- Property-type detail: office, MF, hospitality, construction/land.
- Geography: UT/CA/TX/AZ/NV/CO; Western secondary-market exposure.
- Maturity ladder by quarter if available.
- Criticized/classified ratios by property type.
- Whether Basis MF creates held-for-sale / construction / stabilization balance sheet risk.

**Output:** `research/CRE_MULTIFAMILY_MATURITY.md` + KB rows.

---

### 3. Municipal / conduit risk deep dive
**Question:** Is ZION's muni book really low-risk public-sector credit, or private borrower risk through pass-through structures?

**Known hooks:**
- Total muni investments/extensions ~$5.9B Q1.
- Municipal loans ~$4.27B.
- Unfunded muni commitments ~$423M.
- Q1 nonaccrual muni loans ~$2M, tied to private commercial entities using pass-through muni structures.

**Pull/check:**
- Historical muni loan trend and nonaccrual trend.
- Private conduit borrower types: hospital, developer, 501(c)(3), project finance.
- Unfunded commitment draw risk under market stress.
- Any geographic concentration in stressed municipalities/Western development areas.

**Output:** `research/MUNI_CONDUIT_RISK.md` + KB rows.

---

### 4. Fraud/accounting follow-through
**Question:** Did ZION's aggressive Stupin/Cantor recognition fully resolve risk, or is there residual legal/recovery/accounting tail?

**Known hooks:**
- ~$60M exposure, ~$50M charge-off.
- Collateral described as irretrievably lost / subordinated/transferred.
- EY auditor; ZION led disclosure before WAL.

**Pull/check:**
- Q4/Q1 updates on recovery, litigation, insurance.
- Any additional charge-offs.
- Auditor CAMs / audit committee treatment.
- Comparison to WAL residual Cantor exposure.

**Output:** `research/FRAUD_ACCOUNTING_COMPARISON.md` + KB rows.

---

## Priority 2 — capital / funding / governance

### 5. AOCI + Basel III / RWA offset
**Question:** Is ZION an especially exposed AOCI capital-rule name, or is Basel III relief enough to neutralize it?

**Known hooks:**
- AOCI loss ~-$1.935B.
- ~$1.5B pre-tax / ~$1.2B after-tax unrealized losses on transferred AFS→HTM securities.
- Treasurer cited potential +93bps CET1 from Basel III endgame/RWA relief.

**Output:** `research/AOCI_CAPITAL_RULE.md`.

---

### 6. Funding / liquidity durability
**Question:** Is Q1 funding strength durable or seasonal?

**Known hooks:**
- FHLB borrowings reduced sharply / zero in liquidity table.
- Deposits +2% QoQ; uninsured liquidity coverage 134%.
- Brokered deposits ~4.9%.

**Output:** section in `research/ZION_DEEP_DIVE_FRAMEWORK.md` or standalone if material.

---

### 7. Insider / governance / auditor scan
**Question:** Are there Form 4, executive departure, auditor, or board-risk signals comparable to OZK/WAL work?

**Known hook:** prior domain scan said ZION insider behavior looked green; verify current.

**Output:** `research/INSIDER_GOVERNANCE_SCAN.md`.

---

## Priority 3 — synthesis / trade framework

### 8. Build ZION scenarios
After Priority 1 files exist, write:
- `SCENARIOS.md`
- `WEAKNESSES.md`
- updated `THESIS.md` v2 if warranted

Scenarios should explicitly separate:
1. **Bull/stabilization:** ZION genuinely disciplined; July put dead.
2. **Latent bear:** MF/muni/MI3 risk but timing H2 2026+.
3. **Active bear:** Call Report exposes hidden CRE or credit metrics reverse.
4. **Tail:** AOCI capital rule + CRE/muni stress converge.

---

## Immediate next action

When ready to continue: start with **Priority 1.1 Call Report / MI3 screen**. That is the fastest way to test whether the “bad CRE moved into C&I” memory applies to ZION or only to OZK/WAL.
