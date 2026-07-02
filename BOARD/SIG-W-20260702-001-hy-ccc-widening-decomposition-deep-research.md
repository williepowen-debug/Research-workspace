---
signal_id: SIG-W-20260702-001
dispatched: 2026-07-02T23:00:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260702-001 — Batch-2 prompt 05, June HY/CCC widening decomposition) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-02
source: DEWEY report `AGENTS/DEWEY/output/2026-07-02_hy-ccc-widening-decomposition.md` (Mode Thesis / Confidence High on leg (a) index mechanics + leg (b) sector attribution, Medium on leg (c) headline figures; two `/deep-research` workflows [206 agents] + DEWEY independent primary pass — FRED full-history 4 OAS series, EDGAR 8-Ks [6/1, 6/18, 6/25], ICE Bond Index Methodology, SPDR JNK holdings)
signal_type: research-output
domain: MACRO_INFLATION
cluster: AI_INFRA_CAPEX
cluster_secondary: PC_STRESS
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [VIOLET, LIQUID]
info: [RED, TERRY, HENRY, BOND]
confidence: 0.80
verify_verdict: VERIFIED-PRIMARY on leg (a) index mechanics (ICE methodology lock-out arithmetic + FRED tape + EDGAR 8-Ks — DISH 6/30 Ch11 filed AFTER the 6/25 June lock-out → does NOT exit until the 7/31 rebalance; 7/1 CCC print is NOT ex-DISH) and leg (b) sector attribution (4 independent named institutions: Nuveen wk-6/26, Man Group, Lord Abbett, PGIM). The two headline composition figures (8.3% tech/AI share of HY, 10.3% of IG) are UNVERIFIED — no originating source; 8.3% HY in tension with Bloomberg "tech <5% of junk" + DEWEY's JNK pull (~1-2.5% identifiable software) → likely definitional (broad tech/AI/media/telecom vs narrow GICS); the ~10% IG magnitude IS corroborated (Janus Henderson Dec-25, PineBridge). DEWEY primary correction: the "record CCC−BB dispersion ~8.06" is NOT a record gap (8.31 printed Apr-2025); the window-record is the CCC/BB RATIO (6.07× on 6/22). No WALTER verify-spawn (Phase 2.8b — deep-research primary-verified, 2 competing theories refuted 0-3 in-run).
verify_method: none — deliverable is two `/deep-research` workflows + independent DEWEY FRED/EDGAR/ICE/JNK primary pull. WALTER routes + extracts per-recipient genuine delta (lean mandate — no re-analysis). Caveats carried verbatim.
deep_research_ref: REQ-DEWEY-20260702-001 (Batch-2 prompt 05) / decision gates VIOLET Gate A + Bin-A (7/6, 7/10), LIQUID X1 >280 composition discriminator, LIQUID Gate C breadth. Closes the DEEP_RESEARCH_FLAGGED_LOG row for REQ-DEWEY-20260702-001 (disposition RESOLVED / executor DEWEY). 1st of the 13-prompt Will-approved Batch-2 to return (with REQ-002→SIG-W-20260702-002 this same boot).
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. ONE research-output signal (legs (a) mechanics + (b) sector + (c) holder-base are one "genuine sector-driven, NOT a DISH composition artifact, Gate A should NOT stand down" verdict). Cluster-primary AI_INFRA_CAPEX (the June widening IS the late-June AI-equity selloff transmitting equities→credit, Nasdaq −4% 6/26 — keeps it on the AI-capex-bear evidence chain), secondary PC_STRESS (credit-bifurcation / CCC-tail dispersion). signal_role cluster_mediating (composition-vs-genuine discriminator + the "record 8.06 dispersion" framing-correction + the DISH-still-in-index premise correction) → RED auto-cc. ACTION = VIOLET (Gate A) + LIQUID (X1). **Full DEWEY report is durable in-repo at the `source:` path (committed) — this BOARD file carries the tape table + per-recipient deltas + verdict rather than re-embedding the ~140-line packet verbatim (both artifacts live in one repo; a reference is sufficient for durability). Non-verbatim-embed is a deliberate, documented deviation from the prior-batch embed pattern.**
---

# June HY/CCC widening decomposition — GENUINE sector-driven, NOT a DISH composition artifact; Gate A should NOT stand down (DEWEY deep-research)

This routes the 1st returned deliverable of the Will-approved 13-prompt DEWEY Batch-2. It answers whether the June CCC widening is a genuine credit move or a DISH-index composition artifact (should Gate A stand down as a composition false-fire), and supplies the LIQUID X1 composition discriminator. **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis.** Full report in-repo at `AGENTS/DEWEY/output/2026-07-02_hy-ccc-widening-decomposition.md`.

> ⚠️ **GRADE: VERIFIED-PRIMARY on leg (a) mechanics + leg (b) sector; the two headline figures (8.3% HY / 10.3% IG tech share) are UNVERIFIED. The "record CCC−BB dispersion 8.06" is a record RATIO (CCC/BB 6.07×), NOT a record gap.**

## Verdict (one line)
**The June CCC widening is a GENUINE, sector-driven move — an AI-related equity selloff (Nasdaq −4%, peak 6/26) spilling into credit — NOT a DISH composition artifact. Gate A should NOT stand down as a composition false-fire.** DISH is still IN the index until the 7/31 rebalance (its 6/30 Ch11 filing landed AFTER the ~6/25 June lock-out), so the 7/1 CCC print is NOT ex-DISH and the mechanical removal delta is a *future* July event.

## The tape (DEWEY FRED primary pull, 7/1 data published 7/2 — verbatim)

