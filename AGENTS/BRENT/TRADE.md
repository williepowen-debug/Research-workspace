# BRENT TRADE.md — domain trade surface

**Updated: 2026-09-10 ~16:3x ET — Sep-18 150/165 spread CLOSED by Will ~15:1x for $630.00 (+$330, PROME 16:10 capture transcription); WQ-207 discharged unexecuted; new Will-hand USO Sep-11 159C ×1 @1.52 noted, no rule. Earlier: 12:3x screenshot mark 6.11; underlyings moved (USO 156.74 between the Sep-18 strikes; XLE 65.17, −0.5% on a +5% crude day); delayed option indications 11:35–11:47 ET in [WPSR report §2](research/2026-09-10_wpsr/REPORT.md).** No direct broker session or current open-order check. XLE fill receipt remains pending (L253). Prior evidence: [September 9 review](research/2026-09-09_squeeze-review/REPORT.md). Historical states remain dated; current executable bids are UNKNOWN.

## CURRENT STANCE (v5.8 reference)

Thesis and calibration: `thesis/THESIS.md`. **WQ-189/192 STAND DOWN; no live deploy gate or discretionary arm.** Existing confirmed-destroyed-capacity frame-breaker handling remains binding; a quote or source failure does not meet it. No new proposal or capital action. Market evidence: `setups/2026-09-08_market-docket-owner-read.md`.

## POSITIONS (live)

Broker truth remains off-repo. Two recorded open oil expressions after the 9/10 spread close (USO 37 shares; XLE 65C ×1 — one of two sold on an unrecorded date per FORGE 9/10) plus a Will-hand USO 159C 9/11 day-trade leg; new delayed marks are in the evidence report, not broker valuations. This table supersedes the former October-call ×2 and XLE LAPSE live rows. The former STNG phantom record is retained in the before-image and RULINGS; STNG is tracked, never owned. CF June 18 130C expired worthless, historical only.

| Position | Type | Status | Existing rule / source |
|---|---|---|---|
| USO 37 shares | Shares | HELD in newer broker mirrors; direct broker not rechecked | Corrects stale 35 from PROME September 3 transcription and September 9 screenshot review; not a new purchase. See evidence report. Share risk scaffold remains UNRATIFIED. |
| USO Oct-16 135C ×0 | CLOSED September 9 | Remaining ×1 sold by Will at $17.55; net $1,754.30; settlement September 10 | [PROME receipt](../../PROME/reports/2026-09-09_USO135C-sale-receipt.md). B/C discharged because no contract remains; neither trigger claimed fired. First September 2 sale price permanently UNKNOWN/no re-ask. No roll or replacement; resting-order cancellation unverified. |
| USO Sep-18 150/165 ×0 | CLOSED 2026-09-10 ~15:1x ET — Will's hand | **CLOSED EARLY.** Activity row 'USO Call Debit Spread $630.00' ~1h before the 16:10 capture; spread absent from the Options list ⇒ closed (PROME inference from absence + activity row; the row prints no legs or per-contract price). Proceeds **$630.00** vs **$300.00** debit (7/24) ⇒ **+$330.00 realized (+110%)**. USO official close 158.38. | [PROME transcription of Will's 16:10 ET Robinhood capture](../../PROME/data/2026-09-10_robinhood-capture-1610-TRANSCRIPTION.md). **WQ-207 (Will 9/10 12:35: close 9/17 open / overrides ≥165 / <153) DISCHARGED by early execution — neither override fired, the 9/17 rail never reached.** TERRY card `TRY-MGMT-USORH150165` ⇒ EXECUTED. No roll. |
| USO Sep-11 159C ×1 | Call — Will's hand, day-trade class | HELD at 16:10 9/10; expires **Fri 9/11 (CPI day)** | Bought ~15:1x ET 9/10 at **$1.52** ($152.00); marked +$64 (+42.11%) at 16:10 ⇒ ≈$2.16. **No card, no rule, no BRENT instruction** — price leg noted only; TERRY owns structure if a rule is ever wanted. [PROME transcription of Will's 16:10 ET Robinhood capture](../../PROME/data/2026-09-10_robinhood-capture-1610-TRANSCRIPTION.md) |
| XLE Sep-30 65C **×1** (was ×2) | Calls | September 9 OPEN EXIT SELECTED; **FORGE 9/10 CLOSE (ANVIL, broker-verified): qty 2→1 — one contract SOLD, date/price UNKNOWN (not among the visible 9/10 ledger rows)**; remaining ×1 marked 1.47 at the 9/10 close | September 8 regular-session vendor close 64.77 <66.50 selects approved WQ-168 §7 exit of both at bid next open, including red open; rebound does not replace the September 8 test. TERRY implementation; Will live broker holdings/orders/bid check and execution. L253 receipt pending (still pending 9/10; delayed 65C 1.42/1.52 at 11:35 ET vs 1.66/1.85 on 9/9). |

