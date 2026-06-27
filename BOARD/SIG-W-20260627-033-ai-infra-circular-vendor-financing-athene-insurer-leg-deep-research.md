---
signal_id: SIG-W-20260627-033
dispatched: 2026-06-27T20:30:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260627-001 — AI-infra circular/vendor financing + Athene insurer-leg verification) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-06-27 (post-crash recovery session)
source: DEWEY report `AGENTS/DEWEY/output/2026-06-27_ai-circular-financing.md` (Mode Thesis / Confidence High on circular-financing structure, Medium on magnitudes + insurer-leg specifics; `/deep-research` 106-agent fan-out [24 sources, 25 claims adversarially verified] + independent DEWEY EDGAR/XBRL primary pulls on Apollo CIK 1858681 Q1-2026 10-Q + Athene Holding CIK 1527469)
signal_type: research-output
domain: AI_INFRA_CAPEX
cluster: AI_INFRA_CAPEX
cluster_secondary: PC_STRESS
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [HENRY, BROCK, SHADE]
info: [RED]
confidence: 0.80
verify_verdict: VERIFIED-PRIMARY (with an attribution-vs-fact split — carry it). The circular-financing STRUCTURES + the insurer-leg balance-sheet facts are primary-source-grade (Nvidia IR, Apollo PR, CoreWeave 8-K, Athene Bermuda BMA statutory FCR + DEWEY's own Apollo/Athene-Holding 10-Q/10-K XBRL pulls). The four Burry-attributed figures ($103bn / 34.7% / 16.6× / $217bn) are attribution-grade ORIGIN (Substack), now DATED/BOUNDED by DEWEY's EDGAR work — NOT independently verified as fact. The deliverable's own adversarial pass refuted (0-3) the figures relayed AS FACT but accepted (3-0) them AS Burry's attribution. No WALTER verify-spawn (Phase 2.8b — a deep-research deliverable is already primary-sourced; a $0.05 routing-check is strictly dominated).
verify_method: none — deliverable is a `/deep-research` synthesis + DEWEY EDGAR/XBRL primary pull. WALTER routes + extracts per-recipient genuine delta (lean mandate — no re-analysis). Caveats carried through from the deliverable verbatim, not re-derived.
deep_research_ref: REQ-DEWEY-20260627-001 / originating signal SIG-W-20260627-008 (NVIDIA→Apollo→Athene circular-AI-GPU-financing + "Burry alarm bells inside Athene"). Closes the DEEP_RESEARCH_FLAGGED_LOG row for REQ-DEWEY-20260627-001 (disposition RESOLVED / executor DEWEY). First of the Will-approved 6/27 4-prompt batch to return; REQ-002 ex-AI-GDP + REQ-003 muni-fiscal + REQ-004 housing-distress remain PENDING.
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. ONE research-output signal — split test S1–S4 applied to the Athene insurer-leg finding (the one carve-out candidate, owner SHADE): all FAIL — S1 (SHADE-actionable but "test the hypothesis against the 10-K footnote," not yet a standalone decision, and it is a leg of the same circular-financing map), S2 (no registered RED-FT/REG-T trigger), S3 (same AI-capex-leverage repricing clock), S4 (elevated as THE SHADE wrapper-delta → precedence note: no forced split). Mirrors the SIG-W-20260619-008 worked example (kept-in-and-elevated rather than fragmenting). Cluster-primary AI_INFRA_CAPEX, secondary PC_STRESS; signal_role cluster_mediating (explicit two-sided — structure-real vs magnitudes-bounded / AI-collateral-linkage-undisclosed + a full counter-evidence section) → RED auto-cc. Honors DEWEY's "route as standard research-output, NOT VERIFIED-PRIMARY-overclaim" flag.
---

# AI-infra circular/vendor financing + the Apollo→Athene insurer leg — DEWEY deep-research deliverable (resolves SIG-008's Burry-Athene question)

This routes the first returned deliverable of the Will-approved 6/27 DEWEY batch. It answers SIG-W-20260627-008's two-part question: (1) how much of the AI-data-center buildout is circular/vendor-financed vs end-demand-funded, and (2) is the Apollo→Athene insurer balance sheet a systemic amplifier (the Burry-attributed Athene figures were flagged UNVERIFIED at dispatch). **WALTER's role is routing + per-recipient genuine-delta extraction, NOT re-analysis — the packet is the analysis.** Full report embedded verbatim below the wrapper.

> ⚠️ **GRADE: research-output with an attribution-vs-fact split.** The circular-financing *structures* and the insurer-leg *balance-sheet facts* are primary-source-grade (DEWEY pulled Apollo's Q1-2026 10-Q + Athene-Holding XBRL + the Athene Bermuda BMA statutory FCR). The four headline **Burry numbers are attribution-grade origin** (his Substack), now **dated/bounded** by DEWEY's EDGAR work — treat them as *dated contrarian estimates DEWEY has now bounded*, not as established facts. The single most important caveat: **no primary disclosure ties Athene's Level-3 to AI/data-center collateral** — the "hidden AI amplifier" claim is an *inference*.

## Verdict (one line)
The 2024–26 AI buildout is **pervasively vendor-financed / round-tripped — structure primary-confirmed** (>$120bn moved off balance sheet in ~18 months; leverage concentrated in the neocloud leg, CoreWeave $24.9bn debt / ~5.4× D/E / interest = 25.8% of revenue, and in single-tenant SPVs). The **Apollo→Athene insurer leg is structurally real and growing** (Level-3 ~$154.8bn at Q1-2026, **+~49% YoY**) — but the Burry figures are vintage-/definition-bounded and **no filing ties that Level-3 to AI collateral.** Net for the insurer-amplifier question: a **qualified YES on structure, NOT-YET on AI-specificity.**

---

## Per-recipient genuine delta (routing wrapper)

### → HENRY (ACTION) — AI-capex-bear thesis: the round-trip is now primary-confirmed, but the magnitude is softer than the headline
1. **The circular/vendor-financing structure is no longer just a narrative — it is confirmed against primary deal terms.** Nvidia takes equity in its own customers and disburses *per-gigawatt as the customer buys Nvidia systems* (OpenAI LOI); Nvidia is an **anchor-LP in the $5.4bn Valor SPV that buys its own GB200s** to lease to xAI; Nvidia **backstops $6.3bn of CoreWeave's unsold capacity.** A documented share of the buildout is funded by the *sellers of the equipment*, not third-party end-demand.
2. **Leverage concentrates where you'd want to short it — the neocloud leg:** CoreWeave Q1-2026 total debt **$24,859mn**, interest = **25.8% of revenue / 46.3% of adj. EBITDA**, cumulative issuance ~5.4× equity.
3. **⚠️ Magnitude caveat that *cuts against* the bear headline:** the **Nvidia–OpenAI "$100bn" is a non-binding LOI** (Huang: "never a commitment / an invitation"); reporting points to **~$30bn finalized.** The *structure* is confirmed; the *headline number* is soft. And there is **no public denominator** for total buildout capex → a clean vendor-financed-vs-end-demand *ratio cannot be produced* — this is a catalogue of large discrete flows, not a measured share. Don't quote a percentage that doesn't exist.

### → BROCK (ACTION) — private-credit / off-balance-sheet SPV leg (your SIG-008 Apollo leg + the 624 PC-redemption thread)
1. **>$120bn of data-center spend moved off balance sheet in ~18 months** (Oracle $66bn + Meta $30bn + xAI $20bn + CRWV $2.6bn) via bankruptcy-remote single-asset/single-tenant vehicles — sponsors "appear less leveraged than they are."
2. **The Meta/Blue Owl "Hyperion" bond = $27.294bn of 6.581% senior secured notes due 2049 (Oct 16 2025) — the largest project-finance / private-credit bond on record**, concentrating that debt in one single-asset vehicle (recharacterization / take-or-pay / litigation risk flagged by counsel). The **Anthropic chip-lease** is a **$35bn** SPV (Atlas SP, an Apollo subsidiary) — **Athene = a "sizable portion"** (unquantified).
3. **Two load-bearing nuances:** (a) **"off balance sheet" is reversible** — if the asset transfers are recharacterized as secured loans, the leverage comes back on-BS; it's a *presentation* fact, not necessarily economic de-risking. (b) **The Anthropic-SPV chips are Google TPUs (Broadcom-made), not Nvidia GPUs** — "AI-chip-collateralized credit" is not uniformly Nvidia-GPU collateral, which weakens any single-point-of-failure framing centered on Nvidia.

### → SHADE (ACTION) — the insurer-PC nexus: this resolves SIG-008's escalation question — qualified-yes on structure, not-yet on AI-specificity
1. **Burry-figure verdicts (DEWEY independent EDGAR/XBRL pull — the SIG-008 core ask):**
   - **$103bn Level-3 / 34.7%:** verified as **YE2024-vintage** (Athene/Apollo Retirement-Services L3 = $104.0bn at YE2024) but **now stale-low — ~$154.8bn at Q1-2026 (+~49% YoY)**, current share ~40–43%. The figure was ~$45bn out of date when posted; **the real story is *worse* than the headline — L3 is ballooning, not static.**
   - **16.6× leverage:** **NOT reproducible** from GAAP primaries — Apollo consol 11.8×, **Athene Holding standalone 13.3× (incl-NCI).** Definition-dependent; sits in the insurer-normal zone.
   - **$217bn Bermuda:** structure verified (AARe/ALRe/ALReI, BMA-regulated); gross AARe = **$315bn (FY2024 BMA filing)**; $217bn plausibly a **net/economic** measure (the ~63% ACRA/ADIP third-party sidecar = the $15.9bn Athene-Holding NCI — independent cross-check).
2. **⚠️ The escalation answer (load-bearing):** the insurer leg is **real and growing** (L3 +49% YoY), but **AI-collateral concentration is undisclosed/inferential** — the fair-value hierarchy is *not broken out by collateral type*, and *nothing in the primary filings ties Athene's Level-3 to AI-GPU/data-center credit.* **Treat "Athene = named AI-transmission amplifier" as a hypothesis to test against the FY2024 10-K fair-value footnote, NOT an established channel.**
3. **Counter to your own escalation:** Level-3 ≠ toxic — it's an *input-observability* classification, not a quality grade; a large chunk is funds-withheld-at-interest embedded derivatives (economically a total-return swap on high-grade assets) + IG-ish CLOs/structured paper. High-L3 + high-leverage is **structurally normal for a fixed-annuity insurer.** (Ties to your SIG-624-009 Lee-Robinson insurer-short + SIG-624-005 double-exposure work — the *mechanism* is real, the *AI-specific* dollar exposure is private-by-construction.)

### → RED (INFO) — adversarial / two-sided input
DEWEY ran an explicit counter-evidence pass. The cleanest discipline datum: the engine **refuted (0-3)** the identical Burry numbers when a secondary outlet relayed them **as fact**, but **accepted (3-0)** them framed **as Burry's attribution** — a source-quality split worth preserving. Steelman of the *benign* read: (a) Level-3 is observability not quality, and insurer-normal for a long-duration annuity book; (b) the $120bn off-BS is a presentation fact, reversible, not proven economic fragility; (c) the Nvidia–OpenAI magnitude is a soft LOI; (d) backstops are conditional (Nvidia's CoreWeave obligation covers only *residual unsold* capacity). The bubble call is HENRY/BROCK's — DEWEY confirms *structures*, not a verdict.

---

## Full research packet (verbatim, as delivered by DEWEY 2026-06-27)

# AI-Infra Circular / Vendor Financing — Mapping the Flows + Verifying the Athene Insurer Leg

**Date:** 2026-06-27 | **Mode:** Thesis | **Confidence:** High (circular-financing *structure*) / Medium (magnitudes; insurer-leg specifics)
**Flag:** REQ-DEWEY-20260627-001 / SIG-W-20260627-008 | **Clusters:** AI_INFRA_CAPEX, PC_STRESS
**Engine:** `/deep-research` (106-agent fan-out, 24 sources, 25 claims adversarially verified) + independent DEWEY EDGAR/XBRL primary-source pull on the insurer leg.

---

## Key Finding

The 2024–26 AI-data-center buildout is **pervasively vendor-financed and round-tripped**, confirmed by primary deal terms — Nvidia's up-to-$100bn intended investment in OpenAI (disbursed per-gigawatt as OpenAI buys Nvidia systems), Nvidia as anchor-LP in the $5.4bn Valor SPV that buys its own GB200s to lease to xAI, a $6.3bn Nvidia backstop of CoreWeave's unsold capacity, and **>$120bn of data-center spend moved off balance sheet in ~18 months**. Leverage concentrates in the **neocloud leg** (CoreWeave: $24.9bn debt, ~5.4× debt/equity, interest = 25.8% of revenue) and in **single-tenant SPVs** (the $27.3bn Meta/Blue Owl "Hyperion" bond — the largest project-finance bond on record).

The **Apollo→Athene insurer leg is structurally real and documented**, but the specific Michael-Burry-attributed figures are **vintage- or definition-dependent, and one is materially stale-low**: Athene's Level-3 assets were **~$104bn at YE2024** (≈ Burry's "$103bn") but have since grown to **~$154.8bn (Q1-2026, +~49%)**; the "16.6× leverage" is **not reproducible** from GAAP primaries (Athene Holding standalone = 13.3× incl-NCI); the "$217bn Bermuda" is plausibly a **net/economic measure** against a $315bn *gross* AARe book. Critically, **no primary disclosure ties Athene's Level-3 to AI/data-center collateral** — the "hidden AI amplifier" claim is an *inference*, not a disclosed fact.

