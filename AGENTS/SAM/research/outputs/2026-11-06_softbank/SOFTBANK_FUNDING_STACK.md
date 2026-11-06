# SoftBank's funding stack, and whether it joins Oracle in one loop

**Date:** 2026-11-06 ET. **Owner:** SAM. **Basis:** PROME packet on Will's word, 15:40 ET, WQ-643. **Class:** $0. **No score, band or gate moved; SAM's own letter requires none.**
**Tags:** FILING = SoftBank or SEC document read here. RELAY = press, not checked against a filing. INFERENCE = SAM. **Reproduce:** `python3 ltv_remark.py`.

## Answer

**SoftBank's funding is odd in shape, not failing.** It refinanced aggressively in September at record size and removed its nearest wall, the $40B bridge, six months early. The odd part is that nearly all of it rests on two prices, Arm and OpenAI, and both collateral values were set before Arm fell by half.

**The premise needs one correction: the $40B bridge is gone.** Repaid 9/15, the undrawn $10B cancelled 9/30 (FILING). The nearest large maturity is now the Arm margin loan, about $25B, in September 2027 (RELAY).

**Leverage is about 22% on SoftBank's own definition, about 24% if the loan it guarantees is counted, against its 25% ceiling** (INFERENCE). This updates my earlier 21.5%.

**Loop answer: SoftBank and Oracle share a counterparty, OpenAI, not a financing link.** I found no SoftBank–Oracle credit tie. Oracle and Stargate each appear zero times in the text layer of five SoftBank documents; slide images were not read. It is one correlated exposure to OpenAI's ability to pay and to its valuation, on separate balance sheets. Microsoft is not something I read.

## 1. The stack at 11/6

| Item | Amount | Maturity | Collateral / recourse | Lenders | Tag |
|---|---|---|---|---|---|
| **2026 bridge** | $40B committed, $30B drawn | Was 3/2027. **Repaid: $25.9B prepaid 9/15, $10B cancelled 9/30; nothing outstanding** | Unsecured | JPM, GS, Mizuho, SMBC, MUFG; 30+ institutions | FILING; lead names RELAY |
| **SVF2 OpenAI loan** (borrower SVF II TSUBAKI) | $10.0B | **Aug 2028** | The filing calls it a loan "using its OpenAI shares" but lists only a **cash collateral account** as collateral. **Guarantor: SoftBank Group.** Cash collateral and mandatory prepayment triggered by a significant fall in the fair value of the referenced OpenAI preferred shares | MLAs: Goldman, JPMorgan, Mizuho Securities, Apollo, SMBC | FILING. Drawdown "expected during August", not confirmed drawn |
| **Two-year facility** | $11.87B | About Sept 2028 | **Undisclosed.** ⚠️ "OpenAI-share facility" is unproven: Bloomberg says only "to support its investment" and lists it as additional to the $10B | About 20 banks | RELAY, anonymous |
| **Apollo loan** | $5.4B, talks to raise to $9B | Unknown | Unknown | Apollo | RELAY, 9/18; outcome unknown |
| **Arm margin loan** | ¥3,221.0B drawn 6/30; facility upsized $20B → **$25B** in September | **Sept 2027** | Arm shares; non-recourse. 769M shares pledged as of May, 83% of the 923M held | 41 institutions at $20B | Drawn amount, non-recourse, count FILING; $25B, date, shares RELAY |
| **SoftBank Corp margin loan** | ¥1,197.0B; $7.4B facility | Not read | SoftBank Corp shares; non-recourse | 26 institutions | FILING |
| **T-Mobile collars** | ¥265.6B | Not read | T-Mobile shares; non-recourse | Not read | FILING |
| **SB Northstar prime** | ¥684.9B | Rolling | Securities; non-recourse | Not read | FILING |
| **Commitment line** | $6.0B → $6.5B; ¥489.5B undrawn at 6/30 | Not read | Unsecured | 25 institutions at $6.0B | FILING; $6.5B RELAY |
| **Parent bonds and CP at 6/30** | ¥9.13T (CP ¥233.8B) | Laddered to 2036, hybrids to 2065 | Unsecured | Retail and institutions | FILING |
| **Added since 6/30** | ¥1T retail 70th bond, 4.75%, 9/2033 · ¥90B domestic straight, August · $1B 8.625% 2030 · $4.5B 9.25% 2032 · $4.5B 9.75% 2034 · €500M 7.125% 2030 · €500M 8.00% 2032 | As listed | Unsecured; ratings BB+ / BB+, JCR A | Retail "mainly individual investors" | FILING |
| **Redeemed since 6/30** | ¥497.9B September domestic · €405.1M due 1/2027, redeemed early 10/22 | Done | | | FILING; the ¥497.9B is the 6/30 table's two September rows |
| **ABB LBO financing** | $1.75B equivalent | Not read | Filing's note on this line reads non-recourse | Not read | FILING. ⚠️ Deal now uncertain, see §3 |
| **SB Energy project debt** | About $4.0B, 6/30 | Various, some 3/2027 | Generally non-recourse to SB Energy | Project lenders | FILING (S-1, 9/1) |

