# PRODUCTION REVIEW #6 — READER REPORT · COHORT R5 (Florida / climate / housing / insurers / regional banks)

**Reader:** DAEDALUS fan-out reader R5 · **Date:** 2026-09-17 (Thu) · **Review period:** 2026-09-01 00:00 → 2026-09-17
**Desks:** CORAL · MARCO · AEOLUS · HOMER · SHADE · REGINALD
**Mode:** read-only. Every claim below carries a `path:line` or a commit hash. Where I could not ground a verdict I wrote NOT-ADJUDICATED or CANNOT-EVALUATE rather than guessing.

> **Instrument note (binds every byte figure below):** `python3 scripts/read_cap_check.py --agent <X>` grades **% of BUDGET (32,550 B)**, not % of the 54,250 B cap. Several desk-side claims in this period are stated in %-of-cap. I use %-of-budget throughout and say so where the two disagree.

---

## CORAL — Market · FLEET_MAP L3 / Conf H / last_scored 2026-09-05

### 1. Period production
| Metric | Value |
|---|---|
| Commits touching `AGENTS/CORAL/` since 9/1 | **16** |
| Self-authored (subject starts `CORAL`) | **4** — `70025dcc3` 9/2 · `53dc298b6` 9/2 · `7035b2b3b` 9/13 · `cd8da96a9` 9/13 |
| Routed-in | **12** |
| Last self-commit | **2026-09-13** |
| Dark-days now | **4** |

**What shipped:** two working sessions. 9/2 (`70025dcc3`) — MSI reading #5 breaks breadth 3-of-5, clock starts, leg HOLDS 🔴; the FMHPI-excludes-condos finding that **dissolved CORAL's own "three statewide signs"**; read-cap split 95,195 B → 26,730 B. 9/13 (`7035b2b3b`) — **MSI-01 reading #6 GRADED 4-of-5 ⇒ leg STANDS DOWN 🔴→🟠**, i.e. a pre-registered stand-down rail fired *against the desk's own live call*. `cd8da96a9` folded it into NEXUS_BRIEF with the Parcl-listings caveat.

### 2. Row-claim test
| # | Claim in `Gaps` / `Next_upgrade` | Verdict | Locator |
|---|---|---|---|
| 1 | Read-cap split executed 9/2, STATUS 161 ln boot-read whole | **REFUTED IN PART** — the split happened, but STATUS has **regrown +5,051 B in 11 days** (27,442 B @`53dc298b6` → **32,493 B = 100% of budget**, 57 B of headroom). The 9/2 rotation stopped in the 75–100% band and re-breached, which is the PAT-055 regrowth case rule 5's second threshold exists to prevent. | `git show 53dc298b6:AGENTS/CORAL/STATUS.md \| wc -c`; `read_cap_check --agent CORAL` |
| 2 | `thesis/THESIS.md` v1.1, rails 8/23, carries a DATED `Next falsify grade: 2026-11-15` | **TRUE-STILL** | `AGENTS/CORAL/thesis/THESIS.md:3-4` |
| 3 | ⭐7 Trepp gap CLOSED (clean negative reported as asked) | **TRUE-STILL** (nothing in-period reopens it) | FLEET_MAP CORAL row; no contrary artifact found |
| 4 | 🔴 F-1: **no TRADE surface at all** — L4 gated on a ruling nobody would produce; cheap path = a declared-flat `TRADE.md` in ZHAO's form | **TRUE-STILL — still absent.** `find AGENTS/CORAL -iname "*TRADE*"` returns only an inbox packet and an unrelated `sources/` file. CORAL has **accepted** the finding and deferred: *"DEFERRED, not refused — accepted that it is not Will-blocked."* | `AGENTS/CORAL/SCRATCH.md:31`; `AGENTS/CORAL/STATUS.md:163` |
| 5 | F-2: CORAL's intl migration figure carries no year and no source | **REFUTED — FIXED 9/13.** Now reads `+178,674 (2025 annual Census vintage — Census Vintage 2025 state population estimates, components of change; stamped 2026-09-13 per DAEDALUS 9/5 reconcile)`, with the −56.5% vs −57% arithmetic shown and the "the two desks CORROBORATE" sentence carried. | `AGENTS/CORAL/STATUS_DETAIL.md:49` |
| 6 | Oldest un-worked item = Amendment 3 item E (Judge David Frank, 2nd Judicial Circuit; Nov-3 hard clock) | **TRUE-STILL**, and now **4 failed attempts**; CORAL has itself diagnosed the fix (court dockets, not news outlets) and not executed it. | `AGENTS/CORAL/STATUS_DETAIL.md:277`; `AGENTS/CORAL/SCRATCH.md:28` |
| 7 | Next_upgrade: "then Citizens' early-Sep observable" | **TRUE-STILL — still owed.** STATUS carries `Citizens 8/31 month-end … **owed now**` twice, at the 9/13 write. | `AGENTS/CORAL/STATUS.md:66`, `:124`, `:175` |
| 8 | "MARCO reconciliation DONE" | **TRUE-STILL** — both halves shipped (CORAL 9/13, MARCO 9/17 `FIGURES.md:77`). | `AGENTS/MARCO/FIGURES.md:77` |

### 3. Ladder walk (Market, current L3 → next L4)
| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L1 | STATUS + labeled BOTTOM LINE | **MET** | `AGENTS/CORAL/STATUS.md:165` `## BOTTOM LINE` |
| L2 | structured record, valid schema, accruing | **MET** — `workbook/KB.tsv` 166,784 B, `VX_Vectors.md`, `board_log.tsv` 30,005 B all live | `AGENTS/CORAL/workbook/` |
| L3 | convergence matrix + exit rules | **MET** — 10-pillar grid + the MSI stand-down rail with a two-reading ≥10-day-apart condition | `AGENTS/CORAL/thesis/THESIS.md:5` |
| L3 | predictions resolving | **MET** — MSI-01 readings #5 and #6 both graded in-period, #6 *against* the desk's own 🔴 | `7035b2b3b` |
| L3 | **dated falsification surface** | **MET — cohort exemplar.** Six FROZEN criteria, a scoring rule (≥4 MET ⇒ downgrade candidate; HALF = 0.5; UNGRADED = 0 **and obliges an instrument note**), a no-rewording clause, a first-ever score (1.5 of 6) and a dated next grade. | `thesis/THESIS.md:63-118`, esp. `:102-105`, `:118` |
| L4 | **TRADE.md feeding proposals** | **NOT MET** — no TRADE surface exists (row-claim 4) | — |
| L4 | signals flowing | **MET** — `fcbcf5be2` routed MSI #5 to PROME/RED/CREED/HOMER/MARCO; `5ee4908f0` superseded MARCO's MSI cell | `fcbcf5be2`, `5ee4908f0` |

**Recommendation: HOLD L3, Conf H.** Exactly one L4 leg short and it is the same leg as in July — but the *reason* has changed from "blocked on Will" to "deferred by CORAL", which is the outcome the 9/5 packet was for. Confidence H: I read the thesis rail, the STATUS_DETAIL fix and the TRADE absence myself.

### 4. Profile trigger
> `profiles/CORAL.md:4` — **"Staleness: 30-day clock (its own, tighter than fleet default) → checkpoint 2026-10-05"**

**NOT FIRED** (18 days out). Profile body dated 2026-09-05 and still accurate on identity, the read-cap split and the MARCO reconciliation. **One statement now out of date:** the profile's §2 read-cap paragraph reads as settled; STATUS has since regrown to 100% of budget (row-claim 1). Not a trigger leg, but it should be re-cut at the 10/05 checkpoint.

### 5. Falsification read — **not in scope** (CORAL is not on either list; its surface is scanner-visible and dated 11/15).

### 6. Negative-resolution leg
**Ledgers opened:** `workbook/FL_Forward_Log.md` (47 table rows, `Status` column), `thesis/THESIS.md` §Confirm/Falsify grade table. CORAL has **no `PREDICTIONS.tsv`** — its scored instrument is the six-criterion falsify table.

| Row | Negative? | Names a SEARCH INSTRUMENT? | Dated search-attempt precondition? |
|---|---|---|---|
| Criterion **5** "Bankruptcy acceleration fades per-capita" — graded **UNGRADED (0)**, *"Untracked June→August. Neither met nor refuted — unobserved."* | ✅ pure negative-by-absence | **PARTIAL** — an *instrument note is owed*, and the note names the series (Ch.7 per-capita M.D./S.D. Fla, tripwire >~230/100k) but **the instrument is unbuilt**. STATUS says criterion 5 "scor[es] 0 again if it stays that way." | ❌ none |
| Criterion **6** "Property-tax relief lowers carrying cost" — **PENDING (0)**, Amendment-3 ruling *unlocated* | ✅ resolution blocked by a failed search | ❌ — news outlets tried and failed 3–4×; the correct instrument (court docket, 2nd Judicial Circuit) is **named as a next step, not registered** | ✅ dated attempts (8/3, 8/23, 9/2) are logged — this is the good half |
| `FL_Forward_Log.md:16` Ocala June UR residual | ✅ | ✅ BLS LAUS metro | ❌ still `⏳ Pending` since 7/29 |

**Counts: candidates opened 3 · confirmed negative-class 3 · lacking a registered instrument 2 (criteria 5 and 6).**
⭐ CORAL is the only desk in the cohort whose grading rule **requires** the instrument note on an UNGRADED cell (`thesis/THESIS.md:103`) — the obligation exists and is unpaid, which is a far better state than the obligation not existing.

### 7. As-made receipt — **n/a**.

### 8. Cross-agent / pattern
- **→ CORAL (self):** criterion 5's instrument is the only thing standing between the 11/15 formal grade and a second consecutive 0-by-absence. 59 days of runway.
- **PATTERNS candidate (PATTERN):** *a rotation that stops inside the 75–100% band re-breaches on ordinary work* — CORAL rotated to 84% of budget on 9/2 and was back at **100% in 11 days** on two sessions of normal appends (+5,051 B). Rule 5's **two** thresholds are the fix and this is a clean measured instance. Evidence: `git show 53dc298b6:AGENTS/CORAL/STATUS.md | wc -c` = 27,442 vs live 32,493.

### 9. Reviewer-side defects
None found in the CORAL row. The 9/5 F-1 diagnosis (PAT-080, "a gate leg no one can clear is a hold, not a standard") **worked** — CORAL read it, accepted it and re-classified the item from blocked to deferred (`STATUS.md:163`). Record that as the rule paying out.

---

## MARCO — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-05

### 1. Period production
| Metric | Value |
|---|---|
| Commits touching `AGENTS/MARCO/` since 9/1 | **20** |
| Self-authored | **3** — `381028da8` 9/3 (s25) · `7541964af` 9/17 · `ba19ba661` 9/17 |
| Routed-in | **17** |
| Last self-commit | **2026-09-17 (today)** |
| Dark-days now | **0** |

**What shipped:** `381028da8` — read the Section 338 line list the fleet could not open since 8/22; energy (Ch.27) and potash (Ch.31) **CONFIRMED absent** by zero lines; 9/8 is not the auto date. `7541964af` (today) — **DOCKET L332: the ONE FL enrollment figure, 193,656 (−3.97% YoY)**, with the decomposition that matters (72% of the decline is pipeline turnover, only 25% is within-cohort attrition where out-migration can live) and an explicit ⛔ *"Migration pillar UNCHANGED; enrollment is NOT a migration direction tell without a voucher denominator."* Plus the Canadian 629-line perimeter, a 12-item drain and 6 as-made confidences re-derived.

