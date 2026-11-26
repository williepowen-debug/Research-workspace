# CYPHER — 2026-11-26 due-row wake and inbox drain (PROME prome-80, C6, WQ-184)

**Session:** Thu 2026-11-26 (Thanksgiving, NYSE closed), boot 11:06 EST (boot.py wall clock). Runtime Claude Code, Opus 5.5 (claude-opus-5-5); WebSearch and WebFetch loaded on demand; no subagents used. $0, no accounts, no external sends. Boot reads: root CLAUDE.md 4 pages, AGENTS.md 1, USER.md 3, AGENTS/CYPHER/CLAUDE.md 4, each to eof via PROME/tools/boot_read.py.

## 1. Boot

- `git pull --rebase`: up to date (tree clean at pull).
- boot.py rc 1 REVIEW: catalysts due (2 today, 2 past, 1 tomorrow); re-checks due CYB-INC-005, -019; leg 9 flagged Elmet Group (ELMT) and SBC Medical (SBC) 8.01 filings; leg 10 listed N-able, TruStage, Finastra settlement, Kaseya leads. Leg 7 KEV v2026.11.25 (1,805 entries) LIVE; leg 8 LIVE, no Item 1.05 8-K since 11/19.
- corrections_boot_check rc 1: three NAMED corrections unreceipted (COR-20261120-10, COR-20261123-23, COR-20261124-21); receipted this session (§8).
- Leg 9 flags, disposition: Elmet Group and SBC Medical Group are a manufacturer and a Japanese aesthetic-clinic group, neither a bank nor a financial vendor; filings not opened (desk rule: leg 9 asks "bank/vendor?" first). No REVIEW carried.

## 2. Row: Abrigo Sageworks follow-up (CYB-INC-060), due 11/26 — CONSUMED, RE-DATED 12/03

| Check | Reading | Basis |
|---|---|---|
| status.abrigo.com/history.rss (read 11:08 EST) | Incident "Borrower-facing functionality is unavailable" still open; latest update **Nov 25 13:55 EST**: "We are continuing to monitor for any further issues." Prior: Nov 16 14:45 "remain unavailable as we work with an external firm to complete platform testing". Patching window Nov 21-22 completed | PRIMARY-VERIFIED |
| Data taken, root cause | Unstated (classaction.org page, updated 11/09: "Impacted Data: TBD"; no notice letter or AG filing cited) | SECONDARY |
| HIBP "Abrigo" | April 2026 Salesforce extortion (ShinyHunters), 711.1k addresses, added 14 May 2026: an earlier incident, not Sageworks | PRIMARY (HIBP page) |
| State AG portals | CA AG list page 1 (of 109): no Abrigo entry. **Maine AG viewer returned HTTP 403 to the fetch tool: a block, not bypassed.** WA, TX, VT not read | partial |
| Any institution stating disruption | None found | search |

Threshold: none met. Borrower-facing features down 10/30 to at least 11/25 (27 days). Re-dated 12/03 to ride with the cluster watch.

## 3. Row: Bank-vendor and payment-plumbing cluster watch, due 11/26 — CONSUMED, RE-DATED 12/03

New CONFIRMED incidents or outages at bank-core, CU-vendor or payment-messaging suppliers since 11/19: **0**. Outage limb (2+ institutions, 1 business day+): **not met**.

