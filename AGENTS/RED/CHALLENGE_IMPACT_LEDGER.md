# RED — Challenge Impact Ledger (harmful-revision measurement)

**Built:** 2026-07-31 (S27b) on PROME's 7/25 task (`inbox/processed/2026-07-25_from-PROME_harmful-revision-ledger-task.md`, from `AUDITS/2026-07-22_system_analysis_v2.md` §12 Priority 6). **Question measured:** of the revisions RED's challenges forced on target theses, did any make the thesis materially *worse* against subsequent evidence known today?

**Population:** all 43 rows of `workbook/CHALLENGES.tsv` (CHG-RED-001…043) + the SAM V1.6 dialogue (rows 029-032, 039). Source of truth for pre/post states: the frozen `Key_Finding` / `Resolution` fields of each TSV row, the `challenges/` files, and target-agent commits cited therein. Read-only against owners' files; no thesis or threshold moves anywhere in this work.

---

## RUBRIC (pre-registered 2026-07-31, committed BEFORE any row was graded — grading follows in a separate commit)

**Unit of grading = the ACCEPTED REVISION**, not the challenge's quality. A revision is "accepted" only if the record shows the target changed its thesis/spec/estimate because of the challenge (target's own response file, commit, or version ship citing the challenge). A clever challenge that produced no accepted revision cannot be IMPROVED or HARMED — it goes to NO-REVISION and its rebuff is sub-graded.

**Verdicts:**

| Verdict | Test (against subsequent evidence known today, 2026-07-31) |
|---|---|
| **IMPROVED** | Evidence sides with the POST-revision state over the pre-revision state: the outcome landed nearer the revised estimate; a falsifier the challenge forced into registration later fired/bound usefully; a claim the challenge removed was later shown false. Process-only revisions (registration, provenance, reproducibility) grade IMPROVED only if they later **bound** (were exercised on real data); otherwise NEUTRAL-PROCESS. |
| **NEUTRAL** | Revision neither vindicated nor punished: spec never exercised, hygiene with no downstream consequence, or evidence genuinely balanced both ways. |
| **HARMED** | Evidence sides with the PRE-revision state: the revision moved an estimate away from what then happened, or trimmed/retired a leg that then fired. Magnitude stated (weight-points moved, decision consequence). Graded against elegance NEVER — only against outcomes. |
| **UNRESOLVABLE-YET** | The revision's own test window is still open. The resolving date/event must be named. A real category, not a miss. |
| **NO-REVISION** (failed attack) | Owner rebuffed, challenge died on evidence, or nothing was adopted. Sub-grade the rebuff: REBUFF-RIGHT / REBUFF-WRONG / REBUFF-UNTESTED vs subsequent evidence. |
| **UNGRADEABLE** | No frozen pre/post state exists in the record to grade against (early-cohort sweep rows). Counted in the denominator disclosure, excluded from rates. |

**Multi-leg rule (packet guard):** where one challenge produced several revision legs that diverge (e.g., a confidence cut + a channel retirement), legs are graded separately and itemized; the row's headline verdict is the most decision-relevant leg.

**Evidence discipline:** pre/post states quoted from the frozen record (file+row or commit); subsequent evidence carries source+date; no retro-editing of what the challenge actually demanded. Where RED's challenge was directionally right but RED's own *sizing/weight* consequence was wrong, both are logged — the second does not launder the first.

