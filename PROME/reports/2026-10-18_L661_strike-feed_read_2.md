INDEPENDENT READER · DOCKET L661 READ 2 (episode reads: 1 → 2 of 3) · OSPREY strike_feed.py read-1 fix · acceptance `31053d1f6`, fix `7299a2e39`
Stamp: Sun Oct 18 18:03 EDT 2026 (`date`). Read-only: nothing in the repo was edited, staged or committed. The reviewed artifacts are byte-identical from `7299a2e39` to HEAD (`git diff --quiet 7299a2e39 HEAD -- AGENTS/OSPREY/scripts AGENTS/OSPREY/domain/energy-strikes/feed/README.md`). Scratch copies came from `git show HEAD:` (cmp-identical to the worktree), `48342e63a:` (pre-fix) and `4ea2b4539:` (released). Every row counterexample ran through the owner's own `run()` harness: injected date and fetch, temp ledger, `days_back` 10.
Harness: /tmp/claude-1000/-home-willi-Research-workspace-PROME/23f41fc0-bac7-4608-b43a-6667a1b47ab3/scratchpad/l661r2/ — cx/cx.py and cx/cx3.py (counterexamples), cx/fuzz2.py (prefix fuzz + candidate predicate on the real fixtures), cx/diff.py (HEAD vs pre-fix differential), mut/mk.py (mutants).

# VERDICT: HOLD · 14 claims · 9 ✅ · 4 ⚠️ · 1 ❌

**HEADLINE: STILL UNRESOLVED (❌ = 1).** AC22 fixes CX-A exactly as written, but it does not close the defect class. In five shapes I built, the title's own window does not match the parser's patterns, or it sits after the extra text, or the extra text is in a featured listing of the same link. In each, a stale bulletin still reads `BULLETIN — read manually`, NOT_READ 0, because a later two-year range in the anchor text governs. The released `4ea2b4539` reads `BULLETIN_STALE`, NOT_READ 1, in every one of them, so these are fail-open regressions introduced by AC16 that AC22 leaves open. They are the same class, and graded by the same standard, as read 1's ❌1.

Read 1's proposed line ("leftmost start wins") was itself incomplete. "Leftmost" compares only the matches the regexes can produce, so a yearless, abbreviated or late-placed own window is invisible to it.

**Reachability today: none observed (INFERRED).** All 28/28 matching anchors on the 10/9 and 10/16 fixtures are title-only. My candidate guard (❌1) fires on 0 of those 28 and on all five failing shapes.

**Unattended use: HOLD.** The withholding rule follows consequence: an index layout change that adds teaser or excerpt text to an anchor would make a stopped publisher read fresh, and nothing in the instrument detects that change. One read remains in the budget.

## Step 1 — the owner's suite and fails-first (my own runs)
| Command (from `AGENTS/OSPREY/scripts/tests/`, Python 3.12.3) | Observed |
|---|---|
| `python3 -B -W error::ResourceWarning -m unittest test_strike_feed_L624 test_strike_feed_L661` | **Ran 64 tests, OK** |
| `python3 -I -B test_strike_feed_L661.py` / `… L624.py` | OK / OK |
| `grep -c 'def test_'` | L624 32 · L661 32 (24 prior + 8 new) |
| `STRIKE_FEED_PATH=<48342e63a copy>` (pre-fix), both files | **FAILED (failures=3)**: the single-date "7 days" pin, CX-A row, direct leftmost |
| `STRIKE_FEED_PATH=<4ea2b4539 copy>` (released), both files | **FAILED (failures=16)**: the 11 from 10/16 + 5 new (two-year forms, CX-F, 14-day span, reversed, year-apart). CX-A and direct-leftmost pass there, as their docstrings say |

## Step 2 — my own counterexamples (HEAD = 7299a2e39 · PRE = 48342e63a · REL = 4ea2b4539)
Every row case uses a slug carrying the true window `21st-27th-september-2026`, run 2026-10-08, cutoff 09-28. Fail-closed therefore requires STALE.

