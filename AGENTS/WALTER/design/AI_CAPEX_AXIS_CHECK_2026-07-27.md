# AI_INFRA_CAPEX — REVISIT-TRIGGER EVALUATION AT THE 40/40 CAP

reviews_cluster: AI_INFRA_CAPEX

**Date:** 2026-07-27 · **Run by:** WALTER · **Trigger:** `SIG-W-20260727-012` took the cluster to **40/40**, AT the soft cap set by `CLUSTER_TAXONOMY` v0.5 (Will-approved 7/16, raised 15→40 with the KEEP verdict).
**Authority:** `CLUSTER_TAXONOMY` v0.6 — *"Evaluate at a cap breach or a review, **not continuously**"*; the evaluation is **WALTER-owned, no Will gate.** Changing the cap is **Will's** (spec Rule 8: structural change → proposal first).
**Precedent:** [`AI_CAPEX_AXIS_CHECK_2026-07-16.md`](AI_CAPEX_AXIS_CHECK_2026-07-16.md) (the v0.5/v0.6 check).

---

## 1. VERDICT

> **KEEP the cluster. Limb (a) does NOT fire. Limb (b) FIRES — and it is diagnosing a WALTER INTAKE DEFECT, not a taxonomy defect.**
>
> **No split, no re-cut, no new cluster.** The recommendation that follows is about **cap policy and intake coverage**, not about this cluster's coherence.

## 2. THE BIDIRECTIONAL TEST, EVALUATED

v0.6 rewrote the trigger to two limbs. Both evaluated against the **trailing 60 days (≈ 2026-05-28 → 2026-07-27)**, which covers ~25 of the 40 rows.

### Limb (a) — DISPERSION: angle count > 5?

| Angle | In-window signals (60d) | Present? |
|---|---|---|
| **financing** | ~10 (`626-031`, `627-010`, `627-011`, `704-001`, `708-001`, `709-001`, `721-002`, `721-012`, `723-009`, `723-010`) | ✅ dominant |
| **power** | 3 (`717-009`, `721-011`, `725-010`) | ✅ |
| **supply-chain / geopol-semis** | 2–4 (`723-008` SK hynix, `723-011` supply-side mosaic) | ✅ |
| **ROI / FCF** | 2–3 (incl. **`727-012` — Alphabet capex raise vs NEGATIVE FCF**, the cleanest ROI-axis signal in months) | ✅ |
| muni / fiscal | 1 | marginal |
| **memory / input-cost** | **0–1** | ❌ |
| **obsolescence** | **0** (last was 5/11, now ~11 weeks stale) | ❌ |

**Distinct angles genuinely populated: 4, with a 5th marginal. NOT >5.**
**⇒ LIMB (a) DOES NOT FIRE. The cluster has not fragmented — the same finding as 7/16, and it has held for eleven days and seventeen further signals.**

### Limb (b) — CONCENTRATION: any ORIGINAL angle < 2 signals in 60d?

The original v0.2-era four angles were **financing · ROI · obsolescence · input-cost.**

- financing — ~10 ✅
- ROI — 2-3 ✅ (helped over the line by `727-012`)
- **obsolescence — 0. ❌ FIRES.**
- **memory / input-cost — 0-1. ❌ FIRES.**

**⇒ LIMB (b) FIRES, on two of the four original angles.**

## 3. 🔑 BUT WHAT LIMB (b) IS ACTUALLY MEASURING — the reason this is not a split

**VULCAN already settled this on 7/16, and the answer is the whole point of the bidirectional rewrite:**

> *"Your cluster count is measuring your taxonomy, not my domain."*

VULCAN's 7/16 adjudication established, with receipts, that **the two empty angles are empty because WALTER'S INTAKE NEVER SAW THEM**, not because the domain went quiet:

- **memory / input-cost:** **TrendForce returned 0 hits across all 764 archive rows.** **Micron's FQ3 beat ($41.46B vs $32.75-34.25B guide) never entered WALTER at all — not killed, NEVER SEEN.** And WALTER's own *clustering* filed the memory signals under `ASIA_CHINA`, so the count under-read the domain twice over. The lone signal labelled "input-cost" (`627-018`) **isn't one** — its header reads `domain: ASIA_CONTAGION`.
- **obsolescence:** an explicit **hypothesis, not a finding** — VULCAN was built 7/10, has zero obsolescence coverage, and cannot see the 5/11→7/10 window. **Nobody in the fleet owns hyperscaler depreciation schedules.**

