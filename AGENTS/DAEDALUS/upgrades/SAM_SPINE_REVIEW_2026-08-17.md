# SAM — Spine & Operating-Contract Review (READ-ONLY)

**Date:** 2026-08-17 · **Reviewer:** DAEDALUS (reader, Will-directed SAM+BRENT architecture review)
**Mode:** READ-ONLY — SAM was in a LIVE session throughout; nothing touched.
**Map used:** `profiles/SAM.md` (built 2026-07-10) — **stale, see PROFILE DRIFT below.** Every claim relied on was re-verified against disk.
**Scope:** contract-vs-execution layer (PAT-096/097) — does the specified process actually run?

---

## PROFILE DRIFT (profiles/SAM.md, built 7/10 — 38 days)

| Profile claim | Current fact |
|---|---|
| `STATUS.md` **300 ln > 250 cap** | **248 ln — UNDER cap.** SAM compressed repeatedly (8/2: 408→179). The cap is *executed*. **But see F3 — bytes.** |
| THESIS v1.6.3 | **v1.7** (2026-08-07, carry-convexity tail RETIRED TO LOW, leg-1 SPF fired) |
| PREDICTIONS 54 rows: 9 CONFIRMED / 11 FAILED / 7 OPEN | **14 CONFIRMED / 14 FAILED / 1 special / 5 OPEN** |
| "FXY modal band OVERDUE" = sharpest owner-lane flag | **Superseded** — the whole convexity frame retired 8/7; band is moot |
| §8 handle MISSING, STATUS 300>250 | STATUS now cap-compliant on lines; §8 unchanged |
| Sub-agent trio | **Confirmed live and stronger than at build** — see F7 |

**Verdict on the profile:** the *anatomy* and *DO-NOT-TOUCH* sections held up well; every *number* had moved. Refresh trigger ("Sep-18 window advances / >45d") fired via the 8/7 frame break, which the profile could not anticipate. **Recommend re-build.**

---

## FINDINGS

