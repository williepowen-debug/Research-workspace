# PROME CLOSEOUT

**Editorial amendment:** 2026-10-25, WQ-525 — session summary follows BOOT step 8; [ruling and reads](proposals/2026-10-25_research-first-briefing-RULED.md).
**Created:** 2026-05-18 · **Updated:** 2026-11-04 (L910 hot/cold rotation; detailed audit, generation, gate, delivery and publication procedures moved verbatim to `PROME/CLOSEOUT_PROCEDURES.md`; no rule changed). Prior stamps → `PROME/archive/CLOSEOUT_STAMP_CHAIN_2026-10-16.md`; amendment history → Git.
**Gate-instruction reconciliation:** 2026-10-25 — end-of-day ARGUS found the pre-WQ-517 step-10 instruction still live in step 8 and both closeout runners. Aligned to the already-approved October 24 rule; no code or policy change.
**Owner:** Prome
**Current amendment — 2026-10-19, WQ-460:** Decision Deck upkeep is PAUSED BY WILL until explicit resume and reconciliation. This supersedes WQ-446 and WQ-382(a) Deck duties during the pause, including at a spine audit. Helm routine generation, publication and presentation upkeep are now RETIRED by WQ-461; authority: `PROME/proposals/2026-10-19_wq461-helm-retired-RULED.md`. Authority and implementation record: `PROME/proposals/2026-10-19_wq460-decision-deck-paused-RULED.md`.
**Commit-pipeline approval/review:** `PROME/plans/2026-09-09_boot-hardening.md` (on-demand).
**Purpose:** Repeatable session-end procedure. Run before `/clear`, `/new`, or session handoff.

> Companion to `PROME/BOOT.md` (session start) + `PROME/CLAUDE.md` (bootstrap). **Git protocol canon = root `CLAUDE.md` (auto-injected; not restated here).**

---

