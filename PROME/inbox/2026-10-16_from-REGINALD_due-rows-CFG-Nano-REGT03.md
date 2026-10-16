# REGINALD → PROME — 2026-10-16 due rows: D:L620 CFG grade · D:L516 Nano · REG-T-03 count · L0 drain · REG-07 VOID + successor draft

**Spawn:** prome-ac, WQ-184 L0, Tier 1, $0. Runtime: Claude Code, Opus 5.5 (subagent). Report: `AGENTS/REGINALD/reports/2026-10-16_due-rows_CFG-Q3-grade_Nano_REG-T-03.md` (commit `844abc79d`). Prices/spreads live (FRED API 13:38 ET; yfinance). No score, threshold, gate letter or trade moved.

| Item | Result | Basis |
|---|---|---|
| **D:L620 CFG Q3** | **INCONCLUSIVE** (leans DOWN) | 8-K acc 0000759944-26-000206 (release, supplement p.6, deck). IB cost 2.13% (+5bp, need ≥2.18%) · avg NIB $40.57B (+1.7%) · NIB 22% · **FHLB $7.613B (+32%) = the only F leg** · cap-call + PC $15.0B deck basis (< $15.46B; INFERRED comparable) · NII +2.7% inside the 2.5–3.5% guide. **Your named line — unfunded non-bank commitments ≈ drawn ($22.5B) — is NOT PRINTED** in release/supplement/deck → grades at Q3 10-Q / 11/07 Call Report. Separate facts: TCE 7.2% → 6.7%; NCO 37bp stable; DLIC $450M revolver not mentioned. Call transcript NOT read (Quartr needs auth) → FHLB-build motive UNKNOWN. |
| **D:L516 Nano P&A** | **NOT POSTED** | 13:37–13:38 ET 10/16: FDIC Nano page (HTTP 200, last updated 10/8) lists Bid Summary only; alt URL 404; failed-bank CSV no link. 21 days after closing. Propose re-check Tue 10/20; DEWEY 10/27 escalation stands. Retained-pool scenario (≈$70–90M) unchanged. |
| **REG-T-03** | **2-of-3** | FRED HY 325 [10/14], 323 [10/15] (316 [10/13] reset). 10/16 close publishes ~Mon 10/19 AM: **>320 ⇒ CREDIT-CANARY-FIRED** (REGINALD action / CARL info), recorded with the cross-check beside it, never as bank transmission by itself; **≤320 ⇒ reset to 0-of-3**; exit after a fire = ≤300 ×5. **Cross-check (10/13→10/15): BANK-ABSENT, ~0.7** — BB +3.1% leads, CCC +0.9% last (rate signature after hot CPI/PPI); 10-name bank preferred basket mean +0.06%; KRE +1.0%. OZKAP −1.26% is the one bank-specific mover, 4 sessions before OZK's 10/20 print. RED's AI-levered composition caveat cited, not re-derived. CCC/HY 3.96× (HY-led). |
| **Failures count** | **6, unchanged**; -013 discarded | FDIC CSV re-pulled 13:38 ET; none after 9/25. The 4th 2026 failure really is a Kansas bank (Small Business Bank, 7/17) — likely why the 2023 article looked current. |
| **D:L731 REG-07** | **VOID encoded** (`workbook/PREDICTIONS.tsv`) | Will's tap verified at `PROME/proposals/2026-10-15_deck-batch-16-RULED.md` row 412. Successor draft below. |

## REG-07 successor — DRAFT for Will's word (unregistered; please open a WQ row before SSB prints Wed 10/21 AMC)

- **Proposed REG-27:** SouthState (SSB) "Nonperforming loans as a percentage of period end loans" (8-K EX-99.1 asset-quality table) **prints ≥ 0.70%** at any quarterly release Q3-2026 through Q2-2027. **Crossing:** up through 0.70% from 0.54% [6/30/26]; 0.70% sits 7bp above the series' 5-quarter high (0.63%), so a TRUE needs a new high, not noise.
- **Base rate (thin, stated):** SSB series at primary 0.63 [6/30/25] / 0.63 / 0.62 / 0.61 / 0.54 [6/30/26] — 0 of 5 quarters ≥ 0.70%; the 4 QoQ moves were 0.00 / −0.01 / −0.01 / −0.07pp; TRUE needs +0.16pp within 4 prints. History before 6/2025 NOT pulled (n=5 is the whole base). **Proposed confidence 15%.**
- **FALSE** if no print ≥ 0.70% through the Q2-2027 release. "From substandard" is recorded if SSB attributes it, not required. Graded on the release; confirmed at the 10-Q.

## L0 drain — 46 of 46 logged (every sender)
25 top-level → `inbox/processed/.consumed.tsv` (ACTED 5 · ACTED-PRIOR/INTEGRATED-PRIOR 7 · INTEGRATED 3 · INFO_ONLY 6 · NO-OP 2 · DEFERRED 3: CARL fintech fields ×2 → 10/26, RED CET1/AOCI → 10/23). 21 WALTER → `board/BOARD_LOG.tsv`. ⚠️ 4 WALTER handoffs (-20261015-005, -20261016-019/-020/-025) are **untracked WALTER deliveries** — logged consumed, files left in place until WALTER commits them. 7 correction receipts written, check rc=0. Packets: WALTER (holiday rule CONFIRMED + -025 answer), BROCK (CFG NDFI basis), GIBBS (Q3 read locations) — `70c048a8a`.

## ⚠️ For PROME (owner flags, no edits made)
1. **REG-T-06 instrument discrepancy:** the letter names the FHLB **Combined Financial Report** (Q3 = 11/13), but the Q2 $810.7B leg was graded from the **Combined Operating Highlights** (7/30). Whether the 10/30 Highlights may grade leg 3 is an instrument question for Will; as written, leg 3 waits for 11/13.
2. **HBAN puts expire today Fri 10/16** (REGINALD MEMORY item 4, WQ-302) — no fill on file at my desk; not actioned here (no trade authority).
3. Weekly H.4.1/H.8 funding read (MEMORY item 1) NOT run — outside due-row scope.

## COMPLETION — REGINALD — 2026-10-16
STATUS: DONE (D:L620, D:L516, REG-T-03 count, L0 drain, D:L731 VOID); PARTIAL (L731 successor = draft awaiting Will)
CHANGED: report 2026-10-16_due-rows; STATUS, MEMORY, CALENDAR, NEXUS_BRIEF, PREDICTIONS (REG-07 VOID), registry/NOTES (non-session rule), BOARD_LOG, .consumed.tsv, corrections_receipts; 3 peer packets
RESULT: CFG INCONCLUSIVE (FHLB +32% only F leg; unfunded $22.5B line not printed) · Nano P&A NOT POSTED 13:38 ET · REG-T-03 2-of-3, cross-check BANK-ABSENT ~0.7 · failures 6 · 46/46 inbox logged · -013 discarded
GAPS: CFG call transcript unread (Quartr auth); 10-Q Table 9 + 11/07 CR confirm N/F; 4 untracked WALTER handoffs unmoved; RED CET1 ask deferred 10/23; H.8 read not run
WILL_NEEDS: REG-27 successor draft (WQ row before 10/21 AMC); REG-T-06 Highlights-vs-CFR instrument call before 10/30
FOLLOW-UP: Mon 10/19 AM grade 3rd HY bar (fire or reset); Tue 10/20 Nano re-check; WAL 10/19 / OZK 10/20 WQ-318 rows
