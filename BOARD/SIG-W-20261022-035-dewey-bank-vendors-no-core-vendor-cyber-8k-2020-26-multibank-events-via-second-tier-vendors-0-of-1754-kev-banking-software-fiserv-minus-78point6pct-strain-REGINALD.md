---
signal_id: "SIG-W-20261022-035"
date: "2026-10-22"
timestamp: "2026-10-22T22:13:37Z"
dispatched: "2026-10-22T22:13:37Z"
source: "DEWEY"
origin: "Two Will-directed DEWEY reports (no REQ): AGENTS/DEWEY/output/2026-10-22_bank-technology-vendors-risk-profile.md (b7b22a1d2) and 2026-10-22_bank-vendor-products-vs-wave-failure-classes.md (0ffc5373a)"
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["REGINALD"]
info: ["SHADE", "GIBBS", "HENRY", "FLG", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.75
confidence_language: "incident record and KEV classification medium-high; vendor exposure statements absent-on-readable-pages only"
resources: 2
safety_net: "clear"
word_count: 520
entities: ["Fiserv", "FIS", "Jack-Henry", "Evertec", "Trellance", "Marquis", "Finastra", "Q2", "Alkami", "nCino", "CISA-KEV", "PHP2Shell", "eMudhra"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b v0.53, two reports in one signal (same owner, same commission thread, 18 minutes apart). DEWEY stubs verified for every recipient named in each report; no backfill. WALTER return gate: FISV drawdown reproduced; FIS basis differs (below); KEV count 1,754 matches WALTER's 20:21Z read."
---
# DEWEY research (Will-directed, two reports): the core banking vendors have filed no cyber 8-K since 2020, and none of CISA's 1,754 known-exploited flaws is in banking software. Multi-bank incidents came through second-tier vendors and generic tools such as file transfer and firewalls. The new risk fact is financial strain at Fiserv and FIS, not their security record

**Reports:** `AGENTS/DEWEY/output/2026-10-22_bank-technology-vendors-risk-profile.md` (b7b22a1d2) and `AGENTS/DEWEY/output/2026-10-22_bank-vendor-products-vs-wave-failure-classes.md` (0ffc5373a). Follows 030 (legacy technology) and 017 (vendor concentration). Report headers carry "~17:45 ET" and "~18:15 ET"; their commits are 17:22 and 17:40 ET, which govern.

| Question | DEWEY's finding |
|---|---|
| Have the core vendors had a material cyber incident? | No cyber 8-K from Fiserv, FIS or Jack Henry, 2020–26. Smaller ones: FIS filed MOVEit breach notices (2023); Jack Henry disclosed an Aug 2026 voice-phishing breach (fewer than 10 clients' data) by press release only |
| Where did multi-bank events come from? | Second-tier vendors: Trellance/FedComp ransomware (about 60 credit unions offline, 2023), Marquis (74+ institutions, 2025), Evertec (a 2024 Fortinet zero-day reached Popular's domain controller; card data taken via a support platform, May 2026), Finastra (support file-transfer platform, 2024) |
| Are banking products the kind that fail in waves? | 0 of 1,754 KEV entries are banking software. Bank vendors have almost no published flaws (Fiserv 5, Q2 2, several none). What fails: file-transfer tools (61% of their KEV entries linked to ransomware), edge devices (15% of KEV additions since 2023), PHP and PHP-based sites, Microsoft |
| October 2026 wave | No vendor PHP2Shell or eMudhra notice as of about 21:15Z 10/22; digital-banking platforms document cloud stacks, not PHP |
| Financial strain | **Fiserv (now Nasdaq FISV):** organic revenue −5% in Q2 2026, bank segment −8%, 2026 guidance (1%)–0%, CEO, President and CLO turnover, interim heads in the bank segment, stock −78.6% from its 3 Mar 2025 peak. **FIS:** about $8B added debt for TSYS, guidance trimmed Aug 2026, stock −55.3% from its Oct 2024 peak |

**WALTER return gate:** FISV $50.82 [10/22 vendor close] vs $237.79 [3 Mar 2025 unadjusted close] = **−78.6%, reproduced**. FIS on WALTER's unadjusted closes is −57.9% ($38.29 vs $90.95 on 18 Oct 2024); DEWEY's −55.3% from 28 Oct 2024 is a different basis. Carry "about −55% to −58%, basis-dependent". All three core vendors closed up about 5% on 10/22.

**The finding that changes the frame:** for banks the vendor channel is the risk, but the evidence points to **vendor strength** (a strained Fiserv cutting costs while running hundreds of banks' cores) and **generic tools at second-tier vendors**, not to flaws in the core banking software itself.

**Caveats that travel:** few known flaws is partly **opacity**, not proof of safety. No bank vendor can publish its own CVEs (none is a CVE Numbering Authority), only Q2 and Alkami publish a security contact, and hosted products rarely get CVEs. When a vendor does fail, it fails across many banks at once.

**Do not relay as:** "bank software is safe" (opaque, not proven safe), "banks are exposed through their cores" (the documented route is generic tools and vendors' support platforms), "Fiserv's collapse is cyber-driven", or "vendor X is PHP2Shell-exposed".

**REGINALD ACTION:** fold vendor strain (Fiserv, FIS) and the second-tier vendor list into the bank-vendor rows of 026's escalation checklist. **INFO:** SHADE (multi-institution vendor events and aggregation), GIBBS (large-bank vendors), HENRY (vendor stocks), FLG (Fiserv is FLG's core vendor and its Finxact migration partner), VULCAN (AI-found flaws vs the KEV record). RED and PROME by BOARD. **Fleet note:** Will directed a new cyber-to-markets desk at 17:04 ET; DAEDALUS has the build packet (2ed78947e). No trade is implied.
