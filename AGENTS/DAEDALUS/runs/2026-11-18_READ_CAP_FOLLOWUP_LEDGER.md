# FOLLOW-UP LEDGER — read_cap_check.py correction diff (uncommitted, over e334fb1c15)

Reviewed 2026-11-18, diff-bounded, read-only against the repo. Subject: `git diff -- scripts/read_cap_check.py` (+40/−15).
Method: read the diff and the code around it (L870–1300, L2066–2230, prome_gate.py L372–403). Ran the selftest. Compared HEAD with the working tree on every desk in both modes. Ran my own fixtures, plus mutation tests on the new legs.
Working copies used: `cmp/head.py` and `cmp/wt.py` in this scratchpad. They are byte-identical to HEAD and the working tree, except that the one `HERE =` line is pinned to the repo `scripts/`.

## Selftest
`python3 scripts/read_cap_check.py --selftest` → `✅ READ-CAP SELFTEST 140/140 leg(s) pass` (EXPECTED_LEGS 140).

Mutation check (scratch copies only):
| Mutation | Legs that caught it |
|---|---|
| A: revert the rotation_due change | CH2 + CH9 fail (138/140) |
| B: drop "cannot be read whole" from the default line | CH8 fails (139/140) |
| C: `>=` → `>` at the ceiling | CH7 fails (139/140) |

The new legs fail when the thing they guard is broken.

