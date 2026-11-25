# HOMER look, second pass at the source documents — NEXUS, Will 2026-11-25 15:24 ET ("yes go deeper"); written 2026-11-25T15:27:59-05:00

**Read at issuer:** ICE Mortgage Monitor November 2026 PDF (mortgagetech.ice.com/publicdocs/mortgage/ICE_Mortgage_Monitor_Nov_2026.pdf; pp. 3–6, 16, 19) · Q3-2026 10-Qs: Fannie 0000310522-26-000089, Freddie 0001026214-26-000063, MGIC 0000876437-26-000033, Essent 0001448893-26-000032, NMI 0001547903-26-000045, Radian 0001193125-26-451985, Enact 0001823529-26-000242 (targeted sections, not whole). Not read: Arch; insurer calls; Trepp. Examine-and-report; no letter, Conf, root or threshold moved.

## 0. Correction to my 15:20 ET work (RECORD.md finding 1; HOMER and TERRY packets; chat)
**Withdrawn as evidence of a default shift:** Fannie single-family provision $694M vs $226M. The 10-Q puts higher actual and projected interest rates first; the nine-month provision is FLAT ($1,023M vs $1,030M) and Freddie booked a nine-month $0.5B benefit (model change). The default-shift finding rests on ICE, GSE delinquency rates and insurer counts below.

## 1. The default shift: confirmed at source, small, concentrated in recent loans
| Evidence | Figure |
|---|---|
| ICE Sept new 90-day defaults YoY | all −2%, FHA −14%, GSE +17%, VA +14%; GSE cure rate 10.2%, VA 5.0%. National serious rate 1.04% vs 1.06% Sept average 2017–19 |
| Fannie 9-month additions to seriously delinquent loans | 148,909 vs 135,778, +9.7%; cured or back under 90 days 64,369 vs 47,761 (+35%); liquidations and sales 22,690 vs 32,986 (−31%); workouts −6% |
| Fannie serious rate | 0.62% vs 0.54%; MI-covered 1.36% vs 1.16%; over 100% loan-to-value 4.39% vs 3.46%; Florida 0.91% (0.81), Texas 0.78% (0.68) |
| Freddie serious rate | 0.61% vs 0.57%, "primarily" 2022–2024 loans; MI-covered 1.29% vs 1.19% at 12/31 |
| Five mortgage insurers, Q3 new notices | 58,427 vs 52,844, **+10.6%**: MGIC +6.1, Radian +9.4, Enact +10.8, Essent +16.2, NMI +16.4. Loans in default 110,569 vs 98,624, +12.1% |
| Seasoning test (MGIC, by policy year) | 2023 and later: 3,908 vs 2,246; 2022 and earlier: 10,504 vs 11,336, **−7.3%**. All of MGIC's rise is newer loans (more insured, aging) |
| Seasoning test (rates, not counts) | Essent default rate 2.75% vs 2.29%; NMI 1.23% vs 1.05%. NMI loss ratio to date by book year: 2021 3.4%, 2022 17.8%, 2023 17.3%, 2024 16.7% |
| Loss absorption | MGIC loss ratio 10.0% vs 4.5%; Enact 20% vs 15%; claim assumption on new notices 7.5% unchanged at MGIC and Radian; paid claims MGIC +37%, Radian +43%, Essent +67%, NMI +132% (93 → 216). Capital over the GSE requirement: MGIC $5.8B available, $2.8B over (~193%), Essent 177%, NMI $3.77B vs $2.18B (173%), Enact 158%; Radian not read |
| Cushion thinning | ICE: 1.1M (2%) underwater, largest Q3 share since 2018; 8.4% under 10% equity, highest since 2017; loans since 2022 underwater: VA 19%, FHA 13%, conventional 1.2%. ICE HPI +1.0% Oct |

**Read:** earnings drag, not capital event. Reserve releases from cures are shrinking (MGIC prior-year development $22M vs $32M, Enact $37M vs $45M) and both rest on home-price gains. Counterevidence: cures rising at Fannie, conventional underwater 1.2%, seasoning.

## 2. Apartments: the strongest leg, and the GSE book is the cleanest read
| Fannie multifamily | Q3-26 | Q3-25 | 9M-26 | 9M-25 |
|---|---|---|---|---|
| Provision | $446M | $69M | $879M | $278M |
| Realized credit losses (before loss sharing) | $223M | $161M | $692M | $373M |
| Net of loss sharing | $144M | $101M | $510M | $248M |
| Foreclosed-property expense | $103M | $19M | $227M | $109M |
| Write-offs | $160M | $167M | $604M | $350M |
| Severity at write-off | 11.8% | 22.2% | 16.1% | 26.0% |

