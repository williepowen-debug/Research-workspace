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

## Response protocol (any band fires)

1. **Y:** log here + STATUS Open Monitors row; no routing.
2. **O:** route — ES-01 → REGINALD; ES-02/03/04 → check the basis-trade unwind cluster together (they are one cascade: MMF pulls → sponsored repo shrinks → FTDs spike), alert PROME + HENRY; ES-05 → SAM.
3. **R:** treat as HOURS-speed (FLOW-2.02 cascade); alert PROME immediately; cross-check SRF/SOFR-dispersion same session.
4. Any TWO of ES-02/03/04 at O+ simultaneously = basis-unwind signature → 🔴 to PROME/REGINALD/HENRY even if each is individually sub-R.

## Resolved / fired log

| ES-ID | Date | Band | Outcome (APPEARED / DID_NOT_APPEAR by review) | Notes |
|-------|------|------|-----------------------------------------------|-------|
| — | | | | |

## How to use

1. Check the table when the owning cadence says so, or when any stress window opens (catalyst docket).
2. A band fire → response protocol above + a row in the fired log.
3. A stress episode that RESOLVES without these firing → log DID_NOT_APPEAR with the episode name — that's the absence-is-data record.
4. Review bands at each STATUS spine refresh; a band that no longer maps to a live threshold gets re-derived or the row FROZEN, not silently kept.
