# PROMPTS.md — Research Prompts for Will

Prompts for Will to run through external LLMs (multi-model cross-verification protocol).
Prome adds prompts here; Will picks them up and runs them.

---

## Queued

### DHS Shutdown Status Verification
**Priority:** 🔴 HIGH — affects whether current claims data is clean
**Context:** ChatGPT (Mar 9) says DHS shutdown was still ongoing as of Mar 8, 2026. Gemini says fully resolved. If shutdown is ongoing, initial claims 213K is still suppressed.
**Prompt:**
```
Is the US DHS partial government shutdown that began in late January / early February 2026 still ongoing as of March 9, 2026? Specifically:
1. Has a funding bill been signed into law that fully funds DHS?
2. If resolved, what date was it resolved?
3. If still ongoing, how many DHS workers remain affected (essential working without pay vs furloughed)?
4. Are there any reports of backlogged unemployment insurance claims from DHS-related workers?
Source all claims to specific news articles or government releases with dates.
```

### Google Trends — Labor Search Terms
**Priority:** 🟡 LABOR KB staleness
**⚠️ WILL MUST DO MANUALLY** — LLMs cannot access real-time Google Trends data. Go to trends.google.com directly.
**Prompt (for your own reference):**
```
Using Google Trends data for the United States, provide the current relative search interest (past 90 days trend) for each of the following terms:

1. "unemployment benefits"
2. "file for unemployment"
3. "laid off"
4. "severance package"
5. "hiring freeze"
6. "food stamps" / "SNAP benefits"
7. "job openings near me"

For each term, state: current week's index value (0-100), 4-week average, whether the 90-day trend is rising/flat/declining, and any notable spikes in the past 30 days. Compare current levels to the same period in 2025 and 2024 if possible.

Note if any terms show breakout or unusual patterns. These are used as real-time sentiment proxies for labor market stress.
```

---

## Completed

### Indeed Job Postings (Mar 9)
4 LLMs: Gemini, DeepSeek, Perplexity, ChatGPT → KB-LAB-018 updated

### Cass Freight Index (Mar 9)
4 LLMs: Gemini, DeepSeek, Perplexity, ChatGPT → KB-LAB-043 updated

### Continuing Claims + JOLTS (Mar 9)
3 LLMs: Gemini, Perplexity, ChatGPT (DeepSeek skipped) → updating KB
