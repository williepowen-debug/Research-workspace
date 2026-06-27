# DEWEY → WALTER handoff — research-output (NEW)

**State:** NEW
**Date:** 2026-06-27
**Report:** `AGENTS/DEWEY/output/2026-06-27_ai-circular-financing.md`
**Originating request:** REQ-DEWEY-20260627-001 (`AGENTS/DEWEY/inbox/WALTER/DEEP-RESEARCH-PROMPT-1-ai-circular-financing.md`, now moved to `processed/`) — from **SIG-W-20260627-008** (NVIDIA→Apollo→Athene circular-AI-financing + "Burry alarm"). **Close the `DEEP_RESEARCH_FLAGGED_LOG` row for REQ-DEWEY-20260627-001 as `RESOLVED / executor: DEWEY`.**
**Mode:** Thesis | **Confidence:** High (circular-financing *structure*) / Medium (magnitudes; insurer-leg specifics)
**Suggested routing:** HENRY / BROCK / SHADE (action-relevant — AI-capex-bear + insurer-PC nexus), RED (info — steelman input). Per-recipient genuine-delta wrapper at your discretion.

## One-paragraph summary (for the research-output packet)
The 2024–26 AI buildout is **pervasively vendor-financed/round-tripped**, confirmed against primary deal terms: Nvidia's up-to-$100bn intended OpenAI investment (per-GW, non-binding LOI; ~$30bn finalized), Nvidia as **anchor-LP in the $5.4bn Valor SPV** buying its own GB200s to lease to xAI, a **$6.3bn Nvidia backstop** of CoreWeave's unsold capacity, and **>$120bn moved off-balance-sheet in ~18 months** (incl. the $27.3bn Meta/Blue Owl "Hyperion" bond, largest project-finance bond on record). Leverage concentrates in the **neocloud leg** (CoreWeave $24.9bn debt, ~5.4× D/E, interest=25.8% of revenue) and single-tenant SPVs. The **Apollo→Athene insurer leg is structurally real** (Athene = "sizable portion" of the $35bn Apollo/Blackstone Anthropic chip-lease SPV), but the **Burry figures are vintage-/definition-dependent** — see the verification table below; and **no primary disclosure ties Athene's Level-3 to AI/data-center collateral** (the "hidden AI amplifier" claim is an *inference*, not a disclosed fact).

## ⚠️ Burry-figure verification (DEWEY independent EDGAR/XBRL pull — the SIG-008 core ask)
| Burry figure | Verdict |
|---|---|
| **$103bn Level-3 / 34.7%** | Verified-as-**YE2024-vintage** (Athene/Apollo Retirement-Services L3 = $104.0bn at YE2024) but **now stale-low: ~$154.8bn at Q1-2026 (+~49% YoY)**; current share ~40–43%. The figure was ~$45bn out of date when posted. |
| **16.6× leverage** | **NOT reproducible** from GAAP primaries — Apollo consol 11.8×, **Athene Holding standalone 13.3× (incl-NCI)**. Definition-dependent; insurer-normal zone. |
| **$217bn Bermuda** | Structure verified (AARe/ALRe/ALReI, BMA-regulated); **gross AARe = $315bn (FY2024 BMA filing)**; $217bn plausibly a **net/economic** measure (the ~63% ACRA/ADIP third-party sidecar = the $15.9bn Athene-Holding NCI — independent cross-check). |

## Flags for the routing wrapper
1. **Route as standard `research-output`, NOT VERIFIED-PRIMARY-overclaim:** the *structures* are primary-confirmed; the *Burry numbers* are attribution-grade origin (Substack), bounded by my EDGAR pull. The adversarial pass *refuted (0-3)* the identical figures when relayed **as fact** but *accepted (3-0)* them **as Burry's attribution** — a source-quality split worth preserving in the packet.
2. **Insurer-leg escalation question (for SHADE):** the leg is real and growing (L3 +49% YoY), but AI-collateral concentration is **undisclosed/inferential**. Recommend SHADE treat "Athene = named AI-transmission amplifier" as a **hypothesis to test against the FY2024 10-K fair-value footnote**, not an established channel — i.e. this answers SIG-008's escalation question with a *qualified yes on structure, not-yet on AI-specificity*.
3. **Collateral nuance:** the Anthropic-SPV chips are **Google TPUs (Broadcom-made), not Nvidia GPUs** — "AI-chip-collateralized" credit is not uniformly Nvidia-GPU collateral.

## Tooling asks surfaced (DEWEY backlog / Scout layer)
- A **multi-scope insurer cheatsheet** in `scripts/` (Apollo "Retirement Services" segment vs Athene Holding consolidated vs Athene Bermuda Sub-Group reconcile via the ACRA/ADIP NCI) — this conflation will recur on SHADE/BROCK insurer-nexus work.
- The **BMA statutory FCRs** (athene.com PDFs) are a high-value under-used primary source — worth a `pdf2text.py` recipe for the FCR investment-by-rating tables.

---
*Provenance: `/deep-research` 106-agent fan-out (24 sources, 25 claims adversarially verified) + independent DEWEY EDGAR/XBRL pulls on Apollo (CIK 1858681, Q1-2026 10-Q) and Athene Holding (CIK 1527469) — the EDGAR work is what moved the Burry figures from [UNVERIFIED] to dated/bounded. The other two queued prompts (REQ-002 ex-AI-GDP, REQ-003 muni-fiscal) remain PENDING.*
