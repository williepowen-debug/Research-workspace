# PROME manual simplification — 2026-09-11

Will authorized a bounded simplification after the bloat review. Scope: BOOT.md and CLOSEOUT.md only; preserve current procedures, thresholds, exceptions, commands, read scope, headings and memory hooks. Historical explanations remain recoverable at commit `4a0757370074f1a5ed48353894298b465f842047`, linked on-demand from both manuals. No new routine reads, tools, tests or memory entries.

Snapshot measurements from `PROME/tools/measure.py`:

| File | Before (bytes) | After (bytes) |
|---|---:|---:|
| BOOT.md | 20,922 | 19,036 |
| CLOSEOUT.md | 38,762 | 26,214 |

Validation: `git diff --check`; targeted `prome_gate.check_symmetry()` and `check_claude_dir_drift()` pass. Headings, memory hooks and harvested boot-read set preserved. Explicit `scripts/read_cap_check.py` finds both below the 32,550-byte budget; CLOSEOUT remains above the 75% rotation threshold. Full boot/closeout was not run (stateful and outside this editorial task).

Independent plan and result readers compared original and replacement text. Draft command-path and reference errors were corrected. Result review found the old symmetry check depended on a historical filename mention; an explicit one-way procedure-reference entry now preserves registration. The result reader accepted that correction; the final mechanical check passes. Counterexamples considered conflicting deck taps, ledger error classes, unexecuted gates, live guards during rotation, renames, and non-ff recovery with foreign dirty work.

Declared residue (2026-09-11): CLOSEOUT still lacks preferred rotation headroom. Existing runner sequencing puts ARGUS after the final gate even though review may cause writes; “two pages” wording coexists with the separate Decision Deck. The symmetry parser still uses substring presence. These pre-existing issues were not redesigned in this simplification. ARGUS scope/cost remains subject to its existing ordinary-closeout trial.
