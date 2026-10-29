# October 2026 cyber wave, one week on: re-placement and escalation checklist (rerun)
**Date:** 2026-10-29 (checks 16:43–16:50 UTC / 12:43–12:50 ET) | **Mode:** Thesis | **Confidence:** High on the checklist states (primary pulls) · Medium on placement (one unnamed vendor-claimed compromise carries the movement) | **Request:** REQ-DEWEY-20261022-008R (WALTER standing authority; base REQ-008) | **Base report:** `output/2026-10-22_cyber-wave-systemic-base-rates.md` §5

## Key Finding

**Still Log4Shell-like on outcomes; edged one step toward MOVEit on a single axis.** There is now a vendor-reported production compromise with credential theft: the security firm Dream says it found 25 servers rooted, three of them in a "US government-affiliated environment", with the victim unnamed. But nothing in the MOVEit signature has appeared. There is no named victim, no victim list, no bank or core-vendor victim, no material-incident 8-K, no insurer catastrophe designation and no bank-stock damage.
- **CISA's listing of both flaws as actively exploited (10/26, row 2 FIRED) does not discriminate between the two cases.** Log4Shell was listed one day after disclosure and MOVEit two days after; PHP2Shell took five.
- **Escalation to WALTER at intake:** not triggered. No named US bank or core-vendor victim and no insurer catastrophe designation were found as of 16:50 UTC.

## Evidence: escalation checklist, 10/22 vs 10/29

