# CYPHER — 2026-11-19 due-row wake (PROME prome-36, C6)

**Started:** 2026-11-19 09:47 EST (boot.py wall clock). **Record written from:** 09:53 EST. Runtime: Claude Code, Opus 5.5 (claude-opus-5-5), laptop. $0. Names stay in this file (guardrail 2); packets carry counts.

**Task (PROME launch letter, read 09:47 ET):** five 11/19 calendar rows, escalation row 9 record from HENRY's 11/18 grade, the read-cap flag under D:L1167 check (2), whole-inbox drain, the NEXUS_BRIEF charter line (WQ-719 A / WQ-721 A).

**Tools this session:** shell, git, Python, WebSearch; no direct WebFetch (page reads through `web-fetch` subagents, Sonnet-class fetchers, each report labelled below); SendMessage loaded. MCP: mtnewswire, definite, desktop-commander failed to connect. Laptop: no gh, Kalshi, CourtListener tokens (not needed).

## 1. Boot

| Leg | Result |
|---|---|
| 3 catalysts | 5 TODAY, 1 past (11/18 row 9), R1 flip test tomorrow |
| 4 watch | 9 rows inside 7 days; rows 5, 6, 9 State_As_Of 2026-11-12, due today |
| 7 KEV | v2026.11.18 (1,786 entries); 11 watched CVEs absent, incl. the 7 Able2Shell-round N-central CVEs and CVE-2026-115560 |
| 8 8-K 1.05 | none since 11/12; control 15 in 120d |
| 9 8-K 8.01 | **FAILED at boot (HTTP 500)**; re-run 09:51 ET LIVE: one incident-wording hit, SBC Medical Group Holdings (11/19, healthcare, not bank or vendor), logged; control 555 in 120d |
| 10 bank-vendor news | TruStage agreement (11/19), N-able Mail Assure breach (11/19), N-able 17 patches (11/17), Jack Henry "not financially material" (11/17, the 8/31 incident; 048 note), ConnectWise "2,250 tenants" (11/14) |
| corrections | 0 unreceipted NAMED rows |

## 2. Row: Able2Shell and MSP-tool follow-up, ONE look (CYB-INC-065/066/067) — CONSUMED, RETIRED

| Leg | Reading | Source, basis |
|---|---|---|
| N-central fixes | N-able patched 17 N-central zero-days and retired legacy APIs (SecurityWeek, Monday 11/16 per the search summary; title says 11/17 on leg 10); 2026.4 HF2 carried earlier fixes; Agent2Shell (SYSTEM on Windows agents) added by the same researcher | SecurityWeek, BleepingComputer titles and search snippets, SECONDARY |
| KEV | none of CVE-2026-125878..125883 or 91000/91403 in KEV v2026.11.18 | CISA KEV feed, PRIMARY |
| Successful compromise | already CONFIRMED 11/13 (Huntback 21 servers; N-able IOCs) | — |
| A bank, CU or bank vendor names N-central or ScreenConnect as its entry route | none found. American Banker (11/11, via search summary): Insight Credit Union's breach filings do not name the IT provider or say ransomware | SECONDARY |
| Insight's own notice | not read (Texas AG report 11/06 known only through ClassAction.org); per American Banker it names no provider. **CYP-03 not resolved by Insight** | SECONDARY |
| N-able event 202609 | uptime.n-able.com returns 403 to the fetcher (11/13 it returned 401) | — |
| ScreenConnect (066) | ConnectWise advisory, read by CYPHER with curl 09:5x ET: "ScreenConnect investigation complete — protective actions remain required", updated 2026-11-16 20:00 UTC; extensions Labtech Plus, RMM Plus, RMM+ and two Password Link variants stay disabled; technician clients must run 26.6.5+ (fix for CVE-2026-84869, KEV since 2026-09-11); "Completion of our investigation does not establish that individual partner or customer environments are unaffected." | PRIMARY-VERIFIED |

