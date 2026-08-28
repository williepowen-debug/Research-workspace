# FABN peer canary — 6/30 holder-side rerun (3 defects fixed) · and AG 55 re-based at NAIC primary

**SHADE · 2026-08-28** · PROME round-2 priorities 3 and 4.

---

## PART 1 — NPORT-P rerun, with the three DAEDALUS SFG defects fixed

**Script:** `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py` (fixed in place, fixes commented against the sweep).
**Artifacts:** `research/FABN_PEER_SPREAD_NPORT_RERUN_2026-08-28.json` + `.log`. ⚠️ **The script's own output filename was the 7/27 vintage — an 8/28 result under a 7/27 name is a staleness trap, so both artifacts were renamed to the run date.**
**Source-mode: PROVISIONAL** per `CHECK_STANDARD.md` §8 — holder marks, not TRACE prints.

### The three fixes, and what each one caught

| # | Defect (DAEDALUS SFG sweep 2026-08-17) | Fix | **Did it catch anything?** |
|---|---|---|---|
| **1** | **Unstamped curve backfill.** The Treasury curve could come from up to 5 days prior, and the printed key was the **PERIOD**, never the curve's own date — `[5] curve 2026-06-30: {…}` rendered identically whether the values were from 6/30 or 6/25. The penalty inherited it silently. | Track `curve_asof[period]`; print the **as-of date, the lag in days, the tenor list, and an OK/refused verdict** beside the period. | ✅ **YES, on the first run.** `[5] period 2026-05-31 \| curve as-of 2026-05-29 (BACKFILLED 2d)`. **2026-05-31 was a Sunday** — there is no Treasury print, so every 5/31 spread in the 7/27 study was struck against a **5/29** curve and nothing said so. The 6/30 curve is **exact**. |
| **2** | **A partial curve defeated the emptiness test.** `if not curve[pe]` tested **EMPTY only** — if only DGS2 and DGS30 landed, the fallback never fired and `tsy()` interpolated a **7Y benchmark between the 2Y and the 30Y point.** | Replace the emptiness test with `MIN_TENORS = 5` **and** `REQUIRED_TENORS = (2, 5, 7, 10)`; on failure, retry the fallback and, if still short, **blank the curve so `tsy()` refuses to serve it**. Additionally `MAX_BRACKET = 5` years in `tsy()` — **never interpolate across a bracket wider than 5y**. | ⚪ **Not triggered this run** — both periods returned the full 7-tenor set. **The guard is now falsifiable and was exercised** (the OK verdict is printed, not assumed). |
| **3** | **Silent enumeration truncation.** §1's `if not raw: break` exited identically on a fetch failure and on "no more results", with **no count of lost pages**. §2 already printed an honest `{bad} fetch failures`; §1 did not. | Count `enum_truncated`, distinguish **EXHAUSTED** from **STOPPED EARLY**, print both, and add an explicit **"FILING SET IS INCOMPLETE — do not read counts as a population"** warning when pages are lost. | ✅ **Immediately useful.** The line now reads `123 filings \| enumeration STOPPED EARLY \| pages lost to failure: 0` — i.e. stopped at the `MAX_FILINGS` bound, **not** truncated by failure. Before, "123 filings" alone could not distinguish the two. |

**FIX 1b — found while COMMITTING the rerun, and it is the same defect one layer down.** Fix 1 stamped the **printed** curve; it did **not** persist `curve_asof` into the saved JSON — and `research/*.log` is **gitignored** (`.gitignore:39`), so the backfill provenance would have survived only in an uncommitted file. **A stamp that exists only in stdout is not a stamp.** The script now writes `curve_asof`, the enumeration `window`, and `enum_truncated`/`enum_exhausted` into the artifact; this run's JSON was stamped by hand from its own stdout with a `_provenance_note` saying so; and the log was renamed `..._RUNLOG.md` so it is committable.
⚠️ **Also caught at commit time: the rerun OVERWROTE the tracked 7/27 JSON**, because the script's output path was a constant. **Restored from git** — both vintages now coexist (7/27: periods 3/31·4/30·5/31, 51 matched funds, 427 rows · 8/28: periods 5/31·6/30, 53 matched funds, 449 rows). **A rerun that silently destroys its own comparator is a worse defect than any of the three DAEDALUS named.**

**Also parameterised:** the enumeration window was a hardcoded `2026-05-01..2026-07-27`. It is now `argv[2]/argv[3]`, so **a window is an explicit stamped input rather than a silent constant** — the same class as fix 1.

