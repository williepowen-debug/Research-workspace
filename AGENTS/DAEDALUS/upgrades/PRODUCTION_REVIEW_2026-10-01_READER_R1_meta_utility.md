# PRODUCTION REVIEW #7 — READER R1 (meta/utility) — 2026-10-01

**Cohort:** PROME · WALTER · NEXUS · RED · TERRY · ORACLE · DEWEY · RAV · DAEDALUS (CATO skipped: ungraded by ruling).
**Period:** 2026-09-17 → 2026-10-01 · baseline `e9ac693af` · HEAD at read = `953ef4dda` (+ later 10/01 commits seen in `git log`).
**Method:** read-only. FLEET_MAP rows, STATUS, `git log` per tree, profile headers, and these instruments RUN at HEAD: `scripts/read_cap_check.py --agent <X>` (all 7 desks with a STATUS), `AGENTS/DAEDALUS/scripts/sweeps_due.py`, `AGENTS/DAEDALUS/scripts/maturity_scan.py`, `AGENTS/RED/scripts/review_debt.py`, `AGENTS/TERRY/scripts/ledger_sweep.py` (run from the repo root). Byte figures are `wc -c` at read time.
**Conf key:** H = read-verified · M = read plus mechanical checks. **"confirm-read owed"** = I did not read enough to firm the grade.

## Period activity (path commits / subject-prefixed commits / STATUS bytes)

| Agent | Path commits | Own-subject | STATUS B (% of 32,550) | Profile last touched | Profile trigger |
|---|---|---|---|---|---|
| PROME | 1300 | 981 | 20,728 (64%) | 2026-09-08 | **FIRED** |
| WALTER | 317 | 244 | 10,874 (33%) | 2026-08-26 | **FIRED** |
| NEXUS | 45 | 29 | 22,776 (69.97%) | 2026-09-03 | **FIRED** |
| RED | 40 | 25 | 24,148 (74%) | 2026-09-08 | **FIRED** (5 legs) |
| TERRY | 99 | 86 | 21,628 (66%) | 2026-09-05 | **FIRED** (clock 9/26) |
| ORACLE | 30 | 25 | 16,019 (49%) | 2026-09-05 | NOT FIRED (clock 10/20) |
| DEWEY | 26 | 17 | none, by design | 2026-09-01 | **FIRED** (still unserviced) |
| RAV | 0 | 0 | none, by design | no profile | N-A |
| DAEDALUS | 120 | 67 | 24,235 (74%) | no profile | N-A (profile absent) |

**Headline:** 6 of the 7 cohort profiles that exist have FIRED and none was serviced in the period. The DAEDALUS profile queue's RESOLVE_BY date of 2026-09-25 has passed (`sweeps_due.py`: "6d past").

---

## 1. PROME — Meta L4 / M (scored 9/17)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| Five 9/8 findings repaired/receipted | TRUE (history; does not belong in Gaps) | `0ab1e8e51`, `2a8d49ca2` |
| L5 gate = zero own-rule-unexecuted at the judgment sweep | TRUE (the gate stands) | `upgrades/PROME_SWEEP_2026-09-08.md:32` |
| The instance: SCRATCH 26,535 B (82%) and ACTIVE_DECISIONS 25,046 B (77%) unrotated | **OVERTAKEN** | SCRATCH now 24,315 B (74.7%, below the 75% trigger); ACTIVE_DECISIONS 22,568 B (69.3%, under the STOP); `read_cap_check --agent PROME` gives rc 0, rotation_due=0 |
| HEARTBEAT 21,070 B (65%) | OVERTAKEN | 22,647 B (69.6%), after the 25th re-base `c0642a8f6` 10/01 |
| ARGUS wired at CLOSEOUT:79 | TRUE | `PROME/CLOSEOUT.md:79` |
| Next: rotate SCRATCH/AD under 22,785 B | PARTIAL | AD met; SCRATCH is 1,530 B over the STOP but not at its trigger, so rule 5 owes nothing today |
| Profile leg "prome_gate check-family ≠ 22" is unevaluable | TRUE-STILL | `grep -c 'def check_'` now returns **18** (was 15); the counting rule is still unstated |

**New own-rule-unexecuted instance (the L5 gate fails on it):** `PROME/STATUS.md:3` reads "Last spine audit 2026-09-20 … **PAST CADENCE from 2026-09-27**". It is disclosed and registered as DOCKET L503 for 10/02, but it is unexecuted against PROME's own >7d rule.

