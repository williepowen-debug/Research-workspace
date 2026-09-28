# DISPOSITION READ — QQQ $730P ×10 + USO $159C ×2, both Sep-30-2026 (Fidelity)

**Date:** 2026-09-28 Mon, built 10:51–10:5x ET (`date` 10:51:11 at boot). **Spawn:** PROME `prome-7f`, Tier 1, on WQ-315 (Will, verbatim: *"Approve WQ-315. Bring TERRY in now for the QQQ and USO expiries. … Recommendations only; orders remain mine. Keep my TLT hold-to-expiry ruling unchanged."*)
**Id:** `MGMT-QQQ730P-USO159C-SEP30` (management read — no SETUPS row, registered in `setups/INDEX.md`; SETUPS/TRADE_BOOK rotations still owed).
**Thesis owner:** none on file for either line (Will-direct, off-thesis class — `FORGE/STATUS.md` § Off-thesis; card grep 9/27 SEARCH-NOT-FOUND).
**Terry verdict:** **SELL both — QQQ 730P: SELL today (primary); USO 159C: SELL today (low stakes).**
**Confidence in the read:** Medium (quotes are one-vendor screening grade, ~15 min delayed — see §2).
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** Recommendations only; orders are Will's.

---

## 1. Position-open status

| Line | What the repo establishes | What only Will's broker can confirm |
|---|---|---|
| QQQ $730P Sep-30-2026 ×10 | Open at the **Fri 9/25 close**: bought 9/24 −$2,486.63 (Activity row 2), $1.30 mark, $1,300 value, −$1,186.63 / −47.73% (`FORGE/STATUS.md`, ANVIL reconcile, commit f39c70073) | Anything after the 9/25 close — **UNVERIFIED** today. A sale, a working GTC order, or a partial fill this morning would not be in the repo |
| USO $159C Sep-30-2026 ×2 | Open at the 9/25 close: bought 9/18 −$921.33 (row 8), $0.65 mark, $130 value, −$791.33 / −85.89% (same source) | Same — **UNVERIFIED past 9/25** |

⚠️ Account type is **INFERRED** (Traditional IRA, by position-set match; header cropped). It matters for §4.

## 2. Live quotes (yfinance via `chain_fetch.py --no-cache`, the only feed at this desk)

⚠️ **One vendor, screening grade.** Spot is real time. Option bid/ask age is **unknown**. The 10:53 pull flagged `DIRINC` on the QQQ strip: spot fell but put quotes also fell. That means the option quotes lag spot by about 15 minutes (last option trade 10:37, fetch 10:53). **Will reads Fidelity's own live bid before any order.**

| | QQQ $730P Sep-30 | USO $159C Sep-30 |
|---|---|---|
| Underlying (fetch.py, 10:53 ET) | **QQQ $732.18, −1.65%** today (SPY −0.88%, VIX 15.91 +7%) | **USO $152.96, +3.12%** today (WTI Nov CL=F $94.51 +2.27%; ⚠️ BZ=F −4.86% is a Brent front-contract last-day artifact, do not read it) |
| Option bid / ask (pull time; quote time) | 10:51: **2.23 / 2.24** (last trade 10:36) · 10:53: **2.18 / 2.20** (10:37) | 10:51: **0.55 / 0.62** (10:25) · 10:53: **0.58 / 0.67** (10:25) |
| Liquidity | Vol 8,335 today · OI 46,907 · spread ~0.5–0.9% — deep | Vol 151 · OI 1,135 · spread **12–14% wide** — sell at or near bid, don't chase mid |
| Distance to strike | **Put is OTM by ~$2.2 (0.3%)** — QQQ must close below $730 on Wed for any intrinsic | **Call is OTM by ~$6.0 (4.0%)** — USO must close above $159 |
| Worth if SOLD NOW (at bid, gross) | **≈ $2,180–$2,230** (vs cost $2,486.63 ⇒ ≈ −$257 to −$307 realized, before ~$6.50 commission at an assumed $0.65/ct) | **≈ $110–$116** (vs $921.33 ⇒ ≈ −$805 to −$811 realized, before ~$1.30) |
| Worth at 9/25 close (for contrast) | $1,300 | $130 |
| Likely worth at expiry | **$0 if QQQ ≥ $730 at Wed close.** Each $1 below $730 = $1,000. Beats selling now only if QQQ closes **≤ ~$727.8** (−0.6% more) | **$0 if USO ≤ $159.** Beats selling now only if USO closes **≥ ~$159.6** (+4.3% more) |
| Rough odds (lognormal, 2.2 sessions, IV band stated) — INFERRED, a model not a measurement | P(ITM) **38–42%**; P(beats selling now) **29–36%** (IV 13–20%) | P(ITM) **16–20%**; P(beats selling now) **14–18%** (IV 42–50%) |

