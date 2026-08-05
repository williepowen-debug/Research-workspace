# BRENT SCRATCH — Wed Aug 5, 2026 **~00:3x ET** (⏰ `date`-verified) · **SESSION 5: THE RAV PILOT RECONCILIATION — THE CONSOLIDATION SHIPPED AND LEFT ITS OWN POINTERS BEHIND**

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ⛔ **NO MARKET DATA WAS PULLED AFTER THE 8/4 CLOSE. NO THESIS CHANGE. NO POSITION CHANGE. `$0` MOVED.**
> **This was an INFRASTRUCTURE session. Every tape figure in STATUS/NEXUS_BRIEF is an 8/4 close — re-pull at boot (LESSONS #5).**

---

## ⏳ FIRST THING NEXT SESSION

**1. 🟠 WED 8/5 10:30 ET — EIA WPSR (wk 7/31).** Pre-registration is **FROZEN** (`setups/2026-08-04_EIA-wk0731-prereg.md`) — **do not write to it before the print; grade in the ADDENDUM only.** The cloud routine fires 11:00 and **records/flags, never grades.**

**2. 🔴 DO *NOT* RE-SURFACE THE DEPLOY.** Will declined 8/4 eve, **STANDING**: *"I am happy enough with the current USO calls we have without adding another one."* v3's legs **will** re-clear at the open — **that is not new state and does not reach Will.** What I own is the **8/13 arm-expiry disposition** (re-arm vs retire). Nothing before.

**3. 🟠 RE-VERIFY THE 8/4 OVX CLOSE (53.45) AGAINST FRED `OVXCLS`.** It had **not** published 8/4 as of 22:32 ET (latest row 8/3 @ 57.20) ⇒ **still single-witness on value.** *(The PROME conflict itself is RESOLVED — see below.)*

**4. 🔴 FRI 8/7 — COT as-of 8/4.** Ladder from **101,016**. **Raw `f_disagg.txt`, NOT Socrata. MUST NOT STACK.**

## ★ THE SESSION IN THREE LINES

**Ran:** Will handed me RAV's `brent-state-replacement-pilot-plan.txt` — the plan for the consolidation I had **already executed** in session 3. So I reconciled **the shipped branch against the plan**, WP by WP, rather than against my own memory of it.
**Found:** the pilot delivered WP1–WP6 — **and left two of its own ownership pointers stale**, plus a headline metric that measured the flattering thing. **Both pointers fixed; the metric restated honestly.**
**Wrote:** the **WP0 baseline artifact that never existed** — RAV's WP7 QC had no auditable answer to *"did duplicate live threshold homes decrease?"* because the before/after numbers lived only in **this file**, which is rewritten every session.

## CHANGES SINCE LAST SESSION

- **✅ THE OVX CONFLICT IS RESOLVED, AND IT IS THE INTRADAY-AS-CLOSE CLASS AGAIN.** PROME's **53.08** is the **open/high of the 15:30 5m bar**; the daily close is **53.45**. Mechanically diagnosable — same class as WALTER's WTI $86.80 (8/2) and three of my own this week. **Not a feed disagreement.** Gate verdict unaffected throughout (both ≪ 58.6245).
- **⛔ TWO STALE OWNERSHIP POINTERS — MINE, SHIPPED 8/4, FIXED 8/5.** `CLAUDE.md:216` and `thresholds.py:7` **both still declared `thesis/THESIS.md` the canonical threshold registry**, four days after the pilot moved the machine home to `REGISTRY.tsv`. `thresholds.py` carried **two contradictory ownership declarations in one file** (docstring vs L78) and pointed readers at *"the tables below"* that the same commit had **deleted**.
- **📉 NO NEW TAPE.** Last prints are 8/4 closes: USO **$115.78** · Brent **$79.12** · WTI **$75.41** · OVX **53.45** · VIX **16.50**. Overnight 8/4 22:35: Brent **$78.79** (−0.72%), WTI **$74.95** — still leaking, third-consecutive-down-session picture intact.
- **🔴 BOOT FINDINGS UNCHANGED:** 7 blocking instrument rows · Cushing **18.60M** (below the 20.0M floor, Path-B breached) · refinery util **97.2%** · gasoline demand **−0.25% YoY**.

## WHAT I DID

**① RECONCILED THE SHIPPED PILOT AGAINST RAV'S PLAN.** WP1 ✅ (location deviates — `workbook/REGISTRY.tsv`, not `registry/TESTS.tsv`; deliberate, the retirement ratchet applied to itself, **declared** so QC finds it) · WP2 ✅ · WP3 🟡 partial · WP4 ✅ (9 human boot actions, inside RAV's 7–9) · WP5 ✅ · WP6 ✅ · **WP0 ⛔ was never done** · WP7 is RAV's.
**② ⛔ FOUND AND FIXED RAV'S RISK #1, REALIZED — IN THE OWNERSHIP *CLAIMS*, NOT THE DATA.** Both pointers were **CORRECT WHEN WRITTEN** — ratified by the **F3 ruling of 7/31, whose entire subject was ownership** (*"one table, one home, boot reads the pointer"*). **F3 fixed the question once; the pilot moved the answer; nothing re-asked it.** ★ **A stale pointer with a citation defends itself** — reviewing it surfaces the ruling saying it is right. **No check caught either:** `lessons_check`, `instrument_check` and the prose/index drift check all probe **levels and instruments**; **nothing probes "does this file name the right owner."**
**③ ⛔ MY OWN HEADLINE METRIC MEASURED THE FLATTERING THING.** I reported *"coverage 15 → 46 registered tests."* That counts **enrollment in the registry, not migration of the level into it.** **10 of 47 rows carry no machine-readable level**; 6 of those have a working instrument and their level simply **never moved**. **And `eia_weekly.py` is a FOURTH threshold home the pilot never touched** — `CUSHING_MIN = 20.0` and `UTIL_SQUEEZE = 95.0` **both fired red at this boot**, and refinery util has **no registry row at all**. **Honest restatement: 3 homes → 1 for the rows `thresholds.py` already owned; unchanged for EIA-, gate-, falsifier- and prediction-sourced rows.**
**④ WROTE `workbook/PILOT_STATE_REPLACEMENT_MEASUREMENT.md`** (108 ln) — WP0 baseline **reconstructed from git** (pre-pilot `fbd3c100f`), not memory. Carries the findings **against** the pilot and the two QC warnings for RAV.
**⑤ ⛔ C6 CAUGHT A SECOND LIVE ONE IN `NEXUS_BRIEF`, AND IT WAS A PARTIAL FIX DESCRIBED AS DONE.** The **NEXT DECISION POINT** block was still publishing **DEPLOY GATE v2 as the governing rule** — one day after v3 superseded it, and one day after that file's own header recorded C6 catching *exactly this defect* in the **gate block**. **The gate block was rewritten 8/4; this block was not.** ✅ Rewritten to v3 + the DECLINED action-state.
**⑥ AUTO-MEMORY:** created `[[finding_ownership_claim_is_last_to_move]]` (dedup-checked against `dead_path_regrows` and `governance_doc_stale_default_drift` — **neither covers it**; those are about dead PATHS and stale DEFAULTS, this is a moved OWNER).