Implementation sources: `../TERRY/setups/XLE65C_approved-exit-tracking_2026-09-08.md` and `../TERRY/setups/USO-135C_rule20-management_2026-09-01.md`. September 9 USO closure is established by the PROME receipt; other owner-card history retains its date. Refiners fill status remains UNKNOWN; no re-ask.

Current execution receipts are in §EXECUTION LOG below.

## Decision read paths

Supersedes: the former whole-TRADE conditional read and mixed historical rule containers (Will-approved cleanup, 2026-09-08).

| Decision | Required read BEFORE assessing or proposing it |
|---|---|
| Position review / exit / pending receipt | This file, then [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md) and the relevant TERRY owner card |
| Structural proposal / frame-breaker | This file, [SPECS_GATES.md](setups/SPECS_GATES.md), then [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md) |
| Off-ramp proposal / entry / second tranche | This file, [SPECS_OFFRAMP_ENTRY.md](setups/SPECS_OFFRAMP_ENTRY.md), then [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md), including unresolved persistence applicability |
| Initially unrelated session becomes trade-relevant | Stop the decision work and take the applicable read path above; boot’s earlier conditional read does not cover this transition |

Read the COMPLETE named spec, including caveats and unresolved clauses. A healthy feed or a reconciliation stamp does not establish that the deciding agent read the rule. Any proposal remains subject to Will’s explicit approval.

## EXECUTION LOG

| Date | Action | Detail |
|---|---|---|
| 2026-09-10 ~15:1x | **USO Sep-18 150/165 spread CLOSED — Will's hand, early** | 'USO Call Debit Spread $630.00' (Robinhood activity, ~1h before the 16:10 capture); spread absent from positions. $630.00 proceeds vs $300.00 debit ⇒ **+$330.00 (+110%)**. Seven sessions before the WQ-207 9/17 rail; neither override fired (USO close 158.38). Receipt: [PROME transcription of Will's 16:10 ET Robinhood capture](../../PROME/data/2026-09-10_robinhood-capture-1610-TRANSCRIPTION.md). ⏳ RESOLVED — no further receipt owed on this leg. |
| 2026-09-10 ~15:1x | USO Sep-11 159C ×1 BOUGHT — Will's hand | $1.52 ($152.00), Robinhood; marked ≈$2.16 at 16:10. Day-trade class; expires 9/11. No rule. Same receipt. |
| 2026-09-10 12:35 | **USO Sep-18 150/165 spread — management rule RULED (WQ-207)** | Will, BRENT session: "Approve option 1" on TERRY `TRY-MGMT-USORH150165` ⇒ dated close 9/17 open · harvest override close ≥165 · BE defence close <153 · OR-joined · no roll. Rec'd by TERRY, concurred by BRENT. **Discharged ~15:1x the same day by Will's early close (row above).** |
| 2026-09-10 | USO Sep-18 150/165 spread — broker mark receipt | Will's Robinhood screenshot ~12:3x ET: HELD ×1, mark 6.11 ($611), avg cost 3.00, total return shown +$311 (+103.67%), today +$265. Screenshot is a position mirror, not a fill; no action taken. ~~HOLD through expiry stands~~ **SUPERSEDED 12:35 ET the same day by WQ-207 (Will 9/10 12:35 ET): close at the 9/17 open, or at the next open after a USO close ≥165 / <153; never 9/18 — see the ruling row above.** |
| 2026-09-09 | Final USO October 135C sold | Will’s receipt via [PROME](../../PROME/reports/2026-09-09_USO135C-sale-receipt.md): ×1 at $17.55, net $1,754.30 after $0.70 costs, settles September 10; zero remains. Execution time/account field absent from receipt; no order-cancellation inference. B/C discharged. |
| 2026-09-08 | XLE exit selected for September 9 open | PENDING live broker check / execution / receipt. Reaffirmed September 9 approved review: TERRY card STAGED; PROME records Will intention to sell, not fill. Receipt requested; no broker quantity/price/time received or inferred. |
| 2026-09-02 | First USO October 135C sold | One remained after this sale; final contract closed September 9 above. First-sale price permanently UNKNOWN under WQ-167; no re-ask. |
| 2026-07-24 | USO September 150/165 spread filled | Recorded ~$300 net debit; historical fill basis, not a live quote. ~~Current holding instruction is HOLD through expiry~~ **SUPERSEDED 2026-09-10 — live instruction is WQ-207 (Will 9/10 12:35 ET): close at the 9/17 open, or at the next open after a USO close ≥165 / <153; never 9/18 (POSITIONS row).** |
| 2026-06-18 | CF June 130C expired worthless | Historical closed leg. |
| 2026-09-08 | Convex-arm stand down | WQ-189/192 unchanged; no deployment. |

