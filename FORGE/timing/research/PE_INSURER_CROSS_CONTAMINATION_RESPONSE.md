# PE-insurer stress transmission: a timeline model of cascading failure

**The most dangerous systemic risk in PE-insurer funding is not the $276B FABN market — it's the $18.5B FABR channel that breaks first and tests whether the FHLB system backstops or tightens.** The distinction between these two outcomes separates a slow-motion, multi-quarter workout from a weeks-long cascade that could force fire sales of illiquid private credit, reprice affiliated assets across every PE-insurer balance sheet, impair Apollo's $938B asset management empire, and trigger the first insurance "run" since Eurovita in 2023. The monoline crisis benchmark shows 35 days from first rating watch to first downgrade, and 9 months to systemic peak — but modern PE-insurer funding structures are both more fragile (FABR has no contractual delay mechanism) and more resilient (bullet FABNs cannot be put) than monolines were. The single most dangerous feedback loop is **forced liquidation of affiliated ABS → mark contagion across PE-insurers holding identical paper → RBC ratio compression → regulatory tripwires → accelerated surrenders** — a doom loop with no natural circuit breaker once it begins.

---

## Section 1: The monoline benchmark establishes the speed of cascade

The monoline insurer crisis (AMBAC, MBIA, FGIC) provides the clearest precedent for how a concentrated financial guarantee sector transmits stress to banks. The timeline reveals two distinct phases: a **5-year denial period** followed by a **9-month collapse**.

**Phase 0 — Early warning ignored (Dec 2002–Nov 2007).** Bill Ackman published his 66-page report "Is MBIA Triple-A?" on December 9, 2002, via Gotham Partners. MBIA's CEO allegedly threatened him. The SEC and NY Attorney General Eliot Spitzer investigated Ackman (not MBIA) for six months in 2003. It took until autumn 2004 for MBIA to receive subpoenas, 2005 for MBIA to restate seven years of earnings and pay a **$75 million fine**, and end-of-2005 for Ackman to write directly to Moody's board warning that the AAA rating was enabling uninformed investment. Throughout this period, all three rating agencies maintained AAA on all major monolines while the companies *expanded* their CDO/structured finance guarantees.

**Phase 1 — Rating agency action to first downgrade: 35 days.** Moody's placed FGIC and XL Capital Assurance on review for downgrade on **December 14, 2007**. Fitch followed on December 17, S&P on December 19. By late December, Fitch had placed Ambac, MBIA, and FGIC on review. The first actual AAA downgrade came **January 18, 2008** when Fitch cut Ambac to AA after the insurer scrapped a $1 billion equity issuance. FGIC lost AAA at Fitch on January 30 and S&P on January 31. MBIA lost AAA at Fitch on April 4, 2008.

**Phase 2 — Downgrades to bank writedowns: concurrent to 6 months.** Banks were already taking monoline-related credit valuation adjustments (CVAs) in Q4 2007, before formal downgrades. Citigroup recorded $967 million in monoline CVA losses for full-year 2007. The peak hit in Q2 2008: Merrill Lynch wrote down **$2.9 billion** specifically from monoline exposure; Citigroup took **$2.4 billion** in monoline CVAs. Citigroup's total monoline-related losses reached **$5.7 billion** across 2008. Merrill's total crisis writedowns exceeded $40 billion.

**Phase 3 — Final AAA loss to systemic crisis: 3 months.** S&P cut both MBIA and Ambac from AAA on **June 5, 2008**. Moody's followed with a 5-notch cut of MBIA (Aaa to A2) and 3-notch cut of Ambac (Aaa to Aa3) on **June 19, 2008**. Lehman Brothers filed bankruptcy on September 15, 2008. The monoline downgrades triggered automatic rating cuts on **$2.4+ trillion** in insured municipal bonds, disrupting the auction-rate securities market and forcing banks to hold more regulatory capital.

| Metric | Duration |
|--------|----------|
| First watch → first AAA downgrade | **35 days** |
| First downgrade → peak bank writedowns (Q2 2008) | **~6 months** |
| First watch → final AAA loss (MBIA/Ambac) | **~6 months** |
| First watch → peak systemic crisis (Lehman) | **~9 months** |
| Ackman's first warning → peak crisis | **~5 years, 10 months** |

---

## Section 2: RBC regulatory tripwires and where PE-insurers stand today

