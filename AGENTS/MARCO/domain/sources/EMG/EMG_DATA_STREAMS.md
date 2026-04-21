# VX-MARCO-EMG-01 — Data Stream Evaluation
**Purpose:** Select 3-5 trackable data sources to baseline American emigration rate
**Analyst:** Research sub-agent | **Date:** 2026-04-21
**Status:** PENDING → decision input; do not edit without fresh research

---

## VERDICT FIRST — Recommended Stack (Top 5)

| Rank | Source | Role in Triangulation | Cadence |
|------|--------|----------------------|---------|
| 1 | IRS Federal Register expatriate list | Hard count — renunciations | Quarterly |
| 2 | Canada IRCC open data — US PRs | Destination: largest receiving country | Monthly |
| 3 | Portugal AIMA annual report — US residents | Destination: fastest-growing EU cohort | Annual (Oct) |
| 4 | Google Trends basket | Leading intent indicator — 1-3mo lead | Daily/Weekly |
| 5 | Spain OPI visa data — non-lucrative by nationality | Destination: second EU corridor | Annual |

**Triangulation logic:**
- (a) Renunciations hard count → Source 1 only. No substitute exists.
- (b) Residency applications at destination countries → Sources 2, 3, 5 cover the three highest-volume corridors (Canada, Portugal, Spain). Mexico INM and Costa Rica DGME are theoretically complementary but data is not reliably public.
- (c) Leading-indicator intent → Source 4 (Google Trends). Historically leads hard counts by 1-3 months and captured post-election spikes. Reddit is no longer viable due to quarantine and API closure.

**Upgrade trigger for EMG-01 PENDING → ACTIVE:** 3+ consecutive quarters of Federal Register counts above 1,500 AND Canada IRCC US-citizen PRs showing YoY >25% growth.

---

## Full Source Evaluations

### 1. IRS Form 8854 / Federal Register Quarterly Expatriate List

| Field | Detail |
|-------|--------|
| Accessibility | Free public — federalregister.gov, govinfo.gov |
| Cadence | Quarterly (published within ~30 days of quarter end) |
| Lag | ~6-week lag. Most recent: Q4 2025 (published Jan 23, 2026) |
| Reliability | HIGH for renunciations specifically; MEDIUM for total emigrant count |
| Signal strength | Hard count of named individuals losing citizenship. 2024 total: ~4,920. Q1 2025: 1,285 (+102% YoY). 2025 full-year run-rate: >6,000 (projected record). Threshold: >1,500/quarter = structural acceleration |
| URL | https://www.federalregister.gov/quarterly-publication-of-individuals-who-have-chosen-to-expatriate |
| Effort | LOW — names listed in Fed Register; quarterly count extractable by counting entries or citing AARO/IMI Daily aggregations |
| Key caveats | Undercounts actual renunciations by ~2x (FBI background check system showed 13,110 in 2025 vs 5,986 IRS names). Excludes LPR abandoners (Form I-407, ~18K/yr historically). Counts only the most committed emigrants — demand for appointment already backlogged. Fee drop to $450 (April 2026) will likely inflate Q2-Q4 2026 counts |

---

### 2. Canada IRCC — US Citizen Permanent Residence Landings (Monthly Open Data)

| Field | Detail |
|-------|--------|
| Accessibility | Free public — Canada Open Government Portal |
| Cadence | Monthly (CSV/XLSX, updated monthly) |
| Lag | ~6-8 weeks. Coverage through Jan 2026 as of April 2026 |
| Reliability | HIGH — official government administrative data, values 0-5 suppressed for privacy |
| Signal strength | Monthly count of US citizens granted Canadian PR status, by program stream. Quantifies the largest single receiving country for American emigrants. Threshold: >500 US-citizen PRs/month = sustained structural inflow |
| URL | https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda (Permanent Residents by Country of Citizenship) |
| Effort | LOW-MEDIUM — CSV download, filter by "United States" citizenship, aggregate monthly |
| Key caveats | PR landings ≠ applications; typically 12-24 month lag between application and landing. Still measures realized inflow, which is what matters for population displacement. Applications received dataset also available separately: https://open.canada.ca/data/en/dataset/9b34e712-513f-44e9-babf-9df4f7256550 |

---

### 3. Portugal AIMA Annual Report — US Citizens Resident

