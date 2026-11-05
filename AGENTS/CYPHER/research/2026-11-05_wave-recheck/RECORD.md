# CYPHER — WAVE-2026-10 re-check, DOCKET L812 second pass, plus +14d, cluster watch and claim pass — 2026-11-05

**Session:** 2026-11-05, WQ-618 A. Runtime Claude Code, Opus 5.5. Reads by CYPHER (curl, WebSearch), two WebFetch helpers for routes curl cannot reach (NYDFS, American Banker, GMO, Binance listing). No subagent verdicts: every call below is CYPHER's.

## Verdicts

| Row | State 11/05 | Instrument read | Reading |
|---|---|---|---|
| 1 | **NOT-FIRED** (evidence moved again, see §1) | NCSC alert; Palo Alto advisory and Unit 42 brief; Dream post; Kiteworks advisory; CSA Singapore AL-2026-157; CERT-FR alerts | Compromise now vendor-verified, no organisation named |
| 2 | FIRED (terminal) | KEV v2026.11.04 via boot leg 7 | Both CVEs listed |
| 3 | NOT-FIRED | Searches at victim/vendor level; boot legs 8, 9, 10 | No named US bank, CU or core/digital vendor tied to PHP2Shell. Abrigo and Finzly are named vendors but carry **no wave link** (§3) |
| 4 | NOT-FIRED | boot leg 8 live 13:57 ET: no Item 1.05 8-K since 10/29; control 17 in 120d | Leg 9 Revolve already CYB-INC-058 |
| 5 | NOT-FIRED | NYDFS list via WebFetch: latest cyber letter still 10/22; 11/04 letter is wage-exemption. No Fed, OCC, FDIC, NCUA, FFIEC, FS-ISAC or ECB statement found | NSA, FBI and CISA urged fixes (already known), no concern at regulated entities |
| 6 | NOT-FIRED | Trade press to 11/02; PCS MIRROR-WALLED | CyberCube long-tail, not a catastrophe; Marsh Re: closer to routine patching. No figure |
| 7 | NOT-FIRED | Searches; CISA, NCSC, CSA pages | Attribution still private. Dream's "Chinese-nexus" is a suspicion; a search snippet of the coverage says affiliation is "not clearly evident" from the attacker's logs. CISA declined comment to The Record |
| 8 | NOT-FIRED | Bank and operator statements | Arkéa off-wave, under one business day. Abrigo is a vendor, not a bank or payment system, and off-wave |
| 9 | NOT-FIRED | HENRY and VULCAN own this; no fire read from either in STATUS | Test 11/18. Magnitude decision due Friday 11/06 to PROME by 11/10 |

All non-terminal rows re-stamped 2026-11-05. Next 7-day clock: 11/12. R1 flip test 11/20 unchanged, re-checks inside 11/13..11/20.

## §1. Row 1: why it moved, and why it holds

**The 10/29 read called this "one research firm's VENDOR CLAIM". That is out of date.** Palo Alto's Unit 42 brief, updated 10/29 11:00 PT (14:00 ET, after the L812 reads):

> "Unit 42 has independently verified the same attacker's tooling and confirmed the reported results."
> "Only a small fraction of a percent (approximately .02%) of our global installed base has internet-facing management interfaces configured and were impacted. Each of these customers has been individually contacted by our teams."

So the compromise is confirmed by the vendor of the affected product, and the population is known to that vendor. Palo Alto's spokesperson wording to Cybersecurity Dive is softer ("exposed to the internet and potentially impacted"). The denominator is not published, so .02% is not a count. Dream has made no correction; it has added detail (first government firewall rooted 10/23, second 10/24, ~19,000 fingerprinted targets, "persistent tunnel ... likely still running"). The Record: GreyNoise reports at least six successful exploitations (sensor-level). Singapore's CSA alert carries the chain as reported.

CYB-INC-047 moves REPORTED → CONFIRMED (compromise), PRIMARY-VERIFIED at Palo Alto; the "US government-affiliated" label remains Dream's inference; victims unnamed.

**Why NOT-FIRED holds.** The R1 flip reads "a named organisation's successful PHP2Shell compromise confirmed by the victim, an incident-response report, a national CERT, or a leak-site claim", and the row's healthy reading is "no successful compromise named". No organisation is named.

**⚠️ Letter risk, stated plainly:** row 1's Sign reads "Confirmed successful PHP2Shell compromise (named victim, incident-response case, ransomware claim)". A vendor's verification of unnamed customers could be read as an "incident-response case" on the row's own words. CYPHER reads the row with the R1 sentence, as on 10/29, so naming stays required. If PROME reads the parenthetical as three alternatives, row 1 is FIRED and the toward-MOVEit test is NOT, because R1 itself says named. That reading is PROME's to overrule; no letter was changed here.

