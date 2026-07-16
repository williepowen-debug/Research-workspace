# China Custody-Hub Check — Luxembourg / Cayman / Ireland (+ Belgium baseline)
**Agent:** HANS · **Created:** 2026-07-16 ~13:45 ET · **Retrieved:** TIC data pull same session, ~13:20-13:40 ET
**Scope:** Test ZHAO's flagged coverage gap — its Belgium-only proxy for China custody migration ignores Setser/CFR-flagged secondary hubs (Luxembourg, Cayman, Ireland). This file owns the hub-side numbers; ZHAO owns China-side interpretation.

**Retrieval note:** `ticdata.treasury.gov` 403'd without a header; fixed with `curl -A "Mozilla/5.0 (research; contact williepowen@gmail.com)"`. Both TIC endpoints return a **rolling 13-month table** — there is no way to request "Feb-Apr only." May 2026 came back in the same pull as the Feb-Apr baseline, so the pre-print/post-print split collapsed into one retrieval. **Thresholds below were computed from Jun-2025→Apr-2026 trailing deltas only (May excluded from the volatility calc) before the May reading was applied to the verdict** — preserves pre-registration discipline even though the number was visible early.

**⚠️ May-26 data label (PROME-verified 2026-07-16 ~13:35 ET):** every **May-26 figure in this file** is **May 2026 [TIC SLT pre-staged, pulled ~13:15 ET 7/16; official release 4:00 PM ET 7/16 — PROME re-verifies at 4:03 PM]**. PROME independently pulled `slt_table3.html` and confirmed the pre-staged May column is genuine (Belgium Mar 454,026 exact match to ZHAO's anchor; schema = `for_lt_treas_net` etc.) — this was NOT a stale-mirror/date-shift misread. Sign convention is also now confirmed from the source file's own documentation line (`slt_table3.txt` header): **"A positive number for net U.S. sales to foreigners denotes an increase in a foreign position."** If PROME's 4:03 PM re-check finds any May figure moved at the official release, this file gets re-stamped — treat May figures below as pre-staged-but-verified, not yet reconciled against the 4 PM press release.

---

## 1) Holdings level, Feb-May 2026 (Table 5, $B)

| Hub | Jan-26 | Feb-26 | Mar-26 | Apr-26 | May-26 | Feb→May cum. Δ |
|---|---:|---:|---:|---:|---:|---:|
| **Belgium** | 451.0 | 454.7 | 454.0 | 459.9 | **472.0** | **+17.3** |
| **Luxembourg** | 446.2 | 446.0 | 432.4 | 431.1 | **436.0** | **-10.0** |
| **Ireland** | 342.1 | 350.8 | 355.9 | 345.3 | **357.2** | **+6.4** |
| **Cayman Islands** | 433.2 | 443.4 | 460.1 | 471.6 | **471.3** | **+27.9** |
| *China, Mainland (ref., ZHAO owns)* | *695.3* | *694.2* | *653.3* | *651.1* | *659.3* | *-34.9* |

Source: Treasury TIC Table 5 (`slt_table5.txt`), retrieved 2026-07-16. Belgium Mar=454.0 matches ZHAO's pinned baseline exactly. **Minor revision note:** Table 3 carries Luxembourg Mar at 432.424 (vs an earlier HANS Apr-vintage file's 432.0) and Ireland Mar at 355.925 (vs 355.2) — routine TIC revision, not a data error; use this file's figures as current.

## 2) Month-over-month deltas ($B)

| Hub | Feb Δ | Mar Δ | Apr Δ | **May Δ** |
|---|---:|---:|---:|---:|
| Belgium | +3.7 | -0.7 | +5.9 | **+12.1** |
| Luxembourg | -0.2 | -13.5 | -1.3 | **+4.9** |
| Ireland | +8.7 | +5.1 | -10.7 | **+12.0** |
| Cayman Islands | +10.2 | +16.7 | +11.5 | **-0.4** |
| *China (ref.)* | *-1.1* | *-40.9* | *-2.2* | ***+8.2*** |

## 3) Pre-registered thresholds (trailing volatility, Jun-2025→Apr-2026, May excluded)

| Hub | Trailing MoM σ | 1σ | **2σ ("notable rise" flag)** |
|---|---:|---:|---:|
| Belgium | $13.1B | $13B | **$26B** |
| Luxembourg | $7.8B | $8B | **$16B** |
| Ireland | $8.1B | $8B | **$16B** |
| Cayman Islands | $12.5B | $13B | **$25B** |

