# POSITION RECONCILE — 2026-06-10 (Fidelity CSV, downloaded 3:52 PM ET)

**Source:** `Portfolio_Positions_Jun-10-2026.csv` (Will-provided, Session 17). Supersedes the 5/21 CSV as RED's position ground truth.
**Mark caveat:** "Last Price" on illiquid options = last trade, can be stale intraday. WAL $85P last $3.80 vs $3.18 intrinsic (~$0.62 time) is plausible; treat dust marks as indicative only.
**Account shape:** IRA total ≈ $40.7K. **Cash $26,468 = 65.1%** — the account is now mostly de-risked. AAPL 25 sh $7,305 = **17.96%** (below the 20% VX-RED-016 line → vector flip CONDITION MET). Options book ≈ $5.9K market value across ~45 lines.

---

## JUN 18 CLUSTER (T-6) — the decision set

| Position | Qty | Last | Value | Cost | P/L | Read |
|---|--:|--:|--:|--:|--:|---|
| **WAL $85P** | 1 | $3.80 | **$380** | $591 | −35.7% | **ITM $3.18 intrinsic + ~$0.62 time. THE live salvage decision — 54% of recoverable Jun-18 value.** |
| **TLT $85P** | 3 | $0.49 | **$147** | $245 | −40.0% | **ATM (TLT 84.91). ROUND-TRIPPED from +92.2% on 5/21** — the "best trade in stack" gave it all back as 10Y fell to 4.47 then only partially re-rose. Catalyst path live: 30Y ~5.0%, FOMC 6/17 pre-expiry. +16.7% today. |
| WAL $77.5P | 1 | $0.45 | $45 | $551 | −91.8% | Dust+ |
| IWM $257P | 1 | $0.47 | $47 | $939 | −95.0% | Dust+ (+17.5% today on the red tape) |
| EGBN $25P | 1 | $0.30 | $30 | $157 | −80.9% | Dust |
| FITB $45P | 2 | $0.10 | $20 | $181 | −89.0% | Dust |
| WAL $67.5P | 2 | $0.09 | $18 | $981 | −98.2% | Dust |
| **HYG $75P** | 8 | $0.02 | $16 | $245 | **−93.5%** | Dead. **Closure write-up input: $245.39 → ~$16, HYG 79.49 vs $75 strikes.** |
| WAL $65P | 1 | $0.10 | $10 | $450 | −97.8% | Dust |
| ARES $95P | 1 | $0.10 | $10 | $803 | −98.8% | Dust |
| APO $100P | 1 | $0.05 | $5 | $771 | −99.4% | Dust |
| KRE $60P | 1 | $0.04 | $4 | $266 | −98.5% | Dust |
| AAL $10P | 2 | $0.01 | $2 | $179 | −98.9% | Dust |
| *USO Jun12 $155C* | 1 | $0.08 | $8 | $1,008 | −99.2% | *Expires in 2 days* |

**Jun-18 cluster total value ≈ $734, of which WAL $85P ($380) + TLT $85P x3 ($147) = 72%.** Dust legs sum ≈ $207.

## SOFI / OWL JUN 5 — RESOLVED-GONE
Absent from CSV → positions terminated at/before 6/5 expiry. Exact outcomes (expired vs closed, final value) still unconfirmed — Will confirm when convenient. Docket row updated from resolved-unverified → resolved-gone.

## JUN 30 CLUSTER (T-20)
IWM $250P $77 (+33% today) · KRE $67P $27 · KRE $65P x4 $44 · KRE $63P $3. Total ≈ $151 — effectively dust unless KRE breaks <$67 fast (KRE 71.58).

## JUL 17 (T-37) — Q2-print-adjacent
CCL $25P x2 **$274 (+47% TODAY — war/oil leg pricing into cruise fuel-cost victims)** · DIS $90P x2 $110 · FLG $13P x3 $45 · ZION $57.5P $30 · WAL $65P $20 · OZK $42.5P x2 $20 · AAL $10P $4. OZK Thread-3 Jul roll now $20 vs $203 cost (−90%) — Q2 pre-announce is its only path.

