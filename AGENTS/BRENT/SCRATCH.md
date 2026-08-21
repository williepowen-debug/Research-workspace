# BRENT SCRATCH — Fri Aug 21, 2026 **~12:0x ET** *(live session #3, Will-directed · boot 11:12 → FULL FILE AUDIT → fix-all → write-back)*

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴🔴 **READ THIS FIRST: BOTH OF TODAY'S GRADES ARE *STILL* OWED AND *STILL* UNTAKEN. THEY ARE NOW THE ONLY THING ON THIS DESK THAT MATTERS.**
>
> **This session was a Will-directed file audit, not a market session. It ended BEFORE Baker Hughes (~13:00 ET) and BEFORE CFTC COT (~15:30 ET) — the same way session 2 did.** `$0` moved, no gate fired, no threshold LEVEL moved.
>
> | Series | Prints | State | Cost of stacking |
> |---|---|---|---|
> | **Baker Hughes** (`BRT-26`) | Fri 8/21 ~13:00 ET | ⏳ **UNGRADED** | Next print Fri **8/28**. `BRT-26` sits **2 rigs from the 457 line**, window closes 9/30. Two prints on one series destroys the WoW deltas the ladder is defined on. |
> | **CFTC COT** as-of Tue 8/18 | Fri 8/21 ~15:30 ET | ⏳ **UNGRADED** | **Vintage #2 — the FIRST grade of the 35b successor on a clean vintage.** TERRY + two desks staged on it. Vintage #3 lands 8/28. |
>
> ⛔ **MY OWN STANDING RULE: "DO NOT LET GRADES STACK. If a grade slips past its print, grade it BEFORE the next one lands." REPAIR WINDOW: 8/21 15:30 → 8/28 13:00.** A session booting Mon 8/24 can still take both cleanly.
> ⚠️ **IF TAKEN LATE, SAY SO ON THE GRADE.** A late grade is valid; one that hides its latency is not.
> ✅ **BAKER HUGHES GRADE PLAN (corrected — the primary is NOT unreachable):** primary returns **HTTP 200 in 0.36s** to a labelled table but publishes the **TOTAL only**; `BRT-26` grades the **OIL** count and the split is in no BH page's HTML. **Total is not a proxy (8/14: total +5, oil +1).** ⇒ anchor the CAPTURE at the primary (its companion TOTAL reproduces to the unit), take the OIL leg from an aggregator, **and say which leg is which.** ⛔ Never a bare digit-regex on BH HTML — it returns `457`, my own frozen line, out of CSS/UUID fragments.
> ✅ **COT:** `cot_grade.py --expect 2026-08-18`. Leg A deadband **109,165–118,325**, Leg B OI-share ≤ **4.909%** GATING; raw `f_disagg.txt` code **067651**, NOT Socrata; verify `report_date` IN-ROW; **exit 3 = WAIT**; `median_unit 9,160` FROZEN; **incumbent RETIRED, do not re-grade**.

---

## CHANGES SINCE LAST SESSION *(session 2 closed ~11:1x; this is the same calendar day, ~1h later)*

- **Boot 7/7 clean, 23.3s.** Mail 0/0 at the check — **but a PROME packet landed at 11:12, the same minute**, and a DAEDALUS packet at ~11:4x. Both handled (below).
- **Tape [PROVISIONAL LIVE BARS]:** Brent `BZ=F` **$93.99** · WTI **$86.68** · USO **$134.50** · XLE **$63.69** · GASREGW **4.049** (8/17, breached). Softer than session 2's 09:48 pull; nothing structural.
- **No new market work.** Thesis unchanged at **v5.7**. No prediction resolved.

## WHAT I DID THIS SESSION — WILL-DIRECTED FILE AUDIT, THEN "FIX ALL OF THEM"

**16 findings surfaced, 16 fixed** (+2 found *during* the fixing, also fixed). Full list was delivered to Will in-session.

