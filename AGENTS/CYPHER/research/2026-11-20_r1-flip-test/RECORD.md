# R1 flip test, WAVE-2026-10 (PHP2Shell): 2026-11-20 record

**Session:** CYPHER, PROME task letter (prome-77, laptop), C6 due-row wake, launched late. Runtime Claude Code, Opus 5.5 (claude-opus-5-5). Boot 2026-11-20 11:33 EST (boot.py wall clock). $0. No trade, spend, external send or authority change.
**Rule read:** `workbook/EXIT_PROTOCOL.md` § R1 (re-derived 2026-10-22), read whole this session. Catalyst row `docket/CATALYSTS.tsv` 2026-11-20 P1, read whole.

## 1. Verdict

| Item | Result |
|---|---|
| Row 1 or row 3 FIRED on or before 2026-11-20? | **No.** Both NOT-FIRED at every in-window check |
| Toward-MOVEit flip | **Not met** |
| Toward-Log4Shell flip | **FIRES.** Rows 1, 3 and 4 all NOT-FIRED at 2026-11-20, from their 2026-10-22 NOT-FIRED, each with dated re-checks inside 2026-11-13..2026-11-20 at its named instrument (section 2) |
| Consequence, by the rule's own text | **R1 state becomes MECHANICAL (Log4Shell-shaped).** Rows stay open; nothing is closed. A row 1 FIRE after 11/20 still flips the stance back (MOVEit's list grew 13+ months; SolarWinds' victims surfaced at +66 days) |
| Packets the rule requires | None (only the MOVEit flip mandates P1 packets). REGINALD and GIBBS carry nothing keyed on R1 (section 4) |

## 2. In-window checks (2026-11-13..2026-11-20)

| Row | Instrument | 11/13 | 11/19 | 11/20 (this session) |
|---|---|---|---|---|
| 1 Named successful PHP2Shell compromise | Victim statement, IR report, national CERT primary | NOT-FIRED (Check Point 070 unnamed; Kiteworks advisory unchanged) | NOT-FIRED (`research/2026-11-19_due-rows/RECORD.md` §7) | **NOT-FIRED.** Dutch NCSC alert read (fetch helper, HTTP 200): "Bijgewerkt: 23 okt 2026 om 15:43", unchanged; names no compromised organisation ("niet bevestigd dat de aanval ook daadwerkelijk succesvol is geweest"). Web search (extended) for a named PHP2Shell breach: only the October government-affiliated and vendor-verified unnamed cases. Kiteworks homepage: no advisory or compromise statement (security.kiteworks.com not read, carried). PLAID/KARTE (section 3) names no flaw: not a PHP2Shell link |
| 3 Named US bank / CU / core-vendor victim | Victim or vendor statement; regulator notice; 8-K | NOT-FIRED | NOT-FIRED (JPMorgan 086 off-wave) | **NOT-FIRED.** Search: no US bank or credit union has publicly reported a PHP2Shell compromise (American Banker "banks dodge early damage", undated in result); MUFG/PLAID (089) is Japanese and has no PHP2Shell link |
| 4 8-K Item 1.05 from a bank/vendor citing PHP | EDGAR full-text, boot.py leg 8 | NOT-FIRED (LIVE, none since 11/06; control 16) | NOT-FIRED (LIVE, none since 11/12; control 15) | **NOT-FIRED.** boot leg 8 LIVE 11:33 EST: no Item 1.05 8-K filed since 2026-11-13; control population 13 in 120 days |

The quiet is a multi-channel conjunction (EXIT_PROTOCOL conjunction warning). Its FROM state is the 10/22 NOT-FIRED; the historical window that satisfies it is Log4Shell's (disclosed 2021-12-09, quiet at 2022-01-08). It is used here to set a stance, not to close the wave, as the rule requires.

## 3. What the rule cannot see (applied as written; disagreement recorded)

The flip keys on a NAMED organisation. The composition under the quiet is not Log4Shell's "attempts only":

