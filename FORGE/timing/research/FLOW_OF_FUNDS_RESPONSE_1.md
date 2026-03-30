Here’s the cleanest read I can get from the Fed’s quarterly Z.1 holder-flow data.

Using the **latest revised Z.1/FRED quarterly transaction series** for corporate and foreign bonds, the first sectors that **actually flipped from net buyer to net seller during the crisis window** were **foreign holders** and **money market funds in Q3 2007**. The next wave came **one quarter later, in Q4 2007**: **mutual funds, life insurers, P\&C insurers, broker-dealers, and banks**. **Private pensions** turned in **Q1 2008**, and **state/local pensions** did not flip until **Q3 2008**. **ETFs never went net negative** in this window. **Households** were already net sellers in **Q1–Q2 2007**, so they do not mark the crisis onset; they were negative before the institutional sequence began. ([FRED](https://fred.stlouisfed.org/data/ROWCBAQ027S.txt))

One important limitation: in the **current Z.1/FRED mapping**, I can build a clean holder table for the sectors you asked for **except ABS issuers**. The current series exposed for ABS on corporate/foreign bonds is a **liability** series, not a clean corporate-bond **asset-holder purchases/sales** series; and the old 2009 instrument table’s asset-holder section likewise does **not** list ABS issuers as a corporate-bond holder line. So I am not going to force a bad proxy into the table. ([FRED](https://fred.stlouisfed.org/series/BOGZ1FU673163005Q))

**Quarterly net purchases/sales of corporate bonds**  
**$ billions, seasonally adjusted annual rate, latest revised Z.1/FRED series**  
(except where noted)

| Sector | Q1 2007 | Q2 2007 | Q3 2007 | Q4 2007 | Q1 2008 | Q2 2008 | Q3 2008 | Q4 2008 | Source |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Households & nonprofits | \-481.5 | \-396.7 | 755.1 | 489.9 | \-137.1 | 87.5 | 491.1 | 601.3 | ([FRED](https://fred.stlouisfed.org/data/HNOCFAQ027S.txt?utm_source=chatgpt.com)) |
| Mutual funds | 83.6 | 100.0 | 169.1 | \-2.0 | 2.9 | 256.9 | \-93.1 | \-353.9 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA653063005Q.txt)) |
| ETFs | 3.6 | 6.9 | 5.2 | 9.1 | 12.0 | 14.5 | 10.7 | 18.3 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA563063003Q.txt)) |
| P\&C insurance | 15.2 | 32.6 | 14.5 | \-35.6 | \-19.6 | \-12.2 | 10.1 | \-34.8 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA513063005Q.txt)) |
| Life insurance | 66.8 | 56.5 | 61.3 | \-18.3 | 14.9 | 44.1 | \-31.3 | \-37.1 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA543063005Q.txt)) |
| Private pensions | 12.2 | 12.2 | 12.2 | 12.2 | \-47.1 | \-47.1 | \-47.1 | \-47.1 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA573063005Q.txt)) |
| State/local pensions (DB) | 102.2 | 159.1 | 15.7 | 236.4 | 12.7 | 90.2 | \-21.2 | \-156.5 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA223063045Q.txt)) |
| Banks\* | 67.1 | 33.7 | 211.5 | \-167.6 | \-46.7 | 60.8 | \-66.2 | 75.6 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA763063095Q.txt)) |
| Broker-dealers | 162.4 | 47.4 | 37.4 | \-115.4 | \-66.3 | \-334.1 | \-114.0 | \-255.5 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA663063005Q.txt)) |
| Money market funds | 103.1 | 165.4 | \-50.7 | \-154.6 | 87.5 | \-66.8 | \-389.0 | \-236.9 | ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA633063005Q.txt)) |
| Foreign sector | 721.8 | 713.4 | \-4.9 | 268.1 | \-3.9 | 273.0 | \-256.5 | \-100.0 | ([FRED](https://fred.stlouisfed.org/data/ROWCBAQ027S.txt)) |

\*For “banks,” the clean current quarterly Z.1 series is **U.S.-chartered depository institutions, including IBFs; corporate and foreign bonds, excluding private MBS and CMOs; asset, transactions**. That is the closest current quarterly match, but it is not identical to the older “commercial banking” label used in the 2009 release. All Z.1 series are revised over time. ([FRED](https://fred.stlouisfed.org/series/BOGZ1FA763063095Q))

**Precise flip sequence and lag**

Mechanically, the first negative line in the table is **households**, but that was already true in **Q1 2007**, before the crisis sequence you are trying to date. For the actual **buyer-to-seller flip**, the first movers were **foreign holders** and **money market funds** in **Q3 2007**. Among domestic non-household institutions, **MMFs were first**. ([FRED](https://fred.stlouisfed.org/data/HNOCFAQ027S.txt))

The **next cohort** flipped **one quarter later, in Q4 2007**: **mutual funds, P\&C insurers, life insurers, broker-dealers, and banks**. That means the lag from the first funding-sensitive sellers to the broader institutional sell wave was **one quarter**. ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA653063005Q.txt))

After that, **private pensions** turned negative in **Q1 2008**, another **one quarter later**. **State/local pensions** did not flip until **Q3 2008**, which is **two quarters after** the private-pension turn and **four quarters after** the first MMF/foreign flip. That is the real lagged institutional transmission. ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA573063005Q.txt))

So your rough sequence was **partly right**, but not quite. In the actual holder-flow data, the first broad stress signal is **not insurers** and not something you can directly label “hedge funds” from Z.1. It shows up first in **funding-sensitive holders**: **MMFs** and **foreign holders**. **Mutual funds and insurers** are **one quarter later**, and **pensions are late**. ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA633063005Q.txt))

