# SHADE → PROME · 2026-08-28 (round 2, final touch) · W1 leg (a) resolved, the flow baseline built, canary rerun, AG 55 re-based

**Session:** PROME-orchestrated, two touches, same approved workstream. **Markets CLOSED — every price is a dated 8/28 close.**
**Round-2 commits:** `130a333ef` · `497195ac0` · `aef508ba5` · `083fa1864` · `cf7922fb1` (brief, folded LAST). **NOT PUSHED — held for your push-train.**

---

## THE HEADLINE: three of my own instruments were wrong, all in the same direction

**Each had been ENUMERATED rather than TESTED — a list I wrote, then treated as a fact about the world.**

| # | Instrument | Defect | Fixed |
|---|---|---|---|
| ① | **Delaware Life escalation ladder** | All six markers were acts of a **regulator, rating agency or issuer** — no rung for the counterparty event that actually happened | **Marker (0) added, MET** |
| ② | **"The Q3 flow figure is GATED"** *(registered by me this morning)* | **False.** I enumerated three GATED routes and treated the list as exhaustive. **The issuer publishes its own quarterlies, free, and Q1 and Q2 2026 were on its website while I wrote that the figure was unreachable.** | **WITHDRAWN; W1 leg (a) RESOLVED** |
| ③ | **`T-SHADE-01`** | Graded and cited across five surfaces since 7/9 with **no locus in my charter**; original registration never located | **REGISTERED CANONICALLY** |

⇒ **The transferable form, flagged for DAEDALUS: an opacity enumeration that lists only the gates will always conclude the thing is gated. `[[finding_unfetched_is_not_unavailable]]`, second instance in 15 days.** The heuristic that would have saved ten minutes: **a regulated entity that wants to be sold through bank distribution has its own reasons to publish statutory financials — look at the issuer first.**

---

## 0. 🔴 EXPLICIT WITHDRAWAL, ON MY OWN WORD — for the DOCKET row you registered on my touch-1 memo

**You registered the ~11/15 Delaware Life Q3 statutory DOCKET row on my touch-1 wording, *"behind the NAIC InsData / state-DOI gate."* I am withdrawing that wording. It is wrong, and the row should be corrected on this statement rather than on RAV's relay.**

| | |
|---|---|
| **What I claimed (touch 1, 2026-08-28 ~18:xx)** | Delaware Life's quarterly statutory statement is reachable only through **NAIC InsData · state-DOI · AM Best–CapIQ**; my proven EDGAR N-VPFS route is **annual-only**; therefore the ~11/15 Q3 instrument is **GATED**, and **W1 leg (a) is the access question standing between SHADE and it**. |
| **What the primary showed** | **Delaware Life publishes its own statutory statements — quarterly AND annual — free, no login, back to 2022,** at **`https://www.delawarelife.com/content/business-highlights`**. I downloaded **Q1-2026** and **Q2-2026** and verified the jurat page of each before reading a figure: NAIC Life/A&H Association Edition, **barcode `79065202620100102`**, **cocode 79065**, **group 4794**, **state of domicile DE**, *"QUARTERLY STATEMENT AS OF JUNE 30, 2026."* **Both were on that page while I was writing that the figure was unreachable.** |
| **What the access path actually is** | **Index page → per-asset Brandfolder CDN PDFs → `pdfminer`.** ⚠️ **The CDN keys are opaque and per-asset — do NOT construct a Q3 URL by pattern; re-read the index page at ~11/15.** ⚠️ **Verify the jurat barcode `79065<YEAR><Q>` before reading any figure.** ⚠️ **DLIC only — DLAC (cocode 17466) and Clear Spring are not on this page.** |
| **What changes for the ~11/15 instrument** | **"Behind a gate" is WITHDRAWN — the instrument is openly published and free.** ✅ **"PARTIALLY BLIND" STANDS and is unchanged:** Q3 covers **7/1–9/30** and the pause surfaced **8/28**, so it captures **at most ~1 of 3 months**, and the first CLEAN full-period read is the **FY2026 annual, ~2027-03-01**. **The row's DATE and its blindness caveat are both still right; only the access clause was wrong.** |
| **What changes for W1 leg (a)** | **RESOLVED, and it no longer blocks anything.** It is **not** the access question standing between SHADE and the Q3 instrument — **nothing was.** The three gated routes were tested and their status recorded (AM Best **bot-blocked**, InsData **paid**, CIS **open but a directory**, Delaware DOI **exam reports only**), which is the enumeration W1 actually asked for. |
| **The defect, so it is on the record as mine** | **I enumerated three GATED routes and treated that list as exhaustive. I never asked whether an UNGATED route existed.** `[[finding_unfetched_is_not_unavailable]]`, **second instance in 15 days.** ⇒ **An opacity enumeration that lists only the gates will always conclude the thing is gated.** |

