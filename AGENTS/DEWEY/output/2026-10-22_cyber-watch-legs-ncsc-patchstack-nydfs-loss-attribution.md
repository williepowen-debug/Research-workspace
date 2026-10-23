# CYPHER escalation-watch legs: Dutch NCSC and Patchstack primaries, victim sweep, NYDFS alert, loss estimates, attribution (WAVE-2026-10 rows 1, 5, 6, 7)
**Date:** 2026-10-22 (research 19:31–19:37 ET; committed 19:37:40 ET (9762a984f). Stamp corrected 20:39 ET, as the original "19:40" was typed, not clocked) | **Mode:** Thesis | **Confidence:** High on what the primaries say; Low on the world (no victim found means attempts only, not "no damage")
**Commission:** CYPHER request by live-session message, 2026-10-22 ~19:31 ET (legs 1, 2, 3 in that order; leg 4 skipped), inside Will's in-session direction to DEWEY to "continue working on the cyber threat with WALTER and CYPHER". No REQ file. WALTER acknowledged the split from the routing side.

## Key Finding
**Row 1 stays NOT-FIRED, and its state is ATTEMPTS-ONLY.** The Dutch NCSC's "first signs of successful misuse" is now pinned at its primary: the NCSC alert, updated 22 Oct 16:00 CEST (14:00Z), says *"Op dit moment onderzoekt het NCSC eerste signalen van succesvol misbruik"* ("the NCSC is currently investigating initial signals of successful misuse"). It names no victim and gives no detail, and NOS reports the investigation "could take months". Patchstack's reversal is also pinned at its primary. At 07:34Z on 21 Oct it posted *"Multiple active exploitation incidents reported to Patchstack by hosting partners"*. At 13:57Z it posted *"our telemetry shows only probing attacks, with no hard evidence of breaches yet"*. No named, confirmed successful PHP2Shell compromise turned up in any source swept through about 23:35Z on 10/22. **Row 5 (NYDFS): REACHED.** It is an NYDFS Industry Letter dated 22 Oct 2026 to "DFS-Regulated Entities", titled "Cybersecurity Alert: Critical Vulnerabilities in PHP that Require Immediate Patching". It covers patching, inventory (including third-party service providers) and taking unpatchable systems offline. It **says nothing about exploitation or compromise at any regulated entity**, sets no deadline, and adds no reporting duty. This meets row 5's sign *as written*: a regulator statement now exists. In substance it is routine patch guidance, not a supervisory-concern signal. CYPHER adjudicates. **Rows 6 and 7: none found.** There is no modeler or industry loss estimate, PCS is MIRROR-WALLED, and no US, UK or EU government has named a culprit. One *vendor* attribution sits next to the wave: Microsoft "assesses" that the China-aligned group Storm-0940 ran the ConnectWise Cloud Backup supply-chain compromise. Microsoft names financial services among the targeted sectors. It is not PHP2Shell and it is not a government statement.

## Evidence

### Leg 1 — Row 1: confirmed successful PHP2Shell compromise

**1a. The Dutch NCSC's statements, in time order.** They move in one direction, from "attempts only" to "investigating first signs of success". None of them is a confirmation.

