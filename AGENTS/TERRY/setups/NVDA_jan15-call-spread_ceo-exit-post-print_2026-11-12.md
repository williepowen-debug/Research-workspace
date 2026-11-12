# TRADE CARD — NVDA — long call spread, bought AFTER the 11/17 print, on the CEO-exit gap
**Date:** 2026-11-12 (written 09:14 to 09:1x EST from `date`)
**Setup ID:** IDEA-NVDA-CEOGAP-NOV12
**Thesis owner:** VULCAN (AI demand, grades the 11/17 print) for leg T1; the tape read (a governance shock priced before demand is known) is TERRY's own, labelled as such. HENRY owns dealer flow at the open.
**Thesis reference:** WALTER `BOARD/SIG-W-20261112-002` (IMMEDIATE, Nvidia newsroom "NVIDIA Announces CEO Transition", read by WALTER's helper); prior board cards 20261109-004, -011, 20261111-003.
**Terry verdict:** CONDITIONAL — NOT-FIRED
**Confidence in trade structure:** Medium (structure). Low (edge): the overreaction read is unproven and has no owner.
**Data freshness:** NVDA 11/11 close $173.73; pre-market $153.47 (−11.66%, vendor, 09:13 ET); 3-month range 165.89–243.37 (65 daily bars). Option chain NOT priced (pre-open quotes are the prior session's, and the card prices at fire on 11/18 anyway, construction rule #14). Position truth: no NVDA line in `FORGE/STATUS.md` (grep, 09:13 ET) `[POSITION_STATE_UNKNOWN]` beyond the mirror.

## 0. Missing inputs / hard caveats
- [x] Live price checked (pre-market, vendor)
- [ ] Option chain: CONDITIONAL, priced on the 11/18 open-session chain at fire, broker quote for the fill (finding 5b)
- [x] Existing position truth: none in the FORGE mirror; Will to confirm if he holds NVDA or a QQQ/SMH call line
- [x] Catalyst date: Q3 FY2027 results Tue 11/17 about 1:20 pm PT (Nvidia release, via WALTER)
- [ ] Thesis owner current: VULCAN has not yet graded the resignation or the print
- ⚠️ **The cause is not stated by Nvidia.** Press links it to reported affairs, and prior cards carry an FBI "looking into it" relay (Megaspeed). A legal, export-control or disclosure problem that surfaces before or after the print is the fat tail this card does NOT survive cheaply.

## 1. One-line setup
If Nvidia's 11/17 print shows the business unchanged by the CEO exit (VULCAN's grade) and the stock has not already recovered half the gap, buy a two-month call spread on 11/18, after the event premium is gone, betting the governance discount narrows.

## 2. Preconditions
- **Thesis precondition (T1):** VULCAN writes, in a committed artifact, that the 11/17 print and guide show no demand or order impact (no data-center guide cut, no order slowdown stated).
- **Tape precondition (T2):** NVDA trades below **$163.60** at fire (the midpoint between the $173.73 close and the $153.47 pre-market print: less than half the gap recovered). At or above it the rebound is priced: do not enter.
- **Day colour (T3):** NVDA red on the fire session (root rule #6, calls on red days). A break needs the refuting chain measurement written here before the fill.
- **Do NOT trade if:** any filing or official statement before entry discloses a legal, regulatory or export-control liability tied to the resignation; or VULCAN grades an order or guide impact; or no fire by the Fri 11/20 close (card void).

## 3. Chart / tape read
| Item | Read |
|---|---|
| Current price | $153.47 pre-market 09:13 ET (vendor), −11.66% vs $173.73 |
| Trend | Down: $243.37 high to $173.73 over 65 bars (−28.6%) before today; today's print is under the 3-month low ($165.89) |
| Key support | none inside the 65-bar window below $165.89; record the 11/12 session low after the close |
| Key resistance | $165.89 (old 3-month low), $173.73 (pre-news close) |
| Relative strength | SMH −4.33%, QQQ −1.40% pre-market: NVDA-specific |
| Vol / gap risk | Event vol into 11/17 on top of the governance shock; the card buys after both |
| Liquidity | NVDA options are among the deepest listed; still `chain_fetch.py --legs` at fire |

## 4. Entry
- **Trigger:** T1 and T2 and T3, graded once at fire on the 11/18 session (or 11/19, 11/20).
- **Preferred entry zone:** NVDA $140–163.60.
- **Do not chase:** NVDA at or above $163.60, or the debit above $4.00.
- **If missed:** no trade; the card voids at the 11/20 close.

## 5. Structure
- **Instrument:** NVDA call debit spread, ×1.
- **Expiry / tenor:** Jan-15-2027 (about 58 days from 11/18): long enough for a governance discount to narrow after the print, short enough that the print has already resolved demand.
- **Strikes:** long = the first $5 strike at or above spot at fire; short = long + $10. (At spot $153: 155/165C.)
- **Debit cap:** **≤ $4.00 net** (40% of width), broker quote at fill. Max loss ≤ $400 + fees, under the $500 card cap.
- **Alternatives considered:** outright calls (pay the full post-shock implied volatility, max loss above $500 for one contract near the money); shares (loss undefined without a stop that a gap skips); buying before the print (pays the 11/17 event premium, construction rule #18(c)); puts (chase of a −11.7% gap).
- **Why this expression:** defined loss, buys after the event premium, sells the upper strike to cheapen the bet.

## 6. Risk / scoring

### 6a. EFFECTIVE-N
| Field | Entry |
|---|---|
| Claimed corroborating legs | 2: VULCAN's demand grade, and the tape read that a governance shock overshoots |
| Shared antecedent(s) | **the AI and tech rebound.** The same falsifier sits under the QQQ Dec-18 670/680C card (NOT approved, WQ-617 C) and the RSP call paper row (PB-0009). Inside this card, both legs die if the print shows a demand problem |
| EFFECTIVE N | **1.** One view: the stock overshot because of governance, not demand |
| Sizing reference | ×1, single view |

- **Risk unit:** max loss ≤ $400 + fees (1.6R at 1R ≡ $250, under the 2R cap).
- **Edge:** small and unproven, labelled subjective. The case: the board says operations, customers and the roadmap continue unchanged; the market prices a governance discount before the print says anything about demand. The case against is in § 8.
- **Kelly reference:** not computed; no measured edge.
- **Sizing proposal:** ×1 at a debit of $4.00 or less.
- **Invalidation:** after the fill, NVDA closes below the 11/12 session low (recorded after today's close), or any official disclosure of a liability tied to the resignation: close at the bid, Will's order.
- **Gap/event risk:** a disclosure gap can take the spread to near zero overnight; the loss is capped at the debit.
- **Liquidity:** `chain_fetch.py NVDA 2027-01-15 --legs <long>,<short> --no-cache` must return rc 0 at fire.
- **Execution block:** Will's approval of this card; T1, T2, T3 at fire; broker debit ≤ $4.00.

## 7. Target / management
- **Harvest (finding 9):** spread bid ≥ $7.00 (70% of width): sell.
- **Partial exits:** none at ×1.
- **Roll rule:** none pre-registered; no roll.
- **Time stop:** spread bid below $1.00 with 21 or fewer days left: let Will decide, no reminder duty (USER.md 10/20).
- **Review cadence:** at fire; at Nvidia's next filing or CEO announcement; otherwise none.

## 8. Why not / counter-trade
- **The stock was already falling hard:** −28.6% over 65 bars before this news. A governance shock on a falling stock may not mean-revert; "the market overreacted" is a common story that is often wrong.
- **The cause is unstated.** If the resignation is tied to the Megaspeed relationship and an FBI interest (relayed on earlier cards), the liability could be real and arrive after the fill.
- **No owner holds the overreaction view.** VULCAN grades demand only; the tape read is TERRY's.
- **Prediction markets (ORACLE KB-ORC-137, 6ac1fce7f3, read 11/12 09:15 ET; ORACLE's figures, not TERRY's):** Polymarket "AI bubble" 12.3 vs 7.0 on 11/11, so the crowd moved toward the bear story overnight; permanent successor open (Kress PM 30.9 / Kalshi 33, Ian Buck 27.5 / 27), so a second leadership headline can land inside the card's window; the 11/17 earnings markets are thin ($2.3K, $8.2K) and give no read. The exit markets are settled: no edge there. ORACLE's own answer is NO CARD from the market side.
- **Crowding:** the bounce trade will be widely discussed; a fade that everyone sees is priced quickly, and T2 may never fire.

## 8b. Trigger forecast (WQ-493 A)
- **Trigger event:** VULCAN grades the 11/17 print as showing no demand or order impact (T1) AND NVDA trades below $163.60 on a red NVDA session (T2, T3) on 11/18, 11/19 or 11/20.
- **Deadline:** 2026-11-20 16:00 ET.
- **Resolution basis:** VULCAN's committed grade of the print; NVDA regular-session prices and day colour from `fetch.py price NVDA`.
- **Probability:** 0.20, subjective TERRY (no base rate for this event type). CALIBRATION row CAL-0008.

## 9. Decision
- [ ] APPROVE
- [ ] REJECT
- [ ] REWORK with changes: [what]

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