## 3. Recommendation

### QQQ $730P ×10 — **SELL, today (Mon 9/28), all 10**

1. **It has handed back most of its loss in one session.** $1.30 → ~$2.20 on today's −1.65% tape; it is now within ~10% of cost. Holding from here is the same as buying a fresh **2-day, slightly-out-of-the-money $2,200 put today** — and there is no card, no invalidation and no thesis owner for that trade. **Good thesis, bad trade is still a bad trade:** a 2-session ATM put is a coin flip whose price already equals the market's fair value, with theta taking roughly half of what's left each day QQQ goes nowhere.
2. **Root rule #6 (day colour) favours selling today.** The rule buys puts on green days; the exit mirror is that a put is sold into a red day, when it is richest. Today is red for QQQ (−1.65%). **SELL does not break root rule #6. HOLD does** — it is the implicit re-purchase of a put on a red day. No break is claimed.
3. **Book context (WQ-297 A: the book is one oil bet).** This put is **not a hedge of that bet** — it is a separate, oppositely-signed equity-down bet. What it could offset: AAPL 10 sh ($3,411 at 9/25c) plus APD/VLO (~$950) — about **$4.4k of equity**. At ~−0.45 delta × 1,000 shares, the put carries roughly **$330k of delta-adjusted short-QQQ exposure** (0.45 × 1,000 × $732, INFERRED delta — yfinance gives no greeks), i.e. ~75× the equity it could hedge. **It does not hedge the oil sleeve at all** (a sell-off with oil up — today's tape — is the one case where both win; oil down + equities up loses on both). It is a tactical short sized at 6.7% of the account in premium.
4. **The honest counter-case (stated, not dismissed):** BOND's 9/28 boot reads a global sell-off (30Y 5.55% intraday, HY 293bp, ~97th percentile, 7bp from 300). If that continues into Wed, the put pays: QQQ $725 ⇒ ~$5,000, $720 ⇒ ~$10,000. **That is a view Will may hold; it is not a rule on this desk.** If Will wants to keep the equity-down view, the construction answer is **later tenor** (construction rule #16 — match expiry to the view's horizon), bought on a green day with a card. That is a new trade, **not proposed here.** A partial hold (sell 5–7, keep 3–5) is a trim. Root rule #7 reads a trim as a broken thesis, and this line has no thesis to break. It is Will's call to make only if he holds the view himself.

### USO $159C ×2 — **SELL, today (Mon 9/28)** — low stakes

1. ~$110 left of $921. Needs +4.3% in 2.2 sessions to beat selling now. Odds are ~15%.
2. **It is more of the same bet.** WQ-297 A: the book is already one oil bet (USO 37 sh $5,488 + VLO). The call adds oil-up convexity to the dominant exposure and diversifies nothing.
3. **Root rule #6:** a call is sold into a green day; USO is +3.12% today. **SELL does not break the rule; HOLD is the implicit re-buy of a call on a green day.**
4. **Catalyst inside the window:** EIA Weekly Petroleum Status Report **Wed 9/30 10:30 ET** (API Tue ~16:30 ET). That is the only thing that plausibly moves USO +4% before expiry, and it is priced into the 45%+ IV.
5. **HOLD is not a mistake of consequence** — it is a ~$110 lottery on the Wed EIA print. If Will prefers the lottery, the one thing he must not do is let it finish ITM unattended (§4).

