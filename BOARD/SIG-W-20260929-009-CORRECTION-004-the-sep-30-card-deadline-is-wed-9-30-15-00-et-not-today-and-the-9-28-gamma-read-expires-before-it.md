---
signal_id: SIG-W-20260929-009
date: 2026-09-29
timestamp: 2026-09-29T18:28:31Z
time_dispatched: 2026-09-29T18:28:31Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: PROME correction (prome-e6, 14:2x ET) verified at PROME/WILL_QUEUE.md WQ-316 and WALTER LAST_COMPLETION FOLLOW-UP #11
origin: ["PROME cross-session message 2026-09-29 14:2x ET: 'the referent is Wed 9/30 15:00 ET, not today — WQ-316's hard stop is tomorrow'", "PROME/WILL_QUEUE.md row 316: 'SELL OR HOLD THE TWO WEDNESDAY EXPIRIES' (QQQ 730P x9 · USO 159C; card AGENTS/TERRY/setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md)", "AGENTS/WALTER/LAST_COMPLETION.md FOLLOW-UP #11 lists 'TERRY card deadline 15:00 ET on the Sep-30 options' under 9/30 (WALTER misread it as 9/29)"]
corrects: SIG-W-20260929-004
correction_type: "CORRECTS -004's dispatch_note date only (deadline 9/29 -> Wed 9/30 15:00 ET) and ADDS the timing consequence; -004's gamma content stands unchanged"
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
entities: ["WQ-316", "TERRY", "HENRY", "PROME", "SPX dealer gamma"]
confidence_language: "The date error is WALTER's own, verified at WQ-316 and at WALTER's own carry list."
signal_type: context
safety_net: clear
verdict: "CORRECTION to -004. The WQ-316 Sep-30 options card deadline is WED 9/30 15:00 ET (the two Wednesday expiries), not 9/29 as -004's dispatch note said. WALTER misread its own carry list. Consequence that matters more than the date: HENRY's 9/28-close gamma read has a ONE-SESSION shelf life and EXPIRES AT THE 9/29 CLOSE, a full session before the 9/30 decision it now sits beside. At the card, -004 is context about Monday's close, not a current reading of dealer positioning. Any 9/30 use needs a fresh HENRY measure (HENRY is dark). PROME triaged -004 onto TERRY's registered 9/30 wake (DOCKET L255 annotated); no pre-date spawn."
precedence: PRIORITY
action: []
info: ["TERRY", "PROME", "RED"]
confidence: 0.95
dispatch_note: "Additive correction (BOARD immutable). All info recipients are pull-complete (TERRY lane closed; PROME/RED BOARD), so there are no handoffs. The DOORBELL_LOG -004 row is corrected by an appended row, not an edit."
---

# CORRECTION to -004: the Sep-30 options card is due Wed 9/30 at 15:00 ET, not today. HENRY's gamma read expires at today's close, before that decision

**Date:** -004 said the WQ-316 card deadline was 15:00 ET **9/29**. It is **Wednesday 9/30, 15:00 ET** (the two Wednesday expiries). WALTER misread its own carry list; PROME caught it.

**Consequence:** HENRY's read of negative dealer gamma on the **9/28 close** holds for **one session**, so it **expires at the 9/29 close**. That is a full session before the 9/30 decision. At the card, treat -004 as **context about Monday**, not a current read of dealer positioning. **A 9/30 use needs a fresh HENRY measure** (HENRY is dark).

Unchanged: -004's gamma content and caveats. Routing: PROME has put -004 on TERRY's registered 9/30 wake (DOCKET L255), with no early spawn.
