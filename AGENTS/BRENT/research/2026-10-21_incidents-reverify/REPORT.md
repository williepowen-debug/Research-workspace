# Incident re-verify: the 25 aged present-tense rows (2026-10-21)

**Run:** Will, 22:19 ET: "can you fix those now?" Two read-only Opus research helpers covered 13 rows (seven Gulf, six other). BRENT mapped the 12 Russian rows to OSPREY's live ledger (`AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv`, last commit 2026-10-21 21:29 ET) and searched Tuapse and Ufa itself. **Every status change and every date refresh below was re-read at its source by BRENT** (LESSONS #20). Helper claims that BRENT did not re-read are marked.

**Rules applied (unchanged from the 10/09 and 10/14 passes):**
- A search that finds nothing does not refresh `last_verified`.
- **Basis tiers:** **P** = operator or state statement (including an operator executive on the record, relayed by a wire). **W** = wire, or a major outlet citing its own sources. **A** = aggregator, analytics firm, brokerage, belligerent-side outlet or OSINT.
- **W or P** may refresh `last_verified`. **Only P** may change a status. A is recorded in notes only.
- `last_verified` carries the **evidence vintage** (the observation date), not the lookup date.
- Numerical outage fields are untouched except where an operator states full restoration.
- **Design choice:** later Russian re-strikes are not added as new INCIDENTS rows. OSPREY owns the RU-UA strike ledger (one source of truth per metric). The existing facility rows point to OSPREY's dated records instead.

## Dispositions

| Row | Facility | Before | After | Basis (tier) |
|---|---|---|---|---|
| RF-018 | SATORP, Jubail | PARTIAL_RESTART, 07-24 | **RESOLVED, 10-12**, offline ZERO-RESTORED | TotalEnergies CEO P. Pouyanné, 10/12 at Matignon, via ATS (bluewin.ch 15:44): « fonctionnelle à 100% depuis « début octobre » » [P via wire; BRENT read]. Written confirmation is due in TotalEnergies' Q3 results, **10/29**; re-check there |
| RF-038 | CPC Marine Terminal | PARTIAL_RESTART, 08-03 | **RESOLVED, 09-30** | Kazakhstan Energy Ministry (Astana Times 9/10): "no issues affecting the further conduct of loading operations were identified" [P; BRENT read]. Reuters via Baird 10/13: September throughput 6.0 Mt ≈ 1.59 mb/d vs 1.6 in August, decline on Karachaganak maintenance [W; helper read]. October run-state not established |
| RF-010 | Corpus Christi water | MONITORING, 08-04 | MONITORING, **10-21** | City page "as of 10/21/26": Stage 1 restrictions; combined storage 37.9% [P; BRENT read] |
| RF-008 | Valero Port Arthur | PARTIAL_RESTART, 06-30 | PARTIAL_RESTART, **07-30** | CFO Bhullar, Q2 call 7/30: DHT unit back "by year-end"; "the refinery continues to operate at normal throughput rates" [P; BRENT read]. Later event: a partial power outage around 9/1 (Tropical Storm Edouard) shut AVU-147 (Hydrocarbon Processing 9/2, unnamed sources) [W, helper]. Valero Q3 results are 10/22 |
| RF-021 | Viva Geelong | PARTIAL_RESTART, 08-21 | PARTIAL_RESTART, **08-25** | Viva ASX half-year presentation 8/25: "above 90% of normal operating capacity until Alkylation unit is repaired or replaced (beyond 2027)" [P; helper read, text saved `viva_0825.txt`] |
| RF-005 | Bazan Haifa | PARTIAL_RESTART, 03-20 | PARTIAL_RESTART, **08-28** | MEES 8/28: Q2 output 186,500 b/d vs 197,000 b/d distillation capacity [W; helper read, paywalled after the opening]. **Status-change candidate → RESOLVED**, pending Bazan's own report |
| RF-031 | MRPL Mangalore | DISPUTED, 04-17 | DISPUTED, **09-30** | Free Press Journal 10/15, "based on company exchange filings": Q2 FY27 throughput 4.18 MMT [W; helper read]. PL brokerage: −5.6% QoQ on maintenance [A]. **Status-change candidate → RESOLVED**, pending the NSE/BSE filing itself |
| RF-022 | Tuapse | ACTIVE, 04-21 | ACTIVE, **04-28** | Reuters 4/28 (wsau.com syndication): "operations have been halted since April 16 … industry sources said"; new fire 4/28 [W; BRENT read]. Still past the 60-day budget; no later restart found |
| RF-041 | Ryazan | MONITORING, 07-30 | MONITORING, **10-16** | OSPREY RU-20261015-RYAZAN: CDU-6 shut from 10/15 (Reuters two industry sources via Ukrinform 10/16); governor-confirmed fire [W/P] |
| RF-040 | Perm (PNOS) | MONITORING, 07-30 | MONITORING, **09-25** | OSPREY RU-20260925-PERM-LUKOIL: HALTED (Reuters via Meduza 9/25) [W] |
| RF-049 | YANOS Yaroslavl | MONITORING, 08-10 | MONITORING, **09-17** | OSPREY RU-20260917: crude processing suspended (Reuters via Ukrinform); governor damage confirmation [W/P] |
| RF-051 | Syzran | MONITORING, 08-10 | MONITORING, **09-16** | OSPREY RU-20260915-SYZRAN: halted 9/15, Reuters three industry sources, published 9/16; repairs ≥ 1 month [W] |
| RF-052 | Saratov | MONITORING, 08-10 | MONITORING, **09-16** | OSPREY RU-20260911-SARATOV: Reuters 9/16, halted 9/11 after a halt on 9/8 [W] |

