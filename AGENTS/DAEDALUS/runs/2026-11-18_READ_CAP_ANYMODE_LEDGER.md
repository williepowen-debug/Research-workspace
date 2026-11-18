# ANYMODE LEDGER: independent review of the uncommitted diff to scripts/read_cap_check.py

Reviewer: independent read-only review, 2026-11-18. Scope: `git diff -- scripts/read_cap_check.py` (+28/-8) only. No repository edits, staging or commits.
Method: working-tree file compared against `git show HEAD:scripts/read_cap_check.py` (scratch `head.py`). Both run through the scratch harness `run.py`, which execs the module with ROOT and READS_TSV re-pointed. Fixtures live in a scratch git repo `fx/` (desks KC and KD, plus a FLEET_DIRECTORY). Mutation copies are `mutant.py` and `mutant2.py`.

## Selftest

| Command | Result |
|---|---|
| `python3 scripts/read_cap_check.py --selftest` | `✅ READ-CAP SELFTEST 143/143 leg(s) pass`, rc 0 |
| Mutant 1: line 1022 reverted to `charter_mode == "explicit" and is_desk_charter(p)` | 142/143. ❌ CH10 fails, so the any-mode leg is falsifiable |
| Mutant 2: `is_desk_charter` regex widened to `AGENTS/.+/CLAUDE\.md` | 141/143. ❌ CH6 and ❌ CH12 fail, so the sub-agent leg is falsifiable |

## Counterexample cases

| # | Input | Command | Printed result (new vs HEAD) | Verdict |
|---|---|---|---|---|
| A | Real repo: WALTER declares `AGENTS/WALTER/CLAUDE.md` whole (24,015 B) | `run.py head\|new . - --agent WALTER` | HEAD: ✅ 74% of budget. NEW: ✅ 48% of ceiling. rc 0 on both; machine line identical (rotation_due=3) | PASS: intended change |
| A2 | Real repo: HOMER declares its 41,649 B charter | `--agent HOMER` | HEAD: 🟠, over_budget=2, rotation_due=3. NEW: ✅ 83% of ceiling, over_budget=1, rotation_due=2, rc 1 (from another file) | PASS: intended change |
| B | KD declares the PEER charter `AGENTS/KC/CLAUDE.md` whole (40,000 B) | `--agent KD`, `--agent KC`, `--agent KC --owner-notice-blocking` | NEW KD: ✅ 80% of ceiling, rc 0. NEW KC owner notice: `🟠 ... 123% of budget over budget ← read whole by KD`, owner_notices_over_budget=1; with `--owner-notice-blocking`, rc 1. HEAD: both sides at budget (consistent) | ⚠️ the same file and bytes are graded two ways (finding 1) |
| C | KD declares CLASS row `AGENTS/*/CLAUDE.md` whole; KC charter 45,000 B | `--agent KD` | NEW: member row `✅ 90% of ceiling` (correct grade), but the CLASS header says `largest 45,000 B (90% of budget)` | ⚠️ label (finding 3); grade correct |
| D | KC declares its own charter, 52,000 B, `--charter-mode injected` | `--agent KC --charter-mode injected` | NEW: 🟠 104% of ceiling, rc 1, over_budget=1, over_cap=0, rotation_due=1. HEAD: 🟠 160% of budget, rc 1 | PASS |
| D2 | Same file, `--charter-mode explicit` (declared plus overlay union) | `--agent KC --charter-mode explicit` | NEW: one charter row (no double count), 🟠 of ceiling, reads=2, rc 1 | PASS |
| E | Declared charter, default mode, at 49,999 / 50,000 / 54,249 / 54,250 B | `--agent KC` | NEW: rc 0/1/1/1; over_budget 0/1/1/1; over_cap 0/0/0/1; rotation_due 0/1/1/1. HEAD: 49,999 gives rc 1 (budget) | PASS: boundaries exact; over_cap <= over_budget <= rotation_due holds at every size |
| F | UNDECLARED KC charter, 52,000 B, default mode | `--agent KC` | NEW = HEAD: rc 0, over_budget=0; advisory text only (`CHARTER-OVER-CEILING ... does not change rc`) | PASS: stays out of perimeter |
| G | `--fleet` (quiet path), KC declares its charter at 23,500 / 45,000 / 52,000 B | `--fleet` | 23,500: NEW `KC/CLAUDE.md 47% of budget`, desks_above_stop_threshold=1. 45,000: NEW ✅ `90% of budget`, rc 0 (HEAD 🟠 rc 1). 52,000: NEW 🟠 `104% of budget`, rc 1 | Grades PASS. ⚠️ label (finding 2). ⚠️ band count (finding 4) |
| G-real | Real repo `--fleet`, HEAD vs NEW diff | `run.py head\|new . - --fleet` | rc 1 on both. The worst-file % changes for RED 90→58, AEOLUS 156→101, FALCON 158→103, HOMER 128→83, HANS 74→48, all printed under the header "% is of BUDGET". HOMER drops from 2 to 1 over budget. desks_above_stop_threshold=22 on both | ⚠️ findings 2 and 4 are live in the real repo |
| H | Heuristic (undeclared) KD whose charter text references `AGENTS/KC/CLAUDE.md` | `--agent KD` | NEW = HEAD: the heuristic did not resolve the peer charter path, so there is no difference | INCONCLUSIVE: no capable case built (see Limits) |

