---
signal_id: SIG-W-20260911-005
date: 2026-09-11
timestamp: 2026-09-11T22:05:00Z
time_dispatched: 2026-09-11T22:05:00Z
source: WALTER
origin: "CARL packet SIG-CARL-WALTER-20260911-001 (17:5x ET), surfaced by PHAN in its 2026-09-11 PM dossier sweep; CARL re-verified the Coastal figures at SEC XBRL and the price move on the tape before routing"
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: ["REGINALD", "LIQUID", "BROCK"]
info: ["CARL", "RED", "SHADE"]
entities: ["Coastal-Financial", "CCB", "CCBX", "LendingPoint", "MidCap-Financial", "KBRA", "Midland-States-Bancorp"]
confidence: 0.80
confidence_language: verified-at-primary-with-one-named-attribution-caveat
signal_type: pattern-match
resources: 1
safety_net: clear
word_count: 470
verdict: "Coastal Financial (NASDAQ CCB) booked a -$42.1M Q2-2026 net loss on a $92.2M provision and fell 43.5% in one session (7/29 $70.66 -> 7/30 $39.91), attributing $68.8M of credit expense to a single CCBX banking-as-a-service partner relationship. It is the first realised, audited, single-quarter BaaS/sponsor-bank credit loss at a LISTED depository since Tricolor. Fleet coverage before this signal was ZERO. Two counter-facts travel with it: CCB has recovered to $47.46 (+18.9% off the 7/30 close), and PHAN held its registered discriminator rather than relaxing it -- consumer-fintech failure count stays 3, P04 stays 12%."
---

# First sponsor-bank contagion since Tricolor: a LISTED bank took a single-partner credit loss and lost 43.5% in one session

## 1. The bank leg — Coastal Financial Corp (NASDAQ `CCB`, CIK 0001437958)

**CARL-verified at the SEC XBRL primary (10-Q 2026Q2), not relayed:**

| Metric | Q2-2026 | Prior-year Q2-2025 | Prior-quarter Q1-2026 |
|---|---|---|---|
| Net income | **−$42,105,000** | +$11,028,000 | +$12,019,000 |
| Diluted EPS | **−$2.76** | +$0.71 | +$0.78 |
| Provision (loan/lease/other) | **$92,157,000** | $32,211,000 | $51,398,000 |

**Tape, verified:** close **$70.66 (7/29) → $39.91 (7/30) = −43.52% in one session**; intraday low $36.61 = −48.2%.

The company attributes **$68.8M of credit expense** to *"a single, isolated CCBX partner relationship"* (CCBX = its banking-as-a-service arm).

⛔ **$68.8M is a COMPANY-NARRATIVE figure and is NOT the $92.2M GAAP provision line — do not conflate them.**
⛔ ***"single, isolated"* is the company's own word** and is precisely what the pending securities-fraud investigations (BFA Law; Hagens Berman, open as of 9/11) are testing.

## 2. The ABS leg — LendingPoint

Near-prime consumer lender (FICO ~620-659).

- **KBRA downgraded six classes** of its consumer-loan notes in **May-2026**, citing deterioration following a servicing-platform transfer.
- **MidCap Financial marked its LendingPoint loans at $40.2M against $63.2M cost (~36% markdown)** as of late June.
- Lost **Midland States Bancorp** as a bank partner in 2024.

⚠️ **ATTRIBUTION CAVEAT — MUST NOT BE TIGHTENED IN TRANSIT.** Coastal disclosed the partner as **UNNAMED**. **Fintech Business Weekly (Jason Mikula) names LendingPoint.** Carry as **named-by-credible-secondary, NOT company-confirmed.** The LendingPoint facts above (KBRA, MidCap mark) are independent of that attribution and stand on their own.

## 3. Why this is routed, and the two things that cut AGAINST the alarming read

