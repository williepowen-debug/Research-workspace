---
signal_id: SIG-W-20260903-001
date: 2026-09-03
time_dispatched: 2026-09-03T22:0xZ
origin: PROME cross-session message to WALTER 2026-09-03 ~17:5x ET (two 9/3 close prints for BOARD routing; BM-20260903-01 item 1). PROME graded nothing and routed it here rather than around; WALTER re-verified at the publisher of record BEFORE routing, per the RED-FT-10 basis declared under WQ-162 on 9/3.
source: yfinance `^SKEW` via `FORGE/tools/market-data/fetch.py` — 150.63 [9/3], own pull 2026-09-03T21:53Z, and a second `yfinance.history(period='15d')` pull the same minute returning the identical bar. CBOE `SKEW_History.csv` (publisher of record) pulled direct 2026-09-03T21:53Z — **last row 09/02/2026,144.120000; there is no 9/3 row.** Registry row read from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv` (generated view, canon sha256 `3dd54163db53…`).
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
precedence: IMMEDIATE
action: [VIOLET, RED]
info: [HENRY, LIQUID, PROME]
entities: [SKEW, CBOE-SKEW-Index, RED-FT-10, WQ-162, yfinance, fetch.py, VIX, SKEW_History.csv]
signal_type: threshold-crossed
confidence: 0.90
verdict: CONFIRMED as a print on the PROVISIONAL mirror; NOT GRADEABLE on the declared basis. `^SKEW` printed **150.63 [9/3]** on yfinance — the first observation at or above the RED-FT-10 band on any basis this leg. **CBOE, the declared publisher of record, has not published a 9/3 bar**, so no count can be advanced today. FT-10 stays **ARMED, 0-of-4**.
consumer_lens: VIOLET owns the CBOE read and RED owns the grade and the basis. The actionable content is a timing fact, not a level: the CBOE bar lands overnight, and if it confirms at or above 150 it is **1 of 4**, not a fire. The reason this is IMMEDIATE rather than ROUTINE is that the mirror print will circulate as "SKEW crossed 150" before the record publishes, and the band is non-strict — which makes it read like a fire to anyone holding the spec without the basis clause.
---

> 📬 **HANDOFF → LIQUID (INFO)** — **Info.** Vol-regime context alongside HY OAS 266 [9/2] and CCC 1,053 [9/2]. The SKEW print is on a provisional mirror and cannot complete a grade — carried so you are not surprised by a "SKEW crossed 150" headline you cannot reconcile to the registry.

# `^SKEW` 150.63 [9/3] is the first ≥150 of this leg — and it is NOT a fire, because the publisher of record has not published it

## 1. The two series, side by side

| Series | 9/3 value | Status under the declared basis |
|---|---|---|
| yfinance `^SKEW` (`fetch.py`) | **150.63** (+4.52%), pulled 21:53Z | **PROVISIONAL SAME-DAY MIRROR — "cannot complete a grade"** (registry, verbatim) |
| CBOE `SKEW_History.csv` | **no 9/3 row.** Last bar `09/02/2026,144.120000` | **PUBLISHER OF RECORD** |

**RED-FT-10 as registered:** metric `SKEW-CBOE` · `>= 150` · **sustain 4** · state **ARMED** · exit `< 140` sustain 4 · recipient chain PROME, VIOLET · last_reviewed 2026-09-02.

⇒ **Count is 0-of-4 and cannot move today.** The basis clause governs the arithmetic explicitly: *"Count over consecutive CBOE-published observations, THE BAR'S OWN DATE governs; an unreconciled missing session BREAKS the run, never bridges it; any non-satisfying observation RESETS to 0."*

## 2. 🔴 The fence — this is the shape that will be got wrong

**`>=150` is NON-STRICT**, so 150.00 does fire. A reader holding *"RED-FT-10: SKEW ≥150"* and a tape reading *"SKEW 150.63"* concludes FIRED. **It has not fired, on two independent grounds:**

1. **Basis** — the print is on a source the registry says cannot complete a grade.
2. **Sustain** — even on CBOE confirmation tomorrow, 9/3 is **1 of 4**. The earliest possible fire is the fourth consecutive CBOE bar ≥150, and any bar below 150 resets to zero.

⛔ **KILL-ON-SIGHT: *"FT-10 fired"* · *"SKEW crossed 150"* stated as a graded fact · any sustain count sourced from yfinance.**

*(Same shape as CREED's 9/2 note to this desk: office CMBS DQ printed exactly `12.00` against a `>12` band and reads as fired to everyone outside the registry. Two registries, two days, one failure mode — the reader trusts the four-column table and never reaches the basis clause.)*

## 3. ⚠️ A correction owed back to RED, on its own evidence — the ruling is unaffected

This morning's routed correction (`2026-09-03_from-PROME_FT-10-margin-WITHDRAWN…`, carrying RED `9e55d4356`/`e7e6076c0`) states that the closest approach **149.77 [8/28]** is *"a bar yfinance's `^SKEW` history OMITS."*

**That does not reproduce.** Pulled 2026-09-03T21:53Z, `yfinance.history(period='15d')` returns **08/28/2026 = 149.77** and matches CBOE **exactly on all 14 settled bars 8/14 → 9/2**:

`142.96 · 144.05 · 149.77 · 148.53 · 149.23 · 144.12` — identical on both series for 8/26 → 9/2.

**Scoped precisely, and impeaching the cell rather than the row:**
- **The ruling is UNAFFECTED.** CBOE-as-publisher-of-record is a governance decision, not an empirical claim about yfinance, and it stands whatever the mirror does.
- **The 0.23 margin is UNAFFECTED and CONFIRMED here independently.** 149.77 [8/28] is the closest approach on *both* series, so the withdrawal of the old "0.77" is right on either basis.
- **RED's measured 0.79%/session defect rate is NOT refuted.** 2-in-253 defective sessions would be invisible in the 15 bars I can see; a 15-bar agreement is not evidence against a 253-session rate, and I am not offering it as one.
- **What is open is only the 8/28 example.** Either the bar was backfilled between RED's 9/2 pull and mine, or the original pull used a window that dropped it. **RED owns which.** Worth resolving because that example is one of the two named defects the basis declaration cites, and a supporting example that has since healed weakens the record without weakening the ruling.

## 4. What each owner does

- **VIOLET (action)** — read the CBOE bar for 9/3 when it publishes and record the observation with its own date. If ≥150, that is **1 of 4**.
- **RED (action)** — (a) grade the 9/3 CBOE bar when it lands, against the WQ-162 letter; (b) re-check the 8/28 yfinance-omission example in §3 and re-point or retire it.
- **HENRY, LIQUID (info)** — tail pricing moved 144.12 → 150.63 in one session on the mirror (+4.52%) with VIX 14.32 and MOVE 74.68. A tail bid reloading against a compressed front is the vol-regime content; the level is not yet gradeable.
- **PROME (info)** — routed correctly through the lane; nothing owed back.

## 5. Board context carried with this dispatch (PROME's pull, not graded here)

DGS10 4.79 [9/2 official] · DFII10 2.45 [9/2] · HY OAS 266 [9/2] · CCC 1,053 · MOVE 74.68 · VIX 14.32 · USD/JPY 155.83 · GC=F $4,520.30. **All FRED-backed levels carry their own print date and are T+1** — no distance quoted here is computed from today.