## Findings (ranked)

No ❌ findings. Every rc, grade and machine-line count matches the stated intent in every case.

1. ⚠️ **The owner notice still grades a desk charter at the budget.** `scripts/read_cap_check.py:1244` (`mark, util, why = grade(b)` in the rule-15 owner-notice loop) was not switched to `grade_charter`. Case B shows the result. The reader desk sees the peer's 40,000 B charter as ✅ under the ceiling. The owning desk's notice shows the same file as 🟠 over budget, counts it in `owner_notices_over_budget`, and under `--owner-notice-blocking` turns rc 1. Before the diff both sides used the budget and agreed; the diff creates the disagreement. This is not live today: all 15 declared whole charter reads in READS.tsv are a desk's own charter. It is latent, and an "every mode where it is graded" claim does not hold for this path.
2. ⚠️ **The `--fleet` worst-file column mislabels a charter's percentage.** `scripts/read_cap_check.py:2176` prints `worst[3]` (now the share of the 50,000 B ceiling for a charter row) as `"% of budget"`, under the header at line 2158 that says "% is of BUDGET — the number the verdict grades". This is live in the real repo for RED (printed 58%, true 90% of budget), AEOLUS (101% vs 156%), FALCON (103% vs 158%), HOMER (83% vs 128%) and HANS (48% vs 74%). On HOMER the row reads `🟠 1 over budget` beside a worst file labelled 83%, which is not the file that is over. Output only; no rc effect.
3. ⚠️ **The CLASS-row header mislabels a charter's percentage.** `scripts/read_cap_check.py:1103` prints `largest N B (big[3] of budget)`. For a desk-charter member, big[3] is the share of the ceiling (case C: "90% of budget" for 45,000 B). The same wording is used at lines 1081 and 1111: members "≥70% of budget" are listed individually and the rest are described as "under 70% of budget". Output only; latent, since no live CLASS row matches a desk charter.
4. ⚠️ **`--fleet` counts a charter in the 70–75% rotation band.** `scripts/read_cap_check.py:2174` applies `in_ambiguous_band(_r[2])` to every row, charters included. `--agent` suppresses the band for charters (line 1062 sets `need = 0`, and case G2 prints no ↳ line), and the diff's own comment says there is "no rotation band" under the ceiling. In the real repo, FERT (23,017 B), ISHM (23,120 B) and HANS (24,213 B) are counted in `desks_above_stop_threshold=22` only because of their charter; the true figure is 19. The fleet text tells them a rotation may be owed. The field has no machine consumer outside this file (grep: only read_cap_check.py and head.py), so the effect is on output and reading only.
5. ℹ️ **The fleet charter summary is wrong for declared charters.** The summary at `scripts/read_cap_check.py:2220` says the over-BUDGET/over-CAP totals "EXCLUDE every charter by design". That is false for desks that declare their charter (15 live, now graded at the ceiling and counted, e.g. AEOLUS and FALCON are 🟠 on their charter). This falsehood existed before the diff, since declared charters were counted at the budget then, but the diff makes declared-charter grading the norm. Selftest R20 (line 1831) pins this string.
6. ℹ️ **The rc 0 verdict line still says "under budget".** The verdict at line ~1193, "every CAP-BEARING read ... is under budget", also covers a charter that is under the ceiling but over the budget (e.g. 45,000 B). Wording only.
7. ℹ️ **The legacy explicit-file mode still grades at the budget.** `python3 read_cap_check.py FILE...` (line 2262) still applies `grade()` to a desk charter path. This mode is not in PROME's listed mode set, so it is recorded only.
8. ℹ️ **The charter advisory reads oddly when the charter is declared.** In case D, `charter_line` prints both "OUT OF PERIMETER by rule 20 unless declared" and "this advisory does not change rc (a charter DECLARED ... is graded at the ceiling in its own row)". The charter is declared and rc did change, via its own row. The text is accurate but makes the reader work.

## Verdict

**ACCEPT-WITH-RESIDUE.** The functional change is correct. A declared desk charter is graded at the 50,000 B ceiling in default, injected, explicit and `--fleet` (quiet) modes: rc 1 at ≥50,000 B, 🔴 at ≥54,250 B, ✅ below with no rotation band in `--agent` output. Sub-agent, root and PROME charters stay at the budget (CH12 and the mutant 2 test). An undeclared charter stays advisory-only. The machine line keeps over_cap <= over_budget <= rotation_due at every boundary. The new selftest legs are falsifiable (mutants 1 and 2 are both caught). The residue is one grading path that still uses the budget, the owner notice (finding 1, latent), and three output and count inconsistencies (findings 2–4, two of them live in the real fleet output). None of these moves a desk's rc in the default configuration.

## Limits

- Time-boxed (~15 min); the review covers this diff only. The rest of the file and prome_gate.py were not reviewed beyond the ordering check at line 389.
- The harness execs the module with ROOT and READS_TSV re-pointed. It does not reproduce the `--reads-path` stderr banner path.
- Case H (the heuristic perimeter picking up a peer charter) did not produce a capable case, so heuristic-mode behaviour for a desk charter is unverified.
- `--owner-notice-blocking` is opt-in and unadopted, so the rc effect in finding 1 applies only under that flag.
- prome_gate.py was not run end to end against the new output.

END OF LEDGER