| Fact | Source | Basis |
|---|---|---|
| Palo Alto's Unit 42 verified Dream's PHP2Shell + Fragnesia chain rooting 24-25 firewalls; about .02% of installed base impacted, customers contacted | CYB-INC-047 | PRIMARY-VERIFIED, victims unnamed |
| Check Point: successful compromises of Mobile Access gateways from 10/30, root via CVE-2026-123039, a wiper at some Israeli victims | CYB-INC-070 | PRIMARY-VERIFIED, victims unnamed |
| A US government-affiliated network had credentials extracted | CYB-INC-047 | Researcher report, unnamed |

So the right reading is **"MECHANICAL for banks, with confirmed but unnamed compromises outstanding"**, not "no damage". The weak-evidence rule (charter boot card item 2) applies: "no named victim" is not "no victim". The stance change moves no score, band or gate (VX composite stays 25/40 raw, 16/40 adjusted).

## 4. Does the flip change anything REGINALD or GIBBS carry?

| Desk | What it carries on this wave | Changed by the flip? |
|---|---|---|
| REGINALD | Nothing keyed on R1 or WAVE-2026-10 in STATUS, workbook or docket (grep 11/20) | No |
| GIBBS | KB-GIB-025 (PHP2Shell consequence NOT OBSERVED at the 16, 10/31); STATUS cyber line (11/19) | No: its reading is already the mechanical one |

No packet sent to either: the letter asks for one only if the flip changes something they carry. Named in the PROME packet so the decision is visible.

## 5. New this session (off-wave)

