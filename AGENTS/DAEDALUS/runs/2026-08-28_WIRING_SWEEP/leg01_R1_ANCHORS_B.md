# Leg ① — R1 corrections boot-leg wiring: desk survey B
**Reader scope:** HANS HAWK HENRY HOMER LABOR LIQUID MARCO MIDAS NEXUS ORACLE OSPREY OTTO
**Method:** read-only. Every claim carries file:line. No files outside this runs/ dir touched.

Wording base (verbatim quote, adapt `<NAME>`):
> `AGENTS/DAEDALUS/CLAUDE.md:42` — `5b. **R1 corrections check** — \`python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" DAEDALUS\` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then \`--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>\` + commit your receipts file).`

Blueprint canon: `AGENTS/DAEDALUS/BLUEPRINTS/market-agent.md:112` (the "R1 corrections boot leg (REQUIRED...)" bullet).

---

## HANS

1. **Boot location:** `## SPAWN PROTOCOL` (`AGENTS/HANS/CLAUDE.md:20`) — flat, unlettered 3-step list (`1.`/`2.`/`3.`, no sub-letters anywhere in the file). No SPAWNED-MODE card, no BOOT/CLOSEOUT split.
2. **Existing shared-script step:** NONE. Zero hits for `rev-parse --show-toplevel`, `ledger_staleness.py`, `orphan_check`, `consumer_check.py`, `claim_check.py` anywhere in the file — HANS runs no shared `scripts/` tool at all today.
3. **Proposed insertion:** insert AFTER line 22 (`1. **Read \`STATUS.md\`** — current European macro state, PMI readings, ECB stance, stale-data warnings`), BEFORE line 23 (`2. **Execute the task**`). Verified unique: `grep -c` on line 22's text = 1.
   - Label: **`1a.`**
   - Text (≤2 lines):
     ```
     1a. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" HANS` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/HANS/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** none exists (`ls AGENTS/HANS/boot.py` → no such file; no `scripts/` dir at all — dir listing is `CLAUDE.md COMPLETED_RP-HANS-1.txt LAST_COMPLETION.md REVIVAL_PLAN_2026-06-22.md STATUS.md domain inbox outbox prompts reports research sources workbook`). CLAUDE.md's 3-step prose IS the entire boot — a session following it verbatim would execute the new line.
5. **Registry dir:** does not exist.
6. **File size:** 7,132 B — far under 32,550 B, no flag.
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** HANS is Tier-2, revival-flagged (`CLAUDE.md:14` "2026-06-22 revival warning"). Boot protocol has **no** spawned-vs-full distinction — it is one flat 3-step sequence regardless of how HANS is invoked, so the R1 line belongs in that single sequence (no alternate "full boot" surface exists to choose between). **Last HANS-authored commit:** `2026-07-16 13:54:19 -0400` — "HANS 7/16: close sweep lens-1 remainder…" (`git log --format="%ci %s" -- AGENTS/HANS/` filtered to subject-line `HANS …`). That is **43 days** before today (2026-08-28), not the ~34d cited in the task brief — flagging the discrepancy rather than silently reconciling it. All *other* commits touching `AGENTS/HANS/` since then are PROME/WALTER routing-stub drops (2026-08-18 through 2026-08-21), not HANS sessions.

---

## HAWK

1. **Boot location:** `### BOOT (read phase)` under `## SPAWN PROTOCOL` (`AGENTS/HAWK/CLAUDE.md:35,39`). Numbering style: `0.`–`8.` with lettered sub-steps (`6a`, `6b`, `7a/b/c`); `### EXECUTE` at step 9; `### CLOSEOUT` at steps 10–16.
2. **Existing shared-script step:** `AGENTS/HAWK/CLAUDE.md:47` —
   `6a. **Ledger staleness check** — run \`python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" HAWK --quiet\`; surface any ⚠️ stale-ledger alert and freeze-or-refresh it at closeout (root CLAUDE.md Data Hygiene).`
