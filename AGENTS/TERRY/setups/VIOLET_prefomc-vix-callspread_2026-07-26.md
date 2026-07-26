# TRADE CARD — VIX — pre-FOMC defined-risk CALL DEBIT SPREAD

**Setup ID:** `TRY-VIOLET-VIXCS` · **Class:** EVENT-BOX (not a fire card — no pre-registered trigger; build-to-order)
**Date built:** 2026-07-26 (Sun) · **Thesis owner:** VIOLET (KB-VIO-125 / locked tree KB-VIO-123; gamma chain HENRY 7/23)
**Request:** `inbox/2026-07-25_from-VIOLET_CONSTRUCTION-REQ-prefomc-vix-call-spread-will-approved-build.md`
**Stage:** Will approved **BUILD IN PRINCIPLE** 7/25 → this card + **live Monday quotes** → Will **final [Approve]** (two-stage fill pattern)

**Terry verdict:** 🟡 **CONDITIONAL** — structure is sound and the expression is correct; the trade **cannot be priced today** and has two named pre-entry kill conditions.
**Confidence in trade structure:** Medium-High · **Confidence in the entry economics:** LOW until Monday's pull.

---

## 1. One-line setup

Buy a small, defined-risk **VIX call debit spread** on Mon 7/27–Tue 7/28 that spans HENRY's VIX>23 vol-control igniter, to own equity-vol convexity into the **first FOMC of this cycle where dealers are SHORT gamma** — then exit into the event, win or lose, at the 7/30 boot.

---

## 2. Preconditions (all must hold at fill)

- ✅ **Thesis gate MET (VIOLET-side):** dealers short-gamma into FOMC, corroborated 5-of-6 trackers (HENRY 7/23: flip ~7,496, net GEX ~−$45B/1%, SPX −88pts below, put wall 7,300–7,400). All five prior absorptions this cycle happened under **LONG** gamma — the gamma sign flip is the *entire* differential.
- ⬜ **VIX < 20 at fill** (registered window, KB-VIO-123 — the long-vol window is BEFORE the confirm).
- ⬜ **Rule #6 (day-color):** VIX calls are bought on a **VIX-soft / equity-green** day. A soft Monday open fits. Filling on a VIX-up day = a rule break that must be written on the card with a reason.
- ⬜ **Main book only.** This goes in the **main account** (cash $24,101 as-of 7/24), **not** the small satellite that capped the USO fill at $241.72 buying power on 7/24.
- ⬜ **Net debit ≤ the no-pay line in §3.** This is the binding constraint, not the thesis.

**What must NOT be happening:**
- VIX **≥20 settle**, or **VIX3M/VIX < 1.0** (term-structure inversion) before the fill → the confirm has arrived, the entry logic has **EXPIRED**. Stand down. Do not buy vol on inversion (KB-VIO-034: inversion/>20-settle are peak-markers, i.e. where you SELL).

