# POSITION-MANAGEMENT CARD — HBAN Oct-16-2026 $16 PUT ×2 (held, IN THE MONEY) — what the 7/18 "ride to expiry" ruling means now
**Date:** 2026-09-26 Sat, written 15:1x ET (`date` 15:11:18 ET) · **Card ID:** `MGMT-HBAN16P-OCT16` (management-only, not a `TRY-` entry card; see foot)
**Updated 2026-09-26 16:0x ET (`date` 16:00:37 ET)** on Will's word, 15:54 ET, verbatim: *"Position cards: Keep WQ-302 open pending confirmation of holdings/account and my management choice. Update the cards with Fidelity's published policy on unsupportable positions, then narrow my question to the handling, timing and costs applicable to this account. Don't treat screening quotes as executable proceeds."* Changed: §4 now quotes Fidelity's published policy and corrects this card's earlier "SEARCH-NOT-FOUND". The question to Fidelity is narrowed to handling, timing and costs. Every option price is relabelled as a SCREENING quote. **WQ-302 stays OPEN** (PROME's row). The 7/18 ruling is not re-ruled, and R-A/R-B are unchanged.
**Commissioned by:** Will, **WQ-292 RULED 2026-09-26 15:04 ET**, verbatim: *"Authorize TERRY to prepare the two position-management cards. Confirm current holdings and identify the broker-mechanics uncertainty. The cards return to me; this authorizes preparation, not trades."* (record `PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md`)
**Thesis owner:** **none, by Will's ruling.** 7/16, Will: *"Stress lottery ticket — I was seeing unusual volume and attempted a play."* 7/18, Will: **EXIT-THESIS** (REGINALD brief `AGENTS/REGINALD/reports/2026-07-18_HBAN_thesis-or-exit_decision-brief.md`). Prior governance: `setups/HBAN_oct16-16P_stub.md` (RETIRED, kept for the record).
**Standing ruling (Will, 2026-07-18), as the stub records it:** *"The Oct-16 $16P ×2 rides to expiry as dust (~$20 mark; commission ≈ proceeds → do NOT pay to close). Zero further analytic effort. No re-entry as a stress vehicle."*
**Terry verdict:** `RULING STANDS AS WRITTEN — ITS PREMISE HAS CHANGED — CONDITIONAL`. TERRY does not re-rule it (§3).
**Construction rule #20 applies:** retroactive, **management-only**. Entry fields are **UNRECOVERABLE**. Forward max loss = the remaining mark (#20(d)).

---

## 0. Position — as the FORGE mirror records it, and what that record cannot tell you

**Mirror row** (`FORGE/STATUS.md` § Other puts, read 2026-09-26 15:1x ET):
| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|---|---|---|---|---|---|---|---|---|
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.25 | $50.00 | −$141.34 / −73.87% | "EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort. 0.20 [9/3] → 0.25 (today −$14). 36 DTE" |

**The mirror runs on THREE vintage clocks, and they are not one date:**
| clock | what it dates | does it cover THIS line? |
|---|---|---|
| **2026-09-16 13:57 ET visual capture** (WQ-272 standing write-in, 9/20) | AAPL · TBT · GLD · cash · Fidelity total · RH total | **NO.** This option's quantity was not re-read on 9/16 (TERRY Q1 map R1). |
| **2026-09-18 receipt** | VLO 1 sh only (D-55) | **NO.** |
| **2026-09-10 CLOSE** (Fidelity positions view) | every option quantity, mark and G/L | **YES. This is the clock for this line.** Qty 2 and the $0.25 mark are 16 days old. The mark is now wrong by a factor of ~2–3 (§1). |

**Account:** Traditional IRA, **INFERRED** by position-set match (mirror header: "header cropped").
**`FORGE/position_management.tsv`:** *"2026-10-16 expiry · APPROVED · … Existing ride-to-expiry disposition; no new trade instruction."*

**WQ-274 gaps that touch this line (named, not closed):**
- **① Fidelity Activity view.** A trade on this contract since 9/10 would appear only there.
- **⑤ Post-capture moves 9/16 → now.** No capture of this line exists after 9/10.
- ②③④ do not touch it.

