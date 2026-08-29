# CANON_PROVENANCE.md — the reasons behind root `CLAUDE.md`

**Purpose:** root `CLAUDE.md` carries rules only. **Every block below carries a stable `key:` and a `root-anchor:` (a phrase that must appear verbatim in root) — the parity test (REVIEW §5 test 3) fails when an anchor vanishes from root, i.e. when a rule is deleted or reworded without its provenance being revisited.** This file carries the incidents, dates, counts, rulings and superseded wording that produced them — keyed by root section, in root order. **Not auto-loaded; read when you want to know WHY a rule exists or argue for changing it.** Exact amendment history: `git log -p -- CLAUDE.md`. When this file and root disagree on a RULE, root wins; when they disagree on a DATE or COUNT, this file wins (root no longer carries them).

*Created 2026-08-29 — Will-ruled WQ-120 (verbatim "approved go ahead"), RAV pass 2 PASS. Text is moved verbatim from root at commit `981ea5e44` wherever it was prose; condensed only where the original was itself a summary. Parity check: every `root-anchor:` below must appear verbatim in root.*

---

## How The System Works

- `key: system-platform` · `root-anchor: serial multi-machine, desktop ⇄ laptop, ONE at a time`
  **Platform:** the OpenClaw/VPS platform was cut 2026-06-26 — `AGENTS/WALTER/design/OPENCLAW_CUTOVER_PLAN.md`. Historically PROME also ran an always-on OpenClaw surface; there is now one PROME on one machine at a time.
- `key: system-prome-address` · `root-anchor: Write to `PROME/inbox/``
  **Coordination address (root line 18):** Will-ruled WQ-118, 2026-08-29, on spine audit #11 blocking #1. Root had said "Write to `AGENTS/<NAME>/outbox/` to request Prome action" and never named `PROME/inbox/`; canon (Will 2026-07-24; `PROME/BOOT.md` step 6; `MESSAGING/DIRECT_MESSAGING_V1_SPEC.md` §6) had made `PROME/inbox/` the sole delivery surface since 7/24. The missing positive address is the suspected feeder for the `AGENTS/PROME/inbox` regrowth (removed 7/24 → re-grew 8/27 → 8/28 REGINALD). Memory: `finding_prome_inbox_is_repo_root_not_under_agents`.
- `key: system-deliver-before-idle` · `root-anchor: final action before going idle`
  **Teams-mode deliver-before-idle:** agents idling "holding" without delivering forced the coordinator to chase them — rule added at the 2026-06 orchestration hardening.
- `key: system-roster` · `root-anchor: `PROME/ROSTER.md` is the single source of truth`
  **Roster count history:** 31→32 at the 2026-08-20 FLG build (Flagstar Financial single-name, the fleet's first greenfield per-bank build); 32→33 at the 2026-08-21 CRUISE re-class (ARCHIVE/personal-interest → EVENT-DRIVEN, Will-ruled queue row 55); both mirrors reconciled 2026-08-21 under in-session words. Tier 2 (spawned as needed): CREED, DEWEY, HANS, OTTO. Special: YEYOU (repo-wide reviewer, manual/branch model), DAEDALUS (fleet architect meta-agent, on-demand), RAV (interim QC reviewer, Will-ratified 2026-08-02). Spinout/promotion provenance (OZK, CORAL, AEOLUS, HOMER, OSPREY/FALCON, WAL [promoted 2026-07-25 — that queue's named successor is UNASSIGNED; nominations = DAEDALUS maturity review, Will-gated]) → `PROME/ROSTER.md`. ROSTER's five responsibility classes are descriptive.
- `key: system-potash` · `root-anchor: Potash is triage-only at FERT`
  **Potash → FERT at triage depth:** Will-ruled in-session 2026-08-18; guard encoded at the owner 2026-08-19 `beb3a36cb` — scope + 4-benchmark table + triage form landed in ONE edit, per the ruling. FERT owns the full N-P-K complex for routing. The rule guards against the ~$270/ton predecessor-killing mislabel; the 8/18 WALTER-caught provenance correction is recorded in FERT's `CLAUDE.md` §POTASH. Deep-dive depth is revisited once N+P benchmark discipline is demonstrated — a real trigger, not a permanent ceiling (FERT charter's words).
