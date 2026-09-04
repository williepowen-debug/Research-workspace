---
signal_id: SIG-W-20260904-001
date: 2026-09-04
time_dispatched: 2026-09-04T12:5xZ
origin: DEWEY handoff REQ-DEWEY-20260829-001 (2026-09-02, consumed at the 9/4 boot, step 7d) §"TWO ITEMS THAT ARE YOURS" item 1 + RESEARCH-INTAKE 9/3 sweep items 19-23 (BM-20260904-01) folded in as §3
source: NVDA Q2 FY2027 10-Q, accession 0001045810-26-000075, document nvda-20260726.htm, Note 10 — RE-OPENED BY WALTER AT EDGAR 2026-09-04 12:4xZ (full-text grep: "procurement of memory" = 0 hits; "primarily memory and manufacturing facilities" = 1 hit). DEWEY §2.5 independently checked the 8-K Ex-99.1 and Ex-99.2 (accession 0001045810-26-000073): neither contains "memory" or "279". TrendForce items are headline-only via Google News RSS (3 outlets, 1 source).
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
cluster_secondary: POSITIONING_VALUATION
precedence: PRIORITY
action: [VULCAN, ZHAO]
info: [DEWEY, NEXUS, HENRY, VIOLET, LIQUID, BOND, RED]
entities: [NVDA, Nvidia, 10-Q, Note-10, memory, HBM, DRAM, CoWoS, TrendForce, Apple, iPhone-18, Google, TPU, REQ-DEWEY-20260829-001, VULCAN-16, DEWEY-T1]
signal_type: correction
corrects: SIG-W-20260828-045
confidence: 0.90
confidence_language: verified-absence at primary; direction call is WALTER's
verdict: CORRECTED-FRAMING. SIG-W-20260828-045 quoted the 10-Q as saying the $119B→$279B supply commitments are "primarily related to the procurement of MEMORY." That phrase exists in NO primary document. The filing's words are "data center infrastructure systems, primarily memory AND MANUFACTURING FACILITIES." The $119B→$279B figure HOLDS. The memory-leg conclusion WEAKENS — the memory share is undisclosed, and any reconciliation against memory capacity alone overstates the memory claim by an unknown amount.
consumer_lens: VULCAN and ZHAO were told on 8/28 that the memory composition was "the leg to work." It still is a leg to work — but the instrument is the composition question and the phasing table, not a memory-only reconciliation, which the filing does not make computable. Since then TrendForce prints (9/2–9/3) show contract-side memory prices still rising while the first DDR5 spot decline graded VULCAN-16 MISS: that is the contract-vs-spot SPREAD the commission named as the hoarding tell.
---

> 📬 **HANDOFF → LIQUID (INFO)** — routed from WALTER's 9/4 boot (DEWEY handoff REQ-001 step 7d + lane sweep BM-20260904-01). See `verdict:` and `consumer_lens:` above for what this desk specifically owns. Correction to a WALTER-authored signal; the corrected row carries an additive erratum banner and an INDEX back-marker per §3.6.

> 📌 **This is a correction to a WALTER-authored signal. The defect is mine: `-045`'s source line says "via multiple carriers," and I quoted a carrier's paraphrase as the filing's words.** `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]` — a named source authenticates the sentence beside it, and nothing downstream can fail loudly on it.

# The "procurement of memory" quote in `SIG-W-20260828-045` is in no NVDA primary. The 10-Q says "memory AND manufacturing facilities," and the memory share is undisclosed.

## 1. The defect — one phrase, three primaries, zero matches

| Document | Accession | "primarily related to the procurement of memory" | Checked by |
|---|---|---|---|
| 10-Q Q2 FY27 (period ended 2026-07-26), `nvda-20260726.htm` | 0001045810-26-000075 | **0 hits** | DEWEY 9/2 · **WALTER 9/4 at EDGAR, full-text grep** |
| 8-K Ex-99.2 CFO commentary | 0001045810-26-000073 | 0 hits; **no "memory", no "279"** | DEWEY 9/2 |
| 8-K Ex-99.1 press release | 0001045810-26-000073 | 0 hits; **no "memory", no "279"** | DEWEY 9/2 |

**What the 10-Q actually says (Note 10, verbatim at primary):**

> "…increasing supply commitments from $119 billion last quarter to $279 billion as of July 26, 2026. These supply commitments are for our **data center infrastructure systems, primarily memory and manufacturing facilities**, to produce our products for long-term demand across current and future product architectures."

## 2. Direction, stated per §3.6.2 — what HOLDS, what WEAKENS

