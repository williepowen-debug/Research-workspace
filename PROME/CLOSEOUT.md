# PROME CLOSEOUT

**Created:** 2026-05-18 · **Updated:** 2026-10-16 00:01 ET (PROME session `b486657a`, L738 / WQ-446 A — the Deck OWED view publishes only when the step-9 gate's *Deck republish* line reads OWED or UNKNOWN; Pre-closeout 4–5, symmetry row, step 11, § Delivery; acceptance `PROME/tools/tests/ACCEPTANCE_L738_deck_owed_digest.md`) · prior stamps 2026-09-11 → 2026-10-15 15:29 ET moved verbatim to `PROME/archive/CLOSEOUT_STAMP_CHAIN_2026-10-16.md`; amendment history `git log -p -- PROME/CLOSEOUT.md`.
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

## Pre-closeout (~1 min)

1. `git status --short` — review what changed.
2. **Foreign uncommitted work does NOT block closeout:** commit only your authored scope using exact pathspecs and safe-push. Include daily memory and self-authored auto-memory under the root grants; never sweep the tree. Non-ff recovery requires root step 3's dirty-path overlap check before autostash. If `AGENTS/PROME/` reappears, migrate its contents to `PROME/inbox/` and flag the sender (BOOT step 6).
3. **Orchestrated-desk release (ANY tier):** enumerate and disposition the desk touches required by `PROME/CLAUDE.md` § Session Process Controls, Spawn-closeout discipline (WQ-249), including its scope and four reported outcomes. Record the closeout ask and answer, or that the desk went dark before the ask, in `PROME/state/ORCH_LOG.tsv` before the closeout commit — **every row through the ONLY writer, `python3 scripts/orch_log.py append …` (flags, contract and the `--tier` word → `PROME/ORCHESTRATION_PLAYBOOK.md` § Two-tier "Ledger"). Step 9's gate runs `orch_log.py check` and the OBSERVED check (view row count == ledger) BLOCKING. ⚠️ OBSERVED catches a hand row that no writer append has followed; equality is NOT evidence of zero hand rows (the writer-side refusal is DAEDALUS's — packet 2026-10-15; L733).** Idle status and committed delivery are supporting evidence, not proof of the ask. Desk-dir residue is in-flight; never sweep it on respawn. Desk lifecycle: `PROME/ORCHESTRATION_PLAYBOOK.md` § Two-tier orchestrated-desk model.
3b. **Inbox (2026-10-21, Will):** every packet that reached `PROME/inbox/` during the session is dispositioned (consumed to `processed/`, routed, or registered) or named as carried, with its count, in the closeout report. The inbox is PROME's sole delivery surface (BOOT.md step 6).
4. List this session's artifacts; check transcript hygiene (preserve durable results in files, not restated dumps); pick the tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart; back within the hour | SCRATCH addendum (3-5 lines) | Optional 1-line checkpoint |
| **Light** | Short session paused for hours; 1-2 artifacts | SCRATCH **targeted update** (WQ-232 — never a mandated full rewrite) + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread / end-of-day | § The routine, steps 1–12 (+ auto-memory if earned) + auto-push | Yes |
| **Heavy** | Pattern-discovery session | Standard + design docs + the FULL residual-trigger sweep (`CLOSEOUT_PROCEDURES.md` § Chunk 3) | Yes |

End-of-day runs at least Standard. **Decision Deck Owed and Reference are PAUSED BY WILL (WQ-460), at every tier.** THE HELM is RETIRED (WQ-461), including its spine-audit publication trigger. No routine dashboard publication is owed. Chunk 3 triggers apply at ANY tier. **Bounce:** append 3–5 SCRATCH lines (what happened, pending, next entry point); optional wrapper checkpoint from repo root with message-file subject `PROME: bounce checkpoint` and exact path `PROME/SCRATCH.md`.
5. **Publication prerequisites (only for a separately requested active deliverable — checked HERE, never at the render; § Delivery):** Helm is RETIRED (WQ-461); Deck is PAUSED BY WILL (WQ-460). Do not maintain dashboard explainers, view/list hosted dashboard files, or prepare dashboard publication. If Will separately requests another deliverable, establish its applicable publication prerequisites now; an unmet active prerequisite is reported and resolved before delivery.

