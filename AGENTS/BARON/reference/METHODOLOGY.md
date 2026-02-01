# Research Methodology

## Evidence Standards

| Level | Definition | Use Cases |
|-------|------------|-----------|
| **CONFIRMED** | Primary source (SEC, OGE 278, official announcement) | Financial holdings, contracts, appointments |
| **HIGH** | Strong circumstantial, multiple secondary sources | Relationships, meeting attendance |
| **SPECULATIVE** | Single source or inference | Must be flagged; useful for generating hypotheses |

## High-Value Sources

| Source | What It Provides | Access |
|--------|------------------|--------|
| **OGE 278 disclosures** | Holdings, income, positions | oge.gov, FOIA |
| **SEC filings** | Holdings, SPAC structures, S-1s | sec.gov EDGAR |
| **Warren/oversight letters** | Pre-digested conflict research | warren.senate.gov |
| **Trade publications** | Details officials omit | Defense News, Inside Defense |
| **USASpending.gov** | Contract awards | usaspending.gov |
| **OpenSecrets** | Donations, lobbying | opensecrets.org |

## Search Patterns

```
"[Name]" OGE 278                    # Ethics disclosures
"[Company]" SBIR OR STTR contract   # Government work
site:treasury.gov "[Name]"          # Official bios
"[Name]" site:sec.gov               # SEC filings
"[Company]" site:usaspending.gov    # Federal contracts
```

## Pattern Analysis Principles

1. **Negative controls matter**: When research clears someone (e.g., Rathje), document it - validates hypothesis by contrast

2. **Patterns have variants**: A pattern may work in multiple directions (e.g., 84-Day Loop has Forward and Reverse). Update the pattern description, don't create separate patterns

3. **Test predictions**: When a pattern predicts something (e.g., Hadrian OSC loan), track whether it occurs. Misses are as informative as hits

4. **Follow the money and family**: Financial incentives explain behavior; family relationships reveal hidden connections

5. **Anomalies reveal patterns**: Things that don't make surface sense often reveal the biggest patterns

## Documentation Protocol

**During research:**
- Update TSV files as discoveries occur (don't batch)
- Note sources immediately
- Mark confidence levels

**At dead ends:**
- Document in EXHAUSTED.md immediately
- Include what was tried and why it failed
- Note unlock conditions

**For new patterns:**
- Require 2+ examples before calling it VALIDATED
- Document mechanism clearly
- Include counter-examples or limitations

## External Research Workflow

**When to generate prompts:**
1. New policy announcement with network implications
2. New thread requiring deep dive
3. Breaking news on existing nodes
4. Gap identified worth comprehensive research

**Prompt location:** `research/prompts/`
**Results location:** `research/results/`

## Operational Constraints

- **LOW-PROFILE**: No FOIA, no paper trails, passive monitoring only
- **OSINT ONLY**: Public sources; mark threads EXHAUSTED if FOIA needed
- **AUTO-APPROVED**: WebSearch, WebFetch, file operations, git
- **AUTONOMOUS**: Run research threads independently; check in for major direction changes

---

*Last updated: 2026-01-12*