The NAIC Risk-Based Capital framework, codified in **Model #312 (Risk-Based Capital for Insurers Model Act)**, defines four escalating intervention thresholds based on Total Adjusted Capital (TAC) relative to Authorized Control Level (ACL) RBC. Companies typically report on the CAL basis (TAC ÷ Company Action Level RBC), where the Company Action Level threshold equals **100%**.

| Level | ACL Basis | CAL Basis | NAIC Model #312 Section | Triggered Action |
|-------|-----------|-----------|------------------------|------------------|
| **Trend Test Zone** | 200–300% | 100–150% | §3 | Trend test applied; if failed → Company Action Level |
| **Company Action Level** | <200% | <100% | §3 | Insurer must submit corrective RBC Plan within 45 days |
| **Regulatory Action Level** | <150% | <75% | §4 | Commissioner required to examine; may issue corrective orders |
| **Authorized Control Level** | <100% | <50% | §5 | Commissioner authorized to seize insurer (rehabilitation/liquidation) |
| **Mandatory Control Level** | <70% | <35% | §6 | Commissioner **required** to seize; may delay up to 90 days |

A typical well-capitalized life insurer operates at **350–500% CAL**. Mutual insurers average **514%**, public stock-owned average **415%**, reinsurers average **298%**.

**Current PE-insurer positions (CAL basis):**

