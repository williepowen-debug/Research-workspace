---
signal_id: "SIG-W-20261022-030"
date: "2026-10-22"
timestamp: "2026-10-22T20:22:18Z"
dispatched: "2026-10-22T20:22:18Z"
source: "DEWEY"
origin: "Will-directed DEWEY commission (plan 15:25 ET, go 15:47 ET; no REQ), AGENTS/DEWEY/output/2026-10-22_bank-legacy-technology-exposure.md (e09427e8b)"
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["REGINALD"]
info: ["GIBBS", "SHADE", "OZK", "WAL", "FLG", "CORAL", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.7
confidence_language: "breach-route record medium-high (88 notices, CA and WA only); vendor map and website exposure low"
resources: 1
safety_net: "clear"
word_count: 560
entities: ["CSBS", "OCC", "Federal-Reserve", "NCUA", "CISA-KEV", "PHP2Shell", "MOVEit", "Jack-Henry", "Fiserv", "FIS", "KRE"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b v0.53. DEWEY copies verified for REGINALD, GIBBS, SHADE, OZK, WAL, FLG, PROME; CORAL backfilled (Florida section, FL-bank carve-out). WALTER return gate: CISA KEV re-read at source 20:21Z. Bank-level exposure kept off the BOARD at DEWEY's request."
---
# DEWEY research (Will-directed): older core systems are widespread at smaller banks, but 0 of 88 bank and credit-union breach notices (2023–26) cite outdated software. Breaches came through file-transfer zero-days, own-network intrusions, email and vendors. For the current PHP2Shell wave the exposed layer is bank websites and vendor web platforms, not cores

**Report:** `AGENTS/DEWEY/output/2026-10-22_bank-legacy-technology-exposure.md` (e09427e8b), with two data files in `AGENTS/DEWEY/output/`: a 167-bank KRE vendor map and 88 classified breach notices with links. **Commission:** Will directly in the DEWEY session (no WALTER REQ). Extends 017 (vendor concentration) and 026 (cyber-wave base rates). The report header says "~16:45 ET"; its commit is 16:13 ET, which governs.

| Question | DEWEY's finding |
|---|---|
| How old is the technology? | 77% of community banks outsource core processing; 1.7% run digital banking in-house (CSBS 2026). The main cores are decades old: Jack Henry on IBM i, Fiserv Premier from before 1995, FIS Systematics on mainframe. OCC (Fall 2025) and the Fed (Feb 2026) both flagged aging and end-of-life technology; the OCC's Spring 2026 report dropped that language |
| How do banks actually get breached? | 88 bank and credit-union notices to the California and Washington attorneys general, 2023–26 (71 cyber). Routes: file-transfer zero-days 34% (mostly MOVEit 2023), own network with no route stated 25%, email 24%, vendor networks 10%. **None cites outdated, unpatched or end-of-life software.** NCUA: 69% of credit-union incidents came through third parties, from 13 vendor events |
| Are banking products being exploited? | **No core or digital-banking product is on CISA's known-exploited list. WALTER re-read it at source, catalog v2026.10.21: zero entries for Fiserv, FIS, Jack Henry, Finastra, Temenos, Q2, Alkami, nCino, NCR, Evertec, Corelation.** The same catalog still does not list either PHP2Shell CVE (109618, 109619), so that escalation-watch item has not fired |
| PHP2Shell (the current wave) | It targets PHP web servers. 5 of 20 readable bank homepages run PHP-based website software; one declares a 2022-era WordPress line. These are marketing sites, usually separate from online banking and cores; PHP versions are never declared, so this is possible exposure, not confirmed vulnerability. 0 of 26 sites serve an eMudhra certificate (Chrome drops that root 10/27) |
| Who runs each bank's core? | Mostly not public: unknown for 108 of 167 KRE banks (58% of the ETF by weight), stale for 34 more. Several banks are mid-conversion through 2028, and conversions concentrate operational risk |

**The one finding that changes the frame:** the fleet's working worry ("old cores make small banks the weak point") is not what the breach record shows. The documented channel is **current internet-facing products and shared vendors**, which is the same many-banks-at-once shape as 017 and 026. That puts the watch on vendor advisories and file-transfer or web-layer zero-days, not on platform age.

**Caveats that travel:** 25% of notices state no entry route, and lawyer-written notices omit causes, so "0 cite outdated software" means never stated, not ruled out. The breach sample is two states only. The website check was one passive homepage load per bank; six bank sites blocked it.

**Do not relay as:** "small banks are hacked through old core systems" (the record says vendors, zero-days and email), "bank X is vulnerable to PHP2Shell" (not observable), or a list of exposed banks (names stay in the report and the desk copies).

**REGINALD ACTION:** decide whether the cheap passive website check becomes a recurring watch (DEWEY's suggestion; the scanners are Will-gated builds) and fold the vendor channel into the bank-vendor rows of 026's escalation checklist. **INFO:** GIBBS (large-bank rows in the map), SHADE (vendor-event aggregation), OZK, WAL and FLG (each desk's own row is in the report's tables; FLG's Fiserv Finxact conversion 2027–28 matches FLG's KB), CORAL (the report's Florida section covers four Florida banks' core vendors). RED and PROME by BOARD. No trade is implied.
