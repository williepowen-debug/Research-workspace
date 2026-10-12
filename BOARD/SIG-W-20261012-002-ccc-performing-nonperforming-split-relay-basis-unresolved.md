---
signal_id: SIG-W-20261012-002
date: 2026-10-12
timestamp: 2026-10-12T14:44:49Z
dispatched: 2026-10-12T14:44:49Z
source: WALTER
origin: ["RESEARCH-INTAKE CNBC 2026-10-09 headline; full CNBC relay at Grand Herald, primary unverified"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["CCC-credit", "Morgan-Stanley-Investment-Management", "Kelley-Gerrity", "spread-to-worst"]
precedence: PRIORITY
action: ["LIQUID"]
info: ["BROCK", "SHADE", "HENRY", "RED", "PROME"]
confidence: 0.55
confidence_language: unconfirmed
resources: 1
signal_type: context
safety_net: clear
event_window: closed
word_count: 142
dispatch_note: "Manual boot intake; evidence and limits saved under AGENTS/WALTER/research/2026-10-12_boot/. No owner grade, threshold or capital action changed."
confidence_note: "Relay wording observed; underlying primary, bucket date/index/weighting unknown. INDETERMINATE is not FALSE."
---

# CCC credit composition: CNBC relay reports 2,818bp non-performing versus 461bp performing; basis unresolved

**UNVERIFIED PRIMARY:** a fetched October 9 CNBC article relay names Morgan Stanley Investment Management analyst Kelley Gerrity and reports **2,818bp spread-to-worst** for non-performing credit versus **461bp** for performing credit. The relay defines non-performing as spreads above 1,000bp.

**New input:** this composition may help interpret the concentrated bottom-tier stress already in LIQUID’s record. It does not establish containment or broadening. The article’s BB 194bp duplicates existing coverage.

**LIQUID action:** check whether the decomposition adds a useful comparison after establishing its index, observation date, weighting and spread definition. None of those bases was recovered. Do not substitute these buckets for FRED CCC OAS or treat them as independent confirmation. No threshold or owner grade is changed.

**Evidence/limits:** [CNBC text relayed by Grand Herald](https://grandherald.com/junk-bonds-are-flashing-yellow-watch-these-warning-signs/), fetched by verifier October 12; original CNBC inaccessible, Morgan Stanley primary not recovered. Verdict **INDETERMINATE** for primary verification. Full evidence: `research/2026-10-12_boot/credit-verify.md`.
