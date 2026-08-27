# ORACLE — TRADE (how prediction-market odds inform positions)

**Refreshed:** 2026-08-27T18:38Z (live pull, both platforms) · **prior refreshes:** 8/12, 7/22
**Structural change this refresh (Will-directed, 2026-08-27):** *"lets not simply delete though — lets track how the numbers have changed over time."* **Every routed figure now carries its own trajectory** instead of a single point-in-time value.

> ### Why the trajectory, and not just a fresher number
> This file is a **routing surface** — other desks key positions off its figures — and it has now rotted the same way twice. DAEDALUS caught it at **21 days** (7/22 figures live on 8/11); the Will-directed sweep caught it again at **15 days**, with Hormuz-normal **14.0pp** stale and best-asset-S&P **14.5pp** stale. **A refresh alone only resets the clock on the next rot.**
> With the history in the row, **a stale row announces itself**: a reader seeing a trailing date knows the figure is old without checking a header. Rot that is visible is a different failure mode from rot that hides.
>
> **Provenance:** every figure below is machine-extracted from ORACLE's own append-only logs (`workbook/ODDS_LOG.tsv`, `workbook/KALSHI_ODDS_LOG.tsv`) by `tools/trade_marks.py`, which writes `workbook/TRADE_MARKS.tsv` (190 rows, 14 marks). **No vintage is hand-typed** — regenerate with `python3 tools/trade_marks.py --write`, and every cell is reproducible from a log row by date + slug.
>
> ⚠️ **CONTRACT IDENTITY — read this before differencing anything.** A trajectory across two *different* contracts is not a trajectory. The tool **segments** a series whenever the slug changes and **refuses to difference across the break**, marked ‖ below. Two live cases on this board: **bank-failure-by-Dec-31 has had three slugs** (delist/relist), so its 69.5→55.5 "fade" **is not a move**; **WTI-$100 is month-stamped**, so Jun/Jul/Aug/Sep are four separate contracts and a fresh month is structurally higher on days-to-touch alone.
>
> ⚠️ **THE COLUMNS ARE A SUBSET, AND THE `range` COLUMN EXISTS BECAUSE OF IT.** ORACLE pulled on **17 dates** since 6/19; these tables show **six**. A subset can hide an excursion and make a series look cleaner than it was — checked mechanically, and it does: the displayed Hormuz columns omit an **8/02 spike to 58.5**, above every value shown. **So every table carries a `range (7/22–8/27)` column taken from ALL pulls in the window, not just the displayed ones.** If a level sits outside the columns you can see, the range column is where it shows up. Full per-date series: `workbook/TRADE_MARKS.tsv`.
>
> ⚠️ **Still a DATED SNAPSHOT, not a live feed. `STATUS.md` is the live home** — re-pull before citing.

---

## Live reads → position implications

### 1. Fed path → KRE / OZK / WAL shorts

| Mark | 7/22 | 7/31 | 8/09 | 8/12 | 8/18 | **8/27** | range (7/22–8/27) | Read |
|---|---|---|---|---|---|---|---|---|
| Fed **no-cuts** 2026 | 84.8 | 89.3 | 85.8 | 85.6 | 85.2 | **87.9** | 84.7–89.3 | range-bound in a ~4.6pp band, net **+3.1** — the higher-for-longer leg is **intact**, never threatened |
| Fed **hike-2026** (aggregate) | 64.5 | 66.5 | 54.5 | 54.5 | **48.5** | **57.5** | **48.5–71.5** | peak-to-trough **−23.0pp** (71.5 on 7/24 → 48.5 on 8/18), then **+9.0** back |
| Fed hike **Sept-specific** (PM) | — | 56.5 | 35.5 | 33.5 | 28.5 | **30.5** | 28.5–56.5 | −28.0pp 7/31→8/18, now edging back up |
| Fed hike **Sept** (Kalshi, T6 canonical) | — | — | — | — | 30.0 | **32.0** | 30.0–32.0 | 1.5pp from PM on **both logged pairs** — caveat below |

**Implication: STILL SUPPORTIVE, AND THE TROUGH IS IN — RE-KEY, DO NOT INVERT.** The mechanism that matters for CRE-refi/NIM is *higher-for-longer*, and no-cuts has not broken all month (84.8→87.9). What de-rated was **conviction in a hike**, and even that has turned: the aggregate bottomed at **48.5% on 8/18** and is back to 57.5%.
⚠️ **Two corrections carried on the record, both found by re-reading this file rather than by any check:**
- **The trough.** The 8/12 refresh called 54.5% the trough. It was not — the series fell on to **48.5% (8/18)**, my own last pull before a 9-day dark window. A point-in-time refresh would have re-published the wrong trough.
- **The size of the de-rating.** This row first read *“fell 16pp”* — measured from the 7/22 column (64.5). But **7/22 was not the peak: the window’s high is 71.5 on 7/24**, a date these columns do not show. Peak-to-trough is **−23.0pp, not −16.0**. Measuring a move from a window edge instead of its extremum understates it — which is exactly why the `range` column now exists. *(That 71.5 is the same figure NEXUS and RED carried stale — KB-ORC-068.)*

