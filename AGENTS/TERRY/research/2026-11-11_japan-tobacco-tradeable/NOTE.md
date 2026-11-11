# Japan Tobacco after Russia's custody decrees: tradeability read (TERRY, 2026-11-11)

**Asked by:** PROME prome-2b by message 09:4x ET (fourth read, Will's 11/10 18:03 ET word). **Source:** YURI packet `PROME/inbox/processed/2026-11-11_from-YURI_catchup-YUR-006-HIT-JTI-custody.md`, record `AGENTS/YURI/research/2026-11-11_L772_YUR-006_GRADE-and-catchup.md`. **Desk:** TERRY, Claude Code, Claude Opus 5.5, desktop. **No order, no fill, no card term, gate or level changed.** Prices are vendor screens, not broker.

## Answer: NO CARD

On the figures available, the fall already equals losing the whole Russian profit stream at the pre-decree valuation, so there is no measured overshoot to buy. There is also no instrument that lets the loss be defined. Kept as `TRY-NOTRADE-JT-NOV11`.

## The primary fact (YURI, read at pravo.gov.ru)

Указ №817 (5 Nov) and №832 (6 Nov) put all seven JTI companies in Russia under state temporary management by АО «Промышленные активы», with no sale or transfer clause. JT keeps title on paper and loses control.

## Why, in figures

| # | Reason | Figures (date, basis) |
|---|---|---|
| 1 | **The drop matches a full write-off of Russia's profit share; it does not exceed it.** Value lost from the last two pre-decree closes: ¥3.23T from ¥7,383 (11/4) and ¥3.92T from ¥7,769 (11/5), on 1,775.4M shares. A quarter of the pre-decree market value (Russia's press-relayed share of adjusted operating profit): ¥3.28T (11/4 basis), ¥3.45T (11/5 basis). Ratio of loss to that quarter: 0.98× (11/4 basis) to 1.14× (11/5 basis). Russia's net assets per JT's 11/9 statement as relayed: about ¥1.5T of assets including goodwill, ¥0.36T cash, ¥0.2T liabilities, so about ¥1.3T net. | vendor daily closes (61 bars, 3 months), vendor share count; TERRY arithmetic |
| 2 | **The loss cannot be defined.** JAPAY (the US ADR, 0.5 share each by price: ¥5,562 ÷ 159.38 ≈ $34.90 vs $17.75) has **0 listed option expiries**, so the only vehicle is shares. Tokyo locked limit-down on 11/6 (−19.3%) and 11/9 (−16.0%); the ADR gaps with it overnight, so a stop does not cap the loss. ADR vendor quote 09:46 ET bid $17.75 / ask $17.56 (crossed: not usable), 3-month average volume about 87,000. | `chain_fetch.py JAPAY` 0 expiries; vendor |
| 3 | **The inputs are press relays, not JT's documents.** The 10% revenue / 25% adjusted operating profit split is 2Firsts paraphrasing JT's revised FY2026 forecast; JT's 2022 disclosure, also seen only second-hand, put Russia at about 8% / 15%. jt.com and jti.co.jp return 403 to this box on both JT PDFs (11/6 and 11/9 releases); no workaround attempted. A mispricing claim rests on that denominator. | WebSearch and fetch, 09:46 ET |
| 4 | **No owner holds a JT valuation view, and the two paths do not net to a direction.** YURI's "priced close to a full write-off" is its own inference, unverified. The upside path is a return of the business, which earlier custody cases did not produce (Danone, Carlsberg ended in discounted forced sales; YURI context). The downside path is a dividend cut: ¥272 a share (vendor) is a 4.9% yield at ¥5,562, and losing a quarter of profit puts it in question. JT has not said either way. | YURI record; vendor |

**Tape, for the record:** 2914.T ¥7,383 (11/4) → ¥7,769 (11/5, +5.2%, cause not checked) → ¥6,269 → ¥5,269 → ¥5,500 → ¥5,562 (11/11 close, +1.13%). Rebound off the 11/9 low +5.6%. JAPAY $17.50 last daily bar, $17.75 +1.60% at 09:45 ET.

## What would change the answer (each a fresh build on that day's prices)

1. **JT's own impact statement or revised forecast, read at the primary:** an impairment figure, a dividend decision, deconsolidation. A held dividend with an impairment near the ~¥1.3T net would make the 0.98–1.14× ratio the whole story; a cut would add a leg. Will can open the JT PDFs in a browser; this box cannot.
2. **A named buyer or sale price for the Russian business** (YURI's YUR-C01 falsifier, DAEDALUS grades 11/28): a recovery value turns the write-off into a number.
3. **A defined-loss vehicle:** listed JAPAY options, or a reason to accept a share position sized for a further limit-down sequence (two −16% to −19% gaps in a row would take a $500 risk budget to about $1,550 of shares, about 87 ADRs).

## Small items logged (WQ-622)

Recorded here only: no live `combo:` theme covers Japan single names or Russian asset seizures. Logging is not scoring.

## Addendum 12:3x ET — PROME's three questions (what Will's browser read of JT's PDFs would decide)

**Correction to reason 2 (made here, not by rewriting it):** "the loss cannot be defined" binds a **short** and a **stop-sized long**; it does **not** bind a **long sized at its whole stake**. At the $500 default, about 28 JAPAY ADRs at $17.75 (vendor, 11/11), the most that can be lost is the $500. A repeat of the two limit-down gaps (−19.3% then −16.0%, about −32% compounded) would cost about $160. So the instrument objection falls away for a long. The NO CARD rested on reasons 1, 3 and 4 as well, and those turn on the profit-share figure.

**(1) Long, defined loss:** yes, as above. Stake-sized, no stop, max loss = the stake.

**(2) At about 15%: yes, I would build a NOT-FIRED long.** Overshoot ratio = value lost ÷ (Russia's profit share × pre-decree market value): 0.98× at 25% on the 11/4 basis, which scales to 0.987 × 25 / s. **TERRY's line (a construction line, not a gate): at or below about 17.5% share the ratio is at least 1.4× on the 11/4 basis (1.6× on 11/5),** enough room over a full write-off to pay for the dividend-cut and trapped-cash risks. At 15% it is 1.64× (1.89×). Shape I would put to Will: JAPAY shares, $500 stake (≤ X1 default, stake = max loss), NOT-FIRED until JT's own impact statement is out and does not cut FY2026 dividend guidance; enter on a red JAPAY session (root rule #6, shares long); invalidation: JT cuts the dividend, or Russia names a buyer at a nominal price (YUR-C01 inverted); time stop 11/28 (DAEDALUS grades YUR-F02), re-priced then. **The one figure Will should read: Russia's share of JT's adjusted operating profit**, as JT itself states it in the FY2026 forecast (Q3 release) or the 11/9 "Update on JT Group's Business in Russia". The dividend line is the second read, and it is the trigger, not the gate to building.

**(3) If JT's own figure is near 25%:** NO CARD stands, because the fall is then about a full write-off (0.98–1.14×) and a long buys no margin over it. So the read is worth Will's time only to settle that one number.
