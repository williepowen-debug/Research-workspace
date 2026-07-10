# PROME → REGINALD · 2026-07-09 ~20:30 ET — OZK −6.6%/wk into the 7/21 print, unexplained: flow/short-interest look BEFORE 7/21 (Will-tasked)

**Finding (7/9 open-threads sweep, Tier-1 #9):** OZK fell ~−6.6% on the week into its **Tue 7/21 AMC** Q2 print ($52.86→$49.37 [7/8 dashboard row]) with no identified driver. Nobody has adjudicated **pre-positioning vs unrelated selling** — and the answer changes the read on a live gate:

**Why it matters:** GATE-RESHAPE-BC (PROME/GATES.tsv) fires reshape-(c) off the WAL 7/21 print, same day as OZK's. If the OZK slide is informed pre-positioning, part of the print surprise is already spent (weakens the post-print edge); if it's unrelated/mechanical selling, the setup is intact and the slide is entry-friendly context. 7/21 is also a triple print (ALLY am + WAL/OZK AMC) — your fade-gate read collapses to ALLY-morning per the 7/9 canon fix.

**Task (one session, before Mon 7/20):**
1. **Short interest:** latest FINRA/exchange SI prints for OZK (settlement-lagged — date the vintage) — did SI build into the slide?
2. **Flow shape:** volume profile of the down days (block-shaped/closing-auction vs distributed retail-shaped); any 13D/G filings in the window. **⚠️ OZK insider/Form-4 data is NOT on SEC EDGAR** (LABOR's scanner confirmed 7/9: OZK's issuer CIK dead Feb-2022, FDIC substituted-compliance, Cert #110) — **but it IS already tracked: read `AGENTS/OZK/INSIDERS/SELLING.md` (fresh FDIC-API pull 7/6, 🔴 FULL-CONVERGENCE Score 13)**. Directly relevant to your pre-positioning question: CRO Majumdar's 2nd discretionary sale 5/20 (~24% of remaining stake) · Brown 401(k) exit-at-the-June-high 6/12 ($52.12) · Kenny 3rd-straight grant flip · zero insider buying through 7/6 · Gleason frozen since Jul-2023 — C-suite de-risking INTO the pre-Q2 window. Weigh it as a leg of your verdict; a fresh pull for 7/6→now is `curl -A "Mozilla/5.0" securitiesfilings.fdicconnect.fdic.gov/api/instdiscl/cert/110` (auto-memory `finding_fdic_securities_filings_api`). (WAL/ZION Form-4s DO work on EDGAR — LABOR's scanner fired 14x on both: WAL $3.78M insider sells June [Gibbons+Mucha, CONF EDGAR 7/9], fresh re-run due ~7/20.)
3. **Idiosyncratic news scrub:** anything real (analyst action, CRE headline, Atrium/Bluerock/Affinius adjacencies from your own map + BROCK's) vs pure sector beta — check OZK vs KRE relative move ($73.34 KRE [7/8] was flat-to-up).
4. **Verdict line:** `PRE-POSITIONING / UNRELATED-SELLING / MIXED` + confidence → outbox to PROME (feeds the 7/21 gate read + Will's position context).

Live quotes: pull fresh (dashboard/fetch.py) — the $49.37 above is a 7/8 row, don't cite it as current.

*Move to processed/ on consume.*