**Conflict flag ⚑:** rows where the grader-is-graded tension bites (self-challenges; revisions to RED's own hypothesis weights; rows where RED wrote both the challenge and the resolution text) are marked ⚑ for PROME's independent spot-check.

**Rates reported:** harmful-revision rate = HARMED / (IMPROVED + NEUTRAL + HARMED) — i.e., over resolvable accepted revisions only — plus every denominator: total rows, rows with an accepted revision, rows gradeable at all.

---

*Grading appended below this line in a separate, later commit — per the pre-registration guard.*

## GRADES (2026-07-31, second commit — rubric above was frozen first)

*Verdicts are on the ACCEPTED REVISION. "Evidence" = subsequent evidence known 2026-07-31, source+date. ⚑ = grader-is-graded flag for PROME spot-check. Compact per-row table; the six most instructive rows expanded below it.*

| CHG | Target | Accepted revision (frozen record) | Subsequent evidence (as of 7/31) | Verdict |
|---|---|---|---|---|
| 001 | SSB $90P | none recorded (advisory EV grade) | position outcome not in record | UNGRADEABLE |
| 002 | SAM | Shunto → #2 catalyst | catalyst ranking's own test not traceable | UNGRADEABLE |
| 003 | Full system | none (baseline sweep) | — | UNGRADEABLE |
| 004 | KRE June puts | prefer Dec expiry over near-dated | June/May KRE puts died; KRE Dec $60P ×7 = "best-surviving structural vehicle" (docket) | **IMPROVED** |
| 005 | Full system (war) | none recorded | — | UNGRADEABLE |
| 006 | Portfolio | timeline-to-instruments discipline | Jun-18 stack expired into VIX-17 risk-on tape exactly as warned Apr-2 (TSV 006 resolution) | **IMPROVED** |
| 007 | All agents | Unanimity Protocol installed | protocol re-fired usefully S22 (5/7 bull-convergence flag); bifurcation it predicted printed for months | **IMPROVED** |
| 008 ⚑ | PROME/network weights | **Policy Rescue 11% → 20%** ("stealth QE active, eSLR, unused tools") | Waller hawkish pivot 5/22; Warsh hike-regime FOMC 6/17 ("easing gutted", dots +40bp); Fed-hike-2026 = base case (ORACLE 71.5% 7/24); Rescue now 2%. TSV 008: "premise dead" | **HARMED** |
| 009 | LABOR/CARL | weighted counter-signals adopted (bull/bear probs, not dismissals) | exercised continuously since — claims 75/25 correctly held off bear-cuts through 1969-low prints (7/23-7/31) | **IMPROVED** |
| 010 | BROCK | none — row sat ACTIVE since 4/2 | **stale-ACTIVE row found by this ledger build — flagged to next DUE-scan** | UNGRADEABLE |
| 011 | BRENT | **none — challenge falsified in 3 days** | Dated Brent $141 physical (TSV: "RED WAS WRONG. Oil ceiling counter-signal invalidated") | NO-REVISION / REBUFF-RIGHT |
| 012 | HAWK | none (challenge WEAKENED) | convergence-scalar question resurfaced independently at CHG-043; not attributable | NO-REVISION / REBUFF-UNTESTED |
| 013 | LABOR/CARL | employment-channel activation ↓ to 35% | employment transmission inert ever since — claims 187-197K = 1969-lows (DOL 7/23-7/31) | **IMPROVED** |
| 014 | LIQUID/ALL | HY-OAS upgraded to strongest counter-signal; HYG exit rec; LIQUID → 🟡 | HY tightened 305→266 over 10 wks; HYG puts died at $0.03; exit rec right for ~15 wks (the 7/27+ >280 sustain came via risk-premium, months after the June instruments died — does not rescue the pre-revision state) | **IMPROVED** |
| 015 | ALL | none (3-5d discriminator registered, expired) | resolved bull emphatically (TSV 015) | NO-REVISION |
| 016 | TLT/HYG | none recorded | duration threat played out as warned; no revision to grade | NO-REVISION |
| 017 | BRENT/HAWK | muted-Kharg reframed → paper-physical bifurcation (VX-RED-019) | frame correctly described the regime for months (paper −37% peak-to-Apr-17 while physical held) | **IMPROVED** |
| 018 ⚑ | RED/self | pre-registered HY-285 rule HONORED → HYG exit | HY never re-widened in the instruments' lifetime; HYG died worthless | **IMPROVED** |
| 019 | LIQUID/BROCK | RE-TARGETED into 027/028 lineage | graded there | UNGRADEABLE (merged) |
| 020 | Portfolio | size-timeline-to-instruments (COMPELLING) | VINDICATED per TSV: every named near-dated leg expired worthless; surviving book is long-dated (Dec/Sep) + duration | **IMPROVED** |
| 021 | HENRY/REGINALD | none recorded (squeeze warning) | squeeze played out (banks rallied into June, WAL ~79) — direction right, nothing revised | NO-REVISION |
| 022 ⚑ | Self/calibration | ranges widened post-Apr | S17 reconcile: "the four new CORRECTs are all modal non-occurrence landings (RED widened ranges post-Apr lesson and it paid)" | **IMPROVED** |
| 023 | VIOLET | VIX-25 distribution ~48% → ~14% (converged to RED's 18%, gap 30pp→4pp, May-3 post-mortem) | VIX never crossed 25 by 5/19 (peaked 19.21); RED-16 CORRECT at modal 82% | **IMPROVED** |
| 024 | BRENT | 3/5 legs adopted (spread-citation retired; curve-flattening; Phase-simultaneity); ch3 REBUFFED | ch3 rebuff RIGHT (rigs 429 falsified RED-19, BRENT-confirmed 5/31); adopted legs neither punished nor decisively vindicated (regime changed with July re-escalation) | NEUTRAL (+1 REBUFF-RIGHT leg) |
| 025 | REGINALD | V2.1: V1 restored pending MI3; EV Jun-conditional; $65P close-rec withdrawn; bear 37→42 | MI3 STILL untested (FFIEC ~8/15); B1 fired via 10-Q (supports restore) but borrower cured at Q2 ($0 charged, REG-26 disconfirmed); $65P leg de-minimis (died OTM either way); bear-prob leg open to Q3/9-18 | UNRESOLVABLE-YET (MI3 ~8/15; WAL Q3; 9/18) |
| 026 ⚑ | RED-self / REGINALD V2.2 | V2.2 shipped MORE bearish than RED's HOLD-rec (bear-medium 30, EV $67.98, PT $50-68) | interim AGAINST the acceleration: Q2 cohort benign 7/21-22, WAL leading ticks reverted, WAL $80.57 [7/31 boot.py] vs EV $67.98 — but bear-MEDIUM horizon runs quarters (Sep $70P 9/18, Q3 prints) | UNRESOLVABLE-YET, interim lean HARMED — logged, not banked |
| 027 ⚑ | Self (bifurcation) | live self-falsifier, count corrected twice (S20 over-read fixed) | eval ~1.5/4; capitulation review armed on BDC 8/4-8/6 | UNRESOLVABLE-YET |
| 028 ⚑ | Self (stagflation-realization) | re-anchored 10/14+11/10 two-print (S25) | resolves Oct-Nov. **One graded sub-leg: the S15 "no snap-mechanism survives → Managed modal" over-read (Acute 12→10) was WRONG vs evidence available days later (DIET signature survived + firing) — self-caught and WITHDRAWN in S16 within one session-cycle = a small HARMED leg, corrected fast** | UNRESOLVABLE-YET (+1 self-caught HARMED leg, 2pp, <1 cycle) |
| 029 | SAM | SAM-21 75% → ~90% (defiance universe 0/2; earned-discount ruled out-of-regime) | **BOJ hiked 6/16 as-priced — SAM-21 ✅** (S20) | **IMPROVED** |
| 030 | SAM | Branch-C disposition split (political/fiscal/ambiguous) pre-registered | BOJ hiked → Branch C never fired; spec unexercised | NEUTRAL-PROCESS |
| 031 | SAM | **SAM-23 MOF-intervention 72% → ~35%** (behavioral falsification of level-trigger anchor) | no strike by 6/16; **MOF monthly ¥0 Jun-29→Jul-29 = the no-strike adjudication HARD-CONFIRMED — SAM's own 7/31 closeout calls CH-011 "the cleanest stamp"** (commit 060abd20) | **IMPROVED** (cleanest in the book) |
| 032 | SAM | 4 pillars audited; modal re-derived 148-152 → 154-160 (USDJPY); yen-strength case → conditional-tail 25-30% | USDJPY ran 159.8→163.7 through July — pre-revision state (148-152) never printed; revision direction right, magnitude still short (noted) | **IMPROVED** (directionally) |
| 033 | VIOLET | sustain-n REGISTERED (n=5 TAIL-STOP, empirically derived); falsification-weight architecture written into TRADE.md; RED's n=3 remedy DECLINED | exercised through three vol episodes (VIX 22.24 Jun / 21.5 NFP / 20.66 FOMC-Jul) with zero false stop-outs and no missed fire; the n=3 RED wanted would have false-fired the 2023-09 path — **rebuff RIGHT** | **IMPROVED** (+1 REBUFF-RIGHT leg against RED) |
| 034 | VIOLET | two-anchor ladder registered (KB-VIO-089, Orch-reproduced); RED's 26+ tail leg right / 24 leg wrong at grading | VIX has not reached 24/26 since — ladder unexercised at the tail | NEUTRAL-PROCESS (bidirectional score stands) |
| 035 | VIOLET | CCC-9.55 2-bin tree pre-registered BEFORE the FRED pull; "LIQUID tripwire" mis-attribution corrected | **EXERCISED HARD: CCC crossed 955 (WL-05) then 1000 (WL-06 FIRED 7/27, holding ×4)** — crosses scored as fired gates, not goalpost-moved; the exact failure mode the challenge named was averted | **IMPROVED** |
| 036 | VIOLET | fade 40-45% → 20-26%; stand-aside 50-60%; P(fade pays\|stabilizes) 0.85→0.75; C-hot/C-frozen split | **Iran did NOT stabilize — July re-escalation was the cycle's largest** (first-ever $100.19 settle 7/23, formal Hormuz closure, OVX 70, kinetic tanker attacks). Fading war-vol at the old 40-45% would have been run over; the revision moved VIOLET to stand-aside BEFORE it | **IMPROVED** (highest-consequence row in the book) |
| 037 | VIOLET | tooling/mechanization pass (VIOLET added a 4th error instance herself) | completion of the tooling pass unverified on RED surfaces | NEUTRAL-PROCESS |
| 038 | VIOLET | SHADE estimate restored 55-60%; ABANDON condition registered | downstream print outcome not recorded on RED surfaces | NEUTRAL-PROCESS |
| 039 | SAM | v1.6: MED-HIGH → **MEDIUM** (SAM's own EV-band gate); Sep-18 retire-window LOCKED; Channel-1 retired; ≤0-EV → trim-tilt | no unwind trigger has fired; carry kept paying to USDJPY 163.7; SAM FLAT through BOJ 7/31 (Branch C confirmed, no trigger) — MEDIUM vindicated over MED-HIGH so far. Watch: USDJPY 159.2 falling toward WL-12 (<155 s=3); tail paying pre-9/18 would make the downgrade premature | UNRESOLVABLE-YET (9/18), interim IMPROVED |
| 040 | REGINALD/CORAL | none — discriminator challenge, pre-registered at Q2 | resolved SPLIT 7/24: OZK name-leg confirmed RED; cohort-leg = REGINALD's reconciled-benign framing vindicated (7 surfaces benign) | NO-REVISION (discriminator; REBUFF-RIGHT at cohort, challenge-right at name) |
| 041 ⚑ | BRENT/HAWK + RED's own weights | **L1:** structural-decoupling adjudication held OPEN (tail-mispricing case kept alive at reduced size vs closing structural-bull). **L2:** RED's own consequence — War 7→6 + energy-tail 🟠→🟡 (7/10), a SMALLER cut than RED's own 7/8 pre-registration demanded | **The tail fired severalfold 7 days later** (7/17-23: $100.19 first-ever settle, GATE-FALCON-001 kinetic, GATE-OSPREY-001 barrels offline, formal Hormuz closure — TSV 041 reopen condition met "severalfold", S24). L1 = keeping the case alive was RIGHT. L2 = cutting the tail into the realization was WRONG (already logged as "the CHG-041 sizing error", S24) — and the pre-registration deviation CUT the harm (−1 instead of the fuller registered reversal) | **HARMED** (headline = L2, the decision-relevant leg; L1 itemized IMPROVED) |
| 042 | FALCON/BRENT/NEXUS/fleet | axes pre-registered; no fleet revision pre-fire | interim 3-of-4 axes confirmed by the 7/17-24 week; residual = de-escalation decay-split, unexercised | UNRESOLVABLE-YET |
| 043 | FALCON/NEXUS/fleet | recs OPEN (FALCON P/R split-scalar; NEXUS route-count) — nothing folded yet | falsifiers live | UNRESOLVABLE-YET |

### The six most instructive rows

1. **CHG-008 (HARMED, the clean one):** the Apr-2 unanimity sweep's flagship revision — Policy Rescue 11%→20% on "stealth QE / eSLR / unused tools" — was the single materially harmful revision of the book. It held elevated ~7 weeks until the Waller pivot (5/22) and died completely under the Warsh hike regime (Rescue now 2%, market prices HIKES). Cost: ~9pp of hypothesis mass parked on a tail that inverted, funded from bear-side mass, during weeks when the bear's duration channel was the one paying. The premise was defensible *at the time*; the rubric grades outcomes, and the outcome is unambiguous.
2. **CHG-041 (HARMED, the expensive one):** both harmful headline rows are **tail-weight revisions, opposite directions** — 008 sized a tail UP that died; 041 sized a tail DOWN 7 days before it fired. Neither is a mechanism error; both are tail-sizing errors, consistent with the prediction book's known narrowness signature (RED-02/03 class). The mitigation on 041 is real: the challenge leg itself (keeping the tail-mispricing case alive against a "settled regime" adjudication) is what made the July War re-mark defensible, and deviating from my own pre-registered fuller cut reduced the damage. Class lesson already promoted: tail re-marks between regime evidence are where RED's harm concentrates.
3. **CHG-031 (IMPROVED, the cleanest):** MOF-intervention 72%→~35% — subsequently hard-confirmed by MOF's own ¥0 print, and the *target* calls it the cleanest stamp in its book (SAM closeout `060abd20`). The full loop: challenge → structural re-derivation → target adopts a LARGER cut than asked → primary-source confirmation.
4. **CHG-036 (IMPROVED, highest consequence):** the fade-weight cut moved VIOLET from fade-leaning to stand-aside ~5 weeks before the largest war re-escalation of the cycle. Counterfactual exposure at the pre-revision 40-45% fade weight through the 7/17-23 week is the biggest single harm this ledger can find that *didn't* happen.
5. **CHG-033/035 (IMPROVED, and the rebuffs matter):** the two registration challenges were exercised for real — 035's pre-registered CCC tree bound at the actual 1000-cross (7/27); 033's n=5 line survived three vol episodes without a false stop. And VIOLET's rebuff of RED's proposed n=3 was RIGHT — preserved per the task's failed-attack requirement, alongside CHG-011 (RED's oil-ceiling challenge, falsified in 3 days by Dated $141).
6. **CHG-026 (⚑ the tension row):** REGINALD's V2.2 went *more* bearish than my HOLD-rec asked, and the interim evidence (benign Q2 cohort, WAL $80.57 vs EV $67.98) currently leans against that acceleration. I am the wrong grader to close this row — it stays UNRESOLVABLE-YET on its own horizon (MI3 ~8/15, Q3 prints, 9/18 vehicle) with the interim lean logged, and it is first in line for PROME's independent spot-check.

## SUMMARY STATS (as of 2026-07-31)

| Denominator | n |
|---|---|
| Total challenge rows | 43 |
| Gradeable at all (frozen pre/post state exists) | 37 |
| — with an accepted revision, resolvable today | **24** |
| — with an accepted revision, window still open (UNRESOLVABLE-YET) | 7 |
| — failed attacks / no revision (rebuffs preserved) | 6 |
| UNGRADEABLE (no frozen record; incl. 1 stale-ACTIVE row flagged, 1 merged) | 6 |

| Verdict (headline, resolvable revisions) | n | share of 24 |
|---|---|---|
| IMPROVED | 17 | 71% |
| NEUTRAL / NEUTRAL-PROCESS | 5 | 21% |
| **HARMED** | **2** | **8%** |

**Harmful-revision rate (headline): 2/24 = 8.3%.** Leg-level: 3 harmful legs (008; 041-L2; 028's self-caught S15 leg, 2pp, corrected within one cycle) across ~30 graded legs = ~10%. Both headline HARMED rows are **tail-sizing revisions** (one up-sized a tail that died, one down-sized a tail that fired), not mechanism revisions — matching the calibration book's known narrowness signature. Failed attacks preserved: 6, of which the owner (or reality) was RIGHT to rebuff in 3 (011, 024-ch3, 033-n3), UNTESTED in the rest. Conflict-flagged rows for PROME spot-check: **008, 018, 022, 026, 027, 028, 041** (026 first).

**Hygiene catches made by this build (flagged, not fixed here):** CHG-RED-010 has sat ACTIVE since 4/2 with no disposition — goes to next boot's DUE-scan. *(→ DISPOSITIONED same day, S27b: RESOLVED / PARTIALLY CONFIRMED / EDGE-MIGRATED — awareness went mainstream AND wrapper-equity shorts stopped paying as it spread; edge migrated to instrument-level measurement now owned by BRK-30/32 + the register. Its ledger verdict upgrades UNGRADEABLE → NO-REVISION (challenge-direction right, nothing revised — BROCK's register/instruments are successor work, not a forced revision): denominators shift to 37 gradeable / 7 NO-REVISION / 5 UNGRADEABLE; headline rate unchanged at 2/24 = 8.3%. Root cause of the 120-day silence: the row's resolution-event field was EMPTY, and the DUE-scan flags rows past a date — an undated ACTIVE row is invisible to it by construction. W2 discipline extended: ACTIVE challenge rows must carry a resolution date/event or a named re-review date. ML-RED-125.)*

---

*Grading completed 2026-07-31 S27b. Rubric was committed (`661a3024`) before any row was graded. Grade against frozen states only; where a revision had diverging legs, legs were graded separately per the packet guard. UNRESOLVABLE-YET rows re-grade at their named windows: 025 (~8/15 MI3), 026 (Q3/9-18), 027 (BDC 8/4-8/6), 028 (10/14+11/10), 039 (9/18), 042/043 (falsifiers live).*
