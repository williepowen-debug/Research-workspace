# VIOLET — Profile refresh, Cluster B (thesis · thresholds · invalidation · trade)

**DAEDALUS Mode-A reader B · 2026-09-04 (Fri) · READ-ONLY** — no VIOLET file edited, no VIOLET script run. Paths relative to `AGENTS/VIOLET/`. The two re-derivations below were my own throwaway commands over file text.

## 1. Thesis

**v4.0, 2026-08-27** (level-signal decay is a CLASS), last commit 8/27 — `thesis:1`. **Path A** (`:236,250,268`) credit-led, 4 conditions (VIX<20 onset · credit-originated · cross-sector · no inversion), high conf / standard size. **Path B** (`:252,264,268`) concentration-unwind parallel, fires when A's conditions are NOT met but HENRY concentration + macro trigger coincide, medium conf / **reduced size until backtest matures**. Debt on both (`:16,422,466,467`): Path A **owes an F2 (pre/post-2018) audit** on its VIX<20 gate; Path B's backtest was never run.

**Matrix vintage vs thesis: unmatchable — the matrix is not in the thesis.** `grep -i "convergence|/55|vector"` over the thesis = **zero** definitional hits (incidental `:52,511`); the 11-vector/55-pt scale lives only at `STATUS.md:95-111`, untagged by version. 🔴 **And it does not add up:** header **25/55** (`:97`), prose *"FLAT at 26"* (`:113`), cells summing to **33** (`:101-111`), deltas netting +1 off 26 ⇒ 27. Same class: `:180` *"12 rows since v4.0 (214→225)"* vs `:167` *"29 rows"* vs `:12` citing through **KB-VIO-243** (=30).

## 2. Gate / threshold / kill register

| Name | Surface | Level | Op | Series+basis? | Vintage/tie? | Last eval | State |
|---|---|---|---|---|---|---|---|
| **RED-FT-10** | `STATUS.md:83`; RED `FALSIFICATION_TRIGGERS.tsv` | ≥150, sustain **4** consecutive bars | **non-strict ≥** | ✅ CBOE `SKEW_History.csv` | ✅ chain 9/3·9/4·9/8·9/9, Labor Day out (`CATALYSTS.tsv:2`) | 9/4 | **ARMED · 1 of 4 · NOT FIRED** |
| **KB-VIO-123** tree | `STATUS.md:84` | 6 legs: credit·COT≥p95·MOVE·VVIX 120·inversion·VIX>20 | mixed | partial (VVIX/VIX bare levels) | ✗ | 9/4 | **0 of 6 — FADE** |
| **GATE-VIO-116** | `STATUS.md:85` | F1 **72.41** re-arm (F3 resolved 7/16) | > | ✅ `move.py`, investing.com | ✅ EOD | 9/4 (74.68) | **RESOLVED**; F1 live |
| **GATE-VIO-RV1** | `STATUS.md:86` | — | — | — | — | 8/27 | **RETIRED (F2-KILLED)** |
| **GATE-VIO-110** | `STATUS.md:87` | — | — | — | — | 7/09 | **LAPSED** |
| **Tail-hedge A/B/C** | `TRADE.md:115-117` | A: CCC≥9.65 OR disp≥8.00 · C: LIQUID BROAD | ≥ | ✅ FRED | ⛔ a **7/02 print** | 7/02 | **RETIRED-SUPERSEDED** (`TRADE.md:106`) |
| **RED-FT-06** | `STATUS.md:89` | exit VIX ≥18 sustain-5 | ≥ | ✅ cash VIX (⚠️ not the future) | ✅ | 9/4 | **FIRED-BANKED** |
| **T9 falsifier** | `STATUS.md:90` | COR1M<6.77 ∧ JPY RV<IV ∧ OVX<45 ∧ MOVE<66 | strict <, conjunctive | ✅ all four | ✅ | 9/4 | **NOT MET (3 of 4 fail)** |
| **`VIO-FOMC-0916`** L1–5 | `research/2026-09-16_..._PREREG_LETTER:167-171` | L1 ΔVIX>−3.66% · L2 Δ>0 (KILL<−1.41%) · L3 2-of-3 · L4 MOVE%Δ>VIX%Δ | strict, both sides | ✅ per leg | ✅ frozen table `:78-89` | 9/16·9/18·9/23 | **REGISTERED READ — NOT A GATE** |
| **Cheap-tail** | `STATUS.md:74`; `CANARY_MAP.md:27` | VVIX≤90·VIX≤16·SKEW≥140·catalyst≤21d | non-strict | ✅ | ✅ SETTLE | 9/3 | **OPEN 4/4** (operator surface) |
| **Canary DARK contract** | `CANARY_MAP.md:57` | >2× cadence (EOD >2td; COT >9d) | > | ✅ ledger max-date | ✅ content-vintage, not mtime | 9/4 | **on ledgers only** (§4) |

