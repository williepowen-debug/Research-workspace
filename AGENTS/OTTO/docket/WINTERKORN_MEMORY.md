# WINTERKORN — Memory (state)

State file for `WINTERKORN.md` (OTTO docket steward). Read this right after the spec.

State lives in the sections below; this header carries none. *(It read "Inaugural state — no prior runs" through three runs.)* Older run entries, cleared PENDING blocks and superseded hints → `WINTERKORN_MEMORY_ARCHIVE.md` (verbatim; OTTO moved them 2026-10-14, s029).

---

## CHANGES SINCE LAST RUN

*(2026-10-28 ~22:10 ET, WINTERKORN run start: what moved in the read-set between the 10/14 run and tonight, 14 days)*

- **OTTO sessions in between:** s030–s036 (10/19 bounded closeouts; 10/25 owner overlay, which was not a WINTERKORN run). OTTO hand-added rows: 10/28 CRMT backstop #5 (BROCK), 10/30 THESIS v1.6 target, 11/01 CRMT bridge-8 expiry (BROCK, 🔴), 11/05 M&T 10-Q check (`modeled`), 11/30 year-end readiness follow-up, ~12/01 Hertz watch (`modeled`). OTTO archived the swept 9/15–10/15 rows (archive 28 → 47 rows).
- **Fired since 10/14, carried unverified from 10/25:** 10/16 BlackRock confer deadline · 10/20 First Brands D&O hearing · 10/21 §721 hearing · ~10/21 Chu suppression check · 10/27 First Brands §341. Carvana Q3 fired tonight; OTTO read it and STATUS already shows it FIRED.
- **Tooling moved:** the CourtListener SEARCH API answers 401 to anonymous calls tonight (it worked through 10/25; DEWEY's `recap_pull.py search` fails). The per-docket RSS feed `courtlistener.com/docket/<id>/feed/` works anonymously and is now the first instrument. Verita's POST works again (it was 403 on 10/25). The Kroll page loads, but its docket-data endpoint returns an empty body.
- **Diff I ran against:** 28 hot rows + 47 archive rows = 75 at start.

*(2026-10-14 ~22:40 ET, WINTERKORN run start — what moved in the read-set between the 7/25 run and tonight, 81 days)*

- **Cases:** First Brands plan confirmation DENIED 8/24 and every debtor converted to Ch.7 (order ENTERED 9/1, Dkt 3748): the Ch.11 hearing cycle is over and the track is trustee administration. Tricolor: ECF 149 Bill of Particulars (filed 8/28, read by OTTO 10/14) charges 11 TAST deals back to 2018; suppression motion argued 9/24, evidentiary hearing 10/7. CRMT (BROCK-owned) bridged six times, STD now 10/15.
- **Predictions:** OTTO-30 FALSIFIED 8/14 (bank-contagion leg down); OTTO-06/-29/-32 resolved 9/30, OTTO-10 → NEEDS_VERIFY (re-check row 12/15). OPEN: OTTO-07/-11/-12/-31/-33/-34 (12/31), OTTO-35 (2027-06-30).
- **Docket structure (OTTO 10/14):** 28 swept rows archived; job step 1 is now ARCHIVE (30-day rule), never delete. Fitch class and the non-MTB/ALLY banks DECLINED; Manheim and the 10-D cycle added as classes. STATUS gained a CONVERGENCE MATRIX (s029) and rotated its swept timeline rows to `STATUS_COLD.md`.
- **Diff I ran against:** 33 hot rows + 28 archive rows = 61 at start.

*(2026-10-14, OTTO s028 — written by OTTO for the next run to diff against; WINTERKORN has NOT run since 2026-07-25, 81 days)*

- **Rows OTTO added BY HAND in s028 — not WINTERKORN output; verify each date at its source:** 2026-10-15 CRMT bridge-6 STD (8-K read at primary) · 10-16 M&T Q3 (BROCK's issuer-verified calendar) · 10-20 Ally Q3 [PRESS] · 10-21 CRMT backstop #4 · 10-21 Carvana T-7 short-seller check · ~10-21 Tricolor suppression-ruling check (modeled) · 10-28 Carvana Q3 [PRESS] · 11-06 Manheim October release (Cox page).
- **Swept by OTTO in s028:** 10/1 CRMT STD, 10/7 backstop, 10/1 10-D cycle, 10/1 seasoning deliverable, 10/1 Tricolor Counts 7-8 (RESOLVED: ECF 149 filed 8/28).
- **Tooling fact for the Tricolor SDNY track:** the CourtListener SEARCH API reaches *US v. Chu* (docket 72046760) unauthenticated via `AGENTS/DEWEY/scripts/recap_pull.py search`. Use it before any press search.

*(Older CHANGES block → `WINTERKORN_MEMORY_ARCHIVE.md`, moved verbatim 2026-10-14.)*

---

## LAST RUN

### 2026-10-28 (~22:10–22:23 ET): trigger = OTTO cadence spawn, 14 days after the last run. Priority: the fired court rows carried unverified since 10/25
- **Archive: 0 moved.** No hot row is older than 30 days; the oldest is 10/16 and the cutoff is 9/28. **Count conserved:** 28 hot + 47 archive = 75 → 32 hot (28 kept + 4 added) + 47 archive = 79.
- **Fired court rows: the fact at source for each, all written into the row notes:**
  - **10/16 Tricolor BlackRock 2004: FIRED, resolved by court order.** There was no agreed order: letter briefs and discovery protocols went to Chambers. Verita **Dkt 1472** (signed 10/22, entered 10/23; PDF read, sha256 `03bbb6429dd82e9e19071f7f773826cac35caee94c3744e994d0c6d7eec50fe4`): Motion GRANTED, and BlackRock applies the **Trustee's** responsiveness criteria. BlackRock keeps protective-order rights over commercially sensitive information, non-Debtor investments and third-party client confidential information. Disputes go to in camera sampling with categorical rulings. The order names no new party.
  - **10/20 First Brands D&O (Dkt 3669): ACKNOWLEDGED-PENDING.** Held (clerk 3956). Transcript Dkt 3990 is restricted to 1/25/2027. Edward James (3985) and Patrick James (3991) ordered daily transcripts. **No order on 3669** in CourtListener's index through Dkt 4003 (RSS feed + RECAP storage + the 10/25 cached search). Scoped to that index; not a negative.
  - **10/21 First Brands §721 (Dkt 3796): FIRED, CONTINUED to 2026-11-17 1:00 PM CT** (hybrid). Sources: Dkt 3997, filed 10/27 by Sommers's counsel, PDF read, sha256 `258a0111961d6a9cdcf7cc92dcc9dc909aebc8e18dd86fe8d9a82545b5995ac9`, plus the 10/27 clerk minute entry. On 10/21 itself there was a status conference: witness Daniel Jerneycic, exhibits admitted (clerk 3973).
  - **~10/21 Chu suppression (ECF 108): ACKNOWLEDGED-PENDING.** The hearing **closed 10/9**: *"Government rests. Defense rests. Court reserves decision."* Post-hearing letters ECF 185 (10/16, Chu), 186 (10/21, USA) and 187 (10/22, Chu, motion to strike 186 or for leave to reply). **No ruling in CourtListener's index.** The newest item is a **SEALED minute entry dated 10/26**, content unknown. The 10/13 unnumbered "Evidentiary Hearing" entry is still textless. The 10/9 entry shows the hearing ended that day, so 10/13 is not shown to be a hearing day.
  - **10/27 First Brands §341(a): FIRED, HELD and concluded** (minute entry 10/27 filed by Engelhart: *"Debtor appeared by zoom, potential assets"*). A §702 permanent-trustee election was possible at this meeting (Onset, Dkt 3989). The minute entry is silent on whether one was requested. No UST election report seen through Dkt 4003.
  - **10/28 Carvana Q3: FIRED.** Accessions -000066 (8-K 2.02/9.01, 20:05:55Z) and -000067 (10-Q, 20:11:03Z) confirmed at the EDGAR submissions JSON. Content is OTTO's.
- **Added (4):** 11/02 First Brands hybrid status conference 1:00 PM CT on Dkt 3933, the McHenry wind-down sale (Dkt 3996 + clerk minute entry) · 11/17 First Brands continued §721 + Evolution turnover hearing 1:00 PM CT (Dkt 3997) · ~12/15 SDART+BLAST November-collection 10-D (`modeled`) · ~12/30 EART November-collection 10-D (`modeled`; window 12/29–12/31; the "December 2026 10-D" that OTTO-34 names).
- **Not touched (owner instruction):** 10/28 CRMT backstop #5 and 11/01 CRMT bridge-8 (BROCK) · 10/29 EART September 10-D (OTTO reading it) · 10/30 THESIS target (internal).
- **Pre-fire (7 trading days, 10/29–11/06): 7 rows scanned, 0 date revisions.** 11/02 new at source · 11/04 NY Fed: no advisory yet (URL probes 10/20–10/28; web search), Q3 xlsx 302 vs Q2 control 200 · 11/05 M&T: Q3 10-Q not filed at 10/28 (EDGAR) · 11/06 Manheim: not re-read at Cox (old URL 404), but the 10/14 receipt and the 5th-business-day rule agree. 10/29 / 10/30 / 11/01 owner-held.
- **Re-verified beyond the window:** Tricolor §341 11/11 10:00 CT (Verita: the 6/2 Dkt 1213 notice is still the only continuance notice through 10/28).
- **Modeled-date revisions: none.** The ~10/21 Chu row stays as OTTO's check date, with next-check 11/04 in its notes.
- **Discovery (in PENDING 2026-10-28):** the First Brands DIP-agent cash-sweep stipulation fight and the "broader settlement and financing" with the Ad Hoc Group · Chu MILs (ECF 178: exclude the government's expert Prof. Christopher Palmer; ECF 184: government MIL with exhibits "Amended Petition", "Chu Declaration", "Radford Letter") · Tricolor trustee interim reports 10/28 (final report still projected 9/30/2030) · Tricolor vehicle-sale deadline extended again (Dkt 1467, 10/16) · James 1:26-cr-00029 ECF 141–143 (an unidentified motion and its opposition).
- **Sources:** CourtListener RSS feeds (6 dockets) OK · RECAP storage (HEAD probes, positive-controlled on Chu 176 and FB 3973; 28 FB PDFs read) · Verita POST OK (the 2nd POST 403'd once, the 3rd OK) · EDGAR OK · Inner City Press OK (pointer only). **Failed:** CL search API 401 · Kroll `Home-LoadDocketData` empty body · NY Fed news page 302 · Cox category page 404.
- **Baseline audit:** no audit trigger this run. Monthly: the first November run. Post-miss: none flagged.

### 2026-10-14 (~22:36–22:58 ET) — trigger: OTTO spawn after an 81-day lapse; first run of October, so the monthly baseline audit fired

- **Archive: 0 moved.** The only row older than 30 days (8/17 EART 2026-4) has no outcome, so it is ESCALATED as passed-but-unswept (folded into the 10/21 row). **Count conserved:** 33 hot + 28 archive = 61 → 42 hot (33 kept + 9 added) + 28 archive.
- **Pre-fire: 13 rows in the 10/15–10/23 window (10 existing + 3 added tonight at source); 0 date revisions.** Verified: CRMT 10/15 STD (DATE ONLY, at the 8-K text + index page; feed shows nothing after 10/8) · CRMT 10/21 backstop arithmetic · SDART/BLAST ~10/15 cadence (6 of 6 on the 15th or the next business day; none filed yet) · MTB 10/16 + ALLY 10/20 (issuer scheduling releases, press mirrors) · CVNA 10/28 → T-7 10/21 · Chu suppression ~10/21 (ECF 171; an unexplained 10/13 entry, see PENDING). Internal rows (10/19, 10/20, 10/21 OTTO-07) need no check. Receipts sit in each row's notes.
- **Re-verified beyond the window:** Tricolor §341 11/11 10:00 CT (Verita) · Chu 12/4, 12/9, 1/25/27 (no adjournment entries 8/15–10/13) · Manheim 11/6 (Cox) · EART ~10/29 (window 10/28–10/30).
- **Added (9):** 10/16 Tricolor BlackRock 2004 confer deadline · 10/20 First Brands D&O-insurers hearing · 10/21 First Brands §721 hearing · 10/27 First Brands §341(a) · ~11/04 NY Fed Q3 window (`modeled`) · ~11/12 EART 2026-5 window close (`modeled`) · ~12/07 Manheim Nov (`modeled`) · 2027-02-01 First Brands criminal PTC · 2027-02-09 First Brands criminal trial.
- **Refreshed / stripped (TRUTH MODEL rule 2):** live prints removed from the 10/15, 10/29 and 11/06 rows. Prediction confidences removed from 10/16 and 10/21. 10/20 WINTERKORN row → DONE EARLY. The 10/21 suppression event text, the 11/11 time and the 12/31 what_to_check (added OTTO-33/-34) were corrected.
- **Modeled-date revisions: none.** All modeled rows match STATUS.
- **EART 2026-4 ISSUED** (8/19 → 8/28; first 10-D 9/29). Facts are on the 8/17 row for OTTO's sweep.
- **Discovery:** three items, all in PENDING 2026-10-14: the First Brands criminal trial 2/9/27 with cooperators docket-confirmed; the Tricolor trustee's Rule 2004 examination of BlackRock; the First Brands trustee Engelhart docket-confirmed.
- **Sources:** EDGAR (submissions, index, FTS) OK · CourtListener SEARCH ~10 calls + 1 RECAP PDF (1:26-cr-00029 ECF 139, VERIFIED, sha256 8bf642a9…) · Verita POST OK after a rebuilt CA bundle · Cox and NY Fed OK. Blocked: ir.mtb.com, truckpartsandservice.com (403).
- **Baseline audit:** fired (monthly). Delta in PENDING.

*(The 2026-07-25 run entry → `WINTERKORN_MEMORY_ARCHIVE.md`, moved verbatim 2026-10-14.)*

*(The 2026-07-04 and 2026-06-09 run entries → `WINTERKORN_MEMORY_ARCHIVE.md`, moved verbatim 2026-10-14.)*

---

## PENDING

> **✅ OTTO dispositions of the 2026-10-14 PENDING blocks (s029, same night):**
> - **First Brands criminal track** — assessed, **not** a cooperating-witness trigger firing: the cooperators' case (US v. Brumbergs, 1:26-cr-00025, Torres) was filed early 2026, so this is OTTO's discovery latency, not new cooperation (the OTTO-30 trap); OTTO re-checked the case number at CourtListener 10/14. The dates (pretrial 2/1/27, trial 2/9/27) go to STATUS and to WALTER for BROCK. The Brumbergs / Graham names are now docket-sourced; their cooperation still rests on one press article.
> - **BlackRock Rule 2004** — an OTTO-33 *lead*, recorded in the ledger note; not an implication. OTTO did not re-read Dkt 1298.
> - **STATUS-SYNC** — applied: six rows added; Dec 9 and Dec 31 priorities follow the TSV (TRUTH MODEL rule 1).
> - **SWEEP-FACTS (EART 2026-4)** — swept (ISSUED; OTTO re-checked at EDGAR) and archived.
> - **SPEC ERRATA** — all four fixed in `WINTERKORN.md` (judge, bank list, RETURN template, docket ids).
> - **BASELINE AUDIT delta** — NY Fed Q3 row accepted as added · Kingsbridge 10/23 admin-expense hearing DECLINED (routine, no OTTO action gate) · OTTO-35 resolve row: propose ~150 days out · Bridgecrest window: deferred as proposed.
> - **CALENDAR-AMBIGUITY** — open; left to the next run.

OTTO-side decisions / actions queued from prior runs. WINTERKORN adds new items; OTTO clears resolved-by-OTTO ones. WINTERKORN never removes its own entries — that's OTTO's job.

> **✅ ALL 3 JUN-9 PENDING BLOCKS CLEARED 2026-07-04** (OTTO): (1) Carvana Jun-12 prod-2 CALENDAR-AMBIGUITY → confirmed PHANTOM, catalyst retired (WINTERKORN's halt-on-ambiguity was correct); (2) Tricolor Nov-11 + Jun-17 STATUS-SYNC → applied (Nov 11 in TSV+STATUS, Jun 17 swept); (3) 5-delta BASELINE AUDIT → all applied/superseded (Fitch prints, NY Fed Q2, Tricolor Nov 11 all docketed; rating-agency #3 stays DEFERRED in CALIBRATION). **No open PENDING as of Jul 4.** Historical blocks retained below for audit trail.

> **✅ ALL 4 JUL-25 PENDING BLOCKS CLEARED SAME-SESSION 2026-07-25 (OTTO s016).** Dispositions inline under each block below. Summary: (1) PREDICTIONS-SYNC → **no re-dating needed**, no OPEN prediction was gated on the Tricolor trial — but the *absence* was itself the finding, and **OTTO-33 was created** to give the book criminal-track exposure. (2) STATUS-SYNC → **all 5 propagated**. (3) SCOPE/examiner → **was NOT integrated; now integrated**, standing monitor added. (4) CALENDAR-AMBIGUITY → 1 of 3 resolved independently, 2 left unresolved and correctly unrevised. **No open PENDING as of 2026-07-25 close.**

### 2026-08-14 — SCOPE (OTTO-authored, OTTO-executed; recorded here so WINTERKORN inherits the rule) — **do not docket unobservable obligations**

**Finding.** Four rows WINTERKORN inherited from OTTO's s017 close (`2026-08-05` Rule 17 subpoena deadline, `2026-08-07` defense privilege log, plus the 8/14 gov't-exemplar and 8/21 defense-submission steps carried inside that row's notes) were keyed to **party-to-party discovery obligations that structurally cannot produce a docket entry.** All swept **empty** on 2026-08-14 — `[CONF CourtListener docket_id 72046761: ZERO entries 2026-08-01..08-14, latest is Dkt 116 (7/30)]`.

**Why they can never fire usefully.** Rule 17 subpoena applications are routinely **ex parte and/or sealed**, and *serving* a subpoena requires no docket entry at all. Privilege logs are **exchanged between counsel and are never filed**. So the row's "what_to_check" was unanswerable through the only channel OTTO has.

**Executed by OTTO this session (no WINTERKORN action required):** the chain was collapsed into **one row at a modeled `2026-09-04`** keyed to the *first DOCKETED output* — an in camera submission, motion to compel, privilege dispute, or an order resolving one. The `2026-08-05` row is annotated and **deliberately NOT re-armed on a date.**

**STANDING RULE FOR FUTURE RUNS — apply at row-creation time, not at fire time:** before docketing any deadline, ask *"what artifact does this obligation produce, and does it land in a channel WINTERKORN can read?"* If the answer is a private exchange, **key the row to the first observable downstream artifact instead.** This is the same halt-on-ambiguity instinct WINTERKORN already applies to dates, extended from *"is the date right?"* to *"is the EVENT visible?"*. ⚠ **Corollary, and it matters for grading:** on rows of this class, **absence of a docket entry is NOT evidence of absence** — never report one as a negative finding.

### 2026-10-14 — DISCOVERY / SCOPE: First Brands criminal track: trial 2/9/2027, cooperators docket-confirmed (OTTO assesses; WINTERKORN did not act)
- **Case:** US v. Patrick James & Edward James, **1:26-cr-00029** (SDNY, Judge **Analisa Torres**). CourtListener dockets 72203330 / 72203217 / 72203326. `[CONF ECF 59, 5/8/2026: "Trial in this matter is set for February 9, 2027, at 9:00 a.m."]` Speedy Trial time is excluded to 2/9/2027 (ECF 76). The pretrial conference is **2/1/2027 12:00 PM** (ECF 104). ECF 139 (10/6, read at primary) moved only the expert and Daubert dates: Daubert motions are now due 12/22/2026. The 10/5 status conference was adjourned sine die; *"The Court shall issue rulings on the pending motions in due course"* (ECF 136). Pending motions include **Patrick James's 9/4 motion to sever trials** (ECF 108, with "Exhibit 42 - Onset Complaint"). Both dates are now TSV rows. **Neither was on any OTTO surface**: OTTO's files carry only the early-press "trial scheduled June 2026" (ML-OTTO-006).
- **Cooperators, named persons with sourcing given per the 7/25 convention:** **US v. Brumbergs, 1:26-cr-00025** (Torres; dockets 72208928 / 72353885) is the case of **Peter Andrew Brumbergs** (the caption) and **Stephen Graham**. ECF 32 (7/27) reads *"the Court ADJOURNS sine die the sentencing of Mr. Graham currently set for August 3, 2026"* until after the James trial, with a status update due 4/16/2027 `[CONF docket text]`. That he pleaded guilty and is cooperating, under a cooperation agreement dated 2/25 and a plea dated 3/2, rests on press only `[PRESS TT News 2026-03-06]`. That article quotes his allocution: *"I knew that the financial statements issued to First Brands' lenders contained false and misleading information"*, conduct period 2018–2025, and names Point Bonita (Jefferies), Raistone and Evolution. **This is the corroboration OTTO's 7/25 gate asked for** before carrying the two names from the examiner report: Graham's name now comes from a court order, Brumbergs's from a case caption.
- **OTTO decides:** whether this fires the standing outbound trigger *"Cooperating witness reveals new fraud/participants"* (→ CARL, REGINALD via WALTER), or whether it predates the trigger and only needs integrating into THESIS / STATUS.

### 2026-10-14 — DISCOVERY: Tricolor Ch.7: trustee's Rule 2004 examination of BlackRock (OTTO-33 relevance is OTTO's call)
- `[CONF Verita docket titles]` **Dkt 1298** (filed 7/8/2026, Trustee Burns): Rule 2004 motion against **BlackRock, Inc., BlackRock Financial Management, Inc., and the Senior Preferred Members**. The BlackRock entities objected 7/29 (Ropes & Gray; Dkt 1350). On **9/1** the court ruled *"Objection overruled. Motion GRANTED. Parties to confer on topics and upload order."* At the **10/7** status conference the parties were told to keep conferring **until 10/16**, and to file competing forms of order if they do not agree. Transcripts of 9/1 and 10/7 are under the 90-day restriction until 12/9/2026 and 1/11/2027. **No OTTO surface mentions it.** A Rule 2004 examination is discovery, **not** a public implication of fraud. Whether it matters for OTTO-33 (*"a counterparty NOT on OTTO's named list publicly implicated"*) is OTTO's judgment, not mine. TSV row added for 10/16.
- Same window, also on Verita: the trustee's **second emergency motion to extend the vehicle-sales deadline** (Dkt 1455, with an expedited motion 1457) was heard **10/14 at 2:30 PM**; outcome not posted at run time. Vervent objection deadlines 10/21 and 10/23. A Navarro Towing 9019 settlement motion, with objections due 11/2. Holman's Sept auctioneer fee of $280,935, with objections due 10/16. Adversary 26-03102 (Lopez v. Tricolor). All are routine; **none docketed**.

### 2026-10-14 — STATUS-SYNC: 6 tracked-case rows to propagate + 2 priority mismatches
- **Tracked-case hearings added to the TSV (spec STATUS inclusion rule):** 10/16 Tricolor BlackRock 2004 confer deadline · 10/20 First Brands D&O-insurers hearing (Dkt 3669; time UNVERIFIED) · 10/21 First Brands §721 operate hearing 09:00 CT · 10/27 First Brands §341(a) 11:00 CT · 2027-02-01 First Brands criminal pretrial conference · 2027-02-09 First Brands criminal trial. **Optional** (recurring or modeled rows, STATUS's call): the ~11/04 NY Fed window, the ~11/12 EART 2026-5 window and the ~12/07 Manheim release.
- **Priority mismatches between TSV and STATUS (event SET aligned, all 22 old forward rows present in STATUS):** Dec 9 FPTC is 🟠 in the TSV and 🟡 in STATUS. Dec 31 year-end cluster is 🟡 in the TSV and 🟠 in STATUS. Which side moves is OTTO's choice.
- **STATUS content upgrade candidate:** the First Brands row says *"trustee name (Engelhart) snippet-only"*. The name is now docket-confirmed: "Trustee Eva S Engelhart" is the filer of Dkt 3796, 3861, 3873 and 3875 and the 9/29 §341 notice `[CONF CourtListener RECAP descriptions]`.

### 2026-10-14 — SWEEP-FACTS: EART 2026-4 issued (8/17 row; OTTO sweeps with the 10/21 OTTO-07 run)
- `[CONF EDGAR FTS, trust CIK 0002150254]` ABS-15G 8/18 · 424H + FWP 8/19 · FWP 8/26 · 424B5 + closing 8-K 8/28 · first 10-D 9/29. Controls: 2026-3 = 130 hits, 2026-5 = 0. The 10/21 row's line *"EART 2026-4 absent = the first candidate"* no longer applies. I left it in place with a note, because the wording is OTTO's. The Exeter cadence test moves to EART 2026-5 (new row, window 10/20–11/12).

### 2026-10-14 — CALENDAR-AMBIGUITY: two unverified items (rows NOT revised)
- (a) **US v. Chu, unnumbered "Evidentiary Hearing" entry dated 2026-10-13** on CourtListener docket 72046760 (no description in the RECAP index; no press). ECF 171 said the hearing would run 10/7, then 10/8–9 as needed. Whether it ran on 10/13 or something else was entered that day is UNKNOWN. The ~10/21 row is an OTTO check date and stays.
- (b) **First Brands 10/20 hearing time.** Dkt 3800 is the *"Amended Notice of Hearing for October 20, 2026"*; the original 3669 setting was 10:00 AM. Time UNVERIFIED. Remote-testimony notices filed 10/13 show the setting is live.

### 2026-10-14 — SCOPE / SPEC ERRATA (ESCALATION-LOG: applied in my own sections; the spec is OTTO's to fix)
- `WINTERKORN.md` gives the Tricolor Ch.7 judge as **"Judge Burns"** (BASELINE AUDIT recurring-release universe table, L133). **Anne Elizabeth Burns is the Ch.7 trustee; the judge is Michelle V. Larson (N.D. Tex.)** `[CONF Verita docket titles]`. Corrected in STANDING MONITORS here; the spec needs OTTO's edit.
- `WINTERKORN.md` CALIBRATION HINTS still says *"Don't propose bank earnings outside the JPM/5-3/BCS/Regions/MTB/OBK set"*. That conflicts with the 10/14 narrowing to MTB + ALLY, and ALLY is not in that old set. The RETURN template's *"Pruned: [resolved events removed (past + >1wk old)]"* also predates the archive rule. I followed CALIBRATION and the archive rule.
- The spec says CourtListener holds **two** per-defendant dockets for US v. Chu. There are now **three**: 72046760, 72046761 and **72046805**.
- **TSV size:** `CATALYSTS.tsv` is **46,501 B** after this run (32,437 B at start; 9 rows with receipt-length notes). `read_cap_check.py --agent OTTO` does not count it as a boot whole-read (the boot uses `catalyst_countdown.py`), so no rule is breached. WINTERKORN's read-set does read it whole, though. Nine swept rows (9/15–10/07) become archive-eligible between 10/16 and 11/07. If OTTO wants a byte cap or a shorter-notes rule for the TSV, it would go in the spec.

### 2026-10-14 — BASELINE AUDIT delta (propose-only; monthly trigger; window 10/14–11/30)
| # | Date | Event | Suggested priority / who_cares / date_class | Rationale | Status |
|---|---|---|---|---|---|
| 1 | ~2026-11-04 (window 11/04–11/12) | NY Fed Q3-2026 HDC | 🟠 / OTTO,CARL,REGINALD / modeled | Accepted class, no row existed (hint 4) | **ADDED as an accepted class (ESCALATION-LOG, veto by deleting the row)** |
| 2 | 2026-10-23 10:00 AM CT | First Brands: Kingsbridge Holdings administrative-expense application hearing (Dkt 3841) | 🟡 / OTTO,BROCK / confirmed | A dated First Brands hearing, but a single creditor's admin claim, i.e. routine | **Proposed, NOT added** |
| 3 | 2027-06-30 | OTTO-35 resolve date | 🟢→🟠 / OTTO / confirmed | Prediction resolve date absent from the TSV; outside the 150-day horizon until ~2027-01-31 | Proposed for a later run |
| 4 | ~Oct–Nov 2026 | Bridgecrest (BLAST) next deal launch window | 🟠 / OTTO,REGINALD / modeled | ABS-pricing class; not modeled this run (cost note: lowest yield) | Deferred to next run |
- **Excluded per CALIBRATION:** the Fitch Auto ABS Index (DECLINED). Q3 earnings for JPM / 5-3 / BCS / Regions / OBK (DECLINED: 5 events). S&P / KBRA / Moody's monthly surveillance (DEFERRED).
- **Checked, no gap:** Manheim (11/06 in the TSV, verified) · 10-D cycles (4 rows) · MTB / ALLY · Tricolor §341 11/11 · Tricolor criminal 12/4, 12/9, 1/25 · SDT ~11/15 · Carvana Q3 10/28. **Carvana Chancery:** no dated milestone found in a web search (SEARCH-NOT-FOUND, not a negative; OTTO has the direct Chancery access).
- **Filled under job step 2 rather than proposed (per-case full forward expansion, the 7/25 accepted pattern):** the three First Brands Ch.7 hearings, the two First Brands criminal dates, the Tricolor BlackRock deadline, the EART 2026-5 window and the 12/07 Manheim row.

### 2026-10-28 — DISCOVERY: Tricolor Ch.7 BlackRock Rule 2004 resolved by order (OTTO-33 relevance is OTTO's call)
- `[CONF Verita Dkt 1472, signed 10/22, entered 10/23, PDF read]`: the court granted the trustee's motion over BlackRock's positions. BlackRock applies **the Trustee's** responsiveness criteria. A protective-order carve-out is reserved for commercially sensitive information, non-Debtor investments and third-party client information. Disputes are resolved by in camera sampling. The examination topics sit in a protocol sent to Chambers, not on the docket. **No new party named.** This is discovery authorized, **not** a public implication. Whether BlackRock / the Senior Preferred Members count as "outside the named list" for OTTO-33 is OTTO's judgment; the order does not say anyone participated in, financed, or was defrauded by the scheme.

### 2026-10-28 — DISCOVERY: First Brands Ch.7 trustee administration (OTTO / BROCK assess; WINTERKORN did not act)
- **DIP-agent cash sweep:** a proposed stipulation and agreed order (Dkt 3952/3953, filed 10/19 by the Ad Hoc Group with the FBG trustee) would modify the stay so the DIP Agent can *"sweep and apply cash collateral of the FBG Converting Debtors"*. Objections: Evolution + SPV trustee Sommers (Dkt 3988; as quoted in Onset's 3989, it argues the proposed stipulation's ¶2 would be an impermissible non-consensual third-party release of the DIP Agent, the Ad Hoc Group and the DIP Secured Parties) and Onset (Dkt 3989, 10/25). Onset's characterization (an objector's, `[ALLEG]`-grade): the interim trustee *"proposes to turn over nearly all of the FBG Estates' cash to the DIP Agent"*, linked to a *"not-yet-finalized but apparently forthcoming settlement and financing arrangement with the Ad Hoc Group"*. No order seen through Dkt 4003.
- **Fee-allocation fight:** Onset (3975), Aequum (3982) and UMB (3983) object to allocating the final Ch.11 fee applications to SPV estates. Guidepost (the examiner's forensic accountant) final fee application Dkt 3994: fees $1,276,730, expenses $5,521,714 (per the RECAP description).
- **§702 election:** possible at the 10/27 §341 meeting; the outcome is not on the docket as indexed. Next WINTERKORN run checks for a UST election report.
- **11/02 status conference on the McHenry wind-down sale (Dkt 3933; 3934 sealed)** and **11/17 continued §721 hearing**: both docketed as rows.

### 2026-10-28 — DISCOVERY: Tricolor criminal (US v. Chu), report-every-run items
- Charging documents / pleas: **none new** in the indexed docket (ECF 165–187 + minute entries, 9/22–10/26).
- New since 10/14: ECF 178–180 (10/8) is Chu's MIL to exclude the government's proposed expert, **Prof. Christopher Palmer**. ECF 182–183 (10/15) are the government's voir dire and jury instructions. **ECF 184 (10/15)** is the government's MIL, with exhibits *"Amended Petition"*, *"Chu Declaration"* and *"Radford Letter"*; the document was not read, so "Radford" is single-source, a docket-description name only. ECF 177 (10/7) is a letter from the Tricolor Ch.7 trustee on a privilege assertion in response to Chu's Rule 17 subpoena. A SEALED minute entry is dated 10/26.
- Suppression: the hearing closed 10/9 with decision reserved. Letters 185–187 followed. No ruling indexed. **The V3 trigger ("suppression granted in material part") has NOT been observed fired, and has not been observed failing.**

### 2026-10-28 — SCOPE / TOOLING: CourtListener search API now requires auth (ESCALATION-LOG)
- `recap_pull.py search` → HTTP 401 *"Authentication credentials were not provided"* on v4, and 403 on v3. It worked anonymously through 10/25 (`~/.cache/dewey_recap/requests.log`). The workaround applied this run: the **per-docket RSS feed** (`https://www.courtlistener.com/docket/<docket_id>/feed/`) is anonymous and returns the latest 30 entries with full descriptions. RECAP storage PDFs remain public (`storage.courtlistener.com/recap/gov.uscourts.<court>.<pacer_case_id>/…<entry>.0.pdf`; case ids: FB txsb.487046, Chu nysd.654892/654891/654893, James nysd.656996, Tricolor Ch.7 txnb.532333). **Limits:** the feed holds 30 items (about 5–7 days on First Brands), and storage holds only purchased PDFs. A storage miss is never a negative. **DEWEY owns `recap_pull.py`.** Whether to get a `COURTLISTENER_TOKEN` or to add a feed mode is a DEWEY/OTTO call, routed via OTTO. WINTERKORN edits nothing outside docket/.

*(The cleared 2026-07-25 and 2026-06-09 PENDING blocks, dispositions inline → `WINTERKORN_MEMORY_ARCHIVE.md`, moved verbatim 2026-10-14.)*

Future format for new PENDING items:
```
### YYYY-MM-DD — [category: SCOPE / DATE-ESCALATION / STATUS-SYNC / PREDICTIONS-SYNC / CALENDAR-AMBIGUITY]
- [one-line description + source + suggested resolution]
```

---

## STANDING MONITORS

> **Owner-consumed overlay October25 (s039/OTS-06), not a WINTERKORN run:** current evidence supersedes active carry-forward hints below. EART2026-4 closedAugust31, not the8/28 filing date (s037 primary8-K); BLAST2026-4 closedOctober22. First Brands October20 hearing held perclerk3956, substantive disposition missing; October21 hearing continued,dateTBD perclerk3973, nextcheckOctober27. Verita recipe verifiedTLS thenHTTP403 onOctober25; a working recipe is not guaranteed present access. Ally/VRM/shelf/T-7 bounded attempts completed lateOctober25, not at old scheduled dates. Current canonical dates/questions → CATALYSTS/STATUS; old next-nodes/next-run hints below are October14 history. Full WINTERKORN last-run date remainsOctober14; full future-date sweep remains incomplete. No source gap or order outcome closed by this overlay.


Recurring watches WINTERKORN should re-verify every run regardless of pre-fire window. These are the rows where source-of-truth is known to drift / be blocked.

*(Rewritten by OTTO 2026-10-14, s029 — the July text is in `WINTERKORN_MEMORY_ARCHIVE.md` only where it was moved; the lines replaced here were stale facts, not history.)*

> **WINTERKORN 2026-10-28 run, read this first.** Changes to the source recipes: **(1) the CourtListener SEARCH API now 401s anonymously.** Use the per-docket RSS feed `https://www.courtlistener.com/docket/<id>/feed/` (30 newest entries with full text; ids FB 71483359, Chu 72046760/72046761/72046805, James 72203330, Brumbergs 72208928). Use RECAP storage PDFs for the documents themselves; HEAD-probe and positive-control first. **(2) Verita POST works again 10/28** (TLS verify 0 with the G2-augmented bundle). One 403 came on a quick second POST and cleared on retry, so space the calls. **(3) Kroll:** the page loads 200, but `Home-LoadDocketData` returns an empty body, so it is not usable. **Dates as of 10/28:** First Brands §721 + Evolution motions **11/17 1:00 PM CT** · FB status conference (McHenry sale, Dkt 3933) **11/02 1:00 PM CT** · FB §341 **held 10/27** · Tricolor BlackRock 2004 **resolved, Dkt 1472**.

### Per-case dockets
- **Tricolor SDNY criminal (US v. Chu, 1:25-cr-00579, Judge Castel) — now the highest-activity case.** Full DISCOVERY scope (CALIBRATION 7/25 ruling — *not* "trial date + cooperator motions only", which this line wrongly said until 10/14). Dates: suppression ruling pending (ECF 108; ECF 171 set the evidentiary hearing for 10/7, continuing 10/8–9 as needed, with no further briefing expected; an unnumbered "Evidentiary Hearing" entry dated 10/13 is unexplained) · Goodgame sentencing control **2026-12-04** · FPTC **2026-12-09 2pm** · trial **2027-01-25 10am** (Chu only); all re-verified 10/14. Re-verify every run. Sources in order: **CourtListener SEARCH API** (`AGENTS/DEWEY/scripts/recap_pull.py search`, unauthenticated). Search by case number 1:25-cr-00579: CourtListener holds **three** dockets for it, ids 72046760 / 72046761 / **72046805** (the third was seen 10/14), so query `docket_id:(72046760 OR 72046761 OR 72046805)`. Then Inner City Press, then DOJ press / Law360. The docket PAGE and REST API return 403/401. **RECAP `description` is often EMPTY on recent entries** (only `short_description`); an empty description is not a missing entry.
- **Tricolor Ch.7 docket (Verita; Judge Michelle V. Larson, N.D. Tex.; Ch.7 trustee Anne Elizabeth Burns)**. *(This line said "Judge Burns" until 10/14; Burns is the trustee. The spec still says it; escalated.)* **Verita works by POST**: `/document/list/6384`, form fields `DocketNumber`, `StartDate`/`EndDate` (mm/dd/yyyy), `DocumentName` (keywords joined by "or"), `PageSize`=2000, `CurrentPage`=1; parse the `Document Name:` / `Date Filed:` blocks. **TLS (10/14):** this box's system bundle no longer contains the G2 intermediate (curl `ssl_verify_result`=20). Fetch `http://certificates.godaddy.com/repository/gdig2.crt` (DER), convert it with `openssl x509 -inform DER`, `cat` it onto `/etc/ssl/certs/ca-certificates.crt` in the scratchpad, and pass `--cacert` (verify result 0). **Never `-k`.** §341 continued to **2026-11-11 10:00 AM CT**, re-verified 10/14 (the 6/2 notice is still the latest). The trustee projects the Final Report for 9/30/2030 (Dkt 1113). **New thread:** the trustee's Rule 2004 examination of BlackRock / the Senior Preferred Members (Dkt 1298, GRANTED 9/1), with the confer deadline 10/16 as a TSV row. Watch for an agreed order or competing orders.
- **First Brands (S.D. Tex., Judge Christopher M. Lopez, Courtroom 402) — Ch.7 since 2026-09-01 (Dkt 3748); trustee Eva S. Engelhart (docket-confirmed 10/14).** Trustee administration: §341 meetings, trustee reports, sale/settlement motions, adversary proceedings, PSEC Rule 2004. Source: CourtListener SEARCH API, `docket_id:71483359`; the hearing-setting search that worked was `description:"scheduled for 10" OR "set for 11"…`. Kroll 403s since 9/30. **Next nodes:** 10/20 D&O-insurers stay-relief hearing (Dkt 3669/3800; time unverified) · 10/21 09:00 §721 operate hearing (Dkt 3796) · 10/23 10:00 Kingsbridge admin-expense hearing (Dkt 3841; not docketed, routine) · 10/27 11:00 §341(a), reset.
- **First Brands criminal: US v. Patrick James & Edward James, 1:26-cr-00029 (SDNY, Judge Analisa Torres)**, CourtListener dockets 72203330 / 72203217 / 72203326. Trial **2027-02-09 9:00 AM** (ECF 59) · pretrial conference **2027-02-01 12:00 PM** (ECF 104) · Daubert motions 12/22/2026, oppositions 1/15/2027, replies 1/26/2027 (ECF 139) · motion to sever (ECF 108) and other defense motions pending, with rulings "in due course" (ECF 136). **Cooperators' case: US v. Brumbergs, 1:26-cr-00025 (Torres)**, dockets 72208928 / 72353885, covering Peter Andrew Brumbergs and Stephen Graham. Graham's sentencing is adjourned sine die, with a status update due **2027-04-16** (ECF 32). Same DISCOVERY scope as Tricolor.
- **Carvana derivative / discovery (DE Chancery)**: verify production milestone dates from StockTitan / PRNewswire / direct Chancery filings. 10/14: one web search found no dated 2026 milestone (SEARCH-NOT-FOUND; OTTO holds the direct Chancery access).

### Recurring releases (verify forward two)
- **10-D monthly cycle**: SDART + BLAST file on the 15th or the next business day (6 of 6 verified 10/14). EART files 0–2 business days before month-end (4/28, 5/28, 6/30, 7/30, 8/31, 9/29). Rows run through the October collection month (~11/16, ~11/30); keep two cycles ahead, and add the November-month rows (~12/15, ~12/30) when the October ones fire. Panel trust CIKs: EART 1920761 / 1931330 / 1964225 / 2005087; BLAST 1993328 / 2006743; SDART 2004812. The SDART 2022-6 / 2023-1 10-Ds sit under depositor CIK 1383094, so use `panel_10d.py`'s resolver rather than a raw CIK.
- **Manheim UVVI**: the full-month release comes on the **5th business day**. October's is 2026-11-06 (verified on Cox's 10/7 page). November's ~2026-12-07 is a `modeled` row; re-pin it from the 11/6 page, which names the next date. Mid-month previews are not docketed.
- **NY Fed HDC (quarterly)**: the **Q3-2026 row exists** (~11/04, `modeled`, window 11/04–11/12, dated at the window OPEN). The NY Fed posts a **media advisory ~5–7 days ahead** naming the date (10/31 for 11/5/2025; 5/5 for 5/12/2026), so re-pin from it. Probe `HHD_C_Report_2026Q3.xlsx` against the 2026Q2 control: at 10/14 the Q3 file returned 302 and Q2 returned 200. The Q4-2026 row (~Feb 2027) is due for a proposal ~mid-January.
- **S&P / KBRA / Moody's ABS surveillance** — on-event only (DEFERRED class, see CALIBRATION).
- ~~Fitch Auto ABS Index~~ — **DECLINED 2026-10-14** (CALIBRATION).

### Bank earnings (narrowed 2026-10-14)
- **MTB** (OTTO-31) Q3 **2026-10-16** (before the open, call 08:00 ET) and **ALLY** (OTTO-12) Q3 **2026-10-20** (~07:30 ET, call 09:00 ET) only, both verified 10/14 from the issuers' own scheduling releases (9/18, 9/17) via press mirrors; ir.mtb.com returns 403. Sweep by the SEC EDGAR 8-K filing date. Q4 dates are announced ~4 weeks ahead (mid-December), so propose them then. The other named banks are DECLINED (CALIBRATION).

### ABS pricing windows (modeled rows)
- **EART 2026-4**: **ISSUED** (424H + FWP 8/19, FWP 8/26, 424B5 + closing 8-K 8/28, first 10-D 9/29; trust CIK 0002150254). The facts are on the 8/17 row for OTTO's sweep. **EART 2026-5**: `modeled` row ~11/12, dated at the window CLOSE (window 10/20–11/12, from launch intervals of 62–85 days). It had 0 FTS hits at 10/14. EDGAR FTS recipe: `efts.sec.gov/LATEST/search-index?q="Exeter Automobile Receivables Trust 2026-5"` with a UA header (add `&forms=424H,FWP,424B5` for launch dates only), **positive-controlled against the previous deal** before banking a zero.
- **Bridgecrest** — Carvana-related; quarterly. Watch for related-party pricing dynamics.
- **GCAR / smaller stressed shelves (CPS, Flagship, Lendbuzz, SAFCO)** — Watch for shelf-halt signal (OTTO-07).

### TRADE.md position expiries
- ✅ **TRADE.md is FROZEN as of 2026-07-04** (corrected 2026-07-25 — this line previously said "rehab-pending," which was stale by three weeks). OTTO holds **no position**. **Do not add position-expiry rows at all** while frozen — there are no positions to expire. If TRADE.md is ever unfrozen, revert to cross-verifying against FORGE before docketing any expiry.

---

## CALIBRATION

**OTTO-owned section. WINTERKORN reads but never writes here.** OTTO records:
1. **Declined release classes** — what OTTO decided isn't worth tracking under the current thesis lens (with date + reason). WINTERKORN excludes these from baseline-audit proposals.
2. **Accepted-as-proposed examples** — patterns WINTERKORN should keep proposing.
3. **Calibration notes** — anything OTTO wants future-WINTERKORN to know about scope decisions.

### Declined release classes

- **[2026-10-14] Fitch Auto ABS Index (monthly)** — DECLINED. OTTO has no Fitch-direct access, the public mirror decayed (newest piece covers January), and OTTO-04 resolved 7/25 onto the deep-subprime 10-D panel, which OTTO now owns. The 7/15 row was never swept in 91 days and was retired 10/14. Do not propose Fitch rows. If a Fitch figure appears in press, OTTO reads it into STATUS; it is not a docket event.
- **[2026-10-14] Bank earnings other than MTB and ALLY** (JPM / 5-3 / BCS / Regions / OBK) — DECLINED. The class existed for OTTO-30's forward-discovery read, and OTTO-30 resolved FALSIFIED 8/14 (bank-contagion leg disconfirmed). REGINALD owns bank sizing. **Re-propose only if a new bank name surfaces in a Tricolor or First Brands filing.**
- **[2026-06-09] Direct rating-agency monthly surveillance row (S&P + KBRA + Moody's, baseline-audit proposal #3)** — DEFERRED-NOT-DECLINED. Auto Finance News mirror already captures on-event additions (CreditWatch placements, ECNL revisions) and feeds the Lender Watchlist directly. A standalone TSV row for "May data mid-month" was too fuzzy on threshold_signal to be action-forcing. **Re-propose ONLY if** OTTO experiences a specific issuer-level event (Exeter, CPS, Flagship, Lendbuzz, SAFCO) where direct rating-agency tracking would have caught it earlier than Auto Finance News did. Default lens: leave as Auto Finance News mirror.

### Accepted (Jun 9 inaugural baseline-audit deltas, for future-WINTERKORN pattern reference)

- ~~**Fitch Auto ABS Index monthly**~~ — **SUPERSEDED 2026-10-14: class DECLINED (see above). Do not follow the pattern line below.** (proposal #1 + #2) — ACCEPTED with `modeled` date_class (typically mid-month; revise within 7d via Fitch direct). Drives OTTO-04 trajectory; rolling next-2 keeps the burn-rate honest. Pattern: keep proposing monthly Fitch ABS Index rows on rolling next-2 cadence.
- **NY Fed Quarterly HDC** (proposal #4) — ACCEPTED with `modeled` date_class. Canonical aggregate-auto read; missing it would silently drop a quarterly check on the Invisible Exit divergence (consumer-flow vs ABS-stress). Pattern: keep proposing each quarter ~14 days out from expected release (Feb/May/Aug/Nov).
- **Tricolor §341 Nov 11 2026 continuance** (proposal #5) — ACCEPTED with `confirmed` date_class (Verita-noticed). Pattern: when WINTERKORN finds a docket-noticed continuance during pre-fire verification, propose adding the continuance date directly — it's a verified-source-of-truth gain.

### Accepted (Jul 25 run — all 5 added rows ACCEPTED as filed)

- **Jul 24 FB status conference / Jul 27 ballot certification / Jul 29 CVNA Q2 / Aug 17 EART 2026-4 (`modeled`) / Dec 9 Tricolor FPTC** — all five accepted, none revised. Two patterns to keep repeating: **(a) promoting a sub-deadline out of another row's notes into its own row** (Jul 27 ballot cert was buried in the Jul 20 row and is the node where the vote tallies actually become public); **(b) positive-controlling a zero before banking it** — the EART 2026-4 "0 EDGAR hits" was checked against 2026-2 (98 hits) and 2026-3 (35 hits) first. That is exactly right and should be the standing habit for every negative.

### ⚠ SCOPE CHANGE — criminal track is a DISCOVERY channel, not a date-keeping row (OTTO ruling, 2026-07-25)

**This is the most important calibration entry to date. Read it before any run.**

The spec scoped the Tricolor SDNY criminal case as *"Selective scope: trial date Oct 19 2026 + cooperator motions only… re-verify monthly until ~T-30, then weekly."* Under that scoping, **four material events were missed for up to a month**, and OTTO missed them too:

| Date | Event | Why the narrow scope missed it |
|---|---|---|
| Jun 24 | **Superseding 8-count indictment** vs Chu invoking §225 "financial kingpin" (10yr-life min) | Not a trial date, not a cooperator motion |
| Jun 24 | **COO Goodgame pleads GUILTY + cooperates** (flip from Jan not-guilty) | Arguably in scope, but framed as "motions," not pleas |
| Jun 30 | Chu arraigned, pleads not guilty | Not a trial date |
| Jul 7 | Trial adjourned Oct 19 → **Jan 25 2027** | ✅ *This* one was in scope and you caught it |

The narrow scope caught **1 of 4** — and the three it missed included **the strongest thesis validation OTTO has ever received**: the indictment charges *"manipulated delinquent loan data to make non-performing loans appear current"* (OTTO's Invisible Exit) **and** *"pledged the same collateral to multiple lenders simultaneously"* (OTTO's Cockroach). OTTO had been treating both as its own inferences.

**Ruling — the criminal docket is re-scoped from date-keeping to full fraud-surface discovery.** Every run, report:
1. **Charging documents** — new/superseding indictments, statutes invoked, count changes. *Statute choice is signal*: a dormant mandatory-minimum statute is a revealed read on evidence strength.
2. **Pleas and cooperation** — any defendant flipping. Cooperators expand named participants; this fires an OTTO standing outbound trigger (→ CARL, REGINALD).
3. **Newly named entities or individuals** — flag them, and **flag them as single-source if that's what they are** (see the examiner-names disposition above).
4. **Alleged-conduct language**, quoted. The specific phrasing is what maps to OTTO's mechanisms; a summary ("fraud charges") destroys exactly the information OTTO needs.
5. **Scope-of-period allegations** — "continuing enterprise from at least 2018" widened OTTO's impaired-vintage window by four years in one clause.

Same re-scoping applies to the **First Brands criminal track (US v. Patrick James)** and to **examiner/trustee reports in both cases** — the Apr 27 examiner interim report sat unintegrated for three months under the old scoping.

**Cost note:** this is a real scope expansion. Prefer it done *well on the two live criminal matters* over thinly across everything; if it forces a trade-off, drop ABS-pricing-window verification first (lowest yield to date).

### ⚠ RULING — Fitch Auto ABS Index: OTTO has NO Fitch-direct access; row stays `modeled`, and the gap is now a named thesis risk (OTTO, 2026-07-25)

> **SUPERSEDED 2026-10-14:** the class is now DECLINED (Declined release classes, above). Ruling 1 ("the row stays `modeled` indefinitely") no longer applies: there is no row. Kept as the record of why.

You escalated this after two consecutive runs of unverifiable Fitch rows. **Answer: OTTO does not have Fitch-direct access either.** OTTO's Fitch figures have always come through the Auto Remarketing / Auto Finance News secondary mirror, and that mirror has gone stale — its newest indexed piece (2026-05-21) still covers the **January** index.

**Rulings:**
1. **The row stays `modeled` indefinitely.** Do not flip it to `confirmed` on a cadence assumption. Keep verifying; keep halting when it can't be verified. Two halts in a row was the correct behaviour, not a failure.
2. **Report the *absence* explicitly each run** — "fired, no new data" is a finding, not a null result. OTTO swept the Jul 15 row that way. **Never let a missing print read as an unchanged series**; the risk is inferring stability from silence.
3. **Your cadence confirmation is now the canonical statement of the lag** (index month = collection month + 1, release lagging further). That upgraded an assumption to a sourced mechanism — keep it in STANDING MONITORS.

**Why this matters beyond docket hygiene, so the next run understands the stakes:** the Fitch blended index is the **resolution metric for OTTO-04** (2022-vintage CNL >25% by Sep 30) and the primary instrument for the summer-re-deterioration watch. Latest available data is **March 2026** — meaning OTTO enters the Sep 30 resolve with an input that is **four months stale by data-month** and a re-deterioration thesis that is **unobserved, not disconfirmed**. This is a structural single-source dependency on a paywalled series reached through a decaying free mirror. **Flagged to OTTO's own follow-up queue** as a measure-design problem of the same family as OTTO-30 (see CHANGELOG 2026-07-25) — the thesis leans on a number OTTO cannot reliably obtain.

### 📋 TESTED 2026-07-25 — free-source alternatives to Fitch: S&P DEAD, KBRA PARTIAL (do not re-run these checks)

Will asked whether the Fitch gap could be closed from another source. All candidates tested the same day; **record kept so nobody re-litigates it.**

| Source | Verdict | Detail |
|---|---|---|
| **S&P Global — U.S. Auto Loan ABS Tracker** | ❌ **DEAD** | Monthly, published through May-2026, but the article URL returns **HTTP 403 Forbidden**. Authentication required. |
| **KBRA — U.S. Auto Loan ABS Indices spreadsheet** | ❌ **PAID** | The `/indices` hub links a full data spreadsheet (maintained — stamped 15 Jul 2026), but it returns a gate: *"This report requires an ABS Premium Subscription"* (`userHasABSAccess: false`). |
| **KBRA — monthly publication free preview** | ⚠️ **PARTIAL — genuinely useful** | Free text carries **MoM changes in bps**, **separated prime vs non-prime**, at a **~2.5-week lag** (May-2026 data published Jun 17). Absolute levels appear only occasionally (Jan-2026 non-prime ANL **10.9%**). |
| **Fitch via Auto Remarketing / AFN mirror** | ❌ **DECAYED** | Newest indexed piece 2026-05-21, still covering the *January* index. |

**Two things KBRA gives that Fitch never did:** it is **~2 months fresher** (May vs March data), and it is **tier-separated** — prime and non-prime as distinct indices, rather than the single blend whose composition bias broke OTTO-04.

**Use it as a directional supplement, with two hard rules:**
1. **NEVER splice KBRA's non-prime index onto Fitch's subprime index.** Differently constructed universes. Splicing them is precisely the composition error that broke OTTO-04 — a level shift would read as a market move.
2. **Chained levels are fragile.** An anchor (Jan-2026 non-prime ANL 10.9%) plus MoM deltas reconstructs a series, but error accumulates, deltas may be quoted against revised bases, and the **April-2026 report did not surface** — so the chain already has a hole. Report chained values as `[EST]`, never `[CONF]`, and re-anchor whenever a free preview happens to state a level.

**Conclusion: the paid aggregators are closed, so the fix is to own the instrument.** Build the 10-D panel — same underlying data the agencies use, free, primary-source, tier-separable by construction. Scoped in MEMORY § NEXT SESSION.

### Calibration notes

- **Inaugural calibration (Jun 9 2026):** 5 baseline-audit proposals → 4 accepted, 1 deferred-not-declined. WINTERKORN's instinct on per-case docket vs recurring-release scope was sound. The one defer was on a class where OTTO already has a working mirror (Auto Finance News for rating-agency surveillance); reflects "don't duplicate an existing pipeline" lens.
- **Date-classification pattern:** NY Fed HDC and 10-D cycle rows go in as `modeled` (Fitch rows: class declined 2026-10-14) (release dates approximate); a docket-noticed continuance like Tricolor Nov 11 goes in as `confirmed` (court-issued). Use this split going forward.
- **Carvana ambiguity is a true PENDING, not a defer.** WINTERKORN's halt-on-ambiguity on the Jun 12 Carvana row was correct — OTTO has direct Chancery access for Carvana derivative track that WINTERKORN doesn't. Don't propose changing the row class unless OTTO updates the calibration.

---

## NEXT RUN HINTS

> **October25 owner correction:** use the current overlay above and CATALYSTS for action; dated October14 hints below are retained as historical run output. No new WINTERKORN run or cadence satisfaction is claimed.

Notes from the most recent run for the next-WINTERKORN to read first. Captures one-off context that doesn't fit in STANDING MONITORS but matters for the next sync.

*(The 2026-07-25 hints → `WINTERKORN_MEMORY_ARCHIVE.md`, superseded 2026-10-14.)*

### Hints for the next run (written by WINTERKORN 2026-10-28, end of run)

1. **Cadence:** due at the first OTTO session on or after **11/04**. A **T-3 run before the 11/17 First Brands hearing** (~11/12–11/14) is also due if OTTO is in session then. If OTTO stays dark past 11/10, the 11/02, 11/04 and 11/06 rows will have fired: sweep facts first.
2. **First run of November = monthly BASELINE AUDIT** (window November–December). Carry the deferred Bridgecrest next-deal window (10/14 audit row #4). Propose the MTB/ALLY Q4 dates only once the issuers announce (~mid-December).
3. **Sweep targets:** an order on FB Dkt 3669 (D&O insurers; transcript 3990 restricted to 1/25/2027) · the outcome of the 11/02 McHenry-sale status conference (Dkt 3933) · any UST §702 election report from the 10/27 §341 · an order on the DIP cash-sweep stipulation (3952/3953) · **the Chu suppression ruling** (RSS feeds of all three Chu docket ids; also read what the 10/26 SEALED minute entry becomes if unsealed) · Tricolor post-1472 BlackRock protective-order motion or in camera dispute (Verita, search `BlackRock or 2004`).
4. **Pre-fire next time:** 11/11 Tricolor §341 (Verita `DocumentName=meeting`) · 11/12 EART 2026-5 window (EDGAR FTS, positive-controlled against 2026-4) · ~11/15 SDT and ~11/16 SDART/BLAST · 11/17 FB hearing (look for a further continuance notice by Sommers's counsel, Jones Murray, as with 3997).
5. **Re-pin:** NY Fed Q3 HDC from the media advisory (probe `newsevents/mediaadvisory/2026/MMDD-2026` in the 10/29–11/06 range; the Q3 xlsx was still 302 on 10/28) · Manheim 12/07 from Cox's 11/06 release page (the category URL used before now 404s; search for the November release text).
6. **Archive step:** the 10/16–10/28 rows become eligible from 11/15 to 11/27. **Only rows with an outcome word go.** Tonight's rows marked ACKNOWLEDGED-PENDING (10/20 D&O, 10/21 Chu) have NO outcome and must NOT be archived. FIRED-with-outcome rows (10/16, 10/21 §721, 10/27, 10/28 CVNA) are eligible once OTTO has swept them. Word-match, never substring.
7. **Do NOT re-run:** `recap_pull.py search` anonymously (401; DEWEY decides on a token) · the Kroll data endpoint · the Carvana Chancery web search · the Cox mid-month PDF hunt for a next-release date (it carries none).

### Hints written by WINTERKORN 2026-10-14, end of run (consumed by the 10/28 run; kept as history)

1. **Cadence:** the next run is due at the first OTTO session on or after **10/21** (7 days). If OTTO is in session on 10/17–10/19, a **T-3 run** is also due before the 10/20 and 10/21 First Brands hearings (spec cadence). If OTTO stays dark past 10/27, the 10/15–10/27 window will hold ~17 fired rows: sweep facts first, then add rows.
2. **Pre-fire sweep targets next time:** the First Brands 10/20 hearing TIME (look for an agenda or witness and exhibit list notice on docket 71483359) · whether the 10/21 §721 hearing went forward · the 10/27 §341, held or reset · the Chu suppression ruling (query all three docket ids, and resolve the 10/13 "Evidentiary Hearing" entry) · the Tricolor BlackRock agreed order or competing orders after 10/16 · the result of the 10/14 Tricolor vehicle-sales-deadline hearing.
3. **Archive step:** rows dated 9/15, 9/18, 9/20, 9/30, the four 10/01 rows and 10/07 become eligible over 10/16–11/07. All carry explicit outcomes (RETIRED / SWEPT / RESOLVED). Run the word-match, never the substring (UNSWEPT ≠ SWEPT).
4. **Rolling next-two to add when their predecessors fire:** 10-D November-month rows (~12/15 SDART/BLAST; ~12/30 EART, which is also OTTO-34's Dec-2026 resolving filing; confirm with OTTO which filing counts) · NY Fed Q4-2026 (~Feb 2027 window) in mid-January · MTB/ALLY Q4 when the issuers announce (~mid-December) · OTTO-35 resolve (2027-06-30) once it enters the 150-day horizon (~2027-01-31).
5. **Baseline audit:** the next monthly trigger is the first run of November (audit window November–December). Bridgecrest's next-deal window was deferred this run (PENDING audit row #4).
6. **Re-pin from announcements:** NY Fed's media advisory for the ~11/04 window; Cox's 11/6 page for the 12/07 Manheim date; an EART 2026-5 424H (if it lands, the 11/12 row becomes a sweep).
7. **Do NOT re-run:** the Carvana Chancery web search (no milestone found 10/14; OTTO has direct access) or the NY Fed Q4-2025 date hunt (the window needs no more than three anchors).

*(OTTO's 10/14 hints, consumed by the 10/14 run → `WINTERKORN_MEMORY_ARCHIVE.md`.)*

### Standing context (durable)

- **Pre-fire date verification is the load-bearing job step.** OTTO's Jun-8 catch (First Brands Jun-17 → Jun-12) is the canonical failure mode this sub-agent exists to prevent.
- **Verita works by POST** (`/document/list/6384`, Go Daddy G2 intermediate). Halt-on-ambiguity only if that and the secondary mirrors both fail.
- **The Tricolor SDNY criminal case is the highest-activity case** (First Brands is in Ch.7 trustee administration since 9/1).
- **TRADE.md is FROZEN (2026-07-04), OTTO holds no position.** Skip position-expiry additions entirely.
- **Spawn cadence:** every OTTO session with ≥7 days since your last run, plus T-3 before a tracked hearing (spec CALIBRATION HINTS, re-written 10/14).