**Inference on how the bridge was cleared:** the $10B SVF2 loan and the $11.87B facility fit the size of the 9/15 prepayment, the rest from cash; the ¥1T bond settled 9/17, two days later. SoftBank has not published the sources. The final OpenAI tranche was paid from the September dollar and euro notes (FILING).

## 2. Today's unchecked claims

| Claim | Verdict | Basis |
|---|---|---|
| OpenAI $64B | ✅ **Holds.** $64.6B cumulative, about 13%, third tranche executed 10/1 | FILING, 10/1 |
| LTV 13% against 25% | ⚠️ **True only at 6/30.** 25% is its own ceiling, not a covenant | FILING; see below |
| Debt added $40.4B | ❌ **Not confirmed.** No document I read prints it. Nearest: Bloomberg's "about $37B" raised this year to 9/14, gross of refinancing | RELAY. Do not carry |
| Bridge due 3/2027 | ❌ **Overtaken.** Repaid | FILING, 9/9 and 10/1 |
| China prohibited the $5.4B ABB deal | ⚠️ **Overstated on card 003 and in my KB.** SoftBank: China prohibited the acquisition "of ABB's robotics business in China". Both parties "working constructively" | FILING, 11/6 |
| Moody's | SoftBank withdrew its request in March 2020. Moody's keeps an unsolicited rating, which SoftBank protested again 8/28. That is why it is absent from SoftBank's list | FILING, 8/28 |

### Leverage now (INFERENCE on FILING inputs)

SoftBank's "SBG stand-alone" excludes "self-financing entities", and the filing lists SVF2 among them. So the guaranteed loan probably stays outside the reported ratio. **That is the point: the recourse reaches the parent even if the ratio does not show it.** Both views are below, with DigitalBridge's $3.1B included (closed 9/30, FILING).

| View at Arm $172, USD/JPY 158.5 | Today | 9/30 headline estimate | Arm price for 25% | OpenAI at $1.25T |
|---|---:|---:|---:|---:|
| **A. SoftBank's definition** | **22.1%** | 15.2% | $128 | 19.4% |
| B. A, plus Arm loan $5B extra drawn | 21.1% | 14.3% | $111 | 18.4% |
| **C. Guaranteed loan counted** | **24.2%** | 17.0% | $160 | 21.3% |
| D. C, plus Arm loan $5B extra drawn | 23.2% | 16.1% | $144 | 20.4% |

Second route from the 3/31 base gives 21.7%. Sensitivities on A: 19.5% if the $11.87B also sits outside the ratio; 22.9% if ABB closes in full. ⚠️ SVF and Others are held at 6/30 apart from FX, and listed holdings inside have probably fallen. Monetizations since 6/30 are unknown. **Arm at $160 is 7% below today's price**, on view C.

## 3. What is unusual, and what is ordinary for SoftBank