---

> **⚡ The gate is step 9 of § The routine, and the routine owns its placement, its `--tier` argument and the regenerate-then-re-run rule.** ⛔ This block previously restated the sequence here — ordering the render *after* the gate and quoting a `--tier`-less command — which is the duplicated-rule problem this file was simplified to remove, recurring inside its own repair. **One home: the numbered sequence below.**

## Boot↔Closeout symmetry — ONE HOME PER FACT

Closeout is the **write-back tail** of boot (`[[finding_closeout_as_writeback_tail]]`). `check_symmetry()` reads this section: every mandatory boot-read surface is registered here, paired-write or explicitly one-way.

⛔ **Write each fact ONCE, in the column that owns it, and nowhere else.** A fact that already has a home is a POINTER everywhere else — never a second copy. This table replaces the former "Prome Write-Back Contract", which said the same things again in different words.

| Surface | Owns (write it here) | Never |
|---|---|---|
| `PROME/SCRATCH.md` | the **resume point** + information registered NOWHERE else. Operator card lives here. **Format contract (7/11):** the dashboard parses the exact label `Pending Will:` with `·`-separated items on one line. | restating a DOCKET / GATES / WILL_QUEUE row, or anything inside a generated block |
| `PROME/STATUS.md` | **current operational state** — PROME's selected queue, owner lanes, restrictions, live surfaces, spine-audit date | session accounts, market narrative, history |
| `PROME/state/CALENDAR.md` | **nothing by hand** — the generated forward-catalyst view of DOCKET (`scripts/docket_view.py --write PROME/state/CALENDAR.md`, step 1); boot reads it at BOOT step 2; moved out of SCRATCH 2026-10-20 (Will) | hand edits; a date that is not a DOCKET row |
| `PROME/DOCKET.tsv` | **dated obligations** (canonical; `state/CALENDAR.md` + HEARTBEAT are views). Append at EOF only; rows are cited by physical line. A decision DEFERRED gets a dated row **at creation** | a second copy of the date in prose |
| `PROME/GATES.tsv` | **gate state** — register an approved action-gate the session it is approved; flip on a landed verdict; refresh `last_checked`. 🔴 **A row must NEVER leave a session `FIRED-UNEXECUTED` without escalation** | inventing an owner's grade |
| `PROME/WILL_QUEUE.md` | **decisions needing Will** — every ruling written to its row verbatim with its stamp; a row leaves OPEN the moment it stops needing him | a second numbered series |
| `memory/YYYY-MM-DD.md` | the **session account** — what happened, what was learned, what was wrong | state other files own |
| `PROME/HANDOFF.md` | **concise navigation** to what the next session needs; 3–5 live entries | a third session recap |
| `PROME/ACTIVE_DECISIONS.md` | non-terminal decision rows; resolution REPLACES pending text | inferring execution — unknown ⇒ `DEFERRED` + reconcile |
| `HEARTBEAT.md` | regime read; update on a regime-level change or >48h stale in a market week — **answer no-op explicitly, at every tier** | mirroring its base date elsewhere |
| `memory/auto/` | durable lessons only; index row in `MEMORY.md`; **self-commit mandatory** (root carve-out ③) | activity recaps |
| **WQ LEDGER** (`PROME/registry/WQ_LEDGER.tsv` + `.crc`) | generated — `wq_ledger.py sync` then `check`, after the WILL_QUEUE write | ⛔ hand-editing; it is sealed and append-only |
| **THE HELM** · **DECISION DECK** | Helm generation, supporting `docket.html`, BRIEF/HANDBOOK presentation upkeep, change-feed advancement and publication are RETIRED (WQ-461). Deck is PAUSED BY WILL (WQ-460). Preserve history and shared libraries; maintain canonical records in their own rows above | regenerating retired/paused surfaces; presenting old HTML or feed history as current |

**Generated blocks are written by their generator, never by hand:** the calendar view `PROME/state/CALENDAR.md`'s `DOCKET-VIEW` (`scripts/docket_view.py --write`; moved out of SCRATCH 2026-10-20, Will) and SCRATCH's and `Pending Will` (`PROME/tools/willq_view.py --write`), the WQ ledger. **Preserve them; stop restating their contents in prose.**

