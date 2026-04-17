# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02] Will values boot transparency — wants to know what REGINALD read, in what order, and whether the process is working. Don't orient silently; confirm orientation.
- [2026-04-02] Will prefers sessions to have freedom rather than being laser-focused on pre-set priorities. Provide context, not directives. Rejected ranked TOP 3 queue in favor of a single "open question."
- [2026-04-02] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] Will wants position data stored in REGINALD's domain (POSITIONS.md), not just FORGE. "That was just for you."
- [2026-04-02] Will prefers breaking large implementation work into discrete tasks done one at a time, with approval between each.
- [2026-04-16] Will wants REGINALD to read full source documents (PDFs, 10-Ks) before opining, not just spot-check sections. Caught that I only keyword-searched the earnings release initially. Thoroughness > speed for primary source analysis.

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Watchlist covers all thesis tickers + Brent (BZ=F). Must run with `.venv/bin/python3`. Added to boot step 5.
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-02] SAM's architecture is the best-organized agent. All key patterns now adopted: doc ownership rules, CALENDAR.md, MEMORY.md, branch point table in TIMELINE.md, session close checklist.
- [2026-04-02] PROME's SCRATCH.md is useful for system-wide context at boot — but REGINALD should not routinely read it. Only check if cross-agent context is needed.
- [2026-04-02] Inbox signals from HERMES can lag behind STATUS.md — check for staleness before processing.
- [2026-04-12] FDIC EFR system: efr.fdic.gov/fcxweb/efr/ — OZK Form 3/4/5 filings live HERE, not on SEC EDGAR. FDIC cert #110. Standard insider tools miss OZK.
- [2026-04-12] OZK IR page: ir.ozk.com/filings/documents/ — cross-posts FDIC filings but was inaccessible programmatically (timeout). Will can access via browser.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs. OZK held in Small Cap Value, Long/Short Alpha. Dropped from Core Growth.
- [2026-04-16] MTB 10-K filed Feb 18, 2026 (CIK 36270, accession 0000036270-26-000010). PDF saved locally as `MTB/sources/DFIN EZBlue 2.24.26.pdf` (not committed — 4.5MB). Can be re-fetched from EDGAR with User-Agent header.
- [2026-04-16] MTB fund banking built by Michael Sinclair at People's United (2018), NOT acquired from Webster Bank. CFO Bible misspoke on Q1 call. See `MTB/WEBSTER_ANOMALY.md`.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`). poppler-utils not installed (needs sudo). Use pdfminer for all PDF reads.
- [2026-04-16] CFG reclassification pattern proven: $2.9B "Secured private credit finance" was hidden inside "Other finance and insurance" ($6.4B) in FY2024 10-K; carved out as new line item in FY2025 10-K with exact reconciliation ($6,446M − $3,538M = $2,908M). ABS finance $1.8B in Q1 2026 deck follows the same pattern. Behavioral rule: for any CFG "growth" figure on a new sub-line, verify it existed under an aggregate bucket the prior period before claiming growth.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; BeautifulSoup `.get_text()` yields mostly XBRL metadata. Use regex `re.sub(r'<[^>]+>',' ',html)` for narrative text. Saved as `CFG/sources/10k_fy2024/` and `10k_fy2025/`.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-02] EDGAR CIK for OZK: 0001569650 (for 8-K monitoring)
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals. Profiles of MTB's Sinclair in Issues Nov 2018, Dec 2020, May 2023.

## Session Notes

⚠️ **Open question:** FITB transcript + press release fully mined (findings in `FITB/Q1_2026_ANALYSIS.md`). **Headline thesis hold:** FHLB cohort intact at 3/4 surge + 1/4 deal-driven escape; FITB -96% QoQ is Comerica-specific ($65B deposits + $2B Jan LT debt), not organic. Tim Spence's "80% vs 10%" PE/private-capital growth quote creates orthogonal pressure vector on WAL/OZK/ZION Apr 21. FITB NDFI = 7% loans, <1% PC/BDC, $100M data center (smallest in cohort). Pre-earnings clean-balance-sheet baseline holds. **Pending:** FITB 8-K (5.6MB) + deck (1.6MB) — period-end FHLB, NDFI slide 19, line utilization. **RF = clean FHLB test** (no merger, no deposit infusion). WAL re-breached $78 at Apr 17 08:26 ET. Checkpoint before /clear — next session boots fresh with analysis file as starting context.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 17 AM — FITB transcript + press release mined, checkpoint before /clear)