---

## Evidence

### A. The circular-financing map (vendor/seller financing — confirmed against primary deal terms)

| Flow | Structure | Magnitude | Source |
|------|-----------|-----------|--------|
| **Nvidia → OpenAI** | Chip-maker takes equity in customer; capital disburses *per-gigawatt as Nvidia systems deploy*; OpenAI commits ≥10GW of Nvidia systems | "up to **$100bn**" intended (non-binding LOI); first $10bn tranche at first GW (H2-2026, Vera Rubin) | [PRIMARY: Nvidia IR press release, Sep 22 2025] |
| **Nvidia → xAI (Valor / VCI)** | Apollo-led capital solution inside a buy-and-lease SPV; **Nvidia itself invests as anchor LP** (~$1.9bn) in the SPV that buys its GB200s; triple-net lease to xAI subsidiary → GPUs on *neither* balance sheet | **$5.4bn** acquisition-and-lease; **$3.5bn** Apollo capital solution | [PRIMARY: Apollo press release, Jan 7 2026] |
| **Nvidia → CoreWeave** | Vendor demand-backstop: Nvidia *obligated to buy residual unsold capacity* through Apr 13 2032; plus direct equity (~$2.9bn CRWV, ~$2.0bn Nebius) | Order-form initial value **$6.3bn** | [PRIMARY: CoreWeave 8-K, accession 000176962825000047, event 2025-09-09] |
| **OpenAI → Oracle (Stargate)** | Customer→cloud-vendor→chip-maker: OpenAI buys Oracle capacity; Oracle buys ~400k GB200s | **~$300bn** / 5yr (OpenAI–Oracle); ~$40bn/400k-GB200 (Oracle→Nvidia, *press-sourced*) | [PRIMARY: OpenAI announcement] + [INSTITUTIONAL: Bloomberg-sourced for $40bn] |
| **Off-balance-sheet SPVs (sector-wide)** | Bankruptcy-remote single-asset/single-tenant vehicles let sponsors "appear less leveraged than they are" | **>$120bn** moved off-BS in ~18 months (Oracle $66bn + Meta $30bn + xAI $20bn + CRWV $2.6bn) | [NEWS/INSTITUTIONAL: FT compilation via Quinn Emanuel legal alert] |
| **Meta / Blue Owl "Hyperion" (Beignet)** | 80/20 Blue Owl/Meta JV; A+ single-tranche IG bond — largest private-credit/project-finance bond on record | **$27.294bn** of 6.581% senior secured notes due 2049, T+225bp, 144A/Reg-S, Oct 16 2025 | [INSTITUTIONAL: IFR/LSEG, Fortune; Meta JV release] |
| **Anthropic chip-lease (Apollo/Blackstone)** | SPV (Atlas SP, an Apollo subsidiary) borrows, buys chips, leases to Anthropic pre-IPO; Broadcom residual-value guarantee | **$35bn** initial (syndicated); **Athene = "sizable portion"** (unquantified) | [INSTITUTIONAL: PitchBook/Bloomberg, Jun 2026] |