**Intentionally one-way (no write-back):** `PROME/CLOSEOUT.md` + `CLOSEOUT_PROCEDURES.md` (procedure reference) · `PROME/BOOT_MODULES.md` (boot procedure modules, edited only as canon) · `PROME/state/SPAWN_SLATE.md` (a gate-generated view, written by `prome_gate.py` at boot and at closeout; no separate manual write-back) · `FLEET_SCAN.md` (superseded snapshot) · inbox/outbox scans (handled inline, never deferred) · OPEN-prediction resolution (domain-agent-owned).

---

## The routine — in order

**Targeted updates at EVERY tier (WQ-240; was Light-only under WQ-232).** One test decides whether a surface gets written: **does the boot path already reach it?** A dated obligation (DOCKET), a decision (WILL_QUEUE), a gate state (GATES) — **do NOT restate.** Anything registered nowhere, and the resume pointer — **write it.** If nothing in a surface's column changed, the correct action is a **stated no-op**, never silence and never a rewrite.

1. **GATES + DOCKET surgical, FIRST.** Enumerate every gate/catalyst the session touched; each gets a row edit or a stated no-op. Then regenerate the view:
   `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/state/CALENDAR.md`
2. **WILL_QUEUE** paired write → `python3 PROME/tools/wq_ledger.py sync` then `check` → `python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`.
3. **SCRATCH · STATUS · ACTIVE_DECISIONS · HEARTBEAT · HANDOFF** per the table above. **A5 (10/16): the session account is written ONCE, in memory; the rest point to it.** Byte-flow lines and rotation recipes → **`PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow**. Blind-reader verification is triggered there too.
4. **Memory** — the day's log; auto-memory only if a durable lesson was earned (root step 1d after).
5. **Residual triggers** → **`PROME/CLOSEOUT_PROCEDURES.md` § Chunk 3**. Walk the list; do not recall it.
6. **Root session-end steps 1b–1e** (root `CLAUDE.md` owns the text): 1b orphan · 1c consumer · **1c-bis ledger nudge** (`python3 scripts/ledger_staleness.py --nudge PROME` whenever `STATUS.md` is in the commit set without one of the ledgers `PROME/workbook/LEDGER_GLOB` declares) · 1d memory-index `--slug` + the hot-index cap check (`check_memory_length.sh`, inside root 1d) · **1d-bis hot-index FLOW rule — PROME-only, not a root step (Will-approved 2026-08-12, ba3a68739):** at ≥75% of the `MEMORY.md` cap, demote (never delete) settled rows to `INDEX_COLD.md` until under 70%, same sitting · 1e claim. **Their WRITES land here, before the audit.**
7. **ALL generation for active surfaces. This is the LAST step that may write any file INSIDE THE REVIEWED CANDIDATE.** Complete affected active views specified in steps 1–6. Steps 8 and 12 write review/baseline records excluded by `RECEIPT_PATHS`. **Helm is RETIRED (WQ-461): do not run `will_handbook.py`, generate its supporting `docket.html`, maintain Helm-only BRIEF/HANDBOOK content or advance its change feed. Decision Deck generation and explainer upkeep remain PAUSED BY WILL (WQ-460): do not run `decision_deck.py`.** Shared parser modules and the boot `will_brief.py --book-line` remain active. **Renders are NOT read-only** — active renders can write tracked snapshots. Any separately requested active render belongs before the freeze; publication follows verification. **Then the deterministic checks, BEFORE the freeze (WQ-417 P4):** `python3 PROME/tools/table_check.py --quiet` · `python3 PROME/tools/done_rows_check.py` · `python3 PROME/tools/wq_ledger.py check` · `python3 scripts/orch_log.py check` (L733). Fix failures HERE. **After ANY correction pass, regenerate affected active outputs and re-run the same four checks.** Corrections never reactivate retired Helm or paused Deck outputs.
8. 🔴 **FREEZE, then AUDIT (Standard/Heavy).** The candidate is complete — steps 1–7 done, including every check that can still produce an edit.
   Concurrent closeouts first follow `PROME/tools/ARGUS_CONTRACT.md` to declare delivery, evidence and attributed observed inventory. `python3 PROME/tools/argus_scope.py --record-review --contract /tmp/prome-delivery-plan.json` → spawn `argus` → apply ❌ only, ⚠️ → residue → RUN-LOG row (`python3 scripts/orch_log.py append --desk ARGUS --tier verifier …`, never typed — L733) → `python3 PROME/tools/argus_scope.py --mark-reviewed "<one line>"`.
   Legacy manifests retain strict behavior; only explicitly classified unrelated versions may update schema2 inventory without re-freezing. Delivery/evidence changes require changed-portion review. **Legacy consumed-move workflow:** if this closeout `git mv`'d a consumed packet from `PROME/inbox/` to `PROME/inbox/processed/`, DECLARE it at the freeze: `--record-review --consumed-move <ORIGIN> <DEST>` (repeatable) — and again at EVERY re-freeze, since a re-freeze rewrites the manifest. ARGUS confirms each pair (its agent file, legs (a) and (b) ①–③); the `--mark-reviewed` note carries its per-pair word. WQ-289 (b), DOCKET L473: the only way an EXCLUDED rename pair passes step 10's `--verify-review --paths`; every other addition at an EXCLUDED path keeps blocking. ⛔ `--consumed-move` is NOT VERIFIED — the live condition and the current reader round are DOCKET L488's state cell (L473 RESOLVED — FOLDED INTO L488 2026-10-08), never a round number written here; until that cell reads INDEPENDENTLY VERIFIED, a consumed packet is committed in a SEPARATE earlier commit, never inside the closeout candidate.**
   ⛔ **Freezing is NOT reviewing.** `--record-review` writes verdict `FROZEN`; only `--mark-reviewed` writes `REVIEWED`, and it refuses if the candidate moved in between. ⛔ **Any ❌ fix ⇒ re-review the changed portion, regenerate affected active outputs under step 7 (never retired Helm or paused Deck), `--record-review` again, and re-mark.**
9. **FINAL gate, with the tier:**
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout --tier <bounce|light|standard|heavy> (--no-memory | --slug <name> …) (--no-superseded | --superseded <old> <new> …)`
   At **standard/heavy** a missing, unevaluable or merely-FROZEN review is **BLOCKING**. **Root steps 1c/1d are declaration-gated at every tier (2026-10-05):** `--no-memory` or one `--slug` per auto-memory written/edited, and `--no-superseded` or one `--superseded <old> <new>` per published figure superseded — an undeclared pair is a BLOCKING row; the gate runs `memory_index_check --strict --slug` and `consumer_check --strict` (fleet + `--self`) itself, and root step 1e (`claim_check --check weekday`) runs mechanically as an advisory. **Log reads (change 2026-10-16): the gate's printed verdict is the read; a named log is opened only as drill-down on a ⚠️/❌ line whose preview does not name the item (BOOT.md step 5's log-read contract, one home).** ⛔ **Omitting `--tier` does not mean “no tier” — it means the review requirement is NOT ENFORCED**, and the gate says so in its own line. Pass the tier you actually ran. **rc=1 ⇒ fix, regenerate affected active outputs under step 7 (never retired Helm or paused Deck), re-freeze, re-run the FULL gate.** Loop to rc=0. ⛔ **rc=2 = INCOMPLETE: one or more checks DID NOT RUN and their subjects are UNKNOWN — never a pass, and not the same failure as rc=1.** Fix the missing/unreadable input the ERROR row names, then re-run the FULL gate; **do NOT proceed to step 10 on rc=2** (before this clause existed, a rc=2 closeout fell straight through to commit → verify → push).
