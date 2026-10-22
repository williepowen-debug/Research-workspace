---
signal_id: "SIG-W-20261022-017"
date: "2026-10-22"
timestamp: "2026-10-22T17:03:13Z"
dispatched: "2026-10-22T17:03:13Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261022-001 deliverable, AGENTS/DEWEY/output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md (11852be57)"
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["REGINALD"]
info: ["GIBBS", "VULCAN", "OZK", "WAL", "FLG", "LIQUID", "RED", "TERRY", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "cited deep research; vendor map mostly UNKNOWN"
resources: 1
safety_net: "clear"
word_count: 513
entities: ["Fiserv", "Jack-Henry", "FIS", "Kansas-City-Fed", "MOVEit", "Evertec", "ConnectWise", "Storm-0940", "Huntress", "Section-1033", "Axios"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b; DEWEY delivered create-only copies to all 10 recipients (verified, 0 backstops). WALTER spot-checked the KC Fed shares at source."
---
# DEWEY research (REQ-001): US bank technology is concentrated by count (Fiserv 42%, Jack Henry 21%, FIS 9% of banks), but no multi-bank core-vendor compromise is confirmed, no AI-agent loss is reported, and no IT or cyber event has a documented deposit run. Which vendor each regional bank uses is mostly not public

**Report:** `AGENTS/DEWEY/output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md` (commit 11852be57). **Commission:** REQ-DEWEY-20261022-001, Will-directed 11:53 ET, plus WALTER addendum 1. Kill condition did not fire. DEWEY delivered create-only copies to every recipient below; WALTER verified the set (no backfill needed).

| Question | DEWEY's finding | Basis |
|---|---|---|
| How concentrated? | Core vendors by count of banks: Fiserv 42%, Jack Henry 21%, FIS 9% (2022 data, ABA survey via the Kansas City Fed, 2024-03-27; **WALTER re-read the KC Fed page and the figures match**). Top 4 digital-banking vendors hold 71% of mobile installations. **No public data by assets or by bank tier.** | Survey, not a census |
| Which vendor does each of 22 banks use? | Only 4 named in a 2024–26 primary document (ZION TCS, PNFP FIS, AUB FIS, BPOP Evertec); 8 UNKNOWN; 4 rest on 2011–21 documents | Filings and vendor releases |
| Have vendor hits spread across banks? | Yes, as data breaches: MOVEit 2023 reached FLG, VLY, Cadence (now HBAN), COLB and BPOP through third parties. None cut customer access | Bank notices, 8-Ks |
| Did any IT/cyber event cause a run? | **No documented deposit run** (IMF 2024). Patelco −2.7% for one quarter, recovered. Lasting stock damage fell on vendors, not banks | Academic, filings |
| Current events | Jack Henry incident (disclosed 8/31): fewer than 10 clients, non-production systems, no outage. Microsoft Storm-0940: more than 2,250 tenants **targeted**, Huntress confirmed 173 compromised; no bank named. ConnectWise is an IT-tool vendor, not core banking. Axios AI-agent story unretracted, key claims anonymous | Microsoft primary, Huntress, company statements |
| AI agents and data access | Restrictions on record are at the largest banks and brokers, citing security and liability; no losses; no regional bank has commented. The Section 1033 data-access rule is enjoined; its rewrite has been at OIRA since about 8/06 | News, regulatory record |
| SEC cyber filings | 4 banks filed 9 Item 1.05 8-Ks (DEWEY re-checked all 9); EDGAR covers only about a tenth of banks | SEC |

**Do not relay as:** "regional banks are the AI-agent target" or "vendor concentration will cause a run." **The base rate is silent** on a multi-week outage at a large bank heavy in uninsured deposits: it neither supports nor rules one out.

**Not checked (outside the question, per the addendum's "do not widen"):** CrowdStrike AI-agent campaigns, PHP2Shell, LiteLLM/Railway/Zeabur, GitLab/Node.js.

**REGINALD ACTION:** does this change any bank's operational-risk read or your ranking? The vendor map is mostly UNKNOWN, so a bank-specific claim needs that bank's own disclosure. INFO: GIBBS (large-bank AI-agent restrictions), VULCAN (agentic-AI adoption friction), OZK, WAL, FLG (your own vendor is UNKNOWN or stale in the map), LIQUID; RED, TERRY and PROME by BOARD (DEWEY copies delivered). No trade is implied.
