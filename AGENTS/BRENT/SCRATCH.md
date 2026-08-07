# BRENT SCRATCH — Wed Aug 5, 2026 **~19:5x ET** *(stamp corrected 8/6 Will-directed review: this closeout committed 19:59 ET and describes daytime work — the "~03:0x ⏰ date-verified" stamp was carried forward from the overnight RAV-pilot closeout. Numbering note: that overnight session self-labels **session 4** in its own artifacts but its closeout also claimed "session 5" — the RAV pilot = session 4, THIS is session 5)* · **SESSION 5: THE STRUCTURE SESSION — TWO UNEXECUTABLE GATES FIXED, AND THE DOC THAT WAS SUPPOSED TO SHRINK HAD BEEN GROWING**

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ⛔ **NO MARKET DATA AFTER THE 8/4 CLOSE. NO THESIS CHANGE. NO POSITION CHANGE. `$0` MOVED.**
> **Every tape figure in STATUS/NEXUS_BRIEF is an 8/4 close — re-pull at boot (LESSONS #5).**

---

## ⏳ FIRST THING NEXT SESSION

**1. 🟠 TODAY, WED 8/5 10:30 ET — EIA WPSR (wk 7/31).** Pre-registration **FROZEN** (`setups/2026-08-04_EIA-wk0731-prereg.md`) — **do not write to it before the print; grade in the ADDENDUM only.** ⚠️ **The cloud routine already ran ~11:31 and CORRECTLY graded nothing** — all sources still capped at wk-7/24 because the print had not happened. **That is a non-event, not a miss.**

**2. 🔴 DO *NOT* RE-SURFACE THE DEPLOY.** Will declined 8/4 eve, **STANDING**. v3's legs re-clearing is **not new state**. What I own is the **8/13 arm-expiry disposition**.

**3. 🔴 FRI 8/7 — COT as-of 8/4.** Ladder from **101,016**. **Raw `f_disagg.txt`, NOT Socrata. MUST NOT STACK.**

## ★ THE SESSION IN FOUR LINES

**Reconciled** the shipped RAV pilot against RAV's own plan → found **two stale ownership pointers** it left behind and that its headline metric measured **enrollment, not consolidation**.
**Fixed two gates that could not be executed** — `GATE-V3-A2` (my own check's false red) and **Stage-A Leg T** (real, Will-ruled → v6). **Blocking 7 → 5; zero window-infeasible rows remain.**
**Measured the thing nobody had measured:** the pilot whose goal was *"flatten boot"* had left `CLAUDE.md` **bigger**. ⇒ **split the operating docs from [`RULINGS.md`](RULINGS.md)**, and **folded v2 into v3** so the live gate is one spec, not a delta.
**Hot context 317 KB → 300 KB. Nothing deleted — moved out of boot context.**

## CHANGES SINCE LAST SESSION

- **✅ OVX 8/4 CLOSE CONFIRMED TWO-WITNESS: FRED `OVXCLS` published 53.45** — exactly my figure. **PROME's 53.08 was the open/high of the 15:30 5m bar**, i.e. an intraday print quoted as a close. **Conflict RESOLVED, not smoothed.**
- **✅ STAGE-A LEG T v6 — WILL-RULED.** v5 graded day-0 **close-to-close** while sizing fires **tranche 1 on day 0** ⇒ **zero-minute window**, the DEPLOY GATE v2 defect in a second ratified gate. **Now: prior close → live print, graded ONCE at/after 14:00 ET. Window 120 min.** Threshold 1.0%, composite and sign-discarding **unchanged**.
- **✅ DEPLOY GATE v2 FOLDED INTO v3.** The live gate was written as a *delta* on v2 — reading it meant applying a patch mentally. **Now one self-contained block, 73 → 40 lines.**
- **✅ OPERATING DOCS SPLIT FROM THE RECORD.** `CLAUDE.md` 252 → 237 ln, **38.9 → 30.2 KB (−22%, below the pre-pilot baseline for the first time)**. `TRADE.md` 688 → 651 ln.
- **⚠️ INFRA, from my own cloud routine:** it found a **stale local master in detached HEAD, 50-commit divergence from origin with NO common ancestor**, and repointed it. No data lost, flagged to PROME. **Worth knowing — that state silently makes an agent work against a phantom repo.**

## WHAT I DID

**① RECONCILED THE SHIPPED PILOT AGAINST RAV'S PLAN** (WP-by-WP; WP0 had never been done → wrote `workbook/PILOT_STATE_REPLACEMENT_MEASUREMENT.md` from git, not memory).
**② ⛔ FOUND RAV'S RISK #1 REALIZED — IN THE OWNERSHIP *CLAIMS*, NOT THE DATA.** `CLAUDE.md` and `thresholds.py` both still named THESIS canonical 4 days after the pilot moved the machine home. **Both were CORRECT WHEN WRITTEN** (F3, 7/31) — **F3 fixed the question once, the pilot moved the answer, nothing re-asked it. A stale pointer with a citation defends itself.** → `[[finding_ownership_claim_is_last_to_move]]`
**③ ⛔ MY OWN HEADLINE METRIC MEASURED THE FLATTERING THING** — *"coverage 15 → 46"* counted **enrollment**, not migration. **10 of 47 rows have no machine-readable level**; **`eia_weekly.py` is a FOURTH threshold home the pilot never touched** (2 hardcodes fired red at boot; refinery util has **no registry row at all**).
**④ FIXED THE `GATE-V3-A2` FALSE RED** — added a **reading basis** (`:final` / `:any` / `:atHHMM`) to `window_req`; bare = `:final`, **fail-safe**, so the loosening must be declared per row. **Falsified 7/7** — the ORIGINAL v2 defect still fires, so the check was **not** weakened.
**⑤ LEG T v6 — and the OBVIOUS fix was REFUTED before I proposed it.** A naive live-at-the-ticket `T` **BLOCKS Jun-17, the one analogue that made money, at 4 of 6 morning checks.** ★ **`T` is a MAGNITUDE THAT GROWS THROUGH THE SESSION ⇒ a full-session threshold is systematically too high at any partial-session moment — a UNITS MISMATCH, not a level to re-tune.** **66.1% of sessions flip the verdict intraday** ⇒ tightening **T1 (one grade only)** is forced by data, not caution; **T2** keeps the close basis binding on tranche 2.
**⑥ MEASURED THE ACCUMULATION AND SPLIT THE DOCS.** ★ **The retirement ratchet governs STATE and says nothing about PROSE** — so specs get replaced while the prose *about* each replacement accumulates. → `[[finding_anti_ratchet_governs_state_not_prose]]`
**⑦ NOTIFIED THE OWNERS:** TERRY (Leg T v6 changes its ticket rail; T1 binds it at the moment of grading) · PROME (proposal of record, marked RULED).

## NEXT SESSION (dated, future-verifiable)

1. 🟠 **Wed 8/5 10:30 EIA** — addendum only · **Fri 8/7 COT**, ladder 101,016, no stacking.
2. 🟠 **Retire the 3 unmeasurable rows that are MINE** — `STAGE-A-AIS` (no instrument, never existed) · `HY-ENERGY-OAS` (no free feed, fleet-wide dark) · `WAR-RISK-HALVES` (no feed AND no anchor). **Blocking 5 → 2.** *A permanent red is decoration.* **PortWatch (FALCON) and EU storage (Will's GIE key) are the only two genuinely pending someone else.**
3. 🟠 **Close the WP3 residual (Will's call, put to him 8/5):** either make `eia_weekly.py` a registry consumer and move the 6 orphaned levels in, **or narrow the registry header's "EVERY registered test" claim** to what actually shipped. **Doing neither leaves an over-claiming single-source-of-truth banner.**
4. 🟡 **`TRADE.md` still has interleaved dated blocks** (the 8/3 disclosure instance, the resolved behavioral test at ~342). **They need HEADINGS introduced before extraction is safe** — live plan content resumes mid-block with no boundary. Smaller job now the gate is clean.
5. 🟡 **NEXUS_BRIEF VIEW + CALIBRATION still stale** (`VIX 19.7` / `OVX 70.27` vs 8/4's 16.50 / 53.45) — **content pass owed; compression rides with it, not before it.**
6. 🟠 **`INCIDENTS.tsv` scope ruling** — 6 days stale, 3–4 vessel strikes unlogged; RF-043 logs an FSRU under a "facility-only" scope that therefore contradicts itself.
7. 🟡 **5 predictions structurally unresolvable** (BRT-07/12/16/17/21), invisible to the due-scan by construction. Register successors FORWARD.
8. 🟡 **SPR "floor" candidate:** **252.4M** (THESIS, §6241 statutory) vs **400.0** (`eia_weekly.py`, "near operational floor"). **147.6M under one word.** May be two legitimate objects — **read the rationale, do not find-and-replace.**

## OPEN THREADS / WATCHES

- 🔴 **PortWatch `chokepoint6` dead since 7/23 (13d) — still BLOCKING the thesis falsifier. FALCON has not answered.**
- 🔴 **n=0 genuine physical reopenings — real-vs-fake UNCALIBRATED.** Every Stage-A number is fitted to a sample containing **no instance of the event the playbook exists to trade.**
- ⚠️ **QC WARNING FOR RAV:** `instrument_check --quick` **cannot detect `WINDOW_INFEASIBLE`** (it skips intraday pulls) — the flagship class. **Compare full-to-full, never quick-to-full.**
- ⚠️ **Leg T v6 limits that must travel:** n=1 analogue intraday (**Apr-17 cannot be re-run**, 5m history starts 5/11) · **14:00 is NOT empirically better than 15:00** (2 vs 5 sessions at n=59) · every intraday grading time carries a **3–9% false-pass**.
- ⚠️ **TERRY's sizing note:** any future tranche sizes on top of **$4,058 of LINEAR USO = 11.6% of the account, no defined risk on the largest leg.**
- 🟠 Diesel crack card `NO AT THIS PRICE` · Velos Amber vs UKMTO 103-26 **still unreconciled** · **46 routine-authored commits unaudited**.

## POSITION DECISIONS PENDING

- **NONE REQUIRING ACTION. `$0` at risk from this arm.** Convex arm **ARMED, NOT deployed, DECLINED (standing)**; expires **8/13**.
- **★ THE REAL RISK IS UNCHANGED AND UNDEFENDED: USO 35 shares ≈ $4,058 = 11.6% of the account, linear, no defined risk.** Not a trim recommendation (root rule #7 — thesis intact), but that is where the exposure actually sits.
- **5 live oil expressions, ~$5,131** `[broker-verified 8/4]`. **USO Oct-16 135C ×2** HELD −36.0% · **USO Sep-18 150/165** HOLD (~29% OTM, effectively a lapse) · **XLE Sep-30 65C ×2** LAPSE −78.5%. ⛔ **STNG is a TRACKED TICKER, not a holding.**

## MAIL STATE

- **INBOX: 1** — `MSG-PROME-20260803-003` (2 obligations, **ACCEPTED, due 8/13**, correctly retained, not consumed this session).
- **SENT (3):** → PROME (Leg T proposal, **marked RULED**, swept to `outbox/delivered/`) · → TERRY (Leg T v6 execution rail) · PROME inbox copy annotated RULED.
- **Outbox: 2** — the 7/31 boot/closeout audits, loops **not** demonstrably closed (pending PROME round-2) ⇒ correctly left top-level.
- **Owed TO me:** **FALCON on PortWatch** (blocking) · **Will: GIE key**, the war-risk-halves ruling, the WP3 call, **8/13 disposition**.

## WORKBOOK HEALTH

- **LIVE:** `TRADE.md` (**651 ln** — GATE v3 self-contained, Leg T v6, positions correct) · STATUS (**246 ln**, inside the 250 cap) · **`RULINGS.md` (NEW, 152 ln — the dated record, NOT boot-read)** · `workbook/REGISTRY.tsv` (47 rows; ⚠️ **10 with no machine-readable level**) · `PILOT_STATE_REPLACEMENT_MEASUREMENT.md` · THESIS v5.4 · TRACKER · board_log · SCRATCH.
- ⚠️ **`NEXUS_BRIEF.md` over its 100-ln cap** — deliberately not compressed; the schema compresses upward from VIEW, which is the section flagged as needing re-verification. **Compression rides with the content pass.**
- **HOT CONTEXT: 317 KB → 300 KB.** `CLAUDE.md` **38.9 → 30.2 KB**; BOOT section 43 → 31 ln, rationale 18 → 7, **human actions unchanged at 9**.
- **Boot 58.1s, 6 checks.** Lesson-conflict **0** · prose/index drift **0** · predictions-due clean · **Instrument Check FINDINGS, 5 blocking (was 7) — every red removed was a FALSE one.**
- **GIT:** 6 commits this session, path-scoped, all pushed (one routine rebase, verified by subject + against origin). **2 auto-memories created** (carve-out ③, self-committed).