## NEXT SESSION (dated, future-verifiable)

1. 🟠 **Wed 8/5 10:30 EIA** — addendum only · **Fri 8/7 COT**, ladder from 101,016, no stacking.
2. 🟠 **Re-verify 8/4 OVX 53.45 against FRED `OVXCLS`** (had not published as of 8/4 22:32).
3. 🔴 **FIX THE `GATE-V3-A2` FALSE RED — it is on the gate I just ratified.** `instrument_check` flags it `WINDOW_INFEASIBLE` off *"last print 16:00 ≥ USO close 16:00."* **That is the right test for a CLOSE-basis leg; a2 is an EXISTENCE-form live print (`same_session_action`) satisfiable any time from 09:30 ⇒ real window ~6.5h, not 0.** The check has **no column distinguishing *"needs the FINAL value"* from *"needs SOME qualifying value."*** ⚠️ **`TANKER-LIVENESS` is a GENUINE red** — it truly is day-0 close-to-close. **Fix the check, do not soften the finding.**
4. 🟠 **Decide the WP3 residual (Will/RAV):** move the 6 orphaned levels into `REGISTRY.tsv` and make `eia_weekly.py` a registry consumer — or **narrow the registry header's "EVERY registered test" claim** to what actually shipped. **Doing neither leaves an over-claiming single-source-of-truth banner.**
5. 🟠 **The 5 UNMEASURABLE registered tests need owner decisions, not standing reds:** PortWatch → **FALCON** (still silent, **12d stale**, blocking the thesis falsifier) · EU storage → **GIE key from Will** · **HY energy OAS** and **war-risk** → probably honest **retirement**. *A permanent red is decoration — same disease as the crack line retired 7/31.*
6. 🟠 **`INCIDENTS.tsv` scope ruling** — now 6 days stale, 3–4 vessel strikes unlogged; RF-043 already logs an FSRU so the "facility-only" scope contradicts itself. **Decide and add a pointer row either way.**
7. 🟡 **NEXUS_BRIEF VIEW + CALIBRATION are stale and flagged** (`VIX 19.7` / `OVX 70.27` vs 8/4's 16.50 / 53.45). **Content pass owed.**
8. 🟡 **5 predictions are structurally unresolvable** (BRT-07/12/16/17/21) and **invisible to the due-scan by construction.** Register successors FORWARD.
9. 🟡 **Candidate, needs a rationale read before anyone touches it:** SPR *"floor"* = **252.4M** in THESIS (§6241 statutory) vs **400.0** in `eia_weekly.py` (*"near operational floor"*). **147.6M under one word.** May be two legitimately different objects — **do not find-and-replace** (`[[finding_deliberate_and_unnoticed_asymmetry_look_identical]]`).

## OPEN THREADS / WATCHES

- 🔴 **PortWatch `chokepoint6` dead since 7/23 — still BLOCKING the thesis falsifier. FALCON has not answered.**
- 🔴 **n=0 genuine physical reopenings — real-vs-fake UNCALIBRATED.**
- ⚠️ **QC WARNING FOR RAV, carried:** `instrument_check --quick` reports **5** blocking, the full run **7**. `--quick` skips intraday pulls so it **cannot detect `WINDOW_INFEASIBLE`** — the flagship class. **Compare full-to-full.**
- ⚠️ **TERRY's sizing note, adopted:** any future tranche sizes on top of **$4,058 of LINEAR USO shares = 11.6% of the account, no defined risk on the largest leg.**
- 🟠 Diesel crack card `NO AT THIS PRICE` · un-anchored *"war-risk halves"* threshold **still open** · Velos Amber vs UKMTO 103-26 **still unreconciled**.
- 🟡 EU storage (**GIE key pending**) · Jazan/product half of the v5.3 retraction **untested** · **46 routine-authored commits unaudited**.

## POSITION DECISIONS PENDING

- **NONE REQUIRING ACTION. `$0` at risk from this arm.** Convex arm **ARMED, NOT deployed, DECLINED (standing)**; expires **8/13**.
- **★ THE REAL RISK IS UNCHANGED AND UNDEFENDED: USO 35 shares ≈ $4,058 = 11.6% of the account, linear, no defined risk.** **Not a trim recommendation** (root rule #7 — thesis intact), but it is where the exposure actually sits.
- **5 live oil expressions, ~$5,131** `[broker-verified 8/4]`. **USO Oct-16 135C ×2** — HELD, −36.0%. **USO Sep-18 150/165** — HOLD, ~29% OTM at 45 DTE, effectively a lapse. **XLE Sep-30 65C ×2** — LAPSE, −78.5%. ⛔ **STNG is a TRACKED TICKER, not a holding.**

## MAIL STATE

- **INBOX: 1** — `MSG-PROME-20260803-003` (2 obligations, **ACCEPTED, due 8/13**, correctly retained — **not consumed this session**, no ledger row owed).
- **Outbox: 2** — the 7/31 boot/closeout audits, **loops NOT demonstrably closed** (pending PROME's round-2 batch) ⇒ correctly left top-level, not swept to `delivered/`.
- **Owed TO me:** **FALCON on PortWatch** (blocking) · **Will: GIE key**, the war-risk-halves ruling, **8/13 disposition**.
- **Owed BY me:** nothing routed this session. ⚠️ **Consider a packet to PROME on the intraday-as-close OVX finding** — it is PROME's figure and the class has now bitten three agents in four days.

## WORKBOOK HEALTH

- **LIVE:** `TRADE.md` (GATE v3 · positions corrected · fallback STRUCK) · STATUS (**245 ln**, inside the 250 cap, current-state block at top) · **`workbook/REGISTRY.tsv` (47 rows — ⚠️ 10 with no machine-readable level)** · **`workbook/PILOT_STATE_REPLACEMENT_MEASUREMENT.md` (NEW, 108 ln)** · THESIS v5.4 · TRACKER · SCHEDULED_RUNS · EIA pre-reg (frozen) · board_log (138) · SCRATCH.
- ⚠️ **`NEXUS_BRIEF.md` = 122 ln, OVER its provisional 100-line cap** (it was already 120 at session start — the 8/4 handoff's *"109 ln, back inside cap"* was wrong). **Not compressed this session ON PURPOSE:** the schema says compress upward from **VIEW / FORWARD CATALYSTS**, and VIEW is exactly the section I just flagged as **stale and owed a content re-verify** — compressing an unverified section would bake the staleness in rather than fix it. **Compression rides with the content pass (NEXT SESSION #7), not before it.**
- **RETIRED/REMOVED:** `workbook/INSTRUMENTS.tsv` (absorbed) · `ledger_staleness` (de-wired) · `thresholds.py` hardcoded tables.
- **Boot 142.5s, 6 checks.** Lesson-conflict **0** · predictions-due **clean** · **Instrument Check = FINDINGS (7 blocking)**.
- **GIT:** 2 commits this session, path-scoped, pushed. **1 auto-memory created** (carve-out ③, self-committed).
