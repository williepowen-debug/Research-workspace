---
signal_id: "SIG-W-20261022-043"
date: "2026-10-22"
timestamp: "2026-10-23T00:26:05Z"
dispatched: "2026-10-23T00:26:05Z"
source: "WALTER"
origin: "WALTER news sweep on Will's ask (20:24 ET). Read before dispatch: TruStage status page via CrossState Credit Union Association (last updated 2026-10-20), TBS News (Bangladesh Bank, 10/22 19:30 local), People's Daily/Xinhua (SBI, 10/21), Haitian Times (Capital Bank, 10/21). TruStage start date and lawsuit from search results (WMTV 7/15, CUInsight, NAPA), not opened."
domain: "CYBER"
cluster: "BANK_COLLATERAL"
action: ["CYPHER"]
info: ["SHADE", "REGINALD", "RED"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.7
confidence_language: "TruStage service status read at a credit-union association page; start date and lawsuit secondary; the three non-US items are single-outlet reads"
resources: 4
safety_net: "clear"
word_count: 380
entities: ["TruStage", "CUNA", "Bessemer-System-FCU", "Bangladesh-Bank", "State-Bank-of-India", "SBI", "Capital-Bank-Haiti", "LockBit", "PHP2Shell"]
event_window: "closed"
dispatch_note: "TruStage is the find: a US financial-services firm in a three-month cyber recovery, absent from every BOARD signal and DEWEY report (grep -i, all history). The other three are small and outside the US."
---
# A US insurer that serves credit unions, TruStage, has been recovering from a cyberattack for three months (since July 11) and still has services down, and it was never on the BOARD. Also tonight: Bangladesh's central bank took its website offline as a precaution, State Bank of India confirmed a small data leak, and a Haitian bank is still partly down

**TruStage (US; insurance, retirement and lending-protection products sold through credit unions):**
- Attacked **Sat 7/11/2026**; services limited from 7/13; infrastructure partly rebuilt (company updates via search results, not opened). A credit union (Bessemer System FCU) filed a class action on 7/17.
- **Status page last updated 10/20, still degraded:** plastic-card claims on hold (credit unions told not to submit); about 90% of pre-incident lending claims processed; life and AD&D claims backlogged; online and phone one-time payments unavailable; retirement online access about 97% restored; annuity balances unaffected.
- **Why it matters:** this is the multi-week vendor outage at a US financial-services firm that the base rates were looking for, and it sat outside the fleet's view for three months. Whether member data was taken is unresolved in the notices read. No ransomware claim found.

**Wave-adjacent, outside the US (small):**
| Item | What is established | What is not |
|---|---|---|
| Bangladesh Bank, website offline 10/22 evening | "Precautionary measure to protect it from cyberattacks" (TBS News) | Not linked by the bank to PHP2Shell; no payment or settlement system affected per the report |
| State Bank of India | SBI confirmed a breach; 3,897 customer records (names, phones, birth dates, addresses) on the dark web; "not expected to have any material impact" (Xinhua, 10/21) | No vector, no vendor named; SBI statement not read at an exchange filing |
| Capital Bank, Haiti | Down since about 10/2; 17 of 27 branches and interbank transfers back by 10/19; online banking still down | Bank cites a "technical incident"; LockBit 5.0 claim "pending verification" |

**Do not relay as:** "a central bank was hacked" (Bangladesh: precautionary website shutdown) · "SBI hacked through PHP2Shell" (no vector).

**CYPHER ACTION:** ledger TruStage (start 7/11, status 10/20) and decide whether it changes the vendor-outage base rate; the other three as context rows (row 8 is payment or bank outages, and none of these is a payment-system outage). **INFO:** SHADE (TruStage is an insurer; claims backlog), REGINALD (credit-union channel; card-claim hold). RED by BOARD. No trade is implied.
