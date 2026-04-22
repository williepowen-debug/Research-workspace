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

⚠️ **Open question:** Does $45P May 15 roll to $45P Aug, $40P Aug, $45P Sep, or $42.5P Sep? Thread 3 is the concrete options-chain analysis — need live quotes (delta/vega/IV skew) before recommending a single roll for Will approval. **Deadline: by May 8** (one week before May 15 expiry).

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 22 PM — Threads 1 + 2 executed, Thread 3 pending)

**Boot:** clean, Will requested OZK deep dive. OZK $48.52 → $47.20 (-2.72% intraday). WAL $77.83 → $79.68 (+2.38%) — **divergence trade flagged in Apr 20 brief played out in real time** post-Q1 prints.

**Main work: 2 of 3 teed-up OZK deep-dive threads completed.**

**Thread 1 → `OZK/SEVEN_CREDIT_DEEP_DIVE.md` (~290 lines):**
- Sponsor-identified 10 of 11 Q1 26 problem credits (HIGH confidence on 9, MED on 1, LOW on the $169M Boston Life Sci). Total $719M problem book.
- Key IDs: Sullivan Courthouse (Leggat McCall + Related Beal), Baltimore Peninsula (Goldman + Sagamore/Kevin Plank), Renaissance Milwaukee West Hotel (HKS Holdings — Bisnow confirmed), Chapter Buildings Seattle (Touchstone + Portman + Lionstone — see below), Schaffer's Mill Truckee (New Martis Partners), 8150 Sunset LA (Townscape + Angelo Gordon, failed buyer OKO/Vlad Doronin), 1229 Concord Chicago (Sterling Bay).
- **3 genuinely new findings:** (a) **Lionstone/Ameriprise wind-down as LP-side credit trigger** (new pattern, signal sent to BROCK); (b) **OZK's workout tempo = years, not quarters** (Schaffer's Mill 6+ years substandard on a revolver — reservoir thesis mechanism now concrete); (c) **Severity comp bands from 2025-26 printed transactions** (Boston vacant office -55 to -63%, Seattle -50 to -60%, Chicago lab -55-60%, LA DTLA office -45 to -68%).
- **Reserve adequacy verdict:** Blended EL on $719M = $211-291M → $628M ACL covers at 2.2-3.0x = ADEQUATE TODAY. But if problem book migrates to $1.4B (past-due doubling trajectory), coverage collapses to 1.1-1.5x → implies $150-300M reserve build over 4Q (2-3x Q1 26 pace).

**Thread 2 → `OZK/IQHQ_PLAYBOOK.md` (~290 lines):**
- **IQHQ has NO 2026 capital raise.** Last injection IIP Aug 2025. Tracy Murphy's Mar 2026 promise of 2 new RaDD tenants DID NOT materialize (still JCVI only, 3.3% leased).
- **Aimco filed $50M fraud complaint against IQHQ in Delaware Chancery, April 2026.** Targets Bluerock PIK + IIP preferred rescue structure as "conflicted financings and insider transactions." Gleason "inner family squabble" framing structurally true but materially misleading. Chills any 4th rescue round. Motion-to-dismiss response due early June.
- **IQHQ portfolio deteriorating across all non-RaDD properties:** Brighton dumped to New Balance at -30% (both lots, ~$10M loss), Arbor Redwood City ($164M Oracle campus) listed for sale instead of developed, Spur Phase I still 0% preleased, Fenway paused + $27M J.F. White suit active, 109 Brookline disclosure gap (Globe says 50% leased vs IQHQ "99% leased"). **Zero internal cash for RaDD equity cure.**
- **Campus at Horton = the comp.** AllianceBernstein took back $399M construction loan via $130M credit bid Sep 2025 = 67% severity. Same submarket, same problem. Scenario D is now a printed precedent, not tail risk.
- **Scenario tree (revised weights post-findings):** A-sponsor extends 20%, **B-substandard migration 50%**, C-third-party takeout 12%, **D-forced note sale/foreclosure 18%**. Weighted EL on $555M funded = **$140M = 22% of total ACL on one credit**. 68% probability of $140M+ event.

