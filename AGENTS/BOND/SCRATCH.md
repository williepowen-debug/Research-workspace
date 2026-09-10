# BOND SCRATCH — 2026-09-09 (Wed) ~21:2x–22:xx ET. Will-spawned catch-up boot after five dark days (bond-30). Rewritten clean at closeout.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout. **Durable learnings → `MEMORY.md`; permanent evidence → `workbook/`. This file is disposable and must be executable COLD.**

> ## ⚠️ STATE AT HANDOFF
> **All BOND work committed. Inbox 7 + WALTER 4 → 0. No blocked action, no partial edit.**
> **Position UNCHANGED: TLT puts HOLD, no add. Composite 12/35 (11th consecutive). $0.**
> 🟢 **REFUNDING LEGS 1–2 CLEAN ON BOTH DEFINITIONS — the FIRST KILL EVALUATION on the dual-print (9/9 10Y-R, +14.13pp) FIRED NOTHING. 20 benign since 7/9. `BND-23` legs 1–2 NOT FIRED; leg 3 = Thu 9/10 30Y-R $22B, bar 62.93 (alt 60.28).**
> 🟠 **Add-gate 7bp [DFII10 2.43, 9/8]; closest approach 5bp [9/2]. `BND-22` has 3 sessions left (9/9–9/11), resolves on the 9/14 publication — do NOT resolve early.**
> 🔴 **CARRY CORRECTED AT THE FISCALDATA PRIMARY: the first stepped-up LONG-END buyback op is THU 9/10 1:40–2:00 PM (10Y–20Y, MAX $6B, 40 eligible), NOT 9/9 (that was cash-management 1Mo–2Y, $12.5B). F2 → RED from the 9/10 results (~2:15 PM). RED + TERRY packeted.**
> ⛔ **NO `git pull` THIS SESSION** — BROCK + TERRY had uncommitted work; origin had nothing new (5 ahead / 0 behind at boot). Pull first next session if they are clean.

## CHANGES SINCE LAST HANDOFF (9/4)

