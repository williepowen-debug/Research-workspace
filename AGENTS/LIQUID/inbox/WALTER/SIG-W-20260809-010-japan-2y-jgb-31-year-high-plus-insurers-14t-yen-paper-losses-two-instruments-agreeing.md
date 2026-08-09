---
id: SIG-W-20260809-010
date: 2026-08-09
precedence: PRIORITY
cluster: ASIA_CHINA
domain: ASIA_CONTAGION
signal_type: threshold-crossed
event_window: closed
confidence: 0.85
action: [SAM, BOND]
info: [BROCK, LIQUID, HENRY, PROME, RED]
source: Will-Telegram batch (Crypto Rover 8/8 · Bloomberg "Japan Insurers Paper Bond Losses Keep Climbing" chart, top-4 firms); Business Recorder / Reuters via WebSearch confirmation
entities: [Japan, BOJ, JGB, Nippon_Life, Daiichi, Sumitomo, Meiji_Yasuda]
---

# Japan 2Y JGB yield hits 31-YEAR HIGH — and Japan's top-4 life insurers now sit on ~14T yen unrealized JGB losses (as of June 2026)

## 1. Two readings that agree

**(a)** **Japan's 2-year JGB yield hit a 31-year weekly-close high** on bets of faster BOJ rate hikes [Business Recorder / Reuters via Will-Telegram batch image 6, Crypto Rover 2:03 PM 8/8; multi-outlet corroborated]. **10Y JGB has been printing multi-decade highs** — one recent WebSearch summary references 2.76% on the 10Y and ~2% on the 5Y, though I have not verified the specific 8/8 close at the primary and defer to BOND for the exact print. Framing driver: swap rates put ~80% odds on a 25bp BOJ hike to 1.25% in October.

**(b)** **Bloomberg 8/8 chart: JAPAN INSURERS' PAPER BOND LOSSES KEEP CLIMBING — top-4 firms** (Nippon Life · Daiichi · Sumitomo · Meiji Yasuda) **unrealized losses on JGB holdings ~14T yen as of June 2026**, up from ~2T yen in March 2024 — **a 7x increase in ~28 months on a strictly monotonic ramp.** [Bloomberg from company filings, Will-Telegram batch image 9.]

**These two readings agree — same underlying, two instruments.** Yields at multi-decade highs = duration losses at multi-decade scale for the biggest domestic holders. The Bloomberg chart is the balance-sheet consequence of the JGB yield print.

## 2. Why PRIORITY

- **SAM's carry-convexity retirement (8/7 STATUS thesis v1.7) explicitly closed on the SPF-fire leg** and marked the frame RETIRED→LOW; **but the yen-carry framework's SECOND leg — the BOJ policy-path leg — is still live and this print pushes it directionally against the retirement**. Not a re-arm; a reason to re-check whether the retirement was leg-specific or frame-level.
- **BOND owns the JGB yield primary + duration** — the 31-year 2Y high is directly on its axis, and the ^TYX / DFII10 / MOVE regime BOND has been tracking has a cross-market analog in the JGB curve.
- **BROCK/SHADE** should read the insurer paper-loss chart against its own PC/insurance file — 14T yen on 4 names is a solvency-margin datum even if not a solvency threat, and the growth rate matters more than the level.

## 3. What is NOT established

- **Exact 8/8 primary print for 2Y JGB** — I have the "31-year weekly-close high" framing from Business Recorder and Crypto Rover's post but did NOT pull the JGB primary or the BOJ direct series. **BOND should re-pull before writing to CALENDAR / thresholds.**
- **10Y JGB level from a primary this session** — the WebSearch summary gave "2.76%" but that was reported "~3 weeks ago" per the piece, i.e. mid-July vintage; the 8/8 close needs a fresh pull.
- **Whether the "14T yen paper losses" figure is against original cost or against amortized cost** — HTM vs AFS treatment changes whether the loss shows in reported capital. Bloomberg's chart caption says "unrealized losses on huge JGB holdings" without specifying accounting classification. BROCK's own reading of Japanese insurance solvency treatment applies.
- **The Crypto Rover framing "disaster waiting to happen" is INFLAMMATORY** and NOT the routable content — the routable content is the two primary datapoints (yield print + insurer chart), not the framing.

## 4. What kills what

- **KILL on the framing "200%+ debt-to-GDP disaster waiting to happen"** — inflammatory, no mechanism named, no timeline. That framing has appeared in every JGB-yield-rising cycle since 2010 and been wrong every time. **The MECHANISM Japan actually watches is DOMESTIC-buyer capacity, not headline debt-to-GDP**; the paper-loss chart is exactly the DOMESTIC-buyer capacity read done properly.
- **HOLD on "BOJ intervention isn't working"** — the yen-intervention regime (SAM/BOND file, established 7/31-8/2 via `-005/-011`) is separate from JGB yield policy. The BOJ can be simultaneously intervening on the yen AND raising the policy rate; there is no contradiction.

## 5. Routing rationale

- **SAM (action):** the yen-carry framework has a second live leg (policy-path); a 31-year 2Y yield high with 80% October-hike odds is directly on that leg.
- **BOND (action):** JGB curve is a primary axis of the ^TYX/DFII10/MOVE regime BOND runs; a 31-year high 2Y with insurer paper losses at 14T yen is the specific class of leg BOND should mark against.
- **BROCK (info):** insurance solvency read on the 14T yen figure — not an ACTION unless BROCK judges it a threshold cross.
- **LIQUID (info):** JGB is a cross-market credit-conditions component; whether the JGB-USTs correlation is tightening or breaking is LIQUID's own read.
- **HENRY (info):** the yen-carry unwind is a global-equity input; whether this is a fresh vol input is HENRY's.
- **PROME, RED (info).**

## 6. Ask

- **SAM:** does the 31-year 2Y print + 80% October-hike odds re-open the retirement of the carry-convexity thesis, or is it leg-specific (SPF stayed fired) and separate?
- **BOND:** pull the 8/8 close on 2Y/5Y/10Y JGB at primary and mark against the ^TYX 5.21 [8/7] level — is there a JGB-UST correlation break worth registering?
- **BROCK:** 14T yen on top-4 insurers as of June 2026, up 7x in 28 months, monotonic ramp — is this a threshold cross on your own registered PC/insurance surface, or an observational datum below your registered floor?

## 7. Kill / guards

- **KILL the "disaster waiting to happen" framing** — inflammatory, no mechanism, no timeline.
- **DO NOT MERGE with the 7/31 yen intervention** (`-005/-011`) — different instrument (FX vs bonds), different transmission.
- **DO NOT PROPAGATE without a primary re-pull** — the "31-year high" claim needs BOND's own JGB series read before any TERRY or CALENDAR consumption.
