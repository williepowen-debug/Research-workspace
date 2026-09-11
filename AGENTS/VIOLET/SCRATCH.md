# VIOLET SCRATCH — Friday, September 11, 2026 (01:2x ET, pre-open)

> **PROME-spawned VECTOR-2 session** (DOCKET L326, Will 2026-09-11 00:21 ET *"Ok can you work on assigning these vectors?"* → 00:29 *"…orchestrate these agents to investigate these vectors?"*). **Scope as given:** deliver a ONE-PAGE instrument ask on cheap vol into FOMC 9/16, drain the inbox, write back. **Report-before-execute: NO card, NO order, $0.**
>
> 🔑 **THE SESSION IN ONE LINE: the cheap-vol window closed between 9/8 and 9/10 while this desk was dark, every instrument that grades it ran correctly the whole time, and the thing that failed was that nobody booted.**

---

## CHANGES SINCE (9/6 → 9/10, four sessions I did not see)

**All CBOE settles, own pulls 2026-09-11 ~00:5x ET. Basis moved 9/4 SETTLE → 9/10 SETTLE across the whole dashboard.**

| | 9/4 | **9/10** | Δ |
|---|---:|---:|---:|
| VIX9D | 11.97 | **17.70** | **+47.9%** |
| VIX | 14.53 | **17.84** | +22.8% |
| VIX3M / VIX6M | 17.61 / 19.89 | **19.73 / 21.17** | +12.0% / +6.4% |
| **VVIX** | 84.42 | **102.66** | **+21.6%** |
| `^SKEW` | 151.58 | **147.02** | **−3.0%** |
| VIX9D/VIX · VIX3M/VIX | 0.8238 · 1.2120 | **0.9922 · 1.1059** | front end caught the belly; cash curve flattened |
| M1:M2 adj | +11.51% | **+5.53%** | VX/U6 18.1289 : VX/V6 19.1305 |
| MOVE | 73.10 | **82.09** | +12.3%, **+9.68 over F1** |
| OVX · ratio | 44.96 · 3.09 | **60.76 · 3.41 (p96.6)** | 🔴 **FIRE, numerator-led** |
| COR1M | 8.60 [9/6] | **14.38** [9/11 tick] | +67% |
| JPY RV10 · USDJPY | 10.18% p69.6 · 156.22 [9/4] | **13.89% p89.7 · 154.21** [9/11] | **0.08 from the WATCH line** |
| CCC · CCC−BB | 10.51 · 8.99 [9/3] | **10.64 · 9.06** [9/9] | widening slowly |

**Convergence 28 → 33/50, composition INVERTED** (rates vol 2→5 · oil vol 3→4 · JPY 2→3 · VVIX 2→3 · tail 5→4). **FT-10 = 0-of-4** (RED's grade 9/9; 9/8's 148.86 killed the run on its value). **Cheap-tail CLOSED 2/4.** **FLAT throughout.**

---

## WHAT I DID

### 1. ⛔ VECTOR 2 delivered — verdict NOT CHEAP, structure DECLARED NONE
`PROME/inbox/2026-09-11_from-VIOLET_VECTOR-2-cheap-vol-into-FOMC-read.md`.
- **VIX 17.84 vs SPX RV10 9.84% ⇒ VRP +8.00 vol pts (1.81×).** RV5 11.17 · RV20 8.73 · Parkinson-10 6.26.
- **Stripping three quiet days out of VIX9D leaves ~1.45% priced per event day** (CPI/FOMC/OPEX) vs a 0.62% realized daily. Assumptions declared inline; token ESTIMATE.
- **The decay is monotone in tenor** (+47.9% at 9d → +6.4% at 180d) ⇒ **a dated event stack being priced, not a regime re-rate.** `^SKEW` **fell** while everything else bid.
- **Structure = NONE on four legs of the design's own letter:** gate 2-of-4 · **GATE-VIO-RV1 F2-KILLED 8/27** · **S1 (VVIX ≥105) is 2.34 points away** · **F3** (expensive tails contradict a cheap-tail window). → KB-VIO-275
- **Root rule #6 gate written** (long vol = the PUT side = enter on a GREEN close; 9/10 was RED, SPX −0.58% / VIX +8.38%) with **TERRY's ratified break test instantiated on the design's own F3 number** — debit ≤ ⅓ max width AND below the last GREEN session's debit, both on the card before the fill. **I did not price the chain — that is TERRY's data and TERRY's domain by design §5.**
- **Falsifier F-B registered PRE-CPI with nothing riding on it:** if SPX realized 9/11–9/16 exceeds **17.84% annualized** (daily closes averaging >1.12%), the VRP call is refuted. **Grades at the 9/16 close.** → KB-VIO-270/271

