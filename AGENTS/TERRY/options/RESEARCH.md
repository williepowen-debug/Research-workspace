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

> **UPDATE 2026-07-17 (both open threads explored, Will-directed).** **TT-08 (PDT) verified TRUE** and unblocked — gone since 2026-06-04, Robinhood day-1 → § TT-08 VERIFIED. **The long-premium challenge was confronted and did not survive contact with independent evidence** → § THE LONG-PREMIUM CHALLENGE. Headline: *"buying premium is negative-EV"* describes a **regime that ended around 2012**, and the Fed/Yale paper that shows this **also implies tastytrade's own 15-16yr sample straddles the break.** **But this does not vindicate the book** — alpha ≈ 0 means *fairly priced*, not *profitable*, and the evidence is **S&P-500-only**. **UPDATE — open item #5 now resolved (§ OPEN ITEM #5):** Will's actual instruments **split** — the **TLT crash-ladder likely pays the FULL rates-vol tax** (the equity break does *not* transfer to rates), while the **HBAN single-name tail is structurally cheap** except around its own 7/23 print. The SPX good-news reaches neither live tail cleanly; **the ladder is the one that pays.**

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
3. **The charts were never seen — PARTIALLY DISCHARGED 2026-07-17.** Extraction rests on the presenters' **verbal** reading of two slides — and one of them **misread the CVaR axis live and was corrected on air** (@5:34 → *"no no no no that's backwards"*). A **second, independent viewing** (a retail trader reading the same charts, § Tertiary corroboration) agrees on **both shapes** (P&L peaks ~day 24 then whipsaws; CVaR low early → explodes after 21 DTE). So the **shape is now doubly-sourced**; the **specific values (−$10/+$40, CVaR $1,400) remain indicative only** — still no one has quoted axis numbers I can verify.
4. **Sample-length ambiguity unresolved** — 15 vs 16 years, stated 5 minutes apart.

