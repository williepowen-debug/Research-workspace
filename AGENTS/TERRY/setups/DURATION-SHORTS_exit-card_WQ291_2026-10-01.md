# EXIT CARD — duration-short sleeve: TLT $82P Oct-16-2026 ×1 + TBT 10 sh (Fidelity IRA) — BOND's thesis kill MET

**Date:** 2026-10-01 Thu, written from 16:25 ET (live reads 16:19:17–16:19:50 ET below). **Session:** TERRY interactive (Will in the window). **Trigger:** BOND packet `inbox/2026-10-01_from-BOND_WQ-291-kill-MET-exit-duration-shorts-card-ask.md` (spawn `prome-2f`, DOCKET L478 / WQ-291), relayed by PROME `prome-2f` ask 4.
**Id:** `MGMT-DURSHORT-EXIT-WQ291` (exit card on held lines; no SETUPS row — ledger at 97.8% of its read budget, rotation owed by Mon 10/05).
**Thesis owner:** **BOND** (the kill and the recommendation). Rates domain also HENRY. **Construction, timing, day colour, mechanics:** TERRY. **Approval:** Will (root rule #5).
**Terry verdict:** ✅ **CLEAN EXIT — SELL BOTH on Fri 10/02, after the open settles (from ~09:45 ET), by 15:00 ET.** The kill is pre-registered and MET; the put has no time value left to give up; the 82P must leave the IRA before 10/16 regardless.
**Confidence in the structure:** High (payoff arithmetic and mechanics). **Confidence in the thesis call:** BOND's, not this desk's — and see the caveat in §2, which BOND attached and which survives here.
**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD MOVED.** BOND states no price, no order and no timing; this card supplies them as a proposal.

---

## 1. The kill (BOND's grade, quoted from the packet — TERRY did not re-grade it)

| Item | Value |
|---|---|
| Rule | Sept-4 thesis kill for the 9/23 5Y `I'` fire; letter `KB-BND-337`/`-342`, Will 9/26 |
| Series | NY Fed FR2004 `PDPOSGSC-G3L6` (dealer net positions, 3–6Y coupons) |
| PRE (as-of 9/16) → POST (as-of 9/23) | **$47.986B → $60.079B** |
| Δ vs bar | **+$12.093B vs +$8.6B ⇒ MET by +$3.493B** (bar level $56.586B) |
| Published | between 16:13:01 and 16:15:20 ET 10/1; BOND grader rc=0 twice |
| Auction leg | 9/23 5Y `91282CRN3`: `I'` 54.31 vs the 59.48 bar (−5.17pp) |
| Record | `AGENTS/BOND/workbook/KB.tsv` `KB-BND-383` |
| BOND's recommendation | **"Exit all duration shorts."** A recommendation, not an action. |

**Riders that travel verbatim (BOND):**
1. An unusual 3–6Y net-inventory build is **NOT proof of auction warehousing** (r = −0.08 vs award size stays on the record).
2. The **funding-leg window for the 9/23 fire is EXPLICITLY UNGRADED**. It was never MET and never NOT MET.
3. This is an **operational rule. It makes no claim that the threshold predicts outcomes.**

## 2. ⚠️ The caveat that could change Will's decision (BOND's, kept in substance)

On the same FR2004 print, dealers' **long-end TOTAL fell to $140.5B (−$3.8B w/w)** and **6–7Y fell to $23.199B (−$4.646B)**. **The inventory build sat in 3–6Y notes, not in duration overall.** Will's 9/26 ruling makes 3–6Y alone govern a 5Y fire, so the letter is MET — but the evidence is about the belly of the curve, while both lines here are long-end exposure (TLT = 20+ year bonds; TBT = 2× inverse of the same index). **It bears on how much weight the exit deserves, not on whether the rule fired.** TERRY's structure read (§5) does not depend on it: exiting costs almost nothing but the direction itself.

## 3. Position (broker truth = Will; source = PROME transcription `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md`, Will's 16:15 ET end-of-day screenshot, ties to the cent at $36,077.04)

| Line | Qty | Basis | Fidelity last (16:15 capture) | Vendor live (16:19 ET) | ≈ vs basis | Exposure it carries |
|---|---|---|---|---|---|---|
| **TLT $82P Oct-16-2026** | 1 | $167.67 ($1.68) | $4.25 ⇒ $425.00, +$257.33 | TLT **$77.71 (−0.09%)** ⇒ **$4.29 in the money**; 82P bid/ask **4.20 / 4.40** (OI 35,345; last trade 15:51) — SCREENING | ≈ **+$252** at the 4.20 bid, net of $0.65 fee | Put delta ≈ **−0.93** (model estimate: IV 18.3%, 15 calendar days) ⇒ behaves like **short ~92 TLT shares ≈ $7,200** (Black–Scholes delta −0.924) |
| **TBT** (2× daily inverse, 20+Y Treasuries) | 10 sh | $346.46 ($34.65) | $42.24 ⇒ $422.40, +$75.94 | **$42.19 (−0.71%)** | ≈ **+$75** at $42.19 | ≈ **$844** of short-long-bond exposure (2 × $422) |
| **Sleeve** | — | **$514.13** | **$847.40** | — | **≈ +$327** | **≈ $8,000 TLT-equivalent short; the put is ~90% of it** |

Sources: `fetch.py price TLT TBT` 16:19:17 ET; `chain_fetch.py TLT 2026-10-16 --type put --no-cache --legs 82` 16:19:50 ET (leg gate PASS — two-sided, no lock/cross/dead). Fill history: 82P ×2 bought before 7/16 (entry fields unrecoverable, construction rule #20); 1 of 2 sold 9/28 @ $3.60 (+$191.66). TBT 14 → 10 sh on 9/15. **HBAN $16P Oct-16 ×2 shares the WQ-302 deadline but is NOT a duration short and is NOT in this card.**

## 4. Entry-equivalent: what the exit is, mechanically

| Leg | Order | Limit guidance | Do-not-chase |
|---|---|---|---|
| **TLT 82P ×1** | **Sell to close**, limit, regular session | At or near **Fidelity's live bid**, and **no lower than intrinsic − $0.10** (82 − TLT at Will's read − 0.10). At tonight's figures: floor ≈ **$4.19** | Do not cut the limit below that floor to force a fill — a 0.05 step every few minutes toward the bid is enough on a 35k-OI strike. If unfilled by 14:30 ET, take the bid. |
| **TBT 10 sh** | **Sell**, limit, regular session | At or near the bid; $0 commission | No floor — the position is small and liquid; a limit just avoids a bad print in the opening minutes |

- **Order of legs:** independent — each is a full exit of its own line; leg risk does not exist here (neither leg hedges the other).
- **Proceeds:** ≈ $419 + ≈ $422 ≈ **$841 into IRA cash** at tonight's marks. That cash also widens the USO 150C ×1's exercise headroom (≈ $525 tonight; see `MGMT-USO150C-OCT09` addendum 10/01 16:2x).

## 5. Timing

- **Payrolls: Fri 10/02 08:30 ET** (BOND `docket/CATALYSTS.tsv`: *"2Y/1y1y reaction … belly-led"*). **Both legs trade only after it** — the 82P from 09:30, TBT in the regular session. **There is no branch that exits before the print;** the sleeve takes the print's move whatever Will decides tonight.
- **Desk timing:** sell **from ~09:45 ET** (let the opening spreads settle), **by 15:00 ET Friday.** Holding over the weekend buys nothing: the thesis is killed and the put has no time value to earn back.
- **Backstops already on file:** WQ-302 dated decision point **Wed 10/14 by the close**; hard backstop **Fri 10/16 before 16:00 ET** (`MGMT-TLT82P-OCT16` §3). This card makes those moot if Will approves.
- **Why the 82P must leave regardless:** held in the money at the 10/16 close, exercise would **sell 100 TLT at $82 = $8,200 short** in an IRA that cannot be short. Fidelity's published Options Agreement reserves three actions (close it at the Rep-Assisted rate, $32.95 + 65¢; exercise and buy in; or instruct the OCC not to exercise — forfeiting the intrinsic, ≈ $429 tonight) and does not say which it uses (`MGMT-TLT82P-OCT16` §4). **Which one applies in this account is UNOBSERVED (FORGE D-60).** Selling first avoids all three.

## 6. Day colour — root rule #6 on a SALE, with the measurement written before the fill

- For closing a long put, the proxy runs in reverse: sell on a **red TLT day** (TLT down, puts bid) — `MGMT-TLT82P-OCT16` §5. For selling TBT, a red TLT day is also the better day (TBT up). **Both legs prefer the same colour.**
- **Friday's colour is unknown until the print.** If TLT is **green** (yields fall — e.g. a soft payrolls number), the sale is a wrong-colour sale and needs the direct measurement before the fill (`RISK_RULES.md` § "Breaking root rule #6").
- **The measurement, tonight (moment property — re-confirm on Friday's Fidelity screen):** the 82P's time value at the bid is **4.20 − 4.29 = −$0.09** — the bid sits **below** intrinsic. **There is no convexity left to sell cheap;** the proxy's question (*"am I selling convexity cheap?"*) has a measured answer of **no**. A green-day sale costs only the delta move itself (~$0.93 per $1 TLT), which is the direction the kill says to stop holding. ⇒ **A green-day exit is a legitimate break IF Friday's Fidelity bid still sits within ~$0.10 of intrinsic. Write the bid and the intrinsic on this card at the fill.**
- **"The deadline is close" is NOT the reason and is not offered as one.** The reason is the fired kill (durable finding 12: a fired kill-switch is held, not re-litigated) plus a measured zero time value.
- No hard guard is relaxed: no gate, cap or stand-down is touched by an exit.

## 7. Choices for Will

| # | Choice | What it does | Desk view |
|---|---|---|---|
| **A** | **Exit both Friday** (§4–§6) | Takes the sleeve to $0 exposure; ≈ +$327 realized vs basis at tonight's marks; ends the D-60 path | ✅ **Desk lean.** BOND's recommendation in TERRY's construction |
| B | Exit the 82P Friday, keep TBT | Removes ~90% of the duration exposure and the whole IRA-expiry problem; keeps a $422 linear short with no expiry and no rule | ⚠️ Keeps a slice of a killed thesis with no management rule on it (FORGE: *"no management rule"*). Only if Will wants a residual view against BOND's kill |
| C | Hold both to the WQ-302 date (10/14) | Keeps the exposure ~8 more sessions | ⛔ Holding a killed thesis's main leg — exactly what a pre-registered kill exists to stop. The put earns no time value by waiting |

## 8. Why not / counter-case

The best reason not to exit: the 3–6Y build is belly evidence and the long end moved the other way on the same print (§2), so a long-end short might still be right on substance even though the operational rule fired. The answer: the rule is Will's and BOND's letter, ruled 9/26, and **an operational rule that is overridden the first time it fires is not a rule** (durable finding 12). The cost of being wrong by exiting is the forgone move on ≈ $8k of TLT-equivalent exposure — the same amount the sleeve risks by staying.

## Decision

> **WQ-291 (Will):** **A — SELL TO CLOSE TLT $82P Oct-16 ×1** (limit at Fidelity's bid, floor intrinsic − $0.10) **and SELL TBT 10 sh**, Fri 10/02 from ~09:45 ET, by 15:00 ET. Or B (82P only) or C (hold to 10/14).

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-02 Fri 09:47–09:50 ET: re-marked after payrolls. TLT is GREEN, the adverse direction for both lines (PROME `prome-70`). §§1–8 stand as written

**Positions as of the 10/1 capture. Quotes are SCREENING** (yfinance `--legs 82`, leg gate PASS. At 09:47 the 82P quote still carried 10/1's last trade and was 7% wide with `NONMONO,DIRINC` flags. By 09:50 it had its first trade of the day, 09:31. It may be up to about 15 minutes old, and Fidelity's bid governs).

| Item | 09:47 | 09:50 |
|---|---|---|
| TLT | $78.06 (+0.44% vs $77.71; no ex-date today) | $77.98 (+0.35%) |
| 82P intrinsic | $3.94–3.96 | $4.02 |
| 82P bid / ask | 3.95 / 4.25 | **4.05 / 4.15** |
| **Time value at the bid** | **≈ $0.00** | **≈ +$0.03** |
| 82P sold, after the $0.65 fee | ≈ $394.35 | ≈ **$404.35** (+$236.68 on $167.67) |
| TBT ×10 | $42.04 ⇒ $420.40 | $42.00 ⇒ **$420.00** (+$73.54 on $346.46) |
| **Exit proceeds, both lines** | ≈ $814.75 | **≈ $824.35** (≈ +$310 on $514.13) |

**§6's day-colour test, measured before any fill:** the time value at the bid is **$0.00–0.03**, which is within the $0.10 the card sets. **A sale on today's green day is therefore a legitimate break of root rule #6, provided Fidelity's own bid is within about $0.10 of intrinsic when Will looks** (floor = 82 − TLT − 0.10 ≈ **$3.92** at TLT $77.98). Payrolls is not the reason, and neither is the 10/16 date.
**What waiting costs on this card's terms:** there's no time value left to earn, so holding is purely a directional bet on ≈ $7.8k of short TLT exposure (put delta ≈ −0.89 on a Black–Scholes model estimate ≈ $7.0k, plus TBT ≈ $0.84k). That's **≈ $78 for every 1% TLT moves, against the lines when it rises.** Today's green tape has already cost ≈ $17–26 against Thursday's ≈ $841. HENRY says the long end can reverse on supply at the 10/6–10/8 auctions, and that's the case for holding. But it's a view against BOND's MET kill, and durable finding 12 keeps the kill in force. Holding also brings back the IRA in-the-money expiry question at 10/16 (D-60).
**Lean unchanged: A. Sell the 82P (limit at Fidelity's bid, floor intrinsic − $0.10) and sell all 10 TBT, today by 15:00 ET.** If WQ-360 is also approved, **sell these first, then buy.**

**APPROVAL REQUIRED — Will must approve/reject before execution.** Memo: `PROME/inbox/2026-10-02_from-TERRY_open-remarks-WQ347-357-360.md`.

---

## ADDENDUM 2026-10-07 Wed 11:0x–11:1x ET: WQ-357 LATER recorded; BOND's 10/5 research read folded in; re-mark before today's 10Y and tomorrow's 30Y reopenings (PROME wave-2 spawn, cloud session). §§1–8 and the 10/2 addendum stand as written

**Ruling recorded (root rule #10):** Will tapped **WQ-357 LATER**, 10/3 21:08 ET, verbatim: *"I would like to do more research on this.  I am not sure any bond rebound continues.  I would like us to do some mroe research"* (PROME packet `inbox/processed/2026-10-03_from-PROME_WQ-357-365-366-rulings.md`). Not approved, not declined. **Path C (hold to 10/14) is the live path by default.**

**BOND's research read, delivered 10/5** (`AGENTS/BOND/analysis/2026-10-05_WQ-357_rebound-research.md`, `ff0992bf1`; DOCKET L608 RESOLVED), in substance: *completed observations do not establish a sustained long-end rebound*; the 10/2 session gave back Thursday's rally; real yields stay elevated; ACM term premium +17.8bp over 5 observations. **BOND's REAFFIRM EXIT recommendation is unchanged**, the kill stays MET, and BOND makes no claim that bond prices must keep falling. ⇒ Will's doubt ("not sure any bond rebound continues") and BOND's evidence point the same way on the tape; BOND's exit rule still says exit.

**Live re-mark (SCREENING; Fidelity governs; position as of the 10/1 capture):**

| Line | Live 11:07 ET | ≈ vs basis |
|---|---|---|
| TLT $82P Oct-16 ×1 | TLT **$77.00 (−0.37%)** ⇒ **$5.00 in the money**; 82P bid/ask **5.10 / 5.20** (OI 1,414; no quote defects) ⇒ time value at the bid **+$0.10**; delta ≈ −0.97 to −0.99 (model) | ≈ **$509 ⇒ +$342** vs $167.67 |
| TBT 10 sh | **$43.16 (+0.94%)** | ≈ **$432 ⇒ +$85** vs $346.46 |
| Sleeve | ≈ $941 | **≈ +$427**; ≈ $84 per 1% TLT move (82P ≈ $75 at delta −0.98 on $77 · TBT ≈ $9), against the lines when TLT rises |

Official curve (FRED): 10Y 5.28 [10/2] → **5.31 [10/5]**; 30Y 5.63 → **5.66 [10/5]**; 30Y real 3.37 [10/5], a cycle high (`SIG-W-20261007-005`, info). TLT closes since the card: 10/1 $77.71 → 10/7 $77.00 intraday. **Holding has paid ≈ +$100 since Thursday's figures.**

**What the next eight sessions hold:** **10Y $39B reopening today 13:00 ET** · FOMC minutes 14:00 · **30Y $22B reopening Thu 10/8 13:00** · CPI Wed 10/14 08:30 · the 82P expires Fri 10/16. Holding through the reopenings is a held view on supply against BOND's MET kill — Will's to take, not the desk's to recommend.

**Desk view (unchanged in form):** A — sell both. Two construction facts hold whatever the view:
1. **The 82P must leave the IRA before the 10/16 close.** It carries $0.10 of time value, so waiting earns nothing but delta, and an in-the-money expiry runs into Fidelity's unobserved handling (D-60; `MGMT-TLT82P-OCT16` § 4).
2. **Sell on a RED TLT session** (puts bid, TBT up): today is red, the right colour for both legs. If Will wants to keep a duration-short view past 10/14, the dated form is the separate WQ-360 card (TLT Dec-18 77P ×2, fills only on a GREEN TLT session), not a roll of a $5-in-the-money October put. **Sell these first, then buy.**

**Will's decision and deadline, plainly:** sell (or keep) the one TLT October put and the 10 TBT shares by **Wednesday 10/14 at the close**; the put must be gone before **Friday 10/16, 4:00 PM ET** in any case.

`$0` MOVED · NO ORDER. **APPROVAL REQUIRED — Will must approve/reject before execution.**