| When (local CEST; UTC = −2h) | What the NCSC said | Source | Basis (Class 12) |
|---|---|---|---|
| 21 Oct evening (TV, *Pauw & De Wit*) | Director Matthijs van Amelsfort: the NCSC "heeft nog geen actief misbruik waargenomen" (has not yet observed active misuse); it sees more traffic, which suggests scanning for vulnerable sites | [NEWS: iBestuur, 22 Oct](https://ibestuur.nl/digitale-weerbaarheid/digitale-veiligheid/ncsc-ziet-nog-geen-misbruik-van-php-lekken) (paraphrase of the TV remarks) | SECONDARY-SOURCE |
| 22 Oct 13:49 (ANP wire) | *"Tot dusver blijft het bij aanvalspogingen die wij zien"* ("so far what we see remains attack attempts"); *"Dat sluit toekomstig misbruik niet uit"* ("that does not rule out future misuse") | [NEWS: ANP via Welingelichte Kringen, 22 Oct 13:49](https://www.welingelichtekringen.nl/samenleving/ncsc-nog-geen-sprake-van-succesvol-misbruik-php-kwetsbaarheden) | SECONDARY-SOURCE |
| **22 Oct 16:00 (alert update; footer "Bijgewerkt 22 okt 2026 om 16:01")** | ***"Op dit moment onderzoekt het NCSC eerste signalen van succesvol misbruik."*** Also: *"Wacht daarom niet op signalen van misbruik, maar installeer de beschikbare beveiligingsupdates zo snel mogelijk."* ("so don't wait for signals of misuse; install the updates as soon as possible") | [PRIMARY: NCSC alert](https://www.ncsc.nl/alerts/update-php-kwetsbaarheden-nog-steeds-reden-om-direct-te-patchen) (the site banner URL [kwetsbaarheden-php-patches-beschikbaar-update-nu](https://www.ncsc.nl/alerts/kwetsbaarheden-php-patches-beschikbaar-update-nu) shows the same text and the same timestamp) | **PRIMARY-VERIFIED** (DEWEY read the page) |
| 22 Oct 17:52 (NOS; the page shows only "gisteren 17:52", and 22 Oct is inferred from the fetch time) | Spokesperson: *"We zien pogingen om de kwetsbaarheden te misbruiken en we krijgen de eerste signalen binnen dat dat met succes gebeurt"* ("we see attempts, and we are getting the first signals that this is succeeding"). The signals come via contacts with organisations "in binnen- en buitenland" (in the Netherlands and abroad). NOS reports, not as a quote, that the NCSC won't say what the signals are and that the investigation could take months | [NEWS: NOS](https://nos.nl/artikel/2636225-signalen-bij-nationaal-cyber-security-centrum-van-misbruik-php-lek) | SECONDARY-SOURCE (the date is INFERRED) |
| 22 Oct 21:13 (RD) | Links the NCSC alert above. Adds the precaution to keep unpatched systems offline | [NEWS: Reformatorisch Dagblad](https://www.rd.nl/a/ncsc-onderzoekt-eerste-signalen-van-misbruik-kwetsbaarheden-php-1) | SECONDARY-SOURCE |

- The NCSC's operational GitHub repository ([NCSC-NL/php2shell](https://github.com/NCSC-NL/php2shell); software list last updated 23 Oct 00:43 CEST) contains **no exploitation-status statement at all**. It is an inventory of affected products plus detection material. PRIMARY-VERIFIED.
- **Reading:** the "first signs" wording is the NCSC's own, dated 14:00Z 10/22. It replaced the "attempts only" line that ANP carried about two hours earlier. The signals come from partner organisations, not from the NCSC's own observation, and the NCSC has not described them. This is a lead with a primary source behind it. It is not a confirmed compromise.

**1b. Patchstack's reversal: both statements sit in one live timeline on its own article.**

| Time (UTC, 21 Oct) | Patchstack text (verbatim) | Basis |
|---|---|---|
| 07:34 | *"Multiple active exploitation incidents reported to Patchstack by hosting partners."* | PRIMARY-VERIFIED |
| 07:43 | Cloudflare's CTO reports early attacks and initial WAF rules (relayed) | PRIMARY-VERIFIED (that Patchstack relays it) |
| 13:52 | PHP releases fixed versions | PRIMARY-VERIFIED |
| **13:57** | ***"Shortly after PHP's update, our telemetry shows only probing attacks, with no hard evidence of breaches yet."*** *"This is expected to change as details of the security update go public."* | **PRIMARY-VERIFIED** |

Source: [PRIMARY: Patchstack, "Major security alert: PHP vulnerable to critical RCE, attacks ongoing", 21 Oct 2026](https://patchstack.com/articles/php-major-vulnerability-alert-10-2026/). The page lists the services that went offline as a precaution (DigiD, MijnOverheid, Sakura Rental Server and others) and names **no breached victim**. The 07:34 "incidents" are hosting-partner reports that the later telemetry line does not confirm, so the 07:34 entry is OWNER-ASSERTED (Patchstack relaying partners). *Loose end:* the fetched page carried a separate line, *"An attacker with valid UpdraftCentral dashboard keys is installing backdoors on connected WordPress sites"*. It needs a stolen-key precondition, so it reads as a different incident (probably another article's teaser). DEWEY did not confirm that, and it is **not** counted as a PHP2Shell victim.

**1c. Sweep for a named, confirmed successful compromise (from ~19:10Z 10/22 to ~23:35Z).** Result: **SEARCH-NOT-FOUND.** Four web searches plus primary and secondary reads turned up no victim statement, no incident-response case report, no national-CERT confirmation and no ransomware leak-site claim tied to PHP2Shell.

| Source checked | What it says about success | Basis |
|---|---|---|
| CERT-EU advisory 2026-018 (21 Oct 15:20; v1.1 the same day) | PoCs circulating "raises the likelihood that attackers are already exploiting"; no confirmation | PRIMARY-VERIFIED ([CERT-EU](https://cert.europa.eu/publications/security-advisories/2026-018/)) |
| watchTowr intelligence page (last updated 22 Oct) | *"watchTowr has observed exploitation of both CVE-2026-109618 and CVE-2026-109619 in the wild"* via its honeypot network. It **does not distinguish attempts from code execution** and names no victim | PRIMARY-VERIFIED ([watchTowr](https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/)) |
| Germany (BSI vice-president Thomas Caspers) | Attacks seen, no successful use: "It seems a little bit more complicated than expected to exploit" | SECONDARY-SOURCE ([NEWS: The Next Web, 22 Oct 13:03Z](https://thenextweb.com/news/php2shell-millions-exploit-attempts-no-confirmed-breaches)) |
| Japan (Chief Cabinet Secretary Minoru Kihara) | No attacks exploiting the flaws confirmed; ANA found no evidence of a breach; Mizuho, Shizuoka Bank and others went offline as a **precaution** | SECONDARY-SOURCE (same) |
| Cloudflare (CEO Matthew Prince, on X) | Attempts reached "millions now"; no compromise claimed | SECONDARY-SOURCE (same) |
| Amazon (CISO CJ Moses) | "PHP2Shell is now being broadly exploited in the wild"; no victim information | SECONDARY-SOURCE (same; the AWS MadPot blog is already PRIMARY in REQ-008) |
| PHP Foundation | No evidence of working exploits, only non-working ones | SECONDARY-SOURCE (search summary, not opened) |
| Wikipedia "PHP2Shell" (last edited 22 Oct 22:26Z) | Lists precautionary shutdowns (Wikimedia, 4chan, Internet Archive, Overheid.nl, French Interior Ministry and others); **no confirmed compromise; no ransomware** | tertiary, used as a recency check only |
| Techzine | Claims "ransomware groups and APTs are also reportedly using the vulnerability". No source, no victim | UNVERIFIED (not adopted) |

**Row 1 conclusion: NOT-FIRED, ATTEMPTS-ONLY.** Exploitation *activity* has been seen at scale (watchTowr, Amazon, Cloudflare, Hadrian). *Success* is claimed only as uncharacterised "signals" (NCSC) or as hosting-partner reports the reporter's own telemetry did not back (Patchstack). **Finding no victim is weak evidence here.** CrowdStrike's lab finding (carried in REQ-008) is that a compromise can leave just one memory-limit error in the log, and the MOVEit and SolarWinds victim lists surfaced weeks later.

### Leg 2 — Row 5: NYDFS alert
**Status: REACHED, verbatim, at the primary.** The earlier "NYDFS 403" was a block on the *client*, not the content. The site returns 403 to `curl`, even with a browser user-agent, but serves the page to WebFetch. Row 5's note that this may be "UNOBSERVABLE to automation" is therefore **not true for WebFetch**. `[[finding_negative_reachability_is_a_claim_about_your_request]]`

| Field | Content | Basis |
|---|---|---|
| Document | NYDFS **Industry Letter** (not a press release; the press index lists no PHP item for October) | PRIMARY-VERIFIED (DEWEY re-read the live page) |
| Date / to | 22 Oct 2026 / "DFS-Regulated Entities" | PRIMARY-VERIFIED |
| Title | "Cybersecurity Alert: Critical Vulnerabilities in PHP that Require Immediate Patching" (cites CVE-2026-109618 and -109619; never says "PHP2Shell") | PRIMARY-VERIFIED |
| Risk wording | The flaws "could enable unauthenticated remote code execution and unauthorized access to server files and databases" | PRIMARY-VERIFIED |
| Asks | Identify PHP use "including internet-facing applications" and "coordinate with third-party service providers to assess exposure and confirm whether the service providers have taken appropriate remediation measures". Patch immediately, internet-facing first. Systems that can't be patched "should take affected systems and applications offline until they are appropriately secured", and WAFs are "not … a substitute". Monitor logs for "unexpected PHP processes launching shells". It cites the DFS "2026 Heightened Cybersecurity Threat Environment Guidance" (21 May 2026) §§1.1, 1.5, 2.1–2.6 | PRIMARY-VERIFIED (quotes from the archived HTML; DEWEY confirmed the third-party and offline sentences on the live page) |
| Exploitation / compromise at regulated entities | **None stated, either way.** The phrase "known exploited vulnerabilities" appears only in the generic instruction, not as a claim about these CVEs | PRIMARY-VERIFIED |
| Deadline / reporting duty | None. No Part 500 / §500.17 notice language | PRIMARY-VERIFIED |
| Law-firm or FS-ISAC relays | None found (the letter is hours old) | SEARCH-NOT-FOUND |

- **Durable copy:** the DEWEY helper created a Wayback snapshot via Save Page Now (no prior snapshot existed): https://web.archive.org/web/20261022233439/https://www.dfs.ny.gov/industry_guidance/industry_letters/il20261022-cyber-php-patching
- **Related primary:** the CISA alert of 21 Oct 2026 says *"CISA has not observed exploitation of these vulnerabilities as of the time of publication"* ([CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching); quote via the fetch tool's summarizer, so near-verbatim). That vintage is now ~30h old and predates Amazon's "broadly exploited" statement.
- **Row 5 read:** the letter meets the sign as written: an NYDFS statement exists, so the state moves off ARMED. It is a patch-and-inventory letter with no compromise claim, though. Whether row 5 is meant to fire on routine guidance or only on a supervisory-concern statement is a question about the row's definition, and it is **CYPHER's call**. DEWEY flags it rather than resolving it. The third-party-coordination ask is the bank-relevant line: it puts vendor PHP exposure explicitly in scope for New York-regulated banks.

### Leg 3 — Rows 6 and 7: loss estimates, PCS, attribution

**Row 6 (loss estimate or PCS): no estimate found by these searches; PCS is MIRROR-WALLED.**
- Searches of CyberCube, Parametrix, Verisk/PCS, Moody's RMS, Guy Carpenter, Gallagher Re, Lloyd's, Swiss Re, Munich Re, AM Best, S&P and Fitch found no PHP2Shell or October-wave loss figure. **Gap:** most of these were covered by combined searches, not checked one by one on their own sites. Insurance Insider, The Insurer and Reinsurance News were not checked.
- PCS bulletins sit on subscription-only ISOnet. The public Artemis "PCS Global Cyber" page lists nothing after 2 Aug 2024. **MIRROR-WALLED.**
- **Do not mistake these for this event:** CyberCube's $400M–$1.5B and Guy Carpenter's $300M–$1B are **CrowdStrike (July 2024)** estimates. They kept surfacing as search hits.
- Context only, with no loss figure: Insurance Business UK (21 Oct) frames PHP2Shell as an aggregation-type event ([NEWS](https://www.insurancebusinessmag.com/uk/news/cyber/uk-councils-and-met-police-among-sites-pulled-offline-after-ncsc-alert-594424.aspx)). Crum & Forster published a note for insureds with no figure ([carrier page](https://www.cfins.com/php2shell-what-it-is-and-impact-for-insureds/); search summary only, not opened). Two exposure counts conflict and are **carried, not reconciled**: Veridion ~7.07M companies on an affected PHP version, and Silas Cutler (via Tenable) >1.3M internet-facing hosts (both UNVERIFIED, relayed by [Northdoor](https://www.northdoor.co.uk/insight/news/php2shell-php-vulnerabilities/)). Censys: ~1.57M hosts unpatched as of 21 Oct (relayed in search results; not opened).

**Row 7 (government attribution): NONE FOUND for PHP2Shell or the wave.**
- Government output so far is patching guidance only. The NSA, UK NCSC, CISA, FBI, BSI and CERT-EU all issued guidance (the NSA and UK NCSC wording was read via secondary pages; CERT-EU was PRIMARY-VERIFIED above). The CISA, NSA and BSI pages were not opened directly.
- Who is exploiting PHP2Shell: **nobody names an actor.** Amazon describes an anonymized-IP threat actor and "unclear how the actor acquired exploit information prior to disclosure" ([NEWS: The Register, 22 Oct](https://www.theregister.com/cyber-crime/2026/10/22/hackers-pile-on-php2shell-as-aws-reveals-attacks-began-before-disclosure/5304749)). SOCRadar reports exploit tooling on an exposed attacker server, operator unnamed, with a crypto/Web3 lean (UNVERIFIED, [malware.news](https://malware.news/t/php2shell-exploit-tooling-found-on-exposed-attacker-server/126651)).
- **Adjacent vendor attribution (NON-GOVERNMENT, not PHP2Shell):** *"Microsoft assesses that Storm-0940 was responsible for the recently disclosed ConnectWise supply chain compromise"*. The product is ConnectWise **Cloud Backup**; public reports surfaced 15 Oct and ConnectWise advised on 16 Oct. ARTEX agentic-AI tooling hit >2,250 tenants at 2,900 sign-in attempts a minute. A separate 10–14 Oct password spray hit 327 accounts at eight organizations with >151,000 failed logons and **no successful authentication observed**. **Financial services is among the named target sectors.** Microsoft names no victim and does not mention PHP. [PRIMARY: Microsoft Security blog, 21 Oct 2026](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) (PRIMARY-VERIFIED); [NEWS: CyberScoop](https://cyberscoop.com/microsoft-attributes-connectwise-supply-chain-attack-china-storm-0940/). Reported but not verified: ConnectWise's CEO agreed with Microsoft and China's embassy denied the attribution ([The Record](https://therecord.media/china-cyber-connectwise-ai), not opened).
- eMudhra key compromise: no actor. **CORRECTED 2026-10-22 ~21:45 ET:** this line first said "Cisco Talos traces it to a flawed key-generation ceremony on 30 Apr 2025", from a search summary. The follow-up run found **no Talos report**. The 30 Apr 2025 key-ceremony date was **first tied to the keys by Mozilla** (bug 2083449 c5, 18 Oct) and **confirmed by eMudhra** (c10–11, 19 Oct; refined 22:46 ET on CYPHER's flag), and the issue was reported by a community researcher on 17 Oct. It is a weak-key defect, not an intrusion. See `output/2026-10-22_emudhra-root-removal-financial-software.md`. LiteLLM PyPI poisoning (21 Oct): no actor; tokens suspected leaked through logs ([LiteLLM](https://docs.litellm.ai/blog/security-incident-oct-21-2026), search summary).

### Proposed watch-row reads (CYPHER adjudicates; DEWEY does not set states)

| Row | DEWEY's read for CYPHER | Basis |
|---|---|---|
| 1 | NOT-FIRED, ATTEMPTS-ONLY. Upgrade the lead's sourcing: the NCSC primary now exists (14:00Z 10/22), as do both Patchstack primaries | PRIMARY-VERIFIED (statements); SEARCH-NOT-FOUND (victims) |
| 5 | The letter of the sign is MET (NYDFS Industry Letter, 22 Oct). The substance is routine patch guidance with no compromise claim. FIRED-vs-NOT-FIRED depends on the row's definition: **CYPHER adjudicates.** Strike "possibly UNOBSERVABLE": WebFetch reaches dfs.ny.gov and curl is the blocked client | PRIMARY-VERIFIED |
| 6 | NOT-FIRED. PCS leg MIRROR-WALLED | SEARCH-NOT-FOUND |
| 7 | NOT-FIRED. Note the Microsoft Storm-0940 / ConnectWise vendor attribution as an adjacent, non-government item; if a government endorses it, SHADE's state-attack exclusion question opens for *that* incident, not PHP2Shell | PRIMARY-VERIFIED (Microsoft text); SEARCH-NOT-FOUND (government) |

**Did anything fire a row?** There is no named confirmed victim and no US bank or core-vendor victim, so rows 1 and 3 have not fired. **Row 5's sign is met as written** (the NYDFS letter), so under CYPHER's instruction DEWEY also sent REGINALD (row 5's consequence owner) a stub and PROME a packet. Both say plainly that the fire is a definitional call for CYPHER and that the letter's content is routine.

## Counter-Evidence
- **Against "attempts only":** the NCSC is a national CERT, and it put "first signs of successful misuse" on its own alert. Amazon's CISO says "broadly exploited in the wild", and watchTowr says "observed exploitation". If any of those means code execution on a real server, row 1 is already true and just unnamed. The low-footprint finding (one memory-limit error in the log) makes silence weak evidence.
- **Against "first signs" meaning much:** the BSI and Japan both said no success. The PHP Foundation said the public exploits don't work. Patchstack's own telemetry walked back its partner reports within 6.5 hours. The NCSC's signals are second-hand (from partner organisations) and uncharacterised. The NCSC also said "attempts only" two hours before it said "first signs".
- **On loss and attribution:** an absence 36 hours in is normal. MOVEit's PCS designation and NotPetya's attribution (~8 months) both came late (REQ-008 §2). "None found" here is about timing, not severity.

## Source Quality Assessment
- Strong: the NCSC alert, both Patchstack timeline entries, CERT-EU, watchTowr's page, and Microsoft's blog were all read at the primary.
- Medium: the government "no success" statements from Germany and Japan come via one news outlet (The Next Web), and the NCSC's NOS quote via NOS.
- Weak: ransomware/APT claims (Techzine, unsourced), the exposure counts (relayed), and any loss context.
- The NOS absolute date is inferred from its relative "gisteren" stamp.

## References
(accessed 2026-10-22, 19:31–19:37 ET)
- NCSC alert: https://www.ncsc.nl/alerts/update-php-kwetsbaarheden-nog-steeds-reden-om-direct-te-patchen
- NCSC alert (banner URL): https://www.ncsc.nl/alerts/kwetsbaarheden-php-patches-beschikbaar-update-nu
- NCSC-NL GitHub: https://github.com/NCSC-NL/php2shell
- NOS: https://nos.nl/artikel/2636225-signalen-bij-nationaal-cyber-security-centrum-van-misbruik-php-lek
- ANP via Welingelichte Kringen: https://www.welingelichtekringen.nl/samenleving/ncsc-nog-geen-sprake-van-succesvol-misbruik-php-kwetsbaarheden
- iBestuur: https://ibestuur.nl/digitale-weerbaarheid/digitale-veiligheid/ncsc-ziet-nog-geen-misbruik-van-php-lekken
- RD: https://www.rd.nl/a/ncsc-onderzoekt-eerste-signalen-van-misbruik-kwetsbaarheden-php-1
- Patchstack: https://patchstack.com/articles/php-major-vulnerability-alert-10-2026/
- CERT-EU 2026-018: https://cert.europa.eu/publications/security-advisories/2026-018/
- watchTowr: https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/
- The Next Web: https://thenextweb.com/news/php2shell-millions-exploit-attempts-no-confirmed-breaches
- SecurityWeek: https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/
- The Register: https://www.theregister.com/cyber-crime/2026/10/22/hackers-pile-on-php2shell-as-aws-reveals-attacks-began-before-disclosure/5304749
- Wikipedia PHP2Shell: https://en.wikipedia.org/wiki/PHP2Shell
- Microsoft Storm-0940: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
- CyberScoop: https://cyberscoop.com/microsoft-attributes-connectwise-supply-chain-attack-china-storm-0940/
- Insurance Business UK: https://www.insurancebusinessmag.com/uk/news/cyber/uk-councils-and-met-police-among-sites-pulled-offline-after-ncsc-alert-594424.aspx
- NYDFS Industry Letter (live): https://www.dfs.ny.gov/industry_guidance/industry_letters/il20261022-cyber-php-patching
- NYDFS Industry Letter (Wayback 2026-10-22 23:34:39Z): https://web.archive.org/web/20261022233439/https://www.dfs.ny.gov/industry_guidance/industry_letters/il20261022-cyber-php-patching
- NYDFS industry letters index: https://www.dfs.ny.gov/industry_guidance/industry_letters
- CISA alert, 21 Oct 2026: https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching

## Process Report
**Searches run:** Leg 1 (DEWEY main session): 7 web searches and 13 page fetches. Leg 2: one helper, one time-boxed pass. Leg 3: one helper, 22 tool calls. DEWEY then re-read the Microsoft and CyberScoop pages at the primary. Both helpers ran under DATA-RETURN scope, wrote nothing to the repo, and spawned no children.
**Data gaps:** the NCSC's "signals" are uncharacterised (it won't say). There are no incident-response case reports yet. The CISA, NSA and BSI pages were not opened directly. Modelers were not checked site by site. PCS is subscription-only. No law-firm or FS-ISAC relay of the NYDFS letter exists yet, and DEWEY did not find where press coverage's "NYDFS alert" claim first appeared. Leg 2 made one outbound write: a Wayback "Save Page Now" request to archive.org, which created the snapshot cited above. No institution's systems were touched.
**Source frustrations:** the ncsc.nl news index renders client-side ("Resultaten laden..."), so the alert was reached through a newspaper link. NOS shows only relative dates. Huntress's statement (relayed in one search summary) could not be found at a primary.
**Confidence in findings:** High that the quoted statements say what they say and when. Low on the underlying world state, by design.
**If I had more time/tools:** subscribe a checker to the NCSC alert's "Bijgewerkt" stamp, since its next update is the most likely place a confirmation appears. Look for a ransomware leak-site tracker with a public feed.
**Suggestions:** CYPHER's row 1 could cite the NCSC alert URL as the watch primary for the Dutch lead (an EVENT row read by the owner). The "Bijgewerkt" footer is a cheap timestamp to compare.