| # | Surface | Finding | Evidence (file:line, dates) | Severity | Route-priority |
|---|---|---|---|---|---|
| 1 | `thesis/THESIS.md` | **Owner doc carries the RETIRED CFTC basis at 11+ LIVE sites** while every derived surface carries the corrected one — drift class **inverted** (derived clean, owner stale). Not dated quotes: L42 is the live **Status:** line, L54 the live channel table, L87 the live SPF leg-1 record, L247 the live threshold table. | THESIS:4,42,54,87,167,196,247 all read `−45,473 = 25.3% of the −180K peak` / `90.8%`. STATUS:5, TRADE:6, STRATEGY:6, NEXUS_BRIEF:7 all read `24.2% of R = −188,077` and stamp the old form `⛔ RETIRED (forum-4, Will-ratified 2026-08-11)`. THESIS last committed **8/13 (dd73f3fe2) — two days AFTER ratification.** | **STRUCTURAL** | **P1 — SAM** |
| 2 | `thesis/THESIS.md` § CROSS-AGENT LINKS | **Live cross-agent routing line contradicts every other surface.** `→ HENRY: Carry-unwind = convexity TAIL at MED-HIGH since 2026-08-02 — PROVISIONAL on the Fri 8/7 CFTC print.` The 8/7 print **resolved that provisional flag to LOW/RETIRED.** This sits in the section whose entire purpose is telling other agents what to consume, inside boot-step-1. | THESIS:299 (verified in-context, not a superseded block — L290-303). Contradicts THESIS:42 in the same file. PROME did circulate a "kill-on-sight the old refs" packet 8/11 (`RED/inbox/processed/2026-08-11_from-PROME_forum4-close…`), so **consumers were warned; the SAM-side propagation is what didn't happen.** | **STRUCTURAL** | **P1 — SAM** |
| 3 | `STATUS.md` + `CLAUDE.md:129` | **The 250-line cap is being satisfied while the file grows 59% in bytes.** Lines pinned at the cap; content up by more than half. The cap has **no byte tier**, so governance measures the one dimension that stopped moving. | 8/3 `fa650a4d1`: **250 ln / 35,654 B** (142.6 B/ln) → 8/17 `8965a1a49`: **248 ln / 56,740 B** (228.8 B/ln). **+21,086 B (+59.1%), −2 lines, +60.4% line density.** Longest lines now 2,113 / 1,504 / 1,371 chars. | **STRUCTURAL** | **P1 — DAEDALUS** |
| 4 | `NEXUS_BRIEF.md` | **Amendment-10 ordering rule is stated with a checkable form but nothing checks it — and today's session is live-at-risk.** Brief folded 08:50:27 citing STATUS `b41406264` (08:48:35) ✅, then **three further STATUS commits** landed with no re-fold. Brief is currently 3 commits / +2,823 B behind. | BRIEF:23 `As of: 2026-08-17 ~09:0x ET … STATUS commit b41406264`. STATUS commits 8/17: 08:48:35 · **09:34:13 · 09:55:13 · 11:10:28**. Rule + checkable form at CLAUDE.md:76. | **HYGIENE** (at-risk, not yet a violation) | **P2 — SAM** |
| 5 | `thesis/timeline/TIMELINE.md` | **Stamp is 7 days behind its own last edit**, and content coverage stops ~7/31. Stamp reads `Last Updated: 2026-07-31`; the file was edited **8/7** (`2d8659eb5`, +15 ln). No entries for the 8/13 SAM-41 discovery, the 8/14 KILL SPEC #3 firing, or the 8/17 JGB-through-4.00% curve flip. | TIMELINE:3 vs `git show 2d8659eb5 --stat`. Recurring class: KOYOMI flagged TIMELINE staleness at Runs 9-10, satisfied at Run-11 (`KOYOMI_MEMORY:478`). | **HYGIENE** | **P2 — SAM** |
| 6 | `SIGNAL_INTAKE.md` + `CLAUDE.md:255` | **A stale-banner that has itself gone stale, and a three-way version disagreement.** The banner warns correctly but its own contents rotted: names `thesis now v1.6.9` and `spot now 163.16`. Actual: **THESIS v1.7**, USD/JPY **~159.3**. Meanwhile `CLAUDE.md:255` describes the same file as stale "thesis now **v1.5**". Three surfaces, three versions, none current. | SIGNAL_INTAKE:3 (`v1.6.9`, `163.16`); CLAUDE.md:255 (`v1.5`); THESIS:2 (`v1.7`); BRIEF:7 (159.3). Banner last refreshed 2026-04-08. `finding_banner_is_a_warning_not_a_fix` — no dated rewrite trigger. | **HYGIENE** | **P2 — SAM** |
| 7 | Sub-agent pair-files | **Ungoverned mega-files.** `METSUKE_MEMORY.md` **333,335 B / 1,479 ln** — the largest file in SAM's tree, ~6× STATUS. Combined staff state **591 KB** vs SAM's own STATUS 57 KB. No cap was ever set for these; they are outside every SAM cap and every fleet check. *(Content quality is high — this is a governance gap, not a rot claim.)* | `METSUKE_MEMORY.md` 333 KB · `KURA_MEMORY.md` 149 KB · `KOYOMI_MEMORY.md` 109 KB. CLAUDE.md:252,263 register them but set no bound. | **HYGIENE** (structural-adjacent) | **P2 — DAEDALUS** |
| 8 | `OPEN_THREADS_2026-07-09.md` | **Silent-rot middle — the clearest two-state violation in the tree.** No banner, no live reference anywhere in the repo, untouched since 7/12, dated filename implying a point-in-time snapshot. Neither FROZEN nor LIVE. | 9,946 B / 43 ln, last commit 2026-07-12. Zero hits for `FROZEN|superseded|not maintained`. Not in CLAUDE.md's FILES table. | **HYGIENE** | **P2 — SAM** |
| 9 | `V16_RED_DIALOGUE.md` | Fold-complete marker present (`✅ SAM FOLD — CHUNK 1 DONE, 2026-06-22`) but **no FROZEN banner**. A v1.6-era artifact (thesis now v1.7) at 39 KB / 272 ln, untouched since 6/22, unregistered in FILES. Reads as a live dialogue surface. | V16_RED_DIALOGUE.md:14; last commit 2026-06-22. Referenced only from `MAINTENANCE.md:93` (its own creation record). | **HYGIENE** | **P3 — SAM** |
| 10 | `INFRA_AGENDA.md` | `Status: SCOPING — Will to decide` since capture 2026-06-26; **untouched 7 weeks, no dated rewrite trigger.** Its own §2 says the eval suite is "~2 of 5 cases built" — still 2. A decision surface parked indefinitely with no expiry. | 3,267 B / 26 ln, last commit 2026-06-26. Not in CLAUDE.md FILES table. `finding_dated_carry_item_has_no_expiry_check`. | **HYGIENE** | **P3 — PROME/Will** |
| 11 | `LAST_COMPLETION.md` | Stale 7/29 (19 days, ~12 sessions) on a surface **whose name promises currency**. **BUT: fleet class, not SAM's defect** — `PROME/COMPLETION_SPEC.md` re-keyed delivery method 1 away from this file on **8/13**, and **18 agents still carry one**. Classic `finding_a_ruling_governs_the_next_write_not_the_existing_state`. | SAM `LAST_COMPLETION.md` 2026-07-29 (`1ee62bf4d`). COMPLETION_SPEC.md:3 (8/13 re-key, cites `finding_completion_stamp_skip_reads_as_current`). Peers: HANS 7/16, CREED 7/27, BOND/BROCK 7/28, RED/TERRY/LIQUID 7/29 … REGINALD already archived its own 7/30. | **HYGIENE** | **P2 — DAEDALUS/PROME (fleet retro-sweep, NOT a SAM packet)** |
| 12 | `MEMORY.md` | 103 lines against its own stated 100-line cap. | MEMORY.md:3 (`Cap at 100 lines`); `wc -l` = 103. | **TRIVIA** | P3 — SAM |

