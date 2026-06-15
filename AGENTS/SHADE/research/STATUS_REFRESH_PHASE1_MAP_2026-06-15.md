# SHADE STATUS Refresh — Phase 1 Map
**Date:** 2026-06-15 ET
**Author:** Prome
**Scope:** Local-source audit only. No primary-source/web refresh yet. Purpose is to define what SHADE `STATUS.md` must change before a substantive rewrite.

---

## Bottom line

SHADE `STATUS.md` is not usable as a current dashboard. It is a valuable March-2026 thesis snapshot, but it overstates immediacy if read today: prices, position rows, Jun18 option framing, and several catalyst windows are stale. The refreshed STATUS should preserve the core insurer-wrapper thesis while downgrading old "everything firing now" language into a current, source-tagged vector map.

Current working read from owner docs:
- **BROCK:** private-credit / semi-liquid fund stress has worsened materially since SHADE went stale: gate clusters, public-BDC dividend cuts, record private-credit default print, issuance slowdown, and first PE-wrapper contagion via Partners Group. BROCK owns those facts.
- **LIQUID:** broad HY confirmation is still absent/stalled near tight spreads; funding plumbing is clean; APO >$130 reassess fired but not with HY compression. This argues SHADE should frame insurer-wrapper risk as **structural/latent with named trigger paths**, not confirmed systemic cascade.
- **REGINALD:** bank/NDFI transmission remains relevant, but broad bank-cohort deterioration is more nuanced/idiosyncratic than old status implied. SHADE should not carry old bank-loss numbers as live without owner confirmation.

---

## Source audit

| Source | Current use in SHADE refresh | Key takeaways |
|---|---|---|
| `AGENTS/SHADE/STATUS.md` | Historical baseline; mine for thesis vectors and legacy key numbers | Last updated 2026-03-26. Contains stale APO ~$104, Jun18 option rows, AG55 "filings now" language, March NAIC/EJR framing. |
| `AGENTS/SHADE/research/NAIC_SPRING_MAR26.md` | Preserve as March regulatory baseline | PBR reinvestment guardrails adopted; AG55 filing period active; no public named Athene/SVO action; EJR SEC Aug12 clock. |
| `AGENTS/BROCK/STATUS.md` | Owner source for fund/BDC/gate/private-credit facts | 6/8 status: Stage 2→3 pivot; 4-fund gate cluster; Partners Group PE-wrapper gate; public-BDC div-cut cluster; Fitch PC default 6.0%; PC issuance -40% vs Q1. |
| `AGENTS/LIQUID/STATUS.md` | Owner source for macro credit/funding state | 6/13 status: HY OAS 278 (6/11), not confirming cascade; APO >$130 x4 close reassess fired but no HY compression; funding plumbing clean; broad credit still below confirmation. |
| `AGENTS/REGINALD/STATUS.md` | Owner source for bank/NDFI/FHLB transmission nuance | 6/8 status: NDFI/private-credit channel still relevant, but bank-cohort deterioration not broad/linear; WAL bear now idiosyncratic after cohort NCO decomp. |
| SHADE inbox Apr-May | Candidate signals; do not import unverified as fact | Signals point to insurance phantom assets/XOL, related-party dumps, Athene FHLB/FABR fast fuse, CFO/rated-feeder capital arbitrage, SIFI deregulation, Metcold/BlackRock recovery fragility. |

---

## What old STATUS should keep

1. **Domain framing:** PE-insurer/captive/offshore reinsurance structures as private-credit risk transmission wrappers.
2. **Primary vector set:** affiliated reinsurance, statutory reserve credit, FABN/funding-agreement liabilities, Egan Jones/rating machinery, AG55/PBR/NAIC pressure.
3. **Historical March baseline:** NAIC Spring outcomes, EJR SEC formal review/relief denial, AG55 first filing period, PHL Variable, PE-insurer/offshore reserve scale.
4. **Apollo/Athene as primary target:** Athene reserve credit / ACRA / FABN / deposit-type-contract framework remains central, but all figures require source/date tags and a current verification pass before trade use.

---

## What old STATUS must change

| Old STATUS element | Issue | Refresh action |
|---|---|---|
| `Signal Status: 🔴 CRITICAL — ESCALATING` | Too broad/current-sounding for a Mar26 stale file | Replace with a dated current read: likely **🟠 structural/latent, 🔴 on named fund-wrapper stress, systemic unconfirmed pending HY/funding/reg action**. |
| APO stock ~$104 / -23% YTD | Stale and directionally wrong vs LIQUID 6/13 APO $133.88 | Remove from dashboard unless refreshed live; note old price as historical only if needed. |
| Jun18 option rows | Position/expiry stale; SHADE should not own active trade rails unless Will requests | Move to historical/archive note or delete from live dashboard. |
| "AG55 first filings NOW" | March framing; by June should be checked/updated | Replace with "AG55 review/disclosure status: needs primary-source refresh." |
| Broad urgent outbox rows | HERMES/mail degraded and stale | Replace with current cross-agent dependencies / owner-source references. |
| BROCK FFIEC/bank exposure numbers | Needs owner confirmation; bank/NDFI is REGINALD/LIQUID/BROCK-adjacent | Reference owner docs rather than carrying live values. |
| Form PF/regulatory pressure implication | BROCK later reframed Form PF as largely deregulatory | Do not use generic "regulatory action escalating" without distinguishing NAIC/PBR/AG55 from SEC Form PF. |