| Item | Facts | Basis | Counted? |
|---|---|---|---|
| VSoft (Duluth GA; core and digital banking for CUs and community banks) | Reddit r/cybersecurity post 11/24 via Govly: ransomware took down "many" web servers; core, ACH, wire, ATM and mobile services disrupted; entity unclear. vsoftcorp.com shows no notice (latest news 2025-08-19). No VSoft, NCUA or press statement found | REPORTED, community post only | **No** (single claim). New CYB-INC-094 |
| Best Egg (Barclays-owned personal-loan platform) | CA AG filing (reported 11/24): breach 10/25-10/26 on the Best Egg Financial Health platform; notice letter: name, date of birth, SSN, the account number used to pay the loan; "we have not detected any fraud". 791,852 people per the Texas AG portal (relayed by CyberInsider 11/26) | PRIMARY-VERIFIED (letter); count SECONDARY | No: the lender itself, not a supplier. New CYB-INC-092 |
| Barclays Bank Delaware | CA AG filing (reported 11/24): breach window 11/05/2025 to 11/04/2026; letter: suspicious activity detected 11/04/2026 on the online tool that lets card applicants check application status; name, contact, DOB, SSN; existing accounts not affected. 27,272 per Texas AG (CyberInsider). Barclays: unrelated to Best Egg | PRIMARY-VERIFIED (letter); count SECONDARY | No: the bank itself. New CYB-INC-093 |
| FinCEN | see §7 | | No: a regulator, not a supplier. New CYB-INC-090 |
| MeridianLink | Search returned only the November 2023 ALPHV claim: a date trap, not a 2026 event | — | No |
| Sharetec outage | September 2026 (cooling failure), already 050 | — | No |

Abrigo (confirmed 11/02) stays inside 30 days to 12/02, so the count is above zero: weekly, 12/03. Add VSoft confirmation to that look.

## 4. Row: Arkéa provider and shared-reach weekly check (CYB-INC-059), due 11/23 — CONSUMED LATE 11/26, RE-DATED 12/03

- cm-arkea.com press page (read 11/26): November items are the two 11/04 attack releases, 11/13 Route du Rhum, 11/25 and 11/26 foundation releases. **No third statement.** Provider not named by the bank.
- Searches (FR): Paris prosecutor's cybercrime section opened an inquiry on the bank's complaint (France 24 11/04, AFP); provider identity not revealed; no second institution, no ACPR, ECB, EBA or CERT-FR statement found. Les Echos 11/14 naming (unconfirmed) unchanged.
- Nothing met. No HANS, LIQUID, REGINALD or GIBBS packet. CYP-05 resolves in the 12/29-12/31 window.

## 5. Row: Optimizely follow-up (CYB-INC-073) with N-able, JPMorgan, MUFG/PLAID adds, due 11/24 — CONSUMED LATE 11/26, RE-DATED 12/08

| Item | Reading | Basis |
|---|---|---|
| **CISA KEV** | **CVE-2026-132224, Optimizely Web Experimentation, dateAdded 2026-11-24, due 2026-11-27** (KEV v2026.11.25) | PRIMARY-VERIFIED (KEV JSON) |
| status.optimizely.com | Still "Unresolved". Latest 11/18 14:49 UTC: a flaw in the account signup flow let the party "impersonate users on targeted customer accounts and insert malicious JavaScript"; vulnerability closed within three hours of detection; "not a credentials breach"; limited to Web Experimentation; "Less than 5% of our customers were impacted"; every customer contacted | PRIMARY-VERIFIED |
| Listed US financial firms | No breach notice, card-fraud statement or 8-K citing Optimizely found (CA AG list page 1; trade-press searches). Researchers: number of cards skimmed unknown | search, partial |
| N-able 085 | N-able blog 11/22 14:30 EST: dashboard and APIs restored **11/21 23:45 UTC**; CVE-2026-134624 (KEV 11/23, due 11/26); "no evidence of exploitation beyond the single N-able-hosted server"; formal RCA "within the next two weeks". Credential statement not on that page; a secondary relays "may have been able to access certain credentials stored on the platform" with API/OAuth token revocation | PRIMARY (blog) / SECONDARY (credentials) |
| JPMorgan 086 | American Banker headline "Vendor attack exposes JPMorgan Reserve cardholder emails" (body not read); vendors still unnamed; no count, no 8-K | SECONDARY title |
| MUFG/PLAID 089 | No PLAID notice naming a flaw found after 11/20 (JP search) | search |

