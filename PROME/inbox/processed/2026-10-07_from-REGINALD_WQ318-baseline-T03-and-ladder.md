# REGINALD → PROME · 2026-10-07 Wed (post-close) · WQ-318 delivered · REG-T-03 graded · ladder at live marks · new Fidelity lines read · inbox drained

**Session:** PROME-spawned (`prome-0e`) DOCKET L527 Tier-1 wake, run as a full REGINALD domain session. Model **Opus** (`desk` agent definition; runtime reports `claude-opus-5-5`). Laptop host; I am the sole live REGINALD writer (WQ-387). The tree carried PROME's own dirty files (`PROME/WILL_QUEUE.md`, `registry/WQ_LEDGER.*`, `state/board_*`). I did not pull or stash and touched none of them. Stamps come from `date`.

## Will-facing items (nothing new needs a ruling from this desk)
- **None new.** Three existing Will items bear on my lines and are already registered elsewhere:
  1. HBAN Oct-16 $16P ×2 is in the money. Will rules by Wed 10/14 (WQ-302). HBAN reports 10/22, after that expiry.
  2. Fills, entry dates and management approval for the two NEW Fidelity bank puts are unrecorded (FORGE D-73/D-74). They need Will's Activity view.
  3. The FFIEC CDR login token (JWT) expires **11/05**, two days before my 11/07 Call Report run that confirms half the WQ-318 Q3 list. Renewal is Will's action.
- **One caveat to carry if the new puts come up with Will.** FORGE says the 10/7 capture is *consistent with* same-session entries, and that is unverified. If both were bought 10/7, that was a red day for both names (WAL −2.29%, OZK −2.29%, KRE −1.68%). Root rule #6 belongs to TERRY; I am reporting the day colour only.

## 1. WQ-318: DELIVERED (DOCKET L527) — `a033c799c`
`AGENTS/REGINALD/reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` · `scripts/wq318_funding_baseline.py` · `workbook/FUNDING_COHORT_2026Q2.tsv` (FFIEC Call Report, 6 banks × 5 quarters, one basis) · KB ML-REG-176..180.
- **Consume-grade checklist:**
  - ✅ both deliverables in one file;
  - ✅ the six banks (CUBI · CFG · WAL · OZK; FLG · EGBN as CRE contrasts) on the 6/30 common baseline, with later disclosures in a SEPARATE column (1h);
  - ✅ August's negative result retained (the 8/14+ selloff did not sort on the private-credit proxy: −0.559 at n=14 → −0.255 at n=26; the 9/15+ leg sorted on SIZE, ρ −0.72);
  - ✅ every rate-sensitivity figure carries its stated assumptions, marked INCOMPARABLE across banks;
  - ✅ UNAVAILABLE fields named (collateral terms at all four NDFI banks; numeric betas at 5 of 6);
  - ✅ Q3 allowed to stay inconclusive.
- **Answer:**
  - **No cheap-deposit flight at 6/30 at any of the six.** The share of deposits paying no interest was flat or up, and interest-bearing deposit costs fell 27–52bp over four quarters.
  - **The two exposures sit in different banks, and CUBI is the only one high on both.** On the non-bank-draw side: non-bank loans are 34.1% of CUBI's loans and the private-credit slice 19.96%; its interest-bearing deposit cost of 3.54% is the highest of the six; its Federal Home Loan Bank (FHLB) advances are up 72% in a year. On the deposit-fragility side: brokered deposits are 21% and uninsured deposits 44%.
  - **Unfunded non-bank commitments ≈ drawn balances at CFG ($22.5B) and OZK ($3.3B).**
  - **Every bank's own model has net interest income rising with rates, but the figures are not comparable.** FLG's short-rate-only scenario has the opposite sign.
- **Pre-committed Q3 list** (UP/DOWN/INCONCLUSIVE per bank, with the exact disclosure line), in print order:
  - **CFG Fri 10/16** (call 09:00 ET);
  - **WAL Mon 10/19 after the close** (call Tue 10/20 12:00 ET);
  - **OZK Tue 10/20 after the close** (call Wed 10/21 08:30 ET);
  - **EGBN Wed 10/21 after the close** (call Thu 10/22 10:00 ET; company IR 10/7);
  - **FLG and CUBI: NOT ANNOUNCED** (10/7).
  - Same week, for my other registered rows (issuer text, verified 10/7): **VLY Thu 10/22 before market** (L521) · FL rail **BKU Wed 10/21 before market · SSB Wed 10/21 after close · AMTB Thu 10/22 after close · SBCF Tue 10/27 after close** (L227; the 10/9 date deadline is discharged).
  - **Register on delivery (the L527 row asks this):** please register the CFG 10/16 and CUBI (date TBA) grading rows. WAL L170 · OZK L520 · EGBN L35 · FLG L522 already exist.
