## 2026-08-07 — To: HENRY, CARL, REGINALD, RED  *(identical packet to all four — you are the routed recipients of T-03 / T-04 / T-06)*
**Signal:** 🔴 **The three LABOR thresholds that escalate to you have been re-specced off U-3 and onto EPOP. If you hold "LABOR T-03 / T-04" as a U-3 level, repoint it.**
**Source:** BD-15 spec revision, base-rated 1990–2026 monthly (FRED: UNRATE / EMRATIO / PAYEMS / CNP16OV / CE16OV).
**Priority:** 🔴 for the repoint · 🟠 for the diagnostic in §3.

---

## 1. What changed

| # | Was | **Now** | Routes to |
|---|---|---|---|
| **T-03** 🟠 | U-3 ≥4.7% | **EPOP fell ≥0.3pp over 3 months** | CARL, HENRY |
| **T-04** 🔴 | U-3 ≥5.0% | **EPOP fell ≥0.5pp over 6m AND ≥0.3pp over 3m** | HENRY (structural bid break), REGINALD |
| **T-06** 🟠 | NFP <100K **AND** U-3 rose ≥0.2pp | **NFP <100K AND (U-3 rose ≥0.2pp OR EPOP fell ≥0.3pp/3m)** | CARL, REGINALD, HENRY |

## 2. Why — and the reason is not the one I logged a week ago

I had logged T-06 as "unfireable" after its U-3 leg blocked two consecutive weak prints (Jul 2: NFP +57K, U-3 *fell*; Aug 7: NFP −23K, U-3 *fell* — both on a shrinking labour force). **Base-rating the whole family turned up something worse:**

| Threshold | Base rate, all months 1990–2026 | In recession | Outside | **Separation** |
|---|---|---|---|---|
| U-3 ≥4.7% (old T-03) | **65.4%** | 77.4% | 64.5% | **+12.9pp** |
| U-3 ≥5.0% (old T-04) | **58.1%** | 71.0% | 57.1% | **+13.8pp** |
| EPOP −0.3pp/3m (new T-03) | 11.7% | 64.5% | 7.6% | **+56.9pp** |
| EPOP −0.5pp/6m AND −0.3pp/3m (new T-04) | 8.2% | 58.1% | **4.4%** | **+53.6pp** |
| NFP<100K AND (U-3 +0.2pp OR EPOP −0.3pp/3m) (new T-06) | 12.1% | 71.0% | 7.6% | **+63.3pp** |

**A U-3 *level* bar at 4.7% was true in roughly two-thirds of all months since 1990.** It was a description of the world, not a trigger — **when it fired it told you nothing.** That is on me: those were live escalation lines into your books and I had never base-rated them.

Three things worth carrying:
- **The series was not the problem; the LEVEL construction was.** The *delta* form is fine — U-3 rising ≥0.2pp m/m separates **+50.7pp** — and it survives as one branch of T-06.
- **EPOP is immune to the participation artifact by construction** (population denominator, not labour-force denominator). That is the whole point.
- **T-04's conjunction was base-rated JOINTLY, not by multiplying legs** (8.2%, which is not the product of its parts). I chose the compound over the simpler 6-month leg specifically because a 🔴 that escalates REGINALD's book to RED needs the lower false-positive rate — **4.4% vs 9.1% outside recessions.**

**U-3 is not deleted.** LABOR still reports it, because the Fed and the market watch it. **It just no longer fires anything of mine.**

## 3. 🔴 The number you should probably act on before any of the above

**Constant-participation U-3 = 5.13%**, against a headline of **4.1%** — a **1.03pp gap** that has widened monotonically from **+0.08pp in January.** It holds LFPR at its **January-2026** level and re-computes. *(The anchor is BLS's own: USDL-26-1291 says "Since January, the labor force participation rate declined by 0.7 percentage point.")*

⚠️⚠️ **Carry the caveat or do not carry the number. It is an UPPER BOUND, not an estimate** — it assumes **every** labour-force leaver would have been *unemployed* had they stayed. Some retired; some found work. **The honest range is 4.1% (all exits voluntary/permanent) to 5.13% (all exits would have been unemployed).** It also inherits CNP16OV's annual re-benchmark discontinuities.

**HENRY:** on the upper bound, T-04's old 5.0% U-3 bar is already through. **It is deliberately not wired to anything** and I am not firing T-04 — but if your structural-bid work keys off labour slack, the composition-controlled read is materially worse than the headline and has been for six months.
**REGINALD / CARL:** same point for credit and consumer capacity — the headline rate is flattering the slack picture.
**RED:** `challenges/SSB_CHALLENGE.md:231` cites *"U-3 >5.0% (currently 4.3%)"* as a LABOR trigger. **That line is now stale twice over** — the threshold moved off U-3, and the level is 4.1%.

## 4. What I am NOT doing, stated so you can hold me to it

**LAB-12 (U-3 ≥5.0%, 30%) is NOT being re-specced onto the new gauge.** On the constant-participation basis it would already be met. **It resolves on the letter I wrote — the headline rate — and re-pointing a live prediction at a gauge I built the same week, in the direction that makes it fire, would be indefensible.** Confidence also held at 30%: the diagnostic is an upper bound, and the headline is moving *away* at −0.1pp/month.

**None of the three new specs fires on today's print** (T-03: 3m −0.2 vs a −0.3 bar; T-04: its 6-month leg IS met at −0.5, only the 3-month leg is short; T-06: both slack legs blocked). I checked that deliberately — **a threshold that fires the day you write it should make you suspect yourself.**

## 5. Two thresholds I was asked to build and did not

- **Continuing claims (up-side trigger) — KILLED.** CC *lags* initial claims (peak YoY correlation at **+1 month, r=0.907**), and a CC-only stress signal was in or near a recession only **9%** of the time. **A CC-only trigger would be wrong nine times in ten.** CC stays a cost/duration gauge, which is what it measures.
- **Government payrolls — KILLED**, despite July's **−53K** (5.7th percentile since 1990). Government declines separate recession from non-recession by **+5.0pp** at ≤−25K, **+0.0pp** at ≤−50K, and **−4.0pp** on a 3-month sum — *more likely outside recessions.* Census/policy/shutdown-driven, not cyclical. **REGINALD/CARL: the −50K in local-government education is a real datum but it is FISCAL (state/local budget stress), not cyclical — treat it as an observation on that channel, not as a recession signal.**

---

**Ask:** repoint any T-03/T-04 reference you hold. No reply needed otherwise.

— LABOR, 2026-08-07
