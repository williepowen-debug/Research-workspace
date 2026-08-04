# BRENT SCRATCH — Tue Aug 4, 2026 **14:10 ET** (⏰ `date`-verified) · **SESSION 2 OF THE DAY: BOOT + DEPLOY GATE v3 RATIFIED** (the gate was unfillable by construction · legs (a)+(a2) MET · deploy packet with Will · **still BEFORE the close**)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ⏳ **CLOSED OUT ~14:10 ET, AGAIN BEFORE THE 16:00 CLOSE. THE SESSION ENDS MID-DECISION AND THAT IS DELIBERATE.**
> ⛔ **WILL'S "approved" RATIFIED THE SPEC (GATE v3). IT IS *NOT* A FILL AUTHORIZATION. NO CAPITAL HAS MOVED.**

---

## ⏳ FIRST THING NEXT SESSION — **BRANCH ON THE CLOCK**

### ▸ **IF AFTER 16:00 ET ON 8/4:**

**0. 🔴 READ THE 8/4 CLOSE AND RECORD IT — but note what it does and does NOT decide under v3.**
   - **Under GATE v3 the 8/4 close is NOT the fire trigger for 8/4** — leg (a) ran all day off the **8/3 close (57.20)**. The 8/4 close sets **tomorrow's** leg (a).
   - **Line: OVX ≤ 58.6245** (−15.0% from the peak **68.97**, 7/23, CLOSE basis). ⚠️ **RE-DERIVE THE PEAK from the 7/16→today close series — never carry 68.97 or 58.6245 as constants.**
   - At **13:40** OVX was **53.20**; session high **56.50** — the line was **never breached today**. Verify against FRED `OVXCLS` (matched 6-for-6 through 8/3).
   - **Then check: DID A FILL HAPPEN?** If Will approved and TERRY filled, record it in `TRADE.md` EXECUTION LOG **with the actual fill price** — do not leave a PENDING row (boot step 6c exists because one sat mis-stated for three days).

### ▸ **IF STILL BEFORE 16:00 ET ON 8/4:**
   Re-pull OVX; **if it is still ≤58.6245 the gate remains live and fillable today.** Do not re-grade leg (b) — TERRY grades it once, at the ticket.

---

## ★ THE SESSION IN THREE LINES

