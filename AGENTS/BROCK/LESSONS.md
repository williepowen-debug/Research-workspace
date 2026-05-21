# BROCK LESSONS — Mistake Patterns & Rules

*Review at spawn. If you catch yourself breaking one, stop.*

---

## 🔴 Data Verification

1. **PSEC PIK was 8.6%, not 35%.** Agent hallucinated a 4x inflated number. Always verify BDC financials against SEC 10-K/10-Q filings, not summaries.
2. **BDC earnings dates shift.** Check company IR pages, not cached data. OZK was wrong twice in other agents.
3. **NAV is self-reported.** BDCs mark their own books. Market price (discount to NAV) is the market's opinion of real value. Always track both.

## 🟡 Process Rules

1. **Don't conflate "gating" with "restricting."** Blue Owl restricted quarterly redemptions ≠ formal gating. Blackstone honoring 100% ≠ stress-free. Precision in language matters for cross-agent signals.
2. **Track the delta, not just the level.** BCRED going from 5% to 7.9% redemptions matters more than the absolute 7.9%. Rate of change is the signal.
3. **Mark-to-model ≠ mark-to-market.** Private credit NAVs are model-derived. When BDCs trade at 73% of NAV, the market is saying the model is wrong. Don't trust the model over the market.
4. **Insurance/reinsurance is a parallel domain.** Don't let Athene/ILS analysis crowd out core BDC monitoring. Track both but keep STATUS.md focused on credit first, insurance second.

## 🔵 Lessons from Mar 9-12, 2026 Events

5. **Transparency cascades follow disclosure anchors.** DB disclosing €26B PC exposure forces other banks to quantify their own NBFI/PC books. The first mover in a disclosure cascade is always the most important signal — not because of their individual exposure, but because of what it makes others reveal. Watch for JPM, BofA, Citi quantifying their PC books in 2-4 weeks.

6. **When the world's largest bond manager calls something structural, it IS structural.** PIMCO Stracke calling this a "crisis of bad underwriting" with multi-year defaults matters not because PIMCO is always right, but because institutional allocators respond to PIMCO publicly. This is the mechanism: PIMCO speaks → allocators cut PC strategic allocation → redemption pressure is sustained over years, not months. Different from retail gate cascade.

7. **Verify the ownership chain on named companies.** Thoma Bravo owns Medallia (78¢ bellwether). This wasn't in our initial framing — the bellwether WAS ALREADY a Vista/TB signal all along. When working with named PE sponsors, immediately trace portfolio ownership to see if you already have live pricing.

8. **Structural vs cyclical distinction changes trade duration.** A cyclical credit stress resolves in 12-18 months — position with Dec expiry. A structural repricing (returns 10%→6%, institutional reallocation) plays out 2-4 years. Dec 2026 puts may need to be rolled again. Don't let "cyclical frame" collapse a structural position prematurely.

9. **Distressed dry powder is a two-sided signal.** $100B+ vulture capital entering = validates stress is real AND provides a floor. The presence of buyers moderates the cliff-down scenario and favors a grinding, stepwise decline. Adjust expected path: staircase down, not elevator.

10. **Sector broadening is the confirmation, not the trigger.** When consumer products hit >12% default rate (doubled YoY), that confirms software wasn't idiosyncratic. The LABOR→consumer→private credit channel is active. Consumer credit stress is the second epicenter and deserves its own watch vector.

## 🟢 Lessons from May 1, 2026 Catch-up Session

11. **Fee economics vs lending economics — read alt-manager Q1 prints with separation.** OWL Q1 2026 (Apr 30) posted +14% FRE / +11% DE on record AUM $314.9B but direct lending strategy returned **-1.1% for the quarter** with negative net deployment of $0.5B. Stock surged on the FRE beat. Bulls and bears are pricing different things. When reviewing PE/alt earnings, separate management-fee P&L (scales with AUM, agnostic to credit) from balance-sheet/portfolio P&L (the actual credit signal). The fee economics can mask the lending decay for several quarters.

