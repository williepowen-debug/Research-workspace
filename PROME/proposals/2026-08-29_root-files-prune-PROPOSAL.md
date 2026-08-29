# Root-files prune / merge / condense — PROPOSAL
**Author:** PROME · **Date:** 2026-08-29 (Sat, second session, Will-directed: *"examining our root files and looking for opportunities to prune, merge, condense"*) · **Status:** PROPOSED — WQ rows 122 · 123 · 124
**Scope:** the 8 tracked root-level files + a one-line census of the 12 root-level directories. Root `CLAUDE.md` (20,621 B) and `HEARTBEAT.md` (21,286 B) were restructured yesterday (WQ-120 / WQ-121) and are OUT of scope here.

## 1. Inventory (measured 8/29 12:1x)

| File | Bytes | Last commit | Boot-read by | Live citations (excl. archive/memory/inbox) | Verdict |
|---|---|---|---|---|---|
| `AGENTS.md` | 10,198 | 8/26 | PROME on-demand (roster/routing) | root CLAUDE.md ×2 · ROSTER · _INDEX · KERNEL Gate-C docs · `canon_check.py` / `consumer_check.py` target lists | **CONDENSE** (WQ-123) |
| `KERNELS.md` | 8,502 | 6/30 (2 commits ever) | nobody | USER.md grant line · LESSONS.md · SYSTEM.md rows 43/88 | **RETIRE → archive** (WQ-122) |
| `README.md` | 8,435 | 6/30 (3 commits ever) | nobody (public-facing) | none as ROOT README | **REFRESH** (WQ-124) |
| `LESSONS.md` | 5,928 | 6/30 | nobody (every `LESSONS.md` boot-read in the fleet is an AGENT-LOCAL file) | USER.md grant line · KERNELS.md · one FORGE/STATUS.md D-17 evidence cite | **RETIRE → archive**, 8 unique items folded to owners (WQ-122) |
| `USER.md` | 5,791 | 8/29 | PROME every boot | 19 | KEEP — live governing home (decision-block format); no change |
| `.gitignore` | 2,890 | 8/26 | — | — | KEEP |

## 2. Findings

