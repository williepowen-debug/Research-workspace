# REGINALD registry — row notes

**Created:** 2026-07-30 · **Owner:** REGINALD
**Why this file exists:** `THRESHOLDS.tsv` is a strict 8-column TSV with no notes column, so a row cannot carry its own rationale without breaking the schema. Anything a reader needs *in order to evaluate a row correctly* lives here, keyed by `trigger_id`. **A row with an entry below cannot be read safely from the TSV alone.**

**Rule:** notes record *measurement basis, provenance, and deliberate divergences*. They never restate or modify a level, operator, window, or action — those live in the TSV and move only by an explicit ruling.

---

## `REG-T-07` — OFFICE-CMBS-DQ-TREPP > 15, sustain 3

**⚠️ Evaluation basis is load-bearing and was previously ambiguous. Two providers publish "office CMBS delinquency" and they sit ~8pp apart.**

| Evaluate against | June 2026 | Distance to the >15 fire |
|---|---|---|
| ✅ **Trepp office DQ** — THE basis for this trigger | **11.91%** [July 2026] | **3.09pp** |
| ❌ Fitch *overall* CMBS DQ (different universe **and** different scope) | 3.31% (May) | 11.7pp — reads "nowhere near" |

**History.** Until 2026-07-30 the metric field read the un-provisioned `OFFICE-CMBS-DQ`, while my STATUS dashboard row under the heading "Office CMBS DQ" carried the **Fitch overall** figure. Both numbers are correct for what they measure; the defect was **a wrong denominator under the right label**, which makes the gate look ~3.5× further from firing than it is. Found by **CREED 2026-07-27** (`inbox/processed/2026-07-27_from-CREED_REG-T-07-fires-on-my-series...`) in a Will-directed structure survey. Same provider-stacking class as `[[finding_blended_index_masks_bifurcation]]`.

**Edits made 2026-07-30 (PROME-ruled GO; disambiguation, not level moves — no level, operator, window or action changed):**
1. metric `OFFICE-CMBS-DQ` → **`OFFICE-CMBS-DQ-TREPP`**
2. recipient chain += **`CREED info`** → `REGINALD action / CREED info / BROCK SHADE info`

**★ The divergence from CREED's trigger on the same series is DELIBERATE — recorded here because nothing previously recorded that anyone had compared them.**

