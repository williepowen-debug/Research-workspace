# CONDITIONAL CARD — KRE (regional banks ETF) — ADD long puts — **NOT constructible today**

**Date:** 2026-09-30 Wed, written 08:1x ET (`date` 08:10:35 before drafting) · **Id:** `TRY-COND-KREADD` (conditional, no fill; registered in `setups/INDEX.md`, no SETUPS row — that ledger sits at 98% of its read budget with a rotation owed)
**Asked by:** Will, relayed by REGINALD 2026-09-29 ~18:2x ET, verbatim: *"Send this to TERRY for a card on adding KRE puts."* and ~19:2x ET: *"Send the attribution report to TERRY for the card."* **This relays an ASK for a card, not an approval to fill.**
**Thesis owner:** REGINALD (regional-bank credit). **Construction:** TERRY. **Approval:** Will (root rule #5).
**Terry verdict:** **CONDITIONAL — NO FILL TODAY. Four standing rules each block a fill on their own; the card pre-registers what would arm it.**
**Confidence in the structure:** Medium (structure checked; moment properties deliberately NOT graded — construction rule #14).
**`$0` MOVED · NO ORDER · NO THRESHOLD CREATED OR MOVED** — every arm leg below is an instrument that already exists at its owner.

---

## 1. One-line setup

Add bearish regional-bank exposure through KRE puts, max loss `$500`, **only once the mechanism REGINALD's desk underwrites — regional credit reaching bank balance sheets — shows up**, not on the price move alone.

## 2. Why there is no fill today — each row blocks by itself

| # | Standing rule | Today's reading (source, date) | Blocks? |
|---|---|---|---|
| **a** | **Fresh capital only on a fired trigger** (Will 6/26; `RISK_RULES.md` durable finding #1) | KRE's own trigger `REG-T-01` (KRE close < $60) is **UN-FIRED**: $69.83 [9/29 close], $9.83 / 14.1% away (REGINALD STATUS 9/29). The fired trigger on that desk is `REG-T-02` (WAL < $78, fired 9/1), and it **already carries its card** — `TRY-WAL-ROLL70`, $220 deployed. A trigger licenses the card registered to it. Pointing a WAL trigger at a KRE add changes the underlying, which makes it a new deployment needing its own gate (the same guard as construction rule #21's roll definition) | **YES** |
| **b** | **X1 sizing gate CLOSED / DON'T-SIZE** (8/28 adjudication; DOCKET L494) | Conjunctive; BROCK's wrapper half adjudicated NOT ARMED (LIQUID STATUS 9/29). LIQUID's HY half reads >280 on 9/25 and 9/28, which does not open it. Bank-put fresh capital has sat behind the X1 banner since the 8/4 reshape card. **Re-sits Fri 10/2 (L494).** Any override is Will's, Tier 3 | **YES** |
| **c** | **Root rule #6 — puts on GREEN days** | KRE 9/29 **RED** (−1.02%, close near the $69.46 low). Pre-market 9/30 08:08 ET $69.85 (+0.03%, a quote). Today's colour: see § 5. No measurement exists that refutes the colour proxy, so no break is available | today: see § 5 |
| **d** | **Construction rule #23 — name the driver before you add** | REGINALD's attribution (`AGENTS/REGINALD/reports/2026-09-29_selloff_attribution_and_preprint_observables.md`, `5e973d37a`): leg 2 (9/15→9/29) is **financials sector −5.0 of −5.9 log-%**, KRE residual **+1.1%**; the 14-name cross-section sorted on **SIZE (ρ −0.72)**, while his credit matrix sorted the **wrong way (+0.48)**; preferreds/HYG/BIZD barely moved (−1.4 / −1.5 / −0.8 vs KRE −5.8); H.8 through 9/16 and H.4.1 through 9/23 all 🟢 (NDFI lending +1.1%, discount window $6.2B = 60-week median). **The existing KRE puts have been paid by a mechanism nobody underwrote (a sector/size repricing).** Under #23 that is evidence **against** adding, not for it. No name ⇒ no add | **YES** |

**His read, kept whole because it is the card's centre:** *"The tape has moved ahead of any evidence I can produce; the evidence I can produce says nothing has transmitted to regional balance sheets yet, and the last two weeks priced SIZE, not the credit ranking this desk exists to measure."*

## 3. What is already on (position truth off-repo; FORGE 9/29 ANVIL reconcile via REGINALD, marks 9/29 13:4x)

| Leg | Qty | Mark | Note |
|---|---|---|---|
| KRE $60P Dec-18-2026 | 5 (2 + 3) | $0.46 ⇒ ≈$230 | −82% / −84% on cost |
| KRE $60P **Sep-30-2026** | 2 | $0.02 | **expires today — LAPSE (WQ-168 ⑥)**; see § 9 |
| KRE $25P Jan-15-2027 (RH) | 1 | ~$0.01 | deep-OTM lottery (D-54) |
| WAL $70P Dec-18-2026 (RH) | 1 | ≈$2.65 | `GATE-TERRY-ROLL70-EXIT` |

**Independence (RISK_SCORING §2b):** every line shares one falsifier — *no regional credit transmission by the Q3 print cluster (~10/20–28)*. **N_eff = 1** for this sleeve. An add is more size on the same view, so **construction rule #17 binds: the size-increasing branch carries the higher evidential burden.** WQ-297 A (Will accepted the book's concentration, 9/25) neither requires nor forbids this card; how a KRE put behaves in the book's worst scenario (oil down AND yields down) is **UNMEASURED** and not claimed.

## 4. ARM — the card becomes a fire card only when ALL THREE hold (proposed for registration; every leg is an existing owner instrument)

| Leg | Condition | Owner / grader |
|---|---|---|
| **A1 — evidence** (any ONE) | ① `REG-T-03`: HY OAS > 320 on its own letter (×3), **with** REGINALD's bank-credit cross-check NOT reading `BANK-ABSENT` · ② the Q3 print-cluster breadth test **fails** (DOCKET **L180**) · ③ `REG-T-01`: a KRE close < $60 | REGINALD |
| **A2 — sizing** | X1 **OPEN** at or after the 10/2 L494 sitting, **or** Will's explicit Tier-3 word overriding X1 for this card | BROCK / LIQUID; Will |
| **A3 — fill day** | a KRE **GREEN** session (root rule #6), or the refuting measurement written on the card in figures before the fill (`RISK_RULES.md` § "Breaking root rule #6") | TERRY, live at fill |

On arm, TERRY writes the fire card from the broker-checked chain (RISK_RULES 5b: vendor marks are screening only) and Will approves or rejects. **Arming is not approval.**

## 5. Structure — pre-screened (structure properties only; the debit, IV and spread are graded ONCE, at fire)

| Property | Rule on this card | Reading |
|---|---|---|
| **Tenor** | The listed monthly **60–90 DTE on the arm day**, preferring the first that clears the Q3 print cluster (the desk's new-deployment band; construction rule #21 binds in full) | Today: **Dec-18-2026 = 79 DTE**. Dec-18 leaves the band after 10/19; Jan-15-2027 enters it 10/17 |
| **Strike** | nearest listed to **~7% below the arm-day close** — inside construction rule #18's 10% line, so the move it needs is one a sector repricing has already produced once this quarter (KRE −10.2% since 8/13) | Today's reference: **$65** on $69.83 (−6.9%) |
| **Size** | `floor($500 ÷ (broker ask × 100))`; max loss = premium ≤ **$500 = 2R** | Reference only, not a price: Dec-18 65P last print $1.15 (9/29 11:15, stale vs the close) ⇒ ~4 contracts |
| **Liquidity / quote sanity** | two-sided, no `LOCK`/`XSD`/`DEAD`/`NOBID` on the leg (`chain_fetch.py --legs`) | see § 5b |
| **Alternative** | Dec-18 66/62 put spread (sell the richer deep wing, construction rule #18(b)) — only if the outright's IV is rich at fire | graded at fire |

**Vehicle question, not TERRY's to answer:** REGINALD notes the large-bank instruments (KBWB −7.4%, IAT −7.7% vs KRE −5.8%) carried leg 2 better. If the view is *"the financials repricing continues"*, KRE is the weaker vehicle for it. If the view is *"regional credit transmits"*, KRE is right — and that is the view still waiting on § 4 A1.

### 5b. Structure check at the open

*Filled 2026-09-30 10:23 ET (`date` 10:23:52), TERRY interactive session — the 08:1x spawn left this section as a placeholder; it was not filled before 10:23.* **Screening marks only (RISK_RULES 5b) — the vendor bid/ask has no timestamp; a fill is priced from the broker chain.**

| Check | Reading (`chain_fetch.py KRE 2026-12-18 --type put --no-cache --legs 65,66,62`, spot $69.89) | Result |
|---|---|---|
| Quote sanity on the named legs | 65P / 66P / 62P: no `LOCK`/`XSD`/`DEAD`/`NOBID`; `--legs` rc=0 | PASS |
| Reference strike Dec-18 **65P** | bid **1.23** / ask **1.34**, spread 8.6%, IV 25.5%, OI 10,648, vol 507 (last trade 09:50) | liquid; two-sided |
| Reference size | `floor($500 ÷ $134)` = **3 contracts** ≈ $402 at the ask (replaces the § 5 "~4" read off the stale $1.15 print) | reference only |
| Alternative 66/62 spread | 66P 1.37/1.66 (19% wide) · 62P 0.62/0.82 (28% wide) ⇒ mid debit ~0.80, worst-case 1.04 on 4-wide | wide legs; graded at fire only if outright IV is rich |
| Day colour (A3) | KRE **$69.89, +0.09%** at 10:23 — a moment reading, not the session's colour (that is the close) | not graded: A1 and A2 are unmet, so A3 has nothing to bind |

**Changes nothing:** the card stays CONDITIONAL with no fill, because § 2 (a), (b) and (d) each block independently of today's quotes.

## 6. Risk and management (forward-looking; binds from the fill)

- **Max loss:** the premium, ≤ `$500`.
- **Invalidation (REGINALD's refuters, any one):** B-tier OAS back under 300 · KRE closes ≥ $72.74 (the 9/16 gap-down close) · HY OAS under 280 · a clean Q3 print cluster (L180). On one: sell at the broker bid next session.
- **Harvest (durable finding #9):** sell half at **2× the fill debit** on the broker bid; the rest rides to the L180 grade or a refuter.
- **Time stop:** review at 30 DTE (for Dec-18: Wed 11/18); no roll rule is pre-registered, so none exists (Non-Negotiable #6).
- **Event map:** Q3 regional prints ~10/20–28 · NFP Fri 10/2 · FRED tiers daily ~AM.

## 7. Why not / counter-case

**The best case against this card's own design:** waiting for credit confirmation means buying after more of the move and at higher implied vol; the card may arm late or never, and a correct price call would then be missed. REGINALD names the trap: *"the price is ahead of the evidence — the setup the thesis wanted, and the moment it is easiest to over-read."* If Will holds the view on price alone, the honest route is his own Tier-3 word on § 2 (a) and (b). **TERRY does not recommend it:** the only fresh evidence (the attribution) points the other way.

## 8. Decision

> **For Will:** register § 4 (A1–A3) as the arm conditions for a KRE-put add — **no capital moves**; a fire produces a card, not an order. Or decline and let the ask close. TERRY recommends **register**.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

## 9. Record — KRE $60P Sep-30-2026 ×2 expires today (WQ-168 ⑥ LAPSE)

- **Graded on:** KRE's official close **today, Wed 9/30, vs $60.00.** Reference: $69.83 [9/29 close] = **$9.83 / 14.1% above the strike**; pre-market $69.85 (08:08 ET, a quote).
- **Close ≥ $60 (expected):** expires worthless ⇒ realized **−$454.00** (2 × $2.27 × 100, REGINALD's cost figure from the 9/29 FORGE reconcile; FORGE governs the cent). Last print $0.02 on 9/25; bid/ask 0.00/0.00 pre-open.
- **Close < $60:** would need −14.1% in one session; auto-exercise ≥ $0.01 ITM ⇒ short 200 KRE; account handling UNKNOWN (D-60). Not expected; recorded so the branch is not unseen.
- No action owed. `$0`.
