# INDEPENDENT LOCATOR VERIFICATION — P1 drafts (BOND · BROCK)

**Verifier:** DAEDALUS fan-out reader P1-VERIFY (adversarial second reader; did not write the draft) · **Date:** 2026-09-17 (Thu)
**Input:** `AGENTS/DAEDALUS/profiles/REFRESH_2026-09-17_READER_P1_BOND_BROCK.md` — PART A for BOND, PART A for BROCK.
**Method:** every claim naming a file, line, section, count, byte size, date, version, script, column or behaviour was opened at HEAD. Bytes by `wc -c`, counts by `grep -c`/`awk`, dates by `git log`, script behaviour by reading the source and by running the three read-only `--selftest` entry points (no writes, no mutating git).
**Verdicts:** VERIFIED (matches) · FAILED (says what is actually there) · DRIFTED (true, locator/count off — correct one given) · UNLOCATED (no locator, not found in ≤2 tries).
**Scope note:** PART A only, per the task. PART B claims are graded only where PART A restates them.

---
---

# ██ DESK 1 — BOND ██

## 1 · Verification table

| § | Claim (≤20 words) | Verdict | Correction |
|---|---|---|---|
| Hdr | `CLAUDE.md` 250 ln / 36,493 B | VERIFIED | |
| Hdr | `STATUS.md` 146 ln / 23,401 B | VERIFIED | |
| Hdr | Staleness ①: `thesis/THESIS.md:3` `Version:` = **1.2.7** | VERIFIED | `:3` is the `**Version:**` line, value 1.2.7 |
| Hdr | Staleness ②: `TRADE.md:3` `Last Updated:` = **2026-09-09** | VERIFIED | |
| Hdr | Staleness ③: `read_cap_check --agent BOND` rc≠0 | VERIFIED | live rc=0 today |
| Hdr | Staleness ④: `monitors/*.py` count = **12** | VERIFIED | exactly 12 |
| Hdr | Staleness ⑤: STATUS composite = **12/35** | VERIFIED | `STATUS.md:73` |
| §1 | Core scope at `CLAUDE.md:65-71` | **DRIFTED** | core owns-list is **`:67-73`** (`**You own:**` is `:66`) |
| §1 | Coverage extension (MBS/FHLB/EU) at `CLAUDE.md:72-74` | **DRIFTED** | **`:74-76`** |
| §1 | Sovereign-credibility set at `CLAUDE.md:75` | **DRIFTED** | **`:77`** |
| §1 | Sovereign set = ACM 10Y TP **+ KW `THREEFYTP10`** | **FAILED** | `:77` names "ACM 10Y TP level + BOND's own curve-shape/attribution falsifier structure". KW `THREEFYTP10` is a live instrument but lives at `STATUS.md:33` / `VX-BND-12`, not in the scope line |
| §1 | US sovereign CDS → unowned, **re-test 2026-12-01** | **FAILED** | `CLAUDE.md:77` says "Will HELD this sub-item, DOCKET deferral, **reconsider 8/24**". The 12/1 re-test is at `STATUS.md:107` and `PROTOCOL.md:19`. Two surfaces, two dates |
| §1 | Tool `monitors/dm_cross_section.py` | VERIFIED | exists, built 2026-09-01 |
| §1 | Declines: gold/real-yield→MIDAS · tails→retired for cause | VERIFIED | `CLAUDE.md:77` |
| §1 | Transmission matrix at `CLAUDE.md:91-110` | VERIFIED | `## CROSS-AGENT SIGNALS` = `:91`; inbound table ends `:110` |
| §1 | 5 outbound rows / 4 targets; 4 inbound (LIQUID/ZHAO/HENRY/HAWK) | VERIFIED | `:97-101`, `:107-110` |
| §1 | ↔SAM + ↔REGINALD carried in `THESIS.md:194-195` only | **DRIFTED** | SAM = **`:193`**, REGINALD-FHLB = **`:194`** |
| §1 | `THESIS.md:183-195` CROSS-AGENT LINKS | VERIFIED | heading `:182`, table `:184-194` |
| §1 | `STATUS.md:42` keeps NO copy of USD/JPY · Brent · VIX | VERIFIED | verbatim |
| §2 | ~431 tracked files | VERIFIED | `git ls-files` = 431 |
| §2 | STATUS 23,401 B = **72% of budget** | VERIFIED | tool prints 72% |
| §2 | STATUS holds a **17-row** live dashboard | **DRIFTED** | **16 data rows** (`:23-42`); 17 lines counting the header |
| §2 | Gate-distance table; FR2004 block; catalyst twin; BOTTOM LINE | VERIFIED | `:44` / `:56` / `:112` / `:131` |
| §2 | `Rolls up (workbook/VX.tsv)` column on the matrix | VERIFIED | `STATUS.md:63` |
| §2 | `THESIS.md` 199 ln / 65,206 B, v1.2.7 | VERIFIED | |
| §2 | 6 transmission channels | VERIFIED | `:64-69` |
| §2 | INSTRUMENT CONTEXT `:22-37` | VERIFIED | heading `:22`, section runs to `:40` |
| §2 | CONTESTED banner `:6-16` | VERIFIED | blockquote `:6-16` exactly |
| §2 | EXIT/FALSIFICATION `:91-131` | VERIFIED | heading `:91`, last content line `:131` |
| §2 | KEY THRESHOLDS `:135-145` | **DRIFTED** | `:135-150`; `:145` is the struck tail row, not the end |
| §2 | CHANGELOG: every entry old view → new view | VERIFIED | e.g. `:19` |
| §2 | PREDICTIONS.tsv 5 live rows `BND-25`→`-29`, 11 cols, `If_Falsified_Action` | VERIFIED | col 11 |
| §2 | 3 crc-stamped resolved archives | VERIFIED | `thesis/archive/` ×3 |
| §2 | Tally **13 TRUE · 11 FALSE · 1 VOID** at `STATUS.md:83` | VERIFIED | verbatim |
| §2 | `TRADE.md` 89 ln / 14,334 B | VERIFIED | |
| §2 | `TRADE.md:3` "RE-BASED … POSTURE and GATES only. No marks." | VERIFIED **as text** | but see 🔴 R-B2 — `:11` carries three marks |
| §2 | view = 4 numbered paras; add-gate table `:21-37`; cross-agent deps `:68-79` | VERIFIED | `:11/:13/:15/:17`; headings `:21`/`:38`, `:68`/`:80` |
| §2 | `KB.tsv` **297 data rows**, 13 col | VERIFIED | 298 lines |
| §2 | `VX.tsv` **20 vectors**; `VX-BND-09` RETIRED | VERIFIED | `STATUS.md:66` marks it retired |
| §2 | "7 roll up into the composite, the rest are feed-not-double-count" | **DRIFTED** | **14 VX vectors** roll into **7 headline matrix rows**; 5 (`-15/-17/-18/-19/-20`) are outside; `-09` retired |
| §2 | `FLOW.tsv` **15 pathways**; enum incl. **CONTRADICTED** | VERIFIED | all six tokens present |
| §2 | `FL-BND-15` = "the channel that actually fired, and NOT the one the position expresses" | VERIFIED | verbatim in `Flow_Name`; Status FIRED |
| §2 | `docket/CATALYSTS.tsv` **24 data rows**, 8 col, 24,049 B = 74% | VERIFIED | tool prints 74% |
| §2 | `date_class` ∈ **resolved/confirmed/recurring/watch/hard** | **FAILED** | observed set is **{confirmed 17, estimated 1, recurring 3, watch 3}** — no `resolved`, no `hard`; `estimated` missing from the draft |
| §2 | monitors = 6 `.md` + 12 `.py` + 3 `.tsv` + `fixtures/` | VERIFIED | 22 tracked |
| §2 | `AUCTION_HEALTH.md` 44,774 B, canonical for `I'` bars per `STATUS.md:98` | VERIFIED | `:98` names §GRADING BASIS; §GRADING BASIS is at `AUCTION_HEALTH.md:134` |
| §2 | `registry/f2_reads.tsv` 15 col, built 9/17 | VERIFIED | 15 cols; first commit 2026-09-17 |
| §2 | `NEXUS_BRIEF.md` 310 ln / 66,985 B; RE-PIN at `:5` supersedes below | VERIFIED | verbatim |
| §2 | `PROTOCOL.md` 11,726 B; §DELIVERY MODEL declared 2026-08-27 | VERIFIED | `PROTOCOL.md:39` |
| §2 | `MEMORY.md` 56 ln / 29,072 B = **89%** | VERIFIED | tool prints 89% |
| §2 | `SCRATCH.md` 9,727 B · `AUDIT.md` 32,927 B (8/21 audit) | VERIFIED | |
| §2 | `analysis/` 26 files | VERIFIED | |
| §2 | `outbox/` 47 live + 15 `delivered/` | VERIFIED | |
| §2 | `domain/sources/` ~50 rotated blocks + KBRA PDFs | **DRIFTED** | **46 files total**, the 2 KBRA PDFs included |
| §2 | `inbox/WALTER/processed/` (~200) | **FAILED** | `inbox/WALTER/processed/` = **112**; a separate `inbox/processed/` holds **121**; 235 inbox files in all |
| §2 | `archive/` 4 crc-stamped snapshots | VERIFIED | |
| §2b | `docket_check.py` boot 5 = `CLAUDE.md:28`; `VERIFIED ONLY THROUGH` line | VERIFIED | string present in source |
| §2b | `docket_check` **17 assertions / 11 fixtures** | VERIFIED | `--selftest` prints exactly that, rc=0 |
| §2b | `boot_recompute.py` boot 6 = `CLAUDE.md:29`; `rc=1` NOT a pass | VERIFIED | source `:31-32` |
| §2b | boot_recompute drift-checks TRADE/monitors/NEXUS_BRIEF; runs `check_fr2004()`; invokes `buyback_f2` | VERIFIED | `:68-71`, `:93`, `:130`; 4 `buyback` refs |
| §2b | `closeout_check.py` closeout 16 = `CLAUDE.md:44`; rc 0/1/2, 2 not a pass | VERIFIED | source `:23-24`, `:108-113`, `:150` |
| §2b | `closeout_check --selftest` = **35 fixtures** | **FAILED** | live run prints **"COMBINED: 8 numeric + 14 workbook-lint + 32 assertion = 54 fixtures"**, rc=1 |
| §2b | `assertion_check.py` **27 fixtures** | **FAILED** | live run prints **32 fixtures**, and **1 FAILURE**, rc=1 — see 🔴 R-B1 |
| §2b | `kb_lint.py` enforces PREDICTIONS enum **OPEN·TRUE·FALSE·VOID** | VERIFIED | `kb_lint.py:316` |
| §2b | `grade_auction.py` refuses a gate below **n=6**; **computes no tail** | VERIFIED | `MIN_N_FOR_GATE = 6` (`:55`); "NO TAILS" (`:23`, `:408`) |
| §2b | `buyback_f2.py` BUILT 2026-09-17; keyed to the operation SCHEDULE not a date | VERIFIED | first commit 9/17; docstring `:11` verbatim |
| §2b | `fr2004_fetch.py` resolves SBN2015/SBN2022/SBN2024 at runtime | VERIFIED | all three in source |
| §2b | `cdx_proxy.py` HYG/IEF + LQD/IEF | VERIFIED | |
| §2b | `dm_cross_section.py` 4 legs (FRED · ECB SDW · BoE IADB · MOF), built 9/1 | VERIFIED | all four; first commit 2026-09-01 |
| §2b | `watchers.py` 8/20, "a state change with NO PUBLISHER" | VERIFIED | first commit 2026-08-20; docstring `:11` verbatim |
| §2b | `matrix_v2_base_rate.py` one-off/periodic | VERIFIED | exists (first commit 2026-09-02) |
| §3 | `THESIS.md:41-90` CORE + channels + episode | VERIFIED | `:41`/`:60`/`:77`, EXIT at `:91` |
| §3 | regime-level posture with no dated numbers `:71` | VERIFIED | verbatim |
| §3 | third explanation held open (basis trade) `:83` | VERIFIED | verbatim |
| §3 | Convergence `STATUS.md:61-78`; re-sum `:74`; outside-list `:76`; divergence `:78` | VERIFIED | all four exact |
| §3 | Exit `STATUS.md:95-108`; PAIRED kill `:97`; add-gate asymmetry `:99` | VERIFIED | all exact |
| §3 | Thresholds `CLAUDE.md:114-129`; retired tail struck in both tables | VERIFIED | `CLAUDE.md:125`, `THESIS.md:145` |
| §3 | Routing `TRADE.md:68-79`; verification by CONTENT `CLAUDE.md:176-179` | VERIFIED | both exact |
| §3b | `monitors/RETIRED_TOKENS.tsv` `Retired_On` + `Guard_Words` cols | VERIFIED | header = Token·Retired_On·Reason·Guard_Words |
| §3b | `FL-BND-09` reads "CONTRADICTED — do not cite without this note" | VERIFIED | verbatim |
| §3b | `AUCTION_HEALTH.md` `**Last Updated:** 2026-09-17` | VERIFIED | `:4` |
| §4-1 | Boot⇄closeout symmetric pairing `CLAUDE.md:18`; r1→w9, r2→w13, r4→w10, r5→w12 | VERIFIED | boot `:24/:25/:27/:28`, closeout `:37/:41/:38/:40` |
| §4-2 | "conditional self-assessed steps get skipped" at `:29`, `:44` | VERIFIED | both lines carry it |
| §4-3 | Tail tombstone `CLAUDE.md:125`, `THESIS.md:145`, `STATUS.md:108` | VERIFIED | all three |
| §4-4 | 9/15 ceiling committed 10:06:44 ET pre-print (`CHANGELOG.md:21`) | VERIFIED | verbatim |
| §4-5 | Pairing rec was BOND's own, against its own book (`THESIS.md:100`) | VERIFIED | verbatim |
| §4-5 | 8/27 dealer-leg question halted, not self-ruled (`THESIS.md:124`) | VERIFIED | present — note the halt is now marked SUPERSEDED/RULED and retained as record |
| §4 | `MEMORY.md` 89%, 6,288 B owed; `SCRATCH.md:11` receipt | VERIFIED | tool and receipt quoted exactly |
| §4 | BOND has ZERO rows in `PROME/registry/READS.tsv`; BROCK declared 16 on 9/12 | VERIFIED | 0 vs 16 |
| §4 | `read_cap_check` perimeter caveat quoted verbatim | VERIFIED | exact match to tool output |
| §4 | `CLAUDE.md:224-250` FILES table omits 8 surfaces + 4 monitor scripts | VERIFIED | zero hits for any of the twelve in `:224-250` |
| §4 | NEXUS_BRIEF "named only inside a drift-check parenthesis (`:29`)" | **FAILED** | named at **`:29`, `:43` and `:247`**. `:43` is worse than absence: closeout 15 routes the feed "→ `NEXUS_BRIEF.md` **once Packet 7 lands**" — future tense (🔴 R-B3) |
| §4 | charter lists 4 outbound targets; live outbox carries 12 | VERIFIED | `:97-101` = 4 distinct targets; 47 outbox files |
| §4 | `CLAUDE.md:151-160` §EXIT RULES is generic template | **DRIFTED** | heading `:151`, four template categories run to **`:161`** |
| §4 | `CDX_CASH_BASIS.md` 21 days behind STATUS on its own vector | VERIFIED | `:4` = 8/27, `0.8567`, `z20 +0.82`; `STATUS.md:70` = `0.8585`, `+1.28 [9/8, STALE]` |
| §4 | 6/29 debt "NEXUS_BRIEF ABSENT" REFUTED — exists, 310 ln, refreshed 9/17 | VERIFIED | `NEXUS_BRIEF.md:3` |
| §4 | "HERMES live mail carrier" REFUTED — zero occurrences | VERIFIED | grep empty in both files |
| §4 | MATRIX_V2 adopted 8/27, first fired 9/15 | VERIFIED | `CHANGELOG.md:17-27`; `THESIS.md:102`, `:121` |
| §5 | `[[finding_threshold_vs_mechanism]]` wired into closeout 10 | VERIFIED | `CLAUDE.md:38` |
| §5 | durable docs carry no live values — `THESIS.md:17` **and `:35`** | **DRIFTED** | the retracted-figure/disclaimer record is at **`:17`** only ("the disclaimer stops the reader checking"); `:35` is the real-vs-nominal basis caveat, a different point |
| §5 | `VX-BND-08`…`-16` roll up; `-15/-17/-18/-19/-20` outside | **FAILED** | rolling set is `-01`…`-08`, `-10`…`-14`, `-16`; `-09` RETIRED and `-15` is explicitly OUTSIDE, so the range as written is wrong at both ends |
| §5 | ADD re-arm on the OLD stricter test (`STATUS.md:99`, WQ-99 Will 9/1) | VERIFIED | verbatim |
| §5 | Tail retired and not revivable (`STATUS.md:108`) | VERIFIED | verbatim |
| §5 | Dealer >18% contrarian-BULLISH, dropped as bearish kill (Will 8/27) | VERIFIED | `STATUS.md:98`; `THESIS.md:102` |
| §5 | rc semantics per tool are load-bearing | VERIFIED | all three source docstrings |
| §5 | `outbox/delivered/` verification by CONTENT; 7 of 22 false orphans | VERIFIED | `CLAUDE.md:176-179` |
| §5 | Rotation crc convention; 160,077 B pre-split snapshot named | VERIFIED | `STATUS.md:6`, crc32 `1210262` |
| §6 | FLEET_MAP BOND `Gaps` headline blocker is out of date | VERIFIED | cell says "STATUS 160,077 B / 250 ln = 492%"; HEAD is 23,401 B / 146 ln / 72% |
| §6 | Residual `Next_upgrade` legs = LEDGER_GLOB + a READS.tsv declaration | **DRIFTED** | the cell's surviving legs are **LEDGER_GLOB + PAT-044 headers + the derived-inheritance class fix**. READS.tsv is the reader's own new finding, not a map leg — keep it, but do not attribute it to the row |
| §6 | `AGENTS/BOND/workbook/LEDGER_GLOB` does not exist | VERIFIED | workbook holds only FLOW/KB/SCHEMA/VX |
| §6 | old profile's `conf M` reasoning | VERIFIED | `profiles/BOND.md:67`; FLEET_MAP now carries conf **H** |
| §6 | `upgrades/BOND_CARD.md`, `BOND_REVIEW_2026-08-20.md` + `_reader_raw.md` | VERIFIED | all three exist |
| §7-1 | `TRADE.md:11` marks 25× Sep-30 77P at $0.035 vendor mid, expiry 9/30 | VERIFIED | verbatim at `:11` (also summarised at `:42`, `:89`) |
| §7-2 | 9/18 FR2004 join is the declared critical path (`STATUS.md:144`) | VERIFIED | verbatim |
| §7-3 | WQ-246 "sustained" has no session count; 4 sessions through | VERIFIED | `THESIS.md:146`; `STATUS.md:65`, `:73` |
| §7-4 | Mirror divergence 9th session (`STATUS.md:78`), `-05`=4 / `-16`=4 vs 3 and 2 | VERIFIED | verbatim |
| §7-5 | `AUCTION_HEALTH.md` 44,774 B, cited canonical, not a declared boot-read | VERIFIED | absent from the 6 boot reads the tool enumerates |
| §7-6 | `watchers.py`/`WATCH_DATES.tsv` invocation site — CANNOT-EVALUATE | **UPGRADE** | resolves to a verified NEGATIVE: a repo-wide grep over all `.md`/`.py` finds **zero** invocation sites. See 🟠 R-B4 |
| §2/B2 | `ledger_staleness.py BOND` → "3 scanned, all ok" | **DRIFTED** | tool prints **"4 ledger(s) scanned; 7 TSV(s) NOT scanned"**; 3 rows displayed (FLOW +3d, KB +0d, VX +3d — those three values VERIFIED) |

