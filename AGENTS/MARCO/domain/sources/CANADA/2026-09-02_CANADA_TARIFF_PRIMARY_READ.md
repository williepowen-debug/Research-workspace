# Canada tariff chain — primary read, 2026-09-02 (MARCO, session 25)

**Pulled by MARCO 2026-09-02 ~22:5x–23:0x ET. Every figure below is VERIFIED at the artifact named beside it.**
This file is the evidence backing the corrected cells on `STATUS.md`, `NEXUS_BRIEF.md` and `docket/CATALYSTS.tsv`.

## Sources reached

| # | Artifact | Route | Status |
|---|---|---|---|
| P1 | Dept of Finance Canada — *Canada announces targeted countermeasures and substantive support…* (announced 2026-08-25) | `canada.ca/en/department-finance/news/2026/08/canada-announces-targeted-countermeasures-…` | ✅ read |
| P2 | Dept of Finance Canada — *List of products from the United States subject to counter-tariffs effective September 8, 2026* (list updated 2026-08-26) | `canada.ca/en/department-finance/news/2026/08/list-of-products-…` | ✅ read |
| P3 | **CBP CSMS #69606660** (sent 08/21/2026 11:16 PM EDT) | `content.govdelivery.com/accounts/USDHSCBP/bulletins/4261d04` — **HTTP 200 with a browser User-Agent** (recipe from HAWK 8/22b) | ✅ **read — first time this desk has reached it; 403 on 8/22** |
| P4 | **`Section 338 Canada HTS LIST Final.pdf`** — the enumerated line list attached to P3, 6 pages | `content.govdelivery.com/attachments/USDHSCBP/2026/08/21/file_attachments/3754630/…` | ✅ **read — this is the Annex II enumeration that renders `[TIFF OMITTED]` in the Federal Register** |
| — | Complete Canadian tariff-item list (`…/complete-list-us-products-subject-to-counter-tariffs.html`) | canada.ca | ❌ **HTTP 404** — Canadian line-level enumeration NOT obtained |

## A · Canadian counter-tariffs (9/8) — P1 + P2