3. **Proposed insertion:** AFTER line 47 (step 6a, quoted above), BEFORE line 48 (`6b. **Dormant-book re-sweep check**…`). Verified unique via `grep -cF '6a. **Ledger staleness check**'` = 1.
   - Label: **`6a-2`** (mirrors the fleet's existing `5a-2` convention used by OSPREY/FALCON for a second check riding the same anchor step).
   - Text:
     ```
     6a-2. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" HAWK` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/HAWK/registry/corrections_receipts.tsv`).
     ```
   - Alternative if the reviewer prefers not to wedge between 6a/6b: append as `6c` immediately after 6b (line 48) instead — both are safe, unique anchors.
4. **boot.py:** exists at `AGENTS/HAWK/scripts/boot.py` but is explicitly **FROZEN and dead** — `AGENTS/HAWK/CLAUDE.md:237` states its `BOOT_SEQUENCE` literal "is **not reachable** — nothing invokes this wrapper, and HAWK's boot steps 0-8 call no script but `ledger_staleness.py`." HAWK's real boot is 100% prose steps 0–8; a session following CLAUDE.md verbatim would execute the new line with zero boot.py interaction.
5. **Registry dir:** does not exist.
6. **File size:** 33,653 B — **≥32,550 B, FLAG.**
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable to HAWK (core active desk, not in the Tier-2/dormant set named in the brief).

---

## HENRY

1. **Boot location:** `## SPAWN PROTOCOL` → `### Boot (read phase — this order matters)` (`AGENTS/HENRY/CLAUDE.md:24,26`). Numbering: `1.`–`3.` then lettered `3a`–`3d`, then `### Execute` (`4.`), `### Write-back` (`5.`–`10.`).
2. **Existing shared-script step:** NONE of the named shared scripts (`ledger_staleness.py`/`orphan_check`/`consumer_check.py`/`claim_check.py`) appear anywhere in the file. The only `rev-parse --show-toplevel` hit is line 35 (step 3c), which invokes HENRY's **own** `AGENTS/HENRY/scripts/boot.py` (gamma flip, credit monitor, predictions-due) — not a repo-root shared tool.
3. **Proposed insertion:** AFTER line 41 (end of step 3d's block — text ends "...The detector was never the gap — the obligation was."), BEFORE line 43 (`### Execute`). Verified unique via full-line match on line 41 = 1 hit.
   - Label: **`3e.`**
   - Text:
     ```
     3e. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" HENRY` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/HENRY/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** exists (`AGENTS/HENRY/scripts/boot.py`), invoked at step 3c as one orchestrator sub-step among several manual prose steps (1, 2, 3, 3a, 3b, 3d). Not "the whole boot" — CLAUDE.md's own numbered sequence is what a session executes, so the new prose step 3e will run regardless of boot.py's contents.
5. **Registry dir:** does not exist.
6. **File size:** 32,007 B — under 32,550 B (543 B of headroom), **no flag**, but close enough to note.
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set).

---

## HOMER

1. **Boot location:** `## BOOT (standalone — root \`CLAUDE.md\` owns the fleet-wide protocol; this is HOMER's sequence through it)` (`AGENTS/HOMER/CLAUDE.md:200`). Flat numbering `1.`–`11.`, no sub-letters in BOOT; separate `## CLOSEOUT` section numbered `1.`–`6.` (with `1b`/`1c`/`5b` sub-steps).
2. **Existing shared-script step:** `AGENTS/HOMER/CLAUDE.md:211-212` —
   ```
   6. Staleness check (cwd-proof, PAT-031):
      `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" HOMER --quiet`
   ```
3. **Proposed insertion:** AFTER line 212 (the ledger_staleness command), BEFORE line 213 (`7. Workbook staleness eyeball: ...`). Verified unique via `grep -cF` on the exact command line = 1.
   - Label: **`6a.`**
   - Text:
     ```
     6a. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" HOMER` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/HOMER/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** does not exist — no `scripts/` dir under `AGENTS/HOMER/` at all (dir listing: `CLAUDE.md LESSONS.md MEMORY.md NEXUS_BRIEF.md SCRATCH.md STATUS.md archive board_log.tsv docket domain inbox outbox reports state_vectors thesis workbook`). Boot is pure prose calling the shared script directly — the new line will run exactly as written.
5. **Registry dir:** does not exist.
6. **File size:** 48,824 B — **≥32,550 B, FLAG** (well over — HOMER already runs its own byte-tier discipline internally, unrelated to DAEDALUS's cap, but worth noting for the batch).
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set; HOMER is a full active promoted agent).

---

## LABOR

1. **Boot location:** `## SPAWN PROTOCOL` → `### BOOT (read phase)` (`AGENTS/LABOR/CLAUDE.md:35,39`). Numbering: `B0`–`B6` (lettered-prefix scheme, sub-steps `B2a`, `B5a`, `B5b`), `### EXECUTE` (`B6`), `### CLOSEOUT` (`C1`–`C6`). LABOR ALSO has a separate `## SPAWNED-MODE BOOT CARD` at the top (`:18`) with its own flat `1.`–`5.` numbering (see item 7).
2. **Existing shared-script step:** NONE of `ledger_staleness.py`/`orphan_check`/`consumer_check.py`(as a boot step)/`claim_check.py` run at boot. `consumer_check.py` appears only in a FILES-table doc-comment (`:279`, describing `PUBLISHED.tsv`, not a boot invocation). LABOR's boot-time freshness gate is its own `scripts/boot.py` (B2, line 44) + `spine_check.py`, not a shared root-level staleness tool.
3. **Proposed insertion:** AFTER line 67 (end of B5b's block — text ends "...that is the summons gap (`BUILD_DEBT.md` BD-02 + the external CATALYSTS-driven alert PROME owns)."), BEFORE line 69 (`### EXECUTE`). Verified unique via full-line match = 1.
   - Label: **`B5c.`**
   - Text:
     ```
     B5c. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" LABOR` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/LABOR/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** exists (`AGENTS/LABOR/scripts/boot.py`), invoked at B2 as one orchestrator sub-step among many manual prose steps (B0, B1, B3, B4, B5, B5a, B5b). Not the whole boot — new prose step B5c executes independently.
5. **Registry dir:** does not exist.
6. **File size:** 49,879 B — **≥32,550 B, FLAG.**
7. **SPAWNED-MODE card:** **YES, present** (`AGENTS/LABOR/CLAUDE.md:18-31`) — "This `CLAUDE.md` does **not** auto-load when PROME spawns you from another cwd." Its 5 numbered lines are: `1.` read STATUS+task packet+LESSONS; `1a.` scan `inbox/`+`inbox/WALTER/`; `1b.` unconsumed dated-artifact check; `2.` FRESHNESS GATE (`boot.py --verbose` / fetch.py FRED); `3.` Git (cwd-proof, pathspec, no-push-when-spawned); `4.` DELIVER BEFORE IDLE; `5.`/`5a.` closeout-if-state-changing + NEXUS_BRIEF re-pin declaration. **Recommend YES, the R1 line should also be named there** — this card is explicitly the "minimum viable boot for a scoped/spawned task," and LABOR is one of the fleet's most frequently PROME-spawned desks (per its own card and the root CLAUDE.md carve-out language), so a spawned LABOR session that never reads past the card would otherwise never run R1 at all. Propose adding as a new numbered line (e.g. `1c.`) immediately after `1b.` (the other "owed work outranks the task" check), reusing the same ≤2-line text as B5c above.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set).

---

## LIQUID

1. **Boot location:** `## SPAWN PROTOCOL` (`AGENTS/LIQUID/CLAUDE.md:18`) — flat numbering `0.`–`6.` with one lettered sub-step (`1b`), no `### BOOT`/`### EXECUTE` sub-headings (single flowing list; step 3 is "Execute the task").
2. **Existing shared-script step:** NONE of the named shared scripts run at boot. The only `rev-parse --show-toplevel` hit (`:24`, step 1b) invokes LIQUID's own `AGENTS/LIQUID/scripts/boot.py` (FRED/yfinance dashboards + catalyst countdown + predictions due-scan) — not a repo-root shared tool.
3. **Proposed insertion:** AFTER line 28 (end of step 2, WALTER intake — last line "Do not use bash `mv`; use `git mv`... Spec: ... v0.2."), BEFORE line 29 (`3. **Execute the task** — ...`). Verified unique via full-line match = 1.
   - Label: **`2a.`**
   - Text:
     ```
     2a. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" LIQUID` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/LIQUID/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** exists (`AGENTS/LIQUID/scripts/boot.py`), invoked at step 1b as one component of the boot list (steps 0, 1, 2 remain manual/prose). New step 2a runs as ordinary prose regardless.
5. **Registry dir:** does not exist.
6. **File size:** 26,481 B — under cap, no flag.
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set).

---

## MARCO

1. **Boot location:** `## SPAWN PROTOCOL` → `### Boot (read phase)` (`AGENTS/MARCO/CLAUDE.md:18,22`), numbered `1.`–`4.`; a separate unnumbered `### WALTER signal intake` subsection (its own internal `1.`–`3.`) runs after boot-read and before `### Execute` (`5.`); `### Closeout` follows (`6.`+).
2. **Existing shared-script step:** NONE of the named shared scripts run at boot. Two `rev-parse --show-toplevel` hits: line 26 (MARCO's own `scripts/boot.py` — catalyst/predictions/STATUS-VX staleness) and line 27 (MARCO's own `tools/fl_migration_proxies.py`) — both agent-local, not repo-root shared tools.
3. **Proposed insertion:** AFTER line 44 (last line of the WALTER-intake subsection — "⚠️ **This lane is exempt from the \"do NOT process inbox on normal spawns\" MAIL rule below.**..."), BEFORE line 46 (`### Execute`). Verified unique via `grep -cF` = 1.
   - Label: **`4b.`** (sits after boot step 4 / the WALTER intake block, before Execute's step 5 — numbered to slot ahead of "5. Execute the task" without renumbering it)
   - Text:
     ```
     4b. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" MARCO` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/MARCO/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** exists (`AGENTS/MARCO/scripts/boot.py`), invoked at step 4 as one boot component (steps 1-3 + WALTER intake remain manual). New prose step 4b runs independently.
5. **Registry dir:** does not exist.
6. **File size:** 25,982 B — under cap, no flag.
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set).

---

## MIDAS

1. **Boot location:** `## BOOT SEQUENCE (when spawned)` (`AGENTS/MIDAS/CLAUDE.md:28`) — flat numbering `1.`–`8.`, no sub-letters, no BOOT/EXECUTE sub-headings; a separate `## CLOSEOUT PROTOCOL (before idle)` follows with its own `1.`–`5.`.
2. **Existing shared-script step:** `AGENTS/MIDAS/CLAUDE.md:33` —
   `4. **Run \`boot.py\`** — \`python3 "$(git rev-parse --show-toplevel)/AGENTS/MIDAS/boot.py"\` — ledger staleness + predictions-due. rc 0 = quiet · 1 = a prediction is due (REVIEW) · 2 = a leg failed.`
   Note: this is MIDAS's own `boot.py` (agent-local, at `AGENTS/MIDAS/boot.py` — the one desk of the 12 with a top-level boot.py rather than a `scripts/` subdir one), which itself does ledger-staleness-style checking; it is not the shared repo-root `scripts/ledger_staleness.py` and is unrelated to the R1 corrections script.
3. **Proposed insertion:** AFTER line 33 (step 4, quoted above), BEFORE line 34 (`5. **Resolve predictions**...`). Verified unique via `grep -cF` on the step-4 opener = 1.
   - Label: **`4b.`**
   - Text:
     ```
     4b. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" MIDAS` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/MIDAS/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** exists at `AGENTS/MIDAS/boot.py` (top-level, not `scripts/`), invoked at step 4 of 8 — the most script-driven of the 12 boots, but still only one step among manual reads (SCRATCH, STATUS), a predictions-resolve step, inbox processing, and the channel-liveness check. CLAUDE.md's own numbered list is what a session executes; the new step 4b runs on its own.
5. **Registry dir:** does not exist.
6. **File size:** 15,785 B — under cap, no flag.
7. **SPAWNED-MODE card:** none present (MIDAS's "BOOT SEQUENCE (when spawned)" heading covers ALL spawns, not a separate minimal card — no split to reconcile). N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set — MIDAS is a DAEDALUS-built core utility/market agent).

---

## NEXUS

1. **Boot location:** `## SPAWN PROTOCOL` → `### BOOT` (`AGENTS/NEXUS/CLAUDE.md:28,30`), numbered `1.`–`7.` (no lettered sub-steps in BOOT); `### LIVE-EVENT OVERRIDE` note follows; then `### EXECUTE` (`8.`); `### CLOSEOUT (write-back tail)` (`9.`–`16.`, with `9a/9b/9c`).
2. **Existing shared-script step:** NONE. NEXUS runs no boot.py and no shared repo-root script at boot at all — it is a pure-synthesis desk whose "freshness" mechanism is the in-house `git log -1 --format=%ci` fleet-wide scan (step 6's "Multi-day re-anchor" sub-bullet, `:44`), not a `scripts/` tool.
3. **Proposed insertion:** AFTER line 48 (end of step 7, WALTER intake — "...Spec: `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.2."), BEFORE line 50 (`### LIVE-EVENT OVERRIDE`). Verified: `grep -n "^7. \*\*WALTER signal intake"` = exactly one hit (step-7 header); the block's last line (line 48) was also spot-checked and is a stock WALTER-lane closer shared verbatim with several other desks' step text — treat as unique-in-file (it is; no duplicate WALTER-lane block exists elsewhere in NEXUS's CLAUDE.md) rather than unique-across-fleet.
   - Label: **`7a.`**
   - Text:
     ```
     7a. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" NEXUS` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/NEXUS/registry/corrections_receipts.tsv`).
     ```
   - ⚠️ **Note for the batch author:** as placed, `7a` falls just before `### LIVE-EVENT OVERRIDE` (`:50-51`), which "short-circuit[s] BOOT steps 2-6" on a live tier-1 event and does not mention step 7/7a at all — meaning under that override NEXUS's WALTER intake (7) and the new R1 check (7a) are both implicitly skipped that pass, deferred to "full BOOT on next pass." This mirrors how step 7 already behaves today; flagging only so the override text isn't read as silently exempting 7a from the same treatment as 7.
4. **boot.py:** does not exist for NEXUS (no `scripts/` dir, no top-level boot.py). Boot is 100% prose; the new line executes exactly as written by a session following the numbered steps.
5. **Registry dir:** does not exist.
6. **File size:** 50,239 B — **≥32,550 B, FLAG** (largest of the 12).
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** NEXUS is the fleet's utility **synthesis** desk (explicitly named in the brief). Its boot has no spawned-vs-full split — one `### BOOT` sequence serves every invocation, with `### LIVE-EVENT OVERRIDE` as the only alternate path (see the ⚠️ above). The R1 line belongs in the standard BOOT sequence at 7a; there is no separate "full boot" surface to choose between.

---

## ORACLE

1. **Boot location:** `## SPAWN PROTOCOL` → `### BOOT (read phase)` (`AGENTS/ORACLE/CLAUDE.md:24,28`), numbered `1.`–`6.`, no lettered sub-steps; `### EXECUTE` (`7.`); `### CLOSEOUT` (`8.`–`14.`).
2. **Existing shared-script step:** NONE of the named shared scripts run at boot. All three `rev-parse --show-toplevel` hits (`:207,208,215`) are inside the DOMAIN SCOPE / market-fetcher documentation further down the file (`polymarket.py`, `kalshi.py` — ORACLE's own `scripts/`), not boot-sequence lines.
3. **Proposed insertion:** AFTER line 35 (step 6 — "...**Run \`tools/metrics.py\`, never hand-compute a σ**..."), BEFORE line 37 (`### EXECUTE`). Verified unique via full-line match = 1.
   - Label: **`6a.`**
   - Text:
     ```
     6a. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" ORACLE` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/ORACLE/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** does not exist (no orchestrator; ORACLE's `scripts/` holds standalone fetchers `polymarket.py`/`kalshi.py`, run individually at EXECUTE, not at boot). Boot is pure prose; new line executes as written.
5. **Registry dir:** does not exist.
6. **File size:** 26,250 B — under cap, no flag.
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set).

---

## OSPREY

1. **Boot location:** `## SPAWN PROTOCOL` → `### BOOT (read phase)` (`AGENTS/OSPREY/CLAUDE.md:23,27`), numbered `0.`–`8.` with lettered sub-steps (`5a`, `5a-2`, `5b`, `6a/b/c`); `### EXECUTE` (`8.` — note OSPREY's numbering re-uses `8` for both the last boot-adjacent line and EXECUTE, see raw file); `### CLOSEOUT` (`9.`–`15.`).
2. **Existing shared-script step:** TWO, both ledger-staleness family:
   - `AGENTS/OSPREY/CLAUDE.md:34` — `5a. **Ledger staleness check (workbook)** — cwd-proof: \`python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" OSPREY --quiet\`; surface any ⚠️ alert and freeze-or-refresh at closeout (root CLAUDE.md Data Hygiene).`
   - `AGENTS/OSPREY/CLAUDE.md:35` — `5a-2. **War-risk staleness check at a TIGHT bar**...` (same shared script, `--glob 'workbook/WARRISK.tsv' --days 7`).
   Line 36 (`5b`) is a **different**, OSPREY-manual, non-shared-script check (`domain/energy-strikes/STRIKES.tsv` in-content-date check) — not a `scripts/` invocation.
3. **Proposed insertion:** AFTER line 35 (5a-2, the second ledger_staleness invocation — full text ends "...check the **TD6 continuous proxy** as the tripwire for when to look."), BEFORE line 36 (`5b. **Strike-ledger staleness check**...`). Verified unique via full-line grep on the 5a-2 closing text = 1.
   - Label: **`5a-3.`** (extends OSPREY's own `5a`/`5a-2` numbering family, keeping it grouped with the other two shared-script staleness checks and ahead of the unrelated manual 5b strike-ledger check)
   - Text:
     ```
     5a-3. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" OSPREY` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/OSPREY/registry/corrections_receipts.tsv`).
     ```
4. **boot.py:** does not exist — no `scripts/` dir under `AGENTS/OSPREY/` (dir listing: `CLAUDE.md LESSONS.md MEMORY.md NEXUS_BRIEF.md SCRATCH.md SOURCES.md STATUS.md board_log.tsv domain inbox outbox proposals reports research templates thesis workbook`). Boot calls the shared script directly, no orchestrator layer; the new line runs exactly as written.
5. **Registry dir:** does not exist.
6. **File size:** 34,971 B — **≥32,550 B, FLAG.**
7. **SPAWNED-MODE card:** none present. N/A.
8. **Tier-2/dormant:** not applicable (not in the named Tier-2/dormant set — OSPREY is a full theater-tracking desk).

---

## OTTO

1. **Boot location:** `## Startup Protocol` (`AGENTS/OTTO/CLAUDE.md:68`) — flat numbering `0.`–`6.`, no lettered sub-steps in Startup; `## Closing Protocol` (`:125`) uses `1.`–`8.` with sub-steps (`1a`, `1b`, `7a`, `7b`).
2. **Existing shared-script step:** NONE of the named shared scripts (`ledger_staleness.py`/`orphan_check`/`consumer_check.py`/`claim_check.py`) run at boot. The one `rev-parse --show-toplevel` hit (`:88`, step 4) invokes OTTO's own `AGENTS/OTTO/scripts/boot.py` (predictions scan + price snapshot), not a repo-root shared tool.
3. **Proposed insertion:** AFTER line 103 (end of step 5, calendar scan — "...awaiting external resolution — note days-since but don't re-flag as a miss)."), BEFORE line 104 (`6. **Report**...`). Verified unique via `grep -cF` = 1.
   - Label: **`5a.`**
   - Text:
     ```
     5a. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" OTTO` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file at `AGENTS/OTTO/registry/corrections_receipts.tsv`).
     ```
   - Caution: OTTO's own boot doc says step order is deliberate — "This order matters — it ends on the action items and the time-sensitive scan" (`:70-72`). Inserting 5a between step 5 and step 6 (Report) is safe because Report is a synthesis/output step, not a read step — it does not change what gets read last, only adds one more cheap mechanical check before the report is composed.
4. **boot.py:** exists (`AGENTS/OTTO/scripts/boot.py`), invoked at step 4 as one component of the numbered Startup Protocol (steps 0,1,2,3,5,6 remain manual/prose). New step 5a runs independently of boot.py.
5. **Registry dir:** does not exist.
6. **File size:** 37,922 B — **≥32,550 B, FLAG.**
7. **SPAWNED-MODE card:** none present (OTTO's "Startup Protocol" is the only boot surface, used for every spawn — "If the task is specific... go direct after step 1" is a shortcut inside the SAME protocol, not a separate card). N/A.
8. **Tier-2/dormant:** OTTO is Tier-2 per the brief but is clearly a **live, heavily-active** desk (large CLAUDE.md, rich `scripts/`, frequent-looking closeout machinery) — nothing here suggests dormancy. Its Startup Protocol has no spawned-vs-full split (unlike LABOR's separate SPAWNED-MODE card); one sequence serves every boot, so 5a is the only sensible placement.

---

## Summary table

| Desk | Anchor line# (insert after) | New label | registry/ exists | CLAUDE.md bytes | ≥32,550B flag | SPAWNED-MODE card |
|---|---|---|---|---|---|---|
| HANS | `CLAUDE.md:22` | `1a` | NO | 7,132 | no | NO |
| HAWK | `CLAUDE.md:47` | `6a-2` | NO | 33,653 | **YES** | NO |
| HENRY | `CLAUDE.md:41` | `3e` | NO | 32,007 | no (543B under) | NO |
| HOMER | `CLAUDE.md:212` | `6a` | NO | 48,824 | **YES** | NO |
| LABOR | `CLAUDE.md:67` (+ card line `~24`, new `1c`) | `B5c` (+ card `1c`) | NO | 49,879 | **YES** | **YES — recommend adding there too** |
| LIQUID | `CLAUDE.md:28` | `2a` | NO | 26,481 | no | NO |
| MARCO | `CLAUDE.md:44` | `4b` | NO | 25,982 | no | NO |
| MIDAS | `CLAUDE.md:33` | `4b` | NO | 15,785 | no | NO |
| NEXUS | `CLAUDE.md:48` | `7a` | NO | 50,239 | **YES** | NO |
| ORACLE | `CLAUDE.md:35` | `6a` | NO | 26,250 | no | NO |
| OSPREY | `CLAUDE.md:35` | `5a-3` | NO | 34,971 | **YES** | NO |
| OTTO | `CLAUDE.md:103` | `5a` | NO | 37,922 | **YES** | NO |

**Desks with no safe unique anchor found:** none — all 12 have a verified-unique (`grep -c` = 1) insertion anchor.

**Cross-cutting observations for the batch author:**
- **Zero of the 12 have a `registry/` directory today** — every one of these desks' first R1 receipt (on an rc=1) will need `AGENTS/<NAME>/registry/corrections_receipts.tsv` created from scratch. Not a wiring blocker, just a shared first-use cost across the whole batch.
- **6 of 12 exceed DAEDALUS's own STATUS.md-style 32,550 B budget** (HAWK, HOMER, LABOR, NEXUS, OSPREY, OTTO) — that budget is DAEDALUS-specific (`AGENTS/DAEDALUS/CLAUDE.md` OUTPUT RULES), not a fleet-wide cap on other desks' CLAUDE.md files, so this is informational, not a defect to fix in this leg.
- **Only LABOR has a SPAWNED-MODE BOOT CARD** among these 12; it is also the only desk where a spawned session might skip the full-protocol R1 line entirely if the card isn't updated too.
- **No desk in this batch runs the shared `orphan_check`/`consumer_check.py`/`claim_check.py` scripts from CLAUDE.md boot text** — root canon wires those at closeout, conditionally, not boot; irrelevant to this leg but confirms no naming collision with existing lettered closeout steps of the same shape (e.g. LABOR's C-series, HOMER's closeout `1b/1c/5b`).
