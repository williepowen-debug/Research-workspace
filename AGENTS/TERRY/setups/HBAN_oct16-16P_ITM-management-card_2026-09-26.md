# POSITION-MANAGEMENT CARD — HBAN Oct-16-2026 $16 PUT ×2 (held, IN THE MONEY) — what the 7/18 "ride to expiry" ruling means now
**Date:** 2026-09-26 Sat, written 15:1x ET (`date` 15:11:18 ET) · **Card ID:** `MGMT-HBAN16P-OCT16` (management-only, not a `TRY-` entry card; see foot)
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

## 1. Live pull — Saturday, so the 2026-09-25 Fri close is the freshest close

| item | value | source + time |
|---|---|---|
| HBAN | **$15.64** (+2.16% on 9/25) | `fetch.py price HBAN`, 2026-09-26 15:09 ET; as-of 9/25 close |
| Oct-16 16P | **bid 0.45 / ask 0.80 / mark 0.62** · **spread 56%** · IV 39.84% · OI 14,129 · vol 161 · **last trade 9/24 15:58** (not a 9/25 print) · no quote-defect flag on this strike | `chain_fetch.py HBAN 2026-10-16 --type put --no-cache`, 15:09 ET 9/26 |
| chain quality | 🟠 NONMONO 2 of 6 rows (33%) on the 13 and 14 strikes, both NOBID. **The strip is thin.** Trust the 16 strike (OI 14,129) more than its neighbours. Still re-pull at the broker. | same pull |
| moneyness | **ITM by $0.36** (HBAN must rise **+2.30%** to reach $16) | arithmetic |
| intrinsic ×2 | $72 | 0.36 × 200 |
| value ×2 at the bid | **$90** (time value at the bid ~$0.09/ct ⇒ ~$18) | 0.45 × 200 |
| vs cost $192 | **−$102 at the bid** | |
| commission to close ×2 | **$1.30** (+ small regulatory fees) | Fidelity: *"$0.65 per contract"* (fidelity.com/trading/commissions-margin-rates, read 2026-09-26) |
| sessions to expiry | **15** (Mon 9/28 → Fri 10/16) | |