## When to run
*(Execution wrapper: the `/closeout` skill — `PROME/.claude/skills/closeout/SKILL.md` — runs this file's order with the exact commands; this file stays the canon for rules and tiers.)*

Before `/clear` or `/new` · before stepping away from a long session · after any session that produced state changes worth persisting. Skip for casual one-off exchanges with no artifacts.

---

## Restart checkpoint — Bounce extension (WQ-526, 2026-10-26)

“Checkpoint for restart” preserves an unfinished working session across a context reset. It is not an actual session closeout, even though it uses Bounce's writeback surface. This is the narrow exception to Pre-closeout item 3 and the charter's Spawn-closeout discipline: do not ask surviving owners to close merely because PROME resets. Actual session closeout, machine shutdown/switch and end-of-day retain the existing lifecycle rules. Never label a checkpoint as completed Standard/Heavy closeout or reset session limits.

- Use SCRATCH's existing resume section for the task/next action and pointers to original boot directory, working-session identity, pending controls, owner assignments and consumed process/spawn/review allowances. Decisions/obligations stay in WILL_QUEUE/DOCKET/GATES; research stays in its existing report/account. Preserve unresolved PARTIAL/UNKNOWN states and work not recoverable from committed files. An unchanged checkpoint needs no new artifact, stamp or commit; update only changed facts. HANDOFF points to SCRATCH rather than duplicating it.
- Enumerate existing PROME-owned touches from ORCH_LOG and other known active work from the current assignment evidence; keep Will-launched desks separate. Establish whether each process can survive the departing context, using supported runtime evidence. Independent reachable owners keep their assignments; notify an owner only when coordination requires it. Record existing IDs, scope and durable entry point, with observed reachability/survival and time, in SCRATCH or existing task records. Do not turn a saved list into a liveness claim or write a false closeout event. Later actual closeout still enumerates these carried touches, including those from earlier dates in this unfinished session.
- **Session-bound or unknown-survival work:** before ending its parent context, request a bounded checkpoint/stop at a safe boundary through its verified channel; obtain durable partial output, exact remaining work and a stop/survival acknowledgement. Do not request a full domain closeout solely for the restart. Never kill an uncheckpointed worker to manufacture readiness. If the process cannot cooperate or its state cannot be established, name the at-risk work and mark restart NOT READY; keep the context open where possible and ask Will how to handle the concrete risk. An unavoidable crash remains a failed preservation condition, not success. On resume, verify the old writer stopped before any replacement and retain the original assignment/limits. No authority to modify or stop Will-owned sessions is inferred; unresolved dependencies are reported to Will.
- Preserve changed results and rulings before departure under their ordinary exact-path commit, review and delivery requirements; no shortcut around required content review. A pointer-only Bounce checkpoint uses the existing commit wrapper and verified fast-forward push, without generating the Standard closeout candidate/ARGUS baseline. If nothing changed, no commit is necessary; already-owed delivery still remains owed. Verify which bytes are durable locally/remotely; failed publication or unavailable output is explicit PARTIAL. Do not stage foreign files. Recheck inbox/working-tree changes before yielding and carry arrivals that cannot be consumed yet.
- Resume by PROME/BOOT_MODULES.md § Resume after a restart (pointer at BOOT.md's § heading). The original PROME yields repository writing before the successor starts. Only one bounded real fresh-context trial is authorized by WQ-526: record task recovery, arrivals/deadlines, assignment preservation and repeated work avoided in the existing implementation report; distinguish observed passes, failures and unexercised cases. No recurring measurement or separate checkpoint system.

## Pre-closeout (~1 min)

1. `git status --short` — review what changed.
2. **Foreign uncommitted work does NOT block closeout:** commit only your authored scope using exact pathspecs and safe-push. Include daily memory and self-authored auto-memory under the root grants; never sweep the tree. Non-ff recovery requires root step 3's dirty-path overlap check before autostash. If `AGENTS/PROME/` reappears, migrate its contents to `PROME/inbox/` and flag the sender (BOOT step 6).
3. **Orchestrated-desk release at every actual closeout:** enumerate carried/current touches and record the closeout ask/answer or dark-before-ask through `python3 scripts/orch_log.py append …` before the closeout commit; restart checkpoints follow § Restart checkpoint. Full states/scope/writer rules → `PROME/CLOSEOUT_PROCEDURES.md` § Spawn-closeout release.
3b. **Inbox (2026-10-21, Will):** every packet that reached `PROME/inbox/` during the session is dispositioned (consumed to `processed/`, routed, or registered) or named as carried, with its count, in the closeout report. The inbox is PROME's sole delivery surface (BOOT.md step 6).
4. List this session's artifacts; check transcript hygiene (preserve durable results in files, not restated dumps); pick the tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart; back within the hour | SCRATCH addendum (3-5 lines) | Optional 1-line checkpoint |
| **Light** | Short session paused for hours; 1-2 artifacts | SCRATCH **targeted update** (WQ-232 — never a mandated full rewrite) + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread / end-of-day | § The routine, steps 1–12 (+ auto-memory if earned) + auto-push. **ARGUS only at the day's LAST Standard/Heavy closeout (WQ-485 A); an intra-day Standard freezes and defers the audit, gate `--tier light`** | Yes |
| **Heavy** | Pattern-discovery session | Standard + design docs + the FULL residual-trigger sweep (`CLOSEOUT_PROCEDURES.md` § Chunk 3) | Yes |

End-of-day runs at least Standard. **Decision Deck Owed and Reference are PAUSED BY WILL (WQ-460), at every tier.** THE HELM is RETIRED (WQ-461), including its spine-audit publication trigger. No routine dashboard publication is owed. Chunk 3 triggers apply at ANY tier. **Bounce:** append 3–5 SCRATCH lines (what happened, pending, next entry point); optional wrapper checkpoint from repo root with message-file subject `PROME: bounce checkpoint` and exact path `PROME/SCRATCH.md`.
5. **Publication prerequisites (only for a separately requested active deliverable — checked HERE, never at the render; § Delivery):** Helm is RETIRED (WQ-461); Deck is PAUSED BY WILL (WQ-460). Do not maintain dashboard explainers, view/list hosted dashboard files, or prepare dashboard publication. If Will separately requests another deliverable, establish its applicable publication prerequisites now; an unmet active prerequisite is reported and resolved before delivery.

---

> **⚡ The gate is step 9 of § The routine, and the routine owns its placement, its `--tier` argument and the regenerate-then-re-run rule.** ⛔ This block previously restated the sequence here — ordering the render *after* the gate and quoting a `--tier`-less command — which is the duplicated-rule problem this file was simplified to remove, recurring inside its own repair. **One home: the numbered sequence below.**

## Boot↔Closeout symmetry — ONE HOME PER FACT

Closeout is the **write-back tail** of boot (`[[finding_closeout_as_writeback_tail]]`). Every mandatory boot-read surface is registered here, paired-write or explicitly one-way.

⛔ **Write each fact ONCE, in the column that owns it, and nowhere else.** A fact that already has a home is a POINTER everywhere else — never a second copy. This table replaces the former "Prome Write-Back Contract", which said the same things again in different words.

| Surface | Owns (write it here) | Never |
|---|---|---|
| `PROME/SCRATCH.md` | the **resume point** + information registered NOWHERE else. Operator card lives here. **Format contract (7/11):** `PROME/tools/willq_view.py --check` parses the exact label `Pending Will:` with `·`-separated items on one line. | restating a DOCKET / GATES / WILL_QUEUE row, or anything inside a generated block |
| `PROME/STATUS.md` | **current operational state** — PROME's selected queue, owner lanes, restrictions, live surfaces, spine-audit date | session accounts, market narrative, history |
| `PROME/state/CALENDAR.md` | **nothing by hand** — the generated forward-catalyst view of DOCKET (`scripts/docket_view.py --write PROME/state/CALENDAR.md`, step 1); boot reads it at BOOT step 2; moved out of SCRATCH 2026-10-20 (Will) | hand edits; a date that is not a DOCKET row |
| `PROME/DOCKET.tsv` | **dated obligations** (canonical; `state/CALENDAR.md` + HEARTBEAT are views). Append at EOF only; rows are cited by physical line. A decision DEFERRED gets a dated row **at creation** | a second copy of the date in prose |
| `PROME/GATES.tsv` | **gate state** — register an approved action-gate the session it is approved; flip on a landed verdict; refresh `last_checked`. 🔴 **A row must NEVER leave a session `FIRED-UNEXECUTED` without escalation** | inventing an owner's grade |
| `PROME/WILL_QUEUE.md` | **decisions needing Will** — every ruling written to its row verbatim with its stamp; a row leaves OPEN the moment it stops needing him | a second numbered series |
| `memory/YYYY-MM-DD.md` | the **session account** — what happened, what was learned, what was wrong | state other files own |
| `PROME/HANDOFF.md` | **the decision, what remains owed and the next action**, each a pointer to its record, never a retyped fact; 3–5 live entries | a third session recap |
| `PROME/ACTIVE_DECISIONS.md` | non-terminal decision rows; resolution REPLACES pending text | inferring execution — unknown ⇒ `DEFERRED` + reconcile |
| `HEARTBEAT.md` | regime read; update on a regime-level change or >48h stale in a market week — **answer no-op explicitly, at every tier** | mirroring its base date elsewhere |
| `memory/auto/` | durable lessons only; index row in `MEMORY.md`; **self-commit mandatory** (root carve-out ③) | activity recaps |
| **WQ LEDGER** (`PROME/registry/WQ_LEDGER.tsv` + `.crc`) | generated — `wq_ledger.py sync` then `check`, after the WILL_QUEUE write | ⛔ hand-editing; it is sealed and append-only |
| **THE HELM** · **DECISION DECK** | Helm generation, supporting `docket.html`, BRIEF/HANDBOOK presentation upkeep, change-feed advancement and publication are RETIRED (WQ-461). Deck is PAUSED BY WILL (WQ-460). Preserve history and shared libraries; maintain canonical records in their own rows above | regenerating retired/paused surfaces; presenting old HTML or feed history as current |

**Generated blocks are written by their generator, never by hand:** the calendar view `PROME/state/CALENDAR.md`'s `DOCKET-VIEW` (`scripts/docket_view.py --write`; moved out of SCRATCH 2026-10-20, Will) and SCRATCH's `Pending Will` (`PROME/tools/willq_view.py --write`), the WQ ledger. **Preserve them; stop restating their contents in prose.**

**Intentionally one-way (no write-back):** `PROME/CLOSEOUT.md` + `CLOSEOUT_PROCEDURES.md` (procedure reference) · `PROME/BOOT_MODULES.md` (boot procedure modules, edited only as canon) · `PROME/state/SPAWN_SLATE.md` (a gate-generated view, written by `prome_gate.py` at boot and at closeout; no separate manual write-back) · `FLEET_SCAN.md` (superseded snapshot) · inbox/outbox scans (handled inline, never deferred) · OPEN-prediction resolution (domain-agent-owned).

---

## The routine — in order

**Targeted updates at EVERY tier (WQ-240; was Light-only under WQ-232).** One test decides whether a surface gets written: **does the boot path already reach it?** A dated obligation (DOCKET), a decision (WILL_QUEUE), a gate state (GATES) — **do NOT restate.** Anything registered nowhere, and the resume pointer — **write it.** If nothing in a surface's column changed, the correct action is a **stated no-op**, never silence and never a rewrite.

1. **GATES + DOCKET surgical, FIRST.** Enumerate every gate/catalyst the session touched; each gets a row edit or a stated no-op. Then regenerate the view:
   `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/state/CALENDAR.md` — rc=2 writes nothing: a DOCKET row is malformed (e.g. a date span like `2026-10.30`), the calendar is NOT current and the spawn list cannot see that row; fix the line it names, then regenerate (WQ-578 batch 2: no gate checks the calendar any more).
2. **WILL_QUEUE** paired write → `python3 PROME/tools/wq_ledger.py sync` then `check` → `python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`.
3. **SCRATCH · STATUS · ACTIVE_DECISIONS · HEARTBEAT · HANDOFF** per the table above. **A5 (10/16): the session account is written ONCE, in memory; the rest point to it. Reference the authoritative record (WILL_QUEUE row, DOCKET L#, commit, artifact) instead of retyping its facts or figures (WQ-583 A, 2026-10-31).** Byte-flow lines and rotation recipes → **`PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow**. Blind-reader verification is triggered there too.
4. **Memory** — the day's log; auto-memory only if a durable lesson was earned (root step 1d after).
5. **Residual triggers** → **`PROME/CLOSEOUT_PROCEDURES.md` § Chunk 3**. Walk the list; do not recall it.
6. **Root session-end steps 1b–1e run here, before the audit.** Exact commands and hot-index flow → `PROME/CLOSEOUT_PROCEDURES.md` § Root session-end checks.
7. **ALL generation for active outputs is the LAST step that may write any reviewed-candidate file, BEFORE the freeze.** Renders are NOT read-only. Run `python3 PROME/tools/table_check.py --quiet` · `python3 PROME/tools/done_rows_check.py` · `python3 PROME/tools/wq_ledger.py check` · `python3 scripts/orch_log.py check`. Full rules → `PROME/CLOSEOUT_PROCEDURES.md` § Generation and deterministic checks.
8. 🔴 **FREEZE, then AUDIT (Standard/Heavy).** The candidate is complete — steps 1–7 done, including every check that can still produce an edit.
   Audit cadence and intra-day deferral → `PROME/CLOSEOUT_PROCEDURES.md` § Audit contract details; deferred report: `audit DEFERRED to the end-of-day closeout (WQ-485)`.
   Concurrent closeouts follow `PROME/tools/ARGUS_CONTRACT.md`. Immediately pre-freeze: `python3 PROME/tools/inbox_census.py PROME`; freeze: `python3 PROME/tools/argus_scope.py --record-review --contract /tmp/prome-delivery-plan.json`; audit, then `python3 PROME/tools/argus_scope.py --mark-reviewed "<one line>"`. Full procedure → `PROME/CLOSEOUT_PROCEDURES.md` § Audit contract details.
   Legacy manifest rules → `PROME/CLOSEOUT_PROCEDURES.md` § Audit contract details.
   Live-fleet and pinned-perimeter rules → `PROME/CLOSEOUT_PROCEDURES.md` § Audit contract details.
   ⛔ **Freezing is NOT reviewing.** `--record-review` writes verdict `FROZEN`; only `--mark-reviewed` writes `REVIEWED`, and it refuses if the candidate moved in between. ⛔ **A ❌ fix in the WQ-583 classes above (approval or ruling, position or book, obligation, completion state, research conclusion) ⇒ re-review that changed portion, regenerate affected active outputs under step 7 (never retired Helm or paused Deck), `--record-review` again, and re-mark; every other ❌ fix is disclosed in memory as unreviewed and the review is marked (WQ-485 A, 2026-10-22).**
9. **FINAL gate, with the tier:**
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout --tier <bounce|light|standard|heavy> (--no-memory | --slug <name> …) (--no-superseded | --superseded <old> <new> …)`
   Tier and return-code handling → `PROME/CLOSEOUT_PROCEDURES.md` § Final gate rules.
10. **Commit → VERIFY → push. In that order, and the verification gates the push.**
    ```
    cd "$(git rev-parse --show-toplevel)"
    python3 PROME/tools/argus_scope.py --deliver-candidate -F <msgfile> [--carry <path> …]   # never pushes
    python3 PROME/tools/argus_scope.py --verify-review --ref <DELIVERY_SHA> --paths <the paths it printed>
    bash scripts/safe-push.sh        # ONLY if the line above returned rc 0
    ```
    Post-freeze arrival classification and strict-arrival `--observe /tmp/prome-observed.json` route → `PROME/CLOSEOUT_PROCEDURES.md` § Delivery verification details.
    ⛔ **`--push` on the commit wrapper is forbidden at this step.** It pushes inside the same command, so the delivery check would run *after* the bytes were already on origin — detecting an unreviewed delivery once it has shipped is not a control.
    Candidate-delivery rules; intra-day path: `commit_check.py commit --stage -F <msgfile> -- <exact paths>` → `PROME/CLOSEOUT_PROCEDURES.md` § Delivery verification details.
    **Push receipt, verbatim:** `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` A bare `Pushed.` is not a receipt.
11. **Publish the verified artifacts** only after verified delivery. **Unmet owed publication for a separately requested active deliverable is reported, never waived.** Helm RETIRED; Deck PAUSED. Full rule → `PROME/CLOSEOUT_PROCEDURES.md` § Publication rule.
12. **ARGUS baseline, AFTER successful verified delivery:** `python3 PROME/tools/argus_scope.py --record-baseline <DELIVERY_SHA>` (the reviewed commit, not a moving HEAD); it rides the next commit with any `--carry` edits. ⛔ **The baseline record and the review receipt are never part of a reviewed candidate** — they are bookkeeping *about* a review, they change after the commit, and including them would make the next closeout inherit a guaranteed failure.

---

## Delivery — say which of the three was reached

⛔ **COMMITTED, PUSHED and PUBLISHED are three different states and the report names them separately.** An owed delivery state not reached makes the closeout **PARTIAL**, with the **concrete blocker** — never a silent waiver because publication became inconvenient. Report **Deck: PAUSED BY WILL (WQ-460)** separately; the authorized pause alone is not PARTIAL and is never PUBLISHED or a current NO-OP. Report **Helm: RETIRED (WQ-461)**; this retirement likewise is not PARTIAL or PUBLISHED. No routine dashboard publication remains owed.

| State | Established by |
|---|---|
| **COMMITTED** | `commit_check` intent↔commit match, exact paths |
| **PUSHED** | the verbatim receipt above |
| **PUBLISHED** | an active artifact republished at its own URL; when no active publication is owed, report NOT REQUIRED; report Deck separately as PAUSED BY WILL (WQ-460) and Helm as RETIRED (WQ-461) |

**Publication prerequisites are checked at Pre-closeout, not at the render** (item 5), only for a separately requested active deliverable. Helm retirement and the Deck pause require no dashboard explainer, page read, file listing or hosted receipt. **If an active prerequisite cannot be met, say so at Pre-closeout and decide then**; discovering it only at step 11 remains a process defect.

**Session summary to Will:** apply `PROME/BOOT.md` step 8 **Research-first briefing**. **Required operational accounting:** what landed (commit hashes belong HERE, never in state files — they decay) · the three delivery states · **"Done without asking": each C1–C9 act of the session with its commit, or the word none (WQ-348 guard, `PROME/CLAUDE.md` § Ask First)** · **RETIRED: Helm under WQ-461; PAUSED BY WILL: Deck under WQ-460 (neither is a skipped control)** · **SKIPPED: any active routine step not run, or run by reasoning instead of by the instrument, with its reason — and then the headline is PARTIAL whatever the three delivery states say (`PROME/CLAUDE.md` § Skipped-control reporting)** · what is owed at next boot · open `PROME/WILL_QUEUE.md` rows by number.

---

## Conditional procedures — explicit pointers

⛔ These run when their trigger fires. **`PROME/CLOSEOUT_PROCEDURES.md`** holds: § Audit contract details · § Byte-flow and rotation recipes (incl. blind-reader verification) · § Chunk 3 residual triggers · § Skip rules · § Cross-session behavioral rules · § Closeout-class fleet memories.

**Historical rationale is NOT restated here.** Amendment history: `git log -p -- PROME/CLOSEOUT.md`; the WQ-240 simplification and the L338 sizing decision: `PROME/proposals/2026-09-12_wq240-closeout-simplification-RULED.md`.
