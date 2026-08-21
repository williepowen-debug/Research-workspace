# BOND Monitor — CDX/Cash Credit Basis

**Owner:** BOND
**Last Updated:** 2026-08-21 by BOND — **proxy RE-RUN** (`cdx_proxy.py`, data through **8/21**): **HYG/IEF 0.8574, z20 +1.17, 98th pctile of 3mo** = credit-excess RICH, **no divergence** — essentially unchanged through the entire rates round-trip (8/18 read 0.8567 / +1.40 / 98th). **LQD/IEF: negative every one of the last 10 sessions, but the MAGNITUDE has collapsed — −1.96 [8/17] → −1.54 [8/18] → −0.25 [8/19] → −0.63 [8/20] → −0.38 [8/21], against the −1.43 this file has been citing.** The sign persists; the signal has faded — **stop quoting −1.43 as the live magnitude.** ✅ **AND THE OPEN CHECKBOX ON THIS FILE IS CLOSED: VIOLET ANSWERED 8/20.** They can produce a POINT but not the DIRECTION the trigger clause needs — **so the "OR VIOLET skew-vs-flat-cash" leg is NOT FIREABLE AS WRITTEN**, and that is the answer, not a deferral. *(Prior: 2026-08-18 re-run, data through 8/14.)* ⚠️ **A CONFOUND IS NAMED FOR THE FIRST TIME — see Current Read.** *(Prior: 2026-07-28, data through 7/27.)*
**Purpose:** Detect when faster synthetic/hedging credit demand leads cash spread repricing.

## Current Read — 2026-08-18

**Proxy run 8/18, data through 8/14:** HYG/IEF **0.8567** · z20 **+1.40** · **98th percentile of the 3-month range** (0.8377–0.8568) · 20d change **+0.73%**. LQD/IEF **1.1406**, z20 **−1.43**.

**Verdict: credit-excess RICH, NO divergence. The basis is not signalling stress.** The registered divergence trigger (proxy z20 **< −1.5** *while cash HY stays TIGHT*) is nowhere — z20 is **positive** and near the top of its range.

> ## ⚠️ CONFOUND NAMED 2026-08-18 — do not cite this ratio alone while the long end is repricing
>
> **HYG/IEF rises MECHANICALLY in a rates-led selloff, because the IEF denominator falls on duration.** Over the window this run covers, the 30Y rose to a **19-year high** and IEF fell with it. **So "98th percentile / credit-excess rich" is partly an artifact of the very move this desk is tracking, not an independent statement about credit.**
>
> **The read survives only because an independent instrument agrees:** cash **HY OAS 267 [FRED 8/14]** is at its tightest since the 263 cycle trough. **Two instruments, one of which is confounded ⇒ weight the unconfounded one.** Had cash HY been *widening* while this ratio sat at the 98th percentile, the correct reading would have been "the ratio is lying," not "divergence."
>
> ⚠️ **This monitor's whole purpose is to detect a sign-divergence between fast and slow credit layers. A denominator that moves with rates injects a rates signal into a credit instrument** — which is exactly the failure mode the 6/24–26 sign-check lesson was written for. **Fix when there is time: run the ratio against a duration-matched credit-free denominator, or report HYG total-return excess directly rather than versus IEF.** Logged, not fixed today.

*LQD/IEF z20 has now been negative every session for ~5 weeks (−1.83 on 7/28 → −1.43). **IG credit-excess remains the more persistent signal, and it is the one this monitor keeps not acting on.*** IG OAS itself is **80bp and flat through the entire episode in both directions**, so the persistent negative z20 is not corroborated by cash IG — another reason to suspect the denominator.


## Working Model

- Synthetic/fast layer widening ahead of cash = hedging demand / fast-money stress before bonds trade.
- Cash OAS widening without the fast layer = slower fundamental repricing.
- Divergence sustained for 2+ weeks matters more than one-day noise.

## Data Reality (read before citing)

