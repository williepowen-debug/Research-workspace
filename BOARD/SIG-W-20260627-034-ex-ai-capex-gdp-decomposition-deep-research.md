---
signal_id: SIG-W-20260627-034
dispatched: 2026-06-27T21:05:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260627-002 — ex-AI-capex GDP decomposition) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-06-27
source: DEWEY report `AGENTS/DEWEY/output/2026-06-27_ex-ai-capex-gdp.md` (Mode Thesis / Confidence High on direction+decomposition, Low on the specific "−1.1%" figure [refuted as a vintage/method artifact]; `/deep-research` 106-agent fan-out [23 sources, 25 claims adversarially verified, 5 killed] + an independent DEWEY BEA-NIPA/FRED primary pull that reconstructs + EXTENDS the St. Louis Fed AI-contribution series past its Q3-2025 endpoint)
signal_type: research-output
domain: MACRO_INFLATION
cluster: CONSUMER_STAGFLATION
cluster_secondary: AI_INFRA_CAPEX
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [CARL]
info: [HENRY, RED, BROCK]
confidence: 0.85
verify_verdict: VERIFIED-PRIMARY. The headline-vintage sequence, the full Q1-2026 contribution decomposition, and the AI-contribution reconstruction+extension are all PRIMARY (BEA 3rd-estimate release + FRED NIPA Table 1.1.2 contribution series, DEWEY-pulled 2026-06-27). The "−1.1% ex-AI contraction" figure is REFUTED-as-artifact (not reproducible from any primary; pairs an ex-AI residual with the now-stale +1.6% 2nd estimate — final Q1 was revised UP to +2.1%). No WALTER verify-spawn (Phase 2.8b — deep-research deliverable already primary-verified + adversarially passed). DOWN-WEIGHT one input: the construction-channel magnitudes lean on ConstructConnect, a single vendor whose "nonresidential buildings" aggregate is not coextensive with BEA NIPA nonres structures.
verify_method: none — deliverable is a `/deep-research` synthesis + independent DEWEY BEA-NIPA/FRED pull. WALTER routes + extracts per-recipient genuine delta (lean mandate — no re-analysis). Caveats carried through verbatim, not re-derived.
deep_research_ref: REQ-DEWEY-20260627-002 / originating signal SIG-W-20260627-017 (the "ex-AI economy contracted −1.1%" dispatch). Closes the DEEP_RESEARCH_FLAGGED_LOG row for REQ-DEWEY-20260627-002 (disposition RESOLVED / executor DEWEY). 2nd of the Will-approved 6/27 4-prompt batch to return (after REQ-001→SIG-033); REQ-003 muni-fiscal + REQ-004 housing-distress remain PENDING.
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. ONE research-output signal — split test S1–S4 on the "AI-capex re-accelerated to ~1.5 ppt in Q1-26" finding (the one carve-out candidate, of interest to HENRY): all FAIL — S1 (HENRY-info-relevant but it's a leg of the same decomposition + the deliverable's decision-question is CARL's recession-timing, not a standalone HENRY decision), S2 (no registered trigger), S3 (same Q1-26 GDP-vintage clock), S4 (surfaced as the HENRY info-delta → precedence note, no forced split). Mirrors SIG-619-008 / SIG-033 (kept-in + elevated). Cluster-primary CONSUMER_STAGFLATION (the deliverable's real signal is the consumer, and the originating SIG-017 was CONSUMER_STAGFLATION), secondary AI_INFRA_CAPEX; signal_role cluster_mediating (paper-vs-substance: headline +2.1% vs ex-AI ~0; + the number-refuted-but-direction-intact correction + full counter-evidence section) → RED auto-cc. Honors DEWEY's "route as VERIFIED-PRIMARY, close the REQ-002 ledger row on route" flag.
---

# Ex-AI-capex GDP decomposition — is "the economy ex-AI is already contracting" fact or artifact? (DEWEY deep-research; resolves SIG-017)

This routes the 2nd returned deliverable of the Will-approved 6/27 DEWEY batch. It answers SIG-W-20260627-017's question — is the "US real GDP ex-AI-capex contracted ~−1.1% Q1-26 while headline stayed +1.6%" claim load-bearing or a fragile artifact? **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis; the packet is the analysis.** Full report embedded verbatim below the wrapper.

