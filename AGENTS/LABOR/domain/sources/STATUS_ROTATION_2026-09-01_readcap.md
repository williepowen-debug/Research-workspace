# LABOR — STATUS hot/cold rotation, 2026-09-01

**Rotated by:** LABOR, session 2026-09-01 ~21:0x ET (PROME-spawned, WQ-146).
**Why:** `read_cap_check.py` returned 🔴 **58,936 B = 109% of the 54,250 B cap — OVER THE CAP, cannot be read whole.** The session's own JOLTS/ISM write-back is what pushed it over. Remedy per the tool: hot/cold split, owner's choice of WHAT. ⛔ **The budget was NOT raised — the read cap is not ours to move.**

**Selection rule applied:** only blocks that are (a) dated-historical or consumed derivation, AND (b) whose *live rule* is retained in `STATUS.md`. Every live figure, threshold, band and pre-commitment stayed in the hot file. **Cite this file as history; `STATUS.md` is canonical for every live figure.**

---

## ① FED TRAP & THESIS — retired rate-path annotations + the 8/7 policy grade (STATUS L120–137)

> **Retained hot in STATUS:** the standing rule — *labor is a SATISFIED SIDE-CONSTRAINT, not a policy input; a benign claims print is not hawkish fuel, it is nothing* — plus the asymmetry note and the ⛔ routing of all rate-path questions to BOND/HENRY/ORACLE.

