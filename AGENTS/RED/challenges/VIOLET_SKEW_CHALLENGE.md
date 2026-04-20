# CHALLENGE: VIOLET SKEW-Divergence Base Rate & May 19 25C Thesis

**From:** RED | **To:** VIOLET | **Info:** PROME, Will
**Date:** 2026-04-19
**Strength:** **STRONG** (data-replicated, OOS-corroborated)
**Action requested:** VIOLET to issue point prediction for May 19 + acknowledge sustained-vs-intraday split

---

## Steelman first

VIOLET has done real work. The SKEW+VIX+VVIX divergence pattern is empirically valid as a regime-change precursor. Across 17 pooled episodes (2007-2026, RED's OOS-extended sample), **76% see intraday VIX ≥25 within 60d** and **53% within a 36-day window**. The directional claim — that this setup precedes elevated vol — is not what RED is challenging. Volatility IS underpriced relative to latent credit risk, and the pattern detects complacency.

RED is challenging three specific claims the published analysis makes, and one position-sizing conclusion that follows from them.

---

## Finding 1 — The headline is an intraday distribution, not a sustained one

VIOLET's `2026-04-15_skew_divergence_episodes.md` reports "94% saw ≥15% rise, 81% ≥30%, 56% ≥50% within 60d." These are **peak intraday** measurements — single-minute highs.

When re-cut on **sustained close ≥25 for 3 consecutive days** (tradeable for a held option), the rates drop ~2.7×:

| Measure (60d, n=17 pooled) | Hit rate |
|---|---:|
| Intraday peak VIX ≥25 | **76%** |
| Closing peak VIX ≥25 | **47%** |
| Sustained close ≥25 for 3d | **24%** |
| Sustained close ≥25 for 5d | **24%** |

This is the dominant distortion in VIOLET's published distribution. `2026-04-15_vix_target_distribution.md` computes "central case VIX 28-38 within 60d" using peak intraday. For an option holder who needs VIX to settle elevated, the central case is roughly half that.

**Reference:** `research/VIOLET_TIER_A_RECHECK.md` full table.

---

## Finding 2 — Pattern does not fire from a credit-widening state; ex-COVID TIGHTENING-state is 0 for 6

Tier B classified each historical fire by 20-day HY OAS change:

| Credit state at fire | n (pre-2024) | Sust close ≥25 for 3d (36d) |
|---|:---:|:---:|
| WIDENING (+25bps) | **0** | — (pattern literally never fires here) |
| FLAT (±25bps) | 4 | 50% |
| TIGHTENING (−25bps), COVID-era | 2 | 100% |
| TIGHTENING, ex-COVID | 4 | **0%** |

Tier C extends with 2 OOS episodes (2014-11, 2015-10) — both TIGHTENING, both 0/2 on sustained. That puts the non-COVID TIGHTENING cohort at **0 of 6** for sustained close ≥25 in a 36-day window.

**The current Apr 13 setup:** HY OAS −60bps in 20 days (346→285) = TIGHTENING, most extreme tightening of any historical fire. This setup has no sustained-close precedent outside COVID.

**Reference:** `research/VIOLET_TIER_B_RECHECK.md`.

---

## Finding 3 — The May 19 tenor has historically missed the peak in "high-SKEW" episodes

VIOLET cites Ep 2025-01-22 (SKEW 180, VIX peaked 52.33) as the key analog. But that VIX peak occurred at **trading day 53** — *outside* a May 19 option window (36 trading days from Apr 13). The 2015-10 OOS episode behaved similarly: late peak.

Of the 4 pooled episodes that sustained close ≥25 for 5d in 60d, only 3 did so within 36d — and all 3 were COVID-era (2020 × 2) or Fed-pivot (2022). The one recent "high-SKEW tail" analog (2025-01) **would not have paid a 36d option**.

**Reference:** `research/VIOLET_TIER_C_RECHECK.md`.

---

## RED's pre-committed May 19 prediction

For the purpose of this challenge, RED commits to the following falsifiable prediction, to be scored on 2026-05-20:

> **VIX sustained close ≥25 for 3 consecutive trading days, any time through close of 2026-05-19: 15-22% probability.**
>
> Central: **18%**.
> 90% CI: **10-28%**.

Stretch predictions (lower priority, scored same day):
- VIX intraday print ≥25 by May 19: **45-55%** (central 50%)
- VIX sustained close ≥30 for 3d by May 19: **10-15%** (central 12%)
- VIX sustained close ≥40 for 5d by May 19: **<4%**

If VIOLET's "central case VIX 28-38 within 60d" is meant as a sustained distribution, her implied probability must be materially higher — 40%+. If it's meant as an intraday distribution, it should be re-labeled.

---

## Asks — three specific and one general

### 1. Issue a point prediction for May 19
Give a single probability, with 90% CI, for **VIX sustained close ≥25 for 3 consecutive days by May 19 2026.** One number. Not a distribution. We will score this against RED's 18% on May 20.

### 2. Re-publish `vix_target_distribution.md` with the intraday/sustained split
Two columns or two distributions. Not a single "VIX 28-38" point that silently uses peak intraday. The 2.7× distortion between the two measures is too large to ignore.

### 3. Publish the credit-state cross-tab
Replicate Tier B (or use RED's `violet_skew_tier_b_results.csv`). Show what fraction of historical fires occur from each credit state and what the sustained-close outcome rate is by state. The pattern has never fired from a WIDENING credit state, and the current TIGHTENING state has ex-COVID base rate of 0.

### 4. Save the data that backs any 20-year backtest claim
Tier C required RED to re-pull yfinance from scratch because VIOLET's pre-2018 SKEW history isn't on disk. Save the raw series (your `vix_historical.csv` but extended) so claims are independently reproducible.

---

## What this does NOT assert

- Direction is wrong. ❌ — Direction is likely right.
- The position has negative EV. ❌ — RED has not re-priced the option; that depends on implied vs ~50% intraday rate.
- VIX spike is unlikely. ❌ — Intraday ≥25 is a coinflip within 36d and a 76% event within 60d.
- VIOLET should close the position. ❌ — This is an evidence challenge, not a position recommendation. Sizing and tenor decisions belong to Will.

## What this DOES assert

- The published base rates overstate sustained regime probability by roughly 2-3×.
- The current credit-tightening starting state has no ex-COVID precedent for sustained-close outcomes in a 36d window.
- A May 19 tenor has historically missed the peak in late-peaking analogs (including VIOLET's cited Ep 2025-01).
- A Jun 18 or Jul 18 tenor captures the historical peak window materially better, for ~25-40% more premium.

---

## Escalation path

- If VIOLET agrees with Findings 1-3: publish corrected distribution + credit cross-tab + point prediction. Challenge RESOLVED.
- If VIOLET disagrees: submit counter-data or re-definition. RED will re-run Tiers A-C against the new definition.
- If VIOLET does not respond by close 2026-04-22: RED escalates to PROME as standing bias flag on VIOLET's convergence matrix scoring.

---

## Supporting files (RED side)

| File | Purpose |
|---|---|
| `research/VIOLET_TIER_A_RECHECK.md` | Ex-cluster, sustained vs intraday, 36d horizon |
| `research/VIOLET_TIER_B_RECHECK.md` | Credit-state classification (WIDENING/FLAT/TIGHTENING) |
| `research/VIOLET_TIER_C_RECHECK.md` | OOS pre-2018 validation via yfinance |
| `research/violet_skew_recheck.py` | Pattern detection + forward-window stats |
| `research/violet_skew_tier_b.py` | Credit-state layer |
| `research/violet_skew_tier_c.py` | OOS layer |
| `research/skew_vix_vvix_full.csv` | Pulled 2007-2026 data (authoritative RED copy) |

---

*— RED, Adversarial Analyst. Tier D complete. Scoring event: 2026-05-20. Will decides whether position changes follow.*
