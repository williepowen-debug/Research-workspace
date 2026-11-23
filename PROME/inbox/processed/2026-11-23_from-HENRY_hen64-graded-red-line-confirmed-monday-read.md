# HENRY → PROME — D:L1226 delivered: HEN-64 HIT, red line confirmed on FRED, `--source` switch built, Monday midday read

**Written:** 2026-11-23 12:13 ET (from `date`). Session: Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop, spawned by PROME prome-77 for **DOCKET L1226** (read whole with `sed -n '1226p'`).

**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/HENRY/CLAUDE.md` 7 · `PROME/COMPLETION_SPEC.md` 4. Desk boot: STATUS, LESSONS, MEMORY read whole; `boot.py --source vendor` 16.1 s; corrections check rc 0; **inbox and WALTER lane both empty (L0 drain: nothing to log).**

## L1226, item by item

| L1226 item | Result | Basis |
|---|---|---|
| Grade HEN-64 on FRED SP500 11/20 | **RESOLVED-HIT, Brier 0.36** (0.40 on YES) | FRED SP500 11/20 **6,910.39** first published, read 12:07 ET 11/23; 189.61 under 7,100.00; 11/19 7,175.83 (over). Vendor bar agrees to the cent |
| Confirm the red-line fire on FRED | **CONFIRMED** | FRED peak since 2025-11-01 = 7,818.93 [10/6] (next 7,811.54 [10/9]); 0.9 × 7,818.93 = 7,037.04; 11/20 is 126.65 under, −11.62% |
| FRED HY and VIXCLS 11/20 | VIXCLS **35.89** (confirms provisional); HY **376bp** (+24), BB 229, CCC 1,402, CCC−BB 1,173 | FRED, read 12:07 ET 11/23. REG-T-04 day 2 of 3 (REGINALD grades) |
| Act on PROME's `--source` answer | **Built:** `--source auto|cboe|yfinance|vendor` on `gamma_flip.py` and `boot.py`; default `auto`; `vendor` sends no Cboe request; `--help` prints usage instead of running a read | Author tests: parse 6/6, zero Cboe requests under a `urlopen` spy (positive control: `auto` reached it), invalid value rc 2, selftest PASS, live boot 16.1 s. **IMPLEMENTED · TESTED · not independently verified.** No level or rule moved; `--publish` still refuses non-Cboe chains. `MAINTENANCE.md` 2026-11-23 |

## Today's tape (vendor live, 12:07–12:08 ET; root rule #4)

S&P **7,245.69 (+4.85%)**, gap open 7,227, back over red 7,037.04, orange 7,100 and yellow 7,200; under the 200-day 7,331.08. NVDA 166.12 (+32.3%; 125.53 on 11/20), SMH +15.0%, NDX +6.96%, **RSP +2.42%**, IWM +3.10%, KRE +1.27%, HYG 76.62 (+0.39%), VIX **28.22** (PROME's 28.39 at 12:04 agrees in level), VIX9D 30.73, VIX3M 26.19, MOVE **102.76** (matches), 10Y 4.94, Brent bar 86.84 (−6.2%). **Cause of the gap UNVERIFIED:** web search found no 11/23 coverage and WALTER has no card today; the NVDA move past its 11/19 level points at a weekend turn in the Nvidia/SEC story (VULCAN's lane, unread by me).

**Dealer-positioning read (my rules: VOL REGIME carries the GEX regime every session).** Source: vendor (yfinance) SPX chain via `gamma_flip.py --both --source vendor`, 12:08 ET; no Cboe request (Cboe refused this box since 11/20). Limits: free-tier proxy, naive dealer convention, $B assumption-dependent; vendor open interest through 11/20 trades; in-session vendor IVs healthy (near-ATM median 24.3% with VIX 28.2). **NOT published** (the script refuses non-Cboe chains by design). Result: **NEGATIVE −19.6 / −43.2 $B per 1%** (14d / 35d), flip **~7,443 / ~7,497**, call 7,400 at both horizons, put WITHHELD (14d 7,300 vs 35d 7,000).

## Forward view (Will 11/19; moves nothing)

- **Expect:** a close over the red line today (≈95%+), then a two-way, amplified tape under the flip into Thanksgiving. Both the break and the rebound were narrow (equal weight about half the index move each day) and credit has not confirmed the rebound (HY +24 on the break day, HYG +0.4% today).
- **Unscored odds to 12/4:** a retest close under 7,037.04 **about 45%** (simulation 42–49%; base rate 50% after +3.5% days with VIX ≥25 since 1990, n=42, crisis-heavy). HEN-65 (≤6,700) current view **about 20%** (simulation 9–15%, base rate 33%); its registered letter stays 0.40 by rule.
- **Alternative:** a V-bottom on an idiosyncratic shock that has now reversed.
- **Horizon:** through 12/4 and the 12/9 FOMC (HEN-63 0.70 for a hike).
- **Changes my mind:** toward the V, FRED HY 11/23 ≤ ~355 (posts Tue 11/24) plus a close over 7,331 and ~7,500. Toward a retest, HY 11/23 ≥376 with equities up, NVDA under ~146, or a close back under 7,100. My 11/21 downside marker (HY ≥ ~370 **with** HYG under ~$75.50) is **not met**: the HYG leg fails.

## Sent

- **TERRY** (awake, Will's 11/10 word): `AGENTS/TERRY/inbox/2026-11-23_from-HENRY_red-line-reclaimed-intraday-credit-unconfirmed.md`, WQ-696 form, no direction forced.
- **No WALTER signal:** no registered threshold fired today; the red-line fire was routed 11/21 (SIG-W-20261121-004) and FRED only confirms it.

## For PROME

- **Optional C4:** charter step 3c still shows the boot command without `--source`; a one-line pointer (`--source vendor` while Cboe refuses) is a C4-class edit I did not make this session.
- **DOCKET L1213** (HEN-64 resolution row, dated 11/25) can be marked RESOLVED-HIT from this memo; HEN-65 is L1227 (12/4).
- **Due next:** the 11/23 close read (HEN-65 window; the 11/21 upside marker "close over ~7,200 with VIX under 30") and FRED HY 11/23 on Tue 11/24 have no DOCKET row naming HENRY that I can see; register if you want a wake.

Records: `AGENTS/HENRY/research/2026-11-23_monday-read/READ.md` · `AGENTS/HENRY/STATUS.md` · `AGENTS/HENRY/workbook/PREDICTIONS.tsv` (HEN-64).

## COMPLETION — HENRY — 2026-11-23
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/{STATUS.md, STATUS_COLD.md, MAINTENANCE.md, MEMORY.md, LAST_COMPLETION.md, NEXUS_BRIEF.md, scripts/gamma_flip.py, scripts/boot.py, workbook/PREDICTIONS.tsv, workbook/KB.tsv, workbook/MARKET_DATA.tsv, research/2026-11-23_monday-read/READ.md}; TERRY inbox packet; this memo
RESULT: HEN-64 RESOLVED-HIT on FRED SP500 11/20 6,910.39 (Brier 0.36); red line 7,037.04 confirmed on FRED (−11.62%); VIXCLS 35.89, HY 376bp. `--source` switch built and author-tested (zero Cboe requests on vendor). Midday S&P 7,245.69 (+4.85%, chip-led, cause unverified); vendor gamma NEGATIVE, flip 7,443–7,497, unpublished; retest by 12/4 about 45%, unscored.
GAPS: Cause of the 11/23 gap unverified (no coverage indexed). Gamma unpublishable while Cboe refuses this box. Switch not independently verified.
WILL_NEEDS: None.
FOLLOW-UP: 11/23 close read and FRED HY 11/23 (Tue 11/24) — no HENRY DOCKET row seen; HEN-65 resolves 12/4.
