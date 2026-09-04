# `PREDICTIONS_MONITOR.md` HOT/COLD SPLIT — OBLIGATION LEDGER (before → after)

**Author:** NEXUS · **Date:** 2026-09-03 · **Ruling executed:** WQ-163 item 1 (Will 2026-09-02 22:24 ET *"Approve 163 item 1 as adjudicated"*; DAEDALUS adjudication `213ef8963`; `READ_CAP.md` rules 16 + 17, OFF-PATH branch).
**Source vintage:** `AGENTS/NEXUS/PREDICTIONS_MONITOR.md` at `c2dbc635a` — **59,146 B, crc32 3831447128** (`PROME/tools/measure.py`).
**Result:** hot `PREDICTIONS_MONITOR.md` **21,624 B** (66% of the 32,550 B budget) · cold `PREDICTIONS_COLD.md` **48,029 B**, 12 verbatim blocks, crc32 per block · this ledger (on demand).
**Method:** the split was cut by LINE RANGE from the source by script (`/tmp/nexus_split.py`, run once; every source line asserted as cold / hot-verbatim / structural, zero unaccounted, zero double-homed except the ACTIVE table header reproduced in both halves by design). **Then this ledger was built by reading the pre-split file end to end and listing every owed action, watch, guard and dated resolver** — the byte census and the obligation census are different questions (9/02: the first STATUS split passed both byte checks while it had deleted two obligations).

> **Rule this ledger applies (READ_CAP rule 17, off-path branch):** moving a container off the boot path makes every live obligation inside it MORE invisible; so each one is named, its state re-checked at the artifact today, and given exactly ONE home. **Discharged ≠ deleted:** a discharged obligation goes cold WITH the evidence of its discharge named here.

## A. Obligations found in the pre-split file (29) — state re-checked 9/03, new home

| # | Pre-split obligation (where it lived) | State re-checked 9/03 | Home after split |
|---|---|---|---|
| O1 | 🔒 T-12 non-renewable clause ARMED, C#1 of 2; second C ~9/11 forces re-spec; base-rate successor for reachability *(header line 3)* | LIVE | **HOT header L1** + STATUS T-12 |
| O1a | *(implicit — never written)* the window START for the C#2 evaluation | 🔴 **UNPINNED** — SEARCH-NOT-FOUND in `research/2026-08-28_successor_falsifier_RESOLUTION.md` (grep: "second", "9/11", "window"); only the evaluation DATE was named | **HOT header L1a — PINNED 9/03 (8/28→9/10 FRED cells), flagged to PROME for objection** |
| O2 | Dated resolvers: PRED-48 10/1 · PRED-24 9/30 · PRED-37 Sep-end · PRED-41 Q4/Q1 · PRED-45 @35% *(header)* | LIVE | HOT header L7 + ACTIVE rows |
| O3 | PRED-30 next arbiter July TIC ~9/16 *(header + row)* | LIVE | HOT L7 + PRED-30 row |
| O4 | ORACLE T-16 instrument mislabel — "corrected in place below" *(header)* | DISCHARGED 8/28 (the corrected T-16 text is in the 7/28-31 block) | COLD §P1 (note) + §G4 (corrected text) |
| O5 | "SCOPED pass — 8/18→8/27 owner outputs unconsumed; QCEW/Warsh no packet" *(header)* | DISCHARGED 9/02 — STATUS docket row "8/18→9/02 SWEPT AND CLOSED, 13 owner-graded outcomes consumed" | COLD §P1 |
| O6 | MIDAS-07 (d) INDETERMINATE; WILL_QUEUE row 51 MIDAS-06 phantom print to be ruled before 8/28 *(header)* | DISCHARGED — MIDAS-06 TERMINAL 8/31, YES verified in Kernel 9/2 (STATUS BREACHED table) | COLD §P1 |
| O7 | CARL kill-rule re-spec to Will (A)/(B)/(C), needed ~9/30; count stays 1-of-2 *(header ×2 + 7/28-31 note)* | LIVE | **HOT header L2** + STATUS chain link |
| O8 | PortWatch `chokepoint6` impeached; C-35 grading line carries caveat until ~8/20 control *(header)* | SUPERSEDED 9/02 — control FAILED ×2, POSITIVE-DETECTOR-ONLY; wait BRENT re-spec 9/5-9/8 | **HOT header L3** (updated form) + STATUS T-20 / CONFIRMED pointer |
| O9 | RED-FT-12 = branch B verbatim; Disc-H count once *(header)* | LIVE standing guard | **HOT header L4** + STATUS PROXIMATE row |
| O10 | FT-01 demoted by owner mid-window (coverage defect) *(header)* | LIVE standing guard (restored HOT in STATUS 9/02) | HOT header L4 + STATUS BREACHED row |
| O11 | "M-10 not moved — re-reading owed to the ≥8/29 sweep" *(header)* | DISCHARGED 9/02 — M-10 ↓2 → 30 | COLD §P1 |
| O12 | Cross-agent adjudications logged 8/17-8/28 (BRENT COT-FUEL retired · SAM B0 + KILL-SPEC-3 · GATE-FALCON-001 leg-3 FIRED 8/15 · SHADE M-11 both legs FINAL · OTTO-30 FALSIFIED) *(header)* | all RESOLVED records; none carries a forward ask of NEXUS | COLD §P1 |
| O13 | BOND figure corrections (30Y run-length · 5.27 cycle high · DFII10 post-2023 high) consumed *(header)* | DONE; the corrected figures live in STATUS BREACHED rows | COLD §P1 |
| O14 | ZHAO 8/21 PRED-30 conditional MET → row re-graded *(header + row)* | DONE 8/28; row LIVE | HOT PRED-30 row |
| O15 | Pass-log rule "current + ONE prior inline, archive the rest at each prune" *(header)* | **AMENDED 9/03** — hot header carries live obligations only; pass narratives → COLD §P at write time | HOT header (rule stated) |
| O16 | Orphan `PROME/PREDICTIONS_MONITOR.md` routed to PROME to trash *(line 4)* | DISCHARGED — **VERIFIED absent 9/03** (`ls`: No such file) | COLD §P2 |
| O17 | PRED-48 resolve 10/1; LABOR may sharpen the bar *(row)* | LIVE | HOT row |
| O18 | PRED-49 — graded MISSED 9/02; consequence (amendment 12 + §4.6 CAP) discharged *(row)* | CLOSED | COLD §C2 |
| O19 | PRED-24 dated re-review 9/30 *(row)* | LIVE | HOT row |
| O20 | PRED-37 resolve Sep-end *(row)* | LIVE | HOT row |
| O21 | PRED-38 Q3 leg + BDC-adjacent window open *(row)* | LIVE | HOT row |
| O22 | PRED-40 resolve or re-scope Q3-end *(row)* | LIVE | HOT row |
| O23 | PRED-41 window Q4-26/Q1-27; next instruments HHDC + holiday credit *(row)* | LIVE | HOT row |
| O24 | PRED-43 "resolve FALSIFIED-in-mechanism if Kharg fires via seizure" *(row)* | LIVE, but the in-cell premise is 7/22-vintage and stale after the 9/02 Kharg finding | HOT row + **HOT header L6 (`[STALE 7/22]`, re-mark owed)** |
| O25 | 🔴 PRED-45 re-mark on First Brands Ch.7 venue change — "queued for the ≥8/29 sweep" *(row)* | **NOT DONE 9/02** — the full matrix review missed a queued prediction row (defect recorded) | HOT row + **HOT header L5 (owed ≤9/11)** |
| O26 | 7/21-22 block: sinking watch closes 7/26 · ≥2-of-4 decided at MSFT/META 7/29 · PortWatch post-strike prints ~7/29-8/1 resolve FALCON leg-2 | all CLOSED (7/25-27 + 7/28-31 blocks); FALCON's leg-2 is FALCON's gate, carried on this board only through T-20/M-06 | COLD §G1 |
| O27 | 7/25-27 block: **2Y+5Y auctions "BOND grade OWED", 7Y tiebreaker** · **KFRC Q2 "LABOR grade OWED"** · 8/5 SOQ grader (KB-VIO-127) | BND-13 CONFIRMED 7/28 (§G4) · **KFRC graded by LABOR 7/31 — VERIFIED at `AGENTS/LABOR/NEXUS_BRIEF.md:133`** · KB-VIO-127 resolved MISS 7/31 (§G4) | COLD §G3 |
| O28 | 7/28-31 block: FAL-04 window 7/30-8/20 · BND-01 FAILED 7/31 · T-16 FedWatch leg UNRESOLVABLE · HEN-36 guard | all CLOSED (FAL-04 crude legs = NOT CONFIRMING on STATUS; FAL-01 FIRM-NEGATIVE 9/02) | COLD §G4 |
| O29 | FALSIFIED/SUPERSEDED log + E-phase closed section + CONFIRMED Mar-Apr + PAST-TRIGGER archive | records only; zero forward asks (each row re-read) | COLD §F / §E / §C1 / §C3 |

