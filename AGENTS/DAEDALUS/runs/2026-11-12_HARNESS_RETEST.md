# Harness re-test, provider switch (Codex to Claude Opus 5.5) — 2026-11-12

**Commissioned:** Will, DAEDALUS window, 2026-11-12 ~09:07 ET, verbatim "okay do harness re-test". **Trigger:** `sweeps/HARNESS_AUDIT_SWEEP.md:7` (WQ-654 A item 5: a provider switch counts as a model upgrade; unconditional). DAEDALUS ran on Codex through 11/09 and on Claude Code Opus 5.5 today. **Scope (WQ-654 A item 4):** removals and simplifications only (WQ-577: no additions), plus git, authority and trade-path contradictions, read across every charter whether changed or not. **Brief:** `runs/harness_audit_2026-11-12/BRIEF.md`. **Ledgers (verbatim):** `runs/harness_audit_2026-11-12/READER_{P1,P2,U,C,K,E,F,M,S}.md`.

## 1. Coverage

Nine independent Opus readers (coldreader agent, `model: opus`), each reading its files whole; working tree at HEAD 29d4ac658b to df0b61849a (desks committed during the pass; line numbers are as each reader found them).

| Reader | Files | Rows | HIGH / MED / LOW |
|---|---|---|---|
| P1 root + PROME boot/closeout | root CLAUDE.md, AGENTS.md, USER.md, GIT_WORKTREE_PROCEDURES, PROME BOOT, BOOT_MODULES, CLOSEOUT, CLOSEOUT_PROCEDURES, COMPLETION_SPEC | 44 | 1 / 8 / 35 |
| P2 PROME charters | PROME CLAUDE, SYSTEM, AUTONOMY, ORCHESTRATION_PLAYBOOK (whole, first time) | 55 | 5 / 17 / 33 |
| U utility | WALTER CLAUDE + BOOT_PROTOCOL (whole, first time), NEXUS (whole), RED, TERRY + CLOSEOUT, DEWEY, ORACLE | 71 | 6 / 19 / 46 |
| C credit/bank | REGINALD, WAL (+AGENTS.md), OZK, FLG, GIBBS, BROCK, CREED, SHADE, LIQUID + CLOSEOUT | 91 | 5 / 8 / 78 |
| K consumer/labor | CARL + 7 sub-agents, HENRY, LABOR | 70 | 5 / 23 / 42 |
| E energy/geo | BRENT, HAWK, FALCON, OSPREY, YURI, WATT + CLOSEOUT, VULCAN, CYPHER | 69 | 4 / 16 / 49 |
| F Florida/housing | CORAL, MARCO + TOURISM, AEOLUS + 5 workers, FERT, CRUISE, HOMER | 58 | 10 / 26 / 22 |
| M markets | SAM, ZHAO, HANS + CLOSEOUT, BOND + CLOSEOUT, VIOLET | 78 | 4 / 35 / 37 |
| S special | MIDAS, OTTO, ISHM, DAEDALUS CLAUDE + OPERATIONS, RAV charter | 63 | 7 / 23 / 33 |
| **Total** | **74 files, about 1.9 MB** | **599** | **47 / 175 / 375** |

Excluded by roster: YEYOU (retired), BARON and SENTRY (dormant), ATHENA (not a launchable desk), CATO (manual-only by ruling). This closes the counterpart's two named gaps (ORCHESTRATION_PLAYBOOK, NEXUS and WALTER BOOT_PROTOCOL now read whole). **Not covered:** no runtime or hooks behaviour was tested (the readers judged text, not sessions).

Readers' by-eye savings estimates for seven of nine scopes sum to about 300 KB (P2 ~60, F 51, U 50, S 38, E ~40, C 35, P1 28; K and M gave per-file figures only). Estimates, not measured diffs.

## 2. DAEDALUS verification of the 47 HIGH rows