- **Order kept:** the 9/27 skipped write-backs (MEMORY 0-WB) were done FIRST (`ffc713c55`: KB +6, matrix §3e notes, ROADMAP threads, VLY Q1 brief bannered STALE).
- **BROCK's L494 named-facility answer was consumed:**
  - one tightened facility (JPMorgan's revolver to FSK; none of my six is the lender);
  - the counter-case at the same depth (lines to ARCC expanded);
  - no attributable bank loss.

## 2. REG-T-03 (HY sustained-3) — graded on MY letter: **0-of-3, NOT FIRED**
Letter (`registry/THRESHOLDS.tsv`): FRED `BAMLH0A0HYM2` > 320 on **3 consecutive daily closes**. Own pull 2026-10-07 21:47 ET. The cache-busted fredgraph CSV and ALFRED first-published agree on every cell.

| Obs date | 9/29 | 9/30 | **10/1** | 10/2 | 10/5 | 10/6 |
|---|---|---|---|---|---|---|
| HY OAS | 308 | 312 | **324** | 310 | 312 | 303 |
| Count | 0 | 0 | **1 of 3** | **RESET → 0** | 0 | **0** |

- **Peak run 1 (10/1). Count at the latest published cell (10/6) = 0-of-3.** The 10/7 cell publishes Thu ~10:15 ET.
- B 302 [10/6]. It peaked at 329 [10/1], 1bp under my `VX-REG-18.05` ORANGE line (330).
- CCC 1,214 [10/6]. The 10/1 print of 1,215 is the high of FRED's public window.
- CCC/HY ratio **4.007×**. It rose because high yield TIGHTENED (324 → 303) while CCC held — the denominator form, so **no re-escalation** by `VX-REG-18.04`'s own rule. The 9/26 escalation stands.
- X1 is LIQUID's and stays CLOSED. The bank-credit cross-check caveat stands: a high-yield level is not bank transmission.
- **TERRY's `TRY-COND-KREADD` (the conditional card from Will's 9/29 KRE-put ask) is NOT armed on its REGINALD leg** (packet `db3565b15`).

## 3. Bank ladder at live marks — settled Wed 10/7 closes (yfinance daily bars + Nasdaq historical API, independent routes, agree to the cent; pulled 21:5x ET)

| Name | 10/7 close | Read |
|---|---|---|
| **FLG** | **$11.30** (−2.25%) | 🔴 **`VX-REG-6.03` RED BROKE on this close.** −20.6% vs the frozen $14.24. YELLOW broke 9/16, ORANGE 9/28, RED 10/7. The ladder is exhausted (no band beyond RED). Packets PROME + FLG `018af9846`. Matrix 6 unchanged (price is not an input). Cause UNKNOWN; no FLG 8-K since 7/24 |
| **WAL** | **$74.35** (−2.29%) | `REG-T-02` FIRED (since 9/1). Exit run **0-of-3**, 26 rows in `registry/REG_T02_EXIT_LOG.tsv`; $7.55 / 9.2% short of $81.90. **For TERRY's `GATE-TERRY-ROLL70-EXIT` (TERRY owns it):** closes 9/30 75.10 · 10/1 75.70 · 10/2 76.38 · 10/5 76.02 · 10/6 76.09 · 10/7 74.35 ⇒ **0-of-3**. `GATE-REG-T02` TERMINAL: every sub-$78 close is a SUPPRESSED re-entry. Packet TERRY `fe37dd785` |
| **OZK** | **$43.56** (−2.29%) | −4.31% on 10/6 vs KRE −0.45% (cause UNKNOWN). **Below the OZK desk's own <$45 band on 10/6 and 10/7.** The OZK desk grades it and has been dark since 10/2; signal sent to WALTER for routing (`db3565b15`) |
| KRE | $68.89 (−1.68%) | `REG-T-01` UN-FIRED, 12.9% above $60. Lowest close in my 9/14 → 10/7 series |
- CREED-T-08a is CREED's and stays FIRED; I did not touch it.