**Rule stated before applying to May:** a hub MoM rise ≥ its 2σ line, in a month China's official line falls, counts as a re-routing-signature candidate. A cumulative multi-month rise approaching or exceeding the *single-month* 2σ line while China falls over the same window is a softer "watch" flag (not a fired threshold).

## 4) Applying thresholds

**May 2026 (freshest month):** None of the four hubs breach their 2σ line. Also — **the premise doesn't hold this month**: China's holdings **rose** +$8.2B Apr→May, reversing its Feb-Apr decline. There is no China fall in May for a hub rise to "explain." Ireland's +$12.0B is the closest to its $16B line (~1.5σ) but coincides with China rising, not falling — not a re-routing read.

**Feb→Apr window (the window ZHAO's original ask targeted, before the May print landed in the same pull):** China fell **-$43.1B** (694.2→651.1). Against that:
- **Cayman Islands rose +$28.2B** cumulative — *exceeds* its own single-month 2σ line ($25.1B) even spread over two months. This is the one hub that moved materially opposite China's direction, in scale.
- Belgium: +$5.2B (flat, below threshold).
- Luxembourg: -$14.9B (fell **with** China — same direction, not re-routing).
- Ireland: -$5.5B (fell with China — same direction, not re-routing).

## 5) China May rebound — composition (ref. only, ZHAO owns interpretation)

Table 3, China row, **2026-05 [pre-staged, see label above]** — sign convention per source doc: positive = increase in foreign position.

| Component | 2026-05 value | Read |
|---|---:|---|
| Total net U.S. sales (= net position change) | **+$5.947B** | Net increase in China's position |
| LT (bonds/notes) net | **-$0.129B** | ~flat — essentially no long-term buying |
| LT valuation change | **+$1.705B** | Price/FX effect, not a transaction |
| ST (bills) net | **+$6.076B** | Bill buying drives essentially all of the net increase |

**Read:** China's May **+$8.2B holdings rebound (Table 5, 651.1→659.3) is bills-driven, not a resumption of coupon/duration buying** — LT net purchases are approximately flat (-$0.13B). This composition detail matters for ZHAO's exit-thesis interpretation: a bill-only bounce is consistent with cash-management/collateral behavior and is a materially weaker signal than a coupon-buying rebound would be. HANS pulled this row independently (Table 3, `slt_table3.txt`, 2026-07-16) to source it directly rather than relay a secondhand figure.

---

## Verdict

**Cayman Islands is the one candidate re-routing signature in the data, but it did not sustain into May.** Feb-Apr showed Cayman rising materially (+$28.2B) while China fell (-$43.1B) — the one hub/window combination that clears its own pre-registered volatility band in the direction ZHAO's re-routing thesis would predict. However: (a) Cayman went flat in May (-$0.4B) exactly as China rebounded (+$8.2B) — the two series stopped moving inversely, which is what you'd expect from unrelated noise reverting, not from an ongoing custody-migration channel; (b) magnitude-coincidence between two series is not itself a mechanism — Cayman Islands custody is dominated by hedge-fund/offshore-fund domiciles, a different investor base than Belgium/Euroclear's official-proxy channel, so a shared driver isn't obvious. **Net read: no hub shows a clean, sustained "rises while China falls" pattern across Feb-May. Belgium/Luxembourg/Ireland corroborate a genuine-exit-consistent or noise-consistent read (flat-to-down or moving with China); Cayman is a two-month flag worth one more month of confirmation, not a fired threshold.**

**Caveat (unchanged from HANS's Apr TIC file):** all four series are custody/domicile attribution, not beneficial ownership — Cayman is fund/hedge-fund domicile, Luxembourg/Ireland are UCITS/ETF platform domiciles, Belgium is Euroclear/official-proxy. None of this file's numbers identify a beneficial owner.

---

## Follow-up

- **Resolved:** sign convention on Table 3's "Net U.S. Sales" columns is confirmed (source doc: positive = increase in foreign position) — the flow/valuation split (§5 above) is now usable; a full four-hub flow table (not just China) is a candidate follow-up if ZHAO's thesis needs the LT/ST split for Belgium/Lux/Ireland/Cayman too (not built here, time-boxed).
- One more month (June TIC, releases ~mid-Aug) would confirm or kill the Cayman two-month flag.
- **Pending:** PROME's 4:03 PM ET re-verification of the May column against the official 4:00 PM release. If any figure moves, this file and the ZHAO note both need a re-stamp.

**Sources:** `ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.txt`, `.../slt_table3.txt` — both retrieved 2026-07-16.