| Date | HY (H0A0) | CCC (H0A3) | BB | IG | CCC−BB | CCC/BB | CCC/HY |
|------|-----------|------------|----|----|--------|--------|--------|
| 6/17 | 263 | 939 | 156 | 74 | 7.83 | 6.02× | 3.57× |
| 6/22 | 265 | 947 | 156 | 74 | 7.91 | **6.07×** | **3.57×** |
| 6/26 | **283** | **973** | 173 | 77 | 8.00 | 5.62× | 3.44× |
| 6/29 | 280 | 967 | 169 | 76 | 7.98 | 5.72× | 3.45× |
| 6/30 | 275 | 970 | 164 | 76 | **8.06** | 5.91× | 3.53× |
| **7/1** | **274** | **968** | **163** | **76** | 8.05 | 5.94× | 3.53× |

CCC peaked **6/26** (four days *before* the 6/30 bankruptcy) and has since drifted — the widening did NOT extend into the 7/1 print. HY printed **283 on 6/26 (above the 280 X1 line) and exactly 280 on 6/29** before retracing to 274.

---

## Per-recipient genuine delta (routing wrapper)

### → VIOLET (ACTION) — Gate A should NOT stand down; three KB-VIO-110 refinements
1. **Gate A does NOT stand down as a composition false-fire** — the widening is genuine sector-driven, not a DISH artifact.
2. **Sector texture is no longer single-source** (the KB-VIO-110 worry): four independent named institutions carry "AI/software weakest, record dispersion" — **Nuveen** (wk-ending 6/26), **Man Group** (6/16), **Lord Abbett** (6/4), **PGIM** (Feb/Mar). Idiosyncratic/sector channel, not broad deterioration.
3. **Refine the "record CCC−BB dispersion ~8.06":** it is **NOT a record gap** (8.31 printed 2025-04-07; exceeded 8.06 on 3 prior days). The window-record is the **CCC/BB RATIO (6.07× on 6/22)** — partly a *BB-too-tight* (163bp) story, not pure tail blowout. Refine KB-VIO-110 to the ratio.
4. **Premise fix:** the "$2B 7.75% notes" are a **7/1 MATURITY** (out of the index since ~mid-2025 via the ≤1yr rule; to be paid at par from AT&T proceeds), NOT the June coupon. The $183M 6/1 coupon skip was on **three OTHER tranches** and was **cured 6/18**. Index-resident DISH paper = the longer-dated **2027-29 bonds, impaired/distressed under the prepack — do NOT assume near-par.**

### → LIQUID (ACTION) — the X1 composition-discriminator answer + a 7/31 forward flag
1. **X1 discriminator answer:** the CCC widening is an **idiosyncratic AI/software sector channel** (equities→credit, Nasdaq −4% 6/26), **NOT broad-breadth deterioration** — so a >280 trip driven by *this* channel is not the broad deterioration X1 is meant to catch. Any X1 sector-composition overlay must stay **qualitative** (can't be sized: needs exact tech weight × tech-vs-rest spread gap, neither sourced).
2. **X1 tape context (your call on validity):** HY closed **283 on 6/26** and exactly **280 on 6/29** before retracing to 274 — the level printed on the two DISH-stress-peak days, then retraced.
3. **Forward flag (load-bearing):** DISH is still IN the index until the **7/31 rebalance** (6/30 Ch11 filed AFTER the 6/25 lock-out) → **re-pull BAMLH0A3HYC + constituent composition after 7/31 and expect a mechanical CCC *tightening* from DISH removal that is NOT credit improvement.** The −2bp CCC move 6/30→7/1 confirms DISH is still in (no large mechanical tightening yet).

### → RED (INFO) — cluster_mediating counter-read
- **The two-sided read:** Nuveen calls the June widening "**modest**" (heavy primary/new-issue calendar = a competing technical; IG total return stayed positive); the dispersion regime **predates June** (Man Group 6/16); **AllianceBernstein** frames tech-IG repricing as **healthy, not stress**; the big-5 hyperscalers are only **~3.5% of IG debt** (low leverage), so the "record ~10% tech weight" overstates the *distress-relevant* exposure; PGIM finds **senior CLO tranches stable** (stress is equity/mezz). The composition-driven aggregate-OAS blowout is directionally plausible but **unsized**.

### → TERRY (INFO) — timing
- The composition **mechanical delta first prints at the 7/31 rebalance**, not in June. If positioning on credit-recognition, the DISH removal is a July-end event to not misread as "healing" — a naive July-avg-CCC vs August-print comparison would misread the mechanical DISH removal as credit improvement.

### → HENRY (INFO) — AI equity→credit transmission
- The June widening was an **AI-equity selloff transmitting equities→credit** (Nasdaq ~−4% late June on AI-infra cost fears; CNBC 6/25 "chip stocks tumble," Bloomberg 6/23) — ties directly to the AI-capex-bear / mechanical-selling thread (feeds the batch-2 prompt-12 mechanical-selling-stack you'll get next). Sector channel, not broad deterioration.

### → BOND (INFO) — a "record"-claim caveat on ICE BofA series
- **FRED now exposes only a rolling ~3-year window** for ICE BofA OAS series (earliest obs 2023-07-03 on both API and fredgraph) — any "record" claim beyond July 2023 is **NOT verifiable from FRED** and needs ICE direct. Relevant to any rates/credit "record" framing you carry.

---

*Routed by WALTER per CHECKLIST Phase 2.8b (2026-07-02). Originating flag REQ-DEWEY-20260702-001 (Batch-2 prompt 05) — DEEP_RESEARCH_FLAGGED_LOG row closed RESOLVED / executor DEWEY. Handoff `AGENTS/WALTER/inbox/DEWEY/2026-07-02_hy-ccc-widening-decomposition_handoff.md` → `processed/`. Full report: `AGENTS/DEWEY/output/2026-07-02_hy-ccc-widening-decomposition.md`.*
