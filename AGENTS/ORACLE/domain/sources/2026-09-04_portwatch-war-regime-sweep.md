# ORACLE — PortWatch war-regime sweep (PROME's 2026-08-17 ask, run on the 6th carry)

**Author:** ORACLE · **Date:** 2026-09-04 · **Box:** desktop
**Requested by:** PROME 2026-08-17, routing BRENT's measured impeachment of IMF PortWatch Hormuz `chokepoint6` completeness. Carried unworked for 18 days across five sessions; run today at Will's direction.
**Status of the underlying impeachment:** BRENT's, **hardened since the ask** — see §1.

---

## 0. BOTTOM LINE

**Every Hormuz transit market ORACLE tracks resolves *exclusively* on the IMF PortWatch print. The impeachment therefore does not make these markets wrong — it makes them a different object than I have been routing.**

- The markets are **valid forecasts of what PortWatch will publish.** They are **not** throughput reads, and I have been routing them as throughput reads to HAWK/BRENT/FALCON since ~7/17.
- **PROME's framing needs one correction, and it is the most useful thing this sweep returns:** the packet said the ~88/day denominator "is pre-crisis vintage and looks unaffected." True in isolation, **misleading in use** — *a clean denominator over a defective numerator is still a defective ratio.*
- **I am correcting my own work from this morning**, six hours old, in the same session that published it.

---

## 1. The impeachment has hardened since 8/17 — three independent legs, not one

I checked BRENT's current state rather than working from the 8/17 packet, because an 18-day-old relay of someone else's finding is exactly the thing that goes stale.

| leg | what it is | source |
|---|---|---|
| **① internal contradiction** | `n_tanker > 0` AND `capacity_tanker = 0` on **0 of 424 pre-crisis days** vs **19 of 113 war-regime tanker-days (16.8%)** | BRENT, measured at the FeatureServer 8/17 |
| **② external vendor** | a third-party AIS vendor puts **~58% of a week's Hormuz transits DARK** | `SIG-W-20260817-004`, reached independently, BRENT board_log **8/20** |
| **③ failed known-positive control** | at a second port (FALCON, 8/20) | BRENT board_log 8/20 |

⚠️ **The control BRENT specified in the 8/17 packet was run and CLOSED AS UNDERPOWERED, not as a pass.** Own pull 8/12–8/16 showed `n_tanker` 1·2·2·1·1 and max `capacity_tanker` 78,587 dwt — **no VLCC-class (≥250k dwt) signature anywhere** while ≥3 VLCCs loaded — **but "loaded at Ju'aymah" ≠ "transited Hormuz in-window", so it cannot bind.** Re-specified on a clean known positive (*Sidr*, *Senegal Prosperity*), mirrored to a 2026-09-08 forward check. **So the cause is still a hypothesis; only the defect is measured.**

⚠️ **Undercount factor: NOT QUANTIFIED.** BRENT says so explicitly. **I add no number to it**, and nothing below depends on one.

---

## 2. LEG 2 OF THE ASK, TAKEN FIRST — because it decides Leg 1

PROME asked me to *"record the venue's actual resolution source on the row — that fact decides whether the 24.1% is information or instrument noise."* Read directly from the Polymarket resolution text on **2026-09-04**:

| market (ORACLE pin) | resolves on |
|---|---|
| **Hormuz normal by Dec 31** — $10.4M, my deepest leg | *"resolve YES if **IMF Portwatch publishes** a 7-day moving average of transit calls … **equal to or above 60**"* |
| Hormuz avg-daily transits end-Sep | *"the **finalized 7-day moving average** of transit calls ('Arrivals of Ships') … that **IMF Portwatch reports** for September 30"* |
| Hormuz ships-transit weekly (wk 8/31) | *"the total number of transit calls that **IMF Portwatch reports** … Aug 31 – Sep 6"*, source URL `portwatch.imf.org/pages/cb5856222a5b4105adc6ee7e880a1730` |
| Hormuz ships-any-day ladder by Sep 30 | same family, same clauses |
| **Hormuz 0-ships closure (by-date)** | *"resolve to 'Yes' if **IMF PortWatch publishes** a daily number of transit calls … **equal to 0** for any date"* |

**Two clauses appear in all of them and they are decisive:**

> **(a)** *"Ships not reported by IMF Portwatch will not be considered."*
> **(b)** *"Data integrity issues … **do not include cases where IMF Portwatch differs from alternative sources**."*

⇒ **The contract cannot be reopened on a divergence from AIS, satellite or vendor data. PortWatch *is* the definition.** The market therefore **cannot be wrong about PortWatch**; it can only be **misread as being about ships**.

### 2a. The 0-ships leg is the sharpest case, and PROME's question has a clean answer

It resolves YES on **a PortWatch *print* of zero**, not on an actual zero. In a regime where PortWatch is impeached for coverage, **a detection failure and a real stoppage resolve this market identically.** BRENT's own *"7/23 first zero-transit day"* headline was self-flagged as possibly artefactual — that is precisely this event.

> **Answer to "information or instrument noise?": on this contract the two are not separable.** Not "it is noise" — *the contract has no clause that could ever tell them apart.*

### 2b. Three nested readings of that one row, each weaker, each pass thinking it was finished

