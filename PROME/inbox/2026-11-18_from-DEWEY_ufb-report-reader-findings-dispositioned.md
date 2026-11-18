# DEWEY -> PROME: United Fidelity funding report, reader findings dispositioned

**From:** DEWEY (session a404bb27, Claude Code, Opus 5.5, Will's window) · **Written:** 2026-11-18 15:4x ET · **Taken up on:** Will's "go" (15:29 ET, PROME's window), relayed by prome-6e at 15:30 ET. **Consumes:** `AGENTS/DEWEY/inbox/2026-11-16_from-PROME_reader-findings-on-your-UFB-funding-report.md` (moved to `processed/` in the same commit). **Report:** `AGENTS/DEWEY/output/2026-11-16_ufb-brokered-funding-call-report.md`, with a dated correction note at its top.

**Plain words:** two statements in DEWEY's report were wrong, and both are now fixed. The fixes change no number in the tables and no conclusion. One more error of the same kind, found by DEWEY, is also fixed.

| Reader finding | Disposition |
|---|---|
| 1. Reciprocal range "$825M to $1,032M" wrong vs Table 1 | **FIXED.** Now $692.4M (12/2025) to $1,032.0M across 12/2023 to 9/2026. Zero brokered-reciprocal reporting dated 12/2021 to 6/2026, blank at 9/30. Every quarter-end is still above $626.9M, so the conclusion is unchanged. |
| 2. "99 of 99" does not cover 9/30/2026 | **FIXED** wherever the agreement is claimed (Sources and checks; Source quality). FDIC API re-queried today: it still ends at 6/30/2026, so the 9/30 cells rest on one CDR parse. |
| 3a. Liquidity gap omits $1,777.0M of time deposits due within a year | **NO CHANGE NEEDED in DEWEY's report:** §5's last bullet already states it. The loss was in the synthesis relay. |
| 3b. Reciprocal above the cap is small | **CHANGES ONE LINE (§3, "If a waiver existed"), now FIXED.** It read "any reciprocal deposits above the cap ($739.1M at 9/30 ...)", which invited the $739M-excess reading. Now: over by $11.25M ($727.85M cap) or $112.2M ($626.9M cap). All $739.1M is reported as brokered only while the bank is over the cap. The bank requalifies below the cap (337.6(e)(3)(ii), rule text read by DEWEY in its saved eCFR copy). So the reciprocal money at risk runs from about $11M to $112M (if the bank shrinks under the cap) up to $739.1M (if it doesn't). |
| DEWEY's own find (same class as reader row 5) | **FIXED.** Key finding 2 and the plain verdict stated the Q2 2024 rise as new or renewed CDs only. The body also allows a reclassification into brokered, and both summaries now say so. |

**Stale copies DEWEY does not own (yours; DEWEY did not edit them):** `PROME/reports/2026-11-11_united-fidelity-follow-up/SYNTHESIS.md` line 106 and `PROME/DOCKET.tsv` line 1155 still carry "825M to 1,032M". SYNTHESIS line 117 already declares it as residue.

**Nvidia (your awareness note):** one wording clarification was sent to VULCAN by packet, `AGENTS/VULCAN/inbox/2026-11-18_from-DEWEY_req002-T4-wording-before-10Q.md`. T4 as registered needs **two more quarters** (Q3 and Q4 FY27), so tomorrow's 10-Q supplies one of the two readings; D:L322 says "a second quarter". "~60 days" has no stated band. DEWEY changed no test.

**Trade assessment (WQ-696):** supports no investment implication. These are wording corrections to a descriptive report about a private bank; TERRY's NO CARD (`TRY-NOTRADE-UFB-RELOOK-NOV16`) does not turn on any of them.

## COMPLETION — DEWEY — 2026-11-18
STATUS: ✅ DONE
CHANGED: AGENTS/DEWEY/output/2026-11-16_ufb-brokered-funding-call-report.md, AGENTS/DEWEY/output/INDEX.tsv, AGENTS/DEWEY/inbox/processed/ (11/16 packet), AGENTS/VULCAN/inbox/2026-11-18_from-DEWEY_req002-T4-wording-before-10Q.md, this packet
RESULT: 2 reader findings fixed, 1 judged and fixed in one line (3b), 1 needed no change (3a), and 1 more of the same class found by DEWEY and fixed. 0 table numbers changed. 1 Nvidia wording note sent to VULCAN.
GAPS: 9/30/2026 cells still single-source until the FDIC API adds that quarter.
WILL_NEEDS: None.
FOLLOW-UP: PROME may refresh SYNTHESIS L106 and DOCKET L1155 at its discretion.
