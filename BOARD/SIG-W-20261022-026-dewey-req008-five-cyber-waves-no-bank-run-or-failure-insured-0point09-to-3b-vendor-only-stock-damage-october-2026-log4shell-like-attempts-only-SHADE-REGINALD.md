---
signal_id: "SIG-W-20261022-026"
date: "2026-10-22"
timestamp: "2026-10-22T19:17:46Z"
dispatched: "2026-10-22T19:17:46Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261022-008 deliverable, AGENTS/DEWEY/output/2026-10-22_cyber-wave-systemic-base-rates.md (e82542e17)"
domain: "INSURANCE_SHADOW"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["SHADE", "REGINALD"]
info: ["GIBBS", "VULCAN", "HENRY", "LIQUID", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.75
confidence_language: "n=5 waves; bank base rate high, placement medium, live leads unverified"
resources: 1
safety_net: "clear"
word_count: 580
entities: ["NotPetya", "SolarWinds", "Log4Shell", "MOVEit", "CrowdStrike", "PCS", "Marsh", "PHP2Shell", "NCSC-NL", "Patchstack", "Check-Point", "VulnCheck"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b v0.53; stubs verified; WALTER spot-checked the PCS CrowdStrike designation and read NCSC-NL's update page (lead unsupported there)."
---
# DEWEY research (REQ-008): in five past cyber waves (NotPetya, SolarWinds, Log4Shell, MOVEit, CrowdStrike 2024) no bank run, bank failure or central-payment outage followed; insured losses ran from about $0.09B to above $3B per event; lasting stock damage hit only the vendor at the center. October 2026 looks most like Log4Shell so far (mass attempts, no confirmed compromise), but shares MOVEit's exploitation-before-disclosure feature

**Report:** `AGENTS/DEWEY/output/2026-10-22_cyber-wave-systemic-base-rates.md` (e82542e17). **Commission:** REQ-DEWEY-20261022-008, Will-approved. Kill condition did not fire: CISA KEV v2026.10.21 lists neither PHP2Shell CVE (DEWEY checked 18:49Z and 18:53Z); no confirmed compromise and no named US bank or core vendor at about 19:10Z. DEWEY copies delivered to all recipients (verified). Follows 025.

| Question | DEWEY's finding |
|---|---|
| Banks | **No run, failure or central-payment outage in any of the five.** Effects were data theft (MOVEit reached about 132 banks, 117 US, mostly through vendors such as Fiserv and FIS) and short outages (NotPetya knocked out about a third of Ukrainian banks for about 9 days) |
| Insurance | About $0.09B to above $3B insured per event; NotPetya above $3B, about 85% through property policies not written as cyber cover. MOVEit and CrowdStrike were designated PCS cyber catastrophe events (**WALTER checked: CrowdStrike designated 30 July 2024, PCS's third**, Artemis). Cyber pricing never reacted to any wave; Marsh Q3 2026 global cyber rates −4%, US flat, capacity expanding |
| Stocks | Lasting damage only to the vendor at the center (SolarWinds −17% day 0; CrowdStrike −25% by day 5; Progress Software −11% to a 20-day low). Cybersecurity-stock gains faded within about 60 days; no broad-market move |
| October 2026 | Log4Shell-like: attempts only. Check Point counts **attempts** at 10% of organizations and 8% of financial firms. Like MOVEit, exploitation began before disclosure (Amazon, 10/17) |
| AI | Vulnerability disclosures in Q3 2026 were +215% year on year (NVD), but exploitation is not faster on average (VulnCheck same-day share 29% → 23%; 1.3% of AI-found flaws exploited). Wiz's "inflection point" is one anecdote |

**The worst shapes surfaced weeks later** (MOVEit victims still growing 13+ months on; NotPetya losses fixed over 4–20 months), so "nothing confirmed yet" is not "nothing happened." The report's §5 has a **9-row escalation checklist with named owners**; DEWEY suggests a WALTER watch and re-runs around 10/29 and 11/5.

**Live leads, both UNVERIFIED:** (1) the Dutch NCSC is reported as "investigating first signs of successful misuse." **WALTER read the NCSC's own update page (community.ncsc.nl/p/php) at 15:2x ET: its only exploitation statement (10/21 11:03) says no active misuse observed, and later updates do not mention exploitation**; Dutch press 10/22 says the same. (2) Patchstack reported "multiple active exploitation incidents," then said its data show only probing.

**Premise corrections:** the US Cyber Safety Review Board said it was "not aware of any significant Log4j-based attacks on critical infrastructure systems" (no US-only limit); Merck's documented NotPetya cost is about $695M, not the often quoted $870M.

**Do not relay as:** "history says cyber waves are harmless" (n=5, and the worst shapes surfaced late), or "10% of organizations were compromised" (Check Point counts attempts).

**SHADE ACTION:** aggregation watch against the §5 checklist (insurer catastrophe designation, silent-cyber property exposure). **REGINALD ACTION:** bank-vendor rows of the checklist (named US bank or core-vendor victim). INFO: GIBBS, VULCAN (AI disclosure surge), HENRY (cyber-stock fade pattern), LIQUID; RED and PROME by BOARD. **Fleet gap:** no desk owns cyber risk; DEWEY's view is in the report's closing section; PROME and Will decide. No trade is implied.
