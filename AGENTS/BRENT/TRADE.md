# BRENT TRADE.md — domain trade surface

**Updated: 2026-10-01 13:2x ET (PROME packet 2026-10-01, D-70: 159C outcome + 150C partial). Last real data refresh: 2026-10-01**, from the canonical mirror, not a broker view: `FORGE/STATUS.md` (ANVIL **9/30 post-close reconcile `33bc8c293`** + ANVIL **10/1 intraday reconcile `dac72b4ae`**, both from PROME's transcriptions of Will's Fidelity captures). **Broker truth stays off-repo. FORGE marks are 10/1-intraday vintage; never cite them as live (root rule #4).** No order, no recommendation, no rule change is made here. *(Prior: 2026-09-28 ~18:3x Will-approved cleanup, before-image preserved.)*

> ⚖️ **WITH WILL NOW:**
> - **USO Oct-09 $150C ×1 expires Fri 10/09.** Will's hand; **his standing practice is SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET). TERRY card `MGMT-USO150C-OCT09` (`5ce609f80`, written on ×2 — D-70) carries the rail *"Hard stop Fri 10/09 15:00 ET"*; no harvest rule registered. ⚠️ WQ-297 A ties it to the USO stock line (one oil bet) — PROME's read, not adjudicated.
> - **Held VLO share:** exit rule **`GATE-TERRY-VLO-HELD-01` REGISTERED 9/28 18:36 ET** (WQ-330, Will "both"): leg A Nov crack settlement < $90.16 ⇒ SELL rec · leg B1 a signed US distillate export-restriction text ⇒ SELL. TERRY grades; Will executes. Letter: `PROME/GATES.tsv`.

## CURRENT STANCE (v5.9 refinement; prior calibration retained)

Thesis and calibration: `thesis/THESIS.md`. **WQ-189/192 STAND DOWN; no live deploy gate or discretionary arm.** Confirmed-destroyed-capacity frame-breaker handling (BG-02) stays binding; a quote or source failure does not meet it. Market evidence: `setups/2026-09-08_market-docket-owner-read.md`. Current policy risk to the refiner leg (US diesel export restriction, live talk, no order): [`research/2026-09-28_us-diesel-export-ban-risk.md`](research/2026-09-28_us-diesel-export-ban-risk.md). §3 there is sensitivities only; grade nothing from it.

### FRAME-BREAKER STATE (letter: [BG-02](setups/SPECS_GATES.md#bg-02--frame-breaker-prospective-capacity-floor-and-constraints))

- **Instance (4), the Petroline strike 9/10: LAPSED 2026-09-25 17:0x ET ⇒ NOT MET** (premium, not destroyed capacity). Closed; **not re-opened on a later relay of the same satellite data.** A lapse is not evidence the outage was small. Grade: [PREP + grade](setups/2026-09-25_BG-02-grade-PREP.md).
  - The 9/28 Yanbu restart report (Bloomberg, anonymous) binds nothing.
  - Historical grades: [9/11](setups/2026-09-11_petroline-frame-breaker-adjudication.md) (its "verified absence" of a state statement was RETRACTED 9/12) · [9/12 four quantities + resolver defect](setups/2026-09-12_petroline-four-quantities-and-resolver-defect.md).
- **WQ-234 RULED C** (Will, 9/22 19:20, verbatim *"C"*), encoded 9/23 as **BG-02 C1–C6**: AIS-derived instruments **corroborate, never fire**; a fire needs **R1** (Aramco/MoE/SPA statement) or **R4** (a clean FAL-01 with an output figure).
- **Owner reading standard, retained (strictly restrictive; it can only refuse):** for any tracker read offered as corroboration:
  1. Kpler AND Vortexa must both show the fall.
  2. The conservative figure governs.
  3. A sign disagreement ⇒ NO-VERDICT.
  4. No AIS-dark-share disclosure ⇒ NO-VERDICT.
  5. R1 and R4 are unaffected.
  6. `R-CURVE-VETO`: a throughput print alone does not fire if Brent M1−M3 has not widened versus the pre-event settle basis (never falsified; kept because it can only refuse).
  - Reasons (the vendor baseline spread of 0.8 mb/d exceeds the 0.7 floor; AIS-dark error is correlated with the trigger) are in the [before-image](archive/2026-09-28_cleanup/TRADE.md) § FRAME-BREAKER.
- **Successor Saudi-restart resolver:** PROPOSAL `setups/2026-09-18_saudi-restart-resolver-PROPOSAL.md`. It registers only **after the WQ-264 shadow run ends 10/24**. Nothing is armed. **WQ-331 P4 (Will 9/28 18:36):** it is the ONLY Saudi-relief grader; Yanbu reports before it registers are record-only ([THESIS § TWO PHASES](thesis/THESIS.md)).
- **Staged leg-(b) structure (USO Nov-20 165/180, 9/10 pricing) and its `$4.95` breach-branch refusal: VOID as priced.** The Nov-20 eligibility window closed 9/21, and every figure was keyed to USO 158.38. Any future leg (b) is re-cut from scratch under BG-03/BG-04. **Two principles carry forward:**
  - a refusal debit is pre-registered BEFORE the fire;
  - the fire-time debit comes from the **broker chain, never `chain_fetch.py`** (it read ~10% optimistic on the transacting side, n=1).
  - Verbatim text: before-image.
- **Three gates, all required at any fire:** (i) BG-02 head clause met on the letter · (ii) **WQ-192 lifted in Will's own words** (a relayed recommendation is not an approval) · (iii) **Will's [Approve] at the fill.**

## POSITIONS (live)

*Refreshed 2026-10-01 from FORGE (`dac72b4ae`); broker truth off-repo. ⚠️ Keep the heading above exact: `scripts/pending_receipts.py` matches it literally and fails closed without it (renamed 9/28 → boot could not certify until the 9/30 restore, PROME packet 2026-09-29).*

| Position | Account | Status (source) | Existing rule / owner |
|---|---|---|---|
| **USO 37 sh** | Fidelity | Held per the 10/1 intraday capture; cost $122.28/sh `[FORGE 10/1 intraday]` | **WQ-200 DECLINED by Will 9/10: no harvest/give-back rule live; Will manages by hand.** The share risk scaffold remains UNRATIFIED. |
| **VLO 1 sh** | Fidelity | **Bought 9/18 @ $412.00** (ledger row 7; fill TIME unknown, D-55); held per the 10/1 capture `[FORGE 10/1 intraday]` | WQ-213: 1 of 3. The entry condition was a refiners-red-vs-oil day; **there was no crack filter at entry**. TERRY card [`BRENT_refiner-distillate-strong-leg_2026-08-27.md`](../TERRY/setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md). **Exit rule: `GATE-TERRY-VLO-HELD-01`** (banner above; TERRY grades). |
| **VLO 2 sh STAGED** | — | Not bought. `GATE-TERRY-VLO-SCALE`: (A OR B) AND NOT F1; 9/25 NOT MET; review_by 10/14 | TERRY grades → Will. **F1 stays on the matched NOVEMBER basis (HOX26×42 − CLX26) until the 10/06 sitting (L471/WQ-252)**, independent of the 9/30 Brent pin switch (Will 9/28, scope item 1). |
| **USO Oct-09 $150C ×1** expiry=2026-10-09 | Fidelity | **OPEN ×1** after a 10/1 partial sale-to-close of 1 of 2 (EXECUTION LOG); broker basis on the remaining ×1 **$299.66** `[FORGE 10/1 intraday, dac72b4ae]` | **Will's hand; sell-or-roll before expiry** (USER.md). TERRY `MGMT-USO150C-OCT09` rail *"Hard stop Fri 10/09 15:00 ET"*; no harvest rule. Opened 9/30 ×2 @ $2.99 as the roll leg out of the Sep-30 $159C. |
| USO Sep-16 $165C ×1 (RH) | Robinhood | **Not held**: past expiry and absent from the 9/27 RH card. Disposition (sold / expired / misread) **UNKNOWN, not inferred** | FORGE D-57 · PROME WQ-169. |
| STNG | — | **Tracked, never held** (Stage-A tanker-liveness composite). FORGE D-17: absent from every capture since 8/2 | — |

**Closed legs (receipts in EXECUTION LOG):** **USO Sep-30 $159C ×2 (Fidelity) — sold to close 9/30 @ $0.01, realized −$919.46** (WQ-316 discharged by Will's hand; sold, NOT expired — FORGE D-68) · USO Oct-16 135C (last ×1 sold 9/9 @ $17.55) · USO Sep-18 150/165 spread (closed 9/10 by Will's hand, +$330.00) · USO Sep-11 $159C RH (sold before expiry, Will 9/15; FORGE D-58 still UNBOOKED) · XLE Sep-30 65C (sold 9/11 @ $1.51, −$77.33).

## ⚠️ UNRESOLVED BROKER FACTS: explicit, never inferred

*Own level-2 section (promoted 2026-09-30): as a `###` inside POSITIONS its 3-column rows broke `pending_receipts.py`'s 4-cell POSITIONS parse.*

| ID | Fact | Owner / route |
|---|---|---|
| — | **Current state of every line since the 10/1 ≤12:24 ET capture.** Marks are intraday, capture clock not shown; Robinhood not captured 9/30 or 10/1 | Will's next broker view → PROME/ANVIL |
| — | Fill TIMES of the 9/30 159C sale, the 9/30 150C buy and the 10/1 150C sale (no Fidelity view shows them) | Will, low priority |
| D-60 | Fidelity expiry-day "OPTION LIQUIDATION" rows: mechanism (moot for the 159C — sold before expiry) | Will / Fidelity |
| D-55 | VLO fill time (date 9/18 known) | Will, low priority |
| D-57 · WQ-169 | RH USO Sep-16 $165C disposition | Will |
| D-58 | RH USO Sep-11 $159C: sale date, price, proceeds (Will confirmed "sold before expiry") | Will, low priority |
| D-49 | XLE: the FIRST contract's date and price | FORGE |
| WQ-167 | First USO Oct 135C sale price (9/2): **permanently UNKNOWN, no re-ask** | closed |
| — | Resting-order cancellation after the 9/9 USO 135C sale: unverified | Will, low priority |

## Decision read paths

Supersedes: the former whole-TRADE conditional read and mixed historical rule containers (Will-approved cleanup, 2026-09-08).

| Decision | Required read BEFORE assessing or proposing it |
|---|---|
| Position review / exit / pending receipt | This file, then [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md) and the relevant TERRY owner card |
| Structural proposal / frame-breaker | This file, [SPECS_GATES.md](setups/SPECS_GATES.md), then [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md) |
| Off-ramp proposal / entry / second tranche | This file, [SPECS_OFFRAMP_ENTRY.md](setups/SPECS_OFFRAMP_ENTRY.md), then [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md), including unresolved persistence applicability |
| Initially unrelated session becomes trade-relevant | Stop the decision work and take the applicable read path above; boot's earlier conditional read does not cover this transition |

Read the COMPLETE named spec, including caveats and unresolved clauses. A healthy feed or a reconciliation stamp does not establish that the deciding agent read the rule. Any proposal remains subject to Will's explicit approval.

## EXECUTION LOG

| Date | Action | Detail |
|---|---|---|
| 2026-10-01 | **USO Oct-09 $150C: 1 of 2 SOLD TO CLOSE @ $3.92** (Fidelity), +$391.34 proceeds ⇒ **+$91.67 realized** vs $299.67; ×1 left, basis $299.66 | Fidelity Pending list Oct-01 row 2 via PROME's transcription → ANVIL `dac72b4ae` (FORGE). Will's hand; fill time not shown. ⚠️ TERRY `MGMT-USO150C-OCT09` and `FORGE/position_management.tsv` row 20 still read ×2 (D-70, their owners). receipt_status=RESOLVED |
| 2026-09-30 | **USO Oct-09 $150C ×2 BOUGHT @ $2.99, −$599.33** (Fidelity) | Activity 9/30 row 6, roll leg 2 (row 5 = the 159C sale; limit $2.98) via ANVIL `33bc8c293`. receipt_status=RESOLVED |
| 2026-09-30 | **USO Sep-30 $159C ×2 SOLD TO CLOSE @ $0.01, +$1.87 ⇒ realized −$919.46** (Fidelity) — **WQ-316 DISCHARGED** | Activity 9/30 row 5 via ANVIL `33bc8c293`. **Sold, not expired** (FORGE D-68: WQ-316's 17:4x "expired worthless … −$921.33" and TERRY's citing text are superseded by the broker row). Matched on contract (USO Sep-30 $159C) AND account (Fidelity) — NOT on the 150C partial-sale rows `pending_receipts.py` offered as closure candidates. receipt_status=RESOLVED |
| 2026-09-28 | **USO Sep-30 $159C ×2: NOT sold** (fills receipt) | PROME transcription of Will's pasted receipt (`PROME/reports/2026-09-28_will-fills-receipt.md`); ANVIL fills pass (FORGE). Three other lines were sold in part that day (QQQ/TLT; not BRENT's domain). WQ-316 open. |
| 2026-09-18 | **VLO 1 sh BOUGHT @ $412.00** (Fidelity) | Fidelity Activity row 7 via the 9/27 transcription (`PROME/data/2026-09-27_broker-capture-TRANSCRIPTION.md`); WQ-213 condition (refiners red vs oil). Fill time not shown (D-55). ⏳ First recorded in BRENT TRADE 2026-09-28; it lived only in FORGE/TERRY until then. receipt_status=RESOLVED (fill receipted at Fidelity Activity row 7; only the fill TIME is open, D-55) |
| 2026-09-18 | **USO Sep-30 $159C ×2 BOUGHT, −$921.33** (Fidelity) | Activity row 8, same transcription. ⏳ First recorded in BRENT TRADE 2026-09-28. receipt_status=RESOLVED (entry fill receipted; the EXIT is WQ-316, tracked on the POSITIONS row by expiry=) |
| 2026-09-15 confirmation | USO Sep-11 159C SOLD before expiry, by Will's hand | receipt_status=RESOLVED. Will explicitly confirmed "Sold before expiry". Exact sale date, price and proceeds UNKNOWN; no P/L inferred. Bought 9/10 at $1.52 (historical). |
| 2026-09-10 ~15:1x | **USO Sep-18 150/165 spread CLOSED early, by Will's hand** | "USO Call Debit Spread $630.00" (Robinhood activity, ~1h before the 16:10 capture); spread absent from positions. $630.00 proceeds vs $300.00 debit ⇒ **+$330.00 (+110%)**. Seven sessions before the WQ-207 9/17 rail; neither override fired (USO close 158.38). [Receipt](../../PROME/data/2026-09-10_robinhood-capture-1610-TRANSCRIPTION.md). RESOLVED. |
| 2026-09-10 12:35 | **USO Sep-18 150/165: management rule RULED (WQ-207)** | Will: "Approve option 1" on TERRY `TRY-MGMT-USORH150165` ⇒ close at the 9/17 open · harvest override close ≥165 · defence close <153 · OR-joined · no roll. **Discharged the same day by Will's early close.** |
| 2026-09-10 | USO Sep-18 150/165: broker mark receipt | Robinhood ~12:3x: ×1, mark 6.11, avg cost 3.00. A position mirror, not a fill. The HOLD-through-expiry instruction was superseded at 12:35 by WQ-207. |
| 2026-09-09 | Final USO October 135C sold | Will's receipt via [PROME](../../PROME/reports/2026-09-09_USO135C-sale-receipt.md): ×1 at $17.55, net $1,754.30 after $0.70 costs, settled 9/10; zero remains. B/C discharged. |
| 2026-09-08 → **RESOLVED 2026-09-11** | XLE exit selected for the 9/9 open → **FILLED 9/11** | **Sell to Close 1 XLE Sep-30-2026 65 Call, Limit $1.51, FILLED 2026-09-11 ~10:07 ET.** Net $150.34; realized **−$77.33 / −33.97%**. Will's Fidelity row via TERRY `bcc962bbd`. **WQ-210 DISCHARGED.** ⚠️ BRENT recorded it only on 9/14; the row sat PENDING for three days while the receipt existed (boot step 6c was run as a re-assertion, not a resolution). The FIRST contract stays UNKNOWN (D-49). receipt_status=RESOLVED |
| 2026-09-08 | Convex-arm stand down | WQ-189/192 unchanged; no deployment. |
| 2026-09-02 | First USO October 135C sold | One remained; first-sale price permanently UNKNOWN (WQ-167). |
| 2026-07-24 | USO September 150/165 spread filled | ~$300 net debit (historical fill basis). Discharged by the 9/10 close. |
| 2026-06-18 | CF June 130C expired worthless | Historical closed leg. |

