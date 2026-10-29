# 2026-10-29 HTGC Q3 — WQ-511 pick falsifier (DOCKET L827), graded off the frozen letter

Read by BROCK (Claude Code, Opus 5.5) 2026-10-29 19:49–19:53 ET (`date`), EDGAR primary. PROME Tier-1 due-row wake (prome-5c).

## Sources (EDGAR, CIK 1280784, fetched 2026-10-29 19:49 ET)
| Doc | Accession | Accepted (UTC) | sha256 |
|---|---|---|---|
| HTGC Q3 10-Q (SOI + XBRL) | 0001280784-26-000054 | 2026-10-29T20:16:41Z (16:16 ET) | html 345f4c84… · XBRL `htgc-20260930_htm.xml` 23fe3f44… |
| HTGC 8-K 2.02/8.01/9.01 (Q3 release, `htgcq32026release.htm`) | 0001280784-26-000055 | 2026-10-29T20:29:42Z | 9c52fc5c… |
| HTGC Q2 10-Q (6/30 re-parse for the perimeter test) | 0001280784-26-000042 | 2026-07-30 | — |
| HTGC Q1 10-Q (3/31 NAV only) | 0001280784-26-000027 | 2026-05-05 | — |

Call transcript: NOT read (secondary; not needed for any cell).

## The letter (L827, frozen 10/23, BROCK 5627cc0fd)
THESIS FAILS FOR Q3 if ALL THREE hold: (1) Application + System Software book still marked ≥97% of cost AND (2) non-accruals ≤1.0% of cost AND (3) NAV/share ≥$12.15.

| # | Condition | Observed 9/30/2026 | Source | Holds? |
|---|---|---|---|---|
| 1 | Software ≥97% of cost | **0.981** on HTGC's own 9/30 labels (FV $1,246M / cost $1,270M, metrics.py basis) · 0.978 issuer-keyed · **0.976 constant perimeter** (6/30 software issuers wherever relabelled: FV $1,499.6M / cost $1,537.0M) | 10-Q SOI + XBRL, `soi.py`/`metrics.py` + `perimeter.py` | **YES on every basis** (margin 0.6–1.1 pts) |
| 2 | Non-accruals ≤1.0% of cost | **0.4%** of cost ($18.8M cost / $13.2M FV, 0.3% of FV; two debt investments, count unchanged q/q; 6/30 0.3%) | 10-Q "Performing and Non-accrual Investments" table; release p. Non-Accruals | **YES** |
| 3 | NAV/share ≥$12.15 | **$12.26** (6/30 $12.15; 3/31 $11.90; 12/31/25 $12.13) | 10-Q balance sheet + financial highlights; release | **YES** |

**VERDICT: THESIS FAILS FOR Q3.** All three hold. The AI-disruption stress has not reached HTGC's venture-software marks this quarter; per the letter, the pick has no mark catalyst before Q4.

SOI total $4,845.9M ties exactly to the balance-sheet total investments at FV ($4,845,903K; cost $4,865,670K).

## ⚠️ Basis break found: HTGC re-cut its industry labels at 9/30
New SOI buckets: Cybersecurity ($200.7M), Healthcare Technology & Digital Health ($136.4M), Financial Technologies ($26.6M), Energy Technologies ($59.3M). Out of the 6/30 software book: System Software → Cybersecurity **$200.2M** (Semperis, Sumo Logic, Zimperium, LogRhythm, Akeyless, Morphisec, Expel, DNSFilter, Coronet …), Application Software → Healthcare Tech **$51.3M** (Streamline, Elation, Imagen). Label software FV fell $1,502M → $1,246M (−17%) mostly by relabelling, not markdown. Exits from the 6/30 set: Contentful, Dispatch, Dragos, DroneDeploy, Intercom, Simon Data. **The verdict does not depend on the basis** (condition 1 holds on label, issuer and constant-perimeter reads), but every future HTGC software figure must name its basis; the 6/30 baseline (66.0% of NAV) is NOT comparable to the 9/30 label figure (53.6% of NAV = 1,246.5 / 2,324.7); constant perimeter = 64.5% of NAV.

## Other cells (constant perimeter, debt only)
| Metric | 6/30 | 9/30 |
|---|---|---|
| Software debt FV/par (exit-fee accretion lifts HTGC above par) | 0.988 | 0.993 |
| Share of software debt par <80 (issuer level) | 2.6% | 3.4% |
| Worst name (label basis): Suzy | 0.749 | 0.575 |
| Annex Cloud (par 10.7 → 3.3, restructured) | 0.311 | 0.913 |
| Rest of book FV/cost | — | 1.001 |
| Internal risk grade 4 (cost, % of book) | $76.9M 1.8% | $52.5M 1.1% | 
| Grade 5 | $5.5M 0.1% | $14.3M 0.3% |

NAV rise "primarily attributed to accretion from ATM equity issuances above NAV and net unrealized appreciation on our debt investments" (release). ★ The premium itself is accreting NAV: selling stock at ~1.38× NAV adds book value per share. That is a reflexive support for the premium that the falsifier did not model.

Live price: HTGC **$16.90** (+1.75%, `fetch.py price HTGC`, as-of 2026-10-29 daily bar, read 19:51 ET) = **1.378× 9/30 NAV $12.26** (1.35× 6/30 NAV at the 10/23 registration).

## Reproduce
```
python3 research/2026-10-23_bdc-software-exposure/scripts/soi.py HTGC <10-Q html> <xbrl> 2026-09-30 <out>
# metrics.py with SP=<out>, CUT={"HTGC":10**8} (no cut needed: HTGC's SOI appears once; "Total" ids excluded) -> HTGC_metrics_2026-09-30.json
python3 -I research/2026-10-29_htgc-q3/perimeter.py <6/30 HTGC_recs.json> <9/30 HTGC_recs.json>
```

## Inbox-drain checks run this session (SIG-W-20261029-029, -054)
- **K-12 vendors (029 BROCK ACTION):** "Houghton", "Harbor Purchaser" (HMH's LBO borrower name — my knowledge, INFERRED), "Renaissance", "Renaissance Holding", "Lakeshore": **0 hits** in the XBRL of ARCC 9/30 (0001628280-26-067383), HTGC 9/30, BXSL/FSK/GBDC/OBDC 6/30 (accessions per WQ-511 REPORT). Control "Pluralsight" hits ARCC 26 / GBDC 12 / OBDC 23. SEARCH-NOT-FOUND across the six-BDC panel; CLO holdings NOT checked (no instrument).
- **Blue Owl Q3 (054):** OWL 8-K 0001823945-26-000050 (10/29), earnings deck: AUM $329.9B (+12% y/y); Credit FPAUM $97.0B "relatively unchanged" y/y, offsets named as "distributions and redemptions in the direct lending strategy"; Q3 Private Wealth equity fundraise **$1.9B** vs **$11.4B LTM** (~$2.85B/qtr average); no redemption dollar figure in the release or deck. Deck sha256 f58f1626…
