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

⇒ **WAL sold off into the close. The gap is very nearly HALF what the tasking assumed.** *(79.15 → 78.00.)* **This does not make the trigger fired and does not arm anything. It makes pre-staging correct rather than precautionary.**

✅ **INDEPENDENTLY CONFIRMED, same figure, ~17:0x ET:** PROME consumed the WAL desk's own verified close (`d110a070f`) at **`$79.15`** — **two desks, separate pulls, identical number.** ⚠️ **One figure in that relay does NOT verify, and I checked before carrying it: it is the FOURTH consecutive down session, not the sixth.** Unadjusted closes, own pull:

| 8/12 | 8/13 | **8/14** | 8/17 | 8/18 | 8/19 | **8/20** |
|---|---|---|---|---|---|---|
| 82.62 | 81.74 (−1.07%) | **82.32 (+0.71%) ⬅ UP** | 81.72 (−0.73%) | 80.75 (−1.19%) | 80.40 (−0.43%) | **79.15 (−1.55%)** |

**The streak is `8/17 → 8/20` = FOUR.** The **−3.85% is CORRECT** and reconciles exactly — but it is measured **from 8/14's `82.32`, which is the local PEAK and itself an UP day** *(79.15 / 82.32 − 1 = −3.85%)*. ⇒ **the magnitude survives, the count does not.** `[[finding_window_start_at_an_extremum_inverts_the_move]]`. **Nothing downstream changes** — the buffer, the catalyst-free finding and the pre-stage all stand — **but "sixth consecutive" is a stronger momentum claim than the tape supports and it would have been re-cited.** Routed back to PROME/WAL desk.

> ⚠️ **TWO CORRECT DISTANCES, TWO DENOMINATORS — do not read them as a discrepancy.** **`−1.45%`** = the move WAL must make **from `79.15`** to breach *(1.15 / 79.15)*. **`+1.47%`** = how far `79.15` sits **above `78.00`** *(1.15 / 78.00)*. **Same `$1.15` gap.** Quote whichever you mean and say which — `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`. **The tradeable one is `−1.45%`: that is the move the tape has to deliver.**

🔴 **ONE ORDINARY RED DAY FIRES THIS — measured, not asserted.** WAL 1-yr daily returns: **n=248, sd 2.30%, median ABSOLUTE move `1.24%`.** **Days with a move ≤ −1.45%: `49/248` = `19.8%`.** ⇒ **the breach base rate is ~1-in-5 on an ordinary day, and today alone was −1.55%.** *(Unconditional 1-yr base rate; states nothing about tomorrow. Note it lands within a point of the independently-computed VLY branch at 21.1% — coincidence of two ~1-in-5 tails, not a shared mechanism.)*

✅ **AND IT IS CATALYST-FREE — DOCUMENTED, NOT MERELY UNOBSERVED.** WAL desk ran a live multi-angle news sweep at Will's request for **8/13–8/20: EMPTY** — no 8-K since 7/30, no analyst action, no litigation, no release; **KRE +0.03%, ZION/EGBN green the same session.** Logged as a **clean negative, `KB-WAL-180`.** ⇒ **the drift is idiosyncratic and mechanism-less.** *(That is a finding about the ABSENCE, which only counts because somebody ran the search and wrote down the zero — `[[finding_verification_zero_is_ambiguous]]` cuts the other way here: this zero has a stated scope.)*

🔑 **Method note, because it is the whole reason this section exists:** WALTER did the right thing — it published an intraday number, **labelled it intraday**, and named the successor action. The defect would have been inheriting the relayed level as a close. `[[finding_relayed_level_predates_the_event]]`

---

## 1. ✅ RULED BY THE OWNER 2026-08-20 — `REG-T-02` IS **`UN-FIRED`**. THE QUESTION IS CLOSED.

**State token of record, verbatim — use this string in any cross-desk citation:**

> **`REG-T-02: UN-FIRED (exited 2026-06-30; prior cycle 2026-05-11 → 2026-06-30)`**

**Ruling of record: `AGENTS/REGINALD/registry/NOTES.md` §"STATE RULING 2026-08-20", commit `b51e6465c`.** ✅ **Read at REGINALD's own file by TERRY, not accepted on the relay** — `[[finding_verify_reader_before_source]]`.

**The resolution is a STATE MACHINE, and it makes BOTH prior readings partly right:**

| | |
|---|---|
| **5/11** | fired — **WALTER's 7/27 claim was CORRECT** |
| **5/12 → 6/03** | **8 further sub-78 closes = RE-ENTRIES INSIDE the fired state, not 8 separate fires.** *A trigger with an exit condition is a state machine, not an event counter.* |
| **6/30 — close 82.20** | ✅ **EXITED** — 3rd consecutive close ≥ 81.90. State returns to `UN-FIRED`. Satisfied twice more since. |
| **8/20 — close 79.15** | **`UN-FIRED`, `$1.15` above the line.** |

**Retroactivity, addressed rather than waved:** the 8/13 exit spec is **a definition of state-reset, not a dated policy** — the alternative leaves the row **permanently fired with no reachable reset.**

