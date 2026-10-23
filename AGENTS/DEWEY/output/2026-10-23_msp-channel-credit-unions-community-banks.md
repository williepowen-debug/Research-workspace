# The vendor-of-the-vendor route: managed IT providers, shared tools (ConnectWise) and US credit unions / community banks
**Date:** 2026-10-23 (research 11:12–11:28 ET) | **Mode:** Thesis | **Request:** REQ-DEWEY-20261023-001 (WALTER, Will-approved 2026-10-23 00:03 ET) | **Confidence:** High on structure and regulator facts (primaries read); Medium on precedents ("none named" is not "none affected"); Low on how often the channel actually reaches institutions (under-observed by construction)

## Key Finding

**The channel has wide reach but little observed traffic, and it is badly observed.**
- **Reach.** 91.2% of community banks have an outside party running all or part of their network monitoring (CSBS 2026: 45.0% fully outsourced, 46.2% shared). For credit unions, about 7 in 10 reported cyber incidents involved a third party (NCUA, Sept 2023 – Aug 2024).
- **Supervision.** NCUA cannot examine vendors, and since December 2025 FSOC no longer asks Congress to give it that power.
- **Observed traffic.**
  - Only **one** of 88 bank and credit-union breach notices in California and Washington since 2023 says the attacker came in through the institution's IT service provider (Alaska Air Group FCU, March 2026).
  - The only US multi-institution case through an IT provider is the Ongoing Operations/Trellance ransomware attack (Nov 2023). It hit ~60 credit unions, all with ≤$100M in assets, and restoration took ~17 days.
  - Neither Kaseya VSA (2021) nor ScreenConnect (2024) has a bank or credit union named in public reporting.
- **The October 2026 ConnectWise Cloud Backup compromise.**
  - **No financial institution has been named.** ConnectWise says "We have not identified confirmed downstream customer compromise". It adds this is "not assurance that no unauthorized activity occurred."
- **Who is reached.** The tier the channel reaches is the **small** one: sub-$100M credit unions and community banks that lack in-house IT. It is not large banks.

## Intake checks