10. **Commit → VERIFY → push. In that order, and the verification gates the push.**
    ```
    cd "$(git rev-parse --show-toplevel)"
    python3 PROME/tools/commit_check.py commit --stage -F <msgfile> -- <exact paths>   # NO --push
    python3 PROME/tools/argus_scope.py --verify-review --ref <DELIVERY_SHA> --paths <the same exact paths>
    bash scripts/safe-push.sh        # ONLY if the line above returned rc 0
    ```
    ⛔ **`--push` on the commit wrapper is forbidden at this step.** It pushes inside the same command, so the delivery check would run *after* the bytes were already on origin — detecting an unreviewed delivery once it has shipped is not a control.
    Record the commit’s full immutable SHA as DELIVERY_SHA immediately after committing. Both arguments matter: `--ref` checks committed bytes and `--paths` declares the exact commit set; schema2 also discovers full inventory and actual commit paths, so a truncated list cannot hide an addition. Follow `ARGUS_CONTRACT.md` for outgoing and actual fresh-fetch snapshot comparisons; ancestry proves inclusion, not unchanged current content.
    **Push receipt, verbatim:** `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` A bare `Pushed.` is not a receipt.
11. **Publish the verified artifacts** only for a separately requested active deliverable, after step 10 verification. **Helm: RETIRED (WQ-461); Deck Owed and Reference: PAUSED BY WILL (WQ-460).** No routine dashboard publication, hosted reads/listing/verification or hosted-receipt writes are owed, including at spine audits. Preserve existing hosted/local artifacts and history without claiming them current or disabled. Retiring Helm supersedes WQ-382(b); resuming dashboard work requires an explicit new instruction and reconciliation, not a timer, correction pass or spine audit. Fleet-Ops remains retired as page and build (WQ-372 / WQ-452.FLEETOPS). Unmet owed publication for a separately requested active deliverable is reported, never waived.
12. **ARGUS baseline, AFTER successful verified delivery:** `python3 PROME/tools/argus_scope.py --record-baseline <DELIVERY_SHA>` (the reviewed commit, not a moving HEAD); it rides the next commit. ⛔ **The baseline record and the review receipt are never part of a reviewed candidate** — they are bookkeeping *about* a review, they change after the commit, and including them would make the next closeout inherit a guaranteed failure.

