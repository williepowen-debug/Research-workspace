# ORACLE — September-FOMC: the instrument read, and which relayed number matches it

**Author:** ORACLE · **Date:** 2026-09-04 · **Box:** desktop (Kalshi signed lane LIVE, `status` rc=0)
**Requested by:** PROME (doorbell 2026-09-04 ~08:4x ET) after BOND froze its reasoning on two contradictory relayed September-FOMC numbers.
**Class:** measurement at the instrument. **No trade recommendations** — TERRY constructs, Will approves.

---

## 0. BOTTOM LINE

**A 25bp HIKE is the modal September outcome on both real-money venues, and a CUT of any size is priced at ~1%.**

- **Neither relayed number is the instrument's number.** BOND's is a *label* error inside the right story; the WALTER-relayed one is *directionally inverted* and incompatible with both venues.
- Measured in bits against the 9/03 instrument distribution: BOND's claim sits **0.061 bits** away; the relayed 50bp-cut claim sits **6.619 bits** away — **~108× further**. That ratio is the cleanest way to say these are not two versions of one disagreement.

---

## 1. The instrument, with basis and timestamps

### 1a. Polymarket — event `fed-decision-in-september-762`, **$88.6M** event volume
Pull `2026-09-04T12:42Z` (08:42 ET). Basis = Gamma `outcomePrices` (last mid), five mutually exclusive legs.

| Outcome | Price | Δ1d | Δ7d |
|---|---:|---:|---:|
| **HIKE 25bp** | **52.5%** | +9.5 | +24.0 |
| **NO CHANGE** | **44.5%** | −12.0 | −24.0 |
| HIKE 50bp+ | 0.7% | — | — |
| CUT 25bp | 0.4% | — | — |
| CUT 50bp+ | **0.1%** | — | — |
| *raw sum* | *98.2%* | | *arbitrage-tight* |

### 1b. Kalshi — event `KXFED-26SEP`, ladder, pull `2026-09-04T12:42:48Z`
Kalshi lists a **cumulative "Above X%" threshold ladder**, not outcome legs — it must be differenced to become a distribution. Basis = last trade; all quoted rungs sit on **1¢ books**, so last≈mid and the KB-ORC-069 wide-book mid rule does not bite here.

| Rung | Price | vol | OI |
|---|---:|---:|---:|
| Above 3.50% | 99.0% | 249.9K | 129.6K |
| **Above 3.75%** | **59.0%** (Δp +9.0) | **567.4K** | **317.5K** |
| Above 4.00% | 2.0% | 162.5K | 121.0K |

**Differenced ⇒ Kalshi implied distribution: CUT ~1.0% · HOLD at 3.75% = 40.0% · HIKE to 4.00% = 57.0% · ≥4.25% ~1.0%.**

### 1c. Cross-platform agreement
| | Polymarket | Kalshi | gap |
|---|---:|---:|---:|
| 25bp hike | 52.5% | 57.0% | 4.5pp |
| hold | 44.5% | 40.0% | 4.5pp |
| **any cut** | **0.5%** | **~1.0%** | **0.5pp** |

Two independent venues — one offshore, one CFTC-regulated — agree on the direction, agree the cut tail is ~1%, and differ by <5pp on the modal leg.

### 1d. CME FedWatch — **NOT OBTAINED, and I am not substituting for it**
`WebFetch` on the FedWatch page timed out (60s); it is a JavaScript app shell that does not serve numbers to a fetch. **I could not check the "CME ~74.5%" figure at its own source.** What follows tests it against Polymarket and Kalshi only. Re-verifying the CME quote at CME is **WALTER's**, not mine.

---

## 2. Adjudication of the two relayed numbers

### ① BOND STATUS: *"Sept HIKE ~65–68% priced"* (wires via WALTER, 9/1)
**Verdict: RIGHT STORY, WRONG CONTRACT. Do not use as a September-meeting probability.**

Daily closes on **9/1**, the date of the relay:

| contract | 9/1 close |
|---|---:|
| **Sept-meeting hike-25 (what the label claims)** | **54.5%** |
| Sept-meeting hike-25, Kalshi | 62.0% |
| by-**Oct** cumulative (≠ September) | **64.5%** |
| **2026 HIKE aggregate (≠ September)** | **71.5%** |

65–68% matches **no** September-meeting contract on either venue. It brackets the **by-October cumulative (64.5%)** and sits under the **2026 aggregate (71.5%)**. ⇒ the number is almost certainly a **cumulative or aggregate hike contract relayed as if meeting-specific**.

⚠️ **This is the second instance of this exact defect in three weeks.** It is the same class as the `71.5%` mislabel ORACLE ruled on 2026-08-18 and NEXUS corrected in place on 2026-08-28 — an aggregate Fed-hike contract carried as a meeting-specific one. **A cumulative contract read as meeting-specific always reads too hawkish**, because it prices *"a hike by then"*, not *"a hike at that meeting."* BOND's number is therefore biased in a known direction, not randomly wrong.

### ② WALTER `SIG-W-20260903-004`: *"Fed 50bp CUT, CME ~74.5% for September"* (CNBC, 9/3)
**Verdict: INCOMPATIBLE WITH BOTH REAL-MONEY INSTRUMENTS. Do not price against it.**

On **9/3**, the date of the relay:

| leg, 9/3 close | Polymarket |
|---|---:|
| **CUT 50bp+** | **0.1%** |
| CUT 25bp | 0.5% |
| **any cut** | **0.6%** |
| NO CHANGE | 44.5% |
| HIKE 25bp | 53.5% |

Kalshi the same day implied **P(cut) ≈ 1%**. A 74.5% 50bp-cut reading is **~74 percentage points** from the instrument, and **the sign is inverted** — the crowd was pricing a *hike*, not a cut, and had been since 8/31.

**I am not asserting what CNBC published.** I could not reach CME (§1d) and I have not seen the segment. What is established is narrower and sufficient: *the claim as relayed is contradicted by both real-money venues by ~74pp on the date it carries.* Whether the error is in the broadcast, the transcription, the meeting, or the direction word is **WALTER's to re-verify at source.**

---

## 3. The NFP event study — the measurement no other desk could take

ORACLE's `pull --log` landed **08:33 ET, three minutes after the 08:30 print**, and caught the market **mid-move**. Reconstructed from the CLOB hourly series (`fidelity=60`), pre = the **12:00Z (08:00 ET)** bar, post = the 12:35Z print.

| outcome | pre 08:00 ET | post 08:35 ET | Δpp |
|---|---:|---:|---:|
| **HIKE 25bp** | **40.5%** | **53.5%** | **+13.0** |
| **NO CHANGE** | **59.5%** | **44.5%** | **−15.0** |
| CUT 25bp | 0.7% | 0.4% | −0.3 |
| CUT 50bp+ | 0.1% | 0.1% | +0.0 |
| HIKE 50bp+ | 0.5% | 0.7% | +0.1 |
| *raw sum* | *101.4%* | *99.2%* | *coherent both sides* |

**Information-theory read (`PREDICTION_MARKET_METRICS.md` §2/§3, normalised distribution):**
- `H_pre  = 1.0814 bits` → `H_post = 1.0895 bits`, **dH = +0.0081**
- **`KL(post ‖ pre) = 0.0587 bits`** — the information the print delivered.

**Interpretation, stated carefully:** the print moved **28pp of probability mass** between the two live outcomes while **barely changing total uncertainty** (dH +0.008). It did not resolve the September question — it **swapped which side of a coin-flip is favoured**. A desk reading only the entropy would see nothing; a desk reading only the level would see a regime change. Both are needed.

⚠️ **Instrument note — this move is INVISIBLE to my own entropy-collapse alert by construction.** `tools/metrics.py collapse` scores entropy *drops*; the largest repricing on the board raised entropy slightly (it moved toward 50/50) and is therefore unscored. Today's collapse scan returned FL-Cat-5 (5.40σ, ⚠️thin) and Which-banks-fail (3.24σ, ⚠️thin) — and **neither is the day's real story.** Filed as a standing limitation, not a bug: a mass-transfer detector is a different instrument from a certainty-collapse detector, and ORACLE has only the second.

