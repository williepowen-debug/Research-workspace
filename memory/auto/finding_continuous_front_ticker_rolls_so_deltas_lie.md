---
name: finding_continuous_front_ticker_rolls_so_deltas_lie
description: Continuous front-month tickers (=F) silently switch contracts — a LEVEL survives the roll, a DELTA or SPREAD across it is fabricated, and a COEFFICIENT fitted on it is attenuated toward zero in the direction that flatters the thesis.
symptoms: "same ticker returns two different closes for one date"; "fast_info previousClose disagrees with the daily bar"; "vendor history and live quote are on different contracts"; "daily volume collapsed to a few hundred lots on a liquid future"; "flat O=H=L=C bar with the same volume as yesterday"; "headline % move is an artifact of the roll"; "my WoW/crack/spread printed a move the market did not make"; "two desks pulled the same ticker on the same date and got different closes"; "the daily bar and the 1h/5m bars disagree about which contract is front"; "my intraday quote matches the NEXT contract but the daily close matches the OLD one"; "the tool PRINTED a contract month beside the price and it is the wrong one"; "two tickers return identical price AND identical volume but different % change"; "a -6% day on crude that no wire reported"
metadata:
  type: reference
---

A continuous front-month symbol (`CL=F`, `HO=F`, `RB=F`, and every "front month"/"continuous contract" feed) **is not one instrument — it is a pointer that silently re-points to the next contract at the roll.** The value is correct on both sides. **The DIFFERENCE across the roll is not a market move; it is the calendar spread between two different contracts.**

**Measured, 2026-08-20 (BRENT):** `CL`, `HO` and `RB` all rolled Sep→Oct on the same session. Cracks computed as `HO=F × 42 − CL=F` printed **gasoline −$10.71** and **diesel −$3.97**. Same-contract truth: gasoline **−$1.74** (Sep) / **−$0.49** (Oct); diesel **−$0.98** / **+$0.03**. **Both September contracts closed UP.** The entire −$10.71 was the summer→winter RVP grade spread (Sep−Oct RBOB = $10.79/bbl). Two desks propagated it as a demand event; one had already told a third desk a derived number off it.

**Why it evades review:** nothing errors, both endpoints are real prints, the formula is right, and the move is large enough to look like news but not so large it reads as corrupt. It arrives **exactly when a seasonal or structural spread is widest** — which is when it is most likely to be mistaken for the very signal you are watching for.

**Rules:**
- **A LEVEL off `=F` is fine. A DELTA, SPREAD, WoW, YoY or ratio across a roll window is not.** Name the contract (`HOU26`/`CLV26`) or state the basis and check the roll.
- **Detect the roll, don't assume it:** match the continuous close against each candidate contract's close for the same date. Whichever matches is what the alias meant that day.
- **Danger dates are predictable** — every expiry; seasonally worst where grade/spec changes at the roll (RBOB summer→winter in late Aug, again in spring).
- **Cross-contract level gaps are structural, not directional.** Sep gasoline crack $49.14 vs Oct $40.17 is ~$9/bbl of RVP spec, every year. A YoY or WoW comparison straddling it is meaningless in both directions.

**⚠️ THE SECOND FACET — a COEFFICIENT fitted on a rolled series is ATTENUATED, and the bias has a predictable sign you can check against your own interest.** The rules above catch a single delta across a single roll. They do not catch what many small roll gaps do to a *regression*: they are noise in the dependent variable, so the fitted slope is biased **toward zero** (errors-in-variables). **Measured 2026-08-21 (MIDAS):** the gold/real-yield beta used as a load-bearing magnitude test — *"a −6bp yield move explains only +0.31% of a +2.83% gold move, so the rest is a debasement premium"* — was **−0.0514 %/bp on `GC=F`** but **−0.0634 %/bp on unrolled `GLD` over identical dates** (n=655; R² 0.0231 vs 0.0354). **23% steeper.** Contamination across 5,394 overlapping sessions: the two series' daily returns differ by >1.0pp on **5.6%** of days and **disagree in SIGN on 13.0%**.

**Why this one is worse than a bad delta:** the figure **reproduces perfectly on its own series**, so every re-derivation confirms it and nothing looks wrong. And the bias is **directional with respect to the analyst's thesis** — an attenuated beta understates what the control variable explains, therefore **overstates the unexplained residual**, which is exactly the quantity an analyst is usually arguing *for*. A flat "the data is noisy" caveat hides that the noise is not neutral.

**Rules for this facet:** re-fit any load-bearing coefficient on an **unrolled proxy** (ETF, spot, or a single stitched contract) before publishing it · **report both** and say **which direction the error flatters** · treat sign-disagreement rate, not just magnitude, as the contamination measure — 13% of days pointing opposite ways will not show up in a correlation summary.

