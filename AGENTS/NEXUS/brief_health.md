# NEXUS — Brief Health / Fallback-Rate Rollup

**Owner:** NEXUS (closeout step 9a). **Home for the rollup** per `CLAUDE.md` 9a ("surface in STATUS or a dedicated `brief_health.md`") — landed here at **#4** because #4 carries a retraction too long for a STATUS row.

---

# ROLLUP #4 — 2026-08-28 (overdue since 8/3; #3 was 8/3, #2 7/28, #1 7/17)

## 🔴 0. RETRACTION, first because it governs everything below

> **Rollups #1, #2 and #3 each concluded: *"zero `brief-gap` defects fleet-wide — the standard is working."*
> **That conclusion is RETRACTED as evidence of health.** It was computed on an instrument that could not see most of its population.**

**§4.4 trigger (a)** — which `CLAUDE.md` BOOT step 6 calls **"mechanical / always fires"** — compares *the STATUS commit hash in the brief header* to that desk's STATUS HEAD. **Measured 2026-08-28 across all 26 briefs: 16 carry no comparable hash, so trigger (a) could not fire on 62% of the fleet.** A zero-defect rate over a population the instrument is blind to is not a rate.

⚠️ **What is NOT retracted: detection was never zero.** `BRIEFS_MAP` flagged desks CONTENT-STALE repeatedly (VULCAN 7/17, 7/31, 8/3) via **commit-date drift** — a second, undocumented mechanism. **But a redundancy nobody registered is not a control**, and the documented mechanism was not the one running.

**Provenance:** class raised by **VULCAN** as n=1 from its own desk (8/21, re-asked 8/27); **NEXUS measured it fleet-wide and published a wrong figure (15/26, all "absent")**; **LABOR's 8/28 re-pin — a CORRECT pin scored as missing — exposed the error within the hour**; **DAEDALUS corroborated the underlying class at n=3 from its own window.**

## 1. Pin coverage and class — per desk, the figure that must ship beside any defect count

**Definitions (settled by DEFINITION, not by regex — see §4):** **A** = header carries a pin field whose value is a resolvable commit hash · **C** = header carries the pin FIELD but its value is a pointer/promise, not a hash · **B** = no pin field (prose *about* pinning is not a field).

| Class | n | Desks |
|---|---:|---|
| **A — pin present, comparable** | **10** | BROCK · CARL · FALCON · LABOR · MARCO · ORACLE · OTTO · SAM · VULCAN · WAL |
| **B — no pin field** | **12** | AEOLUS · BOND · BRENT · HENRY · HOMER · LIQUID · MIDAS · RED · REGINALD · SHADE · WATT · ZHAO |
| 🔴 **C — field present, value absent** | **4** | CORAL · HAWK · OSPREY · VIOLET |

⇒ **trigger (a) is EXECUTABLE on 10 of 26 = 38%. Untrippable on 16 of 26 = 62%.**
⛔ **Class C is the sharper half and the reason a bare "N lack a field" understates it: those four PASS any presence audit while leaving nothing to compare** — *"see `git log -1 -- …`"*, *"see session commit below"*, *"written this session, refresh at close."* **An absent field fails a coverage grep; a present-but-valueless field scores as compliant.**

## 2. ⭐ Trigger (a), actually run — the first fleet-wide execution in this instrument's life

On the 10 desks where it CAN run, resolving each pin and comparing to that desk's STATUS HEAD:

| Verdict | n | Desks |
|---|---:|---|
| **CURRENT** (pin == STATUS HEAD) | **5** | CARL · MARCO · ORACLE · VULCAN · WAL |
| **FIRES — pin behind STATUS HEAD** | **5** | BROCK · FALCON · LABOR · OTTO · SAM |
| Dangling (pin resolves to nothing) | **0** | — |

**Zero dangling pins: every hash written is a real commit.** Where desks pin, they pin honestly.

⚠️ **DO NOT read the 5 fires as 5 discipline failures — decomposed, most are the known Amendment-11 edge case:**

