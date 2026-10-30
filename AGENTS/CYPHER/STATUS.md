# CYPHER STATUS

**Last Updated: 2026-10-30 11:0x EDT — spawned session (PROME prome-c5, WQ-550 commission on Will's word 10:46 ET, DOCKET L878).**
- **WQ-550 leg 1 done** (`research/2026-10-30_wq550-leg1/RECORD.md`), four reads on the Binance incident:
  - **The headline premise was a clock mismatch.** "COIN −13.7% vs BTC −1.3%" compares the equity move since Thursday's 4pm close with a bitcoin move since midnight UTC. On the equity clock bitcoin is −4.15% and the Nasdaq-100 −2.6%, so Coinbase is down about 3× bitcoin, not 10×.
  - Beta check (IBIT + QQQ, 120 days): only COIN has a residual (−5.7pp), and its own Q3 results (10/29) and two target cuts (10/30) overlap it. MSTR, HOOD, CRCL and the rest sit within their beta. The venue risk shows in Binance's token BNB (−5.7%), not in US stocks.
  - **Venue contagion:** none found. No other exchange has halted. Aave froze its affected lending markets. Binance withdrawals are still off on all 1,447 pairs (14:51Z).
  - **Stablecoins:** the freezes are unchanged and nothing has been burned. There is no redemption surge in the first daily print. The redemption test opens when withdrawals reopen.
  - **Counterparties:** market makers Wintermute (<20% of net equity) and GSR (<5%); no bank, prime broker or lender is named.
- **Leg 2 registered** (11/02, P1). The VX-CYP-02 letter caveat went to PROME before the grade. Facts went to LIQUID (CHK-40) and HENRY (equity tape). Inbox drained (2 items; FIS and Q2 WATCH_FOR phrases ADOPTED). No score moved.
- **Earlier 10/30 (09:2x, prome-a9, L871):** Binance first read at the primaries (CYB-INC-055; `research/2026-10-30_binance-first-read/RECORD.md`); inbox drain of 10 items (CYB-INC-056 Fiserv/Cl0p claim, 057 Polymarket, KB-CYP-082 EO 14421); Palo Alto hotfix ETAs retired; GMO re-dated to 10/31.

> ~~FIRST-LIVE-SESSION BANNER~~ — **SPENT 2026-10-22.** Normal boot.

## Current judgment

**WAVE-2026-10 (PHP2Shell) is open, and the evidence has moved from "exploited somewhere" to "a successful compromise is reported, victim unnamed".**
- Palo Alto's own advisory (updated 10/29) says "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet". It raised the severity to Critical on 10/27.
- One security firm, Dream (blog post 10/26, a VENDOR CLAIM), reports a PHP2Shell + Fragnesia chain that rooted 24-25 firewalls, including a US government-affiliated network with credential extraction (CYB-INC-047).
- No victim is named, so under the registered rule (R1 needs a *named* organisation) **row 1 stays NOT-FIRED**. Two earlier firm claims in this wave were withdrawn or corrected (Unit 42, Sophos). Dream is therefore re-checked for a correction on 11/04.
- No US bank, credit union or core vendor is a named victim.
- One US credit union took digital banking down for about 24h as a precaution (CYB-INC-046). That is a YELLOW case under the pre-registered band, not a fire.
- Base rate: 0 of 5 past waves were systemic for banks (KB-CYP-001, DEWEY-inherited).
- **DEWEY's rerun (008R, 10/29) agrees:** still Log4Shell-like on outcomes, one step toward MOVEit on Dream's claim alone; KEV timing does not separate the two shapes (Log4Shell +1 day, MOVEit +2, PHP2Shell +5). Fortinet's -20.9% is its earnings, not the wave (KB-CYP-071..073).

| Gauge | Reading | Canonical |
|---|---|---|
| Escalation rows, WAVE-2026-10 | **1 FIRED (row 2, KEV 10/26) · 8 NOT-FIRED**, all re-checked 2026-10-29 (row 2 terminal) | `workbook/ESCALATION_WATCH.tsv` |
| Convergence composite | **22/40 raw · 16/40 shared-root-adjusted** (VX-02/03/06 PHP2Shell cluster counted once at max 4). VX-02 held at 3, VX-06 held at 4 ORANGE (RED needs mass compromise or a late-surfacing victim list) | `workbook/VX.tsv` |
| Transmission map | 20 mechanisms: 7 CONFIRMED, 7 NOT-OBSERVED, 2 MODELED, 4 UNTESTED (unchanged since 10/26) | `workbook/FLOW.tsv` |
| Incident ledger | 57 rows. 10/30: 055 Binance, 056 Fiserv/Cl0p claim (Aug, denied), 057 Polymarket halt; 032 GMO updated. 10/29: 046 credit-union PHP pause; 047 Dream firewall chain; 048 Jack Henry; 049 Central Bank of India; 050 Sharetec; 051 N-central; 052 NY bank closure; 053 Citizens CA AG notice; 054 US commissary freezers. 027 Node2Shell -> CONFIRMED (KEV 10/27) | `workbook/INCIDENTS.tsv` |
| Chokepoint map | 40 rows: CHK-40 USD stablecoin issuers (10/30, NONE-KNOWN); CHK-34/35 Treasury nodes (BOND); CHK-36 Sharetec, CHK-37 print/mail vendors (Sefas), CHK-38 N-able N-central, CHK-39 SitusAMC. CHK-03 Jack Henry CONFIRMED-OFF-WAVE; CHK-32 perimeter appliances CONFIRMED wave touch | `workbook/CHOKEPOINTS.tsv` |
| Predictions | CYP-01 30% · CYP-02 15% · CYP-03 15% · CYP-04 35%; all OPEN, none due (registered on Will's word 10/22–10/23) | `workbook/PREDICTIONS.tsv` |
| R1 two-way flip | Toward MOVEit: row 1 or 3 FIRES on or before 2026-11-20 (a named organisation). Toward Log4Shell: rows 1, 3 and 4 all NOT-FIRED at 11/20, with re-checks dated 11/13–11/20 | `workbook/EXIT_PROTOCOL.md` |

## Binance, 10/29 (OFF-WAVE · NO-OWNER class · canonical CYB-INC-055)

| Item | Reading (2026-10-30) | Basis |
|---|---|---|
| What happened | Unauthorized withdrawals from hot wallets; Binance points to a compromised DevOps engineer laptop that reached a service container, and says it found "no evidence of any wallet private key leak". Its CEO later said "additional points of breach" | Notice PRIMARY-VERIFIED; CEO SECONDARY |
| Size | Binance: ~$6.3B estimated total IMPACT and ~$3B frozen, so about $3.3B is not frozen. Arkham: $6.01B taken, $2.80B frozen | OWNER-ASSERTED / SECONDARY |
| Issuer freezes | On Ethereum: USDC $823.00M and USDT $1,350.46M traced (+$30M probable), frozen 37–41 min after the first drain; none destroyed. **Unchanged at 14:54Z re-tally.** Tron not checked | PRIMARY-VERIFIED on-chain |
| Withdrawals | Off on 0 of 1,447 coin-network pairs at 13:07Z and **still at 14:51Z**; deposits on. Binance account "45 hours" (from its latest update) | ARTIFACT-VERIFIED / SECONDARY |
| Attribution | TRM and Chainalysis (private): TraderTraitor. No government attribution found | SECONDARY / SEARCH-NOT-FOUND |
| Transmission (WQ-550 leg 1) | No other exchange halted; Aave froze its affected markets. Market makers Wintermute (<20% of net equity) and GSR (<5%) are exposed; no bank, prime broker or lender is named. US crypto stocks move with bitcoin and the Nasdaq on the equity clock. COIN's residual overlaps its own earnings | SECONDARY / ARTIFACT-VERIFIED (prices) |
| Map | Not a CHK event: the issuers were the control that worked. New class row CHK-40 (USD stablecoin issuers, NONE-KNOWN) | desk judgment |
| Watch / vectors | No escalation row (not PHP2Shell). VX-02 held at 3. **Answered by Will (WQ-550 C):** grade on the letter as written at 11/02, note that the composition does not match the mechanism, and draft a prospective re-cut. ⚠️ The ORANGE cell says "bank or payment operator" and Binance calls its pause a "precaution" (the YELLOW cell's word); this went to PROME before the grade (leg-1 RECORD §5) | desk judgment |
| Do not relay | "$5B hack" · "$6.3B stolen" · "largest bank heist" · "CZ confirms" · "North Korea did it" · "user funds lost" (first-read RECORD §9) · "COIN down 10× bitcoin" · "Binance halted trading" · "Tether and Circle said they froze $2.36B" (leg-1 RECORD §6) | — |

## Open wave — WAVE-2026-10 (all rows State_As_Of 2026-10-29 except row 2, terminal 10/26)

| Row | Sign | State | 10/29 reading |
|---|---|---|---|
| 1 | Named successful PHP2Shell compromise | NOT-FIRED | Dream reports an unnamed compromise (VENDOR CLAIM); Palo Alto confirms active exploitation; no named organisation. NCSC alert unchanged since 10/23 |
| 2 | KEV listing of both CVEs | **FIRED 10/26** | KEV v2026.10.28 still lists both; federal due date 10/29 |
| 3 | Named US bank / CU / core-vendor victim | NOT-FIRED | None. Finzly is still a claim; the credit-union pause is not a compromise |
| 4 | Bank/vendor 8-K Item 1.05 | NOT-FIRED | Only AASP since 10/22 (rejected 10/26). Hanmi 10/29 leg-9 hit = dividend boilerplate |
| 5 | Regulator supervisory concern | NOT-FIRED | NYDFS 10/22 letter remains the latest; no other agency |
| 6 | PCS designation / loss estimate | NOT-FIRED | None; CyberCube 10/23 headline "isn't a large-loss event today" |
| 7 | Government state attribution | NOT-FIRED | Private attributions only (Dream, CYFIRMA, Microsoft) |
| 8 | Bank/payment outage outside Japan | NOT-FIRED (candidate adjudicated) | Credit union: precautionary, ~24h, digital-only, payments up = YELLOW band as registered 10/22. Missed at the 10/23 check |
| 9 | Sustained equity move | NOT-FIRED | Test 11/18; Palo Alto flagged to VULCAN/HENRY as a possible vector vendor |

## Incidents worth knowing (canonical: `workbook/INCIDENTS.tsv`)

| ID | Event | State | Why it matters |
|---|---|---|---|
| CYB-INC-007 | PHP2Shell root CVEs in KEV since 10/26 | CONFIRMED (flaw level) · PRIMARY-VERIFIED | The wave root |
| CYB-INC-047 | Dream: PHP2Shell + Fragnesia rooted 24-25 firewalls; a US government-affiliated network had credentials extracted; victim and vendor undisclosed | REPORTED · ARTIFACT-VERIFIED (VENDOR CLAIM) | First production-compromise report not yet withdrawn; MOVEit-shape risk if a name surfaces |
| CYB-INC-046 | A US credit union ($8.9B) paused its in-house PHP website and digital banking ~24h on 10/21; payments up; no member impact stated | REPORTED · SECONDARY (operator quoted) | First US FI service pause for this wave; the row 8 band boundary case |
| CYB-INC-027 | Node2Shell CVE-2026-111497: CISA KEV 10/27 (listed under Google Brotli); AI-found (OpenAI Codex Security) | CONFIRMED (flaw level) · PRIMARY-VERIFIED | Off-root; AI-found flaw exploited within 6 days of the fix; VULCAN told |
| CYB-INC-018 | ConnectWise / Storm-0940 supply chain: phased restoration started 10/28 (M365 first); **not restored** | CONFIRMED · PRIMARY-VERIFIED | MSP channel; no FI named |
| CYB-INC-037 | Finzly payments middleware extortion claim; company "investigating", "fully operational" (AB 10/20) | REPORTED · SECONDARY | Strongest unconfirmed financial-supplier lead |
| CYB-INC-043 | Park24: ~1.46M accounts eligible for JPY 3,000 (~JPY 4.4B); JPY 5.5B loss; net forecast cut 44.0B → 38.5B | REPORTED · SECONDARY | Listed-company earnings channel (SAM/OTTO); issuer notice unread |
| CYB-INC-015 / 017 | River Financial (off-wave ransomware, 8-K) · TruStage (CU vendor outage since 7/11) | CONFIRMED · PRIMARY-VERIFIED | Off-wave US financial victims; TruStage answer window 11/15 |
| CYB-INC-009 | eMudhra G3: absent from Chromium root store v43 source; device release unconfirmed by Google; no financial-software breakage found | CONFIRMED · PRIMARY/ARTIFACT | Trust-chain class has NO OWNER |
| CYB-INC-020 / 021 / 022 | Quest (healthcare, NO OWNER; HENRY: no adverse reaction) · SBI · Korea 16 firms | CONFIRMED | Non-US / no-owner classes, flagged earlier |

**Do-not-relay, 13 claims** (canonical `research/2026-10-23_news-sweep-and-relay-pattern.md` §4). 12 of the 13 overstate toward alarm. A news outlet reporting an agency is a lead, never row-1 evidence. **Add:** "FEC hacked" is Reuters' framing of an internal email; FEC's status page says "outage" (board_log 10/29).

## News sweep 10/29 (Will's ask; `research/2026-10-29_news-sweep/RECORD.md`)

- **Jack Henry (core vendor for >900 banks, >700 CUs) had a cyber incident on 8/31** (CYB-INC-048): voice phishing by ShinyHunters, corporate environment only, PII of <10 client FIs, no processing disruption, no 8-K. The 10/23 map missed it because it was press-release-only; core-vendor checks now include newsrooms and trade press (KB-CYP-074).
- **Central Bank of India** (CYB-INC-049): ~$1.7M moved via 187 unauthorized transfers through payment messaging 10/15-17. Non-US, NO OWNER, off-wave.
- **Sharetec** (CYB-INC-050, CHK-36): 9/15 cooling failure took 23 credit unions offline for days. An accident, but the multi-institution shape row 8 watches for.
- **Print/mail vendors** (CHK-37): Citizens/Frost and Citi customer data in 2026 came through them.
- **Second pass (bank software, 13:32 ET):** **the MSP route has carried traffic.** An N-able N-central flaw (MSP remote-management tool) was exploited from 7/31, NYDFS warned on 8/11 that attackers use compromised MSPs to move into their customers' networks; a NYDFS spokesperson told American Banker it was "aware of impact to a limited number of covered entities" (CYB-INC-051, CHK-38). A small NY bank closed its branches about a week citing a vendor flaw (052; the N-central link is unconfirmed). The 10/23 read "little observed traffic" (KB-CYP-020) is revised. Also: Citizens' new CA AG notice, breach 9/10 (053); Sefas named behind Frost's April data (CHK-37); SitusAMC (CHK-39). Base rate ~1 bank-supplier incident a month, 3 in August (KB-CYP-076).
- **Standing watch (Will 13:29 ET, "keep an eye out for bank issues like that"):** bank-vendor and payment-plumbing cluster watch, weekly from 11/05. Escalates on 2+ new confirmed incidents at distinct core, CU-vendor or payment-messaging suppliers within 30 days, or one multi-institution processing outage of 1 business day or more (catalyst row; WALTER asked to route matching stories).
- Nothing new on PHP2Shell victims, file-transfer products, Fiserv/FIS/Broadridge, insurers or election-week warnings. Packets: WALTER, REGINALD, LIQUID, GIBBS, PROME.

**Banking sub-folder (Will 13:49 ET):** `banking/`: the bank cyber / software / vendor-risk thread. README indexes the rows; `THREAD_2026-10-29.md` is the current reading.

## Standing conditions

- **Event, not consequence.** **All 11 boundary owners confirmed** (REGINALD 10/30, with one amendment: credit-union-only items go to it as P3 context; a multi-institution outage of 1 business day or more stays P2; KB-CYP-084). The others: GIBBS, WATT, VULCAN, FALCON, BRENT, LIQUID, OTTO, SHADE, HENRY, BOND (KB-CYP-062..064).
- **Intake rule** (WALTER v0.48): ledger rows only for financial or chokepoint victims, desk-cited claims, or claims CYPHER checked. Everything else goes in board_log notes (`inbox/PROTOCOL.md` rule 0).
- **Recorded disagreement:** DEWEY recommended a WALTER watch, not a desk; Will chose a desk. R0 review on 2026-12-17.
- **Guardrails:** no scanning or probing of institutions. Packets carry counts; names stay in research files.
- **No book** (`TRADE.md`, FROZEN).
- **Approvals:** Tier-2 event ownership and the existing watch. CYP-01..04 registered on Will's word. WQ-500 (no healthcare owner) and WQ-501 (CYBER group) ruled. No new prediction, threshold or capital authority. The L812 session ran on Will's "go" (10/29 11:59 ET).

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
- **Search lesson:** a re-check of row 8 must search trade press (American Banker, Banking Dive, CU Times) for "offline"/"precaution", not only operator pages.

## Dated next

| Date | Check |
|---|---|
| 10/31 | GMO replacement-service / payment procedure (the 10/30 JST deliverable was not yet posted) |
| 11/02 | **WQ-550 leg 2 (P1):** the same four reads at the Binance reopening, plus the VX-CYP-02 grade on its letter, the prospective re-cut draft, and a recommendation on whether crypto venues need a standing owner (Will's word) |
| 11/03 | Keystone erasure statement |
| 11/04 | **PHP2Shell +14d (P1):** rows 1, 3, 4; Dream correction or a named victim; ConnectWise restoration completion |
| 11/05 | Financial-claim pass: 036–040, 043 |
| 11/06 | Row 9 magnitude decision (due to PROME by 11/10) · Kiteworks victim check (advisory upd. 10/27, still no exploitation statement); GMO compensation; Capcom |
| 11/15 · 11/18 · 11/20 | TruStage answer window · row 9 equity test · **R1 flip test (P1)** |

## BOTTOM LINE

The October PHP2Shell wave is still open, with one trigger fired (CISA's exploitation listing, 10/26) and no bank, credit union or banking vendor named as a victim. The big new event sits outside the wave. Binance confirms a theft with an estimated $6.3B impact, about $3B of it frozen. Tether and Circle froze the attacker's stablecoins within about 40 minutes, and CYPHER verified that freeze on-chain. No bank or mapped supplier is touched, and crypto venues have no consequence owner in the fleet. Today's transmission read found no contagion to other exchanges or banks. US crypto stocks are moving with bitcoin and the Nasdaq once both are measured from Thursday's close. The most important unconfirmed points are whether Binance reopens withdrawals and whether stablecoin redemptions follow (leg 2, 11/02) and, in the wave, whether a named victim surfaces behind the firewall break-ins (checked 11/04). Next wakes: GMO 10/31, Binance 11/02, the 11/04 two-week check, the 11/05 bank-vendor watch and the 11/20 flip test.
