COLDREADER · PROME/tools/tests/ACCEPTANCE_deck_changeD_2026-10-15.md (+ changeD.diff + decision_deck.html) · 3531 B (acceptance; wc -c) · 28 claims
SCORE: 19/28 ✅ · 8 ⚠️ · 1 ❌
❌ 15 D4 "A document that fails to parse … removes the mirror classes as it does on the card" — acceptance L11 says exactly that; the code has no such path: the only removal branch is `} else if (cls === 'err') { … mirrorRuling(card, …, null, null); }` (diff L68 / page L429), and `'err'` is emitted ONLY by the write `.catch` (page L~506 `setState(did, 'err', 'Not recorded (' + c + ')…`). The snapshot path (page L442–462) never calls setState with 'err'; a doc with no verdict falls through both branches and leaves whatever class is there. Consequence low (the card behaves the same — so "as it does on the card" is true and "fails to parse" is not).
⚠️ 10 D2 "readable in both light and dark themes using the existing tokens — no new colours" — the RULE's own two clauses collide: dark tokens give tint-vs-surface contrast of 1.015 (ok #182521 vs #1A2321), 1.03 (no), 1.019 (later); light 1.10/1.13. In dark theme an APPROVE tile is the same colour as an unruled one; the pill alone carries Will's "at a glimpse". Stranger needs: which clause wins.
⚠️ 12 D3 "Colour alone is never the only cue" — met (pill), but the pill is `color:#fff` on --ok/--crit/--wait: light 5.25/6.56/4.92, dark 2.20/2.93/2.26 (<4.5). Precedent exists (.pill.crit same pattern), so not new — but the label is low-contrast in exactly the theme where the tint vanishes (claim 10).
⚠️ 13 D2/D3 enumerate four verdicts (approve·decline·later·choice) — COUNTEREXAMPLE 1: the page renders a fifth, `data-v="DONE"` ("Done — hands complete", WQ-187 and WQ-31). v='done' → class `ruled-done` (0 CSS rules in the page) → no tile/row/card tint; pill class falls to the default `rl-ok` → green "RULED DONE". `ruled-done` is also absent from RL_CLASSES and the card's remove list, so it is never removed (invisible today). Will's "turn green or red" is not met for a DONE tap; the conditions are silent on it.
⚠️ 16 D4 err "removes the mirror classes as it does on the card" — met as written; COUNTEREXAMPLE 2: card ruled APPROVE from the store (TINT_TS=T1), then a NEW tap fails (offline/permission) → `err` strips tint + hides the pill in all THREE views while the store still holds the T1 ruling; TINT_TS is not reset, so it reappears only if a later snapshot event fires. Change D widens a pre-existing card behaviour to the Board/Table; the ambiguity is the RULE's ("as on the card").
⚠️ 19 D5 "filters, presets, sort, peek and tap writes are untouched" — true of those, but COUNTEREXAMPLE 3: `.ovtile:hover,.ovtile:focus-visible{border-color:var(--accent)}` (page L93) and `.ovrow:hover td,.ovrow:focus-visible td{background:var(--chip)}` (L86) tie in specificity with the new `.ovtile.ruled-*` (L116) / `.ovrow.ruled-* td` (L117), which come later and win — a ruled tile/row loses its hover AND keyboard focus-visible cue (no outline rule exists for .ovrow/.ovtile; focus outline covers only .tab/.btn/.note/summary).
⚠️ 23 Neighbour overlap "units cannot disagree with the tile" — true, but COUNTEREXAMPLE 4: a multi-unit card with ONE unit ruled (e.g. R-A on unit 1, unit 2 open) shows a green "RULED R-A" tile/row — reads as decided at a glance though a unit is still owed. Inherited card semantics, now on the surfaces Will scans.
⚠️ 25 Neighbour missing info "label falls back to the verdict word" — the fallback in code is `'RULED ' + (label || 'CHOICE')`, keyed on a missing LABEL for a choice, unrelated to a missing ts; the ts rule (`t = ts || ''`) is correct as stated.
⚠️ 28 The reviewed diff is the implementation — worktree `decision_deck.py` (mtime 12:07:13) differs from changeD.diff (12:06:01) on one line: the third Change D selftest check now tests `CSS` (the constant) instead of `page_html`. The rendered page is unaffected; the reviewed object is one edit behind the tree.
✅ 1 Ask quoted with time/date/source (Will, 12:02 ET 10/15)
✅ 2 setState ~L1345 — HEAD L1345 `function setState`
✅ 3 tint applied to .card only at HEAD
✅ 4 tiles/rows carried no state at HEAD (diff adds the only hooks)
✅ 5 List tint faint, no label (light tint/surface 1.10)
✅ 6 written BEFORE the edit — INFERRED (acceptance mtime 12:04:39 < diff 12:06:01)
✅ 7 DOMAIN · consequential ⇒ independent reader
✅ 8 D1 mirror: mirrorRuling is called only inside the `t >= TINT_TS[ck]` gate, for snapshot unconsumed, snapshot consumed, and fresh tap (all route through setState 'sent'); selector `#owed .ovrow/.ovtile[data-wq=N]`
✅ 9 D2 mapping: approve+choice → --tint-ok, decline → --tint-no, later → --tint-later; tile bg+border, row td bg
✅ 11 D3 pill placeholder in all three templates; texts RULED APPROVE/DECLINE/RULED <label>/LATER
✅ 14 D4 nothing baked: 78 `<span class="pill rl" hidden></span>` = 26 cards+26 tiles+26 rows; 0 `class="pill rl rl-`
✅ 17 D5 selftest: SELFTEST PASS (worktree; 60 placeholders for 20 live rows)
✅ 18 D5 split test: 26 passed, 33 subtests
✅ 20 D5 counts: 26 ovrow / 26 ovtile / 26 cards
✅ 21 D5 Reference untouched: selector scoped to #owed
✅ 22 Neighbour ordinary
✅ 24 Neighbour wrong owner: setState returns on no card; querySelectorAll empty → only card in list; no throw
✅ 26 Neighbour concurrent: filters toggle `chiphide`, sort re-appends nodes, peek moves the same node — none rewrites className; classes persist
✅ 27 Reads: plan read named, Result (pending)
POINTERS: 6/6 resolve (decision_deck.py; ~L1345 setState at HEAD; tests/test_decision_deck_split.py; TINT_TS; changeD.diff; decision_deck.html); dead: none
ONE-LINE VERDICT: no — D1/D3/D5 hold and nothing is baked, but D4's parse-failure clause has no code path (❌), and Will's actual ask fails at a glance in two shapes the conditions miss: dark theme (tint 1.015:1 vs surface, pill 2.2:1) and a DONE tap (no tint, green "RULED DONE"); hover/focus cue also lost on ruled tiles/rows.
Method: read-only; selftest + split test run (temp dirs only; `git status --short PROME/` identical before/after). Contrast = WCAG relative luminance on the page's own tokens.