### Live-book relevance (TT-02 applied — analysis, NOT a proposal)
| Position | Type | What TT-02 implies |
|---|---|---|
| **Crash-ladder 77/76/75** (approved fallback shape) | Deliberate tail | Terminal-window convexity is the whole point. **A 21-DTE-style early close would exit before the payoff window opens.** |
| **HBAN Oct-16 16P ×2** ("stress lottery ticket") | Pure tail, deep OTM | Consistent with **letting it ride** — which is already Will's stated 7/16 decision. TT-02 *corroborates* an existing call; it does not prompt a new one. |
| **TLT Sep-30 85P / Oct-16 82P** (Will's book) | **Directional grind, not a crash bet** | **TT-02 does NOT apply — this is the trap.** These need an ordinary move, so accelerating terminal bleed is a **cost**, not a product. Do not let the crash-ladder logic bleed onto them. |

> **Tension with root rule #7** (*"Roll duration, don't trim size"*): TT-02 suggests that on a **deliberate tail**, rolling *out* of the terminal window rolls out of the convexity you paid for. **This is a flag, not a rule change.** Rule #7 is Will-ratified and numbered-API stable; TT-02 is unverified secondary from the opposite side of the trade. **Not enough to touch #7** — logged so the question is askable later with better evidence. **PROMOTION DECISION (Will-approved 2026-07-17):** NOT a numbered rule — wired instead as a **scoped construction note** in `CHART_OPTIONS_WORKFLOW.md` §3c, tag-gated to fire only on "deliberate tail" cards and explicitly walled off from directional puts. Promote to a numbered rule only after a deliberate-tail card fires live OR the magnitudes are independently verified.

### § Tertiary corroboration — an independent second viewing of the charts (2026-07-17)
A third transcript (`sources/2026-07-17_retail_21dte-reaction_tastytrade-study.md`) is a **retail trader re-narrating this same study** — no new data, and his own advice carries a heavy competence flag (self-described "new options trader," "50% return by year-end" goal, promoting the strategy). **It is worth exactly one thing:** he reads the actual P&L and CVaR charts on screen, and I never saw them (TT-02 limit #3 flagged the charts were unseen + one presenter misread the CVaR axis on air). His independent reading **corroborates both shapes**: P&L *"stays pretty steady… at around day 24 [=21 DTE]… before the whipsaw,"* then *"moved drastically"* by day 45 (**confirms TT-01**); and *"the SAR [CVaR]… go up and up… settles around 20-24… then rips back up… risk goes up a lot more after 21 DTE"* (**confirms TT-02's shape** — CVaR low early, explodes in the terminal window). **Effect:** partially discharges TT-02 limit #3 — the inversion's *shape* now has two independent viewings agreeing; the *magnitudes* remain unquoted/unverified. Also corroborates the QQQ caveat (he calls QQQ P&L *"sporadic/wild,"* 20Δ strangle *"probably not a good move"* — matches Video 1's "QQQ CVaR off the charts") and the **15-year** sample figure (not 16). **No new claim IDs — corroboration, not new findings.** One color-not-data note: his first-person account of getting **assigned before he could roll** a 7-DTE short strangle is a live illustration of TT-05/TT-09 assignment risk and of *"give yourself time to be right"* — but it's **short-premium** assignment (he's selling); a long-premium book faces the mirror problem, so it reinforces the *duration* logic (root rule #7) without transferring mechanically.

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

---

## § OPEN ITEM #5 RESOLVED — does the 2012 VRP collapse reach TLT and single-name banks?

**Dug 2026-07-17 (Will-directed). Answer: NO for TLT, YES for single names — the two instruments split, and the split is the whole point.** The SPX "good news" from the last section **does NOT transfer to the crash-ladder**, but it **is corroborated for the HBAN tail by a second, independent mechanism.** This is the answer that actually governs the book, because both live tails are rates or single-name — neither is index.

### Leg A — RATES (TLT crash-ladder): the premium tax most likely PERSISTS ⚠️

**Evidence the rates VRP is real and large:**
- **Mueller, Vedolin & Yen, "Bond Variance Risk Premia" (LSE FMG DP 699, Jan 2012), data 1983-2010**, options on **30Y / 10Y / 5Y** Treasury futures (covers TLT's long end). Shorting Treasury variance earns an **annualized Sharpe ≈ 2**; variance-swap shorts ~**+20%/month**; *"significantly negative and economically relevant,"* robust to transaction costs and margin. **Buying** bond vol protection was expensive — same sign as equities.
- **Critical vintage limit: that sample ENDS in 2010** — *before* the equity paper's Aug-2012 break. On its own it proves the rates VRP existed pre-break; it says **nothing** about survival.

**Evidence it PERSISTED past 2012 (unlike equities):**
- **Swaption VRP, 2015-2020 window:** short-vol in the interest-rate market *"remains highly statistically significant even accounting for transaction costs and margin,"* with **predictive power for future bond returns.** So the rates premium is documented **live well after** the equity break.
- **Recent tape (2026):** MOVE-implied has run **ahead of** realized — a 30-day realized/implied spread in the **~82nd percentile** on a 2-yr lookback during the March-2026 stress. Consistent with a **premium still being paid** for Treasury vol.
- **Mechanism argument (why the equity break should NOT transfer):** Dew-Becker/Giglio attribute the SPX collapse to **retail gaining the ability to *sell* SPX options** + dealer gamma normalizing — a **retail-supply** story. The **Treasury options market is institution/dealer-dominated, not retail-driven**; that specific mechanism has no obvious analog in rates. **The thing that killed the equity premium is largely absent here.**

**⇒ Verdict for the crash-ladder (TLT 77/76/75 puts): assume the full premium tax still applies.** The SPX good-news does not reach rates. **⚠️ This is an INFERENCE, graded MEDIUM** — built from a pre-break existence paper + post-break swaption persistence + a mechanism argument. **I did NOT find a direct post-2012 structural-break test for rates** (the clean analog to Dew-Becker/Giglio doesn't appear to exist yet). Two real limits that cut toward the ladder anyway: (1) the rates VRP is **most negative at short-dated / near-the-money** and the **sign can flip positive at long maturities/tenors** — the crash-ladder is **short-dated OTM**, i.e. the **expensive** end; (2) variance-swap/swaption VRP measures **ATM variance**, while deep-OTM **put skew** is a distinct animal not directly covered. **Net: the crash-ladder pays a real vol tax, and TT-02's convexity argument is the reason to pay it anyway — not evidence that it's cheap.**

### Leg B — SINGLE-NAME (HBAN / bank tail): the tax is SMALL ✅ (independent corroboration)

- **The variance risk premium lives at the INDEX level, not the single-stock level.** Single-name equity options are priced **close to fair value**; the premium is a **correlation risk premium** created by institutions **over-buying *index* puts** for portfolio hedging, which inflates *index* IV relative to component IV.
- **Magnitude:** S&P 500 **implied correlation ~39.5% vs realized ~32.5%** (DJ30: 46.0% vs 35.5%); implied exceeds realized **~70% of trading days.** That gap **is** the premium — and **single names don't carry it.** (This is exactly what dispersion trades monetize: sell the overpriced index, buy the ~fair components.)
- **Convergence, two ways:** this is a **different mechanism** from Dew-Becker/Giglio reaching the **same conclusion** for individual options — component/single-name options ≈ fairly priced. Independent corroboration (fleet: `shared_antecedent_independence_test` — genuinely independent, not circular).

**⇒ Verdict for the HBAN Oct-16 16P tail: the single-name premium tax is small — the position is ~fairly priced structurally, so this is NOT where the money leaks.** ⚠️ **One real exception, and it's live for HBAN:** the "fairly priced" result is an **average over calendar time**; **single-name IV gets rich into an *earnings* catalyst**, and **HBAN Oct-16 spans the 7/23 BMO print.** Event-vol richness is a **local** premium the structural result doesn't cover — so the lottery ticket likely **did** pay some event-vol premium at entry. Consistent with Will's own "stress lottery ticket" framing; doesn't change the ride-it-out call, but names the one place the single-name tax actually bites.

### The synthesis that matters
| Instrument | Live tail | Structural vol tax | Basis |
|---|---|---|---|
| **SPX index options** | (not in book) | **~zero post-2012** | Dew-Becker/Giglio, direct break test |
| **TLT / rates** | **crash-ladder 77/76/75** | **⚠️ likely FULL — persists** | pre-break existence + post-break swaption persistence + institution-dominated microstructure (MEDIUM-confidence inference) |
| **Single-name banks** | **HBAN Oct-16 16P** | **✅ SMALL** — ~fairly priced | correlation-risk-premium literature + Dew-Becker convergence; **local exception: earnings-event vol (7/23)** |

**The trap this kills:** it would have been easy to take the SPX good-news and quietly assume "buying puts is cheap now" across the book. **That is wrong exactly where it's most expensive** — the **crash-ladder is the one live tail that pays the full tax.** The correct read: **structure supplies no free edge in either name; the ladder additionally pays a real rates-vol premium (justified only by the convexity in TT-02), while the single-name tail is structurally cheap except around its own print.** As always: **the edge must come from the thesis, and TERRY does not arm on any of this** — it's construction context, not a signal.

**No rule changed, no card armed, no position touched.**

---

## § OPEN ITEM #9 RESOLVED — the deep-OTM skew / crash premium (dug 2026-07-17, Will-directed)

**The caveat as originally written ("both VRP papers measure ATM variance, not deep-OTM skew") was half-right and needs correcting in BOTH directions.** The skew collapse reaches *further* than I implied, but the *deep* tail — exactly where the crash-ladder and HBAN sit — stays genuinely untested. Net: **the deep tail is the one place a residual premium most plausibly survives, so assume the crash-ladder pays a skew tax on top of the rates tax.**

### The historical baseline: the skew premium was real and grew MONOTONICALLY with depth
**Bondarenko, "Why are Put Options So Expensive?" (SPX futures puts, 08/1987-12/2000):** 1-month puts had average excess returns of **−39%/month ATM** rising to **−95%/month deep-OTM** — i.e. **the deeper the strike, the more overpriced.** Selling them was a documented "puzzle"; cumulative buyer→seller wealth transfer ≈ **$18bn** over the sample. For the deep tail to break even, an **Oct-1987-magnitude crash would have to occur ~1.3× per year.** **This is the base rate for BUYING deep tail insurance: near-total premium loss in most months.** Directly quantifies the theta/decay drag the crash-ladder pays for its convexity.

### Correction #1 — the post-2012 collapse reaches FURTHER than "ATM only"
Re-reading Dew-Becker/Giglio: their five strategies **explicitly include the 5% OTM put**, and the structural-break tests *"do not reject… stability over time for **the put**, straddle, and delta-hedged versions"* — i.e. the **5% OTM put's alpha went to ~zero post-2012 just like the straddle.** They go further: *"volatility and **jump** risk… have not captured any premium in the recent data,"* and they measure realized **jump** variation directly. **So the skew/jump premium collapse is IN their result, at least out to 5% OTM.** My original caveat over-implied that OTM was untouched — wrong. Don't lean on stale Bondarenko-era "deep puts are always rich" logic; that regime (1987-2000) is even *older* than the ATM one and is refuted at 5% OTM.

### Correction #2 — but the DEEP tail (8-13% OTM) is genuinely untested, and it's where a premium most likely persists
- **Depth gap is real.** DBG stop at **5% OTM.** The live tails are **deeper**: crash-ladder ~**8-11% OTM** (TLT 77/76/75 vs ~$84), HBAN 16P ~**13% OTM**. **No study I found tests whether the collapse extends to the 8-13% strip.** Searched directly — the post-2012 deep-tail question is under-researched (the literature that does exist — Bollerslev/Todorov/Kelly-Jiang tail-risk factors — uses deep-OTM puts to *measure jump risk*, not to test whether their premium decayed).
- **Two mechanisms argue the deep tail could survive the collapse that killed 5%-OTM:** (1) **price-insensitive institutional hedging** — institutions buy deep index puts *"because they must, not because it is cheap,"* keeping deep-OTM demand permanently inflated post-1987; (2) the deep tail is nearly **pure jump risk** (diffusive/variance risk barely touches a far-OTM strike), and DBG's *mechanism* — retail gaining the ability to *sell* — plausibly clears the **variance** premium (sellable via straddles) far better than the **crash-jump** premium (few retail agents write deep tail insurance). **So the thing that collapsed the ATM/5%-OTM premium may not reach the deep jump strip.** Unproven either way — lean: **assume a residual deep-tail premium, especially at the far strikes.**

### What this changes for the two live tails
| | Depth | Verdict on the skew/deep-tail tax |
|---|---|---|
| **TLT crash-ladder 77/76/75** | ~8-11% OTM | **Double reason to assume it PAYS:** it's rates (VRP persists, Leg A) **AND** deep-OTM (skew premium most likely to survive). The 75P especially is far-tail. **The convexity (TT-02) is the justification for paying both.** |
| **HBAN Oct-16 16P** | ~13% OTM | Single-name is structurally cheap (Leg B), **but 13% OTM + earnings-event is where any residual single-name premium concentrates** — the deep strike and the 7/23 print stack. Cheapest of the caveats, not zero. |

**Bottom line for the caveat:** don't over-apply the SPX good-news to the far tail. **The crash-ladder pays a real premium — rates VRP + deep-OTM skew — and Bondarenko quantifies the base rate (near-total monthly decay, break-even only on a ~annual '87-scale crash).** That is precisely the trade TT-02 says to make *anyway*: accept the steep average bleed to own the terminal-window convexity. **The research doesn't veto the ladder — it prices the tax, and the tax is real. No rule changed, no card armed, no position touched.**

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
5. ✅ **RESOLVED 2026-07-17 → § OPEN ITEM #5.** The instruments **split**: **TLT rates tail likely pays the FULL vol tax** (rates VRP persisted past 2012; equity break doesn't transfer — MEDIUM-confidence inference), **single-name HBAN tail is structurally CHEAP** (~fairly priced; premium lives at the index level) **except around its own 7/23 earnings print.** Successor threads → #8, #9.
6. **TT-04 — is there tastytrade research on management timing from a non-45-DTE entry?** Would test whether "21 DTE" is a real constant or a 45-DTE artifact.
7. **Re-check TT-06 (0DTE liquidity ranking) before use** — self-described fast-moving; XSP explicitly flagged by the presenters as likely to change.
8. **Rates VRP post-2012 — no direct break test found.** Leg-A verdict is a MEDIUM-confidence inference. A clean post-2012 structural-break study of Treasury/swaption VRP (the rates analog to Dew-Becker/Giglio) would upgrade or overturn it. Watch for one.
9. ✅ **RESOLVED 2026-07-17 → § OPEN ITEM #9.** Skew premium was real + monotonic in depth (Bondarenko: ATM −39%/mo → deep-OTM −95%/mo, 1987-2000). DBG's collapse **reaches to 5% OTM and into jump risk** (further than "ATM only"), **but the deep 8-13% strip — where both live tails sit — is untested and is where a residual premium most plausibly persists** (price-insensitive institutional hedging + pure-jump strikes that retail can't easily supply). Verdict: **crash-ladder pays rates VRP + deep skew (double tax); HBAN's deep strike + 7/23 print is where its small single-name premium concentrates.** Successor: #10.
10. **Acknowledged gap — NOT actively tracked (Will 2026-07-17 declined a standing watch as un-serviceable over a months+ horizon):** no post-2012 deep-OTM (8-13%) put-return study exists (genuine literature gap), and the rates verdict wants a direct post-2012 break test. **Recognize, don't hunt:** if either crosses the desk during options/VRP/tail research, check the **Bollerslev / Todorov / Kelly-Jiang** orbit or DBG follow-ups and fold the result into §#9 / §#5 + memory `[[finding_vrp_split_rates_vs_singlename]]`. Deep premium *collapsed* → skew tax small (upgrade); *persisted* → confirms the DOUBLE tax. Either way prices the tax, doesn't veto — so **nothing here blocks or changes a trade decision today.**

---

# SOURCE 3 — MenthorQ, "Mastering Options Greeks" (graded 2026-08-20, TERRY)

**Raw:** `sources/2026-08-20_menthorq_greeks-cheatsheet-and-higher-order.md` · **Provided by:** Will, in-session, from Twitter/X.

> **⚠️ Standing source-quality caveat, same class as the tastytrade block above.** MenthorQ is a **commercial vendor whose product is higher-order-Greek / GEX analytics.** The article's thesis — *first-order Greeks are insufficient; you need Vanna/Vomma/Zomma/Speed* — **is the vendor's sales case restated as pedagogy.** The mechanics are standard textbook derivatives and are not in doubt; the **emphasis** is not independent. Weight the math, discount the "these are critical" framing. Additionally: **no URL, byline, or publication date was supplied** — this arrived pasted into a chat. Nothing here may be cited as a source; anything load-bearing was **re-derived locally** (`scripts/greeks.py`) and is graded on the re-derivation, not on the article.

## The one-paragraph verdict

**Roughly 85% of this is generic options pedagogy this desk already applies, and its "Common Strategies" columns are premium-SELLING doctrine** — Iron Condors, Credit Spreads, Covered Calls, Short Straddles, "Theta-selling portfolios," "Selling post-earnings premium." **This book is a premium buyer; that column is the counterparty's playbook, not ours** (identical posture to the tastytrade grading). **But two rows are genuinely load-bearing for the live book, and one of them killed a headline finding of my own from two days ago.** The Vega table's *"drops as expiry nears"* and the article's **Vanna** treatment both bear directly on the 8/18 conclusion that `TRY-FIRE-004`'s harvest gate is a volatility gate — **MQ-02** (vega decay makes that gate *decay*) and **MQ-03** (vanna makes the price-leg and vol-leg *non-separable*, which my 8/18 read treated as independent). ⚠️ **Credit where it is actually due, measured not asserted: the 8/18 headline died 80% because of the bond rally and only 10% because of vega decay** (§ decomposition). The article's value is **forward-looking, not retrospective** — vega decay is the term that compounds from here and that nothing on the card was tracking.

| ID | Claim | Applicability to THIS book | Notes |
|---|---|---|---|
| **MQ-01** | Delta/Gamma/Vega/Theta definitions; gamma highest ATM + short expiry; theta accelerates near expiry; long premium is always short theta. | **CONTEXT (already applied)** | Textbook, correct, and already embedded in `CHART_OPTIONS_WORKFLOW.md` and every card's structure section. Changes nothing. Recorded so the file shows it was read and rejected as non-novel, not skipped. |
| **MQ-02** | **Vega is "highest for long-dated, ATM options" and "drops as expiry nears."** | **⭐ ADOPT — and it invalidates a dated headline of my own** | **Direction-agnostic and re-derived locally.** Consequence: a harvest gate reachable *via a vol pop* gets **monotonically harder every day**, because the same IV point buys less. **This was not on the 004 card and was not being tracked.** See § MQ-02 APPLIED. |
| **MQ-03** | **Vanna** = dVega/dSpot; vega and gamma "often peak in the same regions of the surface"; price and vol sensitivities interact rather than add. | **⭐ ADOPT (as a caveat on my own method)** | **My 8/18 measurement priced the two legs as SEPARABLE** — *"needs −2.37%"* OR *"IV ≥18 clears flat."* For a long OTM put they are not: **vega rises +50.8% on a −1% spot move** (measured, § MQ-03 APPLIED). The joint path pays **more** than either leg read alone, and the "no price move at all" branch is the **least** likely route to the gate, not the cheapest. |
| **MQ-04** | Every "Common Strategies" column: Iron Condors, Credit Spreads, Covered Calls, Short Straddles/Condors, Butterflies, "Theta-selling portfolios," "Selling post-earnings premium," gamma scalping with stock. | **NOT-APPLICABLE (wrong book), recorded with the reason** | Premium-**selling** structures requiring margin, delta-neutral rebalancing, and a short-gamma risk profile. This book is **long premium, directional, defined-risk, $500 max loss/card, no naked shorts.** Their own Gamma table says it: *"Naked short options are dangerous."* Agreed — which is why we do not run them. |
| **MQ-05** | Zomma, Speed, Color, Ultima, Veta, Vera (3rd-order Greeks) are "critical" for stress testing and hedging. | **NOT-APPLICABLE — and this is the vendor's sales case** | **3rd-order Greeks matter to a delta-hedged market-maker rebalancing a book continuously.** This desk holds **1–25 contracts of defined-risk long premium to a catalyst and does not hedge dynamically.** Speed/Zomma would change no decision we make. ⛔ **Do not adopt these to look rigorous** — instrument count is not rigor. |
| **MQ-06** | *"Delta also serves as a proxy for the likelihood of an option expiring in the money."* | **⚠️ CONTEXT — imprecise as stated; do not repeat in a card** | The ITM probability is **N(d₂)**, not delta (**N(d₁)**). The article states the folk approximation with no caveat, and **the error is SIGNED BY OPTION TYPE — which the article never says.** Measured (S 83.02, 41 DTE, IV 12.7%): **put K=77 — abs(delta) 0.0287 vs P(ITM) 0.0316 ⇒ delta UNDERSTATES by −9.2%**; **call K=90 — delta 0.0388 vs P(ITM) 0.0354 ⇒ delta OVERSTATES by +9.7%.** ⭐ **For THIS book the direction is the lucky one: on long puts, quoting delta as P(ITM) is CONSERVATIVE.** ⚠️ But `[[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]]` — the sign is fixed by type; whether it protects or flatters belongs to the trade. **On the call side (USO 135C, XLE 65C) the same shortcut FLATTERS.** Use **N(d₂)** whenever a card states a probability. ✍️ *Recorded honestly: I first wrote this row asserting the CALL direction for a put and had the sign backwards; the measurement caught it before it left the desk.* |
| **MQ-07** | Diagram: **Strike** drawn as an input with **no arrow to any Greek** — the only unconnected input. | **CONTEXT (a caution about the diagram, not the math)** | Strike drives every Greek in the diagram; it is unconnected because it is the one input a holder cannot vary continuously. Harmless, but it means the chart is a **mnemonic, not a dependency graph** — do not read structure into it that isn't there. |

## § MQ-02 APPLIED — the 8/18 vol-gate headline is DEAD, and this is the retraction

**The 8/18 block on `FLOW-TRIGGER_duration-TLT-put.md` states, as its headline branch:**
> *"IV ≥18% CLEARS WITH NO PRICE MOVE AT ALL (0.374 flat)"* — measured at 43 DTE, spot 81.64, against the then-current **$0.33** gate.

**That figure was correct when written and is now false.** Re-derived with `scripts/greeks.py` (whose selftest carries the 8/18 figure as a **permanent regression case** — the tool reproduces `0.374` before it is allowed to disagree with anything):

| state | spot | DTE | gate | **IV needed to clear with NO price move** |
|---|---|---|---|---|
| **8/18 (as written)** | 81.64 | 43 | $0.33 | **17.09%** ⇒ "≥18% clears" was right |
| **8/20 (today)** | 83.02 | 41 | $0.3469 | **20.80%** |

**Decomposition — measured, so the article gets credit for exactly what it earned and no more:**

| cause | isolated effect on the IV needed | share |
|---|---|---|
| **spot 81.64 → 83.02** (the 8/19 bond rally) | **+2.96 pts** | **80%** |
| DTE 43 → 41 (**vega decay — the MQ-02 term**) | +0.37 pts | 10% |
| gate $0.33 → $0.3469 (Will row 61, fees-in) | +0.28 pts | 8% |
| **all three (today's true state)** | **+3.71 pts** | |

⇒ **MQ-02 did not cause this; the bond rally did.** The article's contribution is **forward**, and it is the term nothing was tracking — holding spot fixed at 83.02, the vol-only route to the gate degrades on its own:

| DTE | date | IV needed, no price move | vega per IV pt |
|---|---|---|---|
| 41 | 2026-08-20 | 20.80% | 0.0182 |
| 30 | 2026-08-31 | 24.04% | 0.0088 |
| **21** | **2026-09-09** ← buyback window opens | **28.47%** | 0.0030 |
| 14 | 2026-09-16 ← FOMC | 34.61% | 0.0005 |
| 7 | 2026-09-23 | 48.58% | ~0 |

🔑 **The two back-half catalysts this card is counting on — CPI 9/11 and FOMC 9/15-16 — sit where the vol route needs ~29% and ~35% IV respectively, from 12.7% today.** The 8/19 sb0607 block already found the buyback operation *"suppresses the tail-VOL pop that the 8/18 block showed does almost all the harvest-gate work."* **MQ-02 says the vol route is closing on its own timetable regardless of the buybacks** — two independent mechanisms, same direction, and only one of them was on the card.

⛔ **NO GATE MOVED, NO THRESHOLD SHAVED, NOTHING PROPOSED, $0 MOVED.** A gate is not widened for becoming harder to reach — that is the exact move `ledger_sweep` forbids by name. This is a **measurement of what would have to happen**, per `RISK_RULES` #14 (all of it is MOMENT-property and expires). ⚠️ **IV input is the 8/18 chain's 12.70%** — the 8/20 pre-open chain returned **every Sep-30 put row `DEAD` (0/0)**, which is the quote-sanity guard working correctly rather than a defect. **Re-pull IV post-open before any decision.**

## § MQ-03 APPLIED — my 8/18 method treated two legs as separable and they are not

The 8/18 block reads the price route and the vol route as alternatives. **Vanna says they are coupled.** Measured on today's state (S 83.02, K 77, 41 DTE, IV 12.7%):

| | vega per IV pt |
|---|---|
| at spot 83.02 | **+0.0182** |
| at spot 82.19 (**−1%**) | **+0.0275** |
| | **+50.8%** |

⇒ **A −1% TLT day makes every subsequent IV point worth ~half again as much.** Consequences, stated as method corrections to my own prior work:

1. **The realistic path is the DIAGONAL, not either axis.** Today's surface: at IV 12.7% the gate needs **−4.17%**; at IV 20% it needs **−0.44%**; but a **−1.5% day with IV to 18%** clears it, and neither leg alone is close. **The gate's honest description is a joint (move × IV) boundary** — the surface, not a number.
2. **The flat-vol model UNDERSTATES the good case.** No skew is modelled, and a real TLT selloff steepens put skew, so the OTM strike's own IV rises *more* than ATM. **Bias direction stated so it is not mistaken for precision** — the tool's docstring carries it.
3. **It does not rescue the position.** Vanna amplifies a move that has to happen first. **−4.17% at today's IV is a worse tail than 8/18's −2.37%**, and the 3-year sample has no session beyond −3.02%.

## § Promotion decision

**NOTHING here is promoted to a numbered `RISK_RULES` rule today.** MQ-02 and MQ-03 are **ADOPT-grade and already wired where they bite** — as `scripts/greeks.py` (re-derivable on demand, selftested, with the 8/18 regression pinned) plus the § blocks above and the card annotation. **A numbered rule is not warranted**: this is measurement method, not trading discipline, and `RISK_RULES` #14 (*re-measure at any decision*) **already carries the obligation** — MQ-02 is a demonstration of why #14 exists, not a new rule beside it. **MQ-06 (N(d₂) not delta for stated probabilities) is the one candidate for promotion** if a second instance appears; logged, not promoted, on n=1.