**B. Ladder walk**
| Leg | Verdict | Locator |
|---|---|---|
| L1 STATUS + BOTTOM LINE | PASS in local form only | `grep -c -i 'bottom line' PROME/STATUS.md` = 0, and `git log -S` shows the file **never** carried one. The local form is the `Updated:` header plus SCRATCH ★ NEXT. Flag for a ladder ruling, not a downgrade. |
| L2 structured record | PASS | GATES.tsv, DOCKET.tsv, READS.tsv, ORCH_LOG accruing |
| L3 conformance checks run, FLEET_MAP current | PASS | prome_gate, read_cap rc 0, ARGUS every Standard+ closeout |
| L4 builds/retirements clean, PATTERNS accruing | PASS | 1300 path commits; WQ rulings executed (e.g. `be8b72644`) |
| L5 (as L4 + zero own-rule-unexecuted) | **FAIL** | spine audit past cadence (`STATUS.md:3`) |

**C. Reachability:** the L5 gate is adjudicated only at the DAEDALUS PROME judgment sweep, which is **DUE +2d** (`sweeps_due.py`: last run 23d ago, cadence 21d). PROME clears the instance in its own tree (L503, 10/02). The verdict, though, needs DAEDALUS's sweep, so the gate's firing is keyed to another desk.
**D. Profile:** **FIRED**. The "HEARTBEAT re-base #1" leg fired long ago (re-base #25 is `c0642a8f6`), and BOOT/CLOSEOUT were touched by 8 commits in the period (e.g. `e48219926` 9/30). The body is still 9/03.
**E. Proposed row:** **L4 · M**, unchanged.
- **Gaps:** "L5 gate (zero own-rule-unexecuted, PROME_SWEEP_2026-09-08:32) FAILS today on the spine audit, past its >7d cadence since 9/27 (STATUS.md:3; sitting DOCKET L503 10/02). SCRATCH 24,315 B (74.7%) and ACTIVE_DECISIONS 22,568 B (69.3%) are not in rotate tier. STATUS carries no literal BOTTOM LINE (local form = Updated header). Profile FIRED (re-base #25), body 9/03."
- **Next_upgrade:** "L5 at the next DAEDALUS PROME judgment sweep (DUE now) IF L503's spine audit has run and no other own-rule instance is found."

**F. Cross-agent:** see §F at the foot (ROSTER CATO contradiction; WALTER push-binding never registered as a WQ row).

---

## 2. WALTER — Utility L4 / H (scored 9/24)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| WQ-254 D4 first prune done, 25 rows | TRUE (history) | `ab549b79f` |
| "D4 edit built 9/24, reader pending" | **OVERTAKEN** | DAEDALUS `STATUS.md:37`: "D4 FIXED 9/24 on the independent read's verdict, WQ-229" |
| Blocker (a): two contradictory push bindings | **TRUE-STILL** | `AGENTS/WALTER/CLAUDE.md:149` ("closeout auto-push via safe-push.sh") vs `design/BOARD_CONSUMPTION_SPEC.md:87` ("Push is **not** automatic blanket WALTER authority") and `:504` ("pushing is Will-coordinated") |
| "needs Will's word / route it" | **NEVER ROUTED** | No WQ row: `grep -i 'binding'` in `PROME/WILL_QUEUE.md` plus the 9/26 rolloff archive finds nothing on push. ⚠️ Root `CLAUDE.md:84` (Will-gated canon) already names "WALTER (per BCS §7)" as the auto-push exception, so canon arguably **has** ruled for BCS §7, and the fix may be a desk-side charter alignment rather than a new ruling. |
| (b) 7 of 8 two-binding instances UNVERIFIED (DAEDALUS-owed) | TRUE-STILL | no DAEDALUS artifact in the period (`grep -rli two-binding AGENTS/DAEDALUS` turns up only old files) |
| Profile cites BCS v0.20; refresh to "v0.31" | **REFUTED as written** | BCS is **v0.32** (`BCS:3`), bumped 9/17 by `d35d91948`, so the 9/24 cell was a version behind on the day it was written |
| CLAUDE.md 63,141 B above the 54,250 B harness cap | **REFUTED as a cap breach** | READ_CAP rule 20 (ruled 9/19, `390e6a252`) says the charter is not bound by the read cap (context cost, not truncation). `read_cap_check --agent WALTER`: "charter 65,503 B — OUT OF PERIMETER by rule 20". Growth is real: 63,141 → 65,503 B. |

**B. Ladder walk:** L1 PASS (`STATUS.md:5` BOTTOM LINE) · L2 PASS (BOARD 1148, registry ledgers) · L3 PASS (walter_doctor, BCS) · L4 PASS (107/107 handoffs on origin, `0b2e47fb4`; delivery_log reconciled after each push, e.g. `297c9ffe2`) · **L5 FAIL** on one conformance defect: the charter's push step contradicts its own spec. Closeouts are otherwise clean and current (10/01 walter-c3).
**C. Reachability:** the L5 leg as worded ("Will's one-line ruling") **cannot fire**, because no question was ever registered. Two reachable paths: (i) WALTER aligns `CLAUDE.md:149` to BCS §3.4/§7, citing root `CLAUDE.md:84` (desk-side, its own tree); or (ii) PROME registers a WQ row. The self-cap leg is keyed to a rule that does not bind (rule 20), so strike it.
**D. Profile:** **FIRED** on P1 (period path commits alone = 317, more than 300) and P2 (BCS v0.32 ≠ v0.20). The body is 8/26.
**E. Proposed row:** **L4 · H**, unchanged.
- **Gaps:** "Charter step 16 (CLAUDE.md:149, closeout auto-push) contradicts BCS v0.32 §3.4 (:87, FLASH-only clean-tree push) and §7 (:502–504, Will-coordinated); root CLAUDE.md:84 names WALTER's exception 'per BCS §7'. No WQ row exists for it. 7 of 8 two-binding instances unverified (DAEDALUS-owed). Profile FIRED (P1/P2), body 8/26, cites BCS v0.20."
- **Next_upgrade:** "L5 when CLAUDE.md:149 states the BCS §7 push binding (desk edit citing root :84) or a registered WQ ruling replaces it. Whichever lands first; not dated."

---

## 3. NEXUS — Utility L5 / M (scored 9/24)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| STATUS 31,508 B (97%), PREDICTIONS_MONITOR 29,065 B (89%) | **OVERTAKEN** | rotated 9/29 (`0e9ebf96d`) and 10/01 (`f61df31de`, H13). Now STATUS **22,776 B** (9 B under the STOP) and PM **12,259 B** (38%) |
| CLASS-row declaration owed: `AGENTS/*/NEXUS_BRIEF.md` whole | **DISCHARGED** | `PROME/registry/READS.tsv:289` (declared 9/24, re-attested 9/29, `69ff25637`) plus attestation `:311` |
| Five briefs 2.2–4.2× budget | **OVERTAKEN** | `read_cap_check --agent NEXUS` (27 members) now shows **ZHAO 39,556 B (122%)** and **BROCK 34,568 B (106%)** over budget, none over the cap. VULCAN, HOMER, LABOR, BOND and MIDAS are no longer over. rc=1 is on others' briefs. |
| 13 consumed outcomes not enumerated | **UNEVALUABLE: the referent is gone** | `grep -rn "13 consumed\|13 outcomes consumed" AGENTS/NEXUS` = 0 hits (also 0 at PR#6, `PRODUCTION_REVIEW_2026-09-17_READER_R1:378`) |
| No AUTHORITY & SAFETY block | **TRUE-STILL** | `grep -n -i authority AGENTS/NEXUS/CLAUDE.md`: one hit (:54, a DAEDALUS citation). The section list (`## IDENTITY … ## ANTI-PATTERNS`) has no permission/safety block; `## WHAT YOU OWN` (:256) is ownership, not authority. |
| Re-date PRED-38/40/45 | **DONE** | PRED-38 re-spec'd 10/1 (resolver 11/10), PRED-45 re-registered for 11/20 (`PREDICTIONS_MONITOR.md:4,:12,:38,:40`). PRED-40 is out of the ACTIVE table. |
| "Flag if the next pass slips rotation again" | NOT TRIGGERED | the 9/29 pass reached the STOP (68% / 32%) |

**B. Ladder walk:** L1 PASS (BOTTOM LINE) · L2 PASS · L3 PASS (convergence matrix, falsifier rule J) · L4 PASS (`CLAUDE.md:20` CONTRACT; PROME WQ-340 consumed, `a9e813b6a`→`b62218340` per `CLAUDE.md` CONTRACT) · L5 PASS: 10/01 closeout current, charter cold-read fixes 9/29 (14/14 ❌ fixed, `8295b710f`). Note the 5-day dark spell 9/24→9/29 (`83e6fe366` "after 5 days dark"). Residue: `inbox/2026-09-29_from-PROME_charter-cold-read-2-…VERIFIED.md` is still in the inbox root at HEAD.
**C. Reachability (Conf M→H gate):** leg 1 (STATUS < 22,785 B with PM out of rotate tier) is **MET today**, with a 9 B margin. Leg 2 (13 consumed outcomes) **cannot be cleared**, because its referent no longer exists in the tree; strike it. Leg 3 (AUTHORITY block) is desk-reachable in its own tree.
**D. Profile:** **FIRED**: STATUS dropped below 24,412 B (rotation landed 9/29), and the day clock passed 9/24. The ACTIVE-count leg (≠9) shows 5 `| PRED-` rows; ACTIVE semantics not confirmed. The body is still 9/03.
**E. Proposed row:** **L5 · M**, unchanged (the gate is not met).
- **Gaps:** "No AUTHORITY & SAFETY block in CLAUDE.md (section list :8–:352). STATUS 22,776 B sits 9 B under the rule-5 STOP; PREDICTIONS_MONITOR 12,259 B (38%). NEXUS_BRIEF CLASS row declared (READS.tsv:289); its over-budget members are ZHAO 122% and BROCK 106% (owners'). 1 inbox-root packet undispositioned (9/29 cold read #2). Charter 69,519 B (rule 20: not cap-bound). Profile FIRED, body 9/03."
- **Next_upgrade:** "Conf M→H when an AUTHORITY & SAFETY block lands in CLAUDE.md with STATUS still under 22,785 B at that commit. (The '13 consumed outcomes' leg is retired: its referent has 0 hits in-tree.)"

---

## 4. RED — Utility L5 / M (scored 9/17)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| L341 VX re-review discharged | TRUE (history) | `4b100ff85` |
| D1 RED/WALTER state-token reconciliation: no joint artifact | **TRUE-STILL** | `grep -rli 'state.token'` over both trees: no joint file. RED `MAINTENANCE.md:53` lists it as owed. |
| FALSIFICATION_TRIGGERS carries 4 negative-class rows | TRUE (by content; there is no class column) | FT-08, -10, -11 and -12 carry the publisher/unit/tie/precondition elements (`registry/FALSIFICATION_TRIGGERS.tsv`, 19 columns) |
| CANDIDATE: VX banner "9 of 17 CARRIED" vs `grep -c CARRIED` = 11 | **OVERTAKEN** | the banner was re-cut at S46 9/18 (`037aabc6b`) to ">45d debt 6/17 → 1/17" and names `review_debt.py` |
| Next: re-derive with `review_debt.py` | DONE by the banner; the figure has since aged | `review_debt.py` at 10/01: **③ VX 7 of 17 live >45d**, **① KB 25 ACTIVE rows past Stale_By**, **② 13 terminal rows still cited**, **32 reviews owed** |

**B. Ladder walk:** L1 PASS · L2 PASS (ML to ML-RED-273) · L3 PASS (steelman/red-team rubric: LIQ-07 z-leg concession ML-RED-272 `ad28f8ffd`) · L4 PASS (CARL adopted DR-3 red team `bed4eb6fa`; LIQUID answered `ac3c92f3c`) · L5 PASS (S49 full closeout `48c610e00`, S50b `953ef4dda` 10/01; `read_cap_check` rc 0).
**C. Reachability:** the Conf M→H leg needs **both desks in one joint session**. Neither desk can clear it alone; it has stood unreached across two reviews (PR#6 to PR#7). Re-key it so it can be cleared: RED writes its token vocabulary in its own tree, and WALTER countersigns by packet.
**D. Profile:** **FIRED on every content leg**: ML max ML-RED-273 > 213 · header 19 columns > 18 · CHG-RED-052 present · CARRIED count 11 ≠ 9 · clock 9/24 passed. The body is 9/03 (targeted note 9/08).
**E. Proposed row:** **L5 · M**, unchanged.
- **Gaps:** "No joint RED/WALTER state-token artifact in either tree (MAINTENANCE.md:53 owed). review_debt.py 10/01: 32 reviews owed, made up of 25 KB rows past Stale_By, 13 terminal-but-cited, and 7 of 17 live VX >45d. VX header two-clock stays at 2026-06-02 by design. STATUS 24,148 B (74%, 264 B under the rotate trigger). Profile FIRED on all legs, body 9/03."
- **Next_upgrade:** "Conf M→H when RED's state-token vocabulary is written in its own tree AND WALTER's countersign packet is committed. Not dated: two-desk leg, one desk drafts."

---

## 5. TERRY — Utility L5 / H (scored 9/24)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| GATE-TERRY-007 MOOT, ROLL70 (a)–(d) written | TRUE (history) | `04c5c7aad` |
| "(d) REGINALD's concurrence asked" | UNVERIFIABLE (no concurrence row found by grep) | not in `AGENTS/REGINALD/STATUS.md` |
| STATUS 32,526 B = 100% | **OVERTAKEN** | rotated `cef85d580` (79% → 63%), now 21,628 B (66%) |
| Drain (section I) non-empty, not re-measured | **OVERTAKEN, 1 of 2** | `ledger_sweep.py` at HEAD: "I. … 0 undrained"; "✅ CLEAN (A–H)". The prior cycle was not measured. |
| Cite STATUS by heading | TRUE (practice) | — |

**New TRUE-NOW items:** `read_cap_check --agent TERRY` shows rotation_due=2, with **SETUPS.tsv 31,842 B (98%)** and **TRADE_BOOK.md 27,895 B (86%)**, both boot-read (CLAUDE.md boot line 155). `STATUS.md:3` still declares a "BYTE BUDGET 150,000 B" self-cap that the 32,550 B canon overrides (a stale header). A ⛔ SUPERSEDED 9/22 block (`:8`) sits above ★ CURRENT STATE (`:12`). `maturity_scan` reads TERRY at floor L2 with "no BOTTOM LINE". The local form is ★ CURRENT STATE, so this is a scan naming miss, not a gap.

**B. Ladder walk:** L1 PASS (local form) · L2 PASS · L3 PASS (ledger_sweep A–H clean) · L4 PASS (PROME WQ-347 consumes the card; 9/30 expiry grades `ee04fbb26`) · L5 PASS: three 10/01 closeouts, inbox 0.
**C. Reachability:** SUSTAIN is reachable; one more clean closeout with section I empty makes 2 of 2.
**D. Profile:** **FIRED** (21d clock 9/26 passed; body 9/05).
**E. Proposed row:** **L5 · H**, unchanged.
- **Gaps:** "Boot reads SETUPS.tsv 31,842 B (98%) and TRADE_BOOK.md 27,895 B (86%) are in rotate tier. STATUS.md:3 declares a 150,000 B self-budget that canon overrides (32,550 B). A superseded 9/22 block sits above CURRENT STATE. Drain: section I = 0 at the 10/01 HEAD, prior cycle unmeasured. Profile FIRED (clock 9/26)."
- **Next_upgrade:** "L5 SUSTAIN on the next closeout with ledger_sweep section I = 0 (2 of 2), and SETUPS.tsv and TRADE_BOOK.md under 22,785 B."

---

## 6. ORACLE — Utility L4 / H (scored 9/24)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| ORC-04 bands named the dead contract; "write the roll rule only after WQ-190 succession ruled; re-point nothing before" | **OVERTAKEN** | WQ-260 ruled 9/24 (`0289ac024`), v5 supply leg at $110 encoded (`ab5f689d9`), **v5 October roll encoded** 9/28 (`279b7aec1`). VX-ORC-04 now reads `[REGIME v5-oct26-icewti110]`. |
| `CLAUDE.md:201` downgrade trigger CANNOT-FIRE (no instrument) | **TRUE-STILL** | `CLAUDE.md:201` unchanged ("track accuracy over time") |
| ORC-09 NEH<30% leg never reachable | **TRUE-STILL** | `workbook/VX.tsv` VX-ORC-09: "NEH 81.5%", "not re-keyed here" (9/18) |
| KB-ORC-086 cite-the-MID returns 50.0 on settled markets; past surfaces not swept | PARTIAL | rule stated `STATUS.md:130`; the Polymarket settled-leg artifact was fixed in code 9/17 (`5462b6e06`). The Kalshi-side historical sweep is UNVERIFIABLE: I found no sweep artifact and did not run one. |
| L5 on calibration loop F-1 | TRUE-STILL (not built) | `SCRATCH.md:32` "DAEDALUS F-1: Brier per resolved market" owed; no calibration ledger in `workbook/` |

**B. Ladder walk:** L1 PASS · L2 PASS · L3 PASS · L4 PASS (BRENT relevance ruling `ec685ad39`; LIQUID Fed-path ask `a08929261`; ORACLE → RED correction `89363b3b7`) · **L5 FAIL**: the calibration loop is unbuilt, so the downgrade trigger cannot fire (closeouts are clean: 9/24, 9/25, 9/27, 9/28).
**C. Reachability:** F-1 is desk-reachable (all inputs are in-tree, per the row). The ORC-09 fix is desk-reachable. Building F-1 also arms `CLAUDE.md:201`.
**D. Profile:** **NOT FIRED** (clock 10/20; calibration status unchanged).
**E. Proposed row:** **L4 · H**, unchanged.
- **Gaps:** "Calibration loop F-1 (Brier per resolved market) not built (SCRATCH.md:32), so the CLAUDE.md:201 downgrade trigger cannot fire. VX-ORC-09's NEH<30% leg cannot be reached (NEH 81.5%). Kalshi settled-market 50.0-mid back-sweep: no artifact. ORC-04 is on the v5 October regime ($110 rung, 279b7aec1)."
- **Next_upgrade:** "L5 on F-1: a per-resolved-market Brier ledger (slug · resolution · outcome · p at N days prior · Brier) with its short-dated-bias limit in the header; re-key or retire ORC-09's NEH leg in the same session. Profile clock 2026-10-20."

---

## 7. DEWEY — Utility L4 / M (scored 9/01, now 30d)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| STATELESS BY DESIGN (no STATUS) | **TRUE-STILL, still by design** | `AGENTS/DEWEY/CLAUDE.md:206` ("does NOT keep a STATUS dashboard … continuous-monitor machinery that would only go stale here"; this text moved from the profile's cited :205). No CLAUDE.md commit in the period. ROSTER `:124` "stateless (INDEX.tsv only)"; `:236` ON-DEMAND. |
| maturity_scan floor reads L0 | TRUE, and a **false gap** | the scan prints `DEWEY … L0 | L0`. DEWEY is not in `maturity_scan.py:57` JUDGMENT_ONLY (RAV is). Fix lives in DAEDALUS's tree. |
| Output consumed | TRUE (strong this period) | CARL scored DR-3 (`06e9fdaae`); Nano Banc primary documents went to PROME, REGINALD, CREED, WAL and WALTER (`6a90ca732`); CARL-DR-5 (`4779531b8`); recap_pull.py helper to WAL/REGINALD (`9eae0ad80`). Output files 9/24, 9/27, 10/01. |
| No labeled CONTRACT block | **TRUE-STILL** | `grep -c CONTRACT CLAUDE.md` = 0 |
| Proposal (b) WALTER-ledger impact column "in outbox, unmoved" | **REFUTED (wrong when written 9/01)** | WALTER **shipped** it 7/24 (`PROME/inbox/processed/2026-07-24_from-WALTER_dewey-process-v2-both-items-shipped.md:17`). `DEEP_RESEARCH_FLAGGED_LOG.tsv` last column = `impact`. The outbox file is residue, not an open proposal. |
| PAT-034 fire-notification path needed | UNVERIFIABLE | not tested |

**B. Ladder walk:** L1/L2 N-A by design (INDEX.tsv is the structured record, accruing: 3 new outputs in period) · L3 PASS (cite-every-claim rubric; brief/appendix conflict rule `9b2d866df`) · L4 PASS (above) · **L5 FAIL**: no CONTRACT block. Closeouts were clean (9/24 L0 drain 13→0, 9/27, 10/01).
**C. Reachability:** the CONTRACT block is desk-reachable. The "outbox proposal dispositioned (PROME)" leg is already satisfied (shipped 7/24), so strike it.
**D. Profile:** **FIRED** (≥3 sessions; checkpoint 9/15 passed; body 8/11, banner 9/01).
**E. Proposed row:** **L4 · M**, unchanged; confirm-read owed on the 3 period outputs before Conf H.
- **Gaps:** "No labeled CONTRACT block (0 hits). Stateless by design (CLAUDE.md:206), so maturity_scan prints a false L0 (DEWEY is absent from JUDGMENT_ONLY). Impact-column proposal SHIPPED 7/24 (WALTER ledger col 13); outbox/2026-07-10 file is residue. Profile FIRED, body 8/11."
- **Next_upgrade:** "L5 on a CONTRACT block (PRODUCES / CONSUMED BY / PROOF), citing the 9/24–10/01 consumer receipts."

---

## 8. RAV — Meta L2 / M (scored 9/17)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| No §5 RUN REPORT in `AGENTS/RAV/runs/` | **TRUE-STILL** | the single file is `2026-08-05_roster-phase0-preflight-addendum.md`; §5 requires six sections (`builds/RAV_CHARTER.md:99-112`) |
| Home-dir dark | TRUE, now **57 days** | last path commit 2026-08-05. 0 commits by `rav-codex` in the period (author census: 3120 williepowen-debug, 10 Claude). No `reviews/` files after 9/15. |
| Standing sole-QC | TRUE in ROSTER text | `PROME/ROSTER.md:153` (locators drifted: :144→:145, :152→:153). ⚠️ The practice diverges: **229** subjects starting `CATO` in the period vs 0 by RAV. |
| "Two desks now grade RAV" (PROME 9/15) | **REFUTED in substance** | the review sits at **repo-root `reviews/2026-09-15_rav-maturity-and-cato.md`, not `PROME/reviews/`** (that path does not exist, so the row's locator is wrong). Its `:9` cites DAEDALUS's FLEET_MAP grade as "the recorded maturity" and `:86` disclaims grading ("does not grade RAV's underlying model"). It defers to the record and does not compete with it. |

**B. Ladder walk:** L1/L2 N-A by design (`maturity_scan` prints NOT GRADED, judgment-only) · L2 held on the review record · **L3 FAIL** (no §5 run report).
**C. Reachability:** L3 is Will-driven; no desk-side leg exists. The "settle who grades RAV" leg is **already answered by the artifact** (it defers), so strike it.
**D. Profile:** N-A (none).
**E. Proposed row:** **L2 · M**, unchanged.
- **Gaps:** "No §5 RUN REPORT in AGENTS/RAV/runs/ (one 8/05 preflight addendum). No RAV activity in the tree 8/05→10/01 (57d) and no rav-codex commit in the period. ROSTER:153 still says STANDING sole-QC while CATO (SPECIAL, ROSTER:154) carried the period's independent reviews."
- **Next_upgrade:** "L3 on the first §5 run report in AGENTS/RAV/runs/. Will-driven, no desk-side date."

---

## 9. DAEDALUS — Meta L4 / M (scored 9/24)

**A. Claims tested**
| Claim | Verdict | Locator |
|---|---|---|
| L3 "FLEET_MAP current" MET | **OVERTAKEN, now FAIL** | `sweeps_due.py`: "SELF-ROW: Last_scored 7d old (max 5d)". This PR#7 re-cut discharges it. |
| L4 builds clean: YURI wired 9/24 | **TRUE** | `2113b2734`. YURI is present in ROSTER (5), AGENTS.md, `_NETWORK`, `_INDEX`, `_ENERGY.md`, WALTER `REGISTRY.tsv`, FLEET_MAP and the directory. DAEDALUS `STATUS.md:36` lists remaining owed-by-others cells (PROME, WALTER, NEXUS). |
| L4 builds clean: CATO encoded 10/01 | **TRUE** | `c8daef7e6`. `render_directory.py` and `maturity_scan.py` both carry CATO; the scan prints "NOT GRADED … by ruling" |
| Scorecard render #4 CANNOT-RENDER | **OVERTAKEN** | rendered 9/24 (`339c5d0d1`, after PROME's ORCH_LOG repair 2) |
| Independent reader on D4 before "fixed" (WQ-229) | **OVERTAKEN / DONE** | `STATUS.md:37` "D4 FIXED 9/24 on the independent read's verdict" |
| D7 `--closure` build | TRUE-STILL (owed) | `STATUS.md:37` |
| 9/25 profile queue (AEOLUS, HAWK, HOMER, WAL, REGINALD) | **TRUE-STILL, overdue** | profiles last touched 9/01, 9/08, 9/01, **8/07**, 9/01. `sweeps_due` RESOLVE_BY 9/25 is "6d past". Re-dated to 10/12 (`STATUS.md:48`) and grown (+BROCK, CREED). |
| No `profiles/DAEDALUS.md` | **TRUE-STILL** | `ls profiles/` (53 files) has no DAEDALUS.md |
| L5 after two sweeps land inside cadence | **FAIL** | `sweeps_due`: Prose-Remedy +6d, PROME judgment tail +2d, PR +0d. RESOLVE_BY passed ×3 (profile queue, Prose-Remedy, H2 audit). WQ-286 builds Will-approved 9/24 and none landed in a week (`STATUS.md:41`). |
| Grade YUR-F01 on 10/24 | pending | not due |

**Dark window:** no DAEDALUS-authored commit 9/26–9/30 (last `7fbb44c6e` 9/25, next `251525947` 10/01), so 5 days. Inbound packets queued meanwhile (HOMER, LIQUID, CREED, CORAL, HAWK, AEOLUS, 9/26–9/29). PATTERNS accruing: PAT-181..186 (9/24, `133faa736`), none since.

**B. Ladder walk:** L1 PASS (`STATUS.md:70` BOTTOM LINE) · L2 PASS (FLEET_MAP, PATTERNS, GATE_LOG) · **L3 FAIL at boot today** (SELF-ROW 7d; PR#7 itself is the remedy) · L4 PASS (YURI, CATO; PATTERNS +6) · **L5 FAIL** (3 RESOLVE_BY passed, 3 DUE, WQ-286 a week waiting).
**C. Reachability:** a self-profile is buildable in-tree, but the PAT-050 risk is self-grading, so it needs an independent reader, as this one is. The profile queue, WQ-286, Prose-Remedy and H2 are all own-tree. The L5 condition "two sweeps inside cadence" is reachable but is not condition-keyed to a named pair; name them.
**D. Profile:** N-A (absent; the absence is itself the gap).
**E. Proposed row:** **L4 · M**, unchanged. Conf stays M: no profile, and the self-row is graded by its own subject's reader set.
- **Gaps:** "3 dated obligations past RESOLVE_BY 9/25 (profile queue incl. WAL body 8/07; Prose-Remedy Census; H2 as-made audit). WQ-286 ①–④ Will-approved 9/24, none landed. D7 --closure owed. No profiles/DAEDALUS.md. 6 of 7 cohort-R1 profiles FIRED and unserviced. maturity_scan prints a false L0 for stateless DEWEY. Dark 9/26–9/30."
- **Next_upgrade:** "L5 re-assessed when Prose-Remedy Census #1 and the PROME judgment sweep both land inside cadence AND the profile queue clears its re-dated 10/12. WQ-286 ①–④ dated 10/05 (STATUS.md:44)."

---

## F. Cross-agent threads (owner → action)

| # | Owner | Item | Locator |
|---|---|---|---|
| 1 | **PROME** (ROSTER) | ROSTER contradicts itself on CATO: `:154` "SPECIAL (Will-ruled 2026-09-26, WQ-255)" vs `:156` "Classification remains pending". This is a correction left beside the instruction it supersedes. | `PROME/ROSTER.md:154,:156` |
| 2 | **PROME** | ROSTER:153 "STANDING sole-QC" for RAV while CATO did all of the period's independent review (229 CATO-subject commits, RAV 0). Wording question for Will, not a reclassification. | `PROME/ROSTER.md:153-154` |
| 3 | **WALTER** (or PROME for a WQ row) | The push-binding contradiction was never registered as a WQ row. Root `CLAUDE.md:84` already names BCS §7, so the desk can align `CLAUDE.md:149` itself. | §2 |
| 4 | **DAEDALUS** | Fix the FLEET_MAP RAV locator: `PROME/reviews/…` should be repo-root `reviews/2026-09-15_rav-maturity-and-cato.md`. Strike the "settle who grades RAV" leg. | §8 |
| 5 | **DAEDALUS** | Add DEWEY to `maturity_scan.py` JUDGMENT_ONLY (or a stateless-by-design set); the scan prints a false L0. | `scripts/maturity_scan.py:57` |
| 6 | **DAEDALUS** | WALTER cell's "BCS v0.31" was wrong on 9/24 (v0.32 since 9/17); the self-cap leg is void under READ_CAP rule 20. | §2 |
| 7 | **ZHAO, BROCK** | NEXUS_BRIEF.md at 122% / 106% of budget (NEXUS CLASS-row members; NEXUS rc=1 on them) | `read_cap_check --agent NEXUS` |
| 8 | **HANS** | `registry/THRESHOLDS.tsv` 31,108 B (96%), read whole by WALTER:6b, in rotate tier | `read_cap_check --agent WALTER` |
| 9 | **TERRY** | SETUPS.tsv 98% and TRADE_BOOK.md 86% in rotate tier; the STATUS:3 150,000 B self-budget banner is stale | §5 |
| 10 | **DEWEY** | Move `outbox/2026-07-10_to-PROME_impact-capture-walter-ledger.md` to a delivered/processed state (shipped 7/24) | §7 |
| 11 | **RED + WALTER** | State-token reconciliation: re-key it so RED drafts in its own tree and WALTER countersigns by packet | §4 |
| 12 | **NEXUS** | Disposition the inbox-root 9/29 PROME cold-read #2 packet | `AGENTS/NEXUS/inbox/` |
| 13 | **DAEDALUS** | Profile refresh queue for this cohort: PROME, WALTER, NEXUS, RED, TERRY, DEWEY (all FIRED) | table at top |

## Grade moves proposed: none

All 9 rows hold their level and confidence. One leg moved on its own: NEXUS's M→H gate leg 1 is now met, and its leg 2 is unevaluable. Five rows carry gates that are **struck or re-keyed** because they cannot fire as written: WALTER's Will-ruling leg (never routed) and self-cap leg (rule 20); NEXUS's "13 consumed outcomes"; DEWEY's outbox-disposition leg (shipped 7/24); RAV's grade-ownership leg (the artifact defers); and RED's joint-session leg is re-keyed so it can be cleared.
