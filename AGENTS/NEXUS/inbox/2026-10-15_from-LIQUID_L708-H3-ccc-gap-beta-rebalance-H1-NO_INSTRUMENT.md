# LIQUID → NEXUS · L708 LIQUID leg (Will-commissioned CCC-gap read) — 2026-10-15T08:40:04-04:00

**Owner file (cite this):** `AGENTS/LIQUID/analysis/2026-10-15_L708-H3-ccc-gap-beta-and-rebalance.md`. FRED ICE first-published = latest-revised on the window (0 mismatches 8/20→10/13); 10/12 carry-forward excluded; your session lists used as written.

- **H3 rebalance arm — NOT SUPPORTED** for the primary window. 10/1 = +23 of +124bp (18.5%); 9/30+10/1 = 45 of 124 (36%). The primary window 10/2→10/13 contains no rebalance and still widened 7/7 (+64).
- **H3 migration arm — excluded inside the primary window by construction.** ICE fixes constituents between month-end rebalances (FRED's ICE note, quoted in the file), so 10/2→10/13 is a fixed basket repricing. B→CCC migration can act only at 10/1 (next: 10/31). 10/1's +23 is the largest month-turn gap change in 35 month turns (prior max +20); month turns average +2.8bp.
- **H3 few-names arm — NO_INSTRUMENT** (no ICE constituent data). One named distressed event inside the window, SECONDARY-sourced: **Getty Images**. NYSE suspended it 9/29; OTC from 9/30; prepack Ch.11 plan 10/12. Its 11.25% 2030 bond still sat at ~90 [10/13] in HYG holdings, and its contribution to the index is unmeasured.
- **Sector split of the CCC index — NO_INSTRUMENT, confirmed.** A proxy is reachable **forward only**: BlackRock's HYG holdings download gives per-bond sector, price and YTW, latest date only (asOfDate ignored, tested 10/15). It cannot rebuild 10/2→10/13.
- **Beta, CCC vs B** (ΔCCC = 1.245·ΔB, R² 0.69, sd 6.5bp, fit 2023-10→2026-09-23, out of sample):
  - Primary window: B −12 implies CCC −15; actual CCC **+52**. Excess **+66.9bp**, positive **7/7**, ≥1 sd **5/7**.
  - Per session: 10/2 +8.2 · 10/5 +6.5 · 10/6 +17.9 · 10/7 +7.5 · 10/8 +14.3 · 10/9 +7.2 · 10/13 +5.3.
  - Rarity: 7/7 positive excess occurred in 7 of 750 historical 7-session windows. The 12-session gap change of +124 exceeds every 12-session change in the fit window (max +121).
  - ⇒ Neither beta nor index plumbing explains the primary window. What is left is a price move inside a fixed CCC basket. That is consistent with H1, H2 (other names), H3's few-names arm or H4, and tier data cannot choose among them.
- **H2, one line:** VULCAN's 4 CCC names, equity only (your z method). 0 of 4 beyond z ≤ −1.0 on ≥4/7 sessions; 0 of 4 within |z| ≤ 0.3 on ≥4/7 ⇒ rule-4 MIXED. Substantively there is no AI-disrupted-CCC equity signal, except Getty's own bankruptcy path (GETY z −4.93 on 10/2; an OTC sub-$0.10 stock, so the z is unreliable).
- Outside your sessions, not used in any verdict: in the 10/13→10/14 HYG proxy, CoreWeave was 28% of the YTW ≥ 12% sleeve's price loss and the top three issuers were 46%. The proxy can see few-name concentration going forward.

**H1 verdict token (LIQUID's lane): NO_INSTRUMENT.** Spec §3 rule 1, n = 0: LIQUID names no consumer issuers with a verified rating and reachable data. CARL and OTTO own the issuer test.
ASK: none.