**A hike remains modal on both platforms.**
⚠️ **Cross-platform caveat on the Kalshi row:** the 1.5pp PM↔Kalshi gap holds on **both logged pairs** (8/18 30.0 vs 28.5; 8/27 32.0 vs 30.5). A third pair at the same gap exists for **8/12 (35.0 vs 33.5)** but came from an **ad-hoc fetch before this contract was pinned**, so it is not in the logged series and shows as `—` above. Cite it as **two logged + one ad-hoc (KB-ORC-068)** — never as “three consecutive pins.”

### 2. Iran / Hormuz / oil → BRENT / HAWK / FALCON

| Mark | 7/22 | 7/31 | 8/09 | 8/12 | 8/18 | **8/27** | range (7/22–8/27) | Read |
|---|---|---|---|---|---|---|---|---|
| **Hormuz normal** by Dec 31 | 51.5 | 50.5 | 49.5 | 46.5 | 36.5 | **32.5** | **32.5–58.5** | **−19.0pp end-to-end, one contract** — but ⚠️ **NOT monotonic**, see below |
| **US invade Iran** before 2027 | 28.5 | 23.5 | 16.5 | 18.5 | 17.5 | **12.5** | 12.5–29.5 | −16.0pp — the *invasion* tail is being priced out |
| **WTI $100** war premium | 15.7 *(Jul)* | 27.5 *(Aug)* | 10.5 | 12.5 | 9.5 | **22.5** *(Sep)* | ‖ *n/a across rolls* | ‖**TWO ROLLS** — do NOT read 9.5→22.5 as repricing |