### THE THREE THAT TOUCHED LIVE DECISIONS
1. **`XLE Sep-30 $65C` was stale on THREE surfaces with THREE different numbers, all understating exposure.** `CATALYSTS.tsv` said *"deep OTM (~+23% to strike at XLE $52.76)"*; `STATUS.md` said *"8.0% OTM at $60.18, ~51 DTE"*; `TRADE.md` carried an **8/4 broker mark of `$98` / `−78.5%`**. ⇒ **LIVE CHAIN 11:23:45: bid 1.40 / ask 1.51 / mid `$1.455` ⇒ `$291.00` vs cost `$455.35` = `−36.1%`** — the leg was understated **~3×** — and at XLE `$63.69` the strike is **2.1% OTM, 40 DTE**. All three surfaces corrected; `TRADE.md` named as sole owner. ⛔ **DISPOSITION (`LAPSE`) NOT RE-RULED — Will/TERRY's call. An audit corrects figures, never a Will-gated disposition.**
2. **`domain/HORMUZ_TRANSIT_BASELINE.md` carried NO impeachment banner** — 4 days after I impeached the series and wrote it to STATUS, THESIS and the registry. **It is the file FALCON's `hormuz_transit_watch.py`, FALCON's `FRESH_LEG_BASELINE.md` row 2 and WALTER's `anchors/IRAN_WAR.md` actually read** — and §4 still **RECOMMENDED grading off `capacity_tanker`, the impeached field**, on a monthly profile *computed from that same field*. Banner added, recommendation struck and withdrawn, **packets sent to FALCON and WALTER**.
3. **`workbook/REGISTRY.tsv` carried a LIVE EXIT TRIGGER on a position that does not exist** — `MKT-STNG-BELOW-71.5`, classification `risk`, label *"STNG STOP LEVEL — exit trigger"*. STNG ruled a **PHANTOM 8/4** and struck from `TRADE.md` + root `CLAUDE.md` that day; the test surface was never swept. **Retired, with 8 other dead rows.**

### THE REGISTRY SWEEP — 9 rows live → retired, 0 deleted, 0 levels changed
- **(a) phantom-position tests:** `MKT-STNG-BELOW-71.5`, `MKT-STNG-ABOVE-100`.
- **(b) permanently-breached decoration** (the F4 class Will ruled on 7/31 for `crack >$30`): `MKT-VLO-ABOVE-160` (+115%), `MKT-MPC-ABOVE-170` (+112%), `MKT-XOP-ABOVE-150` (+25%), `MKT-LNG-ABOVE-255` (+8.9%). **The 7/31 ruling killed ONE instance and four siblings survived it.**
- **(c) unreachable by construction:** `MKT-USO-BELOW-80`, `MKT-USO-BELOW-75` (~40–44% below spot), `MKT-XLE-ABOVE-100` (+57% away).
- ✅ **FALSIFIED, NOT ASSERTED — and the result inverted my expectation: retiring decoration did NOT blind the board, it UN-blinded it.** With four permanent greens gone, **`FRED-DCOILBRENTEU-ABOVE-100` now renders in NEAR THRESHOLDS at `$95.29` (−4.7%)** — Dated Brent within 5% of the $100 line, live and meaningful, previously buried under rows that could never change state.
- ⛔ **NOTHING RE-LEVELLED.** A replacement refiner-margin / E&P / USO-drawdown line is a **NEW REGISTRATION with base rates** (L21/L22), never a re-level. **Governing lessons L16/L21/L22/L23 now CITED in the registry header** (`--spec` was silent on all four before).
- ⚠️ **`MKT-USO-BELOW-*` retirement makes a real gap VISIBLE rather than papered over: the 35 USO shares have NO live stop. `RISK_RULES #9` is open and Will/TERRY's — NOT closed by this audit.**

