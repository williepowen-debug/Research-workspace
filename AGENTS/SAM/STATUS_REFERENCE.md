# SAM STATUS — WARM REFERENCE

**Hot/cold split out of `STATUS.md` 2026-09-11**, under the fleet READ-CAP rule
(`AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`). STATUS had reached 13 B of headroom against its 32,550 B
budget — the next session block could not be written without breaching it, and the cheap
prose-compression fix was spent (recorded in MEMORY 2026-09-11).

🟡 **WARM — read ON DEMAND, not at boot.** This is not the cold `STATUS_ARCHIVE.md`: everything here is
**current and citable**. It is split out because SAM's boot protocol reads STATUS's header, top session
block and the `LIVE MARKET DATA` / `KEY THRESHOLDS` / `WHAT TO WATCH` / `PREDICTIONS` sections — these
sections were never in that read, so they consumed budget without being read.

⚠️ **Live state stayed in STATUS.** Each section below leaves a pointer in `STATUS.md` carrying its
one-line current state; what moved here is the accumulated evidence, method and durable reference
detail behind it. Read this file whenever a claim turns on intervention evidence, the carry-unwind
method's vintage, channel/policy interpretation, or a durable reference figure.

⛔ **Verbatim move, no edits to the analytical content.** Checked before moving: no external consumer
cites these section names (the `↪️ MOVED:` redirects that peers DO cite deliberately stayed in STATUS).

---

## 📌 DURABLE REFERENCE ROWS
*(moved from `STATUS.md` § LIVE MARKET DATA — stable, slow-moving figures, not live market data)*

**Durable reference rows:** 🆕 **AUGUST CGPI — 2026-09-11 08:50 JST, BOJ `cgpi2608.pdf`, own primary: PPI −0.2% m/m / **+7.6% YoY**; Import PI **yen basis −3.0% m/m / +24.8% YoY**, contract-currency **−1.0% m/m / +16.7% YoY**; **petroleum/coal/natural gas contributed −1.18pp** to the contract-currency monthly fall (crude petroleum, naphtha, LPG); FX column −2.4% m/m (yen appreciation).** ⇒ **in August Japan's import prices FELL in both currencies and terms of trade IMPROVED; oil was the largest single DRAG.** The September oil shock reaches none of the 9/11 CGPI, the 9/16 trade balance or the 9/18 National CPI. 🔧 **The same primary shows July PPI +7.7% r and June +7.4% — this file's earlier 7.2%/7.1% pair (8/13 release) is SUPERSEDED; do not cite it.** · BOJ subsidy-stripped trend gauge 2.8% [Apr] vs official core 1.4% · insurer hedge ratio 44.4% [Mar 2025, 14-yr low] · Tankan Q2 +22 [6/30] · **JAPAN JULY CPI — 2025-BASE, canonical: National headline 1.9 / core 1.8 / core-core 1.9 · Tokyo 1.8 / 1.7 / 1.8** [rel 8/21, e-Stat primary]. ⛔ The 2020-base pair is SUPERSEDED — **never compare across bases**. ⛔ The "Tokyo running ABOVE national" read is RETIRED as a BASE ARTIFACT (2025-base: Tokyo ≤ National 6 of 6). ⚠️ **SCOPE: CORE-CORE ONLY.** · **Japan JULY TB −¥634.5B** (imports +27.8%, crude value +87.8% YoY, **crude VOLUME +5.5%**; crude 12,106 kKL ≈ **76.1 M bbl/mo ≈ 2.46 mb/d**, value **¥1,408.9B**) — **August prints Sep-16, and VOLUME is the discriminator.**

---

---

## CARRY UNWIND PROBABILITY (decomposed estimate — method → `thesis/THESIS.md` § CARRY-UNWIND PROBABILITY METHOD)

**Last assessed August 7: 7d ~3 / 30d ~8 / 60d ~13. Historical assessment, not a fresh rolling forecast.** Amplifier and residual OFF at that assessment; no re-pencil this session. Historical drivers and prior marks → `STATUS_ARCHIVE.md`. Future re-pencils must update all changed anchors; >5pp changes require named drivers. The method's intervention-causing-unwind framing omits the countervailing no-cap/overshoot path. Disclose as a decomposed estimate, never "true probability." No retired entry gate re-arms.

