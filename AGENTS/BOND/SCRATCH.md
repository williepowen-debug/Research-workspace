# BOND SCRATCH — 2026-09-28 (Mon) ~10:34→12:2x ET (two passes): live-event boot (Will: "yields appear to be blowing out across many countries"). *Prior:* 9/26 `prome-1d` spawn (WQ-291 letter + WQ-246 rec + L0 drain) · 9/25 FR2004 timing/FORUM-7/WQ-290 · 9/24 three sessions.

**Purpose:** ephemeral handoff. Read at boot, rewritten at closeout. Durable → `MEMORY.md`; evidence → `workbook/`. Previous SCRATCH text is in git history (`git show HEAD~1:AGENTS/BOND/SCRATCH.md`).

> ## ⚠️ STATE AT WRITING
> ⛔ **POSITION: TLT Sep-30 77P ×20 — HOLD to expiry, no add (WQ-280), `$0`.** TLT 78.61 intraday 9/28 ⇒ strike 2.0% below spot, 2 sessions left (TERRY's rail). Composite **14/35** (unchanged). Counter **0**. OPEN predictions **0**.
> 🔴 **Rates:** official 30Y 5.49 [9/25] = 3rd straight fresh 2026 high; 9/28 intraday vendor 30Y 5.55 / 10Y 5.23 / 5Y 5.06 (+5bp); global DM 10Y +1 to +7bp (Anglo-sphere-led) — `KB-BND-340`.
> 🔴 **Credit:** CCC 1112 [9/24] ≥ 1100 ⇒ `BND-27` FALSE; 1128 [9/25]; HY 293 (+25bp/3 sessions, ~97th pct), **7bp from 300** — `KB-BND-341`.

## WHAT I DID — 2026-09-28 pass 2 (~11:5x→12:2x, Will: "finish this live-event read with one short assessment")
1. `analysis/2026-09-28_live-event-assessment.md` (+ `KB-BND-343`): rates decomposition (10Y +21 = real +20 / BE +1; TP from 9/24 = INFERENCE) · credit tiers CCC/B/BB/BBB/IG (**B and BBB = the only new pulls, disclosed**) · thesis supported/weakened/unchanged-score · evidence ≠ authorization · one new research need (cross-market attribution → PROME to scope).
2. PROME memo `PROME/inbox/2026-09-28_from-BOND_live-event-assessment-and-10-1-dealer-test.md` (assessment + WQ-291 10/1 conditions; **explicit: test lands AFTER the 9/30 expiry**; Will's hold/NO-ADD unchanged). LIQUID facts packet `AGENTS/LIQUID/inbox/2026-09-28_from-BOND_credit-tier-facts-for-Q4-grade.md` (their grade; B crossed p75 9/24, D1 not met).
3. NEXUS_BRIEF T5YIFR distance fixed (history kept as "was 14bp", current 16bp [9/25], caveat that breakevens stay flat); boot_recompute derived-distance + FR2004 drift now clean.
4. prome-7f SendMessage'd 11:07 asking for exactly this memo; PROME + LIQUID doorbelled after commit.

## WHAT I DID — 2026-09-28
1. Boot: pull clean (0 behind) · boot_recompute rc1 = 3 findings (STATUS:28 + SCRATCH:17 FR2004 teaching/history lines; NEXUS_BRIEF:16 T5YIFR "14bp" vs 16) — STATUS/SCRATCH lines rewritten away this session; NEXUS_BRIEF NOT fixed (see threads) · docket_check rc1: 10/6 3Y `91282CRQ6`, 10/7 10Y-R `91282CRF0`, 10/8 30Y-R `912810UW6` — rows EXISTED with CUSIP "TBA"; CUSIPs added · corrections rc0 (COR-20260925-13 ALL-warn, not BOND's).
2. Live read (Treasury official 9/25 + yfinance intraday + TE global + FRED credit/funding) → `KB-BND-340`, `KB-BND-341`; VX-02/05/11 refreshed (VX-11 3→4 on the registered 1100 escalation); VX-01 write-back (owed since 9/24) done.
3. `BND-27` RESOLVED FALSE (first-published vintage verified). Knowledge check: LIQUID + BROCK STATUS already carry CCC 1112 [9/24] ⇒ no packet (disclosed in KB-341).
4. **WQ-291 + WQ-246 ENCODED** (PROME packet 9/26 15:57, ~43h late): THESIS v1.2.9 (DFII10 row replaced; WQ-291 bullet + three riders in the kill section) · CHANGELOG · TRADE gate (a) · STATUS gate table · `KB-BND-342`. Packet git-mv'd to `inbox/processed/`. **Reply with hashes → PROME owed (this commit).**
5. STATUS rewritten (top block condensed; full 9/26 file → `domain/sources/2026-09-28_STATUS_full-snapshot_pre-9-28-rewrite.md`).

## 🔴 NEXT SESSION (dated, future-verifiable)
1. 🔴 **Tue 9/29 AM: HY OAS 9/28 cell** — >300 with this velocity = matrix row 4 letter ⇒ 3, and the HYG-put question reopens on INDEX evidence (TERRY card + Will; never a BOND action). Also DGS30 9/28 official vs 5.49 (4th high?).
2. 🔴 **Wed 9/30:** quarter-end; Aug PCE + GDP 3rd; SOFR−IORB (0bp [9/25]); TLT 77P expiry (TERRY).
3. 🔴 **Thu 10/1 ~16:15: FR2004 as-of 9/23 — WQ-291 grade: 3–6Y ≥ $56.586B ⇒ MET** (report MET / NOT MET / GAP with margin by the 10/2 boot; riders: not proof of warehousing; funding window UNGRADED; a MET = recommendation via TERRY + Will). Same print = FORUM-7 FINAL D3a/D3b (HENRY letter `bc540e071`) + L477 Q4 below-IG inventory (`KB-BND-336`). `fr2004_fetch.py` pulls 7Y+ only — pull `PDPOSGSC-G3L6` explicitly (`analysis/2026-09-25_FORUM-7_fr2004_series.py`). Also H.4.1 week-9/30 (ZHAO reader), F2 10Y–20Y op, quarterly `I'` refresh + corpus re-run, `VX-19` definition, TIPS-`I'` question (DOCKET L410).
4. 🟠 **10/1 announcement → freeze bars for 10/6 3Y / 10/7 10Y-R / 10/8 30Y-R** (the 10/7–10/8 long-end legs can fire row 1's ⇒5 letter). Blind span 10/9→10/19 UNVERIFIED by tool — hand-check against the QRA tentative schedule.
5. 🟠 **By 9/30: `READS.tsv` declaration** (BOND has 0 rows in `PROME/registry/READS.tsv`; DAEDALUS ask) — carried, not done.
6. 🟠 **By 10/21:** register the 10/28 FOMC curve-shape prediction with a base rate (OPEN count is now 0).
7. 🟡 `check_fr2004` pattern gap (bare "FR2004 m/d:" form) · `DEALER_CAPACITY.md` body refresh · `KB-BND-307` cadence correction · NEXUS_BRIEF:16 T5YIFR distance (14→16bp) — all carried.

## OPEN THREADS / KNOWN GAPS
- 🔴 **LIQUID owns the Q4 grade on the 9/25+ cells** (BOND sent facts only). Next BOND-side: D6 FR2004 below-IG 10/1; D8 pulled-HY-deal check STALE since 9/17 (gap). Watch B 15-session ≥ +28 on 9/28–9/30 cells, IG ≥ +6 / BBB ≥ +7.
- 🟡 **New research need named, not started:** cross-market attribution of the 9/22→9/28 move (BOND/HANS/SAM) — PROME scopes.
- ACM/KW TP not re-pulled 9/28 (STATUS marks STALE); FORUM-7 P2 KW grade is HENRY's (~9/28–29).
- Intraday Brent front quote looked like a roll artifact (−5.2%, contract UNKNOWN) — oil is BRENT's; not cited.
- No global-sell-off packet sent: EU/JGB/FX legs belong to HANS/LIQUID/SAM and WALTER routes news. If the OAT>BTP inversion is new to LIQUID, that is LIQUID's lane.
- Replies owed TO BOND: ZHAO (custody/TIC).
- TRAPS (carried): `csv.writer` re-quotes TSV fields — use raw split/join · `python3 -c` fails in this shell wrapper (use a script file) · `fetch.fred_fetch` default limit=5 · ACM xls "ACM Daily" sheet · venv for `grade_auction`/`cdx_proxy`/xlrd.

## POSITION
**TLT Sep-30 77P ×20 — HOLD to expiry, `$0`.** No add (WQ-280). Harvest/expiry = TERRY.

## MAIL
**In:** PROME WQ-291/246 RULED packet — encoded, processed. **Out:** PROME ×2 (WQ-291/246 hashes `5a4c81bfa`; live-event assessment + 10/1 test) · LIQUID ×1 (credit-tier facts for Q4 grade).