- `key: system-position-truth` · `root-anchor: Position truth is off-repo`
  **Position truth / FORGE:** the on-repo `WILL/trading-journal/` photos were removed in the 2026-06 public-prep cleanup; position truth moved off-repo. FORGE reconcile vintage: a hardcoded-date mirror ("7/20") was removed 2026-07-30, Will-approved — it said "7/20" for hours after the 7/30 reconcile (PAT-068 class-kill). FORGE owner = PROME since 2026-07-30 (DAEDALUS FORGE-audit S1, Will-ruled — reconciles run as PROME-directed spawns; FORGE commits PROME-standard; the root line stays Will-gated). `FORGE/PORTFOLIO.md` superseded 5/21 per its own banner — line corrected 2026-07-28, Will-approved, after VIOLET flagged the position-missing symptom (the frozen banner was the cause).

## Critical Rules

- `key: critical-rule-3` · `root-anchor: Agent data can be hallucinated`
  **Rule 3 example:** PSEC PIK was 8.6%, not 35% — the hallucination that produced the rule.
- `key: critical-rule-6-7` · `root-anchor: Rules **6–7** are trade-construction rules`
  **Rules 6–7 ownership:** consolidated at TERRY; numbers frozen as a stable API because TERRY fire-cards cite "rule #6" by number.
- `key: critical-rule-citation` · `root-anchor: never a bare "rule #6."`
  **Numbering collision:** found by TERRY 2026-07-27 while promoting the break test; flagged to Will same session. Root #6 = "puts on green days, calls on red days"; Non-Negotiable #6 = "no roll-by-hope". Neither list can be renumbered (both cited by live cards), so the fix is citation discipline, not renumbering.
- `key: critical-rule-6-break` · `root-anchor: refutes the day-colour proxy`
  **Breaking root rule #6:** adjudication test ratified by Will 2026-07-27. Full test + worked example → `AGENTS/TERRY/RISK_RULES.md`.

## Output Canon

- `key: output-canon` · `root-anchor: Tables > prose. Numbers > narrative`
  Consolidated to root 2026-07-07 (harness-audit strike S1/S4, Will-approved) — per-agent restatements removed.
- `key: output-strict-text` · `root-anchor: Cost-bearing text & state tokens`
  Cost-bearing text & state tokens: 2026-07-31, Will-approved; the 10 rules are `STRICT_TEXT.md`; the vocabulary is `STATE_VOCABULARY.md`.

## Git Protocol

- `key: git-push-auto` · `root-anchor: push is automated at closeout`
  **Push automation:** OpenClaw/VPS cut 2026-06-26; auto-push at closeout replaced the manual Will push window ("the push-train, now automated"). Lazy-sweep to all active agents completed 2026-06-27; stale-parenthetical fix 7/11, Will-approved. Memory: `finding_push_train_pattern`.
- `key: git-carveout-1` · `root-anchor: ① Self-authored inbox packets`
  **Carve-out ①** ratified 2026-07-23, Will-approved — HENRY orphan-gap memo: ~12% of packets orphaned by uncommitted inbox writes pre-detector.
- `key: git-carveout-2` · `root-anchor: ② Self-authored shared-log rows`
  **Carve-out ②** Will→LABOR 2026-07-24, generalized fleet-wide 2026-07-25 Will-approved. An uncommitted shared-log edit orphans by design (`orphan_check.sh` correctly tells every other agent `[not yours]`).
- `key: git-carveout-3` · `root-anchor: ③ Self-authored auto-memory files`
  **Carve-out ③** ratified 2026-07-27, Will-approved — proposed by WALTER 7/25 in `docs/AUTO_MEMORY.md`, forced by an n=6 orphan day: six orphaned memories from four agents in one day, three more appearing while the first three were being fixed. The `--slug` form warning: bare `--strict` blocked a closeout on another agent's orphan within an hour of the flag shipping (2026-07-27). Step 1d was added 2026-07-28 (BROCK proposal) because detection was never the gap — invocation was (9+ orphans from ~5 agents in one day with a working detector). The `check_memory_length.sh` line was added 2026-08-04 (Will-approved 8/3, DAEDALUS canon bundle ①): measured 2026-08-03 at 74% of the byte cap on 12% of the line cap — the 7/31 three-tier restructure made rows long single lines; the guard had a soft tier for lines and none for bytes; DAEDALUS added `soft_bytes` at 80% the same day. "Do not compact MEMORY.md yourself" — Will-ruled 7/28.
- `key: git-carveout-4` · `root-anchor: ④ Gate C Kernel shadow paths`
  **Carve-out ④ + Gate C custody:** enumeration of governance records reconciled 2026-08-27 (C8 review finding N5, Will-worded) — the C7 pilot's runbook already instructed those commits while root did not name them (mirror-lag class, n=3). Carve-out count wording corrected 2026-08-29 (WQ-119, RAV F1): root said "the ONLY three" while ④ sat below it.
