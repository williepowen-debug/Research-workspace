# VULCAN CoreWeave organization implementation

Observed 2026-10-20T15:10:59-04:00. Will authorized completion of the organization review.

Result:20 company-specific rows now have authority at AGENTS/VULCAN/CRWV/KB.tsv;227 broader rows at AGENTS/VULCAN/workbook/KB_GENERAL.tsv. AGENTS/VULCAN/workbook/KB.tsv remains a generated combined read view at the historical consumer path. All247 IDs/fields and initial legacy bytes conserved; no manual duplicate authority.

Writer instructions changed: use the single source, then python3 AGENTS/VULCAN/scripts/kb_catalog.py --write. --find returns authority; --next-id spans both sources. The workbook validator (boot/closeout) enforces13 declared ledgers plus cross-source uniqueness/view equality/permanent-ID preservation. LEDGER_GLOB includes companyKB; all source dates retained.

CRWV/README.md is the entry point. CORRECTIONS.md maps old qualifications; READING_GUIDE.md/CATALOG.json reduce86 copies to48 reading entries with all aliases and distinct recipient variants preserved. The frozen36-row KB and original source map remain historical.

No score, forecast, gate, cadence or capital change. No new research launch requested. Native cross-fleet discovery/notification/consumption unverified; file delivery only.

## COMPLETION — VULCAN — 2026-10-20
STATUS: DONE
CHANGED: Company/general KB authorities, compatibility generator/check, schema/staleness/validator coverage, topic catalogue, correction map, maintenance instructions and own continuity.
RESULT: Approved organization work implemented;12new migration/library regressions and41existing validator cases passed.
GAPS: Company financial underwriting questions remain unchanged; no actual SEC filing archive or current quote refresh claimed.
WILL_NEEDS: None.
FOLLOW-UP: Existing schedule unchanged; future KB writers use canonical sources and regenerate the combined view.