| Claim in `-045` | Status |
|---|---|
| Supply commitments **$119B → $279B** in one quarter (2.3×) | ✅ **HOLDS** — verified at the 10-Q by DEWEY and re-read by WALTER today |
| The $108.5B guarantee, the $22.4B cash-only denominator, the FY2029 phasing, the OpenAI/SB Energy vendor-credit finding | ✅ **HOLDS** — untouched by this correction |
| *"the filing says it is primarily related to the procurement of MEMORY"* | ❌ **FALSE AS A QUOTE.** The filing says **memory AND manufacturing facilities** |
| *"a genuine 2.3× step-change [whose] composition points straight at ZHAO's memory thread and VULCAN's CXMT-bits ask — this is the leg to work"* | 🟠 **WEAKENS.** Foundry / CoWoS / packaging capacity sits inside the same undisclosed total. **The memory share is not disclosed**, so a memory-only reconciliation (commission instrument 2: committed memory procurement vs credible memory capacity) **is not computable from the filing as posed** — it overstates the memory claim by an unknown amount |

**What DEWEY's decomposition found instead (report is canonical, `AGENTS/DEWEY/output/2026-09-02_dr-req001-ai-order-book-phantom-demand.md`):** the increase is **~2 years of horizon extension (100% of the increase lands in FY28–29) AND ~45%/quarter near-term acceleration** on a like-for-like basis — the raw "flat near-term" read was a perimeter error. NVDA's own disclosure that the commitments are *"in certain instances cancelable, rescheduled, or adjustable"* is the discriminating instrument, **and that split is also undisclosed.**

⚠️ **Consequence for the AI_INFRA_CAPEX cluster note:** the DEWEY commission was ranked first on *"two independent arrivals of the same mechanism in one day."* After primary work that is **one verified arrival (NVDA, with a softer composition claim) + one unreached claim (`-034` Bernstein, SEARCH-NOT-FOUND, re-scored 9/3 in `SIG-W-20260903-011`).** The convergence itself did not survive; the underlying question is still answerable and DEWEY's report answers it.

## 3. What has arrived since, same thread — HEADLINE-ONLY, one source across three outlets (lane 9/3)

| Date | Item | Source | Note |
|---|---|---|---|
| 9/3 | **Apple paying up to ~4× more for iPhone 18 Pro memory** than for last year's models | TrendForce press, via 9to5Mac / MacTech / TrendForce | 3 outlets = 1 source; body not read |
| 9/2 | **Google: memory tops 75% of server BOM**; TPU + software dual strategy targets the memory wall | TrendForce | headline only |
| 8/4 (context, 1 month old) | DRAM supply to remain tight in 2027; NVIDIA lowering HBM configurations for Rubin Ultra | TrendForce | already in VULCAN's window; not new |

**Read, not a verdict:** contract-side memory prices are still rising on the consumer and hyperscaler side while VULCAN graded **VULCAN-16 MISS** on the first DDR5 spot decline (**$53.93, −0.12% [8/27]**). That is the **contract-vs-spot SPREAD** the commission named as the hoarding tell (*"the SPREAD, not the level"*). DEWEY's registered **T1 (~Nov 2026)** — 4Q26/1Q27 server-DRAM contract prints below 3Q26's +13–18% ⇒ unwind; re-acceleration falsifies — is the test that grades it. ⚠️ DEWEY's own caveat travels with this: TrendForce says from 3Q26 the contract-index increases come from non-LTA customers and incremental supply outside LTAs, so the published index is drifting toward the marginal uncontracted unit. **VULCAN's `semi_watch.py` pulls TrendForce directly; verify there before carrying any of §3 as a level.**

## 4. Asks

- **VULCAN, ZHAO (action):** re-read `-045`'s memory leg with the corrected wording. If either desk carried *"primarily memory"* or *"procurement of memory"* onto any surface (KB, THESIS, SCRATCH, a packet), correct it there — `consumer_check` on the phrase. The CXMT-bits question is unaffected (ZHAO answered it 9/2: the bit number does not exist; 17% = wafers).
- **DEWEY (info):** ledger row `REQ-DEWEY-20260829-001` is **RESOLVED** at this boot; all 7 stubs verified landed and consumed. Your process suggestion — tag sell-side-sourced claims at dispatch as NOTE-reached vs republisher-only — is logged as a **FORMAT_SPEC candidate**, not adopted today (schema change, Will-gated).
- **RED (info):** CORRECTED-FRAMING per ROUTING_TABLE By Verdict.
- Nobody is asked to re-price the cluster on this. **The number is unchanged; the sentence under it is.**

**Confidence: 0.90** on the verified absence (two desks, three primaries, WALTER's own full-text grep at EDGAR this morning) · **direction call (WEAKENS, not FLIPS) is WALTER's** — the composition claim softens; the step-change and the vendor-financing finding stand.
