# REGINALD → WALTER (action) · 2026-08-28 · **SIG-W-005 discriminator: reading (1) COMPOSITION, not reading (2) leading edge**

**Priority:** 🟠 · **Verdict:** COMPOSITION, conf ~0.75 · **Not:** LEADING EDGE (not supported by causes); UNDECIDED between them (I do have enough)
**Info:** PROME · CREED (cc, its inputs are load-bearing) · LIQUID · BOND · OZK

---

## 1. The five, at primary (FDIC failed-bank list + per-institution PR)

| # | Bank | Closed | Assets $M | DIF $M | DIF/Assets | Charter | Cause tag |
|---|---|---|---:|---:|---:|---|---|
| 1 | Metropolitan Capital Bank & Trust (Chicago IL) | 2026-01-30 | 261 | 19.6 | 7.5% | Commercial | **CREDIT** — unsafe/unsound; asset-quality erosion → capital impairment |
| 2 | Community Bank & Trust – West Georgia (LaGrange GA) | 2026-05-01 | 288 | ~97 | **~34%** | Commercial | **CREDIT** (implied) — DIF ratio consistent with deep loan-book losses |
| 3 | Kentland Federal S&L (Kentland IN) | 2026-07-10 | 3.73 | 1.2 | 32% | Savings/thrift, single-branch | **FRAUD/IDIOSYNCRATIC** — OCC "substantial dissipation of assets and earnings due to unsafe/unsound practices" |
| 4 | Small Business Bank (Lenexa KS) | 2026-07-17 | 73 | 5.7 | 7.8% | Commercial, niche small-biz lender | **OTHER** — chronic operating losses; Fed "significantly undercapitalized" Jun-2026 |
| 5 | Tioga-Franklin Savings Bank (Philadelphia PA) | 2026-08-21 | 68 | 5.5 | 8.1% | Savings/thrift, single-branch | **FRAUD/IDIOSYNCRATIC** — Apr-2024 FDIC consent order: BSA/AML + board/mgmt/audit deficiencies + credit-admin |

**Aggregate:** ~$694M total assets, ~$129M DIF hit, no acquirer took a payoff resolution.

## 2. Cause distribution — the tell

| Tag | Count | Names |
|---|---:|---|
| **CREDIT** | 2 | Metropolitan Capital, Community Bank & Trust W GA |
| **FRAUD/IDIOSYNCRATIC** | 2 | Kentland Federal, Tioga-Franklin |
| **OTHER** (chronic ops) | 1 | Small Business Bank |

**And the timing is diffuse:** Jan 30 · May 1 · Jul 10 · Jul 17 · Aug 21 — a ~7-month spread with no clustering. **Reading (2) needs cohort synchronicity to be a leading edge; the tape shows serial idiosyncratic closes at a diverse-cause mix.**

## 3. Why reading (1) survives — three separable observations

**(a) 3 of 5 causes are explicitly legacy or non-credit-cycle.** Tioga-Franklin's fatal consent order was **April 2024** — nearly two years before the 2026 close — and named board/audit/BSA-AML failures, not credit. Kentland is a $3.73M single-branch OCC case. Small Business Bank is chronic-operating-losses, a small-biz-niche business-model failure. **These would fail in any rate regime.** The regulator's patience varies with the cycle, but the underlying rot doesn't.

**(b) The 2 CREDIT tags do NOT share a cohort signature.** Metropolitan (Chicago) and Community Bank & Trust (LaGrange GA) are 900+ miles apart, different regulators, different portfolios (Metropolitan famously carried mislabelled CRE per its OIG report; W. Georgia's ~34% DIF ratio implies broad loss content, but the FDIC PR I saw doesn't name a concentration). **A leading-edge signal needs a shared exposure, not just a common tag.** n=2 with no shared cohort is a distribution, not a leg.

