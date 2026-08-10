# GATE-FALCON-001 leg-2 — like-for-like adjudication on the REGISTERED basis (TankerMap)

**FALCON · 2026-08-10 · pull times stamped per figure · WATCH-ONLY, no state change, no mark moved**
**Task:** PROME/Will GO, Task 1 — attempt the like-for-like leg-2 grade on the registered basis before any PortWatch re-key.
**Branch reached: (a) TankerMap RETRIEVABLE and a like-for-like read WAS obtained — and it also produces branch (c)'s finding.**

---

## 1. VERDICT

> ## 🟢 **LEG-2 DOES NOT FIRE.** On the registered source, on the registered metric, read as the registered condition intends, the most recent direction is a **sharp RECOVERY, not a step-down.**
>
> **And the PortWatch substitution I declined this afternoon would have fired it — wrongly, on an 8-day-stale series, at the exact moment the live registered source was recording a +200% week-over-week rebound.**

**Proposed mark consequences: NONE.** Leg-2 stays **NOT FIRED**. No convergence move (Bab al-Mandab vector is already at 5/ceiling). No scenario re-mark. Marks stand at **B 5 / C 35 / D 60 · 43/50 · P 23 / K 15 / R 13**. Will rules; I am proposing nothing.

---

## 2. THE LIKE-FOR-LIKE READ

**Registered basis, quoted exactly from `PROME/GATES.tsv` row 24:** *"(2) fresh Bab transit step-down below the ~8/day baseline **[TankerMap 7/21]** sustained >=2 print-days."*

| | Registration pull | Today's pull |
|---|---|---|
| **Source** | TankerMap | TankerMap — `tankermap.com/analytics/straits/bab-el-mandeb` |
| **Pull time** | **2026-07-21** (my archived record, `reports/2026-07-21_babelmandeb-SIG-003-adjudication.md`) | **2026-08-10**, page data-stamp **16:41 UTC** |
| **7-day average** | **5.0 tankers/day** | **3.9 tankers/day** |
| **Week-over-week** | **−3% w/w** (flat) | **🔴 +200% vs prev 7d** |
| **Contemporaneous characterisation** | *"holding up despite escalating regional tensions"* | Sharp rebound off a very low prior week |

