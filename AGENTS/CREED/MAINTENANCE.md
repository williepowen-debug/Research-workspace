# CREED Maintenance Log

Reverse-chronological log of **structural** changes to CREED's docs, folders, schema, and boot/closeout protocol. Answers *"why is CREED organized this way, and what decision am I about to re-litigate?"*

**Distinct from:**
- `STATUS.md` — live analytical dashboard (canonical truth).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every closeout; structural notes there do NOT persist — they persist **here**).
- `thesis/CHANGELOG.md` — **analytical** thesis pivots (scores, signals, base case). Structural ≠ analytical: the *decision to split S8* is analytical and lives in CHANGELOG; *creating a workbook to hold the split* is structural and lives here.

> **⚠️ This is a consult-on-structural-work doc, NOT a per-session ritual.** *(Framing adopted verbatim-in-spirit from BROCK, which warns of exactly this bloat and cites SAM at 636 lines as the cautionary tale.)* **Do not wire it into every closeout** — CREED is **Tier-2 spawn-on-need** and process weight is the specific thing that makes a spawn-on-need agent expensive to wake. Touch it only when a session changes CREED's *structure*: a doc/folder created/retired/moved, a schema or protocol amendment, an ownership boundary shift. **Cap: archive to `archive/` if this grows past ~300 lines.**

---

## 2026-07-27 (second sitting) — Fleet-parity surfaces adopted after a crash exposed the gaps

**Trigger:** Will directed a survey of SHADE's and BROCK's live file structures for anything CREED should integrate. The survey ran immediately after an unclean shutdown in which **CREED had no surface describing what it was mid-way through** — so the gaps were not theoretical, they had just cost something.

**What changed — four surfaces created, and the reasoning for each is a demonstrated CREED failure, not fleet conformity:**

| New file | The failure it answers |
|---|---|
| **`board_log.tsv`** | CREED had consumed **~30 mail items** across four sessions with dispositions recorded **only as prose inside STATUS catch-up sections** — unqueryable, and scrolling off as STATUS grows. Both SHADE (45 rows) and BROCK (68 rows) run this. **Backfilled honestly:** the 12 items from 7/11 forward are logged per-signal; the 17 older WALTER SIGs are marked **PRE-LEDGER provenance and deliberately NOT retrofitted** — reconstructing a disposition I never recorded would manufacture false precision. |
| **`SCRATCH.md`** | The crash. Recovery worked only because modified files happened to be legible on disk. **The file that should have carried the handoff — `LAST_COMPLETION.md` — had skipped two closeouts (7/20, 7/27)** and was still 7/4 vintage, asserting *"CREED has NO own workbook"* four hours after the workbook was built. |
| **`workbook/PREDICTIONS_SCOREBOARD.md`** | CREED registered **10 predictions with self-set confidences on 7/27 and had no calibration surface at all.** BROCK's scoreboard (n=10, Brier 0.216) produced a read that **changed its behaviour** — *"structural calls are under-priced, lean in"* — which is the entire point of keeping score. Created at n=0 deliberately: the discipline has to exist **before** the first resolution, or the first resolution sets the precedent for skipping it. |
| **`MAINTENANCE.md`** | This file. CREED made **three structural changes on 7/27** (workbook built, S8 split 8a/8b, S5 ownership moved to HOMER) with the rationale buried inside a dated catch-up section that will scroll off. |

**Deliberately NOT adopted, and why — the survey's more useful half:**
- **BROCK's `trade/` tree** (per-ticker dirs) — CREED's mandate **explicitly excludes trade construction**. TERRY owns it. Copying this would create a surface CREED is not allowed to fill.
- **BROCK's `docket/CATALYSTS.tsv`** — CREED's catalyst set is **six recurring prints on a known cadence** (Trepp monthly ×2, FDIC quarterly, MBA quarterly, plus named earnings). A separate docket file for six rows is overhead; they live in `SCRATCH.md` §OPEN THREADS with their resolving predictions. **Revisit if the catalyst count passes ~15 or acquires irregular one-off dates.**
- **`NEXUS_BRIEF.md`** — BROCK maintains one because it feeds NEXUS. CREED is not on that route (`CLAUDE.md` §Cross-Agent Route Matrix). Building an unread brief is pure cost.
- **SHADE's `domain/sources/` tree** — CREED's `research/` holds 5 files, all dated by filename. A second tree for 5 files fragments retrieval. **The one piece worth stealing is the convention, not the folder:** SHADE puts a `LAST_REVIEWED:` header + an explicit >60d stale banner on each source doc. Adopt that on `research/*.md` at next refresh.
- **A per-session `MAINTENANCE` write** — BROCK's own warning. Not wired into closeout.

**Files touched:** `board_log.tsv` (new), `SCRATCH.md` (new), `MAINTENANCE.md` (new), `workbook/PREDICTIONS_SCOREBOARD.md` (new), `CLAUDE.md` (boot order + closeout protocol), `STATUS.md`, `archive/STATUS_CATCHUPS_2026-06-28_to_2026-07-04.md` (split out).

**STATUS split — the fifth finding, and the one with a number attached.** CREED's `STATUS.md` had reached **376 lines**, the longest of the three agents surveyed (SHADE 342, BROCK 258) — and it grows by **a full catch-up section per spawn**, with no cap and no archive rule. **BROCK runs a 250-line cap with a mandatory split trigger at 280.** The 6/28 and 7/4 catch-up sections were `git mv`'d to `archive/STATUS_CATCHUPS_2026-06-28_to_2026-07-04.md` — both are fully superseded and independently preserved in `thesis/CHANGELOG.md` and their dated `research/REFRESH_*.md` packs, so **nothing is lost and nothing is deleted.** A soft cap is now written into `CLAUDE.md` §Closeout.

**Boot-impact:** boot order gains `SCRATCH.md` (first, for handoff state) and keeps `STATUS.md` as canonical truth. Closeout gains a `board_log.tsv` row-per-item requirement and the STATUS soft cap. **Net: two cheap steps added, one rot pattern closed.**

**Lessons:**
1. **A file whose *name* promises currency fails differently from an ordinary stale file.** `LAST_COMPLETION.md` skipping a write didn't read as old — it read as **current and wrong**, which is how a 7/4 claim survived two sessions and reached Will. Ordinary rot invites suspicion; this suppresses it.
2. **Fleet parity is not the argument.** Every surface above is justified by a CREED failure with a date on it. The four *rejected* surfaces are the evidence the filter ran — **for a Tier-2 spawn-on-need agent, an unread file is not neutral, it is a recurring boot cost.**
3. **Backfill only what you actually recorded.** The honest `[PRE-LEDGER-BACKFILL]` provenance row is worth more than 17 plausible reconstructed dispositions.
