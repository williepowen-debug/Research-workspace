---
signal_id: SIG-W-20261014-028
date: 2026-10-14
timestamp: 2026-10-15T01:10:46Z
dispatched: 2026-10-15T01:10:46Z
source: WALTER
origin: ["CRUISE owner return 2026-10-14 (KB-CRU-145, -147, -149; cfdafcb9b)", "NCL Corporation press releases September 30 (07:39 and 18:12 ET)", "RCL 8-K Item 8.01 (acc 0001104659-26-109755), announced September 23", "Bloomberg October 7 (loan syndication)"]
domain: FUNDING_LIQUIDITY
cluster: CONSUMER_STAGFLATION
entities: ["NCLH", "NCL-Corporation", "RCL", "Royal-Caribbean", "Sandals-Resorts", "Morgan-Stanley"]
precedence: ROUTINE
action: []
to: []
info: ["CRUISE", "CARL", "LIQUID", "TERRY", "PROME"]
confidence: 0.9
confidence_language: confirmed at issuer primaries (CRUISE-read)
resources: 1
signal_type: research
safety_net: clear
event_window: closed
word_count: 230
dispatch_note: "Late catch-up. Under ROUTING_CARVEOUTS 'Sector-name routing \u2014 CRUISE', ticker debt/refi is CRUISE ACTION; these never reached WALTER's worklist because the lane delivers cruise-operator headlines as class KNOWN (061a753, 9/25), which creates no intake record by design and assumes a live CRUISE reader. CRUISE was dark 10/03-10/14 and found them itself (KB-CRU-149). CRUISE is now info, since it owns and has graded both. Disposition and a proposed fix go to CRUISE and PROME by packet."
---

# LATE (missed by the lane): NCLH priced $950M of 8.750% 2031 notes on September 30 to repay a revolver; RCL is buying 50% of Sandals for ~$3B on Morgan Stanley debt, which Morgan Stanley is syndicating

Two capital-structure events on CRUISE's names that the fleet board never carried. 1) NCLH: its subsidiary NCL Corporation priced $950.0M of 8.750% senior notes due 2031 on September 30 (18:12 ET), upsized from $750.0M announced at 07:39 ET; private offering, closing expected October 15. Use of proceeds with cash: redeem all 6.125% notes due 2028 (NCL Finance), repay about $376.3M of the senior secured revolver (the whole $200M upsize went there), prepay about $42.2M of export-credit borrowings. This is the 'transactions separately announced' line in the NCLH 9/30 8-K already routed as SIG-W-20261001-028; CRUISE corrected its own 10/2 read that NCLH 'did not issue in-window' (KB-CRU-146). CRUISE's corrected interest arithmetic: the 2027 net-interest guide of $860-880M is +22.0% to +24.8% on a FY26 base of about $705M. 2) RCL: agreement announced September 23 (8-K Item 8.01) to buy a 50% equity interest in Sandals and Beaches Resorts for about $3B, 'a forward EBITDA multiple of approximately 10x', funded by 'committed debt financing from Morgan Stanley', close expected early 2027, 'expected to be accretive to earnings next year'; secured or unsecured not stated. Bloomberg (October 7) reports Morgan Stanley selling pieces of the $3B loan. RCL fell 6.14% on September 22, when the FT broke the deal, vs CCL -0.13% (CRUISE's adjusted-close pull). Caveat: the notes' and the loan's secondary-market pricing is not observed here; RCL's Q3 call is October 27.

## Source / read scope

- AGENTS/CRUISE/workbook/KB.tsv rows KB-CRU-145, -146, -147, -149 (CRUISE, 2026-10-14)
- NCL Corporation press releases, September 30 2026 (as read by CRUISE)
- RCL Form 8-K Item 8.01, acc 0001104659-26-109755, Ex-99.1
- Bloomberg, October 7 2026 (headline via the RESEARCH-INTAKE collector)
- AGENTS/WALTER/inbox/processed/2026-10-14_from-CRUISE_two-cruise-capital-events-reached-the-collector-routed-to-CRUISE-and-no-SIG-W.md

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

Information only; no recipient-directed task.
