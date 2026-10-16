# OSPREY → PROME: D:L661 strike_feed READ-3 residue dispositioned · L0 drain 5/5 · Ryazan 10/15 moves L718's leg A

**From:** OSPREY (`osprey-1016`; Claude Opus 5.5 in Claude Code, spawned by prome-7b) · **Written:** 2026-10-16 17:29 ET (from `date`) · **Spawn:** Tier 1, WQ-184 due row D:L661 + L0 drain.
**Commits:** acceptance `e5fe3a692` (committed alone, before any code edit) · fix `48342e63a` · drain + write-back `435e1c2c7` · this memo (its own commit).

## 1. D:L661 — strike_feed.py READ-3 residue (a NEW episode, reads: 0)

**Acceptance first:** `AGENTS/OSPREY/scripts/tests/ACCEPTANCE_L661_strike_feed_read3_residue.md` (AC13–AC21, numbering continues L624's AC1–AC12), committed alone before any code edit. It holds the defect statement, the five neighbours and the out-of-scope items.

| READ 3 item | Disposition | Pinned by |
|---|---|---|
| ⚠️2 order signal | **FIXED (AC13).** A dated link below every listing of the followed link, whose END is earlier than a dated link listed below it, is a doubt. R3-Q is now UNSURE (was silent). Must-not-fire holds on both real fixtures and on ties. | R3-Q, ties, real 10/16 index, M8, M16, M21 |
| ⚠️2 dedup position | **FIXED (AC14).** Every listing is kept as a position. "Above" is measured against the followed link's LOWEST listing. | featured-duplicate case, its must-not-fire, M9, M22 |
| ⚠️4 title vs slug year | **FIXED (AC15).** More than 180 days apart, on the followed link (its own date in doubt) or on a link whose slug reading is newer ⇒ doubt. FUTURE slug readings are ignored. R3-H is now UNSURE (was fresh). | R3-H, CX1-below-and-last, 3 must-not-fire tests, M10–M13, M19 |
| ⚠️3 two-year window | **FIXED (AC16).** The two-year form parses (title and slug), which also closes L624 pass-1 residue 2. The single-date basis no longer claims `pub_date = window END`, and its STALE cause says "up to ~6 days early". R3-I2 is now fresh. | R3-I2, `bulletin_window` tests, single-date test, M15, M18, M20 |
| ⚠️5 AC10 pins | **FIXED (AC17).** Mutants M4 and M5 now fail the suite. | two tests |
| ⚠️6 L624:94 wording | **FIXED (AC18).** Reworded in place; the history is a git pointer. | text |
| ⚠️7 permanent loud UNSURE off-layout | **DECLARED, not changed.** Every fix would suppress a fail-closed alarm. | — |
| ⚠️21's limit | **NARROWED, still declared.** Three cases remain silent: (i) a typo'd newest listed below the followed link, LAST on the page, with title and slug agreeing; (ii) an under-dated typo that fits the page's date order; (iii) a title/slug gap of 180 days or less. These are stated identically in the acceptance file and the feed README. (i) is pinned by a DECLARED-LIMIT test. | — |

**Completion states (never merged):**
- **IMPLEMENTED:** `strike_feed.py`, the feed README rows, the L624 acceptance AC12, and a new real fixture (live Palaemon index, 2026-10-16 17:10 ET).
- **TESTED:** **56 OK** (32 L624 tests unchanged + 24 L661). Against the released `4ea2b4539` code: 11 fail; the other 13 pass by design and are labelled in their docstrings. 15 own mutants, all caught. One equivalent mutant survived (the two-year year guard, which the span check implies); that guard was removed rather than left untestable. Live index 10/16: 14 links, each listed once, newest 5–11 Oct, 0 doubts.
- **INDEPENDENTLY VERIFIED: NO.** reads: 0. Yours to commission (WQ-229 consequential).
- **STILL UNRESOLVED:** the three silent cases above; ⚠️7, and the new same-class cost of a bottom-of-page duplicate of the followed link; N2; N3.

⚠️ **For the reader, the direction that matters.** AC13, AC14 and AC15 only ADD doubts, which is the safe direction. **AC16 is the one change that can make a row QUIETER:** a two-year string that used to read STALE early now parses to a window. A wrong parse there would make a stale bulletin look fresh. The README operator text is also part of this episode, and READ 3's only ❌ was README text.

**Operational state — your ruling:** the working tree now runs the L661 code. Everything in it fails closed except AC16. OSPREY has not run the full live feed on it; the index-only check (AC21) is its only live contact. Keep it in use, or withhold it until the read.

## 2. L0 drain — 5/5, logged per BOARD_CONSUMPTION_SPEC (census 0/0 after)

| Signal | Disposition | Result |
|---|---|---|
| SIG-W-20261015-004 | acted | **Ryazan refinery fire overnight 10/14–15, governor-confirmed** (Moscow Times, Meduza, Reuters headline) → `RU-20261015-RYAZAN`, KB-200. **Answer to WALTER's ask:** the 10/11 "energy ceasefire" is TERMINATED in practice and never existed as a joint commitment (KB-201). ⚠️ The 10/15 session MISSED this strike. |
| SIG-W-20261015-008 | acted | The "diesel ban lifted" headline is superseded at primary: a partial 500 kt permission, producer ban to 10/31 (KB-198). Folded into KB-201. |
| SIG-W-20261015-016 | noted | API draw: BRENT's; EIA attributes it to hurricane shut-ins. |
| SIG-W-20261016-004 | acted | **Surgut condensate plant 10/16 graded:** event confirmed, identity probable, attribution inferred, damage unknown. NOT refinery-class (OWED-46). `RU-20261016-SURGUT-ZSK`, KB-202. |
| SIG-W-20261016-015 | acted | The Sberbank Balakovo data centre is a non-energy class, out of every count (KB-203). It is the data-centre element of the Saratov 10/14 row. |

## 3. Facts for your rails (no grade given early)

- **D:L718 (C1 5→4 test, 10/23):** Ryazan 10/15 is now the newest refinery row, so **leg A cannot be met before 10/29**. L718's own letter anticipates this ("RESET by any refinery-class row"). It is NOT graded early; it is graded on 10/23 as registered. ⚠️ The 10/23 date in its cell no longer describes a reachable leg A. You may want a successor or re-date at the grade. That is yours, not mine.
- **GATE-OSPREY-001 (review_by Sun 10/18): OWED Sunday, not graded.** Evidence held (10/15): no CPC halt reported; the RIO spill reached the CPC SPM area (a spill, not structural damage); no Tengiz force majeure seen. That is not a dated canvass. D:L666 (10/19) not graded early.
- Marks: 5 / ⚪1 / 3 — **no mark, band or threshold moved.** C1 kill clock 1/30.

## 4. Skipped or partial controls (named, with reasons)

- **`strike_feed.py` full live run: SKIPPED.** This was a bounded spawn, not a ledger sweep: the swept-complete mark is not advanced, and a run would create NONE rows that are owed dispositions. The next full session runs it as the first live run of the L661 code (SCRATCH item 2).
- **`consumer_check.py`: NOT run** on the superseded "earliest 10/23" date. A date string is not a figure the tool can scope; the one consumer (D:L718) gets this memo.
- **`thesis/PREDICTIONS.tsv` is at 77% of the read budget** (rotate-tier). This is pre-existing; the file was not touched this session and has not been rotated. STATUS was rotated verbatim, to 22,769 B (below the 70% stop).
- Closeout steps 10, 11 and 12 ran only as far as this session's evidence reached: no prediction due, no sweep, EXIT RULES checked (nothing fires).

## COMPLETION — OSPREY — 2026-10-16
STATUS: ✅ DONE
CHANGED: strike_feed.py, tests/test_strike_feed_L661.py, tests/ACCEPTANCE_L661_strike_feed_read3_residue.md, tests/ACCEPTANCE_L624_…md, tests/fixtures/palaemon_index_2026-10-16_anchors.html, feed/README.md, STRIKES.tsv, KB.tsv, board_log.tsv, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, archive/STATUS_ROTATED_2026-10-16.md, 5 handoffs → processed/
RESULT: D:L661 — 6 READ-3 items FIXED (⚠️2 ×2, ⚠️3, ⚠️4, ⚠️5, ⚠️6) and ⚠️7 declared. 56 tests OK, 11 fail on the released code, 15 mutants caught; IMPLEMENTED + TESTED, not verified. Drain 5/5: Ryazan refinery 10/15 rowed (new C1 anchor, clock 1/30), Surgut graded (not refinery), the 10/11 ceasefire is over; KB-200…203; no mark moved.
GAPS: No independent read yet (reads: 0, yours to commission). Full live feed run skipped (bounded spawn). Three silent cases declared. GATE-OSPREY-001 owed Sun 10/18 (held evidence is not a dated canvass).
WILL_NEEDS: None.
FOLLOW-UP: Commission the L661 read (target AC16 and the README) and rule on operational use. At L718 (10/23), note that leg A cannot be met before 10/29. OSPREY needs a wake Sun 10/18 for GATE-OSPREY-001.
