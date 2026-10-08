# MANAGEMENT NOTES — USO $150C Oct-09-2026 ×2 · KRE $65P Dec-31-2026 ×2 (Fidelity IRA) — Will's 9/30 rolls

**Date:** 2026-10-01 Thu, written 11:11 ET (live reads `date` 11:09:14–11:09:58). **Spawn:** PROME `prome-2a`, Tier 1 (packet `inbox/processed/2026-09-30_from-PROME_sep30-lines-were-ROLLED-not-expired_fills-and-card-asks.md`, ask 3).
**Ids:** `MGMT-USO150C-OCT09` · `MGMT-KRE65P-DEC31` (management notes; no SETUPS rows).
**Terry verdict:** 🟡 **RECORDED — Will's own hand (root rule #5); sell-or-roll rails set, no action owed today.** These notes record the lines and their rails; they do not re-litigate the rolls.
**⏩ CURRENT for `MGMT-USO150C-OCT09` (2026-10-08 19:0x ET, ADDENDUM 2026-10-08 EVENING at the foot): NOT SOLD Thursday (broker Activity 10/2–10/8 shows no USO option row; FORGE `ef2bc83f1`) ⇒ ×1 HELD. The Fri 10/09 15:00 ET HARD STOP STANDS (WQ-366 DECLINE; DOCKET L605). Exercise is UNFUNDABLE: $15,000 against ≈ $11,421 cash. USO $147.58 [10/8c] ⇒ $2.42 out of the money. An earlier Friday sale is Will's choice; the card does not instruct it. No roll.** *(was, 10/8 09:5x: ~~desk lean SELL TODAY at Fidelity's bid~~ — not taken; Thursday is over. The 09:5x line, kept as the dated record:)* ~~desk lean SELL TODAY at Fidelity's bid — the move Will held for has arrived (USO $150.27, +4.42%, 11:03 — now IN the money; Friday exercise UNFUNDABLE and ≈ 53% likely if held). The Fri 10/09 15:00 ET stop is the fallback. No roll. Figures: ADDENDUM 2026-10-08 at the foot.~~ *(The "no action owed today" above is dated 10/1.)*
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** Cents from `FORGE/STATUS.md` (ANVIL `33bc8c293`); option quotes are vendor SCREENING marks — the live bid is Fidelity's (`RISK_RULES.md` durable finding 5b).

---

## A. USO $150C Oct-09-2026 ×2 — `MGMT-USO150C-OCT09`

| Item | Value | Source |
|---|---|---|
| Fill | **BOUGHT 9/30 ×2 @ $2.99, basis $599.33** — leg 2 of a net-debit roll out of the USO Sep-30 159C ×2 (sold @ $0.01, net $1.87 ⇒ −$919.46); limit $2.98 | FORGE (transcription rows 5–6) |
| Live 11:09 ET | USO **$148.26 (+1.78%)** ⇒ 150 strike **$1.74 out of the money**; vendor 150C bid/ask **3.55 / 3.65** (last trade 10:48) ⇒ ×2 ≈ $710 ⇒ ≈ **+$111 vs basis** (INFERRED) | `fetch.py`; `chain_fetch.py --no-cache` |
| Thesis / book | Oil — BRENT owns the thesis. New oil-call exposure on the "one oil bet" book; Will **accepted that concentration in writing 9/25** (WQ-297 A, `PROME/proposals/2026-09-25_wq297-298-RULED.md`). Beside the 37 USO shares (WQ-200: no rule, hand-managed) | FORGE; STATUS 9/25 block |

