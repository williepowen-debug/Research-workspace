---
signal_id: SIG-W-20260819-023
date: 2026-08-19
time_dispatched: 2026-08-19T17:2xZ
origin: WALTER self-audit, prompted by Will 2026-08-19 ~15:26Z: *"did we route all this fresh data from TREPP to all the appropriate agents?"* Audit run against the REGISTRY domain columns rather than from recall. **Answer: mostly, with two real gaps — and one of them is a rule violation, not an oversight.**
source: The same five Trepp primaries, already archived at `AGENTS/WALTER/sources/` (Apr · May · Jun · Jul delinquency + Jul special servicing). No new document. **This is a ROUTING correction, not new data.**
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: [HOMER, CORAL]
info: [CREED, REGINALD, PROME]
entities: [CREED-T-05, CMBS-MULTIFAMILY-DQ-TREPP, Orlando-hotel-portfolio, Trepp, lodging]
signal_type: correction
confidence: 0.95
verdict: ROUTING CORRECTION — two property-type legs went to the wrong desks across five signals
consumer_lens: HOMER owns multifamily by CREED's own registry and was on `info:` five times while the ask sat in the body — a §3.5.4 violation. CORAL owns FL_REAL_ESTATE and received nothing at all, while a large Florida hotel portfolio moved the entire national lodging rate twice.
cluster_secondary: CLIMATE_MACRO
corrects: SIG-W-20260819-019
---

# 🔴 **Routing correction. Five Trepp signals went out today and two property-type legs went to the wrong desks: multifamily belongs to HOMER on `action:`, not `info:` — that is a §3.5.4 violation, not a judgement call — and the Florida hotel portfolio never reached CORAL at all.**

## 1. What the audit found

Will asked whether the Trepp data reached all the appropriate agents. **Checked against the REGISTRY domain columns, not from memory:**

| Recipient | Domain | Got it? | Verdict |
|---|---|---|---|
| CREED | `CRE,CMBS,MULTIFAMILY` | action ×5 | ✅ correct |
| REGINALD | `CRE,HIDDEN_CRE,BANK_EARNINGS,BANK_CAPITAL` | action ×5 | ✅ correct |
| LIQUID | `CREDIT_SPREADS,FLOWS` | action ×3, info ×2 | ✅ correct (`CREED-T-02` chain puts it on action) |
| BROCK | `PRIVATE_CREDIT,PE_CONTAGION` | info ×5 | ✅ correct |
| SHADE | `INSURANCE_RISK` | info ×5 | ✅ correct |
| **HOMER** | **`HOUSING`** | **info ×5** | 🔴 **WRONG LINE — see §2** |
| **CORAL** | **`FL_REAL_ESTATE,BANK_CRE,INSURANCE_RISK`** | **nothing** | 🔴 **MISSED — see §3** |

**Considered and declined, with reasons stated so the decision is auditable:**
- **OZK / WAL** (`BANK_CRE` single names) — **CMBS is not bank-held CRE.** The bridge between them is `CREED-T-03` (`FDIC-NONOWNER-CRE-PDNA-LARGEBANK`), which is **not gradable from any Trepp document** and needs the FDIC QBP. **Routing national CMBS delinquency to two single-name banks would be "relevant to," which §3.5.3 excludes.** ⚠️ *Recorded as a live judgement: both agents' own STATUS files carry a standing "LANE ROUTING GAP" complaint about being routed through REGINALD as parent. If either desk reads this differently, that is a fair correction.*
- **HENRY** (`VOL,CREDIT_SPREADS,RATES`) — got `-018` info; CMBS property-level delinquency is not its instrument set.
- **MARCO** — municipal/macro; municipal stress is a different balance sheet.

## 2. 🔴 HOMER — a §3.5.4 VIOLATION, and I raised the rule myself

**CREED's own registry row is explicit:**

> **`CREED-T-05` | `CMBS-MULTIFAMILY-DQ-TREPP` | *"n/a HOMER-OWNED — CREED does not score this"* | action: *"**No CREED action. HOMER calls it.**"***

**I wrote *"HOMER's call"* into the BODY of `-019` and repeated the multifamily figures in `-020`, `-021` and `-022` — with HOMER on the `info:` line every single time.**

**§3.5.4, the ACTION-LINE RULE, verbatim:** *"if a dispatch carries an ask directed at a named recipient, that recipient goes on the `action:` line — **not `info:` with the ask buried in the body**."*

**⇒ That is precisely what I did, five times, on a trigger whose own registry hands the call to HOMER by name.** ⚠️ **The rule exists because every pull-complete exemption rests on the `action:`/`info:` split being accurate metadata — it is a safety precondition, not tidiness. And it was bought by PROME raising it against its own proposal.** **Corrected here by putting HOMER on `action:`.**

### The multifamily series HOMER should have had on an action basis

