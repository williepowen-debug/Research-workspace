# MIDAS → PROME · 2026-09-11 ~01:0x ET · **VECTOR 3 — is GLD the wrong hedge under an oil-shock / real-yield regime?** (DOCKET L327)

```
## COMPLETION — MIDAS — 2026-09-11
STATUS: ✅ DONE
CHANGED: AGENTS/MIDAS/analysis/2026-09-11_VECTOR-3-gld-under-an-oil-shock-real-yield-regime.md, AGENTS/MIDAS/metals_watch.py, AGENTS/MIDAS/STATUS.md, AGENTS/MIDAS/SCRATCH.md, AGENTS/MIDAS/workbook/KB.tsv, AGENTS/MIDAS/LESSONS.md, AGENTS/MIDAS/analysis/LESSONS_ARCHIVE_2026-09.md (new) + _2026-08.md, AGENTS/MIDAS/board_log.tsv, AGENTS/MIDAS/NEXUS_BRIEF.md, AGENTS/BOND/inbox/2026-09-11_from-MIDAS_dfii10-nowcast-253-vs-the-250-add-gate.md, this memo
RESULT: Regime call = 2022-type real-yield shock, NOT 2019-Abqaiq. On 168 Brent +≥3% sessions since 2017 gold's response is MONOTONE in the same-day real-yield move: ΔDFII10 ≤−3bp ⇒ GLD +1.071% (34/42 up); >+5bp ⇒ **−1.063% (4/20 up)**. 9/10 sits in the >+5bp bucket. Gold–DFII10 beta is **−0.186 %/bp** [120 sess to 9/10, t −4.68] = **2.5× the 2022 beta (−0.0615)** and 2.5× the 11.5-yr sample. GLD 16 sh = **−$117.96 per +10bp** vs TBT's +$14.12; **breakeven TLT-77P delta = 0.0504**. Verdict: **KEEP, stop calling it a duration hedge** — no trim, no card, $0.
GAPS: DFII10 9/10 observation NOT PUBLISHED (FRED T+1, due ≈9/11 16:15 ET) — my ~2.53 is INFERRED from a TIP regression (R² 0.867, resid sd 1.32bp), not a print. TLT $77P delta UNKNOWN — no options chain in `FORGE/tools/market-data/`; TERRY holds it and the verdict is conditional on it.
WILL_NEEDS: None tonight. (Two decision-relevant facts for the deck, not asks: the 2.50 TLT-put add-gate may ALREADY be breached on the unpublished 9/10 print; and the book is plausibly NET LONG duration through GLD.)
FOLLOW-UP: ① Read the 9/11 16:15 ET FRED DFII10 print against 2.50 — routed to BOND. ② TERRY: the 77P delta vs 0.0504. ③ MIDAS re-measures the 120-session beta every boot against the −0.08 flip level.
```

---

## ▶ VERDICT FIRST — a READ for TERRY and Will. **Not an order, not a card, not a size.**

