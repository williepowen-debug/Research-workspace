# BRENT TRADE.md — domain trade surface

**Updated: 2026-09-08 — position/rule reconciliation, not an option-mark refresh. Last real data refresh: 2026-09-02 (option chain).** Current holdings below mirror TERRY's September 8 packet and Will confirmations cited in its owner cards. Live broker inventory, orders, bid and new fills UNKNOWN. Historical marks below are dated records; do not quote them as today's sleeve or current quantity. Full superseded header/current container retained verbatim with checksums in `archive/2026-09-08_owner-writeback-before.json`.

## CURRENT STANCE (v5.8 reference)

Thesis and calibration: `thesis/THESIS.md`. **WQ-189/192 STAND DOWN; no live deploy gate or discretionary arm.** Existing confirmed-destroyed-capacity frame-breaker handling remains binding; a quote or source failure does not meet it. No new proposal or capital action. Market evidence: `setups/2026-09-08_market-docket-owner-read.md`.

## POSITIONS (live)

Broker truth remains off-repo. Four recorded oil expressions pending the selected XLE exit; marks are not refreshed here. This table supersedes the former October-call ×2 and XLE LAPSE live rows. The former STNG phantom record is retained in the before-image and RULINGS; STNG is tracked, never owned. CF June 18 130C expired worthless, historical only.

| Position | Type | Status | Existing rule / source |
|---|---|---|---|
| USO 35 shares | Shares | HELD, broker not rechecked September 8 | Prior Will-confirmed holdings. The share risk scaffold remains UNRATIFIED; no new instruction. |
| USO Oct-16 135C ×1 | One remaining call | One sold September 2 per Will's direct confirmation, mirrored by TERRY | WQ-145/167: A NO-VERDICT; no second 14.25 target. First-sale price permanently UNKNOWN, no re-ask. B official USO close <135 -> next-open exit of remainder. September 8 vendor close 146.03 does not select B on available mirror evidence; not newly exchange-authenticated. C unconditional October 9 before-close time stop. No roll. |
| USO Sep-18 150/165 ×1 | Call debit spread | HOLD through expiry | WQ-168 §3, Will-approved. Former disposition question is closed. |
| XLE Sep-30 65C ×2 | Calls | September 9 OPEN EXIT SELECTED; fill UNKNOWN | September 8 regular-session vendor close 64.77 <66.50 selects approved WQ-168 §7 exit of both at bid next open, including red open; rebound does not replace the September 8 test. TERRY implementation; Will live broker holdings/orders/bid check and execution. L253 receipt pending. |

Implementation sources: `../TERRY/setups/XLE65C_approved-exit-tracking_2026-09-08.md` and `../TERRY/setups/USO-135C_rule20-management_2026-09-01.md`. No fresh order or fill claimed by BRENT. Refiners fill status remains UNKNOWN; no re-ask.

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
| 2026-09-08 | XLE exit selected for September 9 open | PENDING live broker check / execution / receipt. Reaffirmed September 9 startup after the open: read TERRY card remains STAGED/unconfirmed; no later broker receipt supplied or inferred. |
| 2026-09-02 | One USO October 135C sold | One remains. Sale price permanently UNKNOWN under WQ-167; no re-ask. |
| 2026-07-24 | USO September 150/165 spread filled | Recorded ~$300 net debit; historical fill basis, not a live quote. Current holding instruction is HOLD through expiry. |
| 2026-06-18 | CF June 130C expired worthless | Historical closed leg. |
| 2026-09-08 | Convex-arm stand down | WQ-189/192 unchanged; no deployment. |

## BINDING WILL RULINGS

Current scope/tenor and approval clauses: [BG-01 through BG-08](setups/SPECS_GATES.md). Current holding-specific instructions stay in POSITIONS above. Dated reasons remain in [RULINGS.md](RULINGS.md).

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
