# WQ-560 A part 1 (remainder) — re-space glued dates in `PROME/DOCKET.tsv` — PLAN

**Owner:** PROME (prome-34) · **Written:** 2026-10-30 21:06 ET · **Ruling:** `PROME/proposals/2026-10-30_wq560-RULED.md` (Will 20:57 ET "okay REC A approved") · **Carrier:** DOCKET L892.

**Rule:** the patterns are exactly `scripts/claim_check.py --check glued` (c3d16ffd8): month+day, word+date, date+word, as-of+digit, with backtick code spans, markdown link targets and URLs masked. At each match, insert ONE space at the glue point; change nothing else.

**Invariants:** DOCKET rows are cited by PHYSICAL LINE (header convention) — no row inserted, deleted or reordered; every row keeps its tab count; no date value, number, owner, state token or link target changes; text inside quotes of Will or a desk is not edited (none of the matches below sits inside a quote — check). Three rows' state cells begin `RESOLVED2026-10-12` (a state token glued to an ISO date). The patterns do not match ISO dates, so those cells are out of scope and stay as they are; noted for the owner of the state-token checks.

**Pass criterion:** after the edit, `claim_check.py --check glued PROME/DOCKET.tsv` reports 0 flags; `docket_view.py --write` succeeds; the gate's DOCKET checks (buried state token, overdue) give the same row sets as before.

**Excluded:** nothing inside the file is excluded by row; the masks exclude code spans, link targets and URLs.

## Proposed replacements (L# — token → replacement)

- L198 — August31 → August 31 · September1 → September 1
- L200 — October9 → October 9
- L225 — September8 → September 8 · retry9/9 → retry 9/9
- L229 — October26 → October 26
- L234 — September8 → September 8 · retry9/9 → retry 9/9
- L241 — October12 → October 12 · October23 → October 23 · October12 → October 12
- L273 — September8 → September 8
- L275 — September8 → September 8 · September9 → September 9 · establishes9/8 → establishes 9/8 · run0/4 → run 0/4 · scheduled9/9 → scheduled 9/9
- L300 — September8 → September 8 · September8 → September 8
- L301 — September5 → September 5 · September8 → September 8
- L305 — September8 → September 8
- L306 — September8 → September 8
- L307 — OWED30/32 → OWED 30/32 · OWED30/32 → OWED 30/32
- L378 — verified10/19 → verified 10/19
- L432 — October12 → October 12 · September28 → September 28 · October3 → October 3 · October12 → October 12 · October16 → October 16 · October31 → October 31 · November2 → November 2
- L554 — October26 → October 26 · October27 → October 27
- L555 — October27 → October 27
- L558 — through10/15 → through 10/15
- L566 — October15 → October 15 · October13 → October 13 · October15 → October 15
- L567 — October12 → October 12 · November13 → November 13 · November13 → November 13
- L577 — October14 → October 14 · October12 → October 12 · October12 → October 12 · October14 → October 14 · October13 → October 13
- L605 — liquidation10/9 → liquidation 10/9 · Earlier10/9 → Earlier 10/9
- L614 — partial10/8 → partial 10/8 · remaining10/9 → remaining 10/9
- L615 — October12 → October 12 · October14 → October 14 · October12 → October 12 · October13 → October 13
- L617 — October8 → October 8 · October7 → October 7 · October8 → October 8 · October7 → October 7 · October7 → October 7 · October14 → October 14 · October8 → October 8
- L630 — withdrawn10/19 → withdrawn 10/19 · Retain10/29 → Retain 10/29 · the10/19 → the 10/19 · retain10/29 → retain 10/29
- L631 — November5 → November 5 · October26 → October 26 · November5 → November 5 · October27 → October 27
- L633 — existing10/10 → existing 10/10 · consumed10/11 → consumed 10/11
- L635 — October9 → October 9
- L663 — October7 → October 7
- L672 — October12 → October 12 · October14 → October 14 · October20 → October 20 · October12 → October 12 · October14 → October 14
- L673 — October12 → October 12 · October13 → October 13 · October12 → October 12 · October10 → October 10 · October13 → October 13 · October12 → October 12 · October13 → October 13
- L681 — October14 → October 14
- L685 — October12 → October 12 · October13 → October 13
- L686 — October14 → October 14 · October12 → October 12
- L687 — October14 → October 14
- L690 — original10/14 → original 10/14 · Horton10/14 → Horton 10/14
- L691 — exOZK13/13 → exOZK 13/13
- L692 — October12 → October 12 · October13 → October 13 · October14 → October 14 · October12 → October 12
- L693 — October8 → October 8 · October12 → October 12
- L695 — October12 → October 12 · October12 → October 12
- L696 — September2 → September 2 · October13 → October 13 · October12 → October 12
- L699 — October30 → October 30 · October30 → October 30 · November6 → November 6 · October12 → October 12
- L700 — October14 → October 14 · October15 → October 15 · October14 → October 14 · October14 → October 14 · October12 → October 12
- L701 — October30 → October 30 · October12 → October 12 · October19 → October 19
- L704 — Mon10/19 → Mon 10/19
- L725 — October19 → October 19 · formal11/20 → formal 11/20
- L746 — MET3/3 → MET 3/3
- L748 — October19 → October 19
- L751 — observation10/22 → observation 10/22 · publish10/23 → publish 10/23 · October26 → October 26 · October27 → October 27 · October19 → October 19
- L752 — extra10/31 → extra 10/31 · read11/09 → read 11/09 · October19 → October 19
- L753 — observation11/09 → observation 11/09 · publish11/10 → publish 11/10 · October19 → October 19
- L754 — qualifying10/19 → qualifying 10/19 · October19 → October 19
- L755 — October19 → October 19
- L756 — October19 → October 19
- L826 — October25 → October 25
- L827 — October25 → October 25 · October25 → October 25
- L828 — October26 → October 26 · October30 → October 30 · October30 → October 30 · October31 → October 31 · October25 → October 25 · October26 → October 26 · October30 → October 30
- L832 — October26 → October 26 · October27 → October 27 · October23 → October 23 · October24 → October 24 · October26 → October 26 · October27 → October 27
- L836 — October27 → October 27
- L839 — October23 → October 23

