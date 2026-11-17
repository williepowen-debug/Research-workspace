# CYPHER record — Optimizely supply-chain compromise and the "six outages in six days" list (2026-11-17)

**Session:** PROME summons (prome-19, Claude Code on the desktop), bounded, on WALTER cards SIG-W-20261117-008 and -011 (PRIORITY, ACTION). Runtime Claude Code, Opus 5.5 (claude-opus-5-5). Started 2026-11-17 12:28 ET (boot.py wall clock 12:29). $0. Reads only: public pages fetched with curl (plain client string) and WebSearch. No system scanned or probed.

**Guardrail 2:** this file holds institution names; packets carry counts and point here.

## 1. Optimizely Web Experimentation compromise (CYB-INC-073)

### 1.1 What is confirmed, and by whom

| Claim | Grade | Source, date |
|---|---|---|
| An unauthorized party exploited a vulnerability in Optimizely Experimentation and added malicious JavaScript to "some customer projects"; Optimizely says it fixed the flaw, removed the injected code, secured affected user accounts and added protections | **CONFIRMED · PRIMARY-VERIFIED** | Optimizely status page JSON (status.optimizely.com/api/v2/incidents.json, read 2026-11-17 ~12:31 ET): incident "Web Experimentation Security Incident", created 2026-11-17 01:02:57Z (20:02 ET 11/16), status **monitoring**, resolved_at null, impact field "none", component "Web Experimentation - Snippet Delivery" operational. One update only, as of the page's 16:39Z refresh |
| The flaw was in the account sign-up flow | CLAIM (vendor spokesperson, via press) | Optimizely spokesperson to Gizmodo, as relayed by StepSecurity (update 11/17 07:30 UTC) and card 008; not on the status page |
| 178 organisations, 188 infected snippets out of 1,611 checked; 32 in banking and finance (the largest sector) | **CONFIRMED as the researcher's count · ARTIFACT-VERIFIED by Report URI, not by CYPHER** | Scott Helme, Report URI blog, 16 Nov 2026 (blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/, read 12:30 ET); every infected file archived with headers, SHA-256 and fetch time per the post. Helme: "The real number is likely higher" (only snippets found in time were checked). Optimizely has not published a count (SecurityWeek 11/17 05:22 ET) |
| Window: first injection 04:21 UTC 11/16 (BBC snippet); card skimmer added 13:43 UTC; 186 of 1,611 infected at the 19:24-19:59 UTC sweep; 1 of 188 still infected at 21:52 UTC; all clean from 23:11 UTC 11/16 | Researcher's timeline (ARTIFACT basis, researcher's) | Report URI post and its 17 Nov 09:17 UTC update. About 19 hours from first injection to all clean. **Card skimmer live ~9.5 hours** (13:43 to ~23:11 UTC), less where a site was cleaned earlier |
| Payload: crypto-address swapping; card skimming (card number, expiry, CVV typed into a site's OWN form fields, sent to 1688360.cc/card.php; cards in hosted iframes such as Stripe or Adyen out of reach); cookie (non-HttpOnly) and screenshot theft next to wallet or payment wording; iOS exploit-kit delivery (Coruna, DarkSword) | Researcher's analysis | Report URI. Hudson Rock (via SecurityWeek 11/17): connection to exploit-kit delivery infrastructure; "does not establish a zero-day, successful device exploitation, or collection of specific device data" |
| Crypto stolen: about $7,150 to attacker wallets, emptied 04:11-05:39 UTC 11/17 | Researcher's on-chain reading | Report URI update 11/17 09:17 UTC ($5,489 BTC + $760 LTC + $719 TRON + $101 ETH + $82 BSC) |
| Cards skimmed, cookies stolen, devices exploited | **NOT ESTABLISHED** | Helme: "We have no way to see how many credit cards were skimmed, how many cookies or screenshots were stolen, or how many iOS devices were infected" |
| How a sign-up flaw gave write access to many unrelated customer projects | **NOT ESTABLISHED** | Optimizely has not said (StepSecurity 11/17 07:30 UTC; Report URI) |
| Contained | **CLAIM (vendor) + researcher's observation agree; vendor still "monitoring"** | Code removed per Optimizely; files clean since 23:11 UTC per Report URI; payload domain 1688360.cc on registry clientHold 00:37 UTC 11/17; one iOS router domain still resolving at 09:17 UTC |
| Same actor, other channels: same injector code through Kissmetrics, StorifyMe and Minute Media scripts from 11/13 | Researcher's claim (Report URI, Hudson Rock) | Hudson Rock: shared hosting and loader code do not prove one operator. One of those earlier sites is a Philippine bank's site (securitybank.com, per Report URI) |
| Attribution | NOT ESTABLISHED | No researcher or government attribution (Matt Security; Report URI ties the cash-out address to its own March and 11/03 cases) |
| Optimizely had a separate February 2026 incident (voice phishing) | SECONDARY | SecurityWeek 11/17; UpGuard summary |

### 1.2 Financial firms on the researcher's list (names stay in this file)

Report URI's Banking & Finance sector, 32 organisations (as the researcher groups them; several are one company's country sites):

