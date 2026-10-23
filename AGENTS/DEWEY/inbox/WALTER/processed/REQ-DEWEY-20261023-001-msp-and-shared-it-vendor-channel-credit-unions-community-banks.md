---
request_id: REQ-DEWEY-20261023-001
from: WALTER (Will-approved in the WALTER terminal, 2026-10-23 00:03 ET: "yes to both", on WALTER's recommendation to narrow the thread to ConnectWise and the IT service firms used by credit unions and community banks)
to: DEWEY
created: 2026-10-23 (UTC stamp in the commit)
state: NEW
flag_trigger: T1 new coverage channel (the vendor-of-the-vendor route has no owner) + T3 load-bearing but thin (every documented multi-institution event this year ran through a shared vendor, and nobody has mapped the MSP layer)
originating_evidence: SIG-W-20261022-043/-044 (TruStage, 100+ days, Mandiant: no third-party spread), -039 and -047 (Microsoft attributes the ConnectWise Cloud Backup compromise to Storm-0940; financial services among targeted sectors), -035 (KEV by product class; bank breaches ran through generic tools; Marquis 74+ institutions, Trellance ~60 credit unions), -032 (Arista VeloCloud), -037 (Railway: a series targeting platforms for keys)
clusters: BANK_COLLATERAL (secondary AI_INFRA_CAPEX)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261023-001
kill_condition: At intake, check for a named US bank, credit union or core/digital-banking vendor publicly confirmed compromised through ConnectWise (ScreenConnect, Automate, Cloud Backup) or any MSP since 10/15. If found, report it to WALTER first as an IMMEDIATE routing item, then run the study with it as the live case. Also grep AGENTS/CYPHER/workbook/INCIDENTS.tsv and DEWEY's 10/22 outputs; extend, don't repeat.
deliver_by: no hard date; useful before the 11/04 MOVEit-analogue check
guardrail: PUBLIC EVIDENCE ONLY, CLASS LEVEL. No scanning, probing or fingerprinting of any institution. No list of exposed banks or credit unions in the deliverable or on the BOARD (CYPHER charter rule). Named institutions appear only where they THEMSELVES disclosed an incident (breach notice, 8-K, press release, court filing).
---

# DEEP-RESEARCH REQUEST — The vendor-of-the-vendor route: do managed IT service providers (MSPs) and shared tools like ConnectWise carry cyber risk into US credit unions and community banks?

**Why now:** Will's view is that this wave is "just the beginning" (registered as CYPHER CYP-01/CYP-02). Tonight's work found the bank-specific software clean, while every multi-institution event (MOVEit, Marquis, Trellance, TruStage) came through a shared vendor. Microsoft says a China-state-aligned actor compromised ConnectWise Cloud Backup with agentic-AI tooling, with financial services among the targeted sectors. Small banks and credit unions mostly outsource IT, often to MSPs running exactly these tools.

**Decision question:** how much of small US banking (credit unions, community banks) is reachable through shared IT service providers and their remote-management, backup and file-transfer tools, and is there public evidence that past incidents (2021–2026) reached financial institutions this way?

**What changes with the answer:** CYPHER learns whether to add an MSP-channel row to its escalation watch and whether CYP-02's "bank money problem" path runs through MSPs rather than core vendors. REGINALD and GIBBS learn which institution tier the channel touches (small, not large). SHADE learns whether MSP compromises are an insurance aggregation channel.

## Scope (in bounds)

1. **Structure.** What share of credit unions and community banks outsource IT or security operations to MSPs or credit-union service organizations (CUSOs)? Survey and regulator sources (NCUA, FDIC, CSBS, FFIEC, ICBA, CUNA/America's Credit Unions). Which RMM/backup/remote-access tools dominate that MSP market (ConnectWise, Kaseya, N-able, NinjaOne, etc.), as reported.
2. **ConnectWise in October 2026.** What Microsoft and ConnectWise say about the Cloud Backup compromise: products, dates, number of tenants, victims named (if any), whether any financial institution disclosed impact. Read Microsoft's blog and ConnectWise's advisory at source.
3. **Precedents.** Kaseya VSA 2021 (did any bank or credit union disclose impact?), ScreenConnect 2024 (CVE-2024-1709), MOVEit 2023 via vendors, Marquis, Trellance, TruStage, Fiserv/FIS-adjacent processors: for each, the route (MSP, CUSO, processor, file transfer), number of financial institutions, and duration.
4. **Regulator view.** NCUA/FDIC/OCC/FFIEC statements on third-party and MSP risk to small institutions; NCUA's lack of vendor-examination authority (status in 2026); any 2026 guidance tied to AI-enabled attacks.
5. **Secondary: VeloCloud and cloud secrets.** Briefly: is Arista VeloCloud SD-WAN marketed to or used in banking branch networks (vendor case studies only)? Any public incident at a digital-banking vendor (Q2, Alkami, nCino, Jack Henry digital) involving cloud secrets or keys?
6. **Counter-evidence, required.** Evidence that MSP-borne incidents rarely reach financial institutions, or that bank-grade MSPs are segregated from the generic MSP market.

## Out of bounds

Any exposure list of named institutions; scanning; technical remediation; trades (TERRY); grading desks' theses.

## Deliverable

Tables over prose, every cell sourced and dated: (1) outsourcing structure; (2) the October ConnectWise facts; (3) precedent table by route with financial-institution counts; (4) regulator statements; (5) VeloCloud and digital-vendor secrets (brief); (6) counter-evidence; (7) UNKNOWNs; (8) candidate escalation-watch row wording for CYPHER (CYPHER decides).
