# FR2004 — SBN2022/SBN2024 bucket comparability probe + the true ceiling

**BOND · 2026-09-14 ~13:0x ET** · WQ-157 leg ② / DOCKET L271 premise work, ahead of the **2026-09-18** deliverable.
**Status: the two OPEN premises are CLOSED. The join itself is UNBUILT.**

## Why this existed as an open question
WQ-157 leg ② (the pairing instrument for the `I'` kill leg) has a stated ceiling of **n=243 weekly prints**, because the long-end buckets exist only from the **2022-01-05** series break (`KB-BND-234`). The open risk: **if the SBN2022 and SBN2024 bucket DEFINITIONS are not comparable, the two breaks cannot be pooled, usable n collapses to 113, and the 2022–23 hiking/SVB stress half is lost** — which is the half that carries the only dealer-stress regime in the sample.

## ① The ceiling is n=244, not 243 — VERIFIED
Direct count at the NY Fed markets API (`/pd/get/{break}/timeseries/{keyid}.json`), 2026-09-14:

| break | window | rows |
|---|---|---:|
| SBN2022 | 2022-01-05 → 2024-06-26 | **130** |
| SBN2024 | 2024-07-03 → **2026-09-02** | **114** |
| | **pooled** | **244** |

The docket's 113 predates the **2026-09-02** as-of, which has since published. Confidence: **VERIFIED** (direct count at the primary).

## ② Comparability — POOLING IS DEFENSIBLE. Confidence: INFERRED, not VERIFIED.

**Method, and why this one.** The clean test is a same-as-of-date comparison across both breaks. **That test is UNAVAILABLE: there are ZERO overlapping as-of dates** (SBN2022 ends 2024-06-26, SBN2024 begins 2024-07-03 — adjacent weekly observations, no overlap). So the test used is a **discontinuity test**: a bucket redefinition would leave the break boundary as an *outlier* against ordinary weekly variation. Each bucket's boundary w/w change is ranked against its own pooled distribution of |w/w| changes across both breaks.

| bucket | boundary w/w (2024-06-26 → 07-03) | rank in |w/w| distribution | median &#124;w/w&#124; | verdict |
|---|---:|---:|---:|---|
| 7-11Y | −8.12% | 43.5th pctile | 9.81% | ordinary |
| **11-21Y** | **+0.04%** | **0.4th pctile** | 4.67% | **quieter than 99.6% of weeks** |
| **>21Y** | **+0.03%** | **0.8th pctile** | 4.50% | **quieter than 99.2% of weeks** |
| long-end total | −2.42% | — | — | ordinary |

**The two buckets WQ-157 actually depends on (11-21Y, >21Y) transition more smoothly than a typical week.** A redefinition producing a level break would rank HIGH; these rank at the very bottom. Keyids are byte-identical across breaks (`PDPOSGSC-G11L21`, `PDPOSGSC-G21`, `PDPOSGSC-G7L11`).

**A suspected artifact, falsified.** At the tool's display precision both buckets appeared *identical* across the break (22.7 → 22.7 and 28.3 → 28.3 $B), which reads like a seeded/carried-forward first row. At raw $M precision they are **not** identical — 22,652 → 22,660 and 28,275 → 28,283, **+$8M each**. The apparent equality was `fr2004_fetch`'s `/1000` rounding. Recorded because in the deliverable this would have looked like a boundary defect.

## ⚠️ Stated limits — the reason this is INFERRED
1. **Zero overlapping dates** ⇒ no direct identity test is possible from the API.
2. **Level continuity is necessary, not sufficient.** A redefinition that preserved levels — same maturity bounds, changed reporting panel or instrument coverage — would pass this test unseen.
3. **NAMED UNCHECKED PRIMARY: the NY Fed's own FR2004 form-revision documentation.** It is the authority on whether the definitions changed; it was not consulted. Per this desk's rule, an absence claim does not upgrade to VERIFIED until the owner-declared source is checked. **`re-test: 2026-09-18`** — check it before the deliverable asserts comparability as established.

## Consequence for the 9/18 deliverable
**Favourable branch: use n=244 pooled, and the 2022–23 stress half is retained** — subject to limit 3 above. The join is still to be built; this closes its premises only.
