---
signal_id: SIG-W-20260927-004
date: 2026-09-27
timestamp: 2026-09-27T16:35:00Z
time_dispatched: 2026-09-27T16:35:00Z
source: PROME
origin: ["cross-session message prome-09 -> walter-42, 2026-09-27 ~16:2xZ (signal-source pointer; PROME routes nothing)", "https://www.fdic.gov/news/press-releases/2026/sunwest-bank-assumes-all-deposits-and-certain-assets-nano-banc-irvine (read by WALTER 9/27)", "https://dfpi.ca.gov/press_release/california-seizes-nano-banc/ (read by WALTER 9/27)", "PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md §1 (PROME's primary reads: BankFind, Call Reports, American Banker 9/25 21:17 ET)", "AGENTS/REGINALD/workbook/KB.tsv ML-REG-039, ML-REG-044"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Nano Banc", "FDIC cert 58590", "Sunwest Bank", "WAL", "ZION", "BANC", "EFSC", "ML-REG-039", "ML-REG-044", "MOM CA Investco"]
confidence_language: Closure, acquirer, size and DIF cost verified by WALTER at the FDIC and DFPI releases; loan-book and deposit-behaviour figures are PROME's Call Report reads; the WAL exposure figure is a secondhand Feb-2026 KB row
signal_type: catalyst
safety_net: clear
verdict: "Nano Banc (Irvine CA, $736M assets 6/30) closed by California DFPI Fri 9/25; FDIC receiver; Sunwest Bank (Sandy UT) assumed the deposits and ~$476M of assets; estimated DIF cost ~$114M = 15.5% of assets. No depositor loss. The fleet link to WAL is through the Stupin-Marcil fraud (WAL ~$100M exposed per a Feb-2026 external-research KB row), NOT a WAL loan to Nano Banc. Will commissioned REGINALD, CREED, WAL, DEWEY and ORACLE on it 9/27 (PROME 17a205519)."
precedence: IMMEDIATE
action: []
info: ["REGINALD", "WAL", "CREED", "LIQUID", "DEWEY", "ORACLE", "PROME", "TERRY", "RED"]
confidence: 0.85
status: PARTIALLY-CORRECTED
---

> ⚠️ **PARTIALLY-CORRECTED 2026-09-27 by `SIG-W-20260927-005`:** the WAL framing below is INCOMPLETE. Per WAL's own verified complaint (LA Superior 25STCV24263), **Nano Banc holds 4 deeds of trust ($28.04M original face) SENIOR to WAL on 5 of the 10 collateral loans WAL pleads**, so the link is direct, not only through the fraud (current holder of those liens UNKNOWN). Also corrected: "participant, not victim" (liable in one forum, cleared in another); the MOM CA Investco Ch.11 was dismissed in 2025 (not live); the Fed C&D was issued 1/18/2022 and terminated 3/20/2025. Closure, acquirer, size and DIF cost stand.
> ⚠️ **ALSO CORRECTED 2026-09-27 by `SIG-W-20260927-006` (owner-sourced, REGINALD):** the "BANC+EFSC ~$108M" below is THREE lenders combined incl. Nano Banc, with no per-bank split in any filing; the FDIC-retained pool is **≈$215M** (9/22 books), not ~$260M. Shared loss figure to cite: **≈$120M ≈ 17% of $690.9M** (9/22 books); the FDIC's ~$114M / 15.5% stays correct on its own 6/30 basis.

# Nano Banc (Irvine, CA) failed Friday: a $736M bank, a ~$114M loss to the FDIC fund, and a fraud-ring link to WAL that is indirect

**Short version:** California's regulator (DFPI) closed **Nano Banc**, Irvine CA, on **Friday 2026-09-25** after markets shut. The FDIC is receiver. **Sunwest Bank** (Sandy, UT) assumed the deposits and ~**$476M** of the assets, and the branch reopens Monday as Sunwest. **No depositor loses money.** The FDIC estimates the cost to the Deposit Insurance Fund at **~$114M, about 15.5% of the bank's $736M assets** — a heavy loss for its size.

**Why it is on the board at IMMEDIATE:** it is a closed-market event touching an underlying held in the book (WAL; the position is TERRY's and the broker's, not described here), and the market prices it at Monday's open.

## ⚠️ Read the WAL link narrowly (this is the caveat that matters)

- The fleet's tie to WAL is **REGINALD's KB rows `ML-REG-039` / `ML-REG-044` (2026-02-02)**: Nano Banc was a **co-conspirator** in the Stupin–Marcil fraud syndicate ($270M+), in which **WAL ~$100M, ZION ~$60M, BANC+EFSC ~$108M** were exposed.
- ⛔ **That is exposure to the FRAUD, not a WAL loan to Nano Banc.** Nano Banc was a participant, not a victim, so its failure does not by itself create a new WAL loss.
- ⚠️ **The ~$100M is secondhand** — the KB row's source is an external research agent, not a filing. Whether the receivership changes WAL's recovery (FIRREA claims bar; the ~$382M MOM CA Investco / Honarkar Ch.11) is **open and is the WAL desk's commissioned question.**
- REGINALD's `ML-REG-044` called it (*"facing receivership"*, Feb 2026). It had no date and did not predict the 15.5% severity; REGINALD grades its own row.

## Verified at the primaries by WALTER (9/27)

| Fact | Figure | Source |
|---|---|---|
| Closed | Fri 2026-09-25 by California DFPI; FDIC receiver | FDIC + DFPI releases, both dated 9/25 |
| Acquirer | Sunwest Bank, Sandy UT — all deposits + ~$476M of assets | FDIC |
| Size | total assets **$736M**, total deposits **$686M** (as of 2026-06-30) | FDIC |
| DIF cost | **~$114M** (= 15.5% of 6/30 assets, WALTER arithmetic) | FDIC |
| Why seized | equity **below the 3% statutory minimum**; unsafe/unsound operation; failed DFPI's order to hold ≥9.5% tangible equity; net loss ~$75.3M reported March 2026 | DFPI |
| Prior actions | DFPI notice order, then a cease-and-desist after leadership was replaced without approval; Federal Reserve actions (2022) on governance/compliance | DFPI |

## PROME's reads (its plan §1; not re-read by WALTER)

- **Deposits assumed ~$605M** (American Banker 9/25) vs **$686M** total deposits at 6/30 — the ~$81M gap is **not explained** by any source read (outflow after 6/30 is one possibility, not established); FDIC's release gives no deposit figure at closing. FDIC keeps ~$260M of assets for later sale.
- **Loan book (6/30):** gross loans $479M, 76% real estate (non-residential CRE $129M · multifamily $71M · construction $47M); **noncurrent loans 25.7%**, up from 0.2% at 12/24. Uninsured deposits $390M (57%). Deposits fell 21% over 15 months — **a bleed, not a run.**
- **Sixth US bank failure of 2026** and the only one above $300M. **A loss over $50M makes a Material Loss Review mandatory** (Fed OIG, ~6 months ⇒ ~late March 2027).
- ⚠️ **Date conflict to resolve (REGINALD's):** PROME's plan and DFPI put the Fed C&D in **2022** (terminated Apr 2025); REGINALD's KB row says *"Fed C&D March 4, 2025."*

## Who is already working it (Will-directed, PROME `17a205519`)

REGINALD (forensics + lookalike screen) · CREED (collateral and the forced-sale mark) · WAL (receivership and the Stupin recovery leg) · DEWEY (primary documents) · ORACLE (the markets question). **Those asks are in PROME's packets; this signal adds no new ask.** LIQUID is on info for the funding read: no depositor loss, and the bank was a slow deposit bleed, not a run.

**Watch terms** PROME suggested for the lane (`Nano Banc` · `Sunwest Bank` · `material loss review` · `FDIC loan sale` · `MOM CA Investco`) go through the R3 live test before landing.

$0. No trade. Trade construction is TERRY's.
