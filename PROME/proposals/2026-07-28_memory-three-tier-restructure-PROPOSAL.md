# PROPOSAL — Auto-Memory Three-Tier Restructure (Phase 2)
**Author:** PROME · **Date:** 2026-07-28 ~06:40 ET · **Status:** ★ **APPROVED 2026-07-28 ~06:50 ET (Will in-session: "lets go with your recommendations")** — all four open questions resolved to the recommendations: **Q1** single `INDEX_COLD.md` (split trigger ~40KB or a theme gaining a routine consumer) · **Q2** Prediction section moves behind `PREDICTION_DISCIPLINE.md` with a ~10-row hot residue · **Q3** WALTER owns the sibling-merge sweep (DAEDALUS consulted on blueprint embeds) · **Q4** tier map approved WHOLESALE; judgment sections refine at first sweep. **Execution: PROME migration session scheduled ~weekend 8/1-8/2 (DOCKET row registered 7/28)** — FOMC-week spine outranks it per the sequencing rec Will accepted. WALTER checker-v2 REQ routed 7/28 ahead of the split (the 80% byte warning is valuable immediately).
**Supersedes:** the two-way hot/cold sketch in the 7/28 Phase-1 compaction plan. **Prereq done:** Phase-1 compaction `c715548d` (21.8→17.9KB, 322 slugs intact).

## 1. Problem (measured)

- `MEMORY.md` is auto-injected into EVERY agent boot; harness read cap **24.4KB**. Post-compaction: **17.9KB (73.5%)**.
- Accrual: steady-state **15–35 memories/week**, burst **~30 in 2 days** (W31). Index re-hits 80% within weeks; stock (~323 files) will pass 1,000 by year-end. A single boot-loaded index structurally cannot hold the fleet's learning rate.
- Waste identified: cross-agent duplicate-class creation (sibling lessons banked as separate files); nobody owns dedup.

## 2. The design key: split by WHEN A LESSON FIRES, not by topic

The harness has exactly two loading modes: in `MEMORY.md` = always in context; elsewhere = on-demand. So every split decision is really "does this lesson keep auto-fire?" The classification:

| Tier | Trigger profile | Home | Loading |
|---|---|---|---|
| **1 HOT** | Unpredictable — fires mid-work on whoever is moving fast (verify-before-acting, git safety, record-vs-reality) | `MEMORY.md` | auto, every boot |
| **2 EMBED** | Predictable consumption moment (card-build, spawn, boot, closeout, registration, tool-use) | The artifact consulted AT that moment | fires at 100% when relevant, 0 bytes otherwise |
| **3 COLD** | Rare / historical / project-state | `memory/auto/INDEX_COLD.md` | on-demand via pointer block in MEMORY.md header |

Rules: memory FILES are never deleted or moved — only index rows move. Every Tier-2 embed = the one-line rule copied into the target + `[[slug]]` link; its index row moves to COLD annotated `embedded → <target>`. Rollback = one line back to hot.

## 3. Tier map (per current section; counts approximate)

| Current section (rows) | Tier | Embed target / notes |
|---|---|---|
| Boot/closeout/revival/sync (17) | **2** | `PROME/BOOT.md` + `PROME/CLOSEOUT.md` (PROME-owned) + DAEDALUS agent-blueprint boot cards. The moment IS boot — the docs read at boot are the right carrier, not the index. |
| Sub-agents/teams/workflow (35) | **2** | `PROME/ORCHESTRATION_PLAYBOOK.md` (BOOT.md already mandates reading it before any multi-spawn) + `PROME/COMPLETION_SPEC.md` (delivery-contract rows: idle≠result, terminated-can-precede-delivery, ship-artifact-skip-writeback). |
| Git/multi-machine (22) | **1 + graduate** | Stays HOT (unpredictable, protects shared state) — EXCEPT ~8 rows already verbatim in root `CLAUDE.md` Git Protocol (pathspec, safe-push, add-scope): retire those as `embedded → root canon`. |
| Verify-before-acting (41) | **1** | The crown jewels; 5 live saves on 7/28 alone. Note partial graduation to `claim_check.py` (weekday/hash/units/pointer) but keep rows hot — the checker runs at closeout, the lesson prevents the error mid-session. |
| Prediction & calibration (33) | **2 + residue** | New fleet artifact `FORGE/PREDICTION_DISCIPLINE.md` (or DAEDALUS blueprint section) cited by every prediction ledger/registration template; ~10 sharpest operational rules stay HOT (inversion test, FROZEN-vs-TRACKED, made-date check). ⚠️ Judgment section — weakest natural "moment"; see open question Q2. |
| Numbers/data/staleness (26) | **1** | Unpredictable; stays. |
| Cross-agent coordination (27) | **1** | Unpredictable (fires when routing); stays. A few redundant-with-messaging-spec rows flagged for WALTER review. |
| Doc/state-file hygiene (27) | **1 + partial 2** | Mostly hot; ~6 closeout-moment rows (writeback-tail, state-token sweep, completion-stamp) → `PROME/CLOSEOUT.md`. |
| Trade/position/risk (11) | **2** | `AGENTS/TERRY/RISK_RULES.md` + card templates (root canon already names TERRY canonical owner of rules 6-7; domain-data agents never needed these rows). Cleanest section-level move. |
| Rail & scope (3) | **1** | Tiny; PROME-relevant; stays. |
| Evidence & source quality (31) | **1 + partial 2** | Mostly hot; the 4 `deep_research_*` rows → DEWEY's CLAUDE.md (which ALREADY cites them inline) — pure dedup. |
| Agent-specific pointers (19) | **2** | Each agent's own CLAUDE.md/boot card. A fleet-wide boot payload is the wrong home for one agent's dashboard link. Cleanest win. |
| Infra/tooling/project-state (26) | **1/2/3 split** | Tool gotchas → tool headers/doctor checks (Tier 2, `orphan_check` header is the existing pattern); `project_*` state rows → COLD; genuinely unpredictable classes (unversioned-secret, hardlink-edit) stay HOT. |
| User preferences (2) | **1** | Stays. |