**Rail (sell-or-roll, `USER.md` 9/30 19:03 ET):**
- **Hard stop Fri 10/09 15:00 ET.** Sell at Fidelity's bid, or roll as one net-debit order.
- **Exercise path if held in the money:** a close above $150.00 ⇒ the IRA **buys 200 USO at $150 = $30,000** against ≈ $14,094 settled cash (FORGE header, derived) — it cannot fund it; Fidelity's handling **UNOBSERVED (D-60)**.
- **Roll form (construction rule #21: same strike, later expiry):** indicative today, buy at the ask and sell the Oct-09 at the bid: **Oct-16 150C** 5.00 / 5.15 ⇒ ≈ $1.60/ct (≈ $320 for two) · **Oct-23 150C** 6.35 / 6.60 ⇒ ≈ $3.05/ct (≈ $610). Re-price at the order.
- **Root rule #6:** calls on red days — USO is **green today (+1.78%)**: the wrong colour to BUY a call leg, the right colour to SELL.

**Rules on the line, recorded and not re-litigated:** strike moved 159 → 150, so the 9/30 trade was not a construction rule #21 roll · forward max loss = remaining mark (construction rule #20) ≈ $710 ≈ **1.4× the $500 per-card cap** · ⚠️ **no P/L-keyed harvest (durable finding 9)** — suggested form if Will wants one: sell both at any Fidelity bid ≥ $5.98 (2× the $2.99 fill) · catalyst map: none registered on this line (BRENT owns oil's calendar).

## B. KRE $65P Dec-31-2026 ×2 — `MGMT-KRE65P-DEC31`

| Item | Value | Source |
|---|---|---|
| Fill | **BOUGHT 9/30 ×2 @ $1.68, basis $337.33** — leg 2 of a net-debit roll out of the KRE Sep-30 60P ×2 (sold @ $0.01, net $1.87 ⇒ −$451.48); limit $1.67 filled after $1.63 and $1.55 attempts were Verified Canceled | FORGE (transcription rows 1–4, 7–8) |
| Live 11:09 ET | KRE **$68.36 (−1.55%)** ⇒ 65 strike **$3.36 / 4.9% out of the money**; vendor 65P bid/ask **2.00 / 2.28** (13% wide, OI 83, last trade 9/30 15:13) ⇒ ×2 ≈ $400 at the bid ⇒ ≈ **+$63 vs basis** (INFERRED) | `fetch.py`; `chain_fetch.py --no-cache` |
| Fidelity's 9/30 mark | $0.01 post-close — **not a valuation (FORGE D-67)**; the line is not −99% | FORGE |
| Thesis | Regional banks — REGINALD owns | — |

**Rail (sell-or-roll):** hard stop **Thu 12/31 15:00 ET** (91 days). Exercise path if held in the money: the IRA **sells 200 KRE at $65 = $13,000 short** — Fidelity's handling UNOBSERVED (D-60). Roll form, when the time comes: 65 strike, a later expiry, same two. ⚠️ **Liquidity:** a $0.28-wide market on 83 open interest — crossing it costs ≈ $56 on two; work a limit, never a market order.

**Recorded against this desk's own card, not re-litigated:** the add went on the same day `setups/KRE_add-puts_conditional-card_2026-09-30.md` read **CONDITIONAL — NO FILL** (REG-T-01 un-fired · X1 CLOSED · construction rule #23 driver unnamed). Strike moved 60 → 65: not a construction rule #21 roll. Root rule #6: KRE was red on the day of a put BUY (9/30 −0.56%); it is red again today (−1.55%) — right colour to SELL, wrong to add. Forward max loss ≈ $400 (under the $500 per-card cap). ⚠️ No P/L-keyed harvest (durable finding 9) — suggested form if Will wants one: sell both at any Fidelity bid ≥ $3.36 (2× the $1.68 fill). Construction rule #18: the Q3 regional-bank prints (dates from company IR, REGINALD's clock) move this sector a median 2–3% (0 of 32 ≥ 10%) — a print alone rarely reaches a 4.9%-OTM strike; the 91-day tenor, not a print, is what this line holds.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed; any sale or roll is his order).

---

## ADDENDUM 2026-10-01 12:5x ET: `MGMT-USO150C-OCT09` is now ×1 (Will sold 1 of 2). § A above stands as written for ×2

**Source:** PROME packet `inbox/2026-10-01_from-PROME_10-01-partial-sales-QQQ740P-x4-USO150C-x1.md`; mirror `FORGE/STATUS.md` (ANVIL `dac72b4ae`). The sale was Will's hand and his standing practice, not a deviation.

| Item | Value | Source |
|---|---|---|
| 10/1 sale | **1 @ $3.92, proceeds $391.34, realized +$91.67** vs broker basis $299.67. Fill time not shown | FORGE Pending row 2 |
| Left | **USO $150C Oct-09 ×1, basis $299.66** | FORGE |
| Live 12:52 ET | USO **$148.33 (+1.83%)** ⇒ 150 strike **$1.67 out of the money**; vendor 150C bid/ask **3.30 / 3.50** (last trade 12:12). One at the bid ≈ $330 ⇒ ≈ **+$30 vs basis** (INFERRED). Fidelity mark $3.30 `[≤12:24]` agrees | `fetch.py`; `chain_fetch.py --no-cache` (SCREENING) |
| His sale vs now | $3.92 against a $3.30 bid: the contract he sold fetched ≈ $62 more than the one he kept would now | arithmetic, not a grade |