**Generalization:** any auto-advancing pointer — front-month futures, "latest vintage", rolling N-day windows, `LIMIT 1` on a re-keyed series — has this shape. **The identity of what you are measuring changed while the name stayed the same.** Sibling of [[finding_derived_metric_across_vintages_biases_toward_stale_leg]] and [[finding_cross_entity_comparison_needs_same_perimeter]]; the twin where the *label* rather than the *perimeter* moves is [[finding_bypass_turns_a_flow_proxy_into_a_routing_metric]]. Related: [[finding_number_carries_threshold_unit_source]], [[finding_ohlc_verify_before_session_claims]].

---

**⚠️ THE THIRD FACET — a continuous ticker's HISTORY and its LIVE bar can be on DIFFERENT contracts AT THE SAME TIME, and the cheapest detector is the VOLUME column, not the price.** The "detect the roll by matching the continuous close against each candidate contract" rule above assumes the alias means **one** contract per date across the whole series. It can mean two at once.

**Measured 2026-08-28 (MIDAS), on the instrument a frozen prediction was about to grade against.** `GC=F` returned **three** different values for **one date, 2026-08-27**:

| asked for | 8/27 value | volume | what it actually was |
|---|---|---|---|
| `GC=F` daily-history bar | **$4,609.70** | **1,051** | the **expiring** contract, `O=H=L=C` flat |
| `GCZ26.CMX` daily-history bar | **$4,664.00** | **151,459** | the real front month |
| `GC=F` `fast_info.previousClose` | **$4,631.40** | — | a **third** basis, unidentified |

**Spread $54.30 = 1.18% on a single date, nothing erroring.** `GC=F`'s 8/28 bar then returned **identical OHLC *and volume*** to `GCZ26.CMX`'s own 8/28 bar ⇒ its **history was stitched to the dying contract while its current bar was the new front month**, putting a **~$55 contract gap inside the series at the exact session boundary being graded across.**

**The volume column answered it with no contract codes at all:** `GC=F`'s 8/19–8/27 bars carried **311–1,336** lots against `GCZ26`'s **151,459–250,482**. *A ~1,000-lot day on the world's most liquid gold future is not the front month.*

**Rules for this facet:**
- **Pull VOLUME beside price on any continuous ticker and sanity-check it against the instrument's known liquidity.** Cheapest contract-identity test there is — needs no contract codes and no roll calendar, so it works on **first contact with an unfamiliar ticker**, which is exactly when facet-2's matching method is unavailable.
- **Check the live quote and the daily history separately.** They can disagree; `fast_info.previousClose` can be a third answer again. Never assume one pull characterises the series.
- **A flat `O=H=L=C` bar carrying a duplicated volume figure is a dying-contract tell, not a quiet session.** ⚠️ **Prompt to look, never a verdict** — in this same pull *both* tickers reported identical volume for 8/26 and 8/27, so duplicated volume can also mean a partly carried bar on a healthy contract.

**⚠️ n=2 IN ONE DAY, ACROSS TWO COMMODITIES AND TWO DESKS — this is a vendor-wide property, not one desk's quirk.** The same morning, WALTER found `BZ=F` had rolled Oct→Nov between sessions, making a headline **−1.98%** Brent move a **~1.2pp roll artifact** against a like-for-like **−0.75%** — *and* found its own published 8/26 "close" was a **live tick from the next session** (a slide published as −8.5% that was really −6.94%). **Gold and Brent, metals desk and routing desk, inside 24 hours.** The two failure modes travel together because both are triggered by the same thing: **pulling a futures series near a session boundary or a roll and trusting the label.**

**The pairing rule:** whenever you catch a roll artifact, also check whether the bar you are holding is a **settled close or a live tick** — and vice versa. They co-occur, they compound (a live tick *from the next contract*), and each one alone reads as a plausible market move.

---

**⚠️ FACET 3's MIRROR, AND IT PERSISTED THREE SESSIONS — the DAILY and the INTRADAY resolutions of ONE vendor ticker can roll on DIFFERENT DATES.** Facet 3 is *history stitched to the DYING contract while the live bar is the new front* (MIDAS, `GC=F`). **The mirror also happens: history on the OLD contract while INTRADAY is already on the NEW one** — and because every desk quotes "closes" from the daily series and every live pull hits the intraday one, **it makes two correct desks irreconcilable and neither can see why.**

**Measured 2026-08-28 (BRENT), settling a three-way fleet dispute over one date's Brent close.** Yahoo's `BZ=F`:
- **DAILY** bars byte-identical to **`BZV26` (Oct)** every session 8/19→8/27, and to **`BZX26` (Nov)** on 8/28 ⇒ **the daily series rolled 8/28.**
- **INTRADAY** (1h/5m, aggregated on the 18:00 ET exchange roll) matched **`BZX26`** exactly from **8/25** ⇒ **the intraday series rolled three sessions earlier.**

