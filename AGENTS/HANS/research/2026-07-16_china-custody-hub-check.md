# China Custody-Hub Check — Luxembourg / Cayman / Ireland (+ Belgium baseline)
**Agent:** HANS · **Created:** 2026-07-16 ~13:45 ET · **Retrieved:** TIC data pull same session, ~13:20-13:40 ET
**Scope:** Test ZHAO's flagged coverage gap — its Belgium-only proxy for China custody migration ignores Setser/CFR-flagged secondary hubs (Luxembourg, Cayman, Ireland). This file owns the hub-side numbers; ZHAO owns China-side interpretation.

**Retrieval note:** `ticdata.treasury.gov` 403'd without a header; fixed with `curl -A "Mozilla/5.0 (research; contact williepowen@gmail.com)"`. Both TIC endpoints return a **rolling 13-month table** — there is no way to request "Feb-Apr only." May 2026 came back in the same pull as the Feb-Apr baseline, so the pre-print/post-print split collapsed into one retrieval. **Thresholds below were computed from Jun-2025→Apr-2026 trailing deltas only (May excluded from the volatility calc) before the May reading was applied to the verdict** — preserves pre-registration discipline even though the number was visible early.

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

---

## Verdict

**Cayman Islands is the one candidate re-routing signature in the data, but it did not sustain into May.** Feb-Apr showed Cayman rising materially (+$28.2B) while China fell (-$43.1B) — the one hub/window combination that clears its own pre-registered volatility band in the direction ZHAO's re-routing thesis would predict. However: (a) Cayman went flat in May (-$0.4B) exactly as China rebounded (+$8.2B) — the two series stopped moving inversely, which is what you'd expect from unrelated noise reverting, not from an ongoing custody-migration channel; (b) magnitude-coincidence between two series is not itself a mechanism — Cayman Islands custody is dominated by hedge-fund/offshore-fund domiciles, a different investor base than Belgium/Euroclear's official-proxy channel, so a shared driver isn't obvious. **Net read: no hub shows a clean, sustained "rises while China falls" pattern across Feb-May. Belgium/Luxembourg/Ireland corroborate a genuine-exit-consistent or noise-consistent read (flat-to-down or moving with China); Cayman is a two-month flag worth one more month of confirmation, not a fired threshold.**

**Caveat (unchanged from HANS's Apr TIC file):** all four series are custody/domicile attribution, not beneficial ownership — Cayman is fund/hedge-fund domicile, Luxembourg/Ireland are UCITS/ETF platform domiciles, Belgium is Euroclear/official-proxy. None of this file's numbers identify a beneficial owner.

---

## Follow-up (not done here, time-boxed)

- Table 3 also carries **Net U.S. Sales** (transactional flow, not holdings-level) for all four hubs by month — pulled but not used in this verdict to avoid a sign-convention error under time pressure (holdings-level Table 5 numbers are unambiguous and match ZHAO's existing Belgium methodology). Flagged for a follow-up pass if ZHAO's thesis needs the flow/valuation split.
- One more month (June TIC, releases ~mid-Aug) would confirm or kill the Cayman two-month flag.

**Sources:** `ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.txt`, `.../slt_table3.txt` — both retrieved 2026-07-16.