**Thesis assessment — sharpened more than strengthened:**
- Strengthened: RaDD catalyst quantified, past-due doubling firing, workout tempo mechanically sourced, severity comps printed, IQHQ sponsor distress deeper than disclosed.
- Weakened/corrected: OZK NCO rate 0.57% in-line (not "5.4x peers" 1.18%); OZK retreating from Fund Finance disconfirms NDFI narrative at OZK specifically; capital/liquidity/dividend strong; consumer channel not firing.
- **Net: hold position. Roll May to Aug/Sep (Thread 3). No add, no trim.**

**Files created/updated this session:**
- `OZK/SEVEN_CREDIT_DEEP_DIVE.md` — NEW (~290 lines)
- `OZK/IQHQ_PLAYBOOK.md` — NEW (~290 lines)
- `OZK/workbook/KB.tsv` — appended 2 rows (KB-OZK-176 workout tempo; KB-OZK-177 severity comp bands)
- `outbox/2026-04-22_to-BROCK_lionstone-ameriprise-lp-dissolution.md` — NEW (LP-dissolution pattern)
- `outbox/2026-04-22_to-CREED_ozk-boston-lifesci-plus-affinius-verify.md` — NEW (Boston life sci $325M concentration + Affinius verify ask)
- `CALENDAR.md` — added 6 IQHQ playbook checkpoints (Bluerock Q1 marks May-Jun, OZK May option expiry roll, Aimco motion Jun, OZK Q2 earnings late Jul, Campus at Horton leasing late Jul, RaDD Aug maturity detailed)
- `MEMORY.md` — this rewrite

**Skipped intentionally:** `thesis/CHANGELOG.md` — per rules, only triggered by THESIS.md/TIMELINE.md changes; Thread 1+2 findings are evidence accumulation, not thesis restructuring. KB rows are the correct persistence.

**Deferred to next OZK session:** `OZK/STATUS.md` focused refresh. Currently stale (last Apr 7, pre-Q1 print, pre-sponsor IDs, pre-Aimco). ~20-30 min of its own work. Worth doing at start of next OZK session as boot-integration task.

### NEXT SESSION — Thread 3: $45P May roll math

**Boot:** standard + read `OZK/IQHQ_PLAYBOOK.md` (scenario weights inform duration) + `OZK/SEVEN_CREDIT_DEEP_DIVE.md` (severity comps inform strike selection).

**Thread 3 execution:**

1. **Price refresh** — current OZK price, implied vol for May/Jun/Aug/Sep expiries, IV skew by strike
2. **Quote candidate rolls** — live bid/ask for:
   - Close $45P May 15 (2 contracts) → Open $45P Aug 21 (add 2 to existing 4)
   - Close $45P May 15 → Open $40P Aug 21 (deeper OTM, cheaper)
   - Close $45P May 15 → Open $45P Sep 19 (extra month of duration)
   - Close $45P May 15 → Open $42.5P Sep 19
3. **Compute** — net debit/credit, delta/vega per position, breakeven OZK price, P&L grid by scenario (A/B/C/D from IQHQ Playbook)
4. **Recommend** — single roll for Will approval. Decision framework:
   - Scenario B is base case (50% prob) — want puts ITM if OZK moves to $40-42 on reserve build recognition
   - Scenario D tail (18% prob) — want puts deep ITM if OZK moves to $30-35 on charge-off
   - Scenario A (20% prob) — stock rallies, puts expire worthless either way
   - Aug 21 duration captures all IQHQ Playbook checkpoints
5. **Write to FORGE outbox + update POSITIONS.md on execution**

**Deadline:** by **May 8** (one week before May 15 expiry).

**Carryover items (after Thread 3, if time):**
- `OZK/STATUS.md` focused refresh (Q1 26 actuals + sponsor IDs + IQHQ scenarios + Thread 1/2 references)
- `OZK/THESIS.md` — revise NCO framing (1.18% "5.4x peers" was Q4 anomaly; Q1 0.57% in-line → shift leading indicator from NCO rate to past-due trajectory)
- `STATUS.md` (root) pruning — 572+ lines, overdue. Archive Apr 7/9/10 briefs.
- WAL Round 2 (still awaits WAL supplement/transcript from Will)
- `workbook/PREDICTIONS.tsv` — REG-09 partial-resolve; add past-due trajectory leading-indicator prediction