True **CDX.HY / CDX.IG index levels are owned by S&P Global / Markit and are NOT free** [established ~2026-06-05, **re-test: 2026-12-01** — a paywall is a commercial decision and decays like any other claim; re-test by attempting a free primary, not by re-reading this line]. For weeks this vector sat as "🟡 data gap" — effectively dark. As of 6/5 it is monitored via a **free proxy**, with explicit limits:

- **Proxy (BOND, free):** `monitors/cdx_proxy.py` — the **HYG/IEF ratio** (HY credit ETF stripped of duration via the 7-10Y UST ETF) isolates the credit component of HYG. LQD/IEF gives the IG cross-check. Run it any session; cross-check vs cash HY OAS (FRED `BAMLH0A0HYM2`).
- **What the proxy CAN see:** faster-cash (liquid ETF/hedging layer) vs slower-cash (computed OAS) lead/lag.
- **What it CANNOT see:** HYG is *cash*, not *synthetic*. The genuinely synthetic, fast-money signal is **HYG option put-skew / implied vol** — that lives in **VIOLET's** domain (options/vol). For the true synthetic read, request HYG skew from VIOLET. True CDX needs the **S&P Global MCP connector (auth required)** or a paid Markit feed.

## Current Read (7/28) — 🟢 **NO divergence, and the proxy INDEPENDENTLY CONFIRMS the credit widening is not credit-led**

**The test that mattered:** cash HY OAS widened **+11bp in two sessions** (268 [7/22] → 279 [7/24]). If that widening were genuine credit stress, HYG should underperform IEF and the ratio should break down. **It didn't.**

**HYG/IEF 0.8498 [7/27], z20 −0.08, 79th percentile of the 3-month range** — i.e. still near the *top* of the range, credit-excess **rich**. The ratio did soften modestly (0.8541 [7/22] → 0.8498, −0.50%, z20 +1.22 → −0.08), which is sympathy-level movement well inside the band — **nowhere near the −1.5 trigger.**

**⇒ Cash OAS widened while the faster ETF layer stayed rich.** Per the working model above that is the *"cash widening without the fast layer"* case = slower/broader repricing, **not** hedging-demand or fast-money stress front-running the bonds. **This is an independent, orthogonal confirmation of the tranche-data read** (the widening is absolute-parallel and proportionally largest at the *top* of the stack): three different instruments — index OAS, tranche OAS, and a duration-stripped ETF ratio — all say **repricing, not credit event.** Vector holds **1**.