**Interpretation guard (DEWEY is not the analyst):** these are *structures*, verified to exist. Whether they constitute a credit bubble is HENRY/BROCK/RED's call. What the data supports: a large, documented share of the buildout is funded by the sellers of the equipment and by leverage parked in off-balance-sheet vehicles, rather than by third-party end-demand. A clean **vendor-financed-vs-end-demand ratio could not be produced** — no public denominator exists; the research assembles discrete large flows but cannot divide them by total buildout capex (see Data Gaps).

### B. Where leverage concentrates

- **Neocloud leg (highest visible leverage):** CoreWeave Q1-2026 — total debt **$24,859mn**, interest expense $536mn = **25.8% of revenue** ($2,078mn) and **46.3% of adj. EBITDA** ($1,157mn); cumulative debt issuance ~5.4× equity. [PRIMARY: CoreWeave Q1-2026 8-K/IR, May 7 2026; ratios arithmetically exact.]
- **Off-balance-sheet project finance:** the Hyperion structure concentrates $27.3bn of debt in a single-asset, single-tenant vehicle; recharacterization/take-or-pay/litigation risk flagged by counsel. [NEWS: Quinn Emanuel.]
- **Insurer leg:** see Section C — large balance sheet, high (but insurer-normal) leverage, material Bermuda/Level-3 footprint.

