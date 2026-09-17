# PROFILE REFRESH DRAFTS — READER P3 — SAM · SHADE
**Reader draft, 2026-09-17 (Thu). Read-only pass. DAEDALUS re-verification pending before any of PART A becomes `profiles/<DESK>.md`.**

Review period 2026-09-01 00:00 → 2026-09-17. Repo root `/home/willi/Research-workspace`; all path:line locators are at HEAD unless a commit hash is given.
Template followed: `AGENTS/DAEDALUS/profiles/_TEMPLATE.md:1-53`.

Vocabulary per the common brief: **TRUE-STILL / REFUTED / CANNOT-EVALUATE / NOT-SEEN / NOT-ADJUDICATED**.

---
---

# ═══ DESK 1 of 2 — SAM ═══

# PART A — REFRESHED PROFILE (draft, ready to become `profiles/SAM.md`)

# Agent Profile — SAM

**Profile vintage:** 2026-09-17 (reader draft, DAEDALUS re-verification pending)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** solo full-core read (P3 reader, fan-out leg)
**Sources read:** `CLAUDE.md` · `STATUS.md` · `STATUS_REFERENCE.md` · `MEMORY.md` · `thesis/THESIS.md` (header + section map) · `thesis/PREDICTIONS.tsv` (preamble + all 34 data rows) · `TRADE.md` · `STRATEGY.md` · `NEXUS_BRIEF.md` · `red/{COUNTER_THESIS,CHALLENGES,LOG}.md` · `docket/{CALENDAR.md,CATALYSTS.tsv,2026-09-18_SAM28_SAM31_REVIEW.md}` · `workbook/LEDGER_CADENCE.md` + ledger listing · `scripts/boot.py` · `insurers/TRACKER.md` · `MAINTENANCE.md` · `RECONCILIATION.md` · `SIGNAL_INTAKE.md` · `MOF_INTERVENTION_PLAYBOOK.md` · `board_log.tsv` · sub-agent pair-files
**Staleness:** refresh when **any ONE** of: (a) `AGENTS/SAM/thesis/THESIS.md:1` no longer reads `# SAM THESIS — v1.7`; (b) `AGENTS/SAM/red/CHALLENGES.md:3` `Last RED sweep:` advances past 2026-08-20; (c) `AGENTS/SAM/thesis/PREDICTIONS.tsv` OPEN set is no longer exactly {SAM-28, SAM-31, SAM-33} (`STATUS.md:9` carries the same count); (d) `git log -1 --format=%cs -- AGENTS/SAM/STATUS.md` is more than 45 days after 2026-09-17.

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

## 1. Identity

Japan-side **parallel trigger** in the transmission chain — JGB/BOJ/yen/carry, able to fire independently of the US legs. **Class:** Market (`AGENTS/DAEDALUS/FLEET_MAP.tsv` SAM row, cols Class/Level/Conf). **Domain + channels:** `CLAUDE.md:3-10` — three channels (life-insurer repatriation → UST; carry unwind → VIX; BOJ policy divergence → capital flows). **Spawnable by:** PROME / Will. **Sends to** HENRY / LIQUID / PROME / BOND via WALTER routing (`CLAUDE.md:190-205`); **receives from** LIQUID, HAWK, HENRY, BRENT, PROME (`CLAUDE.md:207-212`).

One line: *the desk that answers "is Japan about to transmit stress to the US, and can I prove it with a primary?"* — currently answering **no live frame, book FLAT, no successor declared** (`STATUS.md:5`, `thesis/THESIS.md:1-6`).

**What actually distinguishes it:** the fleet's densest prediction-resolution machinery (34 scored rows, preamble-as-calibration-warning) and a three-sub-agent internal staff (KOYOMI · METSUKE · KURA), all three still live in 2026-09.

## 2. File anatomy (where the richness lives)

818 tracked files (`git ls-files AGENTS/SAM/ | wc -l`), of which ~470 are the WALTER `inbox/WALTER/processed/` signal lane and ~90 are `archive/`.

| Cluster | Files (anchor) | Bytes / state | Richness |
|---|---|---|---|
| **Charter** | `CLAUDE.md` (294 ln) | 37,570 B | 10-step boot + WALTER intake §"WALTER signal intake" `CLAUDE.md:52-65` + doc-ownership matrix `:118-127` + a hand-written **MANUAL-ONLY script exception list** `:269` that exists so `boot.py --tools`' drift flag stays signal |
| **Live state (HOT)** | `STATUS.md` (131 ln) | **21,720 B = 67% of the 32,550 B budget** | Signal-Status mega-lede `:3-13`, LIVE MARKET DATA `:28-52`, KEY THRESHOLDS + the WQ-162 BASIS blockquote `:65-82`, WHAT TO WATCH `:84-95`, PREDICTIONS `:116-127` |
| **Live state (WARM)** | `STATUS_REFERENCE.md` (52 ln) | 8,109 B | **New anatomy, born 2026-09-11** (`a9afd4701`): durable reference rows, CARRY UNWIND method + vintage, INTERVENTION evidence ladder, CHANNELS·BOJ·FED detail. ⛔ *current and citable, simply not boot-read* (`STATUS_REFERENCE.md:8`) |
| **Cold** | `STATUS_ARCHIVE.md` | 116,632 B | Split out 2026-09-01; header at `:3` carries the read-cap derivation. Superseded; never current |
| **Thesis** | `thesis/THESIS.md` **v1.7** | 65,371 B | `:1-32` the retirement blockquote; `:155-183` Pillar audit 1-4 (Pillar 4 ⚰️ BROKEN); `:190-212` Channels 1-4 (Ch1 RETIRED, Ch4 DEAD); `:238-247` oil-in-yen two-phase |
| **Thesis, candidate** | `thesis/V18_CANDIDATE_PILLAR1.md` · `V20_CANDIDATE_FLOW_SETS_LEVEL.md` · `V20_CROSSREAD_2026-08-27.md` · `V20_CANDIDATE_SELF_ATTACK_SEALED.md` | 13/17/8/2 KB | **v1.8 is a separate document, not a thesis** (`STATUS.md:11`); **v2.0 KILLED 8/20-27** (`STATUS.md:5`) |
| **Calibration** | `thesis/PREDICTIONS.tsv` | 89,614 B · **34 data rows** · 9-col schema (`Pred_ID…Notes`) | 19-line `#`-comment preamble = a versioned scoreboard chain + HIGH-CONFIDENCE FAILURES list `:20-30`. **The asset.** `PREDICTIONS_ARCHIVE.md` holds `#sam-NN` post-mortems |
| **Pre-registrations** | `thesis/{BOJ_2026-07-31,CURVE_ATTRIBUTION_2026-08-17,INTERVENTION_CHARACTER_2026-08-03}_PREREGISTRATION.md`, `REPENCIL_2026-08-07_PREPRINT.md`, `AUCTION_GRADING_RULING_2026-09-11.md` | 21/31/7/13/10 KB | Frozen-before-the-print documents; STATUS `:108-114` keeps named redirects because **external consumers cite them by name** |
| **Audit trail** | `thesis/CHANGELOG.md` | **208,580 B** | Every version bump with old→new view. Never a boot read |
| **Timeline** | `thesis/timeline/TIMELINE.md` (+ `ARCHIVE.md`) | ~96 KB per `CLAUDE.md:25` | Boot reads **last two dated blocks only** — 176% of cap whole |
| **Trade (HISTORICAL)** | `TRADE.md` 50,247 B · `STRATEGY.md` 71,548 B | both ⚰️ bannered at `:3-8` | *"HISTORICAL AS OF 2026-08-07. DO NOT TRADE OFF IT."* Kept as decision record; money fields still load-bearing |
| **Playbook** | `MOF_INTERVENTION_PLAYBOOK.md` | `:1-8` | KILL_MEMO-class S1/S1-A ladder; **method**, not marks |
| **Workbook** | 19 root TSVs + `LEDGER_CADENCE.md` + KURA pair-files | KB.tsv 207,971 B · MOF_FLOWS 94,513 B · KURA_MEMORY 209,222 B | 11 script-written, 4 FROZEN, 2 ARCHIVE. **`LEDGER_CADENCE.md` (3,419 B) is the desk's own two-clock declaration** — per-ledger class + latest observation + next check |
| **Instrumentation** | `scripts/` — 24 py + `lib/` + `tests/` | `boot.py:63-77` = 13-script BOOT_SEQUENCE | `boot.py --tools` prints a **disk-generated** inventory + drift flag; `--predictions` derives OPEN rows; `--orient` read-only |
| **Adversarial** | `red/{CHALLENGES,COUNTER_THESIS,LOG}.md` + `red/CLAUDE.md` | 61.5 / 25.1 / 18.2 KB | **SAM reads, never edits.** 17 keys, 3 OPEN (CH-009 · CH-012 · CH-017), 14 CLOSED (`red/LOG.md:7`) |
| **Docket** | `docket/{CALENDAR.md,CATALYSTS.tsv,RELEASES.md,KOYOMI*.md,PREDICTION_SCHEDULE.json}` + two dated review packets | CATALYSTS 31 rows | CALENDAR is the human twin of CATALYSTS; `2026-09-18_SAM28_SAM31_REVIEW.md` is a **frozen adjudication packet prepared 9/9** |
| **Ops / cross-agent** | `NEXUS_BRIEF.md` · `RECONCILIATION.md` · `insurers/` (TRACKER + 7 profiles) · `board_log.tsv` · `audits/2026-09-10_asmade-disposition.md` · `evals/` · `reports/` (dated, ~1/session) | — | `insurers/TRACKER.md:3` refreshed 2026-09-14 |
| **Sub-agent staff** | `docket/KOYOMI*.md` · `METSUKE*.md` · `workbook/KURA*.md` | 6 pair-files | All three live; latest runs KOYOMI 21, METSUKE 20, KURA 16 (all 2026-09-11, `git log` `056bb0f78`/`a7fc09dbd`) |

*Key question this answers: when I grade section X, which file do I read?* → thesis structure `thesis/THESIS.md`; live numbers `STATUS.md` then `STATUS_REFERENCE.md`; **never** `TRADE.md`/`STRATEGY.md` (bannered historical); adversarial state `red/CHALLENGES.md`, never `red/COUNTER_THESIS.md` (frozen argument record).

## 3. Per-dimension local representation

| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| **Thesis structure** | `thesis/THESIS.md:8-32` (retirement blockquote), `:155-183` pillar audit, `:190-212` channel states | Pillars 1-4 audited individually with per-pillar verdicts; channels carry explicit lifecycle tokens (RETIRED / DEAD / monitored). A **deliberately blank successor** section — "WHAT REPLACES IT" left empty on purpose (`:14-15`) | **EXCEEDS** |
| **Convergence / scoring** | `thesis/THESIS.md:55-67` (HISTORICAL conviction decomposition), `:127-142` EV table | 3-axis conviction + carry buckets (7d/30d/60d) + route-EV table. ⚠️ **All now flagged HISTORICAL**: buckets last re-penciled 2026-08-07 (`STATUS.md:57`). **No universal 5-pt handle, no Independence column** | substance present, handle absent, and the substance is frozen |
| **Invalidation / exit** | `thesis/THESIS.md:86-99` two-legged SPF · `:100-109` LOCKED Sep-18 window · `:143-154` sensitivity · `red/CHALLENGES.md` | Two-legged single-point-failure with a **pre-registered numeric invalidation line (−108K/60%)** that actually **fired 2026-08-07** and retired the frame as written. Channel-kill live with named re-add conditions | **EXCEEDS — fleet reference** |
| **Thresholds** | durable: `CLAUDE.md:216-231`; live: `STATUS.md:65-82` | **Two-surface split, exactly implemented** — charter table says "Current values live in STATUS.md" (`CLAUDE.md:218`); STATUS carries src+date on every row. 🆕 the **WQ-162 BASIS blockquote** (`STATUS.md:67`) pins series, session zone, completed-only, revision direction | **EXCEEDS** |
| **Predictions** | `thesis/PREDICTIONS.tsv` | 34 rows, 9 cols, `Confidence` at registration, mark-history chains in `Notes`, WQ-112 two-vintage field form. **Scoreboard 16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN reconciles exactly against the row set** (counted this pass) | **EXCEEDS** |
| **Cross-agent routing** | `CLAUDE.md:190-205` send table · `:207-212` receive · `NEXUS_BRIEF.md` | Send table's `Target` column **explicitly re-labelled "who must ACT, not a delivery address"** with everything routed via WALTER (`CLAUDE.md:190`) — self-caught 2026-09-03. NEXUS_BRIEF folded LAST per Amendment 10 with a STATUS commit-hash provenance line (`NEXUS_BRIEF.md:3`) | **EXCEEDS** |
| **Session handle (BOTTOM LINE)** | — | **STILL ABSENT as an end-cap.** Substance is inverted into the top mega-lede `STATUS.md:3-13`; the file ends on a one-line pointer `STATUS.md:131` | gap (handle only) |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/THESIS.md:86-99` (leg-1 SPF, −108K/60%) | the carry-convexity tail → LOW | `:3` *"Current integration — September 15, 2026; v1.7 unchanged"*; `:6` retirement record dated 2026-08-07 | **FIRED 2026-08-07**, written into the version header with the contract-level arithmetic |
| `thesis/THESIS.md:100-109` (leg-2, LOCKED Sep-18 window) | same frame, second leg | same `:3` stamp | survives only as the **SAM-28 grading horizon** (`:22-24`) — explicitly demoted from an action deadline |
| `thesis/THESIS.md:190-194` Channel 1 | life-insurer repatriation channel | `:3` | **RETIRED** with a named re-add condition (direct foreign SALES at ≥2 institutions across ≥2 consecutive windows — restated `STATUS.md:103`) |
| `thesis/THESIS.md:207-212` Channel 4 | positioning-convexity channel | `:3` | ⚰️ **DEAD 2026-08-07** |
| `thesis/PREDICTIONS.tsv` (3 OPEN rows) | SAM-28 route/magnitude, SAM-31 yen-haven re-couple, SAM-33 BOJ emergency capping | preamble `# As of 2026-09-10` (line 3 of file) | per-row `Status` + `Date_Resolved`; SAM-33 carries an **activation stamp** lifting its VOID/UNTESTED clause (row Notes, 2026-08-17) |
| `STATUS.md:69-82` KEY THRESHOLDS table | live threshold state incl. retired/VOID gates | table rows carry per-row source dates; basis pinned `:67` | retired gates written **VOID** in-row (`:71`, `:81`) rather than deleted |
| `red/CHALLENGES.md` | the whole thesis, adversarially | `:3` `Last real data refresh: 2026-08-20` · `:4` `Last RED sweep: 2026-08-20` | per-key `**Status:**` line + bright-line resolution criteria; rail state summarised `:6-10` |
| `red/COUNTER_THESIS.md` | v1.6.1 (historical) | `:3` `Last real data refresh: 2026-06-30` · `:4` `Last RED sweep: 2026-08-17` | ⚠️ **banner at `:6-7` declares it a frozen record, cite as history** — per-argument standing table `:9-14` |
| `docket/2026-09-18_SAM28_SAM31_REVIEW.md:1-3` | the 9/18 grading of SAM-28/31 | `:1` *"prepared September 9"* | frozen rows + source SHA256; **preparation only, no grade** |
| `MOF_INTERVENTION_PLAYBOOK.md:1-8` | intervention attribution (S1/S1-A ladder) | `:7` `September 8 integration` | method doc; live marks route to `STATUS.md:59-63` / `STATUS_REFERENCE.md` |

## 4. Deviations from standard (+ why)

- **Synthesis-at-TOP instead of a trailing BOTTOM LINE** (`STATUS.md:3-13`) — *equivalent in substance, debt in handle.* Fix is additive (add an end-cap; never replace the lede).
- **Hot / WARM / cold three-tier state split** (`STATUS.md` → `STATUS_REFERENCE.md` → `STATUS_ARCHIVE.md`, `STATUS_REFERENCE.md:3-8`) — *better than standard.* Distinguishes "current but not boot-read" from "superseded", which the two-state fleet rule does not.
- **Charter carries a hand-written MANUAL-ONLY script list** (`CLAUDE.md:269`) while forbidding a hand-written script inventory (`CLAUDE.md:270`) — *deliberate and correct:* the list exists so the generated drift flag stays signal, and its own count defect was self-corrected 2026-08-27 in-row.
- **Ledger two-clock declaration is a separate owned doc** (`workbook/LEDGER_CADENCE.md`) rather than per-file banners — *better;* it names class, latest observation and next check per ledger, which the fleet rule's banner form cannot.
- **An internal sub-agent staff of three with pair-file memories** (KOYOMI/METSUKE/KURA) plus two purpose-built rollers (`scripts/subagent_memory_roll.py`, `scripts/kura_proposal_roll.py`) — *better;* no other market desk has this, and the second roller was built off a measured 179K→50K spawn-read defect (`CLAUDE.md:269`).
- **`red/` is a rail SAM is contractually forbidden to edit** (`CLAUDE.md:261`) — *better in design, debt in operation:* it can only be refreshed by a RED spawn SAM cannot perform, so its staleness is not SAM's to fix (see flags).

## 5. Load-bearing context / DO NOT TOUCH

1. **Money fields.** Avg cost `$58.32` is Will's ground truth (`TRADE.md:72`); FLAT/0 shares Will-confirmed 2026-06-29 (`TRADE.md:51`). METSUKE is **contractually barred** from even flagging them (`METSUKE.md:74`).
2. **`thesis/PREDICTIONS.tsv` preamble** (`:1-30`) — the versioned scoreboard chain, the count-correction line `:2`, and the HIGH-CONFIDENCE FAILURES block `:20-30`. The calibration record *is* the asset; never compact it.
3. **Retired-but-written-in-place gates.** `−108K/60%`, `−140K/−153K`, `USDJPY 160` are kept as **VOID rows** (`STATUS.md:71,80-81`) — do not delete; deleting a fired gate destroys the resolution record.
4. **R = −188,077, not −180,000.** The `25.3% of −180K` form is RETIRED (`STATUS.md:7`, Will-ratified 8/11) and `MEMORY.md` DO-NOT list repeats it. Percentage labels moved; **contract gates did not.**
5. **The WQ-162 USD/JPY basis** (`STATUS.md:67`) — yfinance `USDJPY=X`, London-labelled completed sessions, **as-LAST-REVISED**. Deliberately opposite in direction to LIQUID's as-first-published rule. Never blend with the BOJ 17:00 JST fix or the MOF curve.
6. **The two named STATUS redirects** (`STATUS.md:108-114`) — external consumers cite those section names (WALTER `SIGNAL_PROCESSING_CHECKLIST.md` §v0.30). Do not delete without a consumer re-check.
7. **`red/`** — SAM reads, nobody edits (`CLAUDE.md:261`).
8. **Sub-agent pair-files** — cross-spawn state; the rollers close on different criteria by design (memory on a CLOSURE MARKER, proposals on PROVABLE LANDING) and **must not be merged** (`CLAUDE.md:269`).
9. **Script-owned TSVs** (`MOF_FLOWS.tsv`, `USDJPY.tsv`, `JGB_YIELDS.tsv`, …) — no hand edits; `CLAUDE.md:268` says verify against `boot.py --tools`, not against the charter list.
10. **PROME's inbox is `PROME/inbox/`, never `AGENTS/PROME/inbox/`** (`CLAUDE.md:97`) — SAM regrew the dead tree three times; the rule now lives in the protocol.
11. **The CH-0NN citation collision** (`red/CHALLENGES.md:12`) — two RED namespaces overlap at CH-004/005/009/010/011. Always say which.

## 6. Maturity snapshot

Grades and classification live in `AGENTS/DAEDALUS/FLEET_MAP.tsv` (SAM row) — not restated here. Work queue → `upgrades/SAM_CARD.md`.

Per-dimension read from this pass: thesis **EXCEEDS** · invalidation **EXCEEDS** · thresholds **EXCEEDS** · predictions **EXCEEDS** · routing **EXCEEDS** · convergence-handle **absent and the substance frozen since 8/07** · session end-cap **absent**. Two of the FLEET_MAP L5 legs recorded on 2026-09-01 are now stale in SAM's favour and need re-cutting (see PART B flags R1/R2).

## 7. Open questions / comprehension gaps

1. **Who refreshes `red/`?** The rail is 28 days past its last sweep and its named 9/3 adjudicator has passed. SAM cannot self-serve it. Whether that is a SAM gap, a RED-spawn-scheduling gap, or a PROME gap is **NOT-ADJUDICATED** from inside SAM's tree.
2. **Is the convergence handle worth building at all** on a desk with no live frame? The conviction decomposition is honestly bannered HISTORICAL; a 5-pt matrix over a retired frame could be worse than nothing.
3. **`boot.py --predictions` vs the eyeball scan.** `CLAUDE.md:27` says boot step 6 "has NO INSTRUMENT" and a `predictions_due()` leg is queued; `STATUS.md:118` says `boot.py --predictions` already derives OPEN rows and checks a reminder sidecar. I could not determine from a read whether the charter line is stale or the two describe different things. **CANNOT-EVALUATE** without running the tool.
4. **`SIGNAL_INTAKE.md` disposition** — MEMORY lists "SIGNAL_INTAKE archive" as DEFERRED (`MEMORY.md` DEFERRED block); the file's own banner is itself stale (see flag S3). Archive-or-refresh is an owner call I did not make.
5. **Do the 7 `insurers/` profiles still earn their place** now that Channel 1 is RETIRED? TRACKER was refreshed 2026-09-14, so the answer is presumably yes, but the link from a retired channel to a maintained tracker is not written down anywhere I found.

---

# PART B — REFRESH REPORT · SAM

## B1. Old-profile section disposition

Old profile = `AGENTS/DAEDALUS/profiles/SAM.md` (body built 2026-07-10, banner-superseded-in-part 2026-08-17 at `:3`).

