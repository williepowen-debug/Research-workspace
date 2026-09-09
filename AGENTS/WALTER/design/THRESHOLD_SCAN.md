# WALTER Threshold Scan v0.41

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

<!-- End of authoritative Phase 2 step 7. -->