| Field | Detail |
|-------|--------|
| Accessibility | Free public — AIMA publishes annual Relatório de Migrações e Asilo |
| Cadence | Annual (typically published October of following year) |
| Lag | ~10 months. 2024 data published Oct 2025 |
| Reliability | HIGH — official administrative count of legally resident foreigners by nationality |
| Signal strength | 2023: 14,126 US citizens resident. 2024: 19,258 (+36% YoY). Golden Visa: 406 US-citizen approvals in 2024 (leading nationality). Digital Nomad Visa: 22.4% of issuances to Americans in 2023. Survey: 49% of Americans in Portugal considering renouncing US citizenship. Threshold: >25,000 US residents OR >500 Golden Visa/yr = fast-track corridor confirmed |
| URL | aima.gov.pt (annual report section); aggregated at https://movingto.com/statistics/portugal-migration-statistics |
| Effort | MEDIUM — annual report is PDF; tables require extraction. Third-party aggregators (GetGoldenVisa, MovingTo.com) publish summaries within weeks of release |
| Key caveats | Annual only; no monthly breakdowns by nationality. Does not disaggregate D7 vs. Digital Nomad vs. Golden Visa by nationality in the public summary. Portugal tightening citizenship laws in 2026 — may dampen D7 inflows but accelerate naturalization queue |

---

### 4. Google Trends Basket — Emigration Intent Proxy

| Field | Detail |
|-------|--------|
| Accessibility | Free public — trends.google.com |
| Cadence | Daily (7-day rolling), Weekly (normalized index 0-100) |
| Lag | Real-time to 72hr |
| Reliability | MEDIUM — leading indicator of intent, not action. Prone to event-driven spikes that don't convert to moves |
| Signal strength | Post-election Nov 2024: "move abroad" searches up 1,514%. "How to move to Canada" peaked Nov 6, 2024. Netherlands searches +3,233%. Tracks intent 1-3 months ahead of visa applications. Recommended basket: ["Portugal D7 visa", "how to renounce US citizenship", "Mexico residency", "move to Canada", "Spain non-lucrative visa"]. Threshold: composite basket >60 (scale 0-100) for 4+ consecutive weeks = structural interest, not event noise |
| URL | https://trends.google.com/trends/ (no persistent link — must build basket manually) |
| Effort | LOW — free, no auth, exportable CSV. Build comparison basket once; re-pull monthly |
| Key caveats | Index is relative (0-100), not absolute search volume. Cannot be converted to headcount. Best used as directional leading indicator and cross-check against hard counts. Quarantined-subreddit data (Reddit) is now unreliable and should NOT be substituted |

---

### 5. Spain OPI — Non-Lucrative Visas by Nationality (Annual)

| Field | Detail |
|-------|--------|
| Accessibility | Free public — Spanish Observatorio Permanente de la Inmigración |
| Cadence | Annual (typically Q3-Q4 for prior year) |
| Lag | ~9-12 months |
| Reliability | MEDIUM-HIGH — official Ministry of Inclusion consular records |
| Signal strength | Spain's non-lucrative visa (NLV) is among the most popular EU relocation routes for Americans with passive income. Total 2023 long-stay visas issued: 169,781 (all nationalities). US-citizen share not broken out in headline stats but available in tables by nationality and visa class. Threshold: US-citizen NLV >2,000/yr = material Spain corridor |
| URL | https://www.inclusion.gob.es/en/web/opi/estadisticas/catalogo/visados |
| Effort | MEDIUM — portal provides Excel/CSV tables; requires filtering by "EEUU" (Estados Unidos) and visa class "residencia no lucrativa" |
| Key caveats | New RD 1155/2024 regulation (May 2025) extended NLV initial validity to 365 days and added physical presence requirements — may affect demand in 2025-2026 data. Data typically 9-12mo old by time of publication |

---

## Sources NOT Recommended (and Why)

### 6. Mexico INM — Temporary/Permanent Resident Cards to US Citizens

| Field | Assessment |
|-------|-----------|
| Accessibility | Not reliably public. INM portal (inm.gob.mx) does not publish nationality-disaggregated residency card stats in a downloadable format |
| Cadence | Annual if published (irregular) |
| Lag | 12-18 months |
| Reliability | LOW for MARCO purposes — data not consistently accessible |
| Signal strength | ~70,000 Americans estimated in Mexico currently; large population but data not trackable without Spanish-language FOIA equivalent or academic partnership |
| Verdict | EXCLUDE. Track via proxy: BBVA Anuario de Migración y Remesas (annual, covers Mexico INM flows) as a lower-effort substitute if Mexico corridor becomes priority |

---

### 7. SSA Retirees Abroad (Annual Statistical Supplement, Table 5.J)

