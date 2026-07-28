# Cross-War Energy-Strike Aggregate — Summary (thin, derived)

> **Convention:** this file is **regenerated from OSPREY's and FALCON's own strike ledgers at HAWK closeout (CLAUDE.md step 13), never independently maintained.** HAWK does not log strike rows — that discipline lives with the theater owners. If this file drifts from the siblings' ledgers, re-pull from them; do not hand-edit rows here.
> **Predecessor:** the original `STRIKES.tsv` + `SUMMARY.md` in this directory are 🧊 FROZEN 2026-07-12 (pre-split, 36-row combined ledger) — see their banners.
> **Regenerated: 2026-07-28** from both siblings' `domain/energy-strikes/`, reading each ledger's **own analysis header**, not just its row count (`LESSONS.md` 2026-07-25 item 2). *(Prior regenerations: 2026-07-25; 2026-07-12 split day.)*

---

## One row per theater

| Theater | Ledger | Data rows | Date range | Swept-through mark | Channel / gate state | Pointer |
|---|---|---:|---|---|---|---|
| **Russia/Ukraine** | `AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv` | **48** | 2026-02-23 → 2026-07-22 | **2026-07-23** ⚠️ **5d, and content-stale** — Tyumen (7/25) and Golden Leo (7/26) are both un-rowed | Three channels in parallel. **Ch.1 refineries/products 4🔴** — all ~11 major Russian refiners hit; pivoting to re-strikes/down-chain. **Ch.2 crude-export terminals — GATE-OSPREY-001 FIRED 7/24** (≥5-session leg, SPMs officially intact); **⚠️ CPC has since RESUMED 7/27 — see below.** **Ch.3 shadow-fleet tankers 3🟠.** | `ANALYSIS_2026-07-23.md`, `CPC_HALT_2026-07-21.md` |
| **Iran/Gulf** | `AGENTS/FALCON/domain/energy-strikes/STRIKES.tsv` | **31** | 2026-03-02 → **2026-07-27** | **2026-07-27** ✅ current (advanced 7/17→7/27 in the 7/27 s1 sweep; ledger 27→30→31) | **GATE-FALCON-001 leg-1 FIRED 7/23**; legs 2-3 unfired (leg-2 on the registered *tanker* metric, leg-3 on data absence). **FAL-01 RESOLVED FAILED 7/27** on the Jazan strike. Scenario re-marked **B 10 / C 40 / D 50**, convergence 42→40. | `ANALYSIS_2026-07-27.md` |

**⚠️ Correction to this file's own prior version (logged, not silently overwritten).** The 7/25 regeneration reported FALCON at **29 rows, swept-through 7/12** and flagged that mark as "13 days old, worth a nudge." **FALCON had already advanced it to 7/27** by the time of this pass — so the nudge was answered before it was sent, and this table understated FALCON for a *second* consecutive regeneration. **The asymmetry has now flipped: OSPREY is the stale side.** *(First instance: the 7/12 version reported FALCON "thin/unbuilt, backfill not yet run" for 13 days after FALCON had executed it.)* Same root cause both times — a derived surface is only as current as its last regeneration.

---

## The cross-war observations

**1. 🆕 THE THEATERS HAVE DECOUPLED FROM EACH OTHER — the 7/25 "both gates fired together" framing is superseded.** As of 7/28 there are **three counter-moving belligerent legs across two agent-theaters**:

| Leg | Direction | Evidence |
|---|---|---|
| **US–Iran** | ↓ **DE-ESCALATING** | 13-night campaign paused 7/24, holding 3+ nights; Iran on record halting retaliation; Oman-mediated Hormuz channel active. ⚠️ Cause is a **munitions/target-list constraint** (Adm. Cooper, Gen. Caine), so it is durable short-horizon and **silent on intent** |
| **Saudi–Houthi** | ↑ **ESCALATING** | Four-year truce broken; Jazan struck 7/25 and still burning 7/26-27 on two claimant-independent satellite constellations; Yanbu fired on and intercepted 7/25; Petroline claimed 7/27 (claim-only) |
| **Russia–Ukraine** | → **CONTINUING** | Tyumen refinery hit ~2,000 km deep 7/25 (deep diesel hydrotreater, ~151 kbpd); Golden Leo sunk 7/26; CPC resumed 7/27 |

