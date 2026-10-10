# Colorado River — Lower Basin implementing / parallel agreements: dated search attempt

**Written:** 2026-10-10 12:27 EDT (`date`), by a research worker spawned by AEOLUS. **All reads 2026-10-10, 16:15Z–16:28Z (12:15–12:28 EDT)** unless a row says otherwise.
**Scope:** search record only. Nothing here scores a channel, fires a trigger, or grades the C6 milestone band. That is AEOLUS's job.
**Tiers:** **PRIMARY** = the issuing body's own document (agency, court docket, statute). **SECONDARY** = news or advocacy write-up, used for leads.
**How absences are stated:** "searched X on 10/10; not found" means not found in what was read. It never means "not executed".

---

## 0. Answer in one table

| Question | Finding | Tier | Source (read 10/10) |
|---|---|---|---|
| LB implementing agreement executed? | **No execution found in any primary searched.** Primaries dated 8/21, 9/3, 9/10 and 9/17 describe it as **still to be finalized**. Secondary reporting from 10/1–10/2 says it is **unsigned**: language is being finished, it goes to member-agency boards "over the next few weeks", and then needs Arizona Legislature approval. MWD has an info item, "Implementation Agreements for the 2027-2028 … Guidelines", set for **10/27** | PRIMARY (absence + "to finalize" statements) / SECONDARY (status 10/1–10/2) | §2 |
| Upper Basin drought-operations agreement (§5.2 parallel agreement) executed? | **Not found.** The UCRC's own site could not be reached (TLS error). Secondary 9/14 reports only a UCRC letter about the *existing* DROA releases | SECONDARY / absence | §2.6 |
| 2027 operating condition | **CY2027 Lower Basin shortage under §5.3.A: 1.25 maf reduction**, announced 8/21. Restated 9/15: *"a shortage condition consistent with Section 5.3.A will govern the operation of Lake Mead for calendar year (CY) 2027."* **No primary read states which state split applies** (§5.3.A.2 agreement split vs §5.3.A.3 "Secretary shall determine"). The 2027 AOP is "currently in development" | PRIMARY | §3 |
| Litigation vs ROD | **State of Nevada et al. v. Burgum et al.**, **D. Nev. No. 2:26-cv-02665-GMN-NJK** (Judge Gloria M. Navarro). Complaint filed **08/24/2026** (ECF 1). Seeks vacatur of the ROD, Final EIS and 2027-28 Guidelines, and an injunction. RECAP shows entries through **ECF 14 (09/16/2026)** only. No other ROD challenge was found. CAP (9/3) and MWD (closed sessions 9/9 and 10/5) have *authorized or considered* litigation; nothing filed was found | PRIMARY | §4 |
| October 24-Month Study | **Not published** as of 16:25Z 10/10. UC `24Month_10_6.pdf` and `_10_7.pdf` return **404**. `24Month_10.pdf` is the **Oct 2025** study. LC `24mo_6/_7.pdf` = **Sept 15, 2026** study. LC `24mo.pdf` = **July 15, 2026** study (stale). **No Oct/Nov/Dec Mead projections to report** | PRIMARY | §5 |

---

## 1. What §5.9 says the "implementing and parallel agreements" are (PRIMARY)

Source: `https://www.usbr.gov/ColoradoRiverBasin/post2026/decision-doc/2027-2028OperatingGuidelines_Final.pdf`. HTTP 200 on the 2nd attempt (the 1st, at 16:15:47Z, was reset by the peer). 1,008,363 B, sha256 `298883f1…0c90a63`. Text extracted with pdfminer.

**§5.9 in one sentence:** the Guidelines rely on implementing and parallel agreements, federal and non-federal, "anticipated to be executed within a sufficient timeframe". Named are **(a) a Lower Basin implementing agreement**, which governs *"portions of Sections 5.3 and 5.4"*, and **(b) "an agreement concerning drought operations at [the CRSP Upper Initial Units]"** under §5.2. The absence of either *"shall not impair, delay, or otherwise limit the Secretary's authority to act."*

