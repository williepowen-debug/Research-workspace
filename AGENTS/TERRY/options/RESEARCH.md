# OPTIONS RESEARCH — extracted claims + applicability grades
**Created:** 2026-07-17 · **Owner:** TERRY · **Tier:** EXTRACTED CLAIMS (middle tier)

**The pipeline this file sits in:** `sources/` (raw, verbatim) → **`RESEARCH.md` (extracted claim + applicability grade)** → an adopted rule in `RISK_RULES.md` / `CHART_OPTIONS_WORKFLOW.md`. **Three different confidence levels — do not collapse them.** A claim reaching this file has been *read and graded*, **not verified**. Nothing here is a TERRY rule until it is promoted, and promotion requires the applicability grade to survive.

**Applicability grades** are always *for THIS book* — long-premium, directional, catalyst-driven, $500 max loss/card:
| Grade | Meaning |
|---|---|
| **ADOPT** | Direction-agnostic and verified enough to shape a card. |
| **INVERT** | True, but measured from the **short**-premium side — its value to us is the mirror image. |
| **CONTEXT** | Useful background; does not change card construction. |
| **NOT-APPLICABLE** | Real finding, wrong book. Recorded *with the reason*, not dropped. |
| **VERIFY-FIRST** | Load-bearing but unverified. **Blocked from use until a primary check lands.** |

> **⚠️ Standing source-quality caveat on ALL tastytrade rows.** tastytrade is a **brokerage**. Its house edge is premium *selling*, and its revenue scales with **trade frequency**. The 21-DTE study's conclusion — *close early and redeploy* — happens to prescribe more trades. The video says the quiet part aloud: *"don't forget you can redeploy also when you manage that."* **This is not proof the finding is wrong** — the mechanism is sound and the data may well be real. It is an incentive flag that stays attached to every number below (auto-memory: `incentive_flag_source_weighting`). Their research is better than most retail sources; "better than most retail" is **not** the standard of the FRED/CFTC pulls I grade arms against.

---

## The one-paragraph verdict

**Both videos are premium-*selling* content, and this book is a premium *buyer*.** Taken at face value, almost nothing here is a rule TERRY should adopt. **But the 21-DTE study contains a finding they never state, because from their seat it's a cost rather than a product: the short strangle's tail risk explodes in the final ~2 weeks — and that explosion IS the long tail's payoff window.** Their own 15-year dataset, read from our side of the trade, is an argument for holding a *deliberate* tail bet into the terminal window rather than rolling out of it. That single inversion (**TT-02**) is worth more to this desk than everything else in both transcripts combined. The 0DTE video contributes durable market-structure facts (**TT-05**, **TT-09**) and **one claim that could materially change the day-trading loop but must not be acted on until verified (TT-08, PDT)**.

---

## Video 1 — "21 DTE magic" (management-timing study)

**Study design as described:** 15 years of option data *(stated "15 years" @3:12, **"16 years" @8:25** — unreconciled)* on **SPY / IWM / QQQ**. Sell **20-delta strangles** opened at **45 DTE**. Test **every fixed-duration management mechanic** from close-immediately through hold-to-expiration. Measure **average P&L** and **CVaR** (conditional value at risk — the mean of the worst ~5% of outcomes).

| ID | Claim | Source | Applicability to THIS book | Notes |
|---|---|---|---|---|
| **TT-01** | Average P&L peaks at **~24 days held = 21 DTE** on a 45-DTE entry, then **declines** from day 25→45. Trades held **<20 days** had **low** average P&L. Sweet spot ≈ **+$20 to +$40** avg; the 0-20d window is roughly a **−$10/+$10 coin flip**. | V1 @3:12, 5:57, 12:10 | **NOT-APPLICABLE** | Short premium, **delta-neutral**, index-only. This book is long premium, directional, single-name/TLT. The P&L curve being measured is **the theta we pay**, not collect. Recorded because it defines the counterparty's incentive, not ours. |
| **TT-02** | **CVaR is low early and explodes late** — sharp increases after ~30 days held, "mostly during the **last two weeks** of a trade," **in all three ETFs**. Hold to expiry and "your CVaR is off the charts." | V1 @6:26, 9:34 | **⭐ INVERT — the highest-value row in this file** | **The seller's CVaR explosion is the buyer's convexity payoff.** Tasty's own data locates where outlier moves get *paid*: the terminal ~2 weeks. From our seat that is not risk — **it is the product we are buying.** Directly bears on the crash-ladder (77/76/75) and the HBAN Oct-16 16P lottery ticket: **both are explicit tail bets, and this says the payoff lives in exactly the window a seller flees.** ⚠️ **Do not overclaim** — see § Limits. |
| **TT-03** | Managing early "eliminates outlier risk" / "flattens volatility" and captures the steepest part of the decay curve. | V1 @2:06, 9:18 | **NOT-APPLICABLE** | Same inversion as TT-02. "Eliminating outlier risk" is precisely what a tail buyer must **not** do — outlier risk is the thesis. |
| **TT-04** | **"21 DTE" is not a constant — it is ~53% of the cycle, an artifact of the 45-DTE entry.** | **TERRY-derived, not their claim** | **CONTEXT (a caution)** | The study tested fixed-duration mechanics *from a 45-DTE start*. **Nothing in it establishes 21 DTE as universal** — a 90-DTE trade's sweet spot is untested and unaddressed. The video brands it "the closest thing we've got in the world of trading to **Magic**," then quietly walks it back at 12:21: *"managing trades at 21 days… **may not be magic**, but leaving positions on for 24 days was in the sweet spot"* — **which is the same number restated as a holding period (45−24=21).** The "magic" is marketing; the finding is "hold roughly half the cycle." |