## 2 · Totals — BOND

| Verdict | Count |
|---|---:|
| **VERIFIED** | **83** |
| **FAILED** | **7** |
| **DRIFTED** | **10** |
| **UNLOCATED** | **0** |
| *(UPGRADE: a draft CANNOT-EVALUATE resolved to a verified negative)* | 1 |
| **Total claims graded** | **101** |

---

## 3 · CORRECTED PART A — BOND

# Agent Profile — BOND

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P1 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** Mode-A — 1 reader solo read at HEAD + 1 independent locator verifier (fan-out leg P1 of the 2026-09-17 refresh wave)
**Sources read:** `CLAUDE.md` (250 ln / 36,493 B, whole) · `STATUS.md` (146 ln / 23,401 B, whole) · `thesis/{THESIS.md,CHANGELOG.md,PREDICTIONS.tsv}` · `TRADE.md` · `PROTOCOL.md` · `MEMORY.md` (head) · `SCRATCH.md` · `AUDIT.md` (head) · `NEXUS_BRIEF.md` (head) · `workbook/{KB,VX,FLOW,SCHEMA}.tsv` · `docket/CATALYSTS.tsv` · `registry/{corrections_receipts,f2_reads}.tsv` · `monitors/` (6 `.md` headers + 12 `.py` docstrings + 3 `.tsv`; `docket_check`/`assertion_check`/`closeout_check` `--selftest` RUN) · newest `analysis/` (9/14–9/17) · `outbox/` filename census · `git log --after=2026-09-01 -- AGENTS/BOND/`. **SKIPPED:** `data/*.csv` (auction history), `domain/sources/*.pdf` (KBRA), the rotated `domain/sources/*STATUS_archive*` files, `inbox/` (233 processed across two lanes).
**Staleness:** refresh when ANY fires — (1) `AGENTS/BOND/thesis/THESIS.md:3` `Version:` leaves **1.2.7**; (2) `AGENTS/BOND/TRADE.md:3` `Last Updated:` leaves **2026-09-09**; (3) `python3 scripts/read_cap_check.py --agent BOND` returns **rc≠0**; (4) the count of `AGENTS/BOND/monitors/*.py` leaves **12**; (5) `AGENTS/BOND/STATUS.md` composite leaves **12/35**; or (6) **> 45 days** from the vintage above ⇒ **2026-11-01**.
*Machine-evaluable in one command:* `python3 scripts/read_cap_check.py --agent BOND >/dev/null; echo rc=$?; grep -c '^\*\*Version:\*\* 1\.2\.7' AGENTS/BOND/thesis/THESIS.md; grep -c '2026-09-09' <(sed -n 3p AGENTS/BOND/TRADE.md); ls AGENTS/BOND/monitors/*.py | wc -l; grep -c 'Composite: 12/35' AGENTS/BOND/STATUS.md` — all five legs read from named artifacts. **YES, evaluable.**

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

## 1. Identity
US **bond-market structure as a transmission mechanism**: Treasury auction health (composition / cover / dealer take), corporate issuance (HY/IG), dealer positioning (FR2004), curve shape, credit-spread structure, credit-leads-equity (Hamilton ~3mo). **Class:** Market (`FLEET_MAP.tsv` owns the grade; not restated). **Spawnable by:** PROME / Will.