---

## 0b. CCC NORMALIZATION — CLOSED as a CITATION, not a registration *(your ruling + BROCK's catch, both adopted in full)*

**Two ratios survive, ONE OWNER EACH, and SHADE registers NEITHER.** **`CCC/HY` → REGINALD `VX-REG-18.04`** — SHADE and BROCK **cite, neither copies the series**. ⛔ **Registering it here would have forked a metric carrying a Will-approved 8/13 escalation stand-down.** **`CCC/BB` + the `CCC−BB` gap → BROCK `KB-BRK-221`.**
**BROCK's reason adopted over my weaker "different questions": each is WRONG FOR THE OTHER'S JOB** — CCC/HY is constituent-inclusive, so the denominator rises with the tail and the ratio **damps exactly at the extreme** (a fixed-sign bias, wrong for a tail threshold); CCC/BB is disjoint and unbounded, right for a threshold, but references no investable index so it cannot answer the context question.
🔴 **BROCK's harder bar adopted too: the CITATION bar lifts now this is written; the INDEPENDENCE bar NEVER does.** Both read the **same 787-obs series**, so **agreement between them is arithmetic, not corroboration.**
🔑 **And my figures completed BROCK's own discriminator, which I did not anticipate:** CCC **1031** ÷ **6.739** ⇒ **implied BB 153.0** vs **160 [FRED 8/12]** ⇒ **BB tightened 7bp while CCC widened 11bp**, gap **860 → 878** — **both legs now point the same way where BROCK had only the ratio.** ⚠️ **Implied BB is DERIVED, not a published print.**
**Also from BROCK, applied to `T-SHADE-01`:** **LIQUID owns the HY series and its sustain count; SHADE owns only whether the trigger fires** · 🔴 **the SIGN LEG is a DATED READING, not a standing state — if the level leg crosses, do NOT read "1 leg" off the 8/13 sign reading; re-read on closes first.**

---

## 0c. RAV QC — all three applied before this delivery
**(1)** The script **still hardcoded the 2026-07-27 JSON output name**, so a future rerun would have recreated the exact stale artifact that already bit me once — **output filename now derived from the RUN date**, noted in the header. **(2)** *"confirms the narrowing"* replaced at **9 sites across 5 files** with **directionally-consistent / SUGGESTIVE corroboration**, with the reason stated inline (overlapping windows, changed CUSIP composition, a different estimator from the +40.2bp headline) — **a 2bp agreement between two noisy estimates is a coincidence worth noting, not a validation.** **(3)** The enumeration line reserved its only incompleteness warning for **network failure**; a **MAX_FILINGS stop is a BOUNDED SAMPLE, not a census**, and it is the *normal* exit, so it is the one most likely to be read as complete — **both cases now warn, and the line names which kind of incompleteness it is.**

---

## 1. W1 LEG (a) — RESOLVED, and the gate does not exist

| Route | Result |
|---|---|
| **AM Best** | ❌ **BLOCKED** — Radware bot wall at `web.ambest.com`. Not a paywall, an automation wall. |
| **NAIC InsData** | ⚠️ **PAID** — account + login, pricing on request. |
| **NAIC CIS** *(the free tier)* | ✅ **OPEN and machine-queryable** — the Tableau CSV export works unauthenticated (**5,262 companies, 1.89 MB**) and is where **cocode 79065** was established. **But it is a DIRECTORY, not financials.** |
| **Delaware DOI** | ⚠️ **Exam reports only**, not statements. |
| 🔑 **THE ISSUER** | ✅ **FULLY OPEN — quarterly AND annual, free, no login, back to 2022:** `delawarelife.com/content/business-highlights` |

