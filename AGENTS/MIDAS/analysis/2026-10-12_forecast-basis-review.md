# MIDAS-09/10 — metal-per-share basis review

**October12,2026 · approved maintenance review.** Both rows remain OPEN on their frozen October30 letters, with November6 source-unavailability backstop. The ledger's SHA256 is recorded in the maintenance validation. No probability, baseline, threshold, outcome or status is amended here.

The binding market object is USD per ETF share, not ounces per share. MIDAS-09 uses GLD/SLV and probabilities0.20/0.55/0.25; MIDAS-10 uses PPLT/PALL and0.26/0.49/0.25. Both specify unadjusted daily Close and STUCK on a split/reverse split or a change in “metal-per-share basis.” Their historical references use ordinary ETF prices without filtering fee-accrual days.

Issuer evidence confirms ordinary metal depletion: [GLD's January2025 FAQ, page9](https://www.spdrgoldshares.com/media/GLD/file/GLD-FAQs-January-2025.pdf) describes gold sales for expenses; [PPLT's 2025 Form10-K risk factors](https://www.sec.gov/Archives/edgar/data/1460235/000199937126004880/pplt-10k_123125.htm) describes daily fee-related reductions in backing per share. A quantity decline does not itself demonstrate a changed legal share denomination. The historical PPLT/PALL May2026 splits occurred before the September24 baselines, not inside these windows. No in-window structural action was established by this review.

| Case | Recommended meaning of basis | What remains unresolved in the frozen wording |
|---|---|---|
| Ordinary recurring fees, same USD/share series and share denomination | Continue to grade the market-return branches; fees are part of the price return | The text does not explicitly exclude ordinary entitlement erosion |
| An in-window split/reverse split | STUCK as explicitly written; do not substitute adjusted prices afterwards | No ambiguity on this case |
| A discontinuous structural redefinition of metal entitlement or the ETF's underlying metal | STUCK under the basis-change clause | Structural versus ordinary drift is not numerically/legally defined in the letter |

**Review conclusion:** the registration object and references support the structural-unit interpretation, but do not prove that the frozen sentence has only that interpretation. The ambiguity is real; this is not a finding that either row is already STUCK. A unilateral insertion excluding fees could move cases from non-resolution into scored outcomes.

The canonical constraint is `FORGE/PREDICTION_DISCIPLINE.md` §Grading & re-marking, WQ-161②③: “a mass-moving specification repair is not allowed as a retrofit”; the proof must establish that the scored set and grading conditions stay unchanged. Unchanged0.20/0.55/0.25 or0.26/0.49/0.25 alone is not that proof. Therefore the approved **review** is complete, while the live criteria remain untouched. No source outage or lower confidence is used to conceal the specification issue.

**Concrete prospective wording:** “Metal-per-share basis change means a split, reverse split or structural redefinition of share denomination/metal entitlement. Ordinary recurring fees already reflected in the quoted USD/share price do not change this basis. Use unadjusted Close throughout; a structural change inside the window sets STUCK.”

**Coordination:** PROME should register the frozen-letter interpretation question for review before October30. Request a finding on the existing term's meaning rather than silently retrofitting the proposed successor text. If a mass-neutral interpretation cannot be supported, preserve the original rows and use separately registered successors; do not alter the historic calibration record. Will's general repair approval does not erase the brief's explicit instruction to preserve these frozen letters.
