---
signal_id: "SIG-W-20261025-020"
date: "2026-10-25"
timestamp: "2026-10-25T20:41:19Z"
dispatched: "2026-10-25T20:41:19Z"
source: "primary-verification"
origin: "Will requested investigation of uncertain bookmark claims; BM-20261025-03, no new scan or mark"
domain: "CYBER"
cluster: "MISC"
action: ["CYPHER"]
info: ["PROME", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "primary evidence and bounded verification; remaining claim limits stated in body"
resources: 1
safety_net: "clear"
word_count: 185
entities: ["Brotli", "brotlicffi", "CVE-2026-111497", "CISA", "Python"]
event_window: "closed"
dispatch_note: "Verification UPDATE: earlier uncertainty was explicit; resolves/adds evidence without changing a previously certified figure. No R1 row. Sunday outside WQ-515 sample window."
---
# Brotli Python fixes verified at PyPA; fresh KEV catalog still does not list the CVE

## Signal

Verification follow-up to the already processed October 25 bookmarks. Material delta from prior card(s): 004 and CYB-INC-027; previously unread Python primaries and refreshed KEV check.

## Data

Full [PyPA Brotli advisory](https://raw.githubusercontent.com/pypa/advisory-database/main/vulns/brotli/PYSEC-2026-4322.yaml) and [brotlicffi advisory](https://raw.githubusercontent.com/pypa/advisory-database/main/vulns/brotlicffi/PYSEC-2026-4323.yaml), published October 23, identify fixes **1.2.1** and **1.2.1.0** respectively. Vulnerability requires affected decoder code handling attacker input; generic Python/HTTP exposure is not enough. GitHub/PyPA range conventions differ, so exact installed and distro-backport mapping still matters.

[CISA catalog](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) fetched October 25: version **2026.10.23**, release **October 23 19:30:18.9209Z**, 1,756 entries; CVE-2026-111497 absent. Absence does not establish no exploitation. [Red Hat October 23 assessment](https://access.redhat.com/security/cve/cve-2026-111497) reports no public reliable RCE PoC as of its update, with severity differing from GitHub. This is the same underlying CVE, not another wave event.

## Relevance

**CYPHER ACTION:** fold Python fixes and exact KEV vintage into **CYB-INC-027**. No new incident count, successful exploitation assertion, or patch/deployment execution.

## Source

Full claim-level evidence and access limits: AGENTS/WALTER/research/2026-10-25_verify/RESULTS.md and its linked helper reports. Retrieval October 25; observation and publication dates above remain distinct.
