# LIQUID — Active Branch Points (Forward Decision Windows)

**Last Updated:** 2026-06-13 (FOMC/TIC pre-stage mirrored into rows 13/15/16; JPY+Brent freshness; worktable at `workbook/FOMC_TIC_DECISIONTREE.md`, DELETE-BY 6/19)

> **Purpose:** Forward-looking bull-vs-bear resolution tree at the decision windows that matter for the LIQUID thesis. Resolved events live in `STATUS.md` (Durable Signals Log). When a window resolves here, retire the row and append the resolution to STATUS's log.

---

## Active Branch Points (Jun 12 → late Jul)

| Window | Question | Bull Resolution (thesis weakens) | Bear Resolution (thesis confirms) | Channels affected |
|---|---|---|---|---|
| **Wed 6/17 — June FOMC (decision day)** | Does FOMC resolve the 5.00-pivot oscillation — and does liquidity-facility language move? *(Pre-stage 6/13: weights Hold ≈93%; dot-flavor hawkish 33 / neutral 38 / dovish 22; cut 5; facility tail 2. Pivot axis = hot-CPI-behind vs **oil-relief-ahead**, not just hot→hawkish. Worktable: `workbook/FOMC_TIC_DECISIONTREE.md`)* | Dovish dots / cuts signaled despite hot May CPI → 30Y breaks lower toward the <4.90 sustained unwind test. **Second dimension:** explicit liquidity-facility language (SRF reform, standing-repo broadening) = **Leg A kill candidate (THESIS §7)** — tail-watch, no funding stress visible | Hawkish dots → Fed-constraint repriced, 30Y re-engages >5.00; no facility language = Leg A persists. **FOMC ARMS, the 30Y close-sequence RESOLVES** (one-day spike ≠ regime); conviction moves scope to the duration LEG only | Duration (Leg B) / **Leg A** / resolves conviction 60 |
| **Rolling, FOMC-coupled** | **30Y downside branch:** which side of the 5.00-pivot oscillation resolves? *(Successor to "30Y >5% durability" — bear test fired 5/12–5/27, durability then failed; KB-LIQ-059)* | **30Y <4.90 sustained** = pre-registered duration unwind fires. Cross-refs (distinct rules, kept distinct): THESIS §7 full thesis reassessment requires **10Y <4.30 sustained AND HY <270**; separately (STRATEGY 6/12 amendment), a **credit kill** (<260 ladder) firing while 30Y is sub-5.00 routes to full reassessment | **≥5 consecutive closes >5.00** (FRED H.15) = regime re-established; KB-LIQ-052 framing reinstated | Duration (Leg B) / conviction |
| **Thu 6/18 — May TIC (April flows)** | Leg B flow read: Japan net, China (Belgium proxy), FOI demand hole | Japan net positive AND Belgium proxy flat/positive = Leg B closing | Japan net negative (>$20B single-month sell = SAM/MARCO signal) OR Belgium proxy crosses $500B orange (**$481B Nov → $19B headroom; one month's flow can cross → SAM+PROME 🟠 route**) = Leg B confirmation | Duration (Leg B) / foreign official |
| **Rolling (TIC 6/18 is gate 1)** | **USD/JPY flow confirmation:** level trigger fired (5 raw closes >160, 6/8–6/12) — does the repatriation *mechanism* confirm in flows? *(Successor to "USD/JPY toward 160": level clause met, confirmation clause open)* | BOJ intervention or reversal <158 sustained = level trigger without mechanism; repat deferred | TIC Japan net selling + SAM repat read confirm = SAM channel firing into LIQUID | Japan repat / Leg B |
| **Daily (rolling)** | **HY direction:** does the post-CPI widening (274→280) extend, or re-compress toward the kill? *(Successor to "276–282 compression run" — resolved by neither branch: broke wider on hot CPI)* | Re-compression: **<270 sustained ≥2 sessions = pre-trigger**; **<265 ×2 sessions = Trigger A**; if concurrent with a live APO ≥3-close streak (new fire 6/9–6/11, extension watch) = **Trigger C precondition**. Genuineness test: **CCC compressing alongside = real resolution; CCC-led divergence = bifurcation, not resolution (KB-LIQ-058)** | Extension through 300 toward 320 confirmation on substance (gate cascade, energy corner, hawkish FOMC) | Credit |
| **Rolling** | **Brent / stagflation-leg de-escalation ladder:** does the THESIS §7 kill conjunction (ceasefire + Brent sustained <$90 + 10Y <4.30) assemble? *(Successor to "Brent reflation sustainability" — overtaken: price collapsed through $95 without the ceasefire its bull branch required)* | First **sub-$90 CLOSE PRINTED 6/12 ($87.20 ICE settle)** — clause 1 of 3 now LIVE, "sustained" clock running; ceasefire and 10Y <4.30 (currently 4.45) remain unmet; all three = stagflation leg killed | Brent back >$100 sustained = oil-CPI loop re-engages | Stagflation / duration |
| **Late June** | BCRED Q2 redemption window | Redemptions ≤ cap, no hard gate = Stage 3 manageable — *but prior is higher than when first written: BROCK 6/8 = Stage 2→3 pivot, 4-fund gate cluster, 3 regular-div cuts, record 6% April default* | Hard gate OR cap breach = Stage 3→4 inflection | Credit / PC |
| **Rolling** | Powell → Warsh transition | Orderly, dovish continuity language | Hawkish shift, intervention-willingness collapse risk | Leg A / all |

---

## How to use this table

- **Each row carries an independent bull / bear binary.** Most resolve over days–weeks; some are rolling watches.
- **Basis canon is binding on every test** (CLAUDE.md KEY THRESHOLDS preamble): yields on FRED H.15 closes; price-level lines on raw unadjusted closes; auction percentages on accepted basis. A branch "fires" only on its declared basis.
- **A row resolves** when the named condition is met. Move the resolution to `STATUS.md` Durable Signals Log; retire the row here. Grade resolutions at the letter of the pre-registered test — record "fired as written, then eroded" rather than re-grading with hindsight (see Retired table, claims row).
- **A row escalates** when the bear-resolution condition fires. Cross-check with `STRATEGY.md` escalation rules and write the cross-agent signal per `STATUS.md` Cross-Domain Signals table.
- **Channel labels** map to THESIS v2.0 §4 transmission map. A bull-resolution row that fires kills *the named channel*, not the whole thesis (per THESIS §7 channel-kill vs full-thesis-kill distinction).
- **Full-thesis-kill** requires the credit-channel kill (HY OAS <260 sustained ≥3 sessions) AND duration-channel kill (10Y <4.30 sustained) concurrent. Single-channel kills are partial. The 30Y <4.90 unwind test is the duration channel's intermediate gate.

---

## Retired (6/12 sweep — outcomes at the letter of each pre-registered test)

> Compact in-file ledger; STATUS log carries one combined line; substance anchors in KB-LIQ-059 / KB-LIQ-057 / CALENDAR. *(Mild deviation from the move-to-STATUS protocol above, deliberate: STATUS's log was pruned 5/20 to pointer-plus-anchors and these six would re-inflate it. **Transition artifact — prune this table at the next TIMELINE pass** once KB-LIQ-059 + CALENDAR are confirmed stable carriers.)*

| Row (5/19 version) | Outcome |
|---|---|
| HY 276–282 compression run | Resolved by **neither branch** — broke *wider* on hot CPI (cycle-tight 274 on 6/4 → 280 on 6/10), not through 265 and no gap through 300. Successor: HY direction row |
| APO co-trigger Day 8+ / break | Both in sequence: ten straight closes >$130 (5/8–5/21, raw), **broke 5/22** without the 2nd-PC-gate its bear branch required; **new fire 6/9–6/11 without HY compression** (NOT Trigger C). Folded into HY direction row |
| "5/21 — 20Y auction" | Row was doubly misdated: 20Y auctioned **5/20** (soft-but-functional, indirect 67.7% → KB-LIQ-057); 5/21 was the 10Y **TIPS** reopening. Superseded by June refunding (10Y reopen 78.2% / 30Y 59.9%, dealer 14.7%) |
| Initial claims (5/22 print) | **Bull branch fired at the letter** — wk-5/16 printed 210k, under the <230k test — then **eroded by four rising weeks** to 229k (wk-6/6). Watch demoted to CALENDAR daily |
| BDC Q1 continuation (OBDC/ARCC/BXSL/MAIN) | Substance arrived via a different door: 3 regular-div cuts (MFIC/OCSL/OBDC) + gate cluster, not the named NAV prints (never verified). Bear-direction, incomplete → BDC monitor (populate-vs-slim pending Will) |
| April PCE (released **5/28**, row had said 5/30) | Never integrated — Tier-5 data debt, pending pull. No longer a forward branch; live inflation branch is the FOMC reaction |

---

## Out of scope here (live elsewhere)

| Lives in | Content |
|---|---|
| `STATUS.md` Durable Signals Log | Resolved events archive |
| `STATUS.md` Danger Windows | Daily / weekly volatility windows (overlaps but operational, not decision-tree) |
| `STATUS.md` Cross-Domain Signals | Current cross-agent signal status |
| `STRATEGY.md` | When to escalate / hold / de-escalate rules at the position level |
| `workbook/KILL_MEMO_HY_OAS_260.md` | Credit-channel kill trigger ladder (granular) |
| `workbook/PREDICTIONS.tsv` | Dated predictions (LIQ-03 CLO AAA resolves by 6/30) |
| `CALENDAR.md` | Data release schedule (no thesis interpretation); June opex 6/19 position decisions |