**Pull path written down and reproducible** (index page → Brandfolder CDN PDFs; ⚠️ **CDN keys are opaque per-asset, so do NOT construct the Q3 URL by pattern — re-read the index at ~11/15**; verify the jurat barcode `79065<YEAR><Q>` before reading any figure). ⇒ **The ~11/15 Q3 instrument is NOT gated. "Partially blind" STANDS; "behind a gate" is WITHDRAWN.**

## 2. THE FLOW FIGURE — pre-pause baseline, at primary, new to the fleet

**DLIC Q2-2026 statutory, 1H-26 vs 1H-25:** direct premiums + deposit-type **$6,726M vs $5,903M (+13.9%)** · individual annuities **$4,645M vs $4,188M (+10.9%)** · **surrenders and withdrawals $2,061M vs $1,425M (+44.6%)** · **surrenders ÷ inflows 24.1% → 30.6%** · net cash from operations **$3,447M vs $2,968M**.
⇒ **The channel Truist and Fifth Third closed was an ACTIVELY GROWING one — which makes the pause more consequential, not less — but outflows grew ~3× faster than inflows.**
⛔ **This does NOT confirm the stripped "flows going the wrong way" framing: it ends 6/30/26, two months before the pause; surrender-charge cohorts are undisclosed so mechanical and behavioural components cannot be separated; and net operations improved. Not a liquidity event.**

**Also at primary:** 🔴 **the remediation plan is not visibly shrinking the book** — affiliate-contingent private credit **$16,372M → $16,822M (+2.75% in DOLLARS)** while the **SHARE fell 35.67% → 32.82%** on a GA that grew 11.6%. **Report the pair; the plan's own metric is not public and that decides which reading is operative.** *(Same share-vs-quantity trap I adopted from `-021-CORRECTION` hours earlier — it landed on my own vector.)*
✅ **Confirmed exactly from an independent document:** FY2025 affiliate-contingent **$16.37B**, bond leg **$12.62B**, GA **$45.90B**, admitted **$64.7B**.
**Charter ratios:** **Illiquidity Ratio 10.05% — a FLOOR ONLY.** ⛔ **The illiquid-ABS leg is missing (Schedule D is annual), so I CANNOT say it is under the 30% red flag.** **Affiliated Reinsurance and TSR/Gober are NOT COMPUTABLE from a quarterly** — both need the FY2025 annual, **which is on the same open route and is now my #1 owed item.**
✅ **Two clean negatives, verified not assumed: going concern NEGATIVE** (a truncated fragment nearly inverted it) and **NO state prescribed or permitted practices** — a registered SHADE mechanism confirmed **not in use** at this name.

## 3. CANARY RERUN — 3 defects fixed (+1 found at commit), and SUGGESTIVE independent support

**53 matched funds / 492 holdings / 0 fetch failures / 0 pages lost. 3–6y penalty +37.8bp: Athene T+112.0 vs peer median T+74.2.** **Athene's own Q2 deck says T+110 — 2bp apart, from unrelated data, same direction.** ⇒ **DIRECTIONALLY CONSISTENT, SUGGESTIVE support for the 8/13 leg-1 STABLE grade, from a source Athene does not control.** ⛔ **NOT "confirms"** — overlapping windows, changed CUSIP composition, a different estimator from the +40.2bp headline. **Kill-path-1 YELLOW, RED bar ~212bp away.**
🔑 **Fix 1 caught a live instance immediately: the 5/31 curve is backfilled to 5/29 — 2026-05-31 was a Sunday — silent in every prior run.** **Fix 3** now distinguishes *stopped early* from *pages lost*. **Fix 2** not triggered but its verdict is printed rather than assumed.
⚠️ **Two further defects found while committing, both recorded:** **(1b)** the provenance fix stamped **stdout but not the saved artifact**, and `research/*.log` is **gitignored** — a stamp that exists only in stdout is not a stamp; **(1c)** **the rerun OVERWROTE the tracked 7/27 JSON** because the output path was a constant — **restored from git; a rerun that silently destroys its own comparator is worse than any of the three defects DAEDALUS named.**
⚠️ **Basis guard: the printed penalty is a POOLED median; 7/27's +40.2bp was the within-fund PAIRED estimator. Direction corroborated, magnitude NOT comparable. PROVISIONAL.**

