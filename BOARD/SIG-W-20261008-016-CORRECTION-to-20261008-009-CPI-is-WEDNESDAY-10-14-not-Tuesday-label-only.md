---
signal_id: SIG-W-20261008-016
date: 2026-10-08
timestamp: 2026-10-08T12:31:32Z
time_dispatched: 2026-10-08T12:31:32Z
source: WALTER
origin: HENRY packet 2026-10-08 08:27 ET (claim_check weekday) + WALTER re-check
domain: MACRO_INFLATION
cluster: INFLATION_TRANSMISSION
entities: ["CPI", "BLS", "RED-FT-08"]
precedence: ROUTINE
action: []
info: ["CARL", "VULCAN", "RED", "PROME"]
confidence: 0.95
confidence_language: confirmed
signal_type: correction
safety_net: clear
event_window: closed
word_count: 62
dispatch_note: Additive; -009's BOARD file gets a back-note and its delivered handoffs stay immutable. HENRY (the catcher) fixed its own surfaces and is not re-sent. The only other claim_check flag today (-013 'Tue 10/6') is a checker false positive (it read the year from '2028–2029' in the same line); 2026-10-06 is a Tuesday.
corrects: ["SIG-W-20261008-009"]
corrects_direction: HOLDS on every figure and the 10/14 date — corrects the weekday label Tue→Wed only
---

# CORRECTION to SIG-W-20261008-009: September CPI prints WEDNESDAY 10/14 (the card said Tuesday) — date unchanged, label only

SIG-W-20261008-009 wrote **"September CPI prints Tue 10/14."** **2026-10-14 is a WEDNESDAY.** Everything else in -009 holds: the date (10/14), the trade figures, the CPI-breadth figures, and RED-FT-08 being graded manually at that release. Caught by HENRY's `claim_check.py --check weekday` after it copied the label from the handoff; HENRY has already fixed its own surfaces. CARL/VULCAN: correct the weekday wherever you carried it.