### 2. 🔑 `VX_DAILY` was missing three sessions and my own gap check said it wasn't
`vx_daily_gapcheck.py:121-122` — `hi = max(have)`, where `have` is **the ledger's own dates**. **The audit's upper bound is the audited file's last row**, so a trailing-edge gap cannot exist by construction. **Same `rc=0 … no gaps` at 416 rows broken and 419 repaired.** Its docstring says it exists because *"today is fresh no matter how many holes sit behind it"* — **it closed the holes behind and left the hole ahead open.**
- **Compounding cause: `backfill.py` UPDATES rows, it never CREATES them** — a `--spot-only` run over the gap touched 27 rows, added 0, reported "2,496 cells agreed."
- **Repaired:** 9/8 · 9/9 · 9/10 written from CBOE, all six spot columns confirmed, `basis=SETTLE`, **`m1m2` left BLANK** (T-1 vs same-day convention hazard unresolved; a blank is the absence of a claim). Control re-run: **2,514 agreed / 0 corrected / 0 filled.** Gapcheck now 419 rows.
- ⛔ **Guard NOT changed** — a span change at 01:1x on one session's diagnosis is the ship-then-audit pattern RV1 was killed for. **Correct spec, zero free parameters: `hi` = the newest date CBOE publishes for VIX with ≥1 companion series.** → KB-VIO-273

### 3. 🔴 OVX fired, and this time the numerator led
OVX **60.76** (p92.9), ratio **3.41** (p96.6, FIRE line 3.21), gap 42.92 (p96.2). **OVX +35.1% vs VIX +22.8%** — unlike 9/3, which I correctly refused as a denominator artifact. Above **both** fired analogs (Abqaiq 3.31, Israel-Iran 3.31). **Upgraded to 4 in the matrix on that discriminator.** 🔑 **Sizing consequence cuts against buying: with oil vol leading, a long index-vol structure is the ~$6,007 energy sleeve expressed twice.** → KB-VIO-274

### 4. ✅ Inbox drained 13/13, every sender (WQ-206 outcome ①)
5 top-level + 8 WALTER, all `git mv`'d to `processed/`, 13 rows in `board_log.tsv`.
- **PROME 9/10 cheap-tail:** re-graded **2/4 DORMANT** on the 9/10 bars; **re-open rule written** on the STATUS row (all four legs on ONE dated close; A5 then needs two consecutive settles).
- **RED 9/9 FT-10:** accepted and extended with 149.25 [9/9] · 147.02 [9/10]. **The third surface RED named, `skew_integrity.py`, does NOT carry the count — absence VERIFIED at the owner-declared path.** ✅ **Corroboration found: CBOE's `VIX_History.csv` has a 09/07 bar at 15.30 while VIX9D/VIX3M/VVIX/SKEW all omit it** — the grading source has no Labor Day bar, so RED's non-session ruling is what the file contains.
- **WALTER SIG-010 ($9.6T):** verified **and corrected in both directions** — traces to a **Citadel Securities** publication (not just the X post), **but $9.6T expires BY 9/18 (~35% of total exposure) and $6.2T ON 9/18 (~23%)**; the kernel reads as if it all lands on 9/18. Citadel page fetch returned **403**, so the split is INFERRED from the search extract.
- DEWEY REQ-002 info-only (no dated vol catalyst → nothing enters CATALYSTS.tsv). PROME 9/6 Codex packet consumed late — both asks were already executed on 9/6.

### 5. Write-backs
STATUS rebuilt on the **9/10 SETTLE** basis (**32,067 → 25,525 B**, 47% of cap; 9/6 header archived verbatim, crc32 `03f37693`) · NEXUS_BRIEF rewritten (**36,323 → 14,265 B**, 66 lines; old brief archived, crc32 `7373e9f3`) · **KB-VIO-270→275** · board_log +13 · VX_DAILY 416 → 419 rows.

