# PROME → BOND · 2026-08-19 ~13:2x ET · **US 20Y `912810UX4` cleared at 1PM while you were dark. Primitives captured off the TreasuryDirect primary. I did NOT grade it — that is yours.**

**Class:** data capture, owner-dark. **No threshold adjudicated. No gate fired. $0 moved. No composite move, no VX-BND-01 touch.**

**Why this packet exists:** you own both of today's registered events and `ListAgents` showed you dark at 12:1x and again at 13:1x. Will ruled (in-session, 13:1x) **not to scramble a BOND session**, on the reasoning that the FOMC minutes are a *permanent document* — your T7 grade off your frozen text is identical whenever you run it — whereas the **auction result and the market reaction are perishable**. So PROME captured the perishable half and left every judgment to you.

---

## 1. The auction, as pulled

[CONF · TreasuryDirect `TA_WS/securities/search?cusip=912810UX4` · pulled 2026-08-19 ~13:1x ET · TD `updatedTimestamp` **2026-08-19T13:03:18**]

| Field | Value |
|---|---|
| CUSIP / type | `912810UX4` · **Bond, 20-Year, NEW ISSUE** (`tips: No`) |
| Offering | **$16.0B** · single-price |
| Auction date | 2026-08-19 · issue 2026-08-31 · matures 2046-08-15 |
| **High yield** | **5.2040%** |
| Coupon / price | 5.125% · 99.021288 |
| Median yield | 5.147% · low yield 3.880% |
| **Bid-to-cover (TD published)** | **2.53** |
| Total tendered / accepted | $42.476B / $18.057B *(incl. SOMA add-on $2.057B, `somaIncluded: No`)* |
| Competitive tendered / accepted | $40.228B / $15.809B |
| Noncompetitive accepted | $0.191B |
| Allocation % at high | 65.58% |

### Composition — **in YOUR denominator** (% of competitive accepted, per your 7/28 7Y grade and the 8/18 refunding grade)

| Bidder | Accepted | **% of competitive accepted** |
|---|---|---|
| Indirect | $9,947,939,100 | **62.93%** |
| Direct | $3,886,857,900 | **24.59%** |
| **Primary dealer** | $1,974,395,000 | **12.49%** |
| | | sum **100.00%** ✓ |

⚠️ **Basis note, because you have been bitten by exactly this class four times (series·basis·window·counting):** TD's published **2.53** is **NOT** competitive-tendered/competitive-accepted. It reproduces only as `(competitive tendered + noncompetitive accepted) / (competitive accepted + noncompetitive accepted)` = **2.5262 → 2.53**. The competitive-only variant is **2.5446 → 2.54**. **They differ by 2bp of cover.** I am handing you both with the arithmetic so you pick the one your trailing-12 series is built in — I do not know which, and guessing would plant a basis mismatch inside a comparison.

---

## 2. What I did NOT do

- **No grade.** No trailing-12 median/min/max comparison for the 20Y — I do not hold that series, and building it inside a coordination packet is how a desk's benchmark gets forked.
- **No composition-failure call.** The figures above are inputs to your test, not the test.
- **No `VX-BND-01` move, no composite re-score, no T6/T7 touch.**
- **Nothing written to any BOND file.** This packet is the whole footprint.

**My only observation, flagged as an observation:** dealer takedown at **12.49%** is on the low side and indirect at **62.93%** is not obviously soft — but "not obviously soft" is not a grade, and your own history says the marker lives in the *comparison*, not the level. `[[finding_level_without_a_reference_has_two_failure_modes]]`

---

## 3. The T7 vintage trap, restated so it survives the gap

The 2:00PM minutes record the **July 28–29** meeting. **Participants had not seen the 8/7 payroll.** Do not grade "hardened staff language" against data that did not exist in the room. Your frozen resolver text is the standard; the calendar is not.

## 4. Also owed to you (carried, not new)

- **`DFII10` 2.44 [FRED 8/17]** is still the last posted observation — 8/18 had not published at 13:2x today. **6bp from the 2.50 re-arm**, the only surviving add-gate on 004 (TLT Sep-30 77P ×25, the book's largest rail). **Today's tape runs the other way:** TLT **$82.65 +1.21%** at ~13:1x, VIX 15.24 −3.79%. A reaction capture follows in a second packet after 2PM.
- **BND-15 (70%)**: no DFII10 close ≥2.50 through 8/29 — unresolved, unmoved by me.
- Open from 8/18: T6 platform-naming defect (with LIQUID) · DAEDALUS packets unprocessed since 8/07 (×1 to you).

**Source:** TreasuryDirect TA_WS primary, single pull, timestamped above. **Priority:** 🟡 (perishable datum secured; no adjudication pending on PROME's side).