## 4. New Fidelity lines in the 10/7 capture — thesis read only (no card; cards are TERRY's)
Basis: FORGE 10/7 (D-74). These are distinct from the Robinhood WAL Dec-18 $70P ×1, and ROLL70's gate does NOT transfer to them. By the seam rule the WAL and OZK legs belong on the WAL and OZK desks' POSITIONS files; I carry pointers only. Distances and vol below are my arithmetic on the 10/7 close and 60-day REALIZED vol (not implied).

**WAL Dec-18 $65P ×4** — 12.6% out of the money; 72 days to expiry; ≈1.2 realized standard deviations. The tenor spans the **10/19 print**, the Q3 10-Q (due by 11/9) and my 11/07 Call Report run.
- **The read: my desk's evidence neither supports nor refutes a WAL-specific move to $65 before the print.**
- WAL is mid-pack (matrix 2). The 9/1 `REG-T-02` fire was a LEVEL event with the mechanism unmoved. The 9/15+ selloff sorted on bank SIZE, not credit.
- What would take WAL to $65 is on the WQ-318 WAL row:
  - interest-bearing deposit cost ≥2.84%;
  - deposit loss beyond the announced ~$4B off-balance-sheet optimization;
  - non-bank loans above 25.9% in a business-credit or PE-fund line (not warehouse);
  - non-bank nonaccruals rising from $122.5M (0.77%);
  - a deposit beta above WAL's own 53–70% assumptions;
  - mid-pack breadth at the 11/07 run (L180).
- Against the put: WAL's own model has net interest income +5.9% per +100bp, the NIB share rose, and deposit costs fell.
- Registered triggers that bear: the WQ-318 WAL row; L180; the AOCI grade at the 10-Q. `REG-T-02`'s exit guards only the Robinhood $70P. The pre-print frame is the WAL desk's (L170). TERRY's TRY-FIRE-002 has its dates locked and stays dormant.

**OZK Nov-20 $40P ×4** — 8.2% out of the money; 44 days to expiry; ≈1.1 realized standard deviations. The tenor spans the **10/20 print**, the FDIC-filed 10-Q (~early Nov) and the Q3 Call Report (due ~10/30).
- **The read: of the two, this strike and date sit closer to registered evidence. OZK is in my CRE top three for investigation.**
  - Foreclosed property rose from $150M to $288.1M in Q2.
  - Reserve coverage falls from 154% to 78% once foreclosed property is counted.
  - OZK carries its foreclosures at 95–100% of appraisal, a mark untested by any sale, while its own Seattle office sold at 58% of appraisal.
  - **The 10/20 print is the first sale-price test of those marks, inside the tenor.** The funding side is the thinnest NIB share of the six (11.6%); management called Q2 an "inflection point" for deposit cost.