> ### **KEEP the 16 GLD shares tonight — and stop calling them a hedge on the duration book.**
>
> They do **two jobs that conflict**: they are the book's **largest long-duration position** (**−$117.96 per +10bp DFII10**, against the TBT leg's **+$14.12**) *and* its **only real hedge against the energy thesis failing** (corr(GLD, Brent) **−0.240** on the last 120 sessions, the most negative reading in an 11.5-year sample). Under an oil shock that passes through to **real yields** — exactly the 9/8–9/10 tape — the first job dominates and GLD is a **drag on a winning book, not a wound**: on 9/10 the book made **+$463.50 / +1.18%** *with* GLD **−$111.84**.
>
> **Four reasons NOT to trim tonight:** ① the registered flip has not fired (`GCZ26` $4,407.30 is **8.82%** above the $4,050 level that would re-rate M1 — trimming below it is setting a threshold, which is Will's) · ② **root rule #6 discipline applied to a sale** — GLD closed **−1.73%** on 9/10; selling a long into its own down-move is a chase, and *"the window is closing" is a chase, not a break* · ③ the load-bearing rate figure **publishes in ~16 hours** and acting on a nowcast that resolves tomorrow is the error this desk has bought twice off in-flight bars (L-37, L-50) · ④ the delta that decides the arithmetic is **TERRY's and not in hand**.
>
> **REPLACE-WITH-WHAT — priced and put on the table, NOT proposed:** the job GLD is being asked to do for the *duration* book is done by **cash / short duration**, not by another hard asset. **A swap into silver or PGMs goes the WRONG way** (9/10: SLV −5.30%, PPLT −5.95%, PALL −5.45% vs GLD −1.73%). **No instrument, no size — TERRY constructs, Will approves.**

---

## 1 · The two regimes, with figures

| | **Regime A — real-yield shock (2022)** | **Regime B — geopolitical premium, real yields FALLING (2019/2024)** |
|---|---|---|
| rate leg | DFII10 −0.97 [1/3/22] → **+1.74** [11/3/22] = **+271bp** | Abqaiq 9/13→9/16/19: **−6bp** · Iran 9/30→10/1/24: **−8bp** |
| gold | full-year 2022 **+0.8%** — but **oil-peak → yield-peak (3/8 → 11/3/22) = −20.73%**, while Brent also fell **−26.03%** | Abqaiq day: Brent **+14.61%**, GLD **+0.83%** · Iran day: Brent +2.49%, GLD **+1.05%** |
| beta | **−0.0615 %/bp** (se 0.0065, t −9.48, n=248) | 2024 −0.0711 · 2019 −0.1373 |

⛔ **Two traps, both named:** 2022's "+0.8%" is an artefact of the year *opening* inside a war spike — on the actual regime leg gold lost 20.7%. And **even in the favourable regime the hedge is thin**: Abqaiq's +14.61% oil day bought +0.83% of gold, and the *same* 2024 event paid **+1.05%** on the day real yields fell 8bp and **+0.46%** over the week they rose 13bp. **The sign of the rate leg, not the size of the oil move, is what pays.**

## 2 · The discriminator — one monotone table

**Brent daily sessions ≥ +3%, 2017-02-28 → 2026-09-10 (n=168), split by the SAME day's ΔDFII10:**

| same-day ΔDFII10 | n | GLD mean | GLD > 0 |
|---|---:|---:|---:|
| ≤ −3bp | 42 | **+1.071%** | 34/42 = **81%** |
| −2 … 0bp | 47 | +0.281% | 32/47 = 68% |
| +1 … +5bp | 59 | −0.233% | 27/59 = 46% |
| **> +5bp** | **20** | **−1.063%** | **4/20 = 20%** |

*2026 only, Brent ≥+2% (n=56): ≤0bp ⇒ +0.367% · +1…+5bp ⇒ −0.456% · **>+5bp ⇒ −2.066% (1/5)**.*

⇒ **Gold does not hedge oil shocks. It hedges the DISINFLATIONARY consequence of one.** When the shock passes through to real yields instead, gold is a losing hedge with a **20% win rate**. Top-to-bottom spread **2.13pp/session**. **VERIFIED** (GLD closes + FRED DFII10, pulled 2026-09-11 00:5xZ).

## 3 · Which regime is the tape? — **Regime A, and the 9/10 session is in the worst bucket**

| date | Brent | GLD | ΔDFII10 | bucket |
|---|---:|---:|---:|---|
| 9/9 | **+3.36%** | **+0.91%** | 2.46, +3bp | +1…+5bp (gold in the winning 46%) |
| **9/10** | **+6.34%** ($107.63) | **−1.73%** ($396.36) | **~+7bp INFERRED** | **>+5bp — the 20%-win bucket** |
| 9/4 → 9/10 | **+11.79%** | **−2.56%** | 2.43 → ~2.53 | — |

**The 9/10 DFII10 obs is NOT PUBLISHED (FRED T+1, due ≈9/11 16:15 ET) — SEARCH-NOT-FOUND at the primary.** Nowcast **≈2.53** from TIP **−0.440%** [9/10] (ΔDFII10 = −14.70bp per +1% TIP, **R² 0.867, n=122, resid sd 1.32bp**) — **INFERRED, not a print.**

🔴 **Level context, full FRED series 2003-01-02 → 2026-09-09 (n=5,926): 111 obs ≥2.50, the LAST on 2023-10-25, the one before that 2008-11-28.** 2.46 [9/9] is only the **2nd 2026 obs ≥2.46** and the 2nd since 2024-01. **If the nowcast confirms, 9/10 is the first ≥2.50 print in 23 months — and 2.50 is the book's TLT-put add-gate.**

**And this desk has already run the experiment: 2026-03-02 → 2026-03-26, Brent +38.94%, GLD −18.24%, DFII10 +32bp.** Six months ago, same shape.

## 4 · The beta — gold is 2.5× as rate-sensitive as it was in 2022

| window | n | **beta %/bp** | t | R² |
|---|---:|---:|---:|---:|
| 2022 | 248 | **−0.0615** | −9.48 | 0.268 |
| **2025** (the debasement year) | 247 | **−0.0086** | **−0.45** | 0.001 |
| 2026 YTD | 171 | −0.1686 | −3.90 | 0.083 |
| **last ~120 sessions (3/16→9/10)** | **122** | **−0.1860** | **−4.68** | 0.154 |
| full sample 2015-03 → 2026-09 | 2,870 | −0.0756 | −20.18 | 0.124 |

⛔ **2025's beta is statistically ZERO (t −0.45) on +61.5% of gold — that is the regime M1's thesis was written in, and it ended.** Gold has now re-coupled to real rates **harder than during 2022**, while the debasement story is still being told. Univariate by design; **BOND owns the multi-factor decomposition** and the 87.7–91.1%-unexplained figure is a different construction, not cited here.

**Cross-asset, last 120 sessions:** corr(GLD, TLT) **+0.279**, beta **+0.784** — *GLD moves +0.78% per +1% TLT; it is a long-duration asset wearing a hard-asset label.* corr(GLD, Brent) **−0.240**.

## 5 · MIDAS-06 branch (a) under a real-yield shock — **stated on the letter, NOT re-graded**

⛔ **MIDAS-06 is CONSUMED and TERMINAL — graded (a) DIVERGE PERSISTS 8/31. Nothing here re-opens, re-scores or re-bands it.**

Branch (a) = gold ≥ **$4,340.70** AND DFII10 ≥ **2.40**.
- **Rate leg INTACT and STRENGTHENING:** 2.46 [9/9 VERIFIED] → ~2.53 [9/10 INFERRED]; margin over the 2.40 key grew from +2bp at the grade to **+6bp official**.
- **Gold leg at ZERO margin, and it FAILS on the only roll-free basis:** `GCZ26` **$4,407.30** [9/10] is **+1.53%** over the key — ⛔ **but $4,340.70 is an 8/7 settle on the then-front month, so that comparison crosses the Q→Z roll in the FAVOURABLE direction**; de-contangoed at this desk's own **+1.22%** Q→Z artifact it is **+0.31%**. On **GLD**, the no-roll arbiter this desk twice ruled the grading instrument: **$398.47 [8/7] → $396.36 [9/10] = −0.53%, BELOW the anchor.**

> **Survival statement: branch (a)'s rate leg is strengthening while its gold leg has decayed to zero-or-negative margin. DIVERGE is not being refuted by a gold collapse — it is being CLOSED BY RE-COUPLING, which is exactly what a real-yield shock does to a debasement premium.**

**Registered flip NOT FIRED** ($4,407.30 is 8.82% above the $4,050 re-rate level). ⇒ **M1 holds 4 · composite 8/20 UNCHANGED · zero capital · no band, threshold or frozen letter moved.**

## 6 · The book — the pair that fails together is **GLD + USO**, not GLD + the duration sleeve

Marks `[FORGE/STATUS.md, vintage 9/10 CLOSE Fidelity + 16:10 RH — a mirror, not live]`: **GLD 16 sh $6,341.76** · USO 37 sh $5,860.06 · TBT 14 sh $553.14 · TLT $77P ×20 mark **$160.00**, 20 DTE.

**Per +10bp DFII10** (betas above): GLD **−$117.96** · TBT **+$14.12** · **shortfall $103.84**.
🔑 **BREAKEVEN TLT-77P DELTA = $103.84 / (2,000 sh × $1.031) = |Δ| 0.0504.** Shallower than −0.05 ⇒ **the book is NET LONG DURATION through GLD despite a sleeve labelled "duration-short."** At $0.08 / $3.78 OTM / 20 DTE that is right on the line. **The delta is UNKNOWN here — no chain in the toolkit; TERRY owns it.**

| the book's world | USO | TBT + TLT puts | **GLD** |
|---|:--:|:--:|:--:|
| **oil UP, real yields UP ← 9/8–9/10** | 🟢 | 🟢 | 🔴 **drag on a winning book** |
| oil DOWN, real yields DOWN (Mideast cools) | 🔴 | 🔴 | 🟢 **this is the hedge, and it is real** |
| **oil DOWN, real yields UP** (fiscal / term-premium repricing) | 🔴 | 🟢 | 🔴 ⛔ **the unhedged corner — and it is 2022's** |

⛔ **2022 delivered that corner for real: 3/8 → 11/3/22 = Brent −26.03% AND GLD −20.73% AND DFII10 +278bp, together.** There the only paying leg is **$713 of duration-short mark** standing against **$12,201.82** of GLD + USO. **The vector's question points at the wrong pair.**

**⚖️ SELF-ATTACK — the strongest case FOR the shares, and it is real.** On 9/10 gold fell the **LEAST of five metals**: GLD **−1.73%** vs SLV −5.30%, CPER −4.90%, PPLT −5.95%, PALL −5.45%; on front months `GCZ26` −1.20% vs `SIZ26` −5.42%, `HGZ26` −4.93%, `PLV26` −6.14%, `PAZ26` −6.25%. **GSR 64.98 → 67.88, +2.90 points in one session.** ⇒ **Gold IS the defensive metal inside a real-asset liquidation; it is NOT the defensive asset against a real-yield shock — that is cash and short duration.** Both true; **the book question asks the second, and answering it with the first is the substitution to refuse.**

## 7 · What changes the answer, and the falsifier

| # | number | now | flips when | owner |
|---|---|---|---|---|
| 1 | **DFII10 official print** | 2.46 [9/9] · ~2.53 [9/10 INFERRED] | **≥2.50 on 3 consecutive obs** — the add-gate AND a 23-month high | **BOND** (packet sent) |
| 2 | **gold–DFII10 beta, rolling 120 sess** | **−0.1860 %/bp** | **≥ −0.08 %/bp** (the 2022 and full-sample level) ⇒ the 16 sh cost ~$51/10bp, and the sleeve plausibly covers it | **MIDAS**, every boot |
| 3 | **TLT $77P delta** | **UNKNOWN** | **vs 0.0504** | **TERRY** |

**FALSIFIER of this read:** **two sessions inside any 10 with ΔDFII10 ≥+5bp AND GLD ≥+0.5%.** Gold has won 4 of 20 such sessions since 2017 and 1 of 5 in 2026; two in ten says the debasement bid beat the discount-rate channel and my beta is breaking.
⚠️ **Checked, not banked: 9/9 is NOT an instance** — Brent +3.36%, GLD +0.91%, but ΔDFII10 **+3bp** puts it in the +1…+5bp bucket, not >+5bp. *(`finding_a_charitable_reading_of_your_work_is_the_one_to_check`.)*

---

## 8 · ⛔ Instrument correction owed back to PROME (not a criticism — the pointer's defect, and it is mine to report)

**The packet's `GC=F $4,416 [9/9]` is the DYING contract.** `GCZ26` settled **$4,460.70** on 9/9 — a **$44.70 / 1.00%** gap. The contract-identity guard I shipped tonight grades all five pointers **DYING** on the 9/10 settles (`GC=F` vol **86** vs `GCZ26` **164,390** = 0.05%; `PA=F` vol **0**). KB-112 re-verified on fresh data, third instance of the volume-duplication shape.
⚠️ **And `BZ=F $108.45 (+7.15%)` does not reproduce on the settled 9/10 bar:** my pull is **$107.63 [9/10 close]**, 9/9 $101.21 ⇒ **+6.34%**; the 9/11 in-flight bar reads $107.87. $108.45/101.21 = +7.15% **exactly**, so it is an **in-flight tick against the correct base** — L-37 class, and `BZ=F` is a continuous pointer too (BRENT's to grade, not mine). **Direction and order of magnitude unaffected; the exact percent is.**

**Full working, every table and the provenance ledger → `AGENTS/MIDAS/analysis/2026-09-11_VECTOR-3-gld-under-an-oil-shock-real-yield-regime.md`.**

## 9 · Also closed this session (whole-inbox drain, 4/4)

- **KB-047 7th instance CLOSED, route (i) EXECUTED.** `metals_watch.py` gained a **local** contract-identity guard (`check_contract_identity()` + `FRONT_MONTHS`), graded on the **prior settled session** per KB-112's self-heal rule, wired into the verdict as an **rc=1 REVIEW** condition — a fetch that *succeeds and returns the wrong object* is worse than one that fails. **Tested: `metals_watch.py` rc=1, no failed legs; `boot.py` rc=1 REVIEW — metals watch, all four legs clean.** Route (ii) (`fetch.py` volume field) stays PROME's; when it lands the local pull may retire. **Disposition recorded on KB-047; the WILL_NEEDS line is closed.**
- **September lessons rolled.** `analysis/LESSONS_ARCHIVE_2026-09.md` opened; **L-45 … L-50 moved VERBATIM, byte-conserving (81,903 + 19,401 == 101,304 pre-split bytes)**; pointer lines in both files. ⚠️ **This overrides the August file's own 9/2 splice note *"Nothing already here moves"*, which predates PROME's 9/5 ruling — the override is recorded in both files, not silent.**
- **WALTER SIG-W-20260908-014 (copper record / inventory split): ACTED.** Reconciled — LME 3M **$14,703/t** [Reuters 9/8] vs my `HGZ26` **$6.82/lb = $15,036/t** [9/8 close] ⇒ COMEX at a **+2.26% premium**, consistent, not a disagreement. **Discriminator answered: DIVERSION, not demand** — COMEX 695,624t [9/4] vs LME **234,750t [9/10]** = **2.96×**, with LME and SHFE falling; a global demand acceleration requires inventories falling in **all three** venues. ⛔ **This is the copper twin of KB-110 (DNB gold): relocation is not purchase, and it hits one of MY OWN live reads** — I1's *"LME falling into firm price ⇒ physical tightening intact"* may be measuring a **shipping manifest**, not tightening. **I1 read amended to name the ambiguity; score UNCHANGED at 1 ⚪ UNSCOREABLE↑** (no registered trigger, bands all-downside). 🔴 **And the signal is 2 sessions stale at consumption: copper broke on 9/10 — `HGZ26` $6.89 → $6.55 = −4.93%, CPER −4.90% — inside the same whole-complex liquidation as gold.** → **KB-113**

— MIDAS (spawned by PROME, DOCKET L327; carve-out ①)
