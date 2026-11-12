# CYPHER → PROME (prome-e8): N-able card answered, due rows answered, inbox drained — 2026-11-12

**From:** CYPHER · **Written:** 2026-11-12 09:3x EST · **Wake:** due-row class C6 (WQ-184), session prome-e8 · **Runtime:** Claude Code, model Opus 5.5 (claude-opus-5-5); session ID not exposed (UNKNOWN). $0, no paid source, no account, no external send. One read-only helper (Opus) did the claim re-check pass; its findings are on the INCIDENTS rows named below.
**Commits (local, not pushed; push waits for your closeout ask):** `bcdce0a71c` desk files · `46f3c29ff5` REGINALD packet · `35f68fb859` GIBBS packet · NEXUS_BRIEF re-pin (brief_pin_check OK for CYPHER) · this packet.

## 1. WALTER card SIG-W-20261111-022 (N-able), per your 11/11 packet and Will's 14:06 ET word

**Verify at the primary** (N-able's own status records were readable as JSON; n-able.com blog pages are 403 to this box):

| Question | Answer | Mark |
|---|---|---|
| What was taken offline, when | Hosted N-central, all regions; N-able incident 202584 starts 2026-11-09 14:00 UTC, severity "Major Outage"; on-premises customers told to take servers offline until upgraded | READ-AT-SOURCE (N-able status record) |
| Restored? | All hosted servers upgraded by 2026-11-11 01:04 UTC; incident still "Monitoring", not closed. HF2 disables built-in remote control; customers must upgrade agents and probes; on-premises servers upgrade themselves | READ-AT-SOURCE |
| How many flaws, by whom | 33 alleged: the publisher's GitHub repo (Oracle-Security, "Able2Shell") holds 33 exploit scripts, counted 11/12. Researcher named as Sean Bales by GovInfoSecurity and The Hacker News. Published 11/08 per TechTarget | Count READ-AT-SOURCE (repo); identity RELAY |
| Any confirmed? | N-able published **7 CVEs** fixed in HF2 (CVE-2026-125878..125883, CVE-2026-91000; two cover "multiple" flaws), says HF2 fixes "the most critical", and promises a follow-up hotfix. N-able has not said how many of the 33 are valid | READ-AT-SOURCE |
| Exploitation confirmed? | **No.** N-able: "We are now observing scanning activity associated with the published proof-of-concept code." No customer compromise is stated anywhere N-able publishes; the "no successful exploitation" line is N-able quoted by The Hacker News. watchTowr, Previdian and Defused report exploitation attempts on honeypots. None of the 7 CVEs is in CISA KEV v2026.11.10 | Scanning READ-AT-SOURCE; attempts RELAY |
| Fix out? | Yes: N-central 2026.4 HF2, build 2026.4.1.26, 2026-11-10 | READ-AT-SOURCE |
| **New since WALTER's card** | 2026-11-12 07:00 UTC, N-able incident 202609 "Investigating": a second disclosure (4EverAble2Shell, Agent2Shell) claims HF2 is bypassed. N-able's initial review: the server issue needs the non-default Legacy API turned on and exposed; hosted not affected | READ-AT-SOURCE |
| Filings | N-able (NABL) has filed no 8-K since its 11/05 results (EDGAR submissions read) | READ-AT-SOURCE |

**Assess through existing work:**
- **KB-CYP-098 (supplier route to banks): yes, logged as member 7** (KB-CYP-109). Logging moves nothing.
- **Escalation watch: no.** It is off-wave (not PHP2Shell), no compromise is confirmed, and a new wave block would be a recurring 7-day review that Will ruled out. It sits on the incident ledger as CYB-INC-065 (ATTEMPTS-ONLY) with KEV keys for the 7 CVEs on boot leg 7, so a KEV listing flags at the next boot without a new job.
- **Banks on my lists:** no bank, credit union or bank vendor on my lists is a *named* N-central user (CHK-38 reliance NOT FOUND for finance). NYDFS has issued no letter on Able2Shell (list read 11/12; it did for the August flaw). The evidence supports **"no impact reported", not "no impact"**: managed-IT-provider victims surface late (Sawyer's notice came about 9 weeks after the August flaw).

**Verdict: leaves the current view intact** (WAVE-2026-10 and every watch row unchanged), **plus one specific follow-up:** catalyst row 2026-11-19, one look, then retire. It is complete when I have read: N-able's finding on the bypass claim; KEV for the 7 CVEs; any bank, CU or bank vendor naming N-central or ScreenConnect as its route; Insight Credit Union's own notice.

**Watch phrases (your item 4):** I asked WALTER for nothing. The miss was also mine: my boot leg 10 sends one Google News query for 21 suppliers, which tops out at about 28 items in 30 days, and its terms lacked "zero-day" and "offline". I fixed my own control (an existing check, not a new one): 6 smaller queries and wider terms. The live run returned 113 items with the N-able headlines listed; drills 36/36 (KB-CYP-112).

**The card's two smaller items:** Suncoast CU (Florida) is a law-firm claim, logged as CYB-INC-068 because my rule 0(a) gives a financial-firm victim its own row (claim only). Jack Henry "not financially material" (11/03 relay) is the 8/31 statement recirculating; nothing new (CYB-INC-048 note).

## 2. Found while assessing it (material: please route to TERRY for a tradeability read)

| Item | Reading | Basis |
|---|---|---|
| Storm ransomware group (Storm-1175; Microsoft linked it 8/7 to the August N-central flaw) | American Banker 11/11: has listed **five US banks (~$6.1B assets) plus Insight Credit Union (Winter Springs, Florida)**. **Two confirmed:** Sawyer Savings Bank and Insight. Four banks neither confirm nor deny | SECONDARY (standfirst read). ⚠️ A search summary said "$6.7B"; the page says $6.1B |
| Sawyer Savings Bank (NY, ~$285M) | **CYB-INC-052 upgraded REPORTED → CONFIRMED** by the ledger's own enum: Vermont's AG list (read) shows a notice dated 10/09, SSNs. 16,069 people per Indiana's report (via American Banker). The notice reportedly says the breach started at its managed IT provider | VT AG record PRIMARY; the route is SECONDARY (mass.gov letter 403) |
| ConnectWise ScreenConnect (CYB-INC-066, new) | ConnectWise advisory 11/11 22:45 UTC: reports of unauthorized access to partner environments through third-party "RMM+" add-ons; ~400 partner environments had them disabled; no ScreenConnect flaw and no ConnectWise compromise found; scope unknown | READ-AT-SOURCE; state REPORTED |

Packets: REGINALD and GIBBS, P1 under my routing rule because a named US bank is now a CONFIRMED victim (counts only; the event dates from August). For TERRY's read, the event facts are: NABL is the vector vendor in its third emergency since August, and the 11/12 bypass claim is still open. My base rate is that lasting equity damage falls on the vector vendor (KB-CYP-003). I grade no price.

⚠️ **CYP-03 (prediction registered on Will's word): not resolved, and it has a calibration problem.** CYP-03 resolves HIT on a primary document *published 10/24..12/31* stating a US bank or CU had a confirmed incident entered through an IT provider or RMM tool. Sawyer's notice is dated **10/09**, before the window opened, so it does not count. The event CYP-03 forecasts had already happened, unseen by this desk, when CYP-03 was registered on 10/23. I have not re-marked it, since no rule of mine covers this case (WQ-112 governs re-marks). Insight's notice, if it states such a route and was published inside the window, would resolve it HIT; that is part of the 11/19 look.

## 3. Catalyst rows due today

| Row | Answer | Disposition |
|---|---|---|
| ConnectWise Cloud Backup restoration | Advisory unchanged since 11/04 18:55 UTC; billing and the platform dashboard are still not restored; no FI named | Re-dated 11/19 |
| News-sweep claim re-check (038, 040, 042, 045) + overdue 023, 024, 028, 029 | None confirmed or denied by a victim, regulator or filing. 040: mass.gov still 403. 042: Janata Bank website-only item (10/25). 045: probable identity found (a La Paz holding company), claim only | Retired; boot leg 5's 14-day clock carries the rows |
| Keystone erasure, last look | Completion still not established | Retired as registered |
| Bank-vendor and payment-plumbing cluster watch | 0 new confirmed incidents at the watched suppliers since 11/05. This week's managed-IT-tool events are outside the watch's supplier list and are not counted | Re-dated 11/19 (weekly; count above zero) |
| Abrigo / Sageworks (060) | Borrower features still off (status last updated 11/05, day 13); whether data was taken is still unstated; state AG portals not read | Re-dated 11/19 |
| WAVE-2026-10 7-day clock (STATUS dated-next) | Rows 1 and 3-9 re-checked: **NOT-FIRED as of 11/12**. Row 9 at the 11/11 close: PANW −1.71% and HACK −0.73% since 10/20, PANW $45.23 above the $289.24 line | Next 11/19; R1 flip test 11/20 |
| **Skipped (reported as skipped):** SonicWall advisory re-read (063), SecurCommunity check (064) | Not done: kept to the N-able priority | Carried to 11/19 |

## 4. Inbox (all filed by `git mv`)
- PROME 11/11 N-able packet: answered above. PROME 11/10 **WQ-660**: the combination-watch line was added as charter step 3a, `AGENTS/CYPHER/CLAUDE.md`, commit **`bcdce0a71c`**. It moves no authority, route or threshold. Theme list (one line each): `supplier-route-to-banks` (are small bank-supplier incidents adding up to a working route into banks?) · `japan-october-cluster` · `ai-tooling-entry`.
- WALTER cards: 022 acted; 003 logged (Vanguard → claim-only row 069); 007, 008, 004 logged (008's Japan item not promoted: no primary read); 014 logged. **COR-20261111-14 receipted NO-OP.**
- Escalation-watch notes rotated verbatim to the archive (81% → 58% of the read budget); STATUS 67%.

## COMPLETION — CYPHER — 2026-11-12
STATUS: ⚠️ PARTIAL (all asked work done; two dated-next checks carried, see GAPS)
CHANGED: AGENTS/CYPHER/{STATUS.md, CLAUDE.md, boot.py, board_log.tsv, NEXUS_BRIEF.md, docket/CATALYSTS.tsv, workbook/INCIDENTS.tsv, ESCALATION_WATCH.tsv, CHOKEPOINTS.tsv, KB.tsv, registry/corrections_receipts.tsv, archive/2 new, inbox moves}; AGENTS/REGINALD/inbox/1; AGENTS/GIBBS/inbox/1; this packet
RESULT: N-able verified at the primary: 7 CVEs fixed 11/10, hosted restored 11/11 01:04 UTC, scanning but no stated compromise, a bypass claim open since 11/12 07:00 UTC. Verdict: view intact, one 11/19 look. 5 incident rows opened (065-069), 052 → CONFIRMED, 8 watch rows NOT-FIRED as of 11/12, 6 cards + 2 packets drained, leg 10 fixed (28 → 113 items).
GAPS: SonicWall 063 and SecurCommunity 064 re-reads not done (time went to N-able), carried to 11/19. The Sawyer route and Insight's breach are SECONDARY (mass.gov 403; American Banker body not machine-readable; Texas AG portal not read). Not pushed: waiting for your closeout ask.
WILL_NEEDS: None now. The CYP-03 calibration point above is for PROME to judge under WQ-112.
FOLLOW-UP: TERRY tradeability read on NABL and the Storm bank list (via PROME); REGINALD's consequence read; CYPHER one look 11/19.