| # | Sign | 10/22 (~19:10Z) | 10/29 (16:43–16:50Z) | Source and date |
|---|---|---|---|---|
| 1 | Confirmed successful compromise | Not yet; leads unconfirmed | **Moved, not met.** (a) Dream (10/26): 25 servers rooted via a PHP2Shell + kernel-flaw (Fragnesia) chain, "artifacts confirm credential extraction"; victim **unnamed**, government link **inferred**; "Chinese-nexus" indicators; vendor marketing its product. (b) A researcher's honeypots logged 35 successful shell executions (10/24, favourable test setup). (c) Palo Alto: "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet", CVSS-4 exploit maturity ATTACKED, severity Critical since 10/27 16:40Z. No named organisation. Two earlier firm claims were withdrawn (Sophos, Palo Alto/Unit 42). | [VENDOR CLAIM: Dream, 10/26](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers) · [NEWS: The Register, 10/27](https://www.theregister.com/cyber-crime/2026/10/27/cisa-confirms-php2shell-under-attack-as-researchers-clock-successful-exploits/5305681) · [PRIMARY: Palo Alto advisory JSON, read 16:45Z](https://security.paloaltonetworks.com/CVE-2026-109618) |
| 2 | CISA KEV listing | Not listed | **LISTED 10/26**, federal due date 10/29; ransomware use "Unknown". Also added: Node.js/Brotli flaw CVE-2026-111497 (10/27, outside the PHP root) and Fragnesia CVE-2026-46300 (KEV dateAdded **10/28**; CYPHER's record says 10/27). | [PRIMARY: CISA KEV v2026.10.28, pulled 16:43Z, sha256 c72e8b7751209e75…](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) |
| 3 | Named US bank, credit union or core/digital-banking vendor victim | None | **None.** "No U.S. bank or credit union has yet publicly reported a compromise stemming from the PHP flaws" (10/23). Searches on 10/29 found no Fiserv, Jack Henry, FIS, Alkami or Q2 compromise. | [NEWS: American Banker, 10/23](https://www.americanbanker.com/news/banks-dodge-early-damage-from-php2shell-flaws) · DEWEY searches 10/29 |
| 4 | 8-K Item 1.05 (material cyber incident) | None (not swept) | **None.** EDGAR full-text: 19 Item 1.05 8-Ks since 7/1 (positive control; CYPHER's build check counted 18 to 10/22). Since 10/15 the only hit is AASP (10/26), filed under items 5.02/5.05/8.01, not 1.05. Zero filings mention PHP2Shell, Node2Shell or Fragnesia. | [PRIMARY: EDGAR full-text search, 10/29](https://efts.sec.gov/LATEST/search-index?q=%22Item%201.05%22&forms=8-K&dateRange=custom&startdt=2026-07-01&enddt=2026-10-29) |
| 5 | Regulator statement | NYDFS alert referenced, unread | **Read; nothing newer.** The NYDFS 10/22 letter tells firms to patch, take unpatchable systems offline and "coordinate with third-party service providers to assess exposure". No later NYDFS letter (page read 10/29). No other supervisory statement found (CYPHER checkers, 10/29). | [PRIMARY: NYDFS industry letters](https://www.dfs.ny.gov/industry_guidance/industry_letters) |
| 6 | PCS catastrophe designation or modeller loss estimate | None | **None found.** PCS is behind a subscription wall. CyberCube 10/23 is headed "Why PHP2Shell isn't a large-loss event today" (CYPHER, title only; DEWEY did not read it). | CYPHER RECORD 10/29 |
| 7 | State attribution (US/UK/EU) | None | **None.** Private only: Dream "Chinese-nexus" indicators; CYFIRMA and Microsoft per CYPHER. | CYPHER RECORD; Dream |
| 8 | Bank or payment outages outside Japan | None | **One precautionary pause, not a compromise:** MSUFCU ($8.9B) took its website and digital banking offline for about 24 hours (10/21–22) after patching warnings; branches, ATMs and cards stayed up; the systems were "developed by and maintained by MSUFCU, not a vendor". CYPHER grades it YELLOW on its pre-registered band. | [NEWS: American Banker, 10/23](https://www.americanbanker.com/news/banks-dodge-early-damage-from-php2shell-flaws) |
| 9 | Sustained equity move | Day 1–2 only | **Not met.** Since the 10/20 close: HACK +8.3% (peak 10/27), Palo Alto +10.8%, KRE +3.3%, XLF +2.2%, FIS +1.5%, JKHY +3.5%, FISV −0.2%. **Fortinet −20.9%, but it is an earnings reaction** (Q3 results 10/28, 8-K item 2.02; service revenue +13%), not a wave vector. The 20-trading-day rule runs to 11/18 (CYPHER). | DEWEY `scripts/event_window.py since --date 2026-10-20`, run ~12:47 ET, **intraday** · [PRIMARY: FTNT 8-K 10/28](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001262039&type=8-K) · [NEWS: Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-beats-q3-2026-estimates-but-shares-plunge-93CH-4981034) |

**Placement verdict.** Still **Log4Shell-like on outcomes**, moved **one step toward MOVEit** on evidence of an unnamed production compromise with credential theft. **What would move it to MOVEit:** a named victim tied to PHP2Shell (row 1 or 3), a leak-site victim list attributed to a PHP2Shell campaign, an Item 1.05 8-K citing PHP, or a PCS designation. **What would move it back:** Dream withdrawing or correcting its claim (CYPHER re-checks 11/04), as Sophos and Unit 42 did.

## Counter-Evidence

- **Against "moving toward MOVEit":**
  - The only production-compromise evidence is one security firm's post marketing its own product. The two earlier firm claims in this wave were withdrawn.
  - Reported exploit reliability is low on hardened appliances (relayed in search results, not verified here).
  - MOVEit's KEV entry already shows "Known" ransomware use; PHP2Shell's says "Unknown".
- **Against "still Log4Shell":**
  - Log4Shell never produced a confirmed mass compromise. This wave already has a credential-extracting intrusion against a government-linked environment within six days of disclosure.
  - MOVEit's victim list surfaced from day 14 onward. Day 8 is too early for silence to count as absence.

## Unknowns

- Who Dream's victim is, and which vendor's firewalls were rooted.
- Whether any 8-K Item 8.01 (non-material) cyber disclosure cites PHP: DEWEY did not sweep 8.01; CYPHER's boot leg 9 does.
- PCS's subscriber bulletins.
- Any non-public supervisory communication.

## Source Quality Assessment

The checklist states rest on primary pulls by DEWEY: the CISA KEV JSON, Palo Alto's advisory JSON, the EDGAR full-text search with a positive control, and the NYDFS page. The placement movement rests on one **vendor claim** (Dream), corroborated in direction by The Register's reporting and Palo Alto's "ATTACKED" rating, not by any named victim. Prices are intraday.

## References
See the inline links. Raw reads (KEV JSON, Palo Alto JSON) were kept in the session scratchpad only. To reproduce: `curl` the KEV feed (`https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`) and `https://security.paloaltonetworks.com/json/CVE-2026-109618`; run EDGAR full-text with `q="Item 1.05"&forms=8-K`; run `scripts/event_window.py since --date 2026-10-20 CIBR HACK FTNT PANW KRE XLF FISV FIS JKHY`.

## Process Report
- **Searches run:** 7 web searches and fetches, 6 EDGAR full-text queries, 2 JSON pulls, 1 price pull. Sized as a targeted update (no fan-out), because CYPHER's 10/29 record already covered the rows.
- **Data gaps:** PCS bulletins (subscription); the CyberCube piece was not read; 8.01 cyber 8-Ks were not swept.
- **Source frustrations:** EDGAR phrase search is inconsistent ("cybersecurity incident" returned 0 while "cybersecurity" returned 499; pagination returned 6 hits). The `"Item 1.05"` query with a positive-control window was the reliable route, matching CYPHER's boot leg 8.
- **Confidence:** High on states, Medium on placement.
- **Suggestions:** none new.