| Check | Result | Source |
|---|---|---|
| **Kill condition:** a US bank, credit union or core/digital vendor publicly confirmed compromised via ConnectWise or any MSP since 10/15 | **NOT FIRED** (11:13–11:20 ET). No such disclosure found. The only October bank/credit-union notice on the California list (Citizens Bank, filed 10/19) has a **9/10** breach date and states no route ("an issue") | Web searches 11:13 ET; `scripts/breach_notices.py --name bank --name "credit union" --name FCU --since 2026-10-01` run 11:15 ET; [CA AG sb24-631520](https://oag.ca.gov/ecrime/databreach/reports/sb24-631520) |
| CYPHER `INCIDENTS.tsv` | CYB-INC-018 (Storm-0940 / ConnectWise) is already logged; there is no MSP-route bank row | `AGENTS/CYPHER/workbook/INCIDENTS.tsv` grep, 11:14 ET |
| DEWEY 10/22 outputs | Already covered: ConnectWise basics, Trellance, Marquis, TruStage, NCUA's lack of vendor authority, core-vendor concentration. **This report extends to the MSP layer and does not repeat them** | `output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md`, `…_trustage-cyber-outage.md`, `…_bank-legacy-technology_breach-notices.tsv` |

## (1) Outsourcing structure

| Measure | Figure | Source |
|---|---|---|
| Community banks, network service monitoring, 2026 (n=330) | **45.0% third party / 46.2% combination / 8.8% in-house** | [PRIMARY: CSBS 2026 Annual Survey, Fig. 11](https://www.csbs.org/2026-csbs-annual-survey) (Oct 2026); legend order checked against the core-processing row (77.2% third party) |
| Same question, 2023–2025 | 2023: 47.1 / 44.9 / 8.1 · 2024: 44.9 / 48.5 / 6.6 · 2025: 46.8 / 47.2 / 6.0 | [PRIMARY: CSBS 2023](https://www.csbs.org/sites/default/files/2023-09/CSBS%202023%20Community%20Bank%20Survey%2010.04.2023.pdf), [2024](https://www.csbs.org/sites/default/files/other-files/FINAL2024CSBSSurvey.pdf), [2025](https://www.csbs.org/2025-csbs-annual-survey) |
| Credit unions: share of reported cyber incidents involving a third party | **742 of 1,072 (~69%), 1 Sep 2023 – 31 Aug 2024.** The earlier window, 1 Sep 2023 – 1 May 2024, was ~73% of 892. No share has been published for later periods (539 incidents in May 2024 – Apr 2025; 588 in May 2025 – Apr 2026) | [PRIMARY: NCUA press release 2024-10-24](https://ncua.gov/newsroom/press-release/2024/board-briefed-cybersecurity-new-charters-and-field-membership); [PRIMARY: NCUA resilience report, Jun 2024](https://ncua.gov/news/publication-search/cybersecurity/cybersecurity-and-credit-union-system-resilience-annual-report-congress-2) |
| Credit-union assets "in some way managed or affected by unregulated third-party service providers" | ~90% (~$1.9T), an NCUA estimate | Same Jun 2024 report [PRIMARY] |
| Credit-union outsourcing rate (institutions, not incidents) | **No current figure.** The latest is 76% outsourcing network management and 86% outsourcing security monitoring (n≈110 credit unions and community banks, 2018) | [VENDOR-CLAIM: Safe Systems survey via CU Times, Feb 2018](https://www.cutimes.com/2018/02/07/understaffing-has-many-cus-outsourcing-it/) |
| Credit-union service organisations (CUSOs) | 1,127 registered; **258 list IT services**; 58 serve 100 or more credit unions (not split by service) | [PRIMARY: NCUA CUSOs at a Glance, as of 2025-12-31](https://ncua.gov/files/publications/cusos-at-a-glance-2025.pdf) |
| MSP tool market (all sectors, global) | ConnectWise 24.3%, Kaseya 22.7%, N-able 11.4%, NinjaOne 9.4% (Q2 2024); Kaseya 25.9% vs ConnectWise 25.4% (Q3 2024); ConnectWise "regained" first place (2025, no shares given) | [INSTITUTIONAL: Canalys via ChannelE2E](https://www.channele2e.com/news/big-3-rmm-psa-vendors-see-market-share-slip-canalys); [Channel Futures](https://channelfutures.com/psa-rmm/kaseya-and-connectwise-face-off-market-leaders-revealed); [Business of Tech, Jun 2025](https://businessof.tech/2025/06/23/msp-sector-surges-to-608b-as-platform-wars-reshape-psa-rmm-landscape/). **No 2026 shares found** |
| Which tools bank-specialist MSPs run (Safe Systems, CoNetrix, Integris-FI, Trellance/Ongoing Operations) | **UNKNOWN.** Not public | Searched; not found |

## (2) ConnectWise, October 2026: what the primaries say

| Item | Fact | Source |
|---|---|---|
| Product | Cloud Backup (formerly SkyKick), a multi-tenant Microsoft 365 app. SaaS Security and Cloud Management were suspended as a precaution on 10/18 | [PRIMARY: ConnectWise Trust Center advisory](https://www.connectwise.com/company/trust/advisories#cloudbackup), first published 10/16 17:47 UTC, read at its 10/23 14:00 UTC update |
| Timeline | Discovered **10/14**; access cut 10/17 05:00 UTC; 7 app identities disabled 10/17 07:00 UTC; service suspended by certificate revocation 10/17 17:00 UTC; full credential reset 10/19; phased restore from 10/21; testing expected to finish "by the end of that weekend" (≈10/25) | Same |
| Downstream | "We have not identified confirmed downstream customer compromise" … "the absence of confirmed compromise is not assurance that no unauthorized activity occurred." Its findings "do not establish whether individual partner or customer Microsoft 365 tenants were affected." Backups are "encrypted, isolated, and preserved, with no indication of compromise" | Same |
| Attribution and scale | "Microsoft assesses that Storm-0940 was responsible for the recently disclosed ConnectWise supply chain compromise"; Storm-0940 is a "China-state aligned actor". ARTEX sign-in attempts against **>2,250 tenants**. "Several" attacks gained privileged access; "the majority of the targeting wasn't successful." Password spray 10/10–10/14 | [PRIMARY: Microsoft Security Blog 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) |
| Sectors | "Financial services" is in Microsoft's list of **sectors ARTEX targets generally**, alongside 14 others. **No bank or credit union is mentioned or named**; the only FS reference is to Korean financial institutions in separate public reporting | Same |
| Tenant counts (third party) | Huntress: **162** tenants with confirmed unauthorized sign-ins as of 10/16; almost 1,000 Entra tenants with sign-in activity from the attacker's IP, >300 of them successful; last confirmed successful sign-in 10/15 08:44 UTC. Directory reads through Graph leave no audit trail. (DEWEY's 10/22 report carried 173, from The Hacker News) | [INSTITUTIONAL: Huntress](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access), **read via search excerpts because the page returned HTTP 403 to DEWEY 11:18 ET**; [NEWS: itNews](https://www.itnews.com.au/news/stolen-connectwise-skykick-credential-exposed-microsoft-365-tenants-629721) |
| Named victims, financial-institution disclosures | **None** as of 11:20 ET 10/23 | Searches; CA AG pull above |

## (3) Precedents by route

| Event | Date | Route | FIs that disclosed | Total victims | Duration | Source |
|---|---|---|---|---|---|---|
| Kaseya VSA / REvil | Jul 2021 | Zero-day in the on-prem remote-management tool, pushed to MSP clients | **0 named** | "Fewer than 60" MSPs and "fewer than 1,500" downstream businesses (Kaseya); the CEO described them as dental, architecture and similar small firms | Decryptor ~22 Jul | [NEWS: The Record](https://therecord.media/kaseya-more-than-1500-downstream-businesses-impacted-by-ransomware-attack); KEV CVE-2021-30116 [PRIMARY] |
| Ongoing Operations (Trellance) / FedComp core | 26 Nov 2023 | Ransomware at a CUSO hosting provider. Citrix Bleed as the entry point is one researcher's claim, unconfirmed | **~60 credit unions disrupted** (NCUA count), all ≤$100M in assets | ~60 credit unions | ~17 days (all back by 13 Dec) | [NEWS: American Banker, quoting NCUA](https://americanbanker.com/news/citrix-software-bug-leads-to-outages-at-60-credit-unions); [NEWS: CU Times](https://www.cutimes.com/2023/12/18/back-online-but-not-out-of-the-woods-cu-ransomware-update/) |
| ScreenConnect CVE-2024-1709 | Feb 2024 | Authentication bypass in a remote-access server; ransomware gangs exploited it | **0 named** | ~8,200 vulnerable instances (Shadowserver); victims named were local government and healthcare | — | KEV added 2024-02-22 [PRIMARY]; [NEWS: BleepingComputer](https://www.bleepingcomputer.com/news/security/black-basta-bl00dy-ransomware-gangs-join-screenconnect-attacks/) |
| MOVEit (vendor-hosted) | May–Jun 2023 | File transfer at vendors (Fiserv, FIS, Alogent and others) | 24 of DEWEY's 88 notices; ~130 banks overall (DEWEY 10/22) | Mass | Weeks to months of notice lag | DEWEY 10/22 notice table [PRIMARY-derived] |
| Marquis | Aug 2025 | Specialist marketing/compliance vendor (firewall configuration backups) | 74+ institutions (WALTER SIG-035) | — | — | DEWEY 10/22 (prior coverage) |
| **Alaska Air Group FCU** | Intrusion ~5 Mar 2026; notices ~Apr 2026 | Notice: "our third-party information technology (IT) service provider experienced a cybersecurity incident, allowing unauthorized actors to use its system to access AAGCU IT systems … may have accessed and copied certain files" | 1 | 10,705 people (Maine AG via search snippet; unverified) | — | [PRIMARY: CA AG notice PDF](https://oag.ca.gov/ecrime/databreach/reports/sb24-621928), text read by DEWEY 11:22 ET |
| TruStage | 11 Jul 2026 → | Credit-union insurance/retirement vendor, service outage | Mandiant: no third-party interaction observed | Unknown | >100 days | DEWEY 10/22 TruStage report |
| *Non-US:* C-Edge (India) | Jul 2024 | Ransomware at a shared technology provider for small banks | ~300 cooperative and rural banks | — | ~1–2 days | [NEWS: CSO Online](https://www.csoonline.com/article/3480250/over-300-indian-banks-suffer-payment-disruption-from-ransomware-attack.html) |
| *Non-US:* Tietoevry (Sweden) | Jan 2024 | Ransomware at an IT services data centre | Riksbank HR/payroll system (a central bank, not a lender) | Many Swedish organisations | ~17 days | [NEWS: Central Banking](https://www.centralbanking.com/fintech/cyber/7960801/riksbank-hr-system-restored-17-days-after-ransomware-attack) |

**Base rate in DEWEY's notice corpus** (California + Washington AG lists, Jan 2023 – Oct 2026, 88 bank/credit-union notices): **1 MSP/IT-provider route**, 24 file-transfer, 7 other vendors, 18 own network with route unstated. [PRIMARY-derived: `output/2026-10-22_bank-legacy-technology_breach-notices.tsv`]

**Live tool flaws in CISA's catalog of exploited vulnerabilities, 2026** (KEV v2026.10.21) [PRIMARY]:
- ScreenConnect CVE-2026-84869 (added 9/11)
- N-able N-central: three CVEs (8/3, 8/4, 9/8)
- SimpleHelp CVE-2026-48558 (6/29)
- BeyondTrust Remote Support CVE-2026-102764 (10/16)
- Arista VeloCloud Orchestrator CVE-2026-16812 (7/27) and CVE-2026-93952 (9/22)

All of the 2026-numbered CVEs carry ransomware-use "Unknown". **No bank or credit-union victim is named for any of them** (victim reporting was not checked for N-central or ScreenConnect 2026).

## (4) Regulator view

| Statement | Date | Source |
|---|---|---|
| NCUA "lacks statutory authority over third-party vendors" (it lapsed in 2001) | Jun 2024 | NCUA report above [PRIMARY] |
| **FSOC 2025 drops NCUA from its decade-old request for vendor authority.** Footnote 30: "NCUA has determined that it may have sufficient authority to monitor these risks through information sharing agreements." Every report from 2015 to 2024 named NCUA | 2025-12-11 | [PRIMARY: FSOC 2025 Annual Report p.80](https://home.treasury.gov/system/files/261/FSOC2025AnnualReport.pdf); [FSOC 2024](https://home.treasury.gov/system/files/261/FSOC2024AnnualReport.pdf) |
| H.R. 10230 (Foster) would repeal the sunset and give vendor authority to NCUA and FHFA. **Referred to committee only; no cosponsors** | Introduced 2026-09-02 | [PRIMARY: congress.gov API](https://api.congress.gov/v3/bill/119/hr/10230), read 10/23 |
| Proposed replacement third-party risk guidance from OCC, Fed and FDIC, **with NCUA joining for the first time**. It would "rescind and replace" the 2023 guidance, which "has been interpreted in an overly broad manner". A third party with access to segmented systems "is not necessarily higher risk". **Comments are due 2026-11-16** | 2026-09-15 | [PRIMARY: 91 FR 58536](https://www.occ.treas.gov/news-issuances/federal-register/2026/91fr58536.pdf) |
| Joint Statement on community banks and **core** providers. Core is "the most material, complex, and highest-risk" relationship. Agencies will weigh "the number and severity of computer security incidents" when deciding whether to add a provider to the service-provider examination program. **Generic MSPs are not addressed; NCUA is not a party** | 2026-09-11 | [PRIMARY: Fed/FDIC/OCC](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20260911a3.pdf) |
| Bank Service Company Act examinations: 16 distinct Significant Service Providers examined since 2020; ~30 Regional Service Provider exams a year. FDIC reads its scope to include "security monitoring". **There is no MSP-specific program, and selection is discretionary** | Aug 2025 | [PRIMARY: FDIC OIG MEMO-25-03](https://www.fdicoig.gov/sites/default/files/reports/2025-08/Significant%20Service%20Provider%20Examination%20Program%20Final%20Memo%20-%20Memo-25-03_0_0.pdf) |
| FDIC OIG: only 18 of 71 Regional Service Provider exams met frequency guidelines; FDIC has no full inventory of bank service providers | Dec 2023 | [PRIMARY: FDIC OIG AEC 24-01](https://www.fdicoig.gov/sites/default/files/reports/2023-12/AEC%20Memorandum%20No.%2024-01.pdf) |
| CISA/NSA/FBI and Five Eyes partners (AA22-131A): MSPs are "an initial access vector to multiple victim networks". No financial-sector mention and no counts | 2022-05-11 | [PRIMARY: CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-131a) |
| AI-enabled attacks: OCC Spring 2026 says AI "lowers the barrier to entry … increases the speed, scale, and sophistication"; NCUA's 2026 report cites a ~90% rise in AI-enabled attacks (relaying CrowdStrike); NYDFS letter (Oct 2024). **No FFIEC statement** | 2024–2026 | [PRIMARY: OCC SRP Spring 2026](https://occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/semiannual-risk-perspective-spring-2026.html) (quote via search excerpt); [NCUA 2026 report](https://ncua.gov/news/publication-search/cybersecurity/2026-cybersecurity-and-credit-union-system-resilience-report); [NYDFS](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks) |

## (5) VeloCloud and digital-vendor secrets (brief)

| Item | Finding | Source |
|---|---|---|
| VeloCloud marketed to banks? | **Yes, generically.** Arista sells a "VeloCloud SD-WAN Financial Services Solution Brief" for branch deployment; no bank or credit union is named in Arista's own marketing. Arista has owned VeloCloud since ~Jul 2025 | [VENDOR-CLAIM: Arista brief](https://www.arista.com/assets/data/pdf/VeloCloud-SD-WAN-Financial-Services-Solution-Brief.pdf) |
| VeloCloud flaws 2026 | Two Orchestrator CVEs in KEV (7/27, 9/22). A third, **CVE-2026-114625** (CVSS 9.9, Arista says "known to be actively exploited"), was published 10/22 and is **not yet in KEV**: re-check | [PRIMARY: Arista SA-0199](https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199) |
| Cloud secrets or keys leaked at a digital-banking vendor (Q2, Alkami, nCino, Banno/Jack Henry, Fiserv digital, Apiture, MeridianLink) | **Not found.** None of the listed SEC registrants filed an 8-K Item 1.05 (2023 – 10/23/2026). A ShinyHunters claim on Jack Henry (8/30) is unverified; Jack Henry's own 8/31 statement says fewer than 10 clients and a non-production environment (DEWEY 10/22) | data.sec.gov submissions [PRIMARY]; [UNVERIFIED: SOCRadar](https://socradar.io/data-breach/jack-henry-associates-shinyhunters-2026/) |
| For SHADE: is MSP compromise an insurance accumulation path? | **Named as one, never priced.** BIS/FSI–IAIS (Jun 2026): reliance on the same "managed service providers … can cascade across numerous companies simultaneously". No public MSP-specific loss scenario, and **no Kaseya insured-loss estimate**, was found | [INSTITUTIONAL: FSI-IAIS Insights No 75](https://www.iais.org/uploads/2026/10/FSI-IAIS-Insights-Cyber-insurance-unpacked-the-corporate-digital-safety-net.pdf) |

## (6) Counter-evidence

- **Observed frequency is low.** 1 of 88 notices is an MSP route. The multi-institution FI events run through **specialist** vendors: file transfer, core hosting, marketing (Marquis), insurance (TruStage). Generic MSPs do not appear.
- **The big MSP-tool waves named no FI.** Kaseya's victims were small non-financial firms; ScreenConnect's named victims were government and healthcare.
- **The one US multi-institution IT-provider case was a credit-union-specialist CUSO, not a general MSP.** Its blast radius stopped at ≤$100M credit unions, and it took about 17 days, with no reported deposit effect (DEWEY 10/22).
- **Partial separation for banks.** Bank-serving MSPs can be examined under the Bank Service Company Act, so the "bank-grade MSP" idea has a legal basis. Its coverage, however, is thin and discretionary (FDIC OIG).
- **The October event is an identity attack on Microsoft 365 email/files.** Per ConnectWise it is not a remote-management push of ransomware, and it is not core banking. The plausible harm path is data exposure and business-email fraud, not a deposit-system outage.
- **Against reassurance:** the channel is **under-observed by construction**.
  - An outage-only MSP event with no personal data exposed needs no state AG notice.
  - About 25% of notices omit the route.
  - NCUA's 69–73% third-party share counts *all* vendors, so it cannot be cut to MSPs.
  - Huntress notes that Graph directory reads leave no audit trail.

## (7) UNKNOWNs

1. Share of **credit unions** using an MSP (no figure newer than a 2018 vendor survey).
2. Which RMM/backup tools bank-specialist MSPs run.
3. How many ConnectWise Cloud Backup tenants belong to FIs, and whether any FI is among the 162 confirmed or the >300 successful sign-ins.
4. NCUA's third-party incident share after Aug 2024.
5. The NCUA "information sharing agreements" that FSOC cites: no NCUA primary found.
6. Kaseya insured loss; any priced MSP accumulation scenario.
7. Whether any FI was hit through the 2026 ScreenConnect or N-central KEV flaws (victim reporting not checked).

## (8) Candidate escalation-watch row for CYPHER (CYPHER decides)

> **MSP-channel row (candidate):** ESCALATE if a US bank, credit union or core/digital-banking vendor discloses (breach notice, 8-K, press release, NCUA/FDIC statement) that an intrusion entered through a managed IT service provider, a CUSO IT provider, or a shared RMM/backup/remote-access tool (ConnectWise, Kaseya/Datto, N-able, NinjaOne, SimpleHelp, BeyondTrust). **Escalate harder** if ≥2 institutions name the same provider, or if any outage passes 7 days. Live case to watch: ConnectWise Cloud Backup (restoration ≈10/25; no FI named as of 10/23). Tier: small (≤$1B community banks, ≤$100M credit unions). **Not** a core-vendor path. Base rate: 1 of 88 CA/WA notices 2023–2026.

## Source Quality Assessment

- **Strong (read at source by DEWEY or a leg, today):** structure (CSBS, NCUA), regulator texts (FSOC, Federal Register, FDIC OIG, joint statement), and the ConnectWise/Microsoft facts.
- **NEWS only:** precedent victim counts.
- **Read via search excerpts:** Huntress counts (the page returned 403) and the Maine figure for AAGCU.
- **Vendor marketing only:** tool market share comes from a Canalys relay and is 2024-dated.
- **The weakest link is the frequency claim:** the evidence of absence is weak evidence, for the reasons in §6.

## References
(accessed 2026-10-23 unless stated)
- ConnectWise advisory: https://www.connectwise.com/company/trust/advisories#cloudbackup
- Microsoft Security Blog 2026-10-21: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
- Huntress: https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access (403; via search excerpts)
- CSBS 2023–2026 surveys: URLs in §1
- NCUA Jun 2024 report; NCUA press release 2024-10-24; NCUA 2025/2026 reports; CUSOs at a Glance 2025: URLs in §1/§4
- FSOC 2024 and 2025 annual reports; 91 FR 58536; Joint Statement bcreg20260911a3; FDIC OIG AEC 24-01 and MEMO-25-03; CISA AA22-131A: URLs in §4
- congress.gov API H.R. 10230: https://api.congress.gov/v3/bill/119/hr/10230
- CA AG notices sb24-621928 (AAGCU) and sb24-631520 (Citizens Bank)
- CISA KEV JSON feed: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json (v2026.10.21)
- Precedent news sources: URLs in §3
- Reproduce: `python3 AGENTS/DEWEY/scripts/breach_notices.py --name bank --name "credit union" --name FCU --since 2026-10-01 --out <file>`; the KEV filter is on vendorProject/product for connectwise|kaseya|n-able|simplehelp|beyondtrust|velocloud; the CSBS figures come from `pdftotext -layout` on the survey PDFs, grepping "Network service monitoring" and reading the legend order (In-house, Combination, Third-party)

## Process Report
**Searches run:** DEWEY ran ~10 direct searches and fetches plus primary pulls (ConnectWise, Microsoft, NCUA, CA AG ×3, CISA KEV, Treasury). Three sized research legs on Opus (structure, precedents, regulators) did ~180 tool calls in total. The full `/deep-research` harness was not used: the residual was three bounded legs.
**Data gaps:** see §7.
**Source frustrations:**
- 403s: Huntress, mass.gov (Fusion CU), maine.gov, congress.gov web (its API works).
- CISA's KEV feed returned non-JSON to a bare curl; leg C's copy was used.
- WebFetch of Huntress timed out after 300s.
**Confidence in findings:** High on structure and regulators; Medium on precedents; Low on frequency.
**If I had more time/tools:**
- Bulk Massachusetts, Vermont, Texas and Montana AG notice pulls.
- NCUA FOIA for third-party incident counts after Aug 2024.
- Job-posting or partner-directory evidence on the tools bank-specialist MSPs run.
**Suggestions:** extend `breach_notices.py` to Vermont and Massachusetts (route text is often present there). Add a browser user-agent to the KEV pull in `kev_classes.py` if it lacks one.
**Leg note:** leg B flagged that Fusion Credit Union Ltd (Massachusetts notice #28342, "one of its managed services providers") is probably a Manitoba institution. It is excluded from the US counts.