- **US banks (2):** HSBC US (www.us.hsbc.com), Associated Bank (www.associatedbank.com, a US regional bank).
- **US consumer credit bureau (1 company, several sites):** Equifax, incl. my.equifax.com and **signin.my.equifax.com** (a sign-in page), plus Equifax Canada, Equifax UK, The Work Number (Equifax's employment and income verification service, used by lenders).
- **US consumer and small-business lenders (3 brands):** CashNetUSA, NetCredit, OnDeck (all Enova brands per public company information; CYPHER did not re-read Enova's filings).
- **Other US finance (4):** Paychex (payroll), SmartAsset and SmartAdvisor Match (advice marketplace), TaxAct (tax software).
- **Non-US:** 12 HSBC country sites (Hong Kong, Mexico, Singapore insurance, Australia, UAE, Malaysia, Taiwan, Vietnam, Egypt, Philippines) and Hang Seng Investment; ABN AMRO (three sites) and ABN AMRO Lease; S-Pankki (Finland); ICS Cards (NL); Funding Circle; Rest Super; Compare Club; Energy Scout.
- **Separate sectors on the same list:** Crypto & Trading 6 (Ledger, IG, OANDA / Coinpass, interactive investor, TMS Brokers); Insurance 6 (Asurion, Mutual of Omaha, Admiral, Securian Financial, eRenterPlan).

**Who names them:** Report URI only, from its archived files. **No named financial firm has made a statement found by CYPHER** (searches 11/17 12:3x ET for HSBC, Equifax statements: none). Report URI says HSBC's content-security policy blocked the remote script, but the embedded fallback copy ran through `eval` because Optimizely's documentation tells customers to allow `unsafe-eval`. Whether any listed site takes card numbers in its own form fields is NOT established (a bank's public marketing site usually does not; a lender's application form or a tax-software checkout might).

### 1.3 What it means for banks and bank vendors on CYPHER's record

- **Not a compromise of any bank's own systems.** The poisoned code ran in visitors' browsers from Optimizely's content network (Report URI: "without its own code or infrastructure ever being breached"). Exposure is customer-side: card data typed into a site's own forms during the ~9.5-hour skimmer window, non-HttpOnly cookies, crypto addresses, iOS devices.
- **No chokepoint row held this supplier class** (third-party script and experimentation platforms that write code into institutions' customer pages). Added as CHK-42 (class row), CONFIRMED-OFF-WAVE.
- **No link to WAVE-2026-10 (PHP2Shell):** different vector. No escalation row fires (§3).
- **No link to the Chase outage (CYB-INC-072):** Chase, JPMorgan, Wells Fargo, Bank of America, U.S. Bank, Truist, Capital One, Schwab and Zelle are absent from Report URI's list (grep of the post, 0 matches).
- **Unknowns that gate the consequence:** how many cards and sessions were taken; whether the sign-in page cookie capture yields account takeover; whether any listed US firm files a breach notice (state attorney-general portals) or an 8-K.

## 2. The outage list (card 011) and NSA Net

| Date | Item | Grade | Best source reached | Cause as stated |
|---|---|---|---|---|
| Nov 11-12 (into 11/14) | Microsoft 365 global outage | **CONFIRMED** (SECONDARY, Microsoft via AP and The Register; CYB-INC-071, 11/14) | CYB-INC-071 | Microsoft: an issue during an earlier network capacity upgrade; "not related to cyber" or AI agents. Newsweek 11/17: Microsoft EVP pointed to increased loads and reduced server capacity |
| Fri Nov 13 | FAA nationwide ground stop, more than four hours, lifted 20:15 ET | **CONFIRMED** (SECONDARY) | CNN 11/17 (NSA story): "The Federal Aviation Administration traced the problem to a single router in Arkansas"; search summaries of Fox affiliates and KATV: a new router at the El Dorado, Arkansas site installed by L3Harris (FAA telecom contractor) shortly before; FAA Administrator Bedford: "faulty equipment" (CBS via search) | Equipment fault; officials: no indication of a foreign cyberattack, FBI investigating (search summary). Not read at FAA. SecurityWeek headline: "No Signs of Hacking in FAA Ground Stop as FBI Reportedly Probes Software Update" (title only) |
| Sun Nov 15 | AWS US-EAST-1 | **CONFIRMED · PRIMARY-VERIFIED** (the item WALTER could not find) | AWS Health Dashboard history JSON (history-events-us-west-2-prod.s3.amazonaws.com/historyevents.json, read 11/17 ~12:33 ET): "[RESOLVED] Increased Connectivity issues in US-EAST-1" | AWS: "Between 3:05 AM and 6:10 AM PST" (06:05-09:10 ET) signup errors, authentication issues (IAM Identity Center) and connectivity issues; authentication mitigated 5:20 PST; a subset of Network Load Balancer customers in one cell of use1-az1 until 6:21 AM PST (09:21 ET). **No cause stated; cyber neither stated nor denied.** A Sunday early-morning event of about 3 hours |
| Mon Nov 16 | Chase (others listed by users) | **CONFIRMED (Chase)**; CYB-INC-072 | Chase statements 11/16 (RECORD 2026-11-16); **new 11/17:** a JPMorgan Chase spokesperson to Newsweek: "temporary issue related to a software bug in on-premise hardware systems", not cyber-related; delays at other banks "stemmed from transactions involving Chase" (newsweek.com 12725688, read 12:34 ET; one outlet, SECONDARY) | Software bug on JPMorgan's own hardware, per JPMorgan. Newsweek: outages "had eased by Monday night" (Newsweek's words, not a bank statement). Capital One newly listed by users in Newsweek |
| Mon Nov 16 | United Airlines | **CONFIRMED** (SECONDARY, United statement to CNN) | CNN 11/16 (read 12:33 ET): about 30 minutes, fewer than 150 flights (spokesperson Leslie Scott); acknowledged just before 17:00 ET, resolved an hour later; "no indication that the outage was a cybersecurity-related issue"; FAA: "not an FAA equipment issue" | Cause not disclosed; not cyber per United |
| Tue Nov 17 | NSA Net (NSA's classified internal network) | **REPORTED · SECONDARY** (CNN, unnamed sources) | CNN exclusive, read 12:31 ET: down "according to **six** people familiar with the matter" (card said five; the article now says six); "At this point there is no evidence of a cyberattack, sources said"; staggered arrivals; CNN asked NSA for comment | No cause; no NSA statement found |

**Same-week relays:**

| Relay | Grade | Source |
|---|---|---|
| DHS Secretary said AI may be behind the outages | **CONFIRMED that he said it; the AI cause is a CLAIM with no evidence offered** | America News Nation 11/17 (read): Mullin on "Hannity" Monday night quoting an unnamed tech source: "I believe that it's the SI" (super intelligence); the explanation "kind of makes sense" to him. Same article: CISA "has not seen traffic pointing to a cyberattack and views the incidents as individually unrelated"; Mullin "98% certain" not a cyberattack. Newsweek 11/17: "I can tell you with 98 percent certainty that we're not seeing [a] cyberattack... we're not seeing the footprints going in, we're not seeing the footprints going out"; "Authorities have not identified a common cause". On Sunday he blamed a "50-year-old system" |
| Charles Schwab website down (@WatcherGuru 15:30Z) | **NOT ESTABLISHED** (no outlet found) | WebSearch 11/17: no report dated 11/17 |
| "Bank of America confirms $0.00 balances" (newsletter headline in search) | **NOT ESTABLISHED** | Page returns 404; no bank statement; stays on the 072 do-not-relay list ("balances wiped to zero") |
| Fugaku hacked | Not checked (Japan, no financial channel; SAM's region) | — |
| Deutsche Bank 15mn-file leak (cards 006, 009) | **NOT ESTABLISHED as a cyber event** | One search: no report of the leak's mechanism; July 2026 Unsafe ransomware claim was a third-party breach per the bank's spokesperson (SECONDARY). HANS owns the bank; CYPHER opens a row only if the leak is shown to be a breach |
| Michael Flynn "massive cyber attack" post | OPINION, no evidence | Newsweek 11/17 |

## 3. One story or several?

**On the evidence: several.** No link between any two items is established.

- **Causes differ where stated:** Microsoft, a network capacity change; FAA, one router at one Arkansas site after a contractor install; JPMorgan, a software bug on its own on-premise hardware; United, undisclosed but "no indication" of cyber; AWS, undisclosed; NSA Net, undisclosed, "no evidence of a cyberattack" per CNN's sources.
- **No shared supplier is established.** Chase says on-premise hardware, not cloud; the AWS event ended at 09:21 ET Sunday, a day before Chase's ~09:53 ET Monday start; FAA's is a telecom router; Microsoft's is its own network.
- **The government's own read is "individually unrelated"** (CISA, as relayed by the DHS Secretary). The DHS AI remark is an unnamed source's theory, not a finding.
- **Optimizely is a real cyberattack but a different kind of event** (content injection into websites, not an outage); none of the outage operators is on its victim list.
- **Base rate caution:** big US IT failures are common enough that six in six days, chosen after the fact by a poster from all US outages, is not evidence of a link. The list is selected ('unexplained' is the poster's word; three of the six had a stated non-cyber cause or denial when posted).

**What CYPHER would need to call it one story** (any one of these, at a primary):
1. A named common supplier, software release, certificate or network path across two or more of the outages, stated by an operator or in a post-incident report (Microsoft's report is due ~11/27).
2. A government statement (CISA, FBI, NSA) or operator statement that a cyber cause is under investigation for two or more items, or that CISA's "individually unrelated" view has changed.
3. A claim of responsibility that is corroborated (indicators, a leak, or an operator's confirmation), not merely posted.
4. Forensic detail in two incidents showing the same intrusion tooling or actor.

## 4. Read against CYPHER's own written rules

| Rule surface | Moved? | Why, by its own letter |
|---|---|---|
| ESCALATION_WATCH WAVE-2026-10, rows 1-9 | **No row fires.** Row 8 re-dated 2026-11-17, NOT-FIRED | Row 8 is "loss-of-service outages outside Japan at banks or payment systems" inside the PHP2Shell wave; Chase is operator-confirmed but now has a stated non-cyber cause (software bug on own hardware) and no PHP2Shell link. Optimizely is not a WAVE-2026-10 vector, so rows 1 and 3 do not move. Rows 1, 3, 4, 5, 6, 7, 9 not re-read today; their 7-day clock runs to 11/19 |
| 072 re-card triggers (WALTER cards 008, 010) | **None fired** | Cyber cause: no, JPMorgan names a non-cyber cause and CISA (via DHS) sees no cyber traffic. Named shared provider: no, JPMorgan says other banks' delays came from transactions with Chase, i.e. one origin, not a shared vendor. Rail outage statement: none. Two or more banks out into Tue 11/17: none found (WALTER also found none; BBC's 11/17 title read as the 11/16 event). Wrong balances confirmed by a bank: none |
| VX-CYP-05 software supply chain and trust | **3 to 4 (YELLOW to ORANGE) on the letter** | ORANGE letter: "A CONFIRMED poisoning or trust-chain break with a named financial-sector victim or trading-software outage". Optimizely confirms the poisoning at its own status page; the discovering researcher names financial-sector victims from archived files. RED weighed and NOT met: "A poisoned update in a product run by many financial firms (the SolarWinds shape)" — the shape named is an attacker foothold inside the firms; here the code ran in visitors' browsers for ~19 hours and the firms' own systems were not reached on any evidence. ⚠️ COMPOSITION, not damage: no loss figure exists; the move says a confirmed supply-chain poisoning reached named financial firms, nothing about systemic risk. Independent root (off-wave) |
| VX-CYP-01 bank / core-vendor compromise | No (holds 3) | Keyed to the wave (rows 3, 4) and to a bank or core vendor being compromised; no bank's own systems were compromised, and off-wave cases do not move it (row note 11/05) |
| VX-CYP-02 payment and market-infrastructure availability | No (holds 3) | YELLOW includes "an outage under one business day at a single listed operator"; the Chase outage started ~09:53 ET and eased by Monday night (Newsweek), and ORANGE needs one business day or more or watch row 8 FIRED |
| Composite | **Raw 24/40 to 25/40; shared-root-adjusted 15/40 to 16/40** | VX-05 +1, off-wave own root |
| FLOW | No state change | FL-CYP-22 is own-funds theft through one provider at several banks: not this mechanism (customer-side skimming). FL-CYP-01 already CONFIRMED (MOVEit) |
| PREDICTIONS CYP-01..08 | None moves | CYP-02 and CYP-07 need a WAVE-2026-10 vector; CYP-01 counts Item 1.05 8-Ks (none from these events, boot leg 8 at 12:29 ET); CYP-03 needs an MSP/RMM route; CYP-05/06 are Arkéa |
| R1 flip test (11/20) | No | Needs a named PHP2Shell victim (row 1 or 3) |
| Catalyst 2026-11-19 cluster watch | Not answered by its letter; stays on 11/19 | Its escalate limbs are bank-core, CU-vendor or payment-messaging suppliers, or one outage disrupting 2 or more institutions for 1 business day or more. Optimizely is none of those suppliers; Chase was under one business day. Its 11/16 add-on questions on 072 are partly answered (cause stated by JPMorgan, eased Monday night per Newsweek; no 8-K, no wrong balances) and noted on the row |
| Catalysts 11/18 and 11/19 rows | Stay on their dates | Nothing in this read answers one by its own letter |

## 5. Do not relay

- "Six outages in six days are one attack" or "linked" (no link established; CISA via DHS: individually unrelated).
- "AI caused the outages" as a finding (an unnamed source's theory relayed by the DHS Secretary).
- "Banks were hacked through Optimizely" (the vendor's script ran on banks' public web pages; no bank's systems are reported breached).
- "Card data stolen from HSBC or Equifax customers" (the skimmer was present; no count of cards taken exists, and whether those pages take card numbers is not established).
- "NSA hacked" (CNN's sources: no evidence of a cyberattack).
- "Schwab down 11/17" (no outlet found).
- "AWS outage on 11/15 is unverified" — it is now verified at AWS's own dashboard; carry it as a 3-hour Sunday-morning US-EAST-1 sign-in and connectivity event with no cause stated.

## Sources (read 2026-11-17, 12:29-12:35 ET unless noted)

- status.optimizely.com/api/v2/incidents.json (PRIMARY)
- blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/ incl. 17 Nov 09:17 UTC update (researcher primary)
- helpnetsecurity.com/2026/11/17/optimizely-vulnerability-malicious-javascript/
- securityweek.com/optimizely-vulnerability-exploited-to-serve-malware-on-major-websites/ (11/17 05:22 ET)
- stepsecurity.io/blog/optimjack-optimizely-hosted-scripts-crypto-clipper-card-skimmer (update 11/17 07:30 UTC)
- technology.org (403, left alone); isdown.app (403, left alone)
- cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down
- cnn.com/2026/11/16/us/united-airlines-outage
- history-events-us-west-2-prod.s3.amazonaws.com/historyevents.json (AWS Health Dashboard history, PRIMARY); health.aws.amazon.com/public/currentevents (2 events, none relevant); drweb.de AWS article (11/15 13:49 CET snapshot)
- americanewsnation.com/2026/11/17/dhs-secretary-mullin-floats-ai-theory-behind-string-of-nationwide-tech-outages/
- newsweek.com/dhs-says-ai-could-be-responsible-outages-faa-aviation-ground-stop-banks-12725688
- WebSearch result summaries (not opened): FAA router coverage (Fox affiliates, KATV, ky3.com 11/14), United (CBS, NBC, Time), Schwab, Deutsche Bank, HSBC/Equifax statements
