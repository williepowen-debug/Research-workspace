# Per-bank borrowing screen — FROZEN classification rule (2026-10-28, Will-approved task "set up 1")

**Frozen before any Q3-2026 per-bank data exists** (FDIC BankFind had not posted Q3 at 23:0x ET 10/28; its Q2 index was built 8/19). Verify this file's sha256 before the graded run. Do not edit it. A change needs a new dated frozen document.

## Question
Is the Q3-2026 rise in smaller banks' borrowings (Fed H.8: SA +$33.5B in 6 weeks to 10/14) **broad**, meaning many banks funding loan growth, or **concentrated**, meaning a few banks under strain? If concentrated, which banks?

## Instrument
`scripts/borrowing_screen.py --prior 20260630 --current 20260930` (FDIC BankFind financials API, public, no login, $ thousands).
- **Borrowings** = `OTHBOR` (other borrowed money: FHLB advances, discount window, other) + `FREPP` (fed funds and repos purchased). Same scope as H.8 "borrowings".
- Also reported: `OTHBFHLB` (FHLB subset), `DEP`, `BRO` (brokered), `ASSET`.
- Field identity verified 10/28: Amerant `OTHBFHLB` 6/30/26 = 702,608, matching the ~$702M implied by its Q3 release.
- **Universe:** commercial charters (`BKCLASS` N, NM, SM) excluding the 25 largest by prior-quarter assets. This approximates H.8 "small". Savings institutions and the largest 25 are reported as context only.
- **Merger handling:** a bank whose assets grew ≥20% in the quarter is a probable acquirer. Its borrowings are inherited, so it is excluded from the concentration count and the flags and listed separately. Institutions that vanish between quarters are counted.
- **Refusal:** fewer than 4,000 institutions in either quarter → exit 2. Partial posting; grade nothing.

## Classification (frozen)

| Measure | Rule |
|---|---|
| Concentration | Top 10 individual increases ÷ all individual increases (gross). **≥ 50% → CONCENTRATED · < 25% → BROAD · otherwise MIXED** |
| Bank flag | Borrowings up **≥ $100M and ≥ 25%** of prior (or from zero) **and deposits down** in the quarter |
| Cohort | All 14 cohort banks listed with borrowing, FHLB, deposit and brokered changes, small or large |
| Reconciliation (a check, not a gate) | Screen's small-commercial net change vs H.8 small-bank NSA change between the Wednesdays nearest the quarter-ends (Q3: 7/1 → 9/30 = **+$4.3B**). A difference over $10B is reported as a coverage mismatch |

## Interpretation (fixed in advance)
- **BROAD, few flags:** system-level funding of loan growth, consistent with the H.8 read. No bank-specific lead.
- **CONCENTRATED or MIXED with flags:** read each flagged bank's own release and 10-Q. A flagged name that is listed and has liquid options is passed to TERRY as a NOT-FIRED idea, with this evidence and its grade.
- **A flag is a lead, never a signal.** The aggregate "borrowing up, deposits down" pattern had **no track record** since 1985 (`reports/2026-10-28_small-bank-borrowing-deep-dive.md` §10). The value here is naming banks, not timing the sector.
- ⚠️ **Expect a small aggregate.** Raw (NSA) quarter-end borrowing rose only +$4.3B in Q3 (H.8: 7/1 $302.3B → 9/30 $306.5B), because Q3 normally falls ~3.5% (2010–2025 median). The surge is in seasonally adjusted terms and in the late-September rebound (+10.4% vs a ~0% norm; only 2022 was larger). Read **gross movers**, not the net.
- The screen cannot see intra-quarter swings: anything borrowed and repaid between 6/30 and 9/30 is invisible. The 10/1–10/14 continuation belongs to Q4.

## Timing and routes
- **Primary:** FDIC BankFind Q3 posting, **estimated ~mid/late November** (Q2 posted ~50 days after quarter-end). The script refuses until fully posted.
- **Optional earlier read:** FFIEC CDR per-bank Call Reports (filed by ~10/30; this desk's JWT expires 11/05) for a target list: the cohort plus the Q2 dry-run flags. Not built tonight.
- **Also:** FHLBank 10-Qs (~mid-Nov) name each FHLBank's largest borrowers.

## Dry run (instrument test, Q1 → Q2 2026; not graded)
Output: `domain/sources/2026-10-28_boot/borrowing_screen_dryrun/`.
- Small commercial universe 3,685 banks (ex 25 largest and 48 probable acquirers; 45 institutions gone between quarters). Net **+$21.8B** (+$22.5B including acquirers) vs H.8 NSA **+$19.2B**: reconciles.
- Top-10 share 32.1% → **MIXED**. 47 banks flagged.
- Cohort reproduces known filing figures: Amerant $0.73B → $0.70B; OZK $0.35B → $0.
- The largest Q2 increases were at Pinnacle (+$4.5B), SoFi Bank (+$1.5B), Regions, Associated and United Community. This is a Q2 baseline only.