**Projected hot index: ~150–180 rows ≈ 9–10KB (~40% of cap)** — years of headroom at disciplined append rates with turnover.

## 4. Mechanics

1. **Files:** `MEMORY.md` (hot) + `memory/auto/INDEX_COLD.md` (single file, same theme headers; split into themed files only if it exceeds ~40KB). MEMORY.md header gains a 3-line pointer block naming what lives cold.
2. **Ownership-respecting migration:** PROME edits only PROME-owned targets (BOOT, CLOSEOUT, ORCHESTRATION_PLAYBOOK, COMPLETION_SPEC) + the two index files. All other embeds go as **packets to owners** (TERRY, DEWEY, DAEDALUS-for-blueprints, per-agent pointer rows). Index rows move to COLD immediately with `embed-pending → <target>` so the hot index shrinks now; owners confirm embeds async; PROME flips the annotation on confirmation.
3. **Checker extension (REQ to WALTER, owner of `memory_index_check`):** (a) validate slugs across BOTH index files; (b) every memory file in exactly ONE index — no orphans, no double-listing; (c) **byte warning at ≥80% of 24.4KB on MEMORY.md** (the mechanized compaction trigger — closes the BOND/DEWEY hook-conflict class); (d) `embed-pending` rows older than 14d re-flag.
4. **Canon amendment (root `CLAUDE.md` carve-out ③ text, Will-gated):** (a) append format — one line, ≤140 chars, slug + minimal hook; (b) **dedup-before-create** — a new memory file must name the existing slugs checked first; extending an existing memory (n+1 instance) is the DEFAULT, a new file the exception; (c) new rows go HOT only if unpredictable-trigger, else cold/embed; (d) **size-hook conflict rule (BROCK 7/28, packet in PROME inbox):** when the harness's MEMORY.md size hook fires ("compact it now"), **flag to PROME — do not compact.** The hook is harness-native (no matching hook in any settings.json BROCK could find) and instructs an action carve-out ③ forbids; an agent with no guidance will likely obey the hook because it is the thing shouting at that moment. The restructure fixes size, not instruction — the hook re-fires for whoever edits the index past ~21KB. This line converts a silent conflict into a routing step.
5. **Sibling-merge sweep:** periodic (monthly) cross-agent dedup pass — merge same-class sibling memories into one file with instance lists. Owner: open question Q3.
6. **Safety rails (same as Phase 1):** slug-set conservation across both indexes (zero deletions), hardlink-preserving writes, `--strict` clean before commit, one-commit migration for the index split, cross-machine union-merge by slug applies to both files.

## 5. Rollout

1. Will approves/edits the §3 tier map (wholesale or per-section — Q4).
2. PROME executes: index split + COLD file + PROME-owned embeds (one session).
3. PROME routes embed packets (TERRY, DEWEY, DAEDALUS, WALTER-REQ; per-agent pointers batched into next-boot packets).
4. WALTER ships checker v2; canon amendment lands at the next canon pass.
5. First sibling-merge sweep runs after migration settles.

## 6. Open questions for Will

- **Q1:** Single `INDEX_COLD.md` vs themed cold files from day one? (Rec: single file, split later.)
- **Q2:** Prediction section — full Tier-2 move behind a new `PREDICTION_DISCIPLINE.md`, or conservative (keep all 33 hot until the artifact proves it gets read)? (Rec: move with 10-row hot residue; the ledger templates give it a real consumption moment.)
- **Q3:** Sibling-merge sweep owner — WALTER (owns the checker, signal-hygiene mindset) or DAEDALUS (owns agent structure/maturity)? (Rec: WALTER, with DAEDALUS consulted on blueprint-level embeds.)
- **Q4:** Approve the tier map wholesale, or walk the two judgment sections (Prediction, Infra) row-by-row first?
