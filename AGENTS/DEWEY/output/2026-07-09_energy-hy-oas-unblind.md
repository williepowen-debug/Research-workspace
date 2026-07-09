# Energy HY OAS — un-blinding the paywalled trip from public primaries
**Date:** 2026-07-09 | **Mode:** Thesis | **Confidence:** Medium-High (level, pre-re-escalation) / Low (live post-7/7 read — genuinely unverifiable from public data)

> **Flag:** REQ-DEWEY-20260702-006 (Batch-2 prompt 10). **Reframe note:** the prompt's 7/4 "energy de-escalated → deprioritized, confirm NOT stressing" framing was superseded before this run — the manifest re-prioritized it UP on 7/8 after the US-Iran truce collapsed and Brent spiked +6.3% to $76 settle [7/9]. This run therefore reads the evidence against a LIVE energy re-arm, not a de-escalation. Verdict below is threshold-adjudicated either way.

## Key Finding
As of the last hard datapoint (**May 31, 2026**), the ICE BofA US High Yield **Energy** sub-index OAS was **164bps — the *tightest* of all HY sectors**, far below both the >300bps trip and the >400bps stress line, and *tighter* than the ~285bps cited for Apr 28. **Neither threshold was crossed Apr 28 → end-May.** No energy-sub-index print exists publicly for the post-July-7 re-escalation, so whether energy HY is widening *beneath the current re-arm* is **UNVERIFIED at the sub-index level** — but the surrounding evidence (broad HY OAS 267–270bps *tightening through* the 7/7-8 re-arm; rising oil is revenue-positive for E&P; a decoupling literature that finds credit widens only ~half what oil moves imply) points to **no energy-credit stress as of 7/9.** The durable deliverable: **no free source publishes the energy sub-index daily**; the one reproducible free artifact carrying it is Fidelity's **monthly** institutional HY PDF (`931730.PDF`).

## Evidence

