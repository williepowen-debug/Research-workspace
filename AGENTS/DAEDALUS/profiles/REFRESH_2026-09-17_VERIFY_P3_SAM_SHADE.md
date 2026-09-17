# INDEPENDENT LOCATOR VERIFICATION — P3 (SAM · SHADE)

**Verifier:** second reader, 2026-09-17 (Thu). Read-only; this file is the only write.
**Subject:** `AGENTS/DAEDALUS/profiles/REFRESH_2026-09-17_READER_P3_SAM_SHADE.md` — PART A for SAM and PART A for SHADE.
**Method:** every claim naming a file, line, section, count, byte size, date, version, script, column or behaviour was opened at the artifact. Bytes by `wc -c`, lines by `wc -l`, counts by `grep -c`/`awk`, tree by `git ls-files`, script behaviour by reading the code. Nothing was executed that writes. Read-cap figures are from `python3 scripts/read_cap_check.py --agent <X>` (read-only).

**Verdicts:** VERIFIED (matches) · FAILED (artifact says otherwise) · DRIFTED (true, locator/count off — correct one given) · UNLOCATED (no locator and not findable in ≤2 tries).

---
---

# ═══ DESK 1 of 2 — SAM ═══

## 1. Verification table — SAM PART A

| § | Claim (≤20 words) | Verdict | Correction |
|---|---|---|---|
| Header | Staleness (a): `thesis/THESIS.md:1` reads `# SAM THESIS — v1.7` | **VERIFIED** | — |
| Header | Staleness (b): `red/CHALLENGES.md:3` carries `Last RED sweep:` | **DRIFTED** | `:3` is `**Last real data refresh:** 2026-08-20`; `Last RED sweep: 2026-08-20` is at **`:4`** |
| Header | Staleness (c): OPEN set exactly {SAM-28,31,33}; `STATUS.md:9` same count | **VERIFIED** | `awk -F'\t' '$6=="OPEN"'` → SAM-28/31/33; `STATUS.md:9` = "16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN (SAM-28/31/33)" |
| Header | Staleness (d): `git log -1 %cs STATUS.md` >45d after 2026-09-17 | **DRIFTED** | Semantically a date floor, not a file property — restated as hard floor **2026-11-01** |
| §1 | Class Market from `FLEET_MAP.tsv` SAM row | **VERIFIED** | row = SAM / Market / L4 / H / ROSTER:active / 2026-09-01 |
| §1 | `CLAUDE.md:3-10` domain + three channels | **VERIFIED** | `:3` Domain; `:10` the three channels |
| §1 | Sends `CLAUDE.md:190-205`; receives `:207-212` | **VERIFIED** | — |
| §1 | `STATUS.md:5` + `THESIS.md:1-6` — no live frame, FLAT, no successor | **VERIFIED** | — |
| §2 | 818 tracked files | **VERIFIED** | `git ls-files AGENTS/SAM/ \| wc -l` = 818 |
| §2 | "~470 are `inbox/WALTER/processed/`; ~90 are `archive/`" | **FAILED** | `inbox/` = **218** total (`inbox/WALTER/processed/` = **141**); `archive/` = **74**. The largest cluster is **`research/` = 312** (308 under `research/outputs/`), which the profile never mentions |
| §2 | `CLAUDE.md` 294 ln / 37,570 B | **VERIFIED** | — |
| §2 | WALTER intake § at `CLAUDE.md:52-65` | **VERIFIED** | — |
| §2 | doc-ownership matrix at `CLAUDE.md:118-127` | **FAILED** | `:118-127` is the signal-writing / `AGENTS/SIGNALS.md` block. The ownership matrix is the **FILES table, `CLAUDE.md:235-277`** |
| §2 | MANUAL-ONLY script exception list `CLAUDE.md:269` | **VERIFIED** | six scripts, count self-corrected in-row 2026-08-27 |
| §2 | STATUS 131 ln / 21,720 B = 67% of 32,550 B | **VERIFIED** | read_cap_check: 21,720 B, 67% |
| §2 | STATUS anchors `:3-13`, `:28-52`, `:65-82`, `:84-95`, `:116-127` | **VERIFIED** | headings at 28, 65, 84, 116 |
| §2 | `STATUS_REFERENCE.md` 52 ln / 8,109 B, born 2026-09-11 (`a9afd4701`), `:8` | **VERIFIED** | `:3` split-out note; `:8` "current and citable"; commit subject matches |
| §2 | `STATUS_ARCHIVE.md` 116,632 B, split 2026-09-01, `:3` read-cap derivation | **VERIFIED** | — |
| §2 | THESIS v1.7, 65,371 B; `:1-32`, `:155-183`, `:190-212`, `:238-247` | **VERIFIED** | every heading boundary checked |
| §2 | Candidates 13/17/8/2 KB; `STATUS.md:11` v1.8 separate; `:5` v2.0 KILLED | **VERIFIED** | 13,088 / 17,265 / 8,370 / 2,378 B |
| §2 | PREDICTIONS 89,614 B · 34 data rows · 9 cols | **VERIFIED** | header `Pred_ID…Notes` at `:40`, 34 `SAM-NN` rows |
| §2 | "19-line `#`-comment preamble"; HIGH-CONFIDENCE FAILURES `:20-30` | **DRIFTED** | preamble is **39 comment lines (`:1-39`)**; the FAILURES block `:20-30` is correct |
| §2 | Pre-registrations 21/31/7/13/10 KB | **VERIFIED** | 21,228 / 30,827 / 6,534 / 13,280 / 9,560 B |
| §2 | `thesis/CHANGELOG.md` 208,580 B | **VERIFIED** | — |
| §2 | TIMELINE "~96 KB per `CLAUDE.md:25`" | **DRIFTED** | `CLAUDE.md:25` does say 96 KB, but the file is **104,615 B** — the charter figure is stale by ~8.6 KB |
| §2 | TRADE 50,247 B / STRATEGY 71,548 B, banners `:3-8` | **VERIFIED** | both `:3` = "⚰️ THIS DOCUMENT IS HISTORICAL AS OF 2026-08-07. DO NOT TRADE OFF IT." |
| §2 | MOF playbook `:1-8` = S1/S1-A ladder | **DRIFTED** | `:1-8` is the header block; **S1 at `:12`, S1-A at `:65` / `:67`** |
| §2 | 19 root TSVs; 11 script-written, 4 FROZEN, 2 ARCHIVE | **VERIFIED** | 19 root TSVs; FROZEN = BOJ_OIS/FLOW/VX/XCCY_BASIS; ARCHIVE = FLOW_ARCHIVE/KB_ARCHIVE; 10 auto-pulled at `CLAUDE.md:268` + `BIS_GLI` |
| §2 | KB 207,971 / MOF_FLOWS 94,513 / KURA_MEMORY 209,222 B | **VERIFIED** | — |
| §2 | `LEDGER_CADENCE.md` 3,419 B, per-ledger class + observation + next check | **VERIFIED** | — |
| §2 | "`scripts/` — 24 py + `lib/` + `tests/`" | **DRIFTED** | **21 top-level `.py`**; 26 `.py` incl. `lib/` (1) + `tests/` (4); 28 files in `scripts/` |
| §2 | `boot.py:63-77` = 13-entry BOOT_SEQUENCE | **VERIFIED** | exactly 13 tuples, `:64-76` inside the literal |
| §2 | red files 61.5 / 25.1 / 18.2 KB; 17 keys, 3 OPEN, 14 CLOSED (`red/LOG.md:7`) | **VERIFIED** | 61,554 / 25,070 / 18,243 B; `LOG.md:7` = "17 keys · 3 OPEN · 14 CLOSED" |
| §2 | docket 9 files; CATALYSTS 31 rows; review packet prepared 9/9 | **VERIFIED** | CATALYSTS = header + 31 data rows |
| §2 | `insurers/TRACKER.md:3` refreshed 2026-09-14; 8 files | **VERIFIED** | — |
| §2 | 6 pair-files; KOYOMI 21 / METSUKE 20 / KURA 16, all 2026-09-11 | **VERIFIED** | 3 spec+memory pairs = 6 (plus 4 `*_ARCHIVE`); `056bb0f78`, `a7fc09dbd` both 2026-09-11 |
| §3 | THESIS `:8-32` / `:155-183` / `:190-212` per-dimension anchors | **VERIFIED** | — |
| §3 | "deliberately blank successor — § WHAT REPLACES IT left empty (`:14-15`)" | **FAILED** | `## WHAT REPLACES IT` is at **`THESIS.md:221`** and is **populated** — two questions, each with a named owner. What is deliberately blank is the successor **frame**, stated at `:13-15` and `:6` |
| §3 | THESIS `:55-67` / `:127-142` HISTORICAL; buckets 8/07 (`STATUS.md:57`) | **VERIFIED** | `:55` heading literally "(v1.6; not fresh probabilities)" |
| §3 | THESIS `:86-99` SPF, `:100-109` LOCKED window, `:143-154` sensitivity | **VERIFIED** | — |
| §3 | `CLAUDE.md:218` "Current values live in STATUS.md"; `STATUS.md:67` WQ-162 basis | **VERIFIED** | — |
| §3 | Scoreboard 16/14/1/3 "reconciles exactly against the row set" | **VERIFIED** | 12 `CONFIRMED` + SAM-30/38 `RESOLVED` + SAM-39/41 `RESOLVED CONFIRMED` = 16; 14 FAILED; SAM-25 special; 3 OPEN = **34** |
| §3 | `CLAUDE.md:190` Target column relabelled; `NEXUS_BRIEF.md:3` provenance | **VERIFIED** | `:190` "names who must ACT … NOT a delivery address"; brief `:3` carries `17873d941` |
| §3 | `STATUS.md:131` = one-line pointer end-cap | **VERIFIED** | last line: "Thesis v1.7 → …; No successor declared." |
| §3b | THESIS `:3` "Current integration — September 15, 2026"; `:6` retirement record | **VERIFIED** | — |
| §3b | THESIS `:22-24` SAM-28 grading horizon | **VERIFIED** | — |
| §3b | Channel 1 re-add condition restated `STATUS.md:103` | **VERIFIED** | — |
| §3b | Preamble `# As of 2026-09-10` at line 3; SAM-33 activation stamp 8/17 in Notes | **VERIFIED** | — |
| §3b | Retired gates written **VOID** in-row (`STATUS.md:71`, `:81`) | **DRIFTED** | Only `:71` uses "VOID" (USDJPY 160). `:80` reads "Fired Aug-7"; `:81` reads "No rearm". Substance (written-in-place, not deleted) holds |
| §3b | `red/CHALLENGES.md:3` / `:4` stamps; rail state `:6-10` | **VERIFIED** | — |
| §3b | `red/COUNTER_THESIS.md:3` / `:4`; frozen banner `:6-7`; table `:9-14` | **VERIFIED** | `:7` quote "kept verbatim … Cite it as history" confirmed |
| §3b | `docket/2026-09-18_SAM28_SAM31_REVIEW.md:1` "prepared September 9" | **VERIFIED** | plus "Preparation only" and source SHA256 |
| §3b | MOF playbook `:7` "September 8 integration"; live marks → `STATUS.md:59-63` | **VERIFIED** | — |
| §4 | `STATUS_REFERENCE.md:3-8` three-tier split rationale | **VERIFIED** | — |
| §4 | `CLAUDE.md:269` manual list / `:270` forbids hand inventory | **VERIFIED** | — |
| §4 | Second roller built off a measured **179K→50K** spawn read (`CLAUDE.md:269`) | **VERIFIED** | `:269` "First run: 179K → 50K, zero proposal IDs lost" |
| §4 | `red/` is contractually un-editable by SAM (`CLAUDE.md:261`) | **VERIFIED** | — |
| §5 | `TRADE.md:72` $58.32 Will's ground truth; `TRADE.md:51` FLAT 2026-06-29 | **VERIFIED** | — |
| §5 | METSUKE "contractually barred from even flagging" money fields (`METSUKE.md:74`) | **DRIFTED** | `:74` forbids **editing** ("FORBIDDEN"); flagging is graded "**risky**", not barred |
| §5 | PREDICTIONS preamble `:1-30` | **DRIFTED** | preamble runs `:1-39` |
| §5 | `STATUS.md:7` R = −188,077, "25.3% of −180K" retired, Will-ratified 8/11 | **VERIFIED** | — |
| §5 | Two named redirects `STATUS.md:108-114`; WALTER checklist §v0.30 | **VERIFIED** | `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` exists, "v0.30" ×2 |
| §5 | PROME inbox rule at `CLAUDE.md:97` | **FAILED** | The rule is at **`CLAUDE.md:114`**. `:97` is boot step "Assess thesis impact" |
| §5 | CH-0NN citation collision `red/CHALLENGES.md:12` | **VERIFIED** | — |
| §7 | Open Q3: `boot.py --predictions` vs `CLAUDE.md:27` — "CANNOT-EVALUATE without running the tool" | **FAILED — SETTLED BY READING** | The instrument exists. `boot.py:296` defines `--predictions`; `boot.py:315-321` calls `prediction_report()`; `scripts/lib/boot_context.py:36-53` reads and schema-validates `thesis/PREDICTIONS.tsv`; `:156-176` emits OPEN rows + sidecar diagnostics vs `docket/PREDICTION_SCHEDULE.json`. **`CLAUDE.md:27`'s "zero scripts read the file … a `predictions_due()` leg in `boot.py` is queued" is FALSE at HEAD.** No tool run needed — see new flag **S7** |
| B5-S1 | CH-017 criteria `:217`, Status `:219`; SAM-41 resolved 2026-08-19; USD/JPY 154.31/154.82 | **VERIFIED** | all four legs confirmed at the artifact |
| B5-S2 | `red/CHALLENGES.md:7`, `:59` bright line, `:63` DISMISS legs; `STATUS.md:44` | **VERIFIED** | `:44` does contain "Sep-3 30Y SOFT remains PRECISION-LIMITED" |
| B5-S3 | `SIGNAL_INTAKE.md:3,5`; MEMORY DEFERRED block | **VERIFIED** | `:3` "thesis now v1.6.9 … spot now 163.16"; `:5` Last Updated 2026-04-08; `MEMORY.md:89` DEFERRED |
| B5-S4 | `ledger_staleness.py SAM` → GPIF_FLOWS ⚠️ STALE +39d vs `LEDGER_CADENCE.md:15` | **VERIFIED** | both reproduced |
| B5-S5/S6 | `STATUS.md:131` vs `:3-13`; `STATUS.md:57`; `THESIS.md:55` | **VERIFIED** | — |
| B2 | read-cap table (3 reads, 21,720 / 21,373 / 8,109; rc=0) | **VERIFIED** | reproduced exactly, incl. the no-`READS.tsv` caveat |
| B3 | 101 commits / 67 self / 34 routed-in; last self `121233a0c` 9/15; delta +76/−192 | **VERIFIED** | all reproduced |

