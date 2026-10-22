# L661 — READ 3 (independent, coldreader on Sonnet, WQ-447 A) of OSPREY's read-2 fix — 2026-10-21 21:2x ET, commissioned by PROME prome-56

**Artifacts read:** acceptance b31056c91 (AC27–AC31, written before code) · fix 6fa90a6fd · read 2 PROME/reports/2026-10-18_L661_strike-feed_read_2.md. **Verdict: RELEASE** (0 ❌ · 3 ⚠️ · 7 ✅). Reader devised its own counterexample (⚠️1). Residue routed to OSPREY by packet the same session; no repository file edited by the reader. Ledger verbatim below.

INDEPENDENT READER · DOCKET L661 READ 3 (episode reads 3 of 3 — the last) · strike_feed.py AC27 fix `6fa90a6fd` · acceptance `b31056c91` · prior read `PROME/reports/2026-10-18_L661_strike-feed_read_2.md`
Read-only: no repo file edited. Reviewed artifacts byte-identical from `6fa90a6fd` to HEAD (`git diff --quiet 6fa90a6fd HEAD -- AGENTS/OSPREY/scripts AGENTS/OSPREY/domain/energy-strikes/feed/README.md` → rc 0). Scratch only: .../scratchpad/r3/ (cx.py, cx2.py, mutant and old-version copies).

# VERDICT: RELEASE · 0 ❌ · 3 ⚠️ · 7 ✅   (⚠️1 is a text-only declaration owed in the residue, not a code fix)

Read 2's single ❌ (a later two-year range in the anchor text governs when the title's own window is not a regex match that starts first) is discharged for every shape read 2 built: CX2-1, 2, 3, 11, 14 (and 4) now read BULLETIN_NEWEST_UNSURE, NOT_READ 1. The rule is exactly the predicate read 2 proposed. My own counterexamples (⚠️1) show the class is NARROWED, not closed; the residue is the same declared class as CX2-13 plus a keying limit of the month-word predicate.

## ❌ (blocks RELEASE)
None.

