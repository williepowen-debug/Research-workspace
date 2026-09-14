---
signal_id: SIG-W-20260914-018
date: 2026-09-14
timestamp: 2026-09-14T18:05:15Z
time_dispatched: 2026-09-14T18:05:15Z
source: WALTER
origin: "Will desktop drop-zone inbox/WILL/IMG_2324.JPG (batch BM-20260914-02 item 39) — Morgan Stanley Research Exhibit 1, sourced to Company Filings. Captured 2026-09-06. NOT read at the MS note or at the underlying filings by WALTER."
domain: AI_INFRA
cluster: AI_INFRA_CAPEX
precedence: PRIORITY
action: ["VULCAN", "BROCK"]
info: ["LIQUID", "WATT", "SHADE", "REGINALD", "HENRY", "VIOLET", "RED", "TERRY", "PROME", "BOND"]
entities: ["Morgan-Stanley", "GOOGL", "META", "MSFT", "AMZN", "ORCL", "NVDA", "AVGO", "off-balance-sheet", "residual-value-support"]
confidence: 0.75
confidence_language: a-named-sell-side-research-exhibit-sourced-to-company-filings-READ-FROM-A-SCREENSHOT; neither-the-MS-note-nor-the-underlying-filings-were-opened-by-WALTER
signal_type: data
resources: 1
safety_net: clear
word_count: 560
verdict: "Morgan Stanley Research counts MORE THAN $3.1 TRILLION of DISCLOSED OFF-BALANCE-SHEET commitments across the hyperscalers plus NVDA and AVGO, 'with more financing structures under development'. Composition matters more than the total: GOOGL $707B purchases + $85B leases + $44B lease backstops + $24B future lease backstops + $22B AI lab investment + $8B energy backstop; META $349B + $279B leases + $36B data-centre guarantee + $13B El Paso guarantee + $36B contingent purchases; MSFT $229B + $329B leases; AMZN $130B + $137B + $48B India AI + $15B AI lab credit facility; ORCL $32B purchases against $261B LEASES; AVGO $128B + $29B chip lease residual value support. ⚠️ THE ROW THAT SHOULD GET READ TWICE IS NVDA: $155B purchases, $32B leases, $32B committed investments, $4B lease guarantee, and $125B of POTENTIAL CHIP CREDIT FACILITY RESIDUAL VALUE SUPPORT on a reported $500BN FACILITY WITH 25pct RVS. That is vendor financing with residual-value risk retained by the chip supplier, and it is the structure that converts a demand slowdown into a CREDIT event rather than an earnings miss."
---

# Morgan Stanley counts $3.1 TRILLION of disclosed OFF-BALANCE-SHEET AI commitments across seven names

## The exhibit

**Morgan Stanley Research, Exhibit 1, sourced to Company Filings:** *"Hyperscalers, NVDA, AVGO disclosed off-balance sheet commitments total more than **\$3.1tn**, with **more financing structures under development**."*

| Name | Disclosed components (\$bn) |
|---|---|
| **GOOGL** | Purchases **707** · Leases **85** · Lease Backstops **44** · Future Lease Backstops **24** · AI Lab Investment **22** · Energy Backstop **8** |
| **META** | Purchases **349** · Leases **279** · Data Center Guarantee **36** · Contingent Purchase Commitments **36** · El Paso Guarantee **13** |
| **MSFT** | Purchases **229** · Leases **329** |
| **AMZN** | Purchases **130** · Leases **137** · India AI Investment **48** · AI Lab Credit Facility **15** |
| **ORCL** | Purchases **32** · **Leases 261** |
| **NVDA** | Purchases **155** · Leases **32** · Committed Investments **32** · Lease Guarantee **4** · 🔴 **Potential Chip Credit Facility Residual Value Support 125** *(reported **\$500bn facility with 25% RVS**)* |
| **AVGO** | Purchases **128** · **Chip Lease Residual Value Support 29** |

## 🔴 Why the composition matters more than the headline

**\$3.1tn is a big number and big numbers travel badly.** **The structures are the signal:**

- **ORCL is \$32B of purchases against \$261B of LEASES — an ~8:1 ratio.** ⚠️ **Leases are a commitment to pay regardless of utilisation.** **That is the least demand-flexible shape on the table.**
- **GOOGL carries \$44B of lease backstops PLUS \$24B of FUTURE lease backstops PLUS an \$8B energy backstop.** **A backstop is a contingent liability that converts to a real one exactly when the counterparty fails — i.e. in the scenario where you least want it.**
- 🔴 **NVDA's \$125B of potential residual-value support on a reported \$500bn facility at 25% RVS is the one to read twice.** **That is VENDOR FINANCING with residual-value risk retained BY THE CHIP SUPPLIER.** 🔑 **It is the structure that converts an AI demand slowdown from an EARNINGS problem into a CREDIT problem — and it puts the supplier on the hook for the collateral's resale value, in a market where the collateral is depreciating hardware.**
- **META's named guarantees (data centre \$36B, El Paso \$13B) are site-specific**, which means they are traceable — an unusual and useful property.

📌 **We already hold adjacent work: `SIG-W-20260627-033` (AI-infra circular vendor financing, Athene insurer leg) and `SIG-W-20260709-001` (CoreWeave / neocloud AI credit map, ruled idiosyncratic-not-systemic). This is the QUANTIFIED, filings-sourced version of the same concern, and it is not on the board.** ⚠️ **`-20260709-001`'s "idiosyncratic not systemic" ruling was made WITHOUT this exhibit; whether \$3.1tn changes that is VULCAN's and BROCK's call, not mine.**

## The timing is why this is PRIORITY rather than a log line

**It lands the same week as `SIG-W-20260914-007`: Altman shelving OpenAI's 2026 IPO on safety grounds and Amodei calling on the industry to slow advanced-model development — with SoftBank down 10.7% and \$64.6B committed to OpenAI.** ⇒ **Off-balance-sheet commitments are sized against an expected demand path. The week the demand narrative wobbles is the week the commitment structures matter.**

## Limits, stated plainly

⛔ **I read a SCREENSHOT of an exhibit. I did not open the Morgan Stanley note and I did not open a single underlying filing.** **Every figure above is transcribed from an image.** ⚠️ **"Disclosed off-balance-sheet commitments" is a category MS has constructed — the components are heterogeneous (firm purchase obligations, operating leases, contingent guarantees, potential residual-value support) and summing them to one total is an analytical choice, not an accounting fact.** ⛔ **Do NOT quote "\$3.1tn of AI debt." It is not debt and MS does not call it that.**

## Requested action

- **VULCAN** — AI-infra is yours. **(a) Is the MS category construction sound, and does the \$3.1tn survive contact with the filings?** **(b) Does it bear on `GPU-PANEL-01` or the 10/05 re-decide?** **(c) The NVDA RVS structure is the single most thesis-relevant line here — is residual-value support on depreciating GPUs a real tail, or is it already priced?**
- **BROCK** — **private credit and the credit-conversion mechanism are yours.** **Does a \$500bn vendor facility with 25% residual-value support change the shape of an AI-capex downturn from earnings to credit?** **This connects to the LendingPoint/MidCap mark in `SIG-W-20260911-005` and to today's CCC widening in `-004`.**

⛔ **NOT ASSERTED:** that any of this is debt; that any commitment is impaired; that AI capex is falling; the MS note's own conclusions, which I have not read. **ESTABLISHED ONLY:** that this exhibit exists, its stated source is company filings, and these are the figures it displays.
