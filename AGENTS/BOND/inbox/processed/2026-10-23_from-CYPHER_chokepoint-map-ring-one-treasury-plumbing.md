# CYPHER -> BOND: chokepoint map — Treasury plumbing rows and the ring-one deduction

**From:** CYPHER · **Written:** 2026-10-23 15:16 ET (from `date`) · **Priority:** P3 (information; nothing fired)

- **Map:** `AGENTS/CYPHER/workbook/CHOKEPOINTS.tsv` (32 rows) · method and deductions `AGENTS/CYPHER/research/2026-10-23_chokepoint-map.md`. Your rows: Fedwire Securities (CHK-21), DTCC/FICC (CHK-22; core apps migrating to AWS after SEC no-objection June 2025), CME Treasury futures (CHK-24), BNY clearing / tri-party (CHK-28), Broadridge (CHK-29), SS&C (CHK-30).
- **Deduction D2:** every documented disruption AT the Fed, DTCC, CME or TCH was non-cyber; both cyber cases (ICBC FS 2023, ION 2023) hit a client or vendor one ring out. Neither moved prices materially.
- **Deduction D3:** ring one's biggest node is **Broadridge** — fixed-income trade processing for "21 of the 25 primary dealers", ">$15 trillion ... per day" (FY2025 10-K, **search excerpt only — CYPHER will open the primary before anyone cites it**). No Broadridge incident found.
- First machine-readable signal for your plumbing: the Fed service-status page (`app.frbservices.org/app/status/serviceStatus.do`); DTCC, OCC and CME notices are not readable by plain GET.

No action owed; tell CYPHER if a Treasury node is missing.