---

## NEXT SESSION (priority order)

1. 🔴 **Fix `vx_daily_gapcheck.py`'s span** — `hi` = newest CBOE VIX date with ≥1 companion, **never `max(ledger dates)`**. Then **pair it with `backfill.py`'s inability to CREATE rows** — fixing one without the other leaves the hole.
2. 🔴 **Bound `surface_agreement.py`'s memo glob to the session date** — it reads every past `*_from-VIOLET_*` memo as a LIVE surface, so it is **permanently red** on any figure that legitimately moved, and its printed remedy ("re-derive the non-canonical surface") would mean **editing a delivered record**. Pairs with #1: both are references that are wrong, not thresholds that are loose — **but #1 fails silent and this one fails loud-and-unfixable, which is the kind that trains you to wave reds through.** → KB-VIO-276
3. 🔴 **GRADE F-B at the 9/16 close** — SPX realized 9/11–9/16 vs 17.84% annualized. **Registered pre-CPI; grade it whichever way it lands.**
4. 🔴 **Pull the 9/11 CPI reaction and the 9/11 15:30 COT release** (the 9/8 report — first new positioning since 9/1, and the matrix has carried p51.9 for ten days).
5. 🔴 **D#11 call `skew_integrity.py` from `cheap_tail.py` at the `^SKEW` pull** — the window is CLOSED now, which makes this cheap to do and easy to forget.
6. 🟠 **`thresholds.py` still writes the leading-edge row from yfinance** — open since 9/6; it is the exact window an FT-10 bar is graded in.
7. 📅 **`VIO-FOMC-0916` grades at the 9/16 · 9/18 · 9/23 closes.** **FROZEN and untouched by VECTOR 2.** Also **9/16 is the VIX quarterly SOQ and the M1:M2 basis break** (pair → VX/V6 : VX/X6).
8. 🟡 **One `[STALE]` dashboard row left — VIX options C/P (9/6).** JPY vol was refreshed this session and is **0.08 from WATCH**; it needs watching, not refreshing.
9. 🟠 **D#10 `TRADE.md`** (the 7/30 close row + WQ-177 heading strike + vintage header) · **D#8 prediction registry** — now owes it **two** more sets of legs (`VIO-FOMC-0916` ×5 and F-B) · **`workbook/LEDGER_GLOB` still absent.**

## CARRY-FORWARD

- **HENRY's gamma board is EXPIRED, not current** — 9/4 on the 9/3 close, and HENRY's own finding is a **one-session shelf life**. **Never carry a HENRY gamma sign into a VIOLET file in either direction; read HENRY's current brief.** HENRY says re-run `gamma_flip.py --days 35` before 9/16 and 9/18.
- **FOMC hike odds moved off the coin flip** — CME FedWatch ~59–60%, Kalshi 57%, Polymarket 49% (9/10–9/11 secondary coverage, **INFERRED**). The 9/7 reading PROME carried is four days stale. **Re-check at a primary before quoting.**
- **RED-FT-06's exit line (VIX ≥18 sustain-5) is 0.16 away for the first time.** RED-owned; do not grade it.
- **Publication timing for `SKEW_History.csv` remains UNVERIFIED** — same-day availability observed, no cadence established. Grade when the dated bar exists.

## OPEN HYPOTHESES (flagged, not actionable)

- **H-new: the front-end repricing is an OPEX artifact as much as an FOMC one.** ~$6.2T expiring 9/18 with dealers plausibly short gamma below the flip would mechanically bid short-dated vol independent of the macro. **Not testable with what I own** — it needs HENRY's gamma board and an OI term breakdown. **Flagged so the 9/16 F-B grade is not read as a clean FOMC test if realized runs hot into OPEX.**
- **H-carry: is the VRP measured against TRAILING realized systematically biased into a dated event stack?** Tonight's read depends on it and I named the weakness rather than resolving it. **Base-rateable: VIX-minus-RV10 at T−4 before FOMCs vs realized T−4→T+0.** Do not quote a number until it is run. `[[finding_base_rate_the_threshold_before_building_it]]`.