| pass | reading | what it sounds like |
|---|---|---|
| the **NAME** | "0-ships closure / full stoppage" | a blockade |
| the **CRITERION** — corrected 2026-08-09 | one calendar day with zero transits | a throughput **floor** |
| the **RESOLUTION SOURCE** — corrected **today** | one calendar day on which **PortWatch publishes** zero | a **detection-failure** floor |

**The 8/09 pass explicitly congratulated itself for reading the criterion instead of the name — and still stopped one layer short.** ⇒ *read the resolution source, not only the criterion.*

---

## 3. LEG 1 — the classification

### 🔴 `PORTWATCH-WAR-REGIME-SUSPECT` (valid as print-forecasts, **not** as throughput reads)
`KB-ORC-063` · `KB-ORC-067` · `KB-ORC-072` · `KB-ORC-078` · and **all five live Hormuz pins**. `KB-ORC-063` and `KB-ORC-067` moved to `Status = CORRECTED` (their claims were framed as throughput). Tags written into `workbook/KB.tsv`; resolution sources written beside each pin in `watchlist.tsv`.

### ✅ CLEARED — no PortWatch exposure
- **WTI-$100 (the supply leg)** — a **price** market. Zero exposure.
- **Iran-shipping attack legs** — attack events, not transit counts.

### ⚠️ `KB-ORC-038` (the ~88/day denominator) — CLEARS AS A LEVEL, DOES NOT CLEAR IN USE
Pre-crisis vintage, the exact window with 0 of 424 contradiction days. **So the level clears — and PROME's instruction to "clear pre-crisis-denominator-only uses" is right as far as it goes.**

**But there is no such thing as a denominator-only use.** Every *"x% of normal"* figure I have published divides a **war-regime** PortWatch count by a **pre-crisis** PortWatch baseline. That is a **cross-regime ratio on an instrument whose coverage changed between the two regimes** — which is exactly the break BRENT measured. **The denominator clearing does not clear the ratio, and the ratio is what consumers read.**

---

## 4. ⛔ Self-correction, same day, to work I routed six hours ago

This morning's `KB-ORC-078`, `STATUS.md` and the HAWK/BRENT/FALCON packet all said:

> *"~84% of the mass BELOW 10 transits/day against a ~88/day pre-crisis baseline"*

**The mass figure is correct. The comparison is not** — it is the cross-regime ratio of §3.

> ✅ **Correct statement: "the crowd expects PortWatch to keep printing 0–10 transits/day."**
> ⛔ **Not:** "the strait is running at ~10% of normal."

The second is a claim about the world that my instrument cannot support. A correction packet goes to HAWK today.

---

## 5. The derived series I log every session is affected, and the bias points the comfortable way

`tools/disruption_supply_spread.py` defines its disruption leg as **`1 − P(normal by Dec 31)`**. Per §2 that is **`1 − P(PortWatch prints a 7dMA ≥ 60)`** — **not** "P(disruption persists)", which is what the tool's docstring, its runtime output and every logged `disruption_label` have said since v2.

- **If PortWatch undercounts, `P(print ≥ 60)` is LOWER than `P(actual normalisation)`** ⇒ the disruption leg reads **HIGH** ⇒ **the spread reads WIDE**.
- **A wide spread is the *reassuring* reading** — "premium, not shortage." ⇒ **the bias favours the comfortable answer**, which is the direction nobody files a complaint about.
- ⚠️ **Asymmetry worth knowing:** the **supply** leg is a price market with **zero** PortWatch exposure. **The two legs of this spread rest on different epistemic bases and only one is impeached.**

**Fixed today:** the label, in the docstring, the runtime output (with an inline warning) and the `disruption_label` column. **NOT changed:** the arithmetic, the slug, the regime. **No regime bump** — the series stays chartable across today, because nothing about the data changed. Verified by `--dry-run`: `73.5 − 28.0 = +45.5pp`, identical to the morning's logged row.

---

## 6. What I am NOT claiming

- **I do not quantify the undercount.** BRENT states it is unquantified; I add nothing.
- **I do not adopt the relayed ~59/day Goldman figure as a level.** It is three relay hops (Goldman → Bloomberg → WALTER SIG `-024` → BRENT), and **BRENT itself declines it**, saying *"I hold no throughput instrument."* I hold less than BRENT does here.
- **I do not assert the strait is busier than the crowd thinks.** Only that **my instrument cannot see the difference** — which is a statement about ORACLE, not about Hormuz.
- **Nothing here fires, unfires or moves a threshold.** `VX-ORC-04` stays 🟠; what changed is the description of what it measures.

---

## 7. Reproduce

```
cd "$(git rev-parse --show-toplevel)/AGENTS/ORACLE"
python3 - <<'PY'
import sys; sys.path.insert(0,"scripts"); import polymarket as P
for s in ["strait-of-hormuz-traffic-returns-to-normal-by-december-31",
          "will-there-be-between-0-and-5-average-daily-transits-of-the-strait-of-hormuz-on-september-30",
          "will-20-39-ships-transit-the-strait-of-hormuz-between-august-31-september-6"]:
    print(s, "\n  ", P._get("/markets",{"slug":s})[0]["description"][:400], "\n")
PY
python3 tools/disruption_supply_spread.py --dry-run   # label corrected, arithmetic unchanged
```
Impeachment source (BRENT's, not mine): `AGENTS/BRENT/setups/2026-08-17_petroline-ras-tanura-discriminator.md`; corroboration `AGENTS/BRENT/board_log.tsv` 2026-08-20.
