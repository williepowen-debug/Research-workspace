# PROME → BOND: one bounded correction from CATO's review — narrow two conclusions in the CCC refinancing-wall note (Will-directed, 9/28 ~16:2x ET)

**From:** PROME (`prome-7f`) · **To:** BOND (live session `bond-d6`, doorbelled) · **Written:** 2026-09-28 16:25 ET · **Authority:** Will, 9/28 16:2x ET, verbatim: *"PROME — please coordinate these bounded corrections from CATO's review with WAL and BOND. Use existing evidence; no new study or broad audit."* · **Class:** qualification of two conclusions in an existing deliverable — no new source hunt (Will: *"No additional source hunt required."*).

**Target artifact (VERIFIED at the artifact 9/28 16:2x ET):** `analysis/2026-09-28_CCC-refi-wall-2027-28.md` (`0fcd3d955`, Will-approved bounded attempt, WQ-323) + its mirrors: `workbook/KB.tsv` row `KB-BND-349`, `SCRATCH.md` item 7b, and any STATUS line that repeats either conclusion.

---

## CATO's finding (Will's words, verbatim)

*"BOND: narrow two conclusions. A 75% share of amendments involving B- or better borrowers does not establish increasing concentration among weaker borrowers without the starting population and extension rates. Likewise, larger aggregate maturities in later years do not rule out near-term CCC or individual-borrower refinancing stress. Retain the supported refinancing-cost mechanism and scoped maturity tables; qualify those broader conclusions."*

## The two sentences, and what the evidence supports

**Conclusion 1 — §4, second bullet:** *"But the weakest issuers are the minority of the extensions. ~75% of 2025 loan amend-and-extends were for issuers rated B- or better (83% in 2024; LCD, snippet). **The residual wall is therefore concentrating in the weakest names.**"*
- What the datum is: the share of A&E volume by rating tier (75% B- or better ⇒ 25% below B-).
- What "concentrating" needs and the datum lacks: the STARTING population share of below-B- paper in the pre-extension wall, and the extension RATE by tier (extensions ÷ maturities-at-risk, per tier). If below-B- paper was ~25% of the population, a 25% share of extensions is proportional — no concentration. The 83% → 75% year-over-year move says the below-B- share of extensions ROSE, which cuts the other way if anything. Neither population nor rate is in your raw pass (`domain/sources/2026-09-28_ccc-refi-wall_web-pass_raw.md` line 35 carries only the shares).
- **Supported statement:** *below-B- issuers were ~25% of 2025 loan A&E volume (up from ~17% in 2024; LCD snippet). Whether the residual wall is concentrating in the weakest names cannot be established from the extension share alone — it needs the starting tier mix of the wall and per-tier extension rates, neither of which the free sources give (GAP).*

**Conclusion 2 — "What this shows" ✅ Timing:** *"the big maturities are 2028–29, so this is a slow squeeze, not a 2026–27 cliff. The watch items are defaults/distressed exchanges and loan interest coverage, not a maturity date."* — and the same reading in **Bottom line**: *"In dollars, the pressure sits in 2028–29 more than 2027."*
- What the tables show: AGGREGATE dollar maturities are larger in 2028–29 than in 2027 (HY bonds $68.5B 2027 vs $314.1B 2029, LSEG; spec-grade $311.2B 2027 vs $639.6B 2028, S&P).
- What they do not show: that CCC issuers, or any individual borrower, are free of near-term refinancing stress. A CCC name with a 2027 maturity faces the coupon step-up now (your §1 shows the CCC yield at a 3-year high); the aggregate's shape says nothing about that name. The "not a 2026–27 cliff" and "not a maturity date" phrasings generalize from the aggregate to the tail.
- **Supported statement:** *in aggregate dollars the wall is larger in 2028–29 than in 2027, so the INDEX-level pressure is a slow squeeze rather than a 2026–27 cliff. That does not rule out near-term refinancing stress for CCC issuers or individual borrowers with 2026–27 maturities, where the §1 coupon step-up applies now; a CCC-only 2027 figure is a GAP (§2), so the near-term tail is UNMEASURED, not small.*

## Required end state

1. Both conclusions **qualified in place** in `analysis/2026-09-28_CCC-refi-wall-2027-28.md` as a dated edit (a dated correction note at the top or beside each sentence, your discipline) — the refinancing-cost mechanism (§1), the scoped maturity tables (§2), the sector GAP (§3) and the distressed-exchange datum (§4) are **retained unchanged**.
2. The same qualification carried to **every mirror**: `KB-BND-349` (its Analysis/Implication cells — do not change the source cells), `SCRATCH.md` 7b, any STATUS line, and `thesis/` if the note was cited there. The summary is where a correction lands last; fix it first (`finding_summary_section_merges_what_the_body_separates`).
3. The watch-item sentence keeps defaults, distressed exchanges and loan interest coverage AND adds the near-term tail: any CCC or single-name 2026–27 maturity that fails to refinance is evidence at the tail even while the aggregate reads slow.
4. **No new search.** If a qualification would need a datum you do not hold (the tier mix of the wall, per-tier extension rates, a CCC-only 2027 figure), it is written as GAP, not fetched.

## Delivery

- **Commit** your own files (path-scoped). Write a receipt to `PROME/inbox/2026-09-28_from-BOND_cato-refi-wall-narrowing-receipt.md` naming every file changed with the commit hash, and any point you could not resolve on existing evidence (UNRESOLVED, never inferred). `SendMessage` the hash to `prome-7f` as your final action before idling.
- Move this packet to `inbox/processed/` when consumed.
