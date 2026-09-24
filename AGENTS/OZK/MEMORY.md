# OZK MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Condensed 2026-09-24 (Will-directed): duplicates merged, LESSONS restatements → pointers, old session blocks → git. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02] Will values boot transparency — wants to know what was read, in what order, and whether the process is working. Don't orient silently; confirm orientation.
- [2026-04-02] Will prefers sessions to have freedom rather than being laser-focused on pre-set priorities. Provide context, not directives. Rejected ranked TOP 3 queue in favor of a single "open question."
- [2026-04-02] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] Will prefers breaking large implementation work into discrete tasks done one at a time, with approval between each.
- [2026-04-16] Will wants full source documents (PDFs, 10-Ks) read before opining, not just spot-check sections. Thoroughness > speed for primary source analysis.
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more." Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows.
- [2026-04-22] **Domain CHANGELOG per bank.** OZK/CHANGELOG.md tracks OZK/THESIS.md only — mirrors format of REGINALD's `thesis/CHANGELOG.md`. Version convention: vX.Y where major = structural, minor = refinement.
- [2026-04-24] **Cross-agent channel writing — strip pleasantries.** REGINALD_CHANNEL is LLM-to-LLM. Skip "welcome," "thanks," social glue. Tight bullets, shorthand that matches the other agent's, link-don't-restate. Will corrected initial draft on this.
- [2026-04-24] **Don't frame editorial judgment as tests/pass-fail.** Describing channel inclusion decisions as "test passed" made collaborative comms sound evaluative. Use "filter" or just state the reasoning. Writing to a collaborator isn't a gauntlet. Will pushed back on this framing.
- [2026-04-24] **Offer files, not verbal reports** — audit/review/analysis goes to a named file in own dir (the file is the handoff).
- [2026-07-04] **When Will asks for a priority ORDER, propose one, then work it one task at a time with a checkpoint between each** (overrides the 4/2 single-open-question default when he asks). **Direct writes to another desk's inbox are sanctioned on his explicit instruction.**

## Findings

