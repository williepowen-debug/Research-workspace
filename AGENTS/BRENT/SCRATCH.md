# BRENT SCRATCH — Thu Aug 27, 2026 **~09:0x ET** *(PROME-doorbelled spawn on the domain state change; TRADE.md mark refresh pending at 09:30 options open)*

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴 THE DOMAIN STATE CHANGED WHILE I WAS DARK — IRAN-OMAN INTERIM HORMUZ FRAMEWORK FINALISED 8/26, BRENT −8.5% IN THREE SESSIONS
>
> **Path:** 94.39 [8/21] → 92.17 [8/24] → 88.58 [8/25] → 86.36 [8/26] = **−8.5% aggregate**; biggest single day 8/25 (−3.9%) landed **BEFORE the 8/26 statement** — market priced the DIRECTION of talks, not the document.
>
> **Live tape 08:37 ET (named contracts per L23):** BZV26 (Oct M1) $88.26 · BZX26 (Nov M2) $87.27 · BZZ26 (Dec M3) $85.25 · **M1−M3 +$3.01 backwardated but FLATTENED $1.35 vs 8/24 (+4.36) ⇒ prompt scarcity easing alongside the level.** OVX 46.83 (−7.5% vs 50.62 [8/21]) · VIX 14.94.
>
> **$100 posture:** fired 7/23, was ~$6.22 AWAY [8/21], **now ~$13.75 AWAY** on BZV26 = 15.6%. **First time since 7/23 the line has widened materially without a supply-side fault appearing.** Threshold did NOT move, distance more than doubled.
>
> **BZ=F rolled Oct→Nov somewhere 8/24-27** — WALTER's $86.36 vs my $87.84 on BZ=F is a contract-basis delta, not a data error. **Reporting rule this session forward: NAME THE CONTRACT.**

---

## ✅ WHAT SESSION DID *(this session)*

**① REGIME VERDICT DELIVERED — STATUS block landed at top of file with 5 new current-state rows:** state change + decomposition + $100 posture + tape + JWC clean. PROME's regime-verdict ask (①) answered on-artifact, not just in a packet. Decomposition into 4 drivers with a bound (not precision) on the diplomatic/narrative share as load-bearing.

**② JWC WATCH RAN CLEAN — JWLA-034 remains newest.** Probed via `instrument_check.py --id KILL-LEG2-JWC-LISTING` AND direct curl of IUA index (HTTP 200, 79KB, JWLA-025→JWLA-034 present, nothing newer). Standing negative holds; **the row did what it was built to do on its FIRST meaningful test** — a diplomatic joint statement is a market-decision document, not an underwriter's verdict, and the JWC didn't move.

