# TRADE rotation 2026-11-14 (BRENT closeout, PROME prome-fe ask)

Moved VERBATIM from `TRADE.md` to bring it under the READ_CAP rule-5 stop (70% of budget). Zero edits to payloads. Nothing live moved: every rotated receipt is RESOLVED and WQ-386 was DISCHARGED November 5.

**PAYLOAD RULE:** each set's payload is exactly the text between its `<!-- BEGIN set X -->` line and its `<!-- END set X -->` line, excluding the single newline after BEGIN and the single newline before END. BYTES = `len(payload.encode("utf-8"))`; crc32 = `zlib.crc32(payload.encode("utf-8"))`.

| Set | Content | UTF-8 bytes | crc32 |
|---|---|---|---|
| a | "Position evidence reconciled October 26" paragraph, superseded by the November 5 broker evidence line | 824 | `cc542db6` |
| b | WQ-386 body after its heading: DISCHARGED November 5, EXIT ESTABLISHED, observation pointer, canonical ruling and the GATE-TERRY-VLO-HELD-01 leg-A note | 4429 | `3ae2761e` |
| c | EXECUTION LOG rows dated 2026-10-14 to 2026-10-23, all receipt_status=RESOLVED, in their original order | 1563 | `69eb3128` |
| d | FRAME-BREAKER bullet: staged leg-(b) structure VOID as priced, with its sub-bullets | 524 | `dbbd4fa3` |

<!-- BEGIN set a -->
**Position evidence reconciled October 26:** latest positions capture is October 22, 11:01 ET per Will, as secondarily transcribed by PROME; October 23 Pending/activity evidence and TERRY’s booking are subsequently available. Original images were not independently viewed here. Fidelity IRA account continuity is INFERRED (identifier obscured); quote/fill clocks, unseen orders and later events remain UNKNOWN. [October 22 source](../../PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md), [October 23 activity](../../PROME/data/2026-10-23_broker-activity-TRANSCRIPTION.md), [TERRY booking](../TERRY/research/2026-10-23_broker-booking/NOTE.md). Quantities after activity below are DERIVED, not a new broker capture. Earlier October 19-only header is superseded; receipts are reconciled, never rebooked into FORGE/TERRY.
<!-- END set a -->

<!-- BEGIN set b -->
**✅ DISCHARGED November 5 (TERRY, FORGE):** Will sold the original share at the regular session, November 5, at $366.665, realized −$45.33 against the $412.00 fill. No further leg-A observation or basis review is owed; the November 18–19 catalyst rows are closed. The December letter below stays as the record of the rule.

**🔴 EXIT ESTABLISHED by TERRY, graded 2026-11-04 20:36 EST (TERRY owns; BRENT records):** accepted November 2 reading **$89.2472**, source (2) within $0.0328 of source (3), $0.9128 below $90.16. November 3 $94.1952 does not cancel under the letter; November 4 $88.5451 is a source (3) ESTIMATE. October 29 $90.6750 and October 30 $92.2762 did not fire, which discharges the BRENT October 29–30 items in SCRATCH. TERRY's SELL recommendation covers the ONE original share only, at the Thursday November 5 regular session; Will executes, no desk order. ⚠️ CME settlements unread (blocked); a final November 2 settle at or above $90.16 reverses the grade. BRENT could not reach a settlement by any other route on November 4 (one web search, none found). Vendor controls: daily row equalled CME FINAL on October 23 and CME preliminary on October 30, so a reversal needs the vendor HOZ26 row to be about 2.2 cents per gallon wrong, or CLZ26 about $0.91 wrong. [TERRY note](../TERRY/research/2026-11-04_vlo-leg-a/NOTE.md); `PROME/GATES.tsv` mirrors FIRED-UNEXECUTED. Vendor November 4 daily rows read HOZ26 4.2055 and CLZ26 88.12 on November 5, but each repeats the November 3 volume, so the letter rejects them; TERRY's source (3) estimate stands for that date.

**October 15–30 December observations rotated, discharged:** [verbatim archive](archive/TRADE_wq386-observations_2026-11-05.md), 2326 UTF-8 payload bytes, crc32 `a82a3865`.

