# PROFILE REFRESH DRAFTS — BOND · BROCK
**Reader:** DAEDALUS fan-out reader P1 · **Date:** 2026-09-17 (Thu) · **Review period:** 2026-09-01 00:00 → now
**Scope:** full profile refresh drafts (PART A) + refresh reports (PART B) for two heavy desks.
**Status:** READER DRAFT. **Not** `profiles/BOND.md` / `profiles/BROCK.md` until DAEDALUS re-verifies. Read-only pass; nothing outside this file was written.

**Method:** every file/section named below was opened at HEAD and carries a `path:line` anchor. Verdict vocabulary: **TRUE-STILL / REFUTED / CANNOT-EVALUATE / NOT-ADJUDICATED**; **NOT-SEEN** where an instrument cannot see a count.

---
---

# ██ DESK 1 — BOND ██

# PART A — REFRESHED PROFILE (draft, ready for re-verification)

# Agent Profile — BOND

**Profile vintage:** 2026-09-17 (reader draft, DAEDALUS re-verification pending)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** 1-reader solo read at HEAD (fan-out leg P1 of the 2026-09-17 refresh wave)
**Sources read:** `CLAUDE.md` (250 ln / 36,493 B, whole) · `STATUS.md` (146 ln / 23,401 B, whole) · `thesis/{THESIS.md,CHANGELOG.md,PREDICTIONS.tsv}` · `TRADE.md` · `PROTOCOL.md` · `MEMORY.md` (head) · `SCRATCH.md` · `AUDIT.md` (head) · `NEXUS_BRIEF.md` (head) · `workbook/{KB,VX,FLOW,SCHEMA}.tsv` · `docket/CATALYSTS.tsv` · `registry/{corrections_receipts,f2_reads}.tsv` · `monitors/` (6 `.md` headers + 12 `.py` docstrings + 3 `.tsv`) · newest `analysis/` (9/14–9/17) · `outbox/` filename census · `git log --after=2026-09-01 -- AGENTS/BOND/`. **SKIPPED:** `data/*.csv` (auction history), `domain/sources/*.pdf` (KBRA), the 60+ rotated `domain/sources/*STATUS_archive*` files, 200+ `inbox/WALTER/processed/`.
**Staleness:** refresh when ANY fires — (1) `AGENTS/BOND/thesis/THESIS.md:3` `Version:` leaves **1.2.7**; (2) `AGENTS/BOND/TRADE.md:3` `Last Updated:` leaves **2026-09-09** (the posture re-base); (3) `python3 scripts/read_cap_check.py --agent BOND` returns **rc≠0**; (4) the count of `AGENTS/BOND/monitors/*.py` leaves **12**; (5) `AGENTS/BOND/STATUS.md` composite leaves **12/35**; or (6) **> 45 days** from the vintage above ⇒ **2026-11-01**.

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

## 1. Identity
US **bond-market structure as a transmission mechanism**: Treasury auction health (composition / cover / dealer take), corporate issuance (HY/IG), dealer positioning (FR2004), curve shape, credit-spread structure, credit-leads-equity (Hamilton ~3mo). **Class:** Market (`FLEET_MAP.tsv` owns the grade; not restated). **Spawnable by:** PROME / Will.

**Scope is now THREE layers, and two were added after the 6/29 profile:**
1. **Core** (`CLAUDE.md:65-71`) — auctions, issuance, dealer inventory, curve, credit spreads, issuance-freeze thresholds, credit→equity lead.
2. **Coverage extension**, Will-approved 6/27, **integrated 7/1** (`CLAUDE.md:72-74`) — **MBS / housing finance + GSE capital**, **FHLB advances** (the 2023-SVB regional-bank funding backstop, coordinated with REGINALD), **Eurozone rates** (bund curve + ECB shocks, RATES leg only; LIQUID owns the EU credit leg).
3. **Sovereign-credibility instrument set**, Will-ruled in-session 2026-08-10 (`CLAUDE.md:75`) — **30Y term-premium decomposition** (ACM 10Y TP + KW `THREEFYTP10`) + **DM sovereign-spread cross-section** as a standing series at BOND's own primaries (tool: `monitors/dm_cross_section.py`). Three **named declines** live in the same line so nobody re-proposes them: gold/real-yield decoupling → MIDAS · auction **tails** → nobody, retired for cause · US sovereign CDS → unowned, re-test **2026-12-01**.

**Transmission (`CLAUDE.md:91-110`, `thesis/THESIS.md:183-195`):** sits between LIQUID (plumbing/funding) and ZHAO (foreign demand). Sends auction-composition-failure→LIQUID 🔴, cover-marker→LIQUID+ZHAO 🟠, credit-equity lead→HENRY 🟠, issuance-freeze→REGINALD 🔴, auction weakness→ZHAO 🟠; **↔ SAM** (JGB long-end / BOJ / yen ↔ US term-premium, channel 6) and **↔ REGINALD** (FHLB) are carried in THESIS:194-195 only. Consumes LIQUID (SOFR/repo, energy-HY OAS), ZHAO (TIC), HENRY/HAWK (vol, geopolitics). One-source-of-truth cessions: energy-HY OAS→LIQUID · TIC→ZHAO · rate-expectations→HENRY · bank-level credit→REGINALD · private credit/BDC→BROCK · USD/JPY→SAM · Brent→BRENT · VIX→VIOLET (`STATUS.md:42` keeps NO copy of the last three).

**What it's for:** *"Is the bond market still* ***clearing****, or starting to* ***break****?"* — and the load-bearing distinction that answers it is **"expensive, not broken."**

## 2. File anatomy (where the richness lives) — HEAVY, ~431 tracked files, 7 layers
| File | Holds | Richness? |
|---|---|---|
| `STATUS.md` (146 ln / **23,401 B = 72% of budget**) | Regime one-liner · 17-row live dashboard with `[CONF src date]`/`[STALE]` tags · **Gate-distance table** (the decision numbers, recomputed never carried) · FR2004 block · 7-vector convergence matrix w/ **`Rolls up (workbook/VX.tsv)` column** · prediction scoreboard · Trade Interface · 4-category Exit/Falsification · catalyst twin · BOTTOM LINE | **live state — the single densest surface** |
| `thesis/THESIS.md` (199 ln / **65,206 B**, v1.2.7) | "expensive, not broken" core · **6 transmission channels** · `INSTRUMENT CONTEXT` block (the 30Y ≥5.00% history that cuts AGAINST the thesis, `:22-37`) · REGIME-LABEL CONTESTED banner (`:6-16`) · full EXIT/FALSIFICATION (`:91-131`) · KEY THRESHOLDS (`:135-145`) · scoreboard · cross-agent links | **durable thesis — and the fleet's most self-adversarial one** |
| `thesis/CHANGELOG.md` | v1.2.7→v1.1.x, every entry **old view → new view** with the bump rule stated | version history |
| `thesis/PREDICTIONS.tsv` (5 live rows `BND-25`→`BND-29`, 11 cols incl. `If_Falsified_Action`) + `thesis/archive/PREDICTIONS_resolved_*.tsv` ×3 (crc-stamped) | falsifiable rows with **named basis** and pre-registered if-FALSE branches. Resolved tally **13 TRUE · 11 FALSE · 1 VOID** (`STATUS.md:83`) | **a STRONGEST dimension** |
| `TRADE.md` (89 ln / 14,334 B) | **RE-BASED 2026-09-09 to POSTURE + GATES ONLY — no marks** (`:3`). The view (4 numbered paras) · add-gate table + **breach protocol** · Active/Legacy · Reactivation Matrix · Cross-Agent Deps · dated Next Review | trade truth (posture; construction is TERRY's) |
| `workbook/KB.tsv` (**297 data rows**, 13 col) | canonical record; Admiralty `Conf` A1–F6 · `Epistemic` EMPIRICAL/ESTIMATE/ASSUMPTION · `Status` lifecycle · `Stale_By` | permanent record |
| `workbook/VX.tsv` (**20 vectors**) | `VX-BND-01`→`-20`; 7 roll up into the composite, the rest are feed-not-double-count or explicitly **"Tracked OUTSIDE the composite"** (`STATUS.md:76`); `VX-BND-09` RETIRED | permanent record |
| `workbook/FLOW.tsv` (**15 pathways**) | `FL-BND-01`→`-15` w/ Speed + Status ∈ {LATENT, WATCH, CONFIRMED, **CONTRADICTED**, CONDITIONAL, FIRED}. `FL-BND-15` = "the channel that actually fired, and NOT the one the position expresses" | **permanent record; the CONTRADICTED token is unusual and load-bearing** |
| `docket/CATALYSTS.tsv` (**24 data rows**, 8 col, **24,049 B = 74% of budget**) | source of truth for dated catalysts; `date_class` ∈ resolved/confirmed/recurring/watch/hard | forward state |
| `monitors/` — **6 `.md` + 12 `.py` + 3 `.tsv` + `fixtures/`** | see §2b. `AUCTION_HEALTH.md` (44,774 B) is **canonical for the `I'` grading bars** (`STATUS.md:98` §GRADING BASIS) | **tooling layer — the single biggest change since 6/29** |
| `registry/f2_reads.tsv` · `registry/corrections_receipts.tsv` | per-op F2 buyback read ledger (15 col, built 9/17) · R1 corrections receipts (boot 7b) | ledgers |
| `NEXUS_BRIEF.md` (310 ln / **66,985 B**) | steady-state rates feed for NEXUS; **RE-PIN block at the top supersedes everything below it** (`:5`) | cross-agent channel — **EXISTS now (it did not on 6/29)** |
| `PROTOCOL.md` (11,726 B) | mail/refresh SOP + **§DELIVERY MODEL declared 2026-08-27** + per-source data-pull recipes (FR2004 series breaks, H.4.1 custody, TA_WS) | durable method |
| `MEMORY.md` (56 ln / **29,072 B = 89% of budget 🟠**) | durable BOND-local learnings (boot read 3) | durable — **rotate-tier, see §7** |
| `SCRATCH.md` (9,727 B) · `RECEIPT.md` · `LAST_COMPLETION.md` | session handoff (must be executable COLD) · run receipt · legacy | ephemeral |
| `AUDIT.md` (32,927 B) | the 2026-08-21 Will-tasked boot-document audit, incl. **dismissed candidate findings** | one-off audit record |
| `analysis/` (26 files) · `setups/` · `proposals/` · `research/` | per-event grade/pre-print records — **the pre-print-before-the-print discipline lives here** | deep analysis — read the newest 2–3 only |
| `data/*.csv` (73–83k) · `domain/sources/` (~50 rotated STATUS/CATALYSTS blocks + KBRA PDFs) · `archive/` (4 crc-stamped snapshots) · `inbox/WALTER/processed/` (~200) | raw + rotated history, each crc-stamped in its own header | SKIP |

### §2b. The `monitors/` tool layer (12 scripts — grade this as a dimension in its own right)
| Script | Wired into | What it is |
|---|---|---|
| `docket_check.py` | **boot 5** (`CLAUDE.md:28`) | v2 rebuild 8/27. Diffs TreasuryDirect `upcoming` vs CATALYSTS **keyed on CUSIP**. **rc0 ≠ "window covered"** — read the `VERIFIED ONLY THROUGH` line; names the ~5-day BLIND SPAN and refuses to adjudicate it. 17 assertions / 11 fixtures |
| `boot_recompute.py` | **boot 6** (`CLAUDE.md:29`) | cache-busted recompute of LEVELS **and DERIVED** stats with aggregation method stamped; prints `TRADE.md`'s gate table; drift-checks the **boot-unread** surfaces (`TRADE.md`, `monitors/*.md`, `NEXUS_BRIEF.md`); runs `check_fr2004()`; invokes `buyback_f2.py`. `rc=1` is NOT a pass |
| `closeout_check.py` | **closeout 16** (`CLAUDE.md:44`) | THE single closeout invocation — 3 checks, 1 fetch, 1 rc (0 clean / 1 finding / 2 fetch-failure, **2 is not a pass**). `--selftest` = 35 fixtures that are real shipped defects |
| `assertion_check.py` | component of 16 | stale-**assertion** sweep for claims with **no number in them**: DIRECTIONAL · FILE-STATE · EXPIRED · CAPABILITY. Reads ISO **and** slash dates; resolves bare `m/d` BACKWARD; 27 fixtures |
| `kb_lint.py` | component of 16 (part 0/3) | workbook conformance vs `SCHEMA.tsv` + `AGENTS/VOCABULARIES.tsv` + the PREDICTIONS `Status` enum (**OPEN·TRUE·FALSE·VOID**, declared 8/21 because it was declared nowhere) |
| `grade_auction.py` | per-event | grades a print or pre-freezes the BARS; per-tenor benchmarks, median **and** mean, margins on every leg, residual branch, **refuses a gate below n=6**, **computes no tail** |
| `buyback_f2.py` + `registry/f2_reads.tsv` | boot, via `boot_recompute` | **BUILT 2026-09-17** (DOCKET L401). The standing **class carrier** for the per-op F2 read — keyed to the operation SCHEDULE, not to a date, because a RESOLVED docket row cannot drive the next op |
| `fr2004_fetch.py` | per-pull | NY Fed primary-dealer fetch; **resolves the SBN2015/SBN2022/SBN2024 series breaks at runtime** — the fix for a 6-week false "access gap" |
| `cdx_proxy.py` | `VX-BND-06` | free HYG/IEF + LQD/IEF proxy, explicit about what it cannot see (true CDX is paywalled) |
| `dm_cross_section.py` | 8/10 scope claim | 4 primary legs (FRED · ECB SDW · BoE IADB · MOF) — built 9/1 to make the "standing series" actually standing |
| `matrix_v2_base_rate.py` | one-off/periodic | per-tenor out-of-sample base-rating of the `I'` test |
| `watchers.py` | 8/20 | the **missing-watcher** class: "a state change with NO PUBLISHER" |

*The key question this answers: when I grade section X, which file do I actually read?* — **and for BOND the answer is increasingly a SCRIPT, not a document.**

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | `thesis/THESIS.md:41-90` CORE + `TRANSMISSION CHANNELS` (6) + `ACTIVE EPISODE` + `FLOW.tsv` | "expensive, not broken"; channels carry Mechanism + **regime-level posture with no dated numbers** (`:71`); episode-not-break framing; a **third explanation deliberately held open** (basis-trade withdrawal, `:83`) | **exemplary** |
| Convergence / scoring | `STATUS.md:61-78` | 7 headline vectors, cols `# \| Vector \| Score \| Status \| **Rolls up (workbook/VX.tsv)** \| Key Signal \| Upgrade Trigger`; composite **re-summed and the arithmetic printed** (`:74`); `Tracked OUTSIDE the composite` line for the 5 non-rolling vectors (`:76`); **an OPEN MIRROR DIVERGENCE is declared rather than silently reconciled** (`:78`) | **strong — the roll-up column now does the independence work** |
| Invalidation / exit | `STATUS.md:95-108` (4 categories) + `thesis/THESIS.md:91-131` (full) + `TRADE.md:21-37` (gates) | every line carries a number **and** a session/date count; **PAIRED kill** with a dated pairing instrument (`STATUS.md:97`); **dual-print of OLD and NEW composition tests** while a ruling beds in; explicit "⛔ the ADD re-arm runs on the OLD, STRICTER test — never loosen an add gate as a side effect of a definition reconcile" (`:99`) | **exemplary — best-in-fleet on this dimension** |
| Thresholds | `CLAUDE.md:114-129` + `THESIS.md:135-145` + `VX.tsv` bands + `monitors/AUCTION_HEALTH.md` §GRADING BASIS | durable docs carry the RULE, never a tenor's instance; live values point to STATUS; **retired thresholds stay visible with the reason** (auction tail, struck-through in both tables); secular-norm caveats baked in (BTC 3.0→2.5 GAO) | **conformant→exemplary** |
| Predictions | `thesis/PREDICTIONS.tsv` + 3 crc-stamped archives + `STATUS.md:80-83` | 11 cols incl. `If_Falsified_Action`; **every row registers its own named basis and base rate before the number exists**; resolution states the margin on every leg | **a STRONGEST dimension** |
| Cross-agent routing | `CLAUDE.md:91-110` matrix + `THESIS.md:183-195` + `TRADE.md:68-79` + `NEXUS_BRIEF.md` + `outbox/` (47 live + 15 `delivered/`) | condition→target→priority 🔴/🟠; **outbox 🔴-acute-only** restraint; steady state now goes to `NEXUS_BRIEF.md`; `outbox/delivered/` created 8/20 and verification is **by CONTENT, not filename** (`CLAUDE.md:176-179`) | **conformant — but the charter table under-states live routes, see §4** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)
| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/THESIS.md:91-131` §EXIT/FALSIFICATION | the whole duration-short thesis; 4 categories | `Version:` + `Last Updated:` at `:3-4`, plus per-clause dated `⚠️ RE-SPECIFIED`/`CORRECTED` riders | prose verdict + a ⚠️/🔴 rider naming the date and the ruling record |
| `STATUS.md:95-108` §Exit/Falsification | the compact live mirror of the above | `**Last session:**` at `:4` | `🔴🔴 / 🔴 / ⛔` + explicit `NOT FIRED` / counter value |
| `STATUS.md:44-55` Gate-distance table | the TLT-put **add** gates (entry-side) | "recomputed every boot, never carried" caption | `🔴 THROUGH by Nbp` / `🟡 Nbp` / `🟢` |
| `TRADE.md:21-37` add-gate table + breach protocol | the position's add authority | `**Last Updated:** 2026-09-09` at `:3` | `🔴 LEVEL LEG THROUGH` / `🟠 UNFIRED, not dead` / `❌ RESOLVED, DID NOT FIRE` |
| `thesis/PREDICTIONS.tsv` `Status` col | each registered claim | `Date_Made` / `Timeframe` / `Date_Resolved` cells | enum **OPEN·TRUE·FALSE·VOID** (declared 8/21, lint-enforced) |
| `workbook/VX.tsv` `Threshold_Yellow`/`_Red` | per-vector state | `Last_Updated` cell | score + `Last_Signal` |
| `workbook/FLOW.tsv` `Status` | a transmission channel's existence | `Last_Updated` cell | `LATENT/WATCH/CONFIRMED/**CONTRADICTED**/CONDITIONAL/FIRED` — `FL-BND-09` reads "CONTRADICTED — do not cite without this note" |
| `monitors/AUCTION_HEALTH.md` §GRADING BASIS + §3d | the `I'` bars and the downgrade counter | `**Last Updated:** 2026-09-17` | frozen per-tenor bars + counter integer |
| `monitors/RETIRED_TOKENS.tsv` | retired thresholds/tokens that must never fire again | `Retired_On` col | row presence + `Guard_Words` |

