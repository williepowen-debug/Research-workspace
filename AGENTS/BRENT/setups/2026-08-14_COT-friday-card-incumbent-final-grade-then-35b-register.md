# FRIDAY 2026-08-14 — COT CARD · **TWO STEPS, IN ORDER, NEITHER OPTIONAL**

**Built 2026-08-13 (Thu) so Friday is MECHANICAL.** · **Authority:** Will RULED all three 35b questions 2026-08-12 (~17:4x ET) — *"I approve the three BRENT changes"* — relayed `inbox/processed/2026-08-12_from-PROME_35b-successor-RULED-all-three-as-recommended-effective-after-8-14.md`. Spec of record → [`2026-08-12_35b-COT-successor-band-N1-build.md`](2026-08-12_35b-COT-successor-band-N1-build.md).

> ## ⛔ THE ORDER IS THE RULING. DO NOT COLLAPSE THE TWO STEPS.
> **1️⃣ The INCUMBENT band grades the Aug-11 vintage ONE FINAL TIME, under 35a REVERT semantics.**
> **2️⃣ THE RE-GRADE IS WRITTEN DOWN. Written, never inferred from the prior state.**
> **3️⃣ ONLY THEN does the 35b successor register.**
> **⛔ THE TWO NEVER RUN ON THE SAME VINTAGE.** *(Also on PROME's DOCKET 8/14 row. If this card and the docket disagree, re-derive from the build file — do not guess.)*

---

## 0. PULL — the primary, and the two traps in it

```
curl -s -A "Mozilla/5.0" https://www.cftc.gov/dea/newcot/f_disagg.txt -o /tmp/f_disagg.txt
grep 067651 /tmp/f_disagg.txt
```
**MM gross SHORTS = field 15 (1-indexed) of the 067651 row. Open interest = field 8.**
Verified 2026-08-13 against the 8/4 vintage: OI `1,886,816` · MM short `102,560` — **reproduces my recorded figure exactly.**

Then: `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/BRENT/scripts/cot_grade.py --expect 2026-08-11)`
**`exit 3` = release not fresh ⇒ WAIT.** Never grade last week's row as this week's print. ⛔ **DO NOT LET GRADES STACK.**

### ⚠️ TRAP 1 — `report_date` must be verified IN-ROW
The raw file carries the as-of date in the row itself (`2026-08-04` on the current vintage). **Read it there.** A file that has not rolled over yet looks identical to one that has, except for that field.

### ⚠️ TRAP 2 — QUERY BY MARKET NAME, NOT BY CONTRACT CODE *(found while building this card, 8/13)*
Socrata `72hh-3qpy` under contract code **`067651` spans a 2022 RENAME**:

| market_and_exchange_names | n | range |
|---|---:|---|
| `CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE` | 165 | 2018-12-11 → 2022-02-01 |
| **`WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE`** | **235** | **2022-02-08 → 2026-08-04** |

**Zero overlapping report dates — it is a clean rename, NOT two concurrent series.** ✅ `cot_grade.py` already carries the correct current name (checked 8/13; **no defect, and I am recording that it passed rather than implying it failed**). ⛔ **But a code-keyed query silently returns a 2018-start series**, and that is not cosmetic — see §2's window sensitivity. **Also note the legacy name uses a SPACED dash (` - `); the un-spaced form `CRUDE OIL, LIGHT SWEET-NY MERCANTILE EXCHANGE` matches NOTHING and returns a clean empty 200.** `[[finding_partitioned_source_returns_stale_window_at_200]]`

---

## 1️⃣ STEP ONE — INCUMBENT FINAL GRADE *(frozen letter, do not re-derive)*

| | |
|---|---:|
| Frozen base (2026-07-07 anchor) | **129,072** |
| Prior print (2026-08-04) | **102,560** |
| Cumulative vs base | **−26,512** |
| Frozen bar | **SPENT iff cum ≤ −25,000** |

### ⇒ THE ONLY ARITHMETIC FRIDAY NEEDS — PRE-COMPUTED

| 8/11 MM gross shorts | verdict |
|---|---|
| **≤ 104,072** | **`SPENT` HOLDS** — fuller-size branch STAYS LIVE |
| **≥ 104,073** | ⛔ **`SPENT` UN-FIRES** — modifier switches OFF, branch reverts to base case |

> ### ⛔⛔ THE SILENT-UNFIRE HAZARD — THIS IS WHY STEP 2 EXISTS
> **Under the 35a REVERT encode (Will 8/11) the modifier is a STATE re-read every print, NOT a latch.** It un-fires on a WoW re-gross of just **+1,513** — **P = 47.4% all-history (n=234) / 50.0% last 52wk. A COIN FLIP TO SWITCH ITSELF OFF WITH NOBODY TOLD.**
> **If nobody writes the grade, the branch's state is simply UNKNOWN and TERRY may size off a stale `LIVE`.**
> ✅ **WRITE THE VERDICT EITHER WAY — including "SPENT holds."** A re-affirmation is a grade; silence is not.

**Then the incumbent DIES.** Mark it superseded in `TRADE.md` + `REGISTRY.tsv` (`COT-FUEL`), superseded text preserved verbatim.

---

## 2️⃣ STEP TWO — REGISTER THE 35b SUCCESSOR *(only after §1 is written down)*

**Approved spec:** trailing-8wk-median base · 1.0-median-unit bar · ±0.5 median-unit NO-VERDICT deadband · **two-leg agreement, Leg B GATING** (33.6% NO-VERDICT rate accepted on the record).

### PRE-COMPUTED FRIDAY NUMBERS — reproduced 2026-08-13 from the build's own window

| quantity | value | basis |
|---|---:|---|
| Trailing-8wk median base (2026-06-16 … 2026-08-04) | **122,904** | ✅ reproduces the build file exactly |
| Median \|WoW\| unit | **9,160** | ✅ reproduces the build (n=235, **2022-02-08 → 2026-08-04**) |
| **Leg-A `SPENT` bar** | **shorts ≤ 113,745** | base − 1.0 median unit |
| **NO-VERDICT deadband** | **109,165 … 118,325** | bar ± 0.5 median unit (±4,580) |
| **Leg-B `SPENT`** | **OI-share ≤ 4.909%** | trailing-104wk median of MM short ÷ OI |

**Leg B input:** `OI-share = MM gross shorts ÷ open interest × 100` (field 15 ÷ field 8).
**VERDICT RULE: both legs must AGREE. Disagreement ⇒ `NO-VERDICT`, and NO-VERDICT is a real answer — it defaults sizing to the base case, the conservative branch.**

> ### ⛔⛔ A FREE PARAMETER I FOUND WHILE BUILDING THIS CARD — READ BEFORE REGISTERING
> **The median-unit window was never declared FROZEN or TRACKED, and the bar is materially sensitive to it:**
>
> | window | n | median \|WoW\| | Leg-A bar |
> |---|---:|---:|---:|
> | **2022-02-08 → 2026-08-04 (the BUILD window — APPROVED)** | **235** | **9,160** | **113,745** |
> | 2022-01-01 → 2026-08-04 | 240 | 8,586 | 114,318 |
> | full available series, 2018-12-11 → 2026-08-04 | 400 | 7,652 | 115,252 |
>
> **⇒ 1,508 contracts of spread in the bar across three defensible window choices — which is almost exactly the incumbent's ENTIRE margin (1,512).** `[[finding_threshold_level_is_a_measurement_not_a_constant]]` — **a threshold level is a MEASUREMENT, and an undeclared measurement window is a free parameter that lets a future session move the bar without ever deciding to.**
>
> ### ⇒ REGISTER IT **FROZEN** AT THE APPROVED BASIS
> **`median_unit = 9,160`, FROZEN, basis `n=235, 2022-02-08 → 2026-08-04`.** Will approved *"numbers as tabled in your build file"* — **the tabled numbers ARE the spec.** ⛔ **Do NOT re-measure the median unit at each print.** A TRACKED median would drift the bar weekly with no ruling and no record — the successor's whole purpose is to stop a verdict being a property of which window I happened to pick. **Re-basing the median unit is a NEW N1 BUILD and a fresh Will ruling, never a maintenance step.**

### RIDERS THAT MUST TRAVEL INTO THE SPEC TEXT
- ⛔ **NEVER REUSE THIS SPEC AS AN ENTRY TRIGGER** without a fresh build. It is a **SIZING modifier**: silence (NO-VERDICT) defaults to the conservative branch, which is acceptable for sizing and **NOT** acceptable for entry.
- **Will's four disclosed non-claims travel with the approval:** no out-of-sample test · **n=0 genuine physical reopenings** · no price validation (a positioning DESCRIPTOR, never shown to predict) · **vintage limit — the build's 8/4 basis PRE-DATES the 8/6 re-escalation and the 8/8 ADNOC attack, and Friday's 8/11 vintage is the first read that includes them and could move BOTH legs.**
- **Registration mechanics:** dated re-spec · superseded text preserved verbatim · **no threshold moved in the same edit** · `supersedes:` names the incumbent.
- **PROME opens the `GATES.tsv` row when the successor actually registers — not before.** Row 35b closes on the register, not on the approval.

---

## 3. ALSO PRINTING FRIDAY — do not let it get lost behind the COT

**🟠 Baker Hughes rig count (~Fri 8/15 per boot; catalyst row says 8/14 — take the print, not the calendar).** Grades **BRT-26** against the **frozen 457** line. Inherited state: **454** vs 457 = **3 to the line**; `BRT-26-RIGS` is flagged STALE (newest datapoint 7/31, 13d vs a 10d budget) and **clears on this print**.
⚠️ **TWO INDEPENDENT PULLS (LESSONS #1).** The Baker Hughes PRIMARY has been 403/timeout-blocked from this box for weeks — **if BRT-26 breaches on agreeing AGGREGATORS alone, SAY SO ON THE GRADE.** A breach recorded without its witness count is the defect, not the breach.

---

---

## 3b. ✅ MARKED 2026-08-14 — THE 5-SESSION FILL-DEBIT ASK IS ANSWERED, BROKER-CONFIRMED

**USO Sep-18 150/165 call spread — NET DEBIT = `$300.00` EXACTLY.** `[CONF, Robinhood positions capture 2026-08-14, back-computed from −$215.00 / −71.67%, tight to ±$0.02; record = FORGE/STATUS.md 8/14 reconcile commit `184a96100`, ANVIL-verified]`

| | |
|---|---:|
| Net debit (broker-confirmed) | **$300.00** |
| Current value | **$85.00** |
| Unrealized | **−$215.00 / −71.67%** |
| Max profit | ~**$1,200** at USO ≥$165 (≈4:1) |

✅ **This CONFIRMS the 7/25 "~$300 net debit" verbal estimate rather than correcting it** — the estimate was right, it had simply never been broker-verified, and it sat as an open ask across **5 sessions / 20 days** (queue row 20, open since 7/24). ⛔ **NOTHING MOVES ON THIS: the debit was already the number every card and packet used, so no break-even, strike, size or threshold changes. What changed is the EVIDENCE GRADE — `[EST, verbal]` → `[CONF, broker]`.** ⚠️ **RESIDUE, NAMED SO IT IS NOT MISTAKEN FOR CLOSED: exact fill DATE/TIME and PER-LEG prices are still unavailable — a positions view cannot show them, and only an activity-tab capture can.** *(The max-profit figure derives from the confirmed debit: 15-wide − $3.00 = $12.00 = $1,200. The card's earlier ~$1,135 / ~3.1× was computed off the ~$365 pre-fill quote and is superseded, not corrected — the fill was better than the quote.)*

---

## 4. CLOSING CHECK — three things that must all be true before Friday's session ends
1. **The incumbent's final verdict is WRITTEN** — `SPENT holds` or `SPENT un-fires`, in figures, with the 8/11 shorts number beside it. Not inferred.
2. **The successor is registered with `median_unit` marked FROZEN and its basis stated**, or explicitly NOT registered with a reason.
3. **`COT-FUEL`'s registry row and `TRADE.md` both reflect the same state.** One source of truth per metric — if they disagree, the session is not closed.
