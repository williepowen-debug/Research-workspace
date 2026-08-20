# WAL — Scenario Analysis & Target Prices
> **✅ v2.4 RE-MARK LANDED 2026-08-20 — the MI3 disconfirmation is now IN the numbers.** Bear-fast **10% → 2%** (its falsifier ran and returned a negative); freed weight to **Base 45% / Bull 30%**; **bear-medium HELD at 16%**. EV **$73.92 → $75.96**; **overvaluation 12.4% → 5.4%** at spot $80.05 [8/20]; PT **$52-76**. ⛔ **Anti-ratchet verified: total bear 26% → 18%.** See §EV SUMMARY (v2.4) immediately below.
> **⚠️ The Sep-18 cores ($67.5P/$70P) now sit $8.46 and $5.96 BELOW EV** — on the central estimate they expire worthless. Routed to TERRY/Will, not actioned here.
>
> **✅ v2.3 RE-MARK LANDED 2026-07-25 — the Q2 second-data-point test is now IN the numbers.** EV **$68.93 → $73.92**; overvaluation **12.4%** at spot $83.11 [7/24 close, market.py]; PT **$52-74**. See §EV SUMMARY (v2.3) immediately below — the v2.2.1 table is preserved beneath it as the audit trail. **The bear weakened: EV rose $4.99 while price rose only $1.23, so the margin of safety COMPRESSED ~6.4pp.**
> **⚠️ RESIDUAL CORRECTION (2026-07-17 audit — still applies):**
> **POSITION TRUTH:** every "$77.5P **Sep**" reference below is a PHANTOM — per canonical `POSITIONS.md` (5/8 broker refresh + 6/19 reconcile), the $77.5P was **Jun-18 tenor, cleared 6/18**; the live Sep core is **$67.5P + $70P** (plus RH $77.5P **Aug-21**, folded 7/20). The strike-by-strike sections were built in May on the mis-recorded book and are **NOT rebuilt in v2.3** — position-architecture rebuild is reserved for the `AGENTS/WAL/` standup (PROME WP-W2). Grep `POSITIONS.md` before ANY position use — never this file.

**Created:** 2026-03-25 (v1.0) | **Last Updated:** **2026-08-20 (v2.4 — MI3-disconfirmation re-mark: bear-fast 10%→2%, probabilities only, no range moved)**; prior **2026-07-25 (v2.3 — Q2 print re-mark: probabilities + ranges + EV off Q2 actuals)**; prior 2026-06-08 PM (v2.2.1 — macro-NIM tailwind softening + cohort RESOLVED → Hyp A); date-fix 7/10; audit banner 7/17
**Current Price:** **$80.05** [2026-08-20 14:4x ET, market.py] *(was $83.11 7/24 close)* | **TBV:** $61.14 [Q1 — Q2 TBV not re-pulled] | **CET1:** 11.0% [Q2 confirmed]
**Short Interest:** 3.54% float / 2.71 days (Mar 25 — REFRESH PENDING)
**Q1 2026 EPS:** $1.65 GAAP / $2.22 adjusted | **FY2025 NI:** $991M

> **📐 OVERVALUATION CONVENTION (pinned 2026-06-08 v2.2.1):** Overvaluation = **(Price − EV) / EV**. All historical figures herein normalized to this denominator. Prior sessions used inconsistent denominators (sometimes ÷EV, sometimes ÷Price) — corrected below.

> **v2.2.1 thesis framing** (per `THESIS.md` v2.2.1, refinement): v2.2 structural vectors UNCHANGED. v2.2.1 adds macro-NIM-tailwind softening (20Y auction clean + Waller pivot) trimming Bear-medium 30%→25% on **loss-absorption channel only** (timing handled by Sep tenor), and cohort-signal context (SIG-030 NPA improvement at 5/10 names — **RESOLVED 6/8 PM → Hyp A genuine cohort improvement**; WAL bear idiosyncratic, "sharpen to WAL-specific" earned, Bear-medium stays 25 / no revert).

> **v2.2 thesis framing** (per `THESIS.md` v2.2, post 10-Q drill): WAL's concentrated CRE tail risk is **actualizing on Q2 timeline** — one quarter earlier than v2.1's bear-slow case priced. 10-Q subsequent-event note disclosed **$99M life-science office sponsor walk-away** (Bucket B1 fired); Chief Banking Officer Curley resigned same week; market reacted ~10% on combined news. **Bear-slow → Bear-medium speed.** V2 inventory test came back clean (no new Leucadia-era credits); V3 NDFI cohort-median confirmed via 10-Q breakout. V1 MI3 primary falsifier still hasn't run (FFIEC PDD pending). Short thesis is now *partially realizing*; Q2 print (confirmed Tue Jul 21 AMC) is the critical second-data-point test.

---

## EXPECTED VALUE SUMMARY (v2.4 — post-MI3-disconfirmation re-mark) ★ CURRENT

**Trigger:** the **V1a MI3 primary falsifier ran 2026-08-07 and DISCONFIRMED** (Q1-26 23.88% · Q2-26 21.20%, both in the frozen `<24%` PLATEAUED band; never ≥25% in 12 quarters). **Bear-fast's 10% weight sat on a tested-and-failed premise.** Will ruled its disposition 2026-08-12 (batch, row 32b, `PROME/proposals/2026-08-12_rule-batch-RULED.md`) with a hard constraint: ⛔ **total bear must NOT rise on a disconfirmation.**

| Scenario | v2.3 Prob | **v2.4 Prob** | Δ | Range | Midpoint | Weighted |
|----------|----------|--------------|----|-------|----------|----------|
| Bear-fast (V1a MI3 ≥25 trigger) | 10% | **2%** | **−8** | $52-62 *(unch)* | $57.00 | $1.14 |
| Bear-medium (V1 Office migration) | 16% | **16%** *(unch)* | 0 | $58-66 *(unch)* | $62.00 | $9.92 |
| Base | 40% | **45%** | +5 | $74-82 *(unch)* | $78.00 | $35.10 |
| Bull | 27% | **30%** | +3 | $86-94 *(unch)* | $90.00 | $27.00 |
| Tail | 7% | **7%** *(unch)* | 0 | $35-45 *(unch)* | $40.00 | $2.80 |
| **Expected Value** | **$73.92** | **100%** | | | | **$75.96** |

**⛔ ANTI-RATCHET CHECK — the binding constraint on this re-mark, verified both ways:**
**Total bear (fast + medium): 26% → 18%. FELL 8pp.** Including Tail: 33% → 25%, also fell. **A disconfirmation reduced the bear. Constraint satisfied, not merely respected.**

**Overvaluation (÷EV convention, pinned):** (80.05 − 75.96) / 75.96 = **5.4%** at spot **$80.05** [2026-08-20 14:4x ET, market.py].

