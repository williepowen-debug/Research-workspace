# GIBBS — 2026-11-11 catch-up: what a hiking Fed does to the large-bank read

**Session:** PROME catch-up wake (prome-2b) on Will's 09:24 ET word. Claude Code, Opus 5.5. Research only. Wall clock at boot: 2026-11-11 10:21 ET (boot.py). Bond market closed today (Veterans Day); EDGAR accepts no filings today, so filings run through 11/10.

## Five things that matter

1. **A December hike is a small, mixed income effect at the 16, not a stress.** Most large banks gain a little from higher rates; five do not. On each firm's own +100bp shock in its Q3 10-Q, JPMorgan gains $1.4B a year, Wells Fargo $1.5B, Bank of America $1.4B and Citi $1.409B. American Express loses $210M, BNY $44M, Capital One 0.1%, PNC about 0.4% (one third of its −1.3% at +200bp) and Truist 0.2% at +50bp. One 25bp hike is roughly a quarter of those figures: about +0.3% of JPMorgan's ~$106.2B full-year NII (my linear arithmetic; the shocks are instantaneous model runs, not forecasts). REGINALD's cohort figure (Western Alliance +3.2% on a +100bp ramp, 10/13) is on a different basis, so the large-versus-regional tag on this stays NOT-YET-DETERMINABLE.
2. **Long rates are lower than at the 9/30 quarter-end, so the bond-loss drag on capital has eased since Q3, even with a hike priced.** The 10-year was 5.29% at 9/30 and 4.98% at 11/10; the 5-year 5.09% → 4.81% (Treasury par curve). Q3 itself hurt: U.S. Bancorp's capital ratio counting bond losses (CET1 with AOCI, the measure the 3/19 proposal would phase in for Category III) fell from 9.4% to 9.1%, with the AOCI deduction growing from $6.790B to $8.853B. Citi's own table puts a +100bp rise at −$3.117B of AOCI and −17bp of CET1; the 31bp fall since 9/30 is about +$0.97B on that table (my arithmetic, assumes a parallel move; the curve did not move in parallel). The watch level is a 10-year back above 5.29%.
3. **The Fed was already in the 9/30 forward curve.** State Street's 10-Q baseline at 9/30 used a 4.00% fed funds rate with 4.25% twelve months forward, "broadly consistent with market expectations". A December 25bp hike pulls forward one hike that was already priced; it does not shock the large banks' plans. U.S. Bancorp's medium-term targets still assume an "upward sloping yield curve driven by rate cuts" (assumptions dated 9/12/2024, deck of 11/06), so a hiking path contradicts a stated planning assumption without, on its own table, hurting NII (+0.45% at +50bp).
4. **Non-bank lending: still expanding, no NDFI losses.** U.S. Bancorp's 11/06 deck shows a private capital manager client relationship being widened (new joint-lead-arranger commitments across portfolio companies, leveraged buyout financings in 2026–2027): an expansion statement, counterevidence on `ndfi-lender-pullback`. NEXUS's PRED-38 (≥$100M of Q3 non-bank-finance charge-offs at a US bank) missed; that matches my 16-firm 10-Q read. A hike raises borrowers' floating costs (BROCK: Blue Owl's OBDC interest cover about 2.0x → 1.94x at +25bp, its estimate); at the banks that would show first as line tightening or reserve builds at the Q4 prints in mid-January 2027.
5. **Market access and the tape after the 11/05 selloff.** Northern Trust priced $2B of senior notes on 11/05, the selloff day (underwriting agreement and prospectus supplement both dated 11/05; issued 11/10): $1B 5.300% due 2031 and $1B 5.700% due 2036, about 71bp and 86bp over the 11/05 5-year and 10-year Treasury (coupon-based; offering prices not read). From the 11/05 close to the 11/10 close, 14 of the 16 rose (Goldman +4.75%, State Street +3.87%, Northern Trust +3.79%, Citi +3.22%) against the regional-bank ETF (KRE) +1.08%; Capital One fell 3.92% and American Express 0.46%, cause not established. The 11/05 large-bank-led drop reversed in the same names: a tape fact, untagged.