> ⚠️ **GRADE: VERIFIED-PRIMARY, but the headline-claim it tests is REFUTED.** The decomposition, vintage sequence, and AI-contribution series are PRIMARY (BEA/FRED). The specific "−1.1%" is **not reproducible** — it pairs an ex-AI residual with the *stale* +1.6% 2nd estimate, and the final Q1 print was revised **UP to +2.1%** (Jun 25). Down-weight one input only: the construction-channel magnitudes are single-vendor (ConstructConnect).

## Verdict (one line)
**The specific "−1.1%" is the artifact; the direction is load-bearing.** Off the actual +2.1% final print, stripping the full AI-capex contribution leaves ex-AI growth **~+0.5% to +0.8% — sharply decelerating, NOT contracting** (−1.1% would require removing ~3.2 ppt, more than all gross private investment combined — i.e. a *modeled* broad AI-GDP, not a NIPA-direct fact). The genuinely alarming primary signal isn't the "ex-AI" abstraction — it's the **consumer**: PCE's growth contribution collapsed **+2.34 → +1.30 → +0.37 ppt** (Q3-25 → Q1-26). And AI-investment's contribution **troughed at 0.48 ppt in Q3-25 then RE-ACCELERATED to ~0.97 (Q4-25) and ~1.50 ppt (Q1-26)** — the economy is *more* AI-capex-dependent for growth, not less.

---

## Per-recipient genuine delta (routing wrapper)

