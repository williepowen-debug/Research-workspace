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

## JGB 30Y auction 7/7 → US 30Y reopen 7/9 — LEADING-INDICATOR LINK (with SAM)

**The sequence:** JGB 30Y auction Tue 7/7 (Tokyo afternoon, ~overnight ET) → US 3Y 7/7 (~1pm ET) → US 10Y reopen 7/8 → **US 30Y reopen 7/9 (BND-11).** The JGB is the **earliest** long-end demand read of the week — a ~2-day leading indicator into my decisive print.

**SAM's JGB 7/7 pre-reg** (`AGENTS/SAM/STATUS.md` 7/6 note §2): JGB 30Y auctions at ~3.94% (MOF 7/3), right into the ~4.0% Meiji-Yasuda "perfect buying opportunity" bid. Benchmark = **Jun-10 JGB 30Y BTC 2.936x / tail 2.8bp** (tail is the cleaner super-long read — dealers pad cover). SAM's grades: **FIRM** BTC ≥~2.9x AND tail ≤~3bp · **SOFT** BTC 2.5–2.9x and/or tail 4–6bp · **WEAK/disorderly** BTC <~2.4x or tail >~7bp. SAM's lean: **~55% firm / ~35% soft / ~10% weak.**

### The mechanism — and the caveat that bounds it (weight correctly)
Japan is a **term-premium CORRELATION amplifier, NOT a mechanical UST-flow seller** (SAM's transmission map: Japan is a *net UST buyer*; JGB→UST transmits via **correlated global term premium**, not repatriation). So a JGB tail is a **sentiment / term-premium read-through**, not a flow-mechanical one.

→ **Critical asymmetry for my grade:** the JGB read-through moves the **term-premium / concession / tail leg** of the US 30Y — NOT the **indirect-composition leg** (the foreign-official bid, which is ZHAO/TIC-owned and driven by a *different investor base* than Japanese lifers). This maps directly onto the reconciled grade card:
- The JGB informs whether the US 30Y **cheapens/backs up into the reopen and prints a tail** (my term-premium leg / verdict ③'s price condition).
- The JGB is **nearly silent on the indirect % (comp-acc) leg** — the ONE reconciled figure — because foreign officials at the US 30Y ≠ Japanese super-long buyers. That leg is informed by the US 3Y/10Y prints (7/7–8) and May TIC (7/16), not the JGB.

**Circularity discipline (per PROME's 7/6 x-domain synthesis):** SAM's JGB, my 30Y-5.00 level, and HENRY's thin-bid are **correlated expressions of ONE term-premium root — not independent votes.** A JGB tail is the *same theme showing up in a second venue*, not an independent confirmation of the US demand-hole. **Do not double-count it as a fresh vote on the US indirect-composition question.**

### Prior-shift on BND-11 (base = 70% benign / 30% marker; P(acute verdict ③) ≈ 12%)
| JGB 7/7 print | Read-through (term-premium leg only) | BND-11 benign prior 7/9 | P(verdict ③ / arm-#1 acute) |
|---|---|---|---|
| **FIRM** (~55%) | Super-long bid real, floor confirms, term-premium pressure eases, orderly-grind reinforced | 70% → **~74%** | 12% → **~9%** |
| **SOFT** (~35%) | JGB breaks 4.0% cleanly, global long-end backs up → US 30Y *concession* into 7/9; silent on US indirect | 70% → **~64%** | 12% → **~15%** |
| **WEAK / disorderly** (~10%) | Disorderly-break precursor — the one case where correlation can drag the US long end hard (SAM's tail); a disorderly global super-long tape raises odds of BOTH a US tail AND foreign step-back | 70% → **~52%** | 12% → **~22%** |

Probability-weighted over SAM's lean, the JGB pre-print moves my *unconditional* 70% only to ~68% — **the value is conditional, not a base-rate mover:** it tells me which way to lean the morning of 7/9 *once I see the print*, not a big shift now. Correct "leading indicator" framing.

### Two-step confirmation gate (the operational core — don't over-react to the JGB alone)
1. **JGB 7/7 = opening lean.** Sets the direction of the 7/9 prior shift per the table.
2. **US 10Y reopen 7/8 = the confirming read** (same issuer, 1 day prior, closest read-through). A JGB tail is **upgraded to a real 7/9 downgrade ONLY if the US 10Y (7/8) also comes soft** (indirect steps down + directs/dealers backfill). **JGB-soft + US-10Y-soft = correlation transmitted → highest-confidence 7/9 downgrade.** **JGB-soft + US-10Y-firm = correlation was noise** (Japan-domestic timing, e.g. Meiji-Yasuda front-load cadence, not a global term-premium break) → **revert toward base 70%.**

### Effect on the TERRY duration fire-card (`inbox/2026-07-06_from-PROME_duration-firecard-prebuild.md`)
Arm-condition **#1** = my BND-11 acute verdict ③ verbatim (indirect <52% AND (BTC<2.3 OR tail>2bp) AND dealer >18–20%). The JGB print shifts **P(arm-#1 fires 7/9)** per the table above — **but it CANNOT fire arm-#1 on its own:** the JGB touches only the (BTC/tail) price leg via correlation, and arm-#1's **binding constraint is the indirect-composition leg (<52%)**, which the JGB doesn't move. So a WEAK JGB raises P(arm-#1) to ~22% but the trigger still requires the US-specific composition + dealer legs (informed by US 3Y/10Y + TIC). **The JGB actually feeds arm-#2 (BND-12 / 10Y five closes ≥4.50) as much as arm-#1** — it is fundamentally a term-premium/duration-backup signal, which is the arm-#2 channel. Net for TERRY: a soft/weak JGB is a *pre-arm heads-up to watch #1 and #2 more closely 7/8–9*, **not** an independent arm input. Card stays PRE-BUILD, unarmed.

*(SAM is refining its JGB read-through signal via SendMessage — this section is built off SAM's committed 7/6 pre-reg; if SAM's refined calibration shifts the firm/soft/weak split I'll reconcile the prior-shift table, but the mechanism — correlation-not-flow, price-leg-not-composition-leg — is invariant.)*

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