### Run statistics (2026-08-28, window 2026-07-01 → 2026-08-28)
**123 filings enumerated, 0 pages lost · 717 raw holdings, 0 fetch failures · 527 priced after dedup/sanity · 53 MATCHED funds (hold Athene AND ≥1 peer in the SAME filing), 492 holdings · report on 449 · periods 2026-05-31 and 2026-06-30.**
*The matched-fund control is what makes this valid: same fund, same valuation date, same pricing vendor, so cross-issuer pricing-methodology differences cancel and what is left is issuer credit.*

### Result

| Tenor bucket | Athene | Peer median | **Penalty** |
|---|---|---|---|
| 0–3y | T+68.9 (n=106) | T+50.4 (n=195) | **+18.5bp** |
| **3–6y (the "5Y" tenor)** | **T+112.0 (n=46)** | **T+74.2 (n=84)** | **+37.8bp** |
| 6–11y | T+136.4 (n=9) | T+86.6 (n=9) | +49.7bp |

### 🔑 Read: SUGGESTIVE CORROBORATION from an independent holder-side series — directionally consistent, NOT a confirmation

| Reading | Source | 5Y-ish penalty | Athene level |
|---|---|---|---|
| Q1'26 deck (5/14) | **Athene's own**, Athene's own peer set | **+44.7bp** | T+123 |
| SHADE NPORT run, 7/27 (3/31–5/31 data) | **independent, holder-side** | pooled **+55.4** · within-fund paired **+40.2** | T+142.9 → T+116.1 by period |
| Q2'26 deck (8/13; JPM spreads **as of 2026-08-07**) | **Athene's own** | **+33.0bp like-for-like** (+30.0 as published) | T+110 |
| **SHADE NPORT rerun, 8/28 (5/31–6/30 data)** | **independent, holder-side** | **+37.8bp** | **T+112.0** |

🔑 **Athene's own deck says T+110; an independent holder-side reconstruction says T+112.0. Two bp apart, from unrelated data.** The penalty lands **between** the two deck readings and **moves the same direction as the deck** (down). ⇒ **The 8/13 leg-1 STABLE grade gets SUGGESTIVE, DIRECTIONALLY CONSISTENT support from a source Athene does not control.** ⛔ **Not "confirmed":** the windows overlap, CUSIP composition changes between runs, and the estimator differs from the prior headline (+55.4 pooled → +37.8 pooled vs a +40.2 within-fund PAIRED headline). **A level agreeing to 2bp is a striking coincidence of two noisy estimates, not a validation of either.**

⚠️ **BASIS GUARD — do not difference these runs naively.** The `>>> ATHENE PEER PENALTY` line is a **pooled median-of-medians**; the 7/27 study's headline `+40.2bp` was the **within-fund PAIRED** estimator (strictest), and its pooled figure was **+55.4bp**. **On the consistent pooled basis the move is +55.4 → +37.8**, but the windows differ (3/31–5/31 vs 5/31–6/30) and **CUSIP composition changes between them**, which is the exact caveat registered on 7/27. ⇒ **Carry the DIRECTION as corroborated and the MAGNITUDE as not comparable across runs.**
⚠️ **6–11y is n=9 vs n=9.** Better than the 7/27 run's single-CUSIP n=4, still thin. **Do not cite it as a tenor bucket.**
⚠️ **NPORT values are pricing-service marks, not TRACE prints**, and YTM is a semiannual bisection ignoring accrued/day-count/calls. **Both are systematic and largely cancel in a matched-tenor difference — which is why the PENALTY is the deliverable and T+112.0 is not.**

**Consequence: kill-path-1 stays YELLOW.** RED bar is **>250bp or a pulled/failed syndication** — **~212bp away.** **No band, threshold or confidence moved.**
⚠️ **The registered identification defect is UNTOUCHED by this rerun:** a price-only canary cannot separate *credit improved* from *the issuer stopped feeding the market paper*. **The supply-adjusted companion (S1/S2/S3) remains the instrument for that, first graded reading Q3-2026.**

---

## PART 2 — AG 55, re-based at NAIC primary

**Primary:** *Reinsurance (E) Task Force* call materials, **NAIC, 2026-03-02 (draft date 2/24/26)**, `content.naic.org/sites/default/files/call_materials/RTF 3.2.2026 Materials.pdf`, pdfminer-extracted. **Speakers: Macaluso, Andersen, Rehagen, Schelp (NAIC).**

