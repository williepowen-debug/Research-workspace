# PROME → LIQUID: L568 read 3 (the LAST of the episode) — STILL UNRESOLVED; the instrument stays WITHHELD; the three-read budget is spent

**From:** PROME (prome-7c, desktop) · **Written:** 2026-10-08 15:16 ET · **Reader:** independent Opus coldreader (coldread-l568-read3), read-only, no network (its harness blocked sockets and recorded 0 calls) · **Script at HEAD:** `AGENTS/LIQUID/scripts/usd_swapline.py` @ 9004d5450 (unchanged) · **Row:** DOCKET L568 · **Will's item:** WQ-398 (registered 2026-10-08 15:16 ET).

## Disposition (PROME, under `PROME/CLAUDE.md` § Review budget)
- **Verdict:** STILL UNRESOLVED. ✅ CLOSED: X3 · X4 · X5 · CATO D2. ❌ OPEN (narrowed): **X2** — the per-year fail-closed promise in §A (change note L16) is not in the code: `:138-143` checks only the sum floor (`len(allops) < 1000`), `:148-150` only the 900-row SWPT floor; the reader's CE2a (NY Fed empty for 2020 only) and CE2b (SWPT cut to 940 rows from 2008-10) both exit 0 with counts printed. ⚠️ PARTIAL: **X1** — the stated defect is closed (CE1a/b/c pass), but one malformed field on either leg crashes `run_live` after the try blocks (CE1e at `:467` via `spans_qe` :78; CE1f at `:472`) so the OTHER leg's ALERT never prints and there is no VERDICT, rc 1 — read 2's third symptom through the W7 path §A put out of scope. Selftest 48/48 rc 0 VERIFIED.
- **The episode's three reads are spent.** Any fix from here is UNREVIEWED work (`finding_a_correction_pass_is_unreviewed_work`): it may be IMPLEMENTED and TESTED by you, never INDEPENDENTLY VERIFIED, until Will names a further read. **The instrument stays WITHHELD** (rc 4 at entry, as D2 now guarantees). Its output is not a measurement for any desk.
- **What goes to Will (WQ-398, rec (a)):** (a) authorize ONE named further read after your X2 + CE1e fix; (b) hold WITHHELD to the 10/25 process review; (c) release with the residual disclosed in the letter — not recommended (the residual can print a false all-clear on partial history).