| Entity | RBC Ratio (CAL) | Date | Rating | Buffer Above Company Action |
|--------|----------------|------|--------|---------------------------|
| **Athene (Apollo)** — AAIA, Iowa | **419%** | YE 2024 | A+ (S&P/Fitch/AM Best), A1 (Moody's) | 319 points |
| **F&G (FNF)** — Iowa | **~430%** | YE 2025 | A (AM Best) | 330 points |
| **Global Atlantic (KKR)** — MA | Not disclosed; AM Best "strong" BCAR | — | A- (S&P/Fitch), A (AM Best) | Unknown |
| **Everlake (Blackstone)** — IL | Not disclosed; AM Best "strongest" BCAR | — | A (AM Best) | Unknown |

These ratios appear comfortable — **319–330 points above Company Action Level**. However, the influential Foley, Goldstein, Sarin, and Weber (2020) paper found that adjusting for the actual risk composition of private-label ABS holdings (rather than NAIC designations), the **adjusted median RBC for PE-owned insurers dropped to ~330%**, with the **25th percentile at only ~150%** — perilously close to Regulatory Action Level. The NAIC has since reformed structured securities treatment (45% residual tranche charge adopted 2024; principles-based bond definition effective January 1, 2025; CLO modeling project expected 2026), but the fundamental question of whether NAIC designations accurately reflect private credit risk remains contested.

---

## Section 3: The FHLB backstop-or-tightens question is the critical branching point

**Historical precedent overwhelmingly supports FHLB-as-backstop.** In 2007–08, FHLB advances to insurers surged by approximately **$20 billion**, replacing roughly three-quarters of lost FABN funding. In March 2020, insurers drew **~$20 billion** in new FHLB advances within a single quarter. The SVB/First Republic episode in 2023 — often cited as a "FHLB tightening" precedent — actually shows the opposite: FHLB San Francisco **increased** lending to SVB from $20 billion to **$30 billion** in SVB's final nine days, and increased lending to First Republic from $19.4 billion to **$28.1 billion**. FHLBs never demanded additional collateral, refused to roll, or called advances from any of these institutions. Per the GAO report (GAO-24-106957, March 2024), SVB failed before FHLB could even coordinate with the Fed to facilitate additional funding.

**There is no statutory single-member lending limit for FHLBs** — a critical structural feature. Per CRS Report R46499: "Commercial banks cannot lend more than 25% of equity to a single borrower, but FHLBs are not limited on advances to an individual member." Each FHLB sets internal credit limits. FHLB Des Moines, where Athene is a member, reported Athene at **13% of total advances** ($12.4 billion) as of Q3 2024. By year-end 2025, Athene had **$23.3 billion** in FHLB advances — the **second-largest FHLB borrower in the entire system**, behind only Truist Financial.

**But the backstop has hard limits.** Athene reports only **~$7.4 billion** in additional FHLB borrowing capacity. The binding constraint is collateral: corporate bonds, private credit, and CLOs — the core of Athene's investment strategy — are **not eligible FHLB collateral**. Only agency MBS, CMBS, Treasuries, and similar housing-related securities qualify, and insurers must **physically deliver** collateral (unlike banks using blanket liens) because FHLB's super-lien position is uncertain in state insurance insolvency proceedings. If Athene needed to replace a **$48 billion** combined FABN + FABR gap, FHLB could plausibly provide an additional $7–15 billion — but not $48 billion. The total increase in FHLB advances to *all insurers combined* in 2007–08 was roughly $20 billion.

Under 12 CFR §1266.4, an FHLB **may limit or deny** advances based on unsafe practices, financial deficiencies, or "any other deficiencies as determined by the Bank." An FHLB can also increase haircuts, demand physical collateral delivery, and restrict product types. While no documented case exists of FHLBs systematically tightening on insurers, the discretion exists, and a Chicago Fed Letter (2014) notes insurers' concern that "an FHLB might require additional collateral if the insurance company's financial performance deteriorates — limiting flexibility at the very time advances could be most useful."

---

## Section 4: The two-branch timeline model

### Branch A: FHLB backstops (slow cascade — quarters to years)

This branch assumes FHLBs expand lending to stressed PE-insurers, as in 2007–08 and 2020, absorbing FABR and partial FABN runoff.

| Stage | Timeline | Magnitude | Mechanism | Self-reinforcing or self-limiting? |
|-------|----------|-----------|-----------|-----------------------------------|
| **1. FABR non-renewal begins** | Weeks 1–4 | $5–18B industry; ~$5–8B Athene | Bank counterparties decline to roll repo as credit concerns mount | Self-reinforcing initially; banks watch each other |
| **2. FHLB absorbs FABR gap** | Weeks 2–8 | $10–20B new FHLB advances industry-wide | Insurers draw on FHLB capacity using eligible collateral | Self-limiting — FHLB is a willing lender within collateral constraints |
| **3. FABN refinancing wall approaches** | Months 3–18 | $155B by YE 2028 (56% of FABNs maturing) | Non-puttable bullets mature; market may refuse to buy new issuance | Slow-burning — each maturity is a discrete event |
| **4. Gradual asset repositioning** | Months 6–24 | $20–50B portfolio rebalancing | Insurers sell liquid assets, reduce private credit allocation | Self-limiting if orderly; generates modest marks |
| **5. Regulatory engagement** | Months 6–18 | — | State commissioners monitor RBC, may require corrective plans | Self-limiting — state regulation is decentralized, slow |
| **6. Policyholder surrenders (moderate)** | Months 12–36 | 5–15% of annuity book | Elevated but manageable surrenders as blocks exit surrender charge periods | Self-limiting if insurer remains investment-grade rated |

**Total elapsed time: 12–36 months from trigger to resolution.** This resembles the GE Capital exit — a slow, managed wind-down where no single event is catastrophic.

### Branch B: FHLB tightens (fast cascade — weeks to months)

This branch assumes FHLB haircuts collateral, caps advances, or refuses to increase lending — triggered by, for example, NAIC re-rating of private credit assets, a major credit event in Athene's portfolio, or FHFA directive to limit insurer concentration.

| Stage | Timeline | Magnitude | Mechanism | Self-reinforcing or self-limiting? |
|-------|----------|-----------|-----------|-----------------------------------|
| **1. FABR non-renewal** | Days 1–14 | $5–18B | Bank counterparties stop rolling repo; no contractual delay | **Self-reinforcing** — each bank's exit signals risk to others |
| **2. FHLB refuses to expand / haircuts collateral** | Days 14–30 | $7–15B gap unfilled | FHLB demands physical collateral delivery; private credit ineligible; haircuts increase on remaining eligible assets | **Self-reinforcing** — declining asset values reduce collateral capacity |
| **3. Forced liquidation of affiliated ABS** | Days 30–90 | $15–30B in forced sales at 70–80¢ | Illiquid secondary market; bid-ask spreads of several percentage points; limited buyer universe | **Strongly self-reinforcing** — fire sale prices become reference marks |
| **4. Cross-insurer mark contagion** | Days 45–120 | $50–100B in mark-to-market losses industry-wide | Global Atlantic, F&G, Everlake hold similar affiliated paper; auditors/regulators force re-marks | **Self-reinforcing** — identical assets held by correlated institutions |
| **5. RBC ratio compression** | Days 60–150 | Multiple PE-insurers approach Company Action Level | 45% charge on residual tranches; re-rated assets consume capital | **Self-reinforcing** — approaching regulatory thresholds accelerates outflows |
| **6. Apollo parent impairment** | Days 60–180 | $3.4B ANI at risk; 54% from Athene SRE | Athene AUM shrinks → fee income drops; rating agencies reassess Apollo HoldCo | Self-reinforcing but with limits — Apollo has $3.4B HoldCo cash |
| **7. Policyholder surrender acceleration** | Days 90–365 | 15–40% of liquid annuity book | Headlines trigger surrender wave; past-surrender-charge blocks withdraw; Eurovita-style regulatory freeze possible | **Self-reinforcing** — the classic insurance run dynamic |

**Total elapsed time: 60–180 days from trigger to peak systemic impact.** This resembles the monoline timeline compressed, but with the critical distinction that FABNs' non-puttable structure provides a floor — unlike monoline CDS which could be terminated.

---

## Section 5: The cascade map — FABR breaks first, then everything depends on FHLB

### Stage 1: FABR fails first (the $18.5B detonator)

FABRs are the clear first-to-break funding channel because they have the **shortest effective maturity**, the **most concentrated counterparty base** (banks, likely a handful), and **no contractual delay mechanism**. Unlike historical XFABNs which gave investors ~1-year "spinoff" securities upon withdrawal, FABR repos simply mature and are not rolled. The bank counterparty can exit at each maturity date.

Athene established its FABR program in Q3 2020 at $1 billion. It grew to **$5.5 billion** by year-end 2023. Industry-wide FABR outstanding reached **$18.5 billion** by March 2025. FABR counterparties are banks that receive favorable capital treatment on these structures — but bank repo desks operate under tight risk limits and can cut exposure instantly in stress.

**Historical precedent:** General American Life Insurance Company experienced a classic funding agreement run in **August 1999** when money market funds holding puttable funding agreements demanded their money back. Missouri's insurance commissioner seized the company. Even after MetLife announced an acquisition (implying MetLife's creditworthiness would backstop the agreements), **MMFs still demanded their money** — demonstrating the self-fulfilling nature of funding agreement runs. Foley-Fisher et al. (JPE, 2020) confirmed that at least **40% of the 2007 XFABN run was self-fulfilling**.