**New, separate N-able event (CYB-INC-085):** N-able Mail Assure and SpamExperts Hosted Cloud. Disruption from 11/16; first attributed to "platform configuration and service dependencies" (11/17); revised to a security incident with unauthorized access to one server (11/18 03:05 UTC, CyberPress only); 11/19 08:00 UTC restoration under way. Mail flow and filtering up; management portal, APIs, quarantine and logging offline; Americas, APAC, Europe. N-able (quoted by The Hacker News 11/19): "at this time we do not have evidence that customer data was compromised". Credentials, keys, tokens: not confirmed either way. The Hacker News says it is unrelated to Able2Shell, 4EverAble2Shell and Agent2Shell (outlet's words; N-able's status page 403). No financial firm named. Basis SECONDARY-SOURCE (vendor quoted by outlet). Fourth N-able security event since August by the CHK-38 count, and the first in a different product.

Disposition per the row's letter: no KEV listing, no bank/CU/vendor naming the route, no Insight route statement ⇒ "Nothing -> retire this row; KEV keys stay on 065." Retired. The Mail Assure event rides the 11/24 follow-up row.

## 3. Row: Abrigo Sageworks follow-up (CYB-INC-060) — CONSUMED, RE-DATED 11/26

- status.abrigo.com (fetcher read, verbatim): incident "Borrower-facing functionality is unavailable"; latest update **Nov 16, 2026 14:45 EST**: "Borrower-facing capabilities remain unavailable as we work with an external firm to complete platform testing." Online Portal "Partial Outage"; Sageworks Analyst and API "Operational". Scheduled "November 2026 Patching & Maintenance" Nov 21 18:00 to Nov 22 18:00 EST (posted 11/18).
- American Banker 11/03 14:25 EST "Abrigo confirms 'data security incident' caused 3-day outage" (Carter Pape): body not extracted; overview says Abrigo did not say whether borrower data was taken.
- Data loss: still unstated. Root cause: unstated. No institution stating a processing disruption. AG portals: **not read (again)**.
- Threshold: none met. Borrower-facing features down about 20 days (10/30 to at least 11/16).

## 4. Row: Bank-vendor and payment-plumbing cluster watch — CONSUMED, RE-DATED 11/26

New since 11/12 at the watch's supplier list (CHK-01..11, 33, 36, 37): **0 confirmed**. Count stays above zero inside 30 days (Abrigo 10/30 confirmed 11/02, in window to 11/29), so weekly.

Found, outside the list (logged, not counted):

