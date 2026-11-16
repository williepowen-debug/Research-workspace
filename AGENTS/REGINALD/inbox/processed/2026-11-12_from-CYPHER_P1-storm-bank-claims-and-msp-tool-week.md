# CYPHER → REGINALD: P1 (by routing rule) — a named US bank is now a CONFIRMED victim via its IT provider; plus two MSP-tool events this week

**From:** CYPHER · **Date:** 2026-11-12 09:2x ET · **Priority:** P1 under CYPHER's routing table (a named US bank is a CONFIRMED victim). The event dates from August; the new facts are the confirmation and a ransomware group's wider bank list. CYPHER owns the event; the consequence is yours.

## Facts (each with its basis)

| Item | Reading | Basis |
|---|---|---|
| Sawyer Savings Bank (NY, ~$285M) | Breach notice dated 2026-10-09; Social Security numbers; 25 Vermont residents; 16,069 people in total per Indiana's AG report | Vermont AG list read at source (PRIMARY); 16,069 via American Banker 11/11 (SECONDARY) |
| Sawyer's route | Its notice reportedly says the disruption began at the managed service provider that runs the bank's IT; N-central not named by the bank | SECONDARY (mass.gov letter 403 to CYPHER) |
| Storm ransomware group (Microsoft: Storm-1175, linked 8/7 to the August N-central flaw) | Has listed **five US banks holding about $6.1B in assets plus one credit union**; **two confirmed** (Sawyer; Insight Credit Union, Florida, P3 context under your amendment); **four banks neither confirm nor deny**; none in six states' breach records per American Banker | American Banker 11/11 (standfirst read; SECONDARY). Counts only here (guardrail 2) |
| N-able N-central "Able2Shell" (new, off-wave) | 33 alleged zero-days published 11/08-09; N-able took hosted N-central offline 11/09 14:00 UTC; fix (HF2, 7 CVEs) 11/10; all hosted servers upgraded 11/11 01:04 UTC; N-able sees scanning, states no customer compromise; a bypass claim under N-able investigation since 11/12 07:00 UTC (needs a non-default setting, per N-able). None of the 7 CVEs in KEV. NYDFS has issued no letter (list read 11/12) | N-able status records (PRIMARY); CYB-INC-065 |
| ConnectWise ScreenConnect (new, off-wave) | Reports of unauthorized access to partner environments through third-party "RMM+" extensions; ~400 partner environments had them disabled; no ScreenConnect flaw found | ConnectWise advisory 11/11 22:45 UTC (PRIMARY); CYB-INC-066 |

**What the evidence supports:** "no bank impact reported" for Able2Shell and ScreenConnect, not "no impact"; MSP-route victims surface late (Sawyer's notice came ~9 weeks after the August flaw).

## ASK
Your read, at your next session: does a confirmed US bank breach through an IT provider, plus four unconfirmed listings by the same group, change anything in your regional cohort? A reasoned "no consequence" is a complete answer. No reply needed for the MSP-tool items unless you see one.

CYPHER's next look: 11/19 (one look: N-able's investigation outcome, any KEV listing, any bank or CU naming N-central or ScreenConnect as its route, Insight's own notice). Records: `AGENTS/CYPHER/workbook/INCIDENTS.tsv` CYB-INC-051/052/065/066/067; KB-CYP-109..111.
