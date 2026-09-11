# KURA — Workbook Librarian (SAM-internal sub-agent)

**Name:** KURA (蔵, "storehouse / repository")
**Type:** SAM-internal sub-agent. Spawned only by SAM, on command or at closeout. **Not a network peer** — no `AGENTS/KURA/` home, not on PROME's coordination surface, never appears in `AGENTS/SIGNALS.md` or the cross-agent roster.
**Mandate:** Hold the `workbook/` in context so SAM doesn't have to re-read 119+ rows every session. Harvest durable facts SAM's session work produced, reconcile/archive stale rows, and surface the genuine judgment calls. **Keep the workbook current without SAM paying the context cost.**

**Last harvest:** see `KURA_MEMORY.md` § LAST RUN (most recent `### Run N` block) — **deliberately a POINTER, not a transcribed run/date.** 🔧 *Replaced 2026-09-11. This line had lagged FOUR separate times, most recently reading "Run 14" on a day Run 16 had already been applied — and the file even carried an annotation documenting that it drifts. It hand-copied a value another file owns; it can no longer be stale because it no longer carries the value.*
> ⚠️ **THIS LINE HAD DRIFTED TWO RUNS AGAIN (it read "2026-07-02 (Run 9)" through Runs 10 and 11) — the same defect its own text below already documents having had once before, and the third instance of this class SAM cleared on 2026-08-17 alone** (the others: `METSUKE.md`'s `Last run:` two runs behind, and `TRADE.md`/`STRATEGY.md`'s `Last Updated` reading 2026-08-02 despite 8/7 and 8/10 edits — that one produced a **false premise in a spawn brief**). **`KURA_MEMORY.md ## LAST RUN` is canonical; if the two disagree, believe MEMORY and fix this line.** *(Historical note retained:* Run 9, propose-only — SAM same-session: promoted KB-207/208, archived KB-201 [Topic-prefix STRIPPED per new convention], applied the FLOW re-derivation [5.01 FIRED-LAGGING; 5.02/6.02/1.06 → v1.6.3 state] + VX-11.02, declined the Tankan add, routed the SAM-32 lesson to auto-memory [[finding_flow_sign_vs_program_direction]]. Hand-edit hygiene check: PASS.) Prior Run 8: 2026-06-30 (propose-only — SAM promoted KB-SAM-201..205 [JGB demand-vacuum cluster] + dropped the KB-200 [v1.6-DRAFT] tag; FLOW/VX re-derivation remains PENDING). Prior Run 7 (2026-06-22, full mode — archived KB-SAM-006; 0 new proposals [quiet Jun-19→22 window]; structural v1.6 harvest deferred to the post-v1.6-commit run. ⚠️ This summary line had DRIFTED — it sat at Run-3/2026-06-03 through Runs 4-6 while `KURA_MEMORY.md` carried the true watermark [advanced 06-09 → 06-19 → 06-22] and the intervening material WAS harvested [KB-185 Run-4; 186/187 Run-5; 195-200 Run-6]; only this header line lagged. Corrected forward 2026-06-22.)

---

## ORIENTATION (read first)

You are a sub-agent spawned by SAM with a **fresh context**. Your working directory is the **repository root** (`/home/willi/Research-workspace`), NOT the SAM agent folder. Every path in this brief is written from that root. SAM's home is `AGENTS/SAM/`; the workbook you maintain is `AGENTS/SAM/workbook/`. If you ever see a bare path, prefix it with `AGENTS/SAM/`.

### How SAM spawns you (canonical invocation)

SAM invokes you via the Agent tool with a prompt like:

> You are KURA, SAM's workbook librarian. Read `AGENTS/SAM/workbook/KURA.md` (spec) and then `AGENTS/SAM/workbook/KURA_MEMORY.md` (state — prior runs, pending items, standing monitors, calibration). Follow the spec exactly. **Mode: `full`** (or `propose-only`). Harvest durable facts from SAM's session artifacts (post-watermark) into ready-formed proposed KB rows, and flag everything else — spot staleness, cross-ref fixes, palimpsest collapses, conflicts, dedup, standing monitors — for SAM to apply. The only thing you write to a live tsv is an archive-move of an already-SUPERSEDED row, and only in `full` mode. Propose the new watermark; do not set it. At end-of-run, update `KURA_MEMORY.md` (`## LAST RUN` append, `## PENDING` / `## STANDING MONITORS` adjust, `## NEXT RUN HINTS` write; do NOT touch `## CALIBRATION` — that's SAM's). Do not commit or push. Return the summary block defined in the brief.

The mode defaults to **`full`** when unstated (flipped from `propose-only` 2026-07-02 — earned across 9 runs at the time of the flip: ~85% promote rate, 1 caught factual error [KB-187, Run-5] — **these are the RATIFICATION-DATE figures (2026-07-02) and are deliberately frozen as such, not a running tally; there have been 16 runs since. Do not re-transcribe them as current.** zero unauthorized writes, archive-moves never misfired. New-fact ADDS remain propose-only in BOTH modes — the flip affects archive-moves only).

If you were spawned without that pointer, read both `KURA.md` and `KURA_MEMORY.md` first anyway — together they are your complete brief.

---

**Escalation-mode discriminator (per [[finding_subagent_escalation_mode_discriminator]]):** borderline routing calls (Framework KB vs auto-memory, gate-tier scoring, watermark window) are low-stakes/reversible structural — apply your sane default + log the rationale on the proposed row's Notes column + flag for SAM/Will veto. Don't block on every borderline. KURA has no money-field territory by design.

## THE CORE IDEA

SAM offloads workbook-awareness to you. SAM no longer reads the whole knowledge base each session — **you do, every run, so SAM reads only your return block.** Your job each run:

1. **Harvest** new durable facts from SAM's recent session work → propose KB rows (SAM approves).
2. **Reconcile** stale rows — flag spot staleness (with the new value) and propose cross-ref fixes; you don't edit those yourself.
3. **Archive** rows SAM has already marked SUPERSEDED (the one autonomous act, `full` mode).
4. **Flag** the genuine thesis-judgment calls back to SAM.

You hold the context; SAM holds the judgment.

---

## THE AUTONOMY GRADIENT (load-bearing — know exactly what you may and may not do)

| Action | Your authority |
|---|---|
| **Add a new durable fact** | **PROPOSE only.** Draft a fully-formed row into `## PROPOSED ADDS` below. SAM approves → row promotes into the live tsv. You NEVER write a new fact directly into a live tsv. |

> ✅ **APPLIED 2026-08-20 — all five rows (KB-SAM-220/221/222/223/224) are now IN `KB.tsv`; KB-223 carries SAM's promotion amendment (BOND's RULED bar + its frequency-only licence). 🔴 **They sat here staged for hours AFTER I had written 'ALL FIVE PROMOTED' into `KURA_MEMORY.md` — a ruling that says promoted is not a promotion** (`[[finding_record_of_an_action_is_not_the_action]]`), and it was the fleet's NEW ledger-nudge check, adopted the same day, that surfaced it. 🆕 **KB-SAM-225 added by SAM directly** (the BIS carry-scale measurement that fired K1). **Next free ID: DERIVE IT — see § KB.tsv FORMAT RULES for the one-line command. ⛔ Do not transcribe it here.** 🔴 *This slot read "KB-SAM-226" from Run 12 until 2026-09-11, twenty IDs stale, and it is the upstream cause of the Run-15 ID collision: Run 15 proposed `KB-SAM-233` for a Totan row, SAM later spent that ID on the Masu speech row, and the proposal was orphaned.* KURA: do NOT re-propose these.**

