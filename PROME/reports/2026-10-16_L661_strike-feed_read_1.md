INDEPENDENT READER · DOCKET L661 READ 1 (episode reads: 0 → 1) · OSPREY strike_feed.py READ-3 residue repair · acceptance `e5fe3a692`, fix `48342e63a`, reviewed at `b5be957d0`
Stamp: Fri Oct 16 17:46:59 EDT 2026 (`date`). Read-only. The repo was not edited, staged or committed. The reviewed artifacts are byte-identical from `b5be957d0` through `a4e9436e1` (`git diff --quiet b5be957d0 HEAD -- AGENTS/OSPREY/scripts AGENTS/OSPREY/domain/energy-strikes/feed/README.md`). `AGENTS/OSPREY/scripts/__pycache__/` (mtime 2026-10-08) existed before this read; everything ran under `-B`. Scratch copies were made with `git show HEAD:` / `git show 4ea2b4539:` and are `cmp`-identical to the worktree. Every counterexample ran through the owner's own `run()` harness (injected date and fetch, temp ledger/out_dir).
Harness: /tmp/claude-1000/-home-willi-Research-workspace-PROME/3b12c1e2-68ac-4b53-9607-efbd2f670b88/scratchpad/l661r1/ — cx/cx.py, cx/cx2.py (counterexamples), cx/fuzz.py (differential), cx/live.py (full live page), mut/mkmut.py + mut/probe.py (mutants), mut/src/*.py (mutant and candidate-fix copies).
SCORE: 18 claims · 13 ✅ · 4 ⚠️ · 1 ❌

**HEADLINE: STILL UNRESOLVED (❌ = 1).** AC16 is the one change that can make a row quieter. Its own guard, "a two-year match is final", opens a new fail-open path: a stale bulletin reads fresh (NOT_READ 1 → 0) when the matching anchor's text carries a second, later full-date pair. The released `4ea2b4539` gets this case right. Nothing in the suite, the declared residue or the README covers it. The fix is one line, and it is verified in scratch (❌1).

**UNATTENDED OPERATIONAL USE, pending ❌1:** my read is that it is acceptable on the CURRENT live layout. On the 10/9 and 10/16 indexes every matching anchor carries the title only (14/14 each, verified on the full untrimmed 10/16 page), so ❌1's trigger is absent. Every other L661 change only adds NOT_READ (code-read, ✅12). Reverting to `4ea2b4539` would re-open R3-Q and R3-H (both silent), R3-I2 (a false STALE) and two N2 mis-parses (✅5), so the reverted code is not the safer fallback. That assurance ends the moment the index layout changes, and nothing in the instrument would detect such a change. Land ❌1's fix and its test before calling L661 verified. The withholding decision is PROME's (`aae1d0ba7`).

## Step 1 — the owner's suite, and fails-first
- `cd AGENTS/OSPREY/scripts/tests && python3 -B -W error::ResourceWarning -m unittest test_strike_feed_L624 test_strike_feed_L661` gave **Ran 56 tests, OK, rc=0**. `python3 -I -B -W error::ResourceWarning <file>` gave OK for each file. Python 3.12.3. `grep -c 'def test_'` counts 24 L661 tests and 32 L624 tests.
- `STRIKE_FEED_PATH=<scratch copy of git show 4ea2b4539:…/strike_feed.py> python3 -B -m unittest test_strike_feed_L661` gave **FAILED (failures=11)**, the exact 11 the owner names. The other **13 pass**, each labelled NON-DISCRIMINATING or DECLARED-LIMIT in its docstring. The L624 file gives OK on `4ea2b4539` (unchanged tests). The owner's claim is confirmed.

## Step 2 — my own counterexamples (NEW = HEAD, OLD = 4ea2b4539; days_back 10)
| # | Input | Fail-closed requires | NEW does | OLD did |
|---|---|---|---|---|
| **CX-A (AC16)** | One link. Title `Maritime Security Report: 21st - 27th September 2026. Our next report, covering 28th September 2026 - 4th October 2026, will follow.` Run 10/08 (cutoff 09-28). | STALE (true END 09-27) | **`BULLETIN`, NOT_READ=0, pub 2026-10-04**, "window 2026-09-28..2026-10-04 (title)" | STALE, NOT_READ=1, pub 09-27 |
| CX-A′ (AC16, direct) | `…: 22nd - 28th December 2026 - 4th January 2027` | END 12-28 (leftmost window), or unparsed | (12-28, **01-04**): a later END | (12-22, 12-28) |
| CX-A″ (AC16, direct) | `…: 5th - 11th October 2026 (archive 1st January 2026 - 31st December 2026)` | 10-05..10-11 | (None, None): falls back to the slug (louder, not quieter) | 10-05..10-11 |
| CX-B (AC16) | R3-I2 two-year title. Read 01-20 / 01-14 / 01-15. | STALE / fresh at END = cutoff / STALE | STALE pub 01-04 / fresh / STALE ✅ | STALE pub 12-29 each time |
| CX-C1/C2 (AC15, gap exactly 180/181 d) | Title 5–11 Oct 2026, slug 2–8 Apr vs 1–7 Apr 2026, followed | 180 d: silent (declared iii). 181 d: UNSURE | silent / UNSURE naming FOLLOWED ✅ | silent / silent |
| CX-J1/J2 (AC16×AC15) | Two-year title, slug 26 Jun–2 Jul vs 25 Jun–1 Jul 2026, run 2027-01-07 | silent (declared iii) / UNSURE | fresh / UNSURE ✅ (at 180 d AC16 changes STALE to fresh: declared iii) | STALE / STALE |
| CX-C3 (AC16×AC15) | Two-year title (right), page-convention slug with a year typo `29th-december-4th-january-2026`, followed | UNSURE (gap 359 d) | UNSURE ✅ | different (DEC followed) |
| CX-C4 (AC15) | CX1 shape in the page's own one-year convention (title `…4th January 2026`, slug `…-4th-january-2027`), below DEC and last on the page | UNSURE | UNSURE ✅ | silent |
| CX-C5 (AC16) | Two-year title, run 2026-12-31 (inside its window, END in the future) | an honest bulletin cannot end after the run date | fresh, pub 2027-01-04 (pre-existing class) | fresh |
| CX-D (AC13 across years) | Pinned DEC, then the past-typo'd real newest `29th December 2025 - 4th January 2026`, then 15–21 Dec 2026 | UNSURE naming the 2025 link | UNSURE ✅ | silent |
| CX-D2 | A forward-typo'd OLD link `29th December 2026 - 4th January 2027` (title = slug) pinned on top. The publisher stopped at 15–21 Dec. Run 2027-01-02. | not silent-fresh | **fresh, NOT_READ 0** | fresh (pre-existing) |
| **CX-E (AC13 listing)** | `OCT, SEP, TYPO25(2025), SEP`: an older link listed again below the typo'd newest. Run 10/13. | UNSURE naming TYPO25 (AC13 :21 "a dated link listed below it"; README :13) | **`BULLETIN`, NOT_READ 0** | silent |
| CX-F (AC14×AC13) | `OCT, OCT, TYPO25, SEP` | UNSURE | UNSURE ✅ | silent |
| CX-G / G2 | Image-anchor-first duplicates (empty text, then title) for every link; honest / with a pinned last week + typo | fresh / UNSURE | fresh / UNSURE ✅ | fresh / silent |
| CX-H / H2 | Em-dash two-year title (— is not a SEP) + two-year slug / + page-convention slug, read 01-12 | fresh via the slug | fresh (slug basis) ✅ | STALE / fresh |
| CX-I | Two-year title with START after the run date (12-27), above DEC | UNSURE (FUTURE) | UNSURE ✅ | UNSURE |
| Direct windows | `29th December 2026-4th January 2027` (the page's no-space style), en dash, `29 December 2026 - 4 January 2027`, `…-4th-january-2027-1`, 14-day span | parse | parse ✅ | None |
| Direct windows | 15-day span · END before START `…4th January 2026` · reversed `4th January 2027 - 29th December 2026` · `…2028` · `29th February 2027…` · `15th December 2025 - 27th December 2026` | None | None ✅ | None, except reversed → (12-27, 12-29) and 2025/2026 → (12-25, 12-27): N2 mis-parses |

## Step 3 — my own mutants (owner's suite, all 56 tests; full output in `mut/mkmut.py`)
| Mutant | Suite | Non-equivalence probe (`mut/probe.py`) |
|---|---|---|
| MR1 AC13 compares adjacent links only | **survives** | Row-equivalent (any increase implies an adjacent increase). Naming changes: in `OCT,TYPO25,OLD24,SEP` the mutant no longer names TYPO25 |
| **MR2 AC14 listing positions compressed** (`n_listing` advances only on new hrefs) | **survives** | `OCT,OCT,TYPO25,SEP`: fixed UNSURE, **mutant `BULLETIN` NOT_READ 0** (fail-open) |
| MR3 AC15 future guard keyed on slug END, not START | **survives** | CX1 shape, run 2027-01-02: fixed UNSURE, mutant silent (the input is near-impossible: the run date falls inside the real newest's window) |
| MR4 AC16 two-year span bound 14 → 33 d | **survives** | `17th December 2026 - 1st January 2027`: fixed None, mutant parses. Only 34 d is tested |
| MR5 AC16 two-year END-before-START bound dropped | **survives** | `4th January 2027 - 29th December 2026`: fixed None, mutant (01-04, 12-29) |
| MR6 AC16 left digit boundary dropped | **survives** | Only `x129th December…` distinguishes it: near-equivalent on any realistic text |
| MR7 AC16 "final" removed (falls through to WIN_RE) | **survives** | `15th December 2025 - 27th December 2026`: fixed None, mutant (12-25, 12-27), an N2 mis-parse |
| MR9 single-date note on any non-title basis | **survives** | A slug-window basis is mislabelled "single date … END unknown" (text only, louder) |
| MR10 AC13 compares START | **survives** | near-equivalent for weekly windows |
| MR11 AC15(ii) ties fire | **survives** | louder only |
| MR12b AC16 second year inferred from the months (printed year ignored) | caught (1 F, `test_two_year_guards`) | — |
| Owner M8, M13, M20, M22, re-built and spot-checked | caught | M8 4F · M13 1F · M20 2F · M22 2F: match the owner's counts |
| FIX_leftmost_precedence (candidate fix, not a defect) | 56 OK | fixes CX-A (STALE, NOT_READ 1); identical to HEAD on every other CX and on the whole fuzz corpus |

## Step 4 — cold read of the operator text
The README (`feed/README.md` :13–:15, :39) and both acceptance files are honest on status: :39 says "IMPLEMENTED and TESTED … NOT independently verified". :15 carries "⚠️ Not guaranteed". READ 3's ❌ class (an absolute guarantee that contradicts the declared residue) is **not** repeated. Three over-reaches remain, all below ❌: (a) "three cases are still silent" (README :15; ACCEPTANCE_L661 :58 "stated so no surface over-claims it"; :82) reads as exhaustive, but CX-E and CX-D2 are further silent shapes, and so is CX-A until it is fixed. (b) README :13 says "the dated links below it never get LATER down the page" for a `BULLETIN` row, and :15(c) says the same; CX-E is a `BULLETIN` row where they do. (c) "up to ~6 days early" (README :14, the code's STALE cause) undercounts the live page's 8-day windows (19–26 Jul, 22–29 Jun), where a START date is 7 days before the END.

## Step 5 — assertion ledger

### ❌
**❌1 AC16's "a two-year match is final" overrides the leftmost one-year title window. This is a new fail-open path: a stale bulletin reads fresh.**
- **Claim:** ACCEPTANCE_L661:36 "Must not regress: every one-year form that already parsed … parses to the same window". :84 names the guards (left digit boundary, 0–14-day span, "a two-year match is final"). :87 says "Every change fails closed except AC16".
- **Artifact:** `AGENTS/OSPREY/scripts/strike_feed.py:134-143` (`m2 = re.search(WIN2_RE, t)` is tried first and returns, :135); `bulletin_window` is applied to the first listing's full anchor text at :178.
- **Command:** `python3 -B cx/cx.py new/tests new/strike_feed.py old/strike_feed.py`, case CX-A, plus the direct-window lines.
- **Observed:** title `Maritime Security Report: 21st - 27th September 2026. Our next report, covering 28th September 2026 - 4th October 2026, will follow.`, run 2026-10-08, days_back 10.
  - HEAD: `BULLETIN — read manually`, NOT_READ=0, pub 2026-10-04, window 2026-09-28..2026-10-04 (title). Its AC15 check (title vs slug, 1 day apart) stays silent.
  - `4ea2b4539`: `BULLETIN_STALE`, NOT_READ=1, pub 2026-09-27.
  - Same mechanism: `…22nd - 28th December 2026 - 4th January 2027` gives a later END (01-04 vs 12-28).
  - It is a regression in the exact direction the owner asked readers to attack. The released code is correct here. No test, declared residue item or README case covers it. The suite is blind both ways: FIX passes 56/56.
  - **Reachability today: none.** 14/14 matching anchors are title-only on both fixtures and on the full untrimmed 10/16 page (`cx/live.py`). The trigger needs an index layout change that puts extra text, holding a later full-date pair, inside the first matching anchor.
- **Proposed change:** in `bulletin_window`, `m1 = re.search(WIN_RE, t)`, then take the two-year branch only `if m2 and (m1 is None or m2.start() <= m1.start())` (leftmost-start precedence).
  - Verified in scratch (`mut/src/FIX_leftmost_precedence.py`): 56/56 OK. Identical to HEAD on all 13,140 generated one-year strings and all 162 two-year strings (`cx/fuzz.py`). R3-I2 is unchanged, because WIN_RE's only match there starts inside "2026", to the right of WIN2's. CX-A becomes STALE, and the released behaviour returns on extra-text titles.
  - Add CX-A as a test that fails on HEAD and passes with the fix.
  - This is a fix after the read, so it is unreviewed under the review budget. PROME rules on the next read.

### ⚠️
**⚠️1 AC13 compares first listings only, while AC13 and the README use listing semantics.**
- **Claim:** ACCEPTANCE_L661:19 defines a "Listing" (a link can be listed more than once). :21 AC13: "END is EARLIER than the END of some dated link listed below it". README :13 "never get LATER down the page", :15(c).
- **Artifact:** `strike_feed.py:206-208` (`below` is ordered by `first`, and `later` scans `below[k+1:]` by item, not by listing).
- **Command:** cx.py case CX-E.
- **Observed:** `OCT, SEP, TYPO25, SEP`, run 10/13, gives `BULLETIN`, NOT_READ 0. TYPO25 is not last on the page, and the listing order breaks monotonicity (2025-10-11 above SEP's second listing, 09-27), so this case sits outside declared (i)–(iii).
- **Realism:** low. Every dated link below the typo'd newest would have to be a repeat listing of a link above it.
- **Proposed change:** in AC13, let a later link count if ANY of its `occ` positions lies below the candidate's first listing, and add CX-E as a test. Alternatively, narrow the AC13 and README wording to "first listing" and add the shape to residue (i).

**⚠️2 The suite leaves the AC13×AC14 overlap and three of AC16's four claimed guards unpinned. 10 of 11 own mutants survive.**
- **Claim:** ACCEPTANCE_L661:78 "15 applied, all caught"; :84 guards.
- **Artifact:** `test_strike_feed_L661.py:152-158` (two-year guards tested only at 371 d and 34 d), :96-101 (the only test with a featured copy directly above).
- **Command:** `python3 -B mut/mkmut.py`; `python3 -B mut/probe.py`.
- **Observed:**
  - **MR2** turns `OCT,OCT,TYPO25,SEP` silent, and the suite passes.
  - MR4 (span 33 d), MR5 (END before START allowed) and MR7 ("final" removed, which re-admits an N2 mis-parse) all survive.
  - MR6 shows the left digit boundary is near-equivalent on realistic text, so it is described as a guard but protects ~nothing.
  - MR3 survives, but only on a near-impossible input.
  - The owner's own mutants that I spot-checked are caught as claimed.
- **Proposed change:** add four small tests: CX-F ⇒ UNSURE; a two-year 15-day span ⇒ None and a 14-day span ⇒ parse; a reversed two-year string ⇒ None; `15th December 2025 - 27th December 2026` ⇒ None. Plus CX-A (❌1). Describe the left boundary as belt-and-braces, not a guard.

**⚠️3 The declared residue "three cases are still silent" reads as exhaustive, and it is not.**
- **Claim:** README :15 "three cases are still silent: (i)…(iii)". ACCEPTANCE_L661:58 "stated so no surface over-claims it"; :82.
- **Artifact:** same lines.
- **Command:** cx.py cases CX-D2, CX-E, CX-C5.
- **Observed:**
  - CX-D2 is pre-existing (OLD is also silent). A forward-dated typo on a pinned non-newest link (title = slug, START ≤ run date) becomes the followed link and masks a stopped publisher.
  - CX-E is ⚠️1's shape.
  - (i)'s "LAST on the page" is narrower than the true condition: no dated link first-listed below it ends later.
  - A cheap partial tell exists for CX-D2 and CX-C5: the followed window ENDS AFTER the run date, which an honest weekly bulletin, published after its window closes, never does. It would not fire on either live fixture (END 10-04 < 10-09; 10-11 < 10-16).
- **Proposed change:** reword as "known silent cases include …", add CX-D2 and CX-E, widen (i) as above, and record an "END after run date ⇒ doubt" rule as a candidate for a later episode (acceptance first).

**⚠️4 Minor precision and pinning.**
- **Artifact:** README :14 and `strike_feed.py:337` ("up to ~6 days early"); MR1, MR9, MR10, MR11.
- **Command:** mkmut.py and probe.py; the fixture titles 19–26 Jul and 22–29 Jun.
- **Observed:**
  - The live 8-day windows make the single-date (START) undercount 7 days, not ~6.
  - The note names a different link under MR1, but the row is unchanged.
  - MR9 mislabels the slug-window basis (text only).
  - MR10 and MR11 are near-equivalent or louder only.
- **Proposed change:** "up to ~7 days early" (or "a week"); optionally assert that TYPO25 is named in a 4-link order test, and add a slug-basis note assertion.

### ✅
1. Suite: 56 OK, rc=0; isolated mode OK for each file (Step 1).
2. Fails first: 11 F / 13 pass-by-design on `4ea2b4539`, labels as stated (Step 1).
3. The owner's mutants M8/M13/M20/M22 are caught with the claimed failure counts.
4. AC16 must-not-regress holds on 13,140 generated one-year title and slug forms (within- and cross-month, "to", no-space, `-1`). The 162 generated two-year forms all parse, none implausibly. `single_date` matches the released inline regex on the whole corpus (`cx/fuzz.py`).
5. AC16 also removes two N2 mis-parses that the released code makes (reversed two-year, and `15th December 2025 - 27th December 2026`).
6. AC16 guards hold on every adversarial window I tried: END before START, 15-day span, invalid date, year +2, year −1 (Step 2 table).
7. R3-I2 is fresh at 01-12. STALE at 01-15 and 01-20 is exactly the one-year cutoff rule (CX-B).
8. The AC15 threshold is exactly as declared (180 silent / 181 fires) on one-year and two-year titles (CX-C1/C2, CX-J1/J2). AC15(i) and (ii) fire on the page's own one-year convention (CX-C3, CX-C4).
9. AC13 fires across a year boundary with two-year windows (CX-D). The AC14 overlaps behave (CX-F, CX-G, CX-G2).
10. AC21: the full untrimmed live 10/16 page gives 14 links, 14 listings, followed 5–11 Oct, 0 doubts at 10/16, 10/19, 10/22 and 10/26.
11. AC18: L624 AC12 is reworded in place. `git show 88d715d03:…ACCEPTANCE_L624…` shows the original wording at :94. The named test exists (`test_strike_feed_L624.py:337`).
12. "Only AC16 can make a row quieter" holds in code. AC10(a) `first < followed.first` is the released `i < pos`, and the AC14 `first < followed.last` adds to it. AC13/AC15 only append reasons. The parse dedup still keeps the first listing's data.
13. The four completion states are unmerged. INDEPENDENTLY VERIFIED: NO pending this read (ACCEPTANCE_L661 :80). README :39 matches.

POINTERS: 11/11 resolve (DOCKET :661, both acceptance files, both test files, both fixtures, README, READ 3 ledger, OSPREY memo §1, commits e5fe3a692 / 48342e63a / 4ea2b4539 / 88d715d03). Dead: none.
ONE-LINE VERDICT: STILL UNRESOLVED (❌ = 1, AC16's "two-year match is final" lets later date text in the anchor make a stale bulletin read fresh, unlike the released code; the fix is one line and verified in scratch). ⚠️ = 4. The code is acceptable for unattended use on the current title-only layout pending ❌1.
