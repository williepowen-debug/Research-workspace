# BRENT Architecture & Folder-Tree Audit — 2026-07-28 (Will-directed)

> 🗄 **DATED AUDIT/WORK RECORD (last content 2026-07-28; bannered 2026-08-17, self-audit F5).** Findings were routed at write time; this doc is history, not a live queue. Closure state of individual findings lives with the owning agents.

**Method:** Mode-A 3-reader fan-out (CLAUDE.md wiring · live-state surfaces · workbook/thesis/tooling) + DAEDALUS mechanical checks (ledger_staleness workbook + --trade, git-tracking, outbox ages). **Read-only throughout — BRENT went LIVE ~21:42 ET mid-audit** (consuming PROME's fighting-shape packet); all fixes route via inbox packet per AUTHORITY (permission + idle).
**Companion input:** PROME → BRENT fighting-shape packet 7/28 (`26d3d945d`, 9 items) — its 4 surface-rot minors all VERIFIED in-file here; this audit covers the structural/architecture layer PROME's queue-review did not.

---

## Verdict

**The architecture is sound; the folder tree is well-built.** Every CLAUDE.md reference resolves but one; the two-state ledger rule is executed at fleet-exemplar level (KB/VX/FLOW/TIMELINE/GROUP_MAP all dated-frozen with live-successor pointers); the 7/21 legacy sweep did its job (LAST_COMPLETION, board/, research corpus, WALTER-handoff all cleanly in `archive/`); STATUS 207/250; live surfaces (TRACKER, CATALYSTS, INCIDENTS, data/) current through 7/27-28.

The defects concentrate in **two classes**, neither of which is tree-shape:

1. **Wiring gaps** — mechanisms that exist with no protocol step that runs them (PAT-040 family, 4 instances).
2. **Derived-surface sweep failure** — the 7/27 adjudication was written into the banner/summary layer but never swept through secondary surfaces (`finding_seeded_selfsweep_secondary_surface_rot` family; the PENDING-vs-FILLED contradiction the 7/27 note *declared fixed* survives in TWO places).

Plus one instrument-level danger item that outranks everything: **thresholds.py**.

## STRUCTURAL findings (8)

| # | Finding | Evidence | Class |
|---|---|---|---|
| S1 | **thresholds.py (boot-run every session) prints the RETIRED thesis-break**: `("BZ=F","below",75.0,"risk","Brent <$75 — THESIS BREAK, squeeze failed")` vs THESIS v5.1:161 (sub-$75 = decoupling; real break = <$70 on demand collapse). Also carries the dead <$85 Phase-2-short frame ($85×3 FIRED bullish per THESIS:160), sources itself from VX.tsv (frozen 6/14), and omits the live 457-rig threshold. **n=2 of script-restates-registry** (REGINALD thresholds.py = n=1) → strengthens the blueprint THRESHOLDS.tsv queue item: scripts READ the registry, never restate it. | scripts/thresholds.py:7,~72 vs thesis/THESIS.md:155-171 | registry-restatement + guard-fires-wrong-direction |
| S2 | **cot_grade.py installed-but-unwired** — no boot/closeout step invokes it; event-driven Friday-COT grader with a live recurring use (COT grades stack THIS Friday 7/31 per PROME item 1). | grep cot_grade CLAUDE.md → 0 | PAT-040 |
| S3 | **No general-inbox boot step** (PROME item 6 confirmed at protocol level): CLAUDE.md:57 "do NOT process inbox on normal spawns"; boot covers WALTER lane + MSG-v1 only; explicit "do not generalize" at :170. 16 packets sat 7/22→7/28. | CLAUDE.md:24-41,57,168-183 | protocol hole |
| S4 | **PENDING resolve-or-reaffirm guard prose-only** (PROME item 7 confirmed): zero hits in CLAUDE.md; lives only in TRADE.md:115 + SCRATCH.md:66 — the surfaces that rotted. | grep PENDING CLAUDE.md → 0 | mechanize-the-cap |
| S5 | **TRADE.md:3 header asserts "pending fill"** while EXECUTION LOG :141 says FILLED 7/24 — the canonical trade surface's header states a false position state, 4d. Same contradiction survives at NEXUS_BRIEF.md:61. | TRADE.md:3 vs :141; NEXUS_BRIEF.md:61 vs :6 | stamp-reads-current |
| S6 | **STATUS.md:24 vestigial `Last Updated: 2026-07-08`** — the file's ONLY "Last Updated" string; any grep/staleness tool reads the whole file as 7/08 (true newest content 7/27). No PAT-044 two-clock header on STATUS/TRADE/NEXUS_BRIEF. | STATUS.md:24 vs :3,:94 | false-staleness trap |
| S7 | **Convergence matrix (63/75, re-scored 7/23) not touched at the 7/27 closeout** despite the −10.5% round-trip: CPC row :152 pre-dates its own banner's fired gate + 7/27 resumption; Storage row :144 (20.04M wk-1-of-2) contradicts dashboard :105 (19.37M FAILED) in the same file. | STATUS.md:144,:152 vs :3,:105 | derived-surface sweep |
| S8 | **NEXUS_BRIEF "As of 7/27" certifies a partly 7/23-vintage body** — SENDING rows cite pre-collapse $92 tape; every WAITING-FOR "Expected by" is past unresolved; :61 pending-fill contradiction (S5). Will/NEXUS-facing. | NEXUS_BRIEF.md:9 vs :40-63 | completion-stamp-skip |

## MINOR findings (12)

1. `domain/sources/` dead archive target (CLAUDE.md:104) — dir doesn't exist.
2. `refiner_ratios.py` unwired (plausibly one-shot; mark it so in BUILD_PLAN or wire it).
3. MSG-v1 validate invocation bare-relative (CLAUDE.md:172-174), prose-guarded only; `msg.py receipt` has no invocation form — same class step 5a was cwd-proofed against 7/01. FASTOW.md:39 also bare.
4. CLAUDE.md KEY THRESHOLDS vs THESIS KEY THRESHOLDS: row SETS diverged (no numeric contradiction; CLAUDE's >$120/Phase-2 row closest to contradicting v5.0 framing; neither table declares precedence).
5. CLAUDE.md:124 hardcoded share counts duplicate TRADE.md's canonical table (agrees today; drift-prone).
6. Duplicate step number 6 (WALTER intake :36 vs EXECUTE :43).
7. PREDICTIONS.tsv:2 "As of 2026-07-06" behind its own Jul-23 note lines; 7-vs-6 OPEN count mismatch vs STATUS:157; BRT-26 + COT-7/21 genuinely ungraded (self-flagged; PROME item 1 clock).
8. Catalyst-calendar past rows unstruck in STATUS:188-190 AND TRADE:155-157 (presentation rot; 7/22 EIA is elsewhere ✅).
9. `workbook/SCHEMA.tsv` unbannered (defines the schema of a ledger frozen 7/1) — silent middle.
10. `workbook/GROUP_MAP.tsv` banner self-declares a pending delete ("retained until KB migration formally closed, then delete") — closeout never executed.
11. `scripts/BUILD_PLAN.md` 3 months stale ("PHASE 1 IN PROGRESS", 4/16); zero mentions of cot_grade/predictions_due/refiner_ratios.
12. FASTOW sub-agent dormant 51d (last run 6/07) with no dormancy note — BRENT maintains the docket directly (well), but spec/memory sit in the silent middle. Also: PREDICTIONS_ARCHIVE ~6wks behind closed preds; ANALOGS.md no vintage header.

## Outbox wiring gap (new, DAEDALUS-found)

CLAUDE.md:63 defines `outbox/delivered/` ("marked delivered manually — HERMES retired") but **no closeout step walks it**. 11 packets 7/8→7/27 sit top-level with their loops demonstrably closed (LIQUID replied 7/23, FALCON 7/23, TERRY delivered 7/26, PROME fill-outcome 7/25). Mirror image of S3: the state exists, no step maintains it. One closeout sub-step fixes both sides symmetrically.

## Archive candidates (folder-tree placement)

| File | Status | Effort |
|---|---|---|
| `design/JOINT_PROPOSAL_2026-05-05_brent_sections.md` | Meets all 3 retirement legs (84d, not boot-read, no live refs) | clean `git mv` |
| `PREREG_20260628_CME_reopen.md` (root) | Resolved 6/29; predates the `setups/` convention | → setups/ or archive/; 3 refs to repoint |
| `2026-07-06_teams-session.md` (root) | Session artifact at root, but LIVE-referenced (THESIS, PREDICTIONS, CHANGELOG) | repoint-required; low priority |
| `workbook/STATUS_archive_*` (10 files) | Deliberately homed, live-referenced (STATUS:24,70,75,207) | lowest priority; 4+ refs to repoint — defensible as-is |

## What is exemplary (keep; blueprint-relevant)

- KB/VX/FLOW freeze banners: dated + per-row disposition + live-successor pointers + (VX) a verified no-live-refs grep note — still the fleet FROZEN-banner model.
- PREDICTIONS.tsv calibration scoreboard (by-class anchors + PRE-FLIGHT CHECK) — best-in-fleet; the *preamble stamp* rotted, not the discipline.
- docket/CATALYSTS.tsv curation (7/28 JMMC row downgraded 🔴→🟠 on 7/27 with an authority-verification note; prune-dates on resolved rows).
- SCRATCH.md closeout handoff — best-maintained surface of the six; candidly logs its own hygiene failure + adopted guard.
- refinery_damage/INCIDENTS.tsv — live, scope-bannered, `last_verified` column.
- Safe-to-run note: boot.py chain is read-only; sole writer is refiner_ratios.py appending its own data TSV.

## L5 confirm-read verdict (the owed FLEET_MAP watch item)

**HOLD L4.** Leg 1 (fill-confirm loop closed) ✓ — FILLED 7/24 in EXECUTION LOG + PROME 7/25 fill packet. Leg 2 (one closeout cycle with zero operator-caught surface errors) ✗ — the 7/27 closeout left TRADE header, convergence matrix, NEXUS_BRIEF body, and catalyst strikethroughs unswept, and the PENDING contradiction its own note declared fixed survives in two places. New L5 condition: one closeout cycle whose derived surfaces all agree with the banner layer (S5-S8 clean) + thresholds.py repointed (S1) + the three wiring steps landed (S2-S4 + outbox).

## Routing

- Findings packet → `AGENTS/BRENT/inbox/2026-07-28_from-DAEDALUS_architecture-audit-findings.md` (carve-out ①). Scoped to NOT duplicate PROME's 9 items — cross-referenced where they overlap (S3↔item 6, S4↔item 7, S5/S7 partial↔item 8).
- FLEET_MAP row updated (L4 HOLD, L5 condition re-cut); FLEET_DIRECTORY regenerated.
- profiles/BRENT.md REFRESHED to 7/28 vintage (Δ-banner cleared; was priority #3).
- Blueprint queue: THRESHOLDS.tsv registry item now n=2 (REGINALD + BRENT thresholds.py).

*Reader evidence preserved verbatim in this doc's source tasks; readers were read-only, delivered-before-idle.*

---

## Addendum — same-night uptake (verified in-file 7/28 ~22:00, commit `a9b241f49`)

BRENT consumed the packet 21:46 (one minute after its inbox drain) and landed the critical fixes same-session. **DAEDALUS verified each at the target artifact:**

1. **S1 FIXED + severity UPGRADED from latent to FIRED-LIVE:** thresholds.py repointed to `THESIS § KEY THRESHOLDS` canonical-wins (header names the frozen-VX defect); retired lines re-classified w/ failure documented in place. BRENT demonstrated the danger was NOT latent — Brent opened **$84.95** (session low, below the $85 line): a morning boot would have printed "squeeze weakening, front-running peace" the day the pause broke. **And BRENT found a THIRD defect my spot-check missed** — `<$100 = "physical squeeze resolving"` — wrong twice (infers physical tightness from flat price = inversion of the v5.1 central finding; unconditionally true so it fired EVERY boot = alert fatigue). **Own miss owned → PAT-070**: audit an alert surface by evaluating it against the live tape, not by diffing constants; the firing set is the evidence.
2. **S5 FIXED in all three homes** (TRADE:3 header, TRADE:120 narrative, NEXUS_BRIEF:61) with in-place failure notes — BRENT's own framing is exactly right: "a declared-fixed defect that is only partly fixed is worse than an open one, because the declaration is what stops anyone looking." Bonus: TRADE header now carries the **PAT-044 two-clock header** (W4 recommendation, adopted unprompted).
3. **Still owed (BRENT's own list, matches mine):** cot_grade wiring (Fri clock) · outbox delivered/-step · STATUS:24 vestigial stamp · matrix sweep · NEXUS_BRIEF body re-vintage — all closeout-shaped; the re-cut L5 condition grades on exactly such a closeout.

Fastest packet→fix cycle on record for a domain agent (~15 min from delivery to verified commit), with source-verification of my claims before accepting them — correct counterparty rigor both directions.
