# TERRY → PROME · 2026-10-08 Thu, written 09:00–09:0x ET (`date` 09:00:41) · C5 re-mark of the two Friday expiries: PARTIAL, pre-open only (closed on Will's 08:59 word via PROME; re-spawn at the open)

**Spawn:** PROME `prome-fc`, laptop `WilliePOwen`, WQ-348 C5 (brief `PROME/tasks/2026-10-08_wakes/TERRY.md` + `COMMON.md`, both read whole). Runtime: Claude Code, Opus 5.5 (`claude-opus-5-5`), sole TERRY writer. **`$0` · no order · no fill · no gate, level or threshold moved.** Option quotes before 09:30 were DEAD (0/0) on every strike pulled, so **no option mark exists in this memo.** Every price below is a vendor pre-market or futures quote with its clock, and none is a close.

## 0. For the fresh window: the re-mark still needs (at or just after 09:30)
1. **USO Oct-09 150C bid/ask** (Fidelity governs; vendor = screening, durable finding 5b). Also the Oct-16 150C ask, and the Oct-16 strike whose ask is ≤ the Oct-09 bid.
2. **QQQ Oct-09 755P bid/ask.** Check it against the ≥ $4.78 harvest suggestion (2× the $2.39 average; suggested 10/7, never adopted).
3. Live USO and QQQ (`fetch.py price`) with clocks. Then fill the arithmetic in §1–§2. Tooling: the `chain_fetch.py --no-cache --legs <strike>` fire-time form.

## 1. USO Oct-09 $150C ×1 (`MGMT-USO150C-OCT09`): pre-open facts

| Item | Value | Basis |
|---|---|---|
| USO | **$149.46 pre-market** at 08:51:38 ET ⇒ **$0.54 below the strike**. 10/7 close $143.91 | yfinance `preMarketPrice`, vendor |
| Crude | `CLX26` $92.41 (08:42 ET; prior $88.28) · `BZZ26` $104.93 | single-vendor futures quotes, not settles |
| Option | **no live quote** (0/0 pre-market). The last mark is the 10/7 close: bid/ask 0.35/0.43, last $0.39 at 15:59 | `chain_fetch.py` 08:54 ET |
| Exercise | ⛔ **UNFUNDABLE**: a Friday close above $150.00 makes the IRA buy 100 USO for $15,000 against ≈ $11,421 cash net of pending [10/7 capture]. The sale is the plan; exercise is not | card 10/7 addendum |

**The arithmetic the open will fill.** Let B = Fidelity's bid at the mark. Intrinsic is $0 while USO is below $150.
- Selling today brings in B × 100 − $0.65.
- Holding to the Fri 15:00 ET stop is worth more **only if USO is at or above about $150 + B at 15:00 Friday.**
- At an unchanged $149.46, the call is worth ≈ **$0.36–0.57 at Fri 15:00** (MODEL, Black–Scholes at 40–55% IV, one hour left). At an unchanged USO the stop forfeits ≈ (B − ~0.45) × 100.
- Near the money, the whole bid is time value. That is construction rule #21(b)'s worked case (~ATM, 100% extrinsic, decaying and accelerating), and it argues for CLOSING, never for rolling.

**What WQ-366's DECLINE fixed** (Will, Deck tap 10/3 21:10 ET: *"I dont think I sell yet. The news in Saudi arabia continues to get worse"*):
- It declined ADDENDUM-3's 10/2 SELL-TODAY lean, which rested on the G7 release decision removing the reversal path.
- It HELD the call.
- The **Fri 10/09 15:00 ET stop STANDS "unless Will says otherwise"** (DOCKET L605).
- ⇒ **A Thursday sale is outside the DECLINE's content.** The DECLINE neither forbids one nor authorizes one. It would be a new Will decision on new facts, and the 10/7 card already says earlier is his choice. The reason Will held, worsening Mideast news, is the move that came overnight (BRENT: Hormuz leads; the Isaias part is transient absent damage).
- **Pre-open desk inclination (the fresh window confirms or revises it on marks):** sell TODAY into strength at Fidelity's bid. The stop stays the fallback.

**Roll:** pre-open lean **NONE**, for four reasons:
1. No fired trigger. BRENT 10/8: "not a new event-class arm", WQ-192 holds, deploy question CLOSED (durable finding 1).
2. Rule #21(b) above.
3. The oil exposure stays via the 37 USO shares and the 1 VLO share.
4. Root rule #6: today is green for USO, the wrong day for a roll's call buy. The measurement bar is the Oct-16 150C's implied vol at the 10/7 red-day ask, **42.6%** (1.85 at USO $143.91, 7 sessions, trading-day convention; screening).

Only a construction rule #21 roll counts as a roll: **Oct-16 150C ×1 as one net-debit order.** An Oct-16 strike priced at or below the sale proceeds is a strike change, so it is a **NEW DEPLOYMENT** (#21), not a roll. It would need its own trigger.

**Root rule #6 on the sale:** selling a held call is an EXIT. The rule governs buys and does not bind the sale. A green USO day is the favourable colour to sell a call.

## 2. QQQ Oct-09 $755P ×2 (`MGMT-QQQ755P-OCT09`): pre-open facts

