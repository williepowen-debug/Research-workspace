# VIOLET TRADE

VIX-linked positions and trade framework.

---

## ACTIVE POSITIONS

**None.** ✅ *Verified by `scripts/position_agreement_check.py`, not merely asserted — see the closed record immediately below. `TRY-VIOLET-VIXCS` closed 2026-07-30 **~09:50 ET**.*

---

## CLOSED — `TRY-VIOLET-VIXCS` (VIOLET thesis · TERRY structure · Will [Approve] 2026-07-27)

### 🔴 REALIZED: **−$111.60 (−38.8%)** · closed 2026-07-30 on the card's mandatory dated rule

| Field | Value |
|---|---|
| **Structure** | **4× VIXW Aug-05 20C / 25C** call debit spread (5-wide, defined risk) |
| **Fill** | **2026-07-27 ~11:35 ET** — long 20C $1.23 / short 25C $0.53 = net debit **$0.70** · **$287.70 at risk**, MAIN book |
| **Exit** | **2026-07-30 ~09:50 ET** — SELL TO CLOSE @ **$0.45 net credit** (20C 0.63 = +$248.15 · 25C 0.18 = −$72.05 → **+$176.10** returned) |
| **Realized P/L** | **−$111.60 = −38.8%** of capital at risk. **Beat the registered base case, which was a 100% loss.** |
| **Exit branch** | TERRY card §6 **base branch (ii)** — mandatory dated exit. **All three strength triggers formally graded, none fired:** VIX cash-session high **18.71** vs the ≥23 monetize-half line · **VIX3M/VIX min print 1.0888**, verified on *simultaneous* 5m bars, never <1.0 · no spike, so the SKEW tell was moot. |
| **My five stand-downs** | **ZERO tripped, start to finish.** Graded formally at the 7/29 close (KB-VIO-143) and again at the 7/30 pre-open. **The position was never killed by a thesis guard — it was closed by the clock.** |
| **★ WHY IT LOST — the entry, not the exit (TERRY's diagnosis, and I adopt it)** | **VIX options settle on the FORWARD, whose beta to spot is a FUNCTION OF TENOR — ~0.6 at our 9→6 DTE, not the 0.28 first published.** The FOMC delivered exactly the event the card was built for — VIX 17.45 → 20.88, **+13.45% settle** — and the structure **still lost**, because the forward went **19.6 (fill) → 18.82 (exit)** and moneyness **DETERIORATED from +2.0% to +6.3% OTM *after* the event we bought.** ⚠️ **CORRECTED 7/30 (TERRY self-audit + my own re-derivation): 0.28 was a LONG-tenor beta applied to a SHORT-tenor position.** My OLS on 246 daily ΔM1/ΔVIX pairs: **21–35 DTE = 0.274 · 11–20 = 0.505 · ≤10 = 0.591.** 0.28 is almost exactly the 21–35 bucket; **ours was the ≤10 bucket.** 🔑 **A beta is not a constant — quoting it as a scalar is itself a specification error (6th instance of the v3.8 family).** **I propagated 0.28 to five surfaces including two published Artifacts, on relay, without re-deriving it.** |
| **⚠️ My share of it, stated plainly** | TERRY records this as "a construction failure on TERRY's axis, **not a mark against VIOLET's vol read**." **The vol read was right and I decline the full exculpation.** The directional call paid — VIX +13.45%, first >20 settle of the episode — and the trade still lost 38.8%. **That is the Episode-17 lesson repeating: *fixed-expiry OTM options die on timing even when the signal is right*, which is written in this very file as my own registered Vehicle rule** ("match the vehicle to the open transmission channel AND the timing uncertainty"). **I owned KB-VIO-129 — spot-vs-forward — before the fill and carried the forward level on my own dashboard the whole time.** Knowing the instrument was the forward and still endorsing a 9-DTE OTM structure into a 3-day window is a **vehicle-selection** miss on my side, whoever priced the strikes. → KB-VIO-154. |
| **Pre-registered evaluation (TERRY card 11.C — registered BEFORE the outcome)** | Holding beat exiting **iff the 8/5 VIX SOQ prints >20.45**; TERRY pre-registered **P ≈ 20%**. The exit was at the market's fair two-sided price ⇒ **EV-neutral by construction**, so the 8/5 print does **not** by itself grade the exit rule (needs n>1). **What 8/5 legitimately grades: my KB-VIO-144 fade verdict, my no-re-entry call, TERRY's forward-beta finding, and HENRY's short-gamma amplification steelman.** |
| ✅ **Fill time RESOLVED ~09:50 ET — by physical evidence, 10 min after TERRY ruled it unestablished** | TERRY (11:02) recorded the clock as **UNESTABLISHED** (PROME ~09:50 vs card ~10:2x, broker record undated, TERRY's figure inferred from a 10:11 chain pull) and asked PROME for a source. **FORGE's 11:11 reconcile supplies one:** the **09:40 ET Fidelity export still carries BOTH VIXW legs live** (20C $240.00 / 25C −$104.00). That is a hard **lower bound — the fill is after 09:40** — which **refutes ~10:2x** and **corroborates PROME's ~09:50**. I withdrew my own "~10:25" earlier for being unsourced; this replaces it with a bracketed, evidenced time rather than another inference. → packet sent to TERRY. |
| ⚠️ **Execution note — WITHDRAWN IN FULL by TERRY, n=2 → n=0** | I previously carried TERRY's finding that *"Will beat me 5c in both directions, n=2 — I was pricing verticals off leg mids."* **TERRY withdrew it entirely on its third correction pass, and my own flag is what triggered the re-check.** Once the fill was established at **~09:50**, TERRY reconstructed the 09:50 mid from the 10:11 chain (spread delta ~0.175) and got **0.44–0.45 across EVERY candidate beta**: **Will filled at the 09:50 mid; TERRY recommended the 10:11 mid. Both said "mid" — there was never a divergence.** The apparent 5c edge was **entirely the 21-minute gap** between fill and marks in a ~2%/hour tape. 🔑 **The real defect TERRY names is worse than the invented one: a BEHAVIOURAL conclusion about itself, built on an INFERRED timestamp, written to durable memory and reported as measured — and its own 11:55 audit re-read that finding and left it standing, because it re-checked conclusions without re-deriving inputs.** |

> ⚠️ **THIS SECTION READ "None." WHILE THE POSITION WAS LIVE — 2026-07-27 11:35 ET to 2026-07-28 ~04:30 ET (KB-VIO-142).** Caught by a provenance audit, not by any guard. **The boot staleness check passed this file `ok +2d`** because it compares *mtime to STATUS.md* — it measures **age, not agreement**, and cannot detect a fresh file that contradicts the truth. This file has now failed in **both** directions: it carried a **dead** position as OPEN for three weeks, and a **live** position as None.
> ✅ **THE FIX EXISTS AND WAS EXERCISED ON THIS CLOSE.** `scripts/position_agreement_check.py` (PROME-built 7/28 to my spec, Will-approved `b8a5f441`) is the positive check that staleness cannot be. **KB-VIO-142 was the None→LIVE direction; this close is its first LIVE→CLOSED test, and it was run against this very edit rather than assumed** (KB-VIO-151).

**Closed:** Episode-17 (VIX May 19 25C) expired worthless 2026-05-19 — recorded below. *(Closeout recorded 6/9; this file had carried the position as OPEN for 3 weeks after expiry — caught by orchestrator review.)*

**Post-Path-B Reversion Fade: CLOSED — FALSIFIED 7/1, never entered** (see the framework section below for the adjudication). Its PRIMARY falsifier — the KB-VIO-090 ⛔[STUCK 8/4 — lines retired, see KB-VIO-187] credit tree — fired **BIN-A** on 6/25 data (KB-VIO-107), which per pre-registration is "Path A confirming, FALSIFIED, full stop." Honest calibration record: the fade's *directional* thesis paid in full (VIX 19.49 → 16.59, inside the 16–17 target zone, on exactly the reversion path predicted) — the credit switch killed a winning trade. That asymmetry is the design (credit tree outranks a paying tape); the cost is now a logged datum on the tree, pending the DISH-decomposition/LIQUID-breadth adjudication. **No new fade/short-vol framework may be constructed while Bin-A stands** (KB-VIO-096 entry asymmetry).

---

## CLOSED POSITIONS

### VIX 25C May 19 — SKEW Divergence Episode #17 (CLOSED — expired worthless)

| Field | Value |
|-------|-------|
| Instrument | VIX May 19 25 Call, long, entered 2026-04-16 (33 DTE) |
| Outcome | **Expired worthless 5/19** — VIX 18.06 at expiry vs strike 25 (6.94 pts OTM at 0 DTE) |
| Path | Trade-level invalidated Apr 23-28 (SKEW <140 4-td strict rule HIT); Will HOLD decision 5/3 as tail lottery on May 13 CPI / expiry mechanics; no tail materialized |
| Post-mortem | `research/2026-06-01_episode17_postmortem.md` — primary mechanism: positive-gamma suppression (KB-VIO-055/062) absorbing 5-6 consecutive catalysts |
| Epilogue | The underlying L1 signal class paid forward 17 days after expiry: 6/5 VIX +40% (KB-VIO-067 DIET fire 5/20-5/29 → spike at td-4). Right framework, wrong expiry window — the timing-vs-thesis lesson, and the vehicle lesson (fixed-expiry OTM calls die on timing even when the signal is right) |

---

## TRADE FRAMEWORK

### VIX Instruments

| Instrument | Use Case | Pros | Cons |
|------------|----------|------|------|
| VIX Futures | Direct vol exposure | Clean, liquid | Contango bleed, term structure risk |
| VIX Options | Defined risk, convexity | Asymmetric payoffs | Expiration timing, IV risk |
| Futures calendars (M2 vs M3) | Event-premium relative value | Not naked short-gamma; defined relationship | Both legs move; basis risk |
| UVXY / SVIX | Tactical only | Easy access | Severe decay / unlimited risk — avoid holding |

**Vehicle rule (Episode-17 + fleet TLT lesson):** match the vehicle to the open transmission channel AND the timing uncertainty. Fixed-expiry OTM options need the move inside the window; calendars and futures tolerate timing slip.

### Trade Types

| Type | Setup | Target | Stop |
|------|-------|--------|------|
| Vol spike hedge | VIX < 20, credit stress building | VIX 30+ | VIX 15 (thesis break) |
| **Sweet spot lag** | **VIX 15-26 + HY OAS >100bps** | **VIX +10pts** | **HY OAS reverses, VIX >30** |
| Credit-vol lag | HY OAS widens, VIX flat | VIX catches up | Credit reverses |
| Regime shift | Low vol → rising vol | VIX 25-30 | VIX back below 18 |
| **Event-premium fade** | **Post-event, premium hump located, substance clean** | **Hump deflates to normal contango** | **Credit confirms / vol re-extends** |

### Position Sizing

**Rule:** VIX trades are hedges, not alpha. Size accordingly. Short-premium trades: defined-risk structures ONLY, one tier lower than the equivalent long-vol conviction.

| Conviction | Long-vol max | Short-premium max | Time Horizon |
|------------|--------------|-------------------|--------------|
| Low (🟡) | 0.5% account | — (don't) | 1-2 weeks |
| Medium (🟠) | 1% account | 0.5% account | 2-4 weeks |
| High (🔴) | 2% account | 1% account | 1-3 months |
| Critical (🔴🔴) | 3% account | 1% account | Event-driven |

---

## LIVE DECISION FRAMEWORK — Pre-FOMC Defined-Risk VIX Call Spread — ✅ **RESOLVED: FILLED 2026-07-27, POSITION LIVE**

> **STAGE CORRECTED 7/28 (KB-VIO-142).** This section read **"IN CONSTRUCTION (TERRY)"** with stage *"Will approved BUILD in principle 7/25"* for **17 hours after the trade actually filled.** Will **[Approve]'d** and TERRY executed **7/27 ~11:35 ET at $287.70**. Position details → **ACTIVE POSITIONS** at the top of this file; risk controls → `STATUS.md`. The framework below is retained as the **registration record** of what was pre-committed before the fill.

**Registration record (pre-fill, unaltered).** Equity-vol expression ONLY (TRY-FIRE-004's 30× TLT Sep-30 77P owns the rates-vol leg — no MOVE-linked double-count); defined-risk call spread, never outright calls; entry window **Mon 7/27–Tue 7/28 pre-FOMC with VIX <20**; do-not-chase = VIX ≥20 settle or inversion <1.0 pre-fill (peak-marker, KB-VIO-034); strike zone from the KB-VIO-099 sub-20 ladder (long ~20-22 / short 26-30; 23-touch modal, don't pay for the ≥+50% tail at 56-60%); event-boxed with MANDATORY post-FOMC review 7/30, monetize into a ≥23 touch or inversion, no roll without fresh approval. Counter-case on the card: 0/5 absorption base rate, 7/23's sold 20.31 break, COT cushion partially rebuilt, cheap_tail DORMANT 2/4. Construction packet (canonical for constraints/exit discipline): `AGENTS/TERRY/inbox/processed/2026-07-25_from-VIOLET_CONSTRUCTION-REQ-prefomc-vix-call-spread-will-approved-build.md`.

**How it resolved against its own registration — every pre-committed condition held:**
- **Entry window:** filled 7/27, inside Mon–Tue. ✅
- **VIX <20 at fill:** 19.06–19.27 on PROME's live pulls 11:31–11:38. ✅
- **Do-not-chase:** no ≥20 settle, no inversion pre-fill (ratio ~1.07). ✅
- **Structure:** 20C/25C spread, never outright. ✅ **Strikes inside the registered zone** (long 20–22 ✅; short 25 vs the registered 26–30 — **TERRY tightened it one strike lower**, which *reduces* the paid-for tail consistent with the 23-touch-modal instruction).
- **Tenor:** 8/5 over my 8/19 lean — **TERRY's departure, argued on spike-capture and accepted.**
- ⚠️ **Rule #6 was broken and logged** — VIX calls bought on a VIX-up day. Recorded at the time; the honest epilogue is that the day **settled +0.48%**, not the +4.6% the fill-time tick showed, so **the break was measured against a tick that did not survive the close.**

---

> ⛔ **RETIRED-SUPERSEDED 2026-07-31** by the rising-vol registration design (DOCKET L163); **stood down by Will 2026-09-04 11:11 ET (WQ-177)**, PROME record `PROME/proposals/2026-09-04_wq177-RULED.md`. History below is **verbatim and unedited**; **nothing in it fires anything.** Gate A/C read PENDING against a **2026-07-02** print and are dead letters — do not adjudicate them. A tail hedge on today’s prints would be a **fresh TERRY ask on live quotes**, not a revival of this gate. *(Origin: my own KB-VIO-230 staleness finding; left untouched until the operator’s word existed.)*

## LIVE DECISION FRAMEWORK — Gated Tail-Hedge Packet (Will-approved gate, 2026-07-01 ~11:30 PM ET, flat) — **RETIRED-SUPERSEDED**

**Authorization scope (exact):** Will approved the GATE on 7/1 ("Approved on the gate — build the packet if it fires"). That authorizes VIOLET to **build and deliver the hedge packet same-session when any gate fires**. It does NOT pre-authorize execution — the packet still goes to Will for [Approve] per standing rule.

**Context:** cycle-sharpest compression-divergence (VIX 16.59 partly wings-suppressed / SKEW 154.82 fresh top-decile / credit tree in first-ever Bin-A, DISH-confounded / Path-B unwind broadened un-indexed / Fed-HIKE repricing live). Registered L1 triggers NOT fired — hence gated, not entered. Full state: STATUS 7/1, KB-VIO-106..109.

**THE GATES (any ONE fires the packet-build):**
- **Gate A — post-DISH credit persistence — PENDING (adjudicates on the ~11:30 ET 7/2 print):** the FRED print for 7/1 data shows **CCC ≥9.65 OR CCC−BB dispersion ≥8.00**. ⚠️ Composition check both ways: DISH's index-exit mechanics are unverified — a mechanically tighter print from DISH removal is not a true retrace, and a hold that still contains DISH is not clean persistence; state which case the print is before adjudicating, and if indeterminate, wait for the next print rather than force it. (DEWEY PROMPT-05 DISH-decomposition lands after this call — informs the follow-up, not this adjudication.)
- **Gate B — jobs shock — ✅ ADJUDICATED NO FIRE 7/2 (KB-VIO-111, amended 9:45 ET):** NFP +57K miss / net revisions −74K / U-3 participation artifact / AHE 3.5%↑ = stagflationary mix; tape evolved dovish-muted (8:33) → hawkish-lean-muted (9:30, 10Y 4.50 +3bp). **Zero registered anchors met under either reading** (no material hike-repricing, VIX ~16.5 flat, ES flat). MOF-strike candidate on the 8:30 bar noted (UNCONFIRMED, SAM verifies). Gate-design note: correctly did not false-fire on a non-hawkish print.
- **Gate C — LIQUID breadth — PENDING:** LIQUID's CCC mover read returns BROAD (not 3-4 idiosyncratic names) → fires regardless of A/B (the KB-VIO-098 discriminator resolving against composition). SIG delivered; LIQUID session pinged by PROME on the adjacent X1 watch.

**STAND-DOWN (all three benign):** CCC back <9.55 + jobs benign + LIQUID idiosyncratic → de-escalate to watch. Re-arm lines: SKEW >150 sustained 4td (prediction #6, count 1/4) · formal DIET/STRICT fire (VVIX = binding leg) · any new Bin-A condition.

**PACKET SPEC (pre-registered so the build is fast):**
- **Vehicle:** long VIX calls, **30-60 DTE** (Aug 19 expiry class from 7/2) — deliberately the CHEAP leg of the surface: VVIX 89 = VIX optionality suppressed, while SKEW 154.82 = SPX far-OTM put wings are the crowded/rich leg. Not SPX puts.
- **Size:** **1% account starter** (🟠 medium conviction long-vol max per sizing table). Escalation to 2% (protocol row ceiling) only if Gate C breadth AND Gate A both fire.
- **Strikes/levels:** off a LIVE INTRADAY chain at build time (evening OI prints are artifact), naming computing-spot + as-of-minute (KB-VIO-092/099/101 discipline). Ladder anchors derived from live spot at pricing time — nothing pre-committed from 16.59.
- **Entry timing:** prefer a vol-down/green-equity moment per rule #6 (calls on red days = don't chase a vol spike); if the gate fires INTO a vol-up tape and waiting sacrifices the hedge's purpose, document breaking rule #6 and why, per the rule's own note-when-breaking clause.
- **Exit/management pre-registered in the packet:** monetization/roll plan (rule #7 — roll duration, don't trim), time-box, and the standing falsification lines (VIX3M/VIX <1.0 peak-marker = monetize-into-strength signal; credit tree state changes re-adjudicate the thesis leg).

---

## LIVE DECISION FRAMEWORK — Post-Path-B Reversion Fade (pre-registered 2026-06-23, flat) — **CLOSED: FALSIFIED 7/1**

**ADJUDICATION RECORD (7/1, KB-VIO-107):** The PRIMARY falsifier fired in the 6/24–6/30 dark window — CCC crossed 9.55 on the 6/23 print (9.56), the A-escalator (9.68 ≥9.65) and A3 dispersion (8.01 ≥8.00) fired on 6/25 data, A2 touched 6/26 (BB 1.73). **BIN-A = framework FALSIFIED full stop, never entered.** The Micron fork itself resolved ambiguously (MU cleared 6/24-6/25, then the sector relapsed 6/26 and again 7/1 — the fork's "cleared" state lasted one session). Tape epilogue: VIX did revert 19.49 → 16.59, inside the 16–17 target — the directional call paid, the credit switch killed it anyway, correctly per registration. Cost datum logged on the tree (single-issuer DISH distortion = refinement candidate, NOT retro-applied). Entry gates remain dead while Bin-A stands.

*Original framework retained below for the registration record:*

**The decision that opens after Micron 6/24.** Pre-registered while flat so the entry is disciplined, not improvised by the tape. This is VIOLET's current "fade the VIX" trigger — it supersedes the (now-closed) Event-Premium Fade below, but reuses that section's still-valid falsification architecture (credit 2-bin tree / n=5 tail-stop / time-box).

**Thesis:** the 6/23 VIX +12.8% to 19.49 was the Path-B coiled-spring's FIRST partial-fire (KB-VIO-105) — a contained, ORDERLY semis/AI positioning unwind (KOSPI / SK-Hynix HBM shock), NOT broad risk-off, credit, oil, or rates (breadth held, credit tight, OVX fell, yields eased, vol structure orderly). Base rate: an orderly sub-20 vol pop on a single-sector shock mean-reverts (~2/3 back toward 16-17 within 1-2 weeks). The fade harvests that reversion + the re-steepening contango — but ONLY once the binary that can re-light it (Micron) clears and the front rolls over. Entering before that = short vol into the negative-gamma + record-leverage tail the night before a ~17%-implied AI bellwether = the textbook bad short-premium add.

**THE FORK — Micron 6/24 AH decides which branch activates:**
- **MU holds / relieves** (no semis follow-through gap-down) → this **reversion fade ARMS**.
- **MU breaks** (semis make new lows, unwind re-accelerates) → **fade DEAD**; the OTHER branch — a small long-vol/tail hedge (HEDGING PROTOCOL, "geopolitical/▲event live" row, sized 🟡) — activates instead. Do NOT fade a re-accelerating unwind.

**Entry gate (ALL required; initiate ONLY on a vol-DOWN / green day — never sell vol on a red day, per the puts-green/calls-red rule):**
1. **Micron cleared without re-igniting** — 6/24 AH earnings past AND semis stable-or-up the next session (SOX/MU/NVDA not making new lows; HENRY read).
2. **Vol rolling over** — VIX back below ~18 (confirming reversion off 19.49), on a green-equity / down-VIX day.
3. **Front premium draining** — VIX9D/VIX back below ~0.95 (front hump deflating; 1.00 now) AND/OR VIX3M/VIX contango re-steepening toward ≥1.10 (flattened to 1.081 on the spike). Re-steepening contango is what the fade actually harvests.
4. **No new fragility fire** — credit still clean (CCC <9.55, no Bin-A; fine now); OVX not re-bidding; SOXL/SOXS flows stabilized; no fresh AI-name shock.
5. **6/30 month-end managed** — the ~$165B rebalance into negative gamma is a within-horizon amplifier: ENTER AFTER 6/30 passes cleanly (preferred), or take ≤50% size before it.

**Structure (defined-risk / non-naked-short-gamma ONLY — sizing rule above):**
1. **Primary: short-front vs long-back VIX futures calendar** (short M1/Jul vs long M2/Aug) — collects the front-hump deflation as contango re-steepens; back leg hedges parallel shifts; not naked short-gamma. Re-quote the live spread at entry (M1:M2 +6.54% on the 6/22 settle).
2. **Alt (fully defined risk):** a VIX call credit spread (sell near-the-money, buy higher), max-loss = the risk budget; or a long VXX/UVXY put spread (decay tailwind, defined risk).
3. **NOT:** naked short VIX futures, short straddles/strangles, SVIX holds.

**Sizing:** short-premium into a fragile (Path-B-fired) regime → **starter ≤0.5% account, defined-risk** (one tier below equivalent long-vol). Scale only after reversion confirms AND the leverage/negative-gamma overhang has worked off.

**Target / time-box:** VIX reverts toward the pre-spike base **~16-17** / contango back to normal. **Time-box ~2-3 weeks** — comes off by the registered window whether or not fully deflated (grind-failure class); no extension without a written re-underwrite.

**Kill / falsification (any one → don't enter, or exit if on) — reuses the registered architecture from the closed framework below:**
- **Micron breaks the tape** (pre-entry) → fade dead, flip to the tail/hedge branch.
- **Credit (PRIMARY):** CCC ≥9.55 → 2-bin tree (KB-VIO-090 ⛔[STUCK 8/4 — lines retired, see KB-VIO-187]); any Bin-A (HY ≥2.85 / BB ≥1.73 / CCC−BB ≥8.00 / CCC ≥9.65) → Path A confirming, FALSIFIED, full stop.
- **VIX >23 close-and-hold n=5** (tail-stop, KB-VIO-088; counter 0/5).
- **VIX3M/VIX inverts** (<1.0) → peak/stress being priced, no fade.
- **VVIX >120** → vol-of-vol stress, no fade.
- **Second Path-B leg** (semis new lows / fresh leveraged-ETF reversal / AI-name shock) → unwind live, not a fade.

**Spot-conditioned kill levels derive AT pricing time (KB-VIO-099)** — do NOT hard-code a stale VIX level; set the structure's strikes/stop when the trade is actually priced, naming the computing-spot + as-of date.

**Approval:** structure + size goes to Will before any execution. This pre-registers the conditions; it does NOT pre-authorize the trade.

---

## LIVE DECISION FRAMEWORK — Event-Premium Fade (M2/Jul into FOMC) — NEW 6/9 · **CLOSED 6/23**

**STATUS: CLOSED — window passed, never entered.** Gates failed twice on 6/10 (CPI/Iran); the BOJ 6/16 + FOMC 6/17 catalyst window then resolved benignly (absorbed, counter 0/5). Superseded by the Post-Path-B Reversion Fade above. **Retained for its falsification architecture** (credit 2-bin tree KB-VIO-090 ⛔[STUCK 8/4 — lines retired, see KB-VIO-187], n=5 tail-stop KB-VIO-088, time-box, ladder KB-VIO-099) — which the new framework references rather than re-deriving.

**The decision that opened post-CPI 6/10.** Framework written BEFORE the print (8:30 ET 6/10) so the entry is pre-registered, not improvised.

**Thesis:** the 6/5 NFP spike left an event-premium hump, located (convexity_read 6/9) at the VIX9D kink (+2.27 over spot) and the M1:M2 contango (+7.50% adj). Both fade legs (rate-shock, AI-unwind) are deflating; credit never confirmed. If CPI passes non-tail, the remaining premium is fade-able into/through FOMC 6/17.

**Structure (priority order):**
1. **Short M2 (Jul) vs long M3 (Aug) futures calendar** — collects the Jul event-hump deflation post-FOMC; M3 leg hedges parallel vol shifts; not naked short-gamma. Relevant carry is the **M2:M3 spread: +4.00%** (VX/N6 20.14 exp 7/22 → VX/Q6 20.95 exp 8/19, CBOE settlement 6/8) — about HALF the M1:M2 +7.5% hump this doc previously implied; re-quote at entry. *(Corrected 6/9 late — orchestrator flag: prior text quoted the Jun/Jul spread for a Jul/Aug structure.)*
2. Alternative (defined risk): Jul VIX call credit spread sized to max-loss = the position's risk budget.
3. **NOT:** naked short VIX futures, short straddles, SVIX holds.

**Entry gate (ALL required, post-print):**
1. CPI non-tail — front collapses (VIX9D/VIX ratio decisively off 1.114 toward ≤1.05; M1 deflates)
2. Credit stays clean — HY <2.85, CCC <9.55 (VIOLET range-break level — NOT a LIQUID line, mis-attribution corrected 6/11; LIQUID's CCC threshold is 1000bp. FRED T+1 check). **GATE×TREE INTERACTION — registered 6/11 evening, flat and pre-tape (KB-VIO-096): an unresolved Bin-B state BLOCKS new entry even though it does not falsify the framework.** Entry asymmetry is deliberate: entering requires stricter evidence than not-exiting. The Bin-B block lifts on the FIRST of: (i) any official CCC print back below 9.55 (gate 2 re-passes as written); (ii) the +5td re-check (6/17 data) resolving clean (breadth clean AND CCC <9.65) — at which point the line re-marks upward in writing and **gate 2's threshold re-marks WITH it** (the gate and the tree must always reference the same line — one source of truth; a re-marked tree with a stale gate recreates this exact ambiguity). Any Bin-A condition during the window = gate 2 fails outright, entry dead this cycle. No improvised "9.5x is basically fine" calls inside the window.
3. AI-unwind leg not re-extending — NVDA/SMH stable-or-up post-print (HENRY read)
4. `convexity_read.py` post-print still locates a rich hump worth selling (M2 premium vs M3 above normal)
5. BOJ 6/16 risk priced: enter ≤50% size before BOJ, or wait until 6/16 post-MPM for full size

**L1-stack tension (state it, don't hide it):** the 5/20-5/29 DIET fire's fwd-60 window runs through **~Aug 12-21** (60 *trading* days from each fire day — the backtest's unit). At the ≥+15% tier it is RESOLVED (6/5 peaked +40%); at the ≥+50% tier (60% episode base rate, L1 canonical table) the window is **still live** — a second leg to VIX ~25+ remains a priced tail. *(Corrected 6/9 late — orchestrator flag: prior "~8/4" was 60 calendar days from the spike: wrong anchor AND wrong unit, would have lifted the size cap ~2 weeks early. The KB-VIO-079 error class, caught in the same session that canonized it.)* This is why size is capped, risk is defined, and the BOJ split-entry exists. Short-premium here fades the *event hump*, not the L1 signal class.

**Adjudication record:** 6/10 AM post-CPI: **GATE FAILS #1** (gate 1: ratio ~1.15 vs ≤1.05; Iran third leg re-armed the front — KB-VIO-081). 6/10 EOD: **GATE FAILS #2** (ratio 1.145 close-basis; M1:M2 +7.98% re-armed; Iran escalation sustained per WALTER/HAWK; credit clean but CCC 9.51 = 4bp from gate-2 flip). NO ENTRY. Framework alive — invalidation not triggered (VIX closed 21.86 < 22.24 overnight peak < 23). Re-adjudicate 6/11+; realistic next entry window is post-6/17 FOMC, and only on Iran stabilization. KB-VIO-086.

**Invalidation / exit — falsification weight REGISTERED 6/10 evening (CHG-RED-033 adjudication, KB-VIO-088). Where falsification lives, stated explicitly: credit tripwires PRIMARY · time-box catches the grind-failure class · VIX close-and-hold is a TAIL-STOP only · BOJ-hawkish is the channel exit. No spot-VIX touch falsifies anything inside the L1 window — that is by design, and now said out loud.**

- **Credit tripwires → PRIMARY falsifier** (credit confirming is the cleanest event-premium vs regime-break discriminator). **HY >2.85 → exit immediately.** **CCC ≥9.55 → adjudicate through the pre-registered 2-bin tree (KB-VIO-090 ⛔[STUCK 8/4 — lines retired, see KB-VIO-187], registered 6/11 AM before the FRED 6/10 print): Bin A (cross + breadth: HY ≥2.85 / BB ≥1.73 / CCC−BB ≥8.00 within 5td, or CCC ≥9.65 escalator) = credit confirms, framework FALSIFIED, full stop. Bin B (cross + HY/IG/BB flat + dispersion <8.00) = composition artifact — MARGINAL-FAIL, no re-arm, re-check +5td, then re-mark the line in writing if still clean.** Provenance corrected 6/11: 9.55 is a VIOLET June-range-break level (episode high 9.52 + 3bp), not breadth-derived and not LIQUID's (theirs = 1000bp). Full tree: `research/2026-06-10_red_sweep_response.md` § CHG-RED-035.
- **TIME-BOX: an entered position comes off by its registered take-off window (post-FOMC target: 6/18-6/22) whether or not the hump has deflated** — no extension without a written re-underwrite. This clause carries the 2024-12 failure class: the one destination-wrong analog failed at the window END, not on mid-window run-length (its max run reads 2→4→7 as the window edge slides Mar 4→Mar 11) — a time-box catches that; a run-counter cannot.
- **VIX >23 close-and-hold: n = 5 consecutive closes** (registered 6/10 evening; derivation `scripts/sustain_run_query.py`, reconciled exactly vs Orch answer key: max run above the +50% line in destination-right analogs = 4 [2023-09], n = one above). **Role: TAIL-STOP, not failure-catcher** — run-length has NO discriminating power between fine-retest and fatal re-arm (dest-right 2023-09 and dest-wrong 2024-12 both ran exactly 4); n=5 fires only on paths worse than any precedent in the 13-yr episode set, bounding unprecedented re-arming. Honest note: ambiguous 2014-11 ran 7 — n=5 fires mid-window there at VIX +50-95% over base, a defensible kill regardless of its +15% end. A 23-touch remains the MODAL path (6/6, KB-VIO-082), expected and non-disqualifying. **Entry-structure corollary — RE-DERIVED 6/12 (KB-VIO-099, supersedes KB-VIO-089 spot-conditioned clauses; raw historical rates stand at 11/19, 9/19, 9/19, 8/19 for 23/24/25/26): the "budget zone 24-25" framing was bound to a near-peak entry (spot ~22 → 24-25 = +8-12% modal retest) and DOES NOT translate to a sub-20 entry by re-marking distances. From spot 19.04-19.44, hitting 24-25 requires +24-31% — that is approaching tail, not budget. RETIRED clauses: "23 near-spent" (now +18-21% away), "budget zone 24-25", "26 no longer comfortably outside." NEW rule: sub-20 entries derive entry-anchored kill levels at pricing time, not pre-registered against a hypothetical. Quote discipline strengthened: every ladder use names its computing-spot AND as-of date alongside the two anchors (KB-VIO-092 family).**
- BOJ 6/16 hawkish-of-pricing (carry-unwind channel opens, SAM signal) → exit or cut to runner before FOMC
- **Vol-side structural falsifier — DEFERRED, not registered:** the structure-native kill (M2:M3 spread inverting and HOLDING — the spread the trade is actually short) is cleaner than any spot level, but its sustain-n needs the same empirical derivation and that requires historical CBOE VX settles the toolkit doesn't have wired. Until that data work lands, the register is credit + time-box + n=5 tail-stop — do NOT treat M2:M3 as if registered. *(RED's candidate — VIX3M/VIX inversion ≥7td — declined: KB-VIO-034 tension; inversion marks peaks, so sustained inversion plausibly marks the moment before the fade PAYS.)*
- Target: hump captured (M2:M3 back to normal contango) post-FOMC — the time-box take-off window, don't overstay

**Approval:** structure + size goes to Will before any execution, per standing rule. This framework pre-registers the conditions; it does not pre-authorize the trade.

---

## THESIS TRADES (Standing)

### Credit-Vol Lag Trade (Four-Model Framework)

**Thesis:** When HY OAS widens >100bps from recent low and VIX < 20, VIX will spike >10pts within 2-6 weeks (70% hit rate, 25-30% false positive).

**Setup (All must be true):** HY OAS +100bps from recent low · VIX < 20 at onset · cross-sector widening · yield curve NOT inverted · no active Fed QE backstop
**Entry:** VIX calls 30-60 DTE (checks 1-3) / 60-90 DTE (all 5)
**Target:** VIX catches up to credit-implied level (HY OAS × 7.6 + 158 = implied VIX)
**Stop:** HY OAS reverses >50bps, VIX >30, or curve inverts
**Sizing:** 1% (medium) / 2% (all 5 checks)
**Status:** DORMANT — **HY 2.79 [7/24 FRED]**, nowhere near the +100bps trigger. *(Was "HY 2.75 (6/8)" — a 7-week-stale naked number, refreshed in the 7/28 audit.)*

### DIET / STRICT Coiled-Spring Trade (L1 population signal)

Owned by `thesis/VIX_THESIS.md` § The DIET Coiled-Spring Trade — setup, tiers, and the **L1 canonical base-rate table (KB-VIO-079)** live there; this file does not duplicate them. Sizing rule of thumb: quote the base rate at the threshold the structure actually needs (≥+15%: 92-94% episode-level; ≥+50%: 56-60%) — far-OTM strikes price off the lower number.
**Status:** 5/20-5/29 DIET fire paid forward 6/5 (+40% at td-4). No new fire since.

### Term Structure Inversion (REVISED v3.1)

Inversion (VIX > VIX3M) **marks vol peaks, not onsets** (KB-VIO-034: 553 events, 2.2% hit rate). Use for **exit timing on long vol**, never entry.

---

## TRADE LOG

| Date | Instrument | Action | Size | Entry | Exit | P&L | Notes |
|------|------------|--------|------|-------|------|-----|-------|
| 2026-04-16 | VIX May 19 25C | BUY | — | — | — | — | SKEW divergence Episode-17. 33 DTE. Central case VIX 25-30. |
| 2026-05-03 | VIX May 19 25C | HOLD | — | — | — | — | Trade-thesis invalidated (4-td rule hit Apr 23-28); HOLD per Will = tail lottery. |
| 2026-05-19 | VIX May 19 25C | **EXPIRED WORTHLESS** | — | — | 0 | −100% of premium | VIX 18.06 vs strike 25. Post-mortem: `research/2026-06-01_episode17_postmortem.md`. *(Log row added 6/9 — was missing.)* |
| **2026-07-27** | **VIXW Aug-05 20C/25C spread** | **BUY (open)** | **4 spreads** | **$0.70 debit** (20C 1.23 / 25C 0.53) | — | **OPEN** | `TRY-VIOLET-VIXCS`. $287.70 all-in, MAIN. Will [Approve] ~11:35 ET. Thesis gate = HENRY short-gamma. **Mandatory review 7/30.** Rule #6 break logged (calls on an up-VIX day). *(Log row added 7/28 — **was missing for 17 hours**, KB-VIO-142.)* |

*P/L figures are placeholders — cost basis per Will, not authoritative from state files. **Open-position marks are TERRY's**; this log records the fill, not the mark.*

---

## HEDGING PROTOCOL

| Condition | Hedge Size | Instrument |
|-----------|------------|------------|
| Portfolio +20% from lows | 1% VIX calls | VIX calls 60 DTE |
| Credit spreads widening | 1-2% VIX calls | VIX calls 30-60 DTE |
| VIX < 15 (complacency) | 0.5% VIX calls | VIX calls 90 DTE |
| Geopolitical event live | 2% VIX calls | VIX calls 30 DTE |
| Term structure inversion | 1% VIX futures | Front month |

---

*Created: 2026-04-12*
*Last Updated: **2026-07-28 ~04:35 ET — PROVENANCE AUDIT (Will-directed), and this file was the worst surface in the domain.** 🔴 **`ACTIVE POSITIONS` read "None." for 17 hours while `TRY-VIOLET-VIXCS` was live with $287.70 at risk and a mandatory review 2 days out** (KB-VIO-142). Also fixed: the Pre-FOMC framework still said **"IN CONSTRUCTION (TERRY)"** after the fill; the **TRADE LOG had no row** for the position; the credit-vol lag trade carried **HY 2.75 (6/8)**, seven weeks stale. **The boot staleness guard passed this file `ok +2d`** — it compares mtime to STATUS.md, so it measures **age, not agreement**, and is structurally blind to a fresh file that contradicts the truth. **A position surface needs a positive check** ("if STATUS shows a LIVE position, TRADE.md must name it") **— queued, not built.** Note the symmetry: this file previously carried a **dead** position as OPEN for 3 weeks, and has now carried a **live** position as **None** — both failure directions have occurred, so it does not self-correct.*

*Prior: 2026-07-25 (NEW live framework: Pre-FOMC Defined-Risk VIX Call Spread — Will-approved build-in-principle, TERRY constructing, final [Approve] on live Monday quotes; canonical packet in TERRY's inbox. Prior: 2026-07-02 body content — Gate B NO-FIRE adjudication et al.; footer date corrected 2026-07-11 per DAEDALUS L4 packet #6, no substantive body change today). **⚠️ Staleness pointer (2026-07-11):** the KB-VIO-110 tail-hedge gate and its VIX-calls 30-60 DTE vehicle spec in the body were ruled **LAPSED by Will 2026-07-09** — the vehicle spec is RETIRED; any re-opened hedge is rates-vol/duration-shaped (TERRY lane). See STATUS.md GATE TRACKER + KB-VIO-113 + `research/2026-07-11_move-led-vol-hedge-fresh-look.md` (registered fire/no-fire conditions). Body gate-sections not yet rewritten — proposed follow-up. Prior entries: 2026-07-01 Reversion Fade CLOSED — FALSIFIED by first-ever Bin-A fire, KB-VIO-107 — no fade/short-vol constructible while Bin-A stands; 2026-06-23 PM Reversion Fade pre-registration.)*
