# WALTER Threshold Scan v0.43

**This file is the authoritative CHECKLIST Phase 2 step 7 procedure. Read it WHOLE at boot step 6c and when executing Phase 2 step 7 at dispatch.** The registry-loading step is CLAUDE.md 6b; current instrument basis, sustain, state and exit come from the owner registries, not dated examples below. Read current values on their registered observation schedules and label each observation date. Boot includes the four registered owner families and Cushing as specified by CLAUDE.md 6b/6c.

Split 2026-09-08 from `SIGNAL_PROCESSING_CHECKLIST.md`, Phase 2 step 7, verbatim. The dated August 22 example below is historical, including its "LIVE NOW" sentence; it is not today's WAL grade. The STATE RULE governs exit-carrying triggers, rather than suppression by elapsed sessions alone. Proximity alone is not an automatic fire dispatch; decision-changing information follows BOARD_CONSUMPTION_SPEC §3.5.3 as before.

Size re-trigger: measure after any append and every Tier-2; next calendar check 2026-09-30. Keep the procedure and all active obligations on this read path; place new incident narrative in `history/`, with an evidence pointer here. Version stays in lockstep with the parent CHECKLIST.

7. **Falsification-trigger auto-fire scan.** Before final dispatch session-end, scan `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` for any thresholds that crossed during the current session per JOINT_PROPOSAL_2026-05-06_red_walter §2 eval logic (read-loop step 6b in WALTER spawn-protocol; sustain-window check, threshold evaluation, last-fired suppression via `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`). For each sustained cross: auto-generate falsification-derived signal with:
   - `signal_type: threshold-crossed`
   - `falsification_trigger: <RED-FT-NN>` body field
   - Action recipient = `trigger.recipient_chain.action`
   - Info recipients = `trigger.recipient_chain.info`
   - Precedence per `trigger.action` enum (IMMEDIATE-FALSIFY → IMMEDIATE / PATH-B-CONFIRM → PRIORITY / ADD-POSITION → IMMEDIATE / etc.)
   - dispatch_note carrying trigger_id ref + current vs threshold value + sustain confirmation count + falsification_thesis_ref pointer
   - Cluster per metric (HY-OAS → BANK_COLLATERAL, BRENT-PAPER → IRAN_HORMUZ or HYDROCARBON_INFRA per state, INITIAL-CLAIMS → CONSUMER_STAGFLATION, VIX → POSITIONING_VALUATION, CCC-OAS → BANK_COLLATERAL)

   > 🔴🔴 **STATE RULE — ADOPTED 2026-08-22 (REGINALD's wording, PROME-endorsed, WALTER's file and WALTER's call per the packet). A TRIGGER WITH AN EXIT CONDITION IS A STATE MACHINE, NOT AN EVENT COUNTER.**
   >
   > **> Trigger fire STATE is graded against the INSTRUMENT — close-by-close against the registered trigger AND its registered exit — never inherited from a board summary. Closes inside a fired state are RE-ENTRIES, not fires.**
   >
   > 🔑 **BOUGHT BY A BOARD THAT WAS WRONG IN BOTH DIRECTIONS AT ONCE.** On 8/20 WALTER's live board carried **"ZERO FIRES"** for `REG-T-02` **and** *"still between fire and exit."* **Both false, in opposite directions.** REGINALD's ruling of record graded it: **FIRED 2026-05-11 at 76.95** (WALTER's own 7/27 claim was correct) · **8 further sub-78 closes 5/12→6/03 were RE-ENTRIES INSIDE the fired state, not 8 fires** · **EXIT MET 6/30** (`WAL ≥81.90` on 3 consecutive closes: 6/26 82.05 · 6/29 82.88 · 6/30 82.20), satisfied twice more since as no-ops. **Ruled state token: `REG-T-02: UN-FIRED (exited 2026-06-30; prior cycle 2026-05-11 → 2026-06-30)`.**
   >
   > ⚠️ **NEITHER board statement was a reading of the tape.** Both were artifacts of a fire-ledger that recorded **neither the fire nor the exit** — and **a ledger that can be simultaneously wrong in both directions will do it again on a different trigger.** ⇒ **the fix is to grade at the instrument, not to correct the summary.**
   >
   > ✅ **OPERATIONAL CONSEQUENCE, LIVE NOW: a `WAL` close <78 from 8/21 onward is a FIRST FIRE OF A NEW CYCLE — fresh signal, full `V1V3-ACCELERATE` chain (REGINALD / WAL / Will), NO duplicate suppression.** Subsequent re-entries inside that new fired state ARE suppressed. **8/21 close: $79.67 — 2.1% above the line, un-fired.**
   >
   > 📌 **Generalises to every exit-carrying row on the board** (`RED-FT-01`/`-06`/`-07`/`-09`/`-10`, `REG-T-*`, `CREED-T-*`): **read the exit column before reporting a state, and report the STATE, not the last event.** `[[finding_record_of_an_action_is_not_the_action]]`

   Append fire row to `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` (5-col schema: trigger_id / fired_date / metric_value_at_fire / dispatched_signal_id / sustain_confirmation — per JOINT_PROPOSAL §2.4, preserves Critical Rule #2 by keeping fire-history out of RED's tree). Approaching-threshold (within 5% one-sided per `threshold_op`) flagged in WALTER closeout SESSION LOG as "near-trigger watch", not auto-dispatched. Stale-fire suppression: skip a trigger if it fired within prior `sustain_window` sessions per the ledger.

> 🔴🔴 **CROSS-SERIES ROLL DESYNC — added v0.42, 2026-09-14 (BRENT's finding, verified at HENRY's artifact; canon `AGENTS/BRENT/demand_destruction/TRACKER.md` § CONTRACT-ROLL CAVEAT).**
>
> **ANY threshold or boundary defined as a SPREAD between two continuous front-month tickers can be wrong while BOTH legs are individually correct and current.** Continuous tickers roll **independently**, so a spread silently becomes *one month's product minus another month's crude*.
>
> **The instance:** `HO=F` and `RB=F` rolled Oct→Nov on **2026-09-14**; `CL=F` did not (Oct, expiry ~9/22). The continuous ULSD crack printed **−\$9.90 (−9.1%)** — read across the fleet as a collapse. **On matched October contracts it was 108.24 → 107.45 = −\$0.79 (−0.73%). ~93% of the move was the roll.** A falsifier (`HEN-46` F1, crack <\$95) **could have fired on the artifact.**
>
> ⛔ **THE TRAP IS THAT EVERY SANITY CHECK PASSES.** Both legs are live, current, correctly labelled and plausible; the magnitude is in-range. **There is no error to notice** — `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.
>
> ⛔ **DO NOT KEY A FIX TO A DATE.** A continuous series rolls on **VOLUME MIGRATION, not expiry** — the product legs left **16 days before** their October legs expired. Product legs expire ~the 30th, WTI ~the 20th, leads are contract-specific ⇒ **the desync is STRUCTURAL and recurs EVERY month. There is no date after which this is safe.**
>
> ✅ **ACTION AT THIS STEP: resolve BOTH legs to their DATED contract month on EVERY pull, and state the months beside any spread figure.** If the months differ, the spread is **NOT GRADEABLE** — report `MONTHS MISMATCHED`, never a number. This binds every spread-defined row (Boundary #6 and #8, any crack, any basis) **and the `CL=F`/`BZ=F`/`HO=F` pulls this step makes.**
>
> 📌 **THIS IS A NEW FORM OF `ADD#23`, NOT AN INSTANCE OF IT.** ADD#23 (`anchors/IRAN_WAR_GUARDS.md`) kills differencing **ONE** series across **ITS OWN** roll — temporal. **This is TWO series rolling at DIFFERENT times, differenced against each other — cross-sectional.** A desk that has correctly internalised ADD#23 is **not** protected against this.
>
> 🔴🔴 **AMENDED SAME SESSION — v0.43. THE MATCHED-MONTH CHECK ABOVE IS NECESSARY AND *NOT SUFFICIENT*, AND ON ITS OWN IT REPORTS CLEAN ON A READING THAT CAN BE OFF BY A WHOLE THRESHOLD BAND.** *(HENRY artifact, credited to TERRY with REGINALD provenance, verified at HENRY's own pull. I encoded v0.42 off a peer's MESSAGE; the owner's ARTIFACT had already moved further — the same defect one layer down.)*
>
> **THERE IS A THIRD ROLL FORM AND THE IDENTITY CHECK DOES NOT CATCH IT: a PERFECTLY MATCHED crack still steps DOWN as the contract month advances.** ULSD crack by matched month [9/14 close]: **Oct 107.72 · Nov 103.15 · Dec 98.36 · Jan 96.60** — mean **−\$3.71/month**. 🔑 **`HEN-46`'s two thresholds are \$4.84 apart and ONE roll step is \$4.56 = 94% of that** ⇒ **a single roll can carry a series nearly stand-down→dead with ZERO change in the underlying margin.** ⚠️ **An unadjusted continuous series is a SAWTOOTH, not a glide path** (down-jump at the roll, drift back between) — **the hazard is observing at the wrong point in it.**
>
> ⇒ **MATCHED MONTHS MAKES A SPREAD COMPARABLE TO ITSELF, NOT TO A FIXED THRESHOLD.** **State WHICH month a spread level is on whenever it is graded against a registered number, and never compare a level on one matched month to a threshold calibrated on another.**
>
> ⚠️ **HENRY'S OWN OPEN CAVEAT TRAVELS WITH THIS AND MUST NOT BE DROPPED: the claim that roll steps "roughly cancel over a cycle" is UNVERIFIED and may UNDERSTATE the hazard** — the only observable window contradicts it, and expired legs are delisted here so past cycles cannot be reconstructed. ⇒ **treat the roll hazard as AT LEAST one step (−\$4.56); do NOT assume self-cancellation.** ⛔ **HENRY deliberately did NOT choose a remedy — every available fix moves its own line in its favour, so it is being settled OUTSIDE the read window, with Will. This step reports the hazard; it does not re-spec anyone's letter.**
>
> 🔴 **SCOPE IS WIDER THAN v0.42 SAID: THE EXPOSURE IS "ANYTHING WITH A WTI LEG", NOT "anything RB-based."** **Both products AND Brent rolled to November; `CL=F` is the odd one out** (`BZ=F` expire 2026-10-01 == `BZX26`, a legitimate November front, NOT a fallback; `CL=F` expire 2026-09-22 == `CLV26`). ⇒ **Brent–WTI spreads taken from the two continuous tickers are ALSO mismatched** until `CL=F` rolls — **a volume event, NOT the 9/22 expiry, which is only an UPPER BOUND.**
>
> ✅ **HOW TO TEST CONTRACT IDENTITY — the method is part of the rule, because two obvious methods FAIL:** use **`expireDate` PLUS a negative control.** ⛔ **NOT `shortName`** (truncates) and ⛔ **NOT price identity** (cannot separate same-contract from a fallback). **This binds the `CL=F` / `BZ=F` / `HO=F` pulls THIS STEP makes.**

> ⚠️ **A THIRD FAILURE MODE, DISCLOSED: `NO INSTRUMENT` ≠ `NOT MET`.** Boundary #5 is specified in **Worldscale** and this fleet has never had a Worldscale feed (the `VLCC > WS200` line was retired 2026-07-31, Will-ruled F4, for that reason). ⇒ **WALTER must never invite an owner to "fire it if your pull clears it" on a row whose instrument does not exist** — that manufactures a fire path and invites instrument substitution (`BWET` is a freight-futures ETF, not a route rate). **Report an uninstrumented row as UNINSTRUMENTED so the gap stays COUNTABLE** — the same treatment `HANS-T-12` already gets at boot 6b.

<!-- End of authoritative Phase 2 step 7. -->