### ★★ THE HONEST HEADLINE: the margin of safety has NEARLY CLOSED — 18.8% (7/17) → 12.4% (7/25) → **5.4% (8/20)**

**And this time only HALF of it is my own re-weight.** At v2.3 the compression was entirely EV-side (EV rose $4.99, price rose $1.23). Here it is two-sided: **EV rose $2.04 (+2.8%) AND price fell $3.06 (−3.7%)** from the v2.3 mark. The price leg is *bear-supportive* — the tape came toward the thesis — but it was swamped by my own EV increase. **Net: WAL is still overvalued against my EV, but by 5.4%, which is inside the range where the honest answer is "barely."**

> ⚠️ **POSITION CONSEQUENCE, stated because it is the most decision-relevant line in this file and it cuts AGAINST the book.** The live Sep-18 cores sit **BELOW** the new EV: **$67.5P is $8.46 below EV · $70P is $5.96 below EV.** On my own central estimate both expire worthless. That was already true at v2.3's $73.92 and it is **$2.04 worse now.** **This is not a trade recommendation and I do not make one** — position action is TERRY + Will [Approve] + a live chain (root rules #4/#5). It is the fact the re-mark produces, routed rather than buried.

### Re-weight rationale — every line tied to the graded result

| Shift | Driver |
|---|---|
| **Bear-fast 10% → 2%** | Its **defining mechanism was measured and found absent.** MI3 never reached its own 25% trigger in **12 quarters**; all-time high 24.24% never came within **76bps** of it; the ≥27% hard-confirm band sits **276bps above the all-time high**; and since 2025Q1 the series oscillates in a ~3pp band with no direction. This is not "unconfirmed" — it is the falsifier running and returning a negative on two concordant quarters. |
| **…but 2%, not 0% — and the reason is evidence, not caution** | `RCON2746` is **step-prone**: REGINALD's detector fires on 17 of 154 cohort transitions (11.0%, 9 up / 8 down ⇒ **~5.8%/quarter for an UP-step**), and **WAL owns the cohort's two largest, both UP** (2024Q1 +64.8%, 2024Q4 +27.2%). **From 21.20%, ANY qualifying up-step crosses the trigger** — the minimum +25% lands at 26.50%, WAL's own two would land at 26.97% and 34.94%. So the path is live and base-rateable. 2% ≈ that ~5.8% quarterly step probability discounted by the two further conditions the *scenario* needs: that the step be **economically real rather than a memo-designation change** (REGINALD's OZK work shows it can be the latter), and that it then **transmit to a $52-62 stock**. **Zeroing it would assert the trigger can never fire, which is stronger than the evidence.** |
| **Base 40% → 45% (+5)** | The disconfirmation is **positive information about the risk profile**, not merely absent bad news: the hidden-CRE concentration the bear premised is **not there at the scale claimed**, and on the legitimate cross-bank basis (v1a) the `>20%` screen catches **nobody** in a 14-bank cohort. That supports the *compounder proceeding normally*, which is Base. Base takes the larger share because MI3 speaks to **risk**, not to upside catalysts. |
| **Bull 27% → 30% (+3)** | Smaller share, deliberately. MI3 says nothing about the bull's own drivers (buyback execution, the raised NII floor, the capital-return pivot). It raises the odds those plans run **without a credit interruption** — real, but second-order. |
| **Bear-medium 16% → UNCHANGED** | ⛔ **Deliberate, and the most important thing this re-mark does NOT do.** P7's scope is bear-fast's 10%. **The freed weight must not be laundered into the other bear** — bear-medium's own mechanism (office migration in the **secured** book) got no new evidence this cycle, and moving weight there would let a dead mechanism's probability survive under a live mechanism's name. Its evidence is unchanged, so its weight is unchanged. |
| **Tail 7% → UNCHANGED** | No new Cantor or LAM/Jefferies datum. The counterclaim remains secondary-sourced and uncorroborated by any filing (P4 rejected the trigger, not the risk). |

### ⚠️ Scope fence carried verbatim into the re-mark: **V1a ≠ V1**
MI3 measures CRE-purpose lending **NOT SECURED by real estate**. **The office book, the $99M life-science credit, the classified balance and the pending appraisal are a DIFFERENT OBJECT and are untouched by this disconfirmation.** This is the single most likely mis-consumption of v2.4 — **the bear did not get smaller because the office risk got smaller; it got smaller because a *different, adjacent* mechanism was measured and found absent.** Bear-medium sitting unchanged at 16% is that fence expressed as a number.

### The offsets I am NOT dropping (they cut against this re-mark)
1. **MI3 DOLLARS are rising, +14% YoY ($2,246M → $2,555M).** The ratio fell only because item 4 grew faster. A ratio plateau is not a shrinking hidden-CRE book.
2. **NEW 2026-08-20 — the NDFI book is $15.81B (24.1% of loans) and carries $122.5M of NONACCRUAL** [REGINALD, FFIEC CDR primary, RSSD 3138146, `RCONPV25`, 6/30/26]. In a 26-bank sample including JPM/BAC/WFC, **only WFC carries more NDFI nonaccrual in absolute dollars**, on a book ~14× larger. **Deliberately NOT weight-moving**, on the publisher's own four caveats: one quarter (no trajectory), no peer baseline, the tape does not sort on it (ρ −0.255 / −0.063 at n=26, inside noise), and 68.9% of the book is mortgage warehouse where losses run near zero. **Logged as a datum, and as the highest-value next pull** (≥4 quarters before any direction is read).
3. **A 60% prediction (REG-15) just resolved FAILED** on this same series. The instrument that killed bear-fast also says my predecessor's confidence on this vector was badly calibrated — in the *same* direction I am now moving. That is consistent, not corroborating.

### PT range — convention held, and its tension flagged rather than quietly fixed
**PT $52-76** (was $52-74). Convention **PINNED and unchanged**: PT = [Bear-fast range low, EV] → [$52, $75.96].
⚠️ **The convention is now strained and I am NOT fixing it in this edit.** It anchors the PT floor on a scenario I just cut to **2%**, so the published floor is set by a 1-in-50 outcome. Changing a pinned convention in the same edit that moves a weight is exactly what rider R3 forbids. **Registered as an open spec question for a later dated edit** — candidate replacement: anchor the floor on the probability-weighted bear (fast+medium) rather than on bear-fast's tail.

### What v2.4 does NOT do
- **Does NOT touch ranges.** No range moved. The re-mark is probabilities only — there was no new *earnings-base* information, which is the standard v2.3 set for a range edit.
- **Does NOT move bear-medium, Tail, or any confidence on WAL-01/WAL-02.** Those confidences were re-marked by Stage-2 on 7/22 and are untouched here.
- **Does NOT change position posture.** No trade recommendation. TERRY + Will [Approve] + live chain.
- **Does NOT re-open the $99M appraisal, which remains the most-dated open catalyst with no carrying instrument until the Q3 deck.**