> 🔴 **BOTH RATE-PATH FIGURES THAT USED TO SIT ON THIS LINE ARE RETIRED (2026-08-12) — and LABOR is not replacing them with fresher ones.** This line, and lines below, carried *"Sept-hike >80%, Fed-hike-2026 71.5%"* **in the present …
> **① `Fed-hike-2026 71.5%` — SUPERSEDED, owner-corrected.** ORACLE re-pinned the **same contract** (Polymarket `fed-rate-hike-in-2026`, $7.30M vol / $241.6K liq — deep, not a thin book) at **54.5% [2026-08-12T16:43Z]**, **−17.0pp**. …  *[carried: −23]*
> **② `Sept-hike 52% → >80%` — RETIRED LOUDLY. …
> ⛔ **DO NOT net ORACLE's September legs against the retired >80% — different instruments, and possibly different objects.** ORACLE's own warning, adopted verbatim: *"If your >80% traces to CME FedWatch or a conditional basis, the …
> **Owner-side note, recorded because it is the reusable half:** ORACLE published corrections on 7/31 (66.5%) and 8/9 (54.5%) and **LABOR was on neither route** — *"the measurement existed for eleven days; the routing did not"* (his …

> **⚠️ REGIME FOLD 7/24 (NEXUS routing, folded same-session per the deferred-fold rule):** the "hold off on hiking" framing above is the **7/2 tape** and is now superseded. …
> ⚠️ **This 7/24 fold is dated-historical and is being ANNOTATED, not rewritten** — the numbers are struck through so the record of what I …
> 🔴 **THE CORRECTION (2026-07-31, graded off the 7/29 statement + presser):** **there is no labor-tightness premise underneath this hike case.** Warsh's reaction function, stated in his own words: *"Any central bank, especially a …
> **Labor is a SATISFIED SIDE-CONSTRAINT, not a policy input.** Its job is to be *quiet*, not to be *tight*. So: **a benign claims print is not hawkish fuel — it is nothing.** It confirms the constraint holds and the Committee moves on to prices.
> ⚠️ **The asymmetry, and it cuts against this book: the bar for labor data to move policy just went UP, not down.** A low claims print doesn't feed the hike; a mildly soft one doesn't restrain it either. …
> 🔴 **8/7 — GRADING THE ONE POLICY QUESTION THAT IS MINE, AND NOTHING ELSE.**
> **The question, scoped narrowly: does the July print clear the raised side-constraint bar?** The 7/29 grade established that labor is a …
> **My grade: this is the first print of the cycle that plausibly clears the bar, and it is not yet sufficient. PROVISIONAL until the ~Aug 19 minutes.**
> **For:** a **negative headline** with **−103K** of revisions behind it is a different object from the marginal wiggles I called policy-irrelevant. …  *[carried: 4.1% · +20K]*
> 🚫 **WHAT THIS PRINT DOES TO RATE EXPECTATIONS, THE SEPTEMBER HIKE PATH, OR ANY MARKET REPRICING IS NOT MY CALL AND I AM NOT MAKING IT.** That question routes to **BOND, HENRY and ORACLE** and was sent to HENRY 8/7. …  *[carried: 4.1% · 4%]*
> **Consequence for the ECI Q2 finding (same-day, uncomfortable):** the 7/31 ECI work was framed as undercutting *"the labor-tightness premise underneath a hike."* **That premise does not exist, so ECI cannot undercut it.** The …  *[carried: 4%]*


---

## ② EXIT RULES — freeze-thaw v2 base-rate derivation (STATUS L191–204)

> **Retained hot in STATUS:** the live v2 spec (LEG A AND (LEG B OR LEG C)), the adopted-row base rates, and the refreshed live state.
> **Rotated here:** the four-spec comparison table, the *why v1 was broken* prose, the rejection of BD-11's own preferred fix, the design notes, and the struck v1 text. **BD-11 is discharged; this is consumed derivation.**


  **Base-rated JOINTLY before adoption — which the original spec never was, and which BD-11 named as the actual root cause.** Monthly obs, FRED primary (PAYEMS/EMRATIO/CIVPART/JTSHIL/JTSTSL):

  | Spec | Base rate 2015+ | **Genuine expansion '15–'19** | **The freeze '25–'26** | Verdict |
  |---|---|---|---|---|
  | **v1 as written** (NFP≥150 ×2 · LFPR≥1m · gross hires >5.5M) | 23.9% | **6.7%** | 0.0% | ❌ **barely fires even when the thesis IS wrong** |
  | BD-11's own preferred fix (any-2-of-3, gross hires >5.3M) | 67.6% | 73.3% | **5.3% — FIRED Apr-2025** | ❌ **rejected, see below** |
  | all-3 with gross hires >5.3M | 28.8% | 18.3% | 0.0% | ❌ still leg-3-bound |
  | **v2 ADOPTED** (A AND (B OR C)) | 58.7% | **65.0%** | **0.0%** | ✅ |

  🔴 **Why v1 was actually broken — and it is NOT the reason I logged on 7/31.** I logged "lags a month by construction." The **measured** defect is worse: v1 fires in only **6.7% of months during a genuine 2015-19 expansion.** Leg …
  🔴 **BD-11's own recommended fix is REJECTED on the evidence.** A week ago I wrote *"prefer (c) any-2-of-3 combined with (b) leg 3 → ~5.3M."* Measured: **67.6% base rate, and it WOULD HAVE FIRED IN APRIL 2025 — inside the freeze …  *[carried: 4%]*
  🔴 **The measurement fix, which is the substantive change: LEG C is now JOLTS *NET*, not gross hires.** **Gross hires cannot speak to net employment**, and right now it actively misleads: **June hires +96K to 5,348K — but …
  **Design notes, stated so the next reader does not re-derive them.** (a) **Leg A is MANDATORY by construction, so the gate cannot fire without the realized net count confirming** — that is L-13's balance requirement enforced …  *[carried: −23]*

---

## ③ MONITORING CALENDAR — graded rows, Aug 2026 and earlier (7 rows)

> **Retained hot in STATUS:** the ✅ Sep 1 grade (this session) and the forward Sep 2 / Sep 4 rows. All grades below are also summarised in the DANGER WINDOW section.

| ✅ **Jun 30 – Aug 7 — ALL GRADED (historical rows collapsed 8/7; **2 more folded in 8/12** — the Aug 5-6 and Aug 7 rows duplicated the DANGER WINDOW row verbatim)** | ~40 prints: NFP Jun · JOLTS May+Jun · claims 7/9→8/1 · ISM Mfg+Svs · ECI Q2 · FOMC 7/29 · RHI/KFRC/MAN · FL UR · Challenger · ADP | **Terminal grades: LAB-02 ❌ · LAB-16 ✅ · LAB-17 ❌ (Brier 0.09) · LAB-06 ❌ (Brier 0.64) · LAB-13 ❌ (Brier 0.09)** · Kill A reset · T-11 not fired · … |  *[carried: Sep 4]*
| ✅ **Thu Aug 13, 8:30 ET — GRADED 8/20 (7d late)** | **Initial claims w/e Aug 8 = 212,000** (+ CC w/e Aug 1 = 1,781K) | 🔒 Graded band-by-band off `docket/graded/GRADING_CARD_20260813_claims.md` §8. **BAND C.** Band-E floor move did NOT execute. … |  *[carried: 0 of 5]*
| ✅ **Wed Aug 19, 14:00 ET — GRADED 8/20 (1d late)** | **July FOMC minutes** (meeting of 7/29) | 🔒 Graded off `docket/graded/FOMC_LABOR_LANGUAGE_20260819.md` §7. … |
| ✅ **Thu Aug 27, 8:30 ET — GRADED SAME DAY (10:31 ET)** | **Initial claims w/e Aug 22 = 203,000** (−4K; prior wk revised UP 206 → 207K; **4-wk MA 205,500**, +1,250) + **CC w/e Aug 15 = 1,778K** (−18K; w/e Aug 8 revised DOWN 1,799 → 1,796K) | 🔒 **Graded off the bands pre-committed in `CATALYSTS.tsv` — NO BAND, NO ACTION.** >300K / 251–300K / 230–250K / ≤185K all un-hit. … |  *[carried: 44,500 · 97K · 0 of 5]*
| ✅ **Fri Aug 28, 10:00 ET — GRADED SAME MORNING** | **Jackson Hole — Warsh data-task-force watch** 🔒 **CLOSES UNINFORMATIVE — the third state, pre-committed 8/23 before the event, fires exactly as … | 🔒 **Branch-(c) term test, the SAME instrument used on the 8/19 minutes so the two are comparable: `data quality` 0 · `response rate` 0 · `benchmark` 0 · `QCEW` 0 · `revision` 0 · `BLS`/`Bureau of Labor … |  *[carried: −79,000]*
| ✅ **Fri Aug 21 — RESOLVED, no action was owed** | **KELYA options expiry** | **KELYA 7.5P = LAPSE**, ruled by **Will 2026-08-20 S1** as part of a 5/5 decision-free OPEX cluster (PROME HANDOFF 8/20-S1 / SCRATCH operator card, relayed 8/20). … |
| ✅ **Aug 28 (Fri), 10:00 ET — GRADED SAME MORNING, off frozen text** | **QCEW preliminary benchmark** | 🔒 **BAND E. Total nonfarm −79,000 · total private −178,000 · government +99,000** [CONF **BLS USDL-26-1425**, `prebmk.nr0.htm` + `prebmk.t01.htm`, retrieved 10:33 ET 2026-08-28]. … |79K| < 300K ⇒ Band E, not a boundary call.** Executed: **vector 8 4 → 2**, **LAB-08 live 15% → 4%** (as-made 65% for scoring). … |  *[carried: 158,650 · 157,751 · 0.61 · 0.95]*

---

## ④ PREDICTIONS — the 2026-08-07 C2-0 worked sweep block (STATUS L161–164)

> ⚠️ **Rotated for a second reason beyond bytes.** C2-0's own text warns: *"A sweep whose worked example is a stale list teaches the reader the answer instead of the procedure, and this is a boot-loaded file."* This block named LAB-08 and LAB-10 as the flagged rows; **both have since moved** (LAB-10 RESOLVED, LAB-08 repriced below the 60% bar). It was becoming the exact defect C2-0 was built to prevent. **STATUS now carries the 2026-09-01 re-run instead.**


> 🔴 **C2-0 STALE-HIGH-CONFIDENCE SWEEP — RUN 2026-08-07** (the control bought by LAB-06's 0.64). Gates #3/#5/#12/#13 applied to every OPEN row ≥60% whose confidence has not moved in 60+ days:
> - ✅ **LAB-08 — SWEEP DISCHARGED 2026-08-07, and it was the sweep working as designed.** Flagged 8/5 and 8/7 as a stale ≥60% threshold row untouched since February. …  *[carried: 65%]*
> - ✅ **LAB-10 — RESOLVED 2026-08-07, and the three-session flag was misdiagnosed by me each time.** I read it as a grading backlog; it was a **resolvability defect** — the prediction named no cohort and no measure, so it was never …
