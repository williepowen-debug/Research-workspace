# Dealer-Positioning Nexus Watch — registered 2026-07-11 (Sat ~18:00 ET)
**Owner:** LIQUID (credit-plumbing side; HENRY covers rates→equity — reconcile on contact, one figure per shared metric) · **Status:** ARMED-WATCH (a monitoring conjunction, **NOT a prediction of the CPI print** — the print branch lives in `CPI_20260714_CREDIT_PREREG.md`) · **Born from:** threads-sweep TOP-1 (7/11), Will-approved.

## The mechanism (why these three belong in one file)

A hot CPI 7/14 landing on a completed arm-#2 (10Y 5-of-5 ≥4.50 if Mon holds) hits three pre-loaded surfaces at once: front-end repricing forces P&L on the record leveraged SOFR short → cover flow amplifies rates vol (the MOVE leg) → duration-sensitive credit paper reprices into a dealer book that is **structurally short exactly the long-end IG bucket** → gap-pricing, not orderly repricing. My HY>280 X1 line could then be *reached by amplification rather than credit substance* — KB-LIQ-062's beta-vs-substance discriminator and KB-LIQ-074's acute funding rows are the check when this fires. This is the load-bearing scenario the mandate-extension SIG named: the HY>280 trigger assumes dealers can reprice; this watch monitors whether they can.

## The three legs (all fresh-pulled Sat 7/11 from free primaries — vintages stamped)

| Leg | Latest | Trend / context | Source |
|-----|--------|-----------------|--------|
| **1. Positioning** — SOFR-3M futures, leveraged-fund net | **−2,872,406 contracts [as-of Tue 7/7, released Fri 7/10]** ≈ **−$718B notional-equiv** (at ~$250K/contract; $2,500 × IMM index) | Record zone INTACT: −2,449,864 [6/9] → −2,399,900 [6/16] → −2,786,248 [6/23] → **−2,943,898 [6/30] ≈ −$736B window peak** → −2,872,406 [7/7] (+71,492 w/w = marginal covering, not an unwind). Confirms + refreshes the ~$700B datum (SIG-W-20260702-009). Companion: leveraged funds also net-short 10Y ERIS SOFR swaps −135,113 [7/7] ≈ −$13.5B | CFTC TFF via publicreporting.cftc.gov API (futures-only, `gpe5-46if`) |
| **2. Dealer warehouse** — corp-bond net positions | IG >10y (G10): **−$9,402mm [as-of Wed 7/1]**. IG 5-10y (G5L10): **−$213mm [7/1]** | ⚠️ **CORRECTION to my 6/17-based framing:** the G5L10 −$825mm [6/17] flip did NOT persist — +$365mm [6/24], −$213mm [7/1] = **oscillation around zero**, not a sustained no-bid flip. The real structural datum is the LONG end: G10 2026 mean **−$10.0B** vs 2025 mean −$3.96B, 2024 −$0.59B, 2023 −$0.15B — a multi-year ~6x deepening; 2026 range −$6.7B to −$11.7B. HY buckets small/mixed: BELG5L10 −$1,734mm [7/1, widest of the 8-wk window], BELG10 +$366mm | NY Fed PD stats API (`markets.newyorkfed.org/api/pd/`), weekly, ~8d lag; next as-of-7/8 release ~Thu 7/16 |
| **3. Rates-vol** — MOVE vs VIX | MOVE **72.41 [7/9]**, 3 sessions up unreversed; VIX 15.51 [7/9] calm | Rates-led vol signature (VIOLET find, PROME canon 7/9; ^MOVE now in FORGE SERIES per 7/11 commit `34999644` — pull live from Mon) | VIOLET-owned read; FORGE fetch.py ^MOVE |

## Fire conditions (watch → write-up, NOT a position trigger)

| ID | Condition | Meaning |
|----|-----------|---------|
| W1 | SOFR-3M lev net beyond **−2,950,000** contracts (new record past the 6/30 peak) **OR** a one-week **cover >300,000** contracts | Pin deepening / unwind starting (either direction is information) |
| W2 | G10 net-short **< −$12.0B** (beyond the 2026 extreme −$11.66B) **OR** G5L10 **< −$800mm two consecutive weeks** (the persistence the 6/17 print lacked) | Warehouse bid withdrawing at the duration end / mid-curve flip turning real |
| W3 | **MOVE >85 while VIX <20** | Rates-led vol regime confirmed (VIOLET's figure governs) |
| **CONJUNCTION** | **Any 2 of W1/W2/W3 inside a rolling 2-week window** | Same-session write-up → PROME + NEXUS (+HENRY seam); re-run KB-LIQ-074 acute rows (SOFR 99pct tail, SRF) and read any concurrent HY move through KB-LIQ-062 (amplification ≠ substance) |

## Cadence + next prints

- **CFTC TFF:** Fridays ~3:30 ET; next = 7/17 carrying **as-of Tue 7/14 = the post-CPI positioning read** (does the short cover into a hot print?).
- **NY Fed PD:** weekly Thu; next release ~7/16 (as-of Wed 7/8).
- **MOVE:** daily via FORGE from Mon 7/13.
- Feeds: KB-LIQ-074 (slow-lead leg), ES-LIQ-02/04 (tracker cross-refs), NEXUS CPI-week read. Registered in KB as **KB-LIQ-076**.
