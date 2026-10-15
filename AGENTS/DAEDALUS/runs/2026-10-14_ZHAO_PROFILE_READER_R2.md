# ZHAO profile refresh: reader R2 (evidence and consumption layer)

**Reader:** R2 (read-only; spawned by DAEDALUS) · **Date:** 2026-10-14 (ET) · **Subject:** ZHAO (`AGENTS/ZHAO/`) · **Baseline:** `AGENTS/DAEDALUS/profiles/ZHAO.md` (refreshed 2026-09-05; read whole, 74 lines / 9,240 B)
**Cluster:** PREDICTIONS · VX · VX_HISTORY · FLOW · KB · SCHEMA · docket/CATALYSTS (+README) · reports/ and outbox/ (incl. delivered/) dated ≥2026-09-05 · consumption at recipients' trees · `scripts/ledger_staleness.py`
**Prices:** every market figure below is a **dated ledger value**, quoted only as evidence of what the desk recorded. None is current (root rule #4).

## 0. Files read: bytes and ranges covered

| File | Bytes | Lines | Coverage |
|---|---|---|---|
| `AGENTS/DAEDALUS/profiles/ZHAO.md` | 9,240 | 74 | whole |
| `workbook/PREDICTIONS.tsv` | 61,472 | 19 | **whole**, in 4 chunks (L2–11, 12–13, 14–16, 17–19); EOF confirmed (`…KB-ZHAO-159.\n`) |
| `workbook/SCHEMA.tsv` | 1,829 | 14 | whole |
| `workbook/VX.tsv` | 40,385 | 43 | **whole**, in 3 chunks (L2–15, 16–31, 32–43); EOF confirmed (`…KB-ZHAO-171.\n`) |
| `workbook/VX_HISTORY.tsv` | 492 | 6 | whole |
| `workbook/FLOW.tsv` | 20,623 | 16 | **whole**, in 2 chunks (L2–12, 13–16); EOF confirmed |
| `workbook/KB.tsv` | 257,776 | 197 | **header + L142–L197 whole** (the 56 rows dated ≥2026-09-05; 118,596 B; EOF confirmed). **L2–L141 NOT read**: only whole-file machine passes were run over them (ID contiguity, enum validity, Group tag, Stale_By expiry) |
| `docket/CATALYSTS.tsv` | 26,459 | 22 | **whole**, in 2 chunks; EOF confirmed |
| `docket/README.md` | 3,141 | 35 | whole |
| `reports/2026-09-17_ASMADE_VERIFICATION.md` | 3,124 | 21 | whole |
| `reports/2026-09-17_JULY_TIC_SESSION.md` | 4,202 | 31 | whole |
| `reports/2026-09-18_PREREGISTRATION_ZHA-18_august-tic.md` | 7,792 | 85 | whole |
| `reports/2026-09-18_WQ112_ASMADE_LEDGER_WRITE.md` | 6,807 | 81 | whole |
| `reports/2026-09-19_PREREGISTRATION_mofcom-announcement-70-primary.md` | 5,031 | 51 | whole |
| `reports/2026-09-19_RESULT_mofcom-announcement-70-primary.md` | 7,994 | 76 | whole |
| `reports/2026-09-25_WATT_TRIGGER_WORDING_gonggao58.md` | 4,256 | 34 | whole |
| `outbox/2026-09-19_to-VULCAN-HAWK-HENRY_mofcom-primary-corrections.md` | 5,279 | 52 | whole |
| `outbox/2026-09-19b_to-VULCAN-HAWK-HENRY_CORRECTION-2-dates-and-scope.md` | 5,655 | 45 | whole |
| `outbox/2026-09-25_from-ZHAO_to-BOND_H41-…md` | 1,191 | 9 | whole |
| `outbox/2026-09-25_from-ZHAO_to-HAWK-HENRY-VULCAN_summit-outcome-and-IEEPA-11-10-leg-VOID.md` | 2,358 | 11 | whole |
| `outbox/2026-09-30_from-ZHAO_to-VULCAN-HAWK-HENRY-WATT-MIDAS_MOFCOM-states-1-10-…md` | 1,967 | 11 | whole |
| `outbox/delivered/2026-09-18_*` (6 files) | 3,788 + 2,897 + 5,995 + 4,430 + 3,454 + 5,585 | 40/32/50/53/34/46 | whole, all six |
| `scripts/boot.py` (ZHAO) | n/a | n/a | **lines 88–106 and 225–275 only**, plus grep hits at 68/86/182/184/194 |
| `STATUS.md` (ZHAO) | 26,235 | n/a | **targeted grep only** (lines 4, 7, 38, 95, 108, 110, 140, 163, 173), not read |
| Recipient trees | n/a | n/a | `find` for ZHAO packet copies + targeted `grep` and `head` (§4b), not read |
| `PROME/inbox/processed/2026-09-30_from-ZHAO_ZHA-16-grade-L481.md` | n/a | n/a | lines 1–60 (to its COMPLETION block) |

**Older reports/outbox (pre-9/05), by name only:** `reports/` 2026-07-16_domain-sweep · 2026-08-03_P3_PREREGISTRATION · 2026-08-21_BOOT_PY_AUDIT · 2026-08-21_JUNE_TIC_SESSION · 2026-09-02_PREREGISTRATION_summit-and-july-tic. `outbox/` 2026-07-16_to-BRENT · 2026-07-16_to-MIDAS · 2026-09-02_to-PROME_37-drained. `outbox/delivered/` 2026-07-04 ×2 · 2026-08-03 ×3 · 2026-08-21 ×3.

---

## 1. PREDICTIONS

**Header (12 columns, `PREDICTIONS.tsv:1`):** Pred_ID · Date_Made · Prediction · Confidence · Timeframe · Resolve_By · Anchor_Type · Status · Date_Resolved · Outcome · Invalidation · Notes.
**Totals:** **18 rows** (ZHA-01…ZHA-18). **6 open**, **12 terminal**. The profile's figure was 17; ZHA-18 was added on 9/18.

### 1a. Resolved since 2026-09-05 (4 rows)

| Row | File:line | Outcome | Date | Governing conf | Brier | Basis |
|---|---|---|---|---|---|---|
| ZHA-11 | PREDICTIONS.tsv:12 | **YES** (China not a 30Y-auction long-duration buyer) | 2026-09-17 | 68% [07-16] | 0.1024 | July TIC LT −$7.685B; SAFE commentary absent at title level |
| ZHA-12 | PREDICTIONS.tsv:13 | **YES**, branch (i) both legs | 2026-09-17 | 80% [08-03] | 0.04 | KRW Aug max high 1,440.94 ≤1,500 [as recorded 9/17]; BoK hiked 8/27 to 3.00% |
| ZHA-17 | PREDICTIONS.tsv:18 | **NO**, boundary zone ("continued but decelerating") | 2026-09-17 | 55% [09-02] | 0.3025 | LT −$7.685B in the −$10B ≥ LT > −$5B zone; boundary owner NO |
| ZHA-16 | PREDICTIONS.tsv:17 | **NO**, branch B via the declared residual | 2026-09-30 | 45% [09-02] | 0.2025 | No instrument with an effective date after 11/10; MOFCOM 9/28 statement ≠ instrument; VOID declined (KB-184/190) |

Mean Brier over these four = **0.162**. New registration: **ZHA-18** on 9/18 at 40%, Resolve_By 2026-10-23 (`PREDICTIONS.tsv:19`; letter `reports/2026-09-18_PREREGISTRATION_ZHA-18_august-tic.md`).

### 1b. Open rows: none past Resolve_By

| Row | File:line | Resolve_By | Conf | Resolver-health note |
|---|---|---|---|---|
| ZHA-18 | :19 | **2026-10-23** (9 days) | 40% | August TIC is due Fri 10/16 (KB-195 confirms the Treasury date). Ready |
| ZHA-01 | :2 | 2026-12-31 | 18% | USD/CNY in VX-2.01 is a live pull, last 9/18 |
| ZHA-05 | :6 | 2026-12-31 | 55% | ⚠️ **No live instrument.** Its metric, VX-6.03 (Guizhou NPL 11.6%, Feb-dated), has been FROZEN in notes since 7/16 (`VX.tsv:24`). The row's own note says "do not treat as resolved until … refreshed" |
| ZHA-06 | :7 | 2026-12-31 | 72% | Resolver = the NFRA 2026 count, unpublished (KB-194 `KB.tsv:195`) |
| ZHA-07 | :8 | 2026-12-31 | 70% | ⚠️ Notes unchanged since March ("Feb $456B proved pattern"). No named resolving instrument |
| ZHA-10 | :11 | 2026-12-31 | 40% | ⚠️ "needs a live data check" (since 7/09). No VX row for petro-yuan volume |

**No open row is past its Resolve_By.** Three of the five 12/31 rows have no live resolving instrument. Those are the likely future "hedge token / unfindable grade" cases the desk itself named (ZHA-09 notes, `:10`).

### 1c. Confidence: as-made vs current (ledger machine form, written 2026-09-18 per WQ-112)

| Row | First call (as-made) | Governing / current | Moved? |
|---|---|---|---|
| ZHA-01 | 70% [03-04] | 18% [08-21] (via 55% [03-09], 25% [07-04]) | ↓ ×3 |
| ZHA-03 | 65% [03-09] | 25% [07-04] | ↓ (graded at 25%, not re-scored, WQ-112(i)) |
| ZHA-04 | 65% [03-09] | 42% [07-16] (via 60%, 65% [07-04]) | ↓ (graded at 42%). The prose "65→30→42" has no 30% mark in the ledger (`:5`) |
| ZHA-06 | 60% [03-09] | 72% [07-16] | ↑ |
| ZHA-11 | 65% [07-09] | 68% [07-16] | ↑ |
| ZHA-12 | 55% [07-16] | 80% [08-03] | ↑ |
| ZHA-14 | 35% [07-16] | 30% [07-16] | ↓ |
| ZHA-15 | 55% [07-16] | 18% [08-03] | ↓ (graded at 18%) |
| ZHA-16 | 35% [09-02] (STATUS only, same session) | 45% [09-02] | ↑ pre-event amendment |
| ZHA-02/05/07/08/09/10/13/17/18 | n/a | unchanged | none (ZHA-10's "45% as-made" was a STATUS draft and never entered the ledger, `:11`) |

The mirror conflict on ZHA-01 (STATUS 15% vs ledger 18%) **is reconciled**: STATUS:140 now reads 18% with "ledger governs". A residue remains: VX-2.01's PRIOR (9/2) note still says "ZHA-01 cut 18% → 15%" (`VX.tsv:9`).

### 1d. Ledger-hygiene defects in PREDICTIONS
- **ZHA-13** (`:14`): Status `RESOLVED NEUTRAL`, but **Date_Resolved and Outcome are both blank**, although Notes date the grade to 7/16. Machine scoring cannot see it.
- **Legacy terminal rows lack Resolve_By/Anchor_Type**: ZHA-02/03/04/08/09/13/14/15 (`:3,4,5,9,10,14,15,16`). The profile's "Resolve_By + Anchor_Type populated" holds only for open and newer rows.
- **Compound Status tokens** on `:12` ("RESOLVED YES — China NOT …"), `:13`, `:17`, `:18` and `:19` ("OPEN — PRE-REGISTERED 2026-09-18, 28 days before the print"). ZHAO's `boot.py` prefix-matches (`scripts/boot.py:239–257`), so ZHAO's own surface still sees them. They still breach the desk's own one-field-one-token rule (`docket/README.md` §ONE FIELD ONE TOKEN), and any exact-match fleet reader would miss them.
- **ZHA-12 Invalidation** (`:13`) carries a "July TIC not published by 9/30 ⇒ STUCK" clause. ZHA-12 resolved on the FX print and BoK, so the clause belongs to ZHA-11 and ZHA-17.
- **ZHA-10 Date_Made backdate** (`:11`): ZHAO flagged it 9/18 as "Raise separately". Nothing in my cluster shows it was raised.
- **ZHA-15 Notes** (`:16`) still carry "Fifth Plenum … the 15th Five-Year-Plan venue". This was superseded 10/09 by KB-195 (agenda = Party self-governance). The row is resolved, but the text can still be picked up.

---

## 2. VX / FLOW / KB (+VX_HISTORY, SCHEMA)

| Ledger | Data rows | Latest real-data date | File-level banner / two-clock header | State | Silent staleness |
|---|---|---|---|---|---|
| **VX.tsv** | 42 | **2026-10-09** (VX-6.12 composite PMI, `:36`). Distribution: 9 rows 9/18, 8 rows 9/17, 1 row 10/09, 24 rows ≤9/02 | **None.** No `Last real data refresh` line, by design (KB-164 `KB.tsv:165`: the header breaks ZHAO's own reader) | LIVE, with per-row FROZEN | **Yes**, see 2a |
| **FLOW.tsv** | 15 | **No date column in the schema** (`FLOW.tsv:1`). Last git commit 2026-09-19 (8fa5617f7) | None | LIVE (no banner) | **Yes**, see 2b |
| **KB.tsv** | 196 (KB-ZHAO-001…196, contiguous, no dupes) | **2026-10-09** (KB-192…196) | None | LIVE | 66 ACTIVE/CONFIRMED rows past their own Stale_By (2c) |
| **VX_HISTORY.tsv** | 5 | **2026-02-13** (all 5 "Initial" rows) | **None** | **Undeclared**: not appended since creation and not bannered | `ledger_staleness --strict`: ⚠️ STALE +238d. Default mode exempts it by name. `CLAUDE.md:259` still describes it as "historical vector states behind VX.tsv" |
| **SCHEMA.tsv** | 13 | static dictionary | none | static | `--strict` STALE +215d (expected for a dictionary) |

**`scripts/ledger_staleness.py ZHAO`** (help read first; return codes read bare):
- default: **rc 0**, all "ok" (FLOW +20d, PREDICTIONS +9d, KB +0d, VX +0d behind STATUS). 6 ledgers scanned; `docket/CATALYSTS.tsv` and `registry/corrections_receipts.tsv` are **not scanned**.
- `--writes --abs-floor`: **rc 0** (FLOW abs 25d, PREDICTIONS 14d, KB/VX 5d).
- `--nudge`: **rc 0** ("STATUS not moving this session").
- `--strict --abs-floor`: **rc 1**, with SCHEMA +215d and VX_HISTORY +238d STALE.
- ⚠️ The tool measures **commit time relative to STATUS**. VX and KB were committed 10/09 with STATUS, so they read +0d while individual VX rows carry content that is weeks stale (2a). That is the blind spot KB-164 predicted.

### 2a. VX: stale rows the tool cannot see
| Row | File:line | Problem |
|---|---|---|
| VX-6.06 PBOC policy rate | `VX.tsv:27` | Still reads "**16th due Sun 2026-09-20**". The 9/20 hold was logged in KB-188 (`KB.tsv:189`) and never written back. The October fixing (~10/20 per KB-188) is not shown |
| VX-6.11 NBS mfg PMI (canonical) | `VX.tsv:35` | Shows **Aug 49.8, ORANGE, updated 9/02**. September mfg **50.1** is recorded in VX-6.12's notes (`:36`) and KB-193 (`KB.tsv:194`) but not in the canonical row. On its own bands 50.1 would read YELLOW (<50.5) |
| VX-6.14 RatingDog | `VX.tsv:41` | August value only. The September print (customary 1st business day of October, per CATALYSTS `:3` note) is not recorded |
| VX-1.07 FX reserves | `VX.tsv:8` | End-June value, "Next print ~2026-08-07". Two or more monthly prints are unrecorded; CATALYSTS `:4` says the SAFE leg is "still owed" |
| VX-2.06 KOSPI flows | `VX.tsv:14` | 2026-07-04 (102 days) |
| VX-3.03, 6.13, 1.08, 7.02 | `:18, :37, :38, :33` | 7/04 · 8/03 · 8/03 · 7/04 (7.02 declares itself STALE in notes) |
| VX-2.01/2.03/2.04/2.05/2.08 (live market legs) | `:9, :11, :12, :13, :42` | last 9/18 (26 days) |
| **Notes say FROZEN, Status cell still coloured** | `VX.tsv:23, 24, 25, 28, 30` | VX-6.02 ORANGE · **6.03 RED** · 6.04 ORANGE · 6.07 ORANGE · 6.09 YELLOW. Each note says "FROZEN 2026-07-16 … not maintained", but the machine Status reads live. 6.03 is ZHA-05's resolver |
| **Vector 8 (LNG) has no VX row** | KB-146 `KB.tsv:147`; KB-162(f) `KB.tsv:163` | Logged as a gap 9/17. The proposed ID **VX-ZHAO-8.01 is taken** by the FROZEN "NPC GDP Target" row (`VX.tsv:34`). Still uncreated |

### 2b. FLOW: stale pathways (FLOW cannot age visibly because it has no date column)
| Row | File:line | Problem |
|---|---|---|
| FLOW-02 Property→Fiscal | `FLOW.tsv:3` | "refreshed 2026-09-02". Its registered tripwire (Sept construction >47.5) **fired 10/09** (KB-193; VX-6.12) and is not reflected |
| FLOW-11 Multi-anchor | `FLOW.tsv:12` | Still June TIC with "Next arbiter: July TIC ~Sep 16". July was graded 9/17 and is not reflected |
| FLOW-14 BIS affiliates | `FLOW.tsv:15` | "★ **ALL THREE LEGS LAND 2026-11-10**". The IEEPA leg has been **VOID since 9/25** (KB-183 `KB.tsv:184`; CATALYSTS `:17`) |
| FLOW-15 MOFCOM 公告70 | `FLOW.tsv:16` | Does not carry MOFCOM's 9/28 written statement of 2027-01-10 (KB-189) or the 10/09 re-check (KB-192) |
| FLOW-03 HK peg | `FLOW.tsv:4` | Says "HIBOR-SOFR … YELLOW −136bps (Jul)" and AB "(May 28)". VX-2.04 has been −98.1, GREEN, since 9/18 (−136/−164 retired, KB-154) |
| FLOW-01 / FLOW-12 | `:2`, `:13` | Cite the frozen Guizhou 11.6% as "near RED"; "pending Fri 7/10 sustain verdict" (3 months) |

### 2c. KB: integrity
- **Enum pass (whole file):** Conf, Epistemic, Status, Date and Stale_By are all valid. Status: 145 ACTIVE / 37 CONFIRMED / 10 CORRECTED / 4 SUPERSEDED.
- **Group tag:** 1 invalid. `KB-ZHAO-125` (`KB.tsv:126`, 2026-08-21) uses `CHINA`, which is not in `AGENTS/VOCABULARIES.tsv` NETWORK_GROUPS (only ASIA_CONTAGION and UST_FOREIGN are).
- **Past Stale_By:** **66 ACTIVE/CONFIRMED rows** have passed their own Stale_By (whole file). **12 of them are dated ≥9/05**: KB-147, 155, 157, 158, 165, 167, 168, 181, 182, 184, 186, 189 (`KB.tsv:148,156,158,159,166,168,169,182,183,185,187,190`).
- **Vectors cross-references that point at the wrong subject** (the defect class ZHAO named itself in KB-162, `KB.tsv:163`). Machine-mapped for rows ≥9/05:

| KB row (line) | Subject | Cites | That VX row is |
|---|---|---|---|
| KB-166 (`:167`) | MOFCOM 公告70 clock | VX-ZHAO-6.06 | PBOC Policy Rate |
| KB-167 (`:168`) | ZHA-16 grading hazard | VX-ZHAO-6.06 | PBOC Policy Rate |
| KB-168 (`:169`) | PBOC yuan management | **VX-ZHAO-1.06** + 6.06 | **Agency MBS Rotation (FROZEN)** |
| KB-172 (`:173`) | MOFCOM primary confirm | VX-ZHAO-6.06 | PBOC Policy Rate |
| KB-175 (`:176`) | never-commenced clauses | VX-ZHAO-6.06 | PBOC Policy Rate |
| **KB-194 (`:195`, written 10/09)** | China bank closures | **VX-ZHAO-4.01** | **SUPERSEDED China Mfg PMI**. Should be VX-6.05 |
| **KB-196 (`:197`, written 10/09)** | PBOC fix 10/08 | **VX-ZHAO-6.01** | **LGFV Total Debt**. Should be VX-2.01 |

That is 7 of 56 post-9/05 rows. **Two were written on 10/09, three weeks after ZHAO's own 9/18 audit named this exact defect and proposed a check.** DAEDALUS's disposition says that check ("②") was **not built** (`AGENTS/DAEDALUS/runs/2026-09-24_CATCHUP_DISPOSITIONS.md:21`).

---

## 3. CATALYSTS

`docket/CATALYSTS.tsv` has 21 data rows and 8 columns (date · event · what_to_check · threshold_signal · priority · who_cares · notes · date_class).

### 3a. Next 30 days (2026-10-14 → 11/13)
| Date | Event | Row | Priority / date_class |
|---|---|---|---|
| **Fri 2026-10-16** (16:00 ET) | **August TIC**: China LT leg (ZHA-18), Belgium YoY, Korea | `CATALYSTS.tsv:14` | P1 🔴 / external (Treasury sb0631 date confirmed, KB-195) |
| Mon 2026-10-19 | RE-CHECK: BIS Entity List package + MOFCOM restriction; 公告2024年第46号 cl.2 primary owed (KB-185/192) | `:15` | P2 / modeled |
| 2026-10-23 | ZHA-18 Resolve_By (read by `catalyst_countdown.py` from PREDICTIONS) | `PREDICTIONS.tsv:19` | n/a |
| **2026-10-26 → 10-29** | **Fifth Plenum, 20th CC.** Confirmed 10/09 at the primary (Politburo 9/21, Xinhua via gov.cn). **Agenda = Party self-governance, NOT the 15th FYP** (that was the 2025 Fourth Plenum) | `:12`; KB-195 `KB.tsv:196` | P2 / confirmed |
| 2026-11-10 | BIS Affiliates Rule reimposition effective (stay's last day 11/09) | `:16` | P1 / confirmed |
| 2026-11-10 | MOFCOM/GAC 公告2025年第70号 suspension expires | `:18` | P1 / confirmed |
| 2026-11-10 | US IEEPA reciprocal-tariff "clock" | `:17` | **VOID** since 9/25 (priority `DONE`) |

Outside the window: 11/27 (公告46 cl.2, `:19`) · 12/01 SEC clearing (`:20`) · 2027-01-25 NBIM (`:21`) · 2027-05 (`:22`).

### 3b. Past-dated rows not dispositioned
- `:4` **2026-09-07 (P2)**: the trade leg resolved, but the **"SAFE Aug reserves/gold leg NOT pulled — still owed"**. The row is still P2, not DONE.
- `:11` **2026-10-01 (P3)**: H.4.1 for the week ending 9/30 was registered as "the correct reader" for BOND's 5Y question (KB-186). **No result is recorded.**
- Every other past-dated row is `DONE` with a result.

### 3c. August TIC (10/16): readiness and one live defect
- Ready: ZHA-18 is pre-registered with a branch map, boundary owner and STUCK rule (`PREDICTIONS.tsv:19`; letter §1). The date is confirmed.
- ⚠️ **The row boot.py will surface on 10/16 lacks the letter's key instruction.** `CATALYSTS.tsv:14` THRESH reads "Belgium <10% YoY = first of two kill-leg prints". The letter (§2) and KB-159 (`KB.tsv:160`) declare that the Aug and Sep Belgium prints are to be recorded **SATISFIED-ON-BASE-EFFECT, not as evidence**. VX-1.04 (`VX.tsv:5`) and STATUS:38/110 carry that caveat; the catalyst row does not. The row's NOTES ("Register the ZHA letter in reports/ before 10/16") are stale: the letter was registered 9/18. This is the surface-the-reader-travels defect (KB-162), with a P1 event two days away.

### 3d. Missing rows (no row exists; the dates below are customary windows, not verified)
- **RatingDog September PMI.** `:3`'s own note instructs "Set the September row to ~2026-10-01". The row was never created.
- October LPR (~10/20; KB-188 notes "Next fixing ~10/20").
- SAFE September reserves · China September trade and CPI/PPI · China Q3 GDP · October NBS PMI (~10/31).

### 3e. Other CATALYSTS defects
- `:18` (公告70) **CHECK and THRESH cells still hold the pre-correction content**: "Pull the primary text (NOT yet fetched — KB-166 sits at Conf B2)" (discharged 9/19), "for military AI" (corrected KB-174) and "this is the EXPANSION returning, not controls appearing" (corrected KB-175). The corrections live only in NOTES.
- `:16` NOTES "★ ALL THREE CLOCKS NOW LAND 2026-11-10" contradict `:17` VOID (9/25).
- `:15` THRESH "grades as ZHA-16 branch C if inside the summit window": ZHA-16 was graded 9/30.
- `DONE` is used as a priority token on 10 rows. `docket/README.md` declares P1/P2/P3 only.
- `:12` (10/26) sits ahead of `:13` (10/09): out of date order (cosmetic).

---

## 4. L3 and L4 legs

### 4a. L3 (market class)
| Leg | Evidence in my cluster | Verdict |
|---|---|---|
| Convergence matrix | **28/60 as of 2026-10-09** (KB-193 `KB.tsv:194`: V5 5→4 on the pre-registered construction tripwire; STATUS:7 and STATUS:95 "computed FROM the rows … 9/18 was 29"). Path: 28 (9/02) → **29 (9/17, V8 3→4 on the LNG leg, KB-146 `KB.tsv:147`)** → 28 (10/09) | PASS. The flat total again hides rotation |
| Predictions resolving | 4 graded since 9/05 with Brier, all on registered letters, none re-marked before grading (§1a); WQ-112 machine form written 9/18 | PASS |
| Dated falsification surface | ZHA-18 letter (branches, boundary owner, STUCK); the construction tripwire **fired and was applied by its letter**, with the disagreement recorded (KB-193); ZHA-16 VOID declined in the flattering direction (KB-184/190); the Belgium kill-leg **declared degenerate before the print**, re-spec deferred to 10/23 (STATUS:108, :163) | PASS, exercised. ⚠️ One kill leg is known-degenerate until 10/23 |

### 4b. L4: do signals reach a consumer? Yes, with consumption shown at recipients' artifacts
| ZHAO packet (date) | Recipient | Delivery | Uptake at the recipient's own surface | Verdict |
|---|---|---|---|---|
| July TIC (9/17) | LIQUID | `LIQUID/inbox/processed/2026-09-17_from-ZHAO_july-tic-…` | `LIQUID/reports/2026-09-17_session.md:19–21` §④ integrates the official/private reversal, the anti-mirror and the route not tripped | **INTEGRATED** |
| Belgium YoY base effect (9/18) | HANS, LIQUID | processed ×2 | `HANS/workbook/ML.tsv:465` (ML-HANS-461: "does not bite", hub rows are level-shaped) + HANS reply 9/18 (ZHAO `inbox/processed/2026-09-18_to-ZHAO_hub-thresholds-are-level-shaped-but-your-warning-found-a-live-error.md`); `LIQUID/board_log.tsv:297` NO-OP (bare-level route) | **CONSUMED** (checked; no-op on their books) |
| Record yield gap (9/18) | HENRY, LIQUID | processed ×2 | `HENRY/board_log.tsv:394` noted (US leg superseded; "cite VX-ZHAO-2.08, do not copy"); `LIQUID/board_log.tsv:298` integrated the against-the-carry line | **CONSUMED** |
| BIS affiliates (9/18) | VULCAN, HAWK, HENRY | processed ×3 | `VULCAN/docket/CATALYSTS.tsv:10–12` (ZHAO re-check + both 11/10 rows); `HENRY/board_log.tsv:393` info-only | **INTEGRATED** |
| China half / 公告70 (9/18) | VULCAN, HAWK, HENRY | processed ×3 | VULCAN reply 9/25 "both asks answered: it does not" (KB-191 `KB.tsv:192`) | **INTEGRATED** |
| Corrections 9/19 (superseded) + 9/19b | VULCAN, HAWK, HENRY | PROME routed both 9/22 (`HAWK/board_log.tsv:345`, commit a307a3387) | HAWK `:346` **acted** (KB-HAWK-404→409, `HAWK/workbook/KB.tsv:413`); HENRY `:395` correctly *skipped* the superseded copy, `:396` info-only; VULCAN adopted correction #2 in full (KB-191) | **ACTED** |
| IEEPA leg VOID (9/25) | HAWK, HENRY, VULCAN | processed ×3 | HAWK `board_log.tsv:356` **acted** (KB-HAWK-410 "two live clocks", `KB.tsv:414`); VULCAN adopted the VOID read (KB-191); **HENRY: no board_log row found** | ACTED (2/3) |
| H.4.1 custody (9/25) | BOND | `BOND/inbox/processed/2026-09-25_from-ZHAO-via-PROME_…` | `BOND/workbook/KB.tsv:340` (KB-BND-339 consumed) | **CONSUMED** |
| WATT trigger wording (9/25) | WATT | `WATT/inbox/processed/2026-09-25_from-ZHAO_battery-channel-trigger-…` | `WATT/STATUS.md:29, 114, 115`: triggered channel registered on ZHAO's T1/T2 wording | **INTEGRATED** |
| MOFCOM 1/10 in writing (9/30) | VULCAN, HAWK, HENRY, WATT, MIDAS | ⚠️ **No copy of ZHAO's packet exists in any recipient tree.** The content went out as WALTER BOARD signal `SIG-W-20260930-003` ("(ZHAO)"), processed in all five `inbox/WALTER/processed/` | `HAWK/board_log.tsv:367` noted; `HENRY/board_log.tsv:452` info-only | CONSUMED **via WALTER relay**; ZHAO's own file sits undelivered in `outbox/` |
| Factory-gate (corrected, 9/18) | HENRY, MARCO, MIDAS | processed ×3 | **No board_log or KB row found** at any of the three | **Moved only.** Notification consumed, no recorded disposition |
| Tooling gaps (9/18) | DAEDALUS | processed | `DAEDALUS/runs/2026-09-24_CATCHUP_DISPOSITIONS.md:21`: ① FIXED (fleet comment-header skip, 11 desks newly supervised); ② semantic cross-ref check NOT built | ACTED (½) |
| PROME (14 packets, 9/17–10/09) | PROME | all in `PROME/inbox/processed/` | not verified past the processed move | processed |

**L4 verdict: PASS, and stronger than at 9/05.** Consumption is shown at **HAWK (acted twice), VULCAN, WATT, LIQUID, BOND, HANS and DAEDALUS** through rows, catalyst entries and channels on their own artifacts. Weak spots: MARCO/MIDAS/HENRY on the factory-gate correction and HENRY on the IEEPA VOID (moved only), and the 9/30 packet arriving by relay only.

---

## 5. Profile claims (§2/§3/§6/§7) tested against this cluster

| § | Claim | Verdict | Evidence |
|---|---|---|---|
| §2 | Last session 2026-09-02 | **CHANGED** | Sessions on 9/17, 9/18, 9/19, 9/25, 9/30 and 10/09 (KB row dates `KB.tsv:142–197`; PROME processed packets; last STATUS commit 011af3188 on 10/09) |
| §2 | STATUS 32,534 B = 99.95% | **CHANGED** | Rotation #2 on 9/17 (KB-148 `KB.tsv:149`). `archive/` holds STATUS_COLD_20260917 · 20260918 · 20260918b · 20260925. STATUS is now **26,235 B = 80.6%** (ls), regrown from "<70%" on 9/17. Not read |
| §2 | PREDICTIONS 17 rows with Resolve_By + Anchor_Type + Invalidation | **CHANGED** | 18 rows. The columns exist (`:1`), but Resolve_By/Anchor_Type are blank on 8 legacy terminal rows (§1d) |
| §2 | Inbox 4 | **CHANGED** (listing only) | 4 root-lane (all MIDAS, 10/12) + 5 WALTER-lane unprocessed (10/10–10/14). Not read |
| §2 | Falsification: STATUS :132/:136 | **NOT-CHECKED** (line refs) / TRUE-STILL in substance | Kill letter now at STATUS:108 (grep); VX-1.09 "PROXY STAYS FALSIFIED" (`VX.tsv:39`), VX-1.10 "REFUTED AGAIN" (`:40`) |
| §2 | Archive STATUS_COLD_20260902 + 7 older | **CHANGED** | 4 more cold splits since then (names above) |
| §3 | Convergence 28/60 with rotation called out | **TRUE-STILL** (via 29 and back) | KB-146 → 29 (9/17); KB-193 → 28 (10/09); STATUS:95 |
| §3 | Exit rules print-counted | NOT-CHECKED | STATUS not read |
| §3 | Predictions resolving (4 resolved 8/21) | **TRUE-STILL, extended** | +4 resolved 9/17–9/30 (§1a) |
| §3 | Dated falsification surface present | **TRUE-STILL** | §4a |
| §3 | Routing consumed | **TRUE-STILL, stronger** | §4b |
| §5.1 | Belgium proxy falsified; preserve the method, don't restore the proxy | **TRUE-STILL** | rho +0.067, n=42 (`VX.tsv:39`; KB-151) |
| §5.3 | boot.py parses the TIC month from VX-1.02 Source ("Mon YYYY") | **TRUE-STILL** | regex at `scripts/boot.py:184`; Source = "TIC Jul 2026 (Table 3/1/5)…" (`VX.tsv:3`) still matches |
| §5.4 | KB enum discipline schema-enforced | **TRUE-STILL, one leak** | Conf/Epistemic/Status 100% valid; 1 invalid Group tag (`KB.tsv:126`) |
| §5.6 | Confidence-move trails in PREDICTIONS Notes are deliberate | **TRUE-STILL, upgraded** | Now also in machine form `X% [date] (was …)` in the Confidence column (WQ-112 write, 9/18) |
| §6 | L1–L2: "6 accruing schema-valid ledgers" | **FALSE-NOW (count)** | 4 accrue (KB, VX, PREDICTIONS, FLOW). VX_HISTORY has not accrued since 2/13; SCHEMA is static (`--strict` flags both) |
| §6 | L3 convergence / predictions / falsification | **TRUE-STILL** | §4a |
| §6 | L4 TRADE ADAPTED-PASS | NOT-CHECKED | TRADE.md not in cluster (mtime 7/09, unchanged) |
| §6 | L4 consumption PASS (LIQUID 8/23, HANS :174) | **TRUE-STILL, re-evidenced on new items** | §4b (HAWK KB-410, WATT STATUS:29, VULCAN CATALYSTS:10–12, BOND KB-BND-339) |
| §6 | L5 clean closeouts FAIL (1 of 2) | **CHANGED** (filename evidence only) | ZHAO `inbox/processed/2026-09-17_from-DAEDALUS_PR6-PR6-second-clean-cycle-MET-…md`. Not opened |
| §6 | L5 current (3 days) | **TRUE-STILL, borderline** | Last session 10/09, 5 days ago; WEEKLY cadence declared 9/30 (PROME packet). ZHA-18 needs a session between 10/16 and 10/23 |
| §7 F-2 | STATUS regrows to the ceiling quickly after splits | **TRUE-STILL (pattern persists)** | 4 cold splits 9/17–9/25; STATUS back at 80.6% by 10/09 |
| §7 F-1, F-3 | map-row error; venv-preserving fix | NOT-CHECKED | out of cluster |
| §8 | VX_HISTORY: revive or FROZEN-banner? | **STILL OPEN, now flagged by tooling** | `--strict` STALE +238d |
| §8 | Cadence: close YES-ACTIVE? | **Evidence supports YES-ACTIVE** | 6 sessions in 23 days (9/17–10/09); WEEKLY declared 9/30 |

---

## 6. Defects to route to ZHAO (ranked)

| # | Defect | File:line | One-line fix |
|---|---|---|---|
| 1 | **The 10/16 P1 catalyst row omits the SATISFIED-ON-BASE-EFFECT rule and carries a stale "register the letter" note.** Event in 2 days | `docket/CATALYSTS.tsv:14` | Put the letter §2 rule into THRESH; point NOTES at `reports/2026-09-18_PREREGISTRATION_ZHA-18_august-tic.md` |
| 2 | **7 KB Vectors cross-refs point at the wrong subject**, 2 of them written 10/09 after the 9/18 self-audit | `KB.tsv:167,168,169,173,176,195,197` | Repoint (KB-194→VX-6.05, KB-196→VX-2.01, 168→VX-2.01, the 6.06 cites → FLOW-14/15 or none). For DAEDALUS: KB-162's proposed semantic check is still unbuilt |
| 3 | **Facts land in KB but the reader's surface is not updated** (KB-162 pattern, recurring) | `VX.tsv:27` (9/20 LPR) · `VX.tsv:35` (Sept PMI 50.1) · `FLOW.tsv:3` (tripwire fired) · `FLOW.tsv:12` (July TIC) · `FLOW.tsv:15` + `CATALYSTS.tsv:16,18` (three-clock text after IEEPA VOID) · `CATALYSTS.tsv:18` CHECK/THRESH pre-correction | Write each KB result back to its VX/FLOW/CATALYSTS home in the same session |
| 4 | **Three open 12/31 predictions have no live resolving instrument** | `PREDICTIONS.tsv:6` (ZHA-05; VX-6.03 frozen) · `:8` (ZHA-07) · `:11` (ZHA-10) | Name the arbiter now, or declare a STUCK branch before 12/31 |
| 5 | **VX rows frozen in Notes but live-coloured in Status** (6.03 reads RED) | `VX.tsv:23,24,25,28,30` | Set Status=FROZEN with a 🧊 value prefix, as rows 1.05/2.02/etc. do |
| 6 | **Undispositioned past rows and missing catalyst rows** | `CATALYSTS.tsv:4` (SAFE leg), `:11` (H.4.1 10/01); missing RatingDog Sept (instructed at `:3`), Oct LPR, Q3 GDP, Sept data, Oct PMI | Disposition the two rows; add the missing rows |
| 7 | **VX_HISTORY is neither appended nor bannered** (strict STALE +238d) | `workbook/VX_HISTORY.tsv:1–6`; `CLAUDE.md:259` | FROZEN-banner it (or resume appends) and amend the CLAUDE.md file-map line |
| 8 | **ZHAO's own reader blocks the two-clock header.** The fleet `validate_all.py` was fixed 9/24 (comment skip at `scripts/validate_all.py:482`); ZHAO's `_read_tsv` was not. FLOW has no date column at all | `AGENTS/ZHAO/scripts/boot.py:94–101`; `FLOW.tsv:1` | Skip leading `#` lines in `_read_tsv`, then adopt `Last real data refresh:`. Give FLOW a Last_Updated column |
| 9 | **PREDICTIONS hygiene** | `:14` (ZHA-13 Date_Resolved/Outcome blank) · `:13` (ZHA-12 misapplied STUCK clause) · `:12,13,17,18,19` (compound Status tokens) · `:11` (ZHA-10 Date_Made backdate) · `:16` (superseded Fifth-Plenum/FYP text) | Fill 7/16 + NEUTRAL; move annotations to Notes; raise the ZHA-10 date; annotate ZHA-15 |
| 10 | **Vector 8 (LNG) still has no VX row, and the planned ID collides** | KB-146 `KB.tsv:147`; `VX.tsv:34` | Create it under a free ID (not VX-ZHAO-8.01) |
| 11 | **66 ACTIVE/CONFIRMED KB rows past their Stale_By** (12 post-9/05) | §2c line list | Expiry sweep: refresh, mark STALE or SUPERSEDED |
| 12 | Invalid Group tag `CHINA` | `KB.tsv:126` | Retag ASIA_CONTAGION (or propose CHINA to VOCABULARIES) |
| 13 | Outbox hygiene: 9/19–9/30 packets left at `outbox/` top level (9/18 ones were moved to `delivered/`); the 9/30 packet was never delivered as a file | `outbox/2026-09-19*`, `2026-09-25*`, `2026-09-30*` | Move them to `delivered/` with a note on the route (9/30 = WALTER SIG-W-20260930-003) |

---

## 7. NOT-READ / coverage limits
- **KB.tsv L2–L141** (KB-ZHAO-001…140, dated 2026-02-xx…2026-09-02): **not read**. Only whole-file machine passes (ID contiguity, Conf/Epistemic/Status/Date/Stale_By enums, Group tag, Stale_By expiry list).
- **ZHAO STATUS.md, CLAUDE.md, NEXUS_BRIEF.md, TRADE.md, LAST_COMPLETION.md, board_log.tsv, registry/corrections_receipts.tsv**: not read. STATUS was grepped at 9 lines; CLAUDE.md at line 259 only.
- **ZHAO inbox/** (4 root + 5 WALTER unprocessed, plus processed/): listing only. The DAEDALUS PR6 9/17 packet is cited by filename only.
- **ZHAO scripts/boot.py**: lines 88–106 and 225–275 plus regex grep. `catalyst_countdown.py` not read.
- **Pre-9/05 reports and outbox**: names only (§0).
- **Recipient trees**: `find` plus targeted grep/head only. LIQUID/STATUS.md has 0 "ZHAO" hits now (uptake verified in its 9/17 session report and board_log instead). PROME's handling of the 14 ZHAO→PROME packets was verified only as "moved to processed/". WALTER's 9/17 processed packet was not opened.
- **The "missing catalyst" dates in §3d** are customary release windows from general knowledge, **not verified** in-repo. They are offered as rows to create, not as dated facts.
- `validate_all.py` was not run (cited only for its comment-skip code at line 482). `read_cap_check --agent ZHAO` was not run (not in this cluster).
