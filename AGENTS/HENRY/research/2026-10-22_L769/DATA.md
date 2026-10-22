# HENRY 2026-10-22 — DOCKET L769: HEN-46 American leg + gamma into the open

Session: Claude Code, Opus 5.5 (`claude-opus-5-5`), spawned by PROME (prome-56, session 84affa50) under WQ-479 A. Clock from `date` in each command.

## 1. American Airlines Q3 2026 (primary)

Source: SEC EDGAR, AAL CIK 6201, 8-K accession 0000006201-26-000064, accepted 2026-10-22 11:00:25Z (items 2.02, 7.01, 9.01). Exhibit 99.1 saved as `src/aal-q3-ex99.htm` (text extract `src/aal-q3-ex99.txt`). Prior guidance: Q2 8-K 0000006201-26-000051 (7/23), Ex 99.1 saved as `src/aal-q2-ex99.htm`.

| Item | Q3 actual (10/22 8-K) | Guide / assumption (7/23 8-K) | Read |
|---|---:|---:|---|
| Adjusted EPS | −$0.28 (adj net loss $182M) | −$0.70 to −$0.10 | INSIDE, $0.42 above the low end |
| GAAP EPS | −$0.41 (net loss $269M) | — | — |
| Fuel price incl. taxes | $3.85/gal | ~$3.75/gal (curve of July 21) | +$0.10/gal (+2.7%) |
| Fuel gallons | 1,204M | — | overrun ≈ $120M pre-tax |
| Total revenue | $16.3B, +19.3% YoY | +16.0% to +19.0% | ABOVE the high end |
| FY2026 adj EPS guide | −$1.60 to −$1.00 | −$0.65 to +$0.65 | CUT (F4 not fired) |
| Q4 fuel / adj EPS guide | ~$4.70/gal; −$1.10 to −$0.50 | — | outside the Q3 letter |

Implied diluted shares ≈ 182 / 0.28 = 650M (INFERRED). Overrun per share ≈ $0.19 pre-tax.

## 2. HEN-46 grade under the pre-stated disposition

Disposition written 2026-10-21 21:10 ET (commit 2e59e4d8a, PREDICTIONS.tsv HEN-46), before American printed: AAL < −$0.70 → CONFIRM; AAL ≥ −$0.70 → NO-VERDICT-AS-WRITTEN with the substantive read "claim not supported", not relabelled DENY.

| Letter test | Threshold | Observed | Result |
|---|---|---|---|
| CONFIRM, AAL leg | adj EPS < −$0.70 | −$0.28 | NOT MET |
| CONFIRM, LUV leg (graded 10/21) | fuel ≥ $4.10/gal | $3.92 ($3.87 unhedged) | NOT MET |
| DENY | AAL inside/above guide AND LUV ≤ $3.85 | AAL inside; LUV $3.92/$3.87 | NOT MET (LUV leg) |

**Verdict: RESOLVED-NO-VERDICT-AS-WRITTEN; claim not supported.** Both carriers overran their fuel assumptions by $0.10–0.22/gal, against ~$0.40/gal the registration projected, and both absorbed it with record revenue.

Outcomes against as-made confidences (no re-mark): AAL miss 0.35 → 0 · LUV CONFIRM leg 0.30 → 0 · card opened 0.20 → 0. Brier 0.1225 / 0.09 / 0.04.

Southwest's 10:00 ET call was not waited for. Its only open item (the basis of the July assumption) cannot move the verdict, because both Southwest fuel bases sit in the unnamed region.

## 3. Gamma and tape into the 09:30 open

`AGENTS/HENRY/scripts/gamma_flip.py --both`, run 08:32:08 ET (Cboe chain asof 2026-10-22; spot input = SPX 10/21 close 7,757.17, because cash SPX is not trading pre-open):

