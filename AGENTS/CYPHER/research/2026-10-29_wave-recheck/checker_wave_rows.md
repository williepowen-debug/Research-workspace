# WAVE-2026-10 escalation rows: web re-check
Checker run 2026-10-29, ~11:59 to 12:30 EDT (`date` at start: Thu Oct 29 11:59:44 EDT 2026). Read-only; published pages only.
Window checked: changes since 2026-10-26. PRIMARY = the victim, the vendor's own advisory, a government agency, a filing, or an IR firm's own blog. Everything else is SECONDARY (a lead only).

## Row 1: named successful PHP2Shell compromise
**Verdict: NOTHING-NEW (no named victim). Exploitation evidence is MATERIALLY STRONGER.**
| Item | Basis | Date | URL | Verbatim |
|---|---|---|---|---|
| Dutch NCSC alert, unchanged since 10/23 | PRIMARY | Bijgewerkt: 23 okt 2026 om 15:43 (in-text update 15:45) | https://www.ncsc.nl/alerts/update-php-kwetsbaarheden-nog-steeds-reden-om-direct-te-patchen | "Op dit moment is bij ons één melding bekend van mogelijk misbruik in het buitenland" ... "maar is niet bevestigd dat de aanval ook daadwerkelijk succesvol is geweest" (one possible case of misuse abroad, not confirmed successful). No victim named. NOTE: the desk's last read was the 10/22 16:01 stamp; this 10/23 update reads as a step-down: "large-scale misuse less likely than first assessed" (paraphrase) |
| Dream (Israeli IR/security firm), own blog | PRIMARY (self-reported; the post also promotes Dream's product) | October 26, 2026 | https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers | "Once rooted, the attacker zeroed in on three specific servers in a US government-affiliated environment." 25 servers rooted across US, JP, TW, KR (PHP2Shell + Fragnesia CVE-2026-46300 kernel LPE). "For security purposes, we are not disclosing the vendor or the affected versions." "We do not attribute this activity to a named threat actor." No victim named; no finance mention |
| Palo Alto Networks advisory | PRIMARY (vendor) | Published 2026-10-21; Updated 2026-10-29; 10/27 changelog: severity raised to Critical, urgency Highest | https://security.paloaltonetworks.com/CVE-2026-109618 | "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet." No device count, no victims. (I could not establish which changelog date added the exploitation sentence) |
| Hacker News on Dream + PANW | SECONDARY | Oct 28 and Oct 29, 2026 | https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html ; https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html | Suggests (does not confirm) Dream's unnamed "large vendor's firewall" = PANW; the outlet labels the actor "suspected China-nexus" |
| Aviatrix write-up | SECONDARY (a summary of THN/Dream; does its own product marketing) | October 29, 2026 | https://aviatrix.ai/threat-research-center/php2shell-attack-roots-25-servers-cve-2026-109618-us-government-breach/ | "a U.S. government-affiliated organization"; attribution unsourced. Do not cite |
| SOCRadar Japanese real-estate extortion | SECONDARY lead; the report itself says there is no link | per SOCRadar | https://socradar.io/blog/php2shell-weaponized-japanese-real-estate-extortion/ | The intrusions ran Oct 9-11; the PHP2Shell tooling was added to the server only Oct 21; the files show no tie to those intrusions |
| Unit 42 retraction (prior, still standing) | SECONDARY via search | 10/25 | (search summaries) | "We are unable to confirm that initial access is associated with the specific PHP2Shell CVEs." |
Searched: the NCSC page; "PHP2Shell CVE-2026-109618 compromise victim"; "PHP2Shell ... named victim breach Oct 27/28"; "PHP2Shell ransomware leak site claim / 8-K"; the Dream and PANW primaries. Result: an IR firm's own report of a successful compromise (Dream) has an UNNAMED victim. ATTEMPTS-ONLY no longer describes the wave: the state is now UNNAMED COMPROMISE REPORTED BY ONE IR FIRM, with vendor-confirmed active exploitation (PANW). The owner should decide whether "named" is the fire condition, because a government-affiliated victim that a firm notified directly is the MOVEit/SolarWinds late-surfacing shape. No 8-K full-text search was run (boot.py leg 4 covers that).

## Row 3: named US bank, credit union or core/digital-banking vendor victim
**Verdict: NOTHING-NEW (no victim).** See row 8 for a US credit union's SELF-TAKEN outage. Its own statement said "no indication any member information has been compromised" (paraphrase relayed by WILX/WLNS; SECONDARY).
| Searched | Result |
|---|---|
| "PHP2Shell Fiserv / Jack Henry / FIS / Q2 / Alkami / NCR Voyix statement" | Nothing found (only profile pages, and an NCR Voyix earnings transcript with no incident) |
| ConnectWise trust advisories page, updates 10/26 14:00 UTC and 10/28 16:00 UTC (PRIMARY) https://www.connectwise.com/company/trust/advisories | Phased Cloud Backup restore. Partners "must re-authorize each Microsoft 365 tenant using the new application". No confirmed customer-tenant compromise; no financial institution named. The 10/21 entry lists "financial services" among the sectors Storm-0940 TARGETED, not victims. Only the first 100k of 188k characters was read |
| Kiteworks advisory (see below) | No exploitation statement |
| American Banker 10/23 (SECONDARY) https://www.americanbanker.com/news/banks-dodge-early-damage-from-php2shell-flaws | "No U.S. bank or credit union has yet publicly reported a compromise stemming from the PHP flaws." |

## Row 5: regulator statement signalling supervisory concern
**Verdict: NOTHING-NEW.**
| Item | Basis | Date | URL | Note |
|---|---|---|---|---|
| NYDFS industry-letters index | PRIMARY | read 10/29 | https://www.dfs.ny.gov/industry_guidance/industry_letters | The latest letter is still 2026-10-22, "Cybersecurity Alert: Critical Vulnerabilities in PHP that Require Immediate Patching" (already adjudicated NOT-FIRED). Nothing after 10/22. The page fetched fine on 10/29, although DATA_ROUTES records a 403 |
Searched: "PHP2Shell NYDFS/OCC/FDIC/FFIEC/NCUA/FS-ISAC/ECB banks"; "NCUA/FFIEC/FS-ISAC/OCC PHP vulnerability statement Oct 2026". Nothing found from the Fed, OCC, FDIC, FFIEC, NCUA, FS-ISAC or ECB. A YouTube video titled "PHP2Shell Alert: New York Warns Financial Institutions" maps to the 10/22 NYDFS letter. Germany's BSI "take offline if in doubt" is routine guidance (secondary).

## Row 6: PCS designation or modeler industry-loss estimate
**Verdict: NOTHING-NEW.**
| Item | Basis | Date | URL | Verbatim |
|---|---|---|---|---|
| CyberCube insight | PRIMARY (modeler) | Oct 23 2026 (before the window; not in the 10/23 row note) | https://insights.cybcube.com/en/php2shell-cyber-insurance-ai-vulnerability | "PHP2Shell hasn't caused a cyber catastrophe yet, but risk remains elevated"; "Why PHP2Shell isn't a large-loss event today". No dollar figure |
| The Insurer analysis | SECONDARY | 2026-10-27 | https://www.theinsurer.com/ti/analysis/cyber-insurers-brace-for-long-tail-losses-from-php2shell-flaws-systemic-hit-2026-10-27/ | Headline: "long-tail losses ... systemic hit dodged for now". No figure seen |
| Carrier Management | SECONDARY | 2026-10-27 | https://www.carriermanagement.com/news/2026/10/27/292995.htm | Aggregation risk; no figure seen |
Searched: "PHP2Shell insured loss estimate CyberCube / Parametrix / PCS catastrophe". No PCS mention found (MIRROR-WALLED). No Parametrix item. No quantified industry-loss estimate found.

## Row 7: US/UK/EU government state attribution
**Verdict: NOTHING-NEW.**
| Item | Basis | Date | URL | Note |
|---|---|---|---|---|
| CISA AA26-293A | PRIMARY | October 20, 2026 | https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a | "#StopRansomware: SafePay Ransomware". It does NOT cover PHP2Shell or ConnectWise and makes no state attribution; ScreenConnect appears only as a SafePay tool. A search snippet had linked it to ConnectWise; that link is false |
| Dream | PRIMARY (IR firm) | 10/26 | above | "We do not attribute this activity to a named threat actor" ("Chinese-nexus" indicators). Not a government |
| CYFIRMA (North Korea / "June 2026 Minjun") | SECONDARY via SBS 10/24 | 10/24 | https://news.sbs.co.kr/english/article.do?news_id=N1008812986 | A private firm, moderate confidence on Lazarus. South Korea's MSIT/KISA 10/22 "Caution" alert carries no attribution. KR is not US/UK/EU anyway |
| ConnectWise advisory | PRIMARY (vendor) | 10/21 22:00 UTC entry | connectwise advisories | "a China state-aligned group was responsible", citing Microsoft = VENDOR attribution |
Searched: "CISA FBI attribution ConnectWise Cloud Backup China Storm-0940"; "PHP2Shell CISA advisory attribution China / North Korea government NCSC UK"; "NSA advisory PHP2Shell". The NSA's 10/21 advisory, "Critical Patches Recommended for PHP Vulnerabilities" (seen through secondaries only), is patch guidance with no attribution. Nothing found from any US/UK/EU government.

## Row 8: operator-confirmed loss-of-service outage at a bank or payment system outside Japan
**Verdict: FIRE-CANDIDATE for owner adjudication. The event predates the window (10/21 to 10/22) and is NOT in the desk's files (grep "msufcu" returned nothing).**
| Item | Basis | Date | URL | Verbatim |
|---|---|---|---|---|
| MSUFCU (Michigan State University FCU, $8.9B, East Lansing) took its website and digital banking offline after the federal PHP warnings | SECONDARY quoting the operator (I found no msufcu.org statement) | AB published Oct 23 2026, 12:18 pm EDT; outage Wed 10/21; restored Thu 10/22 (WILX: website 8:28 am, online/mobile banking 12:20 pm); some features still returning Fri 10/23 | https://www.americanbanker.com/news/banks-dodge-early-damage-from-php2shell-flaws ; https://www.wilx.com/2026/10/21/msufcu-takes-website-digital-banking-offline-amid-cyberscurity-warning-fbi/ | AB: "took its website and digital banking offline Wednesday after the federal warnings". The systems "ran PHP and were vulnerable to the flaws". Built in-house, "not a vendor". Chief of staff Allison Horn: "There is no impact to member information at this time." Branches, the call center, ATMs, cards and payment processing stayed up. CEO April Clobes (per WILX/WLNS): "this disruption has been frustrating and is taking longer than any of us would like" |
Adjudication question for the owner: this was a PRECAUTIONARY, self-taken outage of about 24 hours, not a compromise, and payments were unaffected. The row note excluded Japan's pauses as "precautionary AND inside Japan", so it is ambiguous whether precaution alone disqualifies an outage. The fire condition says "loss-of-service": that is met for digital banking but not for payments. The owner would be REGINALD/LIQUID. Also searched "PHP2Shell bank outage payment system disruption Europe/US Oct 27". Europe: only government sites and Orange (a telecom). Northeast Times 10/24, "Two PHP flaws send banks, hospitals and retailers offline" (SECONDARY, not opened). No payment-system outage found.

## Kiteworks advisory
| Item | Basis | Date | URL | Verbatim |
|---|---|---|---|---|
| Kiteworks PHP2Shell advisory | PRIMARY | "Last updated: 2026-10-27 8:00 PDT" (CHANGED from the desk's 2026-10-22 12:30 PDT read) | https://info.kiteworks.com/php2-vulnerability-advisory | Still only: "An unauthenticated attacker could exploit these vulnerabilities to achieve remote code execution." It makes no exploitation, compromise, IOC or "no evidence" statement and has no dated changelog, so I could not identify what the 10/27 update changed |
