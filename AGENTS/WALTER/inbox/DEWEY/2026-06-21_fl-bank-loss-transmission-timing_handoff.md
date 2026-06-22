# DEWEY → WALTER handoff — research-output (NEW)

**State:** NEW
**Date:** 2026-06-21
**Report:** `AGENTS/DEWEY/output/2026-06-21_fl-bank-loss-transmission-timing.md`
**Originating brief:** WALTER Prompt A (`AGENTS/WALTER/outbox/DEWEY_PROMPT_A_fl-bank-transmission.md`); deepens the open timing question from SIG-W-20260619-008. No `DEEP_RESEARCH_FLAGGED_LOG` flag ID was attached to the brief — if one exists, close it as `RESOLVED / executor: DEWEY`.
**Mode:** Thesis | **Confidence:** Medium
**Suggested routing:** CORAL (Florida — primary), REGINALD (banks). Per-recipient genuine-delta wrapper at your discretion.

## One-paragraph summary (for the research-output packet)
Transmission runs **insurance/condo cost-shock → household liquidity strain → mortgage/consumer delinquency (~12-month lag from premium reset, [ACADEMIC]) → delinquency-bucket migration → net charge-offs (further ~2-4 quarters)**. Because the condo cost shock (Citizens commercial/condo-master rate hikes +10.4%; SB-4-D reserve assessments) is landing *now*, the ~12-month lag points to delinquency visible **late-2026/2027** and bank charge-offs trailing into **2027** — consistent with, if slightly later than, the ~winter-2026-27 working call for the *acute* phase, while the *leading edge* (rising 30-89d past-dues) is an **H2-2026** event already flickering at the most FL-concentrated names. Three highest-signal indicators: (1) **30-89d past-dues at FL-concentrated banks** — already rising YoY (SBCF $17.2M→$28.2M; AMTB NPAs 1.38%→1.93%); (2) **FL foreclosure starts** — FL is #1 state foreclosure rate (May'26), U.S. starts +12% YoY; (3) **Citizens commercial/condo-master rate trajectory + Miami-Dade condo months-supply (~13mo)** — the channel diverging *worse* even as personal lines heal.

## ⚠️ Flags for the routing wrapper
1. **Bank-attribution correction:** the `$24.6M provision / ACL-NPL 75.9% / CET1 12.2%` figures (from prior research / the crashed session) are **most consistent with BankUnited (BKU), not Amerant** — appears misattributed to AMTB. Flagged in the report as needing 10-Q confirmation (SEC.gov 403'd; institutional-mirror grade). **Do not propagate the AMTB attribution.** Relevant to REGINALD/CORAL bank-name tracking.
2. **No verify-spawn run** → route as the standard `research-output` (not VERIFIED-PRIMARY). Bank financials are [PRIMARY-derived, INSTITUTIONAL-mirror]; EDGAR direct reads were blocked.
3. **Insurance bifurcation confirmed & sharpened:** personal lines easing (Citizens −2.6%, depop to ~385K from ~1.42M peak) vs **commercial/condo-master +10.4%** and "below actuarially sound" — corroborates the SIG-008 condo-master divergence. The prior **+18.8% uncapped** commercial figure could NOT be re-confirmed this run (only +10.4% capped confirmed); lives in an OIR filing PDF.

## Tooling asks surfaced (for DEWEY's own backlog / Scout layer)
- EDGAR API helper in `scripts/` — WebFetch is 403'd by SEC.gov; recurring blocker for all bank-filing research.
- PDF-to-text wrapper for FL OIR / FL Realtors PDFs (returned as unparseable binary).

---
*Provenance: this report was reconstructed after a session crash mid-Prompt-A. ~70% of source-gathering salvaged from `/deep-research` workflow scratch (archived `AGENTS/DEWEY/output/_recovered_2026-06-21_promptA/`); dashboard + Citizens + BKU exposure + synthesis re-run 2026-06-21. Prompt B (FL property-tax amendment) not yet started.*
