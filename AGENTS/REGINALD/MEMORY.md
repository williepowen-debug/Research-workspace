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

## References
- [2026-04-02] FRED API key signup: https://fred.stlouisfed.org/docs/api/api_key.html
- [2026-04-16] EDGAR CIK for MTB: 0000036270
- [2026-04-16] Cadwalader Fund Finance Friday — tracks fund banking personnel and deals.

## Session Notes

⚠️ **Open question:** Step 13 boot-test checkpoint pending — Will opens a fresh Claude Code session with cwd=`AGENTS/OZK/` and runs the 7-point validation per plan §10. All 7 must pass before Steps 14-16 proceed.

### CHANGES SINCE LAST SESSION
*(populated at next boot via market.py)*

### LAST SESSION (Apr 24 afternoon — OZK spinout Steps 5-12)

Executed Steps 5-12 of the 16-step spinout plan. Eight commits across OZK/ infrastructure + REGINALD ref updates + root CLAUDE.md agent registration:
- Step 5 `19f91531` — OZK/MEMORY.md (D2=A pattern; 6 moved Findings + 2 moved References + 12 duplicated rows)
- Step 6 `2e0d73a7` — OZK/CALENDAR.md; REGINALD/CALENDAR.md pruned (4 rows + 3 empty sections removed)
- Step 7 `5b93d612` — OZK/LESSONS.md (6 copied verbatim + OZK-framed NDFI rewrite)
- Step 8 `f46fc1b0` — OZK/POSITIONS.md (clean D1 split, 11 contracts from OZK/STATUS.md as source of truth; REGINALD/POSITIONS.md stale warning scoped to non-OZK)
- Step 9 `2f7b90de` — OZK/TRADE.md; REGINALD/TRADE.md pruned (4 prose blocks → pointer stubs; cross-bank tables kept)
- Step 10 `5a796036` — OZK/inbox/ + outbox/ (.gitkeep scaffolding)
- Step 11 `4c52daa0` — REGINALD CLAUDE.md/STATUS.md/2 outbox files: OZK/ → ../OZK/
- Step 12 `8c5773c0` — root CLAUDE.md: OZK* added to active agents list + spinout note

**Side fix mid-session:** Killed PID 67726 (this session's Telegram poller) — was polling with WALTER's shared bot token, competing with WALTER's session. WALTER confirmed recovery post-kill and wrote its own memory handoff (commit `887b8d73`).

**Currently pending push.** 8 spinout commits ahead of origin — Will asked to commit and push before running Step 13.

### NEXT SESSION — RESUME AT STEP 14 (after Will's Step 13 boot test passes)

1. Confirm Step 13 boot test outcome with Will (7-point validation per plan §10). If any failure, work plan §9 rollback options.
2. Step 14 — trim REGINALD/STATUS.md "RESEARCH — OZK" section (lines ~327-349) to a 5-10 line snapshot + pointer to ../OZK/STATUS.md. Add "refreshed from OZK/STATUS.md YYYY-MM-DD" note.
3. Step 15 — `git mv AGENTS/REGINALD/OZK_SPINOUT_PLAN.md AGENTS/OZK/archive/OZK_SPINOUT_PLAN.md`.
4. Step 16 is OZK agent's job (first real session handoff) — not REGINALD's.

**Positions unchanged this session** — no broker data received. Thread 3 roll still pending with May 8 deadline (lives in `../OZK/POSITIONS.md` now).