**Count:** 157 glue points (insert one space each).

## Read log
- **Plan read** 21:0x ET (blind Sonnet coldreader; ledger `wq560-docket-plan-read.md` in PROME's session scratchpad): **PROCEED WITH FIXES — 0 ❌ · 5 ⚠️.** All 61 rows and 157 tokens verified; none in quotes, code spans, links, URLs, field 1 or a leading state token; the reader's patched copy kept 892 lines and tab counts and rerun to 0 flags.
- **Declared residue:** ⚠️1 four state cells, not three, begin `RESOLVED2026-10-12` (L200, L689, L690, L691); out of scope, unchanged · ⚠️4 the pass criterion certifies the glued-DATE class only — other glue stays in these rows (`remaining740P`, `sell1 at6.71`); the file is "glued-date class re-spaced", not clean of glue · ⚠️5 the invariant's trailing "— check" was an instruction; the test used is recorded below. **Adopted in execution:** ⚠️2 `PROME/state/CALENDAR.md` regenerated in the same commit · ⚠️3 scripted insertion, with a whole-file spaces-only proof.
- **Executed** 21:10 ET by script (the checker's own patterns and masks): 157 spaces inserted on 61 lines. Whole-file comparison against the pre-edit copy: 893 split lines, unchanged count; 61 changed; 0 differences other than spaces; 0 tab-count changes; 0 field-1 changes; final newline kept; no CR. Pass criterion: `claim_check.py --check glued PROME/DOCKET.tsv` → clean, rc 0. Calendar regenerated.
- **Result read:** PENDING.
