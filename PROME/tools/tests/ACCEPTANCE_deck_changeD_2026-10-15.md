# ACCEPTANCE — Decision Deck Change D: the ruling colour follows the card into every view (2026-10-15)

**Ask (Will, 12:02 ET 10/15, verbatim):** *"After I approve or decline there is no visual Q on the board/table/list etc. Can we make it so the decisions that I have already decided on turn green or red so that I know that it has been ruled and can at a glimpse see which direction I ruled (by color)?"* (screenshot: the Board view, no tint on any tile).
**Defect in the defect's terms:** the ruling tint (`ruled-approve` / `ruled-decline` / `ruled-later` / `ruled-choice`) is applied to the `.card` node only (`setState`, `decision_deck.py` ~L1345). The Board tiles (`.ovtile`) and Table rows (`.ovrow`) carry no state, so a ruled decision looks identical to an unruled one in the two views Will uses most; in the List view the tint is a faint background with no label.
**Written BEFORE the edit (WQ-229).** Class: DOMAIN (Will's operator surface, his direct instruction); consequential (Will-facing) ⇒ an independent reader BEFORE it is called fixed.

## Conditions
- **D1 — Mirror:** every tap state the page renders for a card (from the store snapshot: unconsumed AND consumed documents, and a fresh tap) is mirrored to the tile and the row with the same `data-wq`: the same `ruled-*` class, chosen by the SAME latest-timestamp rule the card uses (`TINT_TS`), never by iteration order.
- **D2 — Colour:** approve and choice = green tint (`--tint-ok`), decline = red tint (`--tint-no`), later = grey (`--tint-later`) on tiles (background + border) and rows (cell background); readable in both light and dark themes using the existing tokens — no new colours.
- **D3 — Label:** each tile, row AND card rail carries a small pill that says what was ruled — `RULED APPROVE` · `RULED DECLINE` · `RULED <label>` for a choice · `LATER` — hidden until a state exists. Colour alone is never the only cue (the label carries it for colour-blind reading).
- **D4 — Nothing baked:** the rendered HTML carries only hidden placeholders; no ruling state is written at build time (the store is the truth; the page learns it at load). A document that fails to parse or an `err` state removes the mirror classes as it does on the card.
- **D5 — No regression:** `decision_deck.py --selftest` PASS; `tests/test_decision_deck_split.py` PASS (incl. the runtime cjs); the filters, presets, sort, peek and tap writes are untouched; tile/row counts unchanged; the Reference view is untouched.

## Neighbours (WQ-229 five categories)
- ordinary: one ruled card, three views — D1–D3.
- overlap: a card with several units (Change A) — the card tint already follows the latest unit by ts; the mirror takes the card's resolved class, so units cannot disagree with the tile.
- wrong owner: a document whose `wq` has no tile/row (e.g. a done row still in the store) — `querySelectorAll` returns nothing; no throw (the card path already guards `if(!card) return`).
- missing information: a document without `ts` — the existing `t = ts || ''` rule applies; label falls back to the verdict word.
- concurrent activity: a tap while a view filter hides the tile — the class is set on the hidden node and shows when the filter changes; no re-render needed.

## Reads
- Plan read: this file (the acceptance) — the diff is small; the independent reader reads the DIFF + the rendered page's `setState` and the three templates against D1–D5 and devises ≥1 counterexample of its own. Result recorded below.
- Result: (pending)