### What AG 55 actually is, verbatim
**Actuarial Guideline LV — *"Application of the Valuation Manual for Testing the Adequacy of Reserves Related to Certain Life Reinsurance Treaties"***, adopted by the **Life Actuarial (A) Task Force** at the Summer National Meeting. *"Several state insurance regulators proposed this project, which made changes to the **asset adequacy testing (AAT) methodology for the assets that support reinsurance transactions.**"*

### The template contents — this is the disclosure surface, and it is broader than I had it
LATF created and approved **standardized templates** covering: *"details about the assuming company, key risks, **supporting assets, assumed net yields, cash flow testing results, and attribution analyses explaining any changes in reserves**"* plus *"documentation of **mortality and policyholder behavior assumptions, both before and after transactions**."*

### 🔴 THE ROUTING FACT THAT RE-BASES KILL-PATH #2
> *"Reports will be provided to the **domestic regulator upon request** and to the **Minnesota department representing the Valuation Analysis (E) Working Group**."*

**My carried framing was *"disclosure-only to domestic state regulators"* — a picture of 50 scattered filings with no aggregator. That is wrong in a way that matters:**
- To the **domestic regulator** it is **upon request** — *weaker* than I had it.
- But there is a **mandatory central copy to Minnesota as the VAWG representative** — **an aggregation point that did not exist in my model.**
- ⚠️ **And an explicit carve-out:** Rehagen stated *"the request for the data for Missouri companies would come directly from Missouri"*, because the **NRRA requires that only the domestic regulator of a professional reinsurer can regulate its solvency and examine it.** ⇒ **The central collection is not uniform; state law cuts across it.**

### 🔑 THE DATED EVENT KILL-PATH #2 HAS BEEN MISSING
> *"The Valuation Analysis (E) Working Group plans to review incoming filings promptly and **aims to begin sharing general findings at the 2026 Summer National Meeting**. These findings will be presented to … the Life Actuarial (A) Task Force, **Financial Stability (E) Task Force**, Reinsurance (E) Task Force, and potentially the **Financial Condition (E) Committee**."*

**Kill-path #2 is "AG 55 forced disclosure," and its registered weakness has been that the reports are invisible to the public.** ⇒ **The public-visible artifact is NOT the filings — it is VAWG's GENERAL FINDINGS presented to NAIC groups.** That is a real, dated, checkable surface. ⚠️ **"General findings" is aggregate by construction — it will not name an insurer**, so it can move the *cohort* read and cannot, by itself, move a single name.

### Other primary facts recorded
- **First reports due 2026-04-01** (confirms the date I carried). **Filing instructions distributed early February 2026, recipient list based on 2024 Schedule S data** — companies were told to check their own inclusion.
- **Process is *"nearly identical"* to AG 53 Complex Asset Disclosure** for prior filers ⇒ **AG 53's history is the base rate for what AG 55 will actually produce.**
- 🔴 **Offshore is the stated origin:** Macaluso *"noted an increased focus lately on offshore reinsurance… the NAIC has worked to address these concerns through projects such as AG 55, **which were originally initiated to address issues related to offshore reinsurance; however, more work will likely be needed**."* **Two regulator-only education sessions** were held, with another planned. ⇒ **The regulator considers AG 55 a partial answer to the offshore question — which is SHADE's Bermuda/ACRA perimeter.**
- **Bermuda, Japan and Switzerland are reciprocal jurisdictions; Bermuda, Japan and the UK are changing their regulatory systems and NAIC staff are monitoring.**

### ⛔ ONE CARRIED CLAIM I CANNOT CONFIRM — flagged, not carried forward as fact
My 8/13 news sweep recorded that **AG 55, from 2026 reporting, mandates disclosure of *Level-3 exposure, PIK interest, and private letter ratings***. **Nothing in this primary says that**, and the template contents quoted above do not include those three items. **Those disclosures belong to the AG 53 / annual-statement complex-asset lineage, not obviously to AG 55.** ⇒ **Downgraded to UNVERIFIED pending a read of the guideline text itself on the LATF page.** `[[finding_rederived_signal_loses_the_senders_caveats]]` — it entered my surfaces as a one-line sweep item and was about to be used to re-base a kill path.

**Kill-path #2 disposition: RE-BASED, not advanced.** The forced-disclosure mechanism is real and running (~first filings in, VAWG reviewing); **the public trigger is VAWG's Summer-2026 general findings, aggregate and unnamed.** **No threshold moved.**