**Sources & access (OZK files with the FDIC, not the SEC)**
- [2026-07-04 · consolidated 2026-09-24] **OZK files 10-K / 10-Q / 8-K AND Section 16 insider forms with the FDIC (cert #110), not the SEC.** Mechanism: a bank registered under Exchange Act §12(i) files with its primary federal banking regulator; the holding company was dissolved in 2017. **There is no *SEC* 10-Q — there IS an FDIC 10-Q** (`raw/Q1_2026_10Q.pdf` cover: "FEDERAL DEPOSIT INSURANCE CORPORATION · FORM 10-Q · FDIC Certificate No. 110"). SEC CIK 0001569650 is OZK's 13F/13G investment-manager arm; CIK 0001038205 (Bank of the Ozarks Inc) has nothing after 2017. **An empty EDGAR CIK is the EXPECTED observation, not evidence of absence** — the 8/23 note that dropped "SEC" closed this desk's best primary for 5 days (→ `LESSONS.md` §"Compressing a Finding Drops Its Qualifier", KB-OZK-228).
- [2026-07-06] **⭐ FDIC securities-filings JSON API** (`securitiesfilings.fdicconnect.fdic.gov`; old efr.fdic.gov redirects here; browser User-Agent only): `/api/instdiscl/cert/110` = every Form 3/4/5 · `/api/instdiscl/{disclID}` = transaction lines (`asetSctyAcqDspsCde` A/D, `…Cnt` shares, `…ShrAmt` $/sh, `asetSctyOwnCnt` post, `asetSctyTranDte`; exact price range is in the footnote text) · `/api/instflng/cert/110` = all company filings · `/api/instflng/{id}/attachment/{n}` = **the PDF itself** (bypasses 403'd ir.ozk.com). Mechanized as `scripts/flng_watch.py` (in boot.py; `--selftest`).
- [2026-04-22 · 07-18] **What lives where.** Quarterly 8-K bundle (FDIC) = press release + Management Comments (RESG deep dive, substandard roster, sub-notes schedule) + Financial Supplement; the GlobeNewswire/StockTitan release is truncated to EPS + quote. **10-Qs are text PDFs** (pdfminer, tab-delimited; grep "debt-on-debt", "nonaccrual", "subordinated"); **10-Q p.37 carries mgmt's debt-on-debt balance every quarter.** Image-only PDFs (Atrium) need the Read tool's `pages` param. ir.ozk.com 403s scripts — browser only, rarely needed now.
- [2026-08-07 · 09-24] **⭐ FFIEC CDR PWS (REST + JWT).** Base `https://ffieccdr.azure-api.us/public/<function>`, GET. **Every parameter is a HEADER** — `UserID`, **`Authentication: Bearer <token>`** (not "Authorization"), `dataSeries: Call`, `reportingPeriodEndDate`, `fiIDType: ID_RSSD`, `fiID: 107244`, `facsimileFormat: SDF`; query-string forms return 500 "Error Code 5001" (looks like auth, isn't). `RetrievePanelOfReporters` verifies RSSD (OZK = **107244**). `RetrieveFacsimile` body = JSON string of base64 → `;`-delimited SDF. python-urllib default UA is 403'd by the WAF (UA block, not auth). Creds: `FORGE/tools/market-data/.env` (desktop). ⏰ **JWT expires 2026-11-05 — Will action; the Q3 pull (~Nov 1-10) straddles it.**
- [2026-08-07 · 09-24] **Call Report card.** Past-due "OZK basis" = RCON1406+1407+1403 ÷ RCON2122. **NPA% over TOTAL ASSETS** (RCON2170). **NCO ann. on RC-K average loans** (RCON3360), YTD-differenced (RIAD4635/4605 are YTD) — Q1-26 0.56% avg / 0.55% period-end. RCON3123 = ALLL only (~$148M below reported ACL). **No classified/criticized line, no credit names.** **MI3 `RCON2746` ≡ `RCONPV09` (9.a "Other NDFI") ≡ the 10-Q debt-on-debt book** at every quarter checked; Memo-10 `PV05-09` (funded) / `PV12-16` (unfunded) tie the 10-Q NDFI breakdown to the dollar.
- [2026-07-18] **Nasdaq short-interest API** — `api.nasdaq.com/api/quote/OZK/short-interest?assetClass=stocks` (browser UA) = ~24 FINRA settlements with DTC; yfinance gives only the latest two. Float % must be derived. [KB-214]
- [2026-04-02 · 08-23] **Price tooling.** `scripts/market.py` is repo-root (run from root with `.venv/bin/python3`). `fetch.py price --json` carries `asof`/`prev_asof` — branch on vintage, not on "JSON parsed"; `change_pct` is **null** when there's no prior bar (crashed boot.py 9/24). A stale price feeds the <$45/<$40 bands that page other desks, so a stale-as-live bug is an escalation bug.

**Domain facts**
- [2026-04-22] **IQHQ exposure is ONE credit** — "one credit with IQHQ… the senior secured loan on their San Diego RaDD project" (Rossow, OZK CCO, Bisnow 3/19/26). Boynton Yards is **not** IQHQ (Leggat McCall/DLJ/Deutsche Finance). Other IQHQ lenders: Fenway→JPM $165M · Elco Yards→KREF $581M · **Spur Ph I→Apollo $275M (deed-in-lieu to Apollo 9/17/26, single-source TRD)** · 155 N. Beacon→Citizens $486.5M.
- [2026-07-04 · 09-24] **⛔ Vintage trap — seen 4×:** search surfaces a "two-year RaDD extension → Aug 2028" and a "Citi downgrade" as current; both trace to **Jun-2024 Bisnow / May-2024 Citi**. Maturity = **Aug 2026**, from the primary Q1'26 transcript (Mealor, Gleason). Check article dates; check the local primary before re-opening. RaDD funded static at $555M since May 2024.
- [2026-07-04] **RESG concentration (6-qtr primary):** share of unfunded 71→60% (Q4'24→Q1'26; ~79% peak), commitments $34.5B→$27.8B; "88%" is a phantom. [KB-196]
- [2026-07-04 s2] **Bluerock = Bluerock Total Income+ (now BPRE), not "Bluerock Homes."** PIK loans real ($160M@13.5% + $86M@14%); first-loss equity ~$488M; its NAV mark leads RaDD credit. Trade press can confirm a figure while misnaming the entity — verify both. [KB-197/198]
- [2026-07-06] **Sterling Bay: one loss (Lincoln Yards, foreclosed, 320K SF), one PAR exit (Pacific Center, full repayment per Q4'25 Mgmt Comments).** Grep our own quarterly extracts before banking a severity claim from trade press. [KB-199]
- [2026-07-06] **Square Mile Capital = Affinius Capital** (2023 rebrand); OZK holds $95M of the Affinius-originated 777 Industrial note. [KB-203]
- [2026-07-06] **LLM-sourced KB rows can garble primary figures** (KB-117 vs Atrium primary) — treat Conf one notch worse when Source is an LLM output. **Date a third-party report by its citations, not its label** (Atrium said "2026"; citations stop Sep-2025).
- [2026-07-18] **OZK is a beta/range name** — the Nov'25 low was beta to the Oct'25 NDFI-contagion selloff, and the Sep'26 −6.1% was mostly sector (Fed hike, financials selloff). Check the cohort's move before attributing a price move to own-credit. [KB-215]

**Method (the rules themselves live in `LESSONS.md` — pointers only)**
- [2026-07-06] **Partial propagation is this desk's dominant doc-rot mode** — when correcting a figure, grep ALL surfaces for the old value; at revival, check TODO/KB resolutions before re-opening a "gap."
- [2026-08-07] Reproduce a baseline before grading against it (the 37.6% MI3) · never threshold a transit bucket (kill-§1) → `LESSONS.md`. **Don't fix another desk's number, even when disproved** — banner it, write the evidence, route it to the owner.
- [2026-08-23] **Reproduce the other desk's number first** (REGINALD's +$98M, exact) — it shows you're disputing *coverage*, not *accuracy*, and it lands as collaboration. A YoY window nets out a single-quarter step.
- [2026-09-24] **Net quarter-end balances can't exclude a transfer offset by runoff; watch scripts fail closed** → `LESSONS.md` (CATO RB2/RB3).

## Session Notes

⚠️ **Open question:** does OZK report memo item 3 from the debt-on-debt book only? (MI3 ≡ PV09 at every quarter ⇒ zero CRE-purpose balance ever reported from item 4.) *Carried meta-question from 8/28: what check proves a correction pass actually landed? Partial answer — write the per-instrument assertion ledger BEFORE any surface claims "swept" (8/31).*

**CHANGES SINCE:** *(leave blank — next boot populates via boot.py)*

### LAST SESSION (2026-09-24 — Will's catch-up, PROME's 5 tasks, CATO fixes, AM re-check, save-state)

- **Catch-up (dark 8/31→9/24):** FDIC filings none since 8/5 10-Q · Hicks (CFO) + Wolfe sold ≈$574K 8/12-13, zero buys · SI 16.2M / ~16% float @8/31 · $49.08→$46.09 (−6.1% vs KRE −3.8%) · MS→UW 9/8 · Fed +25bp 9/16 · IQHQ Spur deed-in-lieu [single-source] · RaDD nothing. AM re-check 9/24: nothing new. → `research/threads/2026-09-24_CATCHUP_SWEEP.md`.
- **⚖️ L181 RESOLVED — LEGITIMATE, narrowed:** reported debt-on-debt decline **OBSERVED** (10-Q ≡ `RCON2746`, 5/5 qtrs; never in item 4) · runoff **INFERRED** · reclassification out of the book **NOT EXCLUDED** (CATO RB2). → `MI3_2025Q3_ADJUDICATION.md` §6/§6.5, KB-OZK-230; corrections sent to REGINALD + BROCK.
- **L126 sub-notes:** `scripts/flng_watch.py` (schema + coverage validated, rc 2 on bad data, `--selftest` 10/10), in boot.py. Benchmark = **3M term SOFR + 209bp** (issuer release); drag ≈+$11.2M/yr (was $12.8M). PROME runs the watch at its boots to 10/1.
- Housekeeping: inbox → 0 · KB 230/37 · OZK-09 negative-branch instrument named · outbox 11 → delivered/ on evidence (left: 7/20 selfsweep, no receipt; 7/23 ozk09-remark, live citation) · TODO re-baselined · +2 LESSONS · MEMORY condensed (this pass).
- **CATO review (Will-relayed, afternoon): OZ1-OZ4 applied.** ⚠️ **Kill-§1 narrowed to FIRED-LITERAL · mechanism UNDETERMINED** — the "migration-through" dismissal was an inference (a zero-migration flow fits every endpoint). Sub-note redemption now = recalculate (redeem removes ~$280M Tier 2, not just the haircut). Affinius maturity = UNVERIFIED EVENT. OZK-09 attribution guard added (clean searches + no RaDD attribution → STUCK). CATO's next-step advice: **evidence work (Q2 10-Q read, Horton) before more restructuring.**
- **Zero grades/thresholds/weights/conviction moved.**

### NEXT SESSION

1. **Fri 10/2 AM — the 10/1 read (DOCKET L463):** `flng_watch.py` → rc 0 = record **SCHEDULED-UNCONTRADICTED** (never "confirmed"; log rc + row count + date) · rc 1 = read the filing · rc 2 = UNKNOWN, re-run. Benchmark answered: **3M term SOFR + 209bp** (issuer release); call/notice terms still unread (indenture).
2. **Q3 date** (~9/30) → replace boot.py/CALENDAR `~2026-10-21`; build Q3 scoring card pre-print.
3. ⭐ **FIRST (CATO priority):** TODO D4 — full read of the Q2'26 10-Q (Q2 8-K text already extracted in scratch; SEVEN_CREDIT roster needs the Q2 problem-credit table — foreclosed $154M → $293M) (the Q2'25/Q3'25 ones are now local too).
4. 🔴 TODO C1 — Horton leasing (window-search empty, NOT discharged).
5. Open, not L181's: does OZK populate MI3 from the debt-on-debt book only? (MI3 ≡ PV09 every quarter ⇒ zero CRE-purpose from item 4.)
6. Carried: TODO R1/R2/R3 · BPRE 10/6 webinar · P-OZK-1/4/5 Will-gated · FFIEC JWT 2026-11-05 · 7/20 selfsweep packet: no receipt — leave unless evidence surfaces.

⛔ **Standing:** D1/OZK-salvage is **RULED-CLOSED.** Do not re-present, re-litigate or propose a successor. Any future OZK expression is a **new** trade — TERRY-built, Will-gated.

*Prior session notes (8/28 integrity sweep, 8/31 window-close sweep) → `SWEEP_2026-08-28.md`, `research/threads/IQHQ_AUG_WINDOW_CLOSE_SWEEP.md`, `git log -p -- AGENTS/OZK/MEMORY.md`.*
