# TruStage cyberattack (identified 11 Jul 2026): what was taken, ransomware, credit unions affected, cost
**Date:** 2026-10-22 (research 20:34–20:38 ET; committed 20:38:09 ET (2b1b71a14). Stamp corrected 20:39 ET, as the original "20:55" was typed, not clocked) | **Mode:** Thesis | **Confidence:** High on what TruStage, Mandiant, AM Best and the court record say; the four questions themselves remain mostly **UNKNOWN by the company's own account**
**Commission:** Will-directed in the DEWEY session, 2026-10-22 20:34 ET. Will handed DEWEY WALTER's 043 sweep recommending "a short DEWEY pull" on TruStage. WALTER confirmed no REQ and no slot used. The four open questions are WALTER's (SIG-W-20261022-043): what was taken, whether ransomware was involved, how many credit unions are affected, and what it has cost.

## Key Finding
**Three of the four questions are still unanswered at the primary, and the company says so itself.** TruStage, the credit-union insurance and retirement vendor formerly called CUNA Mutual, has **not determined whether member data was accessed**. It has **named no attacker and confirmed no ransom demand**, and it has **given no count** of affected credit unions or people. On 12 Aug its CEO set a 2–3-month window for the data answer, so the open window is ~12 Oct to ~12 Nov. At day 100 (20 Oct) there was still no data update. On cost, no figure is disclosed. AM Best (7 Aug) left the ratings unchanged and said the disruption "has not had a material impact on the credit profile of the enterprise". **The answer that matters for banks:** Mandiant's 10 Aug memo says it has "not observed the threat actor interacting with any files shared with third parties, or with any third-party systems … connected to TruStage". So far this is a **service outage at a vendor, not a spread into credit unions' own systems.** It is the >100-day outage at a US financial vendor that the base rates were looking for. Every service class on TruStage's status page (claims, policy servicing, disbursements) still reads "Partially available" as of 20 Oct.

## Evidence

### 1. Timeline and current state

