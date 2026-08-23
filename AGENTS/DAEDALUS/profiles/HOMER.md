# HOMER — DAEDALUS Comprehension Profile

> ⚠️ **SUPERSEDED IN PART — 2026-08-22. READ THE REVIEW FIRST, NOT THIS FILE.**
> A full Will-directed structure review ran 2026-08-22 (4-reader Mode-A fan-out). Its findings are current;
> this profile is the **2026-08-07** comprehension layer built against **61 files** (the tree is now 89) and
> its "Owner-lane flags (ranked)" section is **materially out of date** — five of its 🔴/🟠 flags have since
> CLOSED (the 94%-multifamily brief residue, the 8.9-vs-8.1 condo contradiction, the SCRATCH:27 superseded
> bands, the 3 unprocessed inbox packets, and the PR#4 mirror write-back, which HOMER closed 8/22 crediting
> the packet by name). **What still stands, re-verified 8/22:** the two L3-blocking absences (no convergence
> handle; no thesis-level kill rail anywhere under any name — AUTHOR-FROM-SCRATCH), and every DO-NOT-TOUCH
> item below.
> **Current sources:** `upgrades/HOMER_REVIEW_2026-08-22.md` (synthesis) · `..._READER_REPORTS.md` (evidence
> + coverage limits) · **`upgrades/HOMER_CARD.md` (the work queue)**.
> **DATED REWRITE TRIGGER — a banner is a warning, not a fix (`finding_banner_is_a_warning_not_a_fix`):**
> full delta-refresh owed by **2026-09-05**, or at the next HOMER touch, whichever is first. Refreshing was
> named as a deliverable in `HOMER_REVIEW_PLAN_2026-08-22.md` §6 and **was NOT done** — caught by
> `complete_check.py`'s claim walk at the same session's closeout, which is exactly the gap that check exists
> to find (PAT-101: my closeout certifies COMMITTED, not COMPLETE).

