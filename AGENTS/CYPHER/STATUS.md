# CYPHER STATUS

**Last Updated: 2026-11-19 ~10:05 EST — PROME task (session prome-36, laptop), C6 due-row wake, launched late; task words are PROME's. Runtime Claude Code, Opus 5.5 (claude-opus-5-5). $0. No escalation row fired; no score, band, gate or prediction moved (composite 25/40 raw, 16/40 adjusted). Four new incident rows (085-088). Record `research/2026-11-19_due-rows/RECORD.md`.**
- **Row 9 recorded:** HENRY graded the collapse leg NOT-FIRED at the 11/18 close (0 of 21 closes met both legs; closest PANW $309.29 on 11/17, $20.05 above the $289.24 line). That leg is spent; the cyber-gain and bank legs stay unsized, so row 9 stays NOT-FIRED with its clock. All 8 open rows re-checked 11/19.
- **JPMorgan (new 086):** the bank says attackers hit its vendors and took marketing data (some customer names and emails); no service disruption; no link to the 11/16 outage. Off-wave. P1 by routing to GIBBS, REGINALD, PROME; substance small. Possibly n0n's 11/16 listing (081), unconfirmed.
- **TruStage (017):** a deal with its attackers (CU Today 11/19 headline, page refused; SECONDARY): assurances the data was destroyed, any payment undisclosed, data review 6 to 8 more weeks. Re-classed RANSOMWARE-EXTORTION. Next look 2027-01-07.
- **N-able (new 085):** a separate breach, Mail Assure / SpamExperts Hosted Cloud, one server accessed, management offline in 3 regions, mail flow up, no customer-data evidence so far. Fourth N-able security event since August. Able2Shell one-look row retired: nothing met (no KEV, no bank naming the route; Insight's filings name no provider, so CYP-03 unresolved).
- **ConnectWise Cloud Backup (018) restored** per its advisory 11/18 19:00 UTC (partners must re-authorize); row retired. ScreenConnect (066) investigation complete 11/16.
- **Abrigo (060):** borrower-facing still down (status 11/16), data loss unstated; next 11/26. **Cluster watch:** 0 new at listed suppliers; next 11/26.
- **Found outside the cards:** Wellington IT, payee data at about 40 to 50 Irish credit unions (087, HANS told); Bank SinoPac, Taiwan, vendor-route transfers ~US$1.3M reimbursed (088, 16 days late); PHP security releases 11/19, 10+ Critical advisories, a second patch round on row 8's patch-side route (KB-CYP-141); CyberCube: M365 outage insured losses under $100M (SHADE told).
- **Charter:** BOOT step 5 NEXUS_BRIEF line changed to WQ-719 A / WQ-721 A. **Read-cap flag (D:L1167 (2)):** resolved at the artifact (charter graded at the 50,000 B ceiling, DAEDALUS 72c7fe1310); root CLAUDE.md at 75% still PROME's.
- **Inbox:** 5 drained (PROME row 9, SAM GMO, WALTER x3). Packets: GIBBS, REGINALD, SHADE, HANS, WALTER, TERRY (no investment implication), PROME. **Git:** pathspec commits; no push; HOLD for PROME's closeout ask.
- **Resume list:** (1) WQ-678 Changelist B trims (optional). (2) CYP-05 letter issue (flagged 11/16). (3) Proposed combination theme `us-outage-cluster` (needs PROME's C4 check).

Earlier session blocks rotated verbatim: 11/06 and 11/08 to `archive/STATUS_ARCHIVE_2026-11-12.md`; 11/12 to `archive/STATUS_ARCHIVE_2026-11-13.md`; 11/13 to `archive/STATUS_ARCHIVE_2026-11-14.md`; 11/14 and 11/16 10:25 to `archive/STATUS_ARCHIVE_2026-11-16.md`; 11/16 16:08 and 11/17 12:39 to `archive/STATUS_ARCHIVE_2026-11-17.md`; 11/17 20:10/21:33 to `archive/STATUS_ARCHIVE_2026-11-19.md`.

> ~~FIRST-LIVE-SESSION BANNER~~ — **SPENT 2026-10-22.** Normal boot.

## Current judgment

**WAVE-2026-10 (PHP2Shell) is open, and the evidence has moved from "exploited somewhere" to "successful compromises verified by the product's vendor, victims unnamed".**
- Palo Alto's own advisory (updated 10/29) says "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet". It raised the severity to Critical on 10/27.
- Dream's 10/26 report of a PHP2Shell + Fragnesia chain rooting 24-25 firewalls is no longer a lone vendor claim: Palo Alto's Unit 42 "independently verified the same attacker's tooling and confirmed the reported results" (brief updated 10/29 11:00 PT), about .02% of its installed base impacted, each customer contacted (CYB-INC-047).
- No victim is named, so under the registered rule (R1 needs a *named* organisation) **row 1 stays NOT-FIRED**. DEWEY's "back on Dream withdrawing" path is closed for now.
- No US bank, credit union or core vendor is a named victim.
- One US credit union took digital banking down for about 24h as a precaution (CYB-INC-046). That is a YELLOW case under the pre-registered band, not a fire.
- Base rate: 0 of 5 past waves were systemic for banks (KB-CYP-001, DEWEY-inherited).
- **DEWEY's rerun (008R, 10/29) agrees:** still Log4Shell-like on outcomes, one step toward MOVEit on Dream's claim alone; KEV timing does not separate the two shapes (Log4Shell +1 day, MOVEit +2, PHP2Shell +5). Fortinet's -20.9% is its earnings, not the wave (KB-CYP-071..073).

| Gauge | Reading | Canonical |
|---|---|---|
| Escalation rows, WAVE-2026-10 | **1 FIRED (row 2, KEV 10/26) · 8 NOT-FIRED**; all 8 open rows re-checked 2026-11-19 (inside the R1 window); row 9 recorded from HENRY's 11/18 grade; next clock 11/26 | `workbook/ESCALATION_WATCH.tsv` |
| Convergence composite | **25/40 raw · 16/40 shared-root-adjusted** (VX-01/02/03/06 PHP2Shell cluster counted once at max 4). 11/17: VX-05 3 to 4 ORANGE on the letter (Optimizely, off-wave own root). Earlier: VX-01 corrected to 3; VX-08 4 ORANGE on the FBI attribution; VX-02 held at 3; VX-06 held at 4 | `workbook/VX.tsv` |
| Transmission map | 22 mechanisms: 8 CONFIRMED, 7 NOT-OBSERVED, 2 MODELED, 5 UNTESTED. New FL-CYP-21 (vendor access to theft of a bank's own funds, CONFIRMED) and FL-CYP-22 (one vendor, several banks, UNTESTED) | `workbook/FLOW.tsv` |
| Incident ledger | 88 rows. 11/19: 085 N-able Mail Assure, 086 JPMorgan vendors, 087 Wellington IT (Irish CUs), 088 Bank SinoPac; 017 re-classed extortion; 018 restored. 11/17 eve: 078 Apple, 079 NWS, 080 Equinor, 081 n0n/Visa supplier, 082 Marriott, 083 Gmail, 084 Java4Shell; 077 NSA CONFIRMED (maintenance; DNI: PHP patching). 11/17: 073 Optimizely supply-chain (CONFIRMED by vendor); 074 AWS US-EAST-1 11/15 (CONFIRMED, AWS); 075 United, 076 FAA, 077 NSA Net (REPORTED); 072 cause stated by JPMorgan. 11/16: 072 US bank login outage opened (INFRA-OUTAGE, Chase confirmed, not stated cyber); 059 Arkéa notes extended (chairman's timeline, instant-payment rail, press-named provider). 11/14: 071 Microsoft 365 global outage opened (INFRA-OUTAGE, not cyber, banks affected none named); 070 KEV-SEEN; 056/057 re-checked, unchanged. 11/13: 070 Check Point PHP2Shell compromises + wiper (CONFIRMED, victims unnamed) opened; 065 N-central → CONFIRMED; 069 Vanguard → CONFIRMED. 11/12: 065 N-central Able2Shell (ATTEMPTS-ONLY), 066 ScreenConnect partner access (REPORTED), 067 Insight CU (REPORTED), 068 Suncoast CU and 069 Vanguard (law-firm claims only) opened; 052 Sawyer → CONFIRMED. 11/06: 063 SonicWall, 064 SecurCommunity and 062 shinkin outage opened; 030 Capcom corrected to CONFIRMED. 11/05: 059 Arkéa, 060 Abrigo, 061 European refrigeration wave opened; 037 Finzly and 047 Dream → CONFIRMED; 055 owner → CYPHER (WQ-589). 11/02: 055 re-classed STATE-CAMPAIGN (FBI). 10/30: 055 Binance, 056 Fiserv/Cl0p claim (Aug, denied), 057 Polymarket halt. 10/29: 046 credit-union PHP pause; 047; 048 Jack Henry; 049 Central Bank of India; 050 Sharetec; 051 N-central; 052 NY bank closure; 053 Citizens; 054 US commissary freezers | `workbook/INCIDENTS.tsv` |
| Chokepoint map | 42 rows (11/19: CHK-16 Cloud Backup restored; CHK-38 fourth N-able event. 11/17 eve: CHK-26 n0n note, Wave_Touch NONE-KNOWN; CHK-20 AWS/Microsoft cause notes): CHK-42 web-script platforms (new 11/17, Optimizely, CONFIRMED-OFF-WAVE); CHK-20 adds AWS 11/15; CHK-20 M365 CONFIRMED-OFF-WAVE (outage 11/12-11/14, not cyber); CHK-10 POSSIBLE (weak), CHK-32 noted (SonicWall, 11/06); CHK-41 Abrigo (11/05); CHK-33 Finzly CONFIRMED-OFF-WAVE; CHK-40 USD stablecoin issuers (LIQUID keeps the figure); CHK-34/35 Treasury nodes; CHK-36 Sharetec, CHK-37 print/mail, CHK-38 N-able (third emergency since August, 11/12 note), CHK-39 SitusAMC; CHK-16 ConnectWise (ScreenConnect note 11/12). Arkéa reaches no row: provider named only by Les Echos on unnamed sources (asset-management compliance software, unconfirmed, 11/16) | `workbook/CHOKEPOINTS.tsv` |
| Predictions | CYP-01 30% · CYP-02 15% · CYP-03 15% · CYP-04 35% · **new 11/05 (WQ-596):** CYP-05 Arkéa provider named 35% · CYP-06 second institution 12% · CYP-07 named PHP2Shell victim 45% (contrarian) · CYP-08 KEV count ≥50 45% on HIT (contrarian lean is MISS); all OPEN, none due | `workbook/PREDICTIONS.tsv` |
| R1 two-way flip | Toward MOVEit: row 1 or 3 FIRES on or before 2026-11-20 (a named organisation). Toward Log4Shell: rows 1, 3 and 4 all NOT-FIRED at 11/20, with re-checks dated 11/13–11/20 | `workbook/EXIT_PROTOCOL.md` |

## Binance, 10/29 (OFF-WAVE · CYPHER-owned class, WQ-589)

Section rotated verbatim 2026-11-16 to `archive/STATUS_ARCHIVE_2026-11-16.md` (third rotation). Canonical: CYB-INC-055 in `workbook/INCIDENTS.tsv` (FBI: North Korea; DOJ 11/12: more than $2.7B frozen; no US bank, custodian, prime broker or lender named; VX-02 YELLOW at 3, VX-08 ORANGE at 4).

## Open wave — WAVE-2026-10 (rows 1, 3-9 State_As_Of 2026-11-19; row 2 terminal 10/26)

| Row | Sign | State | Latest reading |
|---|---|---|---|
| 1 | Named successful PHP2Shell compromise | NOT-FIRED | 11/19: none named. Check Point (070) and Palo Alto's ~.02% stay unnamed; Kiteworks leg empty |
| 2 | KEV listing of both CVEs | **FIRED 10/26** | Terminal |
| 3 | Named US bank / CU / core-vendor victim | NOT-FIRED | 11/19: JPMorgan's vendor data (086) has no PHP2Shell link, off-wave; Storm's bank claims run through the AUGUST N-central flaw |
| 4 | Bank/vendor 8-K Item 1.05 | NOT-FIRED | 11/19: none since 11/12 (leg 8 live); control 15 in 120d |
| 5 | Regulator supervisory concern | NOT-FIRED | 11/19: NYDFS 10/22 still the latest cyber letter |
| 6 | PCS designation / loss estimate | NOT-FIRED | 11/19: no wave figure; Verisk newsroom unreadable; off-wave CyberCube M365 <$100M |
| 7 | Government state attribution | NOT-FIRED | 11/19: none found; Check Point's China-nexus overlap is private and unattributed |
| 8 | Bank/payment outage outside Japan | NOT-FIRED | 11/19: no bank or payment operator ties an outage to PHP patching (DNI tied the NSA's, 11/17). ⚠️ PHP security releases 11/19 open a second patch round on this route |
| 9 | Sustained equity move | NOT-FIRED | HENRY 11/18: collapse leg NOT-FIRED, 0 of 21 closes; 11/18 PANW $339.92, HACK $119.60; leg spent, other legs unsized |

## Incidents worth knowing (canonical: `workbook/INCIDENTS.tsv`)

| ID | Event | State | Why it matters |
|---|---|---|---|
| CYB-INC-086 | JPMorgan 11/19: vendors attacked, "certain marketing data ... some customer names and email addresses"; no service disruption; no link to the 11/16 outage | CONFIRMED (bank) · SECONDARY read | Largest US bank, vendor-held contact data; possibly n0n's listing (081); vendors and count unknown |
| CYB-INC-085 | N-able Mail Assure / SpamExperts Hosted Cloud: one server accessed (declared 11/18), management offline 3 regions, mail flow up, no customer-data evidence so far | CONFIRMED (vendor via THN) · SECONDARY | Fourth N-able security event since August; MSP channel; no FI named |
| CYB-INC-087 | Wellington IT: payee data at ~40-50 Irish credit unions, flaw exploited 10/02-10/04, told 11/16 | CONFIRMED · PRIMARY-VERIFIED | One vendor, many institutions (data, not funds); Ireland |
| CYB-INC-017 | TruStage: deal with attackers (11/19, SECONDARY); data review 6-8 more weeks; outage page 11/18 still investigating | CONFIRMED (outage) · extortion on the CEO's reported words | Serves most US credit unions; member PII undetermined |
| CYB-INC-080 | Equinor: ongoing attack on certain IT systems (release 11/17 17:55Z), operations and production not affected, no data theft indicated; no update by 01:01Z 11/18 | CONFIRMED · PRIMARY-VERIFIED | Europe's largest gas supplier; actor, method and OT reach unknown; supply not engaged on its word |
| CYB-INC-077 | NSA Net outage 11/17: NSA, scheduled routine maintenance; DNI, patching after the PHP flaws; restoration not confirmed | CONFIRMED · SECONDARY | First official tie of an outage to the wave root, patch side, non-bank |
| CYB-INC-081 | n0n lists JPMorgan, Visa, Mastercard 11/16; Visa: third-party APAC supplier incident, Visa systems and card numbers unaffected | REPORTED · SECONDARY | Card-network supplier; JPMorgan and Mastercard claims unverified |
| CYB-INC-073 | Optimizely Web Experimentation: injected JavaScript on 178 organisations' pages 11/16 (32 finance, incl. 2 US banks, a US credit bureau); card skimming ~9.5 h; contained | CONFIRMED (vendor) · PRIMARY-VERIFIED; victim list researcher's | Vendor poisoning reaching named financial firms' customer pages; VX-05 ORANGE; cards taken unknown |
| CYB-INC-074 | AWS US-EAST-1 11/15 06:05-09:21 ET, sign-in and connectivity, no cause stated | CONFIRMED · PRIMARY-VERIFIED | Answers card 011's "unverified"; CHK-20; no financial firm named |
| CYB-INC-072 | Chase online-banking outage 11/16 from ~09:53 ET; JPMorgan 11/17: "a software bug in on-premise hardware systems", not cyber; other banks' delays from transactions with Chase; eased Monday night (Newsweek) | CONFIRMED (Chase) · SECONDARY | Largest US bank's online channel down under a day; not cyber on the bank's word; no shared provider |
| CYB-INC-071 | Microsoft 365 global outage 11/12-11/14, about 24h, 70+ countries; Microsoft: network capacity upgrade, not cyber | CONFIRMED (outage) · SECONDARY (Microsoft quoted by AP) | Banks affected, none named; no payment rail named; cloud common-mode on CHK-20 |
| CYB-INC-070 | Check Point Mobile Access gateways: PHP2Shell compromises from 10/30, root via CVE-2026-123039 (CISA KEV 11/13), wiper at some Israeli victims; second wave 11/02 worldwide | CONFIRMED · PRIMARY-VERIFIED (Check Point Research, victims unnamed) | First destructive outcome in the wave; a name would flip R1 toward MOVEit |
| CYB-INC-065 | N-able N-central: Able2Shell (33 alleged zero-days, hosted offline 11/09-11/11, HF2 11/10), then 4EverAble2Shell 11/12 defeats HF2 where the Legacy API is on: 21 live servers mining, 19 patched (Huntback); N-able IOCs 11/13 | CONFIRMED · PRIMARY-VERIFIED (responder report + vendor IOCs) | MSP route into banks that outsource IT; no FI named; no N-central CVE of this round in KEV |
| CYB-INC-052 / 067 | Storm-1175 lists five US banks (~$6.1B) and Insight CU (FL); Sawyer confirmed (notice 10/09, MSP origin per its notice, SECONDARY), Insight confirmed per American Banker | CONFIRMED · PRIMARY (Sawyer, VT AG) / REPORTED · SECONDARY (Insight) | The August N-central route reaching US banks; four banks neither confirm nor deny |
| CYB-INC-066 | ConnectWise ScreenConnect: partner-environment access via third-party RMM+ extensions (CVE assigned); SCKit toolkit; ~400 environments disabled; outreach to identified affected partners (11/12 18:45 UTC) | REPORTED · PRIMARY-VERIFIED (advisory) | Second MSP-tool event in the same week; no FI named |
| CYB-INC-059 | Crédit Mutuel Arkéa: own-account theft through a provider, about EUR 100M (chairman: "1% of own funds"), over instant payments from 11/01; provider press-named 11/14 on unnamed sources (asset-management compliance software), unconfirmed | CONFIRMED · PRIMARY-VERIFIED (figure and provider not) | First own-funds theft through a vendor in this ledger; reach unknown, no second victim |
| CYB-INC-060 | Abrigo: unauthorized access behind Sageworks shutdown 10/30-11/02; borrower features still off 11/12; data loss unstated | CONFIRMED · SECONDARY | Bank and CU loan documents; >2,400 institutions across all products |
| CYB-INC-047 | Dream: PHP2Shell + Fragnesia rooted 24-25 firewalls; US government-affiliated network had credentials extracted; Palo Alto verified | CONFIRMED · PRIMARY-VERIFIED (victims unnamed) | MOVEit-shape risk if a name surfaces |
| CYB-INC-046 | A US credit union ($8.9B) paused its in-house PHP website and digital banking ~24h on 10/21; payments up; no member impact stated | REPORTED · SECONDARY (operator quoted) | First US FI service pause for this wave; the row 8 band boundary case |
| CYB-INC-027 | Node2Shell CVE-2026-111497: CISA KEV 10/27 (listed under Google Brotli); AI-found (OpenAI Codex Security) | CONFIRMED (flaw level) · PRIMARY-VERIFIED | Off-root; AI-found flaw exploited within 6 days of the fix; VULCAN told |
| CYB-INC-018 | ConnectWise / Storm-0940 Cloud Backup supply chain: **restored** per advisory 11/18 19:00 UTC, partner re-authorization required | CONFIRMED · PRIMARY-VERIFIED | MSP channel; no FI named; row retired |
| CYB-INC-037 | Finzly: company confirms one backup-site device accessed; firewall keys and a map of the clients' Fed link published; Fed "not impacted"; keys untested | CONFIRMED · SECONDARY (company statement) | Strongest financial-supplier lead; first-access date unknown |
| (older) | 007 PHP2Shell root, 030 Capcom, 062 Shinkin rotated verbatim 2026-11-19 to `archive/STATUS_ARCHIVE_2026-11-19.md`; 043 Park24, 015/017 River Financial and TruStage, 009 eMudhra, 020-022 Quest/SBI/Korea rotated verbatim 2026-11-17 to `archive/STATUS_ARCHIVE_2026-11-17.md` § Fourth rotation | — | Canonical in INCIDENTS.tsv |

**Do-not-relay, 13 claims** (canonical `research/2026-10-23_news-sweep-and-relay-pattern.md` §4). 12 of the 13 overstate toward alarm. A news outlet reporting an agency is a lead, never row-1 evidence. **Add:** "FEC hacked" is Reuters' framing of an internal email; FEC's status page says "outage" (board_log 10/29).

## News sweep 10/29

Rotated verbatim 2026-11-06 to `archive/STATUS_ARCHIVE_2026-11-06.md`; its facts stay canonical in INCIDENTS, CHOKEPOINTS and KB. Still standing: Will's 10/29 bank-vendor and payment-plumbing cluster watch (weekly, catalyst row 11/12); `banking/` holds that thread.

## Standing conditions

- **Event, not consequence.** **All 11 boundary owners confirmed** (REGINALD 10/30, with one amendment: credit-union-only items go to it as P3 context; a multi-institution outage of 1 business day or more stays P2; KB-CYP-084). The others: GIBBS, WATT, VULCAN, FALCON, BRENT, LIQUID, OTTO, SHADE, HENRY, BOND (KB-CYP-062..064).
- **Intake rule** (WALTER v0.48): ledger rows only for financial or chokepoint victims, desk-cited claims, or claims CYPHER checked. Everything else goes in board_log notes (`inbox/PROTOCOL.md` rule 0).
- **Recorded disagreement:** DEWEY recommended a WALTER watch, not a desk; Will chose a desk. R0 review on 2026-12-17.
- **Guardrails:** no scanning or probing of institutions. Packets carry counts; names stay in research files.
- **No book** (`TRADE.md`, FROZEN).
- **Approvals:** Tier-2 event ownership and the existing watch. CYP-01..04 registered on Will's word. WQ-500 (no healthcare owner) and WQ-501 (CYBER group) ruled. WQ-589 B-narrow: crypto-venue and stablecoin-issuer hacks, dollar-system reach only. The 11/12 session ran on PROME's C6 wake (WQ-184) and Will's 11/11 word on the N-able card (no broad backlog expansion, no new recurring review). No capital authority.

## Data walls and runtime

- Verisk PCS subscription (MIRROR-WALLED).
- mass.gov notice PDFs 403 to both the fetch tool and curl (Citi 040 vendor name unrecovered).
- chromium.googlesource commit history needs sign-in.
- Bloomberg, WSJ and FT are paywalled.
- NYDFS is reachable by WebFetch. CISA KEV and SEC EDGAR are reachable. 11/19: no direct WebFetch in this runtime (fetches via `web-fetch` subagents); cutoday.info, cybernews.com, uptime.n-able.com 403; ft.com refused; Verisk newsroom script-only. Boot leg 9 HTTP 500 at boot, LIVE on re-run.
- Runtime 10/29: Claude Code, Opus 5.5. Shell, git, Python, WebFetch/WebSearch and subagents are available.
- MCP servers mtnewswire, definite and Prisma failed to connect. SendMessage is loaded only on demand, and its use across sessions is untested.

## Known gaps carried

- Boot-leg fixes and history 10/29 to 11/12 (legs 5, 7-10; Leg 10 rebuilt 11/12; originals read 10/29; charter rotated; MCP connections) rotated verbatim 2026-11-17 to `archive/STATUS_ARCHIVE_2026-11-17.md` § Third rotation. ⚠️ Still standing from it: Leg 10 quiet does not mean no incident.
- **Not done (carried, skipped):** SonicWall advisory re-read (063) and SecurCommunity check (064), on STATUS's 11/19 line but on no calendar row, skipped again 11/19; Abrigo AG portal read; Insight CU's own notice; CU Today TruStage page (403); N-able status pages (uptime.n-able.com 403). 11/13: extortion sites not read directly for Kiteworks; Maine AG list did not render.
- **Search lesson:** a re-check of row 8 must search trade press (American Banker, Banking Dive, CU Times) for "offline"/"precaution", not only operator pages.

## Dated next

| Date | Check |
|---|---|
| 11/20 | **R1 flip test (P1)**, Kiteworks leg rides it; re-read PHP 11/19 advisories for CVE ids (KB-CYP-141) |
| 11/23 | Arkéa weekly look (provider confirmation; client base if named) |
| 11/24 | N-able Mail Assure (085) and JPMorgan vendors (086) follow-up · Optimizely follow-up (CYB-INC-073): statements or breach notices from listed US financial firms; Optimizely detail on cross-customer access · n0n (081): published data or Mastercard/JPMorgan statements · Equinor (080) update |
| 11/26 | Cluster watch weekly; Abrigo (060) |
| 11/27 | Microsoft 365 post-incident report (date estimated) |
| 11/28 | 14-day re-checks 056 Fiserv/Cl0p, 057 Polymarket |
| 12/01 | GMO compensation totals after the 11/30 window |
| 2027-01-07 | TruStage data-access answer (017) |

## BOTTOM LINE

The October PHP wave stays open with one trigger fired (CISA's listing, 10/26) and the other eight not fired, all re-checked 11/19; HENRY's grade closes the Palo Alto collapse test as not fired, and tomorrow's flip test (11/20) will read the Log4Shell way unless an organisation is named first. The day's new events are vendor-side and small: JPMorgan says attackers took marketing contact data from its vendors with no service impact, TruStage has struck a deal with its attackers with the data question open for 6 to 8 more weeks, and N-able has a fourth, separate breach with no customer-data evidence yet. The most important unconfirmed lead is still whether a bank or payment operator ties an outage to PHP patching, now with a second PHP patch round released today. Next wakes: 11/20 flip test, 11/23 Arkéa, 11/24 N-able, JPMorgan, Optimizely and Equinor follow-ups, 11/26 cluster watch and Abrigo.
