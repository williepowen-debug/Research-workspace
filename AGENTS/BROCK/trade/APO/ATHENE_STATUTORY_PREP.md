# ATHENE STATUTORY FILING — What to Look For
**Created:** 2026-03-16
**Purpose:** Prep guide for when Athene's annual statutory filing becomes available, so we can read it day-one before anyone else.

---

## FILING MECHANICS

### What Is It?
- **NAIC Annual Statement** — the statutory accounting (SAP) version of financial statements that all US insurers must file with their state regulator
- Filed by **Athene Annuity and Life Company** (NAIC code 61689), domiciled in Iowa
- SAP is solvency-focused (conservative), unlike GAAP which is earnings-focused. The gap between SAP and GAAP is where the magic tricks hide.

### When?
- **Annual statement deadline: March 1** for the preceding calendar year (i.e., FY2025 statement was due March 1, 2026)
- **It may already be filed.** The NAIC filing was due March 1, 2026.
- **Public availability:** Filed with NAIC, accessible via InsData portal (content.naic.org). Some state DOI sites also publish them. Iowa Insurance Division (iid.iowa.gov) may have it.
- **Q1 2026 quarterly due: May 15, 2026** (45 days after quarter end)

### Where to Get It?
1. **NAIC InsData** — content.naic.org → search for Athene Annuity and Life Company (61689). PDF format. May require small fee ($35-50 per filing).
2. **Iowa Insurance Division** — iid.iowa.gov. Sometimes publishes examination reports.
3. **InsuranceNewsNet** — Previously published quarterly statutory filings for Athene.
4. **Athene IR** — ir.athene.com (unlikely to voluntarily publish the full statutory with schedules)

---

## THE BERMUDA TRIANGLE STRUCTURE

Athene operates a three-entity structure that Gober calls the "Bermuda Triangle":

```
┌──────────────────────────┐
│   ATHENE ANNUITY & LIFE  │ ← US-domiciled (Iowa), sells annuities
│   COMPANY (Iowa)         │   Files NAIC statutory statement (SAP)
│   NAIC Code: 61689       │   THIS IS WHAT WE READ
└──────────┬───────────────┘
           │ Cedes liabilities via reinsurance
           ▼
┌──────────────────────────┐
│   ATHENE RE (Bermuda)    │ ← Offshore reinsurer, Apollo-affiliated
│   + Other offshore subs  │   Does NOT file US statutory statements
│   (Barbados, Caymans)    │   Financial statements are SECRET
└──────────┬───────────────┘
           │ Invests reserves via
           ▼
┌──────────────────────────┐
│   APOLLO (Asset Manager) │ ← Manages the investments
│   Affiliated paper,      │   Controls what goes into the portfolio
│   ALT investments, CLOs  │   Marks are whatever Apollo says
└──────────────────────────┘
```

**Key insight:** The US statutory filing shows what Athene Iowa CEDES to the offshore affiliates. It does NOT show what those affiliates do with the money. Schedule S Part 3 Section 1 is where you see the cession — how much, to whom.

---

## SCHEDULE S PART 3 SECTION 1 — THE TARGET

### What It Shows
**"Reinsurance Ceded — Life Insurance, Annuities, Deposit Funds and Other Liabilities"**

This schedule lists, counterparty by counterparty:
- Name of reinsurer (who the liabilities are ceded to)
- Domicile of reinsurer (Iowa? Bermuda? Cayman Islands?)
- Whether reinsurer is **affiliated** or unaffiliated
- **Reserve credit taken** — the dollar amount Athene Iowa subtracts from its liabilities because it claims the reinsurer will pay
- **Collateral/security** backing the cession
- Type of reinsurance (coinsurance, modco, funds withheld)

### What to Look For

#### 1. TOTAL AFFILIATED REINSURANCE vs. SURPLUS
**The Gober Number:**
- As of Dec 31, 2023: Athene Iowa had **$155 billion** in reinsurance with its own captives and offshore affiliates
- Total reported surplus: **$2.88 billion** (= 1.44% of assets)
- Ratio: 54:1 (affiliated reinsurance to surplus)