| Date | Event | Source | Basis (Class 12) |
|---|---|---|---|
| 11 Jul 2026 | "cybersecurity attack identified on July 11"; "a particularly broad attack on our network and systems" | [PRIMARY: TruStage outage page](https://www.trustage.com/outage) | PRIMARY-VERIFIED (**this confirms 043's search-derived 7/11 date**) |
| 15 Jul | First public statement: "recently identified a cybersecurity incident affecting its environment"; incident response activated, outside experts engaged | [PRIMARY: TruStage newsroom](https://www.trustage.com/newsroom/2026-press-releases/cybersecurity-incident-update) | PRIMARY-VERIFIED |
| 17 Jul | First suit: *Bessemer System FCU v. TruStage Financial Group*, No. 3:26-cv-00644, W.D. Wis. (proposed class of all US credit unions that shared data with TruStage and were hit by the outage; negligence) | [NEWS: American Banker, 21 Jul](https://www.americanbanker.com/news/credit-union-sues-trustage-over-cybersecurity-incident); [NEWS: Credit Union Daily, 13 Aug](https://thecudaily.com/more-than-a-dozen-lawsuits-have-now-been-filed-over-trustage-cybersecurity-incident/) (docket numbers) | SECONDARY-SOURCE |
| 31 Jul | "The incident has been contained"; infrastructure rebuilt; "While we do not yet know whether member data was accessed"; partners notified first if PII is involved | [PRIMARY: TruStage newsroom](https://www.trustage.com/newsroom/2026-press-releases/recovery-restoration-progress-cybersecurity-attack) | PRIMARY-VERIFIED |
| 7 Aug | AM Best: ratings of TruStage Financial Group and Union Security Insurance Co. "remain unchanged"; "not had a material impact on the credit profile". It will monitor whether the incident "has damaged the company's ability to conduct business, eroded its reputation" or changes its view of enterprise risk management | [PRIMARY: AM Best](https://news.ambest.com/newscontent.aspx?refnum=276260&altsrc=23) | PRIMARY-VERIFIED |
| 10 Aug | Mandiant memo (see §2) | [PRIMARY: Mandiant memo PDF on trustage.com](https://www.trustage.com/~/media/pdf/outage/mfr26-691%20investigation%20memo%202026-08-10) | PRIMARY-VERIFIED (text extracted by DEWEY) |
| 12 Aug | CEO Terrance Williams: "two to three months" before answers on member data (**source: [Credit Union Daily, 13 Aug](https://thecudaily.com/more-than-a-dozen-lawsuits-have-now-been-filed-over-trustage-cybersecurity-incident/) quoting "it will likely be 2 to 3 months from now before we have those answers", and [Credit Union Daily, 20 Oct](https://thecudaily.com/trustage-after-100-days-plenty-about-recovery-no-update-on-the-data/) dating it 12 Aug; NOT in the American Banker piece, corrected 22:46 ET on CYPHER's flag**). 14 suits in W.D. Wis. (13 counted by a 29 Jul court order, a 14th the same day); five plaintiffs moved to combine them into credit-union/business and consumer groups; "no judge has yet ruled" | [NEWS: American Banker, 12 Aug](https://www.americanbanker.com/news/cu-vendor-trustage-faces-14-suits-over-monthslong-outage); [NEWS: Credit Union Daily, 20 Oct](https://thecudaily.com/trustage-after-100-days-plenty-about-recovery-no-update-on-the-data/) | SECONDARY-SOURCE |
| 20 Oct (latest) | Status page: Claims (submission, processing, payout), Policy & contract servicing (incl. one-time and recurring payments) and Disbursements (withdrawals, surrenders) **all "Partially available"**; "Existing servicing backlogs, manual processes and system dependencies continue to affect timing" | [PRIMARY: TruStage outage page](https://www.trustage.com/outage) | PRIMARY-VERIFIED |
| 20 Oct (day 100) | Commentary: "plenty about recovery, no update on the data"; the author knows of no evidence that member data was accessed or taken | [NEWS: Credit Union Daily](https://thecudaily.com/trustage-after-100-days-plenty-about-recovery-no-update-on-the-data/) | SECONDARY-SOURCE |

- *Note on 043's detail:* WALTER's read of the CrossState mirror (card claims on hold, one-time payments unavailable, life/AD&D backlog) is **more granular than TruStage's own page**. TruStage's page shows everything as "Partially available" with no per-product holds. The two don't contradict each other, since the mirror relays partner emails, but the per-product holds are partner-relayed (OWNER-ASSERTED), not on TruStage's public page.

### 2. Q1: What was taken? **UNKNOWN (by TruStage's own account).**
- TruStage (31 Jul): "While we do not yet know whether member data was accessed." No later primary changes that. CEO window (12 Aug): 2–3 months, so the window ends ~12 Nov. The "do not yet know" statement is PRIMARY-VERIFIED; **the CEO window is SECONDARY-SOURCE (Credit Union Daily, 13 Aug and 20 Oct; corrected 22:46 ET)**, and the window end is INFERRED from the 12 Aug date.
- **State attorney-general breach lists** (WALTER's suggested cleanest primary):

| List | Result | Basis |
|---|---|---|
| California AG | **0 notices** for TruStage / CMFG / CUNA Mutual / MEMBERS since 2026-06-01 | DEWEY `scripts/breach_notices.py`, run 2026-10-22 ~20:36 ET; SEARCH-NOT-FOUND |
| Washington AG (500+ WA residents) | **0 notices**, same names | same run; SEARCH-NOT-FOUND |
| Texas AG | List did not render to WebFetch (client-side load) | UNREACHED |
| Maine AG | HTTP 403; the database was also noted offline on 10/22 | UNREACHED |
| Vermont AG | Site-restricted search found nothing | SEARCH-NOT-FOUND (weak: search, not the list) |

- **Reading:** finding no notice is consistent with TruStage's "do not yet know". Notices follow a determination, so their absence is not evidence that nothing was taken. A first state notice would be the cleanest primary for "what and how many".
- Mandiant (10 Aug) does not address exfiltration either way. It speaks only to *current* intrusion and third-party interaction (§3).

### 3. Q2: Ransomware? **NOT STATED. No attacker named, no ransom demand confirmed.**
- American Banker (21 Jul): *"It has confirmed no ransom demand and named no attacker."* In context, and alongside "named no attacker", this means TruStage has **not confirmed a demand**. It does **not** mean TruStage confirmed there was none. American Banker (12 Aug) says it the same way: TruStage "has not identified an attacker or confirmed a ransom demand". Credit Union Daily (13 Aug): "has not issued any statement regarding whether ransomware is involved". SECONDARY-SOURCE.
- **Entry route (TruStage's belief, relayed):** "a member of our workforce may have inadvertently downloaded a malicious file while trying to install a legitimate utility" ([American Banker, 12 Aug](https://www.americanbanker.com/news/cu-vendor-trustage-faces-14-suits-over-monthslong-outage)). Bessemer's amended complaint alleges the same thing ("a TruStage representative downloaded malware"); that is an allegation.
- **Shape evidence (not proof):** a "particularly broad attack on our network and systems", a network-wide shutdown, infrastructure *rebuilt* rather than restored, laptop refreshes, and a 100+-day phased return. That is the recovery profile of a destructive or encrypting intrusion. **INFERRED.** No source says ransomware, and DEWEY found no leak-site claim (not searched systematically).
- **Mandiant memo, verbatim (PRIMARY-VERIFIED):** *"TruStage's operating environment is clean, the incident is contained, and Mandiant has identified no indication of any active intrusion. Mandiant has not identified any threat actor activity within the environments in the scope of its investigation since July 11, 2026"*. And: *"Mandiant has also not observed the threat actor interacting with any files shared with third parties, or with any third-party systems, portals, VPNs, APIs, or other environments connected to TruStage."* The memo carries a no-reliance disclaimer: "not intended for use or reliance by any other party".

### 4. Q3: How many credit unions are affected? **NO COUNT GIVEN** (American Banker asked).
- TruStage's own reach claims, as relayed: it serves **"93% of credit unions"** and protects **"42 million consumer relationships"** (American Banker, 12 Aug). An older partner page cites 39 million. **Both figures are carried; DEWEY did not reconcile them.** SECONDARY-SOURCE (TruStage's claim, relayed).
- **Reading:** the outage hit TruStage's own servicing (claims, payments, disbursements) across product lines, so the affected population of *credit unions* is plausibly most of its client base. **That is INFERRED; there is no primary count.** Credit-union notices reviewed say their own systems (online banking, cards, deposits) were **not** affected (e.g. [GNCU](https://www.gncu.org/newsroom/what-you-should-know-about-the-trustage-cybersecurity-incident/), [ACU](https://www.youracu.org/member-notice-trustage-cybersecurity-incident/); SECONDARY-SOURCE). That matches Mandiant's third-party line.
- Named credit-union parties in suits: Bessemer System FCU (plaintiff); Align CU and First Financial FCU (named alongside TruStage in consumer suits).

### 5. Q4: What has it cost? **NO FIGURE DISCLOSED.**
- AM Best (7 Aug): unchanged ratings, "not had a material impact on the credit profile". This is the only quantified-adjacent primary, and it is dated 2.5 months ago. PRIMARY-VERIFIED.
- Litigation: 14 suits, no damages figures; Bessemer "has not put a dollar figure on its own losses"; one consumer plaintiff ~$600 overdrawn. SECONDARY-SOURCE.
- Not found: incident-response cost, business interruption, cyber-insurance recovery, premium refunds (TruStage is "reviewing premiums collected in error during continuity operations", per a search summary only), and royalty-payment effects (a Credit Union Daily headline says Q3 royalties use Q2 amounts; headline only, not read).
- **Where a figure would first appear:** the TruStage insurers' (CMFG Life, MEMBERS Life) **Q3 statutory statements**. These are typically due to state regulators by mid-November, which is INFERRED from the standard NAIC calendar and not checked. Also any AM Best follow-up. TruStage Financial Group is not an SEC registrant as far as DEWEY found (no EDGAR check was run).

### 6. So what for the network
- **Base-rate fit:** this is a US financial-vendor outage lasting **100+ days**, longer than any of the five waves in REQ-008. The transmission ran through **service denial (claims, payments, withdrawals) and litigation**, not deposits or bank failure. That is consistent with the REQ-008 prior that cyber events stay mechanical for banks.
- **Open tails:** (a) a PII determination by ~12 Nov leading to state notices, consumer suits widening, and credit-union notification costs; (b) the Q3 statutory cost line; (c) AM Best's monitoring language (business damage, reputation, enterprise risk management).
- **Not PHP2Shell:** the incident predates the wave by three months, and the entry route was a malicious download.

## Counter-Evidence
- **Against "contained vendor outage":** nobody has ruled data theft *out*. A 100-day rebuild is consistent with destructive malware, and silence about ransomware is not denial. If PII was taken across "42 million consumer relationships", this becomes a mass-notification event touching most US credit unions. Mandiant's clean bill is about *current* activity, not what left before 11 Jul.
- **Against "material":** AM Best saw no material credit impact on 7 Aug. Credit unions report their core systems were unaffected. Mandiant saw no third-party interaction. The day-100 commentary knows of no evidence that data was taken.
- **On 043's framing:** "still not fully back" is right at the primary, though TruStage's page shows partial availability, not hard holds.

## Source Quality Assessment
- Primary, read by DEWEY: TruStage's outage page and two newsroom releases, the Mandiant memo (full text), the AM Best release, and the CA and WA AG lists via script.
- Secondary: American Banker (two pieces, consistent with each other), Credit Union Daily, credit-union notices.
- Unreached: CU Today (403), NAPA (403), the Texas and Maine AG lists, the court docket (no PACER), the Vermont list itself.
- Weak: anything about cost (nothing disclosed) and the 93%/42M reach figures (company marketing, relayed).

## References
(accessed 2026-10-22, 20:34–20:38 ET)
- TruStage outage page: https://www.trustage.com/outage
- TruStage incident update: https://www.trustage.com/newsroom/2026-press-releases/cybersecurity-incident-update
- TruStage recovery update (31 Jul): https://www.trustage.com/newsroom/2026-press-releases/recovery-restoration-progress-cybersecurity-attack
- TruStage clean-environment release (not opened): https://www.trustage.com/newsroom/2026-press-releases/trustage-confirms-clean-isolated-technology-environment
- Mandiant memo (10 Aug): https://www.trustage.com/~/media/pdf/outage/mfr26-691%20investigation%20memo%202026-08-10
- AM Best (7 Aug): https://news.ambest.com/newscontent.aspx?refnum=276260&altsrc=23
- American Banker (21 Jul): https://www.americanbanker.com/news/credit-union-sues-trustage-over-cybersecurity-incident
- American Banker (12 Aug): https://www.americanbanker.com/news/cu-vendor-trustage-faces-14-suits-over-monthslong-outage
- Credit Union Daily (13 Aug, suits): https://thecudaily.com/more-than-a-dozen-lawsuits-have-now-been-filed-over-trustage-cybersecurity-incident/
- Credit Union Daily (20 Oct, day 100): https://thecudaily.com/trustage-after-100-days-plenty-about-recovery-no-update-on-the-data/
- GNCU notice: https://www.gncu.org/newsroom/what-you-should-know-about-the-trustage-cybersecurity-incident/
- ACU notice: https://www.youracu.org/member-notice-trustage-cybersecurity-incident/
- CrossState CUA (WALTER's 043 mirror): https://www.crossstate.org/about/member-resources/trustage-cybersecurity-incident/
- Reproduce the AG pull: `python3 AGENTS/DEWEY/scripts/breach_notices.py --name TruStage --name CMFG --name "CUNA Mutual" --name MEMBERS --since 2026-06-01 --out <file>`

## Process Report
**Searches run:** 9 web searches, 15 page fetches, 1 breach-notice script run (CA/WA), and 1 local PDF text extraction (the Mandiant memo returned compressed binary to WebFetch). No sub-agents.
**Data gaps:** the data-exposure determination (not yet made); attack type; affected counts; any cost figure; the court docket; the Texas, Maine and Vermont lists.
**Source frustrations:** CU Today and NAPA return 403. The Texas AG list renders client-side. The Maine list returns 403 or is offline. The Mandiant PDF needed local extraction.
**Confidence in findings:** High that the primaries say what is quoted. The answers to Q1–Q4 are honestly UNKNOWN or no-figure.
**If I had more time/tools:** a PACER docket read (consolidation status); the CMFG Life Q3 statutory statement in mid-November; a re-pull of the state AG lists after ~12 Nov.
**Suggestions:** `breach_notices.py` could add a Texas route (needs the Salesforce Apex API behind the page). That would be the second occurrence of a Texas-list block if one was hit before; check BACKLOG before adding a row.
