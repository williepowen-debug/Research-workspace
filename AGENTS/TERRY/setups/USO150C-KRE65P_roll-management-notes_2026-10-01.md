# MANAGEMENT NOTES — USO $150C Oct-09-2026 ×2 · KRE $65P Dec-31-2026 ×2 (Fidelity IRA) — Will's 9/30 rolls

**Date:** 2026-10-01 Thu, written 11:11 ET (live reads `date` 11:09:14–11:09:58). **Spawn:** PROME `prome-2a`, Tier 1 (packet `inbox/processed/2026-09-30_from-PROME_sep30-lines-were-ROLLED-not-expired_fills-and-card-asks.md`, ask 3).
**Ids:** `MGMT-USO150C-OCT09` · `MGMT-KRE65P-DEC31` (management notes; no SETUPS rows).
**Terry verdict:** 🟡 **RECORDED — Will's own hand (root rule #5); sell-or-roll rails set, no action owed today.** These notes record the lines and their rails; they do not re-litigate the rolls.
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

## ADDENDUM-4 2026-10-07 Wed 11:0x–11:1x ET: `MGMT-USO150C-OCT09` ×1 — WQ-366 DECLINE recorded; Tropical Storm Isaias folded in (PROME wave-2 spawn, cloud session). ADDENDUM-3 stands as the dated record

**Ruling recorded (root rule #10):** Will **DECLINED the early sell** on the Decision Deck, 10/3 ~21:10 ET, verbatim: *"I dont think I sell yet.  The news in Saudi arabia continues to get worse"* (PROME packet `inbox/processed/2026-10-03_from-PROME_WQ-357-365-366-rulings.md`; DOCKET L605). ADDENDUM-3's SELL-TODAY lean is superseded by his ruling. **The Fri 10/09 15:00 ET stop STANDS.** Caveat still travelling: the 10/2 MET grade rested on the G7 decision as reported, not on the statement read at the primary.

**Live re-mark (SCREENING; Fidelity's bid governs; position as of the 10/1 capture, nothing later reported):**

| Item | Value |
|---|---|
| USO | **$144.92 (+0.01%)** at 11:07 ET (`fetch.py`); closes 10/2 $147.37 · 10/5 $143.99 · 10/6 $144.91 |
| Strike distance | **$5.08 (3.5%) out of the money**, about 2.2 sessions to the stop |
| 150C Oct-09 bid / ask | **0.53 / 0.65** (IV 44.3%, OI 2,111; `chain_fetch.py --no-cache`, no quote defects) ⇒ one at the bid ≈ **$52.35 ⇒ ≈ −$247 against $299.66** |
| Forward max loss | the remaining mark, ≈ $53 (0.11× the $500 cap) |

**The new fact — Isaias (NHC Advisory 4, 10:00 CDT 10/7, read by TERRY at nhc.noaa.gov 11:1x ET, PRIMARY):** 45 mph, 22.4N 93.6W, moving ENE; **hurricane and storm-surge watches issued for the northern Gulf coast**; hurricane by Thursday. Forecast centre: 23.4N 90.8W Thu 08:00 ET → 24.6N 89.2W Thu 20:00 → **26.6N 88.1W at 95 kt Fri 08:00** → 29.2N 87.5W Fri 20:00 → inland Sat. The track crosses the eastern half of the deepwater producing area **Thu night to Fri morning, before the 15:00 stop** (BOARD `SIG-W-20261007-002`, AEOLUS/CORAL/BRENT action).

**What it changes on this card (construction only; the oil read is BRENT's and AEOLUS's):**
1. **The stop does not move.** Sell at Fidelity's bid by **Fri 10/09 15:00 ET** whatever the day's colour (root rule #6 is a cost preference; it does not override a time stop). Never hold past it: a close above $150 means the IRA buys 100 USO for $15,000, and IRA cash is UNKNOWN since the 10/1 capture (exercise handling UNOBSERVED, FORGE D-60).
2. **The storm is the one dated catalyst inside the line's life, and it lands before the stop.** Operator evacuations and shut-ins usually start 48–72 hours ahead, so headlines can come Thu–Fri. That **supports Will's hold to Friday**; it is not a reason to hold past it.
3. **The storm is NOT a clean call catalyst — two signs, unmodeled.** Offshore shut-ins remove crude supply (supportive of WTI). The forecast landfall zone (Mobile Bay / western Panhandle) also holds Gulf-coast refining (Chevron Pascagoula sits west of Mobile Bay — INFERRED from public plant locations, not checked today); a refinery outage removes crude demand (negative for WTI) and supports product cracks. Net sign and size: BRENT/AEOLUS. The NHC track has been public since Advisory 1, so the 44% implied vol already prices some of it.
4. **New early-exit branch (sell-into-strength, the right colour):** if USO trades **at or above $150 before the stop**, sell then rather than wait for 15:00 Friday. Storm premium usually leaves crude once a track is fixed or the storm makes landfall, and the stop day is also the day of the strongest crossing. A sale on a green USO day is the right colour for selling a call.
5. **Still no roll.** An Oct-16 150C would straddle the Saturday landfall, so its buy leg pays storm premium that every desk can see. BRENT holds STAND DOWN (WQ-192), and no trigger has fired (durable finding 1). If Will rolls anyway, buy the leg on a red USO session.

**Will's decision and deadline, plainly:** sell the one USO call by **Friday 10/9 at 3:00 PM ET** (or earlier, if USO reaches $150 first). Today it is worth about $52 at the vendor bid, against $299.66 paid.

`$0` MOVED · NO ORDER · no gate moved.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed; the sale is his order).
