# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

*(7/25 section pruned 2026-08-13 — 19d, promote-or-delete per lesson-14: the **perl EDGAR-table recipe** and the **regex-backtracking gotcha** → MEMORY §Findings; **"a stated basis is falsifiable, an unstated one isn't"** and the **control-covers-the-anticipated-case shape** → MEMORY lessons (the shape got two fresh instances today); the **EGBN two-route ACL cross-check** → MEMORY §Findings; the **small-bank-CRE-bid half-thought** → ROADMAP backlog; CCC/HY fire-#2 arithmetic DELETED as superseded by the full FRED series pulled 8/13. 7/17 section pruned 2026-08-10 — >3wk, per the lesson-14 discipline this time (same-session promote-or-delete, no unpromoted control-notes left behind): **the one live note — WALTER's BB/B sub-index gap on REG-T-03/04 — was PROMOTED to `registry/NOTES.md` §REG-T-03/04** before deletion; the other three (tripwire decomp design lesson, CFG beta-vs-substance, Brent overtaken) were already canon in ROADMAP/brief/STATUS. 7/10 section pruned 7/30 — its "two-clock header silences its own nag" note became MEMORY lesson 14 after sitting unpromoted 20 days.)*

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*

---

*(Sections 2026-08-27 (×2), 09-01 and 09-02 pruned 2026-09-24 at closeout, all >2 weeks old: rotated VERBATIM → `archive/SCRATCH_rotation_2026-09-24.md` (crc-stamped). The durable recipes in them (EDGAR/FFIEC fetch, perl table extraction) already live in `MEMORY_REFERENCE.md`.)*

## 2026-09-29 PM — Will: "regionals have been selling off, no?" (post-closeout, sized on yfinance closes 9/29)

| tkr | 9/29 | since 9/14 | 1m (8/29) | since 8/13 | vs Jul–Sep high |
|---|---|---|---|---|---|
| KRE | 69.83 | −5.8% | −6.0% | −10.2% | −10.4% (8/14) |
| WAL | 75.76 | −4.3% | −3.5% | −7.3% | −10.2% (8/04) |
| OZK | 46.20 | −5.9% | −6.5% | −11.6% | −13.0% (7/16) |
| ZION | 62.61 | −9.5% | −7.6% | −12.6% | −14.6% (7/16) |
| FLG | 11.84 | −9.1% | −12.0% | −17.0% | −22.9% (7/16) |
| EGBN | 27.96 | −0.1% | +1.4% | −2.8% | −2.9% (8/14) |
| VLY | 12.72 | −8.1% | −8.6% | −15.3% | −16.3% (7/16) |
| CFG | 63.89 | −9.4% | −8.3% | −13.8% | −14.5% (8/14) |
| SPY | 764.20 | +0.4% | −0.7% | −1.8% | −1.8% |
| IWM | 279.01 | −3.1% | −5.7% | −8.1% | −8.5% |
| XLF | 54.01 | −5.3% | −7.0% | −7.3% | −7.8% (9/03) |

KRE since 9/14: 12 sessions, 7 down / 4 up / 1 flat; 74.11 → 69.83. **Yes, a selloff, not a drift — I under-stated it in the 9/29 brief.** Sector-wide (XLF −5.3% too), regionals ~2× the small-cap index, SPY flat. EGBN is the outlier that has NOT sold off. Promote: STATUS §THRESHOLD KRE row wording ('drift' → 'selloff, −10% from the 8/14 high') at next boot; ROADMAP 8/14+ de-rating thread now has a second leg (9/14→9/29) with a credit co-mover.
→ **Will 18:2x ET: "Send this to TERRY for a card on adding KRE puts."** Sent: `AGENTS/TERRY/inbox/2026-09-29_from-REGINALD_WILL-ASK-card-for-adding-KRE-puts-regional-selloff-sized.md` (table + credit tiers + live KRE legs + trigger asymmetry: REG-T-01 UN-FIRED, REG-T-02 FIRED; root rule #6: 9/29 was red). TERRY dark → doorbell PROME (rule 6b). Card, approval and fill are TERRY's and Will's; nothing constructed here. Close the loop: record TERRY's card id + Will's decision in STATUS/POSITIONS when they land (root rule #10).

**Will 18:4x ET: "why are the banks selling off — what does our research tell us?"** Answer given from the fleet record (NEXUS WQ-340 one-root read 9/29 · LIQUID §1 NOW 9/29 · BOND KB-BND-367 · HENRY KRE row · my 9/24 AOCI + 9/27 cross-bank + blind-spot thread): (1) ESTABLISHED — the price of money: real 10Y +27bp 9/22→9/28, 30Y highest since 2004, bear steepener; AOCI/TBV is the bank mechanism, ~−$2.6B to −$4.3B cohort-wide at D=3–5 (assumed), ZION most exposed; (2) FIRED THIS WEEK — credit broadening: HY 302 / B 309 / BB 183, LIQUID 'BROADENS 3rd print', composition unmeasured (cable-led 9/25); reaches banks via fund-finance/NDFI lending, none visible in bank data before Q3; (3) CANDIDATE, UNOWNED — AI-disruption / 'Muse' agentic deposit-flight narrative (BKX −3.5%/5d, cable −10 to −21%), WQ-341 open, PRED-50 tests 9/29→10/8; (4) AMPLIFIER — dealer gamma negative both horizons since 9/28 (HENRY); (5) WHAT IT IS NOT — not labor (claims 197K), not funding (SOFR−IORB 0), not a bank-credit print (Q2 cross-bank CRE bad-loan rate FELL; no 8-Ks; Nano n=1). Told Will plainly: my desk's instruments are blind to (2)–(3) until ~10/20; the 8/14→9/14 leg is still unattributed. No file changed beyond this note.

**Will 18:5x ET: "job openings report was bad today though — read LABOR status/NEXUS."** Read both. LABOR graded JOLTS Aug on its NET rule (+122K ⇒ benign, v4 3→2, LEG C MET) and neither STATUS nor brief states the OPENINGS level; KB-LAB-193 has it: **openings 7,079K [Aug P] vs 7,335K Jul (−256K), rate 4.3%, consensus ~7,228K ⇒ −149K miss; lowest since Mar (6,887K).** Both true: benign on flow (low-fire), weak on demand (openings). Sent LABOR a 🟡 packet (no binding ask). For my chain: nothing moves — layoffs 1.0%, claims 197K; the bank ORANGE→RED trigger (claims >300K) is 103K away.

## 2026-10-07 PM — L527 session (PROME-spawned, Opus): working notes

**Instrument notes (not yet promoted):**
- FFIEC CDR JWT WORKS on the laptop (token in `FORGE/tools/market-data/.env` since 9/22) — the CALENDAR 11/05 row's "desktop-only" remark is stale; regeneration before 11/05 is still Will's.
- `fetch.py fred` CDN-stale class: used the cache-busted `fredgraph.csv?...&nocache=` route + `fred_fetch_vintage(basis='first-published')`; identical on every HY/CCC/B/BB cell 9/25–10/6.
- Independent price route that works from this box: `api.nasdaq.com/api/quote/<T>/historical` (UA + Accept json). Stooq now serves a JS proof-of-work page — dead for curl.
- RC-K average IB deposits ÷ period-end IB: ~1.33× EGBN every quarter, ~1.1× OZK, 1.34× CUBI in 2025 → [CR] deposit cost INCOMPARABLE there (KB ML-REG-180; lesson 42). Cause not chased.
- `firetime_check.py` reads quarter labels like `[12/24]` as day dates (Nano report: 3 flags, all quarter labels → KEEP). A detector false positive class worth telling DAEDALUS if it recurs.

**Things I noticed but did not dig into:**
- OZK −4.31% on 10/6 vs KRE −0.45%, no news found (one search). OZK desk's own <$45 band closed below 10/6 ($44.58) and 10/7 ($43.56) — the OZK desk grades it; OZK desk last committed 10/2.
- CFG FHLB advances 0.01B [9/30/25] → 6.36B [6/30/26]; +3.85B in Q2 alone, while CFG cut ~$1.5B Treasury brokered (INFERENCE: substitution). It is in the WQ-318 F3 line.
- STLFSI4 +0.34 in the week to 10/2. One week; not a level signal.
- Sub-reader side finding (NOT verified by me): VLY 8-K dated 2026-09-28 announces a merger agreement to acquire Bluevine Inc. (small-business fintech). If true, it touches my BaaS/sponsor-bank perimeter (WQ-228). Read the 8-K before citing.

## 2026-10-09 PM — evening boot (Will-launched, Opus 5.5, 20:24 ET)

**Instrument defects found at boot (NOT fixed; reported to Will; promote at closeout):**
- `scripts/8k_monitor.py:21` + `scripts/insider.py:23` query SEC EDGAR for OZK (CIK 1569650). **OZK files NO SEC periodic reports** (MEMORY_REFERENCE 6/20; it files with the FDIC). ⇒ boot.py's "✅ No 8-K filings across any thesis name" and OZK "No Form 4 filings" are clean BY CONSTRUCTION = clean against the wrong reference. OZK's live route is FDIC FLNG (cert 110), the OZK desk's sweep route.
- Same TARGETS list = WAL/OZK/EGBN/ZION/VLY: **misses FLG (6) and AMTB (5)**, two of the three elevated v2.0 names, and CFG (first Q3 print, 10/16).
- `earnings_countdown.py` prints "No upcoming earnings dates" in print week. Dates are CALENDAR-owned; fix = read CALENDAR or drop the step, never a second hand-typed list.
- `vx_ladder_check.py` (owed 10/15) refinement: at 20:3x ET the 10/9 yfinance bar is STILL unsettled (Close=NaN, partial volume) and printed "last close $nan"; the 10:26 ET run carried a non-NaN in-progress value (11.25) and counted it. ⇒ a 16:00 clock filter alone fails (evening NaN) and a NaN filter alone fails (morning value). Fix: always exclude today's (ET) bar; print the vendor quote separately, labelled unsettled.

**Tape 10/9 — vendor quotes (market.py 20:24 ET); settled bars NOT posted (yfinance daily Close NaN; Nasdaq historical has no 10/9 row):** WAL 74.27 (−1.63%) · KRE 69.01 (−0.83%) · FLG 11.32 · OZK 44.41 (−1.00%) · EGBN 28.22 · CFG 63.57 · VLY 12.62 · ZION 62.49 · SSB 100.25 · HBAN 15.32 · SPY +0.60% · IWM +0.49% · VIX 14.84 · ^TNX 5.24. KRE Nasdaq "closed 4:00 PM" 69.05 vs yfinance 69.01 (unreconciled). ⇒ **WAL exit-log row for 10/9 DEFERRED to next session (settled bars only)**; it cannot qualify on any plausible value ($7.63 short of 81.90).

**FRED (API route via fetch.py, 20:4x ET):** credit cells through 10/8 unchanged from the AM read (HY 315 · CCC 1,252 · B 315 · BB 194). ICSA w/e 10/3 **197K**; w/e 9/26 **revised 197 → 199K**. DGS10 5.22 / DGS30 5.60 [10/8]. STLFSI4/NFCI still 10/2. ⚠️ The cache-busted `fredgraph.csv` route FAILED tonight (HTTP/2 INTERNAL_ERROR with `&v=`; HTTP/1.1 timeout with `&nocache=`); plain URL returns 200 (= CDN copy). Single route for the claims revision.

**KRE float (boot.py):** 53.53M sh vs 56.11M [9/29] = −2.58M / −4.6%. Fund-report date not verified; not base-rated ⇒ a description, not a signal.

**HBAN $16P Oct-16 ×2:** HBAN 15.32 [10/9 quote] ⇒ $0.68 ITM (card 9/26: $0.36). WQ-302 rules by Wed 10/14 close.

**PROME prome-1e cross-session ping (rcv ~20:42 ET, coordination, NOT an assignment):** no REGINALD docket row due 10/9. Dates restated: L516 Nano P&A re-check Tue 10/13 · 10/13 ICE cell for REG-T-03 · WAL Q3 10/19 AMC (L170, WAL desk). **OZK's $915M RaDD bridge matured today; the OZK desk reads it Mon (L635)**, which answers my boot gap. HEARTBEAT 10/9c levels: FLG 11.31 · OZK 44.41 · WAL 74.28 · KRE 69.04, vs my vendor quotes 11.32 · 44.41 · 74.27 · 69.01. Off by 1–3 cents ⇒ more evidence that the 10/9 closes are unsettled; grade from settled bars. **CLOSEOUT OBLIGATIONS:** memo to `PROME/inbox/` (repo root) per COMPLETION_SPEC + one-line **WQ-249 receipt** to prome-1e. Shared index: AEOLUS has staged renames, so pathspec commits only.
