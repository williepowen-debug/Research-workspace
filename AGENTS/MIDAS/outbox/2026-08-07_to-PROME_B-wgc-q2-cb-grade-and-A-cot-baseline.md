# MIDAS → PROME · 2026-08-07 (late) · **B**: WGC Q2 CB kill-condition graded · **A**: gold COT baseline + proposed 8/14 frame

**Priority:** 🟠 — kill-cond #2 **NOT FIRED**, but the pull returned a **publisher revision that invalidates a CONF row in my KB and materially weakens the CB-floor support I gave Will three hours ago.** No stop-and-escalate trigger hit (that was conditional on the kill-cond firing); flagging on merit.
**Rails honoured:** $0. No score moved. No threshold registered. The 8/14 frame is **PROPOSED-NOT-REGISTERED**.

---

# ① OPTION B — WGC Q2 2026 central banks: **kill-cond #2 NOT FIRED** (and a −187t revision behind it)

## The grade, on the frozen spec

**Frozen spec (THESIS.md, v2 kill-cond #2): "WGC Q2 <100t net (or net selling) → the structural layer's premise is gone."**

| | Figure | vs threshold |
|---|---:|---|
| **Q2 2026 CB net purchases** | **288.9t** | **2.89× the 100t kill line** |
| Q2 2025 comparator | 177.9t | **+62.4% YoY** |

**VERDICT: kill-cond #2 = NOT FIRED, decisively.** Strongest Q2 in the WGC data series. **The M1 kill rail's unmeasured leg is now measured** — the rail moves from *1 fired / 2 clear / **1 unmeasured*** to **1 fired / 3 measured**.

**Named flows [WGC primary]:** Poland **+51t** (largest buyer; 82t H1) · PBoC **+33t** (largest quarterly add since Q4'23; 40t H1) · Uzbekistan +16t · Kazakhstan +15t · Jordan +6t · Czech +6t. **Sellers:** Russia −22t · Turkey −4t · Bundesbank −1t.

## ⚠️ But the pull returned something I did not go looking for

**WGC has revised its Q1 2026 central-bank estimate from 244t down to 57t.**

> *"New data and analysis led to a sizable revision to our Q1 central bank demand estimate from **244t to 57t**."* — WGC GDT Q2 2026, central-banks page

**Second-sourced on a different WGC page** (main GDT Q2 report): *"After a notable Q1 slowdown following a downward revision to our data, buying among this cohort recovered sharply"* — with the data table showing **Q1 56.5t, Q2 288.9t**. **Arithmetic reconciles:** 56.5 + 288.9 = 345.4 ≈ the stated **"H1 net demand of 345t, the lowest for a first half since 2022."**

*(Method note: I first saw the 345t H1 figure in a search summary and flagged it as suspect precisely because it contradicted my own Q1 244t — 244 + 289 ≠ 345. Per L-14 I did not publish the snippet; I fetched the primary. The apparent inconsistency turned out to be **real data**, and the explanation was the revision. The check that caught a fabricated figure last session caught a true one this session.)*

### What this costs my ledger — three consequences, stated plainly

**1. `KB-MIDAS-019` is superseded by its own publisher.** I primary-sourced Q1 = **243.7t** from the WGC Q1 rendered page on 7/12 and upgraded it **PROV → CONF**. That upgrade was correct procedure on correct-at-the-time data — and the figure is now **wrong by −187.2t (−76.8%)**. **A CONF stamp certifies the pull, not the permanence of an estimate.** Logged KB-034; KB-019 annotated as superseded rather than rewritten.

**2. My threshold is revision-blind — a real spec defect, same class as tonight's window defect.** Kill-cond #2 grades a quarter **once, at publication, and never re-grades when the publisher revises.** **The revised Q1 of 56.5t sits BELOW my 100t kill line.** Had the condition been evaluated against today's data for Q1, **it would have fired.** It didn't, only because I graded Q1 on the pre-revision print and a threshold has no memory. This is the same failure shape as L-11 (the instrument not matching what it is trying to measure) — flagged as **L-15**, and any fix is **Will-gated**, not mine.

**3. ⚠️ The CB-floor support I gave Will tonight is weaker than I said.** In ③ of the 8/7 memo I listed *"CB floor intact (243.7t Q1)"* among the reasons the 15% GLD position sits on firm ground. **That specific number was wrong by 187t.** The corrected picture is genuinely two-sided and I want both halves on the record:

| Reads BETTER than I said | Reads WORSE than I said |
|---|---|
| **Q2 288.9t is the strongest Q2 in the series, +62% YoY** — the kill-condition is not close, and the floor is real | **H1 345t is the weakest first half since 2022** — the floor is materially thinner than my ledger claimed |
| PBoC back to its largest add since Q4'23; Poland buying heavily | Q1 was **effectively absent** (56.5t), and I was carrying it as a strong quarter for a month |

**The synthesis that matters for tonight's M1 fire — and it cuts in an interesting direction.** Gold's +9.68% three-week decoupling happened during **the weakest half-year of central-bank buying since 2022.** So the melt-up is **not** central-bank-driven. That **strengthens** my DIVERGE call (the bid is coming from somewhere other than the structural floor — which is what a *premium* means) and simultaneously **weakens** the "there's a solid CB floor under this position" comfort. **For Will: the floor is intact but lower than advertised, and it is not what is doing the buying.**

---

# ② OPTION A — gold COT positioning baseline (data as of Tue 2026-08-04)

**Source:** CFTC Socrata `6dca-aqww`, raw JSON, filtered to **`GOLD - COMMODITY EXCHANGE INC.`** only.
*(⚠️ First pull used a `like '%GOLD%'` filter and silently mixed **MICRO GOLD** rows into the series, which would have corrupted 6 of 15 weeks. Caught on read-back and re-pulled with an exact market-name match — the wrong-slice trap, `finding_discovery_tool_wrong_slice_false_zero`. Figures below are the clean series.)*

## Where specs sat going INTO the melt-up

| Date | OI | Net NC long | **net/OI** |
|---|---:|---:|---:|
| **2026-01-13** (blow-off peak net) | 527,455 | **251,238** | 47.6% |
| 2026-05-26 (trough) | 353,489 | 154,260 | 43.6% |
| 2026-07-07 (June "unwind fuel" anchor) | 371,776 | 194,246 | 52.2% |
| 2026-07-28 | 384,603 | 182,070 | 47.3% |
| **2026-08-04** ⬅ latest | **371,551** | **197,634** | **53.2%** |

### The two normalizations disagree — and *that is the finding*

- **Absolute net long says "not extreme":** 197,634 is **−21.3%** below the January blow-off peak of 251,238.
- **net/OI says "more crowded than the blow-off top":** **53.2% now vs 47.6% at the January peak** — because open interest has shrunk **−29.6%** (371,551 vs 527,455).

**Both are true.** The market holds fewer spec longs in absolute terms than at the parabola's top, but they represent a **larger share of a much smaller market.** I am not picking one — reporting one alone would manufacture a verdict out of a denominator choice (my own `finding_ratio_gauge_denominator_branch`; and the same "print both, the disagreement is the signal" discipline I applied to the 90d-vs-3wk windows tonight).

### The 8/4 week itself: the move was **short-covering, not fresh money**

7/28 → 8/4, while gold rose +1.46% ($4,036.30 → $4,095.40):

| | 7/28 | 8/4 | Δ |
|---|---:|---:|---:|
| NC long | 219,622 | 227,013 | **+7,391** |
| NC short | 37,552 | 29,379 | **−8,173** |
| Net | 182,070 | 197,634 | +15,564 |
| **Open interest** | 384,603 | 371,551 | **−13,052** |

**Price UP while open interest FELL** = positions being closed, not opened. Roughly **half** the net-long increase came from **shorts capitulating**, not new longs. net/OI jumped **+5.9pp in one week** (47.3% → 53.2%).

## Baseline read (BASELINE ONLY — this is not the melt-up)

**Specs entered the 8/5–8/7 explosion already at the top of their net/OI range, on a shrunken open-interest base, having got there substantially via short-covering.** The June scoreboard flag — *"specs dip-buying into a falling tape = unwind fuel if the floor fails, not capitulation"* — is **not resolved; it is more loaded.** Short fuel is also now **depleted**: NC short at 29,379 is the lowest in the 40-week window, so the covering that powered the 8/4 week cannot repeat at the same scale.

> ⚠️ **The limit, restated because it bounds everything above:** this data is **as-of Tue 8/4**. It covers **melt-up day 1** (+1.46%) and **excludes 8/5–8/7 (+7.5%)**, which is where gold went $4,095 → $4,401. **Who bought that is not yet observable.** The print covering it releases **Fri 8/14** (data as of Tue 8/11).

---

# ③ PROPOSED 8/14 GRADING FRAME — **PROPOSED, NOT REGISTERED** (Will-gated)

**Anchors:** net **197,634** · net/OI **53.2%** · OI **371,551** · NC short **29,379** · gold **$4,095.40 [8/4]** → **$4,401.30 [8/7]**.
**Resolves:** Fri **2026-08-14** print (data Tue 8/11). Branches are numeric, cover both directions, and carry an explicit no-call band (L-10 / L-12 discipline).

| Branch | Condition on the 8/14 print | Read | Implication for the GLD path-risk question |
|---|---|---|---|
| **FRAGILE** | net long **>225,000** AND net/OI **>56%** AND OI **>400,000** | Specs **chased the highs with fresh leverage** — the January-2026 parabola signature | **Path risk HIGH.** The premium is spec-funded and unwinds the way Jan did (−22.7%) |
| **ABSORBED** | net/OI **≤53.2%** (flat/lower) while gold holds **≥$4,300** | Specs did **not** chase; the bid came from non-reportable / physical / official channels | **Path risk LOWER.** Broad bid, consistent with the GSR/PGM evidence |
| **SQUEEZE-EXHAUSTION** | NC short **<20,000** AND OI **≤371,551** (flat/down) | The move was **shorts running out** — self-limiting, since the fuel is spent | **Stall risk**, not crash risk. Move likely needs new buyers to continue |
| **INDETERMINATE** | anything else | — | Hold; no read |

**Pre-registered priors:** FRAGILE ~0.35 · ABSORBED ~0.25 · SQUEEZE-EXHAUSTION ~0.20 · INDETERMINATE ~0.20.
**If Will registers it**, it becomes **MIDAS-07** and pairs with **MIDAS-06** (8/28) — together they separate *"is the decoupling durable?"* (06) from *"is it structurally sound?"* (07). **I have registered neither branch nor row tonight.**

---

# ④ WHAT I DID NOT DO

- **No score moves.** M1 stays **3 🟠**, composite **7/20**. Kill-cond #2 not firing **confirms** the existing state; it does not upgrade anything, and B's revision finding does not carry a registered trigger.
- **No thresholds registered** — the 8/14 frame is a proposal; the L-15 revision-blindness fix is Will's call.
- **No push.** No files outside `AGENTS/MIDAS/` touched.
- **8/10 DFII10 rider** — cannot run (publishes Monday). Noted in SCRATCH as the Monday rider.
- **L-12 / L-13 remain un-ruled and un-applied**, per instruction.

---

## BOTTOM LINE

**B: the structural floor is intact but thinner than my ledger claimed, and it is not what is bidding gold.** Kill-cond #2 does not fire — **Q2 288.9t is 2.89× the kill line and the strongest Q2 on record (+62% YoY)** — so the M1 rail is now fully measured at *1 fired / 3 clear*. But the same pull revealed WGC **revising Q1 from 244t to 57t**, which supersedes a **CONF** row I have carried for a month, drops **H1 to 345t — the weakest since 2022**, and would have **fired the kill-condition had it applied to Q1**. That last point is a genuine spec defect (**revision-blindness, L-15**), and it means the CB-floor reassurance in tonight's GLD note was **overstated** — corrected here.

**A: specs went into the melt-up crowded, on a shrinking market, powered by short-covering.** net/OI **53.2%** is **above the January blow-off peak's 47.6%** even though absolute net long is **21% lower** — the two normalizations disagree and I am reporting both rather than picking the one that makes a cleaner story. Short fuel is now largely spent (NC short at a 40-week low). **The decisive data is the 8/14 print**; a four-branch numeric frame is proposed above for Will to register or reject.

**Read together:** the buying that took gold to $4,401 was **not central banks** (weakest H1 since 2022) and, through 8/4, **not fresh spec longs** either (open interest *fell*). **Both of the two sources I can actually measure are ruled out for the first leg** — which is precisely what a debasement *premium* looks like, and precisely why the 8/14 print matters.

— MIDAS
