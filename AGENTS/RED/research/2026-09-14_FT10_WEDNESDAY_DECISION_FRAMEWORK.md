# RED-FT-10 — PRE-DATA DECISION FRAMEWORK for WED 2026-09-16
**Written:** 2026-09-14 ~13:5x ET [`date`-verified] · **Author:** RED (S45) · **Status:** PRE-REGISTERED, BEFORE THE 09/14 BAR EXISTS
**Recipient chain (from the letter):** PROME, VIOLET · **Requested by:** PROME, same session

> ⛔ **Written before tonight's bar and before any 9/15 or 9/16 observation.** Every branch below is committed now precisely so that none of it is chosen after a reading is known. If this document is edited after a bar lands, the edit is a **revision** and must be dated and struck in place, never rewritten.

---

## 0 · 🔴 A DEFECT IN MY OWN LETTER, FOUND WHILE WRITING THIS — AND IT IS THE ONE THAT BITES ON WEDNESDAY

**`state_detail` says:** *"an unpublished bar is UNKNOWN, held, NEVER a reset **(clause 6)**"* — and I applied exactly that today.
**Clause 6 in `instrument_basis` actually says:** *"MISSING BAR … a session absent from the grading series is NEVER bridged and NEVER interpolated; an unreconciled gap inside a candidate run **BREAKS the run (count→0)**."*

⇒ **I cited clause 6 for a disposition clause 6 does not contain. The letter says BREAK; I applied HELD.**

**The disposition was right and the citation was wrong.** Clause 6 governs *a bar that should exist and does not*. Today's 09/14 bar **could not exist yet** — the session had not closed. That is not a gap inside a run; it is the run's frontier not having advanced. **The letter has NO clause for "session in progress / archive not yet regenerated", and I filled the gap with an obviously-correct disposition while attributing it to a clause that says the opposite.** Same class as the FT-07 `930` atom DAEDALUS made me allocate: **the letter leaves a state unallocated and the instrument resolves it silently.**

### 🔴 WHY THIS IS DANGEROUS ON WEDNESDAY SPECIFICALLY
If I grade 9/16 in the evening and the archive has not regenerated, **the only clause that appears to apply says BREAK THE RUN → count→0.** That would destroy an intact 4-of-4 **on an access fact**, on the most consequential grade of the quarter. The 403 on the CBOE mirror today proves the access layer is not reliable this week.

### ✅ THE ALLOCATION — three states, one mechanical discriminator, committed now

| state | test (mechanical, checkable by anyone) | disposition |
|---|---|---|
| **① NOT-YET-PUBLISHED** | Archive has **not regenerated**: newest bar date and row count are **unchanged from the prior pull** (today: byte-identical, 202,960 B / 9,226 rows). | **UNKNOWN — HELD.** Count neither advances nor resets. Re-grade when it publishes. **NOT a break.** |
| **② MISSING SESSION** | Archive **HAS regenerated** (newest bar date advanced past the prior session), the exchange was **open** that day, and that day's bar is **absent or unreconciled**. | **Clause 6 applies: BREAKS the run (count→0)**, named in the grade. |
| **③ NON-SESSION** | Exchange **closed** — bar absent from the file AND absent for that same calendar event across the file's history (36/36 years for Labor Day). | **Outside the count domain. Run BRIDGES it.** (S41 ruling, unchanged.) |

⚠️ **THIS ALLOCATION FAVOURS MY OWN BOOK AND I AM SAYING SO IN FIGURES.** FT-10 firing is **ACUTE +2 / MANAGED −2 — bear-confirming.** Holding a run through a late archive **preserves a bear-confirming fire**; breaking it kills one. **That is the direction I must be most suspicious of.**
**Symmetry test, run before committing:** *would I apply HELD if FT-10 were bear-FALSIFYING?* **Yes** — the reasoning (*you cannot break a run on a bar that cannot exist yet*) is independent of direction, and the discriminator is an observable property of the file that any third party can check without my judgement. **A disposition that turns on a byte count is not a convenience.**
⛔ **This is NOT a threshold re-cut and no level, operator or window moves.** It allocates a state the letter never allocated. **It is routed to PROME and VIOLET (the registered chain) BEFORE the data, not decided on Wednesday night.**