## 4. Deviations from standard (+ why)
**BETTER than blueprint — five, and they are why this desk reads as an exemplar:**
1. **Boot⇄closeout is a declared symmetric read→write pairing** (`CLAUDE.md:18`): STATUS r1→w9, SCRATCH r2→w13, PREDICTIONS r4→w10, CATALYSTS r5→w12. Plus a **mirror-consistency check** (step 17) and a **composite re-sum** (step 9) whose arithmetic is printed on the surface.
2. **Invocation, not detection, is treated as the gap.** Every guard is *wired into a tool that boot/closeout already runs*, explicitly because "conditional self-assessed steps get skipped" (`CLAUDE.md:29`, `:44`). Three separate rc-contract corrections are documented in-charter with the failure that earned each.
3. **A retired instrument keeps its tombstone.** The auction tail is struck-through **in both threshold tables** with "UNSCOREABLE BY CONSTRUCTION" and a do-not-revive clause (`CLAUDE.md:125`, `THESIS.md:145`, `STATUS.md:108`), plus a machine-readable `monitors/RETIRED_TOKENS.tsv`.
4. **Pre-registration before the print, committed with a timestamp.** The 9/15 20Y-R ceiling was committed at **10:06:44 ET before the auction existed** precisely so a bearish print could not be promoted afterwards (`CHANGELOG.md:21`).
5. **Rulings that go against the desk's own book are recorded as such.** The `I'` PAIRING recommendation was BOND's own, made against its own position, and the charter says so (`THESIS.md:100`); the 8/27 dealer-leg question was **halted and asked rather than self-ruled** because answering it would make BOND's own bear thesis easier to confirm (`THESIS.md:124`).

**DEBT (real, verified at the artifact):**
- **`MEMORY.md` is at 89% of the read-cap budget** (29,072 B / 32,550) — rotate-tier, not rotated. BOND's own `SCRATCH.md:11` already carries the receipt: *"MEMORY 89% — rotate-tier, NOT rotated; next session that adds to MEMORY must rotate first."* Declared, not fixed.
- **BOND has ZERO rows in `PROME/registry/READS.tsv`** — so `read_cap_check --agent BOND` runs on the charter **heuristic**, and says so: *"this desk has no declaration … 'clean within what the scan found', NOT a clean bill."* BROCK (a peer) declared 16 rows on 9/12. Cheap, and it is the difference between an attested perimeter and a guess.
- **The `CLAUDE.md` FILES table (`:224-250`) has fallen behind the tree.** Absent: `NEXUS_BRIEF.md`, `PROTOCOL.md`, `AUDIT.md`, `registry/`, `analysis/`, `setups/`, `proposals/`, `research/`, and 4 of the 12 monitor scripts (`buyback_f2.py`, `dm_cross_section.py`, `watchers.py`, `matrix_v2_base_rate.py`). `NEXUS_BRIEF.md` in particular is a 66,985 B live cross-agent surface that the charter names only inside a drift-check parenthesis (`:29`).
- **The charter's CROSS-AGENT SIGNALS table under-states live routing.** `CLAUDE.md:91-110` lists 4 outbound targets (LIQUID/HENRY/REGINALD/ZHAO) and 4 inbound (LIQUID/ZHAO/HENRY/HAWK). The live `outbox/` carries packets to **SAM, MIDAS, RED, TERRY, ORACLE, WALTER, VIOLET, LABOR, ZHAO, HENRY, LIQUID, NEXUS**; `THESIS.md:194-195` adds SAM and the REGINALD-FHLB leg. The topology lives in three places and the charter's copy is the thinnest.
- **`CLAUDE.md` §EXIT RULES (`:151-160`) is still generic template text** ("Conditions that completely invalidate the thesis. 1-2 hard stops") while the real four-category apparatus lives in STATUS/THESIS. Harmless *because* the real thing is elsewhere and pointed at — but a cold reader landing on the charter gets a template.
- **`monitors/CDX_CASH_BASIS.md` lags STATUS on its own vector.** Monitor header: *"Last Updated: 2026-08-27 … HYG/IEF 0.8567, z20 +0.82."* `STATUS.md:70`: *"HYG/IEF 0.8585, z20 +1.28 [9/8, STALE]."* Both are marked, neither is wrong, but the monitor doc is 21 days behind the live surface it exists to explain.

**Floor-not-ceiling note:** BOND's rich local form (the `Rolls up` column, the `Tracked OUTSIDE the composite` list, the `date_class` docket column, the dual-print convention) is **not** blueprint divergence to be corrected. It is the blueprint expressed better.

**Grounding errors a prior pass made — do NOT re-apply:** the 6/29 profile's headline debt *"NEXUS_BRIEF.md ABSENT"* is **REFUTED** — it exists, 310 ln, refreshed 2026-09-17 (`NEXUS_BRIEF.md:3`). *"CLAUDE.md still treats HERMES as a live mail carrier"* is **REFUTED** — zero HERMES occurrences in `CLAUDE.md` or `PROTOCOL.md`. *"MATRIX_V2 approved-but-not-implemented"* is **REFUTED** — adopted and executed 2026-08-27 on Will's ruling and **fired for the first time on 2026-09-15** (`CHANGELOG.md:17-27`).

## 5. Load-bearing context / DO NOT TOUCH
- **"Expensive, not broken."** The term-premium-digestion (slow, absorbed) **vs** demand-hole (fast, mechanical, systemic) axis IS the thesis. Do not flatten it.
- **Threshold-vs-mechanism discipline.** `[[finding_threshold_vs_mechanism]]` is wired into closeout 10. A threshold can fire while the mechanism holds — the 9/15 20Y-R is the canonical instance (indirect lowest ever recorded on a 20Y **while** direct set a modern-series record and BTC held 2.57). Any edit that collapses these two into one verdict breaks the desk.
- **Durable docs carry NO live values.** `CLAUDE.md`, `THESIS.md` and `TRADE.md` deliberately point at STATUS. Do not "helpfully" backfill numbers — `THESIS.md:17` and `:35` document what happens when someone does (a retracted figure survived behind a disclaimer that stopped readers checking).
- **Source tags are mandatory on the dashboard.** Every value `[CONF src date]` or `[EST]`; `[STALE date]` beats carried-forward.
- **Composite re-sum, 7 headline vectors only.** `VX-BND-08`…`-16` roll up; `VX-BND-15/17/18/19/20` are explicitly outside the composite. Do not fold them into the /35.
- **⛔ The TLT-put ADD re-arm runs on the OLD, STRICTER conjunctive test** (`STATUS.md:99`, WQ-99 Will 9/1) even though the kill now runs on the NEW `I'` test. This asymmetry is deliberate: *"never loosen an add gate as a side effect of a definition reconcile."*
- **The auction TAIL is retired and NOT revivable** — TreasuryDirect publishes no when-issued. Wire-reported tails are `[med-conf]` and **may never fire anything** (`STATUS.md:108`). Do not restore a tail-keyed gate anywhere.
- **Dealer take >18% is contrarian-BULLISH, and dealer is DROPPED as a bearish kill criterion** (Will-ruled 8/27). Backtest-grounded, counterintuitive; do not "restore" a dealer-stuffing bearish trigger.
- **`rc=0` semantics differ per tool and are load-bearing.** `docket_check` rc0 = "nothing ACTIONABLE", **not** "the window is covered" — read the `VERIFIED ONLY THROUGH` line. `closeout_check` rc2 = fetch failure = **not a pass**. `boot_recompute` rc1 = unguarded drift = **not a pass**.
- **Percentages are of COMPETITIVE ACCEPTED, and bars are derived PER TENOR at grade time.** Never reuse another tenor's numbers (the 7Y-hardcoded-into-every-tenor defect, corrected 8/18).
- **outbox 🔴-acute-only** + **WALTER lane at boot vs general inbox as a separate task** (`CLAUDE.md:48`) — protocol-deliberate.
- **`outbox/delivered/` verification is by CONTENT, not filename.** A filename scan flagged 7 of 22 as orphans; HENRY demonstrably had one of them under a different filing convention (`CLAUDE.md:176-179`).
- **STATUS/CATALYSTS rotation is verbatim + crc32-stamped, never deletion.** `STATUS.md:6` asserts *"NOTHING HAS EVER BEEN DELETED FROM IT"* and names the 160,077 B pre-split snapshot with its crc. Preserve the crc convention on any rotation.

