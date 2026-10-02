# WQ-237 — root `CLAUDE.md` YEYOU lines: the recorded scope, executed at the spine-audit #15 root-doc sitting (DOCKET L503)

**Authority (already given, no new ask):** Will APPROVE 2026-09-17 by Decision Deck tap (doc `237-20260917223351667-n7sw9k`); Will verbatim 2026-09-26 14:06 ET: *"WQ-237 already carries my September 17 approval in its own queue row. Move it to implementation tracking and execute its recorded scope at the planned root-doc sitting. Any separately gated L419 change still needs its own authority."* Row archived at `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md`. ⛔ L419 (root operator-surface wording) is NOT touched here.
**Executor:** PROME `prome-dc`, 2026-10-02 evening. **Review budget (root canon):** this record is the PLAN read; the root file gets ONE edit — one tool call in one sitting that makes the two deletions below (a stranger counting diff lines reads 2; the budget counts edit PASSES); one RESULT read; residue declared here. **Plan read: coldreader `coldread-wq237-plan` 2026-10-02 18:2x ET — 19 ✅ / 8 ⚠️ / 3 ❌; all three ❌ and the ⚠️ fixed in this record before execution (banner line pointer · read-cap invariant named a tool that never reads root · the four YEYOU-live surfaces were searched in W1, they are in W2 §9 #19); ledger `scratchpad/coldread_wq237_plan.md` of session daab8fa7.**
**Basis fact:** YEYOU RETIRED 2026-09-05 (`PROME/ROSTER.md` retired section; Will *"retire yeyou"*, WQ-181 ①). A retired agent cannot hold an auto-push exception or a memory-index exemption.

## Proposed edits — verbatim before → after

### 1. Root `CLAUDE.md`, Git Protocol, Scope-note paragraph (currently line 84) — strike the YEYOU exception
BEFORE (fragment): `… TERRY (self-sweeps), WALTER (per \`AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md\` §7), YEYOU (manual/branch). Everyone else: …`
AFTER (fragment): `… TERRY (self-sweeps), WALTER (per \`AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md\` §7). Everyone else: …`
Only the string `, YEYOU (manual/branch)` is removed. Nothing else on the line changes.

### 2. Root `CLAUDE.md`, session-end step 1d (currently line 93) — strike the exemption
BEFORE (line end): `… **Do NOT compact \`MEMORY.md\` yourself — flag to PROME.** YEYOU exempt.`
AFTER (line end): `… **Do NOT compact \`MEMORY.md\` yourself — flag to PROME.**`
Only the trailing ` YEYOU exempt.` is removed.

### 3. Root `README.md` line 112 — dead link
BEFORE: `[\`AGENTS/DAEDALUS/MATURITY_MAP.md\`](AGENTS/DAEDALUS/MATURITY_MAP.md) tracks those differences.`
AFTER: `[\`AGENTS/DAEDALUS/FLEET_DIRECTORY.md\`](AGENTS/DAEDALUS/FLEET_DIRECTORY.md) tracks those differences.`
⚠️ **Premise corrected at execution:** the WQ-237 row called this link DEAD; it is NOT — `AGENTS/DAEDALUS/MATURITY_MAP.md` exists (5,266 B; last commit 46851c388, committed 2026-07-08) as a historical snapshot whose own banner (paraphrased, two sentences) says it is FROZEN 2026-07-07, not maintained, levels not current, and that live maturity truth is `FLEET_MAP.tsv`. The approved remedy still applies on the corrected basis: a root README should point readers at the live surface, not a frozen first-scan snapshot. **Why `FLEET_DIRECTORY.md` and not `FLEET_MAP.tsv`:** FLEET_DIRECTORY.md is DAEDALUS's generated, boot-readable directory view over FLEET_MAP.tsv (maturity column included), which is what a README reader wants; the TSV is its data. `FLEET_DIRECTORY.md` exists (11,508 B, 2026-10-01).

### 4. `AGENTS/YEYOU/CLAUDE.md` — one banner line inserted after the title (line 1), nothing else touched
INSERT: `> 🧊 **FROZEN — YEYOU RETIRED 2026-09-05 (Will "retire yeyou", WQ-181 ①; \`PROME/ROSTER.md\` retired section). This charter is history: its routing rows — including its route-around row (the \`**Write** only AGENTS/YEYOU/ … outbox/\` bullet) — are not live; no YEYOU session boots again; nothing here is maintained. Banner placed under WQ-237's extended scope at the 2026-10-02 root-doc sitting.**`
Closes Wiring Sweep #2 census item A-2 by its SECOND alternative ("authorise a one-line FROZEN banner"); the route-around census row can then read NO-FIX-RETIRED on DAEDALUS's side. No line number is cited in the banner because the insertion itself shifts every line below it.

### 5. `AGENTS/_INDEX.md` line 65 — the shared roster-nav row (ROSTER wins; this is a mirror)
BEFORE: `| YEYOU | [\`YEYOU/\`](./YEYOU/) | Meta — repo-wide reviewer (manual/branch) |`
AFTER: `| YEYOU | [\`YEYOU/\`](./YEYOU/) | 🧊 RETIRED 2026-09-05 (WQ-181; \`PROME/ROSTER.md\`) — was the repo-wide reviewer; directory kept as history |`

### 6. `AGENTS/_SYNTHESIS_OPS.md` line 35 — same class
BEFORE: `| YEYOU | [\`YEYOU/\`](./YEYOU/) | Repo-wide reviewer (manual/branch model). |`
AFTER: `| YEYOU | [\`YEYOU/\`](./YEYOU/) | 🧊 RETIRED 2026-09-05 (WQ-181; \`PROME/ROSTER.md\`) — was the repo-wide reviewer; directory kept as history. |`

### 7–8. The two OWNER-held surfaces — packets, never PROME edits
`AGENTS/WALTER/REGISTRY.tsv` line 17 (YEYOU as a Tier-1 LIVE reviewer row) and `AGENTS/RAV/README.md` line 10 (RAV's inbox defined as receiving YEYOU NEEDS-VERIFY escalations) are active files of persistent desks. The approved scope names them; the git protocol routes the edit through the owner. Packets (carve-out ①): `AGENTS/WALTER/inbox/2026-10-02_from-PROME_WQ-237-REGISTRY-YEYOU-row-retired.md` · `AGENTS/RAV/inbox/2026-10-02_from-PROME_WQ-237-README-YEYOU-escalation-line.md`. Source of the four: `AGENTS/DAEDALUS/runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W2.md` line 295 (census row) and line 341 (§9 #19).

## Invariants the result read checks
- Root `CLAUDE.md`: exactly two deletions (the strings above), no other byte changes — `git diff --stat -- CLAUDE.md` prints the literal `1 file changed, 2 insertions(+), 2 deletions(-)` and `git diff` shows only those two lines.
- `grep -c YEYOU /home/willi/Research-workspace/CLAUDE.md` (the ROOT path — from `PROME/` a bare `CLAUDE.md` is the charter and passes vacuously) → 0 after the edit; it reads 2 before.
- Root `CLAUDE.md` stays under the 32,550 B read cap: `python3 PROME/tools/measure.py CLAUDE.md` (24,236 B before the edit; it only shrinks). `read_cap_check.py --agent PROME` is NOT the instrument — it never reads root.
- `README.md`: one line changed; the new link target exists.
- `AGENTS/YEYOU/CLAUDE.md`: one line inserted at line 2; `git diff --stat` = +1/−0.
- `.claude/` parity gate unaffected (no skill/agent file touched).
- `AGENTS/_INDEX.md`, `AGENTS/_SYNTHESIS_OPS.md`: one line changed each; `grep -c YEYOU` on each stays 1 (the row is annotated, not deleted).
- The two packets exist at the paths named in §7–8 and are committed (carve-out ①).
- `PROME/GIT_COORDINATION.md` Hard-Rules bullet 5 already points at this record's outcome (edited tonight in the audit fix round).

## Residue (declared at execution)
- The four YEYOU-live surfaces: two edited here (§5–6), two packeted to their owners (§7–8) — the owners' encodes are OWED, not done, at this sitting; the WALTER and RAV receipts close them. *(The earlier draft of this record called the four SEARCH-NOT-FOUND after searching W1; the plan read found them in W2 — corrected before execution.)*

## Reads (the root-canon budget: one plan read, one result read; both used, no third owed — no result-read ❌ touched a rule's meaning)
- **Plan read:** coldreader `coldread-wq237-plan`, 2026-10-02 18:2x ET — 19 ✅ / 8 ⚠️ / 3 ❌. All three ❌ and the ⚠️ fixed in this record BEFORE any file was edited (see the header line). Ledger: `scratchpad/coldread_wq237_plan.md`, session daab8fa7 (not a repo artifact).
- **Result read:** coldreader `coldread-wq237-result`, 2026-10-02 18:3x ET — 33 ✅ / 6 ⚠️ / 2 ❌. Verdict verbatim: *"The edits are right; the record isn't finished."* Every BEFORE/AFTER matches the working tree exactly; nothing else changed in the five files; root diff stat literally `2 insertions(+), 2 deletions(-)`; `grep -c YEYOU` on root 0 (2 at HEAD); measure.py 24,199 B. ❌ 34 = the packets were not yet committed at read time (true by construction before the closeout commit; the commit discharges it — verify with `git ls-files --error-unmatch` on both paths after). ❌ 37 = this section still said PENDING — fixed here, a record edit, not a canon edit. Ledger: `scratchpad/coldread_wq237_result.md`.

## Declared residue (2026-10-02, after the result read)
- §5–8 (the two nav-row edits and the two packets) were added to this record AFTER the plan read, in response to its ❌ 28; the result read is therefore the first and only independent read of that text. The edits themselves were verified at the artifact by the result reader; the record text for §5–8 has one read, not two. No further read is taken (budget).
- The WALTER and RAV encodes are OWED at their owners; this sitting does not close them. Receipts land in `PROME/inbox/`.
- State: root `CLAUDE.md` + `README.md` + `AGENTS/_INDEX.md` + `AGENTS/_SYNTHESIS_OPS.md` + `AGENTS/YEYOU/CLAUDE.md` = IMPLEMENTED · TESTED (invariants run) · INDEPENDENTLY VERIFIED (result read) · nothing STILL UNRESOLVED on the edits; the two owner encodes = OWED.