### Checked and CLEAN (reported so the negative is on the record)
- **Position-state consistency (Q3):** STATUS / TRADE / STRATEGY / NEXUS_BRIEF **all agree — FLAT, $0 at risk, nothing executed.** No contradiction found.
- **Two-state rule, executed well:** `TRADE.md` + `STRATEGY.md` carry correct `⚰️ HISTORICAL AS OF 2026-08-07 — DO NOT TRADE OFF IT` banners with corrected basis. **`VX.tsv` + `FLOW.tsv` were FROZEN today (8/17)** with canonical banner wording, off a KURA Run-11 escalation — a live two-state ruling made *during* this review.
- **`claim_check --check weekday`** on CATALYSTS.tsv / CALENDAR.md / STATUS.md → **clean, 3 files.**
- **Two candidate findings withdrawn on verification:** (a) KURA's `VX-SAM-11.02` two-run-unapplied flag — **closed today** by the FROZEN ruling; (b) METSUKE's "4th-surfacing version pointer" at TRADE L188 — reads `v1.6.11 — 2026-08-02` inside a banner-marked historical doc, which is **correctly-historical** per METSUKE's own dated-anchor ruling (`METSUKE_MEMORY:1243`). Neither is a defect.
- **7/29 self-declared TIMELINE debt** ("owed next session") — **satisfied 8/7**, +15 lines covering the frame break. Not an open debt.

---

## VERDICT — does SAM's spine match its contract?

**Largely yes, and by a wide margin relative to the fleet — the failure is narrow, deep, and in exactly one place: the owner doc.**

The specified process demonstrably runs. Boot executes (market refresh, WALTER lane drains, `boot.py` fetchers writing ledgers). Closeout executes (MEMORY rewritten, CHANGELOG logged, consumer notices sent). The 250-line cap is genuinely enforced through real compression passes. The Amendment-10 brief-ordering rule — the one most agents fail — **held 4-of-4 across completed sessions (8/7, 8/10, 8/13, 8/14)**, verified against commit timestamps, not self-report. The two-state ledger rule is not merely obeyed but actively *adjudicated*: SAM froze VX and FLOW today with correct canonical wording. This is not a decorative contract.

**The sub-agent staff is emphatically live, and is SAM's strongest structural asset** (Q5 answered): KOYOMI Run-16, METSUKE Run-15, and KURA Run-11 all ran and closed out **on 8/17**, each with SAM adjudicating dispositions and recording accept/decline calibration in the pair-file. More telling than the cadence is the *quality of the disagreement* — KURA's own falsified A1 claim corrected on its own report; METSUKE tracking a flag to its 4th surfacing; SAM retracting half of its own instrument diagnosis the same day. This is a working internal audit loop, not three files that exist.

