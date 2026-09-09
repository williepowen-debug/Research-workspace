# CASUALTY RATCHET — the instrument that replaces retired D-indicator #5

**Built:** 2026-09-08 ~23:3x ET. **Approved:** Will 2026-08-17 (spec batch item ①), as the replacement for D-indicator #5 (*"a SECOND fatality"*), which was **retired as written on 2026-08-10** because it was already satisfied at registration (the Mombasa B seafarer, 7/14, preceded the Kuwait worker, 7/30). **22 days late** — LESSONS FAL-08 is the post-mortem; three live demands arrived in the interval (Tihamah 8/11, Sirik 9/1-9/6, the 73 Saudi injured 9/8). **Owner:** FALCON. **Ledger:** `domain/casualties/CASUALTIES.tsv`. **Registered as:** `VX-FALCON-CASUALTY-01` (an INDICATOR feeding `EXIT_PROTOCOL.md` §3 #5 — NOT a mark trip; the only casualty event that moves a mark is the D→85 rung's trigger (d), a US service member killed on/after 2026-09-08, which this instrument feeds and does not duplicate).

## 1. Why a rate and a class, not an ordinal
*"A second fatality"* failed because an ordinal has no memory: it was true before it was written, and it can only ever be re-cut to "a third." The mechanism the tell was written for is real — **a casualty is what converts an intercepted-salvo exchange into a casualty-driven one** — but it has two faces: **WHO** died (a US soldier moves Washington; a GCC civilian moves Riyadh/Kuwait; an Iranian civilian killed by a US munition moves Tehran — Qalibaf's *"the era of proportionate responses has come to an end"* came after Sirik) and **HOW FAST** the count is growing. So the instrument carries a **class-step** and a **rate-step**, both computable from the ledger, neither re-derivable by hand.

## 2. Bands (STRICT: level · instrument · window · revision)
| Band | Condition | Instrument / window |
|---|---|---|
| 🔴 **RED — CLASS-STEP** | First CONFIRMED fatality in the post-MOU cycle (2026-06-27 →) in a class with NONE since 6/27: **MILITARY_US** [= D→85 trigger (d), on/after 9/8], **MILITARY_GCC**, **MILITARY_COALITION** | `CASUALTIES.tsv`, class column; graded at each session |
| 🔴 **RED — RATE-STEP** | Rolling 30-day confirmed-killed (all in-scope classes) **≥ 2× the preceding 30 days AND ≥ 5** | `CASUALTIES.tsv` killed column; two adjacent 30-day windows ending at the session date |
| 🟠 **ORANGE** | (i) rolling 30-day confirmed-injured ≥ 2× prior AND ≥ 20; **or** (ii) a mass-casualty event (≥ 5 killed) attributed to a US munition by a named third-party assessment with no official finding (the Sirik band) | same ledger |
| 🟡 **YELLOW** | Any new confirmed fatality in a class already hit since 6/27 | same |
| 🟢 **GREEN** | 30 days with zero confirmed killed in scope | same |
**Revision policy:** bands change only through PROME to Will with the ledger evidence; the ledger itself is append-only (corrections as new rows with pointers). **Scope exclusions (registered):** Iranian military/IRGC combatants; Israel-front casualties (HAWK's); claim-only counts from Iranian or Houthi media without a second route.

## 3. State at registration — 2026-09-08 (computed, and it is LIT)
| Window | Confirmed killed | Rows |
|---|---|---|
| 2026-07-11 → 08-09 (prior 30d) | **3** | GFS Galaxy 1 · Mombasa B 1 · Kuwait worker 1 (+ Minoan Pioneer 1 MISSING, not counted) |
| 2026-08-10 → 09-08 (current 30d) | **11** | Tihamah **6** · Sirik **5** (contested attribution, deaths confirmed by Iranian officials) |
**RATE-STEP: 11 vs 3 = 3.7× and ≥ 5 ⇒ 🔴 LIT.** Robustness: excluding Sirik entirely (if one refuses contested-attribution rows) gives 6 vs 3 = 2.0× and ≥ 5 ⇒ **still LIT on Tihamah alone.** **ORANGE (ii) also LIT** (Sirik: 5 dead, ~70 wounded, named weapons experts via Reuters assess a likely direct US munition hit; no official finding). **CLASS-STEP: NOT fired** — no US, GCC-military or coalition death since 6/27; the 9/8 Jordan salvo was 18-of-20 intercepted with zero casualties; the eight Iranian hulls were struck after crew evacuation, zero dead.
⚠️ **The instrument is lit AT REGISTRATION, and that is disclosed rather than hidden:** the doubling it measures happened in AUGUST (Tihamah) and was invisible because the tell that should have seen it had been retired without a successor. This is the FAL-03 already-true-at-registration shape — but for an INDICATOR, not a prediction, the honest disposition is to register it lit, say why, and let the next 30-day window grade it fresh. **Consequence for `EXIT_PROTOCOL.md` §3:** indicator #5 is LIT ⇒ the D→70+ list reads **3 of 8** (from 2 of 8). **No mark moves** — the list is an indicator set; the ladder moves on the registered rung.

## 4. The 8/10 standing correction — folded here from STATUS (its permanent home)
On 7/30 the desk published that the Kuwait worker killed 2026-07-30 was *"the exchange's first fatality"* and built the ratchet argument on it. **False.** On 2026-07-14 (local) ADNOC L&S VLCCs Al Bahyah and Mombasa B were struck by Iranian cruise missiles in the Strait of Hormuz; one Indian seafarer was killed aboard Mombasa B and eight were injured (four seriously); neither sank — verified at the operator's own release (adnocls.ae 7/14) plus The National, Gulf News, Khaleej Times and Insurance Journal. And that correction was itself incomplete: `KB-FALCON-023` already showed **two confirmed deaths standing before 7/12** and a third (GFS Galaxy's engineer, body recovered by the Omani Navy 7/14). **Cause:** the casualty axis was graded off strike-ledger and land-target reporting; mariner deaths live in the vessel-incident stream that the facilities-scoped instruments exclude by construction. **Fix:** this ledger. `KB-FALCON-086`.

## 5. Base rate — the acute phase, for scale
March (acute phase): 7 US service members killed and 140 wounded by 3/11 (`KB-HAWK-067`), 6 of them in one drone strike inside Port Shuaiba (CAS-001); civilian and coalition casualties across the GCC and Iraq. **The post-MOU cycle (6/27 →) has produced ZERO US or GCC-military deaths in 74 days** against that March record — every salvo at US forces has been intercepted or evaded. **That is the class-step's base rate, and it is why trigger (d) is a rung trigger:** the regime has held for 74 days and a single confirmed US death would be a step change, not an increment.

## 6. Cadence
Recompute §3's two windows at every FULL session (the ledger is the instrument; prose is never the source). A new row = a new KB row + this file's §3 refreshed. Boot has no reader for this file — `STATUS.md`'s tells list #5 and `VX-FALCON-CASUALTY-01` are where a session sees it.
