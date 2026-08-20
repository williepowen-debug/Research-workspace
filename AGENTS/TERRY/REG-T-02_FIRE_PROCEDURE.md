# `REG-T-02` (WAL < $78) — FIRE PROCEDURE (EXECUTION-ONLY, WRITTEN COLD)

**Built:** 2026-08-20 Thu 16:5x ET by TERRY, at PROME's tasking, **BEFORE any qualifying close.**
**Trigger owner:** REGINALD (`AGENTS/REGINALD/registry/THRESHOLDS.tsv` row 3 + `registry/NOTES.md`). **WAL** owns the single-name thesis. **TERRY** owns any trade expression. **Will** approves.

> ⛔ **THIS FILE ARMS NOTHING, MOVES NO THRESHOLD, AND PROPOSES NO TRADE.** It exists so that if `$78` prints on a close, nobody is *designing* a response at fire-time. **It cannot amend `REG-T-02` — that row is REGINALD's.** If this file and the owner's registry ever disagree, **the registry wins.**

---

## 0. 🔴 READ THIS FIRST — THE TASKING'S PREMISE WAS ALREADY STALE WHEN IT WAS WRITTEN

PROME's tasking said *"WAL closed at ~$80.05 today — the $78 trigger is +2.6% away."* **Both halves are superseded by the actual settle.**

| | value | source |
|---|---|---|
| WALTER's last read | $80.18 (−0.27%) **INTRADAY 14:18 ET** | WALTER STATUS, which **explicitly flags it is not a close** and says *"NEXT BOOT MUST PULL THE 8/20 SETTLE"* |
| PROME's tasking | ~$80.05 | tasking message |
| **✅ ACTUAL 8/20 SETTLE** | **`$79.15` (−1.55%)** | **TERRY own pull, `fetch.py`, 16:3x ET — the settle WALTER asked for and went dark before seeing** |

⇒ **WAL sold off into the close. Distance to `REG-T-02` is `1.45%`, not 2.6% — the gap is very nearly HALF what the tasking assumed.** *(79.15 → 78.00.)* **This does not make the trigger fired and does not arm anything. It makes pre-staging correct rather than precautionary.**

🔑 **Method note, because it is the whole reason this section exists:** WALTER did the right thing — it published an intraday number, **labelled it intraday**, and named the successor action. The defect would have been inheriting the relayed level as a close. `[[finding_relayed_level_predates_the_event]]`

---

## 1. ⚠️ AN OPEN QUESTION THE OWNER MUST ANSWER — DO NOT RESOLVE IT HERE

**Surfaces disagree on whether `REG-T-02` is currently FIRED or UN-FIRED, and the answer changes what a `<78` close MEANS.**

- **WALTER 7/27 (`SIG-W-20260727-016`):** *"`REG-T-02` (WAL<78) is the live example, since **it fired 5/11** and its exit condition is equally unspecified."*
- **REGINALD's `NOTES.md` (8/13 schema change):** exit conditions are **NEW SPEC as of 2026-08-13** — *"previously **every row was a one-way auto-fire with no recorded un-fire**, so a fired row could only ever be un-fired by undocumented judgment."* The exit `WAL ≥ 81.90 × 3 consecutive closes` was written **after** the 5/11 fire.
- **WALTER's live STATUS (8/20)** reads both ways in one block: the header says **"ZERO FIRES"** and lists WAL as a **near-trigger**, while the WAL line itself says **"still between fire and exit."**

⇒ **Two readings, and they are not equivalent:**

| reading | what a `<78` close is | consequence |
|---|---|---|
| **(A) row is UN-FIRED** | a **first fire**, sustain-1, same-day | dispatch IMMEDIATE → REGINALD + WAL + Will |
| **(B) row has been FIRED since 5/11 and never exited** (WAL has not printed ≥81.90×3) | a **re-entry into the fired zone**, not a new event | **an un-suppressed "FIRE" alert would be a DUPLICATE**, and treating it as new information is the error |

**⛔ TERRY DOES NOT GET TO PICK.** Both readings are defensible from the written record and **the convenient one is (A), which is exactly why I am not choosing it.** `[[finding_owner_of_record_means_authoritative_not_correct]]` — this resolves at **REGINALD's own file**, never between two derived surfaces.

**→ ASK OWED TO REGINALD (routed with this file, and answerable in one line):** *is `REG-T-02` presently FIRED or UN-FIRED?* **§4 below is written so it executes correctly either way**, so a fire is not blocked while the question is open.

---

## 2. THE INSTRUMENT — the only thing that counts

**`REG-T-02` = WAL regular-session CLOSE `< 78`, sustain `1`.** From the owner's registry, verbatim columns:

| field | value |
|---|---|
| grading instrument | `scripts/market.py` → Yahoo Finance ticker `WAL` |
| unit / basis | USD, **regular-session close, unadjusted, per-share** |
| sustain unit | **consecutive daily closes** (`1` = same-day fire) |
| exit condition | **WAL ≥ 81.90 on 3 consecutive daily closes** (+5% hysteresis) |
| chain | **REGINALD action / WAL action / Will** *(the `WAL action` leg added 7/29 by RAV Codex `383bf581`, WALTER diff-verified, REGINALD re-verified at source)* |