### SURFACES THAT WERE CERTIFYING STALE CONTENT
- **`STATUS.md` header was 2h+ behind its own body** (`~08:2x` + session-1 narrative over a `~10:4x` body). Re-stamped.
- **`STATUS.md` § SUMMARY FOR WILL was stranded pre-open** — *"five straight sessions to $93.28 … Nothing needs doing"* while the tape was ~$94, SCRATCH said **six**, and Will had ruled **SELL ONE**. **The block Will is most likely to read was the stalest on the file.** Rewritten.
- **`demand_destruction/TRACKER.md` § REGISTERED ALERT LINES was skipped at session 2's closeout** — last written **08:21** (`9aef6d2a5`); session 2 made **six commits** 10:45→11:10 and never touched it. Its unconditional-refresh rule (adopted 8/17) was **breached at the very next closeout after it was written**, and the 3-day self-check could not catch it because the stamp was 3 hours old. ⇒ ★ **the 8/17 fix addressed STALENESS; the actual failure was OMISSION.** Refreshed + re-stamped SCOPED-PARTIAL with the pre-print boundary on lines 7/8 named explicitly.

### AND TWO DEFECTS FOUND *WHILE* FIXING, WHICH IS THE PART WORTH KEEPING
- ⛔ **I wrote a mechanism claim into `boot.py` without running it** — asserted `--nudge` "exits 0 whether or not it finds ledgers behind", in a comment whose whole subject is *"verified by running it, not by reading it"*, during an audit of exactly that class. **It returns rc=1.** Corrected in place, left visible.
- ⛔ **I archived the NEXUS_BRIEF prior-cycle block and wrote that its rules "are carried in the digest below" — they were NOT, until I put them there a minute later.** I asserted a fix in the same edit that was supposed to perform it. `[[finding_record_of_an_action_is_not_the_action]]`
- ⛔ **A retracted claim was still travelling cross-agent:** `NEXUS_BRIEF.md` FORWARD CATALYSTS still said the Baker Hughes primary *"has timed out on every attempt"* — the claim retired at 11:07 in `CLAUDE.md`. **NEXUS reads this brief INSTEAD of my STATUS**, so the wrong constraint was the one leaving the desk. Also found in `boot.py`'s comments. **Three surfaces; the doc fix had not travelled to either.**

### ★ THE PATTERN ACROSS ALL OF IT
**Every one of the three sharp findings was a defect I had already DOCUMENTED somewhere and not carried through.** The XLE mark was labelled `[STALE 8/4]` in its own row. The impeachment was in three files, just not the one others read. The STNG phantom was struck on the position surfaces and left on the test surface. ⇒ **My failure mode this month is not detection — it is follow-through across surfaces.** `[[finding_record_of_an_action_is_not_the_action]]`

## NEXT SESSION (dated, future-verifiable)