- **No live threshold lacks a named series** — the two un-lined rows are marked **TBD** (`CANARY_MAP.md:33,34`). **Expected-event resolver:** only letter **LEG 3**, handled correctly — legs 1/2/4 anchor on scheduled closes, **leg 3 voids rather than slips** (`letter:173`); `DOCKET.tsv:163` (`next-VIOLET-session`) is RESOLVED, so the bare-event class is empty.
- **Never fired / can it:** FT-10 ✅ earliest the 9/9 close — the live risk is inverse, a non-strict band that *"reads as FIRED to anyone who never reaches the sustain clause"* (`STATUS.md:83`). KB-VIO-123 ✅ (COT p51.9 vs p95, `:70`). **T9 ⛔ untrippable in fact** — its JPY leg is the only ✅ and `STATUS.md:72` calls that RV-through-IV measurement **UNUSABLE**: a conjunctive gate one leg of which its owner declares unmeasurable.

🔴 **Coordination gap (verified):** `grep -c "FT-10\|VIO-FOMC"` on `PROME/GATES.tsv` and `PROME/DOCKET.tsv` = **0 / 0**; GATES.tsv holds **zero VIOLET rows** (only `RED-FT-01/02`). `letter:177` claims routing *"to PROME … so a graded outcome cannot fire into a dark coordination layer (KB-VIO-110 class)"* — **it did not land.** `DOCKET.tsv:125` covers the 9/16 FOMC but names `CALENDAR.md` as artifact, no grade dates. `GATES.tsv:17` cites **KB-VIO-110, VIOLET's own orphan finding**, as why another desk's gate went 31 days unregistered.

## 3. TRADE.md

**Live: nothing** — FLAT since `TRY-VIOLET-VIXCS` closed 7/30, −$111.60 (−38.8%) (`:9,15`); other frameworks closed `:36,130,174,42`. **Retired:** the 7/1 Tail-Hedge Packet, Will 9/4 11:11 / WQ-177 (`:106`).

🟠 **ARMED language over a dead premise — partly.** Banner correct, but the section still heads `## LIVE DECISION FRAMEWORK` (`:108`), Gates A/C still read **"PENDING"** against a **7/02** print (`:115,117`), and a **"Re-arm lines: SKEW >150 sustained 4td…"** block sits under it (`:119`) with SKEW at 150.63, 1-of-4. Queued unfinished at `STATUS.md:172`.

⛔ **Two-state banner FAILS** — neither FROZEN nor LIVE-with-staleness-alert; **no `Last real data refresh:` header**, only footer **`Last Updated: 2026-07-28`** (`:261`), 38d stale and silent on today's retirement in the same file. Its only watcher keys on **mtime vs STATUS.md** — *"measures age, not agreement"* (`:31`). 🔴 **The TRADE LOG still shows the position Exit `—` / P&L `OPEN`** (`:242`) five weeks after `:15` records it closed — a third instance of the failure the file twice confesses (`:31,261`: *"it does not self-correct"*).

