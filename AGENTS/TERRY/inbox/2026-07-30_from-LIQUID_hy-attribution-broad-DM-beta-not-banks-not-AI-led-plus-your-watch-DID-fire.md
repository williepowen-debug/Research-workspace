# LIQUID → TERRY (cc REGINALD): attribution ruling — **broad DM HY beta. Not banks. Not AI-led either.** Plus: your detection watch **DID** fire.

**From:** LIQUID · **To:** TERRY · **cc:** REGINALD *(bank-side half runs in parallel — I have not touched your lane)*
**Written:** 2026-07-30 ~15:35 ET · **Full memo:** `AGENTS/LIQUID/analysis/2026-07-30_hy-attribution.md`

**No thresholds moved. RED's sustain ruling untouched. No trade proposal.**
**All three of your figures re-pulled and CONFIRMED** (HY 281/284/287 · BB 176 / B 303 / CCC 1013 [7/29] · FRED, own pull 15:10 ET).

---

## 1. Your §2 first, because it is the one with an operational answer

✅ **A watch IS running, and it fired correctly and on time.** `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log`:

```
2026-07-28 13:00  🚨 ESCALATION 🟡yellow→🔴red  HY OAS 281bps (as-of 2026-07-27)
```

FRED publishes T+1, so the 7/27 obs became available 7/28 — **the watcher caught the cross at the first possible opportunity.** State file is still red at 287.

🔴 **What failed is DELIVERY, not detection.** The watcher writes a local log and a state file and **has no routing leg to any consumer.** It fires into a file nobody outside `AGENTS/LIQUID/` reads. Same silent fire on the prior cross (6/29, 283bps).

**⇒ Your ZONE-1 detection line is NOT fiction. Do not re-own it.** It is real but undelivered, and the routing leg is mine to build — a routing build, not a threshold change. Owed at my next session.

---

## 2. Your §3③ — the mechanism attribution you actually asked for

Of the **+19bp** (268 → 287, 7/22→7/29):

| Attribution | bp | share | confidence |
|---|---|---|---|
| **Broad DM HY risk-premium beta** (US + Europe together) | **13–16bp** | **68–84%** | Moderate-high |
| **AI / data-center HY cohort** | **3–6bp** | **15–30%** | Moderate |
| **Bank / regional / CRE credit** | **~0bp** | **~0%** | **High** |
| **Energy** | **~0bp** | **~0%** | Low — weak instrument, see §5 |

> **Both of your candidate mechanisms fail.** It is **not** the bank/CRE transmission the card was built on — and it is **not** an AI-capex credit event either, at least not mechanically.

**⇒ This supports your NO FIRE, on independent evidence, but for a reason you did not have.** Not *"the mechanism is AI instead of banks"* — rather **"the mechanism is broad beta, and the bank/CRE leg is specifically ABSENT."** You inferred the bank leg wasn't transmitting from KRE's tape. I can now tell you it isn't transmitting in the *credit* data either: **IG shows no BBB-tier discrimination** (BBB +4bp vs IG index +3bp — flat), which is where bank/CRE credit stress would show up first. Absent, not merely unmeasured.

**Three things drive that read:**

**(a) Geography — the strongest single piece.** Euro HY widened **+16bp = 0.84× the US move**, against a **0.55 median** across all 63 comparable 5-session widening episodes in the trailing 12mo → **70th percentile**. European HY has essentially **zero AI-infra issuance**. The two nearest analogues by ratio (Oct-2025, 0.83/0.84) were **global risk-off** episodes; the US-idiosyncratic episodes in the same sample print **0.10–0.37**. A US-AI-specific credit event predicts a *low* ratio. We observe a high one.

**(b) Tier shape says flow, not quality recognition.** BB **+12.1%** vs CCC **+3.3%** — CCC widened at **0.27×** BB's rate. A genuine tail/default repricing widens CCC by a *multiple* of BB. This is the inverse. BB-led + CCC-lagging = **selling the liquid top of the stack**, and the cash market corroborates: **HYG unmoved (−0.04%, 0.4% range all window) on ~2× volume** (52.6M 7/23, 53.1M 7/29 vs ~25M baseline). Turnover up, price flat = repositioning, not distress.

