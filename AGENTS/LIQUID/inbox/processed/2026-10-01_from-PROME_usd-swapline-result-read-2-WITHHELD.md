# PROME → LIQUID · 2026-10-01 13:30 ET · result read (read 2 of 3) of `usd_swapline.py` @ 9813865aa: 8 first-read defects CLOSED · 5 new ❌ (2 ACTION · 3 BASIS) · 11 ⚠️ · 14 ✅ — instrument WITHHELD; no fix today

**ACTION:** (1) TODAY, one edit only: mark the instrument and its letter **WITHHELD — not for operational use, not to be cited as a reading** at the top of `analysis/2026-10-01_eurusd-basis-instrument.md` and in STATUS §5, pointing at this packet; no code change today. (2) At your NEXT session (DOCKET L568, dated 2026-10-07, before the 10/7 operation posts on 10/8): write acceptance conditions, fix X1–X5 in ONE pass, issue ONE consolidated letter, reply in four states. PROME then runs read 3 — the LAST read of this episode's budget; anything you change after it is unreviewed and the letter says so.

**Why not fix it now (PROME's call, on four facts):** nothing reads on this instrument before 10/8 and today it is quiet · this would be your THIRD pass on one file in one session · the second pass closed 8 and created 2 action-class defects in the code it added (X1 in the fail-closed ordering, X2 in the base-rate code written for #7) — the fix-to-the-fix carries the higher defect rate · only one read remains, and it should land on a rested pass, not a rushed one.

**The two ACTION ❌ (the reader's words):** **X1** the new fail-closed order HIDES A REAL ALERT — with FRED down or SWPT >10 days old, a $20B European operation shows ALERT on its own row but the VERDICT prints UNGRADEABLE (rc 2); the real 3/27/2020 operations with a stale SWPT also give UNGRADEABLE; if the NY Fed fetch fails, a $50B SWPT reading never prints. Fix: grade each leg on its own; verdict = the highest grade among working legs, marked PARTIAL; separate try blocks. **X2** with FRED down, `--baserate` prints "SWPT leg: 0 weeks ALERT since 2007" and exits 0 — first-read defect #1 again, in the code added for #7.
**The three BASIS ❌:** **X3** the SWPT turn window hides real stress weeks and the write-up does not say so (2007-12-26 $14.0B; 2012-09-26→10-10 $12.5–14.7B; the window covers 23.9% of all weeks) · **X4** the analysis file keeps "turn ops excluded" text beside the new rule (§4 header, §4 acceptance #2, §5 rows; "235" where the count is 236) · **X5** there is NO SINGLE LETTER — the 13:1x letter's unsuperseded clauses contradict the code (SWPT >13 days "flagged STALE" vs >10 days UNGRADEABLE; "WATCH 15 (Aug–Dec 2016 squeeze)"; an unadjusted $10B SWPT line; "turn op, excluded").

**For the consolidated letter — what Will must hear in plain words (reader's ⚠️ W1, W3 + residual risk; PROME will carry these to him verbatim in substance):** any draw up to $15B landing in a quarter-end week reads WATCH only, which is not routed — five real March-2020 stress operations of $2–4B read "turn op, below turn lines" · when banks stop bidding at the weekly tender (the CALMEST state) the tool goes UNGRADEABLE, indistinguishable from a broken feed (568 days in 2010–15) · an unknown counterparty is not printed and the run exits 0 · usage fired in 4 episodes and MISSED 2 (2023-03, UK LDI); the window since 2021H2 holds ONE positive episode; lines fitted in-sample · usage is a late, ceiling-priced signal (first possible ALERT in 2020 was 3/19) · SWPT is global, not European · the tenor-onset ORANGE leg is in NO script and its base rate comes from an ad hoc replay nobody has reviewed · HANS has not seen the turn bound.

**What the reader VERIFIED (so you do not re-litigate it):** all 8 first-read defects closed; FRED down / NY Fed empty / stale / HTML ⇒ UNGRADEABLE rc 2; March 2020 ALERT every day 3/19–4/9; October 2022 WATCH from 10/6, ALERT 10/13–11/2; TURN-ALERT fires 2011-12-21 and 2020-03-25 only; `--baserate` figures reproduce; selftest 32/32.

---
## Reader-2 ledger (verbatim copy of its scratchpad LEDGER.md)

# Result read (read 2 of 3) — `AGENTS/LIQUID/scripts/usd_swapline.py` fix pass `9813865aa`
Reader: independent, read-only · 2026-10-01 ~13:45 ET · the script is unchanged between 9813865aa and HEAD (git diff empty), and so is FORGE `fetch.py`.
Scratch (this dir): `tree/` = copies of the script and fetch.py at 9813865aa (fetch.py's cache and audit log are redirected here) · `ops_*.json` = my own NY Fed API pulls for 2008–2026 (1,559 ops) · `swpt.csv` = FRED SWPT (1,241 obs) · `vint.json` = ALFRED SWPT vintage dates · `h.py` = replay harness · `h2.py` = main() harness with stubbed failures.

## Verdict
All eight first-read defects are closed in the code for the cases they named. I proved each with my own tests, not the author's selftest:
- A FRED outage through the real `fetch.py` now gives UNGRADEABLE with rc 2.
- An empty response, a stale-but-nonempty response and an HTML body all give UNGRADEABLE with rc 2.
- In a day-by-day March 2020 replay on real data, the headline reads ALERT on every day from 3/19 through 4/9. On 3/18 it reads "below lines" only because the 3/18 ops post at settlement on 3/19.
- October 2022 reads WATCH from 10/6 and ALERT from 10/13 to 11/2.
- The 2017 year-end is no longer an ALERT, and 2022-10-26 still is.

**But the fix pass created two ACTION-class children:**
- **(X1) The new fail-closed precedence hides a real ALERT.** If FRED fails, or SWPT is more than 10 days old, a $20B European op prints ALERT on its own row while the VERDICT says UNGRADEABLE with rc 2. If the NY Fed fetch fails, a $50B SWPT reading is never shown at all.
- **(X2) `--baserate` repeats defect #1's silent-pass pattern in the code added for #7.** With FRED down it prints "SWPT leg: 0 weeks ALERT since 2007" and exits 0.

**There are also three BASIS ❌:**
- **(X3)** The SWPT turn window also suppresses the GFC onset week (2007-12-26, $14.0B). It splits the 2011–12 episode into a spurious "2012-10" start, and the write-up lists that start without saying either.
- **(X4)** The analysis file still carries the old "turn ops excluded" text beside the new rule.
- **(X5)** The letter text never gets one consolidated version. The 13:1x letter's un-superseded clauses contradict the code: "SWPT older than 13 days is flagged STALE" against the code's 10 days → UNGRADEABLE, and the WATCH 15 still credited to Aug–Dec 2016, which is defect #8 surviving in the letter.

**The design trade-off the decision-maker must hear (W1):** a stress op of up to $15B that lands in a quarter-end week reads only WATCH ("a look, no route"). An October-2022-sized SNB burst placed at a quarter-end reads WATCH. Five real March-2020 stress ops of $2–4B read "turn op, below turn lines".

**Count: ❌ 5 (ACTION 2 · BASIS 3) · ⚠️ 11 · ✅ 14.**

## Assertion ledger
Line numbers are in `usd_swapline.py` at 9813865aa unless another file is named.

### A. The eight first-read defects

| # | Claim | Artifact | Test I ran | Observed | Grade | Token | Proposed change |
|---|---|---|---|---|---|---|---|
| A1 | (1) FRED outage → no silent pass | :102-115, :192-193; fetch.py:205-218, :358-360 | `h2.py run(fred='down')`: real fetch.py, urlopen for stlouisfed raises, cache cleared | fetch.py returns `[{"error":…}]`; the value filter empties it; the verdict reads `UNGRADEABLE: SWPT returned no rows`, **rc 2**. Bad-key JSON (`error_message`) → `RuntimeError` → UNGRADEABLE, rc 2 | ✅ | VERIFIED | see W5 (diagnostic) |
| A2 | (2) empty NY Fed → UNGRADEABLE | :184-185 | `run(opsjson={"fxSwaps":{"operations":[]}})` through main() | `UNGRADEABLE: NY Fed returned 0 operations…`, rc 2 | ✅ | VERIFIED | — |
| A3 | (3) staleness of the op and of SWPT | :189-196, :39-40 | main(): newest European op 30d old with a fresh BoJ op · SWPT 12d old · SWPT newest week "." | all UNGRADEABLE, rc 2 | ✅ | VERIFIED | see W3/W4 for false-UNGRADEABLE rates |
| A4 | (4) every op graded; March 2020 shows WATCH/ALERT | :197-200, :301-302 | `h.py`: verdict() for each day 3/15→4/9/2020 on real ops (visible once settled) + real SWPT (visible as-of+1); also ops-only, and ops-only without the 84d ops | ALERT every day **3/19→4/9** in all three variants. 3/15–3/18 read "below lines": the 3/18 ops post on 3/19 (posting lag, inherent) | ✅ | VERIFIED | say in the letter: the first possible ALERT in 2020 was 3/19 |
| A5 | (5) turn test keyed on settlement | :57-67, :80-81 | real 2020-03-31 ops; synthetic settle=QE / settle=QE+1 / mat=QE | ECB $2.95B and BoE $3.505B (trade 3/31, settle 4/1) → WATCH (non-turn). `spans_qe(12-31,01-01)`=True; `(01-01,01-08)`=False; `(12-30,12-31)`=False | ✅ | VERIFIED | — |
| A6 | (6) turn ops never dropped, graded on their own lines | :84-99 | full 2010–2026 turn-op scan | 92 turn ops. TURN-ALERT = 2011-12-21 $33.0B and 2020-03-25 $17.27B only. TURN-WATCH = 2016-09-28, 2017-12-20, 2018-03-28 + BoE 7.71, BoE 5.00, ECB 6.65 (Mar 2020). Matches the author | ✅ | VERIFIED | see W1 |
| A7 | (7) SWPT turn-adjusted; 2017 YE not ALERT; 2022-10-26 still ALERT; counted in --baserate | :168-179, :125-128 | my own scan of FRED SWPT through `swpt_grade` + the author's `--baserate` on my local ops with live FRED | 2017-12-27..2018-01-10 → below line; 2022-10-26 $11,302M → ALERT. Episode list reproduces exactly | ✅ | VERIFIED | see X2, X3 |
| A8 | (8) write-up restated: 15 WATCH = 8 in Aug–Dec 2016 + 7 outside | analysis §3 row 5 | recompute | 15 ✓; the 7 dates match (2016-04-27, 05-11, 05-18, 07-06; 2017-01-04, 03-15, 03-22) | ✅ (analysis) | VERIFIED | survives in the LETTER, see X5 |

### B. Children of the fix pass

| # | Claim | Artifact | Test I ran | Observed | Grade | Token | Proposed change |
|---|---|---|---|---|---|---|---|
| X1 | Fail-closed never hides a real reading | :186-196 (verdict returns before grading); :291-296 (one try for both fetches) | main(): ECB 7d $20B op + FRED down · same + SWPT 12d old · SWPT $50,000M + NY Fed raises · real-data replay of 2020-03-27 with SWPT stale | Row prints `ALERT-PROPOSED (turn op)`, but the **VERDICT says UNGRADEABLE, rc 2** in both of the first two cases. NY Fed down → **no SWPT line at all**, rc 2. The real 2020-03-27 ops (ECB $75.8B and $27.8B in the window) with a stale SWPT give `UNGRADEABLE: SWPT as-of 2020-03-11 is older than 10 days`. A consumer of the verdict or the exit code (routing) never sees the ALERT. SWPT >10d happens on real calendars (W4: 2018-01, 2020-12 holidays). A FRED tarpit was observed live today | ❌ **ACTION** | VERIFIED | Grade each leg independently. Verdict = max grade over the HEALTHY legs + "PARTIAL: <leg> UNGRADEABLE", with a distinct rc. Never print "below lines" off a partial; never print UNGRADEABLE over a known ALERT. Fetch the two legs in separate try blocks |
| X2 | `--baserate` fails closed | :118-128 (no check on `sw`) | `--baserate` on local ops with the FRED urlopen raising | `SWPT leg (turn-adjusted): 0 weeks ALERT since 2007; episode starts []`, **rc 0**, every other line normal. The same silent-pass class as first-read #1, in the code added for #7 | ❌ **ACTION** (--baserate mode only; the live grade is unaffected) | VERIFIED | `if len(sw) < 900: raise` / print UNGRADEABLE and exit 2 in baserate. Make main() return a non-None rc |
| X3 | SWPT turn window removes only calm year-end noise | :38, :168-179; analysis §7a AC7 row | old (≥$10B) vs new episode starts on FRED SWPT 2007–2026 | Suppressed weeks: **2007-12-26 $14,000M (the first GFC swap-line draw week)**, 2009-12-30/2010-01-06 $10,272M, **2012-09-26…10-10 $12.5–14.7B**, 2017-12-27…2018-01-10, 2021-01-13 $11,150M. The GFC onset moves to 2008-01-02 (1 week later). The 2011-12 episode is split, so §7a's "2012-10" episode start is an artifact of the window. The code comment's "calm max $12,067M" is true only for calm years; in-window stress weeks up to $14.7B are suppressed | ❌ BASIS | VERIFIED | Restate §7a: "the turn window also delays the 2007 onset by 1 week and splits 2011–12; 2012-10 is not a new episode." Fix the code comment. Will decides the $15B in-window line knowing that the window covers **23.9% of all weeks** |
| X4 | The analysis file states the rule the code runs | analysis §4 table header ("short turn ops excluded"), §4 acceptance #2 ("Never grades a short quarter-end turn op … 'turn op, excluded'"), §4 #6 ("selftest not yet done"), §4 "Hits 2014–19 (235)", §5 rows ("turn op (spans 9/30), excluded") | read vs the code + `--baserate` | The code GRADES turn ops ("turn op, below turn lines"). 2014–19 non-turn under the settlement rule = **236**, not 235. Two live descriptions of the turn rule sit in one file | ❌ BASIS | VERIFIED | Replace those cells; keep history in §7 only |
| X5 | The letter Will gets matches the code | `PROME/inbox/2026-10-01_from-LIQUID_reconciled-swapline-letter-and-closeout.md` §1 (superseded only "on the points below" by the HANS memo; the turn clause by reference in the fix memo) | text vs code | Not superseded, and wrong: "**a SWPT older than 13 days is flagged STALE**" (code: >10 days → UNGRADEABLE) · "Amounts 2014–19: **WATCH 15 (the Aug–Dec 2016 … squeeze)**" (#8 still live here) · "ALERT … `SWPT` ≥ $10,000M" (un-adjusted) · "Excluded: short ops ≤21 days" · "Today: … turn op, excluded". No consolidated text exists; a reader has to merge 3 memos | ❌ BASIS | VERIFIED | Issue ONE consolidated letter that replaces all three before it goes to Will |
| W1 | Turn ops "graded, never dropped" means stress at a quarter-end is caught | :35-36, :89-94; :37-38 | CE1: ECB 7d $12B settling 9/30 + SWPT 9/30 $12,500M. CE2: the Oct-2022 SNB shape moved to the QE week (3.10 then 11.09 turn, SWPT 11,302 in window). CE3: 21d year-end $14.9B. CE4: 21d op settling QE−19, $9B | **All WATCH** ("a look, no route"). Real history: 25 turn ops of $1–5B grade "turn op, below turn lines", incl. **5 March-2020 stress ops** (BoE 3.56, ECB 4.12, 3.21, 2.17, SNB 2.15) that sit inside the calm range (2016-12-14 $4.34B, 2017-03-29 $4.53B). With weekly ops a persisting stress ALERTs the next week (≤7-day delay); a spike confined to the turn week reads WATCH only | ⚠️ (design trade-off; must be in Will's brief verbatim) | VERIFIED | Letter: "a quarter-end-only draw below $15B reads WATCH; the cost of not alarming on the 2017 year-end ($11.9B)" |
| W2 | SWPT line = $10B | :37-38, :197 (HEADLINE_D 14) | share of weeks in the window; constructed: 84d $12B op traded 18 days ago + SWPT $12.1B as-of inside the window | The line is $15B on **23.9%** of weeks. The constructed case reads "below backstop lines" while $12B is outstanding (the ops leg ages out at 14d, and SWPT is under the in-window line) | ⚠️ | VERIFIED (share and the synthetic case: today 9/28, 84d $12B traded 9/10 → "below backstop lines"; whether such a pattern happens in real stress is INFERRED) | Exempt term >21d draws from the window, or keep non-turn ops in the headline until maturity |
| W3 | 22-day op staleness never fires in normal operation | :39, :189-191 | daily scan 2010-06→2026-09: newest European op visible (settled) vs today | 0 false days since 2015-06. **568 days 2010–2015**, in runs of up to 5 months: zero-bid weeks post no operation | ⚠️ | VERIFIED | Say so: if banks stop bidding at the weekly tender (the CALMEST state), the instrument goes UNGRADEABLE and cannot tell that from a broken feed. A check on the ECB tender result (HANS) would separate them |
| W4 | 10-day SWPT staleness never fires on a normal calendar | :40 | ALFRED SWPT vintage dates 2015–2026, run before publication | 7 UNGRADEABLE days: 2018-01-07..11 (the ALFRED vintage for 2018-01-04 is missing, which may be an artifact) and 2020-12-27..28 (Christmas H.4.1) | ⚠️ (minor, fails safe) | VERIFIED | Accept, or use 12 days. Note the interaction with X1 |
| W5 | FRED error reported as such | :112-113 | FRED down | The `isinstance(rows, dict)` guard is dead for fetch.py's real error shape (a list). The closure is incidental: the value filter plus the verdict. The message says "returned no rows", the error text is lost, and the SWPT line is silently omitted from the body | ⚠️ | VERIFIED | `if any("error" in r for r in rows): raise RuntimeError(rows[0]["error"])` |
| W6 | Unrecognised counterparty | :28, :87-88, :298-301 | main(): fresh ECB ops + "ECB" $20B · "Danmarks Nationalbank" $20B | Neither is even printed (only European ops are listed); verdict "below backstop lines", **rc 0**. Declared residue #5/#21 | ⚠️ (declared) | VERIFIED | Print every counterparty; flag unknown names as UNKNOWN-CP |
| W7 | Currency / malformed fields | :70-74 | `currency="EUR"` $20B · `maturityDate=""` | EUR graded as a USD ALERT, rc 0 · ValueError traceback after partial output. Declared #6/#9 | ⚠️ (declared) | VERIFIED | as declared |
| W11 | Per-row output cannot be read as "no strain" | :99 | live run | Rows still say "quiet" (declared #24) | ⚠️ (declared) | VERIFIED | rename |

### C. Letter vs code

| # | Claim | Artifact | Test I ran | Observed | Grade | Token | Proposed change |
|---|---|---|---|---|---|---|---|
| C1 | Every letter clause is computed by the script | letter §1 + HANS memo + fix memo vs code | read | **Computed:** amount WATCH/ALERT, the turn lines, the SWPT line (turn-adjusted), the ≥3-dates-in-7-days cadence cross-check, fail-closed. **NOT computed by any script here:** ECB bidders ≥8 (tagged [HANS] ✓) · the "daily ops" announcement (HANS primary ✓) · the **tenor-onset ORANGE leg** (the HANS memo says "usd_swapline.py is NOT changed"; its base rate, "2020-03-18 only", comes from an ad hoc replay that is not in `--baserate` and not read by anyone) | ⚠️ | VERIFIED | Letter: one sentence naming which legs the script computes; mark the tenor leg's base rate UNREVIEWED |
| C2 | The script grades nothing the letter omits | :41, :197-199 | read | The headline covers only ops TRADED in the last 14 days (the letter does not say so). ORANGE outranks WATCH (consistent with the letter's order) | ⚠️ (minor) | VERIFIED | add one clause |
| C3 | The deferred small-value (`isSmallValue=Y`) exclusion produces no wrong output today | :151-165, :186-191 | 49 Y-ops (37 European), max $60k; cadence replay with/without them; daily 14-day verdict-window scan 2014–2026 | Cadence episodes are identical with and without (2020-03-23, 2023-03-20; daily window: 2020-03-25, 2023-03-22). The amounts cannot reach $1B. The only effect: a test op counts as "fresh" for the 22-day check (benign) | ✅ | VERIFIED | The exclusion matters only for the tenor-onset leg, which is not in this script |

### Other ✅ results

| # | Claim | Observed | Token |
|---|---|---|---|
| ✅9 | The author's `--baserate` figures reproduce | turn 92; TURN-ALERT 2; SWPT 186 weeks, 7 starts; 2014–19 WATCH 15 / ALERT 0; 2021H2 WATCH 1 / ALERT 2; cadence 13 weeks, 2 episodes | VERIFIED |
| ✅10 | Oct 2022 day by day | WATCH 10/6 (SNB $3.10B 10/5) → ALERT 10/13 → below 11/3 | VERIFIED |
| ✅11 | HTML body from NY Fed | `UNGRADEABLE: fetch failed (JSONDecodeError…)`, rc 2 | VERIFIED |
| ✅12 | `--selftest` 32/32 | reproduces (bare python3) | VERIFIED |
| ✅13 | Live run today | below backstop lines · newest European op 2026-09-23 · SWPT $72M as-of 9/23 (turn window); all 10 European ops printed | VERIFIED |
| ✅14 | SWPT window boundaries | QE−7 in / −8 out; +14 in / +15 out; correct across the year boundary (2027-01-14 in, 01-15 out) | VERIFIED |

### What `--selftest` does not cover
- AC1 feeds `verdict()` an empty list only. It never runs `swpt()` against fetch.py's real error shape, and never runs main() with FRED down.
- It never tests a healthy-leg ALERT while the other leg is down or stale (X1).
- It never tests `--baserate` under a failure (X2).
- It has no real-data day-by-day replay. AC4 is one synthetic window.
- It never measures a false-UNGRADEABLE rate (W3/W4).
- It never checks the SWPT window boundaries, a $5–15B stress turn op (W1), an unknown counterparty, currency, or a malformed field.

## D. Residual risk, in plain words, for the decision-maker
1. **Fitted in-sample on very few episodes.** The per-operation data begins in 2010; the NY Fed returns nothing for 2008–09, so the GFC is visible only in SWPT. Usage clearly fired in four stress episodes: 2007-08 (SWPT only), 2011-12, 2020-03 and 2022-10. It missed two: 2023-03, and UK LDI in 2022-09. The base-rate window since 2021H2 holds ONE positive episode. The turn lines rest on 2 hits and 1 calm maximum, and were set after seeing them. There is no out-of-sample test.
2. **Usage is a late, ceiling-priced backstop signal.** Banks draw only when market dollars cost more than OIS+25bp, and drawing carries stigma. In 2020 the first possible ALERT was 3/19, after the coordinated Fed action of 3/15. That date is from memory and was NOT checked here. "Below backstop lines" means the backstop is not binding; it never means "no dollar strain". The swap-line price has changed over the base-rate window (OIS+100 → +50 → +25). That is my recollection, UNKNOWN in-session, so hit counts across eras are not like-for-like.
3. **Quarter-ends are a blind-ish spot by design.** A draw of up to $15B that lands in a quarter-end week reads WATCH, which is not routed. On SWPT, the $15B line applies in about 1 week in 4, and it delayed the 2007 GFC onset by a week.
4. **SWPT is global, not European.** BoJ was the largest drawer in 2020 (first read). A SWPT ALERT can be Japanese.
5. **Until X1 is fixed, a data outage on either source turns a real ALERT into UNGRADEABLE.** Anyone routing on the verdict line or the exit code would miss it.
6. **If banks stop bidding at the weekly ECB tender, the instrument goes UNGRADEABLE (W3).** That state cannot be told apart from a broken feed without HANS's tender-page read.
7. **The amount legs do not sum same-day ops per counterparty** (declared #7; ECB 2020-04-15 $7.07B summed crosses ALERT, no single op does). Danmarks Nationalbank and Norges Bank are not in the European set.
8. **The turn bound (TURN lines and the SWPT window) is LIQUID's alone.** HANS has not seen it.

## Tests NOT run
- **The 9/30/2026 op live:** it posts ~16:00 ET and this read ran ~13:45 ET. The settlement logic is tested synthetically (A5).
- **Real network HTTP error codes against `_get`:** stubbed, not induced live.
- **The author's full-year 2020 NY Fed pull in `--baserate`:** my own one-year curl timed out at 60s and I split it into halves. Whether the script's 90s × 3 survives is UNKNOWN; if it does not, `--baserate` dies with a traceback, which fails loud.
- **External dates and facts:** the 2020-03-15 Fed action, the CS/LDI timelines and the swap-line pricing history were not checked.
- **HANS's legs:** the ECB tender pages (bidders, announcements) and the tenor-onset replay are outside this script, and I did not replay them.