- **Effective time, VERBATIM (P2):** *"These countermeasures will be effective as of 12:01 a.m., September 8, 2026."* ⇒ **the derived-date caveat is DISCHARGED.** The 8/22 derivation from *"the Tuesday after Labour Day"* was correct.
- **Value: $27.6 billion.** ⚠️ **The same figure is used on BOTH sides of the match in the primary** — P2: *"the United States' decision to impose a 50 per cent tariff on $27.6 billion of Canadian goods effective August 22"* AND *"Canada's counter tariffs will apply to products covering $27.6 billion in imports from the U.S."* ⇒ the old **"~$28B" was the same quantity, verbally rounded by Carney on 8/21** — this is a PRECISION correction, not a perimeter correction.
- ⚠️ **CURRENCY IS NOT STATED IN THE OPERATIVE TEXT.** CAD is an INFERENCE from the publishing sovereign (Dept of Finance Canada), not a quote. Carry it as **CA$27.6B (currency inferred, not quoted)** and convert explicitly before any comparison with a USD figure. *(Refines HAWK's ①, which asserted CAD from the same inference.)*
- **Rates, VERBATIM (P1/P2):** *"15, 25, and 50 per cent tariffs on products drawn from those targeted by U.S. Section 338 and Section 232 tariffs, with individual product rates based on the matching U.S. rate for the same goods."* P1 puts it in four words: *"dollar for dollar, **rate for rate**."* ⇒ dollar-for-dollar is the **VALUE** claim; the rate is mirror-matched **per line**. **Never size a sector off one blended rate.**
- **Sectors (P1, the wider list):** steel, dairy, appliances, agricultural equipment, pulp and paper, electronics, **furniture**, **clothing and apparel**. P1: *"Goods subject to 50 per cent counter tariffs include steel and aluminum products that were previously only subject to a 25 per cent counter tariff."* ⇒ **derivatives move 25% → 50%.** *(P2's shorter sector list omits furniture/apparel — the two documents differ; P1 is the wider and later-quoted one. HAWK's read CONFIRMED from my independent pull.)*
- 🔴 **NEW — NOT CARRIED BY ANY DESK. P1, on autos:** *"other existing counter-tariffs against the U.S., **including autos, remain in place**."* ⇒ **US-origin autos are NOT part of the new 9/8 measure; they sit under a PRE-EXISTING Canadian counter-tariff that 9/8 neither creates nor removes.** **9/8 is not the auto-exposure date — the auto exposure is already live and has been.** This answers the question HAWK explicitly held open (*"I have NOT established that US-origin motor vehicles are in Canada's list"*): they are not in the NEW list, and the exposure exists anyway by a different instrument.
- **Support figures (P1):** *"a $7.5 billion package of new and enhanced measures"*, building on *"the nearly $25 billion in supports the government has provided since"* the US tariffs began. ⇒ **$25B = cumulative PRIOR domestic support · $7.5B = the new package · NEITHER is tariff value.** The `$25B` kill-on-sight now resolves with a mechanism.

## B · US Section 338 — the line list, read at last (P3 + P4)

**1,074 unique Chapter 1–97 commodity lines, across 65 chapters, spanning Ch.04 – Ch.97.**
*(1,137 unique 8-digit tokens in the PDF, less 63 Chapter-98/99 heading and cross-reference tokens. Zero non-conforming tokens in extraction — the pattern set was validated against a looser pattern that returned the identical 1,171 raw matches.)*

| Heading | Rate | Enumeration |
|---|---|---|
| 9903.03.12 | **50%** | 11 lines — Ch.22 beverages, Ch.44/48 wood & paper |
| 9903.03.13 | **50%** | 9 lines — Ch.04 dairy, Ch.17 sugars, Ch.35 caseins/albumins |
| **9903.03.14** | **50%** | **~1,054 lines — the wide annex, Ch.04→97** |
| 9903.03.15 | **0%** | *no enumerated lines* — defined by product-class language in U.S. note 51(c): steel/aluminium/copper & derivatives, passenger vehicles & light trucks & parts, MHDV & parts, wood products, semiconductors, patented pharmaceuticals |
| 9903.03.16 | **0%** | *no enumerated lines* — civil aircraft, engines, parts, ground flight simulators |

### The three carried claims, now SETTLED at the primary

1. ✅ **"Energy EXCLUDED" — CONFIRMED, and the MECHANISM is confirmed too.** **Chapter 27 (mineral fuels) : ZERO lines.** Energy is **absent from the positive list**, not carved out by the operative clause — exactly the reading MARCO proposed on 8/22 and HAWK adopted over his own seed. **Downgraded 8/22 for want of a primary; UPGRADED 9/2 to primary-supported.**
2. ✅ **"Potash EXCLUDED" — CONFIRMED, same mechanism. Chapter 31 (fertilizers) : ZERO lines.** *(FERT was packeted on 8/22 because its potash triage rested on an unverified exclusion. The exclusion now rests on a read. Root canon §POTASH keeps FERT triage-only.)*
3. ✅ **"Ch.4 through Ch.97 breadth" — was aggregator-only, now PRIMARY-CONFIRMED**, and slightly wider than the aggregator said: the span is **Ch.04–Ch.97 across 65 chapters**.

### Autos — the decisive line-level read
- **Chapter 87 contains exactly ONE line in the 50% list: `8711.50.00`** (motorcycles, reciprocating piston engine > 800 cc).
- **`8703` (passenger cars), `8704` (goods vehicles), `8708` (parts) : ZERO lines.**
⇒ **MARCO's 8/22 mechanism formulation is confirmed with witness lines, not asserted:** §232-subject vehicle lines are out (0%, heading 9903.03.15); the residual vehicle exposure at 50% is **motorcycles and nothing else**.
⚠️ **Steel is the proof the carve-out is LINE-specific, not chapter-wide: 46 Ch.73 + 1 Ch.72 lines sit in the 50% list even though 9903.03.15 carves out "articles of steel."** A chapter-level read of this action is wrong in both directions.

### Composition — the framing correction
By line count the list is **capital goods, not consumer goods**: Ch.85 electrical 187 · Ch.84 machinery 165 · Ch.90 optical/medical 85 = **437 of 1,074 (41%)**.
Consumer-visible lines — beverages 52, apparel/textiles 55, furniture 35, dairy 29, sports/toys incl. hockey 14, footwear 1, cement+salt 2 = **188 lines (17%)**.
⚠️ **Carney's consumer examples (beer, wine, hockey equipment, clothing, cement) are all REAL and all VERIFIED present — `2203.00.00` beer, `2204.*` wine, `9506.99.25` sports equipment, Ch.61-63 apparel, `2523.29.00` cement — but they are a MINORITY of the action by line count.** A read that treats this as a consumer-price action over-weights the visible tail.

### Defect confirmed in the CBP primary itself
P3's rate table is written on **9903.03.12–.16**, but its own **Chapter 98** and **Drawback** paragraphs both cite *"headings 9903.04.12 to 9903.04.14"* — a series appearing nowhere in its own rate table. **Independently reproduced by MARCO at the artifact** (HAWK flagged it 8/22b). Cite the rate table; treat the Ch.98/drawback headings as unresolved.