**But the contract has one systematic blind spot, and it is the doc the contract calls boot step 1.** Every *derived* surface — STATUS, TRADE, STRATEGY, NEXUS_BRIEF — propagated the Will-ratified 8/11 basis correction. `THESIS.md` did not, at 11+ live sites, despite being committed 8/13, two days *after* ratification. SAM's own `RECONCILIATION.md` was written for precisely this class and diagnosed it exactly backwards — "drift hid in the *derived* docs, not the owner doc" — so the sweep it institutionalizes runs owner→derived and structurally cannot catch an owner-doc miss. **The reconciliation discipline is sound; its direction of travel has one gap, and the gap is where the drift now lives.** F2 is the sharp end: a stale MED-HIGH grade sitting in the section built for other agents to consume.

Finding 3 is the one that generalizes past SAM. The 250-line cap is not being gamed deliberately — SAM does real compression work — but the metric has quietly stopped measuring the thing it governs. This is the identical failure the fleet already diagnosed at `MEMORY.md` on 8/3 ("rows became long single lines, so the file grows in bytes while the line count barely moves"), where DAEDALUS added a `soft_bytes` tier the same day. **That lesson was fixed at one instrument and never generalized to the per-agent caps.** SAM is the proof that the class is live and unguarded elsewhere; it is very unlikely to be the only agent.

---

## (a) NOT-READ LIST

Read in full: `CLAUDE.md`, `LAST_COMPLETION.md`, `INFRA_AGENDA.md`, `profiles/SAM.md`.
Read partially (headers, banners, targeted greps, git-verified — **not** end-to-end):
- `STATUS.md` (56 KB) — header + stamps + size history; **body not read line-by-line**
- `NEXUS_BRIEF.md` (68 KB) — CURRENT STATE block + As-of stamp only
- `TRADE.md` / `STRATEGY.md` (55 KB / 75 KB) — banners + targeted sections
- `thesis/THESIS.md` — targeted basis/version/cross-agent greps; **full pillar + channel argument not read**
- `MAINTENANCE.md` (105 KB / 769 ln) — header only. **Q4 mega-file question only partly answered here.**
- `METSUKE_MEMORY.md` (333 KB), `KURA_MEMORY.md`, `KOYOMI_MEMORY.md` — run-log tails + size only
- `MOF_INTERVENTION_PLAYBOOK.md`, `RECONCILIATION.md`, `board_log.tsv` — headers only

**Not opened at all:** `thesis/PREDICTIONS.tsv` and `PREDICTIONS_ARCHIVE.md` (profile's claimed crown jewel — **prediction discipline is therefore UNVERIFIED by me this pass**, and my scoreboard figures are quoted from STATUS/BRIEF, not from the ledger), `thesis/CHANGELOG.md`, `docket/CALENDAR.md` + `CATALYSTS.tsv` bodies, `scripts/` (12 py), `insurers/`, `red/`, `evals/`, `research/outputs/`, `workbook/` TSV bodies, `archive/`, `inbox/`+`outbox/` contents.
**Not re-checked by instruction:** today's `jgb_auctions` / `fxy_options` / `cpi_japan` fixes and the model self-retraction.

## (b) TOP 3 BY CONSEQUENCE

1. **F2 — `THESIS.md:299` tells HENRY the carry-unwind tail is MED-HIGH/PROVISIONAL when it is RETIRED-TO-LOW.** Highest consequence because it is a *cross-agent* claim in the *owner* doc: a consumer following the documented route reads a live grade that every other SAM surface has retired. Wrong-direction risk, not merely stale.
2. **F1 — the retired `−180K / 25.3%` basis is live at 11+ sites in `THESIS.md`, boot step 1.** SAM re-reads this every session; it is the seed from which the retired denominator gets republished. Bounded by the forum ruling that "contract gates unaffected, only labels moved" — no verdict is wrong — but it is the single largest concentration of superseded figures in the tree, and the reconciliation sweep is directionally blind to it.
3. **F3 — the 250-line cap now governs a dimension that stopped moving (+59% bytes at a pinned line count).** Consequence is fleet-wide, not SAM-local: the byte-vs-line lesson was learned at `MEMORY.md` on 8/3 and fixed at exactly one instrument. Every per-agent line cap in the fleet is presumptively exposed to the same evasion, and nothing currently measures it.

**Routing note:** F1/F2/F4/F5/F6/F8/F9/F12 → SAM (packet; SAM is LIVE — do not edit). F3/F7/F11 → **DAEDALUS's own lane** (cap-metric generalization, sub-agent pair-file governance, LAST_COMPLETION fleet retro-sweep). F10 → PROME/Will.