Verbatim anchors:
- §5.9: *"the Secretary acknowledges that portions of Sections 5.3 and 5.4, as described, will be implemented only when a Lower Basin implementing agreement takes effect as well as the drought operations at the CRSP Upper Initial Units pursuant to the process outlined in an agreement concerning drought operations at these facilities and as referenced in Section 5.2."*
- §3: *"shall become effective upon (1) execution by the Secretary and (2) execution of the necessary implementing and parallel agreements … Absent such … the Secretary will proceed as described in Sections 5.2, 5.3, and 5.4"* (confirms KB-AEO-185).
- §5.2: *"The provisions of this section assume that the Upper Division States reach agreement. If such agreement is not reached by that date, the Secretary will conduct drought operations … consistent with existing authorities."* ("that date" has no antecedent in the extracted text.)
- §5.3.A.2: AZ 760,000 / CA 440,000 / NV 50,000 af reductions *"in accordance with a Lower Basin implementing agreement(s)"*. §5.3.A.3: *"If the Lower Division States have not fully executed … the Secretary shall determine the quantities and apportionment thereof."*
- §5.3.B: the 700 kaf system conservation is *"in accordance with a Lower Basin implementing agreement(s)"*, with a fallback.
- §5.4 (ICS): *"assume[s] that the Lower Division States reach agreement. If such agreement is not reached … no new ICS may be created after December 31, 2026."*
- §2 lists the tools these agreements would carry: *"Lower Basin shortage sharing, forbearance, conservation efforts, releases of additional water from the [CRSP] Upper Initial Units."*

⚠️ **Incidental observation, not adjudicated:** Guidelines **§5.3.A.4** sets the Mead consultation trigger at **1,010 ft**: *"Should the Most Probable projection of any 24-Month Study show Lake Mead falling below 1,010 feet at any time in the subsequent 12-month period, the Secretary shall consult and coordinate"*. KB-AEO-086 records the **ROD's** trigger (Op. Principle 2 / §10.7) as **1,000 ft**. So the two instruments carry different numbers for a consultation trigger. This is flagged for AEOLUS and not graded here.

---

## 2. Execution status — what each source says

