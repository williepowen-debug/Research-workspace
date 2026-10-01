# PR#7 Reader R5 — Florida / housing / climate / insurance (CORAL · MARCO · HOMER · AEOLUS · SHADE)

**Reader:** R5 fan-out, read-only · **Period:** 2026-09-17 → 2026-10-01 · **Baseline:** `e9ac693af` (2026-09-16) · **Run:** 2026-10-01
**Instruments run:** `scripts/read_cap_check.py --agent <X>` ×5 · `scripts/ledger_staleness.py <X>` ×5 · `git log e9ac693af..HEAD` per tree · `git status --porcelain` on all five dirs (clean) · greps cited inline.
**Grade summary:**

| Agent | Row now | Proposed | Move | Firmness |
|---|---|---|---|---|
| CORAL | L3 H | **L4 M** | ↑ the only missing L4 leg (TRADE) was authored 9/28 | firm on L4 legs; Conf M = L5-hygiene residue |
| MARCO | L4 H | **L4 M** (held by exception) | Conf ↓: L1 leg still FAILS literally, and the L4 TRADE leg became FROZEN in the period | **confirm-read owed** (adjudication of the exception is DAEDALUS/Will's) |
| HOMER | L2 H | **L2 H** (L3 one leg away) | none — 3b built, 3c still open | firm |
| AEOLUS | L3 M | **L3 M** | none — Conf gate is DAEDALUS-lane, still unserviced | firm |
| SHADE | L3 H | **L3 H** | none — both L4 legs still absent, self-dated 10/08 | firm |

---

## CORAL — Market · row L3 H (scored 9/17)

**Period activity:** ~28 self-commits (9/28 catch-up + Will passes; 10/1 catch-up). Tree clean.

### A. Claims tested
| Claim (row) | Verdict | Locator |
|---|---|---|
| F-2 fixed 9/13, STATUS_DETAIL:49 stamps +178,674 with −56.5% arithmetic | **OVERTAKEN** — −56.5% was cross-vintage; CORAL now carries −37.0% same-vintage | `STATUS.md:53`; `STATUS_DETAIL.md:639`; `NEXUS_BRIEF.md:37`; MARCO `e10db55db` |
| STATUS back at 32,493 B = 100% | **OVERTAKEN** — rotated 9/28, regrown to **25,054 B = 77%** (rotate-tier; owes 2,270 B to the <22,785 stop) | read_cap_check CORAL |
| No TRADE surface exists (L4's one missing leg) | **REFUTED** — `TRADE.md` DECLARED FLAT 2026-09-28 in ZHAO's form, re-arm keyed to the registered bank rail | `TRADE.md:3,10-14`; `496403f3b` |
| Citizens early-Sep observable owed | **OVERTAKEN (delivered)** — 8/31 PIF 266,231 + 9/25 weekly 254,918 | `STATUS.md:40` |
| Criterion 5's Ch.7 per-capita instrument unbuilt | **REFUTED** — `tools/bkcy` built 9/28 (AOUSC F-2 + Census V2025); scoring Will-ruled WQ-321; level trigger retired WQ-322 | `496403f3b`, `8ce8ecb83`, `4661cb048`; `thesis/THESIS.md:129-132`; `STATUS.md:45` |
| Six-criterion falsify table is cohort exemplar | **TRUE** | `thesis/THESIS.md:102-118` |

### B. Ladder walk (L1 → L5)
| Leg | Verdict | Locator |
|---|---|---|
| L1 STATUS + BOTTOM LINE | PASS | `STATUS.md:128` |
| L2 structured record accruing | PASS | `workbook/KB.tsv` +0d; `FL_ENROLLMENT.tsv` new 9/28 (`d8c2a1bd3`) |
| L3 convergence matrix | PASS | `workbook/VX_Vectors.md`; STATUS dashboard |
| L3 exit rules | PASS | `thesis/THESIS.md:63-132` confirm/falsify; `TRADE.md:10-14` |
| L3 predictions resolving | PASS (local form: pre-registered branch reads graded in place) | `workbook/FL_Forward_Log.md:17`; THESIS grade table `:111-118` |
| L3 dated falsification surface | PASS | `thesis/THESIS.md:4` next grade 2026-11-15 |
| L4 TRADE.md feeding proposals | **PASS (declared-flat form)** | `TRADE.md` `496403f3b` |
| L4 signals flowing | PASS | `c46791137` (→CREED), `12c4d01ad` (→PROME), `3010fea3e` (→WALTER) |
| L5 clean closeouts, current | **FAIL** — (i) STATUS 77% rotate-tier, stop unreached; (ii) `workbook/FL_Forward_Log.md` last commit `13768ce9e` 2026-07-23, no FROZEN banner, while charter `CLAUDE.md:156,238` still names it the catalyst home and `CALENDAR.md` (refreshed 10/1) is the live one — two-state rule's silent-rot middle; (iii) `thesis/THESIS.md:4` "Rails last reviewed 2026-08-23" though rails changed 9/28 (`8ce8ecb83`, `4661cb048`) | read_cap; `git log -- workbook/FL_Forward_Log.md`; THESIS:4 |

### C. Reachability
All L5 legs are CORAL-tree and condition-free. The 11/15 falsify grade needs two consecutive AOUSC tables for criterion-5 leg A — AOUSC 9/30 table ~late Oct (expected event; grade can report "1 of 2 tables" if late — no blocker). Citizens 9/30 month-end "~early Oct" is expected-event with no fallback, harmless (observation, not a gate).

### D. Profile trigger
**NOT FIRED** (30-day clock → checkpoint 2026-10-05, `profiles/CORAL.md:5`; fires in 4 days). Content materially moved (TRADE built, bkcy built, criterion 5 re-letter, 9 association Ch.11s) — refresh at 10/05 will have work.

### E. Proposed row
- **Level L4 · Conf M** — reason: both L4 legs PASS at artifact; Conf M because L5 hygiene (rotation, frozen-or-live Forward Log, header) is open, not because any L4 leg is doubtful.
- **Gaps:** STATUS.md 25,054 B = 77% (rotate-tier; 2,270 B short of the <22,785 B stop). `workbook/FL_Forward_Log.md` unmaintained since 2026-07-23 with no FROZEN banner while the charter (CLAUDE.md:156,238) still names it the catalyst surface; CALENDAR.md is the live one. THESIS.md:4 rails-reviewed stamp reads 8/23 over 9/28 rail changes. Citizens Aug mechanism and condo months-supply vintage still unreconciled with MARCO (STATUS.md:124).
- **Next_upgrade:** L5 at the next CORAL session: rotate STATUS under 22,785 B, FROZEN-banner FL_Forward_Log.md and re-point CLAUDE.md:156/238 to CALENDAR.md, bump THESIS.md:4.

### F. Cross-agent threads
| Thread | Owner |
|---|---|
| Citizens Aug mechanism: CORAL "takeout-driven, ex-round ≈ −93" vs MARCO "depopulation RESUMED" — same level, opposite reading; CORAL packet 9/28 sits unread in MARCO inbox | **MARCO** (consume), CORAL owns the series |
| Condo/SF months supply 7.7/4.3 (Aug, CORAL) vs 7.8/4.5 (Jul, MARCO `STATUS.md:15`) | **MARCO** |
| FL reinsurance renewal: CORAL "6/1 −15-20% risk-adjusted (Guy Carpenter, confirmed 7/21)" vs AEOLUS "ROL DOWN 15-30% YoY at Jun-1" [6/28] | **AEOLUS** (refresh to CORAL's sourced figure or state basis) |
| HOMER→CORAL statewide condo price reconciled to CORAL's Aug +2.8% (`f3767d396`) | closed |

---

## MARCO — Market · row L4 H (scored 9/17)

**Period activity:** heavy 9/19 + 9/24 (s28–s30d, ~40 commits); **no MARCO commit since 2026-09-24**. Inbox: 6 top-level packets unread incl. PROME WQ-295 cadence (9/25) and CORAL Citizens (9/28).

### A. Claims tested
| Claim | Verdict | Locator |
|---|---|---|
| `grep -ci 'bottom line' STATUS.md` = 0 | **TRUE (literal re-run = 0)** — STATUS has "This session in one line" (`:3`), no BOTTOM LINE heading anywhere (headings `:4-111`) | grep run 10/1 |
| Handle (2) unmet — 0 hits for 5-pt / Independence | **TRUE** — 0 hits in STATUS, VX, CLAUDE | grep run 10/1 |
| Substance among fleet's strongest (57-vector VX; 16-row PREDICTIONS) | **TRUE** — VX header 57 live; PREDICTIONS 16 rows; s30d band audit 36 rows / 3 blind readers (`986cae52f`) | `workbook/VX.tsv:1`; `thesis/PREDICTIONS.tsv` |
| MEMORY.md 49,058 B = 151% | **OVERTAKEN** — 24,061 B = 74% (rotated s28 `3b365a0ac`); 351 B to trigger | read_cap MARCO |
| STATUS.md 33,789 B = 104% | **OVERTAKEN** — 22,670 B = 70% (under stop) | read_cap MARCO |
| Citizens STATUS-vs-VX vintage split CANNOT-EVALUATE | **REFUTED (closed)** — both at 266,231 8/31 | `STATUS.md:78`; `VX.tsv` SFE-03 |

### B. Ladder walk
| Leg | Verdict | Locator |
|---|---|---|
| **L1 BOTTOM LINE (labelled heading)** | **FAIL — literal.** No heading, 0 grep hits; an L4 desk failing a floor leg | `STATUS.md` (22,670 B, whole) |
| L2 structured record | PASS with defect: `VX.tsv:3` two-clock header still "Last real data refresh: 2026-08-21" though rows were refreshed 9/24 → ledger_staleness reports **STALE +35d** (owner-caused false alarm); `FIGURES.md:77` still carries "−56.5% YoY" two rows above its own correction at `:155` | ledger_staleness MARCO; `FIGURES.md:77,155` |
| L3 convergence matrix | PASS | `VX.tsv` 57 vectors |
| L3 exit rules / falsification | PASS | thesis v3.2; ENR-02 re-spec grades 10/14 (`4eb69663b`); ID-01 both-months pre-committed (`9f2c06408`) |
| L3 predictions resolving | PASS | `thesis/PREDICTIONS.tsv` MAR-10/15 CONFIRMED |
| L4 TRADE.md feeding proposals | **WEAKENED → FAIL on letter** — TRADE.md FROZEN 9/24 ("not maintained … a new idea goes to TERRY as a packet"); that is a FROZEN ledger, not a declared-flat surface with a re-arm condition (the form CORAL was held at L3 for until 9/28) | `TRADE.md:3`; `1fe88f48e` |
| L4 signals flowing | PASS | `e10db55db`, `b1f8502fc` (→CORAL), `f9c071b4a` (→CARL) |
| L5 clean closeouts | FAIL (L1 leg; VX header; no WQ-295 cadence declared — only cohort desk without one) | PROME/inbox/processed listing |

### C. Reachability
Both fixes are MARCO-tree, one-line, condition-free: add a `## BOTTOM LINE` heading; convert TRADE.md's FROZEN banner to DECLARED FLAT + the condition that would re-arm (as CORAL `TRADE.md:10-14`). Trigger is "next MARCO session" — MARCO has no declared cadence, so no date can be keyed; key to the WQ-295 packet already in its inbox.

### D. Profile trigger
**NOT FIRED** (>45d → checkpoint 2026-10-20, `profiles/MARCO.md:5`; body partly edited 10/1 `c8daef7e6`).

### E. Proposed row
- **Level L4 (held by exception) · Conf M** — reason: L1 heading leg has now failed through three self-authored sessions after routing; the L4 TRADE leg went FROZEN in-period, so the exception now covers two legs. **Confirm-read owed** — whether to hold L4 or floor the grade is the adjudicator's call, not this reader's.
- **Gaps:** STATUS.md has no BOTTOM LINE heading (L1 leg). TRADE.md is FROZEN, not declared-flat (L4 leg on letter). No 5-pt / Independence handle. VX.tsv:3 two-clock header reads 8/21 over 9/24 refreshes (ledger_staleness false STALE +35d). FIGURES.md:77 still states −56.5% beside its own −37.0% correction at :155. No WQ-295 cadence declared; 6 inbox packets unread since 9/17–9/28.
- **Next_upgrade:** at the next MARCO session (packet already in inbox): add the BOTTOM LINE heading and re-banner TRADE.md DECLARED FLAT with a re-arm condition; bump VX.tsv:3; declare cadence.

### F. Cross-agent threads
| Thread | Owner |
|---|---|
| Citizens Aug mechanism split with CORAL (see CORAL F) | **MARCO** |
| Months-supply vintage update from CORAL (Aug 7.7/4.3) | **MARCO** |
| WQ-295 cadence/watch-terms packet unanswered | **MARCO** → PROME |
| AEOLUS C5 consumption leg: MARCO KB carries AEOLUS C2 and C6 (Mead) rows (`KB-MARCO-PRD-38`, `SW-38`), **no C5 freight row** | verify — AEOLUS consumption leg NOT MET at MARCO |

---

## HOMER — Market · row L2 H (scored 9/24)

**Period activity:** 9/24 catch-up + 9/29 (AM/PM, ~25 commits). Tree clean.

### A. Claims tested
| Claim | Verdict | Locator |
|---|---|---|
| Both L3 legs UNBUILT; no THESIS.md / no thesis-level kill rail | **REFUTED for the kill rail** — `thesis/THESIS.md` built 9/29, criteria FROZEN, 0 of 5 legs FIRED, formal grade 2026-11-20, PROME-registered `GATE-HOMER-THESIS-KILL` | `74089ab84`, `741467fa9`; `thesis/THESIS.md:3,97-106` |
| No convergence handle | **TRUE** — "Not built here: the convergence handle (L3 build 3c). Still OPEN" | `thesis/THESIS.md:6`; `STATUS.md:107` |
| NEXUS_BRIEF:45 presents CREED Trepp courier as in force | **OVERTAKEN (fixed)** — brief now "the CREED courier is DEAD since 8/13" | `NEXUS_BRIEF.md:36`; `72e63a82a` |
| NEXUS_BRIEF.md 109,239 B = 3.4× | **OVERTAKEN** — 13,908 B (rotated 9/24) | `72e63a82a`; `NEXUS_BRIEF.md:7` |
| LESSONS.md 73% in 70–75 band, owner-only | **TRUE** — 23,551 B = 72%, 861 B to trigger | read_cap HOMER |
| Per-prediction rail good, 1 OPEN row | **TRUE** — HOM-01 RESOLVED MISSED 8/31; HOM-02 OPEN to 2027-02-28 | `thesis/PREDICTIONS.tsv` |

### B. Ladder walk — carry-in: does `d4f8fe3cd` clear an L3 leg?
**Yes, one: the dated-falsification leg (and the thesis-level half of exit rules). It does not clear L3** — the convergence leg is the sole remaining blocker.

| Leg | Verdict | Locator |
|---|---|---|
| L1 | PASS | `STATUS.md:154` |
| L2 | PASS — 9 ledgers ok/FROZEN by banner | ledger_staleness HOMER |
| L3 convergence matrix | **FAIL** — 3c open; CARL confirmed (a) 10/1, (b) provisional to CARL's 10/05 sitting, (c) candidate | `thesis/THESIS.md:6`; `inbox/2026-10-01_from-CARL_3c-handle-confirmed-V3-rescope-at-10-05.md` (`d9d9eeede`) |
| L3 exit rules | PASS — per-prediction invalidation + thesis rail verdict table | `thesis/THESIS.md:76-85` |
| L3 predictions resolving | PASS | HOM-01 resolved 8/31 (`56f4f2638`) |
| L3 dated falsification surface | **PASS (new)** | `thesis/THESIS.md:3,89` |
| L4 | not tested (L3 unmet) | — |

### C. Reachability
3c is HOMER-tree (CARL: "Build 3c into your THESIS as proposed", label CONFIRMED/PROVISIONAL/CANDIDATE). Not blocked by CARL's 10/05 sitting — (b) is a label, not a precondition. HOMER self-dated build **by 10/09** (`STATUS.md:107,164`). Reachable. The row's "then the blueprint conformance grade" is DAEDALUS-lane, not desk-clearable.

### D. Profile trigger
**FIRED** — own trigger "re-read when THESIS.md gets built" (`profiles/HOMER.md:22`) fired 9/29 (`74089ab84`); profile already bannered STALE since PR#5 (`:3`), last commit `31e0b90d7` 9/01. Refresh owed (DAEDALUS lane).

### E. Proposed row
- **Level L2 · Conf H** — no move; L3 is one leg away.
- **Gaps:** L3 convergence leg unbuilt (thesis/THESIS.md:6): the 3c handle over C1/C2/A1–A3 is not written, though CARL confirmed the V10↔C1+A1 root on 10/1 and asked HOMER to build it. Thesis kill rail is built, frozen and PROME-registered (0 of 5 legs fired; formal grade 2026-11-20). LESSONS.md 72% in the owner-only 70–75 band.
- **Next_upgrade:** L3 on building 3c into thesis/THESIS.md with CARL's three labels — HOMER self-dated 2026-10-09; not gated on CARL's 10/05 sitting.

### F. Cross-agent threads
| Thread | Owner |
|---|---|
| V3 re-scope (GSE MF both books) — CARL 10/05 THESIS-SCOPE REVIEW | **CARL** |
| CARL matrix stale citations (V3 May 0.58%, V10/V7 REO) refresh at 10/05 | **CARL** |
| CREED/FLG/WALTER MF packets 9/29–10/1 (75 West, Arbor, NYC rent freeze) unconsumed | **HOMER** |
| HOMER profile refresh (trigger fired) | **DAEDALUS** |

---

## AEOLUS — Market · row L3 M (scored 9/17)

**Period activity:** 9/18 (crash, recovered), 9/28 session (~12 commits). Tree clean. Inbox: 1 WALTER + 1 R3 packet (10/1).

### A. Claims tested
| Claim | Verdict | Locator |
|---|---|---|
| STATUS 32,504 B = 99.86%, rule-5 STOP unreached | **OVERTAKEN** — 19,572 B = 60% | read_cap AEOLUS |
| Falsification rail MET (RAIL-IN-LOCAL-FORM) | **TRUE** — exit triad table; C1 channel-kill IN PROGRESS to 11/30 | `STATUS.md:82` |
| THESIS.md last touched 8/27 | **TRUE** — now 35d; channel state moved since (C5 → 5 fires 9/28, C1 DORMANT, C4 3→2) | `git log -- THESIS.md` → `ef8d95669`; `STATUS.md:16,19` |
| AEO-03 names no publisher | **TRUE for the resolving instrument** — row still "Jan'27 property-cat ROL ≤ +5% YoY", no publisher. A distinct SEARCH instrument (Artemis cat-bond yield, KB-AEO-121) was named and attempted 9/28; AEOLUS itself states it "is NOT rate-on-line" | `workbook/PREDICTIONS.tsv` AEO-03; `088bec590`; DAEDALUS `inbox/processed/2026-09-28_from-AEOLUS_AEO-03-search-instrument-PR6.md` |
| Conf M gate = owed Mode-A profile fan-out | **TRUE — unserviced** (profile last commit 9/01) | `git log -- profiles/AEOLUS.md` |
| Consumption legs MARCO C5 / WATT C3 NOT-ADJUDICATED | **Adjudicated: both NOT MET.** WATT: AEOLUS C3 answer sits unconsumed in `WATT/inbox/2026-09-28_from-AEOLUS_C3-heat-signature…md`; WATT `STATUS.md:95` still "no answer yet"; no WATT session since 9/25. MARCO: no C5 row (see MARCO F) | greps above |

### B. Ladder walk
| Leg | Verdict | Locator |
|---|---|---|
| L1 | PASS | `STATUS.md:136` |
| L2 | PASS — 12 ledgers ok | ledger_staleness AEOLUS |
| L3 (matrix / exit / predictions / falsification) | PASS ×4 | `workbook/VX.tsv`; `STATUS.md:82`; PREDICTIONS 4 HIT (AEO-04/05/06/11) |
| L4 TRADE.md feeding proposals | **FAIL (soft)** — TRADE.md LIVE with per-row dates, but rows 1 and 3 last updated 2026-07-09 (84d); row 1 rationale still cites a CSU forecast long superseded; THESIS channel tables 35d stale | `TRADE.md` rows 1–4 |
| L4 signals flowing | PASS | `310c0df2c`, `3e6951adb`, `1f0334263` |

### C. Reachability
- AEO-03 publisher: AEOLUS-tree; CORAL already cites **Guy Carpenter** for the 6/1 FL renewal (`CORAL/STATUS_DETAIL.md:33`) — a known publisher exists; window closes 2027-01-01. Reachable.
- THESIS refresh: AEOLUS-tree, reachable at the WEEKLY cadence (declared 9/28; next session ~10/05).
- **Conf M→H gate is NOT desk-clearable** — it is DAEDALUS's Mode-A fan-out. Flag: a confidence gate keyed to the grader's own backlog.
- Consumption legs are in other desks' trees (WATT dark since 9/25; MARCO dark since 9/24) — never desk-clearable; should not gate AEOLUS's level.

### D. Profile trigger
**FIRED** (standing) — leg (T) KB rows off 82 by ≥15: KB.tsv now 163 data lines. Leg (P) NOT fired (AEO-12 OPEN; open-count 8). Leg (S) NOT fired (5 workspaces). Banner at `profiles/AEOLUS.md:3` already says fired/unserviced.

### E. Proposed row
- **Level L3 · Conf M** — no move.
- **Gaps:** AEO-03 resolving instrument names no ROL publisher (the 9/28 Artemis cat-bond series is a search instrument, self-labelled not-ROL). THESIS.md 35d behind STATUS (C5 5 fires, C1 dormant, C4 2). TRADE.md rows 1 and 3 dated 2026-07-09. Mode-A profile fan-out unserviced (DAEDALUS). Consumption: WATT has not read the 9/28 C3 answer; MARCO carries no C5 row.
- **Next_upgrade:** L4 on: name the AEO-03 ROL publisher (Guy Carpenter, already CORAL-cited) and refresh THESIS.md + TRADE rows 1/3 to current channel state — next WEEKLY session, before 2027-01-01. Conf M→H stays on DAEDALUS's fan-out.

### F. Cross-agent threads
| Thread | Owner |
|---|---|
| FL reinsurance renewal: AEOLUS "−15-30%" [6/28] vs CORAL "−15-20% risk-adj (Guy Carpenter)" | **AEOLUS** |
| Hurricane season: AEOLUS 0 hurricanes, ACE 10.61% of normal; CORAL "8 named / 0 hurricanes" — consistent | none |
| C3 heat answer unconsumed | **WATT** |
| Mode-A profile fan-out | **DAEDALUS** |

---

## SHADE — Market · row L3 H (scored 9/17)

**Period activity:** dark 8/28 → 10/01 (34 days); 10/1 PROME-spawned session (`prome-0c`) with ~10 commits and full closeout. Tree clean.

### A. Claims tested
| Claim | Verdict | Locator |
|---|---|---|
| PREDICTIONS.tsv ABSENT, self-flagged | **TRUE** — no `*PREDICT*` in tree; self-flagged OVERDUE since 9/30, target **by 2026-10-08** | `find AGENTS/SHADE`; `STATUS.md:124` |
| No TRADE surface | **TRUE** — none in tree; same self-dated item | `STATUS.md:124` |
| 20 dark days, 0 self-commits since 8/28, 11 routed-in WALTER items | **OVERTAKEN** — 10/1 session (`20261f699`…`ffd823d80`); 25-item drain; `inbox/WALTER/*.md` = 1 | git log; ls |
| T-SHADE-01 readings 20d stale; 276 vs >280 | **OVERTAKEN** — re-read 10/1: level 4 of 5 above 280 (312 [9/30]); sign leg NOT MET 5-for-5 (managers −16.99% vs wrappers −7.80%) ⇒ NOT ARMED | `STATUS.md:33` |
| Grade kill-path #4 against REGINALD Brent $104.61 [9/11] | **TRUE (not done)** — no Brent/oil grade in STATUS; ⚠️ STATUS vector table `#4` = NAIC/AG55/SVO (`:79`) while charter kill path #4 = war/macro oil (`CLAUDE.md:48-52`) — two different "#4"s | grep |
| Rotation stop not reached | **PARTLY OVERTAKEN** — STATUS 20,906 B = 64% (done); **MEMORY.md 31,745 B = 98%** (owes 8,961 B; self-dated 10/08) | read_cap SHADE; `STATUS.md:125` |
| Rail well built (4 kill paths; T-SHADE-01 value_basis + sign leg) | **TRUE** | `CLAUDE.md:48`; `STATUS.md:33` |

### B. Ladder walk
| Leg | Verdict | Locator |
|---|---|---|
| L1 | PASS | `STATUS.md:138` |
| L2 | PASS (local form — `registry/corrections_receipts.tsv`, research corpus; no `workbook/`, ledger_staleness finds none) | `registry/` |
| L3 ×4 | PASS (as graded 9/17; T-SHADE-01 graded 10/1, pre-registered ARI match rule `0b2eeb897` graded UNDETERMINED by its own letter) | `STATUS.md:33`; `3b59319de` |
| L4 TRADE.md feeding proposals | **FAIL** — absent | — |
| L4 signals flowing | PASS | `deb771f19` (→CREED), `978f92e4e`, `665964489` (→PROME) |
| (L4 seed-PREDICTIONS leg as written in the row) | **FAIL** — absent | — |

### C. Reachability
Both legs SHADE-tree, self-dated 2026-10-08 under a declared WEEKLY cadence — reachable **if** a session occurs; SHADE's last two sessions were PROME-spawned after 16 and 34 dark days, so the date is only as good as PROME's spawn. **Flag:** kill-path #4 "against REGINALD's Brent $104.61 [9/11]" is keyed to another desk's carried figure, now 20 days old — re-key to a live read at grade time (root rule #4). Also: charter thresholds table HY OAS Yellow = 300–350 (`CLAUDE.md` Thresholds) — HY 312 [9/30] sits in it and STATUS does not grade the band (only T-SHADE-01's 280 leg); CANNOT tell if that table is live or legacy — owner should say.

### D. Profile trigger
**FIRED** — leg (b) `STATUS.md:3` Last Updated advanced to 2026-10-01; leg (c) `inbox/WALTER/*.md` = 1 ≠ 14. Leg (a) NOT fired (no PREDICTIONS). `profiles/SHADE.md:8`.

### E. Proposed row
- **Level L3 · Conf H** — no move.
- **Gaps:** No PREDICTIONS.tsv and no TRADE surface (both L4 legs; self-dated OVERDUE, target 2026-10-08, STATUS.md:124). MEMORY.md 31,745 B = 98% (8,961 B to the stop). Charter kill path #4 (war/macro oil) is ungraded, and STATUS's own "#4" names a different vector. HY OAS 312 [9/30] sits inside the charter's 300–350 Yellow band with no stated grade. Sessions occur only on PROME spawn (34 days dark before 10/1).
- **Next_upgrade:** L4 on seeding workbook/PREDICTIONS.tsv (confidences at registration) + a declared-flat TRADE.md in ZHAO's form — SHADE's own date 2026-10-08, same session rotating MEMORY under 22,785 B.

### F. Cross-agent threads
| Thread | Owner |
|---|---|
| X1 ≡ T-SHADE-01 reconcile (FORUM-5 ruling 2) | **LIQUID / PROME** |
| ARI loans at AAIA ($7.405B 4/24) bear on CREED's sector read | **CREED** (packet `deb771f19`) |
| "Illiquid ABS" leg definition for charter ratio #2 — threshold-adjacent, Will's ruling | **PROME/Will** (proposal by 10/08) |
| WALTER lane-query sizing adopt/decline (`116229ebd`) | **SHADE** |
| SHADE spawn before 10/08 so the self-date can be met | **PROME** |

---

## Cohort-level findings (for the review synthesizer)

1. **Two scoped-overlap metrics are stated differently today** — Citizens Aug mechanism (CORAL takeout-driven vs MARCO depopulation-resumed) and FL reinsurance renewal (CORAL −15-20% risk-adj, Guy Carpenter vs AEOLUS −15-30% [6/28]). The first is blocked only on MARCO being dark; the second is AEOLUS's stale row. The migration figure (−37.0% same-vintage) is now one figure at both desks' live surfaces, but MARCO `FIGURES.md:77` still carries −56.5%.
2. **TRADE-surface form inconsistency:** CORAL earned L4 by declaring flat (9/28); MARCO's TRADE went FROZEN the same week and is still graded L4. Same leg, two outcomes — the adjudicator should apply one rule.
3. **Header-not-bumped instances ×2** (MARCO VX.tsv:3, CORAL THESIS.md:4) — both mean a freshness signal reads older than the content behind it (the reverse of the usual direction); MARCO's trips a false STALE in ledger_staleness.
4. **Three DAEDALUS-lane profile refreshes owed** (HOMER fired, AEOLUS fired, SHADE fired); CORAL's fires 10/05.
5. **Confidence/level gates not desk-clearable:** AEOLUS Conf (DAEDALUS fan-out), AEOLUS consumption legs (WATT/MARCO, both dark), HOMER "blueprint conformance grade" (DAEDALUS).
