# MARCO Research Status Index

**Updated:** 2026-09-24 (s30 stale sweep — prior 2026-06-15)
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
| FL airports — all three legs | CLOSED 2026-08-21 → 9/24: **BTS T-100** (`tools/bts_airport_pull.py`, ASP.NET form POST) covers MCO/FLL/MIA incl. carrier split (Spirit liquidation proven 8/21); **MIA's own Traffic Report PDF** is the graded MIA-trigger basis (Will-ruled 9/24). The MCO "blocked" gap below was a never-tried path, not a wall. | STATUS FL Airports row; MEMORY source map; KB-MARCO-APT-44/45 |
| Produce spike | CLOSED 2026-09-19 — `ES-MARCO-05` DID_NOT_APPEAR on the pre-committed Aug print (fresh F&V +3.13%); MAR-14 12%. Sub-component attribution no longer worth pulling. | STATUS dashboard; `_archive/STATUS_cold_20260924.md` |
| Sub-annual FL migration proxy | BUILT 2026-07-10 (`tools/fl_migration_proxies.py`: voter-reg monthly, FLHSMV, FLDOE) + OCPS enrollment pull 9/17 (−3.97%, migration share ≤2,032, confounded). Direction tells only. | `workbook/MIGRATION_PROXIES.tsv`; STATUS migration row |
| Channel 4 border fiscal/credit | CLOSED 2026-09-24 → thesis v3.2 LOW (Will-ruled). Replaces the never-run Feb muni-spread protocol (`archive/RP-MARCO-MBS_BASELINE.md`, EMMA terms-gated). Laredo watch 2027-03-31. | `domain/sources/BORDER/2026-09-24_border_municipal_credit_rebuild.md` |

---

## ACTIVE THREADS

<!-- Currently investigating -->

| Thread | Focus | Next Action |
|--------|-------|-------------|
| Ag-weather / crop-disaster monitoring | Gap exposed by produce decomp — fleet missed the real $3.17B FL freeze. No agent owns ag-weather. | OPEN LOOP since 5/31 — still no owner in ROSTER or any agent CLAUDE.md (grep 2026-09-24). Lower stakes now the produce channel is closed; re-raise to PROME only if a new weather shock hits produce. |

---

## DORMANT THREADS

<!-- Paused pending external development -->

| Thread | Waiting For | Last Checked |
|--------|-------------|--------------|
| TOURISM sub-agent $-at-risk v0 | **DECISION 6/15: SHELVE the sub-agent, KEEP the vector.** Sub-agent never delivered (no commits since Apr 22); MARCO handles tourism inline (session-9 refresh, 6/2 WC pull, StatCan May integration, 6/15 FLL pull). Vector LIVE (ES-09 WC reversal test runs through ~Aug). The prior "stalled / vector softened" label was misleading — the *content* is current, only the ROOMS sub-agent is dormant; re-spawn only if a dedicated $-at-risk grid build is greenlit. | 2026-06-15 |
| ICE off-farm pivot | Q4 2026 — does ag enforcement resume post-harvest? Re-accelerates SDL-01 if so. Construction raids stayed ON. | 2026-09-24 (no ag resumption seen) |
| Cattle/meatpacking consolidation | Beef-belt plant closures → immigrant layoffs (separate from SDL-01). Weekly slaughter fetcher runs at boot (`baselines/slaughter_weekly.tsv`); layoff list `baselines/beef_belt_layoffs.tsv` last row Nov-2025 — no analysis thread opened. | 2026-09-24 |

---

## GAPS

<!-- Known unknowns worth investigating -->

| Gap | Why It Matters | Priority |
|-----|----------------|----------|
| Spirit seat capacity at MCO/FLL | Capacity replacement has never been measured — only passenger offsets (MCO 97.8% May → 35.6% Jun). Until seats are sized, FL airport YoY cannot separate supply from demand. | 🟠 |
| `NV-01` Canadian basis | BREACHED rests on an unrefreshed Canadian sub-leg; LVCVA has no nativity split. Needs carrier-level AC/WestJet/Flair/Porter LAS capacity. | 🟠 |
| `VX-1.03` "loss" basis | Basis ruled 8/21 (YoY spending) but the fresh 2026 figure is unpulled. | 🟡 |
| `VX-2.01` arrest-rate leg | ICE/TRAC arrest rate still Jun-15 vintage. | 🟡 |
| USMCA preference under §338 | "Does not exempt" is not primary-supported (Proc. 11046 silent). | 🟡 |

*(Closed 2026-09-24: "MCO April YoY" → BTS T-100; "Produce attribution sub-components" → produce channel closed; "StatCan Q2 BOP" → pulled s30, see STATUS.)*

---

*Check this file before suggesting any research direction.*