## 4. CANARY_MAP.md

Contract: **DARK at >2× cadence** (EOD >2td; COT >9d), `:57`. Header **`Last refreshed: 2026-08-04`** (`:106`) = 31 days.

| Row | CURRENT cell | Days past cadence | Live today | Verdict |
|---|---|---|---|---|
| MOVE `:19` | `CURRENT [8/3]` 80.48 | ~22td (EOD) | **74.68 [9/3]** (`STATUS:66`) | 🔴 DARK |
| COT `:24` | `[7/28 report]` −12,289 p76.9 | 38d (weekly) | **−26,258 [9/1] p51.9** | 🔴 DARK |
| JPY `:25` | `Current [8/4 SETTLE]` RV10 12.94% | ~22td (daily) | **9.22% p62.2 [9/4]** | 🔴 DARK |
| OVX `:26` | `[8/4 SETTLE]` 53.45 | ~22td (EOD) | **46.41 [9/3], WATCH→FIRE** | 🔴 DARK + **state-wrong** |
| Cheap-tail `:27` | `[8/4 SETTLE]` **DORMANT 1/4** | ~22td (daily) | **🟣 OPEN 4/4** | 🔴 DARK + **inverted** |
| Tier-3 GEX `:41` | 7,455/7,491 [HENRY 7/28] | 38d | **HENRY 9/2: 7,689–7,699, −$16B, sign INVERTED** (`STATUS:153`) | 🔴 DARK — the row that calls itself *"THE WORST STALENESS IN THIS FILE"* |
| SKEW `:23` | pull source reads **`yfinance ^SKEW`** | — | ruled **CBOE publisher-of-record** 9/2 (`research/2026-09-02_skew_endpoint...:91`) | ⛔ contradicts the live ruling |

Two protocol blocks **were** edited today (`:48-53`, `:59-64`) while all six data cells stayed at 7/28–8/4. The file logs this pattern about itself at n=4 (`:7,90,106,108`); today is **n=5**.

**Rules written here that no script computes:**
1. 🔴 **The stale-cell guard sees 1 of 6.** `scripts/canary_staleness.py:193-195` matches only `Current [M/D]` / `[M/D] <STATE>`; re-running that regex returns **`['CURRENT [8/3]', 'Current [7/28]']`** (the second a retrospective parenthetical). Cells carrying a basis token inside the bracket — `Current [8/4 SETTLE]`, `[8/4 SETTLE]`, `[7/28 report]` — fall outside, as does the un-ledgered GEX row. The matcher was tightened after a v1 false positive (`:186-192`) and the tightening took the true positives with the noise. It returns 1 only under `--strict` (`:326`); `boot.py:52` runs it `--quiet`, non-blocking.
2. ⛔ **`CALENDAR.md:107` credits VX_DAILY gap detection to `scripts/ledger_staleness.py`, which measures vintage, not row gaps.** Nothing computes VX_DAILY completeness — and the ledger is **missing 8/28, 8/31, 9/1 and 9/3 entirely**, with no `skew` on 8/27 or 9/4, while `STATUS.md:62-63` publishes a six-session `^SKEW` run and a rising 20d average **it cannot reproduce**. Max-date reads 9/4, green.

## 5. CALENDAR.md vs CATALYSTS.tsv

**5 rows each** (`CATALYSTS.tsv:2-6`; `CALENDAR.md:58-62`), **1:1 today** — 9/7 Labor Day · 9/11 CPI · 9/16 FOMC · 9/16 VIX quarterly expiry · 9/30 MU; the 9/16 combined row was split 9/4 so a bidirectional twin check sees both (`:61`). ✅ **No past-dated row under a forward heading** — the 8/21 COT, 8/26 NVDA and 8/27 Jackson Hole rows sat forward **14 days after firing** and were moved to RESOLVED 9/4 by `twin_check.py`'s first bidirectional run (`:70-72`); cosmetic residue only at `:30` and `:42`. ✅ **No MODELED/ESTIMATED row carries a decision** — MU is **CONFIRMED 2026-09-30** off VIOLET's own primary fetch (`CATALYSTS.tsv:6`) ⇒ **the MU confound on letter leg 2 is WITHDRAWN**.