12. **Narrative confirmation ≠ thesis terminus.** Howard Marks memo (Apr 9) + JPM/S&P short product (Apr 10) felt like Stage 3 was unstoppable — peak-bearish narrative. Three weeks later, alt-managers had rallied 16-22% off lows on OWL Q1 fee-economics beat. Stage 2→3 transitions can stall on sponsor backstops (BCRED $400M from BX/execs), fee-economics earnings beats, and HY OAS compression from non-PC drivers. Don't treat "consensus catching up" as the trigger to fully cash thesis — it can be local top, with bear-thesis re-arming on the next 10-Q cycle.

13. **National Dentex was Cerberus, not Thoma Bravo.** BRK-21 prediction notes (written Mar 17) attributed National Dentex to Thoma Bravo. Cerberus actually owns it (acquired Oct 2020). Caught at resolution Apr 30 when researching the maturity outcome. **Concrete validation of Rule #7 (verify ownership chain on named companies)** — wrong sponsor attribution wouldn't have changed the prediction outcome but matters for cross-portfolio concentration analysis (Cerberus has separate concentration profile from Thoma Bravo). Always verify sponsor before writing notes that reference cross-fund overlap.

14. **TSV schema: trailing empty fields require explicit tab terminator.** When appending PREDICTIONS rows where the Notes (last) column was empty, awk read those rows as 8 cols instead of 9 — schema validation flagged them. Fix: ensure every row ends with the correct number of `\t` separators even for empty trailing fields, or insert a placeholder character. **Verify NF count via `awk -F'\t' '{if (NF!=N) print NR": BAD "NF}' file.tsv` after every TSV write or append.** Catching this at write time is much cheaper than discovering it during a downstream analysis.

## 🟣 Lessons from May 21, 2026 Revival Session

15. **Match the vehicle to the open transmission channel — equity puts bleed when tape is regime-suppressed even if the thesis validates substance-side.** The May 1 → May 21 window proved this hard: BROCK-domain equity put book (APO Jun $100P, APO Dec $95P, ARES Jun $95P, OWL Jun $9.5P, HYG Jun $75P) ran **-84% on $3,200 cost basis** while substance fully validated (FSK Q1 Max Bear data, NDFI scope 11× bigger than tracked, Ch11 +42% April, regulator escalation, sponsor-bifurcation diagnostic). Same broad credit-stress thesis expressed via TLT puts (LIQUID-side duration channel) was **+$600 cumulative**. The substance was right; the equity-vehicle channel was closed (HY OAS never broke 260, VIX never spiked, gamma suppression held). The duration channel was open (10Y +42bps over window, TLT down -3.2%). **Before sizing into single-name equity puts on a credit-cycle thesis, check which transmission channels are currently open and express via those — not via the channel your narrative wants to use.** Long-dated strike-near-spot puts (e.g., APO Dec $95P at 210d) are the equity-channel exception: enough time for the regime to break. Near-dated deep OTM puts (Jun $100P at 25% OTM, 28d) are the regime-suppression bleed-trap.

16. **Execution rails matter as much as decisions.** TRADE.md's May 1 plan to roll HYG Jun→Dec was correct framework. It never executed during the 20-day BROCK dark window because there was no mechanism to act on it: Will wasn't watching, BROCK wasn't booted, no agent-authorized execution path existed. By 5/21 the HYG mark had collapsed to $0.05 ($40 residual on $245 cost) and the roll math no longer worked. **A decision in a STATUS or TRADE file with no execution mechanism is half-finished work.** Either: (a) explicitly schedule Will-action with a clear trigger ("on next green day, roll"), (b) flag to Prome for monitoring, or (c) accept that the decision is conditional-on-being-booted-when-the-trigger-hits and is therefore weaker than it reads. Don't write rollover plans into STATUS files as if they'll self-execute.