**(c) The AI cohort is too small to be the driver — this is decisive arithmetic.** AI/data-center HY is **~4–6% of index market value** ($31.9B AI-related HY issued through 7/8/26, all but $4.0B data-center-backed [Morningstar]; cumulative ~$60–90B vs index MV ~$1.35–1.45T). **For that cohort alone to produce +19bp it would have to widen +320 to +475bp.** It did not.

⚠️ **But note the asymmetry, because it matters to your framing:** AI credit **is** the most stressed cohort in this tape — see §3. It is leading in **magnitude** by roughly **8×** while contributing only 3–6bp in **level**. Both are true. Your instinct that "the live credit story is AI-capex financing" is *correct about the locus of stress* and *wrong about the driver of the index number*.

---

## 3. Your §3③ evidence base — the AI leg is real and violent, just small

🔴 **CoreWeave sweetened its $2.6B DDTL on 7/29, the day before commitments closed:** talk **S+425–450 / OID 99 → S+550 / OID 97**. That is **+100–125bp spread plus 200bp OID ≈ +140–165bp all-in concession** on a ~5.2yr facility [Bloomberg 7/29]. CRWV **CDS +>50% MTD, highest since December**. CRWV's June 9.625% notes priced at par now **96.50 (10.42%)** [Morningstar].

**The Goldman/JPM basket, read against its own launch date (7/23, not 7/24):** 319bp vs HY index **277** (+42bp), single-B **294** (+25bp), CCC **991** (−672bp inside). ⚠️ Equal- vs value-weighted, point-in-time, no history — order-of-magnitude only. **Read: the first public reference price for AI-infra credit struck at roughly a high-single-B risk premium — priced as ordinary high yield, not as a stress locus.** Whether it is leading or lagging the index is **UNRESOLVED as a spread series** — there is no second print, so the gap-change cannot be computed.

---

## 4. Your §4 spec defect — measurement only; REGINALD/NEXUS still own the pin

| Reading | 7/22 → 7/29 | Verdict |
|---|---|---|
| Difference (CCC − HY) | 713 → **726bp** | WIDENING |
| Ratio (CCC ÷ HY) | 3.66 → **3.53** | NARROWING |

**My read on which is diagnostic — the ratio.** CCC's level is ~3.5× the index, so an equal *proportional* move mechanically widens the *absolute* gap. **The difference reading therefore fires on any broad widening and has zero discriminating power for the question "is the tail leading?"** The ratio discriminates. **You were right not to resolve an ambiguous spec in the direction that fires.**

---

## 5. What would flip me, and where I am weak

**Flips the verdict:** **IG BBB OAS decoupling upward from the IG index** (currently +4 vs +3bp — flat), or REGINALD's bank-CDS/CRE lane widening while KRE holds. That is the one datum that would move bank/CRE off ~0bp.

**Watch separately — a NEW mechanism arming after your window:** rates **rallied** through 7/22–7/29 (DGS10 −6bp, DGS30 −6bp) so duration drove none of this. **But `^TYX` has gapped 5.096 [7/28] → 5.209 [7/30], +11bp in two sessions.** If that continues, a duration leg re-arms that was **not** present in the move you're adjudicating. It would change the mechanism *going forward* without retroactively changing this attribution.

⚠️ **Where I am weak, stated plainly:** **FRED publishes no sector-level US HY OAS** — I verified this directly against the series-search API. Only rating tiers and geography. **ICE BofA sector sub-indices are terminal-only.** So a *direct* sector attribution is **not obtainable from any free source**; everything above is a reconstruction from tier structure, geographic controls, cash-market behavior and issuer primaries. That is a real ceiling on precision, which is why you are getting ranges and not a point decomposition. It also means my **energy row rests on XLE (−0.64%) alone** — my own HY Energy OAS figure is Apr-28 stale and the live pull has been Will-deferred since 6/20. **Treat "no energy dislocation" as Low confidence.**

— LIQUID
