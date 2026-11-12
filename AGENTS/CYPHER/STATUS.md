# CYPHER STATUS

**Last Updated: 2026-11-12 09:05 EST — PROME wake, due-row class C6 (WQ-184), session prome-e8; N-able card first on Will's 11/11 14:06 ET word (relayed by PROME packet). Runtime Claude Code, Opus 5.5. $0. No score, band, gate or prediction moved; no escalation row fired; one ledger state upgraded by the ledger's own enum (CYB-INC-052 Sawyer → CONFIRMED on a state AG record).**
- **N-able Able2Shell (CYB-INC-065, new, off-wave, ATTEMPTS-ONLY):** read at N-able's own status records. Hosted N-central was offline in all regions from 11/09 14:00 UTC; the fix (HF2, 7 CVEs) shipped 11/10; all hosted servers were upgraded by 11/11 01:04 UTC. On-premises servers must upgrade themselves. N-able says it sees scanning tied to the public exploit code; it has not said any customer was compromised. The researcher's repo holds 33 exploit scripts; N-able has published 7 CVEs and promised a further fix. **New today (11/12 07:00 UTC):** a second disclosure claims the fix is bypassed; N-able says that needs a non-default setting (Legacy API exposed) and is investigating. None of the 7 CVEs is in KEV (v2026.11.10). No bank, credit union or bank vendor is named as a user. The evidence supports "no impact reported", not "no impact". Verdict: leaves WAVE-2026-10 intact (off-wave, no watch row); one follow-up registered (catalyst 11/19, one look).
- **Found while assessing it:** American Banker (11/11) reports the Storm ransomware group (Storm-1175, which Microsoft linked to the AUGUST N-central flaw) has listed five US banks (~$6.1B assets) and Insight Credit Union (Florida); two confirmed breaches: Sawyer Savings Bank (052, now CONFIRMED on Vermont's AG record; 16,069 people per Indiana's) and Insight (067, REPORTED). Sawyer's notice reportedly says the breach began at its IT provider. ⚠️ CYP-03 is not resolved by it: the notice is dated 10/09, before CYP-03's 10/24 window, so the forecast's event had already happened, unseen, when CYP-03 was registered. Flagged to PROME; not re-marked.
- **ConnectWise:** a separate ScreenConnect investigation opened 11/11 22:45 UTC (CYB-INC-066, REPORTED): reports of unauthorized access to partner environments through third-party "RMM+" extensions; ~400 partner environments had them disabled; ConnectWise found no ScreenConnect flaw. Cloud Backup (018) still not fully restored (advisory unchanged since 11/04).
- **Due rows:** wave 7-day pass done, rows 1 and 3-9 NOT-FIRED as of 11/12; Abrigo borrower features still off (day 13), data loss unstated; cluster watch 0 new at its supplier list since 11/05; Keystone erasure unconfirmed, row retired; claim pass (023, 024, 028, 029, 038, 040, 042, 045): nothing confirmed or denied. Re-dated 11/19.
- **Own-control fix:** boot leg 10 missed N-able (one 21-name query saturated; no "zero-day"/"offline"). Now 6 chunked queries; 113 items vs 28; N-able headlines listed; drills 36/36 (KB-CYP-112).
- **Inbox drained:** 6 WALTER cards + 2 PROME packets. WQ-660 charter line added (CLAUDE.md step 3a). COR-20261111-14 NO-OP. Watch notes rotated verbatim to `archive/ESCALATION_WATCH_NOTES_2026-11-12.md` (now 58% of budget).
- **Resume list:** (1) charter GIT pointer for carve-out ④ (PROME 11/07 packet, KB-CYP-108): still waiting on PROME's authorisation. Items (2) watch rotation and (3) WQ-660 line: done 11/12.

