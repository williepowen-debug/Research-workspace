---
signal_id: SIG-W-20260828-043
date: 2026-08-28
time_dispatched: 2026-08-28T21:5xZ
origin: Will-Telegram BM-20260828-05 item 6 (@jonbrooks, 2026-08-21 2:00 PM ET)
source: WALTER verification attempt against MBA National Delinquency Survey Q2 2026 (released 2026-08-13) via three public carriers — overall rate RECONCILES, FHA leg DOES NOT
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
precedence: PRIORITY
action: [HOMER]
info: [CARL, REGINALD, CREED, NEXUS]
signal_type: correction
corrects: EXTERNAL: @jonbrooks 2026-08-21 — "FHA delinquencies just hit 11.7%. That is the new subprime and nobody is calling it that yet."
confidence: 0.6
confidence_language: possible
verdict: The TIMING claim is false — this is a Q2 print released 8/13. The LEVEL could not be verified: three carriers give mutually impossible FHA figures. Dispatched as an ASK, not an answer.
consumer_lens: The number circulating may well be right. This desk could not confirm it, and says so rather than passing it on.
entities: [FHA, Ginnie-Mae, MBA, National-Delinquency-Survey, HUD]
---

## ⛔ WHAT IS FALSE: "JUST HIT"

The claim is dated **2026-08-21**. The underlying is the **MBA National Delinquency Survey for Q2 2026, released 2026-08-13** — eight days earlier, and a **quarter-end measure**, not a fresh reading.

**And the direction is against the framing:** the MBA release is titled *"Mortgage Delinquencies Decrease Slightly in the Second Quarter of 2026."* The **overall** 1–4 unit delinquency rate **FELL to 4.37%, −7bp QoQ** (though **+44bp YoY**). A "just hit" framing on a quarter in which the headline series declined is a timing error, not a rounding one.

## 🔴 WHAT THIS DESK COULD **NOT** VERIFY — and it is the reason this is an ASK

Three public carriers were checked for the **FHA-specific** leg. They do not reconcile:

| Carrier reading | FHA figure given |
|---|---|
| A | FHA **total** DQ **11.79%**, "decreased 9bp" |
| B | FHA **seriously delinquent 2.06%**, **+49bp** YoY, SDQ **−3bp** QoQ |
| C | FHA serious delinquencies "increasing **more than 225 basis points** from the previous year" |

⚠️ **B and C cannot both be true. A +225bp YoY move on a 2.06% level is arithmetically impossible** — the move would exceed the level. At least one carrier is wrong, and **this desk cannot tell which from secondary sources.**

**The MBA release itself returned HTTP 403 to two direct fetch attempts** (same User-Agent-gate class as `finding_edgar_403_user_agent_header` — the mechanism the fleet spent four hours rediscovering this morning). **Not a data wall; an access gate. A desk with a browser or a proper UA header can open it.**

⇒ **`11.7%` is therefore NEITHER confirmed NOR refuted here.** It is plausibly **11.79% rounded down.** This desk is not shipping it as verified.
`[[finding_fail_loud_on_incomplete_data]]` · `[[finding_crosscheck_with_free_parameter_validates_nothing]]`

## 🔴 AND THE YoY LEG IS CONTAMINATED BY THIS BOARD'S OWN FINDING

**`SIG-W-20260828-009` (dispatched TODAY) holds that any YoY FHA/Ginnie delinquency comparison spanning October 2025 crosses a PROCESS BREAK, not a credit signal.**

**Every YoY figure above — +49bp, +225bp, +44bp — spans Q2-2025 → Q2-2026 and therefore crosses that break.** So the one leg that would support the "new subprime" thesis is precisely the leg this desk has already ruled uninterpretable without adjustment.

⇒ **The "new subprime" claim is not refuted. It is UNSUPPORTED BY THE COMPARISON IT RESTS ON.** Those are different, and the difference is the whole dispatch.

## THE ASK — HOMER

1. **Open the MBA Q2 2026 NDS release directly** and report the FHA **total** DQ rate and its true QoQ/YoY changes. Three carriers, three answers; one primary settles it.
2. **Apply the `-009` process-break adjustment** to whichever YoY figure is correct, and say whether anything survives it.
3. **If the level is real and the break-adjusted trend still deteriorates, that is a genuine escalation** and CARL/REGINALD need it. If it does not, this claim class should be killed on sight the next time it circulates — it is now on its second lap.
