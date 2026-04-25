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
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more" when public press releases were truncated and he was going to provide supplement PDFs. Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Changelog tracks THESIS.md only. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows. Scope guard: if writing a 4th sentence of sub-doc summary in THESIS.md, it belongs in the sub-doc.
- [2026-04-22] **Domain CHANGELOG needed per bank.** Each bank subdirectory (OZK/, WAL/) should have its own CHANGELOG.md that tracks its THESIS.md only — mirrors format of master `thesis/CHANGELOG.md`. OZK was missing one; authorized creation. Version convention: vX.Y where major = structural, minor = refinement. First entry describes change AND pins prior state as v1.0.

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Must run with `.venv/bin/python3` from workspace root (not from AGENTS/REGINALD/).
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; use regex `re.sub(r'<[^>]+>',' ',html)` not BeautifulSoup `.get_text()`.
- [2026-04-19] **Paywall map:** Forbes.com, Seekingalpha.com, Journalrecord.com (Reuters wire) return 403 to Anthropic WebFetch. Workable substitutes: MarketScreener, PrismNews, Sharecafe (Reuters), Motley Fool / Investing.com (SA transcripts).
- [2026-04-22] **LAM = Leucadia Asset Management = Jefferies subsidiary** (post-2013 Leucadia/Jefferies merger). Semantic mapping critical for V2 fraud chain — WAL's $126.4M LAM charge-off is on the Jefferies rail. Cross-reference in any WAL/Jefferies/Cantor research.
- [2026-04-22] **Quartr MCP is subscription-gated** — returned `subscription_required` error when searching companies. Cannot use for document/event fetching. WebFetch + direct IR page links or user-provided PDFs are the workaround.
- [2026-04-24] **SEC EDGAR direct-fetch pattern** — WebFetch 403s on all sec.gov paths, but `curl` with a `User-Agent: REGINALD research willie@research.local` header returns 200. Canonical paths: `https://data.sec.gov/submissions/CIK<padded>.json` for recent filings index (returns recent form/accession/filingDate/primaryDocument arrays) → `https://www.sec.gov/Archives/edgar/data/<cik>/<accession-no-dashes>/<filename>` for actual documents. Note: SEC accession numbers can start with the FILER's CIK, not the COMPANY's — stocktitan reported WAL Q1 8-K as `0001212545-26-026302` but the real accession was `0001628280-26-026302`. Always cross-check via data.sec.gov.
- [2026-04-24] **Q4CDN IR PDF hosting pattern** — Most public bank IR pages host earnings materials at `https://s21.q4cdn.com/<subscriber-id>/files/doc_financials/<year>/<qnum>/<FILENAME>.pdf`. WAL's subscriber-id is `328636679`. Filename conventions vary per bank (17 naming variants probed for WAL supplement — none hit; WAL is deck+release only). Direct fetch works without auth.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals.

## Session Notes

⚠️ **Open question:** The Round 2 Wave 1 cascade (`WAL/THESIS.md` v2 rewrite) is the natural next step — we have 3 synthesis docs (~1,500 lines of signal) ready to feed it. But DEF 14A is still untouched and gives governance/insider context that doesn't depend on thesis framing. Which to do first? My bias is Wave 1 cascade (WAL/THESIS.md v2) → then DEF 14A — because thesis v2 without governance is still a coherent deliverable, but governance findings may change nothing at the thesis level.

**Also pending resolution:** REG-20 (WAL major stress event, 82%) — Q1 print arguably resolves (GAAP EPS miss -4.6%, $152.5M fraud, tape -2%). Flagged OPEN in PREDICTIONS.tsv with resolution note. Will should call whether to mark CONFIRMED or hold for higher-bar event.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 24 PM-evening — WAL Q1 Round 2 deep-mine: Press Release + Deck synthesis)

**Core deliverables — two synthesis docs, 1,200+ lines combined:**
- `WAL/sources/q1_2026/WAL Q1 2026 - Press Release Synthesis.md` (521 lines) — extraction of 20pp / 5,768-line PDF
- `WAL/sources/q1_2026/WAL Q1 2026 - Deck Synthesis.md` (702 lines, corrected after operator eyes-on Slide 12) — extraction of 25 slides / 2,250-line PDF
- Pair-doc: transcript synthesis from prior session still live (248 lines)

