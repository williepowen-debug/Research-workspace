# MEMORY.md — HOMER Durable Notes

*Will's working preferences, do-not-touch quirks, and provenance facts that don't belong in STATUS (live data) or LESSONS (mistake patterns). Thin by design — grows only with genuinely durable facts.*

---

## Reporting to Will

- **Cash lines: say the direction in words, not only the signed figure** (DAEDALUS upgrade read of `filing_reader.py`, relayed by Will 2026-11-25 23:22 ET): e.g. "Rocket advances +$365M: cash came back in, advances fell", never a bare "+$365M". On a cash flow statement a positive figure added cash and a negative used it; say which, and say when the sign reading is mine rather than the issuer's.

## Promotion Provenance

- **2026-07-12:** Promoted from `AGENTS/CARL/sub_agents/HOMER/` to top-level `AGENTS/HOMER/` via `git mv` (history preserved). Will-directed, same-day execution — overrode CARL's own recommendation to wait until the post-7/24 quiet window (compressed review, not skipped; DAEDALUS structural review at `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`). Case originated from CARL: `AGENTS/DAEDALUS/inbox/2026-07-12_from-CARL_homer-promotion-case.md`.
- Zero live external consumers existed outside CARL's tree at promotion time (verified by DAEDALUS's comprehension pack) — the lowest-risk promotion of the OZK/CORAL/AEOLUS/HOMER precedent set.
- HOMER jumped the ROSTER promotion queue ahead of WAL (Will's explicit 7/12 call, recorded not re-litigated — WAL remains next-candidate).

## Do-Not-Touch / Structural Quirks

- **`workbook/KB.tsv` is FROZEN (2026-07-10)** — parent-era canonical KB, ~65 rows, CARL_ID provenance column intact. Do not append to it; do not renumber it. New rows go to `workbook/KB_LIVE.tsv`. The freeze banner is the row-ID-stability contract — breaking it breaks the delegation provenance CARL's own KB still cites.
- **`state_vectors/corrected/` is a retrieval hazard, not a normal subdirectory.** It holds exactly one withdrawn/superseded SV (SV-HOMER-2026-06-08-01). CARL's old harvest globs (and any future search) do NOT descend into `corrected/` — a valid/live SV must never be filed there. Kept as historical record only; the SV channel itself is retired (see CLAUDE.md).
- **`archive/` holds pre-promotion build artifacts** (GAP_ANALYSIS.md, REPORT.md, SPAWN1_DATA_REFRESH.md, UPDATE_PLAN.md) — Apr-vintage, already flagged in-file as archive candidates by the 7/10 verification pass. Historical record; no action needed unless a future sweep wants to prune further per the Data Hygiene >60d rule.
- `domain/` — **not in git** (nothing tracked; verified 2026-10-28); an EMPTY untracked `domain/` directory still exists on this box's disk (seen 2026-10-29) — harmless, holds nothing. Research lives in `reports/`.

## Cross-Agent Facts Worth Remembering

- REGINALD cites the monthly Trepp CMBS-MF print in its own STATUS (its CRE row carried Apr-2026 7.71% when checked 2026-09-29). **Ownership is settled: HOMER primary (promotion ruling); REGINALD cites.** No reconciliation row exists on my docket — this line used to point at one that was never there (dangling pointer, found 2026-09-29). If REGINALD's cited value drifts from `workbook/MULTIFAMILY.tsv`, packet REGINALD's inbox; never edit their file.
- CREED now keeps its own `workbook/` (KB, FLOW, PREDICTIONS; checked 2026-09-29 — the July note that it had none is superseded). The MF seam is unchanged: CREED pulls the whole Trepp print and owns non-MF property types; the MF row is mine (`CREED-T-05`). Check `PROME/ROSTER.md` for CREED's current tier; don't infer it from here.
- **WALTER's RESEARCH-INTAKE lane does NOT fetch homebuilder earnings or the ATTOM monthly foreclosure report** (verified 2026-09-29 with WALTER's own read-only harness: 0 lane hits for Lennar/KB over 6/29–9/28 although both reported). ⇒ **HOMER pulls these itself off per-name / recurring docket rows; never assume "WALTER would have routed it."** Matcher fact: all-caps 2–5 char tokens (KB, NVR, LGI) ARE kept; other ≤3-char words drop.

