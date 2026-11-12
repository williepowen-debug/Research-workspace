# ESCALATION_WATCH notes archive — rotated 2026-11-12 (read-cap rotation; resume item 2 of 11/06)

Dated Notes segments from 10/23-10/29 (and their undated continuations), moved verbatim from `workbook/ESCALATION_WATCH.tsv` (WAVE-2026-10), as the TSV reader parses the cell (CSV quoting removed; the cells in rows 1, 2, 3, 5, 7, 8 were CSV-quoted). Segments are joined with ' | '. Each row's first (foundational) segment stays in the ledger. crc32 = UTF-8 of the moved text.

## row 1

crc32 5202885a · 3347 B

2026-10-23 re-check: NOT-FIRED. NCSC page unchanged since 22 okt 16:01 (same sentence, no victim). Sweep found no named successful compromise at any source; Patchstack hosting-partner 'incidents' remain unnamed and secondary. Relay-overstatement direction (KB-CYP-019): a news outlet reporting an agency is a lead, never the FIRED evidence. | 2026-10-23 17:1x ET: Google (Hultquist via The Record, secondary) "not validated" in the wild, "may have already begun in a limited fashion" — no named victim, so NOT-FIRED stands; KEV v2026.10.23 still lacks both CVEs (row 2). New off-root disclosures GitLab CVE-2026-110264 and Node.js CVE-2026-111497 are not PHP2Shell and do not touch this row. | 2026-10-26 targeted candidate adjudication: Unit42 government-victim CVE attribution retracted 10/25; Sophos successful-customer claim corrected 10/22 21:21Z; 0x4D31 new evidence concerns intentionally favorable research honeypots, not a named production organisation. None supplies the registered named-victim/R1 evidence. NOT-FIRED retained; no claim of global absence. CISA row 2 remains FIRED. | 2026-10-29 L812 re-check (CYPHER + read-only checker; research/2026-10-29_wave-recheck/RECORD.md#row-1): NOT-FIRED under the registered letter (R1: a NAMED organisation). EVIDENCE MOVED: Dream (Israeli security firm) own blog 10/26, read by CYPHER 10/29: PHP2Shell chain (CVE-2026-109618/-109619) + Fragnesia kernel LPE (CVE-2026-46300, KEV-listed 10/28) rooted 24-25 firewalls of an undisclosed 'large vendor' in US/JP/TW/KR; on three servers in a 'US government-affiliated environment' post-exploitation (reverse SSH tunnel, LDAP enumeration, password spraying; 'artifacts confirm credential extraction'); found by 'proactive threat hunting' with its own product (VENDOR CLAIM, not an IR engagement); victim UNNAMED; no attribution ('Chinese-nexus' indicators). Palo Alto CVE-2026-109618 advisory (updated 10/29, PRIMARY, CYPHER read): 'Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet', Exploit Maturity ATTACKED, severity raised to Critical 10/27; no victim or count. THN suggests (does not confirm) Dream's vendor = PANW. ATTEMPTS-ONLY no longer describes the wave: an UNNAMED successful compromise is reported by one research firm. Prior two firm claims this wave were withdrawn or corrected (Unit 42 10/25, Sophos 10/22): re-check Dream for correction 11/04. NCSC alert unchanged since 10/23 15:43. CYB-INC-047. | CORRECTED 2026-10-29 12:50 ET: Fragnesia CVE-2026-46300 KEV dateAdded is 2026-10-28 (CISA KEV v2026.10.28, CYPHER curl re-read; WALTER SIG-W-20261029-036 caught it), not 10/27 as first written. Government affiliation is Dream's inference from configuration (CAC authentication, naming conventions, certificate data it says links to the target organisation), not a victim or government statement (DEWEY 008R framing agreed). | 2026-10-29 DEWEY 008R (SIG-W-20261029-036, AGENTS/DEWEY/output/2026-10-29_cyber-wave-rerun-008R.md, checks 16:43-16:50Z): independently agrees NOT met; adds The Register 10/27 (secondary) on researcher-clocked successful exploits and Palo Alto severity Critical from 10/27 16:40Z. Moves to MOVEit on a named PHP2Shell victim, a PHP2Shell leak-site victim list, an Item 1.05 8-K citing PHP or a PCS designation; back on Dream withdrawing.

## row 2

crc32 c81cefcf · 756 B

2026-10-23 16:2x ET: KEV v2026.10.23 (released 19:30Z, 1,756 entries) read live — CVE-2026-109618/-109619 still ABSENT; same release listed Arista CVE-2026-114625 (CYB-INC-014, off-root). | 2026-10-26 OWNER ADJUDICATION: both root CVEs dateAdded 2026-10-26; row 2 FIRED on the registered catalog-membership test. This confirms exploitation, not a named victim, bank exposure, loss or state attribution. Rows 1/3 and the R1 flip are separate. P1 handoff this session: REGINALD, GIBBS, SHADE, VULCAN, WALTER and PROME inbox/2026-10-26_from-CYPHER_P1-PHP2Shell-KEV-fired.md. Recipient consumption unverified. | 2026-10-29: terminal FIRED. KEV v2026.10.28 still lists both; federal due date 2026-10-29, forensicTriage Yes; knownRansomwareCampaignUse Unknown.

## row 3

crc32 e7800221 · 894 B

2026-10-23 re-check: no named US bank, CU or core/digital-banking vendor victim — ConnectWise advisory (10/23 14:00Z) and Microsoft blog (10/21) name no bank; Kiteworks advisory (10/22) carries no exploitation statement; boot legs 8/9 show no bank cyber 8-K (leg 9 bank hits FB Financial, Hanmi = boilerplate). Live paths to watch: Kiteworks (catalyst 11/06), ConnectWise MSP (CYP-03). | 2026-10-29 L812 re-check (research/2026-10-29_wave-recheck/RECORD.md#row-3): no named US bank, CU or core/digital vendor victim tied to a wave vector. A US credit union took PHP-running in-house website and digital banking offline as a precaution (CYB-INC-046): no compromise stated ('no impact to member information at this time'), so not a victim. Finzly (037) still a claim; company says investigating and 'fully operational' (American Banker 10/20, SECONDARY). ConnectWise 10/28 advisory names no FI.

## row 4

crc32 61aca2f7 · 852 B

2026-10-26 manual adjudication: boot leg 8 AASP hit is EX-99.2 AUDIT COMMITTEE CHARTER, not a 1.05 filing. EFTS items 5.02/5.05/8.01/9.01, submissions metadata and filing body agree. No qualifying recent 1.05 filing among returned hits. Leg 9 Quest already ledgered; ODFL already read as boilerplate 10/23. No new bank/vendor material-incident evidence. See AGENTS/CYPHER/research/2026-10-26_startup/RECORD.md#edgar. | 2026-10-29 boot.py leg 8 live 11:34 ET: only Item 1.05 since 10/22 is AASP 10/26 (audit-charter text, already rejected 10/26); control 19 in 2026-07-01..10-29. Leg 9 hits: Hanmi 10/29 = dividend release boilerplate (KB-CYP-065); DGX, ODFL already read. | 2026-10-29 DEWEY 008R independent EDGAR read agrees: 19 Item 1.05 8-Ks since 7/1; only AASP since 10/15, filed under 5.02/5.05/8.01; zero cite PHP2Shell, Node2Shell or Fragnesia.

## row 5

crc32 afb18534 · 536 B

2026-10-23 re-check: web search for an FFIEC / OCC / FDIC / NCUA PHP2Shell statement found none; NSA advisory 10/21 (patch-or-take-offline advice, SECONDARY via Insurance Business, nsa.gov 403) is a security agency, not a bank supervisor. | 2026-10-29 L812 re-check (research/2026-10-29_wave-recheck/RECORD.md#row-5): NYDFS latest industry letter still the 10/22 PHP alert (ruled NOT-FIRED); nothing from Fed, OCC, FDIC, FFIEC, NCUA, FS-ISAC or ECB meeting the supervisory-concern test. NSA 10/21 advisory is patch guidance (secondary).

## row 6

crc32 5ffcafe5 · 454 B

2026-10-23 re-check: no PCS designation (MIRROR-WALLED) and no CyberCube / Parametrix / modeler estimate for PHP2Shell found (search 10/23); Insurance Business 10/21 discusses exposure, gives no figure. | 2026-10-29 L812 re-check (research/2026-10-29_wave-recheck/RECORD.md#row-6): no PCS designation visible (MIRROR-WALLED) and no modeler loss estimate. CyberCube 10/23: 'Why PHP2Shell isn't a large-loss event today' (SECONDARY via search; title only).

## row 7

crc32 b79a03b6 · 547 B

2026-10-23 re-check: no CISA / FBI / government attribution of the ConnectWise campaign found (search 10/23); attribution is Microsoft's (vendor) and ConnectWise's 'China state-aligned group'. | 2026-10-29 L812 re-check (research/2026-10-29_wave-recheck/RECORD.md#row-7): no US/UK/EU government attribution. Private only: Dream (no named actor, China-nexus indicators), CYFIRMA (North Korea, moderate, via SBS), Microsoft/ConnectWise (Storm-0940). CISA AA26-293A that a search tied to ConnectWise is a SafePay ransomware advisory, not attribution.

## row 8

crc32 b77a3c77 · 1812 B

2026-10-23 re-check: Fed service-status page 'no notifications' (CHK-21, helper read 10/23); European PHP2Shell takedowns were government and web sites, no bank or payment operator (CYB-INC-025). | 2026-10-29 L812 re-check (research/2026-10-29_wave-recheck/RECORD.md#row-8): ADJUDICATED NOT-FIRED on a candidate. A US credit union ($8.9B; named in CYB-INC-046) took its website and digital banking offline Wed 10/21 after the federal PHP warnings; restored Thu 10/22 after patching (~24h); statement view, web check deposit, assistant still returning Fri 10/23; branches, call centre, ATMs and cards stayed up; chief of staff: systems 'developed by and maintained by [the credit union], not a vendor' (bracket = CYPHER's redaction of the name), 'no impact to member information at this time' (American Banker 10/23 12:18 EDT, operator quoted; CYPHER read 10/29; credit union's own website notice NOT FOUND -> SECONDARY). Rule applied = the pre-registered VX-CYP-02 bands (10/22): 'Precautionary pauses only, or an outage under one business day at a single institution' = YELLOW; FIRE-level ORANGE needs an operator-confirmed outage of one business day or more. A self-taken, ~24h, digital-only pause with payments up sits in YELLOW. This is the band as written, not a re-cut. The 10/23 re-check missed this item (published the same day). Would fire on: a second institution, a payment-channel stop, or an unplanned outage >= 1 business day. CYB-INC-046. | 2026-10-29 news sweep: Central Bank of India RTGS disruption and INR 13.97 crore unauthorized transfers 10/15-17 (CYB-INC-049) is a bank payment disruption outside Japan but OFF-WAVE (vector unstated, no PHP link) and predates disclosure; does not fire this wave row. Sharetec 9/15 (CYB-INC-050) is the accidental precedent for the multi-institution shape.

## row 9

crc32 e39a672e · 1206 B

2026-10-29: HENRY confirmed the boundary 10/29 and graded DGX (no adverse reaction); no HENRY or VULCAN wave-equity read consumed. NOT-FIRED on the 20-trading-day rule until 2026-11-18. Palo Alto (a possible vector vendor: active exploitation of its management interface, severity Critical 10/27) flagged to HENRY and VULCAN P2 for the vector-vendor leg. | 2026-10-29 DEWEY 008R (intraday ~12:47 ET, since the 10/20 close; DEWEY event_window.py, OWNER-ASSERTED, HENRY/VULCAN grade): HACK +8.3% (peak 10/27), PANW +10.8%, KRE +3.3%, XLF +2.2%, FIS +1.5%, JKHY +3.5%, FISV -0.2%. Fortinet -20.9% is its Q3 earnings reaction (8-K item 2.02, 10/28), NOT a wave-vector collapse: do not relay as one. Still NOT-FIRED; 20-day test 11/18. | 2026-10-29 VULCAN reply (inbox/processed/2026-10-29_from-VULCAN_panw-vector-vendor.md, VULCAN KB-330): PANW IS a row-9 vector vendor on its own advisory. VULCAN declines the price-collapse leg by its charter (AI capex and semis only) and flagged scope to PROME. Price grade therefore sits with HENRY, which accepted row 9 on 10/29 (KB-CYP-063). CYPHER charter consequence table still lists cyber-vendor stocks under VULCAN: a boundary conflict for PROME, not resolved here.