**SAM totals — VERIFIED 52 · FAILED 5 · DRIFTED 9 · UNLOCATED 0.**

## 2. New 🔴 the first reader missed (SAM)

| # | Sev | Finding | Locator |
|---|---|---|---|
| **S7** | 🔴 | **The charter tells every fresh session that its calibration step has no instrument, and that is false.** `CLAUDE.md:27` (boot step 6) asserts *"This step has NO INSTRUMENT (DAEDALUS 8/28, confirmed): zero scripts read the file, so a 70-row scan runs by eye every boot. A `predictions_due()` leg in `boot.py` is queued."* The leg was built and shipped: `scripts/lib/boot_context.py:36-53` reads, schema-validates and dedups `thesis/PREDICTIONS.tsv`; `:156-176` emits the OPEN-row report plus `docket/PREDICTION_SCHEDULE.json` sidecar diagnostics; `boot.py:296` and `:315-321` wire it as `--predictions` (`9899e223c`, 2026-09-09). `STATUS.md:118` already says so. A boot line that declares a working guard absent is the inverse of a decorative guard — it trains the reader to do by eye what the tool does mechanically. Fix: replace `CLAUDE.md:27`'s last two sentences with the invocation. | `AGENTS/SAM/CLAUDE.md:27`; `AGENTS/SAM/scripts/boot.py:296,315-321`; `AGENTS/SAM/scripts/lib/boot_context.py:36-53,156-176`; `AGENTS/SAM/STATUS.md:118` |
| **R7** | 🟠 (reviewer-side) | **The profile has no `research/` row at all, and `research/` is SAM's largest cluster by a factor of 1.4 over the next one.** 312 of 818 tracked files (38%), 308 of them under `research/outputs/` (per-run `manifest.json` / `review-draft.json` / `source.html` / `table.png` sets). It is load-bearing, not spoil: `CLAUDE.md:269` cites `research/outputs/2026-09-09_followthrough/ACTIVATION_DECISION_2026-09-11.md` as the xccy decline record, and `workbook/LEDGER_CADENCE.md:3,33` cites `research/outputs/2026-09-14_stale-sweep/` as its machine inventory and before-image. The draft's "~470 = the WALTER processed lane" mis-assigns this mass to `inbox/`. | `git ls-files AGENTS/SAM/ \| awk -F/ ...`; `AGENTS/SAM/CLAUDE.md:269`; `AGENTS/SAM/workbook/LEDGER_CADENCE.md:3,33` |
| **R8** | 🟡 (owner, cheap) | **`CLAUDE.md:268`'s "Auto-pulled" list omits `RATE_DIFFERENTIAL.tsv`**, written by `rate_differential.py`, which is entry 7 of BOOT_SEQUENCE (`boot.py:70`). The charter's own instruction ("verify against `boot.py --tools` rather than trusting this list") makes this non-fatal, which is exactly why it has not been noticed. | `AGENTS/SAM/CLAUDE.md:268`; `AGENTS/SAM/scripts/boot.py:70` |

