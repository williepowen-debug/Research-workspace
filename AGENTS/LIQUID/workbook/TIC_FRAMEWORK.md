# TIC Data Analysis Framework
*Reusable reference for monthly TIC releases*

**Rewritten 2026-08-23** (LIQUID boot) on ZHAO's 8/21 June-TIC packets — two of them, both Will-ruled: the **Belgium-proxy falsification** and the **China-rotation WITHDRAWAL**. Prior version (2026-03-20 vintage, extracted from a Mar-19 STATUS analysis) is superseded. Records: KB-ZHAO-119..124 · KB-ZHAO-127 · VX-ZHAO-1.09/1.10.

---

## ⛔ RULE ZERO — read this before any other row in this file

> **A TIC holdings LEVEL change is NOT a flow. Never quote one as selling.**

The wedge between the two is valuation, it is **large**, and **it flips sign inside a single release**:

| June 2026 TIC | level Δ | net SALES | valuation wedge |
|---|---:|---:|---|
| Total foreign holdings | **−$72.1B** | **−$22.3B** | ≈ **−$49.8B** (prices FELL → level overstates selling ~3x) |
| China, trailing 12m | −$98.0B | **−$122.3B** | ≈ **+$24.3B** (prices ROSE → level UNDERstates selling ~25%) |
| China, all LT US securities TTM | −$11.6B | **−$118.9B** | ≈ **+$107.3B** (markets added back ~$107B) |

**Both directions, one dataset.** ⇒ Any threshold in this file keyed to a *level* or a *level change* is measuring an unknown mixture of flow and price. **Use Table 3 / Table 1 net-transaction lines. If you only have the level, say so and say which way the wedge runs.**

⚠️ **Pre-registered, because it is reflexive and DGS30 sits at a 19-year high:** in a bond selloff the wedge **inverts and amplifies** — the same flow rate prints as a much larger holdings decline, and the TIC headline suddenly reads like a run. **A scary TIC level print arriving with rising yields is the expected artifact, not evidence.** Grade it on flows or not at all.

**Perimeter discipline (ZHAO):** two correct China TTM figures exist — **−$122.3B** (all Treasuries incl. bills, Table 3) and **−$91.3B** (coupons only; Table 1 is long-term). They reconcile to the dollar. **Say which one you mean.**

---

## Key Focal Points Each Release

### 1. Official vs Non-Official — ★ read this cut FIRST, it is the load-bearing one
June 2026: **Foreign Official −$45.40B · Foreign Non-Official +$23.15B · Grand Total −$22.25B.**

**The private bid is absorbing official supply.** That is a different market structure from "nobody is buying," and it is the cut that actually speaks to the demand-hole leg of THESIS v2. → **KB-LIQ-095** for what it means and why it moves the detection instrument. **Do not report the Grand Total without the split** — the aggregate nets two opposite behaviours by two classes of holder with opposite price-sensitivity.

### 2. 🔴 Belgium — the >$500B row survives as a LEVEL alert; the MIGRATION INFERENCE is FALSIFIED
**Do NOT read Belgium-up/China-down as custody migration.** ZHAO tested the rule instead of applying it (n=41, 2023-02→2026-06):

| Window | rho(China net sales, Belgium net sales) |
|---|---:|
| Full n=41 | **+0.050** |
| Last 12m | −0.040 |
| Last 24m | +0.023 |
| Last 36m | +0.005 |

**Zero on every window — a custody mirror requires strong NEGATIVE correlation.** Base rate: of the **27 months China was a net seller, Belgium bought in 15 (56%) — a coin flip.** June looked like a textbook mirror (China −$21.96B, Belgium +$17.56B to an all-time-high $482.5B) and is not one: both legs were simply large that month (each 4th-largest of 41 in its direction). **Two big independent moves in opposite directions look like a mirror and aren't.**