## 4. Decision deadlines and Wednesday mechanics

| | QQQ $730P | USO $159C |
|---|---|---|
| **Recommended action window** | **Today Mon 9/28, before 15:45 ET** (red day, quote 1¢ wide) | **Today Mon 9/28, before 15:45 ET** (green day) |
| **Hard deadline if held** | **Wed 9/30, 15:00 ET** — place the sell order no later than this | **Wed 9/30, 15:00 ET** (after the 10:30 EIA print) |
| Why 15:00, not 16:00 | Fidelity **publishes no time for a close it places itself** (TLT 82P card §4, read 9/26). Its Activity shows 4 "OPTION LIQUIDATION" rows, each on the contract's own expiry day (D-60, mechanism UNKNOWN). Last-hour expiry gamma on a 1,000-share-equivalent line is also violent. | Same broker risk; spread is already 12–14% and widens into the close |
| If ITM at the Wed close and not sold | **VERIFIED (Fidelity Options Agreement, read 9/26):** auto-exercise at ≥ $0.01 ITM. Exercise of 10 puts with no QQQ shares = **sell short 1,000 QQQ (~$730,000)**. **VERIFIED (published): an IRA cannot sell short.** What Fidelity then does — close before 16:00, exercise and buy in, or block — is **UNKNOWN** (same named unknown as the WQ-302 cards). A slightly-ITM put ($0.01–$1) is exactly this case | Exercise of 2 calls = **buy 200 USO at $159 = $31,800 cash**; the account holds **$17,512.69** (9/25c) ⇒ **insufficient**. Fidelity's action is **UNKNOWN (INFERRED: it would close or restrict)** |
| Do-Not-Exercise instruction | Deadline **16:15 ET** (web page) / **16:20 ET** (Options Agreement), by phone 800-343-3548. **DNE on an ITM option forfeits its value — dominated; never use as the plan** | Same |
| If OTM at the Wed close | Expires worthless ($0), or Fidelity "liquidates" it for pennies (the D-60 pattern: +$0.99 to +$3.77) | Same |
| Last trading time Wed | **INFERRED 16:00 ET** for expiring equity/ETF options (standard; not checked at Fidelity) | Same |

**Known vs inferred:** VERIFIED = the ≥ $0.01 auto-exercise rule, the 16:15/16:20 DNE deadlines and the no-short-in-IRA rule, all from Fidelity's published pages read 9/26 (TLT 82P card §4). INFERRED = the 16:00 last-trade time, the account being an IRA, and the call-side cash handling. UNKNOWN = what Fidelity does and **when** on expiry day (D-60).

## 5. Broker information Will must supply

1. **Both lines still open, at ×10 and ×2**, on the Fidelity positions screen now — nothing sold or partially filled since the 9/25 close.
2. **Any working orders** (GTC sells) on either contract — so a new sell is not a double-sale.
3. **Fidelity's live bid/ask** on each contract at order time. The desk quote is delayed, one-vendor, screening grade.
4. *(Only if Will holds either line into Wednesday)* — one call to Fidelity, folded into the WQ-302 / D-60 question: **what time on expiry day Fidelity closes an ITM or near-ITM option itself in this IRA, and what it charges.**
5. *(Low)* The account type — Traditional IRA is INFERRED — and the per-contract commission (assumed $0.65).

## 6. Not touched (noted only)

- **TLT $77P Sep-30 ×20** — Will's **HOLD to expiry** ruling stands unchanged (WQ-168 ④ / WQ-217; NO ADD, WQ-280). Harvest line ≥ $0.3469 fees-in; not re-graded here.
- **KRE $60P Sep-30 ×2** — **LAPSE** as ruled (WQ-168 ⑥).

## Decision

**RECOMMENDATION ONLY — orders remain Will's.** SELL QQQ 730P ×10 and USO 159C ×2 today (Mon 9/28) before 15:45 ET, at or near Fidelity's live bid; if either is held, hard sell deadline Wed 9/30 15:00 ET. **APPROVAL REQUIRED — Will must approve/reject before execution.**
