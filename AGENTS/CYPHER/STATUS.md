# CYPHER STATUS

**Last Updated: 2026-11-27 (PROME task prome-80, C6 catch-up wake on Will's 17:59 ET word; boot 19:10 EST). Runtime Claude Code, Opus 5.5 (claude-opus-5-5). $0. 2 WALTER cards drained (SIG-W-20261127-006, -014). No escalation row fired; no score, band, gate or prediction moved (25/40 raw, 16/40 adjusted). Five new incident rows (095-099). Record `research/2026-11-27_catch-up/RECORD.md`.**
- **SAP (new 095), the one that matters:** SAP acknowledged an IT incident on its GitHub development platform (statement via dpa, heise 11/27 08:02): no indication of customer business-data access, no downstream compromise of customer systems shown. Handelsblatt (company circles): signing keys exchanged, automated builds stopped: REPORTED. No SAP Security Note, KBA, CVE or customer advisory found (November Security Notes page: nothing after the 11/10 Patch Day; newsroom silent; Trust Center 403). ⚠️ Unknown: WHICH keys. Customer-shipped signing keys would make the window's artifacts suspect (SolarWinds shape). Reaches no chokepoint row. Docket 12/08 (December Patch Day). TERRY packet for a tradeability read.
- **UK DWP (new 097) CONFIRMED at gov.uk 11/27:** "a cyber incident affecting our systems"; some online services offline as a precaution; benefit and pension payments not affected; NCSC and the Government Cyber Coordination Centre engaged; data access unstated.
- **Lloyds Banking Group (new 098):** app and online banking outage 11/27 from about 10:00 UTC, confirmed in the bank's own words (via The Register); no cause, no cyber link stated; restored about 13:00-14:00 GMT per WALTER. Row 8 NOT-FIRED (no PHP tie).
- **Air Force Cloud One (new 096) REPORTED only:** Reuters' unnamed sources 11/27; the Air Force declined to confirm; af.mil 403. **Allstate (new 099) REPORTED:** outage since 11/23, cause unstated; Allstate's sites timed out.
- **Officials' "no coordination" remarks** (11/18 hearing, oral as reported; Clayton 11/22) predate FinCEN, SAP, Cloud One and DWP, so they cover only the 11/12-17 outages (KB-CYP-153). Raia's written testimony (read) does not address the outages.
- **Combination watch:** KB-CYP-151 (`combo:supplier-route-to-banks`, SAP), KB-CYP-152 (`combo:ai-tooling-entry`, Spiegel's agentic-AI claim), KB-CYP-153 (cluster, untagged pending the proposed `us-outage-cluster` theme).
- **Not worked (bounded brief):** boot leg 5's nine 14-day re-checks (023, 024, 028, 029, 038 and four more) and leg 9's Elmet Group 8-K 8.01 (11/24). **Blocks:** sap.com Trust Center, af.mil and bleepingcomputer.com 403; reuters.com refused; Allstate sites timed out (not bypassed).
- **Resume list:** (1) leg 5 re-checks and Elmet 8-K. (2) WQ-678 Changelist B trims (optional). (3) CYP-05 letter issue (flagged 11/16). (4) Proposed combination theme `us-outage-cluster` (needs PROME's C4 check). (5) VSoft confirm or drop 12/03.

Earlier session blocks rotated verbatim: 11/06 and 11/08 to `archive/STATUS_ARCHIVE_2026-11-12.md`; 11/12 to `archive/STATUS_ARCHIVE_2026-11-13.md`; 11/13 to `archive/STATUS_ARCHIVE_2026-11-14.md`; 11/14 and 11/16 10:25 to `archive/STATUS_ARCHIVE_2026-11-16.md`; 11/16 16:08 and 11/17 12:39 to `archive/STATUS_ARCHIVE_2026-11-17.md`; 11/17 20:10/21:33 to `archive/STATUS_ARCHIVE_2026-11-19.md`; 11/19 10:02 to `archive/STATUS_ARCHIVE_2026-11-20.md`; 11/20 to `archive/STATUS_ARCHIVE_2026-11-26.md`; 11/26 to `archive/STATUS_ARCHIVE_2026-11-27.md` (crc32 43a9d969).

> ~~FIRST-LIVE-SESSION BANNER~~ — **SPENT 2026-10-22.** Normal boot.

## Current judgment

**WAVE-2026-10 (PHP2Shell) is open and, since the 11/20 R1 test, MECHANICAL (Log4Shell-shaped): no organisation named at disclosure +30 days. Under the quiet, successful compromises are verified by the products' vendors, victims unnamed.**
- Palo Alto's own advisory (updated 10/29) says "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet". It raised the severity to Critical on 10/27.
- Dream's 10/26 report of a PHP2Shell + Fragnesia chain rooting 24-25 firewalls is no longer a lone vendor claim: Palo Alto's Unit 42 "independently verified the same attacker's tooling and confirmed the reported results" (brief updated 10/29 11:00 PT), about .02% of its installed base impacted, each customer contacted (CYB-INC-047).
- No victim is named, so under the registered rule (R1 needs a *named* organisation) **row 1 stays NOT-FIRED**. DEWEY's "back on Dream withdrawing" path is closed for now.
- No US bank, credit union or core vendor is a named victim.
- One US credit union took digital banking down for about 24h as a precaution (CYB-INC-046). That is a YELLOW case under the pre-registered band, not a fire.
- Base rate: 0 of 5 past waves were systemic for banks (KB-CYP-001, DEWEY-inherited).
- **DEWEY's rerun (008R, 10/29) agrees:** still Log4Shell-like on outcomes, one step toward MOVEit on Dream's claim alone; KEV timing does not separate the two shapes (Log4Shell +1 day, MOVEit +2, PHP2Shell +5). Fortinet's -20.9% is its earnings, not the wave (KB-CYP-071..073).

| Gauge | Reading | Canonical |
|---|---|---|
| Escalation rows, WAVE-2026-10 | **1 FIRED (row 2, KEV 10/26) · 8 NOT-FIRED**; all 8 open rows re-checked 2026-11-26; next clock 12/03 | `workbook/ESCALATION_WATCH.tsv` |
| Convergence composite | **25/40 raw · 16/40 shared-root-adjusted** (VX-01/02/03/06 PHP2Shell cluster counted once at max 4). 11/17: VX-05 3 to 4 ORANGE on the letter (Optimizely, off-wave own root). Earlier: VX-01 corrected to 3; VX-08 4 ORANGE on the FBI attribution; VX-02 held at 3; VX-06 held at 4 | `workbook/VX.tsv` |
| Transmission map | 22 mechanisms: 8 CONFIRMED, 7 NOT-OBSERVED, 2 MODELED, 5 UNTESTED. New FL-CYP-21 (vendor access to theft of a bank's own funds, CONFIRMED) and FL-CYP-22 (one vendor, several banks, UNTESTED) | `workbook/FLOW.tsv` |
| Incident ledger | 99 rows. 11/27: 095 SAP dev environment (CONFIRMED incident, keys REPORTED), 096 Air Force Cloud One (REPORTED), 097 UK DWP (CONFIRMED, gov.uk), 098 Lloyds outage (CONFIRMED, cause unstated), 099 Allstate outage (REPORTED). 11/26: 090 FinCEN, 091 1Password, 092 Best Egg, 093 Barclays Bank Delaware (CONFIRMED), 094 VSoft (REPORTED); KEV keys on 073, 085. 11/19: 085 N-able Mail Assure, 086 JPMorgan vendors, 087 Wellington IT (Irish CUs), 088 Bank SinoPac; 017 re-classed extortion; 018 restored. 11/17 eve: 078 Apple, 079 NWS, 080 Equinor, 081 n0n/Visa supplier, 082 Marriott, 083 Gmail, 084 Java4Shell; 077 NSA CONFIRMED (maintenance; DNI: PHP patching). 11/17: 073 Optimizely supply-chain (CONFIRMED by vendor); 074 AWS US-EAST-1 11/15 (CONFIRMED, AWS); 075 United, 076 FAA, 077 NSA Net (REPORTED); 072 cause stated by JPMorgan. 11/16: 072 US bank login outage opened (INFRA-OUTAGE, Chase confirmed, not stated cyber); 059 Arkéa notes extended (chairman's timeline, instant-payment rail, press-named provider). 11/14: 071 Microsoft 365 global outage opened (INFRA-OUTAGE, not cyber, banks affected none named); 070 KEV-SEEN; 056/057 re-checked, unchanged. 11/13: 070 Check Point PHP2Shell compromises + wiper (CONFIRMED, victims unnamed) opened; 065 N-central → CONFIRMED; 069 Vanguard → CONFIRMED. 11/12: 065 N-central Able2Shell (ATTEMPTS-ONLY), 066 ScreenConnect partner access (REPORTED), 067 Insight CU (REPORTED), 068 Suncoast CU and 069 Vanguard (law-firm claims only) opened; 052 Sawyer → CONFIRMED. 11/06: 063 SonicWall, 064 SecurCommunity and 062 shinkin outage opened; 030 Capcom corrected to CONFIRMED. 11/05: 059 Arkéa, 060 Abrigo, 061 European refrigeration wave opened; 037 Finzly and 047 Dream → CONFIRMED; 055 owner → CYPHER (WQ-589). 11/02: 055 re-classed STATE-CAMPAIGN (FBI). 10/30: 055 Binance, 056 Fiserv/Cl0p claim (Aug, denied), 057 Polymarket halt. 10/29: 046 credit-union PHP pause; 047; 048 Jack Henry; 049 Central Bank of India; 050 Sharetec; 051 N-central; 052 NY bank closure; 053 Citizens; 054 US commissary freezers | `workbook/INCIDENTS.tsv` |
| Chokepoint map | 42 rows (11/19: CHK-16 Cloud Backup restored; CHK-38 fourth N-able event. 11/17 eve: CHK-26 n0n note, Wave_Touch NONE-KNOWN; CHK-20 AWS/Microsoft cause notes): CHK-42 web-script platforms (new 11/17, Optimizely, CONFIRMED-OFF-WAVE); CHK-20 adds AWS 11/15; CHK-20 M365 CONFIRMED-OFF-WAVE (outage 11/12-11/14, not cyber); CHK-10 POSSIBLE (weak), CHK-32 noted (SonicWall, 11/06); CHK-41 Abrigo (11/05); CHK-33 Finzly CONFIRMED-OFF-WAVE; CHK-40 USD stablecoin issuers (LIQUID keeps the figure); CHK-34/35 Treasury nodes; CHK-36 Sharetec, CHK-37 print/mail, CHK-38 N-able (third emergency since August, 11/12 note), CHK-39 SitusAMC; CHK-16 ConnectWise (ScreenConnect note 11/12). Arkéa reaches no row: provider named only by Les Echos on unnamed sources (asset-management compliance software, unconfirmed, 11/16) | `workbook/CHOKEPOINTS.tsv` |
| Predictions | CYP-01 30% · CYP-02 15% · CYP-03 15% · CYP-04 35% · **new 11/05 (WQ-596):** CYP-05 Arkéa provider named 35% · CYP-06 second institution 12% · CYP-07 named PHP2Shell victim 45% (contrarian) · CYP-08 KEV count ≥50 45% on HIT (contrarian lean is MISS); all OPEN, none due | `workbook/PREDICTIONS.tsv` |
| R1 stance | **MECHANICAL (Log4Shell-shaped), 2026-11-20**: rows 1, 3, 4 all NOT-FIRED with in-window checks 11/13, 11/19, 11/20. Rows stay open; a row 1 FIRE flips it back. Late-naming tail graded by CYP-07 (12/31) and CYP-02 (2027-01-31) | `workbook/EXIT_PROTOCOL.md` § R1 RESULT |

## Binance, 10/29 (OFF-WAVE · CYPHER-owned class, WQ-589)

Section rotated verbatim 2026-11-16 to `archive/STATUS_ARCHIVE_2026-11-16.md` (third rotation). Canonical: CYB-INC-055 in `workbook/INCIDENTS.tsv` (FBI: North Korea; DOJ 11/12: more than $2.7B frozen; no US bank, custodian, prime broker or lender named; VX-02 YELLOW at 3, VX-08 ORANGE at 4).

## Open wave — WAVE-2026-10 (rows 1, 3-9 State_As_Of 2026-11-26; row 2 terminal 10/26)

| Row | Sign | State | Latest reading |
|---|---|---|---|
| 1 | Named successful PHP2Shell compromise | NOT-FIRED | 11/26: none named; NCSC alert unchanged since 10/23 15:43; Check Point (070) and Palo Alto's ~.02% stay unnamed |
| 2 | KEV listing of both CVEs | **FIRED 10/26** | Terminal |
| 3 | Named US bank / CU / core-vendor victim | NOT-FIRED | 11/26: Best Egg (092) and Barclays Bank Delaware (093) confirmed, neither states PHP; VSoft (094) unconfirmed |
| 4 | Bank/vendor 8-K Item 1.05 | NOT-FIRED | 11/26: none since 11/19 (leg 8 LIVE); control 15 in 120d |
| 5 | Regulator supervisory concern | NOT-FIRED | 11/26: NYDFS 11/21 ARTEX letter (read) states no regulated-entity compromise, no PHP, no deadline |
| 6 | PCS designation / loss estimate | NOT-FIRED | 11/26: no wave figure found in November |
| 7 | Government state attribution | NOT-FIRED | 11/26: none found |
| 8 | Bank/payment outage outside Japan | NOT-FIRED | 11/27: Lloyds Banking Group outage operator-confirmed, no cause, no PHP tie (098); 11/26: VSoft claim not tied to PHP |
| 9 | Sustained equity move | NOT-FIRED | HENRY 11/18 collapse leg spent; reading 11/25 closes HACK $120.40, PANW $356.14 (read 11/26), no persisting gain |

## Incidents worth knowing (canonical: `workbook/INCIDENTS.tsv`)

| ID | Event | State | Why it matters |
|---|---|---|---|
| CYB-INC-095 | SAP GitHub development platform incident (11/26-27); signing keys exchanged and builds stopped per Handelsblatt; no customer advisory found | CONFIRMED (incident, SAP via dpa) · SECONDARY; keys REPORTED | Supplier to banks and insurers; customer exposure hinges on which keys; 12/08 check |
| CYB-INC-092 / 093 | Best Egg (Barclays-owned lender) Financial Health platform 10/25-10/26, SSNs and loan-payment account numbers, 791,852 (Texas AG); Barclays Bank Delaware card-application tool, detected 11/04, 27,272; Barclays: unrelated | CONFIRMED · PRIMARY-VERIFIED (CA AG letters); counts SECONDARY | Two breaches in one US banking group in ten days; data, not funds; P1 to REGINALD, GIBBS |
| CYB-INC-090 | FinCEN: unauthorized access to a limited subset of systems, some offline (11/24); no evidence of BSA database breach per spokesperson; batch filings to 12/30 | CONFIRMED · SECONDARY (notice as quoted) | Treasury bureau holding bank SARs; filing delay only, so far |
| CYB-INC-091 | 1Password: GitHub account to CI/CD, malicious backend code, subset of users' account records; vaults not affected per company | CONFIRMED · PRIMARY-VERIFIED | Build-system access at a credential vendor; no FI named |
| CYB-INC-094 | VSoft (CU core vendor) ransomware claim, one Reddit post 11/24 | REPORTED · UNANCHORED | Would hit the cluster watch's outage limb if confirmed |
| CYB-INC-089 | MUFG Bank 11/18: ~6.5M records of gender, age, region via contractor PLAID's KARTE (access 11/13); no identifying data; bank systems not accessed; PLAID: server flaw, unnamed; 570 client companies' linked data; restart mid-January | CONFIRMED · PRIMARY-VERIFIED | Japan's largest bank, one SaaS vendor across several group firms; WALTER had it as NOT FOUND |
| CYB-INC-086 | JPMorgan 11/19: vendors attacked, "certain marketing data ... some customer names and email addresses"; no service disruption; no link to the 11/16 outage | CONFIRMED (bank) · SECONDARY read | Largest US bank, vendor-held contact data; possibly n0n's listing (081); vendors and count unknown |
| CYB-INC-085 | N-able Mail Assure / SpamExperts Hosted Cloud: one server accessed (declared 11/18), management offline 3 regions, mail flow up, no customer-data evidence so far | CONFIRMED (vendor via THN) · SECONDARY | Fourth N-able security event since August; MSP channel; no FI named |
| CYB-INC-087 | Wellington IT: payee data at ~40-50 Irish credit unions, flaw exploited 10/02-10/04, told 11/16 | CONFIRMED · PRIMARY-VERIFIED | One vendor, many institutions (data, not funds); Ireland |
| CYB-INC-017 | TruStage: deal with attackers (11/19, SECONDARY); data review 6-8 more weeks; outage page 11/18 still investigating | CONFIRMED (outage) · extortion on the CEO's reported words | Serves most US credit unions; member PII undetermined |
| CYB-INC-080 | Equinor: ongoing attack on certain IT systems (release 11/17 17:55Z), operations and production not affected, no data theft indicated; no update by 01:01Z 11/18 | CONFIRMED · PRIMARY-VERIFIED | Europe's largest gas supplier; actor, method and OT reach unknown; supply not engaged on its word |
| CYB-INC-077 | NSA Net outage 11/17: NSA, scheduled routine maintenance; DNI, patching after the PHP flaws; restoration not confirmed | CONFIRMED · SECONDARY | First official tie of an outage to the wave root, patch side, non-bank |
| CYB-INC-081 | n0n lists JPMorgan, Visa, Mastercard 11/16; Visa: third-party APAC supplier incident, Visa systems and card numbers unaffected | REPORTED · SECONDARY | Card-network supplier; JPMorgan and Mastercard claims unverified |
| CYB-INC-073 | Optimizely Web Experimentation: injected JavaScript on 178 organisations' pages 11/16 (32 finance, incl. 2 US banks, a US credit bureau); card skimming ~9.5 h; contained | CONFIRMED (vendor) · PRIMARY-VERIFIED; victim list researcher's | Vendor poisoning reaching named financial firms' customer pages; VX-05 ORANGE; cards taken unknown |
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
| (older) | 007, 030, 062, 071 Microsoft, 072 Chase, 074 AWS rotated verbatim 2026-11-19 to `archive/STATUS_ARCHIVE_2026-11-19.md`; 043 Park24, 015/017 River Financial and TruStage, 009 eMudhra, 020-022 Quest/SBI/Korea rotated verbatim 2026-11-17 to `archive/STATUS_ARCHIVE_2026-11-17.md` § Fourth rotation | — | Canonical in INCIDENTS.tsv |

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
- **Not done (carried, skipped):** Abrigo AG portal read; Insight CU's own notice; CU Today TruStage page (403); N-able status pages (uptime.n-able.com 403). 11/13: extortion sites not read directly for Kiteworks; Maine AG list did not render.
- **Search lesson:** a re-check of row 8 must search trade press (American Banker, Banking Dive, CU Times) for "offline"/"precaution", not only operator pages.

## Dated next

| Date | Check |
|---|---|
| 11/28 | 14-day re-checks 056 Fiserv/Cl0p, 057 Polymarket |
| 12/01 | GMO compensation totals after the 11/30 window |
| 12/03 | Cluster watch weekly (VSoft 094 confirm or drop); Abrigo (060); Arkéa weekly look (059); escalation 7-day clock |
| 12/04 | Allstate (099) cause and restoration; any 8-K |
| 12/08 | SAP (095) December Patch Day: out-of-band note, certificate revocation or customer advisory. Optimizely (073) financial-firm notices; N-able (085) RCA; JPMorgan (086), MUFG/PLAID (089). Not done 11/26: n0n (081) and Equinor (080) updates |
| 12/11 | Air Force Cloud One (096) official confirmation, actor, data |
| 2027-01-07 | TruStage data-access answer (017) |

## BOTTOM LINE

The October PHP wave stays open with one trigger fired (CISA's listing, 10/26) and eight not fired (row 8 re-read 11/27 for the Lloyds outage, no PHP tie); the stance stays mechanical (Log4Shell-shaped) since the 11/20 test, rows kept open because MOVEit-type victim lists surfaced weeks later, and ⚠️ the quiet is about names, not damage. Off-wave, Barclays' US units had two confirmed data breaches (Best Egg about 792,000 people, Barclays Bank Delaware about 27,000; SSNs, no funds) and FinCEN disclosed an intrusion that so far only delays bank filings to 12/30. On 11/27 SAP acknowledged an incident in its GitHub development systems and reportedly replaced signing keys; it has issued no customer advisory, and which keys were replaced is the unknown that decides whether its customers (banks and insurers among them) are exposed. The UK DWP cyber incident is confirmed at gov.uk with payments unaffected; the Lloyds outage has no stated cause. The most important unconfirmed leads are the SAP signing-key scope and a ransomware claim against VSoft, a credit-union core vendor, from a single community post. Next wakes: leg 5 re-checks, 12/03 cluster watch, Abrigo, Arkéa and VSoft, 12/04 Allstate, 12/08 SAP, Optimizely and N-able.
