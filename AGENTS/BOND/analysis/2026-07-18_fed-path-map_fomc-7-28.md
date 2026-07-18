# Fed-Path Pricing Map — FOMC 7/28-29 · the arm's falsifier, quantified
**Author:** BOND · **Date:** 2026-07-18 (Sat eve, PROME-spawned; markets closed) · **Purpose:** convert the corrected TRY-FIRE-004 falsifier ("real-rate / higher-for-longer policy-path channel falsifies on a dovish Fed repricing") from an assertion into **pre-registered, numbered thresholds** — plus the Will-facing "arm-eligible re-fire day" rule for the banked $500.

> **Data vintage — all [as-of] stamped; markets closed Sat 7/18.** FRED obs 7/16; CME FedWatch pull 7/16 (via web 7/18); Fedspeak window 7/16-17 (last before blackout 7/18-30).

---

## 1. Where the Fed-path market actually sits [as-of]

| Datum | Value | Source / obs |
|---|---:|---|
| Fed target range | **3.50–3.75%** | FRED DFEDTARU/DFEDTARL, 7/16 |
| EFFR (effective) | **3.63%** | FRED EFFR, 7/16 |
| 3M (DGS3MO) | 3.84% | FRED, 7/16 |
| 1Y (DGS1) | 3.99% | FRED, 7/16 |
| **2Y (DGS2)** | **4.16%** | FRED, 7/16 |
| 10Y real (DFII10) | 2.35% | FRED, 7/16 |
| 10Y (DGS10) | 4.57% | FRED, 7/16 |
| FedWatch 7/28-29 HOLD | **~90%** | CME FedWatch, 7/16 (hike odds collapsed from 46.5% [7/13 post-CPI] after cool CPI+PPI) |

### The single most important fact for the arm
**The front-end curve is UPWARD-sloping above the funds rate: 3M 3.84 → 1Y 3.99 → 2Y 4.16, all *above* EFFR 3.63.** The 2Y sits **+53bp over the funds rate.** A market pricing cuts would put the 2Y *below* funds; the 2Y at +53bp prices **no near cuts, higher-for-longer, with residual hike risk.** *That upward-sloping front end IS the arm* — it is the market's real-policy-path expectation, and it is exactly what my 7/18 relabel identified as the arm's true driver (policy path, not term premium). The arm lives here, in the 2Y-vs-funds gap — **not** in the 30Y term premium.

**Corollary:** the arm's fate at the 7/28-29 FOMC rides on the **guidance tone, not the rate decision.** The hold is ~90% priced — a hold is a non-event. What moves the arm is whether the statement + presser keep the higher-for-longer premium in the front end (hawkish-hold → arm LIT) or collapse it (dovish-hold → arm FALSIFIED).

---

## 2. Pre-registered arm thresholds (FROZEN 7/18 — grade the reaction against these, don't re-derive)

Three legs must agree; the **2Y is the lead gauge** (policy-path proxy), DFII10 the real-rate confirmer, 10Y the level.

| State | 2Y (DGS2) | DFII10 | 10Y (DGS10) | Fed-path read | **Arm verdict** |
|---|---|---|---|---|---|
| **SUPER-CHARGED** | ≥ 4.30 | ≥ 2.45 | ≥ 4.65 | hike back on the table / hawkish surprise | arm ESCALATES → DFII10 2.5 re-arm watch; possible add-gate |
| **LIT (base/modal)** | 4.00 – 4.30 | 2.25 – 2.45 | 4.50 – 4.65 | higher-for-longer hold, no near cuts priced | **arm CONFIRMED — TLT puts HOLD** |
| **WATCH (eroding)** | 3.85 – 4.00 | 2.15 – 2.25 | 4.35 – 4.50 | higher-for-longer premium compressing | arm SOFTENING — not broken; tighten watch |
| **BREAKS (falsifier)** | **< 3.85 sustained** | **< 2.15 sustained** | **< 4.35 sustained 3 sess** | dovish repricing — cuts back on the table | **arm FALSIFIED → re-evaluate the duration short** |
| **THESIS KILL** | < 3.63 (below funds) | < 2.00 | < 4.15 sustained 3 sess | market prices next move = a CUT | **EXIT** (per THESIS exit rules) |

**Current read [7/16]: 2Y 4.16 / DFII10 2.35 / 10Y 4.57 = squarely LIT.** The arm is confirmed and mid-range; ~15bp of DFII10 headroom to the 2.5 re-arm, ~20bp of 2Y cushion to the WATCH line.