### 2. Row-claim test
| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | Handle (1) **labeled BOTTOM LINE — 0 matches; LEGITIMATE GATE (L1 floor), still unmet, one heading** | **TRUE-STILL.** `grep -ci "bottom line" AGENTS/MARCO/STATUS.md` = **0**. Two more self-authored sessions have shipped since the finding without adding the heading. | `AGENTS/MARCO/STATUS.md` (no match) |
| 2 | Handle (2) **§2 universal 5-pt + Independence handles — 0 hits in STATUS or VX** | **TRUE-STILL.** `grep -ci "independence"` = 0 in **both** `STATUS.md` and `workbook/VX.tsv`; no 5-pt handle either. | `AGENTS/MARCO/STATUS.md`, `AGENTS/MARCO/workbook/VX.tsv` |
| 3 | Handle (3) PREDICTIONS_ARCHIVE / calibration scoreboard — **STRUCK, never a ladder leg** | **TRUE-STILL (and correctly struck).** Re-verified: Market L5 is *clean closeouts · zero YEYOU flags · current*; L3 asks only that predictions resolve. No archive exists and none is owed. | root `CLAUDE.md` §MATURITY LADDER |
| 4 | Substance: 57-vector VX, ledger_staleness wired, ML.tsv FROZEN banner, VX.tsv `STATE: LIVE` | **TRUE-STILL** — `workbook/` unchanged in character; `thesis/PREDICTIONS.tsv` 16 rows + `scripts/predictions_due.py` | `AGENTS/MARCO/workbook/`, `AGENTS/MARCO/thesis/PREDICTIONS.tsv` |
| 5 | MARCO's half of the F-2 fix: `FIGURES.md:77` notes the 2025 print beside the 2024 baseline | **REFUTED — DONE.** Now reads `+411K (2024) — ⚠️ a 2025 print exists: +178,674 (Census components of change, via CORAL; −56.5% YoY), carried in VX.tsv 3.04 since 9/17, **not re-verified at Census by MARCO*** — and the un-verified status is stated rather than hidden. | `AGENTS/MARCO/FIGURES.md:77` |
| 6 | "Citizens STATUS-vs-VX vintage split still UNVERIFIED (confirm-read)" | **CANNOT-EVALUATE** — I did not open both the STATUS Citizens cell and `VX.tsv`'s Citizens rows side by side; that is a confirm-read, not a scan. Needs: the two cells diffed at their vintage stamps. | — |

### 3. Ladder walk (Market, current L4 → next L5)
| Level | Leg | Verdict | Locator |
|---|---|---|---|
| **L1** | STATUS + **labeled BOTTOM LINE** | ⛔ **NOT MET** — 0 matches, three weeks after the finding was routed | `AGENTS/MARCO/STATUS.md` |
| L2 | structured record, valid schema, accruing | **MET** — VX 57 vectors, KB, FIGURES, COUPLINGS, baselines/ | `AGENTS/MARCO/workbook/` |
| L3 | convergence matrix + exit rules | **MET** (unlabeled but present: `Composite`/`NET` blocks) | `AGENTS/MARCO/STATUS.md` |
| L3 | predictions resolving | **MET** — 16 rows, 7 RESOLVED, 4 OPEN, `predictions_due.py` wired | `AGENTS/MARCO/thesis/PREDICTIONS.tsv` |
| L3 | dated falsification surface | **MET** — `thesis/PREREG_2026-07-31_floor_controlled_channel1.md` + `thesis/CHANGELOG.md` | `AGENTS/MARCO/thesis/` |
| L4 | TRADE.md feeding proposals | **MET** — `TRADE.md` 3,903 B present | `AGENTS/MARCO/TRADE.md` |
| L4 | signals flowing | **MET** — `d3c1fd1d8` MARCO → CORAL/PROME reconcile; `96810da37` MARCO → HAWK/CORAL/FERT/CARL/PROME | `d3c1fd1d8`, `96810da37` |
| L5 | clean closeouts | **MET** — today's closeout re-derived as-made confidences and rotated STATUS 35,523 → 33,789 B | `ba19ba661`, `7541964af` |
| L5 | zero YEYOU flags | **N/A** — default-zero instrument, WQ-181 ② ruled 9/10 (see §9) | `PROME/WILL_QUEUE.md:85` |
| L5 | current | **MET** — ran today | `7541964af` |
| — | read-cap | ⚠️ **rc=1**: `MEMORY.md` **49,058 B = 151%**, `STATUS.md` **33,789 B = 104%** of budget | `read_cap_check --agent MARCO` |

**Recommendation: HOLD L4, Conf H.**
⚠️ **State this plainly on the row: MARCO is an L4 desk failing an L1 floor leg.** Under a strictly cumulative reading of the ladder, a desk without a labeled BOTTOM LINE is not L1-complete and the grade is unsupported at every level above it. I am **not** recommending a demote — the gap is one heading over substance that is among the strongest in the fleet, and demoting on a formatting handle would be the PAT-080 error inverted. But the row should say *"L4 held over an unmet L1 leg, by exception"* rather than silently carrying the leg as a distant L5 item. That framing is itself a finding: the FLEET_MAP `Next_upgrade` cell reads *"L5 on TWO form changes"*, which presents an **L1 floor failure as an L5 upgrade** and is how it has survived two sessions of attention.

### 4. Profile trigger
> `profiles/MARCO.md:4` — **"Staleness: >45d → checkpoint 2026-10-20"**

**NOT FIRED** (33 days out). Profile body (2026-09-05) still describes the desk: identity, the three re-measured handles and the CORAL overlap all verify. **One statement now stale:** `profiles/MARCO.md:9` says *"STATUS **171 ln**"* and *"Last session **2026-09-03** (s25)"* — the desk has since run s26 (9/17) and STATUS is 168 ln / 33,789 B. Cosmetic, not trigger-firing.

### 5. Falsification read — **not in scope.**

### 6. Negative-resolution leg
**Ledger opened:** `AGENTS/MARCO/thesis/PREDICTIONS.tsv` (16 rows, `Status` col 6). **4 OPEN:** MAR-11, MAR-12, MAR-14, MAR-24.

| Row | Resolution class | Instrument named | Dated search-attempt precondition |
|---|---|---|---|
| MAR-11 H-2A certs >425K | positive threshold | ✅ DOL **OFLC** disclosure data, H1 FY2026 cited at 254,688 | ✅ FY-2026 close |
| MAR-12 Central America remittances −10% | positive threshold (reversal) | ✅ central-bank remittance series (Q1-2026 +9.1% YoY cited) | ✅ H2-2026 |
| MAR-14 CA produce prices +15% | positive threshold | ✅ **CPI fresh fruit & veg** | ✅ H2-2026 |
| MAR-24 All 3 FL airports negative simultaneously | positive conjunction | ✅ MIA/MCO/FLL monthly traffic | ✅ Q3-2026 |

**Counts: candidates opened 4 · confirmed negative-class 0 · lacking instrument 0.**
MARCO's open book is entirely **positive-threshold**, so the negative-resolution hazard does not arise here. That is a legitimate NOT-SEEN for the hazard class, not a clean bill for anything else — and it is worth recording, because a desk with no negative-class rows is the one place this canon has nothing to say.

### 7. **As-made receipt — DISPOSITIONED.** ✅
Packet `4f7fb2ec2` (2026-09-07) landed at `AGENTS/MARCO/inbox/processed/2026-09-07_from-DAEDALUS_as-made-confidence-audit-9-mismatch-candidates-harvest-H2.md`. Disposition executed **2026-09-17**:
- `AGENTS/MARCO/SCRATCH.md:19-20` — *"As-made audit (DAEDALUS 9/7) — re-derived at the Feb-24 blob `26e974d75`"*: **6 re-marks in the WQ-112 form · 5 SAME · 4 NOT re-derivable** (stated as unverified, not quietly kept).
- `AGENTS/MARCO/thesis/PREDICTIONS.tsv` — every OPEN row's `Confidence` cell re-formed to the machine form, e.g. MAR-11 `72% [ledger] -- AS-MADE 70% [2026-02-23] RE-DERIVED 2026-09-17 (ledger 72% is a WALKED value; chain 70→80→88 (7/2)→72 (8/21))`.
- `AGENTS/MARCO/STATUS.md:4` — *"6 as-made confidences re-derived at the Feb-24 blob."*
⭐ MARCO also **reported back against my tool**: *"the tool still prints 8 MISMATCH because it reads the first % in the cell"* (`SCRATCH.md:20`) and identified 5 of my flags as first-%-after-ID artifacts on July resolution lines. **That is a defect in `scripts/asmade_audit.py`, not in MARCO's ledger** — see §9.

### 8. Cross-agent / pattern
- **→ DAEDALUS (me):** `scripts/asmade_audit.py` reads the **first `%` in the cell**, so a row whose Notes begin with a July resolution line is flagged MISMATCH against its own July text. MARCO measured this at **5 of 9 flags false** on its desk. Fix the parser before the 9/14-sitting calibration numbers are used.
- **→ PROME:** MARCO `MEMORY.md` is **151% of budget** and is a boot read; it is the largest single over-budget boot surface in this cohort after REGINALD's STATUS.
- **PATTERNS candidate (ANTI):** *a floor-level leg written into a ceiling-level `Next_upgrade` cell stops reading as a defect.* MARCO's missing BOTTOM LINE is an **L1** leg presented as *"L5 on TWO form changes"*; it has now survived a correct diagnosis (9/5) plus two self-authored sessions. The cell told the truth about the work and lied about the **urgency**.

---

## AEOLUS — Market · FLEET_MAP L3 / Conf M / last_scored 2026-09-01

### 1. Period production
| Metric | Value |
|---|---|
| Commits touching `AGENTS/AEOLUS/` since 9/1 | **10** |
| Self-authored | **2** — `deb8c35bc` 9/11 · `f0d2a941c` 9/11 |
| Routed-in | **8** |
| Last self-commit | **2026-09-11** |
| Dark-days now | **6** |

**What shipped:** one session, two commits, both 9/11. `deb8c35bc` — read-cap remedy: `SCRATCH.md` 76,209 → 9,339 B, `STATUS.md` 40,446 → 32,504 B, three verbatim crc32-stamped archive blocks, **a rule-18 obligation census (17 named items in → 17 carried out, 8 closed by name with reason)**, and `OPEN_THREADS_2026-07-09.md` `git mv`'d to `archive/`. `f0d2a941c` — 11 inbox items encoded; A-33 pauses the Panama step-down; **AEO-12 re-priced 80 → 60%** on the issuer's own postponement.

### 2. Row-claim test
| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | Predictions RESOLVING — 4 of 12 graded (AEO-04/05/06/11 HIT), 8 OPEN | **TRUE-STILL** — still 4 HIT / 8 OPEN | `AGENTS/AEOLUS/workbook/PREDICTIONS.tsv` |
| 2 | Exit rail LIVE and honestly worked — `STATUS:188` *"Fired count: 0 of 6"* | **TRUE-STILL, line moved** — the text is verbatim intact at **`STATUS.md:117`** (was `:188`) after the 9/11 rotation | `AGENTS/AEOLUS/STATUS.md:117` |
| 3 | THESIS river-keyed rewrite exists | **TRUE-STILL** — `THESIS.md` 134 ln, last touched `ef8d95669` 2026-08-27 | `AGENTS/AEOLUS/THESIS.md` |
| 4 | C6 Mead 1,034.74 ft vs 1,035 binding = a pre-registered falsifier firing live | **TRUE-STILL and advanced** — STATUS head now carries `Mead 1,038.72 ft [9/10, USBR 921/49], 3.72 ft above` and AEO-10's Notes log the 9/11 tracking datum **explicitly as a datum, not evidence**, citing the row's own 8/27 retraction | `AGENTS/AEOLUS/STATUS.md:3`; PREDICTIONS AEO-10 Notes |
| 5 | Conf M because STATUS 40,446 B, byte-rule budget 33,000 B BREACHED ~23% | **REFUTED IN PART** — STATUS is now **32,504 B**, i.e. **99.86% of the 32,550 B budget: rc=0 with 46 B of headroom.** The breach is cleared; the margin is one paragraph. | `read_cap_check --agent AEOLUS`; `deb8c35bc` |
| 6 | Highest self-share in cohort (74%) | **REFUTED for this period** — 2 of 10 = **20%**, the *lowest* self-share in R5 after SHADE's 0% | `git log … -- AGENTS/AEOLUS/` |
| 7 | Next_upgrade: **"Conf M→H at the Mode-A profile fan-out (owed since 8/23)"** | **TRUE-STILL — not done, and the profile has decayed further.** See §4. | `profiles/AEOLUS.md:5` |
| 8 | L4 on consumption legs (MARCO C5, WATT C3 — WATT dark 15d) | **CANNOT-EVALUATE** — I did not open WATT's or MARCO's trees for AEOLUS consumption. Needs: a grep of `AGENTS/WATT/` and `AGENTS/MARCO/` for C3/C5 citations dated in-period. | — |

