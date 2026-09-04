---
signal_id: SIG-W-20260903-004
date: 2026-09-03
time_dispatched: 2026-09-03T22:3xZ
origin: WALTER inbox drain 2026-09-03 ~18:2x ET on Will's "process inbox" (BM-20260903-02). Packet author self-committed under carve-out (1); WALTER routes.
source: see the originating packet named in the body; figures re-read at the packet's own artifacts before routing.
domain: JAPAN_BOJ
cluster: ASIA_CHINA
cluster_secondary: FED_FRAMEWORK
precedence: PRIORITY
action: [HENRY]
info: [LIQUID, BOND, PROME, RED]
entities: [USDJPY, BOJ, Takata, MOF, SAM-39, JGB-2Y, JGB-30Y, CME-FedWatch, usdjpy.py]
signal_type: divergence
confidence: 0.85
verdict: CONFIRMED as a move, DELIBERATELY UNGRADED as a threshold. USD/JPY 156.14 [9/3 ~07:3x ET] — ~2.5% of yen strength in two sessions, strongest yen since Aug-3, giving back the entire post-intervention weakening that carried it back through 160 on 9/1. SAM's registered 2%-intraday-gap bar is ARMED and NOT graded because its basis is unregistered and the two readings disagree.
consumer_lens: HENRY owns carry-unwind transmission — but SAM is explicit that the 2% gap routing to HENRY is NOT cleanly cleared and will not claim it is. LIQUID/BOND get the same session's JGB tape, which is front-led (policy-path repricing, not term premium). The discipline is the point: SAM refused to resolve its own ambiguity in the direction that makes the louder signal.
corrects: none
---

> 📬 **HANDOFF → BOND (INFO)** — routed from WALTER's 9/3 inbox drain (BM-20260903-02). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# USD/JPY 156.14 — the yen gave back the whole post-op move in two sessions, and SAM's 2% bar is ARMED on a basis that was never registered

## 1. The move — SAM's own tape, wire-corroborated before it hit any surface

| | level | basis |
|---|---|---|
| **live** | **156.14** | 9/3 ~07:3x ET |
| 9/2 close | 158.789 | SAM's own `USDJPY.tsv` |
| 9/1 close | 160.193 | same |
| 9/3 range | 158.968 / 155.830 = **3.138y** | ⚠️ **yfinance daily H−L — NOT SAM's registered instrument** |

Named drivers (CNBC 9/3): hawkish **Takata** remarks repricing the BOJ path · intervention talk · **Fed 50bp-cut repricing (CME ~74.5% for September)**.

⚠️ **NO CONFIRMED MOF OPERATION — and that is UNKNOWN, not "no op."** ⛔ Do not let this be downgraded to *"no intervention"* on SAM's say-so; SAM said the opposite.

## 2. 🔴 The reason this is 🟠 and not 🔴 — and it is the most useful thing in the packet

SAM's registered cross-agent 🔴 row is *"yen gaps +2%+ intraday."* **The basis is not stated on the row**, and the two natural readings disagree:

| Basis | Computation | Verdict |
|---|---|---|
| high-to-low | 158.968 → 155.830 = **+2.01%** | ⇒ **fires** |
| prior-close-to-low | 158.789 → 155.830 = **+1.90%** | ⇒ **does not fire** |

⛔ **A threshold whose verdict depends on an unregistered basis is not a fired threshold.** SAM reported it ARMED rather than resolving its own ambiguity toward the louder signal. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]` — **the same failure class as today's SKEW row and CREED's 12.00 print. Three in two days, three different desks.**

## 3. SAM-39 stays OPEN, and the instrument that would grade it is known-defective

**SAM-39** (registered OPEN: ≥1 session 8/04–9/18 with USD/JPY intraday range ≥2.5y) is **ARMED, NOT GRADED.** Its registered instrument `usdjpy.py` ingests completed sessions only and reports 5d max **2.20y [9/2]** — under the bar. The 3.138y above is an unregistered basis on an incomplete session.

🔴 **Carry this, because it can go wrong quietly:** `usdjpy.py` has a **documented under-statement failure mode** — it scored 7/31 as 2.17y against a true 3.655y. **A ~3.1y session scored under 2.5y would resolve SAM-39 FALSE on a known-defective measurement.** SAM's next boot re-runs it with `--revise-window` and cross-checks hourly-derived against daily H−L *before* grading.

## 4. ⛔ Not a re-arm
Nothing here re-arms the carry-convexity frame. THESIS **v1.7** stands (retired to LOW 8/07), no successor frame declared, **book FLAT**, re-entry needs v1.8+ with its own build case — **not a threshold tag.** CFTC is still the Aug-25 vintage (net −63,298 / 33.7% of R); this move pre-dates any positioning data that could describe it.
