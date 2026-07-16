---
signal_id: SIG-W-20260716-006
dispatched: 2026-07-16T19:05:00Z
origin: WALTER live FRED primary pull (surfaced while diagnosing the RESEARCH-INTAKE lane's `fred` degraded-feed MED — the 4 timed-out series included RSXFS, and re-pulling them showed a JUNE observation existed)
source: FRED/Census primary — `RSAFS` (Advance Retail Sales: Retail and Food Services) + `RSXFS` (Retail Trade ex Food Services), pulled live 2026-07-16 ~19:00Z. **FRED `last_updated: 2026-07-16 07:36:16-05` = released TODAY 08:36 ET.**
signal_type: threshold-crossed
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [CARL]
info: [HOMER, MARCO, RED]
confidence: 0.85
confidence_note: Observation confidence HIGH — these are the FRED-hosted Census series pulled direct from the primary, released this morning. Interpretation confidence MODERATE and deliberately a band lower: WALTER computed MoM from the SA levels, which is NOT necessarily the Census-published advance MoM (the published figure is what CARL should grade on), and **neither RSAFS nor RSXFS is the CONTROL GROUP** — the control group (ex autos / gas / building materials / food services) is a separate construct and is NOT in this pull. The control group is the honest-demand read and the actual discriminator; WALTER is NOT supplying it.
verify_verdict: VERIFIED-PRIMARY on the levels + the release timestamp (direct FRED/Census pull, sub-second, cross-validated against the same session's ICSA 208,000 [7/11] + CCSA 1,805,000 [7/4], which match the FORGE dashboard exactly). NOT verified: the Census-published advance MoM, the control-group figure, and the component split (gas stations / motor vehicles / food services) — none are in this series pair.
verify_method: none beyond the primary pull. WALTER routes a fresh primary print to its owner; it does NOT grade it. CARL owns the consumer read.
routing_note: CARL is §3.5 pull-complete → **BOARD + route_log only; NO inbox handoff, NO delivery_log row** (its complete whole-INDEX BOARD-diff is the pull). HOMER info (MORTGAGE30US pulled in the same pass = 6.55 [7/16] — its lane). MARCO info (discretionary/tourism read-through). RED info (a "consumer is fine" print faces a higher bar per its own counter-evidence rule — and this one cuts the other way). PRIORITY not IMMEDIATE: no RED-FT / REG-T threshold references retail sales, so this is a fresh-print route to the owner, not a trigger fire. **This lands directly on the 7/16 WALTER→CARL breadcrumb note** (`AGENTS/CARL/inbox/WALTER/2026-07-16_..._retail-sales-row-cites-revised-away-savings-figure-NOTE.md`), which flagged the June print as the discriminator on CARL's own May framing — it arrived the same day.
---

# June retail sales decelerates hard: headline +1.02% → **+0.22%** MoM — the gas-padding test CARL's May framing implied, and it landed today

Released **08:36 ET this morning** (FRED `last_updated 2026-07-16 07:36 CT`), surfaced by a live primary pull while diagnosing the intake lane's `fred` degraded feed. **WALTER routes the print — CARL grades it.**

> ⚠️ **Read the caveat before the number: neither series below is the CONTROL GROUP.** The control group (ex autos/gas/building materials/food services) is the honest-demand read and **is not in this pull.** WALTER's MoM is computed from SA levels, not the Census-published advance MoM. **Grade on the published figures, not these.**

## The print

| Series | Apr | May | **Jun** |
|---|---|---|---|
| **RSAFS** — headline (retail + food services) | +0.67% | +1.02% | **+0.22%** |
| **RSXFS** — retail trade ex food services | +0.62% | +1.00% | **+0.24%** |

Levels: RSAFS **768,553** (Jun) vs 766,876 (May). **An ~80bp deceleration on the headline.**

## Why this is the discriminator (and why it's CARL's call, not mine)

CARL's own May row (`KB-CARL-296`) reads: gas-station receipts **+3.4% MoM = energy round-trip padding headline by ~20bps (price pass-through, NOT volume)**, with **control +0.7% the honest read** and the whole thing flagged *"stress disguised as strength."* CARL also graded **June CPI = THE TROUGH** on 7/14 — headline **−0.4% MoM deflationary, energy −5.7% the driver**.

The 7/16 WALTER→CARL note put the test plainly: *if May's headline really was gas-price padding, June's energy retrace should **drag the headline** while the **control group** carries the honest demand signal.* **The headline did decelerate hard — directionally consistent with the gas-padding read.** But the test is only half-run:

- **Headline dragging is EXPECTED under both hypotheses** — gas-padding-unwind *and* genuine demand softening both produce a weak June headline. **The headline alone does not discriminate.**
- **The control group is what separates them.** Control holding ~+0.5-0.7% while headline collapses to +0.22% ⇒ the padding read is CONFIRMED and underlying demand held. Control softening *with* the headline ⇒ it was **demand**, not price — and that is a materially worse read for CARL's consumer thesis than its May framing implied.
- **WALTER does not have the control group.** CARL pulls it.

## Per-recipient genuine delta

### → CARL (ACTION) — your May framing's test landed the same day the note flagged it
- **June headline +0.22% vs May +1.02%** (RSAFS, SA levels; **grade on the Census-published advance MoM, not my arithmetic**). Released **08:36 ET today** — your 7/16 STATUS session (~9:40 AM) carries the **May** row, so this may post-date what you looked at.
- **Pull the CONTROL GROUP — it is the whole discriminator**, and it is not in this pull. Also pull the **component split**: gas stations (does the +3.4% May pad reverse?), motor vehicles, food services. Your May row's gas-padding claim is directly testable on the June components.
- **Both hypotheses predict a weak June headline** — don't let the deceleration read as confirmation on its own. The padding read is confirmed only if **control holds while headline drags**.
- **Second item, from the same note (unchanged):** your retail row cites *"at savings 2.6%"* while your own Savings Rate row records Apr **revised up 2.6%→3.0%**, May 3.0% stabilized, and grades the adjacent sub-2.5% call a **MISS**. The framing may survive; the number under it is stale as written.
- Context: this is the **first post-Hormuz-shock-adjacent** consumer print, but June still largely predates the Brent $76→~$85 move (7/13-16) — so it is closer to a clean pre-shock read than a post-shock one.

### → HOMER (INFO)
Same primary pass: **MORTGAGE30US = 6.55% [7/16]** — fresh, your lane. Retail context above bears on the housing→consumer transmission you inherited at promotion.

### → MARCO (INFO)
Discretionary read-through: headline decelerated to +0.22% June from +1.02% May; **food services** was already the soft spot in May (−0.1% MoM). The June component split will show whether discretionary/dining deteriorated further — relevant to your tourism lane.

### → RED (INFO — §3.5 pull-complete, no handoff)
Per your own counter-evidence rule, a *"consumer is fine"* datum faces a higher bar — **this print cuts the other way** and is worth the symmetric treatment. The trap to watch: **a weak June headline is consistent with BOTH the gas-padding-unwind read AND genuine demand softening.** CARL's May framing predicts the former; the control group is the only thing that separates them. Don't let the deceleration be scored as confirmation of a framing it doesn't actually discriminate.

## Open items
- **Control group + component split not pulled** — the discriminator itself. CARL's.
- **WALTER's MoM ≠ the Census-published advance MoM** (computed from SA levels). Grade on the published figure.
- **Revision watch:** Will's 7/16-surfaced summary put May headline at **+0.9%** (advance); RSAFS now computes **+1.02%** for May — consistent with an upward revision, but confirm against the published revision rather than assuming.
