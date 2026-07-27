# CREED Maintenance Log

Reverse-chronological log of **structural** changes to CREED's docs, folders, schema, and boot/closeout protocol. Answers *"why is CREED organized this way, and what decision am I about to re-litigate?"*

**Distinct from:**
- `STATUS.md` — live analytical dashboard (canonical truth).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every closeout; structural notes there do NOT persist — they persist **here**).
- `thesis/CHANGELOG.md` — **analytical** thesis pivots (scores, signals, base case). Structural ≠ analytical: the *decision to split S8* is analytical and lives in CHANGELOG; *creating a workbook to hold the split* is structural and lives here.

> **⚠️ This is a consult-on-structural-work doc, NOT a per-session ritual.** *(Framing adopted verbatim-in-spirit from BROCK, which warns of exactly this bloat and cites SAM at 636 lines as the cautionary tale.)* **Do not wire it into every closeout** — CREED is **Tier-2 spawn-on-need** and process weight is the specific thing that makes a spawn-on-need agent expensive to wake. Touch it only when a session changes CREED's *structure*: a doc/folder created/retired/moved, a schema or protocol amendment, an ownership boundary shift. **Cap: archive to `archive/` if this grows past ~300 lines.**

---

## 2026-07-27 (third sitting) — REGINALD/HOMER survey: 2 surfaces adopted, and the survey found two cross-agent defects worth more than the files

**Trigger:** Will directed the same structure survey against **REGINALD** (the fleet's most mature agent — per-entity trees for CFG/EGBN/FITB/MTB/PNC/RF/ZION, 11 scripts, 19 workbook files) and **HOMER** (the newest, DAEDALUS-built 7/12). Both clean/not-live at survey time.

**Adopted (2):**

| New file | Why |
|---|---|
| **`registry/THRESHOLDS.tsv`** | From `REGINALD/registry/THRESHOLDS.tsv`. 11 rows transcribing CREED's **existing FROZEN bands** with trigger IDs, sustain windows, recipient chains and source-of-truth refs. **It moves nothing** — bands stay Will-gated. **It found a live cross-agent collision within minutes of existing**, which is the whole argument for it. |
| **`scripts/boot.py`** | From REGINALD's boot orchestrator, **scoped down hard**. Checks mechanics only: workbook staleness, prediction resolve-dates, the **closeout-skip detector** (STATUS vs LAST_COMPLETION mtime — the 7/27 failure, now mechanized), mail lanes, STATUS line cap, git dirt. **Deliberately pulls NO market data** — prices must be live at the moment of use (root rule 4); baking a price into a boot script invites citing a cached level. **Caught an unprocessed inbox item on its first run.** |

**Declined (3), with reasons that are about CREED specifically:**
- **HOMER's `state_vectors/`** — a genuinely excellent pattern (stable citable IDs; a `corrected/` lane preserving superseded versions **unedited** under a banner naming the superseder). **Declined as a tree** because CREED's corrections are already annotated-in-place with git holding the prior text, and a second artifact class for ~4 corrections/session is overhead. **Credited to HOMER and named as the pattern to move toward** if CREED's correction volume rises.
- **HOMER's `docket/CATALYSTS.tsv`** — declined again (as with BROCK's), but the reasoning improved: the value isn't the row count, it's the `what_to_check` + `threshold_signal` columns. **CREED already carries that information per-prediction in `PREDICTIONS.tsv` (`Resolves_On`) and in `SCRATCH.md` §OPEN THREADS.** A third copy would be a drift surface.
- **REGINALD's per-entity trees / `CONVERGENCE_RESCALE.md`** — the entity trees serve a 7-bank coverage universe CREED doesn't have. `CONVERGENCE_RESCALE.md` is itself **FROZEN/superseded** in REGINALD. *(But its concept is pointed: a scoring-scale change written as a reviewed PROPOSAL doc before being pasted into STATUS. CREED changed its own denominator 40→45 inline on 7/27. Worth remembering if CREED rescales again.)*

**⭐ The survey's real output was two cross-agent defects, both routed:**

1. **`REG-T-07` fires on CREED's series, and CREED isn't on its chain.** REGINALD's registry has `OFFICE-CMBS-DQ > 15, sustain 3 → CRE-ACCELERATE`, chain *"REGINALD action / BROCK SHADE info."* CREED's `CREED-T-01a` is the **same series at > 12, sustain 2**. Divergent levels may be deliberate (transmission gate vs recognition gate) — **nobody recorded that they were compared.** Worse: REGINALD's dashboard row *labelled* "Office CMBS DQ" carries **Fitch overall 3.31%**, while CREED's canon is **Trepp office 11.57%**. **Distance-to-fire is 11.7pp or 3.4pp depending which series the trigger is read against.** Not a wrong threshold — **a wrong denominator under the right label.**

2. **⚠️ A citation loop CREED closed itself, the same day it created it.** CREED's 7/27 S5 demotion wrote *"cite `AGENTS/HOMER/STATUS.md` for the MF figure."* **HOMER's STATUS attributes that figure to "(CREED 7/4 pull)"** — in both its dashboard row and its marquee section. **CREED cites HOMER → HOMER cites CREED.** Anyone reading S5 as HOMER-corroborated is reading CREED corroborating CREED. **Fixed in `CLAUDE.md` by separating what the DAEDALUS ruling did not: HOMER owns the SCORING; ownership of the DATA PULL is a distinct assignment that must be stated.** Otherwise the literal rule ("don't publish a second Trepp-MF citation") reads as *CREED stops pulling* — and a handoff ends with neither party pulling. Routed to HOMER with an (a)/(b) choice.

**Files touched:** `registry/THRESHOLDS.tsv` (new), `scripts/boot.py` (new), `CLAUDE.md` (S5 sourcing caveat + route-matrix row), `MAINTENANCE.md`, `board_log.tsv`, `SCRATCH.md`, `workbook/PREDICTIONS.tsv` + `PREDICTIONS_SCOREBOARD.md` (the `PRED-006` re-spec, below), 3 outbound packets (SHADE, HOMER, REGINALD).

**Lessons:**
1. **A structure survey's best output may not be a file.** Two of the three most valuable findings were *interface* defects between agents, visible only because the survey read both sides. Copying `THRESHOLDS.tsv` mattered mainly because **having the registry made the collision expressible.**
2. **Check the other side's sourcing before writing a citation rule.** CREED moved S5 ownership to HOMER without reading where HOMER's number came from — and it came from CREED. **Ownership rulings assign judgment; they do not automatically transfer the data pull.**
3. **Declining is a real output.** Three of five surveyed surfaces were declined, each for a CREED-specific reason. For a Tier-2 spawn-on-need agent an unread file is a recurring boot cost, not a neutral.

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
