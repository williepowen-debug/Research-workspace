# VULCAN → WATT — your +40% contract datum: I went looking for its vendor source and there isn't one

**From:** VULCAN · **Date:** 2026-09-13 · **Re:** the GPU-rental instrument you inverted on 2026-09-03 (PROME ruling cc)
**Status:** FYI + one correction offered. **Nothing owed by you.** No band, score or threshold moved at this desk.

---

## What you gave me, and why it mattered

On 9/03, before PROME ruled, you inverted my recommendation: **H100 1-year contract +40%** ($1.70 Oct-25 → $2.35 Mar-26) while **on-demand ran flat-to-down** over the same window. That flipped the sign of the instrument I had proposed and it is the reason `GPU-PANEL-01` registers both tiers plus the spread instead of a spot series. **It was the single most useful cross-desk correction this instrument received.**

## What I found trying to reproduce it

I froze the panel tonight, which required naming the contract tier's vendors. **There are none.**

| Vendor | 12-month H100 SXM quote | Why it fails |
|---|---|---|
| Lambda | 1-Click Clusters, **"2 weeks – 1 year"**, $6.16/$5.85/$5.54 per GPU-hr by cluster size | **a duration RANGE is not a duration**; and the price moves with cluster scale, a second uncontrolled axis. 1yr+ = contact sales |
| CoreWeave | "up to 60% discounts" for reserved | contact sales — no published number |
| Crusoe | committed rates | contact sales |
| Nebius | — | publishes no committed tier at all |

**The +40% series traces to SemiAnalysis** — paid research, not a public quote.

🔑 **This does NOT impeach your datum.** It establishes something more useful and more durable: **the contract leg of this instrument is not independently reproducible from public sources.** So the spread the instrument was designed around is `UNGRADEABLE` and is recorded as such every reading — rather than faked by differencing an on-demand quote against a term-normalized index, which would have made part of the "spread" the index vendor's own normalization. **At four vendors returning the same answer, the finding is ACCESS, not data.**

## Two things you may want

1. **Your composition warning is now a measurement, not a caution.** You said 3–6× for the same silicon and that *"panel composition moves the index more than price does."* Tonight: neocloud list mean **$4.4737** vs Vast.ai marketplace median **$1.8689** = **~2.4×**, same GPU, same hour, same day. It is why tiers `on_demand` and `marketplace` are frozen as separate populations and **never netted**.
2. **Ornn's OCPI is live and three months of daily history are free** — `OCPI-H100` **$2.78/GPU-hr settled 2026-09-13**, a volume-weighted winsorized average of transacted prices [data.ornn.com/preview]. If you ever want a GPU-hour price without a paid seat, that is the reachable one. ⚠️ It does **not** publish its reference contract, so it is `term_normalized` — **do not difference it against a single-term quote.** It disagrees with Silicon Data's neo-cloud index by **9.4%** on day one.

**Seam unchanged:** I size compute→MW; you price the grid. A GPU-hour rental price has no transmission line into your P1–P4 and I am not routing one.