## 4. AG 55 — re-based at NAIC primary, and kill-path #2 finally has a dated public surface

*"Reports will be provided to the **domestic regulator upon request** and to the **Minnesota** department representing the Valuation Analysis (E) Working Group."* ⇒ **weaker to the domicile than I had it, but a CENTRAL AGGREGATION POINT my "disclosure-only to 50 domiciles" model lacked.** ⚠️ NRRA cuts across it (Missouri requests its own).
🔑 **VAWG *"aims to begin sharing GENERAL FINDINGS at the 2026 Summer National Meeting"*** to LATF / Financial Stability (E) TF / RTF / possibly Financial Condition (E). ⚠️ **Aggregate by construction — moves the COHORT read, never a single name.** **Offshore is the stated origin of AG 55** — my Bermuda/ACRA perimeter.
⛔ **My own 8/13 sweep claim that AG 55 mandates Level-3 / PIK / private-letter-rating disclosure is NOT in this primary and is DOWNGRADED TO UNVERIFIED.** **Kill-path #2 RE-BASED, not advanced.**

## 5. Cross-desk
**BROCK's FHLB packet consumed and folded with attribution** — Delaware Life is FHLB Indianapolis's **#2 borrower at $4,963M = 12%, +71.6% YoY, then flat to the dollar two quarters**; both of BROCK's readings carried uncollapsed; the cooperative-not-a-bank guard adopted. ⚠️ **Correction sent: BROCK carries the pause as a precursor to a rating action — the read you and I both settled against.** **CCC + X1 reconcile SENT to `brock-0828`, no reply yet** — my proposal is that **two figures survive with the reason recorded, rather than collapsing them.**

---

## COMPLETION — SHADE — 2026-08-28 (round 2)
STATUS: ✅ DONE
CHANGED: AGENTS/SHADE/{STATUS,SCRATCH,MEMORY,CLAUDE,MAINTENANCE,NEXUS_BRIEF,REFERENCE}.md, board_log.tsv, research/{DELAWARE_LIFE_Q2_2026_STATUTORY,FABN_CANARY_RERUN_AND_AG55}_2026-08-28.md, research/FABN_PEER_SPREAD_NPORT_2026-07-27.py (4 fixes), research/FABN_PEER_SPREAD_NPORT_RERUN_2026-08-28.{json,_RUNLOG.md}, archive/MEMORY_lessons_rotated_2026-08-28.md
RESULT: W1 leg (a) RESOLVED and the "GATED" claim explicitly WITHDRAWN on my own word (§0) for your DOCKET row — the instrument is openly published; "partially blind" stands, only the access clause was wrong. DLIC Q2-2026 pulled at primary: pre-pause flow baseline built (1H-26 inflows $6,726M +13.9%, surrenders $2,061M +44.6%, ratio 24.1%→30.6%); remediation plan UP 2.75% in dollars / DOWN 2.85pp in share; Illiquidity Ratio 10.05% FLOOR only; going concern and permitted practices both clean negatives. T-SHADE-01 registered canonically + BROCK's two corrections (LIQUID owns the series; the sign leg is a DATED reading). CCC reconcile CLOSED as a citation, not a registration — two ratios, one owner each, SHADE registers neither. NPORT rerun +37.8bp vs the deck's T+110: SUGGESTIVE, not confirmation. AG 55 re-based. RAV fixes 1-3 applied. 8 commits, READ-CAP 0. No band, threshold, kill-line, vector score or confidence moved.
GAPS: Affiliated Reinsurance Ratio and TSR/Gober are NOT computable from a quarterly — both need Schedule S / Schedule D from the FY2025 ANNUAL, which is on the same open route and is now owed item #0. NAIC SVO override COUNT not attempted — recorded as owed, not as zero. AG 55's Level-3/PIK/private-letter-rating claim is UNVERIFIED pending the guideline text itself.
WILL_NEEDS: None.
FOLLOW-UP: The FY2025 DLIC annual statement is one fetch and yields two charter ratios I have never been able to compute. BROCK owes a reply on the CCC normalization. 3 BROCK files are uncommitted in the tree (flagged, not swept).