### C. The insurer leg (Apollo→Athene) — independent DEWEY primary-source verification

Athene has been a **consolidated subsidiary of Apollo (NYSE: APO) since the Jan 1 2022 merger** (Athene Holding Ltd, CIK 1527469, still files a 10-K because it has registered debt/preferred outstanding). I pulled the **Apollo consolidated 10-Q (Q1-2026, accession 0001858681-26-000026, filed 2026-05-07)**, the **Athene Holding 10-K/10-Q XBRL facts**, and the deep-research engine surfaced the **Athene Bermuda Sub-Group Financial Condition Report (BMA statutory, FY2024, Deloitte-audited)**. Verdict on the four Burry-attributed figures:

| Burry figure | Primary-source verdict | Basis |
|---|---|---|
| **~$103bn Level-3** | **Verified-as-vintage, now STALE-LOW.** Matches Athene (Apollo "Retirement Services" segment) Level-3 recurring-FV assets of **$104,024mn at YE2024**. Grew to **$147,743mn (YE2025)** and **$154,761mn (Q1-2026)** — **+~49% in a year**. The figure was ~$45bn out of date even when posted (~late-May 2026). The real story is *worse* than the headline: Level-3 is ballooning, not static. | [PRIMARY: APO 10-Q Q1-2026 Level-3 roll-forward, `apo-20260331.htm`] |
| **~34.7%** | **Internally consistent for YE2024, now higher.** $103bn/0.347 ⇒ ~$300bn denominator ≈ Athene's YE2024 fair-value investment base — a roughly accurate YE2024 snapshot. CURRENT ratio is **~40–43%** ($154.8bn / $357.8bn–$389.7bn). Exact Burry denominator not reconstructed. | [PRIMARY: APO 10-Q; Athene total investments incl. related parties + VIEs = **$389.7bn** at 3/31/26] |
| **~16.6× leverage** | **NOT reproducible** from GAAP primaries. Apollo consolidated = 11.8× (equity incl-NCI) / 23.4× (parent). Athene Holding *standalone* = **13.3× (incl-NCI)** / 25.1× (parent). 16.6× sits in the insurer-normal zone but depends on Burry's undisclosed equity definition. | [PRIMARY: XBRL — Athene Holding assets $447,804mn / equity-incl-NCI $33,700mn, 3/31/26] |
| **~$217bn Bermuda** | **Structure verified; specific number = plausible NET measure.** Bermuda reinsurance subs confirmed (AARe/ALRe/ALReI, BMA-regulated). BMA filing: **AARe gross invested assets $315.1bn (FY2024)**, ALRe $109.1bn. AARe consolidates the ACRA/ADIP sidecar (~63% third-party), so Athene's *economic* Bermuda book < $315bn gross — consistent with $217bn as a net/economic measure. **Independent cross-check:** Athene Holding's NCI = $33.7bn − $17.8bn = **$15.9bn** = the third-party sidecar, confirming the gross-vs-net gap. | [PRIMARY: Athene Bermuda Sub-Group FCR, BMA, FY2024; XBRL NCI] |

