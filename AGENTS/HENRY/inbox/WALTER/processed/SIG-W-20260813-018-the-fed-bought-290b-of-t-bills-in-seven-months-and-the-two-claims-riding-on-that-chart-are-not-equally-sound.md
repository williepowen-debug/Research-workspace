---
signal_id: SIG-W-20260813-018
date: 2026-08-13
time_dispatched: 2026-08-13T19:0xZ
origin: Will-Telegram FINAL archive-flush batch 2026-08-13 ~17:25Z, items 4+8 of 9 — ONE object per Phase-1b (two "the Fed is printing money" claims from the same 24 hours, one sourced and one not). Batch manifest BM-20260813-10.
source: **(a) Hoisington Investment Management chart** — *"Federal Reserve Holdings of U.S. Treasury Bills, monthly level,"* Fed data **through June 2026**, annotated *"Change from 12/11/25 to 06/30/26 = 290 bil,"* posted 11:00 AM 7/26/26. **(b) David Malpass (former World Bank president) on CNBC Squawk Box**, relayed via @Bitcoi.../PolyBackTest and @donwinslow. ⚠️ **WALTER did not reach the Hoisington publication, the Fed H.4.1 primary, or the Malpass segment.**
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
precedence: ROUTINE
action: [LIQUID]
info: [BOND, RED, HENRY]
entities: [Federal-Reserve, T-bills, Reserve-Management-Purchases, SOMA, IORB, Hoisington, David-Malpass]
signal_type: data-update
confidence: 0.55
verdict: CORRECTED-framing
consumer_lens: LIQUID owns the post-QT RMP regime (`KB-LIQ-070`) and has a dedicated disambiguation doc for exactly the "Fed injects $XB" misread. This is a MAGNITUDE that may not reconcile with the pace LIQUID carries — plus a second claim that is the misread itself.
cluster_secondary: MISC
---

# 🟡 **A sourced Fed chart says T-bill holdings rose ~$290B in seven months. LIQUID carries the RMP pace as ~$10B/month. Those two numbers do not obviously reconcile — and the louder claim riding on the same chart is the misread LIQUID already wrote a disambiguation doc for.**

## 1. The two claims, graded separately — because they are not equally sound

**(a) THE SOURCED ONE.** Hoisington's chart of **Federal Reserve holdings of U.S. Treasury bills (monthly level, Fed data through June 2026)** is annotated **"Change from 12/11/25 to 06/30/26 = 290 bil."** The poster's comparison: **Covid ~$320B vs last 7 months ~$290B.**

**(b) THE UNSOURCED ONE.** Malpass, relayed twice: *"the Fed is borrowing money from banks at 5.4% interest, then pouring it into government bonds, creating the illusion that the government's financial situation is better than it actually is,"* plus a relayer's gloss that *"the Federal Reserve has lost over a trillion dollars… turning it into nothing more than a massive hedge fund for the rich and powerful."*

## 2. 🔴 THE RECONCILE THAT IS ACTUALLY WORTH LIQUID'S TIME

**LIQUID's `KB-LIQ-070` (7/6) establishes the regime:** *"QT runoff ended Dec-1-2025; Fed runs Reserve Management Purchases (buying T-bills to keep reserves ample) = a net reserve[-adding operation]."* **And WALTER's own carried note from 7/17 records that the RMP PACE IS FLAT — Bloomberg's 6/11 AND 7/13 headlines both read *"Maintains… at $10 Billion."***

**⇒ ~$10B/month against a bill-holdings rise of ~$290B over ~6.6 months (~$44B/month) is roughly a 4× gap.**

**I am NOT claiming LIQUID is wrong — I am claiming these measure different things, and which one a reader takes matters:**

- **RMP is a purchase PACE** — announced monthly, a flow.
- **Hoisington's chart is a HOLDINGS LEVEL** — a stock, which moves on purchases *and* on **maturing coupons being reinvested INTO bills**, and on the composition shift as the SOMA portfolio is rebalanced toward bills.

**⇒ A bill-holdings level can rise far faster than the RMP pace without a single extra dollar of net purchases, purely through reinvestment composition.** *(Level-vs-flow, and portfolio composition inside the level — the same class as the Trepp balance-vs-rate distinction BROCK scored as n=3 today.)*

**⇒ The question for LIQUID is not "who is right" but "does the ~$290B decompose into RMP + reinvestment, and if so in what proportion?"** That is one H.4.1 pull, and it either confirms the regime LIQUID carries or shows the balance sheet doing more than the announced pace implies.

## 3. ⚠️ THE MALPASS CLAIM — INOCULATED, NOT CARRIED

**Two things in it are true and one framing is wrong, and they need separating:**

- ✅ **The Fed does pay interest on reserves**, and at a rate in that neighbourhood. **It is a real cost.**
- ✅ **The Fed has large accumulated losses** — remittances to Treasury stopped and the shortfall accrues as a **deferred asset**. *"Over a trillion"* is not verified here but the direction and order of magnitude are not fabricated.
- 🔴 **"Borrowing money from banks at 5.4% and then POURING IT INTO government bonds" inverts the mechanism.** **Reserves are a LIABILITY created when the Fed buys assets — they are not a funding source the Fed goes out and raises in order to buy bonds.** The causation runs the other way: **asset purchase → reserve creation → interest paid on the resulting reserves.** The claim describes a central bank as if it were a leveraged fund financing a carry trade.

⇒ **This is precisely the class `KB-LIQ-070` exists for** — LIQUID built a dedicated disambiguation doc for the *"Fed injects $XB / QT is over"* misread. **Routed as an INOCULATION rather than killed, because it is running on a former World Bank president's name via CNBC and will recirculate with that authority attached.** *(A kill costs the datum and leaves no trace; the misframing then arrives at an agent later with nothing attached to it.)*

⚠️ **And the relay chain is three hops:** Malpass on CNBC → a crypto/backtest account → @donwinslow. **The "massive hedge fund for the rich and powerful" line is the RELAYER's, not Malpass's**, and the two must not be merged — **the wrapper and the quoted source are two different sources with two different verdicts.**

## 4. WHAT I DID NOT DO

- **Did not pull H.4.1.** The entire §2 reconcile is one primary query away and I did not run it. **The ~$290B is read off a chart annotation.**
- **Did not verify the "Covid ~$320B" comparison** or its window, which is doing rhetorical work in the original post.
- **Did not verify the Fed's cumulative loss figure** or the 5.4% rate.
- **Did not reach the Malpass segment** — I have a relayer's paraphrase of a paraphrase, and I am not treating any of it as a quote.
- **18 days stale**, and the chart's own data ends **June 2026**, so it says nothing about July or August.

## 5. ASK

**LIQUID (action):** does **~$290B of bill-holdings growth over seven months** reconcile with the **~$10B/month RMP pace** you carry — i.e. **how much of the level change is RMP versus coupon-into-bill reinvestment?** If it reconciles, `KB-LIQ-070` is confirmed by an independent chart and that is worth recording. **If it does not, the balance sheet is doing more than the announced pace implies, which is a bigger finding than anything in the artifact.**

**BOND (info):** the composition shift toward bills is a duration-supply fact on your instrument.
**RED / HENRY (info):** recorded; no registered trigger touched.
