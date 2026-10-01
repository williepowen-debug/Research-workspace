# PR#7 map re-cut: drafter notes (2026-10-01)

**Inputs:** the six reader reports `AGENTS/DAEDALUS/upgrades/PRODUCTION_REVIEW_2026-10-01_READER_R{1..6}_*.md`, the current `FLEET_MAP.tsv` rows, and the ladder in `AGENTS/DAEDALUS/CLAUDE.md` § MATURITY LADDER. I also read `AGENTS/DAEDALUS/STATUS.md:41-49` for the DAEDALUS dates: WQ-286 is dated 10/05 at :44; the profile queue, H2 and Prose-Remedy are re-dated 10/12 at :48; PR#8 is 10/15.
**Output:** `RECUT.tsv` has 40 rows, 29,740 B. Every Gaps cell is ≤450 chars, every Next_upgrade ≤260, and every Move reason ≤120.
**Cohort count:** the brief says 39 desks, but its list names **40**: R1 9, R2 7, R3 6, R4 8, R5 5, R6 5. I drafted all 40.

**Moves applied:**
- CORAL UP L3→L4 (M).
- FERT UP L3→L4 (M).
- YURI UP L1→L2 (M).
- OSPREY, CREED and CRUISE CONF M→H.
- MARCO CONF H→M.
- The other 33 rows HOLD.

**Byte legs:** every L5 and Conf byte leg is re-cut to `read_cap_check --agent X: rotation_due=0`. No cell requires "<22,785 B" as a standing condition.

---

## 1. Per-agent: claims refuted or overtaken (→ FLEET_MAP_HISTORY)

Locators are the reader's. "Row" means the current FLEET_MAP cell, scored 9/17 or 9/24.