- But **no observation has moved since Q2**. The 10/6 drop has no found cause. Short interest is ~16% of float (OZK desk, 9/15 vintage), so a clean print cuts the other way.
- Registered triggers that bear: L520 (the OZK desk's row: foreclosed-property sale prices vs carrying, Boston 10 Prospect, RaDD terms); my CRE top-3 "weakens if" lines and loss-bridge re-run; the WQ-318 OZK row; the OZK desk's <$45 band (crossed) and <$40 band (this put's strike).

## 5. Inbox: WHOLE inbox drained, 14 top-level + 19 WALTER lane → 0 (`d3a60d512`, `consume:REGINALD`)
- **Logs:** `board/BOARD_LOG.tsv` +19 rows (11-column, INBOX_WALTER) and `inbox/processed/.consumed.tsv` +14 rows, each with an evidence path.
- **WALTER ACTIONs done:**
  - -005: REG-T-03 graded.
  - -008/-012 (NYFed private-credit visits): none of my six is named. CFG's remark-trigger private-credit book is the closest analogue. Official confirmation is INDETERMINATE; no gate move.
  - -009 (G.19): the household-borrowing-flow vs bank-metric distinction is kept.
  - -007: WAL Q3 date locked and sent to TERRY.
- **Top-level ACTIONs:**
  - WALTER R3 phrases: both DECLINED by name, because `Nano Banc` is landed (PROME packet `db3565b15`).
  - DAEDALUS: PREDICTIONS header edit made; staleness alert cleared.
  - OZK sub-notes citation moved to ≈+$12.3M/yr.
  - BCB Bancorp: neither a watch-surface name nor a sale comp; the 21.1% is a loss figure, not a price (ML-REG-181).
- **Fire-time flags** (`firetime_check.py --window 7`) on the 9/27 Nano report:
  - 3 DATE flags ('12/23', '12/24', '12/25') are **quarter-end labels** (e.g. [12/24] = 12/31/2024). **KEEP; nothing to re-date.**
  - 1 dead DEWEY pointer, repaired to its repo path.
  - The live Nano fire-time date stays **Fri 10/9** (FDIC P&A check, L516). **Checked early on 10/7: the P&A is NOT POSTED.** The FDIC failed-bank page was last updated 9/29, it has no Transaction Documentation block, and the usual PDF address returns 404. No claims bar date is posted either. Re-check on or after 10/9; forensics §3 stays on its 9/22 basis.
- **Doorbells:** no ListAgents tool is exposed in this runtime. The TERRY and WALTER packets are info/routing and WALTER's lane is file-based. If you see either live, rule 6b says doorbell them.

## 6. Other write-backs
- **Book:** KRE $60P Sep-30 ×2 was **SOLD 9/30 @ $0.01 and rolled into Dec-31 $65P ×2** (Will's own roll). My 9/29 "lapse ruled" pre-read was overtaken. POSITIONS, TRADE and CALENDAR were written back from FORGE, not the tape. New lesson 41: pre-register expiries as sell-or-roll, never lapse.
- **Desk surfaces:** STATUS · CALENDAR · POSITIONS · TRADE · VX (6.03/18.02/18.04/18.05) · ROADMAP (rotated R1–R4, crc-recomputed) · MEMORY (session notes rotated M1–M2, crc-recomputed; 76% → 41% of budget) · SCRATCH · NEXUS_BRIEF folded LAST (`5453ee5ad`).
- **Commits this session:** `ffc713c55` (0-WB) · `018af9846` (FLG RED → PROME, FLG) · `fe37dd785` (TERRY: WAL Q3 lock + ROLL70 read) · `a033c799c` (WQ-318) · `d3a60d512` (inbox drain) · `db3565b15` (PROME R3 / TERRY T-03 arm / WALTER OZK signal) · `5453ee5ad` (closeout) · this memo.

## COMPLETION — REGINALD — 2026-10-07
STATUS: ✅ DONE (WQ-318 delivered 2 days before deadline; all five spawn items done)
CHANGED: reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md, scripts/wq318_funding_baseline.py, workbook/{FUNDING_COHORT_2026Q2,KB,VX,PREDICTIONS}.tsv, registry/REG_T02_EXIT_LOG.tsv, board/BOARD_LOG.tsv, inbox 33→processed, STATUS/CALENDAR/POSITIONS/TRADE/ROADMAP/MEMORY/SCRATCH/NEXUS_BRIEF, BANK_EXPOSURE_MATRIX, archive rotations; packets → PROME×3, FLG, TERRY×2, WALTER
RESULT: WQ-318: no cheap-deposit flight at 6/30 at any of 6 banks; CUBI the only bank high on both legs; Q3 list pre-committed (CFG 10/16 · WAL 10/19 · OZK 10/20 · EGBN 10/21). REG-T-03 0-of-3 at the 10/6 cell (324 [10/1] = 1 of 3, reset 10/2). Ladder 10/7: FLG $11.30 RED broke (packets sent); WAL $74.35, ROLL70 0-of-3 (26 rows); OZK $43.56, below the OZK desk's <$45. Inbox 14+19→0.
GAPS: FLG/CUBI Q3 dates not announced. Collateral terms unavailable at all 4 non-bank lenders; numeric deposit betas at 5 of 6. Call Report deposit cost fails to match company figures at CUBI/OZK/EGBN (cause unresolved). No ListAgents tool, so no doorbells.
WILL_NEEDS: None new. Existing: HBAN Oct-16 puts ruling by 10/14 (WQ-302); Activity view for the new WAL/OZK Fidelity puts (D-73/74); FFIEC JWT renewal before 11/05.
FOLLOW-UP: Register CFG 10/16 + CUBI grading rows (L527 asks it). Grade each WQ-318 row at its print (CFG first). Re-check the Nano P&A on/after 10/9 (L516; not posted 10/7). FL bank Q3 dates are done (L227). Route OZK's band signal if WALTER is dark.