### 3. Ladder walk (Market, current L3 → next L4)
| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L1 | STATUS + BOTTOM LINE | **MET** | `AGENTS/AEOLUS/STATUS.md:170` |
| L2 | structured record, valid schema, accruing | **MET** — KB 115 rows, VX 35, FLOW, PREDICTIONS, `LEDGER_GLOB`, `SCHEMA.tsv`, 5 domain workbooks | `AGENTS/AEOLUS/workbook/`, `AGENTS/AEOLUS/*/workbook` |
| L3 | convergence matrix + exit rules | **MET** — C1–C6 channel matrix + the 6-channel exit triad with a counted fired-count | `AGENTS/AEOLUS/CLAUDE.md:103-108`; `STATUS.md:117` |
| L3 | predictions resolving | **MET — best in cohort.** Re-prices are reasoned, dated, self-adversarial and reversible: AEO-10 went 80→30→65 **in one session** and the row states *"this is the SECOND RE-PRICE IN ONE SESSION AND IT REVERSES DIRECTION. That is the system working, not thrashing"* — with the reason (the 30% was tagged PROVISIONAL precisely because the projection error was un-base-rated; the move is what happened when it was). AEO-10's Notes also carry a **published-headline retraction against itself** (*"I RETRACT A HEADLINE I PUBLISHED THIS MORNING"* across STATUS, NEXUS_BRIEF, KB-083 and four outbound packets). | PREDICTIONS AEO-10 Notes |
| L3 | dated falsification surface | **MET** — every row carries `If_Falsified` with a **routing consequence**, not just a flag (AEO-10: *"C6 → 5, route immediately to WATT (Hoover 1,274→382 MW) and CARL/MARCO"*) | PREDICTIONS col 9 |
| L4 | TRADE.md feeding proposals | **PARTIAL** — `TRADE.md` exists (10,123 B) but idea #1 is **STOOD DOWN** with both legs dead and the successor **pre-registered UNARMED**. This is the ZHAO adapted-pass shape: a declared, readable, dated no-book surface. | `AGENTS/AEOLUS/TRADE.md:5-9` |
| L4 | signals flowing | **NOT-ADJUDICATED** — row-claim 8; no in-period AEOLUS→peer packet appears in the commit subjects | — |

**Recommendation: HOLD L3, Conf M (do NOT lift to H).** The M→H gate is explicitly the Mode-A profile fan-out and it is **not met** — worse, the profile has decayed measurably since the gate was written (§4). The substance would support H; the gate is about *my* comprehension of the desk, not the desk's quality, and I have not done the work.

### 4. Profile trigger — ⚠️ **THE ANSWER TO THE LEAD'S QUESTION: NO, THE PROFILE NO LONGER DESCRIBES THE DESK**
> `profiles/AEOLUS.md:3` — **"⚠️ STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01) … full Mode-A fan-out owed since 8/23. Refresh checkpoint: 2026-09-15."**
> `profiles/AEOLUS.md:6` — the 5-leg file-readable trigger: **(P)** AEO-12 leaves OPEN *or* open-count moves off 8 · **(S)** `ls -d AGENTS/AEOLUS/*/workbook | wc -l` moves off 5 · **(T)** KB rows move off 82 by ≥15 · **(F)** exit-triad fired-count moves off 1 of 6 · **(floor)** next Production Review.

| Leg | Measured today | Verdict |
|---|---|---|
| (P) AEO-12 / open-count | AEO-12 **OPEN**; open-count **8** | **NOT FIRED** |
| (S) domain workspaces | `ls -d AGENTS/AEOLUS/*/workbook \| wc -l` = **5** | **NOT FIRED** — and the profile itself already flags this leg as blind to channel-depth growth |
| (T) KB rows | **115 data rows** vs baseline 82 = **+33**, threshold ≥15 | 🔴 **FIRED** |
| (F) fired-count | `STATUS.md:117` **0 of 6** vs baseline 1 of 6 | 🔴 **FIRED** |
| (floor) | this review | 🔴 **FIRED** |

**Verdict: FIRED on three of five legs, and the 2026-09-15 refresh checkpoint is BREACHED by 2 days.**

**Profile statements now FALSE (each verified in AEOLUS's tree):**
| Profile text | Live state | Locator |
|---|---|---|
| §1 *"`OPEN_THREADS_2026-07-09.md` (**dead-unfolded 39d** — the one open QC-docket item)"* | **File no longer exists at root** — `git mv`'d to `archive/` on 9/11 as a CALENDAR-scheduled retirement | `deb8c35bc` commit body |
| §1 *"`scripts/domain_log_check.py` (⚠️ invoked BARE at `CLAUDE.md:57`, **dead from launch cwd, watched-fail**; packeted 8/17)"* | **FIXED 2026-08-21** and the fix is documented in-file with the failure analysis: *"PATH FIXED 2026-08-21 (DAEDALUS PR#4 ACTION 1, verified by running both forms)"*; the invocation is now `python3 "$(git rev-parse --show-toplevel)/AGENTS/AEOLUS/scripts/domain_log_check.py"` | `AGENTS/AEOLUS/CLAUDE.md:57-62` |
| §1 *"`TRADE.md` … ⚠️ 8/12 banner sits above a `Status: LIVE, refreshed 2026-07-09` line — **two-clock ambiguity**"* | **RESOLVED 2026-08-21.** Line now reads *"Status: LIVE — file refreshed 2026-08-21. GRADE EVERY ROW ON ITS OWN `Last Updated` CELL, NOT ON THIS LINE"*, with the reasoning kept beneath it | `AGENTS/AEOLUS/TRADE.md:13-14` |
| §1 *"`workbook/` (**KB 71** … VX 25 … PREDICTIONS AEO-01..11)"* | KB **115**, VX **35**, PREDICTIONS **AEO-01..12** | `AGENTS/AEOLUS/workbook/` |
| §1 *"`STATUS.md` (165 ln/33.7 KB, vintage 8/13 — 105% of the default byte budget)"* | **176 ln / 32,504 B, vintage 9/11, rc=0** | `read_cap_check --agent AEOLUS` |
| §1 *"`CLAUDE.md` (328 ln/34.1 KB … **LAYER CONTRACT :262-279** … **DOMAIN WORKSPACES :304-321**)"* | 340 ln / 41,360 B; LAYER CONTRACT is at **:274**, SHARED-INPUT RULE **:293**, SUB-AGENT SPAWNING **:307**, DOMAIN WORKSPACES **:316**. The cited **:103-105** "C6 discriminator" resolves to the **C2/C3/C4** table rows. | `grep -n "LAYER CONTRACT\|DOMAIN WORKSPACES" AGENTS/AEOLUS/CLAUDE.md` |

**Six statements, six wrong** — and note the shape: **four of the six are false because the defect was FIXED.** The profile is not describing a decayed desk; it is a stale snapshot of a desk that has since serviced most of what the snapshot complained about. A section-task reading this profile today would re-report three closed defects as open. **That is the failure mode the profile layer exists to prevent, and it is mine.**

### 5. Falsification read — AEOLUS (thesis but no separate scanner-visible surface)
**Where the rail actually lives — RAIL-IN-LOCAL-FORM, three layers, all live and dated:**
1. **`AGENTS/AEOLUS/STATUS.md:117`** — the six-channel **exit triad with a counted fired-count**: *"Fired count: 0 of 6. (Was 1 of 6 on 8/21. C5's exit is the same test failing, and it fails on all three days — so the channel is out, not merely stepped down.)"* A counted, dated, direction-explained rail.
2. **`AGENTS/AEOLUS/workbook/PREDICTIONS.tsv` col 9 `If_Falsified`** — populated on every row with a **routing consequence**, not a shrug.
3. **`AGENTS/AEOLUS/THESIS.md`** — per-channel `stage → mechanism → state` transmission tables, river-keyed since the 8/21 rewrite; last touched **2026-08-27** (`ef8d95669`).

**EVIDENCED fire path: YES, three separate resolved falsifications in the record.**
- **AEO-10, 2026-08-27:** *"THE PRE-REGISTERED FALSIFIER FIRED, IN THIS ROW'S OWN WORDS"* — the row's own text (*"Falsifier: … or Mead tracking below USBR's monthly projection path"*) was applied against the desk, 80% → 30%.
- **AEO-12, 2026-08-21:** the registration carried an obligation (*"re-price when the 2023-24 draft trough is verified at primary. If that trough turns out to be SHALLOWER than 47.0 ft, this confidence is too high"*); the obligation was **executed the same day**, the trough came back **deeper** (44.0 ft, primary-verified), and the rule ran the other way — 65 → 80%.
- **AEO-12, 2026-09-11:** re-priced **80 → 60%** on A-33-2026's postponement, i.e. the rail moved *against* the desk's own position on the issuer's word.

**Verdict: RAIL-IN-LOCAL-FORM (`STATUS.md:117` + PREDICTIONS `If_Falsified` + `THESIS.md`), live, dated, and with three evidenced fires — two of them against the desk's own call.**
**Severity: none on the rail.** The one live gap is the **THESIS.md vintage**: last touched 8/27, so the per-channel state tables are **21 days behind** a STATUS that moved on 9/11 (AEO-12 re-price, A-33 Panama pause). That is a two-clock exposure, not a rail failure.

### 6. Negative-resolution leg
**Ledger opened:** `AGENTS/AEOLUS/workbook/PREDICTIONS.tsv` (12 rows, `Status` col 10, `Resolution_Criteria` col 8). **8 OPEN.**

| Row | Negative class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **AEO-10** *"Lake Mead does **NOT** fall to or below 1,035 ft at any point through 2026-12-31"* | ✅ **pure non-event** | ✅ **exact**: *"USBR daily pool elevation (reservoir 921, datatype 49): minimum daily value 2026-08-13 through 2026-12-31 stays above 1,035.00 ft"* | ✅ the window is the precondition, and the series is daily |
| **AEO-09** *"NIFC above-normal potential for TX/OK is **REMOVED**"* | ✅ **absence in a named publication** | ✅ *"NIFC National Significant Wildland Fire Potential Outlook (monthly, issued ~1st) … TX and OK no longer shaded above-normal for the then-current month in any issuance from 2026-10-01 through 2026-12-01"* | ✅ named issuances, and **disambiguated 2026-08-21 BEFORE the 9/1 outlook landed** — pre-committed, not retunable to a result |
| **AEO-03** *"Property-cat reinsurance **stays soft** at Jan 1 2027 (ROL flat-to-down YoY)"* | ✅ persistence-negative | ⛔ **NOT NAMED** — criterion is only *"Jan'27 property-cat ROL ≤ +5% YoY"*. **No publisher, no index, no series.** Whose ROL? (Guy Carpenter RoL index? a broker renewal report? Howden?) | ⛔ none |
| **AEO-12** (falsify leg) *"draft never reaches 47.0 in the window"* | ✅ the MISS is a non-event | ✅ **exemplary**: *"maximum authorized draft for the Neopanamax Locks, TFW, as stated in a numbered ACP Advisory to Shipping … Discover the PDF by search then fetch; **NEVER the advisories index (JS-rendered, silently stale)**"* | ✅ 2027-01-01 → 2027-04-30 |

**Counts: candidates opened 8 · confirmed negative-class 4 · lacking instrument 1 (AEO-03).**
⭐ AEOLUS is the **strongest desk in the cohort on this canon**, by a distance. AEO-12's criterion does not merely name the instrument — it names the *wrong* instrument and forbids it, which is the only form of this rule that survives a tired reader. AEO-04's resolution note is the reason why: *"MY REGISTERED BAND MEASURES THE VARIABLE ACP IS DELIBERATELY HOLDING CONSTANT"* — a 51-day miss caused by an instrument structurally blind to the event, diagnosed at the instrument rather than at the attention.
⛔ **AEO-03 is the one hole and it is a real one:** a soft-market persistence call is exactly the kind that resolves by *nothing happening*, and with no named publisher it can only be graded by whatever source is to hand at renewal.

### 7. As-made receipt — **n/a**.

### 8. Cross-agent / pattern
- **→ AEOLUS:** (a) AEO-03 needs a named ROL publisher before Jan-1-2027 — 105 days. (b) `THESIS.md` is 21 days behind STATUS. (c) STATUS sits at **46 B under budget**; the next append breaches.
- **→ DAEDALUS (me):** the AEOLUS profile is the most decayed artifact I found in this cohort. The Mode-A fan-out is **25 days overdue** against a checkpoint that has now passed.
- **PATTERNS candidate (ANTI):** *a stale profile's most misleading rows are the ones describing defects that have since been FIXED.* Four of six false AEOLUS profile statements are false **because the desk repaired them** — so the profile's error is not "out of date", it is "actively re-opens closed work". A decay clock keyed on the SUBJECT's activity (as AEOLUS's is) still cannot distinguish decay-by-rot from decay-by-repair, and only the second kind actively costs the fleet work.
- **PATTERNS candidate (PATTERN):** *quote the closeout metric on the instrument's own denominator.* `deb8c35bc`'s **subject** reads *"STATUS 75%→60%"* (% of the 54,250 B **cap**) while the fleet instrument grades **% of budget**, where the same file is **100%**. The commit **body is correct** — it names `budget 32,550` and `rc 1 -> rc 0` — so this is a subject-line basis mismatch, not bad work. But a reader of the log alone reads "60%, comfortable" where the tool reads "rotate-tier, 46 B of headroom." `finding_distance_to_a_threshold_is_a_claim_about_its_basis`, one layer up: the *compliance report* inherits the basis too.