| Old section | Disposition | Evidence |
|---|---|---|
| Δ 2026-08-17 banner ("BODY SUPERSEDED IN PART") | **CARRIED-VERIFIED → now redundant.** Every number it flagged as moved has moved again; PART A replaces the body outright, so the banner retires with it | `profiles/SAM.md:3` |
| Header: *Built 2026-07-10 · Grade at build L4 Conf-H · Class Market* | **CARRIED-VERIFIED** on class; grade defers to FLEET_MAP | `FLEET_MAP.tsv` SAM row cols 2-3 |
| Header staleness trigger: *"refresh when the Sep-18 LOCKED window advances a stage or FXY modal band re-derived or >45d"* | **UPDATED.** The >45d leg fired 2026-08-24. The "FXY modal band" leg is **DROPPED — its subject no longer exists**: `STRATEGY.md` is bannered historical at `:3` and the convexity frame is retired | `profiles/SAM.md:5`; `STRATEGY.md:3-8`; `STATUS.md:5` |
| *Identity: Japan parallel trigger, thesis v1.6.3, best predictions discipline, 3-sub-agent staff* | **UPDATED.** Parallel trigger TRUE-STILL; **v1.6.3 → v1.7**; staff TRUE-STILL (all three ran 2026-09-11) | `thesis/THESIS.md:1`; `056bb0f78`, `a7fc09dbd` |
| File anatomy — Core row (*`STATUS.md` 300 ln > 250 cap*) | **REFUTED.** STATUS is **131 ln / 21,720 B = 67% of budget** after the 2026-09-11 hot/cold split; `STATUS_REFERENCE.md` is new anatomy | `wc`; `a9afd4701`; `read_cap_check.py --agent SAM` → `READ-CAP 0`, 3 reads |
| File anatomy — Thesis row (*PREDICTIONS 54 rows: 9 CONFIRMED/11 FAILED/7 OPEN*) | **REFUTED.** **34 data rows; 16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN**, and the four-way split reconciles exactly against the rows | `thesis/PREDICTIONS.tsv` (counted); `STATUS.md:9` |
| File anatomy — Trading row (*TRADE.md FLAT banner + entry card*) | **UPDATED.** Both `TRADE.md` and `STRATEGY.md` now carry ⚰️ **"HISTORICAL AS OF 2026-08-07 — DO NOT TRADE OFF IT"**; the "modal band UNDER RE-DERIVATION" flag is moot | `TRADE.md:3-8`; `STRATEGY.md:3-8` |
| File anatomy — Workbook row (*17 files, 8 auto TSVs, zero silent rot*) | **UPDATED.** **19 root TSVs**, 11 script-written, plus the new `LEDGER_CADENCE.md`. "Zero silent rot" now **REFUTED in one cell**: `GPIF_FLOWS.tsv` reads ⚠️ STALE +39d | `ledger_staleness.py SAM`; `workbook/LEDGER_CADENCE.md:15` |
| File anatomy — Instrumentation row (*12 py, 11-script BOOT_SEQUENCE*) | **UPDATED.** **24 py + lib/ + tests/**; BOOT_SEQUENCE is **13** entries | `ls AGENTS/SAM/scripts/`; `scripts/boot.py:63-77` |
| File anatomy — Ops row (*docket/red/insurers/NEXUS_BRIEF/board_log/OPEN_THREADS*) | **CARRIED-VERIFIED**, plus new `audits/`, `evals/runs/`, `reports/`, `STATUS_REFERENCE.md` | `git ls-files` |
| Per-dimension §1 EXCEEDS | **CARRIED-VERIFIED** | `thesis/THESIS.md:155-212` |
| Per-dimension §2 *"substance abundant, handle ABSENT"* | **UPDATED — worse.** Handle still absent **and** the substance is now explicitly HISTORICAL/frozen (buckets last assessed 8/07) | `thesis/THESIS.md:55` heading; `STATUS.md:57` |
| Per-dimension §3 *"two-surface split exactly implemented"* | **CARRIED-VERIFIED and strengthened** by the WQ-162 basis blockquote | `CLAUDE.md:218`; `STATUS.md:67` |
| Per-dimension §4 EXCEEDS (two-legged SPF, LOCKED window, channel-kill) | **CARRIED-VERIFIED — and the SPF has since FIRED as written** | `thesis/THESIS.md:6`, `:22-24` |
| Per-dimension §5 EXCEEDS (*fleet-reference candidate*) | **CARRIED-VERIFIED** | preamble `thesis/PREDICTIONS.tsv:1-30` |
| Per-dimension §6 EXCEEDS (route matrix + NEXUS_BRIEF) | **CARRIED-VERIFIED and upgraded** — the send table now names WALTER routing explicitly | `CLAUDE.md:190`; `NEXUS_BRIEF.md:3` |
| Per-dimension §7 EXCEEDS (flow-sign≠program-direction, pre-registration, Δ>5pp rule) | **CARRIED-VERIFIED in kind; the cited locator is DEAD.** "STATUS:204" does not exist in a 131-line file. Folded into §4/§5 of PART A rather than re-anchored | `wc -l AGENTS/SAM/STATUS.md` = 131 |
| Per-dimension §8 *"handle MISSING — no BOTTOM LINE; STATUS 300>250"* | **SPLIT: BOTTOM LINE TRUE-STILL (still no end-cap); the 300>250 half REFUTED** | `STATUS.md:131`; `wc -l` = 131 |
| DO-NOT-TOUCH 1 (money fields, $58.32, METSUKE barred) | **CARRIED-VERIFIED.** The "no realized P&L — TBD from Will" line's old locator STATUS:239 is dead; the substance is at `STATUS.md:99` | `TRADE.md:51,72`; `METSUKE.md:74` |
| DO-NOT-TOUCH 2 (PREDICTIONS preamble + mark chains) | **CARRIED-VERIFIED** | `thesis/PREDICTIONS.tsv:1-30` |
| DO-NOT-TOUCH 3 (LOCKED Sep-18 window language, THESIS:45-53) | **UPDATED.** Substance TRUE-STILL but demoted to a **grading horizon**; locator moved to `thesis/THESIS.md:100-109` | `thesis/THESIS.md:22-24` |
| DO-NOT-TOUCH 4 (sub-agent pair-files) | **CARRIED-VERIFIED and extended** — the two rollers' differing closure criteria are now themselves DO-NOT-MERGE | `CLAUDE.md:269` |
| DO-NOT-TOUCH 5 (`red/` — SAM reads, nobody edits) | **CARRIED-VERIFIED** | `CLAUDE.md:261` |
| DO-NOT-TOUCH 6 (Signal-Status mega-lede format) | **CARRIED-VERIFIED** | `STATUS.md:3-13` |
| DO-NOT-TOUCH 7 (`MOF_FLOWS.tsv` script-owned) | **CARRIED-VERIFIED, generalised** to all 11 script-written TSVs | `CLAUDE.md:268` |
| L4 consumption evidence (BOND quotes SAM by name; 2 consumed packets; carry buckets → LIQUID/HENRY) | **CANNOT-EVALUATE from SAM's tree** — the cited anchors are BOND-side line numbers I did not open, and the "STATUS:202" carry-bucket locator is dead. Consumption is independently re-evidenced by 4 routed-in packets this period (PROME ×2, RED, WALTER→SAM) | `git log --after=2026-09-01 -- AGENTS/SAM/` |
| Owner-lane flags — *FXY modal band OVERDUE* | **DROPPED — subject retired.** `STRATEGY.md` is historical; no modal band is live | `STRATEGY.md:3-8` |
| Owner-lane flags — *STATUS compress shape identified* | **DROPPED — DONE.** Executed 2026-09-11 via hot/cold split, plus a 2026-09-01 archive split | `a9afd4701`; `STATUS_ARCHIVE.md:3` |
| Owner-lane flags — *stale oil/MOU 8% EV cell* | **CANNOT-EVALUATE.** The EV table is inside the HISTORICAL block; a stale cell in a bannered-historical table is not a live defect | `thesis/THESIS.md:127-142` |
| Owner-lane flags — *ledger_staleness boot lines unwired* | **UPDATED — superseded by a better answer**: the desk built `workbook/LEDGER_CADENCE.md` (a per-ledger two-clock declaration) instead of boot lines | `workbook/LEDGER_CADENCE.md:1-25` |
| Owner-lane flags — *SIGNAL_INTAKE.md self-labeled stale* | **TRUE-STILL and now worse** — see flag S3 | `SIGNAL_INTAKE.md:3` |
| Owner-lane flags — *Korea/ZHAO overlap CLEAN* | **CANNOT-EVALUATE this pass** — not re-tested; no contradicting evidence found in SAM's tree | — |
| *"red/ 48d stale (RED-spawn-only)"* (from the 8/17 banner) | **UPDATED.** RED ran 8/17, 8/20 and 8/27; the rail is now **28d** past its last sweep with a **passed dated adjudicator** — a different and sharper problem | `red/CHALLENGES.md:3-7`; `daba336d5` |
| *"CLAUDE.md:85 HERMES-era mail line"* (from the 8/17 banner) | **DROPPED — FIXED.** The charter now says HERMES is RETIRED and is not a router, with the DEAD-ROUTER correction in-line | `CLAUDE.md:72`, `:96` |
| *"3 readerless gates at the 8/17 4.00% break"* | **PARTIALLY DROPPED.** SAM-33's activation was stamped 8/17 in-row and `rate_differential.py` was built + boot-wired for SAM-41; FLEET_MAP still records 1-of-3. Not re-counted this pass | `thesis/PREDICTIONS.tsv` SAM-33 Notes; `scripts/boot.py:70` |

## B2. File tree at HEAD

`git ls-files AGENTS/SAM/ | wc -l` = **818**. Cluster counts (`awk` on the first path segment):

| Cluster | Files | Note |
|---|---|---|
| `inbox/` | ~470 | overwhelmingly `inbox/WALTER/processed/` — the signal lane, **0 unprocessed at top level** |
| `archive/` | ~90 | incl. `archive/RED_old/`, `archive/outbox/`, `archive/research/` |
| `evals/` | ~50 | `evals/runs/2026-09-09_boot-promotion/` is a real harness run with events.jsonl + manifests |
| `thesis/` | 17 + `timeline/` | see anatomy |
| `workbook/` | 26 | 19 root TSVs + KURA trio + README + `LEDGER_CADENCE.md` + `boj_ois_reviews/` |
| `scripts/` | 24 py + `lib/` + `tests/` + `AUTOMATION_PLAN.md` + `README.md` | |
| `docket/` | 9 | |
| `reports/` | ~20 dated + `boot-runs/` | ~1 per session |
| `insurers/` | 8 | TRACKER + 7 profiles |
| `red/` | 5 | |
| root `.md` | 21 | |

**Boot-read surfaces, measured** (`scripts/read_cap_check.py --agent SAM`, budget 32,550 B):

| Surface | Bytes | % of budget | Verdict |
|---|---|---|---|
| `STATUS.md` | 21,720 | 67% | ✅ |
| `MEMORY.md` | 21,373 | 66% | ✅ |
| `STATUS_REFERENCE.md` | 8,109 | 25% | ✅ |

`READ-CAP-RESULT v1 mode=agent rc=0 desk=SAM reads=3 over_budget=0 over_cap=0`. ⚠️ The tool's own caveat applies: SAM has **no `PROME/registry/READS.tsv` declaration**, so this is "clean within what the charter heuristic found", not a clean bill — `thesis/THESIS.md` (65,371 B), `thesis/timeline/TIMELINE.md` (~96 KB) and `thesis/PREDICTIONS.tsv` (89,614 B) are all **section-scoped reads** the scan does not measure, and the charter says so explicitly (`CLAUDE.md:22,25,27`).

## B3. Period activity (2026-09-01 → 2026-09-17)

| Metric | Value |
|---|---|
| Commits touching `AGENTS/SAM/` | **101** |
| **Self-authored** (subject `SAM:` or `[tag] SAM:` or `SAM -> X`) | **67** |
| Routed-in | 34 (WALTER ×31, PROME ×2, RED ×1) |
| **Last self-authored commit** | `121233a0c` **2026-09-15** — *"[cleanup] SAM: save session handoff and freeze historical completion stamp"* |
| Dark days since last self-commit | **2** |
| `STATUS.md` delta since `e6fc35eaf` (9/1 base) | **+76 / −192 lines** — net compression, consistent with the 9/11 hot/cold split |
| Distinct session days | 9/8, 9/9, 9/10, 9/11 (very heavy), 9/14, 9/15 |

Substantive period work verified at commit subjects: FY2025 JGB backfill (`5609211aa`), CFTC NET-LONG flip (`266b11482`), STATUS hot/cold split (`a9afd4701`), memory/proposal roller defects found and fixed (`022623946`, `056bb0f78`, `42b5777ef`), xccy proxy activation **DECLINED** with a written reason (`7bb239c70`), a 40-file retirement sweep (`fbfd4fede`), and a self-caught stale flag that had been false for 15 days (`644fc8388`).

## B4. Open questions I could not settle

1. Whether `boot.py --predictions` supersedes `CLAUDE.md:27`'s "this step has NO INSTRUMENT" — a read cannot tell; needs one tool run. **CANNOT-EVALUATE.**
2. Whether the BOND-side L4 consumption anchors in the old profile still resolve — out of perimeter this pass. **NOT-ADJUDICATED.**
3. Whether the 3-readerless-gates count on the FLEET_MAP row is now 1, 2 or 0 — two of three have visible fixes but I did not enumerate the third. **NOT-SEEN** (not 0).
4. Whether `GPIF_FLOWS.tsv`'s +39d is genuine rot or correct quarterly behaviour — see flag S2; the cadence doc argues the latter, the scanner the former.

## B5. Flags for the OWNER (SAM), each verified at the artifact

| # | Sev | Flag | Verified at |
|---|---|---|---|
| **S1** | 🔴 | **`red/CHALLENGES.md` CH-017's CONFIRMED condition is now falsified on its own terms and nobody has adjudicated it.** CH-017 reads *"CONFIRMED … if SAM-41 resolves TRUE by 2026-10-31 **while USD/JPY never trades below 155 inside the same window**"*. **SAM-41 RESOLVED CONFIRMED 2026-08-19** and USD/JPY has since printed **154.31 completed Sep-14 / 154.82 live Sep-15** — below 155, inside the window. The rail still carries CH-017 as `OPEN — … resolves by 2026-10-31 with SAM-41`, i.e. keyed to an anchor that fired 29 days ago. *(The second "or" branch — ≥60% of gap closure attributable to the US leg — is NOT graded here; the finding is that an adjudicatable state change exists and is unread.)* | `red/CHALLENGES.md:217` (criteria), `:219` (Status); `thesis/PREDICTIONS.tsv` SAM-41 row `Status=RESOLVED CONFIRMED / Date_Resolved=2026-08-19`; `STATUS.md:34` and `:71-72` |
| **S2** | 🔴 | **CH-009's own pre-registered bright line named the 30Y auction of 2026-09-03 as adjudicator #2; that auction has happened, SAM has the result on its own surface, and no RED pass has run since 2026-08-27.** SAM's STATUS records *"Sep-3 30Y SOFT remains PRECISION-LIMITED"*. CH-009 and the chained CH-012 are both still `interim NO-VERDICT, next 9/3`. **14 days slipped.** SAM cannot self-serve this — it needs a RED spawn. | `red/CHALLENGES.md:7`, `:59` (bright line), `:63` (DISMISS conjunction legs); `STATUS.md:44`; last `red/` commit `daba336d5` 2026-08-27 |
| **S3** | 🟠 | **`SIGNAL_INTAKE.md`'s stale banner is itself stale, twice over** — it says *"thesis now v1.6.9"* (thesis is **v1.7**) and *"spot now 163.16"* (live **154.82**). WALTER is the named consumer of this file, so a WALTER-side routing decision could be made off a v1.0 trigger list, a retired Channel 1 priority, and a sub-160 regime assumption that inverted. `MEMORY.md` carries "SIGNAL_INTAKE archive" as DEFERRED. Archive it or re-stamp it; a banner naming the wrong version is a header edit mistaken for maintenance. | `SIGNAL_INTAKE.md:3,5`; `thesis/THESIS.md:1`; `STATUS.md:34`; `MEMORY.md` DEFERRED block |
| **S4** | 🟠 | **`workbook/GPIF_FLOWS.tsv` reads ⚠️ STALE +39d on the fleet scanner while `LEDGER_CADENCE.md` calls it LIVE quarterly, next check ~November.** Both cannot be right for a reader. The cadence doc is almost certainly correct on the world; the defect is that the scanner and the declaration disagree with no reconciling token. Either mark the row FROZEN-until-Q2 or give `ledger_staleness.py` the cadence signal. Nothing in this flag says the data is wrong. | `ledger_staleness.py SAM` → `⚠️ STALE +39d`; `workbook/LEDGER_CADENCE.md:15` |
| **S5** | 🟠 | **STATUS still has no trailing BOTTOM LINE.** The file ends on a one-line pointer (*"Thesis v1.7 → …; No successor declared."*). The substance is inverted into the top mega-lede, which is a legitimate local form — but a reader truncating the file, or a consumer scanning for the standard end-cap, gets a pointer. Add an end-cap **alongside** the lede, never replacing it. | `STATUS.md:131` vs `:3-13` |
| **S6** | 🟡 | **The convergence/conviction layer is honestly bannered HISTORICAL and has no live successor.** Carry buckets last assessed 2026-08-07; conviction decomposition is headed `HISTORICAL … not fresh probabilities`. That is the *right* state for a retired frame, and it is written down. The flag is only that nothing schedules a decision about whether it is re-penciled or formally retired — an un-owned "leave blank on purpose". | `STATUS.md:57`; `thesis/THESIS.md:55` |

### FALSE-POSITIVE-CANDIDATEs (SAM) — candidate flags I could NOT verify as defects

- **FALSE-POSITIVE-CANDIDATE — `red/COUNTER_THESIS.md` "STALE 29d, cites v1.6".** `falsification_scan.py` flags it (stamp 2026-08-17 vs live ref 2026-09-15, threshold 21d). **The file pre-empts this in its own header**: `:3` *"the argument below is unchanged from that date — it is the record of a counter-case, not a live dashboard"* and `:6-7` *"kept verbatim because the argument is the record and rewriting it would corrupt what RED actually claimed on 6/30. Cite it as history"*, with a per-argument standing table `:9-14`. The live rail is `CHALLENGES.md`. I judge the scanner's row a **class error** (it grades a frozen record against a live-surface threshold), and the real defect is S1/S2, not this. Recommend: leave the file alone, teach the scanner the FROZEN-record form, or re-point the SAM row at `CHALLENGES.md`.
- **FALSE-POSITIVE-CANDIDATE — "CH-016's 2026-09-08 resolution criterion has passed unadjudicated."** I found a dated criterion at `red/CHALLENGES.md:197` referencing 2026-09-08 and initially read it as a slipped deadline. **It belongs to CH-016, which was CLOSED RESOLVED-DISMISSED-CONVERGED on 2026-08-20** (`:6,8`), i.e. resolved *before* its own date. Not a defect. Recording it because the CH-0NN namespace collision (`:12`) makes this exact mis-read cheap.
- **FALSE-POSITIVE-CANDIDATE — "boot step 6 has no instrument."** `CLAUDE.md:27` asserts it; `STATUS.md:118` describes `boot.py --predictions` doing the derivation. One of the two is stale and I cannot tell which from a read. Not raised as an owner defect.

### Reviewer-side findings — DAEDALUS's own map is wrong (welcome findings per brief rule 5)

| # | Finding | Evidence |
|---|---|---|
| **R1** | **The SAM FLEET_MAP `Gaps` cell (Last_scored 2026-09-01) is REFUTED on two legs.** It reads *"Byte-creep TRUE: STATUS 79,059 B / 247 ln (243% of read budget)"* — STATUS is now **21,720 B / 131 ln = 67% of budget**, fixed by the 9/1 archive split and the 9/11 hot/cold split. It also reads **"Dark since 8/27"** — SAM has **67 self-authored commits since 9/1**, last one 9/15. The `Next_upgrade` cell still asks for *"a STATUS byte tier (rotate to <32,550 B)"*, which is **already done**. | `FLEET_MAP.tsv` SAM row cols 6-8; `read_cap_check.py --agent SAM`; `a9afd4701`; `git log --after="2026-09-01"` |
| **R2** | **Three locators in the old profile are dead against a 131-line STATUS** — `STATUS:204`, `STATUS:239`, `STATUS:202` (§7 Δ>5pp rule, the no-realized-P&L line, the carry-buckets routing line). The substance of all three survives; only the anchors rotted. This is the predictable cost of anchoring a profile to line numbers in a file under active rotation. **Recommend profiles anchor to section headings, not line numbers, on any surface that rotates.** | `profiles/SAM.md` §Per-dimension §7, §DO-NOT-TOUCH 1, §L4 consumption; `wc -l AGENTS/SAM/STATUS.md` = 131 |
| **R3** | **`falsification_scan.py`'s SAM row grades a self-declared frozen record.** See the first FALSE-POSITIVE-CANDIDATE. The scan has exactly one SAM surface in its visible set (`red/COUNTER_THESIS.md`) and it is the wrong one — the live rail (`red/CHALLENGES.md`, stamped `:3-4`) is not in the row set at all, and it is the surface where the two real slips (S1, S2) live. | `falsification_scan.py` output SAM row; `red/CHALLENGES.md:3-4` |

---
---

# ═══ DESK 2 of 2 — SHADE ═══

# PART A — REFRESHED PROFILE (draft, ready to become `profiles/SHADE.md`)

# Agent Profile — SHADE

**Profile vintage:** 2026-09-17 (reader draft, DAEDALUS re-verification pending)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** solo full-core read (P3 reader, fan-out leg)
**Sources read:** `CLAUDE.md` (whole, 170 ln) · `STATUS.md` (whole, 150 ln) · `SCRATCH.md` (whole) · `MEMORY.md` (section map) · `REFERENCE.md` (§8, §10b, section map) · `NEXUS_BRIEF.md` · `MAINTENANCE.md` (top) · `board_log.tsv` · `registry/corrections_receipts.tsv` · `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md` · `research/` + `domain/sources/` + `sources/` listings · `inbox/WALTER/` listing · `2026-08-04_athene-q2-m11-grade-card.md`
**Staleness:** refresh when **any ONE** of: (a) a file matching `AGENTS/SHADE/*PREDICT*` or `AGENTS/SHADE/**/PREDICTIONS.tsv` exists (the standing L4 trigger — it has still not fired); (b) `AGENTS/SHADE/STATUS.md:3` `**Last Updated:**` advances past 2026-08-28; (c) `ls AGENTS/SHADE/inbox/WALTER/*.md | wc -l` returns 0 after currently reading 14 (i.e. the desk booted and drained); (d) hard floor **2026-11-01**.
*(The prior profile's floor of 2026-09-15 has PASSED — this draft is the response to it.)*

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

## 1. Identity

PE-owned life-insurer / captive-reinsurance forensics — the *shadow insurance system*: affiliated reinsurance, offshore captives, synthetic surplus, FABN/FHLB funding, AMAPS/CFO rated wrappers, Egan-Jones ratings machinery, AG 55 / NAIC / SVO. **Class:** Market (`FLEET_MAP.tsv` SHADE row). **Core question** (`CLAUDE.md:9`): *when private-credit stress enters an insurance wrapper, does it become hidden leverage, funding fragility, or forced capital pressure?*

**Transmission:** signals to BROCK / LIQUID / REGINALD / NEXUS+PROME (`CLAUDE.md:147-151`); reads those desks as owners rather than re-deriving (`STATUS.md:111-123`). **Spawnable by:** PROME / Will. **SHADE-canonical owner of insurer-exposure figures**; the BROCK boundary is a four-row table at `CLAUDE.md:15-22`.

One line: *the desk that asks whether stressed credit is being made to look contained by an insurance balance sheet.*

## 2. File anatomy (where the richness lives)

162 tracked files (`git ls-files AGENTS/SHADE/ | wc -l`) — a **small, dense** tree, the opposite shape from SAM.

| File / cluster | Holds | Bytes | Richness |
|---|---|---|---|
| `CLAUDE.md` (170 ln) | identity, BROCK boundary table `:15-22`, 5 key ratios `:32-37`, Athene target block `:39-46`, **4 independent kill paths `:48-52`**, environment threshold band `:54-62`, 🆕 **§REGISTERED TRIGGERS / T-SHADE-01 `:64-87`**, historical precedents `:91-96`, symmetric boot↔closeout `:98-145` | 22,082 | **durable method + the desk's only registered trigger** |
| `STATUS.md` (150 ln) | **the canonical live surface.** §0 where-everything-is + the rotation receipt `:12-26` · §0l live rails `:30-43` · §1 top-line `:47-51` · **§3 signal dashboard with a 5-pt stackable handle + Independence column `:55-78`** · §4 transmission map incl. 🆕 stage 4b `:81-85` · §6 forward regulatory calendar + the Delaware Life escalation ladder `:89-102` · §7 cross-agent deps `:111-123` · §10 owed list `:127-140` · **BOTTOM LINE `:146-150`** | **32,462 = 100% of budget** | live state; **rotate-tier** |
| `REFERENCE.md` (201 ln) | **the cold half, born 2026-08-28.** §2 carried figures · §2Q Delaware Life Q2 statutory · §2Q-bis the four-denominator warning · §3D per-vector evidence · §3R per-vector one-liners · §4 full transmission map · §5 watchlist · §6M standing monitor rows · §8 active questions (10) · §9 retired rails · **§10b DAEDALUS maturity asks** | 36,669 | **NOT boot-read; consulted by section before citing any figure** (`CLAUDE.md:111`) |
| `SCRATCH.md` (88 ln) | **canonical session handoff** — CHANGES SINCE / WHAT I DID / 🔴 NEXT SESSION (13 dated, priority-ordered items) / open threads / mail state | 10,288 | handoff |
| `MEMORY.md` (111 ln) | BROCK boundary, source-quality caveats, forensic-discipline lessons, a rotated-lessons one-line index, per-session lesson blocks | **31,745 = 98% of budget** | learning; **rotate-tier** |
| `MAINTENANCE.md` (186 ln) | structural-change log; the 8/28 entry `:7-14` records an Amendment-10 self-violation and a stamp defect, both caught and repaired | 46,312 | architecture record |
| `NEXUS_BRIEF.md` (32 ln) | board-facing synthesis; folded LAST per Amendment 10 `:3` | 13,145 | cross-agent |
| `research/` (19 files) | per-thread deep work: ATHENE_FABN_MATURITY_LADDER + `AGF_NPORT_crawl_2026-06-22.py`/`.json` · FABN_PEER_SPREAD_NPORT `.py`/`.json` + the 8/28 RERUN + RUNLOG · DELAWARE_LIFE ×4 · ATHENE_FUNDING_MIX · BMA_EGAN_JONES · COMBINED_INSURER_SINK_WELD2 · ARCC pre-registration · INSURER_LENDER_DOUBLE_JEOPARDY | — | **crown jewels + the only executable code on the desk** |
| `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md` | **new anatomy.** A pre-registered instrument spec (S1/S2/S3), `State: REGISTERED, NOT YET GRADED`, with an explicit companion-not-replacement constraint | — | pre-registration discipline |
| `domain/sources/01-08` | 8 deep KB reference reports (PE nexus → captive/XOL → statutory reserves → liquidity transmission → filing forensic manual → Apollo fee dependency → FABN wall → Egan-Jones) | — | KB library, **Mar'26 vintage, stale-flagged at `STATUS.md:8`** |
| `sources/athene_statutory_2026-06-15/` | ~12K lines raw statutory text (AANY/ALIRT/ALRE) + `MANIFEST.md` | — | primary-filing chain (SKIP for grading) |
| `registry/corrections_receipts.tsv` | **new anatomy** — R1 corrections receipts; exactly 1 row (`COR-20260828-03`, NO-OP) | — | protocol compliance |
| `board_log.tsv` (97 rows) | WALTER signal-consumption ledger, `timestamp_read/signal_id/disposition/source/notes` | — | record |
| `archive/` (17 files) | incl. the three **crc32-stamped** 8/28 pre-rotation files (STATUS 125,359 B crc `0502fd27`; SCRATCH 50,727 B crc `34385c68`; MEMORY 35,782 B crc `fdf1e872`) | — | **the fleet's cleanest byte-cap rotation receipt** |
| `2026-08-04_athene-q2-m11-grade-card.md` | the M-11 dual-test grade card, **at agent root** | — | ⚠️ still not in any ledger |
| `outbox/` (7) · `inbox/` | delivery memos to PROME; `inbox/WALTER/` lane + `inbox/processed/` | — | **14 files sit unprocessed in `inbox/WALTER/`** |

*Key question this answers:* live state → `STATUS.md`; **any figure before citing it** → `REFERENCE.md` §2/§2Q; what fires the dig → `CLAUDE.md:64-87`; what happened last session → `SCRATCH.md`; why the structure is this shape → `MAINTENANCE.md`.

## 3. Per-dimension local representation

| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| **Thesis structure** | `CLAUDE.md:48-52` (4 independent kill paths) + `STATUS.md:47-51` (top-line + SHADE-specific thesis) + `STATUS.md:81-85` / `REFERENCE.md §4` (6-stage transmission map) | Kill paths are numbered and independent; the transmission map gained **stage 4b (distribution channel closes — the LIABILITY side)** on 2026-08-28 after an event the map had no rung for | **strong** |
| **Convergence / scoring** | `STATUS.md:55-71` | 🆕 **"Convergence index (5-pt stackable handle)"** — 9 vectors, per-vector score, **Independence column with a shared-antecedent flag**, and a **composite over SHADE-owned independent roots only: 20/30**, plus a written guard against reading a single-name firing vector as cohort stress | **NOW CONFORMANT** — this is the handle the old profile recorded as missing |
| **Invalidation / exit** | `CLAUDE.md:48-52` kill paths · `CLAUDE.md:64-87` **T-SHADE-01** · `STATUS.md:95` escalation ladder (markers 0-6) · `STATUS.md:101` C2 self-executing withdrawal test | T-SHADE-01 is a **two-leg conjunctive** trigger with a named `value_basis`, a *directional-not-relative* sign leg, a window-sensitivity guard, an ownership split (LIQUID owns the series, SHADE owns only whether the trigger fires), and a **counted fired-state: 4-for-4 NOT MET**. C2 is a **self-executing withdrawal** dated 2026-11-18 | **strong; the FIRED-triad ask is effectively answered in counted form** |
| **Thresholds** | `CLAUDE.md:54-62` durable environment band · `STATUS.md:43` live tape · `REFERENCE.md §2` carried figures | Durable-vs-live split with an **explicit do-not-confuse note** (`CLAUDE.md:87`): the environment band and T-SHADE-01's level leg *will disagree by construction* | **conformant (strong)** |
| **Predictions** | **no ledger.** Named binaries live scattered: `PRED-006` with a confidence chain 65%→30% (`STATUS.md:98`), the canary spec `REGISTERED, NOT YET GRADED`, the 2026-11-18 C2 test, the ladder's dated Q3 step | Dated, falsifiable, confidence-bearing — and **with no scoring surface**. Self-flagged 🔴 in three places | **MISSING — the single L4 blocker** |
| **Cross-agent routing** | `CLAUDE.md:147-151` · `STATUS.md:111-123` · `NEXUS_BRIEF.md` | §7 is written as *"read the OWNER, never re-derive"*, with the **CCC channel reconciled to one-owner-each** and an explicit **independence bar** (both ratios read the same 787-obs series ⇒ agreement is arithmetic, not corroboration) | **strong** |
| **Session handle** | `STATUS.md:146-150` | **BOTTOM LINE present**, dated, and it leads with the session's own instrument failures | **present** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)

⚠️ **SHADE has no thesis-class file. Its rails live in `CLAUDE.md` and `STATUS.md` §6, which is why `falsification_scan.py` reports "no surface this scan can see" for SHADE** — that is a scanner blind spot, **not** an L3 gap. Hand-derived inventory:

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `CLAUDE.md:48-52` — the 4 independent kill paths | the whole SHADE thesis, four ways | path 1 carries `(Currently YELLOW per 6/22 ladder …)` — **the only stamp, and it is 6/22** | per-path colour + a named RED bar (FABN spread >250bp **or** a pulled/failed syndication) |
| `CLAUDE.md:64-87` — **T-SHADE-01** wrapper-decoupling | arms the pre-registered statutory entity+fund dig (`STATUS.md:137`) | `**State 2026-08-28**` row `:85`; sign-leg reading row `:82` dated 8/13→8/28 | ❌ **NOT ARMED — ZERO legs, both freshly measured**; level leg HY OAS 263 = 17bp below bar; sign leg **4-for-4 NOT MET** |
| `CLAUDE.md:54-62` — environment threshold band | the credit-environment read (not an arming condition) | none in-row; live values at `STATUS.md:43` | green/yellow/red per signal; explicit non-conflict note `:87` |
| `STATUS.md:95` — **Delaware Life escalation ladder** (markers 0-6) | vector #1's escalation state | `**AMENDED 2026-08-28**` in-row | **🆕 marker (0) COUNTERPARTY/DISTRIBUTION — ✅ MET 2026-08-28** (Truist + Fifth Third paused) |
| `STATUS.md:96` — Delaware Life Q3-2026 statutory | the ladder's **first DATED step** | `~2026-11-15` in the Date column | instruments named (Exhibit 1, SoO L15) differenced against the 1H-26 baseline |
| `STATUS.md:98` — `PRED-006` MBA Q2 bar | the CRE/multifamily holdings leg | `~2026-09-mid` in the Date column; confidence chain **65% → 30%** | **≥ +$10.0B as printed**; graded jointly with `PRED-CREED-010`. ⚠️ **date window is NOW** |
| `STATUS.md:101` — **C2 withdrawal test** | SHADE's own C2 claim — *self-executing against itself* | `2026-11-18` in-row | three-conjunct bar (peer penalty ≤+48bp AND S1 ≥$2.0B AND S2 ≥36.2%) ⇒ *"I withdraw C2 and record the quiet as informative health"* |
| `STATUS.md:102` — **W2 ordering test** (shared with BROCK) | the bloc's instrument set | `Standing, no expiry` | a gated instrument firing before/with the non-gated one ⇒ **the bloc owes a RETRACTION, not a re-spec** |
| `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md:3` | kill-path 1's second reading | `**Dated spec:** 2026-08-13 · **State:** REGISTERED, NOT YET GRADED` | S1/S2/S3, no-bands rule; first graded reading at the Athene Q3 cluster (`STATUS.md:99`) |
| `REFERENCE.md §8` (10 active questions) | the research agenda, several with pre-stated expected results | section header only | items 7 CLOSED-with-verdict-retained, 8/9/10 OPEN; item 2 flagged *"no EDGAR screen exists"* |

## 4. Deviations from standard (+ why)

- **No thesis file; the thesis is distributed across `CLAUDE.md` (kill paths) + `STATUS.md` §1/§3/§4.** *Equivalent, with one cost:* it is invisible to the fleet falsification scanner, which then prints a Market-class gap over a desk that has rails. Fix is a scanner/registry fix, not a SHADE restructure.
- **Hot/cold split into `STATUS.md` + `REFERENCE.md` with a crc32-stamped verbatim archive.** *Better than standard* — 125,359 B → 32,462 B with a byte-exact reproduction recipe written into the receipt (`STATUS.md:20`). This is the form to copy fleet-wide.
- **`SCRATCH.md` as the canonical handoff, `LAST_COMPLETION.md` demoted to legacy** (`CLAUDE.md:167`). *Equivalent.*
- **Read→write pairing declared as one symmetric sequence** (`CLAUDE.md:102`): STATUS read 1 → write 6, SCRATCH read 2 → write 8, MEMORY read 3 → prune 9, NEXUS_BRIEF write 11a LAST. *Better* — makes the closeout auditable against the boot.
- **A trigger registered with an ownership split rather than a copied series** (`CLAUDE.md:80`). *Better* — SHADE reads LIQUID's HY OAS and owns only the firing decision, which is exactly the anti-fork form.
- **Predictions absent while resolution behaviour is present.** *Debt, and DAEDALUS's own promotion logic said so*: SHADE was promoted L2→L3 on behaviour rather than shelves (`REFERENCE.md §10b:3`). The debt is one file.
- **`domain/sources/` exists but `CLAUDE.md:154` still says "If future `domain/sources/` scaffolding is built, update this pointer."** *Pure debt* — a stale pointer in the charter (see flag H4).

## 5. Load-bearing context / DO NOT TOUCH

1. **The 8/28 crc32 rotation receipts** (`STATUS.md:20-21`) — `tail -n +8` reproduces the pre-rotation STATUS byte-for-byte. Never edit the archived copies; the crc is the proof.
2. **T-SHADE-01's sign leg is DIRECTIONAL, not relative** (`CLAUDE.md:78`) and **is a DATED READING, not a standing state** (`CLAUDE.md:81`) — any level-leg crossing obliges a **fresh** close-based read before the trigger state is restated. Do not collapse it into a relative spread.
3. **The window-sensitivity guard** (`CLAUDE.md:79`): the *relative* spread flips sign with the start date (+1.04pp from 8/3 vs −0.88pp from 7/31, same end date). Never quote it without its window.
4. **T-SHADE-01's sign leg ≠ BROCK's wrapper half** (`CLAUDE.md:83`) — BROCK's additionally requires HY widening, CCC-led. One can flip with the other unmoved.
5. **HY OAS series ownership is LIQUID's; SHADE keeps no parallel series and no parallel sustain count** (`CLAUDE.md:80`, `STATUS.md:114`).
6. **CCC ratios: SHADE registers NEITHER** (`STATUS.md:115-120`). `CCC/HY` → REGINALD `VX-REG-18.04` (Will-approved stand-down attached); `CCC/BB` → BROCK `KB-BRK-221`. **The independence bar never lifts** — both read the same 787-obs series, so agreement is arithmetic.
7. **The retracted 12× leverage figure stays retracted — the filing says 5.1×** (`STATUS.md:38`).
8. **No post-pause flow figure exists** (`STATUS.md:38`); *"regulatory margin call"* and *"flows going the wrong way"* are the relayer's words, stripped by WALTER, and are on **no SHADE surface**.
9. **Four denominators circulate for Delaware Life; concentration swings ~9pp on the choice** (`REFERENCE.md` §2Q-bis). Quote the **pair** (dollars up 2.75%, share down 2.85pp), never one leg.
10. **Peer-relative spread sub-row** — an absolute T+123 green can mask a cohort-widest +43-48bp penalty. MEMORY-codified canary.
11. **Standing rule: no dig absent a trigger** (`CLAUDE.md:84`). The statutory dig is deploy-on-trigger, ordered a→d.
12. **The BROCK boundary and `[CONF BROCK date]` citation form** (`CLAUDE.md:22`); do not maintain a duplicate BROCK dashboard.
13. **Statutory provenance tree** (`sources/athene_statutory_2026-06-15/MANIFEST.md`) and the reusable EDGAR/NPORT crawlers (`research/AGF_NPORT_crawl_2026-06-22.py`, `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py`) — the desk's unique forensic capability.
14. **Session delta lives in `research/`; STATUS carries only the verdict and the live rails** (`STATUS.md:26` standing rule ①). This is what stops §0 accreting; it is the rule that made the byte fix hold.

## 6. Maturity snapshot

Grades and classification live in `AGENTS/DAEDALUS/FLEET_MAP.tsv` (SHADE row). Work queue → `upgrades/SHADE_CARD.md`; the desk mirrors the asks itself at `REFERENCE.md` §10b.

Of the three L2→L3 asks recorded 2026-07-27: **#3 (STATUS compress) ✅ DONE 2026-08-28** under a harder constraint than asked; **#2 (standing FIRED-triad) effectively answered** in counted form at `CLAUDE.md:82` (*4-for-4*) though `REFERENCE.md §10b` still marks it 🔴 OPEN; **#1 (`PREDICTIONS.tsv` with confidences at registration) 🔴 OPEN and untouched across six sessions** by the desk's own count (`SCRATCH.md:42`). That one file is the whole L4 path.

## 7. Open questions / comprehension gaps

1. **Why hasn't SHADE booted since 2026-08-28?** Zero self-authored commits in the review period; the last three real sessions were Will-directed or PROME-orchestrated. Whether this is correct watch-agent cadence for a latent-vector desk or a scheduling gap is **NOT-ADJUDICATED** from inside SHADE's tree.
2. **`PRED-006`'s MBA Q2 window (~2026-09-mid) is now.** I could not determine whether the print has landed. **CANNOT-EVALUATE** without an external source.
3. **Is the FIRED-triad ask (#2) actually still open?** `CLAUDE.md:82` carries a counted standing form; `REFERENCE.md §10b` still says 🔴 OPEN. One of the two is stale.
4. **How light should the predictions ledger be?** The old profile's own caution stands: a full directional calibration scoreboard is lower-value for a watch agent than for a directional one. The risk of over-building is real; the risk of the current state is that **every session adds an ungraded binary** (`STATUS.md:135`).
5. **Does NEXUS actually consume SHADE's brief?** The brief exists and is folded last, correctly. Whether it is read is outside SHADE's tree. **NOT-SEEN.**

---

# PART B — REFRESH REPORT · SHADE

## B1. Old-profile section disposition

Old profile = `AGENTS/DAEDALUS/profiles/SHADE.md` (body built 2026-06-28; three stacked Δ banners 7/22, 7/27, 8/11).

| Old section | Disposition | Evidence |
|---|---|---|
| Δ 2026-07-22 banner (production-review delta store) | **DROPPED — consumed.** Its own 45d clock expired 8/12 and was serviced by the 8/11 banner | `profiles/SHADE.md` banner 1 |
| Δ 2026-08-11 banner (clock serviced; light amend) | **CARRIED-VERIFIED as history; superseded by this draft.** Its three named facts all hold: the M-11 grade card exists at agent root, `NEXUS_BRIEF.md` is new anatomy, ARCC graded 0-of-4 | `2026-08-04_athene-q2-m11-grade-card.md`; `NEXUS_BRIEF.md`; `STATUS.md:91` |
| Δ 2026-08-11 **RE-STAMP trigger** (*"refresh when a PREDICTIONS/grade-card LEDGER file appears … or at the L4 assessment, or hard floor 2026-09-15"*) | **FIRED ON THE FLOOR LEG.** The ledger leg has **still not fired** — `find AGENTS/SHADE -iname '*PREDICT*'` returns nothing; the only TSVs are `board_log.tsv` and `registry/corrections_receipts.tsv`. **Floor 2026-09-15 passed 2 days ago.** This draft is the response | `find`/`ls` at HEAD; today 2026-09-17 |
| Δ 2026-08-11 *"SHADE itself hasn't run since ~8/3"* | **UPDATED — it ran, then stopped again.** SHADE self-authored ~20 commits on 2026-08-28 (a five-touch Will-directed session) and **nothing since** | `git log` `e0177eefc` … `c639efa8f`, all 2026-08-28 |
| Δ 2026-07-27 banner (L2→L3 promotion, vector #1 FIRING, composite 19→20/30) | **CARRIED-VERIFIED.** Vector #1 still FIRING at 5 🔴🔴; composite still **20/30**, explicitly `unchanged 8/28` | `STATUS.md:61`, `:71` |
| Header *Staleness: refresh when §3 dashboard gains a 5-pt handle or a PREDICTIONS ledger appears, or >45 days* | **UPDATED.** The **5-pt-handle leg HAS FIRED** — §3 now opens *"Convergence index (5-pt stackable handle)"* with an Independence column. The >45d leg fired long ago. Only the ledger leg is unfired | `STATUS.md:57-70` |
| §1 Identity | **CARRIED-VERIFIED** in full — domain, class, transmission targets, SHADE-canonical ownership, core question all hold | `CLAUDE.md:4-9`, `:147-151` |
| §2 anatomy — `CLAUDE.md (132 ln)` | **UPDATED → 170 ln / 22,082 B.** New: §REGISTERED TRIGGERS `:64-87` (T-SHADE-01), read-cap discipline `:106`, the `REFERENCE.md` on-demand rule `:111`, R1 corrections step `:122`, byte-budget closeout rule `:132` | `wc`; `CLAUDE.md` as cited |
| §2 anatomy — `STATUS.md (237 ln, <cap)` with §0/§0a RETRACT discipline, §1-§10 | **UPDATED — structure rewritten 2026-08-28.** Now **150 ln / 32,462 B**; §0 is a *where-everything-is* rotation receipt, §0a is gone (retired to `archive/STATUS_section0_deltas_retired_2026-07-27.md`), §0l is the new live-rails block, §2 and §5 have **moved to `REFERENCE.md`**. §3/§4/§6/§7/§10/BOTTOM LINE survive in place | `STATUS.md:12-26`, `:30`; `archive/` listing |
| §2 anatomy — `research/ATHENE_FABN_MATURITY_LADDER` "crown jewel" | **CARRIED-VERIFIED and extended.** The NPORT method was **re-run 2026-08-28** with 4 script defects fixed (3 from a DAEDALUS sweep, 1 found at commit): 53 funds / 492 holdings / 0 failures, penalty **+37.8bp**, landing **2bp from Athene's own deck** | `STATUS.md:134`; `research/FABN_PEER_SPREAD_NPORT_RERUN_2026-08-28*` |
| §2 anatomy — `research/INSURER_LENDER_DOUBLE_JEOPARDY` | **CARRIED-VERIFIED**; `research/` has grown from 2 files to **19** | `git ls-files AGENTS/SHADE/research/` |
| §2 anatomy — `domain/sources/01-08`, Mar'26 vintage stale-flagged | **CARRIED-VERIFIED — and still >90d stale**, now flagged in STATUS itself | `STATUS.md:8` |
| §2 anatomy — `sources/athene_statutory_2026-06-15/` + MANIFEST | **CARRIED-VERIFIED** | `git ls-files` |
| §2 anatomy — `MEMORY.md, board_log.tsv, SCRATCH.md` | **UPDATED.** MEMORY now 31,745 B with a rotated-lessons index `:56`; board_log has grown **10 → 97 rows**; SCRATCH is now formally the canonical handoff | `wc`; `CLAUDE.md:162` |
| §2 anatomy — **missing rows** | **ADDED:** `REFERENCE.md`, `NEXUS_BRIEF.md`, `instruments/`, `registry/`, `archive/` crc32 set, the root grade card | listed in PART A §2 |
| §3 Thesis structure row | **CARRIED-VERIFIED and extended** — transmission map gained stage 4b | `STATUS.md:83-85` |
| §3 Convergence row: *"per-vector emoji state machine … **no 5-pt / composite / Independence column**"* | **REFUTED.** All three are present: 5-pt stackable handle, **composite 20/30** over SHADE-owned independent roots, and an **Independence column** with shared-antecedent flags | `STATUS.md:57-71` |
| §3 Invalidation row: *"… **no standing FIRED-count triad**"* | **REFUTED in substance.** `CLAUDE.md:82` carries a counted standing form — **4-for-4 NOT MET** — plus a dated latest reading and an explicit fired-state. The *table* shape asked for does not exist; the *count* does | `CLAUDE.md:78`, `:82`, `:85` |
| §3 Thresholds row (durable-vs-live split, conformant) | **CARRIED-VERIFIED and strengthened** by the explicit environment-band vs trigger-leg non-conflict note | `CLAUDE.md:87` |
| §3 Predictions row: *"(none — grep-confirmed absent) … no ledger/calibration"* | **TRUE-STILL, re-verified by grep at HEAD.** Now additionally self-flagged 🔴 by the desk in three places | `find` returns none; `STATUS.md:135`; `SCRATCH.md:42`; `REFERENCE.md §10b:7` |
| §3 Cross-agent row: *"conditions + deps table + crisis-only outbox; NEXUS_BRIEF specced-but-deferred"* | **UPDATED.** NEXUS_BRIEF is **built and standing** since 2026-08-03; the deferral is explicitly CLOSED in the charter. §7 gained the CCC one-owner-each reconcile and an independence bar | `CLAUDE.md:102`, `:141`; `STATUS.md:115-120` |
| §4 Deviations — *"NPORT-P reconstruction genuinely novel"* | **CARRIED-VERIFIED** | as above |
| §4 Deviations — *"Held below L3 by HANDLES not substance … missing: 5-pt matrix, predictions ledger, standing exit-triad, trailing BOTTOM LINE"* | **THREE OF FOUR RESOLVED.** 5-pt matrix ✅, exit-triad ✅ (counted form), **BOTTOM LINE ✅ present and dated**; only the predictions ledger remains | `STATUS.md:57`, `CLAUDE.md:82`, `STATUS.md:146-150` |
| §4 *"Verifier called the grade generous, not overstating"* | **CARRIED as history** | — |
| §5 DO-NOT-TOUCH — §0/§0a boot-delta verified-threshold table | **DROPPED — the structure no longer exists.** §0a was retired 2026-07-27 to `archive/STATUS_section0_deltas_retired_2026-07-27.md`; §0 was replaced 2026-08-28 by the rotation receipt. The *discipline* (RETRACT/DOWNGRADE framing) survives in MEMORY and in the 8/28 self-corrections, not as that table | `git ls-files AGENTS/SHADE/archive/`; `STATUS.md:12-26` |
| §5 peer-relative spread sub-row canary | **CARRIED-VERIFIED** | PART A §5 item 10 |
| §5 trigger-gated pre-registered dig lane (§10 item 6) | **CARRIED-VERIFIED** — still §10 item 6, still deploy-on-trigger, ordered a→d, with the live not-armed reading in-row | `STATUS.md:137` |
| §5 144A / NPORT-P methodology + reusable crawler | **CARRIED-VERIFIED** | `research/` |
| §5 BROCK boundary + SHADE-canonical ownership | **CARRIED-VERIFIED** | `CLAUDE.md:15-22` |
| §5 obs-date + unit tagging; mechanism-vs-thermometer | **CARRIED-VERIFIED** | `REFERENCE.md` §2 |
| §5 statutory provenance tree | **CARRIED-VERIFIED** | `sources/.../MANIFEST.md` |
| §6 Maturity snapshot *"L2 (conf H)"* | **REFUTED as written** (superseded by the 7/27 banner's L3 and by the FLEET_MAP row). PART A defers to FLEET_MAP rather than restating | `FLEET_MAP.tsv` SHADE row |
| §7 open question — *watch-agent cadence, keep the ledger LIGHT* | **CARRIED-VERIFIED — still the live design question** | PART A §7.4 |
| §7 open question — *APO threshold band self-flagged stale; confirm refresh owner* | **UPDATED.** APO band still in the environment table (`CLAUDE.md:62`) with no stamp; but MEMORY's mechanism-vs-thermometer rule already says **APO price is NOT a SHADE stress gauge**, so the band's staleness is low-stakes. Folded into flag H4 rather than carried as an open question |
| §7 open question — *NEXUS_BRIEF specced-but-deferred; confirm whether NEXUS consumes SHADE* | **HALF-RESOLVED.** Built and standing; consumption still **NOT-SEEN** | `CLAUDE.md:141` |

## B2. File tree at HEAD

`git ls-files AGENTS/SHADE/ | wc -l` = **162**.

| Cluster | Files | Note |
|---|---|---|
| root `.md` | 11 | incl. the M-11 grade card and `ARCH_REPORT_2026-06-26.md` |
| `inbox/` | 55 | `inbox/WALTER/processed/` 32 · **`inbox/WALTER/` top-level 14 UNPROCESSED** · `inbox/processed/` 24 |
| `research/` | 19 | 15 `.md` + 2 `.py` + 3 `.json` (the only executable code on the desk) |
| `archive/` | 17 | incl. the 3 crc32 pre-rotation files + `tmp_aaia_extract/` |
| `domain/sources/` | 8 | Mar'26 KB library |
| `sources/athene_statutory_2026-06-15/` | 9 | 8 raw text + MANIFEST |
| `outbox/` | 7 + `delivered/.gitkeep` | |
| `instruments/` | 1 | the canary spec |
| `registry/` | 1 | corrections receipts, 1 data row |
| `board_log.tsv` | 1 | 97 rows |

**Boot-read surfaces, measured** (`scripts/read_cap_check.py --agent SHADE`, budget 32,550 B):

| Surface | Bytes | % of budget | Verdict |
|---|---|---|---|
| `STATUS.md` | 32,462 | **100%** | 🟡 rotate-tier — needs **9,678 B more removed** to reach the <70% stop |
| `MEMORY.md` | 31,745 | **98%** | 🟡 rotate-tier — needs **8,961 B more removed** |
| `NEXUS_BRIEF.md` | 13,145 | 40% | ✅ |
| `SCRATCH.md` | 10,288 | 32% | ✅ |

`READ-CAP-RESULT v1 mode=agent rc=0 desk=SHADE reads=4 over_budget=0 over_cap=0`. **rc=0 and two surfaces at 98-100% are not in tension** — the tool's rc grades *over-budget*, the 🟡 grades *rotate-tier*. ⚠️ The desk's charter (`CLAUDE.md:142`) requires `rc must be 0` at every closeout, which is satisfied — and which is exactly why a 100%-of-budget STATUS can sit unaddressed. See flag H2.
`ledger_staleness.py SHADE` → `no ledgers matched workbook/*.tsv` — **the absence is the finding**, not a pass.

## B3. Period activity (2026-09-01 → 2026-09-17)

| Metric | Value |
|---|---|
| Commits touching `AGENTS/SHADE/` | **11** |
| **Self-authored** | **0** |
| Routed-in | **11 — all WALTER** (`5f146edb8` 9/1 … `0951f361e` 9/15) |
| **Last self-authored commit** | `e0177eefc` **2026-08-28** — *"SHADE (orch): closeout receipt — step-by-step results, the two defects the re-run caught, and the three enumerated lists"* |
| **Dark days since last self-commit** | **20** |
| `STATUS.md` delta since `e6fc35eaf` (9/1 base) | **ZERO** — the file has not been touched in the period |
| Last STATUS stamp | `2026-08-28 ~20:55 ET` (`STATUS.md:3`) |

The 2026-08-28 session itself was substantial (≈20 commits, five touches, Will-directed via PROME): Delaware Life Q2 statutory pulled at primary and a pre-pause flow baseline built, T-SHADE-01 registered canonically after 15 days with no charter locus, the NPORT rerun, AG 55 re-based at NAIC primary, the CCC reconcile closed, and the P1 read-cap rotation. **Everything in the period is inbound signal; nothing is desk output.**

## B4. Open questions I could not settle

1. Whether `PRED-006`'s MBA Q2 print (due ~2026-09-mid, i.e. now) has landed. **CANNOT-EVALUATE** — needs an external source.
2. Whether the FIRED-triad ask is open or closed — `CLAUDE.md:82` and `REFERENCE.md §10b:8` disagree. **NOT-ADJUDICATED**; it is an owner call which form counts.
3. Whether SHADE's 20-day dark period is correct cadence for a latent-vector watch desk. **NOT-ADJUDICATED** from inside the tree.
4. Whether NEXUS reads the brief. **NOT-SEEN.**
5. Whether the FY2025 DLIC annual statement (SCRATCH item 0, "one fetch, highest value available") has been attempted since. No artifact in `research/`. **NOT-SEEN**, not 0.

## B5. Flags for the OWNER (SHADE), each verified at the artifact

| # | Sev | Flag | Verified at |
|---|---|---|---|
| **H1** | 🔴 | **14 WALTER signals sit unprocessed in `inbox/WALTER/`, spanning 2026-08-28 → 2026-09-15, with no board_log row and no `git mv`.** Under the desk's own boot step 4a this is the first thing a session does. Several are directly on SHADE's live rails — `SIG-W-20260903-006` (August office CMBS DQ printed **exactly 12.00** against a `>12` band; *"six desks hold the spec that makes it look fired"*), `SIG-W-20260903-009` (the BCRED filing type *"does not exist … structurally impossible, not merely old"*), `SIG-W-20260901-001` (alt managers −3 to −5% on a global bond-selloff day — **that is a sign-leg-relevant tape day for T-SHADE-01**). | `ls AGENTS/SHADE/inbox/WALTER/*.md` = 14; `board_log.tsv` last row 2026-08-28T23:07Z; `CLAUDE.md:118-121` |
| **H1b** | 🟠 | **One of those 14 is logged under a DIFFERENT id than its filename, so the desk's own membership test will re-pick it forever.** `board_log.tsv` carries `2026-08-28_from-WALTER_NOTE-delaware-life-clear-spring-denominators` (disposition `deferred`); the file on disk is `2026-08-28_from-WALTER_NOTE-delaware-life-**and**-clear-spring-**asset**-denominators.md`. Boot step 4a matches on *exact* `signal_id`, so this file reads as unconsumed on every boot. SCRATCH already lists "formally consume" as NEXT SESSION item 1 — the fix is the `git mv` **and** an id that matches. | `board_log.tsv` final row vs `ls inbox/WALTER/`; `CLAUDE.md:119`; `SCRATCH.md:36` |
| **H2** | 🔴 | **`STATUS.md` is at 100% of the read budget and `MEMORY.md` at 98% — both rotate-tier — and the charter's own closeout gate cannot see it.** `CLAUDE.md:142` requires `rc must be 0`, and rc **is** 0, because rc grades over-*budget* while these two sit exactly at it. The next append to either file breaches. The desk's own §0 standing rule ② says run the check at every closeout; the check passes and the problem is real. Recommend the closeout gate read the **tier**, not just rc: `STATUS.md` needs **−9,678 B**, `MEMORY.md` **−8,961 B** to reach the <70% stop. | `read_cap_check.py --agent SHADE`; `CLAUDE.md:142`; `STATUS.md:26` |
| **H3** | 🔴 | **`PREDICTIONS.tsv` is still absent — untouched across six sessions by the desk's own count — and the period added nothing to change that.** It is the single named L4 blocker in three places. Meanwhile dated, confidence-bearing binaries keep accruing with no scoring surface: `PRED-006` (65%→30%, bar ≥+$10.0B as printed, **window is now**), the supply-adjusted canary (`REGISTERED, NOT YET GRADED`), the C2 self-executing withdrawal (2026-11-18), the ladder's Q3 dated step (~2026-11-15). | `find AGENTS/SHADE -iname '*PREDICT*'` → none; `STATUS.md:135`, `:98`, `:99`, `:101`; `SCRATCH.md:42`; `REFERENCE.md §10b:7` |
| **H4** | 🟠 | **Three stale statements sit in the charter, the file a fresh session reads first.** (a) `CLAUDE.md:100`: *"SHADE is currently in architecture catch-up mode: `STATUS.md` is stale to Mar 26"* — STATUS was rewritten 2026-08-28; (b) `CLAUDE.md:108` repeats *"Treat any March price/position row as historical"* — no March rows survive the rotation; (c) `CLAUDE.md:154`: *"If future `domain/sources/` scaffolding is built, update this pointer"* — `domain/sources/01-08` has existed since before the profile's own 2026-06-28 build. A charter that describes a state two rotations old is the header-edit-as-maintenance failure. | `CLAUDE.md:100`, `:108`, `:154`; `STATUS.md:3`; `git ls-files AGENTS/SHADE/domain/sources/` |
| **H5** | 🟠 | **Kill-path #1's only in-content stamp is `6/22`** — *"(Currently YELLOW per 6/22 ladder …)"* — while its own instrument was re-run 2026-08-28 (+37.8bp, T+112.0 vs peer median T+74.2) and a companion canary spec was registered 8/13. Paths #2-#4 carry **no stamp at all**. For a Market-class desk whose L3 leg is a *dated* falsification surface, the kill paths are the surface and three of four are undated. Cheap fix: one `[as of YYYY-MM-DD]` per path. | `CLAUDE.md:49-52`; `STATUS.md:134`; `instruments/…SPEC_2026-08-13.md:3` |
| **H6** | 🟠 | **`REFERENCE.md §10b` ask #2 still reads 🔴 OPEN while `CLAUDE.md:82` carries the counted form it asked for (4-for-4).** One surface is stale relative to the other. Either mark #2 satisfied-in-counted-form, or state why a table is still owed — a 🔴 that has silently been answered trains the reader to skip the list. | `REFERENCE.md §10b:8` vs `CLAUDE.md:82` |
| **H7** | 🟡 | **`domain/sources/01-08` are Mar'26 vintage, >90 days past the charter's own 60-day `LAST_REVIEWED` rule** (`CLAUDE.md:139` closeout step 10a). They are correctly stale-flagged at `STATUS.md:8`, so nothing is being cited as current — but the retirement scan the charter mandates has not dispositioned them. Flag-or-archive, don't leave them in the middle state. | `CLAUDE.md:139`; `STATUS.md:8` |

### FALSE-POSITIVE-CANDIDATEs (SHADE) — candidate flags I could NOT verify as defects

- **FALSE-POSITIVE-CANDIDATE — "SHADE is a Market agent with no falsification surface (L3 gap)."** `falsification_scan.py` puts SHADE in the *"MARKET AGENT, NO THESIS-CLASS FILE AND NO SURFACE THIS SCAN CAN SEE"* bucket, and the tool's own text says to hand-verify because that bucket historically contained 4 real rails and 3 real gaps. **Hand-verified: SHADE has rails** — 4 kill paths (`CLAUDE.md:48-52`), a fully-specified two-leg trigger with a counted fired-state (`CLAUDE.md:64-87`), a 7-marker escalation ladder with a dated first step (`STATUS.md:95-96`), a self-executing withdrawal test (`STATUS.md:101`) and a shared ordering test (`STATUS.md:102`). They live in `CLAUDE.md` and `STATUS.md` §6, which the scan's pattern set cannot reach. **Not an owner defect; a scanner/registry gap.** PART A §3b supplies the inventory.
- **FALSE-POSITIVE-CANDIDATE — "SHADE has no ledgers (ledger_staleness returns nothing)."** True as printed, but `ledger_staleness.py` scans `workbook/*.tsv` and SHADE has no `workbook/`. Its two TSVs (`board_log.tsv`, `registry/corrections_receipts.tsv`) are correctly out of scope. The real ledger gap is H3, which this tool cannot see. Reporting the tool's silence as a pass would be the exact instrument-reports-clean-against-the-wrong-reference failure.
- **FALSE-POSITIVE-CANDIDATE — "`STATUS.md` is 20 days stale."** It is 20 days old, but it is **correctly stamped** (`:3`), its live rails are dated in-block (`:30-43`), its tape row says *"2026-08-28 closes, dated, final-for-period"*, and nothing in it asserts current-as-of-today. An unrefreshed-but-honestly-dated surface is not rot. The finding is the **dark period** (B3), not the file.
- **FALSE-POSITIVE-CANDIDATE — "`T-SHADE-01`'s sign-leg reading is stale (8/13→8/28 window)."** The charter pre-empts this: the sign leg *"IS A DATED READING, NOT A STANDING STATE"* (`CLAUDE.md:81`), and a fresh read is obliged **only on a level-leg crossing**. The level leg was 17bp below the bar at last measurement and no SHADE session has run since, so no obligation has been triggered *on SHADE's own surface*. ⚠️ But I could not check whether HY OAS has since crossed 280 — **CANNOT-EVALUATE**; if it has, H1's unread `SIG-W-20260901-001` is the tell and this becomes a real 🔴.

### Reviewer-side findings — DAEDALUS's own map/profile is wrong

| # | Finding | Evidence |
|---|---|---|
| **R4** | **The old SHADE profile's §3 row *"no 5-pt / composite / Independence column"* and §4's missing-handle list are REFUTED at HEAD** — three of the four named gaps closed on 2026-07-27 and 2026-08-28. The profile's own 8/11 banner correctly said "read with the deltas", but the body has been wrong-on-its-face for ~7 weeks and the deltas live in a separate file. **This is the cost of light-amend-at-touch on a body that keeps being cited whole.** | `profiles/SHADE.md` §3, §4; `STATUS.md:57-71`, `:146-150`; `CLAUDE.md:82` |
| **R5** | **The FLEET_MAP SHADE `Gaps` cell (Last_scored 2026-09-01) is accurate and unusually good — including its own self-criticism** (*"Profile NOT FIRED (floor 9/15) but MIS-SPECIFIED"*). One leg has since turned: **the 9/15 floor has now PASSED**, so the row's parenthetical is stale by 2 days. Everything else in it verifies. | `FLEET_MAP.tsv` SHADE row col 7; today 2026-09-17 |
| **R6** | **`profiles/SHADE.md` carries three stacked Δ banners above a body none of them replaced, and the newest points at a fourth file (`upgrades/PRODUCTION_REVIEW_2026-07-22.md`) as "the delta store."** A reader must assemble four documents to know what SHADE is. Recommend PART A replace the body outright rather than adding a fourth banner — the banner stack is itself the finding. | `profiles/SHADE.md:3-7` |

---

## Cross-desk note (both desks, one observation)

Both profiles' staleness triggers were written as **prose with an "or >N days" escape**, and in both cases the substantive leg had either become un-fireable (SAM's "FXY modal band re-derived" — the band's document is bannered historical) or silently unfired for months while a *different* leg did all the work (SHADE's floor). PART A gives both desks **file-readable triggers only**: a named artifact plus a condition a shell one-liner can evaluate. Per PAT-089's fix-form, and per the SHADE row's own *"MIS-SPECIFIED"* self-criticism on the FLEET_MAP.

**Reader:** P3 (SAM · SHADE), DAEDALUS fan-out 2026-09-17. Read-only; this file is the only write.
