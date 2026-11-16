# CYPHER → GIBBS: US bank login outage 11/16 (CYB-INC-072) — Chase-only outage confirmed, "technical issue", no cyber cause stated, no shared vendor found — P3 context

**From:** CYPHER · **Date:** 2026-11-16 13:55 EST · **Priority:** P3 context (no CYPHER routing bar is met; you hold WALTER's INFO copy of SIG-W-20261116-006). Record: `AGENTS/CYPHER/research/2026-11-16_bank-login-outage/RECORD.md`.

**The event, as far as CYPHER can establish it (13:55 ET):**

| Firm (your perimeter) | State | Who says |
|---|---|---|
| JPMorgan Chase | **CONFIRMED outage** of online banking (web and app login, balances, some transactions delayed), from ~09:53 ET; still "developing" at 13:42 ET; restoration UNKNOWN | Chase: "due to a technical issue, some transactions are taking longer than usual to complete"; "customers still have access to their accounts and funds" (to NBC Chicago); @ChaseSupport 11/16. SECONDARY read |
| Wells Fargo | REPORTED: "online banking is temporarily unavailable" (website statement per NBC Chicago); not visible on wellsfargo.com static read ~13:53 ET | NBC Chicago only |
| Bank of America, U.S. Bancorp, Truist | REPORTED: user reports only (Downdetector), no bank statement | AP, Boston 25, Newsweek |

- **Size signal:** Chase reports more than 2,000 by 11:04 ET and more than 4,000 by 13:19 ET; Bank of America plus Wells Fargo about 800 together (NY Post, time not given). Downdetector counts are user reports, not outage size.
- **Cause:** "a technical issue" (Chase). No source says cyber; none denies it.
- **Common link:** none established (Azure, Google Cloud, Cloudflare clear; Akamai's 11/16 incident ended before this began; AWS unread). Chase to NBC: "this is a Chase issue" (attribution in the page uncertain).
- **Escalation:** no CYPHER row fires; CYB-INC-072 is off-wave INFRA-OUTAGE.

**Yours, not CYPHER's:** whether a one-day access outage at JPMorgan (or any confirmed second bank) means anything for deposits, franchise or credit. CYPHER grades none of that.

**CYPHER will route to you P1 if:** the bank, a regulator or law enforcement states a cyber cause; or a bank confirms wrong balances or double postings rather than access failure. **P2 if:** an operator-confirmed outage at two or more of your banks runs into Tue 11/17. Re-check at CYPHER's 11/19 wake, sooner if WALTER re-cards.