- **Honest limit (ZHAO's, carried):** this refutes *systematic monthly mirroring*, **not** the existence of an episodic migration channel — lumpy real events dilute in a full-sample correlation. The operational claim is the narrow one: **a single month's China-down/Belgium-up cannot be read as migration.**
- **Reinstatement band:** restore the migration reading only if **rho < −0.5 on rolling 24m** (VX-ZHAO-1.09).
- ⚠️ **The $500B tripwire STILL FIRES to SAM/PROME 🟠 — but on a bare level, with no inference attached.** Belgium is **$482.5B [Jun-26], an all-time high, $17.5B from the line.** Live and near. If it crosses, report it as *a large concentrated custody position in a small jurisdiction*, and **do not attach "China stealth exit"** — that inference is what was falsified.
- **Dead numbers retired from this file:** *"true China exposure ~$2.5–2.8T via Belgium/Euroclear"* (2026-02 research vintage, ~4x the entire Belgium line) and the *Belgium+China combined −$100B/qtr RED threshold* — both were built on the mirror identity. Historical copies in `domain/sources/research_foundations_20260125/` are **archival, not current**.

### 3. Japan
Largest holder (~$1.1T). **Composition decides the read, not the total.** June: **−$26.86B total but ST/bills −$23.11B vs LT only −$3.75B** = a **bill roll-off, not duration selling** — second such month (May ST −$59.79B). Composition-distinct from China's.
- Trigger: **>$20B net single-month UST sell** = MARCO/SAM signal — ⚠️ **now qualified: LT/coupon basis, not total.** A bills roll-off can clear $20B on its own and means something different. *(Anchor: top of the Feb-2026 FY-Q4 peak-repatriation estimate $13–22B UST-specific/month, KB-LIQ-031 — a peak-run-rate anchor, not a computed SD.)*
- SAM owns Japan; this row is for routing, not adjudication.

### 4. China
**$633.4B [Jun-26] — series low, rank 1 of 78 months (2020-01 on). ~85% of the level drop is transacted (−$21.96B), ~15% price** — China is the *exception* to Rule Zero this month, which is exactly why the split has to be checked rather than assumed.
- **June is the FIRST month this cycle China sold duration in size: LT/coupon −$15.77B** (May: −$0.13B, flat).
- **Live thresholds:** ZHAO's `<$650B` route to LIQUID 🟠 — **BREACHED June.** ZHAO's `>$50B sold in a single quarter` 🔴 route — **NOT tripped** (Q2-26 = +$1.2B / +$5.9B / −$22.0B = **−$14.8B**). *Stated so nobody upgrades on the headline.*
- ⛔ **Retired as dead:** *"~$750–780B range"* and *"any drop below $750B = meaningful escalation"* — crossed long ago; a threshold already behind the tape can never fire and reads as quiet.
- 🔴 **The rotation mechanism is WITHDRAWN, not weakened** (ZHAO 8/21, Will-ruled). Rotation predicts Agency holdings RISE as Treasuries fall. TTM: Treasuries −$91.3B **and Agency −$40.3B — both SOLD**; rho = −0.025 (n=41); June sold both. **China is not rotating; it is selling both.** Aggregate exposure is roughly flat only because **markets added back ~$107.3B** ⇒ that support is **conditional on markets rising, not structural.** Off-SAFE entity-shifting is **demoted to *possible*, not *evidence*** — TIC attributes by custodian/country, never by Chinese owning entity, so it is untestable from these lines.

### 5. Korea (context for SAM/LIQUID)
June **+$2.70B bought — first net-buying month in five**, LT flat. **The Asian anchors DIVERGED.** ⚠️ Table 3 is all-residents with no official/private split (VX-ZHAO-2.07).

### 6. Gulf States (Saudi, UAE, Qatar, Kuwait)
Below fiscal breakeven (~$80/bbl) even before war premium. Selling in *calm baseline* months = structural fiscal position rather than war disruption. HAWK/BRENT own the oil side.

### 7. Total Foreign Holdings
⛔ **The old row — *"aggregate decline >$50B MoM = demand-hole thesis gaining hard data"* — is RETIRED as a live trigger, and June is why: it fell $72.1B and would have FIRED, on $22.3B of actual selling.** It was a Rule Zero violation that would have manufactured a demand-hole confirmation out of a price move.
- **Replacement:** **net SALES** (Table 3 grand total) **< −$50B in a month**, reported **with the official/non-official split**. June = **−$22.3B ⇒ NOT fired.**

---

## Interpretation Frame
- TIC = a **~6-week-lagged snapshot** of the past month. The market interprets forward; the release is a check on a read you already hold, not a new one.
- Contrast between TIC (lagged) and **current auction demand** is the signal — ⚠️ but see KB-LIQ-095: **auction indirect % is composition-blind**, so it can stay strong *through* an official→private handoff. Strong indirect is not evidence that official demand held.
- Weak TIC flows **+** weak auction BTC = **secular** foreign-demand deterioration.
- Strong TIC flows **+** weak auction = event-specific disruption (more recoverable).

---
*Prior version source: STATUS.md Mar 19 analysis, extracted 2026-03-20. Rewritten 2026-08-23 — see header. Next scheduled arbiter for continued China duration selling: **July TIC, ~2026-09-16**.*