**Implication: PREMIUM, NOT SHORTAGE — and the reopening keeps being priced OUT.** Disruption−supply spread **+45.0pp** `[v4-sep-wti-supply-leg]`.
⚠️ **Carry all of these — this block has the most ways to be misread:**
- **The WTI row rolled twice** (Jul→Aug→Sep). The 8/18 9.5% was an August contract with 13 days left; the 8/27 22.5% is a September contract with a full month. **The 13pp step is calendar, not risk.** The spread's own regime was bumped v3→v4 for this reason — **never chart across it.**
- **The new Sept supply leg is THIN at inception** ($1.2K vol vs the August leg's $706.5K) — single-print-unreliable, flagged not marked.
- **Horizon disclosure:** the disruption leg reads off the *Dec-31* contract. The near-dated legs are far more severe — **normalization by Sep-15 is 1.4%**, by Aug-31 **0.4% on $16.6M**. This row understates near-term severity by construction.
- ⛔ **CORRECTED IN REVIEW — this row first called the Hormuz decline “near-monotonic… the cleanest trend on the board.” It is not monotonic.** The displayed columns fall 51.5→32.5 without a single up-tick, but they **skip 8/02, which printed 58.5 — above every value shown and 7.0pp above the 7/22 starting level.** The real path is *up first, then down hard*; the clean staircase was an artifact of which six dates I chose to display. **The end-to-end −19.0pp is real; the shape word was not.** Every table now carries a range column so this class of over-claim is visible rather than inferable.
- ⚠️ **A range cannot be quoted across the WTI rolls at all** — the `n/a` above is deliberate, not missing data. Per segment: Jul 1.6–23.8 · Aug 9.5–27.5 · Sep 22.5 (one print).

### 3. Recession → whole bear book

| Mark | 7/22 | 7/31 | 8/09 | 8/12 | 8/18 | **8/27** | range (7/22–8/27) |
|---|---|---|---|---|---|---|---|
| Recession 2026 (PM) | 12.0 | 12.5 | 7.5 | 8.5 | 7.5 | **8.5** | 7.5–12.5 |
| Recession 2026 (Kalshi NBER) | 13.0 | 7.0 | 6.0 | 10.0 | 6.0 | **7.0** | **6.0–14.0** |

**Implication: crowd calm, and calmer than in July** — both platforms roughly halved off their 7/22 levels and have gone flat. If the crowd is right, equity-stress positions are early/oversized.
⚠️ **A caveat the old single-point row hid:** TRADE.md has called these *"converged, ~1.5pp cross-platform."* The trajectory shows **Kalshi is the noisy leg** — 13.0 → 7.0 → 10.0 → 6.0 → 7.0, swinging 4pp between pulls on a contract with no resting book (depth = OI). **The convergence is real on average and unstable print-to-print.** Do not treat a single-day cross-platform gap as signal. **RED still owed a current fleet recession number — carried since 6/13.**

### 4. Bank failure → REGINALD / WAL / OZK

| Mark | 7/22 | 7/31 | 8/09 | 8/12 | 8/18 | **8/27** | range (7/22–8/27) |
|---|---|---|---|---|---|---|---|
| **ANY** US bank failure by Dec 31 | 72.5 | 72.5 | 69.5 | 69.5 | 69.5 | ‖ **55.5** ⚠️thin | ‖ old slug 69.5–74.0 · new 55.5 |
| **Named**-bank EOY (top leg) | 3.7 | 3.8 | 3.7 | 3.6 | 3.5 | **3.9** | **3.1–4.2** |

**Implication: unchanged in substance — no name is priced.** The named-bank leg has sat in a **3.1–4.2% band for five weeks**, which is the number that would actually matter. **No trend — roughly ±0.5pp of noise around ~3.7.** Both band edges (4.2 on 7/24, 3.1 on 8/11) fall on dates these columns do not show, which is what the range column is for.
⛔ **DO NOT read 69.5 → 55.5 as a 14pp fade.** That is a **delist/relist identity break** — the third for this contract family (7/2, 7/22, 8/24). Different contract instance, and the new one is **thinner** ($1.3K vs $3.1K). Not comparable, not charted, no divergence filed. The ANY-bank gauge is broad-scope anyway (small-bank failures are common), which is why it reads ~70% while the named leg reads ~4%: **different questions, not a contradiction.**

### 5. Tail sentiment → VIOLET vol / tail hedges

| Mark | 7/22 | 7/31 | 8/09 | 8/12 | 8/18 | **8/27** | range (7/22–8/27) |
|---|---|---|---|---|---|---|---|
| **Nothing Ever Happens** 2026 | 66.5 | 73.5 | 80.5 | 79.5 | 81.5 | **85.0** | 65.5–85.0 |
| Best asset 2026 — **S&P leg** | 67.0 | 68.0 | 68.5 | 68.0 | 68.5 | **53.5** | 53.5–68.5 |
| *(same event, other legs — 8/27 only)* | | | | | | **Gold 30.5** (Δ7d +7.0) · **BTC 17.5** (+1.5) | — |

**Implication: 🔴 THESE TWO JUST DECOUPLED, AND THAT IS THE FINDING OF THIS REFRESH.** For five weeks they moved together as one complacency story. Then, in the **nine days since my last pull**, **NEH made a new series high (+3.5 — prior max 84.0 on 7/02, so a round-trip *through* its July peak, not a virgin breakout) while the S&P leg fell −15.0pp** — flat 66.5–68.5 for a *month*, then a break. *(Platform's own trailing Δ7d on the S&P leg is −8.5; the −15.0 is measured from ORACLE's 8/18 pin. Both are stated because they answer different questions.)*
**I pulled the full 3-way ladder rather than reading the one leg, and it changes the read: this is a rotation INTO GOLD specifically** (+7.0 of the S&P's loss), not a broad flight — Bitcoin barely moved (+1.5).
**Read: the crowd still believes nothing breaks, but has stopped believing equities lead.** That is complacency **narrowing and rotating**, not complacency ending — a more fragile state than either number shows alone.
⚠️ **The registered contrarian tell has NOT fired.** VX-ORC-09 watches *"NEH <30% OR gold retakes the best-asset lead"* — **NEH went the opposite way (85.0), and gold at 30.5 has not overtaken the S&P at 53.5.** State raised 🟠→🔴 on **move size**, not on a trigger firing. Do not report this as a fired tell.
**It happened entirely inside my 8/19–8/26 dark window and nothing flagged it** — it surfaced only because this refresh rebuilt the trajectory. → VIOLET, RED
*(Historical note kept, not deleted: the 7/22 row read "complacency crack deepened" at NEH 66.5%. It did not crack — NEH round-tripped to a new high. Anyone who carried that 7/22 read had the sign backwards for three weeks, which is what motivated this file's rebuild.)*

### 6. Blind-spot axis → BOND

| Mark | 7/22 | 7/31 | 8/09 | 8/12 | 8/18 | **8/27** | range (7/22–8/27) |
|---|---|---|---|---|---|---|---|
| US credit-rating downgrade 2026 (Kalshi) | 4.0 | 6.0 | 14.0 | 14.0 | 13.0 | **12.0** | 4.0–14.0 |

**Implication: ⚠️ this axis TRIPLED while the policy board de-rated, and has only partly eased.** ORACLE's instruments price the **policy path only** — they cannot see term premium or credibility. ⛔ **Never read this file as "rates calm per ORACLE."** **BOND owns the regime label.**

---

## Standing rule for downstream agents

When ORACLE hands you a market probability:
1. **Is your trigger outcome already priced?** If yes, re-key your prediction to *"more X than priced"* (anchor-to-surprise).
2. **Is the market thin (⚠️)?** Treat any move as unconfirmed until a ≥3-day re-check **plus** an independent source agrees. Thin books discharge by **DEPTH, never by elapsed time** (N5 clause iv).
3. **Divergence ≠ direction.** A gap vs thesis is a question for RED, not a position change.
4. **★ Check the row's trajectory before you cite its level.** A number that has been flat for five weeks and a number that moved 15pp last week are not the same evidence, even at the same value.
5. **★ Never difference across a ‖ break.** Rolls and relists are identity changes, not moves.

*No position is opened or sized from this file. Owners: FORGE / the named domain agent.*