## 6. Maturity snapshot
Grade + confidence live in `FLEET_MAP.tsv` (**not restated here**). What this read establishes about the L5 legs:
- The **9/1 FLEET_MAP `Gaps` cell is materially out of date on its own headline blocker**: it says *"NO declared byte tier — STATUS 160,077 B / 250 ln = 492% of the read budget … BOND cannot read its own STATUS whole once."* At HEAD, STATUS is **23,401 B / 146 ln = 72% of budget**, with a declared rotation banner and crc'd archive (`STATUS.md:6-7`). **That leg is DONE.** Re-cut the row.
- The residual `Next_upgrade` legs that survive: **LEDGER_GLOB** — `AGENTS/BOND/workbook/LEDGER_GLOB` **does not exist** (verified), so the root closeout-1c-bis ledger nudge cannot run for this desk; and **a `READS.tsv` declaration** (0 rows).
- New since 9/1 and NOT yet on the map: the F2 per-op carrier + `registry/f2_reads.tsv` (9/17), `dm_cross_section.py` (9/1), `MEMORY.md` at rotate-tier.
- The old profile's `conf M` reasoning ("the cross-agent-routing dimension has a live structural hole" = NEXUS_BRIEF absent) **no longer holds** — the hole is closed.
Work queue → `upgrades/BOND_CARD.md`; the 8/20 3-reader review → `upgrades/BOND_REVIEW_2026-08-20.md` + `_reader_raw.md`.

