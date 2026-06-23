# VIOLET TRADE

VIX-linked positions and trade framework.

---

## ACTIVE POSITIONS

**None.** Episode-17 (VIX May 19 25C) expired worthless 2026-05-19 — closed out below. *(Closeout recorded 6/9; this file had carried the position as OPEN for 3 weeks after expiry — caught by orchestrator review.)*

**Pre-registered, NOT entered (pending Will approval):** **Post-Path-B Reversion Fade** — see LIVE DECISION FRAMEWORK below. Arms only AFTER Micron 6/24 clears without re-igniting the semis unwind, on a clean reversion setup. Defined-risk, starter size. The conditions are pre-registered; the trade is not pre-authorized.

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

## LIVE DECISION FRAMEWORK — Post-Path-B Reversion Fade (pre-registered 2026-06-23, flat)

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
- **Credit (PRIMARY):** CCC ≥9.55 → 2-bin tree (KB-VIO-090); any Bin-A (HY ≥2.85 / BB ≥1.73 / CCC−BB ≥8.00 / CCC ≥9.65) → Path A confirming, FALSIFIED, full stop.
- **VIX >23 close-and-hold n=5** (tail-stop, KB-VIO-088; counter 0/5).
- **VIX3M/VIX inverts** (<1.0) → peak/stress being priced, no fade.
- **VVIX >120** → vol-of-vol stress, no fade.
- **Second Path-B leg** (semis new lows / fresh leveraged-ETF reversal / AI-name shock) → unwind live, not a fade.

**Spot-conditioned kill levels derive AT pricing time (KB-VIO-099)** — do NOT hard-code a stale VIX level; set the structure's strikes/stop when the trade is actually priced, naming the computing-spot + as-of date.

**Approval:** structure + size goes to Will before any execution. This pre-registers the conditions; it does NOT pre-authorize the trade.

---

## LIVE DECISION FRAMEWORK — Event-Premium Fade (M2/Jul into FOMC) — NEW 6/9 · **CLOSED 6/23**

**STATUS: CLOSED — window passed, never entered.** Gates failed twice on 6/10 (CPI/Iran); the BOJ 6/16 + FOMC 6/17 catalyst window then resolved benignly (absorbed, counter 0/5). Superseded by the Post-Path-B Reversion Fade above. **Retained for its falsification architecture** (credit 2-bin tree KB-VIO-090, n=5 tail-stop KB-VIO-088, time-box, ladder KB-VIO-099) — which the new framework references rather than re-deriving.

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

- **Credit tripwires → PRIMARY falsifier** (credit confirming is the cleanest event-premium vs regime-break discriminator). **HY >2.85 → exit immediately.** **CCC ≥9.55 → adjudicate through the pre-registered 2-bin tree (KB-VIO-090, registered 6/11 AM before the FRED 6/10 print): Bin A (cross + breadth: HY ≥2.85 / BB ≥1.73 / CCC−BB ≥8.00 within 5td, or CCC ≥9.65 escalator) = credit confirms, framework FALSIFIED, full stop. Bin B (cross + HY/IG/BB flat + dispersion <8.00) = composition artifact — MARGINAL-FAIL, no re-arm, re-check +5td, then re-mark the line in writing if still clean.** Provenance corrected 6/11: 9.55 is a VIOLET June-range-break level (episode high 9.52 + 3bp), not breadth-derived and not LIQUID's (theirs = 1000bp). Full tree: `research/2026-06-10_red_sweep_response.md` § CHG-RED-035.
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
**Status:** DORMANT — HY 2.75 (6/8), nowhere near trigger.

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

*P/L figures are placeholders — cost basis per Will, not authoritative from state files.*

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
*Last Updated: 2026-06-23 PM (Will ask — pre-registered the **Post-Path-B Reversion Fade** trigger while flat: arms only AFTER Micron 6/24 clears without re-igniting, on a clean vol-rollover setup; defined-risk calendar or call-spread, starter ≤0.5%, target VIX 16-17, ~2-3wk time-box; Micron is the explicit fork [holds→fade / breaks→tail hedge]; reuses the closed framework's credit-tree/n=5/time-box falsification. Prior Event-Premium Fade [6/10 CPI→FOMC] marked CLOSED — never entered, window resolved benignly. Conditions pre-registered, trade NOT pre-authorized — to Will for approval. Prior: 2026-06-09 PM Episode-17 closeout + Event-Premium Fade framework.)*
