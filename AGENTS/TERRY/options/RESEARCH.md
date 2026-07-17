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

> **UPDATE 2026-07-17 (both open threads explored, Will-directed).** **TT-08 (PDT) verified TRUE** and unblocked — gone since 2026-06-04, Robinhood day-1 → § TT-08 VERIFIED. **The long-premium challenge was confronted and did not survive contact with independent evidence** → § THE LONG-PREMIUM CHALLENGE. Headline: *"buying premium is negative-EV"* describes a **regime that ended around 2012**, and the Fed/Yale paper that shows this **also implies tastytrade's own 15-16yr sample straddles the break.** **But this does not vindicate the book** — alpha ≈ 0 means *fairly priced*, not *profitable*, and the evidence is **S&P-500-only** while Will's instruments are TLT and single-names (**open item #5 — now the live thread**).

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
| **TT-08** | **"PDT is gone… level playing field."** Pattern Day Trader rule described as **removed**, framed as a *"pretty big structural change"* making ETF 0DTEs more accessible (can close intraday without a PDT strike). | V2 @0:28, 8:40 | **✅ CONFIRMED — primary-verified 2026-07-17 → unblocked. See § TT-08 VERIFIED.** | **The video was right.** PDT eliminated via FINRA Rule 4210 amendment; **SEC approved 2026-04-14** (Rel. 34-105226), **effective 2026-06-04** (FINRA RN 26-10). **Robinhood implemented day-1.** ⚠️ *Elimination ≠ no margin discipline* — see the verified section for what replaced it and what still binds. |

---

---

## § TT-08 VERIFIED — PDT is genuinely gone (primary-checked 2026-07-17)

**Verdict: the transcript's claim is TRUE and the check is closed.** Verified against primaries, not aggregators.

| Fact | Value | Source |
|---|---|---|
| Mechanism | Amendment to **FINRA Rule 4210**, replacing day-trading margin provisions with **intraday margin standards** | FINRA RN 26-10 |
| SEC approval | **2026-04-14** (Release No. **34-105226**; filed 2025-12-29, comments closed 2026-02-04) | SEC / FINRA |
| **Effective** | **2026-06-04** | FINRA RN 26-10 |
| Eliminated | The **$25,000 minimum equity**, the **day-trade count**, and the **"pattern day trader" designation itself** — *"in their entirety."* Firms are **no longer permitted** to classify customers as PDT | FINRA RN 26-10 |
| Replaced by | **Intraday margin deficit (IMD)** monitoring — equity must stay proportional to **real-time intraday exposure**; firms either block deficit-creating trades or issue a margin call | FINRA RN 26-10 |
| **Phase-in** | Firms may take up to **18 months → 2027-10-20** to implement | FINRA RN 26-10 |
| **Robinhood** | **Implemented day-1 (2026-06-04).** *"No more day trade restrictions or day trade calls with your Robinhood margin account."* Existing PDT flags cleared | Robinhood support |
| tastytrade | Also day-1 ready 2026-06-04 (self-reported) | tastytrade |

### What this does NOT mean — the part that matters
1. **⚠️ Elimination of PDT ≠ elimination of margin discipline.** A **fixed $25k floor** was replaced by **exposure-based, real-time control.** In some respects this is *tighter*: a deficit can now be caught **intraday**, not just end-of-day.
2. **The $2,000 margin minimum equity requirement still applies.** Unchanged.
3. **Repeated IMD violations still trigger restrictions.** tastytrade documents a **90-day restriction on creating/increasing short positions**; Robinhood's page says only *"repeated failures to meet requirements can lead to further restrictions"* — **vaguer, and unresolved.**
4. **Phase-in means broker-dependent, not universal.** Any *other* broker could lawfully still enforce PDT until **2027-10-20**. Robinhood is confirmed clear; **no other broker Will uses has been checked.**
5. **House requirements are unaddressed.** Neither FINRA RN 26-10 nor Robinhood's page states whether stricter in-house maintenance requirements apply. **Unknown — do not assume absent.**

### Consequence for the day-trading loop (`daytrading/`)
The **binding constraint that shaped that loop is gone** — no day-trade counting, no $25k floor, on Robinhood, since 2026-06-04. **This does not make day-trading a better idea.** S3 ran **−$3,969** and Will's own standing read is *"plug the leak, keep it small"* — the loop's problem was **never** PDT, it was **P&L**. Removing a constraint that was accidentally acting as a brake is **a risk, not an opportunity**: the rule was capping trade frequency for free. **TERRY's position: no change to the loop's standing, and the $500/card cap is now doing work PDT used to do for us.** *(Also worth noting: the loop's S3 window pre-dates 6/4, so PDT removal is **not** an explanation for those losses.)*

**Calibration note (recorded in fairness to the source):** this was the transcript's single riskiest, most checkable claim, and it **verified clean** — including the subtle framing that it was a *structural* change. That is a genuine mark **in tastytrade's favor** and it is recorded as deliberately as the criticisms above.

---

## § THE LONG-PREMIUM CHALLENGE — confronted, and it does NOT go the way tastytrade implies

**Why this section exists:** Will's standing instruction (7/17) — *if their research says long premium is negative-EV, that's a challenge to this book's whole expression style and should be confronted, not filed.* Confronted. **The result is the opposite of expected, and it is the most consequential thing in this file.**

### Step 1 — the tastytrade claim, and its actual shape
tastytrade's own published SPY strangle table: **~90% win rate · average win +$90 · average loss −$475.** That implies a **seller's EV of ≈ +$33.50/trade** — *(0.90 × 90) − (0.10 × 475)* — with a **5.3× loss-to-win ratio.** *(TERRY-computed from their figures; sanity-check: ≈ +$33.50 sits squarely inside the 21-DTE study's "+$20 to +$40" sweet spot — the two datasets corroborate each other.)* **Mirror it and the buyer's EV is ≈ −$33.50:** lose ~90% of the time, paid ~$475 when right. **That is the variance risk premium, and the classic literature (Coval & Shumway 2001; Bakshi & Kapadia 2003) backs it.** So on its face: **yes, buying premium was negative-EV.**

### Step 2 — the independent evidence, which is newer and cuts the other way
**Dew-Becker (Federal Reserve Bank of Chicago) & Giglio (Yale/NBER), "The decline of the S&P 500 variance risk premium," dated 2026-06-02** (Chicago Fed WP 2025-17). **S&P 500 options, 1987-2025.** Five strategies — **5% out-of-the-money puts** and ATM straddles, each with/without daily delta hedging, plus the variance swap. **Deliberately chosen as an independent, incentive-free check: a Fed/academic paper has no brokerage revenue riding on the answer.**

> **"After 2012 — a sample equally long as those in the original studies that found negative premia — standard options strategies no longer have statistically significant alphas or information ratios."**

- **Structural break: August 2012** (baseline; dated off a shift in dealer S&P 500 gamma, and confirmed by break tests accounting for multiple testing).
- Alphas are **significantly negative pre-2012 across all five strategies**, then **rise post-2012, turning positive for the straddle and delta-hedged straddle**. Betas barely move — so this is **not** a mechanical artifact of changing market exposure.
- **The killer line for the doctrine:** *"there was only a relatively brief period between 1987 and about 2010 where traded options earned a (negative) CAPM alpha. Outside that period, neither traded options nor their dynamic replication strategy had a nonzero alpha in either direction"* — **tested back to 1926.**
- **Mechanism:** dealer/intermediary frictions fell and retail gained the ability to *sell* options, not just buy → the demand asymmetry that created the premium collapsed → dealer net gamma went to zero **exactly when returns did.**
- **The authors' own bottom line:** *"now it is **much less expensive for investors to hedge deep losses in the aggregate stock market** than it used to be."* They frame it as an anomaly decaying after publication: *"markets are getting more efficient."*

### Step 3 — the honest synthesis (and the criticism this licenses)
1. **"Buying premium is negative-EV" is a claim about a regime that ended ~14 years ago.** It was true roughly 1987-2010. Independent, current evidence says it is **no longer true for SPX.** The premium-selling edge was a **~23-year window that has closed.**
2. **⚠️ tastytrade's sample straddles the break — this is a real methodological criticism.** Their study is *"15-16 years"* of data from a video inferred at ~2022-23 → a sample of roughly **2007-2023**, of which **~5 years sit in the pre-Aug-2012 regime where the alpha genuinely existed.** Their averages are therefore **blended across a structural break** and are biased *in favor of their own doctrine* (fleet pattern: `blended_index_masks_bifurcation`). **Important limit on this criticism:** it contaminates their **P&L levels** (the +$20-40, the +$33.50). It probably does **not** contaminate **TT-02's timing shape** — *when* CVaR explodes is a gamma/convexity fact, not a risk-premium fact, so **the inversion survives even though the levels don't.**
3. **🚨 But this does NOT vindicate the book, and I will not let it read that way.** *Alpha ≈ zero* means options are now **fairly priced** — **not** that buying them is profitable. **The structure supplies no edge in either direction.** Every dollar of expected value must come from **the thesis being right about direction and timing.** The correct conclusion is *"the premium tax on your expression is much smaller than the doctrine claims"* — **not** *"buying puts is now a good trade."*
4. **⚠️ Instrument mismatch — the sharpest limit here.** The paper is **S&P 500 index options only.** The book is **TLT and single-name banks.** Index VRP ≠ rates VRP ≠ single-name VRP, and the stated mechanism (SPX dealer gamma, retail SPX supply) is **explicitly index-specific.** **Do NOT assume the 2012 break transfers to TLT or HBAN.** That is a separate, unanswered question — and given the crash-ladder and the HBAN tail are both single-name/rates, it is **the one that actually matters for this book.** *(Open item #5.)*
5. **Status:** working paper (Chicago Fed WP / SSRN), June 2026. Authors are Fed + Yale/NBER; sample ends 2025. **High-quality but not yet peer-reviewed** — strong enough to overturn a house doctrine's applicability, **not** strong enough to found a trade on.

### What actually changes for TERRY
| | Before this check | After |
|---|---|---|
| "Long premium is negative-EV" | Unexamined tastytrade doctrine, treated as a live threat to the book | **Regime-bounded (1987-2010). Refuted for SPX post-Aug-2012 by independent evidence.** Not established either way for TLT/single-names |
| The 21-DTE study's P&L levels | Taken at face value | **Blended across a structural break → biased toward the house's own doctrine** |
| TT-02 (the CVaR inversion) | The file's headline finding | **Survives** — it's a convexity fact, not a premium fact |
| Cost of Will's expression | Presumed to carry a heavy premium tax | **Tax is likely much smaller than doctrine claims — but the edge still must come entirely from the thesis** |

**No rule changes, no card armed, no position touched.** This resolves a *doctrinal* question, not a trade one.

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
1. ✅ **TT-08 (PDT) — CLOSED 2026-07-17.** Primary-verified: **true.** Gone since 2026-06-04; Robinhood day-1. → § TT-08 VERIFIED. Residual unknowns folded into #2.
2. ✅ **Long-premium challenge — CLOSED 2026-07-17.** Confronted per Will. **Regime-bounded and refuted for SPX post-2012** by independent Fed/Yale evidence. → § THE LONG-PREMIUM CHALLENGE. Residual question folded into #5 — **which is now the live one.**
3. **🔴 #5 is the successor thread and the highest-value open question in this file** (see below).

**Still open:**
4. **TT-09 / TT-08 residuals — broker policy unknowns (one Will/broker answer closes all four).** (a) Robinhood's **house maintenance requirements**, if any, beyond FINRA minimums; (b) what Robinhood's *"further restrictions"* for repeated **IMD** violations concretely are — tastytrade documents a **90-day short-position restriction**, Robinhood is vague; (c) **assignment handling** near expiry; (d) **auto-liquidation** policy. Durable once answered.
5. **🔴 Does the post-2012 VRP collapse extend to TLT and single-name banks?** **The one that actually matters for this book** — the crash-ladder is TLT, the HBAN tail is single-name, and **Dew-Becker/Giglio is S&P-500-only with an explicitly index-specific mechanism** (SPX dealer gamma, retail SPX supply). If the break is index-only, Will's *actual* instruments may still carry the full premium tax and the good news above **does not reach them.** Needs separate evidence — rates VRP (TLT/MOVE) and single-name VRP literature.
6. **TT-04 — is there tastytrade research on management timing from a non-45-DTE entry?** Would test whether "21 DTE" is a real constant or a 45-DTE artifact.
7. **Re-check TT-06 (0DTE liquidity ranking) before use** — self-described fast-moving; XSP explicitly flagged by the presenters as likely to change.
