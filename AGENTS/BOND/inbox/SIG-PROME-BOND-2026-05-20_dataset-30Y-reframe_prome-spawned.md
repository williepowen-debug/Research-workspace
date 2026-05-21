# SIG-PROME → BOND — Background Build-Out Delivered + 30Y Reframe

**From:** PROME (Claude Code, via Will-authorized cross-agent inbox write)
**To:** BOND
**Date:** 2026-05-20 PM
**Priority:** 🟡 (no decision change tomorrow, but reframes part of last week's read)

## PROVENANCE

This signal was authored by Claude Code PROME during your idle window. Two background research artifacts were also produced and dropped into `AGENTS/BOND/data/` and `AGENTS/BOND/research/`. All three files carry the `_prome-spawned` suffix. **You own integration + commit on next boot** — rename, refine, or reject as you see fit.

## Three Things For Your Next Boot

### 1. New artifact: WI sourcing playbook

File: `AGENTS/BOND/research/WI_SOURCING_PLAYBOOK_prome-spawned.md`

**Key finding:** Pre-1pm intraday WI is **structurally unobtainable** without a terminal. Stop chasing it. **InvestingLive auction recaps are the new primary source** for post-auction WI (free, ~5-15 min post-1pm, explicit "WI level" bullet from same wire ZH uses). ZH is cross-check #2. Tomorrow's 1pm 10Y: refresh InvestingLive 1:05pm, cross-check ZH by 1:45pm.

### 2. New artifact: empirical auction dataset (364 rows, 2023→present)

Files in `AGENTS/BOND/data/`:
- `auction_history_prome-spawned.csv` — 7 tenors, FiscalData-sourced
- `refresh_auction_history_prome-spawned.py`
- `AUCTION_HISTORY_README_prome-spawned.md`

**Load with one line:** `pd.read_csv('AGENTS/BOND/data/auction_history_prome-spawned.csv')`

**TAIL column omitted by design** — needs WI matching, fragile from public data. README documents the FRED-CMT extension path if you want it.

**Endpoint correction:** FiscalData uses `auctions_query`, not `securities_auctioned`. Sub-agent caught this; refresh script uses the correct one.

### 3. Decision-relevant reframe surfaced by the dataset

Percentile ranks against the 2023-present distribution:

| Print | Headline | Percentile finding |
|---|---|---|
| **5/13 30Y** | BTC 2.30 | **11th percentile** of all 30Y auctions since 2023 — the real statistical outlier of the May refunding triplet, not the 20Y |
| **5/12 10Y** | BTC 2.40 | indirect_pct 51.5% = **7th percentile** of 60 prior 10Y auctions — sharpest foreign-bid signal hidden behind a middling BTC |
| **5/20 20Y** | BTC 2.55 | **38th percentile on BTC** (not weak); dataset's indirect_pct 12th percentile — see methodology flag below |

**You were anchored on the 20Y; the 30Y was the actual tail.** Worth re-examining your 5/13 entry in `monitors/AUCTION_HEALTH.md` — "below avg: +0.5bp tail and lower BTC; demand mix not failed" reads soft against an 11th-percentile BTC empirical print. The long-end leg of BND-07 sits on stronger data than your STATUS currently calls out.

### Methodology flag (worth one minute of your time on next boot)

The dataset computes `indirect_pct = indirect_bidder_accepted / offering_amount`. ZeroHedge and your STATUS use indirect % **of competitive accepted** (sums with direct+dealer to ~100%). For today's 20Y: dataset says 58.3% (12th percentile of total-offering convention); ZH/you say 67.7% (strong vs Apr 22's 59.6% in competitive convention). **Both are correct in their dialect.** Recommend adding an `indirect_pct_of_competitive` column on next refresh so the dataset is directly comparable to how recaps report it. The "strong indirect" read of today survives — but the dataset gives you a second yardstick to cross-check against.

## What I'd Suggest You Do First on Next Boot

1. **~5 min:** Read the README; verify the dataset loads.
2. **~5 min:** Note the 30Y reframe in your STATUS regime-read (one paragraph: "The May 13 30Y was 11th-percentile demand, sharper than my 5/13-5/19 framing implied. Long-end leg of BND-07 rests on stronger empirical footing than I called out.")
3. **~10 min:** Add the `indirect_pct_of_competitive` column to the refresh script; commit all three files (dropping `_prome-spawned` suffix at your discretion).
4. **Then:** your normal 12:30pm pre-auction prep for the 10Y reopening.

## Posterior Carry From This Afternoon's Work

Your 5/21 base-rate estimate of ~20-25% (down from ~35-40%) for a 10Y-Leg-2 weak print already integrated the strong 5/20 20Y indirect. The dataset confirms the empirical base rate is roughly that range — 10Y prints with both BTC <2.40 AND indirect <55% happen in roughly 20-25% of post-refunding sessions historically. You were dead on.

— PROME (Claude Code surface)

---

## ADDENDUM (2026-05-21, Will-authorized) — Files already committed

Will asked Prome to commit your build-out artifacts on your behalf (exception to the usual "subagents own their files" rule, so the files enter git history immediately rather than waiting on your integration pass).

**All 9 files are committed at `fcc9f70b` "BOND (Prome-proxied): build-out artifacts + matrix v2 draft from 5/20-21":**

- `research/WI_SOURCING_PLAYBOOK_prome-spawned.md`
- `data/auction_history_prome-spawned.csv` (v1)
- `data/auction_history_v2_prome-spawned.csv` (v2 enriched)
- `data/refresh_auction_history_prome-spawned.py`
- `data/AUCTION_HISTORY_README_prome-spawned.md`
- `analysis/CROSS_TENOR_BASE_RATES_prome-spawned.md`
- `analysis/ESCALATION_MATRIX_BACKTEST_prome-spawned.md`
- `proposals/MATRIX_V2_DRAFT_prome-spawned.md`
- `inbox/SIG-PROME-BOND-2026-05-20_dataset-30Y-reframe_prome-spawned.md` (this file)

**What changes for your next-boot integration:**

- Do NOT `git add` these files — they're already tracked. Running `git status` will show clean (or only your own subsequent edits).
- Your integration job becomes lighter: **rename `_prome-spawned` suffixes at your discretion** (use `git mv` to preserve history) + **integrate findings into STATUS / monitors / KB** + commit those changes under your normal channel.
- If you renumber files (e.g., dropping `v1` once you commit to v2), use `git mv` and a clear commit message explaining the rename. Don't `rm` + `git add` — that loses provenance.
- The proposal file specifically: you're still the author of all current content; final edits + the Q5 resolution will be your call after today's auction.

**Next session schedule (carried forward from PROME/SCRATCH):**
- ~12:30 PM ET 5/21 — pre-auction tape pull (Prome will respawn you)
- ~2 PM ET 5/21 — post-1pm verdict using mandatory dual-grade format → mechanically resolves Q4 deployment timing

— PROME (Claude Code surface), 2026-05-21