## BINDING WILL RULINGS

Current scope/tenor and approval clauses: [BG-01 through BG-08](setups/SPECS_GATES.md). **2026-09-10 12:35 ET — Will approved TERRY option 1 on the Robinhood USO 150/165 Sep-18 spread: mandatory close 9/17 open, overrides close ≥165 / <153, OR-joined, no roll (letter in TERRY's card; mirrored in POSITIONS above). DISCHARGED ~15:1x ET the same day — Will closed the spread by hand for $630.00 before any rail or override fired; PROME rail WQ-207.** Current holding-specific instructions stay in POSITIONS above. Dated reasons remain in [RULINGS.md](RULINGS.md).

## DEPLOY GATE v3 HARD RULES

The gate is RETIRED. Its surviving frame-breaker and unchanged economics/vehicle/approval constraints are [BG-02 and BG-03](setups/SPECS_GATES.md#bg-02--frame-breaker-prospective-capacity-floor-and-constraints). No OVX re-arm condition is registered.

## STAGE-A v5

Canonical entry, v6 measurement, paired tightenings, calibration caveat and tranche conditions: [SPECS_OFFRAMP_ENTRY.md](setups/SPECS_OFFRAMP_ENTRY.md). Do not grade from old v4 narrative.

## OFF-RAMP ROUND-TRIP PLAYBOOK

Entry: [SPECS_OFFRAMP_ENTRY.md](setups/SPECS_OFFRAMP_ENTRY.md). Harvest, persistence and sizing: [SPECS_TRADE_RULES.md](setups/SPECS_TRADE_RULES.md). H1 is announcement-anchored; the old per-tranche question is superseded. Persistence applicability still requires reconciliation as explicitly described there.

## HARVEST RULE

Complete H1/H2/H3 and calibration limitation: [BH-01 through BH-05](setups/SPECS_TRADE_RULES.md).

## CATALYSTS bearing on the arm

[docket/CATALYSTS.tsv](docket/CATALYSTS.tsv) is the only dated-event record. [STATUS calendar](STATUS.md) is generated from it. This pointer supersedes the obsolete second hand-maintained calendar; no second render is needed.

## RESOLVED / HISTORY

Full pre-migration file, unchanged: [TRADE before-image](archive/2026-09-08_cleanup/TRADE.md). Byte count and SHA-256/CRC32: [manifest](archive/2026-09-08_cleanup/manifest.json). This archive contains outdated holdings, retired instructions and corrected assertions; it supplies provenance only. Current rules are reached by the paths above. Existing older archive links remain in the before-image.

The [obligation inventory](workbook/TRADE_OBLIGATIONS.md) records live, superseded and unresolved dispositions. Ordinary closeout updates current holdings, action state and receipts here; dated analysis goes to an evidence note. It must not append a new historical block to this file.
