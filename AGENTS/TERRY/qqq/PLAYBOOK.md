# QQQ PLAYBOOK — how this desk will trade QQQ

**Created 2026-08-04.** Grounded in `README.md` (the record) and `RESEARCH.md` (the measurements). **Nothing here is a thesis. It is construction.**

---

## 0. The premise, stated plainly

**The QQQ record is 8 expressions, ≈ −$3,081, and 8-of-8 in one direction. Four of the five failure modes are "a rule was written and not followed."**

⇒ **A sixth rule will not fix this.** Everything below is chosen because it works **structurally** — it removes the need for a decision this desk has already proven it will not make under pressure. *(The hard stop is 0-for-4 across four reviews. A control that has never once fired is not a control; it is a wish.)*

---

## 1. 🔴 HARD GATES — mechanical, pre-ticket, no judgement

**All five must pass. A failure is a NO TRADE, not a discussion.**

| # | Gate | Why this one |
|---|---|---|
| **G1** | **Max risk ≤ $500 (2R).** Computed **before** the ticket, from contracts × price × 100. | The 687P was **$843 = 3.4R**, oversized *before it was ever wrong*. |
| **G2** | **ONE QQQ ticket per session. A closed loser does NOT open a slot.** | **4 of 4** failures were same-day re-entries. 7/30: realized −$390, then bought **3.65×** the dead ticket the same session. |
| **G3** | **A harvest order is RESTING at entry** — not intended. Sell half at **+50%**; sell half at **≥+20% into any non-trading gap** (weekend/holiday). | The 687P was **+23.6% at Friday's close** and no rule said take it. |
| **G4** | **Max loss is capped by the STRUCTURE, not by an intention to exit.** | 0-for-4 on executing the hard stop. Structural caps execute themselves. |
| **G5** | **If the last 3 QQQ tickets were the same direction, the 4th in that direction must carry a WRITTEN refutation of "this is a bias, not a read"** — in figures, before the fill. | 8 of 8 short into a **+10.1%** four-session tape. |

> **G5 does not forbid a fourth short.** It forbids an *unexamined* one. The refutation has to be a measurement — a base rate, a level, a flow — not a chart impression. **Identical in spirit to the root-rule-#6 break test: show the number that refutes the proxy, or it is a chase.**

---

## 2. STRUCTURE — spreads over naked longs, and the reason is sizing, not safety

A naked long put and a debit spread both cap loss at the premium. **The reason to prefer the spread is that it lets the same view fit inside G1.**

| | 687P ×3 as traded | the same view as a spread |
|---|---|---|
| Cost | **$843** ⛔ 3.4R | ~$300–450 ✅ inside 2R |
| Directional exposure | 3 contracts | comparable |
| Gate G1 | **FAIL** | **PASS** |

**The trade was not wrong because it was a put. It was wrong because the expression cost 1.7× the cap for the exposure it bought.**

**Current vol regime says this is a reasonable tape for long premium — with a caveat:**
- RV20 **26.3%** vs VXN **25.9%** ⇒ **+0.3pp**, 78th percentile. **Options are fairly-to-cheaply priced vs what the index is actually doing.**
- ⚠️ **But RV is at the 86th percentile — you are buying after the expansion, not before it.** Cheap *relative to realized* is not cheap.
- ⚠️ **Volume is 0.77× the 1-year average.** The range is real; the participation is not. **Wide ranges on light volume overstate conviction in both directions.**

---

## 3. SETUPS — what the measurements actually support

### ✅ S1 — First test of the prior high (745–749): **do not fade it**
**Base rate: 86% break through on first test; 5-of-5 ex-bubble. Rejection is 14%.**
⇒ **Shorting a first touch of 745–749 fights a strong base rate.** The tradeable asymmetry is the *inverse*: **a genuine rejection there is rare, which makes it high-information** — a reason to *watch* for it, not a reason to pre-position for it.
**Level: 745.34 close / 748.65 intraday. Median 18 sessions from the V ⇒ a first test around mid-to-late August.**

### 🟡 S2 — Post-V continuation: **real but too thin to size**
**n=3 ex-bubble, 2 up / 1 down, and the loss was −21.9% over 3 months.** ⇒ **A directional tilt at most, never a position thesis.** Any base rate you see on this above n≈10 is carrying bubble-era rows that behave with the opposite sign.

### ⛔ S3 — Fading strength on "it looks stretched": **retired**
This is the expression the record is built on. **8 of 8, ≈ −$3,081.** It does not return without clearing **G5** with a measurement.

### ⛔ S4 — Anything ≤3 DTE carried through a non-trading gap while in profit
Killed by `daytrading/QQQ_DESK_CARD.md` §4b (added 8/4). **Named here so this lane cannot re-open it.**

---

## 4. ⚠️ THE HONEST GAP — we do not yet have a measured QQQ edge

The base rates in `RESEARCH.md` run **n=3 to n=11**, on a series whose most numerous rows are **not measurement-grade**. **None of them is strong enough to size up on.**

★ **And the QQQ record cannot teach us anything yet, because it was never a controlled experiment:** 8 tickets, one direction, variable size, no executed stops, no harvest rule. **Eight observations with eight uncontrolled variables produce zero information.**

⇒ **The near-term objective is not to find the edge. It is to make the record informative:**
1. **Standardise the expression** (§2) so tickets are comparable to each other.
2. **Enforce G1–G5** so size and management stop being confounds.
3. **Log every ticket with its setup ID** so the record can be sliced by setup rather than by date.
4. **Re-examine at n≥10 clean tickets.** Until then, QQQ is a **small-size, defined-risk lane** — not a conviction book.

*This mirrors `PAPER_BOOK_DESIGN.md` §5b: no scoring until N≥10 closed AND ≥5 distinct antecedents. The same bar applies here, and it is not currently met.*

---

## 5. PRE-TICKET CHECKLIST

```
□ G1  risk ≤ $500 (2R)              — contracts × price × 100, computed and written
□ G2  no other QQQ ticket today     — including a closed loser
□ G3  harvest order RESTING          — +50% half; ≥+20% into a gap, half
□ G4  max loss capped by structure   — not by an intent to exit
□ G5  if 3 prior same-direction      — written refutation, in figures, before the fill
□     setup ID named (S1/S2/…)       — or it is not a setup, it is a hunch
□     live chain pulled              — chain_fetch.py --no-cache --legs <strikes>   (exits 2 on a bad quote)
□     root rule #6 clean, or the break test satisfied in writing
□     what is driving the tape is KNOWN — an unexplained 3% session is a reason not to size
```

**APPROVAL REQUIRED — Will approves/rejects every QQQ ticket. TERRY never executes.**

---

*Owner: TERRY. Cards live in `setups/`; intraday rules live in `daytrading/QQQ_DESK_CARD.md`; this file governs construction and sizing for the instrument. **Revisit at n≥10 clean tickets, or whenever `v_episodes.py` materially disagrees with `RESEARCH.md`.***
