---
signal_id: SIG-W-20261009-008
date: 2026-10-09
timestamp: 2026-10-09T14:31:51Z
time_dispatched: 2026-10-09T14:31:51Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Will in-session ruling 2026-10-09 ~10:27-10:29 ET", "BRENT (brent-58) SendMessage ~10:2x ET: month choice is Will's call; basis conditions", "AGENTS/WALTER/outbox/2026-09-14_boundary-6-8-month-basis-RECOMMENDATION-to-Will.md (decision record)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Boundary-6", "Boundary-8", "gasoline-crack", "Brent-3-2-1-crack", "BZZ26", "RBZ26", "HOZ26", "RBX26", "CLX26"]
precedence: PRIORITY
action: ["BRENT"]
info: ["CARL", "HENRY", "REGINALD", "RED", "PROME"]
confidence: 1.0
confidence_language: "routing-law change on Will's ruling"
signal_type: context
safety_net: clear
event_window: closed
word_count: 330
dispatch_note: "Routing-law change, Will-ruled; changes what two IMMEDIATE alarms mean to their recipients, so it travels as a dispatch (BOARD_CONSUMPTION_SPEC 3.5.3). ROUTING_OVERLAYS v0.41 holds the letter. No recipient moved. CARL/RED/PROME INFO via BOARD id-diff."
---

# Boundary rows #6 and #8 ruled by Will (10/9): #8 = nearest common named-contract month, fires on 3 consecutive official settles above $50, count restarts at a month switch; #6 keeps its $50 spike trigger and retires the $30 re-cross

**Why:** both rows were signed off 5/8 without naming a contract month, and the reading moves with the month (escalated 9/14). BRENT confirmed today that the month choice is Will's; BRENT owns measurement and basis advice.

**#8 — Brent 3:2:1 crack `((2·RB + HO)×42/3 − Brent)` > $50.00 STRICT:**
- **Month:** the nearest month in which Brent, RBOB and ULSD all still trade (December today: `BZZ26` / `RBZ26` / `HOZ26`), named contracts only, identity checked every pull.
- **Fires on the 3rd consecutive official-settlement session above $50.00.** Two in a row = near-trigger watch, not a fire.
- **Settlement source order:** exchange settle → vendor daily row only within $0.15 of → 14:28–14:30 ET one-minute VWAP labelled ESTIMATE. A vendor "previous close" is not a settle. Estimates may raise a watch but never complete the count; within ±$0.15 of $50 on an estimate alone = UNKNOWN.
- A session with no official settlement neither counts nor resets.
- **Month switch:** first session after the Brent leg's last trading day; **a count spanning the switch restarts at zero.**
- Context, not a grade: December was $48.43 on an intraday vendor read ~09:57 ET 10/9 (not a settle).

**#6 — gasoline crack:** the **single-day ≥$50 spike** half stays live on the front matched month (`RB×42 − WTI`, same delivery month; November ~$46 intraday 10/9). The **<$30 → ≥$30 re-cross half is RETIRED** as an **insufficiently validated alert, not a proven annual false alarm**: the 9/14–15 forward curve showed a seasonal shape but did not establish annual crossings. No replacement study is commissioned; any future crack tripwire is a new registration with historical evidence and a stated decision use.

**Preserved:** the prior letters verbatim (`AGENTS/WALTER/design/history/BOUNDARY_6_8_BEFORE_2026-10-09.md`); **position exit rules unchanged** (WQ-386 reads the diesel crack, not these rows). The interim fire-and-decompose rule retires with the escalation.

**BRENT (action):** record the Dec→Jan switch date (`BZZ26` last trading day, ~end-October) for row #8; grade both rows under the new letter. **Info:** CARL, HENRY, REGINALD (alarm recipients), RED, PROME.
