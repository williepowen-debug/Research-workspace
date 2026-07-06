# BND-11 — July 7–9 Mini-Refunding Pre-Registration (BOND × LIQUID reconciled)

**Built:** 2026-07-06 (teams-session, PROME task) · **Owner:** BOND (auction mechanics + term-premium grade)
**Reconciles with:** LIQUID `workbook/DEMAND_HOLE_AUCTION_PREREG_2026-07.md` (absorption / funding-plumbing overlay).
**Rule of engagement:** BOND owns the **mechanical grade** (BTC / tail / dealer take) + the **term-premium read**. LIQUID owns the **absorption composition** (who bought) + **funding plumbing** (SOFR-IORB / SRF / repo). **This doc fuses both into ONE grade card — we grade to ONE indirect figure on ONE denominator. Do not silo, do not double-count.**

---

## Live setup (7/6, ~late-morning ET — re-pull at each auction)

| Metric | Value | Source | Note |
|---|---:|---|---|
| 30Y yield | **~5.00%** | ^TYX intraday 7/6 | **AT the 5.00 line** into the 7/9 reopen (was 4.97 close 7/1). +3bp since STATUS. |
| 10Y yield | 4.48% | ^TNX intraday 7/6 | Flat; a few bp *through* the June 4.538 stop → market rallied into the reopens. |
| 5Y yield | 4.22% | ^FVX intraday 7/6 | |
| DFII10 (10Y real) | **2.25%** | FRED 7/1 | +5bp vs STATUS (2.20, 6/30) — real-rate leg ticking toward the 2.5 re-arm, not there. |
| HY / IG / CCC OAS | 275 / 75 / 971 | FRED 7/2 | Credit inert; not the story this week. |
| TLT | $85.31 | yfinance 7/6 | −0.24% d/d; puts working, no add-gate fired. |
| FR2004 11–21Y | $74.6B (as-of 6/17) | NY Fed | **All-time record.** 6/24 print (rel. 7/2) **PENDING pull** — carry the record, re-grade dealer-absorption 3-vs-4 when it lands. |

**Why the QT fix (applied 7/6) sharpens this read:** QT ended Dec-1-2025; post-QT the Fed buys **T-BILLS** (RMPs + MBS-principal reinvestment), **NOT coupons.** → **No Fed bid at the coupon/long end.** Absorption of the 7/9 30Y is **entirely private/foreign/dealer** — there is no backstop under the reopen. The demand-hole read is *unaffected* by Fed buying.

---

## The reconciliation — why one lens isn't enough

- **BOND's mechanical marker** (BND-11 predicate) fires the "hole" on `(tail >1.5bp AND indirect <60%) OR BTC <2.3 OR dealer >20%`. **Failure mode:** if domestic directs/dealers backfill a fading indirect bid, there is **no tail and BTC stays firm** — so the mechanical grade can read **BENIGN on a masked hole.**
- **LIQUID's absorption read** catches exactly that: the demand-hole shows as **INDIRECT DOWN + DIRECTS/DEALERS ABSORBING**, not a BTC collapse. The June 6/11 30Y already printed it: indirect **66.6%→60.0%** (−6.6pp), directs **+3.6pp**, dealers **+3.0pp**, BTC firm 2.33, **no tail** — the masked signature, live.

**So the two grades can disagree, and that disagreement IS the signal.** The reconciled card below makes a mechanical-clear-but-composition-soft print resolve to **"masked hole progressing"** rather than "healthy auction."

