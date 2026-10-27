# FERT approved build — working record

Authorization: Will in this FERT session, 2026-10-26: “Lets have you start working on these and documenting our findings into our file tree as we go”. This approves the domain-audit baseline work: CF, physical flows, farm affordability/intermediate prices, comparable economics and record cleanup. Existing potash triage, trade, paid-feed and gate-letter limits remain.

Started: 2026-10-27T03:23:51.492736+00:00

1. Initial CF baseline saved: 320 observations, segment/quarter reconciliations, earnings-quality bridge and Q3 checklist. Older Q3/Q4 history and project commitment detail remain research work.
2. Initial physical-flow baseline saved: 525 US import observations through August plus a September China export observation reported by Longzhong and SCI. Official China Customs access failed; primary/YTD verification remains open. One named facility, two guidance vintages; unknown capacity is not zero.
3. Farm/intermediate baseline saved: 36 ERS annual estimates and 99 BLS observations. Six aligned DTN N/P observations add relative context. Crop-specific prices, budgets and application behavior remain open.
4. Navigation/source routes and existing-wake hooks saved. KB lifecycle reviewed row-by-row; validation/delivery recorded below.

Evidence is saved under sources/ as retrieved; browser extracts are labelled extracts, never complete filing snapshots. Tables will retain period, unit, source locator and missing-value state. No market price is inferred from a trade unit value.

## Checkpoint — 2026-10-26 23:35 Monday (boot.py)

- Seven tables, **989 rows**, plus company dossier, source map and research synthesis. Offline extraction uses the repository virtual environment; system Python lacks pandas/BeautifulSoup. No new installed package, paid feed or scheduled collector.
- CF source tables reconcile segment sales, margins and sales volumes; Q1+Q2=H1 on additive metrics. CF's 10-Q explicitly defines tons as short tons. Litigation gain remains in issuer adjusted EBITDA but is removed from adjusted net earnings. Cash timing and insurance remain separate.
- US feed metadata proves nutrient-equivalent weight. Imports for consumption exclude export/re-export rows; query is grouped by HS/nutrient and bounded to fewer than 10,000 results. No zero imputation. China official portal failed TLS/browser; reported September export quantity retains MIRROR-WALLED and no primary-verification claim.
- BLS API returned Jan2024–Sep2026 despite requested start2025; actual observation range preserved. September observations preliminary. Browser PDF metadata confirms index base/NSA; requests403 bodies are failures, not source PDFs. Direct Census returned HTTP200 Missing Key HTML and was rejected.
- KB: **16 overdue ACTIVE rows classified** (7 SUPERSEDED, 9 STALE), **10 blank-deadline rows classified** (6 dated historical records CONFIRMED, 2 STALE, 2 scheduled at existing wakes). No historical fact declared false merely for age. Seventeen safe group aliases mapped; **12 POTASH/FERTILIZER_K rows** await vocabulary-owner action. Full dispositions: `kb_lifecycle_review.json`. Six new source-located claims KB-FERT-091..096.
- Owner-authored read-footprint declaration: `registry/READS_DECLARATION.tsv`; shared registry ingestion remains PROME's action. Whole TRIGGERS read on spawned boot is explicitly declared, alongside script summaries. New research/raw files are on-demand, not mandatory boot reads. Live read-cap verdict remains heuristic until PROME applies it.
- Existing trigger identities checked: T7 CF results, T10 China/call review, T8 NASS, T11 monthly World Bank source wake, T3 CPI, T4 DTN. Notes extended; Next_Check dates, instruments and gate letters unchanged. G4 remains declined; potash triage preserved.
- No figure used as a standing market/gate threshold is superseded by this build. New historical baselines retain dates; stale lifecycle labels do not regrade markets. Pull/push deferred while other owners have dirty work, per root Git procedures.

## Resume points

Follow `DATA_ROUTES.md` and `companies/CF/Q3_PREP.md` at the existing named wakes. Start with China official/YTD and CF Q3/commitment detail, then country import composition and crop-specific affordability. Initial baselines are complete; domain-wide coverage is still partial. This record does not promise unattended execution between sessions.

## Final closeout — requested by Will

The operator asked to document the initial interpretation and close this session. `reports/2026-10-26_closeout.md` records the distinction between 989 data rows and independent evidence, the current judgment, and resume points. No new market read or gate grade.

PROME has now consumed build commit 0ab3db312 on a bounded basis: hashes, seven table shapes/counts and CF additive EBITDA verified. Its consumption report is `PROME/reports/2026-10-26_fert-build-consumption.md`. This supersedes the earlier UNKNOWN consumption and pending-transcription notes above: 24 read rows were transcribed, but declaration remains PARTIAL/UNKNOWN because BASIS rows are missing and the optional correction-receipt file is absent. Owner correction and exact provisional potash affected-ID mapping remain for the existing maintenance wake, as expressly requested by PROME. No missing receipt was fabricated.

PROME could not reproduce the extractor because pandas import failed in its runtime. FERT rechecked successful imports and saved exact interpreter/package paths and versions in ENVIRONMENT.json; DATA_ROUTES and the report now qualify environment claims. No package installed. All source values and baseline counts remain unchanged.

The maintenance packet was read, logged as deferred and filed in processed/; the inbox receipt holds the resume pointer. Local commits and verified Codex notification complete this session's persistence/delivery work; other owners' dirty paths keep pull/push deferred. A notification acceptance is not consumption of the new closeout packet.