The FABR run timeline: **Days 1–7**, repos mature and are not rolled; **Days 7–30**, insurer draws FHLB advances as emergency liquidity (the established 2007/2020 playbook); **Days 30–90**, if stress persists and FHLB capacity is exhausted, forced asset sales begin. Athene holds only ~$10.5 billion in cash and cash equivalents (**3.6% of net invested assets**) — the FABR alone could consume this buffer.

### Stage 2: FHLB backstop tested (the $21–23B lifeline)

Athene's **$23.3 billion** in existing FHLB advances (year-end 2025) makes it the largest insurer FHLB borrower and the second-largest borrower in the entire system. Additional capacity is approximately **$7.4 billion**. The binding constraint is eligible collateral: only housing-related securities (agency MBS, CMBS, Treasuries) qualify, and insurers must physically deliver them.

If FHLB absorbs the FABR gap (~$5–8B for Athene), the crisis stabilizes temporarily. Athene's $7.4 billion capacity is roughly sufficient for its FABR exposure alone. But if the FABN market simultaneously closes — preventing refinancing of maturing bullets — the combined gap ($5–8B FABR + $30B FABNs maturing by 2028) overwhelms FHLB capacity by a factor of 4–5x.

**The FHLB system itself could face stress.** In September 2008, after GSE conservatorship, money market funds became less willing to buy FHLB debt. FHLB debt outstanding shrank rapidly, requiring the Fed to purchase $14.5 billion in FHLB obligations. FHLB Boston, Chicago, and Seattle all reported negative net income. If PE-insurer stress coincides with broader market stress, the backstop itself may be constrained.

### Stage 3: Forced liquidation of affiliated assets (the $15–30B fire sale)

The secondary market for Apollo-originated, Athene-held private credit ABS is **thin, opaque, and illiquid**. These are OTC bilateral markets with no pre-trade transparency. Bid-ask spreads in private credit can reach **"several percentage points, sometimes even double digits"** per Nasdaq Private Market research. In a fire sale scenario, discounts of **10–30%** are plausible — far exceeding the **6.87% fire sale discount** BIS estimated for UK gilts (high-quality sovereign bonds) during the 2022 LDI crisis.