| Item | Value | Basis |
|---|---|---|
| QQQ | **$752.53 pre-market** at 08:52:19 ET (−0.69% vs the $757.73 close) ⇒ **the 755P is $2.47 IN the money** pre-market | yfinance `preMarketPrice`, vendor |
| Option | **no live quote** (0/0). 10/7 close: 2.02/2.07 | `chain_fetch.py` |
| Model at an unchanged $752.53 | one put ≈ **$3.85–4.45 at Thu 14:30** vs ≈ **$3.56–4.07 at Fri 10:00** (12–15% IV) ⇒ waiting from the post-auction window to Friday morning costs ≈ $0.3–0.4/ct, ≈ $60–75 for the two | MODEL, shape, not price |

- **Pre-open inclination (confirm on marks):** with the put in the money, a slipped Friday sale now lands on the assignment branch (≈ $151,000 QQQ short the IRA cannot carry). That moves the lean toward **TODAY 14:00–15:30 ET, after the 13:00 30-year reopening result** (CUSIP `912810UW6`, BOND CATALYSTS). Fri 09:45–10:30 (≤ 12:00) stays the fallback.
- Root rule #6: QQQ is red pre-market, the favourable colour to SELL a put; the rule governs buys.
- **No roll stays no roll:** no agent thesis and no fired trigger. WQ-365 is still not armable (HY OAS 303 [10/6], FRED; the 10/7 cell was unpublished at 08:53 ET).

## 3. VLO leg A (`GATE-TERRY-VLO-HELD-01`), WQ-386 source order: COMPLETE

| Source | 10/7 session | Use |
|---|---|---|
| ① CME settlement | not reachable by desk tools | — |
| ② vendor daily row 10/7 | **REJECTED, duplicated volume** (`HOX26` 41,943 and `CLX26` 265,937 on BOTH the 10/6 and 10/7 rows; own pull 08:54 ET) | — |
| ③ 14:28–14:30 ET 1-min VWAP, ESTIMATE | **$105.79 / $105.82** (typical / close VWAP, 3 bars per leg; own pull 08:54–08:55 ET; `HOX26` exp 10/30, `CLX26` exp 10/20). BRENT $105.82 | **last valid observation** |

- **Leg A NOT FIRED, no notice, on the 10/7 ③ ESTIMATE ≈ $105.8:** $15.6 above $90.16 and $10.8 above $95, far outside the ±$0.15 UNKNOWN band. **The 10/8 intraday $109.67 is diagnostic only and is not graded.** BRENT produced no 10/8 window proxy.
- **Own-text correction (on the card):** my 10/7 line *"10/5–10/7 … stay UNKNOWN, never back-filled"* was too broad. "Never back-filled" bars a later session's number standing in for a missing one; it does not bar reading a session's own ③ value at the next touch. BRENT's ③ values for 10/5 ($101.40) and 10/6 ($102.55) exist (not reproduced here) and also sit far above both lines. No exit or notice was established on any session from 10/2 to 10/7.
- **WQ-392 (informed, no action):** HEN-46 F1 reads December from 10/15 (HENRY's encode). This gate's basis is unchanged under WQ-386.

## 4. The two packets bearing on the cards (read only; left in place, not consumed)
- **VULCAN 10/8:** confirmed, **L590 FINAL's lean NONE did not rest on QQQ membership.** It rests on that memo's pre-registered row *"HY back ≤ 312 ⇒ everything → NONE"*, which fired (HY 310 · 312 · 303). The correction cuts both ways: ORCL is not in QQQ (the card was right), and CRWV is (the folded phrase "by DRAG, not by DIRECT HOLDING" is wrong on the letter; weight unmeasured). It changes no card here.
- **REGINALD 10/7 (REG-T-03 0 of 3, REG-T-01 un-fired):** bears on `TRY-COND-KREADD` only. It changes nothing today; named for the next wake.

## COMPLETION — TERRY — 2026-10-08
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/TERRY/setups/VLO-SHARE_management-proposal_2026-09-28.md (§ 2-bis 10/8 touch), AGENTS/TERRY/setups/INDEX.md (VLO row), this memo
RESULT: Pre-open facts: USO $149.46 pre-mkt 08:51 ($0.54 below the 150 strike); QQQ $752.53 pre-mkt 08:52 (the 755P $2.47 ITM). Option quotes dead pre-open, so no marks. The sell-today-vs-stop arithmetic, WQ-366 scope (a Thursday sale is a fresh Will decision outside the DECLINE), roll NONE reasons and the exit-not-entry root rule #6 read are set up. VLO leg A is DONE: last valid obs is the 10/7 ③ ESTIMATE ≈ $105.8 (own repro; ② rejected for duplicated volume), NOT FIRED; $109.67 not graded. Both packets were read; L590 NONE does not rest on the VULCAN correction.
GAPS: Live USO 150C and QQQ 755P bid/ask (and the Oct-16 legs) not taken: dead pre-open, and this session was closed at 09:00 on Will's word before 09:30. STATUS.md not updated (memo is the record). Top-level inbox (REGINALD, VULCAN unmoved) plus the WALTER and WILL lanes wait for the next full TERRY session.
WILL_NEEDS: None yet. The fresh window turns §1–§2 into the Tier-3 sell/roll asks; the orders are Will's (root rule #5).
FOLLOW-UP: Re-spawn TERRY at the open with §0 as the checklist: fill the marks into §1–§2, confirm or revise the two pre-open inclinations (USO sell today; QQQ sell today 14:00–15:30 after the auction), write the card addenda.
