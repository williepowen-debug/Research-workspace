# BRENT SCRATCH — Fri Aug 21, 2026 **12:53 ET** *(live session #3 CLOSED by Will for a fresh context layer ahead of the prints · boot 11:12 → FILE AUDIT → fix-all → boot-load analysis → close)*

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴🔴🔴 **YOU WERE REBOOTED FOR EXACTLY ONE REASON: TAKE THE TWO GRADES. DO THAT FIRST, BEFORE ANY OTHER WORK ON THIS PAGE.**
>
> **This session closed at 12:53 ET — SIX MINUTES before the Baker Hughes print. Will closed it deliberately to give you a clean context layer for the grades. Nothing else here outranks them.**
>
> | Series | Prints | Almost certainly ALREADY PRINTED when you boot |
> |---|---|---|
> | **Baker Hughes** (`BRT-26`) | **~13:00 ET** | **`455` oil rigs (wk-8/14) is 2 FROM THE FROZEN `457` LINE.** Window closes **9/30**. |
> | **CFTC COT** as-of **Tue 8/18** | **~15:30 ET** | **Vintage #2 — FIRST grade of the `COT-FUEL-35B` successor on a clean vintage.** TERRY + two desks staged. |
>
> ⛔ **DO NOT LET THEM STACK.** Next prints are **Fri 8/28**. Two prints on one series destroys the WoW deltas the ladder is defined on. **Repair window: today → 8/28 13:00.** A Monday 8/24 session can still take both cleanly (3 days old ≠ stacked).
> ⚠️ **IF TAKEN LATE, SAY SO ON THE GRADE.** A late grade is valid; one that hides its latency is not.
>
> ### ✅ BAKER HUGHES — GRADE PLAN (the instrument claim was CORRECTED 8/21; use this, not older text)
> **The primary is NOT unreachable** — `rigcount.bakerhughes.com/rig-count-overview` returns **HTTP 200 in 0.36s** to a labelled table (`U.S. | 14 Aug 2026 | 593 | +5 | …`). **THE REAL CONSTRAINT IS COVERAGE: it publishes the TOTAL ONLY, and `BRT-26` grades the OIL count.** The split is in **no** BH page's static HTML. **Total is NOT a proxy — 8/14: total `+5`, oil `+1`.**
> ⇒ **Anchor the CAPTURE at the primary (its companion TOTAL reproduces to the unit), take the OIL leg from an aggregator, and SAY WHICH LEG IS WHICH on the grade.** The oil leg is **single-sourced by construction** — a property of what BH publishes, not of anyone's diligence.
> ⛔ **NEVER a bare digit-regex on BH HTML — it returns `457`, my own frozen line, out of CSS/UUID fragments.** ⛔ **Do NOT infer the oil split from the total.**
>
> ### ✅ COT — GRADE PLAN
> `cot_grade.py --expect 2026-08-18`. **Leg A** deadband **109,165–118,325** (bar 113,745) · **Leg B** OI-share ≤ **4.909%**, **GATING**. Raw `f_disagg.txt` code **067651**, **NOT Socrata** (`[[finding_cftc_cot_raw_file_beats_socrata_lag]]`). **Verify `report_date` IN-ROW.** **exit 3 = WAIT, do not grade.** `median_unit 9,160` **FROZEN** — re-basing is a NEW N1 build + fresh Will ruling. ⛔ **Incumbent `COT-FUEL` is RETIRED — do not re-grade it.** Last read (8/11 vintage): Leg A `110,638` INSIDE deadband ⇒ NO-VERDICT; Leg B `5.8463%` ⇒ NOT-SPENT.
> ⚠️ **`$?` through a pipe lies — check the script's rc directly.** (Bit me twice on 8/21.)

---

## ⏸️ STAGED AND FULLY PREPPED, NOT EXECUTED — THE BOOT-LOAD CUT

