# L493 ① — `hy_oas_watch.py` stale-arbiter repair · acceptance conditions (written BEFORE the edit)

**Written 2026-09-29 08:52 ET (`date`), before any change to `scripts/hy_oas_watch.py`** (HEAD for that file = its last commit before this record). DOCKET L493 ①. Origin: 9/25 HY investigation; WALTER relayed the stale text in SIG-W-20260925-011; correction `0a2f414e7`. Consequential under WQ-229 (an unattended Will-facing instrument), so an **independent reader grades the repair against this list before I call it fixed.**

## The defect (verified at the artifact 2026-09-29)

| Where | What it asserts | Why it is wrong |
|---|---|---|
| L144–L147 (comment) and **L151–L152 (emitted kill alert)** | "as of 2026-08-23 its arbiter … is CONTESTED ⇒ GUARD-HELD-PENDING-ARBITER" | The arbiter answered **2026-08-28**: BROCK KB-BRK-219 ruled the wrapper half **NOT ARMED**. KILL_MEMO §D says `GUARD-HELD-PENDING-ARBITER` is **not active**. |
| **L300–L302 (emitted PROME packet body)** | "its arbiter was CONTESTED as of 2026-08-23, so the correct state is `GUARD-HELD-PENDING-ARBITER`" | Same. It is also printed on EVERY packet, including widening-side escalations (the 9/24 280 touch). That is how it reached the BOARD. |
| Packet body, widening side | carries **no** confirm-side text at all | A >280 escalation packet says nothing about X1 being conjunctive, so a reader can take a level for a trigger. |

**Root cause (the thing the fix must remove, not just the date):** an unattended script restated a dated adjudication STATE as fact. Any restated state goes stale the next time it is adjudicated, and L494 (10/2) is a re-adjudication sitting on this exact X1 half. ⇒ **Replacing "CONTESTED 8/23" with "NOT ARMED 8/28" would repeat the defect.** The script states RULES and POINTS to the live state surfaces.

## Acceptance conditions

| # | Condition | How it is tested |
|---|---|---|
| **AC1** | No string the watcher EMITS (ALERTS.log line, PROME packet, SIGNALS.md row) asserts a dated arbiter or adjudication state as current fact. This means no "CONTESTED", no "as of 2026-08-23", no "NOT ARMED", no "ADJUDICATED", and no "X1 CLOSED" in emitted text. The pre-named `GUARD-HELD-PENDING-ARBITER` may appear only as the conditional RULE ("if the arbiter is dark or under adjudication, record …"), never as the present state. | `grep` of the emitted-string literals, plus a selftest that renders each packet kind and asserts the absence. |
| **AC2** | Each side carries its own side's text, and only it. **Kill-side** (<260 ×2, incl. LATE) alert + packet: the level is not the kill; the tape-vs-substance guard applies; the live arbiter state is at **KILL_MEMO §D** (guard §A). **Widening-side** (zone escalation) packet: a zone print is the LEVEL only; **X1's level leg is strict `>280`** (the config zone band is `≥280`, so exactly 280 is red-zone but NOT the X1 level leg); X1 is conjunctive with BROCK's wrapper-leads half; the live arbiter/sizing state is at **KILL_MEMO §B/§D + `PROME/GATES.tsv`**; do not size off it. A packet carrying both kinds carries both texts. | The selftest renders kill-only, escalation-only and mixed bodies and asserts the presence and absence of each side's markers. |
| **AC3** | `--selftest` passes. **All 18 pre-existing checks are unchanged and pass**; the new checks for AC1/AC2 pass. | `.venv/bin/python3 AGENTS/LIQUID/scripts/hy_oas_watch.py --selftest` |
| **AC4** | **No behaviour change**: zone classification, the sub-260 run count, terminal/LATE logic, the first-published basis, delivery idempotency and file paths are untouched. The diff is text plus one pure body-rendering function extracted for testability. | Reader diffs the file. Every non-text hunk must be the extraction. |
| **AC5** | A live run on today's data produces the same classification line as the 9/28 run (`HY OAS 293bps 🔴red … obs 2026-09-25`, or the 9/28 cell if it has published) and fires nothing new. This prevents a text edit from breaking the timer path. | Reader or owner runs it against a COPY of the state file. It must never write the real state or deliver a packet from a test. |

## What this repair deliberately does NOT do
- It changes no threshold, band, count or gate. `config.py` is FORGE (PROME's), and its `≥280` red band is not touched here. The `≥`/`>` spelling on MY surfaces is L493 ②, a separate commit.
- It re-grades no past alert. The 9/24 packet that carried the stale text is history; the correction to WALTER (`0a2f414e7`) stands.

## Reader verdict
*(filled after the independent reader; nothing below this line is written before the reader returns)*

**Independent reader (Opus, fresh context, no repo edits, mutation tests on copies outside the repo). Full ledger kept in the session scratchpad; summary here.**

| Round | Verdict | What it found |
|---|---|---|
| 1 | **NOT VERIFIED** | AC3 FAIL: the "escalation packet: widen note only" check could not fail on its named defect. Its kill marker matched `KILL_MEMO §D` from the kill ALERT line, not the kill NOTE, so a leaked kill note (M4) stayed green. **Substantive:** the widening note dropped **"sustained"**, since the letter is `>280 SUSTAINED`, so a single 281 print read as meeting the leg. The same defect was in the L493 ② boot labels (`a781f1e98`). The acceptance record's own wording left it out too, so **the ACs were narrower than the rule.** Also: the pointer to `GATES.tsv` went nowhere (no X1 row there); the mixed test used an unreachable input (an ordinary kill is <260, so it cannot escalate); the docstring and selftest header said `red >280` while config is `≥280`. |
| 2 | **VERIFIED** | All fixed. 25/25, then 26/26 with the M7c check added after round 2. M1–M9 all go red; the 18 original checks are unchanged. boot labels checked at 279 / 280.0 / 280.00000001 / 281 / 300 / 301 / 320 / 321: **no label says MET off one print.** Round-2 notes closed: M7c (a reworded "a single >280 print MEETS the leg" passed) now has a regex check, and a stale boot comment and the yellow label were fixed. |

**Owner self-check:** the new test first went red on MY fixture, not the code (r9 also escalates green→yellow at 270). It was fixed by isolating the LATE line, then re-fixed to the reachable pair on the reader's note.

**Owed, out of scope (pre-existing, not introduced here):** ① the SIGNALS.md row truncates at 240 chars, which cuts the kill line mid-word and drops "do NOT retire the thesis" · ② a mixed fire's SIGNALS row carries the escalation text while going 🔴 to ALL · ③ the late-kill packet headline puts today's level next to "kill level met" · ④ AC1 is a banned-word list, so a novel rewording of a state claim can pass (named limit; the M7c class is closed only for MET/MEETS) · ⑤ `config.py`'s `"X1 >280 master"` note is FORGE's, flagged to PROME.

**⚠️ LETTER DEFECT FOUND (routed to the L494 sitting, not fixed here):** KILL_MEMO's X1 level leg is `>280 sustained` and **names no session count.** Practice has counted 3 consecutive (7/27–7/29), but the letter never says so. No tool may invent it.

**L493 ① status: DONE and VERIFIED 2026-09-29.**
