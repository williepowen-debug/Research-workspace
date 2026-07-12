# SOFR Deep Dive — level, dispersion, positioning, mechanics
**Run:** Sat 2026-07-11 ~22:45 ET (weekend — every figure is release-vintage-stamped; nothing here is a market-live quote) · **Owner:** LIQUID · **Task:** PROME round-5 (Will-directed) · **No trade recommendations.**
**Primary pulls this session:** NY Fed rates API (SOFR daily + percentiles + volume; EFFR; SRF repo ops) · CFTC TFF via publicreporting.cftc.gov (SOFR-3M, 30 weeks, all trader classes) — both endpoints re-proven from this box tonight.

---

## Leg 1 — The rate itself: is the floor showing ANY strain?

**Verdict: no — plumbing is quiet and EASING.** SOFR is falling away from IORB, the entire rate distribution sits at-or-below the ceiling, volumes are steady, SRF is untouched.

### SOFR daily (NY Fed, pulled 7/11; IORB 3.65 throughout the window)

| Date | SOFR | −IORB | 75th | 99th | 99th−SOFR | Vol ($B) |
|------|------|-------|------|------|-----------|----------|
| 6/15 | 3.69 | **+4bp** | 3.74 | 3.78 | +9 | 3,147 |
| 6/23 | 3.62 | −3 | 3.67 | 3.70 | +8 | 3,105 |
| **6/30 (Q-end)** | **3.68** | **+3** | 3.73 | **3.80** | **+12** | **3,418** |
| 7/1 | 3.66 | +1 | 3.71 | 3.73 | +7 | 3,321 |
| 7/2 | 3.64 | −1 | 3.70 | 3.72 | +8 | 3,208 |
| 7/6 | 3.63 | −2 | 3.68 | 3.71 | +8 | 3,212 |
| 7/7 | 3.62 | −3 | 3.67 | 3.71 | +9 | 3,154 |
| 7/8 | 3.58 | −7 | 3.64 | 3.67 | +9 | 3,158 |
| **7/9 (latest)** | **3.53** | **−12** | 3.57 | **3.65** | +12 | 3,126 |

- **The tape's most striking feature is the 7/7→7/9 slide: SOFR −9bp in 3 sessions (3.62→3.53) against a static IORB** — the softest print of the window. On 7/9 even the **99th percentile (3.65) sits exactly AT IORB**: the entire repo distribution is at or below the ceiling-system floor rate. That is the opposite of ceiling pressure. *(Labeled inference on cause: reserves rebounded +$132B w/w to $3.099T [H.4.1 as-of 7/8], RRP is drained ~$5.8B, post-Q-end collateral/cash normalization — cash abundance pressing repo down. Not verified to a single driver.)*
- **Quarter-end 6/30: orderly, one-day, mechanical.** +3bp over IORB with a 3.80 99th tail (+15 over IORB), fully normalized by 7/1-7/2 — textbook KB-LIQ-051 pattern (its 2nd instance, previously logged). The 6/15 +4bp print = the June corporate-tax-date analog, also one-day.
- **Dispersion calm:** 75th−SOFR steady at +4-5bp all window; 99th−SOFR +7 to +12bp vs my ≥20bp tail-blowout alert line. No trend.
- **Volumes:** $3.0-3.4T/day, Q-end peak $3,418B — deep and steady, no seizure signature.
- **EFFR pinned:** 3.62-3.63 [7/2-7/9], vol ~$117-131B — unsecured leg equally quiet.
- **SRF: effectively zero.** 7/8-7/10: $0 submitted/accepted both daily ops; 7/1, 7/6, 7/7 morning ops show $1-3M accepts — de-minimis/SVE-scale test trades, not usage (offering rate 3.75 = ceiling intact, untested).
- **Cross-check vs my own thresholds:** SOFR 3.53 < 3.70 trigger · SOFR-IORB −12bp (needs ≥0 ×3 non-Q-end days) · SOFR75−IORB −8bp · SOFR99−SOFR +12 < 20. **All quiet. Funding is NOT the stressed channel** — which sharpens the two-channel rates read: 10Y holds ≥4.50 on term-premium/inflation while the funding floor SOFTENS. Duration and funding have decoupled, in the benign direction for plumbing.

## Leg 2 — Decomposing the record short (CFTC TFF, SOFR-3M, as-of Tue 7/7, released Fri 7/10)

### The two-sided picture [7/7]

| Trader class | Long | Short | NET |
|--------------|------|-------|-----|
| Leveraged funds | 1,046,636 | 3,919,042 | **−2,872,406** |
| Asset managers | 1,202,379 | 1,703,446 | **−501,067 (same side as lev!)** |
| **Dealer/intermediary** | — | — | **+3,317,752 (the mirror)** |
| Open interest | | | 13,110,035 |