---

## Delivery — say which of the three was reached

⛔ **COMMITTED, PUSHED and PUBLISHED are three different states and the report names them separately.** An owed delivery state not reached makes the closeout **PARTIAL**, with the **concrete blocker** — never a silent waiver because publication became inconvenient. Report **Deck: PAUSED BY WILL (WQ-460)** separately; the authorized pause alone is not PARTIAL and is never PUBLISHED or a current NO-OP. Report **Helm: RETIRED (WQ-461)**; this retirement likewise is not PARTIAL or PUBLISHED. No routine dashboard publication remains owed.

| State | Established by |
|---|---|
| **COMMITTED** | `commit_check` intent↔commit match, exact paths |
| **PUSHED** | the verbatim receipt above |
| **PUBLISHED** | an active artifact republished at its own URL; when no active publication is owed, report NOT REQUIRED; report Deck separately as PAUSED BY WILL (WQ-460) and Helm as RETIRED (WQ-461) |

**Publication prerequisites are checked at Pre-closeout, not at the render** (item 5), only for a separately requested active deliverable. Helm retirement and the Deck pause require no dashboard explainer, page read, file listing or hosted receipt. **If an active prerequisite cannot be met, say so at Pre-closeout and decide then**; discovering it only at step 11 remains a process defect.

**Session summary to Will:** what landed (commit hashes belong HERE, never in state files — they decay) · the three delivery states · **"Done without asking": each C1–C7 act of the session with its commit, or the word none (WQ-348 guard, `PROME/CLAUDE.md` § Ask First)** · **RETIRED: Helm under WQ-461; PAUSED BY WILL: Deck under WQ-460 (neither is a skipped control)** · **SKIPPED: any active routine step not run, or run by reasoning instead of by the instrument, with its reason — and then the headline is PARTIAL whatever the three delivery states say (`PROME/CLAUDE.md` § Skipped-control reporting)** · what is owed at next boot · open `PROME/WILL_QUEUE.md` rows by number.

---

## Conditional procedures — explicit pointers

⛔ These do not run every closeout. **`PROME/CLOSEOUT_PROCEDURES.md`** holds: § Byte-flow and rotation recipes (incl. blind-reader verification) · § Chunk 3 residual triggers · § Skip rules · § Cross-session behavioral rules · § Closeout-class fleet memories.

**Historical rationale is NOT restated here.** Amendment history: `git log -p -- PROME/CLOSEOUT.md`; the WQ-240 simplification and the L338 sizing decision: `PROME/proposals/2026-09-12_wq240-closeout-simplification-RULED.md`.
