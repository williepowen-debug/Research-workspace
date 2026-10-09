# ACCEPTANCE — WQ-382 (a) encode: the Deck Owed page's reference link carries the HOSTED reference build date (written BEFORE the edit, 2026-10-08 20:12 ET, PROME prome-07)

**Ruling encoded:** WQ-382 (a), Will 2026-10-08 20:09 ET, verbatim *"WQ-382 AI pproved"* on the block *"Recommendation B: republish it only on your word or at a spine audit, and add a 'built <date>' warning beside its link so a stale page reads as stale."* Scope = the Deck REFERENCE page only; the 10/7 widening to the Helm and Fleet-Ops is (b), still Will's.

## Acceptance conditions (properties, in the defect's terms — the defect: a stale hosted page reads as current because its link carries no date)
- **AC1 ordinary:** with `PROME/state/deck_reference_hosted.json` present and well-formed ({"artifact","version","built",...}), the Owed page's nav link reads `Reference: Decided · In-flight · Docket — hosted build <built> (<version>); refreshes on Will's word or at a spine audit`.
- **AC2 missing information:** with the state file absent, unreadable or malformed, the link reads `… — hosted build UNKNOWN (state file missing or unreadable); refreshes on Will's word or at a spine audit` — visible on the page, never silent, never a build crash.
- **AC3:** the reference page's own text and its "Back to Owed decisions" link are byte-for-byte unaffected by the state file; the Owed page's `rulings` store and every other panel unchanged.
- **AC4:** `PROME/tools/tests/test_decision_deck_split.py` passes unchanged, plus one new test covering AC1 and AC2 through the helper `_hosted_reference_note(path)`.
- **AC5:** the state file is written ONLY by the sitting that republishes the reference (CLOSEOUT step 11 text says so); the build only reads it.

## Neighbours (WQ-229 — considered, not performed where N/A)
- ordinary → AC1 · missing information → AC2 · overlap → the Helm's "Decision Deck →" link (`will_handbook.py`) points at the OWED page, not the reference: unaffected (checked by grep, no edit) · wrong owner → N/A: PROME owns the tool, the state file and the publish receipt · concurrent activity → N/A: a single reader of a file no other process writes.

## States at commit
IMPLEMENTED · TESTED (the new test + the existing suite + a local preview build) · INDEPENDENTLY VERIFIED: NO (a small self-contained tool change; no reader commissioned) · STILL UNRESOLVED: (b) the Helm/Fleet-Ops extension is Will's.
