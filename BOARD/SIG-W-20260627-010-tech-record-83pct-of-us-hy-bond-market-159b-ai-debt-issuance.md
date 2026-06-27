---
signal_id: SIG-W-20260627-010
dispatched: 2026-06-27T14:11:00Z
origin: Will-Telegram image batch 2026-06-27 — X post citing a Bloomberg/Kobeissi-style chart ("Tech is 8% of HY bond market")
source: X post (uncaptured handle) + "Chart 5: Tech is 8% of HY bond market — Tech as a % of Bloomberg US Corporate HY Bond Index" (8.3%)
signal_type: data-release
domain: FUNDING_LIQUIDITY
cluster: AI_INFRA_CAPEX
cluster_secondary: FUNDING_LIQUIDITY
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: LIQUID
info: [BROCK, HENRY]
confidence: 0.75
verify_verdict: SKIP-VERIFY 0.75 — sourced to a Bloomberg index chart ("Tech as a % of Bloomberg US Corporate HY Bond Index" = 8.3%). The figures (tech 8.3% of HY / 10.3% of IG / 18% of 2026 total corporate issuance / $159B combined AMZN+META+GOOGL+ORCL YTD) are checkable Bloomberg-index composition stats. LIQUID confirms the index-composition number on pickup. Note the relayed text has a Kobeissi-style cadence — anchor on the Bloomberg chart, not the editorializing.
verify_method: none at intake — LIQUID owns the corporate-credit-composition read.
routing_note: tech's record share of the corporate bond market (AI-capex increasingly debt-funded) → LIQUID action (credit-market composition / HY-IG share is LIQUID's lane). BROCK info (AI-capex-funded-by-debt thesis — pairs SIG-626-031 Oracle). HENRY info (the AI/tech concentration extended from equity into the credit market). RED via cluster_mediating? — kept off; this is primarily a composition fact. cluster AI_INFRA_CAPEX / sec FUNDING_LIQUIDITY. signal_role cluster_mediating (concentration-risk two-sided: funding-access vs concentration-fragility).
---

# Tech is now a RECORD 8.3% of the US HY bond market — AI capex increasingly debt-funded ($159B issued YTD) (LIQUID)

**One line:** Technology firms now account for a **record 8.3% of the US high-yield corporate bond market** (+2pts since 2022), **10.3% of IG**, and **18% of all 2026 corporate debt issuance** (the largest share on record). **AMZN, META, GOOGL and ORCL have issued a combined ~$159B of bonds YTD to fund AI infrastructure.** Big Tech is taking on record debt for AI.

> **GRADE: SKIP-VERIFY 0.75, cluster_mediating.** A credit-market-composition datapoint that quantifies the AI-capex-debt thesis at the index level: AI capex is no longer just an equity-concentration story — it's now a record share of the *credit* market too. Two-sided: bull (Big Tech is investment-grade-quality, the market is happy to fund it, ample demand) vs bear (record concentration of bond issuance in one sector funding a single capex theme = concentration-fragility if AI-capex returns disappoint). Pairs SIG-626-031 (Oracle FY26 FCF −$23.7B / $40B raise = AI-capex-funded-by-debt REALIZED).

## Per-recipient genuine delta

### → LIQUID (ACTION) — credit-market composition / concentration
Your lane: tech = a record **8.3% of the Bloomberg US Corporate HY index** (+2pts since 2022), **10.3% of IG**, **18% of 2026 issuance** (record). That's a concentration shift in the corporate-credit market toward one sector funding one theme (AI infra). Confirm the index-composition numbers (Bloomberg HY/IG indices). The credit-risk question you own: does a record sector-concentration in the bond market change the HY/IG beta if AI-capex sentiment turns — i.e., is the marginal HY buyer now long AI-capex-debt? Composes with the CCC-BB tail (CCC 968) and the AI-capex air-pocket thread.

### → BROCK (INFO) — AI-capex-funded-by-debt, the public-market leg
The public-bond complement to your AI-capex-debt read: $159B combined AMZN/META/GOOGL/ORCL issuance YTD for AI infra. Pairs SIG-626-031 (Oracle $40B raise) — the same thesis (AI capex outrunning FCF, funded by debt) now visible as a record share of the IG/HY market. The private-credit leg (Apollo/SPV GPU-financing, SIG-W-20260627-008) is the shadow side of the same capex-funding-gap.

### → HENRY (INFO) — concentration extended from equity to credit
You track the AI/tech equity-concentration extreme (semis 18.8% of S&P, $884B inflows, etc.). This is the same concentration showing up in the *credit* market: tech at a record share of HY/IG issuance. If the AI-capex air-pocket hits, the de-rating now has a credit-market transmission, not just equity. One more axis of the AI/tech concentration risk.

## Sources
- X post (handle uncaptured): "Technology firms now account for a record 8.3% of the US high-yield corporate bond market… risen +2 points since 2022… tech accounts for a record 10.3% of the US investment-grade corporate bond market… 18% of total corporate debt issuance so far in 2026, the largest proportion on record… Amazon $AMZN, Meta $META, Alphabet $GOOGL, and Oracle $ORCL have issued a combined $159 billion in bonds year-to-date to fund AI infrastructure. Big Tech is taking on record levels of debt for AI."
- Chart 5: "Tech is 8% of HY bond market — Tech as a % of Bloomberg US Corporate HY Bond Index" = 8.3%.
- **LIQUID confirm the Bloomberg index-composition figures; anchor on the chart, not the editorializing.** Pairs SIG-626-031.