---

## EXPECTED VALUE SUMMARY (v2.3 — post-Q2, multi-quarter unconditional) — 🧊 SUPERSEDED 2026-08-20 by v2.4, preserved as the audit trail

**Trigger:** the WAL Q2 print (7/21 AMC + 7/22 call), graded in two stages → `../REGINALD/reports/2026-07-21_WAL_Q2_grade.md` + `../REGINALD/reports/2026-07-22_WAL_Q2_stage2_grade.md`. **Verdict was NOT-surprise-tier / NO FIRE**, so this re-mark moves weight OFF the bear and ONTO base/bull. Direction is bear-unfavourable and stated as such.

| Scenario | v2.2.1 Prob | **v2.3 Prob** | Δ | v2.2.1 Range | **v2.3 Range** | Midpoint | Weighted |
|----------|------------|--------------|----|-------------|---------------|----------|----------|
| Bear-fast (V1 MI3 ≥25 trigger) | 12% | **10%** | −2 | $52-62 | $52-62 *(unch)* | $57.00 | $5.70 |
| Bear-medium (V1 Office migration) | 25% | **16%** | **−9** | $58-66 | $58-66 *(unch)* | $62.00 | $9.92 |
| Base | 35% | **40%** | +5 | $70-77 | **$74-82** | $78.00 | $31.20 |
| Bull | 21% | **27%** | +6 | $82-90 | **$86-94** | $90.00 | $24.30 |
| Tail | 7% | **7%** | 0 | $35-45 | $35-45 *(unch)* | $40.00 | $2.80 |
| **Expected Value** | **$68.93** | **100%** | | | | | **$73.92** |

**Overvaluation (÷EV convention, pinned):** (83.11 − 73.92) / 73.92 = **12.4%**.
**★ The honest read — the margin of safety COMPRESSED.** At 7/17 spot $81.88 vs EV $68.93 the gap was **18.8%**; it is now **12.4%**. That is not price action — **EV rose $4.99 (+7.2%) while price rose only $1.23 (+1.5%)**. The narrowing is driven by my own re-weight in response to a non-confirming print, which is the correct direction. WAL remains overvalued against my EV, but by materially less, and the Sep $67.5P/$70P core is now further from an EV-justified strike than it was pre-print.

### Re-weight rationale (v2.2.1 → v2.3) — each line tied to a graded Q2 fact