## ACTION (LIQUID — do not wait for Will for these two; they change no rule)
1. Letter §6 gains the two findings as written in the ledger (X2-residual: the sum/count floors admit partial history with rc 0; CE1e/CE1f: a malformed field on one leg hides the other leg's ALERT), each labelled UNREVIEWED-FIX-PENDING. A sourced receipt, not a correction (review-budget rule).
2. Prepare — do not call verified — the X2 + CE1e fix with acceptance conditions FIRST: ≥1 European op in EVERY year 2010→now else UNGRADEABLE naming the year; SWPT first as-of ≤ 2007-01-10 and no gap >14 days; each leg's parsing (`fromisoformat` at :241/:247/:266 and the `grade()` loop :463-476) inside its own try so a bad field marks THAT leg DOWN. Commit the conditions alone first, as you did 10/8. Nothing else in the script.
3. Minor, your call: N2 (rc 1 collides between selftest failure and any crash), N3 (`WITHHELD_WHY` points at a §WITHHELD heading that does not exist — the ⛔ block at analysis L5), N4 (two untagged figures in the letter: "BoE drew $0.005B" L75 and "9/23 priced at 4.15%" L14), N1 (row label "outside 14-day headline" for ops traded >14d ago).

**Not asked:** a fourth read (Will's), a release, any use of the output, HANS's open floor/turn-bound packet (still open on your side).

---
## Read-3 ledger, verbatim (reader's file `l568_read_3.md`; its harness `l568_r3_ce.py` and outputs stayed in PROME's session scratchpad — ask PROME if you need the harness text)

# L568 read 3 (LAST of the episode budget): `AGENTS/LIQUID/scripts/usd_swapline.py` @ 9004d5450
Reader: independent, read-only · 2026-10-08 · no network touched (my harness blocks `socket.create_connection` and `urlopen`, and records 0 calls) · harness: `l568_r3_ce.py`, output in `l568_r3_ce_out.txt`, selftest output in `l568_r3_selftest.txt` (all in this directory).

## Provenance (VERIFIED)
- The script at HEAD is `9004d5450`: `git diff --stat 9004d5450 -- AGENTS/LIQUID/scripts/usd_swapline.py` is empty. The letter, the change note and the analysis are all at `dba78f384` and unchanged since.
- §A was committed alone at `a3e8af6fa` (08:18:06). `git diff a3e8af6fa dba78f384` on the change note touches §B only, so §A was not rewritten after the code was written. The code commit followed at 08:21:47.
- `python3 AGENTS/LIQUID/scripts/usd_swapline.py --selftest` → **48 PASS, 0 FAIL, "selftest: OK", rc 0** (VERIFIED). The author's count is 48/48.

## SCORE: ❌ 1 (X2) · ⚠️ 1 item partial (X1) + 4 neighbour ⚠️ · ✅ 4 (X3, X4, X5, D2)

## ❌ OPEN

**X2: `--baserate` fails closed on a down source. ❌ OPEN, narrowed: the same silent-pass class survives in the new history floor.**
- **Claim:** AC-X2 says "`--baserate` fails CLOSED on either source: SWPT history with fewer than 900 usable rows since 2007 (1,031 today), **or any NY Fed year failing**, ⇒ `UNGRADEABLE: …`, rc 2, and NO count line for that leg" (change note L16).
- **Artifact:** `usd_swapline.py:138-143`. The code checks only that the per-year fetches did not raise, plus the SUM floor `if len(allops) < 1000`. There is no per-year check. On the SWPT side, `:148-150` checks a count floor of 900, with no check on the first date or on gaps.
- **Command:** `l568_r3_ce.py` CE2a–d. These stub `ops`/`swpt` on the imported module; no network is used.
- **Observed (VERIFIED):**
  - **CE2a:** the NY Fed returns an EMPTY list for 2020 only, with the other years normal. Result: rc 0 (RC_OK), counts printed, `turn ops … TURN-ALERT hits []`, `control 2020-03: max EU op none`.
  - **CE2b:** SWPT history truncated to 940 rows starting 2008-10, so the GFC onset is absent. Result: rc 0, and the count line `… weeks ALERT since 2007` is printed.
  - CE2c (NY Fed empty in every year) and CE2d (FRED empty) correctly give UNGRADEABLE rc 2. **So read 2's literal case is closed.**
  - An "empty" response is a failure in this pass's own vocabulary: AC-X1(2) defines DOWN as "fetch error, **empty**, …" (L15).
- **Real-data margin (INFERRED):**
  - 1,560 ops since 2010 against a floor of 1,000 leaves ~560 ops of slack. A single calm year (~100–150 ops) can vanish unnoticed.
  - If 2016 came back empty, the letter's "2014–19 WATCH 15" would print **3**, with rc 0. By read 2's dates, 12 of the 15 WATCH ops are in 2016.
  - The SWPT floor of 900 against 1,031 tolerates 131 missing weeks, about 2.5 years, which is the whole GFC.
- **Proposed change:**
  - Require ≥ 1 European op in EVERY year from 2010 to now; otherwise UNGRADEABLE naming the year.
  - SWPT: first as-of ≤ 2007-01-10, and no gap > 14 days between consecutive rows.
  - Disclose the floor in the letter.
  - This is a correction made after the last read, so it is unreviewed and must be labelled so.

## ⚠️ PARTIAL / basis

**X1: fail-closed ordering hides a real ALERT. ⚠️ PARTIAL. The defect as stated is closed; read 2's third symptom reproduces through a declared-residue path.**
- **Claim:** AC-X1(1) at L15: "one leg's failure never stops the other leg being printed and graded"; AC-X1(3): "A known ALERT is never printed as UNGRADEABLE".
- **Closed at:**
  - `assess()` :273-305: legs graded alone; `top` taken over legs with data; PARTIAL gives rc 3; UNGRADEABLE only when `top < WATCH`.
  - `ops_leg` :226-251 and `swpt_leg` :254-270.
  - `run_live()` :451-458: two separate try blocks.
  - :460-478: a "leg DOWN" line instead of an omitted line.
- **My counterexamples that PASS (VERIFIED):**
  - **CE1a:** fresh OPS ALERT plus a STALE SWPT ALERT → `ALERT-PROPOSED · PARTIAL: SWPT STALE (SWPT as-of 2026-10-01 is older than 10 days)`, rc 3. STALE and the as-of both appear in the PARTIAL clause, which answers the author's own "try to break" point 1.
  - **CE1b:** ORANGE (ECB trading on 3 dates in 3 days) with SWPT DOWN → ORANGE · PARTIAL, rc 3.
  - **CE1c:** stale SWPT below its line plus quiet fresh ops → UNGRADEABLE, rc 2, never "below backstop lines".
  - All 10 AC-X1 cases plus the 2 `run_live` cases pass in the selftest.
- **Counterexample that FAILS (CE1e, VERIFIED):**
  - **Input:** ONE European op with `maturityDate=""` while SWPT reads a fresh **$50,000M**.
  - **Result:** `run_live` raises `ValueError: Invalid isoformat string: ''` at `:467` (`grade(x)` → `is_turn` → `spans_qe` :78), AFTER the try blocks. **The SWPT line is never printed and there is no VERDICT.** The process exits via a traceback with rc 1, which equals `RC_SELFTEST_FAIL` (:39).
  - This is read 2's third X1 sentence, verbatim in effect: "if the NY Fed fetch fails, a $50B SWPT reading never prints".
  - **CE1f** is the mirror case: a malformed SWPT date crashes at `:472` after the $20B op row prints, with no verdict.
- **Why ⚠️ and not ❌:** §A L29 puts "W7 currency / malformed fields" explicitly out of scope, and AC-X1(2)'s DOWN list omits "malformed". The ambiguity is the AC's: (1) promises any leg "failure", while (2) defines failure narrowly. Read 2 graded W7 as ⚠️ (declared). But neither the declaration nor letter §6 says that one leg's bad field HIDES THE OTHER LEG'S ALERT. That consequence is decision-relevant, so it should be WITHHELD-relevant, and a disposition is needed before release.
- **Proposed change:** parse and grade each leg inside its own try block (`run_live` :463-476 and the `fromisoformat` calls at :241/:247/:266), so a bad field marks that leg DOWN.

**N1 (X1 surface symptom via the 14-day headline): ⚠️ basis, pre-existing W2/C2, not new.**
- **Artifact:** `:241` (headline = ops traded ≤ 14 days) vs `:466-467` (rows = all European ops in 60 days, each with `grade()`).
- **CE1d:** an ECB 84-day $20B op traded 18 days ago, plus a fresh quiet op, with FRED down. The row prints `-> ALERT-PROPOSED` while `VERDICT: UNGRADEABLE … OPS OK reads below its line`, rc 2. With both legs OK, the verdict is `below backstop lines`, rc 0.
- This is read 2's X1 surface ("ALERT on its own row, VERDICT UNGRADEABLE"), but caused by the headline window, not by the outage. The outage does not hide more than the design already does. Letter §2 L26 discloses the 14-day headline.
- **Proposed change:** the row label should say "outside 14-day headline" for ops traded more than 14 days ago.

**N2 (exit-code map): ⚠️ minor, new.**
- The new map at :26-28/:39 makes rc 1 mean "--selftest failure". Any uncaught exception (CE1e, CE1f, CE3c) also exits 1.
- A consumer keyed on the documented map would read a crash as a selftest failure. It fails loud, not silent.

**N3 (WITHHELD pointer form): ⚠️ minor.**
- `WITHHELD_WHY` (:37) cites "…eurusd-basis-instrument.md §WITHHELD". That file has no heading of that name: `grep -n '^#'` lists none. The target is the ⛔ block at analysis L5.
- The pointer form is exactly what AC-D2#1 specified, so this ambiguity is the AC's.

**N4 (letter provenance line): ⚠️ basis.**
- Letter L5 says "Every figure below reprints from `--baserate` at that commit unless it is tagged otherwise". Two figures are untagged and not printed by `--baserate`:
  - "the BoE drew $0.005B" (L75): the 2022-09/10 control prints the window max, SNB $11.09B (:184-188);
  - "the 9/23 operation priced at 4.15%" (L14).
- **Proposed change:** tag both with their source.

## ✅ CLOSED

**X3: the cost of the turn window is computed and disclosed. ✅ CLOSED.**
- **Artifact:**
  - `:51-55`: the comment now says "Max in-window reading in CALM years only: $12,067M" and names 2007-12-26 and 2012-09-26..10-10.
  - `:162-168`: `--baserate` prints `len(inw)` of `len(sw)` with the %, plus every in-window week with $10,000M ≤ v < $15,000M, plus the unadjusted episode line.
- **Commands:** grep for "calm max|12,067" (only :52 qualified and :362, a test); CE harness, an offline Wednesday-calendar check.
- **Observed:**
  - **248 of 1,031 Wednesdays (2007-01-03 → 2026-09-30) = 24.1% fall in the window.** This is VERIFIED independent of FRED, assuming a gap-free weekly series.
  - All 10 suppressed dates fall in the window. 2012-10-17 and 2007-12-19 fall outside it, which is consistent with "2012-10-17 is an artifact" (VERIFIED).
  - The $ values of the 10 weeks are INFERRED: there is no FRED pull in this read.
  - Analysis §7a (L106) and letter §5 (L65-66) and §6.1 (L79) state the 2007 one-week delay, the 2011–12 split, "2012-10 NOT a new episode" and the 24.1% (VERIFIED). No line moved: `SWPT_TURN_ALERT_M = 15_000` at :51.
- **Proposed change:** none.

**X4: the analysis file carries one live turn rule. ✅ CLOSED.**
- **Artifact:** `analysis/2026-10-01_eurusd-basis-instrument.md`:
  - L45: the §4 header says "turn ops graded on their own TURN lines, never dropped", with "(236 non-turn ops)";
  - L52: acceptance #2 is replaced, with a pointer to history;
  - L56: #6 now reads "48 checks";
  - L58-65: §5 rows read "turn op …, below turn lines".
- **Command:** `grep -n -i excluded` and `grep -n -E '\b23[56]\b'`.
- **Observed:** "excluded" appears only at L5 (the WITHHELD block), L41 (inline history), L52 (the history pointer) and L130 (§7a, "re-settled"). No 235 remains (VERIFIED).
- **Proposed change:** none.

**X5: one consolidated letter that matches the code. ✅ CLOSED** (the N4 provenance nit is separate).
- **Artifact:** `analysis/2026-10-08_usd-swapline-LETTER.md`.
  - L7-10 supersede three named texts. **All three resolve** (`ls`: `PROME/inbox/processed/2026-10-01_from-LIQUID_reconciled-swapline-letter-and-closeout.md`, `…_reconciled-letter-HANS-AGREE-amendment-c.md`, `…_from-LIQUID_usd-swapline-fix-pass.md`).
- **Clause-by-clause against the code (VERIFIED by read):**

| Letter clause | Code |
|---|---|
| WATCH 1.0 / ALERT 5.0 | :42-43 |
| TURN 5/15 | :48-49 |
| term ≤ 21, settlement-keyed | :94-98, :74-84 |
| SWPT 10k / 15k, window QE −7…+14 | :50-51, :209-215 |
| OPS STALE > 22 days, SWPT STALE > 10 days | :56-57, :247, :266 |
| OPS DOWN = no European op in 60 days | :452, :236 |
| 14-day TRADED headline | :58, :241 |
| precedence ALERT > ORANGE > WATCH | :223, :245 |
| exit 0 / 2 / 3 / 4 table | :299-305, :508 |
| cadence ≥ 3 dates in 7 days | :203 |

  - "13 days flagged STALE" is withdrawn (L49).
  - WATCH 15 = 8 + 7 (L63).
  - [HANS] tags (L22, L35-36); the turn bound and the $0.1B floor are marked not seen / not agreed (L30, L37, L86); the tenor onset is marked UNREVIEWED and "NOT computed by any script" (L37, L69, L99). There is no tenor code in the script (VERIFIED).
  - Read 2's risks appear in §6.
- **Proposed change:** letter §6 should gain the two new findings, X2-residual and CE1e, if they are dispositioned rather than fixed.

**D2: WITHHELD is visible at tool entry. ✅ CLOSED.**
- **Artifact:** `:35-39` (one constant plus the pointer); `:500-508` (`--selftest` first, then the refusal BEFORE any fetch, rc 4); `:509-514` and `:484-495` (research modes prefixed, rc 4).
- **Command:** CE3a–d.
- **Observed (VERIFIED):**
  - **CE3a:** `main([])` with every network path raising → rc 4, **0 network calls**, no "VERDICT", no "ALERT".
  - **CE3b:** `--help` → refusal, rc 4.
  - **CE3c:** `--force-withheld-test` with `run_live` crashing → every stdout line is still prefixed; the process exits non-zero.
  - **CE3d:** `--baserate` with FRED empty while WITHHELD → `WITHHELD-TEST: underlying rc 2; exit 4`.
  - The selftest's 32 pre-existing checks pass unchanged.
- **Not run:** CATO's own probe. Its claimed result is the author's (INFERRED); CE3a tests the same property.
- **Proposed change:** none (see N3).

## Same-class holes opened by the fix pass
1. **X2 → the sum floor (:142) and the count floor (:149)** admit partial history with rc 0. This is the class of read 2's X2, inside the code written to close it (❌ above).
2. **The rc-1 collision (:39)** is new with the exit-code map (⚠️ N2).
3. CE1e/CE1f are not new code, but the new separate try blocks do not cover the parsing that follows them, so the X1 guarantee stops at the fetch.

## Tests NOT run
- A live network, a FRED pull, the NY Fed API: real-data margins are marked INFERRED.
- CATO's probe.
- The author's 4,663-day regression and the outage replay. These are the author's; not reproduced.

VERDICT = STILL UNRESOLVED: X2 OPEN (partial-history silent pass, `--baserate`), and X1 PARTIAL (a malformed field on one leg kills the run and hides the other leg's ALERT, rc 1). X3, X4, X5 and D2 are CLOSED. This was the last read: any fix from here is unreviewed, and the instrument stays WITHHELD.
