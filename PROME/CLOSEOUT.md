# PROME CLOSEOUT

**Created:** 2026-05-18 · **Updated:** 2026-10-16 00:01 ET (PROME session `b486657a`, L738 / WQ-446 A — the Deck OWED view publishes only when the step-9 gate's *Deck republish* line reads OWED or UNKNOWN; Pre-closeout 4–5, symmetry row, step 11, § Delivery; acceptance `PROME/tools/tests/ACCEPTANCE_L738_deck_owed_digest.md`) · prior stamps 2026-09-11 → 2026-10-15 15:29 ET moved verbatim to `PROME/archive/CLOSEOUT_STAMP_CHAIN_2026-10-16.md`; amendment history `git log -p -- PROME/CLOSEOUT.md`.
**Owner:** Prome
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
4. List this session's artifacts; check transcript hygiene (preserve durable results in files, not restated dumps); pick the tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart; back within the hour | SCRATCH addendum (3-5 lines) | Optional 1-line checkpoint |
| **Light** | Short session paused for hours; 1-2 artifacts | SCRATCH **targeted update** (WQ-232 — never a mandated full rewrite) + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread / end-of-day | § The routine, steps 1–12 (+ auto-memory if earned) + auto-push | Yes |
| **Heavy** | Pattern-discovery session | Standard + design docs + the FULL residual-trigger sweep (`CLOSEOUT_PROCEDURES.md` § Chunk 3) | Yes |

End-of-day runs at least Standard. Standard+: the Decision Deck OWED view publishes when the step-9 gate's *Deck republish (WQ-446 A, L738)* line reads OWED or UNKNOWN (step 11); THE HELM row runs only on Will's word or at a spine audit (WQ-382 (b); step 11). Chunk 3 triggers apply at ANY tier. **Bounce:** append 3–5 SCRATCH lines (what happened, pending, next entry point); optional wrapper checkpoint from repo root with message-file subject `PROME: bounce checkpoint` and exact path `PROME/SCRATCH.md`.
5. **Publication prerequisites (Standard+ — checked HERE, never at the render; § Delivery):** `prome_gate closeout` → *publication prerequisites* — every OPEN `PROME/WILL_QUEUE.md` row has a `PROME/registry/WQ_EXPLAINERS.tsv` row; the gate's *Deck republish (WQ-446 A)* line reads OWED, UNKNOWN or NO-OP — on OWED/UNKNOWN the live Owed artifact must have been viewed this session (once; the publisher refuses an unread URL), on NO-OP the page is not read; the DECIDING line is step 9's (this early read is a preview — a NO-OP here that becomes OWED after step 2's queue writes means view the page then, which is ordinary, not a defect) — and, for the Helm, its files LISTED this session (`Artifact` list, scope `files`, the Helm's URL: the publisher refuses to replace a supporting file the session has not read, listed or itself published) — so the republish cannot be refused at step 11. Unmet ⇒ say so now and decide now.

---

> **⚡ The gate is step 9 of § The routine, and the routine owns its placement, its `--tier` argument and the regenerate-then-re-run rule.** ⛔ This block previously restated the sequence here — ordering the render *after* the gate and quoting a `--tier`-less command — which is the duplicated-rule problem this file was simplified to remove, recurring inside its own repair. **One home: the numbered sequence below.**

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
| **THE HELM** · **DECISION DECK** | Will-facing renders. **The Deck OWED view only when the gate's WQ-446 A line reads OWED or UNKNOWN (NO-OP recorded, never published — L738); the Helm only on Will's word or at a spine audit (WQ-382 (b)).** Sources (`PROME/BRIEF.md`, `PROME/HANDBOOK.md` §Top priorities, `PROME/registry/WQ_EXPLAINERS.tsv`) **AND renders both run at step 7, before the freeze** — renders write tracked files. Only **publication** follows the commit | treating a render as a state file |

**Generated blocks are written by their generator, never by hand:** SCRATCH's `DOCKET-VIEW` (`scripts/docket_view.py --write`) and `Pending Will` (`PROME/tools/willq_view.py --write`), the WQ ledger. **Preserve them; stop restating their contents in prose.**

**Intentionally one-way (no write-back):** `PROME/CLOSEOUT.md` + `CLOSEOUT_PROCEDURES.md` (procedure reference) · `FLEET_SCAN.md` (superseded snapshot) · inbox/outbox scans (handled inline, never deferred) · OPEN-prediction resolution (domain-agent-owned).

---

## The routine — in order

**Targeted updates at EVERY tier (WQ-240; was Light-only under WQ-232).** One test decides whether a surface gets written: **does the boot path already reach it?** A dated obligation (DOCKET), a decision (WILL_QUEUE), a gate state (GATES) — **do NOT restate.** Anything registered nowhere, and the resume pointer — **write it.** If nothing in a surface's column changed, the correct action is a **stated no-op**, never silence and never a rewrite.

1. **GATES + DOCKET surgical, FIRST.** Enumerate every gate/catalyst the session touched; each gets a row edit or a stated no-op. Then regenerate the view:
   `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/SCRATCH.md`
2. **WILL_QUEUE** paired write → `python3 PROME/tools/wq_ledger.py sync` then `check` → `python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`.
3. **SCRATCH · STATUS · ACTIVE_DECISIONS · HEARTBEAT · HANDOFF** per the table above. **A5 (10/16): the session account is written ONCE, in memory; the rest point to it.** Byte-flow lines and rotation recipes → **`PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow**. Blind-reader verification is triggered there too.
4. **Memory** — the day's log; auto-memory only if a durable lesson was earned (root step 1d after).
5. **Residual triggers** → **`PROME/CLOSEOUT_PROCEDURES.md` § Chunk 3**. Walk the list; do not recall it.
6. **Root session-end steps 1b–1e** (root `CLAUDE.md` owns the text): 1b orphan · 1c consumer · **1c-bis ledger nudge** (`python3 scripts/ledger_staleness.py --nudge PROME` whenever `STATUS.md` is in the commit set without one of the ledgers `PROME/workbook/LEDGER_GLOB` declares) · 1d memory-index `--slug` + the hot-index cap check (`check_memory_length.sh`, inside root 1d) · **1d-bis hot-index FLOW rule — PROME-only, not a root step (Will-approved 2026-08-12, ba3a68739):** at ≥75% of the `MEMORY.md` cap, demote (never delete) settled rows to `INDEX_COLD.md` until under 70%, same sitting · 1e claim. **Their WRITES land here, before the audit.**
7. **ALL generation — sources then renders. This is the LAST step that may write any file INSIDE THE REVIEWED CANDIDATE.** ⚠️ Steps 8, 11 and 12 do write tracked files later — the review receipt and the baseline record (both excluded from every manifest by `RECEIPT_PATHS`, which is why they may run later) and, after a Deck publish, the hosted Deck record `PROME/state/deck_owed_hosted.json` (an ordinary PROME path that rides the NEXT commit and is reviewed there). **An earlier wording said *anything tracked*, which those steps contradict.** Helm/Deck sources (`BRIEF.md`, `HANDBOOK.md` §Top priorities, `PROME/registry/WQ_EXPLAINERS.tsv`), then every generator: `python3 PROME/tools/will_handbook.py -o <scratchpad>/handbook.html` (since 10/3 it also writes `<scratchpad>/docket.html` beside the page — the Helm's supporting file, every pending PROME docket row with its cells whole; the page keeps one line per row; `PROME/tools/tests/ACCEPTANCE_helm_size_split_2026-10-03.md`) · `python3 PROME/tools/decision_deck.py`. The Deck generator writes both `decision_deck.html` (Owed) and `decision_reference.html` (Decided/In-flight/Docket); include both in the reviewed candidate. For hosted publication, generate with paired `--owed-url` and `--reference-url` pointing to the private native artifacts; local relative links are for local viewing only. ⛔ **Renders are NOT read-only** — they write tracked snapshot files (`PROME/state/brief_snapshot.json`, `brief_changes.jsonl`, `PROME/artifacts/*.html`). Generating after the freeze would put untracked-by-the-review bytes into the commit; that is why generation sits here and only **publication** comes after. **Then the deterministic checks, BEFORE the freeze (WQ-417 P4, Will 2026-10-10):** `python3 PROME/tools/table_check.py --quiet` · `python3 PROME/tools/done_rows_check.py` (rows the Deck/ledger parsers would skip; every done row's ruling in the ledger) · `python3 PROME/tools/wq_ledger.py check` · `python3 scripts/orch_log.py check` (L733) — a ❌ here is fixed HERE, so ARGUS never spends a read on what a script refuses. **After ANY correction pass, re-run the generators AND the same four checks** — a row fixed after the render ships with a stale Decided view (the 10/10 pass-1 errors were deterministic-class: a transposed column, replacements that never landed, a mis-dated ledger event).
8. 🔴 **FREEZE, then AUDIT (Standard/Heavy).** The candidate is complete — steps 1–7 done, including every check that can still produce an edit.
   `python3 PROME/tools/argus_scope.py --record-review` → spawn `argus` → apply ❌ only, ⚠️ → residue → RUN-LOG row (`python3 scripts/orch_log.py append --desk ARGUS --tier verifier …`, never typed — L733) → `python3 PROME/tools/argus_scope.py --mark-reviewed "<one line>"`.
   **If this closeout `git mv`'d a consumed packet from `PROME/inbox/` to `PROME/inbox/processed/`, DECLARE it at the freeze: `--record-review --consumed-move <ORIGIN> <DEST>` (repeatable) — and again at EVERY re-freeze, since a re-freeze rewrites the manifest. ARGUS confirms each pair (its agent file, legs (a) and (b) ①–③); the `--mark-reviewed` note carries its per-pair word. WQ-289 (b), DOCKET L473: the only way an EXCLUDED rename pair passes step 10's `--verify-review --paths`; every other addition at an EXCLUDED path keeps blocking. ⛔ `--consumed-move` is NOT VERIFIED — the live condition and the current reader round are DOCKET L488's state cell (L473 RESOLVED — FOLDED INTO L488 2026-10-08), never a round number written here; until that cell reads INDEPENDENTLY VERIFIED, a consumed packet is committed in a SEPARATE earlier commit, never inside the closeout candidate.**
   ⛔ **Freezing is NOT reviewing.** `--record-review` writes verdict `FROZEN`; only `--mark-reviewed` writes `REVIEWED`, and it refuses if the candidate moved in between. ⛔ **Any ❌ fix ⇒ re-review the changed portion, regenerate affected outputs, `--record-review` again, and re-mark.**
9. **FINAL gate, with the tier:**
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout --tier <bounce|light|standard|heavy> (--no-memory | --slug <name> …) (--no-superseded | --superseded <old> <new> …)`
   At **standard/heavy** a missing, unevaluable or merely-FROZEN review is **BLOCKING**. **Root steps 1c/1d are declaration-gated at every tier (2026-10-05):** `--no-memory` or one `--slug` per auto-memory written/edited, and `--no-superseded` or one `--superseded <old> <new>` per published figure superseded — an undeclared pair is a BLOCKING row; the gate runs `memory_index_check --strict --slug` and `consumer_check --strict` (fleet + `--self`) itself, and root step 1e (`claim_check --check weekday`) runs mechanically as an advisory. ⛔ **Omitting `--tier` does not mean “no tier” — it means the review requirement is NOT ENFORCED**, and the gate says so in its own line. Pass the tier you actually ran. **rc=1 ⇒ fix, regenerate every derived artifact whose sources the fix touched, re-freeze, re-run the FULL gate.** Loop to rc=0. ⛔ **rc=2 = INCOMPLETE: one or more checks DID NOT RUN and their subjects are UNKNOWN — never a pass, and not the same failure as rc=1.** Fix the missing/unreadable input the ERROR row names, then re-run the FULL gate; **do NOT proceed to step 10 on rc=2** (before this clause existed, a rc=2 closeout fell straight through to commit → verify → push).
10. **Commit → VERIFY → push. In that order, and the verification gates the push.**
    ```
    cd "$(git rev-parse --show-toplevel)"
    python3 PROME/tools/commit_check.py commit --stage -F <msgfile> -- <exact paths>   # NO --push
    python3 PROME/tools/argus_scope.py --verify-review --ref HEAD --paths <the same exact paths>
    bash scripts/safe-push.sh        # ONLY if the line above returned rc 0
    ```
    ⛔ **`--push` on the commit wrapper is forbidden at this step.** It pushes inside the same command, so the delivery check would run *after* the bytes were already on origin — detecting an unreviewed delivery once it has shipped is not a control.
    ⛔ **Both arguments matter.** `--ref HEAD` reads the COMMIT's contents, not the working tree — a path can be edited-then-reverted, or staged differently from the file on disk. `--paths` is the only way an **addition nobody reviewed** is detected; without it the check sees only paths the manifest already knows.
    **Push receipt, verbatim:** `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` A bare `Pushed.` is not a receipt.
11. **Publish the verified artifacts** (Standard+) — **the Deck OWED view at its private URL ONLY when the step-9 gate's *Deck republish (WQ-446 A, L738)* line reads OWED or UNKNOWN — NO-OP is quoted in the report, not published, the page unread (WQ-446 RULED A, Will 2026-10-15 16:16 ET; the set = every § OPEN row the page renders, raw cells + explainer row, plus the renderer's own fingerprint and the hosted-reference note; never the build stamp); after a CONFIRMED publish, download the hosted page (`Artifact` read with `path: index.html` — saved to the scratchpad, never inlined) and run `python3 PROME/tools/decision_deck.py --record-hosted-owed <version> --page <that downloaded copy>` in the same sitting — the record is copied from the receipt EMBEDDED in the page file (never from a build-receipt file, never recomputed: two builds in one minute share a build id, CATO SP6), so it describes the bytes the host holds; a failed or refused publish writes nothing, the previous hosted record stands; the record `PROME/state/deck_owed_hosted.json` rides the NEXT commit like the step-12 baseline (it is written after this sitting's commit; the next gate on the same machine reads it from disk, so only a machine switch before that commit sees a stale version — name an uncommitted record in the closeout report); the HELM ONLY on Will's word or at a spine audit (WQ-382 (b), Will 2026-10-09 18:41 ET, Deck tap APPROVE note "B", consumed 20:28 ET; encoded here 2026-10-15 at spine audit #16, DOCKET L665): a closeout that does not republish the Helm is NOT partial on publication.** When the Helm IS republished, it goes WITH its supporting file (the publish passes `files={"docket.html": "<scratchpad>/docket.html"}` on the same call **ONLY when the step-7 build line shows `+ docket.html`** — a build line reading `no docket file` means the page is in its legacy form and links nothing: publish the page alone, never a stale file; the page is the only thing the session must have VIEWED, the supporting file needs the in-session file LISTING taken at Pre-closeout item 5 or this session's own publish — the 10/3 split exists so the viewed page stays small). **The Deck REFERENCE view republishes ONLY on Will's word or at a spine audit (WQ-382 (a), Will 2026-10-08 20:09 ET, verbatim "WQ-382 AI pproved" on recommendation B): a closeout that does not republish it is NOT partial on publication; the sitting that DOES republish it updates `PROME/state/deck_reference_hosted.json` (built · version · artifact) in the same sitting so the Owed page's link renders the hosted build date (`decision_deck._hosted_reference_note`; a missing file renders UNKNOWN on the page). Fleet-Ops is RETIRED as a published page (WQ-372, Will 2026-10-02): it still BUILDS at every closeout because its state file feeds the closeout gate's L339 checks, but it is not published here; its two unique panels FOLDED into the Helm (DOCKET L594 APPLIED 2026-10-09; the symmetry row above re-wired 2026-10-15).** Keep Owed at the existing ruling artifact so its `rulings` store stays attached; verify reciprocal links and unchanged store access. A first reference artifact requires its private URL before generating the final paired candidate. They were generated at step 7 and verified at step 10; this step only ships them. Prerequisites were settled at Pre-closeout; a failure here is **reported**, never waived.
12. **ARGUS baseline, AFTER the commit:** `python3 PROME/tools/argus_scope.py --record-baseline HEAD`; it rides the next commit. ⛔ **The baseline record and the review receipt are never part of a reviewed candidate** — they are bookkeeping *about* a review, they change after the commit, and including them would make the next closeout inherit a guaranteed failure.

---

## Delivery — say which of the three was reached

⛔ **COMMITTED, PUSHED and PUBLISHED are three different states and the report names them separately.** A closeout that reaches two of three is **PARTIAL**, and the report says so with the **concrete blocker** — never a silent waiver because publication became inconvenient.

| State | Established by |
|---|---|
| **COMMITTED** | `commit_check` intent↔commit match, exact paths |
| **PUSHED** | the verbatim receipt above |
| **PUBLISHED** | the artifact republished at its own URL — or, for the Deck, the gate's WQ-446 line reading NO-OP, quoted in the report |

**Publication prerequisites are checked at Pre-closeout, not at the render** (`prome_gate closeout` → `publication prerequisites`): every OPEN `WILL_QUEUE` row has an explainer row, and, when the step-9 gate's Deck line reads OWED or UNKNOWN, the live Owed artifact has been viewed this session (the Helm's files also LISTED — Pre-closeout item 5) so the republish cannot be refused at the end; a Deck line that flips from the Pre-closeout preview to OWED at step 9 is handled by viewing the page then — not a process defect. **If a prerequisite cannot be met, say so at Pre-closeout and decide then** — an unmet prerequisite discovered at **step 11** is a process defect, not a reason to skip delivery.

**Session summary to Will:** what landed (commit hashes belong HERE, never in state files — they decay) · the three delivery states · **"Done without asking": each C1–C7 act of the session with its commit, or the word none (WQ-348 guard, `PROME/CLAUDE.md` § Ask First)** · **SKIPPED: any routine step not run, or run by reasoning instead of by the instrument, with its reason — and then the headline is PARTIAL whatever the three delivery states say (`PROME/CLAUDE.md` § Skipped-control reporting)** · what is owed at next boot · open `PROME/WILL_QUEUE.md` rows by number.

---

## Conditional procedures — explicit pointers

⛔ These do not run every closeout. **`PROME/CLOSEOUT_PROCEDURES.md`** holds: § Byte-flow and rotation recipes (incl. blind-reader verification) · § Chunk 3 residual triggers · § Skip rules · § Cross-session behavioral rules · § Closeout-class fleet memories.

**Historical rationale is NOT restated here.** Amendment history: `git log -p -- PROME/CLOSEOUT.md`; the WQ-240 simplification and the L338 sizing decision: `PROME/proposals/2026-09-12_wq240-closeout-simplification-RULED.md`.