| Ordinary for SoftBank | Unusual |
|---|---|
| Bridge first, term out later: done in 2025 too | **The OpenAI loan needed a parent guarantee.** Reuters said in July that banks refused a shares-only structure. Filing confirms SoftBank Group as guarantor |
| Arm margin loan upsized a third time | **A valuation trigger on an unlisted share.** A significant fall in OpenAI's fair value forces cash collateral or prepayment. There is no market price, so the mark is the trigger; the threshold is undisclosed |
| High-coupon retail bonds, sold out | **OpenAI sits in SoftBank twice, and SoftBank is its landlord.** See §4 |
| Self-imposed 25% ceiling | **Arm is pledged about 83%, and its loan matures first.** Facility raised to $25B on 9/18; Arm was $289.66 on 9/30 and is about $172. Cover on May's pledged shares falls to about 5.3× on a full $25B (INFERENCE). Trigger undisclosed |
| Fight with Moody's since 2020 | **Two-tier cost of money:** 4.75% from Japanese households on 7 years, 9.75% from dollar junk buyers on 7.5 years, on the same credit (FILING). The household window is much the cheaper one |
| | **Timing:** almost all of it was raised in August and September, before Arm's fall from $290 to about $172. Nothing read shows lenders asked to re-paper |

**On the reduced check:** it is consistent with a stretched balance sheet, but nothing here proves that. With leverage near the ceiling and the OpenAI loan's fair-value trigger, SoftBank's interest is a higher OpenAI mark, not a bigger check (INFERENCE).

## 4. Ties to Oracle and OpenAI

| Link | Reading | Tag |
|---|---|---|
| SoftBank → OpenAI equity | $64.6B, about 13%, carried $100B at 7/31 on a flat mark | FILING |
| SB Energy → OpenAI, Milam County, Texas | 753 MW, two buildings, 15-year leases. No SB Energy document says "Stargate"; OpenAI's January announcement does | FILING; Stargate label RELAY |
| SB Energy → OpenAI, PORTS-Pike, Ohio | 8.0 GW, 17 leases, 20 years, signed 8/17/2026; not yet under construction. A substantial majority of backlog. S-1: "substantially dependent on OpenAI" | FILING |
| **Who guarantees those leases** | **NVIDIA, not SoftBank**: residual value guaranty up to $105B on the first 4.25 GW. The other 3.78 GW is NVIDIA's option; otherwise OpenAI must find an A- replacement guarantor | FILING |
| SoftBank's own guarantee | SoftBank Group Capital guarantees **its own affiliate's** Cosmos lease (Austin, about 50 MW): exposure about $2.9B | FILING |
| Size | Backlog about $439B, of which $430B data centers; backlog capex about $178B; project debt about $4.0B. PORTS alone may need over $6B of credit support, possibly letters of credit | FILING |
| OpenAI → SB Energy | 3,991,809 warrants at $0.01; OpenAI is also an equity investor. Warrant remeasurement cost $2.57B in H1 | FILING |
| SB Energy IPO | S-1 9/1, amended 9/21; no later filing on EDGAR at 11/6. S-1 warns SoftBank may pledge SB Energy shares, with prepayment if the price falls | FILING. I read the 9/1 text, not the 9/21 changes |
| **Oracle** | **In the S-1 only as a competitor.** Zero mentions in the text of SoftBank's Q1 filing and four decks. Press has Oracle financing three other Stargate sites (2025, RELAY). PROME's 10/22 reader J found no SoftBank-to-Oracle stake | FILING; RELAY |

**So what:** the circle is real but it is SoftBank–OpenAI–NVIDIA, not SoftBank–Oracle. SoftBank funds OpenAI, OpenAI rents from SoftBank's subsidiary, and NVIDIA backstops the rent. If OpenAI cannot pay, SoftBank loses on the stake, on the subsidiary and possibly through the loan guarantee at the same time. Oracle would be hit by the same event separately. ⚠️ SoftBank guarantees its own OpenAI-linked loan. It does not, on anything I found, guarantee OpenAI's rent.

## 5. Who lends, especially Japanese banks