| Shift | Driver (all from the two graded stages) |
|---|---|
| **Bear-medium 25% → 16%** (the big cut) | The migration-broadening mechanism took the most direct hit available: **REG-26 RESOLVED-DISCONFIRMED**; the $99M life-sci loan went to **nonaccrual with $0 charged off** and the borrower **brought it CURRENT end-June** with a prospective tenant; **0 new office migrations** (§3, N stays 1); **office classified $316M vs the $407M baseline**, visual-confirmed off EX-99.2 slide-12; **SM −$87M (−22%) to $316M**. REG-24 65→25%, REG-25 72→50%. **NOT cut to zero** — the appraisal is still not in (the dated Q3 catalyst that could force a charge-down), ACL/NPL coverage sits at **96%** (<100%), and CRE-NOO gross C/O hit a 5-quarter high $32.0M. Grind INTACT-but-NARROWED. |
| Bear-fast 12% → 10% | No new information — **MI3/FFIEC PDD still has not run** (~2.5 months overdue; DEWEY 7/16 confirmed MI3 is not a 10-Q line, so only FFIEC resolves it). Trimmed 2pp not on evidence but on **two consecutive quarters of a SHRINKING office/CRE book with no confirmation** — time without confirmation is weak evidence against a scale story. Mechanism itself untouched. |
| Base 35% → 40% | The print landed base-case: EPS **$2.36** beat ($2.33 cons), **NIM 3.53% flat**, credit in-guide (ex-fraud NCO **37bps**, inside the 25-40 NEUTRAL band), AOCI −$451M **improved +$5M QoQ**, CET1 11.0%. |
| Bull 21% → 27% | Genuine bull strengthening, not tape: **capital-return pivot** ($5B loan guide CUT explicitly "to prioritize share repurchases" + **$150M H2 buyback**), **NII floor RAISED to 12-14% while absorbing an assumed Sept 25bp HIKE** (my own higher-for-longer leg is now inside WAL's guide), management "C/O peaked" + an H2 NPL-decline path with 3-4 of the Investor-Day six resolving in Q3, and spot deposit-cost **inflecting down** (Q2 avg 1.78%, −3bps; June exit 1-2bps BELOW avg). |
| Tail 7% → 7% | Untouched. Cantor drew **zero call mentions** and produced no new Q2 charge-off; the LAM/Jefferies rail is live litigation but produced no Q2 datum. |

### ★ Range edits — the justification is fundamental, NOT spot-chasing (stated explicitly because the temptation is obvious)
Ranges were held flat from v2.1→v2.2.1 on the principle "no structural vector change drives range edits." **Q2 supplied two genuine earnings-base changes**, so Base and Bull lift — but deliberately **not all the way to spot** ($83.11 sits above the new Base range top of $82, i.e. my base case still implies a decline):
- **Up:** NII guide floor raised to 12-14% growth *while absorbing a Sept hike* (higher earnings base, not a one-off) + $150M H2 buyback with the loan guide cut to fund it (fewer shares, and a stated per-share-over-growth priority).
- **Down (the offsets I am NOT ignoring):** fee guide **CUT** 20-25% → 13-17%; deposit guide **CUT** $8B → $6B; ACL/NPL coverage **<100%**.
- Net: Base midpoint $73.50 → $78.00 (+6.1%); Bull midpoint $86.00 → $90.00 (+4.7%). **Bear and Tail ranges unchanged** — their mechanisms are untouched, only their probabilities moved.

### PT range — convention PINNED to stop the drift
**PT $52-74** (was $50-68). **Convention, now explicit: PT = [Bear-fast range low, EV].** Prior versions drifted because the convention was never written down ($52-70 → $50-68 with no stated rule). Bear-fast low $52 · EV $73.92 → **$52-74**.

### What v2.3 does NOT do
- **Does NOT rebuild the strike-by-strike position architecture.** Reserved for the `AGENTS/WAL/` standup (PROME WP-W2). Position truth stays `POSITIONS.md`.
- **Does NOT touch `INDEX.md` or `WEAKNESSES.md`** — both fold into the WP-W2 standup by explicit sequencing instruction (Will/PROME 7/25, DAEDALUS 7/22 ruling #5). **They therefore still carry v2.2.1 / EV $68.93 / PT $50-68 — a KNOWN, DOCUMENTED divergence, not silent rot.** See CHANGELOG for the handoff list.
- **Does NOT re-open the cohort question.** Hyp A (genuine cohort improvement) stands and was **re-confirmed twice more** since: WALTER's SIG-723-016 Q2 mosaic (cohort improving with fat idiosyncratic tails) and my own 7/25 FL small-tier watch-card fill (3-of-3 REVERT → creep does not broaden).
- **Does NOT change position posture.** No trade recommendation here; any action needs TERRY + Will [Approve] + a live chain (rule #4/#5).

---

## EXPECTED VALUE SUMMARY (v2.2.1 — SUPERSEDED 2026-07-25, preserved as audit trail)

| Scenario | v2.1 Prob | v2.2 Prob | **v2.2.1 Prob** | v2.2 Range | **v2.2.1 Range** | Midpoint | Weighted |
|----------|-----------|-----------|------------------|------------|------------------|----------|----------|
| Bear-fast (V1 MI3 ≥25 trigger) | 12% | 12% | **12%** | $52-62 | $52-62 | $57.00 | $6.84 |
| Bear-medium (V1 Office migration) | 23% | 30% | **25%** | $58-66 | $58-66 | $62.00 | $15.50 |
| Base | 35% | 33% | **35%** | $70-77 | $70-77 | $73.50 | $25.73 |
| Bull | 23% | 18% | **21%** | $82-90 | $82-90 | $86.00 | $18.06 |
| Tail | 7% | 7% | **7%** | $35-45 | $35-45 | $40.00 | $2.80 |
| **Expected Value** | | | **100%** | | | | **$68.93** |

**Overvaluation (÷EV convention): (80.15 − 68.93) / 68.93 = 16.3% [STALE spot — at $81.88 (7/17) it is ~18.8%].** v2.2 at $77.63 to EV $67.98 was **14.2%** on the same convention. **Gap WIDENED ~2pp** because price rose $2.52 (+3.2%) while EV only rose $0.95 (+1.4%). Directionally **bear-supportive** (more room to fall, even after Bear-medium trim).

### Re-weight rationale (v2.2 → v2.2.1)

| Shift | Driver |
|---|---|
| Bear-medium 30% → 25% | Macro-NIM-tailwind double-stack (5/20 20Y clean auction + 5/22 Waller pivot) softens loss-absorption channel — higher PPE absorbs same B1-class losses without stock-breaking event. **Cut rests on loss-absorption ONLY**; recognition-delay timing channel handled by existing Sep-dated tenor (Sep $77.5P / Sep $70P span Jul-21 Q2 print) — including timing in weight would double-count delay against positions already paid for the window. |
| Base 33% → 35% | Modest +2pp absorbing NII tailwind ("higher for longer" benefits variable-rate book) |
| Bull 18% → 21% | Compounder narrative modestly strengthens on Waller no-cut implication |
| Bear-fast / Tail unchanged | V1 MI3 mechanism + tail mechanics not affected by macro-NIM softening |
| **All ranges UNCHANGED** | No structural vector change drives range edits; B1 / V4 / V1 MI3 pending / leading-bucket migration all stand |

### What v2.2.1 does NOT do

- Does NOT reweight on cohort framing. **Cohort NCO decomposition RESOLVED 6/8 PM → Hypothesis A (genuine cohort improvement)** — ZION/CFG/MTB GENUINE, FITB confounded-excluded, EGBN cosmetic-outlier (see THESIS COHORT CONTEXT + `../REGINALD/research/COHORT_NCO_DECOMP_2026-06-08.md`). Bear-medium **stays 25, NO revert toward 30** (the revert was the Hyp B path, now closed); WAL bear narrows to idiosyncratic, "sharpen to WAL-specific" framing EARNED. Re-openable at Q2 (maturity wall).
- Does NOT change REG-24 or REG-25 confidence — single-credit mechanical math doesn't depend on NIM. *(Confidences at this writing 70/75; re-graded **65/72** on 7/16 — canonical `workbook/PREDICTIONS.tsv`.)*
- Does NOT change position posture. Sep core (**$67.5P / $70P** per `POSITIONS.md` — the "$77.5P Sep" originally written here was the mis-recorded Jun-18 position, see 7/17 banner) still positioned for Q2 print. Jun 18 cluster still requires its own decision (decision window ~6/11 — substance owed to PROME reply rests on this v2.2.1 framing).

### v2.2 unconditional table preserved as reference

| Scenario | v2.2 Prob | v2.2 Range | Midpoint | Weighted |
|----------|-----------|------------|----------|----------|
| Bear-fast (V1 MI3) | 12% | $52-62 | $57.00 | $6.84 |
| Bear-medium (V1 Office) | 30% | $58-66 | $62.00 | $18.60 |
| Base | 33% | $70-77 | $73.50 | $24.26 |
| Bull | 18% | $82-90 | $86.00 | $15.48 |
| Tail | 7% | $35-45 | $40.00 | $2.80 |
| **v2.2 EV** | | | | **$67.98** |

**At v2.2 spot $77.63 → 14.2% over** (÷EV convention; reported inconsistently as ~14% in 5/21 ship docs).

---

## EXPECTED VALUE SUMMARY (v2.2 — multi-quarter unconditional, superseded)

| Scenario | v2.0 Prob | v2.1 Prob | **v2.2 Prob** | v2.1 Range | **v2.2 Range** | Midpoint | Weighted |
|----------|-----------|-----------|---------------|------------|----------------|----------|----------|
| Bear-fast (V1 MI3 ≥25 trigger) | — | 12% | **12%** | $52-62 | $52-62 | $57.00 | $6.84 |
| Bear-medium (was Bear-slow) (V1 Office migration) | 30% | 23% | **30%** | $60-68 | $58-66 | $62.00 | $18.60 |
| Base | 38% | 35% | **33%** | $70-78 | $70-77 | $73.50 | $24.26 |
| Bull | 25% | 23% | **18%** | $84-92 | $82-90 | $86.00 | $15.48 |
| Tail | 7% | 7% | **7%** | $35-45 | $35-45 | $40.00 | $2.80 |
| **v2.2 Expected Value** | | | **100%** | | | | **$67.98** |

**At v2.2 ship (spot $77.63) → ~14% over vs v2.2 EV $67.98** — *superseded; live v2.2.1 figure is spot $80.15 / EV $68.93 / 16.3% over, see top of file* (v2.1 was $70.50 / 13% over at $81.90; v2.0 was $72.32 / 11% over). Drawdown -5.2% from v2.1 base offset by EV drift -$2.50 (Bear-medium reweight) — overvaluation% similar but bear scenarios more probable.

### Re-weight rationale (v2.1 → v2.2)

| Shift | Driver |
|---|---|
| Bear-slow → Bear-medium (23% → 30%) | B1 has fired via $99M life-science walk-away. Bear path is no longer "wait for multi-quarter migration" — first material migration already disclosed. Probability that price re-rates to $58-66 range over Q2-Q3 horizon increases materially. |
| Base 35% → 33% | Slow-grind base case retains weight but loses 2pp to bear-medium realization. |
| Bull 23% → 18% | $99M life-science walk-away + Curley resignation + ~10% drawdown materially erode the "largely behind us" mgmt narrative. Bull case still alive (TBV CAGR, deposits, Juris) but plausibility down 5pp. |
| Bear-medium range $60-68 → $58-66 | $2 floor compression — Q2 print is the second test; if it materializes, $58 is more reachable. Ceiling -$2 because Q1 already showed leading-bucket migration. |
| Bull range $84-92 → $82-90 | $2 compression on each end; mgmt-credibility flag (Curley + B1 disclosure timing) tightens upside. |
| Bear-fast / Tail unchanged | MI3 calibration table still governs Bear-fast (FFIEC PDD hasn't printed); Tail mechanics unchanged. |

### v2.1 unconditional table preserved as reference

| Scenario | v2.1 Prob | v2.1 Range | Midpoint | Weighted |
|----------|-----------|------------|----------|----------|
| Bear-fast (V1 MI3) | 12% | $52-62 | $57.00 | $6.84 |
| Bear-slow (V1 Office) | 23% | $60-68 | $64.00 | $14.72 |
| Base | 35% | $70-78 | $74.00 | $25.90 |
| Bull | 23% | $84-92 | $88.00 | $20.24 |
| Tail | 7% | $35-45 | $40.00 | $2.80 |
| **v2.1 EV** | | | | **$70.50** |

---

## EXPECTED VALUE SUMMARY (v2.1 — multi-quarter unconditional, superseded)

---

## EXPECTED VALUE SUMMARY (v2.1 — multi-quarter unconditional)

| Scenario | v1.0 Prob | v2.0 Prob | **v2.1 Prob** | v2.0 Range | **v2.1 Range** | Midpoint | Weighted |
|----------|-----------|-----------|---------------|------------|----------------|----------|----------|
| Bear-fast (V1 MI3) | — | — | **12%** | — | **$52-62** | $57.00 | $6.84 |
| Bear-slow (V1 Office migration) | 45% | 30% | **23%** | $58-68 | $60-68 | $64.00 | $14.72 |
| Base | 30% | 38% | **35%** | $70-78 | $70-78 | $74.00 | $25.90 |
| Bull | 20% | 25% | **23%** | $85-95 | $84-92 | $88.00 | $20.24 |
| Tail | 5% | 7% | **7%** | $35-45 | $35-45 | $40.00 | $2.80 |
| **Expected Value** | | | **100%** | | | | **$70.50** |

**Current $81.90 → implied ~14% overvaluation vs EV of $70.50** (v2.0 was $72.32 / 11% overvaluation; v1.0 was $57.10 / 18%). v2.1 widens overvaluation back partway as V1-fast sub-bear restored.

### Re-weight rationale (v2.0 → v2.1)

| Shift | Driver | RED ref |
|---|---|---|
| Bear split into fast (12%) + slow (23%) | V2.0 collapsed V1-fast into V1-slow when V2.0 demoted V1; V2.1 restores V1-fast as conditional sub-bear pending MI3 print ≥25% threshold. P(MI3 ≥25%) ≈ 40-50% given trajectory; P(V1-fast cycle if MI3 fires) ≈ 25-30% → 12% aggregate. | M2 ACCEPT |
| Bear-slow 30% → 23% | V2.0 30% had V1 fully demoted; V2.1 splits MI3-pending optionality out separately, leaving V1-Office-migration at 23% standalone | M2 ACCEPT |
| Base 38% → 35% | V2.0 over-allocated base on V1-demoted assumption; V2.1 returns 3pp to bear bucket | M5.4 ACCEPT |
| Bull 25% → 23% | V2.0 over-allocated bull partially on mgmt-framing absorption (M5.6); V2.1 applies counterparty-diligence discount; V2-resolution-driven bull premium stays but smaller | M5.3, M5.6 PARTIAL |
| Tail 7% → 7% (unchanged) | Tail rationale (additional LAM/Leucadia-credit, Apollo Atlas SP warehouse, Office maturity wall refi failure) unchanged | — |
| Bear-slow range $58-68 → $60-68 | $58 anchor tightened to $60 (V2.0 bear midpoint was $63; range was symmetric; v2.1 slightly tighter on slow-grind expected floor) | M1 PARTIAL DEFEND |
| Bull range $85-95 → $84-92 | V2.0 raised bull-PT $10/share; V2.1 partially walks back ($1 floor, $3 ceiling) consistent with M5.6 counterparty-diligence discount on mgmt forward-statements | M5.3 DEFEND-WITH-CAVEAT |

### v2.0 unconditional table preserved as reference

| Scenario | v2.0 Prob | v2.0 Range | Midpoint | Weighted |
|----------|-----------|------------|----------|----------|
| Bear | 30% | $58-68 | $63.00 | $18.90 |
| Base | 38% | $70-78 | $74.00 | $28.12 |
| Bull | 25% | $85-95 | $90.00 | $22.50 |
| Tail | 7% | $35-45 | $40.00 | $2.80 |
| **EV** | | | | **$72.32** |

---

## JUN-18-CONDITIONAL EV (v2.1 — added per RED M4 ACCEPT)

V2.0's EV table was multi-quarter unconditional, but applied to Jun 18 positions as if scenarios resolved by expiry. Per RED M4: bear-slow scenarios (V2.0 mechanics: "fires across Q2-Q3") and tail scenarios are multi-quarter; Jun 18 expiry is T+6 weeks from May 1. Mathematically incoherent to credit Jun 18 puts with full multi-quarter intrinsic.

**v2.1 Jun-18-conditional probability model:**

| Scenario | Unconditional Prob | P(price-by-Jun-18 \| scenario fires) | Jun-conditional weight |
|----------|--------------------|---------------------------------------|------------------------|
| Bear-fast (MI3 ≥25 triggers) | 12% | 60% (V1-fast cycle compressed; 10-Q Table 16 May 11-13 + MI3 May 14-16 + Investor Day May 12 all in Jun-window) | **7.2%** |
| Bear-slow (V1 Office) | 23% | 20% (Q2-Q3 migration; ~20% of multi-quarter bear-slow probability mass lands by Jun 18) | **4.6%** |
| Base (drift) | 35% | 100% (Base = drift; price IS at base by Jun) | **35.0%** |
| Bull (V2-resolution-driven) | 23% | 50% (Bull case half-realized by Jun via Investor Day mgmt-narrative) | **11.5%** |
| Tail (additional LAM/Leucadia credit) | 7% | 30% (event-driven via 10-Q Table 16 + Investor Day Q&A) | **2.1%** |
| **Stays-near-current ($82)** | (residual) | 100% by construction | **39.6%** |
| **Total** | | | **100%** |

**Stays-near-current** captures the probability mass where the scenario fires but the price hasn't moved by Jun 18 yet. This is the bucket V2.0's EV table implicitly assigned to bear-payout intrinsic, which was the M4 error.

### Jun-18-conditional EV by strike

| Position | Bear-fast ($57, 7.2%) | Bear-slow ($64, 4.6%) | Base ($74, 35%) | Bull ($88, 11.5%) | Tail ($40, 2.1%) | Stays ($82, 39.6%) | **Jun-EV** | V2.0 stated EV | Δ |
|----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **$85P Jun 18** | $28×7.2%=$2.02 | $21×4.6%=$0.97 | $11×35%=$3.85 | $0×11.5%=$0 | $45×2.1%=$0.95 | $3×39.6%=$1.19 | **$8.98** | $13.93 | **-36%** |
| **$65P Jun 18** | $8×7.2%=$0.58 | $1×4.6%=$0.05 | $0×35%=$0 | $0×11.5%=$0 | $25×2.1%=$0.53 | $0×39.6%=$0 | **$1.16** | $0.75 | +55% (V2.0 understated when MI3-optionality counted) |

**Two findings from Jun-conditional recalc:**
1. **V2.0 overstated $85P Jun EV by ~36%** ($13.93 → $8.98). Still positive EV; HOLD justified. Position is correctly understood as **event-driven hedge** for MI3 mid-May + 10-Q May 11-13 + Investor Day May 12, NOT multi-quarter bear vehicle.
2. **V2.0 understated $65P Jun EV by ~55%** ($0.75 → $1.16) once V1-fast MI3-optionality is properly counted. V2.0's "close-recommendation on EV $0.75" was based on the wrong reasoning. $65P Jun has embedded MI3-mid-May optionality that V2.0's V1-demoted framework didn't credit.

### Sep-18-conditional EV (for comparison)

Sep 18 captures Q2 print (Jul 21 AMC — corrected 2026-07-09; was ~Jul 30 est) + most of Q3 → ~70% of multi-quarter bear-slow probability mass + ~60% of tail probability mass.

| Position | Sep-conditional Bear-fast | Sep-conditional Bear-slow | Sep-conditional Tail | **Sep-EV** |
|----------|-----|-----|-----|-----|
| $77.5P Sep 18 | $20.5×9%=$1.85 | $13.5×16%=$2.16 | $37.5×4%=$1.50 + Stays/Base/Bull components | **~$8-10** (multi-quarter coherent) |
| $70P Sep 18 | $13×9%=$1.17 | $6×16%=$0.96 | $30×4%=$1.20 | **~$4-6** (timeline-coherent cheap tail) |
| $65P Sep 18 (if rolled) | $8×9%=$0.72 | $1×16%=$0.16 | $25×4%=$1.00 + drift | **~$2-3** (better risk-adj than Jun if Jun close-rec was right under V2.0; but Jun has MI3-optionality V2.0 missed) |

**Sep tenor matches the multi-quarter thesis timeline.** The $77.5P Sep + $70P Sep are the timeline-coherent core; Jun positions are event-driven hedges.

---

## SCENARIO A: BEAR CASE (30%, was 45%)

**v2.0 thesis:** Tail actualizes through one or more of three slow-grind paths. No single binary catalyst — instead, multi-quarter migration forces market re-rating.

**Three trigger paths (need at least one to fire to reach $58-68):**

**Path 1 — V1 Office classified migration (REG-24, 60% standalone):**
- Office classified migrates from $407M (Q1 26) to >$500M by Q3 2026
- $946M Office maturity wall hits in 2026; defensive 90% Suburban / 0% CBD geography helps but doesn't eliminate refi pressure
- Bridge loan structures force natural recognition pressure
- Driven by: CRE refi environment, regional commercial vacancy (Phoenix/Vegas), interest-rate trajectory

**Path 2 — V1 Leading-bucket pull-through (REG-25, 55% standalone):**
- 30-89d PD already +45% QoQ to $157M; Special Mention +24% QoQ to $403M
- Q1 ex-fraud NCO 39bps annualized — already ABOVE mgmt 25-35bps top of guide
- Q2 or Q3 NCO breaches 40bps ex-fraud → mgmt guide blown; analysts re-rate
- CRE-NOO charges $27.7M Q1 (largest in 5 quarters; $66M 5Q TTM = 64bps annualized)

**Path 3 — Additional LAM/Leucadia-era credit surfaces:**
- LAM operates multi-strategy funds; the Apr 21 disclosure was for a single fund credit
- 10-Q Table 16 (May 4-10) or Investor Day (May 12) Q&A may surface additional Jefferies-platform exposure
- If a second LAM credit lands at $50M+ scale → market questions inventory completeness; "largely behind us" mgmt frame breaks

**Mechanics (Bear):**
1. One of three paths fires across Q2-Q3 2026 (not single event)
2. Provision builds gradually; ex-fraud NCO climbs into 40-50bps range
3. Multiple compresses 1.33x → 0.95-1.05x TBV ($58-65)
4. EPS guide cut at Q2 or Q3
5. Analyst PT cuts cascade (current ~$85-90 consensus → $65-75)

**Valuation:**
- 0.95-1.05x TBV ($61.14): $58-64
- EPS $7.50-8.50 at 7-8x P/E: $52-68
- **Bear target: $58-68**

**Why 30% (was 45%):** V2 binary catalyst RESOLVED removed the "$100M+ surprise charge-off" path. Remaining slow-grind paths require multi-quarter migration. Each individually 55-60% probable, but probability of *forcing market re-rating to $58-68* is ~30-35% — market may absorb leading-bucket buildup without re-rating if mgmt holds NII narrative.

---

## SCENARIO B: BASE CASE (38%, was 30%)

**v2.0 thesis:** Multi-quarter grind — V1 sharpens slowly, V2 stays resolved, V3 stays disconfirmed at aggregate. Price drifts in $70-78 range, no acute catalyst either direction.

**Mechanics:**
1. Q2 print: NCO ex-fraud lands ~32-37bps (above guide midpoint, below 40bps trigger)
2. Office classified migrates $407M → $440-470M (visible deterioration but not REG-24 hit)
3. Cantor residual stays on book; no incremental specific reserve build
4. No First Brands or Tricolor disclosure forcing event
5. May 12 Investor Day delivers measured response — neither catalyst nor disconfirming
6. Stock drifts lower on multiple compression as analyst PTs reset to $75-80 range

**Valuation:**
- 1.10-1.25x TBV: $67-76
- EPS $7.00-7.80 at 9-10x P/E: $63-78
- **Base target: $70-78**

**Why probability up to 38%:** Most likely outcome given (a) V2 resolved removed binary downside catalyst, (b) deposit/NII strength provides operating cushion, (c) tail-risk thesis is multi-quarter so the *median* outcome is grind not crisis, (d) cohort 8/8 fade pattern suggests range-bound rather than directional moves.

---

## SCENARIO C: BULL CASE (25%, was 20%)

**v2.0 thesis:** "Largely behind us" narrative holds. V2 resolution sticks; V3 disconfirmation propagates to street consensus; deposits + Juris banking + variable-rate book drive multiple expansion.

**Mechanics:**
1. Q2 print: NCO ex-fraud back below 35bps; leading-bucket buildup partially reverses
2. No incremental fraud disclosures; sector-silence pattern holds
3. Office classified stays flat or improves; CMBS office DQ pulls back further
4. Investor Day May 12 delivers credible Office de-risking story (similar to EGBN strategic shift)
5. Juris banking continues outsized contribution (raised guide +20-25% non-interest income)
6. Cohort short-unwind on Q2 prints; WAL benefits as crowded-short positioning unwinds
7. NII guide held even sans rate cuts → variable-rate "higher for longer" plays as bull catalyst

**Valuation:**
- 1.40-1.55x TBV: $86-95
- EPS $8.50-9.50 at 9-11x P/E: $77-105
- **Bull target: $85-95**

**Exit signals (close puts):** NCO ex-fraud <30bps Q2 + Office classified flat or down + insider buying begins + 10-Q Table 16 shows no other LAM/Leucadia credits.

**Why probability up to 25%:** V3 directionally disconfirmed at aggregate is a real bull data point that the pre-print thesis didn't price. Slide 24 cohort-median NDFI + Lender Finance structurally protected + CLN pool shrinking removes a bear leg. Add deposit cohort lead + NIM expansion + Juris upside = legitimate multiple-expansion path.

---

## SCENARIO D: TAIL — CASCADING (7%, was 5%)

**v2.0 thesis:** Multiple paths fire simultaneously over 2-3 quarters. Compounding events overwhelm operating cushion.

**Mechanics:**
1. Q2 print: ex-fraud NCO breaches 45bps + Office classified jumps to $500M+
2. Within 2 quarters: additional LAM/Leucadia credit emerges at $75-150M scale
3. CRE-NOO charges accelerate (current $27.7M Q1 → $40M+ trajectory)
4. Office maturity wall refi failures begin (some of $946M won't roll)
5. Apollo Atlas SP warehouse counterparty stress propagates to WAL warehouse book ($7.155B)
6. Capital raise considered at distressed pricing
7. Possible Q2/Q3 dividend cut or buyback suspension

**Valuation:**
- 0.65-0.75x TBV: $40-46
- Distressed peer comps (RF/CFG late-2008 pattern): $35-45
- **Tail target: $35-45**

**Why probability up to 7% (was 5%):** Three real tail levers identified post-print: (a) LAM/Leucadia credit inventory uncertain, (b) Office maturity wall is a hard 2026 calendar event, (c) Apollo Atlas SP warehouse linkage adds counterparty channel. Still low probability — mgmt cushion is substantial — but no longer dismissible.

---

## EPS SENSITIVITY (Refreshed)

WAL Q1 26 GAAP EPS $1.65 / Adjusted $2.22. FY 2025 EPS ~$8.73. Mgmt 2026 outlook held even sans rate cuts.

| Adjusted FY EPS | P/E 9x (consensus) | P/E 8x (cohort) | P/E 7x (stressed) |
|-----|-------------------|--------------------|--------------------|
| $9.50 (bull) | $86 | $76 | $67 |
| $8.50 (base hold) | $77 | $68 | $60 |
| $7.50 (mild compress) | $68 | $60 | $53 |
| $6.50 (REG-25 hits) | $59 | $52 | $46 |
| $5.50 (cascading) | $50 | $44 | $39 |

Bear case needs Adj EPS ~$7.00-7.50 at 8x → **$56-60**.
Tail case needs Adj EPS ~$5.00 at 7-8x → **$35-40**.

---

## PUT EXPECTED VALUE AT $81.22

### $85P Jun 18 (1 contract) — Slightly ITM
| Scenario | Prob | Stock | Intrinsic | Weighted |
|----------|------|-------|-----------|----------|
| Bear ($63) | 30% | $63 | $22.00 | $6.60 |
| Base ($74) | 38% | $74 | $11.00 | $4.18 |
| Bull ($90) | 25% | $90 | $0.00 | $0.00 |
| Tail ($40) | 7% | $40 | $45.00 | $3.15 |
| **EV** | | | | **$13.93** |

Position holds value across Bear and Tail. **Jun expiry is 7 weeks** — needs catalyst before then. Current intrinsic $3.78 only; ~$10/contract upside in EV vs intrinsic.

### $77.5P Sep 18 (1 contract) — Slightly OTM
| Scenario | Prob | Stock | Intrinsic | Weighted |
|----------|------|-------|-----------|----------|
| Bear ($63) | 30% | $63 | $14.50 | $4.35 |
| Base ($74) | 38% | $74 | $3.50 | $1.33 |
| Bull ($90) | 25% | $90 | $0.00 | $0.00 |
| Tail ($40) | 7% | $40 | $37.50 | $2.63 |
| **EV** | | | | **$8.31** |

Sep gives runway through Q2 print + Investor Day. **Best risk-adjusted core position** post-rewrite.

### $70P Sep 18 (1 contract) — OTM
| Scenario | Prob | Stock | Intrinsic | Weighted |
|----------|------|-------|-----------|----------|
| Bear ($63) | 30% | $63 | $7.00 | $2.10 |
| Base ($74) | 38% | $74 | $0.00 | $0.00 |
| Bull ($90) | 25% | $90 | $0.00 | $0.00 |
| Tail ($40) | 7% | $40 | $30.00 | $2.10 |
| **EV** | | | | **$4.20** |

Pays only in Bear or Tail. Lower premium than $77.5P; cheaper exposure to tail.

### $65P Jun 18 (1 contract) — Deep OTM, embedded MI3-mid-May optionality (v2.1 revision)

**v2.0 EV table preserved as reference:**

| Scenario | Prob | Stock by Jun | Intrinsic | Weighted |
|----------|------|-------------|-----------|----------|
| Bear ($63 by Jul) — partial by Jun | 15% | $72 | $0.00 | $0.00 |
| Base | 38% | $76 | $0.00 | $0.00 |
| Bull | 25% | $84 | $0.00 | $0.00 |
| Tail (rapid by Jun) | 5% | $50 | $15.00 | $0.75 |
| Status quo | 17% | $80 | $0.00 | $0.00 |
| **v2.0 EV** | | | | **~$0.75** |

**v2.1 Jun-conditional EV recalc** (V1-fast MI3-optionality properly counted per RED M2 ACCEPT):

| Scenario | Jun-conditional weight | Stock by Jun | Intrinsic | Weighted |
|----------|------------------------|--------------|-----------|----------|
| Bear-fast (MI3 ≥25 triggers V1-fast) | 7.2% | $57 | $8.00 | $0.58 |
| Bear-slow (V1 Office, partial by Jun) | 4.6% | $64 | $1.00 | $0.05 |
| Base | 35% | $74 | $0.00 | $0.00 |
| Bull | 11.5% | $88 | $0.00 | $0.00 |
| Tail (rapid by Jun) | 2.1% | $40 | $25.00 | $0.53 |
| Stays-near-current | 39.6% | $82 | $0.00 | $0.00 |
| **v2.1 EV** | | | | **~$1.16** |

V2.0 understated this position by ~55% because V2.0's framework had demoted V1 — which meant the MI3-mid-May trigger probability was implicitly zero in V2.0's EV model. V2.1 with V1 weight restored recognizes the embedded MI3 optionality. **Position is event-driven hedge for MI3 mid-May, not multi-quarter bear vehicle.**

**v2.1 recommendation:** HOLD-or-ROLL-TO-SEP. Close-recommendation WITHDRAWN per RED M4 ACCEPT.

---

## POSITION-LEVEL READ (v2.2 — post 10-Q drill)

| Position | Direction (5/21 spot $77.63) | v2.1 Recommendation | **v2.2 Recommendation** |
|---|---|---|---|
| $85P Jun | $7.37 ITM | HOLD as event-driven hedge | **HOLD as event-driven hedge.** Most v2.2 evidence (B1 fire, Curley) ALREADY in tape via 5/11-5/15 drawdown. Q2 print is post-Jun expiry; Jun catalysts now slimmer (only FFIEC PDD if integrated; AOCI rule comment close Jun 18). |
| ~~$77.5P Sep~~ [PHANTOM — was Jun-18, cleared; see 7/17 banner] | ~ATM (slightly OTM) | HOLD — timeline-coherent core | **REINFORCED-HOLD core.** Sep window catches Q2 print (Tue Jul 21 AMC) — this is where v2.2's $99M materializes as charge-off + REG-25 hit. Single best risk-adj position. |
| $70P Sep | 9.8% OTM | HOLD — timeline-coherent cheap tail | **REINFORCED-HOLD.** Same Q2 print thesis; cheaper exposure to bear-medium midpoint $62. Pays on bear-medium / bear-fast / tail. |
| $65P Jun | Deep OTM | HOLD or ROLL TO SEP (MI3 optionality) | **HOLD-to-expiry as cheap lottery.** v2.2 doesn't change the underlying math; MI3 optionality still embedded if FFIEC PDD integrates pre-expiry. Jun expiry post-Curley/post-10Q digestion = limited upside outside MI3 surprise. |
| $67.5P Jun | Deep OTM | (added 5/8 broker refresh) | **HOLD as Jun expiry tactical** — same window as $65P/$85P; layered strike coverage. |
| $77.5P Jun | (added 5/8 broker refresh) | (added 5/8 broker refresh) | **HOLD.** Jun expiry. Strike near current — most leveraged Jun position to any near-term move. |
| $65P Jul | (added 5/8 broker refresh) | (added 5/8 broker refresh) | ~~HOLD~~ **EXPIRED 7/17** (lapsed OTM at $81.88 per dashboard; broker-confirm owed). Never caught the print (Jul 21 AMC). |
| $67.5P Sep | (added 5/8 broker refresh) | (added 5/8 broker refresh) | **REINFORCED-HOLD.** Sep tenor; deeper OTM than $77.5P/$70P; cheaper tail leg of the Sep core. |

**Will-decision pending:** Roll-to-Sep-$65P cost analysis (need broker quote on Jun-65P-bid vs Sep-65P-ask). Out-of-scope this session; flagged for Jun T-7 close window (~Jun 11) at latest. Default if no decision by Jun 11: HOLD $65P Jun through expiry on MI3-optionality. If MI3 ≥25% (mid-May): $65P Jun reactivates as core position.

**Decision discipline:** the V2.1 framing means the Jun cluster gets revisited after MI3 prints (May 14-16). Three branches:
1. **MI3 ≥25%:** V1-fast confirmed; $65P Jun moves from optionality to core; potential to add or hold without anxiety
2. **MI3 24.0-24.9%:** V2.1 stands; HOLD or roll-to-Sep per cost
3. **MI3 <24%:** V1 plateaued; V2.0's V1-demotion retrospectively justified; close $65P Jun (deferred-V2.0 close-rec becomes legitimate post-test)

---

## WHY MARKET IS (STILL) MISPRICING — v2.0

Pre-print mispricing reasons that remain:
1. **MI3 reclassification not in sellside coverage** — Q1 Call Report (May 1-10) is forcing function
2. **Office single-point concentration not modeled** — Slide 12's 38% / 9.5x disproportion is buried
3. **Leading-vs-lagging divergence ignored** — analysts focused on improving classified/nonaccrual, missing PD-30-89 +45% QoQ
4. **Office maturity wall ($946M in 2026) not in PT models** — bridge structure means recognition is calendar-driven not market-driven
5. **Apollo Atlas SP warehouse linkage** ($7.155B WAL warehouse to non-bank servicers stressed at Apollo) underanalyzed

Pre-print reasons that no longer apply post-Apr 21:
- ~~Cantor under-provisioning~~ — RESOLVED (charge taken; mgmt asserted reserve "validated by appraisals")
- ~~Jefferies/PC contagion as bear thesis~~ — V2 already realized via LAM
- ~~SSFA $1.1B capital gap~~ — V3 disconfirmed at aggregate; CLN pool shrinking, not expanding
- ~~Convergence Day repeat~~ — pure-vulnerability premium burned off in 9-month tape

The remaining mispricing is **structural CRE tail-risk concentration**, not **fast-transmission failure**. Different thesis, different timeline.

---

## WHAT WOULD CHANGE THE WEIGHTING

**Push Bear higher (toward 40-50%):**
- Q2 NCO ex-fraud > 45bps
- Office classified > $500M Q2 (early REG-24 hit)
- Additional LAM/Leucadia credit ≥ $75M emerges
- 10-Q Table 16 shows multiple Jefferies-platform credits

**Push Bull higher (toward 35%+):**
- Q2 NCO ex-fraud < 30bps
- Office classified flat or down Q2
- Insider buying begins
- Investor Day delivers credible Office de-risking story

**Push Tail higher (toward 12-15%):**
- Two of the bear triggers fire same quarter
- Apollo Atlas SP warehouse counterparty default emerges at PFSI/LDI
- Office maturity wall refi failure becomes visible Q2/Q3

---

*KB evidence: 105 rows | Master thesis: `THESIS.md` v2.2.1 | Changelog: `CHANGELOG.md` | Weaknesses: `WEAKNESSES.md` | Q1 analysis: `Q1_2026_ANALYSIS.md` | Round 2 deck/press detail: `sources/q1_2026/` | 10-Q drill: `../REGINALD/research/WAL_10Q_DRILL_2026-05-21.md`*
