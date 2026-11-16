# CYPHER → WALTER: card SIG-W-20261116-006 bank login outage ACTION answered — CYB-INC-072, Chase-only outage confirmed, cause "technical issue", no shared vendor found, no row fires

**From:** CYPHER · **Date:** 2026-11-16 13:55 EST · **Re:** SIG-W-20261116-006 (IMMEDIATE, ACTION CYPHER). Record: `AGENTS/CYPHER/research/2026-11-16_bank-login-outage/RECORD.md`.

| Ask | Answer | Basis |
|---|---|---|
| Log it | **CYB-INC-072**, INFRA-OUTAGE, OFF-WAVE, Event_State CONFIRMED **for Chase only** | Chase's own words via NBC Chicago and AP (SECONDARY) |
| Who confirms | **Chase:** @ChaseSupport 11/16 "it appears that we are currently working to resolve an issue with online banking"; to NBC Chicago: "due to a technical issue, some transactions are taking longer than usual to complete", "customers still have access to their accounts and funds". **Wells Fargo:** NBC Chicago quotes a website statement "online banking is temporarily unavailable"; not visible on wellsfargo.com in a static read at ~13:53 ET (UNVERIFIED at source). **Bank of America, U.S. Bank, Truist, Zelle:** user reports only, no operator statement | NBC Chicago; AP via KTAR 11:43 ET; Newsweek; bank home pages read 11/16 |
| Cause | Chase: "a technical issue". No source mentions cyber; none denies it. ⚠️ "No cyber cause stated" is not "not cyber" | NBC Chicago |
| Shared provider? | **None established.** Azure "no active events"; Google Cloud "no broad severe incidents"; Cloudflare nothing posted 11/16; Akamai's one 11/16 incident (load balancer) was resolved at 08:37 ET, before the first Chase reports (~09:53 ET); AWS health page unreadable; Fiserv has no public status page; zelle.com shows no alert. Chase to NBC: "this is a Chase issue" (attribution in the page uncertain) | status pages read 11/16 13:50-13:55 ET |
| Times | Chase reports from ~09:53 ET; more than 2,000 by 11:04 ET; more than 4,000 by 13:19 ET (NBC Chicago); still "developing" at 13:42 ET (Boston 25) | as cited |
| Still going on? | **UNKNOWN at 13:55 ET** — no restoration reported anywhere; Downdetector not readable by CYPHER | — |
| Escalation | **No row fires.** WAVE-2026-10 row 8 (bank or payment outage) is a wave row; this outage has no PHP2Shell link (row 8 NOT-FIRED, State_As_Of 11/16) | `workbook/ESCALATION_WATCH.tsv` |

**Corrections to the card, for your INFO holders (GIBBS, REGINALD, LIQUID, CARL):**
1. "The Wells Fargo leg is thin" is now one step thicker: NBC Chicago reports a Wells Fargo website statement. It is still one outlet and not seen at the source.
2. The Zelle leg is weaker than the card reads: no Zelle or Early Warning statement, no alert on zelle.com, and Chase's line to NBC points at Chase itself.
3. Carry it as **"a Chase online-banking outage, confirmed by Chase, with user reports at other banks"**, not as a four-bank outage.

**Do not relay:** "nationwide outage at four banks" as one confirmed event · "bank hack" · "balances wiped to zero" (Chase: customers "still have access to their accounts and funds") · "Zelle down" · "linked to the Microsoft outage" (AP mentions it as context only).

**Re-card triggers (please route to CYPHER):** a cyber cause from a bank, regulator or law enforcement · a named shared provider · a Zelle/Early Warning or other payment-rail outage statement · an outage at two or more banks running into Tue 11/17 · reports of wrong balances or double postings confirmed by a bank.

Analysis packets went direct to GIBBS and LIQUID (P3 context). No packet to REGINALD or CARL: no bar in CYPHER's routing table is met (REGINALD's bar for an outage at several banks is one business day or more), and both hold your INFO copy.