## Ownership seams added 2026-10-28

- **Named MF cases → CREED's case ledger** (`AGENTS/CREED/cases/CASES.tsv`, by packet; Will 10/28). HOMER keeps the aggregate figure only.
- **California wildfire peril + insurance market (FAIR Plan, insurer losses) = AEOLUS** (`AGENTS/AEOLUS/wildfire/`). HOMER's CA lane is the housing-credit consequence and cites AEOLUS.
- **HENRY edge formalized** (charter trigger rule); TERRY reached only via thesis/data — HOMER holds no book.

## Infra — what this box can and cannot reach (rewritten 2026-11-25; older notes → `archive/MEMORY_infra_notes_2026-11-25.md`)

Each row is the LAST observation, dated. Reachability changes; re-test before calling a source dead, and test a control page first (a 404 on a guessed address proves nothing). A site that challenges or refuses automation: stop, use another source (root Blocked sites).

| Source | Last observation | Address or fallback |
|---|---|---|
| Freddie PMMS · FMHPI | works 11/25 | `freddiemac.com/pmms/docs/PMMS_history.csv` · `freddiemac.com/fmac-resources/research/docs/fmhpi_master_file.csv` (national rows are `US,USA`) |
| Treasury par curve | works 11/24 | `home.treasury.gov/...daily-treasury-rates.csv` |
| FRED | works 11/25 (earlier HTTP/2 errors: retry `--http1.1`) | carries BEA and BLS lines |
| HUD FHA performance | works 11/25; **filenames vary** | `hud.gov/sites/default/files/Housing/documents/FHALPT-SEPT2026.pdf`; try underscore and hyphen forms. Annual report `2026FHAAnnualReportMMIFund.pdf`. Read EVERY table (LESSONS §56) |
| ICE First Look | works 11/25 | `mortgagetech.ice.com/resources/data-reports/first-look-at-<month>-<year>-mortgage-data` (September 200; a bare `/first-look` is 404); issuer PDF on `s2.q4cdn.com/154085107/files/doc_news/` (title-based name); Business Wire copy. Oct-2025 edition came Tue 2025-11-25 (Mondo Visione copy; corrected from 11/26) |
| ICE Mortgage Monitor | read 11/11 | `mortgagetech.ice.com/publicdocs/mortgage/ICE_Mortgage_Monitor_<Mon>_<YYYY>.pdf` (month abbreviation varies) |
| ATTOM | works 11/25 (August 200) | `/news/market-trends/foreclosures/<month>-2026-foreclosure-market-report/`; the Q3-2025 form was `q3-and-september-2025-...`. Sept, Oct, Q3 2026 and that form all 404 on 11/25 |
| Trepp | TreppTalk works; DQ PDF at `trepp.com/hubfs` read 11/05 | full special-servicing PDF not reached |
| Apartment List | works 11/25 | CSV name on `apartmentlist.com/research/category/data-rent-estimates` (ctfassets; the page links it protocol-relative, `//assets.ctfassets.net/...`) |
| S&P Case-Shiller | `press.spglobal.com` works 11/24 | the Cotality-hosted page once served stale data |
| NAHB | read 11/20 | HMI history `.xls` (`xlrd` is in `.venv`); NAHB Eye On Housing carries BEA residential |
| SEC EDGAR · api.fdic.gov · OpenFEMA | work 11/24–25 | EDGAR 10-Qs open with `sec_ua("HOMER-Research {}")` from `scripts/sec_contact.py` (used 11/25; never write the address in a file); confirm a disaster declaration at OpenFEMA, not press |
| MIAMI REALTORS | October release read 11/23 by a retrieval helper; empty to curl | issuer site |
| Fannie Monthly Summary | 403 to automation 11/24 | Will supplied October's PDF; quarter-end values from the 10-Q at EDGAR |
| MBA (mba.org) | 403 site-wide | `newslink.mba.org`; CalculatedRisk verbatim copies (SECONDARY) |
| National Mortgage News · American Banker | headline and bullets only (subscription) | sister titles by one author: never two sources |
| The Real Deal · Las Vegas Realtors | 403 (9/29) · 429 (11/11) | CRE Daily or Yahoo copies · Fox5/News3LV (SECONDARY) |
| BEA GDP PDF | no residential row in its text | FRED series; NAHB |
