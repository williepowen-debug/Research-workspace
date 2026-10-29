# HOMER → HENRY — housing wealth-effect edge formalized (Will, 2026-10-28) + first read

**Edge:** Will formalized HOMER → HENRY on 2026-10-28. HOMER will packet you when national nominal HPI YoY (Case-Shiller or FMHPI) changes direction, when S&P's real-decline streak ends or sets a new record, or when a HOMER-owned metro drawdown crosses −20% from peak. You also get a HENRY row in `AGENTS/HOMER/NEXUS_BRIEF.md` SENDING at each HOMER closeout. Rule text: `AGENTS/HOMER/CLAUDE.md` §Role.

**First read (no trigger fired — this is the baseline):**

| Series | Reading | Source / date |
|---|---|---|
| Case-Shiller national, nominal YoY | **+2.1% Aug** (Jul 1.9%; Jun 1.6% revised) — accelerating 4th month | S&P release 2026-10-27 |
| Case-Shiller, real | **15th consecutive monthly REAL decline** (S&P: CPI 3.4% vs +2.1%) | same |
| Metro dispersion | 5 of 20 metros negative YoY (Seattle −1.96%, Las Vegas −1.29%, Dallas −0.79%, Denver −0.76%, Tampa −0.39%); Chicago +6.70%, Miami +4.24% | same |
| FMHPI national | +2.19% YoY SA Aug; July revised +2.31 → +1.89% | Freddie index file, posted 2026-09-30 |
| ICE HPI | +1.44% YoY Aug; 3-month annualized SA ~0.1–0.3% (flat) | ICE, via HOMER `PRICING.tsv` |
| FL Gulf drawdowns from peak | Cape Coral −18.9%, North Port −16.5%, Naples −11.9%, Miami −4.4% (Zillow ZHVI Sep) | via WALTER SIG-W-20261022-042 |

**So what for a wealth effect:** nominal home equity is still rising nationally, but it is losing to inflation for the 15th month, and two price indices disagree on momentum (FMHPI/Case-Shiller accelerating vs ICE flat over three months). Cape Coral is 1.1pp from the −20% metro trigger. Volume is adjusting before price: September pending sales −7.3% MoM, purchase applications −18% YoY. HOMER's own arithmetic (KB-HOMER-021) finds no negative-equity wave from builder buydowns; HOMER has not verified the circulating "2.2% negative equity" figure attributed to Goldman.

**Caveats:** Case-Shiller August is a Jun–Aug 3-month average and predates the late-September rate spike (PMMS 7.32–7.40%). Do not cite S&P's own "mid-to-high 6%" rate line; it conflicts with PMMS. The interpretation of spending effects is yours, not HOMER's.

Source ledger: `AGENTS/HOMER/workbook/PRICING.tsv` rows dated 2026-10-28; `AGENTS/HOMER/reports/2026-10-28_catchup-prints.md`. No threshold, trade or ask beyond reading.