**⚠️ One thing genuinely worth watching, and it is NOT the HY leg: `LQD/IEF` z20 has been persistently negative for two full weeks** (−1.16 to −2.09, every session 7/14→7/27, hitting −1.83 on 7/24). IG credit-excess has been soft *longer and more consistently* than HY — the opposite of where attention has been. Not a trigger (this vector's threshold is specified on the HY leg), but it is the more durable of the two signals and deserves a look if IG OAS keeps grinding.

**Standing caution retained:** the 6/24–26 lesson is that a proxy breach *while cash is also widening* is a **co-move, not a divergence** — sign-check both legs before ever calling one.

---

### Prior read (7/1, superseded)

**🟢 No true divergence — the 6/24–26 z-breach FAILED the sign-check.** The proxy breached the −1.5 trigger for three sessions (z20 −3.28 / −2.58 / −2.82, 6/24–26) — but cash HY OAS was widening **concurrently** (276→283), so the fast layer did not LEAD cash; both were co-moving beta to an equity/tech risk-off (Apple price-hike → AI-demand fears, VIX 18.9). That is a **co-move, not a divergence** — the trigger's spirit ("z < −1.5 *while HY tight*") did not fire. Fully normalized by 7/1 (z −0.17, ratio 0.8464, 58th pctile of 3mo). LQD/IEF dipped in sympathy (−2.87 on 6/26) and recovered (−1.38). Vector holds 1. Lesson logged: **sign-check the two legs before calling a divergence** — the trigger requires cash STILL TIGHT while the proxy breaks.

## Rolling Table

| Date | HY OAS | HYG/IEF (z20) | LQD/IEF | Read | Source |
|---|---:|---:|---:|---|---|
| 2026-03-21/26 | ~319bps | n/a (not wired) | n/a | 🟠/🔴 then — CDX widening per notes | Sentiment Trader/RIA via LIQUID/BOND seed |
| 2026-05-08/11 | 281bps | n/a (data gap) | n/a | 🟡 gap — could not adjudicate | FRED + missing CDX source |
| 2026-05-20 | 286bps | 0.8504 (+1.86) | — | proxy z-spike = IEF/duration weakness, NOT credit | yfinance + FRED |
| 2026-06-05 | 274bps | 0.8484 (+0.36) | 1.1554 | 🟢 no divergence — credit-excess rich | yfinance + FRED |
| 2026-06-18 | 263bps | 0.8479 (−0.40) | 1.1559 | 🟢 no sustained divergence (brief 6/16 z −1.54 normalized) | yfinance + FRED |
| 2026-06-24→26 | 276→283bps | 0.8429→0.8401 (**−3.28→−2.82**) | 1.1550→1.1523 (−2.87) | 🟡 z-breach but **co-move w/ cash widening = NOT divergence** (equity-beta episode) | yfinance + FRED (KB-BND-063) |
| 2026-07-01 | 275bps (6/30) | 0.8464 (−0.17) | 1.1535 (−1.38) | 🟢 normalized; vector holds 1 | cdx_proxy.py run 7/1 |
| 2026-07-22 | **268bps** | 0.8541 (**+1.22**) | 1.1458 (−1.16) | 🟢 proxy at the top of range; cash at its tightest of the month | cdx_proxy.py run 7/28 |
| 2026-07-24 | **279bps** (+11bp/2sess) | 0.8517 (+0.51) | 1.1419 (**−1.83**) | 🟢 **cash widened, proxy stayed RICH = no fast-layer confirmation ⇒ repricing, not credit stress** | cdx_proxy.py run 7/28 |
| **2026-07-27** | *(no print — FRED OAS lags)* | **0.8498 (−0.08)** | **1.1418 (−1.61)** | 🟢 **no divergence; HYG/IEF 79th pctile of 3mo.** ⚠️ *LQD/IEF z20 negative every session for 2 weeks — IG credit-excess softer and more persistent than HY* | cdx_proxy.py run 7/28 |

## Triggers

| Trigger | Action |
|---|---|
| HYG/IEF breaks to bottom of range (z20 < -1.5) while HY OAS stays tight for 2+ weeks | 🟠 signal HENRY/LIQUID — fast layer leading cash |
| HYG/IEF and HY OAS both deteriorate >75bps-equiv from trough | 🔴 credit-equity lead active |
| HYG/IEF normalizes while cash stays tight | downgrade prior divergence as resolved (current state) |
| VIOLET reports HYG put-skew steepening while cash OAS flat | 🟠 true synthetic-leading-cash — escalate (BOND proxy blind to this) |

## Automation Status

- ✅ Free proxy wired (`cdx_proxy.py`) — repeatable, no auth needed.
- 🟡 Synthetic/options leg: HYG put-skew from VIOLET (BOND-blind). ⚠️ **This checkbox read ⬜ for 76 days against a request that was NEVER DELIVERED** — the 2026-06-05 packet was written and committed to `outbox/` and never reached VIOLET's inbox. **Writing a packet is not sending it.** **RE-SENT 2026-08-20, restated as of today rather than re-delivering the stale June text; original moved to `outbox/delivered/` as the record. `re-test: 2026-09-20` — if no reply by then, RETIRE the "OR VIOLET skew-vs-flat-cash" clause from this vector's upgrade trigger rather than leaving it unfireable a second time.**
- ⬜ True CDX: S&P Global MCP connector (auth) — evaluate when connectors are live headless.