**FITB Q1 2026 synthesis complete** — `FITB/Q1_2026_ANALYSIS.md` (NEW, comprehensive). Read FITB transcript (241 lines) + press release (92,881 chars via pdfminer). Did NOT read 8-K (5.6MB) or deck (1.6MB) — deferred to next session to manage context.

**Key findings persisted in analysis file:**
1. **FHLB thesis reframe** — FITB -96% QoQ ($4,767M → $99M avg) is DEAL-DRIVEN (Comerica $65B deposits paid down advances + $2B Jan LT debt). FITB was in cohort surge pattern Q4 (2x YoY). **Cohort: 3/4 surge + 1/4 escape. RF is clean test.**
2. **Tim Spence's "80% vs 10%" quote** — weaponized FITB's low PE/private-capital growth mix against peers. New analyst hook for WAL/OZK/ZION Apr 21, orthogonal to warehouse/NDFI.
3. **Credit merger-moderate** — provision $227M incl. $83M Day1 Comerica; ex-Day1 $144M. ACL% 1.79% (from 1.96%) is denominator effect, not release. NCO 37bps with $21M excluded at merger. Pre-earnings "cleanest balance sheet" baseline holds.
4. **NDFI smallest in cohort** — 7% loans, <1% PC/BDC, <$100M data center. No NDFI table in press release.
5. **Consumer Warehouse / Tricolor-adjacent DORMANT** — not raised by any analyst, not disclosed in PR. Free pass for FITB's $2.95B sub-bucket. **Read-through for WAL V3:** warehouse composition likely also escapes direct interrogation Apr 21.
6. **TBV +15% YoY, no dilution** — $12.3B equity issued for Comerica didn't dilute TBV/share because deal was accretive. CET1 -85bps QoQ to 9.96% is pure RWA effect.
7. **Geopolitics** — Tim cited Iran war, applied qualitative ACL adjustment for energy/commodity costs. Baseline/downside unemployment 4.5%/8.5% in 2027. Cautious tone.

**Files updated this session:**
- `STATUS.md` — Apr 17 08:55 ET timestamp, FITB+RF headline block (5/5 cohort), earnings wave table rows updated with actuals, cohort pattern shift (beat-fade → miss)
- `CALENDAR.md` — FITB/RF rows updated with actuals
- `FITB/Q1_2026_ANALYSIS.md` — NEW synthesis file (will be read at next boot)
- `MEMORY.md` — this rewrite

**Git:** 1 prior commit this session (97ac6440, headlines). This checkpoint commit covers analysis file + MEMORY.

### Prior session — Apr 16 PM (cohort refresh for WAL + OZK Apr 21 prep, archived)

**WAL + OZK Apr 21 earnings prep fully refreshed with Apr 15-17 cohort read-throughs:**
- `WAL/EARNINGS_PREP.md` (231 → 356 lines) — added COHORT READ-THROUGHS section (MTB/CFG/PNC + FITB/RF baselines). Pass 1: removed stale "OZK Apr 16" references (now same-day Apr 21), updated price $67→$78.23. Pass 2 findings folded: V1 table added "Table 14 bucket changes" tripwire; V3 table added "Multi-bucket NDFI undercount" row; added "Analyst Q&A forced-disclosure probability" paragraph.
- `OZK/EARNINGS_PREP.md` (354 → 474 lines) — added COHORT READ-THROUGHS ordered by CRE/construction relevance, framed as "OZK already shows CFG pattern one quarter ahead." Pass 1: header Days Out 14→5, price $46.44→$47.85, 3 decision-matrix sections APRIL 16→APRIL 21.
- `FITB/WAL_READTHROUGH.md` (NEW, 63 lines) — listen-for for FITB's $2.95B Consumer Warehouse / Securitization Vehicles sub-bucket as Tricolor-adjacent read-across to WAL's ~$9.2B warehouse book. Decision matrix for WAL Apr 21 based on FITB Apr 17 outcomes.