**Tally:** 29 items · **LIVE and re-homed HOT: 15** (O1, O1a, O2, O3, O7, O8, O9, O10, O14, O15, O17, O19–O25) · **DISCHARGED with evidence named, gone COLD: 14** (O4, O5, O6, O11, O12, O13, O16, O18, O26, O27, O28, O29 + the two discharge sub-items in O27). **Deleted: 0.** **Newly surfaced by the audit: 2** (O1a unpinned window; O25 missed re-mark).

## B. What the cure did NOT do
- No prediction row was re-graded or re-marked (PRED-45/43 re-marks are OWED, dated, not done — a dark-owner drain at the tail of a session is the wrong place for a 35% re-mark on a venue that changed character).
- No threshold, letter or instrument was moved. **L1a pins a window START that was never written**, on the interested party's authority, before the event, and is flagged to PROME for objection — it is a pin, not a re-spec.
- The 7/10 + 7/16 gate blocks stay at `signals_archive/GATE_ADJUDICATIONS_20260710_20260716.md`; pass blocks ≤8/12 stay at `signals_archive/PREDICTIONS_PASS_LOG_20260627_20260724.md`. Nothing was consolidated across archives.

## C. Rule 17 measurement (same commit)
| Surface | Before | After | Δ |
|---|---:|---:|---:|
| `PREDICTIONS_MONITOR.md` (boot read) | 59,146 | **21,624** | **−37,522** |
| `PREDICTIONS_COLD.md` (off path) | — | 48,029 | +48,029 (not on the reading path) |
| NEXUS whole-read boot total (`read_cap_check` perimeter, after the charter reword makes step 3 a counted read) | 77,956 + 59,146 uncounted | see `read_cap_check` receipt in `LAST_COMPLETION.md` | — |

*The destination is OFF the reading path (rule 17 off-path branch) ⇒ the obligation enumeration above is the cost paid, and it is the cost this ledger measures.*
