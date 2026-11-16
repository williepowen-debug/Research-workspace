# RECORD — US bank login outage, Mon 2026-11-16 (CYB-INC-072, card SIG-W-20261116-006)

**Session:** CYPHER, PROME summons (WQ-369 class, IMMEDIATE card), PROME session prome-6f. Runtime Claude Code, Opus 5.5. Research window 13:50-13:55 ET (wall clock from `date`). $0.
**Method:** web search (extended) plus page reads through a web-fetch subagent (one GET per page, no login, no forms, no probing of any bank system: guardrail 1). Downdetector could not be fetched (tool refused the domain); Men's Journal, TradersUnion 403; SF Chronicle served a bot challenge; X/Twitter not read directly.

## 1. What is confirmed, and by whom

| Firm | Claim | Who says it | Basis (Class 12) |
|---|---|---|---|
| JPMorgan Chase | Online banking issue, being worked on | @ChaseSupport post dated 2026-11-16: "it appears that we are currently working to resolve an issue with online banking" (embedded in NBC Chicago; also Cedar News) | SECONDARY-SOURCE (bank's own post, read through NBC Chicago's embed; X not read at source) |
| JPMorgan Chase | "due to a technical issue, some transactions are taking longer than usual to complete"; "customers still have access to their accounts and funds" | Chase to NBC Chicago (no spokesperson named, no time) | SECONDARY-SOURCE |
| JPMorgan Chase | In-app banner: "Some services aren't available. We're working on them. Please try back later." | AP (via KTAR, 11:43 AM) and Newsweek | SECONDARY-SOURCE |
| JPMorgan Chase | "this is a Chase issue" | Chase to NBC Chicago, per the fetch reader; the paragraph's attribution is UNCERTAIN (it sits between unrelated page elements and does not clearly refer to Zelle) | SECONDARY-SOURCE, attribution uncertain |
| Wells Fargo | "online banking is temporarily unavailable"; ATMs, branches and phone bankers available | Statement "on its website", per NBC Chicago (no time). **Not visible** in a static read of wellsfargo.com home page at about 13:53 ET (HTTP 200, no banner; a script-injected banner would not show) | SECONDARY-SOURCE, unverified at source |
| Bank of America | Users report login, $0 balances, mobile problems | Downdetector listings and users only; no bank statement found; Newsweek emailed the banks, no reply reported | REPORTED (user reports) |
| U.S. Bank | Users report credit card balances showing zero | Users only (yourNEWS: "did not establish any change to funds") | REPORTED (user reports) |
| Truist | Listed on Downdetector (Boston 25) | Users only. truist.com shows a fraud warning about "the Microsoft outage", not a Truist outage notice | REPORTED (user reports) |
| Zelle (Early Warning Services) | Users report transfer problems; "error reports appeared to be climbing" (NBC Chicago) | Users only. zelle.com (redirect from zellepay.com) shows no alert; no Zelle or EWS statement found; IBTimes AU: Zelle/EWS had not acknowledged an outage; spikes "can reflect issues at individual banks" | REPORTED (user reports) |

**Event_State for the ledger row: CONFIRMED** — for a Chase online-banking outage, on the bank's own words relayed by NBC Chicago and AP. The other firms are not confirmed by their operators (Wells Fargo's reported website statement is one step short: read through NBC only).

## 2. Times (all ET, Monday 2026-11-16)

| Time | Event | Source |
|---|---|---|
| ~09:53 | Chase problem reports begin on Downdetector | yourNEWS citing Downdetector |
| "shortly after 10 a.m." | more than 3,400 Chase reports | search summary (outlet not pinned) |
| 11:04 | more than 2,000 Chase reports | GV Wire via yourNEWS |
| 11:43 | AP story: Bank of America, Chase, J.P. Morgan, U.S. Bank, Wells Fargo, Zelle listed by users as down | AP via KTAR |
| ~12:00 | Chase report mix: web login 43%, balances/transactions 24%, mobile login 17%; no public Chase statement yet | Men's Journal via yourNEWS (Men's Journal itself 403) |
| 13:19 (12:19 CT) | more than 4,000 Chase error reports, Chicago a hotspot | NBC Chicago |
| 13:32 (18:32Z) | Will's bookmark (Daily Mail) | WALTER card |
| 13:42 | Boston 25: "It is not clear why"; "developing story" | Boston 25 |
| ~13:53 | Static reads of chase.com, wellsfargo.com, bankofamerica.com, usbank.com, truist.com: HTTP 200, no outage banner in the returned text | CYPHER web-fetch reader |

**Still going on?** UNKNOWN at 13:55 ET. No source reports restoration; the latest dated reports (13:19 and 13:42 ET) call it ongoing/developing. Home pages load, which says nothing about the logged-in service. Downdetector, the one live instrument, was not readable. Duration so far: about 4 hours from the first reports (09:53 to at least 13:42 ET), under one business day.

⚠️ Downdetector counts are user reports, not a measured outage size. "Thousands of reports" for each of several banks is a known pattern when the largest bank fails: customers of other banks report sympathetically, or their own transfers to and from the failing bank fail. The Chase count (2,000 to 4,000+) dwarfs Bank of America plus Wells Fargo together (about 800, NY Post via Jingletree, time not given). This is an interpretation, not a finding.

## 3. Is there a common vendor, network or payment-rail link?

None established. Checked at about 13:50-13:55 ET:

