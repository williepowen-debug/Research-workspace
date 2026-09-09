# USO holding and short-interest review — September 9, 2026

**PROME assessment:** substantial reported short interest and a high indicated borrow fee deserve attention. Neither establishes that oil must fall or that USO must squeeze. The existing oil thesis still has support from this morning's futures curve; the more immediate portfolio issue is concentrated exposure and how much profit the existing call rule permits giving back. This review does not activate a new exit, add or roll.

## Position and forward risk

The user-supplied screenshot has no visible capture timestamp. Its values are the basis for account arithmetic, not executable quotes. [Reconciled source](../2026-09-09-position-review/snapshot.csv).

| Holding | Screenshot value | Open gain |
|---|---:|---:|
| USO shares ×37 | $5,499.21 | $974.94 |
| October 16 $135 call ×1 | $1,680.00 | $969.34 |
| Combined | **$7,179.21 / 18.64% of account** | **$1,944.28** |

BRENT's independently running session has now captured the [Cboe delayed chain](https://cdn.cboe.com/api/global/delayed_quotes/options/USO.json), retrieved at 14:26:55 UTC. [Retained extract and provenance](quote-extract.json): $135 call **$16.40 bid / $17.05 ask**, delta **0.7729**, IV **44.54%**, theta **−0.0835 per option unit/day**. Underlying last trade $148.54 at 10:11:06; option last trade 10:06:13. Those trade times are not quote timestamps. The endpoint is delayed; it cannot certify a current Fidelity fill. A separate chain wrapper agrees on bid/ask but is not an independent market observation.

**INFERRED from those Greeks:** the call adds approximately 77.29 shares of local price sensitivity, so the combination behaves like about **114.29 shares for a small underlying move**, all else equal. The call contributes most of that sensitivity. Indicative time decay is about **$8.35/day** and sensitivity to one volatility percentage point about **$14.26/contract**. These change with price, time and volatility; do not extrapolate them linearly through a crash or to October.

At the screenshot's $148.6275 underlying and $16.80 call mark, $1,362.75 of the call is intrinsic and $317.25 is time value. Most value is exposed to oil direction, although time/volatility still matter. The remaining economic value at risk is roughly $1,680, regardless of the original $710.66 basis. The first call's sale price remains permanently UNKNOWN under WQ-167; no basis-recovery claim or re-ask.

## Is USO heavily shorted?

