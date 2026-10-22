# Boot threshold scan — 2026-10-22 evening sitting (pulls 20:19–20:28Z)

Registries unchanged since the morning scan (`research/2026-10-22_boot/THRESHOLD-SCAN.md`): last commits RED canon 10/21 09:04, HANS 10/21 22:49, REGINALD 10/11, CREED 9/28. RED scan view banner hash 32203f81 == canon sha256 prefix. Only rows with a new observation since the morning are re-graded below; all others carry the morning grade with its dates.

| Row | Instrument / basis | New observation | Result |
|---|---|---|---|
| REG-T-01 | KRE close <60 | 72.41 (+2.53%) [10/22 vendor close, fetch.py 20:19Z] | not near |
| REG-T-02 | WAL close <78; exit ≥81.90 ×3 | 76.67 (+1.48%) [10/22 vendor close] | cycle-2 fired state; re-entry, exit 0 of 3 |
| RED-FT-06 / safety net | VIXCLS exit ≥18 ×5; VIX >30 or +5 intraday | ^VIX 18.90 (+13.31%, about +2.2 points) [10/22 vendor close]; VIXCLS 10/22 publishes 10/23 | intraday second witness only; no safety net |
| HY rows (FT-01/02/12, REG-T-03/04) | FRED BAMLH0A0HYM2 first-published | no new print (327 [10/21] latest); HYG $77.10 (+0.16%) vendor | morning grade holds; REG-T-04 23bp away, outside the 5% band |
| RED-FT-03 / -04, boundary 1/2 | Brent front settlement | BZ=F $113.04 (+3.88%) vendor 20:19Z; `contract_probe('BZ')` ~20:29Z: IDENTIFIED, tracking BZZ26.NYM $112.86 (control passed; BZF27 $108.45); vendor bar, not a settle | not near 130 / 75 / 120 |
| WTI | CLZ26 (resolved) | $99.31 (+2.22%) vendor | context only |
| RED-FT-11 | DGS30 5-session ≤ −10.2bp | ^TYX 5.29 (−2.79%) vendor; FRED DGS30 10/22 publishes 10/23 | precondition may meet again; RED classifies (routed in 031) |
| UST 10Y (context) | FRED DGS10 5.13 [10/21]; ^TNX 4.95 (−3.75%) vendor close | about −18bp one day | routed in 031 (not a registered row) |
| HANS VX-3.07 / T-10 | OAT level, i-i basis | Reuters intraday 5.06%, high 5.1415% (secondary) | HANS grades; routed IMMEDIATE in 031 |
| Cushing / boundary 3 | EIA weekly | 27.594M [w/e 10/16] unchanged | not near |

Safety net: no VIX >30 or +5 intraday, no HY +25bp single session observed. No sustained cross, so no auto-fire. Not a full-registry clearance: CREED/HANS event and qualitative legs were not re-swept by WALTER.