**What we need for FY2025:**
- Has affiliated reinsurance grown from $155B? Given GAAP assets grew $71.5B in 2025, ceded amounts likely grew proportionally. Could be **$180-200B+ now.**
- Has surplus grown proportionally? If surplus is still ~$3B but ceded amounts hit $200B, the ratio gets worse.
- **Screen:** Affiliated reinsurance / surplus ratio. Higher = more fragile. Compare to peers (TIAA surplus 13.83%, NYL 12.24% vs Athene's 1.44%).

#### 2. OFFSHORE vs. ONSHORE CESSIONS
- How much goes to **Athene Re (Bermuda)** vs US entities?
- How much goes to **ACRA 1 / ACRA 2** (the Apollo/ADIP vehicles)?
- How much goes to **Catalina** (Bermuda-based, $6.3B recoverable as of GAAP 10-K)?
- **The more offshore, the less transparent.** Bermuda entities don't file SAP.

#### 3. COLLATERAL QUALITY
- For each cession, what secures it?
- **Funds withheld** = Athene Iowa retains the assets but gives the reinsurer credit (best case)
- **Trust accounts** = assets in a trust (decent, depending on what's in the trust)
- **Letters of credit** = a bank guarantee (introduces bank counterparty risk)
- **Unsecured** = pure promise (worst case)
- **Screen:** % of cessions backed by funds withheld vs unsecured or LOC

#### 4. DEPOSIT-TYPE CONTRACTS (Schedule E / Exhibit of Premiums)
- 10-K showed ~$85B in funding agreements. The statutory filing will show these as "deposit-type" liabilities.
- **Key question:** What is their duration vs the duration of assets backing them?
- SAP requires cash-basis reserving. If the assets are illiquid private credit and the liabilities are short-term deposits, the mismatch shows up in statutory liquidity ratios more starkly than in GAAP.

#### 5. RISK-BASED CAPITAL (RBC) RATIO
- This is the statutory solvency metric. NAIC sets minimums.
- **Company Action Level** = 200%. Below this → regulator intervention.
- Athene's RBC ratio has historically been adequate (~350-400%?) but thin vs peers.
- **Key question:** Has the massive asset growth (23% YoY) outpaced capital? RBC charges on illiquid/below-IG assets are higher.
- If Athene is loading up on affiliated ABS, CLOs, and alternative investments, the RBC charges should be rising.

#### 6. SCHEDULE D — INVESTMENTS
- Unlike GAAP which allows mark-to-model, SAP values differently:
  - Bonds: amortized cost (not fair value) if IG. OTTI if impaired.
  - Stocks: fair value
  - Mortgage loans: amortized cost less reserves
  - Alternatives: varies — often equity method or cost
- **Screen:** Look for concentration in affiliated investments, CLOs with low NAIC designations (3-6 = junk equivalent), and any assets carried at cost that may be impaired.

#### 7. SCHEDULE BA — "OTHER INVESTED ASSETS"
- This is where the unusual stuff lives: limited partnerships, hedge funds, affiliated vehicles, real estate partnerships.
- **Gober's concern:** "Joint ventures, limited partnerships with affiliates in the Cayman Islands"
- **Screen:** Total Schedule BA as % of admitted assets. Growing? What's in it?

---

## THE GAAP vs SAP ARBITRAGE

| Item | GAAP (10-K) | SAP (Statutory) | Why It Matters |
|------|-------------|-----------------|----------------|
| DAC (deferred acquisition costs) | Amortized over 25+ years | Charged immediately to surplus | SAP shows the real cost of new business |
| Affiliated reinsurance | Eliminated in consolidation | Shown as ceded with counterparty detail | SAP reveals the Bermuda Triangle |
| Bond valuation | Fair value (AFS) or amortized cost (HTM) | NAIC designation-based | Low-rated bonds hit surplus harder in SAP |
| Surplus | ~$55B equity (GAAP) | ~$3B surplus (SAP) | 18:1 ratio. GAAP hides the thinness. |
| Investment funds/VIEs | Consolidated | May be non-admitted | SAP can exclude assets GAAP includes |

**Critical gap:** GAAP shows Athene with ~$55B in equity. SAP shows ~$3B in surplus. The difference is GAAP goodwill, VOBA, DAC, and the consolidation of offshore entities that SAP strips out. **Under statutory accounting, Athene is operating on a razor-thin margin.**

---

## WHAT EISMAN/GOBER SPECIFICALLY SAID TO LOOK FOR

1. **Schedule S Part 3 Section 1** — "The secrets are in there" — shows all reinsurance ceded, counterparty by counterparty, with affiliated flags
2. **$7B liabilities backed by $200M real assets** — Gober saw one set of captive financials (accidentally published). The "XOL assets" were contingent instruments "like a lottery ticket before the drawing"
3. **Permitted practices** — Iowa may allow Athene to use accounting methods that SAP guidelines prohibit. Look for footnotes disclosing "permitted practices" — these are exceptions the regulator granted.
4. **The ratio test:** Affiliated reinsurance ÷ surplus. For Athene it was 54:1 in 2023. Compare to: TIAA (much lower), NYL (much lower), Pacific Life (much lower).

---

## ACTION PLAN

### Immediate (This Week)
1. **Check if FY2025 annual statement is available.** It was due March 1, 2026. May already be on NAIC InsData or the Iowa DOI site.
2. **If available:** Pull it. Go straight to Schedule S Part 3 Section 1. Count affiliated reinsurance total. Compare to FY2023's $155B.
3. **Also check:** RBC ratio, Schedule BA total, Schedule D concentrations.

### If Not Yet Available
- Set a watch. InsuranceNewsNet typically publishes quarterly statutory filings ~6 weeks after quarter end.
- Q4 2025 / FY2025 annual should be publicly accessible by late March / early April 2026.
- Q1 2026 quarterly due May 15, 2026.

### What Constitutes a Finding
- Affiliated reinsurance > $180B with surplus still < $4B = ratio deteriorating
- Any new offshore cession entities we haven't seen before
- Schedule BA growth > 20% YoY = alternative/opaque asset loading
- RBC ratio decline > 50 points from prior year
- Any disclosed "permitted practice" not previously known

---

## WHY THIS MATTERS FOR THE TRADE

Nobody on sellside reads these. Eisman: *"There is not one sellside analyst who covers Apollo/KKR who has ever looked at a statutory filing."*

The analysts covering APO are alternative asset management specialists. They analyze fee revenue, AUM growth, performance allocations. They have never opened a 7,700-page NAIC filing. They don't know what Schedule S Part 3 Section 1 is.

If we can pull the FY2025 statutory filing and quantify the updated Bermuda Triangle numbers, we will have primary source data that:
1. No sellside analyst has
2. Confirms or extends the Gober analysis
3. Provides specific dollar amounts for the risk that APO bulls dismiss as theoretical

This is where edge lives — in the documents nobody reads.