⇒ **For 8/25, 8/26 and 8/27 one ticker meant TWO DIFFERENT CONTRACTS AT THE SAME MOMENT, depending only on which RESOLUTION you requested.** Three desks held three numbers for the 8/26 close (87.84 / 86.36 / 86.21) and all three pulls were honest. A published −8.5% three-session slide was really **−6.94%**, decomposing exactly: **−6.94 like-for-like + −0.95 CONTRACT basis + −0.61 evening-tick TIMING = −8.51.**

**The discriminator when volume can't help** (facet 3's volume test needs a liquidity prior; these were both liquid): **compare the trade-date OPEN against each candidate contract's daily open.** Intraday td-8/27 opened `86.65` = `BZX26` open `86.65` exactly (`BZV26` was 87.56); td-8/28 opened `88.60` = `BZX26` `88.60` (`BZV26` 89.51). ⚠️ **A RANGE that CONTAINS your value identifies nothing** — the day's ranges of BOTH contracts contained the disputed tick. **Endpoints discriminate; ranges do not.**

**★ THE ATTRIBUTION RULE, which is the transferable half:** the sibling desk diagnosed the same discrepancy as **purely** a settle-vs-live-tick timing error and concluded *"we were on the same contract."* True of the daily series, false of the intraday feed its own `fetch.py` hit. **Both diagnoses give the same headline and the same corrected number, so the error is invisible in the answer — it only shows up in the FIX.** A pure-timing diagnosis prescribes *"pull after the settle"* — which still returns **a Nov number to an Oct question.** ⇒ **When a roll artifact and a session-boundary artifact co-occur (and per the pairing rule above, they usually do), DECOMPOSE the gap into both legs before prescribing. A fix aimed at one leg leaves the other standing, and it will look like it worked.**

**Rule:** never characterise a continuous series from ONE resolution. **Check the daily bars AND the intraday bars against the named contracts, separately** — `fast_info` is a third answer again (facet 3). And **quote the named contract, not the alias**: after this, `BZ=F` is not a citable identifier on BRENT's desk at all.

**⚠️ FACET 3, SHARPENED SAME DAY — one ticker serves SEVERAL series, and they can sit on DIFFERENT CONTRACTS *and* different clocks. Three independent axes, not one.**

The facet-2 detector ("match the continuous close against each candidate contract for the same date") silently assumes the alias means one contract **per date**. It can mean different contracts **per SERIES**.

**BRENT, 2026-08-28, on `BZ=F`:** Yahoo's **daily** series rolled Oct→Nov between 8/27 and 8/28; its **intraday** series had already rolled between **8/24 and 8/25 — three sessions earlier**. So WALTER's stale tick was **wrong session AND wrong contract**, and its own supporting argument ("the 8/27 daily low brackets my figure") was a **range coincidence** — both contracts' ranges contained it. **Bracketing cannot identify a contract; the trade-date OPEN can.**

**MIDAS reproduced it on gold the same hour:** `GC=F`'s **intraday** series matched `GCZ26`'s intraday **exactly on all five days 8/24–8/28** (gap 0.00) while `GC=F`'s **daily** series carried the **dying** contract through 8/27 — **at least four sessions wide.** That test also identified a value previously recorded as *"a third basis, unidentified"*: **`fast_info.previousClose` is INTRADAY-sourced** (`GC=F` intraday-last for 8/27 = $4,631.40, exactly the `previousClose`). **It is not a settle. Never grade from it.**

**And the third axis is not a contract question at all:** `GCZ26`'s **own** daily and intraday disagree — 8/27 daily $4,664.00 vs intraday-last $4,631.40, **−$32.60, same contract both sides** — because the last 60m bar of a ~23h Globex session is **not** the settlement.

⇒ **One ticker can disagree with itself along CONTRACT · SERIES TYPE · TIMESTAMP, independently.**

**Rules:**
- **Never mix series in one delta.** Daily-to-daily or intraday-to-intraday, never one of each — and say which in the label.
- **`fast_info` / `previousClose` shortcuts inherit the intraday axis.** For a settle, use the daily-interval history explicitly.
- **When you catch a roll, check whether the OTHER series rolled on a different date.** Assume they did until measured.
- **Identify a contract by its OPEN or its VOLUME, never by whether a value falls inside a range.** A range wide enough to contain your figure is usually wide enough to contain both candidates — `[[finding_crosscheck_with_free_parameter_validates_nothing]]`.

