# FIRE CARD — FXY — Carry-Convexity ENTRY / FXY calls (long-yen convexity)
**Setup ID:** TRY-FIRE-005 · **Trigger class:** PRINT/CONFIRM discriminator (weekly CFTC COT release) — explicitly NOT a spot-level trigger; today's ~161.8 USD/JPY tape is context, not the arm condition.
**Thesis owner:** SAM (`AGENTS/SAM/thesis/THESIS.md` v1.6.4, commit 8d1291dc) — GATE-SAM-30 FIRED: Jun-30 CFTC JPY noncommercial net **−155,092** (long 111,872 / short 266,964) = **86.2%** of the −180K cycle peak, through the pre-registered −153K/85% build line (registered 6/26; Jun-16 baseline −150,132/83.4%). SAM tail conviction: **MEDIUM → MED-HIGH**, net 60d EV ~**+1.3%** on the underlying carry-convexity frame (registered RED-#1 flip-up math). PROME-verified vs CFTC public API exact.
**Card pre-built:** 2026-07-10 ~11:15 ET (Will-authorized "option-b pre-build" — decision-ready ahead of the 3:30 PM ET Jul-7-data COT print).
**Fired:** NEVER — gate resolved **DENY** on the 2026-07-10 3:30 PM ET print. · **Status:** 🔴 **SHELVED 2026-07-10 (logged 2026-07-17 — see DISCRIMINATOR LOG).** No entry was made; card is dead per its own ZONE 1 kill rule. Nothing below is actionable. A re-arm requires a **fresh build** off SAM's current MEDIUM read — not a revival of this card.
> **Header preserved as-built (2026-07-10) for the record.** The v1.6.4 MED-HIGH thesis grade cited below was itself superseded that same evening (SAM v1.6.5, MED-HIGH → MEDIUM). Do not read the ZONE 1 grades as current.

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════

### Covering-check semantics (the card's confirm gate — pinned exactly, no undefined middle)

**Event:** TODAY ~3:30 PM ET, the Jul-7-data CFTC COT print lands (covers the truce-collapse repricing week, 7/7→7/8 US-Iran strike + Brent +6.3%).

| Print (JPY noncommercial net) | Read | Card action |
|---|---|---|
| **≤ −153K** (build held/extended past the 85% escalation line) | **CONFIRM** | → Will **[Approve]** gate opens; proceed to ZONE 2 live-marks-at-fire |
| **≥ −140K** (covered through the de-load line) | **DENY** | → card **SHELVES**; SAM's amplifier de-loads to +5pp (or lower); no entry |
| **between −140K and −153K** | **NOT-CONFIRMED** | → **no entry today**; gate stays **LIVE** to the next weekly print (Tue release cadence); card does not shelve, does not fire |

No fourth state. If the print is delayed/unavailable by end-of-day, treat as NOT-CONFIRMED (gate stays live), not as a CONFIRM-by-default.

### One-line setup
Express SAM's carry-convexity tail (CFTC record-short JPY positioning, built through the 85% escalation line, into a strengthening-yen tape) via **defined-risk FXY calls** — a convex, capped-loss proxy for a reverse-carry-squeeze payoff, not a directional yen call on today's tape.

### Structure
- **Instrument:** FXY (CurrencyShares Japanese Yen ETF) listed calls.
- **Expiry:** **2026-08-21** (42 DTE from build). Tenor reasoning vs. theta:
  - Named catalyst cluster: **7/16** (TIC May transactions + MOF ITS double-discriminator, SAM arm-#3-equivalent) → **~7/31** (MOF monthly flow data) → **7/31 BOJ MPM**. Aug-21 clears the entire cluster with a **3-week buffer** past 7/31 — survives the window plus buffer per the build mandate.
  - Rejected **2026-07-17** (7 DTE): expires literally the day after the 7/16 TIC print, before the MOF/BOJ 7/31 leg even arrives — captures only 1 of 3 named catalysts, thinnest-possible buffer, and the near-dated chain is largely a single wide-quote wall (see chain snapshot below) — bad theta-for-coverage trade.
  - Rejected **2026-09-18** (70 DTE): this is SAM's own **locked eligibility-window boundary** for the full convexity-tail thesis (retire-check date). It is tempting to match it 1:1, but at build-time ATM/near IV is statistically indistinguishable between Aug-21 and Sep-18 (12.04% vs 11.89% at the 57-strike) — Sep-18 pays ~28 extra days of theta for exposure to a window-tail (post-7/31, pre-9/18) that is thinner on named catalysts than the 7/16→7/31 cluster. **Explicit tradeoff flagged for Will:** if the entry is approved and none of the named catalysts fire by 8/21 but SAM's Sep-18 window remains open, a **roll decision is a separate ask** — not pre-approved here (no roll-by-hope, RISK_RULES #6).
- **Strike ladder (2-leg, both 2026-08-21):**
  | Leg | Strike | Moneyness | Rationale |
  |---|---|---|---|
  | A | **$58C** | +2.3% OTM | Near-tail leg — captures the smaller-magnitude routes (BOJ hawkish-of-pricing +4%, oil/MOU re-escalation +3%) with less convexity drag |
  | B | **$59C** | +4.0% OTM | Far-tail leg — sits closest to the probability-weighted average conditional move across SAM's 6 named tail routes (≈+4.1%, computed below) and carries the single best liquidity print in the entire chain (OI 4,562 / Vol 1,048 at build) |
  - **$60C and beyond explicitly rejected for the ladder:** 8/21 60C printed **bid $0.00 / ask $0.50 (200% spread, IV 20.63%)** at build — a one-sided/no-real-market quote, not a genuine cheap-convexity source. Reaching for deep-OTM "lottery" strikes here would be paying an even-more-inflated implied-vol markup (see IV-richness finding below) for a contract that may not fill near its screen price. 58C/59C are the two strikes in the chain with actual two-sided, OI-backed markets.
- **Conditional-move math (build-time, from SAM THESIS.md § THE CARRY-CONVEXITY TAIL route table):** probability-weighted average FXY move conditional on ANY route firing ≈ Σ(P₆₀d × move) / ΣP₆₀d = (8×4 + 10×2 + 6.5×7 + 5×5 + 8×3 + 10×5) / 47.5 = **196.5 / 47.5 ≈ +4.1%** → spot $56.71 × 1.041 ≈ **$59.03**. The 58C/59C ladder brackets this weighted center almost exactly.

### Why this expression (beats alternatives)
- **Outright FXY long (shares):** unbounded-relative-to-budget for the same $ risk, no convexity — SAM's own thesis already rejected the "hold/trim spot" frame at the prior MEDIUM grade; MED-HIGH reopens entry but the frame is explicitly a *tail/convexity* payoff, which options express directly and shares do not.
- **FXY puts / short:** wrong direction — long yen = USD/JPY down = FXY **up**; a put here would be the short-yen (wrong) direction (per SAM's own vehicle note in THESIS.md § VEHICLE).
- **USDJPY-put / JPY-call structure (FX options):** SAM's RED #4 gate keeps this OFF pending a clean confirmed-cheap FXY-vol read on a second source — not re-litigated here; FXY listed options are the approved vehicle.
- **Spread (call debit vertical) instead of outright calls:** would cap the exact tail-convexity payoff (the +5-7% risk-off/residual-cascade routes) that is the thesis's best-paying leg — rejected; outright calls preserve unlimited upside on the $480 capped downside.

### Max-loss budget & sizing arithmetic (BUILD-TIME REFERENCE — re-derive at fire with a fresh chain pull, rule #4)
Hard cap: **$500/card** (Will standing rule, 2026-06-26).

| Leg | Strike | Live ask (2026-07-10 ~11:09 ET pull) | $/contract (×100) | Contracts | $ at risk |
|---|---|---|---|---|---|
| A | 58C | $0.30 | $30.00 | 6 | $180.00 |
| B | 59C | $0.15 | $15.00 | 20 | $300.00 |
| **Total** | | | | **26 contracts** | **$480.00** |

- `risk_calc.py --premium 0.30 --max-loss 500` (single-leg check) → max 16 contracts / $480 budget-used / $20 unused, confirming Leg A's per-contract math independently.
- `risk_calc.py --premium 0.15 --max-loss 500` (single-leg check) → max 33 contracts / $495 budget-used / $5 unused, confirming Leg B's per-contract math independently.
- Combined 2-leg split (6+20=26 contracts) leaves **$20.00 unused** vs the $500 cap — deliberate buffer for ask-price drift between build (7/10 11:09 ET) and actual fire (post-3:30 PM confirm). **Re-run both `risk_calc.py` legs against the live fire-time ask before sizing final contract counts — this table is illustrative, not an executable order.**

### Edge / Risk-Score (per RISK_SCORING.md)
- **Thesis input:** SAM MED-HIGH, net 60d spot-equivalent EV ~+1.3% (registered RED-#1 flip-up math, THESIS.md v1.6.4).
- **TERRY construction-level check — IV vs recent realized (rule: option marks need live chain + context):**
  | Window | FXY realized vol (annualized, computed 2026-07-10 from yfinance 3mo history) |
  |---|---|
  | 5d | 6.29% |
  | 10d | 6.83% |
  | 20d | 5.39% |
  | 30d | 4.47% |
  | 60d | 6.56% |

  vs. **build-time chain IV at the ladder strikes (8/21 expiry): 58C = 9.96%, 59C = 10.65%** (ATM 57C = 12.04%, further OTM 60C = 20.63%).

  **Finding: IV is pumped ~1.5-2.7x trailing realized** (10.3% avg ladder IV ÷ 4.47-6.56% recent RV range), consistent with the market already pricing some event/tail premium post-Katayama jawbone + the 7/16-7/31 catalyst cluster ahead. **This is the load-bearing construction caveat:** the options market is not asleep on this tail — some of SAM's +1.3% EV is already being charged for at the strike level. **How it changes the ladder:** (1) it rules out reaching into the deep-OTM wing (60C/62C) where IV richness is worst (20.63%/31.74%) and liquidity is close to fictional (zero bid); (2) it keeps the ladder anchored at the two strikes with real two-sided markets (58C/59C) rather than maximizing raw convexity-per-dollar; (3) it means the realistic edge is **Small-to-Moderate, not Strong**, per RISK_SCORING.md's qualitative bands — a genuinely cheap-IV entry this is not.
- **Kelly gut-check (illustrative only — do not treat as precise, per RISK_SCORING.md §3):** collapsing SAM's own P(no eligible trigger by Sep-18) ≈ 0.55-0.60 to a rough P(some trigger fires within the shorter 8/21 window) ≈ 0.25-0.35 (subjective, window-scaled down from the full Sep-18 box), and assuming a fired-route payoff of roughly 2-4x premium on the ladder (b): f\* = (p·b − q)/b ranges from **≈ −0.05 (b=2, p=0.30)** to **≈ +0.13 (b=4, p=0.30)** — sign-flips depending on assumed payoff multiple. This is exactly the "uncertain edge" case RISK_SCORING.md says to shrink aggressively for, not scale up. **TERRY policy invoked: the $500 hard-loss cap is already the binding constraint** (smaller than any Kelly-implied size at these p/b ranges), so no further reduction is needed beyond the cap already built into the 26-contract ladder above — but this is NOT a "strong edge, could size bigger" situation.
- **Verdict inputs:** Edge = **Small-to-Moderate** (thesis-positive, IV-taxed). Sizing = capped at $480/$500 (hard budget binds, not Kelly). Execution status = **BLOCKED** until Will approval + fire-time preconditions below.

### Rule #6 check — puts on green days, calls on red days (RISK_RULES.md #6 / root CLAUDE.md rule 6)
**FXY is GREEN today** (+0.41%, $56.71; USD/JPY −0.49% to 161.74 — yen strengthening on the Katayama jawbone). **Buying calls on a green day breaks rule #6.** Per the rule's own "note when breaking and why" clause:

- **Why it's being flagged, not silently overridden:** the entry is gated on a discrete 3:30 PM COT print event, not on today's chart momentum — the trigger class is PRINT/CONFIRM, not a chase off today's green tape. This is the same class of rationale TRY-FIRE-004 uses for flow/velocity triggers (never the bare level/day-of chase).
- **Branch 1 — fire same-day if CONFIRM lands 3:30 PM today (7/10, still green):** acceptable ONLY as an event-driven exception, not a momentum chase — Will should treat this as intentionally breaking rule #6 for a dated, external catalyst (the print itself), with the tradeoff that entry happens on the exact day yen strength is most already-priced into the tape and possibly into the ladder's IV.
- **Branch 2 — hold CONFIRM-armed but unfired, wait for the next red FXY day (rule-#6-clean):** if CONFIRM lands today, Will could elect to hold the card ARMED-CONFIRMED and wait for the next red day (FXY down / USD/JPY up) — plausibly Mon 7/13 or later — before actually pulling the trigger. Tradeoff: (a) risk of chasing a *worse* price if yen keeps strengthening into 7/16 (waiting for red could mean waiting for a day that doesn't come before the TIC print, i.e., a real cost to the 7/16 double-discriminator window); (b) IV could compress further post-print-fade, improving entry economics, or could stay rich/widen further into 7/16. **Both branches are presented; TERRY does not pick one — this is Will's call at the fire-time [Approve] gate.**

### Invalidation / disarm lines (what kills this card)
- **COT de-load:** any future weekly CFTC print covers back through **−140K/77%** (SAM's DENY line) → card **SHELVES**, no re-derivation needed — the same print event that arms the card also owns its kill line.
- **Full SAM thesis retirement (either leg, per THESIS.md § two-legged SPF):** CFTC covers below **−108K/60%** (Leg 1) OR **Sep 18 2026 reached with no eligible trigger fired** (Leg 2) → SAM's frame retires to LOW → this card is DEAD regardless of where it sits (thesis-owner disconfirmation kills the construction).
- **USD/JPY reclaims the 162-163 zone on MOF silence** (i.e., today's Katayama-driven move fully round-trips with no fresh MOF response) → reads as the confirm-day catalyst fading, not as thesis-breaking on its own, but **disarms the "fire same-day" impulse** (Branch 1 above) — push toward Branch 2 (wait-for-red-day) if this happens.
- **S1-A strike-regime change** (MOF shifts off unsignalled-ambush tactics, or an actual strike fires and resolves the Channel-3 backdrop) → re-confirm-needed before firing; not TERRY's call to grade, flag to SAM/PROME.
- **Card-level lapse condition:** any ONE of the above four fires → card does not proceed to fire without a fresh Will/PROME/SAM re-check. No silent middle state.

### Fire-time preconditions (ALL required before ZONE 2 can be filled)
1. **Will [Approve]** — explicit, per rule #5. No execution without it.
2. **Live broker book pull** — book was confirmed **FLAT this axis** as of Will's 6/25 close of the FXY Jun-18 $58C position (SAM THESIS.md § POSITION VIEW, "🟢 POSITION FLAT (Will-confirmed 2026-06-29)"). Position truth is off-repo (Will/broker direct, root CLAUDE.md) — **re-verify FLAT (or note any new exposure) live at fire time; do not assume it still holds** (rule #6 / RISK_RULES #4).
3. **Fire-time chain re-pull:** `chain_fetch.py FXY 2026-08-21 --type call --no-cache` — fresh marks, not the build-time snapshot below.
4. **Fire-time spot + green/red re-check:** `fetch.py price FXY --json` + `fetch.py price USDJPY=X --json` at fire time, not today's tape carried forward.
5. **Fire-time sizing:** re-run `risk_calc.py` per leg against the live ask; do not carry forward the $480/26-contract table above without re-deriving.

══════════════════════════════════════════════════════════════
DISCRIMINATOR LOG (dated entries — record, don't re-derive ZONE 1)
══════════════════════════════════════════════════════════════

**2026-07-10 ~11:15 ET — CARD BUILT, gate PENDING.** Source: SAM THESIS.md v1.6.4 (GATE-SAM-30 fired, Jun-30 print −155,092/86.2%, PROME-verified). Awaiting the 3:30 PM ET Jul-7-data COT print for the covering-check resolution (CONFIRM / DENY / NOT-CONFIRMED — see ZONE 1 table). **No arm has fired yet — this entry records the pre-build only.**

- Build-time context: USD/JPY 161.74 (−0.49%), FXY $56.71 (+0.41%) — both live-pulled 2026-07-10 ~11:09-11:15 ET via `fetch.py`.
- Build-time chain: FXY 2026-08-21 calls pulled via `chain_fetch.py --no-cache`, fetch timestamp 2026-07-10 11:09 ET (see BUILD-TIME REFERENCE block below).
- Realized-vol computation: yfinance FXY 3mo daily history through 2026-07-10 close ($56.71).

**2026-07-10 ~3:30 PM ET — GATE RESOLVED: DENY → CARD SHELVES. NO ENTRY MADE.** Jul-7-data CFTC COT print landed **−123,778 / 68.8% of the −180K Jul-2024 peak**, vs Jun-30's −155,092 / 86.2% = **+31,314 contracts of covering, −17.4pp** — the largest one-week net-short reduction in SAM's tracked series (`AGENTS/SAM/workbook/CFTC_JPY.tsv`, 2026-04-07→present). **Clears the ≥−140K DE-LOAD line by 16,222 contracts — not a close call, no judgment exercised.** Per the ZONE 1 table this SHELVES the card with no re-derivation owed. Thesis owner concurred same session: SAM THESIS v1.6.5 (SAM-36 resolved FALSE/DE-LOAD), convexity-tail **MED-HIGH → MEDIUM**, amplifier **+8-10pp → +5pp**, explicit "TRY-FIRE-005 entry NOT recommended." The AM MED-HIGH reclaim that justified the pre-build stood <12 hrs. Source: `AGENTS/SAM/STATUS.md` (7/10 PM session note + CHANGELOG 2026-07-10 PM).

**2026-07-17 ~09:50 ET — LOGGING LAG CLOSED (process note, not a new grade).** The DENY above was resolved by SAM on 7/10 but **never propagated to TERRY's own surfaces** — for 7 days `SETUPS.tsv` carried this card as ARMED-PENDING, `FIRE_CARDS_LADDER.md` described the gate as PENDING, and this log ended at the pre-build entry. **No trade was ever placed on the stale row, so the cost was zero dollars and one stale ledger** — but this is exactly the ledger-drift failure the root CLAUDE.md Data Hygiene rule names ("STATUS is canonical; ledgers silently drift"). `LAST_COMPLETION.md` had even pre-written the correct next step ("DENY → shelve"); the session ended before it ran and no boot re-surfaced it. **Lesson: a card whose resolver fires outside a TERRY session has no owner.** Gap → `POSTMORTEMS.md`. Next CFTC print (Fri 7/17 3:30 PM ET) does **not** revive this card — a DENY shelve is terminal per ZONE 1.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY at actual fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** [Jul-7-data COT net = ____] — CONFIRM / DENY / NOT-CONFIRMED? ____
- **Spot(s):** FXY $____ / USD/JPY ____ (from `fetch.py price ... --json`) — as-of ____
- **Green/red day check (rule #6):** [puts on green ✓ / calls on red ✓ / breaking & why — re-derive at fire, do not carry forward today's green-day note above]
- **Chain marks:** `chain_fetch.py FXY 2026-08-21 --type call --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [Y/N]
- **Broker position truth:** `[POSITION_STATE_UNKNOWN]` until pulled live at fire — build-time reference only says FLAT as of 6/25 close.
- **Sizing:** `risk_calc.py --premium <mark> --max-loss 500` per leg → ____ contracts

---
**BUILD-TIME REFERENCE — NOT FIRE MARKS (2026-07-10 ~11:09-11:15 ET pull, for construction reasoning only, do not use for sizing at fire):**

FXY spot $56.71 (+0.41%) · USD/JPY 161.74 (−0.49%) — `fetch.py price FXY` / `fetch.py price USDJPY=X`, 2026-07-10.

FXY 2026-08-21 calls (`chain_fetch.py FXY 2026-08-21 --type call --no-cache`, fetch 2026-07-10 11:09 ET):

| Strike | Mny% | Bid | Ask | Mark | Spread% | IV% | Vol | OI | Last trade |
|---|---|---|---|---|---|---|---|---|---|
| 54.00 | −4.8 | 2.40 | 3.10 | 2.75 | 25.45 | 17.53 | 10 | 402 | 2026-07-10 13:34 |
| 55.00 | −3.0 | 1.70 | 2.35 | 2.02 | 32.10 | 17.29 | N/A | 1 | 2026-07-07 18:21 |
| 56.00 | −1.3 | 0.85 | 1.50 | 1.18 | 55.32 | 14.36 | 3 | 17 | 2026-07-06 16:15 |
| 57.00 | +0.5 | 0.55 | 0.80 | 0.68 | 37.04 | 12.04 | 5 | 2,174 | 2026-07-10 14:29 |
| **58.00 (Leg A)** | **+2.3** | **0.15** | **0.30** | **0.22** | **66.67** | **9.96** | **10** | **676** | 2026-07-10 13:47 |
| **59.00 (Leg B)** | **+4.0** | **0.10** | **0.15** | **0.12** | **40.00** | **10.65** | **1,048** | **4,562** | 2026-07-09 16:25 |
| 60.00 | +5.8 | 0.00 | 0.50 | 0.25 | 200.00 | 20.63 | 215 | 273 | 2026-07-08 16:08 |
| 62.00 | +9.3 | 0.00 | 0.75 | 0.38 | 200.00 | 31.74 | N/A | 10 | 2026-06-22 18:59 |

FXY realized vol (annualized, yfinance 3mo history through 2026-07-10 close): 5d 6.29% / 10d 6.83% / 20d 5.39% / 30d 4.47% / 60d 6.56%.

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] COT print actually landed and reads CONFIRM (≤−153K) — not NOT-CONFIRMED, not DENY
- [ ] Live marks < 15 min old (spot + chain) · [ ] Green/red rule satisfied or break explicitly justified (see Branch 1/2 above)
- [ ] Liquidity OK on both legs (58C/59C two-sided market, not the 60C-style zero-bid case)
- [ ] Max loss ≤ $500 at fire-time asks · [ ] Broker position truth re-confirmed FLAT (or new exposure noted)

**Terry verdict (as of build, 2026-07-10 ~11:15 ET):** **NO TRADE YET — awaiting 3:30 PM ET covering-check.** Card is decision-ready: structure, ladder, sizing math, and both rule-#6 branches are pre-locked. Edge graded Small-to-Moderate (thesis MED-HIGH, taxed by ~1.5-2.7x IV-over-realized richness) — this is a CONDITIONAL setup, not a Strong one, even if CONFIRM lands.
**Decision:** [ ] APPROVE  [ ] REJECT  [x] HOLD — awaiting 3:30 PM ET Jul-7-data COT print

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