## AUG-DEC STRUCTURAL CORE (survives)
| Bucket | Lines | Value |
|---|---|--:|
| OZK Aug (IQHQ vehicles) | $45P x4 $320 + $42.5P $50 | $370 |
| KRE structural | Aug $60P x3 $165 · Sep $60P x2 $178 · **Dec $60P x7 $1,120** | $1,463 |
| WAL Sep (V2.2 horizon) | $70P $205 + $67.5P $160 | $365 |
| **Duration bear (4 vehicles now)** | TLT Sep $85P x2 $422 · TLT Oct $82P x2 $236 · **TBT 14sh $508 (+4.7%, NEW)** · (TLT Jun18 expiring) | $1,166 |
| APO Dec $95P | 1 | $220 |
| HBAN Oct $16P x4 | | $280 |
| KELYA Aug $7.5P | 1 | $75 |

## NEW SINCE 5/21 (not in RED's prior view)
**TBT 14 sh** (duration bear via shares — no theta), **TLT Oct $82P x2**, **XLE Sep $65C x2** ($272, **+36% today**), **CCL Jul $25P x2** (+47% today), **USO Jun12 $155C**, **CF Jun $130C**, **KELYA Aug $7.5P**. Pattern: vehicle migration toward **war/oil expressions (XLE/USO calls, CCL puts) + duration-bear-without-theta (TBT)** — consistent with the ML-RED-067/072 channel-migration lesson. Today's only green in the book IS the war/oil leg (CCL +47%, XLE +36%, IWM +33%, TLT +17%) while every bank put bled — position-level confirmation of ML-RED-080.

## RECONCILE DELTAS vs RED 5/21 VIEW
1. **TLT Jun $85P x3: +92.2% → −40.0%.** Full round-trip; "best trade in stack" no longer true. STATUS corrected.
2. **Cash 65.1%** (was ~$2.5K in Feb records) — major de-risking happened between CSVs; portfolio-vulnerability framing changes: the book is now small relative to cash, theta bleed is bounded, and the structural core (Aug-Dec) is the real position.
3. **AAPL 17.96% < 20%** → VX-RED-016 flip condition met (was 20.08% at S16 audit).
4. SOFI/OWL gone (above). HYG confirmed dead at $0.02.
5. WAL Jun $85P $7 (5/21) → $3.80 — WAL's rally from sub-$76 to $81.82 cost the put ~$320 while the thesis (Q2/MI3) never got to print. Timeline-vs-instrument mismatch, again.

---

## JUN-STACK DECISION MENU (for Will — backstop 6/11, pre-registered NOW, not improvised on the day)

**A. WAL Jun $85P x1 ($380, ITM).** Three catalysts (BOJ 6/16, FOMC 6/17, live Iran) land BEFORE 6/18 expiry; time premium is only ~$0.62 for that bridge.
   - A1 (lock): sell at ≥$3.50 — banks keep rallying, take the $380 before it decays toward intrinsic-minus.
   - A2 (bridge): hold through FOMC 6/17, exit 6/17 PM / 6/18 AM regardless of outcome. Costs ~$0.62 time + WAL-rally risk (~$100/per-$1 WAL move); pays if Iran/FOMC cracks the tape.
   - RED lean: **A2 only if the war leg is still live on 6/16; otherwise A1 on any WAL red day before then.** A 25%-of-cost recovery question, not a thesis question.
**B. TLT Jun $85P x3 ($147, ATM).** 30Y at 5.0%, auction pressure, hawkish-dot risk 6/17 — the one Jun-18 line with a genuinely live catalyst path. Cheap to hold ($147 at risk), binary into FOMC. RED lean: **hold through 6/17** — but acknowledge this is the same "one more catalyst" reasoning that rode it from +92% to −40%. The Sep/Oct/TBT legs already carry the duration thesis; this is now a lottery ticket, treat it as one.
**C. Dust sweep (~$207 across 11 Jun-18 lines + USO 6/12).** Sweep on any green-tape bid day or let expire — immaterial either way; prefer sweep where bids exist to clean the book.
**D. HYG x8** — dead; formal closure write-up owed by 6/18 (RED drafting).

*All position changes are Will's call — this menu is pre-registration, not execution.*
