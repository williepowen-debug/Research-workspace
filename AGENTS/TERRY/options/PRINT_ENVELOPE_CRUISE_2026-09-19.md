# Print-reaction envelope — CRUISE names (CCL / NCLH / RCL)

**Built 2026-09-19 Sat ~20:4x ET** (`date` wall clock, copied not inferred). **Markets CLOSED; every price is the 2026-09-18 regular-session close and every option quote is Friday's last two-sided quote** — root rule #4, and `RISK_RULES` **5b**: vendor chain marks are SCREENING marks over a weekend doubly so. ⛔ **No fill may be priced off this file.**

**Why this file exists:** construction rule **#18** measured its 10%-OTM line on **regional-bank singles** and says so in its own scope clause — *"Before applying the 10% line to another sector, re-measure the envelope — the tool is re-runnable."* Will directed a cruise-sector look on 2026-09-19. This is that re-measure. **It is a STRUCTURE-property file (rule #14): the envelope is a fact about these names and does not expire tonight. The quotes inside it DO.**

**Instrument:** `options/partb_realized_moves.py`, extended this session to take tickers on argv (default basket unchanged — **regression-checked byte-identical against a pre-edit baseline run**). Reaction attribution came from the vendor timestamp on all 24 rows (`attrib=ts`), never the convention fallback.

---

## 0 · ⛔ CORRECTIONS, SAME DAY — three statements on top of this measurement were wrong. **The measurement itself is not corrected and was independently re-derived.**