**Built:** 2026-08-07 (first profile — closes "graded twice without a profile"; Mode-A single-reader full read, 61 files) · **Grade at build:** L2 (FLEET_MAP owns it; L3 gated on ONE leg — see below, and the leg is AUTHOR-from-scratch, not extract-and-stamp) · **Class:** Market (promoted from CARL sub-agent 7/12 by git mv, Will-directed same-day, overriding CARL's wait-recommendation; lowest-risk promotion of the set — zero external consumers at promotion) · **Staleness (content-derived):** re-read when THESIS.md gets built (the L3 leg), after the next HOMER session closes the 5 passed resolver dates, or when STATUS's stamp leads this build date >21d.

## Identity in one line
The fleet's U.S. **national** housing asset-market + housing-credit-structure agent (NOT an FL specialist) — foreclosure pipeline + non-bank servicer stress, multifamily **BOTH books** (GSE and CMBS; ★-ruled primary owner of the Trepp CMBS-MF row and the GSE-vs-CMBS divergence), the **mortgage-specific rate surface** (30Y PMMS, 10Y-FRM spread, FHA-vs-Conv DQ spread — "nobody else owns it"), builders, HPI/inventory, state-level FL/TX — feeding CARL (consumer transmission; CARL retains the K-shape *interpretation*, same pattern as LABOR→CARL), REGINALD (Path C collateral), HENRY (wealth effect), + live edges to LABOR (builder→construction employment) and CREED (couriers the Trepp row, HOMER scores it).

## FL boundary vs CORAL (as actually operated)
CORAL canonical for the FL statewide headline (state foreclosure rate; statewide condo median/inventory); HOMER cites it and owns the pipeline decomposition (starts/REO/timelines/metro cuts/Miami-Dade). Locked 7/17, both sides record identically. **Lock state 8/7: one HOLDS (H1 foreclosure rate — byte-identical, strengthened by HOMER's accepted rank-vs-level correction on CORAL's row 8/3), one BROKEN** — see flags.

## File anatomy
| Cluster | Files | Notes |
|---|---|---|
| Core | `CLAUDE.md` 231 ln — scope seams + **Key Thresholds :76-121 (the strongest dimension)** + a ~26-line FL-band derivation block inside the instructions (excellent content, future THESIS/methods material — do NOT move before THESIS exists, the bands would lose their derivation) · `STATUS.md` 197/250 — 5 signal tables + **MARQUEE OPEN QUESTION :19-43 (the nearest thing to a thesis surface — genuinely strong, rewritten 7/31 when the Q2 GSE prints broke the frame, retirement stated not silently edited — but structurally undatable, a section of a rewritten file)** + labeled BOTTOM LINE · `SCRATCH.md` · `NEXUS_BRIEF.md` (the surface REGINALD/CARL/HENRY read — carries a defect, see flags) · `LESSONS.md` 7 entries Mistake→Rule→Tell (best-in-cohort form; 4 of 7 written 7/31) · `MEMORY.md` thin-by-design | LIVE 7/31 |
| Workbook (8 ledgers, best-in-cohort two-state hygiene) | `KB.tsv` **FROZEN 7/10** (parent-era; CARL_ID provenance col = a row-ID-stability CONTRACT with CARL's KB) · `KB_LIVE.tsv` 15 rows · `PIPELINE.tsv` 54 (incl. FHA/VA/Ginnie policy-instrument layer) · `MULTIFAMILY.tsv` 41 (Freddie Table-27 split) · `STATE_HSG.tsv` 59 · `BUILDER.tsv` 80 · `RATES.tsv` 11 (**opened 7/31, the ★-ruled rate surface; header self-issues a STALE-FLAG on the 10Y-FRM spread row**) · `PRICING.tsv` 20 (7/31) — ⚠️ **SCHEMA.tsv covers only 6 of 8** (no RATES/PRICING rows) | LIVE 7/31 |
| Predictions | `thesis/PREDICTIONS.tsv` — **2 rows only, but the discipline is real**: line-1 prose preamble carries the CRL-06/23 parent-retain ruling (deliberate, load-bearing — do not "fix"); HOM-01 INSTRUMENT-BLOCKED (FMHPI June print not out, **primary-verified at Freddie's own page** after a mirror-inference same day); HOM-02 carries an early-kill arm AND an explicit "THE BET AGAINST" section · `reports/2026-07-24_HOM-01-grading-sheet.md` — **pre-print frozen card whose "release delayed/missing" branch was exercised 7/31 and stopped a false CONFIRM** (PAT-053 spirit; never edit post-print) | correctly quiet |
| Ops | `board_log.tsv` 13 rows (incl. a self-issued AMENDED-SAME-SESSION correction pair — do not collapse) · `docket/CATALYSTS.tsv` 16 rows incl. 2 permanent break-flags + an ★OVERDUE row · outbox **0 sitting** (drained deliberately — see the double-false-delivery lesson) · `state_vectors/` RETIRED channel + `corrected/` retrieval hazard (a valid SV filed there is invisible to CARL's harvest globs) | mixed |

## The two L3-blocking absences (both fold into ONE build)
**No `thesis/THESIS.md`** — the thesis lives in CLAUDE "Transmission Pathways" (8 pathways, no state column) + the MARQUEE. **No convergence handle of any kind** (unlike HENRY — rich labels, no handle — HOMER has *neither*; build local scoring + the 5-pt together). **No thesis-level kill rail in ANY local form** — grep zero hits on every kill-vocabulary term. ⚠️ **The retrofit is AUTHOR-from-scratch — HOMER is the second genuine case after VULCAN, and unlike the 4-of-5 detector artifacts.** A future builder reading only the 8/7 amendment's "never author over a rail that works" caveat might wrongly hunt for an existing rail to stamp: there is none. Per-prediction invalidation is excellent and stays.

## §3 Invalidation-surface inventory (PAT-088 rows; kinds per PAT-077)
| Surface | Kind | Vintage rule | State 8/7 |
|---|---|---|---|
| PREDICTIONS.tsv Invalidation col (HOM-01/02 early-kills) | APPEND-ONLY | newest in-cell `>>` stamp | LIVE unfired, 7/31; HOM-01 instrument-blocked, HOM-02 resolver ~mid-Aug |
| HOM-02 `>> NEWLY DISCOVERED SPEC RISK` block (HUD ML 2026-08 threat to its own numerator) | APPEND-ONLY | in-cell 7/31 | **exemplary** — a documented threat to its own metric, NOT re-spec'd, successor-metric named for use only if it misses |
| 7/24 HOM-01 grading sheet | STATE (frozen pre-reg card) | "Prepared 7/24, ahead of the print" | correctly frozen; delayed-print branch exercised 7/31 |
| CLAUDE Key-Thresholds rail (incl. the DISARMED FL-YoY row w/ strikethrough + "do not treat its silence as FL-is-fine") | STATE | inline RETIRED/RE-ANCHORED markers, **no scanner-datable stamp** | LIVE, recently re-derived; carries ONE self-declared unrepaired band (GSE MF — mod-suppressible headline; interim rule "pair every GSE DQ reading with the same filing's provision direction" is what held the Q2 signal) |
| Thesis-level kill rail | — | — | 🔴 **DOES NOT EXIST — not a detector artifact** |
| MARQUEE | STATE | STATUS header | strong content, structurally undatable |
| board_log | EVENT | fires on WALTER dispatch | correctly quiet — but SIG-W-20260802-008 sits at the wire unlogged 5d |

## DO-NOT-TOUCH
1. `KB.tsv` FROZEN — never append/renumber (row-ID contract with CARL's KB; new rows → KB_LIVE). 2. `state_vectors/corrected/` retrieval hazard — never file anything under state_vectors/. 3. The struck FL-YoY threshold row + DISARM paragraph. 4. The MARQUEE's retired-frame sentence (the retraction vehicle for 3 agents carrying the old frame). 5. archive/ BUILD-VINTAGE banners (decided, recorded — no further pruning). 6. The 7/24 grading sheet post-print. 7. The AMENDED-SAME-SESSION board_log pair. 8. PREDICTIONS line-1 preamble (carries the parent-retain ruling).

## Owner-lane flags (ranked)
🔴 **Broken CORAL lock, intra-file**: STATUS:116 "Statewide = 8.9mo (Apr, CORAL-canonical)" vs STATUS:119 "8.1mo (June)" — both written 7/31, the WRONG figure on the more-read surface; CORAL formally superseded 8.9 on 8/3 (packet unprocessed). STATE_HSG.tsv is correct. One-cell fix + cite refresh. 🔴 **NEXUS_BRIEF:13 still reads "94% multifamily"** — the BANC figure the 7/31 audit corrected to 95.8% on STATUS; the residue survived *inside the audit's own fix pass*, on the cross-agent surface REGINALD reads, 7d (audit scorecard: **6 of 7 items fully fixed, this is the 1 partial**). 🔴 **Five self-registered `Next:` dates passed unworked** (Trepp 8/4 — first row under the CREED-courier arrangement · LGI 8/4 · **PMMS 8/6 — named specifically in HOMER's own 7/31 BOTTOM LINE, and it unblocks HOMER's own STALE-flagged spread row** · GSE condo 8/3 · TX auction 8/3) = **PAT-089 instance 3**; the two-clock `Next:` headers are the working detector — `ledger_staleness` reads all-green because it measures ledgers relative to a STATUS that is itself 7d old (**uniformly-idle agents are invisible to it — real blind spot, flagged for the shared-check register**). 🟠 SCRATCH:27 carries the superseded first-pass FL bands BEFORE the final ones in a boot-read file. 🟠 3 inbox packets unprocessed oldest 8/2 (CORAL's carries the owed 8.1 refresh; PROME's 8/2 dead-path ask is answerable in one line — **the regression was not in a HOMER surface**, grep-verified: only narrative hits). 🟡 SCHEMA rows for RATES/PRICING · no Reports-to/Spawnable-by header · $160B+ MF-wall re-source owed to CREED (carried provisional downstream, 7d) · Amendment-10 ack (HOMER's closeout already conforms; its own 7/31 brief-75-min-behind failure is the demonstrated instance).

## Standing strengths (do not "fix")
**The strongest retraction culture read in the fleet**: on 7/31 alone HOMER retracted its own published headline read, corrected its own multi-week framing error against its own dashboard, found its own kill-list entry had a false reason (traced to a Newsweek/Reventure citation; kill survives on other grounds; routed), and recorded a near-miss that would have falsely CONFIRMED its own open prediction — each with the generalizable rule written ("a number that confirms your own prediction never feels like it needs checking"). The judgment layer is well above the L2 grade; the gaps are structural.

## Corrections applied to the FLEET_MAP row (8/7 PM)
Row counts were LINE counts (KB_LIVE 15 not 17; board_log 13 not 14). "8 ledgers best-in-cohort hygiene" true for banners but SCHEMA covers 6 of 8. L3 wording tightened: the falsification leg is **author-from-scratch**. CRL-06/23 + promotion residue: CLEAN (both obligations honored, zero drift, both files agree; only benign provenance mentions of the CARL era).

## Open questions
Do the CORAL locks get a re-verification cadence (one drifted in 14d with no mechanism that could catch it — consumer_check --self can't see a bare 8.9→8.1)? Is the GSE-MF interim rule (band on a mod-suppressible metric = a band on measurement, not credit) promotable fleet-wide? The uniformly-idle-agent blind spot in ledger_staleness — register in CHECKS.tsv.
