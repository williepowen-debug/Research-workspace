# UNG bounded refresh — 2026-11-02T10:23:00-05:00

| Item | Evidence / disposition |
|---|---|
| Authority | WALTER packet f28fc8021, Will selected “Check trigger and refresh the card”; PROME same-task resume. No alternate fire route or order authorized. |
| Owner record | Read AEOLUS STATUS C3 and recent commits: last numerical observation +14.1 m/s [10/29 00Z]. Trigger NOT-FIRED on record; current physical observation UNKNOWN. PROME coordinates owner. |
| Quotes | fetch.py returned UNG $9.22 +1.49% in 10:20–10:21 EST retrieval bracket; source tool transcript. Separate chain 10:22:02 local spot $9.185. No exchange quote time or per-leg bid/ask time supplied. |
| Chain arithmetic | 10C .89/.95 minus 12C .48/.62 => purchase outer .47, sale outer .27, mid .37; round trip .20 / .37 = 54.05%. x5 .47 loss $241.50 after $6.50 opening fees; unchanged .50 cap loss $256.50. Short-leg width 25.45%; broker complex quote needed. |
| Data preservation | successful_tool_excerpt.json explicitly transcribes selected fields from the successful tool output. prices.txt / chain_jan15.json and retry files preserve failed saved requests plus stderr/return codes. Empty JSON is a failed request, not a market quote. CF/TLT temporary attempts belong to the continuing WQ-590 work and are not relied on for this refresh. |
| Guard reading | DAEDALUS Gate Basis #3 consumed. Prior completed close >=10.40 permanently voids pre-entry; entry quote must separately be <10.40. Both operate jointly; synthetic prior close 10.45 / later quote 10.30 stays void. PROME owns GATES summary write-back. |
| Observation reading | Original prose/fallback and AEOLUS-logged T1 have a wording distinction. Preserve it; this refresh makes no TERRY-derived fire or trigger waiver. |
| Book / scope | No order, fill, approval change, held-line prompt, new scoring or monitoring. WQ-573 already records Will's X1 choice for conditional x5; no second approval requested for the same card. |

## Source arrival integrated — 2026-11-02T10:24:32-05:00

WALTER d7218258c / BOARD 007 supplied NOAA GFS November 2 06Z f000, exact 60N / 10 hPa / 1,440 equally spaced longitudes. TERRY independently decoded the saved GRIB2 simple-packing payload and recovered +5.531545627 m/s; hash matches WALTER. Accepted as a sampled, nonqualifying analysis on the intended variable. No duplicate network fetch. This narrows the earlier UNKNOWN: a current positive GFS sample is available, while AEOLUS canonical acceptance/logging and any unsampled intraday reversal remain unknown. The earlier +14.1 ECMWF and this GFS sample are different models, not a measured same-series delta. Daily 00Z October 29 through November 2 are also positive in WALTER's five-row sample; that does not prove continuous non-reversal.
