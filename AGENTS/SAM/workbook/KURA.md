# KURA — Workbook Librarian (SAM-internal sub-agent)

**Name:** KURA (蔵, "storehouse / repository")
**Type:** SAM-internal sub-agent. Spawned only by SAM, on command or at closeout. **Not a network peer** — no `AGENTS/KURA/` home, not on PROME's coordination surface, never appears in `AGENTS/SIGNALS.md` or the cross-agent roster.
**Mandate:** Hold the `workbook/` in context so SAM doesn't have to re-read 119+ rows every session. Harvest durable facts SAM's session work produced, reconcile/archive stale rows, and surface the genuine judgment calls. **Keep the workbook current without SAM paying the context cost.**

**Last harvest:** 2026-06-03 (Run 3; 1 KB add promoted — KB-184 MOF intervention measurement scope (A1, Framework). KB-185 thin-liquidity prediction-market discipline RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` by Will — transferable cross-agent discipline, not Japan-specific. KB-183 routing precedent narrowed: tool-specific *and* SAM-domain-only → KB; cross-agent transferable rules → auto-memory. + 2 FLOW spot-stale fixes — FLOW-JPN-5.02 + 6.02)

---

## ORIENTATION (read first)

You are a sub-agent spawned by SAM with a **fresh context**. Your working directory is the **repository root** (`/home/willi/Research-workspace`), NOT the SAM agent folder. Every path in this brief is written from that root. SAM's home is `AGENTS/SAM/`; the workbook you maintain is `AGENTS/SAM/workbook/`. If you ever see a bare path, prefix it with `AGENTS/SAM/`.

### How SAM spawns you (canonical invocation)

SAM invokes you via the Agent tool with a prompt like:

> You are KURA, SAM's workbook librarian. Read `AGENTS/SAM/workbook/KURA.md` (spec) and then `AGENTS/SAM/workbook/KURA_MEMORY.md` (state — prior runs, pending items, standing monitors, calibration). Follow the spec exactly. **Mode: `propose-only`** (or `full`). Harvest durable facts from SAM's session artifacts (post-watermark) into ready-formed proposed KB rows, and flag everything else — spot staleness, cross-ref fixes, palimpsest collapses, conflicts, dedup, standing monitors — for SAM to apply. The only thing you write to a live tsv is an archive-move of an already-SUPERSEDED row, and only in `full` mode. Propose the new watermark; do not set it. At end-of-run, update `KURA_MEMORY.md` (`## LAST RUN` append, `## PENDING` / `## STANDING MONITORS` adjust, `## NEXT RUN HINTS` write; do NOT touch `## CALIBRATION` — that's SAM's). Do not commit or push. Return the summary block defined in the brief.

The mode defaults to `propose-only` when unstated.

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
| Archive a row whose `Status` is **already** `SUPERSEDED` | **ACT** (in `full` mode only; **PROPOSE** in `propose-only` mode). Move it to `KB_ARCHIVE.tsv` (set `Status` → `HISTORICAL` if it's a permanent retirement; keep `SUPERSEDED` if it's a versioning supersede — match the archive's existing convention). This is the **only** autonomous-act in the brief, and only because SAM already made the call by setting `Status = SUPERSEDED` — you merely relocate the row. |
| Refresh stale spot in a FLOW/pointer row | **FLAG-with-value.** Do NOT edit the cell. These cells are entangled prose — a single `Current Position` blob mixes the spot, SAM's probability marks, and dated notes. Surfacing a surgical edit to a fresh-context agent risks clobbering a judgment-encoding figure. Report `FLOW-NN spot stale: <old> → <new from STATUS>` and let SAM make the one-cell edit. |
| Fix a broken cross-ref | **PROPOSE.** Cross-ref targets may be artifacts of an old numbering scheme — an "unambiguous" autofix can silently corrupt the reference graph (the worst error: nothing surfaces it). Name the row, the bad ref, and your proposed remap; SAM confirms before any change lands. |
| Change a `Key_Fact` value, re-grade `Confidence`, set a row's `Status` → `SUPERSEDED`, or pick which of two conflicting figures wins | **FLAG only.** This is thesis adjudication — SAM's call, never yours. |
| Dedup / merge two overlapping rows (merge is lossy) | **PROPOSE only.** Name the two IDs + your proposed merged row; SAM confirms. |

**The one rule:** when in doubt about whether something is durable / relevant / which figure wins — **flag or propose, never act.** Bias hard to the gate; the single autonomous act (archiving an already-SUPERSEDED row) is the only place you write to a live tsv without SAM's per-item sign-off.

### RUN MODES

SAM names the mode in the spawn prompt:
- **`propose-only`** (default for the inaugural run and any low-trust run) — write **nothing** to a live tsv, not even archive-moves. Everything, including proposed archives and spot fixes, goes into the return block / `## PROPOSED ADDS`. This lets SAM grade your judgment before any autonomy is granted.
- **`full`** — the single autonomous act (archive already-SUPERSEDED rows) is live; everything else still propose/flag per the table.

If the mode isn't stated, assume **`propose-only`**.

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
| **Not already in KB** | You hold all 119 rows — dedup is your native advantage | already covered by an existing row → reject (or propose a merge instead) |
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

`CFTC_JPY.tsv` · `CPI.tsv` · `FXY_OPTIONS.tsv` · `JGB_AUCTIONS.tsv` · `JGB_YIELDS.tsv` · `MOF_FLOWS.tsv` · `USDJPY.tsv`

Also off-limits: STATUS, THESIS, TIMELINE, CHANGELOG, PREDICTIONS, TRACKER, the per-insurer profiles, the docket (KOYOMI's), and `FLOW_ARCHIVE`/`KB_ARCHIVE` *beyond receiving archived rows*. If one of those needs to change, that's an **escalation, not an edit**.

---

## TRUTH MODEL (how the KB differs from a snapshot — read before editing)

1. **The KB is a RECORD, not a snapshot. Dated point-in-time facts are legitimate — do NOT strip them.** This is the opposite of the docket rule. A row like "30Y-10Y spread ~117bp (May 27)" is a valid dated observation; leave the date and the figure. (Contrast: KOYOMI strips live levels from CALENDAR because the calendar is forward-looking. The workbook is a ledger of what was true when.) The *only* spot that goes stale-in-a-bad-way is in **pointer rows** (rows that explicitly say "live values auto-pull into <tsv>; this row is the durable pointer", e.g. KB-SAM-174) and **FLOW rows** — there, a stale embedded snapshot duplicating an auto-pulled feed may drift from STATUS. **You FLAG that drift with the corrected value; you do not edit the cell** (see the autonomy table — these cells entangle spot with SAM's judgment marks).
2. **Preserve category-clustering, NOT strict ID-sort.** KB.tsv is grouped into 9 category blocks (Insurer, Regulatory, Repatriation, BOJ/Wages, Carry/FX, Household, Framework, Cross-Agent — plus Energy in the archive). IDs jump around within a block (archived rows leave gaps). New rows append to the correct **category block**, not to the numeric end. Never re-sort by ID — it would scatter the categories.
3. **Annotation palimpsest is the KB's characteristic decay mode.** Rows accrete `||`-delimited update-on-update notes (`CONFLICT resolved … || CONFIRMED CURRENT … || FY2025 UPDATE …`). Once a conflict is *stably resolved*, the row should collapse to a clean Key_Fact + one-line provenance — **but collapsing means rewriting the Key_Fact to the resolved value, which is adjudication → FLAG it, don't do it.** Surfacing palimpsest rows for SAM to collapse is one of your highest-value outputs.

---

## KB.tsv FORMAT RULES (a proposed/edited row must conform)

- Columns, tab-separated, 9 of them: `ID  Date  Category  Status  Topic  Key_Fact  Confidence  Source  Notes`
- `ID` = `KB-SAM-NNN`. **Next free ID = one above the current max** (scan the file; as of last full read the max was `KB-SAM-175`, so the next add is `KB-SAM-176`). Never reuse an archived ID.
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
- You did NOT touch any hands-off file (the 7 script tsvs or any non-workbook doc).
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

**KB-SAM-183 (Framework)** — `fxy-proxy-v1` failure mode: ATM_IV can collapse to near-zero (read sign/trend, not absolute)

```
KB-SAM-183	2026-06-02	Framework	LIVE	FXY Vol Proxy (`fxy-proxy-v1`) — Read Sign Not Level	The `fxy-proxy-v1` ATM_IV / RR25 calc in `fxy_options.py` can collapse to near-zero or extreme readings (Jun 2 print: Jun-18 ATM IV 1.56% vs 10.52% Jun 1; Jul-17 1.17%; Sep/Dec 0.39%; RR25 -38.62 vs -8.11). When this fires, Vol_Quality flips to `approx` on the longer tenors but can read `ok` on the nearest expiry. Operating rule: read sign and direction of change, not the absolute level; cross-check vs prior session and CME CVOL (JPVL) before citing.	B2	FXY_OPTIONS.tsv Jun 2 vs Jun 1 (rows 62 / 66); SAM STATUS Jun 1 RR25 caveat	Cf. KB-174 (Vol Positioning Current Read). Calibration anchor for any future vol-proxy reading. Proxy-scale ≠ OTC RR — already flagged in STATUS Jun 1; promoting that caveat to durable KB. Will likely need a `fxy-proxy-v2` revision before this row retires.
```

**Rationale:** Jun 2 boot surfaced an apparent data anomaly in the auto-pulled vol feed — ATM IV reading 1.56% (Jun-18) and 0.39% (Sep/Dec) is implausible mid-June BOJ window pricing. SAM is reading sign-only and has flagged level as suspect in MEMORY NEXT SESSION #9 ("vol-proxy recalibration now urgent"). The caveat is durable (it's a methodology fact about `fxy-proxy-v1`, not a single tape print) and reference-grade (next time the proxy prints weird, this row is the lookup). Gate test: Durable ✅ (methodology, not telemetry) / Reference-grade ✅ / Not in KB ✅ (KB-174 covers the LIVE read pointer but not the proxy-failure mode) / Not tsv-territory ✅ (this is interpretation of the tsv, not the tsv data itself) / Thesis-relevant ✅ (vol read feeds 3-of-3 convergence read, position decisions). Conservative grade B2 — proxy methodology not yet primary-source documented.

*(KURA judgment-call note: this is borderline at the "Framework" category since it shades into "process/calibration." Routed it as Framework KB row rather than auto-memory because it's a fact about a specific SAM tool, not a transferable agent-cross-cutting lesson. SAM may prefer to push it to auto-memory or to a `scripts/README.md` instead — flag for SAM call.)*

**[Run-2 RESOLUTION 2026-06-03]:** SAM approved KB-SAM-183 as Framework KB row (landed in KB.tsv row 126). Routing call settled in favor of KB over auto-memory / scripts/README. Pattern: tool-specific methodology caveat earns a KB row when the tool drives thesis-level reads (vol proxy feeds 3-of-3 convergence + position decisions). Logged for SAM CALIBRATION pass.

---

### Run 3 — 2026-06-03 (proposed)

**KB-SAM-184 (Framework)** — MOF intervention measurement scope: lead with monthly aggregate; footnote named-op estimates

```
KB-SAM-184	2026-06-03	Framework	LIVE	MOF Intervention Measurement Scope — Lead With Monthly Aggregate	MOF official monthly aggregate (released via 為替介入実施状況 monthly report ~3-5 days after month-end) is the AUTHORITATIVE intervention size figure — lead with it. Named-op intraday estimates (Reuters/BofA back-out from BOJ daily settlement-balance discrepancies) carry ±10-15% noise per operation and routinely miss small unflagged smoothing ops. Apr 28–May 27 worked example: official ¥11,734.9B vs two-op named-op sum ¥9.78T (Apr 30 ¥5.48T + May 6 ¥4.3T) = ~¥1.95T residual (~17% gap) classifiable as ~70% back-out slippage / ~30% possible unflagged smoothing op. Per-op breakdown only available in MOF quarterly per-op release.	A1	MOF 為替介入実施状況 May release (2026-05-29) / Reuters & BofA Apr 30 + May 6 BOJ-balance back-outs / SAM verification 2026-06-03	Resolves the Apr 30 + May 6 named-op estimate vs MOF authoritative aggregate question for KB-170. Reaction-function intensity read unchanged — both methods show "largest round since 2022." Cf. KB-170 (named-op #1+#2 estimates). Future intervention measurement: STATUS leads with MOF monthly authoritative; footnotes named-op estimates with provenance.
```

**Rationale:** Today's PM verification (commit `1122060a`) resolved a real STATUS-vs-Trading-Economics discrepancy between ~¥10T (Reuters/BofA two-op back-out) and ¥11.73T (MOF authoritative). The resolution methodology — lead with the monthly aggregate, footnote the back-out estimates with their ~±10-15% per-op noise — is a durable measurement-discipline fact, not a one-off tape print. Next time SAM (or any consumer of MOF intervention data) faces the same question, this row is the lookup. Gate test: Durable ✅ (methodology, not the figure itself — the figure lives in KB-170 / STATUS) / Reference-grade ✅ (named provenance hierarchy) / Not in KB ✅ (KB-170 documents named-op #1+#2 but no row codifies the source-hierarchy methodology) / Not tsv-territory ✅ (methodology, not an auto-pulled feed) / Thesis-relevant ✅ (Channel 3 is a v1.5 pillar; measurement integrity feeds reaction-function intensity reads). Conservative grade A1 — primary-source documented (MOF release) with cross-method delta quantified. **Gold-standard add per spec — mechanism + durable provenance hierarchy.**

**KB-SAM-185 (Framework)** — Thin-liquidity binary prediction-market read rule: single-print ≠ "holds"; require cross-source

```
KB-SAM-185	2026-06-03	Framework	LIVE	Thin-Liquidity Prediction-Market Single-Print Discipline	Thin-liquidity binary prediction-market prints (Polymarket BOJ-hike contracts, Kalshi event markets) can move 5-10pp on a single trade in low-volume contracts — a single-print move is NOT a "holds." Operating rule before any mark update from a prediction-market signal: (1) require pricing to hold at the new level on a re-check ≥3 trading days later; (2) cross-verify against an independent source (swap pricing via OIS, dealer-desk read e.g. MUFG, Bloomberg consensus); (3) where prior failures on the same mechanism establish an earned-discount calibration, hold below market until both gates pass. Worked example Jun 3: Polymarket BOJ Jun 16 hike 87.6% → 94.8% (+7pp/24h); SAM-21 HELD 70% — pre-registered mechanical trigger "if Polymarket ≥90% on Jun 9 re-check AND no Takaichi pushback → +5pp to 75%." Earned-discount basis: SAM-08 (90% too-hawkish FAIL) + SAM-20 (60% too-hawkish FAIL) on same Takaichi-ceiling mechanism.	B2	SAM Jun 3 PM session (commit `1122060a` STATUS pre-registered trigger) / SAM-21 honesty caveat (STATUS § BOJ ASSESSMENT) / PREDICTIONS_ARCHIVE SAM-08, SAM-20 lessons	Cf. KB-058 (Stop Discipline conjunction rule — same "both-conditions-required" pattern). Calibration-flavored but anchored to a specific tool-class (binary prediction markets) and stated as an operating rule, so reads as Framework methodology rather than agent-cross-cutting lesson. SAM may prefer routing to auto-memory if the rule generalizes beyond Japan-macro probability marks — flag for SAM call.
```

**Rationale:** Today's Polymarket +7pp/24h move was correctly NOT chased; the discipline that produced that outcome (single-print isn't a hold; cross-verify; honor earned-discount calibration on prior-failure mechanisms) is reference-grade and SAM has now applied it twice in two sessions (Jun 2 87.6% → didn't move from 70%; Jun 3 94.8% → didn't move from 70% but pre-registered trigger). Gate test: Durable ✅ (methodology, not telemetry) / Reference-grade ✅ (operating rule with three named gates) / Not in KB ✅ / Not tsv-territory ✅ / Thesis-relevant ✅ (Polymarket drives mark updates on SAM-21, SAM-23 routinely). Conservative grade B2 — methodology synthesized from session work, not yet primary-source documented as a published rule. **Borderline placement** (Framework KB vs auto-memory) — this is the same borderline that came up with KB-183 (proxy methodology); since SAM ruled in favor of KB for tool-specific methodology, applying the same routing here. Flag for SAM to re-decide if the rule reads more universal than Japan-macro.

**[Run-3 RESOLUTION 2026-06-03]:** Will RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` — cross-agent transferable discipline (LIQUID/HENRY/BROCK also read Polymarket/Kalshi prints), not Japan-macro-specific. KB-183 routing precedent NARROWED: Framework KB = tool-specific AND SAM-domain-only; cross-agent transferable rules → auto-memory. Test refined for future borderlines. Row NOT promoted to KB.tsv.

---

### Run 4 — 2026-06-04 (proposed; low-yield window as flagged in spawn prompt)

**KB-SAM-185 (BOJ-Wages)** — Sato Ayano replaces Nakagawa Jun 30: Apr-28 hike-dissent bloc 3 → 2 — **CONDITIONAL ON KOYOMI PRIMARY-SOURCE VERIFICATION**

```
KB-SAM-185	2026-06-30	BOJ-Wages	LIVE	Sato Ayano Replaces Nakagawa — Apr-28 Hike-Dissent Bloc 3 → 2	Sato Ayano (Aoyama Gakuin University law prof, reflationist, Takaichi appointee) takes Nakagawa Junko's BOJ Policy Board seat Jun 30 2026 (Nakagawa term expires Jun 29). Nakagawa was one of the three Apr 28 2026 active dissenters who voted FOR the 1.00% hike (alongside Takata Hajime and Tamura Naoki); Sato is reflationist. The Apr-28-style active hike-dissent bloc therefore drops from 3 → 2 unless Sato surprises. Material dovish shift in marginal-vote count for the post-Jun-16 PATH/CEILING story (beyond 1.00% gets harder); no Jun-16 binary impact (Sato seats Jun 30, after MPM Jun 16-17). Sato is Takaichi's 2nd dovish BOJ board appointment after Asada (Mar 2026).	A2	BOJ Policy Board official page (Nakagawa term-end) / Bloomberg + Japan Times + Nikkei (Sato Ayano characterization, Jun 4 verification window) / SAM CHANGELOG 2026-06-04 entry (c)	Cf. KB-SAM-058 (Takaichi ceiling — Stop Discipline), THESIS § Channel 3 (BOJ board stacking dovish). Strengthens v1.5.1 path-MEDIUM near-term-timing conviction (post-June ceiling harder); affirmatively closes the "no Takaichi/cabinet pushback" pre-condition of the SAM-21 Jun-9 mechanical trigger by way of the Takaichi government's broader posture. Date corrected Jun 4 from prior Jun 16 framing (SAM was conflating with the BOJ MPM in 4 places — STATUS, THESIS L182, CALENDAR L28, CATALYSTS row 8). HOLD PROMOTION until KOYOMI verifies the "Nakagawa actively voted for 1.00%" characterization clears primary-source quarantine.
```

**Rationale:** Material durable board-composition fact with explicit thesis-side consequence (post-June PATH/CEILING harder via marginal-vote arithmetic). The date is locked by procedural fact (Nakagawa term expiry per BOJ official page). The thesis-relevance is locked by the CHANGELOG 2026-06-04 entry (c) where SAM explicitly writes "Apr-28-style hike-dissent bloc drops 3 → 2 unless Sato surprises. Material dovish shift in marginal-vote count for the post-June PATH/CEILING — strengthens v1.5.1 path-MEDIUM conviction; no Jun-16 binary impact." Gate test: Durable ✅ (board seating is structural; Sato term begins Jun 30) / Reference-grade ✅ (named individual, dated event, named consequence chain) / Not in KB ✅ (KB-SAM-058 references the Takaichi ceiling broadly but no row codifies the board-composition dissent arithmetic) / Not tsv-territory ✅ (composition fact, not an auto-pulled feed) / Thesis-relevant ✅ (Channel 2/3 path-MEDIUM conviction half of v1.5.1 decomposition rests on the post-June ceiling arithmetic). **Gold-standard add per spec — durable structural fact with explicit consequence anchor.**

**⚠️ Hold-promote condition (per Will's Run-4 brief):** "Do NOT add to KB if KOYOMI quarantines — wait for verification." KOYOMI is running in parallel on Sato characterization. Three branches:
- **KOYOMI returns CONFIRMED** on "Nakagawa actively voted for 1.00% Apr 28" + Sato characterization → SAM promotes this row as drafted (consider upgrading A2 → A1 if KOYOMI sources primary-source language).
- **KOYOMI returns REFRAMED** (e.g., Nakagawa dissented but not specifically for 1.00%, or Sato characterization softer) → SAM softens the row ("active-dissent bloc reshapes" rather than "3 → 2 unless Sato surprises") before promoting.
- **KOYOMI returns QUARANTINED** (primary sources unavailable or contradictory) → SAM declines the row; revisit when KOYOMI clears the quarantine.

**Routing note:** Filed under BOJ-Wages category (BOJ Policy Board composition fact, with policy-path consequence). Alt categories considered: Regulatory (rejected — policy-personality, not regulatory action), Framework (rejected — this is a fact, not a methodology). Conservative A2 grade — multi-source secondary aggregator (Bloomberg + Japan Times + Nikkei + BOJ official page); A1 upgrade reserved for KOYOMI primary-source confirmation.

*(KURA judgment-call note: this is the only Run-4 promote candidate clearing the 5-gate rubric. The other three Will-flagged candidates — discipline-credibility pattern, Aug-2024-speed conditional, OS.1 3-question rubric — all route elsewhere; see FLAGGED add-candidates uncertain. Precision-over-recall held; did not pad with cross-agent-transferable items per the Run-3 CALIBRATION refinement.)*

**[Run-4 RESOLUTION 2026-06-04 PM]:** KOYOMI Run 6 cleared all 4 sub-claims primary-source. SAM promoted KB-SAM-185 to KB.tsv row 128 (BOJ-Wages, A1 graded up from A2 on primary-source verification).

---

### Run 5 — 2026-06-09 (proposed; mid-yield in-session window)

**KB-SAM-186 (Framework) — CATALYST-PATH DECOUPLING — level-reads vs path-reads — BORDERLINE / ROUTING-PENDING**

```
KB-SAM-186	2026-06-09	Framework	LIVE	Catalyst-Path Decoupling — Level-Driven vs Path-Driven Triggers	When a framework anchors mark-up/mark-down conjunction triggers on an assumed catalyst path (e.g. SAM-23: MOU break → oil rally → yen-weak → USDJPY upside → MOF intervention), a different upstream path hitting the same downstream level invalidates path-dependency without invalidating the level read itself. Two empirical decouplings observed Jun 5-9: (1) Fri Jun 5 USDJPY tagged 160.20 via US-side NFP shock (+172K vs 85K, DXY +0.66%) — not via yen-side MOU/oil; (2) Tue Jun 9 Brent breached the "$90 = headwind resolved" line via China demand + Trump-Iran walk-back rumors WHILE USDJPY held above 160.37 — oil-leg and USDJPY-leg moved opposite to the path. Operating rule: distinguish "level trigger fires if level is met by any path" from "path trigger fires only if upstream sequence holds intact." For SAM-23 in particular: intervention probability is HIGH at USDJPY 160+ regardless of upstream driver (level-driven), so SAM-23 mark holds via the level read even when the assumed MOU/oil path decouples. Pre-registered conjunction triggers gate against the path; an additional level-only trigger may be warranted post-Jun-16 settle.	B2	STATUS § INTERVENTION STATUS Sat Jun 6 + Tue Jun 9 evals; TIMELINE Jun 5-6 + Jun 8-9 RESOLVED blocks; MEMORY NEXT SESSION #4 (re-anchoring candidate); auto-memory candidate `finding_catalyst_path_decoupling` flagged	Cf. KB-058 (Stop Discipline conjunction rule), KB-185 (Sato BOJ Path/Ceiling — also level-vs-path framing). ⚠️ BORDERLINE ROUTING: Per Run-3 narrowed rule (tool-specific AND SAM-domain-only → KB; cross-agent transferable → auto-memory), this candidate sits between — Japan-macro-specific worked example BUT the rule generalizes to any agent anchoring a conjunction trigger on an assumed catalyst path. SAM/Will routing call needed; if re-routed to auto-memory `finding_catalyst_path_decoupling`, drop this row.
```

**Rationale:** Two distinct micro-windows (Jun 5 USD-side route + Jun 9 oil-leg inversion under USDJPY-leg stable) provide empirical decoupling of the SAM-23 framework's assumed catalyst path from the level read. The discipline lesson — distinguish level-driven from path-driven triggers — is durable and reference-grade. Gate test: Durable ✅ (structural framework rule, not telemetry) / Reference-grade ✅ (named operating rule with two worked examples) / Not in KB ✅ / Not tsv-territory ✅ / Thesis-relevant ✅ (SAM-23 framework re-anchoring candidate per MEMORY NEXT SESSION #4). Conservative B2 grade. **Borderline placement** — per Run-3 narrowed rule this likely re-routes to auto-memory; SAM has already flagged `finding_catalyst_path_decoupling` in MEMORY for auto-memory promotion. Surfaced as KB candidate per spawn prompt request to give SAM/Will the explicit routing call. If routed to auto-memory, drop row; KURA Run 6 should re-propose only if a fresh Japan-macro datapoint materializes.

**KB-SAM-187 (Cross-Agent) — MOF intervention reaction-function: 4 sustained days at USDJPY 160+ without strike under Bessent-Katayama-Himino cabling-aligned posture**

```
KB-SAM-187	2026-06-09	Cross-Agent	LIVE	MOF Intervention Reaction-Function — 4d at USDJPY 160+ No-Strike Under Cabling-Aligned Posture	Empirical observation Jun 5-9 cycle: MOF did NOT strike across 4 consecutive sustained days above the USDJPY 160.00 hard #3 trigger (Fri Jun 5 tagged 160.20 intraday; Mon-Tue Jun 8-9 sustained 160.20-160.37) under a Bessent-Katayama-Himino cabling-aligned posture (Reuters Jun 1: US Treas affirms US-Japan FX coordination cabling hike + intervention combo for Jun 16). Reaction-function read: under cabling-aligned posture pre-BOJ blackout, MOF appears to tolerate level penetration when the level is USD-driven (NFP-routed) rather than yen-side disorderly, suggesting the reaction-function gates not just on level but also on (a) driver (USD-side macro vs yen-side flow), (b) cabling posture (whether intervention is being telegraphed in combination with BOJ action), (c) blackout proximity (pre-blackout intervention risks BOJ communications interference). Distinguishes from Apr 30 + May 6 strikes which fired on yen-side disorderly tape under acute pre-MOF-blackout pressure. Pairs with KB-040 (intervention paradox baseline ~0.20 unwind|fires per CH-003) and KB-184 (measurement scope) for forward intervention-probability reads.	B2	STATUS § INTERVENTION STATUS Sat Jun 6 + Tue Jun 9 evals; TIMELINE Jun 5-6 + Jun 8-9 RESOLVED blocks; KB-040 intervention paradox; KB-170 named-op #1+#2; KB-184 measurement scope; Reuters Jun 1 Bessent-Katayama-Himino cabling alignment	Cf. KB-040 (intervention paradox), KB-170 (Apr 30 + May 6 named ops), KB-182 (Bessent-Katayama affirmation), KB-184 (measurement scope). Reaction-function asymmetry observation — durable structural mechanism fact about how MOF gates intervention decisions under different posture/driver/blackout conditions. NOT a calibration lesson, NOT cross-agent transferable (Japan-specific MOF reaction-function); falls cleanly under Cross-Agent category (Channel 3 mechanism). Forward-relevant: if MOF strikes after Jun 16 BOJ resolves (post-blackout), confirms blackout-gating sub-claim; if MOF strikes before Jun 16, falsifies blackout-gating + cabling-posture sub-claims. Category: Cross-Agent (Channel 3 mechanism — same as KB-040, KB-170, KB-182).
```

**Rationale:** 4 consecutive sustained days above the hard #3 trigger without strike, under a publicly-cabled US-Japan coordination posture, is a durable empirical mechanism observation that refines the MOF intervention reaction-function beyond simple level-tagging. The reaction-function asymmetry (cabling-aligned + USD-driven + pre-blackout → tolerate; yen-side disorderly + acute pressure → strike) is the kind of durable structural fact the KB exists to record — anyone looking up "did MOF strike at the next 160 print" in future will want this reference data. Gate test: Durable ✅ (mechanism observation, not telemetry) / Reference-grade ✅ (named conditions + falsifiable forward predictions) / Not in KB ✅ (KB-040/170/182/184 cover surrounding facts but not this reaction-function asymmetry observation) / Not tsv-territory ✅ (interpretation, not auto-pulled feed) / Thesis-relevant ✅ (Channel 3 reaction-function feeds SAM-23 mark + forward intervention-probability reads). Conservative B2 — observation made in real-time, falsifiable forward sub-claims (blackout-gating, cabling-posture-gating) not yet tested. Category Cross-Agent (clusters with KB-040/170/182 Channel 3 mechanism rows). **CLEAR PROMOTE candidate per spec — gold-standard mechanism + durable provenance hierarchy with falsifiable forward implications.**

**[Run-5 RESOLUTION 2026-06-09 PM]:** KB-187 DECLINED same-day (premise-fail — 2 distinct USDJPY tags with Mon dip between, not 4 sustained days). Re-form gate set for post-Jun-16 with corrected framing. **See Run-6 KB-SAM-196 for the corrected-framing successor (post-BOJ 48h+ no-strike at USDJPY 161+ under cabling-aligned posture).**

---

### Run 6 — 2026-06-19 (Fri AM, propose-only, post-BOJ + post-FOMC + Iran-deal triple cluster)

Next free ID after SAM hand-adds Jun 10-15: max in KB.tsv = KB-SAM-194 → Run-6 adds start at **KB-SAM-195**.

**KB-SAM-195 (Cross-Agent) — Fed Chair = WARSH since 2026-05-22; debut FOMC Jun 17 statement-gutting hawkish**

```
KB-SAM-195	2026-05-22	Cross-Agent	LIVE	Fed Chair = Warsh since May 22 2026 — statement-gutting hawkish frame	Kevin Warsh confirmed Fed Chair since 2026-05-22 (debut FOMC Jun 17). Style: gutted FOMC statement ~300→~130 words, removed forward easing bias ("extent and timing of additional adjustments," balance-of-risks language); added Middle East uncertainty + supply-shock inflation framing + "the Committee will deliver price stability." Refused to dot himself at presser ("forward guidance not well suited for the current policy conjuncture"). On 2% target: "I see no reason, until we have reestablished our commitment and ability to deliver on the 2% inflation objective, to revisit that." No FX / coordination language. Powell-era cut-pricing dynamics no longer apply.	A1	fed.gov FOMC statement Jun 17 2026 + SEP / Reuters + Yahoo Finance Warsh presser coverage / Bloomberg Jun 17 / CNBC redline	Chair change sat un-modeled in SAM's docs for ~4wk (4 boot cycles) before Will-directed Jun-18 news sweep surfaced it. Boot-sweep-gap process lesson already promoted to auto-memory `[[finding_boot_sweep_macro_regime_context]]` (Jun 18 CHANGELOG). Cf. KB-006 (HANS Fed-cut path — now SUPERSEDED, see Run-6 palimpsest list). Forward implication: Pillar 1 directional vector now requires walk-back of Warsh framing, not just data-dependent Powell-style easing. v1.6 anchor.
```

**Rationale:** Macro-regime fact that anchors the Fed-side of Pillar 1 and the entire secondary path. Gate test: Durable ✅ (Chair tenure) / Reference-grade ✅ (named regime change with stylistic discriminator) / Not in KB ✅ (no Fed-Chair row exists; KB-006 anchored Powell-era dynamics implicitly) / Not tsv-territory ✅ / Thesis-relevant ✅ (Pillar 1 directional vector + Fed-cut anchor #4). A1 — fed.gov primary + multi-source verification. Category: Cross-Agent (clusters with KB-152, KB-161, KB-162 macro-regime/policy rows). **CLEAR PROMOTE.**

**KB-SAM-196 (Cross-Agent) — FOMC Jun 17 SEP: 2026 median dot +40bp (3.4→3.8), 9-of-18 see ≥1 hike; rate-differential RE-WIDENING post Jun 16-17**

```
KB-SAM-196	2026-06-17	Cross-Agent	LIVE	FOMC Jun 17 — Median 2026 Dot +40bp; Rate-Differential RE-WIDENING (Pillar 1 directional vector inverted)	FOMC Jun 17 held 3.50-3.75% unanimous 12-0 (April's 4 dissenters dropped because easing language removed). SEP was the move: 2026 median dot 3.4%→3.8% (+40bp, implies ≥1 hike); distribution 9 of 18 hike (6 see two), 8 hold, 1 cut. Core PCE 2026 +60bp to 3.3%; headline +90bp to 3.6%; 17 of 18 see inflation risks to upside. 2027 median 3.6%; long-run ~3.1% modestly up. U/E cut to 4.3%. Net Jun 16-17 sequence: BOJ +25bp compression < Fed-dot +40bp re-widening — rate-differential is now WIDER than pre-Jun-16, not narrower. CME FedWatch July hike ~75%; Polymarket "Fed hike 2026" ~52% → ~56%. Market: DXY ~100.40 (broke 100), 2Y +16bp to 4.216%, 10Y +6bp to 4.49%, 30Y bear flattener up; USDJPY 160.78 Wed close → 161.34 Thu.	A1	fed.gov SEP / CNBC redline / Reuters + Yahoo (Warsh presser) / Bloomberg "Markets Alert for Japan Intervention" Wed Jun 17 / FXStreet (DXY) / investingLive (USDJPY) / Polymarket	Pairs with KB-195 (Warsh regime). Pillar 1 STRUCTURAL-LEVEL argument survives ("the level of the gap is the carry"); DIRECTIONAL VECTOR broken. THESIS v1.5.1 § Pillar 1 [2026-06-18 fact update] paragraph encodes this; this row is the durable point-in-time SEP fact. v1.6 splits Pillar 1 into level (alive) vs vector (broken). Falsification gate: walk-back of the Jun-17 dot revision in subsequent SEPs (Sep / Dec 2026).
```

**Rationale:** Load-bearing thesis-pillar inversion fact, primary-source documented, durable point-in-time SEP record. Gate test: all 5 pass. A1. Category: Cross-Agent. **CLEAR PROMOTE.**

**KB-SAM-197 (Cross-Agent) — Iran/US deal SIGNED Jun 17 — electronic (Al Jazeera), NOT Geneva ceremony; signing-binary resolved, verification leg OPEN**

```
KB-SAM-197	2026-06-17	Cross-Agent	LIVE	Iran/US Deal SIGNED Jun 17 — Electronic (Al Jazeera) Initial Agreement; Verification Leg OPEN	Pezeshkian + Trump signed Iran/US deal Wed Jun 17 ELECTRONICALLY per Al Jazeera (primary-source — NOT a Geneva/Switzerland ceremony; corrected at Step 1.5 HAWK reconcile). Per CNN this is an INITIAL agreement — "tougher talks lie ahead" on verification. Pakistan PM Sharif confirmed "enters force immediately." Terms: 60-day toll-free Hormuz reopen THEN Oman-administered fees (per NBC); US lifts naval blockade; Iran dilutes HEU; sanctions WAIVED (not terminated); 60-day nuclear-negotiation window. Hormuz reopening PROCESS BEGUN Day 110 (Thu Jun 18) — initial traffic resuming (4 supertankers transiting incl. first Saudi-owned vessels since Day 1; backlog "weeks to clear"). Verification leg OPEN: demining, insurance restoration, traffic normalization, Oman fee-administration after 60-day window (closes ~Aug 16), HEU dilution compliance, sanctions-waiver rollout. Iran-docket UNFROZEN on signing-binary per Will instruction; implementation watch active (not formally closed).	A1	Al Jazeera (electronic-signing confirmation) / CNN (initial-agreement / tougher-talks) / NBC (toll-free-then-Oman) / NPR / CNBC / Rigzone (Hormuz traffic) / Step 1.5 HAWK-Iran reconcile (SAM CHANGELOG 2026-06-18)	Resolves the Channel 3 MOU-break (KB-170 paths + STATUS Jun 1 IRAN MOU BROKEN entry). Signing-binary cleared the Jun-12 framework caveat ("digital MOU / Iran confirmed / Geneva ceremony — not hardened until primary-source"). Step 1.5 calibration: PROME sampled CALENDAR L51 only and read first-pass as clean; SAM's comprehensive `grep -nE "Switzerland|signing ceremony|4 supertankers|physically reopening|enters force"` audit caught 10 spots incl. load-bearing L104. PROME named comprehensive-grep as correct standard. Cross-agent calibration lesson routed to auto-memory candidate (see Run-6 escalations). Pairs with KB-040 (intervention paradox), KB-051 (Brent $120 Kharg path — now SUPERSEDED-pending), KB-170 (MOF #1+#2).
```

**Rationale:** Resolves a 6mo open Channel 3 binary. A1 with multi-source primary + Step 1.5 reconcile already documented in CHANGELOG. Category: Cross-Agent. **CLEAR PROMOTE.**

**KB-SAM-198 (Energy) — IEA glut warning: +8 mbpd supply by 2027 vs +2 demand; durable bearish-oil regime independent of ME**

```
KB-SAM-198	2026-06-18	Energy	LIVE	IEA Glut Warning Jun 2026 — Bearish-Oil Regime +8 mbpd Supply / +2 mbpd Demand by 2027	IEA Jun 2026 glut warning quantifies durable bearish-oil structural regime developing independent of Middle East dynamics: +8 mbpd supply growth by 2027 vs +2 mbpd demand growth — net +6 mbpd surplus. Brent $79.68 Thu Jun 18 reaction split half deal-signing (KB-197) half IEA glut. Implication: oil-in-yen Phase 2 recession-bid path now has a non-geopolitical structural underpinning; even if Iran verification leg sticks and de-escalation reverses, the supply-side glut dampens the Brent-spike path to USDJPY upside. Pairs with KB-187 (Japan ~205d reserve cover) as the supply-side companion fact.	A2	IEA Jun 2026 monthly Oil Market Report (via Will-directed Brent sweep Jun 18); Brent $79.68 Thu confirms market read	Category Energy (with KB-001-022 oil-shock cluster, KB-187/188/189/190 Japan-oil cluster). Forward implication for THESIS v1.6: oil-in-yen Phase 1 inversion (KB-176) reinforced — even post-deal, supply glut suppresses crude-import-bill recovery; trade-balance recovery path muted. Falsification gate: IEA Sep/Dec OMR revisions tightening the surplus.
```

**Rationale:** Durable structural energy-supply regime fact, primary-source (IEA OMR), pairs cleanly with the Japan oil-reserves cluster. Gate test: all 5 pass. Category: Energy. A2 (single primary source, no cross-source check yet). **PROMOTE.**

**KB-SAM-199 (Cross-Agent) — MOF reaction-function decay: 48h+ no strike at USDJPY 161.34 post-BOJ-hike (Bloomberg intervention-alert Wed)**

```
KB-SAM-199	2026-06-18	Cross-Agent	LIVE	MOF Reaction-Function Decay — 48h+ No Strike at USDJPY 161+ Post-BOJ-Hike Under Cabling-Aligned Posture	Empirical observation Wed-Thu Jun 17-18: USDJPY ran 160.78 (Wed close) → 161.34 (Thu boot) with 48h+ no MOF strike, despite Bloomberg's "Markets Alert for Japan Intervention" Wed Jun 17. Cabling-aligned posture (Bessent-Katayama-Himino alignment publicly affirmed Jun 1) intact; pre-event blackout cleared. The corrected-framing successor to KURA Run-5's declined KB-187 (4-days-at-160 premise-fail). Refines KB-040 intervention paradox baseline and KB-184 measurement-scope under the reaction-function: under cabling-aligned posture + USD-driven tape (FOMC-routed +40bp dot move) + post-major-catalyst (BOJ +25 just delivered) + no statement crossing "decisive action" language from Katayama Jun 17-18 → MOF tolerates 161+ for >48h. Distinguishes from Apr 30 + May 6 strikes which fired on yen-side disorderly tape under acute pre-BOJ-blackout pressure (KB-170).	A2	STATUS § FOMC JUN 17 RESOLVED + § BOJ JUN 16 RESOLVED blocks; Bloomberg "Markets Alert for Japan Intervention" Wed Jun 17; USDJPY 160.78 Wed → 161.34 Thu boot.py; CHANGELOG 2026-06-18 propagation entry	Pairs with KB-040 (intervention paradox baseline ~0.20 unwind|fires), KB-170 (named-op #1+#2 Apr 30 + May 6), KB-184 (measurement scope), KB-182 (Bessent-Katayama cabling affirmation). Forward-relevant: feeds the post-BOJ MOF-#3 scenario-weighted anchor in v1.6 EV-table (Run-6 KB-SAM-200 DRAFT). Falsification gates: (i) MOF strikes pre-Jun 30 at 161+ → cabling-decay sub-claim invalidated; (ii) Katayama "decisive action" language surfaces without strike → posture-decay refined; (iii) USDJPY falls back below 160 → row scope contracts to "post-hike + cabling + USD-driven" reaction-function only. Category Cross-Agent (Channel 3 mechanism cluster).
```

**Rationale:** Corrected-framing successor to Run-5 declined KB-187, premise now solid (48h, post-catalyst, single-driver USD-routed). Gate test: all 5 pass. A2 — observation real-time, falsifiable sub-claims pre-registered. Category: Cross-Agent. **CLEAR PROMOTE — gold-standard mechanism observation with explicit falsification gates.**

**KB-SAM-200 (Framework) ⚠️ v1.6 DRAFT-TAGGED — Convexity-tail survival EV table (per-route P×move, modal bleed, sensitivity)**

```
KB-SAM-200	2026-06-19	Framework	LIVE	⚠️ v1.6 DRAFT INPUT — Convexity-Tail Survival EV Table (per-route P×move, modal bleed, sensitivity)	[v1.6 DRAFT context, NOT v1.5.1 fact — finalize-or-discard on v1.6 commit per Run-6 routing.] PROME-requested EV-table inputs (closes RED #1 quantitative sub-clause) per-route P×move over 60d window: BOJ hawkish-of-pricing 8%×+4% blended = +0.32%; MOF #3 sustained 10%×+2% blended = +0.20%; risk-off shock 10%×+7% = +0.70%; Fed walk-back of Jun-17 dot 5%×+5% = +0.25%; oil/MOU re-escalation 8%×+3% = +0.24%; residual positioning cascade 10%×+5% = +0.50% (CONDITIONAL on Sat Jun 20 CFTC residual-ON). GROSS sum +2.21%; overlap-discounted net gross +1.7-1.9% per CH-004. Cost side: modal bleed -1.1 to -1.2% (Warsh-hawkish + cross-pair USD-haven), stop-loss tail -0.5 to -0.6% (FXY ≤ $55.05 single-leg). Net 60d EV ≈ +0.0 to +0.3% per share — MARGINAL not strongly positive. Sensitivity: CFTC cover <60% peak → -0.50% gross → frame fails; risk-off P→15% → +0.35% → frame strengthens.	B2	THESIS_v1.6_DRAFT.md § CONVEXITY-TAIL SURVIVAL EV (PROME-requested 2026-06-19); CHANGELOG 2026-06-19 v1.6 draft entry	⚠️ v1.6 DRAFT INPUT — NOT v1.5.1 fact. Finalize-or-discard on v1.6 commit. RED challenge #1 decomposes into #1a (per-route probabilities honest?), #1b (FXY-move conditionals honest?), #1c (modal-bleed assumption honest?), #1d (60d window arbitrary?). Pre-registration: Sat Jun 20 CFTC print is load-bearing — cover <-120K kills 0.5pp gross EV → frame fails margin test → trim/close discussion; hold at -140K to -150K → frame survives; build through -153K/85% → frame strengthened (gross EV ~+3.0%, net ~+1.3%). Row should be promoted-or-discarded on v1.6 commit, not held indefinitely as DRAFT.
```

**Rationale:** PROME-requested EV-table inputs are durable as v1.6 working assumptions but explicitly NOT v1.5.1 fact per spawn-prompt routing. Surfacing as PROPOSED with explicit DRAFT tag in both Topic + Notes; SAM/Will rule on whether the workbook adopts a `LIVE-v1.6-DRAFT` Status convention or this Notes-tag pattern. Gate test: borderline on Durable (depends on v1.6 commit) — surfaced under SAM's escalation-mode discriminator (low-stakes/reversible structural; apply sane default + flag for veto per [[finding_subagent_escalation_mode_discriminator]]). Category: Framework. B2 — modeled inputs, not primary-source fact.

---

**Run-6 PALIMPSEST / SUPERSEDED PROPOSALS (SAM-side adjudication required):**

- **KB-SAM-006 (HANS Fed Cut + JPY)** → propose `Status = SUPERSEDED`. Fed-cut path FLIPPED to Fed-HIKE regime under Warsh (KB-195/196). Original row's "if Fed forced to cut faster" framing is regime-inverted. Reasoning preserved as palimpsest collapse → archive on Run 7 `full` mode.
- **KB-SAM-127 (Inflection 2 — FX Hedge Crisis)** → propose RE-GRADE to mechanism-direction-failure cluster. Modeled "BOJ surprise hike 0.75%→1.00% → USDJPY falls 10y in 2 weeks → margin calls" mechanism FIRED Jun 16 (BOJ +25bp delivered to 1.00%) but USDJPY weakened, not strengthened (modal hike-as-priced). Add cluster cross-ref: SAM-14/19/25 + KB-186 mechanism-direction-failure pattern.
- **KB-SAM-051 (Brent $120 Kharg Island Scenario)** → propose RE-GRADE pending. Iran/US deal SIGNED Jun 17 (KB-197) demotes Kharg-strike escalation path from main-path-tail to dormant. Don't archive — verification leg OPEN; tail could reactivate.
- **KB-SAM-152 (PC Cascade Q2 2026)** → propose RE-GRADE pending Q2-end (Jun 30). Q2 was named PEAK; if Q3 redemptions surface, refresh; otherwise re-grade to "Q2 peak observed."

**Run-6 DEDUP / CONSOLIDATION:**

- **KB-187/188/189/190 (Japan oil/energy cluster, SAM-added Jun 15):** four rows cover overlapping ground (reserves / exposure / grid-mix / transmission). NO MERGE — deliberately-decomposed cluster reads as designed; each row anchors a distinct sub-question.
- **KB-191/192 (SoftBank-OpenAI cluster, SAM-added Jun 15):** two rows reasonable (one exposure/credit, one Japan-transmission). NO MERGE.

**Run-6 SPOT-STALENESS (FLOW/VX):**

- **FLOW-JPN-5.02 (Carry Unwind):** spot stale Jun 4 → CFTC -114,667 → -145,818 (Jun 9 data, Jun 12 release; 81% peak); USDJPY 159.92 → 161.34; SAM-21 70 → ~90 (CH-009) → RESOLVED-CONFIRMED Jun 16; carry-unwind decomposed bucket reset post-BOJ; CARRY UNWIND BUCKETS need full re-derivation per v1.6.
- **FLOW-JPN-6.02 (USD Safe-Haven vs Yen Safe-Haven):** spot stale Jun 4 → USDJPY 161.34; Brent $79.68 (Iran deal SIGNED + IEA glut); Israel-Lebanon ceasefire context superseded by Iran-deal-SIGNED; SAM-23 72→~30 (CH-011) RESOLVED-FAILED Jun 16.
- **FLOW-JPN-3.01:** Norinchukin gate already updated Jun 10; row dated Jun 10 — current.
- **VX.tsv all rows dated 2026-05-28:** May TB (Wed Jun 18) + May National CPI (Fri Jun 19) due → next VX update window OPEN this weekend.

**Run-6 FLOW / VX UPDATES (proposed for SAM-applied refresh):**

- FLOW-JPN-5.02 → full re-derivation per v1.6 (not surgical spot fix).
- FLOW-JPN-6.02 → full re-derivation per v1.6.
- VX-SAM-11.02 trade balance → refresh after Wed Jun 18 May TB print lands in workbook.