- `key: git-scope-note` · `root-anchor: Scope note — who commits what`
  **Scope note:** HEARTBEAT ungated 2026-08-23 (record `PROME/proposals/2026-08-23_heartbeat-gate-RULED.md`; measurement: 117 HEARTBEAT commits / 60d, 82 carrying a Will word, zero declines, no defect the gate ever caught — freeing changed LATENCY, not detection; re-gate trigger = any HEARTBEAT defect reaching Will unrepaired past one weekly spine audit). FORGE ungated 2026-07-30. **This root line carried the FORGE entry as Will-gated for 24 days after the grant** and the HEARTBEAT entry until the same-day sweep — ungating a surface reliably leaves its root mirror behind (n=2); when a surface is freed, grep root for its name that sitting. WALTER's auto-push exception cites `BOARD_CONSUMPTION_SPEC` §7; DAEDALUS's 2026-08-26 packet (finding D1) flagged that WALTER's own `CLAUDE.md` and practice contradict that clause — reconcile owed at WALTER, unresolved as of 2026-08-29 (spine audit #11 minor). YEYOU per Auto-push Decision C.
- `key: git-step-1b` · `root-anchor: 1b. **Orphan check:**`
  **Step 1b orphan check** adopted 2026-07-23, Will-approved.
- `key: git-step-1c` · `root-anchor: 1c. **Consumer check:**`
  **Step 1c consumer check** adopted 2026-07-28, Will-approved — HENRY-built, the orphan_check adoption path. Born from VIOLET carrying HENRY's stale gamma flip as a live position's kill line for 5 days — the check is one grep; the failure was that nobody ran it. The `--old` repeat guidance: root batch item 5, Will-ruled 2026-08-21; HENRY-endorsed, `38ad4495d`; live instance VIOLET's 8/20 `--self` 3-of-3 false 🔴. The `--self` form: the cross-agent scan deliberately excludes your own dir — ~25 of the 7/31 audit defects were intra-agent (HOMER 7 · CARL 7+ · MARCO 4+ · ORACLE 4 · LABOR 3). Tool demotes uncertifiable hits to 🟠 since 8/7.
- `key: git-step-1c-bis` · `root-anchor: 1c-bis. **Ledger nudge:**`
  **Step 1c-bis ledger nudge** adopted 2026-08-20, Will-approved — DAEDALUS staleness-cadence proposal (b), "approve the staleness proposal"; shipped `747fe1472`; nudge v2 8/20 enumerates all ledgers count-first; "each" reconciled 2026-08-21 root batch — the counter is STATUS-writes, not weeks. First live runs caught four desks 6–30 writes behind.
- `key: git-step-1d` · `root-anchor: 1d. **Memory-index check:**`
  **Step 1d memory-index check** adopted 2026-07-28, Will-approved — BROCK proposal; it puts carve-out ③'s existing enforcement into the sequence agents actually execute (detection was never the gap; invocation was). YEYOU exempt (manual/branch model, Auto-push Decision C).
- `key: git-step-1e` · `root-anchor: 1e. **Claim check:**`
  **Step 1e claim check** adopted 2026-08-04, Will-approved 8/3, DAEDALUS canon bundle ③. n=4 fleet-wide, once inside the ruling record of a Will-pre-authorised mechanical execution. Scope from measurement: decision classes = 13 files / 1 flag; whole tree = 6,197 files / 131 flags — tree-wide would ship alert fatigue.
- `key: git-step-2` · `root-anchor: is on origin/master (fresh fetch).`
  **Step 2 push receipt:** `safe-push.sh` prints `Pushed. CONFIRMED: HEAD … on origin/master` since 2026-08-28 (DAEDALUS); rc=2 CANNOT-CONFIRM added `e0ce45241`. "Pushed." can be true about SOMEONE ELSE's commits — `finding_push_train_hides_a_failed_commit`.
- `key: git-step-3` · `root-anchor: If safe-push aborts (non-ff), do NOT force`
  **Step 3 non-ff:** re-based 2026-08-03 (CORAL packet + RED 7/31 precedent, Will-approved): verified same-box committers with ZERO path overlap — a non-ff is a property of the commit graph, not file paths, so separate directories cannot prevent it; only per-agent branches could. `--autostash` reconciles the fix with "never pull over others' uncommitted work" — RED verified byte-identical restoration. The old "recurs mid-session" tripwire fired on routine same-box pushes and produced a false escalation (CORAL 8/3) — retired. RAV 2026-08-29: the overlap check is prose and `--autostash` is not fully safe; a separate explicit recovery tool is designed at `PROME/proposals/2026-08-29_nonff-recovery-tool-DESIGN.md` (RAV review pending).