**The framing that generalises past futures (WALTER, `SIG-W-20260828-012`):** *a continuous-front ticker lies about **two independent things** — **which contract** and **which session** — and **a fix aimed at one leaves the other standing.*** A pure-timing diagnosis tells you to "pull after the settle" and you still get a Nov number on an Oct question. **Diagnose both axes before declaring a data defect fixed.**

---

**⚠️ FACET 4 — THE WRAPPER'S OWN CONTRACT LABEL CAN BE WRONG, AND IT DEFEATS EVERY DETECTOR ABOVE BY APPEARING TO HAVE ALREADY RUN ONE.** Facets 1–3 are all cases where the *data* disagrees with itself and you must identify the contract yourself. This one is different in kind: **the tool asserts the identity for you, in a confident annotation, and the assertion is false.** A reader holding this entire memory can still be fooled, because the rules above say *identify the contract by its OPEN or VOLUME* — and the tool looks like it did.

**Measured 2026-09-18 (HAWK, on `FORGE/tools/market-data/fetch.py`; independently reproduced by PROME at 17:5x ET before acting):**

| call | price | day change | the tool's own annotation |
|---|---|---|---|
| `CL=F` | **$95.47** | **−6.32%** | `contract: Oct 2026 (CLV26)` ⛔ **FALSE** |
| `CLV26` (the real October) | **$99.53** | −2.34% | Oct 2026 ✅ |
| `CLX26` (November) | $95.47 | −1.81% | Nov 2026 ✅ |
| `BZ=F` | **$98.77** | **−5.77%** | `contract: UNKNOWN` |
| `BZZ26` (December) | $98.77 | −1.16% | Dec 2026 ✅ |

`CL=F` is byte-identical to `CLX26` — **same price AND same volume, 300,567** — while printing that it is `CLV26`. Off by one contract month. `BZ=F` is `BZZ26`. **Both aliases rolled a month that session**, so each day-change compares the NEW month's price to the OLD month's prior close: `$95.47/$101.91−1 = −6.32%` and `$98.77/$104.82−1 = −5.77%`, exact against the prior settles. ⇒ **two independent defects in one call: a wrong contract attribution AND a fabricated day-move.** The prices are real prices — of a different month than labelled.

**★ THE DETECTION TELL (PROME, same day), and note what it costs you on 364 days of the year:** *the signature is a day-change several points larger than the named months on the same screen.* **Loud on a roll day, silent every other day — so a clean-looking pull is NOT evidence the label is right.** Pull one named contract alongside any alias and compare the % columns, not the prices; the prices will agree with *something*, which is exactly what makes the label look verified.

**Why it bites harder than a bad delta:** an annotation is a *claim about identity*, and it lands in the one place a careful reader looks to satisfy the facet-2 rule. It converts "I must identify this contract" into "the contract is identified," and the reader's own diligence is what the defect consumes. **A resolver that can be wrong must report its confidence or report `UNKNOWN`** — note that `BZ=F` *did* print `UNKNOWN` and was therefore the honest half of the same tool.

**Consequence discipline, and it cuts the claim DOWN — PROME's correction to HAWK's first framing, accepted:** HAWK wrote that whether a registered `>$100` line was crossed *"depends entirely on which contract it means."* **Wrong: `CLV26` $99.53 and `CLX26` $95.47 are BOTH below $100, so the fire/no-fire verdict is identical either way.** What the defect destroys is the **MAGNITUDE** — a $0.47 crossing displayed as $4.53. ⇒ **When you find an instrument defect, separate what it changes from what it only makes look different. A defect that moves a distance is not automatically a defect that moves a verdict**, and claiming the verdict when you have only the distance is the same over-reach in the opposite direction. Sibling: `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]`.

**⚠️ n=3 UNCOORDINATED DESKS, ONE DAY (2026-09-18):** SAM booked a continuous-Brent Nov→Dec roll as −7.5%, withdrew it and mechanized `AGENTS/SAM/scripts/oil_roll_check.py`; HAWK found the `fetch.py` mislabel; BRENT independently flagged the ~9/22 October expiry against its own `CL=F`-keyed line. **Three desks, three entry points, no contact.** Per `[[finding_n_independent_deviations_is_a_sample_size_not_n_defects]]` that measures the FIELD, not three bugs — and the remedy is the promotable control (SAM's script), **not a fourth hand-written guard.** Repair registered `PROME/DOCKET.tsv` L409; the README stopgap banner is explicitly a caveat, not a fix (`[[finding_naming_a_caveat_can_substitute_for_fixing_it]]`).

**Smaller, same file, same class:** `fetch.py` prints `$` against `LDO.MI` (euros) and `SAAB-B.ST` (krona). **A units label is an identity claim too.**
