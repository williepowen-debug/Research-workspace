---
signal_id: SIG-W-20260706-001
dispatched: 2026-07-06T18:20:00Z
origin: RESEARCH-INTAKE lane (edgar_8k feed, 2026-07-06) — EGBN 8-K filed 2026-07-06, items 5.02 + 9.01, flagged severity=red by item-code heuristic; substance pulled from SEC primary by WALTER
source: "SEC 8-K, Eagle Bancorp Inc (EGBN), CIK 1050441, accession 0001050441-26-000083, filed 2026-07-06 (event 2026-06-29), Item 5.02(d): https://www.sec.gov/Archives/edgar/data/1050441/000105044126000083/gnw-20260629.htm"
source_tag: RESEARCH-INTAKE
signal_type: catalyst
domain: BANK_EARNINGS
cluster: BANK_COLLATERAL
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
event_window: closed
precedence: PRIORITY
to: [REGINALD]
info: [RED]
confidence: 0.90
verify_verdict: CONFIRMED-with-CORRECTED-FRAMING 0.90 (SEC primary, WALTER, 2026-07-06). Event CONFIRMED verbatim from the 8-K. CORRECTED-FRAMING on the intake-lane severity: the item-5.02 RED "critical 8-K" flag is item-code-heuristic — the actual substance is the formal completion of a PREVIOUSLY-ANNOUNCED, planned CEO succession (board-seat appointment for an incoming CEO), NOT a distress / for-cause / surprise departure. Material governance for a watched CRE-concentrated regional bank; not a crisis event.
verify_method: WALTER pulled the 8-K body directly from SEC EDGAR (User-Agent header; the intake-lane feed carries only ticker/items/severity). CIK 1050441 confirmed = EAGLE BANCORP INC (Nasdaq: EGBN, State Commercial Banks); the "gnw-" document prefix is EGBN's EDGAR filename convention, not a mis-map.
routing_note: >
  Eagle Bancorp (EGBN) — a DC-metro, CRE-concentrated regional bank in REGINALD's cohort — has a NEW President & CEO effective TODAY (7/6). Per the 8-K (Item 5.02(d)): on 6/29/26 the board, on the Governance & Nominating Committee's recommendation, appointed Stephen R. Curley to the boards of Eagle Bancorp + EagleBank effective 7/6, "in connection with his previously announced position as President and Chief Executive Officer" of the Company and the Bank, also effective 7/6. No extra board comp; no related-party transactions; no special selection arrangements. FRAMING: this is the board-seat formality COMPLETING a previously-announced, planned succession — NOT a distress/for-cause departure (don't over-read the intake-lane RED severity flag, which is item-code-driven). REGINALD (action): (1) EGBN has new leadership as of today — new-CEO risk = potential shifts in CRE workout posture / reserve philosophy / capital plan into the Q2-print window; (2) reconstruct the full transition from the prior 5.02s (EGBN filed 5.02s on 3/18/26 and 5/12/26 as well — a leadership-refresh cycle, the 5/12 filing likely being the "previously announced" CEO appointment); (3) EGBN was the lone "cosmetic outlier" in your cohort NCO decomposition — a governance overlay on that read. RED (info): framing-corrected governance datapoint.
---

# EGBN (Eagle Bancorp) installs a new President & CEO — Stephen R. Curley, effective 7/6 — planned succession completing (not a distress departure)

Surfaced by the **RESEARCH-INTAKE lane** (edgar_8k feed, 2026-07-06) as a severity-RED critical 8-K (Item 5.02); **substance pulled from the SEC primary by WALTER** and framing-corrected.

## What the 8-K says (CONFIRMED — SEC primary)
Eagle Bancorp, Inc. (Nasdaq: **EGBN**), 8-K filed **2026-07-06** (event **2026-06-29**), Items **5.02 + 9.01**:
> "(d) On June 29, 2026, the Board of Directors … of Eagle Bancorp, Inc. … upon the recommendation of the Governance and Nominating Committee …, appointed **Stephen R. Curley** to the boards of the Company and the Company's wholly owned subsidiary **EagleBank**, effective **July 6, 2026**. Mr. Curley's appointment to the boards is in connection with his **previously announced position as President and Chief Executive Officer** of the Company and the Bank, also effective July 6."

No additional board compensation; no Item 404(a) related-party transactions; no special selection arrangements. Item 9.01 = cover-page XBRL only.

## Framing — corrected
The intake lane flags any Item-5.02 8-K severity **RED / "critical"** by item-code heuristic. The actual substance here is the **formal completion of a planned, previously-announced CEO succession** — the board-seat appointment for an incoming CEO whose appointment was already disclosed. **This is NOT a distress, for-cause, or surprise departure.** It is, however, genuine governance for a watched CRE-concentrated regional bank.

## Why it routes (REGINALD — action)
- EGBN has **new leadership as of today.** New-CEO risk = potential shifts in CRE workout posture, reserve philosophy, and capital plan heading into the Q2-print window.
- **Reconstruct the full transition** from the prior 5.02s — EGBN also filed Item-5.02 8-Ks on **3/18/26** and **5/12/26** (the 5/12 filing, items 5.02+7.01+9.01, is the likely "previously announced" CEO appointment; 3/18 may be the prior-CEO departure). A leadership-refresh cycle at a stressed-tier regional bank.
- EGBN was the **lone "cosmetic outlier"** in your cohort NCO decomposition (STATUS 6/08) — a governance overlay on that read.

## Per-recipient
- **REGINALD (action):** update the EGBN line — new President & CEO Stephen R. Curley effective 7/6; characterize the succession + any strategy/reserve/capital implications; route with the "planned, not distress" frame.
- **RED (info):** framing-corrected governance datapoint (intake RED item-code → planned succession).

## Caveats
- The intake-lane feed carries only ticker + item-codes + a heuristic severity; the **substance and the framing correction are WALTER's from the SEC primary.**
- The 5/12 and 3/18 5.02s were not pulled here — REGINALD to reconstruct the full transition if it wants the complete leadership-change picture.
