# L708 — issuer universe fixed BEFORE any equity price was pulled

**Written:** 2026-10-15 (`date` in the commit; no issuer price read yet). Source: `issuer_ledger_helper.md` in this folder (an Opus read-only helper's sourced search, 88 tool calls, 10/14 late ET; most ratings are SNIPPET-sourced from filings/press because agency pages are paywalled — VULCAN's 10/9 method had the same limit). Lock rule: `METHOD_LOCK.md` row 6.

## Governing set (named issuers for spec §3) — consumer-facing, non-lending, USD HY bonds, B or CCC with a dated level from a filing or major press
| Issuer | Ticker | Rating used (agency, level, date, source class) | Tier | Bonds |
|---|---|---|---|---|
| Kohl's | KSS | S&P B+ Negative / Moody's CFR B2, unsecured B3 (FY2025 10-K, as of 2026-01-31; Moody's unsecured OPENED) | B | 10% secured 2030 + unsecured |
| Newell Brands | NWL | S&P B+ (2025); Moody's Ba3 CFR / unsecured B1 (2025-04-14) — STALE, no 2026 action found | B (bond level) | senior notes |
| Norwegian Cruise Line | NCLH | S&P B+ / Moody's B1, unsecured B3 (Q2-26 10-Q, as of 2026-06-30) | B | senior unsecured |
| AMC Entertainment | AMC | S&P B- from CCC+ (2026-07-31, secondary) + 8-K 2026-10-05 OPENED: upgrades "by all three" agencies, levels unnamed; B- or CCC either way | B/CCC boundary | $2.0B 1L 2031 (10/5) |
| JetBlue | JBLU | S&P CCC+ from B- (2026-06-08, Reuters); Fitch CCC+ (Apr 2026) | CCC | $2B 9.875% 2031 |
n = 5.

## Sensitivity set (reported beside, never governs) — tier or bonds weakly sourced
| Issuer | Ticker | Why not governing |
|---|---|---|
| Hertz | HTZ | B- issuer / CCC unsecured from aggregators only |
| Petco | WOOF | downgraded 2026-04-13, new level NOT FOUND |
| Herbalife | HLF | Moody's B1, year inferred (2024), STALE |
| Bally's | BALY | Fitch B- (Mar 2025); bonds UNVERIFIED |

## Named, no reachable daily data (count toward the universe description, not toward n)
Michaels (private; S&P B from B- on 2026-09-28, OPENED; 2L notes CCC+) · PetSmart (private) · Staples (private).

## Excluded with reason (BB+, loans only, defaulted, acquired, rating NOT FOUND) — see helper §1b/§2
Macy's, VSCO, BBWI, AAP, SBH, Wayfair, Life Time, Brinker (BB) · Torrid, Dave & Buster's, Cracker Barrel, Red Robin, Leslie's (no HY bonds) · Denny's, Hanesbrands (acquired/private) · Spirit (ceased) · Avis, Six Flags, Bloomin', Papa John's, Peloton, Energizer, Cinemark, Academy, Mister Car Wash, WW, QVC (post-emergence), Saks/Exemplar (rating NOT FOUND).
⚠️ Index membership of each bond was NOT checked against ICE constituent data (unreachable); ICE buckets by bond-level rating.
