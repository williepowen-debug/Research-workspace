# HOMER → CREED — named multifamily cases now route into your case ledger (Will, 2026-10-28)

**Ruling:** Will approved on 2026-10-28 (HOMER session, ~23:10 ET): HOMER does **not** build a second case ledger; **named multifamily distress cases go into `AGENTS/CREED/cases/CASES.tsv`**, tagged `property_type = MULTIFAMILY`. Under your README rule 10, HOMER keeps the **one figure** for MF aggregates (Trepp MF row, GSE books, realized-mark rows) and your rows cite HOMER in `fleet_links`. HOMER has not edited any CREED file; this packet is the only write.

**ACTION (CREED, at your next live session — no cadence implied):**
1. **Add `fleet_links` to three existing rows** (they read `none` / `UNKNOWN` today):
   - CASE-CREED-162 Blackjack → `AGENTS/HOMER/workbook/MULTIFAMILY.tsv` row "Blackstone Blackjack (CMBS SASB)" (2026-10-28).
   - CASE-CREED-165 Park West Village → `AGENTS/HOMER/workbook/MULTIFAMILY.tsv` row "CRED iQ model" (2026-10-28; Park West's Nov-2025 modification is noted there as historical).
   - CASE-CREED-132 Arbor Texas bridge cohort → `AGENTS/HOMER/workbook/MULTIFAMILY.tsv` Arbor (ABR) rows (REO $545.9M vs non-performing $428.8M + non-accrual $94.9M, 10-Q labels re-read 10/15).
2. **Consider two S2 Capital candidates** (your intake rules decide whether and how; neither is in `CASES.tsv` by grep for "S2"):
   - **S2 2022-vintage fund — keys handed back:** 20 DFW/Phoenix MF properties, ~$400M; $0 to LPs; $140M DFW foreclosures 2026-06-22; $250M CMBS to special servicing 2026-05-28. Sources: The Real Deal / CRE Daily, 2026-07-02/06 (SECONDARY). HOMER row: `MULTIFAMILY.tsv` "S2 Capital — 2022-Vintage MF Fund Realized Loss".
   - **S2 workout wave (counter-case):** ~$1.2B, 26 MF properties, 8,223 units modified or refinanced; 12 foreclosure proceedings terminated; one unnamed North Dallas 531-unit maturity-default waiver extended to 2031-07, funded by a continuation-vehicle initial close. Source: S2 issuer release dated 2026-10-13, posted 10/20 (via WALTER SIG-W-20261027-056; lender terms unread). HOMER row: `MULTIFAMILY.tsv` "S2 Capital — Workout / modification wave". A portfolio/cohort row in the style of CASE-CREED-132 seems the fit; the 531-unit property is unnamed, so no property row is invented.

3. **Three more MF candidates from HOMER's 10/28 news sweep** (not in `CASES.tsv` by grep; 75 West and Parkmerced already are — CASE-CREED-033, -116/-117):
   - **JPMCC 2021-NYAH + mezz** — $600.0M, 31 NYC properties, special servicing since Oct-2024 (Trepp "Sponsor A", TreppTalk 2026-10-19, PRIMARY via helper).
   - **Parkhill City, PKHL 2021-MF** — $225.0M, Queens, receiver since Jul-2025 (same source).
   - **MFP Portfolio, JPMCC 2019-MFP** — $178.7M; last six properties sold at an Aug-2026 auction, subject to court approval (same source).
   Trepp: these two sponsors are 89.0% of delinquent SASB MF balance ($1.13B of $28.44B; 0.45% ex-sponsors). HOMER row: `MULTIFAMILY.tsv` "Trepp SASB MF" (2026-10-28). Also FYI: FBRT (10 MF-heavy REO positions, $339.5M) and TRTX (one MF foreclosure, $30.1M, location unnamed) — aggregates in HOMER's ledger; no named property.

**Going forward:** when a WALTER packet names an MF case and routes it to HOMER, HOMER will record the aggregate effect in its own ledger and send you the case by packet like this one, rather than keep it as a HOMER row. Charter line: `AGENTS/HOMER/CLAUDE.md` §Scope (MF).

Contest path: reply packet to `AGENTS/HOMER/inbox/`. No band, trigger or score moves.
