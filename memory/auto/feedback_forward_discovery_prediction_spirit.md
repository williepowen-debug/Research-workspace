---
name: forward-discovery-prediction-spirit
description: "When a prediction's literal text is satisfied by pre-existing public data the agent didn't know about at creation, resolve by the forward-discovery SPIRIT (was something NEW found in-window?) not the literal reading — log the data, keep the prediction OPEN, drop confidence"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 100558f6-d8df-4075-804f-2f8e2484343f
  modified: 2026-07-25T16:04:00.160Z
---

Many predictions are implicitly **forward-discovery** bets: "a Nth case/name/disclosure will SURFACE by date X." Their intent is that something *new* emerges during the prediction window. If you later discover the literal text was already satisfied by public data that existed *before* the prediction was made (you just hadn't logged it), don't auto-confirm — that rewards archaeology, not foresight. Resolve by spirit: did a genuinely new instance appear in-window?

**Why:** OTTO-30 predicted "a 6th US bank discloses Tricolor exposure by Q2 2026." Research later surfaced Origin Bancorp's $74.7M Tricolor disclosure — but dated Oct 23 2025, *predating* the Apr 15 2026 prediction. Literally a 6th name; not a forward discovery. OTTO logged the Origin data, kept OTTO-30 OPEN, and dropped confidence (the forward-discovery window hadn't actually produced a new name yet). Confirming on the pre-existing disclosure would have scored a "hit" that wasn't.

**How to apply:** At prediction creation, note whether the bet is forward-discovery (something new surfaces) vs static-threshold (a level is/becomes true). For forward-discovery predictions, write the invalidation as "no NEW [name/case/disclosure] AFTER [creation date]." When pre-existing data turns up that satisfies the literal text, log it as a known-unknown, hold the prediction OPEN, and adjust confidence — don't retroactively confirm. Transferable to any prediction-book steward.

**⚠ It happened again on the same prediction (2026-07-25).** A complete EDGAR full-text scan surfaced **Triumph Financial / TBK Bank** ($60.5M Tricolor floorplan facility, ~$22.5M held) — disclosed since a **2025-09-11 8-K**, seven months *before* OTTO-30 was written, and missed by press monitoring for over ten months. This scoring rule was applied correctly both times, and the trap still recurred — because it governs *how to score* a known-unknown, not *how to stop generating them*. The missing half is the discovery **instrument**: see [[finding_discovery_instrument_defines_the_claim]]. Read the two together.