**③ 6 INBOX PACKETS CONSUMED, board_log rows 245-251:** PROME S338 (energy carve-out = UNKNOWN-AT-PRIMARY, carry forward not-asserted); MIDAS retraction (nothing owed); TERRY row-58 reordering (RISK_RULES #21+#22 landed, honest §4 answer sent); LIQUID §3 (no post-closure energy-HY figure on my desk, 8/07 retirement reasoning matches, packet sent to record UNMEASURED); WALTER Perm (extends v5.6 distillate mechanism, no threshold moved); WALTER Iran-Oman (the state change, verified at artifact, drove this session's STATUS write). DAEDALUS boot-load stays deferred on its own condition (TRADE.md cut still partial).

**④ REPLIED SAME SESSION to LIQUID §3 + TERRY §4.** LIQUID: their 6/30 183bp is freshest anywhere; systemic-credit leg deferred to LIQUID; refuted substitution. TERRY: no thesis-break instrument at defensible base rate TODAY (using their own escape); row-58 construction validated by the −8.5% stress (thesis-break rail correctly silent, profit-keyed would have ratcheted). Both packets under `AGENTS/<they>/inbox/`.

**⑤ PROME PACKET DELIVERED PRE-OPEN** to `PROME/inbox/` (not `AGENTS/PROME/inbox/` — the dead-path guard on my desk since 7/30 held). Regime verdict + decomp + $100 posture + JWC clean + owed items. Delivered BEFORE 09:30 open so PROME has it without waiting on mark refresh.

**⑥ CATALYSTS.tsv +1 row:** 2026-10-10 modeled midpoint for the 30-60d permanent-route window (~2026-09-25 to ~2026-10-25). Registers three branches: US-endorsed permanent route / Oman-only permanent route / window lapses. Grades against joint statement, not delegate sourcing (L18).

**⑦ NEXUS_BRIEF re-cut with C6 SCOPED-PARTIAL boundary explicit.** Top block is 8/27 content-re-verified; everything below is 8/21 vintage NOT re-verified against the 8/26 impact. Named the amendment to the 8/21 "corridor question... IS NOW CLOSED" language: it was correct AT 8/21 but is complete only if one adds "until JWLA-035+ delists" (JWC probed clean, so still valid, but the framing needs the guard).

## ⏳ WHAT'S OWED — inside this session

**⑧ TRADE.md MARK REFRESH at 09:30 open.** Four legs need live-chain marks: USO Oct-16 135C ×2 (Will-ruled SELL-ONE unfilled 8/21), USO Sep-18 150/165, XLE Sep-30 65C. **May surface a mark-driven Will decision on the remaining 135C** (post-open packet to PROME if so).

**⑨ Git commit + safe-push.** Path-scoped `AGENTS/BRENT/` + shared-log carve-out (`AGENTS/BRENT/inbox/processed/` moves + board_log + this SCRATCH + STATUS + NEXUS_BRIEF + CATALYSTS + the three outbound packets). Auto-push per closeout protocol.

## 🆕 LATE-SESSION ADDITIONS *(11:12-11:2x ET, after the STATUS write)*

- ✅ **Will's HOLD RULING on 135C ×2 encoded (PROME relay 11:12).** *"I want to wait. I do think this ride isn't over yet."* Fill status = CONFIRMED UNFILLED, SELL-ONE SUPERSEDED. Leg no longer carries fill-status question. Mark-tracking continues at ±$1.50/contract threshold vs 8/26 last-trade $5.70.
- ✅ **PROME cross-roll certification packet delivered.** Certified BZV26 like-for-like 8/21→8/26 = **−$6.55 / −6.94%** (NOT −8.5%). Cross-roll ruled out for the window (BZ=F was Oct-basis through 8/26; roll happened overnight 8/26→8/27). WALTER endpoint discrepancy $86.36 vs my $87.84 = source issue, not roll issue — reconcile owed to WALTER.
- ✅ **Ticker sweep (PROME-requested MIDAS-parallel):** 8 registered MKT-BZ-F-* / MKT-CL-F-* level rows all safe by explicit L23-compliant design; 1 DIESEL-CRACK spread row has ruled t-4 net-change basis — deeper look someday, not urgent. No re-registration needed.
- ✅ **L26 encoded** (pathspec-rename discipline, C2-clean same-commit prose+index).
- ✅ **TERRY refiner-construction ask delivered.** Will asked "should I buy more USO"; my answer: no on USO, yes on thesis, better via refiner name (VLO/MPC). Will: *"loop TERRY in on a VLO/MPC construction."* Packet at `AGENTS/TERRY/inbox/2026-08-27_from-BRENT_construction-ask-refiner-add-*.md` provides thesis fit, refiner-vs-XLE decoupling data (+14-17% 30d vs +5.4%), concentration constraints, timing/tenor/instrument menu. **Construction stays TERRY's; nothing armed.**
- ✅ **Deep (b) equilibrium analysis delivered to Will.** Verdict: NOT converged on $88-90 as equilibrium. ~55% probability temporary dip (retracement to $90-95 within weeks), ~30% probability equilibrium holds, ~15% probability continuation to $82-85. Bias check: I'm long, my prior favors thesis; without the 8/27 curve-bounce data point my probabilities shift to 35/50/15 — still against equilibrium but weaker. Will agreed with the temporary-dip framing.

## NEXT SESSION (dated, future-verifiable)

1. **🔴 FRI 8/28 DUAL GRADE:** BRT-26 Baker Hughes rigs (~13:00 ET; fires on RISE to ≥457; last 452 [8/21]) + COT vintage #3 as-of 8/25 (~15:30 ET). **DO NOT LET COT STACK past next Fri.** Grader is READY per 8/21 verification (rc=3 WAIT was healthy at 13:18 ET last Fri). BH primary path repaired 8/21 (browser UA fix), instrument check clean this boot.
2. **🔴 30-60d PERMANENT-ROUTE WINDOW** — starts ~9/25. Registered CATALYSTS row 2026-10-10 modeled midpoint. Watch for: WSJ/Bloomberg joint announcement, Oman News Agency corroboration, US endorsement/rejection statement.
3. **🔴 OPEC+ MEETING 9/6** — Q4 (Oct-Dec) decision, spare-capacity single-agency caveat (EIA STEO alone), Bloomberg 7/28 pause expectation is UN-REFRESHED (row updated 8/21).
4. **🔴 RUSSIA DIESEL BAN 9/1** — producer-direct carve-out takes effect.
5. **⏸️ WILL-GATED:** the remaining `USO Oct-16 135C ×1` disposition (post 09:30 mark refresh may re-open the second SELL question); DAEDALUS boot-load cut TRADE.md half (five sections left, do NOT rotate by heading).
6. **🟠 12 ACTIVE INCIDENTS + 6 unbudgeted still past 60d re-verify budget** (boot instrument-check flags; no action forced, disclosure honest).
7. **🟠 BRT-29 mechanism deadline is 8/31 — 4 days** (from 8/27). Its leg needs ≥3 NAMED carriers citing fuel/war economics. ⛔ Do not substitute off-list evidence.

## OPEN THREADS / WATCHES

- **⛔ SHARPEST EXPOSURE (v5.7):** the 8/21 framing named this closed; the 8/26 framework tested it and the JWC held. But: an Oman-track permanent-route agreement WITHOUT US endorsement could reprice again on nothing but a signature. Watch US State Department for endorse/reject statement on the Iran-Oman framework.
- **⚠️ BZ=F ROLL CAUGHT ONE VINTAGE DISPARITY BUT MORE MAY BE OUT THERE** — for the 8/24-27 window, any BZ=F delta may mix Oct+Nov contracts. This applies to competing figures on other desks; if I see a Brent close disagreeing with WALTER or FALCON by ~$1-2, ASK THE CONTRACT BEFORE ARGUING THE PRICE.
- **⚠️ S338 Canadian energy-lines status = UNKNOWN-AT-PRIMARY** (per PROME 8/22 ruling). Do not re-assert exclusion NOR inclusion. Watch for HTSUS annex line-list release (was `[TIFF OMITTED]` in the FR text; CBP CSMS returns 403 to this fleet per PROME).
- **⚠️ Russian capacity-offline estimates disagree ~2.5× — DO NOT AVERAGE.** Reuters 17% (conservative live) · S&P 7 offline end-July +4 in Aug (cleanest count) · Kyiv Post 42.7% CUMULATIVE-EVER-STRUCK belligerent-aligned.
- **⛔ EXPORT-SIGN WARNING live · RUNS-DECLINE IS NOT CAPACITY-OFFLINE · every 8/19-20 Russian strike item is "fire reported" or CLAIMED with ZERO operator statements — do not convert into barrels.**
- **⛔ Unresolved:** Petroline 5 vs 7 mb/d · SPR floor 252.4M vs 400.0 · Yanbu↔Sidi Kerir double-count seam · TANECO incrementality · Mina Al-Ahmadi capacity 346k (reporting) vs 466k (ledger).
- **⚠️ TRADE.md has still not been re-marked since 8/21 14:2x — the very defect PROME flagged 8/21 (11-day stale marks class). Being fixed at 09:30 this session.**

## POSITION DECISIONS PENDING

- ✅✅ **8/27 ~11:12 ET WILL RULED VIA PROME RELAY: 8/21 SELL-ONE SUPERSEDED BY DELIBERATE HOLD ON `USO Oct-16 135C ×2`.** Verbatim: *"I want to wait. I do think this ride isn't over yet."* Fill status = CONFIRMED UNFILLED. **This is thesis-conviction HOLD with concentration flag standing, NOT a lapsed order and NOT a re-open of the roll question.** The leg NO LONGER carries fill-status as an open item. **Mark tracking continues** — packet PROME on material moves ≥±$1.50/contract from 8/26 last-trade $5.70 either direction. **Congruent with my (b) equilibrium analysis this session: Will's HOLD implicitly bets on my ~55% retracement branch, not the ~30% new-equilibrium branch or the ~15% continuation-lower branch.**
- ✅ **HOLD the second 135C, no roll (Will 8/21).** Rationale: every live catalyst fires BEFORE Oct-16. Roll bought 63 days with ZERO live catalysts.
- ✅ **35 USO shares HOLD (Will 8/18).** Basis $121.88 vs USO $127.35 [8/26 close] = +4.5% (giveback from +11.3% peak 8/21). No live stop. Row-58 construction: profit-keyed = primary rail (would have ratcheted); thesis-break = backstop (correctly silent).
- ⚠️ **XLE Sep-30 $65C ×2 — 34 DTE, moneyness now depends on 09:30 mark.** Disposition LAPSE unchanged.
- ⚠️ **USO Sep-18 150/165 spread — 22 DTE, deep OTM given USO $127.35.** Disposition unchanged.

## MAIL STATE

- **INBOX 1 OPEN (DAEDALUS deferred, own condition) · WALTER lane 0 · outbox 0.** board_log **251** rows (was 244; +7 this session).
- **SENT THIS SESSION (3):** LIQUID (energy-HY UNMEASURED reply, §3 answered) · TERRY (row-58 §4: no thesis-break instrument at defensible base rate today) · PROME (regime verdict + decomp + $100 posture + owed items).
- **Owed TO me:** Will — remaining 135C disposition (may re-open post-09:30 mark). DEWEY — `gie_pull.py` (from 8/21). HAWK — the three 8/21 asks (unchanged, not blocking this session).
- ✅ **6 packets consumed and `git mv`'d to processed/** — PROME S338, MIDAS retraction, TERRY row-58, LIQUID §3, WALTER Perm, WALTER Iran-Oman.

## 📒 LEDGER-NUDGE DISPOSITION *(pending closeout run)*

| Ledger | Disposition |
|---|---|
| **`TRADE.md`** | ✅ **REFRESHED 08:35 ET via 8/26 last-trade prints (options market pre-open)** — new LIVE-VINTAGE COMPANION table added, 8/21 table untouched. **Book NOW `−$611.23 / −9.5%` vs basis (was `+$837.62 / +13.0%` [8/21 14:2x]) — swung `−$1,448.85` in 6 sessions.** Undefended-linear share `65.2% → 76.4%`, exactly the 8/21 STAR note's predicted reversal on the way down. **DECISION-RELEVANT: 8/21 SELL-ONE ruled at mid $10.35, 8/26 last-trade $5.70 — if unstaged, ~$465/contract of harvest opportunity has degraded.** Follow-up packet sent to PROME. |
| **`INCIDENTS.tsv`** | ⏸️ NOT touched this session (no new strike events verified at primary; existing 12 ACTIVE + 6 unbudgeted stay past 60d budget per boot flag). |
| **`REGISTRY.tsv`** | ⏸️ NOT touched this session (no new registrations, no level changes). |
| **`LESSONS_INDEX.tsv`** | ⏸️ NOT touched this session (no new lesson coined; the "NAME THE CONTRACT" reporting rule from the BZ=F roll is a candidate for L26 if it reifies — flagged, not authored). |
| **`board_log.tsv`** | ✅ **REFRESHED** — 244 → 251. |
| **`docket/CATALYSTS.tsv`** | ✅ **REFRESHED** — +1 row (permanent-route window). |