- **CYB-INC-089 MUFG / PLAID KARTE.** MUFG Bank notice 2026-11-18 (bk.mufg.jp/news/news2026/pdf/news1118.pdf, PDF extracted locally with pdfminer, PRIMARY-VERIFIED): unauthorized access to PLAID's KARTE (outsourced web/app customer-guidance service) occurred 11/13; MUFG told of the leak scope 11/17; leaked: gender, age, region (prefecture or designated city), "約 650 万件" (about 6.5 million records); no names, addresses, phone numbers, emails or anything that identifies or contacts a customer; "本件は当行のシステムが不正アクセスを受けたものではありません" (the bank's systems were not accessed); no misuse found to date. PLAID notices 11/13, 11/16, 11/20 (plaid.co.jp/news, fetch helper): detected 11/13 08:59, contained ~15:23; "a third party exploited a vulnerability in our server to steal connection credentials" (11/16); "a vulnerability in some internal processing on a public-facing route" (11/20); **no product, CWE or CVE named**; 570 client companies' linked data, 754 companies' integration credentials (overlapping); PPC reported, police consulted; KARTE phased restart targeted mid-January 2027; client-level detail from 11/24. Secondary only: MUFG Trust ~230,000 records (Rocket Boys, citing tr.mufg.jp 261118_2.pdf, unread); a blog claims five MUFG companies and ~8 million total (only MUFG Bank's figure has a primary).
  - **Correction for WALTER:** card SIG-W-20261119-011 said the MUFG 6.5M claim was "NOT FOUND ... do not relay as fact". The figure is MUFG's own. The aggregator's "customer records" framing overstates it: the fields are non-identifying demographics.
- **CYB-INC-085 N-able:** SecurityWeek 11/20 04:08 ET and BleepingComputer 11/20 08:18 AM: N-able now says the breach caused the worldwide Mail Assure / SpamExperts Hosted Cloud outage (from 11/16 per SecurityWeek; "Tuesday" per BleepingComputer); attacker "may have been able to access certain credentials stored on the platform"; internal credentials rotated, customer API tokens revoked, OAuth tokens invalidated, local passwords reset; portal and API still disabled; no evidence of customer data or mailbox access; unrelated to N-central. No FI named.
- **PHP 11/19 releases (KB-CYP-141 follow-up):** 8.6.0, 8.5.13, 8.4.28, 8.3.37, 8.2.36 (each point release "a security release"). 8.5.13 ChangeLog lists 18 CVE entries: CVE-2026-129474, -129182, -129538, -129496, -129501, -129291, -129289, -129292, -128090, -15353, -129506, -126714, -115560, -129481, -128064, -127960, -129438, -48841. CVE-2026-115560 (watched on boot leg 7, absent from KEV) is among them. 8.3/8.2 sections not read.

## 6. Overdue re-checks (boot leg 5)

| Row | 11/20 reading | State |
|---|---|---|
| 036 Commonwealth Community Bank (Qilin claim) | Only a tracker (Breachsense, discovered 10/26) carries it; no bank, regulator or AG notice found | REPORTED, re-dated |
| 039 Delta Electric Power Association (Qilin claim) | No 2026 report found (results are the 2021 Colorado DMEA case) | REPORTED, re-dated |
| 043 Park24 / Times Car | Company's own notices exist (share.timescar.jp 2026/09/28; search summary, page not read): ~6.6M accounts; 10/23 follow-up per MLex: ~1.46M encrypted ID images sent out, ~892,000 accessed not sent, JPY 3,000 to those with both | CONFIRMED · SECONDARY-SOURCE |

## 7. Inbox (8 WALTER cards: 6 at launch, 2 arrived mid-session)

| Card | Disposition |
|---|---|
| 20261119-010 Florida storms / FLHSMV | LOGGED. FLHSMV said "degradation of services" (X, ~11:00 ET 11/18); press ties it to ORION, one outlet to a vendor upgrade; no cyber vector stated. Out of scope (non-financial, no cyber vector) |
| 20261119-011 cyber claims | ACTED. MUFG -> CYB-INC-089 (claim is real; correction to WALTER). European Commission ARTEX attack: NOT FOUND by CYPHER's search either (only the January and March 2026 incidents); claim only. DHS Iran-linked / senators AI threats: board_log only, no financial victim |
| 20261119-015 correction of card 010 | DISCARDED, CORAL owns. Corrections receipt COR-20261119-15 NO-OP |
| 20261119-016 FALCON and GIBBS grades | LOGGED. GIBBS's JPMorgan grade added to CYB-INC-086 notes |
| 20261119-019 HANS grades | LOGGED. HANS logged Wellington IT (087) as no funding or processing event; EC claim not found by HANS either |
| 20261120-001 FLASH VIX/AI-chip selloff | DISCARDED, not cyber: VIOLET (vol), HENRY (equity), VULCAN (AI/chips) own it |
| 20261120-006 small items (arrived mid-session) | LOGGED. White House cyber official removed after outages (FT/BBC titles, unread) -> note on CYB-INC-076; TruStage and N-able lines already held (017, 085) |
| 20261120-009 Will's bookmarks 11/19 (arrived mid-session) | ACTED. Visa and Mastercard statements -> CYB-INC-081 (Mastercard: a subset of cardholders in a benefit program, contained, no network impact; via WALTER's read of a WSJ excerpt image). FAA to announce ground-stop cause -> note on 076. Cairncross leaving: not found by CYPHER's search; titles only; no row. USDA cyberattack: NOT FOUND by CYPHER's search either; claim only |

## 8. Forward view (PROJECTION, kept apart from the evidence above)

- **Expect:** the wave stays mechanical for banks through year-end. Why: 30 days of disclosure, three vendors confirming unnamed compromises, yet no bank, credit union, core vendor or 8-K Item 1.05 has surfaced; the damage so far lands on appliance owners and on the patch side (outages from emergency patching), and a second PHP patch round (11/19) adds to that patch-side load rather than to the compromise side.
- **Meaningful alternative:** the MOVEit/SolarWinds tail, a named victim surfacing late through a breach notice, an 8-K or an IR report. Already registered: CYP-07 (a named PHP2Shell victim by 12/31, 45%) and CYP-02 (a named US bank / CU / core vendor tied to a wave vector by 2027-01-31). Not re-registered.
- **Separate event, unscored:** a US bank or payment operator ties an outage to PHP patching (row 8) before 12/31. My judgment: about 15%, given the second patch round and the DNI's 11/17 tie of the NSA outage to PHP patching. Not registered (no fixed settle source beyond row 8's adjudication; WQ-601 unit 4 governs new rows).
- **What would change my mind:** one named organisation confirmed through CVE-2026-109618/-109619 (flips R1 back toward MOVEit the same session); any bank-side 8-K Item 1.05 citing PHP.