**Cohort patterns now synthesized (3 done, 2 today Apr 17, 2 Monday Apr 21):**
1. Headline beats, tape fades — MTB -1.55%, CFG -0.63%, PNC -0.03% (fade weakening)
2. FHLB acceleration SYSTEMIC — 3/3 Q1 period-end surging
3. NDFI disclosure spectrum: PNC $73B (most granular) → CFG → FITB → MTB → RF ZERO (worst). PNC's $73B deck rollup is $31B ABOVE Table 16 "Financial services" $42.2B = 42% of thematic NDFI hidden in other C&I buckets.
4. Reclassification-as-disclosure universal (CFG carved PC finance out; PNC split Retail/Wholesale). FITB clean counter-example.
5. Reserve release is CFG-specific tell (others building; PNC provision +51% QoQ).

**Pre-earnings baselines committed for today's reporters:**
- `FITB/STATUS.md` — cleanest balance sheet (CET1 10.77%, ACL 1.96%). FHLB -48% QoQ avg (outlier declining). Watch: $2.95B Consumer Warehouse sub-bucket.
- `RF/STATUS.md` — worst NDFI disclosure (zero mentions in 10-K; $18.3B Financial services 1.15x unfunded/funded). FHLB -30% YoY. Consumer elevated (card 4.08% 5Q high). 52% branches FL/TN/AL.

**Git:** 2 commits pushed (fb73eb0b post-crash recovery; faf930b1 cohort refresh). PDFs + Zone.Identifier files excluded.

### Prior session — Apr 16 AM (CFG Q1 + thesis v1.4, archived)