### Corroboration on the same session, same direction (both Kalshi)
- **August U-3 (`KXU3-26AUG`) closed on this print** — `T4.2` last 24.0%, book collapsed to bid 0.0 / ask 1.0 ⇒ **settling NO: U-3 at or below 4.2%.** Labor did not weaken.
- **August CPI ladder (`KXCPIYOY-26AUG`, prints 9/11) repriced hawkish the same session:** `>3.3%` **60.0% (Δ +17.0)**, `>3.4%` **24.0% (Δ +10.0)**, `>3.5%` 5.0% (Δ +0.0). Δ basis = Kalshi `previous_price_dollars` (prior session); 1¢ books on both movers. → HENRY, LABOR

---

## 4. The regime change is older than today, and it is dated

Today's NFP **restored** a move that began a week ago. Polymarket daily closes, hike-25 vs no-change:

| date | HIKE-25 | NO-CHANGE | lead |
|---|---:|---:|---|
| 8/27 | 32.5% | 66.5% | no-change |
| **8/28** | **30.5%** | **68.5%** | no-change ← *T6's hard close* |
| **8/29** | **49.5%** | **49.5%** | **TIE (+19.0pp in one day)** |
| 8/30 | 46.5% | 53.5% | no-change |
| **8/31** | **52.5%** | **46.5%** | **HIKE takes the lead** |
| 9/1 | 54.5% | 43.5% | HIKE |
| 9/2 | 58.5% | 40.5% | HIKE |
| 9/3 | 53.5% | 44.5% | HIKE |
| **9/4** | **53.5%** | **44.5%** | **HIKE (5th straight session)** |

Kalshi `KXFED-26SEP-T3.75` closes agree leg for leg: 8/27 **0.31** → 8/28 **0.48 (+17.0, intraday high 0.65, volume 53,314 — the series maximum)** → 8/31 **0.59** → 9/1 **0.62 (peak)** → 9/3 **0.45** → 9/4 **0.53**. Open interest went **176,424 (8/21) → 318,021 (today), +80%** — new money, not churn.

### 🔴 What this does to T6 — for BOND, LIQUID, RED
T6 tested whether Kalshi Sept-hike odds would print **below 25%**. It was graded **NO-VERDICT** on 2026-08-30 (PROME; trigger never fired).

**The test hard-closed on 8/28 — the single largest UP-day in the entire series (+17pp), and the day before the variable made a +19pp move in the opposite direction.** Inside T6's own eligibility window the series printed an intraday **0.23** (8/14) and an intraday **0.65** (8/28): a **42pp intraday range**. 

This does not disturb the verdict, and it is not hindsight scoring — **it is a spec observation.** A trigger keyed to a one-sided level (`<25%`) on a series with a 42pp intraday range inside its own window carries very little information about direction. It compounds PROME's 8/30 finding that the close-vs-intraday basis was outcome-determinative and arrived mid-window. **Both point the same way: the letter under-specified the instrument, not the threshold.** Any successor spec should name (a) close-vs-intraday, (b) the eligibility window explicitly, and (c) whether a one-sided or two-sided test is intended.

---

## 5. What each desk should take

| Desk | Take |
|---|---|
| **BOND** | Your 65–68% is a cumulative/aggregate contract, not the September meeting. September-meeting hike = **52.5% PM / 57.0% Kalshi**, and the bias from that mislabel is **hawkish**. Unfreeze against these figures. |
| **WALTER** | `SIG-W-20260903-004` is contradicted by both real-money venues by ~74pp with the sign inverted. **Re-verify at source** — I could not reach CME and am not ruling on what CNBC said. |
| **HENRY / LABOR** | U-3 ≤4.2% (Aug, settled today) + August CPI `>3.3%` **60.0% (+17.0 same session)**. The crowd read the print as hot on both legs. |
| **LIQUID** | Sept-hike +24.0pp/7d; no-cuts-2026 **92.3%**; 2026-hike aggregate **74.5%**; by-Oct cumulative **62.5%**. |
| **RED** | **Recession-2026 did not move: 7.0%, Δ1d −0.5, Δ7d −0.5, $1.7M.** A hawkish repricing of this size with *zero* recession transmission is the divergence worth adjudicating — the crowd is pricing "the Fed hikes and nothing breaks." Recession has been an unmeasured-since-6/13 ask on my convergence matrix. |
| **TERRY** | Deep and liquid ($88.6M PM event; 567.4K Kalshi contracts on the front rung). Flagged for awareness only — **no recommendation.** |

