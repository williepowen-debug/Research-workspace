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

## Findings
- [2026-04-02] `scripts/market.py` pulls live prices via yfinance. Must run with `.venv/bin/python3` from workspace root (not from AGENTS/REGINALD/).
- [2026-04-02] FRED API key not configured — HY OAS, claims, and other FRED series at boot require `FRED_API_KEY` env var. Low priority but would close data gap.
- [2026-04-02] OZK price sources can conflict ($46 vs $49 in same session) — always verify at broker when discrepancy >5%.
- [2026-04-12] FDIC EFR system: efr.fdic.gov/fcxweb/efr/ — OZK Form 3/4/5 filings live HERE, not on SEC EDGAR. FDIC cert #110. Standard insider tools miss OZK.
- [2026-04-12] Wasatch fund commentaries: wasatchglobal.com/wp-content/uploads/strategy-and-fund-documents/ — quarterly fund PDFs.
- [2026-04-16] pdfminer works for PDF text extraction (`.venv/bin/python3`, `from pdfminer.high_level import extract_text`). poppler-utils not installed.
- [2026-04-16] CFG 10-K HTML from EDGAR has inline-XBRL markup; use regex `re.sub(r'<[^>]+>',' ',html)` not BeautifulSoup `.get_text()`.
- [2026-04-19] **Paywall map:** Forbes.com, Seekingalpha.com, Journalrecord.com (Reuters wire) return 403 to Anthropic WebFetch. Workable substitutes: MarketScreener, PrismNews, Sharecafe (Reuters), Motley Fool / Investing.com (SA transcripts).
- [2026-04-22] **OZK public press release is truncated on globenewswire + stocktitan mirrors.** Real data lives in 3 separate docs on IR page: (1) Financial Supplement PDF (228K, balance sheet + income statement + ACL + classified/criticized detail), (2) Management Comments PDF (1.3MB, 38 pages — RESG portfolio deep dive, Figure 24 substandard credit roster, foreclosed asset detail, sub notes repricing schedule, variable-rate floor ladder), (3) earnings call transcript. The press release body is essentially just EPS + CEO quote.
- [2026-04-22] **LAM = Leucadia Asset Management = Jefferies subsidiary** (post-2013 Leucadia/Jefferies merger). Semantic mapping critical for V2 fraud chain — WAL's $126.4M LAM charge-off is on the Jefferies rail. Cross-reference in any WAL/Jefferies/Cantor research.
- [2026-04-22] **Quartr MCP is subscription-gated** — returned `subscription_required` error when searching companies. Cannot use for document/event fetching. WebFetch + direct IR page links or user-provided PDFs are the workaround.

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-02] EDGAR CIK for OZK: 0001569650
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals.
- [2026-04-22] OZK IR docs: `ir.ozk.com/filings/documents/` — cross-posts FDIC + SEC filings. Quarterly: Financial Supplement + Management Comments (separate PDFs) + transcript. Will can pull via browser when WebFetch 403/timeouts block.

## Session Notes

⚠️ **Open question:** Which OZK deep-dive thread to prioritize next session? Three candidates teed up from Q1 analysis (see NEXT SESSION). All three can work from `OZK/Q1_2026_ANALYSIS.md` as starting point; each hits ~1-2 hours of focused work.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 22 AM — WAL + OZK Q1 integration)

**Boot:** clean (pulled MARCO TOURISM work from origin; no inbox signals beyond processed). Prices flagged WAL below $78 post-print.

**Main work — WAL + OZK Q1 2026 earnings analysis:**
- **WAL:** Pulled 8-K via stocktitan mirror (press-release text). Round 1 analysis 12 sections → `WAL/Q1_2026_ANALYSIS.md` (265 lines).
- **OZK:** Press release truncated on public mirrors. Will delivered supplement + management comments + transcript in `OZK/OZK 2026 Q1 data/`. Extracted all three via pdfminer + Read. Round 2 full analysis 13 sections → `OZK/Q1_2026_ANALYSIS.md` (330 lines).
- **Headline findings:**
  - **WAL V2 FRAUD CONFIRMED IN PUBLIC 8-K.** Vecchione explicitly labeled "two fraud-related credits": LAM $126.4M (Jefferies subsidiary) + Cantor $26.1M (from specific reserve, ~89% utilized; $13M senior liens acquired). $50.5M security sales gains = "mitigation strategy" (cohort 2/2 with RF). Ex-fraud NCO 0.39%.
  - **OZK slow-grind thesis CONFIRMED.** Past due DOUBLED QoQ $207M → $465M (0.64% → 1.41%). Classified+criticized +23% QoQ. 3 new substandard credits (2 Seattle U District with signed LOI, 1 Boston Life Sci $169M). 2 new foreclosed (Chicago Life Sci $50M, Santa Monica Office $45M at 15% leased). Near-zero LTVs: Boston Office 95%, Seattle Pioneer 100%, Wauwatosa Hotel 103%.
  - **3 NEW OZK catalysts discovered:** Oct 1 2026 $350M sub notes reprice (2.75% → SOFR+209bps, Tier 2 -20% for 12mo, +$12.8M/yr interest); Aug 2026 IQHQ maturity (STATUS had wrong — was mislabeled Aug 2028); $350M new "Other borrowings" (offensive carry trade for $1.44B securities purchase, not defensive).
  - **OZK RETREATING from Fund Finance** (Jake Munn, CIB President) — disconfirms "regionals pressing into NDFI" narrative at OZK specifically.
