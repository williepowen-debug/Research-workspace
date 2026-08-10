# WHAT ACTUALLY FUNDS A US YEN-BUYING INTERVENTION — ESF, SOMA, WAREHOUSING, AND WHY "FIMA vs ESF" IS THE WRONG QUESTION

**Author:** SAM · **Date:** 2026-08-10 · **Status:** COMPLETE — answers the question SAM registered the same morning as "the highest-value open item on the intervention file"
**Verdict in one line:** 🔴 **THERE IS NO BALANCE-SHEET CEILING ON A REPEAT US YEN OPERATION. SAM's own 8/10-morning "ceiling candidate" escalation is RETRACTED.** The real constraint is a **$5B FOMC decision-rights threshold** that binds the **Fed leg only** — and there is direct evidence the Fed leg may not be participating at all.

> ## ⚠️ THIS DOCUMENT RETRACTS A SAM CLAIM PUBLISHED EARLIER THE SAME DAY
> On 2026-08-10 (~16:3x ET) SAM published, to `STATUS.md`, `NEXUS_BRIEF.md`, `MEMORY.md` and a routed packet to **BOND**, the read that *"the US leg of the two-sovereign regime has a balance-sheet ceiling"* — sourced from WALTER `SIG-W-20260809-014`, and flagged at publication as a **CEILING CANDIDATE, not a measured constraint**. **That flag was doing real work: the candidate does not survive.** The retraction and its routing are §7.

---

## 1. THE QUESTION AS IT WAS HANDED TO SAM, AND WHY IT WAS MALFORMED

WALTER `SIG-W-20260809-014` §3 framed the open item as a **substitution**:

> *"NO detail on the FIMA UPSIZING Bessent flagged in `-011` — if FIMA upsizing is the funding mechanism for future ops, the ESF Q1 snapshot is not the binding capacity constraint; the FIMA repo capacity is."*

SAM carried that framing forward verbatim. **It is a category error, and SAM should have caught it before routing it.**

**FIMA and the ESF do not fund the same leg. They fund different sovereigns.** From the Federal Reserve's own facility page:

> *"The FIMA Repo Facility allows FIMA account holders, which consist of **central banks and other international monetary authorities** with accounts at the Federal Reserve Bank of New York, to enter into repurchase agreements with the Federal Reserve. In these transactions, approved FIMA account holders **temporarily exchange their U.S. Treasury securities held with the Federal Reserve for U.S. dollars**… an alternative temporary source of U.S. dollars for foreign official holders of Treasury securities **other than sales of the securities in the open market**."*

- **FIMA is a facility for FOREIGN authorities to obtain dollars.** Eligibility is restricted to central banks and official monetary authorities with FRBNY custody accounts. **The US Treasury cannot use it.** It is not, and cannot be, a funding source for the US leg.
- **For a yen-buying operation, FIMA is the JAPANESE leg's channel:** MOF/BOJ raise dollars against their UST holdings **without selling USTs into the market**, then sell those dollars for yen. That is exactly what WALTER's own `-011` had correctly identified — *"the regime is funded by REPO-ing Treasuries at the Fed, NOT selling them"* — and it is a **UST-demand-positive** mechanism, which is why it was routed to LIQUID/BOND as Channel-1-RETIRED-reinforcing.
- **The ESF is the US leg.**

**⇒ They are not alternatives. Both can be live simultaneously, on opposite sides of the same trade.** The correct decomposition is two independent questions:
- **(a) What constrains the US leg?** → §2-§4 below.
- **(b) What constrains the Japanese leg?** → FIMA capacity + MOF reserves. **Out of scope here and NOT answered by this document** (see §8).

*(Class: [[finding_threshold_vs_mechanism]] — the packet named a threshold ("FIMA capacity") without checking that the mechanism attaches to the leg being constrained.)*

---

## 2. WHAT THE US ACTUALLY HOLDS — AND THE COLUMN THE PACKET DIDN'T READ

**Source: FRBNY, *Treasury and Federal Reserve Foreign Exchange Operations, January-March 2026*, Table 2 (published 2026-05-14). Own pull, primary.**

WALTER's figures were **correct as far as they went** — SAM checked specifically whether a combined figure had been misattributed to the ESF, and it had not. **But Table 2 has TWO columns**, and only one was read:

| Carrying value, $M, 2026-03-31 | **ESF** | **SOMA** | **COMBINED** |
|---|---|---|---|
| **Euro-denominated assets** | 13,130.9 | 13,151.6 | **26,282.5** |
| — cash held on deposit at official institutions | **5,736.4** | **5,757.1** | **11,493.5** |
| — marketable securities held outright | 7,394.5 | 7,394.5 | 14,789.0 |
| —— French government securities | 6,232.3 | 6,232.3 | 12,464.6 |
| —— German government securities | 670.5 | 670.5 | 1,341.0 |
| —— Dutch government securities | 491.7 | 491.7 | 983.4 |
| **Yen-denominated assets** | 5,919.4 | 5,919.4 | **11,838.8** |
| — yen cash on deposit | 3,007.5 | 3,007.5 | 6,015.0 |
| **TOTAL FX** | **19,050.3** | **19,071.0** | **38,121.3** |

**The two portfolios are near-exact mirrors — the yen legs are identical to the dollar.** That is by design, and the report says so:

> *"The SOMA and the ESF foreign currency reserves are **managed comparably** so that their risk and return characteristics match as closely as possible. **To the extent practicable, investments are split proportionately between the SOMA and ESF holdings.**"*

And the standard institutional arrangement is that **US intervention is jointly financed by the two accounts, shared equally** — *(this specific "shared equally" claim is from secondary sources, NOT the primary report; the mirror-portfolio structure above IS primary, and is the stronger evidence)*.

### The arithmetic, restated against the Bessent notepad's "Buy JPY $5-10 bil"

