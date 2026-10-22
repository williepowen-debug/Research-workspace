# The vendors behind regional and community banks: reach, incident record, exposure to the October 2026 wave, and financial strain
**Date:** 2026-10-22 (committed 17:22 ET) | **Mode:** Thesis | **Confidence:** Incident record: Medium-High (EDGAR plus CA/WA attorney-general lists; press thin because the session search cap was spent) · Disclosure language: High (10-K text compared year by year) · October 2026 wave statements: Medium (absence on the pages readable; several vendor sites blocked) · Financial strain: High (filings; DEWEY verified Fiserv) · Client counts: Medium (self-reported) | **Request:** Will-directed (live session, 17:04 ET: "lets start looking at the vendors specifically"); follows `output/2026-10-22_bank-legacy-technology-exposure.md` | **Recipients:** REGINALD (action); SHADE, GIBBS, HENRY, FLG, PROME (info); WALTER (record)

## Key Finding

**The vendors banks depend on have a clean record on major SEC cyber disclosures, but a steady record of smaller incidents.** No cyber 8-K from any of the three core vendors (Fiserv, FIS, Jack Henry) from 2020 to 2026, and all three still say no incident has "materially affected" them. Underneath:
- **FIS filed its own MOVEit breach notices in 2023:** 4 with the California AG, 3 with Washington.
- **Jack Henry disclosed an Aug 2026 breach** (voice-phishing, fewer than 10 clients' data) **by press release only**, three days after a 10-K worded "As of the date of this filing".
- **Second-tier vendors produced the multi-bank events:**
  - Trellance/FedComp ransomware: about 60 credit unions offline (2023).
  - Marquis, a marketing vendor: 74+ institutions (2025).
  - Evertec, Popular's core processor: 2024 Fortinet zero-day that "migrated to one of Popular's domain controllers"; a fraud through its Brazilian unit in 2025; card data stolen via a support platform in May 2026.

**No vendor has issued a PHP2Shell or eMudhra notice** as of ~21:15 UTC on 22 Oct. The digital-banking platforms document cloud stacks (AWS, Azure, Salesforce), not PHP. The PHP use DEWEY could see is on vendor marketing websites only.

**The main new risk fact is financial strain at the two largest core vendors.** Both have been cutting guidance, and their stocks have collapsed:
- **Fiserv:** organic revenue −5% in Q2 2026, bank segment −8%; 2026 guidance cut to (1%)–0%; turnover in the CEO, President and CLO roles; interim heads run the bank-facing segment. Stock −78.6% from its March 2025 peak.
- **FIS:** ~$8B of added debt for the TSYS deal; guidance trimmed in Aug 2026. Stock −55% from its October 2024 peak.

## Scope

| Tier | Vendors | Why they matter |
|---|---|---|
| Core | Fiserv (Nasdaq: **FISV**; moved from NYSE "FI" ~11 Nov 2025), FIS, Jack Henry (JKHY); CSI (private, "#2 most-used core", self-reported) | Run account systems for most small banks (CSBS 2026: 77% outsource core) |
| Digital banking | Q2 (QTWO), Alkami (ALKT), nCino (NCNO), Candescent (ex-NCR digital banking, sold to a Veritas Capital affiliate Sep 2024) | 98% of community banks use a vendor for digital banking (CSBS 2026) |
| Processors / infrastructure | Evertec (EVTC), Finastra (private), Trellance (private) | Concentrated processing; documented multi-institution events |
| Peripheral data holders | Marquis, Alogent, Sefas/Messagepoint, FBCS, Fortra GoAnywhere, Mercadien, Infosys McCamish | **Most vendors named in bank breach notices are these**, not core vendors (prior report's data file) |

## Evidence

### (1) Reach

| Vendor | Reach (latest) | Source |
|---|---|---|
| Jack Henry | "over 7,200 clients"; cores at >900 banks (SilverLake >500, CIF 20/20 >200, Core Director ~200), >700 credit unions; nearly all revenue from financial institutions | [PRIMARY: 10-K FY2026, 0000779152-26-000067, 28 Aug 2026](https://www.sec.gov/Archives/edgar/data/779152/000077915226000067/jkhy-20260630.htm) |
| Fiserv | **No bank or credit-union client count in the 10-K.** Financial Solutions = 45.6% of FY2025 revenue ($9,664M of $21,193M) | [PRIMARY: 10-K FY2025, 0000798354-26-000009](https://www.sec.gov/Archives/edgar/data/798354/000079835426000009/fi-20251231.htm) |
| FIS | **No client count.** Banking Solutions = 73.5% of Q2 2026 revenue | [PRIMARY: 10-Q Q2 2026, 0001136893-26-000050] |
| CSI | "3,000+ customers" | [UNVERIFIED: company site] |
| nCino | ~1,500 banks and credit unions of >2,700 customers | [PRIMARY: 10-K FY2026, 0001902733-26-000022] |
| Candescent | "1,300+ financial institutions" | [UNVERIFIED: company site] |
| Q2 | "more than 1,200 financial institution customers" | [PRIMARY: 10-K FY2025, 0001410384-26-000006] |
| Trellance | "1,000+ credit unions" | [UNVERIFIED: company site] |
| Marquis | "over 500 banks and credit unions" | [UNVERIFIED: company site] |
| Alkami | 301 institutions on its digital platform; 22.4M users | [PRIMARY: 10-K FY2025, 0001529274-26-000009] |
| Evertec | Popular ≈ 29% of FY2025 revenue; runs Puerto Rico's ATH debit network | [PRIMARY: 10-K FY2025, 0001559865-26-000012] |

### (2) Incident record, 2020–2026

| Vendor | Event | Route (as stated) | Institutions reached | SEC disclosure | Source |
|---|---|---|---|---|---|
| FIS | MOVEit, 27–31 May 2023 | File-transfer zero-day | Umpqua (145,274 WA residents), Pathward/Emerald Card, Republic Bank, Sound Community Bank and others | **None** (no 8-K; 0 MOVEit mentions in filings) | [PRIMARY: CA AG sb24-571656, -573842, -574655, -576312](https://oag.ca.gov/privacy/databreach/list); data.wa.gov sb4j-ca4h |
| Fiserv | MOVEit 2023 (via client filings) | File-transfer zero-day | Flagstar (837,390 people), Hanmi | **None**; no Fiserv-filed notice in CA (5,378 rows) or WA | Prior report; CA/WA lists |
| Fiserv | "Everest" ransomware claim, May 2026 | — | — | None | **UNVERIFIED** (single French blog); not in Q2 2026 10-Q |
| Fiserv | CVE-2026-21665, Feb 2026 | Remote code execution in an **unsupported version** (2021.2.4) of a loan print service, client-managed deployments | Not stated | None | [PRIMARY: CVE record](https://cveawg.mitre.org/api/cve/CVE-2026-21665) |
| Jack Henry | 31 Aug 2026 | Voice-phishing (ShinyHunters); "internal, non-production corporate environment"; "No client-facing systems… core platforms… accessed" | PII of "fewer than 10 clients"; all 7,200+ notified | **No 8-K**; press release; no CA/WA notice | [PRIMARY company statement via Finviz reprint](https://finviz.com/news/387138/jack-henry-issues-statement-on-response-to-cybersecurity-incident) |
| Evertec | 2024 | **Fortinet** enterprise-management-server zero-day "migrated to one of Popular's domain controllers due to a shared network environment"; no Banco Popular customer data exfiltrated | Popular | Evertec's 10-K mentions "a third-party software vulnerability" without naming Fortinet; **Popular's 10-K names Fortinet** | [PRIMARY: Popular 10-K, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/763901/000119312526085756/d17859d10k.htm) (DEWEY verified) |
| Evertec | 29 Aug 2025 (Sinqia, Brazil) | Legitimate IT vendors' credentials used | 2 of 24 institutions on the environment; ~R$710M of unauthorized Pix (instant-payment) transactions | 8-K Item 8.01 | [PRIMARY: 0001559865-25-000043] |
| Evertec | 13 May 2026 | Data taken "through a third-party support platform": card numbers, transaction records | "primarily… financial institution clients in Puerto Rico" (count undisclosed); class actions from 12 Jun 2026 | 8-K Item 8.01, 9 Jun 2026; Popular 8-K the same day | [PRIMARY: 0001559865-26-000039](https://www.sec.gov/Archives/edgar/data/1559865/000155986526000039/evtc-20260609.htm); Popular 0001193125-26-263044 |
| Trellance / FedComp | Late Nov 2023 | Ransomware "through a third-party vendor, FedComp, using Trellance software" (NCUA via press) | **~60 credit unions** with outages | n/a (private) | [NEWS: ABC7/CNN](https://abc7news.com/ransomware-attack-in-us-credit-union-outages-trellance-cyberattack-ncua/14133374/); NCUA report to Congress ("60 small credit unions") |
| Finastra | 31 Oct – 8 Nov 2024 | Support file-transfer (SFTP) platform | Client count not stated | n/a | [PRIMARY: CA AG sb24-604911](https://oag.ca.gov/ecrime/databreach/reports/sb24-604911) |
| Marquis | 14 Aug 2025 | Network intrusion; SonicWall-linked (disputed, see prior report) | "over 74" institutions; 269,773 WA residents | n/a | [PRIMARY: CA AG sb24-614933](https://oag.ca.gov/ecrime/databreach/reports/sb24-614933) and later filings |
| Alogent | 30 May – 1 Jun 2023 | MOVEit zero-day (since discontinued MOVEit) | Huntington check data; 4,000 WA residents | n/a | [PRIMARY: CA AG sb24-574245](https://oag.ca.gov/ecrime/databreach/reports/sb24-574245) |
| FBCS | 14–26 Feb 2024 | Network intrusion / ransomware | Truist and others; 25,175 WA residents. **fbcs-inc.com now redirects to an unrelated Indonesian domain** | n/a | [PRIMARY: CA AG sb24-584498](https://oag.ca.gov/ecrime/databreach/reports/sb24-584498) |
| Fortra GoAnywhere | 2023; 2025 | KEV: CVE-2023-0669 (added 10 Feb 2023) and **CVE-2025-10035 (added 29 Sep 2025)**, both used in ransomware | Hatch Bank (2023) | n/a | [PRIMARY: CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) |
| Q2, Alkami, nCino, CSI | — | No Item 1.05 8-K; no vendor-filed CA/WA notices; no bank filing naming an incident. Alkami's 10-K: "vulnerable to and have experienced cybersecurity attacks" (not material) | — | — | 10-Ks above; CA/WA lists |

**Pattern:**
- **None of the three core vendors has filed a cyber 8-K,** and FIS and Fiserv's MOVEit exposure appears only in breach notices.
- **Multi-institution events come from processors and peripheral vendors** (Trellance, Marquis, Evertec, Finastra) and from **file-transfer and support platforms**, not core systems.
- **No banking product appears on CISA's KEV list.** File-transfer products do: MOVEit and GoAnywhere ×2.

### (3) What the vendors' own disclosures say now

| Vendor | Change in the latest 10-K | Filing |
|---|---|---|
| Jack Henry (FY2026) | **First admission** that incidents "have occurred in our systems in the past". New "frontier AI allows these parties to identify and exploit software vulnerabilities faster and more broadly than ever before, including… zero-day vulnerabilities". New "We rely on a limited number of third-party service providers that provide significant portions of our hosting". Materiality reworded to "**As of the date of this filing**, we have not determined that any known cybersecurity threat, including those arising from prior incidents, has materially affected…" (filed 28 Aug; incident disclosed 31 Aug) | [PRIMARY: 0000779152-26-000067](https://www.sec.gov/Archives/edgar/data/779152/000077915226000067/jkhy-20260630.htm) (DEWEY verified both quotes) |
| FIS (FY2025) | New: "the targeting of vendors who serve large numbers of customers for supply chain attacks"; "the use of AI by threat actors"; "cyber actors from some of the BRICS countries may conduct attacks on payment infrastructure"; EU DORA "Critical Third-Party Provider" designation | 0001136893-26-000013 vs -25-000014 |
| Fiserv (FY2025) | Unchanged materiality line ("not been materially affected… to date") in FY2023–25. Constant since FY2023: threats "have materially affected our business strategy and processes". New: AI-model safeguard and AI-regulation risks; cyber insurance mentioned | 0000798354-26-000009 vs -25-000047 |
| Alkami (FY2025) | New: "we have acquired and continue to acquire companies with cybersecurity vulnerabilities and/or unsophisticated security measures"; generative AI aids attackers | 0001529274-26-000009 |
| Q2 (FY2025) | New: "agentic" AI defence; insider-threat programmes; "Major global outages caused by faulty updates from a cybersecurity vendor" | 0001410384-26-000006 |
| Evertec (FY2025) | Drops the 2024 incident sentence; adds the Sinqia/Pix matter; the 2026 incident cost is not quantified in the Q2 10-Q | 0001559865-26-000012; -26-000047 |

### (4) The October 2026 wave

| Item | Finding (checked ~21:13–21:20 UTC, 22 Oct) |
|---|---|
| PHP2Shell flaws | Confirmed at the primary: GitHub advisories GHSA-w8hw-w9fx-j79w (CVE-2026-109618) and GHSA-6wmf-4rv5-p3rp (CVE-2026-109619), published 21 Oct 2026. Fixed in 8.2.35, 8.3.36, 8.4.27 and 8.5.12 (php.net ChangeLog, dated 22 Oct). Not in CISA KEV (v2026.10.21) |
| Vendor statements on PHP2Shell or eMudhra | **None found** at Fiserv, FIS, Jack Henry, Q2, Alkami, nCino, Candescent, Evertec, Finastra, CSI, Trellance or Marquis. Several pages were not readable (Fiserv newsroom 403; Jack Henry IR 403; nCino 429; Q2 IR 403; Fortra 403), so "none" covers readable pages only |
| PHP in client-facing products | **No public documentation.** The 10-Ks name AWS/Azure (Q2), AWS (Alkami) and Salesforce + AWS (nCino); "PHP" appears 0 times in the core vendors' 10-Ks. This is **absence of evidence, not evidence of absence** |
| PHP on vendor marketing sites (passive check) | WordPress at Alkami, Evertec and CSI; Drupal at Finastra and Alogent. **Evertec's site declares PHP/8.3.36, the patched release.** Others declare no version |
| eMudhra certificates | None among the 13 second-tier vendor sites checked |
| Fiserv's general guidance | Its cybersecurity page (first archived 11 Aug 2026, before the wave) warns that end-of-life systems "may no longer receive security updates" |

### (5) Financial strain

| Vendor | Facts | Source |
|---|---|---|
| **Fiserv** | Q2 2026 revenue −4%, **organic −5%, Financial Solutions −8%**. 2026 organic outlook cut to **(1%) to 0%**, adjusted EPS $7.20–7.40 (6 Aug 2026). 2025 outlook "reset" from ~10% to 3.5–4% (29 Oct 2025). Financial segment margin 38.7% vs 48.7%. CEO resigned 12 Jun 2026; President resigned 7 Jul (**interim leaders run Financial Solutions**); CLO left 30 Sep. Debt $27.9B. Securities class action | [PRIMARY: Q2 2026 release, 0000798354-26-000028](https://www.sec.gov/Archives/edgar/data/798354/000079835426000028/fisvq226earningsrelease.htm) (DEWEY verified); 8-Ks 0001193125-26-270336, -297448, -397250 |
| FIS | Debt $21.2B at 30 Jun 2026 (from $13.1B) after the TSYS deal; buybacks "temporarily curtailed"; pro forma guidance trimmed 4 Aug 2026; Chief Product Technology Officer resigned Mar 2026 | 0001136893-26-000050; release -26-000046 |
| Jack Henry | FY2026 revenue +7.1%, GAAP operating margin 25.0%; debt $40M; "record 58 competitive core wins" | 0000779152-26-000067 |

**Vendor stock prices** (DEWEY yfinance pull, adjusted closes; 22 Oct intraday at ~17:06 ET):

| Ticker | From 2-year peak | 2026 YTD | Since 20 Oct | Largest 1-day drop (2 yrs) |
|---|---|---|---|---|
| FISV | **−78.6%** (peak 3 Mar 2025) | −22.5% | +5.3% | **−44.0% on 29 Oct 2025** (the guidance reset) |
| FIS | **−55.3%** (peak 28 Oct 2024) | −39.8% | +5.1% | — |
| JKHY | −15.0% (peak 14 Jan 2026) | −8.2% | +4.6% | — |
| QTWO / ALKT / NCNO | −37% / −62% / −45% | −0.1% / −29.7% / −5.3% | +5.1% / +8.8% / +8.1% | — |
| EVTC | −12.5% | +16.9% | +4.9% | — |
| S&P 500 / KRE | −2.0% / −6.6% | +11.7% / +12.9% | −0.6% / +2.5% | — |

Incident windows (same method):
- **FIS and FISV around MOVEit (base 31 May 2023):** no reaction. +1.2% and +12.4% at +20 days vs S&P +6.5%.
- **JKHY after its 31 Aug 2026 disclosure:** −13.5% at +20 days vs S&P −0.5%. Confounded: no attribution to the incident is established.
- **EVTC after the 9 Jun 2026 8-K:** +27.7% at +20 days. Confounded.

The banking-software stocks rose 4–9% during the current wave while the S&P fell.

## Counter-Evidence

**Against "vendors are the weak point for this wave":**
- **No vendor is named as a PHP2Shell victim.** The platforms document non-PHP cloud stacks.
- **No banking product is on CISA KEV.**
- **The three core vendors report no material incident in six years.** Jack Henry's breach touched non-production systems only.
- **Markets show no vendor-risk pricing in the wave.**
- **Fiserv's and FIS's falls are business-driven** (guidance, growth, leverage), not cyber.

**Against "vendors are safe":**
- **The multi-bank events of 2023–26 all came through vendors:** Trellance ~60 credit unions; Marquis 74+; Evertec ×3; Finastra; MOVEit through Fiserv, FIS and Alogent. NCUA attributes 69% of credit-union incidents to third parties.
- **Disclosure is weak.** Vendors rarely file 8-Ks: Jack Henry used a press release, FIS's MOVEit appears only in AG notices, and Evertec doesn't name Fortinet. Absence in SEC filings understates incidents.
- **Old, unsupported vendor software exists in client hands** (Fiserv CVE-2026-21665 in an "unsupported version").
- **Strain at the largest vendor:** Fiserv's bank segment is shrinking (−8% organic) under interim leadership, the condition under which the 2025–26 regulator warnings about end-of-life technology would bite. This is a mechanism, not evidence of any lapse.
- **Peripheral vendors hold bank customer data with no regulatory perimeter.** FBCS's domain now redirects to an unrelated Indonesian site.

## Unknowns

| Unknown | Why it matters | What would close it |
|---|---|---|
| Whether any core or digital vendor runs PHP in client-facing layers | Direct PHP2Shell exposure across hundreds of banks | Vendor advisories; FS-ISAC; bank 8-Ks |
| Fiserv's and FIS's bank and credit-union client counts | Size of a single-vendor event | Not in filings; FedFis/Cornerstone (paid) |
| The "Everest" claim against Fiserv (May 2026) | Possible unreported incident | Fiserv statement; leak-site monitoring (out of scope) |
| Institutions affected by Evertec's May 2026 event; its cost | Puerto Rico concentration | Evertec Q3 2026 10-Q (due ~early Nov) |
| The 13 vendor events behind NCUA's 742 reports (2023–24) | Which vendors drive credit-union incidents | NCUA (not published by name) |
| Whether Fiserv's strain affects security investment | The financial-strain mechanism | Not observable from filings; supervisory (FFIEC) |
| Trellance unit identity (Ongoing Operations?) | Attribution | Trellance or NCUA statement |

## Source Quality Assessment

- **Strong:** EDGAR filings compared year by year; CA and WA AG notices filed by the vendors; the CVE and KEV records; the PHP primaries. DEWEY re-verified the Popular/Fortinet passage, the Jack Henry 10-K wording and the Fiserv Q2 2026 release.
- **Weak:** client counts for private vendors (self-reported); the Trellance attribution (press relaying NCUA); the Fiserv "Everest" claim (single blog).
- **Press coverage of vendor incidents is thin:** the session's web-search cap allowed 4 searches for this study.
- **Equity windows are single events and confounded.**

## References

All accessed 2026-10-22. Accession numbers are inline. Key:
- Jack Henry 10-K FY2026: https://www.sec.gov/Archives/edgar/data/779152/000077915226000067/jkhy-20260630.htm
- Fiserv 10-K FY2025: https://www.sec.gov/Archives/edgar/data/798354/000079835426000009/fi-20251231.htm ; Q2 2026 release: https://www.sec.gov/Archives/edgar/data/798354/000079835426000028/fisvq226earningsrelease.htm
- FIS 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1136893/000113689326000013/fis-20251231.htm
- Popular 10-K (Fortinet passage): https://www.sec.gov/Archives/edgar/data/763901/000119312526085756/d17859d10k.htm
- Evertec 8-K, 9 Jun 2026: https://www.sec.gov/Archives/edgar/data/1559865/000155986526000039/evtc-20260609.htm
- CA AG breach list: https://oag.ca.gov/privacy/databreach/list ; WA: https://data.wa.gov/resource/sb4j-ca4h.json
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Prior reports: `output/2026-10-22_bank-legacy-technology-exposure.md` (+ data files); `output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md`; `output/2026-10-22_cyber-wave-systemic-base-rates.md`

**Reproduction recipe for the stock table:** yfinance `history(period="2y", auto_adjust=True)` for FISV, FIS, JKHY, QTWO, ALKT, NCNO, EVTC, VYX, ^GSPC, KRE; peak = 2-year max close; "since 20 Oct" = last vs the 20 Oct 2026 close; incident windows as in the REQ-008 report.

## Process Report

- **Engine:** two Opus legs (core vendors; second tier), each capped at 2 web searches, plus DEWEY's stock pull and verification. The near-empty session search cap shaped the design: EDGAR, CA/WA AG data, CVE/KEV and direct page loads do not count.
- **DEWEY verified at the primary:** Popular's Fortinet passage, the two Jack Henry FY2026 10-K quotes, the Fiserv Q2 2026 organic and guidance figures, and the Evertec 8-K's existence.
- **Correction carried:** Fiserv trades as **FISV** (Nasdaq, since ~11 Nov 2025). The yfinance "FI" pull returned no data.
- **Data gaps:** Fiserv/FIS client counts; the Everest claim; Evertec's 2026 institution count; NCUA's 13 vendor events; vendor PHP use; several vendor pages blocked (403/429).
- **Source frustrations:** vendor newsroom and IR sites block automated reads (Fiserv, Jack Henry, Q2, Evertec, nCino, Fortra).
- **If I had more time/tools:** a fresh-session press sweep of vendor incidents (2020–26); Maine and Massachusetts AG lists; FS-ISAC advisories; Evertec's Q3 10-Q in early November.
- **Suggestion:** a vendor watch row for REGINALD (vendor 8-Ks, CA/WA AG vendor filings, KEV entries for file-transfer and edge products, vendor PHP2Shell advisories). It is cheap and mechanical.
