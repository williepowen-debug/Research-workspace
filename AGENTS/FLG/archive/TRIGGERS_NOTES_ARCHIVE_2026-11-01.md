# FLG TRIGGERS NOTES ARCHIVE — rotated 2026-11-01

Verbatim Notes cell rotated out of `workbook/TRIGGERS.tsv` row T-01 on 2026-11-01, when T-01 was consumed (Q3-2026 Call Report ingested, KB-FLG-099) and re-dated to the Q4-2026 Call Report. History, never current — its FFIEC-token expiry (2026-11-05) is superseded (KB-FLG-103). crc32 of the segment (UTF-8 bytes, exactly as between the fences): `baafe99a`.

## T-01

```
Date = quarter-end 2026-09-30 + 45d filing lag (RULE-derived, not an announced date). Call Report data is RESTATED — amendments can cross a line months later. | ⚠️ ACCESS DEPENDENCY (2026-10-22, DAEDALUS finding 11): the FFIEC CDR JWT expires 2026-11-05 (DOCKET L180; WILL_QUEUE row 31 = Will regenerates), BEFORE this row's ~11/14 check. FALLBACK PROVEN 10/22: FDIC BankFind financials API, cert 32541 = RSSD 694904, no token; it reproduced SR 07-1 327.5% and total RBC $10,003,181K at 6/30/26 exactly (KB-FLG-080). Use it if the token lapses; label the cells FDIC-published, not CDR. | 2026-10-28 FLG: CDR token WORKED — Q1+Q2 2026 facsimiles pulled, MI3 cells exact, SR 07-1 327.52% (KB-098); Q3 = CDR Error 204 (not yet filed). The 11/05 token expiry above still stands; FDIC fallback unchanged.
```