**Methodological consequence, and it is HAWK's own version of the problem FALCON solved with its P/R split: reconciling BY AGENT-THEATER is now the wrong cut.** FALCON's single file contains two counter-moving wars — its convergence composite *fell* 2 points in the week its theater took its first Aramco production-class hit since 2022. The correct cut for cross-war synthesis is **by belligerent dyad**, not by which sibling owns the file. → `KB-HAWK-238`.

**2. 🆕 THE CPC RESOLUTION — the cleanest natural experiment either theater has produced, and it confirms the migration thesis.** HAWK pre-registered the test on 7/25: *"owner return with SPMs intact = strong confirm; a late SPM-damage or FM disclosure = the fire was severity all along and I mis-attributed it."*

**Outcome (Astana Times 7/27, primary):** loadings resumed at two SPMs after ~1 week, **no structural damage confirmed, no repair, no new force majeure**, with the operator framing continuation as conditional on *"ongoing assessments of the security situation."* The returning tankers (SEAMAJESTY, MILOS) were chartered by **Tengizchevroil** — i.e. **the same Chevron whose refusal to call defined the willingness leg on 7/23.**

**The refinement this forces:** during the halt ~**440 kbpd** of Kazakh output was offline (2.07 → 1.63 M bpd, −21%; Tengiz −56%). That is **production-class magnitude with zero capacity destroyed**, reversed on a decision rather than a repair. **⇒ Magnitude no longer discriminates a premium event from a physical supply event — only reversibility does.** → `KB-HAWK-235/236`, `FLOW-HAWK-19`.

⚠️ **Two vintage traps caught while resolving this**, both of which would have falsely fired `HAW-18`: a Baird Maritime "CPC returns to full loading capacity after mooring point repaired" headline is **25 January 2026** (SPM-3, damaged Nov 2025), and every "Tengiz force majeure" headline in circulation is the **January 2026** GTES-4 power-station arc. Neither is a July event. *(OSPREY had independently date-verified both — the guard held on both sides.)*

**3. Production-class sparing is a CURRENT-CYCLE regime, not a war-long constant.** FALCON's backfill establishes Gulf/Iranian **production-class** damage in the war's first phase (**Feb 28 – Apr 9**):

| Asset | Class | Impact |
|---|---|---|
| Khurais (Aramco) | upstream production | −300 kbpd [C3] |
| Manifa (Aramco) | upstream production | −300 kbpd [C3] |
| South Pars / Asaluyeh (Iran) | gas production/processing | ~14% of output offline [B1, 3/18] |
| Ras Laffan ×2 + Pearl GTL (Qatar) | LNG production trains | ~17% of Qatar export capacity, 3–5 yr repair [B1] |
| Shah + Habshan (ADNOC) | gas processing | halted/fire [C3] |
| East-West pipeline pump + Ju'aymah (Aramco) | export infrastructure | −700 kbpd flow [C3] |

What is spared is the **Kharg oil-export chain** and **Aramco/ADNOC-class complexes during the current post-MOU cycle (Jun 27 →)**. **The sparing regime is ~4-5 weeks old, not 5 months old** — HAW-18 was corrected 60%→55% on this. Independent corroboration of the higher base rate: Goldman's **42% average 4-yr production-hit base rate** [SIG-W-20260721-006].

**4. The old timing observation, retained and now weaker:** Russia's refinery campaign peaked the same week Iran signed its (now-collapsed) MOU. With the theaters visibly decoupling in observation 1, this looks more like coincidence than ever. **Still coincidence until a mechanism is demonstrated.**

---

## Reading this table

- **The ledger asymmetry has flipped.** It is no longer FALCON that lags — **OSPREY's swept-through mark (7/23) is now the stale side**, with two material un-rowed events (Tyumen 7/25, Golden Leo 7/26) and a superseded CPC state. Nudge sent 7/28. Do not re-import the retired "FALCON is thin/unswept" framing in either direction — check the marks each pass.
- **Row counts are not comparable across theaters** and never were: 48 vs 31 reflects campaign tempo and duration, not data quality.
- **HAWK's job here** is limited to (a) keeping this pointer table current at closeout and (b) flagging when the siblings' swept-marks go stale — **not** rebuilding their ledgers. Where a metric has a theater owner, cite theirs; keep no competing copy.
