# BOND — STATUS archive (sections retired from `STATUS.md` on 2026-08-18)

**Why:** `STATUS.md` crossed its 250-line cap during the 8/18 staleness sweep. Per `CLAUDE.md` OUTPUT RULES (*compress; archive old research to `domain/sources/`*), the resolved-historical sections below were moved here **verbatim, unedited**. Nothing in this file is current — it is the record of how resolved calls were reasoned.

⚠️ **Do not cite any figure in this file as live.** Every value here was current on its own dated line and is superseded by `STATUS.md`.

---

## Part A — resolved auction sections (June/July 2026)

## Auction Read — 6/23–25 cluster (RESOLVED, grade C+) — *historical baseline; the live series is `monitors/AUCTION_HEALTH.md`*

> ⚠️ *Retained as the June benchmark the 7/27 cluster is graded against. **The tail figures in this table are the old, unscoreable kind** — "8th consecutive tailing 5Y" came from a secondary, and TreasuryDirect publishes no when-issued yield. Under the rule adopted 7/28, no gate may key on them. Read the composition columns, not the tail notes.*

| Date | Tenor | Size | BTC | High Yield | Indirect | Direct | PD | Read |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 6/23 | 2Y (91282CQY0) | $69B | 2.64 | 4.189% | **55.45%** | 34.31% | 10.24% | 0.3bp **stop-through**; HY highest since Jan-25; dealer take lowest since Feb. |
| 6/24 | 5Y (91282CQX2) | $70B | 2.35 | 4.200% | 61.60% | 25.51% | 12.89% | **0.7bp tail — 8th consecutive tailing 5Y**; indirect −13.3pp m/m. |
| 6/25 | 7Y (91282CQW4) | $44B | 2.50 | 4.260% | **57.55%** | 29.70% | 12.75% | Indirect −20.8pp m/m; tail **unpinnable** (treat as unknown). |

**Read:** no hard stress marker (nothing near BTC <2.3 / tail >1.5bp / dealer spike) — **6th straight benign test**. The story is **composition**: foreign/custodial (indirect) bid faded hard at the belly, absorbed ~1:1 by domestic directs — *rotation, not hole*; dealers were NOT stuffed.

## 🟢 BND-11 RESOLVED (7/9 30Y reopen) — NOT FIRED, verdict ① HOLDING (7th benign test)

**912810UU0 · $22B · TreasuryDirect primary (comp-accepted %; June $ reproduce the 60.0/25.3/14.7 benchmark exactly → method validated):**

| Metric | Jul-9 | Jun-11 bench | Δ | Fire test | Leg |
|---|---:|---:|---:|---|---|
| Indirect | **77.74%** | 59.95% | +17.8pp | <52% | ❌ |
| Dealer | **10.05%** | 14.74% | −4.7pp | >18–20% | ❌ |
| BTC | **2.44** | 2.33 | +0.11 | <2.15* | ❌ |
| High yield | 5.058% | 5.020% | +3.8bp | — | priced in |
| Direct | 12.21% | 25.31% | −13.1pp | — | crowded out by indirect |

