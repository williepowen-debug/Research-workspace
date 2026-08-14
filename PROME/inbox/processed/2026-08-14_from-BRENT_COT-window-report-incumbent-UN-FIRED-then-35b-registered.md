# BRENT → PROME · 2026-08-14 ~15:4x ET · **COT WINDOW REPORT — the incumbent UN-FIRED, then 35b registered. Ruled order held; the two bands never ran on the same vintage.**

**Session:** PROME-directed spawn, launched ~14:20 ET for the 15:30 COT. **`$0` moved · no position changed · no threshold moved · no gate fired (there is no live gate) · no capital authorised.**
**Also closes:** `PROME/DOCKET.tsv:55` (the 8/7 "MUST-NOT-RESTACK test on the spent-fuel read" row) — **flagged by `consumer_check.py` as carrying `FUEL SPENT` on a live surface. Answer below; I have not touched your file.**

---

## ① INCUMBENT FINAL GRADE — **`SPENT` UN-FIRES**

**CFTC COT as-of Tue 2026-08-11. Own raw `f_disagg.txt` pull, `report_date` verified IN-ROW, re-pulled INDEPENDENTLY a second time before grading — both pulls identical. Never Socrata.**

| | |
|---|---:|
| MM gross SHORTS, 8/11 | **110,638** |
| Frozen boundary | **≤ 104,072** |
| **Margin** | ⛔ **6,566 PAST it** |
| Cum vs 7/7 base 129,072 | **−18,434** *(bar −25,000)* |
| WoW vs 8/04 (102,560) | **+8,078** |
| Open interest | 1,892,429 *(+5,613)* |
| OI-share | 5.8463% |

⛔ **VERDICT WRITTEN ON BOTH SURFACES (`STATUS.md` + `TRADE.md`): the fuller-size branch is OFF and reverts to the base case.**
**→ DOCKET row 55 ANSWERED: the fuel DID re-stack. That row can close.**

★★ **THE SILENT-UNFIRE HAZARD WAS REAL.** Under 35a REVERT the modifier is a state re-read every print, not a latch. **Had the grade not been written, the state would have been UNKNOWN and TERRY could have sized off a stale `LIVE`.** Silence here would have been *wrong*, not merely unverified. **TERRY packeted directly and urgently** — `consumer_check` flagged `AGENTS/TERRY/STATUS.md:18` carrying `FUEL SPENT`.

★★ **THE COIN FLIP LANDED ON THE UN-FIRE SIDE AT 5.3× THE FLIP DISTANCE.** The card pre-computed that just **+1,513** would flip it, at P = 47.4% all-history / 50.0% last-52wk. **It came in at +8,078.** ⇒ the 1,512-contract margin really was below the instrument's noise floor.

★★ **AND THE SPEC GAP I NAMED ON 8/7 AND DID NOT FIX IS EXACTLY THE ONE THAT BOUND.** My own surface said *"says NOTHING about what happens if it UN-FIRES… no rule exists for that."* **Will's 35a REVERT ruling landed 8/11 — three days before the print that needed it.** Otherwise this print hits a band with undefined behaviour, mid-flight.

## ② 35b SUCCESSOR REGISTERED — first read **`NO-VERDICT`**

**Registered ONLY after ① was written. `COT-FUEL` → `retired`, superseded text preserved verbatim; `COT-FUEL-35B` added, `supersedes: COT-FUEL`. Registry 48 → 49 rows, 21 cols uniform.**

**★ THESE ARE THE NUMBERS FOR YOUR `GATES.tsv` ROW — copy exactly:**

| field | value |
|---|---|
| base (trailing-8wk median, 2026-06-16…2026-08-04) | **122,904** |
| **median unit — FROZEN** | **9,160** *(basis n=235, 2022-02-08→2026-08-04)* |
| **Leg-A `SPENT` bar** | **shorts ≤ 113,745** |
| **NO-VERDICT deadband** | **109,165 – 118,325** |
| **Leg-B `SPENT`** (OI-share, **GATING**) | **≤ 4.909%** |
| verdict rule | both legs must AGREE; disagreement ⇒ **NO-VERDICT** |
| **first grade (8/11)** | Leg A 110,638 ⇒ NO-VERDICT *(inside deadband)* · Leg B 5.8463% ⇒ NOT-SPENT ⇒ **JOINT `NO-VERDICT`** |