---

## Proposed new STATUS vector model

| Vector | Current owner/input | SHADE-specific question | Initial Phase-1 stance |
|---|---|---|---|
| **1. Insurer asset-transfer / affiliated exposure** | BROCK for stressed asset/fund facts; SHADE for insurer balance sheet | Are stressed/illiquid private-credit assets being transferred, financed, or obscured inside insurer/captive affiliates? | 🔴 structural watch; needs current Apollo/Athene/Kuvare/GA/Aspida source refresh. |
| **2. Funding fragility** | LIQUID for broad funding; SHADE for FABN/FHLB/funding agreements | Are FABN/FHLB/funding-agreement liabilities rolling cleanly or repricing into stress? | 🟠 structural; no broad funding stress per LIQUID, but insurer-specific fast fuse remains open. |
| **3. Regulatory capital / NAIC-PBR-AG55** | SHADE primary; regulatory sources needed | Are PBR/AG55/SVO changes forcing disclosure/capital pressure? | 🟠 active but unverified post-Mar26; needs primary-source follow-up. |
| **4. Ratings / valuation machinery** | SHADE primary; EJR/NAIC/SVO/rating docs | Are private ratings/CFO/rated-feeder structures losing capital-efficiency credibility? | 🟠 EJR SEC Aug12 remains live; CFO/rated-feeder signal important but needs source verification. |
| **5. BROCK stress translation** | BROCK | Which private-credit stress facts matter to insurers rather than just funds? | 🔴 gates/defaults/div cuts matter only if they hit insurer allocations, capital marks, or funding confidence. |
| **6. System transmission** | LIQUID/REGINALD/NEXUS | Does insurer-wrapper stress feed broad credit/banks, or remain latent? | 🟡/🟠 broad confirmation absent; do not call systemic cascade yet. |

---

## Candidate STATUS structure for Phase 2

1. **Header / current read** — dated, with explicit stale-history note.
2. **Dashboard** — six vector rows above, source-tagged and owner-tagged.
3. **Insurer-wrapper transmission map** — BROCK fund stress → insurer balance sheet/funding/reg capital → LIQUID/REGINALD/NEXUS channels.
4. **Primary targets** — Apollo/Athene first; KKR/Global Atlantic, Ares/Aspida/IHAM-adjacent, Blue Owl/Kuvare as watchlist.
5. **Regulatory/funding calendar** — AG55/PBR/SVO/EJR/FABN windows; only forward-looking, source-tagged.
6. **Cross-agent dependencies** — BROCK facts, LIQUID broad credit/funding, REGINALD bank/NDFI.
7. **Next actions** — targeted primary-source pulls.
8. **Historical archive note** — point to old Mar26 content/research rather than deleting useful history.

---

## Targeted primary-source refresh list for Phase 3

Minimum viable refresh before trade-relevant claims:
1. **Apollo/Athene** — latest quarterly/annual/statutory materials; FABN/funding agreement maturities; Athene/Apollo commentary on private credit/CLO/AMAPS; any NAIC capital-charge disclosures.
2. **NAIC / SVO / AG55 / PBR** — post-Mar26 updates, adopted text/status, whether AG55 disclosures became visible.
3. **Egan Jones / SEC** — current status of Aug12 formal review track; any new SEC/DOJ/rating recognition changes.
4. **Kuvare / Global Atlantic / Aspida** — only enough to populate watchlist; do not deep-dive until Apollo/Athene is current.
5. **FHLB/FABN insurer funding** — source current insurer-specific borrowing/funding spread evidence if available.

---

## Phase 1 conclusion

Do **not** rewrite SHADE STATUS as "March thesis plus new BROCK facts." The correct rewrite is a cleaner insurer-wrapper dashboard that explicitly separates:
- fund stress (**BROCK-owned**),
- macro credit/funding confirmation (**LIQUID-owned**),
- bank/NDFI transmission (**REGINALD-owned**), and
- insurer-wrapper mechanisms (**SHADE-owned**).

Recommended next step: Phase 2 draft a new STATUS skeleton from this map, with placeholders for Phase 3 primary-source refresh rather than pretending unresolved facts are current.
