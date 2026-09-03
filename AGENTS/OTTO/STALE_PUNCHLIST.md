# OTTO — Stale-Intel Punch-List

> **📌 s016 dispositions (2026-07-25) — 6 items closed, 3 explicitly DEFERRED (not silently dropped).**
> **CLOSED:** ① `KB.tsv` / `CROSS_AGENT_LOG.tsv` / `EXTENSION_PROXY.tsv` → **FROZEN** with banners (were re-flagging every fleet sweep).
> ② `ABS_ISSUANCE.tsv` → **FROZEN with an inversion warning** — it read `0 deals / shelf_halts 0` for a period STATUS documents as robust
> issuance, because its feeder script is a manual-check stub that emits zeros when unfilled. **This surfaced a live prediction defect: OTTO-07's
> instrument cannot falsify OTTO-07.** Flagged on the row; re-instrumenting owed before Dec 31.
> ③ `RESEARCH_STATUS.md` → **ACTIVE MONITORING table DELETED** (doc-ownership violation; it duplicated STATUS and had rotted into present-tense
> misinformation — "Carvana Feb 18 earnings 🔴 CRITICAL", "Tricolor Chu trial Aug 2026"). Completed-research index kept; it doesn't expire.
> ④ `EDGAR_8K_MONITOR.md` → **REPURPOSED, not retired** — reversing this punchlist's own "retire or hand to REGINALD". The bank-watchlist half is
> frozen (REGINALD's lane); the EDGAR full-text-search *method* is promoted to the top as OTTO's canonical instrument registry, because it is what
> found TFIN and what OTTO-30/-33/-07 now depend on.
> ⑤ `thesis/PREDICTIONS_ARCHIVE.md` scoreboard → **backfilled** (was stale at 5/5; actual **5/7**) + OTTO-05/-28 post-mortems written.
> ⑥ Stale `TRADE.md` "rehab-pending" pointers → **FROZEN 2026-07-04**.
>
> **DEFERRED — tracked, not dropped** (recorded here so they are not silently lost, per DAEDALUS 7/25):
> **(a)** §2 universal 5-pt handle overlay + Independence column over SIGNAL DASHBOARD (additive; DAEDALUS card priority 2).
> **(b)** Delete the dead `AGENTS/SIGNALS.md` append instruction in `CLAUDE.md` §313-18 — contradicts OTTO's actual WALTER routing.
> **(c)** `CLAUDE.md` version-stamp 3-way drift (v2.5 header / v2.7 footer / unversioned 7/4 edit); research-corpus retirement pass (~17 spent
> prompts >60d). **Reason for deferral:** all three are `CLAUDE.md`/corpus edits with no clock, and this session's remaining budget was spent on
> the 7/28-clocked work and on defects that mislead readers *now*. Next spawn.

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

> ⛔ **THIS ORDERED LIST IS 39 DAYS OLD (2026-07-25) AND CONTRADICTS THE DISPOSITIONS AT THE TOP OF ITS OWN FILE. Re-audited 2026-09-02; do not work it as written.**
> Found by BROCK's heading test — *read every heading that implies currency* — not by a string sweep, because a stale to-do list carries no wrong token. `STALE_PUNCHLIST`'s own charter says *"re-audit each major session"*; it had not been opened in **39 days and roughly eight sessions**. **A punch-list that goes stale is the one document class where staleness is self-refuting.**
>
> **Item-by-item reconcile against what actually happened:**
> - **#2 "re-point ACTIVE MONITORING"** — ⛔ **IMPOSSIBLE.** That table was **DELETED** in s016 by disposition ③ at the top of this very file. **The header retired the table and the footer still schedules work on it.**
> - **#5 "EDGAR_8K_MONITOR — retire or hand to REGINALD"** — ⛔ **REVERSED.** Disposition ④, four paragraphs above, **explicitly reverses this line**: the file was REPURPOSED, its EDGAR full-text-search method promoted to OTTO's canonical instrument registry. **The same file says both.**
> - **#4 "stub-script decision"** — ✅ **PARTLY DONE.** `EXTENSION_PROXY` and `ABS_ISSUANCE` frozen (s016); **`SHELF_ACTIVITY.tsv` FROZEN with an EVENT-DRIVEN cadence 2026-09-02** (DAEDALUS staleness #4 / PAT-095).
> - **#1 TRADE.md rehab** — ⚠️ **STILL OPEN and now ~5.2 months rotted.** TRADE.md is FROZEN and no position is live, so behavioural risk is contained — but the item is real and carried.
> - **#3 VX.tsv / DQ-series reconcile** — ⚠️ **STILL OPEN.** VX is FROZEN; the `0.117%` row inside it was deliberately left (a frozen ledger stays frozen; correcting one row implies the rest are maintained).
> - **#6-#7 Will-decision + hygiene** — unchanged, still open.
>
> 🔑 **The generalisable defect: a file can contain its own refutation and pass every check, because nothing compares a document's header to its footer.** Disposition ④ reversed recommendation #5 in the same edit that wrote it, and both have coexisted for 39 days. `[[finding_a_file_that_examples_its_own_structure_is_ambiguous]]` · `[[finding_summary_section_merges_what_the_body_separates]]`
>
> **⇒ WORK THE RECONCILE ABOVE, NOT THE LIST BELOW. The list is retained verbatim as the record of what was recommended, not as instructions.**

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