## 7. Open questions / comprehension gaps
1. **Is the TLT Sep-30 77P leg still live at HEAD?** `TRADE.md:11` marks it 25× at **$0.035** vendor mid on 9/9 with expiry **9/30** — thirteen days out at this read. Position truth is off-repo (Will/broker). **NOT-ADJUDICATED** by design; do not resolve from STATUS or TRADE (root rule #4 / §Position truth).
2. **Does the 9/18 FR2004 weekly join land?** It is the desk's declared critical path (`STATUS.md:144`): a live `I'` fire from 9/15 sits on the far side of an **unbuilt** pairing instrument, so the thesis kill is currently **UNEVALUABLE with one leg lit**. Everything about BOND's falsification posture turns on tomorrow.
3. **WQ-246 — "sustained" has no session count.** The add-gate's level leg has been through for 4 published sessions and the desk has correctly refused to pick the count *after* knowing the answer. Open with Will. Until ruled, gate (a) **cannot be graded** and silently converts to "never add."
4. **The declared MIRROR DIVERGENCE is in its 9th session un-reconciled** (`STATUS.md:78`): `VX-BND-05`=4 and `VX-BND-16`=4 in `workbook/VX.tsv` vs matrix rows scoring 3 and 2. BOND states the direction (components HOTTER ⇒ the divergence UNDER-states risk) and flags rather than reconciles. Is that the right disposition at 9 sessions, or is it now debt?
5. **Is `AUCTION_HEALTH.md` (44,774 B) at risk of becoming an unreadable canon surface?** It is cited as canonical for the `I'` bars (`STATUS.md:98`) but is not a declared boot-read, so no cap binds it. FALSE-POSITIVE-CANDIDATE as a read-cap breach; a real question as a *comprehension* surface.
6. **Where does the `WATCH_DATES.tsv` / `watchers.py` layer get invoked?** Both exist; I could not locate an invocation site in `CLAUDE.md`'s boot or closeout steps. **CANNOT-EVALUATE** — would need `boot_recompute.py`'s call graph read in full.

---

# PART B — REFRESH REPORT: BOND

## B1 · Old profile (`profiles/BOND.md`, body 2026-06-29, 80d) — section-by-section disposition
| Old §  | Claim as written | Verdict | Evidence / locator |
|---|---|---|---|
| Banner `:3` | "STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01) … Refresh checkpoint: **2026-09-15**" | **CARRIED-VERIFIED, and the checkpoint is BLOWN** | checkpoint date 9/15 < today 9/17; body still 6/29 |
| Banner `:5` | "current truth = `upgrades/BOND_REVIEW_2026-08-20.md`" | CARRIED-VERIFIED (file exists) | `AGENTS/DAEDALUS/upgrades/BOND_REVIEW_2026-08-20.md` |
| §1 Identity | domain list, LIQUID↔ZHAO position, cessions | **UPDATED** — three scope layers now, not one; MBS/FHLB/EU-rates integrated 7/1; sovereign-credibility set ruled 8/10 | `CLAUDE.md:72-75` |
| §2 `STATUS.md (108 ln)` "composite 11/35" | file anatomy row | **UPDATED** — 146 ln / 23,401 B, hot/cold split + crc'd rotation; composite **12/35**, 15th consecutive | `STATUS.md:6`, `:73` |
| §2 `thesis/THESIS.md (v1.0, 115 ln)` | " 5 transmission channels" | **UPDATED** — **v1.2.7**, 199 ln / 65,206 B, **6 channels**, + INSTRUMENT CONTEXT + CONTESTED-label banner | `THESIS.md:1`, `:60-69`, `:22`, `:6` |
| §2 `PREDICTIONS.tsv (10 rows)` | BND-01..10 | **UPDATED** — 5 live rows `BND-25`→`-29`, 3 crc'd archives, tally **13 TRUE / 11 FALSE / 1 VOID**; `Status` enum now declared + lint-enforced | `PREDICTIONS.tsv:2-6`; `STATUS.md:83`; `CLAUDE.md:244` |
| §2 `TRADE.md (78 ln)` "Active/Legacy + Reactivation Matrix" | trade truth | **UPDATED** — 89 ln, **RE-BASED 2026-09-09 to posture+gates ONLY, no marks**, at Will's direction after a whole-file read found it contradicted in six places | `TRADE.md:3` |
| §2 `KB.tsv (56 rows)` | canonical record | **UPDATED** — **297 data rows** | `workbook/KB.tsv` |
| §2 `VX.tsv (16 vectors)` | 7 headline + 9 sub | **UPDATED** — **20 vectors**; `VX-BND-09` RETIRED; 5 explicitly outside the composite | `workbook/VX.tsv`; `STATUS.md:76` |
| §2 `FLOW.tsv (10)` | pathways | **UPDATED** — **15**, and the status enum grew a **CONTRADICTED** token | `workbook/FLOW.tsv:10,14` |
| §2 `CATALYSTS.tsv (8)` | forward catalysts | **UPDATED** — 24 data rows / 24,049 B (74% of budget) | `docket/CATALYSTS.tsv` |
| §2 `monitors/ … SKIM not read` | "live monitor docs + free CDX-basis proxy script" | **UPDATED — this is the single biggest change since 6/29.** 6 `.md` + **12 `.py`** + 3 `.tsv` + `fixtures/`; 4 scripts are wired into boot/closeout with declared rc contracts and selftest fixture counts. No longer skimmable | `CLAUDE.md:28-29`, `:44`, `:242-247`; §2b above |
| §2 `proposals/MATRIX_V2_DRAFT … implementation PENDING (Packet 9 paused)` | design | **REFUTED** — adopted + executed 8/27 on Will's ruling; **fired for the first time 2026-09-15** | `CHANGELOG.md:17-27`; `THESIS.md:121` |
| §3 Convergence row: "**no Independence column**" | handle gap | **UPDATED/partly REFUTED** — the matrix now carries a `Rolls up (workbook/VX.tsv)` column naming each headline vector's constituents, plus a `Tracked OUTSIDE the composite` line. The word "Independence" is still absent; the function is present | `STATUS.md:63`, `:76` |
| §3 Cross-agent row: "**no NEXUS_BRIEF**" | gap | **REFUTED** — `NEXUS_BRIEF.md` exists, 310 ln / 66,985 B, refreshed **2026-09-17** | `NEXUS_BRIEF.md:3` |
| §4 debt "NEXUS_BRIEF.md ABSENT … blocks L5" | debt | **REFUTED — DROPPED** | as above |
| §4 debt "CLAUDE.md still treats HERMES as a live mail carrier (L82/161/164)" | debt | **REFUTED — DROPPED.** Zero HERMES occurrences in `CLAUDE.md` or `PROTOCOL.md` | `grep -n HERMES AGENTS/BOND/CLAUDE.md AGENTS/BOND/PROTOCOL.md` → empty |
| §4 nuance "10 predictions exist, 6 resolved" | count correction | **SUPERSEDED — DROPPED** (new corpus, new tally) | `STATUS.md:83` |
| §4 "MATRIX_V2 status nuance … L4 rests primarily on TRADE.md" | grade reasoning | **UPDATED** — MATRIX_V2 is now live *and* fired; TRADE.md is now posture-only, so the "feeds proposals" leg rests on the gate table + breach protocol rather than on position rows | `TRADE.md:21-37` |
| §5 all 8 DO-NOT-TOUCH bullets | load-bearing | **7 CARRIED-VERIFIED, 1 UPDATED.** The "composite re-sum" bullet carried forward verbatim (`STATUS.md:74`); the "MATRIX_V2 dealer-criterion" bullet is now **ruled canon**, not a finding — dealer is dropped as bearish, >18% contrarian-bullish | `CLAUDE.md:120`; `THESIS.md:102` |
| §6 "L4 (conf M) … held below L5 on (a)–(e)" | maturity | **UPDATED** — (a) NEXUS_BRIEF and (c) HERMES are CLOSED; (d) MATRIX_V2 is CLOSED; (b) is partly closed; (e) is now a **default-zero instrument that can never fire** (YEYOU retired 9/5, WQ-181 ②). New residual legs: LEDGER_GLOB absent, READS.tsv undeclared, MEMORY at rotate-tier | this file §6 |
| §7 Q1 "coverage-EXTENSION SIG sits UNPROCESSED" | biggest drift | **REFUTED — DROPPED.** Integrated 7/1 and visible in `CLAUDE.md` scope, `THESIS.md:73` and vectors `VX-BND-17/18/19` | `CLAUDE.md:72-74` |
| §7 Q2 "is the live TLT-put leg still open?" | open Q | **CARRIED** (re-framed to the Sep-30 77P leg) | `TRADE.md:11` |
| §7 Q3 "will Packet 9 ever un-pause?" | open Q | **REFUTED — DROPPED** (MATRIX_V2 live) | `CHANGELOG.md` |
| §7 Q4 "BND-10 / BND-02 / BND-04 DUE-flagged, unresolved" | open Q | **RESOLVED — DROPPED** (all in `thesis/archive/PREDICTIONS_resolved_BND-01_to_BND-17.tsv`) | archive files present |

**Tally:** 8 CARRIED-VERIFIED · 12 UPDATED · 7 DROPPED-as-REFUTED/RESOLVED.

## B2 · File tree at HEAD (`git ls-files AGENTS/BOND/` = **431** tracked files)
| Cluster | Count | Note |
|---|---|---|
| Root `.md` | 11 | CLAUDE · STATUS · SCRATCH · MEMORY · TRADE · PROTOCOL · RECEIPT · AUDIT · NEXUS_BRIEF · BND11_REFUNDING_PREREG · LAST_COMPLETION |
| `thesis/` | 3 + 3 archives | THESIS · CHANGELOG · PREDICTIONS.tsv + `archive/PREDICTIONS_resolved_*` ×3 |
| `workbook/` | 4 | KB · VX · FLOW · SCHEMA |
| `docket/` | 1 | CATALYSTS.tsv |
| `monitors/` | **22** | 6 `.md` + 12 `.py` + 3 `.tsv` + `fixtures/buyback_20260910.json` |
| `registry/` | 2 | corrections_receipts · f2_reads |
| `analysis/` | 26 | newest: `2026-09-17_PREPRINT_TIPS-R_91282CRE3_SEP-grade_F2-carrier.md`, `2026-09-17_grade_BND-25_BND-26_on_the_9-16_H15_cells.py` |
| `outbox/` | 47 live + 15 `delivered/` | |
| `inbox/WALTER/processed/` | ~200 | pending lane **EMPTY** (0 unprocessed) |
| `domain/sources/` | 46 | rotated STATUS/CATALYSTS blocks (each crc-stamped) + 2 KBRA PDFs + LIQUID-donated frameworks |
| `archive/`, `data/`, `setups/`, `proposals/`, `research/` | 4 / 5 / 3 / 2 / 2 | |

**Byte sizes of the boot-read surfaces** (`read_cap_check --agent BOND`, budget 32,550 B):
| Surface | Bytes | % budget | Verdict |
|---|---:|---:|---|
| `MEMORY.md` (boot 3) | 29,072 | **89%** | 🟡 **rotate-tier** — rule-5 stop is <22,785 B ⇒ **6,288 B still owed** |
| `docket/CATALYSTS.tsv` (boot 5) | 24,049 | 74% | 70–75% band; 363 B of headroom to the trigger |
| `STATUS.md` (boot 1) | 23,401 | 72% | 70–75% band; rotated this session |
| `thesis/PREDICTIONS.tsv` (boot 4) | 22,176 | 68% | ok |
| `SCRATCH.md` (boot 2) | 9,727 | 30% | ok |
| `workbook/SCHEMA.tsv` (boot 7) | 1,829 | 6% | ok |
| *(not boot-read, for context)* `CLAUDE.md` | 36,493 | 112% | **FALSE-POSITIVE-CANDIDATE** — harness-auto-loaded, not a boot-protocol whole-read; the READ_CAP rule is scoped to "a surface a boot protocol tells a session to READ WHOLE" |
| *(not boot-read)* `NEXUS_BRIEF.md` / `THESIS.md` / `AUCTION_HEALTH.md` | 66,985 / 65,206 / 44,774 | 206% / 200% / 138% | same class — **NOT** cap breaches; flagged only as comprehension load |

`read_cap_check --agent BOND` → **rc=0**, with the perimeter caveat printed verbatim: *"this desk has no declaration in PROME/registry/READS.tsv, so this is 'clean within what the scan found', NOT a clean bill."*
`ledger_staleness.py BOND` → 3 scanned, **all ok** (FLOW +3d, KB +0d, VX +3d); 7 TSVs outside the scan perimeter.

## B3 · Period activity, 2026-09-01 → 2026-09-17
| Metric | Value |
|---|---|
| Commits touching `AGENTS/BOND/` | **90** |
| **Self-authored** (subject begins `BOND`) | **37** |
| Routed-IN (subject begins another desk's name) | 53 |
| **Last self-commit** | `f2599a3a0` **2026-09-17** — *"BOND: closeout 9/17 09:0x — L404 grade OWED to the 13:00 spawn; F2 carrier blind-read + 10 fixes; memo to PROME"* |
| Dark days | **0** |
| Distinct self-authoring days | 8 (9/01, 9/02, 9/04, 9/09, 9/10, 9/14, 9/15, 9/17) |
| Structural events in period | TRADE.md re-based to posture-only (9/9, `9a3b78b2b`) · STATUS back under budget 33,551→31,002 B (9/4, `79794d7f0`) · `dm_cross_section.py` built (9/1) · `buyback_f2.py` + `registry/f2_reads.tsv` built (9/17) · THESIS v1.2.1→v1.2.7 (six minor bumps) · `BND-22` FALSE, `BND-23/24/28/29` TRUE · first-ever `I'` fire (9/15) |

**This is the fleet's busiest node and the period confirms it.** The 9/1 FLEET_MAP note ("102 self / 85 inbound") is directionally unchanged.

## B4 · Open questions I could not settle
1. Whether the 9/30 TLT put leg is live — off-repo by design; I did not and must not resolve it from STATUS/TRADE.
2. Whether `watchers.py` / `monitors/WATCH_DATES.tsv` have a live invocation site. Neither appears in `CLAUDE.md`'s boot or closeout step list. **CANNOT-EVALUATE** without reading `boot_recompute.py` end-to-end.
3. Whether the 9/18 FR2004 join actually lands — it is tomorrow. **NOT-SEEN** by any instrument available to me.
4. Whether the 9-session mirror divergence (`STATUS.md:78`) is a deliberate hold or accumulated debt. The file states the direction but not a resolution date.

## B5 · Flags for the OWNER (BOND) — each verified at the artifact
| # | Pri | Flag | Artifact |
|---|---|---|---|
| B-1 | 🟠 | **`MEMORY.md` is 29,072 B = 89% of the 32,550 B budget, rotate-tier, not rotated.** Rule 5 stops at <70% (22,785 B) ⇒ **6,288 B still owed**. Stopping at the 75% trigger re-breaches on the next append | `read_cap_check --agent BOND`; the desk's own receipt at `SCRATCH.md:11` |
| B-2 | 🟠 | **No `PROME/registry/READS.tsv` declaration** — 0 rows for BOND. Every read-cap verdict on this desk is heuristic-perimeter, self-labelled "NOT a clean bill." Peer desks (BROCK, 9/12) have declared | `grep -c BOND PROME/registry/READS.tsv` → 0 |
| B-3 | 🟠 | **`workbook/LEDGER_GLOB` does not exist**, so root closeout step 1c-bis (`ledger_staleness.py --nudge BOND`) has no declared ledger set to nudge against | `ls AGENTS/BOND/workbook/LEDGER_GLOB` → No such file |
| B-4 | 🟠 | **`CLAUDE.md:224-250` FILES table is behind the tree.** Missing: `NEXUS_BRIEF.md` (66,985 B live cross-agent surface), `PROTOCOL.md`, `AUDIT.md`, `registry/`, `analysis/`, `setups/`, `proposals/`, `research/`, and monitors `buyback_f2.py` · `dm_cross_section.py` · `watchers.py` · `matrix_v2_base_rate.py` | `CLAUDE.md:224-250` vs `git ls-files AGENTS/BOND/` |
| B-5 | 🟠 | **`CLAUDE.md:91-110` CROSS-AGENT SIGNALS lists 4 outbound targets; the live `outbox/` carries 12.** SAM and the REGINALD-FHLB leg exist only in `THESIS.md:194-195`. Three surfaces carry the topology and the charter's copy is the thinnest | `ls AGENTS/BOND/outbox/*.md`; `THESIS.md:194-195` |
| B-6 | 🟡 | **`monitors/CDX_CASH_BASIS.md` is 21 days behind STATUS on its own vector** — monitor says 8/27 `z20 +0.82`, STATUS says `[9/8, STALE] z20 +1.28`. Both tagged; neither wrong; the explainer lags the number | `CDX_CASH_BASIS.md:4` vs `STATUS.md:70` |
| B-7 | 🟡 | **`CLAUDE.md:151-160` §EXIT RULES is still generic template prose** while the real 4-category apparatus lives in STATUS/THESIS. A cold reader landing on the charter gets a template, not the desk's exits | `CLAUDE.md:151-160` vs `STATUS.md:95-108` |
| B-8 | 🟡 | **`docket/CATALYSTS.tsv` sits at 74% of budget with 363 B of headroom** to the rotate trigger. One session's additions crosses it | `read_cap_check --agent BOND` |

**FALSE-POSITIVE-CANDIDATES (raised, NOT upheld — recorded because a dismissed flag is part of the record):**
- **"`CLAUDE.md` is 36,493 B = 112% of the read-cap budget."** *Not upheld.* READ_CAP binds "any surface a boot protocol tells a session to READ WHOLE"; `CLAUDE.md` is harness-auto-loaded by directory walk, not a boot-protocol read step, and `read_cap_check --agent BOND` does not count it. Same disposition for `NEXUS_BRIEF.md` (206%), `THESIS.md` (200%) and `monitors/AUCTION_HEALTH.md` (138%). **They are comprehension load, not cap breaches** — DAEDALUS may still want a view on whether a 44,774 B file should be canon for the `I'` bars.
- **"The composite has been 12/35 for 15 consecutive sessions — the matrix is not moving."** *Not upheld.* `STATUS.md:73` gives a per-row reason for each hold and states *"Nothing crossed a pre-registered line this session."* A stable composite with stated reasons is discipline, not rot.
- **"`workbook/VX.tsv` disagrees with the convergence matrix."** *Not a defect to flag* — BOND declares it on the surface (`STATUS.md:78`), names the direction, and says it is flagged rather than silently reconciled. It is listed above only as open question §7-4, not as a flag.

---
---

# ██ DESK 2 — BROCK ██

# PART A — REFRESHED PROFILE (draft, ready for re-verification)

# Agent Profile — BROCK

**Profile vintage:** 2026-09-17 (reader draft, DAEDALUS re-verification pending)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** 1-reader solo read at HEAD (fan-out leg P1 of the 2026-09-17 refresh wave)
**Sources read:** `CLAUDE.md` (247 ln / 24,688 B, whole) · `STATUS.md` (123 ln / 31,963 B, whole) · `LESSONS.md` (84 ln, headings + head) · `SCRATCH.md` (head) · `MAINTENANCE.md` (incl. MODERNIZATION BACKLOG) · `EXPECTED_SIGNALS.md` (head) · `NEXUS_BRIEF.md` (head) · `OPEN_ITEMS_2026-09-03.md` · `ARCH_REPORT_2026-06-26.md` (head) · `workbook/{KB,VX,VX_HISTORY,FLOW,PREDICTIONS,PREDICTIONS_ARCHIVE,PREDICTIONS_SCOREBOARD,SCHEMA,PUBLISHED,PC_REDEMPTION_REGISTER,BANK_BDC_MATRIX,BDC_CASH_COVERAGE}` · `docket/CATALYSTS.tsv` · `board_log.tsv` (header + tail) · `trade/{TRADE,NAMES,CROSS_ANALYSIS}.md` · `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` · `tools/soi_nonaccrual.py` · `registry/corrections_receipts.tsv` · newest `domain/sources/` (9/9–9/12) · `PROME/registry/READS.tsv` BROCK rows · `git log --after=2026-09-01 -- AGENTS/BROCK/`. **SKIPPED:** `archive/research-outputs/RP-BRK-*` (8), `archive/domain-sources/` incl. PNG/JPG, ~190 `inbox/WALTER/processed/`, `research/` pre-Jul memos.
**Staleness:** refresh when ANY fires — (1) `AGENTS/BROCK/STATUS.md` `**Convergence: NN/70**` leaves **57/70**; (2) `AGENTS/BROCK/workbook/PREDICTIONS.tsv` row `BRK-02` `Status` leaves **OPEN** (resolver 2026-09-30); (3) a directory `AGENTS/BROCK/thesis/` appears (MAINTENANCE.md backlog item #3); (4) `python3 scripts/read_cap_check.py --agent BROCK` returns **rc≠0**; (5) `AGENTS/BROCK/trade/TRADE.md:1` loses its `🧊 FROZEN` banner; or (6) **> 45 days** from the vintage above ⇒ **2026-11-01**.

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

## 1. Identity
**Private credit / BDC contagion** — BDC financials (PIK %, dividend coverage, NAV, non-accruals), private-credit defaults and maturity walls, redemption/gate mechanics, alt-asset managers (APO/OWL/BX/KKR/ARES), Athene–Apollo insurance-credit linkage, ILS/reinsurance, **AI-infrastructure lending (neocloud, GPU collateral)**, fund finance / warehouse-line utilisation, software-sector marks. **Class:** Market (grade in `FLEET_MAP.tsv`, not restated). **Spawnable by:** PROME / Will.

**Core thesis (`CLAUDE.md:12-14`):** *"Private Credit's Public Reckoning"* — PIK masks a ~6% shadow default rate vs a reported 2.1%; the $482B BDC market is **bifurcated** (disciplined top tier vs a fragile long tail burning cash); AI-infra lending is 2000-style vendor financing. **Second layer:** insurance/reinsurance reflexivity loops.

**Transmission (`CLAUDE.md:195-217`):** sends to **REGINALD** (BDC↔bank warehouse, shared portfolio-company markdowns, PIK >20% of TII at FSK/ARCC), **LIQUID** (revolver draws, NAV-facility LTV breaches, gates), **OTTO** (BDC earnings / DQ), **LABOR** (portfolio-company layoffs), **HAWK** (insurance capacity), **ALL** on APO<$100 or an Athene RBC breach. Receives from HAWK / HENRY / LIQUID / REGINALD / OTTO.

**Cessions are unusually explicit and have grown:** HY OAS → LIQUID · VIX/macro → HENRY · bank CRE + bank-level scores → REGINALD · **insurer-exposure NUMBERS → SHADE (Will 6/26)** · **the EU bank/private-credit seam → HANS at full depth (Will 8/28)** (`NEXUS_BRIEF.md:4`). BROCK keeps only the insurer-**as-lender** leg.

**Routing rule, corrected 2026-09-03:** **SIGNALS → WALTER** (never direct); **ANALYSIS and PACKETS → straight into the recipient's `inbox/`** under root carve-out ①; **`outbox/` is for PROME-action requests only** (`CLAUDE.md:77`, `:247`). This line previously instructed direct signal delivery and was fixed on DAEDALUS's fleet census.

**What it's for:** *"Is private credit cracking, and where does it transmit to banks?"*

## 2. File anatomy (where the richness lives) — HEAVY, ~334 tracked files, 6 layers
| File | Holds | Richness? |
|---|---|---|
| `STATUS.md` (123 ln / **31,963 B = 98% of budget 🟠**) | **REGIME BLOCK (5-line, `:14-20`)** · near-window catalyst calendar · **14-vector convergence matrix + an explicit `Independence map` line (`:63`)** · composite arithmetic printed (`:66`) · 4-part EXIT RULES incl. a **TRIGGER LADDER** migrated from the frozen TRADE.md (`:98-100`) · **THESIS-KILL DECISION TREE** (`:102`) · BOTTOM LINE | **live state — and BROCK's de-facto thesis surface** |
| `workbook/FLOW.tsv` (**25 pathways**, LIVE hdr 9/12) | **the contagion engine** — `FLOW-BRK-001`→`-025` with Speed (DAYS/WEEKS/MONTHS/QUARTERS) + Layer + Status. Newest two are the period's own findings: `-024` *Measurement-Basis Masking* and `-025` *Weekly-Leash Bridging* | **exemplary; exceeds blueprint** |
| `workbook/KB.tsv` (**276 data rows / 258,682 B**) | canonical 13-col record; Admiralty `Conf` A1–F6 + EMPIRICAL/ESTIMATE/ASSUMPTION | permanent record |
| `workbook/VX.tsv` (**25 vectors**, LIVE hdr 9/3) | `VX-BRK-001`→`-025` with a `Category` taxonomy (BDC_Health · Credit_Marks · Liquidity · Contagion · Default_Rates · Market_Signal · Sponsor_Strategy · Cross_Channel · Gate_Cascade · Price_Discovery · Regulatory_Legal · Structure). **Header carries an explicit "cite the owner, do not read a level off this file" fence** | permanent record |
| `workbook/PREDICTIONS.tsv` (22 rows / **48,681 B — declared `scoped`, NEVER read whole**) + `PREDICTIONS_ARCHIVE.tsv` + `PREDICTIONS_SCOREBOARD.md` | 10 cols incl. **`Invalidation`** and **`Action_If_Falsified`**; status enum used in practice: OPEN · PARTIAL · REMOVED · SUPERSEDED · RESOLVED-TRUE · RESOLVED-FALSE-LETTER. **11 OPEN**, `BRK-02` resolves 9/30 | **institutional learning loop** |
| `workbook/PC_REDEMPTION_REGISTER.tsv` (24 rows, LIVE hdr) | **the definition surface for `GATE-BRK-R2`** — registered 9/3; the header itself carries the gate's (a)/(b) legs, state, and the dated corrections against them | **a genuine local invention: a ledger that IS a spec** |
| `workbook/PUBLISHED.tsv` (21 rows) · `VX_HISTORY.tsv` (16) · `SCHEMA.tsv` · `KB_ARCHIVE_MAR26.tsv` (100) | published-claim register · retired vectors · data dictionary · KB archive | supporting record |
| `workbook/{BANK_BDC_MATRIX,BDC_CASH_COVERAGE}.tsv` | **both FROZEN with banners** (7/04 and 6/26) — the two-state rule satisfied, verified by `ledger_staleness` | correctly dead |
| `board_log.tsv` (**121 rows / 89,476 B — declared `grep`, NEVER read whole**) | append-only WALTER-consumption ledger: `timestamp_read · signal_id · disposition ∈ {acted,noted,deferred,info-only,skipped} · source · notes`. Per `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.2 | **permanent record; the fleet's fullest signal-consumption audit trail** |
| `docket/CATALYSTS.tsv` (42 data rows, 8 col) | dated catalysts with `date_class ∈ {hard, confirmed, modeled}` — the **`modeled`** token is a BROCK marker for a window inferred from filer history rather than announced | forward state — **but see §4, it is not boot-read** |
| `LESSONS.md` (84 ln / **31,469 B = 97% of budget 🟠**) | numbered mistake patterns (through **#35**), grouped by date-of-session with emoji severity; **boot read 2** | **learning engine — and the one that gates future predictions** |
| `SCRATCH.md` (199 ln / 46,122 B) | NEXT-BOOT ranked first moves · open debts · watch order · FOLLOW-UP tiers · SESSION LOG · workbook/mail/git health block | session handoff — **but see §4, the boot manifest does not list it** |
| `MAINTENANCE.md` (6,747 B) | structural change-log (**Trigger / What changed / Files touched / Boot-impact / Lessons**) + a ranked **MODERNIZATION BACKLOG** scored *leverage ÷ effort × tack-on-fit* | **a genuine local invention — no other desk read carries one** |
| `NEXUS_BRIEF.md` (121 ln / 34,501 B) | curated cross-agent synthesis feed, refreshed at closeout | cross-agent channel — **stale, see §7** |
| `EXPECTED_SIGNALS.md` (4,655 B) | durable banded rules, **NO live values** (the HENRY pattern) | durable method — last reviewed 2026-03-06 |
| `trade/TRADE.md` (287 ln) | **🧊 FROZEN 2026-07-27 with a CONDITION-not-lifecycle banner** naming exactly what was stale and where §9 migrated. §1–§8 kept in-tree as a readable record of how the position was reasoned | **the fleet's exemplar freeze banner** |
| `trade/{NAMES,CROSS_ANALYSIS}.md` + `trade/APO/` (4) | 5-tier names list w/ promotion log · 4-entity cross-pattern synthesis (99.7¢ ceiling, spread-compression-universal) · APO/Athene deep dives | deep multi-firm analysis — vintages 3/16–5/01 |
| `tools/soi_nonaccrual.py` | SOI non-accrual extractor. **Validated exact (25 loans / 15 issuers) against BCRED Q2-2026 `0001803498-26-000048`**; the docstring names the two silent corrupters it handles | **tooling — built 9/3, the desk's first real script** |
| `domain/sources/` (33) · `research/` (16) · `archive/` (23) · `inbox/WALTER/processed/` (~190) | per-session primary reads and memos · pre-Jul research corpus · crc'd STATUS rotations · consumed signals | deep — read newest 2–3 only |
| `OPEN_ITEMS_2026-09-03.md` · `OPEN_THREADS_2026-07-09.md` · `ARCH_REPORT_2026-06-26.md` | Will-commissioned 5-col inventory (item · class OPEN/PENDING/OWED/BROKEN/BLOCKED · whose move · dated? · artifact) · prior threads · 6/26 architecture report | one-off records |

*The key question this answers: when I grade section X, which file do I actually read?* — **for BROCK the answer is almost always `STATUS.md` plus one ledger, because this desk has no `thesis/` layer.**

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | `CLAUDE.md:12-14` (core + second layer) + `STATUS.md:14-20` **REGIME BLOCK** + `workbook/FLOW.tsv` (25 pathways) + `trade/NAMES.md` cascade + `trade/CROSS_ANALYSIS.md` | **no `thesis/` directory and no versioned doc** — the standing argument is split across a charter paragraph, a 5-line regime block rewritten each session, and the FLOW ledger. `MAINTENANCE.md:41` registers this as backlog item #3, ranked MED/MED and deferred | **content exemplary, HOUSING is the gap** |
| Convergence / scoring | `STATUS.md:42-71` | 14 vectors, cols `Vector \| current \| Δ \| Threshold → next level \| Rescored`; **a per-vector `Rescored` date** ; composite arithmetic printed (`:66`); **an explicit `Independence map` line** naming which vectors share a node and vote once (`:63`); downgrades carry a signed reason paragraph each (`:67-69`) | **strong — the Δ column + per-vector rescore dates are better than blueprint** |
| Invalidation / exit | `STATUS.md:73-103` (4 numbered categories + §5 TRIGGER LADDER + a 5-step **THESIS-KILL DECISION TREE**) + `CLAUDE.md:145-170` | literal thresholds with FIRED/NOT-FIRED and session counts; **the decision tree needs 2-of-3 reversals to override and the 8/28 run is recorded as 0-of-3**; a retired kill leg is kept struck-through with the base rate that killed it (`:77-80`) | **exemplary** |
| Thresholds | `EXPECTED_SIGNALS.md` (durable, no live values) + `workbook/VX.tsv` bands + `STATUS.md` matrix "Threshold → next level" column + `PC_REDEMPTION_REGISTER.tsv` header (gate definitions) | durable-vs-live split enforced by the Doc Ownership table (`CLAUDE.md:112-125`); conjunction triggers; **registered `GATE-*` ids shared with the fleet registry** | conformant |
| Predictions | `workbook/PREDICTIONS.tsv` + `_ARCHIVE` + `_SCOREBOARD.md` + `LESSONS.md` | `BRK-NN` ids (charter-mandated, `CLAUDE.md:109`); `Invalidation` **and** `Action_If_Falsified` columns — the latter is a genuine blueprint-plus; Brier + hit-rate scoreboard; failure synthesis feeds LESSONS | **strong** |
| Cross-agent routing | `CLAUDE.md:195-217` route matrix + `:76-93` Signal Protocol + `NEXUS_BRIEF.md` + `board_log.tsv` | condition→target→priority; **SIGNALS→WALTER / PACKETS→inbox / outbox=PROME-only** three-way split, corrected 9/3; WALTER consumption is **logged row-by-row with a disposition token** | **conformant → exemplary on the inbound side** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)
| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `STATUS.md:75-80` §1 Thesis Kill | the 100% private-credit overlay | `**Updated:**` at `:3` | `NOT FIRED` / `~~struck~~ RETIRED AS A KILL <date> (WQ-nnn)` |
| `STATUS.md:82-85` §2 Position-Specific | the APO Dec $95P | same | `🔴 FIRED 8/12` + the ruling that followed |
| `STATUS.md:87-89` §3 Convergence Downgrades | the timeline, not the thesis | same | `NOT FIRING (0 this session)` — and `:70` carries the live count **2 of 3** |
| `STATUS.md:91-96` §4 Time-Based / prediction-linked | individual `BRK-*` rows | per-row resolver dates | `NOT GRADED` / `COUNT STAYS AT 2` / `55% HELD` |
| `STATUS.md:98-100` §5 TRIGGER LADDER | 11 registered triggers (migrated from frozen `trade/TRADE.md` §9) | `State, 9/2:` | `2 of 11 FIRED, both reviewed and closed` · `1 RESOLVED NEGATIVE` · `1 RE-LABELLED` |
| `STATUS.md:102` THESIS-KILL DECISION TREE | overrides a compression-driven kill | `RUN 2026-08-28` | `0 of 3 REVERSED` per-leg with ❌/✅ |
| `workbook/PREDICTIONS.tsv` `Status`+`Invalidation`+`Action_If_Falsified` | each registered claim | `Made_Date`/`Resolve_Date` | OPEN · PARTIAL · REMOVED · SUPERSEDED · RESOLVED-TRUE · RESOLVED-FALSE-LETTER |
| `workbook/PC_REDEMPTION_REGISTER.tsv` header | `GATE-BRK-R2` legs (a)/(b) | `# Status: LIVE` + dated in-header corrections | state sentence naming the vehicle count and the next live read date |
| `workbook/VX.tsv` `Threshold`/state cells | per-vector level | `# Last real data refresh: 2026-09-03` two-clock header | score + category |
| `workbook/FLOW.tsv` `Status` | a contagion pathway's existence | `# Last real data refresh: 2026-09-12` | ACTIVE/ARMED/FIRED/BUILDING/LATENT |
| `workbook/{BANK_BDC_MATRIX,BDC_CASH_COVERAGE}.tsv` | **nothing — correctly dead** | `# FROZEN <date>` banner | banner presence; `ledger_staleness` reports FROZEN +70d / +78d |
| `trade/TRADE.md:1` | **nothing — correctly dead**; §9 migrated to STATUS §5 | `🧊 FROZEN 2026-07-27` + condition paragraph | banner presence |

## 4. Deviations from standard (+ why)
**BETTER than blueprint:**
1. **The two-state ledger rule is fully satisfied, and visibly.** Two ledgers FROZEN with banners, six LIVE with **content-derived two-clock headers** (`# Status: LIVE. Last real data refresh: YYYY-MM-DD (content-derived — newest cell in the file)`) that name PAT-044 and tell `ledger_staleness.py` to read that line and never mtime. `ledger_staleness.py BROCK` returns **zero silent-rot rows**. Several headers *explain why the file will read days behind* — *"That alert is the point, not a defect"* (`FLOW.tsv:1`).
2. **`trade/TRADE.md`'s freeze banner is the fleet exemplar** (`:1-9`): it states the freeze as a **condition, not a lifecycle**, enumerates exactly which figures were stale and by how much, names the load-bearing §9 and where it migrated, points at position truth off-repo, and says why the file stays in-tree.
3. **An explicit `Independence map` line under the convergence matrix** (`STATUS.md:63`) naming which vectors share an antecedent and vote once. BROCK solved the no-double-count problem the 6/28 profile flagged as a handle gap.
4. **`MAINTENANCE.md` — a structural change-log + ranked modernization backlog**, with an explicit anti-ritual clamp: *"do NOT wire it into the every-session closeout."* No other desk read carries this.
5. **Read-cap perimeter is DECLARED and ATTESTED**, 16 rows in `PROME/registry/READS.tsv` (desk #3 to file, 9/12), with per-row modes `whole/scoped/grep/summary`. Two boot steps were **rewritten to be un-whole-readable** (`CLAUDE.md:32`, `:36`) and each carries the arithmetic: PREDICTIONS *"48,681 B = 149% of the 32,550 B budget, so a whole read is a breach"*; `board_log.tsv` *"89,476 B: 275% of the budget and 165% of the CAP ITSELF."*
6. **ALWAYS / SCALED closeout tiering** with a Live-event override carrying **two named clamps** (`CLAUDE.md:24-26`) — the override defers timing, never waives; ALWAYS steps fire regardless.
7. **A retired kill leg keeps its base rate.** The `HY OAS <260 for 10+ sessions` kill was re-labelled to an OBSERVABLE because BROCK's own measurement showed it closed <260 **exactly once in three years (n=787), longest run 1 session** — *"a kill that was never reachable in its own sample"* (`STATUS.md:80`). Label corrected on Will's word; no threshold moved.

**DEBT (real, verified at the artifact):**
- **No `thesis/` layer.** The standing argument has no versioned home and no changelog; `MAINTENANCE.md:8` admits it and `:41` ranks the build as backlog #3, deferred. Consequence: every thesis pivot is traced through STATUS prose that is rewritten each session and rotated to `archive/`. This is the desk's **largest structural gap**, and it is self-registered.
- **`STATUS.md` 31,963 B = 98% of budget; `LESSONS.md` 31,469 B = 97%.** Both rotate-tier. Rule-5 stop is <22,785 B ⇒ **9,179 B** and **8,685 B** still owed respectively. Both are boot reads 1 and 2, i.e. this desk's boot loads ~63,400 B of rotate-tier surface before it does anything.
- **`SCRATCH.md` is boot-read in practice but not in the manifest.** `SCRATCH.md:3` says *"Read at boot (after STATUS), refreshed at closeout."* `CLAUDE.md:28-39` BOOT lists steps 0→5b and **does not include SCRATCH**; `PROME/registry/READS.tsv` has **no SCRATCH row** and its `ATTESTATION` row says `manifest-complete` for `BROCK:0-5b`. Either the attestation is wrong or SCRATCH's own header is. At 46,122 B (**142% of budget**) the answer matters.
- **`docket/CATALYSTS.tsv` is the same class.** It exists (42 rows, 29,434 B) and STATUS routes readers to it (`:26`, `:123`), but no boot step reads it, it has no READS.tsv row, and `CLAUDE.md:48` still describes it in the **future tense** — *"Phase 2 will replace this informal version with `docket/CATALYSTS.tsv`."* The charter has not caught up with its own tree.
- **`domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` is in the silent-rot middle.** `**Last updated:** 2026-04-02` (`:3`) = **168 days**, no FROZEN banner, no two-clock header, not boot-read, and referenced only by one consumed inbox signal and one archived-class source memo — i.e. not by a live analytical or protocol doc. Root §Data Hygiene forbids exactly this state.
- **`workbook/PREDICTIONS_SCOREBOARD.md` is 70 days behind its own ledger.** `**Updated:** 2026-07-09 … SCORE (fully-resolved, n=10)`. Since then `BRK-27` resolved FALSE-ON-LETTER (8/28) and `BRK-30` RESOLVED-TRUE (9/3). The calibration surface does not carry them, so hit-rate and Brier are stale by two rows.
- **`NEXUS_BRIEF.md` carries a superseded composite.** `:7` reads *"convergence **59/70** — HELD, nothing rescored 9/2"*; `STATUS.md:65` has read **57/70** since the 9/3 rescore. The cross-agent feed is 15 days stale and disagrees with the canonical surface on the headline number other desks consume.
- **`EXPECTED_SIGNALS.md` `Last reviewed: 2026-03-06`** (195 days) and **`trade/NAMES.md` `Last Updated: 2026-05-01`** (139 days) — both durable-method docs cited in the charter FILES table, neither frozen nor refreshed.
- **`CLAUDE.md:227-247` FILES table is behind the tree**: no `SCRATCH.md`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`, `docket/`, `board_log.tsv`, `registry/`, `tools/`, `workbook/{PC_REDEMPTION_REGISTER,PUBLISHED,PREDICTIONS_SCOREBOARD,PREDICTIONS_ARCHIVE}`.
- **`workbook/LEDGER_GLOB` does not exist**, so root closeout 1c-bis cannot nudge this desk against a declared ledger set — despite BROCK having twelve of them.

**Floor-not-ceiling:** the `Category` taxonomy on VX, the `date_class` `modeled` token, the disposition enum on `board_log`, the `Action_If_Falsified` column and the ranked backlog are **rich local form, not divergence**. Do not normalise them away.

## 5. Load-bearing context / DO NOT TOUCH
- **`workbook/FLOW.tsv`'s 25-pathway grid IS the contagion engine.** It is the only durable home for the transmission model while there is no `thesis/`.
- **The shared-antecedent independence DISCIPLINE** — `STATUS.md:63` *"AI-unwind node (APO/ARES) = ONE vote inside cross-asset; NEXUS M-09 adds none. Q2 redemption wave (5 funds) = ONE vote."* Plus `:71`: *"OCIC hardens BOTH the redemption-gates and Blue Owl vectors; per the 6/26 shared-antecedent verdict that is ONE wave and I moved neither on it."* Any Independence-column formalisation must preserve this.
- **The 5-step THESIS-KILL DECISION TREE needs 2-of-3 reversals to override** (`STATUS.md:102`). Do not weaken to 1-of-3.
- **`trade/TRADE.md` is FROZEN and §9 lives in `STATUS.md` §5.** `BRK-25` and `BRK-26` cite §9 in their `Action_If_Falsified` fields — the citation target resolves through STATUS, not through the frozen file. Do not unfreeze, and do not delete the frozen file: §1–§8 are the record of how the position was reasoned.
- **Position truth is off-repo.** `STATUS.md:83` marks the APO Dec $95P book mark as **14 days stale on the 8/14 FORGE vintage** and says so. Never resolve the position from STATUS or from `FORGE/PORTFOLIO.md` (frozen Feb-2026).
- **The two-clock ledger headers are load-bearing text, not decoration.** `ledger_staleness.py` parses `Last real data refresh:` first and scans the header block for RETIRED/SUPERSEDED as dead-banners — which is why `PC_REDEMPTION_REGISTER.tsv:1` opens with an explicit `# Status: LIVE` declaration *explaining* that its own gate-history prose contains those words. Reword that header and the ledger silently reclassifies as dead.
- **`board_log.tsv` and `workbook/PREDICTIONS.tsv` must NEVER be read whole** — 275% and 149% of budget. Use `cut -f2` / `grep` and `awk -F'\t' '$6~/OPEN|STUCK/'`. The charter states the arithmetic at both sites.
- **`git mv`, never bash `mv`, for the WALTER consume move** (`CLAUDE.md:38`) — bash `mv` leaves a dangling deletion in the shared index.
- **Pre-commit git-status check is BROCK-local and stricter than root** (`CLAUDE.md:55`): run `git status -- AGENTS/BROCK/` **and** `git diff --cached --stat` before every commit; installed after catching a SHADE file pre-staged by a concurrent session.
- **SIGNALS → WALTER, always.** `outbox/` is PROME-action-only. The direct-signal instruction that used to sit here was a route-around-WALTER defect, corrected 9/3.
- **`BRK-NN` prediction ids, no bare numbers** (`CLAUDE.md:109`) — collision guard across agents.
- **Cessions:** insurer NUMBERS → SHADE, EU seam → HANS, HY OAS → LIQUID, VIX → HENRY, bank scores → REGINALD. `STATUS.md:71` shows the discipline in action: *"Duration is the one candidate and I did not take it — LIQUID owns the 10Y series."*

## 6. Maturity snapshot
Grade + confidence live in `FLEET_MAP.tsv` (**not restated**). What this read establishes:
- **The 9/1 FLEET_MAP `Gaps` cell is stale in three cells.** It says *"Matrix 59/70"* — STATUS has read **57/70** since 9/3 (`:65`). It says *"byte budget cited (54,250 cap …)"* — the binding number is the **32,550 B budget** and STATUS now sits at **98%** of it. It says *"Dark since 8/28"* — BROCK self-committed on 9/2, 9/3, 9/9 and 9/12 (31 self-commits in the period).
- `FLEET_MAP` `Next_upgrade` reads *"L5 blocker external; a declared byte-budget block (TERRY form) is the one cheap self-leg."* The **external** blocker (YEYOU) is now permanently unfireable — the seat was retired 2026-09-05, so *"zero YEYOU flags"* is a default-zero instrument (WQ-181 ②, re-point-or-N/A at the 9/14 ladder sitting). The **self** leg is still open, and BROCK has gone further than the suggestion: it filed a full READS.tsv manifest (9/12) rather than just a budget block.
- New residual self-legs this read surfaces: STATUS + LESSONS both at rotate-tier; no `thesis/` layer; `LEDGER_GLOB` absent; the SCRATCH/docket manifest gap.
Work queue → `upgrades/BROCK_CARD.md`.

## 7. Open questions / comprehension gaps
1. **Is `SCRATCH.md` boot-read or not?** Two surfaces disagree (`SCRATCH.md:3` vs `CLAUDE.md:28-39` + the `manifest-complete` attestation in READS.tsv). At 46,122 B = 142% of budget, the answer decides whether this desk's boot is over cap. **NOT-ADJUDICATED** — it is the desk's call, not a reader's.
2. **Is the APO Dec $95P still live?** `STATUS.md:83` last marks it at $0.05 on the 8/14 FORGE vintage, flagged 14 days stale at the time of writing (now 34). Off-repo truth; **do not resolve from STATUS or FORGE**.
3. **Does `BRK-02` resolve on the amortized-cost or fair-value basis?** BROCK found (`STATUS.md:108-110`) that OBDC discloses non-accruals on two bases that **moved in opposite directions over the same two quarters** — 2.3%→2.8% at amortized cost, 1.1%→0.8% at fair value — and that `BRK-02`'s letter does not name a basis. BROCK explicitly refused to settle it because *"the amortized-cost basis both fires my bearish prediction and is the one I believe analytically correct, and that coincidence is exactly the reason it is not mine to rule."* Flagged to PROME; **resolver date is 2026-09-30, thirteen days out.** This is the desk's single sharpest open item.
4. **Was the 9/18 CRMT date ever added to BROCK's OWN docket?** It is in `PROME/DOCKET.tsv` line 343 (verified). It is **not** in `AGENTS/BROCK/docket/CATALYSTS.tsv` (no 2026-09-18 row). BROCK has been dark since 9/12 and the date is tomorrow.
5. **What does `EXPECTED_SIGNALS.md` still govern?** Last reviewed 3/06; it is named in the charter twice as the durable-method home, but I could not find a live citation to any specific rule in it from STATUS or the workbook. **CANNOT-EVALUATE** without a full read of the file against the current matrix.
6. **Does `PREDICTIONS_SCOREBOARD.md` have an owner-declared cadence?** It calls itself the calibration surface but carries no refresh rule and is 70 days behind. **NOT-ADJUDICATED.**

---

# PART B — REFRESH REPORT: BROCK

## B1 · Old profile (`profiles/BROCK.md`, body 2026-06-28, 81d) — section-by-section disposition
| Old § | Claim as written | Verdict | Evidence / locator |
|---|---|---|---|
| Header `:4` | "Staleness: refresh when TRADE.md position layer or the convergence matrix materially changes, or > 45 days" | **TRIGGER FIRED ×3, UNSERVICED.** TRADE.md was FROZEN 7/27 (a position-layer change); the matrix moved 60→59→57; 81 days > 45 | `trade/TRADE.md:1`; `STATUS.md:65` |
| Δ banner `:6` | "2026-07-22 PRODUCTION REVIEW — trigger NOT fired (matrix 60/70 + book unchanged) … Next check: BDC marks-window aftermath (~7/28+)" | **CARRIED-VERIFIED as history; the 7/28 next-check never produced a banner update** | banner unchanged since 7/22 |
| §1 Identity | ARCC/Ares/Apollo/Owl, BCRED gating, NDFI, PIK, Athene-Apollo; "Cedes insurer numbers to SHADE, HY OAS to LIQUID" | **UPDATED** — add AI-infra lending (neocloud/GPU collateral), fund finance, software marks; and **the EU bank/PC seam is now ceded to HANS at full depth (Will 8/28)** | `CLAUDE.md:176-184`; `NEXUS_BRIEF.md:4` |
| §1 "consumes WALTER signal lane (board_log)" | routing | **UPDATED** — routing is now a declared three-way split: SIGNALS→WALTER, PACKETS→recipient inbox (carve-out ①), outbox→PROME-only. Corrected 9/3 on DAEDALUS's census | `CLAUDE.md:77`, `:247` |
| §2 `STATUS.md (211 ln)` "14-vector matrix (composite 60/70)" | anatomy | **UPDATED** — **123 ln / 31,963 B**; still 14 vectors; **composite 57/70** (60→59 on 8/28, 59→57 on 9/3) | `STATUS.md:65-66` |
| §2 `KB.tsv (158 rows)` | record | **UPDATED** — **276 data rows / 258,682 B** | `workbook/KB.tsv` |
| §2 `FLOW.tsv (21)` "the contagion engine" | record | **UPDATED** — **25 pathways**; `-024`/`-025` added 9/12 from the period's own primary reads | `workbook/FLOW.tsv:26-27` |
| §2 `VX.tsv (20) banded vectors` | record | **UPDATED** — **25 vectors**, and they now carry a `Category` taxonomy + an explicit owner-fence in the header | `workbook/VX.tsv:1-27` |
| §2 `PREDICTIONS*` "Brier 0.244, 5/7" | learning loop | **REFUTED as stated / UPDATED.** The scoreboard at HEAD reads **7/10 = 70%, Brier 0.216** — but is itself stamped 2026-07-09 and does not carry `BRK-27` (8/28) or `BRK-30` (9/3) | `PREDICTIONS_SCOREBOARD.md:3`, `:7-11` |
| §2 `trade/TRADE.md (275 ln)` "feeds live APO Dec $95P … **position layer stale 5/21**" | trade truth | **REFUTED/RESOLVED — the debt was DISCHARGED by freezing.** 287 ln, **🧊 FROZEN 2026-07-27** with a condition-not-lifecycle banner; §9 migrated to `STATUS.md` §5 | `trade/TRADE.md:1-9`; `STATUS.md:98-100` |
| §2 `EXPECTED_SIGNALS.md (147)` | durable method | **CARRIED-VERIFIED with a new caveat** — still no live values, but `Last reviewed: 2026-03-06` (195 d) | `EXPECTED_SIGNALS.md:5` |
| §2 `LESSONS.md (64) — 22 numbered lessons` | learning | **UPDATED** — 84 ln / 31,469 B, numbered through **#35**, grouped by session date; **97% of read-cap budget** | `LESSONS.md`; `read_cap_check --agent BROCK` |
| §2 `docket/CATALYSTS.tsv, NEXUS_BRIEF.md` | forward state / sync | **UPDATED** — docket 42 rows with a `modeled` date_class; NEXUS_BRIEF **15 days stale and carrying a superseded composite** | `docket/CATALYSTS.tsv`; `NEXUS_BRIEF.md:7` |
| §2 `archive/ (huge, incl 88k-ln ARCC fulltext, PNGs)` | history | **REFUTED in part — DROPPED.** No 88k-line ARCC fulltext is tracked under `AGENTS/BROCK/archive/`; what is there is 8 `research-outputs/RP-BRK-*` memos, 4 STATUS rotations, `LESSONS_ROTATED_2026-09-12.md`, and 4 images | `git ls-files AGENTS/BROCK/archive/` |
| §2 (absent) | — | **NEW ROWS OWED:** `MAINTENANCE.md`, `SCRATCH.md`, `board_log.tsv`, `tools/soi_nonaccrual.py`, `workbook/PC_REDEMPTION_REGISTER.tsv`, `workbook/PUBLISHED.tsv`, `registry/corrections_receipts.tsv`, `OPEN_ITEMS_2026-09-03.md`, `ARCH_REPORT_2026-06-26.md` | all tracked at HEAD |
| §3 Convergence row: "**no Independence column** — in prose only" | handle gap | **REFUTED — DROPPED.** `STATUS.md:63` carries a named **`Independence map:`** line | `STATUS.md:63` |
| §3 Predictions row: "**no if-falsified ACTION column** — consequences in TRADE.md" | handle gap | **REFUTED — DROPPED.** `workbook/PREDICTIONS.tsv` header carries `Action_If_Falsified` as column 9 | `workbook/PREDICTIONS.tsv:1` |
| §3 Thesis-structure row "FLOW.tsv + NAMES.md cascade + CROSS_ANALYSIS + domain tracker — **exemplary**" | dimension | **UPDATED, and one input is now rot.** FLOW is exemplary and grew; `NAMES.md` is 139 d old; `CROSS_ANALYSIS.md` 3/17; `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` is 168 d old with **no banner**. The live thesis carrier is now `STATUS.md` REGIME BLOCK | `trade/NAMES.md:3`; `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md:3`; `STATUS.md:14-20` |
| §4 debt "BANK_BDC_MATRIX flagged-stale but NOT frozen (silent-rot middle, root-CLAUDE hygiene violation)" | debt | **REFUTED — DROPPED.** `# FROZEN 2026-07-04` banner present; `ledger_staleness` reports it FROZEN | `workbook/BANK_BDC_MATRIX.tsv:1` |
| §4 debt "VX self-count inconsistent across files (STATUS 18 / ARCH 21 / file 20)" | debt | **CANNOT-EVALUATE as stated / effectively DROPPED.** The file has 25 rows; `STATUS.md` no longer states a VX count anywhere; the 6/26 ARCH_REPORT is a frozen one-off. The *mechanism* (a count restated in three places) is gone because only one place states it | `workbook/VX.tsv`; `grep` of STATUS finds no VX count |
| §4 debt "TRADE.md position table anchored to a 5/21 Fidelity PDF … residuals ~-90%/-97% unresolved" | debt | **RESOLVED — DROPPED** (frozen 7/27; position truth routed off-repo) | `trade/TRADE.md:1-9` |
| §5 all 8 DO-NOT-TOUCH bullets | load-bearing | **7 CARRIED-VERIFIED, 1 UPDATED.** The "shared-node independence in prose" bullet is now **formalised** as the `Independence map` line and must be preserved as such | `STATUS.md:63`, `:71` |
| §6 "L4 (conf H) … below L5 only on: stale trade-position layer, unfrozen BANK_BDC_MATRIX, no zero-YEYOU clean bill" | maturity | **UPDATED — two of three legs CLOSED.** Trade layer frozen 7/27; BANK_BDC_MATRIX frozen 7/04; the YEYOU leg is now a **default-zero instrument that can never fire** (seat retired 2026-09-05). New residual legs: no `thesis/`, STATUS+LESSONS at rotate-tier, SCRATCH/docket manifest gap, `LEDGER_GLOB` absent | this file §6 |
| §7 Q1 "are the ~90%-loss TRADE.md residuals closed or live?" | open Q | **DROPPED** (file frozen; position truth off-repo) | `trade/TRADE.md:7` |
| §7 Q2 "VX row-count of record (18/20/21)" | open Q | **DROPPED** (see §4 above) | |
| §7 Q3 "is the live APO Dec $95P the current book?" | open Q | **CARRIED-VERIFIED — still open**, now with a stated staleness | `STATUS.md:83` |

**Tally:** 5 CARRIED-VERIFIED · 13 UPDATED · 9 DROPPED-as-REFUTED/RESOLVED · 1 CANNOT-EVALUATE.

## B2 · File tree at HEAD (`git ls-files AGENTS/BROCK/` = **334** tracked files)
| Cluster | Count | Note |
|---|---|---|
| Root `.md` | 10 | CLAUDE · STATUS · SCRATCH · LESSONS · MAINTENANCE · NEXUS_BRIEF · EXPECTED_SIGNALS · OPEN_ITEMS_2026-09-03 · OPEN_THREADS_2026-07-09 · ARCH_REPORT_2026-06-26 · (+ LAST_COMPLETION) |
| Root `.tsv` | 1 | `board_log.tsv` (89,476 B) |
| `workbook/` | **14** | KB · KB_ARCHIVE_MAR26 · VX · VX_HISTORY · FLOW · PREDICTIONS · PREDICTIONS_ARCHIVE · PREDICTIONS_SCOREBOARD.md · PUBLISHED · SCHEMA · PC_REDEMPTION_REGISTER · BANK_BDC_MATRIX · BDC_CASH_COVERAGE · STATUS_ARCHIVE_MAR26.md |
| `docket/` | 1 | CATALYSTS.tsv (29,434 B) |
| `trade/` | 7 | TRADE (frozen) · NAMES · CROSS_ANALYSIS · `APO/` ×4 |
| `research/` | 16 | incl. 4 dated 2026-09-03 (WQ-158 pre-reg + results, migration test, BCRED NA names) |
| `domain/` | 34 | `PRIVATE_CREDIT_CONTAGION_TRACKER.md` + 33 `sources/` (newest 4 dated 9/09–9/12) |
| `tools/` | 1 | `soi_nonaccrual.py` |
| `registry/` | 1 | `corrections_receipts.tsv` (3 rows) |
| `archive/` | 23 | 7 root rotations + `domain-sources/` (8, incl. 4 images) + `research-outputs/` (8 RP-BRK memos) |
| `outbox/` | 24 `.md` + `delivered/.gitkeep` | newest 2026-09-02 |
| `inbox/` | ~205 | **1 pending root packet (REGINALD 9/14) + 15 pending `WALTER/` (9/14–9/15) + ~190 processed** |

**Byte sizes of the boot-read surfaces** (`read_cap_check --agent BROCK`, budget 32,550 B, **perimeter DECLARED + ATTESTED**, 16 manifest rows):
| Surface | Mode | Bytes | % budget | Verdict |
|---|---|---:|---:|---|
| `STATUS.md` (boot 1) | whole | 31,963 | **98%** | 🟡 **rotate-tier — 9,179 B still owed to the <70% stop** |
| `LESSONS.md` (boot 2) | whole | 31,469 | **97%** | 🟡 **rotate-tier — 8,685 B still owed** |
| `workbook/PREDICTIONS.tsv` (boot 3) | **scoped** | 48,681 | (149% if whole) | not cap-bearing — awk-filtered to OPEN/STUCK past-resolver rows |
| `board_log.tsv` (boot 5) | **grep** | 89,476 | (275% if whole) | not cap-bearing — `cut -f2` / grep by signal id |
| `inbox/WALTER/*.md` (boot 5) | whole, CLASS row | — | — | not a single file |
| `registry/corrections_receipts.tsv` (5b) | scoped | 164 | — | ok |
| 3 shared scripts (`ledger_staleness`, `dashboard`, `corrections_boot_check`) | summary | 65,095 / 25,057 / 14,765 | — | not cap-bearing |

`read_cap_check --agent BROCK` → **rc=0** on the attested manifest (2 cap-bearing measured, 7 declared-not-counted).
`ledger_staleness.py BROCK` → 8 scanned: **2 FROZEN** (BANK_BDC_MATRIX +70d, BDC_CASH_COVERAGE +78d), **6 ok** (FLOW +1d, KB +0d, PC_REDEMPTION_REGISTER +1d, PREDICTIONS +0d, PUBLISHED +16d, VX +10d). **Zero silent-rot rows.** 3 TSVs outside the scan perimeter (`docket/CATALYSTS.tsv`, `registry/corrections_receipts.tsv`, `research/NDFI_BANK_LEVEL_Q4_2025.tsv`).

## B3 · Period activity, 2026-09-01 → 2026-09-17
| Metric | Value |
|---|---|
| Commits touching `AGENTS/BROCK/` | **69** |
| **Self-authored** (subject begins `BROCK`) | **31** |
| Routed-IN | 38 (PROME, WALTER, OTTO, REGINALD, LIQUID, DAEDALUS) |
| **Last self-commit** | `bcafb7769` **2026-09-12** — *"BROCK: consume PROME's READS-registration packet — inbox clear, session closed"* |
| **Dark days since last self-commit** | **5** (9/12 → 9/17) |
| Distinct self-authoring days | 4 (9/02, 9/03, 9/09, 9/12) — heavily clustered: **17 of 31** on 9/03 alone |
| Structural events in period | READS.tsv manifest filed, desk #3 (9/12) · two boot steps rewritten to be un-whole-readable (9/12) · `GATE-BRK-R2` registered on `PC_REDEMPTION_REGISTER.tsv` (9/3) · `tools/soi_nonaccrual.py` built + validated exact (9/3) · three silent-rot ledgers given true two-clock headers (9/3) · matrix rescored 59→57 (9/3) · `FLOW-BRK-024/025` added (9/12) · LESSONS rotated (9/12) · WQ-106 kill→observable executed (9/2) · WQ-173/176 ruled and encoded (9/4) |

**Shape of the period:** one very heavy session (9/3), one heavy session (9/12), then dark. The 9/12 session is notable for being almost entirely **self-correction against other desks' instruments** — OTTO caught a +4d bridge error propagated across 6 surfaces, PROME caught a wrong read-cap denominator and a double-counted BCRED print, and BROCK corrected its own "OTTO owes that commit" claim **4m14s after writing it**.

## B4 · Open questions I could not settle
1. Whether `SCRATCH.md` is in-scope for boot (see §7-1). The attestation and the file's own header disagree; I am a reader, not the attester.
2. Whether `BRK-02` resolves on amortized cost or fair value — BROCK deliberately did not rule it, and I will not either (§7-3). Resolver is 9/30.
3. Whether the APO Dec $95P is live. Off-repo.
4. Whether `EXPECTED_SIGNALS.md` still governs any live rule (§7-5) — would need a full read of the file against the current matrix.
5. Whether the 15 pending WALTER signals contain anything time-critical. I did not open them (read-only scope, and opening them is the desk's own boot-step-5 work, logged to `board_log.tsv`). **NOT-SEEN**, not zero.

## B5 · Flags for the OWNER (BROCK) — each verified at the artifact
| # | Pri | Flag | Artifact |
|---|---|---|---|
| K-1 | 🔴 | **`domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` is in the silent-rot middle root CLAUDE.md forbids.** `**Last updated:** 2026-04-02` = 168 days; **no FROZEN banner, no two-clock header**; not boot-read; referenced only by one consumed inbox signal and one archived-class source memo — not by a live analytical or protocol doc. Freeze it or refresh it; it is also >60d retirement-eligible | `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md:3`; `grep -rn` shows only `inbox/WALTER/processed/SIG-W-20260716-007.md:110` and `domain/sources/FSK_PREBUILD_MAY11.md:243` |
| K-2 | 🔴 | **`STATUS.md` contradicts itself on whether the 9/18 CRMT date is registered.** Header `:3` says *"**9/18 now registered at DOCKET L343**"*; the body row `:35` still says *"**NEW, and REGISTERED NOWHERE** — asked PROME to docket it (9/12 packet)."* The header is TRUE (PROME/DOCKET.tsv line 343 carries the 2026-09-18 CRMT row). Two live instructions in one file; the correction was placed **beside** the superseded text rather than replacing it | `STATUS.md:3` vs `STATUS.md:35`; `PROME/DOCKET.tsv:343` |
| K-3 | 🟠 | **BROCK's OWN `docket/CATALYSTS.tsv` has no 2026-09-18 row** — the date BROCK's own STATUS calls *"the next hard forcing date"* is **tomorrow** and is absent from the desk-local docket, which does carry the downstream 9/21 §2.1 rung. The fleet docket has it; the desk's does not, and the desk is dark | `awk -F'\t' '$1>="2026-09-13"' AGENTS/BROCK/docket/CATALYSTS.tsv` → 9/15, 9/21, 9/30 ×2, 10/31, 11/13, 12/03, 2027-04-30. No 9/18 |
| K-4 | 🟠 | **`NEXUS_BRIEF.md` publishes a superseded composite to the cross-agent lane.** `:7` reads *"convergence **59/70** — HELD"*; STATUS has read **57/70** since the 9/3 rescore. 15 days stale on the headline number other desks consume | `NEXUS_BRIEF.md:7` vs `STATUS.md:65` |
| K-5 | 🟠 | **`STATUS.md` 31,963 B = 98% of budget AND `LESSONS.md` 31,469 B = 97%** — both boot reads 1 and 2, both rotate-tier, **9,179 B + 8,685 B owed** to the rule-5 <70% stop. Boot loads ~63,400 B of rotate-tier surface before it does anything | `read_cap_check --agent BROCK` |
| K-6 | 🟠 | **`SCRATCH.md:3` says "Read at boot (after STATUS)" but no boot step reads it, no READS.tsv row covers it, and the `ATTESTATION` row claims `manifest-complete` for BROCK:0-5b.** At 46,122 B (142% of budget) the two answers have different cap consequences. Fix one surface or the other | `SCRATCH.md:3` vs `CLAUDE.md:28-39` vs `PROME/registry/READS.tsv` BROCK rows |
| K-7 | 🟠 | **`workbook/PREDICTIONS_SCOREBOARD.md` is 70 days behind its own ledger.** `Updated: 2026-07-09`, `n=10`; `BRK-27` (FALSE-ON-LETTER, 8/28) and `BRK-30` (RESOLVED-TRUE, 9/3) are not in it. Hit rate and Brier are both stale | `PREDICTIONS_SCOREBOARD.md:3`, `:7-11` vs `workbook/PREDICTIONS.tsv` rows 20-21 |
| K-8 | 🟠 | **`CLAUDE.md:48` still describes `docket/CATALYSTS.tsv` in the FUTURE tense** — *"Phase 2 **will replace** this informal version with `docket/CATALYSTS.tsv`"* — while the file exists with 42 rows and STATUS routes readers to it as the full docket. The charter has not caught up with its own tree | `CLAUDE.md:48` vs `docket/CATALYSTS.tsv`; `STATUS.md:26`, `:123` |
| K-9 | 🟠 | **`CLAUDE.md:227-247` FILES table omits 11 tracked surfaces**: `SCRATCH.md`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`, `docket/`, `board_log.tsv`, `registry/`, `tools/`, `workbook/{PC_REDEMPTION_REGISTER,PUBLISHED,PREDICTIONS_SCOREBOARD,PREDICTIONS_ARCHIVE}` — including `board_log.tsv`, which boot step 5 depends on | `CLAUDE.md:227-247` vs `git ls-files AGENTS/BROCK/` |
| K-10 | 🟠 | **16 unprocessed inbound items and the desk is dark.** 15 `inbox/WALTER/*.md` (9/14–9/15) + 1 root packet (`2026-09-14_from-REGINALD_i-am-inverting-my-own-benign-ccc-hy-read…`). Last self-commit 9/12 | `ls AGENTS/BROCK/inbox/WALTER/*.md` → 15; `ls AGENTS/BROCK/inbox/*.md` → 1 |
| K-11 | 🟡 | **`workbook/LEDGER_GLOB` does not exist** — root closeout 1c-bis cannot nudge this desk against a declared ledger set, despite twelve ledgers | `ls AGENTS/BROCK/workbook/LEDGER_GLOB` → No such file |
| K-12 | 🟡 | **Two charter-named durable-method docs are long un-reviewed and un-frozen:** `EXPECTED_SIGNALS.md` *Last reviewed 2026-03-06* (195 d) and `trade/NAMES.md` *Last Updated 2026-05-01* (139 d) | `EXPECTED_SIGNALS.md:5`; `trade/NAMES.md:3` |
| K-13 | 🟡 | **No `thesis/` layer.** Self-registered as backlog #3 (`MAINTENANCE.md:41`) and admitted at `:8`. Consequence: the standing argument lives in a charter paragraph plus a REGIME BLOCK that is rewritten and rotated every session, so pivots have no versioned trail | `MAINTENANCE.md:8`, `:41`; `git ls-files AGENTS/BROCK/thesis/` → empty |

**FALSE-POSITIVE-CANDIDATES (raised, NOT upheld):**
- **"`workbook/PREDICTIONS.tsv` is 48,681 B = 149% of budget"** and **"`board_log.tsv` is 89,476 B = 275% of budget."** *Not upheld.* Both are declared **`scoped`** and **`grep`** in the attested READS.tsv manifest and the charter states the arithmetic and the access pattern at both call sites (`CLAUDE.md:32`, `:36`). `read_cap_check` correctly excludes them. This is the desk doing it right, not a breach.
- **"`workbook/KB.tsv` is 258,682 B."** *Not upheld* — not a boot read, not in the manifest, and `ledger_staleness` reports it current (+0d).
- **"Convergence has been held at 57/70 since 9/3."** *Not upheld as a defect.* The desk has been dark since 9/12; a held composite across a dark interval is correct behaviour, and `STATUS.md:65-71` gives a signed reason for each of the two downgrades and for the one **refused** downgrade that BROCK had predicted to Will would move.
- **"`trade/TRADE.md` is 287 lines of stale content."** *Not upheld* — it is FROZEN with an exemplary condition banner, kept in-tree deliberately, and its one load-bearing section migrated with a resolving citation target.
- **"`archive/` contains an 88k-line ARCC fulltext" (old profile §2).** *Could not be confirmed* — no such file is tracked at HEAD. Recorded as a REFUTED carried claim rather than a live flag.

---

## APPENDIX — reviewer-side findings about DAEDALUS's OWN map (welcome findings, per brief rule 5)
| # | Surface | Claim | Verdict | Locator |
|---|---|---|---|---|
| D-1 | `FLEET_MAP.tsv` BOND `Gaps` (last_scored 2026-09-01) | *"NO declared byte tier — STATUS 160,077 B / 250 ln = 492% of the read budget and 295% of the PHYSICAL ceiling (BOND cannot read its own STATUS whole once)"* | **REFUTED at HEAD.** `STATUS.md` is **23,401 B / 146 ln = 72% of budget**, with a declared rotation banner and a crc-stamped archive chain (`STATUS.md:6-7`). The named L5 blocker is DONE | `AGENTS/BOND/STATUS.md:6`; `read_cap_check --agent BOND` |
| D-2 | `FLEET_MAP.tsv` BROCK `Gaps` | *"Matrix 59/70"* | **REFUTED.** 57/70 since the 9/3 rescore | `AGENTS/BROCK/STATUS.md:65-66` |
| D-3 | `FLEET_MAP.tsv` BROCK `Gaps` | *"byte budget cited (54,250 cap + 'never raise')"* | **STALE FRAMING.** The binding number is the **32,550 B budget** (54,250 is the physical cap); BROCK is at 98% of budget, which the cap-framing hides | `read_cap_check --agent BROCK`; `BLUEPRINTS/READ_CAP.md` |
| D-4 | `FLEET_MAP.tsv` BROCK `Gaps` | *"Dark since 8/28"* | **REFUTED.** 31 self-commits in the period, on 9/02, 9/03, 9/09, 9/12 | `git log --after=2026-09-01 -- AGENTS/BROCK/` |
| D-5 | `profiles/BOND.md:3` banner | *"Refresh checkpoint: **2026-09-15**"* | **BLOWN by 2 days at this read.** The banner fired a trigger on 9/01 and set a checkpoint that passed unserviced — PAT-085's own failure mode (a banner is a warning, not a fix) reproduced on the banner that cites PAT-085 | `AGENTS/DAEDALUS/profiles/BOND.md:3` |
| D-6 | `profiles/BROCK.md:4` | Staleness trigger *"refresh when TRADE.md position layer or the convergence matrix materially changes, or > 45 days"* | **FIRED ×3, UNSERVICED, and unlike BOND's it was never even bannered.** TRADE.md frozen 7/27; matrix moved twice; 81 days elapsed | `AGENTS/DAEDALUS/profiles/BROCK.md:4`, `:6` |
| D-7 | Both profiles' §6 | Both cite *"no zero-YEYOU clean bill"* as an L5 blocker | **Now a default-zero instrument that can never fire** — the per-push seat was retired 2026-09-05 (WQ-181 ①). Both §6 blocks need the re-point-or-N/A treatment WQ-181 ② schedules for the 9/14 ladder sitting | `AGENTS/DAEDALUS/CLAUDE.md` §AUTHORITY ⚠️ box |

