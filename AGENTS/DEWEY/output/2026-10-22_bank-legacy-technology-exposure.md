# Regional and community banks: legacy technology and exposure to the October 2026 cyber wave
**Date:** 2026-10-22 (committed 16:13 ET) | **Mode:** Thesis | **Confidence:** Breach-route record: Medium-High (88 primary notices, 25% with no route stated) · Vendor dependence and core platforms: High (CSBS 2026 survey, vendor 10-Ks) · Bank-by-bank vendor map: Low (core vendor named in a 2024–26 primary document for 22 of 167 KRE banks) · Website exposure: Low-Medium (passive, homepage only, 20 of 26 readable) · Regulator view: High (quoted primaries) | **Request:** Will-directed (live session, plan reviewed 15:25 ET, "go ahead" 15:47 ET) | **Recipients:** REGINALD (action); GIBBS, SHADE, OZK, WAL, FLG, PROME (info); WALTER (record)

## Key Finding

**Older technology is widespread at smaller banks, but the breach record does not show it as the way in.**
- **Small banks depend on vendors for nearly everything.** 77% of community banks outsource core processing, and only 1.7% run digital banking themselves (CSBS 2026). The main cores are decades old: Jack Henry's on IBM i midrange computers, Fiserv Premier from before 1995, FIS Systematics on mainframes.
- **Regulators flagged aging and end-of-life technology in 2025 and early 2026** (OCC; the Fed in Feb 2026).
- **But the breach record points elsewhere.** Across 88 bank and credit-union breach notices filed with state attorneys general from 2023 to 2026, none cites outdated or unpatched software, and none names a core system. The documented routes are:
  - zero-day flaws in internet-facing file-transfer tools: 34%, mostly MOVEit in 2023;
  - intrusions on the bank's own network with no entry route stated: 25%;
  - email phishing: 24%;
  - vendors' networks: 10%.
- **Among credit unions, 69% of reported incidents came through third parties**, concentrated in 13 vendor events (NCUA).
- **No core-banking or digital-banking product is on CISA's list of software exploited in real attacks.**

**For the current wave (PHP2Shell targets PHP web servers), the exposed layer is bank websites and vendor web platforms, not cores.**
- **5 of the 20 bank homepages DEWEY could read run on PHP-based website software.** One of them, Home BancShares, openly declares WordPress 5.9.10, a 2022 version line. WordPress says only its current 7.1 line is "safe to use and actively maintained."
- **None of the 26 banks serves an eMudhra certificate.**
- **Which vendor runs each bank's core is mostly not public.** It is unknown for 108 of 167 KRE banks (58% of the ETF by weight) and stale for 34 more.

## Intake and scope

| Item | Decision / result |
|---|---|
| Plan | DEWEY plan of 15:25 ET. Will said "go ahead … now" at 15:47 ET. **Defaults applied:** universe = all 167 KRE holdings for the filing scan, plus a 26-bank deep map (8 fleet names, 14 large KRE holdings, 4 Florida banks); exposure checks = only what a normal visitor to a public website receives; recipients as above |
| Prior work extended, not redone | `output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md` (REQ-001: vendor concentration, the 22-bank map) and `output/2026-10-22_cyber-wave-systemic-base-rates.md` (REQ-008: wave base rates) |
| Four technology layers studied | (1) core system; (2) websites and digital banking; (3) edge devices and file transfer; (4) vendors and processors |
| Guardrail | No scanning, no probing, no querying scanning services about specific banks. Findings about named banks go only in this report and to the desks, **never to the BOARD as a list of exposed banks** |
| Data files saved with this report | `output/2026-10-22_bank-legacy-technology_kre-tech-map.tsv` (167 banks: vendor, status, evidence); `output/2026-10-22_bank-legacy-technology_breach-notices.tsv` (88 classified notices with URLs) |

## Evidence

### (1) What smaller banks run, and how old it is