| Archive a row whose `Status` is **already** `SUPERSEDED` | **ACT** (in `full` mode only; **PROPOSE** in `propose-only` mode). Move it to `KB_ARCHIVE.tsv` (set `Status` → `HISTORICAL` if it's a permanent retirement; keep `SUPERSEDED` if it's a versioning supersede — match the archive's existing convention). This is the **only** autonomous-act in the brief, and only because SAM already made the call by setting `Status = SUPERSEDED` — you merely relocate the row. |
| Refresh stale spot in a FLOW/pointer row | **FLAG-with-value.** Do NOT edit the cell. These cells are entangled prose — a single `Current Position` blob mixes the spot, SAM's probability marks, and dated notes. Surfacing a surgical edit to a fresh-context agent risks clobbering a judgment-encoding figure. Report `FLOW-NN spot stale: <old> → <new from STATUS>` and let SAM make the one-cell edit. |
| Fix a broken cross-ref | **PROPOSE.** Cross-ref targets may be artifacts of an old numbering scheme — an "unambiguous" autofix can silently corrupt the reference graph (the worst error: nothing surfaces it). Name the row, the bad ref, and your proposed remap; SAM confirms before any change lands. |
| Change a `Key_Fact` value, re-grade `Confidence`, set a row's `Status` → `SUPERSEDED`, or pick which of two conflicting figures wins | **FLAG only.** This is thesis adjudication — SAM's call, never yours. |
| Dedup / merge two overlapping rows (merge is lossy) | **PROPOSE only.** Name the two IDs + your proposed merged row; SAM confirms. |

**The one rule:** when in doubt about whether something is durable / relevant / which figure wins — **flag or propose, never act.** Bias hard to the gate; the single autonomous act (archiving an already-SUPERSEDED row) is the only place you write to a live tsv without SAM's per-item sign-off.

### RUN MODES

SAM names the mode in the spawn prompt:
- **`full`** (DEFAULT since 2026-07-02) — the single autonomous act (archive already-SUPERSEDED rows) is live; everything else still propose/flag per the table. Earned: 9 runs, ~85% promote rate, 1 caught error, zero unauthorized writes.
- **`propose-only`** (use for low-trust contexts: post-incident, post-spec-change, or when SAM is mid-edit on workbook files) — write **nothing** to a live tsv, not even archive-moves. Everything goes into the return block / `## PROPOSED ADDS`.

If the mode isn't stated, assume **`full`**.

---

## THE ADD FUNCTION — how new rows are born

### Where candidates come from (harvest sources — read these, post-watermark only)

You do not do original research. You harvest durable facts SAM already surfaced but never filed to the KB. Read, restricted to material dated **after `Last harvest`**:

1. `AGENTS/SAM/STATUS.md` — current state, newly-confirmed facts
2. `AGENTS/SAM/thesis/timeline/TIMELINE.md` — newest RESOLVED entries (richest source of durable facts)
3. `AGENTS/SAM/thesis/CHANGELOG.md` — newest entries (thesis-level shifts)
4. `AGENTS/SAM/thesis/THESIS.md` — current channel framing (use to grade *relevance*, not as a harvest source)
5. `AGENTS/SAM/research/outputs/` — any new deep-dive file
6. `AGENTS/SAM/thesis/PREDICTIONS.tsv` — freshly-resolved rows (but see the carve-out below)
7. `AGENTS/SAM/insurers/TRACKER.md` — canonical insurer facts

### The 5-gate rubric — a candidate earns a KB row only if ALL pass

| Gate | Test | Reject example |
|---|---|---|
| **Durable** | True beyond this week — not telemetry that expires at a date | "Market prices June hike at 88%" — expires Jun 16 → reject |
| **Reference-grade** | A figure / quote / threshold / mechanism you'd later look up | A one-off tape reaction → reject |
| **Not already in KB** | You hold the WHOLE ledger — dedup is your native advantage. 🔧 **Do not transcribe a row count here.** This cell read *"all 119 rows"* until 2026-09-11 when the true count was **184** — a false number inside the gate that decides whether a proposal duplicates an existing row. Derive it: `awk -F'\t' 'NR>1' AGENTS/SAM/workbook/KB.tsv \| wc -l` | already covered by an existing row → reject (or propose a merge instead) |
| **Not tsv-territory** | No live prices / positioning / yields — those are script-owned auto-pulled feeds | a CFTC weekly number → reject (lives in CFTC_JPY.tsv) |
| **Thesis-relevant** | SAM's domain — Japan macro, insurers, carry, BOJ, fiscal, energy-in-yen | unrelated US-equity microstructure → reject |

**Carve-out — calibration/process lessons do NOT go in the KB.** A resolved prediction's *lesson* ("market sided with the wage/activity mechanism over the CPI threshold") is a calibration finding → it belongs in auto-memory + PREDICTIONS, not the workbook. The KB holds *facts about the world*, not *lessons about SAM's forecasting*. If a candidate is really a lesson, flag it for SAM to route — don't propose it as a KB row.

**Gold-standard add** (what you're hunting for): a durable structural/mechanism fact discovered mid-research that would otherwise go unfiled — e.g. KB-SAM-175 (uniform-price JGB auctions have no tail by construction). Mechanism + durable figures, not expiring market reads.

### Proposing in ready-to-promote form

Each proposed add goes into `## PROPOSED ADDS` as a **fully-formed KB.tsv row** (all 9 columns, correct next ID, graded, sourced) plus a one-line rationale citing the source artifact. SAM's approval is then a cheap one-liner ("add 1,3,4 — skip 2") and promotion is a mechanical paste into the live tsv. You did the expensive 90% (find / format / grade / dedup-check); SAM does the 10% (ratify).

A proposal survives across sessions in `## PROPOSED ADDS` until SAM rules on it. **Each run, re-check every queued proposal against rows that may have landed meanwhile** — a fact that was novel last week may now be covered.

**Precision over recall — this is load-bearing.** Every proposal costs SAM a read. A list of 15 marginal candidates that yields 3 keeps has *inverted* the offload — SAM now does more work, not less. A short, high-confidence list beats a long one every time. When a candidate is borderline on durability or relevance, do NOT propose it as a row — list it in one line under FLAGGED as an "add-candidate (uncertain)" and let SAM decide whether it's worth a slot. Aim for a proposal list SAM can approve almost wholesale. If a single run surfaces more than ~6-8 strong candidates, that's a signal to surface the *count* and the *theme* and let SAM prioritize, not to dump all of them formatted.

---

## OWNED WRITE-SET (you may write these; touch nothing else)

- `AGENTS/SAM/workbook/KB.tsv` — knowledge base. **Only autonomous write: relocate an already-`SUPERSEDED` row OUT (full mode).** Never new-fact writes, never value/grade/status changes, never cross-ref edits — those are propose/flag.
- `AGENTS/SAM/workbook/KB_ARCHIVE.tsv` — retired rows (receive archived rows, full mode only).
- `AGENTS/SAM/workbook/FLOW.tsv` — flow map. **No live edits.** Spot staleness is flagged-with-value for SAM to apply.
- `AGENTS/SAM/workbook/VX.tsv` — threshold tracker. **No live edits.** Same flag-with-value rule.
- `AGENTS/SAM/workbook/KURA.md` — **only** the `## PROPOSED ADDS` section. You do NOT advance the `Last harvest:` line yourself (see Watermark below) and do not restructure the rest of this file (that's SAM's).
- `AGENTS/SAM/workbook/KURA_MEMORY.md` — you write `## CHANGES SINCE LAST RUN` at run start; append `## LAST RUN`, adjust `## PENDING` and `## STANDING MONITORS`, and write `## NEXT RUN HINTS` at end-of-run. **Do NOT write `## CALIBRATION`** — that section is SAM's view of which patterns held; you can't know your own approve/reject rate from within your own run.

### HANDS-OFF (never touch — these are written by `scripts/boot.py`; editing fights the next boot)

`BOJ_OIS.tsv` · `CFTC_JPY.tsv` · `CPI.tsv` · `FXY_OPTIONS.tsv` · `GPIF_FLOWS.tsv` · `JGB_AUCTIONS.tsv` · `JGB_YIELDS.tsv` · `MOF_FLOWS.tsv` · `TRADE_BALANCE.tsv` · `USDJPY.tsv`

*🔧 Completed 2026-08-04 (SAM, on KURA Run-10 escalation 2): `GPIF_FLOWS` (built 7/9), `TRADE_BALANCE` (6/10) and `BOJ_OIS` (8/4) were all boot-wired but missing from this list — a KURA run could have edited a file the next boot overwrites.* **Do not maintain this list by hand going forward — verify it against `boot.py --tools`, which generates the live toolset from disk.**

Also off-limits: STATUS, THESIS, TIMELINE, CHANGELOG, PREDICTIONS, TRACKER, the per-insurer profiles, the docket (KOYOMI's), and `FLOW_ARCHIVE`/`KB_ARCHIVE` *beyond receiving archived rows*. If one of those needs to change, that's an **escalation, not an edit**.

---

## TRUTH MODEL (how the KB differs from a snapshot — read before editing)

1. **The KB is a RECORD, not a snapshot. Dated point-in-time facts are legitimate — do NOT strip them.** This is the opposite of the docket rule. A row like "30Y-10Y spread ~117bp (May 27)" is a valid dated observation; leave the date and the figure. (Contrast: KOYOMI strips live levels from CALENDAR because the calendar is forward-looking. The workbook is a ledger of what was true when.) The *only* spot that goes stale-in-a-bad-way is in **pointer rows** (rows that explicitly say "live values auto-pull into <tsv>; this row is the durable pointer", e.g. KB-SAM-174) and **FLOW rows** — there, a stale embedded snapshot duplicating an auto-pulled feed may drift from STATUS. **You FLAG that drift with the corrected value; you do not edit the cell** (see the autonomy table — these cells entangle spot with SAM's judgment marks).
2. **Preserve category-clustering, NOT strict ID-sort.** KB.tsv is grouped into 9 category blocks (Insurer, Regulatory, Repatriation, BOJ/Wages, Carry/FX, Household, Framework, Cross-Agent — plus Energy in the archive). IDs jump around within a block (archived rows leave gaps). New rows append to the correct **category block**, not to the numeric end. Never re-sort by ID — it would scatter the categories.
3. **Annotation palimpsest is the KB's characteristic decay mode.** Rows accrete `||`-delimited update-on-update notes (`CONFLICT resolved … || CONFIRMED CURRENT … || FY2025 UPDATE …`). Once a conflict is *stably resolved*, the row should collapse to a clean Key_Fact + one-line provenance — **but collapsing means rewriting the Key_Fact to the resolved value, which is adjudication → FLAG it, don't do it.** Surfacing palimpsest rows for SAM to collapse is one of your highest-value outputs.

---

## KB.tsv FORMAT RULES (a proposed/edited row must conform)

- Columns, tab-separated, 9 of them: `ID  Date  Category  Status  Topic  Key_Fact  Confidence  Source  Notes`
- `ID` = `KB-SAM-NNN`. **Next free ID = one above the current max — DERIVE IT, never read it from a note.**
  ```
  cat AGENTS/SAM/workbook/KB.tsv AGENTS/SAM/workbook/KB_ARCHIVE.tsv | \
    awk -F'\t' '$1 ~ /^KB-SAM-[0-9]+$/{n=substr($1,8)+0; if(n>m) m=n} END{print "KB-SAM-" m+1}'
  ```
  Scan **both** ledgers; never reuse an archived ID. 🔧 **This line used to transcribe a value — *"as of last full read the max was `KB-SAM-175`"* — and by 2026-09-11 the true max was **245**, i.e. it had been wrong by seventy IDs. A hand-copied mirror of a number another file owns is wrong by default; the command above cannot go stale.**
- `Date` = `YYYY-MM-DD`, the date the fact became known/true.
- `Category` = one of the 9 existing categories (match an existing block; don't invent a category without flagging).
- `Status` = `LIVE` (in KB.tsv) | `SUPERSEDED` (SAM-set, awaiting your archive-move) | `HISTORICAL` (in KB_ARCHIVE.tsv).
- `Confidence` = Admiralty/NATO grade: letter A–F (source reliability) + number 1–6 (info credibility). In practice the KB uses `A1` (best) / `A2` / `A3` / `B2` / `B3`, and ranges like `A2-B2`. Grade conservatively on proposals; if unsure, grade lower and say so in the rationale.
- `Source` = where the fact came from (e.g. `TIMELINE 2026-05-31`, `gaiyo p.7`, `TRACKER`, `Bloomberg 5/26/26`).
- `Notes` = context, cross-refs (`Cf. KB-SAM-NNN`), conflicts. Keep it one clean statement on a fresh row — don't pre-stack annotations.

## FLOW.tsv / VX.tsv notes

- **FLOW.tsv** columns: `ID  Name  Speed  Layer  Status  Trigger  Current Position  Pathway  Key Insight  Last Updated`. You do **not** edit FLOW rows. When the spot inside `Current Position` has drifted from STATUS, FLAG it with the corrected value (`FLOW-NN spot stale: <old> → <new>`) for SAM to apply — the cell entangles spot with SAM's probability marks and narrative, so a surgical refresh isn't yours to make.
- **VX.tsv** columns: `ID  Name  Category  Current_Value  Yellow  Orange  Red  Status  Confidence  Last_Updated  Source  Notes`. Same rule — flag a stale `Current_Value` with the corrected figure; do not edit. Threshold bands and `Status` color are always SAM's call.

---

## THE JOB (run sequence)

1. **Read the watermark** (`Last harvest:` in this spec). Everything you harvest must be dated after it. (Inaugural run: no watermark → full sweep.)
2. **Read `KURA_MEMORY.md`** — load `## LAST RUN` (what was done previously), `## PENDING` (open SAM-side decisions to keep in mind), `## STANDING MONITORS` (open items to keep surfacing), `## CALIBRATION` (SAM's pattern-tuning — bias your proposals toward what SAM accepts). Then write `## CHANGES SINCE LAST RUN` based on what's moved in the read-set since the watermark.
3. **Load the workbook** — KB.tsv, KB_ARCHIVE.tsv, FLOW.tsv, VX.tsv. Re-read the existing `## PROPOSED ADDS` queue in `KURA.md`.
4. **Archive** any `Status = SUPERSEDED` rows in KB.tsv → KB_ARCHIVE.tsv. In `full` mode this is the one autonomous edit; in `propose-only` mode, list them under Archived as proposals instead.
5. **Harvest** durable facts from the post-watermark artifacts; run each through the 5-gate rubric; draft passers as ready-formed rows into `## PROPOSED ADDS` (PROPOSE — precision over recall). Re-check the pre-existing queue against newly-landed rows.
6. **Reconcile (no live edits)** — collect into the **FLAGGED** list: spot staleness in FLOW/pointer rows (with corrected value), proposed cross-ref remaps, palimpsest collapses, conflicting figures, dedup/merge candidates, re-grades, stale-flag clusters, standing monitors. You surface all of these; SAM applies/adjudicates.
7. **Propose the new watermark** (today's / the spawn date) in the return block. Do **NOT** edit the `Last harvest:` line yourself — SAM sets it after confirming your run actually covered the window. (Self-advancing on a self-assessed "clean" run is dangerous: if a run quietly ran out of context mid-harvest and advanced anyway, the skipped window is never revisited.)
8. **Write back to `KURA_MEMORY.md`** — append the new `## LAST RUN` entry; adjust `## PENDING` (add new items, do NOT remove resolved-by-SAM ones — SAM clears those); update `## STANDING MONITORS`; write `## NEXT RUN HINTS`. **Skip `## CALIBRATION`** — SAM owns that.
9. **Return** the summary block. Do **not** commit or push — git is SAM's job (agent-git-isolation rule). Leave the working tree for SAM to stage.

> **Sequencing:** SAM must not edit workbook files while you are running — it's a read-modify-write race on the same tsvs. SAM spawns you, waits for your return, *then* applies your flagged edits and commits.

---

## DONE =

- Workbook loaded. In `full` mode: already-`SUPERSEDED` rows relocated to KB_ARCHIVE — nothing else written live. In `propose-only` mode: nothing written live at all.
- Every durable harvest is a ready-formed proposal in `## PROPOSED ADDS`; the list is short and high-precision, none written into a live tsv.
- All spot staleness, cross-ref fixes, and judgment calls are in FLAGGED — none acted on.
- `KURA_MEMORY.md` updated: `## LAST RUN` appended; `## PENDING` / `## STANDING MONITORS` adjusted; `## NEXT RUN HINTS` written; `## CALIBRATION` NOT touched.
- You did NOT touch any hands-off file (the script-written tsvs listed above — **10 as of 2026-08-04; confirm against `boot.py --tools` rather than trusting this count** — or any non-workbook doc).
- You did NOT advance the watermark, commit, or push.
- New watermark is *proposed* in the return block for SAM to set.

## RETURN TO SAM (your summary — keep it tight)

```
KURA workbook run — [date] (mode: propose-only | full)
- Archived:    [full mode: SUPERSEDED rows moved out, by ID | propose-only: PROPOSED archive list]  (or "none")
- PROPOSED ADDS: [N candidates — short & high-precision; list ID + one-line topic each; full rows in the section below]  (or "none")
- FLAGGED (SAM applies / adjudicates):
    · Spot stale (apply): [FLOW/pointer row — old → new from STATUS]
    · Cross-ref fixes (confirm): [row — bad ref → proposed remap]
    · Palimpsest-collapse: [row IDs ripe for collapse]
    · Conflicting figures / re-grade: [IDs]
    · Dedup/merge candidates: [ID pairs + proposed merge]
    · Stale-flag clusters: [IDs + what's stale]
    · Standing monitors: [open items to keep surfacing — JICPA, Norinchukin print, UST-denominator gap, etc.]
    · Add-candidates (uncertain): [one-liners that didn't clear the bar to a full proposal]
- Watermark PROPOSED: [old date] → [new date]  (SAM sets the line after confirming coverage)
- ⚠️ ESCALATIONS: [anything needing a non-workbook edit, or a relevance call you couldn't make]  (or "none")
```

---

## PROPOSED ADDS

*Queue of ready-to-promote rows awaiting SAM approval. Each entry: the full tab-separated KB.tsv row + a one-line rationale citing the source artifact. SAM approves → paste the row into the correct KB.tsv category block → delete it from here. KURA re-checks this queue against newly-landed rows each run.*

### Run 2 — 2026-06-02 (proposed)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 1 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-183). Reference-only; not spawn-read.

### Run 3 — 2026-06-03 (proposed)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 2 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-184, KB-SAM-185). Reference-only; not spawn-read.

### Run 4 — 2026-06-04 (proposed; low-yield window as flagged in spawn prompt)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 1 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-185). Reference-only; not spawn-read.

### Run 5 — 2026-06-09 (proposed; mid-yield in-session window)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 2 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-186, KB-SAM-187). Reference-only; not spawn-read.

### Run 6 — 2026-06-19 (Fri AM, propose-only, post-BOJ + post-FOMC + Iran-deal triple cluster)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 6 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-195, KB-SAM-196, KB-SAM-197, KB-SAM-198, KB-SAM-199, KB-SAM-200). Reference-only; not spawn-read.

### Run 7 — 2026-06-22 (Mon, full mode, quiet-weekend window) — NO NEW PROPOSALS

**Queue status:** Run-6's 6 NEW + 1 v1.6-DRAFT proposals ALL LANDED in KB.tsv (KB-SAM-195/196/197/198/199 promoted Phase A; KB-SAM-200 promoted Phase C with `[v1.6-DRAFT]` Notes-tag). Verified present (KB.tsv rows 138-143). Run-6 PROPOSED-ADDS blocks above are retained for audit (carry SAM's inline RESOLUTION annotations); SAM may prune them at will — KURA leaves SAM's own annotations intact.

**Harvest (Jun 19→22):** 0 genuine 5-gate passers — as the spawn anticipated for this quiet post-cluster weekend. The v1.6 commit that Run-6 NEXT-RUN-HINTS expected to seed 3-5 structural rows (re-centered carry-unwind tail / MOF-decay anchor / FXY-vehicle / Warsh tripwire) HAS NOT LANDED — CHANGELOG still dated 2026-06-18, v1.6 gated on the Mon Jun-22 3:30 PM ET CFTC Jun-16 EV-print + RED pass (both still pending at boot). The structural-KB harvest is therefore DEFERRED to the run that follows the v1.6 commit. Post-watermark material was telemetry or extensions of just-landed rows (see FLAGGED add-candidates-uncertain in the return block): National May CPI (→ CPI.tsv telemetry; durable interpretive content already in KB-169, whose embedded forward call resolved TRUE), MOF 6-day-no-strike (extends KB-199, not a new row), Brent declaratory-Hormuz SHRUG (single event — needs 2nd instance / v1.6).

---

### Run 8 — 2026-06-30 (Mon, propose-only, v1.6.1 JGB DEMAND-VACUUM harvest)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 4 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-201, KB-SAM-202, KB-SAM-203, KB-SAM-204). Reference-only; not spawn-read.

### Run 9 — 2026-07-02 (Thu ~11:15 AM ET, propose-only, post-transmission-map + demand-floor/v1.6.3 window)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 2 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-207, KB-SAM-208). Reference-only; not spawn-read.

### Run 10 — 2026-08-04 (Tue, FULL MODE, ~5-week window Jul 2 → Aug 4: two-sovereign intervention · v1.6.7→v1.6.11 · 5 predictions resolved)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 6 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-209, KB-SAM-210, KB-SAM-211, KB-SAM-212, KB-SAM-213, KB-SAM-214). Reference-only; not spawn-read.

### Run 11 — 2026-08-17 (Mon, FULL MODE, 13-day 8/4 → 8/17 window: THESIS v1.7 frame break · three retractions · two basis corrections)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 4 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-215, KB-SAM-216, KB-SAM-217, KB-SAM-218). Reference-only; not spawn-read.

### Run 12 — 2026-08-20 (Thu, FULL MODE, 3-day 8/17 → 8/20 window: the 20Y adjudicator landed AMBIGUOUS · an adversarial second-eyes pass broke SAM's own replacement number · the auction ledger gapped a second time)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 5 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-220, KB-SAM-221, KB-SAM-222, KB-SAM-223, KB-SAM-224). Reference-only; not spawn-read.

### Run 13 — 2026-08-27 (Thu, FULL MODE, 7-day 8/20 → 8/27 window: MOF weekly reversed at 21-yr scale under a 3-defect instrument repair · v2.0 candidate opened AND killed inside the same window · SAM-41 CONFIRMED · three owed palimpsests ruled)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 3 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-226, KB-SAM-227, KB-SAM-228). Reference-only; not spawn-read.

### Run 14 — 2026-09-02 (Tue, FULL MODE, 6-day 8/27 → 9/2 window: the ¥15.4T MOF monthly landed as a RECORD; USD/JPY back through 160 for the first time since the day BEFORE the op; the whole JGB curve broke to NEW SERIES HIGHS; `jgb_yields.py` silently dropped three sessions across a dark month-boundary and the defect propagated through a derived tsv that had no defect of its own)

> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — all 3 proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv (KB-SAM-229, KB-SAM-230, KB-SAM-231). Reference-only; not spawn-read.

### Run 15 — 2026-09-08 (FULL MODE; post-watermark catch-up and approved integration)

**Verified disposition first:** KB.tsv has **169 data rows**, KB_ARCHIVE.tsv **62**, both uniformly 9 fields; no duplicate or reused IDs across the two files; max ID **232**, no live SUPERSEDED rows. **No archive move and no live-ledger writes.** Run-13/14 adds 226–231 are landed; SAM's KB-232 cutoff-repair row is landed. KB-209's September 8 consolidation closes the old two-legged proposal: **do not append Run-14's obsolete cash-sleeve/convergence wording.** KB-169/197 quote repair is syntactic only; it does not close the substantive items below. All edits below are proposals for SAM, not applied changes.

**One proposed add — KB-SAM-233 (Framework, A1):**

```tsv
KB-SAM-233	2026-09-08	Framework	LIVE	Totan meeting OIS — incremental 25bp equivalents differ from cumulative expected hike counts	Totan publishes indicative OTC meeting-to-meeting OIS medians. Its policy-only interpretation assumes 25bp steps and next-business-day effectiveness; the table supplies the reference terms. An incremental 25bp equivalent is a binary hike probability only under a no-change/one-step assumption. Cumulative expected hike counts can exceed one and are not probabilities. Quotes are indications, not exchange trades: a last-traded timestamp is inapplicable. Preserve each chart vintage and its stated or assumed timezone; the standalone cumulative chart can update independently and must not be spliced into a newer meeting table.	A1	workbook/BOJ_OIS_README.md; reports/2026-09-08_integration.md; reviewed Totan publisher table/methodology saved in research/outputs/2026-09-08_integration/ (publisher: https://www.totan.com/archives/15647)	Japan-specific instrument-reading rule, distinct from KB-SAM-221's historical TFX futures traps. BOJ_MEETING_OIS.tsv is the separate current ledger; BOJ_OIS.tsv stays frozen. Ingestion verifies a SAM-reviewed image hash, source age, expiry, terms and arithmetic; a new chart requires new visual review. REVIEWED_INDICATIVE certifies ingestion validation, not perpetual freshness. No market price is filed here.
```

**Five-gate rationale:** durable instrument semantics, reference-grade when interpreting any BOJ meeting quote, absent from existing KB (221 concerns the retired futures derivation), not a price feed, and Japan-policy-specific. Generic image-review engineering stays in the README. The September 8/9 percentage observations are deliberately excluded. Promotion would take KB.tsv **169 → 170**; next free ID afterward **234**.

#### Exact correction proposals — apply current facts, preserve historical evidence

**P1 — KB-051/197: apply the already-ruled sustain gate and missed verification window; the landed rows contain only the second round-trip sentence.** Keep Status LIVE and existing grades. Before collapsing, preserve each original row verbatim in SAM's chosen before-image archive.

- KB-051 `Topic` → `Brent $90/$120 scenarios — sustain-conditioned oil gate; level alone does not fire`.
- KB-051 `Key_Fact` → `The historical $120 Kharg scenario is a conditional oil-shock scenario. Under SAM's August 20 re-specification, a Brent tag above $90 arms monitoring; the gate fires only on BRENT's sustain call supported by at least two fresh institutional legs. BRENT/FALCON own the physical-supply verdict. A price tag alone does not reactivate a retired carry or FXY entry rule.`
- Both rows `Notes` append → `September 8 ledger reconciliation of prior rulings: preserve the first round-trip ($100.43 on July 23 to $79.98 on August 4) and the second ($94.58 on August 20 to corrected $89.70 BZV26 on August 27). The prior $87.30 August 27 value matched neither named contract; August 26 was $87.84 BZV26, not $86.36, and the three-session decline was 6.94%, not 8.5% (September 1 correction). The September 1 $96.36 BZX26 tag is a later crossing, with FAL-01 unfired at that observation. The August 31 Kharg video was synthetic, not supply-loss evidence. The September 8 assessment does not supply a new owner sustain ruling; maintain price-versus-physical separation. BZX26 is November 2026.`
- KB-197 `Topic` → `June 17 Iran/US initial agreement — historical signing; August verification window missed`.
- KB-197 `Key_Fact`: preserve the dated signing/terms; replace its current `Verification leg OPEN:` sentence with `The original verification watch covered demining, insurance, traffic, Oman fee administration, HEU compliance and sanctions implementation; its approximately August 16 review window passed without SAM adjudication. Record a MISSED review window, not verified implementation or a backfilled live judgment.`
- KB-197 `Notes`: replace `KB-051 (Brent $120 Kharg path — now SUPERSEDED-pending)` with `KB-051 (sustain-conditioned oil gate; remains LIVE)`; append `The August 26 Iran-Oman interim framework is a separate later instrument, not completion of the June agreement's verification leg.`

**P2 — KB-206: close its stale forward adjudicators without upgrading the named-buyer claim.** Keep A2; replace `Topic` with `Meiji Yasuda >¥2T FY2026 super-long plan — conditional bid; September 3 auction SOFT`. Replace the final `Realized-flow confirm OPEN:` sentence in `Key_Fact` with `Subsequent auctions supplied market-level demand evidence; they do not identify Meiji's executed purchases. The announced plan remains A2 trade-press evidence. Auction support is conditional and September 3's 30Y was SOFT on the frozen rule.` Append Notes:

> August 20 20Y: BTC 3.982, tail 1.5bp = AMBIGUOUS/NO-VERDICT, not nearly FIRM; the tail independently fails the FIRM condition. September 3 30Y, graded separately: BTC 3.788, yield tail 2.1bp = SOFT because 2.1 > 2.0, despite cover above its trailing mean. The 0.1bp margin equals quote granularity; preserve the grade and rule precision prospectively. CH-016's frozen auction leg is the August 20 20Y, not the September 3 30Y: both directional branches are unreachable, so NO-VERDICT does not increment the retirement counter (0-of-2; first possible tick September 29). Terminal slope deviation was −14.3bp, only 0.7bp inside the bar: retire the earlier safe-margin claim. Do not infer a named lifer's transactions or a floor break from the yield level. The September 29 40Y has no yield tail by construction (KB-175); any prospective precision ruling must respect tenor-specific auction methods.

Source: STATUS_ARCHIVE September 3/4 blocks; assessment §6; current JGB research. The correction was owed before September 3 and did not land then; do not date the new row amendment as though it did.

**P3 — KB-211/214/229: align intervention instruments with the integrated playbook.** Keep historical measurements; add no September operation conclusion.

- KB-211 `Topic` → `BOJ fiscal factors — forecast, actual and independent broker baseline are different measurements`.
- KB-211: replace `NO year subdirectory` with `prefer the official index-linked path; September 8 testing found both the no-year and /2026/ projection forms returned identical workbook bytes`. Replace `a null can NEVER be graded "no op" — only "MOF did not also fire"` with `a null alone establishes neither no operation nor no MOF participation: ordinary fiscal flows share the line, the independent broker baseline may be absent, and U.S.-only activity is outside this instrument`.
- KB-211: replace `A missed jp pull costs the ~T+2 SPEED, not the verification` with `Final actuals can be recovered from jd, but cannot reconstruct a missed contemporaneous projection or independent broker baseline; recovering one leg does not restore the complete comparison`.
- KB-211: replace Notes' `All figures above are PROJECTIONS, not provisional/final actuals` sentence with `The n=62 distribution and recovered August 3/4/5 values are jd actuals; the separately labelled forward jp anchors are projections. Keep source stage and settlement date on each observation.` Append `A Totan page repeating the BOJ figure is not an independent pre-publication baseline. A BOJ forecast-to-actual residual includes ordinary fiscal surprises. Align Japanese and relevant currency holidays before assigning a trade date; require workbook content/date validation, not HTTP status or URL shape alone. Source: MOF_INTERVENTION_PLAYBOOK.md September 8 controls.`
- KB-214 `Topic` → `USD/JPY daily range — volatility alert with an unresolved intervention-attribution limit`; prepend `Key_Fact` with `Daily range flags unusually large FX moves but cannot distinguish an official strike from an extended grind. ` and replace the first sentence's `usable own-instrument detector for suspected MOF operations` with `volatility-screening input to investigation of suspected MOF operations`. Notes append: `September 3/4 review exposed a qualifying multi-hour grind; any successor attribution instrument needs a shape leg and separate official/settlement evidence. No threshold or historical SAM-39 grade is changed. The September 8 assessment leaves current intervention attribution OPEN.` This harvests the instrument limit, not the prediction lesson.
- KB-229: replace `What the release DOES do at the primary: confirms MOF fired 7/31 alongside the US Treasury` with `The monthly primary confirms aggregate Japanese intervention within July 30–August 26; it cannot alone assign an operation to July 31`. Replace the cash-sleeve conclusion with `Capacity is not use. September 8 reserve-stock evidence and its valuation/window limits are consolidated in KB-209; Japanese funding remains unresolved.` Remove the stale `SAM's palimpsest owed there` instruction. Keep the dated 61% retracement as a historical observation, not a current efficacy mark. **This is a KURA-authored overstatement in an already-promoted A1 row; it needs correction, not a duplicate row.**

**P4 — current claims left behind by the approved demand/energy integration.** Recommended current wording, retaining each row's original dated numbers and source evidence:

- KB-177 `Topic` → `J-ICS and super-long demand — buffer-conditional; blanket no-re-entry claim retired`; `Key_Fact` → `J-ICS reprices assets and liabilities; its effect on demand depends on duration mismatch and capital buffers. Mid-tier step-backs are dated evidence, but Meiji Yasuda's July plan falsified the claim that higher yields never draw insurers back. Economic-value duration matching can support buying; disorderly J-GAAP impairment is a separate mechanism. Current sponsorship is mixed (KB-206/212), and domestic JGB behavior alone does not establish foreign-credit sales.`
- KB-204 `Topic` → `FY2026 super-long issuance reduction — conditional demand and future supply pressure`; preserve its ¥17.4T gross-supply fact and labelled net-supply estimates, but replace `KEY RECONCILIATION` onward with `Lower net supply and higher yields do not uniquely identify a demand collapse: policy repricing, global term premium and changing sponsorship remain alternative contributors. The blanket lifer-abandonment interpretation is retired; current demand is buffer-, yield- and tenor-conditional. FY2027 supply/taper remains a prospective amplifier, not an attribution already established by this arithmetic. Cf. KB-206/212 and September 8 JGB_SUPPLY_DEMAND_THESIS.md.`
- KB-176 `Topic` → `Blockade supply destruction — conditional import-bill inversion, not a permanent oil regime`; Notes append → `The July volume/cost diagnostic found crude volume +5.5% YoY with value +87.8%: the April supply-destruction inversion was not operating in that later observation. Retain April as a blockade-conditional mechanism, not a current regime. The July unit-cost comparison had a +21% discrepancy outside the script's ±20% band; CIF/FOB, insurance and FX explanations were plausible, unverified. September 8's matched crude×FX calculation remains only a price proxy, excluding freight, insurance, grades, LNG lags, hedges and subsidies; stronger yen can cushion rather than eliminate the import-cost increase.` No duplicated live trade-balance mark.

**P5 — repair historical/current labels without inventing new facts.**

- KB-220 `Topic` → `jgb_auctions.py first-result gap — repaired August 20; preserve full-window scan`; date its opening mechanism `Before the August 20 repair, ...`; replace Notes' open fix request with `Fixed August 20: the default loop scans the complete lookback without breaking after its first result. September 8 disk recheck confirms the guard remains at scripts/jgb_auctions.py:386. Preserve the two historical gap examples; --quick still skips the probe and --catalog remains a separate mode.` Current code, not the old promotion note, verifies closure.
- KB-221: retain the five dated futures traps, but replace `cite ~73% converged` and the current `boj_ois.py centralbank.watch` instruction with `The August 17 converged percentage is historical and superseded. Legacy BOJ_OIS.tsv stays frozen; current boj_ois.py uses separately reviewed Totan meeting OIS in BOJ_MEETING_OIS.tsv (BOJ_OIS_README.md; proposed KB-233). Different instrument, no historical splice.`
- KB-199 `Topic` → `June 17–18 no-strike observation — decay interpretation retired`; its existing Notes already govern. No additional decay monitor.
- KB-169 `Topic` → `April CPI record; Tokyo–National core-core comparison corrected on 2025 base`. Do not re-open the completed August 23 remeasurement. Collapse Notes to its **existing** resolved core-core result (six same-month 2025-base pairs, mean −0.13pp; sample window is not publisher-history start), explicitly retiring the older cross-base HOT/exception inference; preserve the full prior text before collapse. The quoting repair did not do this work. The subsidy-wedge remains unmeasured; no new computation proposed.

**P6 — proxy interpretation and stale pointer (lower priority).**

- KB-228 replace `a wrong-but-constant JPY rate cancels in first differences, so CHANGES are the usable output, never the LEVEL` with `A constant assumed JPY rate drops out of computed differences, but real policy-path repricing, timing, futures convexity and expiry proximity still contaminate residual changes; neither level nor change is a direct offshore-basis measurement`. Link KB-232 for cutoff repair; do not re-propose it.
- KB-183: recommend retain B2 as a documented warning, not auto-SUPERSEDE merely because September 1 was unreadable. September 8's nearest RR is inside the plausibility bound while later expiries remain implausible. `Topic` → `FXY options proxy — plausibility gates and independent corroboration required`; replace the sign-only operating rule with `Do not infer direction from an implausible or stale quote; a passing plausibility flag alone does not validate ATM IV or RR against the underlying FX-vol market. Require the prior-session and independent benchmark checks before a directional or cheap-vol citation.` Source refresh to the current plausibility-gated script is still owed.
- KB-174 is a pointer with a May snapshot and expired June focus. Prefer `Topic` → `Volatility and positioning — dated feed pointers`; `Key_Fact` → `Current observations belong to FXY_OPTIONS.tsv and CFTC_JPY.tsv, with quote-quality and vintage checks. CFTC percentage comparisons use KB-217's corrected denominator. No fixed spot or expiry is maintained in this pointer.` This avoids another daily-price KB row.

**Cluster flag, not a bulk rewrite request:** KB-069/120 still say JGB selling proves stress/deleveraging rather than rotation; KB-010/040/049/058/112–124/128/141/142/156/172 contain legacy entry, automatic forced-selling, or deferred-channel language. These are historical model claims on a LIVE surface. SAM should rule a bounded legacy-model status/label sweep; KURA has not inferred individual SUPERSEDED statuses or changed their numbers. KB-152's Q2/Q3 owner-data timing, UST-denominator gap and archive-side KB-200 Topic convention remain SAM rulings, not new defects or autonomous archive candidates.

#### Declines and remaining monitors

No new rows for BOJ odds, daily prices/yields/funding marks, July wages, Q2 GDP revision, or August monthly flows (telemetry / tracker ownership). Reserve funding already lives in KB-209; cutoff repair in 232; monthly aggregate in 229. MOF sector/account labels do not identify GPIF, USTs or named lifers: already explicit in TRACKER/assessment, so no duplicate row. Norway and GPIF changes remain proposals, not transactions; China DCS is provisional product-specific exposure without measured macro transmission. SAM-39's grade and mislabeled Fed quote are calibration/auto-memory territory; the range-method limit is folded into P3, not another add. Auction price-tail versus yield-tail units fit KB-175/206 and the existing unit-discipline memory, not a new row.

Current monitors: fresh reviewed Totan chart/expiry (replacement installed; visual review still required); September 8 funding and September 11 CFTC vintages (no post-rally liquidation inference before them); independent pre-BOJ fiscal baseline and joint settlement calendars; funding-proxy September 14 expiry; prospective auction precision before September 29 (40Y no-tail method); July wage absence closes, June historical backfill remains unverified; owner oil sustain ruling remains unreceived in this harvest. No refresh of frozen FLOW/VX/legacy BOJ_OIS. No daily-price KB add.

**Watermark proposed: 2026-09-02 → 2026-09-08**, covering the completed September 8 integration including its separately timestamped September 9 JST OIS source. KURA has not advanced the spec header. Memory/proposal roll is report-only; SAM applies after dispositions.

### Run 16 — 2026-09-11 (Fri, FULL MODE, 9-day 9/02 → 9/11 window: SAM filed 13 rows directly [233–245] · the Run-15 queue was ORPHANED BY ID COLLISION · 40-file retirement sweep audited CLEAN · KB-SAM-197 archived)

**Verified disposition first (at disk, before any write):** KB.tsv **182 data rows → 181** after the one autonomous act; KB_ARCHIVE.tsv **62 → 63**; both uniformly **9 fields**; **no duplicate or reused IDs across the two files**; **0 SUPERSEDED remain in KB.tsv**. Max live ID **KB-SAM-245**. **Next free ID = KB-SAM-246.** `git diff --numstat` confirms the move touched **exactly one line out and one line in** — no other byte of either ledger changed. `git diff --check` clean.

⚠️ **The `## PROPOSED ADDS` header's "Next free ID: KB-SAM-226" line is stale by twenty IDs and has been stale since Run 12. It is SAM's to fix (KURA owns only the run blocks below it) — but it is now actively dangerous, because the ID-collision failure recorded under ESCALATION 1 is exactly what a stale next-free-ID line produces.**

**3 proposed adds — KB-SAM-246 / 247 / 248, all Framework block, all instrument-basis rows.** In a window this loud (a VERDICT NONE, an oil shock, a 98%-priced MPM, a series backfill) the durable residue is again *what was learned about the instruments*, not what happened — the Run-11 pattern SAM adopted.

```tsv
KB-SAM-246	2026-09-11	Framework	LIVE	USD/JPY READING BASIS (WQ-162) — every level and every USD/JPY-derived COUNT on this desk is USDJPY=X, COMPLETED Europe/London sessions, AS LAST REVISED	Encoded 2026-09-11 as a CONVENTION line, never a revision claim, on SAM-39's PREDICTIONS.tsv row and as the canonical blockquote under STATUS KEY THRESHOLDS. THE BASIS: yfinance USDJPY=X, 1-hour bars aggregated to sessions labeled in Europe/London (the index's own zone), COMPLETED sessions only - the current bar is never scored; intraday range = session high minus session low, in yen; observations taken AS LAST REVISED inside a 30-day upsert window (usdjpy.py --revise-window), NOT as first published. This is NOT the BOJ 17:00 JST reference rate and NOT the MOF curve: never blend or difference across bases. dashboard.py and fetch.py price USDJPY=X read the SAME yfinance series and are basis-compatible; the BOJ 17:00 JST fix is not. THE VINTAGE DIRECTION IS DELIBERATELY OPPOSITE TO LIQUID's GATE-HY-REKILL letter (as FIRST published) AND THE REASON IS THE POINT: HY OAS revisions are rare and first-publication protects a closed count, whereas THIS instrument's revisions ARE its bug fix - it silently understated 2026-07-31 as 2.17y against a true 3.655y, so first-publication grading would have resolved SAM-39 FALSE on a known-defective measurement.	A1	STATUS KEY THRESHOLDS basis blockquote (encoded 2026-09-11); thesis/PREDICTIONS.tsv SAM-39 row; PROME VECTOR-5 packet ask 2 (WQ-162); MEMORY.md 2026-09-11	Two desks holding OPPOSITE vintage conventions is not an inconsistency to reconcile - it is why WQ-162 requires each desk to DECLARE its direction and its reason. Quote this blockquote verbatim into the SAM-39 successor rather than re-deriving the basis (that successor still owes a SHAPE leg). Extends KB-SAM-214, which records the Europe/London bar-labelling defect and the --revise-window hatch but states no reading convention, and sits in KB-SAM-217's class (a corrected basis whose LABEL propagates further than its contract gates). Cf. KB-SAM-183 (read the sign, not the level), KB-SAM-184 (measurement hierarchy). ALTERNATIVE SAM MAY PREFER: fold into KB-SAM-214's Notes instead of a standalone row. KURA proposes standalone because the convention governs EVERY USD/JPY level and count on the desk - KEY THRESHOLDS rows, the VECTOR-5 re-open leg (c) 158 test, the oil-in-yen proxy, SAM-28/31/39 - not only the range detector KB-214 owns.
KB-SAM-247	2026-09-11	Framework	LIVE	THE INDEPENDENT PRE-BOJ FISCAL BASELINE EXISTS — a money-broker month-ahead forecast authenticated by publisher Last-Modified; KB-SAM-211's cannot-source finding is FALSIFIED on its sourcing half	KB-SAM-211 states that the true signal is the GAP vs private money-broker (Tanshi) forecasts, which SAM cannot source or automate (7/11 NOT-BUILD finding). THE SOURCING HALF IS FALSIFIED 2026-09-09: Ueda Yagi publishes a monthly fund supply-demand (jukyu) forecast PDF at uedayagi.com/wp/wp-content/uploads/2026/09/202609jukyu.pdf, dated 2026-09-03, publisher HTTP Last-Modified 2026-09-03 09:40:41 UTC consistent with its 9/3 listing, page 2 visually inspected - a MONTH-AHEAD expectation dated BEFORE the event, which is exactly the independent pre-event baseline the row said did not exist. MEASURED RESIDUALS (outcome minus Ueda / minus BOJ own projection; source units 100 million yen): Sep-7 +330B final = -70B / +10B; Sep-8 -1,100B final = -1,200B / -540B; Sep-9 -3,590B provisional and later FINAL = provisional = +10B / -230B; Sep-10 +340B = -460B / +120B. THE DISCRIMINATING RESULT: the LARGEST drain in the window (Sep-9, -3,590B) is the LEAST suspicious - it matched the independent pre-event forecast to 10B - while a day roughly one third its size (Sep-8) carries the window's largest unexplained residual. That is KB-SAM-211's own conclusion demonstrated at live data: a LEVEL bar (its rejected 2.0T noise floor and 7.0T corroborate bar) reads the wrong variable; the RESIDUAL against an independent pre-event baseline is the instrument. AUTHENTICATION RULE learned the same session: Central Tanshi's September forecast ALSO prints -3,600B, but its page carries a Sep-9 modification timestamp, so it is corroboration only and NOT independently authenticated pre-event evidence - a same-day-modified page cannot witness its own pre-event state.	A1	Own primary pulls; reports/2026-09-09_followthrough.md (Funding and intervention evidence); reports/2026-09-10_news-catchup.md section 2; STATUS INTERVENTION STATUS 2026-09-11; BOJ jd/2026/ and jp/ releases; uedayagi.com 202609jukyu.pdf	THE AUTOMATION HALF OF THE NOT-BUILD STANDS: this is a monthly PDF read by eye, not a wired feed - do not record the finding as fully overturned. Same form class as KB-SAM-211's own PERMANENTLY correction and the FIMA availability-read-as-use retraction: the verifiable half was fine, the claim about what CANNOT be done was not. Scope limits that travel on every cite: a forecast miss is NEVER an operation size; the Japanese settlement series remains SOVEREIGN-BLIND and cannot exclude a U.S.-only operation; Sep-7/8 attribution stays OPEN. OWED AT KB-SAM-211 - both its cannot-source-or-automate sentence and its no-independent-baseline premise need amending; that is adjudication, flagged not applied. Cf. KB-SAM-209, KB-SAM-210, KB-SAM-214, KB-SAM-229.
KB-SAM-248	2026-09-11	Framework	LIVE	TOTAN MEETING-OIS — MORE THAN ONE CHART PER DAY, and a MEASURED intraday dispersion floor of about 0.03 cumulative hikes	The publisher issues the meeting-OIS table more than once per trading day - observed stamps 2026-09-09 11:15 and 15:15 JST, 2026-09-10 11:15, 2026-09-11 11:15 and 15:15 - each a DISTINCT image URL and SHA256 requiring its own SAM visual review (one JSON per stamp in workbook/boj_ois_reviews/); the image carries no timezone, so JST is ASSUMED from the Japanese publisher and is recorded in the timezone_basis column. MEASURED DISPERSION at SAM's own ledger (workbook/BOJ_MEETING_OIS.tsv, terminal 2027-03 cumulative expected hikes): 2.65 [9/09 11:15] to 2.63 [9/09 15:15] to 2.63 [9/10 11:15] to 2.59 [9/11 11:15] to 2.62 [9/11 15:15]. The two SAME-DAY moves are -0.02 and +0.03 over roughly four hours each. Meanwhile the SEPTEMBER meeting is PINNED: incremental 25bp equivalent 98% at all five stamps and OIS 1.2213% identical to four decimal places at four of them. CONSEQUENCE: on this instrument a forward-path change of absolute delta cumulative at or below 0.03 does not discriminate any hypothesis, because the same magnitude occurs WITHIN a single session. Compare like with like - the same clock stamp on both ends - before reading any forward-path delta.	A2	workbook/BOJ_MEETING_OIS.tsv (5 stamps, 25 rows, 2026-09-09 to 2026-09-11); workbook/boj_ois_reviews/*.json; STATUS 2026-09-11 LIVE MARKET DATA	NOT a claim about KB-SAM-240's grade - that is SAM's call and is flagged separately in this run. What this row supplies is the DENOMINATOR that KB-SAM-240's -0.04 must be read against: 240's own endpoints are 11:15-to-11:15, which IS like-for-like and correctly done, but the signal is the same order as the within-session dispersion measured here, which is why B2 rather than A1 was the right grade there. ALSO CARRIED HERE from the unpromoted Run-15 proposal (whose intended ID KB-SAM-233 was subsequently used for a different row - see ESCALATION 1): the standalone cumulative chart can update independently of the meeting table and must NOT be spliced into a newer meeting table, and a quote is an INDICATION not a trade, so a last-traded timestamp is inapplicable. The incremental-25bp-equivalent versus cumulative-expected-hikes distinction is deliberately NOT restated here - it already landed inside KB-SAM-240's Notes. A2 not A1: own ledger and own primary, but the readings are VISUAL transcriptions of an image, the publisher timezone is assumed, and n = 5 stamps over 3 days. Contract and ingestion controls: workbook/BOJ_OIS_README.md. Legacy BOJ_OIS.tsv stays FROZEN and do-not-cite. Cf. KB-SAM-221, KB-SAM-240, KB-SAM-183.
```

**Five-gate rationale (one line each).** **246** — durable reading convention, reference-grade at every USD/JPY cite, absent from KB (KB-214 holds the *defect*, not the *convention*), not a price feed, and it is the basis of SAM's own thresholds and open predictions. **247** — durable instrument + authentication rule with a measured four-day residual table, absent from KB, not tsv territory (the numbers are the *evidence*, the rule is the row), and it repairs a live A1 row's NOT-BUILD claim. **248** — durable publisher/instrument semantics plus a measured noise floor, reference-grade before any forward-path read, absent from KB, and it is a reading rule rather than the quotes themselves.

Promotion of all three would take KB.tsv **181 → 184**; next free ID afterward **KB-SAM-249**. All three append to the **Framework** block (43 → 46), preserving category clustering.

#### FLAGGED — SAM applies or adjudicates (KURA acted on none of these)

**① Cross-ref remap (PROPOSE, confirm before applying) — KB-SAM-223.** Its Source cites `AGENTS/BOND/inbox/2026-08-20_from-SAM_4wk-rolling-sigma-and-n-answered-plus-first-datum-on-the-ratified-form.md`; BOND processed it, so the live path is `AGENTS/BOND/inbox/processed/2026-08-20_from-SAM_4wk-rolling-sigma-and-n-answered-plus-first-datum-on-the-ratified-form.md`. This is the only unresolvable file reference in the whole ledger (bare `fetch.py` in KB-207/239/242 resolves to `FORGE/tools/market-data/fetch.py` and is not a defect).

**② Retirement-sweep cross-ref audit — CLEAN NEGATIVE, and the instrument was falsified before the negative was reported.** All 40 files `git mv`'d into `AGENTS/SAM/archive/` on 2026-09-11 (`fbfd4fede`) were matched against every field of KB.tsv, KB_ARCHIVE.tsv, FLOW.tsv and VX.tsv by full path AND by filename stem: **zero hits in any of the four ledgers.** Positive control run first so the negative means something — the same matcher finds `MOF_INTERVENTION_PLAYBOOK` (2 rows) and `US_INTERVENTION_FUNDING_ESF_SOMA_FIMA` (3 rows), both un-moved. 53 of 181 KB rows cite a file path; none cites a mover. **Nothing to remap — the named movers (`NORINCHUKIN_CLO_FORTRESS_ANALYSIS`, `JAPAN_ENERGY_COMPLEX`, `FXY_ACTIVATION_CARD`, the four `*_FYEND_REPATRIATION` files, the `outbox/` and `proposals/` items) were never cited by the workbook at all.**

**③ Palimpsest — KB-SAM-051, the dead-Brent-figures correction, now owed for a FOURTH run (opened Run 14).** The row still carries `$87.30 [8/27, back BELOW]` in its re-spec ledger. WALTER `SIG-W-20260828-013` corrected this on 9/1: **8/26 was $87.84 BZV26, not $86.36; 8/27 was $89.70 BZV26; SAM's $87.30 matched NEITHER named contract; the three-session slide was −6.94%, not −8.5%.** Direction survives ($89.70 is still under $90 by 30 cents), which is exactly why it has been survivable to defer — and exactly why it will not surface itself. SAM's 2026-09-11 `ANNOTATED` append addressed the Kharg-headline authentication question and left the wrong prices in place. **The same wrong figure has now been carried into the archive at KB-SAM-197, disclosed in its ARCHIVED stamp rather than silently corrected.**

**④ Re-grade question (adjudication, SAM's alone) — KB-SAM-240 against proposed KB-SAM-248.** 240 reads a −0.04 cumulative shave across two oil sessions as a direction. The same ledger now shows **+0.03 inside four hours on 9/11 and −0.02 inside four hours on 9/09**, and **15:15-to-15:15 across BOTH oil sessions is 2.63 → 2.62 = −0.01**. 240's own 11:15-to-11:15 endpoints are like-for-like and its B2 grade and registered falsifier already carry the caution, so KURA proposes **no change** — but SAM should rule explicitly whether 240's Notes should carry the dispersion floor, because a future reader will otherwise compare stamps of different clocks. **KURA does not touch a Confidence grade.**

**⑤ Archive-side contradictions disclosed at KB-SAM-197, not resolved (see the ARCHIVED stamp).** The archived row simultaneously carries `STAYS LIVE -- re-specified, NOT superseded` in a mid-row annotation and `SUPERSEDED` in its Status; and it calls KB-051 `now SUPERSEDED-pending` while KB-051 is LIVE. Both are Key_Fact/Notes adjudication. **Live cross-refs to KB-197 remain at KB-SAM-051 and KB-SAM-198** — both now point into the archive, which is conventional (archived rows keep their IDs) but worth SAM knowing.

**⑥ Category typo — KB-SAM-245 reads `BOJ-Wages` (hyphen) where the canonical block label is `BOJ/Wages` (slash).** It is the only row in the file carrying that spelling (16 `BOJ/Wages` vs 1 `BOJ-Wages`), so it is invisible to any category-scoped scan or sort. **Value-cell edit ⇒ SAM's, not KURA's.**

**⑦ Add-candidates (uncertain) — declined from a full proposal, listed so SAM can overrule.** (a) The **`consumer_check` 🔴 still open at WALTER `BOARD/SIG-W-20260810-002:33`** — a delivered-and-unconsumed correction is a cross-agent state, not a durable fact, and SAM already says it is not SAM's to edit. (b) The **`≥160 count does not exist`** SEARCH-NOT-FOUND correction to DOCKET L328/L34 — real and load-bearing, but it is a correction to another desk's index, already annotated at the owner surface. (c) **The vendor-feed rejection for the Dec-26/Mar-27 futures pair** (Yahoo rounding = 3.06bp of the signal; legs desynchronised by 10h29m46s / 37,786s) — genuinely durable, but KB-SAM-244 already carries both defects inside its own Notes as the *weaker* reasons for the same decline, and a second row would split one decision across two lookups.

#### Declines, tested against the spawn brief's own candidate list (precision over recall)

The brief named four candidates and **three are already filed by SAM's own hand** — checked at disk, not taken on trust: **August CGPI import prices falling in both currencies with petroleum the largest drag = KB-SAM-241** (including the 7.7%/7.4% PPI vintage correction); **Totan September pinned at 98% across consecutive stamps while the forward path moved = KB-SAM-240**; **bank ADRs rose on the +5.6% Brent day while EWJ fell = KB-SAM-242** (the figures are in its Key_Fact verbatim). The fourth, the **US August CPI print** (core +0.3% m/m, one tick soft), is **declined on Gate 1 and Gate 5**: a monthly US print that expires into the 9/16 FOMC, whose SAM-side consequence (Waller's vote) is Fed-side telemetry the desk already refuses to grade. Also declined: the **MOF weekly 4-week rolling −¥1.55T 🟡** and the third straight JGB inflow week (Gate 4, `MOF_FLOWS.tsv`); the **Sep-10 no-intervention-signature settlement** (telemetry under KB-SAM-211's existing mechanism); **SAM-28's +4.49% magnitude bar clearing with no eligible route** (PREDICTIONS carve-out — a fact about the record, not the world); the **STATUS hot/cold split and `STATUS_REFERENCE.md`** (SAM-internal doc hygiene, the Run-14 STATUS-rotation decline class); and the **`CURRENT UNAVAILABLE` regression-test rot** found 9/9 (calibration carve-out — it is `[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]`, already in auto-memory, recommend appending the instance rather than minting a row or a slug).

**Watermark proposed: 2026-09-02 → 2026-09-11.** KURA has not advanced the `Last harvest:` line. Note the line currently reads Run 14 / 2026-09-02 and is **correct** — Run 15 proposed 9/08 and SAM never set it, so this run genuinely re-covered 9/02 → 9/08 as well as 9/08 → 9/11.


---

**Your closeout has always had a WRITE step. It now has a PRUNE step, because the write step alone was never enough.**

### Why this exists — measured, not theoretical
SAM's own surfaces are capped (`STATUS.md` **250 lines**, `MEMORY.md` **100**) because unbounded accumulation drowns signal. **Your state file had no such rule and nobody noticed until it was measured on 2026-08-20:**

| | spec | state | total a spawn reads first | |
|---|---|---|---|---|
| **METSUKE** | 20K | **370K** | **~100K tokens** | before looking at a single artifact |
| **KURA** | 158K | 176K | ~85K tokens | |
| **KOYOMI** | 17K | 119K | ~35K tokens | |

⚠️ **And the cost was already realised, not hypothetical:** METSUKE's `## PENDING` was found holding **97 open items**, most made moot by a ruling issued 13 days earlier, **surviving 14 runs** — because nothing in the closeout ever asked *"what does this ruling close?"*

### The rule
1. **At closeout, run:** `.venv/bin/python3 AGENTS/SAM/scripts/subagent_memory_roll.py <your state file>` — **report-only by default.** Include its output in your return block.
2. ⛔ **You PROPOSE the roll. SAM applies it.** Do not pass `--apply` yourself — same propose-only pattern as everything else you do.
3. ⛔ **MOVE, NEVER DELETE.** Terminal run-history goes to `<YOUR>_MEMORY_ARCHIVE.md` **verbatim**; the tool refuses to write if bytes are lost. **Closing by adjudication, never by tidying.**
4. ⛔ **TERMINAL MEANS EXPLICITLY MARKED CLOSED.** An unmarked block stays LIVE. **Silence is never read as closure.**
5. **Archives are reference-only and NOT boot-read.** Do not read yours at boot; read it when you need a historical disposition.
6. 🔑 **AND THE PART THE TOOL CANNOT DO FOR YOU: when SAM issues a ruling that changes what counts as open, sweep your own backlog against it IN THE SAME RUN.** *(METSUKE Run-16 is the model: **97 → 0, with 208 insertions and ZERO deletions**, every item classified and closed with a reason.)* **A ruling governs the next write, not the existing state — so pair every ruling with a retroactive sweep.**

⚠️ **`## CALIBRATION` never rolls and you never write it — that is SAM's.** `## STANDING MONITORS`, `## NEXT RUN HINTS`, `## CHANGES SINCE` and the LIVE `## PENDING` never roll either: they are the working set.