**Was selling gradual or cliff-like?**

For the early sellers, it was mostly **cliff-like**, not smooth. **MMFs** went from **\+165.4** in Q2 2007 to **\-50.7** in Q3 and **\-154.6** in Q4, then hit **\-389.0** in Q3 2008\. **Broker-dealers** dropped from **\+37.4** in Q3 2007 to **\-115.4** in Q4 and **\-334.1** by Q2 2008\. That is a classic funding/intermediation snap, not a slow drift. ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA633063005Q.txt))

**Mutual funds** were more of a **late cliff** than an early cliff: still a strong buyer in **Q3 2007 (+169.1)**, barely negative in **Q4 2007 (-2.0)**, back slightly positive in **Q1 2008 (+2.9)**, then sharply negative in **H2 2008**. So the retail-fund complex did not lead the crisis in corporate-bond holdings; it cracked after the funding-sensitive layer. ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA653063005Q.txt))

**Insurers** look more like **hesitant retrenchers** than forced liquidators at first. Both **life** and **P\&C** turn negative in **Q4 2007**, but they bounce rather than dump in a straight line. **State/local pensions** are unmistakably the **late sellers**: still positive through **Q2 2008**, then negative in **Q3 2008** and sharply negative in **Q4 2008**. ([FRED](https://fred.stlouisfed.org/data/BOGZ1FA543063005Q.txt))

**How I’d map 2007 to 2026**

Your mapping is directionally right, but I would tighten it.

The 2007 “hedge funds/SIVs sold first” bucket maps **less to BDCs alone** and more to the **private-credit warehousing and funding stack**: subscription/NAV lenders, asset-based-lending warehouses, fund finance, semi-liquid interval funds/non-traded BDCs, and any bank/dealer financing lines against private-credit collateral. That is where 2026 stress is already visible: banks are tightening, Barclays is pulling back from smaller-borrower ABL, and public bonds issued by semi-liquid private-credit funds were already widening before the redemption wave. ([Reuters](https://www.reuters.com/business/finance/barclays-pulls-back-asset-based-lending-after-mfs-tricolor-collapse-bloomberg-2026-03-25/))

Your “2007 mutual funds → 2026 retail credit ETFs \+ BDC retail” mapping is **half right**, but the **closer analog is non-traded BDCs and interval/semi-liquid private-credit funds**, not HYG/JNK first. The 2026 action is happening in vehicles with redemption windows and valuation lag: Morgan Stanley, BlackRock, Apollo, and Ares all limited withdrawals after large tender requests, while Oaktree met an **8.5%** request only by using portfolio liquidity and sponsor support. That is much closer to the **fund-flow transmission channel** than liquid ETFs alone. ([Reuters](https://www.reuters.com/business/finance/private-credit-strains-ripple-through-wall-street-investors-grow-wary-2026-03-24/))

Your “2007 insurance → 2026 PE-controlled insurers” mapping is broadly right, but I would expand it to **PE-controlled insurers plus captive/offshore reinsurance channels**. The obvious large platforms are **Athene** and **Global Atlantic**; industry coverage also points to **Everlake** as another PE-linked insurer in the private-credit ecosystem. The systemic issue is not just who owns the insurer; it is the growing **interconnectedness between private credit, insurers, and banks**. ([Global Atlantic](https://www.globalatlantic.com/news/KKR-completes-acquisition-of-global-atlantic))

Your “2007 banks → 2026 banks with PC commitments” mapping is right, but the key is to think in terms of **credit lines, warehouses, funding agreements, marks, and unused commitments**, not just direct loan books. Moody’s said U.S. banks had almost **$300 billion** of loans outstanding to private-credit providers as of June 2025, plus **$340 billion** of unused commitments and **$285 billion** of loans to private-equity funds. That is the bank transmission rail. ([Reuters](https://www.reuters.com/business/finance/us-banks-surge-loans-private-creditors-may-pose-risks-moodys-says-2025-10-22/))

What you are missing is the **dealer/funding layer** between fund redemptions and ultimate asset sales. In 2007 that layer was ABCP/SIV funding and dealer balance sheets. In 2026 it is **warehouse/A BL/NAV/sub-line funding, private-credit fund bonds, and bank marks against private collateral**. That is why I would not reduce stage 1 to “BDCs.” ([Reuters](https://www.reuters.com/business/finance/barclays-pulls-back-asset-based-lending-after-mfs-tricolor-collapse-bloomberg-2026-03-25/))

**Where 2026 sits in the sequence**

As of **March 30, 2026**, I would place the market **around the Q4 2007 analog**, maybe **late Q3/early Q4 2007** if you want to be conservative. The reason: the **retail/semi-liquid fund layer is already under redemption stress**, and the **bank/dealer layer has begun retrenching**. Morgan Stanley, BlackRock, Apollo, and Ares have all imposed limits; Barclays has pulled back from smaller-borrower ABL; JPMorgan has marked down some loans to private-credit funds; and Treasury is now preparing regular consultations with insurance regulators. ([Reuters](https://www.reuters.com/business/finance/private-credit-strains-ripple-through-wall-street-investors-grow-wary-2026-03-24/))

What I do **not** see yet is evidence of the **late-stage pension seller** phase or of broad **forced insurer liquidation**. In fact, Powell said today that the Fed is watching private credit closely but does **not currently** see it as having the makings of a broader systemic event, even though regulators are looking for banking-system links and contagion channels. So this looks like **stage 2/3 with stage 4 beginning**, not the full 2008 endgame. ([Reuters](https://www.reuters.com/business/finance/fed-watching-private-credit-sector-signs-trouble-powell-says-2026-03-30/))

On your listed 2026 signals specifically: I **did verify** the fund gating, Barclays’ pullback, and Treasury’s insurance-regulator meetings. I also verified Goldman’s view that **retail investors are pulling money out** and that Goldman expects **net outflows to continue through 2026 and likely 2027**. I did **not** independently verify the exact **$45–70 billion** figure from an accessible primary source, so I would treat that number as unconfirmed unless you already have the note itself. ([Reuters](https://www.reuters.com/business/finance/private-credit-strains-ripple-through-wall-street-investors-grow-wary-2026-03-24/))

**Who is the 2026 “Meredith Whitney”?**

My read is: **there is not yet a single Meredith Whitney-style consensus-breaker**. In late October 2007, Whitney’s Citi call was a **specific, public, falsifiable break with consensus** on a core regulated bank. The current private-credit warning set is more **distributed**: rating agencies, hedge funds, ex-bank CEOs, and regulators are all raising related concerns, but no single sell-side call has yet become the market’s focal point. Meredith Whitney’s Oct. 31, 2007 Citi downgrade did in fact hit that role in real time. ([Reuters](https://www.reuters.com/article/world/cibc-analyst-got-death-threats-on-citigroup-report-idUSN04195378/))

If you force me to name the **closest current analog**, I would split it three ways. **Lloyd Blankfein** is the loudest public individual voice; he has warned that private markets look vulnerable and that “just a spark” could light private credit on fire. **Moody’s** is the most clearly **systemic** published research voice, because it tied private credit directly to banks’ loan and commitment exposures and said risks rise as interconnectivity grows. **Fourier Asset Management** has the cleanest **market-based early-warning note**, because it argued that semi-liquid private-credit fund bonds were signaling stress before the redemption headlines. ([MarketWatch](https://www.marketwatch.com/story/just-a-spark-may-light-private-credit-on-fire-warns-ex-goldman-ceo-blankfein-d3d236d5))

There are also other serious warning voices, but they are not quite Meredith Whitney equivalents. **Fitch** reported a record **9.2%** private-credit default rate for 2025\. **Partners Group chairman Steffen Meister** warned defaults could **double** over the next few years. And today’s official tone is still “watchful, not systemic”: Treasury is convening insurers, and Powell says the Fed is monitoring exposures, but not seeing a full-system event yet. That combination tells me the market is still in the **recognition phase**, not the “one-note breaks consensus and forces immediate institutional de-risking” phase. ([Reuters](https://www.reuters.com/business/us-private-credit-defaults-hit-record-92-2025-fitch-says-2026-03-06/))

My simplest bottom line:

**2007 sequence from the data:**  
**Q3 2007:** foreign \+ MMFs  
**Q4 2007:** mutual funds \+ insurers \+ dealers \+ banks  
**Q1 2008:** private pensions  
**Q3 2008:** state/local pensions  
**ETFs:** never sellers in the sample  
**Households:** already negative before the sequence started. ([FRED](https://fred.stlouisfed.org/data/ROWCBAQ027S.txt))

**2026 analog:**  
We look **past stage 1 and into stage 2/3**, with **retail/semi-liquid funds already under pressure** and **banks/dealers starting to retrench**, but **not yet** at the pension/forced-insurer endgame. Closest historical analog: **Q4 2007**, not late 2008\. ([Reuters](https://www.reuters.com/business/finance/private-credit-strains-ripple-through-wall-street-investors-grow-wary-2026-03-24/))

