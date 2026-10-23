---
signal_id: "SIG-W-20261023-017"
date: "2026-10-23"
timestamp: "2026-10-23T15:39:48Z"
dispatched: "2026-10-23T15:39:48Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261023-001 deliverable, AGENTS/DEWEY/output/2026-10-23_msp-channel-credit-unions-community-banks.md (6fd185af5)"
domain: "CYBER"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["CYPHER"]
info: ["REGINALD", "GIBBS", "SHADE", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "cited deep research; High on structure and regulator facts, Medium on precedents, Low on frequency (under-observed by construction)"
resources: 1
safety_net: "clear"
word_count: 719
entities: ["ConnectWise", "Storm-0940", "Huntress", "NCUA", "CSBS", "FSOC", "Trellance", "Ongoing-Operations", "Kaseya", "ScreenConnect", "Alaska-Air-Group-FCU", "Arista-VeloCloud", "H.R.-10230"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b; DEWEY delivered create-only copies to all 4 REQ recipients (CYPHER, REGINALD, GIBBS, SHADE; verified, 0 backstops). WALTER spot-checked the NCUA 742-of-1,072 figure at the NCUA press release (match). Kill condition NOT FIRED. VULCAN (default CYBER info) omitted: no genuine delta beyond 039/047."
---
# DEWEY research (REQ-DEWEY-20261023-001): managed IT providers reach most small US banks and credit unions (91.2% of community banks outsource all or part of network monitoring), but observed traffic through that route is thin (1 of 88 CA/WA bank and credit-union breach notices since 2023) and no financial institution is named in the October ConnectWise compromise. The tier at risk is small institutions, not large banks

**Report:** `AGENTS/DEWEY/output/2026-10-23_msp-channel-credit-unions-community-banks.md` (commit 6fd185af5). **Commission:** REQ-DEWEY-20261023-001, Will-approved 10/23 00:03 ET. **Kill condition NOT FIRED** (DEWEY 11:13–11:20 ET): no US bank, credit union or core/digital vendor publicly confirmed compromised via ConnectWise or any MSP since 10/15. DEWEY delivered copies to every recipient below; WALTER verified the set (no backfill needed).

| Question | DEWEY's finding | Basis |
|---|---|---|
| Reach | Community banks, network monitoring 2026: 45.0% third party, 46.2% combination, 8.8% in-house (n=330). Credit unions: 742 of 1,072 reported cyber incidents (~69%) involved a third-party vendor, 9/1/2023–8/31/2024 (**WALTER re-read the NCUA press release: match**). NCUA estimates ~90% of credit-union assets (~$1.9T) are touched by unregulated third parties | CSBS 2026 Fig. 11; NCUA primaries |
| Observed traffic | 1 of 88 CA/WA bank/CU notices 2023–2026 names an IT-provider route (Alaska Air Group FCU, Mar 2026). Only US multi-institution IT-provider case: Ongoing Operations/Trellance ransomware, Nov 2023, ~60 credit unions all ≤$100M, ~17 days. Kaseya 2021 and ScreenConnect 2024 named no FI | DEWEY notice corpus; news for precedent counts |
| ConnectWise Oct 2026 | Cloud Backup (multi-tenant Microsoft 365 app); discovered 10/14; restore testing expected done ≈10/25. ConnectWise: "We have not identified confirmed downstream customer compromise", and that this "is not assurance". Huntress: 162 tenants with confirmed unauthorized sign-ins (DEWEY's 10/22 report carried 173 via The Hacker News; Huntress page 403, read via search excerpts). **No FI named** | ConnectWise advisory (10/23 14:00 UTC update), Microsoft 10/21 |
| Supervision | NCUA has no vendor-exam authority; **FSOC 2025 (12/11/2025) dropped NCUA from its 2015–2024 request for that authority** (fn 30, "information sharing agreements"; no NCUA primary found for those). H.R. 10230 referred only. Interagency third-party-risk replacement proposal, NCUA joining for the first time: **comments due 11/16/2026**. Bank-serving MSPs can be examined under the Bank Service Company Act, but coverage is thin and discretionary (FDIC OIG) | FSOC, 91 FR 58536, FDIC OIG |
| Insurance (SHADE) | MSP compromise is **named** as an accumulation path (FSI-IAIS Jun 2026) but **never priced**; no Kaseya insured-loss estimate found | FSI-IAIS Insights No 75 |
| VeloCloud | CVE-2026-114625 (CVSS 9.9, Arista says actively exploited) published 10/22, **not yet in KEV: re-check** | Arista SA-0199 |

**Counter-evidence (DEWEY §6):** multi-institution FI events have run through **specialist** vendors (file transfer, core hosting, Marquis, TruStage), not generic MSPs. The October event is an identity attack on Microsoft 365 email and files, not a remote-management ransomware push and not core banking: the plausible harm is data exposure and business-email fraud, not a deposit-system outage. **Against reassurance:** the channel is under-observed by construction (an outage-only event needs no state AG notice; ~25% of notices omit the route; Graph directory reads leave no audit trail). **"None named" is not "none affected."**

**Do not relay as:** "credit unions hacked through ConnectWise" (no FI named); "70% of credit unions use MSPs" (the 69–73% is a share of INCIDENTS involving any third party, not of institutions using MSPs); "regulators can't examine bank MSPs" (they can for banks, under the Bank Service Company Act; it is NCUA that cannot).

**UNKNOWNs:** credit-union MSP usage share (latest is a 2018 vendor survey); which tools bank-specialist MSPs run; whether any FI is among ConnectWise's affected tenants; NCUA third-party share after Aug 2024; any FI hit through the 2026 ScreenConnect or N-central KEV flaws (not checked).

**CYPHER ACTION:** DEWEY §8 drafts a candidate MSP-channel escalation-watch row (escalate on any US bank, CU or core/digital vendor disclosing entry via an MSP, CUSO IT provider or shared RMM/backup/remote-access tool; harder on ≥2 institutions naming the same provider or an outage past 7 days). CYPHER decides; its live session has already read the report (owner's working tree, uncommitted at dispatch: row not adopted, ConnectWise restoration check 10/26 decides). INFO: REGINALD and GIBBS (tier: ≤$1B community banks and ≤$100M credit unions, not your large-bank perimeter; GIBBS has nothing to grade), SHADE (accumulation named, unpriced), RED by BOARD. No trade is implied.
