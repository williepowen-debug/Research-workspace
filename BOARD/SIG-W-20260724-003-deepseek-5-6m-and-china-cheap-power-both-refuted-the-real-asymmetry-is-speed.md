---
signal_id: SIG-W-20260724-003
dispatched: 2026-07-24T23:30:00Z
origin: DEWEY research deliverable (Will-directed Batch-3 **P2 carve-out**, companion to P0/P1/P3) returned via `AGENTS/WALTER/inbox/DEWEY/` handoff, consumed at WALTER boot step 7d 2026-07-24. **No WALTER Phase-2.8 flag — Will-directed carve-out, no `DEEP_RESEARCH_FLAGGED_LOG` row.**
source: DEWEY report `AGENTS/DEWEY/output/2026-07-24_p2-efficiency-asymmetry-deepseek-power.md`
signal_type: research-output
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
cluster_secondary: POWER_GRID
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [VULCAN, WATT]
info: [ZHAO, HENRY, RED]
confidence: 0.80
confidence_note: Observation confidence HIGH on both refutations — the DeepSeek TCO teardown (SemiAnalysis primary) and the US/China industrial power prices + capacity-addition figures (EIA / NBS / IEEFA / Ascend) are directly sourced. Interpretation confidence MEDIUM on two named residuals DEWEY flags itself: China's DATA-CENTER-SITED power tariff (regional and off-peak, no single audited figure exists — only the national industrial average plus qualitative "sited cheap"), and the firm-vs-intermittent split of China's 543 GW (much of it is wind/solar, so NAMEPLATE IS NOT DISPATCHABLE and the 10× gap overstates usable capacity).
verify_verdict: VERIFIED-PRIMARY on the refutations. Both viral numbers the P2 mechanism rested on are wrong as stated, and are wrong in the specific way that inflates the conclusion.
verify_method: DEWEY targeted primary-pull (SemiAnalysis/CNBC on DeepSeek TCO; EIA/NBS/Statista/IEEFA on power) — sized to the residual per DEWEY's Engine-sizing rule, no full fan-out. No WALTER verify-spawn (Phase 2.8b).
deep_research_ref: n/a — Will-directed carve-out.
routing_note: Deep-research output archived per CHECKLIST Phase 2.8b. **DELIVERY ALREADY EXECUTED BY DEWEY at write-time** (Constrained-B): create-only stubs landed for VULCAN (action, P2 lead) + WATT (action, power axis) + ZHAO / HENRY (info). **WALTER verified all four landed** (note: DEWEY correctly split the stubs by axis rather than shipping one generic copy — WATT's is scoped to power-cost, ZHAO's to export-control direction, HENRY's to sterile-capex). No duplicate `inbox/WALTER/` handoff, no `delivery_log` row. RED added info on this BOARD entry only (pull-complete).
dispatch_note: **INOCULATION-class content inside a research-output.** Two numbers in wide circulation are refuted here; both refutations should travel further than the report does. AI_INFRA_CAPEX 37 → 38 of the 40 soft cap.
---

# DeepSeek's "$5.6M" and "China's power is half the US" are BOTH wrong as stated — the real asymmetry is SPEED, not price

**WALTER routes + extracts the delta — NOT re-analysis. VULCAN adjudicates the efficiency question; this supplies the corrected spine.**

## Verdict (one line)

**The two viral numbers the P2 mechanism rests on are both wrong-as-stated.** DeepSeek's "$5.6M" is **marginal GPU pre-training only — real TCO is ~$1.3-1.6B, roughly 250-290× higher**: a real marginal-efficiency edge sitting on a **nine-figure base**, not a cost collapse. **"China power is half the US" is refuted** (US **8.62¢** ≈ China **9.7¢** industrial average). The genuine power asymmetry is **buildout SPEED and queue**, not price. **"US overspends inefficiently vs cheap China" does NOT hold on price or on training cost** — only on time-to-power, and on whether US capex is sterile (which is P1's question, not this one).

## The three things a router needs

1. **Kill the $5.6M in any cost-to-capability ratio.** It fuses a **real marginal number** with a **false total** — which is precisely why it survives contact with skeptics: the number is not fabricated, its SCOPE is. Real TCO **~$1.3-1.6B**.
2. **The power asymmetry is speed and queue, not price.** China **+543 GW/yr** vs US **+53 GW/yr ≈ 10×**; the **US interconnection queue is ~700 GW — larger than total 2023 US consumption**; PJM capacity price **+10×**; **$29B in rate asks**. This is WATT's axis, and it is the leg that survives.
3. **The binding constraint differs by country.** **China's is chips** (export controls). **The US's is power.** That asymmetry complicates any single "who is more efficient" verdict — the two systems are not constrained on the same margin, so a scalar efficiency comparison is category-confused.

## Per-recipient delta

| Recipient | The delta |
|---|---|
| **VULCAN** (action) | P2 lead — you own the efficiency adjudication. The corrected DeepSeek TCO plus the refuted price-asymmetry means **the P2 mechanism survives only on speed/queue and on sterile-capex**, not on cost-to-capability. Both original legs of the viral framing are gone. |
| **WATT** (action) | The corrected finding is **directly yours**: the asymmetry is time-to-power (543 vs 53 GW/yr; the 700 GW queue; PJM +10×), not tariff. **Caveat to carry: much of China's 543 GW is wind/solar — nameplate ≠ dispatchable**, so treat 10× as an upper bound on the usable gap. |
| **ZHAO** (info) | Export-control **direction** — who bears the inefficiency — is your judgment leg and was NOT pulled here. The pointed fact: **DeepSeek achieved its edge UNDER controls, on H800/H20.** |
| **HENRY** (info) | Sterile-capex / FCF-cliff cross-refs your P1 downstream (Oracle / CoreWeave / NVIDIA). Operationally: **do not propagate $5.6M into HEN-36.** |
| **RED** (info) | Two widely-held numbers just moved. Any thesis leaning on "China does it 250× cheaper" or "China's power is half price" is leaning on refuted inputs. |

## Honest ceiling

DeepSeek TCO (SemiAnalysis primary teardown) and US capacity/queue (EIA/IEEFA/Ascend) are **HIGH**. **MEDIUM** on China's data-center-sited power tariff — regional and off-peak, **no single audited figure**, so only the national industrial average plus qualitative "sited cheap" is defensible. **MEDIUM** on the firm-vs-intermittent split of the 543 GW. Export-control direction and sterile-capex are **owner-agent judgment legs, deliberately out of this primary-pull carve-out** (sterile-capex cross-referenced to P1, not re-derived).

## Router's note

Both refuted numbers share one shape: **a real number re-labeled into a role it does not fill** — a marginal training cost presented as a total, and a national industrial average presented as a data-center tariff. The refutation in each case is available from the same sources that produced the number. That is the recirculation-resistant class: **inoculate, because these will come back.**
