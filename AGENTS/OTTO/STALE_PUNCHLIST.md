# OTTO — Stale-Intel Punch-List

**Produced:** 2026-06-02 (Phase-3b cross-doc audit) | **Re-audited:** 2026-06-08
**Status:** discovery + light remediation. STATUS.md was line-capped/archived Jun 8 (no longer a rot item).
Everything below is still OPEN unless marked ✅. Resolve at a dedicated content-refresh; mark
`[STALE <date>]` on anything that can't be refreshed rather than carrying it forward as current.

> **Jun 8 note:** This session refreshed STATUS dashboard + predictions (spreads, First Brands Jun 12,
> OTTO-05) but did NOT touch the docs below. Several got *relatively* worse because STATUS moved and
> these didn't (TRADE.md, VX.tsv spreads). Ranked by behavioral impact — does a stale read make OTTO
> *do* something wrong? — not line count.

## Original 9 (Jun 2) — Jun 8 status

| # | File | Last touched | Status Jun 8 | What's rotted (behavioral risk) |
|---|------|--------------|--------------|----------------------------------|
| 1 | **`TRADE.md`** | 2026-02-16 | 🔴 OPEN — **now worse** | Pre-5:1-split CVNA (~$343 / ATH $486.89) vs this-session **confirmed spot ~$64** — strikes off by 5×; dead Feb-18 triggers (GT resign, 10-K delay, "Feb 18 catalyst"); ALLY "~$37 (need to verify)"; broken cross-refs to nonexistent `POSITIONS.md`/`PREDICTIONS.md`. **Top priority** — a trader acts on a dead thesis. |
| 2 | **`RESEARCH_STATUS.md`** | 2026-02-14 | 🔴 OPEN | ACTIVE MONITORING all Feb-18-stale (Carvana "Feb 18", PrimaLend "THIS WEEK Feb 17", First Brands examiner "~Feb 25", Tricolor "Aug 2026" → now Oct 19). **Confirmed missing post-Feb work:** RP-OTT-3.3 + `recon/STAGE2_FINDINGS_2026-03-16.md` not indexed. Misroutes "what's next" at boot. |
| 3 | **`workbook/VX.tsv`** | 2026-04-17 hdr / Feb data | 🟠 OPEN — **now more divergent** | Current_Value Feb-stale (VX-001 "6.80% 60+ DQ"; VX-002/003 "BBB 180bps Jan / BB 350bps+") — **contradicts this session's +190 EART print + the falsified "IG-only" claim**. 3-way threshold dup (VX rungs ↔ CLAUDE rules ↔ STATUS) persists. Decide: VX = structured registry, current values reference STATUS. |
| 4 | **`EDGAR_8K_MONITOR.md`** | 2026-03-09 | 🟠 OPEN | All watch windows expired (OZK Apr 16, WAL Apr 22 passed); "Next mandatory sweep Mar 25" long past. Heavy REGINALD overlap (bank 8-Ks = REGINALD). **Decide: retire, or hand the watchlist to REGINALD and keep only method.** |
| 5 | **`workbook/KB.tsv`** | 2026-04-17 (9 rows) | 🟡 OPEN | `STALE_BY` convention firing on aged rows (First Brands `STALE_BY 2026-04-30`). Small file — quick refresh-or-supersede. |
| 6 | **`scripts/*` + `workbook/ABS_ISSUANCE.tsv`/`EXTENSION_PROXY.tsv`** | 2026-04-14 data | 🟠 OPEN — **decision needed** | The two scripts are **STUBS** ("manual check required") — this session's test-run appended a junk placeholder row (`0 / TBD / TBD`) to ABS_ISSUANCE.tsv. **Decide: implement a real EDGAR/rating-agency pull, or retire the stubs** (= roadmap #12). Don't keep producing placeholder rows. |
| 7 | **`workbook/FLOW.tsv`** | 2026-02-04 valid | 🟡 OPEN | `Last_Validated 2026-02-04` across rows — validation stale even where mechanisms intact. Low risk; re-validate dates. |
| 8 | **`LESSONS.md`** | durable | 🟡 OPEN — **more urgent** | Overlaps MEMORY § Feedback + Evidence Conventions; **this session promoted 4 lessons to auto-memory**, deepening the overlap. Consolidation candidate — pick one home (Will-decision). |
| 9 | **`OUTBOX.md`** | vestigial | 🟡 OPEN | Deprecated by messaging overhaul; routing now via WALTER inbox. Decommission candidate — but part of the messaging-overhaul workstream; don't patch piecemeal. |

## New items surfaced Jun 8

| # | Item | Behavioral risk |
|---|------|-----------------|
| 10 | **DQ-series reconciliation** | STATUS "60+ DQ **7.1%**" vs Fitch ABS index **6.90%** vs VX-001 **6.80%** — three numbers, unclear which series the dashboard tracks (TransUnion all-DQ vs Fitch ABS subprime). Pick the canonical series, label it, reconcile across STATUS/VX/CLAUDE. Until then OTTO can't say its headline DQ with confidence. |
| 11 | **"Below-IG clearing" reframe not propagated to VX** | The Jun 8 correction (below-IG tranches ARE clearing; "IG-only" retired) lives in STATUS/PREDICTIONS/CHANGELOG but VX-002/003 still say "BB 350bps+ / IG-only" framing. If VX is kept (item 3), propagate; covered by the item-3 refresh. |

## Recommended next-session order
1. **TRADE.md rehab (#1)** — highest behavioral risk; split-adjust CVNA, kill dead triggers, fix cross-refs. (Roadmap #3.)
2. **RESEARCH_STATUS.md (#2)** — re-point ACTIVE MONITORING to live catalysts; index RP-OTT-3.3 + recon STAGE2.
3. **VX.tsv (#3) + DQ-series reconcile (#10)** — do together; resolves the 3-way threshold dup AND the DQ-series ambiguity. Propagate below-IG reframe (#11).
4. **Stub-script decision (#6)** — implement real pull or retire (don't keep emitting junk rows). (Roadmap #12.)
5. **EDGAR_8K_MONITOR (#4)** — retire or hand to REGINALD.
6. **Will-decision items: LESSONS consolidation (#8), OUTBOX decommission (#9)** — structural, need a call.
7. **Low-risk hygiene: KB.tsv (#5), FLOW.tsv (#7) re-validate.**

## Notes
- **Do not fix opportunistically** — this is a coherent refresh pass. Items 1–3 + 10 carry real behavioral risk; rest is hygiene.
- TRADE.md (#1) is the case the `[STALE]` convention exists to prevent — rotted silently ~3.7 months now.
- Items 8–9 are structural consolidation calls, not value-refreshes — Will-decision before action.