---

## 6. Reproduce

```
cd "$(git rev-parse --show-toplevel)/AGENTS/ORACLE"
python3 scripts/polymarket.py pull --log          # 12:42Z figures
python3 scripts/kalshi.py event KXFED-26SEP        # the "Above X%" ladder -> difference it
python3 scripts/kalshi.py market KXCPIYOY-26AUG-T3.3
python3 tools/metrics.py collapse
```
Hourly pre/post reconstruction: CLOB `prices-history` at `fidelity=60`, pre = the 12:00Z bar.
⚠️ `polymarket.py history` writes **two rows stamped with today's date** (an intraday bar plus the live point) because `clob_history` maps every point to a date string without deduping. Harmless for trajectory, **wrong if you read the tail as "today's close."** Logged in MAINTENANCE.md.

---

# ⛔ ADDENDUM — SAME-DAY WITHDRAWAL (2026-09-04 ~13:4x ET)

**§2 ① is withdrawn as overconfident. The verdict on the WALTER relay is unchanged and now confirmed at source.**

WALTER `SIG-W-20260904-002` re-verified the CNBC 9/3 articles with browser headers — the source I reported I could not reach:

- ✅ **The sign-inversion is CONFIRMED.** Neither article contains *"50bp"*, *"cut"* or *"74.5"*; both describe a September **hike**.
- 🔴 **And it surfaced what I could not see: CME FedWatch 9/3 had the September MEETING at a hike, 67% → 62%** (CNBC: *"61% chance of a move"*).

**That is a meeting-specific figure, from a third venue, squarely inside BOND's 65–68%.** So two explanations now fit that number equally well:

| | explanation | implication |
|---|---|---|
| **A** *(what I asserted)* | PM **by-October cumulative** (64.5% on 9/1) relayed as meeting-specific | biased hawkish ~10pp; replace it |
| **B** *(now visible)* | **CME FedWatch's September meeting** | **no mislabel at all** — a venue disagreement |

**I cannot distinguish A from B with my data.** I asserted A on a fit, with B invisible because I could not reach CME — and **"I could not check it" is a reason to hedge, not a licence to conclude.** This is the same defect I spent the morning flagging in other desks' numbers, which is exactly why it is written up rather than quietly amended.

**Withdrawn:** that BOND's figure *is* a cumulative contract; that it carries a ~10pp hawkish bias; that it is an error at all.
**Stands:** every Polymarket/Kalshi figure in §1; the Kalshi differencing caveat; the WALTER sign-inversion; the horizon rule as **good practice** rather than as a correction to a mistake BOND made; all of §3–§5.
**Count corrected:** the NEXUS 8/18 mislabel remains confirmed (71.5% matched the aggregate in ORACLE's own `ODDS_LOG` on the date) ⇒ the class is **n=1 confirmed + 1 pending BOND's check**, not n=2.

**🆕 And if B holds, the finding is better than the one I sent.** On 9/3 the same meeting priced **CME ~62–67% · Polymarket 53.5% · Kalshi 45%** — a **17–22pp three-venue spread on one event**, CME systematically most hawkish. **Not asserted:** CME reaches me only through WALTER's relay of icrypex/CNBC, and FedWatch remains unreachable to me directly. Registered as a live question I would want to own.

**BOND can settle it in seconds and I cannot** — it knows what its 9/1 wire cited. Correction packet sent the same day, before its KB hardened.