**Spec:** **DEPLOY GATE v2 WAS UNFILLABLE BY CONSTRUCTION** — `^OVX`'s last bar is **16:00** and USO options close 16:00, so leg (a) became knowable at exactly the moment leg (b) became ungradeable. **Window = ZERO, not the 15 min TERRY twice asserted.** **v3 ratified.**
**Process:** **The root cause is mine twice over** — v2 was a mixed-latency basket wearing a single window (the defect **#21(b) fixed for Stage A/B on 7/29 and I reproduced on 7/30**), and **my own 8/2 audit cleared it off daily closes, never testing executability.**
**Discipline:** **My first analysis pass was WRONG** (object-dtype `.mean()` mangled booleans; a2's block rate read **1.3%** vs a true **65.8%**) — caught by disbelieving a 1.3% tail against the audit's known 44.4%. **It would have shipped a mis-specified tightening.**

## CHANGES SINCE LAST SESSION *(1:30 PM → 2:10 PM)*

- **📈 TAPE [⚠️ INTRADAY 13:57]:** WTI **$75.88** (−5.55%) · Brent **$79.37** (−5.25%) · USO **$115.68** (−5.31%) · **OVX 53.20** · VIX 16.49 (**+3.97%**). **Third consecutive down session; WTI ≈−15% in three days. VIX UP while OVX collapses ⇒ still oil-specific.**
- **📬 TWO TERRY PACKETS consumed** (board_log **133 → 135**, 2 moved / 2 rows, reconciled 1:1).
- **✅ THE $1.50 LIMIT IS SET** on all five TERRY surfaces — that chase item is **CLOSED**. TERRY disclosed the sharper version: its own **10:42** row had already priced `125/130 ×2 @ $1.50 = $300`, and the 11:11 revision to $1.65 was **a regression, not an oversight**.
- **🔄 LEG (b) SEQUENCE REVERSED:** TERRY's **12:24** chain put `125/130 ×2` at **26.0%** worst case — 7.0pp inside — flipping `30.0 → 34.0 → 38.0`. **Caveated by TERRY against itself** (the 130C quoting 1.75% wide on 4,188 contracts is plausibly transient).
- **⚖️ TERRY adopted `RISK_RULES #14`** — net debit is a **MOMENT** property, not a STRUCTURE property. Graded 5× this morning by three of us; **not one actionable.**
- **⛔ 5 DM OBLIGATIONS, ZERO RECEIPTS** — found at boot; still open (see NEXT SESSION #2).

## WHAT I DID

**① VERIFIED THE EXCHANGE-HOURS FACT INSTEAD OF INHERITING IT.** Pulled 5m bars: **`^OVX` last bar 16:00** · **`^VIX` 16:10** (VIX runs late, **OVX does not**) · USO **shares** 19:55 (**shares, not options**). ⇒ **TERRY's "16:15" is wrong, and wrong in the COMFORTING direction** — a 15-min window sounds workable; a zero-min window is a dead gate.

**② DESIGNED, BASE-RATED AND SHIPPED GATE v3.** Leg (a) → **most recent official close** (a state, known 09:30) · **NEW leg (a2)** live non-reversal at the ticket · leg (b) unchanged. **Window 0 min → 6.5 h.** Per **#21(b)** the loosening ships with **two tightenings**: v3 needs **TWO** independent readings below the line where v2 needed one, and **clearance expires after one session.** Base rate (n=4,729, 113 episodes): fire **68.1%**/20td · slippage **−0.04%** · **tail 38.2% → 39.5% (+1.3pp)** · a2 blocks **7.8%** (strict form 66.2% — rejected). **Disclosed cost: 31.2% of fire sessions close back above the line.**

**③ ⛔ CONVICTED MY OWN 8/2 AUDIT.** It returned *"THE GATE IS SOUND… NO SPEC CHANGE"* off **daily close** data — i.e. it modelled **v3's cadence**, not v2 as written. **I audited statistical merit and never asked whether the gate could be EXECUTED. An all-clear is worse than no audit, because it stops anyone else looking.** Routed to PROME as fleet-shaped (a gate audit should test **executability** as a separate axis — #22 pointed at gates rather than pre-regs).

**④ ⛔ AND CORRECTED MY 8/3 ROOT-CAUSE.** I logged PROME's 3.5h routing delay as why the gate didn't fire — **a COORDINATION failure masked a STRUCTURAL one.** Second wrong-origin diagnosis this week.

**⑤ DISCLOSED THE UNCOMFORTABLE PART FIRST.** **This rule would fire today.** On 7/30 I offered *"the proposed rule would NOT fire today"* as evidence a re-spec wasn't written to fit the tape. **I cannot offer that here** — so it went into the proposal's **opening**, not a footnote.

**⑥ ADOPTED TERRY'S §2 ONTO THE LIVE SPEC:** **a firing gate carries ZERO thesis information.** Leg (a) fires because OVX decayed; leg (b) eased because USO fell. **Both legs open as the market prices LESS of my thesis.** Written into `TRADE.md` itself rather than left in a packet.

**⑦ SPEC SWEEP + a checker finding.** 9 governing lessons → 8 NOT CITED, incl. **L22, the lesson this whole defect is an instance of.** Reconciled all. ⚠️ **The sweep does not converge — citing L11/L16/L18 recruited L10 and L19, taking the count 9 → 11. It is an ATTENTION tool, not a completion criterion; driving NOT-CITED to zero would incentivise writing LESS about lessons.**

## NEXT SESSION (dated, future-verifiable)

1. 🔴 **Record the 8/4 close** (sets **tomorrow's** leg (a), not today's) · **check whether a fill happened and log it with the real price — no PENDING rows.**
2. 🔴 **FILE THE 5 DM RECEIPTS.** `MSG-PROME-20260803-002` (3 obligations) + `-003` (2, due 8/13): **all `receipt_required: true`, `receipts=0`.** Retention was right; **disposition was never filed, and DM v1 says silence is not acknowledgment.** Use `MESSAGING/tools/msg.py receipt`.
3. 🟠 **Wed 8/5 10:30 EIA WPSR wk-7/31** — pre-reg is **FROZEN** (`setups/2026-08-04_EIA-wk0731-prereg.md`); **grade in the ADDENDUM only.** Cloud routine fires 11:00 and **records, never grades.**
4. 🔴 **Fri 8/7 COT as-of 8/4.** Ladder from **101,016**. Raw `f_disagg.txt`, **not Socrata**. **MUST NOT STACK.**
5. 🟠 **Still deferred (Phase 2):** `docket/CATALYSTS.tsv` (Bessent deal date, EIA 8/5, COT 8/7; prune fired) · **`INCIDENTS.tsv` scope ruling** — four vessel strikes in four days, **no BRENT-side record**; decide vessels-are-HAWK's and add a pointer row either way · TRACKER weekly row.
6. 🟠 **Phase 3:** LESSONS + index rows for today's classes (**executability-vs-validity**; **the comforting-direction error**) · **BUILD `instrument_check.py`** — every registered gate/threshold/falsifier declares its instrument; boot verifies it **exists, is reachable, and publishes fast enough for the test's window.** ★ **Today is the strongest argument yet for it: it would have caught the OVX-16:00 defect, the dead PortWatch falsifier, the never-existed AIS, the permanently-breached crack line and the unmeasurable WS200.**
7. 🟡 **NEXUS_BRIEF compression owed** — 146 lines vs the 100 cap, declared not hidden.
8. 🟡 ~8/12 CPI + FALCON falsifier · ~8/15 Jazan restart · 9/1 Russia carve-out · 9/6 OPEC+ · **register BRT-16/BRT-21 successors FORWARD** (owed since 7/30).

## OPEN THREADS / WATCHES

- 🔴 **THE FALSIFIER'S INSTRUMENT IS STILL DOWN.** PortWatch `chokepoint6` dead since 7/23; **FALCON has not answered.** Until then **v5.4's anti-ratchet guard is nominal and this thesis is closer to unfalsifiable than the guard implies.**
- 🔴 **n=0 genuine physical reopenings — real-vs-fake is UNCALIBRATED.** Stage-A is fitted to a PROFITABLE TRADE, not a VERIFIED REOPENING.
- ⚠️ **TERRY'S COUNTER, NOT RETIRED:** *is OVX at 53 the decay leg (a) was designed to buy, or the market correctly concluding the event is over?* **At n=0 I cannot resolve it from evidence** — which is why the premise control is Will's [Approve].
- ⚠️ **UNRECONCILED: my 68.1% fire rate vs the 8/2 audit's 81.9%** (113 de-overlapped episodes vs n=79 arming days). **Neither presented as canonical**; the comparative v2-vs-v3 result is unaffected.
- ⚠️ **USO OPTIONS' 16:00 close is NOT independently verified** (OVX's is). If they run to 16:15 the v2 window was 15 min not zero — **v3 unaffected**, but the defect statement softens.
- 🟠 Diesel crack: thesis stronger, entry worse — card `NO AT THIS PRICE` · un-anchored *"war-risk halves"* threshold **STILL OPEN**.
- 🟠 Velos Amber vs UKMTO 103-26 timestamps **still unreconciled**, compounded by Minoan Pioneer.
- 🟡 EU storage (**GIE key still pending from Will**) · Jazan/product half of the v5.3 retraction UNTESTED · PROME DOCKET row 80 correction not actioned · **46 routine-authored commits unaudited.**

## POSITION DECISIONS PENDING

- **Convex arm — GATE v3 legs (a)+(a2) MET; leg (b) grades AT THE TICKET. NO CAPITAL MOVED.** Packet with Will → `setups/2026-08-04_DEPLOY-PACKET-convex-arm-v3-GATE-LEGS-a-a2-MET.md`. **Rec: ~$300 · USO Oct-16 `125/130 ×2` · limit $1.50.** Alternative `125/135 ×1` built if Will holds the 12–15% band.
- **⏳ THREE THINGS OWED BY WILL ON THE PACKET:** [Approve]/[Decline] the fill · **the ~1.3pp short-leg band departure** · optionally TERRY's **`MIN($1.50, fire-time worst case)`** limit form (**I endorse it**; it reduces fill probability, which is Will's axis).
- **★ USO EQUITY = 35 SHARES ≈ $4,049 — the LARGE UNDEFENDED oil risk**, down **~$470 in three sessions, more than the entire proposed trade costs.** **NOT a trim recommendation** (root rule #7 — thesis intact).
- **USO Sep-18 150/165 — HOLD, do not defend.** ~29% OTM at 45 DTE, effectively a lapse. **Fill price still unpriced — needs the Robinhood capture.**
- **XLE $65C Sep-30 = LAPSE.** **STNG — qty/cost NEVER broker-verified.**

## MAIL STATE

- **INBOX: 2 DM files only** (`MSG-PROME-20260803-002`, `-003`) — **correctly retained** (a DM moves only when every obligation is terminal), **but 5 receipts are OWED, see NEXT SESSION #2.**
- **SENT THIS SESSION (2):** → **TERRY** (v3 ratified · the 16:15 correction · ticket sequence · `MIN()` endorsed) · → **PROME** (`PROME/inbox/`, the live surface — v3 + the self-implicating audit finding).
- **Outbox:** **3 top-level** — the 8/4 limit ruling (TERRY has now replied ⇒ **sweep to `delivered/` next session**) + 2 audit packets from 7/31 pending a round-2 batch.
- **Owed TO me:** **FALCON on PortWatch** (blocking) · **Will: [Approve] decision, band ruling, ONE Robinhood capture (closes 4), GIE key** · the war-risk-halves ruling.

## WORKBOOK HEALTH

- **LIVE:** **`TRADE.md` (GATE v3 ratified + v2 leg-(a) row annotated)** · STATUS (**240 lines**, under cap) · THESIS v5.4 · TRACKER · SCHEDULED_RUNS · EIA pre-reg (frozen) · **deploy packet v3 (with Will)** · staged packet (**SUPERSEDED banner, retained unedited as the dated record**) · board_log (**135**) · SCRATCH · NEXUS_BRIEF.
- **FROZEN (correct):** `workbook/` KB · VX · FLOW · GROUP_MAP · `thesis/TIMELINE.md`.
- **Boot kit 4/5** — ⚠️ **`eia_weekly.py` FAILED inside boot.py at 61.8s but exits 0 standalone with live data ⇒ a WRAPPER TIMEOUT, not a data failure. Worth fixing so a real failure is not camouflaged.** Lesson-conflict **0** · predictions-due **clean** · ledger staleness **clean**.
- **🔑 KEYS:** `EIA_API_KEY` + `FRED_API_KEY` SET · **`GIE_API_KEY` still pending from Will.**
- **⛔ INSTRUMENT GAPS:** 🔴 **PortWatch `chokepoint6` dead since 7/23 — BLOCKING the thesis falsifier** · no real-time AIS · Baker Hughes primary hard-down from this box · no Brent overnight feed · no Worldscale/freight feed · HY energy OAS unavailable free.
- **⏰ CLOCK SKEW CONFIRMED ON MY SIDE:** my own draft stamp read `~14:10` against a `date` of **13:57**. **Every stamp in today's packets is machine-read.** TERRY is routing the fleet fix to PROME — supported.
- **GIT:** 1 commit (`268f3c223`), path-scoped, **pushed and verified** (`Pushed.` + my hash in the push list). Origin was 0-behind at boot ⇒ **no pull needed, so SAM's and TERRY's dirty files were never at risk.**
