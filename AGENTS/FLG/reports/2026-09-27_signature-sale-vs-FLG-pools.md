# WQ-309 — FLG pools against the FDIC's 2023 Signature Bank loan sale (2026-09-27, Sun PM)

**Commissioned by:** PROME (WQ-309, approved by Will 17:44 ET; scope `PROME/plans/2026-09-27_signature-sale-relevance-SCOPE.md`, 6102d9336). **Maps onto:** CREED `AGENTS/CREED/analysis/2026-09-27_signature-bank-2023-sale-economics.md` (515d18483). **Author:** FLG.
**Bounds (Will, verbatim):** *"'No usable loss-rate comparison' is a valid result … No model or loss-rate changes under this authorization."* No discount is converted into a loss rate here. No bridge rate, score, threshold, tool or trade is changed.

---

## Answer first

1. **No FLG pool can take a loss rate from the Signature sale.** CREED's reading holds at the primary (FLG re-read pr23105 and pr23107 on 9/27). The sale was a set of joint ventures. Partners bought 5–20% equity stakes, the FDIC kept 80–95%, and on one venture the FDIC also lent 50% of the venture's value. The prices are levered minority-equity checks, not prices for loans.
2. **Per-pool grades:** the three NYC rent-regulated pools are **PARTIAL (directional only)**. The four "other" multifamily and CRE pools **DO NOT INFORM**.
3. **The scope's expectation holds on collateral resemblance but inverts on the only number that exists.** The rent-regulated pools resemble the rent-stabilized ventures best, and those ventures yield **no computable value**. The one imputable figure (≈71% of book, market-rate venture) relates to market-rate multifamily, office and retail. On FLG's side, that is an undisclosed NYC slice of the "other" multifamily pools and New York office and retail CRE, the pools the expectation ranked **least** relevant. Even there it does not inform, for the reasons in §B.
4. **An FLG-side link CREED could not see:** FLG bought part of Signature itself in March 2023, taking **$1,680M of CRE loans at fair value and no multifamily loans** (10-K FY2024, Signature purchase-price allocation). FLG's **multifamily** pools therefore contain no disclosed Signature-originated loans. FLG's **CRE** pools may. Their remaining balance and grade today are not disclosed.

---

## §A. OBSERVED

### A1. Signature side (CREED primaries; FLG spot-checked two)
| Fact | Source | FLG check |
|---|---|---|
| Market-rate venture: ~$16.8B "office, retail and market-rate multifamily"; "does not hold any loans collateralized by rent-stabilized or rent-controlled multifamily properties"; 20% for $1.2B; FDIC financing "equal to 50 percent of the Venture's value" ≈ $6B purchase-money note | FDIC pr23105, 2023-12-14 | ✅ re-read 9/27, verbatim |
| Rent-stabilized venture (Santander): ~$9.0B "rent-stabilized or rent-controlled"; 20% for $1.1B; FDIC keeps 80%; **no financing mentioned**; no loan count, no performing/non-performing split | FDIC pr23107, 2023-12-20 | ✅ re-read 9/27 |
| Rent-stabilized ventures (CPC): $5.8B; 5% for $129M + $42M; FDIC 95% | FDIC pr23106, 2023-12-15 | CREED only (MIRROR to FLG) |
| Implied market-rate venture value ≈ $12B on $16.8B ≈ 71% of book | CREED arithmetic on pr23105 | Reproduces: $1.2B / 20% = $6.0B equity + ~$6B note ≈ $12B |

