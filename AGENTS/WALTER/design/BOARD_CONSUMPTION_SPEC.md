# BOARD Delivery + Consumption Spec

**Version:** v0.2
**Created:** 2026-04-20 (v0.1 consumption-only) · **Extended:** 2026-06-17 (v0.2 delivery layer)
**Owner:** WALTER
**Status:** **Delivery layer = Phase 1, ships now.** Consumption = Phase 2, time-boxed (see §8). Approved-in-principle by Will + PROME + ORC ("WALTER Routing v2 — Final Design Packet", 2026-06-17).

---

## 0. Why v0.2 exists — "in BOARD" ≠ "received"

v0.1 defined a *consumption* mechanism (`board_log.tsv` + a recipient boot-step that scans `/BOARD/INDEX.md`). It shipped, but propagation to agent boot docs stalled ~2 months → BOARD became **write-only**. The prototype failure: **SIG-W-20260610-001 (BRENT action) + -002 (HAWK action) were correctly published to BOARD but delivered to nobody's inbox** — both were BOARD-only per the Apr-14 delivery policy, and the recipients had no working pull. The miss was *structural*, not a one-off: it was true for every IMMEDIATE/PRIORITY signal.

v0.2 adds a real **delivery layer** (a per-recipient handoff file WALTER actively creates) and a **phased-but-time-boxed** consumption rollout, with **telemetry shipping immediately** so the Phase-2 gap can't rot silently the way v0.1's did.

---

## 1. State vocabulary — published / delivered / consumed

Three orthogonal delivery states. **These are distinct from the signal-validity lifecycle** (`status:` = SUPERSEDED / FALSIFIED / EVENT-PASSED, FORMAT_SPEC v0.10) — do **not** overload the `status:` field to carry delivery state. Track delivery via file location + the WALTER-side `delivery_log.tsv`.

| State | Definition |
|-------|-----------|
| **published** | Signal file in `/BOARD/` + a row in `/BOARD/INDEX.md`. (Unchanged from today.) |
| **delivered** | Handoff file exists where the recipient will actually read it — **platform-dependent**, see §3. |
| **consumed** | Recipient processed it: logged a disposition in its `board_log.tsv` **and** moved the handoff file to `inbox/WALTER/processed/`. |