| Evidence | Finding | Qualification |
|---|---|---|
| [Benzinga short-interest table](https://www.benzinga.com/quote/USO/short-interest) | **9,967,247 shares**, August 14 settlement / August 25 publication; July 31 was 14,054,826 | Reported count fell **29.08%**. Vendor copy, not a direct FINRA security-row download. |
| [MarketBeat](https://www.marketbeat.com/stocks/NYSEARCA/USO/short-interest/) and [ChartExchange](https://chartexchange.com/symbol/nyse-uso/short-interest/) | Same share count; percentages **63.81% versus 70.57%** | Their share denominators disagree. Do not certify one exact float percentage; these may share upstream data. |
| Benzinga's matched August 14 volume denominator | 5,624,548 average shares/day → **1.77 days to cover** | Volume ratio, not a deadline or assurance that all shorts can cover without moving price. MarketBeat's overview mixes a different volume figure with its 1.8 ratio; that explanation is not used. |
| [ChartExchange borrow feed](https://chartexchange.com/symbol/nyse-uso/borrow-fee/) | **37.42% indicated fee; 250,000 shares available at 08:52:40 EDT September 9** | Vendor attributes feed to IBKR; single broker, not market-wide. Not independently authenticated in IBKR. Earlier search snapshot showed zero at 07:34; the later opened page supersedes that inventory snapshot. |
| [FINRA publication calendar](https://www.finra.org/filing-reporting/regulatory-filing-systems/short-interest) | August 31 positions scheduled for publication **September 10** | August 14 is the latest scheduled public cycle today. The next report will still lag today's positioning. |

**VERIFIED** means these pages contain the reported observations, not that PROME audited their upstream loan books. The high borrow indication suggests borrow pressure at that broker; it does not establish a market-wide shortage, forced covering or who is short. The quoted fee is an annualized borrowing rate, not a daily percentage. [IBKR's own explanation](https://www.interactivebrokers.com/en/trading/short-securities-availability.php) describes availability and rates as indicative; [its cost documentation](https://www.interactivebrokers.com/en/pricing/short-sale-cost.php) explains supply/demand effects and account-dependent charges. We have not established that all USO shorts pay this rate.

**Interpretation:** bearish oil bets are one possible source of shorts. Hedging and arbitrage are others; the aggregate count does not reveal the mix. Also, a headline about daily short-sale volume is a different claim: transactions can be closed the same day and create no outstanding short position. FINRA explains this distinction in its [short-volume notice](https://www.finra.org/rules-guidance/notices/information-notice-051019). Will's original article/link was requested optionally and has not been provided at writing.

USO holds oil derivatives and collateral, rather than barrels of oil. Authorized participants can create/redeem 100,000-share baskets, which normally supports arbitrage between fund shares and asset value. **Inference:** this makes a fixed-share-supply stock-squeeze analogy incomplete. Creation can be constrained or suspended, so it is not proof that a squeeze is impossible. [April 24, 2026 prospectus](https://www.sec.gov/Archives/edgar/data/1327068/000207187626000128/i26211_uso-424b3.htm).

**UNKNOWN:** current matched-time premium/discount to NAV, matched-date shares outstanding, today's actual creation/redemption activity, any current creation restriction, and the identities/hedges of shorts. The [issuer page](https://www.uscfinvestments.com/uso) exposed the relevant labels but no populated current NAV/share figures in the retrieved text. Do not compare today's price with yesterday's NAV to manufacture a premium. A squeeze interpretation needs these inputs alongside borrow evidence.

## Oil case and existing management

[BRENT's 09:58 capture](../../../AGENTS/BRENT/research/2026-09-09_morning/REPORT.md) shows October WTI $95.79 and November $92.53 at the same 09:48:57 timestamp. Near delivery trades above later delivery. Its indicative November–January Brent spread widened to $7.54 from $6.62 at prior vendor closes, with timestamp skew disclosed by BRENT. This supports demand for near-term supply-risk exposure. It does **not** independently establish new lost production or a lasting price floor. A de-escalation, restored supply or weaker demand could reverse the premium. USO's futures holdings and roll matter to fund returns; rising spot oil alone does not specify the return path.

The [adopted remaining-call terms](../../../AGENTS/TERRY/setups/USO-135C_rule20-management_2026-09-01.md) remain:

- Official regular-session USO close **below $135** → sell the remaining call at the next open.
- Sell before the close **October 9**, regardless of P/L; **no roll**.
- The old $14.25 first-sale target is already a completed leg, not a second-call target. September 8 vendor close $146.03 was above $135; today's intraday prices cannot grade today's closing rule.

**The weakness is profit protection:** $135 is about **9.17% below** the screenshot price. A return there gives back about **$504 on the shares alone**, and erases the call's current intrinsic value; whatever time value remains depends on when and how it happens. A next-open exit also bears gap risk. This fixed call rule is not a trailing profit floor and does not apply to the shares.

The [shares exit scaffold](../../../AGENTS/TERRY/setups/USO-SHARES_named-exit-condition_2026-08-23.md) still lacks ratified numerical terms and uses an old 35-share title. The broker image establishes 37. Completing that already-commissioned management work is the actionable gap; PROME does not invent a trailing percentage in this review. The call has an approved plan, but retaining it entails accepting substantial gain giveback. Short interest alone is insufficient evidence to replace those terms or increase the position.

## Near-term decision checks

1. **Today:** compare the September EIA outlook with the prior demand, supply and inventory forecasts. [Release schedule](https://www.eia.gov/outlooks/steo/release_schedule.php): noon–12:15 EDT; still ahead at this review.
2. **Tomorrow:** read August 31 USO short interest, then the holiday-delayed [EIA weekly petroleum report](https://www.eia.gov/petroleum/supply/weekly/) at noon EDT. Look at inventories, production, refinery runs and product demand together; an inventory headline alone can reflect trade flows.
3. **To establish a fund-specific squeeze:** reconcile current NAV premium, actual share creations and availability/rates across brokers. A high single-broker fee alone cannot answer this.

[Arithmetic script](analyze.py) and [results](summary.json) reproduce holdings, sensitivities and short-count change. Validation checks positive/noncrossed quoted bid/ask, contract identity, delta bounds and cent-level snapshot totals. No new trade, execution receipt, broker mirror rewrite, monitoring automation or outbound message was created. BRENT's working artifacts were read and left untouched; this report preserves its own quote extract for continuity.
