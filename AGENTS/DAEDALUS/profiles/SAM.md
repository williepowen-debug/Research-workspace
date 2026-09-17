<!-- INSTALLED 2026-09-17 by DAEDALUS (PR#6 profile-refresh queue, resolve_by 9/15 passed). Mode-A: reader draft + independent locator verification (evidence: profiles/REFRESH_2026-09-17_VERIFY_P3_SAM_SHADE.md — verification table, totals, missed-🔴 list). Prior body (vintage from the old header) preserved verbatim at profiles/_prior/SAM_PRIOR_2026-09-17.md. -->
# Agent Profile — SAM

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P3 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** solo full-core read (P3 reader) + independent second-reader locator verification (every path:line below opened twice, by two readers).
**Sources read:** `CLAUDE.md` · `STATUS.md` · `STATUS_REFERENCE.md` · `MEMORY.md` · `thesis/THESIS.md` (header + section map) · `thesis/PREDICTIONS.tsv` (preamble + all 34 data rows) · `TRADE.md` · `STRATEGY.md` · `NEXUS_BRIEF.md` · `red/{COUNTER_THESIS,CHALLENGES,LOG}.md` · `docket/{CALENDAR.md,CATALYSTS.tsv,2026-09-18_SAM28_SAM31_REVIEW.md}` · `workbook/LEDGER_CADENCE.md` + ledger listing · `scripts/boot.py` + `scripts/lib/boot_context.py` · `insurers/TRACKER.md` · `MAINTENANCE.md` · `RECONCILIATION.md` · `SIGNAL_INTAKE.md` · `MOF_INTERVENTION_PLAYBOOK.md` · `board_log.tsv` · sub-agent pair-files
**Staleness:** 45-day clock from the Profile vintage above (refresh at ≥45 days) OR earlier when ANY ONE of these fires — (a) `AGENTS/SAM/thesis/THESIS.md:1` no longer reads `# SAM THESIS — v1.7`; (b) `AGENTS/SAM/red/CHALLENGES.md:4` `**Last RED sweep:**` advances past 2026-08-20; (c) the `Status == OPEN` set of `AGENTS/SAM/thesis/PREDICTIONS.tsv` is no longer exactly {SAM-28, SAM-31, SAM-33} (`STATUS.md:9` carries the same count); (d) hard floor **2026-11-01**.

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

### 1. Identity

Japan-side **parallel trigger** in the transmission chain — JGB/BOJ/yen/carry, able to fire independently of the US legs. **Class:** Market (`AGENTS/DAEDALUS/FLEET_MAP.tsv` SAM row, cols Class/Level/Conf). **Domain + channels:** `CLAUDE.md:3-10` — three channels (life-insurer repatriation → UST; carry unwind → VIX; BOJ policy divergence → capital flows). **Spawnable by:** PROME / Will. **Sends to** HENRY / LIQUID / PROME / BOND via WALTER routing (`CLAUDE.md:190-205`); **receives from** LIQUID, HAWK, HENRY, BRENT, PROME (`CLAUDE.md:207-212`).

One line: *the desk that answers "is Japan about to transmit stress to the US, and can I prove it with a primary?"* — currently answering **no live frame, book FLAT, no successor declared** (`STATUS.md:5`, `thesis/THESIS.md:1-6`).

**What actually distinguishes it:** the fleet's densest prediction-resolution machinery (34 scored rows; a 39-line calibration preamble that is a versioned scoreboard chain) and a three-sub-agent internal staff (KOYOMI · METSUKE · KURA), all three still live in 2026-09.

### 2. File anatomy (where the richness lives)

818 tracked files (`git ls-files AGENTS/SAM/ | wc -l`). Cluster mass, measured: **`research/` 312 · `inbox/` 218 · `archive/` 74 · `evals/` 47 · `workbook/` 32 · `scripts/` 28 · `reports/` 25 · root 22 · `thesis/` 18 · `outbox/` 14 · `docket/` 9 · `insurers/` 8 · `red/` 5.**

| Cluster | Files (anchor) | Bytes / state | Richness |
|---|---|---|---|
| **Charter** | `CLAUDE.md` (294 ln) | 37,570 B | 10-step boot + WALTER intake §`CLAUDE.md:52-65` + the **doc-ownership FILES matrix `:235-277`** + a hand-written **MANUAL-ONLY script exception list** `:269` that exists so `boot.py --tools`' drift flag stays signal |
| **Live state (HOT)** | `STATUS.md` (131 ln) | **21,720 B = 67% of the 32,550 B budget** | Signal-Status mega-lede `:3-13`, LIVE MARKET DATA `:28-52`, KEY THRESHOLDS + the WQ-162 BASIS blockquote `:65-82`, WHAT TO WATCH `:84-95`, PREDICTIONS `:116-127` |
| **Live state (WARM)** | `STATUS_REFERENCE.md` (52 ln) | 8,109 B | **New anatomy, born 2026-09-11** (`a9afd4701`): durable reference rows, CARRY UNWIND method + vintage, INTERVENTION evidence ladder, CHANNELS·BOJ·FED detail. ⛔ *current and citable, simply not boot-read* (`STATUS_REFERENCE.md:8`) |
| **Cold** | `STATUS_ARCHIVE.md` | 116,632 B | Split out 2026-09-01; header at `:3` carries the read-cap derivation. Superseded; never current |
| **Thesis** | `thesis/THESIS.md` **v1.7** | 65,371 B | `:8-32` the retirement blockquote; `:155-183` Pillar audit 1-4 (Pillar 4 ⚰️ BROKEN); `:190-212` Channels 1-4 (Ch1 RETIRED, Ch4 DEAD); `:221-237` § WHAT REPLACES IT (two owned questions); `:238-247` oil-in-yen two-phase |
| **Thesis, candidate** | `thesis/V18_CANDIDATE_PILLAR1.md` · `V20_CANDIDATE_FLOW_SETS_LEVEL.md` · `V20_CROSSREAD_2026-08-27.md` · `V20_CANDIDATE_SELF_ATTACK_SEALED.md` | 13/17/8/2 KB | **v1.8 is a separate document, not a thesis** (`STATUS.md:11`); **v2.0 KILLED 8/20-27** (`STATUS.md:5`) |
| **Calibration** | `thesis/PREDICTIONS.tsv` | 89,614 B · **34 data rows** · 9-col schema (`Pred_ID…Notes`, header at `:40`) | **39-line `#`-comment preamble (`:1-39`)** = a versioned scoreboard chain + the count-correction guard `:2` + HIGH-CONFIDENCE FAILURES `:20-30` + CLOSED-AS-RESOLVED-SPECIAL `:31`. **The asset.** `PREDICTIONS_ARCHIVE.md` holds `#sam-NN` post-mortems |
| **Pre-registrations** | `thesis/{BOJ_2026-07-31,CURVE_ATTRIBUTION_2026-08-17,INTERVENTION_CHARACTER_2026-08-03}_PREREGISTRATION.md`, `REPENCIL_2026-08-07_PREPRINT.md`, `AUCTION_GRADING_RULING_2026-09-11.md` | 21/31/7/13/10 KB | Frozen-before-the-print documents; STATUS `:108-114` keeps named redirects because **external consumers cite them by name** |
| **Audit trail** | `thesis/CHANGELOG.md` | **208,580 B** | Every version bump with old→new view. Never a boot read |
| **Timeline** | `thesis/timeline/TIMELINE.md` (+ `ARCHIVE.md` 52,062 B) | **104,615 B** (`CLAUDE.md:25` still says 96 KB — stale) | Boot reads **last two dated blocks only**; whole-file read is impossible, not merely wasteful |
| **Research outputs** | `research/outputs/` (308 files) + `research/inputs/` | — | **The largest cluster in the tree.** Per-run artifact sets (`manifest.json` · `review-draft.json` · `source.html` · `table.png`) plus dated decision memos that live docs travel to: the xccy activation decline (`CLAUDE.md:269`) and the 9/14 stale-sweep inventory + before-image (`workbook/LEDGER_CADENCE.md:3,33`) |
| **Trade (HISTORICAL)** | `TRADE.md` 50,247 B · `STRATEGY.md` 71,548 B | both ⚰️ bannered at `:3-8` | *"HISTORICAL AS OF 2026-08-07. DO NOT TRADE OFF IT."* Kept as decision record; money fields still load-bearing |
| **Playbook** | `MOF_INTERVENTION_PLAYBOOK.md` | header `:1-8`; **S1 ladder `:12`, S1-A amendment `:65`/`:67`** | KILL_MEMO-class S1/S1-A ladder; **method**, not marks |
| **Workbook** | 19 root TSVs + `LEDGER_CADENCE.md` + KURA pair-files (32 tracked files) | KB.tsv 207,971 B · MOF_FLOWS 94,513 B · KURA_MEMORY 209,222 B | 11 script-written (10 auto-pulled at `CLAUDE.md:268` + `BIS_GLI`), 4 FROZEN, 2 ARCHIVE. **`LEDGER_CADENCE.md` (3,419 B) is the desk's own two-clock declaration** — per-ledger class + latest observation + next check |
| **Instrumentation** | `scripts/` — 21 top-level `.py` + `lib/` (1) + `tests/` (4) = 26 `.py`, 28 files | `boot.py:63-77` = 13-script BOOT_SEQUENCE | `boot.py --tools` prints a **disk-generated** inventory + drift flag; **`--predictions` (`boot.py:296`, `:315-321` → `lib/boot_context.py:36-53,156-176`) parses, schema-validates and reports OPEN rows against the `docket/PREDICTION_SCHEDULE.json` sidecar**; `--orient` read-only |
| **Adversarial** | `red/{CHALLENGES,COUNTER_THESIS,LOG}.md` + `red/CLAUDE.md` | 61.5 / 25.1 / 18.2 KB | **SAM reads, never edits.** 17 keys, 3 OPEN (CH-009 · CH-012 · CH-017), 14 CLOSED (`red/LOG.md:7`) |
| **Docket** | `docket/{CALENDAR.md,CATALYSTS.tsv,RELEASES.md,KOYOMI*.md,PREDICTION_SCHEDULE.json}` + two dated review packets (9 files) | CATALYSTS 31 data rows | CALENDAR is the human twin of CATALYSTS; `2026-09-18_SAM28_SAM31_REVIEW.md` is a **frozen adjudication packet prepared 9/9** (`:1`) |
| **Ops / cross-agent** | `NEXUS_BRIEF.md` · `RECONCILIATION.md` · `insurers/` (TRACKER + 7 profiles) · `board_log.tsv` · `audits/2026-09-10_asmade-disposition.md` · `evals/` (47) · `reports/` (25, ~1/session) | — | `insurers/TRACKER.md:3` refreshed 2026-09-14 |
| **Sub-agent staff** | `docket/KOYOMI*.md` · root `METSUKE*.md` · `workbook/KURA*.md` | 3 spec+memory pairs (6 files) + 4 `*_ARCHIVE` | All three live; latest runs KOYOMI 21, METSUKE 20, KURA 16 (all 2026-09-11, `056bb0f78` / `a7fc09dbd`) |

*Key question this answers: when I grade section X, which file do I read?* → thesis structure `thesis/THESIS.md`; live numbers `STATUS.md` then `STATUS_REFERENCE.md`; **never** `TRADE.md`/`STRATEGY.md` (bannered historical); adversarial state `red/CHALLENGES.md`, never `red/COUNTER_THESIS.md` (frozen argument record); run evidence behind a verdict `research/outputs/<date>_<slug>/`.

### 3. Per-dimension local representation

| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| **Thesis structure** | `thesis/THESIS.md:8-32` (retirement blockquote), `:155-183` pillar audit, `:190-212` channel states, `:221-237` WHAT REPLACES IT | Pillars 1-4 audited individually with per-pillar verdicts; channels carry explicit lifecycle tokens (RETIRED / DEAD / monitored). The **successor FRAME is deliberately blank** (`:13-15`: *"v1.7 records the retirement honestly and leaves the successor blank"*) while § WHAT REPLACES IT `:221` decomposes it into two questions, each with a named owner | **EXCEEDS** |
| **Convergence / scoring** | `thesis/THESIS.md:55-67` (HISTORICAL conviction decomposition), `:127-142` EV table | 3-axis conviction + carry buckets (7d/30d/60d) + route-EV table. ⚠️ **All now flagged HISTORICAL**: buckets last re-penciled 2026-08-07 (`STATUS.md:57`). **No universal 5-pt handle, no Independence column** | substance present, handle absent, and the substance is frozen |
| **Invalidation / exit** | `thesis/THESIS.md:86-99` two-legged SPF · `:100-109` LOCKED Sep-18 window · `:143-154` sensitivity · `red/CHALLENGES.md` | Two-legged single-point-failure with a **pre-registered numeric invalidation line (−108K/60%)** that actually **fired 2026-08-07** and retired the frame as written. Channel-kill live with named re-add conditions | **EXCEEDS — fleet reference** |
| **Thresholds** | durable: `CLAUDE.md:216-231`; live: `STATUS.md:65-82` | **Two-surface split, exactly implemented** — charter table says "Current values live in STATUS.md" (`CLAUDE.md:218`); STATUS carries src+date on every row. 🆕 the **WQ-162 BASIS blockquote** (`STATUS.md:67`) pins series, session zone, completed-only, revision direction | **EXCEEDS** |
| **Predictions** | `thesis/PREDICTIONS.tsv` + `boot.py --predictions` | 34 rows, 9 cols, `Confidence` at registration, mark-history chains in `Notes`, WQ-112 two-vintage field form. **Scoreboard 16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN reconciles exactly against the row set** (recounted by two readers). A **schema-validating reader** derives the OPEN set mechanically (`scripts/lib/boot_context.py:36-53`) | **EXCEEDS** |
| **Cross-agent routing** | `CLAUDE.md:190-205` send table · `:207-212` receive · `NEXUS_BRIEF.md` | Send table's `Target` column **explicitly re-labelled "who must ACT, not a delivery address"** with everything routed via WALTER (`CLAUDE.md:190`) — self-caught 2026-09-03. NEXUS_BRIEF folded LAST per Amendment 10 with a STATUS commit-hash provenance line (`NEXUS_BRIEF.md:3`) | **EXCEEDS** |
| **Session handle (BOTTOM LINE)** | — | **STILL ABSENT as an end-cap.** Substance is inverted into the top mega-lede `STATUS.md:3-13`; the file ends on a one-line pointer `STATUS.md:131` | gap (handle only) |

### §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/THESIS.md:86-99` (leg-1 SPF, −108K/60%) | the carry-convexity tail → LOW | `:3` *"Current integration — September 15, 2026; v1.7 unchanged"*; `:6` retirement record dated 2026-08-07 | **FIRED 2026-08-07**, written into the version header with the contract-level arithmetic |
| `thesis/THESIS.md:100-109` (leg-2, LOCKED Sep-18 window) | same frame, second leg | same `:3` stamp | survives only as the **SAM-28 grading horizon** (`:22-24`) — explicitly demoted from an action deadline |
| `thesis/THESIS.md:190-194` Channel 1 | life-insurer repatriation channel | `:3` | **RETIRED** with a named re-add condition (direct foreign SALES at ≥2 institutions across ≥2 consecutive windows — restated `STATUS.md:103`) |
| `thesis/THESIS.md:207-212` Channel 4 | positioning-convexity channel | `:3` | ⚰️ **DEAD 2026-08-07** |
| `thesis/PREDICTIONS.tsv` (3 OPEN rows) | SAM-28 route/magnitude, SAM-31 yen-haven re-couple, SAM-33 BOJ emergency capping | preamble `# As of 2026-09-10` (line 3 of file) | per-row `Status` + `Date_Resolved`; SAM-33 carries an **activation stamp** lifting its VOID/UNTESTED clause (row Notes, 2026-08-17) |
| `STATUS.md:69-82` KEY THRESHOLDS table | live threshold state incl. retired gates | table rows carry per-row source dates; basis pinned `:67` | retired gates **written in place, never deleted** — `:71` "Retired gate remains VOID", `:80` "Fired Aug-7", `:81` "No rearm" |
| `red/CHALLENGES.md` | the whole thesis, adversarially | `:3` `Last real data refresh: 2026-08-20` · `:4` `Last RED sweep: 2026-08-20` | per-key `**Status:**` line + bright-line resolution criteria; rail state summarised `:6-10` |
| `red/COUNTER_THESIS.md` | v1.6.1 (historical) | `:3` `Last real data refresh: 2026-06-30` · `:4` `Last RED sweep: 2026-08-17` | ⚠️ **banner at `:6-7` declares it a frozen record, cite as history** — per-argument standing table `:9-14` |
| `docket/2026-09-18_SAM28_SAM31_REVIEW.md:1-3` | the 9/18 grading of SAM-28/31 | `:1` *"prepared September 9"* | frozen rows + source SHA256; **preparation only, no grade** |
| `MOF_INTERVENTION_PLAYBOOK.md` (S1 `:12`, S1-A `:65`/`:67`) | intervention attribution | `:7` `September 8 integration` | method doc; live marks route to `STATUS.md:59-63` / `STATUS_REFERENCE.md` |

### 4. Deviations from standard (+ why)

- **Synthesis-at-TOP instead of a trailing BOTTOM LINE** (`STATUS.md:3-13`) — *equivalent in substance, debt in handle.* Fix is additive (add an end-cap; never replace the lede).
- **Hot / WARM / cold three-tier state split** (`STATUS.md` → `STATUS_REFERENCE.md` → `STATUS_ARCHIVE.md`, `STATUS_REFERENCE.md:3-8`) — *better than standard.* Distinguishes "current but not boot-read" from "superseded", which the two-state fleet rule does not.
- **Charter carries a hand-written MANUAL-ONLY script list** (`CLAUDE.md:269`) while forbidding a hand-written script inventory (`CLAUDE.md:270`) — *deliberate and correct:* the list exists so the generated drift flag stays signal, and its own count defect was self-corrected 2026-08-27 in-row.
- **Ledger two-clock declaration is a separate owned doc** (`workbook/LEDGER_CADENCE.md`) rather than per-file banners — *better;* it names class, latest observation and next check per ledger, which the fleet rule's banner form cannot.
- **An internal sub-agent staff of three with pair-file memories** (KOYOMI/METSUKE/KURA) plus two purpose-built rollers (`scripts/subagent_memory_roll.py`, `scripts/kura_proposal_roll.py`) — *better;* no other market desk has this, and the second roller's first run measured **179K → 50K with zero proposal IDs lost** (`CLAUDE.md:269`).
- **A dated run-artifact lane (`research/outputs/`, 308 files)** that live docs cite by path — *better than standard,* and the reason STATUS can stay at 67% of budget: the session delta goes to a dated run directory, STATUS carries the verdict.
- **`red/` is a rail SAM is contractually forbidden to edit** (`CLAUDE.md:261`) — *better in design, debt in operation:* it can only be refreshed by a RED spawn SAM cannot perform, so its staleness is not SAM's to fix (see flags).

### 5. Load-bearing context / DO NOT TOUCH

1. **Money fields.** Avg cost `$58.32` is Will's ground truth (`TRADE.md:72`); FLAT/0 shares Will-confirmed 2026-06-29 (`TRADE.md:51`). METSUKE is **forbidden to edit** them and told that even flagging them is risky (`METSUKE.md:74`).
2. **`thesis/PREDICTIONS.tsv` preamble** (`:1-39`) — the versioned scoreboard chain, the count-correction guard `:2`, the HIGH-CONFIDENCE FAILURES block `:20-30` and the CLOSED-AS-RESOLVED-SPECIAL block `:31`. The calibration record *is* the asset; never compact it.
3. **Retired gates are written in place, never deleted** — `USDJPY 160` VOID (`STATUS.md:71`), `−108K/60%` "Fired Aug-7" (`:80`), `−140K/−153K` "No rearm" (`:81`). Deleting a fired gate destroys the resolution record.
4. **R = −188,077, not −180,000.** The `25.3% of −180K` form is RETIRED (`STATUS.md:7`, Will-ratified 8/11) and `MEMORY.md` DO-NOT list repeats it. Percentage labels moved; **contract gates did not.**
5. **The WQ-162 USD/JPY basis** (`STATUS.md:67`) — yfinance `USDJPY=X`, London-labelled completed sessions, **as-LAST-REVISED**. Deliberately opposite in direction to LIQUID's as-first-published rule. Never blend with the BOJ 17:00 JST fix or the MOF curve.
6. **The two named STATUS redirects** (`STATUS.md:108-114`) — external consumers cite those section names (`AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` §v0.30). Do not delete without a consumer re-check.
7. **`red/`** — SAM reads, nobody edits (`CLAUDE.md:261`).
8. **Sub-agent pair-files** — cross-spawn state; the rollers close on different criteria by design (memory on a CLOSURE MARKER, proposals on PROVABLE LANDING) and **must not be merged** (`CLAUDE.md:269`).
9. **Script-owned TSVs** (`MOF_FLOWS.tsv`, `USDJPY.tsv`, `JGB_YIELDS.tsv`, …) — no hand edits; `CLAUDE.md:268` says verify against `boot.py --tools`, not against the charter list (which is itself incomplete — it omits `RATE_DIFFERENTIAL.tsv`).
10. **PROME's inbox is `PROME/inbox/`, never `AGENTS/PROME/inbox/`** (`CLAUDE.md:114`) — SAM regrew the dead tree three times; the rule now lives in the protocol.
11. **The CH-0NN citation collision** (`red/CHALLENGES.md:12`) — two RED namespaces overlap at CH-004/005/009/010/011. Always say which.

### 6. Maturity snapshot

Grades and classification live in `AGENTS/DAEDALUS/FLEET_MAP.tsv` (SAM row) — not restated here. Work queue → `upgrades/SAM_CARD.md`.

Per-dimension read from this pass: thesis **EXCEEDS** · invalidation **EXCEEDS** · thresholds **EXCEEDS** · predictions **EXCEEDS** · routing **EXCEEDS** · convergence-handle **absent and the substance frozen since 8/07** · session end-cap **absent**. Two of the FLEET_MAP L5 legs recorded on 2026-09-01 are now stale in SAM's favour and need re-cutting (PART B flags R1/R2).

### 7. Open questions / comprehension gaps

1. **Who refreshes `red/`?** The rail is 28 days past its last sweep and its named 9/3 adjudicator has passed. SAM cannot self-serve it. Whether that is a SAM gap, a RED-spawn-scheduling gap, or a PROME gap is **NOT-ADJUDICATED** from inside SAM's tree.
2. **Is the convergence handle worth building at all** on a desk with no live frame? The conviction decomposition is honestly bannered HISTORICAL; a 5-pt matrix over a retired frame could be worse than nothing.
3. ~~`boot.py --predictions` vs the eyeball scan~~ — **SETTLED 2026-09-17 by reading the code.** The instrument exists and is wired; `CLAUDE.md:27`'s "NO INSTRUMENT" line is stale. Now owner flag **S7**, not an open question.
4. **`SIGNAL_INTAKE.md` disposition** — MEMORY lists "SIGNAL_INTAKE archive" as DEFERRED (`MEMORY.md:89`); the file's own banner is itself stale (flag S3). Archive-or-refresh is an owner call.
5. **Do the 7 `insurers/` profiles still earn their place** now that Channel 1 is RETIRED? TRACKER was refreshed 2026-09-14, so presumably yes, but the link from a retired channel to a maintained tracker is written down nowhere I found.
6. **Is `research/outputs/` (308 files, 38% of the tree) under any retirement discipline?** Dated run directories accrete; the >60d fleet rule would reach most of them, and nothing in the charter scopes them in or out. **NOT-ADJUDICATED.**

---
---