| Denominator | Amount | $5-10B op as % |
|---|---|---|
| ESF euro **cash** only *(WALTER's basis)* | $5.74B | **87-174%** ← the "ceiling" |
| **Combined** euro cash (ESF+SOMA) | $11.49B | **44-87%** |
| Combined **total** euro assets | $26.28B | 19-38% |
| Combined **total** FX reserves | $38.12B | 13-26% |
| ESF FX **+ ESF dollar assets** (§3) | $44.33B | 11-23% |

**The "ceiling" exists only if you insist the operation must be funded exclusively out of one account's euro cash — an assumption nobody made and no document supports.**

---

## 3. THE US DOES NOT NEED EUROS TO BUY YEN — AND THIS IS THE POINT THE WHOLE FRAME MISSED

A yen-**buying** intervention means selling *something* for yen. The euro-selling leg on 7/31 was a **tactical choice**, not a resource constraint. The US can also sell **dollars**, and its dollar resources are not scarce:

**ESF balance sheet, 2026-06-30 (own pull — Treasury publishes MONTHLY, see §5):**

| ESF line | 2026-03-31 | 2026-06-30 |
|---|---|---|
| Foreign Currency & FCDAs *(≤3-month maturity)* | $4,246,121,681.56 | **$4,555,754,242.56** |
| Other Investments, Net *(FX, >3-month maturity)* | $14,695,592,736.31 | **$14,279,183,257.16** |
| **= Total ESF foreign currency** | **$18.94B** | **$18.83B** |
| **Nonmarketable U.S. Treasury securities** *(dollar asset)* | $23,589,785,713.60 | **$24,452,039,297.08** |
| Fund Balance with Treasury | $206,823,240.46 | **$1,043,693,303.86** |
| **SDR holdings** | $172,586,424,500.11 | **$172,061,985,325.41** |
| *of which* SDR certificates issued to Federal Reserve Banks | $15,200,000,000.00 | **$15,200,000,000.00** |

**Three things follow:**

1. **ESF FX was FLAT across the quarter into the operation** ($18.94B → $18.83B, a −0.6% move consistent with revaluation). **There was no pre-op drawdown.** Any story requiring a depleted ESF going into 7/31 is refuted.
2. **The ESF holds ~$25.5B of dollar assets** (nonmarketable USTs + FBWT) it can redeem to buy yen directly, entirely bypassing the euro leg.
3. **The SDR position is $172.06B with only $15.2B monetized** as certificates to the Federal Reserve Banks. ⚠️ **SAM is NOT claiming the ~$157B remainder is freely drawable** — SDR monetization has its own statutory and IMF-facing constraints that this document did **not** verify. It is stated only to establish the **order of magnitude of the resource stack** the "ceiling" was measured against.

### And warehousing is explicitly authorized, with no numeric cap in the current text

**FOMC *Authorization for Foreign Currency Operations*, ¶4 (own pull, primary):**

> *"The Committee authorizes the Selected Bank, **with the prior approval of the Subcommittee and at the request of the U.S. Treasury**, to conduct swap transactions with the United States Exchange Stabilization Fund… in which the Selected Bank **purchases foreign currencies from the Exchange Stabilization Fund** and the Exchange Stabilization Fund repurchases the foreign currencies… at a later date (such purchases and sales also known as **warehousing**)."*

**No dollar limit appears in the paragraph** — only Subcommittee approval. *(A numeric warehousing limit existed historically; SAM did not find one in the current authorization text and is not asserting either that it is uncapped in practice or that a cap exists elsewhere.)* Warehousing lets Treasury convert FX into dollars **at the Fed rather than in the market** — i.e. it monetizes the euro book without a euro-market footprint, which is precisely the constraint the "must sell French OATs" scenario assumed away.

**⇒ Table 1's own footnote confirms warehousing is a live component:** *"Net purchases and sales include foreign currency purchases related to official activity, repayments, **and warehousing**."*

---

## 4. THERE **IS** A REAL CONSTRAINT — AND IT IS A COMMITTEE VOTE, NOT A BALANCE SHEET

**FOMC *Authorization for Foreign Currency Operations*, ¶3.A — STANDALONE SPOT AND FORWARD TRANSACTIONS:**

> *"i. **The Committee must direct** the Selected Bank in advance to execute the operation if it would result in the overall volume of standalone spot and forward transactions in foreign currencies… **exceeding $5 billion since the close of the most recent regular meeting of the Committee.** The Subcommittee must direct… if the Subcommittee believes that consultation with the Committee is not feasible in the time available.*
> *ii. The Committee authorizes the **Subcommittee** to direct… if it would result in the overall volume… **totaling $5 billion or less** since the close of the most recent regular meeting."*

> *"B. Such an operation also shall be: i. **Generally directed at countering disorderly market conditions**…"*

🔴 **Three observations, and the third is the sharp one.**

1. **The $5B line is a decision-RIGHTS threshold, not a resource ceiling.** Up to $5B per inter-meeting period the **Foreign Currency Subcommittee** can direct the Desk; **above $5B the FULL FOMC must direct it in advance.**
2. **Bessent's notepad read "Buy JPY $5-10 bil" — astride exactly that line.** A $5-10B SOMA-leg operation is the difference between a subcommittee sign-off and a full-Committee direction, on a **Warsh FOMC that has just produced its first unified 3-dissent hold since Sep-2016.** *(SAM is not claiming this gate was invoked — see the caveat below.)*
3. **The public justification language is lifted from the authorization.** Bessent 8/2: *"Friday's coordinated foreign exchange actions **countered disorderly yen movements**."* ¶3.B.i: *"generally directed at **countering disorderly market conditions**."* **The statement was written to the authorization's own eligibility test.** ⚠️ This also means the "disorderly" framing is a **legal-authority formula, not a market diagnosis** — it should not be read as an official characterisation of the tape, which is how SAM's own `MOF_INTERVENTION_PLAYBOOK` reaction-function work has been treating that word class.

⚠️ **SCOPE CAVEAT, AND IT IS LOAD-BEARING: the Foreign Authorization governs the SOMA — the Fed's account. It does NOT govern the ESF**, which answers to the Secretary of the Treasury. **A Treasury-only operation faces no FOMC threshold at all.**

---

## 5. TWO DATA-QUALITY CORRECTIONS ANY FUTURE READER NEEDS

**(a) The ESF publishes MONTHLY, not quarterly.** WALTER `-014` §3 stated *"NO Q2-2026 ESF balance sheet in the wires I have"* and treated the 3/31 snapshot as unavoidably stale. **Treasury has published `ESF Monthly Financial Statement` continuously; the June-2026 statement was public well before 8/9.** The constraint could have been re-based to one month before the operation at any time. *(Class: [[finding_unfetched_is_not_unavailable]] — PUBLIC-AND-UNFETCHED was recorded as unavailable.)*

**(b) 🔴 THE ESF BALANCE SHEET AND THE FX QUARTERLY REPORT APPEAR TO DISAGREE BY 4.5× ON THE SAME DATE. THEY RECONCILE — AND CITING THE WRONG ONE UNDERSTATES ESF FX BY ~$14B.**

- ESF balance sheet, "Foreign Currency and Foreign Currency Denominated Assets", 3/31/2026: **$4.25B**
- FX quarterly Table 2, ESF total FX, 3/31/2026: **$19.05B**

**The reconciliation is a maturity split, stated in the ESF's own Note 2:**

> *"Foreign Currency and Foreign Currency Denominated Assets (FCDAs) represent deposits and investments in foreign government securities, denominated in euro and yen, that have **original maturities of three months or less**. **Other Investments are FCDAs that have maturities of greater than three months.**"*

$4,246.1M **+** $14,695.6M = **$18,941.7M** vs Table 2's **$19,050.3M** — a $108.7M residual consistent with accrued interest (Table 1 note *a*: carrying value *"includes interest accrued on foreign currency"*).

⚠️ **So the ESF's headline "Foreign Currency" line is only the ≤3-month sleeve. Anyone quoting it as ESF FX capacity is off by a factor of four.** The two documents are different cuts of one portfolio, not conflicting measurements.

**(c) Provenance oddity, flagged and NOT interpreted:** the published Q1-2026 FX quarterly PDF, served from the NY Fed's own public medialibrary path, carries **"INTERNAL FR/OFFICIAL USE // FRSONLY"** watermarking on every page. Content is the standard public report and the press release is public. Recorded as an observation only.

---

## 6. THE QUESTION THAT IS ACTUALLY OPEN — AND IT IS NOT ABOUT MONEY

The Q1-2026 FX quarterly contains this, and it is the most decision-relevant sentence SAM found all session:

> *"In January, amid continuing yen depreciation, market participants were attentive to press reports that the Federal Reserve Bank of New York had made requests for indicative quotes—commonly referred to as **'rate checks'**—on the dollar–yen exchange rate **solely on behalf of the U.S. Treasury** in the New York Fed's role as the fiscal agent of the U.S. The yen appreciated 1.7 percent against the dollar on the day these press reports were in focus."*

**Two things SAM did not previously have:**

1. **US rate-checks on USD/JPY were already running in JANUARY 2026** — six months before the July operation. SAM's `MOF_INTERVENTION_PLAYBOOK` treats rate-checks as a **Japanese** tell; there is a **US** rate-check precedent on the record, and it moved the yen 1.7% on the report alone.
2. **"Solely on behalf of the U.S. Treasury"** — i.e. **ESF, with no Fed/SOMA leg.**

🔴 **THE REAL OPEN QUESTION IS BINARY AND IT IS ABOUT PARTICIPATION, NOT CAPACITY: is the Fed in, or is this a Treasury-only file?**

| | If **Treasury/ESF-only** | If **joint ESF+SOMA** |
|---|---|---|
| US FX resources | ~$18.8B FX + ~$25.5B dollar assets | ~$38.1B FX + ESF dollar assets |
| $5B FOMC decision gate | **Does not apply** | **Applies to the SOMA half** |
| What a repeat op needs | The Secretary's decision | A Warsh-FOMC direction above $5B |
| Reading of Fed absence | The Fed is deliberately abstaining from the yen file under a hawkish 3-dissent board | n/a |

**Either branch leaves the operation comfortably funded.** The branches differ in *who has to agree*, and under a Warsh Fed that is the harder currency.

---

## 7. RETRACTION AND ROUTING

**RETRACTED:** *"The US leg of the two-sovereign intervention regime has a balance-sheet ceiling"* — published by SAM 2026-08-10 to `STATUS.md` §5, `NEXUS_BRIEF.md` (CURRENT STATE + a SENDING row to **BOND**), `MEMORY.md`, and the packet `AGENTS/WALTER/inbox/2026-08-10_from-SAM_answers-to-three-asks…` §4.

**REPLACED BY:** there is no balance-sheet ceiling at the $5-10B scale. The binding constraints are **(i)** a $5B **FOMC decision-rights** threshold on the **SOMA leg only**, and **(ii)** whatever political price attaches to Fed or Treasury participation.

**Specifically withdrawn — the OAT flow-class claim routed to BOND:** *"if the ESF must sell to fund a repeat op, a US-Treasury-agent seller enters the OAT-Bund curve."* **Withdrawn.** With combined euro cash of $11.49B, ~$25.5B of ESF dollar assets, and uncapped-in-text warehousing available, **there is no forced-OAT-sale scenario at the notepad's scale.** ⚠️ It survives only as a *tail* conditional on an operation an order of magnitude larger than anything discussed.

**Consequence for the thesis watch — and it makes the signal CLEANER, not weaker:** SAM's 8/10 watch item ① asked what a USD/JPY re-entry above 160 would mean. **"They are out of ammunition" is now unavailable as an explanation.** If officials do not act into renewed yen weakness, that is a **willingness** signal, not a **capacity** signal — which is strictly more informative, because capacity constraints are mechanical and willingness is a statement about intent.

**And it sharpens the Kyodo conditionality claim** (`SIG-W-20260810-002`, single-wire, unadopted): if US participation was conditioned on a BOJ September hike, the price the US charged was **Japanese monetary policy, not dollars**. A **resource-cheap but politically expensive** operation is exactly the shape in which you would expect a quid-pro-quo to appear. **This does not confirm Kyodo** — it removes the "they needed the money" alternative explanation for why a price was charged.

---

## 8. WHAT THIS DOCUMENT DOES **NOT** ESTABLISH

- **The Japanese leg.** MOF/BOJ dollar-raising capacity, FIMA take-up, and whether Japan used FIMA on 7/30-31 are **not answered here.** FIMA take-up is reported in the Fed's H.4.1 ("Repurchase agreements — foreign official") and would be the instrument. **Open.**
- **Whether the 7/31 operation used SOMA at all.** No public document yet covers July. **See the catalyst below.**
- **The size of the US leg.** Still undisclosed; the $58.97B press figure remains unreconciled and unadopted, and the −¥11.42T Aug-4 settlement remains a **fiscal-factor line, not a size**.
- **SDR monetization availability.** Order-of-magnitude only; statutory constraints unverified.
- **Whether a warehousing cap exists outside the authorization text.**

---

## 9. 🔴 REGISTERED CATALYSTS — this gets settled on a published schedule

NY Fed quarterly FX reports publish **mid-February / mid-May / mid-August / mid-November** (verified: 2025-05-15, 2025-08-14, 2025-11-13, 2026-02-12, 2026-05-14).

| Date | Event | What it settles |
|---|---|---|
| 🟠 **~Fri Aug-14 2026** *(4 days out)* | **FRBNY Q2-2026 FX quarterly** (Apr-Jun) | ⚠️ **PREDATES the op** — will report no Q2 intervention. **Value = a fresh 6/30 ESF *and* SOMA reserve snapshot**, i.e. the best pre-op baseline against which the Q3 report's change can be read. Also lands the same day as the CFTC print (Aug-11 data) |
| 🔴 **~Fri Nov-13 2026** | **FRBNY Q3-2026 FX quarterly** (Jul-Sep) | **THE DEFINITIVE PUBLIC RECORD OF THE 7/30-31 OPERATION**: the ESF-vs-SOMA split, the size via Table 1 "Net Purchases and Sales", the currencies sold, and whether warehousing was used. **This is what answers §6.** |
| 🟠 ~Aug-31 2026 | MOF monthly intervention data (Jul-30→Aug-27) | The **Japanese** leg's size — already on SAM's docket |
| 🟡 monthly | ESF Monthly Financial Statement (Jul-2026 → ~late Aug) | First ESF book to include the op: watch **FCDA + Other Investments** *together*, never the headline line alone (§5b) |

---

## SOURCES (all own pulls, 2026-08-10)

- FRBNY, *Treasury and Federal Reserve Foreign Exchange Operations, January-March 2026* — Tables 1, 2, 3 + narrative. `newyorkfed.org/medialibrary/media/newsevents/news/markets/2026/q1-2026-fx-quarterly-report.pdf`
- US Treasury, *ESF Monthly Financial Statement* for **June 2026** and **March 2026**, incl. Notes 1-3. `home.treasury.gov/policy-issues/international/exchange-stabilization-fund/esf-reports`
- FOMC, *Authorizations and Continuing Directives for Open Market Operations* — §III Authorization for Foreign Currency Operations ¶¶1-5. `federalreserve.gov/monetarypolicy/files/FOMC_AuthorizationsContinuingDirectivesOMOs.pdf`
- Federal Reserve Board, *FIMA Repo Facility* policy-tools page (last update 2022-03-24). `federalreserve.gov/monetarypolicy/fima-repo-facility.htm`
- FRBNY quarterly-report index pages (publication-cadence verification). `newyorkfed.org/markets/quar_reports`

⚠️ **Retrieval note:** `newyorkfed.org` and `home.treasury.gov` both returned **403 / timeout to the default fetcher** and resolved cleanly under `curl` with a browser User-Agent ([[finding_edgar_403_user_agent_header]]). A block on the default path is **not** an unreachable primary ([[finding_blocked_mirror_is_not_an_unreachable_primary]]).
