# Independent review: commit e334fb1c15, `scripts/read_cap_check.py` (desk charters graded at 50,000 B)

**Reviewer:** independent reader (Claude Code, Opus 5.5), 2026-11-18. I did not edit the repository. Fixtures, harnesses and outputs are in this scratchpad folder (`ce.py`, `ce_out.txt`, `mutate.py`, `mutate_out.txt`, `fleetdiff.py`, `pre.py`, `post.py`, `arch_*`).
**Spec read:** packet `9e02c0d712` ("The shape", "Conditions"); root `CLAUDE.md` § Data Hygiene read-cap bullet; `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rule 20 (line 32) and charter row (line 40); ruling record `PROME/proposals/2026-11-16_wq701-pass8-rules-RULED.md` (lines 21, 103); DAEDALUS proposal `PROME/inbox/processed/2026-11-16_from-DAEDALUS_WQ-701-A2-READ_CAP-rule-20-amended.md` (lines 22–35).
**Working tree:** `scripts/read_cap_check.py` is byte-identical to `e334fb1c15` (`cmp` clean). CAP_BYTES = 54,250; BUDGET_BYTES = 32,550.

**Self-test:** `python3 scripts/read_cap_check.py --selftest` printed
`✅ READ-CAP SELFTEST 137/137 leg(s) pass (R7-stage-2 manifest consumer: C1–C12 + N1–N8 owner notice + rc contract, frozen tempdir fixtures)`.
The pre-change file (`git show e334fb1c15^:scripts/read_cap_check.py`) printed `✅ READ-CAP SELFTEST 131/131`.

---

## (1) Per-condition verdicts

| # | Condition (source) | Verdict | Evidence |
|---|---|---|---|
| S1 | Explicit mode: a desk's own `AGENTS/<NAME>/CLAUDE.md` graded at 50,000 B (packet, The shape 1) | **MET for under-ceiling. Over-ceiling NOT ADJUDICATED, see ❌2** | CE3: a 40,000 B declared charter gives `✅ … 80% of ceiling`, rc 0. On the live repo, HOMER (41,649 B) prints `✅ … 83% of ceiling` and CARL (49,162 B) prints `98% of ceiling`. Over 50,000 B the row is ⚠️ ADVISORY with rc 0 (AEOLUS 50,695 B and FALCON 51,484 B went from rc 1 to rc 0). The packet does not say "advisory" for explicit mode. |
| S2 | Explicit mode: root `CLAUDE.md` and `PROME/CLAUDE.md` stay at 32,550 B (The shape 1) | **MET** | CE7: root and PROME charter at 40,000 B each print `🟠 … 123% of budget`, rc 1, over_budget=2. Self-test CH4 covers root. On the live repo, PROME/CLAUDE.md prints `🟡 … 86% of budget`. |
| S3 | Default mode: one advisory line `CHARTER-OVER-CEILING` for a desk charter over 50,000 B, never rc-driving (The shape 2) | **MET in form, with residue ⚠️4** | The token is appended to the existing `ℹ️ charter …` line (line 922–924). Across all 45 desks run pre vs post in default mode (`fleetdiff.py`), rc and every count are identical. The residue: for a desk that declares its own charter, the same screen shows that file as `🟠 over budget` with rc 1 (CE3 52,000 default; live AEOLUS). |
| S4 | No other behaviour changes (The shape 3) | **MET for default, injected and --fleet. Explicit mode has the intended changes plus two side effects** | Default mode: no count changes on 45 desks. Explicit mode: 9 live desks go from rc 1 to rc 0 (SAM, HENRY, CARL, BOND, AEOLUS, VULCAN, FALCON, DEWEY, OTTO), and rotation_due drops by 1 on 22 desks. Side effect 1: a PROME test turns red (❌1). Side effect 2: the ceiling is also applied to *another* desk's declared charter (ℹ️12). |
| C1 | Acceptance conditions written before the edit (Conditions 1) | **NOT MET** | I found no pre-edit acceptance record in history: the DAEDALUS commits for 2026-11-16 are 648529e55a and 279fd78dc9 (READ_CAP.md only). The untracked `AGENTS/DAEDALUS/runs/2026-11-18_READ_CAP_CHARTER_CEILING_REVIEW.md` line 5 says this itself: "They were not". I read only its header, to avoid anchoring on it. |
| C2 | An over case and a clean case both shown (Conditions 1) | **MET** | CH1 (40,000 B clean), CH2 (52,000 B over), CH3 (over the CAP) and CH5 (default mode, 52,000 B vs 40,000 B). I grafted the CH legs onto the pre-change behaviour: CH1, CH2 and CH5 fail (134/137), so these legs do bite. |
| C3 | Neighbours considered: sub-agent charter, root, PROME charter, desk with no charter (Conditions 1) | **PARTLY MET** | Root: end-to-end (CH4). Sub-agent and PROME: CH6 tests only the `is_desk_charter` predicate, with no end-to-end run. Desk with no charter: no self-test leg. I ran CATO and RAV myself: `READ-CAP 2 CANNOT-EVALUATE [CATO]: no charter at AGENTS/CATO/CLAUDE.md`, rc 2 in both modes, unchanged from before. |
| C4 | One independent reader with its own counterexample before the change is called fixed (Conditions 2) | **NOT ADJUDICATED (this ledger is that reader)** | The change was committed and pushed with "Not reviewed beyond reading the diff". The commit message does not call it fixed. |
| C5 | Sub-agent charters stay undecided: the checker does not grade them at either number (Conditions 3) | **NOT MET** | In explicit mode a sub-agent charter is graded at 32,550 B. CE2 (40,000 B): `🟠 AGENTS/P/sub_agents/S/CLAUDE.md 40,000 B 123% of budget over budget`, rc 1. Live STUE (47,588 B): `🟠 … 146% of budget`, `REMOVE 24,804 MORE B`, rc 1, rotation_due=2. The code comment at line 78–79 decides the case ("sub-agent charters … keep BUDGET_BYTES"). This keeps the pre-change behaviour (consistent with S4), so C5 and S4 conflict and PROME has to say which one wins. Default mode handles sub-agents in line with C5: no grade and no advisory (CE2b, 52,000 B). |
| O1 | Operator's rule: for `AGENTS/<NAME>/CLAUDE.md` the ceiling is 50,000 B, in place of 32,550 B (root § Data Hygiene) | **Consistent in explicit mode only** | In default, injected and --fleet mode, a desk charter declared in READS.tsv is still graded at 32,550 B. Live HOMER: default `🟠 AGENTS/HOMER/CLAUDE.md 41,649 B 128% of budget`, rc 1. Explicit: `✅ … 83% of ceiling`. Same file, two verdicts. In the live `--fleet` run, AEOLUS, FALCON and HOMER all show their own charter as the worst file "of budget". 15 desks declare their own charter whole (READS.tsv). See ⚠️4. |
| O2 | Operator's rule: the charter "stays under" 50,000 B, binding (root bullet; ruling record line 21) | **NOT MET in explicit mode, see ❌2** | Over 50,000 B and under the CAP, explicit mode gives rc 0 (CE1 50,001 and 54,249: rc 0, over_budget=0). |

## (2) Counterexamples I ran (none is in the self-test)

The harness `ce.py` copies the committed script into a fixture tree as `<fx>/scripts/read_cap_check.py`, so ROOT points at the fixture. The full output is in `ce_out.txt`.

| ID | Input | Command | Printed (quoted) | Verdict |
|---|---|---|---|---|
| CE1 | Declared desk D, charter of 49,999 / 50,000 / 50,001 / 54,249 / 54,250 B | `--agent D --charter-mode explicit` | 49,999: `✅ … 100% of ceiling under the ceiling`, rc 0. **50,000: `⚠️ … over the ceiling by 0 B — ADVISORY`**, rc 0. 54,249: `⚠️ … over the ceiling by 4,249 B`, rc 0. 54,250: `🔴 … OVER THE CAP (100% of the 54,250 B cap)`, rc 1, **`over_budget=1 over_cap=1 … rotation_due=0`** | The boundaries are coded consistently with `grade()` (>=). "over by 0 B" is a wording defect (ℹ️9). Neither boundary is tested: mutants M6 and M11 survive. |
| CE2 | Sub-agent `AGENTS/P/sub_agents/S/CLAUDE.md` at 40,000 B, and at 52,000 B | `--agent S --charter-mode explicit` / `--agent S` | Explicit: `🟠 AGENTS/P/sub_agents/S/CLAUDE.md 40,000 B 123% of budget over budget`, rc 1. Default, 52,000 B: no CHARTER-OVER-CEILING, rc 0 | C5 NOT MET in explicit mode (❌3). |
| CE3 | Desk D declares its own charter `whole`, at 40,000 and 52,000 B | default / `explicit` / `injected` | 40,000: default `🟠 … 123% of budget` rc 1; explicit `✅ … 80% of ceiling` rc 0; injected `🟠` rc 1. 52,000 default: `🟠 … 160% of budget` rc 1 **and** on the same screen `⚠️ CHARTER-OVER-CEILING: 2,000 B over … ADVISORY, rc unchanged` | The verdict depends on the mode, and the default screen contradicts itself (⚠️4). |
| CE4 | Reader R declares *D's* 40,000 B charter `whole` | `--agent R` / `--agent R --charter-mode explicit` | Default `🟠 AGENTS/D/CLAUDE.md … 123% of budget` rc 1. Explicit `✅ … 80% of ceiling` rc 0 | Goes beyond the packet's "own" charter, but agrees with root. No live instance (no cross-desk charter rows in READS.tsv) (ℹ️12). |
| CE5 | Desk charter at CAP+1, root at 100 B, nothing else large | `--agent D --charter-mode explicit`, post vs pre | Post: `over_budget=1 over_cap=1 … rotation_due=0`. Pre: `… rotation_due=1`. I fed the post shape (desk renamed PROME) to `PROME/tools/prome_gate.py summarize_read_cap`: **`RAISED: ValueError contradictory read-cap counts`**. With rotation_due=1 it returns normally | The change makes the invariant `over_budget <= rotation_due` (prome_gate.py:389) breakable. It is latent today (⚠️5). |
| CE6 | Path forms: declared row `./AGENTS/D/CLAUDE.md`; script run through a symlinked repo root; desk L whose dir is a symlink to AGENTS/D | `--agent D/L --charter-mode explicit` | All three: `✅ … 80% of ceiling under the ceiling`, rc 0 | Robust, no defect (ℹ️15). |
| CE7 | PROME/CLAUDE.md 40,000 B + root 40,000 B | `--agent PROME --charter-mode explicit` | `🟠 CLAUDE.md 40,000 B 123% of budget`, `🟠 PROME/CLAUDE.md 40,000 B 123% of budget`, rc 1 | S2 MET. |
| CE8 | `--fleet`: desk A (heuristic) with a 52,000 B charter; desk B declares a 40,000 B charter | `--fleet` | A: `· ⚠️ CHARTER-OVER-CEILING: 2,000 B over`. B: `🟠 B 2 1 0 AGENTS/B/CLAUDE.md 123% of budget`. The summary still says `⛔ The over-BUDGET/over-CAP totals above EXCLUDE every charter by design` | Fleet grades declared charters at 32,550 B (⚠️4), and the summary sentence is false (pre-existing, ℹ️13). |
| L1 | Live: STUE, AEOLUS, OSPREY, CARL, HOMER, PROME, CATO, RAV, `--fleet` | `python3 scripts/read_cap_check.py --agent <N> [--charter-mode explicit]` | STUE explicit rc 1 (`🟠 … 146% of budget`). AEOLUS explicit rc 0 / default rc 1. OSPREY explicit `🔴 … OVER THE CAP (102%…)` rc 1. CARL explicit `✅ … 98% of ceiling` rc 0. Fleet `desks_over_budget=3 … desks_with_advisory=4` | See above. |
| L2 | Live pre vs post, 45 desks (fleet plus PROME, STUE, DOC, TOURISM), explicit and default | `fleetdiff.py` (imports pre.py/post.py with ROOT set to the repo; read-only) | Default: **0 differences**. Explicit: 9 desks rc 1→0; HOMER over_budget 2→1; LABOR and OSPREY stay rc 1; rotation_due −1 on 22 desks | This is the rc contract change (section 3 below). |
| T1 | Caller tests at pre and post revisions (`git archive` of `PROME/tools` + `scripts` into scratch) | `.venv/bin/python -m pytest PROME/tools/tests/test_boot_charter_coverage.py` | Pre (`e334fb1c15^`): `10 passed`. Post: **`FAILED …::test_default_other_desk_grade_is_unchanged_and_explicit_is_owner_scoped` / `AssertionError: 0 != 1`** | ❌1. Also run on the live repo: test_boot_coverage 22 passed, test_table_check_manifest_classes 7 passed, DAEDALUS test_read_cap_companions 9 passed. |

**Mutation check of the six new legs (`mutate.py`, output in `mutate_out.txt`).** I applied one mutation at a time to the committed file and ran `--selftest`:

| Mutation | Result |
|---|---|
| M1 explicit dispatch off | CH1, CH2 fail |
| M2 default suffix off | CH5 fails |
| M3 rotation_due filter removed | CH1 fails |
| M4 explicit advisory print removed | CH2 fails |
| M5 `is_desk_charter` loosened to any depth | CH6 fails |
| M7 `need=0` removed | CH1 fails |
| M8 over-ceiling returns 🟠 | CH2 fails |
| M9 over-CAP returns ⚠️ | CH3 fails |
| M10 ceiling constant set to 54,000 | CH1, CH2, CH5 fail |
| **M6 ceiling `>=` changed to `>`** | **survives, 137/137** |
| **M11 CAP `>=` changed to `>` in `grade_charter`** | **survives, 137/137** |

Graft test: the CH block plus the two names it needs, added to the **pre-change** file with no behaviour change, gives `❌ 134/137`, with CH1, CH2 and CH5 failing. CH3 and CH4 pass on the pre-change behaviour by design: they are no-change legs. CH6 runs on the pre-change file only because I stubbed the function in; on the real pre-change file it would stop with a NameError, not fail an assertion.

## (3) Findings, ranked

**❌1. The commit breaks a PROME-owned caller test, and nobody flagged it.**
- Where: `PROME/tools/tests/test_boot_charter_coverage.py:124-131`.
- What: `test_default_other_desk_grade_is_unchanged_and_explicit_is_owner_scoped` writes `AGENTS/ALPHA/CLAUDE.md` at BUDGET+1 (32,551 B) and expects explicit-mode rc 1. Post-change the result is rc 0, so the test fails with `AssertionError: 0 != 1`. It passes at `e334fb1c15^`.
- The new behaviour is the intended one, so the test's expectation is stale. The file belongs to PROME, though, and the commit says "Not reviewed beyond reading the diff". The reconciliation (a new fixture size or a new expected value) is PROME's to make by packet.
- Context: earlier reviews used this test as an acceptance reproduction (`PROME/reports/2026-11-04_L835-acceptance/reproduce.py:25`).

**❌2. In explicit mode, a charter over the ruled ceiling is made rc 0 (advisory only), and the authority cited for that is unsourced.**
- Where: `scripts/read_cap_check.py:881-892`; the docstring at line 884 says "Will chose a warning, not a block".
- What the sources say:
  - The packet makes the default-mode line advisory ("Advisory, never rc-driving") and says only "graded at 50,000 B" for explicit mode.
  - In this tool, "graded at BUDGET" means over → 🟠 → rc 1.
  - Root says the charter "stays under 50,000 B" and that the read-cap budget is "binding".
  - I found no warning-not-block ruling in the ruling record, the DAEDALUS proposal or the packet.
- Effect: live AEOLUS (50,695 B) and FALCON (51,484 B) are over the ruled ceiling and went from rc 1 to rc 0 in explicit mode, the mode used by `daedalus_gate.py` B4/C7 and PROME's boot. This loosens a gate in the all-clear direction.
- Owner: PROME, to state the intended rc semantics. Either way, the docstring's attribution needs a source or needs to go.

**❌3. Condition C5 is not met: sub-agent charters are graded at 32,550 B in explicit mode.**
- Where: `scripts/read_cap_check.py:78-79` (comment), `:875-878`, `:1013-1016`.
- Live STUE (`AGENTS/CARL/sub_agents/STUE/CLAUDE.md`, 47,588 B): `🟠 … 146% of budget`, rc 1, with a rotation remedy.
- This is the pre-change behaviour, kept under S4. The packet's two conditions conflict, and the code resolves the conflict silently in its own comment instead of reporting it.
- A form that keeps the sub-agent case undecided would be: no grade, plus an explicit "not adjudicated" advisory that does not drive rc.

**⚠️4. Declared desk charters are still graded at 32,550 B in default, injected and --fleet mode, so the same file gets two verdicts.**
- Where: `scripts/read_cap_check.py:1013` (only `charter_mode == "explicit"` dispatches to `grade_charter`) and `:922-924`.
- Live HOMER: default `🟠 128% of budget`, rc 1; explicit `✅ 83% of ceiling`, rc 0.
- Default AEOLUS prints `🟠 over budget` for its charter, plus "CHARTER-OVER-CEILING … ADVISORY, rc unchanged" on the same screen, while rc=1 comes from that same file.
- 15 desks declare their own charter whole. The packet's S4 forbids the fix, but root's rule ("in place of 32,550 B") is not honoured in these modes. This is a decision for PROME.

**⚠️5. The result line can now break a consumer invariant.**
- Where: `scripts/read_cap_check.py:2087-2088` (rotation_due excludes charter rows, including 🔴 over-CAP ones) against `PROME/tools/prome_gate.py:389` (`over_cap <= over_budget <= rotation_due`).
- CE5 produces `over_budget=1 … rotation_due=0`, and `summarize_read_cap` raises `contradictory read-cap counts`.
- It is latent: prome_gate parses PROME's run only, PROME's perimeter has no desk charter, and root and PROME/CLAUDE.md keep rotation_due ≥ 2 today. Before the change, rotation_due always counted an over-CAP file.

**⚠️6. Condition C1 is not met: the acceptance conditions were written after the edit.**
- The author's own 11/18 record discloses this. Process residue only, and the record is honest about it.

**⚠️7. The canon text is stale after the build.**
- Where: `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md:32` ("Enforcement: none today … grades them at 32,550 B, not 50,000 B … repair not built") and `:40` ("No instrument applies 50,000 B today").
- Both are false in explicit mode since e334fb1c15. The owner is DAEDALUS.

**⚠️8. In default mode, a charter over the CAP gets only the ceiling advisory.**
- Where: `scripts/read_cap_check.py:922-924`.
- Live LABOR (55,603 B) and OSPREY (55,293 B) print "5,603 B over the 50,000 B desk-charter ceiling … ADVISORY". Nothing says the file cannot be read in one pass. Explicit mode prints 🔴 OVER THE CAP for the same files. The default text understates.

**ℹ️ Minor findings**

| # | Finding | Where |
|---|---|---|
| 9 | Exactly 50,000 B prints "over the ceiling by 0 B". This matches the ">= is over" convention of `grade()`, but the wording contradicts itself. Neither boundary (50,000 or 54,250) is tested: M6 and M11 survive. | lines 889-890 |
| 10 | The header still says "ALL % BELOW ARE OF BUDGET" while charter rows print "of ceiling". | line 1044 |
| 11 | The self-test comment "Each CH leg watched FAILING on the pre-change file" is not true for CH3/CH4 (no-change legs, pass pre-change) or CH6 (NameError, not an assertion). CH1/CH2/CH5 do fail as claimed. | line 1825 |
| 12 | Explicit mode applies the ceiling to any `AGENTS/<X>/CLAUDE.md` in the perimeter, including another desk's declared charter (CE4). That goes beyond the packet's "own" but agrees with root. No live instance. | line 1013 |
| 13 | The fleet summary sentence "totals … EXCLUDE every charter by design" is false for declared charters (AEOLUS, FALCON, HOMER). Pre-existing, not introduced here. | line 2175 |
| 14 | For a 🔴 charter, the rc-1 remedy text prescribes "two-state rotation … or hot/cold split" instead of root's "move history out". Minor wording. | line 1145 |
| 15 | `is_desk_charter` handles a `./` prefix, a symlinked repo root and a symlinked desk dir correctly (CE6). The module never calls realpath, so ROOT and the paths stay in the same form. | — |

## rc / exit-code contract changes visible to callers

| Mode / caller | Change |
|---|---|
| Explicit mode (`daedalus_gate.py` B4/C7 for DAEDALUS; `prome_gate.py` / `boot_session.py` for PROME) | rc 1→0 for desk charters in 32,550–54,249 B. over_budget falls by 1 and rotation_due falls by 1 when the charter is ≥ 24,412 B. DAEDALUS (16,617 B) and PROME (whose charter is not a desk charter) are unaffected today. |
| 9 live desks run in explicit mode by hand or in a Production Review | rc 1→0 |
| Default and `--fleet` (`scripts/validate_all.py` D1, which parses the fleet line) | No count changes. Only text is added to the `ℹ️ charter` line. |
| `validate_all.py` A9 (`--selftest`) | Still passes, 137/137 |
| `PROME/tools/tests/test_boot_charter_coverage.py` | Now fails (❌1) |
| `prome_gate.py:389` invariant | Now breakable (⚠️5, latent) |

## (4) Overall verdict

**REJECT as "fixed" in its current state. No revert is needed.**

The mechanics are sound, and the CH1/CH2/CH5 legs genuinely guard them: they fail on the pre-change behaviour and catch 9 of 11 mutants. But the change cannot be called fixed while:

- a PROME caller test it turned red stays unreconciled (❌1);
- explicit-mode rc semantics over the ceiling rest on an unsourced "Will chose a warning" (❌2);
- packet condition C5 is unmet, and its conflict with S4 is resolved in a code comment instead of being reported (❌3).

What would close it: PROME rules on ❌2 and on C5 against S4, PROME updates its test, and DAEDALUS corrects the line-884 attribution and READ_CAP rule 20 line 32/40. After those, I would expect ACCEPT-WITH-RESIDUE, the residue being ⚠️4, ⚠️5, ⚠️8 and the ℹ️ items.

## (5) Limits (what I did not check)

- I did not run `daedalus_gate.py boot|closeout` end to end, `boot_session.py`, or `validate_all.py` as a whole. I checked their parsing code and ran the prome_gate parser directly on a constructed line.
- I did not run the PROME tests that rely on git fixtures under `scripts/validate_all.py`'s own self-test, other than A9.
- CE5 reachability for PROME is reasoned from READS.tsv (no PROME row declares a desk charter), not exhaustively proven over every future manifest.
- I did not read Will's chat or the session transcript. "No source found" for the warning-not-block attribution covers only the ruling record, the DAEDALUS proposal, the PROME packet and a grep of PROME/, AGENTS/DAEDALUS/ and memory/.
- I read only the header of the author's 11/18 acceptance record, on purpose, to avoid anchoring.
- I did not check Codex-desk charters stored under other filenames (CATO has `AGENTS.md`/`CHARTER.md`, no `CLAUDE.md`). Root's rule names `CLAUDE.md` only.
- The sub-agent end-to-end runs used my fixture and the live STUE only. I did not run DOC, TOURISM and the other sub-agents individually, though `fleetdiff.py` found no pre/post difference for DOC or TOURISM.
- Side effect disclosure: running the three live-repo test files under pytest refreshed gitignored bytecode caches (`PROME/tools/tests/__pycache__`, `AGENTS/DAEDALUS/scripts/__pycache__`, `AGENTS/DAEDALUS/scripts/tests/__pycache__`). These are not tracked files, `git status` is unchanged, and I did not delete them.

END OF LEDGER
