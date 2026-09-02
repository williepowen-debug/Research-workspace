# DM long-end cross-section — 9/3 REBUILD LEG, and a NEW form of the estimator defect

**BOND · 2026-09-01 ~21:1x ET · all figures BOND's own pulls at issuer primaries, this session**
**Tool: `monitors/dm_cross_section.py` (BUILT THIS SESSION — see §0) · consumer: SAM, 9/3 30Y JGB auction grade**

---

## 0. The instrument now exists as an instrument

The Will-ruled 8/10 forum scope says this desk runs a *"DM sovereign-spread cross-section … as a
**standing series** at BOND's own primaries."* **It has never been one.** The 8/20 work
(`analysis/2026-08-20_cross-section_horizon-instability.md`) was an ad hoc hand-pull, and nothing
on any surface said the standing series did not exist — SAM's 8/20 ask is what found that, and it
stayed un-built for a further 12 days. `monitors/dm_cross_section.py` is the discharge.

It encodes the three path-artifact defects that have each cost this desk a false reading, because
**every one of them presented as "the source is unavailable"** (n=5 on this class now):

| # | Defect | What it produced |
|---|---|---|
| 1 | MOF `jgbcme_all.csv` lives under `/historical/`; the flat path 404s, and the file ENDS AT THE PRIOR MONTH | a carried-forward endpoint rendered **JP Δ = +0.0bp for every August window** as a real "Japan didn't move" reading |
| 2 | BoE IADB returns **302 with ZERO BYTES** unless redirects are followed | reads exactly like a refusal |
| 3 | MOF column is `10Y`/`30Y`, not `10`/`30`; RBA daily is `f2-data.csv` (`FCMYGBAG10D`), not `f2.1-data.csv` | "series not found" — which reads exactly like an unavailable series |

A `STALE_ENDPOINT_DAYS = 4` guard now **refuses to silently carry an endpoint** and names the lag on
every leg instead.

---

## 1. The rebuild — TRUE like-for-like (all four legs at the SAME endpoint, 8/13 → 8/27)

| Leg | Series (primary) | 8/13 | 8/27 | Δ | rank |
|---|---|---:|---:|---:|:--:|
| EA AAA 10Y | ECB SDW `SV_C_YM.SR_10Y` | 3.156 | 3.277 | **+12.2bp** | 1/4 |
| UK 10Y | BoE IADB `IUDMNPY` | 4.944 | 5.025 | **+8.2bp** | 2/4 |
| US 10Y | FRED `DGS10` | 4.630 | 4.670 | **+4.0bp** | 3/4 |
| **JP 10Y** | MOF `jgbcme` merged | 2.873 | 2.897 | **+2.4bp** | **4/4** |

**DM median +6.1bp · min-across-legs +2.4bp · spread 9.8bp · common DIRECTION yes (all four positive).**

🔑 **JAPAN IS LAST OF FOUR, 3.7bp BELOW THE DM MEDIAN.** That is not what a Japan-specific demand
vacuum looks like at the 10Y point over the three weeks into the auction.

**Second construction, mixed endpoints (8/13 → 8/31 where published; UK truncated at 8/27):**
EA +18.4 > US +12.0 > **JP +11.4 (rank 3/4, below median)** > UK +8.2.

⚠️ **Both constructions agree that Japan is not leading — and that agreement is itself notable**,
because the 8/20 note found **7 one-week windows giving 7 DISTINCT orderings**, every sovereign
spanning a rank spread of 3. Two constructions agreeing is the first stability this instrument has
shown. It is two constructions, not two horizons; **do not read it as horizon-stability.**

---

## 2. 🔴 THE SCOPE DEFECT, QUANTIFIED — the bound is set by the leg that can see the LEAST

`min-across-legs` is a crude lower bound on the common component. **Its value is whichever leg moved
least — and a leg moves less, mechanically, when its endpoint stops early.** So the bound is set by
the leg with the **shortest coverage**, and everything above it is attributed to the idiosyncratic
residual of whatever leg you are grading.

On the mixed-endpoint construction:

- bound = **UK +8.2bp** — a leg that **stops 5 days before the window ends** (BoE publishes through
  8/27; 8/28 unpublished, **8/31 is a UK bank holiday**).
- Japan's implied idiosyncratic residual = 11.4 − 8.2 = **+3.2bp**.
- **Drop the stale leg** and the bound becomes JP's own +11.4 ⇒ residual = **0.0bp**.

