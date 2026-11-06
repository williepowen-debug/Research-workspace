# SoftBank's reduced OpenAI check, read beside card 003

**Date:** 2026-11-06 ET (Tokyo session 11/6; New York still open at writing). **Owner:** SAM. **Basis:** PROME C9 commission; BOARD SIG-W-20261106-030 and -003. **Class:** $0, no position, no gate, no prediction moved.
**Reproduce:** `python3 research/outputs/2026-11-06_softbank/ltv_remark.py`.

## Answer

**The check itself means nothing for Japan.** Hundreds of millions of dollars is about ¥48B–143B, or about +0.1 to +0.2 points of SoftBank's leverage ratio. It is not a broken commitment: SoftBank's own deck shows $55B funded of a planned $65B at 7/31, with the last $10B executed 10/1 (SoftBank notice). The new money is on top of that.

**The Japan consequence runs through the BOJ, not through SoftBank's credit.** The selloff took December hike pricing from 82% (10/29, before the decision) to 52% (11/6) and the yen weakened on a −6% day. A credit event at SoftBank is a real tail, but nothing read today shows it reaching a Japanese bank or household.

**One figure in circulation needs correcting.** The "13% leverage against a 25% limit" in card 030 is true only at 6/30, when Arm was $354.57. Arm is about $172. My re-mark is about **22% on SoftBank's own definition, about 24% if the loan it guarantees is counted**: the buffer is a good deal thinner than the quoted figure, but it is not gone. Full stack and cases: `SOFTBANK_FUNDING_STACK.md`, which governs.

## What the card's unchecked figures say at the primary

| Claim on card 030 | Primary reading | Source |
|---|---|---|
| About $65B invested | $55B funded at 7/31, $65B planned including October; ownership ~13% pro forma; fair value $100B | SVF deck Q1 FY26, slide "OpenAI: $55B Funded Out of Planned $65B Total" |
| Leverage 13% vs 25% limit | **13.0% at 6/30/2026 only**; 25% is SoftBank's own ceiling, not a covenant | Finance deck Q1 FY26 (L ¥10.81T / V ¥83.11T) |
| OpenAI carrying value | $89.6B at 6/30, cost $44.6B, "unchanged from the previous fiscal year-end". $110B / 13% ≈ $846B, which is the March round | Financial report Q1 FY26; SAM arithmetic |
| Debt added $40.4B | **Not checked.** The bridge is $40B committed; that may be the source, but I did not match it | Finance deck |
| Results "next week" | **Tue 11/10: tanshin 15:30 JST, briefing 16:30.** SoftBank Corp 11/9 | group.softbank/news/info/20261002 |
| Ratings | S&P BB+, Fitch BB+, JCR A at 9/11. Moody's is absent because SoftBank withdrew in 2020; Moody's keeps an unsolicited rating, which SoftBank disputes | group.softbank/ir/stock/rating; SoftBank notice 8/28 |

## Leverage re-mark (SAM estimate, not SoftBank's number)

Cases, inputs and limits moved to `SOFTBANK_FUNDING_STACK.md` § Leverage now, after the filing's loan terms changed the treatment. Summary: 22.1% on SoftBank's definition, 24.2% counting the guaranteed SVF2 loan, 25% at Arm about $128 and $160 respectively. ⚠️ An estimate: SVF and Others held at 6/30 apart from FX, monetizations since unknown. Script: `ltv_remark.py`.

**The valuation matters about 25 times more than the check** (cases in the funding stack). $0.5B of new money is +0.11 points. Booking the holding at $1.25T instead of about $852B is +¥8.1T of value and −2.8 points. So the same report can show SoftBank barely funding the round and being helped by its price. ⚠️ The round has not closed, its terms are anonymous, pre- or post-money is unstated, and VULCAN owns the terms.

## Carry grade (card 003 ACTION)

**NOT a Japan-led carry unwind.** The yen did not behave like one.

| Test | Reading | Result |
|---|---|---|
| Direction during the shock | Tokyo cash hours 11/6, 00:00–06:30Z: USD/JPY 157.48 → 158.14, range 0.75 yen. The yen **weakened** through a −5.96% session | Fails the unwind shape |
| Speed bar (≥1.5–2%/day or 2–3 yen in 1–2 sessions) | 11/5 completed 157.492, −0.56%, range 1.254. 11/6 live 158.5, +0.64%, range so far 1.241, **not a completed session**. Two-session span 1.40 yen | No fire |
| Positioning | CFTC net **long** yen +102,321 at 11/3 (Δ +730): no short-yen pool. ⚠️ The window ended before the selloff, so this is positioning going in | Fuel absent going in |
| Crosses | AUD/JPY −1.6% on 11/5 and −0.3% live, but AUD/USD −1.1% and −0.9%: mostly AUD weakness against everything. EUR/JPY −0.6% and −0.2%. Hourly vendor bars, not a synchronized study | Risk-off, not yen-led |
| Rates | 2Y −13.5bp, 5Y −16.5bp, 10Y −14.5bp, 20Y −8.5bp, 30Y −4bp (Reuters 11/6, on-the-run, intraday). Led by the front end, so a BOJ repricing, not a rush to the long end | Policy repricing |
| Banks | MUFG −6.52%, SMFG −5.73%, Mizuho −7.00% vs TOPIX −5.90%. In line with the market, and lower yields hurt banks anyway | No bank-specific break |