### 9. Reviewer-side defects
1. **`profiles/AEOLUS.md` — six false statements, four of them stale-because-fixed** (§4). Mine.
2. **FLEET_MAP AEOLUS `Gaps`: "byte rule v2 budget 33,000 B BREACHED ~23%" and "Highest self-share in cohort (74%)" are both now wrong** — the first cleared 9/11, the second inverted (20%, second-lowest). Both are the accreted-story problem the FLEET_MAP `Gaps` standing rule names: *a cell states what is TRUE NOW.*
3. **The `33,000 B` figure itself is not the canon number** — `READ_CAP.md` / `read_cap_check.py` use **32,550 B**. A row-local constant 450 B off the canonical one is how a desk gets graded against a budget nobody else uses.

---

## HOMER — Market · FLEET_MAP L2 / Conf H / last_scored 2026-09-01

### 1. Period production
| Metric | Value |
|---|---|
| Commits touching `AGENTS/HOMER/` since 9/1 | **18** |
| Self-authored | **7** — `a18bcdd99` 9/2 · `3a50de647` 9/2 · `7895e1915` 9/11 · `a8dd231e7` 9/11 · `423ba1cf4` 9/14 · `448784a9e` 9/14 · `de4cbc23f` 9/14 |
| Routed-in | **11** |
| Last self-commit | **2026-09-14** |
| Dark-days now | **3** |

**What shipped:** the highest self-authored volume in R5 after REGINALD. `a18bcdd99` — DOCKET L224 executed 2 days early + **P1 read-cap remediation on both boot reads**. `3a50de647` — Amendment 12 fold + the **MF maturity-wall retirement published to consumers**. `423ba1cf4` — *"three weeks of prints, and the GSE/CMBS divergence turned out to be running backwards"*, i.e. a self-inverted read. `de4cbc23f` — *"two FL metro rows the closeout nudge caught before the next STATUS rewrite ate them"* (the ledger nudge paying out).

### 2. Row-claim test
| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | **Both L3 legs UNBUILT** — `thesis/` holds `PREDICTIONS.tsv` ALONE; no `THESIS.md`, no thesis-level kill rail under any name | **TRUE-STILL, third consecutive review.** `ls AGENTS/HOMER/thesis/` returns exactly `PREDICTIONS.tsv` (35,975 B). HOMER states it itself: *"**A5** L3 BUILDS 3b+3c (`thesis/THESIS.md` + kill rail, convergence handle), **authorized to BUILD** … **ALL OPEN.** ⚠️ **22 days deferred**"* | `AGENTS/HOMER/thesis/`; `AGENTS/HOMER/STATUS.md:101` |
| 2 | 0 hits for convergence matrix/handle in STATUS | **TRUE-STILL** — the dashboard is 7 domain sections (`STATUS.md:19-90`) with **no cross-domain convergence handle** | `AGENTS/HOMER/STATUS.md` §SIGNAL DASHBOARD |
| 3 | `Resolve_By` column present | **TRUE-STILL** — col 11 of `thesis/PREDICTIONS.tsv` | `AGENTS/HOMER/thesis/PREDICTIONS.tsv:2` |
| 4 | STATUS 211 lines **but ~148 KB — the byte tier is the real cap** | ⛔ **REFUTED — FIXED.** STATUS is **163 ln / 22,773 B = 70% of budget, rc=0**; the cold half lives at `STATUS_COLD.md` (150,761 B). The hot/cold split is done and clean. | `read_cap_check --agent HOMER` |
| 5 | Next_upgrade *"Byte tier: rotate STATUS <32,550 B"* | ⛔ **REFUTED — DONE** (row-claim 4). **This is now the single most misleading cell on HOMER's row: it asks for work that is finished.** | ibid. |
| 6 | Blueprint conformance still NOT GRADED | **TRUE-STILL** — no conformance record found in `upgrades/HOMER_CARD.md` or the 8/22 review | `AGENTS/DAEDALUS/upgrades/HOMER_CARD.md` |
| 7 | PATH FIX: the card is `AGENTS/DAEDALUS/upgrades/HOMER_CARD.md` | **TRUE-STILL** — file exists at the corrected path | `ls AGENTS/DAEDALUS/upgrades/HOMER_CARD.md` |
| 8 | Profile has the fleet's only explicit DATED REWRITE TRIGGER (`:14`) and it FIRED (25d) — queued 8/23, not done | **TRUE-STILL and worse** — now **41 days** past the build date and the profile's own 9/05 deadline plus the PR#5 9/15 checkpoint are both breached. See §4. | `profiles/HOMER.md:14` |
| 9 | *"Lesson: reactive excellence substituting for generative structure"* | **TRUE-STILL, and this period is the cleanest instance yet.** 7 self-commits of high-grade reactive work — an inverted divergence caught, a retired maturity wall published, a caveat receipted — and **zero** progress on the two authoring acts that are the actual gate. | `423ba1cf4`, `3a50de647`, `7895e1915` vs `STATUS.md:101` |

### 3. Ladder walk (Market, current L2 → next L3) — walked leg by leg per the task
| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L0 | dir + CLAUDE.md | **MET** — `CLAUDE.md` 50,813 B | — |
| L1 | STATUS + labeled BOTTOM LINE | **MET** | `AGENTS/HOMER/STATUS.md:149` |
| L2 | structured record, valid schema, accruing | **MET** — 9 workbook TSVs incl. `SCHEMA.tsv`, `board_log.tsv` 55,904 B, `registry/corrections_receipts.tsv` | `AGENTS/HOMER/workbook/`, `AGENTS/HOMER/registry/` |
| **L3** | **convergence matrix + handle** | ⛔ **NOT MET** — row-claim 2; self-declared open at `STATUS.md:101` (A5) | `AGENTS/HOMER/STATUS.md:101` |
| **L3** | **exit rules** | ⚠️ **PARTIAL** — exit/kill logic exists **per prediction** (early-kill arms, `Invalidation` col 9) and per band, but there is **no thesis-level exit rule**. HOMER's own `STATUS.md:145` states the discipline: *"`Date_Resolved`/`Outcome` stay EMPTY while arms have fired but the call is unresolved — one arm of a two-arm kill is not a resolution."* | `thesis/PREDICTIONS.tsv`; `STATUS.md:142,145` |
| **L3** | **predictions resolving** | **MET** — HOM-01 **CLOSED MISSED (EARLY-KILL) 2026-08-31**, IF-MISSED action executed (Realtor.com list-price loses standing as a 60-90d lead), and **corroborated 9/14 by Case-Shiller with the corroboration explicitly labelled *"of a closed call, NOT a re-opening"*** | `AGENTS/HOMER/STATUS.md:141` |
| **L3** | **dated falsification surface** | ⛔ **NOT MET** — the rail is real but lives per-prediction, not at thesis level (§5). This is leg 3b. | §5 below |

**Recommendation: HOLD L2, Conf H.** Two of five L3 legs NOT MET and a third PARTIAL; the two blockers are **authoring acts, not extract-and-stamp**, Will-authorized since 8/23, and 22 days deferred by HOMER's own count. Confidence H: I opened `thesis/`, STATUS and the predictions ledger myself.
⚠️ **But say the other half on the row too:** HOMER is doing **L4-grade domain work at an L2 grade**. The instrument discipline in `STATUS.md:108` (§5 below) is better than anything at L3 in this cohort. The grade is correct and it is also, read alone, misleading about the desk.