**Will asked me to look at what BRENT loads at boot. I measured it, proposed a fix, and asked his word. He closed the session for the grades instead — so this is READY TO RUN, nothing done.** DAEDALUS reviewed at Will's request (`eea9460ff`): **CONCUR on the diagnosis and all 4 steps, do-now over hold.** ⛔ **That is a REVIEWER'S REC, NOT WILL'S WORD — I gated it by asking him** `[[finding_relayed_recommendation_is_not_an_approval]]`. **Get his word before cutting.**

**THE MEASUREMENT:** boot loads **~525 KB ≈ 135,000 tokens** every session. `STATUS.md` **202 KB / ~52k tok** + `TRADE.md` **159 KB / ~41k tok** = **69% of it.**
**THE DEFECT:** the `STATUS.md` cap is **250 LINES**; STATUS is at **246 = 98% "compliant"** — and **843 bytes per line** (line 90 alone is **17,887 B ≈ 4.5k tokens**). **No byte cap exists; nothing enforces even the line cap** (prose in `CLAUDE.md` twice, no script measures bytes anywhere in the kit). **66% of STATUS bytes is dated history the file itself declares as history at line 7.**
★ **THE SHARPENING (mine, DAEDALUS is extending PAT-086 with it): 19 `STATUS_archive_*` files exist — the archiving ritual IS being performed at every closeout. Archiving by LINE COUNT does not reduce BYTES when retained lines are 17 KB each. Compliance looks like the fix, so the growth is invisible.**
**Fleet precedent: this exact class was found + fixed on `MEMORY.md` 2026-08-03 with a `soft_bytes` tier. BRENT's cap never got the byte tier.**

