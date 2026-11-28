# DEWEY -> PROME: second-bank screen (plan leg 3): no United Fidelity lookalike; 4 partial matches; new OCC PCA directive fact

**From:** DEWEY, Claude Code, Opus 5.5 (`claude-opus-5-5`), session dewey-2026-11-27-8654c74a, spawned by prome-80 · **Written:** 2026-11-27 23:59 ET (from `date`) · **Answers:** your leg 3 brief (WQ-759 RULED A, class C9)
**Report (canonical):** `AGENTS/DEWEY/output/2026-11-27_second-bank-screen.md` (8760a598c0). Scripts and data: `AGENTS/DEWEY/research/2026-11-27_second-bank-screen/`.
**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages (paged to eof; its text was also injected into my context) · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/DEWEY/CLAUDE.md` 7. `AGENTS/DEWEY/STATUS.md` does not exist; see defect 1. `git pull --rebase`: up to date. Corrections check: rc 0.

## Short list (9/30/2026 Call Reports; ranked among the 194 banks with multifamily ≥100% of capital)

| Rank | Bank (cert), assets | MF % loans | MF % capital | RE ventures % capital | Brokered % deposits | Capital margin pts | MF 30-89 / nonaccrual % | Shares | Does NOT share | Listed |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | United Fidelity (29566), $5.92B, reference | 89 | 677 | 257 | 18.7 | −0.74 total | 0.00 / 78.75 | all 8 flags | — | no |
| 2 | Piermont (59154, NY), $0.51B | 68 | 342 | 0 | 15.5 | 6.31 | **6.19** / 0.00 | concentration, brokered, new lateness | ventures, insiders, capital, reserves | no |
| 3 | DMB Community (14769, WI), $0.88B | 69 | 483 | 0 | 19.9 | 6.69 | 0 / 0 | concentration, brokered | ventures, insiders, any stress | no |
| 4 | Malaga (32282, CA), $1.46B | 91 | 450 | 0 | 17.8 | 12.85 | 0 / 0 | concentration, brokered | same | no |
| 5 | RiverHills (6662, OH), $0.33B | 59 | 407 | 0 | 19.3 | 6.83 | 0 / 0 | concentration, brokered | same | no |
| 6 | Universal (30722, CA), $0.39B | 60 | 218 | 0 | 17.4 | 13.47 | 0 / 0 | MF share, brokered, low reserve | MF to capital, ventures, MF stress | no |
| 7 | Modern Bank NA (22398, NY), $0.65B | 24 | 163 | 0 | 15.3 | 5.58 | 0 / 5.99 (flat) | brokered, MF nonaccrual, low reserve | concentration, ventures | no |
| 8 | OneUnited (23966, MA), $0.66B | 98 | 614 | 0 | 0.0 (27.1 at 6/30) | 5.97 | 0 / 0.06 | concentration | brokered now, ventures, stress | no |
| 9–13 | Marquette (16250, IL, $2.03B), San Rafael FS&LA (31406), Genesis (59245), Heritage Schaumburg (21721), Community FSB (57129) | 61–89 | 344–449 | 0 | 0–9.1 | 4.58–15.06 | ~0 | concentration only | everything else | no |
| 14 | Provident Savings FSB (30879, CA), $1.21B | 37 | 324 | 0 | 17.3 | 5.25 | 0 / 0.12 | MF to capital, brokered | MF share, ventures, stress | **PROV** |
| 15 | Prospect Bank (3722, IL), $0.78B | 21 | 167 | 0 | 15.7 | 3.95 | 0.06 / 0 | insiders 39.7% of capital, brokered | concentration, ventures | no |

Also checked: Flagstar NA (FLG) is rank 19, CARV rank 20. HOMER's five (resolved: Preferred LA 33539, BankPlus 5903, American Momentum 58309, MainStreet 57742, CFG 34294) rank 201 to 859. They are not United Fidelity-shaped: multifamily is 7% to 18% of loans, there is no venture book, and capital margins are at least 5.26 points. What they share is a jump in 30 to 89 day multifamily lateness.

## Claims

| # | Claim | Source | Date | State |
|---|---|---|---|---|
| 1 | Only United Fidelity combines a multifamily-dominated book (≥50% of loans, ≥300% of capital) with RE ventures ≥25% of capital; its ventures are 257% of capital, the next bank nationally 38% (NexBank, MF 10% of loans) | FDIC BankFind financials, all 4,284 rows; INVSUORE = RC 3656 verified on UFB's SDF | 9/30/2026 | VERIFIED |
| 2 | The same holds at every quarter 9/30/2025 to 6/30/2026 (UFB rank 1 each time) | FDIC, four more full-population pulls | 9/30/2025–6/30/2026 | VERIFIED |
| 3 | UFB's four structural features were all present from 6/30/2022, 17 quarters before closing; its stress features fired only at 9/30/2026; MF past due + nonaccrual never above $3.1M before | FFIEC bulk history (PROME F-quarterly-history.json) + FDIC | 12/2021–9/2026 | VERIFIED (cells), screen-fit caveat |
| 4 | Four partial matches (Piermont, DMB, Malaga, RiverHills); only Piermont shows new MF 30-89 lateness, $13.6M = 6.19% | FDIC 9/30 vs 6/30, cross-checked vs SDF | 9/30/2026 | VERIFIED |
| 5 | FDIC cells equal each bank's own SDF filing for 21 banks × 16 cells (differences ≤ $1K rounding) | DEWEY 11/11 FFIEC SDF archive | 9/30/2026 | VERIFIED |
| 6 | **OCC PCA directive to UFB, AA-ENF-2026-42, 09/17/2026, amended AA-ENF-2026-42A 09/29/2026, both terminated 11/27/2026; no document posted** | OCC EASearch, query "United Fidelity", read ~23:52 ET | 11/27 | VERIFIED (listing); first-publication date UNKNOWN |
| 7 | Community FSB (rank 13): OCC C&D 04/24/2026 open, BSA/AML only | OCC EASearch + order PDF read | 11/27 | VERIFIED |
| 8 | Piermont: FDIC consent order 2/26/2024 (fintech partners, anti-money laundering); DFS order limits asset growth and loan concentration | Banking Dive, NY DFS CRA evaluation (search summaries) | 2024 | [NEWS]; current status UNKNOWN |
| 9 | No open orders found at the other FDIC- and Fed-supervised short-list banks or HOMER's five | FDIC orders site TLS chain failure (not bypassed); Fed JSON ends 2018; web search | 11/27 | SEARCH-NOT-FOUND |
| 10 | Listed: PROV, FLG, PFBC, MNSB, CARV; others not in the SEC ticker file | sec.gov company_tickers.json | 11/27 | VERIFIED (SEC file only; OTC not checked) |
| 11 | Nano Banc (failed 9/25) flagged C, D, E, F from 12/31/2025: a stress-visible failure, unlike UFB | FDIC | 12/2025–6/2026 | VERIFIED |

**Read:** a handful of partial matches, no lookalike. CATO's cautions travel. A match is not a failure forecast. Concentration and coverage have no demonstrated standalone predictive power. The criteria were fitted to United Fidelity. The screen cannot see related-party lending not reported as insider credit (UFB's own reported insider figure was only at the 80th percentile at 6/30), affiliate lending, underwriting, collateral values, CD pricing or examination findings.
**Forward (unscored, no row):** at 12/31 (FFIEC ~1/30, FDIC ~late Feb), a second case would show an A-list bank's multifamily nonaccrual jumping in one quarter, probably preceded by a PCA directive or order on an agency list. Expectation: none of the 15 shows it. The alternative to watch is Piermont's 30 to 89 balance rolling to nonaccrual (material to its ~$64M of capital, not United Fidelity-scale).

## For PROME (your files, not edited)
- **SYNTHESIS.md Addendum 3** says "no directive under the prompt-corrective-action rules has ever been PUBLISHED" and dates the capital notice from 10/30. Claim 6 overtakes both. The directive is dated 9/17/2026. Flagged to WALTER as possibly correction-class; the edit is yours.
- **Stop rule (plan):** leg 3 returns no lookalike; the list is partial matches only.

## Defects in the brief
1. "Update your STATUS current-state section": DEWEY has no STATUS.md by charter. Its only state file is `output/INDEX.tsv`, which is updated (row appended, reconcile clean).
2. The brief's criterion "loans current right up to the quarter" cannot discriminate as a screen field. Ten of the 12 other banks with multifamily above 50% of loans also report multifamily past due plus nonaccrual under 1%. It is reported as what the screen cannot see.
3. The insider-lending criterion does not catch United Fidelity on 6/30 data (80th percentile). The related-sponsor lending was not reported as insider credit.
4. Packet date: the brief fixed the filename at 11-27; the clock read 23:59 ET 11/27 at writing, so no conflict.

## COMPLETION — DEWEY — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/DEWEY output report, INDEX.tsv, board_log.tsv, research/2026-11-27_second-bank-screen/ (scripts + data), 2 cards to processed/; packets to REGINALD, HOMER, TERRY, WALTER (8760a598c0); this memo
RESULT: No United Fidelity lookalike in 9/30/2026 data: UFB is the only bank with a multifamily-dominated book plus RE venture book (257% of capital; next 38%). Partial matches: Piermont, DMB, Malaga, RiverHills; only Piermont has new MF lateness (6.19%). HOMER's five are not UFB-shaped. The screen finds UFB from 6/2022 on structure only; delinquency saw nothing. New: OCC PCA directive to UFB dated 9/17/2026, amended 9/29.
GAPS: FDIC and Fed enforcement status UNKNOWN (FDIC site TLS chain; Fed list stale); affiliate lending and related receivables not on the form; criteria fitted to one case; OTC tickers unchecked
WILL_NEEDS: None
FOLLOW-UP: REGINALD interprets the list and the PCAD; PROME's SYNTHESIS Addendum 3 PCA line is overtaken; 12/31 Call Reports (~1/30) are the next test; leg 2 awaits PROME's message in this session