- **Cohort tape pattern now 8/8** — all faded post-print (only RF rallied on miss-unwind).

**Files updated:**
- `STATUS.md` — Apr 22 AM brief, threshold breach, OZK+WAL research rewritten, matrix + catalysts updated (now 572 lines — over 250 cap, pruning overdue)
- `CALENDAR.md` — Apr 21 WAL+OZK ✅; IQHQ Aug 2026 corrected; Oct 1 sub notes catalyst added
- `WAL/Q1_2026_ANALYSIS.md` — NEW (265 lines)
- `OZK/Q1_2026_ANALYSIS.md` — NEW (330 lines)
- `OZK/OZK 2026 Q1 data/OZK earnings call transcript.md` — NEW, committed (PDFs stay untracked)

**Git:** 1 commit this session (`53db023e`, 5 files, +981/-33). Not pushed — deferred to session end.

### NEXT SESSION — OZK DEEP DIVE (Will's focus request)

**Boot sequence:** standard + read `OZK/Q1_2026_ANALYSIS.md` (330 lines, Round 2 complete) as entry point. Secondary: `OZK/OZK 2026 Q1 data/OZK earnings call transcript.md` for verbatim management commentary.

**Pick priority thread at boot (Will chooses):**

1. **Seven-credit deep dive** — sponsor + asset-level research on $719M problem exposure.
   - 4 substandard non-accrual ($240M): Boston Office $156M, Baltimore Land $40M, Seattle Pioneer Square $25.9M, Wauwatosa Hotel $17.9M
   - 4 substandard accrual ($329M): Boston Life Sci $169M, Seattle U District Office $76M + Life Sci $50M, Lake Tahoe SF Lots $34M
   - 3 foreclosed ($150M): LA Land $54.5M, Chicago Life Sci $50M, Santa Monica Office $45M
   - Target: sponsor identity, project comps, market data, recovery probability
   - Cross-check with OTTO_INTEL + MARCO commercial-RE sponsor research

2. **IQHQ August 2026 playbook** — scenario mapping for the Aug maturity.
   - RaDD 3.3% leased; Boston Life Sci demand shifted toward office/tech/AI users (per Brannon Hamblen)
   - Sponsor's financial capacity to extend
   - Three-scenario model: (a) sponsor extends with new equity, (b) sponsor walks / migrates to substandard, (c) third-party takeout
   - Cross-read with CREED life science stress data

3. **Position roll math — $45P May decision** — concrete options-chain analysis.
   - $45P May 15 expiry vs thesis timeline (past-due doubling = leading, recognition = Q2-Q3)
   - Candidates: $45P Aug, $40P Aug, $45P Sep, $42.5P Sep
   - Quote both legs, compute cost/credit/delta/vega
   - Check IV skew for May expiry distortion
   - Recommend single roll for Will approval

**Lower-priority carryover items (do after thread chosen if time allows):**

- `OZK/THESIS.md` — revise NCO framing (1.18% "5.4x peers" baseline → Q1 actuals 0.57%; promote past-due acceleration as new primary leading indicator)
- `OZK/STATUS.md` — update with Q1 26 actuals (RESG 52.1%, past due 1.41%, classified+criticized $1.215B, TBV $47.15)
- `thesis/CHANGELOG.md` — entry for V2 fraud confirmation (WAL Apr 21 print materializes long-thesis vector)
- `workbook/PREDICTIONS.tsv` — REG-09 (Tier 2 miss) partial-resolve; add new leading-indicator prediction around past-due trajectory
- Outbox signals: BROCK (LAM/V2), OTTO (fraud ledger +$152.5M), LIQUID (OZK offensive FHLB signature differs from MTB/CFG/PNC), CARL (consumer disconfirming at both WAL $0 resi/consumer NCO and OZK indirect 0.42% NCO)
- WAL Round 2 (awaits WAL supplement/transcript from Will — still pending)
- `STATUS.md` pruning (572 lines; archive Apr 7/9/10/Apr 14 briefs to `archive/STATUS_apr7_apr14.md`)

**Residual contradictions to flag in any deep dive:**
- STATUS baseline had OZK NCO 1.18% "5.4x peers" — Q1 26 reality is 0.57% in-line with cohort. Either prior baseline used wrong annualization / denominator or the cycle improved. **THESIS needs framing update.**
- CALENDAR had Affinius Oct 2026 $2.7B bond maturity tagged to OZK — **NOT mentioned on Apr 22 call.** CREED follow-up needed to confirm OZK is actually exposed to this credit.
- IQHQ maturity was wrong in STATUS (Aug 2028 → Aug 2026) — corrected this session, but other dates in OZK docs should be audited for similar drift.
