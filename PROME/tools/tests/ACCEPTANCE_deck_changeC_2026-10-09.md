# ACCEPTANCE — Decision Deck Change C: the overview package (WQ-407 RULED A, Will 2026-10-09 18:48 ET)
**Written BEFORE any edit** (WQ-229; `decision_deck.py` is at its two-correction stop from the Change B episode — this file opens a NEW episode with its own reads). **Owner:** PROME (`prome-15`). **Ruling:** WQ-407 A verbatim *"WQ-407 A approved"* — both a compact TABLE and a tile GRID behind one view toggle, sharing a PEEK panel; named saved views; sorts; the five-card trial decides the default view. Basis: CATO research (9cb87fdb5) + PROME brainstorm; Change A (options) and Change B (chips/pins/fronts/pipeline) preserved.

## Acceptance conditions

**AC-C1 — three views, one toggle.** The Owed panel gains a view switch `List · Table · Board`; List is today's page unchanged; the selection persists per viewer (localStorage, try/catch); default = List until the five-card trial picks otherwise.

**AC-C2 — the table.** One row per card: WQ · Pin · Title · Who acts (the ruled group: you / hands owed / waiting) · Type chip · Deadline (the pill's text, clock included) · Open since. Click a column header sorts client-side (due date default; WQ#; open-since); click a row opens the PEEK. Rows honor the active chip filter and pinning exactly as cards do (pinned rows always visible, sorted first on the due sort).

**AC-C3 — the grid.** One compact tile per card: WQ · PINNED flag · due pill · kind · title (clamped). Click opens the PEEK. Same filter/pin behavior. ≥3 columns desktop, 2 phone.

**AC-C4 — the PEEK is the REAL card.** Opening a card in Table/Board relocates the card's EXISTING DOM node into the peek container (wide: beside the overview; narrow: full-screen overlay) and returns it to its exact slot on close — NEVER a copy, so every Change A/B behavior (tap buttons, option terms, tapstate updates, tint) works identically inside the peek; ←/→ (and on-screen arrows) move through adjacent cards in the current view's order; Esc/close returns without losing scroll position.

**AC-C5 — saved views.** Three named presets as one-tap buttons: `Everything` · `My action today` (pinned + due-today/overdue only) · `Waiting on others` (the blocked group). A preset is a filter state, never a data change; pinned cards remain visible in every preset except that `Waiting on others` is itself an explicit whole-group view (the one ruled place a pinned card of ANOTHER group is absent — stated on the button's title).

**AC-C6 — nothing regresses.** Change A option fragments byte-identical to the live baseline; Change B chips/pins/fronts/pipeline untouched in List view; the store write path unchanged; the reference page untouched; blank-deck and options-mismatch refusals intact; existing selftest/pytest/harness all pass, extended with: view-toggle persistence; peek relocate-and-return (same node identity, listeners intact); table sort order; preset filters never hide a pinned card (except the stated Waiting view).

**AC-C7 — folded Change-B residue (bounded).** DP6: the stage-② line when `recorded_as` renders keeps a four-word receipt reminder ("recorded — execution per that line"); DP8: WQ-375's A/B definitions marked at SOURCE in the sidecar (⚠️ caveat marker) so the card unfolds whole — no generator logic change for DP8.

**Out of scope (named):** DP5 figure-evidence (assignment item 5 — the NEXT episode, owed) · DP7 clock bounding beyond Change B's Needed-by rule · custom user-named views · tile tint sync with live tapstate (declared residue) · list-view re-sorting (its order stays the ruled server order).

## Neighbours (WQ-229)
- **Ordinary:** AC-C1–C7. **Overlap:** the peek relocation must not fight the minimize-memory (`deck.min.*`) or the chip filter's `chiphide` (a peeked card ignores both while peeked, restores after). **Wrong owner:** none — render-only; option terms untouched. **Missing info:** a view/preset saved for a chip that no longer exists falls back to defaults (same as Change B's stale-chip rule). **Concurrent:** old store docs and live taps unaffected (no write-path change); a tap taken INSIDE the peek behaves identically (same nodes).

## Verification plan
selftest (extended) → pytest → node harness (extended: peek node-identity case, preset-pin case, toggle persistence) → build → fragment diff vs live baseline → independent Opus read(s) to ❌ = 0 (ceiling 3) → republish → records.

## Closing section (2026-10-09 ~19:1x ET, prome-15 — written BEFORE read 3 so the final read grades the as-shipped contracts)
**State at this write: IMPLEMENTED · TESTED (26 pytest + 33 subtests + the extended node harness incl. production-handler key-guard/min-restore/blank-fallback cases + the selftest — count per its own run, never this line) · read 3 PENDING (the ship gate).** Episode: read 1 (coldread-deckC) 7 ❌ · 8 ⚠️ → all 7 fixed + ⚠️9–12/14; read 2 (coldread-deckC2) verified all seven closed with its own counterexamples, found 1 NEW ❌ (the fix pass hardcoded "12 pinned" into the blank-view note — the false-count class again) · 9 ⚠️ → the ❌ fixed (note built live, preset-aware, no baked number) + ⚠️3/⚠️8.

**AC re-cuts (supersede the text above):**
- AC-C2: the Open-since column does NOT sort — its values are month/day strings with no year (read-1 ❌1); the header says so in plain words. Sorts = Deadline (default; pinned-first by the FILTER's pin, build pin + live due-date top-up) and WQ# (plain ascending; the th title says pinned-first applies on the Deadline sort only).
- AC-C3: phone = exactly 2 columns under 560px (media rule), not minmax flow.
- AC-C4: the peek is an overlay DRAWER at every width (read-1 ⚠️13), not a side panel at desk widths; a view switch always closes it (read-1 ⚠️12); arrow keys never fire while the target is an INPUT/TEXTAREA/contentEditable (read-1 ❌3); a minimized card restores minimized on close (read-1 ❌4).
- AC-C5: a saved view that would open BLANK falls back to Everything WITHOUT overwriting the saved preset (read-1 ❌5); the blank state, when reached by live filtering, shows a cause-naming note with LIVE counts; the Waiting exception is stated in the visible chipnote, not only a tooltip.
- AC-C7/DP6 text as shipped: " — execution follows that record, never the tap itself" (substance per the AC; wording differs — recorded here per read-1 ⚠️8/read-2 ⚠️2).
- Deep links under a saved Table/Board open the card in the PEEK (read-1 ❌6); blocked/nonexistent hash targets no-op safely (read-2 CE-verified).

**Declared residue (not fixed):** r2-⚠️4 the minimize round-trip edge (expand-inside-peek then close restores the PRE-peek min state until reload; aria-expanded stale after openPeek's expand) · r2-⚠️5 SELECT targets and Alt+arrow combos still step (no selects exist on the page today) · r2-⚠️6 arrows from a filtered-out peeked card jump to the first in view · r2-⚠️7 no harness case for the deep-link peek, closePeek heading recount, or the empty-note render (read 2 verified them by counterexample) · r2-⚠️9 the blank-view fallback is load-time only and the next chip click saves preset 'all' (defensible; noted) · r2-⚠️10 blocked rows/Waiting render exercised only by the node fixture · r1 carried: chip counts read as result size (chipnote discloses); kind_chip brittleness; the today-preset makes chips no-ops (implied by pinNow); no focus move into the peek; the spawn brief said "two caveat markers" where the sidecar delta marks one row (375 — the 401 marker rode the Change B commit). READ-3 ADDENDA: the from-blank Everything tap now resets the chip too (the one post-read-3 ❌-only edit; read 3 verified every other fix closed) · r2-⚠️6's second half (openPeek's bare 'WQ-n' position wording vs refreshPeekPos's) stays residue · AC-C6's "reference page untouched" holds for the BODY only (the shared JS rode along) · this closing section was graded at the FILE by read 3 (untracked at the diff freeze, ⚠️5) · read-3 ⚠️2's latent note branches are covered by the chip-reset edit.

