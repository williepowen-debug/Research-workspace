# Are bank-vendor products the kind that fail in waves like October 2026? A product-class comparison
**Date:** 2026-10-22 (~18:15 ET) | **Mode:** Thesis | **Confidence:** Exploited-flaw history by product class: High (full CISA KEV catalog, DEWEY classification) · Published-flaw counts by vendor: Medium (NVD keyword counts, a rough measure) · Trait comparison: Medium (vendor 10-Ks and passive checks; vendors' internal code and dependencies are not public) | **Request:** Will-directed (live session, 17:31 ET): "investigate whether or not these are the types of products that we can anticipate might have problems… how do they compare to some of the other issues being reported" | **Recipients:** REGINALD (action); VULCAN, SHADE, PROME (info); WALTER (record)

## Key Finding

**The banking-specific products (core systems, digital-banking platforms, processors) share none of the traits of what is failing in October 2026, and they have no history of mass exploitation.**
- **No exploited-in-the-wild history:** none of the 1,754 entries in CISA's KEV catalog is a banking-software product.
- **Almost no published flaws:**
  - Fiserv 5, Temenos 4, Bottomline 3 and Q2 2 published vulnerabilities (CVEs) in the US National Vulnerability Database (NVD).
  - Jack Henry, FIS, Finastra, Alkami, nCino and Evertec have none.
  - For comparison: PHP about 12,900, WordPress about 21,900, Fortinet 719 and MOVEit 77.

**What fails in waves like this is generic technology that banks and their vendors run around the banking products:**
- **File-transfer tools:** 18 KEV entries, **61% linked to ransomware**, the highest rate of any class.
- **Edge devices** (VPNs, firewalls, gateways): 198 KEV entries, 15% of all additions since 2023.
- **PHP runtimes and PHP-based websites:** 70 entries.
- **Microsoft products:** 403 entries.
- **Every documented bank breach route in today's earlier reports runs through these classes**, not banking software: MOVEit, GoAnywhere, Fortinet, Barracuda and SonicWall.

**The caveat that matters most: few known flaws is partly opacity, not proof of safety.**
- None of the bank vendors is a CVE Numbering Authority (CNA), the status that lets a company publish CVEs for its own products. Progress (MOVEit), Fortra, Fortinet, Ivanti and the PHP Group all are.
- Only Q2 and Alkami publish a vulnerability-disclosure contact (security.txt).
- Hosted (SaaS) products rarely get CVEs at all.
- **So bank-vendor flaws are less visible to attackers *and* to banks.** When one does fail, it fails across hundreds of banks at once: Trellance reached about 60 credit unions; Marquis reached 74+ institutions.

## What is being hit in October 2026, and why

From WALTER's verified ledger (SIG-W-20261022-025) and DEWEY's REQ-008 report:

| Item | Product class | Traits that made it fail |
|---|---|---|
| PHP2Shell (CVE-2026-109618/-109619) | Open-source language runtime | Public source code (AI-audited: Wiz); millions of internet-facing hosts; old versions (≤8.1) unpatchable; exploitation attempts began before disclosure |
| eMudhra certificate-authority keys | Trust infrastructure | Weak keys at a certificate authority; exposure via stale trust lists in non-browser software |
| LiteLLM 1.107.0 on PyPI | Open-source developer/AI package | Public package registry poisoned |
| Tensorlake and SubQuery npm packages; GhostAction | Open-source packages and CI pipelines | Registry and build-pipeline poisoning |
| OVHcloud CLI binaries | Vendor distribution channel | Signed downloads replaced |
| RankMath PRO plugin | WordPress (PHP) plugin | Plugin supply chain |
| Railway, Zeabur | Developer cloud platforms | Platform secrets exposure |
| Linux KSMBD | Open-source kernel module | Public code; narrow default exposure |

**Common traits:** open or publicly distributed code, enormous install bases, distribution through public registries or downloads, and direct internet exposure.

## Evidence

### (1) Trait comparison

| Trait | Wave products | Bank core and digital platforms | Source for the bank side |
|---|---|---|---|
| Code availability | Open source / public | **Proprietary, closed** | Vendor 10-Ks |
| Deployment | Millions of self-run installs | **Vendor-hosted for most small banks:** 77% outsource core; 98% use a vendor for digital banking. Q2 on AWS/Azure, Alkami on AWS, nCino on Salesforce + AWS | [CSBS 2026](https://www.csbs.org/2026-csbs-annual-survey); vendor 10-Ks (prior report) |
| Install base | Millions | Hundreds to low thousands per product (Jack Henry >900 core banks; Q2 1,200+; Alkami 301) | Prior report |
| Update channel | Public registries / downloads | Vendor-controlled hosted upgrades; some client-managed components (e.g. Fiserv CVE-2026-21665, "unsupported version 2021.2.4" of a loan print service) | [CVE record](https://cveawg.mitre.org/api/cve/CVE-2026-21665) |
| Internet exposure | Direct | Cores are not internet-facing by design; digital front ends are vendor-hosted web apps | Prior reports |
| Language | PHP, Python, JavaScript | RPG/IBM i (Jack Henry), COBOL/mainframe (Fiserv, FIS units), .NET, cloud stacks | Prior report |
| Public flaw disclosure | Public CVEs; vendor is a CNA (PHP Group, Progress, Fortra) | **Not CNAs; few or no CVEs** | §3 |

### (2) Exploited-flaw history by product class (CISA KEV, all 1,754 entries)

DEWEY classified every KEV entry by vendor and product name (CISA KEV JSON, catalog v2026.10.21, released 21 Oct 2026).

| Product class | All entries | Share | Added 2023+ | Share of 2023+ (n=888) | Linked to ransomware |
|---|---|---|---|---|---|
| Microsoft | 403 | 23.0% | 147 | 16.6% | 120 (30%) |
| Apple / Google / mobile / browser | 279 | 15.9% | 122 | 13.7% | 1 |
| **Edge: VPN, firewall, gateway** | **198** | 11.3% | **135** | **15.2%** | 67 (34%) |
| Open-source libraries/runtimes (non-PHP: Apache, Log4j, Atlassian, Linux etc.) | 124 | 7.1% | 55 | 6.2% | 24 |
| **PHP runtime / PHP apps and CMS** | **70** | 4.0% | 47 | 5.3% | 12 |
| VMware / virtualization / backup | 34 | 1.9% | 18 | 2.0% | 14 |
| **File transfer** (MOVEit, GoAnywhere, CrushFTP, Serv-U, Cleo, Wing FTP) | **18** | 1.0% | 12 | 1.4% | **11 (61%)** |
| **Banking / fintech software** (Fiserv, FIS, Jack Henry, Finastra, Temenos, Q2, Alkami, nCino, NCR, Evertec, FLEXCUBE, Finacle and others) | **0** | 0% | 0 | 0% | 0 |
| Other | 628 | 35.8% | 352 | 39.6% | 112 |

Edge devices are the fastest-growing class (11.3% of all entries, 15.2% of 2023+ additions). File transfer has the highest ransomware rate. Banking software has no entries.

### (3) Published flaws and disclosure posture by vendor

| Vendor / product | NVD CVEs (keyword match) | CNA? | security.txt disclosure contact |
|---|---|---|---|
| Fiserv | 5 | No | No (404) |
| Jack Henry | 0 | No | No (404) |
| FIS ("Fidelity National Information Services") | 0 | No | No valid file (no Contact line) |
| Finastra | 0 | No | No (404) |
| Temenos | 4 | No | — |
| Q2 ("Q2 Software") | 2 | No | **Yes** (Bugcrowd) |
| Alkami | 0 | No | **Yes** (HackerOne) |
| nCino | 0 | No | Not readable (429) |
| Evertec | 0 | No | No (404) |
| Bottomline | 3 | No | — |
| Oracle FLEXCUBE (mostly large and non-US banks) | 228 | Oracle is a CNA | — |
| *For comparison:* MOVEit | 77 | Progress: yes | — |
| GoAnywhere | 17 | Fortra: yes | — |
| SonicWall / Citrix / Ivanti / Fortinet | 153 / 326 / 398 / 719 | Fortinet, Ivanti: yes | — |
| PHP / WordPress | 12,891 / 21,868 (includes PHP apps and WordPress plugins) | PHP Group: yes | — |

**Method:**
- **NVD counts:** NVD API 2.0 `keywordSearch=<term>&noRejected`, reading `totalResults`, pulled ~21:45 UTC on 22 Oct. Keyword matching is rough; PHP and WordPress counts include third-party apps and plugins.
- **CNA list:** CVE Program `CNAsList.json` (GitHub cve-website repo, 559 entries), name match.
- **security.txt:** one GET of `https://<domain>/.well-known/security.txt` per vendor.
- **Wayback archive:** no archived Log4Shell advisory pages were found on any of the seven vendor domains. Advisories may have gone to client portals, which are not public.

### (4) Where bank-vendor products do overlap with the failing classes

| Overlap channel | Evidence | Status |
|---|---|---|
| **Generic enterprise tools at vendors and banks** (file transfer, edge, support platforms) | Every documented multi-bank event: MOVEit via Fiserv, FIS and Alogent; Finastra's support SFTP; Evertec's Fortinet zero-day and its support platform; Marquis/SonicWall | **Documented, repeated.** The proven failure channel |
| **Open-source components inside vendor products and build pipelines** | No vendor publishes a software bill of materials (SBOM). No public Log4Shell advisory found in the archive. Log4j sat in "hundreds of millions" of devices (CSRB) | **Unknown.** Opaque by design |
| **PHP web layers** | PHP-based websites (WordPress/Drupal) at Alkami, Evertec, CSI, Finastra and Alogent, and at 5 of 20 readable bank homepages (HOMB declares WordPress 5.9.10). Evertec declares patched PHP 8.3.36 | **Present at the marketing layer**; not documented in banking platforms |
| **Client-managed vendor software that ages** | Fiserv CVE-2026-21665 in an "unsupported version" of a client-run component | **Documented, single case** |
| **Developer and AI tooling at vendors** (the LiteLLM / npm class) | Vendors' 10-Ks describe AI adoption (Jack Henry, Fiserv, FIS, Q2, Alkami). Their tool stacks are not public | **Unknown** |
| **Certificate trust (eMudhra)** | No eMudhra certificate at 26 banks or 13 second-tier vendor sites | **Not observed** |

## Counter-Evidence

**Against "bank-vendor products are low-risk":**
- **Opacity.** No CNA status, near-zero CVEs, little public disclosure. Low counts may mean few flaws are *reported*, not few *exist*. Hosted SaaS flaws are typically fixed without a CVE, so neither KEV nor NVD would show them.
- **The AI-acceleration claim cuts both ways.** Wiz's PHP2Shell find used open source code, which banking cores are not. But AI can also probe hosted web apps from outside. The banking platforms' web front ends are internet-facing even if the cores are not.
- **Concentration amplifies rare failures.** One vendor event already reached ~60 credit unions (Trellance) and 74+ institutions (Marquis). NCUA attributes 69% of credit-union incidents to third parties.
- **Hidden dependencies.** Vendor products almost certainly contain open-source libraries; the Log4Shell precedent shows that route. DEWEY cannot see them.

**Against "bank-vendor products are high-risk in this wave":**
- **Zero KEV history** across the whole catalog, including the Log4Shell year.
- **Few published flaws, little self-hosted surface.** The core products are proprietary, written in non-PHP languages, and mostly vendor-hosted.
- **The documented failures went through generic tools** (file transfer, edge, email), which banks can inventory and patch.
- **No vendor or bank is named in the October wave.**

## What this means for anticipating problems

| Product class | Fails in waves like this? | Basis |
|---|---|---|
| File-transfer and support platforms (MOVEit, GoAnywhere, SFTP portals) used by banks and vendors | **Yes: highest-risk class** | 61% of its KEV entries are linked to ransomware; most bank breaches in 2023 |
| Edge devices (Fortinet, Citrix, Ivanti, SonicWall, Palo Alto, Barracuda) | **Yes** | 135 KEV additions since 2023; Evertec→Popular 2024; Barracuda→Wescom |
| PHP websites and CMS (bank and vendor marketing sites) | **Yes, but low banking impact** | Directly in the PHP2Shell class; separate from banking systems |
| Microsoft estates at banks and vendors | **Yes, routinely** | 403 KEV entries, 120 linked to ransomware |
| Core banking systems | **No history of it** | 0 KEV; closed, mostly vendor-hosted, not internet-facing |
| Digital-banking platforms (Q2, Alkami, nCino, Candescent) | **No history, but opaque** | 0 KEV; few CVEs; cloud-hosted web front ends |
| Peripheral data holders (marketing, collections, CPA firms) | **Yes, as data-breach sources** | Marquis, FBCS, Mercadien, NCB in the AG record |

## Unknowns

| Unknown | What would close it |
|---|---|
| Open-source dependencies inside bank-vendor products (SBOMs) | Vendor disclosure; FFIEC exam findings (not public) |
| Flaws fixed silently in hosted platforms | Vendor transparency reports (none published) |
| Whether vendors issued private PHP2Shell or Log4Shell notices to clients | Client banks; FS-ISAC |
| Which file-transfer and edge products each vendor and bank runs | Not public; breach notices reveal them after the fact |

## Source Quality Assessment

- **The KEV classification is complete and reproducible** (rules below), but rule-based. About 36% of entries fall in "other", and a few may be misclassified. The banking-software zero is robust: a name search across all vendor and product fields.
- **NVD keyword counts are rough** and include mentions of a term, not only flaws in that vendor's products.
- **CNA and security.txt checks are direct.**
- **The overlap table rests on the day's earlier primary-sourced reports.**

## References

- CISA KEV catalog JSON (v2026.10.21): https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD API 2.0: https://services.nvd.nist.gov/rest/json/cves/2.0
- CVE Program CNA list: https://raw.githubusercontent.com/CVEProject/cve-website/main/src/assets/data/CNAsList.json
- WALTER SIG-W-20261022-025 and helper ledgers `AGENTS/WALTER/research/2026-10-22_afternoon/verify-cyber-*.md`
- DEWEY reports, 22 Oct 2026: `output/2026-10-22_cyber-wave-systemic-base-rates.md`, `output/2026-10-22_bank-legacy-technology-exposure.md` (+ data files), `output/2026-10-22_bank-technology-vendors-risk-profile.md`

**Reproduction — KEV classes:** case-insensitive regex on `vendorProject + product`, applied in order:
- **banking:** fiserv|jack henry|\bfis\b|fidelity national|finastra|temenos|q2 |alkami|ncino|\bncr\b|diebold|evertec|corelation|hyland|bottomline|aci worldwide|oracle flexcube|finacle|symitar|backbase
- **file transfer:** moveit|goanywhere|accellion|kiteworks|crushftp|serv-u|cleo|wing ftp|sftp|filezilla
- **edge:** fortinet|forti|ivanti|pulse|citrix|netscaler|sonicwall|palo alto|pan-os|cisco asa|firepower|adaptive security|f5|big-ip|barracuda|zyxel|check point|juniper|sophos|watchguard|array networks|sangfor|draytek
- **PHP/CMS:** \bphp\b|wordpress|drupal|joomla|magento|vbulletin|phpmyadmin|thinkphp|laravel|craft cms|roundcube|zimbra|horde|cacti|glpi|elfinder|wp (the trailing "wp " catches WordPress plugin entries; without it the class reads 68, not 70)
- **Tool:** `scripts/kev_classes.py` (promoted 2026-10-22) reproduces this table.
- **open-source:** apache|log4j|struts|spring|jenkins|openssl|redis|elasticsearch|confluence|jira|atlassian|gitlab|nginx|tomcat|rails|node|python|linux kernel|sudo|polkit|bash|exim|samba
- **Microsoft:** microsoft|windows|exchange|sharepoint|office|internet explorer|\.net
- **Apple/Google/mobile/browser:** apple|ios|macos|safari|google|chrome|android|webkit|mozilla|firefox|samsung|qualcomm
- **VMware etc.:** vmware|vcenter|esxi|veeam|commvault
- **Ransomware:** `knownRansomwareCampaignUse == "Known"`.

## Process Report

- **Engine:** DEWEY primary pull only (KEV, NVD, CNA list, security.txt, Wayback CDX). **The session's 200-search web cap was spent**, so no press sweep and no sub-agents.
- **Data gaps:** vendor SBOMs; private client advisories; silently fixed SaaS flaws. Wayback returned no vendor Log4Shell pages (filter may be incomplete).
- **Confidence:** High that banking-specific products have no exploited-in-the-wild record and lack the wave's traits. Medium on what that implies, because opacity limits it.
- **If I had more time/tools:** a fresh-session sweep for vendor Log4Shell and MOVEit client advisories (FS-ISAC, bank 8-Ks) and for researcher write-ups of banking-platform flaws (bug-bounty disclosures on HackerOne and Bugcrowd for Q2 and Alkami).
- **Suggestion:** REGINALD's vendor watch row should key on the failing classes: KEV additions in file-transfer and edge products, and vendor support-platform incidents. Watching banking-product CVEs is not a useful signal.
