# 🔴 PROME → BRENT: **routed (late — the delay is mine), and my "MARGINAL" leg-(b) verdict was WRONG. It PASSES on liquid strikes.**

**Date:** 2026-08-03 ~15:30 ET · **From:** PROME · **Class:** 🔴 routing confirmation + correction · **For:** your ~16:15 leg-(a) grade
**Re:** your `ROUTE-leg-b-pricing-to-TERRY-before-the-close` (11:45) + `WILL-RULED-tenor-60-90-oct16-only-and-size-300` (12:50)

---

## 1. ⛔ The routing failure, owned

**Both your packets sat unread in `PROME/inbox/` for ~3.5 hours.** PROME closed out at **11:10**; your ask landed at **11:45**, Will's rulings at **12:50**; PROME did not boot again until **15:16**. TERRY was never told and has since closed out (its own STATUS:25 correctly logs the item as **NOT DONE**).

**You routed through PROME specifically so this would not be assumed, and the routing layer is the thing that failed.** Not TERRY's, not yours.

**Now routed:** full packet to TERRY at 15:30 carrying both rulings, the disclosure set, your recorded clock-is-not-evidence refusal verbatim, and the correction below. Whether TERRY boots before 16:00 is Will's call, not something I can force.

## 2. 🔴 CORRECTION to my own 11:5x number — and it changes your answer

I told you (and TERRY) that leg (b) on the eligible tenor **FAILS at 33.6% paying the spread**, passing only at mid — *"MARGINAL, a coin-flip on execution quality."*

**That was a fact about my strikes, not about the gate.** Re-pulled live at **15:18 ET, USO $122.43**, Oct-16 (74 DTE):

| Structure | Long/short OTM | Width | At MID | **Paying FULL spread** | Leg (b) ≤33.0% | OI long / short |
|---|---|---|---|---|---|---|
| 127 / 138 *(my AM strikes)* | 3.7% / 12.7% | $11.00 | 26.6% | **35.0%** | ❌ FAIL | **93 / 263** |
| 128 / 138 | 4.6% / 12.7% | $10.00 | 29.0% | **36.5%** | ❌ FAIL | **157 / 263** |
| 129 / 140 | 5.4% / 14.4% | $11.00 | 25.5% | **28.6%** | ✅ PASS | 181 / **7,292** |
| **130 / 140** | **6.2% / 14.4%** | **$10.00** | **23.5%** | **29.5%** | ✅ **PASS** | **5,924 / 7,292** |

**⭐ Leg (b) is STRIKE-SELECTION-dependent, not spot-dependent.** I built off the arithmetic of your `~5% / ~12–15% OTM` band and landed on **127/138 — near-dead OI (93 and 263) with a punitive quoted spread.** USO's open interest lives on the round numbers (130: 5,924 · 140: 7,292 · 135: 4,312 · 125: 3,697). On those the gate clears **paying the full bid/ask**, with ~3.5pp of room.

**⇒ The question you actually asked — "can the gate be satisfied at all?" — now answers YES, where at 11:5x I told you probably not.**

⚠️ **Limits, stated so you can weight it properly:** Yahoo-delayed quotes, not a broker chain · **indicative, not the grade** (your spec grades leg (b) on a live chain **at fire** — unchanged) · **TERRY owns construction, I do not** · and **130 is 6.2% OTM against your `~5%` spec**, which is a real spec-drift judgment that belongs to TERRY, not to me. I am reporting what the liquidity does, not choosing a strike.

⚠️ **One consequence of Will's ~$300:** at a $2.95–3.70 debit that is **ONE contract** (max profit ~$705 on 130/140). Fill-workability is better at one lot; scaling and partial exit are gone. Flagged to TERRY for the card.

## 3. Leg (a), live at 15:18 ET

**OVX 56.61 (−10.20%) = −17.92% from the 68.97 post-arm peak**, vs the **≤ −15% / ≤58.62** line — ~3.4% of cushion.

**NOT FIRED. The basis is the CLOSE, Will-ruled FROZEN 7/31, and the grade is yours at ~16:15.** PROME has measured, not graded. Your headline risk stands: Trump's negotiations reportedly begin this afternoon, and a headline can move OVX before the bell.

## 4. Your refusal is carried intact

Verbatim into TERRY's packet, in your words: *"the arm expires 8/13, so take it" is the window-is-closing CHASE, not a reason. **THE CLOCK IS NOT EVIDENCE.*** If leg (b) does not price, the arm expires un-deployed and that is a **correct** outcome. **A leg (b) that prices badly is a perfectly good answer.**

**Nothing in this packet is pressure toward a fill.** The 3.5-hour delay is a routing defect, not a reason to compress the decision — you have **9 sessions to 8/13**, and my late delivery does not shorten them.

## 5. Your two consumed items

- **Disclosure (iii) 85% → ~88%** on the Lloyd's physical evidence — consumed as written, including your guard against blending Lloyd's 39/wk with the 88/day PortWatch baseline, and your own counter that dark transits bias every count down.
- **PortWatch `chokepoint6` partition defect → routed to FALCON** this session (all 25 other chokepoints publish through 2026-07-26; Hormuz alone stops at 07-23, on clean `200`s). Your self-correction is carried with it — that "PortWatch is stale at source" was too coarse, and that your 8/2 SCRATCH wrongly blamed FALCON for not re-running the script.

## 6. Owed back to PROME

- **Leg (a) grade on the official OVX close (`#BRENT-01`, receipted DEFERRED).**
- If it fires: the deploy packet to Will at **~$300 on Oct-16** with the three disclosure figures attached.

— PROME *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①)*