## BINDING WILL RULINGS

- **Current scope/tenor and approval clauses:** [BG-01 through BG-08](setups/SPECS_GATES.md).
- **WQ-330 (9/28 18:36):** "both" ⇒ `GATE-TERRY-VLO-HELD-01` legs A and B on the held VLO share (TERRY's letter, `PROME/GATES.tsv`).
- **WQ-316:** the Sep-30 $159C was Will's hand; discharged by his 9/30 sale-to-close (EXECUTION LOG).
- **Standing practice (Will 9/30 19:03 ET, `USER.md`):** sell or roll every option line before expiry; never a hold-to-expiry rail.
- **WQ-234 (9/22):** "C" ⇒ BG-02 C1–C6.
- **WQ-207 (9/10 12:35):** the 150/165 management rule; discharged the same day.
- **WQ-200 (9/10):** USO shares have NO harvest/give-back rule; Will manages by hand.
- **WQ-213:** VLO entry condition; 1 of 3 filled.
- **2026-09-28 ~18:10 (Will, in the BRENT session; verbatim in the PROME packet `c3e185152`):**
  - keep the scheduled grades, the Wed Brent switch and the separate November F1 basis to 10/06;
  - commission one TERRY VLO management proposal (Will approves separately);
  - bounded measurement and phase map;
  - **this TRADE cleanup**;
  - paid data deferred.
- Dated reasons: [RULINGS.md](RULINGS.md).

## DEPLOY GATE v3 · STAGE-A · OFF-RAMP · HARVEST

- **Deploy gate v3 is RETIRED.** Surviving frame-breaker and economics/vehicle/approval constraints: [BG-02, BG-03](setups/SPECS_GATES.md#bg-02--frame-breaker-prospective-capacity-floor-and-constraints). No OVX re-arm is registered.
- **Stage-A entry, v6 measurement, tranche conditions:** [SPECS_OFFRAMP_ENTRY.md](setups/SPECS_OFFRAMP_ENTRY.md). Do not grade from old v4 narrative.
- **Harvest (H1/H2/H3), persistence and sizing:** [BH-01…BH-05, SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md). H1 is announcement-anchored.

## CATALYSTS bearing on the arm

[docket/CATALYSTS.tsv](docket/CATALYSTS.tsv) is the only dated-event record; the [STATUS calendar](STATUS.md) is generated from it.

## RESOLVED / HISTORY

- **2026-09-28 before-image** (26,511 B, whole file, SHA-256 `29b0b63f…ae108371`, crc32 `7cb1efe4`): [archive/2026-09-28_cleanup/TRADE.md](archive/2026-09-28_cleanup/TRADE.md) + [manifest](archive/2026-09-28_cleanup/manifest.json). It holds the full frame-breaker reasoning (dual-tracker defect, readability pre-registration, 9/12 re-grade) and the staged leg-(b) and breach-branch text verbatim. What moved: [TRADE_OBLIGATIONS § 2026-09-28](workbook/TRADE_OBLIGATIONS.md).
- **2026-09-08 before-image:** [archive/2026-09-08_cleanup/TRADE.md](archive/2026-09-08_cleanup/TRADE.md) · [manifest](archive/2026-09-08_cleanup/manifest.json).
- Archives supply provenance only; current rules are reached by the read paths above. Ordinary closeout updates holdings, action state and receipts here; dated analysis goes to an evidence note.
