# MARCO Research Status Index

**Updated:** 2026-06-15
**Purpose:** Track research thread status to prevent re-investigation

---

## Status Categories

| Status | Meaning |
|--------|---------|
| EXHAUSTED | OSINT exhausted - do not re-investigate without new external lead |
| COMPLETE | Fully documented - monitor for news only |
| ACTIVE | Currently investigating or watching for triggers |
| DORMANT | Paused pending external development |
| GAPS | Known unknowns that could be researched |

---

## EXHAUSTED THREADS

<!-- Add threads here as they're exhausted -->

| Thread | Summary | Date Closed | Unlock Condition |
|--------|---------|-------------|------------------|
| | | | |

---

## COMPLETE THREADS

<!-- Fully documented, monitor only -->

| Thread | Summary | Documentation |
|--------|---------|---------------|
| Produce-spike attribution | RESOLVED 2026-05-31 (deep-research + verification). Spike is MULTI-CAUSAL — labor SECONDARY (~10-20%); real co-drivers = FL freeze ($3.17B, verified), tomato tariff (17%), diesel. MAR-21 cut 75→50. Exact %-split unknowable. | `domain/sources/PRODUCE_ATTRIBUTION_DECOMP_2026-05-31.md` |
| Remittance paradox | RESOLVED 2026-06-02 — Apr Banxico: $ +3.7% YoY / count -1.7% (narrowing from -3.6%), avg-transfer premium compressing. Tax-pull-forward signature FADING toward normal, NO Q2-Q3 air-pocket. Count still negative = SDL-01 senders-fewer tell intact. | STATUS "Mexico Remittances" row; KB |
| FLL April pax | RESOLVED 2026-06-15 — pdfminer on Broward PDF: total +5.0% YoY but -4.7% 2-yr stack (base-effect); intl +4.6% YoY / -18.7% stack (structural). MIA done (-2.02% Apr). MCO still blocked → BTS T-100 ~Jul. 🔴 **2026-08-21: THAT ROUTE IS NOW DEAD — do not retry.** broward.org rebuilt as an SPA; the legacy document tree 404s (7 months tested), Wayback empty. **The April result stands; the method for getting new months does not.** MIA's route IS live and verified 8/21 (`miami-airport.com/airport_stats.asp`, note the double space in the filename). | STATUS "FL Airports" row; KB-MARCO-IVF-30 |

---

## ACTIVE THREADS

<!-- Currently investigating -->

| Thread | Focus | Next Action |
|--------|-------|-------------|
| Ag-weather / crop-disaster monitoring | Gap exposed by produce decomp — fleet missed the real $3.17B FL freeze. No agent owns ag-weather. | OPEN LOOP — flagged PROME (outbox 5/31); owner still unassigned. Chase PROME for assignment. MARCO candidate (FL-adjacent). |

---

## DORMANT THREADS

<!-- Paused pending external development -->

| Thread | Waiting For | Last Checked |
|--------|-------------|--------------|
| TOURISM sub-agent $-at-risk v0 | **DECISION 6/15: SHELVE the sub-agent, KEEP the vector.** Sub-agent never delivered (no commits since Apr 22); MARCO handles tourism inline (session-9 refresh, 6/2 WC pull, StatCan May integration, 6/15 FLL pull). Vector LIVE (ES-09 WC reversal test runs through ~Aug). The prior "stalled / vector softened" label was misleading — the *content* is current, only the ROOMS sub-agent is dormant; re-spawn only if a dedicated $-at-risk grid build is greenlit. | 2026-06-15 |
| ICE off-farm pivot | Q4 2026 — does ag enforcement resume post-harvest? Re-accelerates SDL-01 if so. | 2026-05-31 |
| Cattle/meatpacking consolidation | Beef-belt plant closures → immigrant layoffs (separate from SDL-01). Queued since Apr 21. | 2026-05-31 |

---

## GAPS

<!-- Known unknowns worth investigating -->

| Gap | Why It Matters | Priority |
|-----|----------------|----------|
| StatCan Q2 2026 BOP | Q1 BOP released ~May 28 (Canada net travel-services exporter +$1.3B — integrated). Next data = Q2 (~Aug 28). | 🟡 |
| MCO April YoY pax | MIA done (-2.02% Apr); FLL done 6/15 (+5.0% YoY / -4.7% stack, pdfminer on Broward PDF). MCO still blocked (flymco JS-rendered, no extractable PDF) → BTS T-100 ~Jul. MAR-24 (all-3-negative) test. | 🟡 |
| Produce attribution sub-components | Which crops/regions drive the +6.1%? Isolate labor-intensive (berries, leafy greens) vs commodity | 🟡 |

---

*Check this file before suggesting any research direction.*