*\*BTC acute threshold **reconciled 7/9 to <2.15** (matched LIQUID; was 2.30 — a mis-ported 5Y line, non-discriminating vs the 30Y's 2.30–2.44 recent cluster). Tail-vs-WI unpinnable in-env (immaterial — gating legs already fail).*

**The inverse of the masked hole:** indirect **surged**, dealers **un-stuffed** — foreign demand for the long bond is robust. Confirms JGB-30Y-7/7 FIRM (SAM) + clean 10Y-7/8. **Channel split (HEN-40):** demand/flow FIRM; the ~5.05% 30Y *level* is the oil/term-premium channel (elevated, orderly — cleared a +3.8bp concession into a *surging* bid). **TERRY arm-#1 (= verdict ③) does NOT fire.** Live duration channel = arm-#2 (10Y sustain). Full grade → `outbox/2026-07-09_to-PROME_bnd11-30y-reopen-grade.md`.

> **✅ BND-11 RESOLVED 7/9 = NOT FIRED (verdict ① HOLDING).** Pre-reg `BND11_REFUNDING_PREREG_2026-07.md`; both agents graded to ONE metric: 30Y indirect as % of _competitive accepted_ vs June 6/11 = 60.0% — the 7/9 print **surged to 77.7%** (inverse of the masked hole; not <55%, dealers un-stuffed). Acute leg (BND-11 FALSE), **BTC threshold reconciled 7/9 to <2.15**: indirect <52% AND (BTC<2.15 OR tail>2bp) AND dealer>18–20% — every gating leg failed.
>
> **JGB 30Y auction 7/7 folded in as a LEADING INDICATOR (with SAM):** Japan = term-premium *correlation* amplifier, NOT a UST-flow seller → the JGB read-through moves the **term-premium/tail leg** of the US 30Y, NOT the indirect-composition leg (foreign-official bid, TIC-owned). So a JGB tail shifts my 7/9 prior only modestly (SAM-reconciled: weak JGB → benign 70%→~58%, P(acute)→~22%; soft → ~66%; firm → ~73%) and **cannot fire the demand-hole alone** — the binding indirect<52% leg is US-specific. **Two-step gate:** a JGB-soft is upgraded only if the US 10Y reopen 7/8 *also* comes soft (correlation transmitted); JGB-soft + US-10Y-firm = noise, revert to base. Circularity: JGB / 30Y-level / thin-bid are ONE term-premium root, not independent votes. Detail in the pre-reg file.

---


---

## Part B — BOTTOM LINE entries, 2026-07-10 → 2026-07-28

**[7/28 Tue ~14:40 ET — 7Y auction grade, PROME-spawned]** **The 7Y cleared, and it cleared the way my frozen spec said "policy-path holds" looks: BTC 2.49 dead on its trailing-12 median, indirect 70.15%, dealers at 12.97% and not stuffed.** `BND-13` resolves TRUE on branch B. **The 7/27 5Y cover marker did not extend to the back-belly** — normalized to each tenor's own median, the 5Y was −0.060 and *below its own trailing-12 minimum* while the 7Y was −0.005 with gross demand dead normal ($109.3B tendered vs a $109.6B median). So auction health **reverts 3 → 2 on the condition I wrote before the print**, one session after I fired the upgrade on a condition I also wrote before the print. Composite **12/35**. **The more useful part of this grade is the three places I argued against myself.** *First:* the headline "+12.6pp indirect surge" **overstates real demand** — directs fell −12.82pp, so end-user take was **87.03% vs 87.25% in June, flat**, and the indirect/direct boundary is reclassification-sensitive. The claim that survives is the narrower one: *dealers were not stuffed, gross demand was normal, and the concession was paid in price (+21.3bp)*. 70.15% is #17 of 50, top-third, **not a record**. *Second:* **the bias disclosure travels with the verdict.** My §4 is biased toward not firing, so this no-fire is the weak kind of evidence and HENRY was right to be told to discount it — **but the discount is calibratable.** The known defect is a *threshold-placement* error worth **0.82pp**; the indirect leg cleared by **~13pp**. A placement error cannot manufacture a thirteen-point margin, so the indirect *measurement* stands independent of where the bar sits, and I would have graded B under the corrected rule too. The **dealer** leg is the opposite case — it cleared by **0.032pp**, genuinely knife-edge, full discount applies — though it is precisely the wrong-signed leg the backtest says to drop, and dropping it makes B fire *more* cleanly. *Third:* **the spec had a hole I only found at resolution.** §4's branches were **not exhaustive** — a 13.05% dealer print alongside 70.15% indirect would have fired **no branch at all** and left BND-13 ungradeable. We landed 0.03pp from that. Same defect *class* as the tail leg and the hard-to-fire challenge: three instances in one day, all mine, all caught at or near resolution rather than at authorship. §4 was **not** edited; v1.1.4 makes a residual branch mandatory and requires the margin be stated on every leg. **One observation routed, not adjudicated:** the thin cover failing to extend 24h later into a *longer* tenor argues against a general repo-levered bid withdrawal **and** against the FOMC-eve confound (the 7Y priced *closer* to the FOMC, longer in duration, with normal cover) — that points 5Y-specific, and **KB-BND-092 is LIQUID's call, not mine.** **Position unchanged: TLT puts HOLD, no add.** Add-gate (c) is now resolved-and-dead; (a) DFII10 >2.5 is **7bp away** and (d) the FOMC is the only add-gate with a live catalyst. **Tomorrow 2:00PM is the event this week actually turns on — ~34% hike, no forward guidance — and nothing in today's auction speaks to it.**

---

**[7/28 Tue ~04:00 ET — 5-day-dark boot + 12-item mail drain]** **Three things changed while I was dark, and I was blind to two of them.** **(1) The FOMC is two-sided.** My surfaces carried "HOLD ~90% priced" on a 7/16 vintage; the live July-hike probability is **~34%**, and Warsh has removed forward guidance. That is a ~25pp error on the biggest event of the week, and it inverts the framing: I had been treating the *decision* as settled and the *guidance tone* as the event. At ~1-in-3 with nothing telegraphed, **the decision is the event** — and the 5Y auction priced 48 hours into it. **(2) Credit stopped being inert.** HY OAS ran 268→279 in two sessions off a nine-session flat range, CCC is 4bp from 1000, IG +2. My dashboard carried **275 tagged [7/2] for 26 days** — it survived every session precisely *because* it was plausible, sitting between the 263 trough and today's print. A stale number that looks wrong gets caught; one that looks reasonable does not. The widening is broad and quality-*indiscriminate*, so it reads as a repricing rather than a credit event — but it is 21bp from my watch line and I no longer get to call credit "not the story." **(3) The 7/27 5Y produced the first real cover marker of the cycle** — BTC 2.28, lowest since Sept-2022 — and I fired my own pre-registered `BTC<2.3` trigger on it even though I have a benign story, because that is what pre-registration is for. **But the mechanism did not fail: indirect demand ROSE with duration on the day (2Y 56.59% → 5Y 59.24%) and dealers were not stuffed.** Cover thinned; composition held. **The most useful thing I did this session was concede a specification error.** My joint HEN-42 falsifier did not fire, and that is not a pass — I anchored its DENY branch on a *2Y tail*, which a term-premium story structurally cannot produce, so it could only have fired if the thesis were already wrong for some other reason. It passed by construction. HENRY blamed himself for accepting it; the defect is mine as its author. The replacement 7Y pre-registration is keyed on **composition** and is **tail-free by construction**, and it carries an explicit *"the confound wins, defer"* branch — because FOMC-eve event risk and term premium predict the **same** thin cover and **different** composition. Separately: **HENRY over-retracted his FedWatch leg.** The instrument (scraped odds, six irreconcilable vintages) deserved to die; the claim it carried did not. Across the ~11% crude collapse, **DFII10 went 2.43 → 2.43 while T10YIE fell −7bp** — the policy path did not reprice on oil, measured cleanly on primaries he already uses. Re-instrument, don't retract. **Position: TLT puts HOLD, no add** — DFII10 2.43 is **7bp** from the 2.5 re-arm gate and no pre-registered add-gate has fired. Composite **12 → 14/35**.

---

**[7/18 Sat eve — label check + EU reconcile + weld, PROME-spawned]** **★ The "term-premium channel CONFIRMED" canon is a MISLABEL — corrected to "real-rate / higher-for-longer (policy-path-led) channel."** RED's flag was right: net of the 2Y policy component, the arm-completing +14bp 10Y move (7/6→7/13) was **real POLICY PATH, not a term-premium expansion.** The decisive tell is the curve shape — a **belly-led bear-flattener** (5Y +16 > 10Y +14 > **30Y +11**; the long end LAGGED, 30Y−10Y −3bp), which is the *opposite* of a term-premium expansion (that steepens, long-end-led). The "86%-real" fact is correct but "real ≠ term-premium": of the +14bp, ~14% is inflation-comp (T10YIE +2, 5Y5Y flat), and the ~86% real leg is ~80-90% policy-path / only ~0-7% term-premium. Term premium is elevated in the **level** (ACM 10Y TP +0.73%, positive first time since 2023 — why the 10Y won't rally) but was **flat over the move.** Operationally the falsifier sharpens: not "fast Hormuz de-escalation → Brent retrace" (that's a breakevens story, and breakevens were only 14%) but a **dovish Fed repricing** (FOMC 7/28-29) — already stress-tested, since cool June CPI+PPI did NOT break the line. **CARL's 7/18 weld compounds it:** the forward Aug-Sept core-CPI feed rides structural legs (Russia ban, distillate base, sticky freight), not Hormuz — so the arm is **doubly insulated from the Mideast book** (backward decomposition + forward inflation feed), softening TERRY's §9 concentration flag both ways. Route-out to PROME with the exact HEARTBEAT amendment wording. **EU-sovereign reconcile w/ LIQUID CLOSED:** BTP-Bund 83 / Bono-Bund 47 / GGB-Bund 71 [7/17] all benign; BOND owns the sovereign-curve, LIQUID owns the xccy transmission; ONE trigger BTP-Bund >200bp. Live rates: 10Y 4.57 [7/16] holding 6+ sessions ≥4.50, DFII10 2.35, ~15bp from the 2.5 re-arm. No new BOND trade rec (scoped); TLT puts HOLD, Will NO-ADD stands.

---

**[7/16 AM update — teams-mode, PROME-spawned]** **ARM-#2 (10Y five-close sustain) COMPLETED 5-of-5 Mon 7/13 → RESOLVED-ARMED 7/16.** Co-graded independently vs FRED DGS10 per my co-ratified semantics: 7/7 4.55 · 7/8 4.56 · 7/9 **4.54** · 7/10 4.56 · **7/13 4.62** (streak began after the 7/6 4.48 reset; 7/14 4.58 = 6 straight, live ^TNX 4.59 = 9bp over the line). The 7/9 official DGS10 (4.54) closed the one leg that was unposted at my 7/10 grade with **no cross-line divergence** — R3 clean, no restatement. **Fill decision RESOLVED NO-ADD (Will 7/16** — TERRY book-aware rec accepted, $500 banked; nothing owed. ACTIVE_DECISIONS commit e396dddd, GATE-TERRY-ARM2 RESOLVED-ARMED b64e970e). **The 10Y holds ≥4.50 on a REAL-YIELD / term-premium move, not inflation expectations** — 86% of the +14bp (7/6→7/13) is DFII10 (2.24→2.36, series high, ~14–17bp from the 2.5 re-arm); breakevens dead flat (T10YIE 2.25, 5Y5Y 2.21 anchored). That is *why* a deflationary June CPI (−0.42% MoM headline) didn't break the line — the line was never held by inflation expectations. Firm auctions (BND-11 NOT FIRED, indirect 77.7%) rule out a demand hole; this is real term premium / higher-for-longer real policy, with the 2Y up 13bp confirming a hawkish-hold Fed-path read. **Hormuz closed 7/11–12 + Brent $86 loads the JULY CPI path hot** (~+0.4–0.6pp headline MoM from gasoline alone; lands mid-Aug, after the FOMC) and reinforces the same term-premium channel — so the **4.50-line sustain through FOMC 7/28–29 is well-supported** (main falsifier: fast Hormuz de-escalation → Brent retrace → DFII10 eases). **ARM-#3 (May TIC, 4PM ET today): grade off NET TRANSACTIONS both net sellers, NOT holdings** — GATES.tsv condition text is stale (holdings), flagged to PROME; template staged. MIDAS DFII10 seam reconciled (2.31 [7/9] exact).

---

### [7/10 prior] Auction read — BND-11 NOT FIRED (verdict ① HOLDING)
**The month's decisive print came in firm, not hollow — the demand-hole did NOT bite.** The 7/9 30Y reopen (BND-11) resolved **NOT FIRED** (verdict ① HOLDING, high conf): foreign/indirect demand **surged to 77.7%** of competitive accepted (vs June 60.0%), BTC firmed to 2.44, and dealers took *less* than June (10.0%) — the **inverse** of the masked demand-hole we'd pre-registered as the likeliest way it bites. Seventh straight benign test, and every long-end demand read of the week points the same way (JGB 30Y 7/7 FIRM per SAM, US 10Y 7/8 CLEAN, US 30Y 7/9 FIRM). **The demand/flow channel is firm; the elevated 30Y level (~5.05) is the oil/term-premium channel** — the 7/8 truce-collapse oil shock (Brent $78.82→~$75.67) — which cleared a +3.8bp concession into a surging bid, i.e. orderly, not a buyers' strike (HEN-40 decoupled-channels). **TERRY arm-#1 (= BND-11 acute verdict ③) does NOT fire**; the live duration channel is arm-#2 (BND-12 / 10Y five closes ≥4.50 — 10Y 4.53 today, provisionally 3-of-5 pending the close, term-premium-driven). **TLT puts HOLD, no add** — no auction add-gate fired; DFII10 was 2.25 (<2.5 re-arm) at last read. **BTC acute threshold reconciled fleet-wide to <2.15** (BOND matched LIQUID; the 30Y's recent BTC cluster is 2.30–2.44 so <2.30 was non-discriminating). Credit a non-story at the index level (HY 275, IG 75); CCC tail (971) the only residue.