## Sources (read 2026-11-11, 15:21Z–15:28Z)

| Item | Source |
|---|---|
| +100bp NII sensitivity, 16 firms | Q3 10-Qs at EDGAR, each submissions response naming the intended issuer: JPM 0001628280-26-069523 · BAC 0000070858-26-000548 · C 0000831001-26-000056 · WFC 0000072971-26-000327 · GS 0000886982-26-000532 · MS 0000895421-26-000293 · BK 0001390777-26-000120 · STT 0000093751-26-000600 · AXP 0000004962-26-000409 · NTRS 0000073124-26-000066 · USB 0000036104-26-000058 · COF 0000927628-26-000152 · PNC 0001628280-26-069377 · TFC 0000092230-26-000129 · SCHW 0000316709-26-000038 · FITB 0000035527-26-000243 |
| Treasury curve | home.treasury.gov daily par yield CSV 2026 (9/30, 11/05, 11/10 rows) |
| USB deck | 8-K 0001193125-26-450781 (U.S. Bancorp, filed 11/06, Item 7.01), Ex. 99.1 |
| NTRS notes | 8-K 0001193125-26-455429 (filed 11/10 21:05Z, Item 8.01) |
| COF | 8-K 0000927628-26-000157 (11/10, Item 7.01: KBW conference 11/11 11:40 ET; webcast, not read) |
| Fed press feed | federalreserve.gov press_all.xml, read 15:26Z: no capital-regime item since 10/23 |
| Vendor-risk guidance (D:L798) | Federal Register API, document 2026-18859: comments close 2026-11-16; dockets OCC-2026-0793, Fed OP-1881, NCUA-2026-1684 |
| Closes | yfinance daily closes 11/04, 11/05, 11/10 (BK trades as BNY); settled sessions only |

## +100bp sensitivity table (Q3 10-Qs, 9/30/2026; prior period as filed)

| Firm | +100bp (unless noted) | Prior | Basis |
|---|---|---|---|
| JPM | +$1.4B | +$2.1B (12/31) | earnings-at-risk, instantaneous parallel |
| BAC | +$1.4B | +$0.7B (12/31) | banking-book NII, instantaneous vs forward curve, dynamic deposits |
| C | +$1,409M (USD +$37M) | +$1,234M (6/30) | NII 12m; AOCI −$3,117M, CET1 −17bp |
| WFC | +$1.5B | +$1.9B (12/31) | NII 12m, instantaneous |
| GS | +$190M | +$56M (6/30) | net revenues incl. preferred dividends, parallel |
| MS | +$250M | +$202M (6/30) | Wealth Management segment NII, instantaneous |
| BK | −$44M | −$16M (6/30) | vs baseline, static deposits |
| STT | +$354M (USD +$69M) | +$283M (9/30/25) | vs internal baseline |
| AXP | −$210M | n/a | annual NII, instantaneous |
| NTRS | +$36M | +$68M (9/30/25) | gradual over one year, above forwards |
| USB | +0.45% at +50bp; +1.02% at +200bp | −0.07% / +0.80% (12/31) | immediate |
| COF | −0.1% | +0.6% (12/31) | vs projected baseline; EVE −3.5% |
| PNC | about −0.4% (one third of −1.3% at +200bp) | +1.8% at +200bp (9/30/25) | first-year NII |
| TFC | −0.2% at +50bp instantaneous; −0.1% at +200bp gradual | −0.1% / −0.9% (12/31) | 12m |
| SCHW | +3.0% | +3.6% (6/30) | from the 11/08 read |
| FITB | +0.21% (12m), +1.52% (13–24m) | −1.28% / −0.83% (9/30/25) | +100bp ramp over 12 months |

⚠️ Sixteen different models, horizons and deposit assumptions: compare signs and orders of magnitude, never sum.
