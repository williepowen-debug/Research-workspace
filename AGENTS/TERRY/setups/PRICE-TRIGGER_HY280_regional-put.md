# FIRE CARD — KRE — Regional-bank puts (fresh deploy)
**Setup ID:** TRY-FIRE-001 · **Trigger class:** PRICE
**Thesis owner:** REGINALD (regional/CRE) + NEXUS (regime) · **Card pre-built:** 2026-06-26 · **Fired:** ____ (fill at fire)
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5). Detection owned by LIQUID/SENTRY.

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** **HY OAS breaks ≥ 280 bps** (from ~276 baseline 6/24) AND sustains
  the level (not a single intraday print — thin-liquidity discipline). This is the credit-regime
  widening tell that pulls broad-regional transmission forward from the Q1–Q2 2027 base case.
- **One-line setup:** credit is repricing risk in real time — buy liquid regional-bank downside
  before the equity tape catches the spread move.
- **Structure:** **KRE puts**, **~3–6 month** expiry (capture the widening momentum, not the 2027 grind),
  **~8–12% OTM** strike ladder. KRE = most liquid regional expression; tight option spreads.
- **Why this expression:** HY-break is a *path/level* trigger, not a single-name event → ETF beta is
  the clean vehicle. Puts (not duration/TBT) because the channel is credit-spread, not rates.
- **Alternatives rejected:** single-name (WAL/OZK) puts = idiosyncratic, miss the broad move;
  equity short = unbounded + margin; long-dated 2027 puts = wrong tenor for a momentum break.
- **Max-loss budget:** $500 per card (set by Will 2026-06-26)
- **Invalidation (thesis/price/time):** HY round-trips back < 270 sustained → credit-stress false alarm.
- **Kill line:** HY back < 270 sustained, OR KRE reclaims prior range high → exit.
- **Confirm line:** HY sustains > 280 **and** KRE breaks key support **and** CCC-HY ratio widening
  (REGINALD/NEXUS corroboration) → hold / consider 2nd tranche on next red day.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY this at fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** HY OAS ___ bps (≥280 & sustained?) [Y/N] · CCC-HY ratio ___ · `fetch.py fred BAMLH0A0HYM2`
