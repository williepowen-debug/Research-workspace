# POSITION-MANAGEMENT CARD — TLT Oct-16-2026 $82 PUT ×2 (held, IN THE MONEY) — harvest vs hold into expiry
**Date:** 2026-09-26 Sat, written 15:1x ET (`date` 15:11:18 ET) · **Card ID:** `MGMT-TLT82P-OCT16` (management-only, not a `TRY-` entry card; see foot)
**Updated 2026-09-26 16:0x ET (`date` 16:00:37 ET)** on Will's word, 15:54 ET, verbatim: *"Position cards: Keep WQ-302 open pending confirmation of holdings/account and my management choice. Update the cards with Fidelity's published policy on unsupportable positions, then narrow my question to the handling, timing and costs applicable to this account. Don't treat screening quotes as executable proceeds."* Changed: §4 now quotes Fidelity's published policy and corrects this card's earlier "SEARCH-NOT-FOUND". The question to Fidelity is narrowed to handling, timing and costs. Every option price is relabelled as a SCREENING quote. **WQ-302 stays OPEN** (PROME's row). Nothing is re-ruled, and choices A/B/C/D are unchanged.
**Commissioned by:** Will, **WQ-292 RULED 2026-09-26 15:04 ET**, verbatim: *"Authorize TERRY to prepare the two position-management cards. Confirm current holdings and identify the broker-mechanics uncertainty. The cards return to me; this authorizes preparation, not trades."* (record `PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md`)
**Thesis owner:** none on file. The leg predates every TERRY card: it was already in the book on 2026-07-16 as part of Will's duration "grind" stack (TBT + 85P + 82P, `outbox/delivered/2026-07-16_to-PROME_try-fire-004-arm-packet.md`). Rates domain = BOND / HENRY.
**Terry verdict:** `HOLD OR EXIT — CONDITIONAL` · the one unconditional part: **do not let this put reach the 10/16 close unattended until Fidelity has answered the question in §4.**
**Confidence in the management structure:** Medium. The payoff arithmetic is High. The broker mechanics are UNKNOWN.
**Construction rule #20 applies:** this is a retroactive, **management-only** card. Entry fields are **UNRECOVERABLE** (§0). Forward max loss = the remaining mark, never the original debit (#20(d)).

---

## 0. Position — as the FORGE mirror records it, and what that record cannot tell you

**Mirror row** (`FORGE/STATUS.md` § Fidelity — Thesis Puts / TLT, read 2026-09-26 15:1x ET):
| Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|---|---|---|---|---|---|---|---|
| $82P | Oct-16 | 2 | $1.68 | $1.96 | $392.00 | +$56.65 / +16.89% | "No ruling recorded on this file" |

**The mirror runs on THREE vintage clocks, and they are not one date:**
| clock | what it dates | does it cover THIS line? |
|---|---|---|
| **2026-09-16 13:57 ET visual capture** (WQ-272 standing write-in, 9/20) | standing quantities + account totals: AAPL · TBT · GLD · cash · Fidelity total · RH total | **NO.** The six corrected cells are stock and account cells. This option's quantity was not re-read on 9/16 (TERRY Q1 map R1). |
| **2026-09-18 receipt** | VLO 1 sh @ $412.00 only (account + time UNKNOWN, D-55) | **NO.** |
| **2026-09-10 CLOSE** (Fidelity positions view) | every option quantity, every mark, every G/L | **YES. This is the clock for this line.** Qty 2 and the $1.96 mark are 16 days old. |

**Account:** "Fidelity: ONE account (Traditional IRA …, INFERRED by position-set match; header cropped)" (mirror header). ⚠️ **Even the account TYPE is inferred.** It matters here because the mechanics question in §4 is IRA-specific.

**WQ-274 gaps that touch this line (named, not closed):**
- **① Fidelity fills / Activity view.** Any trade on this contract after 9/10 would appear only there. The mirror cannot rule one out.
- **⑤ Post-capture moves 9/16 → now (current-book verification).** No capture of this line exists after 9/10.
- ②③④ do not touch this line (VLO account · Robinhood Sep-16 contracts · expired-unbooked rows).

