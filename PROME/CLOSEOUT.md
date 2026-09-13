# PROME CLOSEOUT

**Created:** 2026-05-18 · **Updated:** 2026-09-11 (Will-directed simplification: remove historical explanations; retain procedures, thresholds, exceptions, section names and runner interfaces). Amendment history: `git log -p -- PROME/CLOSEOUT.md`; pre-simplification text: `git show 4a0757370074f1a5ed48353894298b465f842047:PROME/CLOSEOUT.md` (on-demand).
**Owner:** Prome
**Commit-pipeline approval/review:** `plans/2026-09-09_boot-hardening.md` (on-demand).
**Purpose:** Repeatable session-end procedure. Run before `/clear`, `/new`, or session handoff.

> Companion to `PROME/BOOT.md` (session start) + `PROME/CLAUDE.md` (bootstrap). **Git protocol canon = root `CLAUDE.md` (auto-injected; not restated here).**

---

## When to run
*(Execution wrapper: the `/closeout` skill — `PROME/.claude/skills/closeout/SKILL.md` — runs this file's order with the exact commands; this file stays the canon for rules and tiers.)*

Before `/clear` or `/new` · before stepping away from a long session · after any session that produced state changes worth persisting. Skip for casual one-off exchanges with no artifacts.

---

## Pre-closeout (~1 min)

1. `git status --short` — review what changed.
2. **Foreign uncommitted work does NOT block closeout:** commit only your authored scope using exact pathspecs and safe-push. Include daily memory and self-authored auto-memory under the root grants; never sweep the tree. Non-ff recovery requires root step 3's dirty-path overlap check before autostash. If `AGENTS/PROME/` reappears, migrate its contents to `PROME/inbox/` and flag the sender (BOOT step 6).
3. **Orchestrated-desk release (ANY tier):** tell each named desk spawned this session to run its own closeout; verify idle + last delivery committed (desk `(orch)` commits). Desk-dir residue is in-flight; never sweep it on respawn. Log final touch in `PROME/state/ORCH_LOG.tsv`. Single home: `PROME/ORCHESTRATION_PLAYBOOK.md` §Two-tier.
4. List this session's artifacts; check transcript hygiene (preserve durable results in files, not restated dumps); pick the tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart; back within the hour | SCRATCH addendum (3-5 lines) | Optional 1-line checkpoint |
| **Light** | Short session paused for hours; 1-2 artifacts | SCRATCH **targeted update** (WQ-232 — never a mandated full rewrite) + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread / end-of-day | Chunk 1 + Chunk 2 (+ auto-memory if earned) + Chunk 4 + auto-push | Yes |
| **Heavy** | Pattern-discovery session | Standard + design docs + Chunk 3 full sweep | Yes |

End-of-day runs at least Standard. Standard+ includes the MANDATORY dashboard and THE HELM symmetry rows, plus the Decision Deck row. Chunk 3 triggers apply at ANY tier. **Bounce:** append 3–5 SCRATCH lines (what happened, pending, next entry point); optional wrapper checkpoint from repo root with message-file subject `PROME: bounce checkpoint` and exact path `PROME/SCRATCH.md`.

---

> **⚡ Mechanical tail in one shot — RUN IT AFTER EVERY MANDATED WRITE**, including ARGUS's ❌ fixes and root steps 1b–1e, and after `fleet_dashboard.py` (which writes the `dashboard_state.json` the gate reads), immediately BEFORE the Helm/Deck render: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout`. An early run is optional preflight, not the final verdict. **WQ-231 rule — no write to a SOURCE the gate checks may fall after the run that certifies it**, because nothing re-checks it. **Derived renders are excluded because they write no GATE-CHECKED source** — *not* because they are pure projections: they are not. The Helm run owns the change-feed baseline and writes `PROME/state/brief_snapshot.json` + `brief_changes.jsonl`; `argus_scope.py --record-baseline` writes `argus_baseline.json`. The gate checks none of the three (`grep -c brief_ / WQ_EXPLAINERS / argus_baseline prome_gate.py` = 0,0,0), which is what makes them safe to run late — a narrower and more fragile licence than "projection", and it dies the moment any of those files gains a gate check. That is why every HAND edit feeding them — BRIEF narrative, HANDBOOK priorities, Deck explainer rows — runs BEFORE the gate, and only render+publish runs after. The runner owns the resulting sequence. **On rc=1: fix, then REGENERATE EVERY DERIVED ARTIFACT whose sources the fix touched, THEN re-run the full gate.** The gate reads the generated FILE, not the sources, so re-running it alone re-checks output built before the fix. The four: `dashboard_state.json` (`fleet_dashboard.py`) · SCRATCH's DOCKET-VIEW block (`docket_view.py --write`) · SCRATCH's Pending-Will block (`willq_view.py --write`) · `WQ_LEDGER.tsv`+`.crc` (`wq_ledger.py sync` then `check`). ⛔ **`prome_gate.py` has NO wq_ledger check** — that artifact is covered by no gate run at all, so its regeneration is remembered, never caught. Loop to rc=0. ⛔ **It does not certify "the shipped state."** It establishes selected source records + `dashboard_state.json` — never the Helm, the Decision Deck, publication success, or the eventual (possibly rebased) commit. Say what passed. rc=1 means BLOCKING failures. The script also prints reminders for manual root steps 1c (consumer check) and 1d (memory index); it does not replace judgment writes. New mechanical checks go in the SCRIPT, not this prose.

## Boot↔Closeout symmetry — ONE HOME PER FACT

Closeout is the **write-back tail** of boot (`[[finding_closeout_as_writeback_tail]]`). `check_symmetry()` reads this section: every mandatory boot-read surface is registered here, paired-write or explicitly one-way.

⛔ **Write each fact ONCE, in the column that owns it, and nowhere else.** A fact that already has a home is a POINTER everywhere else — never a second copy. This table replaces the former "Prome Write-Back Contract", which said the same things again in different words.

| Surface | Owns (write it here) | Never |
|---|---|---|
| `PROME/SCRATCH.md` | the **resume point** + information registered NOWHERE else. Operator card lives here. **Format contract (7/11):** the dashboard parses the exact label `Pending Will:` with `·`-separated items on one line. | restating a DOCKET / GATES / WILL_QUEUE row, or anything inside a generated block |
| `PROME/STATUS.md` | **current operational state** — PROME's selected queue, owner lanes, restrictions, live surfaces, spine-audit date | session accounts, market narrative, history |
| `PROME/DOCKET.tsv` | **dated obligations** (canonical; SCRATCH + HEARTBEAT are views). Append at EOF only; rows are cited by physical line. A decision DEFERRED gets a dated row **at creation** | a second copy of the date in prose |
| `PROME/GATES.tsv` | **gate state** — register an approved action-gate the session it is approved; flip on a landed verdict; refresh `last_checked`. 🔴 **A row must NEVER leave a session `FIRED-UNEXECUTED` without escalation** | inventing an owner's grade |
| `PROME/WILL_QUEUE.md` | **decisions needing Will** — every ruling written to its row verbatim with its stamp; a row leaves OPEN the moment it stops needing him | a second numbered series |
| `memory/YYYY-MM-DD.md` | the **session account** — what happened, what was learned, what was wrong | state other files own |
| `PROME/HANDOFF.md` | **concise navigation** to what the next session needs; 3–5 live entries | a third session recap |
| `PROME/ACTIVE_DECISIONS.md` | non-terminal decision rows; resolution REPLACES pending text | inferring execution — unknown ⇒ `DEFERRED` + reconcile |
| `HEARTBEAT.md` | regime read; update on a regime-level change or >48h stale in a market week — **answer no-op explicitly, at every tier** | mirroring its base date elsewhere |
| `memory/auto/` | durable lessons only; index row in `MEMORY.md`; **self-commit mandatory** (root carve-out ③) | activity recaps |
| **WQ LEDGER** (`PROME/registry/WQ_LEDGER.tsv` + `.crc`) | generated — `wq_ledger.py sync` then `check`, after the WILL_QUEUE write | ⛔ hand-editing; it is sealed and append-only |
| **Fleet-Ops dashboard** · **THE HELM** · **DECISION DECK** | Will-facing renders. **Standard+ mandatory.** Source edits (`BRIEF.md`, `HANDBOOK.md` §Top priorities, `WQ_EXPLAINERS.tsv`) run BEFORE the gate; renders run after | treating a render as a state file |

**Generated blocks are written by their generator, never by hand:** SCRATCH's `DOCKET-VIEW` (`scripts/docket_view.py --write`) and `Pending Will` (`PROME/tools/willq_view.py --write`), `dashboard_state.json` (`fleet_dashboard.py`), the WQ ledger. **Preserve them; stop restating their contents in prose.**

**Intentionally one-way (no write-back):** `PROME/CLOSEOUT.md` + `CLOSEOUT_PROCEDURES.md` (procedure reference) · `FLEET_SCAN.md` (superseded snapshot) · inbox/outbox scans (handled inline, never deferred) · OPEN-prediction resolution (domain-agent-owned).

---

## The routine — in order

**Targeted updates at EVERY tier (WQ-240; was Light-only under WQ-232).** One test decides whether a surface gets written: **does the boot path already reach it?** A dated obligation (DOCKET), a decision (WILL_QUEUE), a gate state (GATES) — **do NOT restate.** Anything registered nowhere, and the resume pointer — **write it.** If nothing in a surface's column changed, the correct action is a **stated no-op**, never silence and never a rewrite.

1. **GATES + DOCKET surgical, FIRST.** Enumerate every gate/catalyst the session touched; each gets a row edit or a stated no-op. Then regenerate the view:
   `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/SCRATCH.md`
2. **WILL_QUEUE** paired write → `python3 PROME/tools/wq_ledger.py sync` then `check` → `python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`.
3. **SCRATCH · STATUS · ACTIVE_DECISIONS · HEARTBEAT · HANDOFF** per the table above. Byte-flow lines and rotation recipes → **`PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow**. Blind-reader verification is triggered there too.
4. **Memory** — the day's log; auto-memory only if a durable lesson was earned (root step 1d after).
5. **Residual triggers** → **`PROME/CLOSEOUT_PROCEDURES.md` § Chunk 3**. Walk the list; do not recall it.
6. **Root session-end steps 1b–1e** (root `CLAUDE.md` owns the text): 1b orphan · 1c consumer · 1d memory-index `--slug` · 1d-bis hot-index flow · 1e claim. **Their WRITES land here, before the audit.**
7. **Helm/Deck SOURCE edits + Fleet-Ops build** — `BRIEF.md`, `HANDBOOK.md` §Top priorities, `WQ_EXPLAINERS.tsv`, then `python3 PROME/tools/fleet_dashboard.py`. **This is the last step that may edit anything.**
8. 🔴 **FREEZE, then AUDIT the finished candidate (Standard/Heavy).** The candidate must be COMPLETE first — steps 1–7 done, including every check that can still produce an edit:
   `python3 PROME/tools/argus_scope.py --record-review` → spawn `argus` → apply ❌ only, ⚠️ → residue → RUN-LOG row.
   ⛔ **If any ❌ fix changes the candidate: re-review the CHANGED portion, regenerate affected outputs, and `--record-review` AGAIN.** A verdict certifies the content it saw, never a path list.
9. **FINAL gate** — after every write in 1–8:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout`
   It now includes **`ARGUS review manifest (content, not paths)`** — BLOCKING when the reviewed candidate changed after the audit. **rc=1 ⇒ fix, regenerate every derived artifact whose sources the fix touched, then re-run the FULL gate.** Loop to rc=0.
10. **Render + publish** (Standard+) — Helm, then Deck. Prerequisites were checked at Pre-closeout; a failure here is reported, never waived.
11. **Commit + push** — exact paths, message file, wrapper:
    `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/commit_check.py commit --stage --push -F <msgfile> -- <exact paths>`
    Then `python3 PROME/tools/argus_scope.py --verify-review` must still read **UNCHANGED** — the committed contents are the reviewed result.
    **Push receipt, verbatim:** `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` A bare `Pushed.` is not a receipt.
12. **ARGUS baseline, AFTER the commit:** `python3 PROME/tools/argus_scope.py --record-baseline HEAD`; it rides the next commit.

---

## Delivery — say which of the three was reached

⛔ **COMMITTED, PUSHED and PUBLISHED are three different states and the report names them separately.** A closeout that reaches two of three is **PARTIAL**, and the report says so with the **concrete blocker** — never a silent waiver because publication became inconvenient.

| State | Established by |
|---|---|
| **COMMITTED** | `commit_check` intent↔commit match, exact paths |
| **PUSHED** | the verbatim receipt above |
| **PUBLISHED** | the artifact republished at its own URL |

**Publication prerequisites are checked at Pre-closeout, not at the render** (`prome_gate closeout` → `publication prerequisites`): every OPEN `WILL_QUEUE` row has an explainer row, and the live artifact has been viewed this session so the republish cannot be refused at the end. **If a prerequisite cannot be met, say so at Pre-closeout and decide then** — an unmet prerequisite discovered at step 10 is a process defect, not a reason to skip delivery.

**Session summary to Will:** what landed (commit hashes belong HERE, never in state files — they decay) · the three delivery states · what is owed at next boot · open `PROME/WILL_QUEUE.md` rows by number.

---

## Conditional procedures — explicit pointers

⛔ These do not run every closeout. **`PROME/CLOSEOUT_PROCEDURES.md`** holds: § Byte-flow and rotation recipes (incl. blind-reader verification) · § Chunk 3 residual triggers · § Skip rules · § Cross-session behavioral rules · § Closeout-class fleet memories.

**Historical rationale is NOT restated here.** Amendment history: `git log -p -- PROME/CLOSEOUT.md`; the WQ-240 simplification and the L338 sizing decision: `PROME/proposals/2026-09-12_wq240-closeout-simplification-RULED.md`.