- **The headline "$700B short" is really a lev+AM −3.37M net short warehoused almost 1:1 by dealer books +3.32M.** Dealer net long grew in lockstep with the short all year (+183K [12/30/25] → +3.47M [6/30]). Asset managers — usually the other side of leveraged funds in a directional trade — have been persistently net-short SINCE 5/5, the same window the lev short accelerated.
- **Build path (lev net):** −306K [12/23/25] → −667K [1/6] → ~−0.9M plateau (Jan-Apr) → **May-June acceleration:** −1.34M [5/5] → −1.72M [5/26] → −2.10M [6/2] → −2.45M [6/9] → −2.79M [6/23] → **−2,943,898 [6/30] = the record** → −2,872,406 [7/7]. That is ~9.4x since late December and ~2.2x since early May. **The record is RECENT (6/30), not a plateau, and the +71,492 w/w [7/7] is the first meaningful cover since mid-June.**
- **Record in contracts AND notional: yes.** Notional convention matters: contract value = $2,500 × IMM price (~96.4 at ~3.6% rates) ≈ **$241K/contract** → net ≈ **−$692B [7/7] / −$710B [6/30]**; the cruder $250K/contract shorthand gives −$718B/−$736B. Canonical statement: **≈ −$700B, band $690-720B by convention.** (Corrects my round-4 single-convention figure.) Press corroboration: Saxo's Hansen called the 6/23 week "a fresh record… more than USD 700 billion," and characterizes the data series' ~6-year history as never more extreme.
- **Front vs deferred strip: UNKNOWABLE from free data.** CFTC TFF aggregates all SR3 expiries into one market row; per-expiry positioning by trader class is not published anywhere free. CME publishes OI by expiry but not who holds it. **Labeled uncertainty — do not infer strip placement.**
- **Breadth + concentration:** 185 distinct lev-fund short traders [7/7] — the window HIGH (155-188 range since Dec) = broad participation, not one whale; top-4 net short concentration 12.1% of OI (~1.59M contracts) — meaningful but not dominant. Companions, same direction: SOFR-1M lev net −283,695 [7/7]; 10Y ERIS SOFR swap futures lev net −135,113 [7/7] ≈ −$13.5B notional.

## Leg 3 — What IS this short, mechanically? (the load-bearing question)

**Honest answer: the directional/RV split is not knowable from free data — CFTC does not tag strategy. But the observable structure supports "substantially directional, dealer-warehoused," with a real RV component of unknown size:**

| Evidence | Points toward |
|----------|---------------|
| Build timing tracks the hike-repricing exactly (May-Jun acceleration; Fed-hike-2026 odds crossed >50% [ORACLE 7/9]; Hansen attributes the build to "hawkish shift in Fed expectations post-FOMC") | **Directional** (higher-for-longer/no-cuts view) |
| Asset managers net-short on the SAME side since 5/5 — real money doesn't take the RV leg; same-side positioning reads as shared rate-view/hedging, not two-sided RV | **Directional/hedging** |
| 185 short traders = broad participation (RV concentration would look narrower) | **Directional** |
| Dealer +3.32M mirror long = classic intermediation/warehousing of client hedging flow; invoice-spread and swap-spread structures short futures vs received-fixed | **RV/structural component real** |
| Record volume in SOFR-vs-fed-funds futures spread trading (briefs.co) = active STIR RV desks in the same complex | **RV component real** |
| OI only +5% (12.5M→13.1M) while net short tripled = much of the build was position rotation, not fresh gross risk | Mixed — consistent with view-flipping |

**Implication for the squeeze thesis (stated, not recommended):** to the extent the short is directional — and the balance of observable evidence says substantially so — a SOFT CPI 7/14 (cut-repricing) puts −$700B of notional offside and the cover bid is in the FRONT-END/STIR complex. Transmission to the 10Y is indirect (a front-end-led steepener impulse, not a direct 10Y bid) — the "forced cover caps the 10Y" version over-claims; the defensible claim is *front-end rate vol amplification on a soft print* (and symmetric: a hot print rewards the short and removes the squeeze). This is now encoded as a caveat in the nexus watch. **The discriminator to watch at any cover: swap spreads / SOFR-FF spread stable while shorts cover = directional squeeze confirmed; those spreads moving with the cover = RV unwind (less systemic).** CFTC as-of 7/14 (released Fri 7/17) is the post-CPI positioning read.

## Leg 4 — Actions taken back into my artifacts

1. **`workbook/DEALER_POSITIONING_NEXUS_WATCH.md` UPDATED:** notional convention corrected (~$241K/contract, $690-720B band); dealer-mirror + AM-same-side structure added; **basis-vs-directional caveat added to the fire protocol** (read any W1 cover against concurrent swap-spread/SOFR-FF-spread behavior before calling it systemic); W1 record baseline anchored to −2,943,898 [6/30]; >300K one-week cover threshold validated as ~4x the largest cover in the 30-week history (largest weekly build −379K [6/2], largest cover +71K [7/7]).
2. **KB-LIQ-076 leg-(a) re-word: YES, done** (in the watch file + KB note appended). Note: there is deliberately **no PROME/GATES.tsv row** for this watch — it is a monitoring conjunction (write-up on fire), not an action gate; if PROME wants it promoted to the fire-ledger, that's PROME's call.
3. **KB-LIQ-078 registered** (decomposition + quiet-floor findings, this file as source).

**Sources:** NY Fed markets API (SOFR/EFFR/SRF, pulled 2026-07-11); CFTC publicreporting.cftc.gov TFF `gpe5-46if` (pulled 2026-07-11, data as-of 2026-07-07); FRED H.4.1 vintages as cited; [Ole S. Hansen/Saxo on X (6/23-week record)](https://x.com/Ole_S_Hansen/status/2071158513351471514); [CreAnalyst squeeze-thesis piece](https://www.creanalyst.com/insights/record-sofr-short-positioning-could-spark-a-rate-squeeze); [briefs.co SOFR-FF spread record volume](https://www.briefs.co/news/t-bill-supply-disagreement-sparks-record-trading-in-sofr-fed-funds-futures-spread/); ORACLE Fed-odds packet 7/9.