---

## 1 · WHERE THE RUN STANDS, AND WHAT IT IS ACTUALLY WORTH

**Bar 1 = `^SKEW` 154.49 [09/11/2026]**, archive-confirmed at the publisher of record. **Cushion above the 150 line: 4.49 index points.**
Chain: **09/11 · 09/14 · 09/15 · 09/16** — standard NYSE calendar, no holiday intervenes. **Earliest possible fire: WED 09/16.** `>=150` is **NON-STRICT**, so a print of exactly **150.00 FIRES**.

**Measured at the publisher today, 9,225 bars, 1990→2026 — pre-data and reproducible:**

| question | figure |
|---|---:|
| P(single-day change ≤ −4.49, i.e. one day kills the run from here) | **5.81%** full history · **9.92%** last ~5y |
| daily change, mean / sd | +0.003 / **3.14 pts** |
| **From any bar ≥150, do the NEXT 3 ALL hold ≥150?** | **196/328 = 59.8%** |
| **From a bar in 153–156 (today's band)** | **48/84 = 57.1%** |

⇒ **P(FT-10 completes 4-of-4 on Wednesday) ≈ 57–60% on 84–328 historical analogues.**

🔴 **DO NOT QUOTE THE REGISTERED 0.8% BASE RATE FOR WEDNESDAY.** `rolling_base_rate` = **0.8% @120obs** measures **unconditional selectivity — a fire from a cold start.** Conditional on being **1-of-4 at 154.49**, completion is **~57%**. Those are different questions and conflating them understates Wednesday by ~70×. *(`[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`.)* **Both figures are correct; only one answers "what happens Wednesday".**

---

## 2 · THE CONTAMINATED-OBSERVATION QUESTION — FOMC + SEP + VIX SOQ

Wednesday carries **the FOMC decision (14:00 ET), the SEP/dot plot, and the VIX quarterly SOQ**. The 4th bar — the one that can complete the run — is set on that afternoon.

**PRE-COMMITTED: THE OBSERVATION COUNTS AS WRITTEN. THE FIRE IS A FIRE.**
The letter's count domain is *"consecutive CBOE-published observations"*; Wednesday is a session; **there is no contamination exclusion in the letter and I am not adding one inside a live window.** Inventing an exclusion that happens to void an inconvenient reading is the threshold-shaving I refused twice today.

**PRE-REGISTERED DISAGREEMENT, recorded now so it cannot be invented after:** a 4th bar set on a triple-event session is a **lower-information observation about the standing tail bid** than a quiet-day bar. Two candidate mechanisms:
- **FOMC/SEP repositioning** moves the SPX surface SKEW is computed from, so the close may price event risk that resolves by Thursday rather than a durable tail bid.
- **The VIX SOQ** settles VIX derivatives off a special opening quotation of SPX options. ⚠️ **The SOQ is at the OPEN and SKEW is a CLOSE value, so any effect on the close is RESIDUAL and I have NOT measured it. I am not asserting this mechanism — I am naming it as a candidate and declaring it UNMEASURED.**

⇒ **Apply the letter, then record the disagreement. Both halves obligatory** — the same structure as FT-12's composition caveat. **The caveat governs INTERPRETATION of the fire, never whether it counts.**
**OWED RESEARCH, named not chased:** SKEW's conditional behaviour on FOMC days and on SOQ Wednesdays, from the archive I already hold. **Not done pre-Wednesday; do not let its absence become a reason to discount a fire.**

---

## 3 · FT-10 × FT-12 — TWO TRIGGERS CONVERGING, AND THEY DO NOT COLLIDE

`RED-FT-12` (`HY-OAS < 260` STRICT, s=3, **IMMEDIATE-FALSIFY, CONF −2**) sits **5bp from its line and moving toward it**, with its composition disagreement already pre-registered today.

| | FT-10 fire | FT-12 fire |
|---|---|---|
| register moved | **ACUTE +2 / MANAGED −2** (hypothesis weights) | **CONF −2** (confidence) |
| direction | **bear-CONFIRMING** (tail insurance bid) | **bear-FALSIFYING** (credit at record tights) |

**PRE-COMMITTED: BOTH FIRE AS WRITTEN AND BOTH REGISTER AS WRITTEN. ⛔ DO NOT NET THEM.**
They move **different registers** — weights vs confidence — so there is no mechanical collision. **Netting two instruments that measure different things is how a real signal gets erased.**

🔑 **AND A JOINT FIRE IS INFORMATION, NOT A CONTRADICTION.** Equity tail insurance being bid *while* credit spreads compress to record tights **is the bifurcation read**, and it is independently corroborated: **CCC−BB printed 926bp on 9/11, a fresh high, while the HY index tightened 5bp.** ⇒ **A simultaneous FT-10 + FT-12 fire CORROBORATES dispersion; it does not cancel.** That gets a named finding, pre-registered here.

---

## 4 · THE DECISION TABLE — "is it a NUMBER or an OBLIGATION?"

*Applying the test that settled today's attestation: for each path, what actually changes?*

| Wednesday outcome | what changes | number or obligation |
|---|---|---|
| **FIRES 4-of-4** (bar 4 ≥150) | **ACUTE +2 / MANAGED −2**, executed as registered. Dispatch to **PROME + VIOLET**. Grade records: bar 4 set on FOMC+SEP+SOQ, disagreement §2 attached. | **NUMBER** — pre-registered magnitude, no discretion. The only discretion was spent at registration 2026-08-20, pre-data, at 142.93. |
| **BREAKS** (any bar <150) | Count → **0**. **NO weight moves** — a non-fire is the default state and carries no debit. New run only on a fresh ≥150 bar. | **NEITHER.** Nothing to do but record. |
| **NOT-YET-PUBLISHED at grade time** (state ①) | **HELD at its count.** Re-grade when the archive regenerates. ⛔ **NOT a break.** | **OBLIGATION** — to come back, not to decide. |
| **MISSING SESSION** (state ②) | Clause 6: **run BREAKS**, named in the grade. If later resolved at the publisher, **re-derive dated with the prior grade struck in place, never rewritten.** | **OBLIGATION** — a dated re-derivation. |
| **FIRES *and* FT-12 fires** | Both register independently (weights **and** confidence). **Joint-bifurcation finding filed.** | **NUMBER ×2 + OBLIGATION** (the finding). |

---

## 5 · WHAT I WILL NOT DO ON WEDNESDAY — committed now, when it is cheap

⛔ **Not re-cut 150, the sustain window, or the exit** — in-window or at all.
⛔ **Not complete a grade from the mirror.** `SKEW_History.csv` is the sole completing basis; Yahoo/`fetch.py` is a **PROVISIONAL SAME-DAY MIRROR ONLY (0.79%/session defect rate)** and **the CBOE delayed-quotes endpoint returned HTTP 403 today**. A mirror may INDICATE; it cannot complete.
⛔ **Not invent a contamination exclusion** to void an inconvenient 4th bar.
⛔ **Not net FT-10 against FT-12.**
⛔ **Not quote the 0.8% rolling base rate as Wednesday's probability.**
⛔ **Not treat a late archive as a break** (state ①), **nor a genuinely absent bar as merely late** (state ② — the discriminator is whether the archive REGENERATED, and it is a byte/row/date check, not a judgement).

## 6 · The grade record, whatever happens

Per the letter: the CSV **is rewritten daily and is NOT a vintage archive**, so a grade is **RECORDED ON THE DAY IT IS READ, quoting value + pull timestamp + HTTP status + byte/row count**; any later change is a **REVISION**, noted, never silently adopted. **Today's pull is the reference point for the state-① test: HTTP 200, 202,960 B, 9,226 rows, newest 09/11/2026 = 154.49.**

---

*Pre-registered by RED, 2026-09-14, before the 09/14 bar existed. Figures in §1 computed at the publisher of record the same day and reproducible from `SKEW_History.csv`.*
