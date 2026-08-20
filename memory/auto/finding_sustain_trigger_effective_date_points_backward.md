---
name: finding_sustain_trigger_effective_date_points_backward
description: "A sustain trigger's effective date points BACKWARD by construction — it dates to the EARLIER print of the qualifying pair, so judging a signal's freshness by its effective date understates it, sometimes by a whole reporting period"
metadata:
  node_type: memory
  type: feedback
---

A trigger requiring **N consecutive prints** resolves to the **earliest** print of the qualifying run, not the latest. So its stated *effective date* marks **when a condition completed**, never **when the market could first have seen the newest and worst data**. Judging staleness by the effective date therefore **understates freshness by up to (N−1) reporting periods** — and the most recent print, which is the actual information peak, is invisible in that framing.

**Why:** "effective June, six-week lag ⇒ too stale to explain an August move" *sounds* like date arithmetic and is actually a category error. The label answers a different question than the one being asked. The dismissal feels rigorous precisely because it cites a date.

**How to apply:** when dating a sustain/consecutive-print trigger, ask **two** questions, never one — *when did the condition complete?* (the effective date) and **_when did the most recent qualifying print PUBLISH?_** (the information peak). Use the second for any claim about what the market could have known. Also re-read the **level** on the owner's own preferred basis before calling a series decaying: a share-of-total series with a swinging denominator can fall in percent while the underlying rises to a record in absolute terms.

**Instance (2026-08-20, TERRY, caught by CREED):** I dismissed `CREED-T-02` as *"effective June, ~6-week lag, too stale"* for an 8/14 move. Wrong twice. The trigger needs 2 consecutive prints, so it dates backward to June by construction — while the **July** print published **8/12–13, two days BEFORE the move**. And in dollars (the owner's own stated basis, which I failed to carry) **July was the series maximum: $3.96B, +131% vs June** — the share series read 70→65→66 and looked like decay. The conclusion happened to survive on an unrelated mechanism argument, but **two of three stated reasons were wrong, and a correct conclusion resting on a refutable reason is fragile.**

**Corollary that bit the same day:** an attribution study is bounded by the prints available when it ran. The July print landed ~13 days **after** the 7/30 bank/CRE attribution closed — so that finding, still widely cited, was made **without the largest month in the series**. Not refuted; **evidentiary-base-limited**, which is a different claim and must be stated as such. See [[finding_record_of_an_action_is_not_the_action]], [[finding_instrument_cadence_cannot_resolve_the_claims_window]], [[finding_sustain_count_role_discriminating_power]].
