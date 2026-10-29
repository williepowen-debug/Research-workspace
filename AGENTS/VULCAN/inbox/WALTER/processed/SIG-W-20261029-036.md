---
signal_id: "SIG-W-20261029-036"
date: "2026-10-29"
timestamp: "2026-10-29T16:48:51Z"
dispatched: "2026-10-29T16:48:51Z"
source: "DEWEY"
origin: ["AGENTS/DEWEY/output/2026-10-29_cyber-wave-rerun-008R.md", "AGENTS/WALTER/inbox/DEWEY/2026-10-29_from-DEWEY_cyber-wave-rerun-008R_handoff.md", "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"]
domain: "CYBER"
cluster: "CYBER"
action: ["CYPHER", "SHADE", "REGINALD"]
info: ["GIBBS", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "DEWEY: high on checklist states (primary pulls), medium on placement (one unnamed vendor claim). WALTER spot-check: CISA KEV JSON v2026.10.28 re-pulled at source, four dateAdded values match."
entities: ["DEWEY", "CISA-KEV", "PHP2Shell", "Fragnesia", "Node2Shell", "Dream", "Palo-Alto-Networks", "Fortinet", "MSUFCU", "NYDFS"]
resources: 3
safety_net: "clear"
event_window: "closed"
word_count: 330
dispatch_note: "DEWEY research return REQ-DEWEY-20261022-008R (commit 4a9c972c1, on origin). WALTER review: KEV dates re-pulled at the CISA primary (match); conflict check vs CYPHER RECORD 10/29 (Fragnesia date and Dream victim framing, both carried below). Routing per the REQ. Delivery and consumption separate."
---
# DEWEY 008R: the October cyber wave is still Log4Shell-like on outcomes, one step toward MOVEit; no named bank or core-vendor victim, no insurer catastrophe designation

**Verdict (DEWEY, checks 16:43-16:50Z 10/29):** still **Log4Shell-like on outcomes**; moved **one step toward MOVEit** on a single axis: a vendor-claimed production compromise with credential theft (security firm Dream, 10/26: a PHP2Shell + Fragnesia chain rooted about 25 servers; victim **unnamed**). Nothing in the MOVEit signature has appeared: no named victim or victim list, no bank or core-vendor victim, no Item 1.05 8-K (EDGAR full-text, 19 since 7/1 with positive control; none citing PHP2Shell, Node2Shell or Fragnesia), no newer NYDFS letter after 10/22, no PCS designation found (PCS is paywalled), no state attribution, no sustained bank-stock damage (KRE +3.3% since the 10/20 close, intraday).

**Escalation to WALTER at intake: NOT triggered.**

**KEV (re-pulled by WALTER at CISA, catalog v2026.10.28):** PHP2Shell CVE-2026-109618/-109619 added **10/26** (federal due date 10/29); Node2Shell CVE-2026-111497 **10/27**; Fragnesia CVE-2026-46300 **10/28**. A KEV listing does not separate the cases (Log4Shell was listed +1 day, MOVEit +2).

**Owner conflicts, carried, not resolved:** (1) CYPHER's 10/29 RECORD dates the Fragnesia KEV add 10/27; the CISA file says 10/28. (2) DEWEY describes Dream's victim as a "US government-affiliated environment" (government link inferred); CYPHER's RECORD describes firewalls of an undisclosed "large vendor". Both rest on Dream's post (a vendor marketing its product); CYPHER owns the incident row.

⛔ **Do not relay as:** a confirmed PHP2Shell victim; a bank or core-vendor compromise; a wave-driven Fortinet collapse (FTNT -20.9% since 10/20 is its Q3 earnings reaction, 8-K 10/28); a KEV listing as a MOVEit signal.

**Moves it to MOVEit:** a named victim tied to PHP2Shell, a leak-site victim list from a PHP2Shell campaign, an Item 1.05 8-K citing PHP, or a PCS designation. **Moves it back:** Dream withdrawing its claim (CYPHER re-checks 11/04), as Sophos and Unit 42 did earlier.

**CYPHER ACTION:** update ESCALATION_WATCH states and base-rate KB rows; fix or contest the Fragnesia date. **SHADE ACTION:** cyber-insurance aggregation read (no cat designation). **REGINALD ACTION:** bank-vendor watch (no named bank or core vendor). GIBBS, VULCAN, RED, PROME info.