**DEWEY's 008R "back toward Log4Shell on Dream withdrawing" path is closed for now:** Palo Alto has verified the claim. Direction: one further step toward MOVEit on evidence, flip not met.

Kiteworks: advisory `info.kiteworks.com/php2-vulnerability-advisory`, "Last updated: 2026-10-27 8:00 PDT", read 14:1x ET: no exploitation statement. Friday row stands.

## §2. VX re-grades

| Vector | Was | Now | Reason |
|---|---|---|---|
| VX-CYP-01 | 2 | **3 YELLOW (correction)** | Cell: "A KEV-listed flaw in a product US banks are known to run; still no named victim". True since 10/26 KEV plus a US credit union's own PHP site (CYB-INC-046) and CHK-32 perimeter appliances. The 10/26 and 10/29 passes left it at 2: a miss on the letter, not new evidence |
| VX-CYP-02 | 3 | 3 | WQ-589 re-cut encoded. Arkéa YELLOW under either letter |
| VX-CYP-08 | 3 | **4 ORANGE** | Cell: "A US / UK / EU government attribution of a financial-sector-relevant campaign". FBI, 10/31, North Korea TraderTraitor, Binance. Basis SECONDARY (fbi.gov 403). Composition note: a crypto venue, no dollar-plumbing consequence (WQ-550). North Korea denied it (Kim Yo Jong, The Record 11/03, Monday = 11/02 inferred). Graded under catalyst row, PROME issued no contrary ruling |
| Others | | held | Linked rows NOT-FIRED |

Composite: **24/40 raw** (3+3+3+3+3+4+4+1). Shared-root-adjusted **15/40**: PHP2Shell cluster VX-01/02/03/06 counted once at max 4 (24 − 3 − 3 − 3). VX-01 joins the cluster because its 3 now rests on that root. Raw rises 2, adjusted falls 1, and both moves are bookkeeping plus one attribution, not new bank damage.

## §3. Bank-vendor cluster watch (catalyst, Will 10/29): **THRESHOLD MET**

Letter: "2 or more NEW confirmed incidents or outages at distinct bank-core, CU-vendor or payment-messaging suppliers inside any 30-day window". Not an escalation-row fire.

| Supplier | Class | Confirmed by | What is confirmed | What is not |
|---|---|---|---|---|
| **Finzly** (CHK-33) | Payment middleware to ACH, Fedwire, RTP, FedNow, SWIFT | Company statement, American Banker 10/30 12:12 ET (Carter Pape; read via WebFetch) | "an unauthorized third party accessed a single device in our backup data center containing configuration information"; keys and credentials rotated; n0n published passwords, keys and a map for the firewall guarding the clients' Fed link; five of six files look like a FortiGate configuration | Whether that device was the firewall; whether credentials still worked ("American Banker did not test"); dates. Fed: services "were not impacted". Finzly: possession alone gives no access; no evidence customer data was compromised. Site listed 11 bank and CU clients |
| **Abrigo** (new CHK-41) | Lending, risk and AML software to community banks and CUs | Company spokesperson, American Banker 11/02 evening; own status page (RSS read) | "data security incident" with unauthorized access; Sageworks disabled ~11:25 ET Fri 10/30; platform back 07:11 EST Mon 11/02 except borrower-facing features; status "Resolved" 11/03 14:23 EST with that exception | Whether data was taken (documents held include tax returns, financial statements, credit reports). Cause. Whether borrower features are back. >2,400 institutions is ALL Abrigo products, not Sageworks; 1,200+ was the 2018 Sageworks figure |

**Call:** count limb MET at 2 of 2. Both are company-confirmed, both new since 10/29, distinct suppliers, inside 30 days. ⚠️ Abrigo fits "CU-vendor" on plain words (it sells to credit unions); it is not a core. If PROME reads the class narrowly, the count is 1 and this is not a fire.

Outage limb ("disrupts processing at 2 or more institutions for 1 business day or more"): **not relied on.** Main platform ~69 clock hours but about 5.6 business hours (Fri 11:25-17:00, back before Monday opening); borrower-facing features longer; no institution has stated a processing disruption.

Neither is PHP2Shell-linked on any evidence. Abrigo's status feed shows an unexplained "security update" on Construct on 10/21; not a link and not to be read as one. If Abrigo's root cause proves PHP2Shell, row 3 fires.

**A miss worth recording:** boot leg 10 printed "no bank-vendor incident headline since 2026-10-29" with both stories live. American Banker's Finzly headline says "bank vendor", not "Finzly" (body match, unlisted by design); Abrigo was not on the supplier list. The fix is one list entry (Abrigo, Sageworks). The body-only blind spot stays a known limit: leg 10 quiet does not mean no incident. No new check proposed (Will 10/31).