### PRE-CUT PREP — ALREADY DONE, DO NOT REDO
- ✅ **BREAKAGE MAPPED (DAEDALUS's addition 1, the one my plan missed):** cutting lines 36–200 dangles every `STATUS:N` anchor below the cut. **4 LIVE files, 8 anchors, must be re-pointed FIRST:** `AUDIT_2026-08-12_self-audit-canonical-surfaces.md` (2) · `STATUS.md` self-ref (1) · `board_log.tsv` (3) · `workbook/PILOT_STATE_REPLACEMENT_MEASUREMENT.md` (2). **5 point-in-time mail files may dangle — acceptable.** ⛔ **3 external citers are DAEDALUS surfaces (FLEET_MAP, BRENT_CARD, BATCH_03) — IT owns re-pointing them, do NOT touch.** Re-point to the archive file **or** convert to section-name anchors (survive line shifts).
- ✅ **ADDITION 5b CLEARS:** grepped `SCHEDULED_RUNS.md` — **NO cloud routine reads `TRADE.md`.** The routines parse `TRACKER.md`'s top block only ⇒ the PAT-069 format-consumer risk does **not** apply to the TRADE restructure. *(Worth checking precisely because the TRACKER `📟` block proves a line-move in a machine-read file IS a breaking change.)*
- ✅ **CONSTRAINTS ADOPTED:** byte tier declared from density measured **AFTER** the archive (blueprint §8) — **NOT** the 25,600 fleet default (my own inherited-default finding) and **NOT** today's 843 B/line bloat · **archive and guard = TWO commits**, guard watched firing **both** directions (my own 09:41 lesson: adding the PATH and adding the ALERT are different changes) · rotation **verbatim + crc32, contiguous** · **cut boundary is the file's OWN line-7 history declaration, never a byte target** — if bytes don't drop enough, **the tier binds higher; live state is never rotated to hit a number** · `TRADE.md`'s PAT-044 two-clock header **must survive UN-BUMPED** (hygiene commit; TRADE is in `LEDGER_GLOB` now and the reader I wired watches that exact stamp) · `CLAUDE.md`: **move the STORY, keep the ⛔ TOMBSTONES** (sentinels stop retracted claims re-entering by pattern-match).
- **Expected: 60–70% cut to the boot load, no loss of retrievable content.**
- **DEFERRED, offered not asked:** `LESSONS.md` (39 KB read whole at boot; ~36 KB recoverable via hot/cold split — `workbook/LESSONS_INDEX.tsv` already exists). ⚠️ **Two caveats: lessons are cited BY NUMBER (`LESSONS #1` in my own step 10) = a stable API, so the index must carry numbers verbatim; and `lessons_check.py` needs checking for whole-file assumptions before the boot step changes.** Fine to defer.

---

## WHAT SESSION 3 ACTUALLY DID *(complete; nothing half-finished)*

**Will-directed file audit → "fix all of them". 16 findings, 16 fixed (+2 found while fixing), committed `f0a9927b6`, pushed and verified on origin.**

**The three that touched live decisions:** ① `XLE Sep-30 65C` carried **three different** moneyness figures on three surfaces + an 8/4 mark of `$98` — **live chain: `$291.00` vs cost `$455.35` = `−36.1%`**, understated **~3×**; all three corrected, disposition **NOT** re-ruled (Will/TERRY's). ② `domain/HORMUZ_TRANSIT_BASELINE.md` had **no impeachment banner** 4 days on, and still **recommended grading off `capacity_tanker` — the impeached field**; banner added, recommendation withdrawn, **FALCON + WALTER packeted**. ③ `REGISTRY.tsv` carried a **live EXIT TRIGGER on STNG**, a position ruled phantom 8/4 — retired with 8 other dead rows.
**Registry sweep: 9 rows live→retired**, 0 deleted, 0 levels changed. ✅ **FALSIFIED and it inverted my expectation — retiring decoration UN-blinded the board: `FRED-DCOILBRENTEU-ABOVE-100` now renders NEAR-THRESHOLD at `$95.29` (−4.7%)**, previously buried under four rows that could never change state. **L16/L21/L22/L23 now cited in the registry header.**
**Boot wiring:** did **not** invent a `--days` number; wired the **thresholdless `--nudge`** as a second boot reader. **Boot now renders `Ledger Staleness OK` + `Ledger Nudge FINDINGS` — expect that on your boot; it is the fix working, not a regression.**

★ **THE PATTERN, and it is the thing to carry: all three sharp findings were defects I had ALREADY DOCUMENTED elsewhere and not carried through** — the XLE mark was labelled `[STALE 8/4]` in its own row, the impeachment was in three files but not the one other desks read, the phantom was swept from position surfaces but not test surfaces. **My failure mode this month is not detection — it is follow-through across surfaces.** `[[finding_record_of_an_action_is_not_the_action]]`

⛔ **AND I REPRODUCED IT TWICE WHILE FIXING IT, both kept visible:** wrote a mechanism claim into `boot.py` **without running it** (`--nudge` returns rc=1, not 0) inside a comment whose subject is *"verified by running it, not reading it"* · archived the NEXUS_BRIEF block asserting its rules were *"carried in the digest below"* when they **were not**, until a minute later. **Also stamped SCRATCH `~12:0x` when the clock said `11:35` — and that fabricated stamp propagated into a wrong timing figure I gave Will.** ⇒ **RUN `date` BEFORE EVERY STAMP.**

## NEXT SESSION (dated, future-verifiable)

1. **🔴🔴 TAKE BOTH GRADES — see the banner at the top. Everything you need is there.**
2. **⏸️ BOOT-LOAD CUT — staged, prepped, WILL-GATED.** See the block above. **Get Will's word; do not act on the peer concur.**
3. **🟡 OWED — PROME ROW 58** *(packet deliberately LEFT IN `inbox/`, logged `deferred` on the sender's own scope: "explicitly QUEUED BEHIND today's rigs + COT grades")*. Name the observable(s) that say the oil-sleeve view is **COMPLETE or BROKEN for a LINEAR SHARES leg**, distinct from the options clocks, base-rated where a level is named (L21/L22). **Scope fence: independent of the 135C pair.** TERRY leads construction; nothing fills without Will.
4. **🔴 MON 8/24 — BESSENT PRESS CONFERENCE.** Grade on **PUBLISHED MECHANISMS** (OFAC designations, named entities, effective dates), **never on the presser happening** (L18). **Pre-registered read is in the catalyst row — do not rewrite it after the fact.**
5. **⏳ THE SECOND `USO Oct-16 135C` + TWO UNANSWERED RULINGS:** (a) the ratified **60–90 DTE** band has **NO satisfying USO expiry** (56 vs 119, no November) — Will must SCOPE it or grant an exception; **widening it silently is the LESSONS #21(b) trap.** (b) the **root-rule-#6** break, offered with its refuting measurement. ⛔ **NO FILL WITHOUT BOTH.**
6. **🟠 `INCIDENTS.tsv` RE-VERIFICATION BACKLOG — REAL WORK STILL OWED.** 17 ACTIVE rows past the 60d budget (worst `RF-004`, 155d). **A disclosure header was added 8/21 — that is NOT the fix.** ⛔ **Do NOT downgrade on a timer** (fabricates a restart nobody observed). ⚠️ **Bias is DIRECTIONAL — un-re-verified ACTIVE rows OVERSTATE offline capacity, i.e. toward my own thesis.** Also owed: Novorossiysk/Sheskharis, 2 events wide.
7. **🔴 `KILL-LEG2-TRANSIT` — RESOLVE OR RE-INSTRUMENT, MINE AS OWNER.** Banner now on the baseline doc and consumers notified, **but the falsifier itself is untouched and may be structurally unfireable.** ⛔ Re-scoping is a **WILL GATE** — bring a spec.
8. **🔴 ~Wed 9/9 — SPR EXCHANGE-WINDOW FALSIFIER** (base 293.426M; branches ≥−2.0M/wk vs ≤−4.0M/wk, no-verdict band between). **OPEN ASK: locate the RFP docket / Federal Register notice AT SOURCE.**
9. **🟠 RE-SPEC FORWARD CHECK ② (FALCON `KB-FALCON-102`).** 670 kbpd is Asia-only+month-scoped vs 2.17 mb/d total weekly liftings; **as written it manufactures a ~70% phantom collapse.**

## OPEN THREADS / WATCHES

- **⛔ SHARPEST EXPOSURE (v5.7): an official narrative capable of declaring Hormuz resolved, against a falsifier that may be unable to answer it.**
- **⚠️ MINE WARNING in Hormuz issued after Trump claimed it clear** — headline at seatrade-maritime; **site 403'd, issuing body and date UNVERIFIED.** Routed to HAWK.
- **⚠️ Closure date CONTESTED, n=4** (2/28 · "March" · 7/7 · 7/11-12). HAWK asked for the fleet-canonical one.
- **⚠️ Iranian exports `156 kb/d` through 8/17 from `893 kb/d` July [Kpler, single-source]** ⇒ ~83% already gone ⇒ **8/24 is largely SYMBOLIC for the oil balance.** Wants a second source.
- **⚠️ Russian capacity-offline estimates disagree ~2.5× — DO NOT AVERAGE:** Reuters **17%** (conservative live) · S&P **7 offline end-July +4 in Aug** (cleanest count) · Kyiv Post **42.7%** = CUMULATIVE-EVER-STRUCK, belligerent-aligned outlet.
- **⚠️ War-risk INSURANCE figures are JULY-VINTAGE** (3–10% of hull vs 0.25% pre-war) — **≥5 weeks stale, mark `[STALE]`.**
- **⛔ Unresolved:** Petroline 5 vs 7 mb/d · SPR floor 252.4M vs 400.0 · P5 row-27 width-bias re-spec · Yanbu↔Sidi Kerir double-count seam · `TANECO` incrementality.
- **⛔ EXPORT-SIGN WARNING live · RUNS-DECLINE IS NOT CAPACITY-OFFLINE · every 8/19–8/20 Russian strike item is "fire reported" or CLAIMED with ZERO operator statements — do not convert into barrels.**
- **⚠️ `NEXUS_BRIEF.md` 116 lines vs the provisional 100 cap — DISCLOSED, not silently accepted.** Remainder is CROSS-DOMAIN (31) + CALIBRATION (15), the blocks the cap rule protects. **Next compression must come from the STANDING blocks — a NEXUS/Will call.**

## POSITION DECISIONS PENDING

- **💵 WILL RULED 8/21: SELL ONE of the `USO Oct-16 135C ×2`.** Card → [`setups/2026-08-21_uso-135c-roll-card.md`](setups/2026-08-21_uso-135c-roll-card.md). ⚠️ **Execution is Will's — nothing filled, no order staged.**
- **⏳ OPEN: the SECOND contract** — roll to `Dec-18 $135C` (~$375 net debit) vs hold to Oct-16. **Blocked on rulings (a) and (b).**
- **🟠 `XLE Sep-30 $65C ×2`: `2.1% OTM`, 40 DTE, `$291` vs `$455.35` cost (`−36.1%`, live chain 11:23).** ⛔ **Disposition `LAPSE` NOT re-ruled** — but *"not meaningful forward exposure"* is an 8/4 judgement the tape has overtaken. **Flagged for the next disposition review.**
- **NONE PENDING ON THE SHARES — WILL RULED HOLD 8/18.** **35 USO sh, basis $121.88.** ⛔ A CHOSEN outcome. ⚠️ **They have NO live stop** — the retired `MKT-USO-BELOW-*` rows made that visible rather than papering over it. **`RISK_RULES #9`, open, Will/TERRY's.**
- **⛔ NO LIVE DEPLOY GATE EXISTS** — v2 retired 7/30, v3 retired by Will 8/07, `TRY-FIRE-006` retired 8/18.

## MAIL STATE

- **INBOX 2 OPEN (both deliberate) · WALTER lane 0 · outbox 0.** board_log **239** rows.
  - **PROME row-58 ask** — `deferred` on the sender's own scope. See NEXT SESSION #3.
  - **DAEDALUS boot-load review** — `acted` (prep executed), **kept in inbox as the ACTIVE WORKING REFERENCE for the staged cut.** Archive it when the cut lands.
- **SENT (2, both no-ask/no-reply-needed):** → **FALCON** *(HORMUZ impeachment banner + the ≤5% `capacity_tanker` bar WITHDRAWN — the one they might adopt)* · → **WALTER** *(their `anchors/IRAN_WAR.md` cites the same file)*.
- **Owed TO me:** **Will** — rulings (a) tenor scope, (b) root-rule-#6 break, the war-risk-halves ruling, the WP3 call, **and the go/no-go on the boot-load cut.** **DEWEY** — `gie_pull.py`. **HAWK** — the three 8/21 asks.
- ✅ **CLOSED 8/21:** the `ledger_staleness`/`TRADE.md` glob-coverage flag to PROME — ruled, answered, no longer owed.

## 📒 LEDGER-NUDGE DISPOSITION

| Ledger | Disposition |
|---|---|
| **`INCIDENTS.tsv`** | ✅ **REFRESHED 8/21** — disclosure header added. ⛔ **Re-verification still owed — NEXT SESSION #6.** |
| **`REGISTRY.tsv`** | ✅ **REFRESHED 8/21** — 9 rows retired + retirement-sweep record + 4 governing lessons. |
| **`board_log.tsv`** | ✅ **REFRESHED** — 235 → 239. |
| **`TRADE.md`** | ✅ **REFRESHED 8/21** — XLE mark corrected off the live chain. ⚠️ **In `LEDGER_GLOB` since 8/21 but INERT at boot's inherited 30d default** — per-entry `--days` is queued to DAEDALUS's ~9/1 Staleness #4 manifest; the labelled-INERT state is the ratified interim. |