1. **🔴🔴 TAKE BOTH GRADES.** See the banner at the top — plans, bands and traps are written out there. **Do not let them reach 8/28 ungraded.**
2. **🟡 OWED TO PROME/TERRY — ROW 58 (deferred on the sender's own scope, packet LEFT IN `inbox/` deliberately).** Name the observable(s) that say the oil-sleeve view is **COMPLETE or BROKEN for a LINEAR SHARES leg**, distinct from the options clocks, base-rated where a level is named (L21/L22). Scope fence: **independent of the 135C pair.** TERRY leads construction; nothing fills without Will.
3. **🔴 MON 8/24 — BESSENT PRESS CONFERENCE.** Grade on **PUBLISHED MECHANISMS** (OFAC designations, named entities, effective dates), never on the presser happening (L18). **Pre-registered read is in the catalyst row — do not rewrite it after the fact.**
4. **⏳ THE SECOND `USO Oct-16 135C` + TWO UNANSWERED RULINGS** (unchanged): (a) the ratified **60–90 DTE** band has **NO satisfying USO expiry** (56 vs 119, no November) — Will must SCOPE it or grant an exception; **widening it silently is the LESSONS #21(b) trap.** (b) the **root-rule-#6** break, offered with its refuting measurement. ⛔ **NO FILL WITHOUT BOTH.**
5. **🟠 INCIDENTS.tsv RE-VERIFICATION BACKLOG IS REAL WORK STILL OWED.** 17 ACTIVE rows past the 60d budget (worst `RF-004`, 155d). **A disclosure header was added 8/21 making the boundary visible — that is NOT the fix.** ⛔ Do **not** downgrade on a timer: it would fabricate a restart nobody observed. ⚠️ **The bias is directional — un-re-verified ACTIVE rows OVERSTATE offline capacity, i.e. toward my own thesis.** Also still owed: Novorossiysk/Sheskharis, 2 events wide.
6. **🔴 `KILL-LEG2-TRANSIT` — RESOLVE OR RE-INSTRUMENT, MINE AS OWNER.** Banner now on the baseline doc and consumers notified, **but the falsifier itself is untouched and may be structurally unfireable.** ⛔ Re-scoping is a **WILL GATE** — bring a spec.
7. **🔴 ~Wed 9/9 — SPR EXCHANGE-WINDOW FALSIFIER** (unchanged; base 293.426M, branches ≥−2.0M/wk vs ≤−4.0M/wk, no-verdict band between). **OPEN ASK: locate the RFP docket / Federal Register notice AT SOURCE.**
8. **🟠 RE-SPEC FORWARD CHECK ② (FALCON `KB-FALCON-102`) — still not done.** 670 kbpd is Asia-only+month-scoped vs 2.17 mb/d total weekly liftings; **as written it manufactures a ~70% phantom collapse.**

## 📒 LEDGER-NUDGE DISPOSITION *(now fires at BOOT as well as closeout — see below)*

| Ledger | Behind | Disposition |
|---|---|---|
| **`INCIDENTS.tsv`** | 15 STATUS-writes | ✅ **REFRESHED THIS SESSION** — disclosure header added (17 ACTIVE rows past budget, directional bias named, coverage 2 events wide). ⛔ **Re-verification itself is still owed — see NEXT SESSION #5.** |
| **`REGISTRY.tsv`** | 4 | ✅ **REFRESHED THIS SESSION** — 9 rows retired, retirement-sweep record + 4 governing lessons added to the header. |
| **`board_log.tsv`** | 1 | ✅ **REFRESHED** — 2 packets logged (235 → 237). |

## OPEN THREADS / WATCHES

- **⛔ SHARPEST EXPOSURE, unchanged (v5.7): an official narrative capable of declaring Hormuz resolved, against a falsifier that may be unable to answer it.**
- **⚠️ MINE WARNING in Hormuz issued after Trump claimed it clear** — headline at seatrade-maritime; **site 403'd; issuing body and date UNVERIFIED.** Routed to HAWK.
- **⚠️ Closure date CONTESTED, n=4** (2/28 · "March" · 7/7 · 7/11-12). HAWK asked for the fleet-canonical one.
- **⚠️ Iranian exports `156 kb/d` through 8/17 from `893 kb/d` July [Kpler, single-source]** ⇒ ~83% already gone ⇒ **8/24 is largely SYMBOLIC for the oil balance.** Wants a second source.
- **⚠️ Russian capacity-offline estimates disagree ~2.5× — DO NOT AVERAGE:** Reuters **17%** (conservative live) · S&P **7 offline end-July +4 in Aug** (cleanest count) · Kyiv Post **42.7%** is CUMULATIVE-EVER-STRUCK from a belligerent-aligned outlet.
- **⚠️ War-risk INSURANCE figures are JULY-VINTAGE** (3–10% of hull vs 0.25% pre-war) — **≥5 weeks stale, mark `[STALE]`.**
- **⛔ Still unresolved:** Petroline 5 vs 7 mb/d · SPR floor 252.4M vs 400.0 · P5 row-27 width-bias re-spec · Yanbu↔Sidi Kerir double-count seam · `TANECO` incrementality.
- **⛔ EXPORT-SIGN WARNING live · RUNS-DECLINE IS NOT CAPACITY-OFFLINE · every 8/19–8/20 Russian strike item is "fire reported" or CLAIMED with ZERO operator statements — do not convert into barrels.**
- **⚠️ `NEXUS_BRIEF.md` is 116 lines vs the provisional 100 cap — DISCLOSED, not silently accepted.** Cut 125→116 by archiving the prior-cycle block. **Stopped there deliberately:** the remainder is CROSS-DOMAIN (31) + CALIBRATION (15), the two blocks the cap rule protects, plus this cycle's new market state. **The next compression must come from the STANDING blocks — a NEXUS/Will call, not mine.**

## POSITION DECISIONS PENDING

- **💵 WILL RULED 2026-08-21: SELL ONE of the `USO Oct-16 135C ×2`.** Card → [`setups/2026-08-21_uso-135c-roll-card.md`](setups/2026-08-21_uso-135c-roll-card.md). ⚠️ **Execution is Will's; nothing filled, no order staged.**
- **⏳ OPEN: the SECOND contract** — roll to `Dec-18 $135C` (~$375 net debit) vs hold to Oct-16. **Blocked on rulings (a) and (b) above.**
- **🟠 `XLE Sep-30 $65C ×2`: `2.1% OTM`, 40 DTE, `$291` vs `$455.35` cost (`−36.1%`, live chain 11:23).** ⛔ **Disposition `LAPSE` NOT re-ruled** — but the *"not meaningful forward exposure"* line is an 8/4 judgement the tape has overtaken. **Flagged for the next disposition review.**
- **NONE PENDING ON THE SHARES — WILL RULED HOLD 8/18.** **35 USO sh at $134.50 vs basis $121.88.** ⛔ A CHOSEN outcome, not a defaulted one. ⚠️ **They have no live stop (see the registry sweep) — `RISK_RULES #9`, open, Will/TERRY's.**
- **⛔ NO LIVE DEPLOY GATE EXISTS** — v2 retired 7/30, v3 retired by Will 8/07, `TRY-FIRE-006` retired 8/18.

## MAIL STATE

- **INBOX 1 OPEN (deliberate) · WALTER lane 0 · outbox 0.** board_log **237** rows (was 235).
- **CONSUMED (1):** **DAEDALUS** — both my `ledger_staleness` flags **CONFIRMED AT CODE and fixed** (`a9a1129e7`): docstring `default 14`→30 (I was the **only** desk carrying the inherited 14); **the legend sign was INVERTED SINCE BIRTH** (`+` = older than STATUS) and my low-confidence read was right. Per-glob-entry `--days` deliberately queued to the **Staleness #4 ~9/1 manifest**; my labelled-INERT `TRADE.md` row confirmed as the right interim state. → `inbox/processed/`.
- **OPEN (1, LEFT IN INBOX ON PURPOSE):** **PROME** row-58 ask — deferred on the sender's own scope (*"explicitly QUEUED BEHIND today's rigs + COT grades"*). **Deferral is fine, silence is not** — logged `deferred` with the reason. See NEXT SESSION #2.
- **SENT (2):** → **FALCON** *(HORMUZ baseline impeachment banner + the ≤5% `capacity_tanker` bar WITHDRAWN — the one they might adopt)* · → **WALTER** *(their `anchors/IRAN_WAR.md` cites the same file; convention stands, throughput reading does not)*. Both **no-ask, no-reply-needed**.
- **Owed TO me:** **Will** — rulings (a) tenor scope and (b) root-rule-#6 break; the war-risk-halves ruling; the WP3 call. **DEWEY** — `gie_pull.py`. **HAWK** — the three 8/21 asks (log MINOAN DIGNITY separately from 8/15; canonical closure date; mine-warning source).
- ✅ **CLOSED THIS SESSION:** the `ledger_staleness`/`TRADE.md` glob-coverage flag to PROME — **ruled and answered**; no longer owed.
