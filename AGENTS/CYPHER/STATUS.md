# CYPHER STATUS

**Last Updated: 2026-10-29 12:09 ET** — the DOCKET L812 seven-day wave re-check is complete. All nine rows were re-dated: **1 FIRED (row 2), 8 NOT-FIRED**. No score changes: **22/40 raw, 16/40 adjusted**. Evidence: `research/2026-10-29_wave-recheck/RECORD.md`. The prior STATUS (10/26) was rotated verbatim to `archive/STATUS_ARCHIVE_2026-10-29.md` (cksum 3362934535).

> ~~FIRST-LIVE-SESSION BANNER~~ — **SPENT 2026-10-22.** Normal boot.

## Current judgment

**WAVE-2026-10 (PHP2Shell) is open, and the evidence has moved from "exploited somewhere" to "a successful compromise is reported, victim unnamed".**
- Palo Alto's own advisory (updated 10/29) says "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet". It raised the severity to Critical on 10/27.
- One security firm, Dream (blog post 10/26, a VENDOR CLAIM), reports a PHP2Shell + Fragnesia chain that rooted 24-25 firewalls, including a US government-affiliated network with credential extraction (CYB-INC-047).
- No victim is named, so under the registered rule (R1 needs a *named* organisation) **row 1 stays NOT-FIRED**. Two earlier firm claims in this wave were withdrawn or corrected (Unit 42, Sophos). Dream is therefore re-checked for a correction on 11/04.
- No US bank, credit union or core vendor is a named victim.
- One US credit union took digital banking down for about 24h as a precaution (CYB-INC-046). That is a YELLOW case under the pre-registered band, not a fire.
- Base rate: 0 of 5 past waves were systemic for banks (KB-CYP-001, DEWEY-inherited).

| Gauge | Reading | Canonical |
|---|---|---|
| Escalation rows, WAVE-2026-10 | **1 FIRED (row 2, KEV 10/26) · 8 NOT-FIRED**, all re-checked 2026-10-29 (row 2 terminal) | `workbook/ESCALATION_WATCH.tsv` |
| Convergence composite | **22/40 raw · 16/40 shared-root-adjusted** (VX-02/03/06 PHP2Shell cluster counted once at max 4). VX-02 held at 3, VX-06 held at 4 ORANGE (RED needs mass compromise or a late-surfacing victim list) | `workbook/VX.tsv` |
| Transmission map | 20 mechanisms: 7 CONFIRMED, 7 NOT-OBSERVED, 2 MODELED, 4 UNTESTED (unchanged since 10/26) | `workbook/FLOW.tsv` |
| Incident ledger | 47 rows (046 credit-union precautionary pause; 047 Dream firewall chain). 027 Node2Shell → CONFIRMED (CISA KEV 10/27) | `workbook/INCIDENTS.tsv` |
| Chokepoint map | 35 rows (CHK-34 TAAPS, CHK-35 interdealer venues, both added on BOND's request). **CHK-32 perimeter appliances: POSSIBLE → CONFIRMED wave touch** (Palo Alto's exploitation statement; no bank named) | `workbook/CHOKEPOINTS.tsv` |
| Predictions | CYP-01 30% · CYP-02 15% · CYP-03 15% · CYP-04 35%; all OPEN, none due (registered on Will's word 10/22–10/23) | `workbook/PREDICTIONS.tsv` |
| R1 two-way flip | Toward MOVEit: row 1 or 3 FIRES on or before 2026-11-20 (a named organisation). Toward Log4Shell: rows 1, 3 and 4 all NOT-FIRED at 11/20, with re-checks dated 11/13–11/20 | `workbook/EXIT_PROTOCOL.md` |

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

## Standing conditions

- **Event, not consequence.** **10 of 11 boundary owners confirmed:** GIBBS, WATT, VULCAN, FALCON, BRENT, LIQUID, OTTO, plus SHADE, HENRY and BOND on 10/29 (KB-CYP-062..064). SHADE graded the 10/26 KEV P1 as NONE for the insurer channel. **REGINALD is outstanding** (reminded 10/29).
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

- **Fixed 2026-10-29 (Will 12:31 ET), drills 33/33** (3 rotted drills repaired; 4 added; mutation-checked):
  - **Leg 5** now flags a blank or unparsable Last_Checked on ANY live incident row, not only REPORTED/ATTEMPTS-ONLY ones.
  - **Leg 7** stays quiet on listings the owner has marked `KEV-SEEN:<CVE>@<dateAdded>` in Watch_Keys (007, 014, 027 marked). It re-alerts if the date changes.
  - **Leg 8** shows hits without Item 1.05 in their EDGAR items as info only (the AASP audit charter).
  - **Leg 9** reads each hit's document and shows boilerplate as info only. Calibration: `research/2026-10-29_wave-recheck/BOOT_LEG9_CALIBRATION.md` (16 of 16 real incidents still alert, including SR Bancorp, which a simpler rule missed).
- Row 8 lesson: a re-check must search trade press (American Banker, Banking Dive, CU Today) for "offline"/"precaution", not only operator pages.

## Dated next

| Date | Check |
|---|---|
| 10/30 | DEWEY REQ-008 rerun (not out 10/29); Palo Alto remaining hotfix ETAs; GMO replacement-service checkpoint |
| 11/03 | Keystone erasure statement |
| 11/04 | **PHP2Shell +14d (P1):** rows 1, 3, 4; Dream correction or a named victim; ConnectWise restoration completion |
| 11/05 | Financial-claim pass: 036–040, 043 |
| 11/06 | Kiteworks victim check (advisory upd. 10/27, still no exploitation statement); GMO compensation; Capcom |
| 11/15 · 11/18 · 11/20 | TruStage answer window · row 9 equity test · **R1 flip test (P1)** |

## BOTTOM LINE

The October PHP2Shell wave is open. One escalation row has fired: CISA's 10/26 listing confirming the flaw is being exploited. This week the evidence moved further: Palo Alto confirms attacks on its firewall management interface, and one security firm reports a successful break-in at an unnamed US government-affiliated network. No bank, credit union or banking vendor is a named victim, and the one US credit union that went offline did so as a 24-hour precaution with payments untouched. The most important unconfirmed lead is whether a named victim surfaces behind the firewall compromises (the MOVEit pattern), checked next on 11/04, with Finzly the strongest financial-supplier claim. The next wakes are DEWEY's rerun on 10/30, the 11/04 two-week check and the 11/20 flip test.