> 🔑 **AND THE OWNER OWNED ITS OWN GROUNDS, WHICH IS WHY THIS IS A RULING AND NOT A PREFERENCE.** REGINALD adopted the reading TERRY had flagged as *convenient*, stating why: **it is what the tape says, AND Reading A is the SAFER ERROR** — it alerts more, and on a `V1V3-ACCELERATE` chain **the costly failure is the MISSED signal, not the extra one.** *(TERRY's refusal to self-resolve was endorsed as correct in the same breath: the point was never that A was wrong, it was that **the owner, not the consumer, gets to pick** — `[[finding_owner_of_record_means_authoritative_not_correct]]`.)*

### 📌 PIN 1 — A `<78` CLOSE FROM 8/21 ONWARD IS THE **FIRST FIRE OF A NEW CYCLE**
**Fresh signal. Full `V1V3-ACCELERATE` chain — REGINALD + WAL + Will. NO duplicate suppression.** The duplicate risk this procedure raised at build time **does not apply to the cycle-opening close**, because the row exited 6/30.

### 📌 PIN 2 — ⚠️ MY DUPLICATE-SUPPRESSION CONCERN DOES NOT VANISH; IT **MOVES TO AFTER THE FIRE**
**Precedent from the prior cycle: `9` sub-78 closes in `5/11 → 6/03`.** ⇒ **when WAL enters the band, it STAYS.**

> **⇒ EXPECT RE-ENTRIES AFTER A FIRE AND SUPPRESS THEM. THE FRESH-ALERT PATH IS THE CYCLE-OPENING CLOSE ONLY.**

**Why this matters more than it looks:** the second, third and ninth sub-78 closes will each *feel* like new information and each will arrive with a red tape behind it. **They are the same fire.** A desk that re-alerts on every one of them manufactures nine urgencies out of one event — and then **an alert-fatigued reader misses the close that actually matters, which is the EXIT** (≥81.90 ×3). `[[finding_registered_gate_captures_attention]]`

⇒ **Operationally: after a fire, the only two closes that carry new information are (a) the exit count building toward ≥81.90 ×3, and (b) a genuinely new low that changes the WAL/REGINALD read — which is THEIR call to make, not an automatic alert.**

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
| **< 78.00** | **qualifying close, sustain-1 ⇒ same-day** | **① VERIFY** the close on the owner's instrument (§2) — never an intraday, never FORGE. **② ROUTE:** REGINALD owes the read; WAL owes the single-name read; **TERRY builds any proposal; Will approves.** **③ CYCLE CHECK (§1, RULED):** the row is `UN-FIRED` since 6/30 ⇒ the **first** `<78` close is a **FIRST FIRE OF A NEW CYCLE — full chain, NO suppression.** **Every SUBSEQUENT sub-78 close in the same cycle is a RE-ENTRY ⇒ SUPPRESS** (prior cycle ran **9** of them). **Fresh alerts resume only after an exit (≥81.90 ×3).** **④ TERRY's OWN OUTPUT IS §3'S PRE-REGISTERED ANSWER**: the Sep-18 cores are NOT re-opened; any new expression is a NEW CARD. |
| **< 78.00 again, same cycle** | **re-entry, NOT a new fire** | **SUPPRESS the alert.** Record the close in the cycle log; publish no fresh urgency. Prior cycle had **9** such closes. |
| **≥ 81.90, 1st or 2nd consecutive** | exit count building | Record the count. **Not an exit yet.** |
| **≥ 81.90 × 3 consecutive** | **exit condition met** | Owner un-fires the row. **TERRY does nothing** — no position consequence; the cores are already a lapse-in-progress. |
| **no close / holiday** | non-day | Neither counts nor resets. Re-check next session. |

### 🔑 THE SYMMETRY RULE — carried VERBATIM from the WAL desk, and it binds BOTH directions

> **The signal must not be suppressed because the model disagrees, AND a breach must not be read as thesis-confirmation — a move with no identified mechanism confirms no mechanism.**

**Both halves have a live failure mode here and each is the mirror of the other:**
- **Suppression side:** §3 says this desk's expression is a lapse-in-progress, and §1's re-entry rule suppresses *later* closes. **NEITHER is a reason to sit on the CYCLE-OPENING close.** Route it. **The read belongs to REGINALD and WAL; the alert is not TERRY's to withhold.** ⚠️ **Note the two suppressions are not the same thing and must not be conflated: §1 suppresses a DUPLICATE of a fire already routed; nothing here licenses suppressing the FIRST one.**
- **Confirmation side:** the drift is **catalyst-free by a documented sweep** (`KB-WAL-180`). **A `<78` print off a mechanism-less drift is a PRICE FACT, not evidence the CRE thesis is working** — and it will feel like evidence precisely because a registered gate fired. `[[finding_registered_gate_captures_attention]]` · `[[finding_market_ignoring_is_not_market_refuting]]`

### 🤝 HANDOFF — REFERENCE, DO NOT DUPLICATE
**WAL desk's next-boot `★0` already is:** *pull price → check `$78` → signal **REGINALD + PROME** 🔴 **before any recap** if printed. **That is the detection path and it is WAL's.** This procedure does **not** re-implement it and must never become a second, competing alarm. **TERRY's role starts AFTER the signal exists** — §4 step ④ and §3's pre-registered answer. *(Two desks independently scanning the same trigger is how a duplicate fire gets manufactured — see §1.)*

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