Every HIGH quote below was re-found at the working tree by `grep -F` (27 of 27 priority quotes present; OTTO's spans a line wrap). Re-grades:

| Reader HIGH | DAEDALUS verdict | Why |
|---|---|---|
| S-36 DAEDALUS `scripts/` grant; S-45 dormant-freeze pre-approval; U-W01 WALTER BOARD/LIAISON scope | **LOW (pointer fix)** | Grants exist: Will ~14:45 2026-07-31, recorded by PROME 1a82649101; Will 2026-07-04, recorded by DAEDALUS fd6e0d1de4 (self-recorded) and `sweeps/STALENESS_SWEEP.md` §3; ROSTER:48 gives WALTER the BOARD (LIAISON scope not traced). The charter text cites "via PROME" / PAT-036 instead of the record. |
| K01 CARL, K38 HENRY, K55 LABOR, M35 HANS, S-32 ISHM, F06 MARCO, C66 SHADE, S-01 MIDAS (desk-own packets to named consumers) | **KNOWN, not re-proposed** | WQ-508 R0 A (Will 2026-10-23) ruled a desk's own analysis or threshold fire to a named consumer is a packet, delivered direct; the 11/04 reconciliation dropped the root sentence and authorized no uniform routing sweep. Only internal self-contradictions (CARL :102 vs table, HENRY :51 vs :133) are worth a one-line owner fix. |
| F03 AEOLUS, F04 CORAL (no carve-out ① commit line) | **NO-OP** | Silence is not contradiction; root binds; adding the line is an addition (WQ-577). |
| U-R01 RED, U-D01 DEWEY bare `git pull` | **LOW** | Root's last Git sentence makes a charter's bare `git pull` mean `--rebase`. |
| U-R02 RED OUTBOX.md (215,709 B, last commit 11/10) | **MED** | Only `PROME/HEARTBEAT_COLD.md` names it; 0 "COMPELLING" items at present, so no live miss found. |
| U-O02 ORACLE outbox (27 files, 7/22 onward) | **MED, owner question** | Whether each reached its recipient was not traced. |
| All others in § 3 | **CONFIRMED** | Quotes present; contradiction stands against root/USER.md as cited. |

## 3. Changelist A — verified contradictions (owner edits, each makes text shorter or replaces it)

| # | File:line | Defect | Change |
|---|---|---|---|
| A1 | OZK :91 · FALCON :135 · YURI :100 · ORACLE :56 | Push-rejection (non-ff) shorthand skips root step 3's overlap check; OZK and ORACLE escalate a bare recurrence to Will | Replace with "non-ff → root Git Protocol session-end step 3" |
| A2 | LABOR :142 | `git commit AGENTS/SIGNALS.md` commits other desks' uncommitted rows; text claims to override root | Replace with "own rows only, root carve-out ②" |
| A3 | PROME/CLAUDE.md :39 | Force-push listed as ask-first; root says never | Move force-push to never |
| A4 | ORCHESTRATION_PLAYBOOK :106 | "leave commits to PROME's closeout sweep" contradicts root and carve-out ① | Replace with "root Git Protocol (own dir + carve-outs)" |
| A5 | ORCHESTRATION_PLAYBOOK :202 · PROME/BOOT.md :61 | Name checks retired 10/31 (WQ-578) as running at boot | Strike the retired names |
| A6 | ORCHESTRATION_PLAYBOOK :90-109 | Model table (PROME on Fable, desk spawns on `sonnet`) contradicts USER.md (desks Opus, readers Sonnet, Fable PROME-only) | Strike the table; point to USER.md |
| A7 | PROME/AUTONOMY.md :27 (+:29, :75) | Class index stale (C6 cap, C10–C13 missing), HANDOFF retired, WQ-673 written as pending | Strike the stale index lines |
| A8 | LABOR :232-235 | Exit template says "trim … partial exits", root rule #7 says trimming = thesis broken; LABOR holds no position | Strike the trim/partial-exit rows |
| A9 | BROCK :169 | "Thesis Kill (exit 100% …)" execution wording | Drop "exit 100%" |
| A10 | CORAL :123 | ">24h old" implies fresher STATUS prices may be cited; root rule #4 forbids any | "Prices: always live" |
| A11 | CRUISE :100 | Names PROME as owner of trade execution/sizing | "Trade construction → TERRY" |
| A12 | OTTO :386-398 | Trade flow via frozen TRADE.md → PROME → Will skips TERRY | One line: TERRY card, Will approves |
| A13 | HAWK :130-131 · FALCON :276 | "profit-taking alert" broadcast to all desks | Drop the phrase |
| A14 | MARCO :70 · BOND :78 | PROME requests to own outbox / "surface to PROME/Will directly … pending the messaging overhaul" (stale) | Point to root `PROME/inbox/` |
| A15 | FERT :16 · CRUISE :198 · OTTO :184-185, :342 · TOURISM :7 · VIOLET :183 | Name Claude-only tools (SendMessage, ListAgents, Agent tool, harness auto-memory, parent auto-load, Artifact) as the only route | "verified available channel/method (COMPLETION_SPEC)"; OTTO memory → repo `memory/auto/` |
| A16 | PROME/CLOSEOUT_PROCEDURES :67 · BOOT_MODULES :27 | Blocking review step spawns Claude-only `argus` / `anvil` with no Codex route | Same rewording (PROME's call) |
| A17 | USER.md :50 vs :52 | :50 still says cards carry a sell-or-roll rail; :52 bans sell-or-roll pushes in cards | **Will's file:** strike the "Cards, rulings and mirrors carry …" sentence, or keep it |
| A18 | DAEDALUS CLAUDE.md :93 · OPERATIONS.md :14 | Grants cited by hearsay / a pattern row | Cite 1a82649101 and `sweeps/STALENESS_SWEEP.md` §3 (own files) |

**Optional retirement (Will's fewer-rules direction):** the 7/4 dormant-freeze pre-approval was used once (the 7/4 dormant cluster) and 0 times in the 6 Staleness runs since; it could be retired with its text.

## 4. Changelist B — trims (the remaining MED/LOW rows, about 550)

History inside steps, duplicates of root and stale pointers across all 74 files; per-desk detail in the nine ledgers. Proposed form: one packet per desk carrying its own rows; each owner applies or declines at its next session (owner judgment, no direct edits by DAEDALUS). Known dead pointers to include: HENRY `power_watch.py`, META's eight missing files, OSPREY `/BOARD/INDEX.md`, VULCAN `KILL_MEMO.md`, HAWK `REMARK_20260628.md`, BRENT bare "RISK_RULES #5", ORACLE memory slug, CORAL/MARCO/OTTO desk-relative `scripts/` paths, AEOLUS/MARCO `LAST_COMPLETION.md`, `MEMORY.md`.

## 5. Status

**Ruled:** WQ-678 A, Will in PROME's chat 2026-11-12 09:59 ET, verbatim "677 B and 678 A" (`PROME/proposals/2026-11-12_wq678-RULED.md`, efb80255b4, verified). **Executed 10:1x ET:** 40 desk packets plus one PROME packet in commit 6a43711d27 (Changelist A 20 desk rows across 14 desks; B 447 optional; PROME A3–A7/A16 10 rows, 73 optional, 11 root rows left to PROME's judgment as Will-gated, 5 USER.md rows for the record only). Generated mechanically from the ledgers; one ID collision (reader S and reader P2 both use `S-nn`) was caught and fixed before commit. A18 applied in own `CLAUDE.md:93` and `OPERATIONS.md:14`. Own 28 B rows (DAEDALUS files and RAV charter) deferred to a later own session. **Not decided:** A17 and retiring the dormant-freeze pre-approval (Will's word). No desk launched.

**Addendum (Will, PROME's chat ~10:10 ET, "Can we junk them both?", then "One short line instead"; record `PROME/proposals/2026-11-12_wq678-RULED.md` § Addendum, verified):** A17 done by PROME (USER.md one line under "No expiry nagging"; sell-or-roll rail on cards withdrawn). The 7/4 dormant-freeze pre-approval is RETIRED: removed from `sweeps/STALENESS_SWEEP.md` § 3 (the pre-approved bullet and the grant block), `sweeps/FALSIFICATION_SWEEP.md` (pre-approvable class), `OPERATIONS.md` lines 14 and 16; text removed only, every freeze now surfaced for approval. The grant's history stays in git (fd6e0d1de4 onward) and in the Staleness Run Log. No WQ-678 desk packet carries a sell-or-roll instruction (RED's U-R04 cites the ban).

**Before the ruling:**

Detection complete; **no harness file edited** (all edits approval-gated). Changelist goes to Will as one decision via a PROME-registered WILL_QUEUE row. Clock: `last_run` stays 2026-10-04 until the approved changes are applied; this run is recorded as the provider-switch review.
