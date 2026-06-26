---
signal_id: SIG-W-20260626-003
dispatched: 2026-06-26T21:29:00Z
origin: Will-Telegram image batch 2026-06-26 — (a) junkbondinvestor (@junkbondinvest) 4:44 PM 6/26 "Apollo chart: deep distress concentrating in small private-credit funds — loans marked below 50: ~12.5% small vs ~8% big"; (b) junkbondinvestor 2:15 PM 6/25 "US software loans have still NOT recovered" (Bloomberg I39241US ~89.7)
source: Apollo (Torsten Slok) chart relayed by junkbondinvestor; Bloomberg I39241US software-loan index
signal_type: data-release
domain: PRIVATE_CREDIT
cluster: PC_STRESS
cluster_secondary: AI_INFRA_CAPEX
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: BROCK
info: [SHADE, LIQUID, RED]
confidence: 0.75
verify_verdict: SKIP-VERIFY 0.75 — Apollo/Slok chart is a credible primary (Apollo's own distress decomposition); junkbondinvestor is a reliable credit relay; the I39241US software-loan index is an objective Bloomberg series. Interpretive weight (does small-fund concentration matter / is software the tell) is BROCK's call.
verify_method: chart + index relay, no verify-spawn. The two datapoints corroborate each other and the existing AI-software→PC thread.
routing_note: PC_STRESS → BROCK action per ROUTING_TABLE; SHADE info (insurer-PC nexus), LIQUID info (credit/funding), RED info (adversarial). primary_substance with a tail-vs-headline mediation: the load-bearing delta is that distress is concentrating in the small / non-headline funds — headline big-fund marks understate the tail. cluster_secondary AI_INFRA_CAPEX (software-loan leg). Extends SIG-W-20260622-002 (first European CLO 2.0 rated-tranche default, AI-software-loan mechanism).
---

# PC tail-stress persists & concentrates in the SMALL funds — software loans still not recovered (BROCK)

**One line:** Two corroborating credit datapoints say the private-credit stress is **real and concentrating where the headlines aren't looking**: (a) **Apollo's own chart** — deep distress is **concentrating in small PC funds**: loans **marked below 50% of principal are ~12.5% at small funds vs ~8% at big ones**, with the small-fund line crossing *above* the big-fund line ~2024 and accelerating since; (b) the **US software-loan index (Bloomberg I39241US) has STILL not recovered** — ~94 pre-Feb → 88.4 low (3/03) → only back to **~89.7 (6/23)**, a partial dead-cat off the AI-software-loan air-pocket. The tail is cracking; the big-fund marks understate it.

> **GRADE: SKIP-VERIFY 0.75, primary_substance.** Apollo flagging tail-concentration in *small* funds is notable precisely because it's the big-manager telling you the danger is in the names without 13-F-grade disclosure. Pairs with the software-loan index that **never healed** — advancing the AI-software→PC thread (SIG-W-20260622-002: first European CLO 2.0 Class-F default; software ≈15.9% of LSTA, −7.8% since mid-Jan). BROCK owns whether small-fund concentration is contained (idiosyncratic small managers) or leading (the marks travel up-fund).

## Per-recipient genuine delta

### → BROCK (ACTION) — the tail is where the disclosure isn't
1. **Apollo small-vs-big decomposition:** loans marked <50 are **~12.5% at small funds vs ~8% at big** — and the small-fund line crossed above big-fund ~2024 and kept rising. The headline big-fund marks (the ones that make the news / the BDC NAVs you track) are the *lower* number; the distress is concentrating in the smaller, less-disclosed vehicles. Is this (contained) small-manager idiosyncrasy / survivorship in the marks, or (leading) the realized-loss frontier that migrates up into the big funds with a lag? Your call — it bears on the BDC NAV-understatement thesis.
2. **Software loans never recovered (I39241US 89.7, 6/23):** the partial bounce off the 3/03 low (88.4) stalled well below the pre-Feb ~94. The AI-software-loan air-pocket from SIG-W-20260622-002 (the European CLO 2.0 Class-F default mechanism) is **still open** — not a V, a stalled dead-cat. Confirms the software leg of the PC tail is a persistent mark, not a one-off.
3. Convergence: this is the same tail BROCK already marked STAGE 2→3 (KBRA DLD 2.3% record-match; Fitch BDC Q1 NAV −2%, 11 BDCs cut divs). Apollo's chart + the software index are two more independent reads that the tail is widening, not healing.

### → SHADE (INFO)
Small-fund PC distress concentration (12.5% marked <50) feeds your insurer-PC nexus: the life insurers that own PC-fund stakes AND lend to them (SIG-W-20260624-005) are likely over-indexed to exactly the smaller, higher-distress funds reaching for yield. The tail-concentration sharpens the double-exposure channel (Lee Robinson's named short, SIG-W-20260624-009).

### → LIQUID (INFO)
PC tail marks deteriorating in the small funds + a software-loan index that won't heal = the structural credit-stress pins you've kept (CCC−BB tail-gap wide vs index compression) getting more support, even as HY OAS (278) sits benign at the index. Bifurcation: index calm, tail cracking.

### → RED (INFO)
Steelman: (contained) Apollo is talking its book — "the distress is in the *small* funds, not us big managers" is a convenient self-serving frame; small-fund marks are noisier/survivorship-prone; software loans are one sector. (leading) a large manager publicly conceding tail-concentration + a software index that never recovered + the realized European CLO default = the marks-migrate-up-fund thesis. Hold both; watch whether big-fund <50 marks rise toward the small-fund line.

## Folded / context
- **BDC/interval-fund redemption-request chart (ZeroHedge / Public Filings; Will-Telegram batch 2, 6/26)** — bar chart of redemption requests Q3-2025 → Q2-2026 across the PC BDC/interval-fund complex: **OTIC ~41% (Q1-26), OCIC ~22%, CCLFX ~17% (Q2), Apollo Debt Solutions (APODS) ~17% (Q2, arrow flagging the Q1→Q2 acceleration), North Haven (NHPIFS), HLEND ~13%, Blackstone (BCRED) ~10%.** This is the **visual corroboration** of the sector-wide redemption wall already dispatched (SIG-W-20260624-001: MS North Haven PIF / Apollo / Blue Owl OCIC 21.9% / OTIC 40.7% all at the 5% cap). **Not separately routed** (same data as -624-001 = DUP) — folded here because it adds the **cross-fund Q1→Q2 acceleration** picture (the redemption demand is broadening AND rising quarter-over-quarter, not a one-quarter spike), reinforcing the "tail cracking" read.
- **Unicus Research PSA (@UnicusResearch, 6/25, 43K views)** — "building a map of direct-lending PC funds line-by-line, down to each borrower, tracing exposure back to company fundamentals… looking into the loan books, not the headline news" (CCLFX fund-complex leverage stack, 1,525 borrowers). **Not separately routed** (research-product promo, no datapoint = Novelty kill) — folded here as a **market-attention datum**: sophisticated shops are now bottom-up mapping PC borrower exposure, a sign the opacity itself is becoming the trade. Reinforces the "tail where the disclosure isn't" read.

## Sources
- junkbondinvestor (@junkbondinvest, X) 4:44 PM 6/26/26 — Apollo chart "Private credit distress concentrating among smaller managers" (loans marked <50% principal: ~12.5% small fund / ~8% big fund; small crossed above big ~2024).
- junkbondinvestor (@junkbondinvest, X) 2:15 PM 6/25/26 — Bloomberg I39241US software-loan index, 89.69 as of 6/23 (high 95.20 12/11/25, low 88.38 3/03/26).
- Folded: @UnicusResearch (X) 3:07 PM 6/25/26 — PC-fund borrower-mapping research PSA (market-attention note).