### FOMC 7/28-29 outcome → arm mapping (no SEP; statement + presser only)
- **Hawkish-hold (modal, arm LIT):** holds 3.50-3.75, retains higher-for-longer language, presser pushes back on cut timing, no dovish dissent. Front-end holds ≥4.00. → arm confirmed.
- **Dovish-hold (THE falsifier event):** holds *but* softens — acknowledges labor cooling, opens the door to cuts, or a dovish dissent. Front-end reprices sub-3.85, DFII10 sub-2.15. → **this specific event fires the arm falsifier** (not an oil retrace — the relabel's whole point).
- **Hawkish surprise / hike (arm super-charges):** Waller's conditional-hike door (7/13) isn't fully shut; a hike or explicitly hawkish hold spikes the 2Y toward 4.30+, DFII10 toward 2.5. → arm escalates.
- **Watch window:** the 2Y move in the 2 min after the statement + the presser tone. July CPI lands ~8/13 = **post-FOMC** → the Fed meets seeing the shock, not the data → structurally favors the hawkish-hold (keeps the front-end premium bid).

---

## 3. ★ Will-facing: the "arm-eligible re-fire day" for the banked $500

The re-fire adds to TLT puts (a duration short). **Two gates, both must be true:**

**Gate A — Arm eligible (BOND signal, my domain):** the arm must be **LIT or SUPER-CHARGED** — 2Y ≥ 4.00 AND DFII10 ≥ 2.25 AND 10Y ≥ 4.50, falsifier NOT firing. *If the falsifier is firing (§2 BREAKS row), do NOT re-fire, regardless of the day's color.*

**Gate B — Entry-day timing (rule #6, TERRY-owned — flagged):** rule #6 = "puts on green days." For a TLT **put**, a "green day" = **TLT UP = yields DOWN**. So the rule-#6-consistent re-fire is on a **TLT-green / yields-down session** — buy the put into a bond *rally* (cheap premium, not chasing a selloff).

> **⚠️ Discrepancy flagged for TERRY/PROME — the HEARTBEAT "red-day entry only" phrasing needs disambiguation.** For a TLT put, buying on a TLT-*red* day (bonds selling off, yields up) is *chasing* — the opposite of rule #6's intent. The phrase likely means an **equity red / risk-off day**, which *classically* coincides with a bond rally (TLT green) — consistent with rule #6. **BUT the arm's own regime breaks that assumption:** a real-yield/higher-for-longer shock is exactly when stock-bond correlation flips **positive** — equities AND bonds sell off together, so an "equity-red day" = a "TLT-red day" too, and buying TLT puts then *chases*. **BOND recommendation (rate-grounded, sidesteps the equity proxy): re-fire the $500 on a day TLT is GREEN (yields down intraday) while Gate A holds** — rule-#6-consistent and arm-disciplined. Final rule-#6 call is TERRY's; this is the signal-side input.

**One-line decision rule for Will:**
> Re-fire the banked $500 **only when** the rates arm is LIT (2Y ≥ 4.00, DFII10 ≥ 2.25, 10Y ≥ 4.50 — falsifier not firing) **AND** TLT is green on the day (yields down — buy the dip in premium, don't chase a selloff). **Skip the re-fire if the arm has flipped to WATCH/BREAKS** — a dovish-Fed repricing is the kill, and you don't add into a falsifying tape.

---

## 4. What this sharpens
- The relabel's falsifier is now a **number, not a vibe**: 2Y < 3.85 / DFII10 < 2.15 / 10Y < 4.35 sustained = arm broken. Feeds NEXUS_BRIEF (falsifier surface) + STATUS exit rules.
- The FOMC is re-cast correctly: **the hold is priced; the guidance tone is the event.** A dovish-hold is the specific falsifier trigger — the first real test of the corrected label.
- The $500 re-fire gets a two-gate rule that resolves the "red-day" ambiguity in the arm's own (positive-correlation) regime.

**Sources:** FRED (DFEDTARU/DFEDTARL/EFFR/DGS3MO/DGS1/DGS2/DFII10/DGS10, obs 7/16); [CME FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html) (7/16); [CNBC 7/13 hike-odds](https://www.cnbc.com/2026/07/13/-a-july-rate-hike-from-the-fed-the-odds-are-rising.html).