Canonical ruling: [PROME § Approved amendment](../../PROME/proposals/2026-10-07_VLO-december-management-RULED.md#approved-amendment). TERRY owns canonical card integration and grades; Will executes. Exact approved operational letter reproduced for this reader path; rationale at [RULINGS](RULINGS.md#r-2026-10-07-wq-386--held-share-month-extension).

> For GATE-TERRY-VLO-HELD-01 leg A only, November matched HOX26×42−CLX26 governs through the October 14, 2026 settlement. December matched HOZ26×42−CLZ26 governs the settlement observations dated October 15 through November 19, 2026, inclusive. Verify named-contract identity on each pull; a continuous ticker or wrong delivery month is rejected. No automatic January roll is authorized.
>
> The held-share thresholds remain strictly below $95 per barrel for notice only and strictly below $90.16 per barrel for TERRY's SELL recommendation. The stock price is not the crack and is not a new stop. The switch is unconditional on the two months agreeing: an accepted December reading below $90.16 may trigger the exit even if November remains above it. No offset, persistence requirement, roll-window suppression or threshold recalibration is adopted.
>
> Preserve the existing source order and observation standard: (1) CME settlement; (2) the vendor daily row dated to that session, finalized and accepted only within $0.15 of (3); (3) 14:28–14:30 ET one-minute volume-weighted settlement-window proxy, labelled ESTIMATE. Reject duplicated-volume/provisional daily rows. If only (3) is available within ±$0.15 of $90.16, or a required leg/window/identity is missing, the observation is UNKNOWN, not a fire. Do not substitute a later session's value or a stale expired-contract value. Re-read at the next touch under the existing missing-data rule. This extension creates no automatic monitor or guaranteed touch cadence.
>
> An exit established under the prior governing November observation remains owed after the switch; an outstanding exit is not cancelled by a higher December reading, missing data or the end of the observation window. TERRY writes the recommendation at its next touch; Will executes at the next regular session under the existing card. No order is placed by the desk.
>
> Review the next basis by November 18, 2026. If no further ruling is made, new leg-A observations become SUSPENDED/UNKNOWN after the November 19 settlement. An already-established exit still remains owed. Policy legs B1–B3 and their existing execution limitations continue unchanged until sale or withdrawal. This is authority to maintain the existing share's management rule, not to buy or re-enter.
<!-- END set b -->

<!-- BEGIN set c -->
| 2026-10-23 | **USO 5 shares SOLD**, fill 168.595, net 842.96 | Secondary Pending view + TERRY booking; 35→30 DERIVED, no new capture. Lot-specific realized not adopted here. receipt_status=RESOLVED |
| 2026-10-23 | **USO Oct30 $165C SOLD CLOSE 1 of 2**, fill 7.15, net 714.32 | TERRY booking matches activity; remaining 1 DERIVED, lot allocation UNKNOWN; no duplicate booking. receipt_status=RESOLVED |
| 2026-10-23 | **USO Oct23 $163C SOLD CLOSE 1**, fill 4.36, net 435.34 | Matched TERRY CLOSED card; DERIVED realized +145.68 versus 289.66 basis. Separate 4.50 limit canceled. receipt_status=RESOLVED |
| 2026-10-21 | **USO Oct30 $163C BOUGHT OPEN 1**, net 358.66 | October 22 positions+ledger; gross fill/time UNKNOWN; distinct from October23 contract. receipt_status=RESOLVED |
| 2026-10-20 | **USO Oct30 $165C BOUGHT OPEN 1**, fill 3.15, net 315.66 | October 20 Filled 3.17-limit order; separate 3.15-limit order canceled; quantity 2 confirmed October 22 before October 23 sale. receipt_status=RESOLVED |
| 2026-10-14 | **USO Oct14$150C ×2 SOLD CLOSE**, net **$760.68** | October15 Fidelity Activity two exact-contract sales354.34+406.34; original basis375.33 gives DERIVED realized+$385.35. Secondary transcription and TERRY closed card matched; times UNKNOWN; no duplicate booking. receipt_status=RESOLVED |
| 2026-10-19 | **USO Oct23 163C / Oct28 165C / Oct30 165C BTO ×1 each** | October19 secondary Activity rows2/3/18: fills2.89/3.35/2.70, net debits289.66/335.66/270.66. No roll linkage or management approval inferred. receipt_status=RESOLVED |
<!-- END set c -->

<!-- BEGIN set d -->
- **Staged leg-(b) structure (USO Nov-20 165/180, 9/10 pricing) and its `$4.95` breach-branch refusal: VOID as priced.** The Nov-20 eligibility window closed 9/21, and every figure was keyed to USO 158.38. Any future leg (b) is re-cut from scratch under BG-03/BG-04. **Two principles carry forward:**
  - a refusal debit is pre-registered BEFORE the fire;
  - the fire-time debit comes from the **broker chain, never `chain_fetch.py`** (it read ~10% optimistic on the transacting side, n=1).
  - Verbatim text: before-image.
<!-- END set d -->
