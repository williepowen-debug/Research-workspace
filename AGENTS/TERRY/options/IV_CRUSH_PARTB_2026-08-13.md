# IV-CRUSH DIAGNOSTIC — PART B RESULTS (the free proxy, finally run)
**Run:** 2026-08-13 ~12:35 ET (Will-directed; QUEUED since the 8/4 audit, "pending" since 7/17) · **Owner:** TERRY · **Plan:** `IV_CRUSH_DIAGNOSTIC_PLAN.md` §Part B
**Tool:** `options/partb_realized_moves.py` — re-runnable, self-heals under `.venv` (one-time dep: `lxml` installed to the repo venv 8/13; yfinance's earnings-dates path needs it and failed LOUD, not silent, without it)
**Verdict class:** construction context, NOT a signal, arms nothing.

## Method (as registered 7/17)
Last 8 earnings prints per basket name (WAL, OZK, HBAN + ZION), realized **1-day close-to-close move on the reaction session** (AMC ⇒ next session, BMO ⇒ same session — all 32 rows resolved from the print's own timestamp; the convention fallback was never needed), compared against **the move the July book's puts needed**: WAL 70P = 15.5% OTM · OZK 45P = 13.8% · HBAN 16P = 12.7% (Part A, 7/17 spots).

## The data — 32 prints, Oct-2024 → Jul-2026

| | n | mean \|move\| | median \|move\| | max \|move\| | worst down | down prints | book needed |
|---|---|---|---|---|---|---|---|
| WAL | 8 | 3.43% | 3.43% | 8.93% | **−8.93%** | 3/8 | **15.5% OTM** |
| OZK | 8 | 3.10% | 1.66% | 9.70% | −6.89% | 4/8 | **13.8% OTM** |
| HBAN | 8 | 2.49% | 2.09% | 6.02% | −6.02% | 4/8 | **12.7% OTM** |
| ZION | 8 | 2.57% | 1.61% | 6.21% | −3.95% | 4/8 | (context name) |

Pooled: mean |move| ≈ 2.9% · moves ≥5% = 6/32 (19%) · **moves ≥10% = 0/32** · biggest move in the whole sample was an UP move (OZK +9.70%).

## The finding — CONFIRMED, and sharper than the hypothesis

**The registered verdict rule was: "realized move consistently smaller than the move the puts needed ⇒ structurally buying overpriced event vol, crush confirmed indirectly." It is not just consistently smaller — the needed move is outside the entire two-year realized envelope.**

1. **Not one print in 32 — up or down, any name — reached even 10%, while every held strike needed 12.7–15.5%.** The worst single-print drawdown anywhere in the sample (WAL −8.93%, Oct-2024) covers only ~58% of the distance to the 70P the book actually held through the 7/21 print. **A single ordinary earnings print structurally cannot pay a >10%-OTM put on these names.**
2. **This closes the loop Part A opened.** Part A measured the event premium concentrating in front-month deep-OTM strikes (+10 to +16 vol pts on OZK's held strikes). Part B now shows what that premium was pricing: **a move the underlying has never delivered in two years.** The richest-skew strikes are the most overpriced against realized — you pay peak event vol for an event that cannot reach your strike.
3. **Direction was never the problem — magnitude was.** Down prints ran 15/32 (~47%, a coin flip). The basket's thesis could be "right" on the print and the puts still die, because ±2–3% (the median print) leaves a 13–15% OTM strike untouched. This is Part A's "the bleed is direction+theta, not crush" restated with the event's actual size distribution attached.

## Stated limits (do not overquote this)
- **n=8 per name, and the window contains no bank-crisis print.** March-2023-class gaps (SVB/FRC; WAL itself traded ~−47% intraday 3/13/23) are outside the sample and DID exceed this envelope. The finding is regime-conditional: *ordinary* prints can't reach deep strikes. A deep-OTM bank put held through a print is therefore a bet that **the regime break lands on the print date specifically** — possible, but that is a tail-timing lottery, not an earnings trade, and the slow-transmission thesis this desk runs says the gap does NOT arrive on a scheduled date.
- Proxy, not direct IV: crush is inferred from realized-vs-needed, per the plan's own data-wall note. Part C (direct historical IV) stays KILLED (Will, 8/4).
- Close-to-close on the reaction session; an AMC print's overnight gap is inside that window by construction.

## Construction-rule candidate (the deliverable)

> **A print never justifies a deep-OTM strike. Match the strike to the event's realized envelope, or take the tenor past the print.**
> Concretely, for regional-bank singles (n=32, 2024–26): (a) a strike >10% OTM **may not cite an upcoming print as its catalyst** — the print cannot reach it; its catalyst must be the multi-quarter transmission, so its tenor must span quarters (`RISK_RULES` #16's horizon test, now with the event's measured size). (b) If the print IS the intended catalyst, the strike belongs **inside the realized envelope** (median ~2–3%, p95 ≲ 9%) — near-the-money — where the crush tax is real and a **spread selling the rich deep wing** collects the event premium instead of paying it (Part A rule 2b). (c) Size any print-spanning long option for the post-print mark, not the pre-print hope.

**Status: CANDIDATE.** Consistent with (and quantifying) existing `RISK_RULES` #16 and Part A's rules; promotion into `RISK_RULES.md` as a numbered rule is a separate deliberate step per the `options/` pipeline ("nothing is a TERRY rule until promoted"). `TRY-FIRE-002`/`TRY-FIRE-003` are PRINT-class staged cards and face exactly this test at build time.

## Handoff
- Part A (crush on the then-current book): CLOSED 7/17 — minor in dollars, priced for future entries.
- **Part B (this): CLOSED 2026-08-13.** The plan has no remaining live parts (C killed).
- The lane's durable outputs: `RISK_RULES` durable finding #8 (VRP split), rule #16 (tenor-horizon), and this envelope number. Next consumer: any PRINT-class card build.
