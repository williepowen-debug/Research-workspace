# US bank technology-vendor concentration and AI-agent/cyber risk

**Date:** 2026-10-22 | **Mode:** Thesis | **Confidence:** concentration by count: Medium · concentration by assets or by tier: none (no public data) · bank-to-vendor map: Low (most cells UNKNOWN or stale) · incident base rate: Medium, silent on the large-bank multi-week tail · 8-K counts: High (two independent EDGAR methods agree) · AI-agent channel: Medium for on-record statements, Low for anonymous claims | **Request:** REQ-DEWEY-20261022-001 (WALTER; Addendum 1 considered) | **Recipients:** REGINALD (action); GIBBS, VULCAN, OZK, WAL, FLG, LIQUID, RED, PROME, TERRY (info)

## Key Finding

Counted by institutions, US bank technology is concentrated. In 2022 survey data three core vendors ran more than 70% of banks (Fiserv 42%, Jack Henry 21%, FIS 9%). In 2026 the top four digital-banking vendors hold 71% of bank mobile-banking installations, and one federally examined service provider serves more than 4,200 banks. One vendor event can therefore reach many banks at once, and the 2023 MOVEit campaign did reach 5 of the 22 listed banks studied here through third parties. However, as of 2026-10-22 there is no confirmed multi-bank core-vendor compromise and no reported AI-agent loss anywhere. No IT or cyber event, at one bank or many, has a documented deposit run or a lasting fall in an affected bank's stock: the measured effects are small, slow and reversed, and the lasting stock damage fell on vendors. **Which vendor each listed regional bank uses is mostly not public: only 4 of the 22 banks have a core vendor named in a 2024–2026 primary document.**

## Intake checks

