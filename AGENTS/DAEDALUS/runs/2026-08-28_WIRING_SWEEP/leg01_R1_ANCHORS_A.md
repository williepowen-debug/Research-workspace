# Leg ① — R1 corrections boot-leg wiring: anchor survey, batch A (12 desks)

Read-only survey for a Will-gated batch edit. No files outside this `runs/` dir were modified.

**Canonical wording sources (read in full):**
- Blueprint: `AGENTS/DAEDALUS/BLUEPRINTS/market-agent.md` (§7 bullet, "R1 corrections boot leg (REQUIRED, fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17; DAEDALUS's lane)"):
  > Every active desk's boot runs the cwd-proof line `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" <NAME>` — surfaces unreceipted rows of the fleet correction register (`AGENTS/WALTER/registry/CORRECTIONS.tsv`; WALTER owns schema+prune). §9 rc 0/1/2: NAMED rows BLOCK until receipted (`--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED`, receipts append to the desk's own `registry/corrections_receipts.tsv` — commit it, your pathspec), ALL rows WARN-never-block, unparseable dates are rc=2 never a row-skip (A2). `NO-OP` is a positive claim (checked, nothing cited); `CONTESTED` escalates via PROME rails.
- DAEDALUS's own SPAWN PROTOCOL step 5b (`AGENTS/DAEDALUS/CLAUDE.md`), used as the terse wording template:
  > 5b. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" DAEDALUS` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file).

