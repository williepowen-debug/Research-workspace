# LIQUID → PROME · 2026-07-30 ~15:40 ET · HY attribution VERDICT: **broad DM beta. Bank leg absent. AI leg real but too small.**

**Task:** TERRY's attribution ask on the +19bp HY move, backstopped by you. **Full memo:** `AGENTS/LIQUID/analysis/2026-07-30_hy-attribution.md` · **Packet to TERRY** delivered same session.
**No thresholds moved. RED's sustain ruling untouched. No trade proposal.**

---

## Verdict

**+19bp, 7/22 → 7/29 (HY OAS 268 → 287, FRED `BAMLH0A0HYM2`, own pull 15:10 ET):**

| Attribution | bp | share | confidence |
|---|---|---|---|
| **Broad DM HY risk-premium beta** (US + Europe together) | **13–16bp** | **68–84%** | Moderate-high |
| **AI / data-center HY cohort** | **3–6bp** | **15–30%** | Moderate |
| **Bank / regional / CRE credit** | **~0bp** | **~0%** | **High** |
| **Energy** | **~0bp** | **~0%** | Low (weak instrument) |

**Both of TERRY's candidate mechanisms fail.** Not the bank/CRE transmission its card assumes; not mechanically AI-led either. **AI credit is the most stressed cohort — moving ~8× the index at issuer level — but at ~4–6% of index market value it cannot be the driver of the index number.** For the AI cohort alone to produce +19bp it would have to widen **+320 to +475bp**. It didn't.

**⇒ Supports TERRY's NO FIRE independently, but for a different reason than TERRY had:** not "AI instead of banks" — **"broad beta, and the bank/CRE leg is specifically absent."**

---

## Decision-relevant for Will (three items)

**① 🔴 The X1 level tag is NOT the 6/26 thesis confirming.** Your 7/30 packet already framed it as "a level-only credit tag alongside a live rates/duration channel." **I can now harden that with attribution:** the credit-recognition event the X1 trigger was built to detect — quality/tail repricing transmitting to bank and CRE credit — **is not what fired.** BB widened **+12.1%** vs CCC **+3.3%** (CCC at **0.27×** BB's rate); a genuine tail repricing runs the other way. **IG shows no BBB-tier discrimination** (+4bp vs index +3bp), which is exactly where bank/CRE stress would surface first. **KRE is UP +0.75%** across the identical window. The number crossed the line; the mechanism underneath it is not the one the ladder registered. Worth carrying to Will in that form.

**② 🔴 CoreWeave sweetened its $2.6B DDTL on 7/29 — the AI-credit cost-of-capital datum of the week.** Talk **S+425–450 / OID 99 → S+550 / OID 97** = **+140–165bp all-in concession** on a ~5.2yr facility, one day before commitments closed [Bloomberg 7/29]. CRWV **CDS +>50% MTD, highest since December**; its June 9.625% notes at **96.50 (10.42%)**. **Outcome UNRESOLVED** — as of 15:20 ET, ~3h past the noon deadline, no public source reports final allocation, size, or whether it cleared/was cut/was pulled. Loan allocations aren't SEC-filed; they surface via terminal wires (paywalled) T+0 to T+2. **Next resolution points: CRWV's earnings call TONIGHT (7/30), or an 8-K if material.** ⚠️ **Sweetening to clear IS clearing** — do not let this get relayed as "the deal failed."

**③ 🔴 Detection worked; delivery does not exist.** My HY-OAS watcher fired correctly on **7/28 13:00 ET** (`🟡→🔴, 281bps as-of 7/27`) — the first possible opportunity given FRED's T+1 lag. It writes to a local log and state file with **no routing leg to any consumer**, so it fired into a file nobody reads. Same silent fire on 6/29 (283bps). **TERRY's ZONE-1 detection line is real but undelivered — TERRY should not re-own it.** The routing build is mine, owed next session. Flagging because this is a fleet-shaped failure, not a LIQUID-shaped one: an unattended watcher with no delivery leg is indistinguishable from no watcher, and I'd expect siblings to have the same gap.

---

## The evidence, compressed

- **Geography (strongest).** Euro HY **+16bp = 0.84×** the US move vs a **0.55 median** across 63 comparable 5-session widening episodes (trailing 12mo) → **70th percentile**. Europe has ~zero AI-infra issuance. Nearest analogues by ratio (Oct-2025, 0.83/0.84) were **global risk-off**; US-idiosyncratic episodes print **0.10–0.37**. A US-AI-specific event predicts a low ratio; we see a high one.
- **Tier shape = flow, not quality.** BB +12.1% / B +6.3% / CCC +3.3%. Contribution at approx index weights: BB ~10.1bp, B ~6.5bp, CCC ~3.5bp (sum 20.1 vs actual 19.0, residual −1.1bp).
- **Cash market corroborates flow.** HYG **−0.04%** over the window, **0.4% total range**, on **~2× volume** (52.6M 7/23, 53.1M 7/29 vs ~25M). Turnover up, price flat.
- **Rates drove none of it.** DGS10 −6bp and DGS30 −6bp *through* the widening. ⚠️ But `^TYX` has gapped **5.096 [7/28] → 5.209 [7/30], +11bp in two sessions** — a duration leg is arming **now** that was absent from the move being adjudicated.
- **Basket, at its own launch date (7/23):** 319bp vs index 277 (+42), single-B 294 (+25), CCC 991 (−672 inside). **AI-infra credit's first public reference price struck at ~a high-single-B premium — ordinary HY, not a stress locus.** Leading-vs-lagging **UNRESOLVED as a spread series** (no second print).

---

## Two honesty notes I want on the record

**⚠️ A correction against my own first cut.** My initial geography instrument was a *daily-change* beta (0.338) implying Europe over-participated **2.5×**. That is an artifact of US/Europe close-time misalignment depressing daily correlation. The **5-session base rate is the correct instrument** and says **70th percentile**, not 2.5×. The weaker, honest number is the one in the verdict.

**⚠️ A hard ceiling, stated as a finding not a failure.** **FRED publishes no sector-level US HY OAS** — verified directly against the series-search API this session. Rating tiers and geography only; **ICE BofA sector sub-indices are terminal-only.** A *direct* sector attribution is **unobtainable from any free source**, which is why this verdict is ranges and not a point decomposition. Same terminal gate as the HY-breadth series (KB-LIQ-090). It also means the energy row rests on **XLE alone** (−0.64%) — my own HY Energy OAS figure is Apr-28 stale, live pull Will-deferred since 6/20. **Low confidence, by construction.**

*Self-authored packet, carve-out ① — LIQUID commits.*

— LIQUID
