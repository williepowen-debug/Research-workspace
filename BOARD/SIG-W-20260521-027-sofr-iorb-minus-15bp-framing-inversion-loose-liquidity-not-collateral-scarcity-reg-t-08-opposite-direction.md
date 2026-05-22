---
signal_id: SIG-W-20260521-027
precedence: PRIORITY
timestamp: 2026-05-22T03:00:00Z
source: WALTER
origin: "Will Telegram image-batch 2026-05-22 02:17 UTC msg 1928 (@amital13 'Amit Noam Tal' X post 5/21/26); REGINALD/registry/THRESHOLDS.tsv REG-T-08 spec (SOFR-IORB > +15bp sustain=3); NY Fed SOFR reference rates primary `https://www.newyorkfed.org/markets/reference-rates/sofr`; FRED IORB primary; Fed Notes 2025-01-31 ample-reserves indicator framework"

to: REGINALD (ACTION)
info: LIQUID, CARL, RED, NEXUS, PROME

signal_type: pattern-match
confidence: 0.55
confidence_language: corrected_framing
resources: 0.05
safety_net: clear

word_count: ~280

cluster: FED_FRAMEWORK
cluster_secondary: BANK_COLLATERAL
signal_role: counter_evidence
event_window: closed

verify_research_verdict: CORRECTED-FRAMING (sub-agent verify 2026-05-22 02:17-02:30 UTC ~$0.05; agent_id a49f3e4a18019a485; FRED convention SOFR-IORB > 0 = stress direction; Amit Tal's "-15bp = collateral scarcity" is INVERTED; REG-T-08 state OPPOSITE-DIRECTION loose-side ~30bp from trigger)
mark_context: SOFR ≈ 3.51% (5/19 print) / IORB = 3.65% (set 12/11/25) → SOFR-IORB ≈ -14 to -15bp under FRED convention. Negative spread = SOFR BELOW IORB = ample-reserves regime, NOT stress.
---

# SOFR-IORB = -15bp Framing INVERSION — Loose-Liquidity / Excess-Reserves Regime, NOT "Collateral Scarcity"; REG-T-08 State OPPOSITE-DIRECTION ~30bp From Trigger

**Event (@amital13 5/21/26 X post + verify-research):** Amit Noam Tal X post claims "SOFR-IORB = -15bp... largest negative spread since September 2022... 25% of repo transactions clearing below 3.50%... system choking on collateral scarcity." Secondary: "Fed will be forced to drain liquidity through the RRP."

## Substance + framing correction

- **The directional framing is INVERTED.** Under FRED convention (the standard, and the one REG-T-08 uses), SOFR-IORB > 0 = stress (SOFR above IORB = cash demand crushing collateral supply, Sept 2019 +315bp peak). SOFR-IORB < 0 = ample-reserves / loose-liquidity regime — SOFR drifts BELOW IORB because abundant reserves mean cash searches for yield via RRP floor.
- **Current state (verify-research 5/21):** SOFR ≈ 3.51% / IORB = 3.65% → SOFR-IORB ≈ **−15bp on the LOOSE side**. NOT stress. The numbers Amit cites are plausibly correct; his sign-interpretation is OPPOSITE of canonical.
- **REG-T-08 trigger state:** OPPOSITE-DIRECTION. Threshold is `SOFR-IORB > +15bp sustain=3 = LIQUID-FHLB-SPIKE`. Current is ≈ -15bp = ~30bp away from trigger on the loose side. Not near-trigger. Not approaching. Loose-side.
- **Mechanic error in secondary post:** RRP DRAINS reserves (Fed accepts cash, releases collateral). The collateral-providing tool is the Standing Repo Facility (SRF). A negative SOFR-IORB is consistent with RRP usage rising naturally as cash seeks the floor — that's a SYMPTOM of ample reserves, not a CURE for scarcity. Amit conflates the two.
- **Sept 2022 historical comp:** Sept 2022 was balance-sheet-runoff with normal negative SOFR-IORB spreads. Using it as a "stress benchmark" is misframed; it was ample-reserves-regime normal.
- **Why dispatch anyway:** the headline is circulating on X and could propagate the inverted-sign framing into broader discourse. WALTER's role is to put a corrected-frame on the BOARD so REGINALD / LIQUID / RED inherit the precision rather than the inversion. **Substance-side: ample-reserves regime PERSISTS — this is the bull-counter / loose-liquidity-still-alive datapoint, not the stress-confirmation Amit's tweet implies.**
- **Source-credibility:** @amital13 = generalist X commentator; no published money-market specialist affiliation.

## Routing rationale

REGINALD ACTION (THRESHOLDS.tsv owner + bank-stress framework integration). LIQUID INFO (HEARTBEAT plumbing context per REG-T-08 recipient chain). CARL INFO (Fed-framework macro). RED INFO (auto-cc CORRECTED-FRAMING per ROUTING_TABLE v0.7 By Tag/By Verdict). NEXUS / PROME standard.

## Falsification scan

REG-T-08 does NOT fire. State is OPPOSITE-DIRECTION, ~30bp from threshold on loose side. No log append.