| Check | Result as of 2026-10-22 | Source |
|---|---|---|
| **Kill condition:** a confirmed multi-bank core-vendor compromise | **Holds. None is confirmed.** This report therefore answers a structural and base-rate question; there is no event in progress to measure | Sections (3) and (3b) below |
| Jack Henry incident, disclosed 2026-08-31 | PII of **fewer than 10 clients**; "a limited portion of our internal, non-production corporate environment"; "no system outages"; no core or processing systems accessed; vishing attributed to ShinyHunters; extortion refused; **no 8-K filed** (press release only) | [PRIMARY company statement via Finviz reprint](https://finviz.com/news/387138/jack-henry-issues-statement-on-response-to-cybersecurity-incident); [NEWS: American Banker](https://www.americanbanker.com/news/jack-henry-refuses-to-pay-extortionists-after-data-theft) |
| Axios, 2026-10-22, "Unvetted AI agents are accessing U.S. bank accounts" | Published and not retracted. The alarming claims (agents "gone rogue", call-centre contacts, "horrifying") are **anonymous**. No theft or loss figure was reported. Reuters could not verify the story independently. Morgan Stanley said on record that it has not seen "rogue AI agents accessing our platforms" | [NEWS: Axios (original 403; read via relays)](https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access); [UNVERIFIED relay: Decrypt](https://decrypt.co/381602/banks-rogue-ai-agents-inside-customer-accounts) |
| Microsoft, 2026-10-21, Storm-0940 / "ARTEX" agentic framework / ConnectWise | Published and not retracted. Sign-in attempts against **more than 2,250 tenants (TARGETED)**. Microsoft gives no compromised count beyond "several" and "many organizations". A separate spray of 151,000+ logons against 327 accounts at 8 organizations had "no successful authentication". **Huntress: 173 tenants with confirmed unauthorized sign-ins as of ~10/17.** **No bank or credit union is named as affected**; "financial services" appears only in Microsoft's list of sectors ARTEX targets generally | [PRIMARY: Microsoft Security Blog 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/); [NEWS: The Hacker News 2026-10-17](https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html) |
| Is ConnectWise a core-banking vendor? | **No.** The compromised product is ConnectWise Cloud Backup (formerly SkyKick), a multi-tenant Microsoft 365 app sold through managed-service providers. It is an IT-tool vendor and does not process deposits or payments | Same sources |
| Bank list | 8 fleet names (WAL ZION OZK FLG HBAN VLY SSB EGBN) plus the KRE top 15 by weight from SSGA's daily holdings file as of 2026-10-21 (EWBC UCB UBSI EBC PNFP FHB HOMB OZK FBP BPOP WTFC FNB COLB AUB GBCI). OZK is in both, so the list has **22 banks**. **Caveat: KRE is close to equal-weighted (the top 25 weights run 1.11%–1.18%), so "top 15 by weight" is close to arbitrary** and is not a ranking of size or risk | [SSGA KRE daily holdings file](https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx) (as of 2026-10-21) |
| WALTER Addendum 1 leads | ConnectWise was used (Microsoft primary plus Huntress). **NOT checked:** CrowdStrike AI-agent campaigns, PHP2Shell, the backdoored LiteLLM release / Railway / Zeabur, and the GitLab and Node.js flaws. These belong to the general cyber base rate and fall outside this question | — |

## Evidence

### (1) Vendor market share, by tier where any data exists

**The public record gives vendor share by *count of institutions*, not by *assets*, and no source gives share by bank tier ($10–100B or >$100B).** About 31 institutions over $100B hold about 65% of bank plus credit-union assets: 8,741 federally insured banks and CUs under $100B held $9.6T, about 35% of the assets of all 8,772 federally insured institutions (BauerFinancial, 2025-09-30, as cited in Q2 Holdings' FY2025 10-K) [PRIMARY]. Asset-weighted share is therefore decided by the largest banks, and for that tier no public vendor data exists. The latest by-count bank figures come from a **survey of 2022 data**, not a census.

| Class | Tier | Measure | Value | Basis | As-of | Source |
|---|---|---|---|---|---|---|
| Core | All banks (survey sample) | Fiserv / Jack Henry / FIS | **42% / 21% / 9%**; Big Three ">70 percent of banks surveyed"; CSI 7%, Finastra 3%, COCC 3% | Count; survey, **not a census**, not by assets | 2022 data, published 2024-03-27 | [PRIMARY/ACADEMIC: KC Fed briefing citing ABA 2023 Core Platforms Survey](https://www.kansascityfed.org/research/payments-system-research-briefings/market-structure-of-core-banking-services-providers/) |
| Core | Banks ≤$55B | Jack Henry | **>900 of ~4,300 banks (~21%)**; SilverLake >500 banks (~13%) | Count | FY2026 10-K (FYE 2026-06-30); denominator at 2025-12-31 | [PRIMARY: JKHY 10-K FY2026](https://www.sec.gov/Archives/edgar/data/0000779152/000077915226000067/jkhy-20260630.htm) |
| Core | Ceiling | Jack Henry | Core clients served only **up to ~$55B assets** (payments clients to $200B+) | Vendor statement | FY2026 | Same |
| Core | <$10B | Any vendor | **No public by-tier share.** Qualitative only: Jack Henry "primarily serves small banks", FIS "primarily… large and midsized", Fiserv serves both | Qualitative | 2024 | [KC Fed 2024-03-27](https://www.kansascityfed.org/research/payments-system-research-briefings/market-structure-of-core-banking-services-providers/) |
| Core | >$10B | FIS | 78 banks | Count | 2019 (Aite) | Same |
| Core | $10–100B | Any vendor | **GAP: no public data** | — | — | — |
| Core | >$100B (~31 institutions, ~65% of assets) | Any vendor | **GAP: no public data.** Jack Henry is effectively zero here (ceiling $55B) | — | 2025-09-30 | [PRIMARY: Q2 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1410384/000141038426000006/) |
| Core + digital | All FIs | Fiserv Banking | ">3,500 financial institutions"; claims "#1 in U.S. core and digital banking" | Count; **mixes core and digital, banks and CUs**; secondary, deck 403 | 2026-05-14 | [UNVERIFIED: investor-day notes](https://bobhammel.substack.com/p/fiserv-investor-day-notes) |
| Core | Credit unions | Fiserv / Jack Henry / Corelation | 25.9% (−118 bp YoY) / 12.0% / 4.7% (+67 bp) | Count | mid-2025, published 2025-12-01 | [INSTITUTIONAL: Callahan](https://creditunions.com/blogs/leaders-of-the-pack-the-top-20-cores-for-credit-unions/) |
| Digital | Banks | Top 4 / top 10 vendors | **71% / 92.8%** of mobile-banking installations; Fiserv first, Jack Henry second | Installations, banks only; vendor-level percentages not read | published 2026-05-13 | [INSTITUTIONAL: FI Navigator via CCG Catalyst 2026-10-07](https://www.ccgcatalyst.com/thought-leadership/research-snapshot/sector-spotlight-digital-banking-landscape/) |
| Digital | Credit unions | Top 4 / top 10 | 45.5% / 77.5% | Installations | published 2026-09-01 | [INSTITUTIONAL: William Mills / FI Navigator](https://www.williammills.com/news/u.s.-credit-union-mobile-banking-market-share-report-published-by-william-mills-agency-and-fi-navigator) |
| Digital | Banks + CUs | Alkami | 301 FI clients; 22.4M users | Count (mixed) | 2025-12-31 | [PRIMARY: Alkami 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1529274/000152927426000009/) |
| Digital | Banks + CUs | Q2 | 27.8M registered users; **no FI count disclosed** | Users | 2026-06-30 | [PRIMARY: Q2 Q2-2026 release](https://www.businesswire.com/news/home/20260729254821/en/) |
| Digital | Banks + CUs | Candescent (ex-NCR) | ">1,300 banks and credit unions" (all services) vs ">600" on digital banking | Count; conflicting definitions | 2024 / undated | [NEWS: IT Brief Sept 2026](https://itbrief.co.uk/story/candescent-expands-google-cloud-ai-tie-up-for-banks) |
| Aggregation | **One bank only (JPMorgan)** | Plaid + Yodlee + Morningstar + Akoya | >95% of data pulls on JPMorgan's systems | Share of pulls, one bank | Nov 2025 | [NEWS: Payment Expert 2025-11-17](https://paymentexpert.com/2025/11/17/jpmorgan-chase-to-charge-fintechs-for-customer-data-access/) |
| Supervision | One unnamed significant service provider (SSP) | Bank clients | "can exceed **4,200**" | Count | Aug 2025 | [PRIMARY: FDIC OIG MEMO-25-03](http://fdicoig.gov/sites/default/files/reports/2025-08/Significant%20Service%20Provider%20Examination%20Program%20Final%20Memo%20-%20Memo-25-03_0_0.pdf) |

Two readings follow from the table. First, by count, digital banking is more concentrated than core among banks (top four 71% of installations, against Big Three cores at >70% in a 2022 sample). Among credit unions it is much less concentrated (45.5%). Second, the cohort under study sits mostly in the $10–100B band, which has no share data at all. Jack Henry's $55B ceiling means the large banks among the 22 can only be on FIS, Fiserv, another vendor or in-house cores. The bank-level map in (2) is consistent with that: FIS is the most frequently named core. The supervisory side acknowledges the concentration in plain words. The 2026-09-11 Joint Statement by the FRB, FDIC and OCC says "a small number of large providers dominate the core processing market" and that "market concentration can limit community banks' negotiating power" [INSTITUTIONAL: [Troutman, Sept 2026](https://www.troutmanfinancialservices.com/2026/09/federal-banking-agencies-issue-joint-statement-on-community-banks-engagement-with-core-service-providers/); [Mayer Brown, Sept 2026](https://www.mayerbrown.com/en/insights/publications/2026/09/federal-banking-agencies-issue-proposed-updates-to-interagency-third-party-risk-management-guidance-and-joint-statement-on-core-service-providers)].

### (2) Bank-to-vendor map, 22 banks

**The vendor-identity gap is itself the main mapping finding.** Most banks do not name their core or digital vendor publicly. Their 10-Ks carry a generic risk factor, for example WAL's "We rely on third parties to support critical business operations, such as data processing… online banking systems", with no vendor named. Confidence labels:
- **CONFIRMED:** the bank's own filing or release, or the vendor's own named-client release or client list.
- **REPORTED:** trade press, or a state breach notice seen through a search index.
- **UNVERIFIED:** a job posting, or a login host or script domain observed on the bank's homepage on 2026-10-22. These are leads only, not evidence of the vendor.
- **UNKNOWN:** nothing found.

**The document date is stated in every cell.** A CONFIRMED cell resting on a 2011–2021 document says what the vendor was then, not what it is now.

| # | Ticker | List | Core vendor (label, source, document date) | Digital platform (label, source, date) | Vendor-channel incident disclosed 2023–26 | Core change in flight |
|---|---|---|---|---|---|---|
| 1 | WAL | Fleet | UNKNOWN: risk factor only, [10-K 2026-02-23](https://www.sec.gov/Archives/edgar/data/1212545/000162828026010336/wal-20251231.htm) | UNVERIFIED login hosts: retail `…/uux.aspx`, business `ebanking-services.com` (fetched 2026-10-22). Fiserv merchant alliance CONFIRMED, [8-K 2026-05-12](https://www.sec.gov/Archives/edgar/data/1212545/000162828026033850/wal_investordayx2026xfin.htm) (not core) | **Y:** zero-day in a third-party secure file-transfer tool, Oct 2024; data published; vendor not named, [10-K 2025-02-25](https://www.sec.gov/Archives/edgar/data/1212545/000121254525000090/wal-20241231.htm) | None disclosed |
| 2 | ZION | Fleet | **TCS BaNCS, CONFIRMED**: [8-K 2024-07-22](https://www.sec.gov/Archives/edgar/data/109380/000010938024000119/exh991earningsrelease20240.htm); [10-K 2026-02-24](https://www.sec.gov/Archives/edgar/data/109380/000010938026000046/zions-20251231.htm) ($221M capitalized) | UNKNOWN | None found | Completed Jul 2024 |
| 3 | OZK | Fleet + KRE | UNKNOWN. **Files periodic reports with the FDIC, not the SEC**; the 10-K was not retrieved. A "Fiserv Premier" job-skill mention is UNVERIFIED | UNVERIFIED: `uux.aspx` plus `onlineaccess1.com` script (fetched 2026-10-22) | Not determinable (no EDGAR 10-K) | — |
| 4 | FLG | Fleet | **REPORTED:** Fiserv DNA plus FIS today; selected **Fiserv Finxact**, [Banking Dive 2026-08-21](https://www.bankingdive.com/news/flagstar-bank-fiserv-finxact-cloud-native-core-tech-modernization/828477/) | Fiserv mobile/payments, REPORTED, [Banking Dive 2023-10-10](https://www.bankingdive.com/news/fiserv-moveit-victim-cyberattack-breach-flagstar-bank-fis/696141/) | **Y:** MOVEit **via Fiserv**, May 2023, **837,390 customers**; MDL stayed, [10-Q 2026-08-06](https://www.sec.gov/Archives/edgar/data/910073/000091007326000068/fbc-20260630.htm) | Finxact migrations summer 2027 and summer 2028 (REPORTED) |
| 5 | HBAN | Fleet | UNKNOWN. Job postings cite DXC Hogan (UNVERIFIED, undated) | UNKNOWN | **Y:** acquired **Cadence** hit by MOVEit, [8-K Ex. 99.1 2025-12-01](https://www.sec.gov/Archives/edgar/data/49196/000114036125043724/ny20057909x3_ex99-1.htm) | Cadence conversion completed mid-June 2026, [8-K 2026-07-23](https://www.sec.gov/Archives/edgar/data/49196/000004919626000060/hban20260630_8kex991.htm) |
| 6 | VLY | Fleet | UNKNOWN. Single core since Oct 2023; Leumi USA was on FIS (2016); an FIS job post is UNVERIFIED | UNVERIFIED: `onlineaccess1.com` script | **Y:** MOVEit via unnamed "third-party service providers", 2023, [10-K 2026-02-27](https://www.sec.gov/Archives/edgar/data/714310/000071431026000017/vly-20251231.htm) | Bluevine acquisition announced 2026-09-28, [8-K](https://www.sec.gov/Archives/edgar/data/714310/000119312526403391/d31493dex991.htm) |
| 7 | SSB | Fleet | UNKNOWN: risk factor ("core processing"), [10-K 2026-02-20](https://www.sec.gov/Archives/edgar/data/764038/000110465926017884/ssb-20251231x10k.htm) | UNKNOWN. nCino conference session 2025-05-20 (REPORTED link, modules not stated) | Own network, not vendor: **Item 1.05**, [8-K 2024-02-09](https://www.sec.gov/Archives/edgar/data/764038/000095010324002017/dp206600_8k.htm) | Independent Bank Group converted May 2025 |
| 8 | EGBN | Fleet | UNKNOWN: risk factor, [10-K 2026-03-09](https://www.sec.gov/Archives/edgar/data/1050441/000105044126000021/egbn-20251231.htm) | New platform launched early 2024; vendor UNKNOWN. Business hosts UNVERIFIED | None found | — |
| 9 | EWBC | KRE | **CONFIRMED (vendor-supplied list): FIS IBS.** "East West Bank" is listed among notable IBS clients in [Celent's NA edition reprinted by FIS, 2023-05-12](https://www.fisglobal.com/-/media/fisglobal/files/pdf/report/retail-banking-core-banking-systems-na-large-bank-edition-2023-fis-reprint.pdf). Not named in EWBC filings. *Cross-map merge; EastWest Bank Philippines (Temenos) is a different bank* | UNVERIFIED: FIS-domain deposit/RDC host (fetched 2026-10-22) | None. "Not experienced any known… material" incident, [10-K 2026-02-27](https://www.sec.gov/Archives/edgar/data/1069157/000106915726000009/ewbc-20251231.htm) | — |
| 10 | UCB | KRE | **Fiserv Premier, CONFIRMED 2013 (stale)**: [American Banker 2013](https://americanbanker.com/news/united-community-banks-renews-with-fiserv) | **Conflict:** Q2 REPORTED (undated) vs `uux.aspx` fingerprint UNVERIFIED | None material, [10-K 2026-02-17](https://www.sec.gov/Archives/edgar/data/857855/000085785526000008/ucbi-20251231.htm) | — |
| 11 | UBSI | KRE | **FIS, CONFIRMED 2011 (stale)**: 7-year term plus automatic renewals, [8-K 2011](https://www.sec.gov/Archives/edgar/data/729986/000119312511183622/d8k.htm) | UNVERIFIED: FIS login host (fetched 2026-10-22) | None, [10-K 2026-02-27](https://www.sec.gov/Archives/edgar/data/729986/000119312526081470/d90970d10k.htm) | Piedmont converted Q1 2025 |
| 12 | EBC | KRE | UNKNOWN: "outsourced core", [S-1 2020-06-18](https://www.sec.gov/Archives/edgar/data/1810546/000119312520172003/). FIS IBS job posts UNVERIFIED | **Backbase, CONFIRMED** (vendor PR [2022-11-07](https://www.backbase.com/press/backbase-announces-expanded-relationship-with-eastern-bank)), hosted on Microsoft cloud | Small Massachusetts breach-log entries Jan–Mar 2026, 17–50 people each (REPORTED) | HarborOne converted Feb 2026 |
| 13 | PNFP | KRE | **FIS (Synovus platform), CONFIRMED**: [8-K 2025-08-28](https://www.sec.gov/Archives/edgar/data/2082866/000114036125033036/ny20052516x3_ex99-1.htm). Legacy Pinnacle on Jack Henry ("largest single user"), [425 2025-09-10](https://www.sec.gov/Archives/edgar/data/2082866/000114036125034560/ef20055422_425.htm) | Q2 on the Synovus side, CONFIRMED ([Q2 PR 2021](https://www.q2.com/company/news/pr/synovus-banks-on-q2-to-deliver-innovative-digital-banking-services-faster)). Legacy Pinnacle UNKNOWN | None found | **Jack Henry → FIS, 1Q 2027, "on track"**, [8-K 2026-07-22](https://www.sec.gov/Archives/edgar/data/2082866/000208286626000075/) |
| 14 | FHB | KRE | **FIS IBS, CONFIRMED**: FIS PR 2019 (403; via [FinTech Futures 2019-05-06](https://www.fintechfutures.com/fintech/first-hawaiian-stays-with-fis-but-switches-core-systems)); conversion May 2022 per [DEF 14A 2023-03-16](https://www.sec.gov/Archives/edgar/data/36377/000110465923033344/) | FIS Digital One (2019 plan); MX Helios mobile ([2021](https://www.mx.com/news/first-hawaiian-bank-goes-live-with-mx-helios-for-mobile-banking-empowering-customers-with-financial-insights/)); 2025 app vendor UNKNOWN | None found | TriCo acquisition; TriCo is on Fiserv, platform decision pending, [425 2026-08-14](https://www.sec.gov/Archives/edgar/data/36377/000110465926097140/tm2620283d10_425.htm) |
| 15 | HOMB | KRE | UNKNOWN: risk factor, [10-K 2026-02-27](https://www.sec.gov/Archives/edgar/data/1331520/000133152026000051/homb-20251231.htm) | UNKNOWN. Newgen account opening REPORTED | **FIS** (customer-due-diligence vendor) misdirected a customer file 2026-08-07 (REPORTED, [Mass. AG notice](https://www.mass.gov/doc/2026-1555-centennial-bank-including-its-division-happy-state-bank/download)). 2023 network intrusion REPORTED; entity match unconfirmed | MCBI closed 2026-04-01; conversion date not found |
| 16 | FBP | KRE | FIS IT outsourcing CONFIRMED for 2013–2016 only ([10-K FY2015](https://www.sec.gov/Archives/edgar/data/1057706/000105770616000020/fbp12312015x10k.htm)). Current core UNKNOWN | UNKNOWN app. nCino lending CONFIRMED ([2024 PR](https://investor.ncino.com/news-releases/news-release-details/firstbank-puerto-rico-selects-ncino-transform-commercial-lending)) | **Y:** MIAC vendor ransomware 2023 (REPORTED, [JD Supra](https://www.jdsupra.com/legalnews/firstbank-puerto-rico-announces-data-2253411/)) | Core/mainframe cloud migration since 2023 |
| 17 | BPOP | KRE | **Evertec, CONFIRMED**: "our provider of core financial transaction processing and information technology services"; MSA ends **2028-09-30**, [10-K 2026-03-02](https://www.sec.gov/Archives/edgar/data/763901/000119312526085756/d17859d10k.htm) | **In-house**, CONFIRMED (bought from Evertec 2022), [8-K 2022-07-01](https://www.sec.gov/Archives/edgar/data/763901/000119312522186782/d335340d8k.htm) | **Y (×3):** MOVEit via a service provider, 2023. Evertec Fortinet zero-day 2024 "migrated to one of Popular's domain controllers due to a shared network environment". Evertec support-platform breach, [8.01 2026-06-09](https://www.sec.gov/Archives/edgar/data/763901/000119312526263044/d46942d8k.htm) | Service-by-service exit from Evertec before 2028-09-30 |
| 18 | WTFC | KRE | **FIS IBS, CONFIRMED (vendor-supplied list, 2023-05-12)**; [FIS client story](https://www.fisglobal.com/insights/fis-client-stories/wintrust) | NCR Digital First ([2020 PR](https://www.businesswire.com/news/home/20201202005953/en/Wintrust-Selects-NCR-Digital-First-Banking-Platform)); now Candescent (inferred, not confirmed) | None found | None found |
| 19 | FNB | KRE | **Fiserv Premier, CONFIRMED 2013 (stale)**: [425 2013-02-28](https://www.sec.gov/Archives/edgar/data/37808/000119312513084636/d494726d425.htm) | **In-house** eStore, CONFIRMED (bank releases 2025–26) | None, [10-K 2026-02-24](https://www.sec.gov/Archives/edgar/data/37808/000003780826000007/fnb-20251231.htm) | None found |
| 20 | COLB | KRE | UNKNOWN current ("Umpqua technology environment"). Fiserv Premier ~2009, REPORTED historical | **Q2 mobile plus FIS D1B business, CONFIRMED**, [8-K 2023-03-01](https://www.sec.gov/Archives/edgar/data/887343/000119312523056342/d413616dex102.htm) | **Y:** MOVEit via a technology service provider, **~429,000 customers**, [10-K 2026-02-26](https://www.sec.gov/Archives/edgar/data/887343/000088734326000088/colb-20251231.htm). Maine AG filing submitted by FIS's counsel (REPORTED) | Pacific Premier converted Q1 2026 |
| 21 | AUB | KRE | **FIS, CONFIRMED**: [8-K 2024-05-07](https://www.sec.gov/Archives/edgar/data/883948/000088394824000050/aub-20240507xex99d1.htm). "Continue to reduce reliance on one core vendor", [8-K 2025-12-10](https://www.sec.gov/Archives/edgar/data/883948/000088394825000114/aub-20251210xex99d1.htm) | **Q2, CONFIRMED** (8-K 2025-12-10) | None found | Sandy Spring consolidated late 2025 |
| 22 | GBCI | KRE | **Jack Henry, CONFIRMED 2021 (stale)**: [8-K 2021-05-18](https://www.sec.gov/Archives/edgar/data/868671/000086867121000057/projectelevateinvestorpr.htm) | UNKNOWN | None found | Bank of Idaho Q3 2025; Guaranty Q1 2026 (vendor not stated) |

**Core-vendor tally (22 banks):**

| Evidence state | Banks | Count |
|---|---|---|
| Named in a 2024–2026 primary document | ZION (TCS), PNFP (FIS), AUB (FIS), BPOP (Evertec) | **4** |
| Named in a 2023 document (vendor-supplied list or bank proxy) | WTFC (FIS IBS), EWBC (FIS IBS), FHB (FIS IBS) | 3 |
| CONFIRMED but stale (2011–2021) | UBSI (FIS 2011), UCB (Fiserv 2013), FNB (Fiserv 2013), GBCI (Jack Henry 2021) | 4 |
| REPORTED (trade press, current) | FLG (Fiserv DNA plus FIS → Finxact) | 1 |
| Historical only; current UNKNOWN | FBP (FIS 2013–16), COLB (Fiserv ~2009) | 2 |
| UNKNOWN (leads, if any, UNVERIFIED) | WAL, OZK, SSB, EGBN, HOMB, HBAN, VLY, EBC | 8 |

FIS is the most frequently named core: CONFIRMED at PNFP, AUB, WTFC, EWBC and FHB, stale at UBSI. Three of the 22 (PNFP via Synovus, WTFC and EWBC) appear on the same FIS IBS notable-client list. Counting non-core roles too (any vintage, CONFIRMED or REPORTED), FIS is named at 9 of 22 banks. Fiserv is named at 7 of 22, but several of those rest only on 2007–2015 documents. Digital-platform vendors are named for fewer banks than core vendors are. Q2 is the most common (PNFP/Synovus, COLB, AUB, and UCB REPORTED), and two banks run in-house platforms (BPOP, FNB). Homepage login-host patterns suggest one shared retail digital platform across WAL, OZK and UCB (`uux.aspx`), with VLY loading the same script domain. The vendor behind that domain is not established (the registrant is redacted). **This is an UNVERIFIED concentration lead, not a finding.**

Several large core changes are scheduled or under way: PNFP (Jack Henry → FIS, 1Q 2027), FLG (Finxact, 2027–2028), BPOP (Evertec exit by 2028-09-30), and FHB/TriCo (platform decision pending). This is relevant as an inference only: the one bank IT event with measured customer attrition, TSB 2018, was a migration failure (Table 5).

### (3) Correlated-incident base rate: one vendor, many institutions, 2023–2026

**The 13 rows below are what this run found, not a census.** Searches beyond these vendors (FIS/Worldpay, Deluxe, Temenos, Cenlar) were not done in depth. Stock moves were computed from yfinance adjusted closes (run 2026-10-22), measured from the last close before the event against a named benchmark. They are uncontrolled event windows with no factor model.

| # | Date | Vendor | Type | Institutions affected | Duration | Money effect | Source |
|---|---|---|---|---|---|---|---|
| 1 | 2023-11-24 | Trellance / FedComp core (Ongoing Operations) | Ransomware | ~60 credit unions | ~17–19 days to core restoration (12/13) | No deposit data; all unlisted | [NEWS: The Record](https://therecord.media/credit-unions-facing-outages-due-to-ransomware); [NEWS: CU Times 2023-12-18](https://cutimes.com/2023/12/18/back-online-but-not-out-of-the-woods-cu-ransomware-update) |
| 2 | 2023-05-27 | Progress MOVEit (Cl0p) | Supply-chain data theft | Many FIs, directly or via vendors: Flagstar via Fiserv (837,390), FISC (753,261), Schwab/TDA, others; >2,100 organizations across all sectors | Data theft, no outage | No access lost; vendor PRGS −3.2% at +20 days vs SPY +6.5%, +2.9% at +60 days | [NEWS: Banking Dive](https://www.bankingdive.com/news/fiserv-moveit-victim-cyberattack-breach-flagstar-bank-fis/696141/); [NEWS: American Banker](https://americanbanker.com/creditunions/news/15-banks-credit-unions-confirm-moveit-data-breaches) |
| 3 | 2023-01-31 | ION Trading UK | Ransomware | 42 clients (derivatives clearing) | ~1 week | Institutional only; CFTC report delayed; Treasury: "not… systemic" | [NEWS: Kitco/Reuters 2023-02-07](https://www.kitco.com/news/off-the-wire/2023-02-07/update-1-ion-brings-clients-back-online-after-ransomware-attack-source) |
| 4 | 2024-02 to 05 | Evolve Bank & Trust (BaaS sponsor) | Ransomware / breach | 1 bank, customers of many fintechs; 7,640,112 individuals | Data theft | **Evolve deposits rose**: $1,142.7M (2024-06-30) → $1,331.0M (2024-12-31) | [NEWS: SecurityWeek](https://www.securityweek.com/evolve-bank-data-breach-impacts-7-6-million-people/); FDIC BankFind cert 1299 [PRIMARY data] |
| 5 | 2024-04-22 | Synapse (BaaS ledger) | Ledger failure, not cyber | 4 partner banks, >100,000 end-user accounts | Months; part >16 months | **End users lost access; $65–96M shortfall estimates.** Not a bank run; the gap was in FBO accounts | [NEWS: CNBC via NBC NY](https://www.nbcnewyork.com/news/business/money-report/synapse-bankruptcy-trustee-says-85-million-of-customer-savings-is-missing-in-fintech-meltdown/5487272/); [NEWS: Banking Dive 2025-08-27](https://www.bankingdive.com/news/cfpb-sues-synapse-plans-use-victims-fund-pay-end-users/758776/) |
| 6 | 2024-07-19 | CrowdStrike Falcon update | Outage, not cyber | Global; named banks are non-US (TD, Capitec, Bahamas) | Hours to ~1 day | Bank stocks: no documented move. **Vendor CRWD: −11.1% day 1, low −36.5% within 60 days, later new highs** | [PRIMARY: Central Bank of Bahamas](https://centralbankbahamas.com/news/public-notices/global-crowdstrike-outage-has-minimal-impact-on-retail-banking-services); [NEWS: Bloomberg](https://www.bloomberg.com/news/articles/2024-07-19/capitec-of-south-africa-says-its-systems-hit-by-global-outage) |
| 7 | 2024-07-31 | C-Edge (India) | Ransomware | ~300 small banks (~0.5% of India's payments) | Days (isolated by NPCI) | None documented | [NEWS: Globe and Mail/Reuters](https://www.theglobeandmail.com/business/article-ransomware-attack-forces-hundreds-of-small-indian-banks-offline) |
| 8 | 2024-11-07 | Finastra file-transfer platform | Breach | Affected banks never named | No outage | None documented | [NEWS: CSO Online](https://www.csoonline.com/article/3610267/finastra-investigates-breach-potentially-affecting-top-global-banks.html) |
| 9 | 2025-01-15 | FIS facility (power/hardware) | Outage, not cyber | ">two dozen banks" incl. Capital One, BOKF | ~4–5 days (Capital One) | COF +3.2%, BOKF +1.6% on day 1 (KBE +2.6%). **No negative move** | [NEWS: Banking Dive](https://www.bankingdive.com/news/capital-one-outage-fis-bank-of-oklahoma-citi/737847/) |
| 10 | 2025-05-02 | Fiserv (Zelle/online banking) | Outage, "not malicious" | "Multiple banks" (BofA statement) | Same day plus backlog | FISV +0.7% on day 1 | [NEWS: WBAY/CNN](https://www.wbay.com/2025/05/02/zelle-is-down-some-bank-customers/) |
| 11 | 2026-08-31 | Jack Henry | Breach (vishing) | PII of <10 clients; 7,200+ notified | Contained; non-production | JKHY −1.1% on day 1; −9.3% by 10/21, **in line with peers** (FIS −11.1%, FISV −9.3%, GPN −8.8%, KBE −5.5% from 8/28) | [NEWS: Banking Exchange](https://www.bankingexchange.com/news-feed/item/10680-jack-henry-cyberattack-compromises-client-data) |
| 12 | 2026-09-15 | Sharetec (core processor) | Outage (cooling failure) | 23 credit unions, ~$2.56B assets | Days; restoration date not reported | Not reported; unlisted | [NEWS: American Banker 2026-09-21](https://www.americanbanker.com/news/overheated-data-center-knocked-23-credit-unions-offline) |
| 13 | 2026-10-14/15 | ConnectWise Cloud Backup; Storm-0940 using "ARTEX" | Supply-chain compromise (IT tool) | >2,250 tenants targeted; 173 confirmed (Huntress, ~10/17); **no bank named** | Ongoing | None reported | [PRIMARY: Microsoft 2026-10-21](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) |

Three patterns stand out:
- **The type of incident decides whether money is involved at all.** Only the core and payment outages (#1, #7, #9, #10, #12) cut customers off from their money. The breaches (#2, #4, #8, #11, #13) exposed data and stopped no one's access.
- **Multi-institution core or payment outages recur about once a year:** Trellance 2023, FIS Jan 2025, Fiserv May 2025, Sharetec Sep 2026.
- **The long outages (2–3 weeks) hit small, unlisted credit unions,** so stock data cannot test the question where outages last longest. Outages at large banks lasted hours to about 5 days.

**Correlated hits through vendors are real at the data-breach level within the 22-bank set.** MOVEit 2023 reached FLG (via Fiserv, 837,390 customers), VLY, Cadence (now HBAN), COLB (~429,000; via FIS) and BPOP, each through a third party. BPOP's processor Evertec is a second, repeating channel. A 2024 Fortinet zero-day crossed into a Popular domain controller "due to a shared network environment". On 2026-06-09 Evertec and Popular filed Item 8.01 8-Ks on the same day for a support-platform breach that exposed debit card numbers; Popular has a contractual indemnity right [PRIMARY: [Evertec 8-K](https://www.sec.gov/Archives/edgar/data/1559865/000155986526000039/evtc-20260609.htm); [Popular 8-K](https://www.sec.gov/Archives/edgar/data/763901/000119312526263044/d46942d8k.htm)]. **These were data exposures. None cut off customer access to accounts.**

### (3b) SEC 8-K cyber filings by banks and bank-tech vendors, 2023-12-18 to 2026-10-22, with denominator

**Item 1.05 ("Material Cybersecurity Incidents"): 4 banks filed 9 filings (4 original 8-Ks plus 5 amendments).** Two independent EDGAR methods returned the same 9 accession numbers [PRIMARY].

| Bank | Ticker | Original filing | Amendments | What happened (filer's words, condensed) | Channel | Customer access lost? |
|---|---|---|---|---|---|---|
| SouthState | SSB | [2024-02-09](https://www.sec.gov/Archives/edgar/data/764038/000095010324002017/dp206600_8k.htm) | 1 ([2024-03-29](https://www.sec.gov/Archives/edgar/data/764038/000155837024004390/ssb-20240206x8ka.htm)) | Isolated network segments; "some disruption" and later "significant impact on certain… business processes"; not material | Own network | No customer outage described; business processes disrupted |
| BayFirst | BAFN | [2025-10-30](https://www.sec.gov/Archives/edgar/data/1649739/000164973925000246/bafn-20251028.htm) | 0 | Marketing-services vendor exposed name, DOB, SSN/TIN | **Vendor** | No |
| CB Financial | CBFV | [2026-05-11](https://www.sec.gov/Archives/edgar/data/1605301/000160530126000021/cbfv-20260507.htm) | 0 | Customer data handled with an "unauthorized artificial intelligence-based software application"; material "due to the volume and sensitive nature" of the data | **Unauthorized AI app** (internal) | No ("customer access to accounts" not disrupted) |
| River Financial | RVRF | [2026-06-25](https://www.sec.gov/Archives/edgar/data/1641601/000119312526282946/ck0001641601-20260619.htm) | 4 (2026-07-06, 07-10, 07-17, 07-30) | Ransomware across "portions of its server environment"; data removed; 4 class actions; materiality still undetermined as of the last amendment | Own network | "Certain operations have been impacted" |

**Item 8.01 cyber filings by banks: 7 filings by 7 banks, a lower bound because the search depends on wording. 5 of the 7 came through a vendor or third party.** They are Middlefield 2023-12-21 (own systems), Santander Holdings USA 2024-05-14 (hosting provider), MainStreet 2025-05-30 (an "outside vendor to the core bank", ~4.65% of customers), Heritage Financial 2026-03-23 (own server), Orrstown 2026-05-29 (an unnamed vendor serving many clients), Popular 2026-06-09 (Evertec) and SR Bancorp 2026-07-10 (audit firm Mercadien) [PRIMARY: accessions in References]. Across both items, **11 banks** filed a cyber-incident 8-K in the window. 2026 year-to-date has 6 bank filers, against 4 in 2024 and 2025 combined. The numbers are too small to call this a rate, but the direction is up.

| Denominator / context | Value | Source |
|---|---|---|
| Bank/thrift-SIC SEC filers with a 10-K or 10-Q in the window | **~451** (382 with a ticker) | [PRIMARY: EDGAR submissions API, pulled 2026-10-22](https://data.sec.gov/submissions/) |
| FDIC-insured institutions | **4,238** (3,818 community banks), Q2 2026 | [NEWS: ABA Banking Journal on the FDIC QBP, 2026-08](https://bankingjournal.aba.com/2026/08/quarterly-banking-profile-banking-net-income-90-1b-in-q2-2026/) |
| Coverage | **EDGAR sees roughly a tenth of banks by count** (more by assets). Most community banks and all credit unions are invisible to this count; Patelco, Evolve and Trellance's credit unions are absent by construction | Inference from the two rows above |
| Bank Item 1.05 rate | 4 / (451 × 2.85 years) ≈ **0.3% per bank-year**; a floor, because Item 1.05 captures only what management calls material | Computed |
| All-market Item 1.05 | 85 filings from 58 companies; banks are 4 of the 58 companies (6.9%) | [PRIMARY: EDGAR FTS sweep](https://efts.sec.gov/LATEST/search-index?q=%22Item%201.05%22&forms=8-K&dateRange=custom&startdt=2023-12-18&enddt=2026-10-22) |
| Core/digital vendors' cyber 8-Ks (Fiserv, FIS, Jack Henry, Q2, Alkami, nCino, NCR Voyix; also ACI, Blend) | **None filed under Item 1.05 or 8.01.** Jack Henry's 2026-08-31 incident was disclosed by press release only | [PRIMARY: data.sec.gov submissions per vendor CIK](https://data.sec.gov/submissions/) |
| Vendor 8.01s found | Evertec only: 2025-09-02 (Sinqia, Brazil Pix: ~R$710M of unauthorized transactions at 2 FI clients) and 2026-06-09 (Puerto Rico FI clients' data) | [PRIMARY: Evertec 8-K 2025-09-02](https://www.sec.gov/Archives/edgar/data/1559865/000155986525000043/evtc-20250829.htm) |
| Separate confidential channel | Since 2022, banks must notify their primary federal regulator within **36 hours** of a qualifying computer-security incident, and bank service providers must notify their bank clients. These notices never reach EDGAR | [PRIMARY: rule described in PNFP 8.01 exhibit 2026-03-02](https://www.sec.gov/Archives/edgar/data/2082866/000208286626000020/pnfp-20260302_d2.htm) |

Bank-adjacent and outside the count: the Federal Home Loan Bank of New York (SIC 6111) filed an Item 1.05 on 2024-03-01. Someone attempted fraudulent fund transfers after a "fourth-party vendor (i.e., a vendor of a Bank vendor)" was compromised; no money moved [PRIMARY: [FHLBNY 8-K](https://www.sec.gov/Archives/edgar/data/1329842/000165495424002505/fhlbny_8k.htm)].

**Reproduction recipe:**
- (a) Query EDGAR full-text search for 8-K forms with `dateRange=custom&startdt=2023-12-18&enddt=2026-10-22`. Use the terms "Item 1.05", "cybersecurity" and "incident" in monthly slices, and keep hits whose `_source.items` contains "1.05".
- (b) Cross-check: list CIKs by SIC 6021/6022/6029/6035/6036 via `browse-edgar?action=getcompany&SIC=<code>`, then filter the 8-K item lists in `data.sec.gov/submissions/CIK##########.json` (including the paginated `files[]`) from 2023-12-18.
- (c) For Item 8.01: sweep 23 incident phrases (for example "cybersecurity incident", "threat actor", "unauthorized access", ransomware) over bank-SIC 8-Ks tagged 8.01 or 7.01 without 1.05, then screen each candidate by hand to exclude boilerplate.

### (4) Regulatory timeline: AI-agent access, Section 1033, vendor supervision

| Date | Event | Source |
|---|---|---|
| Since 2001 | NCUA has no examination authority over credit-union vendors | [NEWS: American Banker 2026-09-21](https://www.americanbanker.com/news/overheated-data-center-knocked-23-credit-unions-offline) |
| 2023-12-18 | SEC Item 1.05 effective; smaller reporting companies from 2024-06-15 | [PRIMARY: SEC Release 33-11216](https://www.sec.gov/files/rules/final/2023/33-11216.pdf) |
| 2024-10-22 | CFPB Section 1033 final rule (89 FR 90838, published 2024-11-18): bars screen scraping as a way of meeting the interface duty; bars fees. **Forcht Bank / KBA / BPI sue the same day** (E.D. Ky. 5:24-cv-00304) | [PRIMARY: Federal Register](https://www.federalregister.gov/documents/2024/11/18/2024-25079/required-rulemaking-on-personal-financial-data-rights) |
| 2025-05-23 | CFPB tells the court the rule "is unlawful and should be set aside" | [PRIMARY: ECF 57](https://infobytes.orrick.com/wp-content/uploads/DEFENDANTS-STATUS-REPORT-1.pdf) |
| Aug 2025 | FDIC OIG: 16 SSPs examined 2020–23 (9 every year); "unable to conclude on the program's effectiveness"; vendor selection "highly subjective, poorly documented" | [PRIMARY: FDIC OIG MEMO-25-03](https://www.fdicoig.gov/sites/default/files/reports/2025-08/Significant%20Service%20Provider%20Examination%20Program%20Final%20Memo%20-%20Memo-25-03_0_0.pdf) |
| 2025-08-22 | 1033 reconsideration ANPR (90 FR 40986) | [PRIMARY: consumerfinance.gov](https://www.consumerfinance.gov/rules-policy/rules-under-development/personal-financial-data-rights-reconsideration/) |
| **2025-10-29** | **Preliminary injunction**: CFPB enjoined from enforcing the rule until reconsideration is complete | [INSTITUTIONAL: ABA Banking Journal 2025-11-03](https://bankingjournal.aba.com/2025/11/kentucky-federal-court-enjoins-cfpb-from-enforcing-current-1033-final-rule/) |
| 2025-12-10 | Court orders notice within 5 days of any interim final rule | [PRIMARY: ECF 93](https://storage.courtlistener.com/recap/gov.uscourts.kyed.106299/gov.uscourts.kyed.106299.93.0.pdf) |
| 2026-04-01 | Tier-1 compliance date passes "not as a binding enforcement trigger" | [INSTITUTIONAL: Cozen O'Connor](https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration) |
| 2026-04-17 | OCC Bulletin 2026-13 (model risk): "Generative AI and agentic AI models… are not within the scope of this guidance"; an AI RFI is promised. **No RFI published as of mid-October** | [PRIMARY: OCC](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) |
| ~2026-08-06 | CFPB 1033 rewrite submitted to OIRA. **Not published as of 2026-10-22** | [INSTITUTIONAL: Ballard Spahr](https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/) |
| 2026-09-11 | FRB/FDIC/NCUA/OCC propose replacing the June 2023 third-party guidance (Federal Register 2026-09-15; **comments due 2026-11-16**). Joint Statement on core providers: some core providers "may qualify as institution-affiliated parties"; no new contract terms | [INSTITUTIONAL: Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/09/federal-banking-agencies-issue-proposed-updates-to-interagency-third-party-risk-management-guidance-and-joint-statement-on-core-service-providers) |
| 2026-10-13 → 10-22 | JPMorgan, Schwab, Citi and BofA state agent restrictions (see 4a); Axios report; OCC's Gould: banks "all over this for months" and declined twice to say whether customers would be made whole | [NEWS: American Banker 2026-10-22](https://www.americanbanker.com/news/gould-banks-preparing-for-rogue-ai-agents-for-months) |

**1033 original compliance tiers (now enjoined)** [INSTITUTIONAL: [Cooley 2024-10-31](https://www.cooley.com/news/insight/2024/2024-10-31-cfpb-finalizes-section-1033-rule-on-personal-financial-data-rights)]:

| Date | Depository institutions |
|---|---|
| 2026-04-01 | ≥$250B |
| 2027-04-01 | $10B to <$250B |
| 2028-04-01 | $3B to <$10B |
| 2029-04-01 | $1.5B to <$3B |
| 2030-04-01 | >$850M to <$1.5B |
| Exempt | ≤$850M |

**(4a) What the record actually contains on AI specifically.** Four kinds of item exist, and none of them is an AI-agent loss at a bank.

| Item | Date | What it is | Bank-level money effect | Source |
|---|---|---|---|---|
| Big-bank restrictions on outside agents | 2026-10-13 to 10-19 | JPMorgan CFO Barnum: credential access "not secure… we are blocking them". On losses: if a customer gives credentials to an agent, "that's going to be on them". Citi: does "not permit third-party AI agents… to log into a customer's account"; read-only via approved providers continues. BofA's Moynihan: "a human in the loop to authorise money moving". Schwab's Wurster: "blocking unauthorized agents"; no outside-agent money movement | **No losses reported anywhere** | [NEWS: American Banker 2026-10-13](https://www.americanbanker.com/news/jpmorgan-warns-of-risks-to-consumers-who-rely-on-ai-agents); [NEWS: RBI/FT via Yahoo 2026-10-19](https://finance.yahoo.com/news/us-banks-limit-ai-agents-113229223.html) |
| Regional banks | to 2026-10-22 | **No regional bank has said anything about blocking outside agents.** PNC (2026-09-14) spoke only about controlling its own agents | n/a | [NEWS: American Banker 2026-09-14](https://www.americanbanker.com/news/bofa-and-pnc-respond-to-rising-ai-fears) |
| AI-enabled supply-chain attack | 2026-10-14 → 10-21 | Storm-0940 / ARTEX against ConnectWise (an IT tool, not banking) | No bank named | Intake checks |
| Unsanctioned AI app as a leak channel | 2026-05-05 | CBFV Item 1.05 (single bank, PII) | No access lost | Table 3b |

**Loss allocation.** Reg E 12 CFR 1005.2(m)(1) excludes from "unauthorized" any transfer by "a person who was furnished the access device… by the consumer" until the consumer notifies the bank. Comment 2(m)-2 makes the consumer "fully liable" when that person exceeds the authority given. Read literally, this puts losses from agent overreach on the consumer until notice. Comment 2(m)-3 cuts the other way where credentials were obtained "through fraud". **No CFPB interpretation addresses AI agents**, and wires sit outside Reg E (1005.3(c)(3)) [PRIMARY: [eCFR Part 1005](https://www.ecfr.gov/current/title-12/chapter-X/part-1005)]. On small-bank API readiness, a vendor-sponsored survey (American Banker/Akoya, n=218, fielded Oct 2025) found **no APIs offered at 11% of community banks, 12% of credit unions and 2% of national banks**. API-only shares were 25%, 20% and 43% [INSTITUTIONAL, sponsor-biased: [American Banker](https://www.americanbanker.com/payments/news/exclusive-research-banks-approach-an-open-finance-shift)]. Where no API exists, outside access runs through credentials and screen scraping, the channel the large banks are now blocking. Whether a small bank can detect such logins depends on its digital-banking vendor, and no vendor statement on this was found (inference).

### (5) Transmission to money: deposits and stock

**No documented pure IT or cyber event has caused a deposit run.** The IMF (2024-04-09) states that "no significant 'cyber runs' have occurred thus far", while "modest and somewhat persistent deposit outflows have occurred at smaller US banks after a cyberattack" [INSTITUTIONAL: [IMF blog](https://www.imf.org/en/blogs/articles/2024/04/09/rising-cyber-threats-pose-serious-concerns-for-financial-stability)].

| Event | Scope | Deposit effect (basis, as-of) | Bank stock effect (computed 2026-10-22; uncontrolled) | Source |
|---|---|---|---|---|
| Patelco CU ransomware, 2024-06-29 | Single institution, $9.6B; ~17 days down | Shares **$8.064B → $7.849B (−2.7%)** in Q3 2024 vs **+0.4% for all CUs**; **$8.105B by 2025-03-31, above pre-attack**. Uninsured shares −7.8%, then recovered. Q3 net income −$39.2M | n/a (CU) | NCUA call reports, CU 68579 [PRIMARY data]; [PRIMARY: DFPI](https://dfpi.ca.gov/press_release/dfpi-takes-action-against-patelco-credit-union-for-cybersecurity-violations/) |
| Evolve breach, 2024 | 1 bank, 7.6M people | **Rose:** +3.3% QoQ, +16.5% over 2 quarters after disclosure | n/a (private) | FDIC BankFind cert 1299 [PRIMARY data] |
| Capital One cloud breach, 2019 | ~106M people | COF NA deposits **+1.6%** in the breach quarter ($249.4B → $253.4B) | −5.9% day 1 (−6.8pp vs KBE); −3.8% at +60 days (−4.3pp vs KBE); overlaps the Aug-2019 selloff | FDIC cert 4297 [PRIMARY data]; [NEWS-legal: Cleary](https://www.clearygottlieb.com/news-and-insights/publication-listing/occ-imposes-80-million-penalty-in-connection-with-bank-data-breach) |
| TSB migration failure, 2018 | Up to 1.9M locked out; weeks to months | Deposits **−4.7%** to £29.1bn for the year, which TSB attributes to a **planned ISA rate cut** (confounded). ~80,000 switched away vs ~50,000 in 2017; ~140,000 joined | Parent SAB.MC −17.7% at +60 days, confounded by the May-2018 euro-bank selloff | [PRIMARY: TSB FY2018 results](https://www.tsb.co.uk/news-releases/tsb-announces-2018-full-year-results/) |
| RBS/NatWest batch failure, 2012 | 6.5M customers | Not found | −16.6% at +5 days, +12.7% at +60 days; confounded by the Moody's downgrade and the Libor fine | [NEWS: Gulf News](https://gulfnews.com/amp/story/business%2Fbanking%2Frbs-fined-56m-for-it-meltdown-1.1415510) |
| FIS outage, Jan 2025 | >2 dozen banks, ~4–5 days | Not checked | COF +3.2%, BOKF +1.6% day 1; no negative move | Table 3 |
| Jack Henry breach, Aug 2026 | Vendor | n/a | JKHY in line with FIS/FISV/GPN; a sector move | Table 3 |
| Vendors: CRWD 2024 / EFX 2017 (reference) | Vendor | n/a | CRWD low −36.5%, later new highs; EFX −20.3% at +60 days (−27.8pp excess) | yfinance [computed] |
| Academic: small US banks, 2005–2017 breaches | Branch level | Deposit growth at affected branches **>20pp lower** than controls; deposits move to the largest unaffected local banks | n/a | [ACADEMIC: Gogolin, Lim & Vallascas](https://www.communitybanking.org/~/media/files/communitybanking/2020/gogolin%20et%20al%202020%20cyberattacks%20on%20small%20banks30092020.pdf) |

**Lasting stock damage fell on vendors (CrowdStrike, Equifax), not banks.** The incidents that did move money share four features. Customers lost access for days to weeks, not hours. The failure was traceable to one named institution. A credible alternative bank was close at hand. Some claims were uninsured: Patelco's uninsured shares fell 7.8% against 2.7% for total shares, and Synapse's FBO end users are the only group that took a lasting loss. **Vendor-wide outages so far fail the first two tests.** They have been short for large banks, and they spread the blame across many institutions. **There is no precedent for a multi-week outage at a large commercial bank heavy in uninsured deposits; the base rate is silent on that scenario.** Reproduction: FDIC BankFind `api.fdic.gov/banks/financials` (field DEP, by CERT); NCUA call-report zips (`ncua.gov/files/publications/analysis/call-report-data-YYYY-MM.zip`, FS220 ACCT_018); yfinance adjusted closes from the last pre-event close.

## Counter-Evidence

**Against the view that concentration creates correlated bank risk:**
- **No confirmed multi-bank core compromise exists.** The nearest event (Jack Henry, 2026) touched fewer than 10 clients in a non-production environment.
- **Large-bank vendor outages are short.** FIS 2025 lasted ~4–5 days and Fiserv 2025 a single day, and neither moved affected bank stocks.
- **Measured deposit effects are small and reversed.** Patelco recovered within ~3 quarters, and Evolve's and Capital One's deposits rose after their breaches.
- **Some concentration is falling.** Fiserv's credit-union share fell 118 bp to mid-2025, and AUB's own decks state an intent to "reduce reliance on one core vendor".
- **The largest vendors are examined federally.** Fiserv calls itself an SSP and FIS falls under MDPS, both examined annually.
- **The AI-agent problem on record sits at G-SIBs and brokers.** Those firms are the best resourced to block it, and Morgan Stanley denies seeing rogue agents.

**Against the reassuring reading:**
- **The supervisory backstop is unmeasured.** The FDIC OIG could not conclude whether the SSP program works, and NCUA has no vendor-exam authority.
- **The longest outages hit unlisted institutions** whose deposits cannot be observed at useful frequency.
- **Attrition is real even without runs.** Gogolin et al. find slow drag: more than 20pp lower deposit growth at affected branches.
- **Vendor-channel disclosures are rising in 2026** (3 of 4 bank 8.01s).
- **Shared networks have carried an intrusion across the vendor–bank boundary** (Evertec → Popular, 2024).

**On "older software at regional banks":**
- The evidence is mixed. Small institutions lag on APIs (11–12% offer none, against 2% of national banks), which leaves credential scraping as the access route.
- However, the cores at most such banks are vendor-run. "Older software" is then largely the vendors' software, so exposure is common to a vendor's clients rather than specific to a bank (inference).
- Several of the 22 run modern or in-house platforms: ZION (TCS BaNCS, 2024), FLG (moving to cloud-native Finxact), BPOP and FNB (in-house digital).

## Unknowns

- **Current core vendor at 8 of 22 banks:** WAL, OZK, SSB, EGBN, HOMB, HBAN, VLY and EBC. **Current status at 4 stale-CONFIRMED banks:** UBSI, UCB, FNB and GBCI.
- **Digital-platform vendor at most banks.** The vendor behind the shared `uux.aspx` / `onlineaccess1.com` pattern (WAL, OZK, UCB, VLY) is also unknown.
- **Vendor share by assets, and by tier ($10–100B, >$100B), for any vendor class.**
- **The SSP/MDPS roster.** It is non-public, so the provider with "more than 4,200" bank clients is unnamed.
- **Deposit behaviour at the ~60 Trellance and 23 Sharetec credit unions.** The institutions are unnamed, so no call-report test was possible.
- **AI-agent traffic and losses by bank size; customer AI-agent adoption by bank size.** No data exists.
- **The text, thresholds and timing of the 1033 rewrite** (at OIRA since ~2026-08-06).
- **Any CFPB position on AI agents under Reg E.**
- **Confidential 36-hour regulator notices.** These are the only complete incident record for the ~90% of banks outside EDGAR, and they are not public.
- **Final materiality decision for River Financial.** No amendment has been filed since 2026-07-30.

## Source Quality Assessment

- **Strongest:**
  - SEC filings, read in full through EDGAR: the 8-K counts, vendor 10-Ks and bank 10-K/8-K vendor naming.
  - Regulator data: FDIC BankFind, NCUA call reports, the FDIC OIG memo and OCC bulletins.
  - Rule text: eCFR and the Federal Register.
  - Court dockets.
- **Market share:**
  - The KC Fed figures are a Fed publication relaying an ABA *survey sample* of 2022 data.
  - The FI Navigator digital figures are secondary; the vendor-level infographics were not read.
  - The Fiserv ">3,500 FIs" figure is unverified (deck 403).
- **Bank map:**
  - Cells marked CONFIRMED are primary, but four rest on 2011–2021 documents.
  - Two rest on a vendor-supplied client list (Celent 2023, reprinted by FIS), which carries sponsor bias.
  - The EWBC cell is a cross-map merge, made because a North-America-edition list names "East West Bank".
  - Login-host and job-posting observations are UNVERIFIED leads.
- **AI-agent channel:**
  - The on-record quotes come via American Banker, Fortune and RBI/FT. They were not checked against earnings transcripts, because Quartr was unavailable.
  - The Axios original was 403. Its alarming content is anonymous, and Reuters could not verify it.
- **Base rate:**
  - The incident facts are mostly NEWS-tier.
  - The deposit and stock figures were computed by DEWEY from primary data. They are uncontrolled event windows.
  - The 13-incident list is not a census.

## References

All accessed 2026-10-22 unless noted.

**Vendor share and supervision**
- KC Fed, "Market Structure of Core Banking Services Providers", 2024-03-27 — https://www.kansascityfed.org/research/payments-system-research-briefings/market-structure-of-core-banking-services-providers/
- Jack Henry 10-K FY2026 (acc 0000779152-26-000067) — https://www.sec.gov/Archives/edgar/data/0000779152/000077915226000067/jkhy-20260630.htm
- Fiserv 10-K FY2025, filed 2026-02-19 — https://www.sec.gov/Archives/edgar/data/798354/000079835426000009/
- FIS 10-K FY2025, filed 2026-02-24 — https://www.sec.gov/Archives/edgar/data/1136893/000113689326000013/
- Q2 Holdings 10-K FY2025, filed 2026-02-11 — https://www.sec.gov/Archives/edgar/data/1410384/000141038426000006/
- Q2 Q2-2026 results release, 2026-07-29 — https://www.businesswire.com/news/home/20260729254821/en/
- Alkami 10-K FY2025, filed 2026-02-26 — https://www.sec.gov/Archives/edgar/data/1529274/000152927426000009/
- Callahan, "Top 20 Cores for Credit Unions", 2025-12-01 — https://creditunions.com/blogs/leaders-of-the-pack-the-top-20-cores-for-credit-unions/
- CCG Catalyst, digital banking landscape, 2026-10-07 — https://www.ccgcatalyst.com/thought-leadership/research-snapshot/sector-spotlight-digital-banking-landscape/
- William Mills / FI Navigator CU mobile share, 2026-09-01 — https://www.williammills.com/news/u.s.-credit-union-mobile-banking-market-share-report-published-by-william-mills-agency-and-fi-navigator
- Fiserv Investor Day notes (secondary), 2026-05 — https://bobhammel.substack.com/p/fiserv-investor-day-notes
- IT Brief, Candescent, Sept 2026 — https://itbrief.co.uk/story/candescent-expands-google-cloud-ai-tie-up-for-banks
- Payment Expert, JPMorgan data-access fees, 2025-11-17 — https://paymentexpert.com/2025/11/17/jpmorgan-chase-to-charge-fintechs-for-customer-data-access/
- FDIC OIG MEMO-25-03, Aug 2025 — https://www.fdicoig.gov/sites/default/files/reports/2025-08/Significant%20Service%20Provider%20Examination%20Program%20Final%20Memo%20-%20Memo-25-03_0_0.pdf
- Mayer Brown, TPRM proposal and Joint Statement, Sept 2026 — https://www.mayerbrown.com/en/insights/publications/2026/09/federal-banking-agencies-issue-proposed-updates-to-interagency-third-party-risk-management-guidance-and-joint-statement-on-core-service-providers
- Troutman, Joint Statement on core providers, Sept 2026 — https://www.troutmanfinancialservices.com/2026/09/federal-banking-agencies-issue-joint-statement-on-community-banks-engagement-with-core-service-providers/
- SSGA KRE daily holdings file (as of 2026-10-21) — https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx

**Bank-to-vendor map** (bank filings are linked in-cell in Table 2; additional sources)
- Celent NA Large Bank core report, FIS reprint, 2023-05-12 — https://www.fisglobal.com/-/media/fisglobal/files/pdf/report/retail-banking-core-banking-systems-na-large-bank-edition-2023-fis-reprint.pdf
- Banking Dive, Flagstar–Finxact, 2026-08-21 — https://www.bankingdive.com/news/flagstar-bank-fiserv-finxact-cloud-native-core-tech-modernization/828477/
- Banking Dive, Fiserv MOVEit / Flagstar, 2023-10-10 — https://www.bankingdive.com/news/fiserv-moveit-victim-cyberattack-breach-flagstar-bank-fis/696141/
- FinTech Futures, First Hawaiian stays with FIS, 2019-05-06 — https://www.fintechfutures.com/fintech/first-hawaiian-stays-with-fis-but-switches-core-systems
- American Banker, United Community renews with Fiserv, 2013 — https://americanbanker.com/news/united-community-banks-renews-with-fiserv
- Backbase–Eastern Bank, 2022-11-07 — https://www.backbase.com/press/backbase-announces-expanded-relationship-with-eastern-bank
- Business Wire, Wintrust selects NCR, 2020-12-02 — https://www.businesswire.com/news/home/20201202005953/en/Wintrust-Selects-NCR-Digital-First-Banking-Platform
- FIS client story: Wintrust (undated) — https://www.fisglobal.com/insights/fis-client-stories/wintrust
- Q2 press release, Synovus (2021) — https://www.q2.com/company/news/pr/synovus-banks-on-q2-to-deliver-innovative-digital-banking-services-faster
- MX, First Hawaiian Helios, 2021-05-27 — https://www.mx.com/news/first-hawaiian-bank-goes-live-with-mx-helios-for-mobile-banking-empowering-customers-with-financial-insights/
- nCino, FirstBank Puerto Rico, 2024 — https://investor.ncino.com/news-releases/news-release-details/firstbank-puerto-rico-selects-ncino-transform-commercial-lending
- Mass. AG notice 2026-1555 (Centennial Bank) — https://www.mass.gov/doc/2026-1555-centennial-bank-including-its-division-happy-state-bank/download
- JD Supra, FirstBank PR / MIAC — https://www.jdsupra.com/legalnews/firstbank-puerto-rico-announces-data-2253411/
- Homepages fetched 2026-10-22 (UNVERIFIED fingerprints): https://www.westernalliancebank.com · https://www.ozk.com · https://www.valley.com · https://www.ucbi.com · https://www.bankwithunited.com · https://www.eastwestbank.com · https://www.eaglebankcorp.com

**Incidents, 8-Ks and transmission**
- Microsoft Security Blog, Storm-0940 / ARTEX, 2026-10-21 — https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
- The Hacker News (Huntress 173 tenants), 2026-10-17 — https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
- Jack Henry statement (Finviz reprint), 2026-08-31 — https://finviz.com/news/387138/jack-henry-issues-statement-on-response-to-cybersecurity-incident
- American Banker, Jack Henry refuses extortion — https://www.americanbanker.com/news/jack-henry-refuses-to-pay-extortionists-after-data-theft
- Banking Exchange, Jack Henry — https://www.bankingexchange.com/news-feed/item/10680-jack-henry-cyberattack-compromises-client-data
- American Banker, Sharetec outage, 2026-09-21 — https://www.americanbanker.com/news/overheated-data-center-knocked-23-credit-unions-offline
- Banking Dive, FIS outage / Capital One, Jan 2025 — https://www.bankingdive.com/news/capital-one-outage-fis-bank-of-oklahoma-citi/737847/
- WBAY/CNN, Fiserv Zelle outage, 2025-05-02 — https://www.wbay.com/2025/05/02/zelle-is-down-some-bank-customers/
- The Record, Trellance ransomware, 2023-12 — https://therecord.media/credit-unions-facing-outages-due-to-ransomware
- CU Times, 2023-12-18 — https://cutimes.com/2023/12/18/back-online-but-not-out-of-the-woods-cu-ransomware-update
- American Banker, MOVEit 15 banks/CUs — https://americanbanker.com/creditunions/news/15-banks-credit-unions-confirm-moveit-data-breaches
- Kitco/Reuters, ION, 2023-02-07 — https://www.kitco.com/news/off-the-wire/2023-02-07/update-1-ion-brings-clients-back-online-after-ransomware-attack-source
- SecurityWeek, Evolve, 2024 — https://www.securityweek.com/evolve-bank-data-breach-impacts-7-6-million-people/
- CNBC via NBC NY, Synapse $85M — https://www.nbcnewyork.com/news/business/money-report/synapse-bankruptcy-trustee-says-85-million-of-customer-savings-is-missing-in-fintech-meltdown/5487272/
- Banking Dive, CFPB sues Synapse, 2025-08-27 — https://www.bankingdive.com/news/cfpb-sues-synapse-plans-use-victims-fund-pay-end-users/758776/
- Central Bank of the Bahamas, CrowdStrike — https://centralbankbahamas.com/news/public-notices/global-crowdstrike-outage-has-minimal-impact-on-retail-banking-services
- Bloomberg, Capitec, 2024-07-19 — https://www.bloomberg.com/news/articles/2024-07-19/capitec-of-south-africa-says-its-systems-hit-by-global-outage
- Globe and Mail/Reuters, C-Edge — https://www.theglobeandmail.com/business/article-ransomware-attack-forces-hundreds-of-small-indian-banks-offline
- CSO Online, Finastra — https://www.csoonline.com/article/3610267/finastra-investigates-breach-potentially-affecting-top-global-banks.html
- TSB FY2018 results, 2019-02-01 — https://www.tsb.co.uk/news-releases/tsb-announces-2018-full-year-results/
- Gulf News, RBS fine — https://gulfnews.com/amp/story/business%2Fbanking%2Frbs-fined-56m-for-it-meltdown-1.1415510
- DFPI, Patelco consent order, 2025-02-04 — https://dfpi.ca.gov/press_release/dfpi-takes-action-against-patelco-credit-union-for-cybersecurity-violations/
- Cleary Gottlieb, OCC Capital One penalty, 2020 — https://www.clearygottlieb.com/news-and-insights/publication-listing/occ-imposes-80-million-penalty-in-connection-with-bank-data-breach
- IMF blog, 2024-04-09 — https://www.imf.org/en/blogs/articles/2024/04/09/rising-cyber-threats-pose-serious-concerns-for-financial-stability
- Gogolin, Lim & Vallascas working paper, 2020 — https://www.communitybanking.org/~/media/files/communitybanking/2020/gogolin%20et%20al%202020%20cyberattacks%20on%20small%20banks30092020.pdf
- FDIC BankFind API — https://api.fdic.gov/banks/financials · NCUA call-report data — https://ncua.gov/files/publications/analysis/
- Bank Item 1.05 8-Ks: SSB https://www.sec.gov/Archives/edgar/data/764038/000095010324002017/dp206600_8k.htm · SSB/A https://www.sec.gov/Archives/edgar/data/764038/000155837024004390/ssb-20240206x8ka.htm · BAFN https://www.sec.gov/Archives/edgar/data/1649739/000164973925000246/bafn-20251028.htm · CBFV https://www.sec.gov/Archives/edgar/data/1605301/000160530126000021/cbfv-20260507.htm · RVRF https://www.sec.gov/Archives/edgar/data/1641601/000119312526282946/ck0001641601-20260619.htm (amendments: …/000119312526295704/, …/000119312526300763/, …/000119312526307288/, …/000119312526325324/)
- Bank Item 8.01 cyber 8-Ks: MBCN https://www.sec.gov/Archives/edgar/data/836147/000119312523300259/d441183d8k.htm · Santander Holdings USA https://www.sec.gov/Archives/edgar/data/811830/000081183024000030/statementissuedbybancosant.htm · MNSB https://www.sec.gov/Archives/edgar/data/1693577/000143774925019008/main20250328_8k.htm · HFWA https://www.sec.gov/Archives/edgar/data/1046025/000162828026020261/hfwa-20260320.htm · ORRF https://www.sec.gov/Archives/edgar/data/826154/000114036126023313/ef20075213_8k.htm · BPOP https://www.sec.gov/Archives/edgar/data/763901/000119312526263044/d46942d8k.htm · SRBK https://www.sec.gov/Archives/edgar/data/1951276/000094337426000261/srbk-20260706.htm
- Evertec 8.01s: https://www.sec.gov/Archives/edgar/data/1559865/000155986525000043/evtc-20250829.htm · https://www.sec.gov/Archives/edgar/data/1559865/000155986526000039/evtc-20260609.htm
- FHLBNY Item 1.05, 2024-03-01 — https://www.sec.gov/Archives/edgar/data/1329842/000165495424002505/fhlbny_8k.htm
- SEC Release 33-11216 — https://www.sec.gov/files/rules/final/2023/33-11216.pdf
- ABA Banking Journal, FDIC QBP Q2 2026 — https://bankingjournal.aba.com/2026/08/quarterly-banking-profile-banking-net-income-90-1b-in-q2-2026/

**AI agents, 1033 and Reg E**
- American Banker, JPMorgan on AI agents, 2026-10-13 — https://www.americanbanker.com/news/jpmorgan-warns-of-risks-to-consumers-who-rely-on-ai-agents
- Fortune, Dimon / Meta Muse, 2026-10-15 — https://fortune.com/2026/10/15/jamie-dimon-ai-agents-meta-muse-jpmorgan/
- RBI (citing FT) via Yahoo, 2026-10-19 — https://finance.yahoo.com/news/us-banks-limit-ai-agents-113229223.html
- Axios, 2026-10-22 (403; read via relays) — https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access
- Decrypt relay, 2026-10-22 — https://decrypt.co/381602/banks-rogue-ai-agents-inside-customer-accounts
- American Banker, Gould on rogue agents, 2026-10-22 — https://www.americanbanker.com/news/gould-banks-preparing-for-rogue-ai-agents-for-months
- American Banker, BofA and PNC on AI, 2026-09-14 — https://www.americanbanker.com/news/bofa-and-pnc-respond-to-rising-ai-fears
- Federal Register, 1033 final rule, 2024-11-18 — https://www.federalregister.gov/documents/2024/11/18/2024-25079/required-rulemaking-on-personal-financial-data-rights
- Cooley, 1033 final rule tiers, 2024-10-31 — https://www.cooley.com/news/insight/2024/2024-10-31-cfpb-finalizes-section-1033-rule-on-personal-financial-data-rights
- CFPB status report ECF 57, 2025-05-23 — https://infobytes.orrick.com/wp-content/uploads/DEFENDANTS-STATUS-REPORT-1.pdf
- ABA Banking Journal, injunction, 2025-11-03 — https://bankingjournal.aba.com/2025/11/kentucky-federal-court-enjoins-cfpb-from-enforcing-current-1033-final-rule/
- E.D. Ky. order ECF 93, 2025-12-10 — https://storage.courtlistener.com/recap/gov.uscourts.kyed.106299/gov.uscourts.kyed.106299.93.0.pdf
- CFPB reconsideration page — https://www.consumerfinance.gov/rules-policy/rules-under-development/personal-financial-data-rights-reconsideration/
- Cozen O'Connor, 2026-04-09 — https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration
- Ballard Spahr, OIRA submission, 2026-08-06 — https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/
- eCFR 12 CFR Part 1005 (as of 2026-10-01) — https://www.ecfr.gov/current/title-12/chapter-X/part-1005
- OCC Bulletin 2026-13, 2026-04-17 — https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html
- American Banker/Akoya open-finance survey, 2026-01-29 (updated 2026-05-01) — https://www.americanbanker.com/payments/news/exclusive-research-banks-approach-an-open-finance-shift

## Process Report

- **DEWEY verification and provenance:**
  - DEWEY ran the intake checks itself: the Microsoft 10/21 primary, the Axios coverage, the Jack Henry incident and the KRE holdings file (SSGA, as of 2026-10-21).
  - DEWEY re-verified all 9 bank Item 1.05 filings against `data.sec.gov/submissions` item codes (SSB 2, BAFN 1, CBFV 1, RVRF 5). The match was exact.
  - DEWEY checked the EWBC cell against map B's source line (FIS IBS notable-client list, Celent NA 2023), which is the same evidence class as WTFC.
  - Six Opus legs ran in data-return mode. A report-writer sub-agent drafted this report; DEWEY reviewed it before filing.
- **Searches run:**
  - Six research legs: vendor share; two bank-to-vendor maps; incident base rate; SEC 8-K census; AI-agent / 1033 / Reg E.
  - For the maps: EDGAR full-text search on ~45 vendor and cyber terms, restricted by CIK, for all 22 banks (2022-01-01 to 2026-10-22). Then latest 10-K Item 1A/1C reads, vendor-newsroom and trade-press searches, and homepage login-host fetches on 2026-10-22.
  - For the 8-K census: EDGAR FTS plus the submissions API across 3,605 bank-SIC CIKs, and 23 incident phrases for Item 8.01.
  - Primary data pulls: FDIC BankFind and NCUA call reports for deposits; yfinance for event windows.
  - What worked: the FTS `items` field matched the submissions API exactly, and merger 425 and investor-deck exhibits were the richest source of vendor names.
  - What did not work: 10-K text alone, where vendor names are almost never disclosed.
- **Data gaps:**
  - Vendor share by assets or tier.
  - Current core vendor for 8 banks, and current status for 4 stale ones.
  - OZK's FDIC-filed 10-K.
  - Names of the Trellance and Sharetec credit unions, which blocked a deposit test.
  - Daily or weekly deposit data for any incident.
  - AI-agent traffic or losses by bank size.
  - The 1033 rewrite text.
  - Addendum 1 leads other than ConnectWise were NOT checked: CrowdStrike AI-agent campaigns, PHP2Shell, LiteLLM / Railway / Zeabur, GitLab and Node.js.
- **Source frustrations:**
  - HTTP 403 on: Axios; the Fiserv investor deck and newsroom; FIS's 2019 First Hawaiian release; Jack Henry's IR page; the Maine and Massachusetts AG notices; FinTech Futures.
  - Paywalled: FedFIS, the Callahan 2026 guide, ABA survey tables.
  - The Quartr transcript tool returned a subscription error, so no earnings-call vendor remarks were checked.
  - FI Navigator vendor-level shares exist only as images.
  - OZK reports to the FDIC, not the SEC.
- **Confidence in findings:**
  - **High** that the 8-K counts are complete for SEC bank filers, and that no multi-bank core compromise or cyber run is documented.
  - **Medium** on concentration by count, because it rests on a 2022 survey.
  - **Low** on the bank-to-vendor map, given 8 UNKNOWN and 4 stale cells.
  - **Low** on any statement about the large-bank, multi-week tail, which has no precedent.
- **If I had more time/tools:**
  - Pull OZK's 10-K from the FDIC filing system.
  - Use Quartr or other transcripts for vendor remarks on bank earnings calls.
  - Get FedFIS / S&P MI core-vendor-by-asset data.
  - Read the FI Navigator infographics.
  - Run state-AG breach-portal sweeps per bank.
  - Check reginfo.gov for 1033 OIRA status.
  - Do WHOIS/TLS-certificate attribution for `onlineaccess1.com` and `ebanking-services.com`.
- **Suggestions:**
  - (1) Promote the 8-K item sweep (EFTS plus submissions-API cross-check) into `scripts/` as a reusable tool, subject to Will's build gate. A 1.05/8.01 bank count will recur.
  - (2) Add an FDIC-filer path for §12(i) banks such as OZK to `scripts/BACKLOG.md`.
  - (3) Treat merger Form 425 FAQs and investor-day decks as the first place to look for vendor identity.
  - (4) A vendor-fingerprint helper (login host → vendor) would turn UNVERIFIED leads into checkable ones. It should stay labelled UNVERIFIED until the domains are attributed.