| # | Anchor text (first matching listing) | HEAD | PRE | REL |
|---|---|---|---|---|
| **CX2-1** missing info: own window lacks its year | `Maritime Security Report: 21st - 27th September. Our next report, covering 28th September 2026 - 4th October 2026, will follow.` | **BULLETIN, NOT_READ 0, pub 10-04** | same | STALE, NOT_READ 1 (slug) |
| **CX2-2** malformed own window ("Sept") | `…: 21st - 27th Sept 2026. Our next report, covering 28th September 2026 - 4th October 2026` | **BULLETIN, NOT_READ 0** | same | STALE, NOT_READ 1 |
| **CX2-3** later two-year range BEFORE the title (kicker/teaser) | `Coming next: 28th September 2026 - 4th October 2026 \| Maritime Security Report: 21st - 27th September 2026` | **BULLETIN, NOT_READ 0** | same | STALE, NOT_READ 1 |
| **CX2-11** ordering: CX2-1's text on top, an honest older link below | CX2-1 text + `14th - 20th September 2026` | **BULLETIN, NOT_READ 0** | same | STALE, NOT_READ 1 |
| **CX2-14** featured duplicate: teaser listing first, clean title listing second, same href | CX2-1 text, then `…: 21st - 27th September 2026` | **BULLETIN, NOT_READ 0** (dedup keeps the first listing's text) | — | STALE, NOT_READ 1 |
| CX2-15 | the same two listings, clean one first | STALE ✅ | — | STALE |
| CX2-13 | title holds only a later window: `Maritime Security Report. Next report covering 28th September 2026 - 4th October 2026` | BULLETIN, NOT_READ 0 | same | STALE |
| CX2-4 (pre-existing) | as CX2-3, clause in one-year form `28th September - 4th October 2026` | BULLETIN, NOT_READ 0 | same | **same (REL also fresh)** |
| CX2-5 (pre-existing) | yearless own window + one-year clause | BULLETIN, NOT_READ 0 | same | **same** |
| CX2-6 (pre-existing) | slug `…-week-39`, title `… Week 39 - next issue 4th October 2026` | BULLETIN (single-date basis), NOT_READ 0 | same | same |
| CX2-7 ✅ | `28th September - 4th October 2026 (previous: 21st September 2026 - 27th September 2026)`, slug matches | BULLETIN ✅ | **STALE (pre-fix wrong)** | BULLETIN |
| CX2-8/8b ✅ | two-year own window + later one-year clause `Next: 5th - 11th January 2027`, run 01-14 / 01-15 | fresh (END 01-04 = cutoff) / STALE pub 01-04 ✅ | fresh (01-14) | STALE (single date 12-29) |
| CX2-9 ✅ | year-boundary page convention `29th December - 4th January 2027. Next: 5th January 2027 - 11th January 2027`, run 01-14 | END 01-04 (leftmost) ✅ | **END 01-11 (pre-fix wrong)** | END 01-04 |
| CX2-10 (louder) | `Issue 22 - 29th December 2026 - 4th January 2027`, run 2027-01-09 | **STALE, pub 12-29**: a one-year fragment `22 - 29th December 2026` starts first, so a false STALE | fresh, 01-04 | STALE, 12-29 |
| Direct | `Issue 1 - 29th December 2026 - 4th January 2027` · `31 - 29th December…` | (None, None): louder | parses | (None, None) |

Prefix fuzz (`cx/fuzz2.py`) prefixed every weekly 2026 window with `Issue n - `, `No. n `, `n `, `Vol n, `, `Report n: `, `n - `, `Week n – ` for n = 1..31. Over **13,144 strings**: END later than the true END **0**; END earlier or unparsed (louder) **155**. A leftmost one-year fragment can only end at the two-year START, so the fragment hole fails closed. It never makes a row quieter (VERIFIED by fuzz; INFERRED by regex structure).

Differential (`cx/diff.py`): **7,902** plain titles and slugs (one- and two-year, within- and cross-month, 6- and 7-day spans, numeric-slug and `-1` forms, 2026–2027) give **0 diffs** between HEAD and PRE. AC22 changes behaviour only on text that carries more than one date pattern.

## Step 3 — mutants (owner's suite, 64 tests; `mut/mk.py`)
| Mutant | Result |
|---|---|
| MR2 listing positions compressed | 1 F (CX-F) ✅ |
| MR4 span 14 → 33 | 1 F ✅ |
| MR5 END before START allowed | 1 F ✅ |
| MR7 "final" removed | 2 F ✅ |
| REVERT AC22 (`if m2:`) | 2 F ✅ |
| MY1 `<=` → `<` | survives: EQUIVALENT (the two patterns cannot start at the same offset, because WIN2 needs a month where WIN needs a day) |
| MY2 two-year only when the one-year form is absent | 6 F ✅ |
| MY3 rightmost one-year match instead of leftmost | 2 F ✅ |

The owner's mutant counts are reproduced exactly.

## Step 4 — assertion ledger

### ❌
**❌1 AC22 does not close read 1's defect class. A later two-year range in the anchor text still makes a stale bulletin read fresh whenever the title's own window is not a regex match that starts first. This is a regression vs the released code.**
- **Claim:**
  - README follow_newest bullet: "when a text carries more than one window, the one that STARTS FIRST governs — L661 AC22, read 1 ❌1".
  - ACCEPTANCE_L661 AC22: "A two-year pair later in the text … must never override the leftmost one-year window" (also the code comment at `strike_feed.py:137-140`).
  - The AC22 Neighbours line: "missing information — text with only one form: behaviour unchanged by construction".
  - The owner's memo §2: "352,800 composed strings — the result equals the leftmost window alone in every case (0 violations)".
- **Artifact:** `AGENTS/OSPREY/scripts/strike_feed.py:135-141`. `m1 = re.search(WIN_RE, t)` is the leftmost regex-matchable one-year window. When the own window is yearless, abbreviated or malformed, `m1` is the fragment `26 - 4th october 2026` inside the clause, which starts after `m2`, so the two-year clause governs. `pick_newest` uses the title basis first (`:184`) and dedup keeps the first listing's text (`parse_html_index`).
- **Command:** `python3 -I -B cx/cx.py <tests> head/ pre/ rel/` and `python3 -I -B cx/cx3.py <tests> head/ rel/`
- **Observed:** CX2-1, CX2-2, CX2-3, CX2-11 and CX2-14 each give HEAD `BULLETIN — read manually`, NOT_READ 0, pub 2026-10-04, against REL `BULLETIN_STALE`, NOT_READ 1, pub 2026-09-27. AC15 stays silent, because the gap between the title and the slug is 1 day (≤ 180).
  - These are not covered by declared residue (iii). (iii) declares how a correctly parsed title is resolved against the slug. Here the title is misparsed, which is exactly how read 1 graded CX-A.
  - The owner's 352,800-string property check is clean against the wrong reference: it defines "leftmost window" with the same regexes, so it cannot see an own window that the regexes miss.
  - The Neighbours "missing information" line was scoped to "text with only one form" and never tried an own window that fails to parse.
  - CX2-4, CX2-5 (one-year clause) and CX2-6 (single later date) are the same class but pre-existing: REL is also fresh there.
- **Reachability:** none on the current layout (INFERRED). 28/28 matching anchors on both fixtures are title-only. I did not re-check the full untrimmed live page; read 1 reports it as 14/14 title-only. The trigger is any teaser, excerpt or kicker text inside a matching anchor, the common card layout for a featured post (CX2-14).
- **Proposed change (acceptance first):** a fail-closed doubt, not a smarter parse. When the anchor TITLE of the followed link carries a month token outside its governing window match, or carries month tokens with no governing match, add the doubt reason "anchor text carries date text outside its window — the followed link's own date is in doubt", which gives `BULLETIN_NEWEST_UNSURE` and NOT_READ. The month token is word-bounded, full name or 3-letter abbreviation: `\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b`.
  - Do not just fall back to the slug: with an undated slug, `single_date(href + " " + inner)` picks the clause's 28 Sept, which is borderline fresh.
  - `bulletin_window` would need to expose the governing span, or a sibling helper would need to recompute it.
  - Predicate verified in scratch (`cx/fuzz2.py`): **fires on 0/28** live fixture anchors. It fires on CX-A, CX2-1, CX2-2, CX2-3, CX2-4, CX2-5 and the CX2-14 teaser.
  - It does NOT catch CX2-13, where every month token lies inside the one later window. Declare CX2-13 as a known silent case alongside (iii): it is indistinguishable by dates from the live benign mis-slug.
  - Tests: CX2-1, CX2-3, CX2-14 (each must fail on HEAD), plus a must-not-fire on both fixtures. `may` as an English word fires louder only, which is acceptable.
  - This would be a fix after read 2, so read 3 (the last in the budget) would review it.

### ⚠️
**⚠️1 The leftmost rule introduces an undisclosed louder behaviour change: a number before a two-year window forms a one-year fragment that starts first.**
- **Claim:** the completion section says "No other behaviour changed". The README states the leftmost rule without noting fragments.
- **Artifact:** `strike_feed.py:135-141`. WIN_RE has no left digit boundary (N2).
- **Command:** cx.py CX2-10 and the direct lines; fuzz2.py prefix fuzz.
- **Observed:**
  - `Issue 22 - 29th December 2026 - 4th January 2027` gives (12-22, 12-29), so a fresh bulletin reads STALE at 01-09. PRE parsed it right; REL behaves the same as HEAD.
  - `Issue 1 - …` and `31 - …` give (None, None).
  - Across 13,144 prefixed strings, END is never later and 155 are earlier or unparsed. The fragment only ever makes a row louder (safe direction).
- **Proposed change:** note in the AC22 completion and residue that a numeric prefix can produce a false STALE or an unparsed title (louder, safe direction), or measure the precedence from the first non-fragment start. Optional; not a blocker.

**⚠️2 The owner's property check certifies the rule against itself.**
- **Claim:** memo §2 and the completion section: "352,800 composed strings … 0 leftmost violations".
- **Artifact:** completion section, `ACCEPTANCE_L661…:120`.
- **Command:** reasoning from the definition, plus ❌1's CX2-1 and CX2-3.
- **Observed:** "leftmost" is computed with the same two regexes, so a violation is impossible by construction for any own window the regexes match, and invisible for any they miss. The figure supports IMPLEMENTED, never "the class is closed".
- **Proposed change:** reword it as "consistency with the leftmost rule", not as defect-class evidence. Compose with yearless, abbreviated and prefix-placed own windows next time.

**⚠️3 Pre-existing fail-open shapes of the same class are undeclared.**
- **Claim:** README "known silent cases include …" (i)–(v), declared non-exhaustive.
- **Artifact:** README `BULLETIN_NEWEST_UNSURE` row; ACCEPTANCE :58.
- **Command:** cx.py CX2-4, CX2-5, CX2-6.
- **Observed:**
  - A one-year later clause before the title, or after a yearless own window, reads fresh on HEAD and REL alike.
  - A slug with no date plus a title with a single later date ("next issue 4th October 2026") reads `BULLETIN` on the single-date basis, NOT_READ 0. The note says only that the date "may be the window START", never that it may be a later date.
  - The list is honestly non-exhaustive, so this is not an over-claim. But the shapes are the operator-relevant ones.
- **Proposed change:** add "date text in the anchor beyond the title's own window" to the known silent cases until ❌1's doubt lands. ❌1's predicate also covers CX2-4 and CX2-5.

**⚠️4 The historical 10/16 completion text still reads as current residue.**
- **Artifact:** ACCEPTANCE_L661 :73 and :82 ("the three still-silent cases"); :84 (guards: "the left digit boundary … and 'a two-year match is final'").
- **Command:** `grep -n "three still\|left digit boundary" ACCEPTANCE_L661…`
- **Observed:**
  - :58 (widened) and :103 (left boundary is belt-and-braces) supersede these lines.
  - :82 and :84 stand undated-in-line under a header dated 10/16.
  - "A two-year match is final" is now true only when the two-year match starts first.
  - Pointer/basis class: no operator surface depends on it.
- **Proposed change:** add a one-line "superseded by AC22/AC25 (10/18)" marker at :82 and :84, without rewriting the record.

### ✅
1. **Suite:** 64 OK (32 + 32); isolated mode OK per file (Step 1). VERIFIED.
2. **Fails-first exactly as claimed:** 3 F on `48342e63a`, 16 F on `4ea2b4539`, with the named tests (Step 1). VERIFIED.
3. **CX-A and the direct `…22nd - 28th December 2026 - 4th January 2027` are fixed:** STALE, NOT_READ 1, pub 09-27, and END 12-28. VERIFIED (tests and my runs).
4. **No regression on plain forms:** 7,902 plain title and slug strings give 0 diffs between HEAD and PRE. R3-I2, the `to` form and the no-space form still parse. Year-boundary cases (CX2-8, CX2-8b, CX2-9) take the leftmost window correctly, and CX2-7 and CX2-9 fix PRE errors. VERIFIED.
5. **Process order:** the acceptance was committed alone first. `31053d1f6` (17:47:21 EDT) touches only the acceptance file; `7299a2e39` (17:50:31) holds the code. VERIFIED (`git show --stat`).
6. **⚠️2 (read 1) FIXED by tests, truthfully:** my rebuilt MR2/MR4/MR5/MR7/REVERT give 1/1/1/2/2 F, matching the owner's counts. MY1 is equivalent; MY2 and MY3 are caught. VERIFIED.
7. **⚠️1 (read 1) DECLARED, truthfully:**
   - AC13 code (`:211-218`) compares first listings: `below` is in first-listing order and `later` scans items.
   - The README `BULLETIN` row and tell (c) are narrowed to "first listings".
   - The CX-E pin passes on HEAD and is labelled a DECLARED LIMIT.
   - No surface claims it closed. VERIFIED.
8. **⚠️3 and ⚠️4 (read 1) FIXED in text, truthfully:**
   - README and ACCEPTANCE :58 say "known silent cases include (the list is not exhaustive)".
   - (i) is widened to "no dated link FIRST-listed below it ends later"; CX-D2 and CX-E are added; the "END after run date" tell is recorded as a later-episode candidate.
   - "~7 days" appears in the code (`:344`), the README and the test pin.
   - MR1/MR9/MR10/MR11 are declared, not added, as stated. VERIFIED (residual stale text in ⚠️4 above).
9. **Completion states unmerged and status honest:** the README status says read 1 failed on one ❌, the fix is IMPLEMENTED and TESTED, NOT independently verified, and the unattended run is UNAVAILABLE on either version. The completion section says "INDEPENDENTLY VERIFIED: NO". VERIFIED.

## RELEASE / HOLD
**HOLD.** ❌1 is a fail-open regression vs the released code in the defect's own terms, and it is undetected and undeclared. The released code is not a safe fallback either (read 1: R3-Q, R3-H, R3-I2). So the UNATTENDED feed run stays UNAVAILABLE on both versions. Attended runs and the index-only AC21 contact remain fine, because the current title-only layout does not trigger any failing shape (INFERRED from 28/28 fixture anchors).

The episode has one read left (3 of 3). The ❌1 change should be written acceptance-first, kept to the one doubt rule plus its tests, and read once. If read 3 finds a further action-class ❌, the review budget forces a disposition, not a fourth read.

POINTERS checked: read-1 ledger, PROME packet (and its 21:28 correction), OSPREY memo §2, ACCEPTANCE_L661 (AC13–AC26), test_strike_feed_L661.py, README, `git show 7299a2e39` / `31053d1f6`, `48342e63a`, `4ea2b4539`: all resolve. Dead: none.
ONE-LINE VERDICT: HOLD — STILL UNRESOLVED (❌ = 1: a later two-year range in the anchor text still makes a stale bulletin read fresh when the own window is yearless, abbreviated, placed after the clause, or in a featured teaser listing; the released code reads STALE in each). ⚠️ = 4. ✅ = 9.