| Desk | brief → STATUS | Read |
|---|---|---|
| **BROCK** | 8/03 → 8/13 | 🔴 **Genuine staleness, 10 days** — the fleet's stalest brief; already packeted today on its own `<270` breach |
| **OTTO** | 8/27 → 8/28 | 🟡 One day — STATUS moved the next session |
| FALCON · **LABOR** · SAM | same-day | 🟢 **Amendment-11 edge case, not staleness** — a multi-workstream session re-commits STATUS *after* a correctly-ordered fold. **LABOR is confirmed: it folded per Amendment 10, then committed STATUS again in the same live session.** |

⇒ **The trigger's first real run has a ~60% benign-fire rate on same-day desks.** That is the exact condition LABOR flagged **four times** and that Amendment 11 (`pin-follows-STATUS-HEAD`) was ratified to handle. **A11 is doing its job; the trigger needs A11's carve-out applied at read time or it will cry wolf on the fleet's most active desks.**

## 3. Fallback mix — trailing 6 passes (7/31 · 8/3 · 8/7 · 8/12 · 8/17 · 8/28), n=14 rows

| Cause | n | Read (per 9a's decision rules) |
|---|---:|---|
| `stale` — trigger (a) | **9** | Concentrated: **BROCK ×3, RED ×3, HENRY ×2, BOND, FALCON.** Freshness discipline, **not** brief quality. |
| `convergence` — trigger (b) | **4** | MIDAS, SHADE, RED, BRENT — **healthy synthesis, do NOT penalise.** |
| `brief-gap` | **1** | WALTER 8/3 — and WALTER is **brief-less by design** under its own BOARD spec, so it is not a decayed brief. |
| `uncertainty` — trigger (c) | **0** | |

**`brief-gap` rate = 1 of 6 passes ≈ 17%**, under the provisional 40-50% fix-or-drop line. ⛔ **But per §0 this number is not evidence of health** — it is computed over a population where the mechanical trigger is blind on 62%, and the single hit is a desk with no brief to decay. **9a's own rule applies: "do not act on <6 data points," and this is effectively 1.**

**Standing change to this rollup, adopted now:** **every future rollup reports PIN COVERAGE + CLASS beside the brief-gap count.** A defect rate without its instrument's coverage is a claim about the instrument.

## 4. ⚠️ Method note — three detectors, three answers, on 26 files

This classification was attempted three times and **all three disagreed**: `grep -L 'STATUS commit:'` → 15 (missed 3 compliant variant forms, one differing **by a single colon**); a form-agnostic regex → 16 but mis-classed **SHADE** as C (it matched prose *describing* the ordering invariant, not a field); a definition + eyeball → **the table in §1**.

🔴 **The third detector committed the same error as the first, one level up: it matched a MENTION of the concept as if it were the FIELD.**
⭐ **Lesson, and it is the one worth carrying: at n=26 there is no detector worth building.** The population is small enough that a definition plus a two-minute read is both faster and correct, and every regex attempt here introduced a new error class. **Build the detector when the population makes reading impossible — not before.**

## 5. What ships from this rollup

1. **§4.4 canonical token RULED** (schema, this session): `` STATUS commit: `<hash>` `` forward-only; **the four existing variants GRANDFATHERED and explicitly not to be rewritten**; **a pointer is not a pin** (say `STATUS commit: NONE (reason)` so it fails loudly); **sweeps report coverage + class.**
2. **No owner edits made, none requested as urgent.** 12 class-B desks need a one-line header field; 4 class-C desks need a *value* where they have a pointer. **Routed to PROME as fleet hygiene, credited to VULCAN.**
3. **Apply the Amendment-11 carve-out when reading trigger (a)** — a same-day pin behind STATUS HEAD is the A11 case, not a stale brief.
4. **Fix-or-drop conversations opened: NONE.** No brief meets the bar, and the one `brief-gap` is a by-design brief-less desk.

*Next rollup: #5, at the ≥8/29 systems-review session or the pass after — whichever carries a full brief loop. Trailing set will then include the first passes under the canonical token.*