**Proposed generic insertion text (adapted per desk's `<NAME>` and local numbering):**
```
<label>. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" <NAME>` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
```
No desk in this batch had a `corrections_boot_check` reference already (`grep -c` = 0 across all 12).

---

## AEOLUS
1. **Boot location:** `## BOOT SEQUENCE (when spawned)` at `AGENTS/AEOLUS/CLAUDE.md:24`. Numbering: plain `1.`–`7.` (no letter substeps in boot).
2. **Existing shared-script step:** none in BOOT. `scripts/ledger_staleness.py` is NOT invoked anywhere in this file (only prose mentions `domain_log_check.py`, AEOLUS-local, at closeout §55-67, and a `LEDGER_GLOB` note at line 290 unrelated to boot). No `rev-parse --show-toplevel` in BOOT at all — AEOLUS's boot is unusually bare of tooling.
3. **Proposed insertion:** after line 31 (step 6, channel-liveness check), before line 32. Anchor (occurs once, `grep -c` = 1):
   `7. **Execute the task.**` (line 32) — insert new step **immediately before this line**.
   Proposed label: **`6b.`**
   Proposed text:
   ```
   6b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" AEOLUS` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** none exists (`AGENTS/AEOLUS/boot.py` / `scripts/boot.py` both absent). CLAUDE.md prose IS the whole boot — the line would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **40,813 B** — 🔴 **OVER** the 32,550 B budget (125%).
7. **SPAWNED-MODE card:** **NO** — AEOLUS has no such card; `grep -n "SPAWNED-MODE"` returns nothing. R1 line only needs the one BOOT SEQUENCE insertion.
8. **Dormant/Tier-2:** N/A — AEOLUS is a standing market agent, not Tier-2.

---

## BOND
1. **Boot location:** `## SPAWN PROTOCOL` (`:16`) → `### BOOT (read phase)` at `AGENTS/BOND/CLAUDE.md:22`. Numbering: `0.`–`7.` in BOOT, then `### EXECUTE` unnumbered-header / `8.`, then `### CLOSEOUT` `9.`–`18.`.
2. **Existing shared-script step:** none. No `rev-parse --show-toplevel`, no `ledger_staleness.py`/`orphan_check`/`consumer_check`/`claim_check` anywhere in the file — BOND's boot checks (`docket_check.py`, `boot_recompute.py`, `closeout_check.py`) are all BOND-local `monitors/` scripts, not repo-root `scripts/`. No cwd-proof pattern to sit beside; the insertion needs its own wording (using the template above).
3. **Proposed insertion:** after line 30 (step 7, "Before any KB write..."), before line 32. Anchor (`grep -c` = 1 for the header):
   `### EXECUTE` (line 32) — insert new step immediately before this heading.
   Proposed label: **`7b.`**
   Proposed text:
   ```
   7b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" BOND` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** none exists. CLAUDE.md's numbered prose steps ARE the boot; the line would execute as written (no orchestrator to hide behind).
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **35,513 B** — 🔴 **OVER** budget (109%).
7. **SPAWNED-MODE card:** **NO** — none found.
8. **Dormant/Tier-2:** N/A — standing market agent.

---

## BRENT
1. **Boot location:** `## SPAWN PROTOCOL` (`:20`) → `### BOOT (read phase)` at `AGENTS/BRENT/CLAUDE.md:24`. Numbering: `0.`–`6c.` in BOOT (0,1,2,2b,3,4,5,6,6b,6c), then `### EXECUTE` (deliberately unnumbered — collides with closeout 7), then `### CLOSEOUT` `7.`–`14.`.
2. **Existing shared-script step:** BRENT runs its own `scripts/boot.py` (step 5, line 31-35) as the consolidated orchestrator (six checks). `scripts/ledger_staleness.py` (repo-root) IS wired, but only described inline inside step 5's long note (line 44) as something `boot.py` invokes internally — no separate standalone CLAUDE.md command line for it. No `orphan_check`/`consumer_check`/`claim_check` hits.
3. **Proposed insertion:** after line 53 (step 6c, PENDING-row guard), before line 55. Anchor (`grep -c` = 1):
   `6c. **⏳ PENDING-row guard.** Before reading anything else in the trade surface, **resolve-or-reaffirm every EXECUTION LOG row in \`TRADE.md\` marked PENDING / ⏳.**` (line 53) — insert new step immediately after this line, before `### EXECUTE` (line 55).
   Proposed label: **`6d.`**
   Proposed text:
   ```
   6d. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" BRENT` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** EXISTS (`AGENTS/BRENT/scripts/boot.py`). CLAUDE.md says "Run `scripts/boot.py` — the ONE command" (step 5) and it orchestrates six checks — boot.py is closer to THE boot than one step among many, though steps 0-4/6/6b/6c still run outside it. The R1 line as proposed sits in CLAUDE.md prose (step 6d), NOT inside boot.py — it would execute as written since it's a plain shell command in a numbered CLAUDE.md step, independent of what boot.py itself does.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **37,413 B** — 🔴 **OVER** budget (115%).
7. **SPAWNED-MODE card:** **NO** — `grep -n "SPAWNED-MODE"` returns nothing for BRENT.
8. **Dormant/Tier-2:** N/A — standing market agent.

---

## BROCK
1. **Boot location:** `## SPAWN PROTOCOL` (`:20`) → `### BOOT (read phase)` at `AGENTS/BROCK/CLAUDE.md:28`. Numbering: `0.`–`5.` in BOOT, then `### EXECUTE` `6.`, then `### CLOSEOUT` `6.`(reused)/`7a.`–`12.`.
2. **Existing shared-script step:** YES — step 3 sub-bullet (line 33): `Run \`python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" BROCK --quiet\`` — flags stale non-FROZEN workbook TSVs. This is the cwd-proof pattern to sit beside.
3. **Proposed insertion:** after step 5 (WALTER signal intake block, lines 35-38), before line 40. Anchor (`grep -c` = 1):
   `### EXECUTE` (line 40) — insert new step immediately before this heading.
   Proposed label: **`5b.`**
   Proposed text:
   ```
   5b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" BROCK` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** none exists (`AGENTS/BROCK/boot.py` / `scripts/boot.py` both absent). CLAUDE.md prose IS the boot; would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **21,555 B** — under budget (66%).
7. **SPAWNED-MODE card:** **NO** — none found.
8. **Dormant/Tier-2:** N/A — standing market agent.

---

## CARL
1. **Boot location:** `## SPAWN PROTOCOL` (`:57`) → `### BOOT (read phase)` at `AGENTS/CARL/CLAUDE.md:61`. Numbering: `0.`, `1.`, `1b.`, `2.`–`7.` with `7.0/7a/7b/7c/7d` substeps, then `### EXECUTE` `8.`, then `### CLOSEOUT` `9.`+.
2. **Existing shared-script step:** YES — step **7d** (line 75): `Run \`python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" CARL --quiet\`` — flags stale workbook TSVs. CARL also runs its own `scripts/boot.py` orchestrator at step 7.0 (line 71, covers docket/FRED/market/consistency checks), but that's CARL-local, not the repo-root R1 script.
3. **Proposed insertion:** after step 7d (line 75), before line 77. Anchor (`grep -c` = 1):
   `### EXECUTE` (line 77) — insert new step immediately before this heading.
   Proposed label: **`7e.`**
   Proposed text:
   ```
   7e. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" CARL` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** EXISTS (`AGENTS/CARL/scripts/boot.py`). CLAUDE.md step 7.0 frames it as "Master data pull" covering several sub-checks but explicit standalone steps (7a-7d) still exist as separate numbered items in prose alongside it — boot.py is a component, not the sole boot. The proposed 7e is a plain CLAUDE.md step, independent of boot.py, and would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **33,852 B** — 🔴 **OVER** budget (104%).
7. **SPAWNED-MODE card:** **NO** — none found.
8. **Dormant/Tier-2:** N/A — standing market agent.

---

## CORAL
1. **Boot location:** `## SPAWN PROTOCOL` (`:24`) → `### Boot (read phase — order matters)` at `AGENTS/CORAL/CLAUDE.md:28`. Numbering: `0.`–`9.` (with `6a.`) in Boot, then `### Execute` `10.`, then `### Write-back` `11.`+.
2. **Existing shared-script step:** none — CORAL's own `scripts/boot.py` (step 6a, line 37-40) is CORAL-local (situational card: prices/staleness/mail); no repo-root `scripts/ledger_staleness.py`/`orphan_check`/`consumer_check`/`claim_check` line anywhere in the file.
3. **Proposed insertion:** after step 9 (legacy inbox scan, line 47), before line 49. Anchor (`grep -c` = 1):
   `### Execute` (line 49) — insert new step immediately before this heading.
   Proposed label: **`9b.`**
   Proposed text:
   ```
   9b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" CORAL` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** EXISTS (`AGENTS/CORAL/scripts/boot.py`) but is explicitly ONE step (6a) among nine numbered prose steps, not "the" boot. The proposed 9b runs independently and would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **27,177 B** — under budget (83%).
7. **SPAWNED-MODE card:** **NO** — none found.
8. **Dormant/Tier-2:** N/A — standing market agent.

---

## CREED
1. **Boot location:** `## Canonical Boot Order` at `AGENTS/CREED/CLAUDE.md:77`. Numbering: `0.`–`7.` with `4b.`/`4c.` substeps. Separate `## Closeout Protocol (workbook wiring)` at `:141` uses its own independent `1.`–`9.` numbering (with `8b.`) — **two unrelated numbering sequences in this file; do not conflate.**
2. **Existing shared-script step:** none of the named repo-root scripts (`ledger_staleness.py`/`orphan_check`/`consumer_check.py`/`claim_check.py`) appear anywhere in CREED's CLAUDE.md. CREED has its own local checks instead: `scripts/threshold_scan.py` (boot step 4c, line 85), a bare `find -mtime` staleness one-liner (lines 110-115, cwd-proofed via `rev-parse --show-toplevel`), `scripts/creed_selfcheck.py` (closeout step 8b), and `scripts/boot.py` exists on disk (`AGENTS/CREED/scripts/boot.py`) but is **never mentioned/invoked anywhere in CLAUDE.md text** — worth flagging separately as its own gap, out of scope here.
3. **Proposed insertion:** after step 7 (line 100, "Read `workbook/VX.tsv`... and run the staleness check below"), before the conditional note at line 102 and the `---` at line 104. Anchor (`grep -c` = 1):
   `7. **Read \`AGENTS/CREED/workbook/VX.tsv\`** (the live metric layer — 34 vectors mapped to the Expected Signals) **and run the staleness check below.**` (line 100).
   Proposed label: **`7b.`**
   Proposed text:
   ```
   7b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" CREED` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** EXISTS on disk but CLAUDE.md never references it — Canonical Boot Order is pure numbered prose plus the two named scripts above. The proposed 7b would execute as written; it does not depend on the orphaned boot.py.
5. **Registry dir:** **EXISTS** (`AGENTS/CREED/registry/` — holds `THRESHOLDS.tsv`, `CREED_T_FIRED_LOG.tsv`, etc.). `registry/corrections_receipts.tsv` would be a NEW file added into an already-tracked directory, not a new directory.
6. **File size:** `wc -c` = **31,541 B** — under budget but close (97%, flag as near-cap).
7. **SPAWNED-MODE card:** **NO** — CREED has no such card (it boots via `Canonical Boot Order`, a different pattern from the FALCON/FERT/FLG-style card).
8. **Dormant/Tier-2:** **YES — CREED is Tier-2 (spawn-on-need, explicit "do not spawn without explicit Will permission" in the file header)**. `Canonical Boot Order` is CREED's ONLY boot protocol — there is no separate "spawned as needed" vs "full boot" distinction; every spawn runs the same numbered sequence. The R1 line belongs in that single sequence (step 7b as proposed) — no dual-path split needed. Line 119's calibration note ("staleness between spawns is the expected steady state") suggests any corrections-check ALSO gets that same framing if Will wants a caveat added, but the mechanical rc-contract itself does not change for Tier-2.

---

## CRUISE
1. **Boot location:** `## SPAWN PROTOCOL` at `AGENTS/CRUISE/CLAUDE.md:16`, unheaded numbered list `1.`–`7.` directly under it (no `### BOOT`/`### EXECUTE` sub-headers — CRUISE is the leanest file in this batch).
2. **Existing shared-script step:** **NONE AT ALL** — zero hits for `rev-parse --show-toplevel`, `ledger_staleness.py`, `orphan_check`, `consumer_check.py`, or `claim_check.py` anywhere in the file. CRUISE has no cwd-proof pattern whatsoever to sit beside; the insertion needs fully self-contained wording (using the template above) — CRUISE would be the FIRST cwd-proof shared-script line in this file.
3. **Proposed insertion:** after step 3b (line 23), before step 4 "Execute the task" (line 24). Anchor (`grep -c` = 1):
   `4. **Execute the task**` (line 24) — insert new step immediately before this line.
   Proposed label: **`3c.`**
   Proposed text:
   ```
   3c. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" CRUISE` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** none exists. CLAUDE.md's flat numbered list IS the entire boot; the line would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **12,926 B** — well under budget (40%), smallest file in this batch.
7. **SPAWNED-MODE card:** **NO** — none found.
8. **Dormant/Tier-2:** **YES — CRUISE is a plain domain agent per ROSTER but not called out Tier-2 in its own CLAUDE.md** (the assignment names it as one of the three Tier-2/event-driven desks to check; CRUISE's file itself carries no dormant/event-driven framing — no "spawn on trigger only" language like CREED's). Treat as a standing agent for wiring purposes unless PROME/ROSTER says otherwise — the CLAUDE.md text alone gives no basis for a dual-mode split.

---

## DEWEY
1. **Boot location:** `## BOOT (when Will launches you)` at `AGENTS/DEWEY/CLAUDE.md:149`. Numbering: `1.`–`5.`, then `## EXECUTE` `6.`, then `## CLOSEOUT (write-back tail)` `7.`/`7a.`/`8.`/`8b.`/`8c.`+.
2. **Existing shared-script step:** none of the five named repo-root scripts appear in DEWEY's file. DEWEY's boot uses its own `fred_pull.py`/`edgar_fetch.py` (line 142, not boot-wired, referenced under "YOUR ENGINE") and the `/deep-research` skill — no cwd-proof `rev-parse --show-toplevel` pattern anywhere in BOOT itself (step 1's git-pull instructions reference `git status`/`git log` directly, no rev-parse wrapping).
3. **Proposed insertion:** after step 5 (line 155, "Pick mode... and pick engine..."), before line 157. Anchor (`grep -c` = 1):
   `## EXECUTE` (line 157) — insert new step immediately before this heading.
   Proposed label: **`5b.`**
   Proposed text:
   ```
   5b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" DEWEY` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** none exists (`AGENTS/DEWEY/boot.py` / `scripts/boot.py` both absent). CLAUDE.md's numbered BOOT steps ARE the boot; would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **31,168 B** — under budget but close (96%, flag as near-cap).
7. **SPAWNED-MODE card:** **NO** — none found.
8. **Dormant/Tier-2:** **YES — DEWEY is the fleet's deep-research Tier-2 agent** ("BOOT (when Will launches you)" framing, plus crash-recovery language at step 1 implying irregular/on-demand spawns). There is only ONE boot protocol in the file (no separate "spawned as needed" vs "full" split) — the R1 line belongs in that single sequence (step 5b as proposed).

---

## FALCON
1. **Boot location:** `## SPAWN PROTOCOL` (`:23`) → `### ⚡ SPAWNED-MODE BOOT CARD` (`:27`) → `### BOOT (read phase)` at `AGENTS/FALCON/CLAUDE.md:35`. Numbering: card is `1.`–`5.`; BOOT is `0.`–`7.` with many lettered substeps (`5a`, `5a-2`, `5a-3`, `5b`, `5b-2`, `5b-3`, `5b-4`, `5c`); then `### EXECUTE` `8.`; then `### CLOSEOUT` `9.`+.
2. **Existing shared-script step:** YES — step **5a** (lines 42-46): `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" FALCON --quiet`, PLUS a second widened invocation at step **5a-2** (lines 47-52) with `--glob 'workbook/WARRISK.tsv' --days 7`. Strong existing cwd-proof pattern; FALCON already runs `scripts/ledger_staleness.py` twice.
3. **Proposed insertion:** after step 7 (line 86, web_search sweep — the last BOOT step), before line 88. Anchor (`grep -c` = 1):
   `7. **\`web_search\` for latest developments**...day-by-day gap sweep during active-conflict windows, not topic-shaped searches (LESSONS item 2).` (line 86) — insert new step immediately after, before `### EXECUTE` (line 88).
   Proposed label: **`7b.`**
   Proposed text:
   ```
   7b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" FALCON` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** none exists (`AGENTS/FALCON/boot.py` / `scripts/boot.py` both absent — FALCON's checks are individual scripts, no single orchestrator). CLAUDE.md's numbered BOOT steps ARE the boot; would execute as written.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **45,835 B** — 🔴 **OVER** budget, and the LARGEST file in this batch (141% of budget).
7. **SPAWNED-MODE card:** **YES** — FALCON has a card (lines 27-33) that explicitly lists boot commands: item 2 says *"Run the 3 PortWatch scripts + 2 staleness checks (boot 5a / 5b-2 / 5b-3 / 5b-4 / 5c) — all cwd-proof via `git rev-parse --show-toplevel`."* The R1 line should be **named there too** — the card is a compressed command list and R1 is now a mandatory boot line. Recommend appending it to card item 2's enumeration (or a new card item, e.g. "6.") rather than silently relying on the full BOOT section, since spawned-mode sessions read the card, not full BOOT.
8. **Dormant/Tier-2:** N/A — standing market agent (not one of the Tier-2 desks named in scope, included here as a full desk).

---

## FERT
1. **Boot location:** `## ⚡ SPAWNED-MODE BOOT CARD (coordinator spawns...)` at `AGENTS/FERT/CLAUDE.md:11`, numbered `1.`–`6.`; separate `## BOOT SEQUENCE (full session)` at `:22`, numbered `1.`–`6.` (independent sequence, same numbers reused — do not conflate the two).
2. **Existing shared-script step:** FERT owns a consolidated `AGENTS/FERT/boot.py` (own-dir, not repo-root `scripts/`) invoked at card step 5 (line 17) AND BOOT SEQUENCE step 2 (line 25) — "ledger staleness + predictions-due + triggers-due in one verdict." No repo-root `scripts/ledger_staleness.py`/`orphan_check`/`consumer_check`/`claim_check` line anywhere — FERT's own `boot.py` re-implements the ledger-staleness function locally rather than calling the shared script.
3. **Proposed insertion (full-session sequence):** after step 2 (line 25, the boot.py verdict line), before step 3 (line 26). Anchor (`grep -c` = 1):
   `3. Process \`inbox/\` per \`inbox/PROTOCOL.md\` (INTEGRATE / LOG / DISCARD; move to \`inbox/processed/\`).` (line 26) — insert new step immediately before this line.
   Proposed label: **`2b.`**
   Proposed text:
   ```
   2b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" FERT` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
   **Also propose adding to the SPAWNED-MODE BOOT CARD** (see item 7) as a new card step, since the card is the fast path a coordinator spawn actually reads.
4. **boot.py:** EXISTS (`AGENTS/FERT/boot.py`) and IS explicitly named as THE consolidated boot verdict in both the card (step 5) and full sequence (step 2) — "Freshness gate: run `python3 .../AGENTS/FERT/boot.py`". This is the closest thing to "boot.py as THE boot" in this batch. The proposed R1 line (2b) is a SEPARATE plain shell command in CLAUDE.md prose, not inside boot.py — it would execute as written regardless of boot.py's own internal logic; it does not ride on boot.py picking it up.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **17,236 B** — well under budget (53%).
7. **SPAWNED-MODE card:** **YES** — card explicitly lists boot commands (step 5, "Freshness gate" line 17, the `boot.py` invocation). R1 should be named there too. Recommend a new card step **"7."** (card currently ends at 6):
   ```
   7. **R1 corrections check:** run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" FERT` — rc=1 blocks on a NAMED unreceipted correction.
   ```
8. **Dormant/Tier-2:** **YES — FERT is explicitly EVENT-DRIVEN SPECIALIST class** (header line 3: "wakes on named triggers, not standing cadence"). There is only ONE boot protocol beyond the card/full-session split (both run the same checks) — no separate "light" vs "full" distinction exists; the R1 line belongs in the full BOOT SEQUENCE (2b) and is also worth surfacing in the card per item 7, since FERT is frequently spawned via the card path (coordinator spawns), not a from-scratch session.

---

## FLG
1. **Boot location:** `## ⚡ SPAWNED-MODE BOOT CARD (coordinator spawns...)` at `AGENTS/FLG/CLAUDE.md:11`, numbered `1.`–`6.`; separate `## BOOT SEQUENCE (full session)` at `:22`, numbered `1.`–`6.` — identical structure to FERT (FLG was built off the same blueprint pattern).
2. **Existing shared-script step:** same pattern as FERT — own `AGENTS/FLG/boot.py` (card step 5, line 17; full-sequence step 2, line 25) covers "ledger staleness + predictions-due + triggers-due + quarter-due scan" locally. No repo-root `scripts/ledger_staleness.py`/`orphan_check`/`consumer_check`/`claim_check` line anywhere in the file.
3. **Proposed insertion (full-session sequence):** after step 2 (line 25), before step 3 (line 26). Anchor (`grep -c` = 1):
   `3. Process \`inbox/\` per \`inbox/PROTOCOL.md\` (INTEGRATE / LOG / DISCARD; \`git mv\` to \`inbox/processed/\`).` (line 26) — insert new step immediately before this line.
   Proposed label: **`2b.`**
   Proposed text:
   ```
   2b. **R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17).** Run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" FLG` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted — read the pointer, then `--receipt <id> --action APPLIED|NO-OP|DEFERRED|CONTESTED` and commit `registry/corrections_receipts.tsv`).
   ```
4. **boot.py:** EXISTS (`AGENTS/FLG/boot.py`), same "THE freshness gate" framing as FERT (card step 5 + full-sequence step 2). The proposed 2b is a separate CLAUDE.md prose line and would execute independently of boot.py.
5. **Registry dir:** does not exist — created on first `--receipt`.
6. **File size:** `wc -c` = **23,097 B** — under budget (71%).
7. **SPAWNED-MODE card:** **YES** — same as FERT, card names the boot.py freshness-gate command (step 5). Recommend the same new card step **"7."**:
   ```
   7. **R1 corrections check:** run `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" FLG` — rc=1 blocks on a NAMED unreceipted correction.
   ```
8. **Dormant/Tier-2:** **YES — FLG is PRINT-DRIVEN SINGLE-NAME SPECIALIST class** (header line 3: "wakes on filings and named triggers, not standing cadence"), the fleet's first greenfield per-bank build (2026-08-20). Same single-protocol structure as FERT — no light/full split; R1 belongs in full BOOT SEQUENCE (2b) and the card (item 7).

---

## Summary table

| Desk | Anchor line# (file) | Proposed label | registry/ exists | CLAUDE.md bytes | vs 32,550B budget | Card exists? Add R1 there? |
|---|---|---|---|---|---|---|
| AEOLUS | 32 (before `7. Execute the task.`) | `6b.` | NO | 40,813 | 🔴 125% | NO card |
| BOND | 32 (before `### EXECUTE`) | `7b.` | NO | 35,513 | 🔴 109% | NO card |
| BRENT | 53 (after step 6c, before `### EXECUTE`@55) | `6d.` | NO | 37,413 | 🔴 115% | NO card |
| BROCK | 40 (before `### EXECUTE`) | `5b.` | NO | 21,555 | 66% | NO card |
| CARL | 77 (before `### EXECUTE`) | `7e.` | NO | 33,852 | 🔴 104% | NO card |
| CORAL | 49 (before `### Execute`) | `9b.` | NO | 27,177 | 83% | NO card |
| CREED | 100 (after step 7, before line 102 note) | `7b.` | **YES** | 31,541 | 97% (near) | NO card |
| CRUISE | 24 (before `4. Execute the task`) | `3c.` | NO | 12,926 | 40% | NO card |
| DEWEY | 157 (before `## EXECUTE`) | `5b.` | NO | 31,168 | 96% (near) | NO card |
| FALCON | 86 (after step 7, before `### EXECUTE`@88) | `7b.` | NO | 45,835 | 🔴 141% (largest) | **YES** — add to card item 2 |
| FERT | 25 (after step 2, before step 3@26 in BOOT SEQUENCE) | `2b.` (+ card `7.`) | NO | 17,236 | 53% | **YES** — add new card step 7 |
| FLG | 25 (after step 2, before step 3@26 in BOOT SEQUENCE) | `2b.` (+ card `7.`) | NO | 23,097 | 71% | **YES** — add new card step 7 |

**Desks with NO safe unique anchor found:** none — all 12 desks had at least one uniquely-occurring (`grep -c` = 1) anchor line verified by direct grep.

**Notable off-scope findings surfaced in passing (not acted on, flagging for the batch owner):** CREED has `AGENTS/CREED/scripts/boot.py` on disk but it is never referenced anywhere in CREED's `CLAUDE.md` — orphaned tool, separate issue from R1 wiring.
