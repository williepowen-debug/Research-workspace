# L603 — WALTER's system-improvement bookmark candidates · DAEDALUS disposition

**Author:** DAEDALUS · **Written:** 2026-10-20 09:2x ET (hook clock 09:19 during drafting) · **Row:** `PROME/DOCKET.tsv` L603 (dated 10/19, re-dated from 10/12) · **Inputs:** `AGENTS/WALTER/research/2026-10-03_system-improvement-bookmarks.md` (50f81979c) · PROME's primary-source read `PROME/reports/2026-10-03_system-improvement-candidates-primary-source-read.md` (with CATO's review folded in) · `PROME/WILL_QUEUE.md` rows 377/379/380 · `measure.py` on five auto-loaded files, 10/20. **Nothing adopted or installed here; no charter, setting or tool changed.**

⚠️ **Caveat that travels (WALTER's own):** except for PROME's four primary reads, candidates were read off the posts, not the underlying talks or repos. A "defer" below is not a verdict on the artifact.

## The pain point the Tier-1 list was keyed to has moved

WALTER's 10/3 premise was "~107 KB auto-loaded every boot." Measured today (`PROME/tools/measure.py`, 10/20 09:1x ET):

| File | 10/3 (PROME report) | 10/20 |
|---|---|---|
| root `CLAUDE.md` | 24,199 B | 22,499 B |
| `PROME/CLAUDE.md` | 34,340 B | 23,874 B |
| `AGENTS/WALTER/CLAUDE.md` | 65,767 B | 22,760 B |
| `memory/auto/MEMORY.md` | 17,937 B | 17,821 B |
| `USER.md` | 4,626 B | 7,026 B |

A WALTER boot's standing load fell from ≈108 KB to ≈63 KB (root + WALTER + MEMORY), and PROME's from ≈76 KB to ≈64 KB. The charter-diet candidates (#162, #96, #151, #179) are therefore pressure on a direction already being worked (WQ-379, L580, WQ-299 R3's under-20,000 B charter target), not an unaddressed gap.

## Dispositions — Tier 1

| # | Candidate | Disposition | Reason / what would change it |
|---|---|---|---|
| #162 | Cherny token-waste clip | **DECLINE as a row** — already absorbed | PROME's primary read: the percentages are the poster's; Cherny's advice ("short; delete and restart; add only when the model goes wrong") is already our design and is carried into the BOOT.md canon-pass proposal (spine audit #16). No new DAEDALUS work. |
| #96 | Prompt caching, static-at-top | **DEFER** — no row | Caching is a harness/API property the fleet does not control in Claude Code sessions; the transferable part (stable text first, volatile state last) is already the hot/cold split DAEDALUS uses (PATTERNS_HOT, FLEET_DIRECTORY). Re-open only if a desk measures per-turn cost and shows charter order matters. |
| #151 | 65-line CLAUDE.md, mistake-rate claim | **DECLINE** | Unverified headline (the poster flags his own headline-vs-body gap); our measure of instruction quality is reader ❌ counts, not line count. |
| #220 | MarkItDown | **DEFER to WALTER** (owner) — no DAEDALUS row | PROME's trial: gains label–value pairing on Trepp tables, fragments two-column prose; a targeted `pdfplumber.extract_tables()` route is the sharper candidate. WALTER's lane, Will's word if it touches the production tool. CATO concurred. |
| #169 | `.env` deny line | **CLOSED — Will ruled** | WQ-380 RULED DECLINE 2026-10-04 16:18 ET ("just leave it as it is"). Not re-argued here. |
| #195 | 421-page "Agentic Design Patterns" | **DEFER** — reference only | A curriculum, not a change. DAEDALUS reads a named chapter only when a live design question needs it (e.g. guardrails for L495's canaries). No dated row: a "read 421 pages" row would be paperwork with no decision attached. |
| #159 | JPM "Ask David" architecture | **DECLINE as a row** — validation, not news | Same shape as ours (supervisor → specialists → judge → human). PROME's #215 read reached the same conclusion for a sibling article. Nothing to adopt without the write-up's primary, which nobody has read. |
| #206 | Anthropic skills taxonomy (9 categories) | **DEFER** | Would matter only if the fleet's skill set grows past PROME's five (boot · closeout · reconcile · coldread · spineaudit); today a taxonomy organises nothing. Re-open at a skills restructure. |

## Tier 2 — grouped

| Group | Items | Disposition |
|---|---|---|
| Output / prompting discipline | #152 (positive instructions, define length, name outputs), #126 (define big words) | **DECLINE as rows** — both already canon (`BLUEPRINTS/STRICT_TEXT.md`; root Operator-surface clause "jargon unpacked or dropped on first use"). #152's "positive over negative" is a candidate test for the next STRICT_TEXT sitting, noted here only. |
| Plan hardening | #231 (one-line accretive prompt), #216 (`/review-plan`) | **HELD** per CATO/PROME 10/3: routine use waits on one instance of the prompt changing a Will ruling. DAEDALUS adds nothing. |
| Memory / graph / worktrees | #91, #214, #203/#210/#140, #179 | **DECLINE** — we run a version of each (file memory, auto-memory index, worktree isolation exists in the harness). No defect named that they fix. |
| Chief-of-staff | #215 | **CLOSED** — PROME read it; the four-label trial (dispatch · prep · yours · skip) is PROME's presentation experiment. |
| Observability / MCP / search / courses | #156, #171, #189, #245/#246 | **DEFER** — #156's observability theme overlaps L495/L496 (today's canary + unattended register), which is the fleet's own version; nothing to import. |
| X-ingestion compare | #242 | **DEFER to WALTER** — compare only if WALTER's bookmark intake shows a defect (WQ-377 stopped the backlog). |
| Tier 3 hype + stale financial | named in WALTER's file | **DECLINE** (WALTER's own disposition). |

## Result

**0 adoptions · 0 new dated rows from this list.** 4 closed/declined as already absorbed or ruled (#162, #169, #151, #159), 4 deferred with a named re-open trigger (#96, #195, #206, Tier-2 observability), 2 deferred to WALTER as owner (#220, #242). L603 can be marked **DONE** — the row asked for a per-candidate disposition, and this file is it.
