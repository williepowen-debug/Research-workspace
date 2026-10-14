# LIQUID — Expected-Signals Tracker (absence-is-data)
**Born:** 2026-07-11 (DAEDALUS Batch-1 ask-8, Will-approved; PROME first-class-slot packet 7/10 — executed 7/11) · **Owner:** LIQUID
**Purpose:** Re-homes the 5 signal-types orphaned when `archive/legacy/EXPECTED_SIGNALS.md` was stranded (`4894d8cc`; sibling-drift vs LABOR/SAM, DAEDALUS 7/4). These are signals that **SHOULD appear if the stress thesis is transmitting** — their **absence is information** (transmission blocked, timing wrong, or thesis leg weak). The other 7 of the legacy file's 12 types are covered by live STATUS Triggers; do not duplicate them here.

**Template:** LABOR/SAM ES pattern (ID table + bands + response protocol + resolved log). Bands carried from the legacy doc; restated 2026-07-11 without re-derivation — re-validate a band before acting on a first fire.

---

## Active Expected Signals

| ES-ID | Signal | Bands (Y / O / R) | Data source (status) | Check cadence | Implication if ABSENT under stress |
|-------|--------|--------------------|----------------------|---------------|-------------------------------------|
| ES-LIQ-01 | **FHLB stress** — advance-rate surge / issuance spike / delivery issues | advances >75% / >85% / "delivery" issues | FHLB Office of Finance issuance + FFIEC (REGINALD-adjacent; quarterly + headline-driven) | On any regional-bank funding headline; else monthly | Bank leg of the BDC→bank path NOT drawing on the lender-of-next-to-last-resort → credit stress staying in PC wrappers, not reaching bank funding |
| ES-LIQ-02 | **Sponsored-repo contraction** — FICC sponsored volume decline (dealer capacity / HF deleveraging tell) | plateau / −$100B/wk / — | DTCC sponsored-repo volumes (⚠️ OFR mirror of FICC HFM series was STALE 10/15/25 — check DTCC direct before first citation; MEMORY.md stage-2 note) | Weekly when basis-trade rows are hot; else monthly | $700B leveraged SOFR-short (Open Monitors, SIG-W-20260702-009) NOT unwinding via the funding leg — positioning pin holds, no forced-cover cascade yet |
| ES-LIQ-03 | **MMF WAM shortening** — liquidity hoarding ahead of redemptions/vol | <30d / <20d / <15d | ICI weekly flows + SEC N-MFP (monthly, lagged); Crane if accessible | Weekly in stress windows; else monthly | MMF managers NOT defensive → repo funding to the basis trade still rolling; FLOW-LIQUID-2.02 cascade precondition absent |
| ES-LIQ-04 | **FTD spike** — UST settlement fails, concentrated on-the-runs, aged-fails rising | — / >$50B / >$60B (+aged >30d ratio rising) | NY Fed primary-dealer fails data (weekly Thu, free) | Weekly (pairs with the PD inventory pull, mandate-ext PRIMARY) | Collateral velocity holding (VX-8.01 concept) → dealers not stuffed; auction-fail cascade (FLOW-3.02) precondition absent |
| ES-LIQ-05 | **CCY-basis widening** — USD/JPY 3M xccy basis = USD funding stress for Japanese institutions | >−60bps / >−75bps / >−100bps | ⚠️ terminal-gated (Bloomberg); free proxy = none clean — reason from SAM's USD/JPY + MOF flow reads, do not fabricate a print | On SAM repat/JGB escalations; else at TIC windows | Japan repat pressure NOT converting to a dollar squeeze → SAM's orderly-grind read (JGB floor ~4.0%, ALM-buyer base) corroborated from the funding side |

**Standing read (2026-07-11, registration):** all 5 = **QUIET-EXPECTED** — the calm is *consistent* with the current posture (X1 both-halves failed, funding clean: SOFR−IORB −12bp / SRF $0 / reserves $3.099T [as-of Wed 7/8]). Quiet here + HY >280 later would be the KB-LIQ-074-flagged anomaly (signal fires while plumbing never confirmed) — that combination is itself reportable.

## ★ REVIEW 2026-08-24 — first review since registration. Two bands and two SOURCES were wrong; one nearly produced a false 🔴.

*(Opened on the PAT-060 queue. Registered 7/11 with the bands **"carried from the legacy doc, restated without re-derivation"** and an explicit instruction to **re-validate before acting on a first fire.** That instruction is the only reason this review produced a correction instead of an alert.)*

### 🔴 ES-LIQ-04 — band RE-DERIVED (the registered one is unusable)

| | registered | reality |
|---|---|---|
| ORANGE | >$50B | **exceeded in 111/111 weeks (100%)** |
| RED | >$60B | **exceeded in 107/111 weeks (96%)** |
| | | **2-yr minimum = $54.1B — above the ORANGE line** |

**Distribution, `PDFTD-USTET`, n=111 weekly, 2024-07-03 → 2026-08-12 (US$mm):** min 54,116 · p25 75,017 · **median 89,587** · p75 102,245 · p90 128,923 · p95 197,018 · **max 290,520 [2025-12-17]**.

**RE-DERIVED BANDS (regime-appropriate, adopted — this file owns them and its own rule says re-derive or FREEZE, never silently keep):**
> **🟡 >$129B (p90) · 🟠 >$197B (p95) · 🔴 >$250B**, each requiring **≥2 consecutive weekly prints.**