⚠️ **SCREENING marks** (construction rule #14; the feed cannot date the bid/ask). **At a 56% spread the mid is not a fill.** Any real price comes from the Fidelity chain on the day.

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
| value ×2 | "~$20 mark" | **~$90 at the bid** ($72 intrinsic) |
| commission ≈ proceeds? | yes, *"commission ≈ proceeds → do NOT pay to close"* | **no. $1.30 to close against ~$90 of proceeds (~1.4%)** |
| what "rides to expiry" meant | a lapse to $0 at expiry, with zero effort | **not a lapse if it stays ITM. See §4.** |

**What the letter implies now (TERRY's reading, not a re-ruling):**
1. **"Rides to expiry" still binds.** No close, no roll, no add. Nothing on this card overrides it.
2. **"Do not pay to close" no longer describes the economics.** Closing an ITM long put **receives** money. The ruling's concern was commission eating the proceeds, and at today's quote the proceeds are about 69× the commission. **The premise failed. The letter did not change.**
3. **"Zero effort" is no longer guaranteed.** The ruling assumed the put would expire worthless, which needs no broker action. **If HBAN closes below $16.00 on 10/16, the put reaches Fidelity's auto-exercise process ITM** (Fidelity: *"$0.01 or more in the money … will be automatically exercised"*) **in an account with no HBAN shares.** What happens then is the §4 UNKNOWN. **The ruling did not consider that branch, because on 7/18 it was far from reachable.**
4. **The letter does NOT call for a Do-Not-Exercise instruction.** DNE forfeits the intrinsic (Fidelity: *"the intrinsic value of the option is forfeited, resulting in a total loss on the value of the option if the contract is not closed by the customer prior to expiration"*). Reading "ride to expiry" as "block the exercise" would turn ~$72 of intrinsic into $0. **TERRY does not read it that way, and neither should a default.**

**What changes ONLY if Will re-rules** (listed, not recommended; the ruling is Will's and only Will moves it):
| option | effect |
|---|---|
| **R-A: permit a sell-to-close before expiry** | Captures ~$90 at the 9/25 screening bid (−$102 vs cost instead of up to −$192). Removes the §4 branch entirely. **Costs one ticket and a 56%-wide spread**: work a limit order, never the market. |
| **R-B: ride, but close on 10/16 if still ITM** | Keeps the ruling's spirit (no effort unless the exercise branch is live) and never meets the expiry process. Needs one look on 10/16 before 16:00 ET. |
| **No re-rule** | The letter stands. If HBAN ≥ $16.00 at the 10/16 close, it lapses to $0 exactly as ruled (**forward max loss ~$90, the remaining mark**). If HBAN < $16.00, **Fidelity's process decides**, per §4. |

**The dated decision point:** **Wed 2026-10-14, by the close**, if Will wants R-A or R-B in place with two sessions to spare. **Hard backstop: Fri 10/16 before the 16:00 ET close.** Fidelity's call-in deadline to block an auto-exercise is **16:15 ET on the last trading day** (fidelity.com/options-trading/options-auto-exercise-rules, read 2026-09-26). That deadline matters only for DNE, which the letter does not call for.

---

## 4. ⛔ The named UNKNOWN — broker mechanics at expiry, in an IRA, ITM, no shares

**UNKNOWN to this desk:** what Fidelity does, in **this account**, with a long put that is ITM at the 10/16 close when the account **holds no HBAN shares**: **auto-exercise · close it out · let it lapse.**

**What Fidelity's own pages say** (read 2026-09-26 via WebFetch; no page date shown on any of them):
- Auto-exercise at ≥ $0.01 ITM (fidelity.com/options-trading/faqs and /options-auto-exercise-rules).
- DNE by phone before 16:15 ET on the last trading day. DNE forfeits the intrinsic (learning center, "Managing and monitoring options expirations").
- The IRA strategy list on the FAQ contains **no short-stock position** (⚠️ an inference from an omission, not a stated policy).
- **None of them says what Fidelity does when exercising a long put would create a short stock position in an IRA,** or whether it closes such positions on expiration day. **SEARCH-NOT-FOUND at Fidelity's public pages.**

**In dollars:** exercising ×2 **sells 200 HBAN at $16 = $3,200**, against no shares, in an account that (by inference) cannot be short. The value is the ~$72 intrinsic under any sane mechanism. **The risk is the path** (a buy-in price, a same-day close-out at the broker's time and price, or a short over the 10/16→10/19 weekend). **Small in dollars on this line. The same question is ~5× larger on the TLT 82P, so ask it once for both.**

**The one question Will asks Fidelity** (the same single question as on the TLT card, both lines in one call — 800-544-6666 or chat):
> *"In my Traditional IRA I hold long TLT Oct-16-2026 $82 puts (×2) and long HBAN Oct-16-2026 $16 puts (×2), and no shares of either. If they are in the money at the close on Friday 10/16, what exactly happens: do you auto-exercise them, close them out for me that day (and if so, at what time and how is the price set), or let them expire, and what is the latest time on 10/16 I can close them myself to avoid that?"*

⚠️ **The answer is account-specific and it is Will's to get.** TERRY asserts no Fidelity policy it has not read.

---

## 5. Day colour — root rule #6 as it applies here
- Rule #6 governs **buying**. It does not bind a leg the ruling says to hold, so **under the ruling as written it has nothing to act on.**
- **If Will re-rules to R-A or R-B**, the inverted proxy applies to the sale: **sell on a RED HBAN day** (puts bid). The convexity at stake is **~$18 of time value at the bid**, and the spread (56%) is a bigger cost than the day's colour. ⇒ **The execution discipline that matters here is a limit order inside a wide spread, not the day colour.** A green-day sale still gets its figures written on the card before the fill (RISK_RULES § Breaking root rule #6). On 10/16 itself, the §4 unknown is the measured reason.

---

## 6. What Will must confirm
1. **Quantity is still ×2** and nothing traded on it since 9/10 (WQ-274 ①⑤).
2. **The account is the Traditional IRA** (INFERRED on the mirror).
3. **Fidelity's answer to the §4 question** (one call covers both cards).
4. **Whether the 7/18 ruling stands as written or is re-ruled (R-A / R-B)**, by Wed 10/14. Silence = the letter stands, and the §4 branch stays live if HBAN is below $16 on 10/16.

---
**APPROVAL REQUIRED — Will must approve/reject before execution.** No trade is proposed, and the 7/18 ruling is not re-ruled here (WQ-292: *"this authorizes preparation, not trades"*). `$0` moved · no order · no gate or threshold moved. — TERRY

*Card-ID note: `MGMT-` is deliberately not a `TRY-` id. `SETUPS.tsv` is at its rotate tier with a rotation owed first (STATUS 2026-09-25). The registry row is in `setups/INDEX.md` beside the retired stub's row.*