⚠️ **Not measured:** offshore yen funding. No basis instrument exists on this desk. This grade rests on spot and positioning and cannot exclude offshore strain.

⛔ The bond-futures halt stays unverified: Fisco's 11/6 close shows 127.59–128.41, all above the implied prior close, and mentions no halt.

## What it means for Japan, in order of importance

| # | Channel | Reading | Direction |
|---|---|---|---|
| 1 | **BOJ December** | Totan December incremental equivalent 82 → **52**; cumulative hikes to April 1.94 → **1.38**. Reuters' separate read: 42% hike. Mizuho's Matsuo: turmoil makes hikes harder. ⚠️ No reviewed chart sits between 10/29 and 11/6, so this is not all one day's move. These are model-dependent equivalents, not probabilities | Market stress lowers BOJ odds; live |
| 2 | **Yen / MOF** | Fed December hike odds about 77–79% after payrolls (card 017) while BOJ odds fall: both legs push the yen weaker. 158.5 is 1.5 yen from 160. The desk's working view is that MOF reacts to speed, not level | Risk is weaker yen, not stronger |
| 3 | **Long end** | 30Y fell only 4bp; Reuters cites Brent. The selloff did not lift the inflation premium off the long end | 11/10 30Y auction is the test |
| 4 | **Banks** | The $40B bridge was repaid 9/15 and cancelled 9/30, so that wall is gone. Mizuho and SMBC are on the $10B guaranteed OpenAI loan. Per-bank exposure undisclosed. No statement found | Unknown until 11/10 |
| 5 | **Households** | Senior retail bonds about ¥2.9T at 6/30 (primary) plus the reported ¥1T September issue at 4.75% (⚠️ secondary) ≈ ¥3.9T: 0.16% of household financial assets, but about 39% of the ¥10T households hold in corporate bonds at 3/31, on SoftBank's own chart. No large yen senior maturity before Dec-2029 (¥385B); subordinated ¥480B falls due Sep-2028 and ¥549B Feb-2029. Bond redemptions next two years ¥1.5T against ¥2.3T cash at 6/30 | A paper-loss and confidence channel, not a redemption run |
| 6 | **Funding access** | CDS 466bp high (Reuters via relay, unread here; was 432 on 10/20, Bloomberg). The channel to watch is whether the next yen retail deal clears and at what coupon | Not tested yet |

**Correction to my own June file:** `SOFTBANK_OPENAI_RISK.md` called this "spot-yen-bullish". On the first real test the yen weakened. The "hands the BOJ cover to pause" half held. This fits the desk's existing evidence that the yen is not behaving as a haven, but one day is not a regime.

**Not read:** SoftBank's motive. The small check could mean a stretched balance sheet, a concentration limit or a choice, and the sourcing is anonymous. Also not read: the NYT piece in full, the Reuters CDS piece (403), SoftBank's retail bond secondary prices, per-bank exposure, the share of Arm pledged.

## What would change this read

| Date | Fact | Why |
|---|---|---|
| Tue 11/10 15:30 JST | SoftBank results | ⚠️ **The headline LTV will be at 9/30, with Arm $289.66 and before the October $10B: my estimate is about 14–17%, some 7 points kinder than today.** Read any pro forma line. Full read list: funding stack §6 |
| Tue 11/10 | Summary of Opinions | Written about 10/29–30, before the selloff, so it will read hawkish against the new pricing. Not a reaction |
| Tue 11/10 | 30Y auction, frozen bars | Long-end demand after a rally of only 4bp |
| Open | Arm near $128–160 | My 25% zone, assuming OpenAI stays at the March mark |
| Open | S&P or JCR action | JCR A is the rating Japanese retail buyers see |
| Open | Next yen retail deal | Whether the household window stays open |

**Thesis:** v1.7 unchanged, retired-to-LOW, no successor, no entry. SAM-33 unaffected: yields fell. Ueda's 11/6 IMF text (`ko261107a1.pdf`) is about the current account and does not discuss policy or markets; any Q&A was not read.

Sources: [SoftBank results notice](https://group.softbank/news/info/20261002) · [SoftBank bonds](https://group.softbank/ir/stock/bond) · [SoftBank ratings](https://group.softbank/en/ir/stock/rating) · Q1 FY26 finance deck, SVF deck and financial report at group.softbank/media/Project/sbg/sbg/pdf/ir/ · [Reuters via Zawya](https://www.zawya.com/en/capital-markets/china-and-asia-pacific/japan-bond-yields-hit-multi-month-lows-as-tech-rout-spurs-flight-to-safety-2045007) · [Fisco via Zaikei](https://www.zaikei.co.jp/article/20261106/876469.html) · [Bloomberg via The Edge, 10/20](https://theedgemalaysia.com/node/822480) · [BOJ speech index](https://www.boj.or.jp/en/about/press/koen_2026/index.htm) · Totan meeting OIS 11/6 15:15 JST, SHA 802f8a6c.
