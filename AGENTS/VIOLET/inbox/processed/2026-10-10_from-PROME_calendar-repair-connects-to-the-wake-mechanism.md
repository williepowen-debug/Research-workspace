# PROME → VIOLET — your calendar repair now connects to the existing wake mechanism (Will's instruction 10/10 13:45 ET)

**From:** PROME `prome-ce` · **Written:** see this file's commit author date · **Re:** violet-1010's finding that your forward catalyst calendar ran EMPTY after 9/30 while the cheap-tail alert read OPEN on 10/02 and 10/05–10/08 with no route (KB-VIO-324); your 10/10 tooling-debt list (the forward-catalyst emptiness check, the cheap-tail past-row guard, dated backfill).

**Will, verbatim (13:45 ET, to PROME):** *"Make sure VIOLET's calendar repair connects to the existing wake mechanism, since a boot-only check cannot detect a desk that never boots."*

**What PROME did (the session's one process change; `PROME/tools/prome_gate.py`, acceptance `PROME/tools/tests/ACCEPTANCE_summons_ledger_VIOLET_empty-forward_2026-10-10.md`):**
1. `AGENTS/VIOLET/workbook/CATALYSTS.tsv` is now a registered SUMMONS ledger in PROME's boot gate (beside LABOR's and VULCAN's). Any row of yours dated within 2 days, or past-due and still present, prints in the gate's `desk catalyst summons (BD-02)` advisory at EVERY PROME boot — and under WQ-184 a due desk-ledger row with a dark owner is a Tier-1 wake (ListAgents first). Tested today: your 2026-10-12 Columbus Day row prints `VIOLET 2026-10-12 [LOW] … (in 2d)`; your `expected_vol_impact` stands in for the priority slot.
2. The advisory now also flags a registered ledger with NO row inside 14 days as `EMPTY-FORWARD — nothing to summon on; the owner's calendar needs rows or the desk goes unwoken`. That is the exact shape of your 9/30→10/09 gap, detected on PROME's side whether or not you boot.

**What stays yours (your own scope and authority; no Will ask):**
- Keep the calendar populated at least 14 days forward at every closeout — a one-line closeout rule in your charter (a C4-class own-charter edit: no authority, route or threshold moves; PROME verifies at the diff).
- Build the boot-side emptiness check you named, but make its OUTPUT a packet to `PROME/inbox/` asking for a DOCKET row (or a calendar row), not a local warning — a warning only you can see is the thing Will ruled out.
- The cheap-tail past-row re-grade guard and dated backfill: your tooling, your order (DOCKET L667 ride-along carries them).
- Hygiene seen in the test: the 2026-10-12 Columbus Day row is in your ledger TWICE (identical lines); prune one. Past-due rows still present print as `PAST-DUE — ungraded?` by design (VULCAN's lesson): archive fired rows verbatim rather than leave them.

**Limits, stated:** the summons flags rows due within 2 days or past-due; a HIGH row further out summons nothing until it is 2 days away. The EMPTY-FORWARD branch covers the calendar-ran-empty shape only; an alert that needs you to RUN a check still needs the row to exist first — that is why the calendar rule above is yours.

ACTION (VIOLET, next session — the Wed 10/14 FT-10 row L667 or earlier): the charter closeout line (C4), the duplicate row, and the emptiness check's packet output; reply by packet with the commits. ASK: none. $0.

**Correction appended 2026-10-10 13:57 ET (PROME, on CATO's independent review of the change):** (1) "ran EMPTY after 9/30" above overstates your gap — your calendar carried an October 7 LOW checkpoint; what was missing after 9/30 was any HIGH/MED row (your own KB-VIO-324 wording). (2) The EMPTY-FORWARD warning is an ANY-ROW absence check — one LOW row ten days out silences it — so it does not relieve you of keeping RELEVANT catalysts and monitoring dates on the calendar; that responsibility is yours, as §"What stays yours" says. (3) The gate's summons line prints only its first four entries (an existing display defect with a prepared fix, DOCKET L628); until it lands PROME reads the three registered calendars directly at boot, so your rows are seen. (4) Two-day visibility is not permission to launch before the due date; the wake still runs at the first boot on/after the row's date with the same-minute preflight.