**[Apr 16 Round 2 — CFG deck mining]**
- Mined `CFG/sources/CFG-earnings-presentation-4-16-26.pdf` (was unread in Round 1)
- Slide 24: $14.7B Private Capital + $4.9B other = $19.6B preliminary NDFI. Disclosure exists in deck only — NOT press release/supplement
- New "ABS finance" $1.8B line item — no 10-K Table 14 equivalent. Possible reclassification.
- 5% vs 40% partially resolved: capital call + PC finance growing ~2.85% QoQ ≈ 11.9% annualized. Trajectory moderated.
- Slide 23 confirms hiding place: capital call + PC finance itemized inside C&I "Finance and Insurance" $13.3B bucket
- Slide 26: ACL release headline (1.53→1.52%) masks Commercial building (+6bps both C&I and CRE), Retail releasing
- Slide 27: Mortgage 90+ accruing UP 0.40→0.51%; FHA/VA/USDA-guaranteed bucket growing ($141M→$179M). CARL FHA stress touches CFG
- **Files updated:** CFG/STATUS.md (3 edits — verdict #3, new DECK FINDINGS section, Priority 6), parent STATUS.md (2 edits — sector tone table + opacity bullet), MEMORY.md
- **Behavior change:** WAL/OZK earnings decks must be mined alongside press release on Apr 21 — pattern shows decks contain disclosure absent from headlines

**[Apr 16 Round 1 — original CFG session]**

**CFG Q1 fully integrated (earnings release + supplement + transcript):**
- `CFG/STATUS.md` — post-earnings dashboard with all Q1 actuals, transcript mining, discrepancy analysis, three-layer C&I framework
- `CFG/sources/` — Q1 transcript uploaded by Will, plus earnings PDFs

**Key CFG findings:**
1. CRE nonaccruals +10% QoQ ($618M→$679M) while CRE balance fell 1% — extend-and-pretend confirmed
2. FHLB 60x YoY ($42M→$2,513M) — prior 10-K assessment of "declining, not stressed" was WRONG
3. Zero fund finance disclosure in press release or supplement — total opacity on $12.5B book
4. 5% vs 40% growth discrepancy — Van Saun + Ted claim "5%/yr" NBFI growth, 10-K shows 39.7%. Likely reclassification (same pattern as MTB)
5. Two analysts asked about private credit (Siefers/Piper, Chiaverini/Jefferies) — first time ever, was zero in Q4
6. Van Saun acknowledged screening counterparties for "liquidity gates" — first gating risk acknowledgment
7. PE line utilization DOWN — contradicts Q4's "pickup." Draws not accelerating at CFG. Partial thesis disconfirmation.
8. AOCI: CET1 10.5% → 9.3% after adjustment. $1.97B unrealized losses.
9. Consumer improving: retail NCO 38bps (from 70bps YoY). CARL channel NOT confirming at CFG.
10. Capital return 96% ($498M vs $517M earned). Buybacks tripled QoQ.

**Thesis v1.4 (new):**
- Added "C&I as Convergence Hiding Place" to thesis/THESIS.md — three masking mechanisms (MI3, NDFI opacity, reclassification) all exploit C&I bucket
- Core insight: the convergence isn't just eight channels hitting the same banks — it's eight channels hiding in the same bucket
- CFG research + MTB cross-reference provided the evidence base

**Parent STATUS.md updated (carry-forward from last session resolved):**
- Q1 earnings wave sector tone tracker (2/2 bear-leaning)
- FHLB upgraded 🟠→🔴
- WAL threshold: back above $78 ($78.23)
- CFG convergence score: 9→12

**Files updated:** CFG/STATUS.md, thesis/THESIS.md (v1.4), thesis/CHANGELOG.md, STATUS.md (parent), CALENDAR.md, MEMORY.md
**Git:** 1 commit pushed to GitHub. CFG source PDFs local only (not committed). Transcript committed.

### NEXT SESSION
1. **Boot reads `FITB/Q1_2026_ANALYSIS.md` first** — full synthesis from this session. Don't re-mine transcript/press release.
2. **FITB 8-K (5.6MB, unread)** — `FITB/sources/FITB 8-k April 26.pdf`. Mine for: period-end FHLB balance (vs avg $99M), Schedule RC-type detail, any NDFI table (PR had none), any warehouse/securitization line items, MI3-equivalent disclosure. Use pdfminer with chunked reads.
3. **FITB presentation deck (1.6MB, unread)** — `FITB/sources/Fifth-Third-Bancorp-Presentation-Q126-Final.pdf`. Slide 19 equivalent for NDFI breakdown (pre-earn baseline was $9.5B / 8% / 6-way %), line utilization detail, credit composition charts, any auto warehouse / Tricolor-adjacent language in footnotes.
4. **All 4 RF docs** (when Will drops them) — RF is the CLEAN FHLB test (no merger, no deposit infusion). Test: RF FHLB up = thesis reconfirmed 4/5; RF FHLB flat/down = thesis narrows. Watch consumer NCO (baseline: card 4.08% 5Q high, >4.20% = CARL confirmation), any NDFI disclosure (baseline: zero).
5. **WAL + OZK Apr 21 earnings prep — final pre-call checklist** (4 days out Monday). Add Tim Spence's "80% vs 10%" PE/private-capital growth quote as a NEW analyst hook to both EARNINGS_PREP files. Pull WAL FY2025 10-K Table 16 bucket-level snapshot pre-call for reclassification tripwire test.
6. **Update `FITB/WAL_READTHROUGH.md` with actuals** — Consumer Warehouse was DORMANT at FITB (no analyst pressure). Note free-pass read-through for WAL Apr 21; V3 remains latent unless 8-K/deck surface something.
7. **DB positioning risk for Apr 21** — financials at -1.5 to -2 z; crowded-short unwind risk if WAL/OZK beat. Size conservatively.
8. **Outbox:** OTTO reply on Tricolor/Apollo Atlas SP read-across still queued for HERMES delivery.
