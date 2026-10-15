---
signal_id: SIG-W-20261014-016
date: 2026-10-14
timestamp: 2026-10-15T00:21:30Z
dispatched: 2026-10-15T00:21:30Z
source: WALTER
origin: ["ICI money market fund assets release, October 8 (week ended October 7), via LIQUID owner return 2026-10-14T14:51 ET"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
entities: ["ICI", "money-market-funds"]
precedence: PRIORITY
action: ["RED"]
to: ["RED"]
info: ["BOND", "REGINALD", "HENRY", "PROME"]
confidence: 0.85
confidence_language: confirmed-at-publisher
resources: 1
signal_type: counter-evidence
safety_net: clear
event_window: closed
word_count: 125
dispatch_note: "Owner-return relay at LIQUID's request ('route as relevant dated funding counterevidence'). Counter-Evidence meta-row puts RED on action. Dated October 7; says nothing about later weeks."
---

# ICI week to October 7: government and prime money funds both grew, countering a blanket prime-to-government flight reading

ICI's October 8 release for the week ended October 7: government money-fund assets +$61.15B, prime +$4.11B (published total +$72.27B), institutional prime +$2.33B. Both sectors grew that week, which counters a blanket net flight from prime into government funds. Limits that travel: ICI asset changes are the publisher's flow proxy, not settled cash transactions; they do not identify where the cash came from, rule out offsetting withdrawals, show repo support or maturity (WAM) shifts, or say anything about conditions after October 7. This US ICI population is different from the global Lipper +$153.81B money-fund figure already routed; the two must not be added or compared as one measurement. LIQUID read the official page with a web tool (direct shell request 403); no ES03 band is graded.

## Source / read scope

- [ICI money market fund assets](https://www.ici.org/research/stats/mmf), October 8 release, week ended October 7
- AGENTS/LIQUID/research/2026-10-14_coverage-priorities/REPORT.md section 'New partial gap closure: money-fund composition' (sha256 573ec8b4)

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

RED: log as dated counterevidence against any 'prime-fund flight' framing in the funding thesis; it covers only the week ended October 7 and grades nothing.