- ⚠️ **CLOSES ONLY. An intraday $77.xx is NOT a fire** and must not start anything. WALTER's own board states every price trigger grades on regular-session closes.
- ⚠️ **`< 78` is strict.** A close of exactly `78.00` does **not** qualify. `77.99` does.
- ⚠️ **Do not grade off a stale mirror.** `FORGE/STATUS.md` is a broker-export mirror with its own vintage — it is position truth, never price truth (root rule #4).

---

## 3. WHAT THE BOOK ALREADY HOLDS AGAINST THIS — AND THE TENSION, STATED

**Live WAL position (`FORGE/STATUS.md` via `positions_from_forge.py`, 8/20):**

| leg | qty | FORGE mark | value | P/L | DTE |
|---|---|---|---|---|---|
| WAL **$70P Sep-18** | 1 | 0.10 | $10 | **−$758.67 / −98.70%** | 29d |
| WAL **$67.5P Sep-18** | 1 | 0.05 | $5 | **−$745.67 / −99.34%** | 29d |

**Total residual ≈ `$15`.** ⚠️ Marks are FORGE-vintage — **re-pull live before any decision** (`chain_fetch.py`, rule #4).

### 🔴 THE TENSION PROME ASKED TO BE PUT ON THE RECORD — and it is sharper than "below EV"

**WAL desk shipped v2.4 on 8/20: `EV $73.92 → $75.96`, PT $52–76.** The live cores sit **below their own desk's central estimate**: $70P by **$5.96**, $67.5P by **$8.46**.

⇒ **THE FIRE LEVEL AND THE STRIKES ARE NOT THE SAME TRADE.** `REG-T-02` fires at **$78**. WAL's own EV is **$75.96**. The strikes are **$70 / $67.5**. **A move from 79.15 all the way through the trigger to WAL's own central case still leaves both legs OUT OF THE MONEY by 6–8 points with 29 days on them.**

> **⇒ A `REG-T-02` FIRE CONFIRMS DIRECTION WHILE LEAVING THIS EXPRESSION UNPAID ON THE THESIS'S OWN CENTRAL CASE.** The two questions are independent and must not be merged at fire-time:
> 1. **Is the thesis working?** — WAL's and REGINALD's call, not mine.
> 2. **Is this expression the right one?** — mine. **And the answer today is that it is a ~$15 residual needing >10% MORE downside than the trigger itself to have any intrinsic value.**

### ✅ ANSWERING PROME'S DIRECT QUESTION: does a fire re-open the Sep-18 cores?

**NO — not on its own, and this is pre-registered COLD so it cannot be decided by whatever is convenient on the day.**

- **A fire does NOT re-open them.** `$15` of residual on legs needing >10% beyond the fire level is **not a position to defend; it is a lapse already in progress.** Root rule #7 does not apply — **rule #7 governs a thesis-intact position with a timeline problem; these legs have a STRIKE problem**, and rolling to fix a strike is a new trade wearing an old trade's clothes.
- **What a fire DOES legitimately re-open:** whether a **NEW, correctly-struck** expression is warranted. That is a **fresh card** with its own entry/invalidation/sizing — **never a "roll" of the existing cores**, because presenting it as a roll would launder a new-trade decision through a management rule.
- ⚠️ **And it would be a NEW-CARD decision made against a desk whose own EV ($75.96) sits ABOVE the current spot ($79.15) by less than 5%** — i.e. WAL's central case is only ~4% of downside from here. **Size any such card to that, not to the bear tail.**

---

## 4. DECISION TABLE — read the close, then act

| WAL regular-session close | state | action |
|---|---|---|
| **≥ 78.00** (incl. exactly 78.00) | no qualifying print | ✅ **NOTHING.** No proposal, no gate change, `$0` moved. Record only if a level-watch note is wanted. |
| **< 78.00** | **qualifying close, sustain-1 ⇒ same-day** | **① VERIFY** the close on the owner's instrument (§2) — never an intraday, never FORGE. **② ROUTE:** REGINALD owes the read; WAL owes the single-name read; **TERRY builds any proposal; Will approves.** **③ DISAMBIGUATE §1** — if REGINALD says the row was already FIRED (reading B), this is a **re-entry, not a new event**, and TERRY publishes **no** fresh urgency. **④ TERRY's OWN OUTPUT IS §3'S PRE-REGISTERED ANSWER**: the Sep-18 cores are NOT re-opened; any new expression is a NEW CARD. |
| **≥ 81.90, 1st or 2nd consecutive** | exit count building | Record the count. **Not an exit yet.** |
| **≥ 81.90 × 3 consecutive** | **exit condition met** | Owner un-fires the row. **TERRY does nothing** — no position consequence; the cores are already a lapse-in-progress. |
| **no close / holiday** | non-day | Neither counts nor resets. Re-check next session. |

### ✅ THE NO-ACTION BRANCH IS LEGITIMATE AND IS THE BASE CASE
**A fire that produces no trade is a CORRECT outcome, not a missed one.** `REG-T-02` is a **thesis-recognition** trigger owned by another desk; it is **not an entry signal for this desk** and has never been one. **The failure mode this file is built against is manufacturing a trade because an alert fired** — `[[finding_registered_gate_captures_attention]]`. **If the fire prints and TERRY proposes nothing, that is the procedure working.**

---

## 5. Moot-risk, pre-registered

The Sep-18 cores expire **9/18 (29 DTE)**. **If expiry beats the trigger, the correct read is `NO-VERDICT`** — a non-event is never scored as a miss. The `$15` residual is the entire exposure; there is no scenario in which this procedure's failure to fire costs more than that.

## 6. Write-back if and only if something happened
- [ ] Record the observed close + verdict here, dated, with the value.
- [ ] `PROME/GATES.tsv` and REGINALD's `THRESHOLDS.tsv` are **THEIR files — packet them, never edit.**
- [ ] `python3 AGENTS/TERRY/scripts/ledger_sweep.py` must exit 0 before closeout.

---
*Nothing in this file moves money, arms a gate, or amends a threshold. TERRY proposes only; Will approves.*