## Counterexamples
| # | Input | Command | Printed result | Verdict |
|---|---|---|---|---|
| X1 | Fixture. The charter is declared `whole` in the manifest AND read with `--charter-mode explicit`, at sizes 49,999 / 50,000 / 54,249 / 54,250 | driver → `main(["--agent","KC","--charter-mode","explicit"])` | 1 row for the charter (no double count; reads=3 = root + charter + S.md). 49,999: ✅ rc0 ob0 oc0 rot0. 50,000: 🟠 rc1 ob1 oc0 rot1. 54,249: 🟠 rc1 ob1 oc0 rot1. 54,250: 🔴 rc1 ob1 oc1 rot1 | PASS |
| X2 | Fixture. The charter is declared in the manifest, DEFAULT mode, 52,000 B | `main(["--agent","KC"])` | 🟠 "160% of budget", rc 1 (graded at 32,550). The charter line also says "CHARTER-OVER-CEILING … ADVISORY in this mode, rc unchanged" | Pre-existing behaviour, same at HEAD. See ⚠️1 |
| X3 | Fixture. Undeclared charter, explicit mode, CAP+1, quiet | `check_agent("KC", quiet=True, charter_mode="explicit")` | rc 1, nb 1, nc 1, 0 bytes printed | PASS |
| X4 | Fixture. Over-cap / 50,000 / 49,999 charter machine lines (desk renamed PROME) passed to `prome_gate.summarize_read_cap(..., "explicit")` | driver | Over-cap: no raise, (False, …over_budget=1 over_cap=1 rotation_due=1…). 50,000: no raise, False, rotation due. 49,999: (True, all zero) | PASS. Order invariant holds; rc/findings agree |
| X5 | Fixture. Manifest with only an attestation; explicit mode; charter 51,000 | `main([... "explicit"])` | `rc=1 reads=2 over_budget=1 over_cap=0 rotation_due=1` | PASS. Without the diff this case would read rotation_due=0 < over_budget=1, and prome_gate would raise |
| X6 | Fixture. `injected` and `unspecified` modes at CAP+5 / 50,000 / 49,999 | `main([... "--charter-mode", mode])` | rc 0 in all six runs. CAP+5: OVER-CEILING + "cannot be read whole". 50,000: OVER-CEILING only. 49,999: neither | PASS |
| X7 | `is_desk_charter` on AGENTS/KC/CLAUDE.md, AGENTS/KC/sub/CLAUDE.md, PROME/CLAUDE.md, CLAUDE.md | driver | [True, False, False, False] | PASS (root and PROME keep 32,550) |
| R1 | Real repo, all 48 AGENTS/* dirs + PROME, both modes (98 runs) | `python3 cmp/{head,wt}.py --agent <D> [--charter-mode explicit]` | Machine lines differ ONLY in explicit mode, ONLY for the 4 over-ceiling charters: AEOLUS 50,695 (rc 0→1, ob 0→1, rot 2→3), FALCON 51,484 (rc 0→1, ob 0→1, rot 3→4), LABOR 55,603 (rot 1→2), OSPREY 55,293 (rot 3→4). Default mode: 0 machine-line differences. The over_cap<=over_budget<=rotation_due<=reads invariant holds on all 98 working-tree lines | PASS. Matches the intent; no other behaviour change |
| R2 | Real repo `--fleet` | `python3 cmp/{head,wt}.py --fleet` | rc 1 both. Diff = 4 charter-line texts only (LABOR/OSPREY gain "cannot be read whole"; all four say "ADVISORY in this mode") | PASS |
| R3 | Real AEOLUS / OSPREY / CARL, explicit mode | `python3 scripts/read_cap_check.py --agent <D> --charter-mode explicit` | AEOLUS 🟠 101% of ceiling, rc 1. OSPREY 🔴, ob1 oc1 rot4, rc 1. CARL 49,162 ✅ 98% of ceiling, rc 0. No rule-5 "REMOVE … MORE B" line under any charter row (need forced to 0) | PASS |

## Findings
| Rank | Where | Finding |
|---|---|---|
| ⚠️1 | scripts/read_cap_check.py:929–933 (text the diff touched) and L1022–1025 (not in the diff) | **Pre-existing, residue.** In DEFAULT mode, a desk charter that the desk declares in READS.tsv (live: AEOLUS 50,695 B, WALTER) is graded by `grade()` at 32,550 B. AEOLUS shows 🟠 156% of budget, rc 1. On the same screen the charter line says "CHARTER-OVER-CEILING … ADVISORY in this mode, rc unchanged", yet that file is what makes rc 1. Two problems: (a) the output contradicts itself; (b) the root text says a desk charter's ceiling is 50,000 B "in place of 32,550 B", so grading at 32,550 here arguably contradicts the ruling. The output is identical at HEAD, so the diff did not cause this, and the "no other behaviour change" instruction rightly keeps it. Put to PROME beside the sub-agent (A7/A4) conflict |
| ℹ️2 | :1291–1295 | In explicit mode, an over-cap 🔴 charter's CHARTER-OVER-CEILING line says "over the ceiling by N B … Counted over budget (rc 1)" and does not mention the cap. The row above it does say "OVER THE CAP … cannot be read whole", so nothing is lost; the two lines just say different things |
| ℹ️3 | :929–933 | At exactly 50,000 B the default line prints "0 B over the 50,000 B … ceiling". At 49,999 B the explicit row prints "100% of ceiling ✅" (rounding of the `:.0%` format, which is older than this diff). Both are cosmetic |
| ℹ️4 | :1053 | The header's new suffix "except desk-charter rows, which say 'of ceiling'" prints on every `--agent` run, including runs with no charter row. Harmless |
| ℹ️5 | :79–82, :886–892 | The comments cite `runs/2026-11-18_READ_CAP_CHARTER_CEILING_REVIEW.md`. That file exists and covers the A7/A4 conflict (its F2), but it is UNTRACKED. Commit it with the script, or the pointer has nothing to resolve to |

No ❌ found.

## Verdict
**ACCEPT-WITH-RESIDUE.** The diff does what was intended:
- explicit mode: 🟠 / rc 1 from 50,000 B and 🔴 from 54,250 B, boundaries exact;
- root and PROME charters stay at 32,550;
- the over_cap <= over_budget <= rotation_due order holds, including the charter-only case that would have raised in prome_gate;
- default and injected modes only change advisory text and never change rc;
- no other machine-line change across 98 real runs.

The residue (⚠️1) is older than this diff and is a question for PROME to rule on, not a defect in the correction.

## Limits
- Time-boxed. I did not re-review the whole feature (out of scope).
- The class-row print path (L1084–1107) prints "of budget" for a member's %. Its interaction with a desk charter inside a CLASS row in explicit mode is NOT tested. No live manifest declares one; I checked only the READS.tsv grep.
- prome_gate's live run is PROME-only, and PROME/CLAUDE.md is not a desk charter, so X4 used a renamed fixture line, not a live gate run.
- Real-repo runs read live files that other sessions may be changing. HEAD and the working tree were run back to back on the same tree.
- `owner_notice` paths were not exercised against charter rows.

END OF LEDGER