### 1. The load-bearing level — independently document-confirmed
DEWEY pulled the Fidelity PDF directly (`pdf2text.py`, not relying on the workflow's extract) and the table reads verbatim:
- **ICE BofA HIGH-YIELD CORPORATE SECTORS → Energy → OAS 164bps** [PRIMARY: ICE BofA, republished in Fidelity Institutional US Fixed Income monthly `931730.PDF`, **as of May 31, 2026**, pulled 7/9/2026].
- Energy is the **tightest** HY sector in the table (sector OAS set: 164/247/304/331/668/250/164/248/266/2153).
- Same PDF, broad HY: **"Spreads decreased −9 basis points to 274 at month-end... Yields decreased −2bps to close May at 7.00%... There were no defaults in May"**; ICE BofA trailing-12mo default rate **1.85%**.
- Separate **Bloomberg** (IG) Corporate-Energy OAS line in the same PDF = 73bps [5/31] — the IG reference point; not to be confused with the 164 HY figure.

**Provenance caveat (kept, not relaxed):** 164 is one **republisher** (Fidelity citing ICE BofA), not a direct ICE feed print — the workflow's adversarial vote was 2-1 on this. DEWEY's independent pull confirms the *document says 164*; it does not independently confirm ICE's underlying calc. Rated Medium-High on that basis: the number is real and internally consistent (energy ~108bps *inside* the 274 broad index — a normal tightest-sector relationship), but rests on a single secondary carrier.

### 2. The broad-HY backdrop THROUGH the re-arm — DEWEY primary pass (fills the workflow's blind spot)
The workflow's freshest hard number was Jul 7. DEWEY pulled the full broad-HY-OAS path across the 7/7-8 re-escalation [PRIMARY: FRED `BAMLH0A0HYM2`, accessed 7/9/2026; 1-day print lag]:

| Date | Broad HY OAS |
|------|--------------|
| Apr 28 | 285 |
| Jun 26 (AI-selloff bump) | 283 |
| Jun 30 | 275 |
| Jul 6 | 272 |
| **Jul 7** (re-arm day 1) | **267** |
| **Jul 8** (Brent +6.3%) | **270** |

**Broad HY did NOT widen through the re-arm — it sits 267–270, near the tight end, −15bps vs the Apr 28 anchor.** Energy HY is a subset of this index and historically its tightest sector; for energy to have crossed >300 while the parent tightened to 270 would require a ~30–40bps *idiosyncratic energy blowout against a calm tape* — for which there is zero corroborating evidence (no energy default headlines, no distress-ratio spike found).

### 3. Threshold adjudication (explicit)
| Threshold | Verdict | Evidence |
|-----------|---------|----------|
| **>300bps (LIQUID energy-credit trip)** | **NOT crossed** on any available data (last read 164, 5/31) | Fidelity/ICE 164 @ 5/31; broad HY 267-270 through 7/8 caps the plausible energy level |
| **>400bps (BRENT energy-stress)** | **NOT crossed** — nowhere near (236bps of headroom at last read) | same |
| Post-7/7 sub-index | **UNVERIFIED** — no public print exists | 164 predates re-escalation by 5+ weeks; circumstantial evidence = no stress |

### 4. Decoupling claim (KB-LIQ-058) — SUPPORTED
Oil-price spikes do **not** pass one-for-one into energy credit:
- ECB Economic Bulletin box 2026/04 (Bayesian VAR on Iacoviello-Tong oil-geopolitical-risk index): oil-supply shocks push oil ~+30% for ~two quarters, but **"risk spreads widened slightly at the start of the conflict, to about half the levels suggested by historical patterns, before returning to pre-war levels"** [PRIMARY: ECB, Apr 2026]. *Caveat: ECB uses aggregate BBB spreads, does not isolate energy credit.*
- Sector-specific corroboration the ECB lacks: energy HY was **tightest-in-class (164) while Brent was still elevated** in Q2 — consistent with rising oil being *revenue-positive* for E&P issuers (higher oil → better energy-credit fundamentals), the opposite of a stress channel.
- SSGA Q1-2026 Global HY ("Carry vs Conflict", 3/31): base case defaults →~3%; a **"sustained energy shock"** stress case → defaults 6-7%, **"markets are not yet pricing for this outcome."** *Caveat: global aggregate HY, Q1 vintage, forward opinion — not a US energy-sub-index level.*

**Net:** the decoupling is real, and it runs in the *reassuring* direction for this question — an oil re-arm is not a mechanical energy-credit-stress trigger; it can even be credit-supportive for E&P. Energy credit stress requires *sustained* shock + demand destruction, not a price spike.

### 5. DELIVERABLE — reproducible free source to keep the cell live
**No free/registerable source publishes the ICE BofA energy HY sub-index OAS on a live/daily cadence.** Confirmed dead ends: FRED carries only the broad `BAMLH0A0HYM2` (energy sub-index tickers `BAMLHE0EHYIEOAS` et al. **HTTP 400 — genuinely not on free FRED**, DEWEY-verified 7/9); ICE Developer Portal / `indices.theice.com` = commercial contract / login wall; S&P DJI HY Energy proxy landing page did not validate in this run (open item); HYG/JNK factsheets publish sector *weights* but **no sector OAS**, are stale (3/31 vintage), and JNK tracks a Bloomberg (not ICE) family.

**Best available free source → Fidelity Institutional monthly HY PDF:**
- **URL:** `https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F931730.PDF`
- **Access path:** `pdf2text.py <url> --grep "ICE BofA"` (DEWEY-verified working 7/9; the ICE BofA HY sector table incl. the Energy OAS line is machine-readable).
- **Cadence:** **monthly** (as-of month-end; May-31 vintage was live on 7/9 — so ~5-6wk publication lag). NOT daily; dependent on Fidelity continuing to publish.
- **Caveat:** gives a *republished monthly* energy-sector OAS, not a live feed. It un-blinds the cell to a monthly resolution — enough for a slow-moving threshold watch, not enough for a same-week trip confirmation. For same-week reads the fleet must proxy off broad HY (FRED, live) + the knowledge that energy trades tightest-in-class.

## Counter-Evidence
- **The live question is genuinely unanswerable from public data.** The 164 is 5+ weeks stale relative to the re-arm. If an energy-specific credit event fired between 6/1 and 7/9, no public source would show it yet (next Fidelity vintage ≈ June-30 data, publishing ~mid-to-late July). *This is the honest gap, not a confident all-clear.*
- **Rising oil is not unambiguously credit-positive** if it reflects supply destruction that also destroys demand / raises recession odds — a sustained-shock path (SSGA's 6-7% default scenario) would widen energy HY. The current re-arm is a *price* move, not yet a *sustained supply-loss* move (per the BRENT sustain test resolving Fri 7/10).
- **164 rests on one republisher.** If Fidelity mis-transcribed the ICE table, the whole level is off — though the internal consistency (energy 164 < broad 274, both from the same sheet) argues against a transcription error.
- **Broad-HY-as-cap is an inference, not a measurement.** Energy *can* decouple wider from broad HY in a true energy bust (2015-16, 2020 saw energy HY >1000 while broad ~600). Nothing in 2026 resembles that regime, but the cap logic assumes normal cross-sector behavior.

## Source Quality Assessment
Reliable on the pre-re-escalation level and the decoupling dynamic (PRIMARY: ICE-via-Fidelity, ECB, FRED; SECONDARY: SSGA). The single unavoidable weakness is **time-sensitivity**: the load-bearing number predates the event the question is about. No public source closes that gap — this is a structural data-availability limit (the exact reason the cell was blinded), not a search failure. Gaps: S&P DJI HY Energy proxy tracking-validation not completed; confirmed current ICE energy ticker code not positively pinned.

## References
- ICE BofA HY sector OAS table (Energy 164, 5/31) + broad HY 274 / default 1.85% — Fidelity Institutional US Fixed Income monthly, `931730.PDF`, accessed 7/9/2026: `https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F931730.PDF`
- Broad HY OAS path (285→270, Apr28–Jul8) — FRED `BAMLH0A0HYM2`, accessed 7/9/2026: `https://fred.stlouisfed.org/series/BAMLH0A0HYM2`
- Oil-shock → credit-spread decoupling — ECB Economic Bulletin box 2026/04: `https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202604_02~7d79ce3c90.en.html`
- HY stress-scenario framing — SSGA Global HY Q1 2026 ("Carry vs. Conflict"): `https://www.ssga.com/library-content/assets/pdf/global/fixed-income/2026/ghy-q1-2026.pdf`
- Energy sub-index NOT on free FRED — tickers `BAMLHE0EHYIEOAS` / `BAMLHE1H0HYE1OAS` / `BAMLHYH0A0HYM2EY` all HTTP 400, DEWEY-verified 7/9.

## Process Report
- **Searches run:** 1 `/deep-research` workflow (104 agents, 6 angles, 21 sources fetched, 30 claims → 25 verified → 20 confirmed / 5 refuted / 6 synthesized findings) + DEWEY independent pass (FRED broad-HY path pull; direct `pdf2text` re-pull of the Fidelity PDF to confirm the 164; 4 discontinued-FRED-ticker probes).
- **What worked:** the Fidelity institutional PDF was the single high-value find — a free artifact that actually republishes the ICE BofA HY *sector* OAS table. DEWEY's independent pull upgraded it from the workflow's 2-1 "medium" to document-confirmed. FRED broad-HY path pull added the through-the-re-arm read the workflow lacked (its data stopped 7/7).
- **Data gaps:** no post-6/1 energy-sub-index print anywhere public — the live question is structurally unanswerable. S&P DJI HY Energy proxy tracking-vs-ICE validation not completed. Current ICE energy ticker code not positively confirmed.
- **Source frustrations:** iShares HYG factsheet URLs 403 to automated fetch (bot wall — already in BACKLOG). ICE portal is a hard commercial/login wall. Energy sub-index removed from free FRED (the root blinding).
- **Confidence:** Medium-High on the pre-re-escalation level + decoupling; **Low** on the live post-7/7 read (honestly unverifiable). High on the deliverable (the monthly-PDF constraint is a firm finding, not a maybe).
- **If I had more time/tools:** check whether a **June-30-vintage** Fidelity PDF has published (would bracket the re-escalation start) — the literature ID may rotate; worth a monthly re-pull. Validate the S&P DJI HY Energy index free-tier page as a second monthly proxy.
- **Suggestions:** (1) add the Fidelity PDF monthly energy-OAS pull to the fleet's monthly cadence — it permanently un-blinds the cell to monthly resolution. (2) For same-week reads, LIQUID/BRENT should proxy energy off broad HY (FRED live) + the "energy = tightest HY sector" prior, and treat a >300 energy trip as *not confirmable same-week* by design.
