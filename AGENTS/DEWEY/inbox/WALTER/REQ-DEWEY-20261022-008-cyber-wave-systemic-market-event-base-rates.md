---
request_id: REQ-DEWEY-20261022-008
from: WALTER (Will-approved in the WALTER terminal, 2026-10-22 ~14:00 ET: "Yes, full study")
to: DEWEY
created: 2026-10-22 (UTC stamp in the commit)
state: NEW
flag_trigger: T1 new coverage channel (no fleet desk owns cyber risk) + T2 cross-channel (software vulnerability to bank operations, insurer losses and equity prices) + T3 load-bearing but thin (the fleet has no base rate for how cyber waves reach markets)
originating_evidence: SIG-W-20261022-025 (verified "Black October" ledger: PHP2Shell attempts in the millions, no confirmed compromise, not in CISA KEV as of 10/22 17:56Z; Japanese bank precautionary shutdowns only; eMudhra weak keys; supply-chain poisonings; no insurer statement; cyber stocks up 10/21) + SIG-W-20261022-019 (PHP2Shell reaches Japanese banks) + SIG-W-20261022-017 (bank vendor concentration; no cyber event has a documented deposit run) + WALTER helper ledgers AGENTS/WALTER/research/2026-10-22_afternoon/verify-cyber-supplychain.md and verify-cyber-php-sector.md
clusters: BANK_COLLATERAL (secondary AI_INFRA_CAPEX)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-008
kill_condition: At intake, check the CISA KEV catalog and news for a CONFIRMED mass compromise via PHP2Shell (CVE-2026-109618/-109619) or a named US bank / core-vendor victim. If either has occurred, report it to WALTER first (it is an IMMEDIATE routing item), then run the study with that event as the live case. Also grep AGENTS/SHADE, AGENTS/REGINALD, AGENTS/GIBBS and AGENTS/VULCAN for an existing cyber-event base-rate study; extend it if one exists.
deliver_by: no hard date; useful within a few days while the wave is live
---

# DEEP-RESEARCH REQUEST — Is a cyber wave like "Black October" a systemic, market-moving event? Base rates from past waves

**Why now:** a cluster of serious software failures hit in mid-October 2026 (PHP2Shell, the eMudhra certificate keys, several poisoned software packages), sped up by AI-assisted exploit discovery. Japanese banks took online services down as a precaution; cybersecurity stocks rose on fear alone. The fleet has no desk for cyber risk and no base rate for how such waves reach banks, insurers or markets. Will wants to go deeper.

**Decision question:** in past broad cyber waves, how often and how fast did the damage reach (a) bank operations or deposits, (b) insurer losses, and (c) equity prices of affected firms, cybersecurity vendors and software companies? What would distinguish a wave that stays a patching scramble from one that becomes a systemic loss event, and where does October 2026 sit today?

**What changes with the answer:** SHADE learns whether cyber-insurance aggregation is a real exposure for the insurers it watches. REGINALD and GIBBS learn whether bank operational risk from this wave deserves a watch row. VULCAN learns whether AI-found exploits change the software and cybersecurity picture. If history says waves like this rarely become loss events, the fleet stops reacting to the noise and watches only the named escalation signs.

## Scope (in bounds)

1. **Comparison set.** At minimum: NotPetya (2017), SolarWinds (2020), Log4Shell (Dec 2021), MOVEit (2023), and the CrowdStrike Falcon outage (July 2024, an accident, not an attack, included as the operational-outage case). For each: what was hit, time from disclosure to confirmed mass compromise, number of organizations affected, financial-sector victims, and how long before the full scope was known.
2. **Banks.** Any bank outages, deposit movements, regulator actions or bank-level losses in each wave. Distinguish data breaches from loss of service. Note 2024 CrowdStrike effects on bank and payment operations.
3. **Insurance.** Insured losses per event (Verisk PCS cyber, Lloyd's, Guy Carpenter, rating agencies), whether the event was treated as an aggregation or catastrophe event, war-exclusion disputes (NotPetya: Merck, Mondelez), and effects on cyber-insurance pricing and capacity.
4. **Equities.** Stock reactions of directly affected firms (SolarWinds, Progress Software for MOVEit, CrowdStrike 2024), of cybersecurity vendors, and of the broad market, with dates and windows. Note how long cybersecurity-stock gains lasted.
5. **October 2026 placement.** Using SIG-W-20261022-025 and the two helper ledgers: which past wave does it most resemble so far, and what would move it toward the worse cases? Name concrete escalation signs (e.g. a CISA KEV listing, a confirmed mass compromise, a named US bank or core-vendor victim, an insurer catastrophe designation).
6. **AI-assisted discovery.** Evidence on whether AI tools are increasing the rate of critical vulnerability discovery and exploitation (Wiz's "AI inflection point" claim, others), kept separate from vendor marketing.
7. **Counter-evidence, required.** Cases where loud waves produced little measurable financial loss, and analyses arguing cyber risk is overstated for markets.

## Out of bounds

Technical remediation advice; stock picks or position sizing (TERRY); grading any desk's thesis; general news collection (WALTER owns that).

## Deliverable

Tables over prose, every cell sourced and dated: (1) comparison table of past waves; (2) bank-impact table; (3) insured-loss and aggregation table; (4) equity-reaction table with windows; (5) October 2026 placement and escalation checklist; (6) counter-evidence; (7) explicit UNKNOWNs, plus a one-line view on whether the fleet needs a cyber owner and which desk.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-008. WALTER routes it as a research-output signal: SHADE and REGINALD action; GIBBS, VULCAN, HENRY, LIQUID, RED and PROME info.
