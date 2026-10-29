# boot.py leg 9 boilerplate filter — calibration 2026-10-29

**Why:** leg 9 flagged every 8-K Item 8.01 filing whose text contains a cyber term (Hanmi, ODFL and FB Financial were hand-read as forward-looking boilerplate on 10/23 and 10/29). Will approved the fix at 12:31 ET on 10/29.

**Sample:** every leg-9-kept hit 2026-07-01..2026-10-29: 47 documents. Source: EDGAR full-text search (499 term hits; items limited to 8.01, 7.01 and 9.01, and 8.01 required). Each matched document was fetched from sec.gov/Archives.

**Rule shipped:** a hit is shown as boilerplate (ℹ️, no REVIEW) only when BOTH tests come back empty:
1. **Near:** no incident verb (discovered, detected, identified, became aware, learned, experienced, gained access, exfiltrated, incident response, notified law enforcement, previously disclosed, forensic, recovery …) within 300 characters of a cyber term.
2. **Document:** no incident narrative anywhere in the document ("the/this incident", "the cybersecurity attack", "accessed and acquired", "gained unauthorized access", "activated its incident response", "notified law enforcement", "became aware of", "previously disclosed cybersecurity incident").

Fetch failures and documents where the term cannot be found still alert (fail closed).

| Iteration | Real incidents alerting | Boilerplate filtered | Verdict |
|---|---|---|---|
| A: forward-looking marker within ±400 chars | 15 of 16 | 1 of 31 | Useless: the risk lists run longer than the window |
| B: Near test only | **15 of 16. MISSED SR Bancorp (SRBK, a bank, 7/10)** | ~26 | Rejected. SRBK's body ("a data security incident … an unauthorized actor accessed and acquired") uses none of the search terms; the terms occur only in its forward-looking paragraph |
| C: Near OR verbs anywhere in the document | 16 of 16 | 9 | Too broad: risk prose says "experienced" and "identified" |
| D: Near OR document narrative incl. bare "the event" | 16 of 16 | 19 | "the event" occurs in generic risk prose |
| **E (shipped): Near OR narrative with cyber-qualified "event/attack"** | **16 of 16** | **~26** | Shipped |

The real incidents in the sample: Five Below, IEH, Clover Health, HealthStream, Levi Strauss, CenterPoint, Boston Scientific, SR Bancorp, Ardent, Veradigm, NovoCure, Conduent, Quest, Nutex (×2) and Coca-Cola.

**Live result 10/29:** Hanmi 10/29 and ODFL 10/22 → boilerplate. Quest 10/22 → still alerts (incident wording).

**Known limit:** a real incident disclosed without any of these phrasings would be filed as boilerplate. Every miss so far was caught by the narrative test, and the regexes are in `boot.py` next to this file's path. Re-calibrate if a hand-read finds a miss. The drill `test_801_boilerplate_vs_incident_vs_unread` carries the SR Bancorp shape; a mutation run (narrative test switched off) made it fail as it should.