REO 226 properties / $1.7B vs 181 / $1.0B [12/31]. Forecast cut: 2026 property values −1.2% (was +3.1%), income growth +0.2% (was +1.9%). Substandard $28.3B vs $27.1B (5.3% vs 5.2%), 2022 loans 10.5% substandard, 2023 8.1%, 2024 5.4%. Headline delinquency FELL 0.74% → 0.62% on a modification and foreclosures: the headline is the wrong meter. Offsets: criticized flat at 6%, Q3 write-offs flat on the year and severity lower; loss-sharing partners take about a quarter ($182M of $692M). Loans not covering debt service: 5% of the book (4%), 6.54% of them seriously delinquent (5.88%). Freddie: substandard held apartment loans $2,842M vs $1,468M [12/31] on a growing book (1.5% vs 1.0%); 0.58% vs 0.44% [12/31], "primarily" elevated rates; subordination bucket 0.80% vs 0.56%. Fannie's drivers include property income and values, so this is not only a rate story.
**HOMER does not hold:** REO count, realized losses, forecast cut, substandard by year (searched MULTIFAMILY.tsv and STATUS). It holds the provision (row 94).

## 3. Track record
| Call | Direction | Odds | Outcome |
|---|---|---|---|
| HOM-01 prices roll over | worse prices | 60% | missed |
| HOM-02 FHA delinquency ≥ 12% | worse credit | 65% | missed (loans moved into foreclosure) |
| HOM-03 existing sales < 3.90M | worse demand | 60% | hit (3.75M) |
| HOM-04 builder price cutters > 45% | worse demand | 30% | hit (46%) |

Brier 0.358 (fleet 0.228 on n = 220, PROME report 11/05, different calls; always-50% = 0.250). n = 4 proves nothing; the PATTERN matches the read: demand calls hit, price and credit-stock calls missed. Two headline calls failed because the instrument excluded the next stage (HOM-02, HOMER's own LESSONS §55). Seven open; HOM-05 and HOM-07 now lean toward easing credit, HOM-09 (88%) toward weaker demand.

## NEXUS view
Three clocks: demand breaking now; apartment losses realized now, at the GSEs, bond holders and bridge lenders; mainstream mortgages early and small, in 2022–24 loans. Unscored: insurers' Q4 new notices up on the year (about 85%: rising in all five in Q3 and Q4 seasonally heavier); a capital problem at any of the five by their Q4 reports, under 2%. Both are judgment. Would change it: newer-book default rates rising in a 2021-and-earlier book too, or home prices negative nationally.

## Outside check read (Will 15:58 ET, HOMER housing report check, revised about 16:00 ET); read 2026-11-25T15:59:05-05:00
Agrees with findings 1, 2, 4, 6, 8 and adopts the −3bp flows read. **Overtaken:** (a) its §6 cites Fannie SF provision $694M vs $226M as in HOMER's brief; HOMER withdrew it as default evidence at 15:30 ET (c070c5376f, 842b154462), after its base d2910fbf46; (b) its base predates this file (f4d16dca2c); (c) ICE October-2025 First Look dated 11/26 there; HOMER holds a Mondo Visione copy dated Tue 11/25/2025, the 11/26 being a blog post, so "normal timing" needs that limit; (d) its Blackjack question was closed by HOMER 14:50 ET (not in October's count, DERIVED). Paste-block steps 1–3, 6 done at HOMER's files; 4, 5, 7 accepted by HOMER as report wording (PROME packet 14:35 ET). **HOM-09 re-run:** 88% reproduces (z 1.30, t7 0.883); at an error of 0.10M (the HOM-03 miss, a different n = 1 ratio that ran high, which helps this call) it is about 78%. Odds frozen; context only. Not an owner figure.

**Precision from HOMER's re-read (11/25 16:1x ET):** in §0, $226M is Q2-2026 (year-ago quarter $269M); 'rates first' is the Q3 ordering, for the nine months Fannie lists rates third. **§ NEXUS view corrected:** apartment losses also fall on insured banks (net charge-offs ex United Fidelity $784M, +21%).