| Item | Figure | Source |
|---|---|---|
| Outsource core processing | **77%** of 330 community banks (<$10B), surveyed Apr–Jul 2026 | [INSTITUTIONAL: CSBS 2026 Annual Survey, p. 15](https://www.csbs.org/2026-csbs-annual-survey) |
| Digital banking from the core vendor only | **62.5%**; core vendor plus fintech 34.1%; **internal resources only 1.7%** | same, p. 18, Fig. 17 |
| Satisfaction with core vendors | "more than half… neutral or dissatisfied… growing dissatisfaction… across several survey cycles" | same, p. 14 |
| Cyber as a risk | Top internal risk "for the ninth year in a row"; "close to 66%" call it the hardest challenge to adopting new technology | same, pp. 7, 17 |
| Legacy systems, tech spending, contract terms | **Not asked** in the 2024–26 surveys | CSBS |

| Vendor | Platform | Age / technology base | Status | Source |
|---|---|---|---|---|
| Jack Henry | SilverLake (>500 banks), CIF 20/20 (>200) | IBM i, written in RPG | Active; "no plans to draft any end-of-life letters" (2023); cloud replacement under construction for "several decades" at the 2023 pace | [PRIMARY: JKHY 10-K FY2026](https://www.sec.gov/Archives/edgar/data/779152/000077915226000067/jkhy-20260630.htm); [NEWS: IT Jungle, 31 Jul 2023](https://www.itjungle.com/2023/07/31/jack-henry-reiterates-ibm-i-support-for-the-foreseeable-future/) |
| Fiserv | Premier, Signature, DNA; newer Finxact and CoreAdvance | Premier dates from **before 1995** (ITI); IBM midrange and Unisys mainframe as of 2009 | **Precision and Cleartouch dropped from the "principal" list in the FY2025 10-K.** A signal only, not an announced sunset | [PRIMARY: Fiserv 10-K FY2025](https://www.sec.gov/Archives/edgar/data/798354/000079835426000009/fi-20251231.htm); [NEWS: IT Jungle 2009](https://www.itjungle.com/2009/12/08/fhs120809-story01/) |
| FIS | Systematics, IBS, Horizon | Systematics from the **1970s** on mainframe (relayed); IBS from Metavante (2009) | Active; FIS is building a "next-generation core… on a cloud foundation" | [PRIMARY: FIS 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1136893/000113689326000013/fis-20251231.htm); [NEWS: Finovate 2019](https://finovate.com/first-hawaiian-stays-with-fis-but-switches-core/) |

### (2) The bank-by-bank map: 167 KRE banks, from SEC filings

| Core vendor status | Banks | Notes |
|---|---|---|
| CONFIRMED (named in a 2024–26 primary document) | **22** | FIS 8, Fiserv 8, Jack Henry 4, TCS 1 (ZION), Evertec 1 (BPOP) |
| CONFIRMED-ROLE (processing or back office) | 2 | ASB, TRST (Fiserv) |
| REPORTED | 1 | FLG: Fiserv Finxact, "replacing legacy systems" (Fiserv release of 17 Aug 2026, seen only via a relay) |
| STALE (named only before 2024) | 34 | |
| UNKNOWN | **108** | **58.0% of KRE by weight** (DEWEY arithmetic on SSGA weights of 21 Oct 2026) |

Digital-banking vendor: confirmed for **6** banks, unknown for 150. Across 2023–26, no universe bank's filing names Alkami, Banno, Backbase, Thought Machine, Candescent, Nymbus or Mambu. Vendor share among confirmed and stale cores together: FIS 24, Fiserv 20, Jack Henry 11. Full map with evidence: `output/2026-10-22_bank-legacy-technology_kre-tech-map.tsv`. Method: SSGA KRE holdings as of 21 Oct 2026, then EDGAR full-text search on ~85 vendor and legacy terms (2010–26, ~1,350 documents parsed).

**Core changes under way** (all [PRIMARY] EDGAR unless noted):

| Bank | Change | Timing |
|---|---|---|
| PNFP | Legacy Pinnacle: Jack Henry → FIS (Synovus platform) | 1Q 2027 |
| FLG | → Fiserv Finxact (REPORTED) | 2027–28 |
| BPOP | Exit from Evertec | by 30 Sep 2028 |
| MBWM | Fiserv → Jack Henry | 2026–27 |
| PFS | → FIS IBS | 2026 |
| BANR | Core conversion | Nov 2026 (8-K 21 Oct 2026) |
| INDB | Conversion, vendor not named | $2.2M cost in Q3 2026 |
| RF | Core modernization | client migrations 2027 |

Conversions finished in 2026: FMNB, QCRH, SBCF (Villages), HFWA, EQBK, BBT, HBAN (Cadence), MCB.

**Legacy language in filings:**
- AMTB: "decommissioning of legacy technologies" (10-K, 27 Feb 2026).
- GSBC: "contractual disputes regarding its proposed conversion to a new core banking platform", with capitalized hardware and software written off (10-K, 6 Mar 2026).
- ZION: "end-of-life planning" (10-K, 24 Feb 2026).
- CCB: "$4.4 million of capitalized software amortization due to shortened useful lives associated with technology modernization" (10-Q, 7 Aug 2026).
- CUBI, as a counter-example: "unencumbered by legacy systems" (10-K, 27 Feb 2026).

**Florida rows:**

| Bank | Core | Digital | Notes |
|---|---|---|---|
| Seacoast (SBCF) | UNKNOWN (no vendor in filings 2010–26) | Q2 since 2022 (STALE, Q2 case study) | MOVEit exposure via a vendor serving Professional Bank accounts, 2023 (REPORTED); Villages conversion done Jul 2026 |
| BankUnited (BKU) | Fiserv (STALE; 8-K 27 Jun 2011) | UNKNOWN | — |
| Amerant (AMTB) | **FIS, CONFIRMED**: "The transition to FIS was completed in 2023" (10-K, 27 Feb 2026; DEWEY verified on EDGAR) | UNKNOWN | — |
| Capital City (CCBG) | Core ran **in-house until outsourced mid-2024** under a multi-year contract; vendor not named | UNKNOWN | 8-K 25 Jul 2023; 10-Q 31 Oct 2025 |

Updates to the earlier 22 rows:
- **SouthState (SSB):** now STALE Fiserv Premier. "Both SouthState and Atlantic Capital leverage Fiserv Premier for the core systems" (425, 23 Jul 2021; DEWEY verified).
- **Eagle (EGBN):** now STALE FIS (10-Q 2011).
- **East West (EWBC), Wintrust (WTFC), First Hawaiian (FHB):** move to STALE under the strict 2024 cutoff.

### (3) Website exposure: DEWEY passive check, 26 banks, 22 Oct 2026 ~19:55–20:00 UTC

**Method:** one normal homepage page load per bank, with a browser user agent. DEWEY read only what the site openly declares: response headers, the "generator" tag, and the paths that identify the website software. It also recorded the certificate the site served, and the external hosts linked from login or online-banking buttons. Nothing was scanned or probed.

**What this does and doesn't cover:** these are **marketing websites**, which are usually separate from online-banking and core systems. The PHP version is never declared, so "PHP-based" means *possible* exposure to PHP2Shell, not confirmed vulnerability.

| Finding | Banks | Detail |
|---|---|---|
| **Website software runs on PHP** (WordPress or Drupal) | **5 of 20 readable:** HOMB, AMTB (WordPress); WAL, FHB (Drupal, three markers each); EGBN (Drupal, one marker, so "probably") | PHP2Shell targets PHP. Every PHP-based site depends on its host having patched PHP; PHP 8.1 and earlier get no patch |
| **Outdated website software declared** | **HOMB:** "WordPress 5.9.10" (generator tag). **AMTB:** "WordPress 7.0.4" | WordPress: latest is 7.1.3 (6 Oct 2026) and "Only the most recent in the 7.1 series is safe to use and actively maintained" ([PRIMARY: wordpress.org releases](https://wordpress.org/download/releases/)). 5.9 shipped Jan 2022 |
| Old browser script libraries | SBCF jQuery 1.11.2 (2014); HOMB jQuery 3.3.1 (2018) | Known flaws are cross-site scripting in visitors' browsers, **not** the server-side PHP2Shell class. Low relevance to this wave |
| Server software declared | FNB Microsoft IIS 10.0 (current); AUB ASP.NET; EWBC Apache behind CloudFront; most others behind Cloudflare, CloudFront or Varnish, with nothing declared | A CDN in front hides the server; it does not patch the server behind it |
| **eMudhra certificates** | **0 of 26** | Issuers: DigiCert, Sectigo, Google Trust Services, Let's Encrypt, GoDaddy, Entrust, GlobalSign, Starfield, Amazon |
| Online-banking login hosts (vendor signals) | FIS-owned hosts linked from EWBC (`depositbridgeplus-eastwestbank.fisglobal.com`), FNB (`clientpoint.fisglobal.com`), SBCF (`dlmlr8.fisglobal.com`), CCBG (`fislbxcentral.com`); shared hosts `*.online-banking-services.com` (EGBN, UBSI) and `ebanking-services.com` (EGBN; WAL in REQ-001), operator UNVERIFIED | These are products linked from the site (deposit, lockbox, business banking), **not proof of the core vendor** |
| Not readable (bot protection, HTTP 403) | FLG, HBAN, UCB, EBC, PNFP, COLB | Certificate issuers only (none eMudhra) |

Recipe to reproduce: an HTTPS GET of `https://www.<domain>/` with a browser user agent. Record the Server, X-Powered-By and Via headers; the `meta name="generator"` tag; `wp-content`/`wp-includes`/`wp-json` (WordPress) and `drupal-settings-json`/`data-drupal`/`/sites/default/files` (Drupal); jQuery file versions; and the served certificate issuer via a standard TLS handshake on port 443. Domains are listed in the table and in REQ-001.

### (4) How small banks actually get breached

**Sample:** California and Washington attorney-general breach lists, bank and credit-union names, reported 1 Jan 2023 – 22 Oct 2026. 88 institution-incidents after collapsing re-filings, 71 of them cyber. The full classified list with URLs is in `output/2026-10-22_bank-legacy-technology_breach-notices.tsv`.

| Route (from the notice's own text) | Count | Share of 71 | Example |
|---|---|---|---|
| File-transfer tool (MOVEit ×21–22, GoAnywhere, vendor SFTP); 16 of 24 at a vendor | 24 | 34% | [Hanmi via Fiserv](https://oag.ca.gov/ecrime/databreach/reports/sb24-579424); [Hatch Bank, GoAnywhere](https://oag.ca.gov/ecrime/databreach/reports/sb24-563714); [Western Alliance](https://oag.ca.gov/ecrime/databreach/reports/sb24-599939) |
| Own network, entry route not stated | 18 | 25% | [Patelco](https://oag.ca.gov/ecrime/databreach/reports/sb24-590495); [Evolve](https://oag.ca.gov/ecrime/databreach/reports/sb24-588210) (its own FAQ says phishing); [SouthState](https://oag.ca.gov/ecrime/databreach/reports/sb24-583294) |
| Email-account compromise | 17 | 24% | [Summit State Bank](https://oag.ca.gov/ecrime/databreach/reports/sb24-583180) |
| Vendor's own network | 7 | 10% | [Truist via FBCS](https://oag.ca.gov/ecrime/databreach/reports/sb24-592704) |
| Web application or portal | 2 | 3% | [Varo, credential stuffing](https://oag.ca.gov/ecrime/databreach/reports/sb24-584955) |
| Edge device | 1 | 1% | [Wescom CU, Barracuda zero-day](https://oag.ca.gov/ecrime/databreach/reports/sb24-575506) |
| Unknown | 2 | 3% | — |
| **Notice cites outdated, unpatched or end-of-life software** | **0 of 88** | — | Regex over every notice. Every "patch" mention was patching *after* a zero-day |

Two time patterns:
- **2023 was the MOVEit year:** 20 of the 24 file-transfer cases.
- **From 2024 to 2026** the mix shifts to own-network intrusions (16) and email (13).

Vendor events reaching many banks at once (filed by the vendor; outside the count):
- **Marquis**, a marketing vendor: "over 74" banks and credit unions, 2025. Its initial notice said entry was through a SonicWall firewall; Marquis later said firewall configuration backups were stolen from SonicWall's cloud.
- **Finastra:** support SFTP platform, 2024.
- **Mercadien**, a CPA firm, 2025.
- **MOVEit through other parties:** Fiserv, FIS, Sovos and Alogent.

**Regulator incident data:**
- **NCUA:** 892 credit-union reports from 1 Sep 2023 to 1 May 2024, "approximately 73 percent… related to the use or involvement of a third party". It also cites "a third-party core service provider ransomware disruption affecting 60 small credit unions" ([PRIMARY: NCUA report to Congress](https://ncua.gov/news/publication-search/cybersecurity/cybersecurity-and-credit-union-system-resilience-annual-report-congress-2); DEWEY verified).
- **NCUA, full first year:** 1,072 reports, **742 (69%) third-party, from 13 vendor events**; ransomware 16 (1.5%) ([PRIMARY: NCUA board briefing, 24 Oct 2024, slide 6](https://ncua.gov/files/agenda-items/cybersecurity-board-briefing-20241024.pdf)). The same briefing lists "patching" among small credit unions' exam strengths.
- **FDIC:** 201 notifications under the 36-hour rule from 161 FDIC-supervised banks, Apr 2022 – Aug 2024 (~5.5% of banks), no route breakdown ([PRIMARY: FDIC paperwork-renewal statement for the rule, OMB 3064-0214, via the omb.report mirror](https://omb.report/icr/202408-3064-006/doc/151607901.pdf)).

**CISA's known-exploited list (v2026.10.21):**
- **Banking products:** zero entries for Fiserv, FIS, Jack Henry, Finastra, Temenos, Q2, Alkami, nCino, NCR, Evertec, Corelation and others.
- **The products tied to bank breaches are all listed:** MOVEit, GoAnywhere, Barracuda, Cleo and SonicWall. MOVEit, GoAnywhere and Barracuda were **zero-days**, exploited at or before disclosure.

**OCC enforcement (orders tagged IT, 2023–26):**
- **Small banks** (Lake Shore, First National MN, Vast, North Side, Blue Ridge, Touchmark): orders require IT programs, including "effective patch management… all network components… are appropriately updated" (Lake Shore, Feb 2023, [PRIMARY](https://www.occ.gov/static/enforcement-actions/ea2023-002.pdf)).
- **No order cites end-of-life software, a named breach or a core vendor.**
- **FDIC and Fed orders were not reachable.**

### (5) What regulators say

| Body | Date | Quote | Source |
|---|---|---|---|
| OCC Semiannual Risk Perspective | Fall 2025 (16 Dec 2025), p. 5 | "A recent firewall access incident highlights the ongoing importance of banks continuing to manage risks related to aging infrastructure and end of life (EOL) of IT assets." | [PRIMARY](https://www.occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-fall-2025.pdf) (DEWEY verified) |
| same | p. 9 | "prolonged use of older or legacy systems could increase the likelihood of operational outages, introduce security vulnerabilities, create system maintenance challenges, and reduce operational resilience." | same (DEWEY verified) |
| OCC | Spring 2026 (7 May 2026) | **No legacy or end-of-life language.** Shifts to AI-enabled "rapid vulnerability discovery and exploitation… timely patch management" | [PRIMARY](https://www.occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-spring-2026.pdf) |
| Fed, *Community Banking Connections* | 17 Feb 2026 | Windows 10 support ended 14 Oct 2025, "leaving many systems and environments exposed and vulnerable". "Common examples of legacy technology in community banks include core banking systems that are built on older platforms, outdated operating systems such as Windows 7 or macOS 12, and network hardware…" | [PRIMARY](https://www.communitybankingconnections.org/articles/2026/first-release-2026/navigating-legacy-technology-in-community-banking) (DEWEY verified) |
| Interagency third-party guidance | 9 Jun 2023 | Resilience includes "potential end of life issues with the software programming language, computer platform, or data storage technologies used by the third party" | [PRIMARY: 88 FR 37920](https://www.federalregister.gov/documents/2023/06/09/2023-12340) |
| GAO-15-509 | Jul 2015 (still open) | NCUA "lacks [the] authority" to examine third-party technology providers; the bills to grant it were not enacted as of Feb 2026 | [PRIMARY](https://www.gao.gov/products/gao-15-509) |
| Jack Henry 10-K risk factor | 28 Aug 2026 | "frontier AI allows these parties to identify and exploit software vulnerabilities faster and more broadly than ever before" | JKHY 10-K FY2026 |

No regulator publishes how much end-of-life software sits in banks. The Fed article gives no counts.

## Counter-Evidence

**Against "older technology at small banks is the vulnerable layer":**
- **The breach record doesn't show it.** 0 of 88 notices cite outdated software. The routes are zero-days in current internet-facing products, vendors, and email.
- **No core or digital-banking product appears in CISA's known-exploited catalog.**
- **Old cores are hard to reach from the internet.** They sit behind vendor-hosted digital layers; IBM i and mainframe cores are not internet-facing by design.
- **NCUA lists patching as a small credit-union exam strength**, and the OCC dropped its legacy language in Spring 2026.
- **The concentration that matters is the vendor, whatever its age.** One vendor ransomware attack disrupted 60 credit unions.

**Against "older technology is not a concern":**
- **Missing entry routes.** 25% of notices give no entry route, and lawyer-written notices omit causes. "0 cite outdated software" means never stated, not ruled out.
- **Regulators did flag it.** The OCC flagged aging infrastructure after a real firewall incident (unnamed), and the Fed says Windows 10's end of support left community-bank systems "exposed and vulnerable".
- **This wave targets the web layer, where old software is visible.** One fleet-adjacent bank declares a 2022-era WordPress line, and five of 20 readable homepages run on PHP-based software.
- **Small banks lag on vendors.** 98% depend on vendors for digital banking, and more than half are neutral or dissatisfied with their core vendor, so they control patch timing less than large banks do.
- **Conversions are a risk window.** Several banks are mid-conversion (PNFP, FLG, MBWM, BANR, BPOP's exit from Evertec), and conversions concentrate operational risk.
- **The evidence base is thin.** Who hosts each bank's website, what PHP version it runs, and which vendor runs 108 of 167 cores are all unknown. The absence of evidence is partly an absence of data.

## Unknowns

| Unknown | Why it matters | What would close it |
|---|---|---|
| Core vendor for 108 of 167 KRE banks (58% by weight); digital vendor for 150 | The vendor-concentration channel | Vendor client lists (FedFis/Cornerstone, paid); conversion announcements; bank IR |
| PHP version behind the five PHP-based bank websites, and who hosts them | Direct PHP2Shell exposure | Not observable passively by design. Bank or vendor statements |
| Whether any core or digital vendor (Fiserv, FIS, Jack Henry, Q2, Alkami) runs PHP in customer-facing layers | The many-bank channel for this wave | Vendor PHP2Shell advisories (none found yet) |
| Entry route for 25% of breach notices | The legacy-software question | Regulator incident data with routes (NCUA after 2024; FDIC/OCC/Fed 36-hour data not published) |
| FDIC and Fed IT-related enforcement 2023–26 | Supervisory evidence | orders.fdic.gov (did not connect); Fed search (JavaScript only) |
| Bank websites that blocked the check (FLG, HBAN, UCB, EBC, PNFP, COLB) | Coverage | A manual browser read |
| Fiserv Precision/Cleartouch status | Possible platform retirements affecting their client banks | Fiserv statement; client conversion notices |

## Source Quality Assessment

**Strong (primary):**
- CSBS 2026, the vendor 10-Ks, the OCC, Fed and Federal Register texts. DEWEY verified the OCC and Fed quotes.
- NCUA's report and briefing (verified).
- EDGAR filings for the vendor map; DEWEY verified the AMTB and SSB quotes.
- The breach notices themselves.

**Limits:**
- **The vendor map's main finding is absence:** most banks never name vendors.
- **The breach sample covers California and Washington only** (Maine's database is offline), and Washington lists only breaches of 500+ residents.
- **The website check covers homepages only,** marketing sites that may be hosted separately from banking systems; 6 of 26 sites blocked it.
- **Platform ages for Premier and Systematics** rest on 2009–2019 trade press.

## References

All accessed 2026-10-22. Links are inline. Key sources:
- CSBS 2026 Annual Survey: https://www.csbs.org/2026-csbs-annual-survey
- OCC Semiannual Risk Perspectives, Fall 2025 and Spring 2026 (links above)
- Fed Community Banking Connections, 17 Feb 2026 (link above)
- NCUA report to Congress and the 24 Oct 2024 board briefing (links above)
- California AG breach list: https://oag.ca.gov/privacy/databreach/list ; Washington AG: https://www.atg.wa.gov/data-breach-notifications and https://data.wa.gov/resource/sb4j-ca4h.json
- OCC enforcement search: https://apps.occ.gov/EASearch/
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- SSGA KRE holdings (as of 21 Oct 2026): https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx
- EDGAR full-text search: https://efts.sec.gov/LATEST/search-index
- Data files: `output/2026-10-22_bank-legacy-technology_kre-tech-map.tsv`; `output/2026-10-22_bank-legacy-technology_breach-notices.tsv`

## Process Report

- **Engine:** three Opus legs in data-return mode, plus DEWEY's own pull:
  - Leg A, landscape and regulators: 8 searches.
  - Leg B, the 167-bank filing map: 6 searches, ~1,350 EDGAR documents.
  - Leg C, the breach record: 6 searches, 88 notices.
  - DEWEY: the passive website check (26 banks) and verification.
- **Searches run:** 20 by the legs, 0 by DEWEY. The run was deliberately designed around the near-empty session search cap: EDGAR, agency datasets and direct fetches do not count.
- **DEWEY verified at the primary:** the OCC Fall 2025 quotes, the Fed article, NCUA's 892 / 73% / 60-credit-union figures, AMTB's "transition to FIS" and SSB's "Fiserv Premier" (EDGAR), the leg C notice counts (TSV), and the WordPress maintenance statement.
- **Data gaps:**
  - Most bank-vendor relationships.
  - Website hosting and PHP versions.
  - FDIC and Fed enforcement.
  - Maine AG (offline).
  - The FFIEC AIO booklet (CAPTCHA).
  - Vendor newsrooms: Fiserv 403, FIS timeout, nCino 429, Jack Henry 403.
- **Source frustrations:** vendor newsrooms block automated reads; 6 bank sites returned 403; Maine's breach database is offline after abuse.
- **Confidence:**
  - Medium-High that the documented breach route is vendors, zero-days and email rather than old cores.
  - Low on any bank-level exposure claim.
- **If I had more time/tools:**
  - A paid core-vendor dataset (FedFis/Cornerstone).
  - A manual check of the six blocked sites.
  - Vendor PHP2Shell advisories.
  - Re-running the website check after the PHP patches age by 2–4 weeks.
- **Suggestions:**
  - The KRE filing scanner (`efts` → sentence extraction) and the breach-notice classifier are reusable. Both are Will-gated builds for `scripts/`.
  - The passive website check is a cheap recurring watch for REGINALD.