**Rail at ×1 (unchanged in form):**
- **Hard stop Fri 10/09 15:00 ET.** Sell at Fidelity's bid, or roll as one net-debit order.
- **Exercise path, re-stated for ×1:** a close above $150.00 means the IRA **buys 100 USO at $150 = $15,000**. Cash is $14,147.60 settled + $2,245.00 pending ≈ **$16,392.60** (FORGE `[10/1 ≤12:24]`). ×1 is roughly coverable where ×2 ($30,000) was not, **but only if the cash is not spent first**: a roll of the QQQ 740P ×4 (≈ $2.5k) or of the Monday 735P ×5 would bring it back under $15,000. It would also turn the option into 100 shares beside the 37 already held (WQ-297 A, the one-oil-bet flag). Fidelity's handling is still **UNOBSERVED (D-60)**. ⇒ The sell-or-roll rail still governs; exercise is not a planned path.
- **Roll form (construction rule #21), indicative 12:52:** **Oct-16 150C** 4.75 / 4.95 ⇒ $4.95 − $3.30 = **$1.65 net (≈ $165 for one)**. Re-price at the order.
- **Root rule #6:** USO is **green (+1.83%)**, the right colour to SELL a call and the wrong colour to BUY one (a roll's buy leg).
- **Per-card cap:** forward max loss = the remaining mark ≈ **$330 (0.66× the $500 cap)**, which is now inside it (×2 was 1.4×).
- ⚠️ **Harvest:** there is still no P/L-keyed harvest rule (durable finding 9). The suggested form, re-stated for ×1: sell at any Fidelity bid ≥ $5.98 (2× the $2.99 fill). It is a suggestion, not a gate.

**APPROVAL REQUIRED. Will must approve or reject before execution** (no action is proposed).

---

## ADDENDUM 2026-10-01 16:2x ET: `MGMT-USO150C-OCT09` ×1 refreshed to Will's 16:15 ET end-of-day capture — the strike is now AT THE MONEY and the exercise cash is thinner

**Source:** `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md` (Fidelity positions, after the close). ×1, basis $299.66, unchanged.

| Item | Value | Basis |
|---|---|---|
| USO close | **$150.02 (+2.99%)** ⇒ the 150 strike is **$0.02 IN the money** (Fidelity shows USO $150.00) | `fetch.py`, 16:19 ET; broker view |
| Fidelity last | **$4.15 ⇒ $415.00; +$115.34 / +38.49% total; +$125.00 today** | broker view |
| Vendor 150C Oct-09 bid/ask | **4.20 / 4.50** (16:23:01; 6.9% wide, OI 1,435) | `chain_fetch.py --no-cache --legs 150`, SCREENING ONLY |
| Indicative roll (construction rule #21) | **Oct-16 150C** 5.70 / 6.00 ⇒ $6.00 − $4.20 = **$1.80 net (≈ $180)** | screening; re-price at the order |

**The exercise path tightened (this is the change that matters):**
- A close **above $150.00 on Fri 10/09** ⇒ the IRA **buys 100 USO at $150 = $15,000**.
- Cash now: **$14,147.60 money market + $1,377.10 pending ≈ $15,524.70** — the pending fell **$867.90** today because the QQQ 740P roll to Oct-02 drew on it. **Headroom over $15,000 is now ≈ $525** (was ≈ $1,393 at 12:5x).
- The 12:5x addendum's warning came true in part: *"a roll of the QQQ 740P ×4 … would bring it back under $15,000."* It did not go under, but **one more QQQ roll (Friday's Oct-09 form ≈ $1.7k, or Monday's 735P ×5) would.**
- Exercise would also add 100 shares to the 37 already held — WQ-297 A's one-oil-bet concentration. Fidelity's handling: **UNOBSERVED (D-60)**. ⇒ **Exercise is not a planned path; the sell-or-roll rail governs.**

**Root rule #6:** USO was **green (+2.99%)** — the right colour to SELL a call, the wrong colour to BUY one. **Harvest suggestion (≥ $5.98, 2× fill):** the line is at $4.15–4.20, ~70% of the way there; still a suggestion, not a rule (durable finding 9). **Per-card cap:** forward max loss ≈ $420 at the bid ≈ 0.84× the $500 cap — inside it.

**Unchanged:** hard stop **Fri 10/09 15:00 ET** — sell at Fidelity's bid or roll as one net-debit order. `MGMT-KRE65P-DEC31` (§ B) not re-read here; Fidelity shows KRE 65P ×2 at $1.60 / $320.00 (−$17.33), KRE $69.95 (+0.73%).

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed).

---

## ADDENDUM 2026-10-02 Fri 09:47–09:50 ET: `MGMT-USO150C-OCT09` ×1 re-marked after oil's drop (PROME `prome-70`). The text above stands as written

**Positions as of the 10/1 capture. Quotes are SCREENING** (yfinance `--legs 150`, leg gate PASS, 9% wide; Fidelity's bid governs).

| Item | Value |
|---|---|
| USO | **$144.38 (−3.76% vs $150.02)** at 09:47 · $144.64 (−3.59%) at 09:50 ⇒ the 150 strike is **≈ $5.5 (3.7–3.9%) out of the money** |
| 150C Oct-09 bid / ask | **1.45 / 1.59** (both pulls) ⇒ one at the bid ≈ **$144.35 net ⇒ ≈ −$155 against $299.66** |
| Roll to the 150C Oct-16 | ask 2.95 ⇒ **$1.50 net ≈ $150** |
| Exercise path | A close above $150 now needs ≈ +3.8%. **The 10/1 cash-headroom worry (≈ $525 over $15,000) eases a lot**, so a QQQ roll today no longer threatens the funding of a likely exercise |

**Lean: no action owed today.** USO is **red**: the wrong day to *sell* a call, the right day for a roll's *buy* leg (root rule #6). BRENT is attributing this morning's drop now, and that attribution is the input that matters. Sell or roll by **Fri 10/09 15:00 ET**. The ≥ $5.98 harvest suggestion is now out of reach. KRE 65P (§ B) wasn't re-read.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed).

### ADDENDUM-2 2026-10-02 Fri 09:53 ET: BRENT's oil-drop attribution folded into `MGMT-USO150C-OCT09` (the 09:47–09:50 addendum stands)

**Input:** `PROME/inbox/2026-10-02_from-BRENT_10-2-oil-drop-attribution.md` (`5ddb2dfea` + `1ffe243cf`).
- **BRENT's attribution:** a Reuters story, carried by one wire and three anonymous sources, that EU governments discussed a **PROPOSAL** to release 50M bbl of diesel plus 50M bbl of IEA crude. **No decision was taken**, and the European Commission's own statement carries no volume. A deal may be tied to a US commitment not to ban diesel exports.
- **Timing:** the drop was a diesel-led step at 03:50–04:05 ET. Payrolls was not the driver.
- **BRENT's lines:** Nov ULSD crack $101.42 (leg A is $11.26 above $90.16), B1 not fired, and nothing fires. BRENT's WQ-192 STAND DOWN holds.

| Live 09:53:33 (SCREENING; Fidelity governs) | Value |
|---|---|
| USO | **$145.08 (−3.29%)** ⇒ the strike is **$4.92 (3.4%) out of the money** |
| 150C Oct-09 bid / ask | **1.37 / 1.45** ⇒ one at the bid ≈ **$136.35 net ⇒ ≈ −$163 against $299.66** |
| Roll to the 150C Oct-16 | ask 2.81 ⇒ **$1.44 net ≈ $144** |

**What BRENT's read changes:** the drop rests on a **headline about a proposal, not a decided supply change.** Before the 10/9 stop the outcome can go either way:
- An **adopted volume** would be a fresh bearish step. BRENT watches leg A's distance.
- **No decision, or a rejection,** would leave room for this morning's drop to give back.

That makes the call a cheap, five-session option on the "no decision" outcome. It's worth ≈ $136 at the bid, against a $299.66 basis.

**Lean (unchanged in form, now with its reason):** **no sale today.**
- USO is red, which is the wrong day to sell a call (root rule #6).
- Selling into a headline-driven low gives up the reversal path for ≈ $136.
- **Sell, don't roll, by Fri 10/09 15:00 ET at the latest.** Sell earlier on the first green USO session if Will wants the value banked. Sell on the spot if an EU volume is adopted, because that removes the reversal path.
- **A roll is not the desk's form here.** It adds ≈ $144 of cash to a line whose thesis owner holds STAND DOWN, with no fired trigger (durable finding 1). If Will rolls anyway, today's red tape is the right day for the buy leg.

**Exercise path:** remote, since it needs +3.4%. The 10/1 cash-headroom constraint no longer binds.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed).

### ADDENDUM-3 2026-10-02 Fri 10:42–10:5x ET: the G7 DECIDED a release ⇒ ADDENDUM-2's early-sell condition is graded MET. Lean changes to SELL TODAY (PROME doorbell 10:41; WALTER `SIG-W-20261002-009`; BRENT packet `inbox/processed/2026-10-02_from-BRENT_G7-release-ADOPTED-verified-read.md`)

**The fact (BRENT's verified read; primary text NOT opened by BRENT or TERRY):**
- After a videoconference Macron hosted on 10/2, the **G7 agreed to release up to 100M bbl of diesel plus crude over 4 months, with "a substantial diesel release within the first 20 days"**, coordinated by the IEA.
- **Sources:** NBC 10:22 ET (quoting the G7 statement), Bloomberg, Newsquawk, Macron on the record, and Trump: "Europe has just agreed…".
- **Not published:** the diesel/crude split and per-country volumes.
- **Unchanged:** the US diesel export-ban threat is not withdrawn.

**The condition, graded against its own words.** ADDENDUM-2 (09:53) wrote: *"Sell on the spot if an EU volume is adopted, because that removes the reversal path."* The reversal path it named was **"no decision, or a rejection."**

| Element | Fact | Read |
|---|---|---|
| A decision was taken | **YES.** "Agreed" and "decided" (G7 statement via NBC; Macron on the record) | The "no decision / rejection" path is gone |
| A volume | **up to 100M bbl** (a ceiling); diesel front-loaded in 20 days | A stated volume. The European diesel leg itself is not sized |
| "EU" | The decision is the **G7's**. It includes France, Germany and Italy, and Europe holds the diesel | A wording gap, not a substance gap: the body that decided is wider than the one the condition named |

⇒ **MET.** The decision removes exactly the path the condition was written to protect. I am NOT reading "EU, not G7" or "up to" as reasons it did not fire. That reading would keep the position on a technicality, and it is the comfortable reading, which is the one to check. ⚠️ **Verification gap:** the G7/Élysée text is unread at the primary. If it turns out that no decision was actually taken, this grade reverts.

**Live re-mark (SCREENING; Fidelity governs):**

| Item | Value |
|---|---|
| USO | **$142.93 (−4.73% vs $150.02)** at 10:42:10 (`fetch.py`) ⇒ the strike is **$7.07 (4.9%) out of the money**, 5 sessions left |
| 150C Oct-09 bid / ask | **1.26 / 1.36** (`chain_fetch.py --no-cache --legs 150`, PASS; last trade 10:23, so the quote is probably ~20 minutes old) |
| One sold at the bid, after the $0.65 fee | **≈ $125.35 ⇒ ≈ −$174.31 against $299.66** |
| Roll to the 150C Oct-16 (not the lean) | ask 2.67 ⇒ **$1.41 net ≈ $141** |

**Root rule #6, in figures (as done for the 82P).** USO is **red**, the wrong day to sell a call. The proxy asks: *am I selling convexity cheap?* Measured by backing out implied vol (Black–Scholes, r 4%, no dividend):
- the 150C's IV at the **10/1 close bid** (4.20, USO $150.02, 8 days) = **46.6%**;
- **now at the bid** (1.26, USO $142.93–143.50) = **43.5–45.7%**.
- ⇒ **The proxy is mildly CONFIRMED, not refuted.** Vol is about 1–3 points cheaper than yesterday's close. At a vega of ~$0.05 a point on this contract, that is **≈ $5–15 on the one contract**.

**So this is NOT a proxy-refuting break.** It is a **wrong-colour sale with a measured colour cost of ≈ $5–15**, made because the card's **pre-registered exit condition fired**:
- Durable finding 12: a fired exit is held, not re-litigated.
- Root rule #6 is a cost preference, and it does not override an exit. No hard guard is relaxed.
- "The window is closing" is not the reason. The 10/9 stop is a week away.
- Waiting for a green USO day to save ≈ $5–15 is a bet that the reversal path comes back, and the decision just removed it.

**Lean: SELL the 150C ×1 at Fidelity's bid TODAY** (limit at the bid; a $0.05 step toward it is enough on a 1,458-OI strike). **No roll:** BRENT holds STAND DOWN (WQ-192), no trigger has fired, and the roll's buy leg would pay ≈ $141 to keep a path that was just closed. The hard stop stays **Fri 10/09 15:00 ET** if Will declines.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-07 Wed 22:03 ET: `MGMT-USO150C-OCT09` ×1 — Will's WQ-366 DECLINE recorded; Friday re-marked at tonight's close (PROME `prome-0e`, Tier 1, C5 + DOCKET L605). The text above stands as written

**Ruling recorded (root rule #10).** WQ-366, Will's Decision Deck tap 2026-10-03 21:10 ET (doc `366-20261004011010023-wclrjd`), **DECLINE the early sell**, verbatim: *"I dont think I sell yet.  The news in Saudi arabia continues to get worse"*. Source: PROME packet `inbox/processed/2026-10-03_from-PROME_WQ-357-365-366-rulings.md`. ⇒ ADDENDUM-3's SELL-TODAY lean (10/2) is **declined, not withdrawn**; the call is HELD; the **Fri 10/09 15:00 ET stop STANDS** (DOCKET L605). **No new rail is added here.** Caveat that travels from ADDENDUM-3: its MET grade rests on the G7 release decision, whose statement neither BRENT nor TERRY has read at the primary.

**Position (capture received 10/7, Will's word "yes today", exact time UNKNOWN; `PROME/data/2026-10-07_broker-capture-TRANSCRIPTION.md`):** ×1, basis $299.66, last $0.26 ⇒ $26.00 (−$273.66). The $0.26 is a last trade at an unknown time, not a bid.

| Live read 21:45 ET (after the close; SCREENING, Fidelity governs) | Value |
|---|---|
| USO | **$143.91 close (−0.69%)** ⇒ the 150 strike is **$6.09 (4.2%) out of the money**, two sessions left |
| USO path since the decision was declined | 10/2 $147.37 · 10/5 $143.99 · 10/6 $144.91 · 10/7 $143.91 (yfinance closes). The tape has not priced a worsening |
| 150C Oct-09 bid / ask | **0.35 / 0.43** (IV 51.4%, OI 2,111, last trade 15:59; 20% wide). One at the bid ≈ **$34.35 net ⇒ ≈ −$265.31 against $299.66** |
| Model chance of finishing above $150 | **≈ 18%** (vendor IV, two sessions; needs about +4.2%) |

**What the 15:00 ET stop means at these marks** (MODEL, Black–Scholes at ~51%; shape, not price):

| USO at Fri 15:00 | 150C ≈ | What the stop does |
|---|---|---|
| unchanged ($143.91) | ≈ $0.00 (a cent or two, if any bid) | Recovers a few dollars at most. Its job is to keep the line from lapsing unattended, Will's standing practice |
| +3% (≈ $148.2) | ≈ $0.17 | ≈ $17 before the $0.65 fee |
| +5% (≈ $151.1) | ≈ $1.44 + | Sells the intrinsic before an exercise the account cannot fund (below) |

- **The exercise path got worse since 10/1:** a close above $150.00 ⇒ the IRA **buys 100 USO = $15,000** against **$12,993.82 cash − $1,572.64 pending ≈ $11,421** (capture) ⇒ **≈ $3,579 short of funding it** (on 10/1 the headroom was ≈ +$525). Fidelity's handling: **UNOBSERVED (D-60)**. It would also add 100 shares to the 37 held (WQ-297 A). ⇒ If USO is above $150 at 15:00 Friday, the sale at the stop is not optional in substance.
- **Earlier is Will's choice, not a card instruction** (L605): a USO-up session before Friday 15:00 sells a call into strength, the right colour for a call SALE (root rule #6 governs buys; selling a call on a red USO day fetches less).
- **No roll** (unchanged from ADDENDUM-2/3): BRENT holds STAND DOWN (WQ-192), no trigger has fired. Tonight's screening roll to the 150C Oct-16 would be 1.85 − 0.35 = **$1.50 net ≈ $150**.
- The Saudi news Will cited (WALTER `-003` Riyadh refinery fire 10/3, Houthi-claimed, operator-unconfirmed; `-014` FALCON Khurais-corridor FIRMS finding 10/4) is BRENT's to weigh; this desk does not re-underwrite oil.

**`MGMT-KRE65P-DEC31` (§ B), capture marks only, not re-read:** ×2 last $1.41 ⇒ $282.00 (−$55.33); KRE $68.89 close (−1.68%). Stop Thu 12/31 15:00 ET unchanged; C5 card due by Tue 12/29.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no new action is proposed; the 15:00 ET Friday sale is his order).

## ADDENDUM 2026-10-08 Thu, written 09:5x ET (`date` 09:54:30): `MGMT-USO150C-OCT09` ×1 re-marked at the open — lean SELL TODAY (C5; Will's direct session `terry-01`, sole TERRY writer, PROME-acked; completes the 09:00 pre-open memo's §0). The text above stands as written

**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD MOVED.** Vendor SCREENING marks (durable finding 5b): pulled **09:52:37 ET**, quotes' last trades **09:30–09:37** ⇒ ≈ 15 min old against the spot. **Fidelity's live bid governs.** Clock checked against two external HTTP `Date` headers 09:52:56 ET (agree to the second).

| Item | Value | Basis |
|---|---|---|
| USO | **$148.82** (09:52 ET) vs $143.91 [10/7c] = **+3.41%, GREEN** ⇒ **$1.18 below the strike** (pre-market $148.20 at 09:19, $149.46 at 08:51) | yfinance |
| Crude | `CLX26` $92.21 · `BZZ26` $104.49 (09:09 ET, single-vendor quotes, NOT settles); driver per BRENT 10/8: Hormuz leads, Isaias transient absent damage; **not an event-class arm, WQ-192 holds** | yfinance; BRENT memo `330999913` |
| 150C Oct-09 | **1.14 / 1.24**, last 1.21, IV 39.8%, OI 2,362, vol 187 (was 0.35 / 0.43 at the 10/7 close) | `chain_fetch.fetch_chain`, last trade 09:35 |
| Intrinsic / time value | **$0 / $1.14** — the whole bid is time value | arithmetic |
| ×1 at the bid, after $0.65 | **≈ $113.35 ⇒ −$186.31 vs $299.66** (INFERRED, not a fill) | arithmetic |
| 150C Oct-16 (roll leg) | 3.30 / 3.50, OI 6,467 ⇒ roll ≈ **$2.36/ct** (3.50 − 1.14) ≈ $237 incl. fees | screening |
| Oct-16 strike with ask ≤ the Oct-09 bid | **160C ask 0.90** (155C ask 1.75 does not qualify) ⇒ a strike change = a **NEW DEPLOYMENT** under construction rule #21, needs its own trigger | screening |

**Sell today vs the Fri 15:00 stop** (MODEL, Black–Scholes calibrated to the 1.19 mid at 32.1% on a trading-hour clock; shape, not price; spot and quote ≈ 15 min apart):

| At an unchanged USO ($148.82) | 150C ≈ |
|---|---|
| Now (screening bid) | $1.14 |
| Thu 14:30 | $0.84 |
| Fri 10:00 | $0.67 |
| **Fri 15:00 (the stop)** | **$0.10** |

| USO at Fri 15:00 | $148.00 | $149.50 | $150.00 | $151.00 | **$151.14** | $152.00 | $153.00 |
|---|---|---|---|---|---|---|---|
| 150C ≈ | 0.02 | 0.27 | 0.48 | 1.14 | **1.25** | 2.03 | 3.01 |

- **Holding to the stop beats selling now only if USO is at or above ≈ $151.1 at Fri 15:00 (+1.6% from here).** At an unchanged USO the stop forfeits ≈ **$104** of today's bid. Model chance of finishing above $150 ≈ 39%.
- **Hurricane Isaias landfall is forecast late Fri 10/9–early Sat 10/10 — AFTER this call's last trading minute.** The call cannot hold that event; only the shares and the VLO share carry it.
- **What WQ-366's DECLINE fixed (10/3 21:10 ET, verbatim "I dont think I sell yet. The news in Saudi arabia continues to get worse"):** it declined the 10/2 SELL-TODAY lean and HELD the call; the Fri 15:00 stop stands "unless Will says otherwise" (L605). **A Thursday sale is outside the DECLINE's content** — it neither forbids nor authorizes one; it is a new Will decision on new facts. **The reason Will held — worsening Mideast news — is the move that came overnight** (WALTER `-014`: tanker strikes spread to the central Gulf, casualties off Qatar; CENTCOM preparation reported, no decision).
- ⛔ **Exercise stays UNFUNDABLE:** a Friday close above $150.00 ⇒ the IRA buys 100 USO = $15,000 against ≈ $11,421 cash net of pending [10/7 capture]. **The sale is the plan; exercise is not.**
- **Root rule #6:** the sale is an EXIT — the rule governs buys and does not bind it; a green USO day is the favourable colour to SELL a call. **A roll's call buy today is wrong-colour (USO green), and the refuting measurement does not exist:** the Oct-16 150C's implied vol at the ask is **40.2% at USO $148.82 / 43.1% at $148.20** (trading-day convention) against the **42.6%** 10/7 red-day bar (reproduced exactly) — it straddles the bar inside the quote-age noise, so it does not refute the proxy ⇒ a roll today would be a chase, not a break. **⚠️ SUPERSEDED 11:03 ET — at the re-pull the same leg reads 34.9–37.4% (below the bar beyond the noise); see RE-PULL below.**
- **Roll: NONE** — no fired trigger (BRENT 10/8: not a new event-class arm; WQ-192 holds; durable finding 1); construction rule #21(b) (near the money, 100% extrinsic, decaying) argues for closing; the oil exposure stays via the 37 USO shares and the 1 VLO share.

**Desk lean: SELL the 150C ×1 TODAY at Fidelity's bid** (the sooner the less decay); the **Fri 10/09 15:00 ET stop stays the fallback.** The order is Will's (root rule #5).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

### RE-PULL 2026-10-08 11:03 ET (`date` 11:02:58; external `Date` 15:02:56 GMT agrees) — after a wifi outage; the 09:52 marks above are a dated record, NOT current

| Item | 11:03 value | vs 09:52 |
|---|---|---|
| USO | **$150.27 (+4.42% vs $143.91 [10/7c]) ⇒ $0.27 IN the money** | was $148.82, $1.18 OTM |
| 150C Oct-09 | **1.36 / 1.45**, last 1.42, vol 1,813; `chain_fetch.py --no-cache --legs 150` ⇒ ✓ usable two-sided (rc 0); last trade 10:47 (≈ 16 min old) | was 1.14 / 1.24 |
| Intrinsic / time value | $0.27 / $1.09 | was $0 / $1.14 |
| ×1 at the bid, after $0.65 | **≈ $135.35 ⇒ −$164.31 vs $299.66** (INFERRED) | was ≈ $113.35 |
| 150C Oct-16 (roll leg) | 3.45 / 3.65 ⇒ roll ≈ **$2.29/ct** (≈ $230 incl. fees); strike with ask ≤ the Oct-09 bid = 160C (0.90) ⇒ NEW DEPLOYMENT | was $2.36 |

- **Model** (calibrated to the 1.405 mid at 24.5%, trading-hour clock; shape, not price): at an unchanged USO the call is ≈ $1.18 at Thu 14:30, $1.04 at Fri 10:00, **$0.52 at the Fri 15:00 stop** ⇒ the stop forfeits ≈ $84. **Holding beats selling now only if USO is ≥ ≈ $151.4 at Fri 15:00 (+0.7%).**
- ⛔ **The exercise branch is now a coin flip:** model chance of a Friday close above $150 ≈ **53%** ⇒ the IRA buys 100 USO = $15,000 against ≈ $11,421 cash — **UNFUNDABLE.** A slipped stop is no longer a small risk.
- **Root rule #6 for a roll — the measurement now EXISTS:** Oct-16 150C implied vol at the 3.65 ask = **34.9% at USO $150.27 / 37.4% at $149.80** (trading-day convention) vs the **42.6%** 10/7 red-day bar ⇒ the structure is **cheaper** than on the clean-colour day, by more than the spot/quote-age noise. **A roll today would NOT be a chase on day-colour grounds** (it would need these figures re-taken on Fidelity's chain and written before the fill).
- **Roll lean stays NONE — now on the trigger, not the colour:** no fired trigger (BRENT 10/8: not a new event-class arm; WQ-192 holds; durable finding 1 — fresh capital only on a fired trigger); construction rule #21(b); the oil exposure stays via 37 USO + 1 VLO. If Will wants to keep the bet over the hurricane weekend anyway, the #21 form is **Oct-16 150C ×1 as one net-debit order, ≈ $2.29/ct now, do-not-chase $2.75**, on his word — a new decision, not a desk rec.
- **Desk lean CONFIRMED: SELL the 150C ×1 TODAY at Fidelity's bid.** The Fri 15:00 stop is the fallback. `[POSITION_STATE_UNKNOWN]` for today: if Will has already acted during the outage, his fill governs and gets recorded (root rule #10).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

## ADDENDUM 2026-10-08 EVENING, written 19:07 ET (`date` 19:07:30): `MGMT-USO150C-OCT09` ×1 NOT SOLD Thursday. The Fri 15:00 ET stop stands. PROME spawn `terry-1008pm`. The text above stands as written

**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD MOVED.** Broker facts: `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md` and `git show ef2bc83f1:FORGE/STATUS.md`.

- **Booked (root rule #10): no fill.** The 10/8 Activity (pending, plus the past 30 days from 10/2) shows **no USO option row**. The positions view shows **×1 held**: basis $299.66, last $0.66 ⇒ $66.00 (−$233.66) `[10/8 rcv]`. The morning's SELL-TODAY lean (ADDENDUM 2026-10-08, RE-PULL 11:03) was not taken. That was Will's call, and it is recorded, not graded.
- **The rail for Friday is unchanged: the Fri 10/09 15:00 ET HARD STOP STANDS** (WQ-366 DECLINE, Will 10/3 21:10 ET; DOCKET L605). Sell at Fidelity's bid no later than 15:00 ET. A sale earlier on Friday is Will's choice and is outside the DECLINE's content; the card does not instruct it.
- ⛔ **Exercise is still UNFUNDABLE.** A Friday close above $150.00 ⇒ the IRA buys 100 USO = **$15,000** against **$11,421.19 cash** (≈ $12,705 counting the +$1,283.98 pending from the three QQQ fills) `[10/8 rcv]`. Fidelity's handling is UNOBSERVED (D-60). If USO is above $150 at 15:00, the sale at the stop is not optional in substance.

| At the 10/8 close (closes and screening marks, NEVER bids) | Value |
|---|---|
| USO | **$147.58 [10/8c]** (+2.55% vs $143.91 [10/7c]; day range $146.06–$150.48) ⇒ the 150 strike is **$2.42 (1.6%) out of the money**. Post-market $147.50 at 18:47 ET (not a close) |
| 150C Oct-09, vendor end-of-session | **0.58 / 0.65**, IV 35.8%, OI 2,362, volume 5,167, last trade 15:59 ⇒ ×1 ≈ $57.35 at that bid, ≈ −$242.31 vs $299.66 (INFERRED, not a Friday bid) |
| Model (trading-hour clock, calibrated to the 0.615 mid at 41%; shape, not price), at an unchanged USO | ≈ $0.59 at Fri 09:45 · $0.52 at 10:30 · $0.36 at 12:00 · **$0.03 at the 15:00 stop** ⇒ at an unchanged USO the stop forfeits ≈ $56 against a 09:45 sale |
| Model at Fri 15:00 by level | USO $148 ⇒ 0.06 · $149 ⇒ 0.23 · $150 ⇒ 0.61 · $151 ⇒ 1.23 · $152 ⇒ 2.07. Chance of a Friday close above $150 ≈ **26%** (model) |

- **Root rule #6:** the sale is an EXIT, and the rule governs buys. A green USO session gets a better price for a call sale. Neither colour is a break.
- **Roll: NONE** (unchanged). There is no fired trigger: BRENT's 10/8 read is not a new event-class arm and WQ-192 holds (durable finding 1). The 11:03 RE-PULL's #21 form (Oct-16 150C ×1, do-not-chase $2.75) remains Will's to take on his own word, not a desk recommendation, and must be re-priced on Fidelity's chain.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no new action is proposed; the Friday sale at or before 15:00 ET is his order).
