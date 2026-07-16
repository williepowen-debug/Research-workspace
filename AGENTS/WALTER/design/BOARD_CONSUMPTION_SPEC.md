# BOARD Delivery + Consumption Spec

**Version:** v0.9
**Created:** 2026-04-20 (v0.1 consumption-only) · **Extended:** 2026-06-17 (v0.2 delivery layer) · **Clarified:** 2026-06-18 (v0.3–v0.5 Quick-WALTER tightening) · **Collapsed:** 2026-06-26 (v0.6 single-machine platform-collapse — OpenClaw cut)
**Owner:** WALTER
**Status:** **Single-machine (desktop CC) since 2026-06-26 — OpenClaw cut; `delivered` is uniform (committed + on-origin); Quick-WALTER retired.** Delivery layer SHIPPED; consumption = Phase 2 self-apply (see §8). Approved-in-principle by Will + PROME + ORC (2026-06-17); v0.6 collapse Will-ratified 2026-06-26 (`design/OPENCLAW_CUTOVER_PLAN.md`).

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
| **delivered** | Handoff file is **committed AND on origin** (reachable on the recipient's next pull). Written-but-unpushed is NOT delivered. See §3. |
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

### 3.3 `delivered` — single-machine definition

All agents run as Claude Code sessions on the one shared desktop repo (the OpenClaw/VPS platform was cut 2026-06-26 — see `design/OPENCLAW_CUTOVER_PLAN.md`). `delivered` has **one meaning for every recipient**:

> A handoff file is **delivered** when it is **written, committed, AND pushed/synced to origin** (reachable on the recipient's next pull). **Written-but-unpushed is NOT delivered.**

**Urgent fallback:** FLASH (and IMMEDIATE) while a sync is pending falls back to the existing **FLASH → Telegram/Will alert** path so the signal is never invisible. See §3.4 for the precedence→push handling.

### 3.4 Push handling by precedence

Push is **not** automatic blanket WALTER authority (see §7). The one standing auto-push authorization:

- **FLASH / IMMEDIATE:** WALTER may perform a **clean-tree scoped commit + push via `scripts/safe-push.sh`** (the ff-gated helper) — *only if* there is no unrelated/uncommitted work in the shared tree and no unsafe rebase condition (0g, Will-ratified 2026-06-26). Git pushes **commits, not files**, so this is: *commit only the exact WALTER / BOARD / recipient-handoff paths, verify the tree is clean/safe, `pull --rebase` if behind, push via the ff-gate, never force* — NOT "push specific files." This is the **only** standing auto-push authorization; all other pushes stay Will-coordinated.
- **PRIORITY / ROUTINE:** write + commit locally, mark `written_not_delivered_pending_push`, and surface in `walter_doctor` + closeout until a Will sync window (or the next push-train) pushes it.

---

### 3.5 Pull-complete recipient exemption — skip inbox delivery (added v0.7, 2026-07-04)

A recipient that runs a **complete** `/BOARD/` diff-scan at boot — one that dispositions **every unrecorded `SIG-W` across all of INDEX** (not a tiered/selective subset) — already has a **complete pull**. For such an agent the per-recipient `inbox/WALTER/` handoff is redundant with its own scan (both are fed the same BOARD entry), so **WALTER SKIPS the `inbox/WALTER/` handoff + the `delivery_log` delivery row for it.** The BOARD entry + `route_log` row are still written (the signal is published + audit-logged as normal); only the redundant push-delivery to that agent is skipped.

**Exemption criterion (verify empirically before adding an agent):** the agent's boot doc must run a *complete whole-INDEX* BOARD-diff (grep all of `BOARD/INDEX.md` vs its ledger, disposition every unrecorded ID). **Tiered/selective scans do NOT qualify** — they can skip the cluster an ACTION item lands in. Confirm by the 2026-07-04 CARL reconciliation method: the agent's ACTION handoffs already appear dispositioned in its ledger with **zero un-dispositioned ACTION**.

**Current exemption list:**
- **CARL** — runs a complete whole-INDEX BOARD-diff (`AGENTS/CARL/CLAUDE.md` boot step 5, diffs *all* of INDEX vs `board/BOARD_LOG.tsv`). Verified 2026-07-04: 22/22 ACTION handoffs already dispositioned, 0 misses → WALTER stops writing to `AGENTS/CARL/inbox/WALTER/`.
- **RED** (added 2026-07-09, Will-approved design-walkthrough) — runs a complete whole-INDEX BOARD scan at boot (`AGENTS/RED/CLAUDE.md` step 1.5, RED-scoped consumption pass: reads the cluster ToC + drills into every section). **Stronger case than CARL: RED is auto-cc'd INFO-only (never the ACTION owner)**, so dropping its handoffs carries *zero* ACTION-miss risk by construction. RED was 24% of all delivery-lane volume + the single largest `delivered_but_unconsumed` INFO pile — the per-signal handoff is pure redundancy with its own step-1.5 scan. → WALTER stops writing to `AGENTS/RED/inbox/WALTER/`; RED drains its current backlog normally, then its step-5.5 consume becomes a WALTER no-op (RED may retire it). *(Fixes the 2026-06-23 over-cc finding at the routing source, per `[[feedback...]]` delivery-telemetry calibration.)*
- **NOT exempt — REGINALD** (BOARD-diff is *tiered/selective*, step 9b three-tier scope; the 7/4 reconciliation found an un-dispositioned ACTION — the OZK deed-in-lieu SIG-W-20260704-004 → keeps the lane + a drain-step) and **SAM** (no `/BOARD/` scan at all → the lane is its only intake).

**Doctor:** `walter_doctor` carries a `PULL_COMPLETE` set that excludes exempt agents from `delivered_but_unconsumed` and instead flags any residual handoffs in their inbox as **to-ARCHIVE** (a one-time cleanup, not a consume-gap). **Transition:** existing pre-exemption handoffs are bulk-archived to `processed/` by PROME (cross-dir write, Will-authorized) once the exemption lands; going forward WALTER simply never creates them. Adding/removing an agent from the exemption edits both this list and the doctor's `PULL_COMPLETE` set.

#### 3.5.1 Scope limit — the exemption covers DISPATCHES, not NOTES (added v0.9, 2026-07-16)

**The §3.5 exemption rests on a premise that is easy to lose: the content is ON BOARD.** The exemption is sound *only because* the recipient's whole-INDEX BOARD-diff **is** the pull — i.e. the handoff and the scan are fed the same BOARD entry, so the handoff is pure redundancy. **Remove the BOARD entry and the redundancy argument collapses: a BOARD-diff cannot surface something that was never on BOARD.**

**Rule:** a **non-BOARD note** to a pull-complete recipient (CARL, RED) **IS delivered to `AGENTS/{RECIPIENT}/inbox/WALTER/` — the §3.5 skip does NOT apply.** The inbox is that note's **only** delivery channel.

**What counts as a non-BOARD note** (the existing, unchanged fold/breadcrumb practice — this sub-section names its delivery consequence, it does not create a new artifact class): a create-only `*-NOTE.md` written to a recipient's `inbox/WALTER/` that carries a mechanism, correction, or cross-reference which **fails the Novelty gate as a signal** (owner already holds the event) but whose *value-add* the owner does not hold — so it is deliberately **not** dispatched: no BOARD entry, no `route_log` row, no `delivery_log` row. Worked examples: the **2026-07-11 CREED 1740-Broadway ratings-lag precedent** (event already in CREED's KB; the 17-month downgrade-lag *mechanism* was not) and the **2026-07-16 CARL retail-sales/savings breadcrumb** (CARL held the May print more precisely; the internal inconsistency between its own retail row and its own savings row was the delta) — the second is what surfaced this gap.

**⚠️ Known telemetry gap — accepted, named, NOT silently tolerated.** Because a note writes **no `delivery_log` row**, it is invisible to `walter_doctor`'s `delivered_but_unconsumed` **and** `written_but_undelivered` checks. **A note to a pull-complete recipient therefore has exactly one delivery path and zero telemetry behind it** — the weakest-instrumented thing WALTER produces, and a direct exception to the CONTRACT's "PROOF — instrumented (best-in-fleet)" claim. This is **tolerable at current volume** (2 notes total, ~1/wk at peak; both to non-exempt-or-adjacent agents) and is **not** worth a parallel ledger yet. **Escalation trigger: if note volume reaches ~1/wk sustained, OR a note is ever found unconsumed/missed, add a `note_log.tsv` (or a `delivery_log` row with `role: NOTE` + a `written_state` that the doctor can age) rather than continuing to rely on the recipient noticing an un-tracked file.** Until then the mitigation is that notes are rare, create-only, and boot-visible in the recipient's inbox.

**Author discipline:** a note to a pull-complete recipient **must state, in the note itself, why it is arriving in an inbox the recipient's §3.5 exemption would normally make redundant** — otherwise the recipient may reasonably read a stray inbox file as an exemption violation or a stale artifact and archive it unread. (Both worked examples above carry that line.)

**This is a clarification of §3.5's scope, not a change to it.** No agent moves in or out of `PULL_COMPLETE`; the doctor's set is untouched; every dispatch-path rule above is unchanged.

---

## 4. `delivery_log.tsv` — WALTER-side delivery record

File: `AGENTS/WALTER/routed/delivery_log.tsv` — **WALTER-owned**, append-only, **one row per signal × recipient** (a single signal fanning to N recipients writes N rows). Separate from `route_log.tsv` (which stays one row per *signal* = the routing decision); the two have different cardinality, so they are not merged.

| Column | Type | Description |
|--------|------|-------------|
| `timestamp_routed` | ISO 8601 UTC | When WALTER wrote the handoff file. |
| `signal_id` | string | `SIG-W-YYYYMMDD-NNN`. |
| `recipient` | string | Agent name. |
| `role` | enum | `ACTION` / `INFO`. |
| `recipient_platform` | enum | `CLAUDE_CODE` (constant since the single-machine collapse, 2026-06-26). Historical `OPENCLAW` rows preserved as-is — append-only, never rewritten. |
| `precedence` | enum | `FLASH` / `IMMEDIATE` / `PRIORITY` / `ROUTINE`. |
| `handoff_path` | string | `AGENTS/{RECIPIENT}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md`. |
| `written_state` | enum (write-time stamp; **NOT** maintained post-write) | `written_not_delivered_pending_push` — the write-time default (handoff created; rides the next closeout `safe-push.sh`). Legacy values `COMMITTED` / `DELIVERED` / `DELIVERED_SHARED_CLONE` predate the 2026-06-26 single-machine collapse. **This is a creation stamp, not a lifecycle field** — WALTER does not flip it to delivered post-push (the ~560 rows stuck at `pending_push` are expected, not a backlog). **Authoritative delivered-state is git-derived** via the doctor's `written_but_undelivered` check (handoff committed AND on origin = delivered). Do not backfill. *(Formalized v0.8, 2026-07-09.)* |
| `notes` | free text | Optional. |

**Critical (requirement B):** WALTER records *written/committed* state only. Whether a committed handoff is **on origin / delivered** is **derived read-only from git by `walter_doctor`** (see §6) — PROME does **not** edit this log after pushing. WALTER owns the log; PROME owns the sync/push *action*; the doctor derives sync state. This keeps the log a WALTER-only write surface and avoids a cross-agent edit race.

**UTC discipline:** `Z` means UTC. Convert ET/local clock before writing; never append `Z` to local wall-clock time.

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
For each `AGENTS/*/inbox/WALTER/*.md` not in `processed/`: a **delivered** handoff (on origin) older than **N days** (default **N=2**, configurable) → flag. Until the recipient's Phase-2 consume boot-step is installed, nothing moves to `processed/`, so this surfaces the consumption gap per recipient — exactly the intended visibility.

### 6.2 `written_but_undelivered` (git-derived)
For each non-`processed/` handoff file: derive push/origin state **read-only from git** (a handoff in commits ahead of `origin/master`, or not reachable from origin, = not delivered):
- **Committed-but-not-on-origin** → **MED** (genuinely undelivered; needs the §3.4 push). MED escalates for FLASH/IMMEDIATE precedence.
- **Uncommitted (`WRITTEN`)** → LOW (mid-session transient).
- If `origin/master` ref is unavailable (fresh/shallow clone) → INFO "origin ref unavailable, sync state underivable" (per `[[finding_shallow_clone_false_fork]]` — don't assert divergence on a missing ref).

---

## 7. Sync & push authority

WALTER commits locally; **pushing is Will-coordinated** (a Will-opened window or the push-train; root CLAUDE.md + auto-memory `[[feedback_defer_push_coordinate]]`). The single standing exception is the §3.4 FLASH/IMMEDIATE clean-tree scoped-push via the `safe-push.sh` ff-gate — **WALTER-self-authorized on a verified-clean tree** (0g, Will-ratified 2026-06-26; PROME is no longer an always-on push agent).

---

## 8. Consumption rollout — phased, but NOT open-ended

**Delivery ships first (Phase 1, this session).** Consumption is **Phase 2 — tracked and time-boxed**, because "define template, agents apply later" already failed once (v0.1 → the BRENT miss).

- **WALTER defines** the recipient consumption boot-step template (§8.1) and does **not** edit other agents' boot docs.
- **All recipients self-apply** the consume boot-step (§8.1) on next spawn — single-machine, every agent is a CC session. (The OpenClaw "PROME installs it" path is retired with the VPS.)
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

## 9. Run mode — Full WALTER only

**Quick WALTER was RETIRED 2026-06-26** (0d, Will-ratified). It was a PROME-spawned, VPS-resident route-only mode — made moot by the OpenClaw cut. Its historical guardrails (registry-only RED-FT/REG-T/safety-net routing, canonical-lane discipline, the Iran-anchor guard, UTC-stamp discipline) live in git history; they no longer gate a live mode. UTC-`Z` timestamp discipline still applies to all BOARD/delivery artifacts.

- **Full WALTER** (Will spawns) is the **only** mode: everything — BOARD curation, registry refresh, anchor re-verify, audits, liaisons, full boot + closeout. Owns reconciliation.

---

## 10. Portability

Tools invoke with the portable-python fallback (also in CLAUDE.md boot step 0.5) so they run whether or not `.venv` is present:

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

- [x] WALTER routes a signal → BOARD file + INDEX row + `route_log` row + delivery file(s) in each recipient's `inbox/WALTER/` + `delivery_log` row(s). *(Phase-1 shipped; Quick-WALTER retired 2026-06-26.)*
- [x] BOARD still reconciles (ToC = sections = files). *(verified 2026-07-03 — doctor `board_reconcile` ✓ at 434.)*
- [x] `walter_doctor` runs via portable python and includes both new checks (`delivered_but_unconsumed` + git-derived `written_but_undelivered`). *(both live + running every boot.)*
- [x] BRENT -001 / HAWK -002 audited; backfill handoff files created (narrow — those two only). *(delivery_log confirms both created 2026-06-17, COMMITTED — closed the structural BRENT miss.)*
- [x] Nothing claims `consumed` (Phase 2 not shipped). *(satisfied at Phase-1 ship; Phase-2 consume has since rolled to 9 agents, correctly logged.)*
- [x] Concise diff-stat shown; no push until Will/PROME approve. *(standing process criterion.)*

*(All boxes ticked/verified 2026-07-03 arch/infra audit — Phase-1 acceptance complete.)*

---

## 14. Future extensions (deferred)

- Cross-agent "0 consumers after 7 days" routing-gap telemetry (now partially covered by §6.1).
- Disposition analytics (skipped-rate → persistent mis-routing detection).
- ~~COP integration: per-agent "unread WALTER-delivery count" when COP resumes.~~ *(DROPPED 2026-07-03 — COP decommissioned 2026-06-28; dead conditional.)*

---

## Version History

- **v0.9** — 2026-07-16 — **§3.5.1 scope limit: the pull-complete exemption covers DISPATCHES, not NOTES** (Will-directed, same-session). The §3.5 skip is sound only because the recipient's whole-INDEX BOARD-diff **is** the pull — handoff and scan are fed the same BOARD entry. A **non-BOARD note** (create-only `*-NOTE.md`: a mechanism/correction/cross-reference that fails Novelty as a signal but whose value-add the owner lacks — deliberately no BOARD entry / no route_log / no delivery_log) has **no BOARD entry for a BOARD-diff to find**, so the redundancy argument collapses and **the inbox is its ONLY channel**. Rule: notes to CARL/RED ARE delivered; the skip does not apply. **Names an accepted telemetry gap:** a note writes no `delivery_log` row → invisible to `delivered_but_unconsumed` AND `written_but_undelivered` = one delivery path, zero telemetry, a direct exception to the CONTRACT's instrumented-PROOF claim; tolerable at 2-notes-total volume, **escalation trigger = ~1/wk sustained OR any note found missed → add `note_log.tsv` or a `role: NOTE` delivery_log row**. Author discipline: a note to an exempt recipient must state why it's arriving in an inbox its exemption would normally make redundant (else it reads as a violation/stale artifact and gets archived unread). **Clarification only — no agent moves in/out of `PULL_COMPLETE`, doctor's set untouched, no dispatch-path rule changed.** Surfaced by the 2026-07-16 CARL retail-sales/savings breadcrumb; worked precedent 2026-07-11 CREED 1740-Broadway. No CHECKLIST bump (Phase 3.5 governs dispatch delivery; notes are not dispatches — a pointer was added).
- **v0.8** — 2026-07-09 — **§3.5 adds RED to the pull-complete exemption** (Will-approved design-walkthrough): RED runs a complete whole-INDEX BOARD scan (boot step 1.5) AND is auto-cc'd INFO-only (never ACTION) → zero ACTION-miss risk; it was 24% of delivery volume + the largest unconsumed-INFO pile. `walter_doctor` `PULL_COMPLETE = {"CARL", "RED"}`. WALTER stops writing `AGENTS/RED/inbox/WALTER/` handoffs. Also **formalized the `delivery_log.written_state` enum** (§ below): a write-time stamp, NOT a maintained lifecycle field — authoritative delivered-state is git-derived via the doctor's `written_but_undelivered` check (the 564 rows stuck at `written_not_delivered_pending_push` are expected, not a backlog; do not backfill).
- **v0.7** — 2026-07-04 — **§3.5 pull-complete recipient exemption** added (Will-approved, relayed via PROME). A recipient that runs a *complete whole-INDEX* `/BOARD/` diff-scan has a complete pull → WALTER skips its `inbox/WALTER/` handoff + `delivery_log` row (BOARD + route_log still written). First exemption: **CARL** (verified 7/4 — 22/22 ACTION already dispositioned, 0 misses). Explicitly NOT exempt: REGINALD (tiered scan; 1 un-dispositioned ACTION found) + SAM (no scan). `walter_doctor` `PULL_COMPLETE` set excludes exempt agents from `delivered_but_unconsumed` + flags residual handoffs as to-ARCHIVE. Provenance: WALTER↔PROME consume-step reconciliation 2026-07-04 (the "asymmetric-records" class; CARL/REGINALD asymmetry surfaced by the tiered-vs-complete distinction).
- **v0.6** — 2026-06-26 — **single-machine platform-collapse** (OpenClaw/VPS cut). `delivered` collapses to one definition (committed + on-origin); §3.3 platform table retired; §3.4/§7 push authority → WALTER-self-on-clean-tree via `safe-push.sh` ff-gate (0g); §4 `recipient_platform` constant `CLAUDE_CODE` going forward (historical `OPENCLAW` rows preserved, append-only); §8 all recipients self-apply consume; §9 **Quick WALTER RETIRED** (0d); §10 VPS framing dropped. Will-ratified 2026-06-26 (Phase-0 0a/0d/0e/0f/0g). Canonical: `design/OPENCLAW_CUTOVER_PLAN.md` + `BOARD_CONSUMPTION_SPEC_v0.6_CHANGESET.md`. (v0.3–v0.5 were Quick-WALTER tightening — moot with Quick retired.)
- **v0.2** — 2026-06-17 — Delivery layer added (`inbox/WALTER/` create-only handoff files + platform-nuanced `delivered` + `delivery_log.tsv` + git-derived sync telemetry + scoped-push policy + phased-time-boxed rollout + `board_log` `source` column + Quick/Full mode reference). Per "WALTER Routing v2 — Final Design Packet", Will + PROME + ORC approved-in-principle 2026-06-17.
- **v0.1** — 2026-04-20 — initial consumption spec (`board_log.tsv` + BOARD-scan boot-step). Defaults approved by Will via Telegram msg 938. Propagation stalled → motivated v0.2.
