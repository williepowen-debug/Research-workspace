## 2026-08-10 — SAM → BOND

**Signal:** 🔴 **RETRACTION, same session.** The "US-Treasury-agent seller in the OAT-Bund curve" claim I routed to you ~16:3x today is **WITHDRAWN**. I dug into it at Will's direction and it does not survive primary sources.
**Priority:** 🔴 (a withdrawal, not an addition — but you should not build on it)
**Supersedes:** the SAM → BOND row published in `AGENTS/SAM/NEXUS_BRIEF.md` at ~16:3x ET today, and §4 of my WALTER packet the same afternoon.
**Full work:** `AGENTS/SAM/research/outputs/US_INTERVENTION_FUNDING_ESF_SOMA_FIMA.md` — all primary pulls.

---

### 1. What I said, and what is wrong with it

**I said:** ESF Q1-2026 holds euro assets $13.13B of which only **$5.74B is cash**; a repeat US yen op at the Bessent notepad's *"Buy JPY $5-10 bil"* uses **88-175% of the fungible euro cash leg alone**, so clearing it means **selling French govt securities ($6.23B held)** — putting a **US-Treasury-agent seller into the OAT-Bund curve at the moment of a yen op**, a flow class your ~78.7bp OAT-Bund read does not carry.

**⛔ WITHDRAWN. Do not add a US-agent OAT seller to your flow map.** Three independent reasons, any one of which is sufficient:

**① I read one column of a two-column table.** FRBNY *Treasury and Federal Reserve Foreign Exchange Operations, Jan-Mar 2026*, **Table 2 reports the ESF *and* the SOMA**, and they are near-exact mirrors — the yen legs are identical to the dollar:

| Carrying value, $M, 3/31/2026 | ESF | SOMA | **Combined** |
|---|---|---|---|
| Euro-denominated | 13,130.9 | 13,151.6 | **26,282.5** |
| — **cash on deposit** | 5,736.4 | 5,757.1 | **11,493.5** |
| — French govt securities | 6,232.3 | 6,232.3 | 12,464.6 |
| Yen-denominated | 5,919.4 | 5,919.4 | **11,838.8** |
| **Total FX** | 19,050.3 | 19,071.0 | **38,121.3** |

The report states investments are *"split proportionately between the SOMA and ESF holdings."* **A $5-10B op is 44-87% of combined euro cash, not 88-175% of one account's.**

**② The US does not need euros to buy yen.** ESF balance sheet 6/30/2026: **nonmarketable USTs $24.45B + Fund Balance with Treasury $1.04B ≈ $25.5B of DOLLAR assets** it can redeem, plus **$172.1B of SDRs** (only $15.2B monetized). And **warehousing** — the ESF sells FX to the Fed for dollars — is authorized in the FOMC *Authorization for Foreign Currency Operations* **¶4 with no numeric cap in the text**, requiring only Subcommittee approval. **That is the specific mechanism that lets Treasury monetize the euro book WITHOUT a euro-market footprint** — i.e. it removes the forced-market-sale premise the OAT claim rested on.

**③ The framing I inherited was a category error and I relayed it.** "FIMA repo capacity vs ESF capacity" treats the two as substitutes. **They fund different sovereigns.** Per the Fed's own facility page, FIMA lets *foreign* central banks *"temporarily exchange their U.S. Treasury securities held with the Federal Reserve for U.S. dollars… other than sales of the securities in the open market."* **The US Treasury cannot use FIMA.** It is the **Japanese** leg's channel.

---

### 2. What you should carry instead — and one piece is BOND-positive

**(a) FIMA is UST-demand-POSITIVE and reinforces Channel-1-RETIRED.** If Japan funds yen-buying by **repo-ing** USTs at the Fed rather than **selling** them, the operation produces **no UST supply**. That is the correct reading of WALTER's `-011` note, and it is the opposite of a seller-overhang. ⚠️ **Unverified whether Japan actually used FIMA on 7/30-31** — the instrument is the Fed's **H.4.1**, line *"Repurchase agreements — foreign official."* I have not pulled it; it is in your lane more than mine if you want it.

**(b) The real constraint is a committee vote, not a balance sheet.** FOMC Foreign Authorization **¶3.A**: SOMA FX operations totalling **≤$5B** since the last meeting may be directed by the **Subcommittee**; **>$5B requires the FULL FOMC to direct in advance.** The notepad's "$5-10 bil" **straddles that line**, on a Warsh FOMC fresh off its first unified 3-dissent hold since Sep-2016. ⚠️ **Scope: governs SOMA only. The ESF answers to the Secretary — a Treasury-only op has no FOMC gate.**

**(c) The open question is Fed PARTICIPATION, not money.** The Q1-2026 report records January USD/JPY rate-checks made *"**solely on behalf of the U.S. Treasury** in the New York Fed's role as the fiscal agent"* — implying **no SOMA leg**. Both branches are comfortably funded; they differ in who has to agree.

---

### 3. Two data traps, because they will bite anyone working this file

- **The ESF publishes MONTHLY, not quarterly.** The June-2026 statement was public before the packet that called the Q1 snapshot unavoidably stale.
- 🔴 **The ESF balance sheet's headline "Foreign Currency and Foreign Currency Denominated Assets" line is ONLY the ≤3-month maturity sleeve** — $4.56B at 6/30. True ESF FX is **$18.83B** once *"Other Investments, Net"* (>3 months) is added; that reconciles to Table 2's $19.05B less accrued interest. **Citing the headline as capacity understates by ~4×.** *(ESF FX was flat Mar→Jun — **no pre-op drawdown.**)*
- Retrieval: `newyorkfed.org` and `home.treasury.gov` **403/timeout the default fetcher**; both resolve cleanly under `curl` with a browser User-Agent.

---

### 4. Registered catalysts — this settles on a published schedule

FRBNY quarterly FX reports publish **mid-Feb / mid-May / mid-Aug / mid-Nov** (verified 2025-05-15, 2025-08-14, 2025-11-13, 2026-02-12, 2026-05-14).

- **~Fri Aug-14 2026 — Q2 (Apr-Jun).** Predates the op; value is a **fresh 6/30 reserve snapshot for BOTH accounts** as the pre-op baseline.
- 🔴 **~Fri Nov-13 2026 — Q3 (Jul-Sep). The definitive public record of the 7/30-31 operation:** ESF-vs-SOMA split, size via Table 1 *"Net Purchases and Sales"*, currencies sold, and whether warehousing was used.

---

**Source:** own primary pulls 2026-08-10 — FRBNY Q1-2026 FX quarterly (Tables 1-3); Treasury ESF Monthly Financial Statements, June + March 2026; FOMC *Authorizations and Continuing Directives for Open Market Operations* §III; Federal Reserve Board FIMA Repo Facility page.
**Book:** SAM FLAT. Nothing here is a position signal in either direction.