## 3. Staleness-trigger evaluability — SAM

**YES — machine-evaluable from named artifacts, in one command, after the `:3`→`:4` fix and restating leg (d) as a date floor.** Verified to print `SAM PROFILE FRESH` at HEAD:

```sh
sed -n 1p AGENTS/SAM/thesis/THESIS.md | grep -q '^# SAM THESIS — v1.7' \
 && grep -q '^\*\*Last RED sweep:\*\* 2026-08-20' AGENTS/SAM/red/CHALLENGES.md \
 && [ "$(awk -F'\t' '$6=="OPEN"{print $1}' AGENTS/SAM/thesis/PREDICTIONS.tsv | sort | tr '\n' ' ')" = "SAM-28 SAM-31 SAM-33 " ] \
 && [ "$(date +%F)" \< "2026-11-01" ] \
 && echo "SAM PROFILE FRESH" || echo "SAM PROFILE REFRESH"
```

---

## 4. CORRECTED PART A — SAM

# Agent Profile — SAM

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P3 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** solo full-core read (P3 reader) + independent second-reader locator verification (every path:line below opened twice, by two readers).
**Sources read:** `CLAUDE.md` · `STATUS.md` · `STATUS_REFERENCE.md` · `MEMORY.md` · `thesis/THESIS.md` (header + section map) · `thesis/PREDICTIONS.tsv` (preamble + all 34 data rows) · `TRADE.md` · `STRATEGY.md` · `NEXUS_BRIEF.md` · `red/{COUNTER_THESIS,CHALLENGES,LOG}.md` · `docket/{CALENDAR.md,CATALYSTS.tsv,2026-09-18_SAM28_SAM31_REVIEW.md}` · `workbook/LEDGER_CADENCE.md` + ledger listing · `scripts/boot.py` + `scripts/lib/boot_context.py` · `insurers/TRACKER.md` · `MAINTENANCE.md` · `RECONCILIATION.md` · `SIGNAL_INTAKE.md` · `MOF_INTERVENTION_PLAYBOOK.md` · `board_log.tsv` · sub-agent pair-files
**Staleness — refresh when ANY ONE fires (all four machine-evaluable; command in the verification file §3):** (a) `AGENTS/SAM/thesis/THESIS.md:1` no longer reads `# SAM THESIS — v1.7`; (b) `AGENTS/SAM/red/CHALLENGES.md:4` `**Last RED sweep:**` advances past 2026-08-20; (c) the `Status == OPEN` set of `AGENTS/SAM/thesis/PREDICTIONS.tsv` is no longer exactly {SAM-28, SAM-31, SAM-33} (`STATUS.md:9` carries the same count); (d) hard floor **2026-11-01**.

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

# ═══ DESK 2 of 2 — SHADE ═══

## 1. Verification table — SHADE PART A

