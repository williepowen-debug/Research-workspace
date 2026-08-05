# BRENT SCRATCH — Tue Aug 4, 2026 **18:4x ET** (⏰ `date`-verified) · **SESSION 3: GATE v3 · THE CONSOLIDATION PILOT · WILL DECLINED THE DEPLOY · AND MY POSITION LIST WAS WRONG IN BOTH DIRECTIONS**

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ⛔ **THE DEPLOY IS DECLINED. `$0` AT RISK. THE ARM RUNS QUIETLY TO 8/13 — DO NOT RE-PRESENT IT ON DAILY RE-CLEARING.**

---

## ⏳ FIRST THING NEXT SESSION

**1. 🔴 DO *NOT* RE-SURFACE THE DEPLOY PACKET.** Will declined 8/4 eve: *"I am happy enough with the current USO calls we have without adding another one."* **PROME reads it as STANDING, not same-day.** **v3's legs WILL re-clear at the 8/5 open** (8/4 OVX close **53.45**, −22.50% from the 68.97 peak vs the ≤58.6245 line) — **that is NOT new state and does not reach Will.** Escalate ONLY on a peak-re-ratcheting escalation or the frame-breaker carve-out.
   - **What I own:** the **8/13 arm-expiry disposition** (re-arm vs retire) goes to Will then. Nothing before.

**2. 🟠 WED 8/5 10:30 ET — EIA WPSR (wk 7/31).** Pre-registration is **FROZEN** (`setups/2026-08-04_EIA-wk0731-prereg.md`) — **do not write to it before the print; grade in the ADDENDUM only.** The cloud routine fires 11:00 and **records/flags, never grades.**

**3. 🔴 FRI 8/7 — COT as-of 8/4.** Ladder from **101,016**. **Raw `f_disagg.txt`, NOT Socrata. MUST NOT STACK.**

## ★ THE SESSION IN THREE LINES

**Spec:** **DEPLOY GATE v2 was UNFILLABLE BY CONSTRUCTION** — `^OVX` prints to 16:00, USO options close 16:00, so leg (a) became knowable exactly when leg (b) became ungradeable. **Window = ZERO.** v3 ratified; TERRY confirms I *undersold* it (I said 15 min).
**Structure:** Ran RAV's **state-replacement pilot** — threshold homes **3 → 1**, boot phase **9 steps**, `ledger_staleness` **retired**, retirement ratchet adopted.
**Position:** ⛔ **My card was wrong in BOTH directions** — counted a phantom (**STNG, not in the book**), missed two real legs (**USO 135C ×2, XLE 65C ×2**). **Five oil expressions, ~$5,131.** Will declined the add.

## CHANGES SINCE LAST SESSION

- **⛔ WILL DECLINED THE DEPLOY.** Standing. `$0` at risk, arm not consumed, runs to 8/13. **Consistent with my own no-abort-leg warning, which was in front of Will with the packet.**
- **⛔⛔ POSITION TRUTH, BROKER-VERIFIED** (Fidelity + Robinhood, Will-supplied ~15:40, *"this is it"*): **STNG IS NOT IN THE BOOK** — carried 7/21→8/4 across STATUS, TRADE, `CLAUDE.md` scope and **every `N_eff` count I used to argue about size.** **MISSING:** `USO Oct-16 135C ×2` ($910 mkt / $1,421 cost) · `XLE Sep-30 65C ×2` ($98 / $455). ⇒ **5 legs, ~$5,131. I said a new card would be the FOURTH; it would have been the SIXTH.**
- **⛔ THE `125/135 ×1` FALLBACK IS STRUCK — UNEXECUTABLE.** Will is long `Oct-16 135C ×2`, so **selling a 135C closes half an existing long instead of opening a short leg.** ⇒ if Will holds the 12–15% band the answer is **NO TRADE**, not "fall back to the wide." **`125/130 ×2` is unaffected.**
- **📊 8/4 CLOSES:** USO **$115.78** (−5.19%) · Brent **$79.12** (−5.55%) · WTI **$75.41** (−6.14%) · OVX **53.45** (−6.56%) · STNG $76.40 · VIX 16.50 (+4.04%). **Third consecutive down session.**
- **⚠️ UNRECONCILED:** PROME's packet states the 8/4 OVX close as **53.08**; my feed says **53.45**. **FRED `OVXCLS` has not published 8/4, so mine is SINGLE-SOURCE.** Verdict unaffected (both ≪58.62) but it is a conflict on a **gate input** — flagged, not smoothed. **Re-verify against FRED next boot.**

