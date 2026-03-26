# Aspida Deep Dive — Research Plan
**Created:** 2026-03-26
**Priority:** HIGH — last major research gap in ARES thesis
**Template:** Athene statutory analysis (KB-BRK-053) — same Eisman/Gober methodology

---

## WHAT WE KNOW

- Aspida = ARES-owned insurance subsidiary
- Management calls it "capital-light" vs Apollo/Athene's balance-sheet-heavy model — **UNVERIFIED**
- Insurance AUM: **$139.1B** (22% of total ARES AUM, up from $75.3B YoY = +85%)
- ARES balance sheet insurance investment: **$617.5M** (+59% YoY) — growing faster than any other category
- ARES is simultaneously REDUCING its own credit investments (-28%) while loading up on insurance
- Same PE-insurance structural template as Athene (Apollo) and Global Atlantic (KKR)
- NAIC PBR guardrails (APF 2025-16) constrain the PE-insurance spread model
- No detailed public disclosure in ARES 10-K — Aspida is essentially a black box

## WHAT WE NEED TO FIND

### Tier 1: Statutory Filings (PRIMARY SOURCE — highest edge)

**Where to look:**
1. **NAIC database / state insurance filings** — Aspida is domiciled in a US state (need to confirm which one). Statutory filings are PUBLIC.
2. **Aspida's own website** — check for IR/financial disclosures (like Athene posts on its IR site)
3. **ARES 10-K** — search for "Aspida" mentions, any footnotes about insurance subsidiary
4. **State insurance department** — annual statements filed with domiciliary state

**Key metrics to extract (mirroring Athene analysis):**
| Metric | Why It Matters | Athene Comparison |
|--------|---------------|-------------------|
| **Surplus** | Capital cushion | Athene $4.1B |
| **Reinsurance receivables** | Leverage indicator | Athene $225.7B (55:1 ratio!) |
| **Reinsurance ratio** (receivables/surplus) | Systemic risk | Athene 55:1 |
| **Deposit-type contracts** | Liability growth | Athene $64.3B (+76.6% YoY) |
| **Unassigned surplus** | Dividend capacity | Athene Iowa: NEGATIVE ($1.647B) |
| **Bermuda/offshore cessions** | Captive reinsurance | Athene ALRe surplus -22% |
| **AVR (Asset Valuation Reserve)** | Hidden loss absorption | Athene +42% |
| **Affiliated paper %** | Self-dealing risk | Is Aspida buying ARES-originated assets? |
| **Investment portfolio composition** | CLO/PC exposure | Does Aspida hold ARCC/IHAM paper? |

### Tier 2: Corporate Structure

- **Aspida Life Insurance Company** — confirm legal entity name
- **Aspida Life Re Ltd** — likely Bermuda reinsurer (same pattern as ALRe/Athene)
- **Domiciliary state** — determines which state regulator + filing location
- **Captive reinsurance structure** — does Aspida use offshore captives to inflate onshore surplus?
- **Relationship with Athene** — are there any co-investments, shared portfolios, or reinsurance treaties between Aspida and other PE-insurers?

### Tier 3: Business Model Questions

- What insurance products does Aspida write? (annuities, life, pension risk transfer?)
- What's the investment strategy for policyholder assets? (if they're buying ARES-originated credit/CLOs, that's circular)
- How does "capital-light" actually work? (management fee on insurance AUM vs taking balance sheet risk?)
- What's Aspida's growth trajectory? ($139B AUM growing 85% YoY — is this organic or acquisition?)
- GCP International acquisition — is any of the $45B GCP AUM insurance-related?

---

## RESEARCH APPROACH

### Phase 1: Find the Filings (1-2 hours)

**Step 1:** Search for Aspida's legal entities and domiciliary state
- Web search: "Aspida Life Insurance Company" NAIC, state filing
- Check NAIC UCAA database
- Check common PE-insurer domiciles: Iowa, Arizona, Delaware, South Carolina

**Step 2:** Pull statutory annual statement
- State insurance department website (usually free PDF download)
- NAIC database (may require subscription)
- Aspida's own website / ARES IR page
- If not freely available, check AM Best or ALIRT reports

**Step 3:** Pull Bermuda filing (if Aspida has offshore reinsurer)
- BMA (Bermuda Monetary Authority) filings
- Search for "Aspida" on BMA register

### Phase 2: Extract & Analyze (2-3 hours)

Using Athene template (KB-BRK-053 / trade/APO/ATHENE_STATUTORY_FY2025.md):
- Extract all Tier 1 metrics
- Compare to Athene, Global Atlantic, Evermore benchmarks
- Identify any affiliated paper (ARES-originated assets on Aspida's books)
- Map captive reinsurance flows

### Phase 3: Assess & KB (1 hour)

- Score Aspida vs Athene on each metric
- Determine if "capital-light" claim holds
- Identify specific risk vectors
- Update THESIS.md Vector 3
- Add KB rows

---

## EXECUTION

**Option A: Self-directed research session**
- Spawn subagent to do Phase 1 web research (find filings, extract legal structure)
- Prome does Phase 2-3 analysis once filings are located

**Option B: Will-assisted**
- Will navigates to NAIC database or state insurance dept website
- Paste/screenshot statutory filing data (same workflow as today's 10-K/A)
- Prome extracts and analyzes

**Option C: Hybrid**
- Subagent does background web research
- Will fills gaps where paywalls/logins block access

**Recommendation: Option C.** Start with a subagent doing web research to find the entity structure and any freely available filings. Then Will fills gaps. The Athene statutory filing was sitting on their own IR page — Aspida may be the same.

---

## SUCCESS CRITERIA

| Finding | Impact on Thesis |
|---------|-----------------|
| Aspida reinsurance ratio >20:1 | 🔴 Confirms systemic risk, validates Vector 3 |
| Aspida holds ARES-originated assets | 🔴 Circular/self-dealing risk (like Athene holding Apollo paper) |
| Aspida uses Bermuda captive | 🟡 Standard for PE-insurers but confirms structural template |
| "Capital-light" is actually capital-light | 🟢 Weakens Vector 3 (reduces thesis by one vector) |
| Aspida surplus is healthy | 🟢 Weakens Vector 3 |
| No statutory filings accessible | 🟡 Inconclusive — flag as ongoing research gap |

---

*Cross-references: KB-BRK-049, KB-BRK-053, KB-BRK-056, KB-BRK-057, KB-BRK-091*
*Athene template: trade/APO/ATHENE_STATUTORY_FY2025.md*