**POSITION_INTAKE:** qty 2 `[9/10 view]` · cost $0.96/ct ($192) · fill date **UNRECOVERABLE** (the stub records a 7/16 trim from ×4 to ×2; the original entry was never recorded) · thesis: none, by ruling · max additional loss tolerated: the ruling implies the whole remaining mark. **`[POSITION_STATE_INCOMPLETE]`**: quantity and account type unconfirmed since 9/10.

---

## 1. Live pull (SCREENING only): Saturday, so the 2026-09-25 Fri close is the freshest close

| item | value | source + time |
|---|---|---|
| HBAN | **$15.64** (+2.16% on 9/25) | `fetch.py price HBAN`, 2026-09-26 15:09 ET; as-of 9/25 close |
| Oct-16 16P, **SCREENING quote** (vendor feed, 9/25 close basis, bid/ask undated) | **bid 0.45 / ask 0.80 / mark 0.62** · **spread 56%** · IV 39.84% · OI 14,129 · vol 161 · **last trade 9/24 15:58** (not a 9/25 print) · no quote-defect flag on this strike | `chain_fetch.py HBAN 2026-10-16 --type put --no-cache`, 15:09 ET 9/26 |
| chain quality | 🟠 NONMONO 2 of 6 rows (33%) on the 13 and 14 strikes, both NOBID. **The strip is thin.** Trust the 16 strike (OI 14,129) more than its neighbours. Still re-pull at the broker. | same pull |
| moneyness | **ITM by $0.36** (HBAN must rise **+2.30%** to reach $16) | arithmetic |
| intrinsic ×2 | $72 | 0.36 × 200 |
| screening value ×2 at the vendor bid (**not proceeds**) | **$90** (time value at the bid ~$0.09/ct ⇒ ~$18) | 0.45 × 200 |
| screening value vs cost $192 | **−$102 at the screening bid** | |
| commission to close ×2 | **$1.30** (+ small regulatory fees) | Fidelity: *"$0.65 per contract"* (fidelity.com/trading/commissions-margin-rates, read 2026-09-26) |
| sessions to expiry | **15** (Mon 9/28 → Fri 10/16) | |

