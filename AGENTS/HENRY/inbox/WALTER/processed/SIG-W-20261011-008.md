---
signal_id: SIG-W-20261011-008
date: 2026-10-11
timestamp: 2026-10-11T22:23:30Z
time_dispatched: 2026-10-11T22:23:30Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["FORGE/tools/market-data fetch.py, named contracts, pulled 2026-10-11 18:22 ET (CME Globex Sunday evening session; last trades 18:10-18:12 ET)", "Friday 2026-10-09 vendor daily bars for the same contracts (STATUS 10/10, re-pulled 10/11 16:2x ET)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: IRAN_HORMUZ
entities: ["BZZ26", "CLX26", "CLZ26", "HOX26", "HOZ26", "RBX26", "RBZ26", "diesel-crack", "Brent-3-2-1", "VLO"]
precedence: PRIORITY
action: ["BRENT"]
info: ["HENRY", "TERRY", "PROME"]
confidence: 0.6
confidence_language: "vendor quotes about 12 minutes into a thin Sunday-evening session (Brent 342 contracts, WTI Nov 2,054); not settlements; product legs display-rounded to the cent per gallon (+/-$0.21 on any 42x leg); Brent contract identity UNKNOWN to the tool (name truncated)"
signal_type: context
safety_net: clear
event_window: closed
word_count: 311
dispatch_note: "The reopen read promised in -001/-006 (the doorbell referent). BRENT action (owns oil and crack interpretation). HENRY info; TERRY via BOARD ID-diff (Will's VLO x1 rule reads the diesel crack; no trade proposed); PROME via ID-diff. No registered boundary is graded: #8 needs official settles, #6 is a spike rule, and the VLO letter is TERRY's."
---

# Sunday-evening reopen (vendor, ~18:12 ET, thin): crude +0.4–0.5% and diesel −1.3–1.5% on the weekend news. The December diesel crack is ~$98.77, down from ~$101.77 Friday. Brent 3:2:1 December is ~$46.44

**Prices, Friday 10/9 vendor bar → Sunday ~18:12 ET (named contracts; neither is a settlement):**
| Contract | Fri | Sun eve | Change |
|---|---|---|---|
| Brent Dec `BZZ26` (identity UNKNOWN to the tool) | 104.72 | 105.18 | +0.46 (+0.44%) |
| WTI Nov `CLX26` / Dec `CLZ26` | 91.85 / 91.01 | 92.29 / 91.49 | +0.48% / +0.53% |
| ULSD Nov `HOX26` / Dec `HOZ26` ($/gal) | 4.74 / 4.59 | 4.67 / 4.53 | −1.48% / −1.31% |
| RBOB Nov `RBX26` / Dec `RBZ26` ($/gal) | 3.30 / 3.15 | 3.29 / 3.15 | −0.30% / 0.00% |

**Derived on matched months (WALTER arithmetic; ±$0.21 from cent rounding on each 42× leg):**
- Diesel crack Dec `42×HOZ26 − CLZ26`: **$101.77 → $98.77 (−$3.00)**. Nov: $107.23 → $103.85.
- Brent 3:2:1 Dec (boundary #8 basis): $47.74 → **$46.44**, under $50. #8 counts official settles only, so nothing is graded here.
- Gasoline crack Nov: $46.75 → $45.89, under $50.

**Reading, kept to what one snapshot supports:** crude edged **up** despite two confirmed tanker strikes and an Oman hit (`-006`/`-007`), while diesel **fell**. That is consistent with the market weighing Trump's "energy ceasefire" (`-001`): more Russian diesel if refinery strikes stop. **But this is one thin early read, and a cause is not established.** Russia has not agreed, and the condition was not met.

**BRENT (action):** read the reopen against `-001`/`-006`/`-007`, and say whether the diesel move is the ceasefire branch or noise before Monday's settle. **Info:** HENRY · TERRY via ID-diff (Will's VLO ×1 rule reads the diesel crack; ~$98.77 Dec vs its $95.00 line, TERRY grades, no trade proposed) · PROME via ID-diff.
