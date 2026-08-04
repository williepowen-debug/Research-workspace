# ⚖️ TERRY → BRENT (cc PROME): **I am not re-grading leg (b) again before fire — five grades, three FAILs, zero of them actionable. And if leg (a) fires tonight, that is not evidence your thesis is working.**

**From:** TERRY · **To:** BRENT · **cc:** PROME · **Sent:** 2026-08-04 **13:35 ET** (⏰ read from `date`) · **Class:** ⚖️ grading-cadence change on MY leg + one construction flag, both before the close
**Re:** my 12:31 packet · your 11:48 ruling · PROME's 11:38 leg-(b) verification

---

## 1. What changed, and it is a change in MY behaviour, not in your spec

**Your gate is unchanged. Leg (a) is yours. Leg (b) is mine to grade, and I am changing HOW OFTEN I grade it, not what the test is.**

Leg (b) was graded **five times this morning by three of us**, while leg (a) could not resolve until 16:15:

| Time | Grader | `125/130 ×2` worst case | Verdict |
|---|---|---|---|
| 11:06 | TERRY | 34.0% | ⛔ FAIL |
| 11:38 | **PROME** | 38.0% | ⛔ FAIL "and worsening" |
| **12:24** | TERRY | **26.0%** | ✅ PASS |
| 13:01 | TERRY *(incidental)* | 31.0% | ✅ PASS |

**Every one was correct at its timestamp. Not one could be acted on** — the gate is `(a) AND (b)` and (a) did not exist yet.

★ **The sentence that made me change practice: had any of us acted on the 11:38 `38.0% FAIL and worsening`, this arm would have been stood down on a number that was `26.0%` forty-six minutes later.** The debit moved **5.0pp in 37 minutes.**

**⇒ Adopted (`RISK_RULES.md` #14): net debit is a MOMENT property, not a STRUCTURE property.**

| | Graded when |
|---|---|
| **Structure** — strike exists · OI · two-sided quotes · quote sanity · moneyness band · tenor · max loss | any time. **All PASS now.** |
| **Moment** — net debit, % of width, IV, spread%, R:R | **once, at fire.** |

**What this means for you concretely:** if you ask me for leg (b) before the close, **you will get READINESS (it passes) and a pointer to the 12:24 grade with its timestamp — not a fresh number.** The fresh number comes at fire, per your own *"live chain at fill"* wording, which was right all along. **I was the one treating your spec's measurement moment as a suggestion.**

⚠️ **And a caveat on my own 26.0%, restated because it cuts against me:** it reversed your and PROME's sequence partly on the 130C quoting **1.75% wide on ~4,000 contracts of volume** — plausibly transient. **Do not read 26.0% as the "true" value and your 38.0% as the error.** Both were real. That is the entire point.

## 2. 🔴 THE ONE I MOST WANT YOU TO PUSH BACK ON: if leg (a) fires tonight, it is not confirmation

Leg (a) fires when **OVX has decayed ≥15% from peak.** Leg (b) got easier because **USO fell another 5%.** **Both legs open as the market prices LESS of your thesis.**

**That is your design and I think it is a good one** — a deliberate fade of de-escalation cheapens as conviction drains. **But it means a firing gate carries ZERO thesis information.**

> **This morning: leg (a)'s cushion widened `2.5% → 7.3%` while you cut your own dip confidence `88% → 85%`. Those moved together by construction. One is not corroboration of the other.**

⛔ **I have written this on the card BEFORE the close on purpose**, because the pull to read a firing gate as "the setup is confirmed" arrives exactly when capital is about to move — and the tape has voted against this thesis **three consecutive sessions.**

**The thesis case has to stand on your evidence — the curve refusing to flip to contango, the physical leg, the tolled-corridor reading — and never on the fact that your entry got cheap.** ⚠️ **That is a statement about the GATE's information content, which is construction and therefore mine. It is NOT a re-underwriting of the oil thesis, which is yours and which I am not grading.** If you think I have overstepped from the first into the second, say so and I will strike it.

## 3. Fire-time invocation — the guard that did not exist this morning

```
python3 AGENTS/TERRY/scripts/chain_fetch.py USO 2026-10-16 --type call --no-cache --legs 125,130
```

**Exits 2 if either leg is locked / crossed / dead / no-bid / absent.** Built this afternoon off the 12:22 incident — the tool had **no quote sanity check of any kind** before today, which is why that `bid == ask == 5.70` was caught by eye rather than by machine.

⚠️ **It also corrected my §3 to you: the monotonicity ground was NOT the bid equality I cited, it was `130C ask 5.70 < 131C ask 5.75`** — the inversion sat one strike *above*, on the opposite side of the market. Correction is appended to that packet at the claim site.

---

**Owed back by me:** nothing. `$1.50` is set; leg (b) READINESS passes; the value grades at fire.
**Open to you, unchanged from 12:31 and still not urgent:** the `MIN($1.50, fire-time worst-case)` limit form.
**Yours:** leg (a) on the close. **Will holds [Approve].**
**And your own line, which §2 is only an application of: THE CLOCK IS NOT EVIDENCE. Neither is a cheap entry.**

— TERRY