**And WALTER's filter is NOT the cause: VULCAN checked it — 6 relevant kills out of 270, all 6 correct, *"changing a gate on this evidence would be a regression."***

### 🚩 A THIRD CONFIRMING INSTANCE, produced TODAY

**`SIG-W-20260727-012` exists because WALTER MISSED IT for four days.** Alphabet raising FY26 capex to **$195-205B** with **negative FCF**, Tesla capex **+142%**, and the **Magnificent-7's worst day in over a year (−4.8%, ~$787B erased)** — an **ROI-axis event, in this cluster, on 7/23** — went unrouted by a WALTER session that ran *that same evening and dispatched 19 signals*, four of them in this cluster.

**That is the same failure mode as the Micron and TrendForce gaps, on a third axis, and it is now n=3.** The pattern is consistent and specific: **WALTER's intake reliably catches AI-infrastructure FINANCING and SUPPLY/CREDIT, and reliably misses the DEMAND-SIDE CAPEX-GUIDANCE / ROI / INPUT-COST legs.**

## 4. CONCLUSION + RECOMMENDATION TO WILL

**Cluster action: NONE.** Keep it whole, cap stays at 40 until Will decides otherwise. Limb (a) — the only limb that speaks to *fragmentation* — has now failed twice, eleven days and seventeen signals apart. VULCAN wants both halves; the angles still answer one question (*"does the buildout continue?"*).

**Two things ARE owed, and neither is a taxonomy change:**

1. **🔴 THE REAL DEFECT IS INTAKE COVERAGE, and it now has three instances** (Micron/TrendForce 7/16 · obsolescence structurally · **Alphabet/Tesla 7/27**). **The fix is a collection question, not a filter or taxonomy question** — WALTER's gates were audited clean. Candidate: add megacap **capex-guidance and FCF** lines, plus memory-pricing (TrendForce/DRAMeXchange class), to a named intake surface — the RESEARCH-INTAKE lane is the obvious host, since it is already the live successor to the dead cron feeds. **Flagged to PROME/Will as a lane-scope proposal; not built unilaterally.**
2. **📐 CAP POLICY (the recorded-but-undecided counter from v0.5, now with evidence).** A bare row-count keeps measuring the taxonomy rather than the domain — **limb (b) fired here on angles that are empty because of collection, and a naive reader would take that as a reason to split a healthy cluster.** **WALTER's recommendation stands: retire per-cluster numeric caps in favour of the review trigger, fleet-wide.** Peer calibration continues to argue the same way — `IRAN_HORMUZ` is now **94**, `CONSUMER_STAGFLATION` **103**, `BANK_COLLATERAL` **94**, `POSITIONING_VALUATION` **83**, all **uncapped and unremarked**, while AI_INFRA_CAPEX at 40 is the only capped cluster in the taxonomy. **Will's call.**

**Also worth recording, because it is the cap working as designed:** two *duplicates* would have consumed the 40th slot earlier today — the `$1.65T` hedgehog re-post and the Oracle `$7B` re-post, both killed on Novelty. **The slot went to Alphabet's capex guidance instead.**

## 5. VULCAN's PROPOSED 5-AXIS RE-CUT — still NOT adopted

`financing · ROI (incl. obsolescence) · memory/input-cost · power · supply-chain-geopol` — recorded in v0.6, **needs Will + the live VULCAN's ratification**, unchanged by this evaluation. **Honouring VULCAN's own caveat: *"arrive there by the reasoning, not by deference to my frame."*** Note this evaluation supplies one piece of supporting reasoning: **collapsing obsolescence into ROI would remove one of the two angles that just fired limb (b) for reasons that have nothing to do with the domain** — i.e. the re-cut would make the trigger less noisy. That is an argument *for* it, but it is Will's and VULCAN's to make.
