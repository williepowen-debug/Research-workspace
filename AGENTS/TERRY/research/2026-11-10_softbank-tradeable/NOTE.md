# SoftBank Q2 loss: is there a trade? TERRY's one bounded pass

**Stamp:** 2026-11-10 18:05 EST (from `date`). TERRY, Claude Code, `claude-opus-5-5`, desktop. Asked by PROME prome-07 at 18:03 ET on Will's words: 17:18 ET "alright lets have you direct and orchestrate the investigation into softbank..." and 18:03 ET "yes we should always be looking to see if something is tradeable". **No order by the desk. $0. No threshold, gate, band or card term changed.**

**Read at the artifacts:** PROME `PROME/themes/ellison/reports/2026-11-10_softbank-loss-investigation.md`; SAM `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_LOSS_INVESTIGATION.md` (§ leverage roll, § 6 Tokyo) and `PROME/inbox/processed/2026-11-10_from-SAM_red-s62b-leverage-check.md`; LIQUID `PROME/inbox/processed/2026-11-10_from-LIQUID_softbank-credit-leg.md`. RED and VULCAN were taken through PROME's findings table and challenge verdicts. I did not read their full reports in this pass, and their figures are not re-derived. The thesis is the owners'; TERRY grades only the expression.

## Verdict: NO CARD

There is no listed, defined-risk instrument that carries SoftBank's stress instead of something larger. Each candidate either has no options, or is mostly a bet on Nvidia, semiconductors and rates, or duplicates the HYG and ORCL cards already on the book.

## Candidates, in figures

| Candidate | What it actually carries | Live read (US options are post-close quotes, pulled 18:04 ET, screening marks) | Verdict |
|---|---|---|---|
| **SFTBY** (US ADR) | SoftBank equity directly | **No listed options: `chain_fetch.py SFTBY` returns 0 expiries.** $11.27, −4.00% [11/10], −43.65% over 30 days | No defined-risk expression. Shorting the shares carries unlimited loss (Hard Boundary 7, Non-Negotiable #2) → **no card** |
| **9984.T** | SoftBank equity | Tokyo listing; this desk has no chain and no route to OSE options | Not reachable → **no card** |
| **ARM** puts | **Arm is SoftBank's collateral, not where its stress shows up.** The Arm margin loan is non-recourse to SBG (SAM, fr 14/12) and **no margin-call level is disclosed** (LIQUID § 5). The 25% line is SoftBank's own policy ceiling, not a lender's trigger, and a breach leads to asset monetisation; nothing read names Arm shares as what gets sold. On the day, Arm moved as a semiconductor stock: ARM −2.58% vs NVDA −5.47% [11/10] | $181.49; −37.34% in 30 days; 30-day low $166.72. Dec-18 puts **IV 67–79%**. 170/155P outer **$6.10 = $610/lot > $500 cap**; 165/150P outer $4.65 = $465; 160/145P outer **$4.15 = $415**, BE $155.85, 15-wide, about 2.6:1 | An Arm put is long the semiconductor/Nvidia sell-off and long rate shocks (a high-multiple stock on a hawkish-Fed day), with SoftBank a small share of the payoff. It also pays 72% IV after a 37% fall → **no card** |
| **Arm < $166 / < $159 as a trigger** (SAM/RED dated lines) | SoftBank's ABB-inclusive 25% case | At 72% IV, one daily standard deviation = 4.5%. $166 is −8.9% (log) from $181.49 = about 2 days' noise. **Driftless odds of touching $166 by 12/18 about 71%, of closing below it about 35%; $159: touch about 58%** (TERRY arithmetic, Black-Scholes, 27 trading days, no drift) | Noise is more likely than not to reach the line, so a fire carries little information. Construction rule #15 also applies: a gate opened by a price fall feels like confirmation and isn't. **Not a usable trigger for a card on Arm itself** |
| **Cohort** (IREN, NBIS, CRWV, NVDA) | The AI-capex cycle | 11/10: IREN −7.85%, NBIS −5.27%, CRWV −0.51%, NVDA −5.47%; owners attribute no cause (PROME finding 15) | RED: "specific in who strains first, not in cause". A cohort short is a different thesis with no owner card → **no card** |
| **Equipment makers** (GE Vernova, Siemens Energy) | SB7's cut orders | **Suppliers unnamed**; equipment not stated to be turbines (VULCAN KB-419); GE Vernova "no negative or positive impact" (Reuters, secondary) | No named counterparty → **no card**; Siemens Energy results ~11/11 is the next observation (VULCAN) |
| **SoftBank credit** (CDS, USD bonds) | SoftBank default risk | 5Y CDS 497 [11/9, DTCC US-nexus sample, ±10 bp, LIQUID]; not tradeable from Will's accounts; TRACE unreachable | Not tradeable → **no card** |

## Overlap with the open book

- **HYG ×5 hedge (WQ-615 A + WQ-663 B, FIRED, UNFILLED)** is already the book's position on AI-funding stress reaching broad credit. **HYG ×4 (WQ-513 A, NOT FIRED)** is the second one, and the pair is capped at $711.70 with Will's word. Any SoftBank-keyed credit card would load a third position on the same factor. LIQUID: HYG −0.43% [11/10]; the 11/10 HY cell grades 11/12 (11/11 bond holiday). Whether HYG holds SoftBank USD bonds, and at what weight, was not read.
- **ORCL Dec-18 115/100P (NOT FIRED)** is the book's single-name AI-funding card. LIQUID: Oracle 5Y 305 → 301.5 [11/6 → 11/9] while SoftBank widened +27, so credit has not passed from SoftBank to Oracle. PROME/VULCAN: Oracle has no role at PORTS-Pike. **The ORCL card's T1 (CDS ≥ 350) is already the observation that would mean SoftBank's stress has reached Oracle.** No change.

## What would change the answer (dated observations; owner in brackets)

| Observation | Why it matters to construction | What TERRY would do |
|---|---|---|
| DTCC 11/10 CDS **> 513 with Oracle and CoreWeave flat** (LIQUID, about 20:15 ET tonight) | SoftBank-specific credit stress confirmed | Still no SoftBank instrument. It feeds the HYG ×4/×5 and ORCL watch; no new card |
| 9984.T **closes below ¥3,400 on volume above 64.8M** (SAM, Tokyo 19:00–01:30 ET) | Equity market rejects the "mostly paper" read | Same: no carrier. Re-check whether SFTBY has listed options; if it does, price a put spread |
| **TDnet: an Arm block sale, a new Arm-backed facility or a collar on Arm** (SAM) | Makes Arm a carrier through a dated supply overhang | Build an Arm put spread only before or at the filing. ⚠️ A filing-triggered entry buys after the overnight gap, the wrong side of the event, unless a measured block-sale envelope says the drift continues (construction rule #18's measure-first clause). Not measured today |
| **Credit stress passes on: Oracle 5Y ≥ 350** (LIQUID) or **HY > 350 ×3** (REGINALD) | Stress reaches a name the book already trades | Existing cards fire on their own letters. No new card |
| An OpenAI round priced under SoftBank's mark (VULCAN) | Cuts both the SoftBank and cohort reads | Cohort question for VULCAN/NEXUS; TERRY builds only on an owner's dated view |

## Known-unknowns that bind construction

1. Margin-call levels on the Arm, SoftBank Corp and SVF2 OpenAI-share loans, and the T-Mobile collar strikes (LIQUID § 5, SAM). Without them, no forced-selling level exists to trade against.
2. Which holding SoftBank would monetise first above 25%. Not stated anywhere read.
3. After-results credit and the Tokyo session (both tonight, unread at this stamp).