**⚠️ Gitignore discovered:** `AGENTS/REGINALD/*/sources/q[1-4]_*/` ignores the whole sources directory. Source PDFs intentionally excluded (IP/size), but our synthesis markdown files are also excluded. **Synthesis files NOT in git commit for this session.** Needs Will decision: (a) negation rule for `*.md`, (b) move synthesis to non-ignored path like `WAL/synthesis/`, or (c) force-add with `git add -f`.

**Headline Round 2 findings (condensed — full in STATUS.md POST-DECK INTEGRATION section):**

1. 🔴 **Office stress is acute single-point concentration.** Slide 12 classified mix (operator-verified): Office 38% / C&I 32% / Construction 12% / Other 10% / Resi 5% / CRE Investor non-Office 3%. **Office = $407M on $2.2B book = 18.5% stress rate, 9.5x book-share disproportion.** Initial read had category mapping wrong ("70% CRE" framing). Corrected framing is sharper: single-point Office concentration, not broad CRE.
2. 🔴 **Office maturity wall $946M matures 2026** (Slide 23). Bridge-loan structure → natural recognition pressure on refi failure.
3. 🟢 **NDFI cohort position disclosed** (Slide 24, 30-bank table). WAL at 7% Ex-Mtg Credit (peer median 6%). **V3 NDFI-opacity thesis disconfirmed at aggregate level.** But $7.155B Mortgage Warehouse (12% of loans, 30x peer median) remains a confirmed concentration, classified as C&I not NDFI.
4. 🟡 **Hotel $4.5B (44% of CRE Investor) — sizing risk, NOT active stress.** WAL has formal Hotel Franchise Finance line. Slide 12 confirms non-Office CRE Investor only 3% of classified = ≤$32M. Latent watch vector.
5. 🟡 **Mgmt Revised 2026 Outlook** (Slide 17). NCO 25-35bps ex-fraud (held) but Q1 came in at 39bps → **above top of guide**. NII +11-14% even without rate cuts. Non-interest income raised +2-4% → +20-25% (Juris banking). Deposit costs RAISED $535-585M → $650-700M.
6. 🟢 **CLN reference pool SHRINKING** (press release p4): $8.5B → $7.9B YoY. V3 CLN-arbitrage sub-vector directionally disconfirmed.
7. 🔴 **Leading vs lagging indicator divergence**: 30-89d PD +$49M QoQ (+45%), Special Mention +$78M QoQ (+24%) while nonaccrual/classified improved. Vecchione narrative skips leading buckets.

**Thesis read: intact but refined.** New framing = "good compounder with concentrated CRE tail risk." Structural bull case stronger than prior assumed (10yr TBV CAGR 18.3% top quartile; NII held despite no rate cuts). Short thesis still needs (a) CRE tail to actualize, or (b) market re-rate on concentration. Thesis PT range may need to widen $47-60 → $55-70.

**New predictions added (REG-24, REG-25):**
- REG-24: WAL Office classified > $500M by Q3 2026 (60%) — driven by $946M Office maturity wall
- REG-25: WAL ex-fraud NCO > 40bps in Q2 OR Q3 2026 (55%) — driven by Q1 39bps vs 25-35bps guide tension

**Interpretation error caught + corrected.** Initial Slide 12 reading had "70% CRE" as top finding. Operator eyes-on check caught mapping swap (32% is C&I not CRE Investor, etc.). Synthesis patched in 5 places with explicit error disclosure. Lesson: PDF chart extractions are interpretation calls; operator verification for high-impact findings is cheap insurance. Also caught under-weighted items in press release synthesis (securities carry trade, MSR servicing revenue swing, gov-guaranteed mortgage magnitude, provision decomposition, Juris context) — flagged as "Known gaps" at top of doc.

**STATUS.md heavily updated** — 80-line POST-DECK INTEGRATION callout at top; RESEARCH — WAL section fully refreshed; Convergence Matrix WAL row updated; NDFI cohort spectrum refreshed with Slide 24 data; Predictions table adds REG-24/25.

