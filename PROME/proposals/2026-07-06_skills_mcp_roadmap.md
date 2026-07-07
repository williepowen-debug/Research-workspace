# Skills / MCP / Hooks Roadmap — outside-LLM feedback, PROME-annotated
**Created:** 2026-07-06 (Mon eve) · **Owner:** PROME · **Status:** BACKLOG — items 1-10 pending DAEDALUS harness-audit adjudication (see companion packet `AGENTS/DAEDALUS/inbox/2026-07-06_from-PROME_harness-audit-loops-md.md`)
**Provenance:** Will ran the repo past an outside LLM through a skills/MCP lens (7/6); ranked list below is its output, PROME annotations in **[PROME:]** brackets. Converges independently with the Karpathy LOOPS.md Rule-8 theme (harness needs deliberate pruning/encoding discipline) — the two inputs are one workstream.

## Ranked backlog

| # | Item | Type | Sig | Effort | PROME annotation |
|---|---|---|---|---|---|
| 1 | **`calibration` skill** — pre-register → invalidation leg → grade-against-line → scoreboard → threshold-vs-mechanism tag, as one versioned procedure | skill | 10/10 | M | **[PROME: agree, crown jewel — it IS the methodology; currently convention-enforced across ~15 agents. Prototype on ONE agent's loop first (LABOR or HENRY predictions), validate, then fleet. Project-level skill in-repo = shared both machines.]** |
| 2 | **SEC EDGAR MCP** — FTS + section fetch + XBRL native | MCP | 9/10 | M-L | **[PROME: DEMOTED. Sharp edges already scripted (EDGAR FTS + FDIC API, both in auto-memory); standing MCP server = runtime cost on serial two-box for capability we mostly have. Its own "single-machine tax" caveat argues against it. Revisit only if footnote-grain errors recur despite scripts.]** |
| 3 | **SessionStart hook** — boot enforcement (fetch + ahead/behind + env_doctor/firetime flags) | hook | 8/10 | S | **[PROME: ✅ BUILT 7/6 eve — `.claude/settings.json` + `scripts/session_banner.sh` (flag-not-force: fetch w/ 10s timeout + ahead/behind + dirty-tree + env_doctor flags; never pulls; cwd-proof; pipe-tested both cwds). In-repo = both boxes. Live for every session launched after 7/6. PROME-specific gates (firetime) stay in BOOT.md.]** |
| 4 | `signal-routing` skill (modernized WALTER) | skill | 7/10 | M | **[PROME: real but WALTER-owned — route to WALTER, don't build over its head. Audit adjudicates.]** |
| 5 | `nexus-brief` skill — write-once-read-many schema + FRESH/PIN-STALE/CONTENT-STALE rules | skill | 6/10 | S-M | Audit adjudicates encode-vs-convention. |
| 6 | **FRED MCP** — native macro-series pulls | MCP | 6/10 | S-M | **[PROME: same demotion logic as #2 — fetch.py works, .env single-home solved the key problem. Ergonomics only.]** |
| 7 | `red-review` skill — RED's challenge framework as invokable procedure | skill | 6/10 | S | **[PROME: attractive but risks diluting RED's standing-adversary role — a self-serve version may become a checkbox. RED should co-own the call.]** |
| 8 | `repo-git-protocol` skill — pathspec/safe-push/pull recipes | skill | 5/10 | S | Audit adjudicates; overlaps root CLAUDE.md Git Protocol (canon must stay single-home). |
| 9 | `market-data` tools → MCP | MCP | 4/10 | M | **[PROME: skip — refactor of working tooling, lowest urgency, same MCP tax.]** |
| 10 | Retire/rebuild stale `walter` skill (refs Toscanini/HERMES/clawdbot) | hygiene | 3/10 | S | **[PROME: ✅ DONE 7/6 eve — verified real at root `skills/` (walter + jina-reader + youtube-transcript, all `.clawhub` OpenClaw provenance, NOT loaded by CC which reads `.claude/skills/`); walter SKILL.md carried stale thresholds (HY >320 vs live 280 X1) + retired Toscanini/HERMES/`sessions_spawn`. Whole dir `git mv` → `archive/skills-openclaw/` (no live consumers — grep-verified; SYSTEM.md mirror rows swept). Any rebuild = WALTER-owned per #4.]** |
| 11 | **PreCompact write-back hook** — inject "write hot state to SCRATCH/STATUS now" before auto-compaction | hook | 6/10 | S | **[PROME addition 7/6 — the outside review missed it (no visibility into fleet failure history): long sessions losing hot state to compaction is an observed incident class ([[finding_workflow_scratch_crash_recovery]], closeout-as-write-back-tail canon). Same flag-not-force shape as #3. Build on Will's call or after the DAEDALUS audit.]** |

## Two structural cautions (theirs, endorsed)
- **Single-machine tax:** every MCP = a server to keep alive on serial desktop⇄laptop. Lean skill/hook-first; reserve MCP for genuine new capability.
- **Skills rot like docs:** whatever gets built inherits the FROZEN-or-LIVE hygiene rule. The dead `walter` skill is the proof case.

## Sequence (PROME recommendation, Will 7/6)
1. **#3 SessionStart hook** (S, immediate enforcement, fleet-wide benefit, near-zero rot risk — dynamic checks, not encoded doctrine).
2. **#1 calibration skill prototype** on one agent, validated before fleet rollout.
3. Everything else waits on the **DAEDALUS harness audit** (encode vs prune vs leave-as-convention, per item).
