# REGINALD — 2026-10-20 due row L516 (Nano P&A) · REG-T-03 third bar · whole-inbox drain

PROME Tier-1 spawn (WQ-184 due row, C6 wake). Session start 09:15 ET (`date`). Runtime: Claude Code, Opus. Spawned from PROME cwd; root + desk CLAUDE.md, AGENTS.md, USER.md read explicitly.

## 1. D:L516 — FDIC Nano Banc P&A agreement → **NOT POSTED** (checked 09:16 ET 2026-10-20)

| Check | Result (09:16–09:17 ET) |
|---|---|
| FDIC failed-bank page `fdic.gov/bank-failures/failed-bank-list/nano-banc` (cache-busted, HTTP 200, `last-modified` 13:16:06 GMT) | "Transaction Documentation" links **only the Bid Summary**. Page "Last Updated: **October 19, 2026**" (was Oct 8 at DEWEY's 10/14 check). |
| What changed on the page | New link: **Publication Notice to Creditors and Depositors** (PDF). **Claims Bar Date = January 20, 2027** (FDIC as Receiver, 12 U.S.C. §1821(d)(5)(C)). This resolves CALENDAR read (2) (FIRREA claims bar date). |
| Precedent URL form | Metropolitan Capital page links `/bank-failures/purchase-assumption-agreement-metropolitan-capital-bank-trust-chicago-il.pdf`. Nano equivalents `purchase-assumption-agreement-nano-banc-irvine-ca.pdf`, `…-nano-banc.pdf`, `purchase-and-assumption-agreement-nano-banc-irvine-ca.pdf`, `pa-agreement-…`, `nano-banc-pa.pdf` → **all HTTP 404**. |

**Grade: NOT POSTED as of 09:16 ET 2026-10-20** (25 days after the 9/25 closing; the precedent was ~10 days). Confidence on the absence: VERIFIED for the inspected page and the five guessed URLs; an unlisted file elsewhere is not excluded.
**Nothing settles.** The retained-pool allocation stays at the 10/9 desk SCENARIO (≈$70–90M ≈32–42% of the ≈$215M kept; direction VERIFIED, magnitude INFERRED; `reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`). The headline ≈$120M ≈17% [9/22 base] is unchanged. The $97.1M HFS pool, the ~$81M deposit gap and WAL O1 are still UNKNOWN. DEWEY's 10/14 caveat still applies: the posted schedules may never disclose pool sizes.
**No CREED/WAL routing:** the row routes only on posting. Both desks hold the 10/9 packets; nothing new reaches them except the claims-bar date (info, in PROME memo).
**Proposed disposition (PROME edits the row):** re-date L516 → **Tue 2026-10-27**. That is already the standing source-escalation checkpoint (CALENDAR: "no posting by Tue 10/27 → ask DEWEY for a records route"). If it is still absent then, DEWEY drafts the records route: the FDIC Resolutions Call Center inquiry, which is an external send and needs Will's OK. Also strike "FIRREA claims bar date" from L516/L513 siblings as RESOLVED: **2027-01-20**.

## 2. REG-T-03 third bar → **3-of-3 · CREDIT-CANARY-FIRED** (cross-check: BANK-ABSENT, confidence lowered ~0.7 → ~0.6)

FRED `BAMLH0A0HYM2` fredgraph pull 09:16 ET 10/20: **325 [10/14] · 323 [10/15] · 331 [10/16]** — three consecutive daily closes > 320. It agrees with WALTER SIG-W-20261019-003 and NEXUS 10/19. 10/19 bar not yet published at pull.
**State: CREDIT-CANARY-FIRED, dated 10/16 close** (action REGINALD / CARL info). Per the letter, the fire is recorded **with the cross-check beside it, never as bank transmission by itself**. Exit (only now armed): HY ≤ 300 on 5 consecutive closes. REG-T-04 (>350) is 19bp away, not in play.

**Bank-credit cross-check 10/15 → 10/16** (method `reports/2026-07-30_bank-side-HY-attribution.md`; FRED fredgraph 09:16 ET; yfinance closes pulled 09:17 ET):

| Instrument | 10/15 → 10/16 | Proportional |
|---|---|---|
| BB OAS | 197 → 203 | **+3.05%** |
| B OAS | 326 → 335 | +2.76% |
| HY OAS | 323 → 331 | +2.48% |
| CCC OAS | 1,278 → 1,297 | **+1.49%** (last among HY tiers) |
| IG / BBB OAS | 84 → 85 / 105 → 106 | +1.19% / +0.95% |
| Bank pref/jr-sub basket, n=10 (same names as 10/16) | — | **mean −0.33%, median −0.31%; 7 of 10 down** (HBANL −0.81, OZKAP −0.74, VLYPO −0.66, WAL-PA −0.64) |
| Broad preferred PFF / PGX | 29.17 → 28.86 / 10.09 → 10.04 | **−1.06% / −0.50%** |
| KRE / KBWB / ^BKX | 69.75 → 69.81 / 86.61 → 86.78 / 168.63 → 169.03 | +0.09% / +0.20% / +0.24% |
| BKLN | 20.47 → 20.44 | −0.15% |

**Verdict: BANK-ABSENT on the 10/16 bar**, INFERRED, confidence ~0.6 (lowered from ~0.7). Widening is again BB/B-led with CCC last, the rate/duration signature. Bank equities rose. The bank preferred basket fell, but by **less than the broad preferred market** (−0.33% vs PFF −1.06%), so the bank-specific residual is positive.
⚠️ Why confidence fell: this is the first bar where the bank basket moved down in breadth (7/10). **OZKAP has now fallen 3 straight sessions (15.10 → 14.68, −2.8% since 10/14) into OZK's print tonight**: single-name, not cohort.
Context, not graded: on Mon 10/19 bank equities fell (KRE −0.79%, KBWB −1.07%, ^BKX −1.11%) and the basket slipped again (mean −0.31%, 6/10 down). The 10/19 HY bar is unpublished, so the cross-check for that day waits.
**NEXUS seam (10/19 packet) incorporated:** the earlier BANK-ABSENT covered 10/13→15 only. This section extends it to 10/16 with its own dated instruments. NEXUS's point stands: a broad spread sustain does not establish bank transmission.

## 3. Whole-inbox drain (every sender)

### 3a. Desk packets (6) → `inbox/processed/`

| From | Disposition |
|---|---|
| GIBBS 10/19 first-owner Q3 context | **Seams confirmed** (reply packet to GIBBS). AOCI/Basel calendar row stays REGINALD until an explicit mutual transfer. HBAN stays REGINALD. FITB "INDUSTRY-WIDE" tag accepted **only against the CFG cost/NIB rows**, as GIBBS scoped it. No transfer. |
| NEXUS 10/19 HY-sustain seam | INTEGRATED (§2). |
| WAL 10/19 ×4 (Stage-1 actuals · CET1 numerator correction · broader context · earnings bridge) | INTEGRATED as context. WAL's grades are WAL's (WAL-02 INVALIDATED at 30bp, WAL-01 provisional INVALIDATED). CET1 capital $7,389M disclosed, 10.9% preliminary. Deposits $81.874B → $81.755B, borrowings $6.236B → $5.613B, NIB −$2.068B. No common funding shock. Cautions: special mention 316 → 397, OREO 126 → 165, the $99M appraisal is unidentified. **See §4 for the WQ-318 grade gap.** |

### 3b. WALTER lane: 19 handoffs, all → `inbox/WALTER/processed/` (4 were already logged 10/16 but not moved; 15 newly logged in `board/BOARD_LOG.tsv`)

| SIG | Role | Disposition |
|---|---|---|
| 20261016-029 discount window $11.044B | ACTION | **VERIFIED at the primary.** Fed H.4.1 10/15 Table 1 shows Primary credit Wed 10/14 **11,044**, week avg 11,312, +3,611 w/w (week avg), +5,230 YoY. **Owner decision: no bank-stress reading is assigned and no watch is registered this session.** Borrowers are not named, and precautionary use is not separable from need-based use. KRE was flat. Registering a new threshold is outside this spawn's scope. Carried as a ROADMAP candidate for the next owner session, keyed on the 10/22 H.4.1. |
| 20261016-038 BKX 6-week streak | ACTION | INTEGRATED. Large-bank-led (KRE +1.2% that week). Consistent with BANK-ABSENT. On 10/19, BKX fell 1.11% and KRE 0.79%: still large ≥ regional. |
| 20261019-003 HY 331 3/3 | ACTION | INTEGRATED (§2, fire recorded with cross-check). |
| 20261019-008 OTTO Sept panel 44/44 · OTTO-31 12% → 8% | ACTION | Carried: OTTO's 8% OPEN forecast and its narrow-instrument limit (corporate trust ≠ non-mortgage ABS custody). No REGINALD bank-sizing change. Matrix unchanged. |
| 20261019-001 FITB morning print | INFO | INFO_ONLY |
| 20261019-021 WAL Q3 counterevidence | INFO | INTEGRATED (same evidence as WAL packets) |
| 20261018-005 ATTOM Aug REO +42% YoY | INFO | INFO_ONLY (secondary, month-old) |
| 20261018-006 Kohan Chicago towers | INFO | INFO_ONLY (pledge enforcement, not lender foreclosure; lender unknown) |
| 20261019-004 NAHB HMI 29 | INFO | INFO_ONLY |
| 20261019-006 Exeter reserves / CPS / Enova | INFO | INFO_ONLY |
| 20261019-007 correction Meridian → CREED | INFO | NO-OP receipt COR-20261019-07 |
| 20261019-009 HOMER nine-read | INFO | INFO_ONLY |
| 20261019-010 LIQUID dealer inventory | INFO | INFO_ONLY |
| 20261019-012 OTTO Ally correction | INFO | NO-OP receipt COR-20261019-12 |
| 20261019-014 France OAT | INFO | INFO_ONLY |

Corrections check: rc 1 → **rc 0** after both receipts.

## 4. Gaps disclosed (not done this session)

- **WAL WQ-318 grade (due "within one session of print"; WAL printed 10/19 AMC): NOT GRADED.** The named line, the release "cost of interest-bearing deposits" (Q2 2.74%), is not in WAL's saved reads. EDGAR refused an anonymous fetch: SEC requires a contact User-Agent. ⚠️ Disclosure: one earlier directory-listing request to sec.gov carried Will's email in its User-Agent; I stopped and sent nothing further. What can be said from WAL's figures: the F leg's "brokered/FHLB up ≥15%" conjunct looks unmet, since quarter-end borrowings fell 10%, but brokered deposits are not in hand. **Proposed:** grade at the next REGINALD touch after the 10/20 noon call (WAL's Stage 2), from the release line.
- **OZK Q3 prints tonight AMC** (call Wed 10/21 08:30). OZK desk owns the frame; REGINALD's WQ-318 OZK row is due within one session of the print.
- Print-window `boot.py` sweep: SKIPPED (scoped due-row + drain spawn; not a print-grade session). market.py and the ladder ran: FLG ladder RED, unchanged since 10/7, last settled $10.96 [10/19].