### 4. Profile trigger
> `profiles/HOMER.md:14` — **"DATED REWRITE TRIGGER — a banner is a warning, not a fix (`finding_banner_is_a_warning_not_a_fix`): full delta-refresh owed by 2026-09-05, or at the next HOMER touch, whichever is first."**
> `profiles/HOMER.md:3` (PR#5 banner) — **"Refresh checkpoint: 2026-09-15."**
> Profile body — **"Staleness (content-derived): re-read … when STATUS's stamp leads this build date >21d."**

**FIRED — on all three legs, independently:**
| Leg | Measurement | Verdict |
|---|---|---|
| dated deadline 2026-09-05 | today is 9/17 | 🔴 **FIRED +12d** |
| *"or at the next HOMER touch, whichever is first"* | HOMER touched **9/2, 9/11, 9/14** — three touches after the deadline | 🔴 **FIRED ×3** |
| STATUS stamp leads build date >21d | build 2026-08-07, STATUS 2026-09-14 = **38d** | 🔴 **FIRED** |
| PR#5 checkpoint 2026-09-15 | today 9/17 | 🔴 **BREACHED +2d** |

**Profile statements now false:**
- `profiles/HOMER.md` §Staleness: *"built against **61 files** (the tree is now 89)"* — the tree is now **larger again** (`STATUS_COLD.md`, `LESSONS_COLD.md`, `LESSONS_COLD_2.md`, `OBLIGATIONS_OTHERS.md`, `registry/` all post-date the build).
- The byte-tier concern carried in the FLEET_MAP row is **closed** (row-claim 4/5).
- **Still true and re-verified today:** the two L3-blocking absences, and every DO-NOT-TOUCH item.

### 5. Falsification read — HOMER (market desk with no thesis-class file the scanner can see)
**Where the rail actually lives — RAIL-IN-LOCAL-FORM, and the local form is unusually good:**
1. **`AGENTS/HOMER/thesis/PREDICTIONS.tsv`** — `Invalidation` (col 9) + `Resolve_By` (col 11) + **early-kill arms** per row.
2. **`AGENTS/HOMER/STATUS.md:136-146` §PREDICTIONS** — the live grade surface, carrying the two-arm rule at `:145`.
3. **`AGENTS/HOMER/STATUS.md:48`** — retirement-with-a-guard: *"⛔ **2026 MF maturity wall** — RETIRED 9/2 — `$160B+` and `$270B+` BOTH DEAD … ⛔ **kill-on-sight: *"the $160B MF wall is Trepp's"***" — a retired figure with a standing do-not-cite rule attached.
4. ⭐ **`AGENTS/HOMER/STATUS.md:108` §C — "Instruments that GRADE NOTHING — do not read their silence as calm."** Five entries, each with a dated search attempt and a disposition: *"Trepp AUGUST MF special servicing — **SEARCH-NOT-FOUND 2026-09-14** (trepp.com unreachable from this box; multihousingnews 403; **searches return August 2025 figures that look current**)"* · *"ICE Mortgage Monitor (Sept, pub 9/11) — **published and UNREAD. Not a data gap; a *me* gap**"* · *"Google Trends — RETIRED at CARL 9/1; endpoint 429, **4th confirmation 2026-09-14** … ★ **the hard data SPLITS and search sits on the IMPROVING half** — do not carry as corroborated."*

**EVIDENCED fire path: YES.** **HOM-01 resolved MISSED via EARLY-KILL on 2026-08-31**, the IF-MISSED consequence executed, the call marked **DO NOT RE-OPEN**, and a later confirming print (Case-Shiller, 9/14) correctly logged as corroboration of a **closed** call rather than a reason to reopen. That is a complete falsification cycle through the local rail.

**Verdict: RAIL-IN-LOCAL-FORM** — `thesis/PREDICTIONS.tsv` (`Invalidation`/`Resolve_By`/early-kill arms) + `STATUS.md:136-146` + `STATUS.md:108` §C — **live, dated, and with one resolved falsification through it.**
**Severity of the gap: MEDIUM and precisely bounded.** The rail is **per-prediction**, so it can kill a *call* but has no instrument that can kill the *thesis*. With exactly **two** predictions on the book (HOM-01 closed, HOM-02 open), the entire falsification surface of a desk covering foreclosures, GSE/CMBS multifamily, rates, builders, pricing and state housing rests on **one open row**. That, not the missing file, is the real argument for leg 3b.

### 6. Negative-resolution leg
**Ledger opened:** `AGENTS/HOMER/thesis/PREDICTIONS.tsv` (2 data rows, `Status` col 6). **1 OPEN: HOM-02.**

| Row | Negative class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **HOM-02** *"MBA NDS FHA total DQ (SA) crosses 12.00% in the Q2, Q3 **OR** Q4-2026 release"* — the MISS resolves as **"no release crosses by Q4"** | ✅ MISS is a non-event | ✅ **MBA National Delinquency Survey**, named, with the exact SA series and the 12.00% band | ✅ **three dated release windows**, and the Q2 leg is already graded (*"11.79%, 21bps short"*) with the Q3 print named as *"the modal decider"* (~mid-Nov) |

**Counts: candidates opened 1 · confirmed negative-class 1 · lacking instrument 0.**
⭐ Beyond the ledger, **§C `STATUS.md:108` is the fleet-reference implementation of this canon** — it is a standing register of *searches that failed, with the date of the attempt and what the failure does and does not license*. `SEARCH-NOT-FOUND 2026-09-14` on the Trepp row is exactly the dated search-attempt precondition the canon asks for, and the note that *"searches return August 2025 figures that look current"* is the failure mode (`finding_plausible_stale_value_evades_review`) caught at the instrument.

### 7. As-made receipt — **n/a** (HOMER not in the packet set).

### 8. Cross-agent / pattern
- **→ PROME:** `AGENTS/HOMER/OBLIGATIONS_OTHERS.md` B7 — *"PROME's CalculatedRisk 'dead source' census is WRONG"*, live, ~12 desks asked to re-annotate on it (`f1a2b36c0`). HOMER flagged it and correctly did not edit. **Unresolved at 9/14.**
- **→ HOMER:** `LESSONS.md` is **23,748 B = 73% of budget**, inside the 70–75% ambiguity band; if it was just rotated it owes 964 B more, if never breached it owes nothing. Only HOMER knows which.
- **PATTERNS candidate (PATTERN):** *a "grades nothing" register is the missing half of a signal dashboard.* HOMER's §C converts silence into a **dated, attributed non-reading** — separating *unpublished* from *unreachable* from *"a me gap"*. Recommend promoting the form to the market-agent blueprint. Evidence: `AGENTS/HOMER/STATUS.md:108-114`, 5 entries, 4 carrying a dated search attempt.

### 9. Reviewer-side defects
1. ⛔ **FLEET_MAP HOMER `Next_upgrade` asks for finished work.** *"Byte tier: rotate STATUS <32,550 B"* — done; STATUS is 22,773 B at 70%. HOMER remediated on **9/2** (`a18bcdd99`, *"P1 READ-CAP remediation DONE on both boot reads"*) and my row has carried the ask for 15 days. A `Next_upgrade` that names completed work teaches the desk the cell is not read.
2. ⛔ **The `Gaps` cell's "STATUS 211 lines … but ~148 KB"** is a superseded measurement presented in the present tense.
3. ⚠️ **`profiles/HOMER.md:14` is the strongest self-indictment in my tree** — it cites `finding_banner_is_a_warning_not_a_fix` **in the banner that is not a fix**, sets a hard deadline (9/05), adds *"or at the next HOMER touch, whichever is first"*, and has now been overrun by the deadline **and** three touches **and** a second checkpoint. The trigger design is correct; nothing consumes it.

---

## SHADE — Market · FLEET_MAP L3 / Conf H / last_scored 2026-09-01

### 1. Period production
| Metric | Value |
|---|---|
| Commits touching `AGENTS/SHADE/` since 9/1 | **11** |
| Self-authored | ⛔ **0** |
| Routed-in | **11** (all WALTER lane) |
| Last self-commit (any date) | **2026-08-28** (`e0177eefc`) |
| Dark-days now | ⛔ **20** |

**What shipped from SHADE: nothing.** Every in-period commit is WALTER routing into SHADE's inbox. The desk has not run since the 8/28 PROME-orchestrated closeout.

### 2. Row-claim test
| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | Leg (a) 3 cheap handles = 1.5 of 3 | **TRUE-STILL** — no session since | — |
| 2 | STATUS compressed 498→150 ln / 32,462 B via crc32 archive form — *"the fleet's cleanest byte-cap answer, cite as exemplar"* | **TRUE-STILL on the form; ⚠️ NOT on the number.** 150 ln / **32,462 B = 100% of budget, 88 B of headroom, rotate-tier.** The archive craft is exemplary; the **stopping point is not** — it stopped at the trigger, not below the 70% stop. Citing it as the exemplar without that qualifier propagates the half-rotation. | `read_cap_check --agent SHADE`; `archive/STATUS_PRE-ROTATION_2026-08-28.md` |
| 3 | FIRED-triad now a COUNTED standing form (`STATUS:43` T-SHADE-01 4-for-4) | **TRUE-STILL, line moved** — the counted form is at **`STATUS.md:43`**: *"HY OAS 263 [FRED, 8/27 print] = ties the 2026 LOW ⇒ `T-SHADE-01` NOT ARMED, ZERO legs — and BOTH now freshly measured. Level leg 17bp below the bar (vs 9bp on 8/13 — further away)."* | `AGENTS/SHADE/STATUS.md:43` |
| 4 | **`PREDICTIONS.tsv` STILL ABSENT and self-flagged** | **TRUE-STILL.** `find AGENTS/SHADE -iname "*PREDICT*"` = **no match**; the only `.tsv` files are `board_log.tsv` and `registry/corrections_receipts.tsv`. Self-flag verbatim intact: *"🔴 **DAEDALUS L4-path item, still untouched: seed `PREDICTIONS.tsv` with confidences AT REGISTRATION.** Dated binaries exist without a scoring surface; every session adds more."* | `AGENTS/SHADE/STATUS.md:130` (§10 item 4) |
| 5 | Trigger registered with `value_basis` + directional sign leg | **TRUE-STILL** — `CLAUDE.md` §REGISTERED TRIGGERS, T-SHADE-01 table, registered 2026-08-28 | `AGENTS/SHADE/CLAUDE.md:~68+` |
| 6 | CCC channel reconciled one-owner-each with BROCK (§7) | **TRUE-STILL — CLOSED 8/28**, with SHADE's figures completing BROCK's own discriminator | `AGENTS/SHADE/STATUS.md:135` (§10 item 9) |
| 7 | Profile **NOT FIRED (floor 9/15)** but **MIS-SPECIFIED** | ⛔ **REFUTED — the floor has now FIRED** (9/15 passed; today 9/17). The mis-specification claim is **TRUE-STILL and confirmed** (§4). | `profiles/SHADE.md` Δ 2026-08-11 block |
| 8 | Next_upgrade: *"L4 on `PREDICTIONS.tsv` seeded with confidences AT REGISTRATION (one file) — everything else for L4 is on disk"* | **TRUE-STILL** — one file, still absent, 20 days dark | — |

### 3. Ladder walk (Market, current L3 → next L4)
| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L1 | STATUS + BOTTOM LINE | **MET** | `AGENTS/SHADE/STATUS.md:146` |
| L2 | structured record, valid schema, accruing | **MET** — `board_log.tsv` 159,872 B, `MAINTENANCE.md` structural log, `registry/corrections_receipts.tsv` | — |
| L3 | convergence matrix + exit rules | **MET** — §3 per-vector dashboard + §4 five-stage transmission map + `CLAUDE.md:48` 4 independent kill paths + the threshold band table | `AGENTS/SHADE/CLAUDE.md:48-60` |
| L3 | predictions resolving | ⚠️ **PARTIAL** — calls **do** resolve (M-11 dual-test graded to a full NO-VERDICT day 8/4; ARCC 0-of-4; T-SHADE-01 4-for-4) but they resolve **on grade cards at the agent root and in STATUS prose, with no ledger**. Row-claim 4. | `2026-08-04_athene-q2-m11-grade-card.md` (34,483 B, at root) |
| L3 | dated falsification surface | **MET** — §5 below | — |
| L4 | **TRADE.md feeding proposals** | **NOT MET** — no `TRADE.md`; no declared-flat surface either | `ls AGENTS/SHADE/` |
| L4 | signals flowing | **MET (historically)** — SHADE-canonical insurer-exposure figures consumed by BROCK/LIQUID/REGINALD/NEXUS; the 8/28 CCC reconcile completed BROCK's discriminator. **Zero flow in-period** (0 self-commits). | `AGENTS/SHADE/STATUS.md:135` |

**Recommendation: HOLD L3, Conf H.** The L4 gate is one file and it has not moved in 20 dark days. Note that my row's `Next_upgrade` says *"everything else for L4 is on disk"* — that is **wrong**: there is also **no TRADE surface**, the same leg CORAL is held on. See §9.
**Dormancy:** 20 days dark with 11 routed-in WALTER items. Not yet a ROSTER question, but it is the longest dark run in R5 and the desk's live rail has moved materially against it (§8).

### 4. Profile trigger
> `profiles/SHADE.md` Δ 2026-08-11 — **"RE-STAMP: refresh when a PREDICTIONS/grade-card LEDGER file appears (the standing trigger — grade cards at root ≠ a ledger), or at the L4 assessment, or hard floor 2026-09-15."**
> Profile body — **"Staleness: refresh when §3 dashboard gains a 5-pt handle or a PREDICTIONS ledger appears, or > 45 days."**

| Leg | Measurement | Verdict |
|---|---|---|
| PREDICTIONS/grade-card **ledger** appears | still absent | **NOT FIRED** |
| L4 assessment | not run | **NOT FIRED** |
| **hard floor 2026-09-15** | today 9/17 | 🔴 **FIRED +2d** |
| >45 days from body vintage 2026-06-28 | 81 days | 🔴 **FIRED** |

**Verdict: FIRED (floor + 45d).** The FLEET_MAP prediction *"Profile NOT FIRED (floor 9/15)"* is now **REFUTED by two days**.

**And the MIS-SPECIFICATION is confirmed at the artifact — the profile's §2 file anatomy no longer describes the file:**
| Profile §2 says | Live | Locator |
|---|---|---|
| *"STATUS.md (**237 ln**, <cap) — §0/§0a … §2 evidence … §5 entity watchlist … §8 questions, §9 retired rails"* | **150 ln**, and the section scheme is different: `§0` WHERE EVERYTHING IS · `§0l` LIVE RAILS · `§1` Top-line · `§3` Signal dashboard · `§4` transmission map · `§6` calendar · `§7` cross-agent · `§10` next actions. **There is no §2, §5, §8 or §9.** | `grep -n "^## " AGENTS/SHADE/STATUS.md` |

So the profile's map of SHADE's canonical output points at **four sections that do not exist** and misses the two that carry the live rails (`§0l`, `§10`). The FLEET_MAP note *"STATUS structure rewritten 8/28 and nothing watches that — re-key at refresh"* was **right** and the refresh has not happened.

### 5. Falsification read — SHADE (market desk with no thesis-class file the scanner can see)
**Where the rail actually lives — RAIL-IN-LOCAL-FORM, in the CHARTER not a thesis file:**
1. ⭐ **`AGENTS/SHADE/CLAUDE.md:48` — "## Kill Paths (4 Independent)":** (1) FABN rollover failure — *currently YELLOW per the 6/22 ladder*, mechanism intact, wall sized ~$13–18B bottom-up via the NPORT-P crawl; (2) AG 55 forced disclosure; (3) Egan Jones indictment → NRSRO revoked; (4) war/macro transmission. **Four independent paths, each with a stated mechanism** — the structural equivalent of a thesis kill tree, living in the agent's instructions.
2. **`CLAUDE.md` §Thresholds & Triggers** — a 6-row Green/Yellow/Red band table (Athene FABN spreads, HY OAS, Egan Jones DOJ status, AG 55 filings, NAIC SVO overrides, APO stock).
3. ⭐ **`CLAUDE.md` §REGISTERED TRIGGERS → `T-SHADE-01` (registered 2026-08-28)** with instrument, `value_basis`, a **directional (not relative) sign leg**, a window-sensitivity guard and an explicit do-not-confuse against the separate HY OAS environment band. The registration note is itself a finding: *"The wrapper-decoupling trigger has been graded, cited and reported across STATUS, SCRATCH, NEXUS_BRIEF, LAST_COMPLETION and MAINTENANCE since 2026-07-09 — and had **no locus in this charter**. Its 7/9 registration was never located."*
4. **`AGENTS/SHADE/STATUS.md:43`** — the counted live reading of that trigger.

**EVIDENCED fire path: YES — and unusually, the evidence is of the rail *declining* to fire.** T-SHADE-01 has been graded **4-for-4 NOT ARMED**, each time with both legs freshly measured and the distance-to-bar stated with its direction (*"17bp below the bar (vs 9bp on 8/13 — further away)"*). The 8/4 M-11 dual-test grade card was frozen pre-print and **executed as a full NO-VERDICT day, both legs deferred-not-orphaned**. ARCC graded **0-of-4**. A rail that repeatedly declines to fire *and says by how much* is better evidence than one that has fired once.

**Verdict: RAIL-IN-LOCAL-FORM** (`CLAUDE.md:48` Kill Paths + §Thresholds & Triggers + §REGISTERED TRIGGERS `T-SHADE-01` + `STATUS.md:43`), **live, registered and dated 2026-08-28.**
⛔ **Severity: HIGH, and not for the reason the scanner would find.** The rail is well-built; its **readings are 20 days stale and the market has moved through most of the gap.** SHADE's last recorded level is *"HY OAS **263** [FRED, 8/27] … **17bp below the bar** … further away than on 8/13."* Pulled live this session: **HY OAS 276 bps [FRED BAMLH0A0HYM2, 2026-09-15]** (2.71 on 9/14, 2.65 on 9/11, 2.70 on 9/10). **The T-SHADE-01 level-leg bar is >280.** The gap has gone **17bp → 4bp** while the desk has been dark, and the trigger needs *sustained 5+ sessions* above 280, so the arming clock could start without SHADE present. **The sign leg (wrapper basket leading managers down) I could not evaluate** — that needs the basket pulled. **This is the cohort's single most actionable finding.**
⚠️ Second-order: `CLAUDE.md:48` kill-path #1 is stated *"per the 6/22 ladder"* — **87 days old**, and kill-path #4 (war/macro → oil spike) sits against REGINALD's 9/14 read of **Brent $104.61 with the cycle high $107.63**, which is the exact input that path names. Nobody has graded kill-path #4 against it.

### 6. Negative-resolution leg
**NOT-SEEN.** What I looked for and did not find: `AGENTS/SHADE/**/PREDICTIONS*`, any `.tsv` with a status column other than `board_log.tsv` (a routing log) and `registry/corrections_receipts.tsv` (a receipts log), and a `workbook/` directory (**none exists**). The scored calls are in **prose and grade cards**: `2026-08-04_athene-q2-m11-grade-card.md` (34,483 B, at the agent root), `STATUS.md` §3 and §10.

**Counts: candidates opened NOT-SEEN · confirmed negative-class NOT-SEEN · lacking instrument NOT-SEEN.**
⭐ **But the discipline this canon protects is present without the ledger**, which is worth recording as the honest reading: `STATUS.md:128` (§10 item 0b) carries *"W1 leg (b) — read AARe Note 14 vs the §2.8 private-notice claim. **Expected result PRE-STATED: no allocation disclosure.** Due **2026-09-30**."* — **a pre-stated negative expectation, with a named instrument (AARe Note 14) and a dated due date, registered before the read.** That is exactly the form, in the wrong container. The L4 file would make it countable.

### 7. As-made receipt — **n/a** (SHADE not in the packet set).

### 8. Cross-agent / pattern
- 🔴 **→ SHADE / PROME (highest priority in this cohort):** T-SHADE-01's level leg is **4bp from its bar** on FRED 9/15 (276 vs >280) against a desk-held reading of 263 [8/27] annotated *"further away."* 20 dark days. The trigger requires 5 sustained sessions, so the window can open unobserved. **Recommend a doorbell.**
- **→ SHADE:** kill-path #4 (war/macro → oil spike → portfolio stress) has a live input it has never been graded against: REGINALD's Brent **$104.61 [9/11]**, cycle high **$107.63 [9/10]** (`AGENTS/REGINALD/STATUS.md:2`).
- **→ DAEDALUS (me):** stop citing SHADE's 8/28 rotation as the byte-cap exemplar **without the qualifier**. The *form* (verbatim, crc32-stamped, pointer left in place) is exemplary; the *stopping point* (100% of budget) is the half-rotation the two-threshold rule exists to prevent.
- **PATTERNS candidate (ANTI):** *a distance-to-threshold annotated with its direction expires faster than the level itself.* SHADE's `STATUS.md:43` does everything right — level, date, basis, distance, **and the direction of travel** (*"17bp below … further away than on 8/13"*). That last clause is the most useful sentence on the surface **and the first to go false**: 20 days later the direction had reversed and the gap had closed 76%. A directional annotation is a **dated claim about a derivative** and needs a shorter shelf-life than the level it decorates. Compare `finding_dated_carry_item_has_no_expiry_check`.

### 9. Reviewer-side defects
1. ⛔ **FLEET_MAP SHADE `Next_upgrade` is incomplete: *"L4 on `PREDICTIONS.tsv` … everything else for L4 is on disk."*** **False.** SHADE has **no `TRADE.md`** — the same L4 leg I hold CORAL on, diagnosed at CORAL on the same day (2026-09-05) with an explicit precedent family (ZHAO/CARL/LIQUID/MIDAS). I applied the TRADE-surface test to CORAL and **did not apply it to SHADE**, then wrote a cell asserting the opposite. `finding_guard_correctness_and_wiring_are_independent` — my own rule missed the desk beside it.
2. ⛔ **"Profile NOT FIRED (floor 9/15)"** is a dated carry-item that went false on schedule and nothing re-evaluated it (`finding_dated_carry_item_has_no_expiry_check`). It is now REFUTED.
3. ⚠️ **The "cite as exemplar" endorsement** in the `Gaps` cell propagates a rotation that stopped at 100% of budget, unqualified.

---

## REGINALD — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-01

### 1. Period production
| Metric | Value |
|---|---|
| Commits touching `AGENTS/REGINALD/` since 9/1 | **68** — by far the highest in R5 |
| Self-authored | **31** |
| Routed-in | **37** |
| Last self-commit | **2026-09-14** (`2af446340`) |
| Dark-days now | **3** |

**What shipped:** four working sessions (9/2 ×3, 9/11, 9/14). 9/2 — read-cap rotations, CARRIED LESSONS aging rule, 12 aged OPEN THREADS closed with per-row verdicts, MTB Baltimore graded off a **frozen pre-registration** to `TRUE AND IRRELEVANT / NO ROW`, a peer-figure sweep finishing its own partial. 9/11 — REG-T-02 exit graded across 5 closes, inbox 25→0, **REG-07 as-made re-form**. 9/14 — catch-up: three rows to 🔴, **and the session's own headline is against itself**: *"★ THE SESSION'S REAL FINDING IS AGAINST MY OWN ROW: the CCC/HY benign read has INVERTED"* (`STATUS.md:2`), followed by ⛔ *"I did **NOT** escalate — the re-arm is one leg short (HY 265 vs 272). **The condition governs the fire**; what changed is the GROUND of Will's 8/13 stand-down, and that is reported, not acted on."*

### 2. Row-claim test
| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | L5 behaviour observed 9/1: REG-T-02 graded by the owner at the registered instrument, attribution separated from the fire | **TRUE-STILL and repeated ×3** — graded again 9/2 ($79.12), 9/11 (five closes, 0-of-3), 9/14 ($79.29, 8 rows logged, state stays FIRED) | `AGENTS/REGINALD/STATUS.md:2`, `:4`; `45cffdd14`, `a19a0dd6d` |
| 2 | THESIS v1.4 RETIRED 8/13 to a pointer stub, STATUS canonical | **TRUE-STILL** — *"⛔ RETIRED 2026-08-13 … THIS FILE IS A POINTER STUB … STATUS.md is now CANONICAL for thesis state (Will-ruled)"* | `AGENTS/REGINALD/thesis/THESIS.md:1-5` |
| 3 | BOTTOM LINE stamps current | ⚠️ **TRUE-STILL but slipping** — BOTTOM LINE re-stamped **9/11**, STATUS head **9/14**. Honest two-state (the header says so verbatim) but a 3-day lag, which is the exact leg that has held L5 before | `AGENTS/REGINALD/STATUS.md:166` |
| 4 | Predictions expiry-swept 8/13 | **TRUE-STILL** — every OPEN row's Notes carry the 8/13 sweep verdict with a live resolution path | `AGENTS/REGINALD/workbook/PREDICTIONS.tsv` |
| 5 | **SOLE SURVIVING L5 LEG: Brier/archive layer absent (standing since 6/29)** | **TRUE-STILL — 80 days.** `find AGENTS/REGINALD -iname "*ARCHIVE*" -o -iname "*BRIER*"` finds **no PREDICTIONS_ARCHIVE and no scoreboard** (only `archive/` dirs and sub-agent fossils). Self-flagged live: *"predictions Brier/archive loop (DAEDALUS standing since 6/29)"* in the aged-still-open list. See §3. | `AGENTS/REGINALD/MEMORY.md:69` |
| 6 | UNVERIFIED ×4 (three-way STATUS macro contradiction · F1 under-scope 7→15 · 3 dead per-bank ledgers · fence-② rides P-OZK-2) | **CANNOT-EVALUATE** — these are confirm-reads at the profile refresh, not scans. I did not open them. | — |
| 7 | BOARD_LOG BACKFILL-PENDING ×3 since 5/9 (Class-10) → REGINALD's next brief (PROME) | **CANNOT-EVALUATE** — but note **BROCK routed a related finding in-period**: *"your `board_log` is at an address `walter_doctor` does not visit"* (`8777c2b47`, 9/12), then **withdrew the mirror recommendation before REGINALD read it** (`f9d69a5be`, 9/12) | `8777c2b47`, `f9d69a5be` |
| 8 | 5 cohort ledgers 14-24 STATUS-writes behind = owner-confirm | **PARTIAL PROGRESS** — `02130c102` 9/14 *"VX ledger catches up to the CCC/HY inversion"*. Whether the other four moved: **CANNOT-EVALUATE** without a per-ledger vintage diff. | `02130c102` |
| 9 | Profile FIRED (MI3 landed, THESIS left v1.4), Δ 8/17 only | **TRUE-STILL — still unserviced.** See §4. | `profiles/REGINALD.md:3` |

### 3. Ladder walk (Market, current L4 → next L5)
| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L1 | STATUS + labeled BOTTOM LINE | **MET** | `AGENTS/REGINALD/STATUS.md:166` |
| L2 | structured record, valid schema, accruing | **MET** — 20 workbook files incl. KB 132,813 B, VX 41,884 B, `MI3_COHORT.tsv` 39,731 B, `registry/THRESHOLDS.tsv` + `registry/NOTES.md` | `AGENTS/REGINALD/workbook/`, `registry/` |
| L3 | convergence matrix + exit rules | **MET** — 8-channel convergence matrix, EXIT RULES section, `registry/THRESHOLDS.tsv` 8 rows with a separate rationale file keyed by `trigger_id` (*"never fold NOTES into the TSV"*) | `AGENTS/REGINALD/STATUS.md` §CONVERGENCE MATRIX, §EXIT RULES |
| L3 | predictions resolving | **MET** — 21 rows, 7 resolved, 4 OPEN, expiry-swept, FROZEN rows stamped | `AGENTS/REGINALD/workbook/PREDICTIONS.tsv` |
| L3 | dated falsification surface | **MET** — `thesis/CHANGELOG.md` live (thesis state moved 🟠→🔴 with a dated entry 2026-09-14); `workbook/THESIS_VALIDATION.md`; REG-T-02's append-only exit log *"so the count is counted, not remembered"* | `45cffdd14`; `AGENTS/REGINALD/thesis/CHANGELOG.md` |
| L4 | TRADE.md feeding proposals | **MET** — `TRADE.md` 31,950 B; **REG-T-02's exit grade guards a LIVE position** (`GATE-TERRY-ROLL70` FILLED 9/2, 1× WAL Dec-18 $70P @ $2.20) | `AGENTS/REGINALD/STATUS.md:4`; `db9660066` |
| L4 | signals flowing | **MET** — 37 routed-in items from WAL/BROCK/HOMER/LABOR/PROME/WALTER in-period; REGINALD is the convergence terminus and the traffic shows it | `git log … -- AGENTS/REGINALD/` |
| **L5** | **clean closeouts** | **MET** — 9/2 ran three closeouts including a "finish the sweep I left partial one commit ago" (`95908b623`) and a CALENDAR past-event pass that found *"three rows reading as PENDING under a 'Forward-looking only' header"* (`4a8d2161e`) | `95908b623`, `4a8d2161e` |
| **L5** | **zero YEYOU flags** | **N/A** — default-zero instrument; WQ-181 ② RULED 2026-09-10 (see §9) | `PROME/WILL_QUEUE.md:85` |
| **L5** | **current** | ⚠️ **PARTIAL** — STATUS 9/14, BOTTOM LINE 9/11 (row-claim 3) | `AGENTS/REGINALD/STATUS.md:166` |
| — | **Brier/archive layer (row-local expectation, NOT a ladder leg)** | **NOT MET** — §2 row-claim 5, and see the ⚠️ below | `AGENTS/REGINALD/MEMORY.md:69` |
| — | read-cap | ⛔ **rc=1, 4 boot reads over budget** — `STATUS.md` **53,374 B = 164%** · `ROADMAP.md` 46,005 B = 141% · `MEMORY.md` 42,746 B = 131% · `CALENDAR.md` 33,278 B = 102%; `NEXUS_BRIEF.md` 27,359 B = 84% rotate-tier | `read_cap_check --agent REGINALD` |

**Recommendation: HOLD L4, Conf H.**
⚠️ **BUT the Brier/archive leg must be re-adjudicated, not carried.** My own MARCO row, written the **same day** (2026-09-05), **STRUCK** the identical expectation with a stated reason: *"🔴 **STRUCK — this was never a ladder leg.** Market L5 is *clean closeouts · zero YEYOU flags · current*; L3 asks only that **predictions resolve**… I appended a row-local expectation and then graded MARCO against it as if it were a gate."* — and named it the **third instance that day** (ORACLE Brier, ZHAO archive/scoreboard). **REGINALD's row carries the same construct, calls it the "SOLE SURVIVING L5 LEG", and was not corrected.** Four instances, one struck. **Recommended row edit: re-classify REGINALD's Brier/archive item from "L5 leg" to "row-local expectation (not a ladder gate)", exactly as MARCO's was, and re-cut `Next_upgrade` to the two legs that ARE the market L5 gate — currency (BOTTOM LINE lag) and the read-cap breach.**
Confidence H on the grade; H on the Brier absence (I searched for it); **M** on "nothing else blocks L5" because row-claim 6's four UNVERIFIED items are still unread at this depth.

### 4. Profile trigger
> `profiles/REGINALD.md:3` — **"⚠️ STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01): MI3 re-derivation landed 8/13 · THESIS left v1.4 (RETIRED 8/13) · Δ 8/17 only. Refresh checkpoint: 2026-09-15."**
> Profile body — **"Staleness (content-derived): re-read when the CONVERGENCE MATRIX scores or EXIT RULES materially change, when `thesis/THESIS.md` bumps off v1.4, **when the MI3 re-derivation lands**, or >45d."**

| Leg | Measurement | Verdict |
|---|---|---|
| MI3 re-derivation lands | landed **2026-08-13** | 🔴 **FIRED 35d ago** |
| THESIS bumps off v1.4 | **retired to a pointer stub 8/13** — off v1.4 in the strongest sense | 🔴 **FIRED** |
| CONVERGENCE MATRIX / EXIT RULES materially change | **§THESIS Stagflation Trap 🟠→🔴, both legs standing, 9/14** — a thesis-state move, not a score tweak | 🔴 **FIRED 9/14** |
| >45d from the 2026-08-07 rewrite | 41 days | **NOT FIRED** (due 9/21) |
| PR#5 checkpoint 2026-09-15 | today 9/17 | 🔴 **BREACHED +2d** |

**Verdict: FIRED on three of four content legs, checkpoint breached.**

**Profile statements now false:**
| Profile text | Live | Locator |
|---|---|---|
| *"`STATUS.md` **248/250 — 2 lines of headroom** (8/7 flag #9)"* | **180 lines** — and the binding constraint has inverted: lines are fine, **bytes are 164% of budget**. The profile watches the wrong dimension. | `read_cap_check --agent REGINALD` |
| *"BOTTOM LINE :236 (7/25)"* / Δ 8/17 *"BOTTOM LINE at :238 (was :236)"* | **`:166`, stamped 9/11** | `AGENTS/REGINALD/STATUS.md:166` |
| *"`VX.tsv` 61 rows, two-clock 2026-04-03 = STALE +126d, `ledger_staleness` FIRING 8d"* | VX refreshed 8/23 and again **9/14** (`02130c102`) | `02130c102` |
| *"KEY CATALYSTS (**4 resolved events in forward tense** under a 'Forward-looking only' header)"* | **FIXED 9/2** — `4a8d2161e` *"CALENDAR past-event pass — three rows were reading as PENDING under a 'Forward-looking only' header"* | `4a8d2161e` |
| *"THRESHOLD STATUS … Claims cell `:226` carries LABOR's superseded 187K"* | **CANNOT-EVALUATE** — line has moved; needs a fresh grep of the Claims cell against LABOR's current figure | — |

### 5. Falsification read — **not in scope** (REGINALD's surfaces are scanner-visible; `thesis/CHANGELOG.md` is live and dated 9/14).

### 6. Negative-resolution leg
**Ledger opened:** `AGENTS/REGINALD/workbook/PREDICTIONS.tsv` (21 rows; `Status` col 6, `Invalidation` col 9, `Notes` col 10). **4 OPEN: REG-01, REG-03, REG-06, REG-07.** Every one of the four has a **negative-class leg** — REGINALD's `Invalidation` column is written as the negative by construction.

| Row | Negative leg (verbatim from `Invalidation`) | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **REG-01** "Office CMBS DQ **stays** >10% through 2026" — persistence; HIT resolves by *nothing dropping* | *"Office DQ <10% for 2+ consecutive months"* | ✅ **YES, named**: *"Instrument IS live and named (**REG-T-07 = Trepp monthly office CMBS DQ**); last read **11.57% [Jun-2026]**"* | ⚠️ **PARTIAL** — monthly cadence + a dated last read, but **no registered next-read date**; Jun-2026 is the last held value (79 days) |
| **REG-03** "$936B maturity wall forces recognition wave" — MISS resolves as *no wave by 12/31* | *"Maturity extensions >80% success rate"* | ⛔ **NO** — no source named for either the wave or the extension rate. The row's own Notes flag a **figure discrepancy** ($936B here vs $875B on STATUS vs CREED's CMBS-only nest) rather than an instrument. | ⛔ none |
| **REG-06** "At least one Tier 1 bank (EGBN, WAL) capital raise" — conf **10%**, so the **modal outcome is the negative** | *"Both avoid capital raise through 2026"* | ⛔ **NO** — no 8-K / press-release / filing scan named. Notes carry dated *evidence* (WAL's 7/22 capital-return pivot, EGBN Q2 CET1 +78bps) but no **search instrument** for establishing the absence. | ⛔ none |
| **REG-07** "SSB NPL migration >0.5% from substandard" | *"SSB NPLs stay <0.3%"* | ⚠️ **IMPLIED, not named** — SSB quarterly disclosure; the Notes cite the 7/25 watch-card fill and the FDIC Q2 QBP | ✅ **YES** — *"the Q3 print is the remaining chance"*, and the row is flagged **OVER-CONFIDENT-PENDING-REMARK** with the re-mark deliberately deferred to that print |

**Counts: candidates opened 4 · confirmed negative-class 4 · lacking a named search instrument 3 (REG-03, REG-06, REG-07).**
⭐ **REGINALD's `Invalidation` column is the right structure** — it forces the negative to be *written down* at registration, which is more than most desks do, and REG-07's *"⚠️ 68% is stale as a live number and I am NOT silently re-marking it … a re-mark belongs in a deliberate pass with the Q3 print, not in a closeout nudge"* is exemplary handling of a disconfirming leg.
⛔ **The gap is one column short:** the negative is *stated* but not *instrumented*. REG-06 is the sharpest case — a 10%-confidence prediction whose expected resolution is "neither bank raised capital", with **no named instrument for establishing that absence** and **no dated search attempt**. Under `FORGE/PREDICTION_DISCIPLINE.md` § Grading, that row cannot be resolved negatively as written. **It expires 12/31 — 105 days.**

### 7. **As-made receipt — DISPOSITIONED.** ✅
Packet `4f7fb2ec2` (2026-09-07) landed at `AGENTS/REGINALD/inbox/processed/2026-09-07_from-DAEDALUS_as-made-confidence-audit-6-mismatch-candidates-harvest-H2.md`. Disposition executed **2026-09-11** (`9f4837ac5`):
- **`AGENTS/REGINALD/registry/NOTES.md:65`** — receipt table row: `| REG-07 | NOT-FOUND | "SSB NPL migration >0.5% **55%**" 2/12; seeded 55%; upgraded 68% 2026-03-05 (e30e09d50, ML-REG-110), documented in Notes but the cell carried only 68%. | **Re-formed: 68% [2026-03-05] (was 55% [2026-02-23]). Brier on 55%.** |`
- **`AGENTS/REGINALD/workbook/PREDICTIONS.tsv`** REG-07 Notes — *"2026-09-11 AS-MADE RESTORED (DAEDALUS H2 audit, WQ-112 form): as-made = 55% (STATUS blob `67d336e32` 2026-02-12; ledger seeded 55% at `91c301279`) … **Brier scores on 55% as-made.**"*
- **Ledger header** — the disposition is recorded at the file's two-clock header with the scope stated: *"ONE AS-MADE PROVENANCE re-form in the WQ-112 machine form (REG-07 only)"*, plus a reasoned **refusal** on REG-06 (*"Kernel-pinned / byte-frozen (Gate C a6/a7) and is NOT re-formed: its as-made 50% is documented in its own 8/27 Notes entry, and a cell-reading tool will still score 10% — read that entry"*) and a **correction of my tool**: the REG-02/03/04 MISMATCH flags are **ID cross-map artefacts**, not confidence walks (the 3/6 STATUS table numbered them differently; confidences agree **by text**).
⭐ **Both as-made desks independently found and reported defects in `scripts/asmade_audit.py`** — MARCO the first-`%`-in-cell parse, REGINALD the ID cross-map. See §8.

### 8. Cross-agent / pattern
- 🔴 **→ DAEDALUS (me), highest priority tool fix:** `scripts/asmade_audit.py` has **two independently-reported defects** from two desks in one harvest: (1) it reads the **first `%` in the cell**, so a Notes field beginning with a July resolution line flags MISMATCH against the row's own text (MARCO: 5 of 9 flags false); (2) it keys on the **ledger's** prediction ID, so a row renumbered between the STATUS table and the ledger flags MISMATCH when the confidences **agree by text** (REGINALD: REG-02/03/04). **Two desks, two failure modes, same run.** The audit's headline counts (`SAME 3 · MISMATCH 5 · NOT-FOUND 12` for REGINALD; `SAME 1 · MISMATCH 8 · NOT-FOUND 7` for MARCO) are therefore **parseability counts, not behaviour counts** — `finding_lenient_parser_reports_unparseable_as_a_behavior`. **Do not feed them to the calibration sitting unfixed.**
- **→ PROME:** REGINALD has **4 boot reads over budget**, STATUS at **164%**. The 9/2 read-cap session (`47dfa5916`) reported *"Over-budget 4 → 3"* — but STATUS was **51,159 B at that commit** and is **53,374 B now**; the session rotated `thesis/CHANGELOG.md` and `CALENDAR.md` and **left the largest surface untouched, then it grew**. The heaviest desk in the fleet is booting on ~203 KB of over-budget reads.
- **→ REGINALD:** REG-06 and REG-03 need named search instruments before 12/31 (§6).
- **PATTERNS candidate (ANTI):** *a struck row-local expectation stays live on every row that was not the one you struck it on.* I struck the "PREDICTIONS_ARCHIVE / calibration scoreboard is an L5 gate" construct on **MARCO** on 2026-09-05, naming ORACLE and ZHAO as the same-day second and third instances — and **REGINALD's row, written in the same batch, still calls it the "SOLE SURVIVING L5 LEG"** 12 days later. The correction was authored, published and **not swept**. `finding_a_ruling_governs_the_next_write_not_the_existing_state` + `finding_hand_fixing_named_rows_is_not_fixing_the_class`: the fix for a construct found on 4 rows is a **grep of every row for the construct**, not four hand-edits minus one.

### 9. Reviewer-side defects
1. ⛔ **The Brier/archive item on REGINALD's row contradicts my own MARCO ruling of the same date** (§3). Four instances that day (MARCO, ORACLE, ZHAO, REGINALD); I struck one and left three. **This is the single most consequential reviewer-side defect in R5**, because REGINALD's `Next_upgrade` names it as *the* L5 gate — so the row currently tells the heaviest desk in the fleet that its promotion is blocked on something that is not a ladder leg.
2. ⚠️ **REGINALD's row carries no byte-budget claim at all**, while the desk has 4 over-budget boot reads including a STATUS at 164%. Compare AEOLUS, where I set Conf M *specifically* on a 23% breach. **The same defect, graded on one desk and invisible on another** — `finding_guard_correctness_and_wiring_are_independent`.
3. ⚠️ **`profiles/REGINALD.md` watches `STATUS.md` line count (`248/250 — 2 lines of headroom`) when the binding constraint is bytes.** The line count has since *fallen* to 180 while bytes rose to 164% of budget, so the profile's own headroom instrument now reads **comfortable** on a surface that is the worst byte breach in the cohort. A correct instrument on the wrong dimension reads as a clean bill — `finding_instrument_reports_clean_against_the_wrong_reference`.
4. ℹ️ **Ladder-leg scope gap (applies to all six desks):** WQ-181 ② ruled the *"zero YEYOU flags"* default-zero leg to **N/A** (Will, 2026-09-10 11:19 ET, tap 15:19Z) for the **9/14 ladder-integrity sitting**, whose recorded scope (`PROME/DOCKET.tsv:285`, `EVOLUTION.md:55-70`) is the **utility** ladder plus five named desks. The leg is textually identical in the **Market** and **Meta** columns of root `CLAUDE.md` §MATURITY LADDER and has **not** been explicitly N/A'd there. I have graded it **N/A** for all six market desks on the reasoning that a leg no reviewer can populate is vacuous regardless of class — **but that is my inference, not a cited ruling.** Flagging for the record rather than assuming the sitting covered it.

---

## COHORT SUMMARY

| Desk | Commits (self/routed) | Dark-days | Rec level/conf | Row-claims T/R/CE | Profile trigger | Falsification verdict | Neg-res (cand/neg/lacking) | Top finding (≤15 words) |
|---|---|---|---|---|---|---|---|---|
| **CORAL** | 4 / 12 | 4 | **HOLD L3 / H** | 5 / 2 / 0 | **NOT FIRED** (ckpt 10/05) | n/a (scanner-visible, dated 11/15) | 3 / 3 / 2 | STATUS regrew 27,442→32,493 B in 11 days; half-rotation re-breached |
| **MARCO** | 3 / 17 | 0 | **HOLD L4 / H** | 4 / 1 / 1 | **NOT FIRED** (ckpt 10/20) | n/a | 4 / 0 / 0 | L4 desk failing an L1 leg, filed on the row as an L5 upgrade |
| **AEOLUS** | 2 / 8 | 6 | **HOLD L3 / M** (no M→H) | 4 / 2 / 2 | 🔴 **FIRED** 3-of-5 legs; ckpt 9/15 breached | **RAIL-IN-LOCAL-FORM** — STATUS:117 triad + `If_Falsified`; 3 evidenced fires | 8 / 4 / 1 (AEO-03) | Profile has 6 false statements; 4 false because the desk FIXED them |
| **HOMER** | 7 / 11 | 3 | **HOLD L2 / H** | 6 / 2 / 0 | 🔴 **FIRED** ×3 legs (9/05 + 3 touches + 38d); ckpt breached | **RAIL-IN-LOCAL-FORM** — per-prediction early-kill + §C; HOM-01 fired 8/31 | 1 / 1 / 0 | Byte gap CLOSED; my row still asks for it. Two L3 legs unbuilt, 22d |
| **SHADE** | **0** / 11 | ⛔ **20** | **HOLD L3 / H** | 6 / 1 / 0 | 🔴 **FIRED** (floor 9/15 +2d, 45d) | **RAIL-IN-LOCAL-FORM** — `CLAUDE.md:48` 4 kill paths + T-SHADE-01; 4-for-4 not-armed | NOT-SEEN (no ledger) | 🔴 HY OAS 276 [9/15] vs the >280 bar; gap 17bp→4bp while dark 20d |
| **REGINALD** | 31 / 37 | 3 | **HOLD L4 / H** | 6 / 0 / 3 | 🔴 **FIRED** 3-of-4 legs; ckpt breached | n/a (CHANGELOG live, dated 9/14) | 4 / 4 / 3 | "Sole L5 leg" is a construct I struck on MARCO the same day |

### Cohort-level observations
1. **Profile layer is the fleet's weakest surface, not the desks.** Four of six profiles have fired triggers; **all four breached the 2026-09-15 checkpoint**; AEOLUS's fan-out is 25 days overdue and HOMER's dated rewrite has been overrun by a deadline *and* three touches *and* a second checkpoint. The desks are largely servicing their own gaps faster than my comprehension layer tracks them.
2. **Four reviewer-side defects, all the same species:** a `Gaps`/`Next_upgrade` cell asserting a **superseded measurement in the present tense** — HOMER's byte tier (closed 9/2), AEOLUS's 23% breach (closed 9/11) and 74% self-share (now 20%), SHADE's "profile NOT FIRED (floor 9/15)" (fired), REGINALD's Brier "L5 leg" (struck on MARCO 9/5). The FLEET_MAP standing rule — *a cell states what is TRUE NOW; how it came to be true goes to HISTORY* — is the right rule and it is not being applied at re-cut.
3. **One live market finding outranks everything structural: SHADE.** HY OAS **276 bps [FRED, 2026-09-15]** against T-SHADE-01's **>280** bar, on a desk carrying **263 [8/27]** annotated *"further away"*, dark **20 days**, with a 5-session sustain clock that can start unobserved.
4. **Negative-resolution canon splits the cohort cleanly by container.** The desks with a *column* for it (AEOLUS `Resolution_Criteria`, REGINALD `Invalidation`, HOMER `Invalidation`+§C) write the negative down; only **AEOLUS** reliably instruments it, and only AEOLUS names the **wrong** instrument and forbids it (AEO-12: *"NEVER the advisories index (JS-rendered, silently stale)"*). REGINALD states four negatives and instruments one. **A column makes the negative visible; it does not make it resolvable.**
5. **Both as-made desks corrected my tool.** MARCO and REGINALD independently found two distinct defects in `scripts/asmade_audit.py` in a single harvest. Its MISMATCH counts are parseability counts, not behaviour counts, and must not reach the calibration sitting unfixed.
