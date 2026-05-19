# LIQUID Research Prompts Index

**Created:** 2026-01-25
**Updated:** 2026-01-25
**Purpose:** Standalone prompts for deep research LLM sessions

---

## Quick Reference

| # | Prompt File | Vector | Scope | Priority | Status |
|---|-------------|--------|-------|----------|--------|
| 01 | 01_RRP_DEPLETION_MECHANICS.md | VX-LIQUID-1.02 | Complex | HIGH | **COMPLETE** |
| 02 | 02_SOFR_STRESS_EPISODES.md | VX-LIQUID-1.01 | Medium | HIGH | **COMPLETE** |
| 03 | 03_TREASURY_AUCTION_HEALTH.md | VX-LIQUID-2.01/2.02 | Medium | MEDIUM | **COMPLETE** |
| 04 | 04_FTD_SETTLEMENT_PATTERNS.md | VX-LIQUID-1.03 | Medium | MEDIUM | **COMPLETE** |
| 05 | 05_MMF_DEPLOYMENT_POST_RRP.md | VX-LIQUID-1.02 | Complex | HIGH | **COMPLETE** |

---

## Research Results Summary

All research prompts executed and processed on 2026-01-25. Results stored in `RESEARCH_RESULTS/` folder.

| # | Result File | Key Findings |
|---|-------------|--------------|
| 01 | The Vanishing Buffer...md | RRP depleted. Fed started RMP $40B/mo. Central Bank Balance Sheet Trilemma. |
| 02 | SOFR Stress Episodes...md | SRF is porous ceiling (Dec 31 breach +12bps). GSIB constraints binding. |
| 03 | Treasury Auction Health...md | Thresholds validated. Tail is most immediate signal. 7Y most fragile. |
| 04 | Treasury FTD Patterns...md | $42.4B = Yellow. Scarcity + clearing transition. Monitor aged fails. |
| 05 | MMF Post-RRP...md | $2.5T rotated to T-bills + repo. MMF→HF basis trade transmission ($1.85T). |

---

## Domains NOT Covered (Handled by Peer Agents)

| Topic | Agent | Reason |
|-------|-------|--------|
| Japan repatriation flows | SAM | SAM's primary domain |
| GPIF/Lifer holdings | SAM | SAM tracks Japan institutional behavior |
| FHLB advance rates | REGINALD | REGINALD tracks bank funding stress |
| Regional bank deposits | REGINALD | REGINALD's primary domain |
| CLO/BDC transmission | REGINALD | REGINALD tracks credit transmission |

LIQUID receives signals FROM these agents rather than duplicating research.

---

## New Vectors Added From Research

| Vector | Name | Source Research |
|--------|------|-----------------|
| VX-LIQUID-1.04 | SRF Usage | Research 01, 02 |
| VX-LIQUID-1.05 | Dealer Net Position | Research 02 |
| VX-LIQUID-1.06 | Sponsored Repo Volume | Research 05 |
| VX-LIQUID-2.03 | Auction Tail | Research 03 |
| VX-LIQUID-5.01 | MMF WAM | Research 05 |
| VX-LIQUID-5.02 | Basis Trade Exposure | Research 05 |

---

## Future Research Queue

See `RESEARCH_STATUS.md` for future research topics. Current priorities:
- Central clearing transition impact (June 2027 mandate)
- GSIB surcharge mechanics (year-end cliff effect)

---

*LIQUID Research Index v2.0 | All initial research COMPLETE*