### Limits on TT-02 — read before citing it
The inversion is real but it is **not symmetric, and the numbers do not transfer.**
1. **Averages vs tails run opposite ways for a buyer.** The seller's edge exists *because* long premium is negative-EV on average. A buyer holding into the terminal window has a **worse average** outcome (theta bleed accelerates) and a **better tail** outcome. So TT-02 supports holding **only** where the position is *explicitly and deliberately* a tail bet. **It is not a licence to hold every long put to expiry** — for a directional put that needs an ordinary move rather than a crash, the accelerating bleed is a genuine warning against the same behavior.
2. **Instrument mismatch.** Measured on **20-delta index strangles (SPY/IWM/QQQ)**. Our tails are **deep-OTM single-name and TLT puts** (HBAN 16P was −13.2% OTM). The *mechanism* — terminal-window gamma/convexity — is general. **The magnitudes are not.** Never quote their CVaR figures onto our positions.
3. **The charts were never seen.** Extraction rests on the presenters' **verbal** reading of two slides — and one of them **misread the CVaR axis live and was corrected on air** (@5:34 → *"no no no no that's backwards"*). The corrected reading is the one recorded above. Treat the shape as reliable and the **specific values (−$10/+$40, CVaR $1,400) as indicative only.**
4. **Sample-length ambiguity unresolved** — 15 vs 16 years, stated 5 minutes apart.

