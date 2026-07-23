## 2026-07-23 (~2:30 PM ET) — To: PROME — OSPREY data-hygiene sweep + Task C rebuild
**Priority:** 🟡 (hygiene — no marks moved, no gate touched). Own dir only. Zero threshold/mark moves; frozen gate conditions + today's Will-approved marks untouched.

---

### A. TASK C — full strike-ledger rebuild 7/12→7/23 (the main event) ✅ DONE, swept-mark ADVANCED
Complete row-by-row mechanism-level sweep (refineries AND terminals AND tankers AND pipelines/depots), all events 2026-vintage-verified. **Swept-complete mark advanced 7/12 → 7/23** on a genuinely complete in-window pass (HAW-15 discipline: mark only moves on a complete pass — this was it). **+8 material rows:**

| Row | Date | Ch | Source (date-verified) |
|---|---|---|---|
| Gazprom Neftekhim Salavat | 7/13–14 | 1 | Ukrainska Pravda/Militarnyi 7/14 |
| Black Sea shadow-fleet tankers (Louise 1, Banda +~20; +7/17) | 7/15–17 | 3 | Bloomberg 7/16; KyivInd 7/17 |
| NS-Oil Refinery (Novospasskoye, Ulyanovsk) | 7/22–23 | 1 | KyivIndependent 7/23 |
| Oil pump-station (Tuymazy, Bashkortostan) | 7/22–23 | 2 | KyivIndependent 7/23 |
| Oil depot (Armavir, Krasnodar) | 7/22 | 1 | Zelensky/Moscow Times 7/22 |
| **Kstovo (LUKOIL-Nizhegorodnefteorgsintez)** *(pre-mark backfill)* | 7/2 | 1 | Militarnyi 7/23; United24 7/7 |
| **Ilsky (KNGK)** *(pre-mark backfill, PROME-flagged)* | 7/9 | 1 | Moscow Times/Pravda 7/10 |
| **Taganrog terminal + Azov depot** *(pre-mark backfill)* | 7/10 | 2 | United24; Pravda 7/10 |

**KEY FINDING:** all 3 pre-mark backfills (Kstovo 7/2, Ilsky 7/9, Taganrog 7/10) were gaps the prior "swept-complete through 7/12" mark had **ALSO missed** — the **HAW-15 date≠content pattern repeated**. The founding lesson held again.
**Pattern shift (interpretation → `ANALYSIS_2026-07-23.md`):** Salavat 7/13-14 was the **last major RU petrol producer not yet hit in 2026** → the refinery campaign now covers **all ~11 majors**; new-refinery escalation is largely exhausted, replaced by re-strikes + a **down-chain pivot** to depots/pump-stations/logistics (the 7/22-23 223-drone wave). **Channel scores UNCHANGED** — this is data completeness, not a re-score. Logged KB-OSPREY-021.

### B. Data-hygiene fixes (was → now → source)
| Surface | Was | Now | Basis |
|---|---|---|---|
| `CPC_HALT` §1 table | "Fri 7/18" / "Sun 7/19–20" / "**Mon 7/21**" (Nelsa) — day-of-week labels WRONG | "7/17–18" / "Sun 7/19" / "7/20–21" + calendar-consistency note | Actual calendar: 7/17=Fri, 7/20=Mon, 7/21=Tue. Reconciles with §7 day-1=7/20 basis (unchanged) |
| `CPC_HALT` §1 prose | "re-halted **Monday 7/21** AM" | "re-halted **Mon 7/20** AM (Euronews dates 7/21 — tz lag)" | Same; aligns doc internally |
| `STRIKES.tsv` swept-mark | 7/12 (incomplete — missed 3 pre-mark rows) | **7/23** + honest residual-gap annotation | Task C complete pass |

### C. Verified-CLEAN (checked, no fix needed)
- **War-risk surface** (`BLACK_SEA_WAR_RISK.md`): B-04 absence row current (7/23); B-02 (7/21 >1%/1.5%) properly stamped; no fresh print to add. Clean.
- **NEXUS_BRIEF As-of**: 7/23, matches session. Clean.
- **KB rows 017/019/020 cross-consistency**: day-3→day-4 progression consistent; attribution row (020) non-contradictory. Clean.
- **STATUS slow-aggregates** (floating storage ~120M bbl mid-June; Urals ~25% May): already **explicitly stamped STALE**, 14-day re-verify due ~7/26 — properly disclosed, not silently rotting. Clean (correctly stale-marked).
- **Refining-offline band 25-35% [EST]**: stamped, expires 8/2 → OSP-03. Clean.

### D. Flagged (not fixed — per rules)
- **Residual pre-7/12 ledger gap, NOT rowed:** Kstovo **6/24** strike (referenced by the 7/2 reporting) — bounded out of this pass; row on next full sweep. Documented in the swept-mark annotation so the mark doesn't overstate.
- **Unconfirmed:** Tuymazy 7/22-23 pump-station **pipeline affiliation** (likely Transneft trunk; not independently confirmed) — rowed with an explicit UNCONFIRMED flag.
- **Cross-agent / N/A:** the seed's "scripts' state JSONs (bypass/hormuz/kharg)" are **FALCON's** (Iran/Gulf) — OSPREY is instrument-light (no scripts/ dir). Not mine to touch; flagging for FALCON's own sweep.

### Bottom line
Task C closed (twice-deferred item cleared, mark honestly advanced). One real internal inconsistency fixed (CPC_HALT weekday labels). The rest verified clean or flagged. No marks moved, gate untouched. Nothing owed before the Fri 7/24 day-5 check.
