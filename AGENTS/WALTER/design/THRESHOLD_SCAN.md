# WALTER Threshold Scan v0.49

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

   Append fire row to `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` (5-col schema: trigger_id / fired_date / metric_value_at_fire / dispatched_signal_id / sustain_confirmation — per JOINT_PROPOSAL §2.4, preserves Critical Rule #2 by keeping fire-history out of RED's tree). Approaching-threshold (within 5% one-sided per `threshold_op`) flagged in WALTER closeout SESSION LOG as "near-trigger watch", not auto-dispatched. Stale-fire suppression: for exit-carrying rows, apply the STATE RULE above and the current owner exit. The elapsed `sustain_window` heuristic must never suppress a new cycle after a registered exit, or re-fire an ongoing fired state.

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
> ✅ **HOW TO TEST CONTRACT IDENTITY — the method is part of the rule, because two obvious methods FAIL:** use the current `fetch.py` Python function `contract_probe(root)` output (there is no probe CLI subcommand) with a negative control and its explicit refusal/staleness status. **`expireDate` is absent on this vendor metadata path; it cannot be a required field.** A parsed metadata month/year can identify a contract only when actually supplied; truncated names (notably Brent) may leave identity unresolved. **Do not infer identity from a ticker or matching price alone.** Capture `resolved_symbol`, identity basis and quote timestamps; a stale/ambiguous/refused probe remains UNRESOLVED. The probe’s 900-second freshness limit remains uncalibrated; implementation is not consumer acceptance. **This binds the `CL=F` / `BZ=F` / `HO=F` pulls THIS STEP makes.**

> 🔴🔴 **v0.44 — NAME THE AXIS, AND SIZE THE SLOPE BEFORE YOU SPEND ATTENTION ON IT.** *(BRENT, reproduced at its own instruments; the numbers below are BRENT's own pull, NOT relayed from HENRY.)*
>
> **⚠️ THERE ARE THREE INDEPENDENT ROLL AXES AND A ROW CAN BE EXPOSED TO ANY SUBSET. "NOT EXPOSED" WITHOUT NAMING WHICH AXIS IS A FALSE-CLEAN:**
> **(i) CROSS-SERIES MISMATCH** — the two legs sit on different months. *(Fixed by the identity check above.)*
> **(ii) WITHIN-SERIES STEP ACROSS A LOOKBACK** — a roll falling inside an N-period window makes a **one-off jump read as a CHANGE.** **Hits NET-CHANGE / Δ rows, which the identity check does NOT protect** (both legs can be perfectly matched on every observation and the series still jumps at the roll).
> **(iii) FIXED-LEVEL ON A SLOPING CURVE** — the 3d hazard above. **Hits LEVEL rows. Does NOT hit net-change rows**, because a slope common to both endpoints differences out.
> 🔑 **BOUGHT BY BRENT CATCHING ITS OWN OVER-BROAD CLEARANCE: it annotated a row "MATCHED AND NOT EXPOSED", which cleared axis (i) only and READ AS CLEARING THE ROW** — that row grades on a t−4 net-change basis and `HO=F` rolled INSIDE the live window, so it was exposed on (ii) throughout. ⇒ **write the axis, never the verdict alone.**
>
> ⭐ **AND THE (iii) HAZARD IS NOT UNIFORM — MEASURE THE TERM-STRUCTURE SLOPE, DO NOT ASSUME IT.** **CRACKS are steep** — matched ULSD crack, BRENT's pull: **Oct 107.29 · Nov 102.88 · Dec 98.30 · Jan 96.33**, steps **−4.41 / −4.58 / −1.97** ⇒ **naming the month is CRITICAL** (one step ≈ 94% of `HEN-46`'s threshold gap). **WTI–BRENT is nearly FLAT** — **Nov −8.89 · Dec −8.59 · Jan −8.23**, steps **+0.30 / +0.36** ⇒ **month-basis specification is NEAR-IRRELEVANT there; any consistently-matched month lands within ~\$0.30.**
>
> ⇒ ⛔ **DO NOT APPLY (iii) UNIFORMLY ACROSS EVERY SPREAD ROW.** **Spend the month-naming requirement where the slope earns it — the crack rows (#6, #8).** ⚠️ **A check applied where its effect is \$0.30 costs attention on rows that do not need it, and a requirement that cries wolf stops being read** — which is how the ones that DO matter get skipped. **The MATCHING requirement (i) stays universal; only the month-NAMING burden is slope-scaled.**
>
> ⚠️ **TWO DESKS, SAME SHAPE, DIFFERENT ABSOLUTE LEVELS — RECORDED, NOT SMOOTHED (third instance today).** BRENT's matched Oct **107.29** vs HENRY's **107.72**; Nov 102.88 vs 103.15; Dec 98.30 vs 98.36; Jan 96.33 vs 96.60. **\$0.06–\$0.43 apart, same direction, same magnitude class.** 🔑 **The FINDING is the step size (~−\$4.5/month) and both desks agree on it; the LEVELS are their own and HENRY owns the series.** **Do not average them into a figure that matches neither.**

> ⚠️ **v0.45 — BEFORE NAMING A MECHANISM FROM A CURVE, EXTEND THE SAMPLE PAST WHERE IT TURNS.** *(BRENT, self-reported against itself.)* **FOUR POINTS ON THE DESCENDING LIMB OF A SEASONAL V LOOK EXACTLY LIKE A LINEAR DRIFT**, and the drift reading produced a confident and WRONG mechanism (“a one-time scheduled fire”) on an UNPROVEN crossing conclusion. **The extended snapshot shows a winter trough near the bar and a recovery of about $14; the sampled minimum remains above $30. It does not prove a crossing or annual recurrence.** 🔑 **The refuting measurement was ONE MORE LINE OF THE SAME COMMAND ALREADY RUN** — the cost of extending was ~zero and the cost of not extending was a wrong mechanism handed to two desks. ⇒ **when a monotone run of 3–4 points is about to become a MECHANISM, pull further until it turns or demonstrably does not.** 📌 **Applies directly to this step's near-trigger reporting: a “N% away and closing” line is a mechanism claim, not just a distance.**
>
> ⚠️ **A THIRD FAILURE MODE, DISCLOSED: `NO INSTRUMENT` ≠ `NOT MET`.** Boundary #5 is specified in **Worldscale** and this fleet has never had a Worldscale feed (the `VLCC > WS200` line was retired 2026-07-31, Will-ruled F4, for that reason). ⇒ **WALTER must never invite an owner to "fire it if your pull clears it" on a row whose instrument does not exist** — that manufactures a fire path and invites instrument substitution (`BWET` is a freight-futures ETF, not a route rate). **Report an uninstrumented row as UNINSTRUMENTED so the gap stays COUNTABLE** — the same treatment `HANS-T-12` already gets at boot 6b.

<!-- End of authoritative Phase 2 step 7. -->
