# ARM PACKET → PROME → Will [Approve] — TRY-FIRE-004 (TLT duration-short / puts)
**From:** TERRY · **Date:** 2026-07-16 (updated ~10:10 ET w/ Will's live broker chain; markets open) · **Gate:** GATE-TERRY-ARM2 = FIRED (arm-#2 5-of-5 completed Mon 7/13)
**Consequence executed:** arm-#2 fired → TERRY arms TRY-FIRE-004 → **this packet → Will [Approve].** Will has APPROVED the ladder structure; this version finalizes sizing on live marks + offers the grind-spread refinement.
**Terry verdict:** **CLEAN structure. Recommendation: 81/76 put debit spread (§5C)** — better-matched to the confirmed term-premium GRIND than the outright crash-ladder. Defined risk ≤$500 every variant.
**Confidence in trade structure:** Medium (structure clean + thesis confirmed by BOND/HENRY; magnitude/timing is the open risk — hence spread over outright).

---

## 0. Pre-registration note (why this packet exists at all)
Arm-#2 (VX-BND-05 10Y-sustain) is a **pre-registered gate**. It fired; the registered consequence is that I arm the card and hand Will a packet. **The arm executes as registered** — the new context below (cool June CPI, MOVE round-trip, TLT at range lows) goes IN the packet as decision context, **not** as a reason to skip the arm. Whether Will *fills* is a separate decision this packet informs.

## 1. Independent arm-#2 verification (FRED DGS10 direct, pulled 2026-07-16 ~09:31 ET)
Semantics applied per BOND co-ratification (2dp DGS10, ≥ inclusive, holidays neither count nor reset, official governs over ^TNX).

| Date | DGS10 (official) | ≥4.50? | Consecutive count |
|---|---:|---|---|
| 7/6 | 4.48 | NO | 0 (reset) |
| 7/7 | 4.55 | YES | 1 |
| 7/8 | 4.56 | YES | 2 |
| 7/9 | 4.54 | YES | 3 |
| 7/10 | 4.56 | YES | 4 |
| **7/13** | **4.62** | YES | **5 ✅ COMPLETE** |
| 7/14 | 4.58 | YES | 6 (streak intact) |

**Verdict: 5-of-5 CONFIRMED, HIGH confidence. Matches PROME/BOND exactly.** 7/3 holiday ("." in FRED) correctly neither counted nor reset. Streak still live through 7/14 (arm-#2 has not disarmed — no close <4.50). Consumer note: the 7/8 official is **4.56** (the 4.57 in some older artifacts was a ^TNX read — count-neutral).

## 2. Live tape (pulled 2026-07-16 ~09:32–09:35 ET, FORGE fetch.py)
| Instrument | Level | Δ vs prev | Read |
|---|---:|---|---|
| TLT | **$83.80** | −0.52% | RED day; at/near **low of 6-day range** (84.49 [7/9] → 83.80) |
| 10Y (^TNX) | 4.59 | +0.9% | above the 4.50 sustain line, pushing higher — thesis moving in real time |
| 30Y (^TYX) | 5.12 | +0.65% | term-premium channel live |
| MOVE (^MOVE) | 68.48 | — | rates-vol round-tripped: spiked **77.77 [Mon 7/13, +11.82%, investing.com daily]** then faded through CPI (see §6) |
| VIX | 16.17 | +3.19% | still cycle-calm |

**TLT 6-session tape:** 84.36 (7/8) · 84.49 (7/9) · 84.47 (7/10) · 83.97 (7/13) · 84.08 (7/14) · 84.24 (7/15) · **83.80 (7/16)**. Grinding lower; today gapped down and sits at range lows.

## 3. LIVE BROKER CHAIN — TLT Sep-18 puts (Will's screenshots ~10:04–10:05 ET; TLT spot $83.89, −0.4%)
*(The FORGE data tool could not serve live TLT option NBBO across three pulls (09:32/09:45/09:52 all 0.00) — these are Will's broker marks. Final fill marks are read-at-order-time; NBBO moves.)*

| Strike | Bid × sz | Ask × sz | Mark | IV | Δ | Θ/day | Vega | OI |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 82 P | 0.65 ×1394 | 0.67 ×699 | 0.66 | 11.53% | −0.265 | −0.0081 | 0.115 | 43,275 |
| 81 P | 0.43 ×395 | 0.44 ×227 | 0.435 | 11.70% | −0.191 | −0.0071 | 0.096 | 54,970 |
| 80 P | 0.28 ×95 | 0.29 ×288 | 0.285 | 11.97% | −0.134 | −0.0059 | 0.076 | 64,886 |
| 77 P | 0.11 ×222 | 0.12 ×1030 | 0.115 | 14.07% | −0.056 | −0.0038 | 0.040 | 54,506 |
| 76 P | 0.08 ×777 | 0.09 ×382 | 0.085 | 14.77% | −0.042 | −0.0032 | 0.031 | 2,661 |
| 75 P | 0.06 ×700 | 0.07 ×142 | 0.065 | 15.55% | −0.032 | −0.0028 | 0.025 | 30,195 |

**Liquidity: fine for $500-scale on all rungs** (77 P ask 0.12×1030, 82 P bid 0.65×1394). **Put skew is steep and matters:** OTM-low IV (75 P 15.55%) >> near-money (82 P 11.53%) — so a *spread that sells the lower strike sells the richer vol* (structural tailwind, quantified in §5B).

## 4. Structure — Sep-18 2026, $500 cap. Two ways to express it (Will approved the ladder; §5C = my rec)
Yield mapping below uses TLT effective duration ≈ **15.5y** (approx; TLT tracks 20+yr, so the yield Δ is the *long end* — ~30Y from 5.12 — a curve-parallel read for the 10Y is similar magnitude).

### 5A. APPROVED LADDER — outright deep-OTM puts, sized at live ASK ($500 cap)
| Rung | Ask | Contracts | Cost | Max loss | BE (TLT@exp) | 5× at TLT | 10× at TLT | netΔ | Θ/day |
|---|---:|---:|---:|---:|---:|---|---|---:|---:|
| **77 P** | $0.12 | 41 | $492 | $492 | 76.88 | 76.40 (+58bp) | 75.80 (+62bp) | ≈228 sh | −$15.6 |
| 76 P | $0.09 | 55 | $495 | $495 | 75.91 | 75.55 (+64bp) | 75.10 (+68bp) | ≈229 sh | −$17.6 |
| 75 P | $0.07 | 71 | $497 | $497 | 74.93 | 74.65 (+71bp) | 74.30 (+74bp) | ≈228 sh | −$19.9 |

**What the ladder IS: a duration-CRASH bet.** All rungs need TLT *below the strike* (77/76/75, i.e. −8 to −11%, long-end +58–74bp) just to have value at expiry. It pays uncapped in a genuine shock — but it is **worth $0 if TLT merely grinds to ~78** (see §5B stress). High theta ($16–20/day).

### 5B. GRIND-SPREAD variants — put debit spreads (buy hi @ask / sell lo @bid), $500 cap
| Spread | Net debit | Ct | Cost | Max loss | Max payoff (ratio) | BE (TLT) | Max-profit at TLT≤ | **Value if TLT→78** | netΔ | Θ/day | Vol edge |
|---|---:|---:|---:|---:|---|---:|---|---:|---:|---:|---|
| 82/77 | $0.56 | 8 | $448 | $448 | $3,552 (7.9×) | 81.44 (+19bp) | 77 (+53bp) | **$3,200 (7.1×)** | ≈167 | −$3.4 | sell 14.07% / buy 11.53% |
| **81/76** | $0.36 | 13 | $468 | $468 | $6,032 (12.9×) | 80.64 (+25bp) | 76 (+61bp) | **$3,900 (8.3×)** | ≈194 | −$5.1 | sell 14.77% / buy 11.70% |
| 80/75 | $0.23 | 21 | $483 | $483 | $10,017 (20.7×) | 79.77 (+32bp) | 75 (+68bp) | **$4,200 (8.7×)** | ≈214 | −$6.5 | sell 15.55% / buy 11.97% |

**The decisive contrast (TLT grinds to 78 by Sep — the actual BOND/HENRY thesis, ~long-end +45bp):** every spread pays **7–9× ($3,200–$4,200)**, while **all three outright ladder rungs expire worthless ($0)** — because a grind to 78 never reaches the 77/76/75 strikes. Spreads also: break even far closer to spot (80.6–81.4 vs 74.9–76.9), **sell the rich tail-skew vol** against a cheaper long leg, and bleed **~1/3 the theta** ($3–7/day vs $16–20). The short leg's only cost is capping the payoff in a true crash — which is *not* this thesis (falsifier is a bond rally, not a deeper selloff).

### 5C. TERRY RECOMMENDATION → the **81/76 put debit spread**
Given BOND + HENRY both confirm a **term-premium GRIND** (real-yield-led, higher-for-longer) rather than a crash, and the registered falsifier is a *rally* (Hormuz de-escalation → DFII10 eases), the outright ladder is mispriced against the thesis — it needs a crash to pay and dies on a grind. The **81/76 spread** is the best match: breakeven $80.64 (−3.9%, a *realistic* grind, ~+25bp long-end) so it profits without a shock; 12.9× max ($6,032 if TLT ≤76); 8.3× ($3,900) at the plausible TLT-78 grind; sells the 76 P's 14.77% vs the 81 P's 11.70% (skew tailwind); theta only ~$5/day. **82/77** = higher win-probability / lower ratio (7.9×) if Will wants the closest breakeven; **80/75** = max convexity (20.7×) if he wants the biggest tail. Keep the **outright 77 P (41 ct/$492)** ONLY if the view is a genuine duration crash with uncapped upside — the approved fallback. $500 cap ⇒ pick one (or split); all are defined-risk.

## 6. Decision context — what changed since the card was scoped (goes IN, doesn't veto the arm)
- **June CPI (7/14) printed COOL** — headline −0.42% MoM (outright deflationary month), core −0.02% [FRED CPIAUCSL/CPILFESL] — **yet the 10Y HELD the 4.50 line** (4.62 pre-print → 4.58 post). This is the bull case for the *re-scoped* thesis: yields sustaining despite a cool print = **term premium, not inflation expectations**. The demand-hole leg was already refuted (7/9 auction); this is the term-premium/inflation-channel card.
- **BOND rates decomposition (co-grade memo 7/16) — WHY the line held is quantified: it's an 86%-REAL-yield move.** DGS10 = DFII10 (real) + T10YIE (breakeven); the +14bp 7/6→7/13 climb above 4.50 was **+12bp DFII10 (real, 86%)** vs **+2bp breakeven (14%)**, with 5Y5Y forward inflation dead-anchored at 2.21. A cool backward CPI *can't* break a line that inflation expectations weren't holding up. DFII10 at **2.36 [7/13]** = series high, ~14–17bp under BOND's 2.50 real-stress re-arm. Front end co-moved (**2Y +13bp through the deflationary print**) = hawkish-hold pricing, not cuts-sooner. **Directional support for the trade.**
- **The oil shock loads the JULY print, not June** — Hormuz closed 7/11–12, Brent ~$71→$86 (≈+21%) ≈ **+0.4–0.6pp to July headline MoM from gasoline alone** (BOND), releasing ~mid-Aug (after FOMC 7/28–29, which nonetheless sees Brent $86 + Hormuz closed feeding the inflation-risk premium). This is the inflation leg the card was re-scoped to. **BOND verdict: 4.50-sustain through FOMC is WELL-SUPPORTED; main falsifier = fast Hormuz de-escalation → Brent retrace → DFII10 eases back to the line.** That falsifier is the trade's key thesis-invalidation to watch.
- **Rates-vol round-tripped, it didn't just fade:** authoritative daily (investing.com, web-verified 7/16) shows MOVE **69.55 [7/10] → 77.77 [Mon 7/13, +11.82%, above the 72.41 cycle peak] → 75.03 [7/14 CPI, −3.52%] → 68.48 [7/15, −8.73%]**. The spike was the **7/13 duration move** (same day 10Y completed 5-of-5 at 4.62), already fading *through* the cool CPI. Vol has deflated — a tailwind for *buying* puts now (IV coming off), but a headwind for the acute-catalyst framing (spike + CPI both passed). *(Corrects an earlier 1h-bar read that mislabeled the spike to 7/14; that series lagged one day.)*
- **Next catalysts:** (a) **May TIC today 4:00 PM ET** = arm-#3 (grading template pre-staged, see companion file); (b) the **JULY CPI (mid-Aug)** now carries the Hormuz/Brent oil shock (Brent ~$86 [7/16]) — the inflation leg the card was re-scoped to. Sep-18 expiry covers both.

## 7. Rule #6 (timing) + counter-case — Will decides fill timing
1. **Rule #6 (puts on green days): TLT is RED (−0.4% @10:04, was −0.5% at open), near range lows** — so an *outright* put fill today is a chase; the disciplined outright entry waits for a green TLT bounce toward **84.2–84.5**. **But the rule is much weaker for the recommended SPREAD:** the short leg cuts net delta ~15% and net vega sharply, so the 81/76 is far less exposed to entry-day direction than an outright, and you're *selling* the rich vol — filling it on a red day carries little chase penalty. **Rec:** if outright → wait for green / scale; if spread → a limit at/through the natural is fine today, no market-order chase. The thesis is a multi-week grind through FOMC 7/28–29 — **no urgency to chase the open either way.**
2. **Primary acute catalyst already passed** (CPI 7/14, cool; MOVE spike 7/13 round-tripped). Next dated drivers: **May TIC today 4pm** (arm-#3), then **July CPI mid-Aug** (carries the oil shock). Sep-18 expiry spans both — theta is the cost of waiting, which is *why the low-theta spread beats the high-theta outright* for a slow grind.
3. **Thesis-invalidation (BOND):** fast Hormuz de-escalation → Brent retraces → DFII10 eases back to the 4.50 line → exit. This hurts both structures; it's the trade's stop, not a structure choice.
4. **Position truth is OFF-repo (rule #4).** `[POSITION_STATE_UNKNOWN]` — Will must confirm no existing TLT/duration exposure this doubles (the VIO-116 rates-vol look folds into THIS lane — see companion memo; do not double-count duration-short risk).

## 8. Execution checklist
- [x] Arm-#2 fired — **YES (verified §1)**
- [x] Live option marks — **YES, Will's broker chain 10:04 ET (§3). Final fill marks read-at-order-time.**
- [~] Green/red check (rule #6) — **RED day (TLT −0.4%); muted for the spread, flagged for outright (§7.1)**
- [x] Liquidity OK — **YES on all rungs at $500 scale (§3)**
- [x] Max loss ≤ $500 — **YES, defined-risk every variant (§5)**
- [ ] Position truth — **Will confirms no conflicting TLT/duration book (VIO-116 same lane)**

## Decision
**Terry verdict: CLEAN structure — recommend the 81/76 put debit spread (§5C)** over the approved outright ladder: same defined ≤$500 risk, but it *pays on the confirmed grind* (the outright ladder expires worthless if TLT only reaches ~78), breaks even far closer to spot, sells the rich tail-skew vol, and bleeds ~⅓ the theta. Will approved the ladder structure; this is an APPROVE-MODIFIED refinement, his call.

- [ ] **APPROVE-MODIFIED → 81/76 spread** (13 ct, ~$468, max loss $468, max payoff $6,032) — *Terry rec*
- [ ] APPROVE-MODIFIED → 82/77 (higher win-prob) or 80/75 (max convexity) spread
- [ ] APPROVE → outright 77 P ladder (41 ct, $492) — approved fallback, crash-only
- [ ] REJECT / HOLD (e.g. wait for green-day fill)

Fill timing is Will's (rule #6, §7.1). **APPROVAL REQUIRED — Will must approve/reject before execution. TERRY never executes.**
