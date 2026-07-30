# PRE-STAGED — Bank-Put Reshape Wake-Up Brief
**Status: PRE-STAGED, CONDITIONAL on tomorrow's HY OAS print (7/29 FOMC-day data, publishes ~7/30 via FRED).** This is NOT a trade recommendation and does not by itself trigger anything. It exists so that IF GATE-RESHAPE-BC's HY leg fires on the sustain-confirm, Will/PROME/TERRY have the credit-side context on hand instead of re-deriving it live.

**Author:** LIQUID · **Date:** 2026-07-29 ~22:5x ET · **Trigger being pre-staged for:** `PROME/proposals/2026-06-26_bank-put-reshape-roll.md` (GATE-RESHAPE-BC, `PROME/GATES.tsv`)
**Construction is TERRY's. Decision is Will's (root rule #5). This brief supplies the credit read only.**

---

## 0. Where the gate stands right now

HY OAS: 268(7/22) → 277(7/23) → 279(7/24) → 281(7/27) → **284 (7/28, own FRED pull tonight)** — **sustain 2-of-3 sessions ≥280**. Tomorrow's print (7/29 FOMC-day data, publishes ~7/30) is session 3 and decides:
- **Confirms (≥280 on 7/29):** GATE-RESHAPE-BC's HY leg (level-only, LIQUID-owned) FIRES → proposal goes to Will per the gate's registered consequence.
- **Breaks (<280):** sustain resets; per the gate's own 6/26–7/1 tagged-not-sustained precedent (283/280/275/274, all failed to hold), the HY leg stays NOT-FIRED.

Full branch detail and the discipline against reading a level-only fire as "X1 MET" → `workbook/KB.tsv` KB-LIQ-089.

**The proposal's OTHER firing condition — WAL Q2 print 7/21 AMC — has already resolved, and resolved NOT-FIRED.** See §2.

---

## 1. What has changed since 6/26 (levels)

### Credit
| | 6/26 (proposal's own reference) | 7/29 (tonight) | Δ |
|---|---|---|---|
| HY OAS | 275bp (6/30 print, proposal's stated thesis-base) | **284bp [7/28]** | +9bp, and now above the X1 line (was below it at registration) |
| Path: | n/a | 268→277→279→281→**284**, sustain 2-of-3 | decisive print 7/29 data |

### Rates (path-b driver)
10Y sat in the low-4.3s/mid-4.4s through most of the proposal's registration window; now **DGS10 4.61 [7/28 FRED] / ~4.62 intraday [7/29 live, ^TNX +0.39%]**, with the duration regime independently RE-ESTABLISHED on both legs since 7/22 (30Y six straight closes >5.00, 10Y six straight >4.50 — KB-LIQ-086). This is a materially firmer rates backdrop than the proposal was built against.

### Prices (underlyings, own live pull tonight vs the proposal's 6/26 ~10:50 ET reference)
| Ticker | 6/26 ref | 7/29 live | Δ |
|---|---|---|---|
| KRE | $74.93 | $76.18 (−0.79% today) | +1.7% |
| **WAL** | $81.81 | **$80.70 (−3.53% today)** | −1.4% |
| OZK | $51.80 | $51.55 (+0.10% today) | −0.5% |
| ZION | $69.07 | $68.92 (−0.86% today) | −0.2% |
| HBAN | $17.81 | $16.84 (−2.66% today) | −5.5% |
| **TLT** | $87.21 | **$82.85 (−1.65% today)** | **−5.0%** (largest mover) |
| APO | $120.32 | $119.77 (−3.95% today) | −0.5% |

TLT's −5.0% move is the standout — it directly implicates the proposal's path-(b) AOCI/rates leg (§4 below).

### WAL single-name (path-c)
**REG-T-02 (WAL < $78 binary):** current $80.70, **≈3.46% away** ($80.70 vs $78). Not close to a fresh fire.

---

## 2. The WAL-print leg is CLOSED, and it closed NOT-FIRED

The proposal's path-(c) catalyst — "WAL Q2 print Jul-21-26 AMC" — has already happened. **REGINALD Stage-1 (7/21) + Stage-2 (7/22) verdict: NOT-FIRED, no GATES consequence.**

- EPS $2.36 (beat $2.33 consensus); ex-fraud NCO 37bps (NEUTRAL band [25,40], below the >55bp surprise line); the $99M life-sci/office CRE loan moved to **nonaccrual, $0 charged off** (disposition letter final: **(B)**, softer than a realized loss).
- **REG-26 (the surprise-tier prediction) DISCONFIRMED.** REG-25/REG-24 pushed OPEN to Q3 (10-Q + the pending appraisal on the $99M loan).
- Stock reaction: WAL closed **+3.61%** the day after the print (capital-return pivot — $150M buyback, loan-growth guide cut explicitly to fund it — into a crowded short), i.e. the print's own tape reaction ran counter to the bear thesis short-term.
- REGINALD's own framing: "grind INTACT-but-NARROWED... WAL-GRIND card stays HELD-DORMANT."

**Consequence for this brief:** the proposal's original two-catalyst structure (HY>280 sustained OR WAL Q2 print) is no longer symmetric. One leg already fired-null with a real, dated, primary-sourced verdict against it. If the gate fires tomorrow, it fires on the OTHER leg only — which changes what a fire actually means (§3).

---

## 3. Credit-side read: does a firing tomorrow map to the thesis the proposal was registered under?

**Short answer: only partially, and on a narrower, weaker version of the thesis than 6/26 registered.**

The proposal's own framing (§ "core insight") split the book into three catalyst-dated paths: **(a) broad regional — already TRIMMED at registration; (b) AOCI/rates — no single date, needs 2027 duration; (c) WAL single-name — dated to the Jul-21 print.** Path (c) has since resolved null (§2). Path (a) was already discounted at registration. **What's left standing, if tomorrow's print fires, is functionally path (b) — a rates/AOCI-duration mismatch — with a LEVEL-only credit tag riding alongside it, not a fresh credit-recognition event.**

That reading is reinforced, not weakened, by tonight's own tier decomposition (KB-LIQ-088) and by BROCK's independent 7/27 verdict (`inbox/2026-07-27_from-BROCK_x1-retest-verdict-hy-279.md`):

- BROCK ran the tranche decomposition on the 7/22→7/24 leg and found it **BB-led, proportionally** (BB +7.01% vs CCC +1.53% on the acute move) — beta/level repricing, not credit recognition. **X1's wrapper-leads half independently failed on 7/27, symmetrically** (managers led the recovery up, wrappers lagged; wrappers then also lagged the renewed widening) — "beta-insensitivity, the signature of a mark-to-model asset class, not suppressed recognition."
- My own extension through 7/28 (KB-LIQ-088) shows the same shape continuing: BB proportionally +10.19% vs CCC +2.45% over the full 7/22–7/28 window; the CCC/BB and CCC/HY ratios have been COMPRESSING since 7/22 (a real quality-recognition event would EXPAND them), even as the raw CCC-BB gap keeps widening on pure level-effect (824→832bp).
- The later leg of the move (7/23→7/28, HY +7bp) ran **while DGS10 FELL 10bp** (4.71→4.61) — decoupled from a simple rates-mechanical read, which argues the widening is a real (if BB-led, beta-flavored) spread move, not a yield-curve artifact — but "real spread move" and "credit recognition" are not the same claim, and BROCK's wrapper test speaks to the latter.

**Net:** if the gate fires tomorrow, the honest framing is *"a level-only credit tag fired alongside a live rates/duration channel, on a book where the WAL-specific leg already resolved null and the wrapper-lead confirmation test has twice failed"* — not *"the 6/26 credit-bear thesis has been confirmed."* Route this framing to whoever picks the proposal up; don't let a bare "280 sustained" headline stand in for it.

---

## 4. What the proposal would need re-marked before anyone acts on it

**The proposal's own position tables are already flagged stale** — its 2026-07-18 banner states the §A/§C instrument list (strikes/expiries) no longer matches the live broker book as of the 7/16 FORGE reconcile (WAL strikes wrong, OZK expiries wrong, TLT expiry wrong, KRE tranches differ, HBAN is exit-thesis dust). That banner is now **11 days further stale on top of the original 3-week gap**. Per the proposal's own instruction: *"do NOT execute from the §A/§C tables — rebuild the harvest/keep arithmetic from the fresh broker export."* This brief does not change that instruction; it reinforces it.

Additional re-mark items surfaced by tonight's pull:

- **TLT is down 5.0% since 6/26 ($87.21 → $82.85)** — the largest mover of any underlying in the book. If the harvest→roll into TLT 2027 puts (the proposal's "V1 — recommended" variant) was executed at any point, those puts are considerably more valuable today than the 6/26 marks used to size the recommendation; if it was NOT executed, the entry price for the same 2027 strikes is materially different than what the proposal quoted. **Position truth is off-repo/broker-direct (rule #4) — confirm which state applies before assuming either.**
- **The proposal's own path-(b) kill/confirm line reads CONFIRM at current levels, not KILL:** its stated test is *"confirm = 10Y sustains >4.40 / breaks higher → AOCI widens; kill = 10Y rallies back <4.20 sustained."* Current 10Y (4.61–4.71 range across the last 6 sessions) sits well inside CONFIRM territory. If path-(b) is re-graded fresh at fire-time, its own gate reads CONFIRM.
- **Vol regime is materially higher than the proposal's registration window.** VIX is **20.66 [7/29 live, +13.45% today]** vs high-teens for most of the 6/26–7/22 period per this file's own STATUS history (e.g. 15.51 [7/10], 18.71 [7/17]). Any option chain re-pulled at fire-time will price meaningfully more expensive than a naive extrapolation of 6/26 quotes — re-pull the live chain, don't scale the old one.
- **Brent $89.36 (+6.27% today)** — a live geopolitical leg (HAWK/BRENT domain, WALTER SIG-W-20260728-013 "pause broken, IRGC missiles/US base") sits in the same tape as tomorrow's decisive HY print; flagged as background only, not scored here.

---

## 5. Explicit conditionality

**This brief is PRE-STAGED and CONDITIONAL.** If tomorrow's print breaks the sustain (Branch B, KB-LIQ-089), GATE-RESHAPE-BC's HY leg stays NOT-FIRED, this brief has no live consequence, and should sit as background only — do not surface it to Will as an active decision. If the print confirms (Branch A), the proposal goes to Will per the gate's registered consequence; §3 and §4 above are the context that should travel with it. **No trade recommendation is made or implied anywhere in this document — construction is TERRY's, decision is Will's.**