## WHAT I DID

**① GATE v3 — designed, base-rated, ratified, shipped.** Leg (a) → **most recent official close** (a state, known 09:30); **NEW leg (a2)** live non-reversal at the ticket; leg (b) unchanged. **Window 0 min → 6.5 h.** Per #21(b), two paired tightenings (v3 needs **two** independent readings below the line where v2 needed one; clearance expires after one session). Base rate n=4,729 / 113 episodes: fire **68.1%**, entry slippage **−0.04%**, tail **38.2→39.5%**. **Disclosed cost: 31.2% of fire sessions close back above the line.**
**② ⛔ CONVICTED MY OWN 8/2 AUDIT.** It returned *"THE GATE IS SOUND"* off **daily closes** — it modelled v3's cadence, never v2 as written. **I audited statistical merit and never asked whether the gate could be EXECUTED.** → auto-memory `[[finding_executability_is_a_separate_audit_axis]]`.
**③ BUILT `instrument_check.py` + `REGISTRY.tsv`, wired into boot.** Verifies every registered test's instrument **exists / reachable / fresh / still prints while the action market is open**. **Found a defect nobody knew about: TANKER-LIVENESS** is a day-0 close-to-close test that Stage-A requires acting on *on day 0* — same zero-window class.
**④ RAN RAV'S CONSOLIDATION PILOT.** Threshold homes **3 → 1** (`REGISTRY.tsv`; `thresholds.py` tables deleted and read from it, **proven equivalent 21/21 + 10/10 against git HEAD**); THESIS `Status` column removed (14 cells, carrying 7/21–7/30 readings and a gate retired 7/30); boot phase **9 steps**; `ledger_staleness` **de-wired**; **retirement ratchet** adopted. **Coverage went UP: 15 → 46 registered tests.**
**⑤ ⛔ THREE OF MY OWN ERRORS TODAY ALL FAILED IN THE COMFORTING DIRECTION** — a relayed "16:15" that was 16:00; a v1 window check reporting 5 min where the truth was 0; a flat 2× staleness multiplier rendering a **dead falsifier** as advisory. → extended `[[finding_test_the_guard_not_just_the_guarded]]`, n=3.
**⑥ REPOINTED EVERY RUN-TIME CONSUMER OF THE RETIRED GATE** — TRACKER's alert block (**read at run time by the Wed 11:00 routine**), the CATALYSTS 8/13 row (**printed by boot every session**), TRADE's header. **I created that propagation gap myself at ~14:05 and found it by sweep at ~16:00.**

## NEXT SESSION (dated, future-verifiable)

1. 🔴 **Do not re-present the deploy.** Own only the **8/13 expiry disposition.**
2. 🟠 **Wed 8/5 10:30 EIA** — addendum only · **Fri 8/7 COT**, ladder from 101,016, no stacking.
3. 🟠 **Re-verify the 8/4 OVX close against FRED `OVXCLS`** and reconcile 53.45 vs PROME's 53.08.
4. 🟠 **The 5 UNMEASURABLE registered tests need owner decisions, not standing reds** (RAV): PortWatch → **FALCON** (still silent) · EU storage → **GIE key from Will** · **HY energy OAS** and **war-risk** → probably honest **retirement**. *A permanent red is decoration — same disease as the crack line retired 7/31.*
5. 🟠 **`INCIDENTS.tsv` scope ruling** — 5 days stale, 3–4 vessel strikes unlogged; RF-043 already logs an FSRU so the "facility-only" scope contradicts itself. **Decide and add a pointer row either way.**
6. 🟡 **5 predictions are structurally unresolvable** (BRT-07/12/16/17/21) and **invisible to the due-scan by construction** — my SCRATCH has been saying "2 STUCK rows." Register successors FORWARD.
7. 🟡 RAV **QC of the consolidation** is expected — hand it the `--quick`-vs-full warning below.

## OPEN THREADS / WATCHES