- `key: git-before-committing` · `root-anchor: Never `git commit --amend``
  **Before committing:** the pathspec pattern exists because of the shared-`.git/index` race — `finding_pathspec_commit_race_safety`, incident `8ac5bf71` Jun 4 2026. Step 0 (repo-root cwd): from an agent's launch dir `git commit AGENTS/<NAME>/<file>` fails loudly but `git status -- AGENTS/<NAME>/` silently shows nothing. Step 4b (never amend): Will-approved 2026-08-21, DAEDALUS proposal `548d06e87`; n=3 across 3 desks Aug 2026 — one amended a PUSHED commit; record + repair preconditions → `finding_backtick_command_substitution_in_commit_message`. Step 5 validated 2026-06-26: first use caught 53 foreign pre-staged files mid-race + a months-old display-copy desync; the `git mv`-vs-bash-`mv` residue class → `feedback_git_mv_for_inbox_processing`. Commit-message overclaims (d3915f75d 8/28, 6704cfc37 8/29) → `PROME/tools/commit_check.py` (RAV review 8/29).

## Data Hygiene

- `key: data-hygiene` · `root-anchor: STATUS is canonical truth`
  Closeout discipline ratified 2026-06-26 after a 5-agent architecture review — `PROME/cluster/2026-06-26_fleet_arch_compare.md`.
- `key: data-mtime` · `root-anchor: Never key a NEW freshness/throttle mechanism on mtime`
  **mtime rule:** VIOLET 7/27, `finding_mtime_is_corrupted_by_git_sync`; wording amended 2026-07-28 per DAEDALUS ruling, Will-approved — the enforcer had preferred content-vintage since 7/22, the line had lagged it. PAT-044 = the two-clock header.
- `key: data-retirement` · `root-anchor: Research/sources retirement`
  **Retirement two-clause amendment:** Will-ruled 2026-08-21 root batch — deliberately-dormant fire-time artifacts fail the boot-read test by design, and archiving one breaks the gate at fire-time; indexes enumerate everything, so counting them makes every indexed file immortal and the rule dead.
- `key: data-read-cap` · `root-anchor: 32,550 B`
  **Read-cap byte budget:** Will-approved 2026-08-28, P1 — 60% of the harness single-read cap (25,000 tokens × 2.17 B/token measured on fleet markdown ⇒ ≈54,250 B). Spine audit #11 (8/29) found PROME's own CLOSEOUT/prome_gate still keyed to the retired 51,200 B budget one day later.
- `key: data-messaging` · `root-anchor: Direct Messaging v1`
  **Direct Messaging v1 first cohort:** Will-approved 2026-07-14. Cross-session messaging first use 2026-08-16; awareness posture Will-ruled 8/16 late (verbatim word in the ruling packet); pointer line Will-approved 2026-08-16; rule 6b (dark-owner doorbell-PROME branch) added 2026-08-23, Will-approved — "Approve the one-line root CLAUDE.md mirror amendment pointing dark recipients to rule 6b."

## Reference

- `key: reference-cost-model` · `root-anchor: Status key`
  **Cost model line** ("Heavy research on Sonnet, synthesis on Opus. Typical sub-agent: $0.02-0.05. Long research: $0.10-0.20.") deleted 2026-08-29 (WQ-119, RAV F5) — stale, not a rule.

## AGENTS.md (routing topology — same rules-vs-provenance split, WQ-123, 2026-08-29)

- `key: agents-routing-table` · `agents-anchor: 34 rows: 31 of the 33 live ACTIVE agents`
  **Table count history:** the caption said "~20 rows against 30" from authoring — never true; corrected 8/6 (Will-directed review) to 31 rows; 31→32 at the 2026-08-16 FERT registration; 32→33 at the 2026-08-21 FLG row (build 8/20, Will-ruled root batch); 33→34 same day at the CRUISE re-class row (Will-ruled queue row 55). **Potash line history:** the chain-10 line read "Potash = UNOWNED, routes to PROME" for 3 days after Will's 2026-08-18 triage-only ruling; reconciled 2026-08-21 under the root-batch word — but the FERT TABLE ROW kept "potash EXCLUDED-UNOWNED" until WQ-123 (2026-08-29); Codex's 2026-08-24 evaluation (line 26) named the pair as evidence that an annotated correction does not clear the mirrored cell. **Dropped sections (WQ-123):** `First Message` (PROME boot pointer in a fleet file), `Safety` and `Core Principles` restated root Critical Rules 5/11 + AUTONOMY; the one load-bearing line (Gate C carve-out ④ pointer, KERNEL readiness plan C2) survives in the `Pointers` block.