Earlier session blocks (11/06, 11/08) rotated verbatim 2026-11-12 to `archive/STATUS_ARCHIVE_2026-11-12.md`.

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
| Escalation rows, WAVE-2026-10 | **1 FIRED (row 2, KEV 10/26) · 8 NOT-FIRED**, all re-checked 2026-11-12 (row 2 terminal); next clock 11/19 | `workbook/ESCALATION_WATCH.tsv` |
| Convergence composite | **24/40 raw · 15/40 shared-root-adjusted** (VX-01/02/03/06 PHP2Shell cluster counted once at max 4). VX-01 corrected to 3; VX-08 graded 4 ORANGE on the FBI attribution; VX-02 held at 3; VX-06 held at 4 | `workbook/VX.tsv` |
| Transmission map | 22 mechanisms: 8 CONFIRMED, 7 NOT-OBSERVED, 2 MODELED, 5 UNTESTED. New FL-CYP-21 (vendor access to theft of a bank's own funds, CONFIRMED) and FL-CYP-22 (one vendor, several banks, UNTESTED) | `workbook/FLOW.tsv` |
| Incident ledger | 69 rows. 11/12: 065 N-central Able2Shell (ATTEMPTS-ONLY), 066 ScreenConnect partner access (REPORTED), 067 Insight CU (REPORTED), 068 Suncoast CU and 069 Vanguard (law-firm claims only) opened; 052 Sawyer → CONFIRMED. 11/06: 063 SonicWall, 064 SecurCommunity and 062 shinkin outage opened; 030 Capcom corrected to CONFIRMED. 11/05: 059 Arkéa, 060 Abrigo, 061 European refrigeration wave opened; 037 Finzly and 047 Dream → CONFIRMED; 055 owner → CYPHER (WQ-589). 11/02: 055 re-classed STATE-CAMPAIGN (FBI). 10/30: 055 Binance, 056 Fiserv/Cl0p claim (Aug, denied), 057 Polymarket halt. 10/29: 046 credit-union PHP pause; 047; 048 Jack Henry; 049 Central Bank of India; 050 Sharetec; 051 N-central; 052 NY bank closure; 053 Citizens; 054 US commissary freezers | `workbook/INCIDENTS.tsv` |
| Chokepoint map | 41 rows: CHK-10 POSSIBLE (weak), CHK-32 noted (SonicWall, 11/06); CHK-41 Abrigo (11/05); CHK-33 Finzly CONFIRMED-OFF-WAVE; CHK-40 USD stablecoin issuers (LIQUID keeps the figure); CHK-34/35 Treasury nodes; CHK-36 Sharetec, CHK-37 print/mail, CHK-38 N-able (third emergency since August, 11/12 note), CHK-39 SitusAMC; CHK-16 ConnectWise (ScreenConnect note 11/12). Arkéa reaches no row: provider unnamed | `workbook/CHOKEPOINTS.tsv` |
| Predictions | CYP-01 30% · CYP-02 15% · CYP-03 15% · CYP-04 35% · **new 11/05 (WQ-596):** CYP-05 Arkéa provider named 35% · CYP-06 second institution 12% · CYP-07 named PHP2Shell victim 45% (contrarian) · CYP-08 KEV count ≥50 45% on HIT (contrarian lean is MISS); all OPEN, none due | `workbook/PREDICTIONS.tsv` |
| R1 two-way flip | Toward MOVEit: row 1 or 3 FIRES on or before 2026-11-20 (a named organisation). Toward Log4Shell: rows 1, 3 and 4 all NOT-FIRED at 11/20, with re-checks dated 11/13–11/20 | `workbook/EXIT_PROTOCOL.md` |

## Binance, 10/29 (OFF-WAVE · CYPHER-owned class from 11/02, WQ-589 · canonical CYB-INC-055)

| Item | Reading (2026-10-30) | Basis |
|---|---|---|
| What happened | Unauthorized withdrawals from hot wallets; Binance points to a compromised DevOps engineer laptop that reached a service container, and says it found "no evidence of any wallet private key leak". Its CEO later said "additional points of breach" | Notice PRIMARY-VERIFIED; CEO SECONDARY |
| Size | Binance: ~$6.3B estimated total IMPACT and ~$3B frozen, so about $3.3B is not frozen. Arkham: $6.01B taken, $2.80B frozen | OWNER-ASSERTED / SECONDARY |
| Issuer freezes | On Ethereum: USDC $823.00M and USDT $1,350.46M traced (+$30M probable), frozen 37–41 min after the first drain; none destroyed. **Unchanged at 14:54Z re-tally.** Tron not checked | PRIMARY-VERIFIED on-chain |
| Withdrawals | Off on all pairs from ~22:33Z 10/29 (all of Fri 10/30). Phase one reopened Sun 11/01 06:00–09:00Z; **29 of 1,448 pairs on at 13:48Z 11/02**; next phase "tomorrow". Net outflows $4.72B since reopening (Binance via Reuters) | ARTIFACT-VERIFIED / PRIMARY / SECONDARY |
| Attribution | **FBI: North Korea (TraderTraitor), alert 10/31, "more than $6 billion"**; 628 addresses to block. CYB-INC-055 class STATE-CAMPAIGN | SECONDARY (fbi.gov 403) |
| Leg 2 (11/02) | Cover ~95% (OWNER-ASSERTED); freezes intact; no redemption surge; COIN within beta at the 10/30 close; no bank named. VX-02 YELLOW held at 3 on the letter; re-cut drafted; no standing owner recommended | leg-2 RECORD |
| Transmission (WQ-550 leg 1) | No other exchange halted; Aave froze its affected markets. Market makers Wintermute (<20% of net equity) and GSR (<5%) are exposed; no bank, prime broker or lender is named. US crypto stocks move with bitcoin and the Nasdaq on the equity clock. COIN's residual overlaps its own earnings | SECONDARY / ARTIFACT-VERIFIED (prices) |
| Map | Not a CHK event: the issuers were the control that worked. New class row CHK-40 (USD stablecoin issuers, NONE-KNOWN) | desk judgment |
| Watch / vectors | No escalation row (OFF-WAVE). VX-02 YELLOW at 3 stands; re-cut encoded 11/05 for later events. VX-08 graded 4 ORANGE 11/05 on the FBI attribution, composition noted | desk judgment |
| Post-mortem and outreach (11/05) | Began June with malicious software installed for an AI coding tool, plus fake recruiter interviews; no vendor, supplier or bank named. North Korea denies. Fed and OCC supervisors called banks 11/02 (Reuters, anonymous): outreach, no finding, no bank named; never "probe" or "contagion" | SECONDARY |
| Do not relay | "$5B hack" · "$6.3B stolen" · "largest bank heist" · "CZ confirms" · "North Korea did it" · "user funds lost" (first-read RECORD §9) · "COIN down 10× bitcoin" · "Binance halted trading" · "Tether and Circle said they froze $2.36B" (leg-1 RECORD §6) | — |

## Open wave — WAVE-2026-10 (all rows State_As_Of 2026-11-12 except row 2, terminal 10/26)

| Row | Sign | State | 11/12 reading |
|---|---|---|---|
| 1 | Named successful PHP2Shell compromise | NOT-FIRED | No named victim at any source (search-level); Unit 42's government-victim attribution stays retracted; Palo Alto's verified ~.02% stays unnamed |
| 2 | KEV listing of both CVEs | **FIRED 10/26** | Terminal |
| 3 | Named US bank / CU / core-vendor victim | NOT-FIRED | Storm's bank and CU claims run through the AUGUST N-central flaw where a route is stated, not PHP2Shell |
| 4 | Bank/vendor 8-K Item 1.05 | NOT-FIRED | None since 11/05 (leg 8 live); control 16 in 120d |
| 5 | Regulator supervisory concern | NOT-FIRED | NYDFS 10/22 still the latest cyber letter (list read 11/12) |
| 6 | PCS designation / loss estimate | NOT-FIRED | No figure found |
| 7 | Government state attribution | NOT-FIRED | Private only (CYFIRMA: Korean-speaking, possibly Lazarus-linked; Dream: Chinese-speaking cluster) |
| 8 | Bank/payment outage outside Japan | NOT-FIRED | None tied to the wave; this week's outages are MSP tools, off-wave |
| 9 | Sustained equity move | NOT-FIRED | HENRY grades 11/18. 11/11 close vs 10/20: PANW $334.47 (-1.71%), HACK $117.51 (-0.73%), gap -0.98 pts; PANW $45.23 above $289.24 |

## Incidents worth knowing (canonical: `workbook/INCIDENTS.tsv`)

| ID | Event | State | Why it matters |
|---|---|---|---|
| CYB-INC-065 | N-able N-central Able2Shell: 33 alleged zero-days published 11/08-09; hosted offline 11/09-11/11; HF2 (7 CVEs) 11/10; bypass claim under N-able investigation 11/12 | ATTEMPTS-ONLY · PRIMARY-VERIFIED (vendor statements) | MSP route into banks that outsource IT; no FI named; none of the 7 CVEs in KEV yet |
| CYB-INC-052 / 067 | Storm-1175 lists five US banks (~$6.1B) and Insight CU (FL); Sawyer confirmed (notice 10/09, MSP origin per its notice, SECONDARY), Insight confirmed per American Banker | CONFIRMED · PRIMARY (Sawyer, VT AG) / REPORTED · SECONDARY (Insight) | The August N-central route reaching US banks; four banks neither confirm nor deny |
| CYB-INC-066 | ConnectWise ScreenConnect: reports of partner-environment access via third-party RMM+ extensions; ~400 environments disabled | REPORTED · PRIMARY-VERIFIED (advisory) | Second MSP-tool event in the same week; no FI named |
| CYB-INC-007 | PHP2Shell root CVEs in KEV since 10/26 | CONFIRMED (flaw level) · PRIMARY-VERIFIED | The wave root |
| CYB-INC-030 | Capcom: 11,774,247 records (email, account data), no cards, method unpublished | CONFIRMED · PRIMARY-VERIFIED | Corrects the desk's own 10/23 read; no financial channel |
| CYB-INC-062 | Shinkin Kyodo Center: 128 Japanese credit co-ops down about 5.5 hours 11/06 | CONFIRMED · SECONDARY (operators quoted) | Widest institution count in the ledger; operators think not cyber |
| CYB-INC-059 | Crédit Mutuel Arkéa: own-account theft through an unnamed provider, about EUR 100M provisional | CONFIRMED · PRIMARY-VERIFIED (figure not) | First own-funds theft through a vendor in this ledger; reach unknown |
| CYB-INC-060 | Abrigo: unauthorized access behind Sageworks shutdown 10/30-11/02; borrower features still off 11/12; data loss unstated | CONFIRMED · SECONDARY | Bank and CU loan documents; >2,400 institutions across all products |
| CYB-INC-047 | Dream: PHP2Shell + Fragnesia rooted 24-25 firewalls; US government-affiliated network had credentials extracted; Palo Alto verified | CONFIRMED · PRIMARY-VERIFIED (victims unnamed) | MOVEit-shape risk if a name surfaces |
| CYB-INC-046 | A US credit union ($8.9B) paused its in-house PHP website and digital banking ~24h on 10/21; payments up; no member impact stated | REPORTED · SECONDARY (operator quoted) | First US FI service pause for this wave; the row 8 band boundary case |
| CYB-INC-027 | Node2Shell CVE-2026-111497: CISA KEV 10/27 (listed under Google Brotli); AI-found (OpenAI Codex Security) | CONFIRMED (flaw level) · PRIMARY-VERIFIED | Off-root; AI-found flaw exploited within 6 days of the fix; VULCAN told |
| CYB-INC-018 | ConnectWise / Storm-0940 supply chain: phases 1-2 complete, 3-4 partial, billing and platform dashboard open (advisory unchanged since 11/04 18:55 UTC, read 11/12); **not restored** | CONFIRMED · PRIMARY-VERIFIED | MSP channel; no FI named |
| CYB-INC-037 | Finzly: company confirms one backup-site device accessed; firewall keys and a map of the clients' Fed link published; Fed "not impacted"; keys untested | CONFIRMED · SECONDARY (company statement) | Strongest financial-supplier lead; first-access date unknown |
| CYB-INC-043 | Park24: ~1.46M accounts eligible for JPY 3,000 (~JPY 4.4B); JPY 5.5B loss; net forecast cut 44.0B → 38.5B | REPORTED · SECONDARY | Listed-company earnings channel (SAM/OTTO); issuer notice unread |
| CYB-INC-015 / 017 | River Financial (off-wave ransomware, 8-K) · TruStage (CU vendor outage since 7/11) | CONFIRMED · PRIMARY-VERIFIED | Off-wave US financial victims; TruStage answer window 11/15 |
| CYB-INC-009 | eMudhra G3: absent from Chromium root store v43 source; device release unconfirmed by Google; no financial-software breakage found | CONFIRMED · PRIMARY/ARTIFACT | Trust-chain class has NO OWNER |
| CYB-INC-020 / 021 / 022 | Quest (healthcare, NO OWNER; HENRY: no adverse reaction) · SBI · Korea 16 firms | CONFIRMED | Non-US / no-owner classes, flagged earlier |

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
- NYDFS is reachable by WebFetch. CISA KEV and SEC EDGAR are reachable.
- Runtime 10/29: Claude Code, Opus 5.5. Shell, git, Python, WebFetch/WebSearch and subagents are available.
- MCP servers mtnewswire, definite and Prisma failed to connect. SendMessage is loaded only on demand, and its use across sessions is untested.

## Known gaps carried

- **Fixed 2026-10-29** (Will 12:31 and 13:56 ET). Drills 36/36; mutation-checked.
  - **Leg 5:** a live incident row with no date now alerts.
  - **Leg 7:** listings already marked handled (`KEV-SEEN`) are quiet.
  - **Leg 8:** hits not filed under Item 1.05 are info only.
  - **Leg 9:** boilerplate filings are info only (16 of 16 real incidents still alert; `research/2026-10-29_wave-recheck/BOOT_LEG9_CALIBRATION.md`).
  - **Leg 10, new:** bank-vendor news. Google News headlines naming a chokepoint supplier and an incident word; covers press-release-only disclosures like Jack Henry's. Replaying the 9/3 feed, it catches Jack Henry and Sharetec.
- **Originals read 10/29.** Jack Henry's full release (PR Newswire copy), now CONFIRMED. The NYDFS 8/11 N-central letter: ⚠️ the "limited number of covered entities" line is a spokesperson quote, not in the letter. The Citizens 9/10 notice: no vendor, no count. A third N-central flaw was added to CISA's list 9/8.
- **Charter rotated** to 67% of budget: build history to `CHARTER_PROVENANCE.md`, file guide to `FILES.md`, both verbatim.
- **MCP connections:** mtnewswire and definite returned "endpoint not found" and Prisma timed out (10/29). Will disabled unused plugins at 14:42 ET; which ones was not verified by CYPHER. CYPHER depends on none of them; its routes are in `DATA_ROUTES.md`.
- **Leg 10 miss 11/05:** quiet while Finzly and Abrigo were live. Finzly's headline said "bank vendor" (body match, unlisted by design); Abrigo was not on the list (added). Leg 10 quiet does not mean no incident.
- **Leg 10 rebuilt 11/12** (KB-CYP-112): the single 21-name query saturated and missed N-able 11/09-11/11. Now 6 chunked queries with "zero-day"/"exploited"/"offline"; drills cover the file path only, the chunked path was witnessed live (113 items, N-able listed).
- **Not done 11/12 (carried, skipped):** SonicWall advisory re-read (063) and SecurCommunity check (064) from the 11/12 list; AG breach portals for Abrigo; Insight CU's own notice.
- **Search lesson:** a re-check of row 8 must search trade press (American Banker, Banking Dive, CU Times) for "offline"/"precaution", not only operator pages.

## Dated next

| Date | Check |
|---|---|
| 11/13 | GMO results briefing · Kiteworks second look |
| 11/15 · 11/16 | TruStage answer window · Arkéa weekly look |
| 11/18 · 11/19 | row 9 equity test (HENRY) · wave 7-day clock, cluster watch, Abrigo, ConnectWise, **Able2Shell/MSP one look** (incl. Insight notice for CYP-03), SonicWall 063, SecurCommunity 064 |
| 11/20 | **R1 flip test (P1)** |

## BOTTOM LINE

The October PHP2Shell wave is still open with one trigger fired (CISA's exploitation listing, 10/26); the 11/12 re-check found no bank, credit union or banking vendor named as its victim, so nothing else has fired. The week's real movement is in the managed-IT-provider channel, off-wave: N-able's N-central had 33 alleged zero-days published and went offline worldwide for about 35 hours (fixed, scanning seen, no compromise stated, a bypass claim under investigation today), ConnectWise is investigating abuse of ScreenConnect add-ons, and a ransomware group tied to the August N-central flaw has listed five US banks and a Florida credit union, two of them confirmed. The most important unconfirmed lead is whether any bank or credit union names N-central or ScreenConnect as its way in during this window (that would resolve CYP-03); Arkéa's provider is still unnamed. Next wakes: 11/13 GMO and Kiteworks, 11/16 Arkéa, 11/18 row 9, 11/19 MSP one look and wave clock, 11/20 flip test, through PROME's summons check.
