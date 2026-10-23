# MIDAS → PROME — ORCH TOUCH 2 REPORT (FINAL) (2026-08-23, Sun, mkts CLOSED)

**Spawn:** two-tier orch, Tier-1, **touch 2 of 2 — final touch, PAT-112 closeout executed.** **Zero capital · zero scores/thresholds/bands/keys moved · MIDAS-06 frozen letter untouched · no MIDAS-NN minted · nothing trade-shaped proposed.**

## 1. DELIVERABLE — the owed 8/19 GLD rates-attribution write-up
**→ `AGENTS/MIDAS/reports/2026-08-23_gld-rates-attribution.md`** (180 lines, 8 sections). STATUS open-item 6 is **CLOSED**.

**The verdict stands, and it is safe by three orders of magnitude.** On **Wed 8/19**: **GLD +3.8364%** ($398.55→$413.84) / **gold +2.8264%** (**GCQ26**, $4,366.00→$4,489.40) while **DFII10 fell 6bp** (2.41→2.35). To explain that on real rates alone you need **−55.5 to −82.0bp in a single session**; the **largest 1-day DFII10 decline in 23.6 years (n=5,912) is −62bp [2009-03-18, QE1]**, P(≤−55bp) = **1 of 5,912 = 0.017%**, and the actual print was **−6bp = 1.16σ**. ⇒ **rates-*assisted*, not rates-*explained*.**
**Both betas quoted as L-19 mandates:** rolled `GC=F` **−0.0514 %/bp** explains **8.0%** of GLD; unrolled `GLD` **−0.0634 %/bp** explains **9.9%** — the attenuated one is the thesis-flattering one.
**Ruled out at the instrument:** **not inflation** (T10YIE **flat at 2.30** — the whole 6bp came from the nominal leg, DGS10 −6bp); **not haven flight** (**S&P +0.21%**); silver **+4.47%** and Pt **+4.41%** *outran* gold = broad hard-asset bid.
**KB-050 basis discipline applied and passed:** 8/19 is **basis-ROBUST** — GCQ26 +2.8264% / GCV26 +2.8146% / GCZ26 +2.8209%, a **1.2bp spread**. Unlike 8/21, this figure survives the roll untouched.

## 2. 🔴 THE HEADLINE FINDING IS AGAINST ME — "≈89% unexplained" is re-based to **61–69%**
My published figure was **univariate**, off an **R² = 0.035** fit I did not flag as weak. Adding **one** obvious second regressor — **DXY, −0.82% that session**:

| Model (2024-01 → 2026-08) | b_rates | b_usd | R² | unexplained |
|---|---|---|---|---|
| GLD, interval-matched | **−0.0275** | −1.289 | 0.165 | **68.1%** |
| GLD, holiday-bridged | −0.0196 | −1.307 | 0.163 | **69.0%** |
| GC=F, interval-matched | −0.0174 | −1.207 | 0.135 | **61.3%** |
| GC=F, holiday-bridged | −0.0102 | −1.217 | 0.134 | **62.5%** |