- **Spot:** KRE $____ (as-of ____) · `fetch.py price KRE --json`
- **Green/red day check (rule #6):** KRE today ___% → puts on green ✓ / breaking & why: ____
- **Chain marks:** `chain_fetch.py KRE <EXPIRY> --type put --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [spread/OI per chain flags — Y/N]
- **Broker position truth:** existing KRE puts in book (FORGE/STATUS shows KRE Dec/Sep/Aug ladder) — net new vs overlap? [check live]
- **Sizing:** `risk_calc.py --premium <mark> --max-loss <budget>` → ____ contracts

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] HY actually ≥280 & sustained (not near-miss) · [ ] Live marks < 15 min · [ ] Green/red OK
- [ ] Liquidity OK · [ ] Max loss ≤ budget · [ ] Position truth known (overlap with existing KRE ladder checked)

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## 🔴 2026-07-30 ~13:40 ET — **THE ENTRY TRIGGER IS MET. TERRY STILL SAYS DO NOT FIRE.** (surfaced from the WALTER backlog, not by detection)

### The trigger leg — MET

**ZONE-1 trigger, exact wording:** *"HY OAS breaks ≥280 bps AND sustains the level (not a single intraday print)."*

| Date | HY OAS (bps) | |
|---|---|---|
| 7/22 | 268 | |
| 7/23 | 277 | |
| 7/24 | 279 | |
| **7/27** | **281** | ✅ ≥280 |
| **7/28** | **284** | ✅ ≥280 |
| **7/29** | **287** | ✅ ≥280 |

**Three consecutive daily observations ≥280, monotonically widening, +19bp in five sessions.** That is *sustained*, not a single print. **The entry trigger as written is MET.** *(FRED `BAMLH0A0HYM2`, pulled 2026-07-30 ~13:30 ET.)*

**Quality-sorted, which is the genuine-stress signature, not a technical:** CCC **981 → 1013 (+32bp)** · HY **268 → 287 (+19bp)** · IG **78 → 81 (+3bp)**. Widening concentrates down the quality curve. *(Independently matches VIOLET's KB-VIO 7/24→7/28 read: CCC +9 > HY +5 = BB +5 > B +2 > IG +1.)*

### 🔴 TERRY VERDICT: **NO FIRE.** The trigger is met and the trade is still wrong.

**① The transmission this card is built on is DEMONSTRABLY NOT HAPPENING.** The one-line setup reads *"buy liquid regional-bank downside **before the equity tape catches the spread move**."* The equity tape is not lagging — **it is going the other way.**

| | |
|---|---|
| KRE | **$76.15** |
| 6-month high | **77.92 (7/16)** — KRE is **2.3% below its high** |
| 20d MA / 50d MA | 75.61 / 72.90 — **above both** |
| Last 8 closes | 75.89 · 75.98 · 75.60 · 75.15 · 75.73 · 75.52 · 76.79 · 76.18 — **flat-to-up while HY widened 19bp** |

**② ⚠️ THE CARD'S OWN KILL LINE IS CLOSER TO FIRING THAN ITS CONFIRM LINE.** Kill = *"HY back <270 sustained, **OR KRE reclaims prior range high**."* KRE at 76.15 vs a 6mo high of 77.92 is **within 2.3% of the kill clause.** Confirm = *"HY sustains >280 **and KRE breaks key support** and CCC-HY ratio widening"* — KRE breaking support is **not remotely true.** **When a card's entry trigger and its kill line converge, the premise is not transmitting.** That is the finding, not the trigger.

**③ ⚠️ MECHANISM MISMATCH — `finding_threshold_vs_mechanism`, and this is the load-bearing objection.** The card assumes HY widening = **broad credit stress → regional-bank/CRE transmission**. But the live credit story in the tape is **AI-capex financing**: Oracle 5Y CDS at a **record in ICE's 17.5-year series** (210.675 on 7/27, high 215.610 on 7/24) on the Nvidia ~$250bn OpenAI guarantee, whose *stated purpose is OpenAI's non-investment-grade credit profile* (WALTER `SIG-W-20260728-002`). **If HY ≥280 is being driven by tech-vendor credit rather than bank/CRE credit, the threshold fired on a mechanism this card was never built for — and KRE has no reason to follow.** ⚠️ **I have NOT established the attribution** — that is LIQUID's and REGINALD's to rule on, and it is the question that decides this card.

**④ CCC-HY "ratio" is SPEC-AMBIGUOUS and I will not resolve it in the firing direction.** The confirm line says *"CCC-HY ratio widening."* Both readings are defensible and **they disagree**:
- **Difference** (CCC − HY): 713 → **726bp** = **WIDENING** ✅
- **Ratio** (CCC ÷ HY): 3.66 → **3.53** = **NARROWING** ❌

**The card never defined which.** → spec defect, routed to the owners. *(`finding_ratio_gauge_denominator_branch` / `finding_number_carries_threshold_unit_source`.)*

### 🔴 DETECTION FAILURE — this reached me by accident

**Detection on this card is owned by LIQUID/SENTRY (ZONE-1, line 4). The trigger crossed on 7/27 and no signal reached TERRY.** I found it on **7/30** while draining a **13-deep WALTER backlog** — and only because I pulled FRED to check an unrelated credit signal. Meanwhile `STATUS.md` carried **"HY OAS 269 [7/20] — moved AWAY from the 280 line"** for **nine days**, i.e. **stale in the dangerous direction**: it advertised the card as receding while it was crossing. **Neither the detection owner nor my own surface caught a fired gate on a staged card.** → routed to LIQUID; logged as the un-owned-gate class (the `TRY-FIRE-005` lesson, recurring).

### Status

**Card stays STAGED, unfired, $0 at risk.** ZONE 2 deliberately left empty — no live marks pulled, because I am not proposing an entry. **Revisit only on:** (a) LIQUID/REGINALD ruling the widening is bank/CRE-driven rather than AI-capex-driven, **AND** (b) KRE actually breaking support. **If instead KRE reclaims 77.92, the kill line fires and this card lapses.**
