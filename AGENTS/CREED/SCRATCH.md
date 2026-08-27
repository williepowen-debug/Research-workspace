# CREED SCRATCH.md — Ephemeral Session State

**Rewritten:** 2026-08-27 (crash-recovery boot → band revisit → CORAL feed → trap widening; **four work items, all closed**)
**Purpose:** the *handoff* surface — "what was I mid-way through, and what should the next spawn do first." Overwritten every session. **Durable analysis → `STATUS.md`; structural changes → `MAINTENANCE.md`; nothing here is canonical.**

> **Canonical-truth ordering, and this file is at the BOTTOM:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/` > `SCRATCH.md`. **If SCRATCH disagrees with anything above it, SCRATCH is wrong.**
>
> ⚠️ **A crash lands on THIS surface first.** Commits are atomic and survive; SCRATCH is rewritten LAST at closeout, so after any unclean exit it is the file most likely to be a window stale — while being the one the next boot reads FIRST. **Diff the commit log against §MAIL before trusting it.** *(Learned the hard way this morning: two packets sent, committed, and absent from this file, and §3 would have made the next boot re-send one.)*

---

## 🔴 NEXT-BOOT FIRST MOVES

1. **🔴 AUGUST TREPP PRINTS (~early Sept) — the nearest live trigger, and now the ONLY unquestioned one.** `CREED-T-01a` sits **9bp** from firing (office DQ 11.91% vs `>12`, sustain 2) — **0.24× the mean monthly move**, i.e. well inside one month's noise. ⚠️ **Watch `VX-CREED-3.04` on the DOLLAR series via `VX-CREED-3.05`, not the share** (trap #11; T-02 already FIRED and is spent). ⚠️ **Check `AGENTS/WALTER/sources/` for the archived PDF first** (trap #3). **Same pull feeds CORAL cycle 2 — and SEND THE ZEROS if no FL asset is named.**
1b. 🔴 **READ `registry/PREREG_2026-09_TREPP_PRINT.md` BEFORE READING THE AUGUST PRINT — it is FROZEN and its whole value is its date.** Fixed in advance: a single print ≥12 is **one leg of two, NOT a fire**; `12.00` is not `>12`; no band moves in response; **and a `T-01a` fire does NOT license any claim about the maturity mechanism** (see §2 below). Falsifiers registered. **Append the grading record below its line; do not edit above it.**
2. **⚖️ `VX-4.01` / `CREED-T-03` BASIS DEFECT — WITH WILL, but a REGINALD answer may beat the ruling.** 🆕 **Question sent 8/27 (`8855234c3`): does REGINALD carry a non-owner-occupied-specific large-bank PDNA series?** **A yes ⇒ fix (a) is a `source_of_truth` re-point, i.e. OWNER LANE under the 8/20 pointers-aren't-bands precedent — no ruling needed, trigger live again.** A no ⇒ it stays with Will as a band re-base. **Check REGINALD's reply first.** ⛔ **Never move the band to fit 2.48.** Do NOT re-grade the level leg until one path closes. `3.40%` is not reproducible from the FDIC Q1-2026 QBP it cites (that cell reads **2.73%**). `KB-CREED-024`. ⛔ **Never move the band to fit 2.48.** **Ask REGINALD first — likely one line: does it carry a non-owner-occupied-specific large-bank PDNA series?**
3. **⚖️ `CREED-T-08a` basis declaration — STILL WITH WILL, PROPOSED NOT RULED.** Band `< -10` does not say total-return or price-only; the two differ **0.65pp ≈ 6.5% of the 10pp band**. Low stakes now (~2.1σ away).
4. **`PRED-CREED-006` + `010` joint verdict — MBA Q2, ~mid-Sept.** `010`'s Athene leg is at its terminal interim state (PARTIAL, Δ +$6.9B, $103M short). **Do not grade `010` standalone.**
5. **`VX-9.03` standing duty — Q3 prints (~late Oct):** pull **CBRE (canonical) AND Moody's + C&W as context rows, every quarter.** ⚠️ **Skipping the context rows silently kills the band re-base.** Grade on **ABSORPTION DIRECTION** until re-based.
6. **HOMER owed a narrow, named item** (agreed 8/27, NOT a revived courier): **MF maturity-adjusted DQ + MF SS rate, back-filling gap months, on the next whole-Trepp pull. No cadence promised.**

## ✅ CLOSED THIS SESSION — do not re-raise

- **VX BAND MONTH-1 REVISIT — RUN, RULED, EXECUTED.** Artifact `registry/BAND_REVISIT_2026-08-27.md`. Will: *"Approve all three asks - go ahead"* (`PROME/proposals/2026-08-27_creed-band-asks-RULED.md`). **`T-01b` sustain 1→2** *(sole frozen-field edit; `>18` untouched)* · **`VX-CREED-3.05` dollar vector registered NO BAND** *(deferred by ruling; the n=4 refusal was itself ruled)* · **base-rating re-keyed DATE → n=12**, homed at `THRESHOLDS` header **(D)** *and* PROME's docket.
- **CORAL FL-SLICE FEED — cycle 1 delivered** (24 days late). ⚠️ **Standing debt discharged; the feed is now live and CREED owes cycle 2 on the August print.**
- **Standing trap #7 WIDENED** — `n=3`, one document class. `MAINTENANCE.md` §2026-08-27 + `CLAUDE.md` #7 (mirror: SCRATCH #12).
- **Owner-lane registry work:** `T-04`/`T-06`/`T-06b` pointers wired; `threshold_scan.py` hardened twice.
- 🆕 **Will-approved follow-ups ("1+2+3+5 approved"), ALL DONE 8/27:** ① REGINALD `T-03` question sent · ② the symptom-vs-mechanism finding registered (`COVERAGE` blind spot 9) · ③ September print **pre-registered** · ⑤ **`VX-CREED-5.03` built**, `T-06b` now machine-gradeable (comparable rows **3 → 4**). ⛔ **Item ④ (a registered spawn occasion for the Sept print) was NOT approved — do not re-raise it.**

## ⚖️ AWAITING WILL — **2 open**, both basis items, neither blocking

Both are §1's items 2 and 3 above. **Durable copies: `registry/THRESHOLDS.tsv` header entries (A) and (B).** Next QBP ~late Nov, so there is time.

## 🟡 STATE AT HANDOFF

- **Base case:** *selective CRE recognition accelerating* — **HOLDS**, tested on both sides. **🟠 ELEVATED. Convergence 25/45 (55.6%) — UNCHANGED.**
- **🔴 `CREED-T-02` FIRED** (8/20, effective JUNE). **Read NARROWLY: a CMBS-recognition event, NOT a bank event.** REGINALD and LIQUID concur in those words. ⚠️ **It is SPENT — a fired binary trigger says nothing further, which is why `VX-3.05` now exists.**
- **✅ `CREED-T-03` GRADED NOT FIRED** (8/27) on all three conjunctive legs, **decided on the basis-independent reserve-coverage leg (166.8% → 172.7%)** — safe to publish while the level leg is impeached. **S3 HELD AT 2. STILL PRE-BANK-TRANSMISSION.** ⚠️ **The one-sided scope limit was APPLIED, not waived. A clean print is NOT "no CRE stress at banks."**
- **🟠 THE COMPOSITION IS RECOGNITION, NOT HEALING, and it splits by bank size.** Regionals **CRE OREO +26.4% in one quarter** while PDNA fell; large banks **charging off** (CRE NCO 0.14% → ~0.22%, +57%) with OREO shrinking. **C&D PDNA at >$250B +3bp — the only CRE-family category rising there.** ⚠️ **Accounting-scale comparison, NOT attribution.**
- 🔴 **SYNTHESIS TO CARRY FORWARD:** leasing improving **and** lenders easing **and** bank CRE books cleaning up — **while $3.96B of matured balloons still could not clear in a month.** ⇒ **a CAPITAL-STRUCTURE / MATURITY event; the binding constraint is the ASSET AGAINST THE COUPON.** **That is why T-02 fired and T-03/T-07 did not, and it narrows the bear case to VALUES AND DEBT.**
- **Trigger board:** `T-01a` **11.91, 9bp below — nearest** · `T-01b` 16.58 (142bp below, moving away, **sustain now 2**) · `T-02` **FIRED** · `T-03` NOT FIRED, level leg impeached · `T-06` **wired, NOT machine-gradeable** (`[QUALITATIVE-VALUE]`) · 🆕 `T-06b` **NOW GENUINELY GRADEABLE** — `VX-CREED-5.03` built 8/27, CLEAR at 0 vs `>=1` ⚠️ **on a 7/27 vintage; verifying the count is its first duty** · `T-08a` ~2.1σ, basis undeclared · `T-08b` ⚠️ **7/27 state, cohort tape ~5wk stale, NOT re-verified.**
- **Predictions: n=2, 1/2, mean Brier 0.306.** ⚠️ **NOT a calibration read — both graded rows were priced on premises that did not hold.**
- **Source tier:** Trepp **PRIMARY-READ** Apr–Jul · **FDIC QBP PRIMARY-READ** · CBRE/C&W/JLL Q2 office PRIMARY-READ.
- **STATUS 290 lines** — under the 320 trigger and the ~300 soft target.

## 🔴 THE FINDING THIS SESSION

**No band was mis-levelled. Every defect was a defect of CONNECTION — and the fix for one manufactured a false fire on its own first run.**

- **Three states, not two:** **UNINSTRUMENTED** (no instrument) · **UNWIRED** (instrument exists, no pointer) · 🆕 **WIRED BUT NOT MEASURED** (instrument exists, carries the concept and the evidence, **emits no number**).
- ⚠️ **Only the third fails LOUD.** States 1 and 2 report as unscannable and nobody grades them. **A state-3 row wired without a marker reports as `COMPARABLE` and the scan grades PROSE** — `T-06` compared `30 > 30` (the band against a copy of itself) and `T-06b` read a **discount percent as a count of fund gates** and declared it TRIPPED.
- 🔴 **The artifact's §3b had ALREADY warned that careless wiring "manufactures a fire" — and the next edit manufactured one by a mechanism that warning had not anticipated. Being right about the class did not protect against the instance.**
- ⇒ **RUN THE FIX AFTER EACH WIRE, NOT AFTER THE BATCH.** Nothing about the edit looked wrong: pointer correct, referent correct, frozen fields verified untouched, row read fine.

## 🔴 THE STRUCTURAL FINDING — registered 8/27, accepted not fixed

**CREED's LIVE BAND SET IS POINTED AT SYMPTOMS, NOT AT ITS OWN THESIS MECHANISM.** The synthesis says the distress is a **capital-structure / maturity** event; every *live* numeric bar measures a **level** (office DQ, office SS, bank PDNA, VNQ-vs-SPY). The one bar keyed to the maturity mechanism was **`CREED-T-02`, which FIRED and is SPENT**; its successor `VX-CREED-3.05` has **no band until n=12 (~2027-04)**.
⇒ 🔴 **The mechanism CREED believes is driving everything has NO live tripwire, and `T-01a` — the only bar that can realistically fire — confirms a SYMPTOM.**
- **Found via VULCAN's lens** (their state-4: *a band keyed to a different mechanism than the one the channel is evolving through*). ⚠️ **CREED spent the same session writing that defect class up for the fleet and did not check itself against it.** `COVERAGE.md` blind spot **9 of 9; 6 of 9 now other-found.**
- ⛔ **NOT fixed by re-opening the band.** Will ruled n=12 the same day and the n=4 refusal was correct. **The discipline is: REPORT THE DOLLAR LEVEL EVERY PRINT** so the series accrues toward an honest bar. **Report it even if it falls — especially if it falls.**

## 🛠️ WHAT THE GUARDS CANNOT SEE (read before trusting a green)

`creed_selfcheck` was **CLEAN through this entire session** and missed everything above. `threshold_scan` **produced** one of the defects. Neither checks:
- a pointer that resolves to the **wrong** thing, or to a source **not containing** the value (**n=3**),
- **whether a cited instrument actually emits a measurement** (🆕 the state-3 gap),
- **unit commensurability** — `30` vs a `>=1` gate count passes silently; **a wired state-3 row is safe only because a HUMAN marked it,**
- a derived vector whose inputs moved · a stale sentence inside an updated file (check 1 is **file-level**) · a count in a NEW prose phrasing · a shared vector drifting from its owner,
- 🆕 **a SPEC FIELD superseded in another desk's dispatched relay** — `consumer_check.py` scans **values**; a sustain window is not a value. **Found today only because step 1c was run manually and nearly skipped as a no-op.**

## ⚫ STANDING TRAPS — re-read before writing any number

> ⚠️ **Traps 1, 2, 3, 6, 8, 11, 12, 18 are ALSO in `CLAUDE.md` §Standing traps, and THAT copy is the one that matters.** Edit one here, edit it there. **Mapping: SCRATCH 11 → CLAUDE.md 6 · SCRATCH 12 → CLAUDE.md 7 · SCRATCH 18 → CLAUDE.md 8.**

1. **Never cite a CRE mREIT price move without checking corporate actions first** (ARI −33.4% on a total-return-*positive* day).
2. **A real number carrying the WRONG BASIS is the dominant failure mode**, not a fabricated one.
3. **Trepp source tier is MONTH-SCOPED — check `AGENTS/WALTER/sources/` before assuming either way.** Apr–Jul 2026 archived and READ.
4. **Do not fuse ARI→Athene with Delaware Life.**
5. **S5 (multifamily) is HOMER-owned for scoring.** Courier KILLED 8/13; opportunistic only.
6. **Anchor a threshold to a DISTRIBUTION, not the most recent number** — and **BASE-RATE it before shipping.** 🆕 **Ruled into the registry 8/27: base-rating is now keyed to n=12, not a date.**
7. **Check the other side's sourcing before writing a citation rule.**
8. **⚠️ The MBA $775B life-insurer line is WHOLE LOANS ONLY.**
9. **⚠️ Do not let 99.7% be generalized into "the sink absorbs at par."**
10. **A band derived as a % of an unverified quantity silently hard-codes that quantity.**
11. **A SHARE IS NOT A TREND WHEN ITS DENOMINATOR MOVES.** Apply it to other desks' numbers too.
12. **ABSENCE INFERRED FROM RETRIEVAL SHAPE — `n=3`, one document class.** "Not published" usually means "not fetched"; **"not in the table" usually means "it is in the prose."** 🆕 **WIDENED 8/27 — the old wording would not have caught its own third instance**, which said *"no metro detail reachable ⇒ no FL slice exists"* and never used the words "not published." **Name WHICH SHAPE you looked for before writing that a figure is unavailable.**
13. **A METRIC THAT LOOKS LIKE IMPROVEMENT CAN BE THE CONFIRMING EVIDENCE.** The Q2 QBP is the largest instance yet.
14. **READ THE COLUMN HEADERS BEFORE READING A SERIES** — QBP Table V-A emits columns out of order under `pdfminer`. **Anchor on a known cell.** 🆕 **Used again 8/27** on Trepp Table 2: April's `APR-26` column was verified cell-for-cell against May's `APR-26` column before any lodging figure was quoted.
15. **FIX BY PATTERN, NOT BY THE FINDINGS LIST.**
16. **A TWO-POINT DELTA IS NOT A TREND — PRICE THE INSTRUMENT'S NOISE FIRST.** 🆕 **Applied to CORAL's number 8/27, and it changed the read:** the FL hotel's −79bp is **1.10× the mean monthly lodging move**, and Mar→Apr was **also −79bp** with no FL asset named. **The attribution was striking; the magnitude was not.**
17. **A REGISTRY ROW CAN NAME A VECTOR THAT EXISTS AND BE THE WRONG ONE** — or name a SOURCE that exists and does not contain the value. **Follow the pointer and read what is on the other end.**
18. **A PARTIAL REFRESH CERTIFIES THE PART YOU DIDN'T TOUCH — `PAT-117`.** **Re-read the whole unit before closing an edit.**
19. **A CONJUNCTIVE SPEC LETS YOU GRADE ON THE CLEANEST LEG — USE THAT DELIBERATELY.** **Say which leg carries the verdict and why it is immune.**
20. **🆕 A GUARD'S OWN FIX IS UNREVIEWED WORK — RUN IT IMMEDIATELY, PER EDIT.** Both `threshold_scan` v1 (a phantom pointer defect from range shorthand) and the 8/27 wiring fix (a false `TRIPPED`) failed on their FIRST RUN, and both were caught only because the run happened before the commit.

## 🔵 DEFERRED WORK (carried forward)

| # | Item | Why it matters |
|---|---|---|
| 1 | **FOLLOW-THE-POINTER check** — ⚠️ **PARTIAL** | `threshold_scan` resolves every `source_of_truth` vector and reports one that does not exist — the **weakest** limb. It still does NOT verify the pointer names the RIGHT vector (`T-08a`'s defect) or that the cited SOURCE contains the value (`T-03`'s). **2 of 3 instances remain uncaught, and the item now LOOKS closed.** |
| 3 | **BAND-vs-VALUE predicate** | Must **WARN-not-fail** on `4.01` and `9.03`, or it flags two deliberate states every run. |
| 4 | **DERIVED-VECTOR check** (`Last_Updated ≥ max(inputs)`) | `VX-2.03` sat at June while both inputs moved to July. **PROME routed the general form to DAEDALUS — coordinate, don't duplicate.** ⚠️ **`VX-3.05` is now a second derived vector; it inherits this gap.** |
| 5 | **PROMISED-REFERENT check** | A surface naming an artifact that does not exist. |
| 7 | **Evals decontamination — STILL UNOWNED** | Traps name ARI/MBA/Trepp/HOMER verbatim, so the VOID rule kills any session correctly applying its lessons. **PROME's nit stands: NAME AN OWNER or it orphans.** Untouched four sessions. |
| 8 | **Evaluate-and-date the non-scannable triggers** | ⚠️ **PARTIALLY DISCHARGED 8/27** — `T-04`/`T-06`/`T-06b` swept and wired. **`T-05`/`T-07`/`T-08b` still never swept.** |
| 9 | **`VX_HISTORY` staleness coverage** | Exempt fleet-wide by the `EXEMPT_SUBSTR` "history" rule — **no default enforcement.** |
| 10 | **`boot.py`** — zero invocation sites + mtime-keyed checks | Wire it, fix the keying, or retire it with a docstring note. |
| 11 | **Cross-desk register vintage audit** | REGINALD's 8/20 ask. **`REG-T-07` items closed; the rest unaudited.** |
| 12 | **News-sweep leads (8/13)** | ACR cohort-add candidate; CMBS new-issuance YTD scope discrepancy → `research/2026-08-13_NEWS_SWEEP_RESULTS.md` §2. **LIQUID called this the other half of the conduit-takeout hole.** |
| 13 | **`ledger_staleness --nudge` counts an append-only EVENT ledger** | `CREED_T_FIRED_LOG` reads "8 STATUS-writes behind"; one fire exists and it does not move between fires. **Fires forever ⇒ trains the desk to ignore its own nudge.** ⚠️ **Self-inflicted** — CREED's 8/20 `LEDGER_GLOB` fix closed a real gap and created a false-positive generator in the same edit. **Routed to DAEDALUS as a rider 8/27; disposition theirs.** |
| 14 | 🆕 **Registry-ID grep across BOARD after any frozen-field ruling** | A dispatched BOARD relay can carry a superseded SPEC; `consumer_check.py` scans values and cannot see it. **Committed to WALTER 8/27 as a CREED practice regardless of their convention call.** |

## 📬 MAIL STATE

- `inbox/` — **CLEAN.** `inbox/WALTER/` — **CLEAN.** All items read, logged to `board_log.tsv` at READ time, filed to `processed/`.
- ⚠️ **`inbox/WALTER/processed/README.md` — read it before trusting a listing.** Three signals assert REFUTED claims in their own filenames, deliberately NOT renamed — WALTER's canonical BOARD paths.
- **In 8/27:** PROME — **all three band asks RULED APPROVED**, executed same session, logged, filed.
- **Out 8/27 (9 packets):** REGINALD · LIQUID · HOMER · PROME ×3 *(window executed · DOCKET row 33 · band revisit + 3 asks)* · DAEDALUS ×3 *(taxonomy `121024a91` · carry-row `976315d38` · retrieval-shape + axis addendum `e431f938f`/`a37a7e030`)* · **CORAL** *(FL slice cycle 1, `e0e7f859b`)* · **WALTER** *(`SIG-019` stale spec, `b0c222b91`)*.
- ⚠️ **CORAL and WALTER were DARK at commit; rule-6b doorbells went to PROME.** Neither is time-critical — **CORAL's ask is a request NOT to act.**
- ⚠️ **A ruled kill did not reach its counterparty:** HOMER asked 8/22 to re-spec a courier **KILLED 8/13** — encoded on CREED's surfaces, never landed on HOMER's. **Mine to eat; flagged to PROME as possibly a class.**