⚠️ **Two caveats I am not resolving by assertion.** ① **The persistence leg is carried over from GATE-LIQ-079's backtest logic** (one-week spikes are settlement artifacts that reverse) — it is **mechanistically motivated, not fitted**, and it has **not** been backtested here. ② **The $290.5B max [2025-12-17] is mid-December and may be a year-end/settlement artifact rather than stress** — and **GATE-079 taught me the opposite lesson applies too** (Sep-2019 proved funding seizures happen *on* calendar dates, so "calendar artifact" reasoning pushed one step too far deletes the event class). **Flagged, deliberately unresolved: a p95 band anchored to a possible calendar spike is the weak point of this re-derivation.**

### 🔴 Two registered DATA SOURCES do not carry what the rows claim

- **ES-LIQ-04** said *"NY Fed primary-dealer fails data (weekly Thu, free)."* **The `-FDT`/`-FRT` series family in that API is agency-MBS ONLY — all 20 of them. UST fails are `PDFTD-USTET` / `PDFTR-USTET`, a different key family my own suffix scan missed.** ✅ **Positive-controlled before banking it:** the API returns **1,539** series and 20 fails series, so the endpoint works — the gap was real and specific, not a broken tool. **Corrected source: `PDFTD-USTET` (deliver) / `PDFTR-USTET` (receive), NY Fed PD, series break resolved at runtime.** ⚠️ **A stale break returns a 200 whose data stops mid-2024, and a mis-cased key returns an EMPTY 200 — both hit me tonight** (BOND's `fr2004_fetch.py` documents them).
- **ES-LIQ-02** said *"DTCC sponsored-repo volumes (⚠️ OFR mirror of FICC HFM series)."* **The OFR `repo` dataset has DVP / GCF / tri-party and NO sponsored series.** ⇒ **the registered mirror does not exist there.** **Row marked SOURCE-UNVERIFIED.** ⛔ **I did NOT substitute DVP total volume for it** — that is a different instrument, and swapping one in silently is exactly the error this desk keeps logging. DVP is recorded above as *episode context*, explicitly not as ES-02.

### Standing read, refreshed
**ES-01 QUIET (first movement flagged 7/23 — FHLB Chicago advances +16% to $71.1B with insurers named as co-driver; the Office of Finance COMBINED Q2 pull is STILL OWED and 1 district of 11 cannot grade the row).** **ES-02 SOURCE-UNVERIFIED.** **ES-03 unchecked this pass.** **ES-04 QUIET on the re-derived bands** ($108.0B = p78, well under the new 🟡 $129B). **ES-05 terminal-gated, unmeasured.**

---

## Response protocol (any band fires)

1. **Y:** log here + STATUS Open Monitors row; no routing.
2. **O:** route — ES-01 → REGINALD; ES-02/03/04 → check the basis-trade unwind cluster together (they are one cascade: MMF pulls → sponsored repo shrinks → FTDs spike), alert PROME + HENRY; ES-05 → SAM.
3. **R:** treat as HOURS-speed (FLOW-2.02 cascade); alert PROME immediately; cross-check SRF/SOFR-dispersion same session.
4. Any TWO of ES-02/03/04 at O+ simultaneously = basis-unwind signature → 🔴 to PROME/REGINALD/HENRY even if each is individually sub-R.

## Resolved / fired log

| ES-ID | Date | Band | Outcome (APPEARED / DID_NOT_APPEAR by review) | Notes |
|-------|------|------|-----------------------------------------------|-------|
| **ES-02/03/04 (cluster)** | **2026-08-24** | — | 🟢 **DID_NOT_APPEAR — episode: "HY 7/23→8/03 excursion to 287bps"** | **The first absence-is-data record this tracker has ever carried, and it is 43 days late.** The tracker's own rule 3 says *a stress episode that resolves without these firing gets logged* — **the episode opened and closed inside the gap and nobody wrote it down.** MEASURED, not asserted: **DVP repo volume was FLAT-to-HIGHER through it** ($2.79T [7/20] → $2.85T [7/29] → $2.85T [8/05]; range since 6/1 $2.72–3.45T, mean $2.87T; the 7/31 $3.16T print is month-end) — **no repo-capacity contraction during a 19bp HY widening.** UST fails ran 92.3 → **61.2 [7/29]** → 88.4 → 108.0 — i.e. fails **FELL to a window low in the week HY peaked.** ⇒ **The credit widening had NO funding-side signature.** Corroborates KB-LIQ-091 (68–84% broad DM beta) from an instrument that shares no input with it. *(Basis: OFR `-P` preliminary vintage — the `-F` final ends **2026-03-31**, a ~5-month lag; do NOT mix vintages.)* |
| **ES-LIQ-04** | **2026-08-24** | 🔴 **BAND DEAD — NOT a fire** | ⛔ **NO FIRE LOGGED. The band is uncalibrated and would read RED continuously.** | **This is the row the "re-validate a band before acting on a first fire" warning was written for, and it just earned its keep.** `PDFTD-USTET` = **$108.0B [8/12]**, which is >$60B and would have routed a false 🔴 to PROME/REGINALD/HENRY. **But the registered ORANGE >$50B is exceeded in 111 of 111 weeks (100%) and RED >$60B in 107 of 111 (96%). The two-year MINIMUM is $54.1B — above the ORANGE line.** A band exceeded in 96% of weeks is not a threshold. **$108.0B is the 78th percentile — elevated, ordinary, not a signal.** |

## How to use

1. Check the table when the owning cadence says so, or when any stress window opens (catalyst docket).
2. A band fire → response protocol above + a row in the fired log.
3. A stress episode that RESOLVES without these firing → log DID_NOT_APPEAR with the episode name — that's the absence-is-data record.
4. Review bands at each STATUS spine refresh; a band that no longer maps to a live threshold gets re-derived or the row FROZEN, not silently kept.