## 6. The 9/16 FOMC letter

✅ **Every leg is gradeable from a named source at a named time** — L1/L2 on `^VIX` closes (`:99-113`), L3 on VIX3M/VIX·VVIX·MOVE at the **9/18** close with a whole-map NULL declared (`:117-126`), L4 on MOVE vs VIX %Δ (`:134`), L5 the contango-roll process leg (`:144-146`). ⚠️ L4's two legs **start on different dates** (8/26 vs 8/27) — basis asymmetry inside a comparative threshold; ⚠️ L3's 9/18 grade date is absent from the §7 grade-card header (`:163`).

**The `^SKEW` defect touches no graded leg** — it appears only in the frozen state table at CBOE basis (`:82`). **But the exposure moved rather than vanished:** the 9/4 integrity rule (`CANARY_MAP.md:48-53`, rc 0/1/**2 fails closed**) is scoped to **`^SKEW` only**, while L1–L2 grade on yfinance **`^VIX`** — same redistributor, **no base-rated defect rate**. RED's rate on the sibling series is **2/253 = 0.79%, two modes** (`STATUS.md:8`); a wrong value does not announce itself and the omission mode **self-heals** (`:16`), so a later audit passes clean over a grade that was wrong when computed.

**9/16:** the Sept VIX quarterly expiry settles at the **special opening quotation that morning**, ~6h before the **14:00 ET** statement + SEP/dots (`:27-29`) — expiring VX/U6 **cannot** express the outcome, the premium sits in VX/V6 (M1 that same morning, `:38`). L1 and L5 grade at that close; `m1m2_adj_pct` **breaks basis** on that row (KB-VIO-218). **9/23:** L2 grades.

⚠️ **Two declared weaknesses went stale on a frozen instrument, no addendum written** (none in `research/`): the *"1.83 unexplained"* MOVE gap (`:155`) was resolved 9/4 as a vintage compare (`STATUS.md:20`); *"the gamma board is UNMEASURED since the 8/21 OPEX"* (`:156`) was superseded by HENRY's 9/2 read, **which inverted the sign to −$16B / dealers AMPLIFY** (`:153`). `:4` permits *"a dated addendum, never a rewrite"* — a 9/16 grader reading the canonical instrument alone inherits two dead caveats, one a live input to branches A/C.

## 7. Falsification

Live and dated: the **letter grade card** (frozen 9/02, the strongest surface on the desk) · **Level-Decay Class** (8/27, `thesis:407-422`) · **KB-VIO-123 tree** (9/04) · PREDICTIONS (rows current to v4.0; header still reads *"Status (6/6)"*, `thesis:430`).

🔴 **The thesis tail is the weakest and reads as live.** `### Current status (2026-06-10 ~3 PM ET intraday)` — **86 days** — inside a v4.0-stamped file, present-tense throughout: *"Iran/oil leg (NEW 6/10): **LIVE**"* (`:490`), *"**NO short-vol while the war leg is live**"* (`:491`), *"**Invalidation is CLOSE-AND-HOLD above 23**"* (`:492`) against VIX **14.32**, LIQUID HY **2.75 [6/8]** (`:481`), closing on *"6/10 EOD re-adjudication is the next decision point"* (`:511`); the footer still reads *"v3.0 → v3.5"* (`:515`). The letter, by contrast, states the live branch set correctly — **HIKE vs HOLD, no cut branch** (`letter:11-19`).

🟠 **Prediction #7 fired and is ungraded.** *"Fires: 20d-avg cross-back >140 within ±2 sessions of 9/1 … Falsifies: no cross-back by 9/8"* (`thesis:439`); `STATUS.md:63` shows **141.13 [9/1] → 141.67 [9/2] → 142.47 [9/3]**, inside the window. Thesis untouched since 8/27, STATUS never mentions #7, agenda still lists it ungraded (`:469`). **The one prediction with a dated resolver that has come due is the one nothing is watching, and its falsifier expires Tue 9/8.**

## 8. TOP 5 — what needs help or attention

| # | Item + exact line | Failure risked | Owner |
|---|---|---|---|
| **1** | **Thesis tail 86d stale, present-tense** — `thesis:479-511` (*"Iran/oil leg (NEW 6/10): LIVE"* `:490`; invalidation **VIX 23** vs spot 14.32 `:492`; HY 2.75 [6/8] `:481`); footer still v3.5 `:515` | The 9/16 grader or any cold reader takes a **dead invalidation line and a retired posture as the live falsification tail**, off the canonical thesis | **VIOLET desk** — first cut of the queued *"read the thesis against its own KB trail"* (`STATUS.md:167`) |
| **2** | **Prediction #7 fired ~9/1, ungraded; falsifier expires 9/8** — `thesis:439,469` vs `STATUS.md:63` | A well-specified forward prediction **resolves unrecorded**; grading after 9/8 from memory is not a pre-registered grade | **VIOLET desk** — grade before the Tue 9/8 close |
| **3** | **Six CANARY_MAP CURRENT cells 31–38d stale, guard sees one** — `CANARY_MAP.md:19,24,25,26,27,41`; matcher `canary_staleness.py:193-195`, rc only `--strict` `:326`, boot `--quiet` (`boot.py:52`) | The cross-domain early-warning surface carries **two state-inverted cells** (cheap-tail DORMANT vs live OPEN 4/4; a GEX band whose sign has since inverted); a guard tightened against false positives now under-detects its own class | **VIOLET desk** (cells + matcher, both VIOLET-owned) · **DAEDALUS structure-tooling** (`CHECK_STANDARD §3` — a regex tightening is a new guard and owes a fresh capable-case watch) |
| **4** | **VX_DAILY missing 4 of the last 6 sessions; nothing checks completeness** — `workbook/VX_DAILY.tsv` (no 8/28, 8/31, 9/1, 9/3); `CALENDAR.md:107` credits `ledger_staleness.py`, which measures vintage | **The FT-10 chain and 20d average cannot be reproduced from the desk's own ledger** while max-date reads green; blocks RESEARCH-QUEUE item 1 (`STATUS.md:166`) | **VIOLET desk** (backfill + completeness check) · **DAEDALUS** (`CHECKS.tsv`: `ledger_staleness` PASS proves vintage, **not** completeness — the doc claiming otherwise is a live mis-citation) |
| **5** | **Neither the letter nor FT-10 is on PROME's rails; TRADE.md's log still shows a closed position OPEN** — `grep -c`=0/0 on `PROME/GATES.tsv`+`DOCKET.tsv` vs `letter:177`; `TRADE.md:242` vs `:15`, footer `:261` | Two hard grade dates (**9/16, 9/23**) and an ARMED sustain counter live **only inside VIOLET/RED files** — if VIOLET is dark on 9/16, nothing on the coordination layer knows a grade is due | **PROME coordination** (DOCKET rows naming the letter; rule whether FT-10 warrants a transcription-only GATES row, `GATE-VIO-RV1` precedent) · **VIOLET desk** (log close row + banner) · **TERRY** (informational only — cheap-tail 4/4 into CPI 9/11 + FOMC 9/16 stays an operator surface) |

*Below the top 5: the convergence-score arithmetic (§1) is a clean own-file defect and a minutes-long fix — VIOLET desk.*