| Horizon | Contracts | Flip | Net GEX per 1% | Put wall | Call wall |
|---|---:|---:|---:|---|---|
| 14d | 3,405 | ~7,742 | +$10.2B | 7,750 (clean, +44% over #2) | 7,800 near-tie → band 7,800–7,900 |
| 35d | 7,197 | ~7,748 | +$7.2B | 7,750 (clean, +30% over #2) | 8,000 near-tie → band 7,900–8,000 |
| Cross-horizon | — | band 7,742–7,748 | POSITIVE both | PUBLISH 7,750 | WITHHOLD (7,800 vs 8,000) |

Tape (`FORGE/tools/market-data/fetch.py`, vendor quotes):

| Time ET | ESZ26 | Change | VIX | Nikkei | Hang Seng |
|---|---:|---:|---:|---:|---:|
| 08:32 | 7,725.50 | −0.96% | 18.09 | — | — |
| 08:36 | 7,727.00 | −0.94% | 18.10 (+8.51%) | 62,907.84 (−2.65%) | 22,934.68 (−3.03%) |

ES 10/21 daily close 7,800.25 (vendor; the 10/20 and 10/21 rows carry an identical volume 1,718,580, a copy-forward signature, so the close is a vendor row, not a certified settle). ES−SPX basis at the 10/21 close ≈ +43, consistent with ~2 months of carry.

**Implied SPX at the open** = 7,757.17 × (7,727.00 / 7,800.25) ≈ **7,684** (08:36 ET). That is **~58 pts below the 14d flip, ~64 pts below the 35d flip, and ~66 pts below the 7,750 put wall.** If futures hold, SPX opens in NEGATIVE gamma (dealers amplify moves), below the put wall. This is an implied pre-open read, not a cash test of the put wall.

Caveats: free-tier proxy; the sign and the flip are the robust reads; dollar magnitudes depend on assumptions; the flip is a property of the chain's gamma profile and shifts as open interest and the open itself reprice the chain.

## 4. FINRA margin debt (WALTER SIG-W-20261021-029 ACTION)

FINRA `margin-statistics.xlsx` (finra.org, pulled 2026-10-22 08:3x ET; saved `src/finra/`): debit balances in customers' securities margin accounts, $ millions.

| Month | Debit balances | Note |
|---|---:|---|
| 2026-06 | 1,502,072 | record |
| 2026-08 | 1,453,832 | — |
| 2026-09 | 1,480,054 | 2nd highest; +26,222 MoM |
| 2025-12 | 1,225,597 | YTD +254,457 (+20.8%) |

Kobeissi's $1.48T, +$26B and +$255B (+21%) YTD are VERIFIED at FINRA. The 4.5%-of-GDP and 6.3%-of-M2 ratios were not verified.

## 3b. Post-open cash read (09:53 ET)

`gamma_flip.py --both` 09:53 ET (Cboe chain 3,421 / 7,232 contracts; spot input 7,696.94, a delayed Cboe quote; output saved `gamma_both_postopen.txt`). fetch.py SPX 7,680.71 (−0.99%) at 09:52:58 ET, VIX 17.80 (+6.71%), ESZ26 7,730.50.

| Horizon | Flip | Net GEX per 1% | Regime | Put wall | Call wall |
|---|---:|---:|---|---|---|
| 14d | ~7,745 | −$29.0B | NEGATIVE | 7,750 near-tie → band 7,650–7,750 | 7,800 clean |
| 35d | ~7,750 | −$39.3B | NEGATIVE | 7,750 near-tie → band 7,700–7,750 | 8,000 clean |
| Cross-horizon | band 7,745–7,750 | — | NEGATIVE both | PUBLISH 7,750 (as bands) | WITHHOLD |

Cushion at SPX 7,680.71: **−64 pts vs 7,745, −69 pts vs 7,750.** The pre-open implied ~7,684 matched the cash tape within ~4 pts. The put wall is TESTED (below the strike and below the 35d band floor, inside the 14d band); a break at both horizons would be a cash close under ~7,650.
