# TRADE CARD — RSP January 215/225 bull-call spread — breadth confirmation
**Date:** 2026-11-02; reprices the 2026-10-20 card under D:L905 / WQ-574.
**Setup ID:** `IDEA-RSP-OCT20`
**Terry verdict:** CONDITIONAL — APPROVED NOT-FIRED (WQ-591 A, Will in PROME's chat 2026-11-04 20:59 ET, verbatim "approved with your recs"; record `PROME/proposals/2026-11-04_wq591-601-RULED.md`; GATE-TERRY-RSP-01). ×1 only, past closed X1 by his per-card choice. The order is Will's hand (root rule #5).
**Prepared:** 2026-11-02T09:54:21-05:00.
**Thesis owner:** HENRY, L616 breadth study dated 2026-10-31 on 10/30 closes, `AGENTS/HENRY/STATUS.md` § MARKET BREADTH.
**Confidence in structure:** Low at the observed markets. Recommendation: wait; do not pay the displayed debit.

> **TRIGGER STATE 2026-11-06 10:17 EST (TERRY): NOT ELIGIBLE WHILE GREEN.** RSP $217.15 +0.13% at 10:15, green; PROME told 10:15. Re-read on any red turn today. No fill known.

> **TRIGGER STATE 2026-11-06 10:11 EST (TERRY): ELIGIBLE AT THE MID ONLY, BROKER QUOTE DECIDES; order presented via PROME 10:07 EST, no order by the desk.** RSP $216.02 −0.39% at 10:07, red so far, above $215; then $216.57 −0.14% at 10:10. RSP/SPY 0.2925, above 0.280498. Chain 10:05 and 10:07 EST: 215C $5.60/$8.00, 225C $1.95/$2.40, mid $4.625, outer $6.05 vs ≤ $4.90; 215C last traded 11/5 15:47, quote $2.40 wide, two DIRINC rows; Cboe file was an overnight snapshot, no use. Tape narrowing: SPY up, QQQ about +2.2%, VIX −13.8% (HENRY: chips). HY 348 [11/5] changes no term and weakens the read. The first-qualifying-opportunity clause of § 4 applies only if the broker debit is ≤ $4.90 on a red day; a broker debit above it is no order.

> **TRIGGER STATE 2026-11-05 15:40 EST (TERRY, stamped 15:40 EST): NOT-FIRED, debit blocks; no entry.** RSP $216.85 −2.90%, red, above $215; ratio 0.2951 intraday. Chain 15:40 EST: 215C $7.80/$8.90 (DIRINC), 225C $2.50/$2.90, outer $6.40, mid $5.65, vs ≤ $4.90. The debit rose while RSP fell $0.35 from 13:33, so the rough sensitivity below (mid $4.90 near RSP $215.7) did not hold; do not rely on it. Screening marks, no broker quote; only a broker complex quote ≤ $4.90 changes this. Sent to PROME for Will's 15:39 ET question.

> **TRIGGER STATE 2026-11-05 13:33 EST (TERRY): NOT-FIRED, debit blocks; no entry.** RSP $217.20 −2.75%, red, above $215; ratio 0.2950 intraday. Chain: 215C $7.60/$9.00, 225C $2.75/$3.10, outer $6.25, mid $5.375, vs ≤ $4.90. Rough: mid reaches $4.90 near RSP $215.7, outer near $214.7, under the floor. Screening marks, no broker quote. New card `IDEA-RSP-DEC-NOV05` (WQ-616) does not change this card.

> **TRIGGER STATE 2026-11-05 11:10 EST (TERRY): NOT-FIRED, debit blocks.** Selloff: RSP $219.37 −1.78% (11:08 EST), red so far and above the $215 floor. Volatility rose with it: VIX $27.96. Chain 11:08 EST: 215C $9.50/$11.20, 225C $3.80/$4.80, outer $7.40 (×1 $741.30), leg mid $6.05, against ≤ $4.90. Screening marks, no broker quote. No close yet.

> **TRIGGER STATE 2026-11-05 earlier 09:50 EST (TERRY): NOT-FIRED, no entry.** RSP $222.80 −0.24% at 09:45 EST, red so far today, not a completed close. The debit test blocks entry whatever the colour: `chain_fetch.py` 09:46 EST, usable legs, 215C $11.30/$13.80, 225C $4.70/$5.40 (225C flagged NONMONO; both last traded 11/4; six-row DIRINC warning), outer debit $9.10 (×1 $911.30), leg mid $7.50, against the $4.90 cap. Screening marks, no broker quote. ⚠️ Rough read: the spread moves about $0.20 per $1 of RSP, so a $4.90 fill needs RSP near $210, below this card's own $215 floor. The approved card may simply not fill; that is a valid outcome, and the limit does not move.

## 0. Authority, freshness and hard caveats
| Item | Evidence and consequence |
|---|---|
| Revival only | Will, 10/31 14:23 ET: “574 approved your rec”; committed PROME packet `../inbox/processed/2026-10-31_from-PROME_WQ573-574-RULED.md`. RSP revived; VST stays shelved. This does not approve an order or a larger budget. |
| Live equity pull | `fetch.py price RSP SPY`, retrieved 2026-11-02 09:48:08 EST: RSP $220.04, +0.79%; SPY $760.22, +0.60%. Payload shows date only; retrieval time is not an exchange timestamp. |
| Required option tool | `chain_fetch.py RSP 2027-01-15 --type call --legs 215,225 --no-cache --json`, 09:48:20 and 09:51:02 EST: both named legs 0/0, DEAD; exit 2 on both pulls. These are missing quotes, not free options. |
| Primary fallback | Cboe delayed endpoint, retrieved 09:48:59 EST, payload timestamp `2026-11-02 14:48:04` (timezone not specified in payload). Underlying $219.80, last trade `09:32:58`; individual option bid/ask timestamps unavailable. Delayed screening data only, not a live executable quote. |
| Broker gaps | No broker connection: current complex bid/ask, fees, live Greeks, deliverables, orders and full position truth unverified. `[POSITION_STATE_UNKNOWN]`; do not assume this is an independent hedge for the book. |
| Budget / sizing gate | **$500 per card default. X1 CLOSED / DON'T-SIZE.** Proposed future size is at most ×1 at the stated limit; deployment now is ×0 / $0. A fill against X1, or a larger budget, requires Will's explicit per-card choice under root rule #5. |

Evidence files: `../research/2026-11-02_rsp-reprice/` (`live_prices.txt`, `chain_jan15.json`, `chain_jan15_retry.json`, `cboe_rsp.json`, `history_preopen.txt`, `NOTE.md`). No STATUS price is used.

## 1. One-line setup and thesis
Buy limited exposure to a broad US equity advance if equal-weight strength persists and a red-day entry becomes affordable. HENRY's October RSP/SPY **+5.91 percentage points** is a total-return ratio measure, not an RSP price target. Its 10/30 study found **60.2% / 59.2%** of S&P 500 members above their 50-/200-day averages, versus **20.9% / 40.4%** on 9/30. Friday's index fall was concentrated: **55.1%** of members fell and 26 mega-cap/chip names produced **79%** of the index decline. Sources: HENRY L616, 10/31, same section. This supports participation; it proves no positive option expectancy.

## 2. Trigger state and tape
| Test | Line / observation | Grade at this read |
|---|---|---|
| Completed breadth confirmation | Existing card: RSP close > $215.00 and paired price-close RSP/SPY > frozen 0.280497871. 10/30: $218.31 / $755.72 = 0.288877; prior 20-close maximum on that date = 0.286004. | Confirmation MET. Price-close ratio is distinct from HENRY's total-return study. |
| Revived entry opportunity | First red RSP session after the 10/31 revival, RSP ≥ $215, intact confirmation and broker complex debit ≤ $4.90. The old first-red 10/23 opportunity was spent; WQ-574 authorizes this fresh review, not a retroactive entry. | **NOT-FIRED:** Monday +0.79% at 09:48:08 EST. No qualifying fill observed. |
| Root rule #6 | Calls on red days. No direct same-basis measurement refutes the day-colour proxy. | Entry blocked at this observation; no exception proposed. |
| Quote / budget | Both Yahoo named quotes DEAD. Cboe outer-market debit $7.70; mid $6.20 is not executable. | Entry blocked independently of day colour. |
| Daily / weekly context | Prior session close $218.31; 60 completed bars to 10/30 span $208.02–$222.77. 10/30 ratio 0.288877 exceeded 10/29 0.286004. | Broadening with a pullback on Friday; today's green quote is a rebound, not a completed close. |

Source: retained 09:15:54 EST daily-bar calculation, 87 aligned bars 6/30–10/30; 60-bar range explicitly counted. Completed bars are unchanged by today's intraday quote. Do not resolve a closing trigger from unsynchronised intraday prices. Invalidation remains the original **$208.02 completed close**; no owner threshold was changed.

## 3. Fresh option screen — Jan-15-2027 expiry (74 calendar days from 11/02)
Cboe delayed snapshot as identified above; standard 100-share deliverable assumed, broker must confirm.

| Leg | Bid / ask | Width / mid | Open interest | Volume | IV / delta / theta per day |
|---|---:|---:|---:|---:|---:|
| Buy 215C | $8.90 / $10.40 | 15.54% | 1,052 | 0 | 16.11% / 0.6607 / −0.0380 |
| Sell 225C | $2.70 / $4.20 | 43.48% | 7,763 | 0 | 13.10% / 0.3922 / −0.0334 |

Last executed trades are **10/30**, $8.60 and $2.70; they are not current quotes. Cboe's two-sided fallback has no locked/crossed/dead/no-bid selected leg, but its delay does not cure the failed live-feed check. Long ask − short bid = **$7.70**; long bid − short ask = **$4.70**; leg-mid difference = **$6.20**. The $3.00 outer-market round trip is **48.39%** of that mid. The midpoint-to-limit improvement needed is **$1.30 / 20.97%**. Neither a $4.70 liquidation value nor a Friday last-trade difference is a purchase price.

Net model delta ≈ **26.85 shares** and theta ≈ **−$0.46/day per spread** at this delayed snapshot; these are model outputs, not broker Greeks or a decay guarantee. IV rank and a reliable expected move are unavailable. Sell the upside at 225 to reduce premium versus an outright call; the wings remain too wide for a firm entry recommendation.

## 4. Entry, size and loss — figures govern
| Basis, ×1 spread | Debit | Opening fee assumption | Maximum option loss | Terminal maximum profit, after opening fee | Terminal breakeven |
|---|---:|---:|---:|---:|---:|
| Cboe outer markets, NOT recommended | $7.70 | $1.30 | **$771.30** | $228.70 | $222.713 |
| Cboe leg mids, NOT a fill | $6.20 | $1.30 | $621.30 | $378.70 | $221.213 |
| Proposed future broker limit | **≤ $4.90** | $1.30 | **≤ $491.30** | $508.70 at the limit | $219.913 at the limit |

Default **1R = $250**, ceiling **2R = $500** (`STATUS.md` standing risk unit). At the outer screen even one spread exceeds the default by **$271.30**; permitted size there is **0**. The conditional limit fits **×1**, $491.30 = 1.9652R, leaving $8.70 under the default. **Actual proposed deployment now: ×0 / $0.** Fees assume $0.65 per contract per side; exact fees must fit the $500 ceiling. Profit figures exclude closing costs. Net terminal reward/risk is only **0.30:1** at the outer screen versus **1.04:1** at the limit; neither ratio proves edge.

Buy only as one broker complex spread under WQ-591 A, on a red RSP day with RSP ≥ $215 and debit ≤ $4.90. Do not chase a higher debit or replace the missing quote with a model. If the first qualifying opportunity is missed, return for rework; no automatic recurring order or new entry permission. A larger size/budget is Will's choice, never pre-approved by WQ-574.

## 5. Independence and alternatives
| Field | Assessment |
|---|---|
| N_claimed / N_eff | **1 / 1**: the single breadth view. Several participation statistics share the same equity rotation; they are not independent signals. |
| Shared falsifier | Broad US equities weaken and participation fails. Financials and energy are inside RSP; it is not insulated from the fleet's bank/oil theses. |
| Book interaction | Direction opposes bearish equity options, but a realised hedge ratio and current combined exposure are UNKNOWN. Do not size from a claimed hedge benefit. VST remains SHELVED, not a second approved allocation. |
| Alternatives | Shares avoid option spread/decay cost but have different dollar downside; no new shares proposal. Outright January 215C ask alone is $1,040 before fees. Retain the commissioned vertical or wait. |
| Edge / Kelly | HENRY evidence supports the thesis; no calibrated payoff probability or positive EV established. No Kelly size. |

## 6. Prospective management, only if later approved and filled at ≤ $4.90
| Rail | Condition / consequence |
|---|---|
| Harvest | Sell the whole spread at executable complex bid ≥ $8.00: +$307.40 net at a $4.90 entry with $1.30 fees each way. |
| Invalidation | RSP completed close < $208.02, thesis-owner retraction, or executable spread bid ≤ $2.45: exit whole spread. At exactly $2.45 the modeled loss is $247.60 including round-trip fees; gaps can lose the full debit. |
| Time stop | Existing view ends 2026-12-18: close any then-held spread under the approved card. This is a prospective new-position term, not a reminder on held lines. |
| Roll / add | None pre-approved. A missed opportunity needs rework; root rule #7 does not approve a new deployment. |
| Review | At the next requested desk touch or a material HENRY change; recheck broker quote and day colour at any proposed order. No held-line expiry prompts. |

ETF options can be assigned early. The capped expiry payoff assumes the intact managed spread; assignment or broker intervention can create share/cash obligations and extra costs. Standard deliverables and account handling must be confirmed.

## 7. Best counter-case and forecast treatment
October's breadth repair can already be priced; a profitable relative RSP/SPY move need not lift RSP enough in absolute dollars. HENRY's 11/02 pre-open map remains negative gamma, so market instability persists. Paying $771.30 for $228.70 of maximum terminal gain is poor construction even if the breadth thesis is sound. Recommendation: **wait for both a red day and a genuinely affordable broker quote; otherwise no trade.**

WQ-493 A: this is a reprice of the existing pre-ruling 10/20 card, with its completed confirmation now known. No retrospective trigger probability is created or back-filled. The historical card, including the spent 10/23 entry, is preserved at `../research/2026-11-02_rsp-reprice/RSP_card_before.md`; the first verdict above is current.

## 8. Decision route
WQ-591 A approved this card as a conditional (see the verdict line). TERRY re-checks live and presents the order at an eligible entry; broker debit above $4.90 or size above ×1 is not approved.

**APPROVAL REQUIRED — Will must approve/reject before execution.**
