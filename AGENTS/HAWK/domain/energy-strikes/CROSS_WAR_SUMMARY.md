# Cross-War Energy-Strike Aggregate — Summary (thin, derived)

> **Convention:** this file is **regenerated from OSPREY's and FALCON's own strike ledgers at HAWK closeout (CLAUDE.md step 13), never independently maintained.** HAWK does not log strike rows — that discipline lives with the theater owners. If this file drifts from the siblings' ledgers, re-pull from them; do not hand-edit rows here.
> **Predecessor:** the original `STRIKES.tsv` + `SUMMARY.md` in this directory are 🧊 FROZEN 2026-07-12 (pre-split, 36-row combined ledger) — see their banners.
> **Regenerated:** **2026-07-25** from both siblings' `domain/energy-strikes/` as of today. *(Prior regeneration: 2026-07-12 split day — it had gone 13 days stale and understated FALCON by 23 rows; see the correction note below.)*

---

## One row per theater

| Theater | Ledger | Rows | Date range | Swept-through mark | Channel state (as of 7/24-25) | Pointer |
|---|---|---:|---|---|---|---|
| **Russia/Ukraine** | `AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv` | **49** | 2026-02-23 → **2026-07-22** | **2026-07-23** (advanced 7/12→7/23 in OSPREY's Task-C rebuild; +8 rows incl. 3 backfills the 7/12 "complete" mark had also missed) | Three channels in parallel. **Ch.1 refineries/products 4🔴** — campaign has now hit **all ~11 major Russian refiners** (Salavat 7/13-14 closed the last untouched major), pivoting to re-strikes/down-chain. **Ch.2 crude-export terminals 4🔴 — GATE-OSPREY-001 FIRED 7/24** on the ≥5-session leg (CPC halt continuous 7/20-24), SPMs officially intact. **Ch.3 shadow-fleet tankers 3🟠**, vessel counts reconciled. | `AGENTS/OSPREY/domain/energy-strikes/ANALYSIS_2026-07-23.md`, `CPC_HALT_2026-07-21.md` |
| **Iran/Gulf** | `AGENTS/FALCON/domain/energy-strikes/STRIKES.tsv` | **29** | **2026-02-28 → 2026-07-12** | **2026-07-12** — ✅ **founding-mandate backfill EXECUTED** (5→27 rows on 7/12 PM), *no longer the 3/19-stale seed ledger this table previously reported* | **GATE-FALCON-001 leg-1 FIRED 7/23** (Encelia struck 7/22, UKMTO-confirmed) — premium-dominant; legs 2-3 unfired, no hull sunk, zero barrels lost. | `AGENTS/FALCON/domain/energy-strikes/ANALYSIS_2026-07-12.md` |

**⚠️ Correction to this file's own prior version (logged, not silently overwritten):** the 7/12 regeneration reported FALCON at **4 rows, swept-through 2026-03-19, "thin/unbuilt, backfill not yet run."** That was true at the moment of spinout and **false within hours** — FALCON executed the backfill the same afternoon (5→27 rows). This table then carried the stale asymmetry for 13 days. It is exactly the failure mode the file's own convention note warns about: a *derived* surface is only as current as its last regeneration, and "derived" is not the same as "self-updating."

---

## The cross-war observations

**1. Both gates fired on their NON-severity legs, 24 hours apart (7/23-24).** FALCON's on premium-dominant kinetic execution; OSPREY's on duration/persistence. In both theaters the *severity* legs (production damage / SPM structural damage / FM / vessel sunk) remain **unfired**. This is the current core HAWK finding — see `STATUS.md` §1, `KB-HAWK-228/229`, `FLOW-HAWK-19` (re-cut).

**2. 🔴 Production-class sparing is a CURRENT-CYCLE regime, not a war-long constant — and this table is where that becomes visible.** FALCON's backfill establishes that Gulf/Iranian **production-class** assets **were** damaged in the war's first phase (**Feb 28 – Apr 9**):

| Asset | Class | Impact |
|---|---|---|
| Khurais (Aramco) | upstream production | −300 kbpd [C3] |
| Manifa (Aramco) | upstream production | −300 kbpd [C3] |
| South Pars / Asaluyeh (Iran) | gas production/processing | ~14% of output offline [B1, 3/18] |
| Ras Laffan ×2 + Pearl GTL (Qatar) | LNG production trains | ~17% of Qatar export capacity, 3–5 yr repair [B1] |
| Shah + Habshan (ADNOC) | gas processing | halted/fire [C3] |
| East-West pipeline pump + Ju'aymah (Aramco) | export infrastructure | −700 kbpd flow [C3] |

FALCON already re-worded the claim correctly on 7/12: what is spared is (a) the **Kharg oil-export chain** (US spared it 3× deliberately) and (b) **Aramco/ADNOC-class production complexes during the CURRENT post-MOU cycle (Jun 27 →)**. **Consequence for HAWK: the sparing regime is ~4 weeks old, not 5 months old.** HAW-18 was corrected 60%→55% on this the same session it was registered — a bet on a *regime holding* is weaker than a bet on a constant. Independent corroboration of the higher base rate: Goldman's **42% average 4-yr production-hit base rate** [SIG-W-20260721-006, 7/20].

**3. The older timing observation, retained:** Russia's refinery-strike campaign peaked the same week Iran signed its (now-collapsed) MOU — two independently-driven escalation cycles cresting in one window with **no shared causal mechanism shown**. Still coincidence until a mechanism is demonstrated.

---

## Reading this table

- **Ledger asymmetry has substantially CLOSED** (49 vs 29 rows, both actively swept) and is now mostly a genuine difference in campaign tempo and duration, not a data gap. Do not re-import the old "FALCON is thin/unswept" framing — it is retired.
- **The two swept-through marks are 7/23 (OSPREY) and 7/12 (FALCON).** FALCON's is 13 days old as of this regeneration — worth a nudge if it hasn't advanced by the next pass, especially since FALCON's theater has had the more eventful fortnight (Bab ladder, Encelia, Mangaf).
- **HAWK's job here** is limited to (a) keeping this pointer table current at closeout and (b) flagging when the siblings' swept-marks go stale — **not** rebuilding their ledgers. Where a metric has a theater owner, cite theirs; keep no competing copy.