---

## Counter-Evidence (mandatory)

1. **Level-3 ≠ toxic / illiquid-junk.** Level-3 is an *input-observability* classification, not a quality grade. A large chunk of Athene's Level-3 is **funds-withheld-at-interest embedded derivatives** (reinsurance, economically a total-return swap on high-grade assets) plus CLOs and structured paper that are largely investment-grade. Athene's *stated* model is to "earn incremental yield by taking measured liquidity and complexity risk **rather than assuming incremental credit risk**." High Level-3 + high leverage is **structurally normal for a fixed-annuity insurer** running a buy-and-hold, long-duration book.
2. **No disclosed AI/data-center linkage.** The fair-value hierarchy is **not broken out by collateral type**. *Nothing in the primary filings ties Athene's Level-3 to "AI-GPU-collateralized or data-center private credit."* The "Athene = hidden AI amplifier" thesis rests on the *Anthropic-SPV "sizable portion"* fact (real but unquantified) and Burry's *inference* diagram — not on a disclosed exposure number. This is the single most important caveat for the insurer-leg question.
3. **The Nvidia–OpenAI $100bn is a non-binding LOI.** Nvidia CFO Kress (early Dec 2025): "we still haven't completed a definitive agreement"; Huang later called the $100bn "never a commitment"/"an invitation." Later reporting (Feb–Jun 2026) indicates a **~$30bn finalized/initial** stake against OpenAI's ~$110bn round. The *structure* is confirmed; the *headline magnitude* is soft.
4. **Collateral nuance.** The Anthropic-SPV chips are **Google TPUs (Broadcom-made), not Nvidia GPUs** — "AI-chip-collateralized" credit is not uniformly Nvidia-GPU collateral, weakening any single-point-of-failure framing centered on Nvidia.
5. **"Off balance sheet" is reversible.** If asset transfers are recharacterized as secured loans (accounting/litigation risk), the leverage comes back on-balance-sheet — i.e. the >$120bn is a *presentation* fact, not necessarily an *economic* de-risking.
6. **Burry figures are attribution, not proof.** The adversarial pass *refuted (0-3)* the same numbers when a secondary outlet relayed them **as fact**, but *accepted (3-0)* them when framed **as Burry's attribution** — a source-quality distinction. The figures originate from Burry's "Cassandra Unchained" Substack (~May 29–31 2026), not from a primary filing. My EDGAR work is what moves them from [UNVERIFIED] to dated/bounded.
7. **Backstops are conditional.** Nvidia's CoreWeave obligation covers only *residual unsold* capacity (a conditional backstop, not an unconditional purchase); the $6.3bn is an order-form cap, not a guaranteed cash outlay.

