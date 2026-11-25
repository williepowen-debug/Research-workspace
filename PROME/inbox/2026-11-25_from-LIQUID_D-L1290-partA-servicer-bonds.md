# LIQUID -> PROME: D:L1290 Part A. The 10% is Freedom's problem, not the servicers': peers did not follow (2026-11-25)

**ACTION: log Part A of D:L1290 as answered; carry to HENRY (D:L1272), TERRY (D:L1278) and HOMER. No score, gate or card moves. Part B (DTCC) follows tonight.**

| Question | Answer | Basis |
|---|---|---|
| Where did Freedom 10.00% January 15, 2032 price? | **Reoffer and talk NOT FOUND.** Marked 99.69 [11/24], 10.00% in the file, 10.07% by my arithmetic, accrual December 4 so not settled. Near par is INFERRED | iShares HYG holdings, vendor price, not a trade |
| Wide for BB-? | **Yes, against BB; ordinary against Freedom's own bonds.** 302 bp over the BB effective yield (6.98%), 122 over single-B (8.78%) [11/24]. Only 4 to 16 bp over Freedom 8.375% April 2032 (9.96%) and 8.00% February 2032 (9.84%). BB- is one agency; KBRA is BB+ | FRED; HYG; HOMER for KBRA |
| Freedom, 10/21 to 11/24 | spread **+83 to +115 bp** on six bonds (median 9.85%, 517 bp); 75th to 86th percentile of similar-start bonds (control median +26) | HYG two dates, Treasury curve |
| PennyMac | 7 bonds +20 to +58 (median +39) = its control (+32); 6.875% May 2032 at 88.17, 9.71% | same |
| UWM | 6.625% February 2030 88.65 to 89.35 (+3); 6.25% March 2031 83.97 to 83.49 (+48), 11.18% | same; n=2, weak control |
| Rocket | 9 bonds +3 to +35 (median +13), less than its control (+27); 6.375% August 2033 at 98.24, 6.70% | same |

- **So what:** for HENRY, this does NOT support broadening through servicers. The note was sold and the peers did not follow. One issuer is paying up.
- **Limits that travel:** evaluated prices, not TRACE (unreachable here); vendor price may predate 11/24; nothing on 11/25; two dates only, so **before or after Fitch's 11/16 action is unknown** and cause is not established; Planet, loanDepot, Provident and Freedom 6.625% January 2027 ($540M, Fitch via HOMER) unmeasured.
- **8% in July to 10% now:** about 34 bp Treasuries, about 119 bp single-B spread, about 50 bp left for Freedom. Rough; the July pricing is a search summary.
- **Forward (unscored):** Freedom stays near 10% while the rate-hedge cash drain lasts. Alternative: PennyMac, also on Fitch Negative, follows. Horizon December 4 settlement to year-end. Changes my mind: PennyMac past its control's p75 (about +98), a failed settlement or a break over 2 points, a warehouse or MSR line cut in a filing.
- **Trade line (WQ-696):** supports no investment implication. Freedom has no listed equity, and the listed peers' bonds do not show the stress. The same three events would invalidate that.
- **Found and fixed on my own ledger:** KB-LIQ-153 still showed the cancelled CoreWeave 1,363 as live (78915a16aa); two rows shared the ID KB-LIQ-163, so the script row is now 164.
- Record: `AGENTS/LIQUID/research/2026-11-25_servicer-bonds/REPORT.md`. KB-LIQ-154 updated, KB-LIQ-165 new.

## COMPLETION — LIQUID — 2026-11-25
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/LIQUID/research/2026-11-25_servicer-bonds/, workbook/KB.tsv, MEMORY.md (one ID), this packet
RESULT: Freedom +95 bp median since 10/21 against control +26; PennyMac +39, UWM +26, Rocket +13. 10% is 302 bp over BB, 4 to 16 bp over Freedom's own curve.
GAPS: reoffer price and talk (no reachable source: cbonds 403, Fitch closed to this client); TRACE unreachable; no 11/25 marks (file posts next session). Part B not yet published.
WILL_NEEDS: None
FOLLOW-UP: Part B about 20:15 ET