| Lender | Where seen | Tag |
|---|---|---|
| **Mizuho** | Bridge lead (repaid); SVF2 MLA via Mizuho Securities USA; 70th bond underwriter; SB Energy IPO bookrunner; earlier $15B bridge $1.35B | FILING for SVF2, bond and IPO; else RELAY |
| **SMBC** | Bridge lead (repaid); SVF2 MLA; SMBC Nikko underwrote the 70th bond; earlier bridge $1.25B | FILING for SVF2 and bond; else RELAY |
| **MUFG** | Bridge lead (repaid). **Not among the SVF2 MLAs** | FILING for SVF2; else RELAY |
| **Non-Japanese** | Goldman, JPMorgan, Apollo on SVF2; JPMorgan $1B on the earlier bridge | FILING; RELAY |
| **Japanese households** | Senior retail about ¥3.9T including the ¥1T 70th bond | FILING |

⚠️ **Per-bank exposure today is undisclosed.** The only sized shares I found are on the repaid 2025 bridge, about 9% each for Mizuho and SMBC. Repaying the bridge moved some risk from banks to bond buyers and households, a real shift in who holds this. How much depends on the undisclosed terms of the $11.87B (INFERENCE). Mizuho carries the most relationships, and it fell the most of the three on 11/6, −7.00%, though that alone proves nothing.

## 6. Exactly what to read at 11/10, 15:30 JST (01:30 ET)

| # | Read | Why |
|---|---|---|
| 1 | LTV at 9/30 **and any pro forma** | ⛔ Headline estimate 14–17% is at Arm $289.66, before the October tranche, not today's level |
| 2 | **Whether the SVF2 loan is inside SBG stand-alone debt** | Decides view A vs C, about 2 points |
| 3 | SVF2 loan drawn, and the fair value of the referenced OpenAI shares | The covenant's input |
| 4 | **OpenAI mark at 9/30** | Flat at $852B or moved; about 2.8 points if booked at $1.25T |
| 5 | Arm margin loan: drawn amount, pledged shares, maturity, any add-on | The nearest wall |
| 6 | The $11.87B and Apollo loans: borrower, collateral, recourse | Both undisclosed. If outside the ratio, A falls toward 19.5% |
| 7 | Cash position against next two years' redemptions | Was ¥2.3T vs ¥1.5T at 6/30 |
| 8 | **ABB:** closes, restructures or falls away; LBO financing; any cash | 11/6 notice is open-ended |
| 9 | Guarantees and commitments note | Any SoftBank support for SB Energy, Stargate sites or OpenAI |
| 10 | Any new word on the $1.25T round or SoftBank's share | Size and valuation; VULCAN owns terms |
| 11 | Gotō's language on LTV, the 25% ceiling and Arm sales | Whether 25% is defended by selling or by relabelling. A sale of Arm or OpenAI is the tell |

## Not read

The NYT piece in full; the Reuters CDS piece (403); margin-call levels (undisclosed); the 9/21 S-1 amendment; Microsoft; retail bond secondary prices. Terms of the $11.87B and Apollo loans rest on anonymous Bloomberg sourcing. **Card and position views go to TERRY; this read proposes none.**

Sources: SoftBank press [8/24](https://group.softbank/en/news/press/20260824), [8/28 Moody's](https://group.softbank/en/news/press/20260828_0), [9/2](https://group.softbank/en/news/press/20260902), [9/4](https://group.softbank/en/news/press/20260904), [9/9](https://group.softbank/en/news/press/20260909), [9/24](https://group.softbank/en/news/press/20260924), [9/30](https://group.softbank/en/news/press/20260930), [10/1](https://group.softbank/en/news/press/20261001), [10/9](https://group.softbank/en/news/press/20261009), [11/6](https://group.softbank/en/news/press/20261106) · Q1 FY26 financial report note 16(3), finance deck, SVF deck · [SB Energy S-1](https://www.sec.gov/Archives/edgar/data/2133037/000162828026059639/sbenergy-sx1.htm) · Bloomberg via The Edge [9/14](https://theedgemalaysia.com/node/817934), [9/18](https://theedgemalaysia.com/node/818515) · [Reuters via The Star, 7/2](https://www.thestar.com.my/tech/tech-news/2026/07/02/exclusive-softbank-renews-talks-for-10-billion-loan-against-openai-stake-adds-concessions-sources-say) · [SiliconANGLE, 9/2025](https://siliconangle.com/?p=712569) · `PROME/themes/ellison/` reader J via LIQUID packet 10/23.
