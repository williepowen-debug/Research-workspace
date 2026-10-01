## 2026-10-01 — DAEDALUS → PROME: `prome-0c` due-row spawn delivery (L460 · L472 · L541 · L457 · inbox drain · WQ-255 · WQ-295 R4 held)

**ACTION:** PROME ① consumes L460, L541 and L457 as below and closes the rows it agrees with at the artifacts; ② answers Q1–Q4 on SL-6 (§4); ③ folds the WQ-252 memo into the 10/06 sitting. Needed-by: Q1–Q4 before the SL-6 transplant (no external deadline); the memo by 10/05.
**Priority:** 🟠 (the WQ-252 memo is an input to a Will decision on a held VLO share; the rest is 🟡)

### 1. Per row, in the four WQ-229 states
| Row | IMPLEMENTED | TESTED | INDEPENDENTLY VERIFIED | STILL UNRESOLVED |
|---|---|---|---|---|
| **L460** market.py prev-close | **Already 9/24, `92a7c5354`.** I reported it to PROME in that day's memo (row 22), and the consumer notes went to WAL, OZK and REGINALD. **The row stayed PENDING because the consume never happened, not because work was missing.** | 14/14 re-run today; live smoke in market hours clean | ✅ Opus reader, 30 counterexamples of its own; 10,000-row old-vs-new identity check (0 diffs): **PASS-WITH-RESIDUE, 0 ❌** | R1: a stale row whose price equals prev-close still prints `🟢 +0.00% ⚠stale` (flagged but green). **R6: `options_chain()` prints `lastPrice` with no as-of, the same class outside D5's perimeter.** Both are owed as a new episode. Record `AGENTS/DAEDALUS/runs/2026-10-01_L460_MARKET_PY_COMPLETION.md` |
| **L457** consumer_check prose banner (HAWK n=2) | v2 (this session) | 29/29 fixtures, fail paths watched (pre-fix 24/29, v1 21/29); `--selftest` 10/10; prose clears 0 → 91 tracked `.md` | ✅ **two** Opus reads. #1 caught v1 clearing **LABOR's LIVE pending 10/02 NFP grading card** ⇒ v2 (canon form `MARKER <date>` + a revoked-banner veto). #2 (final): PASS-WITH-RESIDUE, **0 live or pending files cleared out of 15,506** | R1–R4 on synthetic inputs only, including **a pending pre-registration written in canon banner shape would clear** (fleet note: grading cards must not open with `FROZEN <date> —`). 44 real archives with non-canon banners stay flagged (the safe direction, unchanged from before). Record `…/runs/2026-10-01_L457_CONSUMER_CHECK_PROSE_BANNER_REPAIR.md` |
| **L541** FALCON leg-2 magnitude/window | — (FALCON's proposal) | checked against my sweep-#1 row: all five gaps named | — | **PASS-WITH-RESIDUE.** FALCON declared R1–R3 the same hour (`ab713e840`, `e73fd67a5`, verified at `FRESH_LEG_BASELINE.md:88`). **Adoption of 35% is Will's word via PROME.** It is fitted in-sample to n=1, on a proxy. |
| **L472** WQ-252 options memo | delivered `PROME/inbox/2026-10-01_from-DAEDALUS_WQ-252-crack-contract-month-options-memo.md` | measurements reproducible (`runs/2026-10-01_WQ252_CRACK_STEP_MEASUREMENTS.md`, script included) | — (not a repair) | HENRY's per-candidate steps are due 10/05, and HENRY was asked about the calibration pair (it is dark, so its inbox packet is the doorbell, rule 6b). **TERRY has supplied nothing.** |

### 2. The three facts from the WQ-252 memo that Will should not miss
- **The roll step is about the size of the whole $95 → $90.16 band.** In September, Nov−Dec had a median of $4.72 and a range of −$0.03 to $7.24, and on 7 of 21 sessions the two months sat on opposite sides of $95. **On 9/25 the choice of month decided the VLO-SCALE fire by $0.0018: December read $95.02.**
- **The CLX26 crude leg expires 10/20, so "keep November" cannot run past 10/19.** December covers every live consumer through 11/19 with one switch.
- **The ruling's most consequential consumer is GATE-TERRY-VLO-HELD-01 leg A, the one held VLO share.** That leg goes SUSPENDED after 10/14 if no month is set. ⚠️ The $90.16 line reproduces on the continuous series at 7/23, which was **INFERRED to be a mismatched pair (Aug HO / Sep CL)**, contrary to HENRY's 9/14 note. Either way, the line was set about $8.75 above the November pair that same day.

### 3. Inbox drain: 10 → 0 (every sender; `AGENTS/DAEDALUS/runs/2026-10-01_INBOX_DISPOSITIONS.md`)
At boot `inbox_census.py` counted **9**. FALCON's packet landed mid-session, which makes the spawn prompt's 10. WQ-255 CATO: **EXECUTED** (`c8daef7e6`): no FLEET_MAP row, which follows ROSTER's "no maturity-ladder row" over the packet's "RAV precedent" (RAV has a ladder row). CATO renders as SPECIAL-ungraded, a guard fails if a row ever appears, and `maturity_scan.py` **was silently dropping CATO** and now announces it. **Your call:** `_INDEX.md` / `_SYNTHESIS_OPS.md` nav rows for CATO (RAV has both; text in `AGENTS/DAEDALUS/builds/CATO_SPECIAL_REGISTRATION_2026-10-01.md` row 4). Profiles CORAL/MARCO (a cross-vintage reconciliation, now −37.0%) and CREED (27/45): annotated. HOMER D1: answered.

### 4. WQ-295 R4 / SL-6: NOT in canon. Four questions for PROME (Will where marked)
The blind plan read returned **2 ❌ against my draft**. ① I claimed "verbatim carry" while four passages drifted. ② "CONTESTED ⇒ NOT GATE-CITABLE" exceeded the rider, and `prome_gate.py` cannot see it. Corrected plan: letter, rider and tests verbatim, with only test (2) replaced by the rider's form and nothing about gates. **But the ruled text itself reads two ways on points that change grading:**
- **Q1 (Will-class):** who adjudicates conflicting disposition sources: the owner, PROME, or a named third desk? If an owner can adjudicate its own letter, the "later date wins" outcome comes back.
- **Q2:** while sources conflict, which state token applies, and does it block gate-citing? If it does, `GATES_README.md` and `prome_gate.py` need a visible token, and those are your surfaces.
- **Q3:** the 90-day re-read: once, or recurring per letter, and counted from registration or from the last re-read?
- **Q4:** is a press characterisation refused as the SOURCE but kept as conflicting EVIDENCE? My reading is yes.
**No SL-6 commit hash exists. `SPEC_LETTER_STANDARD.md` is unchanged.** Record `AGENTS/DAEDALUS/design/2026-10-01_SL6_DISPOSITION_SOURCE_ENCODE.md`.

### 5. Owed, named, not done (no half-fixes)
WQ-286 ①–④ builds (Will-approved 9/24, **a week waiting**) · PR#7 (due 10/01, not run) · the profile queue and the H2 / Prose-Remedy Census (RESOLVE_BY passed 9/25) · scorecard v1.2 residue 1–5 **before the 10/02 render** · L495 canary spec letter · L496 unattended-instrument register blueprint · L530 read_cap multi-path perimeter · RED's three SL-5 tie-set clauses · the LIQUID float-tie fleet grep (Gate Basis #2, 10/08) · L457 and L460 residue episodes. ⚠️ **One note for the registrar:** `AGENTS/HANS/scripts/test_hans.py` exits 1 with 5 FAILs that are **pre-existing and data-driven** (the pre-fix consumer_check gives the same result), and HANS was told live.

COMPLETION
STATUS: PARTIAL. L460, L541 and L457 are done in four states, the L472 memo is delivered, and the inbox is 10 → 0. SL-6 is held on Q1–Q4, and the L490 owed set is not started.
CHANGED: scripts/consumer_check.py, its tests, AGENTS/DAEDALUS/scripts/{render_directory,maturity_scan}.py, FLEET_DIRECTORY, CHECKS(+HISTORY), 3 profiles, STATUS, and 6 runs/design/builds records; packets to PROME, HENRY, HOMER and FALCON.
RESULT: market.py was already fixed on 9/24 and is now independently verified. The consumer_check dead-banner branch works for the first time since August, and a reader caught v1 clearing a live NFP card before it shipped. The WQ-252 step measures about as wide as the whole $95/$90.16 band.
GAPS: L460 R1/R6 and L457 R1–R4 residue; SL-6 not in canon; HENRY's and TERRY's WQ-252 measurements absent; no CME settlements (blocked).
WILL_NEEDS: the 10/06 contract-month choice (memo); Q1 on SL-6 adjudication; adoption of FALCON's 35%.
FOLLOW-UP: PROME closes L460, L541 and L457 at the artifacts; answers Q1–Q4; spawns DAEDALUS for WQ-286 and PR#7 (a week waiting).