- 🔴 **PortWatch `chokepoint6` dead since 7/23 — still BLOCKING the thesis falsifier. FALCON has not answered.**
- 🔴 **n=0 genuine physical reopenings — real-vs-fake UNCALIBRATED.**
- ⚠️ **QC WARNING FOR RAV:** `instrument_check --quick` reports **5** blocking, the full run **7**. `--quick` skips intraday pulls so it **cannot detect `WINDOW_INFEASIBLE`** — the flagship class. **Compare full-to-full.**
- ⚠️ **TERRY's sizing note, adopted:** the $300 tranche was being sized on top of **$4,058 of LINEAR USO shares = 11.6% of the account, no defined risk on the largest leg.** *Sizing the arm without that written down is sizing against the wrong denominator.*
- ⚠️ **TERRY's `MIN($1.50, fire-time worst case)` limit form** — I endorse it; **moot while the decline stands.**
- 🟠 Diesel crack card `NO AT THIS PRICE` · un-anchored *"war-risk halves"* threshold **still open** · Velos Amber vs UKMTO 103-26 **still unreconciled**.
- 🟡 EU storage (**GIE key pending**) · Jazan/product half of the v5.3 retraction **untested** · **46 routine-authored commits unaudited**.

## POSITION DECISIONS PENDING

- **NONE REQUIRING ACTION. `$0` at risk from this arm.** Convex arm **ARMED, NOT deployed, DECLINED**; expires **8/13**.
- **★ THE REAL RISK IS UNCHANGED AND UNDEFENDED: USO 35 shares ≈ $4,058 = 11.6% of the account, linear, no defined risk.** **Not a trim recommendation** (root rule #7 — thesis intact), but it is where the exposure actually sits, not in the $300 card we spent the day on.
- **USO Oct-16 135C ×2** — **HELD**, −36.0%. **USO Sep-18 150/165** — HOLD, ~29% OTM at 45 DTE, effectively a lapse. **XLE Sep-30 65C ×2** — **LAPSE**, −78.5%.

## MAIL STATE

- **INBOX: 1** — `MSG-PROME-20260803-003` (2 obligations, **ACCEPTED, due 8/13**, correctly retained). **`-002` archived: all 3 obligations terminal since 8/3.**
- **⚠️ Boot-report correction on the record:** I told Will *"5 DM obligations, zero receipts, disposition never filed."* **Wrong.** `validate.py` counts receipts only among the files passed to it, and I passed only `inbox/MSG-*.md`. **Both receipts exist and are thorough.** The real defect was **archival, not disposition.**
- **SENT (2):** → TERRY (v3 + the 16:00 correction) · → PROME (`PROME/inbox/` — v3 + the self-implicating audit finding).
- **Outbox:** limit-ruling **swept to `delivered/`** (TERRY replied). **2 remain** — the 7/31 boot/closeout audits, pending a round-2 batch.
- **Owed TO me:** **FALCON on PortWatch** (blocking) · **Will: GIE key**, the war-risk-halves ruling, **8/13 disposition**.

## WORKBOOK HEALTH

- **LIVE:** `TRADE.md` (**GATE v3 · positions CORRECTED both directions · fallback STRUCK**) · STATUS (**244 lines**, current-state block at top) · **`workbook/REGISTRY.tsv` (NEW — the single threshold/test home, 46 rows)** · THESIS v5.4 (**Status column removed**) · TRACKER · SCHEDULED_RUNS · EIA pre-reg (frozen) · board_log (**138**) · SCRATCH · NEXUS_BRIEF (**109 lines, back inside cap**).
- **RETIRED/REMOVED:** `workbook/INSTRUMENTS.tsv` (absorbed) · `ledger_staleness` (de-wired from BRENT boot) · `thresholds.py` hardcoded tables.
- **Boot 46.2s, 6 checks, `FINDINGS`≠`FAIL` now distinguished.** Lesson-conflict **0** · prose/index drift **0** · predictions-due clean · memory-index **0 blocking**.
- **⛔ 7 BLOCKING instrument rows** — 2 window-infeasible (GATE-V3-A2, TANKER-LIVENESS), 1 stale (PortWatch), 4 no-instrument (AIS, HY energy OAS, war-risk, EU storage).
- **GIT:** 6 commits, path-scoped, all pushed. **2 auto-memories committed** (1 new, 1 extended) per carve-out ③, `memory_index_check --slug` exit 0.