| Candidate common link | Reading | Source |
|---|---|---|
| Microsoft Azure / M365 (CHK-20; last week's CYB-INC-071) | "There are currently no active events" | azure.status.microsoft, read 11/16 |
| Google Cloud | "No broad severe incidents", last updated 10:50 PST | status.cloud.google.com |
| Cloudflare | No incident posted for 11/16 (an older Workers/Queues incident from 11/10; maintenance windows in Asia and Minneapolis) | cloudflarestatus.com |
| Akamai | One 11/16 incident, Application Load Balancer availability errors, posted 03:49 UTC, mitigated 13:37 UTC (08:37 ET), resolved: ended over an hour BEFORE Chase reports began (~09:53 ET). Timing does not fit | akamaistatus.com |
| AWS | Health page returned an empty body: UNREAD | health.aws.amazon.com |
| Fiserv (CHK-01; processes Zelle for many smaller banks) | No public status page (404); third-party tracker "operational" (stale-prone) | fiserv.com; statusgator |
| Zelle / Early Warning Services | No alert on zelle.com; no statement; "this is a Chase issue" (Chase to NBC, attribution uncertain) points away from Zelle as the source | zelle.com; NBC Chicago |

The four big banks run their own online-banking stacks; no published shared login, core or CDN vendor connects Chase, Bank of America, Wells Fargo and U.S. Bank (CHOKEPOINTS UNKNOWN-STACK applies: this is absence of a published link, not proof of independence). No CHOKEPOINTS row is touched by any primary statement.

## 4. Cyber or not

No source mentions a cyberattack and none denies one. Chase's only stated cause is "a technical issue" (NBC Chicago). ⚠️ "No cyber cause stated" is not "not cyber": the bank has not said what failed. Symptoms (login failures, delayed transactions, balances not loading, funds intact per Chase) fit an internal authentication or back-end failure, the shape of past Chase and Wells Fargo outages (authentication database; data-center power-down 2019), but that is pattern, not evidence.

## 5. Classification (charter rules)

| Field | Value |
|---|---|
| ID | CYB-INC-072 |
| Class | **INFRA-OUTAGE** (market, payment or cloud infrastructure, malicious or accidental) — cause unknown, no cyber vector stated |
| Wave_ID | OFF-WAVE (no PHP2Shell or other wave link) |
| Event_State | CONFIRMED (Chase outage, bank's own words via NBC/AP); other firms REPORTED in Notes |
| Basis | SECONDARY-SOURCE |
| Escalation | No row fires. WAVE-2026-10 row 8 (bank or payment outage outside Japan, operator-confirmed) is a WAVE row: an off-wave outage with no PHP2Shell link does not fire it (Central Bank of India and SecurCommunity precedents, 10/29 and 11/06). Row stays NOT-FIRED, State_As_Of 2026-11-16 |
| Chokepoint | none touched |

**What would change the class or the routing:**
1. **A cyber cause** (bank, regulator or law enforcement says malicious; ransomware claim verified) → re-class to RANSOMWARE-EXTORTION or the matching class; P1 to GIBBS and PROME (named US bank, confirmed victim); an 8-K Item 1.05 from JPMorgan (boot leg 8) would be the formal marker.
2. **A shared provider named** (CDN, identity, core, cloud, Zelle/EWS) → re-class SUPPLY-CHAIN or keep INFRA-OUTAGE with the CHOKEPOINTS row marked; reach becomes every client of that provider.
3. **Zelle/EWS or another payment rail confirms an outage** → the payment-outage routing row (LIQUID, BOND, PROME, P1).
4. **Operator-confirmed outage at two or more banks lasting one business day or more** (into Tue 11/17) → REGINALD's amended P2 bar; GIBBS P2.
5. **Funds wrong rather than unavailable** (balances truly zeroed, double postings) → a data-integrity event; GIBBS P1.

## 6. Do not relay

- "Nationwide bank outage at Chase, Bank of America, Wells Fargo and U.S. Bank" as one event — only Chase is operator-confirmed; the others are user reports (Wells Fargo: one outlet quoting its website).
- "Bank hack" / "cyberattack on banks" — no source says so.
- "Customer balances wiped to zero" — users see $0 displayed; Chase says customers "still have access to their accounts and funds"; yourNEWS: no change to funds established.
- "Zelle down" — user reports only; no Zelle or EWS statement; Chase's own line points at Chase.
- "Linked to the Microsoft outage" — AP mentions it as context only; Azure shows no active events.

## Sources (read 2026-11-16, 13:50-13:55 ET)

- AP via KTAR: ktar.com/national-news/customers-at-some-of-the-nations-largest-banks-are-reporting-difficulty-accessing-accounts-online (11:43 AM)
- NBC Chicago: nbcchicago.com/news/local/multiple-banks-reporting-online-banking-outages-across-u-s/4017471/
- Newsweek: newsweek.com/are-chase-wells-fargo-down-latest-update-on-bank-outages-12722872
- Boston 25 News: boston25news.com/news/trending/customers-report-chase-us-bank-zelle-others-are-down/LYYL3KX37JAGDGDPB65AS36Q24/ (1:42 PM)
- yourNEWS: yournews.com/2026/11/16/7269508/
- Cedar News: cedarnews.net/newstasks/1156593/
- Jingletree (NY Post reprint): jingletree.com/chase-bank-of-america-and-wells-fargo-customers-report-outages-in-latest-tech-hiccup-308549.html
- Sunday Guardian: sundayguardianlive.com/trending/chase-outage-today-... (21:28 IST)
- IBTimes AU (search summary only): ibtimes.com.au/zelle-users-report-payment-problems-us-1878716
- Status pages: akamaistatus.com, cloudflarestatus.com, azure.status.microsoft/en-us/status, status.cloud.google.com, health.aws.amazon.com (empty), fiserv.com service-status (404), zelle.com
- Bank home pages (static GET, no login): chase.com, wellsfargo.com, bankofamerica.com, usbank.com/index.html, truist.com
- Not readable: downdetector.com (fetch refused), mensjournal.com (403), tradersunion.com (403), sfchronicle.com (bot challenge), x.com (not attempted directly)