The buyer universe is severely constrained: opportunistic/distressed credit funds (capacity-limited), other PE-insurers (holding similar paper and facing similar pressures), sovereign wealth funds (weeks to months to deploy), and bank trading desks (Volcker Rule-constrained). The "affiliated" nature of the paper adds a further discount — buyers question arm's-length origination, fair marking, and affiliate-friendly terms.

**Recent stress events confirm illiquidity:** In early 2026, Blue Owl gated withdrawals from a retail credit vehicle; an Apollo-managed BDC cut its payout and marked down assets; Blackstone's private credit fund raised its repurchase cap to meet ~$2 billion in redemptions.

### Stage 4: Mark contagion across PE-insurers (the $50–100B repricing)

**"Marks are contagious"** is the central transmission mechanism. When Merrill Lynch sold CDOs at **22 cents on the dollar** in 2008, it established a market-clearing price that forced every other CDO holder to re-mark. The same dynamic would apply if Athene liquidated Apollo-originated ABS at 70–80 cents: Global Atlantic (KKR), F&G (FNF), Everlake (Blackstone), and Corebridge (Blackstone) — all holding similar affiliated paper — would face pressure from auditors, regulators, and rating agencies to mark to observed transaction prices.

The concentration is extreme. Per Moody's (November 2025), illiquid investments account for **18% ($685 billion)** of the U.S. life insurance industry's $3.8 trillion fixed income holdings. **Ten life insurers account for 43% of all illiquid assets.** The IMF found PE-backed insurers hold **almost twice as much** in illiquid assets as traditional insurers.

The 2022 UK LDI crisis provides the closest modern analog for a mark-contagion doom loop. **£25 billion** in gilt sales over five weeks — with **30% of sales in the first 5 days** — pushed yields up by over 100 basis points in 4 days, triggering margin calls that forced more sales. Just **3 firms accounted for 70% of total sales**. The Bank of England was forced to intervene with £19.3 billion in emergency purchases. Transaction costs **more than doubled within days** and contagion spread to non-LDI clients and short-dated bonds.

### Stage 5: Apollo parent company impairment

Apollo's dependence on Athene is profound. In FY2025, Athene's Spread Related Earnings (SRE) of **$3,361 million** represented **54% of Apollo's total segment income** ($6,227 million) and **65% of per-share adjusted net income** ($5.43 of $8.38). Apollo manages **100% of Athene's $292 billion** in net invested assets. Athene accounts for **$392 billion** of Apollo's $536 billion in perpetual capital AUM — the bedrock of recurring fee income.

A **30% decline in Athene AUM** would cut SRE by ~$1 billion, dropping Apollo's ANI by ~19% to ~$6.76/share. This would "almost certainly trigger a ratings downgrade" at both Athene and Apollo. A **50% decline** would be "catastrophic" — likely multi-notch downgrades and potential covenant issues on Apollo's $5.5 billion HoldCo debt.

Critically, Apollo's other funds hold the same or similar assets. Apollo Aligned Alternatives has **$14 billion** of Athene NAV invested alongside $11 billion of third-party capital. Apollo's $749 billion credit AUM encompasses direct origination, CLOs ($47.4 billion), and asset-backed finance — overlapping substantially with Athene's portfolio. If Athene's forced sales establish fire-sale marks, Apollo's third-party funds face redemptions and markdowns simultaneously.

One structural protection: Athene Holding Ltd. **does not guarantee** Apollo's senior notes. Apollo HoldCo is structurally subordinated to Athene's creditors and policyholders.

### Stage 6: Policyholder surrender — the actual "run" (the $50–200B bank run equivalent)

FABNs cannot run — they're non-puttable bullets. But policyholders **can** surrender fixed annuities. Typical surrender charges decline from **7–10% in Year 1** to 0% by Year 8–11. After the surrender period expires, policyholders can withdraw **100% without penalty** (tax consequences still apply). Free withdrawal provisions during the surrender period typically allow **10% annually** without charges.

Historical precedents are stark:

- **Executive Life of California (1991):** Held $9 billion in junk bonds (largest % of any insurer). Drexel Burnham's February 1990 failure accelerated a junk bond collapse. Policyholder runs intensified. Seized **April 11, 1991**. Court records describe "the equivalent of a 'run on the bank' — policyholders whose contracts permitted were cashing out, requiring ELIC to dispose of its better investments." **75,040 annuitants received only 70 cents on the dollar.** Some waited until 2005+ for full resolution.

- **Mutual Benefit Life (1991):** $14 billion in assets, 700,000 customers, heavy commercial real estate exposure. Seized **July 16, 1991** "to prevent a run on its assets." At the time, the largest-ever American insurer collapse. Not fully liquidated and dissolved until **June 14, 2001** — a 10-year process.

- **Eurovita (Italy, 2023):** Owned by PE firm Cinven. Rising rates pushed solvency ratio from ~230% to near 130%. Surrenders accelerated. IVASS imposed a **six-month surrender freeze** — policyholders literally locked out. Five Italian insurers eventually assumed policies.

The trigger sequence observed historically: investment losses surface → media coverage → rating downgrades → agent channel disruption (agents stop selling the company's products) → surrender acceleration → forced asset sales → further losses → **self-reinforcing spiral** → regulatory seizure.

**The pari passu problem:** FABNs rank **equally with policyholders** in insolvency — both are Class 2 claims competing for the same general account assets (per state insurance insolvency statutes, e.g., Washington RCW 48.31.280, Delaware Title 18 §5918). With **$276.8 billion** in FABNs outstanding industry-wide as of September 2025, policyholder recoveries in any PE-insurer insolvency would be materially diluted. State guaranty funds cap coverage at **$250,000 per person per insurer** (NAIC Model #520). NOLHGA has guaranteed **$30.4 billion in total coverage** since 1983 across all insolvencies combined — a single $200B+ PE-insurer failure would represent **6.5x the system's entire 40-year track record**.

### Stage 7: Cross-counterparty chain — the reinsurance web amplifies

The PE-insurer ecosystem is deeply interconnected through reinsurance. F&G's September 2024 10-Q reveals **$12.4 billion** in reinsurance recoverables, growing **38% in just 9 months**:

- **Aspida Re (Ares/PE-backed): $7.5 billion** — 61% of total recoverables
- **Somerset Reinsurance: $2.2 billion** — tripled in 9 months  
- **Everlake (Blackstone/PE-backed): $1.1 billion**
- Combined PE-backed reinsurer exposure: **~$8.7 billion (70% of total)**

F&G itself discloses this as a "significant concentration of reinsurance risk." If a credit cycle downturn impairs private credit assets simultaneously, the ceding insurer (F&G) and its PE-backed reinsurers (Aspida, Everlake) face correlated stress. Reinsurance recoverables can become impaired — reinsurers are not backed by guaranty funds. Related-party investment exposure across PE-insurers ranges from 12% (Athene) to **43% (Security Benefit)**.

The Egan-Jones ratings probe adds an accelerant. The SEC's Complex Financial Instruments Unit is investigating whether Egan-Jones (which rated **3,000+ private credit investments in 2024 with only 20 analysts**) exerted improper commercial influence on ratings. Bermuda's monetary authority **removed Egan-Jones from its approved providers list** in January 2026. If NAIC re-rates private credit assets currently carrying Egan-Jones designations, RBC ratios across multiple PE-insurers could compress simultaneously.

---

## Section 6: Which branch is more likely in 2026 conditions?

**The FHLB-backstops branch remains the base case**, but with lower confidence than historical precedent alone would suggest. Four factors favor backstop: FHLBs have never tightened on insurers as a class; the super-lien protects FHLBs' own credit; FHLB Des Moines has institutional familiarity with Athene after 12 years of membership; and FHFA has no stated policy of restricting insurer access.

**Three factors tilt toward the tightens branch in 2026 specifically:**

1. **Collateral quality.** If NAIC SVO re-rating or the Egan-Jones investigation triggers reclassification of private credit holdings, Athene's eligible FHLB collateral shrinks. FHLB Des Moines would face pressure to increase haircuts on remaining collateral — potentially triggering the very "additional collateral demand during deterioration" that the Chicago Fed flagged insurers worry about.

2. **Concentration risk awareness.** Post-SVB, FHFA and Congress have scrutinized FHLB concentration. Athene is already the **second-largest FHLB borrower in the entire system**. A request to double borrowing would make Athene 25–30% of FHLB Des Moines total advances — a concentration that FHLB Des Moines' board may refuse.

3. **No Fed cutting room.** In 2007–08, the Fed cut rates from 5.25% to effectively zero, providing massive relief. In the current environment, with rates already elevated and inflation concerns constraining cuts, the Fed's ability to backstop the FHLB system (as it did with $14.5 billion in FHLB debt purchases in 2008) may be politically and operationally constrained.

**Assessment: 65% probability FHLB backstops (partially), 35% probability FHLB tightens.** The most likely outcome is a hybrid: FHLB absorbs some FABR runoff but refuses to cover the full FABN refinancing wall, forcing partial asset sales that are orderly enough to avoid the full doom loop but large enough to compress marks across the PE-insurer ecosystem. This "partial backstop" scenario plays out over **6–12 months** rather than the extremes of either branch.

---

## Section 7: The most dangerous feedback loop

**The single most dangerous feedback loop is: forced sale of affiliated ABS → mark contagion → RBC compression → regulatory tripwire → accelerated policyholder surrender → more forced sales.**

This loop is uniquely dangerous for five reasons. First, PE-insurers hold **correlated affiliated assets** — Apollo-originated ABS on Athene's books, KKR-originated on Global Atlantic's, Blackstone-originated on Everlake's — meaning fire-sale marks for one insurer's assets reprice assets held by all others. Second, the loop crosses the boundary between institutional funding (FABR/FABN) and retail liability (policyholder annuities), meaning stress that begins in wholesale markets can trigger a retail "run." Third, the reinsurance web means stress at one PE-insurer impairs recoverables at another — F&G's $7.5 billion Aspida Re recoverable could become impaired precisely when F&G itself is under pressure. Fourth, Apollo's dual role as asset manager and insurance parent means Athene's distress simultaneously impairs Apollo's fee income, Apollo's fund investors, and Apollo's own creditworthiness — creating a feedback between the insurance sector and the $938 billion alternative asset management complex. Fifth, there is **no natural circuit breaker**: state guaranty funds are inadequate ($30.4 billion lifetime capacity vs. $200B+ potential exposure), state regulation is decentralized and slow, and the Fed has no direct authority over insurance companies.

The only historical circuit breakers have been regulatory seizure (Executive Life, Mutual Benefit) and surrender freezes (Eurovita). Both impose severe losses on policyholders and take years to resolve. The monoline crisis was ultimately absorbed by bank balance sheets and $700 billion in TARP funding. There is no equivalent federal backstop mechanism for the PE-insurer complex.

---

## Conclusion: three novel insights from the analysis

The PE-insurer stress transmission pathway differs from the monoline precedent in a crucial structural way that cuts both directions. Bullet FABNs create a **floor** that monolines never had — $155 billion in non-puttable obligations cannot run, giving regulators quarters rather than weeks. But the FABR channel creates a **trapdoor** that monolines never had either — concentrated bank repo counterparties can exit without any contractual delay, and the $18.5 billion FABR market has grown 18x from essentially zero since 2020 with almost no regulatory reporting or transparency.

The FHLB system is being asked to serve as a backstop for a risk it was never designed to absorb. FHLB was created to support housing finance. Its eligible collateral requirements explicitly exclude private credit and CLOs. When PE-insurers whose investment strategy centers on private credit seek emergency FHLB funding, they can only pledge their housing-related holdings — a fraction of their portfolios. This creates an asymmetry: FHLB capacity scales with the size of an insurer's conventional holdings, not with the size of its wholesale funding needs.

The reinsurance web between PE-insurers transforms what could be isolated institution-specific stress into a **correlated system event**. F&G's $12.4 billion in recoverables from PE-backed reinsurers, Athene's $392 billion under Apollo management, and Global Atlantic's integration into KKR's $600B+ credit complex mean that the "independent" PE-insurers are bound by common asset exposure, common origination platforms, and bilateral reinsurance obligations. A credit cycle downturn that impairs private credit assets would simultaneously hit origination (Apollo, KKR, Blackstone fee income), insurance portfolios (marks on affiliated ABS), reinsurance recoverables (counterparty credit risk), and wholesale funding (FABR and FABN investor confidence) — four transmission channels firing simultaneously rather than sequentially. This is why the PE-insurer complex, despite comfortable RBC ratios today, deserves monitoring as a potential source of systemic stress that would move faster than the monoline precedent once it begins.