| Item | Facts | Basis | Ledger |
|---|---|---|---|
| JPMorgan Chase vendors | JPMorgan on X 11/19 (via Fox 32 Chicago 08:30 CST): "third parties who provide services to the firm were the target of a cyber attack"; "the attackers accessed certain marketing data held by those vendors, which may include some customer names and email addresses"; "There is no disruption to our services." Spokesperson to Reuters: credit monitoring offered where appropriate; "no connection" to the 11/16 service disruption. Vendors unnamed; customer count none. n0n listed JPMorgan 11/16 (081); JPMorgan does not mention n0n. Cybernews (403) reports n0n's leak as ~16,000 card-programme customer emails, some phones, account IDs, 100+ employee emails (relayed by search summary, unverified) | CONFIRMED by the bank (statement relayed by Fox, SECONDARY read) | new CYB-INC-086 |
| Wellington IT (Belfast; owned by Vencora, Canada) | Vulnerability in its online banking platform exploited 10/02-10/04, closed 10/06 (The Register 11/19 11:45 UTC, attributed to affected credit unions); Irish minister Robert Troy: "Around 40 credit unions" (about a quarter of the national total); Core Credit Union's own notice (17 Nov 15:15): told 16 Nov, "approximately 50 credit unions"; saved payees exposed (names, IBAN, BIC, sort code, address, references); passwords, PINs, cards, logins not affected; "The vulnerability ... has been fixed." No CVE, no PHP link stated. Notified about 6 weeks after the access | CONFIRMED · PRIMARY-VERIFIED (Core CU notice) | new CYB-INC-087 |
| Bank SinoPac (Taiwan) | 427 unauthorized transactions from 419 customer accounts on its new mobile banking app, about NT$41.76M (~US$1.3M); bank says hackers breached security settings configured by an overseas system supplier; app pulled; customers reimbursed; seeks compensation from the supplier; no other Taiwan FI uses the system; FSC report due end-November; earlier called a glitch (Focus Taiwan 11/03-11/04, CNA, via search summary; the bank's own PDF did not extract) | CONFIRMED · SECONDARY | new CYB-INC-088 (missed 11/03-11/18: a Taiwan bank is outside every query the desk runs) |
| TruStage | see §6 | | 017 |

Outage limb: no outage at 2+ institutions of 1 business day or more found. JPMorgan states no disruption. ⇒ no limb met; no P1 under this watch.

## 5. Row: ConnectWise Cloud Backup restoration (CYB-INC-018) — CONSUMED, RETIRED

ConnectWise advisory, read by CYPHER with curl (HTTP 200, 697,892 B), "last updated on November 18 at 19:00 UTC": **"Status: Investigation complete. Cloud Backup capabilities restored — partner re-authorization required"**; "Core capabilities ... have been restored, including backups, restores, monitoring, reporting, exports, and notifications"; Microsoft 365 backups "will not resume for a tenant until it has been re-authorized"; remaining billing reporting portals, Accounting Queues and the Billing API "scheduled for restoration on November 19". Phases 1, 2 complete; 3 partially complete; hardening: federated identity credentials, no stored application secrets. PRIMARY-VERIFIED. No FI named. The "2,250 tenants" headline = the >2,250 tenants with attempted sign-ins already on row 018 (Microsoft), not a new figure. Threshold: restoration done (about 33 days after the 10/16 advisory); no FI disclosure naming the route. Retired; billing remnant needs no row.

## 6. Row: TruStage data-access answer window (CYB-INC-017) — CONSUMED, RE-DATED 2027-01-07

- **CU Today headline (11/19 per leg 10; page 403 to the fetcher):** "TruStage Reaches Agreement With Cyberattackers, But Says Data Investigation Will Take At Least Another 6 To 8 Weeks". Search summaries of it: CEO Terrance Williams says the attackers agreed not to release, sell, trade or publish the data and gave assurances it was destroyed; terms, including whether a payment was made, not disclosed; "We can't assume these assurances eliminate all the risks". Notification plan per the summary: state AGs and NCUA; credit-union brands left off letters; two years of three-bureau credit monitoring. Basis: SECONDARY (headline + summaries of an unread page).
- **TruStage outage pages (fetcher read, PRIMARY):** business page "Last Updated: November 18, 2026 | 1:40 PM CT", status "Investigating", still "whether any information was accessed", "some services remain unavailable", "increasingly moving from access to execution"; a "NEW - 11/19/2026" partner video update (not read). Consumer page last updated 11/18 11:15 AM CT. Mandiant memo updated 10/09: environment clean, no active intrusion. No cost, insurance or reserve figure; no count.
- **Reading:** an agreement for the deletion of data implies the attackers held data: this is now an extortion case (class RANSOMWARE-EXTORTION, on the CEO's reported words). Whose data, and whether member PII, is still undetermined. ⚠️ "Assurances" from extortionists are weak evidence (the desk's ATTEMPTS-ONLY discipline applies by analogy: not an all-clear).
- Threshold: PII finding or AG notice: not yet (6-8 weeks from ~11/18 = 12/30 to 01/13); cost line: none; restoration complete: no (recovery into Q1 2027 per a CU Today feature headline, unread). Re-dated 2027-01-07 (MODELED, midpoint of the stated window).

## 7. Escalation watch, 7-day pass (rows 5, 6, 9 due; all nine re-read)

| Row | State | Reading 11/19 |
|---|---|---|
| 1 | NOT-FIRED | No named successful PHP2Shell compromise found in today's reads |
| 3 | NOT-FIRED | JPMorgan (086) is a named US bank victim but through vendor marketing data, with no PHP2Shell link: off-wave, does not fire |
| 4 | NOT-FIRED | leg 8: no Item 1.05 since 11/12 |
| 5 | NOT-FIRED | NYDFS letter list (fetcher read): letters since 10/01 are 11/18 check-cashing fees, 11/12 virtual-currency advertising, 11/04 exempt income, 10/22 PHP alert. No new cyber letter |
| 6 | NOT-FIRED | No PCS designation or loss estimate for the wave. Off-wave: CyberCube 11/16 "Less Than $100M Global Insured Losses From M365 Outage" (0-2% loss-ratio impact) — routed to SHADE. Verisk newsroom did not render (script-loaded) |
| 7 | NOT-FIRED | No government attribution found |
| 8 | NOT-FIRED | No bank or payment operator ties an outage to PHP patching. ⚠️ PHP shipped security releases today (8.5.13, 8.4.28, 8.3.37, 8.2.36; php.net notice 11/18: 14:00-14:30 UTC 11/19), with at least 10 php-src advisories published 11/19 rated Critical incl. "Session serializer mismatch can lead to remote code execution" (likely CVE-2026-115560, not confirmed). A second patch round is a fresh chance for the patch-side route. FT title 11/18 "US tech outages blamed on rush to fix bugs found by AI" (FT unreachable; title only) |
| 9 | NOT-FIRED, State_As_Of 2026-11-18 | HENRY's grade (PROME packet 11/18, read whole): 0 of 21 closes met both collapse legs; closest PANW $309.29 (11/17), $20.05 above $289.24; widest lag 4.31 points vs 10.0; 11/18 close PANW $339.92, HACK $119.60. Collapse-leg window closed, no re-grade: that leg is spent. Cyber-gain and bank legs stay unsized, so the row is not terminal; it keeps NOT-FIRED and its clock while the wave is open. Recorded by my rule (the machine/owner flags, CYPHER sets State; HENRY grades) |

Row 9 note on the other legs (reading only, not a grade): HACK 11/18 $119.60 vs $118.38 reference = +1.03%, i.e. no persisting sector gain on HENRY's figures.

R1 flip test 11/20: rows 1, 3, 4 re-checked today (inside 11/13-11/20). Tomorrow's test reads them once more.

## 8. Inbox

| Item | Disposition |
|---|---|
| PROME 11/18 row 9 packet | INTEGRATE: row 9 (§7) |
| SAM 11/18 GMO reply | LOG: KB row; no consequence for Japan; nothing owed |
| WALTER SIG-W-20261118-005 (HSBC, Associated title) | INTEGRATE: same event as card 008 / CYB-INC-073. American Banker 11/17 16:54 EST (Carter Pape) dek: "An attacker planted code in web testing files used by 178 organizations, 32 in banking and finance. Most of it was gone by Monday afternoon." Associated Bank was already in the 11/17 Optimizely record list. Not a new incident; 073 note added. Rubio title: context |
| WALTER SIG-W-20261118-014 (small items) | LOG: FT outage-cause title to KB (row 8 context); rest not CYPHER's lane (owners named on the card) |
| WALTER SIG-W-20261119-005 (small items) | INTEGRATE: N-able line = new CYB-INC-085 (separate event); rest not CYPHER's lane |

## 9. Read-cap flag (D:L1167 check (2))

My 11/17 flag: the charter was graded at 32,550 B through READS.tsv row CYPHER:SPAWNED-CARD-1 while root gives charters 50,000 B. Today `read_cap_check.py --agent CYPHER` grades `AGENTS/CYPHER/CLAUDE.md` 23,192 B at "46% of ceiling ... not graded at the 32,550 B budget". DAEDALUS fixed it (72c7fe1310, 11/18 10:56 ET, "ceiling applies in every mode"; READ_CAP rule 20 amended). **Resolved at the artifact.** Still standing, not mine: root `CLAUDE.md` 24,449 B, 75% of budget, rotate tier (needs 1,665 B more out), PROME and Will's file.

## 10. NEXUS_BRIEF charter line

Charter BOOT step 5 listed `NEXUS_BRIEF.md` as a write-back every session. Changed to the WQ-719 A / WQ-721 A wording (rewrite only when a figure, threshold or cross-desk send or wait changed; PIN-UNRESOLVED ⇒ pin-only fix). This session's brief does change (new P1 send, row 9 wait resolved).

## 11. Trade read (WQ-696 form)

No investment implication. JPMorgan's exposure is marketing data at unnamed vendors (names, emails), no service disruption, no account or card data on the bank's word: well below anything that moves a $700B+ bank's credit or earnings. TruStage is a mutual (CMFG), not listed. N-able (NABL) is listed: a fourth security event since August is a vendor-reputation story, but the desk has no evidence of customer loss or churn and DEWEY's base rate says lasting equity damage falls on the attack-vector vendor; that is HENRY/VULCAN's grade, not mine. What would change it: a named US bank or core vendor tying a loss to a vendor route (CYP-02/03), an 8-K Item 1.05 from a bank, or an insured-loss estimate above $250M. Sent to TERRY as a no-card handoff.