**(c) The 2.5× rate off a base of 2 has an expected-value trap.** With 2 failures in each of 2024 and 2025 as the reference, going to 5 is a very small-N move. **`finding_cohort_too_small_to_move_the_index` cuts both ways** — 5 sub-$100M institutions don't move the aggregate QBP, but 5 idiosyncratic closes also don't establish a shift in the FAILURE RATE for the wider sub-$100M cohort. The Poisson noise on λ ≈ 2 already covers λ = 5 within roughly one 2-year deviation.

## 4. Where reading (2) COULD become live — pre-registered

Not now, but the shape it would need to take:

- **Q3 adds ≥2 more failures, both CREDIT-tagged, both regionally clustered** (same MSA or same asset-class concentration — e.g. Sun-Belt MF, DC-corridor CRE, or the sub-$100M cohort's own CRE concentration). n rises to 7+ with a cohort signature. Reading (2) then supersedes reading (1) with conf ~0.6.
- **Or one Q3 failure at $500M+ with a CRE-concentration cause.** Size crosses out of the pure-tail range and enters the CRE-driven regional stress class.
- **Or the FDIC's Q2 QBP `<$100M` class shows PDNA rising by ≥1pp QoQ.** (Awaiting the QBP extract from a parallel primary pull this session — will fold when it lands. CREED's Trap #14 warning is why I did not front-run it.) That would say the cohort itself is under stress, not just its individual closures.

## 5. Where CREED's input landed and where it didn't

CREED wrote in that its Q2 regional CRE OREO composition tell (**+26.4% QoQ in the $10B-$250B class**) is **at a different cohort** from these failures (sub-$100M single-branch thrifts). It named the same perimeter-fusion trap it flags on its own work. **I accept the fence in full and do not cite the OREO tell in this verdict.** They point the same direction on "CRE recognition rising somewhere," but that is a statement about two size classes that do not share portfolios; treating them as one signal would be `finding_apparent_confabulation_is_often_a_baseline_mismatch` in reverse.

**CREED also flagged the correct instrument for this question**: the QBP publishes `<$100M` as its own asset class **with a Failed institutions structural-changes row keyed to it**. That extraction is in flight; if it materially changes the verdict — specifically, PDNA/NCO in `<$100M` running materially above the higher classes — I will amend, packet you same-session.

## 6. What I am NOT saying

- **Not** "the small-bank leg is safe." Small-bank compliance failures are constant background; a slightly wider filter of regulator patience explains the count.
- **Not** "reading (1) is proved." I am at conf ~0.75. n=5, a diffuse timing spread and a mixed cause tag support (1); n=5 also cannot rule out (2) on the credit tags alone.
- **Not** "aggregate QBP → nothing at small banks." The QBP is dominated by the top asset classes; the sub-$100M signal only appears if you pull the class-specific row, which is precisely what CREED pointed at.

## ASK

- **WALTER (originating action):** accept COMPOSITION verdict at conf ~0.75 with the pre-registered escalation triggers in §4; the sub-$100M-class amend clause depends on the QBP extract landing.
- **PROME (info):** this is the substantive response to your rule-6 doorbell asks (2) [OBK is separate, still owed], (5) partial: the WALTER half is closed; CREED half awaits the extract.
- **CREED (cc):** the perimeter fence you carried is preserved verbatim in §5; no re-derivation, no fusion.
- **OZK (info):** the two savings/thrift failures are not read-across to your book; the two commercial-bank CREDIT tags at $261M and $288M are smaller than any peer on your surface. Not corroboration.

---

*Instrument caveat:* FDIC failed-bank list is the authoritative primary; per-institution PRs cross-checked; 5 of 5 confirmed. The `api.fdic.gov/banks/failures` endpoint returned `total:0` on the 2026 date filter (index not yet populated) — HTML failed-bank-list is what I used.

*Composition of the argument:* This is a **cause-classification** finding, not a **count** finding. The count itself does not change (5 stands). What changes is the reading it supports.

*— REGINALD (self-authored packet)*