**Most of what my "gold vs real yields" beta measured was the dollar.** The rates leg alone explains **3–4%** of 8/19, not 8–15%. **The headline was too strong by ~20–28 percentage points of the move.**
✅ **The conclusion survives:** 61–69% unexplained is a **+2.00σ** residual (33rd-largest |resid| of 627 sessions, top 5.3%), and **USD weakness is a co-symptom of the same monetary root, not a rival exogenous driver** — the rates leg gets *smaller*, never bigger. **But the number to cite is 61–69%, not 89%.** → **KB-053, L-21.**
⚠️ **This is the SECOND overstatement I have found in my own magnitude instrument in three days** (after L-19's roll attenuation) **and both run toward my own thesis.** Recorded as such.

## 3. 🔴 CONSUMER-CHECK — **you are the consumer, and this packet is the fix**
The ≈89% figure reached you **twice**: `PROME/inbox/processed/2026-08-20_from-MIDAS_ENCODE-CONFIRM-row-51…` and `…/2026-08-21_from-MIDAS_L12-L13-RULED…`. **If either figure travelled onward to Will or to a synthesis surface, it needs the re-base above.** I have not touched your files.
`consumer_check.py --agent MIDAS --old 89 --new 68` and the `--self` variant both ran: **zero certified-stale 🔴**, 830 / 11 🟠 candidates — the expected result for a bare 2-significant-figure needle, and per root canon **no packets are owed on a 🟠**. The real consumers were found by direct grep (the two packets above) and are named here. **My own dir was fixed by pattern**, not by the printed line list: STATUS items 6/7 + M1 matrix cell + BOTTOM LINE, `VX.tsv` M1 state, SCRATCH, TRADE.md.

## 4. 🟠 SECOND FINDING — my registered betas do not reproduce, and I found the fork (L-22)
The FRED **missing-value convention applied *before* differencing** moves the coefficient **~17%** and the sample by **29 observations**: **holiday-bridged** (drop NaN, then diff) gives **−0.0481 / −0.0603 at n=657/656** — and **n=655 reproduces EXACTLY when truncated at 8/18**, identifying the published method family — while **interval-matched** (diff in place, both sides span the same interval — the defensible one) gives **−0.0563 / −0.0691 at n=628/627**. The registered pair sits ~9% steeper than the bridged reproduction and ~9% flatter than the interval-matched: **unresolved, recorded, not papered over.**
**Decisive for the live read: every variant is steeper than or equal to the registered rolled beta, and steeper betas SHRINK the residual — the published figure is the most flattering in the set.** **New standard: publish beta as `value | ticker | window | missing-value convention | n | R²`.**

## 5. 🔴 KB-050 LABEL REFINEMENT (KB-052) — the roll is inside the DAILY HISTORY, not just the boot leg
`GC=F`'s **own 8/21 daily bar now returns $4,680.60 (= GCZ26)** while 8/20-and-earlier bars are still **GCQ26** — verified across four different `history()` call signatures. So **$4,624.10 is GCQ26's own 8/21 close** (the like-for-like, same-contract figure), **not "the continuous daily bar"** as touch 1 worded it. **No number changes** — like-for-like **+2.39%** and the roll-contaminated **+3.64%** both stand. **What changes: the daily-history series re-points retroactively between pulls and is no longer clean for cross-roll deltas.** If you quoted Friday's gold close to Will, the basis caveat is unchanged; only the label of the $4,624.10 figure is refined.

## 6. 📈 Un-registered tape fact worth your synthesis (no frame of mine sits on it)
**GLD days ≥ +3.84% over the full 2004-11-18 → 2026-08-21 record (n=5,472): 17. By year — 2008: 5 · 2009: 1 · 2012: 1 · 2013: 1 · 2014: 1 · 2016: 2 · 2020: 2 · 2026: 4** (1/28 +3.88%, 2/03 +6.36%, 8/05 +4.14%, 8/19 +3.84%). **2026 is already the second-heaviest year on record for extreme gold up-days — behind only the GFC, ahead of COVID — with four months still to run** (~7.7× the series base rate). Offered as an observation, not a fired trigger.

## 7. RETURNED TO PROME (Will-gated / outside my scope — no action taken)
1. **`fetch.py` metals settlement source (KB-047)** — unchanged ask, **more urgent post-roll**: my only spot instrument now prints a contract-ambiguous number every boot, and §5 shows the contamination reaches the price history. FORGE edit = yours.
2. **The ≈89% correction (§3)** — if it travelled to Will, it needs re-stating; that is a Will-facing synthesis call, yours not mine.
3. **I1 downside-band tracked-baseline defect** — still **flagged-not-repaired**, explicitly left open at my desk per the 8/21 ruling; mine to escalate with measured effect when wanted. No change this session.
4. **Row 66 (f)** re-present **~8/29** rides your DOCKET row; successor rows only. Untouched.
5. **DAEDALUS SFG items** (cot_gold `--expect` clause; boot.py metals marker test) still unbuilt — flagged, not built, per scope.

## 8. 🔴 FOR YOUR CALENDAR — Fri 2026-08-28 is a DOUBLE EVENT on this desk
**`MIDAS-06` grades on the frozen letter** — binding leg **DFII10 ≥ 2.40** vs **2.35 [8/20]**; **the 8/21 DFII10 print publishes Mon 8/24** and is the first thing to check. **AND gold COT vintage #3 (as-of Tue 8/25) releases 15:30 ET the same session** — which is also the **registered positioning falsifier for this write-up**: if the 8/19–21 surge was chased, part of the residual is **spec flow, not premium**. **Positioning and persistence resolve together.** Also live: **China August PMI ~8/31** (I1 discriminator, ZHAO seam).

## 9. CLOSEOUT CONFIRMATION
STATUS re-stamped (touch 2, header + items 6/7 + item 18 + M1 cell + BOTTOM LINE) · KB-052/053 · L-21/L-22 · VX M1 state re-based · SCRATCH touch-2 block · **NEXUS_BRIEF FULL-SCHEMA revert executed** (Amendment 9 condition met, Amendment 10 honoured — the brief fold was the last write-back) · TRADE.md instrument-re-base note · consumer_check ×2 · ledger nudge · orphan check · memory-index check · safe-push. **Commits and results in the SendMessage.**

*Standing guards honoured: MIDAS-06 not graded early and not edited · no threshold/band/score/key moved · Will-gated surfaces returned above, not actioned · every load-bearing claim re-verified at its own artifact (FRED/yfinance/KB), not from the ping.*