**NOT yet done (Wave 1 / Wave 2 / DEF 14A):**
- DEF 14A (~90pp) untouched
- `WAL/Q1_2026_ANALYSIS.md` still at Round 1
- `WAL/THESIS.md` v2 rewrite pending
- `WAL/STATUS.md`, WAL/FRAUD, WAL/SCENARIOS, WAL/KB.tsv cascades pending
- Thesis changelog entry pending
- Outbox signals to BROCK, CARL, OTTO, PROME, LIQUID, HAWK/BRENT pending
- 10-Q (files ~May 10) + Q1 Call Report (May 1-10) will address remaining §11 open items (MI3, loan servicing revenue swing, Hormuz reserve, Other Leucadia credits)

**Commit this session:** `(pending)` — STATUS.md + PREDICTIONS.tsv + this MEMORY.md only. Synthesis files blocked by gitignore (see above).

### NEXT SESSION — Wave 1 thesis cascade (recommended) + DEF 14A

1. **Boot normally** — git pull (WALTER has been active; check for conflicts), read STATUS (POST-DECK INTEGRATION up top), LESSONS, CALENDAR, MEMORY; run market.py; check inbox.
2. **Resolve gitignore question** with Will on how to track synthesis files. If negation rule approved, commit the 2 pending synthesis files.
3. **REG-20 resolution call** — Will's decision: mark CONFIRMED (Q1 print satisfied "stress event") or hold for higher bar.
4. **Wave 1 cascade** (order matters — each depends on prior):
   - `WAL/THESIS.md` v2 — integrate Round 2 findings. New framing: "good compounder with CRE tail risk." Office concentration + maturity wall + Hotel latent + NDFI at cohort median + CLN shrinking + warehouse 30x peer. Bump version, update PT range ($55-70 candidate vs $47-60 prior).
   - `WAL/STATUS.md` — WAL-specific (separate from REGINALD/STATUS.md). Post-Round-2 refresh.
   - `WAL/FRAUD/STATUS.md` + `FRAUD/SYNTHESIS_V2.md` — LAM integrated with Jefferies rail, Cantor resolved with $13M senior liens.
   - `WAL/workbook/KB.tsv` + `KB_INDEX.md` — row count refresh. Add LAM rows, update Cantor rows, add CLN trajectory rows, add Office classified rows, add Hotel exposure rows.
   - `WAL/SCENARIOS.md` — probability re-weight given Round 2 data. Structural bull case stronger; CRE tail case refined.
   - `WAL/INDEX.md` — housekeeping.
   - `thesis/CHANGELOG.md` — document Round 2 integration as thesis event (not a V2 revision per se, but a Round 2 evidence integration + framing refinement).
5. **Wave 2 cross-agent outbox** (after Wave 1 done):
   - BROCK: LAM = Leucadia/Jefferies rail ($126.4M ring); fund-of-LAM implications for BDC sector
   - CARL: consumer disconfirming at WAL ($0 Construction + $0 Residential charge-offs 5 straight quarters)
   - OTTO: $152.5M fraud ledger update (WAL LAM+Cantor); Office classified $407M as new concentration watch
   - PROME: Round 2 completes; thesis PT widening candidate; position duration assessment
   - LIQUID: WAL funding NOT stressed (deposits +$5.6B QoQ dwarf borrowing +$676M ST)
   - HAWK/BRENT: no dedicated Middle East reserve at WAL (unlike RF's $17M overlay)
6. **DEF 14A pass (90pp)** — only AFTER Wave 1. Governance/insider layer: CFO Idnani comp package, ownership table, related-party transactions, audit committee composition, board committee assignments. Independent of thesis — findings are optional enhancement.
7. **Carry-over: OZK Spinout Step 14** — trim REGINALD/STATUS.md "RESEARCH — OZK" section to 5-10 line pointer. Low priority.
8. **Calendar-gated (May 1-10):** Auto-fetch WAL 10-Q + Call Report. MI3 ratio = V1 thesis test. Loan servicing revenue swing (-$23M YoY) also needs 10-Q to explain.

**Positions unchanged this session** — no broker data. Thread 3 roll still pending May 8 deadline (lives in `../OZK/POSITIONS.md`).
