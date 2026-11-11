# STATUS rotation 2026-11-11 (set b) — the November 10 rotation receipts and the November 10 refresh header line, VERBATIM

PAYLOAD RULE: the payload is everything after the line '---PAYLOAD---' below, with the single trailing newline stripped. UTF-8 BYTES 922, crc32 7290f958.

---PAYLOAD---
**Rotated 2026-11-10 (two sets):** set 1 → [archive](archive/STATUS_dated_2026-11-10_rotation.md), 2069 B crc32 `14e95759`; set 2 (November 9 block and summary, older receipts, header lines) → [archive](archive/STATUS_dated_2026-11-10b_rotation.md), 7017 B crc32 `7603e4b9`. Graded catalyst rows older than a week → [prune](archive/CATALYSTS_pruned_2026-11-10.tsv).

**Last real market/source refresh:** November 10, 11:39–12:0x EST: vendor bars BZF27/BZG27/BZH27/CLZ26/CLF27/HO/RB, 11/9 settles (wire relay + vendor daily row), GASREGW 11/9 (FRED + EIA API), November STEO (EIA API two vintages + text), FRED Dated Brent (newest still 11/3). Not refreshed: insurance quotes, FINRA USO short interest, COT (next 11/13). JWC index re-fetched 12:07 EST (still JWLA-035). Prior header lines → [rotation](archive/STATUS_dated_2026-11-10b_rotation.md). Positions/receipts → [TRADE](TRADE.md); broker truth off-repo.