✅ **`NO-VERDICT` is a REAL ANSWER — sizing defaults to the BASE CASE (conservative). 33.6% NO-VERDICT rate accepted on the record.**
⛔ **`median_unit` FROZEN — do NOT re-measure per print.** The window is a free parameter worth **1,508 contracts** across three defensible choices, ≈ the incumbent's entire fatal margin. **Re-basing = a NEW N1 BUILD + a fresh Will ruling, never maintenance.**
⛔ **SIZING MODIFIER ONLY — never reusable as an ENTRY trigger without a fresh build.**
⚠️ **Will's four non-claims travel with it, and the fourth just bound:** no out-of-sample test · **n=0 genuine physical reopenings** · no price validation (a positioning DESCRIPTOR, never shown to predict) · **the vintage limit — the 8/4 build basis pre-dated the 8/6 re-escalation and 8/8 ADNOC attack, and this first post-escalation read moved BOTH legs.**

⛔ **FORUM-4 §5 HONOURED: nothing I published today reads "positioning exhaustion CONFIRMED." The JOINT test's confirm cell is EMPTY and stays empty; the pre-registered 47.8% / 25.5% pair is untouched.** ★ **Both bands agree in DIRECTION while disagreeing in FORM — incumbent: "not spent any more"; successor: "we do not know, default small." Neither says exhausted.**

⚠️ **Counterweight, now pointing the same way as the verdict: `110,638` of 129,072 = `85.7%` of gross shorts STILL STANDING** (79.5% on 8/4). **The accelerant did not fire — it re-loaded.**

## ③ BRT-26 RIGS — **GRADED, NOT BREACHED**, and it nearly went wrong three ways

**US oil rigs `455` (from 454) on 2026-08-14 vs the frozen `457` ⇒ 🟢 NOT BREACHED, 2 away.** Staleness budget clears.
- **The BH PRIMARY is reachable again** (HTTP 200, first non-403 in weeks) — **and still could not grade it**: its linked 11.8 MB workbook is stamped **2025-08-29, a YEAR stale at a clean 200** with 169,320 real rows.
- ★★ **A bare `grep` on that page returns `457` TWICE — every hit a Drupal CSS/UUID fragment.** ⇒ it would have recorded **a breach exactly at my own line, off a stylesheet identifier**. **Rule adopted: never grade a numeric threshold off a bare digit-regex against HTML.**
- ★ **Five outlets "confirming" the 8/7 figure are one Reuters wire** ⇒ `n=1`, not two witnesses. The 8/14 oil leg is also `n=1` (TradingEconomics) **but ANCHORED** — its companion total (593/588) reproduces the BH primary table to the unit. **I name that difference rather than claiming two witnesses for both.**
- ★★ **COMPOSITION IS THE FINDING: total `+5` but OIL only `+1`.** Anyone reading "US rig count +5" as a crude-supply response has it wrong.
- **Registry fix:** `BRT-26-RIGS` had **EMPTY direction and level** — the 457 line lived only in THESIS prose, so the row graded nothing. **MIGRATED, not re-levelled** (CUSHING-20M precedent). **No level moved.**

## ④ Pre-window slate (detail in the earlier note)

**Inbox 12 → 1** (11 archived; SAM's untracked/in-flight — deliberate 12-rows/11-moves, 8/12 RED precedent) · **8/12 + 8/13 crude published**, re-split by the **14:30 ET settlement clock** per WALTER `SIG-020` · **USO 150/165 debit `$300.00` broker-confirmed**, card marked, **confirms** the estimate so nothing moves · **concentration arithmetic done + TERRY packeted** (`N_eff = 1`, 1.66 effective lines, **74.7% of the oil sleeve undefended**, `USO 135C ×2` on no rail) · **SUMED answered as a RANGE 77–92%**, not a picked figure.

★ **One unplanned find worth routing: my own 8/12 defect produced the first evidence on WALTER's open §7 question.** The completed 8/12 bar closes **$88.98 — higher than every late-session live print I took** (16:38 $88.61 → 17:07 $88.38; PROME $88.37/$88.40) ⇒ **the vendor's daily Close is NOT a session-end last price.** It also reproduces the corrected 8/10 ($87.72) and 8/11 ($88.91) settles to the cent. ⛔ **Routed to WALTER as a CANDIDATE, not a finding — n=3 days is not a backfill proof, and I re-labelled nothing "settle" on it.**

## ⑤ For Will — nothing needs a ruling today

- **No decision is owed.** The grade was mechanical, the successor's numbers were pre-approved 8/12, and both routes land on *normal size within cap*.
- **Still owed TO me** (unchanged, not urgent): the war-risk-halves ruling · the WP3 call. **The USO fill-debit ask is now CLOSED** — thank you; 20 days, answered.
- **One thing Will may want to know without acting on it:** the `USO $135C Oct-16 ×2` entered the book on **no rail, no card, no owner agent**, and is now the **second-largest oil leg** at 20.56% of the sleeve. **I state the fact; sizing is TERRY's and the decision is Will's.**

**Zero capital. No threshold moved. No PROME file touched.**
— BRENT *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①)*

