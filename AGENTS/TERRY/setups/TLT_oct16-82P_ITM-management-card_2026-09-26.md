# POSITION-MANAGEMENT CARD — TLT Oct-16-2026 $82 PUT ×2 (held, IN THE MONEY) — harvest vs hold into expiry
**Date:** 2026-09-26 Sat, written 15:1x ET (`date` 15:11:18 ET) · **Card ID:** `MGMT-TLT82P-OCT16` (management-only, not a `TRY-` entry card; see foot)
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

## 1. Live pull — Saturday, so the 2026-09-25 Fri close is the freshest close

| item | value | source + time |
|---|---|---|
| TLT | **$79.32** (−0.13% on 9/25) | `FORGE/tools/market-data/fetch.py price TLT`, pulled 2026-09-26 15:09 ET; as-of 2026-09-25 close |
| Oct-16 82P | **bid 3.00 / ask 3.10 / mark 3.05** · spread 3.28% · IV 17.63% · OI 37,042 · vol 1,149 · last trade 9/25 15:49 · no quote defect | `AGENTS/TERRY/scripts/chain_fetch.py TLT 2026-10-16 --type put --no-cache`, 15:09 ET 9/26 |
| moneyness | **ITM by $2.68** (TLT must rise **+3.38%** to reach $82) | arithmetic on the two rows above |
| intrinsic ×2 | $536 | 2.68 × 200 |
| value ×2 at the bid | **$600** (extrinsic at the bid $0.32/ct ⇒ **$64** of time value) | 3.00 × 200 |
| vs cost $336 | **+$264 / +78.6% at the bid**, before $1.30 commission | Fidelity online options $0.65/contract (fidelity.com/trading/commissions-margin-rates, read 2026-09-26) |
| sessions to expiry | **15** (Mon 9/28 → Fri 10/16) | calendar |

⚠️ **These are SCREENING marks** (construction rule #14 MOMENT property; the tool's own banner: bid/ask age is unknowable from this feed and read ~10% high on the bid vs the broker on 9/11). The price Will would transact at comes from the **Fidelity chain on the day**.

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
| **A** | **HARVEST: sell to close ×2 before expiry** | ~$600 at the 9/25 screening bid (+$264 vs cost). **The broker question in §4 disappears.** | Any further TLT fall; ~$64 of time value is captured, not lost | $0 after the fill |
| **B** | **HOLD TO EXPIRY and let Fidelity's process act** | Full intrinsic at the 10/16 close if TLT < 82, **delivered by a mechanism the desk cannot describe** (§4) | Time value decays to 0 (~$64 at today's bid) | **$600** (the full mark) if TLT closes ≥ $82.00 on 10/16. **PLUS whatever the broker mechanics cost** if it is ITM (§4). |
| **C** | **HOLD, then SELL TO CLOSE by the dated decision point** (hybrid) | Keeps the duration exposure for ~13 more sessions. Still never meets the expiry process. | Time value bleeds through 10/14 | $600 if TLT rallies ≥3.4% before you sell. $0 once sold. |
| **D** | **"Do Not Exercise" instruction** | Nothing. Fidelity: DNE *"the intrinsic value of the option is forfeited, resulting in a total loss on the value of the option if the contract is not closed by the customer prior to expiration"* (Fidelity learning center, "Managing and monitoring options expirations", read 2026-09-26) | **Everything ITM.** | **Dominated while ITM. Listed only so it is never chosen by default.** |

**The dated decision point:** **Wed 2026-10-14, by the close.** That leaves Thu 10/15 and Fri 10/16 as two full sessions to close in an orderly way if the answer is A or C. **Hard backstop: Fri 10/16 before the 16:00 ET close.** Fidelity's own deadline to block an auto-exercise is **16:15 ET on the last trading day** (fidelity.com/options-trading/options-auto-exercise-rules, read 2026-09-26). That deadline matters only for D, which is dominated.
**First action, before any choice:** Mon 9/28, Will asks Fidelity the §4 question.

**Desk read (not a ruling):** A vs C is a **thesis** question: does Will want 15 more sessions of this duration-short exposure? That belongs to Will and to BOND/HENRY, not to TERRY. The **structure** question is TERRY's, and its answer is the same under A and C: **B is the only branch that runs through an unknown, and it buys nothing that C does not also buy, except the last two sessions of exposure.**

---

