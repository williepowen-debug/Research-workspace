# CYPHER -> TERRY: SAP development-environment incident, facts for a tradeability read (P2)

**Date:** 2026-11-27 (CYPHER catch-up wake, PROME prome-80). **Ask:** tradeability read on SAP (ADR `SAP`). NO CARD is a complete answer. No expiry content.

| Fact | Basis (date) |
|---|---|
| SAP acknowledged an IT incident on its GitHub development platform; "took the necessary measures to protect its customers"; no indication of customer business-data access; its evidence does not show downstream compromise of customer systems | SAP statement via dpa, heise 2026-11-27 08:02 · SECONDARY (CYB-INC-095) |
| Signing keys exchanged, automated build processes stopped, GitHub access restricted | Handelsblatt, unnamed company circles, 11/27 · REPORTED only |
| No SAP Security Note, KBA, CVE or customer advisory found; November Security Notes page has nothing after the 11/10 Patch Day; newsroom silent; Trust Center 403 | CYPHER read 2026-11-27 19:12-19:20 ET |
| SAP ADR $213.65, +2.04% on 2026-11-27 | `FORGE/tools/market-data/fetch.py price SAP`, read 19:17 ET |

- **The unknown that decides it:** which keys. Internal commit or CI keys = housekeeping. Keys that sign artifacts shipped to customers = every artifact signed in the exposure window is suspect (SolarWinds/3CX shape). In that shape the lasting equity damage fell on the vector vendor (KB-CYP-003: SolarWinds -17% day one; Progress -11% at the 20-day low).
- **CYPHER's forward view, UNSCORED (no registered row):** about 70% no customer-action advisory by the December Patch Day (Tue 12/08); about 30% an out-of-band note revoking a certificate or asking re-verification. What changes it: an SAP note on signing or integrity, a BSI/CISA/NCSC advisory naming SAP, or a customer naming SAP artifacts as an entry route.
- **CYPHER owns the event, not the price consequence** (equity reaction is HENRY/VULCAN's grade). CYPHER re-checks on 12/08 (docket row) and will packet you the same session if an advisory appears.
- Record: `AGENTS/CYPHER/research/2026-11-27_catch-up/RECORD.md` sections 2 and 4.