*(Raised by CATO via Will, relayed and part-verified by CRUISE, **re-verified here against this desk's own data and arithmetic before any edit**. ⚠️ `finding_a_correction_pass_is_unreviewed_work` — this block is itself a fix pass and carries the higher defect rate that implies.)*

✅ **NOT IMPEACHED:** CRUISE re-derived the envelope independently off **EDGAR 8-K item-2.02 dates** rather than a vendor calendar and **every headline figure reproduces exactly** (median 4.59% · max 9.81% · worst down −4.87% · 5 of 8 down). **A different perimeter agreeing on the same numbers is worth more than my own re-run would have been.**

**① 🔴 THE "LAST THREE PRINTS" SEQUENCE WAS WRONG — MY ERROR, AND THE SKIPPED ROW WAS PRINTED IN MY OWN TOOL OUTPUT.**
I wrote *"CCL's LAST THREE prints are all down and monotonically worsening (−3.98 → −4.31 → −4.87), n=3."* **The actual last three are `+9.81%` (2025-12-19) · `−4.31%` (2026-03-27) · `−4.87%` (2026-06-23).** The sequence I quoted **skipped 2025-12-19** — the single largest UP print in the sample — and reached back to 2025-09-29 to assemble three in a row.
**Corrected claim: the last TWO prints are down and worsening (−4.31 → −4.87), n=2. Two of the last three are down. The three most recent DOWN prints do descend monotonically, but that is a SELECTED SUBSEQUENCE and cannot be quoted as "the last three."**
🔑 **Why this one survived, and it is the lesson worth keeping: it was my BEAR-side counter-qualifier — an error that cut AGAINST my own headline. A mistake that makes your own conclusion look weaker reads as intellectual honesty and gets audited less than one that flatters you.** Correcting it **strengthens** the up-skew finding. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]` — the inverse case.

**③ 🔴 THE NCLH STRADDLE COMPARISON WAS THE WRONG HURDLE — REASON WITHDRAWN, CONCLUSION STANDS ON DIFFERENT ARITHMETIC.**
I wrote *"the Dec-18 ATM straddle prices ±21%, so an −11% print is half the priced move; the print alone does not beat the price."* **A long put's breakeven is `strike − premium`, not the straddle's implied move.** `14.00 − 1.35 = 12.65 = −10.41%` from 14.12 — **CRUISE's arithmetic is correct and the sentence is withdrawn, not annotated.**
⚠️ **And it was wrong in the direction that UNDERSTATED the trade — including in CRUISE's own gentler version of it.** At the print with **44 DTE still to run**, an −11% move marks the 14P at **+21.3% / +24.5% / +30.1%** (IV 42/45/50%), not at breakeven: you exit with time value, you do not hold to expiry.
✅ **THE REAL REASON EV ≈ 0, which I should have written in the first place:** at IV 45% the **6 down-prints average +15.0%** while the **2 UP prints average −69.7%**. **The up-tail kills it, not the size of the down move.** Equal-weighted EV −6.2%. **A conclusion that is right for a wrong reason is a defect, not a near-miss** — the corrected reason is also a *better* one, because it names which observations actually drive the number.

**② 🔴 THE HEADLINE DID NOT SURVIVE ITS OWN TABLE — AND MY DISMISSAL OF THE EXCEPTION WAS ITSELF WRONG. THIS IS THE MOST SUBSTANTIVE OF THE THREE.**
I disclosed the positive cell (`Nov-20 21P` at ≥45% post-print IV) and then dismissed it: *"requires the event premium not to crush, which contradicts this desk's own measured +10–16 vol points."*
⛔ **That dismissal applied a FRONT-MONTH finding to a BACK-MONTH strike.** `IV_CRUSH_PARTA`'s +10–16 vol points is a statement about **front-month** event premium — and I measured that kink live in this very file (**Oct-02 54.7% vs Nov-20 45.4%**). **Nov-20 sits 52 days past the print; the event premium is not in it to begin with, so it has almost nothing to crush.** ⇒ **For Nov-20, ~45% is the CENTRAL assumption, not the optimistic one** — indeed **45.36% is that strike's own currently quoted IV.** The 42% default I used was a ~3.4-point crush assumed into an expiry that never carried the premium.
**Restated result, and this is the form that survives:**
> **Over CCL's FULL 8-print distribution, every examined structure is negative-EV at every post-print IV from 35% through 50%** (`Nov-20 21P`: −29.2% @40 · −24.4% @42 · **−16.3% @45.36 (no crush)** · −9.9% @48 · −5.0% @50; it turns positive only at **55%**, which is vol *expansion* through a print).
> **Granting the direction for free, five of six structures stay negative — `Nov-20 21P` turns POSITIVE (+5.8% @45%, +6.7% at its own quoted 45.36%). That is a genuine exception and is now recorded as one.**
**It is still not a trade, for a reason that does not depend on the disputed cell: *"assume the direction is right"* is not an assumption available to anyone before the fact.** The all-8 line is the honest one and it is negative throughout.

**④ ⚖️ I ALSO CALLED THIS AN "INDEPENDENT CONFIRMATION OF `WQ-218 ②`." WITHDRAWN — CRUISE RAISED IT AGAINST THEIR OWN WORDING AND THEY ARE RIGHT.**
`WQ-218 ②` retired a **MECHANISM** claim (fuel convexity does not discriminate CCL from its peers). This file makes an **EXPRESSION** claim (no put pays at one print). **A cheap option would not have resurrected the fuel mechanism, and a dead mechanism does not imply no put pays — neither is evidence for the other.** Two findings pointing at the same practical action are **not** mutual corroboration; treating them as such manufactures confidence from a coincidence of direction. **What actually survives is the narrower constraint, which is the part with content: there is no CCL put expression at this print, whatever the Q4 yield guide says on 9/29.**

### §0-bis · ⛔ CORRECTION **TO THE CORRECTION** — I OVER-CORRECTED ②, AND I MADE A FALSE ACCUSATION. *(same night, raised by CRUISE)*

⚠️ **`finding_a_correction_pass_is_unreviewed_work` — "so does the fix TO the fix." This is that case, arriving within the hour.**

**②-bis 🔴 "THE NOVEMBER EXPIRY NEVER CARRIED THE EVENT PREMIUM" IS FALSE. IT CARRIES ~2–3 VOL POINTS, AND MY ORIGINAL 42% ASSUMPTION WAS THE BETTER ONE.**
CRUISE flagged that my replacement claim was *"not supported by the evidence shown"* and was now load-bearing. **They are right, and testing it reverses my own correction.** I had shown only that `Oct-02` is 9.3 vol points richer than `Nov-20` — **which establishes a KINK, not an ABSENCE.** A back-month expiry containing the same event carries the same event *variance* diluted over more time; it does not escape it.

**The test, done properly.** For an expiry containing one event, `IV² · T = σ_base² · T + J²` (`J` = implied one-day event jump). Two expiries, two unknowns, solved on my own 2026-09-18 quotes:

| specification | σ_base | implied jump `J` | premium in **Oct-02** | premium in **Nov-20** | ⇒ post-print Nov-20 |
|---|---:|---:|---:|---:|---:|
| **21-strike puts** (same strike ⇒ skew controlled; and it is the strike actually being priced) | **42.17%** | **6.94%** | +12.91 pts | **+3.19 pts** | **≈ 42.2%** |
| ATM-interpolated, put side | 45.01% | 6.12% | +9.79 pts | **+2.35 pts** | ≈ 45.0% |

- 🔴 **Both specifications refute my claim: the November expiry's event premium is ~2–3 vol points, NOT zero.**
- 🔑 **And the same-strike solve — the appropriate one, since it is the 21-strike put being priced and skew is controlled by construction — puts post-print `Nov-20` at `42.2%`, i.e. essentially the `42%` default I originally used and then "corrected" away from.**
- ⚠️ **HONEST LIMIT, and it is why this does not simply flip back: the two specifications DISAGREE (42.2% vs 45.0%), and the sign of that one cell flips between them** (`−2.0%` at 42% vs `+5.8%` at 45%). Both assume base vol is FLAT across 14d and 63d, which in a de-rating name it need not be. ⇒ **The correct status of that cell is INDETERMINATE on the evidence I have — not positive as my correction claimed, and not negative as my original claimed.** ⛔ **I am not picking the specification that returns the answer I first published.**
- ✅ **The NO-TRADE verdict never rested on that cell and still does not:** the **all-8 line is negative at 40 / 42 / 45.36 / 48 / 50%**, and *"assume the direction is right"* is not an assumption anyone holds before the fact.

✅ **AND THE EXCHANGE PRODUCED A BETTER FOUNDATION THAN EITHER OF MY REASONS — this is now the cleanest statement of the finding:**
> **The market prices a one-day CCL print jump of `6.94%`. CCL's eight realized prints have an RMS move of `5.53%`. Implied / realized = `1.25×`.** **The event is measurably overpriced, on CCL's own history, with no directional assumption anywhere in it.**
*(n=8; `J` is a model-implied quantity from a two-tenor solve, not a market quote; RMS is the right comparator because `J` enters as a variance.)*

**②-ter 🔴 I ACCUSED CATO OF MERGING TWO STRUCTURES. THE ACCUSATION IS WITHDRAWN AND THE ERROR WAS MINE.**
I wrote that CATO had merged `Nov-20 21P` and an October structure into one *"October structure."* **CRUISE's packet — which I had read before writing that — distinguishes them: *"`Nov-20 21P` at `+5.8%` at 45% post-event IV **and** an October structure at `+10.6%` at 55%."*** The merged phrasing existed **only in the summary message**, and CATO reports its own output kept them separate. ⇒ **CATO's figures are correct, correctly separated, and both reproduce exactly against my table** (`Nov-20 21P` @45% = `+5.8%`; `Oct-16 21P` @55% = `+10.6%`; they share the 21 strike). **I built an accusation about another agent's work off a summary while the precise source was open in front of me. Routed back for correction.**
⚠️ *One substantive note that is NOT a criticism of the figure: `55%` post-print on an **October** expiry would be vol EXPANSION through a print, in the expiry carrying ~13 points of event premium that should crush. My sweep ran to 55% deliberately to include implausible cases; that cell is arithmetic, not a scenario I would defend.*

**①-bis ✅ ATTRIBUTION ACCEPTED AS SHARED.** CRUISE withdrew their *"that is my error, not yours."* **Correct: my headline contradicted my own sensitivity table four lines below it; their error was dropping the caveat I had disclosed. Two different real errors — and filing it as solely theirs would have left mine unfixed at source.**

---

## 1 · The envelope — realized 1-day close-to-close print reactions, last 8 prints each

| name | n | mean \|mv\| | median \|mv\| | max \|mv\| | worst DOWN | # down | reachable by a print? |
|---|---:|---:|---:|---:|---:|---:|---|
| **CCL** | 8 | 4.73% | 4.59% | 9.81% | **−4.87%** | 5 | 🔴 **downside capped ~5%** |
| **NCLH** | 8 | 9.09% | 8.90% | 15.28% | **−15.28%** | 6 | ✅ **yes, and skewed down** |
| **RCL** | 8 | 7.14% | 5.37% | 18.65% | −8.53% | 2 | ⚠️ skewed **UP** |
| *(reference: WAL/OZK/HBAN/ZION, rule #18's own basket)* | 8 ea | 2.5–3.4% | 1.6–3.4% | 6.0–9.7% | −3.95 to −8.93% | 3–4 | — |

**⇒ Cruise prints run ~2× the regional-bank envelope. Rule #18's 10% line does NOT transfer — it is too tight for NCLH and too loose for CCL's downside.** The per-name numbers below replace it for this sector.

**CCL, print by print** (reaction session = same session; BMO release): −0.32 · +6.43 · −1.23 · +6.91 · −3.98 · **+9.81** · −4.31 · −4.87.
🔑 **The asymmetry is the finding: CCL's three largest moves are all UP (+6.43 / +6.91 / +9.81) and NOT ONE of eight down-prints exceeded −4.87%.**
⚠️ **Counter-qualifier — ⛔ CORRECTED, see §0 ①. It previously read *"the LAST THREE prints are all down and monotonically worsening (−3.98 → −4.31 → −4.87), n=3"* and that sequence SKIPPED `+9.81%` (2025-12-19), the biggest up-print in the sample.** **What is true: the last TWO prints are down and worsening (`−4.31` → `−4.87`), n=2; two of the last three are down.** It is a trend in a sample far too small to be a base rate. **Named so the up-skew is not quoted without it — but it is a weaker counter than I first wrote, so the up-skew stands cleaner than this file originally allowed.**

**NCLH, print by print:** +6.29 · −5.31 · −7.77 · +9.23 · **−15.28** · −10.53 · −8.56 · −9.78.
🔑 **The last FOUR consecutive prints were all down 8.56–15.28%, mean −11.04%.** ⚠️ **n=4.**

---

## 2 · The EV tables — does the realized envelope pay the premium?

Black-Scholes, r=4%, spot held flat to the print (so **drift between now and the print is NOT modelled, in either direction**; theta from 9/18 to the print **is**, because each value is struck at the post-print DTE). Debits are the **ask** — the side you buy. Post-print IV is swept, because it is the assumption most likely to be wrong.

### CCL — the 2026-09-29 print (CONFIRMED at CCL's own press release 9/15, via CRUISE)

| structure | debit (ask) | EV over **all 8** prints | EV over the **5 DOWN** prints |
|---|---:|---:|---:|
| Oct-02 **21P** (−3.8% OTM) | $0.54 | **−70.9%** | **−53.5%** |
| Oct-02 **22P** (ATM) | $1.01 | **−44.7%** | **−12.4%** |
| Oct-16 **21P** | $0.81 | **−44.0%** | **−17.8%** |
| Nov-20 **21P** | $1.21 | **−24.4%** | **−2.0%** |
| Nov-20 **20P** | $0.81 | **−29.9%** | **−6.9%** |
| Nov-20 **21P/17.5P spread** (rule 18(b)'s "sell the rich wing" form) | $1.01 on $3.50 | **−26.2%** | **−5.5%** |

🔴 **THE SENTENCE THIS FILE EXISTS FOR — ⛔ RESTATED, see §0 ②; the original over-claimed on the right-hand column:** **over CCL's FULL 8-print distribution every structure above is negative-EV, and stays negative at every post-print IV from 35% through 50%.** **Granting the direction for free, five of the six remain negative — `Nov-20 21P` turns POSITIVE at ≥45% (+5.8%), and 45.36% is that strike's OWN quoted IV.** ⛔ **My original dismissal of that cell was wrong, AND SO WAS THE CORRECTION TO IT — see §0-bis.** The November expiry does carry **~2–3 vol points** of event premium (not zero, as I then claimed), and the same-strike variance solve puts post-print `Nov-20` at **~42.2%**, essentially my original default. **The two defensible specifications disagree and the cell's SIGN flips between them ⇒ its honest status is INDETERMINATE, neither positive nor negative.** ✅ **The verdict never rested on it: the all-8 line is negative at 40/42/45.36/48/50%, and *"assume the direction is right"* is not an assumption anyone has before the fact.**

**Sensitivity — the verdict survives the assumption sweep** (EV over the 5 down prints, post-print IV 35%→55%):

| structure | IV 35% | 40% | 45% | 50% | 55% (no crush at all) |
|---|---:|---:|---:|---:|---:|
| Oct-02 21P | −59.5% | −53.5% | −47.3% | −41.0% | −34.5% |
| Oct-02 22P | −14.5% | −12.4% | −10.0% | −7.4% | −4.7% |
| Oct-16 21P | −33.0% | −22.2% | −11.3% | −0.4% | +10.6% |
| Nov-20 21P | −20.0% | −7.2% | +5.8% | +18.7% | +31.6% |

⇒ **Only Nov-20 turns positive, and only if front-month event premium does NOT crush** — which contradicts `IV_CRUSH_PARTA_2026-07-17`'s measured **+10–16 vol pts** of event premium in front-month strikes. The Friday chain shows exactly that premium live: **CCL Oct-02 ATM IV 54.7% vs Nov-20 ATM 45.4% — a 9.3 vol-point front-month kink.** Buying the front expiry pays it; the sweep says paying it is not recoverable from CCL's realized down-moves.

**Rule #18(a) additionally kills the spread as a print trade:** the 17.5P short leg is **−19.9% OTM**. The print cannot reach it. Its real catalyst would be multi-quarter transmission, and CRUISE has no dated catalyst for that before Q4.

### NCLH — the 2026-11-04 print *(vendor calendar, `earnings_dates` 07:00 ET)*

> 🔴 **DATE STATUS, RESOLVED 2026-09-19 LATE: `UNVERIFIED — CHECKED AT TWO SURFACES, NOT YET ANNOUNCED.` It still BLOCKS any card.**
> CRUISE checked and reported it does not close; **I corroborated both halves with my own pulls rather than relaying** (`finding_asymmetric_rigor_counterparty_claims`).
> - **SEC** `data.sec.gov` CIK `0001513761`, own pull: **newest filing of ANY kind = `2026-08-12` (8-K/A).** ⚠️ CRUISE's packet says *"nothing since 2026-09-01"*; my pull says **nothing since 08-12** — the negative holds harder; **my figure is the one cited here**, not theirs.
> - **NCLH IR** `nclhltd.com/investors`, own fetch: **83,016 B of real content, newest earnings artifact `NCLH Q2 2026`, no Q3-2026 / November-2026 item.** *(`/news-events/events` returned 38,014 B with no match but is likely JS-rendered — that negative is weak and is NOT leaned on.)*
> - ⛔ **EDGAR CANNOT ANSWER THIS BY CONSTRUCTION** — CCL's own date arrived as a press release that never became an 8-K, which is exactly how CRUISE's six-day miss happened. **The IR leg is load-bearing; the SEC leg is corroboration. The PAIRING is what makes this *not-yet-announced* rather than *missed-by-us*.**
> - ⏳ **POINT-IN-TIME, NOT A STANDING NEGATIVE.** CCL announced **14 days** ahead ⇒ expect NCLH ~**mid-October**. **`Stale_By 2026-10-20`** (CRUISE `KB-CRU-087`). **Re-check; do not carry as settled.**
>
> ⚠️ **Every EV figure in this section is computed to a 2026-11-04 print that the company has not confirmed. If the real date lands in a different week the `44 DTE remaining` assumption moves and every number below shifts with it.** The *envelope* (a structure property) is unaffected; the *pricing* is not.

`Dec-18 14P` (ATM, −0.8%), debit **$1.35** ask, spread **2.25%**, OI **3,870**, IV **50.20%**, 91 DTE from 9/18 → **88 DTE from Mon 9/21, i.e. INSIDE the 60–90 band** (rule #21: this would be a NEW deployment, so the band binds in full — it clears).

| basis | EV @ post-print IV 42% | 45% | 50% |
|---|---:|---:|---:|
| **all 8 prints** | −9.7% | −6.2% | **−0.2%** |
| **the 6 DOWN prints** (direction granted) | +9.3% | +15.0% | +20.8% |
| **the last 4 prints only** (the regime claim) | +22.4% | +25.6% | +31.1% |

🔑 **Read this honestly: against its OWN 8-print base rate the option is priced at roughly fair — EV ≈ 0. There is no structural mispricing to harvest.** The entire edge is a **regime claim** that the last four prints (all −8.6 to −15.3%) are the right sample and the earlier four are not. **That is n=4 and it is subjective** (`RISK_SCORING` §2: never invent a precise p_model; if it is subjective, say so). ⇒ **The trade is a directional bet wearing an event's clothes.**

**Structural facts that DO hold regardless (rule #14 — stable, gradeable any time):**
- **NCLH skips November entirely.** `2026-10-30` (42 DTE) **expires five days BEFORE the 11/4 print** and `2026-12-18` (91 DTE) is the first expiry that spans it. **There is no mid-tenor choice.** *(Same defect this desk measured on VLO/MPC on 9/11 — an empty 60–90 band. Worth noting it recurs.)*
- **Dec-18 liquidity is the best in the sector:** spreads 2.25–11%, OI 1,455–22,435, skew flat at ~50–51% from the 13 to the 18 strike. Strike gap 10 → 13 (no 11 or 12).
- Leg gate on `14P`: **✓ usable, two-sided** (`chain_fetch --legs 14`, rc=0).
- ⛔ **WITHDRAWN, see §0 ③.** This read: *"ATM straddle Dec-18 ≈ $2.97 = 21.0% of spot; a −11% print is half of that, so the print alone does not beat the price — you need print plus continued drift."* **The straddle is the hurdle for a STRADDLE. A long put's breakeven is `strike − premium` = `$12.65` = `−10.41%`, which an −11% print clears** — and at the print with **44 DTE left** it marks **+21% to +30%**, not breakeven. ✅ **Replacement reason, which is the true one:** at IV 45% NCLH's **6 down-prints average +15.0%** and its **2 UP prints average −69.7%**. **The up-tail is what drives EV to ≈0, not the size of the down move.**
- ⚠️ Put IV 50.20% vs call IV 56.89% at the same 14 strike. **Checked, not chased:** C−P = 0.31 vs S−PV(K) = 0.259 — a $0.05 gap, inside the legs' own bid/ask. Parity holds; the IV split is vendor carry-assumption noise, not a signal.

### RCL — the 2026-10-27 print
> 🔴 **DATE STATUS: `UNVERIFIED — UNCHECKED, BY DECISION.` Nobody has looked, and that is deliberately NOT the same state as NCLH's.**
> CRUISE offered to run the same two surfaces; **I declined** — RCL is not a bear candidate on the measurement below, so its date is load-bearing for nothing at this desk. ⛔ **The two UNVERIFIED labels are worded differently on purpose: one was examined and came back empty, the other was never examined. A reader who reads equal scrutiny into them would be wrong** (`finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit`). **If an RCL trade is ever contemplated, this date must be checked first — it has NOT been.**
**Not a bear candidate on this measurement.** 2 of 8 prints down, max **+18.65%**, FY26 guide **raised**. A put here is fighting the name's own print distribution. Recorded so the sector is covered, not because anything is proposed.

---

## 3 · What this does NOT say

- ⛔ **It sets no level, arms nothing and proposes no card.** Both CRUISE rows are **Will-ruled WATCH, no card** (`WQ-218` ①②, 2026-09-10). A card is a **fresh** proposal under root rule #5 — this file is an input to one, never a substitute.
- ⛔ **It is not a thesis.** Thesis ownership is CRUISE's (HARD BOUNDARY #3). This file answers only *"can the instrument pay the view?"*
- ⚠️ **Spot is held flat to the print in every EV table.** Real drift between 9/21 and the print is unmodelled and can dominate — that omission favours neither side and is the largest single limitation here.
- ⚠️ **Eight prints is eight prints.** The CCL sample spans a cruise-demand boom (2024–25) into a de-rating (2026); the two halves are not the same regime, which is exactly why the last-3 / last-4 qualifiers are written beside the headline numbers rather than under them.

---

## 4 · ⭐ THE MULTI-QUARTER FRAME — added 2026-09-19 late, **Will-directed, and it corrects the SCOPE of §3's NCLH verdict**

**Will's challenge, in his words: *"we see no edge even with the oil pricing issues, loss of canadian tourism, alleged iranian hacking of commercial vessels?"* and then *"the rest of 2026 is not very long."* Both land. This section exists because they do.**

⛔ **SCOPE CORRECTION TO §3 — STATED BEFORE THE NEW WORK, BECAUSE IT QUALIFIES A VERDICT ALREADY PUBLISHED.** §3's *"EV ≈ 0, CONDITIONAL, no card"* on NCLH was measured **against the print-day base rate for a print-spanning structure.** **None of the three channels Will names is a print-day event** — they are multi-quarter transmission. **Construction rule #16** (match the expiry to the view's horizon) and **#18(a)** (a multi-quarter catalyst needs multi-quarter tenor) mean **§3's verdict does not transfer to the trade he is describing, and must not be read as covering it.**

### 4.1 · The three channels, graded at the OWNING desks — two weaken, one is an open hole

| channel | owner | status |
|---|---|---|
| **Fuel / oil** | BRENT · CRUISE | **52% hedged — but ONLY "rest-2026."** ⚠️ **Will is right that this is short: ~3.4 months from today, and `Dec-18-26` options EXPIRE 13 DAYS BEFORE THE CLIFF.** 🔴 **Fleet-wide grep returns NOTHING on NCLH's 2027 coverage — nobody holds it.** ⇒ **My earlier "the channel is halved" was scoped to a window the proposed trade does not live in.** |
| **Iranian vessel hacking** | FALCON · CRUISE | ⛔ **CRUISE assessed it THIS DAY, at Will's prompting: *"REAL EVENTS, OVERSTATED HEADLINES, NO CRUISE EXPOSURE ON THE EVIDENCED CHANNEL."*** The propulsion/navigation version traces to **Iranian state media during an active conflict (D3)**; **USCG+FBI say no operational disruption (B2)**. Sourcing runs **inverse** to the alarm. A separate real cruise exposure runs through **data, not the helm**. |
| **Loss of Canadian tourism** | ⚠️ **NOBODY** | 🔴 **ZERO hits across CRUISE, CARL and FALCON. The fleet does not track this at all.** ⇒ **It is the only one of the three that is genuinely un-priced here — and it is un-priceable BY ME, because no desk has measured it.** Routing ask, not a TERRY finding. |

**`N_eff`:** fuel and maritime theatre **share a Middle East antecedent**; Canadian tourism is independent. `N_claimed = 3`, **`N_eff ≈ 2` before grading, ≈ 1 after** (one channel graded overstated at its owner, one halved-then-unknown, one unmeasured).

### 4.2 · The structural fact that FAVOURS the long tenor — NCLH's vol term structure is flat

Put IV, own pull 2026-09-18: **`Dec-18-26` 50.20% · `Jan-15-27` ~50.2% · `Mar-19-27` 49.37% · `Jun-17-27` ~51–53%.** **Flat 48–53% out to nine months.** ⇒ **Nine months of transmission time costs the same VOLATILITY as three.** Doubling tenor `Dec → Mar` costs **+39% premium** and moves breakeven only **3.8pp** further (`−10.41%` → `−14.16%`). **The opposite of the CCL front-month, which charges ~13 extra points for one event.**
⚠️ **Counterweight, and it is material: execution degrades badly with tenor.** `Dec-18 14P` spread **2.25%**, OI **3,870**. `Mar-19-27 14P` spread **12.43%**, OI **244**. `Jun-17-27` has **no 14 strike at all** (10 · 13 · 15 · 18 · 20 · 22) and spreads 6–76%. **Cheap in vol, expensive in execution.**

### 4.3 · 🔴 THE MEASUREMENT — and it does NOT go Will's way

The multi-quarter analogue of the 8-print base rate: NCLH's **own empirical overlapping horizon returns**, payoff valued **at expiry**, debits at the **ask**, **no early exit credited** (conservative).

⛔ **BEFORE READING THE `P(profit)` COLUMN: it is WITHDRAWN as a decision input — see §5.6.** Independent windows behind it are only `35 / 17 / 11 / 11` with 95% CIs spanning `10–57%`. **The column is retained to show the method, never as odds.** ✅ **The EV columns' SIGN is what survives** (`P(EV>0) ≤ 3%`, §5.4).

| structure | debit | E[payoff] | **EV (10y)** | **EV (ex-2020)** | ~~P(profit)~~ **(withdrawn, §5.6)** |
|---|---:|---:|---:|---:|---:|
| `Dec-18-26 14P` (3m) | $1.35 | 1.07 | −19.6% | **−20.5%** | 28.2% |
| `Mar-19-27 14P` (6m) | $1.88 | 1.39 | −22.2% | **−25.9%** | 28.6% |
| `Jun-17-27 13P` (9m) | $1.92 | 1.25 | −28.6% | **−34.9%** | 24.7% |
| `Jun-17-27 15P` (9m, ITM) | $3.00 | 2.30 | −22.0% | **−23.4%** | 31.3% |

🔑 **EVERY tenor is negative-EV against NCLH's own decade, and GOING LONGER MAKES IT WORSE, NOT BETTER.** **The flat term structure does not mean duration is free — it means the options are priced consistently, and a longer window gives the stock more time NOT to fall as well as more time to fall.** ⛔ **So "buy more time because the thesis is slow" is refuted on this desk's own data.**

⚠️ **THE LIMIT THAT CUTS WILL'S WAY, AND IT IS THE REAL ONE: this is an UNCONDITIONAL base rate — a random start date over ten years. Today's setup is not random.** NCLH is −43.6% from its peak, at a multi-year low, into a named hedge cliff. **If the forward distribution is genuinely worse than the unconditional history, these numbers understate the trade.**
⇒ **THE HURDLE, QUANTIFIED — which is the useful output of this section:** **the forward 6–9 month distribution must be roughly `25–35%` worse than NCLH's own decade for these puts to break even.** **That is a THESIS claim, not a pricing claim, and it is not mine to make.** **The three channels above are exactly such a claim — and after grading, one is overstated at its owner, one is halved-then-unknown, and one is unmeasured by anyone.**

⚠️ **Effective `n` is NOT the overlap count:** ~10 years gives **~40 independent 3m windows, ~20 6m, ~13 9m.** The 2,000+ rows are the same decade re-counted. **Quote the independent count** (rule #19).

### 4.4 · Verdict — unchanged in direction, narrowed in reason, and with the ask named
**Still NO CARD.** ⛔ **But the reason is now specific: at every tenor tested the option is priced `20–35%` above its own unconditional base rate, and the thesis must carry that whole gap.** ⇒ **The one input that could change it is the one nobody holds: size the Canadian-tourism exposure for NCLH, and establish 2027 fuel coverage from the 10-K/10-Q.** **Both are routing asks to CRUISE/CARL/BRENT, not TERRY findings.**

---

## 5 · ⛔ HOW GOOD ARE §4's NUMBERS? — **Will asked; the answer RETRACTS one of them as a decision input.** *(2026-09-20)*

**Question put to the desk: *"How confident are we regarding this chance of profit? How is it determined?"*** Answered by stress-testing rather than by restating.

### 5.1 · What `P(profit)` literally is — no model in it at all
> `P(profit)` = the fraction of historical windows in which the put finished worth **more than the ask paid** = **`P(return over the horizon < breakeven)`**, where `breakeven = (strike − ask)/spot − 1`.

**There is no Black-Scholes here, no volatility input and no distributional assumption.** It is a raw count: *how often did NCLH actually fall that far, over that many trading days, in the last decade?* **Its entire content is the historical sample — so its reliability is the reliability of that sample, and nothing else.**

### 5.2 · 🔴 THE SAMPLE IS FAR SMALLER THAN THE ROW COUNT SUGGESTS, AND THE CONFIDENCE INTERVALS ARE RUINOUS

| structure | breakeven | overlapping n | P quoted | **independent n** | **P (indep)** | **95% CI (Wilson)** | winners |
|---|---:|---:|---:|---:|---:|---|---:|
| `Dec-18-26 14P` | −10.41% | 2,198 | 28.2% | **35** | 25.7% | **14.2% – 42.1%** | k=9 |
| `Mar-19-27 14P` | −14.16% | 2,135 | 28.6% | **17** | 23.5% | **9.6% – 47.3%** | k=4 |
| `Jun-17-27 13P` | −21.53% | 2,072 | 24.7% | **11** | 27.3% | **9.7% – 56.6%** | **k=3** |
| `Jun-17-27 15P` | −15.01% | 2,072 | 31.3% | **11** | 36.4% | **15.2% – 64.6%** | k=4 |

⛔ **The nine-month figures rest on THREE AND FOUR INDEPENDENT OBSERVATIONS. A 95% interval of 10%–57% is not a probability, it is the absence of one.** ⚠️ **And the point estimate itself moves with the counting method** (28.2% overlapping vs 25.7% independent) — a tell that the overlap was doing work it should not have been.

### 5.3 · 🔴 THE EV IS DOMINATED BY ONE OR TWO WINDOWS

| structure | independent windows | finished ITM | **top-2 windows as a share of ALL payoff** |
|---|---:|---:|---:|
| `Dec-18-26 14P` | 35 | 18 | 36.9% |
| `Mar-19-27 14P` | 17 | 9 | **52.2%** |
| `Jun-17-27 13P` | 11 | 4 | **68.1%** |
| `Jun-17-27 15P` | 11 | 6 | 58.4% |

**At nine months, two windows out of eleven carry two-thirds of the entire expected payoff.** Remove the 2022 drawdown and the estimate is a different number.

### 5.4 · ✅ BUT THE **SIGN** SURVIVES EVERYTHING — block bootstrap resampling YEARS (preserves within-year autocorrelation), 2,000 draws

| structure | EV point | **90% CI** | **P(EV > 0)** |
|---|---:|---|---:|
| `Dec-18-26 14P` | −20.5% | [−51.8%, **−2.3%**] | **3.0%** |
| `Mar-19-27 14P` | −25.9% | [−72.5%, **−10.0%**] | **2.1%** |
| `Jun-17-27 13P` | −34.9% | [−81.7%, **−29.7%**] | **0.0%** |
| `Jun-17-27 15P` | −23.4% | [−66.6%, **−9.3%**] | **2.0%** |

🔑 **Every 90% interval EXCLUDES ZERO.** ⇒ **The DIRECTION of the verdict is well supported; the MAGNITUDE is not.** *"Negative-EV against its own history"* is defensible. *"−25.9%"* is a point estimate inside a 60-point band and must never be quoted bare.

### 5.5 · ✅ One choice checked and found NOT load-bearing
Excluding 2020 moves EV by only **1–6pp** and never changes a sign (`Dec` −19.6 vs −20.5 · `Mar` −22.2 vs −25.9 · `Jun 13P` −28.6 vs −34.9 · `Jun 15P` −22.0 vs −23.4). **The COVID-exclusion judgment does not decide the answer.**

### 5.6 · ⛔ THE RULING, AND IT RETRACTS SOMETHING I PUBLISHED

> 🔴 **`P(profit)` IS WITHDRAWN AS A DECISION INPUT. Do not cite the 25–31% figures.** They are three-to-nine-observation tail estimates with intervals spanning 10%–57%. **§4's table carries them and they should be read as illustrative of method, never as odds.**
> ✅ **What survives and is quotable: the SIGN of the EV, at every tenor, with `P(EV>0) ≤ 3%`. And the ordering — longer tenor is worse — holds in every specification tested.**
> ⚠️ **`P(profit)` was never the decision-relevant statistic anyway:** a cheap tail option can have low `P(profit)` and still be `+EV`. **EV is the number that decides; `P(profit)` is the number that feels like it does.**

### 5.7 · Four limits no resampling can repair — named, not buried
1. **UNCONDITIONAL.** A random start date over ten years. **Today is not random** (−43.6% from peak, multi-year low, into a named hedge cliff). **This is the limit that cuts toward Will's thesis and it is not quantified here.**
2. **REGIME / SAME-COMPANY.** NCLH's share count roughly doubled through the COVID dilution and its leverage was transformed. **Ten-year returns are not ten years of the same instrument.**
3. **NO EARLY EXIT CREDITED.** Payoff valued at expiry only. A managed position exits with time value ⇒ **this biases the estimate DOWNWARD. Conservative, but a real bias, and it flatters the refusal.**
4. **~10 YEARS IS ALL THERE IS.** NCLH listed in 2013. **The sample cannot be enlarged, only re-cut.**

### 5.8 · Contrast worth keeping — not every figure in this file is this weak
**The CCL `implied 6.94% vs realized RMS 5.53% = 1.25×`** result (§0-bis) is **better determined than any of the above**: it compares two directly measured quantities rather than estimating a tail probability, and needs no distributional assumption. ⚠️ **It is still `n=8` on the realized leg, and `J` is model-implied from two quotes — so it is *better*, not *strong*.**