1. **Graded 9/8 3Y + 9/9 10Y-R at the TreasuryDirect primary** (`KB-BND-246/247`; rolling table + VX-01/08/13 + CATALYSTS rows resolved). Downgrade counter 0→1 (the 10Y-R passed both legs; the 3Y's indirect was −1.19pp below median).
2. **`BND-24` RESOLVED TRUE (+4bp)** — 9/3→9/4 Δ2Y +3 > Δ30Y −1; vector +3/+1/−1 front-led. C-36 leg 2 n=2, NOT a path, no upgrade. **THESIS v1.2.3 + CHANGELOG.** `KB-BND-248`.
3. **Buyback date carry corrected** (`KB-BND-250`) across CATALYSTS, VX-16, TRADE, NEXUS_BRIEF, STATUS. Eligible list saved `analysis/2026-09-10_buyback_10-20Y_eligible_list.json`. **August MTS re-dated 9/10→9/11** at FiscalData (`KB-BND-260`).
4. **`docket_check` rc=1 → 9/15 20Y-R `912810UX4` + 9/17 10Y TIPS-R `91282CRE3` docketed with bars frozen pre-print. Blind span 9/11→9/30 HAND-VERIFIED at the Treasury tentative auction schedule PDF** (pdfminer layout parse): 2Y 9/22 · 5Y 9/23 · 7Y 9/24 · 2Y FRN-R 9/23 · Oct 3Y 10/6 · 10Y-R 10/7 · 30Y-R 10/8. Row discharged for September. `KB-BND-262`.
5. **FR2004 8/26 vintage propagated** to TRADE/NEXUS_BRIEF/CATALYSTS/DEALER_CAPACITY (boot_recompute check_fr2004 had flagged three). 8/26 remains the latest published print at 9/9; the 9/2 as-of publishes ~9/10–11 (pull it then). `KB-BND-251`.
6. **`grade_auction.py` PATCHED — prints the `I'` line (P15 linear, STRICT) + the reopening-only alt (last-12 reopenings, the base-rating's construction) beside the OLD test; reproduces the frozen 58.90 / 65.05 / 62.93 and alts 66.32 / 60.28 / 64.66 EXACTLY.** (SCRATCH 9/4 item 8 discharged.) ⚠️ First cut used reopenings *inside the pooled window* (n=8 → 66.95/62.10) — a different set; fixed before commit.
7. **Live refreshes:** SOFR−IORB −1bp (month-end reversed, `KB-BND-254`) · DM cross-section 8/13→9/9 (EA +22.3 > US +17.0 > UK +16.4 > JP +1.8; JGB 10Y 3.006 [9/2] high, 2.891 [9/9]; `KB-BND-253`) · ECB SDW curve 9/8 (front-led flattening) · BTP-Bund ~89 / OAT-Bund ~86 [TE 9/9, secondary] replacing the 54-day-stale 83 · credit 9/8 (CCC 1056 fresh 2026 high; Sept IG ~$215B record forecast, `KB-BND-259`) · TLT 81.73 / ^MOVE 76.74 [9/9] · KW TP 0.8892 [9/4].
8. **Canadian counter-tariffs 9/8 — breakeven re-test NULL** (T10YIE +2bp, DFII10 0; `KB-BND-249`).
9. **WALTER lane 4 → 0** (DNB gold `KB-BND-255` · France>Italy `KB-BND-256` · NVDA erratum `KB-BND-257`, **R1 `COR-20260908-01` receipted APPLIED, `KB-BND-235` → CORRECTED** · copper `KB-BND-258`). **General inbox 7 → 0** (`KB-BND-263`): TERRY 9/8, RED 9/6 ×2 (float precision; "both operators" test withdrawn — NOT adopted), MIDAS-08 indeterminate, PROME WQ-175 (FROZEN-ON-REVISABLE — apply at the next revisable-series registration), PROME L17 (**answered**: US CDS exists at S&P Global, paywalled; no free primary; `KB-BND-261`), PROME NVDA correction.
10. **27 stale ACTIVE KB rows dispositioned individually** (STALE / SUPERSEDED with named successor / Stale_By extended for 107, 160, 243). kb_lint clean.
11. **VX-BND-19 spec observation logged, NOT fixed:** yellow "OAT-Bund >85" is AT its bar (already at 3); red "Bund >3.25 DISORDERLY" has level met (3.40) + an undefined qualifier ⇒ unfireable. **Docketed 10/1** with the quarterly `I'` re-freeze + RED's positive boundary fixture.
12. **Read cap: CATALYSTS was OVER budget (34,101 B) — 5 resolved rows rotated verbatim** (`domain/sources/2026-09-09_CATALYSTS_rows_pruned.md`, crc32 `2773346310`) → 26,658 B; **PREDICTIONS `BND-18`→`21` rotated** (`thesis/archive/PREDICTIONS_resolved_BND-18_to_BND-21.tsv`, crc32 `3942345676`) → 14,549 B. **Watcher registry:** three serviced gates moved to `monitors/WATCH_DATES_serviced.tsv` (inert — `check_dates()` flags every past row PASSED regardless of `Serviced_On`; removal is the only retire), seven September gates added. **Consumer check** on 68.9→65.0 returned 3 🔴 that are all OTHER series (NDFI, FABN) — no packet. **STATUS rotated under the cap** (three verbatim crc-stamped archives: 9/4 BOTTOM LINE `551641974` · VX-20 block `896693574` · Fed-figure cell `562960837`).

## NEXT SESSION (dated, future-verifiable)

0. ⛔ **PULL FIRST** if BROCK/TERRY are clean.
1. 🔴 **9/10 — GRADE THE 30Y-R `912810UW6` $22B on the frozen bars** (`I'` <62.93, alt 60.28 — 60.28–62.93 graded both ways, pooled governs; OLD ind <59.95 AND dlr >14.74; cover re-derive). **Resolve `BND-23`** (TRUE only if all three legs clear). The tool now prints the `I'` line — READ the snapshot, don't re-derive.
2. 🔴 **9/10 ~2:15 PM — pull the FIRST long-end buyback results** (FiscalData `buybacks_operations` + `buybacks_security_details`, `operation_date=2026-09-10`): accepted vs $6B, offer-to-cover, CUSIP distribution vs the saved eligible list. **Route the F2 read to RED same day** (`RED-FT-11` v1.1 gated on it). Off-the-run ⇒ RED adds a butterfly leg at the next non-fired window; on-the-run ⇒ F2 flip candidate — do NOT adjudicate YCC-lite on one op.
3. 🟠 **9/10 — ECB decision** (consensus 25bp → 2.50 DFR): re-pull the ECB SDW curve + BTP/OAT-Bund; `VX-19` re-scores only on a pre-registered leg.
4. 🟠 **9/11 — August MTS** (calendar-artifact test) · **9/11 — PROME hyperscaler IG-share deliverable (a second miss ⇒ DECLINE)**; perimeter = the record September (~$215B).
5. 🟠 **9/14 — resolve `BND-22`** on the 9/11 close's publication; state the closest approach (5bp on 9/2 unless 9/9–9/11 beat it).
6. 🟠 **9/15 — 20Y-R `912810UX4`** (bars frozen: `I'` 61.72 / alt 64.66 · OLD 55.17/17.59 · cover 2.36): the first long-end auction AFTER the official bid — the "does composition normalize?" read registered 8/19. **From 9/11 the kill is PAIRED** (`I'` + FR2004/SOFR−IORB) — the pairing instrument is item 8.
7. 🟡 **9/16 FOMC · 9/17 10Y TIPS-R `91282CRE3`** (no `I'` bar; real-yield referendum) · **9/17 announcement → re-freeze the 2Y/5Y/7Y bars** for 9/22–24 and docket the CUSIPs.
8. 🔴 **9/18 — DELIVER THE FR2004 WEEKLY JOIN** (WQ-157 leg ②, PROME WQ 157 + DOCKET L271). n ≤ 243 (130 SBN2022 + 113 SBN2024, 2022-01-05→); **state the SBN2022/SBN2024 comparability verdict explicitly**; goes to Will only after it lands. Also pull the 9/2 FR2004 as-of when it publishes (~9/10–11) — the 9/1-selloff week.
9. 🟡 Still open: the mirror divergence (VX-05/VX-16 = 4 vs matrix 3/2, 5th session) · `^MOVE`/TLT are yfinance closes · JGB 30Y `[STALE 9/1]` (SAM owns) · LIQUID repo-to-IORB extension · duration-neutral cash construction to LIQUID · DAEDALUS ⑰ residue.

## OPEN THREADS / KNOWN GAPS

- ⚠️ **The kill-leg question cannot be ruled on evidence until the FR2004 join exists** (item 8). TLT-5d answered a PRICE question; the kill is a MECHANISM claim.
- ⚠️ **From 9/10 the 10–30Y sector carries an official bid — post-op curve-shape attribution is contaminated for policy-vs-term-premium.** Grade auctions on composition, ops on CUSIP selection, never either on the tape.
- ⚠️ The corpus refresh script still carries the destroy-on-empty defect (`AUCTION_HEALTH.md` § TOOLING DEFECT) — not run; `grade_auction` overlays TA_WS (AT CAP, 250 rows — recent prints only).
- ⚠️ `fetch.fred_fetch` DEFAULTS TO limit=5 — pass an explicit `limit`.
- ⚠️ WebFetch of the Treasury schedule PDF returns binary — **extract with pdfminer `extract_pages` and rebuild rows by y-coordinate** (the flat `extract_text` loses column alignment). Worked 9/9; reusable for the October span.
- ⚠️ FRED direct (`fredgraph.csv`) `re-test: 2026-09-10` (timed out 9/2; FORGE `fetch.fred_fetch` fine).

## POSITION

**TLT puts HOLD, no add — UNCHANGED. $0.** Only live add-gate DFII10 ≥2.50, **7bp away [2.43, 9/8]** (closest 5bp, 9/2). Composite 12/35, eleventh unchanged. Downgrade counter 1. **OPEN predictions: 2 — `BND-22` (resolves 9/14) · `BND-23` (resolves on the 9/10 30Y-R).** Harvest/roll/sizing are TERRY's. Will's standing 7/16 NO-ADD governs; root rule #5 backstops.

## MAIL

**In: 0** (7 general → `inbox/processed/`, 4 WALTER → `inbox/WALTER/processed/`). **Out: 3 new** — RED (F2 does not exist yet; first long-end op 9/10) · TERRY (buyback attribution starts 9/10; legs 1–2 clean; NO-ADD stands) · PROME (L17 answer + legs 1–2 + `BND-24` + buyback/MTS date corrections + docket adds). All copied to recipient inboxes (PROME's at repo root `PROME/inbox/`). WALTER lane: CLEAR.
