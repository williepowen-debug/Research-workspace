---
signal_id: "SIG-W-20261124-020"
date: "2026-11-25"
timestamp: "2026-11-25T04:46:40Z"
dispatched: "2026-11-25T04:46:40Z"
source: "FinCEN order FIN-2026-R002 (fincen.gov PDF, read 2026-11-25T04:43Z) and FinCEN news list; The Verge 2026-11-25 01:00 UTC; Sulat 2026-11-25; Silicon Report Nov 24"
origin: ["X bookmark 2125421101933080979 @HormuzLetter", "FinCEN order FIN-2026-R002"]
action: ["CYPHER"]
info: ["REGINALD", "GIBBS", "SHADE", "LIQUID", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "development"
confidence: 0.85
confidence_language: "order read at issuer; incident text through one press page; scope undisclosed"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["FinCEN", "Treasury", "SDTM", "BSA"]
word_count: 294
dispatch_note: "PRIORITY. ACTION CYPHER. Channel info REGINALD, GIBBS (BSA filers), LIQUID (no payment system named). RED, PROME by BOARD diff."
event_window: "open"
---
# FinCEN (Treasury bureau) disclosed Tue Nov 24 unauthorized access to 'a limited subset of its systems', some taken offline as a precaution (alert read through The Verge, not at FinCEN); its order FIN-2026-R002 (read at fincen.gov) gives banks that batch-file by SDTM until Dec 30 for reports due Nov 18 to Dec 29

# FinCEN cybersecurity incident

| Object | Read | Status |
|---|---|---|
| The incident | Unauthorized access to 'a limited subset of its systems'; some systems taken offline as a precaution; e-filing site works but 'some services may not be immediately available'; hotline unaffected | The Verge, Nov 25 01:00 UTC (page read), quoting FinCEN's alert; **the alert itself not read** (e-filing page is script-rendered) |
| The order | FIN-2026-R002, issued Nov 24: 'a service disruption that is hindering filers'; institutions that used SDTM as of Nov 18 file reports due Nov 18 to Dec 29 by **Dec 30**; same for beneficial ownership reports and FinCEN ID updates; other AML duties, monitoring included, stand; may be modified or extended | **primary, read at fincen.gov**. The order does not mention a cyber incident |
| SDTM outage | Alert on the e-filing site by Fri Nov 20 with no cause (JBizNews, through Sulat Nov 25) | secondary; FinCEN has not said the outage and the intrusion are one event |
| Not said | systems reached, data taken, start date, actor, any link to the CIA and ODNI breach reported the same day | The Verge: 'unclear if related' |

- **The bookmark overstates:** 'US Treasury hit by cyberattack, taking multiple FinCEN systems offline'. It is one bureau, and FinCEN took systems offline itself as a precaution. No department-wide event found.
- **So what:** no payment or settlement system is named. The money channel is (a) about six weeks of delayed batch suspicious-activity and currency reports from larger filers, and (b) if data left, bank-filed suspicious activity reports. Neither exposure is established. Delay in filing is a relief order, not a pause in monitoring.
- CYPHER owns the event; do not list institutions.
