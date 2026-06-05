---
name: CARL KB Architecture — Push Down to Sub-Agents
description: Will wants CARL KB lean (thesis-level only); push domain-specific data down to sub-agent KBs
type: feedback
originSessionId: 70fec9bd-7725-4d8e-8fdb-7ab1bda624c9
---
CARL's KB should be the executive summary — thesis-level signals only. Sub-agents hold the supporting evidence.

**Why:** KB was growing (196 entries) with a mix of thesis-level cross-domain findings AND domain-specific detail (individual ATTOM reports, servicer metrics, builder earnings). Will wants CARL to offload lower-priority rows so CARL KB stays lean and every entry matters.

**How to apply:**
- CARL KB keeps: cross-domain transmission findings, threshold breaches, macro signals affecting multiple vectors, counter-signals, trade-relevant data
- Sub-agent KBs absorb: domain-specific data points, source documentation, historical baselines, granular geographic/cohort breakdowns
- When adding new KB entries, ask: "Is this thesis-level or domain detail?" If domain detail → goes to sub-agent KB, not CARL
- Sub-agents should have their own KB.tsv (currently only HOMER has one — others use domain-specific TSVs)
- CARL reads sub-agent KBs during synthesis but doesn't duplicate them
