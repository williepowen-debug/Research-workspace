---
name: finding_grade_execution_only_against_same_timestamp_marks
description: Grading a fill against marks pulled at a different time in a moving market manufactures a fake execution finding — establish the fill timestamp FIRST, then compare like with like.
metadata:
  type: feedback
---

**Never grade an execution against marks from a different moment. Establish the fill TIMESTAMP first; if you cannot, you cannot grade the fill — say so instead of inventing a verdict.**

**Why:** on 2026-07-30 TERRY published a confident behavioural finding about itself — *"my limit-setting on liquid verticals is systematically ~5¢ too generous; n=2, Will beat me in both directions"* — and told Will so directly. **It was an artifact of a 21-minute timestamp gap and it did not survive one hour of scrutiny.**

| | TERRY's claim | Reality |
|---|---|---|
| Exit fill | Will $0.45 "beat" TERRY's $0.40 open | Will filled at **~09:50**; TERRY's marks were pulled at **10:11**, *after the trade was already done* |
| The market in between | *(assumed static)* | VIX **18.8 → 18.37** — the spread was genuinely worth more at 09:50 |
| Reconstructed 09:50 mid | — | **~0.44–0.45** (robust across beta 0.53/0.59/0.60) |
| Verdict | "n=2, Will 5¢ better both times" | **Will filled at the 09:50 mid. TERRY recommended the 10:11 mid. Both said "mid." There was never a divergence.** |

The entry leg collapsed the same way: TERRY proposed a $0.75 limit, Will worked $0.70 — **and $0.70 *was* the mark.** Neither observation shows what was claimed. **n=2 → n=0.**

**The deeper failure:** the fill time was recorded as an *inference from when TERRY happened to pull the chain*, then used as if it were the decision moment. A **behavioural** conclusion was then built on top of that inference and written to a durable memory. **An unverified timestamp propagated into a false self-model.**

**How to apply:**
- **Before grading any fill:** get the timestamp from a **physically dated artifact** (a broker export, an order confirmation), never from when you looked. *"When I pulled the chain"* is not when it filled.
- If the fill timestamp is unestablished, **the correct output is "cannot grade," not a comparison.** A missing input is a missing conclusion.
- Compare execution to the mid **at the fill's own timestamp**. In a market moving ~2%/hour, 20 minutes is worth more than the entire effect you are trying to measure — **the noise exceeded the signal by several times here.**
- ⚠️ **Behavioural self-findings deserve MORE scrutiny than market findings, not less.** They are unfalsifiable-feeling, flattering to write ("I found my own bias"), and they propagate into memory where they silently steer future decisions. **Demand a same-timestamp comparison before believing one about yourself.**
- Related: [[finding_loadbearing_number_must_be_reproducible]], [[finding_quote_carries_data_minute]], [[finding_relayed_level_predates_the_event]], [[finding_plausible_stale_value_evades_review]].

*(Supersedes the withdrawn `finding_vertical_trades_inside_its_legs_quoted_market`. The microstructure claim in that file — a vertical trades inside the sum of its legs' quoted markets — is textbook-true, but **TERRY's evidence for it was entirely this measurement error**, so it is withdrawn rather than kept on borrowed authority. Re-establish it with same-timestamp data or not at all.)*
