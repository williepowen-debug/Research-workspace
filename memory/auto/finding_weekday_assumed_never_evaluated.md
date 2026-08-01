---
name: finding_weekday_assumed_never_evaluated
description: "Fleet blind spot, n=3 in one week: agents assert a date's DAY OF WEEK without evaluating it, and the error survives into escalations and ledgers; run `date -d <date> +%A` before any weekday-dependent claim"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0bad791-6fdb-4cd3-8e7e-6057db95d7db
  modified: 2026-07-27T18:51:23.320Z
---

**Three instances in one week, two of them on the same date, by three different agents. Nobody evaluated the day of week — they inferred it.**

- **WALTER, 2026-07-27:** flagged the RESEARCH-INTAKE collector as DEAD on the reasoning *"it is weekday-daily and it missed Fri 7/25 and Mon 7/27."* **7/25 was a SATURDAY.** Zero weekday runs were missed. The alarm went to PROME as a collector-death flag, blocked a lane change Will had already approved, and was repeated to Will at the next boot from WALTER's own carried record before PROME caught it.
- **BROCK, 2026-07-27:** caught itself carrying *"~8/15 BCRED"* as a filing date. **2026-08-15 is a SATURDAY.** Re-pointed to a ~8/13-8/17 window and re-labelled expectation-not-filing-date.
- **The fleet, ~2026-07-27 (via OTTO→WALTER `SIG-W-20260727-003`):** the NY Fed Household Debt & Credit release was carried fleet-wide as **"8/15"** — also a Saturday. Corrected to ~Aug 4-11.

**Why it recurs:** a date that *looks* like a business day gets treated as one. The inference is invisible — nothing in the sentence marks it as an assumption, so it reads as a fact in every downstream doc, ledger row and escalation that inherits it.

**Why it is expensive out of proportion to its size:** it is a **sub-second check that becomes an assertion about the world.** A wrong weekday turns into "the collector is dead" (a false alarm to another agent), "the filing lands 8/15" (a calendar the desk plans around), or "we missed two runs" (a fabricated outage in a closeout record).

**How to apply:**
- **Before any claim that depends on a weekday** — a missed scheduled run, a filing date, a release calendar, an "N business days" span — **run `date -d <YYYY-MM-DD> +%A`.** Do not infer it from proximity to a date you do know.
- **When checking whether a scheduled job missed a run, compare against the LAST EXPECTED RUN, not against "now."** WALTER's second error was reading liveness *inside* the day's window, before that day's run had landed — the lane ran at 16:54Z and the check was at 17:0xZ.
- **Weekend-adjacent dates are the high-risk set**: month-ends, the 15th, and any date carried from a secondary source that itself may not have checked.
- **A date inherited from your own prior record is not verified** — WALTER's second telling was to Will, from its own closeout, which had never been checked either.

Sits with [[finding_relayed_level_predates_the_event]] and [[finding_asymmetric_records_need_reconciliation]] (turned inward — the counterparty whose record disagrees is your own earlier self). The correction-taxonomy framing is [[finding_log_the_correction_with_its_catch_mechanism]]: this is the cheap-check-skipped class, and the fix is a threshold, not a resolution to be careful.

**Fleet-level guard is PROME's, not any one agent's** — three agents hit it independently, so it is not a discipline problem in any single file.

---
**n=4-6 (2026-07-31 late-eve audit round) — the class escalated to an EXECUTION GATE, and the FIX minted a fresh instance:**
- **CARL:** "Sunday 8/3" ×7 across three files (8/3 = MONDAY) — **including in the ruling record of a Will-pre-authorized mechanical execution** (V5 3→4 on the 8/3 close). Worst consequence class yet: the wrong weekday sat on the gate of an action a future session executes without asking.
- **CARL's fix, same night:** corrected the event weekday, then wrote "verify FRED weekly **w/e 8/2**" — a SUNDAY, on a series (GASREGW) whose own labels are week-ending MONDAY. **A weekday fix that doesn't check the NEW dates it writes mints the next instance.**
- **The auditor, same night:** classified a "Sunday 8/3" grep hit as "history, correct as-is" **without opening the line** — it was the live ROADMAP header carrying both the weekday error AND a superseded re-ask. The check is not just `date -d` on dates you write; it is **opening every hit before classifying it**.
- Also this round: STUE's own CLAUDE.md prescribes the exact `date -d` remedy at line 186 — the parent (CARL) didn't run it. **A remedy that lives in a sub-agent's file does not protect the parent.** Mechanization proposed to DAEDALUS 7/31 (design bundle): scan dated ledger rows + gate specs for weekday-name+date pairs at boot/closeout.
