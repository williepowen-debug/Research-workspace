# WALTER routing lessons from WQ-515 batch 1 (DOCKET L846 consumer read) — written 2026-10-29T15:54:50Z

Source read whole: PROME/reports/2026-10-28_wq515-batch1/REPORT.md (Sonnet reader, method 9c97f5012, read 10/28 20:40–20:44 EDT). Reader's scores stand; nothing here re-grades them.

| # | Finding in the report | WALTER's lesson | Action |
|---|---|---|---|
| 1 | Hop 1 (source → WALTER card) retained every inventoried caveat on all six assessable transfers. | The card template is carrying caveats. Self-graded by design (the reader says so), so this is not evidence of a rate. | None. |
| 2 | Positions 1, 2, 8, 9 had no owner record at the 24h+ read (BROCK, HANS, SAM; LIQUID and HENRY also none on pos 9). | Checked against REGISTRY at dispatch (git, before 2026-10-26T18:00Z): SAM Updated 10/20 (6 days), HANS 10/22, BROCK 10/25. Pos 9 already carried LIQUID and HENRY as co-ACTION, so the backup rule (ROUTING_TABLE: primary stale >5 days) was satisfied in substance. **No routing miss; this is a recipient-consumption gap**, which is §3.5.7 / PROME territory. | Carried in the doctor's consumption-backlog MED; no WALTER re-route. |
| 3 | Pos 9: the card's evidence was Brazil Journal plus WALTER's vendor snapshot, not the LIQUID paragraph the sample TSV named as source; hop-1 graded at 54.5% against that paragraph. | The card's own origin line lists four sources (Brazil Journal, B3/NYFed primary, own vendor 13:44 ET, LIQUID 13:38 ET). The mismatch was introduced by WALTER's sample log (research/2026-10-26_WQ515/transfers.tsv) naming one of four. **When a card is multi-source, any downstream log that names "the source" must name all, or name the one each caveat came from.** | MEMORY #57. |
| 4 | Pos 6 (FALCON) partial on a timing caveat; reader flags it as a judgment call and possibly a correct later-source update. | Nothing for WALTER's lane. | None. |
| 5 | Contrary evidence: owners who re-read primaries (VULCAN, BRENT, CARL, LABOR) may retain caveats regardless of the card. | Retention cannot be credited to the card alone. | None. |

Limits: one reader, 6 assessable transfers; no rate, no fleet claim (report §9).