### The ONE figure both agents grade to
> **30Y indirect bid as % of _competitive accepted_, benchmarked to June 6/11 = 60.0%**, computed from raw TreasuryDirect $ (LIQUID's method). **Same metric, same denominator, both sides.**
> Discriminator: **indirect <55% with directs/dealers backfilling above their June shares = the masked demand-hole — regardless of a firm BTC / no-tail headline.**

*(Denominator hygiene: past BOND reads occasionally used "% of total accepted" (e.g. BND-08 cited 59.84% of total); LIQUID uses competitive-accepted %. These differ by the small noncompetitive/SOMA slice. **Grade the 7/9 30Y on competitive-accepted % on both sides** to avoid a spurious 1–2pp divergence.)*

---

## RECONCILED GRADE CARD — 30Y reopen 7/9 (decisive; weight >> 10Y >> 3Y)

Benchmark = June 6/11 30Y: **indirect 60.0% / direct 25.3% / dealer 14.7% / BTC 2.33 / stop 5.020% / no tail.**

| Joint verdict | Indirect (comp-acc%) | + supporting | BND-11 (mechanical) | LIQUID M-10 (absorption) | Reconciled action |
|---|---|---|---|---|---|
| **① HOLDING** (benign) | **≥58%** (≈ June) | BTC ≥2.30 · no tail (stop ≤ WI+1bp) · dealer ≤17% · SOFR-IORB ≤0 | **TRUE** | holding | Benign. China exit stays masked; April +$206B foreign-inflow mask persists. A sub-$650B May-TIC (7/16) gets absorbed without strain. |
| **② SOFTENING — masked hole** (bearish) | **<55%** | AND directs/dealers backfill (**direct >28% OR dealer >17%**) · BTC still firm 2.28–2.33 · ≤ mild tail | **mechanically TRUE but FLAGGED** (no tail → marker doesn't fire) | **bearish / softening progressing** | **THE reconciliation: do NOT call it healthy.** Mechanical-clear + composition-deteriorating = masked hole progressing → escalate long-end read; **pre-confirms** a biting sub-$650B TIC (China exit reaching the long end). BND-11 scores TRUE, thesis still escalates. |
| **③ DEMAND-HOLE FIRING** (acute) | **<52%** | AND (**BTC <2.3 OR tail >1.5–2bp**) AND dealer **>18–20%** (forced warehouse) | **FALSE** (marker fires) | acute | Converge → escalate. TLT-put add re-arms; long-end vector →4; cross-flag LIQUID/ZHAO/PROME same-day; feeds mid-July node packet C hard. |

*Indirect **55–58%** = yellow band (between ① and ②): call by whether directs/dealers are backfilling above June shares.*

## 10Y reopen 7/8 (secondary — June was a 78% flight-to-belly outlier)
- **Holding:** indirect ≥68% AND BTC ≥2.45.
- **Softening:** indirect <62% AND directs/dealers *absorbing* the gap (not a WI concession clearing it). ⚠️ **Discount the first ~10pp of any drop off the 78% June spike as mean-reversion** — genuine softening needs domestic backfill, not price.
- Weight **30Y >> 10Y** for the demand-hole read.

## 3Y 7/7 (context only)
- Short/domestic-driven, not foreign-official-sensitive. Only informative if it tails hard (BTC <2.3 or >2bp tail) = a *broad* concession, not a foreign-bid signal.

---

## Funding-plumbing overlay (LIQUID-owned; BOND watches for the mechanical read)
Refunding weeks stress the plumbing as dealers finance new inventory ("plumbing seizes before the signal fires"). LIQUID grades these; BOND cross-reads them against the auction take:
1. **SOFR–IORB** (post-Q-end −1bp, 7/2): a move **>0 during 7/7–9** = dealer-financing strain from auction settlement (not a Q-end artifact this time).
2. **Dealer net UST coupon position** (NY Fed PD, Thu): inventory ballooning to ATH/+2σ = shrinking warehouse + basis capacity — **directly the FR2004 →4 trigger.**
3. **30Y repo specialness / SOFR dispersion** spiking = collateral scramble around the reopen.
4. **SRF** any print >$0 = dealers reaching the Fed for funding = acute.

---

## BND-11 scoring integrity (unchanged)
BND-11's pre-registered criteria (7/1) stand as written — resolve TRUE/FALSE strictly on the mechanical predicate `(tail>1.5bp AND ind<60%) OR BTC<2.3 OR dealer>20%`, weight 7/9 30Y heaviest, resolve tails from TreasuryDirect primary (flag if unpinnable, per the BND-08 lesson). **The reconciliation adds an interpretation layer, not a goalpost move:** a verdict-② "masked hole" scores BND-11 **TRUE** *and* escalates the thesis/long-end read. Base rate favors benign (6 straight benign tests: BND-05 F, BND-08 F, BND-09 F, 6/16 20Y strong, 6/23-25 cluster C+). The surprise case is verdict ② or ③ **with the 30Y sitting at 5.00.**

## Grade timing
Results ~1pm ET each day. Post a one-line reconciled verdict per tenor to STATUS; cross-flag LIQUID same-day; roll the 30Y composite into the mid-July node.