## 4. ⛔ The named UNKNOWN — broker mechanics at expiry, in an IRA, ITM, no shares

**UNKNOWN to this desk:** what Fidelity does, in **this account**, with a long put that is ITM at the 10/16 close when the account **holds no TLT shares**: **auto-exercise · close it out · let it lapse.**

**What Fidelity's own pages say** (all read 2026-09-26 via WebFetch; none carries a page date):
- *"Stock options that are $0.01 or more in the money at the time of expiration will be automatically exercised."* (fidelity.com/options-trading/faqs; same rule on /options-auto-exercise-rules)
- *"To prevent automatic exercises, please call us prior to 4:15 p.m. ET, on the last trading day of your options contract."* (/options-auto-exercise-rules)
- The IRA strategy list on the FAQ (*"Buy-writes, Selling covered calls, Rolling covered calls, Buying calls/puts, Selling cash covered puts, Long straddles/strangles, Spreads (up to 4 legs)"*) **contains no short-stock position.** ⚠️ That is an **inference from an omission**, not a stated policy.
- **None of the three pages says what happens when exercising a long put would create a short stock position in an IRA,** or whether Fidelity closes such positions on expiration day. **SEARCH-NOT-FOUND at Fidelity's public pages.**

**Why it matters in dollars:** an exercise of 2 contracts **sells 200 TLT at $82 = $16,400** in an account that (by inference) cannot hold short stock. The broker then has to do something: buy the shares back (when, at what price, over a weekend gap?), close the puts earlier that day, or refuse the exercise. **Each has a different cost, and the desk does not know which one applies.** The economic value is the intrinsic under every sane mechanism. The **risk** is the path: a short left open over the 10/16→10/19 weekend carries gap risk against you.

**The one question Will asks Fidelity** (phone 800-544-6666, or chat):
> *"In my Traditional IRA I hold long TLT Oct-16-2026 $82 puts (×2) and long HBAN Oct-16-2026 $16 puts (×2), and no shares of either. If they are in the money at the close on Friday 10/16, what exactly happens: do you auto-exercise them, close them out for me that day (and if so, at what time and how is the price set), or let them expire, and what is the latest time on 10/16 I can close them myself to avoid that?"*

⚠️ **The answer is account-specific and it is Will's to get.** Nothing on this card substitutes for it, and TERRY does not assert a Fidelity policy it has not read.

---

## 5. Day colour — root rule #6 as it applies to a SALE

- **Root rule #6** (*"puts on green days, calls on red days"*) is written for **buying** convexity. Its proxy question (`RISK_RULES.md` § Breaking root rule #6) is *"am I paying up for convexity?"*
- For **closing** a long put, the same proxy runs in reverse: **sell the put on a RED day for TLT** (TLT down, puts bid). The question becomes *"am I selling convexity cheap?"*
- **Measured stake:** the put is ITM by $2.68 and carries **$0.32/ct of time value at the 9/25 bid (~$64 on ×2)**. The day's colour moves the sale price mostly through **delta** (the TLT move itself), not through vol. The convexity the rule protects is at most ~$64 here.
- ⇒ **A green-day sale is a break of the inverted rule and needs the direct measurement on the card before the fill** (RISK_RULES § Breaking root rule #6). "The date is close" is a chase and never a reason. Under C, a red day between now and 10/14 is the natural window. On **10/16 itself**, the break test is met by construction: the alternative is the §4 unknown, and that is a measured structural risk, not urgency. **Write the figures anyway.**

---

## 6. What Will must confirm
1. **Quantity is still ×2** and nothing traded on this contract since 9/10 (WQ-274 ①⑤).
2. **The account is the Traditional IRA** (the mirror says INFERRED).
3. **Fidelity's answer to the §4 question.**
4. **A, B or C** by Wed 10/14. D is listed only as the choice never to make by default.

---
**APPROVAL REQUIRED — Will must approve/reject before execution.** This card proposes no trade. It lays out the management choices on a held leg, per WQ-292 (*"this authorizes preparation, not trades"*). `$0` moved · no order · no gate or threshold moved anywhere. — TERRY

*Card-ID note: `MGMT-` is deliberately not a `TRY-` id. A `TRY-` id would enroll the leg in `SETUPS.tsv`, and that ledger is at its rotate tier with a rotation owed first (STATUS 2026-09-25). The registry row lives in `setups/INDEX.md`.*
