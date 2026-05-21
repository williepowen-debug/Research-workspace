# AUCTION_HISTORY — README (Prome-spawned, 2026-05-20)

## PROVENANCE

- **Author:** Prome-spawned one-shot research sub-agent (Claude Code), 2026-05-20 PM ET.
- **Why this exists:** BOND has been reading auction results in N=1 anecdote mode (5/20 20Y BTC 2.55 "vs Apr 22's 2.68"). This artifact gives BOND an empirical distribution layer so future commentary can say "BTC X.YY is the Nth percentile of the last 36 months" instead of vibing off the last print.
- **Status:** Background build-out. BOND owns this directory going forward. BOND integrates and commits on next boot. Files are tagged `_prome-spawned` until BOND adopts them (rename / move at BOND's discretion).
- **Source of truth:** US Treasury FiscalData API — the same source BOND already references.

## How to refresh

```
source .venv/bin/activate && python3 AGENTS/BOND/data/refresh_auction_history_prome-spawned.py
```

The script is idempotent; it overwrites the CSV with a fresh pull each run. It paginates defensively and runs in well under a minute.

## Source

- **Endpoint:** `https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query`
- **Filter:** `auction_date:gte:2023-01-01,auction_date:lte:<today>`
- **Scope:** Coupon-bearing Treasuries only (`security_type` in {Note, Bond}). Bills excluded per task scope. Tenors: 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y, including reopenings. TIPS retained and flagged via `is_tips`.
- **Row count as of 2026-05-20:** 364 auctions with completed results (out of 1,475 raw auction records in the date window — the rest are bills or future/announcement-only entries).

## Schema

One row per auction with completed results.

| column | meaning |
|---|---|
| `auction_date` | Date the auction cleared (ISO YYYY-MM-DD). |
| `tenor` | Normalized original tenor: one of {2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y}. |
| `security_type` | Treasury classification: `Note` (2/3/5/7/10Y) or `Bond` (20/30Y). |
| `is_reopening` | `True` if this auction reopened an existing CUSIP. |
| `is_tips` | `True` if inflation-indexed (TIPS). 5Y / 10Y / 30Y TIPS only. |
| `issue_date` | Settlement date. |
| `maturity_date` | Maturity date of the issued security. |
| `cusip` | Treasury CUSIP. |
| `offering_amt` | Announced offering size in dollars. |
| `total_accepted` | Total competitive+noncompetitive accepted (dollars). |
| `high_yield` | Stop-out yield in %. |
| `bid_to_cover_ratio` | Total tendered / total accepted. |
| `primary_dealer_accepted` | Dollars allocated to primary dealers. |
| `direct_bidder_accepted` | Dollars allocated to direct bidders (non-dealer competitive). |
| `indirect_bidder_accepted` | Dollars allocated to indirect bidders (incl. foreign central banks). |
| `soma_accepted` | Fed SOMA allocation in dollars. |
| `dealer_pct` | `primary_dealer_accepted / total_accepted` (fallback: `/ offering_amt`). |
| `direct_pct` | Direct bidder share, same denominator rule. |
| `indirect_pct` | Indirect bidder share, same denominator rule. |

## Known gaps

- **TAIL is NOT included.** Deriving tail requires matching each auction to a WI (when-issued) yield close — generally the FRED constant-maturity series (`DGS2/3/5/7/10/20/30`) snapped at the auction-day pre-results timestamp. WI is not the same as the daily H.15 close, and the timing match is fragile. Per the task brief, omitted rather than guessed. To add this credibly later, BOND should pull FRED H.15 and document the assumed snap convention (e.g., 1pm ET CMT yield) — and note explicitly that this is a proxy for WI, not WI itself.
- **No CMB / Bills.** Out of scope per task.
- **TIPS allocation fields can be sparse** for older reopenings. The `dealer_pct` etc. will be NaN where the underlying allocation column is null.
- **Same-day multi-tenor auctions** (rare) are not deduped — each tenor is its own row, which is correct, but consumers grouping by date should group by `(auction_date, tenor)`.
- **`offering_amt` vs `total_accepted`:** allocation percentages use `total_accepted` as the denominator when present (true allocation base), falling back to `offering_amt` if missing. This matches the Treasury auction-results convention but differs from some vendor calcs that always use `offering_amt`.

## Worked percentile examples (verdict-first)

All examples computed against the full 2023-01-01 → auction-date prior history of the same tenor. Percentile rank = % of prior prints with value <= the current print (lower percentile = weaker on demand-side metrics; lower percentile on BTC / indirect = softer auction).

### 1. 5/20/2026 20Y reopening — "soft but functional" reread

| metric | value | percentile (all prior 20Y, N=40) | trailing-12mo (N=12) |
|---|---|---|---|
| bid_to_cover | **2.55** | **38th** | 33rd |
| dealer_pct | 8.1% | **15th** | — |
| indirect_pct | 58.3% | **12th** | — |

Verdict: BTC was middling (38th pctile, not alarming). But **indirect take at 58.3% was the 12th percentile of all 20Y prints since 2023** — that's the actual weak signal in this auction, not the headline BTC. Dealer take 8.1% was also bottom-quintile, meaning dealers did NOT have to backstop — supply cleared into real money. So "soft but functional" is right directionally but the *softness* is on the indirect side specifically, with the offset that dealers weren't loaded up. That's a more useful framing than "BTC 2.55 < 2.68."

### 2. 5/12/2026 10Y — what BOND should have said the day of

| metric | value | percentile (all prior 10Y, N=60) | trailing-12mo (N=17) |
|---|---|---|---|
| bid_to_cover | 2.40 | **30th** | 29th |
| indirect_pct | 51.5% | **7th** | — |
| dealer_pct | 9.6% | 37th | — |

Verdict: **Indirect bid at 51.5% was the 7th percentile of 60 prior 10Y prints** — the weakest indirect take in nearly all of the last 3.4 years of 10Y auctions. That is a real foreign-bid signal, not noise. BTC alone (30th pctile) understates it.

### 3. 5/13/2026 30Y — the actual outlier in the recent set

| metric | value | percentile (all prior 30Y, N=47) | trailing-12mo (N=13) |
|---|---|---|---|
| bid_to_cover | **2.30** | **11th** | 15th |
| indirect_pct | 53.7% | 21st | — |
| dealer_pct | 9.4% | 34th | — |

Verdict: **30Y BTC 2.30 was the 11th percentile of all 30Y auctions since 2023-01-01** (i.e., worse than 89% of the prior sample). Sample mean 2.42, std 0.115. This was not "soft but functional" — this was a genuine tail event in long-end demand, and the framing should reflect that. The 30Y is the auction BOND should have called out hardest, not the 20Y.

### Cross-cutting takeaway for BOND's next read

The three recent prints rank, by composite weakness:
1. **30Y 5/13:** BTC 11th pctile — clearest outlier.
2. **10Y 5/12:** indirect 7th pctile — sharpest foreign-bid degradation.
3. **20Y 5/20:** BTC 38th pctile (middling) but indirect 12th pctile — softest in *quality of demand* not headline cover.

BOND's "soft but functional" frame for 5/20 was correct in spirit but missed that 5/13 30Y was the actual statistical tail and that 5/12 10Y carried the cleanest foreign-demand signal. Going forward: always report headline BTC alongside its percentile rank, AND check indirect_pct percentile separately — they decouple.

---

## v2 changelog (2026-05-20 PM)

Companion CSV `auction_history_v2_prome-spawned.csv` adds four columns to the v1 layout (v1 left untouched for any in-flight readers). All v1 columns retained, including `indirect_pct` (of offering_amount) for backwards compatibility. Refresh script `refresh_auction_history_prome-spawned.py` now writes both v1 and v2 in a single run.

### New columns

| column | formula | notes |
|---|---|---|
| `cmt_close_prior_day` | FRED `DGS{tenor}` close on auction_date; fallback = most recent business day strictly prior. | Used for tail proxy. See caveat below. |
| `tail_vs_cmt_bps` | `(high_yield - cmt_close_prior_day) * 100`, rounded 1 dp. | Positive = stopped at higher yield than CMT close (auction "tailed"). NaN for TIPS (40 rows) and for any tenor where no prior CMT obs exists. |
| `total_competitive_accepted` | `primary_dealer_accepted + direct_bidder_accepted + indirect_bidder_accepted`. | Excludes noncompetitive + SOMA. |
| `indirect_pct_of_competitive` | `indirect_bidder_accepted / total_competitive_accepted * 100`, rounded 1 dp. | The convention ZeroHedge and BOND's STATUS use. Coexists with `indirect_pct` (of offering_amount). |

### Why both indirect conventions matter

The two indirect percentages diverge by ~10pp and rank auctions **differently**. The same 20Y print can be "12th percentile / softening" under the offering-denominator and "45th percentile / middling" under the competitive-denominator. Neither is wrong — they answer different questions:

- `indirect_pct` (of offering_amt) = "what share of supply ended up with indirects" — affected by noncompetitive + SOMA absorption.
- `indirect_pct_of_competitive` = "what share of the competitive book did indirects win" — closer to the true bidder-demand signal because it normalizes out noncompetitive/SOMA noise.

When reconciling against external commentary (ZeroHedge, primary dealer notes), use `indirect_pct_of_competitive`. When tracking the foreign-demand-into-actual-supply signal, use `indirect_pct`. They will be quoted alongside each other in BOND commentary going forward to prevent the dialect collision that surfaced on 5/20.

### CMT-vs-WI approximation caveat (READ BEFORE USING tail_vs_cmt_bps)

The "true" tail is `auction_high_yield - WI_yield_at_13:00_ET_auction_close`. WI (when-issued) is a forward-yield quote on the not-yet-issued security at the moment the auction snaps. The H.15 daily CMT close is **not** WI. It is:

1. A constant-maturity *interpolation* across the curve, not the on-the-run WI quote.
2. Snapped at ~3pm ET, not 1pm ET (auction close).
3. Frequently not yet published when read same-day; we fall back to the prior business day's close in that case.

Practical impact: `tail_vs_cmt_bps` is a **directional proxy with non-trivial noise**. Cross-checked against ZeroHedge prints, individual auctions can disagree with our proxy by 1–5bps. On days with sharp intraday curve moves (or when same-day CMT hasn't published and we use the prior day), the disagreement is larger. The proxy is most useful as a **percentile-ranked time series** within tenor (where the noise is roughly mean-zero), and least useful as a single-auction "was this a tail" classifier.

**Date-matching rule (explicit):** if FRED has an obs for `auction_date`, use it; else fall back to the most recent prior business day in the FRED series.

### Three percentile examples using the new columns (verdict-first)

#### 1. 5/20 20Y reconciled in BOTH indirect conventions

| metric | value | pctile vs prior 20Y (N=40, non-TIPS) |
|---|---|---|
| `indirect_pct` (of offering_amount) | 58.3% | **12.5th** (soft) |
| `indirect_pct_of_competitive` | 67.7% | **45.0th** (middling) |
| `tail_vs_cmt_bps` (proxy) | **-6.8** (i.e., cleared 6.8bps THROUGH 5/19 CMT close) | 0th — but see caveat |
| `bid_to_cover_ratio` | 2.55 | 37.5th |

Resolution: ZeroHedge's "strong" framing (indirect 67.7%, 45th pctile, near-median) and BOND's "soft" framing (indirect 58.3%, 12th pctile of offering) are **both internally consistent** in their own conventions. The honest read is **mixed**: indirect demand was median-to-good *as a share of the competitive book*, but below-trend *as a share of total supply* — meaning a higher-than-usual fraction of the issue went to noncompetitive + SOMA absorption rather than to indirect bidders directly. Dealer take 8.1% (15th pctile) confirms dealers were NOT forced to backstop. Tail proxy of -6.8 is **likely an artifact of the CMT-prior-day approximation** (intraday backup on auction day not captured in 5/19 close); true WI tail was reported ~+1bp. Net: 5/20 20Y was a functional auction with mid-range bidder quality, mild noncompetitive lean, and no dealer stress — not the "weak" headline that "BTC 2.55 < 2.68" would suggest.

#### 2. 5/13 30Y tail in percentile terms

| metric | value | pctile vs prior 30Y (N=40, non-TIPS) |
|---|---|---|
| `tail_vs_cmt_bps` (proxy) | **+1.6** | **75th** (above-median tail = weaker stop) |
| `indirect_pct_of_competitive` | 66.6% | 57.5th (median-to-good) |
| `bid_to_cover_ratio` | 2.30 | 11th (the headline standout) |

Resolution: 30Y tail proxy of +1.6bps is the 75th percentile of prior 30Y prints — auction stopped at a meaningfully higher yield than the 5/12 CMT close. Combined with BTC at the 11th percentile, this confirms 5/13 30Y as the **clearest demand-weakness print in the recent set**. Tail-based ranking (75th) is consistent with BTC-based ranking (11th = bottom-decile cover); both metrics point the same direction. The fact that `indirect_pct_of_competitive` was 57.5th pctile (i.e., NOT weak) means the softness was a *price* problem (had to clear at +1.6 vs CMT) not an *allocation* problem (indirects still showed up). That's a different signature than the 5/20 20Y mix.

#### 3. Cross-tenor tail distribution (decision-useful sizing)

Empirical tail distribution by tenor, 2023-01 → 2026-05 (non-TIPS, proxy basis):

| tenor | mean | std | 25th | 50th | 75th | max |
|---|---|---|---|---|---|---|
| 2Y | +3.4 | 2.2 | +2.4 | +3.5 | +4.4 | +10.9 |
| 3Y | +2.6 | 2.4 | +1.5 | +2.4 | +3.9 | +7.7 |
| 5Y | +0.9 | 4.4 | +0.1 | +1.5 | +2.4 | +4.9 |
| 7Y | +0.9 | 2.6 | +0.3 | +1.0 | +2.2 | +4.8 |
| 10Y | +1.4 | 2.8 | -0.4 | +0.6 | +2.9 | +9.5 |
| 20Y | +1.0 | 2.2 | +0.3 | +1.0 | +2.0 | +4.5 |
| 30Y | +0.2 | 2.5 | -1.1 | +0.3 | +1.6 | +4.9 |

Decision use: any future tail BOND sees can be sized against this distribution. A 20Y tail of +5bps is a ~95th-pctile tail-disaster print; a 20Y tail of +1bp is a median print; a 20Y tail of -2bps is ~10th pctile (stop-through, strong). Useful **calibration** for translating "the auction tailed N bps" into "this is a 1-in-K event for this tenor" instead of relying on dealer-desk vibes.

### Known additional gaps after v2

- `tail_vs_cmt_bps` remains a proxy. If BOND wants WI-accurate tails, the path is to pull the Treasury Direct auction announcement files (which sometimes publish WI) or scrape Bloomberg/TradeWeb — both are higher-friction sources.
- Same-day FRED data lag: for very-recent auctions (today/yesterday), `cmt_close_prior_day` is necessarily the prior business day; expect noisier tails for the most recent rows.
- TIPS rows (40 of 364) intentionally have NaN tail — `high_yield` is a real yield, not nominal, and FRED CMT series are nominal; the comparison is apples-to-oranges. TIPS tails would need DFII* series and were left for a future build.