### 2.1 Arizona (ADWR / CAP / Legislature)
| Date of item | Item | Tier | URL | HTTP |
|---|---|---|---|---|
| 2026-08-21 | ADWR Director Buschatzke statement: *"We will continue to work with our partners in Arizona, the Lower Basin and Interior, **to finalize the agreements necessary to implement the Lower Basin Plan**."* | PRIMARY (ADWR's official news blog) | https://azwaternews.com/2026/08/21/2026rod_opguidelines/ | 200 |
| 2026-07-31 | ADWR: *"ADWR will continue to work to complete the agreements necessary to implement the Lower Basin Proposal"* | PRIMARY | https://azwaternews.com/ (front page) | 200 |
| ADWR blog front page | Latest posts 9/17 (Kyl), 9/2 (AWPF grants), 8/21 (ROD). **No post on agreement execution through 10/10** | PRIMARY absence | https://azwaternews.com/ | 200 |
| 2026-08-21 | CAP: the Guidelines *"contemplate the execution and incorporation of a Lower Basin states agreement"*; *"CAP supports the finalization and implementation of a Lower Basin proposal"* | PRIMARY (CAP's Know Your Water News) | https://knowyourwaternews.com/record-of-decision-and-operating-guidelines-underscore-need-for-3-state-deal/ | 200 |
| 2026-09-03 | CAWCD Board: *"CAWCD encourages the Lower Basin States to **finalize and execute** a Lower Basin agreement"*. GM Burman: *"Our top priority is finalizing a three-state Lower Basin deal."* | PRIMARY | https://knowyourwaternews.com/cap-prioritizes-three-state-agreement-and-ability-to-defend-its-rights/ | 200 |
| 2026-10-01 | CAWCD Board Oct 1 summary covers an energy agreement, the CAP award and a recovery study. **No Lower Basin agreement action** | PRIMARY absence | https://knowyourwaternews.com/cawcd-board-convenes-for-october-meeting-presents-cap-award-for-water-research/ | 200 |
| statute | **A.R.S. §45-106:** *"An agreement entered into between the director and the United States or a state or government involving a sovereign right or claim of this state is not effective unless approved by the legislature by concurrent resolution."* | PRIMARY | https://www.azleg.gov/ars/45/00106.htm | 200 |
| 10/10 | AZ Legislature session API: the latest session is **"2026 – 57th Legislature – Second Regular Session"**. **No 57th-Legislature special session is listed.** The API does list past special sessions, e.g. 2021 1S | PRIMARY absence | https://apps.azleg.gov/api/Session/ | 200 |
| — | azwater.gov news pages, and the ARC Meeting #14 deck (8/24) whose agenda per search lists "AZ legislative authorization of the Lower Basin agreement" | — | https://www.azwater.gov/news ; …/2026-08/2026.08.24_ARC_Meeting_FINAL.pdf | **403** (not read) |
| — | cap-az.com guessed paths `/news/` and `/board-of-directors/board-meetings/`. CivicClerk agenda link returned a 1.3 KB JS stub | — | cap-az.com ; capaz.portal.civicclerk.com/event/556/files/agenda/10243 | 404 / stub (not read) |

### 2.2 California (MWD / IID / CRB)
| Date of item | Item | Tier | URL | HTTP |
|---|---|---|---|---|
| set 9/10–9/11, meeting **2026-10-27** | MWD Subcommittee on Imported Water, item 3a (matter **21-5019**, "Oral Presentation Only"): **"Information on Implementation Agreements for the 2027-2028 Colorado River Operating Guidelines."** No attachments. No board approval item for a Lower Basin agreement on the **10/13** Board agenda | PRIMARY | https://webapi.legistar.com/v1/mwdh2o/events/1955/eventitems ; matter https://webapi.legistar.com/v1/mwdh2o/matters/7114 | 200 |
| 8/25, 9/9, 9/22, 10/5 (added) | MWD closed-session items: *"Update on Colorado River negotiations and protection of Metropolitan's Colorado River water rights [Conference with legal counsel—anticipated litigation—**deciding whether to initiate litigation**; 1 or more potential cases]"* (One Water 10/12, added 10/5). Also 8/25 "Report on Development of Post-2026 Guidelines" and 9/22 "Colorado River Communications" | PRIMARY | Legistar events 1923/1939/1941/1953 eventitems (same API) | 200 |
| 10/8–10/9 | MWD GM Report (Sept) and General Counsel Monthly Report (Sept), 10/13 board items 5C/5D. **Neither mentions a Lower Basin agreement or ROD litigation.** The GC report lists only Colorado River outside-counsel contract lines | PRIMARY absence | https://d1q0afiq12ywwq.cloudfront.net/media/kfsid1b3/10132026-bod-5c-report.pdf ; …/md1n3za0/10132026-bod-5d-report.pdf | 200 |
| — | IID news room / home | — | https://www.iid.com/news-room ; https://www.iid.com/ | **403** (not read) |
| — | Colorado River Board of California | — | https://crb.ca.gov/ ; /meetings (curl and WebFetch) | **403** (not read) |

### 2.3 Nevada (SNWA / CRC Nevada)
| Date of item | Item | Tier | URL | HTTP |
|---|---|---|---|---|
| 2026-09-17 | SNWA Board agenda: *"Ratify the Authority's filing of a federal complaint against the U.S. Department of the Interior challenging the Final [EIS] and [ROD]…"*. **No Lower Basin implementing agreement item** | PRIMARY | https://www.snwa.com/universal/agenda/getfile.cfml?id=6592&lang=en | 200 |
| 2026-08-20 (minutes) | SNWA ratified a **System Conservation Implementation Agreement with Reclamation, "executed on August 11, 2026"**: up to 50,000 af of system conservation for $16,250,000. ⚠️ **This is a bilateral system-conservation agreement, NOT the three-state "Lower Basin implementing agreement" of §5.3.A.2. Do not conflate the two.** Entsminger: the Authority *"continued to work with the other Basin States to reach an agreement that would not require litigation"* | PRIMARY | https://www.snwa.com/universal/agenda/getfile.cfml?id=6612&lang=en | 200 |
| listing 10/10 | SNWA agendas list meetings through **09/17/2026**. No October agenda posted yet | PRIMARY absence | https://www.snwa.com/apps/snwa-agendas/index.cfml | 200 |
| 2026-09-10 (posted) | CRC Nevada 9/17 agenda, item D: ratification of the 8/24 complaint. **No Lower Basin agreement item** | PRIMARY | https://www.crc.nv.gov/siteassets/documents/20260917_crcnv-notice-and-agenda-of-public-meeting..pdf | 200 |
| page updated 10/06 | CRC Nevada **Oct 13, 2026 Commission Meeting: "Cancelled — There will be no Commission meeting held for October 2026."** | PRIMARY | https://www.crc.nv.gov/meetings/october-13-2026/ | 200 |
| — | snwa.com `/news/`, `/about/news-releases/index.html` | — | — | 404 (not read) |

### 2.4 Federal (USBR / Interior / Federal Register)
| Item | Finding | Tier | URL | HTTP |
|---|---|---|---|---|
| USBR news release 5392 (For Release **Aug 21, 2026**) | *"If the Lower Basin States implement their proposed sharing agreement, the reduction per State would be: Arizona 760,000 / California 440,000 / Nevada 50,000"*. *"For Lake Mead, water deliveries to the Lower Basin States will be reduced by 1.25 million-acre feet for calendar year 2027."* | PRIMARY | https://www.usbr.gov/newsroom/news-release/5392 | 200 |
| USBR decision-doc page (10/10) | Still reads *"…will be implemented by October 1, 2026"*. Documents posted: Guidelines, Factsheet, BO, ROD. **No executed agreement posted** | PRIMARY absence | https://www.usbr.gov/ColoradoRiverBasin/post2026/decision-doc/ | 200 |
| USBR Post-2026 index (10/10) | No agreement-execution item | PRIMARY absence | https://www.usbr.gov/ColoradoRiverBasin/post2026/index.html | 200 |
| USBR newsroom releases 5393–5460 | **NOT READ.** Every request was reset by the peer (curl 56) on a sequential probe at 16:22–16:23Z, almost certainly rate-limiting caused by my burst. The newsroom landing page is a JS app with no listing in raw HTML | — | https://www.usbr.gov/newsroom/news-release/NNNN | 000 |
| USBR LC region page | No agreement item | PRIMARY absence | https://www.usbr.gov/lc/ | 200 |
| DOI press releases page 1 | Items dated 10/02, 9/22, 9/21, 8/30, 8/27, 8/21… Only Colorado River item is **8/21** (ROD). Nothing on agreement execution | PRIMARY absence | https://www.doi.gov/news | 200 |
| Federal Register API, Reclamation, pub ≥ 2026-07-01 | **2 docs, both July (GCDAMP notices). Zero Reclamation documents published 8/01–10/10**: no ROD notice, no agreement notice | PRIMARY absence | `federalregister.gov/api/v1/documents.json?conditions[agencies][]=reclamation-bureau&conditions[publication_date][gte]=2026-07-01` | 200 |
| FR API term "Colorado River", pub ≥ 2026-08-15 | 4 docs, none on Colorado River operations | PRIMARY absence | `…documents.json?conditions[term]="Colorado River"&…gte=2026-08-15` | 200 |
| FR public inspection (pub dates 10/13–10/14) | 108 docs; **none from Reclamation or titled Colorado River** | PRIMARY absence | https://www.federalregister.gov/api/v1/public-inspection-documents/current.json | 200 |
| 2027 Draft AOP, "First Consultation" | Dated **June 25, 2026**. Pre-ROD, based on the 2026 AOP and the June 24MS. **Silent on the agreements.** Still the only 2027 AOP posted | PRIMARY | https://www.usbr.gov/uc/water/rsvrs/ops/aop/AOP27_draft.pdf (via https://www.usbr.gov/ColoradoRiverBasin/aop/index.html) | 200 |

### 2.5 Secondary leads (status, unconfirmed at a primary)
| Date | Outlet | Claim | URL |
|---|---|---|---|
| 2026-10-01 / 10-02 | KJZZ / Mountain West News Bureau (via UPR) | Three-state deal **not yet signed**. Buschatzke: *"I'm very optimistic … that we're going to close on the agreement language in a way that it will be then ready to go to various boards over the next few weeks."* AZ and NV *"have plans in place"*, while California is "working out final details" (MWD, IID). The deal *"must be signed by"* **Jan 1, 2027**. It also needs Arizona Legislature approval, possibly in a special session. The Nevada suit *"did take some time"* to work through. Entsminger memo to the federal government: Nevada is *"committed to working cooperatively towards finalizing and implementing the Lower Basin agreement"* (memo not found). ⚠️ The article also says the rules *"officially go into effect"* Oct 1. That conflicts with Guidelines §3's execution condition, and is reporter framing | https://www.kjzz.org/politics/2026-10-01/new-colorado-river-rules-start-today-but-questions-linger-about-arizona-water-cutbacks ; https://www.upr.org/politics/2026-10-02/colorado-river-rules-arizona-cuts-california-nevada-deal |
| 2026-10-09 | western-water.com | *"A proposed agreement would divide those reductions…"*; *"The state-by-state division remains tied to implementation of the Lower Basin states' proposed sharing agreement."* | https://www.western-water.com/2026/10/09/colorado-river-cuts-how-the-lower-basin-states-are-preparing/ |
| 2026-09-05 | KJZZ (search snippet, not fetched) | Hobbs intends to convene a special session for the deal but **has not formally called one**. GOP House leaders asked ADWR for weekly briefings | https://www.kjzz.org/politics/2026-09-05/arizona-republican-lawmakers-request-more-frequent-briefings-on-colorado-river |
| 2026-08-24 | KJZZ | Quotes A.R.S. §45-106. Arizona is the only basin state where the legislature approves | https://www.kjzz.org/politics/2026-08-24/a-new-colorado-river-plan-is-heading-for-arizona-lawmakers-do-they-have-the-power-to-change-it |
| undated | 8newsnow "Basin states set to sign new 2-year Colorado River agreement, SNWA says" | **Not read**: 403 on curl and WebFetch. Date unknown; it may predate the ROD | https://www.8newsnow.com/investigators/basin-states-set-to-sign-new-2-year-colorado-river-agreement-snwa-says/ |

### 2.6 Upper Basin drought-operations agreement (§5.2)
- Upper Colorado River Commission site: **not reachable**. curl failed TLS verification ("no alternative certificate subject name matches") on both `www.ucrcommission.com` and `ucrcommission.com`. **TLS verification was not bypassed.**
- SECONDARY, Cowboy State Daily, 2026-09-14: UCRC voted to send Burgum a letter saying the **existing** DROA (2019) releases from Flaming Gorge *"appear to have been effective"*. Recovery is *"a priority when hydrologic conditions improve"*; releases are expected to total about 1 maf through early April. **No mention of a new 2027-28 drought-operations agreement being executed.** https://cowboystatedaily.com/2026/09/14/lake-powell-crisis-averted-wyoming-wants-water-taken-from-flaming-gorge-replaced/
- The Sept 15 24MS (PRIMARY) models *"a 1.00 maf Drought Response Operations release"* under the **2026** DROA plan. It does not cite a new §5.2 agreement.

---

## 3. The 2027 operating condition (PRIMARY)

- **8/21 (USBR 5392):** the August 24MS *"determin[es] the 2027 operations based on the new guidelines"*. Powell begins WY2027 in the *"Lower Elevation Infrastructure Protection Range"*, with a 6.0–7.0 maf release to be set in April. **Mead: a 1.25 maf Lower Basin reduction for CY2027.**
- **9/15 (September 24MS, both `24mo_6.pdf` and `24mo_7.pdf`):** *"The operation of Lake Powell and Lake Mead in the September 2026 24-Month Study for operating year 2027 is pursuant to the … 2027-2028 Operating Guidelines"*. *"In accordance with the 2027-2028 Operating Guidelines, a shortage condition consistent with Section 5.3.A will govern the operation of Lake Mead for calendar year (CY) 2027."* *"The 2027 operational determinations … will be documented in the 2027 Annual Operating Plan (AOP) which is currently in development."* Mead CY2027 is also governed by *"Section III of IBWC Minute No. 334"*.
- **Neither document says the Guidelines are "effective" in the §3 sense, and neither invokes §5.3.A.3.** The 24MS cites §5.3.A generically. The strings "implementing", "5.3.A.3" and "shall determine" do **not** occur in the September 24MS text. Operating "pursuant to" §5.x is consistent with **both** paths, because §3 itself says that absent the agreements *"the Secretary will proceed as described in Sections 5.2, 5.3, and 5.4"*.
- **Which state split applies is not stated in any primary read.** Under §5.3.A.2 it would be the 760/440/50 kaf agreement split. Under §5.3.A.3 the Secretary determines it. Reductions to Mead deliveries are calendar-year and start **2027-01-01**. The secondary sources treat 1/1/2027 as the practical deadline for the three-state deal.

---

## 4. Litigation (PRIMARY: court docket via CourtListener/RECAP)

**State of Nevada, Colorado River Commission of Nevada, and Southern Nevada Water Authority v. Doug Burgum (Sec. of Interior), U.S. DOI, U.S. Bureau of Reclamation, and Aubrey Bettencourt**
- Court: **U.S. District Court, District of Nevada.** Case **No. 2:26-cv-02665-GMN-NJK**. Judge **Gloria M. Navarro**, reassigned 8/26 after Judge Dorsey recused on 8/25. Magistrate Judge Nancy J. Koppe.
- **Complaint, ECF 1, header reads "Filed 08/24/26".** CourtListener's docket metadata shows "Date Filed: Aug. 23, 2026", but the entry reads "Entered: 08/24/2026". The court-stamped document date is used here.
- Claims: APA, NEPA, "Law of the River". **Prayer:** (B) vacate the 8/21/2026 ROD; (C) vacate the July 2026 Final EIS; (D) vacate the 2027-2028 Operating Guidelines; (E) enjoin implementation of the ROD and Guidelines.
- Complaint ¶72: Nevada *"stands to experience a shortfall of 213,556 acre-feet **at a 3.6 maf shortage**, which constitutes approximately 71% of Nevada's Colorado River entitlement."* ⚠️ This figure is keyed to a **3.6 maf** Lower Basin shortage, the outer bound of the Decision Framework. It is **not** the 2027-28 Guidelines' 1.25 maf, so do not read it as Nevada's 2027 cut. The Governor's 8/24 release states the same figure without that qualifier (PRIMARY, https://www.gov.nv.gov/press-releases/nevada-files-lawsuit-against-department-of-the-interior-over-colorado-river-operations-record-of-decision/).
- Docket activity visible in RECAP: summons (8/25); pro hac vice motions (9/2) and orders (9/15); DOJ appearances, Snodgrass (9/10, ECF 10) and Candrian, ENRD (9/16, ECF 14). **No PI motion, answer, dispositive motion or intervention is visible through ECF 14.** RECAP is not a full PACER mirror; CourtListener lists "Date of Last Known Filing: Sept. 16, 2026". Proof of service is due 11/22/2026.
- Ratified by the CRC Nevada board (9/17 agenda item D) and the SNWA board (9/17 agenda).
- URLs: https://www.courtlistener.com/docket/74688268/state-of-nevada-v-burgum/ · ECF 1: https://storage.courtlistener.com/recap/gov.uscourts.nvd.184047/gov.uscourts.nvd.184047.1.0_2.pdf · ECF 14: …/gov.uscourts.nvd.184047.14.0.pdf (all 200)

**Other suits:** CourtListener RECAP searches (filed ≥ 2026-08-01 or ≥ 08-20) on `Burgum "Colorado River"`, `"Lake Mead"`, `"Colorado River" "Bureau of Reclamation"`, `"Operating Guidelines" "Colorado River"` and `"Lake Powell"` return **no other challenge to the ROD**. Keyword hits that are not ROD challenges on their face:
- *GreenLatinos v. Mullin*, D. Colo. 1:26-cv-04629, filed 9/21. Defendants are DHS/ICE, NEPA cause.
- *CBD v. Burgum*, D. Or. 3:26-cv-01686, filed 8/13. ESA case against BLM/USFS, filed before the ROD.
- *State of Idaho v. United States*, D. Idaho 1:26-cv-00546. Not read.

**Not filed but authorized or considered (PRIMARY):** CAWCD Board 9/3 authorized legal action "should legal action become appropriate", on top of a prior $12M litigation fund. MWD has closed-session items "deciding whether to initiate litigation" (added 9/9 and 10/5). SECONDARY: a search summary of a Lexology item (403, not read) and news searches found no Arizona, California, tribal or Upper Basin suit.

---

## 5. October 2026 24-Month Study (PRIMARY)

| URL | HTTP (10/10 ~16:24–16:25Z) | Content |
|---|---|---|
| https://www.usbr.gov/lc/region/g4000/24mo.pdf | 200 | **"July 2026 Most Probable 24-Month Study", July 15, 2026.** The "current" LC URL is stale. sha256 `b7bf437f…a951d8a` |
| https://www.usbr.gov/lc/region/g4000/24mo_6.pdf | 200 | **September 2026 Most Probable 24MS, 6 maf scenario, September 15, 2026** |
| https://www.usbr.gov/lc/region/g4000/24mo_7.pdf | 200 | **September 2026 Most Probable 24MS, 7 maf scenario, September 15, 2026** |
| https://www.usbr.gov/uc/water/crsp/studies/index.html | 200 | Lists `24Month_08_6/_7`, `24Month_09_6/_7`, and `24Month_10.pdf`. **No `_10_6`/`_10_7`** |
| https://www.usbr.gov/uc/water/crsp/studies/24Month_10_6.pdf | **404** | — |
| https://www.usbr.gov/uc/water/crsp/studies/24Month_10_7.pdf | **404** | — |
| https://www.usbr.gov/uc/water/crsp/studies/24Month_10.pdf | 200 | **"October 2025 Most Probable 24-Month Study", October 15, 2025.** Last year's, as CALENDAR warns |

**The October 2026 24MS is not published as of 2026-10-10 16:25Z, so there are no Oct/Nov/Dec 2026 Mead projections from it.** The UC index text says the August, October, January and April runs come with Min and Max Probable runs.

---

## 6. Search log (every query, 2026-10-10)

**Web searches** (WebSearch tool; results used only as leads):
1. `Lower Basin implementing agreement Colorado River Arizona California Nevada signed October 2026` (extended)
2. `Colorado River 2027-2028 operating guidelines implementing agreement executed`
3. `Colorado River record of decision lawsuit filed 2026 Burgum` (extended)
4. `Arizona California Nevada sign Lower Basin agreement Colorado River shortage sharing 2027 2028` (extended)
5. `Colorado River lawsuit Arizona OR California OR tribe OR "Upper Basin" challenge Record of Decision September 2026` (extended)
6. `Central Arizona Project board approves agreement 2027-2028 operating guidelines Lower Basin implementation` (extended)
7. `Southern Nevada Water Authority board Lower Basin agreement October 2026`
8. `Upper Basin drought response operations agreement 2027 Flaming Gorge Upper Initial Units Upper Colorado River Commission signed` (extended)
9. `usbr.gov news release Colorado River September 2026 OR October 2026 Lower Basin` (domains usbr.gov, doi.gov)
10. `Colorado River Lower Basin agreement Hobbs Newsom Lombardo October 2026 water cuts deal finalize` (extended)
11. `Arizona legislature special session Colorado River Lower Basin agreement authorization 2026` (extended)
12. `Imperial Irrigation District board Lower Basin agreement 2027 2028 conservation approve October 2026`
13. `"Lower Basin agreement" Colorado River October 2026` (extended)
14. `snwa.com board of directors meeting agenda 2026 Colorado River` (domains snwa.com, lvvwd.com)
15. `Entsminger letter Interior "Lower Basin agreement" finalizing implementing September 2026`
16. `Arizona Legislature special session called Hobbs October 2026 Colorado River concurrent resolution`

**APIs:** MWD Legistar (`webapi.legistar.com/v1/mwdh2o/events?$filter=EventDate ge datetime'2026-08-01'`, plus eventitems for events 1907/1913/1923/1935/1939/1941/1943/1948/1951/1953/1955 and matter 7114 with its histories and attachments, both empty). CourtListener v4 search (`type=r`, 6 queries). Federal Register v1 (3 document queries + public inspection). Arizona Legislature `apps.azleg.gov/api/Session/`. All 200.

**Unreachable, with no content used:** azwater.gov (403) · iid.com (403) · crb.ca.gov (403, curl and WebFetch) · ppic.org (403) · lexology.com (403) · 8newsnow.com (403, curl and WebFetch) · ucrcommission.com (TLS name mismatch, not bypassed) · usbr.gov newsroom releases 5393–5460 (connection reset) · cap-az.com guessed paths (404) · snwa.com `/news/` (404).

**Not searched:** Arizona Water Banking Authority, Coachella Valley WD, San Diego CWA, Palo Verde ID, the Gila River Indian Community or other tribes' own sites, the Governor of California / California Natural Resources Agency, Arizona Governor press releases (azgovernor.gov), PACER directly.

**Raw downloads:** `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-AEOLUS/6c123771-9ca2-4110-985a-a5179561245c/scratchpad/crb2/`. This is scratch storage and is not preserved.