**Scope is now THREE layers, and two were added after the 6/29 profile:**
1. **Core** (`CLAUDE.md:67-73`) — auctions, issuance, dealer inventory, curve, credit spreads, issuance-freeze thresholds, credit→equity lead.
2. **Coverage extension**, Will-approved 6/27, **integrated 7/1** (`CLAUDE.md:74-76`) — **MBS / housing finance + GSE capital**, **FHLB advances** (the 2023-SVB regional-bank funding backstop, coordinated with REGINALD), **Eurozone rates** (bund curve + ECB shocks, RATES leg only; LIQUID owns the EU credit leg).
3. **Sovereign-credibility instrument set**, Will-ruled in-session 2026-08-10 (`CLAUDE.md:77`) — **30Y term-premium decomposition** (the charter line names **ACM 10Y TP level + BOND's own curve-shape/attribution falsifier structure**; the *daily* Kim-Wright leg `THREEFYTP10` is carried separately at `STATUS.md:33` / `VX-BND-12`) + **DM sovereign-spread cross-section** as a standing series at BOND's own primaries (tool: `monitors/dm_cross_section.py`). Three **named declines** live in the same line so nobody re-proposes them: gold/real-yield decoupling → MIDAS · auction **tails** → nobody, retired for cause · US sovereign CDS → unowned. ⚠️ **Two dates are live for that last sub-item and they disagree:** the charter at `:77` still says *"reconsider 8/24"* (24 days past), while `STATUS.md:107` and `PROTOCOL.md:19` carry a **12/1** re-test (`KB-BND-261`). The charter is the stale copy.

**Transmission (`CLAUDE.md:91-110`, `thesis/THESIS.md:183-194`):** sits between LIQUID (plumbing/funding) and ZHAO (foreign demand). Sends auction-composition-failure→LIQUID 🔴, cover-marker→LIQUID+ZHAO 🟠, credit-equity lead→HENRY 🟠, issuance-freeze→REGINALD 🔴, auction weakness→ZHAO 🟠; **↔ SAM** (JGB long-end / BOJ / yen ↔ US term-premium, channel 6, `THESIS.md:193`) and **↔ REGINALD** (FHLB, `THESIS.md:194`) are carried in THESIS only. Consumes LIQUID (SOFR/repo, energy-HY OAS), ZHAO (TIC), HENRY/HAWK (vol, geopolitics). One-source-of-truth cessions: energy-HY OAS→LIQUID · TIC→ZHAO · rate-expectations→HENRY · bank-level credit→REGINALD · private credit/BDC→BROCK · USD/JPY→SAM · Brent→BRENT · VIX→VIOLET (`STATUS.md:42` keeps NO copy of the last three).

**What it's for:** *"Is the bond market still* ***clearing****, or starting to* ***break****?"* — and the load-bearing distinction that answers it is **"expensive, not broken."**

## 2. File anatomy (where the richness lives) — HEAVY, 431 tracked files, 7 layers
| File | Holds | Richness? |
|---|---|---|
| `STATUS.md` (146 ln / **23,401 B = 72% of budget**) | Regime one-liner · **16-row** live dashboard with `[CONF src date]`/`[STALE]` tags (`:23-42`) · **Gate-distance table** `:44-55` (the decision numbers, recomputed never carried) · FR2004 block `:56-60` · 7-vector convergence matrix `:61-79` w/ **`Rolls up (workbook/VX.tsv)` column** (`:63`) · prediction scoreboard `:80-86` · Trade Interface `:87-94` · 4-category Exit/Falsification `:95-108` · catalyst twin `:112-130` · BOTTOM LINE `:131` | **live state — the single densest surface** |
| `thesis/THESIS.md` (199 ln / **65,206 B**, v1.2.7) | "expensive, not broken" core · **6 transmission channels** (`:64-69`) · `INSTRUMENT CONTEXT` block (the 30Y ≥5.00% history that cuts AGAINST the thesis, `:22-40`) · REGIME-LABEL CONTESTED banner (`:6-16`) · full EXIT/FALSIFICATION (`:91-131`) · KEY THRESHOLDS (`:135-150`) · scoreboard · cross-agent links (`:182-194`) | **durable thesis — and the fleet's most self-adversarial one** |
| `thesis/CHANGELOG.md` (389 ln / 71,910 B) | v1.2.7→v1.1.x, every entry **old view → new view** with the bump rule stated | version history |
| `thesis/PREDICTIONS.tsv` (5 live rows `BND-25`→`BND-29`, 11 cols incl. `If_Falsified_Action`) + `thesis/archive/PREDICTIONS_resolved_*.tsv` ×3 (crc-stamped) | falsifiable rows with **named basis** and pre-registered if-FALSE branches. Resolved tally **13 TRUE · 11 FALSE · 1 VOID** (`STATUS.md:83`) | **a STRONGEST dimension** |
| `TRADE.md` (89 ln / 14,334 B) | `:3` declares **RE-BASED 2026-09-09 to POSTURE + GATES ONLY — "No marks."** ⚠️ **The declaration is refuted eight lines later:** `:11` carries a $0.035 vendor mid, a TLT $81.73 close and a $76.89 breakeven (🔴 R-B2 below). The view (4 numbered paras `:11`–`:17`) · add-gate table + **breach protocol** `:21-37` · Active/Legacy `:38-45` · Reactivation Matrix `:56-67` · Cross-Agent Deps `:68-79` · dated Next Review `:80+` | trade truth (posture; construction is TERRY's) |
| `workbook/KB.tsv` (**297 data rows**, 13 col, 494,685 B) | canonical record; Admiralty `Conf` A1–F6 · `Epistemic` EMPIRICAL/ESTIMATE/ASSUMPTION · `Status` lifecycle · `Stale_By` | permanent record |
| `workbook/VX.tsv` (**20 vectors**) | `VX-BND-01`→`-20`. **14 of them** (`-01`…`-08`, `-10`…`-14`, `-16`) roll up into the 7 headline matrix rows; `VX-BND-09` is **RETIRED**; `-15/-17/-18/-19/-20` are explicitly **"Tracked OUTSIDE the composite"** (`STATUS.md:76`) | permanent record |
| `workbook/FLOW.tsv` (**15 pathways**) | `FL-BND-01`→`-15` w/ Speed + Status ∈ {LATENT, WATCH, CONFIRMED, **CONTRADICTED**, CONDITIONAL, FIRED}. `FL-BND-15` = "the channel that actually fired, and NOT the one the position expresses" (FIRED); `FL-BND-09` and `-13` both carry CONTRADICTED | **permanent record; the CONTRADICTED token is unusual and load-bearing** |
| `docket/CATALYSTS.tsv` (**24 data rows**, 8 col, **24,049 B = 74% of budget**, 363 B of headroom) | source of truth for dated catalysts; `date_class` observed set = **confirmed (17) · recurring (3) · watch (3) · estimated (1)** | forward state |
| `monitors/` — **6 `.md` + 12 `.py` + 3 `.tsv` + `fixtures/`** (22 tracked) | see §2b. `AUCTION_HEALTH.md` (44,774 B) is **canonical for the `I'` grading bars** — `STATUS.md:98` points at its §GRADING BASIS, which sits at `AUCTION_HEALTH.md:134`; the §3d percentile rail is at `:111` | **tooling layer — the single biggest change since 6/29** |
| `registry/f2_reads.tsv` · `registry/corrections_receipts.tsv` | per-op F2 buyback read ledger (15 col, built 9/17) · R1 corrections receipts (boot 7b) | ledgers |
| `NEXUS_BRIEF.md` (310 ln / **66,985 B**) | steady-state rates feed for NEXUS; **RE-PIN block at the top supersedes everything below it** (`:5`) | cross-agent channel — **EXISTS now (it did not on 6/29)** |
| `PROTOCOL.md` (96 ln / 11,726 B) | mail/refresh SOP + **§DELIVERY MODEL declared 2026-08-27** (`:39`) + per-source data-pull recipes (FR2004 series breaks, H.4.1 custody, TA_WS) | durable method |
| `MEMORY.md` (56 ln / **29,072 B = 89% of budget 🟠**) | durable BOND-local learnings (boot read 3) | durable — **rotate-tier, see §7** |
| `SCRATCH.md` (51 ln / 9,727 B) · `RECEIPT.md` · `LAST_COMPLETION.md` | session handoff (must be executable COLD) · run receipt · legacy | ephemeral |
| `AUDIT.md` (299 ln / 32,927 B) | the 2026-08-21 Will-tasked boot-document audit, incl. **dismissed candidate findings** | one-off audit record |
| `analysis/` (26) · `setups/` (3) · `proposals/` (2) · `research/` (2) | per-event grade/pre-print records — **the pre-print-before-the-print discipline lives here** | deep analysis — read the newest 2–3 only |
| `data/` (5 tracked, incl. 2 auction-history CSVs) · `domain/sources/` (**46 files total**: rotated STATUS/CATALYSTS blocks + 2 KBRA PDFs + LIQUID-donated frameworks) · `archive/` (4 crc-stamped snapshots) · `inbox/` (**112 in `WALTER/processed/` + 121 in `processed/`**; both pending lanes EMPTY) | raw + rotated history, each crc-stamped in its own header | SKIP |

### §2b. The `monitors/` tool layer (12 scripts — grade this as a dimension in its own right)
| Script | Wired into | What it is |
|---|---|---|
| `docket_check.py` | **boot 5** (`CLAUDE.md:28`) | v2 rebuild 8/27. Diffs TreasuryDirect `upcoming` vs CATALYSTS **keyed on CUSIP**. **rc0 ≠ "window covered"** — read the `VERIFIED ONLY THROUGH` line; names the ~5-day BLIND SPAN and refuses to adjudicate it. **`--selftest` green at HEAD: 17 assertions across 11 fixtures, rc=0** |
| `boot_recompute.py` | **boot 6** (`CLAUDE.md:29`) | cache-busted recompute of LEVELS **and DERIVED** stats with aggregation method stamped; prints `TRADE.md`'s gate table; drift-checks the **boot-unread** surfaces (`TRADE.md`, `monitors/*.md`, `NEXUS_BRIEF.md`); runs `check_fr2004()`; invokes `buyback_f2.py`. `rc=1` is NOT a pass, `rc=2` is not either |
| `closeout_check.py` | **closeout 16** (`CLAUDE.md:44`) | THE single closeout invocation — 3 checks, 1 fetch, 1 rc (0 clean / 1 finding / 2 fetch-failure, **2 is not a pass**). `--selftest` aggregates **54 fixtures** (8 numeric + 14 workbook-lint + 32 assertion). 🔴 **RED at HEAD — see R-B1** |
| `assertion_check.py` | component of 16 | stale-**assertion** sweep for claims with **no number in them**: DIRECTIONAL · FILE-STATE · EXPIRED · CAPABILITY. Reads ISO **and** slash dates; resolves bare `m/d` BACKWARD; **32 fixtures**. 🔴 **`--selftest` rc=1 at HEAD, 1 failure (R-B1)** |
| `kb_lint.py` | component of 16 (part 0/3) | workbook conformance vs `SCHEMA.tsv` + `AGENTS/VOCABULARIES.tsv` + the PREDICTIONS `Status` enum (**OPEN·TRUE·FALSE·VOID**, `kb_lint.py:316`, declared 8/21 because it was declared nowhere) |
| `grade_auction.py` | per-event | grades a print or pre-freezes the BARS; per-tenor benchmarks, median **and** mean, margins on every leg, residual branch, **refuses a gate below `MIN_N_FOR_GATE = 6`**, **computes no tail** (`:23`, `:408`) |
| `buyback_f2.py` + `registry/f2_reads.tsv` | boot, via `boot_recompute` | **BUILT 2026-09-17** (DOCKET L401). The standing **class carrier** for the per-op F2 read — *"keyed to the OPERATION SCHEDULE, not to a date"* (`:11`), because a RESOLVED docket row cannot drive the next op |
| `fr2004_fetch.py` | per-pull | NY Fed primary-dealer fetch; **resolves the SBN2015/SBN2022/SBN2024 series breaks at runtime** — the fix for a 6-week false "access gap" |
| `cdx_proxy.py` | `VX-BND-06` | free HYG/IEF + LQD/IEF proxy, explicit about what it cannot see (true CDX is paywalled — canonical statement + `re-test: 2026-12-01` at `PROTOCOL.md:19`) |
| `dm_cross_section.py` | 8/10 scope claim | 4 primary legs (FRED · ECB SDW · BoE IADB · MOF) — built 2026-09-01 to make the "standing series" actually standing |
| `matrix_v2_base_rate.py` | one-off/periodic (built 9/02) | per-tenor out-of-sample base-rating of the `I'` test |
| `watchers.py` (+ `WATCH_DATES.tsv`) | **NOTHING — built 2026-08-20, zero invocation sites repo-wide** | the **missing-watcher** class: *"a state change with NO PUBLISHER"* (`:11`). 🟠 An un-invoked guard is unowned in practice — R-B4 |

*The key question this answers: when I grade section X, which file do I actually read?* — **and for BOND the answer is increasingly a SCRIPT, not a document. Which is why a red selftest is a thesis-surface problem here, not a housekeeping one.**

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | `thesis/THESIS.md:41-90` CORE + `TRANSMISSION CHANNELS` (6, `:64-69`) + `ACTIVE EPISODE` (`:77`) + `FLOW.tsv` | "expensive, not broken"; channels carry Mechanism + **regime-level posture with no dated numbers** (`:71`); episode-not-break framing; a **third explanation deliberately held open** (basis-trade withdrawal, `:83`) | **exemplary** |
| Convergence / scoring | `STATUS.md:61-79` | 7 headline vectors (`:65-71`), cols `# \| Vector \| Score \| Status \| **Rolls up (workbook/VX.tsv)** \| Key Signal \| Upgrade Trigger` (`:63`); composite **re-summed and the arithmetic printed** (`:74`); `Tracked OUTSIDE the composite` line for the 5 non-rolling vectors (`:76`); **an OPEN MIRROR DIVERGENCE is declared rather than silently reconciled** (`:78`) | **strong — the roll-up column now does the independence work** |
| Invalidation / exit | `STATUS.md:95-108` (4 categories) + `thesis/THESIS.md:91-131` (full) + `TRADE.md:21-37` (gates) | every line carries a number **and** a session/date count; **PAIRED kill** with a dated pairing instrument (`STATUS.md:97`); **dual-print of OLD and NEW composition tests** while a ruling beds in; explicit "⛔ the ADD re-arm runs on the OLD, STRICTER test — never loosen an add gate as a side effect of a definition reconcile" (`:99`) | **exemplary — best-in-fleet on this dimension** |
| Thresholds | `CLAUDE.md:114-129` + `THESIS.md:135-150` + `VX.tsv` bands + `monitors/AUCTION_HEALTH.md:134` §GRADING BASIS | durable docs carry the RULE, never a tenor's instance; live values point to STATUS; **retired thresholds stay visible with the reason** (auction tail, struck-through at `CLAUDE.md:125` and `THESIS.md:145`); secular-norm caveats baked in (BTC 3.0→2.5 GAO) | **conformant→exemplary** |
| Predictions | `thesis/PREDICTIONS.tsv` + 3 crc-stamped archives + `STATUS.md:80-86` | 11 cols incl. `If_Falsified_Action`; **every row registers its own named basis and base rate before the number exists**; resolution states the margin on every leg | **a STRONGEST dimension** |
| Cross-agent routing | `CLAUDE.md:91-110` matrix + `THESIS.md:182-194` + `TRADE.md:68-79` + `NEXUS_BRIEF.md` + `outbox/` (47 live + 15 `delivered/`) | condition→target→priority 🔴/🟠; **outbox 🔴-acute-only** restraint; steady state now goes to `NEXUS_BRIEF.md`; `outbox/delivered/` created 8/20 and verification is **by CONTENT, not filename** (`CLAUDE.md:176-179`) | **conformant — but the charter table under-states live routes, see §4** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)
| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/THESIS.md:91-131` §EXIT/FALSIFICATION | the whole duration-short thesis; 4 categories | `Version:` + `Last Updated:` at `:3-4`, plus per-clause dated `⚠️ RE-SPECIFIED`/`CORRECTED` riders | prose verdict + a ⚠️/🔴 rider naming the date and the ruling record |
| `STATUS.md:95-108` §Exit/Falsification | the compact live mirror of the above | `**Last session:**` at `:4` | `🔴🔴 / 🔴 / ⛔` + explicit `NOT FIRED` / counter value |
| `STATUS.md:44-55` Gate-distance table | the TLT-put **add** gates (entry-side) | "recomputed every boot, never carried" caption at `:44` | `🔴 THROUGH by Nbp` / `🟡 Nbp` / `🟢` |
| `TRADE.md:21-37` add-gate table + breach protocol | the position's add authority | `**Last Updated:** 2026-09-09` at `:3` | `🔴 LEVEL LEG THROUGH` / `🟠 UNFIRED, not dead` / `❌ RESOLVED, DID NOT FIRE` |
| `thesis/PREDICTIONS.tsv` `Status` col | each registered claim | `Date_Made` / `Timeframe` / `Date_Resolved` cells | enum **OPEN·TRUE·FALSE·VOID** (declared 8/21, lint-enforced at `kb_lint.py:316`) |
| `workbook/VX.tsv` `Threshold_Yellow`/`_Red` | per-vector state | `Last_Updated` cell | score + `Last_Signal` |
| `workbook/FLOW.tsv` `Status` (col 8) | a transmission channel's existence | `Last_Updated` cell | `LATENT/WATCH/CONFIRMED/**CONTRADICTED**/CONDITIONAL/FIRED` — `FL-BND-09` reads "CONTRADICTED — do not cite without this note" |
| `monitors/AUCTION_HEALTH.md:134` §GRADING BASIS + `:111` §3d rail | the `I'` bars and the downgrade counter | `**Last Updated:** 2026-09-17` at `:4` | frozen per-tenor bars + counter integer |
| `monitors/RETIRED_TOKENS.tsv` | retired thresholds/tokens that must never fire again | `Retired_On` col | row presence + `Guard_Words` |

## 4. Deviations from standard (+ why)
**BETTER than blueprint — five, and they are why this desk reads as an exemplar:**
1. **Boot⇄closeout is a declared symmetric read→write pairing** (`CLAUDE.md:18`): STATUS r1→w9, SCRATCH r2→w13, PREDICTIONS r4→w10, CATALYSTS r5→w12. Plus a **mirror-consistency check** (step 17, `:45`) and a **composite re-sum** (step 9, `:37`) whose arithmetic is printed on the surface.
2. **Invocation, not detection, is treated as the gap.** Guards are *wired into a tool that boot/closeout already runs*, explicitly because "conditional self-assessed steps get skipped" (`CLAUDE.md:29`, `:44`). Three separate rc-contract corrections are documented in-charter with the failure that earned each. ⚠️ **The rule has one live exception the desk has not noticed: `watchers.py` (R-B4).**
3. **A retired instrument keeps its tombstone.** The auction tail is struck-through **in both threshold tables** with "UNSCOREABLE BY CONSTRUCTION" and a do-not-revive clause (`CLAUDE.md:125`, `THESIS.md:145`, `STATUS.md:108`), plus a machine-readable `monitors/RETIRED_TOKENS.tsv`.
4. **Pre-registration before the print, committed with a timestamp.** The 9/15 20Y-R ceiling was committed at **10:06:44 ET before the auction existed** precisely so a bearish print could not be promoted afterwards (`CHANGELOG.md:21`).
5. **Rulings that go against the desk's own book are recorded as such.** *"The recommendation to pair was BOND's, made against its own book, and Will adopted it verbatim"* (`THESIS.md:100`); the 8/27 dealer-leg question was **halted and asked rather than self-ruled** because answering it would make BOND's own bear thesis easier to confirm (`THESIS.md:124`, now marked SUPERSEDED-and-retained after the ruling landed).

**DEBT (real, verified at the artifact):**
- 🔴 **The desk's own regression suite is RED at HEAD.** `python3 AGENTS/BOND/monitors/assertion_check.py --selftest` exits **rc=1** with *"1 FAILURE(S) — 32 fixtures"*; `closeout_check.py --selftest` therefore also exits 1 (*"FAILURES PRESENT"*, 54 fixtures). Cause: fixture C9 at `assertion_check.py:614-616` pins a payload dated `[8/19]`/`8/20` and grades it against a **live MIN_AGE floor**, so it rots by the calendar. See R-B1.
- 🔴 **`TRADE.md` refutes its own re-base declaration.** `:3`: *"This file carries POSTURE and GATES only. **No marks.**"* `:11`: *"25× TLT Sep-30 77P at 21 DTE [9/9], vendor mid **$0.035** … against TLT **$81.73** [9/9 close] and a fees-in breakeven of **$76.89**."* Eight lines apart. See R-B2.
- 🔴 **`CLAUDE.md:43` (closeout 15) still routes the steady-state feed "→ `NEXUS_BRIEF.md` once Packet 7 lands"** — future tense for a 66,985 B file refreshed today. See R-B3.
- **`MEMORY.md` is at 89% of the read-cap budget** (29,072 B / 32,550) — rotate-tier, not rotated; **6,288 B still owed** to the <70% stop. `SCRATCH.md:11` already carries the receipt: *"MEMORY 89% — rotate-tier, NOT rotated; next session that adds to MEMORY must rotate first."* Declared, not fixed.
- **BOND has ZERO rows in `PROME/registry/READS.tsv`** — so `read_cap_check --agent BOND` runs on the charter **heuristic**, and says so: *"this desk has no declaration … 'clean within what the scan found', NOT a clean bill."* BROCK declared 16 rows on 9/12.
- **The `CLAUDE.md` FILES table (`:224-250`) has fallen behind the tree.** Absent: `NEXUS_BRIEF.md`, `PROTOCOL.md`, `AUDIT.md`, `registry/`, `analysis/`, `setups/`, `proposals/`, `research/`, and 4 of the 12 monitor scripts (`buyback_f2.py`, `dm_cross_section.py`, `watchers.py`, `matrix_v2_base_rate.py`). `NEXUS_BRIEF.md` is named in the charter only at `:29`, `:43` and `:247` — never as a file of record.
- **The charter's CROSS-AGENT SIGNALS table under-states live routing.** `CLAUDE.md:91-110` lists 4 outbound targets (LIQUID/HENRY/REGINALD/ZHAO) and 4 inbound. The live `outbox/` carries packets to **SAM, MIDAS, RED, TERRY, ORACLE, WALTER, VIOLET, LABOR, ZHAO, HENRY, LIQUID, NEXUS**; `THESIS.md:193-194` adds SAM and the REGINALD-FHLB leg. The charter's copy is the thinnest of the three.
- **`CLAUDE.md` §EXIT RULES (`:151-161`) is still generic template text** ("Conditions that completely invalidate the thesis. 1-2 hard stops") while the real four-category apparatus lives in STATUS/THESIS.
- **`monitors/CDX_CASH_BASIS.md` lags STATUS on its own vector.** Monitor `:4`: *"Last Updated: 2026-08-27 … HYG/IEF 0.8567, z20 +0.82."* `STATUS.md:70`: *"HYG/IEF 0.8585, z20 +1.28 [9/8, STALE]."* Both marked, neither wrong; the explainer is 21 days behind.
- **`docket/CATALYSTS.tsv` sits at 74% of budget with 363 B of headroom** to the rotate trigger.

**Floor-not-ceiling note:** BOND's rich local form (the `Rolls up` column, the `Tracked OUTSIDE the composite` list, the `date_class` docket column, the dual-print convention) is **not** blueprint divergence to be corrected. It is the blueprint expressed better.

**Grounding errors a prior pass made — do NOT re-apply:** the 6/29 profile's headline debt *"NEXUS_BRIEF.md ABSENT"* is **REFUTED** — it exists, 310 ln, refreshed 2026-09-17 (`NEXUS_BRIEF.md:3`). *"CLAUDE.md still treats HERMES as a live mail carrier"* is **REFUTED** — zero HERMES occurrences in `CLAUDE.md` or `PROTOCOL.md`. *"MATRIX_V2 approved-but-not-implemented"* is **REFUTED** — adopted and executed 2026-08-27 on Will's ruling (`THESIS.md:102`, `:121`) and **fired for the first time on 2026-09-15** (`CHANGELOG.md:17-27`).

## 5. Load-bearing context / DO NOT TOUCH
- **"Expensive, not broken."** The term-premium-digestion (slow, absorbed) **vs** demand-hole (fast, mechanical, systemic) axis IS the thesis. Do not flatten it.
- **Threshold-vs-mechanism discipline.** `[[finding_threshold_vs_mechanism]]` is wired into closeout 10 (`CLAUDE.md:38`). A threshold can fire while the mechanism holds — the 9/15 20Y-R is the canonical instance (indirect lowest ever recorded on a 20Y **while** direct set a modern-series record and BTC held 2.57). Any edit that collapses these two into one verdict breaks the desk.
- **Durable docs carry NO live values.** `CLAUDE.md`, `THESIS.md` and `TRADE.md` deliberately point at STATUS. Do not "helpfully" backfill numbers — `THESIS.md:17` documents what happens when someone does: *"a durable doc that declares two sentences later that it 'deliberately carries none' of the live values, while carrying a retracted one, is the worst case of the class: **the disclaimer stops the reader checking**."* ⚠️ `TRADE.md:3`-vs-`:11` is a live second instance.
- **Source tags are mandatory on the dashboard.** Every value `[CONF src date]` or `[EST]`; `[STALE date]` beats carried-forward.
- **Composite re-sum, 7 headline rows only.** `VX-BND-01`…`-08`, `-10`…`-14` and `-16` roll up; `VX-BND-09` is RETIRED; `VX-BND-15/17/18/19/20` are explicitly outside the composite. Do not fold them into the /35.
- **⛔ The TLT-put ADD re-arm runs on the OLD, STRICTER conjunctive test** (`STATUS.md:99`, WQ-99 Will 9/1) even though the kill now runs on the NEW `I'` test. Deliberate: *"never loosen an add gate as a side effect of a definition reconcile."*
- **The auction TAIL is retired and NOT revivable** — TreasuryDirect publishes no when-issued. Wire-reported tails are `[med-conf]` and **may never fire anything** (`STATUS.md:108`). `grade_auction.py` computes none by design.
- **Dealer take >18% is contrarian-BULLISH, and dealer is DROPPED as a bearish kill criterion** (Will-ruled 8/27; `STATUS.md:98`, `THESIS.md:102`). Backtest-grounded, counterintuitive; do not "restore" a dealer-stuffing bearish trigger.
- **`rc=0` semantics differ per tool and are load-bearing.** `docket_check` rc0 = "nothing ACTIONABLE", **not** "the window is covered" — read the `VERIFIED ONLY THROUGH` line. `closeout_check` rc2 = fetch failure = **not a pass**. `boot_recompute` rc1 = unguarded drift = **not a pass**.
- **Percentages are of COMPETITIVE ACCEPTED, and bars are derived PER TENOR at grade time.** `MIN_N_FOR_GATE = 6` — a thinner base cannot support a composition gate. Never reuse another tenor's numbers (the 7Y-hardcoded defect, corrected 8/18).
- **outbox 🔴-acute-only** + **WALTER lane at boot vs general inbox as a separate task** (`CLAUDE.md:48`) — protocol-deliberate.
- **`outbox/delivered/` verification is by CONTENT, not filename.** A filename scan flagged 7 of 22 as orphans; HENRY demonstrably had one under a different filing convention (`CLAUDE.md:176-179`).
- **STATUS/CATALYSTS rotation is verbatim + crc32-stamped, never deletion.** `STATUS.md:6` asserts *"NOTHING HAS EVER BEEN DELETED FROM IT"* and names the 160,077 B pre-split snapshot (crc32 `1210262`). Preserve the crc convention on any rotation.

## 6. Maturity snapshot
Grade + confidence live in `FLEET_MAP.tsv` (**not restated here**; the row reads L4 / conf **H**, last_scored 2026-09-01). What this read establishes about the L5 legs:
- The **9/1 FLEET_MAP `Gaps` cell is materially out of date on its own headline blocker**: it says *"NO declared byte tier — STATUS 160,077 B / 250 ln = 492% of the read budget and 295% of the PHYSICAL ceiling (BOND cannot read its own STATUS whole once)."* At HEAD, STATUS is **23,401 B / 146 ln = 72% of budget**, with a declared rotation banner and crc'd archive (`STATUS.md:6-7`). **That leg is DONE.** Re-cut the row.
- The `Next_upgrade` legs that survive as written: **LEDGER_GLOB** (`AGENTS/BOND/workbook/LEDGER_GLOB` does not exist — verified; the workbook holds only FLOW/KB/SCHEMA/VX — so root closeout 1c-bis cannot run for this desk), **PAT-044 two-clock headers on 5 TSVs**, and **the derived-inheritance class fix**.
- **New legs this read adds, not on the map:** (a) a `READS.tsv` declaration — 0 rows; (b) the **red selftest** (R-B1), which is an L4 "signals flowing"/L5 "clean closeouts" problem, not cosmetic; (c) `MEMORY.md` at rotate-tier; (d) `watchers.py` un-invoked.
- New since 9/1 and NOT yet on the map: the F2 per-op carrier + `registry/f2_reads.tsv` (9/17), `dm_cross_section.py` (9/1), `matrix_v2_base_rate.py` (9/2).
- The old profile's `conf M` reasoning (`profiles/BOND.md:67` — "the cross-agent-routing dimension has a live structural hole" = NEXUS_BRIEF absent) **no longer holds**; the map already carries conf H.
Work queue → `upgrades/BOND_CARD.md`; the 8/20 3-reader review → `upgrades/BOND_REVIEW_2026-08-20.md` + `_reader_raw.md`.

## 7. Open questions / comprehension gaps
1. **Is the TLT Sep-30 77P leg still live at HEAD?** `TRADE.md:11` marks it 25× at **$0.035** vendor mid on 9/9 with expiry **9/30** — thirteen days out at this read. Position truth is off-repo (Will/broker). **NOT-ADJUDICATED** by design; do not resolve from STATUS or TRADE (root rule #4 / §Position truth).
2. **Does the 9/18 FR2004 weekly join land?** The desk's declared critical path (`STATUS.md:144`): a live `I'` fire from 9/15 sits on the far side of an **unbuilt** pairing instrument, so the thesis kill is currently **UNEVALUABLE with one leg lit**. **NOT-SEEN** by any instrument available to a reader.
3. **WQ-246 — "sustained" has no session count.** The add-gate's level leg has been through for 4 published sessions and the desk has correctly refused to pick the count *after* knowing the answer. Open with Will. Until ruled, gate (a) **cannot be graded** and silently converts to "never add."
4. **The declared MIRROR DIVERGENCE is in its 9th session un-reconciled** (`STATUS.md:78`): `VX-BND-05`=4 and `VX-BND-16`=4 in `workbook/VX.tsv` vs matrix rows scoring 3 and 2. BOND states the direction (components HOTTER ⇒ the divergence UNDER-states risk) and flags rather than reconciles. Right disposition at 9 sessions, or now debt?
5. **Is `AUCTION_HEALTH.md` (44,774 B) at risk of becoming an unreadable canon surface?** Cited as canonical for the `I'` bars (`STATUS.md:98` → `AUCTION_HEALTH.md:134`) but not a declared boot-read, so no cap binds it. FALSE-POSITIVE-CANDIDATE as a read-cap breach; a real question as a *comprehension* surface.
6. ~~Where does `watchers.py` get invoked?~~ **CLOSED by verification: nowhere.** Zero invocation sites in `CLAUDE.md`, `boot_recompute.py`, `closeout_check.py`, or anywhere else in the repo. It is an un-invoked guard (R-B4). The remaining question is the disposition — wire it, or declare it DELIBERATE and say so in its own docstring the way `gen_automemory_index` does.
7. **NEW — how long has the assertion_check selftest been red?** A time-rotting fixture fails on a calendar boundary, so the break date is not the last-edit date. Needs a `git bisect`-style walk the reader did not run. **NOT-ADJUDICATED.**

## 4 · 🔴 Findings the first reader missed — BOND

| # | Pri | Finding | Locator |
|---|---|---|---|
| **R-B1** | 🔴 | **BOND's own regression suite is RED at HEAD.** `python3 AGENTS/BOND/monitors/assertion_check.py --selftest` → **rc=1**, *"1 FAILURE(S) — 32 fixtures"*, failing fixture *"release-lag caveat inside MIN_AGE does NOT fire — expected False, got True"*. `closeout_check.py --selftest` → **rc=1**, *"COMBINED: 8 numeric + 14 workbook-lint + 32 assertion = 54 fixtures … FAILURES PRESENT"*. **Cause:** the fixture payload is pinned to hardcoded dates `[8/19]` / `8/20` and graded against a *live* MIN_AGE floor, so it ages out of its own guard — `[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]`. The draft graded this layer as the desk's biggest strength and reported fixture counts (35 / 27) that no longer exist | `AGENTS/BOND/monitors/assertion_check.py:614-616`; runs of `--selftest` on both scripts, 2026-09-17 |
| **R-B2** | 🔴 | **`TRADE.md` refutes its own re-base declaration inside 8 lines.** `:3` — *"This file carries POSTURE and GATES only. **No marks.** Every live level, distance, run and score → `STATUS.md`."* `:11` — *"vendor mid **$0.035** … against TLT **$81.73** [9/9 close] and a fees-in breakeven of **$76.89**."* This is the exact class `THESIS.md:17` names ("the disclaimer stops the reader checking"), reproduced in the file re-based to prevent it. The draft quoted both lines in different sections without reconciling them | `AGENTS/BOND/TRADE.md:3` vs `:11` |
| **R-B3** | 🔴 | **`CLAUDE.md:43` (closeout 15) still speaks of `NEXUS_BRIEF.md` in the future tense** — *"→ `NEXUS_BRIEF.md` **once Packet 7 lands**"* — for a 310 ln / 66,985 B live cross-agent surface refreshed **today** (`NEXUS_BRIEF.md:3`). Structurally identical to BROCK's K-8 (`docket/CATALYSTS.tsv` "Phase 2 will replace"); the draft found it at BROCK and missed it at BOND | `AGENTS/BOND/CLAUDE.md:43` vs `AGENTS/BOND/NEXUS_BRIEF.md:3` |
| **R-B4** | 🟠 | **`monitors/watchers.py` + `monitors/WATCH_DATES.tsv` have ZERO invocation sites anywhere in the repo.** A grep over every tracked `.md` and `.py` returns only a memory-file reference and the draft itself. The draft left this **CANNOT-EVALUATE**; it is decidable and the answer is a verified negative. PAT-071 / `CHECKS.tsv` class: *a check with no invocation site is unowned in practice, whoever wrote it* | `grep -rn "watchers.py" --include=*.md --include=*.py .` → no invocation |
| **R-B5** | 🟠 | **The charter carries a dead review date for a live open sub-item.** `CLAUDE.md:77`: US sovereign CDS — *"Will HELD this sub-item, DOCKET deferral, **reconsider 8/24**"* (24 days past). `STATUS.md:107` and `PROTOCOL.md:19` carry the live **12/1** re-test (`KB-BND-261`). Two dates, two surfaces, no cross-reference — and the durable doc holds the dead one | `AGENTS/BOND/CLAUDE.md:77` vs `STATUS.md:107`, `PROTOCOL.md:19` |
| **R-B6** | 🟡 | **`docket/CATALYSTS.tsv`'s `date_class` column has no declared enum and no lint.** Observed values: `confirmed` (17) · `recurring` (3) · `watch` (3) · `estimated` (1). `kb_lint.py` validates KB/VX/FLOW/PREDICTIONS, not the docket, and `ledger_staleness` lists CATALYSTS as outside its perimeter. A state column read by boot 5 with nothing checking it | `awk -F'\t' 'NR>1{print $NF}' AGENTS/BOND/docket/CATALYSTS.tsv \| sort \| uniq -c`; `ledger_staleness.py BOND` perimeter line |

---
---

# ██ DESK 2 — BROCK ██

## 1 · Verification table

| § | Claim (≤20 words) | Verdict | Correction |
|---|---|---|---|
| Hdr | `CLAUDE.md` 247 ln / 24,688 B | VERIFIED | |
| Hdr | `STATUS.md` 123 ln / 31,963 B | VERIFIED | |
| Hdr | Staleness ①: STATUS `**Convergence: NN/70**` = **57/70** | VERIFIED | `STATUS.md:65` |
| Hdr | Staleness ②: `BRK-02` `Status` = OPEN, resolver 2026-09-30 | VERIFIED | `PREDICTIONS.tsv` row `BRK-02` |
| Hdr | Staleness ③: `AGENTS/BROCK/thesis/` appears | VERIFIED | `git ls-files` empty today |
| Hdr | Staleness ④: `read_cap_check --agent BROCK` rc≠0 | VERIFIED | live rc=0 |
| Hdr | Staleness ⑤: `trade/TRADE.md:1` loses `🧊 FROZEN` | VERIFIED | `:1` carries it |
| §1 | Core thesis at `CLAUDE.md:12-14` (PIK ~6% vs 2.1%, $482B bifurcated) | VERIFIED | `:12` core, `:14` second layer |
| §1 | Transmission matrix at `CLAUDE.md:195-217` | VERIFIED | heading `:195`, next `:221` |
| §1 | Cessions: insurer NUMBERS→SHADE (6/26), EU seam→HANS (8/28) at `NEXUS_BRIEF.md:4` | VERIFIED | verbatim |
| §1 | Routing rule at `CLAUDE.md:77`, `:247`, corrected 2026-09-03 | VERIFIED | both verbatim, both name the 9/3 correction |
| §2 | ~334 tracked files | VERIFIED | `git ls-files` = 334 |
| §2 | `STATUS.md` 31,963 B = **98%** of budget | VERIFIED | tool prints 98% |
| §2 | REGIME BLOCK 5-line at `:14-20` | VERIFIED | heading `:14`, 5 numbered lines `:16-20` |
| §2 | 14-vector matrix + `Independence map` at `:63`; arithmetic at `:66` | VERIFIED | both verbatim |
| §2 | TRIGGER LADDER `:98-100`; THESIS-KILL DECISION TREE `:102` | VERIFIED | headings `:98`, `:102` |
| §2 | `FLOW.tsv` **25 pathways**, LIVE hdr 9/12, `-024`/`-025` newest | VERIFIED | 25 ids; header refresh 2026-09-12 |
| §2 | `KB.tsv` **276 data rows / 258,682 B** | VERIFIED | |
| §2 | `VX.tsv` **25 vectors**, LIVE hdr 9/3, `Category` taxonomy, owner-fence | VERIFIED | fence verbatim: "cite the owner, do not read a level off this file" |
| §2 | `PREDICTIONS.tsv` 22 rows / 48,681 B, declared `scoped` | VERIFIED | 22 `BRK-` rows |
| §2 | 10 cols incl. `Invalidation` + `Action_If_Falsified` | VERIFIED | `Action_If_Falsified` = col 9 |
| §2 | Status enum OPEN·PARTIAL·REMOVED·SUPERSEDED·RESOLVED-TRUE·RESOLVED-FALSE-LETTER | VERIFIED | all six present, no others |
| §2 | **11 OPEN**; `BRK-02` resolves 9/30 | **FAILED** | **13 OPEN** (PARTIAL 1 · REMOVED 5 · SUPERSEDED 1 · RESOLVED-TRUE 1 · RESOLVED-FALSE-LETTER 1). `BRK-02` 9/30 VERIFIED |
| §2 | `PC_REDEMPTION_REGISTER.tsv` 24 rows, LIVE hdr, gate legs in the header | VERIFIED | 24 data rows; `# Status: LIVE (explicit declaration …)` |
| §2 | `PUBLISHED.tsv` 21 · `VX_HISTORY.tsv` 16 · `KB_ARCHIVE_MAR26` 100 | VERIFIED | all three |
| §2 | `BANK_BDC_MATRIX` + `BDC_CASH_COVERAGE` FROZEN with banners | VERIFIED | `# FROZEN 2026-07-04` / `# FROZEN 2026-06-26` |
| §2 | `board_log.tsv` **121 rows / 89,476 B**, declared `grep` | VERIFIED | 121 data rows |
| §2 | board_log cols `timestamp_read · signal_id · disposition · source · notes` | VERIFIED | exact |
| §2 | disposition enum ∈ {acted, noted, deferred, info-only, skipped} | VERIFIED | enum declared at `CLAUDE.md:37`; observed in data: acted 42 · info-only 47 · noted 32 (deferred/skipped unused) |
| §2 | `docket/CATALYSTS.tsv` 42 data rows, 8 col | VERIFIED | 44 lines, 42 dated rows |
| §2 | `date_class` ∈ **{hard, confirmed, modeled}** | **FAILED** | observed **8** values: `confirmed` 20 · `modeled` 12 · `hard` 6 · `estimated` 1 · `fired` 1 · `standing` 1 · `attempted-unresolved` 1 · **one BLANK cell** |
| §2 | `LESSONS.md` 84 ln / 31,469 B = 97%, numbered through **#35**, grouped by session date | VERIFIED | max #35; headings are session-dated |
| §2 | `SCRATCH.md` 199 ln / 46,122 B | VERIFIED | |
| §2 | `MAINTENANCE.md` 6,747 B, change-log + ranked MODERNIZATION BACKLOG | VERIFIED | `:41` carries the ranked row |
| §2 | `NEXUS_BRIEF.md` 121 ln / 34,501 B | VERIFIED | |
| §2 | `EXPECTED_SIGNALS.md` 4,655 B, no live values, last reviewed 2026-03-06 | VERIFIED | `:5` |
| §2 | `trade/TRADE.md` 287 ln, 🧊 FROZEN 2026-07-27, condition-not-lifecycle | VERIFIED | `:1-9` exact |
| §2 | `trade/{NAMES,CROSS_ANALYSIS}.md` + `trade/APO/` (4) | VERIFIED | 7 tracked files under `trade/` (the working tree also holds untracked ARCC/ARES/KKR/OWL/WFC/NATIONAL_DENTEX dirs) |
| §2 | `tools/soi_nonaccrual.py` validated exact 25 loans / 15 issuers, BCRED Q2-2026 `0001803498-26-000048` | VERIFIED | docstring verbatim; names two silent corrupters |
| §2 | `domain/sources/` (33) · `research/` (16) · `archive/` (23) · `inbox/WALTER/processed/` (~190) | **FAILED (2 of 4)** | `domain/sources/` **33** ✓ · `archive/` **23** ✓ · `research/` = **17** · `inbox/WALTER/processed/` = **107** (plus `inbox/processed/` **75**; 200 inbox files total) |
| §2 | `OPEN_ITEMS_2026-09-03.md` · `OPEN_THREADS_2026-07-09.md` · `ARCH_REPORT_2026-06-26.md` | VERIFIED | all three tracked |
| §3 | Thesis structure: no `thesis/` dir; `MAINTENANCE.md:41` ranks it backlog #3 MED/MED deferred | VERIFIED | verbatim; `:8` admits the gap |
| §3 | Convergence `STATUS.md:42-71`; `Rescored` col; `:63` Independence map; `:66` arithmetic; `:67-69` signed reasons | VERIFIED | heading `:42`, EXIT at `:73` |
| §3 | Invalidation `STATUS.md:73-103` + `CLAUDE.md:145-170` | VERIFIED | headings `:73`/`:145`, next `:104`/`:174` |
| §3 | Decision tree needs 2-of-3; 8/28 run recorded 0-of-3 | VERIFIED | `STATUS.md:102` heading states "RUN 2026-08-28, 0 of 3 REVERSED" |
| §3 | Retired kill leg struck-through with the base rate `:77-80` | VERIFIED | `:77` struck row, `:80` the n=787 blockquote |
| §3 | Doc Ownership table `CLAUDE.md:112-125` | VERIFIED | heading `:112`, next `:129` |
| §3 | `BRK-NN` ids charter-mandated at `CLAUDE.md:109` | VERIFIED | charter writes `BRK-xx` |
| §3 | Routing `CLAUDE.md:195-217` + `:76-93` Signal Protocol | VERIFIED | Signal Protocol `:76`, next heading `:95` |
| §3b | `STATUS.md:75-80` §1 · `:82-85` §2 · `:87-89` §3 · `:91-96` §4 | **DRIFTED** | sections run `:75-81` · `:82-86` · `:87-90` · `:91-97` (headings correct; each range ends one line short) |
| §3b | `:70` carries the live count "2 of 3" | VERIFIED | verbatim |
| §3b | `STATUS.md:3` `**Updated:**` stamp | VERIFIED | `:3` = `**Updated:** 2026-09-12 …` |
| §3b | `VX.tsv` two-clock header 2026-09-03; `FLOW.tsv` 2026-09-12 | VERIFIED | both verbatim |
| §3b | `ledger_staleness` reports the two frozen ledgers FROZEN +70d / +78d | VERIFIED | exact |
| §4-1 | Two-state rule fully satisfied; zero silent-rot rows; `FLOW.tsv:1` "That alert is the point, not a defect" | VERIFIED | verbatim; run shows 2 FROZEN + 6 ok, no rot |
| §4-1 | `ledger_staleness.py BROCK` → "8 scanned" | **FAILED** | tool prints **"12 ledger(s) scanned; 3 TSV(s) NOT scanned"**; 8 rows displayed. The 8 row-verdicts themselves VERIFIED |
| §4-2 | `trade/TRADE.md:1-9` freeze banner is the fleet exemplar | VERIFIED | all five stated properties present |
| §4-3 | `Independence map` line at `STATUS.md:63` | VERIFIED | verbatim |
| §4-4 | `MAINTENANCE.md` anti-ritual clamp "do NOT wire it into the every-session closeout" | VERIFIED | present |
| §4-5 | 16 rows in `PROME/registry/READS.tsv`, modes whole/scoped/grep/summary | VERIFIED | rows `:190-205`, all dated 2026-09-12 |
| §4-5 | **desk #3 to file, 9/12** | **FAILED** | ATTESTATION rows: **PROME 2026-08-31, BROCK 2026-09-12, RED 2026-09-14, WALTER 2026-09-15**. BROCK is the **2nd** attesting desk, the 1st domain desk |
| §4-5 | `CLAUDE.md:32` "48,681 B = 149% of the 32,550 B budget"; `:36` "89,476 B: 275% … 165% of the CAP ITSELF" | VERIFIED | both verbatim |
| §4-6 | ALWAYS/SCALED tiering + two named clamps at `CLAUDE.md:24-26` | **DRIFTED** | both clamps are at **`:24`** ("Two clamps, non-negotiable"); `:26` is a separate "quality > completeness" rule |
| §4-7 | HY OAS <260 kill re-labelled; n=787, once, longest run 1 session (`STATUS.md:80`) | VERIFIED | verbatim |
| §4 | STATUS 98% / LESSONS 97%; 9,179 B + 8,685 B owed; ~63,400 B of rotate-tier at boot | VERIFIED | tool prints both figures exactly; 31,963+31,469 = 63,432 |
| §4 | `SCRATCH.md:3` "Read at boot (after STATUS), refreshed at closeout"; `CLAUDE.md:28-39` omits it; READS.tsv has no SCRATCH row; ATTESTATION says `manifest-complete` | VERIFIED | all four legs; 46,122 B = 142% |
| §4 | `docket/CATALYSTS.tsv` 29,434 B, no boot step, no READS row, `CLAUDE.md:48` future tense | VERIFIED | `:48` verbatim: *"Phase 2 will replace this informal version with `docket/CATALYSTS.tsv`"* |
| §4 | `PRIVATE_CREDIT_CONTAGION_TRACKER.md:3` = 2026-04-02, 168 days, no banner | VERIFIED | |
| §4 | `PREDICTIONS_SCOREBOARD.md` 70 days behind; `:3` 2026-07-09, n=10 | VERIFIED | `:3`, `:7`, `:11` (7/10 = 70%, Brier 0.216) |
| §4 | `NEXUS_BRIEF.md:7` carries **59/70 HELD** vs STATUS **57/70**, 15 days stale | VERIFIED | both verbatim |
| §4 | `EXPECTED_SIGNALS.md` 195 d · `trade/NAMES.md` 139 d | VERIFIED | `:5` = 2026-03-06; `NAMES.md:3` = 2026-05-01 |
| §4 | `CLAUDE.md:227-247` FILES table omits 11 surfaces | VERIFIED | heading `:227`, file ends `:247` |
| §4 | `workbook/LEDGER_GLOB` does not exist | VERIFIED | |
| §5 | `STATUS.md:63` and `:71` independence quotes | VERIFIED | both verbatim |
| §5 | `BRK-25`/`BRK-26` cite §9 in `Action_If_Falsified` | VERIFIED | `trade/TRADE.md:5` states it; PREDICTIONS col 9 |
| §5 | `STATUS.md:83` APO mark 14 days stale on the 8/14 FORGE vintage | VERIFIED | verbatim, incl. "$0.05 … FORGE D-21: not readable as realizable" |
| §5 | `PC_REDEMPTION_REGISTER.tsv:1` explicit `# Status: LIVE` explains its own RETIRED/SUPERSEDED prose | VERIFIED | verbatim |
| §5 | `git mv` not bash `mv` at `CLAUDE.md:38` | VERIFIED | verbatim |
| §5 | Pre-commit git-status check `CLAUDE.md:55`, installed after a SHADE file pre-staged | VERIFIED | verbatim |
| §6 | FLEET_MAP `Gaps` stale in three cells (59/70, 54,250 cap framing, "Dark since 8/28") | VERIFIED | all three phrases present in the cell |
| §6 | `Next_upgrade` = "L5 blocker external; a declared byte-budget block (TERRY form) is the one cheap self-leg" | VERIFIED | verbatim |
| §6 | 31 self-commits in the period, on 9/02, 9/03, 9/09, 9/12 | VERIFIED | 69 total / 31 self / 38 routed-in |
| §7-1 | SCRATCH boot-read contradiction | VERIFIED | and stronger — see 🔴 R-K4 |
| §7-3 | OBDC two bases 2.3→2.8 amortized vs 1.1→0.8 fair value; BROCK refused to rule | VERIFIED | `STATUS.md:108`, `:110` verbatim |
| §7-4 | 9/18 CRMT in `PROME/DOCKET.tsv` line 343, absent from BROCK's docket | VERIFIED | `DOCKET.tsv:343` carries the 2026-09-18 CRMT row; BROCK docket dates ≥9/13 are 9/15, 9/21, 9/30×2, 10/31, 11/13, 12/03, 2027-04-30 |
| B5 | K-2: `STATUS.md:3` "9/18 now registered at DOCKET L343" vs `:35` "REGISTERED NOWHERE" | VERIFIED | both verbatim; header is TRUE |
| B5 | K-10: 15 pending `inbox/WALTER/*.md` + 1 root packet | VERIFIED | exact |

## 2 · Totals — BROCK

| Verdict | Count |
|---|---:|
| **VERIFIED** | **73** |
| **FAILED** | **5** |
| **DRIFTED** | **2** |
| **UNLOCATED** | **0** |
| **Total claims graded** | **80** |

---

## 3 · CORRECTED PART A — BROCK

# Agent Profile — BROCK

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P1 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** Mode-A — 1 reader solo read at HEAD + 1 independent locator verifier (fan-out leg P1 of the 2026-09-17 refresh wave)
**Sources read:** `CLAUDE.md` (247 ln / 24,688 B, whole) · `STATUS.md` (123 ln / 31,963 B, whole) · `LESSONS.md` (84 ln, headings + head) · `SCRATCH.md` (head) · `MAINTENANCE.md` (incl. MODERNIZATION BACKLOG) · `EXPECTED_SIGNALS.md` (head) · `NEXUS_BRIEF.md` (head) · `OPEN_ITEMS_2026-09-03.md` · `ARCH_REPORT_2026-06-26.md` (head) · `workbook/` (all 14) · `docket/CATALYSTS.tsv` · `board_log.tsv` (header + tail) · `trade/{TRADE,NAMES,CROSS_ANALYSIS}.md` · `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` · `tools/soi_nonaccrual.py` · `registry/corrections_receipts.tsv` · newest `domain/sources/` (9/9–9/12) · `PROME/registry/READS.tsv` BROCK rows · `git log --after=2026-09-01 -- AGENTS/BROCK/`. **SKIPPED:** `archive/research-outputs/RP-BRK-*` (8), `archive/domain-sources/` incl. PNG/JPG, the 182 processed inbox items, `research/` pre-Jul memos.
**Staleness:** refresh when ANY fires — (1) `AGENTS/BROCK/STATUS.md` `**Convergence: NN/70**` leaves **57/70**; (2) `AGENTS/BROCK/workbook/PREDICTIONS.tsv` row `BRK-02` `Status` leaves **OPEN** (resolver 2026-09-30); (3) a directory `AGENTS/BROCK/thesis/` appears (MAINTENANCE.md backlog item #3); (4) `python3 scripts/read_cap_check.py --agent BROCK` returns **rc≠0**; (5) `AGENTS/BROCK/trade/TRADE.md:1` loses its `🧊 FROZEN` banner; or (6) **> 45 days** from the vintage above ⇒ **2026-11-01**.
*Machine-evaluable in one command:* `grep -c 'Convergence: 57/70' AGENTS/BROCK/STATUS.md; awk -F'\t' '$1=="BRK-02"{print $6}' AGENTS/BROCK/workbook/PREDICTIONS.tsv; git ls-files AGENTS/BROCK/thesis/ | wc -l; python3 scripts/read_cap_check.py --agent BROCK >/dev/null; echo rc=$?; sed -n 1p AGENTS/BROCK/trade/TRADE.md | grep -c '🧊 FROZEN'` — all five legs read from named artifacts. **YES, evaluable.**

> A Profile is DAEDALUS's **durable understanding** of a heavy agent — the map of the labyrinth. Section-tasks read the relevant slice of THIS, not the raw agent. Compressed but faithful; never a substitute for reading the actual file when applying a change.

---

## 1. Identity
**Private credit / BDC contagion** — BDC financials (PIK %, dividend coverage, NAV, non-accruals), private-credit defaults and maturity walls, redemption/gate mechanics, alt-asset managers (APO/OWL/BX/KKR/ARES), Athene–Apollo insurance-credit linkage, ILS/reinsurance, **AI-infrastructure lending (neocloud, GPU collateral)**, fund finance / warehouse-line utilisation, software-sector marks. **Class:** Market (grade in `FLEET_MAP.tsv`, not restated). **Spawnable by:** PROME / Will.

**Core thesis (`CLAUDE.md:12-14`):** *"Private Credit's Public Reckoning"* — PIK masks a ~6% shadow default rate vs a reported 2.1%; the $482B BDC market is **bifurcated** (disciplined top tier vs a fragile long tail burning cash); AI-infra lending is 2000-style vendor financing. **Second layer:** insurance/reinsurance reflexivity loops.

**Transmission (`CLAUDE.md:195-217`):** sends to **REGINALD** (BDC↔bank warehouse, shared portfolio-company markdowns, PIK >20% of TII at FSK/ARCC), **LIQUID** (revolver draws, NAV-facility LTV breaches, gates), **OTTO** (BDC earnings / DQ), **LABOR** (portfolio-company layoffs), **HAWK** (insurance capacity), **ALL** on APO<$100 or an Athene RBC breach. Receives from HAWK / HENRY / LIQUID / REGINALD / OTTO.

**Cessions are unusually explicit and have grown:** HY OAS → LIQUID · VIX/macro → HENRY · bank CRE + bank-level scores → REGINALD · **insurer-exposure NUMBERS → SHADE (Will 6/26)** · **the EU bank/private-credit seam → HANS at full depth (Will 8/28)** (`NEXUS_BRIEF.md:4`). BROCK keeps only the insurer-**as-lender** leg.

**Routing rule, corrected 2026-09-03:** **SIGNALS → WALTER** (never direct); **ANALYSIS and PACKETS → straight into the recipient's `inbox/`** under root carve-out ①; **`outbox/` is for PROME-action requests only** (`CLAUDE.md:77`, `:247`). This line previously instructed direct signal delivery and was fixed on DAEDALUS's fleet census.

**What it's for:** *"Is private credit cracking, and where does it transmit to banks?"*

## 2. File anatomy (where the richness lives) — HEAVY, 334 tracked files, 6 layers
| File | Holds | Richness? |
|---|---|---|
| `STATUS.md` (123 ln / **31,963 B = 98% of budget 🟠**) | **REGIME BLOCK (5-line, `:14-20`)** · near-window catalyst calendar (`:24-41`) · **14-vector convergence matrix + an explicit `Independence map` line (`:63`)** · composite arithmetic printed (`:66`) · 4-part EXIT RULES (`:73-97`) incl. a **TRIGGER LADDER** migrated from the frozen TRADE.md (`:98-101`) · **THESIS-KILL DECISION TREE** (`:102`) · BOTTOM LINE (`:104`) | **live state — and BROCK's de-facto thesis surface** |
| `workbook/FLOW.tsv` (**25 pathways**, LIVE hdr 9/12) | **the contagion engine** — `FLOW-BRK-001`→`-025` with Speed (DAYS/WEEKS/MONTHS/QUARTERS) + Layer + Status. Newest two are the period's own findings: `-024` *Measurement-Basis Masking* and `-025` *Weekly-Leash Bridging* | **exemplary; exceeds blueprint** |
| `workbook/KB.tsv` (**276 data rows / 258,682 B**) | canonical 13-col record; Admiralty `Conf` A1–F6 + EMPIRICAL/ESTIMATE/ASSUMPTION | permanent record |
| `workbook/VX.tsv` (**25 vectors**, LIVE hdr 9/3) | `VX-BRK-001`→`-025` with a `Category` taxonomy (BDC_Health · Credit_Marks · Liquidity · Contagion · Default_Rates · Market_Signal · Sponsor_Strategy · Cross_Channel · Gate_Cascade · Price_Discovery · Regulatory_Legal · Structure). **Header carries an explicit *"cite the owner, do not read a level off this file"* fence** | permanent record |
| `workbook/PREDICTIONS.tsv` (22 rows / **48,681 B — declared `scoped`, NEVER read whole**) + `PREDICTIONS_ARCHIVE.tsv` + `PREDICTIONS_SCOREBOARD.md` | 10 cols incl. **`Invalidation`** (col 8) and **`Action_If_Falsified`** (col 9); status enum used in practice: OPEN · PARTIAL · REMOVED · SUPERSEDED · RESOLVED-TRUE · RESOLVED-FALSE-LETTER. **13 OPEN · 1 PARTIAL · 5 REMOVED · 1 SUPERSEDED · 1 RESOLVED-TRUE · 1 RESOLVED-FALSE-LETTER**; `BRK-02` resolves 9/30 | **institutional learning loop** |
| `workbook/PC_REDEMPTION_REGISTER.tsv` (24 rows, LIVE hdr) | **the definition surface for `GATE-BRK-R2`** — registered 9/3; the header itself carries the gate's (a)/(b) legs, state, and the dated corrections against them | **a genuine local invention: a ledger that IS a spec** |
| `workbook/PUBLISHED.tsv` (21 rows) · `VX_HISTORY.tsv` (16) · `SCHEMA.tsv` · `KB_ARCHIVE_MAR26.tsv` (100) | published-claim register · retired vectors · data dictionary · KB archive | supporting record |
| `workbook/{BANK_BDC_MATRIX,BDC_CASH_COVERAGE}.tsv` | **both FROZEN with banners** (`# FROZEN 2026-07-04` / `# FROZEN 2026-06-26`) — the two-state rule satisfied, verified by `ledger_staleness` (+70d / +78d) | correctly dead |
| `board_log.tsv` (**121 rows / 89,476 B — declared `grep`, NEVER read whole**) | append-only WALTER-consumption ledger: `timestamp_read · signal_id · disposition · source · notes`. Spec enum = {acted, noted, deferred, info-only, skipped} (`CLAUDE.md:37`); **observed in 121 rows: acted 42 · info-only 47 · noted 32** — `deferred` and `skipped` have never been used. Per `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.2 | **permanent record; the fleet's fullest signal-consumption audit trail** |
| `docket/CATALYSTS.tsv` (42 dated rows, 8 col, 29,434 B) | dated catalysts. ⚠️ **`date_class` has no declared enum and no lint:** observed `confirmed` 20 · `modeled` 12 · `hard` 6 · `estimated` 1 · `fired` 1 · `standing` 1 · `attempted-unresolved` 1 · **one blank**. `modeled` is the BROCK marker for a window inferred from filer history rather than announced | forward state — **but see §4, it is not boot-read and nothing lints it** |
| `LESSONS.md` (84 ln / **31,469 B = 97% of budget 🟠**) | numbered mistake patterns (through **#35**), grouped by date-of-session with emoji severity; **boot read 2** | **learning engine — and the one that gates future predictions** |
| `SCRATCH.md` (199 ln / 46,122 B = **142% of budget**) | NEXT-BOOT ranked first moves · open debts · watch order · FOLLOW-UP tiers · SESSION LOG · workbook/mail/git health block. ⚠️ **`:4` `**Updated:** 2026-09-03` while the file was edited 9/9 and 9/12** (R-K1) | session handoff — **but see §4: no boot step reads it and no closeout step writes it** |
| `MAINTENANCE.md` (47 ln / 6,747 B) | structural change-log (**Trigger / What changed / Files touched / Boot-impact / Lessons**) + a ranked **MODERNIZATION BACKLOG** scored *leverage ÷ effort × tack-on-fit*, with an explicit anti-ritual clamp | **a genuine local invention — no other desk read carries one** |
| `NEXUS_BRIEF.md` (121 ln / 34,501 B) | curated cross-agent synthesis feed, refreshed at closeout | cross-agent channel — **stale, see §7** |
| `EXPECTED_SIGNALS.md` (147 ln / 4,655 B) | durable banded rules, **NO live values** (the HENRY pattern) | durable method — `Last reviewed: 2026-03-06` (`:5`) |
| `trade/TRADE.md` (287 ln / 23,589 B) | **🧊 FROZEN 2026-07-27 with a CONDITION-not-lifecycle banner** (`:1-9`) naming exactly what was stale and where §9 migrated. §1–§8 kept in-tree as a readable record of how the position was reasoned | **the fleet's exemplar freeze banner** |
| `trade/{NAMES,CROSS_ANALYSIS}.md` + `trade/APO/` (4) — **7 tracked** | 5-tier names list w/ promotion log · 4-entity cross-pattern synthesis (99.7¢ ceiling, spread-compression-universal) · APO/Athene deep dives. *(The working tree also holds untracked `ARCC/ ARES/ KKR/ OWL/ WFC/ NATIONAL_DENTEX/` dirs — not in `git ls-files`.)* | deep multi-firm analysis — vintages 3/16–5/01 |
| `tools/soi_nonaccrual.py` (156 ln) | SOI non-accrual extractor. **Validated exact (25 loans / 15 issuers) against BCRED Q2-2026 `0001803498-26-000048`**; the docstring names the two silent corrupters it handles | **tooling — built 9/3, the desk's first real script** |
| `domain/sources/` (33) · `research/` (**17**) · `archive/` (23) · `inbox/` (**200 files: 107 `WALTER/processed/` + 75 `processed/` + 15 pending WALTER + 1 pending root**) | per-session primary reads and memos · pre-Jul research corpus · crc'd STATUS rotations · consumed signals | deep — read newest 2–3 only |
| `OPEN_ITEMS_2026-09-03.md` · `OPEN_THREADS_2026-07-09.md` · `ARCH_REPORT_2026-06-26.md` | Will-commissioned 5-col inventory (item · class OPEN/PENDING/OWED/BROKEN/BLOCKED · whose move · dated? · artifact) · prior threads · 6/26 architecture report | one-off records |

*The key question this answers: when I grade section X, which file do I actually read?* — **for BROCK the answer is almost always `STATUS.md` plus one ledger, because this desk has no `thesis/` layer.**

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | `CLAUDE.md:12-14` (core + second layer) + `STATUS.md:14-20` **REGIME BLOCK** + `workbook/FLOW.tsv` (25 pathways) + `trade/NAMES.md` cascade + `trade/CROSS_ANALYSIS.md` | **no `thesis/` directory and no versioned doc** — the standing argument is split across a charter paragraph, a 5-line regime block rewritten each session, and the FLOW ledger. `MAINTENANCE.md:41` registers this as backlog item #3, ranked MED/MED and deferred; `:8` admits it | **content exemplary, HOUSING is the gap** |
| Convergence / scoring | `STATUS.md:42-71` | 14 vectors, cols `Vector \| current \| Δ \| Threshold → next level \| Rescored`; **a per-vector `Rescored` date**; composite arithmetic printed (`:66`); **an explicit `Independence map` line** naming which vectors share a node and vote once (`:63`); downgrades carry a signed reason paragraph each (`:67-69`) | **strong — the Δ column + per-vector rescore dates are better than blueprint** |
| Invalidation / exit | `STATUS.md:73-103` (4 numbered categories: `:75-81` · `:82-86` · `:87-90` · `:91-97`, + §5 TRIGGER LADDER `:98-101` + a 5-step **THESIS-KILL DECISION TREE** `:102`) + `CLAUDE.md:145-170` | literal thresholds with FIRED/NOT-FIRED and session counts; **the decision tree needs 2-of-3 reversals to override and the 8/28 run is recorded as 0-of-3**; a retired kill leg is kept struck-through with the base rate that killed it (`:77-80`) | **exemplary** |
| Thresholds | `EXPECTED_SIGNALS.md` (durable, no live values) + `workbook/VX.tsv` bands + `STATUS.md` matrix "Threshold → next level" column + `PC_REDEMPTION_REGISTER.tsv` header (gate definitions) | durable-vs-live split enforced by the Doc Ownership table (`CLAUDE.md:112-125`); conjunction triggers; **registered `GATE-*` ids shared with the fleet registry** | conformant |
| Predictions | `workbook/PREDICTIONS.tsv` + `_ARCHIVE` + `_SCOREBOARD.md` + `LESSONS.md` | `BRK-xx` ids (charter-mandated, `CLAUDE.md:109`); `Invalidation` **and** `Action_If_Falsified` columns — the latter is a genuine blueprint-plus; Brier + hit-rate scoreboard; failure synthesis feeds LESSONS | **strong — but three live counts of one ledger disagree, see R-K2** |
| Cross-agent routing | `CLAUDE.md:195-217` route matrix + `:76-93` Signal Protocol + `NEXUS_BRIEF.md` + `board_log.tsv` | condition→target→priority; **SIGNALS→WALTER / PACKETS→inbox / outbox=PROME-only** three-way split, corrected 9/3; WALTER consumption is **logged row-by-row with a disposition token** | **conformant → exemplary on the inbound side** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)
| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `STATUS.md:75-81` §1 Thesis Kill | the 100% private-credit overlay | `**Updated:**` at `:3` | `NOT FIRED` / `~~struck~~ RETIRED AS A KILL <date> (WQ-nnn)` |
| `STATUS.md:82-86` §2 Position-Specific | the APO Dec $95P | same | `🔴 FIRED 8/12` + the ruling that followed |
| `STATUS.md:87-90` §3 Convergence Downgrades | the timeline, not the thesis | same | `NOT FIRING (0 this session)` — and `:70` carries the live count **2 of 3** |
| `STATUS.md:91-97` §4 Time-Based / prediction-linked | individual `BRK-*` rows | per-row resolver dates | `NOT GRADED` / `COUNT STAYS AT 2` / `55% HELD` |
| `STATUS.md:98-101` §5 TRIGGER LADDER | 11 registered triggers (migrated from frozen `trade/TRADE.md` §9) | `State, 9/2:` | `2 of 11 FIRED, both reviewed and closed` · `1 RESOLVED NEGATIVE` · `1 RE-LABELLED` |
| `STATUS.md:102` THESIS-KILL DECISION TREE | overrides a compression-driven kill | `RUN 2026-08-28` in the heading | `0 of 3 REVERSED` per-leg with ❌/✅ |
| `workbook/PREDICTIONS.tsv` `Status`+`Invalidation`+`Action_If_Falsified` | each registered claim | `Made_Date`/`Resolve_Date` | OPEN · PARTIAL · REMOVED · SUPERSEDED · RESOLVED-TRUE · RESOLVED-FALSE-LETTER |
| `workbook/PC_REDEMPTION_REGISTER.tsv` header | `GATE-BRK-R2` legs (a)/(b) | `# Status: LIVE` + dated in-header corrections | state sentence naming the vehicle count and the next live read date |
| `workbook/VX.tsv` `Threshold`/state cells | per-vector level | `# Last real data refresh: 2026-09-03` two-clock header | score + category |
| `workbook/FLOW.tsv` `Status` | a contagion pathway's existence | `# Last real data refresh: 2026-09-12` | ACTIVE/ARMED/FIRED/BUILDING/LATENT |
| `workbook/{BANK_BDC_MATRIX,BDC_CASH_COVERAGE}.tsv` | **nothing — correctly dead** | `# FROZEN <date>` banner | banner presence; `ledger_staleness` reports FROZEN +70d / +78d |
| `trade/TRADE.md:1` | **nothing — correctly dead**; §9 migrated to STATUS §5 | `🧊 FROZEN 2026-07-27` + condition paragraph | banner presence |

## 4. Deviations from standard (+ why)
**BETTER than blueprint:**
1. **The two-state ledger rule is fully satisfied, and visibly.** Two ledgers FROZEN with banners, six LIVE with **content-derived two-clock headers** (`# Status: LIVE. Last real data refresh: YYYY-MM-DD (content-derived — newest cell in the file)`) that name PAT-044 and tell `ledger_staleness.py` to read that line and never mtime. `ledger_staleness.py BROCK` returns **zero silent-rot rows** (tool line: *"12 ledger(s) scanned; 3 TSV(s) NOT scanned"* — 2 FROZEN, 6 ok). Several headers *explain why the file will read days behind* — *"That alert is the point, not a defect"* (`FLOW.tsv:1`).
2. **`trade/TRADE.md`'s freeze banner is the fleet exemplar** (`:1-9`): it states the freeze as a **condition, not a lifecycle**, enumerates exactly which figures were stale and by how much, names the load-bearing §9 and where it migrated, points at position truth off-repo, and says why the file stays in-tree.
3. **An explicit `Independence map` line under the convergence matrix** (`STATUS.md:63`) naming which vectors share an antecedent and vote once. BROCK solved the no-double-count problem the 6/28 profile flagged as a handle gap.
4. **`MAINTENANCE.md` — a structural change-log + ranked modernization backlog**, with an explicit anti-ritual clamp: *"do NOT wire it into the every-session closeout."* No other desk read carries this.
5. **Read-cap perimeter is DECLARED and ATTESTED**, 16 rows in `PROME/registry/READS.tsv` (`:190-205`, all 2026-09-12 — the **second** desk to attest after PROME 8/31, and the first domain desk; RED 9/14 and WALTER 9/15 followed), with per-row modes `whole/scoped/grep/summary`. Two boot steps were **rewritten to be un-whole-readable** (`CLAUDE.md:32`, `:36`) and each carries the arithmetic: PREDICTIONS *"48,681 B = 149% of the 32,550 B read-cap budget"*; `board_log.tsv` *"89,476 B: 275% of the read-cap budget and 165% of the CAP ITSELF."*
6. **ALWAYS / SCALED closeout tiering** with a Live-event override carrying **two named clamps** (`CLAUDE.md:24` — *"Two clamps, non-negotiable"*) — the override defers timing, never waives; ALWAYS steps fire regardless.
7. **A retired kill leg keeps its base rate.** The `HY OAS <260 for 10+ sessions` kill was re-labelled to an OBSERVABLE because BROCK's own measurement showed it closed <260 **exactly once in three years (n=787), longest run 1 session** — *"a kill that was never reachable in its own sample"* (`STATUS.md:80`). Label corrected on Will's word; no threshold moved.

**DEBT (real, verified at the artifact):**
- **No `thesis/` layer.** The standing argument has no versioned home and no changelog; `MAINTENANCE.md:8` admits it and `:41` ranks the build as backlog #3, deferred. Consequence: every thesis pivot is traced through STATUS prose that is rewritten each session and rotated to `archive/`. This is the desk's **largest structural gap**, and it is self-registered.
- **`STATUS.md` 31,963 B = 98% of budget; `LESSONS.md` 31,469 B = 97%.** Both rotate-tier. Rule-5 stop is <22,785 B ⇒ **9,179 B** and **8,685 B** still owed respectively. Both are boot reads 1 and 2, i.e. this desk's boot loads **63,432 B** of rotate-tier surface before it does anything.
- 🔴 **`SCRATCH.md` is claimed at both ends of the session and wired at neither.** `SCRATCH.md:3` says *"Read at boot (after STATUS), refreshed at closeout."* `CLAUDE.md:28-39` BOOT lists steps 0→5b and **does not include SCRATCH**; the CLOSEOUT block (`:44-67`) does not write it either — the only charter mentions are `:45` (a ≥280-line SCRATCH-split trigger) and `:50` (the retirement rule). `PROME/registry/READS.tsv` has **no SCRATCH row** and its `ATTESTATION` row says `manifest-complete` for `BROCK:0-5b`. At 46,122 B (**142% of budget**) the answer matters. **And the file is behaving as if unwired:** `:4` reads `**Updated:** 2026-09-03` while the file was edited on 9/9 (`6c01f41a1`) and 9/12 (`578941311`). See R-K1/R-K4.
- **`docket/CATALYSTS.tsv` is the same class.** It exists (42 dated rows, 29,434 B) and STATUS routes readers to it (`:26`, `:123`), but no boot step reads it, it has no READS.tsv row, `ledger_staleness` lists it as outside its perimeter, and `CLAUDE.md:48` still describes it in the **future tense** — *"Phase 2 will replace this informal version with `docket/CATALYSTS.tsv`."* Its `date_class` column has accordingly drifted to 8 values including one blank (R-K3).
- **`domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` is in the silent-rot middle.** `**Last updated:** 2026-04-02` (`:3`) = **168 days**, no FROZEN banner, no two-clock header, not boot-read, and referenced only by one consumed inbox signal and one archived-class source memo — i.e. not by a live analytical or protocol doc. Root §Data Hygiene forbids exactly this state.
- 🔴 **Three live counts of the prediction ledger disagree.** The file holds **13 OPEN** rows; `workbook/PREDICTIONS_SCOREBOARD.md:7` grades *"SCORE (fully-resolved, n=10)"* stamped `Updated: 2026-07-09` (`:3`), 70 days behind — `BRK-27` resolved FALSE-ON-LETTER (8/28) and `BRK-30` RESOLVED-TRUE (9/3) are not in it. Hit rate (7/10 = 70%) and Brier (0.216) are stale by two rows. See R-K2.
- **`NEXUS_BRIEF.md` carries a superseded composite.** `:7` reads *"convergence **59/70** — HELD, nothing rescored 9/2"*; `STATUS.md:65` has read **57/70** since the 9/3 rescore. The cross-agent feed is 15 days stale and disagrees with the canonical surface on the headline number other desks consume.
- **`EXPECTED_SIGNALS.md` `Last reviewed: 2026-03-06`** (195 days, `:5`) and **`trade/NAMES.md` `Last Updated: 2026-05-01`** (139 days, `:3`) — both durable-method docs cited in the charter FILES table, neither frozen nor refreshed.
- **`CLAUDE.md:227-247` FILES table is behind the tree**: no `SCRATCH.md`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`, `docket/`, `board_log.tsv`, `registry/`, `tools/`, `workbook/{PC_REDEMPTION_REGISTER,PUBLISHED,PREDICTIONS_SCOREBOARD,PREDICTIONS_ARCHIVE}` — including `board_log.tsv`, which boot step 5 depends on.
- **`workbook/LEDGER_GLOB` does not exist**, so root closeout 1c-bis cannot nudge this desk against a declared ledger set — despite BROCK having twelve ledgers in `ledger_staleness`'s own perimeter.

**Floor-not-ceiling:** the `Category` taxonomy on VX, the `date_class` `modeled` token, the disposition enum on `board_log`, the `Action_If_Falsified` column and the ranked backlog are **rich local form, not divergence**. Do not normalise them away. *(That is a separate question from whether they are LINTED — see R-K3.)*

## 5. Load-bearing context / DO NOT TOUCH
- **`workbook/FLOW.tsv`'s 25-pathway grid IS the contagion engine.** It is the only durable home for the transmission model while there is no `thesis/`.
- **The shared-antecedent independence DISCIPLINE** — `STATUS.md:63` *"AI-unwind node (APO/ARES) = ONE vote inside cross-asset; NEXUS M-09 adds none. Q2 redemption wave (5 funds) = ONE vote."* Plus `:71`: *"OCIC hardens BOTH the redemption-gates and Blue Owl vectors; per the 6/26 shared-antecedent verdict that is ONE wave and I moved neither on it."* Any Independence-column formalisation must preserve this.
- **The 5-step THESIS-KILL DECISION TREE needs 2-of-3 reversals to override** (`STATUS.md:102`). Do not weaken to 1-of-3.
- **`trade/TRADE.md` is FROZEN and §9 lives in `STATUS.md` §5.** `BRK-25` and `BRK-26` cite §9 in their `Action_If_Falsified` fields — the citation target resolves through STATUS, not through the frozen file (`trade/TRADE.md:5`). Do not unfreeze, and do not delete the frozen file: §1–§8 are the record of how the position was reasoned.
- **Position truth is off-repo.** `STATUS.md:83` marks the APO Dec $95P at $0.05 on the 8/14 FORGE vintage and says so: *"14 DAYS STALE, a mark and not a close, and one of five rows marking at exactly $0.05 (FORGE D-21: not readable as realizable)."* Never resolve the position from STATUS or from `FORGE/PORTFOLIO.md` (frozen Feb-2026).
- **The two-clock ledger headers are load-bearing text, not decoration.** `ledger_staleness.py` parses `Last real data refresh:` first and scans the header block for RETIRED/SUPERSEDED as dead-banners — which is why `PC_REDEMPTION_REGISTER.tsv:1` opens with an explicit `# Status: LIVE` declaration *explaining* that its own gate-history prose contains those words. Reword that header and the ledger silently reclassifies as dead.
- **`board_log.tsv` and `workbook/PREDICTIONS.tsv` must NEVER be read whole** — 275% and 149% of budget. Use `cut -f2` / `grep` and `awk -F'\t' '$6~/OPEN|STUCK/'`. The charter states the arithmetic at both sites (`:32`, `:36`).
- **`git mv`, never bash `mv`, for the WALTER consume move** (`CLAUDE.md:38`) — bash `mv` leaves a dangling deletion in the shared index.
- **Pre-commit git-status check is BROCK-local and stricter than root** (`CLAUDE.md:55`): run `git status -- AGENTS/BROCK/` **and** `git diff --cached --stat` before every commit; installed after catching `AGENTS/SHADE/inbox/ATHENE_DEPOSIT_MAP.md` pre-staged by a concurrent session.
- **SIGNALS → WALTER, always.** `outbox/` is PROME-action-only (`CLAUDE.md:77`, `:247`). The direct-signal instruction that used to sit here was a route-around-WALTER defect, corrected 9/3.
- **`BRK-xx` prediction ids, no bare numbers** (`CLAUDE.md:109`) — collision guard across agents.
- **Cessions:** insurer NUMBERS → SHADE, EU seam → HANS, HY OAS → LIQUID, VIX → HENRY, bank scores → REGINALD. `STATUS.md:71` shows the discipline in action: *"Duration is the one candidate and I did not take it — LIQUID owns the 10Y series."*

## 6. Maturity snapshot
Grade + confidence live in `FLEET_MAP.tsv` (**not restated**; the row reads L4 / conf H, last_scored 2026-09-01). What this read establishes:
- **The 9/1 FLEET_MAP `Gaps` cell is stale in three cells.** It says *"Matrix 59/70"* — STATUS has read **57/70** since 9/3 (`:65`). It says *"byte budget cited (54,250 cap + 'never raise') but no declared budget block"* — the binding number is the **32,550 B budget** and STATUS now sits at **98%** of it, which the cap-framing hides; and the "no declared budget block" leg is superseded by a full 16-row READS manifest. It says *"Dark since 8/28"* — BROCK self-committed on 9/02, 9/03, 9/09 and 9/12 (31 self-commits in the period).
- `FLEET_MAP` `Next_upgrade` reads *"L5 blocker external; a declared byte-budget block (TERRY form) is the one cheap self-leg."* The **external** blocker (YEYOU) is now permanently unfireable — the seat was retired 2026-09-05, so the mechanical-QC leg *"zero YEYOU flags"* is **ruled N/A** (WQ-181 ② Will 9/10; recorded `runs/2026-09-14_L285_LADDER_INTEGRITY_PARTIAL.md:103`; encoded in the ladder table `AGENTS/DAEDALUS/CLAUDE.md:122` on 2026-09-17) — adjudicate L5 on the remaining legs. The **self** leg is CLOSED and over-delivered: BROCK filed a full READS.tsv manifest (9/12) rather than just a budget block.
- New residual self-legs this read surfaces: STATUS + LESSONS both at rotate-tier; no `thesis/` layer; `LEDGER_GLOB` absent; the SCRATCH/docket manifest gap; the prediction-count disagreement (R-K2); the unlinted `date_class` column (R-K3).
Work queue → `upgrades/BROCK_CARD.md`.

## 7. Open questions / comprehension gaps
1. **Is `SCRATCH.md` boot-read or not?** Three surfaces disagree (`SCRATCH.md:3` vs `CLAUDE.md:28-39`+`:44-67` vs the `manifest-complete` attestation in READS.tsv). At 46,122 B = 142% of budget, the answer decides whether this desk's boot is over cap. **NOT-ADJUDICATED** — it is the desk's call, not a reader's. *(The verification adds a fact the draft did not have: the closeout leg is unwired too, and the stamp has not moved through two sessions of edits.)*
2. **Is the APO Dec $95P still live?** `STATUS.md:83` last marks it at $0.05 on the 8/14 FORGE vintage, flagged 14 days stale at the time of writing (now 34). Off-repo truth; **do not resolve from STATUS or FORGE**.
3. **Does `BRK-02` resolve on the amortized-cost or fair-value basis?** BROCK found (`STATUS.md:108-110`) that OBDC discloses non-accruals on two bases that **moved in opposite directions over the same two quarters** — 2.3%→2.8% at amortized cost, 1.1%→0.8% at fair value — and that `BRK-02`'s letter does not name a basis. BROCK explicitly refused to settle it because *"the amortized-cost basis both fires my bearish prediction and is the one I believe analytically correct, and that coincidence is exactly the reason it is not mine to rule."* Flagged to PROME; **resolver date is 2026-09-30, thirteen days out.** This is the desk's single sharpest open item.
4. **Was the 9/18 CRMT date ever added to BROCK's OWN docket?** It is in `PROME/DOCKET.tsv:343` (verified). It is **not** in `AGENTS/BROCK/docket/CATALYSTS.tsv` (dates ≥9/13 are 9/15, 9/21, 9/30 ×2, 10/31, 11/13, 12/03, 2027-04-30). BROCK has been dark since 9/12 and the date is tomorrow.
5. **What does `EXPECTED_SIGNALS.md` still govern?** Last reviewed 3/06; it is named in the charter twice as the durable-method home, but no live citation to any specific rule in it was found from STATUS or the workbook. **CANNOT-EVALUATE** without a full read of the file against the current matrix.
6. **Does `PREDICTIONS_SCOREBOARD.md` have an owner-declared cadence?** It calls itself the calibration surface but carries no refresh rule and is 70 days behind, over a ledger whose OPEN count (13) it does not reflect. **NOT-ADJUDICATED.**

## 4 · 🔴 Findings the first reader missed — BROCK

| # | Pri | Finding | Locator |
|---|---|---|---|
| **R-K1** | 🔴 | **The desk's canonical "where are we" handoff is stamped 14 days stale over a 5-day-old body.** `SCRATCH.md:4` reads `**Updated:** 2026-09-03 Thu ~23:1x ET — SESSION CLOSED.` The file was edited on **2026-09-09** (`6c01f41a1`) and **2026-09-12** (`578941311`, a substantive correction to a DONE-THIS-SESSION line) with the stamp untouched. Its own `:3` promises *"refreshed at closeout"*; two closeouts since did not. A fresh body under a stale header is the inverse of `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]` and is worse here, because the next boot reads the stamp to decide how much to trust the file. The draft reported the manifest gap (K-6) but not that the file is visibly behaving as unwired | `AGENTS/BROCK/SCRATCH.md:3-4`; `git log -3 -- AGENTS/BROCK/SCRATCH.md` |
| **R-K2** | 🔴 | **Three live counts of one prediction ledger disagree, and the draft published a fourth.** The file holds **13 OPEN** rows (`awk -F'\t' 'NR>1{print $6}' … \| sort \| uniq -c`). `PREDICTIONS_SCOREBOARD.md:7` grades `n=10` fully-resolved, stamped 2026-07-09 (`:3`). The reader draft says "**11 OPEN**". A desk whose strongest dimension is its prediction loop has no single count of that loop | `AGENTS/BROCK/workbook/PREDICTIONS.tsv` Status col; `PREDICTIONS_SCOREBOARD.md:3`, `:7` |
| **R-K3** | 🟠 | **`docket/CATALYSTS.tsv`'s `date_class` is a state column with no enum, no lint and a blank cell.** Observed: `confirmed` 20 · `modeled` 12 · `hard` 6 · `estimated` 1 · `fired` 1 · `standing` 1 · `attempted-unresolved` 1 · **1 blank**. BROCK has no `kb_lint` equivalent, `ledger_staleness.py BROCK` names this file as outside its perimeter, and no boot step reads it. The profile draft describes the enum as `{hard, confirmed, modeled}` — the three the desk *intended*. A blank cell in a classification column passes every presence audit | `awk -F'\t' 'NR>1{print $NF}' AGENTS/BROCK/docket/CATALYSTS.tsv \| sort \| uniq -c`; `ledger_staleness.py BROCK` perimeter line |
| **R-K4** | 🟠 | **K-6 understates the SCRATCH gap by half.** `SCRATCH.md:3` claims *both* "Read at boot (after STATUS)" *and* "refreshed at closeout". The charter supports **neither**: BOOT (`CLAUDE.md:28-39`) has no SCRATCH step, and CLOSEOUT (`:44-67`) has none either — the only mentions are `:45` (a ≥280-line split trigger) and `:50` (the >60d retirement rule). So the fix is not "add a READS row"; it is to decide whether SCRATCH is a boot/closeout surface at all, and then wire or de-claim it in one edit | `AGENTS/BROCK/SCRATCH.md:3` vs `AGENTS/BROCK/CLAUDE.md:28-39`, `:44-67`, `:45`, `:50` |
| **R-K5** | 🟡 | **`board_log.tsv`'s disposition enum is 40% dead letters.** The spec (`CLAUDE.md:37`, BOARD_CONSUMPTION_SPEC v0.2) declares five tokens; across **121 rows** only three occur — `info-only` 47 · `acted` 42 · `noted` 32. `deferred` and `skipped` have never been used. Not a defect, but it means "skipped" as a consumption outcome has no observed instance, so the audit trail cannot distinguish "never deferred" from "deferral never logged" | `awk -F'\t' 'NR>1{print $3}' AGENTS/BROCK/board_log.tsv \| sort \| uniq -c` |

---

## 5 · Staleness-trigger machine-evaluability verdict

| Desk | Evaluable by a machine from named artifacts? | One-command form |
|---|---|---|
| **BOND** | **YES — all 6 legs.** Each names a file, and legs 1/2/4/5 are greps or a `ls \| wc -l`; leg 3 is an rc; leg 6 is a date. | `python3 scripts/read_cap_check.py --agent BOND >/dev/null; echo rc=$?; grep -c '^\*\*Version:\*\* 1\.2\.7' AGENTS/BOND/thesis/THESIS.md; sed -n 3p AGENTS/BOND/TRADE.md \| grep -c 2026-09-09; ls AGENTS/BOND/monitors/*.py \| wc -l; grep -c 'Composite: 12/35' AGENTS/BOND/STATUS.md` |
| **BROCK** | **YES — all 6 legs.** Leg 3 ("a directory `thesis/` appears") is the only one phrased as an existence test; `git ls-files` settles it. | `grep -c 'Convergence: 57/70' AGENTS/BROCK/STATUS.md; awk -F'\t' '$1=="BRK-02"{print $6}' AGENTS/BROCK/workbook/PREDICTIONS.tsv; git ls-files AGENTS/BROCK/thesis/ \| wc -l; python3 scripts/read_cap_check.py --agent BROCK >/dev/null; echo rc=$?; sed -n 1p AGENTS/BROCK/trade/TRADE.md \| grep -c '🧊 FROZEN'` |

⚠️ **One caveat on both:** leg 3 keys on `read_cap_check` rc, and that tool returns **rc=0 for both desks today for different reasons** — BROCK on an attested manifest, BOND on the charter heuristic with the printed caveat *"NOT a clean bill."* The trigger fires the same way; the two rc=0s do not mean the same thing. Do not read BOND's rc=0 as a perimeter guarantee.

---

*Verification pass: read-only. Nothing outside this file was written. No git mutation. Three `--selftest` entry points were executed (all documented as pure/no-I/O); no other script was run.*