⚠️ **Every option price on this card is a SCREENING quote. None of them is proceeds.** Source: a vendor feed on the 9/25 close basis with an undated bid/ask (construction rule #14). **At a 56% spread even the bid is not a fill.** **Executable proceeds come only from Fidelity's live chain on the day of the sale.** Every $ figure below derived from these quotes ("~$90", "−$102", "~$18 time value") is screening arithmetic.

**HBAN moved against the put on 9/25:** ITM by $0.69 at the 9/24 close (Q1 map) → **$0.36** at the 9/25 close. **At this moneyness one ordinary up-day decides whether it expires ITM or OTM.** The 9/25 move alone was +2.16%, and 2.30% is the distance.

---

## 2. What sits between now and Oct-16
- **HBAN Q3 2026 earnings: Thursday 2026-10-22, before the open** (HBAN IR, "Huntington Bancshares Incorporated Announces Earnings Release Dates for 2024 – 2026", release dated 2024-04-04, read 2026-09-26). That is **after** the 10/16 expiry. ⚠️ It is a schedule published in 2024. It could move, but its Q2 2026 date (7/23) held. **⇒ No print inside the window; construction rule #18 is not engaged.**
- No DOCKET row, no gate. The 7/23 print row is RESOLVED / MONITOR-ONLY.

---

## 3. The 7/18 ruling — what it implies NOW, and what changes only if Will re-rules

**The ruling had two parts: a LETTER and the PREMISE it was written on.**
| | 7/18 | 2026-09-25 close |
|---|---|---|
| moneyness | OTM (−13.2% on 7/16) | **ITM by $0.36** |
| value ×2 | "~$20 mark" | **~$90 at the screening bid** ($72 intrinsic at the 9/25 close) |
| commission ≈ proceeds? | yes, *"commission ≈ proceeds → do NOT pay to close"* | **no, on the screening quote: a $1.30 online contract fee against ~$90 of screening value (~1.4%).** If Fidelity places the close instead, the published Rep-Assisted charge is **$32.95 + $1.30 ≈ 38% of the screening value** (§4) |
| what "rides to expiry" meant | a lapse to $0 at expiry, with zero effort | **not a lapse if it stays ITM. See §4.** |

**What the letter implies now (TERRY's reading, not a re-ruling):**
1. **"Rides to expiry" still binds.** No close, no roll, no add. Nothing on this card overrides it.
2. **"Do not pay to close" no longer describes the economics.** Closing an ITM long put **receives** money. The ruling's concern was commission eating the proceeds, and on the screening quote the value is about 69× the online contract fee. Real proceeds exist only on Fidelity's live chain. **The premise failed. The letter did not change.** ⚠️ The published policy (§4) adds an inversion: **a hands-off ITM expiry is exposed to the $32.95 Rep-Assisted charge, or to forfeiting the intrinsic.** The ruling set out to avoid exactly that kind of commission.
3. **"Zero effort" is no longer guaranteed.** The ruling assumed the put would expire worthless, which needs no broker action. **If HBAN closes below $16.00 on 10/16, the put reaches Fidelity's auto-exercise process ITM** (Fidelity: *"$0.01 or more in the money … will be automatically exercised"*) **in an account with no HBAN shares.** What happens then is set out in §4: Fidelity's published policy lets it act in any of three ways, and which one it takes, and when, is UNKNOWN. **The ruling did not consider that branch, because on 7/18 it was far from reachable.**
4. **The letter does NOT call for a Do-Not-Exercise instruction.** DNE forfeits the intrinsic (Fidelity: *"the intrinsic value of the option is forfeited, resulting in a total loss on the value of the option if the contract is not closed by the customer prior to expiration"*). Reading "ride to expiry" as "block the exercise" would turn ~$72 of intrinsic into $0. **TERRY does not read it that way, and neither should a default.**

**What changes ONLY if Will re-rules** (listed, not recommended; the ruling is Will's and only Will moves it):
| option | effect |
|---|---|
| **R-A: permit a sell-to-close before expiry** | ~$90 **screening** value at the 9/25 vendor bid (−$102 vs cost instead of up to −$192). Real proceeds = Fidelity's live bid on the day. Removes the §4 branch entirely. **Costs one ticket and a 56%-wide spread**: work a limit order, never the market. |
| **R-B: ride, but close on 10/16 if still ITM** | Keeps the ruling's spirit (no effort unless the exercise branch is live) and never meets the expiry process. Needs one look on 10/16 before 16:00 ET. |
| **No re-rule** | The letter stands. If HBAN ≥ $16.00 at the 10/16 close, it lapses to $0 exactly as ruled (**forward max loss ~$90, the remaining mark**). If HBAN < $16.00, **Fidelity's published process decides** (§4): a Rep-Assisted close ($32.95 + $1.30), an exercise and buy-in, or an instruction not to exercise (the ~$72 intrinsic is lost). |

**The dated decision point:** **Wed 2026-10-14, by the close**, if Will wants R-A or R-B in place with two sessions to spare. **Hard backstop: Fri 10/16 before the 16:00 ET close.** Fidelity's call-in deadline for a customer to block an auto-exercise is **published twice, and the two differ: 16:15 ET** on the auto-exercise web page, **16:20 ET** in the Options Agreement (§4). That deadline matters only for DNE, which the letter does not call for. **Fidelity publishes no time for a close it places itself.**

---

## 4. ⛔ The named UNKNOWN — broker mechanics at expiry, in an IRA, ITM, no shares

**UNKNOWN to this desk:** what Fidelity does, in **this account**, with a long put that is ITM at the 10/16 close when the account **holds no HBAN shares**: **auto-exercise · close it out · let it lapse.** Narrowed 16:0x ET: the published policy (below) lists the actions Fidelity **may** take. What remains UNKNOWN is **which** action it takes in this account, **when** it takes it on 10/16, and **what it costs**.

**Fidelity's PUBLISHED policy — the Options Agreement covers this case** (read 2026-09-26 ~16:0x ET). ⚠️ **Correction:** this card's 15:1x version said *"SEARCH-NOT-FOUND at Fidelity's public pages."* That was **wrong**. The earlier read covered three web pages and never opened the agreement.

**Source A: Fidelity Options Agreement** (https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/option-agreement.pdf; the same file is at /accounts/mando/option_agreement.pdf; form `1.734349.120`, footer "© 2025 FMR LLC"; no effective date printed). Verbatim, § "Exercise and Assignment of Options":
> *"in the absence of any instructions from you, you authorize us to exercise any in-the-money options that remain in your account on their expiration day, so long as they are in-the-money by $0.01 or greater or in accordance with Fidelity's policies then in effect, as applicable. If you do not want us to exercise any expiring options, you must notify us by 4:20 p.m. Eastern time on the expiration date by calling Fidelity at 800-343-3548."*
> *"If sufficient assets and/or other positions are not available to cover the exercise or assignment of an option, you authorize Fidelity to take the following actions while charging the Rep-Assisted commission rate: • place an order to close option positions • place an order to minimize market risk (for example, if it would result in a short position or cash debit in an account not enabled for margin, result in an equity level that is below the aforementioned minimum, or if there are no shares available for a short sale) • instruct the OCC not to exercise valuable options on or prior to the last trading day"*
> *"If an option is exercised or assigned, you authorize us to close out the unsupported equities positions that result from the exercise."*
> *"If an option assignment results in a short position of a security in your account, you understand that you may be charged short interest fees to maintain that position in your account."*
> § "Purchasing Expiring Options": *"On the expiration date of an equity option, Fidelity may (i) restrict your ability to place new opening transactions and (ii) cancel any unexecuted opening transactions. The timing of these actions may vary."*
> Same agreement, margin section: *"Retirement accounts and Fidelity BrokerageLink® accounts cannot trade foreign securities or sell short, are not eligible for margin loans, and may be subject to other rules and policies."* (The Brokerage Retirement Customer Account Agreement, form `596805.15.0`, carries the same sentence.)
> IRA section: *"You must meet the initial and maintenance requirements for your options positions, including Options Spreads, at all times or your positions may be closed by Fidelity without notice."*

**Source B: Fidelity Brokerage Commission and Fee Schedule** (https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/Brokerage_Commissions_Fee_Schedule.pdf, form `596805.20.0`, no date printed). Verbatim: *"Rep-Assisted $32.95 per trade + 65¢ per contract"* · *"Maximum charge: 5% of principal (subject to a minimum charge of $12.95 for FAST trades and $32.95 for Rep-Assisted trades)."* · *"Exercises and assignments are commission-free and are not charged a per contract fee."* It also names an Options Fee that offsets the OCC's Options Regulatory Fee, *"The ORF has ranged from $0.02 to $0.04 per contract"*.

**Source C: web pages.** Auto-exercise rules (fidelity.com/options-trading/options-auto-exercise-rules): *"To prevent automatic exercises, please call us prior to 4:15 p.m. ET, on the last trading day of your options contract."* Long-put strategy guide (fidelity.com/learning-center/…/longput-speculative): *"If there is no offsetting long (or owned) stock position, then a short stock position is created. … if a speculator wants to avoid having a short stock position when a put is in the money, the put must be sold prior to expiration."* Learning center, "Managing and monitoring options expirations", which speaks of *"a brokerage firm"* in general and not of Fidelity's own policy: *"If the brokerage firm blocks exercise, the intrinsic value of the option is forfeited, resulting in a total loss on the value of the option if the contract is not closed by the customer prior to expiration."* The options FAQ and the "How to exercise, roll, and assign options" page say nothing on this case.

**What the published policy establishes for this account (a Traditional IRA per the mirror, INFERRED):**
| question | what the documents say | status |
|---|---|---|
| Can the IRA hold the short stock that exercise would create? | No. *"cannot … sell short"* | **VERIFIED** (published) |
| Does Fidelity reserve the right to act? | Yes, three ways: **close the options**, **place an order to minimize market risk** (a short position in a non-margin account is the agreement's own example), or **instruct the OCC not to exercise**. It may also close out *"unsupported equities positions"* that an exercise creates. | **VERIFIED** (published) |
| **Which** of the three does Fidelity do in this account? | Not stated. The agreement lists all three as authorized actions and does not say which one it uses. | **UNKNOWN** → the §4 question |
| **When** on 10/16? | Not stated. The OCC instruction is *"on or prior to the last trading day"*. The web page says 4:15 p.m. for a customer's do-not-exercise call and the agreement says **4:20 p.m.**, so **Fidelity's own two documents conflict.** No published time for a Fidelity-initiated close. | **UNKNOWN** → the §4 question |
| **What does it cost?** | A close that Fidelity places is charged *"the Rep-Assisted commission rate"* = **$32.95 per trade + 65¢/contract** (Source B; the 5% maximum is itself *"subject to a minimum charge of … $32.95"*). A self-placed online close costs **$0.65/contract** plus the Options Fee. Exercise itself is commission-free. If a short results: *"short interest fees"*. | **VERIFIED** for the rate card. **UNKNOWN** whether one ticket or one per line, and what the ORF pass-through is on the day |
| Could the intrinsic be forfeited? | Yes, if Fidelity uses the *"instruct the OCC not to exercise valuable options"* branch. The learning center's forfeiture sentence describes that outcome in general terms. | **INFERRED**: the branch is published; whether Fidelity uses it on a long put is not |

**In dollars (screening basis):** exercising ×2 **sells 200 HBAN at $16 = $3,200** in an account that, per the published policy, cannot be short. The screening intrinsic is ~$72.
| branch Fidelity may take | cost to Will vs selling online himself ($1.30 + Options Fee) |
|---|---|
| Fidelity closes the puts (Rep-Assisted) | **+$32.95** per ticket, on a screening value of ~$90 (**~37%**). Plus the fill Fidelity gets inside a 56%-wide spread |
| Exercise, then Fidelity buys in the short | exercise is commission-free. The buy-in is an unsupported-position close, **rate NOT stated**; possible short-interest fees; weekend gap risk if it happens after the close or on Monday 10/19 |
| Fidelity instructs the OCC not to exercise | **the whole ~$72 intrinsic (screening)** |

**The dollars are small on this line, but the Rep-Assisted charge is proportionally large.** The same question is ~7× larger in dollars on the TLT 82P (screening intrinsic ~$536 vs ~$72), so ask it once for both.

**The one question Will asks Fidelity** (narrowed to handling, timing and costs, per Will 15:54 ET; phone 800-544-6666 or chat; the same question word for word on the TLT card, and one call covers both):
> *"Please confirm that my account ending [____] is a Traditional IRA holding 2 long TLT Oct-16-2026 $82 puts and 2 long HBAN Oct-16-2026 $16 puts, and no shares of either. If either put is in the money on Friday 10/16, which of the actions in your Options Agreement will you take in this account (let it auto-exercise and then close out the resulting short stock, sell the puts yourself, or instruct the OCC not to exercise them), and at what time that day? What is my own deadline that day to sell them to close online, and to give a do-not-exercise instruction (your web page says 4:15 p.m. ET, your Options Agreement says 4:20 p.m.)? What exactly would I be charged if you act instead of me: the $32.95 Rep-Assisted commission plus 65¢ per contract, charged per ticket or per line, and any buy-in or short-interest fee?"*

⚠️ **The answer is account-specific and it is Will's to get.** Fidelity's published policy reserves three actions and chooses none of them in writing. TERRY quotes only what it read, on the date it read it. Fidelity's own published way to avoid the branch is *"the put must be sold prior to expiration"*. On this card that is R-A or R-B, **which only Will can rule.**

---

## 5. Day colour — root rule #6 as it applies here
- Rule #6 governs **buying**. It does not bind a leg the ruling says to hold, so **under the ruling as written it has nothing to act on.**
- **If Will re-rules to R-A or R-B**, the inverted proxy applies to the sale: **sell on a RED HBAN day** (puts bid). The convexity at stake is **~$18 of time value at the screening bid**, and the spread (56%) is a bigger cost than the day's colour. ⇒ **The execution discipline that matters here is a limit order inside a wide spread, not the day colour.** A green-day sale still gets its figures written on the card before the fill (RISK_RULES § Breaking root rule #6). On 10/16 itself, the §4 unknown is the measured reason.

---

## 6. What Will must confirm
1. **Quantity is still ×2** and nothing traded on it since 9/10 (WQ-274 ①⑤).
2. **The account is the Traditional IRA** (INFERRED on the mirror).
3. **Fidelity's answer to the §4 question** (handling · timing · costs, with the account-type confirmation inside it; one call covers both cards).
4. **Whether the 7/18 ruling stands as written or is re-ruled (R-A / R-B)**, by Wed 10/14. Silence = the letter stands, and the §4 branch stays live if HBAN is below $16 on 10/16. **WQ-302 stays OPEN until items 1, 2 and 4 are in** (Will 15:54 ET).

---
**APPROVAL REQUIRED — Will must approve/reject before execution.** No trade is proposed, and the 7/18 ruling is not re-ruled here (WQ-292: *"this authorizes preparation, not trades"*). `$0` moved · no order · no gate or threshold moved. — TERRY

*Card-ID note: `MGMT-` is deliberately not a `TRY-` id. `SETUPS.tsv` is at its rotate tier with a rotation owed first (STATUS 2026-09-25). The registry row is in `setups/INDEX.md` beside the retired stub's row.*

---

## ADDENDUM 2026-10-02 Fri 10:5x ET: event calendar to the 10/16 expiry (OZK `PROME/inbox/2026-10-02_from-OZK_events-10-02-to-10-16.md`). The text above stands

- **HBAN reports Thu 10/22 at 09:00 ET** (IR page, VERIFIED by OZK). That is **AFTER these two puts expire (Fri 10/16)**, so **the line never sees HBAN's own print.**
- **The expiry morning carries four peer prints before the open:** MTB (call 08:00) · TFC (08:00) · CFG (09:00) · RF (10:00). It also carries **monthly OPEX**.
  - Earlier in that week: JPM / WFC / Citi / GS 10/13, BAC / MS 10/14, USB 10/15, and CPI 10/14.
- **What it means for the WQ-302 rail** (dated decision Wed 10/14 by the close; hard backstop Fri 10/16 before 16:00):
  - Holding past Wed 10/14 buys exposure to **peer** prints only, on the last morning, with expiry-day exercise risk in the IRA (D-60).
  - No own-print catalyst exists inside the line's life.
  - The construction-rule #18 envelope (regional-bank 1-day moves: median 2–3%) applies to peers' read-through at most.
  - **No lean change is made here.** Re-mark at the 10/14 decision point at the live chain.
- `$0` MOVED · NO ORDER.

---

## ADDENDUM 2026-10-07 Wed 11:0x–11:1x ET: re-mark for the WQ-302 decision (PROME wave-2 spawn, cloud session). The text above stands as written

**Framing update:** Will's standing practice (`USER.md`, 9/30 19:03 ET) puts a **sell-or-roll rail** on every option line and never a lapse rail. That retires the 7/18 "rides to expiry" letter as a default; the line is managed as sell-or-roll. Re-ruling it is still Will's word (WQ-302).

| Item | Value | Basis |
|---|---|---|
| HBAN | **$15.05 (−1.86%)** at 11:07 ET; closes 10/2 $15.33 · 10/5 $15.29 · 10/6 $15.33 | `fetch.py`; yfinance daily |
| Moneyness | **$0.95 in the money** ⇒ intrinsic ×2 ≈ **$190** vs the **$192** paid | arithmetic |
| 16P Oct-16 bid / ask | **0.85 / 1.10** (23% wide, OI 14,134; last trade ~10:06 ET) — the bid sits **below** intrinsic, so the quote is stale or wide; SCREENING ONLY | `chain_fetch.py` |
| Today's tape | Regional banks sold off: WAL −3.7%, KRE −2.0%, FLG under REGINALD's RED line intraday (`SIG-W-20261007-001`, info) | BOARD |
| Calendar | Bank prints JPM/WFC/C 10/13 · BAC/MS 10/14 · USB 10/15 · MTB/TFC/CFG/RF the expiry morning 10/16. **HBAN's own print, Thu 10/22, falls AFTER expiry** | ADDENDUM 10/2 |

**Desk lean: SELL both (R-A), at a limit at or above intrinsic, on a RED HBAN session, by Wed 10/14 at the close.** Today is red — the right colour to sell a put. Work a limit inside a ~23%-wide market; never a market order. **No roll:** a roll past 10/22 would be a new bet on HBAN's own print, and the 7/18 ruling bars re-entry as a stress vehicle. Holding past 10/14 buys only peer read-through plus the IRA expiry-day exercise risk (Fidelity's handling UNOBSERVED, D-60). Position truth: ×2 per the 10/1 mirror; nothing later reported.

**Will's decision and deadline, plainly:** sell the two HBAN puts by **Wednesday 10/14 at the close** (hard backstop Friday 10/16 before 4:00 PM ET). They are worth about $190 in intrinsic value today, roughly what he paid.

`$0` MOVED · NO ORDER. **APPROVAL REQUIRED — Will must approve/reject before execution.**