> ⚠️ **Live cross-risk into Monday (TERRY flag, not in VIOLET's packet).** The Houthi strike on Aramco's **Jazan refinery** landed Saturday with futures closed (WALTER `SIG-W-20260725-008`). If that bleeds into equities, **VIX can gap up Monday** — which trips **both** guards at once: it breaks rule #6 *and* it can push VIX ≥20, voiding the entry window. **A VIX gap-up Monday is a STAND-DOWN, not an urgent entry.** The whole edge here is buying the window *before* the confirm; a gap means the confirm arrived without us and we are now the late money.

---

## 3. Entry

**Trigger:** discretionary within the window — Mon 7/27 or Tue 7/28, on a VIX-soft session, VIX <20.

| Rule | Level |
|---|---|
| **Target net debit** | **≤ $1.00** per 5-wide spread |
| **Hard no-pay-above** | **$1.20** per 5-wide spread |
| **Do-not-chase** | VIX ≥20 settle · VIX3M/VIX <1.0 · debit >$1.20 · Monday VIX gap-up |
| **Order type** | **Limit only, as a spread (net debit).** Never leg it, never market-order. |

**Why the hard $1.20 line matters more than usual:** the 8/5 chain shows bid/ask widths of **85–160% of mark**. On a 5-wide spread the same structure prices anywhere from **$0.60 to $1.85** depending purely on where you get filled. Friction, not the thesis, decides whether this is a 3:1 or a 1.7:1. **If Monday's live market won't come to $1.20, there is no trade** — that is a clean NO, not a reason to pay up.

---

## 4. Structure

**Instrument:** VIX call **debit spread** (defined-risk; never outright VIX calls per KB-VIO-124 — contango/theta bleed).

### Recommended: **8/5 expiry, long 20C / short 25C** (5-wide)
### Named alternative: **8/5 long 21C / short 26C** — if Monday's 20C is bid rich, take this; it is cheaper and still spans 23.

**Expiry call — I am departing from VIOLET's lean, and here is why.**

VIOLET leaned **8/19** for liquidity ("call OI 3.65M vs 8/5's 55K"). At *institutional* size that is decisive. **At our size it is irrelevant** — we are buying **3–5 contracts**, and 8/5's open interest at the 20–26 strikes runs **1,200–13,000 contracts**. That is orders of magnitude more depth than a 5-lot needs. The 3.65M-vs-55K comparison is answering a question we are not asking.

What *does* decide it is **spike capture**, and it runs the other way:

- VIX options settle on the **VIX future** for their expiry, not spot. In a spike, a **near-dated** future tracks spot far more closely than a far-dated one (convergence). On our 7/30 exit date, the 8/5 future has ~6 days to run (high beta to spot); the 8/19 future has ~20 days (materially damped).
- A spot move to 23 might carry the 8/5 forward to ~21.5 but the 8/19 forward only to ~21.0 — **and we are selling the forward, not spot.**

**Honest cost of that choice:** 8/5 decays faster, so on the failure path (VIX stays <20) the 8/5 spread salvages *less* than 8/19 would. Given VIOLET's own counter-case is that absorption is **0/5 against this trade class**, the failure path is the base case — so this is a real trade-off, not a free win. I take it because max loss is the debit either way and it is small; we are buying spike-beta per dollar, and 8/5 delivers more of it.

> **Decision rule for Monday (mechanical):** pull **both** chains. Take **8/5** unless its 20/25 (or 21/26) net debit is **more than $0.25 worse** than the same structure on 8/19 — in which case the friction has eaten the beta advantage and you take **8/19** instead.

### 🚫 Expiry explicitly REJECTED: **7/29**

A **7/29 VIX expiry exists** (it is not on VIOLET's menu). **Do not use it.** VIX options settle against the **SOQ — a Special Opening Quotation struck at the open on expiration Wednesday.** So 7/29 VIX options settle around **09:30 ET on 7/29**, and the FOMC statement lands at **14:00 ET on 7/29**. They expire roughly four and a half hours *before the event they would be bought for*. This is the sharpest available way to lose 100% on a correct thesis.

### Alternatives rejected
- **Outright VIX calls** — VIOLET constraint #2; contango/theta bleed, and it doubles the vol you pay for.
- **Anything MOVE/rates-vol-linked** — VIOLET constraint #1; **TRY-FIRE-004 (30× TLT Sep-30 77P, live) already owns the rates-vol leg** and a rates add double-counts it (GATE-VIO-116 adjudication).
- **VIX puts / short vol** — wrong direction for the thesis.
- **SPX/SPY put spread** — expresses direction, not the vol-of-vol convexity the short-gamma thesis is actually about.

### Strike logic
Registered ladder KB-VIO-099 (sub-20-entry episode economics): **23-touch is modal (+18–21%)** · 24–25 (+24–31%) · 26 (+34–37%) · **≥+50% only 56–60% at episode level → buy the modal-to-mid zone, do not pay for the far tail.** HENRY's vol-control igniter **VIX>23** is the acceleration line, and **the spread spans it** (20 < 23 < 25).

**⚠️ Moneyness is NOT what spot suggests.** Judged against spot 18.58 the 20 strike looks +7.6% OTM. Judged against the **8/5 forward (est. ~19.2)** it is only **~+4% OTM** — nearly at-the-money on the thing that actually settles it. The forward is in contango above spot, so **spot-relative moneyness systematically overstates how far OTM these strikes are** by roughly 3–7pp.

---

## 5. Risk

| Item | Value |
|---|---|
| **Max loss** | **the net debit, in full** — 100% loss is the *expected* outcome on the base path |
| **Recommended budget** | **$300–400** (3 spreads at ≤$1.20, or 4 at ≤$1.00) |
| **Hard cap** | **$500** (standing per-card cap, Will 2026-06-26) |
| **Sizing rule** | `contracts = floor(budget ÷ (net_debit × 100))`, **max 5** |
| **Stop** | **None — and none is wanted.** Defined-risk; a stop on a 3-day event box just donates the spread twice. |
| **Invalidation** | **TIME, not price:** the 7/29 FOMC passes with VIX <20 and no confirm legs → the thesis path failed *for this box*. Exit/salvage at the 7/30 boot. |

**I recommend $300–400, not the full $500.** Three reasons, all from the counter-case: absorption is **0/5** against this trade class this cycle; `cheap_tail` reads **DORMANT 2/4**, so we are paying **mid-range, not floor** prices; and the *realistic* payoff is materially below what the spread width advertises (§6). Sizing to the cap would be paying full freight for a lottery whose base rate is 0-for-5.

**Gap/event risk:** the whole position *is* an event bet. Sized as a full loss. Nothing here can lose more than the debit — no assignment risk (VIX is cash-settled, and we exit before expiry), no margin call, no auto-liquidation exposure.

**Book concentration — this one is genuinely additive.** Unlike the DHI/PHM card that got lapsed for deepening the same higher-for-longer book, this is **equity-vol**, a different axis from every live leg: 004 (rates-vol), the USO Sep call spread + XLE (oil-long), the regional-bank put basket (credit). VIOLET's constraint #1 enforces exactly that separation. **It is a diversifier, not a stack.**

### ★ EFFECTIVE-N — independence audit
*First card to carry this field (adopted 2026-07-26, Will-approved — `RISK_SCORING.md` §2b, source grade SC-03).*

| Field | Entry |
|---|---|
| **N_claimed** | **3** — (i) dealers short-gamma into FOMC, (ii) independent vol channels at episode highs (CCC 9.91 / disp 8.25 / MOVE 80.08 / OVX ratio p98.1), (iii) a dense 3-session catalyst stack in buyback blackout |
| **Shared antecedent** | 🔴 **The gamma sign flip.** VIOLET states it herself: *"The entire differential vs those five absorptions is the gamma sign flip — if you don't believe HENRY's 5-of-6 read, don't build."* Legs (ii) and (iii) were **also present in the five prior absorptions**, all of which were absorbed. They are the *setting*, not independent votes — only (i) distinguishes this instance from the 0-for-5 record. |
| **EFFECTIVE N** | **N_eff = 1** — one inference deep, and it is a single-source read (HENRY's gamma chain, corroborated 5-of-6 trackers). |
| **Sizing reference** | **Sized to N_eff = 1: $300–400, below the $500 cap.** Sizing to N_claimed = 3 would have argued for the full cap or more. |

**Book-level check:** shares **no** falsifier with any live position — 004 dies on a rates rally, USO/XLE on Hormuz de-escalation, the bank basket on regional credit staying clean. **A VIX spike is orthogonal to all three.** This is one of the few genuinely independent adds available to this book.

> **This is the field doing its job on its first outing.** The prose in §7 already said "one inference deep," and I had already sized below the cap — but the *reason* was buried in a counter-case paragraph. Stated as `N_eff = 1` against `N_claimed = 3`, the sizing gap is visible on the page instead of implicit in a judgement call.

---

## 6. Target / management

> ### ⚠️ The most important line on this card
> **The advertised ~4:1 on a 5-wide spread is NOT reachable under this card's own exit discipline.** That payoff requires holding to **8/5 expiry with VIX above 25**. We are contractually exiting at the **7/30 boot** — so we sell the spread on **value, not intrinsic**, with ~6 days of life left.
>
> **Realistic payoff on the modal 23-touch: roughly +50% to +120% on the debit.** On a $360 stake that is ~+$180 to +$430. Anyone sizing this off the "4:1" headline is sizing off a number the exit rule forbids collecting.

| Item | Rule |
|---|---|
| **Target 1** | **VIX ≥23 touch** (HENRY's igniter / VIOLET's modal path) → **monetize INTO strength, sell at least half** |
| **Target 2** | Term-structure **inversion** (VIX3M/VIX <1.0) → peak-marker, KB-VIO-034 → **sell the rest** |
| **Peak tell** | **SKEW crashing during a spike** = protection being monetized — that is often *the* top. Sell, don't admire it. |
| **Time stop** | **7/30 boot — MANDATORY review regardless of P/L.** Window passed with VIX <20 and no confirm → exit/salvage. **No expiry drift.** |
| **Roll rule** | **NONE pre-registered.** One-shot event box. Any roll = fresh Will re-approval from scratch. |

**Do not hold for the tail.** VIOLET's ladder is explicit that ≥+50% episode moves hit only 56–60% of the time — and the peak-markers (inversion, SKEW crash) are *sell* signals, not confirmation to press. This trade monetizes into the spike or it dies at the 7/30 boot.

---

## 7. Why not / counter-trade — the honest case against

VIOLET supplied most of this and it is unusually strong for a packet arguing *for* a trade. I have added three items she did not have.

**From VIOLET:**
1. **GEX-absorption is 0/5 against this trade class this cycle.** Five prior chances, five absorptions.
2. **Thursday's 20.31 intraday break was SOLD hard into the close** — the tape is actively defending this vol level.
3. **COT: leveraged money already re-derisked** (+10.2K → +3.1K) — the vol-supply cushion has partially rebuilt.
4. **`cheap_tail` DORMANT 2/4** — we are paying mid-range, not floor, prices.
5. **Two mechanical suppressors** — record-low correlations (KB-VIO-126) and hedge composition (KB-VIO-108) can pin index vol *even through* single-name earnings chaos.
6. **VIOLET's own bottom line:** *"The entire differential vs those five absorptions is the gamma sign flip — if you don't believe HENRY's 5-of-6 read, don't build."*

**Added by TERRY:**

7. 🔴 **This FOMC carries NO SEP / no dot-plot** (PROME DOCKET row 37), with a hold already **~70–81% priced**. It is the *low-information* meeting of the pair — the September meeting (9/15–16) is the one with an SEP. Buying event-vol into a meeting with no dots and a heavily-priced outcome is buying the **weaker** of the two available catalysts. The offsetting point is fair: the catalyst is the *stack* (FOMC + MSFT/META 7/29 + AMZN 7/30 + BOJ 7/30–31 + month-end, in buyback blackout), not the FOMC alone.

8. 🔴 **The fleet's standing view is that VIX calls are the WRONG vehicle for this family of exposure.** DEWEY, 7/20 (`mechanical-selling-stack`, to me): *"the mechanical-cushion hedge is **rates-vol-shaped, NOT VIX calls** — VIX-call structures **overpay** for the amplification you'd be hedging."* That was written about mechanical-selling cushion, not about short-gamma-into-FOMC, so it is **adjacent, not a direct refutation** — but it is a live fleet finding pointing at this exact instrument and it belongs on the card.

   > ⚠️ **UPGRADED 2026-07-26 (late) — this claim is stronger than the version I first graded.** Filing the packet at closeout, I found it had arrived **twice**: DEWEY's 7/20 original, and a 7/21 WALTER "backstop" reconstructed *from the handoff's routing table*. The backstop added evidence but **dropped the line `(KB-VIO-110 superseded)`** — i.e. **DEWEY originally framed the rates-vol-not-VIX-calls claim as SUPERSEDING a VIOLET knowledge-base entry.** A claim that supersedes a KB entry reads as **general**, not scoped to the mechanical-cushion case — which is materially stronger than the "adjacent, not refuting" grade above.
   >
   > **What this does and does not change.** It does **not** invalidate the trade: VIOLET's own constraint #1 bars a rates-vol expression here on *book* grounds (TRY-FIRE-004 already owns that leg — GATE-VIO-116), so "use rates-vol instead" is not available regardless of who is right about instrument pricing. **But it means the fleet holds two standing views pointing at opposite sides of the vol complex, with no adjudication between them, and one of them may formally supersede a VIOLET KB entry.** Routed to DEWEY (does item 2 supersede KB-VIO-110 *generally*?) and flagged to VIOLET. **Treat counter-case #8 as carrying more weight than its original wording, pending DEWEY's answer** — it is a reason to keep the size at the low end of the $300–400 band, not a reason to stand down.

9. 🟡 **The "index vol is cheap" argument is circular, and I want it stated plainly.** WALTER `SIG-W-20260725-015` (3Fourteen 7/23): index vol **16.6** vs single-stock vol **50.2**, record-low implied correlations, semis at second-highest constituent vol on record. Read one way that is *bullish* for this trade — index vol is cheap, buy it. But **record-low correlation is precisely the mechanism suppressing it** — and that is VIOLET's own counter-case #5 (KB-VIO-126). So: **we are buying something cheap *because it is being actively suppressed*. That is not a free lunch — the suppression has to break for it to pay.** Cheapness and pinning are the same fact wearing two hats.

10. ⚪ **Karsan's "vol shock into month-end"** (WALTER `SIG-W-20260725-006`) is *not* corroboration. Confidence 0.45, relayed secondhand from a video, no levels, WALTER's own base case is that it does not fire. **Do not count it as a vote.**

**The strongest single reason not to do this:** the base rate is **0-for-5**, we are paying mid-range prices, and the one thing that is different — the gamma sign flip — is a **single-source read** (HENRY's, corroborated 5-of-6 trackers). This trade is one inference deep. Size it that way.

---

## 8. ⬜ ZONE 2 — LIVE MARKS (fill Monday 7/27 before presenting for [Approve])

> **Everything below is EMPTY BY DESIGN.** The quotes in §9 are Friday-close / weekend-degraded and **must not be used to fill** (rule #4, `finding_option_marks_need_live_chain`).

```
Timestamp (ET):            ____
VIX spot:                  ____   (need <20)
VIX3M/VIX ratio:           ____   (need >1.0 — inversion = stand down)
★ VX FORWARD for chosen expiry: ____   ← THE number that prices this, not spot
Day color (rule #6):       VIX soft/green? [Y/N] — if N, state the break + why
Jazan/oil spillover check: VIX gapped up? [Y/N] — if Y, STAND DOWN
Chosen expiry:             8/5  /  8/19   (per §4 decision rule)
Long  __C  bid/ask: ____ / ____   OI ____
Short __C  bid/ask: ____ / ____   OI ____
NET DEBIT (limit):         ____   (must be ≤ $1.20; target ≤ $1.00)
Contracts:                 ____   = floor(budget ÷ (debit×100)), max 5
Total at risk:             $____  (≤$500 cap; $300-400 recommended)
Account:                   MAIN book (confirm BP — not the $241 satellite)
```

**Monday runbook (3 commands):**
```bash
cd "$(git rev-parse --show-toplevel)"
.venv/bin/python FORGE/tools/market-data/fetch.py price "^VIX" "^VIX3M"
.venv/bin/python AGENTS/TERRY/scripts/chain_fetch.py "^VIX" 2026-08-05 --type call --window 1.2 --no-cache
.venv/bin/python AGENTS/TERRY/scripts/chain_fetch.py "^VIX" 2026-08-19 --type call --window 1.2 --no-cache
```

---

## 9. Reference — Friday-close inputs (⚠️ STALE, context only, DO NOT FILL FROM THESE)

**Pulled 2026-07-26 12:28 ET. Freshest trade in set = 2026-07-24 20:14 — weekend marks.**

**Underlying (verified independently of VIOLET's packet — they agree):**
| Metric | Value | Source |
|---|---|---|
| VIX | **18.58** (−0.64%) | fetch.py, 7/24 close ✅ matches VIOLET |
| VIX3M | 20.51 | fetch.py |
| **VIX3M/VIX** | **1.104** | ✅ matches VIOLET's independently-derived 1.104 |
| VIX9D | 17.62 | fetch.py |
| VIX path | 7/22 **16.64** → 7/23 **18.70** → 7/24 **18.58** | yfinance history |

*(7/23's close at 18.70 is consistent with VIOLET's "Thursday's 20.31 intraday break was sold hard into the close.")*

**VIX calls, expiry 2026-08-05 (11 DTE) — the recommended chain:**
| Strike | Bid | Ask | Mark | Sprd% | IV% | OI |
|---|---|---|---|---|---|---|
| 20.00 | 0.80 | 2.00 | 1.40 | 85.7 | 152.5 | 1,950 |
| 21.00 | 0.32 | 1.78 | 1.05 | 139.1 | 149.0 | 2,175 |
| 23.00 | 0.16 | 1.27 | 0.71 | 155.2 | 159.0 | 1,216 |
| 25.00 | 0.15 | 0.97 | 0.56 | 146.4 | 174.4 | 12,935 |
| 26.00 | 0.09 | 0.81 | 0.45 | 160.0 | 175.0 | 1,658 |

**Indicative debit ranges (why this cannot be priced today):**
| Structure | At mark | Worst-case fill | Ratio spread |
|---|---|---|---|
| 8/5 **20/25** | $0.84 | $1.85 | **2.2× uncertainty** |
| 8/5 **21/26** | $0.60 | $1.69 | **2.8× uncertainty** |

**8/19 chain is UNUSABLE this weekend** — quotes are broken, not merely wide: the 20C marks 1.32 and the 25C marks 1.14, implying a 5-wide spread for **$0.18 net**, which is impossible. Many strikes show 0.00 bids. Market makers have pulled quotes for the weekend. **The 8/19 leg of the §4 decision rule must be re-pulled live Monday before it can be compared.**

---

## Decision

**Terry verdict: CONDITIONAL.** The expression is right: VIOLET's constraints produce a correct structure, the thesis gate is met on her side, it is genuinely additive to the book rather than a re-stack, and max loss is small and hard-defined. I have moved the expiry to **8/5** on spike-capture grounds and rejected **7/29** outright as a settlement trap.

**What makes it conditional, in one line:** at 85–160% bid/ask widths, *the fill decides this trade, not the thesis* — and the fill cannot be known until Monday.

**Three ways this becomes a clean NO before any money moves:**
1. Monday's live market won't come to **≤$1.20** net debit → **no trade.**
2. **VIX ≥20** or **VIX3M/VIX <1.0** at the fill → window expired, **stand down.**
3. **VIX gaps up Monday** on Jazan/oil spillover → we are the late money, **stand down.**

**Recommended if it clears:** 8/5 **20C/25C**, **3 spreads at ≤$1.20** (~$360 at risk), main book, limit order on the spread, exit at the 7/30 boot regardless of P/L.

- [ ] **APPROVE in principle** (unblocks the Monday live pull; final fill still comes back to you)
- [ ] **REJECT**
- [ ] **REWORK:** ______

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---
*Thesis owner VIOLET — TERRY does not own the vol call and has not re-underwritten it. Structure, expiry, strikes, sizing, entry discipline and the counter-case additions (§7 items 7–10) are TERRY's. Quotes in §9 are weekend-stale by construction and are barred from use at fill.*