### A2. FLG side — what FLG's filings disclose about each pool (10-Q Q2-26 unless noted)
| Disclosure | Figure | Source |
|---|---|---|
| Pool totals tie to the 10-Q grade table | MF nonaccrual **$2,132M** = $1,737M RR + $395M other · MF special mention + substandard **$6,939M** = $2,665M + $4,274M · MF pass **$17,860M** = $4,089M + $13,771M | 10-Q vintage/grade table; REGINALD bridge b93e3ac58 |
| MF **vintage** by grade | Nonaccrual: **86% pre-2022**, 13% 2022, 1% 2023 · SM + SS: 65% pre-2022, 33% 2022 · **Not split RR vs other** | 10-Q vintage/grade table |
| NYC RR criticized + classified ($4,401M = nonaccrual $1,737M + SM/SS $2,665M) | LTV **78%**, amortizing DSCR **1.01×**, occupancy 97%, **49%** reset within 18 months | Deck, NYC MF Portfolio Details, 6/30/26 |
| NYC RR pass ($4,089M) | LTV 61%, DSCR 1.51×, 19% reset within 18 months | Deck |
| RR nonaccrual loss already recognised | $351M charged off (16.80% of original $2,088M) + ACL 4.38% ⇒ 20.45% | Deck s16 (KB-FLG-062) |
| "Other" MF geography (all grades, $18.4B) | NYC market-rate or <50% RR **$4,898M** (27%) · NJ $3,314M · PA $2,699M · FL $1,289M · OH $940M · Long Island + other NYS $1,244M · other states $4,057M. **Geography by grade: not disclosed** | 10-Q MF geography table; deck |
| CRE by property type (all grades, $8,244M) | Industrial **40%** · office 22% · retail 16% · other 22%; New York **42%**. **Property type by grade: not disclosed** | 10-Q CRE tables |
| CRE nonaccrual $471M, vintage | 56% pre-2022, 19% 2022, 23% revolving | 10-Q vintage/grade table |
| **Signature loans FLG itself acquired (3/20/2023)** | Loans HFI at fair value: C&I $9,888M · **CRE $1,680M** · consumer $173M. **No multifamily line** | 10-K FY2024, Signature transaction note (acc 0000910073-25-000038) |

---

## §B. Per-pool grade (one row per pool)

Grades use PROME's vocabulary. **"Loss rate" is DOES NOT INFORM for all seven**, since no rate exists (CREED §0). The grade column below is about **directional/collateral** relevance, which is the ceiling on any future use.

| FLG pool (6/30/26) | CREED six-dimension grade | What FLG's filings add | **FLG grade** | Reason / adjustment that would be needed |
|---|---|---|---|---|
| **MF nonaccrual, NYC ≥50% RR — $1,737M** | PARTIAL | 100% nonaccrual; mostly pre-2022 vintage (MF-wide); 20.45% loss already recognised; LTV 78% / DSCR 1.01× on the combined RR criticized+classified set | **PARTIAL — directional only** | Best type + market match (rent-stabilized ventures). But Signature's performing/non-performing split is undisclosed, so the match to a **100%-nonaccrual** pool fails on the dimension that matters most. Priced Dec-2023, before the June-2026 freeze. The ventures' leverage is undisclosed, so no value can be computed. **What it would take:** the FDIC's realised recoveries on the rent-stabilized ventures, split by performing status. Even then FLG would need to net its 20.45% prior write-down to compare |
| **MF criticized, NYC RR — $2,665M** | PARTIAL | Accruing but criticized; DSCR 1.01× / 49% resetting within 18 months (combined set) | **PARTIAL — directional only** | Same as above. "Criticized-accruing" cannot be isolated in the Signature pool. Direction only: a Dec-2023 bid for 20% of $9.0B of rent-stabilized loans (with the FDIC keeping 80%) says the class had equity value to a bank buyer **before** the freeze. It says nothing about severity |
| **MF pass, NYC RR — $4,089M** | PARTIAL | DSCR 1.51×, LTV 61% | **PARTIAL — directional only** | Plausibly the closest on performing status, if Signature's book was mostly performing. That is **unknown**, so it cannot be claimed. Weak positive evidence that a performing rent-stabilized book is bid-able. Not a mark |
| **MF nonaccrual, other — $395M** | DOES NOT INFORM | Contains an **undisclosed** share of NYC market-rate / <50%-RR loans (27% of all "other" MF is NYC) | **DOES NOT INFORM** | A NYC market-rate slice matches the market-rate venture on type + market. But that venture's only number (≈71%) is a **levered strike blended with office and retail**. The FDIC's 50% financing plausibly **raised** the equity bid, so the ≈71% likely overstates a clearing value (direction is an assumption, S2). FLG does not disclose the pool's NYC share. Non-NYC loans (NJ/PA/FL/OH) have no Signature analogue |
| **MF criticized, other — $4,274M** | DOES NOT INFORM | Same composition limits as above | **DOES NOT INFORM** | Same as above. "<50% RR" buildings contain some regulated units, so this pool straddles both venture types and matches neither cleanly |
| **CRE nonaccrual — $471M** | DOES NOT INFORM | 40% industrial / 22% office / 16% retail across **all** CRE; NY 42%; type by grade not disclosed. **May contain Signature-originated CRE**, bought at fair value 3/2023 | **DOES NOT INFORM** | Office/retail in NY matches the market-rate venture on type + market for an undisclosed slice, with the same levered-and-blended objection. Industrial (the largest share) has no analogue. The direct link, FLG's own Signature-acquired CRE, was **marked to fair value at acquisition**, so any loss on it is measured from that mark, not from par. Its remaining balance and grade are not disclosed |
| **CRE criticized — $1,367M** | DOES NOT INFORM | Same as above | **DOES NOT INFORM** | Same as above |