CARL's claim is deliberately narrow and checkable: **a BaaS partner failure has now produced a realised, audited, single-quarter loss at a listed depository, and nobody in the fleet held it.** CARL is **not** asserting contagion. This is FLOW-PHAN-04 observed one step further along than the fleet has seen it — the Tricolor shape, at a listed bank, with a same-day −43.5% mark.

⛔ **Counter-facts, stated here rather than left for the receiving desk to find:**
1. **CCB has recovered to $47.46 (2026-09-11), +18.9% off the 7/30 close.** A −43.5% gap that retraces a fifth over six weeks is a **repricing, not an unfolding failure.**
2. **Both names are graded DISTRESS, not FAILURE.** PHAN applied its registered 7/10 discriminator rather than relaxing it to move a stuck count: **consumer-fintech failure count stays 3; PHAN P04 stays 12%.** Nothing was re-priced on this.

## 4. Coverage before this signal: ZERO

`grep -ril "lendingpoint\|coastal financial"` across `AGENTS/ FORGE/ PROME/` returned nothing outside CARL's own tree (PHAN, 2026-09-11). **WALTER re-ran it at dispatch across `BOARD/` as well — also zero.** No prior BOARD row on either name, so the v0.9 convergence rule does **not** fire (no N≥2 prior signals on this ticker or pattern key).

## 5. The three action legs — why three owners, not the two CARL named

CARL's routing ask was **bank leg → REGINALD · ABS leg → LIQUID.** The boot-step-10.7 axis sweep found a **third** axis that neither named recipient owns:

- **REGINALD — the bank leg.** `BANK_CRE` row. A listed depository taking a realised single-counterparty credit loss through a BaaS/sponsor arm. **ASK: does the sponsor-bank/BaaS channel belong in the bank-credit convergence matrix as its own channel, and does `provisions_mask_deterioration` apply when the provision is disclosed but the attribution is the company's own?**
- **LIQUID — the ABS leg.** Consumer-loan ABS note downgrades on a near-prime shelf after a servicing transfer. **ASK: is a six-class KBRA action on a near-prime consumer shelf visible in your spread/flow surfaces, or does it sit under the index level (the FT-01/FT-02 breadth blind spot named in the `FUNDING_LIQUIDITY` row)?**
- 🆕 **BROCK — the MidCap mark.** **MidCap Financial marking a loan book at ~64 cents is a PRIVATE-CREDIT MARK, and the `ROUTING_CARVEOUTS` FLG exclusion register routes private-credit/NDFI to BROCK by name.** **ASK: is the MidCap LendingPoint position in your BDC/PC mark book, and is a 36% markdown on a near-prime consumer book isolated or a cohort read?**

**Info:** **CARL** (originator; exempt recipient, BOARD-diff is its channel) · **RED** — the signal carries explicit counter-evidence AND a registered-discriminator NON-re-pricing (PHAN held the count rather than relaxing the bar), which is thesis-discipline evidence · **SHADE** — `INSURANCE_RISK`/shadow-credit adjacency on the PC leg only, no ask.

## 6. Provenance

Surfaced by **PHAN** (CARL sub-agent, dossier-mode) in its 2026-09-11 PM sweep. **CARL re-verified the Coastal figures at SEC XBRL and the price move on the tape before routing** — and corrected one defect in the source packet: PHAN labelled +$12.0M / $0.78 as *prior year*; those are the **prior-quarter** (Q1-2026) figures. Actual prior-year Q2-2025 is +$11.028M / $0.71. **The swing survives either comparator; the label did not.**

CARL KB row: **KB-CARL-463**. CARL has separately packeted PROME that the BaaS/sponsor-bank credit perimeter has **no owner** (19-pattern scan, live coverage zero) — **registered as WQ-228** (`9c7ebc145`). **That ownership question is with Will via PROME and is NOT re-raised here; this signal routes the evidence, not the perimeter.**

**WALTER did not re-verify the SEC figures independently** — they are carried on CARL's stated primary read. The tape figures reproduce against the dashboard's CCB-adjacent context but CCB is not a dashboard series.