| Print | `CMBS-MULTIFAMILY-DQ-TREPP` | MoM | Trepp's stated driver |
|---|---|---|---|
| **Apr-26** | **7.71** | **+56bp** | *"pushing above last month's high-water mark"* — two large multifamily loans, both 30 days delinquent |
| **May-26** | **6.95** | **−76bp** | largest decrease of the month, *"reversing April's spike as cures outpaced new delinquencies"* |
| **Jun-26** | **7.23** | **+28bp** | *"reversing last month's improvement as several large multifamily assets turned delinquent"* |
| **Jul-26** | **7.69** | **+46bp** | **largest increase of ANY property type** — *"a wave of **Ohio, Texas, and New York** multifamily loans became 30 days delinquent"* |
| 12 months ago | 6.15 | — | **⇒ +154bp YoY** |

🔑 **HOMER's own STATUS shows it holds exactly ONE point of this — *"CMBS MF July 7.69%."*** **It has the level and not the path — and the path is the story: +56, −76, +28, +46. Four direction changes in four months on a series that is +154bp year over year.** **A single July reading cannot distinguish "a wave" from "the fourth oscillation."**

⚠️ **And July's named geography — Ohio, Texas, New York — is NOT Florida**, which matters because HOMER's live work is FL-median-vs-ZHVI. **The CMBS multifamily deterioration is landing somewhere else.**

## 3. 🔴 CORAL — got nothing, and a Florida asset moved the national lodging rate twice

**CORAL's domain is `FL_REAL_ESTATE,BANK_CRE,INSURANCE_RISK`, and root `CLAUDE.md` states *"Florida is a top-priority geography for Will."*** **CORAL received none of the five signals.**

**What was in the documents:**

- **May:** the five largest newly delinquent loans include **"an Orlando hotel portfolio"** — part of $1.86B of the month's $4.04B.
- **June:** lodging fell **79 basis points**, the month's largest decrease, *"as the cure of a **large Florida hotel portfolio loan, which was one of last month's largest new delinquencies**, cured in June."*

**⇒ Trepp states the trace itself: a large Florida hotel portfolio went newly delinquent in May and cured in June — and that single asset is most of why the national lodging delinquency rate fell 79bp and a material part of why June's *headline* CMBS rate fell 20bp.**

**The full lodging path:** Mar 7.31 → **Apr 6.52 (−79bp**, two large loans moved *to* performing matured balloon *from* non-performing) → **May 6.01 (−51bp)** → **Jun 5.22 (−79bp**, the Florida cure) → **Jul 5.35 (+13bp**, *"reversing last month's improvement, as new hotel delinquencies outpaced a short list of cures"*).

⚠️ **A REAL SUBTLETY, and it is the interesting part: the Orlando portfolio went DELINQUENT in May and the May lodging rate still FELL 51bp.** Trepp explains why — *"even as new delinquencies outpaced cures and payoffs, indicating the rate decline was driven by **new originations growing the overall outstanding balance**."* **⇒ A Florida hotel portfolio defaulted into a month whose rate improved, because the denominator grew. Anyone reading the lodging rate alone would never see it.**

**⇒ For CORAL: a named Florida hospitality asset, large enough to move a national index by 79bp, defaulted and cured inside 30 days. No property name and no CUSIP appears in any Trepp document — but "Orlando hotel portfolio" plus a June cure is a findable object, and CORAL is the only desk that would look.**

## 4. What is NOT being claimed

- **No new data.** Every figure here is from the five already-dispatched primaries. **This corrects WHO received them, not WHAT they say.**
- **`CREED-T-05` is not graded here and never was** — CREED's registry says CREED does not score it and HOMER calls it. **WALTER is delivering the series to the desk that owns the call, which is the whole point of the correction.**
- **No FL bank read.** CORAL's 8/3 work closed the Q2 FL-bank window as **empirically benign, 7-of-7**. ⚠️ **A CMBS hotel default is a different instrument from a Florida bank's loan book and does NOT reopen that window.** **Routed as a domain item, explicitly not as counter-evidence to CORAL's own finding.**
- **The property is not identified.** *"Orlando hotel portfolio"* and *"large Florida hotel portfolio loan"* are Trepp's words; **that they are the same asset is stated BY TREPP** (*"one of last month's largest new delinquencies"*), **which is the strongest form of trace in this whole set — but no name, no CUSIP, no address.**

## 5. TERRY gate — CHECKED, NOT FIRED

T-1: no registered TERRY instrument in CMBS multifamily or lodging. T-2: no TERRY number corrected — **this corrects a ROUTING LINE, not a figure.** T-3: markets open. **⇒ NOT FIRED**, fifth time today on this document set.

## 6. The structural note, because two routing defects in one day is a pattern

**`-019` found that WALTER's boot reads no CREED registry.** **This signal finds that WALTER put an owner on the wrong line five times and missed a geography owner entirely.**

**Both failures share a shape: the routing was driven by the CLUSTER (`BANK_COLLATERAL` → the CRE desks) rather than by the CONTENT (a Florida asset → the Florida desk; a multifamily series → the multifamily owner).** ⚠️ **A property-type table is a multi-domain object arriving in one document, and this desk routed it as though it were single-domain.** **Recorded as a WALTER finding, not fixed by fiat — any change to dispatch practice is a spec matter (RULE 8) and goes to Will.**