## ⚠️
**⚠️1 The month-word predicate is silent when the title's own window has no RECOGNISABLE month word; declared limit (vi) under-describes this.**
- Claim: README `BULLETIN_NEWEST_UNSURE` row, silent case (vi): "a title holding ONLY a later window, every month word inside it (CX2-13, pinned)". Acceptance AC27: "Declared, not caught: CX2-13 … every month token lies inside the one later window".
- Artifact: `AGENTS/OSPREY/scripts/strike_feed.py` `MONTH_TOKEN_RE` / `date_text_outside_window` (:147-162); README (vi).
- Command: `python3 -B cx.py` (scratch; run through the owner's `run()` harness, slug `…21st-27th-september-2026`, run 2026-10-08, so correct = STALE or UNSURE, NOT_READ 1).
- Observed (all `BULLETIN — read manually`, NOT_READ 0, pub 2026-10-04; the released `4ea2b4539` reads STALE via the slug):
  - A `Maritime Security Report: 21st - 27th Septmber. Next report covering 28th September 2026 - 4th October 2026` (misspelled month)
  - B `… 21.09 - 27.09. Next report covering …` (numeric months)
  - C `… 21st-27thSeptember. Next …` and G `… 21st - 27th Sept26. Next: …` (month glued to a token, so `\b` finds no word)
  - D `… 21 - 27 septembre. Next …` (non-English); F `… Week 39. Next report covering …`
  - Control: E (em-dash in own window, month word spelled) fires UNSURE; I (plain title) STALE; so the rule works exactly where a month WORD is present.
- Why ⚠️ not ❌: needs BOTH a teaser/clause with a later window inside the matching anchor (0/28 live anchors today; nothing in the instrument detects a layout change) AND an own window with an unrecognisable month. Read 2 itself accepted CX2-13 (own window absent) as a declared silent case; A–D are the same property ("no month word outside the later window"). It is still a fail-open vs the released code, and a stricter reader could grade it ❌ — the grade leans on the compound trigger and on the unattended run staying UNAVAILABLE until PROME rules.
- Proposed change (text only): widen (vi) to "the title's own date carries no recognisable month word (misspelled, numeric, glued, non-English, or absent) and a later window follows" and add one pinned DECLARED LIMIT row (e.g. case A) beside the CX2-13 pin. No code change; do not chase the typo space with a smarter parse.

**⚠️2 The CX-A contradiction, graded: COSMETIC to the fail-closed guarantee, a real change to the label contract — disclosed, but the acceptance text is internally inconsistent and the assertion is looser.**
- Claim: ACCEPTANCE `b31056c91` AC27 "every existing test passes unchanged" vs the same bullet's "CX-A stays BULLETIN_STALE-class or louder (it now ALSO carries the AC27 doubt)"; completion: "contradicting this pass's own acceptance line".
- Artifact: `test_strike_feed_L661.py` ~:278-285 (AC22 CX-A test); acceptance completion section.
- Command: `python3 -B -m unittest test_strike_feed_L624 test_strike_feed_L661` from `scripts/tests/` → Ran 73, OK. Mutant m1 (AC22 precedence reverted in the shared helper, `if m2:`) → FAILED (failures=2).
- Observed:
  - The acceptance contradicted itself (the "unchanged" line vs its own "or louder"); the author recorded it rather than editing it out. The change itself is the one AC27 declared.
  - Preserved: NOT_READ 1, `pub_date` 2026-09-27, the STALE cause inside the label (the label carries "the followed bulletin is also BULLETIN_STALE (…)"), and AC22 discrimination (m1 fails 2 tests).
  - Changed: the summary token for CX-A is now `BULLETIN_NEWEST_UNSURE`, not `BULLETIN_STALE` (`f_sum = f_label.split(" — ")[0]`); both are in `NOT_READ_MATCHES`, and no code or doc outside the tests keys on the prefix (grep of `BULLETIN_STALE` in scripts/README: only the NOT_READ tuple and label builders).
  - The assertion is now a disjunction (`startswith((STALE, UNSURE))` + `assertIn STALE`), so it no longer pins UNSURE for CX-A; AC27's own effect on CX-A is pinned only by the CX2-x rows.
- Proposed change: optional — tighten to `startswith("BULLETIN_NEWEST_UNSURE")` + `assertIn("BULLETIN_STALE")` since the behaviour is now deterministic. Not a blocker.

**⚠️3 Louder cost is wider than the README's one example, and tell (e)'s (b) branch has no row-level test.**
- Claim: README (e): "an English 'may' in a title fires it too (louder, the safe direction)".
- Artifact: README `BULLETIN_NEWEST_UNSURE` row (e); `test_predicate_shapes` (predicate-level only for the no-window branch).
- Command: `python3 -B cx.py` / `cx2.py` (cases J, K, L, KICKER, B-ROW).
- Observed: a fresh, correctly dated bulletin with a month word beside its window — `September update | … 28th September - 4th October 2026` (L), `… October roundup: … 28th September - 4th October 2026`, `(may be revised)` (J), `Mar Gold incident` (K) — reads UNSURE, NOT_READ 1. Any publisher habit of putting a month in the title would turn every run UNSURE and train the operator to skip the label. Branch (b) (month word, no window) is exercised at row level only in my run (B-ROW → UNSURE, NR 1, correct); the repo pins it in `test_predicate_shapes` and mutant ME (1 F), not through `run()`.
- Proposed change: README (e) says "a month word in a non-date phrase fires it" (not only "may"); no code change.

## ✅
1. **Process order:** `b31056c91` holds only the acceptance file (+27 lines); `6fa90a6fd` holds code, tests, README and the completion (commit text and `git show --stat`). VERIFIED.
2. **Suite:** 73 tests OK (32 L624 + 41 L661) from `scripts/tests/`; 9 new tests counted by name (CX2-1, 2, 3, 11, 14, 4, must-not-fire fixtures, predicate shapes, CX2-13 pin). VERIFIED.
3. **Fails-first reproduced (own runs, `STRIKE_FEED_PATH`):** 8 on `7299a2e39` (6 F + 2 E — the six row tests and the two predicate tests; the CX2-13 pin passes there by design); 25 on `4ea2b4539`. Matches the commit message exactly. VERIFIED.
4. **Read 2's reproduced shapes are closed:** CX2-1, 2, 3, 11, 14, 4 give UNSURE, NOT_READ 1 with reason "anchor text carries date text outside its window" (tests + my runs). VERIFIED.
5. **Shared precedence helper:** `governing_window_match` (:130-139) is called by `bulletin_window` and `date_text_outside_window`; mutant m1 (revert AC22 inside the helper) fails 2 tests; mutant m2 (drop outside-span check) fails 7. m3 (edge `<=`→`<`) survives: EQUIVALENT (a month token cannot abut the window edge without a separator, `\b`). VERIFIED / INFERRED for m3.
6. **Adds-only direction:** AC27 appends to `why[followed["pos"]]` after all other doubt logic (:259-260); no path lowers a label. Overlap with AC15 on one link yields one doubt entry, reasons joined (OVERLAP run: NR 1, one `1 doubt link(s)`). VERIFIED.
7. **Must-not-fire on real data and docs:** test over every matching anchor on both fixtures (≥28) passes; README doubt tell (e) matches the code (month word, outside the governing match, or month word with no match); status line says read 3 is the last, fix unreviewed, unattended run UNAVAILABLE. AC28–AC31 annotations present as in-place bracketed notes in the acceptance (diff-checked). VERIFIED.

## Pointers
ACCEPTANCE (`b31056c91`), fix (`6fa90a6fd`), read 2 report: all resolve. `STRIKE_FEED_PATH` copies of `7299a2e39`/`4ea2b4539` came from `git show`. Dead: none.

## Operational note (not a code finding)
The unattended feed run is PROME's ruling, UNAVAILABLE until a passing read; this ledger is that read's input. The silent set is "title has a later window, no recognisable own month word, anchor carries teaser text"; if PROME lifts the hold, ⚠️1's text should be in the README first.

RELEASE
