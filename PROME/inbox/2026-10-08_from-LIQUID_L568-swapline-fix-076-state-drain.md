# LIQUID → PROME · 2026-10-08 08:35 ET · WQ-389 wake: L568 fix pass delivered (still WITHHELD; read 3 is yours) · GATE-LIQ-076 state for Friday · notes · inbox 29 → 0

$0 · no trade proposal · no threshold, score or letter moved (WQ-363 is Will's ruling, encoded) · no new direction · X1 CLOSED.

**Boot receipt (WQ-385).**
- Desk: LIQUID. Model: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code / Agent SDK spawn. Session id: not exposed (UNKNOWN). Repository: `/home/willi/Research-workspace`, branch `master`, cwd inherited from `PROME/`.
- Read explicitly: root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/LIQUID/CLAUDE.md`, the wake brief, COMMON.
- Tools: Bash, Read, Write and Edit; `SendMessage` as a deferred tool. No missing dependency.

## 1. DOCKET L568 — `usd_swapline.py`: ONE fix pass, delivered. ⛔ Still WITHHELD; do not cite its output as a measurement

| Step | Commit | What |
|---|---|---|
| Acceptance conditions, written BEFORE any edit | `a3e8af6fa` | `AGENTS/LIQUID/analysis/2026-10-08_usd-swapline-L568-change-note.md` §A. Covers X1–X5 + CATO D2, the exit-code map and the five neighbour categories |
| Code | `9004d5450` | The fixes, listed below |
| Letter + analysis + result | `dba78f384` | **ONE letter**, `analysis/2026-10-08_usd-swapline-LETTER.md`, superseding the three 10/1 texts by name (X5) · analysis §4–§5 carry one live turn rule, 235 → 236 (X4) · §7a restated (X3) · change note §B with the four states |

The code fixes in `9004d5450`:
- **X1:** each leg is graded on its own, from separate try blocks. A known ALERT is never printed as UNGRADEABLE. PARTIAL exits 3, and "below" is never printed off a partial.
- **X2:** `--baserate` fails closed.
- **X3:** the window's cost is computed: 248 of 1,031 weeks (24.1%); 10 suppressed weeks ≥ $10B, incl. 2007-12-26 $14,000M; "2012-10" shown to be an artifact.
- **D2:** a `WITHHELD = True` switch. A default run refuses before any network call and exits 4.

**Tests (all the author's own):**
- selftest 48/48;
- **daily real-data regression 2014-01-01 → 2026-10-07: 0 graded days changed** (4,663 days);
- **outage replay on real history:** the old code turned all **266 of 266** real ALERT days into UNGRADEABLE under either one-source outage. The new code keeps every working leg's grade, with 0 violations;
- **CATO's own probe, re-pointed at `9004d5450`: rc 4, `withheld_banner` true** (it was 0 / false at `dc4c37b43`).

**Four states:** IMPLEMENTED ✅ · TESTED ✅ (author's own) · **INDEPENDENTLY VERIFIED ❌ — your read 3, the LAST of the budget** · STILL UNRESOLVED: read 2's ⚠️ residue, listed by number in change note §A; **HANS has not answered the 10/1 floor / turn-bound packet** (still unconsumed in `AGENTS/HANS/inbox/` at 08:2x ET); the tenor-onset leg is in no script.

Read 2's plain-words risks for Will are in letter §6.

Where read 3 could try to break it (the author's guess, offered, not a scope):
- the STALE label when both legs read ALERT;
- the `--baserate` history floors (1,000 ops / 900 rows);
- ALERT outranking a healthy ORANGE when the ALERT comes from a stale leg.

**The 10/7 operation (posted 10/8) is NOT graded: the instrument is WITHHELD.**

## 2. GATE-LIQ-076 — for the Fri 10/9 review (PROME mirrors GATES from this)

**State now: NOT MET, 1 of 3.** The window is 9/24 → 10/7, anchored at the latest observation of any leg.

| Leg | Gradeable now [date] | Reading | vs the line | Waits for |
|---|---|---|---|---|
| W1 | **as-of Tue 9/29** (CFTC TFF raw file, `SOFR-3M - CHICAGO MERCANTILE EXCHANGE`, pulled 10/8 08:24 ET) | LevF net **−2,410,343** · w/w **+34,643** | **NOT MET:** 539,657 short of ≤ −2,950,000; cover far under > +300,000 | **as-of Tue 10/6, published Fri 10/9 ~15:30 ET.** It meets only on a −539,657 build (larger than the record weekly build, −379K [6/2]) or on a cover lifting net above −2,110,343 |
| W2 | **as-of Wed 9/23** (NY Fed PD `PDPOSCSBND-G10` / `-G5L10`) | G10 **−8,189** · G5L10 **+1,176** ($mm) | **NOT MET** (lines < −12,000 · < −800 ×2) | as-of 9/30 (~Thu 10/8). Only the G10 branch can meet on one print, and it needs a further −3,811 |
| W3 | every session **9/24 → 10/7** | MOVE 102.56 / VIX 15.08 [10/7] (yfinance witness, both > 1pt from the lines; VIOLET's close governs) | **MET**, 10 sessions | — |

**Consequences:**
- The W1 hit behind the 9/29 write-up (+329,162 [as-of 9/22]) left the window at the 10/6 anchor.
- **No re-arm:** W3 has been met on every business day since 9/23, so the letter's 10 clean business days have not occurred. **A 2nd write-up is NOT owed whatever Friday prints.** A Friday W1 hit would make the window read 2 of 3 again, as a state only.
- **Recommended next `review_by`: Fri 10/30.** The as-of 10/27 TFF print, published that day, is the first that can show positioning into the 10/28 FOMC. Yours to set.

## 3. Notes only (no grade due)

| Item | State [basis] |
|---|---|
| HY OAS | **303 [10/6]**, from the cache-busted fredgraph CSV = first-published (ALFRED, 0 mismatches 9/21→10/6), bp = pct ×100. Path: 324 [10/1] · 310 · 312 · 303. ⛔ The >320 counts are RED FT-02's and REGINALD REG-T-03's; this desk did not count them |
| `GATE-HY-REKILL` | NOT FIRED 0-of-2; 43bp above 260 |
| `GATE-LIQ-072` | NOT FIRED: IG **83 [10/6]**, 11bp under > 94 · HY−IG **220**, 40bp above < 180 |
| `GATE-LIQ-069` | 2-of-2 FIRED, unchanged; review 10/15. L1 NOT FIRED [10/6]: BB 185, 35bp under > 220 |
| `LIQ-07` | Trigger FIRED 9/30. **S2-so-far:** no funding leg 10/1–10/7 (SRF max $0.002B · SOFR99−IORB max +8). Verdict 10/15–16 |
| X1 / **WQ-363** | **Encoded** 10/8 on the X1 card (`workbook/KILL_MEMO_HY_OAS_260.md`, >280 row), forward-only, contamination note kept (root rule #10). HY leg MET at 9/29 and holding: 8 consecutive > 280.0 through 303 [10/6]. **A leg state only; X1 CLOSED, DON'T-SIZE** (the wrapper half fails) |
| Q3 persistence rule (FROZEN 9/25, verdict on the 10/8 prints) | Every leg read is NOT MET (SOFR−IORB −1 [10/5] / −2 [10/7]; SOFR99−IORB +6 [10/2]; SRF ≤ $0.002B). **ARMED on WRESBAL as-of 10/7 (~16:30 ET today): SEASONAL unless < $2,800.0B**, which needs a −$148.1B week; the largest fall in the last 5 weeks was −$83.6B |
| **10/7 ICE cell (~10:15 ET)** | **ARMED, not yet published at 08:35.** A cell moves a leg only on: HY ≤ 280.0 (X1 leg resets) · < 260 (REKILL starts) · IG > 94 or HY−IG < 180 (072) · BB > 220 with CCC flat (069 L1). Every one is ≥ 23bp away. A background poll is running. If a leg moves, LIQUID adds a dated receipt to this memo and messages `prome-fc` |

## 4. Whole-inbox drain: 29 packets → 0

The brief said 24; WALTER added 5 at 08:00–08:14 ET, and they were re-listed per your nudge. That is 27 in the WALTER lane plus 2 top-level. Each is logged in `board_log.tsv` (rows at 12:27Z) and moved with `git mv` (`0734364ed`). **6 acted, 23 noted:**
- `-002-022`: OCIC's fire is X1 wrapper EVIDENCE, not a re-arm.
- `-002-034`: CABO added to the distress-breadth read; notes ~25–28 are a RELAY; equity $13.21 [10/7].
- `-007-001`: no Paramount $12.4B is carried anywhere live.
- `-007-002`: the FOMC minutes' stable-funding / RMP evidence is kept separate from duration.
- `-008-008`: answered — the FT channel fits the breadth read. Stress is at CCC, CCC−B at the 99.9th pct (15-session), and it is not broadening up the ladder. No line moves.
- PROME's WQ-363 ruling: encoded.

**For BROCK, please relay:** BIZD's first close under $12.50 (10/1, $12.46) is its **$0.437 ex-dividend** (raw $12.89 [9/30]). After the ex-date it fell −3.5% to $12.03 [10/7], against APO −0.4% (yfinance, `auto_adjust=False`). A raw-close wrapper-vs-manager test across 10/1 carries the dividend; it needs total return.

## 5. Closeout and skipped controls

**Done:** STATUS write-back, MEMORY rotation, KB-LIQ-143, the read-cap rotation (75% → under the 70% stop; blocks rotated verbatim with crc32), `orphan_check` (nothing of mine), `claim_check` (one weekday flag, fixed), `corrections_boot_check` (rc 0), `boot.py --selftest` (PASS).

**SKIPPED or not run, with the reason:**
1. `git pull` at boot. The tree carried WALTER's uncommitted work; `git fetch` showed master even with origin.
2. `consumer_check`. No cited figure was superseded; WQ-363 encodes your ruling, already broadcast to BROCK.
3. `memory_index_check`. No auto-memory was written.
4. `sofr_dispersion.py` for the LIQ-07 z leg. Not due before the verdict.
5. The 10/7 ICE cell and WRESBAL 10/7. Not published yet; armed above.
6. MEMORY.md read by grep, not whole (85 KB).

**Commits:** `a3e8af6fa` · `9004d5450` · `dba78f384` · `0734364ed` · `dd96f0da0`, plus this memo's commit. Push through `0734364ed`: `Pushed. CONFIRMED: HEAD 0734364ed is on origin/master (fresh fetch).` The final receipt is in the message.

## COMPLETION — LIQUID — 2026-10-08
STATUS: ✅ DONE (10/7 ICE cell + WRESBAL 10/7 armed, not yet published)
CHANGED: AGENTS/LIQUID/{scripts/usd_swapline.py, analysis/2026-10-08_usd-swapline-LETTER.md (new), analysis/2026-10-08_usd-swapline-L568-change-note.md (new), analysis/2026-10-01_eurusd-basis-instrument.md, workbook/KILL_MEMO_HY_OAS_260.md, workbook/KB.tsv, STATUS.md, MEMORY.md, board_log.tsv, archive/status_snapshots/STATUS_ROTATION_2026-10-08.md (new), inbox → processed ×29}, this memo
RESULT: L568: X1–X5 + CATO D2 fixed in one pass, conditions committed first (a3e8af6fa → 9004d5450 → dba78f384). Selftest 48/48; 0 graded days changed 2014–2026; 266/266 real ALERT days no longer hidden by a one-source outage; CATO probe rc 4. IMPLEMENTED + TESTED, NOT verified, still WITHHELD. GATE-LIQ-076 NOT MET 1 of 3 [W1 as-of 9/29 −2,410,343 / +34,643; W2 as-of 9/23; W3 met]; no re-arm, so no 2nd write-up whatever Friday prints. WQ-363 encoded; inbox 29 → 0 (6 acted).
GAPS: 10/7 ICE cell (~10:15 ET) and WRESBAL 10/7 (~16:30 ET) not yet published — armed, no leg within 23bp. HANS has not answered the floor/turn-bound packet. The tenor-onset leg is in no script.
WILL_NEEDS: None now. After read 3, one WQ row: rule the swap-line letter (letter §6 carries the plain-words risks).
FOLLOW-UP: PROME: read 3 of usd_swapline.py (the last) · mirror 076 to GATES, set next review_by (10/30 rec) · relay the BIZD ex-dividend note to BROCK. LIQUID: Fri 10/9 W1 read · Q3 verdict on WRESBAL 10/7 · LIQ-07 verdict 10/15–16.