| § | Claim (≤20 words) | Verdict | Correction |
|---|---|---|---|
| Header | Staleness (a): no `*PREDICT*` / `PREDICTIONS.tsv` file exists | **VERIFIED** | `git ls-files` returns nothing |
| Header | Staleness (b): `STATUS.md:3` `**Last Updated:**` = 2026-08-28 | **VERIFIED** | `:3` = "2026-08-28 ~20:55 ET" |
| Header | Staleness (c): `ls inbox/WALTER/*.md` = 14, fires on 0 | **DRIFTED** | 14 confirmed, but "returns 0" is too narrow — a partial drain leaves it unfired. Restated as **≠14** |
| Header | Staleness (d): hard floor 2026-11-01; prior floor 2026-09-15 passed | **VERIFIED** | — |
| §1 | `CLAUDE.md:9` core question | **VERIFIED** | verbatim match |
| §1 | Signals to BROCK/LIQUID/REGINALD/NEXUS+PROME `CLAUDE.md:147-151` | **VERIFIED** | — |
| §1 | BROCK boundary is a four-row table `CLAUDE.md:15-22` | **VERIFIED** | header `:15`, rule + `[CONF BROCK date]` at `:22` |
| §1 | Class Market (`FLEET_MAP.tsv` SHADE row) | **VERIFIED** | SHADE / Market / L3 / H / 2026-09-01 |
| §2 | 162 tracked files | **VERIFIED** | — |
| §2 | `CLAUDE.md` 170 ln / 22,082 B; `:15-22`, `:32-37`, `:39-46`, `:48-52`, `:54-62`, `:64-87`, `:91-96`, `:98-145` | **VERIFIED** | every boundary opened |
| §2 | `STATUS.md` 150 ln / **32,462 B = 100% of budget**; `:12-26`, `:30-43`, `:47-51`, `:55-78`, `:81-85`, `:89-102`, `:111-123`, `:127-140`, `:146-150` | **VERIFIED** | read_cap_check: 32,462 B / 100% / rotate-tier |
| §2 | `REFERENCE.md` 201 ln / 36,669 B; §2 · §2Q · §2Q-bis · §3D · §3R · §4 · §5 · §6M · §8 · §9 · §10b | **VERIFIED** | all eleven headings present (`:11,156,189,100,172,137,40,123,56,73,84`) |
| §2 | `SCRATCH.md` 88 ln / 10,288 B; 13 dated NEXT SESSION items | **VERIFIED** | heading `:31`; 13 numbered items |
| §2 | `MEMORY.md` 111 ln / **31,745 B = 98%**; rotated-lessons index `:56` | **VERIFIED** | — |
| §2 | `MAINTENANCE.md` 186 ln / 46,312 B; 8/28 entry `:7-14` with two self-caught defects | **VERIFIED** | `:13` Amendment-10 violation, `:14` stamp defect |
| §2 | `NEXUS_BRIEF.md` 32 ln / 13,145 B; folded LAST per Amendment 10 `:3` | **VERIFIED** | — |
| §2 | `research/` (19 files) | **DRIFTED** | **20** — and the draft's own breakdown (15 md + 2 py + 3 json) sums to 20 |
| §2 | `instruments/…SPEC_2026-08-13.md:3` `REGISTERED, NOT YET GRADED` | **VERIFIED** | — |
| §2 | `domain/sources/01-08`, Mar'26, stale-flagged `STATUS.md:8` | **VERIFIED** | all 8 filenames match the stated topics |
| §2 | `sources/athene_statutory_2026-06-15/` + MANIFEST | **VERIFIED** | 9 tracked files |
| §2 | `registry/corrections_receipts.tsv` — exactly 1 row, `COR-20260828-03`, NO-OP | **VERIFIED** | — |
| §2 | `board_log.tsv` (97 rows) | **DRIFTED** | 97 **lines** = v0.2 header + **96 data rows** |
| §2 | `archive/` (17 files) incl. the crc32 trio | **DRIFTED** | **18** files; the crc32 trio verifies exactly |
| §2 | crc32 receipts 125,359/`0502fd27`, 50,727/`34385c68`, 35,782/`fdf1e872` | **VERIFIED** | `STATUS.md:20-21` |
| §2 | M-11 grade card at agent root | **VERIFIED** | 1 of 11 root `.md` |
| §2 | 14 files unprocessed in `inbox/WALTER/` | **VERIFIED** | `inbox/` totals 85 (WALTER top 14 · WALTER/processed 47 · processed 24) |
| §3 | Kill paths `:48-52`; top-line `STATUS.md:47-51`; stage 4b `:81-85` | **VERIFIED** | `:85` "🆕 Stage 4b added 2026-08-28" |
| §3 | Convergence index 5-pt handle + Independence column + composite 20/30 `STATUS.md:55-71` | **VERIFIED** | `:57` handle, `:71` "Composite (SHADE-owned independent roots #1–5,7): 20/30" |
| §3 | T-SHADE-01 legs `:78` `:79` `:80` `:81` `:82` `:83` `:84` `:85`; 4-for-4 NOT MET | **VERIFIED** | `:82` "That is 4-for-4"; `:85` "NOT ARMED — ZERO legs", HY OAS 263 = 17bp below bar |
| §3 | Thresholds `CLAUDE.md:54-62` / `STATUS.md:43` / `REFERENCE.md §2`; non-conflict note `:87` | **VERIFIED** | — |
| §3 | Predictions: no ledger; `PRED-006` 65%→30% (`STATUS.md:98`); canary; C2 2026-11-18 | **VERIFIED** | `:98` carries the chain and the ≥+$10.0B AS PRINTED bar |
| §3 | Routing: CCC one-owner-each + 787-obs independence bar `STATUS.md:115-120` | **VERIFIED** | `:120` "787-obs series since 2023-08-29" |
| §3 | BOTTOM LINE present and dated `STATUS.md:146-150` | **VERIFIED** | — |
| §3b | `falsification_scan.py` puts SHADE in the "no surface this scan can see" bucket | **VERIFIED** | reproduced; tool text "4 real rails, 3 real gaps" confirmed |
| §3b | Kill-path 1's only stamp is `(Currently YELLOW per 6/22 ladder…)`; 2-4 unstamped | **VERIFIED** | `CLAUDE.md:49-52` |
| §3b | Ladder `STATUS.md:95` markers 0-6; marker (0) MET (Truist + Fifth Third) | **VERIFIED** | "AMENDED 2026-08-28"; markers (0)…(6) enumerated in-row |
| §3b | `STATUS.md:96` ~2026-11-15 Exhibit 1 / SoO L15 | **VERIFIED** | — |
| §3b | `STATUS.md:101` C2 three-conjunct ≤+48bp / ≥$2.0B / ≥36.2% | **VERIFIED** | — |
| §3b | `STATUS.md:102` W2 standing, no expiry, RETRACTION not re-spec | **VERIFIED** | — |
| §3b | `REFERENCE.md §8` 10 questions; 7 CLOSED, 8/9/10 OPEN; item 2 "no EDGAR screen" | **VERIFIED** | §8 at `:56`; item 2 at `:59` contains "**No EDGAR screen exists**" |
| §4 | 125,359 B → 32,462 B with a byte-exact recipe `STATUS.md:20` | **VERIFIED** | `tail -n +8` recipe in-row |
| §4 | `CLAUDE.md:167` LAST_COMPLETION demoted to legacy | **VERIFIED** | — |
| §4 | `CLAUDE.md:102` read→write pairing (1→6, 2→8, 3→9, 11a LAST) | **VERIFIED** | — |
| §4 | `CLAUDE.md:80` ownership split, not a copied series | **VERIFIED** | — |
| §4 | Promotion-on-behaviour cited as `REFERENCE.md §10b:3` | **DRIFTED** | section-relative numbering. Absolute: **`REFERENCE.md:86`** (asks #1/#2/#3 at `:90`/`:91`/`:92`) |
| §4 | `CLAUDE.md:154` stale `domain/sources/` pointer | **VERIFIED** | — |
| §5 | `STATUS.md:20-21` crc32; `CLAUDE.md:78,79,80,81,83,84`; `STATUS.md:114,115-120,26,38` | **VERIFIED** | `:38` carries BOTH the retracted-12×/5.1× guard and the no-post-pause-flow guard |
| §5 | Four denominators, ~9pp swing (`REFERENCE.md §2Q-bis`) | **VERIFIED** | §2Q-bis at `REFERENCE.md:189` |
| §5 | Peer-relative spread sub-row canary, "MEMORY-codified" | **UNLOCATED → LOCATED** | `AGENTS/SHADE/MEMORY.md:32` |
| §5 | `CLAUDE.md:22` `[CONF BROCK date]` form | **VERIFIED** | — |
| §5 | MANIFEST + the two reusable crawlers | **VERIFIED** | `research/AGF_NPORT_crawl_2026-06-22.py`, `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py` |
| §6 | Ask #3 DONE 8/28; #2 counted at `CLAUDE.md:82` but §10b still 🔴; #1 open six sessions | **VERIFIED** | `REFERENCE.md:90-92`; `SCRATCH.md:42` |
| B2 | read-cap table (4 reads; −9,678 B / −8,961 B to the <70% stop; rc=0) | **VERIFIED** | reproduced exactly, incl. the rc-vs-tier point |
| B2 | `ledger_staleness.py SHADE` → "no ledgers matched `workbook/*.tsv`" | **VERIFIED** | — |
| B2 | `inbox/` 55 · WALTER/processed 32 | **FAILED** | `inbox/` = **85**; `inbox/WALTER/processed/` = **47**; top-level 14; `inbox/processed/` 24 |
| B3 | 11 commits, 0 self, all WALTER; last self `e0177eefc` 2026-08-28; STATUS delta ZERO | **VERIFIED** | all reproduced |
| B5-H1b | board_log id ≠ filename on the 8/28 WALTER note | **VERIFIED** | log: `…delaware-life-clear-spring-denominators`; disk: `…delaware-life-**and**-clear-spring-**asset**-denominators.md` |
| B5-H1b | "Boot step 4a matches on *exact* `signal_id`" | **DRIFTED** | `CLAUDE.md:119` says "not yet logged in `board_log.tsv`"; the key is the `signal_id` column, so the mismatch does re-pick it forever, but the word "exact" is the reader's inference, not the charter's text |

**SHADE totals — VERIFIED 44 · FAILED 1 · DRIFTED 6 · UNLOCATED 1 (located).**

## 2. New 🔴 the first reader missed (SHADE)

| # | Sev | Finding | Locator |
|---|---|---|---|
| **R7** | 🟠 (reviewer-side) | **The draft's R5 says the SHADE FLEET_MAP `Gaps` cell verifies apart from the 9/15 floor. It does not — its FIRED-triad locator is wrong.** The cell reads *"FIRED-triad now a COUNTED standing form (**STATUS:43** T-SHADE-01 4-for-4)"*. `AGENTS/SHADE/STATUS.md:43` is the dated TAPE row (APO 135.01 · ARES 142.50 · BIZD 13.37 …). The counted 4-for-4 standing form lives at **`AGENTS/SHADE/CLAUDE.md:82`**; `STATUS.md` contains no "4-for-4" string at all. Two DAEDALUS surfaces now point a reader at a price row for a trigger state. Fix the cell at the next re-cut. | `AGENTS/DAEDALUS/FLEET_MAP.tsv` SHADE row col 7; `AGENTS/SHADE/STATUS.md:43`; `AGENTS/SHADE/CLAUDE.md:82` |
| **R8** | 🟡 | **The draft's own §10b citations are section-relative, which is the same locator class that rotted the old SAM profile.** `REFERENCE.md §10b:3` / `:7` / `:8` resolve to file lines `:86` / `:90` / `:91`. A profile that mixes absolute and section-relative line numbers cannot be checked mechanically. Corrected throughout PART A below. | `AGENTS/SHADE/REFERENCE.md:84-92` |

## 3. Staleness-trigger evaluability — SHADE

**YES — machine-evaluable from named artifacts, in one command,** with leg (c) restated as ≠14 rather than =0. Verified to print `SHADE PROFILE FRESH` at HEAD:

```sh
[ -z "$(git ls-files 'AGENTS/SHADE/*PREDICT*' 'AGENTS/SHADE/**/PREDICTIONS.tsv')" ] \
 && grep -q '^\*\*Last Updated:\*\* 2026-08-28' AGENTS/SHADE/STATUS.md \
 && [ "$(ls AGENTS/SHADE/inbox/WALTER/*.md 2>/dev/null | wc -l)" = 14 ] \
 && [ "$(date +%F)" \< "2026-11-01" ] \
 && echo "SHADE PROFILE FRESH" || echo "SHADE PROFILE REFRESH"
```

---

## 4. CORRECTED PART A — SHADE

# Agent Profile — SHADE

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P3 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** solo full-core read (P3 reader) + independent second-reader locator verification.
**Sources read:** `CLAUDE.md` (whole, 170 ln) · `STATUS.md` (whole, 150 ln) · `SCRATCH.md` (whole) · `MEMORY.md` (section map) · `REFERENCE.md` (§8, §10b, section map) · `NEXUS_BRIEF.md` · `MAINTENANCE.md` (top) · `board_log.tsv` · `registry/corrections_receipts.tsv` · `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md` · `research/` + `domain/sources/` + `sources/` listings · `inbox/WALTER/` listing · `2026-08-04_athene-q2-m11-grade-card.md`
**Staleness — refresh when ANY ONE fires (all four machine-evaluable; command in the verification file §3):** (a) a file matching `AGENTS/SHADE/*PREDICT*` or `AGENTS/SHADE/**/PREDICTIONS.tsv` exists (the standing L4 trigger — still unfired); (b) `AGENTS/SHADE/STATUS.md:3` `**Last Updated:**` advances past 2026-08-28; (c) `ls AGENTS/SHADE/inbox/WALTER/*.md | wc -l` returns anything other than **14** (the desk booted and drained, wholly or partly); (d) hard floor **2026-11-01**.
*(The prior profile's floor of 2026-09-15 has PASSED — this profile is the response to it.)*

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

### 1. Identity

PE-owned life-insurer / captive-reinsurance forensics — the *shadow insurance system*: affiliated reinsurance, offshore captives, synthetic surplus, FABN/FHLB funding, AMAPS/CFO rated wrappers, Egan-Jones ratings machinery, AG 55 / NAIC / SVO. **Class:** Market (`FLEET_MAP.tsv` SHADE row). **Core question** (`CLAUDE.md:9`): *when private-credit stress enters an insurance wrapper, does it become hidden leverage, funding fragility, or forced capital pressure?*

**Transmission:** signals to BROCK / LIQUID / REGINALD / NEXUS+PROME (`CLAUDE.md:147-151`); reads those desks as owners rather than re-deriving (`STATUS.md:111-123`). **Spawnable by:** PROME / Will. **SHADE-canonical owner of insurer-exposure figures**; the BROCK boundary is a four-row table at `CLAUDE.md:15-22`.

One line: *the desk that asks whether stressed credit is being made to look contained by an insurance balance sheet.*

### 2. File anatomy (where the richness lives)

162 tracked files (`git ls-files AGENTS/SHADE/ | wc -l`) — a **small, dense** tree, the opposite shape from SAM. Cluster mass: `inbox/` 85 · `research/` 20 · `archive/` 18 · root `.md` 11 · `sources/…` 9 · `domain/sources/` 8 · `outbox/` 8 · `instruments/` 1 · `registry/` 1.

| File / cluster | Holds | Bytes | Richness |
|---|---|---|---|
| `CLAUDE.md` (170 ln) | identity, BROCK boundary table `:15-22`, 5 key ratios `:32-37`, Athene target block `:39-46`, **4 independent kill paths `:48-52`**, environment threshold band `:54-62`, 🆕 **§REGISTERED TRIGGERS / T-SHADE-01 `:64-87`**, historical precedents `:91-96`, symmetric boot↔closeout `:98-145` | 22,082 | **durable method + the desk's only registered trigger** |
| `STATUS.md` (150 ln) | **the canonical live surface.** §0 where-everything-is + the rotation receipt `:12-26` · §0l live rails `:30-43` · §1 top-line `:47-51` · **§3 signal dashboard with a 5-pt stackable handle + Independence column `:55-78`** · §4 transmission map incl. 🆕 stage 4b `:81-85` · §6 forward regulatory calendar + the Delaware Life escalation ladder `:89-102` · §7 cross-agent deps `:111-123` · §10 owed list `:127-140` · **BOTTOM LINE `:146-150`** | **32,462 = 100% of budget** | live state; **rotate-tier** |
| `REFERENCE.md` (201 ln) | **the cold half, born 2026-08-28.** §2 carried figures `:11` · §2Q Delaware Life Q2 statutory `:156` · §2Q-bis the four-denominator warning `:189` · §3D per-vector evidence `:100` · §3R per-vector one-liners `:172` · §4 full transmission map `:137` · §5 watchlist `:40` · §6M standing monitor rows `:123` · §8 active questions (10) `:56` · §9 retired rails `:73` · **§10b DAEDALUS maturity asks `:84`** | 36,669 | **NOT boot-read; consulted by section before citing any figure** (`CLAUDE.md:111`) |
| `SCRATCH.md` (88 ln) | **canonical session handoff** — CHANGES SINCE / WHAT I DID / 🔴 NEXT SESSION (`:31`, 13 dated priority-ordered items) / open threads / mail state | 10,288 | handoff |
| `MEMORY.md` (111 ln) | BROCK boundary, source-quality caveats, forensic-discipline lessons, the peer-relative-spread canary `:32`, a rotated-lessons one-line index `:56`, per-session lesson blocks | **31,745 = 98% of budget** | learning; **rotate-tier** |
| `MAINTENANCE.md` (186 ln) | structural-change log; the 8/28 entry `:7-14` records an Amendment-10 self-violation `:13` and a stamp defect `:14`, both caught and repaired | 46,312 | architecture record |
| `NEXUS_BRIEF.md` (32 ln) | board-facing synthesis; folded LAST per Amendment 10 `:3` | 13,145 | cross-agent |
| `research/` (**20 files** — 15 `.md` + 2 `.py` + 3 `.json`) | per-thread deep work: ATHENE_FABN_MATURITY_LADDER + `AGF_NPORT_crawl_2026-06-22.py`/`.json` · FABN_PEER_SPREAD_NPORT `.py`/`.json` + the 8/28 RERUN + RUNLOG · DELAWARE_LIFE ×4 · ATHENE_FUNDING_MIX · BMA_EGAN_JONES · COMBINED_INSURER_SINK_WELD2 · ARCC pre-registration · INSURER_LENDER_DOUBLE_JEOPARDY · the 8/13 news-sweep pair | — | **crown jewels + the only executable code on the desk** |
| `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md` | **new anatomy.** A pre-registered instrument spec (S1/S2/S3), `:3` `State: REGISTERED, NOT YET GRADED`, with an explicit companion-not-replacement constraint | — | pre-registration discipline |
| `domain/sources/01-08` | 8 deep KB reference reports (PE nexus → captive/XOL → statutory reserves → liquidity transmission → filing forensic manual → Apollo fee dependency → FABN wall → Egan-Jones) | — | KB library, **Mar'26 vintage, stale-flagged at `STATUS.md:8`** |
| `sources/athene_statutory_2026-06-15/` (9) | raw statutory text (AANY/ALIRT/ALRE) + `MANIFEST.md` | — | primary-filing chain (SKIP for grading) |
| `registry/corrections_receipts.tsv` | **new anatomy** — R1 corrections receipts; exactly 1 data row (`COR-20260828-03`, NO-OP) | — | protocol compliance |
| `board_log.tsv` (**96 data rows** + v0.2 header) | WALTER signal-consumption ledger, `timestamp_read/signal_id/disposition/source/notes` | — | record |
| `archive/` (**18 files**) | incl. the three **crc32-stamped** 8/28 pre-rotation files (STATUS 125,359 B crc `0502fd27`; SCRATCH 50,727 B crc `34385c68`; MEMORY 35,782 B crc `fdf1e872`) and `STATUS_section0_deltas_retired_2026-07-27.md` | — | **the fleet's cleanest byte-cap rotation receipt** |
| `2026-08-04_athene-q2-m11-grade-card.md` | the M-11 dual-test grade card, **at agent root** (1 of 11 root `.md`) | — | ⚠️ still not in any ledger |
| `outbox/` (7 + `delivered/.gitkeep`) · `inbox/` (**85**) | delivery memos to PROME; `inbox/WALTER/` top-level **14 UNPROCESSED** · `inbox/WALTER/processed/` 47 · `inbox/processed/` 24 | — | see flag H1 |

*Key question this answers:* live state → `STATUS.md`; **any figure before citing it** → `REFERENCE.md` §2/§2Q; what fires the dig → `CLAUDE.md:64-87`; what happened last session → `SCRATCH.md`; why the structure is this shape → `MAINTENANCE.md`.

### 3. Per-dimension local representation

| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| **Thesis structure** | `CLAUDE.md:48-52` (4 independent kill paths) + `STATUS.md:47-51` (top-line + SHADE-specific thesis) + `STATUS.md:81-85` / `REFERENCE.md:137` §4 (6-stage transmission map) | Kill paths are numbered and independent; the transmission map gained **stage 4b (distribution channel closes — the LIABILITY side)** on 2026-08-28 after an event the map had no rung for | **strong** |
| **Convergence / scoring** | `STATUS.md:55-71` | 🆕 **"Convergence index (5-pt stackable handle)"** `:57` — 9 vectors, per-vector score, **Independence column with a shared-antecedent flag**, and a **composite over SHADE-owned independent roots only: 20/30** `:71`, plus a written guard against reading a single-name firing vector as cohort stress | **NOW CONFORMANT** — the handle the old profile recorded as missing |
| **Invalidation / exit** | `CLAUDE.md:48-52` kill paths · `CLAUDE.md:64-87` **T-SHADE-01** · `STATUS.md:95` escalation ladder (markers 0-6) · `STATUS.md:101` C2 self-executing withdrawal test | T-SHADE-01 is a **two-leg conjunctive** trigger with a named `value_basis`, a *directional-not-relative* sign leg `:78`, a window-sensitivity guard `:79`, an ownership split `:80`, and a **counted fired-state: 4-for-4 NOT MET** `:82`. C2 is a **self-executing withdrawal** dated 2026-11-18 | **strong; the FIRED-triad ask is effectively answered in counted form** |
| **Thresholds** | `CLAUDE.md:54-62` durable environment band · `STATUS.md:43` live tape · `REFERENCE.md:11` §2 carried figures | Durable-vs-live split with an **explicit do-not-confuse note** (`CLAUDE.md:87`): the environment band and T-SHADE-01's level leg *will disagree by construction* | **conformant (strong)** |
| **Predictions** | **no ledger.** Named binaries live scattered: `PRED-006` with a confidence chain 65%→30% (`STATUS.md:98`), the canary spec `REGISTERED, NOT YET GRADED`, the 2026-11-18 C2 test (`:101`), the ladder's dated Q3 step (`:96`) | Dated, falsifiable, confidence-bearing — and **with no scoring surface**. Self-flagged 🔴 in three places | **MISSING — the single L4 blocker** |
| **Cross-agent routing** | `CLAUDE.md:147-151` · `STATUS.md:111-123` · `NEXUS_BRIEF.md` | §7 is written as *"read the OWNER, never re-derive"*, with the **CCC channel reconciled to one-owner-each** `:115` and an explicit **independence bar** `:120` (both ratios read the same 787-obs series ⇒ agreement is arithmetic, not corroboration) | **strong** |
| **Session handle** | `STATUS.md:146-150` | **BOTTOM LINE present**, dated, and it leads with the session's own instrument failures | **present** |

### §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)

⚠️ **SHADE has no thesis-class file. Its rails live in `CLAUDE.md` and `STATUS.md` §6, which is why `falsification_scan.py` reports "no surface this scan can see" for SHADE** — a scanner blind spot, **not** an L3 gap (verified independently at the artifact by both readers). Hand-derived inventory:

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `CLAUDE.md:48-52` — the 4 independent kill paths | the whole SHADE thesis, four ways | path 1 `:49` carries `(Currently YELLOW per 6/22 ladder …)` — **the only stamp, and it is 6/22** | per-path colour + a named RED bar (FABN spread >250bp per `:57`, **or** a pulled/failed syndication) |
| `CLAUDE.md:64-87` — **T-SHADE-01** wrapper-decoupling | arms the pre-registered statutory entity+fund dig (`STATUS.md:137`) | `**State 2026-08-28**` row `:85`; sign-leg reading row `:82` dated 8/13→8/28 | ❌ **NOT ARMED — ZERO legs, both freshly measured**; level leg HY OAS 263 = 17bp below bar; sign leg **4-for-4 NOT MET** |
| `CLAUDE.md:54-62` — environment threshold band | the credit-environment read (not an arming condition) | none in-row; live values at `STATUS.md:43` | green/yellow/red per signal; explicit non-conflict note `:87` |
| `STATUS.md:95` — **Delaware Life escalation ladder** (markers 0-6) | vector #1's escalation state | `**AMENDED 2026-08-28**` in-row | **🆕 marker (0) COUNTERPARTY/DISTRIBUTION — ✅ MET 2026-08-28** (Truist + Fifth Third paused), with a pre-registered false-positive reversion |
| `STATUS.md:96` — Delaware Life Q3-2026 statutory | the ladder's **first DATED step** | `~2026-11-15` in the Date column | instruments named (Exhibit 1, SoO L15) differenced against the 1H-26 baseline |
| `STATUS.md:98` — `PRED-006` MBA Q2 bar | the CRE/multifamily holdings leg | `~2026-09-mid` in the Date column; confidence chain **65% → 30%** | **≥ +$10.0B as printed**; graded jointly with `PRED-CREED-010`. ⚠️ **date window is NOW** |
| `STATUS.md:101` — **C2 withdrawal test** | SHADE's own C2 claim — *self-executing against itself* | `2026-11-18` in-row | three-conjunct bar (peer penalty ≤+48bp AND S1 ≥$2.0B AND S2 ≥36.2%) ⇒ *"I withdraw C2 and record the quiet as informative health"* |
| `STATUS.md:102` — **W2 ordering test** (shared with BROCK) | the bloc's instrument set | `Standing, no expiry` | a gated instrument firing before/with the non-gated one ⇒ **the bloc owes a RETRACTION, not a re-spec** |
| `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md:3` | kill-path 1's second reading | `**Dated spec:** 2026-08-13 · **State:** REGISTERED, NOT YET GRADED` | S1/S2/S3, no-bands rule; first graded reading at the Athene Q3 cluster (`STATUS.md:99`) |
| `REFERENCE.md:56` §8 (10 active questions) | the research agenda, several with pre-stated expected results | section header only | item 7 CLOSED-with-verdict-retained; 8/9/10 OPEN; item 2 `:59` flagged *"No EDGAR screen exists"* |

### 4. Deviations from standard (+ why)

- **No thesis file; the thesis is distributed across `CLAUDE.md` (kill paths) + `STATUS.md` §1/§3/§4.** *Equivalent, with one cost:* it is invisible to the fleet falsification scanner, which then prints a Market-class gap over a desk that has rails. Fix is a scanner/registry fix, not a SHADE restructure.
- **Hot/cold split into `STATUS.md` + `REFERENCE.md` with a crc32-stamped verbatim archive.** *Better than standard* — 125,359 B → 32,462 B with a byte-exact reproduction recipe written into the receipt (`STATUS.md:20`). This is the form to copy fleet-wide.
- **`SCRATCH.md` as the canonical handoff, `LAST_COMPLETION.md` demoted to legacy** (`CLAUDE.md:167`). *Equivalent.*
- **Read→write pairing declared as one symmetric sequence** (`CLAUDE.md:102`): STATUS read 1 → write 6, SCRATCH read 2 → write 8, MEMORY read 3 → prune 9, NEXUS_BRIEF write 11a LAST. *Better* — makes the closeout auditable against the boot.
- **A trigger registered with an ownership split rather than a copied series** (`CLAUDE.md:80`). *Better* — SHADE reads LIQUID's HY OAS and owns only the firing decision, which is exactly the anti-fork form.
- **Predictions absent while resolution behaviour is present.** *Debt, and DAEDALUS's own promotion logic said so*: SHADE was promoted L2→L3 on behaviour rather than shelves (`REFERENCE.md:86`). The debt is one file.
- **`domain/sources/` exists but `CLAUDE.md:154` still says "If future `domain/sources/` scaffolding is built, update this pointer."** *Pure debt* — a stale pointer in the charter (flag H4).

### 5. Load-bearing context / DO NOT TOUCH

1. **The 8/28 crc32 rotation receipts** (`STATUS.md:20-21`) — `tail -n +8` reproduces the pre-rotation STATUS byte-for-byte. Never edit the archived copies; the crc is the proof.
2. **T-SHADE-01's sign leg is DIRECTIONAL, not relative** (`CLAUDE.md:78`) and **is a DATED READING, not a standing state** (`CLAUDE.md:81`) — any level-leg crossing obliges a **fresh** close-based read before the trigger state is restated. Do not collapse it into a relative spread.
3. **The window-sensitivity guard** (`CLAUDE.md:79`): the *relative* spread flips sign with the start date (+1.04pp from 8/3 vs −0.88pp from 7/31, same end date). Never quote it without its window.
4. **T-SHADE-01's sign leg ≠ BROCK's wrapper half** (`CLAUDE.md:83`) — BROCK's additionally requires HY widening, CCC-led. One can flip with the other unmoved.
5. **HY OAS series ownership is LIQUID's; SHADE keeps no parallel series and no parallel sustain count** (`CLAUDE.md:80`, `STATUS.md:114`).
6. **CCC ratios: SHADE registers NEITHER** (`STATUS.md:115-120`). `CCC/HY` → REGINALD `VX-REG-18.04`; `CCC/BB` → BROCK `KB-BRK-221`. **The independence bar never lifts** — both read the same 787-obs series (`:120`), so agreement is arithmetic.
7. **The retracted 12× leverage figure stays retracted — the filing says 5.1×** (`STATUS.md:38` guard 2).
8. **No post-pause flow figure exists** (`STATUS.md:38` guard 1); *"regulatory margin call"* and *"flows going the wrong way"* are the relayer's words, stripped by WALTER, and are on **no SHADE surface**.
9. **Four denominators circulate for Delaware Life; concentration swings ~9pp on the choice** (`REFERENCE.md:189` §2Q-bis). Quote the **pair** (dollars up 2.75%, share down 2.85pp), never one leg.
10. **Peer-relative spread sub-row** — an absolute T+123 green can mask a cohort-widest +43-48bp penalty. Codified at `MEMORY.md:32`.
11. **Standing rule: no dig absent a trigger** (`CLAUDE.md:84`). The statutory dig is deploy-on-trigger, ordered a→d (`STATUS.md:137`).
12. **The BROCK boundary and `[CONF BROCK date]` citation form** (`CLAUDE.md:22`); do not maintain a duplicate BROCK dashboard.
13. **Statutory provenance tree** (`sources/athene_statutory_2026-06-15/MANIFEST.md`) and the reusable EDGAR/NPORT crawlers (`research/AGF_NPORT_crawl_2026-06-22.py`, `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py`) — the desk's unique forensic capability.
14. **Session delta lives in `research/`; STATUS carries only the verdict and the live rails** (`STATUS.md:26` standing rule ①). This is what stops §0 accreting; it is the rule that made the byte fix hold.

### 6. Maturity snapshot

Grades and classification live in `AGENTS/DAEDALUS/FLEET_MAP.tsv` (SHADE row). Work queue → `upgrades/SHADE_CARD.md`; the desk mirrors the asks itself at `REFERENCE.md:84-92` (§10b).

Of the three L2→L3 asks recorded 2026-07-27: **#3 (STATUS compress) ✅ DONE 2026-08-28** (`REFERENCE.md:92`) under a harder constraint than asked; **#2 (standing FIRED-triad) effectively answered** in counted form at `CLAUDE.md:82` (*4-for-4*) though `REFERENCE.md:91` still marks it 🔴 OPEN; **#1 (`PREDICTIONS.tsv` with confidences at registration) 🔴 OPEN and untouched across six sessions** by the desk's own count (`SCRATCH.md:42`, `REFERENCE.md:90`). That one file is the whole L4 path.

### 7. Open questions / comprehension gaps

1. **Why hasn't SHADE booted since 2026-08-28?** Zero self-authored commits in the review period; the last three real sessions were Will-directed or PROME-orchestrated. Correct watch-agent cadence for a latent-vector desk, or a scheduling gap? **NOT-ADJUDICATED** from inside SHADE's tree.
2. **`PRED-006`'s MBA Q2 window (~2026-09-mid) is now.** Whether the print has landed is **CANNOT-EVALUATE** without an external source.
3. **Is the FIRED-triad ask (#2) actually still open?** `CLAUDE.md:82` carries a counted standing form; `REFERENCE.md:91` still says 🔴 OPEN. One of the two is stale (flag H6).
4. **How light should the predictions ledger be?** A full directional calibration scoreboard is lower-value for a watch agent than for a directional one. The risk of over-building is real; the risk of the current state is that **every session adds an ungraded binary** (`STATUS.md:135`).
5. **Does NEXUS actually consume SHADE's brief?** The brief exists and is folded last, correctly. Whether it is read is outside SHADE's tree. **NOT-SEEN.**

---

## Cross-desk note (carried forward from the draft, verified)

Both prior profiles' staleness triggers were prose with an "or >N days" escape, and in both cases the substantive leg had either become un-fireable (SAM's "FXY modal band re-derived" — `STRATEGY.md:3-8` is bannered historical) or sat silently unfired while a *different* leg did the work (SHADE's floor). Both corrected PART As above carry **file-readable triggers only**: a named artifact plus a condition a shell one-liner evaluates, and both one-liners were **run at HEAD and observed to print the FRESH line** (the clean-case watch that `BLUEPRINTS/CHECK_STANDARD.md` §3 requires, not merely a claim that they are evaluable).

**Verifier:** independent second reader, P3 leg, DAEDALUS fan-out 2026-09-17. Read-only; this file is the only write.
