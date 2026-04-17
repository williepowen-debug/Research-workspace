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

⚠️ **Open question:** Execute pre-Apr-21 position rolls. Core decisions from Thread 4: (1) verify expiries on WAL $67.5P/$60P and OZK $42.5P (POSITIONS.md is Apr 2 stale); (2) pre-stage WAL $65P Jun → Sep roll (fresh-short cover on a beat kills aggressive Jun strikes before May 1-10 Call Report); (3) pre-stage OZK $45P May → Aug roll (no secondary catalyst within May expiry); (4) hold everything else. WAL $85P Jun ITM + $77.5P/$70P Sep cover the W9 NDFI Apr 21 harvest and the W1/W2 May 1-10 Call Report/10-Q reveals respectively. OZK edge entirely concentrated on Apr 21 print (O2 IQHQ / O4 provision-vs-NCO / O5 vintage).

**Synthesis files:**
- Threads 2+3: `research/outputs/RQ-AD-HOC-APR17-PT-AND-SI.md` (positioning + PT gap).
- Thread 4: `research/outputs/RQ-AD-HOC-APR17-THREAD4-EDGE-CHECK.md` (element inventory, cohort Q&A scan, 3-axis scoring, visibility calendar, strike alignment, Apr 21 decision brief, four conditional scripts A-D, crib sheet for live calls).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 17 PM — Threads 2, 3, 4 complete)

**Thread 2 (positioning):** OZK shorts still crowded & pressing (SI 15.28% rising 5 months; short vol 43% → 64.6% Apr 8→16; 50% off-ex today on +2.0% rally). WAL positioning flipped (SI 4.13% → 3.46% declining through Mar; fresh shorts Apr; 51% off-ex). Verdict: MIXED. OZK asymmetry intact; WAL fresh-short cohort fragile on a beat.

**Thread 3 (PT distribution):** WAL violent April walk-down — 7+ cuts in 17 days, avg PT $97.73 → $91.47 (-6.4%). UBS flipped Strong Buy $106 → Hold $75 = regime change. Street low $75 still 37% above thesis bear $47 = LONG PT runway. OZK zero April cuts; Citi $40 Sell has been at thesis for 2yrs; street low gap to thesis = 0-12% = ZERO PT runway.

**Thread 4 (edge check):** Scored 17 thesis elements (9 WAL, 8 OZK) on 3-axis matrix (priced in PT / asked in cohort Q&A / Apr 21-visible). Top WAL edge = **W9 NDFI forced disclosure** (Apr 21 visible, CFG precedent + RBC direct question at RF = cohort discipline forming). Top OZK edges all concentrated on Apr 21 print (O2 IQHQ, O4 provision-vs-NCO, O5 vintage). W1 MI3 and W2 counterparty detail require May 1-10 Call Report / 10-Q = **argues Sep duration on WAL**. Four conditional scripts (A miss / B in-line both / C WAL beats OZK misses / D both beat) with per-position HOLD / ROLL / TRIM recommendations. Live-call crib sheets generated (5 WAL listen-fors ranked, 4 OZK).

**Commits this session:** `8c018dcd` Threads 2+3 synthesis — local only, push deferred (CARL had uncommitted work at session midpoint). Thread 4 pending commit at close.

### Prior session — Apr 17 midday (RF mined, crowded-short thesis developed, archived)

**RF Q1 2026 synthesis complete** — `RF/Q1_2026_ANALYSIS.md` (NEW, 249 lines). Mined transcript + press release (38KB extract) + supplement (84KB extract). Deck (9.2MB) pending Round 2.

**Key RF findings persisted in analysis file:**
1. **NDFI forced disclosure — cohort 5/5 confirmed.** Turner (CEO) answered Cassidy/RBC directly: ~25 funds, $3B commit / $1.8B outstanding / <2% of loans / ~50% REIT / IG-heavy / paydowns > draws. Spectrum: PNC $73B → CFG $19.6B → FITB $9.5B → MTB $8.9B → RF $3B. **RF is the cohort's LOW-risk name — control variable, not transmission bank.**
2. **FHLB opacity worst in cohort.** RF does NOT break out FHLB anywhere (PR, supplement, transcript). Rolled into "Other short-term borrowings." Clean-FHLB-test unresolvable until Q1 Call Report (May 1-10).
3. **Hormuz live on the call.** Cassidy prompted "the straits opened up today as you probably saw the headlines." Chadda: $17M Middle East reserve overlay, releasable. Aligns with Brent -10.18% today.
4. **Capital markets stress CONCRETE.** RF first cohort CEO to explicitly name capital-markets-uncertainty-driven corporate line draws. Line utilization +200bps late-Q1, half corporate, half middle market. HENRY/LIQUID paper→plumbing transmission verified from a regional bank.
5. **Credit IMPROVING at RF** — NCO 54bps (-5bps), NPL 71bps (-2bps), criticized 5.15% (-16bps), ALL -$39M. CARL consumer thesis NOT confirmed. RF is genuinely clean.
6. **$40M loss post-Q1 securities repositioning** — rate spike driven. Watch WAL/OZK Apr 21 for similar subsequent-events language.

