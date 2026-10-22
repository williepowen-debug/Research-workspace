# Is a cyber wave like "Black October" systemic? Base rates from five past waves
**Date:** 2026-10-22 (committed 15:16 ET) | **Mode:** Thesis | **Confidence:** Bank base rate: High (n=5 waves, primary regulators) · Insured losses: Medium-High (early-print estimates, PCS designations primary) · Equity reactions: Medium (DEWEY price pull; one event each, confounded) · October 2026 placement: Medium (live, attempts-only evidence) · AI acceleration: Medium on volume, Low on exploitation speed | **Request:** REQ-DEWEY-20261022-008 (WALTER, Will-approved ~14:00 ET) | **Recipients:** SHADE, REGINALD (action); GIBBS, VULCAN, HENRY, LIQUID, RED, PROME (info)

## Key Finding

Across five past waves (NotPetya 2017, SolarWinds 2020, Log4Shell 2021, MOVEit 2023, the CrowdStrike outage 2024), **none caused a bank run, a bank failure or a central-bank payment-system outage.**
- **Banks were hit in two ways:** data theft (MOVEit reached ~130 banks via vendors) and short outages (hours for CrowdStrike; up to ~9 days at a third of Ukraine's banks for NotPetya).
- **Insured losses ran $0.09B to just over $3B per event**, and none moved cyber-insurance prices.
- **Lasting stock damage fell on the vendor that was the attack vector:** SolarWinds −17% on day one; CrowdStrike −25% in 5 days; Progress −11% at the 20-day low. The broad market barely moved.

**October 2026 so far looks most like Log4Shell:** a flaw in ubiquitous open-source software, attempts in the millions, no confirmed compromise. It shares one feature with MOVEit: attempts began four days *before* public disclosure (Amazon, 17 Oct). That is the feature that historically produced a large victim list discovered weeks later. **As of 19:10 UTC on 22 Oct:**
- No successful PHP2Shell compromise is confirmed.
- Neither CVE is in CISA's Known Exploited Vulnerabilities (KEV) catalog.
- No US bank or core vendor is named.
- No insurer has commented.

**Kill condition at intake: not fired.** It was re-checked at 18:49, 18:53 and ~19:10 UTC.

## Intake check

| Check | Result |
|---|---|
| Kill condition, live event | CISA KEV catalog v2026.10.21 (released 21 Oct 14:04Z, 1,754 entries) pulled by DEWEY at 18:49Z and by leg C at 18:53Z: **neither CVE-2026-109618 nor -109619 listed**. No confirmed mass compromise; no named US bank or core-vendor victim (searches at ~18:50Z and ~19:10Z). Two leads are unconfirmed (Escalation checklist, row 1). |
| Kill condition, existing study | Grep of SHADE, REGINALD, GIBBS and VULCAN: **no cyber-event base-rate study.** Adjacent: DEWEY `output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md` (REQ-001, this morning: vendor concentration, 8-K counts, "no IT or cyber event has a documented deposit run"), extended here, not repeated; REGINALD `reports/2026-10-22_AI-agent-banking-doc_analysis.md` (AI agents and deposit speed; different question). |
| Commission premises corrected | (1) The CSRB did not say "no major cyberattack attributed to [Log4j] in the US". It said "the Board is not aware of any significant Log4j-based attacks on critical infrastructure systems", with no US limit. (2) Merck's NotPetya cost documented in its 10-Ks is ~$695M, not the widely quoted ~$870M. (3) Wiz's "AI inflection point" is one case with no counts (§6). |

## Evidence

### (1) The five waves compared

| Wave | What was hit | Disclosure → confirmed mass compromise or outage | Organizations affected | Financial victims | Time to full scope | Sources |
|---|---|---|---|---|---|---|
| **NotPetya** (27 Jun 2017) | Ukrainian tax software (M.E.Doc) update, then a self-spreading wiper | **Same day** (destructive on arrival) | No documented count. Firm losses from filings: FedEx/TNT ~$400M; Merck ~$695M; Mondelez −0.4% revenue + $84M; Maersk $200–300M | About **a third of Ukrainian banks** knocked out (NBU) | Banks ~9 days; firm losses fixed over 4–20 months; US/UK attribution ~8 months | [PRIMARY: FedEx 10-K FY2018](https://www.sec.gov/Archives/edgar/data/1048911/000156459018016877/fdx-10k_20180531.htm); [Merck 10-K 2018](https://www.sec.gov/Archives/edgar/data/310158/000031015819000014/mrk1231201810k.htm); [Mondelez 10-K 2017](https://www.sec.gov/Archives/edgar/data/1103982/000119312518037332/d466496d10k.htm); [NEWS: Mind.ua relaying NBU, 6 Jul 2017](https://mind.ua/news/20173935-nbu-minulogo-tizhnya-kiberataka-vivela-z-ladu-tretinu-ukrayinskih-bankiv) |
| **SolarWinds** (13 Dec 2020) | Backdoored Orion IT-monitoring updates, Mar–Jun 2020 (espionage) | Backdoor live **~9 months before** disclosure; victims named **+66 days** | ~18,000 installed it; **9 federal agencies + ~100 companies** actually compromised | NYDFS: **88 regulated firms ran a corrupted Orion; none actively exploited** | 66 days to victim count | [PRIMARY: SolarWinds 8-K, 14 Dec 2020](https://www.sec.gov/Archives/edgar/data/1739942/000162828020017451/swi-20201214.htm); [White House, 17 Feb 2021](https://bidenwhitehouse.archives.gov/briefing-room/press-briefings/2021/02/17/press-briefing-by-press-secretary-jen-psaki-and-deputy-national-security-advisor-for-cyber-and-emerging-technology-anne-neuberger-february-17-2021/); [NYDFS report, Apr 2021](https://www.dfs.ny.gov/system/files/documents/2021/04/solarwinds_report_2021.pdf) (DEWEY read) |
| **Log4Shell** (9 Dec 2021) | Remote-code-execution flaw in a ubiquitous open-source Java logging library | Scanning within **2 hours**; **no mass compromise ever confirmed** | "Hundreds of millions" of devices exposed; exploitation "at lower levels than many experts predicted" | No bank victim found; one fintech (ONUS, Vietnam) lost data | Never: the CSRB calls it an "endemic vulnerability" lasting "a decade or longer" | [PRIMARY: CSRB report, 11 Jul 2022](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf) (DEWEY read) |
| **MOVEit** (31 May 2023) | Flaw in a file-transfer product, used for mass data theft (Cl0p) | **Negative lead:** exploitation began 27 May, before disclosure; first leak-site names +14 days | **2,773 organizations, ~95.8M people** (Emsisoft, Jun 2024) | ~**132 banks** (117 US) in KonBriefing's list, mostly via vendors (Fiserv, FIS, PBI, Majorel) | Still growing **13+ months** later | [PRIMARY: CISA AA23-158A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a); [INSTITUTIONAL: Emsisoft](https://www.emsisoft.com/en/blog/44123/unpacking-the-moveit-breach-statistics-and-analysis/); [KonBriefing](https://konbriefing.com/en-topics/cyber-attacks-moveit-victim-list.html) |
| **CrowdStrike outage** (19 Jul 2024; an accident) | Faulty security-software update crashed Windows hosts | **Immediate:** file live 78 minutes, global outage within hours | **8.5M devices** (Microsoft); 125 of the Fortune 500; $5.4B direct loss (Parametrix model) | Banking loss ~$1.15B (Parametrix, Fortune 500 only); named outages at CBA, Capitec, Absa, Bradesco, Barclays, TD, LSEG | ~99% of sensors restored in 10 days | [PRIMARY: CrowdStrike RCA](https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/); [Microsoft, 20 Jul 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/); [NEWS: Dark Reading on Parametrix](https://www.darkreading.com/cybersecurity-operations/crowdstrike-outage-losses-estimated-staggering-54b) |

### (2) Banks

| Wave | Effect on banks or payments | Type | Duration | Deposits | Regulator action | Sources |
|---|---|---|---|---|---|---|
| NotPetya | A third of Ukrainian banks down; Ukrgasbank took paper orders. **The NBU's own payment system (SEP) and card processing ran normally** | Service loss (wiper) | ~2–9 days | None found | NBU emergency operating-mode decision (29 Jun 2017); created CSIRT-NBU | [NEWS: Glavcom relaying NBU](https://glavcom.ua/news/robota-bankiv-postrazhdalih-vid-hakerskoji-ataki-vidnovlyujetsya-nacbank-423055.html) |
| SolarWinds | 88 NYDFS firms had the backdoor; all 36 with Sunburst removed it by 19 Dec; "no reports or indications that hackers exploited [it] in any financial services organization" | Espionage; no bank exploitation | n/a | None | NYDFS alert (18 Dec 2020) and report | [PRIMARY: NYDFS](https://www.dfs.ny.gov/system/files/documents/2021/04/solarwinds_report_2021.pdf) |
| Log4Shell | No bank compromise found | — | — | None | FINRA/FCA alerts; CSRB review | CSRB |
| MOVEit | Customer data stolen, mostly through vendors; no loss of service | Data only | n/a | **None documented**; data-breach analogues (Evolve 2024) show deposits *rising* (REQ-001) | SEC inquiry into Progress closed with no action (Aug 2024) | [PRIMARY: Progress 8-K, 7 Aug 2024](https://www.sec.gov/Archives/edgar/data/876167/000087616724000138/pressrelease-sec.htm) |
| CrowdStrike | App, card and payment outages; NCR Voyix payments gateway down 1:30–6:03 a.m. EST. **Fed systems "not affected"** (Fed officials via the ABA); ABA: "no indication of any systemic risk" | Service loss | Hours, same day | None found | FCA chaired the UK response; FINRA alert. No Fed statement found | [PRIMARY: ABA CEO letter, 19 Jul 2024](https://oba.com/wp-content/uploads/2024/07/ABA-message-from-Rob-Nichols-07192024.pdf); [NCR Voyix](https://www.ncrvoyix.com/newsroom/crowdstrike-security-update-global-outage-resolved); [FCA FOI](https://www.fca.org.uk/freedom-information/information-crowdstrike-outage-19-july-august-2024) |

**What the systematic evidence adds:**
- **IMF (Apr 2024):** "cyber incidents have thus far not been systemic". After a cyber incident, "retail and wholesale deposits at smaller banks tend to decline by about 5 percent in cumulative terms some six quarters after". That is a slow drain, not a run. Outflows have been "modest" and liquidity rules "appear to have generally been sufficient" ([PRIMARY: IMF GFSR Apr 2024, ch. 3, pp. 1, 14–15, 18](https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch3.pdf); DEWEY read pp. 1 and 14).
- **The modeled tail is large.** If any of the five most active US banks were impaired, "38 percent of the network [would be] affected on average", rising to 22–55% of bank assets depending on the bank ([ACADEMIC: NY Fed Staff Report 909, Eisenbach/Kovner/Lee, rev. May 2021](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr909.pdf); DEWEY read the abstract).
- **The ESRB** (2020, 2022): "to date no cyber incidents with a systemic impact for the financial system have materialised" ([INSTITUTIONAL: ESRB 2022, p. 4](https://www.esrb.europa.eu/pub/pdf/reports/esrb.SystemiCyberRisk.220127~b6655fa027.en.pdf)).
- **The Fed's May 2026 Financial Stability Report:** a successful cyberattack "continued to be flagged as having the most severe potential consequences" but was "not cited as a top risk". It now names "large language models and agentic AI systems [that] detect and exploit vulnerabilities" ([PRIMARY: Fed FSR, 8 May 2026, p. 47, Box 5.1](https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf)).

**Other cyber events and banks, one line each:**
- **Bangladesh Bank (2016):** an $81M theft, not a run.
- **ICBC Financial Services ransomware (Nov 2023):** some Treasury trades went unsettled; impact "limited". The $9B owed to BNY is UNVERIFIED.
- **Heartland Tri-State Bank (failed Jul 2023):** the one cyber-adjacent failure. The CEO wired $47.1M of bank funds into a crypto scam; social-engineering fraud, not an IT compromise ([PRIMARY: Fed OIG, Feb 2024](https://oig.federalreserve.gov/reports/board-material-loss-review-heartland-tri-state-bank-feb2024.pdf)).
- **Closest run analogue (IMF fn 38):** a 2014 rumour-driven 10% retail run at First Investment Bank, Bulgaria. Not a cyberattack.

### (3) Insurance

| Event | Insured loss (latest found) | Economic loss | Catastrophe designation | Source |
|---|---|---|---|---|
| NotPetya 2017 | **Above $3B**, "still developing". ~85% via property policies not written as cyber cover ("silent cyber"); two insureds >80% | $10B (PCS table) | "First PCS-designated global cyber catastrophe" | [PRIMARY: Verisk PCS, undated (2019+)](https://www.verisk.com/siteassets/media/pcs/pcs-cyber-catastrophe-notpetyas-tail.pdf) |
| SolarWinds 2020 | **$90M** (BitSight/Kovrr) | Not estimated | No | [INSTITUTIONAL: BitSight, 12 Jan 2021](https://bitsighttech.com/press-releases/bitsight-and-kovrr-conduct-joint-analysis-of-the-financial-impact-of-the-solarwinds-breach-announce-new-partnership) |
| Log4Shell 2021 | **No estimate exists**; the "Hurricane Andrew" worm scenario never happened | — | No | [INSTITUTIONAL: Moody's RMS](https://www.moodys.com/web/en/us/insights/insurance/log4j-vulnerability-and-the-complexity-of-modeling-cyber-risk.html) |
| MOVEit 2023 | **Above $250M** (PCS threshold; no point estimate) | — | **PCS Cyber Catastrophe Loss Event**, 29 Apr 2024 | [NEWS reporting PCS: Artemis](https://www.artemis.bm/news/pcs-designates-change-healthcare-moveit-as-cyber-catastrophe-loss-events/) |
| CrowdStrike 2024 | **$0.27–1.5B** across four modelers (all Jul–Aug 2024 first prints; no revision found). Guy Carpenter: a "kitty cat" | $5.4B (Fortune 500 excl. Microsoft) | **PCS Cyber Catastrophe Loss Event**, 30 Jul 2024 ("third") | [Artemis, 30 Jul 2024](https://www.artemis.bm/news/pcs-designates-crowdstrike-as-a-cyber-catastrophe-loss-event/) (DEWEY read); [Insurance Journal (Guy Carpenter)](https://www.insurancejournal.com/news/national/2024/08/02/786766.htm) |

**Pricing never reacted.** Marsh's index shows US cyber rates peaking at +130% in Q4 2021, driven by ransomware, not by any of these waves. Rates were −6% in the CrowdStrike quarter (Q3 2024), the same as the two quarters before. In **Q3 2026, global rates were −4% and US rates flat**, with "capacity continued to expand" ([PRIMARY: Marsh Global Insurance Market Index, read 22 Oct 2026](https://www.marsh.com/en/services/international-placement-services/insights/global-insurance-market-index.html); DEWEY read). The market is ~$15–16B of premium (Munich Re; Swiss Re).

**Tail anchors:**
- Guy Carpenter 1-in-200 industry loss: **$15.6–33.4B** ([NEWS: Infosecurity, Jun 2023](https://www.infosecurity-magazine.com/news/insurers-predict-33bn-catastrophic/)).
- Lloyd's/Cambridge payment-system attack scenario: **$3.5T** economic loss over 5 years. No insured figure ([PRIMARY: Lloyd's, Oct 2023](https://www.lloyds.com/insights/media-centre/press-releases/lloyds-systemic-risk-scenario-reveals-global-economy-exposed-to-3.5trn-from-major-cyber-attack)).

**War exclusions:**
- **Merck v. ACE** (NJ App. Div., 1 May 2023): a "hostile or warlike action" exclusion needs a military link, so it did not apply to NotPetya. The case settled confidentially in Jan 2024 before the state supreme court heard it.
- **Mondelez v. Zurich:** settled mid-trial in Nov 2022, terms undisclosed.
- **Lloyd's Bulletin Y5381:** requires state-backed-attack exclusions (LMA5564–5567) in all standalone cyber policies from 31 Mar 2023.
- **So state attribution of "Black October" would be a swing factor for insured loss** ([NEWS: Claims Journal](https://amp.claimsjournal.com/news/east/2023/05/04/316786.htm); [Business Insurance](https://www.businessinsurance.com/Merck,-insurers-settle-dispute-over-2017-NotPetya-cyberattack-Merck-Co,-Inc-v/); [INSTITUTIONAL: Kennedys](https://kennedyslaw.com/thought-leadership/article/new-lloyd-s-market-bulletin-addresses-state-backed-cyber-attacks)).

**October 2026:** no broker, reinsurer, rating agency, Lloyd's, PCS or cyber modeler statement found as of ~14:55 ET.

### (4) Equities: DEWEY price pull

All rows below come from DEWEY's own pull.
- **Method:** yfinance adjusted closes. Base = the close before the first trading day after disclosure (d0); +n = n trading days after d0. "vs S&P" = the stock's return minus the S&P 500's over the same window (simple market adjustment, not a regression model).
- **SolarWinds:** SWI is delisted (taken private 2025) and has no yfinance data. Its d0 figure is from law-firm releases quoting the close: $23.55 → $19.62 (−17%), then $18.06 on 15 Dec (−23% over 2 days) ([NEWS: Robbins LLP](https://www.robbinsllp.com/solarwinds-corporation/)).

| Wave (d0) | Stock | d0 | +5 | +20 | +60 | 20-day low | vs S&P at +20 |
|---|---|---|---|---|---|---|---|
| NotPetya (27 Jun 2017) | Merck | −0.6% | −2.7% | −6.2% | +0.2% | −5.4% | −7.8 pp |
| | Mondelez | −2.1% | −3.5% | −1.1% | −10.1% | −3.8% | −2.7 pp |
| | FedEx | −0.5% | +1.4% | −0.8% | +1.8% | −2.0% | −2.4 pp |
| | Maersk | −0.5% | +2.5% | +6.1% | −7.9% | −0.5% | +4.5 pp |
| | Cyber ETF (HACK) | −1.2% | −1.5% | −0.7% | −1.1% | −3.0% | −2.3 pp |
| | S&P 500 | −0.8% | −0.3% | +1.6% | +2.5% | −1.2% | — |
| SolarWinds (14 Dec 2020) | **SolarWinds (vector)** | **−17%** | n/a | n/a | n/a | — | — |
| | CrowdStrike | −1.2% | +19.7% | +28.7% | +13.1% | −1.2% | +24.7 pp |
| | Palo Alto | +1.4% | +14.9% | +18.0% | +10.5% | +1.4% | +14.0 pp |
| | Cyber ETF (HACK) | +0.7% | +8.1% | **+11.3%** | +8.6% | +0.7% | **+7.3 pp** (+1.0 pp at +60) |
| | S&P 500 | −0.4% | +0.9% | +4.0% | +7.6% | −0.4% | — |
| Log4Shell (10 Dec 2021) | Cyber ETF (HACK) | −0.6% | 0.0% | −2.9% | −6.5% | −3.6% | −3.0 pp |
| | Fortinet | +5.1% | +5.5% | +2.6% | −9.2% | −4.1% | +2.5 pp |
| | S&P 500 | +1.0% | −1.0% | +0.1% | −8.3% | −2.1% | — |
| MOVEit (1 Jun 2023) | **Progress (vector)** | −0.8% | 0.0% | −3.2% | +2.9% | **−10.7%** | −9.7 pp |
| | Cyber ETF (HACK) | −0.7% | −1.0% | +2.4% | +3.6% | −1.8% | −4.1 pp |
| | S&P 500 | +1.0% | +2.7% | +6.5% | +6.1% | +1.0% | — |
| CrowdStrike (19 Jul 2024) | **CrowdStrike (vector)** | **−11.1%** | **−25.3%** | −23.5% | −9.5% | **−36.5%** | −23.7 pp |
| | Microsoft | −0.7% | −3.4% | −4.8% | −4.6% | −10.3% | −5.0 pp |
| | Delta | +1.2% | −1.8% | −10.3% | +19.2% | −16.6% | −10.5 pp |
| | Cyber ETF (HACK) | −0.9% | −1.4% | +3.2% | +11.7% | −6.7% | +3.0 pp |
| | Bank ETF (KBE) | +0.1% | +5.3% | −1.3% | +5.7% | −6.6% | −1.5 pp |
| | S&P 500 | −0.7% | −1.5% | +0.2% | +5.7% | −6.5% | — |
| **October 2026** (base 20 Oct close) | CrowdStrike / Cloudflare / Zscaler / Palo Alto | +5.3% / +5.3% / +7.8% / +2.0% (21 Oct close) | — | — | — | — | — |
| | Cyber ETF (HACK) | +3.2% (21 Oct); **+3.6%** intraday 22 Oct ~14:51 ET | — | — | — | — | — |
| | Regional banks (KRE) | 0.0% (21 Oct); **+2.3%** intraday 22 Oct | — | — | — | — | — |
| | S&P 500 | +0.6% (21 Oct); **−0.9%** intraday 22 Oct | — | — | — | — | — |

Readings from the table:
- **The vector vendor takes the lasting damage:** SolarWinds, Progress, CrowdStrike.
- **Directly hit companies show small, confounded moves.** Mondelez −10% at +60 overlaps a guidance cut.
- **Cybersecurity stocks rallied only after SolarWinds**, a state espionage case that coincided with a broad growth-stock rally. Against the market, the gain was +7.3 pp at 20 days and +1.0 pp at 60 days, so it faded. After Log4Shell and MOVEit, cyber stocks lagged the market.
- **Bank stocks did not react to the CrowdStrike outage.**
- **The academic evidence agrees.** Malicious incidents cut equity prices by 0.1–0.2 pp on average, more at small firms ([PRIMARY: IMF GFSR ch. 3, Fig. 3.6](https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch3.pdf); DEWEY read). Breached firms show a mean 3-day abnormal return of −0.7%, with no 12-month drift ([ACADEMIC: Hilary/Segal/Zhang via HLS Forum, Nov 2016](https://corpgov.law.harvard.edu/2016/11/15/cyber-risk-disclosure-who-cares/)).
- **Supply-chain amplification is the exception that matters.** NotPetya's customer-firm profit losses ($7.3B) were 4× the directly hit firms' damages ($1.8B) ([ACADEMIC: NY Fed SR 937, Crosignani et al.](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr937.pdf)).

### (5) October 2026: where it sits, and escalation signs

**Placement**

| Feature | Oct 2026 (as of ~19:10Z, 22 Oct) | Most like | Source |
|---|---|---|---|
| Flaw type | Remote code execution in core PHP (~2.6M internet-facing hosts per VulnCheck; counts conflict) plus a certificate-authority key failure plus supply-chain poisonings | **Log4Shell** (ubiquitous open-source runtime) | WALTER SIG-W-20261022-025 |
| Exploitation before disclosure | **Yes:** Amazon honeypot attempt 17 Oct; disclosure 21 Oct | **MOVEit** (27 May vs 31 May) | [PRIMARY: AWS Security Blog, 21 Oct 2026](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/) |
| Confirmed successful compromise | **None publicly named**; organizations report attempts "unsuccessful"; circulating proofs of concept reportedly do not achieve code execution (watchTowr, as relayed) | **Log4Shell** | [NEWS: SecurityWeek, 22 Oct](https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/); [The Register, 22 Oct](https://www.theregister.com/cyber-crime/2026/10/22/hackers-pile-on-php2shell-as-aws-reveals-attacks-began-before-disclosure/5304749) |
| Breadth of attempts | Check Point: 10% of organizations worldwide, 8% in financial services, "impacted", defined as attempts ("no way of knowing if the attack has been successful") | **Log4Shell** | [INSTITUTIONAL: Check Point, 22 Oct](https://blog.checkpoint.com/ai-security/php2shell-one-in-ten-organizations-impacted-as-europe-bears-the-brunt) |
| Bank effect | Japanese banks: precautionary shutdowns, no compromise confirmed; interbank network "no impact at present" (Japanese Bankers Association); partial restorations unconfirmed. No US or European bank named | **CrowdStrike-lite** (service loss by choice, not by attack) | [NEWS: Jiji via nippon.com, 22 Oct](https://www.nippon.com/en/news/yjj2026102200263/) |
| Market | Cyber stocks +2–8% on 21 Oct; mixed intraday 22 Oct; banks up | **Log4Shell/MOVEit** (no sustained sector move so far) | §4 |
| Insurance | No statement | Log4Shell | §3 |

**Escalation checklist.** These signs would move it toward the MOVEit or NotPetya cases.

| # | Sign | Status at ~19:10Z, 22 Oct | Why it matters | Who watches |
|---|---|---|---|---|
| 1 | **Confirmed successful PHP2Shell compromise** (named victim, incident-response case, ransomware claim) | **Not yet.** Leads are unconfirmed: the Dutch NCSC is "investigating first signs of successful misuse" (no primary found); Patchstack first reported "multiple active exploitation incidents", then said its telemetry shows probing only | Pre-disclosure exploitation plus a low-footprint compromise (CrowdStrike lab finding) is the MOVEit/SolarWinds pattern: the victim list surfaces weeks later | WALTER |
| 2 | **CISA KEV listing** of CVE-2026-109618/-109619 | **Not listed** (v2026.10.21) | KEV means confirmed in-the-wild exploitation. The AI-found wp2shell flaw went from disclosure to KEV in 4 days (Jul 2026) | WALTER |
| 3 | **Named US bank, credit union or core/digital-banking vendor victim** (Fiserv, Jack Henry, FIS, Q2, Alkami, NCR Voyix) | **None** | The vendor-concentration channel (REQ-001: 3 vendors run >70% of US bank cores) | REGINALD, GIBBS |
| 4 | **8-K Item 1.05** (material cybersecurity incident) from a bank or vendor citing PHP | None found (not systematically swept today) | First public, legally required confirmation | REGINALD |
| 5 | **Regulator statement** (Fed, OCC, FDIC, FFIEC, NYDFS, FS-ISAC, ECB) | None found; an NYDFS alert is referenced but unread | Supervisory concern signal | REGINALD |
| 6 | **PCS cyber catastrophe designation**, or a cyber modeler's industry loss estimate | None | Above $250M insured (the PCS threshold); MOVEit and CrowdStrike both crossed it | SHADE |
| 7 | **State attribution** (US/UK/EU government) | None | Triggers state-attack exclusions; NotPetya attribution took ~8 months | SHADE |
| 8 | **Loss-of-service outages outside Japan** at banks or payment systems | None | The CrowdStrike/NotPetya channel; deposits have never run, but payments stopped | REGINALD, LIQUID |
| 9 | **Sustained equity move**: vector-vendor collapse, or a cyber-sector gain persisting past ~20 trading days, or bank-stock underperformance | None (day 1–2 only) | Past waves: only vectors lost lastingly; sector gains faded within 60 days | HENRY, VULCAN |

### (6) Is AI speeding up discovery and exploitation?

| Measure | Figure | Label | Source |
|---|---|---|---|
| CVEs published, US National Vulnerability Database (NVD) | Q3 2025 **11,725** vs Q3 2026 **36,961** (+215%); 2026 to 21 Oct: 85,344 (all of 2025: 48,151) | MEASURED | [PRIMARY: NVD API 2.0](https://services.nvd.nist.gov/rest/json/cves/2.0) (DEWEY re-pulled the Q3 figures) |
| CISA KEV additions | Q3 2025: 51 vs Q3 2026: **100** (+96%) | MEASURED | CISA KEV JSON (leg C count) |
| Share of KEVs exploited on or before disclosure day | 28.93% (2025) → **23.43%** (1H 2026) | MEASURED | [INSTITUTIONAL: VulnCheck, 28 Jul 2026](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026) |
| AI-found flaws confirmed exploited | **14 of 1,061 (1.3%)**, about the base rate | MEASURED | same |
| Mandiant time-to-exploit (TTE: days from disclosure to exploitation) | 63 days (2018–19) → 32 (2021–22) → **5 (2023)** | MEASURED | [PRIMARY: Google/Mandiant, Oct 2024](https://cloud.google.com/blog/topics/threat-intelligence/time-to-exploit-trends-2023) |
| An AI-found flaw exploited fast | wp2shell (WordPress core; found with an OpenAI model): disclosed 17 Jul 2026, **in KEV 21 Jul** | MEASURED (one case) | CISA KEV; [INSTITUTIONAL: Wiz](https://wiz.io/blog/wp2shell-cve-2026-63030-cve-2026-60137) |
| Wiz "AI inflection point" (PHP2Shell) | One case: "a single researcher completed in a week what previously would have taken a world-class team months". **No counts or rates** | VENDOR CLAIM | [INSTITUTIONAL: Wiz, 21 Oct 2026](https://www.wiz.io/blog/php2shell-php-rce) |
| Anthropic Glasswing / OpenAI Aardvark / Google Big Sleep / DARPA AIxCC | "Thousands" of zero-days claimed; VulnCheck ties 126 published Glasswing CVEs to **1 confirmed exploited** (Jul); AIxCC found 18 real-world flaws | VENDOR CLAIM / MEASURED (competition) | [Anthropic](https://www.anthropic.com/glasswing); [NEWS: CSO](https://www.csoonline.com/article/4159617/behind-the-mythos-hype-glasswing-has-just-one-confirmed-cve.html); [PRIMARY: DARPA, 8 Aug 2025](https://darpa.mil/news/2025/aixcc-results) |

**Reading:**
- **Discovery is measurably accelerating.** Disclosures roughly tripled year on year. How much of that is AI, rather than changes in how CVEs get assigned, is **not measured**.
- **Exploitation is not measurably faster on average.** The same-day share fell, and confirmed exploitation roughly doubled while disclosures tripled.
- **The fast-exploitation evidence is a few cases** (wp2shell; PHP2Shell's pre-disclosure attempts).
- **NVD's 2026 severity counts are unusable** (scoring backlog): do not cite a 2026 "critical CVE" count.

## Counter-Evidence

**Against "this wave is likely to stay a patching scramble":**
- **The two worst historical shapes both began with invisible compromise.** MOVEit was exploited before disclosure, and SolarWinds was in place for 9 months. Victims surfaced weeks to months later. Amazon's 17 Oct attempt and CrowdStrike's "virtually no digital footprint" lab finding mean **"no compromise confirmed" today is weak evidence** for the weeks ahead.
- **The flaw volume is unprecedented.** Disclosures run ~3× last year's, and defenders' patch capacity is finite. The CSRB said Log4j itself remains "endemic".
- **The modeled tail is real.** One top-5 bank impaired affects 38% of the payment network (NY Fed). A 1-in-200 insured loss is $15.6–33.4B. The Fed's May 2026 report now names AI-driven exploitation.
- **Insured-loss estimates are first prints.** NotPetya's tail grew from ~$2.7B to above $3B over years.
- **Small banks lose ~5% of deposits over six quarters after an incident** (IMF). That is not a run, but it is not nothing for thin-margin banks.

**Against "cyber waves are systemic market events":**
- **No systemic event yet.** No cyber event has been systemic for the financial system (IMF, ESRB ×2, the Fed survey's own ranking).
- **No bank damage across five waves:** no run, no failure, no central-payment outage.
- **Small insured losses:** $0.09–3B per event, and prices did not react.
- **Short-lived stock effects:** −0.1 to −0.7% on average for breached firms.
- **Log4Shell is the direct precedent for "loud and small".** Exploitation came "at lower levels than many experts predicted" (CSRB).
- **Typical breach costs are tiny:** ~$200K, and most events cost <0.4% of annual revenue ([ACADEMIC: RAND/Romanosky 2016](https://www.rand.org/news/press/2016/09/20/index1.html)).

**Measurement caveats on both sides:**
- **Few cases:** each wave is one event. The equity windows are confounded by market conditions (Dec 2020 growth rally; Jul 2024 earnings).
- **Selection bias:** the IMF warns that only reported incidents enter its sample.

## Unknowns

| Unknown | Why it matters | What would close it |
|---|---|---|
| Whether any PHP2Shell attempt succeeded at a real organization | The whole escalation path | Incident-response case reports; Dutch NCSC and Patchstack primaries; KEV listing |
| Whether the PHP2Shell compromise is truly low-footprint in the wild (vs CrowdStrike's lab finding) | Determines whether "none confirmed" means anything | Incident-response forensics, next 2–6 weeks |
| Which US banks and vendors run exposed PHP, especially old versions with no patch (≤8.1) | The bank channel | Not public; vendor statements; FS-ISAC |
| Whether the 2026 CVE surge comes from AI discovery or process changes | VULCAN's AI question | CNA-level breakdown of the NVD data |
| Revised CrowdStrike and MOVEit insured totals | Calibrates the loss base rate | PCS industry totals (subscription) |
| Fed, OCC, FDIC and NYDFS statements on PHP2Shell | Supervisory signal | Agency pages; the NYDFS alert text (403 to DEWEY) |
| Japanese bank restoration and forensics (MUFG, Nomura) | Whether precautionary shutdowns hid compromise | Bank releases; JBA |

**Does the fleet need a cyber owner? (DEWEY's view, as the commission asked; Will and PROME decide.)** The base rates point to a mechanical watch rather than a standing desk: five waves produced no bank run and small insured losses, so the 9-row escalation checklist above can run as a WALTER watch. SHADE would own rows 6–7 (insurance) and REGINALD rows 3–5 and 8 (banks), with a desk only if a row fires.

## Source Quality Assessment

**Strong, primary:**
- Bank base rate: NYDFS, CSRB, the IMF chapter, the NY Fed paper, company 10-Ks and 8-Ks. DEWEY read the key passages itself.
- PCS designations.
- The Marsh Q3 2026 page.
- DEWEY's own price, KEV and NVD pulls.

**Medium:**
- Insured-loss figures: modelers' first prints, mostly via trade press.
- The Ukrainian bank figures: NBU via Ukrainian press.

**Weak:**
- The October 2026 escalation leads (Dutch NCSC, Patchstack).
- Japanese restoration status.
- The Wiz AI claim.
- Equity-reaction windows: one event each, simple market adjustment, confounded.

## References

All accessed 2026-10-22. Primary links are inline in the tables. Key sources:
- IMF GFSR April 2024, ch. 3: https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch3.pdf
- NY Fed Staff Report 909: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr909.pdf ; SR 937: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr937.pdf
- CSRB Log4j report, 11 Jul 2022: https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf
- NYDFS SolarWinds report, Apr 2021: https://www.dfs.ny.gov/system/files/documents/2021/04/solarwinds_report_2021.pdf
- ESRB 2020: https://www.esrb.europa.eu/pub/pdf/reports/esrb.report200219_systemiccyberrisk~101a09685e.en.pdf ; ESRB 2022: https://www.esrb.europa.eu/pub/pdf/reports/esrb.SystemiCyberRisk.220127~b6655fa027.en.pdf
- Fed Financial Stability Report, 8 May 2026: https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf
- Verisk PCS NotPetya: https://www.verisk.com/siteassets/media/pcs/pcs-cyber-catastrophe-notpetyas-tail.pdf
- Marsh Global Insurance Market Index: https://www.marsh.com/en/services/international-placement-services/insights/global-insurance-market-index.html
- AWS MadPot PHP2Shell, 21 Oct 2026: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/
- VulnCheck State of Exploitation 1H 2026: https://www.vulncheck.com/blog/state-of-exploitation-1h-2026
- CISA KEV JSON: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Fleet: WALTER SIG-W-20261022-025 and helper ledgers `AGENTS/WALTER/research/2026-10-22_afternoon/verify-cyber-{php-sector,supplychain}.md`; DEWEY REQ-001 report (above).

**Reproduction recipes:**
- **Equity windows:** yfinance `Ticker(t).history(auto_adjust=True)` for the tickers in §4. Base = last close before d0; returns at trading-day offsets 0/5/20/60; 20-day min over the first 20 sessions. October 2026 intraday values were read at ~14:51 ET on 22 Oct and are not closes.
- **NVD counts:** `/rest/json/cves/2.0?pubStartDate=…&pubEndDate=…&resultsPerPage=1&noRejected`, one quarter per call, reading `totalResults`.

## Process Report

- **Engine sizing:** four targeted legs plus DEWEY's own primary pull, not the full fan-out harness, because the residual split cleanly into four researchable questions.
  - Four Opus legs in data-return mode, each with its own search budget: A (waves and banks) ≤25, used 20; B (insurance) ≤25, used 25; C (AI and live wave) ≤25, used 25; D (systemic analyses and counter-evidence) ≤15, used 15.
  - **DEWEY's primary pull:** KEV, NVD re-pull, equity event windows, kill-condition searches.
- **DEWEY verified at the primary:** NYDFS SolarWinds (PDF text), CSRB Log4j (PDF text), IMF ch. 3 deposit and "not systemic" quotes (PDF text), NY Fed SR 909 abstract, Marsh Q3 2026, the PCS CrowdStrike designation, the NVD Q3 counts, and KEV. All matched.
- **Searches run:** 85 by legs plus 5 by DEWEY. The session-wide 200-search cap is shared with this afternoon's REQ-007 follow-up (86); about 24 remain.
- **Data gaps:**
  - Revised CrowdStrike, MOVEit and Change Healthcare insured totals (PCS subscription).
  - The Google/Mandiant TTE 2024–25 editions.
  - The Dutch NCSC and Patchstack primaries.
  - The NYDFS PHP2Shell alert text.
  - The Fed's own CrowdStrike statement (ABA relay only).
  - The published tables of Kamiya et al. (JFE 2021).
  - Peer-reviewed event studies of attack-vector vendors.
- **Source frustrations:** the IMF and CRA-style PDFs refuse curl but download via WebFetch; Stooq now serves a JavaScript bot wall; Wired, ThinkAdvisor, S&P, CNBC and WTW blocked; the Travelers 10-Q fetch was truncated.
- **Confidence in findings:** High on "no systemic bank effect in five waves"; Medium on insurance (first prints); Medium on equities (n=1 per event); Medium on the live placement (attempts-only evidence, changing hourly).
- **If I had more time/tools:**
  - PCS subscription data.
  - A regression-based event study with a peer-group benchmark.
  - A systematic sweep of 8-K Item 1.05 filings for PHP2Shell over the next 4 weeks.
  - A re-run of the escalation checklist on ~29 Oct and ~5 Nov.
- **Suggestions:**
  - Add an `event_window.py` helper to `scripts/` (yfinance windows plus S&P adjustment; written in scratch this run; Will-gated build).
  - The KEV and NVD pulls are good WALTER watch automations.