**`FORGE/position_management.tsv`:** *"Next rates-position review; date not registered … no inherited TLT77P rule."* **No management rule exists on this line.** This card is the first.

**POSITION_INTAKE fields:**
| Field | Value |
|---|---|
| Instrument | TLT Oct-16-2026 $82 put, long |
| Quantity | 2 `[mirror, 9/10 CLOSE view]`, **Will to confirm** |
| Entry price / date | cost $1.68/ct ($336) `[mirror]` · **fill date UNRECOVERABLE** from a positions view (#20(c)) |
| Current mark | see §1 (screening, 9/25 close basis) |
| Original thesis / invalidation | **UNRECOVERABLE** — never written. Not reconstructed here (#20). |
| Catalysts before expiry | §2 |
| Will's desired action | UNKNOWN. That is this card's ask. |
| Max additional loss tolerated | UNKNOWN. §3 gives the forward max loss. |

`[POSITION_STATE_INCOMPLETE]` — quantity and account type unconfirmed since 9/10. Nothing on this card is executable until Will confirms them.

---

## 1. Live pull (SCREENING only): Saturday, so the 2026-09-25 Fri close is the freshest close

| item | value | source + time |
|---|---|---|
| TLT | **$79.32** (−0.13% on 9/25) | `FORGE/tools/market-data/fetch.py price TLT`, pulled 2026-09-26 15:09 ET; as-of 2026-09-25 close |
| Oct-16 82P, **SCREENING quote** (vendor feed, 9/25 close basis, bid/ask undated) | **bid 3.00 / ask 3.10 / mark 3.05** · spread 3.28% · IV 17.63% · OI 37,042 · vol 1,149 · last trade 9/25 15:49 · no quote defect | `AGENTS/TERRY/scripts/chain_fetch.py TLT 2026-10-16 --type put --no-cache`, 15:09 ET 9/26 |
| moneyness | **ITM by $2.68** (TLT must rise **+3.38%** to reach $82) | arithmetic on the two rows above |
| intrinsic ×2 | $536 | 2.68 × 200 |
| screening value ×2 at the vendor bid (**not proceeds**) | **$600** (extrinsic at the bid $0.32/ct ⇒ **$64** of time value) | 3.00 × 200 |
| screening value vs cost $336 | **+$264 / +78.6% at the screening bid**, before the $1.30 contract fee (+ Options Fee) | Fidelity online options $0.65/contract (fidelity.com/trading/commissions-margin-rates, read 2026-09-26) |
| sessions to expiry | **15** (Mon 9/28 → Fri 10/16) | calendar |

⚠️ **Every option price on this card is a SCREENING quote. None of them is proceeds.** Source: a vendor feed on the 9/25 close basis with an undated bid/ask (construction rule #14 MOMENT property). The tool's own banner says bid/ask age cannot be known from this feed, and its bid read ~10% high against the broker on 9/11. **Executable proceeds come only from Fidelity's live chain on the day of the sale.** Every $ figure below derived from these quotes ("~$600", "+$264", "~$64 time value") is screening arithmetic.

---

## 2. What sits between now and Oct-16

- **No registered management rule and no gate on this leg.** DOCKET names it once, as a consequent: **the 2026-10-01 row (FR2004 print)** says BOND's September-4 kill rule is *"A THESIS-KILL RAIL ON THE DURATION SHORTS (exit all duration shorts)"* and that *"the TLT Oct-16 82P ×2 (NO RULING) and TBT 10 sh do not"* expire before that print. ⚠️ **That rule's bucket is unresolved: WQ-291 is HELD** until BOND presents the exact kill rule (Will 2026-09-26 15:04). **If it fires on 10/1 and Will adopts it, the exit it calls for is choice A below.** This card does not grade, adopt or pre-empt it.
- Rates events inside the window: **September NFP Fri 10/2 ~08:30 ET** (DOCKET row; date INFERRED from the BLS first-Friday convention, LABOR confirms). **September CPI: date UNVERIFIED by this desk** (usually mid-month; could land before 10/16). Next FOMC: UNVERIFIED by this desk, not assumed inside the window.
- **Book context, not a rule:** the same duration-short bet is also held as **004 TLT Sep-30 77P ×20** (expires Wed 9/30, ~$20–80) and **TBT 10 sh**. Will **accepted the book's concentration in writing, WQ-297 A, 2026-09-25 14:16 ET**. This card changes nothing about that.
- **Driver (construction rule #23, informational — no add is proposed):** the 9/23 move that took this put ITM was **real-yield-led** (DFII10 +13bp, breakevens not leading; SIG-W-20260924-009, Q1 map). Nobody underwrote a driver for this leg, so there is no card driver to test against. #23 binds only an ADD, and none is on the table.

---

## 3. The choices (management only — each is Will's; none is a proposal to trade)

| # | choice | what you get | what you give up | forward max loss from here |
|---|---|---|---|---|
| **A** | **HARVEST: sell to close ×2 before expiry** | ~$600 **screening** value at the 9/25 vendor bid (+$264 vs cost). Real proceeds = Fidelity's live bid on the day, less $1.30 + Options Fee. **The broker question in §4 disappears.** | Any further TLT fall; ~$64 of time value is captured, not lost | $0 after the fill |
| **B** | **HOLD TO EXPIRY and let Fidelity's process act** | Full intrinsic at the 10/16 close if TLT < 82, **delivered by a mechanism the desk cannot describe** (§4) | Time value decays to 0 (~$64 at today's bid) | **~$600** (the full screening value) if TLT closes ≥ $82.00 on 10/16. **If ITM, the published §4 costs apply:** a close that Fidelity places at the Rep-Assisted rate (**$32.95 + $1.30 = $34.25** on ×2), or **the whole intrinsic** if Fidelity instructs the OCC not to exercise. Which one applies is the §4 question. |
| **C** | **HOLD, then SELL TO CLOSE by the dated decision point** (hybrid) | Keeps the duration exposure for ~13 more sessions. Still never meets the expiry process. | Time value bleeds through 10/14 | ~$600 (screening) if TLT rallies ≥3.4% before you sell. $0 once sold. |
| **D** | **"Do Not Exercise" instruction** | Nothing. Fidelity: DNE *"the intrinsic value of the option is forfeited, resulting in a total loss on the value of the option if the contract is not closed by the customer prior to expiration"* (Fidelity learning center, "Managing and monitoring options expirations", read 2026-09-26) | **Everything ITM.** | **Dominated while ITM. Listed only so it is never chosen by default.** |

**The dated decision point:** **Wed 2026-10-14, by the close.** That leaves Thu 10/15 and Fri 10/16 as two full sessions to close in an orderly way if the answer is A or C. **Hard backstop: Fri 10/16 before the 16:00 ET close.** Fidelity's own deadline for a customer to block an auto-exercise is **published twice, and the two differ: 16:15 ET** on the auto-exercise web page, **16:20 ET** in the Options Agreement (§4). Use 16:15 until Fidelity answers. That deadline matters only for D, which is dominated. **Fidelity publishes no time for a close it places itself (§4). Under A or C, close well before the final hour; do not wait for 16:00.**
**First action, before any choice:** Mon 9/28, Will asks Fidelity the §4 question.

**Desk read (not a ruling):** A vs C is a **thesis** question: does Will want 15 more sessions of this duration-short exposure? That belongs to Will and to BOND/HENRY, not to TERRY. The **structure** question is TERRY's, and its answer is the same under A and C: **B is the only branch that runs through an unknown, and it buys nothing that C does not also buy, except the last two sessions of exposure.**

---

## 4. ⛔ The named UNKNOWN — broker mechanics at expiry, in an IRA, ITM, no shares

**UNKNOWN to this desk:** what Fidelity does, in **this account**, with a long put that is ITM at the 10/16 close when the account **holds no TLT shares**: **auto-exercise · close it out · let it lapse.** Narrowed 16:0x ET: the published policy (below) lists the actions Fidelity **may** take. What remains UNKNOWN is **which** action it takes in this account, **when** it takes it on 10/16, and **what it costs**.

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

**Why it matters in dollars (screening basis):** exercising 2 contracts **sells 200 TLT at $82 = $16,400** in an account that, per the published policy, cannot be short. The screening intrinsic is ~$536. The published branches cost different amounts:
| branch Fidelity may take | cost to Will vs selling online himself ($1.30 + Options Fee) |
|---|---|
| Fidelity closes the puts (Rep-Assisted) | **+$32.95** per ticket, on a screening value of ~$600 (~5.5%). Plus whatever price Fidelity's order gets |
| Exercise, then Fidelity buys in the short | exercise is commission-free. The buy-in is an unsupported-position close, **rate NOT stated**; possible short-interest fees. **The buy-in price is the risk:** if it happens after the close or on Monday 10/19, a weekend gap runs against Will |
| Fidelity instructs the OCC not to exercise | **the whole intrinsic (~$536 screening)**. Total loss of the in-the-money value |

**The one question Will asks Fidelity** (narrowed to handling, timing and costs, per Will 15:54 ET; phone 800-544-6666 or chat; the same question word for word on the HBAN card):
> *"Please confirm that my account ending [____] is a Traditional IRA holding 2 long TLT Oct-16-2026 $82 puts and 2 long HBAN Oct-16-2026 $16 puts, and no shares of either. If either put is in the money on Friday 10/16, which of the actions in your Options Agreement will you take in this account (let it auto-exercise and then close out the resulting short stock, sell the puts yourself, or instruct the OCC not to exercise them), and at what time that day? What is my own deadline that day to sell them to close online, and to give a do-not-exercise instruction (your web page says 4:15 p.m. ET, your Options Agreement says 4:20 p.m.)? What exactly would I be charged if you act instead of me: the $32.95 Rep-Assisted commission plus 65¢ per contract, charged per ticket or per line, and any buy-in or short-interest fee?"*

⚠️ **The answer is account-specific and it is Will's to get.** Fidelity's published policy reserves three actions and chooses none of them in writing. Nothing on this card substitutes for Fidelity's answer. TERRY quotes only what it read, on the date it read it. **The simplest way to avoid all three branches is published by Fidelity itself:** *"the put must be sold prior to expiration"* (choice A or C).

---

## 5. Day colour — root rule #6 as it applies to a SALE

- **Root rule #6** (*"puts on green days, calls on red days"*) is written for **buying** convexity. Its proxy question (`RISK_RULES.md` § Breaking root rule #6) is *"am I paying up for convexity?"*
- For **closing** a long put, the same proxy runs in reverse: **sell the put on a RED day for TLT** (TLT down, puts bid). The question becomes *"am I selling convexity cheap?"*
- **Measured stake:** the put is ITM by $2.68 and carries **$0.32/ct of time value at the 9/25 screening bid (~$64 on ×2)**. The day's colour moves the sale price mostly through **delta** (the TLT move itself), not through vol. The convexity the rule protects is at most ~$64 here.
- ⇒ **A green-day sale is a break of the inverted rule and needs the direct measurement on the card before the fill** (RISK_RULES § Breaking root rule #6). "The date is close" is a chase and never a reason. Under C, a red day between now and 10/14 is the natural window. On **10/16 itself**, the break test is met by construction: the alternative is the §4 unknown, and that is a measured structural risk, not urgency. **Write the figures anyway.**

---

## 6. What Will must confirm
1. **Quantity is still ×2** and nothing traded on this contract since 9/10 (WQ-274 ①⑤).
2. **The account is the Traditional IRA** (the mirror says INFERRED).
3. **Fidelity's answer to the §4 question** (handling · timing · costs, with the account-type confirmation inside it).
4. **A, B or C** by Wed 10/14. **WQ-302 stays OPEN until items 1, 2 and 4 are in** (Will 15:54 ET). D is listed only as the choice never to make by default.

---
**APPROVAL REQUIRED — Will must approve/reject before execution.** This card proposes no trade. It lays out the management choices on a held leg, per WQ-292 (*"this authorizes preparation, not trades"*). `$0` moved · no order · no gate or threshold moved anywhere. — TERRY

*Card-ID note: `MGMT-` is deliberately not a `TRY-` id. A `TRY-` id would enroll the leg in `SETUPS.tsv`, and that ledger is at its rotate tier with a rotation owed first (STATUS 2026-09-25). The registry row lives in `setups/INDEX.md`.*

---

## ⑦ FILL RECORD + RE-READ AT ×1 — 2026-09-28 (recorded 18:2x ET; PROME packet `inbox/processed/2026-09-28_from-PROME_will-fills-9-28-record-on-cards.md`; source `PROME/reports/2026-09-28_will-fills-receipt.md`)

**Fill (Will's hand, root rule #5):** **1 of 2 SOLD @ $3.60** limit Day. Order 09:43:29 ET, filled 09:47:23 ET, **net $359.34**; the account is not named in the paste (FORGE D-61). ⇒ **×1 OPEN.** ANVIL's derivation (FORGE row, broker lot method UNKNOWN): **≈ +$191.67** vs a $167.68/ct average basis; remaining ×1 basis ≈ $167.68.
**Sold before any A/B/C choice** (WQ-292 / WQ-302, due Wed 10/14). In effect it was choice A applied to half the line. **Recorded, not graded.**

**Does the choice set change at ×1? The members do not. Their weights do.**
| | at ×2 (card as built) | at ×1 (now) |
|---|---|---|
| choices | A harvest · B hold to expiry · C hold then sell by 10/14 · D dominated | **same four.** The one option ×2 had and ×1 lacks is a **split** (sell one, hold one), and Will has just used it. ×1 is indivisible. |
| B's broker-cost drag if Fidelity acts (Rep-Assisted $32.95 + $0.65/ct, §4) | ~5.5% of the ~$600 screening value | **~11%** of ~$300 (9/25 screening bid 3.00 × 100) — **doubles in relative terms** |
| exercise if ITM and unsold | −200 TLT (~$16,400) in an account that cannot be short | **−100 TLT (~$8,200)** — the same §4 unknown, at half the size |
| forward max loss | the full screening value, ~$600 | **~$300** (screening; TLT closed $78.62 on 9/28 per `fetch.py`, so ~$3.38 ITM, for scale only; no quote re-read) |

⇒ **The desk read strengthens and does not change:** B is still the only branch that runs through the unknown, and at ×1 its cost share doubles. **A vs C remains Will's thesis call.** Decision point unchanged: **Wed 10/14 close**, backstop Fri 10/16 before 16:00 ET.
**§4's Fidelity question:** read **"1 long TLT Oct-16-2026 $82 put"** in place of "2". The HBAN half stays ×2. WQ-302 stays OPEN (PROME's row).

---

## ⑧ POINTER 2026-10-01 16:2x ET — the decision moved to the EXIT CARD `MGMT-DURSHORT-EXIT-WQ291`
BOND's Sept-4 thesis kill was MET on the 10/1 FR2004 release (3–6Y dealer net +$12.093B vs the +$8.6B bar; BOND packet `b3ef61cf1`). BOND recommends exiting all duration shorts. **The exit card is `setups/DURATION-SHORTS_exit-card_WQ291_2026-10-01.md`** — desk lean: choice **A here (harvest), executed Fri 10/02**: sell to close ×1 at Fidelity's bid, floor intrinsic − $0.10, from ~09:45 ET, by 15:00 ET, alongside TBT 10 sh. Live 16:19 ET: TLT $77.71 ⇒ $4.29 ITM; vendor 82P 4.20 / 4.40 (screening); Fidelity $4.25. Time value at the bid **−$0.09** — the §5 day-colour stake is now measured at ≈ $0, so a green-day sale meets the break test on the figures (re-confirm on Friday's Fidelity screen). §4 (broker mechanics, D-60) is unchanged and is avoided entirely by the sale. The Wed 10/14 decision point and the 10/16 hard backstop stand until Will rules.

## ⑨ POINTER 2026-10-07 Wed 22:0x ET — re-marked on the EXIT CARD, not here

Will's WQ-357 **LATER** (10/3 21:08 ET) is recorded and the ×1 is re-marked at tonight's close on `setups/DURATION-SHORTS_exit-card_WQ291_2026-10-01.md` (ADDENDUM 2026-10-07): TLT $77.15 · 82P intrinsic $4.85, vendor 4.75 / 4.95 (time value at the bid −$0.10) · path C (hold, then sell by Wed 10/14) is the live path · CPI is 08:30 ET on 10/14 itself. **This card's A/B/C/D set and § 4 (D-60) are unchanged; WQ-302's 10/14 decision and 10/16 16:00 backstop stand.** `$0` MOVED.