### → CARL (ACTION) — your recession/stagflation-timing thesis: the number is wrong, the direction is yours, and the real signal is the consumer
1. **Correction to bank (don't carry the −1.1%):** "ex-AI contracted −1.1%" is **not reproducible** — it's an unattributed extension of Furman's data-center-strip method, paired with the **stale +1.6% 2nd estimate**. The **3rd/final Q1-26 print was revised UP to +2.1%** (Jun 25). Stripping AI-capex off the real print leaves ex-AI **~+0.5–0.8% (decelerating, not contracting)**. Lead with this so the thesis doesn't rest on a refuted figure.
2. **Load-bearing delta — the CONSUMER is the clean signal, not "ex-AI":** PCE's contribution collapsed **+2.34 (Q3-25) → +1.30 (Q4-25) → +0.37 ppt (Q1-26)**; residential −0.30. **Real final sales to private domestic purchasers** (the cleanest private core-demand gauge) = +1.7% Q1-26 and was **revised DOWN 0.7 ppt** in the 3rd estimate — the *opposite* direction to the headline.
3. **The headline upgrade is hollow:** the +0.5 ppt 2nd→3rd revision came mainly from a **downward import revision (a trade effect)** while **domestic consumer spending was revised DOWN** — so the firmer +2.1% headline *overstates* domestic-demand strength. This strengthens, not weakens, your deceleration read. (Furman: ex-data-centers, H1-2025 grew ~0.1%.)

### → HENRY (INFO) — AI-capex is carrying even more of the tape, and it re-accelerated
- **AI/tech-capex ≈ 60–75% of Q1-26 growth.** NEW (DEWEY extension of the St. Louis Fed series past its Q3-25 endpoint, validated by exact-match on overlapping quarters): the AI-investment contribution **troughed at 0.48 ppt (Q3-25) → ~0.97 (Q4-25) → ~1.50 ppt (Q1-26)** — it **rebounded**, which is *why* the ex-AI residual looks weak again. This quarter the prop came via **equipment (computers/peripherals) + software/IP**, while **structures (where data-center *construction* sits) was a net DRAG** (−0.13 ppt). Recession-timing read: ex-AI near-flat, growth ever-more AI-capex-levered — but **don't bank −1.1%** (vintage/definition-fragile).

### → RED (INFO) — two-sided / adversarial
- The "−1.1%" **failed verification** (no primary published a Q1-26 ex-AI decomposition; the canonical series stop at Q3/Q4-25). But cutting the *other* way: 5 claims that **private demand *accelerated* to +2.4–2.5%** were also adversarially **killed (0-3)** — they used advance/2nd-estimate vintages later revised down. Every broad demand aggregate stayed **positive** (real final sales to domestic purchasers +2.2%, all four quarters positive) — but those **include** AI capex (the base to subtract from), so they're not ex-AI measures. "Ex-AI" is a **counterfactual, not a cleanly-removable sector** (double-discount risk). Net: vintage-fragility is the meta-lesson on *both* sides.

### → BROCK (INFO) — AI-capex-as-only-growth-engine / fragility
- Corporate capex "would be negative without AI" (Pantheon, Feb-26); ex-AI growth is near-flat and the AI-investment contribution **re-accelerated** into Q1-26 → the real economy is *more* dependent on the AI-capex cycle for top-line growth. Ties your AI-financing-fragility work (SIG-033) to the macro: if the buildout that's vendor/circular-financed rolls, the growth it's been supplying rolls with it. Construction-channel magnitudes (data centers = 42% of 2025 NRB construction growth; ex-DC, NRB forecast −3.8% in 2026) are single-vendor (ConstructConnect) → down-weight.

---

## Full research packet (verbatim, as delivered by DEWEY 2026-06-27)

# Ex-AI-Capex US Real Economy — Is "GDP ex-AI is already contracting" a Fact or an Artifact?

**Date:** 2026-06-27 | **Mode:** Thesis | **Confidence:** High (direction + decomposition) / Low (the specific "−1.1%" figure — refuted as a vintage/method artifact)
**Flag:** REQ-DEWEY-20260627-002 / SIG-W-20260627-017 | **Clusters:** CONSUMER_STAGFLATION
**Engine:** `/deep-research` (106-agent fan-out, 23 sources, 25 claims adversarially verified, 5 killed) + an independent DEWEY BEA-NIPA primary pull (FRED contribution series) that reconstructs and **extends the St. Louis Fed AI-contribution series past its Q3-2025 endpoint**.

---

## Key Finding

The specific claim — **"US real GDP ex-AI-capex contracted ~−1.1% annualized in Q1-2026 while headline stayed ~+1.6%"** — is **not reproducible from primary sources** and rests on a superseded headline vintage. The "+1.6%" was BEA's **second** estimate; the **third/final estimate (released June 25 2026) revised Q1-2026 real GDP UP to +2.1%**. Stripping the entire direct AI/tech-capex contribution from the actual +2.1% print leaves ex-AI growth of **roughly +0.5% to +0.8% — sharply decelerating, but positive, not contracting.** To reach −1.1% you must remove ~3.2 ppt, which exceeds *all* gross private investment combined; that requires a broad *modeled* "AI-related GDP" (capex **plus** construction/electrical/energy/induced-consumption multipliers) — the aggressive tail, not a primary fact.

**But the direction is solid and load-bearing.** AI-related investment is ~60–75% of Q1-2026 growth, it **troughed in Q3-2025 and re-accelerated into Q1-2026**, and on the narrowest defensible read ex-AI growth is *near zero*. The genuinely alarming primary signal is not the "ex-AI" abstraction but the **consumer**: PCE's contribution collapsed from +2.34 ppt (Q3-25) to **+0.37 ppt (Q1-26)**.

---

## Evidence

### A. The headline itself is a moving target (vintage flag)

| Q1-2026 real GDP, % SAAR | Estimate | Released |
|---|---|---|
| +2.0% | Advance | Apr 30 2026 |
| **+1.6%** | **Second (← the SIG's figure)** | May 28 2026 |
| **+2.1%** | **Third / final (latest)** | **Jun 25 2026** |

`[PRIMARY: BEA GDP Third Estimate, Q1 2026, Jun 25 2026]` `[PRIMARY: FRED A191RL1Q225SBEA = 2.1]`. The +0.5 ppt upward revision (2nd→3rd) was driven mainly by a **downward import revision** (a net-exports/trade effect), while **domestic consumer spending was revised DOWN** `[PRIMARY: BEA 3rd-estimate release]`. Implication that *strengthens* the bear read: the firmer headline **overstates domestic-demand strength** — the upgrade came from trade, not from the real economy.

Quarterly context `[PRIMARY: FRED A191RL1Q225SBEA]`: Q1-25 **−0.6** · Q2-25 **+3.8** · Q3-25 **+4.4** · Q4-25 **+0.5** · Q1-26 **+2.1**.

### B. Full primary decomposition of the +2.1% Q1-2026 print (reconciles exactly)

Contributions to the % change in real GDP, ppt SAAR `[PRIMARY: BEA NIPA Table 1.1.2 via FRED, latest vintage, pulled 2026-06-27]`:

| Component | ppt | FRED series |
|---|---:|---|
| Personal consumption (PCE) | **+0.37** | DPCERY2Q224SBEA |
| Nonresidential fixed investment | **+1.42** | A008RY2Q224SBEA |
| — Equipment | +0.81 | Y033RY2Q224SBEA |
| —— Information-processing equipment | +0.77 | Y034RY2Q224SBEA |
| ——— Computers & peripherals | +0.59 | B935RY2Q224SBEA |
| — Intellectual property products | +0.74 | Y001RY2Q224SBEA |
| —— Software | +0.52 | B985RY2Q224SBEA |
| —— R&D | +0.21 | Y006RY2Q224SBEA |
| — Structures (residual) | −0.13 | (1.42−0.81−0.74) |
| Residential investment | −0.30 | A011RY2Q224SBEA |
| Change in private inventories | +0.23 | A014RY2Q224SBEA |
| Net exports | −0.37 | A019RY2Q224SBEA |
| Government | +0.74 | A822RY2Q224SBEA |
| **Total real GDP** | **+2.10** | A191RL1Q225SBEA |

The Q1-2026 investment gain ran **through equipment (computers/peripherals) and software/IP; both residential and nonresidential structures DECLINED** (nonres led by manufacturing structures) `[PRIMARY: BEA 3rd-estimate release]`. So in this quarter the AI prop came via *equipment*, while *structures* (where data-center construction sits) was a net **drag**.

### C. The AI/tech-capex contribution — and the new finding: it RE-ACCELERATED into Q1-2026

The canonical decomposition is the **St. Louis Fed** (Rubinton & Patro, Jan 2026): AI-related investment = information-processing equipment + software + R&D + Census data-center construction, contribution computed via Fisher-Törnqvist. Their published series: **Q1-25 1.3 ppt · Q2-25 1.16 ppt · Q3-25 0.48 ppt** (= 30% of Q2 and 11% of Q3 growth; "helped prevent a sharper contraction in Q1-2025"). **That series ENDS at Q3-2025** `[PRIMARY/INSTITUTIONAL: St. Louis Fed, "Tracking AI's Contribution to GDP Growth," Jan 2026]`.

**DEWEY extension (value-add).** Reconstructing the same bucket from BEA published contributions (info-proc equipment + software + R&D; ex the data-center-construction add-on, which is bundled inside structures on FRED) reproduces the Fed's series almost exactly — then carries it two quarters further `[PRIMARY data, DEWEY-computed from FRED RY2 contribution series]`:

| Quarter | DEWEY (IPE+software+R&D) | St. Louis Fed published |
|---|---:|---:|
| Q1-25 | 1.25 | 1.3 ✓ |
| Q2-25 | 1.02 | 1.16 ✓ |
| Q3-25 | **0.48** | **0.48 (exact)** |
| Q4-25 | **0.97** | *series ends* |
| Q1-26 | **1.50** | *series ends* |

The near-exact match (and the residual ≈ the data-center-construction piece the Fed adds) validates the reconstruction. The new result: **the AI-investment contribution troughed at 0.48 ppt in Q3-2025, then re-accelerated to ~0.97 ppt (Q4-25) and ~1.50 ppt (Q1-26)** — adding data-center construction puts Q1-26 at ~1.5–1.6 ppt. This directly answers the open question of whether AI capex kept fading or rebounded: **it rebounded**, which is *why* the ex-AI residual looks weak again in Q1-2026.

**Ex-AI residual, by definition used** (off the +2.1% headline):

| AI-capex definition | ppt | % of growth | Ex-AI growth |
|---|---:|---:|---:|
| Narrow (info-proc equip + software) | 1.29 | 61% | **+0.81%** |
| St. Louis Fed (≈ equip + software + R&D + DC constr.) | ~1.55 | ~74% | **~+0.55%** |
| All nonresidential fixed investment | 1.42 | 68% | +0.68% |

Off the **old +1.6% vintage**, the St. Louis Fed-style strip lands ex-AI growth at **~0.0%** — matching Harvard's **Jason Furman**, the originator of this whole framing, who found that excluding data centers, **H1-2025 GDP grew ~0.1% annualized** `[NEWS/INSTITUTIONAL: Fortune, "Without data centers, GDP growth was 0.1% in H1-2025," Oct 7 2025, citing Furman]`. The "−1.1%" appears to be an unattributed extension of Furman's method to Q1-2026 — its source is **not traceable to any verified release**, and it pairs an ex-AI residual with the now-stale +1.6% headline.

### D. The consumer is the real signal (and corroborates CARL)

- **PCE contribution collapsed:** Q3-25 +2.34 → Q4-25 +1.30 → **Q1-26 +0.37** ppt `[PRIMARY: FRED DPCERY2Q224SBEA]`. Residential −0.30.
- **Real final sales to private domestic purchasers** (PCE + private fixed investment — the cleanest *private* core-demand gauge, *inclusive* of AI capex): Q2-25 +2.9 · Q3-25 +2.9 · Q4-25 +1.8 · **Q1-26 +1.7%**, and was **revised DOWN 0.7 ppt** in the 3rd estimate — the opposite direction to the headline `[PRIMARY: BEA 3rd estimate; FRED PB0000031Q225SBEA / LB0000031Q020SBEA]`.
- **Pantheon** (Oliver Allen, Feb 2026): corporate capex "would be negative without" AI; AI-related sectors ≈ 0.3 ppt of the ~2.5% average growth across Q1–Q3 2025 `[NEWS/INSTITUTIONAL: Fortune/Pantheon, Feb 23 2026]`.
- **Construction channel:** data centers were **42% of 2025 nonresidential-building construction-spending growth**; ex-data-centers, NRB spending is forecast to **decline 3.8% in 2026** `[INSTITUTIONAL/vendor: ConstructConnect]` — directionally corroborated by Census C30 and Wolf Street, but a proprietary aggregate (see caveats).

---

## Counter-Evidence (mandatory)

1. **Every broad demand aggregate stayed positive — and they refute the "contracting" read at face value.** Real final sales to *domestic* purchasers grew **+2.2%** in Q1-26 (and was positive all four quarters: +2.4/+2.8/+0.6/+2.2); real final sales to *private* domestic purchasers **+1.7%**. The economy *as measured* did not contract. The "ex-AI contraction" only appears once you subtract AI capex — and these aggregates *include* it, so they are the **base to subtract from**, not ex-AI measures themselves.
2. **The "−1.1%" specific figure failed verification.** No primary or institutional source published a Q1-2026 ex-AI decomposition; the St. Louis Fed stops at Q3-25, Pantheon at Q4-25. Five claims asserting private final demand *accelerated* to +2.4–2.5% were **adversarially killed (0-3)** — but only because they used *advance/2nd-estimate vintages* later revised down, which cuts the other way (it shows how vintage-fragile any single number is).
3. **Method sensitivity is large.** The St. Louis Fed explicitly flags that **not all R&D is AI-related**; including all of it overstates AI, excluding it understates. The ex-AI residual swings materially with classification (R&D alone is ~0.2 ppt/quarter).
4. **AI capex IS real GDP.** "Ex-AI" is a counterfactual, not a sector that can be cleanly removed — the data-center buildout pulls through real construction, electrical equipment, and employment. Treating it as subtractable risks double-discounting genuine activity.

---

## Source Quality Assessment

Strong where it matters: the headline, the full contribution decomposition, the vintage sequence, and the AI-contribution reconstruction are **all PRIMARY (BEA/FRED)**. The AI-framing attribution (Furman H1-25, St. Louis Fed, Pantheon) is INSTITUTIONAL/NEWS with named attribution. Weakest link: the construction-channel magnitudes lean on **ConstructConnect**, a vendor forecast whose "nonresidential buildings" aggregate is *not* coextensive with BEA NIPA nonresidential structures (which adds power/utility, drilling, communications), and is likely nominal. **No source computed an ex-AI figure for Q1-2026** — DEWEY's extension is the closest reconstruction, and it's a published-contributions proxy for the Fed's Fisher-Törnqvist method, not an identical recomputation.

---

## References

- BEA, GDP 3rd Estimate Q1-2026 (Jun 25 2026): https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-1st
- BEA, GDP 2nd Estimate Q1-2026 (May 28 2026): https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-1st-quarter-2026
- BEA, GDP Advance Estimate Q1-2026 (Apr 30 2026): https://www.bea.gov/news/2026/gdp-advance-estimate-1st-quarter-2026
- St. Louis Fed, "Tracking AI's Contribution to GDP Growth" (Rubinton & Patro, Jan 2026): https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth
- Fortune / Furman, "Without data centers, GDP growth was 0.1% in H1-2025" (Oct 7 2025): https://fortune.com/2025/10/07/data-centers-gdp-growth-zero-first-half-2025-jason-furman-harvard-economist/
- Fortune / Pantheon, "AI capex … US GDP negative" (Feb 23 2026): https://fortune.com/2026/02/23/ai-capex-us-gdp-negative-pantheon/
- ConstructConnect, "Seeing nonresidential building growth and data centers clearly": https://news.constructconnect.com/seeing-nonresidential-building-growth-and-data-centers-clearly
- FRED series (accessed 2026-06-27): A191RL1Q225SBEA, DPCERY2Q224SBEA, A006RY2Q224SBEA, A008RY2Q224SBEA, Y033/Y034/B935/A937RY2 (equipment), Y001/B985/Y006RY2 (IPP), A011/A014/A019/A822RY2, PB0000031Q225SBEA, LB0000031Q020SBEA, A713RL1Q225SBEA.

---

## Process Report

**Searches run:** 6 angles → 23 sources fetched → 97 claims → 25 adversarially verified (20 confirmed, 5 killed), plus an independent DEWEY FRED pull of ~18 BEA contribution series. The fan-out nailed the source attribution (Furman genealogy, St. Louis Fed, BEA vintages); the FRED pull supplied the reconciled decomposition and the series extension the web sources lacked.
**Data gaps:** No published ex-AI GDP figure for Q1-2026 exists — both canonical series stop at Q3/Q4-2025. The DEWEY extension fills it as a published-contributions reconstruction (validated against the Fed's series), not an official number. Census data-center construction line could not be cleanly isolated from FRED's bundled structures contribution (it lives in the C30 release; would need a direct Census pull to split the ~0.1 ppt data-center-construction add-on).
**Source frustrations:** St. Louis Fed 403s on direct WebFetch (verified via Wayback) — a known pattern, but it's a *Fed* page not SEC, so not the EDGAR-UA fix in BACKLOG. The BEA "advance-estimate" URL had been overwritten with third-estimate content (vintage trap — the URL slug lies about the vintage). ConstructConnect is the only source for the headline construction stat.
**Confidence in findings:** HIGH on direction, the decomposition, the vintage correction, and the re-acceleration; LOW on the specific "−1.1%" (refuted as an artifact); MEDIUM on the construction-channel magnitudes (single vendor source).
**If I had more time/tools:** pull Census C30 data-center construction directly to split the structures contribution and compute the *full* St. Louis Fed bucket (incl. DC construction) for Q4-25/Q1-26; pull ALFRED 2nd-estimate-vintage contributions to reproduce the ex-AI residual off the exact +1.6% vintage; find the literal origin of the "−1.1%" figure (likely an X/Substack post extending Furman).
**Suggestions:** A `scripts/bea_nipa.py` helper that pulls a named set of Table-1.1.2 contribution series and computes "AI bucket vs ex-AI residual" off the latest vintage would make this a one-command refresh each GDP release — this decomposition will be asked again every quarter.

---
*Routed by WALTER per CHECKLIST Phase 2.8b (2026-06-27). Originating flag REQ-DEWEY-20260627-002 / SIG-W-20260627-017 — DEEP_RESEARCH_FLAGGED_LOG row closed RESOLVED / executor DEWEY. Handoff `AGENTS/WALTER/inbox/DEWEY/2026-06-27_ex-ai-capex-gdp_handoff.md` → `processed/`.*
