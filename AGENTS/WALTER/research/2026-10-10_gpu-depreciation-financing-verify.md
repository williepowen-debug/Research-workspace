# GPU depreciation / useful-life cluster: verify-research (2026-10-10, Sat)

Read-only helper for WALTER. All reads made 2026-10-10. Google News links were decoded to publisher URLs. Pages were pulled with curl and turned into text locally. "Read" below means the full visible article text was read, unless the row says otherwise.

Grade key: **CONFIRMED** = read at a primary or a named wire (directly or in a full syndicated copy) · **RELAY-ONLY** = only secondary outlets reached · **UNSUPPORTED** = no source found · **FALSE** = contradicted by a primary.

---

## Item 1: "Don't Believe Your Lyin' Eyes, GPU Depreciation & Useful Lives" (Burry, Cassandra Unchained)

| Field | Finding |
|---|---|
| What I read | PRIMARY https://michaeljburry.substack.com/p/dont-believe-your-lyin-eyes-gpu-depreciation, **paid post: only the free preview was readable** (~6 KB of text). It cuts off at "Below, Billy the Kid's 1968 pitch against the 2026 tape." |
| Published | 2026-10-01T17:23:37Z (Substack `datePublished`). Subtitle: "Hystory Rhymes, Part II: Nvidia & The Great Winfield". |
| Source class | Primary (author's own newsletter) |
| Core claims, free portion (primary) | (a) "On September 27th, as part of a larger investor presentation, Nvidia threw up a slide" titled **"Nvidia AI Infrastructure Retains Value Beyond Accelerated Depreciation Schedules."** (b) The slide plots the retained value of **A100, H100 and B200** against a **5-year accelerated depreciation curve**, implying companies are OVER-depreciating. (c) Names Tae Kim (author of *The Nvidia Way*) as a celebrant. (d) The rest is an excerpt from Adam Smith's *The Money Game* (1968) on the 1960s computer-leasing mania: Leasco Data Processing, Randolph Computer, Data Processing and Financial General; "at least three percent cash"; "what makes a finance company worth fifty times earnings". |
| Paywalled claims (RELAY-ONLY, via Stocktwits; Yahoo carries the same text) | (e) Nvidia's chart is "derived from analytics firm Silicon Data" and is **a DCF of forward rental income over an assumed 8-year physical chip life, not secondary resale prices**, so it is "apples-to-oranges" against a 5-year curve. (f) Quote: "A chip earning more than it costs is a sign of scarcity due to memory and power shortages, not GPU die shortages and not durability." (g) Legacy rental rates should drop once shortages ease and Vera Rubin ramps. (h) In 1968, lessors used **8-year** depreciation against IBM's **4-year**. System/370 collapsed rental yields, and leasing equities fell **~80% by 1970**. (i) Risk could shift to "institutional lenders and private insurers" through GPU ABS, structured debt and private credit. |
| Independent check on (e) | **Silicon Data's own methodology page CONFIRMS the mechanism.** Its "GPU Residual Value" is "a continuous discounted cash flow valuation over the GPU's expected useful life", built from its 36-month rental Forward Curve, with "maximum physical operating life ... currently estimated at around 8 years". (https://www.silicondata.com/products/gpu-residual-value). Whether Nvidia's slide used this exact series is Burry's claim, relayed. |
| Grade | **CONFIRMED** for (a)–(d) at the primary. **RELAY-ONLY** for (e)–(i). (e) is mechanism-corroborated by Silicon Data's primary methodology page. |
| Useful-life specifics? | **In the readable text: only the 5-year accelerated curve on Nvidia's slide.** Per the relay: an 8-year modelled life (Silicon Data) and the 1968 analogy of 8-year lessors against 4-year IBM. **No hyperscaler 5–6-year server-life figures appear in the readable or relayed text of this post.** Companies named: Nvidia, Silicon Data (relay), IBM and the 1960s lessors. His hyperscaler work is in separate paid posts: Sept 19 ("Heretic's Guide Part IV: The Big 5 Hyperscalers & the Missing $3 Trillion", a study of 10-K/10-Q footnotes) and Sept 24/26 ("Capital Cycle IQ & Forensic Files on the Big 5 Hyperscalers (MSFT, AMZN, ORCL, META, GOOG)"). The free preview of the Sept 24 post gives S&P 500 net investment/GDP of **2.07% as of June 30** and **12 straight negative quarters, mid-2003 to mid-2006**. |
| Date traps | (1) Nvidia's slide is dated **Sept 27, a SUNDAY**. I could not find the Nvidia deck itself, so the date rests only on Burry's word. (2) The hyperscaler figures often attached to Burry (**$176B understated depreciation 2026–2028; Oracle ~27%, Meta ~21% earnings overstatement by 2028; 5–6-yr booked vs 2–3-yr real lives**) come from his **Nov 10–11, 2025** X posts, not from this post. Items 7 and 9 re-attach them to 2026 stories. |

## Item 2: "Michael Burry likens Nvidia's AI boom to 1960s computer leasing bubble" (Seeking Alpha / TradingView / Yahoo)

| Field | Finding |
|---|---|
| What I read | Seeking Alpha direct returned **403**. I read the **full SA text through TradingView's syndicated copy** (https://www.tradingview.com/news/seekingalpha:e80aa8d85094b:0-michael-burry-likens-nvidia-s-ai-boom-to-1960s-computer-leasing-bubble/). Yahoo/Stocktwits version read in full (https://finance.yahoo.com/technology/ai/articles/michael-burry-warns-nvidia-ai-213700343.html). Yahoo 10/4 (Benzinga) read in full. |
| Event date | 2026-10-01 (Thursday; Burry post 17:23Z) |
| Source class | Relay of a primary |
| Core claims | Summarises Item 1 faithfully: Sept 27 slide, A100/H100/B200, 5-year accelerated curve, Tae Kim, *The Money Game*. It adds that "last week" Burry warned that Big Tech AI spending (MSFT, GOOG, AMZN, META, ORCL) could produce big write-offs, citing S&P 500 net investment negative for **12 consecutive quarters mid-2003 to mid-2006**. That matches the free preview of Burry's Sept 24 post. |
| Grade | **CONFIRMED.** The relay matches the primary's readable text. |
| Date traps | None in the SA copy. |

## Item 3: "Productive, Durable, Fungible: How NVIDIA AI Factories Maximize Return on Investment" (NVIDIA Blog)

| Field | Finding |
|---|---|
| What I read | PRIMARY https://blogs.nvidia.com/blog/productive-durable-fungible-ai-factories/, full text |
| Published | 2026-10-01T13:00:49Z, by Shruti Koparkar |
| Source class | Primary (corporate advocacy: these are Nvidia's claims and the third-party data it chose) |
| Core claims (numbers) | Each MW of AI factory costs **~$60M**. Vera Rubin NVL72 delivers **>30x** throughput/MW against GB300 NVL72 and **up to 45x lower cost per million tokens** on DeepSeek V4 Pro (SemiAnalysis AgentX). A100 shipped **2020** and is still in service; **CoreWeave extended bookings for 2020-era units through 2029**. Sprout (Sept 2026, "The Productive Life of a Data Center GPU"): every major operator has extended server depreciation life. **Microsoft's V100 fleet ran 8.4 yrs against a 6-yr book life**. **Barkr:** useful life **5–6 yrs** for an 8-GPU H100 system and **9–10 yrs** for GB300 NVL72, based on resale. **Silicon Data:** a 6-yr-old A100 is "still worth a quarter of what it cost" where a 5-yr schedule had it at zero more than a year ago. **Ornn Data:** A100 rent on a 5-yr contract is **80%** of the 1-month rate. GTC Berlin keynote is set for **Oct 21**. |
| Grade | **CONFIRMED** that Nvidia published these claims. The underlying third-party figures were **not independently verified**. |
| Caveat | Silicon Data's "worth a quarter" is the output of its **DCF residual-value model** (see Item 8), not an observed resale price. |

## Item 4: "Nvidia's bet that its chips can finance the AI boom gets a Wall Street reality check" (Reuters)

| Field | Finding |
|---|---|
| What I read | Reuters direct returned **401**. I read the **full Reuters text in BNN Bloomberg's syndicated copy** (https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/01/nvidias-bet-that-its-chips-can-finance-the-ai-boom-gets-a-wall-street-reality-check/). Byline: Saeed Azhar, Isla Binnie, Max A. Cherney, Stephen Nellis, plus Gertrude Chavez-Dreyfuss. |
| Event date | 2026-10-01 (URL date) |
| Source class | Named wire (Reuters), sourced to anonymous bankers plus named credit managers |
| Core claims (numbers) | Some lenders want **higher guarantees** than Nvidia first outlined for its **US$500B financing plan** (announced in August with Blackstone, Apollo, KKR and others). Nvidia has said some deals could carry **no more than a 25% residual-value guarantee**. **Three banking sources:** Nvidia may need to guarantee all deals or have them backed by investment-grade offtake. "The market is not ready" to treat Nvidia compute like aircraft. **Tens of billions** of pipeline deals are likely to carry strong guarantees and contracts. **Impax (Trzcinka):** "Banks typically underwrite GPUs over a **3-4 year** depreciation schedule", against Nvidia's claim of up to a **decade**. **S&P (Andrew Chang):** GPUs work "well north of five years" so far, but S&P takes a conservative view of their value. **Wellington (Moran)** and **TCW (Gelfand)**: precedents suggest creditors "do not subscribe to long average lives". Nvidia cites studies showing clouds moved server lives to **5–6 yrs from 3–4**, and Barkr's **9–10 yrs** for GB300 NVL72. **Precedents:** CoreWeave **$8.5B** facility, the first IG GPU-backed loan, rated **A3** on Meta's contract. Broadcom backstopped **>80% of a $35B** structure for Anthropic. Nvidia gave an RVG for SB Energy's Ohio project (per S&P/Moody's). Nvidia statement: compute is a "productive, durable and fungible asset". Five of six partners declined to comment and Apollo did not respond. |
| Grade | **CONFIRMED** (named wire, full text) |
| Date traps | None. The $500B plan is the Aug 10, 2026 announcement (see Item 5). |

## Item 5: "Key facts: NVIDIA $500B GPU loan; $10B to OpenAI; Burry buys 2027 puts" (TradingView)

| Field | Finding |
|---|---|
| What I read | https://www.tradingview.com/news/tradingview:97d647c56ba00:0-key-facts-nvidia-500b-gpu-loan-10b-to-openai-burry-buys-2027-puts/, full text. Published 2026-10-02 07:00Z. **The page carries its own disclaimer: "This is an AI-generated summary and may contain inaccuracies."** Its legs credit GuruFocus, Reuters and Stocktwits. |
| Source class | Machine-generated relay (aggregator) |
| Leg A: "$500B GPU loan" | **Garbled.** The real event: on **Aug 10, 2026** (Nvidia newsroom date; StorageNewsletter syndicated copy read) Nvidia announced **MOUs** with **Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR** to set up independent compute financing platforms to "mobilize **over $500 billion of third-party capital** ... over time". Nvidia "may provide residual-value support for **up to 25%** of an opportunity" (quoted in StorageNewsletter's commentary on Nvidia's blog FAQ). Partnerships are subject to final agreements. It is **not a loan, not Nvidia's money, and nothing has been lent at $500B.** The summary's "3–4 year depreciation" is Impax's line in Item 4 (banks underwrite GPUs over 3–4 yrs), not a figure from lenders as a group. |
| Leg B: "$10B to OpenAI" | **CONTESTED / off-topic.** Newsquawk (2026-10-01 18:16Z), citing The Information: Nvidia and SoftBank each made the **final $10B of their $30B pledges** to OpenAI's last round. CryptoBriefing says Nvidia did NOT make an October tranche and only SoftBank did. TradingView's "pledged $10B ... totaling $20B" fits neither version. |
| Leg C: "Burry buys 2027 puts" | **RELAY-ONLY.** Stocktwits (10/1): Burry "covered all his short common-stock positions" in MU, NBIS, CAT, SOXX, CRWV, NVDA and PLTR, and "replaced the Nvidia short with **September 2027 puts** at strikes in the **mid $100s**". Primary: Burry's "Trading Post September 28, 2026" is paid. Its only free line is "repositioning the portfolio ... I am moving timelines up." Other relays give conflicting Burry NVDA put histories (Dec-2027 $110 strike; Jan-2027 $115; Sept 9 sale of Dec-2026 puts). Strike and expiry cannot be checked at the primary. |
| Grade | Leg A **FALSE as worded** (the underlying $500B MOU target is CONFIRMED). Leg B **CONTESTED**. Leg C **RELAY-ONLY**. **Do not route this item. Route the underlying events instead.** |
| Date traps | It merges three unrelated events (Aug 10 announcement, Oct 1 OpenAI tranche, Sept 28 Burry repositioning) under a 10/2 date. |

## Item 6: "Nvidia Reportedly Turns To Insurers To De-Risk AI Chip Loans..." (Benzinga on Yahoo; primary = FT)

| Field | Finding |
|---|---|
| What I read | FT primary **403/paywall**: https://www.ft.com/content/d6a9f5df-08d0-4f80-ad2d-5d8a17e2cc82 (Google News stamps it 2026-09-28; TNW and Benzinga say "reported on Tuesday" = Sept 29). Read in full: Benzinga/Yahoo (2026-09-29), Investing.com via Finviz, TNW (2026-09-29T16:25Z), Bisnow (2026-09-30), Startup Fortune (9/28). |
| Source class | FT (named outlet), reached **only through relays** |
| Core claims (consistent across 4 relays) | Nvidia has held **early-stage** talks with insurers on structures to insure loans to **neoclouds** that pledge Nvidia chips as collateral. The insurer would pay lenders if a borrower defaults and the chips can't be resold for enough. Nvidia shared **chip-depreciation and future compute-price data** with at least one insurer. It is working with reinsurance broker **Howden Re** (Howden declined to comment). It has explored insurers **syndicating risk to hedge funds and alternative investors**, because deal sizes could exceed individual insurers' balance sheets. It has also considered joining financing consortia. **No agreements; the talks may not produce deals.** Nvidia: AI infrastructure is "uniquely productive, durable and fungible". TNW adds that the FT's Lee Harris said start-ups now sell "residual value insurance", and many large insurers are already at their limit for AI exposure. |
| Grade | **RELAY-ONLY** (FT text not read). There is strong cross-relay consistency, so it is safe to route labelled "FT-reported, relay-verified". |
| Extras in relays (unverified) | Benzinga: Nvidia had **$36B** of typically six-year cloud-service commitments "according to an SEC filing from July 26". **July 26, 2026 is a Sunday**, so it is probably the fiscal-quarter end, not the filing date. Benzinga: "Nvidia has agreed to provide up to **$105 billion** in guarantees" for an Ohio data center leased by an OpenAI affiliate: **not verified** (Reuters mentions only an RVG of unstated size for SB Energy Ohio). Startup Fortune: "$125B" guarantee ceiling, which is just **25% × $500B** arithmetic attributed to Axios (Axios 403). It also uses CNBC insurer reporting from **April 2026**, a date trap. |
| Context | TNW/Finviz: the report came a day after Nvidia added a record **$150B** to its buyback (Mon Sept 28). Not verified at the Nvidia primary. |

## Item 7: "Banks Push Deeper Into Risky GPU-Backed Loans Across Asia's AI Boom" (Startup Fortune; primary = Bloomberg)

| Field | Finding |
|---|---|
| What I read | **Full Bloomberg text in The Business Times (Singapore) syndicated copy**, 2026-10-06 12:37 SGT, signed "BLOOMBERG": https://www.businesstimes.com.sg/companies-markets/banking-finance/banks-chase-risky-chip-loans-asias-us8-2-trillion-ai-buildout. Startup Fortune relay read in full (2026-10-06). |
| Source class | Named wire (Bloomberg), read in syndication |
| Core claims (numbers) | Asian banks are moving into GPU financing that was previously private-credit-only. PwC: Asia data-centre spending could reach **US$8.2T by 2050**. Banks played key roles in GPU loans totalling **~US$3.8B** to **GMI Cloud, Zankore and PaleBlueDot AI**. **Citi** was sole debt adviser on **Zankore's US$3.1B** (Indonesia). **JPMorgan** was placement agent for PaleBlueDot. **Citi, JPM, Barclays, Deutsche, Santander and SMBC** are evaluating GPU-linked loans. GMI Cloud is in talks for a new **US$300M** loan (Thai data centre; Tencent end user). **UOB** is leading talks for Zankore's fresh **US$6B** (chairman Vikram Sinha, Sept 22), with Zankore scaling **10x to 1 GW**. **Ares (Arougheti):** "No one could really articulate ... what the depreciation curve looks like"; returns run only **~100–200bp** over other AI-infra lending. **In the GMI Cloud and Zankore loans (Sept), Nvidia agreed to buy any unsold computing capacity** as a backstop. Hogan Lovells Cadwalader (Eric Tan) warns of "rapid depreciation, technology obsolescence and volatile rental rates". |
| Grade | **CONFIRMED** (Bloomberg) |
| Date traps (in the Startup Fortune relay) | It drops in Burry's **$176B 2026–2028** understatement and "5–6-yr lives vs 2–3-yr obsolescence" as if current. **Both are Nov 2025.** Its GMI "$635M" and PaleBlueDot "~$300M" figures do not match the Bloomberg text (in Bloomberg, $300M is GMI's new loan). **Use the Bloomberg/BT figures only.** |

## Item 8: "Nvidia B200 58% Premium Fuels GPU-Backed Loans" / "NVIDIA B200 Resale Value Hits 158%" (tech-insider.org)

| Field | Finding |
|---|---|
| What I read | Both tech-insider articles in full (2026-09-18 01:22Z and 01:31Z). Wccftech 2026-09-16 in full. **Silicon Data's own methodology page** in full. The Silicon Data X post (Sept 16, 2026, which Wccftech embeds) **was not reached**. |
| Chain | Silicon Data X post (9/16) → Wccftech (9/16) → tech-insider (9/18). The tech-insider pieces are second-hand, plus padding pulled from other trackers. |
| Core claim | B200 "residual value" = **158% of launch price**, a 58% premium, about 1 year after mass availability. A100/H100 residual values are "well in excess of what 3 or 5-year straight-line schedules would imply". B200 rental went from **just under $5/hr (Jan 2026) to $5.50–5.80/hr (Aug 2026)** per Silicon Data via Wccftech. |
| Key finding | **The "resale value" framing is wrong.** Silicon Data's "GPU Residual Value" is a **DCF of projected rental earnings over an ~8-year useful life** using its 36-month Forward Curve. It is not a secondary-market transaction price. So "158%" means **current high B200 rental rates, capitalised**, not "selling used for 58% more than new". tech-insider's FAQ line ("current resale value on the secondary market equals 158 percent") is **contradicted by Silicon Data's own description**. The "fuels GPU-backed loans" link is the site's own speculation. Its B200 street-price table ($45–55K) mixes unverified trackers. This is the **same Silicon Data model Burry says sits under Nvidia's Sept 27 slide** (Item 1e), so the figure is the bull side's exhibit and is disputed. |
| Grade | 158% figure **RELAY-ONLY** (Silicon Data via Wccftech). "Resale value" label **FALSE** (contradicted by the primary methodology). **Do not route as a resale price.** |
| Date traps | None on dates. Two-hop relay; the 9/18 date trails the 9/16 origin. |

## Item 9: "The GPU Depreciation Debate Behind This Week's AI Dip" (Value The Markets)

| Field | Finding |
|---|---|
| What I read | https://www.valuethemarkets.com/analysis/gpu-depreciation-debate-behind-this-weeks-ai-dip, full text, 2026-09-16T09:04Z |
| Source class | Blog / explainer (it cites MarketWatch, Reuters and SEC 10-Ks) |
| Core claims | Burry: hyperscalers depreciate GPUs over **4–6 yrs** (elsewhere it says 5–6) against a real **2–3 yrs**, understating depreciation by **$176B 2026–2028**; **Oracle ~27%, Meta ~21%** overstated by 2028. **Sept 14, 2026 (Mon) selloff:** NVDA **>−3%**, AVGO **~−5%**, AMD **>−4%** after top lab CEOs called for slowing AI development (cites Reuters Sept 14/15). Counter-case: CoreWeave rebooked expiring H100 capacity at **~95%** of the original price. Huang: H100 rent **+22% in a month to $3.28/hr**. CoreWeave A100 contract runs **through 2029**. Meta extended some useful lives in 2025 and Amazon shortened others (10-Ks). |
| Grade | Burry figures **CONFIRMED but OLD**: the article itself cites MarketWatch **Nov 11, 2025**. Sept 14 selloff figures **RELAY-ONLY** (not checked against prices or Reuters). Nothing new to route. |
| Date traps | It presents a **Nov-2025 thesis** as the driver of a **Sept 2026** dip. The article does say "since late 2025", but the headline merges the two. |

---

## Adjacent items in the same Google News pull (NOT verified; discovery only)

| Item | Outlet / date | Claimed origin |
|---|---|---|
| Amazon moving **~$8B** of Nvidia (Grace Blackwell) GPUs into an investor-funded SPV, off-balance-sheet, up to 10% equity | Wccftech 10/2 | FT (not read) |
| Steve Eisman says Burry's depreciation thesis is "wrong" / "too academic" | Benzinga 10/6 | Eisman (podcast) |
| Nvidia adds a record **$150B** to its buyback (Mon Sept 28) | TNW / Finviz mentions | Nvidia (not read) |
| Bernstein: AI data-centre capex up to **$39.5B per GW**; depreciation "the biggest burden" | BigGo 10/10 | Bernstein (not read) |
| SpaceX bond with Nvidia-chip collateral "worth a fraction by mid-decade" | Tech Times 10/7 | unknown |

---

## WHAT IS ROUTABLE (only CONFIRMED, or RELAY clearly labelled)

| # | Fact | Source / date | Grade | Desk relevance |
|---|---|---|---|---|
| R1 | Lenders want **more guarantees** than Nvidia first offered on its **$500B** chip-collateral financing plan. Banks underwrite GPUs over **3–4 yrs** (Impax) against Nvidia's claim of up to **10 yrs**. Three bank sources say all deals may need a guarantee or IG offtake. **Tens of billions** of pipeline deals are likely to carry strong guarantees. | Reuters 2026-10-01 (full text via BNN Bloomberg) | CONFIRMED | VULCAN, BROCK |
| R2 | The underlying plan: Aug 10, 2026 **MOUs** (not final) with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to mobilise **>$500B of third-party capital over time**. Nvidia residual-value support **up to 25%** per opportunity. | Nvidia release 2026-08-10 (syndicated copy) + Reuters 10/1 | CONFIRMED | VULCAN, BROCK, SHADE |
| R3 | Credit precedents: CoreWeave **$8.5B**, the first IG GPU-backed loan, rated **A3** on Meta's contract. Broadcom backstopped **>80% of a $35B** Anthropic structure. Nvidia RVG on SB Energy Ohio (per S&P/Moody's). TCW: precedents show creditors "do not subscribe to long average lives". | Reuters 2026-10-01 | CONFIRMED | BROCK |
| R4 | Nvidia in **early, non-binding** talks with insurers to cover lenders on neocloud GPU-collateral loans if resale falls short of the debt. Works with **Howden Re**. Shared depreciation and compute-price data with ≥1 insurer. Explored syndicating risk to hedge funds. **No deals.** | **FT ~2026-09-28/29, RELAY-ONLY** (Investing.com/Finviz, TNW, Bisnow, Benzinga all consistent) | RELAY (label "FT-reported") | SHADE (primary), BROCK |
| R5 | Asian banks entering GPU lending: **~$3.8B** across GMI Cloud, Zankore and PaleBlueDot. Zankore **$3.1B** (Citi adviser; UOB among 5 banks); Zankore seeking a fresh **$6B** (UOB leading). Citi, JPM, Barclays, Deutsche, Santander and SMBC evaluating. **Nvidia agreed to buy unsold capacity** in the GMI and Zankore loans. Ares: GPU loans earn only **~100–200bp** more. | Bloomberg 2026-10-06 (full text via Business Times) | CONFIRMED | BROCK, VULCAN |
| R6 | Nvidia's public defence of useful life: ~**$60M/MW**; A100 in service 6 yrs; CoreWeave 2020-era units booked **to 2029**; MSFT V100 fleet **8.4 yrs vs 6-yr book**; Barkr H100 **5–6 yrs**, GB300 NVL72 **9–10 yrs**; Ornn A100 5-yr rent = **80%** of 1-month. | Nvidia Blog 2026-10-01 (primary; corporate claims, third-party data unverified) | CONFIRMED that Nvidia published it | VULCAN |
| R7 | Burry (2026-10-01) calls Nvidia's Sept 27 slide (A100/H100/B200 retained value vs a **5-yr** accelerated curve) a repeat of the **1968 computer-leasing mania**. | Burry Substack (primary, free portion) | CONFIRMED | VULCAN |
| R8 | Burry's paid-section argument: the slide is a **Silicon Data DCF over an ~8-yr modelled life, not resale prices**; strong legacy rents reflect memory and power **scarcity**, not durability; risk migrates to lenders and **private insurers**. | Stocktwits/Yahoo relay 2026-10-01. **The DCF/8-yr mechanism is CONFIRMED by Silicon Data's own methodology page.** | RELAY (mechanism corroborated) | VULCAN, BROCK, SHADE |
| R9 | Burry repositioned on **Sept 28, 2026** ("moving timelines up"; primary free line). Relay says he swapped stock shorts (MU, NBIS, CAT, SOXX, CRWV, NVDA, PLTR) for puts, NVDA **Sept-2027, mid-$100s strikes**. | Primary free line + Stocktwits relay | RELAY for the details; strike and expiry unverifiable | VULCAN (context only) |

**Do NOT route as stated:**
- Item 5's "$500B GPU loan": it is an MOU-stage capital-mobilisation target, not a loan.
- Item 5's OpenAI $10B: contested and off-topic.
- Item 8's "B200 resale value 158%": it is a DCF model output, not a resale price.
- Any **$176B / Oracle 27% / Meta 21%** Burry figure presented as new: those are from Nov 2025.
- Benzinga's "$105B Ohio guarantees" and Startup Fortune's "$125B" ceiling: unverified or derived arithmetic.

---

## URLs actually read (full visible text unless noted)
- https://michaeljburry.substack.com/p/dont-believe-your-lyin-eyes-gpu-depreciation (free preview only; paid)
- https://michaeljburry.substack.com/api/v1/archive?sort=new&limit=25 (post list/dates) + free previews via /api/v1/posts/ for trading-post-september-28-2026, the-heretics-guide-to-ais-stars-part-c9c, capital-cycle-iq-and-the-forensic, short-thoughts-a-wall-street-titan, trading-post-october-5-2026
- https://blogs.nvidia.com/blog/productive-durable-fungible-ai-factories/
- https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/01/nvidias-bet-that-its-chips-can-finance-the-ai-boom-gets-a-wall-street-reality-check/ (Reuters text; reuters.com returned 401)
- https://www.tradingview.com/news/tradingview:97d647c56ba00:0-key-facts-nvidia-500b-gpu-loan-10b-to-openai-burry-buys-2027-puts/
- https://www.tradingview.com/news/seekingalpha:e80aa8d85094b:0-michael-burry-likens-nvidia-s-ai-boom-to-1960s-computer-leasing-bubble/ (seekingalpha.com returned 403)
- https://stocktwits.com/news-articles/markets/equity/michael-burry-warns-nvidia-ai-infrastructure-expansion-mirroring-1960s-computer-leasing-bubble/cZD01nERB0L
- https://finance.yahoo.com/technology/ai/articles/michael-burry-warns-nvidia-ai-213700343.html
- https://finance.yahoo.com/markets/stocks/articles/michael-burry-just-pulled-1960s-180009562.html
- https://storagenewsletter.com/2026/08/12/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital/ (blackstone.com returned 403)
- https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital (date only: August 10, 2026)
- https://finance.yahoo.com/technology/ai/articles/nvidia-reportedly-turns-insurers-risk-023005996.html
- https://finviz.com/news/396264/nvidia-holds-talks-with-insurers-over-ai-infrastructure-financing-risk-ft-reports
- https://thenextweb.com/news/nvidia-insurers-ai-chip-loans-neoclouds-ft
- https://www.bisnow.com/news/national/data-center-capital-markets/nvidia-asks-insurers-to-shoulder-financing-risk-for-some-of-its-largest-customers
- https://startupfortune.com/nvidia-is-quietly-pushing-ai-data-center-risk-onto-insurance-companies/
- https://www.businesstimes.com.sg/companies-markets/banking-finance/banks-chase-risky-chip-loans-asias-us8-2-trillion-ai-buildout
- https://startupfortune.com/banks-push-deeper-into-risky-gpu-backed-loans-across-asias-ai-boom/
- https://tech-insider.org/nvidia-b200-58-percent-premium-gpu-loans-2026/
- https://tech-insider.org/nvidia-b200-residual-value-158-percent-2026/
- https://wccftech.com/nvidias-b200-gpus-currently-command-a-residual-value-that-exceeds-their-original-launch-price-by-58-percent/
- https://www.silicondata.com/products/gpu-residual-value
- https://www.valuethemarkets.com/analysis/gpu-depreciation-debate-behind-this-weeks-ai-dip
- https://www.newsquawk.com/headlines/nvidia-nvda-and-softbank-have-both-made-the-final-usd-10bln-investment-in-each-of-their-usd-30bln-pledges-to-openais-last-funding-round-the-information-reports-citing-sources
- https://cryptobriefing.com/softbank-closes-final-openai-tranche/
- https://wccftech.com/amazon-interested-in-moving-8-billion-of-gpus-off-its-books-as-report-suggests-wall-street-grows-wary-of-nvidias-500-billion-gpu-plan/
- https://www.intelligentcio.com/north-america/2026/08/11/nvidia-partners-with-global-investment-giants-to-mobilise-over-us500-billion-for-ai-infrastructure/ (date only)

**Not reachable:** ft.com (403), reuters.com (401), seekingalpha.com (403), blackstone.com (403), thestreet.com (403), equipmentfinancenews.com (403), axios.com (403), xenospectrum (403), Silicon Data's Sept 16 X post (not attempted; X), the Nvidia Sept 27 investor deck (not found).