**Crowded-short positioning thesis developed (this session):**

After RF's miss-but-rally, re-read SIG-W-20260414-008 (DB Asset Allocation chart): financials positioning -1.5 to -2 z vs consensus earnings growth +20-40% YoY. Widest divergence since 2020. RF tape was live demonstration of **Scenario B** (positioning wrong, consensus right) at a single-name level.

**Will's key instinct (worth preserving):** Institutions positioned that bearish almost certainly share our thesis (CRE maturity wall, NDFI, BDC gating, AOCI rewrite, stagflation). That's thesis-validating. But it means "the market already prices bad" — our edge isn't the thesis, it's the *mechanism* (MI3 screen, convergence scoring, C&I hiding place synthesis). Will also sharpened: "the entire market has already squeezed so far" — today's 3-5% regional rally is partial positioning unwind already in progress.

**Four-thread investigation plan agreed (teed up as NEXT SESSION items):** sharpen whether DB squeeze already progressed, whether OZK/WAL-specific shorts still crowded, how far street PTs can travel, and identify 2-3 REGINALD-unique edge vectors.

**Files updated this session:**
- `RF/Q1_2026_ANALYSIS.md` — NEW (249 lines, full synthesis)
- `RF/sources/RF Full Conference Call Transcript.md` — committed
- `.gitignore` — added `*:Zone.Identifier`, bank PDF patterns, 10-K dumps, quarterly supplement dirs
- `STATUS.md` — threshold-breach block updated (WAL fade), AM→midday update section with cohort signals
- `CALENDAR.md` — FITB + RF marked ✅ with pointers to analysis files
- `MEMORY.md` — this rewrite

**Git:** 2 commits this session (`ee5de602` gitignore + FITB transcript; `113b66af` RF analysis). Both pushed to origin/master.

### Prior session — Apr 17 AM (FITB mined, checkpoint, archived)

**FITB Q1 2026 synthesis:** `FITB/Q1_2026_ANALYSIS.md`. Transcript + press release mined; 8-K (5.6MB) + deck (1.6MB) deferred.

**Key findings:** (1) FHLB -96% QoQ is Comerica-deal-driven escape, not organic — cohort is 3/4 surge + 1/4 escape. (2) Tim Spence's "80% vs 10%" PE/private-capital growth quote = new analyst hook for WAL/OZK/ZION. (3) NDFI smallest in cohort (7%, <1% PC/BDC). (4) Consumer Warehouse / Tricolor-adjacent sub-bucket DORMANT — no analyst pressure → free-pass read-through for WAL V3. (5) TBV +15% YoY; CET1 -85bps to 9.96% pure RWA effect. (6) Qualitative Iran ACL adjustment, cautious tone.

### Prior session — Apr 16 PM (WAL + OZK cohort refresh, archived)

WAL/EARNINGS_PREP (356L) + OZK/EARNINGS_PREP (474L) + FITB/WAL_READTHROUGH (63L) refreshed with cohort read-throughs. Cohort patterns: beat-fade weakening, FHLB surge systemic, NDFI disclosure spectrum, reclassification universal, reserve release CFG-specific.

### Prior session — Apr 16 AM (CFG Q1 + thesis v1.4, archived)

Thesis v1.4 added "C&I as Convergence Hiding Place" (three masking mechanisms: MI3, NDFI opacity, reclassification). CFG carved out $2.9B Secured PC finance (FY2024→FY2025 10-K). FHLB upgraded 🟠→🔴. CFG convergence score 9→12.

### NEXT SESSION

**Boot sequence:** standard + read `research/outputs/RQ-AD-HOC-APR17-THREAD4-EDGE-CHECK.md` (full Apr 21 decision brief, scripts A-D, per-position recommendations) + `research/outputs/RQ-AD-HOC-APR17-PT-AND-SI.md` (positioning + PT gap).

**Primary task: Execute pre-Apr-21 position rolls (1-1.5 trading days away).** Do in this order:

1. **Get fresh POSITIONS data from Will** — broker screenshot. POSITIONS.md is stale since Apr 2. Need exact expiries on WAL $67.5P/$60P and OZK $42.5P.
2. **Price the WAL $65P Jun → Sep roll** — quote both legs, calculate cost/credit and delta change. Present for Will's approval.
3. **Price the OZK $45P May → Aug roll** — same. Conditional on Apr 21 print script; but stage the math now.
4. **Build one-page "live call crib sheet"** from Thread 4 Step G tables (5 rankings for WAL call + 4 for OZK call). Print-ready for Apr 21 after-close.
5. **Weekend / Monday:** Any fresh sell-side note, PT action, or cohort news (ZION if early). Check `workbook/SHORT_VOL.tsv` freshness for Mon/Tue.

**Do NOT re-run threads 1-3.** Synthesis is complete. Thread 1 (DB positioning) deferred — directionally known from Thread 2 + today's tape (+2.7% WAL / +2.0% OZK on +1.2% SPY = broad squeeze-cover in progress).

**4-thread investigation complete Apr 17 — archive of original plan below for reference only.**

