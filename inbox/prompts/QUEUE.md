# Research Prompt Queue

Prompts for Will to run in external LLMs. PROME adds prompts here when research gaps are identified.

---

## How to Use

1. Pick a prompt from **Ready to Run**
2. Run in your preferred LLM (Gemini, GPT, Perplexity, etc.)
3. Save output to `inbox/pending/YYYY-MM-DD_<topic>.md`
4. Tell PROME to process inbox
5. PROME moves the prompt to **Completed**

---

## Ready to Run

### 1. Warehouse Lender Exposure Mapping
**Priority:** HIGH | **Target Agent:** REGINALD  
**Added:** 2026-02-07 | **Source:** Subprime auto research gap

```
Map the warehouse lending relationships for subprime auto originators. Which banks (especially regionals) provide warehouse lines to: Flagship Credit Acceptance, Exeter Finance, Consumer Portfolio Services, American Credit Acceptance, Westlake Financial? Include facility sizes if available.
```

---

### 2. Florida Condo De-Conversion Pipeline  
**Priority:** MEDIUM | **Target Agent:** CORAL/REGINALD  
**Added:** 2026-02-07 | **Source:** FL institutional capital research

```
Research Florida condo de-conversion activity 2024-2025. Which institutional buyers have successfully terminated condo associations? How has the Biscayne 21 ruling (100% consent requirement) affected deal flow? Are there workarounds via receivership?
```

---

### 3. Canadian Snowbird Real Estate Holdings
**Priority:** MEDIUM | **Target Agent:** MARCO/CORAL  
**Added:** 2026-02-07 | **Source:** Canadian tourism research

```
Estimate Canadian ownership of Florida residential real estate, particularly condos in Southeast FL. Are Canadians net sellers in 2025? What's the impact of CAD/USD exchange on their willingness to hold or sell?
```

---

### 4. Florida Seasonal Rental Revenue
**Priority:** MEDIUM | **Target Agent:** CORAL  
**Added:** 2026-02-07 | **Source:** Canadian tourism research

```
Research Florida condo seasonal rental market performance 2025. What's the YoY change in winter rental rates and occupancy in Miami-Dade, Broward, Palm Beach? Are Airbnb/VRBO listings increasing while bookings decline?
```

---

### 5. Florida Tourism Tax Revenue
**Priority:** HIGH | **Target Agent:** MARCO/CORAL  
**Added:** 2026-02-07 | **Source:** Canadian tourism research

```
Find Florida tourism tax revenue data for 2025 (Tourist Development Tax, bed tax). Is there YoY decline in counties with heavy Canadian visitor concentration (Broward, Palm Beach, Lee, Collier)?
```

---

### 6. Private REIT Redemption Queues
**Priority:** LOW | **Target Agent:** REGINALD  
**Added:** 2026-02-07 | **Source:** FL institutional capital research

```
What is the current redemption queue status for major private REITs with Florida exposure: BREIT, SREIT, other non-traded REITs? What percentage of their portfolios are FL residential/multifamily? What would trigger another redemption gate?
```

---

## Completed

*(Move prompts here after research is integrated)*

---

## Prompt Format

When PROME adds new prompts:

```markdown
### [N]. [Title]
**Priority:** HIGH/MEDIUM/LOW | **Target Agent:** [AGENT]  
**Added:** YYYY-MM-DD | **Source:** [Why this research is needed]

\```
[The actual prompt to run]
\```
```

---

*Last updated: 2026-02-07*
