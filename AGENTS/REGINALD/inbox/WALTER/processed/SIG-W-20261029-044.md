---
signal_id: "SIG-W-20261029-044"
date: "2026-10-29"
timestamp: "2026-10-29T19:37:15Z"
dispatched: "2026-10-29T19:37:15Z"
source: "WALTER lane test (Google News RSS); Reuters 8/13 via Business Insurance; BankInfoSecurity 8/17"
origin: ["https://www.businessinsurance.com/hacking-group-claims-mass-data-theft-from-dozens-of-companies/ (Reuters text, WALTER curl 10/29)", "https://www.bankinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581 (WALTER curl 10/29)"]
domain: "CYBER"
cluster: "CYBER"
action: ["CYPHER"]
info: ["REGINALD", "GIBBS", "LIQUID", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.75
confidence_language: "Claim by Cl0p, unverified by Reuters; Fiserv denial quoted by Reuters and ISMG (company statement not read at Fiserv)"
entities: ["Fiserv", "Cl0p", "PTC", "Windchill", "FlexPLM", "Toast", "CVE-2026-12569"]
resources: 2
safety_net: "clear"
event_window: "closed"
word_count: 230
dispatch_note: "Found by WALTER live-testing supplier phrases for PROME's WATCH_FOR ask (14:4x ET packet): the lane fetched 0 supplier-incident headlines in 98 days. BOARD and CYPHER ledgers: no Fiserv/Cl0p/Windchill row. Old event (Aug 12-20), filed late; v0.49 bank-supplier class, not folded. Delivery and consumption separate."
---
# Missed in August: Fiserv was named in Cl0p's mass data-theft claim (PTC Windchill flaw); Cl0p claimed 874 GB incl. design files; Fiserv says no customer, bank, transaction or personal data and no effect on its operating environment

**Dated event, 8/12–8/20, never logged by the fleet.** Found today while testing news-lane phrases for bank suppliers.

- **The claim (8/12–13):** Cl0p listed nearly 50 companies on its leak site, including Shell, Philips, GE, **Fiserv** and restaurant-payments firm Toast. **Reuters could not verify** what was stolen or how much.
- **Route (likely, not proven):** a PTC Windchill / FlexPLM flaw (CVE-2026-12569, remote code execution; patch 6/17–18). Ransom-ISAC warned 7/22 that Cl0p was exploiting it. These are engineering-design tools, not banking systems.
- **Fiserv's answer** (spokesperson to Reuters; repeated to ISMG 8/17): "based on our comprehensive review to date", **no evidence that customer, banking, transaction or personal data had been compromised, or that its operating environment had been affected.** Cl0p claimed **874 GB**, including computer-aided design files.
- Fiserv was still on Cl0p's list of firms that had not negotiated (ISMG 8/17). No later Fiserv statement or 8-K found in this pass (EDGAR not checked).

**Why it matters:** Fiserv is the largest US bank core vendor (CYPHER CHK-01). On the record this is a claim against a non-banking tool with a denial, the same shape as the 2023 MOVEit wave (Cl0p, file theft, many victims). It is not a core or processing hit.

**ACTION CYPHER:** open or decline an incident row for the Fiserv listing; check EDGAR and Fiserv's own statement. Info: REGINALD, GIBBS, LIQUID (Toast/payments), RED, PROME.