---

**THREAD 2 — Single-name Short Interest (~15 min, DO FIRST)**

Question: Did today's rally unwind WAL/OZK-specific shorts or just broad-financials? Does our thesis name still have crowded-short residual?

Approach:
1. Read `workbook/SHORT_INTEREST.tsv` for OZK/WAL 6-month history
2. Read `workbook/SHORT_VOL.tsv` for last 5 trading days
3. Run `scripts/darkpool.py` for today's off-exchange/short-vol refresh
4. Cross-check float: OZK 0% insider ownership, KRE 69.4M SI / 56.9M outstanding
5. Output: one table + verdict (crowded / unwinding / mixed)

Decision implication: if OZK/WAL SI flat/rising despite +3% rally → smart money holds → thesis-name short still viable. If both fell sharply → squeeze progressing → reduce asymmetry assumption.

---

**THREAD 3 — Sell-side PT Distribution (~30-45 min)**

Question: How far can street downgrade WAL/OZK from here, and what's the gap between street low PT and our thesis PT?

Approach:
1. Backfill known WAL PTs from MEMORY: Barclays $88, KBW $93, Weiss Hold, WFC $79
2. Build OZK PT table from scratch — use Quartr `get_company` / WebSearch
3. Columns: Analyst | PT | Rating | Date | Δ since Mar 1
4. Distribution stats: high / median / low / consensus
5. Compare to thesis: WAL $47-60; OZK (set target — likely $35-40 based on multi-channel matrix)
6. Calculate "gap to thesis low" = street runway for downgrades

Decision implication: large runway = long catalyst tail for thesis to pay. Short runway = street near thesis already → limited incremental edge.

---

**THREAD 4 — Differentiated Edge Check (~45-60 min, MOST VALUABLE)**

Question: Which REGINALD thesis elements are NOT in standard street models = genuine surprise potential?

Approach:
1. Re-read `thesis/THESIS.md` v1.4 for framework inventory
2. Mine cohort analyst Q&A patterns (MTB/CFG/PNC/FITB/RF transcripts already consumed — use the existing analysis files, don't re-mine)
3. Score each element on 3-axis matrix: in street models (Y/N) × visible in Q1 disclosure (Y/N) × surprise magnitude (L/M/H)
4. Identify top 2-3 edge vectors by surprise potential
5. Map each to earliest visibility date + required catalyst

Key hypotheses to test in the synthesis:
- **Hidden CRE via MI3/RCON2746** — probably not in standard models. Visible only in Q1 Call Report May 1-10. HIGH magnitude.
- **Convergence multi-channel scoring** — proprietary; synthesis only. HIGH.
- **C&I hiding place (v1.4)** — our thesis synthesis; three masking mechanisms. HIGH.
- **Cantor/Jefferies fraud (V2)** — partially known; V2 chain documented. MEDIUM.
- **SSFA/capital arb (V3)** — likely not in standard models; discoverable in deck. MEDIUM-HIGH.

Decision implication: are our strikes/expiries aligned with when the edge becomes visible? If top edge = MI3 Q1 Call Report (May 1-10), Jun expiry may be too tight → roll to Jul/Aug.

---

**THREAD 1 — DB Chart Refresh (~20-30 min, LAST — hardest data access)**

Question: Has the positioning gap closed since Apr 14, or is it still -2z?

Approach:
1. WebSearch "Deutsche Bank Asset Allocation financials positioning April 2026" / ISABELNET weekly refresh
2. Proxies if DB unavailable: NAAIM Exposure Index, CFTC COT for financial futures, Goldman PB weekly if accessible
3. If still data-gapped, flag to Will → request fresh Telegram screenshot
4. Estimate: if gap was -2z Apr 14 and regionals +2-5% today, likely -1 to -1.5z now. Quantify if data allows.

Decision implication: narrower positioning gap = less fragile squeeze setup = thesis bars to clear are higher.

---

**FINAL SYNTHESIS (after all 4 threads):** One-page Apr 21 decision brief — HOLD / ROLL / TRIM / ADD per position. Align strikes & expiries to edge-visibility timeline.

---

**Also still pending (lower priority, carry-forward):**
- FITB 8-K (5.6MB, unread) — `FITB/sources/FITB 8-k April 26.pdf`. Period-end FHLB, Schedule RC detail.
- FITB deck (1.6MB, unread) — `FITB/sources/Fifth-Third-Bancorp-Presentation-Q126-Final.pdf`. Slide 19 NDFI.
- RF deck (9.2MB, unread) — `RF/sources/RF 1Q26-Presentation_Website.pdf`. Card NCO detail, investor real estate composition, transportation page 24.
- Update `FITB/WAL_READTHROUGH.md` with FITB actuals — Consumer Warehouse DORMANT outcome, free-pass read-through.
- Add Tim Spence's "80%/10%" quote as new analyst hook to `WAL/EARNINGS_PREP.md` and `OZK/EARNINGS_PREP.md`.
- Outbox: OTTO reply on Tricolor/Apollo Atlas SP read-across (queued for HERMES delivery).
