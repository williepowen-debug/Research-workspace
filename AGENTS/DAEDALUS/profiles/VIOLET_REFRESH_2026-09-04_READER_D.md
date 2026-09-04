# VIOLET Profile Refresh — READER D (predictions · KB · research · reports · corrections · cross-desk)

**Read-only Mode-A pass · 2026-09-04 (Fri) · DAEDALUS**
No file outside `AGENTS/DAEDALUS/` written; no `AGENTS/VIOLET/scripts/` script run — KB conformance re-derived independently in `awk`.

---

## 1. PREDICTIONS — a split registry, no `PREDICTIONS.tsv`

`find AGENTS/VIOLET -iname "*PREDICT*"` → **zero files.** Forward predictions live in three disjoint places; nothing joins them:

- `thesis/VIX_THESIS.md:426-448` §PREDICTIONS — the numbered series **#1–#7** + scoring rules; the nearest thing to a register.
- `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md:95-173` — `VIO-FOMC-0916`, 5 legs + grade card, frozen 9/2.
- `workbook/KB.tsv` `Stale_By` — the de-facto resolve date for everything else (KB-VIO-216/218/222/224/227/237).
- `PROME/GATES.tsv` — **no live VIOLET row** (20 gate_ids; the sole `GATE-VIO-RV1` string sits inside `GATE-REG-T02`'s precedent note); `PROME/DOCKET.tsv:49` carries one VIOLET row, **RESOLVED**. `FORGE/PREDICTION_DISCIPLINE.md:31` cites VIOLET once, as an instance that *ratified* the WQ-162 basis rule (the `^SKEW` 8/28 bar).

### 1a. OPEN forward predictions

> **Slippage: none.** Every resolve date below is unreached except the three marked ⚠️. No prediction in this set has slipped or silently passed.

| ID / leg | Claim | Resolve | Anchor TYPE | Grading source |
|---|---|---|---|---|
| `VIO-FOMC-0916` **LEG 1** | ΔVIX 9/15→9/16 **> −3.66%** (void if VIX>16 on 9/15) | **9/16 close** | FIXED calendar | `^VIX` close, yfinance gap-checked vs CBOE (KB-VIO-215) |
| **LEG 2** | ΔVIX 9/16→9/23 **> 0**; KILL < −1.41% | **9/23 close** | FIXED calendar | same |
| **LEG 3** | branch map A/B/C, ≥2-of-3; whole-map NULL possible | **9/16 + 9/18** | **EXPECTED EVENT** (FOMC stmt) — letter declares it **voids rather than slips** | VIX3M/VIX, VVIX, `MOVE.tsv` |
| **LEG 4** | MOVE %Δ 8/26→9/16 **>** VIX %Δ 8/27→9/16 | **9/16 close** | FIXED calendar | `workbook/MOVE.tsv` (basis pinned, letter §6.2) |
| **LEG 5** | contango roll not misread across 9/15→9/16 | 9/16 | FIXED calendar | `VX_DAILY.tsv` `m1m2_adj_pct` (KB-VIO-218) |
| **KB-VIO-222** | `^SKEW` ≥150 sustain-4 (**RED-owned FT-10**; VIOLET counts) | **9/10**; earliest fire **9/9 close** | FIXED chain 9/3·9/4·9/8·9/9 | CBOE `SKEW_History.csv` — **1 of 4, ARMED** (`STATUS.md:83`) |
| **KB-VIO-237** | dealer gamma negative, flip 7,689–7,699 | **9/18** | FIXED | **HENRY** `gamma_flip.py` — VIOLET does not own it |
| **KB-VIO-224 · 227** | NFP hawkish under inverted reaction fn · FedWatch 12–18pp above prediction markets | **9/16** | FIXED | BLS/FOMC · venue quotes |
| **KB-VIO-159 · 173 · 011…018** | H3-prime basis · CCC month-end artifact · 8 founding-literature thresholds | **10/31 · 9/30 · 10/12** | FIXED | own · FRED · literature |
| **KB-VIO-175 · 184 · 185** | cheap-tail arming · BIN-A re-base · FRED 3y window | ⚠️ **9/04 = TODAY**, unresolved at the 17:19 commit | FIXED | own |
| **KB-VIO-230** | TRADE.md ARMED framework | ⚠️ **9/05** — body resolved 9/4 (WQ-177), row due tomorrow | FIXED | own |
| **Thesis #1 / #2' / #4** | HY>400bps→VIX>30 · sustained inversion · VIX>40→HY>600 | **"Next event" — NO DATE** | ⚠️ **UNANCHORED** — no resolver at all; cannot slip because it cannot be scheduled | unstated |

### 1b. Graded in the last 30 days (8/05 → 9/04)

**KB-VIO-196** (8/18) 8/5 SOQ counterfactual — *exiting beat holding*, grade **13 days late** · **KB-VIO-200** (8/20) MOVE pause/resume — *re-arm completed 8/18 while dark, nobody collected it* · **KB-VIO-211** (8/27) F2 pre/post-2018 split — **FAIL**, `GATE-VIO-RV1` retired by its own registered kill · **KB-VIO-220** (9/2) **Prediction #7 — clean HIT on the day** (HENRY SKEW 20d cross-back, 141.13) · **KB-VIO-230** (9/4) 7/1 tail-hedge framework — gates PENDING on a 7/2 print **64 days** → RETIRED-SUPERSEDED · **KB-VIO-233** (9/4) post-NFP vs pre-open card — **NULL on level, divergence widened on structure**.

**Brier / score surface: DOES NOT EXIST.** No scoring ledger, hit-rate tally or calibration file anywhere under `AGENTS/VIOLET/`. `VIX_THESIS.md:444-450` defines six verdict labels; nothing aggregates them, and the verdicts are not co-located with the numbers they grade (§7 item 1).

---

## 2. KB.tsv health

| Metric | Value |
|---|---|
| Rows / bytes | **243** data rows (244 lines) / **548,743 B**; mean row **2,250 B**, largest KB-VIO-242 at **5,830 B** |
| Structure | **244/244 lines = exactly 13 fields** (0 ragged) · IDs `KB-VIO-001`…`243` **0 dupes / 0 gaps / 0 malformed** · `DerivedFrom` **600 refs, 0 orphans, 0 self-refs** · required fields 1–9 **0 empty cells** |
| Status | ACTIVE 173 · CONFIRMED 43 · CORRECTED 12 · SUPERSEDED 10 · STALE 5 — all in `SCHEMA.tsv:10`; **no CONTESTED/RETRACTED exist in this schema** |
| Epistemic · Conf · Group | EMPIRICAL 233 / ESTIMATE 7 / ASSUMPTION 3 · A1 162 / A2 45 / B2 26 / C3 7 / C1·B1·B3 1 each (all valid Admiralty) · VOL 178 / META 40 / CREDIT 15 / MACRO 5 / **CREDIT_SPREADS 5** |

**Conformance clean on every enforced column** — the `validate_workbook.py` wiring (boot stage 11, added 7/30 after 11 rows had violated, one for 109 days, `CLAUDE.md:47`) is holding. ⚠️ Soft item: `CREDIT` and `CREDIT_SPREADS` both appear in `Group` — probable near-duplicate token, not a validator failure.

**Growth:** 11.7 rows/wk lifetime; **56/30d · 35/14d · 30/7d · 23 on 9/4 alone**; **8,006 B/day** at the 14d rate → 700 KB inside 20 days.
**Stale_By breach:** 89 ACTIVE + 11 CONFIRMED = **100 of 216 live rows (46%)** past review date, oldest 2026-04-22; **64 more ACTIVE rows carry none** → only **20 of 173 ACTIVE** have an un-passed date.
**Rotation / cold plan: NONE** — no two-state plan, no `Last real data refresh:` header. Details → §7 items 2–3.

---

## 3. Research corpus — 47 files

**22 top-level `.md` + `RESEARCH_SUMMARY` + 24 across 6 subdirs.** Ages vs 2026-09-04: **22 files at 143d** (the 2026-04-12 founding corpus) · 4 at 140–141d · 1 at 123d · 6 at 81–94d · 2 at 53d · 1 at 44d · 2 at 35d · 5 at ≤7d.

Rule applied: root canon (>60d AND not boot-read AND not referenced by a live doc) + root clause ② (an **index/nav** reference doesn't count) + VIOLET's own transitivity clause, `README.md:28` — *"a reference only counts if the referrer is neither the file itself nor also being retired."*

### Retirement-eligible: **12 files** (not ~20)

- **Zero referrers, 143d:** `credit_vix_lag/CREDIT_VIX_LAG_REPORT.md` · `credit_vix_lag/FOUR_MODEL_SYNTHESIS.md` · `crisis_analogs/feb2021_meme_stocks.csv` · `crisis_analogs/mar2020_pandemic.csv`
- **Zero / archival referrer, 81–84d:** `2026-06-14_stale_data_audit.md` (none at all) · `2026-06-11_march_episode_ccc_analog.md` (only an `inbox/processed/` packet)
- **Transitive, 143d:** `credit_vix_lag/lead_lag_analysis.csv` — sole referrer is CREDIT_VIX_LAG_REPORT, itself a candidate
- **`RESEARCH_SUMMARY.md` only — an index surface, which does not count (root clause ②), 143d each, 5 files:** `credit_vix_lag/2026-04-12_Davernas_…` · `regime_patterns/{Cole_Artemis, VIX_Seasonality_FOMC_Effects}` · `term_structure/{Fed_Volatility, Hosker_Djurdjevic}`

**Correctly NOT eligible** (checked, kept): `analog_2024_cluster/{daily.csv,tells_table.md}` (cited by live scripts `analog_pull.py`/`analog_timeline.py`); `crisis_analogs/feb2018_vix_spike.csv` (chained to a KB-cited analog); the seven crisis-analog `.md` files, rescued by the 8/04 source-citation pass (`MEMORY.md:32` — *"a reference-count sweep found all seven … at ZERO inbound references"*, and VIOLET added citations rather than retiring). Correct disposition.

**On "~20": no 9/4 VIOLET flag of ~20 candidates exists.** Nearest is the `RESEARCH_SUMMARY.md` scope banner (7/30) — *"~20 further files have been added since"* — a claim about **additions, not retirements**, itself understated (true post-4/12 top-level additions: **22**). Retirement precedent = `archive/retired_2026-07-30/README.md` (two-pass sweep, 13 files moved, warns *"the naive reference check … erred toward keeping"*) — **36 days old, no successor.**

---

## 4. `reports/` — 3 files, all orphaned

| File | Age | What it is | Closed? |
|---|---|---|---|
| `2026-07-11_domain-sweep.md` | 55d | Triage inventory: ungraded predictions, ledger drift, thesis/KB disagreement. Zero fixes applied **by design**. | 4 markers. **Its §1 top item — thesis row #6 out of sync with KB — has recurred** (§7 item 1). |
| `2026-07-11_threads-sweep.md` | 55d | Round-3 missed connections: canary map, JPY-vol gap, single-issuer mask, thesis tail rot, brief staleness. | **ZERO closure markers.** Canary map + JPY-vol built (KB-VIO-117/120); **single-issuer mask calibration** and **thesis tail prune** have no disposition since 7/11. |
| `2026-08-04_staleness-sweep.md` | 31d | Mechanical sweep whose headline was a **live market event** — SKEW −9.68% to 126.41, 6th-largest 3y drop, sitting unrecorded. | 12 markers; §2 updated in place, **5 rows CLOSED.** Best-closed of the three. |

⚠️ **None is referenced by any live VIOLET doc.** Two are >60d and formally retirement-eligible — but they are the only record of open triage items, so the disposition is **close them out, not archive.**

---

## 5. Corrections

`registry/corrections_receipts.tsv` — **80 bytes, one receipt:** `2026-09-03T00:32Z · COR-20260826-01 · NO-OP · <empty note>`

- **Owed by VIOLET: none.** `scripts/corrections_boot_check.py VIOLET` → **rc=0** (*"0 unreceipted NAMED rows … register 6 rows; receipts on file: 1"*).
- **Owed to VIOLET: one, already actioned.** `COR-20260826-01`, WALTER-authored, target VIOLET (`WALTER/registry/CORRECTIONS.tsv:14`) — SIG-W-20260809-018's rate-adjustment leg INVERTED, class FLIP, resolve-by 2026-09-09, still `LIVE` at source. VIOLET receipted **NO-OP** correctly: *"the clause was audited 8/27 and never carried"* (`MAINTENANCE.md:144`).
- ⚠️ **The `note` column is empty on the only row on file** — the rationale sits one file away (`MAINTENANCE.md:144`), not on the surface a checker reads. ✅ This receipt was the **real block case** that verified DAEDALUS's own R1 boot leg (`archive/EVOLUTION_ARCHIVE_2026-09.md:11`).

---

## 6. Cross-desk dependencies

**Citing VIOLET:** 27 files match `KB-VIO|VIOLET`; explicit `KB-VIO-` id citations outside VIOLET's dir total **7 across 6 files** — `RED/NEXUS_BRIEF.md` (2) · `HENRY/STATUS.md` · `PROME/{GATES_README, WILL_QUEUE, HEARTBEAT_COLD, ORCHESTRATION_PLAYBOOK}` (1 each). KB's own `Vectors` column routes to **19 desks / 454 arrows** (->NEXUS 94 · ->PROME 82 · ->RED 77 · ->HENRY 70 · ->LIQUID 23 · ->TERRY 22 · ->FORGE 21 · then ≤13). **Publish-intent is ~65× measured inbound id-citation.** Consumption runs through `NEXUS_BRIEF.md` by design (`CLAUDE.md:53`) — so a superseded KB id is not greppable at the consumer.

**External figures VIOLET carries:**

| Figure | Owner | Value / vintage · Stale_By | State |
|---|---|---|---|
| Dealer gamma flip **7,689–7,699**, Net GEX ≈ −$16B/1% | **HENRY** | 9/2, `gamma_flip.py` CBOE-direct · **9/18** (KB-VIO-237) | ⚠️ adopted 9/4 — VIOLET **published "unmeasured" twice on 9/4 while the measurement sat in its own inbox** (`STATUS.md:7`); sign had **inverted inside 12 unmeasured days** |
| **RED-FT-10** `^SKEW` ≥150 sustain-4 | **RED** | 9/3 bar 150.63, CBOE-confirmed · **9/10** (KB-VIO-222) | **1 of 4, ARMED, NOT FIRED**; `STATUS.md:83` carries a KILL-ON-SIGHT on *"FT-10 fired"* |
| **MU FQ4 date** | **VULCAN** | **2026-09-30 16:30 ET**, Micron 8/26 release, VIOLET's own primary fetch | ✅ resolved — VIOLET's `~9/29` was 1d off and it **overwrote it with VULCAN's `~9/22` (8d off) twice** (KB-VIO-235). ⚠️ **Flagged back, not edited:** `VULCAN/workbook/PREDICTIONS.tsv` rows 3/12/13 still carry an **inverted headroom clause** (`STATUS.md:158`) — open at VULCAN |
| **MOVE** 77.88 [9/1] vs brief's 79.71 [9/2] | VIOLET | reconciled — *"one series, adjacent vintages"* | ✅ CLOSED (`STATUS.md:152`) |

---

## 7. TOP 5

**1 · The only numbered prediction registry is out of sync with its own grades — second time, same table.** `VIX_THESIS.md:442` row **#7** still reads *"Untested; live-testable"*, under a status column headed **"Status (6/6)"**. **KB-VIO-220 graded #7 a clean HIT on 9/2** (packeted to HENRY, `FLOW.tsv:29`). Identical to the defect `reports/2026-07-11_domain-sweep.md` §1 raised on row **#6** — fixed then by a **one-row edit, not a mechanism**, so the class returned in 54 days. `VIO-FOMC-0916`'s 5 legs are in **neither** registry.
→ A grade that exists is invisible at the surface a reader travels; the hit-rate is unreadable and unscoreable. `[[finding_transfer_completes_only_when_the_receiver_encodes]]` · **VIOLET** (sync + wire a check); **DAEDALUS** if it generalises fleet-wide.

**2 · 46% of live KB rows are past their own `Stale_By`** (§2; oldest breach 2026-04-22, KB-VIO-029/049, 135 days). Nothing at boot reads the column: `validate_workbook.py` enforces **enums**, `canary_staleness.py` watches **ledger tails**, `read_cap_check` cannot see KB.tsv at all.
→ A declared review contract with **no enforcing mechanism** — PAT-071 / `CHECKS.tsv` class; ACTIVE certifies currency it never checked. `[[finding_dated_carry_item_has_no_expiry_check]]` · **VIOLET** (triage) + **DAEDALUS** (register the check — this column exists in every fleet KB).

**3 · A 549 KB ledger with no two-state plan, growing ~8 KB/day, invisible to every size guard** (§2). `CLAUDE.md:47-48` makes KB.tsv a write-target not a boot read, so `read_cap_check --agent VIOLET` reports **rc=0 over 4 files**. MEMORY, MAINTENANCE and STATUS were each split under pressure this fortnight (`MAINTENANCE.md:141,168,221`); KB was not.
→ Root Data Hygiene's two-state rule (FROZEN **or** LIVE-with-vintage-alert) unmet — the silent-rot middle, on the desk's richest artifact. · **VIOLET** + **DAEDALUS** (the read-cap perimeter cannot see non-boot-read ledgers — a gap in my own instrument).

**4 · `STATUS.md` is 32,546 B against a 32,550 B budget — four bytes of headroom**, after two rotations on 9/4 (33,311 → 31,788 → 32,546); `read_cap_check` already flags it **🟡 rotate-tier**. The next sentence written breaches, and the 9/4 RESEARCH QUEUE closes with **three 🔴 items** that will each want STATUS bytes. ⛔ The budget is not raisable.
→ A breach means the next session boots on a truncated dashboard. · **VIOLET** — rotate **before** the next write, not after.

**5 · 12 research files are retirement-eligible (sweep lapsed 36 days), and the reports holding the open triage items are themselves orphaned** (§3, §4). ⚠️ `MAINTENANCE.md:72` (*"`research/` … and `reports/` deliberately left alone"*) is a rule about **not editing** the historical trail; it reads as an exemption from **moving** it, and `archive/retired_2026-07-30/README.md` proves the desk knows the difference.
→ Corpus rot on one side, silently-abandoned open items on the other; the transitive rule at `README.md:28` exists and is simply not being run. · **VIOLET** (sweep + close the threads-sweep items); **PROME** if those items need re-prioritising rather than closing.

---

## Notes for `profiles/VIOLET.md`

- **Strengths:** in-ledger hygiene is the best I have measured (§2), and the pre-registration habit is real — the NFP card was written **after** the print and **before** the open; the FOMC letter freezes state, declares NOT-GRADED conditions in advance, names its own five weaknesses, and **states the resolver anchor TYPE per leg** (`letter:173`). L3 falsification-surface behaviour done properly.
- **Recurring shape across all five findings:** VIOLET fixes the *instance*, not the *mechanism*, and the class returns — row #6 → row #7 (54 days); the 8/04 crisis-analog reference gap → the same gap in 12 other files; STATUS rotated twice in one day and still at 99.99% of budget. KB-VIO-243 is the desk saying this about itself (*"I got the same guard wrong three times"*). It diagnoses the class correctly and does not yet generalise its own remedies — the layer DAEDALUS owns.
- **Do-not-touch:** `research/`, `reports/`, `outbox/delivered/` are immutable historical record (`MAINTENANCE.md:72`) — retirement *moves* are legitimate, content rewrites are not. KB rows are marked SUPERSEDED/CORRECTED in place, never deleted (`CLAUDE.md:47`).