| | metric | op | level | sustain | purpose |
|---|---|---|---|---|---|
| **`REG-T-07`** (mine) | OFFICE-CMBS-DQ-TREPP | > | **15** | **3** | **bank-transmission ACCELERATE gate** — the point at which securitized office stress is severe and persistent enough to argue transmission into bank-held CRE |
| **`CREED-T-01a`** (CREED's) | OFFICE-CMBS-DQ-TREPP | > | **12** | **2** | **RECOGNITION gate** — earlier, faster, fires when the market is acknowledging the stress |

Different questions of the same series ⇒ different levels are correct, not a conflict. **Do not "reconcile" them to one number.** CREED owns the series; **CREED had me as `action` on its trigger while I had CREED on none of mine** — that asymmetry is what item 2 fixes.

⚠️ **Bank-HELD ≠ securitized.** This trigger reads a CMBS series and is an *input* to a bank-transmission argument, never direct evidence of bank-held CRE deterioration. The bank-held/CMBS gap is tracked separately (~7.5pp as of the STATUS row).

---

## `REG-T-02` — WAL-PRICE < 78, sustain 1

**Chain provenance.** Reads `REGINALD action / WAL action / Will` as of 2026-07-29. The `WAL action` leg was added post-WAL-promotion by **RAV Codex** (Will's outside continuity tool, commit `383bf581`), WALTER diff-verified 7/30 (`SIG-W-20260730-008`), and **re-verified at source by REGINALD 7/30** rather than accepted on the relay. No further edit is owed; WALTER's 7/25 packets asking for it are **superseded**.

### ⚖️ EXIT GRADE 2026-09-02 (owner, REGINALD) — **NOT QUALIFYING. State stays `FIRED`; exit run `0-of-3`.**

> **WAL $79.12** settled regular-session close (+$1.86 / +2.41% vs $77.26 [9/1]); O 77.86 / H 80.55 / L 77.82 / C 79.12; vol 1,245,295. **Instruments agree:** `scripts/market.py`, the yfinance daily bar and `regularMarketPrice` all return **79.12** — no disagreement to adjudicate.
> **Exit condition is `WAL ≥ 81.90 on 3 CONSECUTIVE daily closes`. 9/2 closed $2.78 / +3.51% short of leg 1 ⇒ not a qualifying close; the run stays 0-of-3 (it was 0, so nothing reset).**
> ⛔ **THE ERROR THIS GRADE EXISTS TO PREVENT: WAL closed back ABOVE $78 and that is NOT an un-fire.** `REG-T-02` is a state machine, not an event counter — once `FIRED`, it clears **only** on the registered exit condition. A close above the $78 trigger line looks like a reversal and is not one; anyone reading "WAL $79.12 > $78, so the trigger is clear" has read the trigger, not the state. Sub-78 re-entries stay suppressed for the same reason.
> ⚠️ **Intraday is not gradeable, demonstrated by today's own tape:** the 14:23 print was **$79.51** and the settled close came in **LOWER at $79.12**. `value_basis` is *regular-session close* — same-day readable, so this grades at the close and never off a last-trade.
> **NEW ARTIFACT — `registry/REG_T02_EXIT_LOG.tsv` (append-only, one row per settled close).** The run count had been living in prose on `STATUS.md`, i.e. carried from session to session by memory — the same shape as the CCC/HY row that read *"NOT ARMED … FALLING"* on stale data for three weeks. **The count is now COUNTED from the log, not remembered.** `[[finding_mechanize_the_cap_not_the_ritual]]`
> **Routing: NONE OWED and none sent.** The registered announcement fires on the 3rd qualifying close; TERRY asked for a packet at 2-of-3. The count is 0. Per the standing rule: log the close, move on — do not re-alert a non-event.
> ⚠️ **Consequence note:** `GATE-TERRY-ROLL70` filled 9/2 14:21 ET, so this grade now guards a LIVE position (1× WAL Dec-18 $70P @ $2.20) rather than a staged card. A grading error costs money in both directions.

### ⚖️ STATE RULING 2026-09-01 (owner, REGINALD) — **`REG-T-02` is `FIRED`. Fired 2026-09-01 (cycle 2 start). Exit condition `WAL ≥ 81.90 ×3 consecutive daily closes` is now LIVE.**

**State token for cross-desk records: `FIRED (fired 2026-09-01 on the 9/1 regular-session close $77.26; cycle 2 open; prior cycle 2026-05-11 → 2026-06-30; exit ≥81.90 ×3 consecutive closes LIVE, run 0-of-3)`.**

> **Graded at the registered instrument, not inherited from PROME's consumer read** (`scripts/market.py` → Yahoo `WAL`, regular-session close, unadjusted; re-run Tue 2026-09-01 ~17:0x ET, `marketState: POST`). **Daily bar 9/1: Open 77.94 · High 78.93 · Low 77.05 · Close `$77.26` · Vol 1,044,298** (yfinance `history()`); `regularMarketPrice` 77.26 / `regularMarketPreviousClose` 78.13 — the two reads AGREE, and they agree with PROME's `fetch.py` read ($77.26, −1.11%). **Instrument disagreement: NONE.**
> **Graded against the registered spec:** `WAL-PRICE < 78`, sustain 1. **$77.26 IS < 78.00 ⇒ FIRE. First sub-$78 close since the 6/30 exit ⇒ FIRST FIRE OF A NEW CYCLE (cycle 2), exactly the forward clause the 8/20 ruling wrote and 8/23 / 8/28 re-anchored. No duplicate-suppression applies to THIS close; every subsequent sub-$78 close is a RE-ENTRY inside the fired state and IS suppressed.**
> **Distance, derived from the CLOSE and from nothing else: `$78.00 − $77.26 = $0.74` BELOW the line = `0.74 ÷ 78.00 = 0.95%` below the threshold (÷ threshold basis) / `0.74 ÷ 77.26 = 0.96%` (÷ close basis). Day: `$77.26 − $78.13 [8/31] = −$0.87 / −1.11%`.** ⚠️ Intraday low $77.05 is the deepest print of cycle-1-exit-to-now (beats 8/27's $77.13); recorded, not gradeable. Volume 1.03× 3-mo average (1,044,298 vs 1,016,884) — **no volume tell.**
> ⛔ **KILL-ON-SIGHT from this ruling forward: every buffer figure this desk published 8/21→8/28 (`2.10%` · `0.50%` · `0.91%` · `0.70%` · `$0.55 above`) is HISTORY. WAL is BELOW the line, not above it; there is no "buffer" to quote. The only live distances are the two above and the exit distance: `$81.90 − $77.26 = $4.64` = WAL must RISE `6.01%` (÷ close) to print ONE qualifying exit close, and needs THREE in a row.**
> **Consequence executed (registered action `V1V3-ACCELERATE` → `REGINALD action / WAL action / Will`):** ① REGINALD action = this ruling + `STATUS.md` state flip + attribution below; ② WAL action = packet `AGENTS/WAL/inbox/2026-09-01_from-REGINALD_REG-T-02-FIRED-WAL-77.26-V1V3-ACCELERATE-single-name-leg.md`; ③ Will = packet `PROME/inbox/2026-09-01_from-REGINALD_REG-T-02-FIRED-WAL-77.26-V1V3-ACCELERATE-will-leg-Sep-18-pair.md` (⚖️ line on the Sep-18 67.5/70P pair; any trade = Will [Approve] + TERRY construction + live broker book; nothing self-executes). `AGENTS/SIGNALS.md` row appended (carve-out ②). `PROME/GATES.tsv` is PROME's to sync from this ruling — not edited here.
> **⚠️ ATTRIBUTION — the fire is a LEVEL event on a SECTOR day; the V1/V3 MECHANISM is NOT in the tape (VERIFIED at the instrument, 9/1 closes vs 8/31):** WAL **−1.11%** vs KRE **−1.28%** · KBE −1.27% · IWM −1.14% · XLF −0.88% · SPY −0.69%. **WAL fell LESS than its own sector ETF** (beat KRE by 17bp). Inside my 26-bank NDFI cohort (`workbook/NDFI_COHORT.tsv`) the 9/1 move ran **mean −1.13% / median −1.15%, range −2.71% (SBCF) → +0.75% (WFC)**; **WAL −1.11% ranks 14th of 26 = the median.** Worst were SBCF −2.71 · CUBI −2.25 · RF −1.97 · VLY −1.91 · BKU −1.89 · FLG −1.88; money-centres were flat-to-up. **Spearman ρ(PC-NDFI % of loans, 9/1 move) = +0.253, n=26; ρ(total NDFI %) = +0.298** — the SIGN is wrong for a private-credit repricing (higher exposure fell LESS; it is a size effect), so **the 8/20 result (ρ −0.255) is REPRODUCED in kind: banks are not being repriced for NDFI exposure today either.** The day's epicentre was the ALT-MANAGER complex — BX −4.59% · OWL −4.58% · APO −3.58% · ARES −2.85% (ARCC only −0.80%) — with VIX +13% to 16.34, crude +5.7%, 10Y 4.80%. ⇒ **Sector-wide risk-off with a private-credit-manager epicentre that did NOT transmit to bank-level sorting. WAL-specific component ≈ 0.** ⛔ **Do not narrate this fire as "the hidden-CRE thesis accelerating" — the letter fires on the LEVEL and the routing is mechanical; the MECHANISM leg (`V1` MI3 disconfirmed 8/7 at <25% ×12 quarters; `V3` 11-for-11 no reserve build Q2; BROCK 8/28: WAL's $126.4M First Brands receivables charge-off is H1-2026, in the 7/31 10-Q, a collateral-perfection failure not a credit-selection one, and does NOT fire `BRK-31`) is UNCHANGED by a price crossing a fixed line on a day the whole cohort fell.** `[[finding_registered_trigger_can_fire_on_an_unnamed_mechanism]]` — metric hit, cause unnamed: the FIRE is real under the letter (no mechanism clause exists in this spec), the ACCELERATE is a routing obligation, and the attribution travels WITH it so nobody downstream reads the routing as evidence.
> **Base rate, closed:** TERRY's ~1-in-5 (from $79.15) was an upper bound from $79.67; the event realised on the 7th evaluable close of the near-band (8/21→9/1: 79.67 · 78.39 · 79.63 · 79.60 · 78.71 · 78.55 · 78.13 · **77.26**). Precedent from cycle 1 (9 sub-78 closes 5/11→6/03): expect re-entries; suppress them.
> **Instrument note (VERIFIED 9/1, not a defect in this grade):** the yfinance daily `history()` for WAL and KRE returned NO 2026-08-28 bar today (8/27 → 8/31); the 8/28 closes ($78.55 / $74.31) were graded live on 8/28 and stand. The 9/1 bar is present and agrees with the quote endpoint.
> **`REG-T-01` graded the same close: `UN-FIRED`.** KRE **$72.62** [9/1 close, −$0.94 / −1.28% vs $73.56 (8/31); O 73.36 / H 73.82 / L 72.42; vol 14.0M]. **$12.62 above $60.00 = 21.0% above the line (÷ threshold) / KRE must fall 17.4% (÷ close).** Nowhere near.

### ⚖️ STATE RULING 2026-08-20 (owner, REGINALD) — **`REG-T-02` is `UN-FIRED`. Exited 2026-06-30.**

**State token for cross-desk records: `UN-FIRED (exited 2026-06-30; prior cycle 2026-05-11 → 2026-06-30; state re-graded and CONFIRMED UN-FIRED at the 2026-08-21 close)`.**

> ⚖️ **GRADING ADDENDUM 2026-08-23 (owner, REGINALD) — re-graded at the instrument, not inherited from a summary.**
> **Fri 2026-08-21 close: WAL `$79.67` (+0.66%)** [`scripts/market.py` → Yahoo `WAL`, regular-session close, unadjusted — the registered grading instrument, re-run this session; markets closed 8/22-23, so this is final-for-week and no intervening close exists].
> **Graded against the registered spec:** `WAL-PRICE < 78`, sustain 1. **$79.67 is NOT < 78 ⇒ NO FIRE. State is `UN-FIRED` and unchanged.** Exit condition (`≥ 81.90 ×3 consecutive`) is irrelevant while un-fired — a no-op, as on 7/27-28 and 8/05.
> **Distance, derived from the CLOSE and from nothing else: `$79.67 − $78.00 = $1.67` above the line = `1.67 ÷ 79.67 = 2.10%`.**
> ⛔ **KILL-ON-SIGHT: "WAL is 2.00% from `REG-T-02`."** That figure is wrong and it is wrong in the DANGEROUS direction — it understates the buffer, so it makes the trigger look nearer than it is. **2.10% is the number; anything else must be re-derived from a named close before it is repeated.** ⚠️ Equally kill-on-sight: **any WAL-to-`REG-T-02` distance not re-derived from a specific dated CLOSE.** An intraday print, a percentage carried forward from a prior session, or a distance quoted without its close is not a grade of this trigger. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`
> **The 8/20 ruling's forward clause is UNCHANGED and now re-anchored one session later:** the 8/21 session came and went without a sub-78 close, so **a close <78 from Mon 2026-08-24 onward is still a FIRST FIRE OF A NEW CYCLE** — full `V1V3-ACCELERATE` to `REGINALD action / WAL action / Will`, **no duplicate-suppression**. Re-entries *after* such a fire are suppressed; the first one is not.
> ⚠️ **The base rate moved with the price and it moved the RIGHT way, slightly.** TERRY's measurement (49/248 sessions ≤ −1.45%) was taken from **$79.15**, needing −1.45% to reach $78. From **$79.67** the required one-day move is **−2.10%**, a strictly rarer event — so **~1-in-5 is now an UPPER bound, not the estimate.** ⛔ Do not re-cite the 1-in-5 figure as if it were computed at this price; it was not, and I have not re-run TERRY's distribution.
> **Nothing was registered, no band moved, no level changed.** This is a state annotation at my own surface. `PROME` owns the fleet ledger sync (`GATES.tsv` is not mine to edit and I did not touch it).

**Asked by PROME 8/20 with WAL at $79.15 (+$1.15 from the line) and a live fire procedure staged. Ruled on the TAPE, not on the record conflict — the exit condition is a number and the number is gradeable.**

**Full state history, graded close-by-close against the registered spec** (`WAL-PRICE < 78`, sustain 1 daily close; exit `WAL ≥ 81.90 on 3 consecutive daily closes`), instrument `market.py` → Yahoo `WAL`, regular-session close unadjusted:

| Date | Close | Event |
|---|---:|---|
| **2026-05-11** | **76.95** | 🔴 **FIRED** — first close <78. **WALTER's 7/27 claim that it fired 5/11 is CORRECT.** |
| 5/12 → 6/03 | 77.56 · 74.97 · 75.93 · 74.42 · 76.59 · 76.11 · 77.03 · 77.75 | **8 further sub-78 closes — these are RE-ENTRIES INSIDE the fired state, NOT 8 separate fires.** A trigger with an exit condition is a state machine, not an event counter. |
| 6/26 · 6/29 | 82.05 · 82.88 | exit run 1, 2 |
| **2026-06-30** | **82.20** | ✅ **EXITED — 3rd consecutive close ≥ 81.90.** State returns to `UN-FIRED`. |
| 7/27-28 · 8/05 | — | exit condition satisfied twice more — **no-ops, already un-fired.** |
| **2026-08-20** | **79.15** | `UN-FIRED`, **+$1.15 above the line.** |
| **2026-08-21** | **79.67** | `UN-FIRED` — **+$1.67 / 2.10% above the line.** Re-graded 8/23 at the registered instrument. Week's final close; **no fire, no state change.** |

⇒ **A close <78 from 2026-08-21 onward is a FIRST FIRE OF A NEW CYCLE — a fresh signal. Full `V1V3-ACCELERATE` alert to `REGINALD action / WAL action / Will`. NO duplicate-suppression applies.** (PROME's Reading A.)

**⚠️ I am adopting the reading TERRY declined *because it was convenient* — so the grounds matter, and they are not convenience:**
1. **It is what the tape says.** The exit is a registered number; it was met on 6/30 and twice since. This is a measurement, not a judgment.
2. **It is also the SAFER error.** Reading A produces MORE alerting (a fresh full-chain alert), Reading B produces LESS (suppressed as duplicate). On a trigger whose action is `V1V3-ACCELERATE` with Will on the chain, **the costly error is the missed signal, not the extra one.** Convenient and conservative point the same way here; that coincidence does not make it wrong.

**⚠️ Retroactivity, addressed rather than assumed.** The exit spec was written **2026-08-13**; the exit event was **2026-06-30**. I rule the spec applies retroactively, because it was written as a **definition of when this trigger's state resets**, not as a policy with an effective date — and the alternative is absurd: with no retroactive application the trigger would be **permanently fired from 5/11 with no reachable reset**, which was plainly not the intent of writing an exit at all. *(This is the `finding_threshold_level_is_a_measurement_not_a_constant` family — the level was FROZEN; the state derived from it is TRACKED.)*

**⚠️ Both halves of WALTER's live board are wrong, in opposite directions** — *"ZERO FIRES"* (it fired 5/11) and *"still between fire and exit"* (it exited 6/30). **Neither is a reading of the tape; both are artifacts of a fire-ledger that recorded neither the fire nor the exit.** ⇒ **`REG-T` fire-ledger state must be graded against the instrument, never inherited from a board summary** — flagged to PROME for WALTER, not fixed here (not my file).

⚠️ **Base rate, for whoever sizes the alert:** TERRY measured 49/248 sessions ≤ −1.45% ⇒ **~1-in-5 chance of firing on any given day from $79.15.** This is a near-trigger band, not a remote tail. **The 9 sub-78 closes in the 5/11→6/03 cycle are the precedent: when it fires it tends to STAY in the band, so expect re-entries and suppress them under this ruling, not fresh alerts.**

⚠️ **Sustain is 1 — if it fires, it fires SAME-DAY**, with REGINALD + WAL + Will all on `action`. WAL has been oscillating around the ~5% near-trigger band. **WAL-specific analysis belongs to `../WAL/`;** REGINALD keeps the matrix row and cohort context only.

---

## `REG-T-03` / `REG-T-04` — HY-OAS > 320 / > 350

**⚠️ Two standing interpretation caveats — the levels are UNCHANGED by both; carry them when citing either row:**
1. **Composition drift (SIG-723-002, 7/23):** the thresholds are NOMINAL and the HY index has improved since calibration (CCC weight ~10% vs 16%, secured ~37% vs 18%) — the same print now represents MORE stress than at calibration. Flagged as anchor-drift family, not moved.
2. **Blended-index tail-lag (SIG-717-003, WALTER 7/15; promoted from SCRATCH 8/10):** the blended HY index can sit at a benign percentile while the CCC constituent sits at a stressed one (measured 7/15: blended at the 8.3 pctile of its 3-yr range, CCC at 87.8) — so a tail-led credit break may fire late against these blended-level triggers. Companion instrument = the CCC/HY RATIO tripwire `VX-REG-18.04` (spec pinned to the ratio 7/30), which is the tail-sensitive leg; sub-index (BB/B) collection is a fleet gap flagged to PROME by WALTER.

**Downstream-of-bank caveat (7/30 attribution, standing):** HY sits DOWNSTREAM of bank credit in my chain — an HY move without a bank-credit leg is not my chain firing. Before treating any HY level as bank transmission, run the bank-credit cross-check (`reports/2026-07-30_bank-side-HY-attribution.md`).

---

# SCHEMA CHANGE 2026-08-13 — audit-convention encode (8 cols → 13, APPEND-ONLY)

**Authority:** `PROME/proposals/2026-08-12_audit-convention-RULED.md` (Will-approved 2026-08-12, FLEET SCOPE) — *"a stored value must carry its unit and basis; a threshold must name the instrument that grades it (a continuous series is not a contract); and 'zero' must be distinguishable from 'unknown' and from 'not applicable.'"* Encode requested of REGINALD via PROME's 2026-08-13 spawn brief off DAEDALUS's `THRESHOLDS.tsv` findings (**zero exit conditions · zero instrument/basis columns**).

**⚠️ FLAG-BEFORE-ENCODE — the tension I resolved, stated rather than assumed.** DAEDALUS's own REGINALD profile records **"THRESHOLDS 8-col contract"** as a HELD invariant and **"NOTES.md is a companion, never folds into the TSV."** The convention needs machine-readable per-row instrument/basis; NOTES is prose keyed by `trigger_id` and only two rows carry entries. **Resolution: APPEND-ONLY extension.** Columns 1-8 are **byte-identical to `de75ab659`** (verified by `cut -f1-8` diff), so the 8-col contract survives as an exact prefix and any positional reader is unaffected; the five new columns are appended at the end. **No level, operator, sustain window, action, recipient chain or thesis ref moved.** Grep for script consumers before the edit returned **zero** — this file is read by humans and packets only.

| New column | Carries |
|---|---|
| `grading_instrument` | The named series/tool that grades the row. *A continuous series is not a contract* — so the row names FRED `BAMLH0A0HYM2`, not "HY OAS." |
| `value_unit` | Unit of `threshold_value` (USD / bps / percent / thousands of persons / USD billions). |
| `value_basis` | What the number measures — close vs intraday, SA vs NSA, rate vs balance, first-release vs revised. |
| `sustain_unit` | **The defect this closes:** `sustain_window` was a bare integer meaning *daily closes* on REG-T-01/02/03/04/08, *weekly prints* on REG-T-05, *monthly prints* on REG-T-07 and *quarterly prints* on REG-T-06. One column, four different clocks, none written down. |
| `exit_condition` | What un-fires the row. Previously **every row was a one-way auto-fire with no recorded un-fire**, so a fired row could only ever be un-fired by undocumented judgment. |

**Exit conditions are NEW SPEC, pre-registered here, and are deliberately conservative.** Construction rule, applied uniformly: exit requires the metric back on the benign side **by a stated margin** (5% hysteresis on the two price rows; 20bp on HY; a proportionate step on the rest) sustained for a window **≥ the entry window**, graded on the **same instrument** as entry. This is asymmetric by design — harder to un-fire than to fire — because a fired row escalates other agents and an oscillating gate would thrash the whole chain. **These are not levels moved: no entry threshold changed, and before this edit the exit was not "something else," it was *nothing*.** They are gradeable and executable inside the window their instruments quote (`finding_executability_is_a_separate_audit_axis`). If any owner on a recipient chain thinks an exit is mis-set, argue it before it fires, not after.

**Not registered, deliberately.** MI3 / hidden-CRE has **no row in this registry** and I did not add one on the day I re-ran the screen. The cohort re-run (`reports/2026-08-13_MI3_cohort_rerun.md`) found the legacy `>20%` flag catches one name on the legacy basis and **zero on the uniform basis** — so a new MI3 trigger would need its base rate and separation established first, and *"don't build it"* is a real answer (`finding_base_rate_the_threshold_before_building_it`). Recorded as a candidate on ROADMAP, not as a gate.

---

# MI3 HIDDEN-CRE SCREEN — HARDENING + FLAG DISPOSITION (2026-08-13, PROME follow-up, Will-directed)

**Why this section is in the registry file:** the 8/13 re-run was correct partly because the operator hand-caught the traps *in flight*. That is not a control. This records what moved out of session memory and into the instrument, plus the two judgment calls that are mine and not the script's. **Instrument:** `scripts/mi3_cohort_screen.py` (runbook now lives in its header — cohort definition + rationale, quarters convention, credentials, cadence, and the five traps). **Falsifier:** `scripts/mi3_guard_selftest.py`.

## What is now enforced by the tool rather than remembered

| Guard | Catches | Behaviour |
|---|---|---|
| `coverage_guard` | a bank-quarter silently dropped from the run | **exit 2, nothing written** |
| `schema_guard` | a blank/None in a scored cell — the class that would render a 031-filer's unresolved `RCON1766` as an implied **zero**, i.e. *"six banks have no hidden CRE"* | **exit 2, nothing written** |
| `repro_guard` | **the 37.6% class** — a previously published bank-quarter that no longer reproduces against the prior **committed** vintage (read from `git show HEAD:`, never the working tree) | **exit 2**, unless the restatement is DECLARED via `--accept-restatement "<why + source>"`, which records it on the row and in the summary |

Real FFIEC amendments happen, so restatement is *allowed* — but it can never be *silent*. **The defect that poisoned the OZK cell for months was found by archaeology; it is now found by the machine on the next run.**

**Fail-loud, never fail-partial.** Output is written to `.tmp` + `os.replace` only after all three guards pass, so a tripped guard leaves the previous good vintage in place rather than a half-written one.

**State vocabulary (8/12 convention).** `status` ∈ {OK, OK-V1-ONLY | NOT-REPORTED, DENOM-MISSING, PULL-FAILED}; scored statuses must carry every required cell, unscored statuses must carry **none**. `mi3_zero_class` ∈ {REPORTED-ZERO, NONZERO, UNKNOWN} — SBCF and AMTB file a **reported 0**, which is data, not a gap. A YoY off a zero base is recorded `N-A-ZERO-BASE`: **a third state, not a missing number.**

**Standard output is dual-basis AND absolute dollars, by construction.** `MI3_COHORT.tsv` carries `v1_pct`, `v1a_pct`, `item9_share_of_base_pct`, `mi3_k` and `mi3_yoy_pct` on every row; the script also generates `workbook/MI3_COHORT_SUMMARY.md`, which ranks the cohort **three ways** (v1 · v1a · dollar level) and auto-emits a warning whenever the two bases disagree on the top name or the largest absolute book is not the top ratio. **The up-cap migration is visible in default output — an analyst cannot fail to compute it, because nobody computes it.**

> ## ★ BASIS-NAMING RULE (binding on every claim sourced from this screen)
> **No cross-bank statement without its basis named.** `v1a` (÷ item 4 + item 9) governs **all** cross-bank claims. `v1` (÷ item 4) is retained **only** for continuity against v1-vintage records and is **not cross-bank comparable**. And **never quote a ratio without its dollars.**

**Guards are falsified, not assumed.** `mi3_guard_selftest.py` asserts each guard trips on the exact defect it exists to catch (8 cases: 5 trip, 1 declared-restatement passes, 1 no-false-positive on the live output). **8/8 at 2026-08-13.** A guard nobody has watched fail is an assumption. Re-run it whenever the script changes.

## ★ RULING 1 (mine, owner-lane) — the legacy `>20%` v1 flag is **RETIRED as a cross-bank screen**

**Status: RETIRED 2026-08-13, not re-scoped and not silently kept.** Two independent reasons, either sufficient:

1. **Its basis is non-comparable.** The flag reads `v1`, and the item-9 share of the base ran **5.5% → 65.8%** across the cohort at 2026Q2. The flag therefore ranks banks partly by their funding/bucket mix. It is the defect, not a victim of it.
2. **It no longer discriminates.** At 2026Q2 it catches **one** name (WAL 21.20%, falling), and on the uniform basis it catches **none** (cohort max EGBN 10.77%).

**What "retired" means concretely:** no surface may cite a `>20%` MI3 hit as a signal; `v1_pct` stays in the TSV as a continuity column only. **No level was moved** — this flag was never in `THRESHOLDS.tsv`; it lived inside the screen's own recipe, which is why it outlived its own validity without a publisher (`finding_retired_threshold_has_no_publisher`). It is now retired **in writing, with a date and a reason**, where a reader travelling against the link will find it.

## ★ RULING 2 (mine) — **no successor threshold is registered. Spec + base rate only; the numbers go to Will, not the registry.**

Base rate over the 56 scored bank-quarters (2025Q2 · 2025Q4 · 2026Q1 · 2026Q2):

| `v1a` cut | Fires | Rate | Banks that ever clear it |
|---|---:|---:|---|
| >5% | 22/56 | 39.3% | CFG · CUBI · EGBN · MTB · OZK · VLY · WAL |
| >7.5% | 14/56 | 25.0% | EGBN · MTB · OZK · WAL |
| >10% | 9/56 | 16.1% | EGBN · MTB · OZK · WAL |
| >12% | 4/56 | 7.1% | EGBN · OZK |
| >15% | 4/56 | 7.1% | EGBN · OZK |
| >20% | 2/56 | 3.6% | EGBN · OZK |
| >25% | 0/56 | **0.0%** | — |

Distribution: min 0.00 · p25 1.70 · median 4.34 · p75 8.99 · p90 10.77 · max 23.46.

**⚠️ And the reason I am NOT proposing a level off that table — it is the more important finding:**

| Per-bank `v1a` spread across the 4 quarters | |
|---|---|
| **EGBN 10.77 → 23.46 = 12.69pp · OZK 5.46 → 21.83 = 16.37pp** | the two widest |
| Every other bank | **≤ 2.15pp** (WAL 1.31 · MTB 0.88 · CUBI 1.10 · VLY 0.62 · CFG 1.01 · FLG 1.65 · BKU 2.15 · HBAN 1.05 · ZION 0.84 · SSB 0.16 · SBCF/AMTB 0.00) |

**Any cross-sectional level between ~12% and ~20% fires on exactly two banks' own quarter-to-quarter volatility and on nothing else.** That is not a screen, it is a re-description of EGBN and OZK — and it would have been very easy to publish as one, because the base-rate table alone looks respectable at those cuts.

**`n=56` is also not 56 independent observations.** Twelve of fourteen banks move less than 2.2pp across a full year, so the series are strongly autocorrelated and the **effective n is nearer 14** — well short of what a level calibration needs (`finding_base_rate_the_instrument_before_its_event_table`, `finding_cohort_too_small_to_move_the_index`).

**Recommendation of record — "don't build it" is the answer, for now:**
- **Do NOT register a `v1a` level trigger.** ≥25% has fired 0/56 (jointly unsatisfiable on this record); 12–20% is two-bank noise; ≤10% fires a sixth of the time on names nobody calls stressed.
- **The promising successor is a WITHIN-BANK CHANGE instrument, not a level** — e.g. a sustained multi-quarter rise in a bank's own `v1a`, which is what the *original* discovery (classification migration) was actually about. **Data requirement before it can be spec'd: ≥12 quarters** so a change threshold can be base-rated against its own history. The pull is cheap and cached; the quarters are not yet there.
- **Any level, when it comes, goes to Will as a numbers proposal with its base rate and separation attached — never straight into `THRESHOLDS.tsv`.**

## ⚠️ OPEN QUESTION — carried, not solved: does the up-cap finding change the COHORT?

The cohort was selected under **ratio-era priors**: MTB, HBAN and VLY were admitted as *clean large-cap benchmarks*. The 2026Q2 run then found **MTB holding the largest absolute MI3 book in the cohort ($4.95B, ~2× WAL's) and HBAN's dollars up 100% YoY** — i.e. the names admitted as the control group are where the dollars went.

**If the screen's question is "which bank is most concentrated," the current cohort is fine. If it is "where is hidden CRE pooling," the selection rule is measuring the wrong population** and a size-ranked or dollar-ranked frame is the right one (`finding_ranked_head_sample_is_not_the_population` — a cohort chosen by the ranked head of one metric cannot answer a question about a different metric).

**Deliberately not closed this session**, because re-cutting the cohort mid-instrument would silently change what every prior figure means. **Read-path so it cannot rot:** carried on ROADMAP as a dated thread and named in the script header beside `COHORT` (*"do not silently grow the list"*), so the next runner meets the question at the point of temptation. **Decide it before the 2026Q3 run**, so any change lands on a quarter boundary with both cohorts reported once.

---

## 2026-08-27 — CLASS RULING CONSUMED: lagged-publication series grade-date (Will, option (i))

**Record:** `PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md` — Will in-session ~14:0x ET, verbatim *"Approve option (i) as the class ruling - go ahead."* Arrived via PROME 8/27. **Consumed here, not re-derived.**

**The rule.** Where a registered row's criteria name a metric from a lagged-publication series *"on `<date>`"*:
1. **The observation DATED `<date>` governs.** No substitute observation — an earlier print merely *available on* that date does not instantiate the cell.
2. **The grade WAITS for that observation to publish.** The strike time slips to the publication moment; **the referent never moves.** A publication lag is a transport artifact, not a spec term.
3. Non-lagged legs of the same row read at their own time and are **held**, with the grade marked **PROVISIONAL on its face** until the lagged leg publishes.
4. **It is a READING RULE for existing frozen letters, not an edit to any of them.**

**Which REGINALD surfaces this governs — audited 8/27, not assumed:**

| Row / vector | Series | Lagged? | Effect |
|---|---|---|---|
| `REG-T-03` HY OAS >320 | FRED `BAMLH0A0HYM2` | ✅ **T+1** | governed |
| `VX-REG-18.04` CCC/HY >3.6× ×3 consec | FRED `BAMLH0A3HYC` ÷ `BAMLH0A0HYM2` | ✅ **T+1** | governed |
| Claims >300K | FRED `ICSA` | ✅ weekly + lag | governed |
| Funding plumbing SOFR−IORB | FRED | ✅ T+1 | governed |
| 30Y level reads | FRED `DGS30` | ✅ T+1 | governed |
| `REG-T-06` FHLB advances | FHLB OF combined report | ✅ **quarterly, ~30d** | governed — and this is the one with a live forward fire (leg 3, ~Nov) |
| **`REG-T-01` KRE <$60** | yfinance regular-session close | ❌ same-day | **NOT governed** |
| **`REG-T-02` WAL <$78** | yfinance regular-session close | ❌ same-day | **NOT governed** |

⚠️ **The distinction that matters at fire time:** `REG-T-02`'s `value_basis` is *regular-session close* — same-day readable, so it is graded **on the day, at the close, and never off an intraday print**. **The lagged-series rule does NOT license waiting on it, and does NOT license grading it early off a last-trade.** Two different disciplines, opposite directions, and conflating them would be the expensive error.

⚠️ **Practical effect on my consecutive-session counting** (`VX-REG-18.04`): a run counted *"through 8/26"* is legitimate only once the 8/26-dated observation has published — which for a T+1 series is 8/27. **Count dated observations, never "latest available."** *(My 8/27 recount satisfies this: 19 sessions through the 8/26 observation, published 8/27.)*

**Not ruled, and I am not assuming it:** MIDAS's ask ② (observation-date and read-date as two separate registered fields) stays OPEN. Until it lands, `THRESHOLDS.tsv` carries no read-date column and this note is the read-path.