### Live-book relevance (TT-02 applied — analysis, NOT a proposal)
| Position | Type | What TT-02 implies |
|---|---|---|
| **Crash-ladder 77/76/75** (approved fallback shape) | Deliberate tail | Terminal-window convexity is the whole point. **A 21-DTE-style early close would exit before the payoff window opens.** |
| **HBAN Oct-16 16P ×2** ("stress lottery ticket") | Pure tail, deep OTM | Consistent with **letting it ride** — which is already Will's stated 7/16 decision. TT-02 *corroborates* an existing call; it does not prompt a new one. |
| **TLT Sep-30 85P / Oct-16 82P** (Will's book) | **Directional grind, not a crash bet** | **TT-02 does NOT apply — this is the trap.** These need an ordinary move, so accelerating terminal bleed is a **cost**, not a product. Do not let the crash-ladder logic bleed onto them. |

> **Tension with root rule #7** (*"Roll duration, don't trim size"*): TT-02 suggests that on a **deliberate tail**, rolling *out* of the terminal window rolls out of the convexity you paid for. **This is a flag, not a rule change.** Rule #7 is Will-ratified and numbered-API stable; TT-02 is unverified secondary from the opposite side of the trade. **Not enough to touch #7** — logged so the question is askable later with better evidence.

---

## Video 2 — 0DTE product selection

**Scope note:** 0DTE is **not** TERRY's game — cards are 45+ DTE and catalyst-driven. It lands here anyway for two reasons: the **day-trading side loop** is live (`daytrading/`, S3 −$3,969), and near-expiry work already happens (**the 7/16 USO 7/17 calls triage was a 1-DTE decision**).

| ID | Claim | Source | Applicability | Notes |
|---|---|---|---|---|
| **TT-05** | **Settlement/assignment taxonomy.** **Indices** (SPX, XSP, NDX, RUT): **cash-settled, no assignment risk**, cannot be exercised early; **larger** contract size. **ETFs** (SPY, QQQ, IWM): deep liquidity, easier to size, **carry assignment risk**. **Futures** (ES/MES, NQ/MNQ): ~24h, SPAN margining, **settle to the futures contract** (which may itself settle to cash). | V2 @1:50-3:07, 3:33 | **ADOPT (direction-agnostic market structure)** | The cleanest, most durable content in either video. Cash settlement removes the wake-up-holding-100-shares failure mode. **Structural facts, not a house opinion** — this is what belongs in a workflow file. |
| **TT-09** | **Broker-specific operational risk:** assignment handling varies by broker; **many brokers auto-liquidate** if you lack capital to settle — potentially at a bad price/time; fees are broker- **and product**-specific. | V2 @4:11, 3:20 | **ADOPT (operational)** | Repeated three times, unprompted — the one point they clearly consider load-bearing. **Applies to Will's actual broker and is unknown to me** (`[POSITION_STATE_UNKNOWN]` extends to broker policy). Worth a one-time answer that then stays durable. |
| **TT-10** | 0DTE positions are "highly volatile"; sizes "should be **very very small**." | V2 @7:51 | **CONTEXT (already satisfied)** | Consistent with the standing **$500 max loss/card**. No change implied. |
| **TT-06** | **0DTE liquidity ranking:** SPX / SPY / QQQ / IWM deepest + tightest spreads; then ES / MES / NQ / MNQ "sufficiently deep"; **XSP / NDX / RUT thinner** but tightening fast. SPY dominates contract volume; **SPX trades more than ES**. Volume is *"only one aspect of liquidity"* — also want spreads + open interest. | V2 @4:41, 7:20 | **CONTEXT — ⚠️ DATED** | Their own caveat (volume ≠ liquidity) matches `CHART_OPTIONS_WORKFLOW.md` §3, which already requires bid/ask **and** OI. The **ranking is a snapshot of a fast-moving market** and they say so: XSP *"might be a totally different story in a couple of years."* **Re-check before relying on it.** |
| **TT-07** | NASDAQ products have the **highest std-dev of daily price change**, then Russell, then S&P. Cited live: *"E-minis have had a 10-point range. NASDAQ has had a 150-point range."* | V2 @6:05, 6:34 | **CONTEXT — the anecdote is misleading** | The **std-dev slide is the real claim**; the 10-vs-150 remark is **one day, unnormalized, across different-scale indices** — apples to oranges. Normalized it is ~0.18% (ES ≈5,500) vs ~0.75% (NQ ≈20,000): the directional conclusion survives, **the 15x impression does not.** Classic raw-points-across-scales error — **do not repeat the 10/150 framing.** |
| **TT-08** | **"PDT is gone… level playing field."** Pattern Day Trader rule described as **removed**, framed as a *"pretty big structural change"* making ETF 0DTEs more accessible (can close intraday without a PDT strike). | V2 @0:28, 8:40 | **🔴 VERIFY-FIRST — BLOCKED** | **The one claim here that could materially change the day-trading loop — and it must not.** PDT (FINRA's $25k pattern-day-trader threshold) is longstanding; **removal would be a genuine regulatory change I cannot confirm from a transcript, and the transcript is known-imperfect.** Unverified secondary on a **regulatory** fact is exactly what root Critical Rule #3 exists for. **Requires a FINRA/SEC primary check before it changes a single day-trading decision.** Status: **UNVERIFIED — not actionable.** |

---

## Dating (INFERRED — neither transcript is dated)

| Video | Inferred date | Evidence | Consequence |
|---|---|---|---|
| **V1 — 21 DTE** | **~May 2022-2023** *(low-medium confidence)* | thinkorswim built *"23 years ago"* (founded ~1999-2000 → ~2022-23); a **May 30th** webinar + **June 10th** Dallas show = a **May** air date; references Julia Spina's book (pub. ~2021) as recent. | **~3-4 years stale.** The **study is durable** (15yr dataset, structural mechanism). Any *market-structure* color is not. |
| **V2 — 0DTE** | **Materially newer, undetermined** | Frames PDT removal as recent/structural; *"zero DTE trend started a couple of years ago"*; XSP liquidity up *"the last couple of months."* | Newer, but **TT-06/TT-08 still need re-checking** — it explicitly describes a fast-moving landscape. |

**Decay class:** these are **durable research findings, not signals** — they do **not** belong in `SIGNALS.tsv` and must not inherit its 21-day decay bar. The right staleness test is **"has market structure moved?"** (TT-05/06/08), not "how many days old?" The **21-DTE mechanism (TT-01/02) does not decay** on that clock at all.

## Transcription decode (Will's flag, confirmed)
`sibo` → **Cboe** · `C bar` / `sivar` / `C var` → **CVaR** · `piano` → **P&L** · `spies` → **SPY** · `queues` → **QQQ** · `iwm` → IWM · `SSP` / `SXP` → **XSP** · `RU` → **RUT** · `24DE` *(V1 title)* → **21 DTE** · `20 Delta` → 20Δ · `GTH` → Global Trading Hours *(real term, transcribed correctly)* · `span margining` → **SPAN margin** *(real)* · `zerod` / `ZDES` / `ETEs` → 0DTE · **`"Julius penis book"` → almost certainly *Julia Spina's* book** (tastytrade researcher; *The Unlucky Investor's Guide to Options Trading*, ~2021 — fits "first book that ever covered this kind of stuff… first time anybody ever took tasty research"). **Inference, not certain** — flagged as the clearest demonstration that this transcript needs decoding, not trusting.

## Open items
1. **🔴 TT-08 (PDT) — needs a FINRA/SEC primary check.** Blocked until then; **do not let it touch the day-trading loop.** Highest-value verification in this file.
2. **TT-09 — Will's broker's actual assignment + auto-liquidation policy is unknown.** One-time answer, durable payoff.
3. **TT-04 — is there tastytrade research on management timing from a non-45-DTE entry?** Would test whether "21 DTE" is a real constant or a 45-DTE artifact.
4. **TT-02 — is there tastytrade research from the LONG premium side?** They almost certainly have "buying premium is negative EV" work. **That is a direct challenge to this book's whole expression style and should be confronted, not filed** (per Will 7/17). Would also let TT-02's inversion be checked against their own long-side numbers instead of my reasoning alone.