Arkéa does not count: unnamed provider, type unknown, non-US.

## §4. Claim pass (catalyst row, due today; partial)

| Row | Result |
|---|---|
| 037 Finzly | **Moved to CONFIRMED** (§3) |
| 036 Commonwealth Community Bank | Trackers only; no bank notice found. Stays REPORTED |
| 039 Delta Electric | No coverage found. Stays REPORTED |
| 043 Park24 | Times Car notices via secondary: 1,464,800 ID images with traces of external transmission; ~6.6M accounts in scope; class action in preparation. JPY 5.5B loss still not read in the issuer document. Stays REPORTED |
| 044 Keystone | Erasure completion (expected 11/03) not established; blog 404; latest coverage late October |
| 038, 040, 042, 045 | **NOT RE-READ this session** (bounded scope). Re-dated 11/12 |

## §5. Friday 11/06 rows, date check

| Row | Date source | Verdict |
|---|---|---|
| Kiteworks victim check | Desk rule, disclosure +~14d; R1 note says 11/06 | ✅ Friday. Desk-chosen, not an external deadline |
| Capcom re-check | Desk ("Re-check by 2026-11-06") | ✅ Friday |
| GMO compensation procedure | GMO status block: "申請方法などは、2026年11月6日（金）までにご案内します（第4報）" | ✅ Issuer's own "(金)" agrees. No timezone stated; if JST, end of day = 09:59 ET Friday. **Read Friday after 10:00 ET.** |
| GMO replacement service | Promised 10/30 23:59 JST | **Consumed today:** emails began 10/30 15:30, applications for goodwill payment and replacement service opened 11/04, servers remain stopped with no restart date (status as of 11/05 21:00 JST). Row retired, read folds into CYB-INC-032 |
| Row 9 magnitude | PROME packet 10/29 "by 11/10" | ✅ 11/06 Friday is the desk's date; 11/10 is a Tuesday. Decision NOT taken here (no threshold change in this session) |
| PROME DOCKET | No CYPHER row dated 11/06 | ✅ none. Weekday claim check clean on DOCKET, GATES, STATUS |

## §6. Intake

ConnectWise (cards 013, 011): advisory 11/04 18:55 UTC read at primary. Phases 1 and 2 complete; phase 3 partial (billing open); phase 4 partial; SaaS Security and Cloud Automation restored, partners must reconnect; platform backup dashboard not fully restored. Not "restored". Vendor cannot determine individual tenant compromise from unavailable tenant-side logs (WALTER's read, card 011). No financial institution named.

European refrigeration (card 020): BleepingComputer 11/02 read via WebFetch: >115 stores, six countries there, eight in the card's later Reuters count. Installer Sabcobel's director: "the attacker leveraged the same vulnerability used in similar attacks last month in France" — one vendor director's claim, and same vulnerability is not same attacker. CERT-FR has a standing alert on Danfoss AK-SM/AK-SC and Copeland/Dixell xweb controllers. Whether those controllers are the ones in Belgium is not stated. Per-chain counts are WALTER's and BleepingComputer's, not a census; no food-loss figure. Each victim, date and patch was NOT separately verified at chain level beyond these reads. New lead, not carded: French blood-bank (EFS) freezer attack (search title, unread).

Binance (card 061): post-mortem released Tue 11/03 (The Record, SECONDARY; Binance's own post not found in its listing): began June with malicious software downloaded to install "a popular AI coding tool", plus fake recruitment interviews and compromised internal AI tooling. **No vendor, supplier or bank named,** so no chokepoint match. Recovery Update #8, 11/05, more withdrawals reopening. "$3.6bn withdrawn" and "North Korea prime suspect" titles are duplicates of what the desk holds. "Fake nuclear warning from hacked app" (Ukraine): title only, no money channel, logged.

Mercado Bitcoin (Brazil, 11/02, $40-46M, Tether froze >$4.5M; press): below the WQ-589 bar on loss. Top-10 by volume not established, none of the sources says so. Log only.

Card 037 phishing (CU Today): article 403 to both routes, "248 domains" unverified, search found no match. No loss, no bank named. Logged.

Late cards (doorbell 14:1x ET): **046** Fed and OCC supervisors called banks Monday 11/02 after Binance (Reuters 11/05, anonymous; read through Crypto Briefing, Investing.com 403). Outreach, not a finding; declined comment; no guidance; no bank named. Into CYB-INC-055. Not row 5, which is PHP2Shell-wave. **050** French blood-bank cooling attack and a US refrigeration warning: noted on CYB-INC-061; agency of the warning unread.