---

## Part C — the 7/18 term-premium label decomposition (RED's ask), archived 2026-08-18

**Retained verbatim as the reasoning of record.** It is *correct for its own window (7/6→7/13)* and is **not** retracted — but see `STATUS.md` 8/18: on the daily Kim-Wright series the regime **rotated** after mid-July, so this decomposition must never be cited as the CURRENT label.

## ★ Term-premium label decomposition (7/18, RED's ask — CORRECTED CANON)

**The arm-completing +14bp 10Y move (7/6→7/13) is REAL-POLICY-PATH-led, not a term-premium expansion.** Identity: Δ10Y +14 = ΔDFII10 +12 (real) + ΔT10YIE +2 (BE).

| Bucket | Δ | % | Evidence |
|---|---:|---:|---|
| (c) Inflation compensation | +2bp | ~14% | T10YIE +2 [7/6→7/13]; T5YIFR flat |
| (a) Expected real policy path | ~+11-13bp | ~80-90% | DGS2 +13 · DFII5 +12 = DFII10 +12 (parallel real); 10Y−2Y +1bp |
| (b) Real term premium (marginal) | ~0 to +1bp | ~0-7% | 30Y−10Y **−3bp** (long end LAGGED); ACM TP flat over window |

**Decisive tell:** belly-led bear-*flattener* (5Y +16 > 10Y +14 > 30Y +11) — a term-premium expansion produces the OPPOSITE (long-end-led steepening). **86%-real is correct; real ≠ term-premium.** LEVEL vs MOVE: ACM 10Y TP +0.73% [Jul-2026] elevated in the *level* (why the 10Y won't rally) but flat over the *move*. **Corrected label = "real-rate / higher-for-longer (policy-path-led) channel."** Falsifier shifts from oil-retrace → **dovish Fed repricing** (FOMC 7/28-29). Route-out to PROME for HEARTBEAT amendment (`outbox/2026-07-18_to-PROME_label-check-eu-reconcile-weld.md`). CARL weld (7/18) compounds: forward Aug-Sept core feed rides structural legs, not Hormuz → arm doubly-insulated from Mideast book (TERRY §9 softened).


---

## Part D — New Coverage Baseline (7/1): MBS/FHLB + EU rates, archived 2026-08-18

**Why archived:** 7/1-vintage baselines for VX-17/18/19, none of which has earned matrix weight. The EU leg is explicitly **not actively monitored** (spreads last read 7/17) pending an ECB-calendar verify at the primary. **Levels here are stale by construction — the live owner of each vector is `workbook/VX.tsv`.**

## New Coverage Baseline (7/1) — MBS/FHLB + EU rates

- **MBS/housing (VX-17, score 1):** primary spread ~200–205bp (at/below median — but *policy-compressed* by the Jan-26 GSE $200B purchase directive); CC spread ~100–110bp [EST]; Fed MBS $1.96T — **post-QT, principal paydowns are reinvested into T-bills** (balance sheet no longer shrinking; QT ended Dec-1-2025), not into coupons. Catalyst-monitored: Warsh active-sales (deferred to 2027 lane), GSE-release execution.
- **FHLB advances (VX-18, score 1):** $734B (3/31/26), +8.4% Q/Q (driver unattributed — read Q1 CFR narrative), ~30% below the 2023 SVB peak. Coordinate with REGINALD.
- **EU rates (VX-19, score 2):** **ECB is HIKING** — depo 2.25% (6/11, first since 2023, war-inflation), ≥1 more priced, full QT. **Peripheral spreads-to-Bund [7/17, TE 10Y benchmark; Bund 3.14%]: BTP-Bund 83bp (Italy 3.97) · Bono-Bund 47bp (Spain 3.61) · GGB-Bund 71bp (Greece 3.85) · OAT-Bund 79bp (France 3.93).** All benign/convergence-tight (Italy≈France > Greece > Spain — Greece trades INSIDE the core-periphery). **LIQUID reconcile CLOSED 7/18:** BOND owns sovereign-curve spreads + ECB/TPI mechanics; LIQUID owns the EU-bank→US xccy-funding transmission (the contagion channel, NOT Bund-flight which is a haven/tightening effect). ONE trigger: **BTP-Bund >200bp sustained = benign→contagion-relevant** (ECB TPI caps blowout). ⚠️ **OWNED MISS (logged 7/28, not quietly dropped):** the "7/23-or-24 GovC — verify date" row was carried three sessions, **the date was never verified, and the window passed ungraded.** Low-cost (spreads benign at last read) but it is precisely the defect PROME's 7/25 frame-spec packet warned about — a leg keyed to an unverified event date cannot be graded when it fires. **Next action: verify the ECB 2026 GovC calendar from the ECB primary and re-docket with a confirmed date. Do not grade the missed window retroactively off secondaries.** Spread levels above are **[7/17 — 11 days stale]**; the EU leg is *not* actively monitored until re-docketed.


---

## Part E — Japan intervention → UST supply, adjudicated 8/15 (archived 2026-08-18)

**Why archived:** the adjudication is CLOSED and its conclusion is carried forward in `workbook/FLOW.tsv` (`FL-BND-11`, status CONDITIONAL) and in the 8/31 MOF catalyst row. Retained here verbatim as the reasoning of record.

## ★ Japan intervention → UST supply: ADJUDICATED 8/15 (the fork is closed on one branch and the custody scare is a round-trip)

**`FL-BND-11` asserts that actual MOF intervention = mechanical UST reserve selling = a US long-end supply shock. That mechanism is now recorded as CONDITIONAL, and neither branch has been confirmed.**

**① FIMA take-up for the 7/30-31 operation is measured ZERO** (`KB-BND-111`). SAM pulled H.4.1 *"Repurchase agreements — Foreign official"* across all four releases spanning the op — including the 8/06 release, which **contains both op days** — and every column reads zero. **Because the average-of-daily-figures column also reads zero, an intra-week draw taken and repaid between Wednesday snapshots is EXCLUDED, not merely unobserved.** SAM had shipped BOND the opposite ("funding via repo, not sales ⇒ yen-buying does not imply UST supply"); that rested on a Bessent quote about wanting the facility *upsized* and an MOF post citing it — **statements about availability, not readings of use.** ⛔ **This does NOT invert to "USTs were sold."**

**② The custody "decline" is a ROUND-TRIP, and reading only the decline half inverts the conclusion** (`KB-BND-109`). SAM handed BOND the foreign-official UST custody lead explicitly (*"This is your domain. I am naming the instrument and the numbers, not the verdict."*). **Verdict, off 57 H.4.1 releases pulled from the Fed primary** (FRED's custody family was discontinued 2012 — that is a fact about FRED, not about the data):

| Window | Δ Wed level | z | pctile |
|---|---:|---:|---:|
| **BUILD** 7/16 → 7/30 | **+58,716mn** | **+2.45** | **100th — largest 2wk build in the sample** |
| **UNWIND** 7/30 → 8/13 | **−59,791mn** | **−1.68** | 2nd — largest 2wk decline in the sample |
| **NET** 7/16 → 8/13 | **−1,075mn** | — | **≈ zero** |

**The level went up by ~$59B into the ops and came straight back to where it started** — 8/13 (2,596,842) sits within **$1.1B** of 7/16 and **$0.4B** of 7/09. **The build is the more anomalous half**, and a round-trip of this shape is at least as consistent with a custodian/settlement artifact as with market transactions — the direction SAM's own three caveats (all foreign officials not Japan · redemptions cut custody with no sale · custodian shifts move balances with no transaction) already pointed. **Resolves the basis disagreement SAM flagged:** the weekly-**average** basis shows a five-week net of **+18,530mn** vs −1,075mn on the Wednesday basis — **opposite signs, same substance: no meaningful drawdown.**

> ⚠️ **The secular decline is REAL and separate — do not let this finding be read as denying it.** The 8/13 release prints **YoY −257,964mn** on the same line. **The op window contributed approximately nothing to that trend.**
> ⚠️ **Parser defect caught before publication** (`KB-BND-110`): the first-pass scraper silently skipped week/week changes under 1,000 and shifted a column onto the *agency debt* row, giving a base-rate stdev of 980,561 against a true **20,347**. The op-window rows were never affected — **what was wrong was the base rate I was about to grade against.** v2 fails loud on a band violation and reconciles the release's own printed Δ against my differenced averages: **0 mismatches in 56 consecutive pairs.**

**Honest state: FUNDING CHANNEL UNRESOLVED.** Goldman's decomposition (~$200B of Japan's ~$1T in cash/equivalents) means a ~$53-60B round fits inside the cash sleeve **needing no UST transaction at all**. **Definitive public record: FRBNY Q3 FX quarterly ~11/13** (ESF/SOMA split, size, whether warehousing was used); independent size read **MOF monthly ~8/31**. **Until then FL-BND-11 must not be re-stated as automatic.**

## ★ Term-premium label decomposition (7/18) — ARCHIVED, and PARTLY SUPERSEDED 8/18

**Full text → `domain/sources/2026-08-18_STATUS_archive.md` Part C.** The 7/18 finding — that the +14bp 10Y move of **7/6→7/13** was ~80-90% expected-real-policy-path and ~0-7% term premium, on the decisive tell of a **belly-led bear-flattener** (5Y +16 > 10Y +14 > 30Y +11) — **stands for its own window and is not retracted.**

⚠️ **What changed 8/18: the regime ROTATED after that window, and this desk had no instrument positioned to see it.** On FRED `THREEFYTP10` (daily Kim-Wright term premium, added to the dashboard 8/18), **7/13 → 8/07** gives a **long-end-led bear STEEPENER** — 2Y **−7bp**, 10Y +3bp, 30Y +9bp, with term premium **+2.5bp ≈ 83% of the 10Y move.** That is the opposite signature, on the same falsifier. **⇒ Cite the 7/18 decomposition as history, never as the current label** (`finding_claim_outlives_its_discredited_instrument` in reverse: the instrument is fine, the *window* expired).

## Global Long-End — JGB/FX panel (new, channel 6)

> **[7/16 re-scope — SAM v1.6.7 errata, KB-BND-079]** The "demand vacuum / lifers net sellers" framing below is **superseded**: SAM's base case is now **net-demand-POSITIVE** (Meiji floor auction-confirmed 7/7); the 30Y ~4.5% forced-seller tail is re-scoped to **J-GAAP statutory-impairment, mid-cap-concentrated (Fukoku/Asahi), DISORDERLY-only** — a thin conditional tail, not a fat reflexive one (DEWEY/WALTER SIG-W-20260710-004 concurs: ALM-buyer, not forced-seller). **BOND's Japan-as-term-premium-correlation-amplifier framing is unchanged and consistent** — my long-end tail work does NOT build on the old reflexive forced-seller mechanism. Do not re-cite it.

Japan's super-long demand vacuum is real and worsening (6/25 20Y JGB BTC 2.97x = weakest since the May-2025 rout; lifers net sellers; rinban stepped down to ¥2.5T/mo **effective 7/1**; BOJ stood aside through an 8.8bp 30Y rout) — but the 6/20–7/1 window shows **duration decoupling, not competition**: after the weak JGB 20Y, USTs *rallied* four sessions to a 7-week low. The 6/30–7/1 co-selloff had different signatures (JP: pure super-long steepener, 2Y −3/30Y +9; US: near-parallel +4–7bp policy repricing). **The armed transmission leg is FX:** yen at 40-yr lows, record ¥11.7T already spent Apr–May, Mimura verbal warning 7/1 — *actual* MOF intervention = mechanical selling from $1T+ UST reserves. **Live watch: USD/JPY 165 · BOJ Fri 7/31.** *(The "7/2 10Y JGB auction" watch item sat here 26 days after it passed — removed 7/28. The 7/22 40Y JGB has since cleared FIRM, BTC 2.83, with no channel-6 export to the US 30Y.)* Full read → KB-BND-065.

> **[7/16 DEFERRED — structural-demand corpus handoff, PROME routing 7/11]** HENRY handed BOND the UST structural-demand corpus (the term-premium "why" under the auctions): **ML-HEN-114/115** (Japan withdrawal $50–120B/yr, 30Y depth −30% [Mar vintage]), **FLOW-HEN-025 + VX-HEN-20.05** (Gulf recycling −$50–75B/yr [3/12]). All **Mar-vintage**; nobody owns the structural-demand layer in writing. **Refresh-or-retire deferred to a dedicated session** — it's the mechanism under my arm-#2 term-premium read but not urgent for the arm grades or the 4PM TIC. Owner: BOND.

## New Coverage Baseline (7/1) — MBS/FHLB + EU rates → ARCHIVED 8/18

**→ `domain/sources/2026-08-18_STATUS_archive.md` Part D.** VX-17 (MBS, score 1) · VX-18 (FHLB advances, 1) · VX-19 (EU rates, 2) — tracked in `workbook/VX.tsv` **outside the composite** until they earn matrix weight. ⚠️ **The EU leg is DORMANT, not merely stale:** spreads last read **7/17 (32 days)**, and the **ECB GovC calendar verify at the primary is still owed** — the 7/23 row passed ungraded for exactly that reason. **Re-docket with a verified date before grading anything on it.**