| Agent | Claim in the current row | Verdict | Locator |
|---|---|---|---|
| PROME | SCRATCH 26,535 B (82%) and ACTIVE_DECISIONS 25,046 B (77%) unrotated, which made them the L5 instance | OVERTAKEN: SCRATCH 24,315 B, AD 22,568 B, rotation_due=0. The L5 gate now fails on a new instance: the spine audit is past its cadence since 9/27. | R1 §1; `PROME/STATUS.md:3` |
| PROME | HEARTBEAT 21,070 B (65%) | OVERTAKEN: 22,647 B after re-base #25 | `c0642a8f6` |
| PROME | 'prome_gate check-family ≠ 22' leg: grep returns 15 | Count is now 18; the counting rule is still unstated | R1 §1 |
| WALTER | "D4 edit built 9/24, reader pending" | OVERTAKEN: D4 FIXED 9/24 on the independent read | `AGENTS/DAEDALUS/STATUS.md:37` |
| WALTER | Push-binding contradiction "needs Will's word / route it" | NEVER ROUTED: there is no WQ row. Root `CLAUDE.md:84` already names BCS §7, so the fix is a desk-side alignment (decision 5) | R1 §2 |
| WALTER | Profile refresh should re-cite "BCS v0.31" | REFUTED as written: BCS has been v0.32 since 9/17 | `d35d91948`; BCS:3 |
| WALTER | CLAUDE.md 63,141 B above the 54,250 B harness cap; self-cap leg | REFUTED as a cap breach: READ_CAP rule 20 (`390e6a252`). Charter is now 65,503 B. Leg struck (decision 4). | R1 §2 |
| WALTER | Line cites `CLAUDE.md:147`, `BCS:85-88` | Drifted to `:149` and `:87`, `:502-504` | R1 §2 |
| NEXUS | STATUS 31,508 B (97%), PREDICTIONS_MONITOR 29,065 B (89%) | OVERTAKEN: 22,776 B and 12,259 B | `0e9ebf96d`, `f61df31de` |
| NEXUS | CLASS-row declaration owed | DISCHARGED | `PROME/registry/READS.tsv:289`, `:311` |
| NEXUS | Five briefs at 2.2–4.2× budget | OVERTAKEN: only ZHAO 122% and BROCK 106% remain over | R1 §3 |
| NEXUS | "13 consumed outcomes" leg | UNEVALUABLE, no referent (0 hits at PR#6 and PR#7). Struck (decision 4) | R1 §3; `PRODUCTION_REVIEW_2026-09-17_READER_R1:378` |
| NEXUS | Re-date PRED-38/40/45 | DONE | `PREDICTIONS_MONITOR.md:4,12,38,40` |
| RED | CANDIDATE: VX banner "9 of 17 CARRIED" vs grep 11 | OVERTAKEN: banner re-cut S46 9/18. `review_debt.py` now reads 7 of 17 | `037aabc6b` |
| RED | Joint-session Conf leg | Re-keyed: RED drafts in its own tree, WALTER countersigns by packet | R1 §4 C |
| TERRY | STATUS 32,526 B = 100% | OVERTAKEN: rotated to 21,628 B | `cef85d580` |
| TERRY | Drain section I non-empty, not re-measured | OVERTAKEN for 1 of 2 cycles: section I = 0 at HEAD | R1 §5 |
| TERRY | "(d) REGINALD's concurrence asked" | UNVERIFIABLE: no concurrence row found | R1 §5 |
| ORACLE | Write the ORC-04 roll rule only after WQ-190 succession is ruled | OVERTAKEN: WQ-260 ruled 9/24; v5 October roll encoded 9/28 | `0289ac024`, `ab5f689d9`, `279b7aec1` |
| ORACLE | KB-ORC-086 settled-market 50.0 mid | PARTIAL: Polymarket side fixed in code 9/17; Kalshi back-sweep has no artifact | `5462b6e06` |
| DEWEY | Proposal (b) WALTER-ledger impact column "in outbox 53d unmoved" | REFUTED (wrong when written 9/01): WALTER shipped it 7/24. The outbox file is residue, and the "outbox disposition (PROME)" leg is struck | `PROME/inbox/processed/2026-07-24_from-WALTER_dewey-process-v2-both-items-shipped.md:17` |
| DEWEY | STATELESS cite at profile :34 / CLAUDE.md:205 | Text now at `CLAUDE.md:206` | R1 §7 |
| RAV | PROME read at `PROME/reviews/2026-09-15_rav-maturity-and-cato.md`; "two desks now grade RAV" | REFUTED: the file is at repo-root `reviews/`, and it defers to this row (`:9`, `:86`). The "settle who grades RAV" leg is struck (decision 8) | R1 §8 |
| RAV | ROSTER:144, :152 | Drifted to :145, :153 | R1 §8 |
| RAV | 43 dark days | Now 57 | R1 §8 |
| DAEDALUS | Scorecard render #4 CANNOT-RENDER | OVERTAKEN: rendered 9/24 | `339c5d0d1` |
| DAEDALUS | Independent reader on D4 owed | DONE (D4 FIXED 9/24, WQ-229) | `STATUS.md:37` |
| DAEDALUS | L3 'FLEET_MAP current' MET | OVERTAKEN then FAIL at boot (SELF-ROW 7d). This re-cut discharges it | `sweeps_due.py` |
| DAEDALUS | 9/25 profile queue | TRUE-STILL and overdue; re-dated 10/12 and grown (+BROCK, CREED) | `STATUS.md:48` |
| LIQUID | STATUS 34,662 B = 106%, rc=1 | OVERTAKEN: 22,855 B, rc=0 | `7ad941929` |
| LIQUID | Desk dark 5d | OVERTAKEN: 71 own commits | R2 |
| LIQUID | KILL_MEMO has no 8/28 drill-log row | OVERTAKEN: row added | `db397a6b9`; `KILL_MEMO_HY_OAS_260.md:235` |
| LIQUID | (a)–(d) legs on no live surface | UNVERIFIABLE across PR#5, PR#6 and PR#7. Struck (decision 4) | R2; PR#6 R2 `:101` |
| CARL | L5 re-test after the PHAN pass (target 9/25) | Pass did not happen (re-targeted 10/02). Leg re-keyed to `ledger_staleness.py` 0 stale (decision 6) | `AGENTS/CARL/SCRATCH.md:52` |
| CARL | "Profile body 7/10 = 76d" | REFUTED when written: reinstalled 9/17 | `a020e7714` |
| CARL | CRL-08 / CRL-17 to resolve 9/30 | DONE 10/01 | `2288ba032`, `0f8444c60` |
| CARL | boot.py:150-154 | Now cited at :152 | R2 |
| BROCK | n=3 owner-declared ledger defects | Now n=4: STATUS:91 BRK-30 vs the ledger, found by RED 10/01 | RED packet `inbox/2026-10-01_from-RED_STATUS-BRK-30-…` |
| BROCK | Desk-side items "dated inside 9/30" | All five NOT DONE; the deadline passed | R2 §BROCK A |
| CREED | n=1 session in period | OVERTAKEN: 85 own commits | R2 |
| CREED | VX.tsv 47,960 B = 147%, rc=1 | OVERTAKEN: 22,221 B after the split; attested manifest | `72303435c` |
| CREED | Conf M→H on a second graded session | MET 9/28 and 9/29 | `dcffd6599`, `a88e3a256`, `c36124db1` |
| CREED | Eval-decontamination confirm-read | DONE: NOT decontaminated, and unowned. Struck as a Conf gate; recorded as an ownerless defect for PROME (decision 4) | `evals/results.tsv:1`; `SCRATCH.md:87` |
| BOND | STATUS 72% | Now 69% | R2 |
| BOND | STATUS.md:78 mirror divergence (VX-05, VX-16) | PARTLY OVERTAKEN: VX-05 agrees, VX-16 = 4 vs 2 persists, and the disclosure is gone. :78 is now the Composite line | R2 |
| BOND | "6 TSVs" | Reader counts 5 core TSVs | R2 |
| REGINALD | STATUS 9/14 / BL 9/11 lag | OVERTAKEN: both dated 9/29 | `STATUS.md:7,:131` |
| REGINALD | rc=1, 4 boot reads over budget | OVERTAKEN: rc=0 | `a5bdcd09f` |
| REGINALD | Profile "48d alert" | 55d | `profile_clock_check` |
| HENRY | STATUS 99% | Rotated 9/25 to 69.9%, then regrew to 97% by 9/30 (PAT-055) | `dea50473c` |
| SAM | `CLAUDE.md:86` hygiene licence | Cite drifted to `:93` | R3 |
| SAM | SAM-28/31 not re-verified | VERIFIED | `PREDICTIONS.tsv:45,48` |
| SAM | Sep-16 SAM-33 check | OVERTAKEN (falsifier un-fired through 10/1) | `STATUS.md:39` |
| SAM | STATUS 72% | Now 74% | R3 |
| SAM | red/ CH-009, CH-012 | CH-009 CLOSED 10/01; CH-012 answered 9/29 | `0ad317cfc`, `970904c74` |
| ZHAO | 15 dark days | OVERTAKEN (largest gap 6d) | R3 |
| ZHAO | RatingDog Aug owed | DONE | `STATUS.md:65` |
| ZHAO | Close spawn-or-reclassify to YES-ACTIVE | OVERTAKEN: ACTIVE | `PROME/ROSTER.md:79`; `dd6661e99` |
| HANS | SUSTAIN needs one more closeout | MET 9/25 | `6c46eb0ae` |
| BRENT | STATUS 65%, TRADE 77% | STATUS REFUTED at HEAD (85%); TRADE OVERTAKEN (52%) | `77b8f8af6` |
| BRENT | PR#6 asks due 9/30 | Ask 1 MISSED; 2a DONE; BRT-26 split moot (resolved 9/25) | `72ac567ab` |
| BRENT | Freeze-or-refresh LESSONS_INDEX/INCIDENTS/REGISTRY | DONE | `ledger_staleness` |
| BRENT | Leg (c) "no outside correction" | Struck as a Conf gate (decision 4). It failed this cycle on a PROME correction | `e5dfbfa12`, `6f2ca390d` |
| LABOR | LESSONS 99%, STATUS 99%, NEXUS_BRIEF 94,318 B | OVERTAKEN | `d8ef31719`, `6c977dc54`, `13f40e9c5` |
| LABOR | Sustain leg "before the Oct-2 freeze (~9/25)" | MISSED by letter at the 9/24 freeze; CURED 9/29 before the print | `6145aa00d` |
| VIOLET | L5(b) legs 3 and 2 pending | MET | `1f74e3378`, `d0d7c1275` |
| VIOLET | MEMORY 25,339 B (78%) | Now 22,914 B | R3 |
| VIOLET | Conf keyed to the profile refresh | Re-keyed to desk legs (decision 4) | R3 §VIOLET C |
| HAWK | HAW-19 leg A unfireable | OVERTAKEN: HAW-19 → DEFECTIVE-INSTRUMENT 9/28 | `2d3bb96df` |
| HAWK | Register capacity-only successor by 9/25 | OVERTAKEN: NOT-REGISTERED on data; HAW-22 registered 9/26 | `42ce71cc6`, `bba2e26fd` |
| HAWK | "Or re-enters a 0-OPEN gap" | REFUTED: HAW-20 and HAW-22 OPEN | `thesis/PREDICTIONS.tsv` |
| FALCON | STATUS 70 ln / 9,019 B | Now 84 ln / 11,312 B | R4 |
| FALCON | EXIT_PROTOCOL.md:3 three stamps | OVERTAKEN: v3 rewritten 10/01 | `437af2327` |
| FALCON | FAL-05 the 1 OPEN row | FAILED 9/28, 11 days late; FAL-06 registered 10/01 | R4 |
| FALCON | Boot check for the dated line owed | Partially closed by a prose closeout step 11; no script | `EXIT_PROTOCOL.md:79` |
| OSPREY | Retract banner at profiles/OSPREY.md:3 | DONE 9/24 | `36e8d638f` |
| OSPREY | Channel-3 limb 2 UNDETERMINED, HAWK's word only | Verified | `c9089a455`; `STATUS.md:47` |
| YURI | "No YURI session has run" | REFUTED: sessions 9/25 and 9/26 | `0abe3353c`, `5bf10bb90` |
| YURI | 0 written by the desk; banner DAEDALUS-transcribed | PARTLY REFUTED: desk re-cut YUR-001 and struck the banner. New rows still 0 | `0abe3353c` |
| YURI | No NEXUS_BRIEF yet; registration ROUTED not landed | OVERTAKEN (both) | R4 |
| YURI | L2 path via mil.ru | mil.ru is unreachable (000), so dropped | `STATUS.md:25` |
| MIDAS | STATUS 99%; THESIS:45-46 stale; beta unrun; grade packet owed | ALL OVERTAKEN/DONE | `1d746010b`, `f86fd682c` |
| FERT | "L4 blocked on a leg not FERT's to clear, at the ladder sitting" | No sitting row exists. Resolved by decision 2 (frozen file with an explicit unfreeze condition passes) | R4 §0 |
| FERT | Event-keyed profile trigger is the only NOT FIRED one | OVERTAKEN: FIRED (26d) | R4 |
| WATT | Metered-vs-DR "moves to a dated DOCKET row" | Row was NOT created | R4 |
| WATT | Name DM2 as WATT-11 co-instrument | OVERTAKEN: WATT-11 graded MISS | `2a64a6dd5` |
| WATT | Correct STATUS.md:37 | DONE (`STATUS.md:39`) | R4 |
| VULCAN | Grade packet owed | DONE | `f86fd682c`, `f905c37ed` |
| VULCAN | STATUS 93% | Rotated, now 71% | `193ed19e7` |
| VULCAN | Close mag7 9/11 miss and 4 DRAM reads before MU FQ4 | REFUTED: misses grew (3 mag7; 0 of 8 S2) | `STATUS.md:42,:80` |
| CORAL | F-2 −56.5% arithmetic | OVERTAKEN: −37.0% same-vintage | `STATUS.md:53`, `e10db55db` |
| CORAL | STATUS 32,493 B = 100% | Rotated 9/28, regrown to 77% | R5 |
| CORAL | No TRADE surface | REFUTED: DECLARED FLAT 9/28 | `496403f3b` |
| CORAL | Citizens observable owed; criterion-5 instrument unbuilt | DELIVERED / BUILT | `STATUS.md:40`, `8ce8ecb83` |
| MARCO | MEMORY 151%, STATUS 104% | OVERTAKEN: 74% and 70% | `3b365a0ac` |
| MARCO | Citizens vintage split CANNOT-EVALUATE | REFUTED (closed) | `STATUS.md:78` |
| MARCO | (new) TRADE.md went FROZEN 9/24 | L4 trade leg weakened | `1fe88f48e` |
| HOMER | Both L3 legs unbuilt; no THESIS.md | REFUTED for the kill rail: built 9/29 | `74089ab84`, `741467fa9` |
| HOMER | NEXUS_BRIEF:45 Trepp courier; 109,239 B | OVERTAKEN (fixed; 13,908 B) | `72e63a82a` |
| AEOLUS | STATUS 99.86% | OVERTAKEN: 60% | R5 |
| AEOLUS | Consumption legs MARCO C5 / WATT C3 NOT-ADJUDICATED | Adjudicated: both NOT MET (other desks' trees; R5 says they should not gate AEOLUS) | R5 |
| SHADE | 20 dark days, 11 routed items | OVERTAKEN: 10/1 session, 25-item drain | `20261f699` |
| SHADE | T-SHADE-01 readings stale (276 vs >280) | OVERTAKEN: re-read 10/1, NOT ARMED | `STATUS.md:33` |
| SHADE | Kill-path #4 graded vs REGINALD Brent $104.61 [9/11] | Not done. The re-key to a live read (root rule #4) is in Notes §4, not the cell | R5 |
| OZK | 17 dark days; STATUS identical | OVERTAKEN | `4f6852513` |
| OZK | KB_INDEX tables max 227 | PARTIAL: re-rolled to 241, but 218/219 are in no table | `ef900ced0`, `KB_INDEX.md:15` |
| OZK | Outbox 13 files; 2 inbox packets; group token 36; OZK-09 un-instrumented | FIXED / OVERTAKEN | `c96980acf`, R6 |
| WAL | 15 dark days; STATUS 3 B under budget; KB_INDEX 7 rows behind | OVERTAKEN / FIXED. STATUS regrew to 78% | `0721aded3`, `d959e96f8` |
| WAL | Profile 36d past trigger | Worse: body 8/07 (55d), content stale | R6 |
| FLG | Ledger row counts KB 52 / TRIGGERS 11 | Accrued to 71 / 13 | R6 |
| FLG | 20 dark days; 4 packets behind the 10/01 wake | OVERTAKEN | R6 |
| FLG | T-08 wake triple-wired | DISCHARGED: FIRED and graded 10/01 | `d9fcfc1bd` |
| OTTO | Item (c) STATUS 32,519 B = 100% | OVERTAKEN: 22,373 B (9/28) → 22,959 B | `c922a00b3`, `3f488b4e1` |
| OTTO | L5 item 1 "<22,785 B by NET delta" | MIS-SPECIFIED against canon (DAEDALUS-authored). Re-cut to rotation_due=0 (decision 3) | R6 §OTTO C |
| CRUISE | Demote L3→L2 if the 9/29 print occurred and no session followed | DID NOT FIRE: graded the same day | `c69daded1` |
| CRUISE | Profile clock 10/03 | NOT MIRRORED: `profiles/CRUISE.md:5` still reads 9/26 | R6 |

---

## 2. DAEDALUS-owed items named by the readers

| # | Item | Agent(s) | Source | Date / key |
|---|---|---|---|---|
| D1 | **Profile refresh, FIRED (30 + 1 probable):** PROME, WALTER, NEXUS, RED, TERRY, DEWEY · LIQUID, BROCK, CREED (floor 9/25 passed), BOND, REGINALD (55d ALERT), HENRY · SAM, ZHAO, HANS, VIOLET · HAWK, FALCON, OSPREY, MIDAS, FERT, WATT, VULCAN · HOMER, AEOLUS (Mode-A fan-out = AEOLUS Conf gate), SHADE · OZK, WAL (body 8/07), FLG, CRUISE · OTTO (probable) | 31 | R1–R6 §D | `STATUS.md:48` queue (AEOLUS, HAWK, HOMER, WAL, BROCK, CREED, REGINALD) 10/12; the other 24 are unscheduled |
| D2 | **Profile clocks coming due:** CORAL 10/05, LABOR 10/07, MARCO 10/20, ORACLE 10/20, BRENT 10/22 | 5 | R5, R3, R1 | as listed |
| D3 | **Profile trigger defects:** FALCON has no dated trigger; OTTO's "post-CARL-sitting" trigger is undefined (re-key to a named event); CRUISE's 10/03 clock is not mirrored at `profiles/CRUISE.md:5` (9/26); FLG's profile trigger is date-keyed (11/06), not keyed to the 10-Q occurrence | FALCON, OTTO, CRUISE, FLG | R4, R6 | at refresh |
| D4 | **`profile_clock_check.py` prints OK when only the clock is unexpired;** content triggers had FIRED for LIQUID, BROCK and BOND | tool | R2 finding 1 | — |
| D5 | **`maturity_scan.py` BOND false "predictions unresolved":** the resolved regex (`:211-213`) lacks TRUE/FALSE; `pred_arch_paths` (`:207`) misses `thesis/archive/PREDICTIONS_resolved_BND-*.tsv` | BOND | R2 finding 2 | — |
| D6 | **`maturity_scan.py` DEWEY false L0:** add DEWEY to the `:57` JUDGMENT_ONLY / stateless-by-design exemption list (decision 9) | DEWEY | R1 §7, F5 | — |
| D7 | **`maturity_scan.py` "no BOTTOM LINE" on local forms** (naming-keyed scan): CARL, LIQUID, SAM, HANS, BRENT, TERRY, PROME. **L1 local-form ruling owed**; see §4 item 2 on MARCO | 7 desks | R1, R2 finding 3, R3 floor note | — |
| D8 | **YUR-F01 1–2-call outcome undefined** ("≥3" and "0" are defined; 1–2 is not). Define it before the grade | YURI | R4 §YURI C | before 2026-10-24 |
| D9 | **RAV row locator:** `PROME/reviews/…` → repo-root `reviews/2026-09-15_rav-maturity-and-cato.md` (done in the cell). Strike the "who grades RAV" leg | RAV | R1 F4 | this re-cut |
| D10 | **WALTER 7 of 8 two-binding instances unverified** | WALTER | R1 §2 | — |
| D11 | **HENRY §2 local-form ruling** (does prose satisfy the 5-pt/composite/Independence handle?). Same handle is open on MARCO and OTTO | HENRY (+MARCO, OTTO) | R2 §HENRY | — |
| D12 | **Promote UNRECORDED-AS-MADE / UNSCORED-AS-MADE into `BLUEPRINTS/STATE_VOCABULARY.md`** | HENRY | R2 | — |
| D13 | **CRL-17 forfeited-miss ruling** (R2 says dated 10/02). `STATUS.md:44-45` already shows it **DONE 10/01** (`runs/2026-10-01_CRL17_CONTEST_RULING.md`, NO-VERDICT stands), so R2's thread is overtaken. Confirm, then close | CARL | R2; DAEDALUS STATUS | closed? |
| D14 | **ZHAO KB Vectors wrong-instrument xref checker** (heuristic proposed, not built) | ZHAO | R3 | — |
| D15 | **Encode the L4 trade-leg local form (decision 2)** in the market blueprint and ladder table; "ADAPTED-PASS" is in no BLUEPRINT | Market class | R4 §0 | — |
| D16 | **OTTO L5 item 1 mis-specified against canon** (DAEDALUS-authored). Re-cut in this pass | OTTO | R6 finding 2 | this re-cut |
| D17 | **Convention for PROME inbox→processed sweeps** breaking desks' path checks (HANS C7). Co-owned with PROME | HANS (class) | R3 cross-cohort 1 | — |
| D18 | **Confirm-reads owed:** FERT CF positioning vs no-book; YURI "accruing" (0 desk rows); OSPREY Conf H vs CATO round-count; VIOLET part-2/3 standard vs part 1; DEWEY 3 period outputs (before Conf H); BOND row-3 max-of-vectors; REGINALD 4 UNVERIFIED at profile refresh; CREED 6 negative rows' dated search; ZHAO, HAWK, FALCON, VULCAN trade-leg form (§4 item 3) | 10 | R1–R4 | PR#8 2026-10-15 |
| D19 | **HOMER "blueprint conformance grade"** after L3 (DAEDALUS-lane, not desk-clearable) | HOMER | R5 | after 3c |
| D20 | **Own row:** WQ-286 ①–④ (10/05); profile queue, H2 as-made audit, Prose-Remedy Census #1 (10/12); D7 `--closure`; `profiles/DAEDALUS.md`; PROME judgment sweep DUE +2d | DAEDALUS | R1 §9; `STATUS.md:41-48` | 10/05, 10/12 |
| D21 | **L5 adjudications at PR#8:** REGINALD (three against-legs), BROCK (per-leg table), MIDAS (second clean cycle) | 3 | R2, R4 | 2026-10-15 |

---

## 3. Threads: owners

### PROME

| Thread | Source |
|---|---|
| ROSTER contradicts itself on CATO (`:154` SPECIAL vs `:156` "pending") | R1 F1 |
| ROSTER:153 "STANDING sole-QC" for RAV while CATO did all the period's review. A wording question for Will | R1 F2 |
| CREED eval-suite decontamination has **no owner** (evals FROZEN-VOID 9/29). Name one (Will/PROME) | R2 §CREED; decision 4 |
| HENRY self-measured October-hike odds vs "priced Fed path = ORACLE's". Scope ruling | R2 §HENRY F |
| DR-1 card routing (CARL) | R2 |
| L494 X1 sustained-count sitting 10/2 (LIQUID, BROCK input) | R2 |
| WQ-357 BOND kill-letter REC (Will) | R2 |
| Spawn YURI by 10/02 (YUR-003 + WQ-293 execution) | R4 thread 3 |
| Register or strike the FERT OPEN-count incentive question (no queue row; 17d overdue) | R4 thread 5 |
| Create the WATT metered-vs-DR DOCKET row; schedule a WATT boot by 10/09 | R4 thread 6 |
| Charter sizes VULCAN 81,862 B, FALCON 49,978 B, OSPREY 48,339 B: composite-injection advisory (rule 20 = not a cap breach) | R4 thread 7 |
| FALCON production rung D85→92 + R1–R3 residue to Will | R4 thread 8 |
| MIDAS silver/PGM bands to Will | R4 thread 9 |
| Spawn SHADE before 10/08; "illiquid ABS" ratio-#2 definition (Will) | R5 §SHADE F |
| X1 ≡ T-SHADE-01 reconcile (FORUM-5 ruling 2), with LIQUID | R5 |
| OZK/REGINALD identically named `2026-07-20_to-PROME_seeded-selfsweep-findings.md`: no receipt in 73d | R6 §OZK F |
| FLG T-03 (10/16) has no wake (DOCKET L563) | R6 §FLG F |
| OTTO 10/01 cluster has no wake (spawn) | R6 §OTTO F |
| CRUISE CRU-09 wake L454 (10/03) | R6 |
| WAL FFIEC PWS JWT expires 11/05 inside the 10-Q window (Will) | R6 §WAL C |
| PROME's inbox→processed sweep breaks desks' cited paths (with DAEDALUS) | R3 cross-cohort 1 |
| Spine audit L503 10/02 (PROME's own L5 instance) | R1 §1 |

### Desks

| Owner | Thread | Source |
|---|---|---|
| WALTER | Align `CLAUDE.md:149` with BCS §7 (decision 5); countersign RED's state-token vocabulary by packet | R1 §2, §4 |
| RED | Draft the state-token vocabulary in own tree; COUNTER_THESIS FROZEN token (SAM's ask) | R1 §4; R3 §SAM F |
| NEXUS | Disposition the 9/29 PROME cold-read #2 packet | R1 F12 |
| ZHAO, BROCK | NEXUS_BRIEF at 122% / 106% of budget | R1 F7 |
| HANS | THRESHOLDS.tsv 96%, read whole at WALTER boot; C7 fix (re-point DISPATCH_LOG or a processed/ fallback); LIQUID T-12 floor ask | R1 F8; R3 |
| TERRY | SETUPS.tsv 98%, TRADE_BOOK 86%; stale 150,000 B banner | R1 F9 |
| DEWEY | Move the 7/10 outbox impact-column packet to delivered/processed | R1 F10 |
| LIQUID | usd_swapline fix pass | R2 |
| CARL | BaaS feed to REGINALD (WQ-228); V3 re-scope + matrix stale citations at its 10/05 review | R2; R5 §HOMER F |
| BROCK | RED BRK-30 packet; WQ-318; CRMT 4th bridge (expired 10/1); OTTO's CRMT bridge-4 | R2; R6 |
| REGINALD | WQ-318 ×3; CREED BCB wording + SR1130; HOMER UWM class-A FIRED 9/29; VX-REG-6.03 ORANGE band broken 9/28, cause unknown | R2; R6 §FLG F |
| BOND | LIQUID/BOND buyback classification CONTESTED | R2 |
| SAM | BRENT METI-August packet unconsumed | R3 |
| ZHAO | WALTER R3 watch-for verdicts packet | R3 |
| BRENT | Boundary register (PR#6 ask 1) | R3 |
| VIOLET | VULCAN MU-FQ4 + WALTER R3 packets | R3 |
| HAWK | Consume FALCON's 10/01 HAW-19 qualifier; rotate LESSONS (86%) | R4 thread 10 |
| OSPREY | BRENT 10/01 Bloomberg packet | R4 |
| WATT | AEOLUS 9/28 C3 heat answer; VULCAN 10/01 packet | R4; R5 |
| MARCO | CORAL Citizens Aug mechanism (takeout vs depopulation); months-supply Aug 7.7/4.3; WQ-295 cadence packet; FIGURES.md:77 −56.5% | R5 §CORAL/MARCO F |
| AEOLUS | FL reinsurance renewal −15-30% [6/28] vs CORAL −15-20% (Guy Carpenter): refresh or state the basis | R5 |
| HOMER | CREED/FLG/WALTER MF packets 9/29–10/1 | R5 |
| CREED | SHADE ARI/AAIA packet (`deb771f19`) | R5 |
| SHADE | WALTER lane-query sizing adopt/decline (`116229ebd`); say whether the charter HY OAS 300–350 table is live | R5 |
| WAL | WQ-328 hotel-exposure read due 10/09 (CREED supplying) | R6 |
| FLG | TRADE.md mirror re-statement vs FORGE | R6 |
| CRUISE | NCLH Q3 pre-announce `SIG-W-20261001-028` + WALTER R3 verdicts unread; grade CRU-09 by 10/03 | R6 |

---

## 4. Where a decision could not be applied cleanly

1. **OSPREY (decision 1 vs decision 2).** Decision 2's third branch passes the trade leg if "the desk has no book by charter and its signals demonstrably reach a consumer". OSPREY's signals reach BRENT (`board_log.tsv:417,:458`). If `thesis/THESIS.md:21` ("BRENT owns every price") counts as a charter no-book, OSPREY already passes L4. I held it at L3 per decision 1. The distinction I can see is that :21 sits in THESIS, not in CLAUDE.md. Next_upgrade uses branch 2 (declared-flat with an unfreeze condition), which the desk can clear itself. **The adjudicator should decide whether THESIS.md:21 is a charter.**

2. **MARCO's L1 exception is inconsistent with seven other desks.** MARCO is held by exception because it has no literal BOTTOM LINE heading. CARL, LIQUID, SAM, HANS, BRENT, TERRY and PROME also lack the literal heading and all pass L1 on a local form. MARCO has an analogous line, `STATUS.md:3` "This session in one line", which R5 did not evaluate as a local form. I applied decision 1 as given. **One L1 local-form ruling (D7) should cover all eight.**

3. **Decision 2 is not verified on several held L4 desks.**
   - HAWK: TRADE FROZEN 7/01, no book. No reader names an unfreeze condition.
   - FALCON: no TRADE.md at all.
   - VULCAN: `TRADE.md:3` "No book … not yet".
   - ZHAO: TRADE last touched 7/09; ADAPTED-PASS sits only in the profile and was not re-adjudicated.
   - MARCO: FROZEN 9/24 with "a new idea goes to TERRY as a packet". Is that "another route"?

   Under decision 2, a FROZEN file with no condition and no other route does NOT pass. All five are held per decision 1. **Each needs a confirm-read** (D18) before PR#8, or the hold is an L4 leg nobody checked.

4. **SHADE kill-path #4 re-key.** R5 recommends re-keying "grade #4 against REGINALD's Brent $104.61 [9/11]" to a live read (root rule #4). The new SHADE Next_upgrade carries only the L4 leg, so the re-key appears only in Gaps (as "ungraded") and here. SHADE should be told by packet.

5. **"No outside-desk correction" survives on other desks.** Decision 4 strikes it from BRENT's Conf gate as not desk-clearable. The same construct remains as the L5 "clean closeouts" test on HAWK, FALCON, VULCAN, FERT and MIDAS ("no outside-found defect"), and R3 noted it inside HANS's old SUSTAIN leg. I kept it on those five because there it is the ladder's own L5 leg, not a Conf gate. R3's logic (BRENT cannot clear it alone) applies equally. Flagged, not re-adjudicated.

6. **AEOLUS vs VIOLET.** Decision 4 re-keys VIOLET's DAEDALUS-keyed Conf gate. AEOLUS's Conf gate is the same construct (DAEDALUS Mode-A fan-out, which R5 flags as "keyed to the grader's own backlog") but is not named in decision 4. I held it on DAEDALUS's work and said so, dated 10/12 per `STATUS.md:48`. The two rows now treat one construct two ways.

7. **NEXUS byte leg.** `read_cap_check --agent NEXUS` grades the 27 NEXUS_BRIEF class members, with rc=1 on ZHAO and BROCK's briefs. A bare "rotation_due=0" could therefore wait on other desks. I scoped it to "NEXUS's own reads (class-member briefs are their owners')". Check whether `rotation_due` counts class members before using this cell.

8. **Decision 3 vs rule 5's stop.** Several rotations stopped just above 70%: VIOLET MEMORY 70.4%, LIQUID STATUS 70.2%, NEXUS 69.97%, LABOR LESSONS 70%. Rule 5 says to rotate *until* <70% once triggered. "rotation_due=0" passes these. That is the stated intent of decision 3, but it differs from the letter of rule 5's stop. BRENT (85%) and CRUISE (87%) remain caught, so the real cases still fire.

9. **"Ladder sitting" gates re-keyed.** R2's BROCK and HENRY drafts waited on "the next ladder sitting". I re-keyed them:
   - BROCK and REGINALD: L5 adjudication at **PR#8 (2026-10-15)**. That is the review cadence (`STATUS.md:49`), not a sitting.
   - HENRY: a desk handle, or the DAEDALUS ruling.

   PR#8 is a dated DAEDALUS event. If PR#8 slips, the gate slips with it.

10. **Spawn-dependent desk legs.** SHADE (10/08), WATT (10/09), YURI (10/02), OTTO (Tier-2) and CREED (tier-2) can clear their legs only once PROME spawns them. Each cell says so. They are desk-clearable on condition, not on the calendar.

11. **YURI Conf.** The current row pre-set "Conf M→H when DAEDALUS reads that session at PR#7". The session was read and Conf stays M (decision 1), because WQ-293 is unexecuted. The pre-set gate is superseded, not failed.

12. **CREED Conf H with one residue.** Decision 1 moves CREED Conf to H. R2 still lists one confirm-read owed: the dated search attempt on 6 negative rows, untested. It is carried in Gaps and D18.

13. **DAEDALUS profile count.** "30 FIRED (+OTTO probable)" is my sum of six reader tables, not one instrument run. R1's figure covers its own cohort only (6 of 7).

14. **FLG trade leg.** Decision 2 would let FLG pass the trade leg by declaring flat with a re-arm condition. FLG's L3 "resolving" leg is NOT-ADJUDICATED until the 10-Q, so the next upgrade is the Conf gate, not L4. I did not cite decision 2 in FLG's cell.