Threshold: none met (no firm states card fraud or a notice; Optimizely's mechanism statement is not broader access than 178 organisations). VX-CYP-05 and CHK-42 not re-read on the letters. Re-dated 12/08: N-able RCA (~12/06) and the 30-60 day notice window for Optimizely's financial customers.

## 6. Row: Microsoft 365 post-incident report (CYB-INC-071), due 11/27 — CONSUMED EARLY, RETIRED

- Preliminary post-incident report published in the admin center 11/15-11/16 (BleepingComputer 11/16, read): "a previously undetected software bug, increased traffic after a Microsoft Teams failover, and reduced server capacity"; the bug from a July update to Microsoft 365 networking gateway servers. No authentication, Entra or Azure component named; no cyber cause; no bank, payment or market effect named. Final report (due ~11/20 per secondaries) not read.
- WALTER 20261124-018 item 7: Microsoft's "Code Red" memo concerns the same outage; Reuters: "no indication" of a cyber cause.
- Row rule: "Network-change cause confirmed and nothing named -> close the row." Met on the preliminary report (SECONDARY read). Row retired; 071 stays CONFIRMED INFRA-OUTAGE.

## 7. Inbox items that opened rows

**FinCEN (CYB-INC-090).** Notice on the BSA E-Filing site, posted Tue 11/24 evening (quoted by The Record and Nextgov 11/25, both read): "investigating a cybersecurity incident" that "resulted in unauthorized access to a limited subset of its systems"; "As a proactive measure, FinCEN has taken some systems offline"; E-Filing site operational, some services unavailable. FinCEN spokesperson (The Record): "no evidence of any breach of the Bank Secrecy Act or beneficial ownership databases"; FBI and CISA involved. Order FIN-2026-R002 (read at fincen.gov by WALTER, not re-read by CYPHER; Nextgov describes it): filers who used the automated batch channel as of 11/18 file reports due 11/18-12/29 by 12/30. No actor; no stated link to the CIA/ODNI, FBI NCIC or USDA events (Nextgov: "Officials have not publicly linked those breaches"). Money channel: delayed batch BSA filings; SAR confidentiality only if the spokesperson's "no evidence" changes. Not a payment or settlement system.

**1Password (CYB-INC-091).** Company post 11/25 (read): investigation began 11/19; attacker used an employee's corporate GitHub account, copied private source code, gained CI/CD access, pushed malicious code to backend services that downloaded account records for "a subset of our users" (names, emails, IDs, public keys, SRP parameters, invitation, provisioning and recovery tokens). Not affected per the company: vaults, vault keys, recovery keys, apps, extensions. No count, no customer named. Reaches no CHOKEPOINTS row (Okta CHK-18 is the only identity row): logged, stays low.

**Best Egg (092) and Barclays Bank Delaware (093):** §3. Two separate breaches inside one US banking group within ten days, both customer-facing web applications, both data theft (SSNs), no funds or service disruption stated, no PHP link stated by either letter. Routing table: a named US bank CONFIRMED victim -> REGINALD, GIBBS, PROME, P1 (sent).

**VSoft (094):** §3, REPORTED only.

## 8. Corrections receipts

| ID | Action | Why |
|---|---|---|
| COR-20261120-10 (MUFG 6.5M is real) | APPLIED | CYPHER authored the underlying correction 11/20; CYB-INC-089 carries it |
| COR-20261123-23 (Araghchi; DNI quote; Delta) | NO-OP | No CYPHER row cited the DNI quote as NOT FOUND or the Delta item; Iran lines are FALCON's |
| COR-20261124-21 (CIA/ODNI reported) | APPLIED | KB-CYP-148 federal-intrusion run records it as reported and source-confirmed |

## 9. Escalation watch, 7-day pass (WAVE-2026-10, all open rows due by 11/26)

| Row | State 11/26 | Reading |
|---|---|---|
| 1 | NOT-FIRED | Dutch NCSC alert "Bijgewerkt: 23 okt 2026 om 15:43" unchanged, no victim named; search: no named PHP2Shell victim |
| 3 | NOT-FIRED | Best Egg and Barclays Bank Delaware are confirmed US banking-group victims but neither letter states PHP; no named core-vendor victim; VSoft unconfirmed |
| 4 | NOT-FIRED | boot leg 8 LIVE: no Item 1.05 8-K since 11/19; control 15 in 120 days |
| 5 | NOT-FIRED | NYDFS letters page: new cyber letter **11/21 "Active Threat Campaigns Using ARTEX Agentic AI Framework"** (read): "Recent threat intelligence has identified ARTEX-related attacks involving unauthorized access and data exfiltration"; no exploitation at regulated entities stated, no PHP, no deadline ("encourages"). Does not meet the row's fire test |
| 6 | NOT-FIRED | No PCS designation or modeler estimate found in November (search) |
| 7 | NOT-FIRED | No US/UK/EU government attribution of PHP2Shell found |
| 8 | NOT-FIRED | No operator ties a bank or payment outage to PHP patching; VSoft claim unconfirmed and not tied to PHP |
| 9 | NOT-FIRED | Reading only, HENRY's grade unchanged (collapse leg spent 11/18): 11/25 closes HACK $120.40, PANW $356.14 (FORGE fetch.py, read 11/26, marked stale because markets were closed 11/26); no sector gain persisting |

## 10. Incident re-checks

- CYB-INC-005 (Japan "emergency"): government announced an emergency cybersecurity package 11/06, ¥10B initial, public-private "cyber rescue team" (AP via local syndication, search summary). ITPro still frames 10/09 as a declaration; the row's PRIMARY reading (party remark, no declaration) stands. REPORTED, re-checked.
- CYB-INC-019 (banks restricting AI agents): no November reporting; October coverage unchanged (Morgan Stanley: no "rogue AI agents" observed). REPORTED, re-checked.

## 11. Client name (WQ-735)

boot.py leg 10 now sends `research-bot/1.0` to news.google.com RSS (was "Mozilla/5.0 (CYPHER boot leg 10)"). `scripts/test_boot.py` 36 tests OK. Re-run: leg 10 LIVE, 6 chunked queries parsed, 106 items in 30 days (130 under the old string an hour earlier: the feed's result set differs by client or by time; not investigated). No refusal. The SEC declared-contact string (legs 8, 9) unchanged. Ad hoc pulls this session (KEV JSON, Abrigo RSS, CA AG PDFs) also used `research-bot/1.0`.

## 12. Trade read

Nothing material for TERRY. Best Egg and Barclays Bank Delaware are data theft at one large bank group's US consumer units (~0.82M people combined, Texas AG counts), no funds taken, no outage; FinCEN is a regulator's filing system with a filing-deadline relief order. None meets the bar the launch brief names (a confirmed incident at a core vendor or payment processor with named customer banks). No packet to TERRY.

## 13. Forward view (material items only)

- **FinCEN.** Expect: the incident stays an administrative disruption (late batch filings to 12/30) and joins the November run of federal intrusions without a public attribution inside two weeks. Why: the spokesperson's "no evidence" on the BSA database and the relief order's narrow scope. Alternative: FinCEN or Treasury states that BSA or SAR data was accessed; that would be a bank-confidentiality and supervisory event (REGINALD, GIBBS), still not a funding event. Horizon: to the 12/30 filing date. Changes my mind: any FinCEN statement naming data taken, a CISA emergency directive, or an attribution tying FinCEN to the CIA/ODNI intrusion.
- **Barclays pair.** Expect: litigation and notification cost, no service or funding effect; Barclays says the two are unrelated. Alternative: a third Barclays US incident or a shared vendor named, which would make it a supplier route (FL-CYP-22). Horizon: 30 days. Changes my mind: an 8-K-equivalent RNS from Barclays or a regulator statement.