### F1 — `LESSONS.md` (root) is a pre-canon duplicate nobody reads
- **Zero** live root-specific citations. Every agent `CLAUDE.md` that says "Read `LESSONS.md`" (CORAL, LABOR, OSPREY, REGINALD, WATT, OTTO) means `AGENTS/<NAME>/LESSONS.md`. The census that first showed "272 citing files" was name-collision noise.
- Of its 27 items, **19 restate root `CLAUDE.md` Critical Rules or TERRY Non-Negotiables verbatim-in-substance** (read-before-edit, mechanical-before-creative, deploy-then-wait, puts-on-green, roll-don't-trim, close-the-loop, scoped git, pull at boot, hallucination/live prices) — the same rules-with-provenance mix WQ-120 just split out of root.
- **8 items exist NOWHERE else in live canon** (grep across TERRY `RISK_RULES.md`, `docs/CANON_PROVENANCE.md`, `COMPLETION_SPEC.md`, `AUTONOMY.md`, `ORCHESTRATION_PLAYBOOK.md`, `PREDICTION_DISCIPLINE.md` — all empty): ① CVNA — don't hedge Will out of conviction unless the THESIS is broken · ② two expiry frameworks (PC single-name dateable catalyst vs macro/index Hamilton-clock Dec) · ③ one-spawn-one-objective (REGINALD P-002) · ④ steelman-with-a-probability + honesty ≠ position management · ⑤ earnings dates from IR/8-K (OZK wrong twice) · ⑥ dry-run prompts before batch deployment · ⑦ inject confirmed data into later batches · ⑧ flag LLM-inaccessible data for Will. (Deploy-on-trigger and scrub-by-content already live at TERRY / auto-memory.)
- Fold homes: ①②⑤ → `AGENTS/TERRY/RISK_RULES.md` (trade-construction canon; TERRY-owned → packet, not PROME edit) · ③⑥⑦ → `PROME/ORCHESTRATION_PLAYBOOK.md` (PROME-owned) · ④ → `FORGE/PREDICTION_DISCIPLINE.md` (PROME-owned) · ⑧ → `USER.md` Communication (PROME-owned, pre-granted).

### F2 — `KERNELS.md` is a frozen June thesis-spine with stale claims and dead pointers
- 2 commits in its life, both 6/30 (the rename from root `MEMORY.md`). No boot protocol reads it; SYSTEM.md lists it as "on-demand reference" and nothing has demanded it.
- **Stale against current canon:** "CCC/HY ratio downgraded" (CCC/HY is at its 3-yr record and REGINALD-owned as VX-REG-18.04) · "Timing thesis codified → `FORGE/timing/`" (FROZEN 8/09, cite-as-history) · "Persistent agents — do not spawn" (spawn is TIERED, Will-ruled 8/22; the old claim is the exact kill-on-sight line in SCRATCH caution 5) · "single desktop" (serial multi-machine) · FSK Q1 / "Blue Owl 2026 SIV analog set" = May-vintage discoveries with no refresh trigger.
- **2 dead pointers:** `AGENTS/BROCK/trade/ARES/sources/IHAM_FINANCIALS_FY2025.md` · `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`.
- Nothing in it is load-bearing for a live gate, DOCKET row or position. The durable-thesis content it once held is now owned per-domain (agent `thesis/` + `PREDICTIONS.tsv` + NEXUS_BRIEF).

### F3 — `AGENTS.md` carries a live kill-on-sight contradiction + ~1.6 KB of root/AUTONOMY duplicates
- **BLOCKING-class:** table row FERT (line 61) still reads *"potash EXCLUDED-UNOWNED"* while the chain-10 paragraph above it (8/21 root-batch word) says *"potash is UNOWNED" is kill-on-sight fleet-wide*. Codex's 8/24 evaluation named this exact pair (its line 26); it is still live 5 days later — the annotated-correction-leaves-the-mirror class.
- Sections `## First Message` (273 B — PROME's boot pointer living in a fleet file) · `## Safety` (903 B — restates root Critical Rules 5/11 + AUTONOMY) · `## Core Principles` (411 B — generic) = duplicates of auto-injected root canon. `AGENTS.md` is on-demand for routing; every reader already has root.
- Table caption carries ~700 B of count-correction provenance ("count corrected 8/6 … 31→32 … 32→33 … 33→34") — the WQ-120 class: provenance in a live cell. Home = `docs/CANON_PROVENANCE.md` (add an `agents-anchor:` key, same pattern as `root-anchor:`) or git log.
- The chain paragraph in root `CLAUDE.md` (Transmission chain) and the numbered chains here are **two homes** for one topology. Root line 24 names `AGENTS.md` as the routing owner → keep the numbered list HERE; root keeps its one-paragraph compression (a view, not a second canon — no root edit proposed today).
- Target: 10,198 → ~7,000 B; every routing row unchanged except the FERT fix.

### F4 — `README.md` (public proof-of-work) is 60 days behind the operation it describes
| Claim | Now | Source |
|---|---|---|
| "21-agent" / "21 active" ×4 | **33 ACTIVE** (5 classes) | `PROME/ROSTER.md` line 37 |
| "~3,400+ commits over five months" | **10,219 commits, seven months** | `git rev-list --count HEAD` 8/29 |
| "isn't multi-machine yet … one desktop" | **serial multi-machine, desktop ⇄ laptop** since 8/3 | root CLAUDE.md line 11, `PROME/MACHINE_LOCAL.md` |
| "domain agents run on cheaper Sonnet … synthesis on Opus" | **0 of 33 agent CLAUDE.md files mention Sonnet**; the fleet runs Fable 5 / Opus | grep |
| "`FORGE/STATUS.md` is currently stale" | vintage lives in its own header — a dated adjective in a public doc is the PAT-068 class | root Key Directories |
| "15 domain owners / 6 orchestration" split | ROSTER's five-class split (17 DOMAIN ACTIVE etc.) | ROSTER §ACTIVE |
- Nothing in it is wrong about the METHOD; the numbers are. Because this is Will's outward-facing exhibit, PROME drafts and Will reads the draft before commit (it is not in the pre-granted set).

### F5 — root directories (census only; no decisions asked today)
| Dir | Tracked files | Last commit | Note |
|---|---|---|---|
| `exports/` | 2 | 6/21 | a Claude-Code commands reference (.md + .docx), **zero citations** → `archive/` candidate |
| `reviews/` | 1 | 8/07 | the 8/6 Opus-5-window commit review; cited by 3 processed packets → `AUDITS/` is the natural home (same class) |
| `SIGNALS/` | 7 | 8/11 | already FROZEN-bannered (SENTRY retired); `scripts/fetch_feeds.py` + `.github/workflows/feeds.yml` still point at it — check the workflow is disabled before any move |
| `AUDITS/` | 8 | 8/25 | live (Codex 8/24 evaluation) — keep |
| `WILL/` | 0 (gitignored private drop) | — | keep; boot-surfaced per canon |
| `archive/` | 69 | 7/06 | root-level archive; PROME/archive is separate — fine |
| `BOARD/` 850 · `FORUM/` 142 · `KERNEL/` 116 · `MESSAGING/` 23 · `docs/` 2 · `scripts/` 27 | | | live, owned, out of scope |

## 3. Recommendation (ranked)
1. **WQ-123 AGENTS.md** — fix the FERT potash cell TODAY (kill-on-sight text in a canonical routing file), drop the three duplicate sections, move the count-provenance to `docs/CANON_PROVENANCE.md`. Will-gated (`AGENTS.md` core).
2. **WQ-122 retire LESSONS.md + KERNELS.md** → `archive/ROOT_LESSONS_FROZEN_2026-08-29.md` / `archive/ROOT_KERNELS_FROZEN_2026-08-29.md` (verbatim, crc32 in header, FROZEN banner) after the 8 unique LESSONS items are folded to their owners (TERRY items by packet). Remove the two SYSTEM.md rows and the USER.md grant-line mention. Pre-granted edit scope, but retirement is bigger than an edit — asked by number anyway.
3. **WQ-124 README refresh** — PROME drafts the six corrections above as a diff; Will reads; commit on his word.
4. `exports/` → archive, `reviews/` → AUDITS/: PROME-lane hygiene, will do at closeout unless Will objects.

**Cost:** $0 · zero thresholds · ~24 KB of root surface retired/condensed · no boot-path change (none of the three is boot-read).
