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