**Stated methodology (today's pull, verbatim):** *"Estimate from tanker DWT; LNG excluded; not measured cargo flow."* AIS-based, updated hourly. Crude and chemical/oil product tankers tracked.

**Reading the condition as registered.** The leg requires a ***fresh step-down***, and my own origin report is explicit about why that word is load-bearing: *"the baseline is already depressed post-2023, so the tell is a **fresh step-down, not the standing low**."* **The 7-day average moved 5.0 → 3.9 over twenty days, but the current direction is +200% w/w — the series is recovering hard, not stepping down.** There is no fresh step-down to grade, and therefore no ≥2-print-day sustain to test.

⚠️ **Volatility caveat, stated because the numbers are small:** a 7-day average of 3.9/day means a +200% w/w implies a prior week near ~1.3/day. At these magnitudes single-vessel changes move the percentage violently. **I am reporting the direction, not treating +200% as a precision figure.** The negative verdict does not depend on the magnitude — it depends on the sign, and the sign is up.

---

## 3. 🔴 THE SECOND FINDING — branch (c) also holds, and it is inside a GATE spec

**The `~8/day` in the registered wording is not a measured baseline. It is an estimate, and the contemporaneous measured value was 5.0.**

My archived 7/21 record reads: *"Bab el-Mandeb tanker transits | **~8/day est.**; 7-day avg **5.0/day**; −3% w/w… [TankerMap, 7/21 pull]"*.

⇒ **On the day the gate was written, the registered series was already running at 5.0 — below the 8 that the leg names as its floor.** A **level** reading of leg-2 (*"any 2 print-days below 8"*) was therefore **ALREADY TRUE AT REGISTRATION** and would have fired on day one. **Apply my own registered test — *would it fire on DAY ONE? then it is a descriptor, not a trigger* — and a level reading fails it outright.**

**This is the ninth instance of the already-true-at-registration family, and the first one found inside a GATE specification rather than a prediction row:** HAW-10 (locus) → HAW-14 (catalyst) → HAW-15 (mechanism) → FAL-01 (actor) → FAL-03 (molecule / event-vs-state) → FALCON casualty ordinal → HAW-18 vessel class → `VX-FALCON-SUNK-01` attacker axis → **`GATE-FALCON-001` leg-2 level-vs-delta.**

**Why it happened is recoverable and specific — two qualifiers did not survive the trip from my proposal into `GATES.tsv`.** My 7/21 origin text read: *"drop materially below the current depressed ~8/day baseline on TankerMap/Windward, **attributable to enforcement**, sustained ≥2 print-days (**the baseline is already depressed post-2023, so the tell is a fresh step-down, not the standing low**)."* The registered wording kept the single word **"fresh"** and dropped both the **attribution requirement** and the **parenthetical that explains the baseline is not a level**. **The whole delta semantics now rest on one adjective.**

**⇒ Recommendation to Will (a wording repair, NOT a threshold change — the number stays 8 and stays Will's):** restore the two dropped qualifiers to leg-2, so it reads as a step-down **from the prevailing 7-day average, attributable to enforcement**, sustained ≥2 print-days — rather than a level cross of a figure the series was already beneath at registration. **This does not move the bar; it restores the bar's meaning.**

---

## 4. 🔴 THE PORTWATCH SUBSTITUTION IS NOT MERELY IMPROPER — IT IS NUMERICALLY INVALID

I proposed this morning that Will might re-key the leg's basis to PortWatch `chokepoint4`. **Today's like-for-like pull kills that option on the evidence, and I am withdrawing my own option (b) recommendation.**

| Window | **TankerMap** (registered source) | **PortWatch `chokepoint4`** |
|---|---|---|
| Pre-blockade / registration week | **5.0/day** (7dma, 7/21) | **13.0/day** (median, Jun 1 – Jul 19) |
| Blockade window | **3.9/day** (7dma, 8/10) | **7.0/day** (median, Jul 20 – Aug 2) |

**The two sources differ by roughly 2–2.6× on the same object over overlapping periods.** They are not two measurements of one quantity; they are two different quantities. **"8/day" means something materially different in each series, so porting the number across sources would silently redefine the condition.** This is the same class as the leg-3 traps I rejected — Kpler's Bab *transits* read as Yanbu *loadings*, AGBI's 4.7 *total-liquids* read as crude — and it is the reason the basis discipline held this afternoon was worth holding.

**PortWatch also lags ~8 days** (its newest print is 8/2). **A PortWatch-based fire today would have been struck off a stale window while the live registered source recorded a rebound.** That is the concrete cost the discipline avoided.

**PortWatch `chokepoint4` remains genuinely useful — as a lagging corroborator with 2,771 days of history back to 2019, which TankerMap's live view does not give me.** My 7/21 memo to PROME already recommended exactly this split: *"lean on real-time AIS as the leading read, with PortWatch as lagging confirmation."* **That recommendation was right and I had stopped acting on it. Proposal: run both, labelled by role, never one substituted for the other.**

---

## 5. CORRECTION OWED — to OSPREY and HAWK

In all three of today's forum posts I stated that leg-2 *"has never been gradeable"* because *"only total-vessel Bab data exists."* **That was an unchecked negative and it was wrong twice over:** PortWatch carries tanker-specific Bab transits, and the registered source **TankerMap is live and publishes the exact registered metric.** The leg was gradeable throughout; I had not looked. **Correction owed, and it belongs with the other outward corrections PROME is routing.**

---

## 6. WHAT WOULD CHANGE THIS VERDICT

- A **fresh step-down on TankerMap's 7-day average, sustained ≥2 print-days, attributable to enforcement** — the registered condition, correctly read. Today's direction is the opposite.
- A **UKMTO/Ambrey/JMIC-confirmed enforcement attack** would fire **leg-1**, which is already fired (7/23) and does not need leg-2.
- ⚠️ **Convoying from the 8/12–13 coalition meeting would contaminate this leg exactly as I pre-registered this morning** — a transit recovery under escort is capacity-priced, not threat-priced. **Today's +200% rebound is *pre*-meeting and therefore not yet convoy-contaminated, which makes it a clean baseline reading to hold against next week's.**

---

*Watch-only. No threshold, mark, gate state or ledger row moved. Registered numbers and baselines untouched — those are Will's. Figures stamped with source and pull time per live-data rules.*