---

## §C. SCENARIO ASSUMPTIONS
- **S1.** Signature loans were bank-originated first liens (CREED: "presumed, not confirmed at primary"). FLG's pools are first-lien bank loans. The lien dimension is scored "~" on that presumption.
- **S2.** Cheap FDIC seller financing (50% of venture value) raises what a buyer will pay for equity, so the ≈71% implied value **likely overstates** an unfinanced clearing price. This is a direction-only assumption. It is not quantified and not used.
- **S3.** "Rent-stabilized or rent-controlled" (FDIC) and "≥50% of units rent-regulated" (FLG) overlap closely but are not the same cut (CREED U5). The PARTIAL grades assume the overlap is large.

## §D. UNKNOWNS (exactly what is missing)
1. **FDIC realised recoveries** on the rent-stabilized ventures, 2024–26 (FDIC receivership / DIF reporting). This is the only route to a rate (CREED §C8).
2. **Leverage** on the CPC and Santander ventures (not in pr23106/pr23107).
3. **Signature's performing / non-performing and vintage mix.** Without it, no FLG grade tier (nonaccrual / criticized / pass) can be matched.
4. **FLG side:** geography by grade for "other" MF · property type by grade for CRE · vintage split RR vs other · **remaining balance and grade of the $1,680M Signature-acquired CRE.** None is in the Q2-26 10-Q or deck.
5. **FLG's own disposition pricing.** A closer comparator than Signature would be FLG's own 2026 note sales and discounted payoffs on these same pools. They are not disclosed (KB-FLG-061/066; one 6% anecdote, KB-065).

## §E. Next observation that would change the conclusion
| Observation | Where / when | Direction |
|---|---|---|
| FDIC realised recoveries on the SIG rent-stabilized ventures | FDIC receivership / DIF statements; any FDIC OIG review. Undated | Recoveries well below contributed value → **supports** (never sets) a heavier stress on the three NYC RR pools. At or near value → supports the par-payoff reading and a lighter stress |
| FLG discloses the loss on its own RR dispositions (sale price vs carrying value) | Q3-26 10-Q (~11/9) or call (~10/23) | This would **supersede** Signature as the comparator for the RR pools: same lender, same book, 2026 regime |
| FLG discloses the remaining Signature-acquired CRE by grade | 10-K FY2026 (~3/2027) | Would upgrade the CRE rows from DOES NOT INFORM to a **direct**, same-loan link (from the fair-value mark, not par) |

— FLG