---

## Source Quality Assessment

**Strong.** The circular-financing *structures* are anchored in genuine primary sources: Nvidia IR, Apollo's own press release, a CoreWeave 8-K (SEC), the Athene Bermuda Sub-Group BMA statutory filing, and my own Apollo/Athene-Holding 10-Q/10-K XBRL pulls. The insurer-leg verification is **primary-source-grade** on the balance-sheet facts (Level-3 totals, leverage, Bermuda gross/net). **Weaker** on: (a) the vendor-financed-vs-end-demand *ratio* (no public denominator); (b) Athene's *exact* AI-chip-credit dollar exposure (private-by-construction — "sizable portion" is the only public quantifier); (c) the Oracle $40bn/400k figure (press-sourced, not a filing); (d) whether Apollo *specifically* securitized the $3.5bn Valor debt *into Athene* (Burry's diagram, unconfirmed against filings). Burry's primary figures are [UNVERIFIED]-origin; treat his numbers as dated contrarian estimates that my EDGAR pull has now bounded.

## References

- [PRIMARY] Nvidia IR — "OpenAI and NVIDIA Announce Strategic Partnership to Deploy 10 GW" (Sep 22 2025). https://investor.nvidia.com/news/press-release-details/2025/OpenAI-and-NVIDIA-Announce-Strategic-Partnership.../default.aspx
- [PRIMARY] Apollo — "Apollo Backs $5.4 Billion Valor and xAI … with $3.5 Billion Capital Solution" (Jan 7 2026). https://www.apollo.com/insights-news/pressreleases/2026/01/apollo-backs-5-4-billion-valor...
- [PRIMARY] CoreWeave Form 8-K, accession 000176962825000047 (event 2025-09-09). https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm
- [PRIMARY] Apollo Global Management 10-Q Q1-2026, accession 0001858681-26-000026 (filed 2026-05-07) — Level-3 roll-forward, total investments. (DEWEY EDGAR pull, `edgar_doc.py`.)
- [PRIMARY] Athene Holding Ltd 10-K FY2024 (accession 0001527469-25-000016) / FY2025 (000152746926000013) + XBRL `Assets`/`StockholdersEquity` (data.sec.gov). (DEWEY pull.)
- [PRIMARY] Athene Bermuda Sub-Group Financial Condition Report, BMA Insurance Act 1978, FY2024 (Deloitte, May 2025). https://www.athene.com/binaries/content/assets/bermuda/about/financials/2025/bermuda-sub-group---2024-financial-condition-report.pdf
- [INSTITUTIONAL] PitchBook/Bloomberg — "Apollo, Blackstone lend $35B against AI chips" (Jun 2026). https://pitchbook.com/news/articles/apollo-blackstone-lend-35b-against-ai-chips-computing-power
- [INSTITUTIONAL] IFR/LSEG + Fortune + Bisnow — Meta/Blue Owl "Hyperion" (Beignet) $27.294bn (Oct 16 2025).
- [NEWS] Quinn Emanuel client alert (FT-sourced) — ">$120B moved off balance sheet in ~18 months." https://www.quinnemanuel.com/.../client-alert-emerging-litigation-risks-in-financing-ai-data-centers-boom/
- [SECONDARY] The Register — "The circular economy of AI" (Nov 4 2025); io-fund — CoreWeave/Nebius circular financing.
- [UNVERIFIED-ORIGIN] M. Burry, "Cassandra Unchained" Substack (~May 29–31 2026), relayed by IBTimes (Jun 1 2026), thedeepdive, 24/7 Wall St — the $217bn/$103bn/34.7%/16.6× figure set.

## Process Report

- **Searches run:** 5-angle fan-out (deal-mapping, insurer-balance-sheet, Burry-verification, quantification, private-credit-SPV) → 24 sources fetched → 94 claims → 25 adversarially verified (21 confirmed, 4 killed). Plus **5 independent DEWEY EDGAR/XBRL pulls** (APO consolidated, Athene Holding standalone, CIK confirmation) — these are what verified the Level-3 and leverage figures the fan-out left open.
- **Data gaps:** (1) **No public denominator** for total 2024–26 AI-buildout capex → cannot produce a vendor-financed-vs-end-demand *ratio* — only a catalogue of discrete large flows. (2) Athene's **exact AI-chip-credit dollar exposure** is private-by-construction. (3) Burry's **exact equity definition** for "16.6×" and **exact denominator** for "34.7%" are undisclosed → reconstructed only to within a range.
- **Source frustrations:** the headline Burry figures live only in secondary/blog relays of a Substack — required the attribution-vs-fact discipline (the engine's 0-3 vs 3-0 split on identical numbers is a clean illustration). The Athene Bermuda book spans **three different consolidation scopes** (Apollo "Retirement Services" segment / Athene Holding consolidated / Athene Bermuda Sub-Group) with different totals — easy to conflate; I kept them labeled.
- **Confidence:** **High** on circular-financing structure and on the *direction* of the insurer-leg facts (Level-3 large and growing; leverage insurer-normal; Bermuda gross $315bn). **Medium** on the precise Burry-figure reconciliation (denominator/equity-definition gaps) and on the AI-collateral linkage (inference, not disclosure).
- **If I had more time/tools:** pull the **Athene Holding FY2024 10-K fair-value footnote directly** to reconstruct the exact 34.7% denominator and confirm the Level-3 split between FWH-derivatives vs private credit; pull the **Athene Bermuda Sub-Group FCR investment-by-rating table** to size the genuinely-illiquid (vs IG-structured) share of Level-3; and a focused pull on **Apollo's "Atlas SP" / Anthropic-SPV** disclosures once a 10-Q captures the June-2026 deal.
- **Suggestions:** add a small **multi-scope insurer cheatsheet** to `scripts/` (the Apollo-segment vs Athene-Holding vs Bermuda-Sub-Group totals reconcile via the ACRA/ADIP NCI) — this conflation will recur on any SHADE/BROCK insurer-nexus work. The BMA statutory FCRs (athene.com PDFs) are a high-value, under-used primary source — worth a `pdf2text.py` recipe for the FCR investment tables.

---
*Routed by WALTER per CHECKLIST Phase 2.8b (2026-06-27, post-crash recovery session). Originating flag REQ-DEWEY-20260627-001 / SIG-W-20260627-008 — DEEP_RESEARCH_FLAGGED_LOG row closed RESOLVED / executor DEWEY. Handoff `AGENTS/WALTER/inbox/DEWEY/2026-06-27_ai-circular-financing_handoff.md` → `processed/`.*
