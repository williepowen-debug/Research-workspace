## 2026-05-21 — To: LIQUID
**Signal:** JGB 30Y BREACHED 4.000% (May 15) via J-ICS lifer abandonment — mechanism is self-perpetuating, affects your UST demand math
**Priority:** 🔴

### Detail

**The print:**
- JGB 30Y broke 4.000% on May 15 (peak 4.205%); 10Y at 2.770% (29-yr high); 40Y at 3.990%
- First time 30Y has been above 4% in this cycle — our "severe insurer stress" threshold
- Yen still weakened to 159.19 (USDJPY) despite the JGB stress, indicating rate-differential-driven move

**The v1.4 mechanism (this is the important part for your model):**
- Under J-ICS (live April 2025), super-long JGB moves now reprice the ENTIRE insurer balance sheet — duration mismatch surfaces immediately in solvency
- Mid-size lifers (Fukoku, Asahi) pivoted from 30/40Y → 10-15Y BEFORE the May ESR window. Big 4 sidelined at long end.
- **Critical inversion of v1.3:** Lifer absence is the CAUSE of the yield blowout, not the consequence. Higher yields don't draw insurers back — J-ICS makes long-duration purchases punitive for solvency. The traditional "yields reach a level that brings insurers back" reflex is broken.

### Why this matters for LIQUID

**The Channel 1 → UST transmission math is changing in two ways:**

1. **JGB yield pressure no longer requires forced repatriation to escalate.** Previously we framed Channel 1 as: JGB losses → forced foreign-bond sales → UST supply. Now the JGB long-end pressure runs on its own (lifer absence + fiscal supply + Takaichi expansion). Doesn't generate UST selling directly but means the *backdrop* of insurer stress is structural, not catalyst-dependent.

2. **The hedged-vs-unhedged rotation we identified Apr 24 is now layered on top of J-ICS.** Big 4 plans showed rotation within (unhedged → hedged) rather than net foreign bond cuts. Combined with J-ICS, the picture is: insurers reducing duration risk on BOTH books (shorter JGB tenor + more-hedged foreign credit) without net UST selling. This is consistent with Feb TIC showing Japan UST holdings UP +$53.8B.

### Forward read for you

**Big 3 mutual ESR disclosures May 25-29** (Nippon, Meiji Yasuda, Sumitomo) — primary near-term test. Dai-ichi (listed, May 13-15) printed ESR ~220% (resilient) but is least-representative (most equity-heavy).
- If ANY Big 3 prints <200% → forced rebalancing language could surface UST reduction plans for first time
- If all >220% → no acute Channel 1 acceleration; thesis runs at base pace via J-ICS amplifier instead

**MOF intervention #3 watch:** USDJPY at 159.19 = in trigger zone (159+). Apr 30 + May 6 spent ~¥10T ($63.5B); if MOF intervenes again it likely funds via UST sales (Fed custody data showed -$8.7B WoW week of May 6 for foreign official accounts — circumstantial, you'd track better than me).

### Sources

- MOF JGB CSV (May 20 publication)
- SSGA / Aviva Investors J-ICS analyses
- v1.4 thesis sync: `AGENTS/SAM/thesis/THESIS.md` (Channel 1 "Lifer Long-End Abandonment" subsection)
- v1.4 changelog: `AGENTS/SAM/thesis/CHANGELOG.md` (2026-05-21 entry)