---

## INTERVENTION STATUS — MOF posture

**Sep-7/8 attribution remains OPEN. Sep-9 and Sep-10 legs both CLOSED.** Sep-10 provisional: fiscal +¥340B vs projection +¥220B (residual +¥120B); balance ¥412.71T — **no yen-buying signature** (an op *drains* yen and prints large NEGATIVE; this is a net supply, wrong direction, residual trivial). **Sep-9 FINAL −¥3,590B = provisional**, +¥10B vs Ueda Yagi's Sep-3 forecast ⇒ closed as anticipated fiscal. **Sep-8 final −¥1,100B vs Ueda +¥100B (−¥1,200B) / BOJ −¥560B (−¥540B) stays unexplained** — a forecast miss is never an operation size. ⚠️ Japan's settlement instrument **cannot exclude a U.S.-only operation**. Official words: Katayama 9/8 stance "hasn't shifted"; Bessent 9/9 (secondary quote). Evidence → `reports/2026-09-10_et-boot.md` §2; **`MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A governs**.

**Funding — unresolved, and the 9/6 Bloomberg story does not resolve it.** MOF officially reported **¥15,399.3B for Jul-30–Aug-26** (rel Aug-28): Japan-side aggregate only, no daily split and no U.S. euro-leg amount. Earlier official windows: Apr-28–May-27 ¥11,734.9B; Jun-29–Jul-29 ¥0. August reserve **securities fell $87.773B** and deposits $6.868B (rel Sep-8) — a securities-funding *hypothesis*, **not identified UST sales**, given valuation/FX effects and mismatched stock/intervention windows. 🆕 **The $87.8B fall is ~$10.8B SHORT of the ~$98.6B intervention** — consistent with a joint US leg AND with mark-to-market on a rising-yield month. The FIMA-funded claim was retracted; the historical H.4.1 test found no foreign-official repo use. FRBNY Q3 (~Nov-13) addresses the U.S. account split; MOF's quarterly per-op disclosure (~Nov-9) gives the Japan-side per-op record. Details: KB-SAM-209. Monthly path uses `reference/feio/monthly/`, not `feint`; BOJ projections `jp`, provisional `jx`, final `jd`.

**Aug-3 detector disagreement remains an ambiguity:** 2.67y range exceeded the >2.5y detector bar while final settlement −¥3.29T read ordinary. Post-operation elevated ranges and the invisible U.S.-only route prevent attribution. Unchanged disorder watch: ≥1.5–2% in a day or ~2–3 yen over 1–2 sessions. **Silence is not a safety signal.** Frozen confirmation ladder and preregistered bands → `thesis/INTERVENTION_2026-07-30_CONFIRMATION.md` (registered before reads, commit `aa3ad1980`); full history → `STATUS_ARCHIVE.md`. Preserve these external citation targets.

---

## CHANNELS · BOJ · FED

Canonical mechanism and policy interpretation → `thesis/THESIS.md` and September 8 assessment. Channel 1 requires direct foreign sales at ≥2 institutions across ≥2 consecutive windows; yields and ESR are co-conditions, never substitutes. Sector aggregates cannot update named company profiles. Carry-convexity/positioning frames remain retired. BOJ policy rate is 1.00%; July hold was 8–1 with Takada favoring 1.25%. Current pricing belongs only in LIVE MARKET DATA. Political rhetoric, policy surprise and FX transmission remain distinct.

**September MPM state (sources Sep-10, report §5–6; the forward READ is in the 9/11 L34 block above).** Masu (Sep-10, primary) — policy rate "below the estimated range" of neutral (1.1–2.5%), "the Bank will continue to raise the policy interest rate," pace keyed to **oil**, AI demand and FX; balance sheet halt-the-reduction from FY2027 at ~¥2T/mo (the June-MPM plan). Ueda 9/2, Takata 9/2, Himino 8/26, Aida 9/7 ("narrow window" before the early-Oct Diet), Katayama 9/8; Reuters via FXStreet 9/11 "set to raise by 25bp next week." Fed: Waller 9/3 HOLD-unless-CPI-hot. All secondary press except Masu and the BOJ/MOF primaries named in the report.