| Field | Assessment |
|-------|-----------|
| Accessibility | Free public — ssa.gov/policy/docs/statcomps/supplement/ |
| Cadence | Annual |
| Lag | ~12-15 months. 2025 supplement covers Dec 2024 data |
| Reliability | HIGH data quality, but LOW emigration signal |
| Signal strength | Counts Social Security retirement/disability beneficiaries by country of residence. Measures the already-departed retiree base, not new outflows. YoY change in counts is very slow-moving (retirees don't move back). Useful for stock, not flow. Cannot isolate political emigration from normal retirement abroad |
| Verdict | EXCLUDE from EMG-01 active tracking. Use as annual stock sanity check only (note total in RESEARCH_STATUS.md). Not a leading indicator |

---

### 8. FinCEN FBAR Aggregate Filings

| Field | Assessment |
|-------|-----------|
| Accessibility | NOT reliably public. FinCEN does not routinely publish FBAR aggregate data. AARO has scraped partial counts from public statements (2001-2020 with gaps) |
| Cadence | Annual (if accessible) |
| Lag | 18-24 months |
| Reliability | LOW as emigration proxy — FBAR required for any US person with >$10K foreign account, including domestic investors, not just emigrants |
| Signal strength | 2020: 1.4M filings, but vast majority are US-resident investors with foreign accounts, not emigrants. Cannot disaggregate. Rising trend reflects FATCA enforcement, not emigration |
| Verdict | EXCLUDE. Too noisy, too stale, not publicly accessible in aggregate |

---

### 9. Spain Non-Lucrative Visa — Consular-Level Data

See Source 5 above (OPI is the correct level of aggregation for this data; consulate-level data is not separately published).

---

### 10. Costa Rica DGME — Rentista/Pensionado Grants to US Citizens

| Field | Assessment |
|-------|-----------|
| Accessibility | Nominally public — DGME publishes annual migration report — but US-citizen breakdowns not consistently available in English-accessible format |
| Cadence | Annual |
| Lag | 12-18 months |
| Reliability | MEDIUM data quality, LOW accessibility |
| Signal strength | ~70,000 Americans estimated in Costa Rica; Pensionado requires $1,000/mo pension, Rentista $2,500/mo income. Population is real but small relative to Canada/Portugal/Spain corridors |
| Verdict | EXCLUDE for now. Monitor only if Costa Rica corridor shows headline news acceleration. OECD International Migration Outlook covers Costa Rica annually and is more accessible |

---

### 11. Reddit r/AmerExit Subscriber/Post Volume

| Field | Assessment |
|-------|-----------|
| Accessibility | Quarantined — data collection unreliable per SubredditStats.com. Reddit killed third-party API access (Pushshift) in 2023 |
| Cadence | Was daily/weekly; now effectively inaccessible |
| Reliability | LOW — quarantine + API closure makes automated tracking infeasible |
| Signal strength | Community reached ~177K members; post volume tracked political cycles well. But collection infrastructure no longer functional |
| Verdict | EXCLUDE. Subreddit is quarantined and third-party tracking APIs are dead. Google Trends (Source 4) is a superior and accessible substitute for the intent-signal role |

---

### 12. Knight Frank Wealth Report — US-Citizen International Home Purchases

| Field | Assessment |
|-------|-----------|
| Accessibility | Free public (PDF, annual) — knightfrank.com/wealthreport |
| Cadence | Annual (published March) |
| Lag | ~15 months — March 2025 report covers 2024 data |
| Reliability | MEDIUM — survey-based, 150 family offices globally; not a census |
| Signal strength | Captures high-net-worth emigrant property purchases but misses middle-class renters and budget emigrants who constitute the bulk of political emigration. 2024: US was leading nationality for Portugal Golden Visa (406 permits). Not disaggregated enough to yield an emigration rate |
| Verdict | EXCLUDE from formal EMG-01 tracking. Use as annual context data for the high-net-worth cohort (already captured in Portugal AIMA data). Not a standalone stream |

---

## Monthly Update Protocol (for Active Sources)

| Source | Update Month | Action |
|--------|-------------|--------|
| Federal Register expatriate list | Feb / May / Aug / Nov | Count entries from most recent quarterly notice; log in STATUS.md |
| Canada IRCC CSV | Monthly | Download, filter US citizenship, extract monthly PR count |
| Google Trends basket | Monthly | Pull 12-month index for basket; note any >20pt spike |
| Portugal AIMA | October (annual) | Note US resident count YoY; extract Golden Visa + nomad visa US share |
| Spain OPI | Q3-Q4 (annual) | Filter NLV table for EEUU; compute YoY change |

---

## Key Thresholds for EMG-01 Escalation

| Metric | Watch | Escalate to PROME |
|--------|-------|-------------------|
| Federal Register quarterly count | >1,000 | >1,500 (two consecutive quarters) |
| Canada US-citizen PRs | >300/month | >500/month sustained |
| Portugal US residents YoY | >25% | >40% OR absolute >30,000 |
| Google Trends composite | >50 (4-week avg) | >70 sustained or spike >90 |
| Spain NLV to US citizens | >1,500/yr | >3,000/yr |

**Note:** Fee drop to $450 (April 2026) will structurally inflate renunciation counts in Q2 2026 onward. Do not treat the first post-fee-drop spike as signal without adjusting for pent-up demand release (estimate 1 quarter of excess).

---

*Research sources: Federal Register, IRCC Open Government Portal, AIMA annual reports, Spain OPI, Google Trends, boundless.com/research-reports, getwherenext.com/blog/amerexit-by-the-numbers, Wikipedia Quarterly Publication of Individuals Who Have Chosen to Expatriate, 1040abroad.com, AARO fbar-filing-data-by-year*