**Reporting discipline:** never report "routed to AGENT" on *published* alone; never claim *consumed* until recipient-side processing exists. WALTER can assert *published* and *delivered* (the latter via §3's git-derived check); only the recipient can assert *consumed*.

---

## 2. The BOARD stays as-is

BOARD remains the permanent archive + discovery index, **unchanged**. Every route writes a full-but-minimal BOARD entry (signal file + one INDEX row + `route_log.tsv` append). **No stubs** — stubs create reconciliation debt and break `walter_doctor`'s `board_reconcile`. Heavy curation/reconciliation stays with Full WALTER (see §9). The delivery layer is *additive* to BOARD, not a replacement.

---

## 3. Delivery layer — the operational fix

### 3.1 Where
- **WALTER-only folder per recipient:** `AGENTS/{RECIPIENT}/inbox/WALTER/` (create if missing).
- **One file per signal per recipient.** No rolling file.
- **WALTER only ever CREATES files here — never edits an existing one.** The recipient reads, then moves it to `inbox/WALTER/processed/`. WALTER and the recipient never touch the same file → **collision-safe even if the recipient is active** (sidesteps both the shared-`.git/index` race and the rolling-file race; consistent with auto-memory `[[finding_pathspec_commit_race_safety]]` + `[[finding_concurrent_commit_index_race]]`).

### 3.2 Handoff file template (one per signal per recipient)

Filename: `AGENTS/{RECIPIENT}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md`

```markdown
# SIG-W-YYYYMMDD-NNN — short title
BOARD: /BOARD/SIG-W-YYYYMMDD-NNN-short-slug.md
Priority: IMMEDIATE | PRIORITY | ROUTINE | FLASH
Role: ACTION | INFO
From: WALTER
Date: YYYY-MM-DD
## Kernel
One-paragraph factual summary.
## Why you got this
Specific reason THIS recipient is receiving it.
## Requested action
- ACTION recipient: what to check/update/decide.
- INFO recipient: what to note, if anything.
## Confidence / caveats
Confidence score + verify-research / corrected-framing caveats.
## Cross-refs
Related signals, paired dispatches, thresholds, anchor files.
```

The kernel is a self-contained summary so the recipient can act without round-tripping to BOARD; the `BOARD:` line is the pointer to full detail.

### 3.3 Platform-nuanced `delivered`

| Recipient platform | Agents | `delivered` means |
|--------------------|--------|-------------------|
| **OpenClaw** (shared VPS clone) | BRENT, HAWK, BROCK, LIQUID, HENRY, LABOR, NEXUS, VIOLET, SHADE (+ PROME, Tier-2 OpenClaw) | Handoff file exists in the **shared clone** the recipient reads. Instant when **Quick WALTER** (which runs on the VPS) writes it. *(When **Full WALTER** writes it locally, it reaches the VPS clone only after the commit is on origin and the VPS pulls — so cross-clone delivery is on-origin-gated even for OpenClaw recipients.)* |
| **Claude Code** (own clone) | CARL, REGINALD, SAM, RED (+ OZK per root CLAUDE.md `*`) | File written **and committed AND pushed/synced to origin** (reachable on the recipient's next pull). **Written-but-unpushed is NOT delivered.** |

**Urgent fallback:** FLASH (and IMMEDIATE) to a Claude-Code recipient while sync is pending falls back to the existing **FLASH → Telegram/Will alert** path so the signal is never invisible. See §3.4 for the precedence→push handling.

### 3.4 Push handling by precedence (Claude-Code recipients)

Push is **not** automatic WALTER authority (see §7). The one standing auto-push authorization:

- **FLASH / IMMEDIATE to a CC recipient:** PROME may perform a **clean-tree scoped commit + normal push** — *only if* there is no unrelated/uncommitted work in the shared tree and no unsafe rebase condition. Git pushes **commits, not files**, so this is: *commit only the exact WALTER / BOARD / recipient-handoff paths, verify the tree is clean/safe, `pull --rebase` if behind, push normally, never force* — NOT "push specific files." This is the **only** standing auto-push authorization; all other pushes stay Will-coordinated.
- **PRIORITY / ROUTINE to a CC recipient:** write + commit locally, mark `written_not_delivered_pending_push`, and surface in `walter_doctor` + closeout until a Will/PROME sync window pushes it.

---

## 4. `delivery_log.tsv` — WALTER-side delivery record

File: `AGENTS/WALTER/routed/delivery_log.tsv` — **WALTER-owned**, append-only, **one row per signal × recipient** (a single signal fanning to N recipients writes N rows). Separate from `route_log.tsv` (which stays one row per *signal* = the routing decision); the two have different cardinality, so they are not merged.

| Column | Type | Description |
|--------|------|-------------|
| `timestamp_routed` | ISO 8601 UTC | When WALTER wrote the handoff file. |
| `signal_id` | string | `SIG-W-YYYYMMDD-NNN`. |
| `recipient` | string | Agent name. |
| `role` | enum | `ACTION` / `INFO`. |
| `recipient_platform` | enum | `OPENCLAW` / `CLAUDE_CODE`. |
| `precedence` | enum | `FLASH` / `IMMEDIATE` / `PRIORITY` / `ROUTINE`. |
| `handoff_path` | string | `AGENTS/{RECIPIENT}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md`. |
| `written_state` | enum | `WRITTEN` (file created, uncommitted) / `COMMITTED` (committed locally). **WALTER records up to COMMITTED only.** |
| `notes` | free text | Optional. |

**Critical (requirement B):** WALTER records *written/committed* state only. Whether a committed handoff is **on origin / delivered** is **derived read-only from git by `walter_doctor`** (see §6) — PROME does **not** edit this log after pushing. WALTER owns the log; PROME owns the sync/push *action*; the doctor derives sync state. This keeps the log a WALTER-only write surface and avoids a cross-agent edit race.

Header row (exact):
```
timestamp_routed	signal_id	recipient	role	recipient_platform	precedence	handoff_path	written_state	notes
```

---

## 5. `board_log.tsv` — consumption record (recipient-owned)

Each agent maintains `AGENTS/<NAME>/board_log.tsv` — local, append-only, one row per consumed signal. **v0.2 adds a `source` column** so a consumed entry records *how* the agent encountered the signal.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `timestamp_read` | ISO 8601 UTC | yes | When the agent read it. |
| `signal_id` | string | yes | `SIG-W-YYYYMMDD-NNN`. |
| `disposition` | enum | yes | `acted` / `noted` / `deferred` / `info-only` / `skipped`. |
| `source` | enum | yes (v0.2+) | `INBOX_WALTER` (delivered handoff file) / `BOARD_SCAN` (found via INDEX scan) / `MANUAL` (operator-supplied). |
| `notes` | free text | no | Optional. |

Header row (v0.2):
```
timestamp_read	signal_id	disposition	source	notes
```

**Migration:** existing logs (CARL/REGINALD 9-col; HAWK 4-col) are **owned by their agents** — WALTER does **not** edit them. Each agent adds `source` on its next touch; readers tolerate missing `source` (treat as `BOARD_SCAN`, the v0.1 behavior). Disposition enum unchanged from v0.1 (see table below).

| Disposition | Meaning |
|-------------|---------|
| `acted` | Incorporated into this session's analysis / decision / downstream dispatch. |
| `noted` | Read and filed; no action, no follow-up. |
| `deferred` | Will revisit — use `notes` for when/why. |
| `info-only` | Named in `info`; read for awareness, no action expected. |
| `skipped` | Judged irrelevant despite routing — rare; paper trail for routing-disagreement audit. |

---

## 6. Telemetry — ships immediately (the anti-rot safeguard)

Two read-only checks in `walter_doctor.py` (also runnable by PROME via the portable-python fallback, §10). This is the single safeguard that stops a repeat of v0.1's silent stall.

### 6.1 `delivered_but_unconsumed`
For each `AGENTS/*/inbox/WALTER/*.md` not in `processed/`: a **delivered** handoff (OpenClaw: present in this clone; CC: on origin) older than **N days** (default **N=2**, configurable) → flag. Until the recipient's Phase-2 boot-step is installed, nothing moves to `processed/`, so this surfaces the consumption gap per recipient — exactly the intended visibility.

### 6.2 `written_but_undelivered` (git-derived)
For each non-`processed/` handoff file: derive push/origin state **read-only from git** (a handoff in commits ahead of `origin/master`, or not reachable from origin, = not delivered). Severity by platform (honors §3.3):
- **CC recipient + committed-but-not-on-origin** → **MED** (genuinely undelivered; needs the §3.4 push). MED escalates for FLASH/IMMEDIATE precedence.
- **CC recipient + uncommitted (`WRITTEN`)** → LOW (mid-session transient).
- **OpenClaw recipient + not-on-origin** → INFO (readable in the shared clone once synced; push is for cross-clone durability, not delivery to a same-clone reader).
- If `origin/master` ref is unavailable (fresh/shallow clone) → INFO "origin ref unavailable, sync state underivable" (per `[[finding_shallow_clone_false_fork]]` — don't assert divergence on a missing ref).

---

## 7. Sync & push authority

**Not automatic WALTER authority.** WALTER commits locally; **PROME/Will own the push decision and window.** The single exception is the §3.4 FLASH/IMMEDIATE-to-CC clean-tree scoped-push, which is the only standing auto-push authorization. Everything else rides a Will-opened window per root CLAUDE.md + auto-memory `[[feedback_defer_push_coordinate]]`.

---

## 8. Consumption rollout — phased, but NOT open-ended

**Delivery ships first (Phase 1, this session).** Consumption is **Phase 2 — tracked and time-boxed**, because "define template, agents apply later" already failed once (v0.1 → the BRENT miss).

- **WALTER defines** the recipient consumption boot-step template (§8.1) and does **not** edit other agents' boot docs.
- **OpenClaw recipients:** PROME/Will install the boot step now (Prome controls those CLAUDE.md files) — **start with BRENT**, then HAWK / BROCK / LIQUID / HENRY / LABOR / NEXUS / VIOLET / SHADE.
- **Claude-Code recipients** (CARL / REGINALD / SAM / RED): **self-apply on next spawn.**
- **Time-box:** the `delivered_but_unconsumed` telemetry (§6.1) makes the gap visible per recipient every boot; it is the mechanism that prevents an open-ended stall.

### 8.1 Recipient consumption boot-step (template WALTER provides; others apply)

```markdown
### WALTER signal intake  (inbox/WALTER delivery lane)

At boot, after STATUS / MEMORY / LAST_COMPLETION:

1. List AGENTS/<YOU>/inbox/WALTER/*.md not yet in your board_log.tsv.
   (If board_log.tsv does not exist, create it with the v0.2 header:
    timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes)
2. For each: read it, decide disposition (acted/noted/deferred/info-only/skipped),
   append a row to board_log.tsv with source=INBOX_WALTER,
   then `git mv` the file to inbox/WALTER/processed/.
3. Let `acted` items inform this session.
```

(`git mv`, not bash `mv`, per auto-memory `[[feedback_git_mv_for_inbox_processing]]` — bash `mv` leaves the deletion unstaged.)

**Note vs the v0.1 BOARD-scan boot-step:** v0.1 had recipients scan `/BOARD/INDEX.md` for rows naming them. v0.2's delivery lane replaces the scan with a directory list of files WALTER actively delivered — cheaper and gap-visible. An agent may run both (scan as a backstop), logging `source` accordingly.

---

## 9. Two run modes — Quick vs Full WALTER

Canonical definition lives in `AGENTS/WALTER/CLAUDE.md` (SPAWN PROTOCOL); summarized here for the delivery context.

- **Full WALTER** (Will spawns): everything — BOARD curation, registry refresh, anchor re-verify, audits, liaisons, full boot + closeout. Owns reconciliation.
- **Quick WALTER** (PROME spawns a temporary OpenClaw copy to route one batch): constrained tool-runner. Minimal reads → filter gates + Phase 1.5 verify → classify → write BOARD entry + INDEX row + `route_log` → write delivery file(s) + `delivery_log` → stop. Skips registry refresh / anchor re-verify (except the Iran guard) / audits / liaison discovery / MEMORY-STATUS-LAST_COMPLETION rewrites / full `walter_doctor`. **Does NOT push; commits locally only.**

---

## 10. Portability

Tools may run on the VPS (Quick WALTER) where `.venv` may be absent. Invoke with the fallback (also in CLAUDE.md boot step 0.5):

```sh
PYTHON="${PYTHON:-python3}"
[ -x .venv/bin/python3 ] && PYTHON=.venv/bin/python3
$PYTHON AGENTS/WALTER/tools/walter_doctor.py
```

`walter_doctor.py` is **stdlib-only** (runs anywhere `python3` exists). The market-data threshold scan (CLAUDE.md step 6c, `dashboard.py`) needs the venv libs — confirm the venv exists wherever that scan runs.

---

## 11. Git scope + guardrails

WALTER may write only to: **`/BOARD/`**, **`AGENTS/WALTER/`**, and **`AGENTS/{RECIPIENT}/inbox/WALTER/`** (a second WALTER shared-write zone, same class as `handoff_WALTER/`). WALTER **never** edits a recipient's `STATUS` / `CLAUDE` / `MEMORY` / `board_log.tsv` / `processed/` contents — agents own consumption; WALTER owns delivery. Commit by **explicit pathspec** (per file), never `git add` a whole folder (per auto-memory `[[finding_pathspec_commit_race_safety]]`).

---

## 12. Messaging-overhaul superseding note

Auto-memory `[[project_messaging_overhaul]]` ("don't patch inbox/outbox/HERMES hygiene — file-based messaging being replaced") and `[[project_walter_cop_direction]]` ("don't build full inbox infra yet") are **superseded ONLY for this narrow WALTER signal-delivery lane** (create-only, per-signal, telemetry-audited). Confirmed intentional by Will 2026-06-17. This does **not** revive general inbox/outbox/HERMES infra; those memories stand for everything else. The earlier caution was about building *unguarded* inbox infra — the §6 telemetry is exactly the guard it wanted, which is why the reversal is scoped and safe.

---

## 13. Phase-1 acceptance checks ("done")

- [ ] PROME can spawn Quick WALTER; it routes a test signal → BOARD file + INDEX row + `route_log` row + delivery file(s) in each recipient's `inbox/WALTER/` + `delivery_log` row(s).
- [ ] BOARD still reconciles (ToC = sections = files).
- [ ] `walter_doctor` runs via portable python and includes both new checks (`delivered_but_unconsumed` + git-derived `written_but_undelivered`).
- [ ] BRENT -001 / HAWK -002 audited; backfill handoff files created (narrow — those two only).
- [ ] Nothing claims `consumed` (Phase 2 not shipped).
- [ ] Concise diff-stat shown; no push until Will/PROME approve.

---

## 14. Future extensions (deferred)

- Cross-agent "0 consumers after 7 days" routing-gap telemetry (now partially covered by §6.1).
- Disposition analytics (skipped-rate → persistent mis-routing detection).
- COP integration: per-agent "unread WALTER-delivery count" when COP resumes.

---

## Version History

- **v0.2** — 2026-06-17 — Delivery layer added (`inbox/WALTER/` create-only handoff files + platform-nuanced `delivered` + `delivery_log.tsv` + git-derived sync telemetry + scoped-push policy + phased-time-boxed rollout + `board_log` `source` column + Quick/Full mode reference). Per "WALTER Routing v2 — Final Design Packet", Will + PROME + ORC approved-in-principle 2026-06-17.
- **v0.1** — 2026-04-20 — initial consumption spec (`board_log.tsv` + BOARD-scan boot-step). Defaults approved by Will via Telegram msg 938. Propagation stalled → motivated v0.2.