**Rows refreshed with a halt still standing** (Ryazan, Perm, YANOS, Syzran, Saratov) keep MONITORING. Their halt evidence is W-tier, and a status change needs P. Their notes say "halted per Reuters" so no reader takes MONITORING to mean running.

## Not refreshed (notes only)

| Row | Why |
|---|---|
| RF-013 Ufa (ACTIVE) | No dated evidence on the 4/2 outage after the 10/09 pass. The 10/09 downgrade candidate (evidence of operation via FT relay) still waits for the FT/Bashneft primary. OSPREY's later Ufa-cluster strikes are covered by RF-046–048 |
| RF-014 Mina Al-Ahmadi (ACTIVE) | Nothing dated after 4/3; a KNPC test item is undated. Date trap: Arab Times 7/19/2025 |
| RF-033 VTTI Fujairah (ACTIVE) | No VTTI or operator item after 5/4 |
| RF-044 Jazan (ACTIVE) | Kpler 10/21 (Phil Jones-Lux; BRENT read): "the Jizan refinery on the Red Sea is not expected back until the end of December" [A, a forward expectation]. Consistent with ACTIVE, but A-tier does not refresh. Aramco Q3 results ~11/3 |
| RF-016 Habshan, RF-037 KOC platform, RF-045 Berri | Nothing newer than the existing date (ADNOC Gas Q3 and Aramco Q3 pending) |
| RF-046 Ufaneftekhim, RF-048 Novoil | OSPREY has no record after the existing events |
| RF-047 UNPZ, RF-050 Ilsky, RF-053 Taneco | OSPREY's later records rest on Ukrainian General Staff, belligerent or OSINT sources only (9/22, 9/26, 9/13) [A] |

## Result for the boot check

- **ACTIVE rows past the 60-day budget: still 5** (Ufa, Mina Al-Ahmadi, Tuapse, VTTI, Jazan). No P or W evidence on current state exists for them. Clearing them would mean inventing a restart or a renewed outage.
- **Other present-tense rows:** the boot disclosure list shrinks to the rows that could not be refreshed.

**Next dated primaries:** Valero Q3 10/22 (Port Arthur), TotalEnergies Q3 10/29 (SATORP written confirmation), Aramco Q3 ~11/3 (Jazan, Berri, SATORP), ADNOC Gas Q3 (Habshan), MRPL exchange filing (status change), Bazan Q2/Q3 report.

**Extra product evidence (for the Kpler check):** Kpler's 10/21 diesel-arbitrage note says "Exports from the Gulf are still about 50% below pre-war levels." That is product context, consistent with the 10/1 primary in `research/2026-10-21_eia-oct21/REPORT.md` §8.
