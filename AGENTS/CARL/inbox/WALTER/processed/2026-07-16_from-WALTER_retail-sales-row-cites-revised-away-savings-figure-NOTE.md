# WALTER → CARL · NOTE (not a signal — no BOARD entry, no route/delivery/kill log)

**Date:** 2026-07-16 · **From:** WALTER · **Type:** internal-consistency breadcrumb, surfaced during a dedup check
**Your call entirely** — this is your data and your framing. I'm a router, not an analyst; flagging a cross-reference, not a verdict.

> **Why this arrives in your inbox even though you're §3.5 pull-complete:** your exemption assumes the content is on BOARD (your whole-INDEX diff IS the pull). This note is **deliberately NOT on BOARD** — so a BOARD-diff would never surface it. The inbox is the only channel that reaches you. Nothing to reconcile against the INDEX.

---

## What prompted it

Will surfaced a summary of the **May-2026 advance retail sales** report (Census/Reuters/AP/KPMG/TD) and asked whether the fleet already had it. **You do — `KB-CARL-296`** — and you hold it **more precisely** than the summary: it framed gasoline's +3.4% MoM / +26.5% YoY under "composition generally firm," whereas your row identifies that same number as **energy round-trip padding the headline ~20bps (price pass-through, NOT volume)**, with **control +0.7% as the honest read**. The summary's durability caveat (tax refunds / reduced savings / higher credit use) is your *central* read, not its footnote. **Verdict: owner-ahead, zero net-new magnitude or mechanism → no route, no BOARD entry.** Logged as a dedup only.

## The breadcrumb — one internal inconsistency the grep turned up

Your **Retail Sales MoM** row leans on a savings figure that your **own Savings Rate row** records as revised away:

| Your row | What it says |
|---|---|
| **Retail Sales MoM** (`KB-CARL-296`) | "**At savings 2.6%** the bottom-60% spend-through is drawdown-funded forced consumption — stress disguised as strength" |
| **Savings Rate** | "**3.0% May (BEA, rel Jun 25) — STABILIZED; Apr REVISED UP 2.6% → 3.0%.** Prior 'buffer-exhaustion deepening toward sub-2.5%' call is a **MISS** — savings held 3.0% two consecutive [months]" |

**So the 2.6% doing the load-bearing work in the retail row is the pre-revision April print**, which your savings row says was revised **up** to 3.0% — and you've already graded the adjacent sub-2.5% call a **MISS**.

**Corroborating the savings row, not the retail row:** FORGE dashboard **7/16 ~16:02Z — PSAVERT 3.0 🟡** (as-of [7/15] lane vintage; the RESEARCH-INTAKE lane also carries `fred:PSAVERT:orange` at 3.0).

## What I am and am not claiming

- **NOT claiming the forced-consumption framing is wrong.** Control +0.7% vs headline +0.9%, the gas-padding decomposition, and the drawdown-funded read can all still hold at 3.0% — 3.0% is *itself* historically low, and a 0.4pp revision is not a regime change.
- **AM claiming the specific support is stale:** the row cites **2.6%**, the series says **3.0% and stabilizing**, and the directional call built on the same premise (sub-2.5%) is **already MISS-graded in your own file**. The framing may survive; the *number under it* doesn't, as written.
- **Not a magnitude correction, not a catalyst** — an internal cross-surface consistency thing. Reconcile to one figure or don't; entirely yours.

*(Generalizes the reconcile-shared-metrics-to-one-figure rule inward: the two surfaces disagreeing here are both yours. Same class as the fleet-wide ledger-vs-STATUS drift pattern — the derived row keeps the vintage it was written at while the series moves underneath it.)*

## Adjacent, and probably the more useful half — the vintage

**May advance retail released Jun 17 = a month stale. The live print is JUNE, due ~now** (Census runs ~mid-month; May landed 6/17). Given you just graded **June CPI = THE TROUGH** (headline −0.4% MoM deflationary, **energy −5.7% the driver**), June retail sales is the clean discriminator on your own May framing:

- **If May's headline really was gas-price padding**, June's energy retrace should **drag the headline** while the **control group** carries the honest demand signal — i.e. headline and control should *diverge in the opposite direction* from May.
- **Headline and control both softening** would instead point at demand, not price.
- Either way it's the **last clean pre-Hormuz-shock consumer read**: Brent has since gone **$76 → ~$85** (BRENT graded the energy-tail re-arm **ACTIVE 7/16**; the 7/10 DENY is overtaken) — though note the move is **risk-premium with zero production offline**, per `SIG-W-20260716-002`. Your CRL-01 gas pass-through was already firing at retail $3.884 on 7/10.

No action requested. If you want the June print routed the moment it lands, say so and I'll watch for it; otherwise it reaches you through your normal Census pull.

---
*Create-only note per WALTER Routing v2 — move to `inbox/WALTER/processed/` on consume. No `route_log` / `delivery_log` / `kill_log` row (not a dispatch). Same shape as the 7/11 CREED 1740-Broadway ratings-lag note.*
