# HEN-46 F1 · 9/25 settlement — resolved by inference (CME not read)

**Written:** 2026-09-28 21:43 EDT (`date`), HENRY, on Will's "you can't do this lookup?" · CME settlement pages unreachable from this box (curl exit 92); EIA stopped publishing NYMEX futures in 2024-04.

## Result
**Nov ULSD crack 9/25 = HOX26 4.4621 × 42 − CLX26 92.41 = $94.9982 ⇒ BELOW $95.00 ⇒ F1 FIRES** — by **$0.0018/bbl, less than one HO tick** (1 tick = $0.0001/gal = $0.0042/bbl). A HO settle of 4.4622 would give $95.0024 (not fired). **The verdict rests on the last digit of the HO settle.**

## Why these are the settlements
| Check | Yahoo daily close | Independent settle | Match |
|---|---|---|---|
| CLX26 9/23 | 92.16 | 92.16 (9/24 report "up 2.45 from Wednesday's 92.16") | ✅ exact |
| CLX26 9/24 | 94.61 | 94.61 (same report; BRENT) | ✅ exact |
| **CLX26 9/25** | **92.41** | **92.41** = 9/28 settle 92.60 − "added 19 cents" (9/28 wire) | ✅ exact |
| BZX26 9/25 | 104.32 | 104.32 = 105.28 − "gained 96 cents" (9/28 wire) | ✅ exact |
| HOX26 9/24 | 4.528 | BRENT settle proxy 4.528 | ✅ |
| **HOX26 9/25** | **4.4621** | — no independent read | ⚠️ inferred by the pattern above |
On 9/23–9/24 the Yahoo daily close differs from the last 1-minute trade (evening session) and equals the settle ⇒ Yahoo writes the settle into the daily bar. 9/25 (Friday, no evening session) shows the same value in both.

## Rejected source
DTN's 9/25 story ("ULSD Oct … to $4.8007", "WTI Nov … to $92.60") is **not a settlement**: its levels match 1-minute trades at ~15:15–15:35 ET, an hour after the 14:28–14:30 window, and its WTI level contradicts the wire-derived 92.41. DTN pages are updated intraday.

## Settle-window proxy vs settle (why TERRY's $95.0014 was UNKNOWN, not wrong)
Yahoo 1-min VWAP 14:28–14:29 on 9/25: HOX26 4.4596 · CLX26 92.30 ⇒ $95.00. Proxy error vs true settles on known days: CL +2¢ (9/23), +6¢ (9/24), −11¢ (9/25) ⇒ the proxy cannot resolve a $0.00 margin. The daily-close settle can.

## Consequences (letters, not actions)
- **HEN-46 F1 = STAND DOWN** (not dead; dead is < $90.16). Row stays ACTIVE for grading at the Q3 prints; the entry expression stands down.
- **GATE-TERRY-VLO-SCALE:** TERRY grades; on its letter a settle < $95 makes the row terminal and **both staged shares stand down**. **GATE-TERRY-VLO-HELD-01:** notice only on the held share, no action.
- **Certainty upgrade:** anyone who can open CME's NY Harbor ULSD settlements page for trade date 09/25/2026 and read the Nov-26 settle (expect 4.4621) makes this exact.