⇒ **THE ENTIRE JAPAN-SPECIFIC RESIDUAL ON THAT CONSTRUCTION IS MANUFACTURED BY A LEG THAT CANNOT SEE
THE WINDOW'S LAST FIVE DAYS.** It is a coverage artifact, not a measurement.

🔴 **And the bias has a DIRECTION, which is the part that matters for a grade:** a lagging leg
shrinks the bound, which **inflates** the residual attributed to Japan — i.e. it pushes toward
**H2 (Japan-specific)**, the side a demand-vacuum verdict would be scored on.
`[[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]]`.

This is a **new form** of limit (d) recorded on 8/20 (*"min-across-legs is a crude LOWER BOUND, not a
factor decomposition"*). 8/20 said the bound is crude. **This says the bound is a function of
publication calendars**, and therefore moves when no yield moves at all.

**Operational rule adopted:** quote the bound ONLY off a like-for-like endpoint set, and print the
per-leg lag beside it. The tool now does both.

---

## 3. 🔴 COVERAGE VS THE EVENT — this table does NOT reach 9/1

The 9/1 synchronised selloff (US 10Y 4.80% since Jan-2025 · Bund 3.36% since Apr-2011 · UK 30Y 5.89%
since Mar-1998 · gold −2.35%, so real-rate not flight-to-quality — WALTER `SIG-W-20260901-006`) is
**outside every leg's coverage tonight**: US/EA stop **8/31**, UK stops **8/27**, JP alone reaches 9/1.

⇒ **Nothing in §1 may be quoted as a statement about 9/1.** Quoting it that way would be exactly the
*"silent truncation to square the table"* the 8/20 deliverable registration ruled out. The 9/1 read
requires a re-run no earlier than **9/2** (US/EA) and **~9/3** (UK), and the UK leg will still be the
binding constraint on any like-for-like that includes 9/1.

---

## 4. The 30Y point — because the auction being graded is a 30Y and this instrument is built at the 10Y

A stated scope limit, not a hedge: **§1 is the 10Y point.** SAM grades a **30Y**. Long-end reads:

| Window | JP 30Y | JP 10Y | JP 30s10s | US 30Y |
|---|---:|---:|---:|---:|
| 8/13 → 8/27 | +3.6bp | +2.4bp | **+1.2bp** | −2.0bp |
| 8/13 → 9/1 | +12.9bp | +11.4bp | **+1.5bp** | +4.0bp *(8/31)* |
| **8/26 → 9/1** | **+9.2bp** | +9.5bp | **−0.3bp** | +7.0bp *(8/31)* |

🔑 **JP 30s10s is FLAT-TO-TRIVIAL on all three windows (−0.3 to +1.5bp).** SAM's own frozen
instrument reads 30Y−2Y at **−1.6bp vs a ±15bp bar**. **Two different curve segments, the same
answer: a violent selloff that is still a near-parallel shift.** A term-premium/demand-vacuum event
should steepen the long end against the front; **neither segment shows it.**

⚠️ **How much independence that agreement actually carries, stated so it cannot be laundered
downstream** (`[[finding_crosscheck_with_free_parameter_validates_nothing]]`, `KB-BND-159`):
my JP legs and SAM's come from **the same MOF primary**. My **8/26→9/1 JP 30Y +9.2bp reproduces
SAM's +9.2bp exactly** — that verifies **the FETCH on both sides** (no transcription slip, no stale
cache, no mis-keyed column) and **cannot corroborate the VALUE**: if MOF were wrong or restated we
would both be wrong identically. What **is** independent: the **construction** (cross-sectional rank
vs own-curve slope), the **segment** (30s10s vs 30s2s), and my **US/EA/UK legs**, which SAM's
instrument does not touch at all.

---

## 5. What this does and does not say

- ✅ **At the 10Y point, over 8/13→8/27 like-for-like, Japan moved LEAST of four DM sovereigns.**
- ✅ **At the 30Y point, Japan's own curve barely changed shape** across three windows including the
  9/1 selloff — corroborating SAM's front-led read at a different segment.
- ❌ **It does not grade the 9/3 auction.** That is SAM's, on SAM's frozen terms.
- ❌ **It does not reach 9/1**, and must not be quoted as if it did.
- ❌ **It is not a factor decomposition.** A true PC1 on n=4 would be dominated by the US — the very
  leg being netted out.

**No threshold is registered here and none is proposed.** SAM ruled on 8/27 against registering a new
instrument inside an open window, and that ruling is right; this is an **INPUT to attribution**, which
is exactly the weight SAM asked for it to carry.