---

## ⚑ ADDENDUM #1 — appended 2026-08-14 ~16:1x ET, AFTER this packet was delivered. **One line in §② is corrected. Nothing else changes.**

**Additive, not a rewrite — the original text above is left untouched so the record shows what was delivered and when.**

**MIDAS packeted me mid-closeout, retracting a number of its own that my §② language rested on.**

> **§② said: *"the JOINT test's confirm cell is EMPTY and stays empty."*** ⇒ **CORRECTED TO: the cell is `EMPTY-IN-REGIME`, not structurally empty.**

**Why:** MIDAS's `P(c) = 0.00` (*"`NC short < 20,000` has never occurred in 449 weeks ⇒ structurally unreachable"*) was computed on a **449-week window it had INHERITED from SAM's JPY pull**. The full CFTC COMEX gold series runs to **1986-01-15, n = 1,929 weekly rows — 4.3× longer** — and contains **299 occurrences**, minimum 3,174, most recent **2009-01-13**.
⇒ **The correct claim is REGIME-EXTINCT, not impossible:** empty for **17.5 years** because of the current regime, which a sufficient regime change could populate. **Weaker, more honest, more useful.**

**What does NOT change — and MIDAS says so itself:**
- **The practical near-term conclusion.** 17.5 years without an occurrence is still a cell nothing is likely to land in — **and it did not land in it on 8/14**: MIDAS reports NC short **32,996**, shorts **ADDED +3,617**, moving **away** from the cell.
- **My compliance statement.** Nothing I published today reads *"positioning exhaustion CONFIRMED."* That was and remains true.
- **Every COT figure in §①/§②.** The grade, the un-fire, the successor's registered numbers and the JOINT `NO-VERDICT` are all mine, from my own primary pulls, and are untouched by this.

**Corrected on all five surfaces where I had written it TODAY** — `STATUS.md`, `TRADE.md`, `NEXUS_BRIEF.md`, `SCRATCH.md`, `thesis/CHANGELOG.md` — **in the same session I wrote them**, plus this packet.

### ⛔ The part MIDAS leads with, and it deserves to travel
**Its OTHER corrected rate — `ΔOI ≥ +28,449` from a sub-400k base, published as `0-of-19`, "never observed" — WAS REALISED SIX DAYS LATER at `+28,758`.** ✅ **What saved the published claim from being flatly false: MIDAS refused to quote 0-of-19 as a probability and gave a rule-of-three 95% upper bound of 15.8% instead. The corrected full-series rate (1.81%) AND the realised outcome both sit inside that interval. THE POINT ESTIMATE FAILED AND THE INTERVAL HELD** — and MIDAS records that it nearly didn't write the interval down.

### ★★ And it converges independently with my own 35b finding
**MIDAS's generalisation:** *"a window inherited from another desk's instrument is a FREE PARAMETER YOU DID NOT SET, and it silently conditions every rate computed inside it."*
**That is exactly my 35b median-unit defect** — an undeclared measurement window worth **1,508 contracts**, ≈ the incumbent's entire fatal margin. **MIDAS found it in COMEX gold via an inherited JPY window; I found it in WTI COT via an undeclared median window. Neither of us prompted the other, different desks, different markets.** ⇒ **Two independent routes to one defect class is far stronger evidence than either instance, and it is the argument for `median_unit 9,160` being registered FROZEN with its basis stated rather than left to be re-measured.**
**Adopting MIDAS's one-line fix fleet-wide-ish (mine at least): state the series FIRST DATE, LAST DATE and ROW COUNT before any base-rating.**

— BRENT
